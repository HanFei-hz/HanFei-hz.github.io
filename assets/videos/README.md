# ICRA videos

The homepage currently shows the following two videos, uploaded on September 30, 2026.
Until a file exists, its card shows "Video coming soon".

| File | Paper |
|---|---|
| `icra2025.mp4` | Learn to Swim (ICRA 2025) |
| `icra2026.mp4` | Swimming Under Constraints (ICRA 2026) |

The ICRA 2027 video card is intentionally omitted for now.

Keep each file under ~25 MB (GitHub rejects files over 100 MB, and large files load slowly).
H.264 MP4, 1280×720, ~2 Mbps is plenty. With ffmpeg:

```
ffmpeg -i input.mp4 -vf scale=1280:-2 -c:v libx264 -crf 26 -preset slow -c:a aac -b:a 96k -movflags +faststart icra2025.mp4
```
