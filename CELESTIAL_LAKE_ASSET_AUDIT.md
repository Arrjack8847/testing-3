# Celestial Lake — Scene 1 Asset Audit
Status: **static composition prototype**, not production-ready.
Original `main` files are preserved unchanged; normalized file names are references to their existing Git blob SHA, not regenerated artwork.
- **20 normalized binary assets** copied into `public/assets/celestial-lake/` without duplicating binary uploads.
- **Asset 11 (left peacock) is absent from this GitHub repository**; the left garden base includes a peacock and is used as temporary fallback.
- The user-approved master screenshot is not yet in this GitHub repository. Compare to it manually before merging.
- Known composition risks: 04 is opaque and requires a mask; 07/08 contain peacocks/columns; additional peacocks would duplicate them; some overlays have feathered edges.
- Static preview intentionally uses 07/08 as peacock-and-column bases, not separate 11/12 birds, to avoid doubling.
- No animations, RSVP, backend, or functional wedding page have been implemented.
- Launch locally with `python -m http.server 8000 --directory public`, then open `http://localhost:8000` and compare at 390×844, 375×812 and 360×800.
- Blocker: automated Chromium navigation was blocked in the execution environment. A separate visual layer composite was rendered and reviewed, but an actual browser/mobile screenshot is still **pending**.
- Next gate: replace/fix inconsistent masks and align static composition to approved master before adding animations.