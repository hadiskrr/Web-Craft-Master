# Web Craft Master

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Version](https://img.shields.io/badge/version-2.0.0-informational.svg)
![CI](https://img.shields.io/github/actions/workflow/status/hadi-prv/web-craft-master/validate-skill.yml?branch=main&label=validate-skill)
![Claude Skill](https://img.shields.io/badge/claude-skill-6A5ACD.svg)

Skill maître qui rassemble dans un seul moteur de décision tout ce qu'il faut
pour concevoir, auditer, refondre, animer et rédiger des sites web et des
interfaces produit réellement prêts pour la production — pas des maquettes
qui donnent l'illusion d'être finies.

## Les cinq expertises fusionnées

| Expertise | Ce qu'elle apporte |
|---|---|
| **UI/UX** | Ergonomie avancée, design systems, accessibilité WCAG 2.2 AA/AAA, hiérarchie visuelle, psychologie utilisateur |
| **Tailwind CSS** | Architecture utilitaire moderne (v3/v4), layout mobile-first, dark mode natif, optimisation CSS |
| **Audit & Refonte** | Méthodologie d'audit heuristique, cartographie des frictions, grille de notation, plan d'action |
| **Rédaction** | Élimination des tics de langage artificiels, tonalité directe, naturelle et cohérente avec le projet |
| **Motion & Interfaces Fluides** | Springs interruptibles, suivi 1:1, momentum, rubber-banding, matériaux translucides, typographie optique |

## Pourquoi ce skill existe

La plupart des interfaces finissent par se ressembler : mêmes palettes,
mêmes cartes, mêmes effets, mêmes espacements et mêmes textes génériques.
`web-craft-master` impose une méthode stricte avant toute modification, afin
de produire des interfaces distinctives, cohérentes, accessibles et
réellement fonctionnelles.

## Pratiques bannies vs standard recommandé

| Catégorie | Banni | Standard imposé |
|---|---|---|
| Typographie | Inter, Geist, Space Grotesk | Plus Jakarta Sans / Outfit / Satoshi (SaaS), Cabinet Grotesk / General Sans (editorial), JetBrains Mono / Fira Code (code) |
| Titres & boutons | Emoji en titre ou CTA | SVG inline (`viewBox="0 0 24 24"`, `stroke="currentColor"`, 1.5px) |
| Animations | Flèches animées, hover flottant, particules, transitions CSS bloquantes sur geste | Springs interruptibles, suivi 1:1, handoff de vitesse, momentum, rubber-banding |
| Effets & fonds | Ombres lourdes, glassmorphism surchargé, dot grid, orbes flous, effets décoratifs | Hiérarchie par typographie, espace, contraste, bordures fines et matériaux translucides maîtrisés |
| Rédaction | Antithèses creuses, formules toutes faites, grandiloquence sans preuve | Phrases actives, faits concrets, verbes directs, texte adapté au contexte |
| Limites de scroll/drag | Arrêt brutal | Rubber-banding : résistance progressive et reprise fluide |

Les règles détaillées, exemples et checklists sont regroupés directement dans
[`SKILL.md`](SKILL.md) afin que le package reste autonome et simple à importer.

## Structure du dépôt

```
web-craft-master/
├── .claude-plugin/
│   └── plugin.json              # Manifeste du plugin
├── .github/
│   └── workflows/
│       └── validate-skill.yml   # Validation automatique à chaque push/PR
├── SKILL.md                     # Coeur du skill : règles, workflow, exemples
├── README.md                    # Ce fichier
├── LICENSE                      # Licence MIT
├── .editorconfig                # Règles d'édition communes
├── .gitattributes               # Normalisation Git des fichiers
├── .gitignore                   # Fichiers locaux exclus du dépôt
└── scripts/
    └── validate_skill.py        # Linter local
```

## Installation

### Claude Code (CLI)

```bash
claude plugin install ./web-craft-master
```

Ou directement depuis GitHub une fois le dépôt publié :

```bash
claude plugin install github:hadi-prv/web-craft-master
```

### Claude Desktop

1. Télécharger ou cloner ce dépôt.
2. Ouvrir Claude Desktop → Paramètres → Skills → **Importer un skill**.
3. Sélectionner le dossier `web-craft-master` ou le package `.skill` lorsque
   disponible.

### GitHub

Pour publier le projet :

```bash
git init
git add .
git commit -m "Initial release"
git branch -M main
git remote add origin https://github.com/hadi-prv/web-craft-master.git
git push -u origin main
```

Pour les mises à jour :

```bash
git add .
git commit -m "Update skill"
git push
```

## Validation locale

Avant toute publication, exécuter le linter :

```bash
python3 scripts/validate_skill.py .
```

Il vérifie :
- la structure du package et les fichiers obligatoires ;
- la validité de `.claude-plugin/plugin.json` et des fichiers JSON ;
- les chemins déclarés et les liens Markdown locaux ;
- l'absence de contenu incomplet ou de marqueurs non finalisés.

Le workflow `.github/workflows/validate-skill.yml` exécute la même
vérification automatiquement à chaque push et pull request.

## Exemples de prompts

```
Audite ce site et donne-moi un rapport complet avant de toucher au code.
```

```
Refonds cette landing page : elle a l'air générique, enlève tout ce qui
fait template et garde un seul CTA.
```

```
Écris le texte de cette section À propos avec une tonalité directe,
naturelle et adaptée au projet.
```

```
Implémente ce design en Tailwind CSS, mobile-first, avec dark mode natif.
```

```
Ajoute une bottom sheet qui se glisse au doigt, avec un comportement fluide,
interruptible, du rubber-banding aux bords et un respect de
prefers-reduced-motion.
```

## Licence

MIT - voir le fichier `LICENSE`.
