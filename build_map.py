import json
import os
import re
import subprocess

CHANNEL_URLS = [
    "https://www.youtube.com/@PandanimRS/videos",
    "https://www.youtube.com/@PandanimRS/shorts",
    "https://www.youtube.com/@PandanimRS/streams",
]

YT_REGEX = re.compile(
    r"(?:youtube\.com/(?:watch\?v=|shorts/)|youtu\.be/)([a-zA-Z0-9_-]{11})"
)

# Load existing subs.json so previously mapped videos are never lost
sub_map = {}
if os.path.exists("subs.json"):
    with open("subs.json", "r", encoding="utf-8") as f:
        sub_map = json.load(f)

initial_count = len(sub_map)
print(f"Loaded {initial_count} existing entries from subs.json.")

for url in CHANNEL_URLS:
    print(f"\nScanning {url}...")
    cmd = [
        "yt-dlp",
        "--dump-json",
        "--skip-download",
        "--ignore-errors",
        "--ignore-no-formats-error",
        "--no-warnings",
        url,
    ]

    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, text=True, encoding="utf-8")
    tab_scanned = 0

    for line in proc.stdout:
        try:
            data = json.loads(line)
            tab_scanned += 1
            pandanim_id = data.get("id")
            description = data.get("description", "")

            for orig_id in YT_REGEX.findall(description):
                if orig_id != pandanim_id and orig_id not in sub_map:
                    sub_map[orig_id] = pandanim_id
                    print(f"  [New] {orig_id} -> {pandanim_id}")
        except json.JSONDecodeError:
            continue

    proc.wait()
    print(f"Finished tab ({tab_scanned} items checked).")

with open("subs.json", "w", encoding="utf-8") as f:
    json.dump(sub_map, f, indent=2)

print(f"\nDone! Total mapped videos: {len(sub_map)} (+{len(sub_map) - initial_count} new).")