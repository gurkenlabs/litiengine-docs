---
meta.description: "Learn about texture atlases in LITIENGINE - how to create and use sprite sheets for entity animations."
meta.keywords: "LITIENGINE, texture atlas, spritesheet, sprite, animation, Java"
---

# Texture Atlases

Texture atlases (also called spritesheets) combine multiple sprites into a single image file. LITIENGINE uses them for entity animations and tile rendering.

## What is a Texture Atlas?

A texture atlas is a single image containing multiple sub-images (sprites) arranged in a grid or custom layout. Benefits include:

- Reduced memory usage
- Faster rendering (fewer texture swaps)
- Easier asset management

## Sprite Info Files

LITIENGINE uses `.sprite` info files to define spritesheet metadata:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<sprite name="player-idle" width="32" height="32">
  <animations>
    <animation name="idle" keyframes="5" duration="100" loop="true"/>
  </animations>
</sprite>
```

## Importing Spritesheets

### Via utiLITI

1. Open **Resources -> Import Spritesheets...**
2. Select your image file
3. Configure sprite dimensions
4. Set animation properties

### Via Code

```java
BufferedImage image = Resources.images().get("sprites/player.png");
Spritesheet sheet = new Spritesheet(image, "player", 32, 32);
Resources.spritesheets().add("player", sheet);
```

## Animation Configuration

### Frame Dimensions

Set the width and height of each frame:

- If image is 160x32 pixels and each frame is 32x32
- Result: 5 frames horizontally

### Frame Duration

How long each frame displays (milliseconds):

- 100ms = 10 frames per second
- 50ms = 20 frames per second

### Loop Settings

- **Loop**: Animation repeats continuously
- **No Loop**: Animation plays once and stops

## Naming Conventions

For automatic animation detection, follow naming patterns:

### Entity Animations

```
{spritePrefix}-{state}-{direction}.{ext}
```

Examples:
- `player-idle-left.png`
- `player-walk-left.png`
- `enemy-attack-right.png`

### Prop States

```
prop-{name}-{state}.{ext}
```

Examples:
- `prop-barrel-intact.png`
- `prop-barrel-damaged.png`
- `prop-barrel-destroyed.png`

## Using Spritesheets

### In Entities

```java
@AnimationInfo(spritePrefix = "player")
public class Player extends Creature {
  public Player() {
    super("player"); // Uses "player-*" spritesheets
  }
}
```

### Manual Animation

```java
Spritesheet sheet = Resources.spritesheets().get("player-idle");
Animation animation = new Animation(sheet, true, 100); // loop, duration
entity.getAnimationController().play(animation);
```

### Direct Sprite Access

```java
Spritesheet sheet = Resources.spritesheets().get("player-idle");
BufferedImage frame = sheet.getSprite(0); // First frame
g.drawImage(frame, x, y, null);
```

## Creating Spritesheets

### Recommended Tools

- [Aseprite](https://www.aseprite.org/) - Pixel art and animation
- [TexturePacker](https://www.codeandweb.com/texturepacker) - Atlas generation
- [Tiled](https://www.mapeditor.org/) - Built-in tileset editor

### Best Practices

1. **Consistent frame sizes** across animations
2. **Power of 2 dimensions** for compatibility (32, 64, 128, 256)
3. **Minimal padding** between frames
4. **Logical naming** following conventions

## Spritesheet in Game Files

When you save a project in utiLITI, spritesheets are bundled in the `.litidata` file:

```java
Resources.load("game.litidata");
// All spritesheets now available via Resources.spritesheets()
```

## See Also

- [Resource Management](/docs/resource-management/README/) - Loading resources
- [Sprite Info Files](/docs/resource-management/sprite-info-files/) - Sprite metadata format
- [Animation Controller](/docs/control-entities/animation-controller/) - Using animations
