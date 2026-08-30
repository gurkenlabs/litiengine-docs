---
title: Sprite Info Files
icon: lucide/file-text
description: Batch import spritesheets and configure custom animation keyframe durations
  using .info and .sprite metadata files in LITIENGINE.
keywords: [LITIENGINE, java, game engine, 2D, sprite info files, batch import, spritesheet]
tags: [sprite-info, spritesheet, batch-import, frame-durations, timing]
---
# Sprite Info Files

When managing dozens or hundreds of character animations, importing spritesheets one by one can be tedious. LITIENGINE provides a batch-import mechanism using plain-text **Sprite Info Files** (`.info` or `.sprite`).

A sprite info file defines the file path, frame dimensions, and optional per-frame duration timing for multiple spritesheets in a clean, human-readable format.

---

## File Syntax & Schema

Each line in a sprite info file defines a single spritesheet. Empty lines and comment lines starting with `#` are ignored:

```text
{FILENAME}.{EXTENSION},{FRAME_WIDTH},{FRAME_HEIGHT}(;{KEYFRAME_DURATIONS})
```

### Parameter Breakdown

| Field | Required | Description |
|:---|:---|:---|
| `{FILENAME}.{EXTENSION}` | Yes | The filename and extension of the spritesheet image (e.g. `hero-walk.png`). |
| `{FRAME_WIDTH}` | Yes | The width in pixels of an individual animation frame. |
| `{FRAME_HEIGHT}` | Yes | The height in pixels of an individual animation frame. |
| `{KEYFRAME_DURATIONS}` | Optional | Semicolon followed by a comma-separated list of keyframe durations in milliseconds. |

!!! tip "Default Frame Duration"
    If `{KEYFRAME_DURATIONS}` is omitted, the engine uses the default animation frame rate (typically `100ms` per frame, or 10 FPS).

---

## Example Sprite Info File

```text title="sprites/characters.info"
# ==============================================================================
# Player Character Spritesheets
# ==============================================================================
hero-idle-down.png,24,32
hero-idle-up.png,24,32
hero-idle-left.png,24,32
hero-idle-right.png,24,32

# Walk animations with uniform 120ms frame delays
hero-walk-down.png,24,32;120,120,120,120
hero-walk-up.png,24,32;120,120,120,120
hero-walk-left.png,24,32;120,120,120,120
hero-walk-right.png,24,32;120,120,120,120

# Attack animation with custom variable frame timing (anticipation -> strike -> recovery)
hero-attack-down.png,32,32;80,40,200,100

# ==============================================================================
# Environment Props & Scenery
# ==============================================================================
prop-torch-lit.png,16,24;150,150,150,150
prop-campfire.png,32,32;100,100,100,100
prop-chest-intact.png,16,16
```

---

## Loading Sprite Info Files in Code

Load and register all spritesheets declared in a sprite info file using `Resources.spritesheets().loadFrom(...)`:

```java title="src/main/java/com/example/game/AssetLoader.java"
package com.example.game;

import de.gurkenlabs.litiengine.graphics.Spritesheet;
import de.gurkenlabs.litiengine.resources.Resources;
import java.util.List;

public class AssetLoader {
  public static void loadCharacterSprites() {
    // Batch load and cache all spritesheets declared in the .info file
    List<Spritesheet> loaded = Resources.spritesheets().loadFrom("sprites/characters.info");
    System.out.println("Successfully registered " + loaded.size() + " spritesheets!");
  }
}
```

---

## See Also

- **[Resource Management Overview](/resource-management/)** — Central `Resources` caching API
- **[Texture Atlases](/resource-management/texture-atlas/)** — Sprite sheet organization and animation guidelines
- **[Animation Controller](/control-entities/animation-controller/)** — State-driven entity animation controllers
