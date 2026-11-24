# RESCENE Subtitles Finder

A lightweight browser extension for REMINEs that adds a **Watch with English Subs** button on YouTube videos and Shorts whenever an English-subtitled version is available.

## How It Works

1. An automated daily workflow (`build_map.py` via GitHub Actions) scans **Pandanim** (`@PandanimRS`) for source YouTube links in video descriptions and updates `subs.json`.
2. When you watch a RESCENE video on YouTube, the extension checks the live mapping list and displays a pink **🇬🇧 Watch with English Subs** button next to the channel bar if a subtitled version is matched.
3. Clicking the button takes you straight to the subtitled video.

## Installation (Chrome / Edge / Brave / Arc)

1. Go to the [**Releases**](https://github.com/rcktb1/rescene-subs/releases) page and download **`rescene-subs-finder.zip`**.
2. Extract the ZIP archive into its own folder on your computer.
3. Open your browser's extensions page:
   - Chrome / Brave / Arc: `chrome://extensions`
   - Microsoft Edge: `edge://extensions`
4. Turn on **Developer mode** (top-right toggle).
5. Click **Load unpacked** and select the extracted folder.

Because subtitle mappings are fetched live from `subs.json`, new matches appear automatically without needing to reinstall the extension.

## Credits & Notes

- **English Subtitles:** All fan-subtitled videos belong to their respective creators—huge thanks to **Pandanim** (`@PandanimRS`) for subbing RESCENE content for the community.
- **Coverage:** Only videos with matching source links in `subs.json` will show the button. If a subtitled video is missing, feel free to open an issue or submit a pull request adding `"ORIGINAL_VIDEO_ID": "SUBBED_VIDEO_ID"` to `subs.json`.
