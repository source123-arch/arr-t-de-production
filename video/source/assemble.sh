#!/bin/sh
# 0-80 s : audio_m1.wav (accident + permis) ; 80-152 s : audio.wav de 6 à 78 s (bons réflexes)
set -e
ffmpeg -y -v error -i audio.wav -ss 6 -t 72 -c pcm_s16le good.wav
ffmpeg -y -v error -i audio_m1.wav -i good.wav -filter_complex "[0][1]concat=n=2:v=0:a=1,afade=t=out:st=150.5:d=1.5" -c pcm_s16le full2.wav
ffmpeg -y -v error -framerate 25 -i frames_m/f%05d.jpg -i full2.wav -vf "fade=t=out:st=150.5:d=1.5" \
  -c:v libx264 -crf 23 -maxrate 4M -bufsize 8M -preset slow -pix_fmt yuv420p -c:a aac -b:a 160k -shortest -movflags +faststart "${1:-../espace-confine.mp4}"
