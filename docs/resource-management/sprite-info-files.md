---
title: "Sprite Info Files & Aseprite Pipeline"
icon: "lucide/file-text"
description: "Configure custom animation keyframe durations, batch import spritesheets, and integrate Aseprite pixel art export pipelines in LITIENGINE."
keywords: ["LITIENGINE spritesheets", "sprite info files", "Aseprite export", "keyframe durations", "frame timing", "animation timing"]
tags: ["sprite-info", "spritesheet", "aseprite", "batch-import", "frame-durations", "timing"]
---

# Sprite Info Files & Aseprite Pipeline

LITIENGINE provides a powerful plain-text **Sprite Info File** format (`.info` or `.sprite`) that lets you declare frame dimensions, batch-import asset libraries, and fine-tune individual keyframe timing without writing Java code.

---

## File Syntax & Structure

Each line in a `.info` file defines an individual spritesheet. Lines starting with `#` are treated as comments:

```text
{FILENAME}.{EXTENSION},{FRAME_WIDTH},{FRAME_HEIGHT}(;{KEYFRAME_DURATIONS})
```

### Parameter Breakdown

| Field | Required | Description |
|:---|:---|:---|
| `{FILENAME}.{EXTENSION}` | Yes | Spritesheet image filename (e.g. `hero-attack-right.png`). |
| `{FRAME_WIDTH}` | Yes | Individual animation frame width in pixels. |
| `{FRAME_HEIGHT}` | Yes | Individual animation frame height in pixels. |
| `{KEYFRAME_DURATIONS}` | Optional | Semicolon followed by comma-separated frame durations in milliseconds. |

---

## Custom Keyframe Timing for Combat Animations

In combat and action games, animations look far more impactful when keyframes have variable durations (e.g. holding an anticipation wind-up frame, executing an instant strike, and lingering on recovery):

```text title="sprites/hero.info"
# ==============================================================================
# Player Character Spritesheets (.info format)
# ==============================================================================

# Idle animations: 4 frames at 150ms per frame
hero-idle-down.png,32,32;150,150,150,150
hero-idle-up.png,32,32;150,150,150,150
hero-idle-left.png,32,32;150,150,150,150
hero-idle-right.png,32,32;150,150,150,150

# Walk animations: 4 frames with rapid 100ms cycles
hero-walk-down.png,32,32;100,100,100,100
hero-walk-up.png,32,32;100,100,100,100
hero-walk-left.png,32,32;100,100,100,100
hero-walk-right.png,32,32;100,100,100,100

# Melee Sword Attack: Wind-up (120ms) -> Slash (40ms) -> Impact Hold (180ms) -> Recover (80ms)
hero-attack-down.png,48,48;120,40,180,80
hero-attack-up.png,48,48;120,40,180,80
hero-attack-left.png,48,48;120,40,180,80
hero-attack-right.png,48,48;120,40,180,80
```

---

## Aseprite Export Pipeline

When creating pixel art in [Aseprite](https://www.aseprite.org/), follow these conventions for seamless integration:

### 1. Naming Convention
Name your exported spritesheet PNGs following the standard pattern:
```text
[SPRITE_PREFIX]-[STATE]-[DIRECTION].png
```
* **Examples**: `warrior-idle-down.png`, `warrior-walk-right.png`, `warrior-dead.png`.
* If horizontal mirroring is enabled in your `AnimationController`, you only need to export the `right` direction—LITIENGINE automatically generates flipped `left` sprites at runtime!

### 2. Aseprite Export Settings
1. Go to **File &rarr; Export Sprite Sheet** (`Ctrl + E`).
2. Set **Layout** to **Horizontal Strip** (or uniform Grid).
3. Ensure **Trim** is disabled so all frames maintain consistent canvas origins.
4. Save the PNG and add its entry into your `.info` file.

---

## Batch Loading in Java

Load an entire directory of spritesheets declared in a `.info` file in a single call:

```java title="AssetLoader.java"
package com.example.game;

import de.gurkenlabs.litiengine.graphics.Spritesheet;
import de.gurkenlabs.litiengine.resources.Resources;
import java.util.List;

public class AssetLoader {
  public static void loadAssets() {
    // Loads all spritesheets with custom durations declared in the info file
    List<Spritesheet> sprites = Resources.spritesheets().loadFrom("sprites/hero.info");
    System.out.println("Loaded " + sprites.size() + " animation spritesheets!");
  }
}
```

---

## See Also

<div class="grid cards" markdown>

- :material-image-multiple-outline:{ .lg .middle } **[Texture Atlases](texture-atlas.md)**

    ---

    Organizing spritesheets and texture regions.

- :material-filmstrip:{ .lg .middle } **[Animation Controller](..\control-entities\animation-controller.md)**

    ---

    State-driven animation controllers and direction switching.

</div>

*[Spritesheet]: Image containing sequential animation frames arranged in a grid
*[Resources.spritesheets()]: Spritesheet container and animation frame cache
*[AnimationController]: State machine binding spritesheets to entity locomotion states
