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

### Core `Emitter` Methods

| Method Signature | Return Type | Description |
| :--- | :--- | :--- |
| `data()` | `EmitterAttributes` | Accesses the configurable particle and spawn attributes object. |
| `activate()` / `deactivate()` | `void` | Starts or stops particle emission and lifecycle processing. |
| `pause()` / `setPaused(boolean)` | `void` | Suspends particle updates and spawning without deallocating state. |
| `delete()` | `void` | Deactivates and removes the emitter from the active environment. |
| `getParticles()` | `List<Particle>` | Returns the active collection of living particles managed by this emitter. |
| `setTimeToLive(int duration)` | `void` | Sets lifespan of the emitter entity in milliseconds (0 for infinite). |
| `onFinished(EmitterFinishedListener c)` | `void` | Registers a callback invoked when a finite emitter completes and expires. |
| `onSpawned(EmitterSpawnedListener c)` | `void` | Registers a callback invoked each time a particle is spawned. |

### Configurable Attributes (`emitter.data()`)

| Method Signature | Return Type | Description |
| :--- | :--- | :--- |
| `setParticleType(ParticleType type)` | `void` | Sets the particle primitive (`RECTANGLE`, `ELLIPSE`, `LINE`, `SPRITE`, `TEXT`). |
| `setParticleWidth(RangeAttribute<Float>)` | `void` | Sets particle width range in pixels (`getParticleWidth().setMin() / setMax()`). |
| `setParticleHeight(RangeAttribute<Float>)` | `void` | Sets particle height range in pixels (`getParticleHeight().setMin() / setMax()`). |
| `getParticleTTL()` | `RangeAttribute<Long>` | Configurable lifetime bounds (in milliseconds) per spawned particle. |
| `setMaxParticles(int count)` | `void` | Limits maximum concurrent alive particles spawned by this emitter. |
| `setSpawnRate(int delayMs)` | `void` | Sets the interval delay in milliseconds between successive spawn ticks. |
| `setSpawnAmount(int count)` | `void` | Sets the number of particles spawned during each spawn tick. |
| `setEmitterDuration(int durationMs)` | `void` | Emitter duration in milliseconds (`0` for indefinite / continuous). |
| `setColors(Color... colors)` | `void` | Configures the color palette from which particles randomly draw colors. |
| `setFade(boolean fade)` | `void` | Linearly fades particle opacity to zero over its lifetime. |
| `setSpritesheet(Spritesheet / String)` | `void` | Binds a spritesheet texture for `SPRITE` particle types. |
| `getVelocityX()` / `getVelocityY()` | `RangeAttribute<Float>` | Initial horizontal and vertical velocities. |
| `getAccelerationX()` / `getAccelerationY()` | `RangeAttribute<Float>` | Per-tick acceleration applied to velocity (e.g. gravity, wind). |

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
import de.gurkenlabs.litiengine.attributes.RangeAttribute;
import de.gurkenlabs.litiengine.graphics.emitters.Emitter;
import de.gurkenlabs.litiengine.graphics.emitters.particles.ParticleType;
import de.gurkenlabs.litiengine.resources.Resources;

public class FireEmitter extends Emitter {

  public FireEmitter(double x, double y) {
    super(x, y);

    // Configure emitter
    this.data().setSpawnRate(30); // Milliseconds between spawns
    this.data().setEmitterDuration(0); // 0 = infinite
    this.data().setMaxParticles(100);

    // Configure particles
    this.data().setParticleWidth(new RangeAttribute<>(12f, 16f));
    this.data().setParticleHeight(new RangeAttribute<>(12f, 16f));
    this.data().getParticleTTL().setMin(500L); // Min lifetime (ms)
    this.data().getParticleTTL().setMax(1000L); // Max lifetime (ms)

    // Particle appearance
    this.data().setParticleType(ParticleType.SPRITE);
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
// Particle size range (min/max in pixels)
emitter.data().setParticleWidth(new RangeAttribute<>(4f, 8f));
emitter.data().setParticleHeight(new RangeAttribute<>(4f, 8f));

// Or adjust existing range bounds directly:
emitter.data().getParticleWidth().setMin(4f);
emitter.data().getParticleWidth().setMax(8f);
```

### Color and Opacity

```java
// Base particle colors (emitter randomly samples from configured palette)
emitter.data().setColors(Color.ORANGE, Color.YELLOW, Color.RED);

// Enable linear opacity fade-out towards zero over particle lifespan
emitter.data().setFade(true);
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
// Render particles as text drawn from configured string options
emitter.data().setParticleType(ParticleType.TEXT);
emitter.data().setTexts(List.of("CRIT!", "150", "MISS"));
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

Create custom particle rendering and behavior by extending `Particle` and implementing its `render` and `update` methods:

```java
import java.awt.Color;
import java.awt.Graphics2D;
import java.awt.geom.Point2D;
import de.gurkenlabs.litiengine.attributes.RangeAttribute;
import de.gurkenlabs.litiengine.graphics.emitters.Emitter;
import de.gurkenlabs.litiengine.graphics.emitters.particles.Particle;

public class SparkParticle extends Particle {

  public SparkParticle(float width, float height) {
    super(width, height);
    this.setColor(Color.YELLOW);
  }

  @Override
  public void update(Point2D emitterOrigin, float updateRatio) {
    super.update(emitterOrigin, updateRatio);
    // Custom particle logic on update ticks
  }

  @Override
  public void render(Graphics2D g, Point2D emitterOrigin) {
    Point2D loc = this.getRenderLocation(emitterOrigin);
    g.setColor(this.getColor());
    g.fillRect((int) loc.getX(), (int) loc.getY(), (int) this.getWidth(), (int) this.getHeight());
  }
}

// Override createNewParticle() on a custom Emitter to spawn your custom particle:
public class SparkEmitter extends Emitter {
  public SparkEmitter(double x, double y) {
    super(x, y);
    this.data().setParticleWidth(new RangeAttribute<>(4f, 6f));
    this.data().setParticleHeight(new RangeAttribute<>(4f, 6f));
  }

  @Override
  protected Particle createNewParticle() {
    float width = this.data().getParticleWidth().getRandomNumber().floatValue();
    float height = this.data().getParticleHeight().getRandomNumber().floatValue();
    return new SparkParticle(width, height).init(this.data());
  }
}
```

## Particle Recipes Cookbook

Below are complete, copy-paste ready emitter classes for common 2D visual effects:

### 1. Torch & Campfire Flame

```java
import java.awt.Color;
import de.gurkenlabs.litiengine.attributes.RangeAttribute;
import de.gurkenlabs.litiengine.graphics.emitters.Emitter;
import de.gurkenlabs.litiengine.graphics.emitters.particles.ParticleType;

public class CampfireEmitter extends Emitter {
  public CampfireEmitter(double x, double y) {
    super(x, y);
    this.setWidth(16);
    this.setHeight(16);

    this.data().setParticleType(ParticleType.ELLIPSE);
    this.data().setParticleWidth(new RangeAttribute<>(4f, 8f));
    this.data().setParticleHeight(new RangeAttribute<>(4f, 8f));
    this.data().setSpawnRate(25);
    this.data().getParticleTTL().setMin(400L);
    this.data().getParticleTTL().setMax(800L);

    // Float upwards with slight horizontal jitter
    this.data().getVelocityX().setMin(-10f);
    this.data().getVelocityX().setMax(10f);
    this.data().getVelocityY().setMin(-45f);
    this.data().getVelocityY().setMax(-20f);

    // Warm embers that fade out over time
    this.data().setColors(new Color(255, 200, 50, 220), new Color(255, 100, 30, 220));
    this.data().setFade(true);
  }
}
```

### 2. Explosion / Impact Burst

```java
import java.awt.Color;
import de.gurkenlabs.litiengine.attributes.RangeAttribute;
import de.gurkenlabs.litiengine.graphics.emitters.Emitter;
import de.gurkenlabs.litiengine.graphics.emitters.particles.ParticleType;

public class ExplosionEmitter extends Emitter {
  public ExplosionEmitter(double x, double y) {
    super(x, y);
    this.setWidth(10);
    this.setHeight(10);

    this.data().setParticleType(ParticleType.RECTANGLE);
    this.data().setParticleWidth(new RangeAttribute<>(3f, 6f));
    this.data().setParticleHeight(new RangeAttribute<>(3f, 6f));
    this.data().setSpawnAmount(60);
    this.data().setEmitterDuration(150);
    this.data().getParticleTTL().setMin(200L);
    this.data().getParticleTTL().setMax(500L);

    // Radial explosive velocity in all directions
    this.data().getVelocityX().setMin(-120f);
    this.data().getVelocityX().setMax(120f);
    this.data().getVelocityY().setMin(-120f);
    this.data().getVelocityY().setMax(120f);

    this.data().setColors(new Color(255, 120, 0, 255), new Color(255, 200, 50, 255));
    this.data().setFade(true);
  }
}
```

### 3. Rain Weather Emitter

```java
import java.awt.Color;
import de.gurkenlabs.litiengine.Game;
import de.gurkenlabs.litiengine.attributes.RangeAttribute;
import de.gurkenlabs.litiengine.graphics.emitters.Emitter;
import de.gurkenlabs.litiengine.graphics.emitters.particles.ParticleType;

public class RainEmitter extends Emitter {
  public RainEmitter() {
    super(0, 0);
    // Span across the map or active camera viewport
    this.setWidth(Game.world().environment().getMap().getSizeInPixels().getWidth());
    this.setHeight(10);

    this.data().setParticleType(ParticleType.RECTANGLE);
    this.data().setParticleWidth(new RangeAttribute<>(1f, 1f));
    this.data().setParticleHeight(new RangeAttribute<>(6f, 10f));
    this.data().setSpawnRate(80);

    // Fall downwards with slight wind angle
    this.data().getVelocityX().setMin(-15f);
    this.data().getVelocityX().setMax(-5f);
    this.data().getVelocityY().setMin(180f);
    this.data().getVelocityY().setMax(240f);

    this.data().setColors(new Color(150, 190, 255, 160));
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
