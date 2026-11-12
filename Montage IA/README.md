# Montage IA

Espace de travail pour les montages réalisés avec l'aide de l'IA.

## Outils

| Outil | Rôle | Où |
|---|---|---|
| [Remotion](https://www.remotion.dev/) | Écrire des séquences vidéo en React | `remotion/` |
| [HyperFrames](https://hyperframes.heygen.com/) | Écrire des vidéos en HTML, rendu MP4 | `hyperframes/` |
| [yt-dlp](https://github.com/yt-dlp/yt-dlp) | Télécharger des vidéos en ligne | `.venv/` (Python) |
| [Whisper](https://github.com/openai/whisper) | Transcrire l'audio (sous-titres) | `.venv/` (Python) |
| [FFmpeg](https://ffmpeg.org/) | Convertir, découper, assembler | installé sur le système |

## Installation

```bash
cd "Montage IA"
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt      # yt-dlp + Whisper (~5,6 Go avec torch)
(cd hyperframes && npm ci && npx hyperframes browser ensure)
(cd remotion && npm ci)
```

## Utilisation

```bash
# Remotion
cd remotion && npm run studio            # aperçu interactif
cd remotion && npm run render            # -> out/titre.mp4

# HyperFrames (projet d'exemple : hyperframes/exemple)
cd hyperframes/exemple && npm run dev     # aperçu
cd hyperframes/exemple && npm run render  # -> renders/*.mp4
npx hyperframes init mon-projet --example=blank --non-interactive --skip-skills   # nouveau projet (depuis hyperframes/)

# Whisper : transcription en français -> sous-titres .srt
.venv/bin/whisper audio.wav --model small --language fr --output_format srt --fp16 False

# yt-dlp
.venv/bin/yt-dlp "<url>"

# FFmpeg : extraire l'audio d'une vidéo pour Whisper
ffmpeg -i video.mp4 -ac 1 -ar 16000 audio.wav
```

Notes :
- Whisper télécharge ses modèles au premier usage depuis `openaipublic.azureedge.net`.
- La transcription intégrée de HyperFrames utilise `whisper-cpp`, qui n'est pas installé ici ; utiliser le Whisper Python ci-dessus.

Voir aussi la [méthode](../video/METHODE.md), la [direction artistique](../video/DA.md) et le [suivi](../video/SUIVI.md) de la vidéo espace confiné.
