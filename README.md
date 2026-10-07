# web-craft-master

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Version](https://img.shields.io/badge/version-2.0.0-informational.svg)
![CI](https://img.shields.io/github/actions/workflow/status/hadi-prv/web-craft-master/validate-skill.yml?branch=main&label=validate-skill)
![Skill package](https://img.shields.io/badge/package-skill-4b5563.svg)

Skill maitre pour concevoir, auditer, refondre, animer et rediger des sites web
et des interfaces produit. Le package regroupe cinq expertises dans un meme
workflow : UI/UX, architecture Tailwind CSS, audit & refonte, redaction
naturelle et motion design inspire des interfaces Apple.

## Ce que le package couvre

| Expertise | Ce qu'elle apporte |
|---|---|
| **UI/UX** | Ergonomie, design systems, accessibilite WCAG 2.2, hierarchie visuelle |
| **Tailwind CSS** | Architecture utilitaire moderne (v3/v4), mobile-first, dark mode natif |
| **Audit & Refonte** | Cartographie, friction utilisateur, notation et plan d'action priorise |
| **Redaction naturelle** | Phrases directes, faits concrets, suppression des formulations convenues |
| **Motion design** | Springs interruptibles, suivi 1:1, momentum, rubber-banding et mouvement reduit |

## Principes de travail

Le package applique une priorite stricte :

**fonctionnalite -> securite -> clarte -> accessibilite -> performance -> SEO -> design -> motion**

Quelques regles structurantes :

- ne jamais inventer de contenu, de chiffres, de temoignages ou d'informations
  commerciales ;
- cartographier l'existant avant de modifier une architecture fonctionnelle ;
- conserver les fonctionnalites utiles au lieu de refaire le projet par principe ;
- utiliser un seul CTA principal par page ;
- privilegier la typographie, l'espace, le contraste et la composition ;
- reserver les animations aux changements d'etat, au feedback et aux interactions
  manipulables ;
- traiter les gestes avec des animations interruptibles et compatibles avec
  `prefers-reduced-motion`.

Les details et contre-exemples se trouvent dans
[`references/banned-patterns.md`](references/banned-patterns.md) et
[`references/apple-motion-guide.md`](references/apple-motion-guide.md).

## Structure du depot

```text
web-craft-master/
├── .claude-plugin/
│   └── plugin.json
├── .github/
│   └── workflows/
│       └── validate-skill.yml
├── .editorconfig
├── .gitattributes
├── .gitignore
├── LICENSE
├── README.md
├── SKILL.md
├── references/
│   ├── apple-motion-guide.md
│   ├── audit-framework.md
│   └── banned-patterns.md
└── scripts/
    └── validate_skill.py
```

## Installation

### Claude Code

Depuis une copie locale :

```bash
claude plugin install ./web-craft-master
```

Depuis un depot distant :

```bash
claude plugin install github:hadi-prv/web-craft-master
```

Le manifeste du package se trouve dans
`.claude-plugin/plugin.json`. La version actuelle declaree est `2.0.0`.

## Validation locale

Le package fournit un validateur sans dependance externe :

```bash
python3 scripts/validate_skill.py .
```

Il verifie notamment :

- les titres Markdown et les formulations bannies ;
- les marqueurs de contenu incomplet ;
- la validite des fichiers JSON ;
- la presence des fichiers essentiels du package ;
- les liens Markdown locaux ;
- la coherence des fichiers declares par le manifeste.

La meme verification est executee automatiquement par
`.github/workflows/validate-skill.yml`.

## Contribuer

Avant d'envoyer une modification :

1. conserver les conventions de structure et de nommage existantes ;
2. executer `python3 scripts/validate_skill.py .` ;
3. verifier que les fichiers references existent et que la documentation reste
   exacte.

Aucune dependance externe n'est requise pour la validation locale.

## Licence

Ce projet est distribue sous licence MIT. Voir [`LICENSE`](LICENSE).
