# Espace confiné — vidéo de sensibilisation (maintenance industrielle)

`espace-confine.mp4` — 1280×720, 25 i/s, 80 s, sous-titres incrustés en français, bande-son d'ambiance.

## Déroulé

| Temps | Séquence | Contenu |
|---|---|---|
| 0–6 s | Titre | « Travail en espace confiné » |
| 6–17 s | Étape 1 · Préparation | Permis, consignation, balisage, trépied + treuil au-dessus du trou d'homme |
| 17–27 s | Étape 2 · Détection | Mesure 4 gaz (O₂, LIE, H₂S, CO) avant l'entrée |
| 27–35 s | Étape 3 · Ventilation | Ventilateur et gaine soufflant de l'air neuf au fond de la cuve |
| 35–45 s | Étape 4 · Entrée | Vue caméra-casque : descente à l'échelle, harnais relié au treuil |
| 45–60 s | Étape 5 · Intervention | Vanne consignée/cadenassée, puis alarme O₂ < 19,5 % |
| 60–70 s | Étape 6 · Évacuation | Le surveillant remonte l'intervenant au treuil et alerte les secours |
| 70–80 s | À retenir | Les 6 règles clés |

> Vidéo de sensibilisation : elle ne remplace ni la formation ni les procédures du site.

## Régénérer la vidéo

La scène est une animation 3D procédurale (Three.js, textures générées), rendue image par image dans Chromium headless.

```bash
cd video/source
npm install three@0.160.0
python3 -m http.server 8765 &          # sert scene.html
node render.js preview 10,22,50        # aperçus prev_<t>.jpg
mkdir -p frames && node render.js frames 0 2000
python3 audio.py                       # -> audio.wav (numpy)
ffmpeg -framerate 25 -i frames/f%05d.jpg -i audio.wav -c:v libx264 -crf 21 -preset slow \
  -pix_fmt yuv420p -c:a aac -b:a 160k -shortest -movflags +faststart ../espace-confine.mp4
```
