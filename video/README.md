# Espace confiné — vidéo de sensibilisation (maintenance industrielle)

`espace-confine.mp4` — 1280×720, 25 i/s, 2 min 32, sous-titres incrustés en français, bande-son d'ambiance.

Animation 3D de synthèse : personnages articulés, textures procédurales, éclairage dynamique, profondeur de champ et grain de film.
Structure : **1ʳᵉ partie — les mauvais réflexes** (reconstitution d'un accident), puis **2ᵉ partie — les bons réflexes**.

## Déroulé

| Temps | Séquence | Contenu |
|---|---|---|
| 0:00–0:08 | Titre · 1ʳᵉ partie | « Espace confiné — mauvais réflexes, bons réflexes » |
| 0:08–0:17 | ✗ Erreur | Intervention « rapide » : ni permis, ni balisage, ni consignation |
| 0:17–0:24 | ✗ « Ça ne sent rien » | Vue caméra-casque au-dessus du trou : l'odorat ne détecte pas le manque d'O₂ |
| 0:24–0:31 | ✗ Erreur | Descente seul, sans harnais, sans détecteur, sans ventilation |
| 0:31–0:43 | ✗ Danger invisible | Vue caméra-casque : atmosphère appauvrie, malaise, perte de connaissance |
| 0:43–0:56 | ✗ Erreur fatale | Un collègue accourt, appelle sans réponse, descend sans protection |
| 0:56–1:00 | ✗ | Vue du sauveteur : il s'effondre à son tour |
| 1:00–1:10 | Bilan | 2 victimes — récapitulatif des erreurs |
| 1:10–1:20 | 2ᵉ partie · Permis | Permis de pénétrer rempli case par case et signé |
| 1:20–1:31 | Étape 1 · Préparation | Consignation, balisage, trépied + treuil |
| 1:31–1:41 | Étape 2 · Détection | Mesure 4 gaz (O₂, LIE, H₂S, CO) avant l'entrée |
| 1:41–1:49 | Étape 3 · Ventilation | Ventilateur et gaine soufflant de l'air neuf au fond |
| 1:49–1:59 | Étape 4 · Entrée | Descente encordée, harnais relié au treuil, surveillant dehors |
| 1:59–2:14 | Étape 5 · Intervention | Détecteur porté en continu ; alarme O₂ < 19,5 % → évacuation |
| 2:14–2:24 | Étape 6 · Évacuation | Le surveillant remonte l'intervenant au treuil, alerte les secours |
| 2:24–2:32 | À retenir | Les 6 règles clés |

> Vidéo de sensibilisation : elle ne remplace ni la formation ni les procédures du site.

## Régénérer la vidéo

La scène est une animation 3D procédurale (Three.js, textures générées), rendue image par image dans Chromium headless.

```bash
cd video/source
npm install three@0.160.0
python3 -m http.server 8765 &          # sert scene.html
node render.js preview 10,22,50        # aperçus prev_<t>.jpg
mkdir -p frames_m && node render.js master 0 3800   # timeline complète (renderMaster)
pip install numpy scipy
python3 audio.py && python3 audio_master.py
./assemble.sh                          # -> ../espace-confine.mp4
```
