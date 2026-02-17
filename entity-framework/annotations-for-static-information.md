---
meta.description: "Learn how to use annotations in LITIENGINE to configure entity properties like size, collision, movement, and combat stats."
meta.keywords: "LITIENGINE, annotation, EntityInfo, CollisionInfo, MovementInfo, CombatInfo, Java"
---

# Annotations for Static Information

LITIENGINE uses Java annotations to define static entity properties. These annotations provide metadata that is applied when entities are instantiated from map objects.

## Available Annotations

### @EntityInfo

Basic entity configuration:

```java
@EntityInfo(
  width = 32,              // Entity width in pixels
  height = 32,             // Entity height in pixels
  renderType = RenderType.NORMAL  // Rendering layer
)
public class MyEntity extends Entity {
  // ...
}
```

**Properties:**
| Property | Type | Description |
|----------|------|-------------|
| `width` | int | Entity width (pixels) |
| `height` | int | Entity height (pixels) |
| `renderType` | RenderType | Layer for rendering |

### @CollisionInfo

Collision detection configuration:

```java
@CollisionInfo(
  collision = true,            // Enable collision
  collisionBoxWidth = 28,      // Collision box width
  collisionBoxHeight = 28,     // Collision box height
  collisionBoxAlign = Align.CENTER,     // Horizontal alignment
  collisionBoxValign = Valign.MIDDLE    // Vertical alignment
)
public class Wall extends CollisionEntity {
  // ...
}
```

**Properties:**
| Property | Type | Description |
|----------|------|-------------|
| `collision` | boolean | Enable/disable collision |
| `collisionBoxWidth` | int | Collision box width |
| `collisionBoxHeight` | int | Collision box height |
| `collisionBoxAlign` | Align | Horizontal: LEFT, CENTER, RIGHT |
| `collisionBoxValign` | Valign | Vertical: TOP, MIDDLE, BOTTOM |
| `collisionType` | Collision | STATIC, DYNAMIC, ANY, NONE |

### @MovementInfo

Movement properties for mobile entities:

```java
@MovementInfo(
  velocity = 100,              // Pixels per second
  acceleration = 50,           // Acceleration rate
  deceleration = 50,           // Deceleration rate
  turnOnMove = true            // Face movement direction
)
public class Enemy extends Creature {
  // ...
}
```

**Properties:**
| Property | Type | Description |
|----------|------|-------------|
| `velocity` | float | Maximum speed (pixels/sec) |
| `acceleration` | float | Speed increase rate |
| `deceleration` | float | Speed decrease rate |
| `turnOnMove` | boolean | Auto-face movement direction |

### @CombatInfo

Combat and health configuration:

```java
@CombatInfo(
  hitpoints = 100,             // Maximum HP
  team = 1,                    // Team identifier
  isIndestructible = false,    // Cannot be damaged
  isTarget = true              // Can be targeted
)
public class Player extends Creature {
  // ...
}
```

**Properties:**
| Property | Type | Description |
|----------|------|-------------|
| `hitpoints` | int | Maximum hitpoints |
| `team` | int | Team ID for friend/foe |
| `isIndestructible` | boolean | Immune to damage |
| `isTarget` | boolean | Can be targeted by abilities |

### @AnimationInfo

Animation configuration:

```java
@AnimationInfo(
  spritePrefix = "player",     // Spritesheet name prefix
  spriteBatched = true         // Use sprite batching
)
public class Player extends Creature {
  // ...
}
```

**Properties:**
| Property | Type | Description |
|----------|------|-------------|
| `spritePrefix` | String | Prefix for spritesheet lookup |
| `spriteBatched` | boolean | Enable sprite batching |

### @AbilityInfo

Ability configuration (see [Ability Framework](/docs/control-entities/ability-framework/)):

```java
@AbilityInfo(
  cooldown = 1000,             // Milliseconds between uses
  duration = 500,              // Execution duration
  value = 100,                 // Custom value (damage, etc.)
  range = 200                  // Maximum range
)
public class Fireball extends Ability {
  // ...
}
```

## Combining Annotations

Use multiple annotations for complete entity configuration:

```java
@EntityInfo(width = 18, height = 18)
@MovementInfo(velocity = 70, acceleration = 10)
@CollisionInfo(collisionBoxWidth = 14, collisionBoxHeight = 16, collision = true)
@CombatInfo(hitpoints = 50, team = 1)
@AnimationInfo(spritePrefix = "gurknukem")
public class Player extends Creature {
  
  public Player() {
    super("gurknukem");
  }
}
```

## Annotation vs Runtime Configuration

Annotations define **static defaults** that can be overridden at runtime:

```java
@EntityInfo(width = 32, height = 32)
@MovementInfo(velocity = 100)
public class Enemy extends Creature {
  
  public void speedBoost() {
    // Override annotation value at runtime
    this.setVelocity(200);
  }
}
```

## Map Object Override

Properties set in the Tiled editor or utiLITI can override annotation defaults:

```java
// Annotation provides defaults
@MovementInfo(velocity = 50)

// Map object can specify custom velocity
// This overrides the annotation value when loaded
```

## Creating Custom Annotations

Define custom annotations for game-specific data:

```java
@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.TYPE)
public @interface EnemyInfo {
  int aggroRange() default 200;
  int xpReward() default 10;
  String[] lootTable() default {};
}

@EnemyInfo(aggroRange = 300, xpReward = 25)
public class Boss extends Creature {
  // ...
}
```

## See Also

- [Default Entity Types](/docs/entity-framework/default-entity-types/) - Built-in entity classes
- [Ability Framework](/docs/control-entities/ability-framework/) - Ability annotations
- [Custom Properties](/docs/tile-maps/custom-properties/) - Runtime property configuration
