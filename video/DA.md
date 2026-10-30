# Direction artistique (DA)

Référence visuelle et sonore des vidéos de sensibilisation. Les valeurs ci-dessous sont celles utilisées dans `source/scene.html` et les scripts audio.

## Intention

Réaliste, sobre, industriel. On montre un vrai site de maintenance, sans dramatisation gratuite. Le danger est **invisible** (atmosphère appauvrie) : c'est l'image et le son qui doivent le faire sentir, pas des effets spectaculaires.

## Couleurs

| Rôle | Couleur | Usage |
|---|---|---|
| Jaune sécurité | `#f5b400` | Couleur principale : étiquettes d'étape, barre de titre, liseré des sous-titres, titre de fin |
| Rouge danger | `#ff4d4d` | 1ʳᵉ partie : erreurs (✗), titre du bilan |
| Rouge consignation | `#c8102e` | Étiquettes « CONSIGNÉ », signalétique |
| Vert OK | `#2e8b3a` | Statut correct du détecteur |
| Fond texte | `rgba(10,12,14,.78)` | Bandeau des sous-titres |
| Texte | `#ffffff` / `#cfcfcf` / `#aaa` | Principal / secondaire / mentions |
| Écran détecteur | `#9fb59a` sur `#13200f` | LCD du détecteur 4 gaz |

Brouillard de scène : `#1a1c1e`. Éclairage chaud (`#fff3e0`) pour la lampe frontale.

## Typographie

- **DejaVu Sans** pour tout le texte ; **DejaVu Sans Mono** pour l'horodatage caméra et le détecteur.
- Titre : 64 px gras. Surtitre : 18 px gras, capitales, interlettrage 6 px, en jaune.
- Sous-titres : 24 px, interligne 1,35 ; ligne secondaire 17 px.
- Étiquette d'étape : 16 px gras, capitales, interlettrage 2 px, texte noir sur jaune (texte blanc sur rouge pour une erreur).

## Mise en page

- Titres alignés à gauche, sur un dégradé noir → transparent.
- Sous-titres en bas à gauche : étiquette d'étape au-dessus, bandeau sombre avec liseré coloré de 5 px à gauche.
- Le détecteur apparaît en incrustation (grand pour la mesure, réduit pendant l'intervention).
- Apparitions en fondu + léger glissement horizontal (30 px).

## Image et caméra

- Caméra 50° de focale, légers tremblements « à l'épaule ».
- **Vue caméra-casque** à l'intérieur de la cuve : horodatage `REC`, grain plus fort, lampe frontale, brouillard dense.
- Post-traitement : tone mapping ACES, vignettage, grain, légère aberration chromatique.
- Saturation réduite (0,88 de base ; 0,6 pour le titre ; 0,4 pour la fin) : palette désaturée où le jaune sécurité ressort.
- Malaise / perte de connaissance : flou progressif, tremblement accru, image qui bascule.

## Son

- Pas de musique : ambiance d'atelier synthétisée (grondement grave, ronflement 50 Hz et harmoniques, machines lointaines).
- Dans la cuve : même ambiance mais étouffée (filtre passe-bas), pour l'enfermement.
- Bruitages : pas, échelle métallique, ventilateur, bip du détecteur, alarme.
- Fondu de sortie de 1,5 s sur l'image et le son.

## Ton des textes

- Phrases courtes, vocabulaire du métier (permis, consignation, LIE, surveillant).
- 1ʳᵉ partie : constats (« Descente seul, sans harnais… »).
- 2ᵉ partie : consignes à l'impératif, étapes numérotées (« Étape 1 · Préparation »).
- Les seuils sont toujours chiffrés (O₂ < 19,5 %).
