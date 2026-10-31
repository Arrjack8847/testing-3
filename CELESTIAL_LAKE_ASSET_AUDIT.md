# Celestial Lake — Mobile layout refinement V3
**Branch:** feat/celestial-lake-static-opening — **status:** draft; not approved for merge.

## Corrections
- Replaced harsh horizontal clipping in the composite garden upper/lower layers with 6%-height feathered CSS masks, reducing the visible seam across the mountain and shoreline.
- Reduced top-arch height and softened the duplicated columns.
- Set natural vertical scrolling; no fixed height and no scroll locking.
- Preserved the 852:1846 composition ratio and the interactive text safe region. The Open Invitation label is **still a non-functional visual mock-up**.
- No artwork regenerated; no animations introduced.

## Verification
- `scripts/validate_celestial_lake.py`: 20 HTML image tags resolve and 20+ existing artwork PNGs parse as PNG, including the intentionally opaque sky and lake.
- Layout geometry was inspected by scaling a locally rendered Pillow image-layer composite at **360×800, 375×812 and 390×844**. This is a **simulation**, not a browser screenshot.
- A real headless Chromium navigation was attempted against localhost, file:// and data: URLs; the execution environment blocked it with `ERR_BLOCKED_BY_ADMINISTRATOR`.
- No claim of tested Safari, Android Chrome, or actual browser scroll behavior.
- Visual gaps remain versus the user-approved master (arch/flowers and pavilion/boat size); do not merge until mobile browser review and fixes.

## Test locally
From repository root: `python -m http.server 8000 --directory public`
Open `http://localhost:8000` and check at 360×800, 375×812 and 390×844.
Run `python scripts/validate_celestial_lake.py` for structural checks.

## Remaining work before animation
1. Browser-validate natural vertical scroll and no horizontal overflow.
2. Review and align to approved master using actual on-phone screenshots.
3. Add clean standalone Asset 11 and reconsider already-baked peacocks in the garden composite.
4. Repair any transparency halos, especially around lake and flowers.
