#!/bin/sh
# Partie 1 = frames_bad (0-54 s) ; partie 2 = frames 150..1949 (t = 6-78 s de la timeline « bons réflexes »)
set -e
ffmpeg -y -i audio.wav -ss 6 -t 72 -c pcm_s16le good.wav
ffmpeg -y -i audio_bad.wav -i good.wav -filter_complex "[0][1]concat=n=2:v=0:a=1,afade=t=out:st=124.5:d=1.5" -c pcm_s16le full.wav
ffmpeg -y -framerate 25 -i frames_bad/f%05d.jpg -framerate 25 -start_number 150 -i frames/f%05d.jpg -i full.wav \
  -filter_complex "[0:v][1:v]concat=n=2:v=1:a=0,trim=duration=126,fade=t=out:st=124.5:d=1.5[v]" -map "[v]" -map 2:a \
  -c:v libx264 -crf 23 -maxrate 4M -bufsize 8M -preset slow -pix_fmt yuv420p -c:a aac -b:a 160k -movflags +faststart ../espace-confine.mp4
