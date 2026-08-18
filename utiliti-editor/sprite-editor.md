---
meta.description: "Comprehensive guide to the utiLITI Sprite & Animation Editor: spritesheet slicing, keyframe durations, animated previews, and sprite info export."
meta.keywords: "utiLITI, Sprite Editor, Animation Editor, spritesheets, keyframe durations, sprite slicing, animation preview, sprite info"
meta.title: "Sprites & Animation Editor in utiLITI"
---

# Sprites & Animation Editor

The **Sprite & Animation Editor** (accessible via the `Spritesheets` asset category) allows you to import sprite sheets, configure frame slicing grids, define custom per-frame durations, test animations in a live playback preview, and export sprite metadata.

---

## Editor Overview

```
┌─────────────────────────────────────────────────────────────┐
│ Name: hero-walk  |  Total Frames: 6  |  Frame Size: 32x32   │
├───────────────────────────────┬─────────────────────────────┤
│                               │ [Live Animation Preview]    │
│                               │ ┌────────┐ [▶] [⏸] [⏮] [⏭] │
│                               │ │  HERO  │ Speed: 1.0x      │
│                               │ └────────┘ Zoom: 4x [Loop]  │
│         SPRITE GRID           ├─────────────────────────────┤
│  Interactive Slicing Preview  │ [Keyframe Durations (ms)]   │
│  Columns: 6  |  Rows: 1       │ │ Frame 0 │ 120ms           │
│                               │ │ Frame 1 │ 100ms           │
│                               │ │ Frame 2 │ 100ms           │
│                               │ │ Frame 3 │ 120ms           │
│                               │ │ Frame 4 │ 100ms           │
│                               │ │ Frame 5 │ 100ms           │
└───────────────────────────────┴─────────────────────────────┘
```

---

## 1. Spritesheet Slicing & Metrics

When importing a character or effect sprite sheet (`.png`):
- **Columns & Rows**: Specify the number of horizontal columns and vertical rows in the image.
- **Automatic Frame Dimension Calculation**: utiLITI calculates the resulting `Frame Width` and `Frame Height` in pixels.
- **Manual Overrides**: You can also set explicit frame width and height to automatically deduce column/row counts.
- **Dimension Validation**: If the image dimensions are not evenly divisible by the frame dimensions, utiLITI flags a warning to prevent misaligned clipping.

---

## 2. Keyframe Duration Table

LITIENGINE supports variable keyframe durations, enabling fluid animation pacing (e.g. holding an anticipation frame longer before an attack swing):

- **Individual Durations**: Double-click any row in the duration table to specify its duration in milliseconds (e.g. `120ms`).
- **Batch Uniform Duration**: Set a duration value and click **Apply to All** to instantly synchronize all frames.
- **Total Duration Summary**: The panel displays the total animation loop time (e.g. `640ms total`).

---

## 3. Live Animation Preview Player

The animated canvas preview provides rich playback testing:

- **Playback Controls**:
  - **Play / Pause (`▶` / `⏸`)**: Start or stop animation playback.
  - **Step Forward / Backward (`⏭` / `⏮`)**: Advance or reverse the animation one frame at a time.
  - **Playback Speed**: Adjust speed multipliers (`0.25x`, `0.5x`, `1.0x`, `2.0x`) for slow-motion animation tuning.
  - **Loop Toggle**: Test single-shot vs. repeating animations.
- **Zoom Factor**: Switch between `1x`, `2x`, `4x`, and `8x` zoom levels with crisp nearest-neighbor pixel scaling.
- **Current Frame Display**: Live indicator showing active frame index and elapsed milliseconds.

---

## 4. Importing & Exporting Sprite Info Files

- **Import Spritesheets**: **Resources -> Import -> Import Spritesheets...** (`Ctrl + Shift + I`).
- **Import Texture Atlas**: **Resources -> Import -> Import Texture Atlas...** to import LibGDX or generic texture atlases.
- **Export `.info` Files**: Select **Resources -> Export -> Export Spritesheets...** (`Ctrl + E`) to export `.info` text files containing frame metrics and duration arrays.

```properties
# hero-walk.info
width=32
height=32
durations=120,100,100,120,100,100
```
