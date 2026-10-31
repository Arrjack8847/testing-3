#!/usr/bin/env python3
"""Static sanity checks; does not claim a real browser/mobile render."""
from pathlib import Path
from html.parser import HTMLParser
from struct import unpack

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ROOT / "public"
HTML = PUBLIC / "index.html"
CSS = PUBLIC / "scene.css"

class Images(HTMLParser):
    def __init__(self):
        super().__init__()
        self.images = []
    def handle_starttag(self, tag, attrs):
        if tag == "img":
            src = dict(attrs).get("src")
            if src: self.images.append(src)

p = Images(); p.feed(HTML.read_text(encoding="utf-8"))
assert len(p.images) >= 14, f"Only {len(p.images)} image elements found"
missing = [s for s in p.images if not (PUBLIC / s.removeprefix("./")).is_file()]
assert not missing, "Missing source images: " + ", ".join(missing)

css = CSS.read_text(encoding="utf-8")
for token in ("aspect-ratio: 852 / 1846", ".scene", ".button-position", ".left-garden-upper", ".right-garden-lower", "mask-image", "overflow-y: auto"):
    assert token in css, f"CSS missing {token}"

pngs = sorted((PUBLIC / "assets/celestial-lake").glob("*.png"))
assert len(pngs) >= 20, f"Expected at least 20 PNGs, got {len(pngs)}"
opaque = []
for f in pngs:
    with f.open("rb") as fh:
        header = fh.read(26)
    assert header[:8] == b"\x89PNG\r\n\x1a\n", f"Bad PNG: {f.name}"
    w, h = unpack(">II", header[16:24]); assert w > 0 and h > 0
    if header[25] == 2: opaque.append(f.name)

print(f"PASS: {len(p.images)} image tags resolve, {len(pngs)} PNG files, CSS controls present")
print("VIEWPORT GEOMETRY (estimated CSS-only; not browser-tested):")
for w, h in ((360,800),(375,812),(390,844)):
    scene_h = w * 1846 / 852
    button_width = w * (1 - .24 - .24)
    print(f"  {w}x{h}: scene {w}x{scene_h:.1f}; mock button width {button_width:.0f}px; natural vertical scroll {'yes' if scene_h + 32 > h else 'possible'}")
print("Opaque artwork (requires explicit layering/mask):",opaque)
print("WARNING: actual mobile browser navigation/render test not executed; do not treat this as pixel approval")
