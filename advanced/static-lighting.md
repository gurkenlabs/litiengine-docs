---
meta.description: "Learn about static lighting in LITIENGINE - pre-baked shadows and ambient occlusion for performant illumination."
meta.keywords: "LITIENGINE, static lighting, shadow, ambient occlusion, baked, performance, Java"
---

# Static Lighting

Static lighting refers to pre-computed shadows and illumination baked into your tile map. It offers better performance than dynamic lighting for fixed light sources.

## When to Use Static Lighting

- **Fixed architecture**: Walls, buildings, trees
- **Non-moving lights**: Lamps, windows, torches that don't move
- **Performance-critical areas**: When you need many light sources
- **Mobile/low-end systems**: Reduce computational load

## Creating Static Shadows

### Via Tiled Editor

1. Create an object layer called `SHADOWBOX`
2. Add rectangles where shadows should appear
3. Shadows are automatically rendered based on these shapes

### Via utiLITI

1. Select the **Shadow** layer
2. Draw shadow polygons over obstacles
3. Set shadow opacity in map properties

## Shadow Layer

The shadow layer defines areas that block light:

```java
// Shadows are automatically rendered from the SHADOWBOX layer
// No code needed - handled by engine during map load
```

## Ambient Occlusion

Create depth with contact shadows:

1. In Tiled, add shadow polygons at the base of walls
2. Use semi-transparent dark colors
3. Overlap slightly with the wall base

## Static vs Dynamic Lighting

| Feature | Static | Dynamic |
|---------|--------|---------|
| Performance | Excellent | Moderate |
| Light movement | Not supported | Supported |
| Real-time shadows | No | Yes |
| Light count | Unlimited | Limited |
| Best for | Architecture | Spells, moving lights |

## Combining Static and Dynamic

For best results, use both:

```java
// Static: Pre-baked building shadows
// Dynamic: Player torch, spell effects

// Base ambient light (static)
Game.world().environment().setAmbientLight(new Color(50, 50, 60));

// Add dynamic player light
LightSource playerLight = new LightSource();
playerLight.setIntensity(80);
playerLight.setColor(Color.ORANGE);
playerLight.setFlicker(true);
Game.world().environment().add(playerLight);
```

## Shadow Opacity

Control shadow darkness:

```properties
# In config.properties
gfx_shadowOpacity=0.7
```

Or at runtime:

```java
// Adjust shadow transparency
Game.graphics().setShadowOpacity(0.8f);  // 80% opacity
```

## Best Practices

1. **Bake what you can**: Use static shadows for immovable objects
2. **Layer strategically**: Place shadow layer below entities but above ground
3. **Match art style**: Ensure shadow style matches your game's aesthetic
4. **Test performance**: Verify static lighting improves your target frame rate

## See Also

- [Dynamic Lighting](/docs/advanced/dynamic-lighting/) - Real-time lighting
- [Environment](/docs/game-api/game-world/) - Environment management
- [Render Engine](/docs/game-api/render-engine/) - Rendering system
