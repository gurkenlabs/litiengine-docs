---
meta.description: "Learn performance optimization techniques for LITIENGINE games including rendering, entity management, and memory usage."
meta.keywords: "LITIENGINE, performance, optimization, FPS, memory, rendering, Java"
---

# Performance Optimization

LITIENGINE is designed to be efficient, but game performance depends on how you use it. This guide covers common optimization techniques.

## Measuring Performance

### Enable Debug Metrics

```java
// Show FPS and tick rate
Game.config().debug().setShowGameMetrics(true);
```

Or in `config.properties`:

```properties
cl_showGameMetrics=true
```

### Custom Metrics

```java
long startTime = System.nanoTime();

// Code to measure

long elapsed = System.nanoTime() - startTime;
System.out.println("Operation took: " + (elapsed / 1_000_000.0) + "ms");
```

## Rendering Optimization

### Reduce Draw Calls

Every render call has overhead. Batch similar operations:

```java
// BAD: Multiple state changes
for (Entity e : entities) {
  g.setColor(e.getColor());
  g.fill(e.getBoundingBox());
}

// GOOD: Batch by color
Map<Color, List<Entity>> byColor = groupByColor(entities);
for (Map.Entry<Color, List<Entity>> entry : byColor.entrySet()) {
  g.setColor(entry.getKey());
  for (Entity e : entry.getValue()) {
    g.fill(e.getBoundingBox());
  }
}
```

### Limit Visible Entities

Only render what's on screen:

```java
@Override
public void render(Graphics2D g) {
  Rectangle2D viewport = Game.world().camera().getViewport();
  
  for (IEntity entity : entities) {
    if (viewport.intersects(entity.getBoundingBox())) {
      // Only render visible entities
      entity.render(g);
    }
  }
}
```

### Use Static Lighting

Pre-bake shadows instead of calculating dynamically:

```properties
gfx_enableDynamicShadows=false
```

See [Static Lighting](/docs/advanced/static-lighting/) for details.

## Entity Management

### Suspend Inactive Entities

Disable updates for off-screen entities:

```java
// In custom entity
@Override
public void update() {
  if (!isOnScreen()) {
    return; // Skip update
  }
  // Normal update logic
}
```

### Object Pooling

Reuse objects instead of creating new ones:

```java
public class BulletPool {
  private static final List<Bullet> pool = new ArrayList<>();
  
  public static Bullet get() {
    if (pool.isEmpty()) {
      return new Bullet();
    }
    return pool.remove(pool.size() - 1);
  }
  
  public static void release(Bullet bullet) {
    bullet.reset();
    pool.add(bullet);
  }
}
```

### Limit Entity Count

```java
// Remove entities when not needed
if (Game.world().environment().getEntities().size() > MAX_ENTITIES) {
  // Remove oldest/distant entities
}
```

## Particle System

### Limit Particle Count

```java
emitter.getData().setMaxParticles(50);  // Set reasonable limit
```

### Suspend Off-Screen Emitters

```java
emitter.setSuspended(!isOnScreen());
```

### Use Simple Particles

Shapes are faster than animated sprites:

```java
emitter.getData().setParticleType(ParticleType.SQUARE);
```

## Memory Management

### Unload Unused Resources

```java
// Clear unused spritesheets
Resources.spritesheets().clear();

// Remove disposed entities
entity.dispose();
```

### Avoid Memory Leaks

```java
// Remove listeners when disposing
public void dispose() {
  Game.loop().detach(this);
  Input.keyboard().removeKeyListener(listener);
}
```

### Use Primitive Collections

For large collections, use primitive arrays:

```java
// Consider using int[] instead of List<Integer> for large datasets
```

## Physics Optimization

### Limit Collision Checks

```java
// Use appropriate collision types
@CollisionInfo(collisionType = Collision.STATIC)  // For walls
@CollisionInfo(collisionType = Collision.DYNAMIC) // For moving entities
```

### Use Simple Collision Shapes

Rectangles are faster than complex polygons:

```java
// Prefer simple collision boxes
collisionEntity.setCollisionBoxWidth(32);
collisionEntity.setCollisionBoxHeight(32);
```

## Configuration

### Frame Rate Settings

```properties
# Limit FPS to reduce CPU usage
cl_maxFps=60

# Enable V-Sync
gfx_vsync=true
```

### Resolution Scaling

```properties
# Reduce internal resolution
gfx_enableResolutionScale=true
```

## Profiling Tips

1. **Profile before optimizing**: Measure to find actual bottlenecks
2. **Test on target hardware**: Low-end systems show issues first
3. **Check GC logs**: Frequent garbage collection indicates memory issues
4. **Use Java VisualVM**: Connect to running game for detailed profiling

## Common Performance Issues

| Issue | Symptom | Solution |
|-------|---------|----------|
| Too many entities | Low FPS | Limit count, use pooling |
| Large spritesheets | Memory spike | Reduce image sizes |
| Excessive particles | Frame drops | Lower particle count |
| Complex collision | Stuttering | Simplify shapes |
| Memory leaks | Gradual slowdown | Dispose resources properly |

## See Also

- [Particle System](/docs/advanced/the-particle-system/) - Particle optimization
- [Entity Framework](/docs/entity-framework/README/) - Entity management
- [Render Engine](/docs/game-api/render-engine/) - Rendering system
