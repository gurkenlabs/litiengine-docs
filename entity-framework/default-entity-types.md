---
meta.description: "Learn about the default entity types in LITIENGINE - Entity, CollisionEntity, CombatEntity, Creature, Prop, and their hierarchies."
meta.keywords: "LITIENGINE, entity types, Creature, Prop, CollisionEntity, CombatEntity, Java"
---

# Default Entity Types

LITIENGINE provides a hierarchy of built-in entity types. Each type builds upon the previous, adding more functionality.

## Entity Hierarchy

```
IEntity
  └── Entity (base class)
        └── CollisionEntity (has collision)
              └── CombatEntity (has health/combat)
                    └── Creature (has animation, movement)
                    └── Prop (static/dynamic objects)
```

## Entity

The base class for all game objects.

```java
public class MyEntity extends Entity {
  public MyEntity() {
    super("my-entity");
    setLocation(100, 100);
    setSize(32, 32);
  }
}
```

### Key Properties
- **Name**: Unique identifier
- **Location**: X/Y position in the world
- **Size**: Width and height
- **MapId**: ID from map object
- **Tags**: String tags for categorization
- **RenderType**: Rendering layer (BACKGROUND, GROUND, NORMAL, OVERLAY, UI)

## CollisionEntity

Extends `Entity` with collision detection capabilities.

```java
@EntityInfo(width = 32, height = 32)
@CollisionInfo(collisionBoxWidth = 28, collisionBoxHeight = 28, collision = true)
public class Wall extends CollisionEntity {
  public Wall() {
    super("wall");
  }
}
```

### Collision Types
- **STATIC**: Collides with static geometry
- **DYNAMIC**: Collides with moving objects
- **ANY**: Collides with everything
- **NONE**: No collision

### Key Properties
- Collision box dimensions and offset
- Collision type

## CombatEntity

Extends `CollisionEntity` with health and combat mechanics.

```java
@EntityInfo(width = 32, height = 32)
@CombatInfo(hitpoints = 100, team = 1)
public class Destructible extends CombatEntity {
  public Destructible() {
    super("destructible");
  }
}
```

### Key Properties
- **Hitpoints**: Current and maximum health
- **Team**: For friend/foe identification
- **Indestructible**: Cannot be damaged
- **Target**: Can be targeted by abilities

### Events
```java
combatEntity.onHit(event -> { /* took damage */ });
combatEntity.onDeath(event -> { /* died */ });
combatEntity.onResurrect(event -> { /* revived */ });
```

## Creature

The most feature-rich entity type. Combines collision, combat, movement, and animation.

```java
@EntityInfo(width = 18, height = 18)
@MovementInfo(velocity = 70, acceleration = 10)
@CombatInfo(hitpoints = 50)
@CollisionInfo(collisionBoxWidth = 14, collisionBoxHeight = 16, collision = true)
public class Player extends Creature {
  public Player() {
    super("player"); // spritePrefix
  }
}
```

### Features
- Automatic animation from spritesheets
- Movement controller integration
- Facing direction tracking
- State machine (idle, walking, dead)

### Key Methods
```java
creature.getFacingDirection();      // Current facing direction
creature.setSpritePrefix("prefix"); // For animation lookup
creature.isIdle();                  // Check if not moving
creature.isDead();                  // Check if dead
```

## Prop

Static or interactive objects in the game world.

```java
@EntityInfo(width = 32, height = 32)
@CollisionInfo(collision = true)
public class Barrel extends Prop {
  public Barrel() {
    super("barrel");
  }
}
```

### Prop States
- **INTACT**: More than 50% health or indestructible
- **DAMAGED**: Less than 50% health
- **DESTROYED**: Zero health

### State-based Spritesheets
```
prop-barrel-intact.png
prop-barrel-damaged.png
prop-barrel-destroyed.png
```

## Other Entity Types

### Trigger
Area-based event triggers that activate when entities enter.

```java
Trigger trigger = new Trigger("myTrigger", TriggerActivation.PROPAGATE);
trigger.onActivated(e -> { /* entered */ });
trigger.onDeactivated(e -> { /* exited */ });
```

### LightSource
Dynamic lighting entities.

```java
LightSource light = new LightSource();
light.setIntensity(150);
light.setColor(Color.ORANGE);
```

### Emitter
Particle effect sources.

```java
Emitter emitter = new Emitter("fire");
emitter.getData().setEmitterDuration(5000);
```

### Spawnpoint
Entity spawn locations.

```java
Spawnpoint spawn = new Spawnpoint("start", Direction.RIGHT);
spawn.spawn(new Player());
```

## Choosing the Right Type

| Use Case | Entity Type |
|----------|-------------|
| Decorative object, no interaction | `Entity` |
| Wall, obstacle | `CollisionEntity` |
| Destructible object with health | `CombatEntity` or `Prop` |
| Player, enemies, NPCs | `Creature` |
| Interactive objects | `Prop` |
| Area triggers | `Trigger` |
| Lighting | `LightSource` |
| Particle effects | `Emitter` |

## See Also

- [Entity Framework Overview](/docs/entity-framework/README/) - Entity system intro
- [Annotations](/docs/entity-framework/annotations-for-static-information/) - Configure entities
- [Props](/docs/entity-framework/props/) - Detailed prop documentation
