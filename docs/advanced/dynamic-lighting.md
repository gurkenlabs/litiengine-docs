---
title: Dynamic Lighting
icon: lucide/sun
description: Learn how to use dynamic lighting in LITIENGINE with LightSource entities
  to create atmospheric illumination effects.
keywords: [LITIENGINE, dynamic lighting, light source, ambient, shadow, Java]
tags: [lighting, dynamic-light, shadows, ambient, shaders, effects]
---
# Dynamic Lighting

Dynamic lighting in LITIENGINE uses `LightSource` entities to illuminate the game world in real-time. This creates atmospheric effects like torches, lamps, and spell glow.

## How Dynamic Lighting Works

1. **Ambient Light**: A base illumination level for the entire map
2. **Light Sources**: Point lights that illuminate surrounding areas
3. **Shadows**: Static geometry can cast shadows from light sources
4. **Color Blending**: Multiple light colors blend together

## Ambient Light

Set the base illumination for an environment:

```java
// Set ambient light color for the active environment
Color ambient = new Color(60, 60, 80); // Dim blue-ish ambient
if (Game.world().environment().getAmbientLight() != null) {
  Game.world().environment().getAmbientLight().setColor(ambient);
}
```

In map properties (via utiLITI or Tiled), ambient light is configured on the map using the `AMBIENTLIGHT` property with a hexadecimal color (e.g. `#3d3d50`).

## Creating Light Sources

### Via utiLITI

1. Add a **LightSource** entity to your map
2. Configure intensity, color, and shape type in the Entity Inspector panel

### Via Code

```java
// Create an active orange elliptical light source
LightSource torch = new LightSource(150, Color.ORANGE, LightSource.Type.ELLIPSE, true);
torch.setLocation(100, 100);

// Add to environment
Game.world().environment().add(torch);
```

## Light Properties

### Intensity

Controls the radius of illumination in pixels:

```java
light.setIntensity(100); // Small light
light.setIntensity(200); // Medium light
light.setIntensity(400); // Large light
```

### Color

```java
// Warm light (torch)
light.setColor(Color.ORANGE);

// Cool light (magic)
light.setColor(Color.CYAN);

// Dim light
light.setColor(new Color(200, 150, 100));

// Bright white
light.setColor(Color.WHITE);
```

### Shape

Light sources support elliptical or rectangular shapes via `LightSource.Type`:

```java
// Circular/elliptical light
light.setLightShapeType(LightSource.Type.ELLIPSE);

// Rectangular light
light.setLightShapeType(LightSource.Type.RECTANGLE);
```

### Torch Flickering

You can easily simulate organic torch flickering by updating intensity in the game loop:

```java
Game.loop().attach(() -> {
  // Random small fluctuation around base intensity
  int flicker = Game.random().nextInt(-8, 8);
  torch.setIntensity(150 + flicker);
});
```

## Dynamic Light Behavior

### Moving Lights

Lights can track moving characters:

```java
public class TorchBearer extends Creature {
  private LightSource torchLight;

  public TorchBearer() {
    super("torchbearer");
    this.torchLight = new LightSource(120, Color.ORANGE, LightSource.Type.ELLIPSE, true);
  }

  @Override
  public void loaded() {
    super.loaded();
    Game.world().environment().add(this.torchLight);
  }

  @Override
  public void update() {
    super.update();
    // Anchor light to the center of the creature
    torchLight.setLocation(
      this.getCenter().getX() - torchLight.getWidth() / 2.0,
      this.getCenter().getY() - torchLight.getHeight() / 2.0
    );
  }
}
```

### Toggling Lights

```java
// Turn light on or off
light.activate();
light.deactivate();

// Or toggle between states
light.toggle();

// Check current state
boolean isOn = light.isActive();

// Or toggle via message
light.sendMessage(this, LightSource.TOGGLE_MESSAGE);
```

### Animated Lights

Pulsing or animated lighting:

```java
Game.loop().attach(() -> {
  float pulse = (float) Math.sin(Game.time().now() / 200.0) * 0.3f + 0.7f;
  light.setIntensity((int)(150 * pulse));
});
```

## Performance Considerations

Dynamic lighting is computationally expensive:

1. **Limit light count**: Fewer lights = better performance
2. **Use appropriate intensity**: Smaller lights are faster to calculate
3. **Disable when not needed**: Turn off lights in inactive areas
4. **Consider static lighting**: Use static lighting where possible

## Configuration

```properties
# Enable/disable dynamic lighting
gfx_enableDynamicShadows=true

# Ambient light settings
gfx_ambientLight=3d3d50
gfx_ambientAlpha=0.8
```

## See Also

- [Static Lighting](static-lighting.md) - Pre-baked lighting
- [Environment](../game-api/game-world.md) - Environment management
- [Particle System](particle-system.md) - Visual effects

## Programmatic LightSource Management

You can spawn, configure, and animate `LightSource` entities at runtime in pure Java:

```java
package com.example.game.lighting;

import de.gurkenlabs.litiengine.Game;
import de.gurkenlabs.litiengine.entities.LightSource;
import java.awt.Color;
import java.awt.geom.Point2D;

public class TorchLight {
  public static LightSource createTorch(double x, double y) {
    // 1. Create a radial ellipse light source (intensity = 120, warm amber color, active)
    Color warmGlow = new Color(255, 180, 50, 180);
    LightSource torch = new LightSource(120, warmGlow, LightSource.Type.ELLIPSE, true);
    torch.setLocation(x, y);

    // 2. Add to active environment
    Game.world().environment().add(torch);

    // 3. Add ambient world darkness (RGBA)
    Game.world().environment().getAmbientLight().setColor(new Color(10, 15, 25, 220));

    return torch;
  }
}
```

### Animating Light Flicker

```java
// Create a flickering torch flame effect in your game loop
Game.loop().attach(Game.world().environment(), () -> {
  int jitter = (int) (Math.random() * 8) - 4;
  torch.setIntensity(120 + jitter);
});
```
