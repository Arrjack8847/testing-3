# Celestial Lake — Static opening composition v2

This branch is **still a draft**, not approved or ready to merge.

## Implemented in v2
- Refined arch scaling so the upper filigree does not dominate the sky.
- Rendered each existing garden source twice with two **clipped positions**, keeping upper architectural foliage independent of lower peacock placement; no new images required.
- Shifted the lower peacocks toward their positions in the approved master, avoiding duplicate birds from separate PNGs.
- Aligned the pavilion, boat, mountains, lotus crest, title divider and bottom button.
- Preserved the center names zone for future HTML content.
- No animations or functional guest features added.

## Static preview
Open `public/index.html` from a simple static server (`python -m http.server 8000 --directory public`).

## QA evidence & caveats
- A local Pillow image-layer composite was compared side by side against the **approved 852 × 1846 master**. Some visual differences remain (especially texture, arch and lower garden integration).
- Local HTML references were checked: all 20 referenced PNGs exist. Tags were balanced, and the CSS parsed without errors.
- An actual Chromium navigation test was attempted, but blocked with `ERR_BLOCKED_BY_ADMINISTRATOR`; therefore **browser/mobile layout is not verified**.
- The approved master is still not uploaded to this repository. The existing left-garden source contains a left peacock; dedicated Asset 11 remains absent on GitHub.
- Do not merge or add animations until visually reviewed at phone sizes 390×844, 375×812, and 360×800.
