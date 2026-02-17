---
meta.description: "Learn how to use dynamic lighting in LITIENGINE with LightSource entities to create atmospheric illumination effects."
meta.keywords: "LITIENGINE, dynamic lighting, light source, ambient, shadow, Java"
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
// Set ambient light color (affects entire map)
Color ambient = new Color(60, 60, 80); // Dim blue-ish ambient
Game.world().environment().setAmbientLight(ambient);
```

Or configure in `config.properties`:

```properties
gfx_ambientLight=3d3d50
gfx_ambientAlpha=0.8
```

## Creating Light Sources

### Via utiLITI

1. Add a **LightSource** entity to your map
2. Configure intensity, color, and shape in the Properties panel

### Via Code

```java
LightSource torch = new LightSource();
torch.setLocation(100, 100);
torch.setIntensity(150);           // Light radius
torch.setColor(Color.ORANGE);      // Light color
torch.setShape(LightSource.ELLIPSE); // Light shape

// Add to environment
Game.world().environment().add(torch);
```

## Light Properties

### Intensity

Controls the radius of illumination:

```java
light.setIntensity(100);  // Small light
light.setIntensity(200);  // Medium light
light.setIntensity(400);  // Large light
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

```java
// Circular/ellipse light
light.setShape(LightSource.ELLIPSE);

// Rectangular light
light.setShape(LightSource.RECTANGLE);
```

### Flickering

Add flickering effect for torches and fire:

```java
// Enable flicker
light.setFlicker(true);
light.setFlickerIntensity(0.2f);  // 20% intensity variation
light.setFlickerSpeed(100);       // Flicker interval in ms
```

## Shadow Casting

Static collision boxes can cast shadows:

### Enable in utiLITI

1. Select a CollisionBox
2. Enable **Shadow Casting** in properties
3. Set shadow type

### Via Code

```java
CollisionBox wall = new CollisionBox();
wall.setCastShadow(true);
```

## Dynamic Light Behavior

### Moving Lights

Lights can follow entities:

```java
public class TorchBearer extends Creature {
  private LightSource torchLight;
  
  @Override
  public void update() {
    super.update();
    // Light follows entity
    torchLight.setLocation(this.getCenter());
  }
}
```

### Toggling Lights

```java
// Turn light on/off
light.setActive(false);
light.setActive(true);

// Check state
boolean isOn = light.isActive();
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

- [Static Lighting](/docs/advanced/static-lighting/) - Pre-baked lighting
- [Environment](/docs/game-api/game-world/) - Environment management
- [Particle System](/docs/advanced/the-particle-system/) - Visual effects
