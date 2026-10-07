---
name: web-craft-master
description: >
  Utilise cette skill des qu'une tache touche a la conception, l'audit, la
  refonte, l'animation ou la redaction d'un site web ou d'une interface
  produit : "fais-moi une landing page", "audite ce site", "refonds ce
  projet", "rends ce design pro", "ecris le texte de cette page", "code ca
  en Tailwind", "verifie l'accessibilite", "ajoute des animations fluides
  de façon fluide", "ce site fait générique, corrige-le". Elle orchestre cinq expertises
  en une seule chaine : design UI/UX (WCAG 2.2, design systems),
  architecture Tailwind CSS (v3/v4, mobile-first, dark mode), methodologie
  d'audit heuristique (friction, notation, plan d'action), redaction
  redaction naturelle (suppression des tics synthetiques), et motion design a
  la Motion (springs, suivi 1:1, rubber-banding, materiaux translucides,
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
| **Motion & Interfaces Fluides** | Springs, suivi 1:1, interruptibilite, momentum, rubber-banding, materiaux translucides, typographie optique, 8 principes Motion |

<rules>
1. Ne jamais inventer de contenu (temoignages, chiffres, logos, avis, informations commerciales). Une section sans contenu reel se supprime ou se repense, elle ne se remplit pas de texte factice.
2. Analyser l'architecture existante avant de modifier quoi que ce soit : pages, composants, scripts, appels API, formulaires, dependances.
3. Ne jamais faire une modification uniquement pour donner l'impression que le travail est termine. Si une correction exige un element hors de portee (hebergeur, DNS, cle API, service tiers), l'expliquer precisement plutot que de simuler une solution.
4. Un seul CTA principal par page ; les actions secondaires restent visuellement secondaires.
5. Priorite absolue et non negociable : fonctionnalite -> securite -> clarte -> accessibilite -> performance -> SEO -> design -> motion.
6. Chaque sortie textuelle (UI copy, documentation, rapport) suit les regles de <banned_patterns> redactionnels : pas de tics rédactionnels, pas de formules creuses.
7. Chaque sortie visuelle suit <design_system> : pas de style "landing page generique".
8. Toute animation ou interaction suit <motion_fluid> : interruptible, basee sur des springs, jamais decorative sans fonction.
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
la section « Motifs interdits et remplacements » de ce fichier.

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
| Optique de façon fluide | `letter-spacing` et `line-height` ajustes selon la taille (voir la section « Guide Motion & Interfaces Fluides » de ce fichier §Typographie) — jamais une valeur fixe pour toutes les tailles |

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

<motion_fluid>
Resume operationnel ; le guide complet est dans
la section « Guide Motion & Interfaces Fluides » de ce fichier et doit etre lu avant toute
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
</motion_fluid>

<workflow>
## Phase 1 — Cadrage
Determiner la nature de la demande : creation (nouveau design/page), audit
(site existant a evaluer), refonte (site existant a corriger), animation
(interactions a rendre fluides), ou redaction (texte a humaniser). Une
demande peut combiner plusieurs phases dans l'ordre ci-dessous.

## Phase 2 — Audit (si site existant)
Suivre integralement la section « Grille d’audit et de refonte » de ce fichier : cartographie,
grille de notation par categorie (y compris la fluidite des interactions),
friction utilisateur, plan d'action priorise. Ne rien corriger avant
d'avoir termine la cartographie.

## Phase 3 — System Design & Motion
Definir ou faire respecter un design system coherent (couleurs, typo,
espacements, composants) avant d'ecrire le moindre code. Pour toute
interaction geste-dependante, concevoir le comportement physique
(<motion_fluid>) en meme temps que le visuel — jamais la motion ajoutee
apres coup. Verifier chaque choix contre `<design_system>`,
`<motion_fluid>` et la section « Motifs interdits et remplacements » de ce fichier.

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
Executer la checklist finale de la section « Grille d’audit et de refonte » de ce fichier, incluant
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

### Exemple 3 — Remplacer une carte "glassmorphism" surchargée par une surface maîtrisée

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
// plutot que depuis la cible — voir la section « Guide Motion & Interfaces Fluides » de ce fichier §3.
```

## Index du skill

- **Motifs interdits et remplacements** : règles visuelles, rédactionnelles et techniques.
- **Motion & Interfaces Fluides** : principes de mouvement, interaction gestuelle et accessibilité du mouvement.
- **Grille d’audit et de refonte** : méthode d’audit, notation, priorisation et checklist finale.
- **Validation** : `scripts/validate_skill.py` vérifie la structure et l'intégrité du package.


# Guides intégrés

Cette section contient toute la documentation opérationnelle du package. Elle reste dans `SKILL.md` afin que la skill puisse être distribuée et lue comme un fichier autonome, sans dossier documentaire externe.

## Motifs interdits et remplacements

Guide intégré à `web-craft-master`. Chaque section explique
*pourquoi* le motif est banni, puis donne un remplacement copiable.

## 1. Typographie

**Pourquoi** : Inter, Geist et Space Grotesk sont devenues les polices par
defaut de tous les générateurs et templates SaaS. Leur omnipresence tue
toute identite visuelle distinctive.

| Contexte | Interdit | Remplacement |
|---|---|---|
| SaaS / Tech | Inter, Geist | Plus Jakarta Sans, Outfit, Satoshi |
| Editorial / Haut de gamme | Inter | Cabinet Grotesk, General Sans |
| Code / Technique | — | JetBrains Mono, Fira Code |

**Interdit egalement** : une valeur de `letter-spacing`/`line-height` fixe
appliquee a toutes les tailles de texte. Le tracking et le leading doivent
etre specifiques a la taille (negatif et serre sur les grands titres, pres
de zero et plus ample sur le corps de texte) — voir
la section « Typographie — taille optique, tracking, leading » pour le detail et les valeurs.

```css
/* Avant */
font-family: "Inter", sans-serif;

/* Apres */
font-family: "Plus Jakarta Sans", sans-serif;
```

## 2. Emoji dans les titres et boutons

**Pourquoi** : un emoji en titre signale instantanement un contenu standardisé
sans direction artistique. Une icone vectorielle est controlable (couleur,
epaisseur, taille) et coherente avec le design system ; un emoji depend du
rendu de la plateforme de l'utilisateur.

**Interdit**
```html
<h2>🚀 Demarrez maintenant</h2>
<button>✅ Valider</button>
```

**Remplacement — gabarit SVG reutilisable**
```html
<svg viewBox="0 0 24 24" class="h-5 w-5" fill="none" stroke="currentColor" stroke-width="1.5">
  <path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7" />
</svg>
```
Regle de construction : `viewBox="0 0 24 24"`, `fill="none"`,
`stroke="currentColor"` (herite la couleur du texte parent, compatible dark
mode automatiquement), `stroke-width="1.5"` pour un trait moyen qui ne
s'epaissit pas en petite taille.

Quelques icones de base, pretes a copier :

```html
<!-- Fleche (navigation, pas pour un CTA animee) -->
<svg viewBox="0 0 24 24" class="h-5 w-5" fill="none" stroke="currentColor" stroke-width="1.5">
  <path stroke-linecap="round" stroke-linejoin="round" d="M13.5 4.5 21 12m0 0-7.5 7.5M21 12H3" />
</svg>

<!-- Coche (validation de formulaire, pas en liste systematique) -->
<svg viewBox="0 0 24 24" class="h-5 w-5" fill="none" stroke="currentColor" stroke-width="1.5">
  <path stroke-linecap="round" stroke-linejoin="round" d="m4.5 12.75 6 6 9-13.5" />
</svg>

<!-- Alerte -->
<svg viewBox="0 0 24 24" class="h-5 w-5" fill="none" stroke="currentColor" stroke-width="1.5">
  <path stroke-linecap="round" stroke-linejoin="round" d="M12 9v3.75m9-.75a9 9 0 1 1-18 0 9 9 0 0 1 18 0Zm-8.99 4.5h.01" />
</svg>

<!-- Fermer -->
<svg viewBox="0 0 24 24" class="h-5 w-5" fill="none" stroke="currentColor" stroke-width="1.5">
  <path stroke-linecap="round" stroke-linejoin="round" d="M6 18 18 6M6 6l12 12" />
</svg>
```

## 3. Animations & physique

**Pourquoi** : les fleches qui rebondissent, les elements qui flottent au
survol et les transitions decoratives partout sont le signal visuel le
plus reconnaissable d'un template standardisé. Elles n'apportent
aucune information a l'utilisateur. Sur tout element **manipulable**
(drag, swipe, sheet), une transition CSS classique est en plus un defaut
fonctionnel : elle ne peut pas etre saisie et inversee en plein vol — voir
la section « Interruptibilité — le principe le plus important ».

| Interdit | Remplacement |
|---|---|
| `animate-bounce` sur une fleche de CTA | Pas d'animation sur l'icone ; `transition-colors duration-150` sur le bouton lui-meme |
| `hover:-translate-y-2 hover:scale-105` sur une carte | `hover:border-slate-300 transition-colors duration-150` |
| Particules / neige / effets de fond animes | Aucun. Fond uni ou texture statique tres discrete |
| Transition d'entree sur chaque bloc au scroll | Reserver aux changements d'etat reels (ouverture menu, validation formulaire) |
| `transition: transform 300ms ease` sur un sheet/drawer glissable | Spring interruptible (`type: 'spring'`), anime depuis la valeur live — voir la section « Guide Motion & Interfaces Fluides » ci-dessous §3-4 |
| Snap brutal sur une limite de scroll/drag | Rubber-banding : resistance progressive (la section « Rubber-banding — limites souples ») |
| Vitesse coupee net a la fin d'un drag | Handoff de vitesse vers le spring d'atterrissage (la section « Handoff de vitesse — la jonction entre drag et animation ») |

```html
<!-- Avant -->
<button class="transition-transform hover:scale-110 hover:shadow-2xl">
  Commencer <span class="inline-block animate-bounce">→</span>
</button>

<!-- Apres -->
<button class="transition-colors duration-200 ease-out hover:bg-slate-800">
  Commencer
</button>
```

```js
// Avant : transition CSS bloquante sur un sheet glissable (non interruptible)
sheet.style.transition = 'transform 300ms ease-in-out';
sheet.style.transform = isOpen ? 'translateY(0)' : 'translateY(100%)';

// Apres : spring interruptible, part de la valeur live, recoit la vitesse du geste
import { animate } from 'motion';
animate(sheet, { y: isOpen ? 0 : '100%' }, {
  type: 'spring',
  bounce: isOpen ? 0.2 : 0,
  duration: 0.3,
  velocity: releaseVelocity,
});
```

## 4. Ombres, verre et fonds decoratifs

**Pourquoi** : un glassmorphism surcharge (flou excessif + ombre lourde +
coins trop arrondis) est le signal visuel generique le plus repandu. Un
materiau translucide maitrise de façon fluide (flou mesure, bordure fine,
une seule couche) encode une hierarchie reelle sans tomber dans l'effet
template.

| Interdit | Remplacement |
|---|---|
| `shadow-2xl`, `drop-shadow-xl` | `shadow-xs` ou `shadow-sm` |
| `backdrop-blur-lg bg-white/30 shadow-2xl rounded-3xl` (glassmorphism surcharge) | `backdrop-filter: blur(20px)` + fond semi-transparent **unique** + bordure 1px, sans ombre lourde — voir la section « Guide Motion & Interfaces Fluides » ci-dessous §12 |
| Empiler deux surfaces translucides l'une sur l'autre | Jamais : la lisibilite s'effondre. Une seule couche translucide a la fois, le reste en surface solide |
| Fond en grille de points (`bg-[radial-gradient(...)]` repete) | Fond uni, ou separation par `border-t` |
| Degrade violet/noir plein ecran | Palette maitrisee a 2-3 teintes, utilisee en aplat |
| Orbes flous decoratifs (`blur-3xl` en fond) | Supprimer ; la hierarchie vient de la typographie et de l'espace |
| Bordure dure (`border-b`) sous une barre flottante sticky | Effet de bord au scroll : flou/degrade discret uniquement la ou le contenu passe sous le chrome |

```html
<!-- Avant : glassmorphism surcharge -->
<div class="backdrop-blur-lg bg-white/30 shadow-2xl rounded-3xl border border-white/40 p-8">
  ...
</div>

<!-- Apres (option sobre) : surface nette, sans translucidite -->
<div class="bg-white dark:bg-slate-900 rounded-lg border border-slate-200/80 dark:border-slate-800 shadow-sm p-8">
  ...
</div>

<!-- Apres (option materiau Motion) : translucidite maitrisee, une seule couche -->
<div class="bg-white/60 dark:bg-slate-900/60 backdrop-blur-xl rounded-lg border border-white/40 dark:border-white/10 shadow-sm p-8">
  ...
</div>
```

## 5. Layouts generiques

**Pourquoi** : les grilles bento et les "cartes de fonctionnalites" a trois
colonnes identiques sont devenues la structure par defaut de tout générateur
de landing page. Elles produisent des pages interchangeables.

| Interdit | Remplacement |
|---|---|
| Grille bento (blocs de tailles aleatoires sans logique de lecture) | Grille reguliere `grid-cols-12` avec une vraie hierarchie de contenu |
| 3 cartes identiques "Rapide / Simple / Securise" | Un argument developpe par section, avec un exemple concret |
| Un CTA different et voyant par section | Un seul CTA principal repete a l'identique, les autres actions en lien texte |

## 6. Redaction — tics de redaction artificiels

**Pourquoi** : ces tournures sont statistiquement sur-representees dans le
texte genere et desensibilisent le lecteur des la premiere phrase.

| Categorie | Exemples interdits | Remplacement |
|---|---|---|
| Antithese creuse | « Ce n'est pas juste un site, c'est une experience » | Decrire le fait directement : « Le site charge en 1,2s sur mobile » |
| Ouverture pompeuse | « Dans le monde numerique d'aujourd'hui... », « Plongeons dans... » | Commencer par le fait ou le probleme concret |
| Grandiloquence | « solution revolutionnaire », « experience inedite » | Nommer ce que ca fait, pas ce que ca pretend etre |
| Cloture artificielle | « En conclusion », « Pour resumer » | Terminer sur l'information la plus utile, sans meta-commentaire |
| Attribution vague | « des experts s'accordent a dire » | Citer la source precise ou supprimer l'affirmation |
| Rule of three systematique | « rapide, simple et efficace » | Un seul adjectif precis, ou une phrase factuelle |
| Listes en checkmarks par reflexe | ✓ partout meme pour des phrases non booleennes | Puces simples `-`, checkmarks reserves a un etat reellement valide/invalide |

**Exemple complet avant/apres**

Avant :
> Dans le monde numerique d'aujourd'hui, il ne s'agit pas simplement de
> creer un site, mais de reinventer l'experience utilisateur. Notre solution
> revolutionnaire combine rapidite, simplicite et efficacite. En conclusion,
> rejoignez les experts qui nous font deja confiance.

Apres :
> Un site lent perd des visiteurs des les trois premieres secondes. Celui-ci
> charge en moins d'une seconde sur mobile, sans javascript bloquant.

## 7. Securite — fausses solutions

| Interdit | Remplacement reel |
|---|---|
| Validation JS presentee comme securite suffisante | Validation JS pour l'UX + validation serveur obligatoire si un backend existe |
| Compteur JS cote client comme "rate limiting" | Rate limiting serveur (middleware, reverse proxy, service managé) — a documenter comme "reste a faire" si absent du projet |
| Bouton honeypot visible ou case a cocher "je ne suis pas un robot" sans verification reelle | Honeypot invisible + throttling serveur, ou captcha reel (hCaptcha/Turnstile) |
| Cle API visible dans le bundle front | Appel proxifie via un endpoint serveur qui detient la cle |

## Guide Motion & Interfaces Fluides

Traduction operationnelle, pour le web, des principes exposes par Motion dans
*Designing Fluid Interfaces* (WWDC 2018), *The Details of UI Typography*
(WWDC 2020), *Designing Audio-Haptic Experiences*, et *Principles of Great
Design* (WWDC 2026). A lire avant toute implementation d'interaction
geste-dependante (drag, swipe, bottom-sheet, carousel, slider).

Fil conducteur : **une interface est vivante quand le mouvement part de la
valeur actuellement affichee, herite la vitesse de l'utilisateur, projette
le momentum en avant, et peut etre saisie puis inversee a tout instant.**
Les springs sont l'outil qui rend tout cela naturel, parce qu'ils sont par
nature interruptibles et sensibles a la vitesse.

## 1. Reponse — tuer la latence

Des que le lag apparait, la sensation de controle direct s'effondre.

- Reagir sur `pointerdown`, jamais en attendant `pointerup`.
- Auditer chaque latence sur le chemin de l'input : debounces, timers
  artificiels, attentes de transition, delai de tap ~300ms.
- Le feedback doit etre continu pendant le geste, pas seulement a la fin :
  pour un drag/slider/drawer, mettre a jour l'UI 1:1 avec le pointeur
  pendant toute la duree, jamais seulement a la liberation.

```css
/* Feedback instantane sur l'appui */
.button:active {
  transform: scale(0.97);
  transition: transform 100ms ease-out;
}
```

## 2. Manipulation directe — suivi 1:1

L'element traine doit rester colle au pointeur, en respectant l'offset de
prise (pas de recentrage brutal sur le centre de l'element au grab).

```js
el.addEventListener('pointerdown', (e) => {
  el.setPointerCapture(e.pointerId);
  const grabOffset = e.clientY - el.getBoundingClientRect().top;
  // suivre position + timestamp pour calculer la vitesse au relachement
});
```

Utiliser Pointer Events avec `setPointerCapture` pour que le suivi continue
meme si le pointeur sort des limites de l'element. Garder un historique
court position/temps (quelques `pointermove`) pour calculer la vitesse a la
liberation.

## 3. Interruptibilite — le principe le plus important

Toute animation doit pouvoir etre saisie et inversee a tout moment, sans
attendre qu'elle se termine.

- Ne jamais bloquer l'input pendant une transition.
- Toujours animer depuis la valeur de **presentation** (l'etat affiche a
  l'ecran), jamais depuis la valeur cible — lire le transform live de
  l'element a l'interruption.
- Eviter les transitions CSS et `@keyframes` pour tout ce qui est
  geste-dependant : elles ne peuvent pas etre saisies et inversees en
  douceur en plein vol. Les springs animent depuis la valeur courante par
  defaut.
- Quand un geste s'inverse, fondre la vitesse — jamais de coupure nette
  (effet "mur de brique"). Choisir une librairie de spring qui reporte la
  vitesse lors d'un re-ciblage.
- Decomposer un mouvement 2D en deux springs independants (X et Y) : un
  seul spring sur une distance 2D se desynchronise quand X et Y ont des
  vitesses differentes.

## 4. Comportement plutot qu'animation — utiliser des springs

Penser en deux parametres, pas en triplet physique masse/raideur/amortissement :

- **Damping ratio** (amortissement) — controle le depassement.
  `1.0` = critically damped, pas de rebond, arret net et propre.
  `< 1.0` = depasse et oscille. Plus bas = plus de rebond.
- **Response** — vitesse pour atteindre la cible, en secondes. Plus bas =
  plus vif. Ce n'est **pas** une duree fixe : le temps d'arret emerge des
  parametres, il n'est pas prescrit.

**Valeurs par defaut**
- Commencer la majorite de l'UI a **damping `1.0`** (critically damped) —
  sobre et non distrayant.
- N'ajouter du rebond (**damping ~`0.8`**) que lorsque le geste lui-meme
  portait du momentum (un flick, un lancer, un relachement de drag).

**Valeurs concretes livrees par Motion**

| Interaction | Damping | Response |
|---|---|---|
| Deplacement / repositionnement (ex. PiP) | `1.0` | `0.4` |
| Rotation | `0.8` | `0.4` |
| Tiroir / feuille (sheet) | `0.8` | `0.3` |

```js
import { animate } from 'motion';

// Critically damped par defaut (sans depassement)
animate(el, { y: 0 }, { type: 'spring', bounce: 0, duration: 0.4 });

// Interaction a momentum — un peu de rebond, uniquement parce qu'un flick a precede
animate(el, { y: target }, { type: 'spring', bounce: 0.2, duration: 0.4 });
```

## 5. Handoff de vitesse — la jonction entre drag et animation

A la fin d'un geste, l'animation doit continuer **exactement a la vitesse
du doigt/pointeur au relachement**, sans couture visible entre le drag et
l'animation. C'est le detail qui separe le plus "fluide" de "correct".

```
vitesseRelative = vitesseGeste / (valeurCible − valeurActuelle)
```

Exemple : element a `y=50`, cible `y=150` (100px a parcourir), doigt a
50px/s -> vitesse initiale du spring = `50 / 100 = 0.5`. La plupart des
librairies (Motion/Framer Motion) acceptent directement la vitesse absolue
en px/s via l'option `velocity`.

## 6. Projection de momentum — viser ou le geste se dirige

Ne pas snapper vers la limite la plus proche du point de relachement.
Utiliser la vitesse pour **projeter la position de repos** (exactement
comme la deceleration du scroll), puis snapper vers la cible la plus proche
de ce point projete.

```js
// decelerationRate ≈ 0.998 pour un scroll normal ; 0.99 pour plus vif
function project(initialVelocity /* px/s */, decelerationRate = 0.998) {
  return (initialVelocity / 1000) * decelerationRate / (1 - decelerationRate);
}

const projectedEndpoint = currentPosition + project(releaseVelocity);
const target = nearestSnapPoint(projectedEndpoint);
animateSpringTo(target, { velocity: releaseVelocity });
```

Important : la formule textbook `v²/(2·decel)` n'est **pas** celle
utilisee par Motion — utiliser la forme en decay exponentiel ci-dessus.

## 7. Coherence spatiale — trajectoires symetriques, origines ancrees

- Entree et sortie suivent le meme chemin : un panneau qui entre par la
  droite doit sortir par la droite.
- Ancrer les interactions a leur source : un menu/popover/sheet doit
  sembler provenir de l'element qui l'a declenche (`transform-origin` sur
  le declencheur, pas le centre de l'ecran).
- Miroir de l'easing sur les transitions reversibles : la courbe de sortie
  doit etre l'inverse de la courbe d'entree.

## 8. Orienter dans la direction du geste

Les mouvements intermediaires doivent indiquer ou les choses se dirigent,
pas juste interpoler aveuglement vers la cible finale.

## 9. Rubber-banding — limites souples

A une limite, resister progressivement plutot que s'arreter net. Un arret
dur se lit comme "fige" ; une resistance continue se lit comme "reactif,
mais il n'y a rien de plus ici".

```js
// Plus on depasse la limite, moins l'element suit — comme un objet reel qui ralentit avant de s'arreter
function rubberband(overshoot, dimension, constant = 0.55) {
  return (overshoot * dimension * constant) / (dimension + constant * Math.abs(overshoot));
}
```

## 10. Details de conception du geste

- **Tap** : surbrillance au toucher (instantane), validation au relachement.
  Ajouter ~10px d'hysteresis/zone de tolerance, permettre l'annulation en
  glissant hors de la cible.
- **Drag/swipe** : exiger un petit seuil de mouvement (~10px) avant de
  s'engager dans une direction, puis suivre 1:1.
- Detecter tous les gestes plausibles en parallele des le premier
  mouvement, puis annuler les perdants une fois l'intention claire. Eviter
  les recognizers qui ne rapportent qu'un etat final (type
  `swipeleft`) : ils jettent le suivi continu necessaire au feedback.
- Minimiser les delais de desambiguisation : la detection de double-tap
  retarde toujours le tap simple ; ne payer ce cout que si le double-tap
  existe reellement.

## 11. Fluidite au niveau de la frame

- Garder le changement de position par frame sous le seuil de perception
  pour eviter le "strobing".
- Pour un mouvement tres rapide, un leger flou de mouvement encode la
  vitesse mieux qu'un trait net et dur.
- `requestAnimationFrame` est l'horloge synchronisee a l'ecran du web.
  N'animer que des proprietes compositor-friendly (`transform`, `opacity`)
  et indiquer `will-change` quand le mouvement est imminent.

## 12. Materiaux & profondeur — la translucidite encode la hierarchie

- Construire nav/toolbars/sheets comme des couches translucides
  (`backdrop-filter: blur()` + fond semi-transparent) avec le contenu qui
  defile dessous — pas des barres opaques qui consomment un espace fixe.
- Le poids du materiau encode la hierarchie : plus sombre/epais pour les
  regions structurelles (sidebars), plus leger pour attirer l'attention sur
  les elements interactifs (boutons). Ne jamais empiler une surface
  translucide legere sur une autre — la lisibilite s'effondre.
- Les grandes surfaces doivent paraitre plus epaisses : flou plus fort +
  ombre plus profonde que les petits elements (chips).
- Assombrir pour focaliser, separer pour garder le flux : une tache modale
  associe la surface a un scrim d'assombrissement et repousse l'arriere-plan.
  Un panneau parallele non bloquant utilise la translucidite et un offset
  **sans** scrim pour ne pas casser le flux.
- La vibrance garde le texte lisible sur fond changeant : sur une surface
  translucide, eviter le gris plat — utiliser un contraste plus eleve, un
  poids legerement plus fort, et un leger `letter-spacing`. Mettre la
  couleur sur une couche solide, pas sur le premier plan translucide.
- Effets de bord au scroll plutot que des separateurs francs : un flou/
  degrade discret ou le contenu rencontre le chrome flottant, pas une
  bordure de 1px.
- Materialiser, pas juste fondre : pour une surface en verre/flou, animer
  le rayon de flou et l'echelle ensemble a l'entree/sortie.

```css
.toolbar {
  background: rgba(255, 255, 255, 0.6);
  backdrop-filter: blur(20px) saturate(180%);
  border-top: 1px solid rgba(255, 255, 255, 0.4); /* bord clair = la lumiere accroche le materiau */
}
```

## 13. Feedback multimodal — mouvement + son + haptique

1. **Causalite** — il doit etre evident ce qui a cause le feedback.
   Declencher sur l'evenement causal reel (le toggle qui bascule, l'element
   qui s'enclenche), et faire correspondre son caractere a la physicalite
   de l'action.
2. **Harmonie** — le visuel, le son et l'haptique doivent se declencher sur
   la **meme frame**. Une latence entre eux detruit l'illusion.
3. **Utilite** — n'ajouter du feedback que la ou il gagne sa place. Le
   reserver aux moments significatifs (succes, erreur, validation,
   enclenchement). Trop de feedback entraine les gens a tout ignorer.

## 14. Mouvement reduit & accessibilite

Le mouvement reduit ne signifie pas "aucun feedback" — un equivalent plus
doux, non vestibulaire.

- `prefers-reduced-motion: reduce` -> remplacer les glissements/springs/
  parallax par de courts fondus d'opacite. Supprimer l'elastique/depassement.
  Garder les changements d'opacite/couleur qui aident la comprehension.
- `prefers-reduced-transparency: reduce` -> rendre les surfaces
  translucides plus "givrees"/solides : augmenter l'opacite du fond,
  reduire le flou.
- `prefers-contrast: more` -> fonds quasi solides avec une bordure
  definie et contrastee.

Eviter aussi : les arriere-plans en mouvement plein ecran, les oscillations
lentes en boucle (~0.2 Hz), les sauts de luminosite brusques (adoucir les
changements de theme clair/sombre).

```css
@media (prefers-reduced-motion: reduce) {
  .sheet { transition: opacity 200ms ease; transform: none !important; }
}
@media (prefers-reduced-transparency: reduce) {
  .toolbar { background: white; backdrop-filter: none; }
}
```

## 15. Typographie — taille optique, tracking, leading

- Le tracking (`letter-spacing`) est specifique a la taille — jamais une
  seule valeur pour toutes les tailles. Le grand texte d'affichage veut un
  tracking **negatif** ; le petit texte veut un tracking legerement
  **positif** pour la lisibilite.
- Le leading (`line-height`) varie inversement a la taille : serre sur les
  grands titres, plus ample sur le corps de texte.
- Construire la hierarchie a partir du poids + taille + leading ensemble,
  pas de la taille seule.
- Respecter le reglage de taille de texte de l'utilisateur (Dynamic Type
  equivalent web) : espacer en `rem`/`em`, pas en px fixes.
- Preferer la police systeme avant une police custom quand c'est possible :
  elle embarque deja le reglage optique et les tables de tracking.

```css
:root { font: 100%/1.5 system-ui, sans-serif; }

.display {
  font-size: clamp(2rem, 5vw, 4rem);
  line-height: 1.05;
  letter-spacing: -0.02em;
  font-optical-sizing: auto;
}
```

## 16. Les 8 principes de conception

1. **Purpose (intention)** — construire avec intention ; decider ce qu'on
   ne construit pas. Chaque fonctionnalite demande du temps, de
   l'attention et de la confiance a l'utilisateur.
2. **Agency (controle)** — laisser le controle aux gens : proposer des
   choix, ne pas forcer un chemin unique. Offrir l'annulation facile ;
   reserver la confirmation aux actions reellement destructives et
   irreversibles.
3. **Responsibility (responsabilite)** — agir dans l'interet de
   l'utilisateur. Vie privee : demander au bon moment, seulement ce qui
   est necessaire, de maniere transparente. Securite : anticiper les abus
   et dommages possibles, en particulier avec les systèmes automatisés.
4. **Familiarity (familiarite)** — s'appuyer sur ce que les gens
   connaissent deja. Utiliser des metaphores ni trop litterales ni trop
   abstraites, respecter leur physique. Rester coherent : ce qui se
   ressemble doit se comporter pareil et vivre au meme endroit.
5. **Flexibility (flexibilite)** — concevoir pour differents contextes,
   appareils et capacites. S'adapter a la plateforme et a la situation ;
   permettre la personnalisation quand aucune disposition unique ne
   convient a tous.
6. **Simplicity (simplicite, pas minimalisme)** — retirer le superflu pour
   que le but principal brille. Etre concis (langage simple, pas de
   jargon, moins d'etapes) et clair (hierarchie par ordre, espacement,
   contraste). Montrer le chemin commun d'abord, les options avancees un
   niveau plus bas.
7. **Craft (soin du detail)** — attention sans compromis : typographie
   soignee, couleurs qui s'adaptent clair/sombre, iconographie claire,
   animations reactives et naturelles. Rien n'est laisse au hasard —
   chaque espacement, timing et alignement est un choix deliberable.
8. **Delight (plaisir)** — le resultat d'avoir reussi les sept autres
   principes, pas un effet ajoute en surface. Decider de l'emotion
   recherchee (calme, confiance, enthousiasme) et la renforcer dans chaque
   decision.

**Regles tactiques associees**

- Le feedback existe en quatre types : statut, achevement, avertissement,
  erreur. Confirmer les actions significatives, exposer le statut en
  cours, avertir avant les problemes, valider en ligne (pas seulement a
  la soumission).
- Wayfinding : chaque ecran doit repondre a "Ou suis-je ? Ou puis-je
  aller ? Qu'y a-t-il ici ? Comment sortir ?"
- Groupement & mapping : la proximite implique une relation ; placer un
  controle pres de ce qu'il affecte.
- Des libelles directs et specifiques valent mieux que des libelles
  generiques et prudents.

## 17. Processus

- Prototyper de maniere interactive : on decouvre l'interface en la
  construisant et en la manipulant.
- Concevoir l'interaction et le visuel ensemble, pas l'un apres l'autre.
- Tester avec de vraies personnes dans un contexte reel ; relire le
  mouvement au ralenti / image par image pour attraper ce qui est
  invisible a vitesse normale.

## Repères rapides

| Besoin | Technique | Valeur concrète |
|---|---|---|
| Spring par defaut | Critically damped, sans depassement | `damping 1.0`, `response 0.3–0.4` |
| Spring momentum / flick | Sous-amorti, leger rebond | `damping ~0.8`, `response 0.3–0.4` |
| Geste -> vitesse du spring | Report de la vitesse au relachement | `vitesseGeste / (cible − actuel)` si normalise |
| Point d'atterrissage d'un flick | Projection de momentum | `actuel + (v/1000)·d/(1−d)`, `d ≈ 0.998` |
| Interrompre proprement | Partir de la valeur de presentation (live) | lire le transform a l'ecran |
| Eviter le "mur de brique" au renversement | Reporter la vitesse au re-ciblage | spring qui fond la vitesse |
| Transition reversible | Miroir de la courbe d'easing | cubic-bezier inverse |
| Decider inverser vs valider | Utiliser le **signe** de la vitesse, pas la position | au relachement |
| Drag 1:1 | Pointer Events + capture | respecter l'offset de prise |
| Feedback | Sur pointerdown, continu | jamais seulement a la fin |
| Limite | Rubber-band, jamais d'arret net | resistance progressive |
| Chrome translucide | Couche `backdrop-filter` | le contenu defile dessous |
| Tracking typographique | Specifique a la taille, jamais fixe | serrer les grands textes (`-0.02em`), corps pres de `0` |
| Mouvement reduit | Cross-fade, pas de slide/spring | `@media (prefers-reduced-motion)` |

## Grille d’audit et de refonte

Methodologie complete pour auditer, noter et refondre un site ou une
interface existante. A suivre dans l'ordre : cartographie -> notation ->
plan d'action -> correction -> verification finale.

## 1. Cartographie (avant toute modification)

Ne rien corriger avant d'avoir identifie :

- Pages et routes existantes
- Composants et leur reutilisation
- Scripts JavaScript et leur role
- Appels API (internes/externes, cles exposees ou non)
- Formulaires et leur logique de validation
- Dependances (bibliotheques, versions, poids)
- Ressources externes (polices, CDN, trackers)
- Liens casses ou routes inexistantes
- Fonctionnalites visiblement incompletes

## 2. Grille de notation

Noter chaque categorie de 0 a 5 (0 = absent/critique, 5 = exemplaire). Une
note sous 3 devient une entree prioritaire du plan d'action.

| Categorie | Points de controle |
|---|---|
| Fonctionnel | Liens, boutons, formulaires, routes, etats d'erreur, page 404 |
| Securite | Secrets exposes, validation serveur, anti-spam reel, HTTPS, rate limiting |
| Conformite | Page RGPD, page CGU, banniere cookies avec choix reel, consentement respecte |
| SEO technique | Title/meta par page, H1 unique, hierarchie H2/H3, sitemap.xml, robots.txt, alt, favicon |
| Performance | Poids des images, scripts inutilises, requetes bloquantes, temps de chargement mobile |
| Responsive | Petit smartphone -> grand ecran, aucun scroll horizontal involontaire |
| Accessibilite | Contraste, tailles de texte, labels, navigation clavier, focus visible, semantique HTML |
| Redaction | Absence de tics rédactionnels (voir la section « Motifs interdits et remplacements » ci-dessous), absence de contenu invente, clarte du message |
| Design | Absence des motifs generiques (voir la section « Motifs interdits et remplacements » ci-dessous), coherence du design system, CTA unique |
| Motion (Motion) | Interruptibilite des gestes, feedback sur pointerdown, rubber-banding aux limites, `prefers-reduced-motion` respecte (voir la section « Guide Motion & Interfaces Fluides » ci-dessous) |

## 3. Friction utilisateur — ce qu'il faut traquer

Pour chaque page, suivre le parcours **arrivee -> comprehension -> action
principale** et noter chaque point de friction :

- Message principal pas identifiable en moins de 3 secondes
- Plus d'un CTA visuellement dominant par ecran
- Formulaire qui ne dit pas pourquoi une saisie est refusee
- Action qui ne donne aucun retour visuel (pas de loading, pas de confirmation)
- Navigation qui ne montre pas ou l'utilisateur se trouve
- Texte qui remplit la page sans apporter d'information nouvelle

## 4. Contenu : ne rien inventer

Interdiction absolue d'inventer : temoignages, statistiques, chiffres,
utilisateurs, recompenses, partenaires, certifications, resultats,
fonctionnalites, avis clients, logos, references, informations commerciales
(adresse, societe, hebergeur, tarifs). Une section sans contenu reel se
supprime ou se repense — elle ne se remplit jamais de contenu fabrique.

Pour les pages legales (RGPD/CGU) : utiliser des formulations prudentes et
lister explicitement ce qui manque plutot que d'inventer des informations
juridiques (adresse de societe, identifiant d'hebergeur, etc.).

## 5. Securite — points de controle detailles

- Rechercher dans tout le projet : cles API, tokens, mots de passe,
  identifiants, URLs internes sensibles exposes cote front.
- Verifier qu'aucune API sensible n'est appelee directement depuis le
  navigateur sans protection (proxy serveur, variable d'environnement cote
  serveur).
- Validation des formulaires cote client **et** serveur si un backend
  existe — la validation JS seule n'est jamais suffisante.
- Anti-spam reel (honeypot, throttling, captcha), jamais une protection
  uniquement visuelle.
- Rate limiting documente comme besoin serveur si le projet n'a pas de
  backend capable de l'implementer.
- HTTPS force si la configuration serveur est accessible ; sinon,
  instructions precises pour l'hebergeur.

## 6. Conformite (RGPD / CGU / Cookies)

- Page RGPD : donnees collectees, finalites, cookies, analytics, duree de
  conservation si connue, droits des utilisateurs, contact, consentement.
- Page CGU : utiliser uniquement les informations juridiques reellement
  disponibles (societe, adresse, hebergeur, tarifs) — jamais de fausse
  identite.
- Banniere cookies : categories expliquees, choix reel
  (accepter/refuser/personnaliser), refus non cache, aucun element soumis
  a consentement charge avant le choix de l'utilisateur.
- Analytics audite : ce qui est collecte, quand, quels cookies, besoin de
  consentement.

## 7. SEO technique

- `<title>` et meta description pertinents par page
- H1 unique et correct, hierarchie H2/H3 coherente
- `sitemap.xml` correspondant aux vraies pages, `robots.txt`
- Attributs `alt` pertinents, Open Graph si utile
- Favicon propre coherent avec l'identite visuelle (jamais generique si une
  identite existe deja)

## 8. Performance

- Compression et format moderne des images sans degrader la qualite
- Suppression des bibliotheques et scripts inutilises
- Elimination des requetes repetees et des chargements bloquants inutiles
- Verification du temps de chargement sur connexion mobile moyenne

## 9. Responsive

Tester reellement : petit smartphone, smartphone, tablette, desktop, grand
ecran. Verifier nav, boutons, formulaires, images, titres, espacements,
footer, tableaux, pages legales. Aucun element ne doit provoquer de scroll
horizontal involontaire.

## 10. Accessibilite

Contraste, lisibilite, tailles de texte, structure des titres, labels de
formulaire, navigation clavier, focus visible, attributs ARIA uniquement
quand reellement necessaires (le HTML semantique est toujours prefere).

## 10bis. Motion (Motion Fluid Interfaces)

Pour chaque interaction manipulable (drag, swipe, bottom-sheet, carousel,
slider) — détail complet dans la section « Guide Motion & Interfaces Fluides » ci-dessous :

- Feedback sur `pointerdown`, jamais uniquement a la liberation
- Suivi 1:1 du pointeur pendant tout le geste, offset de prise respecte
- Animation interruptible : redemarrage depuis la valeur live affichee,
  jamais depuis la cible
- Spring (pas de transition CSS a duree fixe) sur tout ce qui est
  manipulable ; `damping 1.0` par defaut, `~0.8` uniquement si le geste
  portait du momentum
- Handoff de la vitesse de relachement vers l'animation d'atterrissage
- Rubber-banding aux limites (jamais d'arret net)
- `prefers-reduced-motion: reduce` remplace les springs/slides par des
  cross-fades courts, sans supprimer le feedback
- `prefers-reduced-transparency: reduce` et `prefers-contrast: more` geres
  pour les surfaces translucides
- Aucune surface translucide empilee sur une autre surface translucide

## 11. Plan d'action

Classer chaque point note sous 3/5 par impact (fonctionnel/securite en
premier) et par effort (rapide a corriger en premier a impact egal).
Ne jamais corriger un point esthetique avant un point de securite ou de
fonctionnement.

## 12. Checklist finale obligatoire

Ne cocher un point que s'il a ete reellement verifie dans le code — jamais
par supposition.

### Fonctionnel
- [ ] Toutes les pages fonctionnent
- [ ] Tous les liens fonctionnent (nav, footer, boutons, CTA)
- [ ] Tous les formulaires fonctionnent (validation, erreurs, succes, chargement)
- [ ] La page 404 existe et fonctionne

### Securite
- [ ] Aucun secret inutilement expose cote front
- [ ] API sensibles protegees
- [ ] Anti-spam reel en place
- [ ] HTTPS verifie ou instructions donnees

### Conformite
- [ ] Page RGPD accessible
- [ ] Page CGU accessible, sans fausses informations
- [ ] Banniere cookies avec choix reel

### SEO
- [ ] Meta title et description par page
- [ ] Sitemap.xml et robots.txt crees
- [ ] Favicon coherent

### Performance
- [ ] Images compressees
- [ ] Scripts et requetes inutiles supprimes

### Responsive
- [ ] Mobile -> grand ecran sans debordement

### Accessibilite
- [ ] Contraste, navigation clavier, focus visible verifies

### Redaction
- [ ] Aucun tic de redaction convenu (voir la section « Motifs interdits et remplacements » ci-dessous)
- [ ] Aucun contenu invente

### Design
- [ ] Aucun motif generique banni present
- [ ] Un seul CTA principal identifiable

### Motion
- [ ] Interactions geste-dependantes interruptibles (spring, pas de transition CSS a duree fixe)
- [ ] Feedback sur pointerdown, suivi 1:1 verifie
- [ ] Rubber-banding aux limites, pas d'arret net
- [ ] `prefers-reduced-motion` et `prefers-reduced-transparency` geres
