"""
bake.py — embed audio + annotations into a single self-contained HTML file

usage:
    python3 bake.py <audio_file> <annotations.json>

output:
    for_u.html — open in any browser, no setup needed
"""

import base64, json, sys, os

if len(sys.argv) != 3:
    print("usage: python3 bake.py <audio_file> <annotations.json>")
    sys.exit(1)

audio_path = sys.argv[1]
json_path  = sys.argv[2]

ext = os.path.splitext(audio_path)[1].lower()
mime_map = {'.mp3':'audio/mpeg', '.mp4':'audio/mp4', '.m4a':'audio/mp4', '.wav':'audio/wav', '.ogg':'audio/ogg', '.webm':'audio/webm'}
mime = mime_map.get(ext, 'audio/mpeg')

with open(audio_path, 'rb') as f:
    audio_b64 = base64.b64encode(f.read()).decode('utf-8')

with open(json_path) as f:
    annotations = f.read().strip()

# Read the annotator template and inject the data
with open('annotator.html') as f:
    template = f.read()

baked = template.replace(
    "const AUDIO_SRC = null;",
    f"const AUDIO_SRC = 'data:{mime};base64,{audio_b64}';"
).replace(
    "const BAKED_ANNOTATIONS = null;",
    f"const BAKED_ANNOTATIONS = {annotations};"
)

with open('for_u.html', 'w') as f:
    f.write(baked)

size_mb = os.path.getsize('for_u.html') / 1024 / 1024
print(f"done — for_u.html ({size_mb:.1f} MB)")
