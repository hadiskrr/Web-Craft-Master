# Guide Apple Motion & Fluid Interfaces

Traduction operationnelle, pour le web, des principes exposes par Apple dans
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

**Valeurs concretes livrees par Apple**

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
utilisee par Apple — utiliser la forme en decay exponentiel ci-dessus.

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
   et dommages possibles, en particulier avec l'IA.
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

## Reference rapide

| Besoin | Technique | Valeur concrete |
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
