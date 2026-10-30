# Espace confiné — vidéo de sensibilisation (maintenance industrielle)

`espace-confine.mp4` — 1280×720, 25 i/s, ~2 min 06, sous-titres incrustés en français, bande-son d'ambiance.

Structure : **1ʳᵉ partie — les mauvais réflexes** (reconstitution d'un accident), puis **2ᵉ partie — les bons réflexes** (la même intervention réalisée en sécurité).

## Déroulé

| Temps | Séquence | Contenu |
|---|---|---|
| 0:00–0:05 | Titre | « Espace confiné — mauvais réflexes, bons réflexes » |
| 0:05–0:08 | 1ʳᵉ partie | Les mauvais réflexes — reconstitution d'un accident |
| 0:08–0:16 | ✗ Erreur | Intervention « rapide » : ni permis, ni balisage, ni consignation |
| 0:16–0:23 | ✗ Erreur | Descente seul, sans harnais, sans détecteur, sans ventilation |
| 0:23–0:33 | ✗ Danger invisible | Vue caméra-casque : atmosphère appauvrie en O₂, malaise, perte de connaissance |
| 0:33–0:41 | ✗ Erreur fatale | Un collègue descend porter secours sans protection |
| 0:41–0:51 | Bilan | 2 victimes — récapitulatif des erreurs |
| 0:51–0:54 | 2ᵉ partie | Les bons réflexes |
| 0:54–1:05 | Étape 1 · Préparation | Permis, consignation, balisage, trépied + treuil |
| 1:05–1:15 | Étape 2 · Détection | Mesure 4 gaz (O₂, LIE, H₂S, CO) avant l'entrée |
| 1:15–1:23 | Étape 3 · Ventilation | Ventilateur et gaine soufflant de l'air neuf au fond |
| 1:23–1:33 | Étape 4 · Entrée | Descente encordée, harnais relié au treuil, surveillant dehors |
| 1:33–1:48 | Étape 5 · Intervention | Détecteur porté en continu ; alarme O₂ < 19,5 % → évacuation |
| 1:48–1:58 | Étape 6 · Évacuation | Le surveillant remonte l'intervenant au treuil, alerte les secours |
| 1:58–2:06 | À retenir | Les 6 règles clés |

Documents du projet : [suivi](SUIVI.md) · [méthode](METHODE.md) · [direction artistique](DA.md)

> Vidéo de sensibilisation : elle ne remplace ni la formation ni les procédures du site.

## Régénérer la vidéo

La scène est une animation 3D procédurale (Three.js, textures générées), rendue image par image dans Chromium headless.

```bash
cd video/source
npm install three@0.160.0
python3 -m http.server 8765 &          # sert scene.html
node render.js preview 10,22,50        # aperçus prev_<t>.jpg
mkdir -p frames frames_bad
node render.js bad 0 1350               # 1re partie (renderBad)
node render.js frames 150 1950          # 2e partie (renderAt)
pip install numpy scipy
python3 audio_bad.py && python3 audio.py
./assemble.sh                          # -> ../espace-confine.mp4
```
