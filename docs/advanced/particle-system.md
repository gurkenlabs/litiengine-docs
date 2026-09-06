---
title: 2D Particle System
icon: lucide/sparkles
description: Learn how to use the LITIENGINE particle system to create visual effects
  like fire, smoke, explosions, and magic.
keywords: [LITIENGINE, particle, emitter, effect, fire, smoke, visual, Java]
tags: [particles, particle-system, emitters, vfx, visual-effects]
---
# 2D Particle System

## Emitter API Method Reference

| Method Signature | Return Type | Description |
| :--- | :--- | :--- |
| `setTimeToLive(int duration)` | `void` | Sets lifespan of the emitter in milliseconds (or -1 for infinite). |
| `setMaxParticles(int count)` | `void` | Limits maximum concurrent alive particles spawned by this emitter. |
| `setSpawnRate(int delayMs)` | `void` | Sets the interval delay between successive particle spawns. |
| `setParticleType(ParticleType type)` | `void` | Sets particle primitive (`RECTANGLE`, `ELLIPSE`, `LINE`, `SPRITE`). |
| `onFinished(EmitterFinishedListener c)` | `void` | Listener invoked when a finite emitter completes and expires. |
| `activate()` / `deactivate()` | `void` | Enables or pauses particle emission. |

---

The LITIENGINE particle system allows you to create dynamic visual effects by emitting and animating large numbers of small sprites or shapes. Use it for fire, smoke, explosions, magic spells, and environmental effects.

## How Particles Work

1. An **Emitter** spawns particles at a defined rate
2. Each **Particle** has properties like position, velocity, size, color, and lifetime
3. Particles are updated every tick and rendered to the screen
4. When a particle's lifetime expires, it is removed

## Creating an Emitter

### Using utiLITI

1. Add an Emitter entity to your map
2. Configure emitter properties in the Properties panel
3. Set particle appearance, behavior, and timing

### Using Code

```java
public class FireEmitter extends Emitter {

  public FireEmitter(double x, double y) {
    super(x, y);

    // Configure emitter
    this.data().setSpawnRate(30); // Milliseconds between spawns
    this.data().setEmitterDuration(0); // 0 = infinite
    this.data().setMaxParticles(100);

    // Configure particles
    this.data().setParticleWidth(16);
    this.data().setParticleHeight(16);
    this.data().getParticleTTL().setMin(500L); // Min lifetime (ms)
    this.data().getParticleTTL().setMax(1000L); // Max lifetime (ms)

    // Particle appearance
    this.data().setSpritesheet(Resources.spritesheets().get("fire-particle"));

    // Start emitting
    this.activate();
  }
}
```

## Particle Properties

### Lifetime

```java
// Particle lives between 500-1000ms
emitter.data().getParticleTTL().setMin(500L);
emitter.data().getParticleTTL().setMax(1000L);
```

### Velocity and Movement

```java
// Upward movement with random variance
emitter.data().getVelocityX().setMin(-20f);
emitter.data().getVelocityX().setMax(20f);
emitter.data().getVelocityY().setMin(-50f);
emitter.data().getVelocityY().setMax(-30f);

// Acceleration (gravity, wind)
emitter.data().getAccelerationX().setMin(-5f);
emitter.data().getAccelerationX().setMax(5f);
emitter.data().getAccelerationY().setMin(-10f);
emitter.data().getAccelerationY().setMax(-5f);
```

### Size and Scale

```java
// Initial size
emitter.data().setParticleWidth(8);
emitter.data().setParticleHeight(8);
```

### Color and Opacity

```java
// Base particle color
emitter.data().setColor(Color.ORANGE);

// Enable color fading over particle lifespan
emitter.data().setFade(true);
emitter.data().setFadeColor(new Color(255, 0, 0, 0));
```

## Particle Types

### Sprite Particles

```java
// Use a spritesheet for particle visuals
Spritesheet sheet = Resources.spritesheets().get("sparkle");
emitter.data().setSpritesheet(sheet);
emitter.data().setParticleType(ParticleType.SPRITE);
```

### Shape Particles

```java
// Render particles as shapes
emitter.data().setParticleType(ParticleType.RECTANGLE);
emitter.data().setParticleType(ParticleType.ELLIPSE);
emitter.data().setParticleType(ParticleType.TRIANGLE);
```

### Text Particles

```java
// Render particles as text
emitter.data().setParticleType(ParticleType.TEXT);
emitter.data().setText("CRIT!");
```

## Emitter Behavior

### One-Shot Effect

```java
// Emit burst of particles once
emitter.data().setSpawnAmount(50);
emitter.data().setEmitterDuration(100);
```

### Continuous Effect

```java
// Continuous emission
emitter.data().setSpawnRate(20); // Milliseconds between spawns
emitter.data().setEmitterDuration(0); // Infinite
```

## Adding Emitters to Environment

```java
FireEmitter fire = new FireEmitter(100, 100);
Game.world().environment().add(fire);
```

## Custom Particles

Create custom particle behavior by extending `Particle`:

```java
public class SparkParticle extends Particle {

  public SparkParticle() {
    super();
    this.setWidth(4);
    this.setHeight(4);
    this.setColor(Color.YELLOW);
  }

  @Override
  public void update(float updateRatio) {
    super.update(updateRatio);

    // Custom behavior: flicker
    if (Game.random().nextFloat() > 0.5f) {
      this.setVisible(!this.isVisible());
    }
  }
}
```

## Particle Recipes Cookbook

Below are complete, copy-paste ready emitter classes for common 2D visual effects:

### 1. Torch & Campfire Flame

```java
import java.awt.Color;
import de.gurkenlabs.litiengine.graphics.emitters.Emitter;
import de.gurkenlabs.litiengine.graphics.emitters.particles.ParticleType;

public class CampfireEmitter extends Emitter {
  public CampfireEmitter(double x, double y) {
    super(x, y);
    this.setWidth(16);
    this.setHeight(16);

    this.data().setParticleType(ParticleType.ELLIPSE);
    this.data().setSpawnRate(25);
    this.data().getParticleTTL().setMin(400L);
    this.data().getParticleTTL().setMax(800L);

    // Float upwards with slight horizontal jitter
    this.data().getVelocityX().setMin(-10f);
    this.data().getVelocityX().setMax(10f);
    this.data().getVelocityY().setMin(-45f);
    this.data().getVelocityY().setMax(-20f);

    // Fade from bright yellow/orange to dark smoky red
    this.data().setColor(new Color(255, 200, 50, 220));
    this.data().setFade(true);
    this.data().setFadeColor(new Color(220, 50, 20, 0));
  }
}
```

### 2. Explosion / Impact Burst

```java
import java.awt.Color;
import de.gurkenlabs.litiengine.graphics.emitters.Emitter;
import de.gurkenlabs.litiengine.graphics.emitters.particles.ParticleType;

public class ExplosionEmitter extends Emitter {
  public ExplosionEmitter(double x, double y) {
    super(x, y);
    this.setWidth(10);
    this.setHeight(10);

    this.data().setParticleType(ParticleType.RECTANGLE);
    this.data().setSpawnAmount(60);
    this.data().setEmitterDuration(150);
    this.data().getParticleTTL().setMin(200L);
    this.data().getParticleTTL().setMax(500L);

    // Radial explosive velocity in all directions
    this.data().getVelocityX().setMin(-120f);
    this.data().getVelocityX().setMax(120f);
    this.data().getVelocityY().setMin(-120f);
    this.data().getVelocityY().setMax(120f);

    this.data().setColor(new Color(255, 120, 0, 255));
    this.data().setFade(true);
    this.data().setFadeColor(new Color(80, 80, 80, 0));
  }
}
```

### 3. Rain Weather Emitter

```java
import java.awt.Color;
import de.gurkenlabs.litiengine.Game;
import de.gurkenlabs.litiengine.graphics.emitters.Emitter;
import de.gurkenlabs.litiengine.graphics.emitters.particles.ParticleType;

public class RainEmitter extends Emitter {
  public RainEmitter() {
    super(0, 0);
    // Span across the map or active camera viewport
    this.setWidth(Game.world().environment().getMap().getSizeInPixels().getWidth());
    this.setHeight(10);

    this.data().setParticleType(ParticleType.RECTANGLE);
    this.data().setParticleWidth(1);
    this.data().setParticleHeight(8);
    this.data().setSpawnRate(80);

    // Fall downwards with slight wind angle
    this.data().getVelocityX().setMin(-15f);
    this.data().getVelocityX().setMax(-5f);
    this.data().getVelocityY().setMin(180f);
    this.data().getVelocityY().setMax(240f);

    this.data().setColor(new Color(150, 190, 255, 160));
  }
}
```

## Performance Tips

1. **Limit max particles**: Set reasonable `maxParticles` values
2. **Use sprite sheets**: More efficient than shapes for complex particles
3. **Recycle emitters**: Reuse emitters instead of creating new ones
4. **Suspend when off-screen**: Emitters outside camera view should be suspended

## See Also

- [Dynamic Lighting](dynamic-lighting.md) - Lighting effects
- [Render Engine](../game-api/render-engine.md) - Rendering system
