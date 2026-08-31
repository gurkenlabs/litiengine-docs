---
title: Texture Atlases
icon: lucide/image
description: Learn how to create, structure, and animate sprite sheets and texture
  atlases in LITIENGINE for 2D characters and environment props.
keywords: [LITIENGINE, texture atlas, spritesheet, sprite, animation, Java, pixel
    art]
tags: [texture-atlas, spritesheet, aseprite, pixel-art, animations]
---
# Texture Atlases & Spritesheets

A **Texture Atlas** (or **Spritesheet**) combines multiple animation frames or graphical tiles into a single contiguous image file. In 2D game development with Java AWT and LITIENGINE, using spritesheets dramatically improves memory efficiency, cache locality, and rendering speed.

---

## Why Use Texture Atlases?

1. **Reduced Memory Overhead**: Packing multiple frames into one image reduces image descriptor overhead.
2. **Simplified Asset Organization**: Keeps all directional animation frames in self-contained files.
3. **Optimized Frame Slicing**: LITIENGINE automatically calculates grid columns and rows based on frame dimensions.

---

## Naming Conventions & Auto-Detection

LITIENGINE uses standardized sprite naming patterns to automatically link spritesheets to `Creature` and `Prop` entities without requiring manual code bindings:

### 1. Creature Entity Animations

Pattern: `{spritePrefix}-{action}-{direction}.{ext}`

```text
player-idle-down.png
player-idle-up.png
player-walk-left.png
player-walk-right.png
player-attack-down.png
```

When an entity is declared with `@AnimationInfo(spritePrefix = "player")`, the engine's `CreatureAnimationController` automatically detects and plays `idle`, `walk`, and `dead` animations matching the entity's facing direction.

### 2. Prop State Sprites

Pattern: `prop-{name}-{state}.{ext}`

```text
prop-chest-closed.png
prop-chest-open.png
prop-barrel-intact.png
prop-barrel-damaged.png
prop-barrel-destroyed.png
```

---

## Creating & Using Spritesheets

### Programmatic Registration

```java title="src/main/java/com/example/game/GameSprites.java"
package com.example.game;

import de.gurkenlabs.litiengine.graphics.Spritesheet;
import de.gurkenlabs.litiengine.resources.Resources;
import java.awt.image.BufferedImage;

public class GameSprites {
  public static void registerCustomSprites() {
    // 1. Direct loading from file path (path, frameWidth, frameHeight)
    Spritesheet heroWalk = Resources.spritesheets().load("sprites/hero-walk.png", 24, 32);

    // 2. Wrap an existing BufferedImage
    BufferedImage rawImage = Resources.images().get("sprites/monsters.png");
    Spritesheet monsterSheet = new Spritesheet(rawImage, "monster-slime", 16, 16);
    Resources.spritesheets().add("monster-slime", monsterSheet);
  }
}
```

### Direct Frame Extraction

```java
// Retrieve a specific keyframe from a spritesheet
Spritesheet sheet = Resources.spritesheets().get("hero-walk");
BufferedImage frame2 = sheet.getSprite(2); // 0-indexed frame
```

---

## Animation Timing & Custom Durations

By default, LITIENGINE plays animation frames at **100ms** per frame (10 FPS). You can customize frame timing in three ways:

1. **In Sprite Info Files**: Using semicolon notation (e.g. `hero-attack.png,32,32;80,40,200,100`).
2. **In the utiLITI Editor**: Select the spritesheet in the **Spritesheets Panel** and edit individual frame millisecond durations.
3. **In Java Code**:
   ```java
   Spritesheet sheet = Resources.spritesheets().get("hero-walk");
   sheet.setKeyFrameDurations(120, 120, 120, 120);
   ```

---

## Recommended Tools & Workflow

- **[Aseprite](https://www.aseprite.org/)**: Industry-standard animated pixel art editor with JSON spritesheet export.
- **[Tiled Map Editor](https://www.mapeditor.org/)**: Map and tileset design tool integrated with LITIENGINE `.tmx` loading.
- **utiLITI**: LITIENGINE's native editor for editing spritesheet metadata, previewing frame loops, and building `.litidata` archives.

---

## Related Documentation

<div class="grid cards" markdown>

- :material-library:{ .lg .middle } **[Resource Management Overview](README.md)**

    ---

    Learn how the static `Resources` hub manages in-memory caching and `.litidata` bundles.

- :material-file-document-edit:{ .lg .middle } **[Sprite Info Files](sprite-info-files.md)**

    ---

    Batch import spritesheets and custom keyframe durations via plain text `.info` files.

- :material-animation-play:{ .lg .middle } **[Animation Controller](../control-entities/animation-controller.md)**

    ---

    Configure state machines and animation rules for creatures and props.

</div>
