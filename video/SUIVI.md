# Suivi de production — Espace confiné

Vidéo de sensibilisation « Espace confiné — mauvais réflexes, bons réflexes » (maintenance industrielle).

## État actuel

| Élément | État | Notes |
|---|---|---|
| Scénario (2 parties) | ✅ Validé | Mauvais réflexes (accident) → bons réflexes (6 étapes) |
| Scène 3D (`source/scene.html`) | ✅ Fait | Three.js procédural, cuve enterrée, hall industriel |
| Rendu images (`source/render.js`) | ✅ Fait | Chromium headless, 1280×720, 25 i/s |
| Bande-son (`audio.py`, `audio_bad.py`) | ✅ Fait | Ambiance synthétisée, pas de voix off |
| Montage final (`assemble.sh`) | ✅ Fait | `espace-confine.mp4`, 2 min 06 |
| Remotion (`remotion/`) | 🟡 Installé | Composition d'exemple `Titre` seulement |
| Voix off | ⬜ À faire | — |
| Version 1080p | ⬜ À faire | Le master actuel est en 720p |
| Validation par un préventeur / HSE | ⬜ À faire | Vérifier seuils, vocabulaire, conformité aux procédures du site |

Légende : ✅ fait · 🟡 en cours · ⬜ à faire · ⛔ bloqué

## Historique

| Date | Étape | Commit |
|---|---|---|
| 2026-10-30 | Sources initiales : scène 3D, rendu, audio | `e0ccab1` |
| 2026-10-30 | Restructuration : mauvais réflexes puis bons réflexes, ~2 min | `9ca8f67` |
| 2026-10-30 | Export final `espace-confine.mp4` (2 min 06) | `9424e6b` |
| 2026-10-30 | Installation de Remotion dans `video/remotion/` | `d8ec701` |

## Prochaines étapes

- [ ] Décider du rôle de Remotion : refaire les habillages (titres, sous-titres, détecteur, bilan) en React par-dessus les images 3D, ou garder le pipeline actuel.
- [ ] Écrire et enregistrer (ou synthétiser) une voix off.
- [ ] Faire relire le contenu par un préventeur.
- [ ] Produire un export 1920×1080.
- [ ] Prévoir des sous-titres séparés (`.srt`) pour l'accessibilité.

## Décisions

- **Structure en deux parties** : montrer d'abord l'accident (mauvais réflexes), puis la même intervention bien faite, pour créer le contraste.
- **Tout est procédural** : aucune image ni son externe, donc pas de question de droits.
- **Pas de voix off pour l'instant** : les textes incrustés portent le message.

## Points ouverts

- Remotion et le pipeline Three.js actuel coexistent : à unifier ou non.
- Le fichier `espace-confine.mp4` (~48 Mo) est versionné directement dans git ; envisager Git LFS si d'autres versions s'ajoutent.
