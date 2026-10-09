# Grille d'audit et de refonte

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
| Redaction | Absence de tics IA (voir `banned-patterns.md`), absence de contenu invente, clarte du message |
| Design | Absence des motifs generiques (voir `banned-patterns.md`), coherence du design system, CTA unique |
| Motion (Apple) | Interruptibilite des gestes, feedback sur pointerdown, rubber-banding aux limites, `prefers-reduced-motion` respecte (voir `apple-motion-guide.md`) |

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

## 10bis. Motion (Apple Fluid Interfaces)

Pour chaque interaction manipulable (drag, swipe, bottom-sheet, carousel,
slider) — detail complet dans `apple-motion-guide.md` :

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
- [ ] Aucun tic d'ecriture IA (voir `banned-patterns.md`)
- [ ] Aucun contenu invente

### Design
- [ ] Aucun motif generique banni present
- [ ] Un seul CTA principal identifiable

### Motion
- [ ] Interactions geste-dependantes interruptibles (spring, pas de transition CSS a duree fixe)
- [ ] Feedback sur pointerdown, suivi 1:1 verifie
- [ ] Rubber-banding aux limites, pas d'arret net
- [ ] `prefers-reduced-motion` et `prefers-reduced-transparency` geres
