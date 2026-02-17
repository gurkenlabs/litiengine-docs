---
meta.description: "Learn how to use the LITIENGINE particle system to create visual effects like fire, smoke, explosions, and magic."
meta.keywords: "LITIENGINE, particle, emitter, effect, fire, smoke, visual, Java"
---

# The Particle System

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
    this.getData().setSpawnRate(30);           // Particles per second
    this.getData().setEmitterDuration(0);      // 0 = infinite
    this.getData().setMaxParticles(100);
    
    // Configure particles
    this.getData().setParticleWidth(16);
    this.getData().setParticleHeight(16);
    this.getData().setMinTTL(500);             // Min lifetime (ms)
    this.getData().setMaxTTL(1000);            // Max lifetime (ms)
    
    // Particle appearance
    this.getData().setSpritesheet(Resources.spritesheets().get("fire-particle"));
    
    // Start emitting
    this.activate();
  }
}
```

## Particle Properties

### Lifetime

```java
// Particle lives between 500-1000ms
emitter.getData().setMinTTL(500);
emitter.getData().setMaxTTL(1000);
```

### Velocity and Movement

```java
// Upward movement with random variance
emitter.getData().setVelocityXMin(-20);
emitter.getData().setVelocityXMax(20);
emitter.getData().setVelocityYMin(-50);
emitter.getData().setVelocityYMax(-30);

// Acceleration (gravity, wind)
emitter.getData().setAccelerationXMin(-5);
emitter.getData().setAccelerationXMax(5);
emitter.getData().setAccelerationYMin(-10);
emitter.getData().setAccelerationYMax(-5);
```

### Size and Scale

```java
// Initial size
emitter.getData().setParticleWidth(8);
emitter.getData().setParticleHeight(8);

// Scale over lifetime (start large, shrink)
emitter.getData().setMinStartScale(2.0f);
emitter.getData().setMaxStartScale(2.5f);
emitter.getData().setMinEndScale(0.1f);
emitter.getData().setMaxEndScale(0.3f);
```

### Color and Opacity

```java
// Color transitions over lifetime
emitter.getData().setStartColor(Color.ORANGE);
emitter.getData().setEndColor(Color.RED);

// Fade out
emitter.getData().setMinStartAlpha(1.0f);
emitter.getData().setMaxStartAlpha(1.0f);
emitter.getData().setMinEndAlpha(0.0f);
emitter.getData().setMaxEndAlpha(0.0f);
```

## Particle Types

### Sprite Particles

```java
// Use a spritesheet for particle visuals
Spritesheet sheet = Resources.spritesheets().get("sparkle");
emitter.getData().setSpritesheet(sheet);
```

### Shape Particles

```java
// Render particles as shapes
emitter.getData().setParticleType(ParticleType.SQUARE);
emitter.getData().setParticleType(ParticleType.CIRCLE);
emitter.getData().setParticleType(ParticleType.TRIANGLE);
```

### Text Particles

```java
// Render particles as text
emitter.getData().setParticleType(ParticleType.TEXT);
emitter.getData().setText("★");
emitter.getData().setFont(Resources.fonts().get("gamefont.ttf", 12f));
```

## Emitter Behavior

### One-Shot Effect

```java
// Emit burst of particles once
emitter.getData().setSpawnAmount(50);
emitter.getData().setEmitterDuration(100);
emitter.getData().setLoop(false);
```

### Continuous Effect

```java
// Continuous emission
emitter.getData().setSpawnRate(20);  // Particles per second
emitter.getData().setEmitterDuration(0);  // Infinite
emitter.getData().setLoop(true);
```

### Burst Emission

```java
// Emit bursts at intervals
emitter.getData().setSpawnAmount(30);
emitter.getData().setSpawnRate(0);  // Not continuous
emitter.getData().setBurstMode(true);
emitter.getData().setBurstInterval(2000);  // Every 2 seconds
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

## Common Effects

### Fire

```java
emitter.getData().setVelocityYMin(-80);
emitter.getData().setVelocityYMax(-40);
emitter.getData().setStartColor(Color.YELLOW);
emitter.getData().setEndColor(Color.RED);
emitter.getData().setMinStartScale(1.5f);
emitter.getData().setMaxEndScale(0.2f);
```

### Smoke

```java
emitter.getData().setVelocityYMin(-30);
emitter.getData().setVelocityYMax(-15);
emitter.getData().setStartColor(Color.DARK_GRAY);
emitter.getData().setEndColor(Color.LIGHT_GRAY);
emitter.getData().setMinStartAlpha(0.8f);
emitter.getData().setMaxEndAlpha(0.0f);
```

### Explosion

```java
emitter.getData().setSpawnAmount(100);
emitter.getData().setEmitterDuration(100);
emitter.getData().setVelocityXMin(-100);
emitter.getData().setVelocityXMax(100);
emitter.getData().setVelocityYMin(-100);
emitter.getData().setVelocityYMax(100);
```

## Performance Tips

1. **Limit max particles**: Set reasonable `maxParticles` values
2. **Use sprite sheets**: More efficient than shapes for complex particles
3. **Recycle emitters**: Reuse emitters instead of creating new ones
4. **Suspend when off-screen**: Emitters outside camera view should be suspended

## See Also

- [Dynamic Lighting](/docs/advanced/dynamic-lighting/) - Lighting effects
- [Render Engine](/docs/game-api/render-engine/) - Rendering system
