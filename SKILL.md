---
name: web-craft-master
description: >
  Utilise cette skill des qu'une tache touche a la conception, l'audit, la
  refonte, l'animation ou la redaction d'un site web ou d'une interface
  produit : "fais-moi une landing page", "audite ce site", "refonds ce
  projet", "rends ce design pro", "ecris le texte de cette page", "code ca
  en Tailwind", "verifie l'accessibilite", "ajoute des animations fluides
  a l'Apple", "ce site fait générique, corrige-le". Elle orchestre cinq expertises
  en une seule chaine : design UI/UX (WCAG 2.2, design systems),
  architecture Tailwind CSS (v3/v4, mobile-first, dark mode), methodologie
  d'audit heuristique (friction, notation, plan d'action), redaction
  redaction naturelle (suppression des tics synthetiques), et motion design a
  la Apple (springs, suivi 1:1, rubber-banding, materiaux translucides,
  typographie optique). Declenche-la meme sans le mot "audit" ou "design"
  si la demande decrit un de ces symptomes. Ne pas utiliser pour une
  question ponctuelle sans livrable (ex: "qu'est-ce que le CSS grid ?").
version: 2.0.0
author: hadi.prv
tags: [ui-ux, tailwindcss, audit, refonte, copywriting, accessibility, design-system, apple-motion, animation]
---

# Web Craft Master

Skill maitre qui fusionne cinq expertises complementaires en un seul moteur
de decision pour produire des interfaces et des sites **reellement**
exploitables — pas des maquettes qui donnent l'illusion d'etre finies, et
pas des animations qui impressionnent sans raison.

## Les cinq piliers

| Pilier | Ce qu'il apporte |
|---|---|
| **UI/UX Pro Max** | Ergonomie avancee, design systems, accessibilite WCAG 2.2 AA/AAA, hierarchie visuelle |
| **Tailwind CSS Master** | Architecture utilitaire moderne (v3/v4), mobile-first, dark mode natif |
| **Audit & Refonte** | Methodologie d'audit heuristique, cartographie des frictions, grille de notation, plan d'action |
| **Redaction humaine** | Elimination des formulations convenues, tonalite directe et naturelle |
| **Apple Design & Motion Fluids** | Springs, suivi 1:1, interruptibilite, momentum, rubber-banding, materiaux translucides, typographie optique, 8 principes Apple |

<rules>
1. Ne jamais inventer de contenu (temoignages, chiffres, logos, avis, informations commerciales). Une section sans contenu reel se supprime ou se repense, elle ne se remplit pas de texte factice.
2. Analyser l'architecture existante avant de modifier quoi que ce soit : pages, composants, scripts, appels API, formulaires, dependances.
3. Ne jamais faire une modification uniquement pour donner l'impression que le travail est termine. Si une correction exige un element hors de portee (hebergeur, DNS, cle API, service tiers), l'expliquer precisement plutot que de simuler une solution.
4. Un seul CTA principal par page ; les actions secondaires restent visuellement secondaires.
5. Priorite absolue et non negociable : fonctionnalite -> securite -> clarte -> accessibilite -> performance -> SEO -> design -> motion.
6. Chaque sortie textuelle (UI copy, documentation, rapport) suit les regles de <banned_patterns> redactionnels : pas de tics rédactionnels, pas de formules creuses.
7. Chaque sortie visuelle suit <design_system> : pas de style "landing page generique".
8. Toute animation ou interaction suit <apple_motion> : interruptible, basee sur des springs, jamais decorative sans fonction.
9. Ne jamais casser une fonctionnalite existante pour la rendre plus esthetique. Toute modification importante est suivie d'une verification (console, routes, responsive, `prefers-reduced-motion`).
10. Terminer toujours par un rapport structure (voir <workflow>, phase 6).
</rules>

<banned_patterns>
## Visuel — interdit
Degrades violet/noir, fond blanc pur, neons, pastels, couleurs arc-en-ciel,
bandes colorees decoratives, cartes de fonctionnalites generiques, grilles
bento, coins arrondis excessifs, drop shadows lourds (`shadow-2xl`,
`drop-shadow-xl`), glassmorphism surchargé / "liquid glass" non maitrise,
dot grid, orbes flous, etoiles decoratives, emoji dans les
titres/boutons, transformation automatique des listes en checkmarks.

Polices interdites : Inter, Geist, Space Grotesk.

## Animation & physique — interdit
Fleches animees qui rebondissent (`animate-bounce` sur un CTA), effets de
particules/neige decoratifs, transitions CSS `@keyframes` bloquantes et non
interruptibles sur un element manipulable au doigt/souris, hard-cut de
vitesse a la fin d'un drag, snap brutal sur une limite (sans
rubber-banding), animation qui ignore `prefers-reduced-motion`.

## Redactionnel — interdit
- Antitheses creuses : « Ce n'est pas X, c'est Y », « Il ne s'agit pas de X mais de Y »
- Tics d'ouverture artificiels : « Plongeons dans », « Dans le monde numerique d'aujourd'hui », « A l'ere de »
- Grandiloquence vide : « revolutionnaire », « inedit », « game-changer », « puissant » sans preuve
- Cloture artificielle : « En conclusion », « Pour resumer »
- Listes a trois elements systematiques ("rapide, simple et efficace")
- Attribution vague : « des experts affirment », « des etudes montrent » sans source

Remplacement : phrases actives, faits concrets, verbes directs, pas de
boursouflure. Detail complet + snippets avant/apres dans
`references/banned-patterns.md`.

## Techniques — interdit
- Validation JavaScript seule presentee comme suffisante pour la securite
- Fausse protection anti-spam uniquement visuelle
- Secrets (cles API, tokens, mots de passe) exposes cote front sans necessite
- ARIA ajoute sans besoin reel (le HTML semantique prime)
</banned_patterns>

<design_system>
La hierarchie visuelle repose sur : typographie, espace, composition,
contraste, structure, proportions, couleur maitrisee — jamais sur gradients,
ombres lourdes ou glassmorphism surcharge.

**Typographie de remplacement par contexte** (jamais Inter/Geist/Space Grotesk) :
| Contexte | Choix recommandes |
|---|---|
| SaaS / Tech | Plus Jakarta Sans, Outfit, Satoshi |
| Editorial / Haut de gamme | Cabinet Grotesk, General Sans |
| Code / Technique | JetBrains Mono, Fira Code |
| Optique a la Apple | `letter-spacing` et `line-height` ajustes selon la taille (voir `references/apple-motion-guide.md` §Typographie) — jamais une valeur fixe pour toutes les tailles |

**Icones** : SVG inline propres, `viewBox="0 0 24 24"`, `stroke="currentColor"`,
`stroke-width="1.5"` — jamais d'emoji en titre, bouton ou badge.

**Effets et fonds** : bordures fines (`border border-slate-200/80`) et ombres
tres legeres (`shadow-xs`/`shadow-sm`) a la place des ombres lourdes.
Materiaux translucides maitrises (`backdrop-filter: blur(20px)` + bordure
1px) pour les surfaces flottantes (nav, toolbars, sheets) — jamais plus
d'une surface translucide empilee sur une autre (la lisibilite s'effondre).

**Accessibilite** : WCAG 2.2 AA minimum (AAA quand demande) — contraste
4.5:1 texte normal / 3:1 texte large, cibles tactiles >= 44x44px, navigation
clavier complete, focus visible, structure semantique avant ARIA.

**Architecture Tailwind** : utilitaires mobile-first (`base -> sm -> md -> lg
-> xl`), dark mode natif via la variante `dark:`, composition par
`@apply` reservee aux motifs repetes, jamais de CSS arbitraire quand une
classe utilitaire standard existe deja.
</design_system>

<apple_motion>
Resume operationnel ; le guide complet est dans
`references/apple-motion-guide.md` et doit etre lu avant toute
implementation d'interaction geste-dependante (drag, swipe, sheet, carousel).

- **Reponse immediate** : feedback sur `pointerdown`, jamais sur `pointerup` seul.
- **Suivi 1:1** : un element traine colle au pointeur (Pointer Events + `setPointerCapture`), en respectant l'offset de prise.
- **Interruptibilite** : toute animation gesture-driven s'anime depuis sa valeur de presentation (live), jamais depuis la valeur cible ; jamais de `@keyframes`/transition CSS bloquante pour ce qui se manipule.
- **Springs, pas de durees fixes** : `damping 1.0` (critically damped) par defaut ; `damping ~0.8` uniquement quand le geste lui-meme portait du momentum (flick, throw).
- **Handoff de vitesse** : a la fin d'un drag, l'animation continue exactement a la vitesse du relachement.
- **Projection de momentum** : la cible se choisit par projection de la trajectoire (fonction de decay exponentiel), pas par la seule position de relachement.
- **Rubber-banding** : resistance progressive aux limites, jamais un arret net.
- **`prefers-reduced-motion`** : cross-fade a la place des springs/slides, jamais "aucun feedback".

Ces regles s'appliquent a toute interaction manipulable (drag, swipe,
bottom-sheet, carousel, slider) ; une simple transition d'apparition
(fade-in au chargement) n'a pas besoin de toute la machinerie spring, une
transition CSS sobre suffit.
</apple_motion>

<workflow>
## Phase 1 — Cadrage
Determiner la nature de la demande : creation (nouveau design/page), audit
(site existant a evaluer), refonte (site existant a corriger), animation
(interactions a rendre fluides), ou redaction (texte a humaniser). Une
demande peut combiner plusieurs phases dans l'ordre ci-dessous.

## Phase 2 — Audit (si site existant)
Suivre integralement `references/audit-framework.md` : cartographie,
grille de notation par categorie (y compris la fluidite des interactions),
friction utilisateur, plan d'action priorise. Ne rien corriger avant
d'avoir termine la cartographie.

## Phase 3 — System Design & Motion
Definir ou faire respecter un design system coherent (couleurs, typo,
espacements, composants) avant d'ecrire le moindre code. Pour toute
interaction geste-dependante, concevoir le comportement physique
(<apple_motion>) en meme temps que le visuel — jamais la motion ajoutee
apres coup. Verifier chaque choix contre `<design_system>`,
`<apple_motion>` et `references/banned-patterns.md`.

## Phase 4 — Integration Tailwind
Traduire le design system en classes utilitaires Tailwind (v3 ou v4 selon
le projet) : mobile-first, dark mode natif, etats interactifs
(`hover:`, `focus-visible:`, `active:`), grilles/flex responsives. Pour les
springs et le suivi de pointeur, utiliser JS (`requestAnimationFrame` /
Pointer Events / une librairie de spring comme Motion) en complement de
Tailwind pour le style statique — Tailwind seul ne fait pas de physique.

## Phase 5 — Redaction humaine
Toute copie (titres, boutons, meta description, pages legales, rapport
final inclus) passe par le filtre `<banned_patterns>` redactionnel. Relire
une fois le texte termine en cherchant specifiquement les tics listes.

## Phase 6 — Verification et rapport
Executer la checklist finale de `references/audit-framework.md`, incluant
la verification `prefers-reduced-motion` / `prefers-reduced-transparency`.
Produire un rapport avec exactement ces categories, dans cet ordre :

```
### CORRIGE
### AJOUTE
### OPTIMISE
### SECURITE
### SEO
### RESPONSIVE
### ACCESSIBILITE
### MOTION
### RESTE A FAIRE
```

Pour "RESTE A FAIRE" : uniquement ce qui necessite une intervention externe
(hebergeur, DNS, cle API, information juridique manquante), avec
l'explication precise de pourquoi ce point ne pouvait pas etre termine
avec le projet seul.
</workflow>

## Exemples d'execution (few-shot)

### Exemple 1 — Remplacer un emoji de titre par du SVG

**Avant (interdit)**
```html
<h2>🚀 Lancez votre projet</h2>
```

**Apres (conforme)**
```html
<h2 class="flex items-center gap-2 text-2xl font-semibold text-slate-900 dark:text-slate-100">
  <svg viewBox="0 0 24 24" class="h-6 w-6" fill="none" stroke="currentColor" stroke-width="1.5">
    <path stroke-linecap="round" stroke-linejoin="round" d="M4.5 16.5c-1.5 1.5-2 5-2 5s3.5-.5 5-2c.8-.8 1.5-2 .5-3-1-1-2.2-.3-3 .5Z" />
    <path stroke-linecap="round" stroke-linejoin="round" d="M15 9l-1.5 1.5m6-10.5c0 4-2 7-5 9l-3.5 3.5-4-4L10.5 10c2-3 5-5 9-5Z" />
  </svg>
  Lancez votre projet
</h2>
```

### Exemple 2 — Corriger un style redactionnel generique

**Avant (interdit)**
```
Dans le monde numerique d'aujourd'hui, il ne s'agit pas simplement de creer
un site, mais de reinventer l'experience utilisateur. Plongeons dans les
details de cette solution revolutionnaire.
```

**Apres (conforme)**
```
Un site lent perd des visiteurs dans les trois premieres secondes. Voici
ce que nous avons change, et pourquoi.
```

### Exemple 3 — Remplacer une carte "glassmorphism" surchargee par une surface Apple maitrisee

**Avant (interdit)**
```html
<div class="backdrop-blur-lg bg-white/30 shadow-2xl rounded-3xl border border-white/40 p-8">
```

**Apres (conforme)**
```html
<div class="bg-white/60 dark:bg-slate-900/60 backdrop-blur-xl shadow-sm rounded-lg border border-white/40 dark:border-white/10 p-8">
```

### Exemple 4 — Remplacer une animation decorative par un spring interruptible

**Avant (interdit — transition CSS bloquante sur un element glissable)**
```css
.sheet {
  transition: transform 300ms ease-in-out;
}
```
```js
sheet.style.transform = isOpen ? 'translateY(0)' : 'translateY(100%)';
```

**Apres (conforme — spring interruptible, anime depuis la valeur live)**
```js
import { animate } from 'motion';

function openSheet(el, velocity = 0) {
  animate(el, { y: 0 }, { type: 'spring', bounce: 0.2, duration: 0.3, velocity });
}
function closeSheet(el, velocity = 0) {
  animate(el, { y: '100%' }, { type: 'spring', bounce: 0, duration: 0.3, velocity });
}
// A l'interruption (nouveau pointerdown pendant l'animation), lire la
// position live de l'element et redemarrer l'animation depuis cette valeur
// plutot que depuis la cible — voir references/apple-motion-guide.md §3.
```

## Reference rapide

- `references/banned-patterns.md` — matrice complete interdits/remplacements, snippets SVG et Tailwind copiables, exemples redactionnels avant/apres.
- `references/apple-motion-guide.md` — guide pratique des springs, velocity handoff, projection de momentum, rubber-banding, materiaux translucides, typographie optique.
- `references/audit-framework.md` — grille d'audit complete (fonctionnel, securite, RGPD, SEO, performance, responsive, accessibilite, motion, redaction) et checklist finale.
- `scripts/validate_skill.py` — linter local : emoji dans les titres markdown, formulations bannies, validation JSON, marqueurs de contenu incomplet.
