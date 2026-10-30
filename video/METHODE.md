# Méthode de production

Comment on fabrique une vidéo de sensibilisation dans ce dépôt, de l'idée au fichier final.

## 1. Principes

- **Un message, un geste** : chaque séquence montre une seule erreur ou une seule bonne pratique.
- **Montrer avant d'expliquer** : l'image porte l'action, le texte incrusté la nomme.
- **Contraste** : d'abord ce qui tourne mal, ensuite la même situation bien gérée.
- **Tout en code** : décor, animation, son et montage sont générés par des scripts. On peut tout régénérer et tout versionner.
- **Rappel systématique** : la vidéo ne remplace ni la formation ni les procédures du site (mention en fin de vidéo).

## 2. Étapes

### Préparation
1. **Brief** : public visé, risque traité, durée cible (~2 min), message principal.
2. **Contenu métier** : liste des erreurs typiques et des règles, avec les seuils chiffrés (ex. O₂ < 19,5 %). À faire valider par un préventeur.
3. **Déroulé** : tableau temps / séquence / contenu (voir `README.md`). C'est la référence pour le rendu, l'audio et le montage.

### Fabrication
4. **Scène** (`source/scene.html`) : décor 3D Three.js procédural, avec une timeline `T` qui découpe la vidéo en séquences. Deux fonctions de rendu : `renderBad(t)` (1ʳᵉ partie) et `renderAt(t)` (2ᵉ partie).
5. **Habillage** : titres, sous-titres (`setCap`), détecteur 4 gaz, bilan et écran de fin, en HTML/CSS par-dessus la 3D. Respecter la [DA](DA.md).
6. **Aperçus** : `node render.js preview 10,22,50` produit des images fixes `prev_<t>.jpg` pour vérifier le cadrage avant le rendu complet.
7. **Rendu** : image par image dans Chromium headless (`render.js`), en JPEG dans `frames/` et `frames_bad/`. Le script saute les images déjà rendues, ce qui permet de reprendre un rendu interrompu.
8. **Son** : `audio_bad.py` et `audio.py` synthétisent l'ambiance (numpy/scipy) en se calant sur le déroulé.
9. **Montage** : `assemble.sh` concatène les deux parties avec ffmpeg, mixe l'audio, ajoute le fondu final et encode en H.264 + AAC.

Commandes complètes : voir `README.md`, section « Régénérer la vidéo ».

### Remotion (optionnel)
Le projet `remotion/` permet d'écrire des séquences en React :
```bash
cd video/remotion
npm install
npm run studio   # aperçu interactif
npm run render   # -> out/titre.mp4
```

### Contrôle
10. **Relecture technique** : synchronisation image/son, lisibilité des textes, pas d'image noire ni de saut.
11. **Relecture métier** : exactitude des gestes et des seuils.
12. **Livraison** : mettre à jour [SUIVI.md](SUIVI.md), commiter le fichier final et ses sources.

## 3. Conventions

- Format de référence : 1280×720, 25 i/s, H.264 (CRF 23), AAC 160 kb/s, `+faststart`.
- Langue : français ; textes courts, à l'impératif pour les règles.
- Les fichiers intermédiaires (`frames/`, `*.wav`, `prev_*.jpg`, `out/`) ne sont pas versionnés.
- Messages de commit en français, au présent (« Ajoute… », « Restructure… »).
