# Web Craft Master

Skill complète pour concevoir, auditer, refondre et améliorer des sites web et des interfaces produit.

## Objectif

Web Craft Master rassemble une méthode de travail unique dans `SKILL.md`. Le package est autonome : les règles, les guides, les exemples et les checklists sont regroupés dans un seul fichier.

## Couverture

| Domaine | Contenu |
|---|---|
| UI/UX | Hiérarchie visuelle, ergonomie, composants et design systems |
| Tailwind CSS | Architecture utilitaire, responsive, dark mode et états interactifs |
| Audit & refonte | Cartographie, notation, friction, priorisation et vérification finale |
| Rédaction | Texte direct, concret et cohérent avec le contexte du projet |
| Motion | Springs, suivi direct, interruption, momentum, rubber-banding et réduction du mouvement |
| Qualité web | Sécurité, SEO, performance, responsive et accessibilité |

## Ordre de priorité

**Fonctionnalité → sécurité → clarté → accessibilité → performance → SEO → design → motion**

## Structure

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
└── scripts/
    └── validate_skill.py
```

## Installation locale

Depuis le dossier parent du package :

```bash
claude plugin install ./web-craft-master
```

## Publication sur GitHub

### 1. Créer le dépôt

Sur GitHub, crée un dépôt vide nommé `web-craft-master`. Ne coche pas l'option qui ajoute automatiquement un README, une licence ou un `.gitignore` : ces fichiers sont déjà présents dans le package.

### 2. Ouvrir un terminal dans le package

```bash
cd web-craft-master
```

### 3. Initialiser Git et envoyer la première version

```bash
git init
git add .
git commit -m "Initial release"
git branch -M main
git remote add origin https://github.com/hadi-prv/web-craft-master.git
git push -u origin main
```

### 4. Vérifier le dépôt

Sur GitHub, tu dois retrouver `SKILL.md`, `README.md`, `LICENSE`, `.claude-plugin/plugin.json`, `scripts/validate_skill.py` et le workflow GitHub.

### 5. Mettre à jour le package

Après une modification :

```bash
git add .
git commit -m "Update skill"
git push
```

## Validation

Avant chaque publication, lance :

```bash
python3 scripts/validate_skill.py .
```

La validation contrôle la structure du package, les fichiers obligatoires, le manifeste, les fichiers JSON, les chemins déclarés et les liens Markdown locaux.

Le workflow `.github/workflows/validate-skill.yml` exécute également cette validation sur les pushes et les pull requests.

## Licence

MIT. Voir `LICENSE`.

## Maintenance

Toute évolution importante doit mettre à jour `SKILL.md`, conserver la structure du package et passer la validation locale.
