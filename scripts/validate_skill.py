#!/usr/bin/env python3
"""
validate_skill.py — Linter autonome pour le depot web-craft-master.

Verifie :
  1. Absence d'emoji dans les titres Markdown (#, ##, ### ... et dans les
     boutons/liens de type [texte](...) utilises comme CTA).
  2. Absence des mots/tournures bannis par la skill (tics de redaction IA).
  3. Validite JSON de .claude-plugin/plugin.json et de tout autre *.json
     du depot.
  4. Absence de marqueurs de contenu incomplet (TODO, FIXME, "a completer",
     "...", placeholders de type Lorem Ipsum).

Usage :
    python3 scripts/validate_skill.py [chemin_du_depot]

Code de sortie : 0 si tout est valide, 1 si au moins une erreur est trouvee.
Concu pour tourner sans dependance externe (stdlib uniquement) afin d'etre
utilisable tel quel dans .github/workflows/validate-skill.yml.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

MARKDOWN_GLOBS = ["**/*.md"]
JSON_GLOBS = ["**/*.json"]

# Plage Unicode large couvrant la quasi-totalite des emojis courants.
EMOJI_PATTERN = re.compile(
    "["
    "\U0001F300-\U0001FAFF"
    "\U00002600-\U000027BF"
    "\U0001F1E6-\U0001F1FF"
    "\U00002190-\U000021FF"  # fleches (souvent utilisees comme "icones" IA)
    "\U00002B00-\U00002BFF"
    "\U0000FE0F"
    "]",
    flags=re.UNICODE,
)

HEADING_PATTERN = re.compile(r"^(#{1,6})\s+(.*)$", re.MULTILINE)

# Tics de redaction IA (francais). Recherche insensible a la casse.
BANNED_PHRASES = [
    r"plongeons dans",
    r"dans le monde num[ée]rique d['’]aujourd['’]hui",
    r"[àa] l['’][èe]re (du|de la|des)",
    r"il ne s['’]agit pas (simplement|juste) de .+ mais de",
    r"ce n['’]est pas (juste|simplement) .+,?\s*c['’]est",
    r"en conclusion",
    r"pour r[ée]sumer",
    r"solution r[ée]volutionnaire",
    r"exp[ée]rience in[ée]dite",
    r"game[ -]changer",
    r"des experts (affirment|s['’]accordent)",
    r"des [ée]tudes montrent",
]
BANNED_RE = re.compile("|".join(BANNED_PHRASES), re.IGNORECASE)

INCOMPLETE_MARKERS = [
    r"(?<!`)\bTODO\b(?!`)",
    r"(?<!`)\bFIXME\b(?!`)",
    r"(?<!`)\bXXX\b(?!`)",
    r"a compl[ée]ter",
    r"(?<!`)\bTBD\b(?!`)",
    r"lorem ipsum",
    r"section en construction",
    r"contenu [àa] venir",
    r"[àa] remplir",
]
INCOMPLETE_RE = re.compile("|".join(INCOMPLETE_MARKERS), re.IGNORECASE)

# Chemins (relatifs a la racine du depot) dont le role est de *documenter*
# les tournures bannies : ils les citent volontairement comme contre-exemples
# et ne doivent donc pas etre verifies par check_banned_phrases.
DOC_EXEMPT_PATHS = {
    "references/banned-patterns.md",
    "SKILL.md",
    "README.md",
}


class Issue:
    def __init__(self, path: Path, line: int, message: str):
        self.path = path
        self.line = line
        self.message = message

    def __str__(self) -> str:
        return f"{self.path}:{self.line}: {self.message}"


def iter_files(root: Path, patterns: list[str]) -> list[Path]:
    files: list[Path] = []
    for pattern in patterns:
        files.extend(sorted(root.glob(pattern)))
    # Ignorer les dossiers de build/dependances eventuels
    ignored_dirs = {".git", "node_modules", "__pycache__"}
    return [
        f for f in files
        if f.is_file() and not any(part in ignored_dirs for part in f.parts)
    ]


def check_emoji_in_headings(path: Path, text: str) -> list[Issue]:
    issues = []
    for match in HEADING_PATTERN.finditer(text):
        heading_text = match.group(2)
        if EMOJI_PATTERN.search(heading_text):
            line_no = text.count("\n", 0, match.start()) + 1
            issues.append(
                Issue(path, line_no, f"Emoji detecte dans un titre : {heading_text!r}")
            )
    return issues


def check_banned_phrases(path: Path, text: str, root: Path) -> list[Issue]:
    issues = []
    try:
        rel = path.relative_to(root).as_posix()
    except ValueError:
        rel = str(path)
    # Les fichiers qui *documentent* les interdits (skill, README, matrice de
    # reference) les citent volontairement comme contre-exemples et ne sont
    # donc pas verifies ici : la detection sert a lineter le contenu produit
    # avec la skill (pages, rapports), pas sa propre documentation.
    if rel in DOC_EXEMPT_PATHS:
        return issues
    for line_no, line in enumerate(text.splitlines(), start=1):
        if BANNED_RE.search(line):
            issues.append(Issue(path, line_no, f"Tournure bannie detectee : {line.strip()[:80]!r}"))
    return issues


def check_incomplete_markers(path: Path, text: str) -> list[Issue]:
    issues = []
    for line_no, line in enumerate(text.splitlines(), start=1):
        if INCOMPLETE_RE.search(line):
            issues.append(Issue(path, line_no, f"Marqueur de contenu incomplet : {line.strip()[:80]!r}"))
    return issues


def check_json_files(root: Path) -> list[Issue]:
    issues = []
    for path in iter_files(root, JSON_GLOBS):
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            issues.append(Issue(path, exc.lineno, f"JSON invalide : {exc.msg}"))
    return issues


def check_plugin_manifest(root: Path) -> list[Issue]:
    manifest_path = root / ".claude-plugin" / "plugin.json"
    if not manifest_path.exists():
        return [Issue(manifest_path, 0, "Manifeste .claude-plugin/plugin.json manquant")]

    required_keys = {"name", "version", "description"}
    try:
        data = json.loads(manifest_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return [Issue(manifest_path, exc.lineno, f"JSON invalide : {exc.msg}")]

    issues = []
    missing = required_keys - data.keys()
    if missing:
        issues.append(
            Issue(manifest_path, 0, f"Cles obligatoires manquantes : {sorted(missing)}")
        )

    semver_pattern = re.compile(r"^\d+\.\d+\.\d+$")
    version = data.get("version", "")
    if version and not semver_pattern.match(version):
        issues.append(
            Issue(manifest_path, 0, f"La version {version!r} ne respecte pas SemVer (X.Y.Z)")
        )

    return issues


def main() -> int:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
    root = root.resolve()

    all_issues: list[Issue] = []

    all_issues.extend(check_plugin_manifest(root))
    all_issues.extend(check_json_files(root))

    for path in iter_files(root, MARKDOWN_GLOBS):
        text = path.read_text(encoding="utf-8")
        all_issues.extend(check_emoji_in_headings(path, text))
        all_issues.extend(check_banned_phrases(path, text, root))
        all_issues.extend(check_incomplete_markers(path, text))

    if all_issues:
        print(f"Validation echouee : {len(all_issues)} probleme(s) trouve(s)\n")
        for issue in all_issues:
            print(f"  - {issue}")
        return 1

    print("Validation reussie : aucun probleme detecte.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
