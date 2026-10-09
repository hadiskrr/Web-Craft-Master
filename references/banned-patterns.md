# Matrice des interdits & remplacements

Reference technique pour `web-craft-master`. Chaque section explique
*pourquoi* le motif est banni, puis donne un remplacement copiable.

## 1. Typographie

**Pourquoi** : Inter, Geist et Space Grotesk sont devenues les polices par
defaut de tous les generateurs IA et templates SaaS. Leur omnipresence tue
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
`apple-motion-guide.md` §15 pour le detail et les valeurs.

```css
/* Avant */
font-family: "Inter", sans-serif;

/* Apres */
font-family: "Plus Jakarta Sans", sans-serif;
```

## 2. Emoji dans les titres et boutons

**Pourquoi** : un emoji en titre signale instantanement un contenu genere
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
plus reconnaissable d'un template genere automatiquement. Elles n'apportent
aucune information a l'utilisateur. Sur tout element **manipulable**
(drag, swipe, sheet), une transition CSS classique est en plus un defaut
fonctionnel : elle ne peut pas etre saisie et inversee en plein vol — voir
`apple-motion-guide.md` §3.

| Interdit | Remplacement |
|---|---|
| `animate-bounce` sur une fleche de CTA | Pas d'animation sur l'icone ; `transition-colors duration-150` sur le bouton lui-meme |
| `hover:-translate-y-2 hover:scale-105` sur une carte | `hover:border-slate-300 transition-colors duration-150` |
| Particules / neige / effets de fond animes | Aucun. Fond uni ou texture statique tres discrete |
| Transition d'entree sur chaque bloc au scroll | Reserver aux changements d'etat reels (ouverture menu, validation formulaire) |
| `transition: transform 300ms ease` sur un sheet/drawer glissable | Spring interruptible (`type: 'spring'`), anime depuis la valeur live — voir `apple-motion-guide.md` §3-4 |
| Snap brutal sur une limite de scroll/drag | Rubber-banding : resistance progressive (`apple-motion-guide.md` §9) |
| Vitesse coupee net a la fin d'un drag | Handoff de vitesse vers le spring d'atterrissage (`apple-motion-guide.md` §5) |

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
materiau translucide maitrise a la Apple (flou mesure, bordure fine,
une seule couche) encode une hierarchie reelle sans tomber dans l'effet
template.

| Interdit | Remplacement |
|---|---|
| `shadow-2xl`, `drop-shadow-xl` | `shadow-xs` ou `shadow-sm` |
| `backdrop-blur-lg bg-white/30 shadow-2xl rounded-3xl` (glassmorphism surcharge) | `backdrop-filter: blur(20px)` + fond semi-transparent **unique** + bordure 1px, sans ombre lourde — voir `apple-motion-guide.md` §12 |
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

<!-- Apres (option materiau Apple) : translucidite maitrisee, une seule couche -->
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

## 6. Redaction — tics d'ecriture IA

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
