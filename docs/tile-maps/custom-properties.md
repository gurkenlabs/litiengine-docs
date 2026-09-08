---
title: Custom Properties
icon: lucide/settings-2
description: Learn how to use custom properties in LITIENGINE to configure map objects
  and entities with custom data.
keywords: [LITIENGINE, custom properties, Tiled, tmx, map object, configuration, entity]
tags: [custom-properties, tmx-properties, metadata, attributes]
---
# Custom Properties

Custom properties allow you to attach arbitrary data to map objects in the Tiled editor or utiLITI. These properties are then accessible at runtime to configure entity behavior.

## Adding Custom Properties

### In utiLITI

1. Select a map object on your map
2. In the Properties panel, find the **Custom Properties** section
3. Click **+** to add a new property
4. Enter the property name and value

### In Tiled Editor

1. Select an object
2. In the Properties view, click **+ Add Property**
3. Choose the property type (string, int, float, bool, color, etc.)
4. Set the name and value

## Built-in Property Names

LITIENGINE recognizes several built-in property names that configure entity behavior:

| Property Key | Java Constant | Type | Description |
|:---|:---|:---|:---|
| `spritesheetName` | `MapObjectProperty.SPRITESHEETNAME` | String | Spritesheet name used for the entity visuals. |
| `collision` | `MapObjectProperty.COLLISION` | Boolean | Enables or disables solid physical collision. |
| `collisionboxWidth` | `MapObjectProperty.COLLISIONBOX_WIDTH` | Float | Width of the collision collider in pixels. |
| `collisionboxHeight` | `MapObjectProperty.COLLISIONBOX_HEIGHT` | Float | Height of the collision collider in pixels. |
| `collisionAlign` | `MapObjectProperty.COLLISION_ALIGN` | Enum | Horizontal collider alignment (`LEFT`, `CENTER`, `RIGHT`). |
| `collisionValign` | `MapObjectProperty.COLLISION_VALIGN` | Enum | Vertical collider alignment (`TOP`, `MIDDLE`, `DOWN`). |
| `collisionType` | `MapObjectProperty.COLLISION_TYPE` | Enum | Physics collider type (`STATIC`, `DYNAMIC`). |
| `velocity` | `MapObjectProperty.MOVEMENT_VELOCITY` | Float | Maximum movement velocity in pixels per second. |
| `acceleration` | `MapObjectProperty.MOVEMENT_ACCELERATION` | Int | Milliseconds to accelerate to top speed. |
| `deceleration` | `MapObjectProperty.MOVEMENT_DECELERATION` | Int | Milliseconds to come to a full stop. |
| `turnOnMove` | `MapObjectProperty.MOVEMENT_TURNONMOVE` | Boolean | Automatically faces the entity towards movement heading. |
| `hitpoints` | `MapObjectProperty.COMBAT_HITPOINTS` | Int | Maximum and initial hit points for combat entities. |
| `indestructible` | `MapObjectProperty.COMBAT_INDESTRUCTIBLE` | Boolean | Prevents combat entity from taking damage. |
| `team` | `MapObjectProperty.COMBAT_TEAM` | Int | Combat team identifier (0 = neutral/player, 1+ = teams). |
| `tags` | `MapObjectProperty.TAGS` | String | Comma-separated tags (e.g. `boss,undead,fire`). |
| `renderType` | `MapObjectProperty.RENDERTYPE` | Enum | Render layer (`BACKGROUND`, `GROUND`, `SURFACE`, `NORMAL`, `OVERLAY`, `UI`). |
| `material` | `MapObjectProperty.PROP_MATERIAL` | Enum | Prop material (`STONE`, `WOOD`, `METAL`, `GLASS`, etc.). |
| `isObstacle` | `MapObjectProperty.PROP_OBSTACLE` | Boolean | Whether a prop blocks pathfinding navigation. |

## Reading Properties at Runtime

### From MapObject

```java
@Override
public Collection<IEntity> load(Environment environment, IMapObject mapObject) {
  // Read string property
  String customValue = mapObject.getStringValue("myProperty");

  // Read with default value
  String value = mapObject.getStringValue("optional", "default");

  // Read typed properties
  int intValue = mapObject.getIntValue("count", 0);
  float floatValue = mapObject.getFloatValue("speed", 1.0f);
  boolean boolValue = mapObject.getBoolValue("enabled", true);

  // ...
}
```

### From Entity

```java
// Get entity's custom property
IEntity entity = Game.world().environment().get("my-entity");
String customValue = entity.getStringValue("customProp");
```

### Using MapObjectProperty Constants

```java
import de.gurkenlabs.litiengine.environment.tilemap.MapObjectProperty;

// Use constants for built-in properties
String sprite = mapObject.getStringValue(MapObjectProperty.SPRITE);
int hp = mapObject.getIntValue(MapObjectProperty.COMBAT_HITPOINTS, 100);
```

## Property Types

Custom properties support various data types:

### String
```java
name: "playerName"
value: "Hero"
```

### Integer
```java
name: "maxHealth"
value: 100
```

### Float
```java
name: "moveSpeed"
value: 2.5
```

### Boolean
```java
name: "isInvulnerable"
value: true
```

### Color
```java
name: "tintColor"
value: #FF5500
```

### File Path
```java
name: "configFile"
value: "config/enemy.json"
```

## Common Use Cases

### Enemy Configuration

```properties
type=enemy
sprite=goblin
hp=50
damage=10
speed=1.5
patrol=true
```

### Interactive Objects

```properties
type=interactable
dialogue=npc_villager_01
questId=village_main
```

### Trigger Zones

```properties
type=trigger
onEnter=spawn_enemies
target=wave1
once=true
```

## Using Properties in Custom Loaders

```java
public class EnemyLoader extends MapObjectLoader {

  @Override
  public Collection<IEntity> load(Environment environment, IMapObject mapObject) {
    Enemy enemy = new Enemy();

    // Configure core engine properties from map object
    enemy.getHitPoints().set(mapObject.getIntValue("hp", 100));
    enemy.setVelocity(mapObject.getFloatValue("speed", 70.0f));
    enemy.setCollision(mapObject.getBoolValue("collision", true));

    return List.of(enemy);
  }
}
```

---

## Declarative Property Injection (`@TmxProperty`)

Instead of writing manual loader extraction code, annotate fields in your custom entity classes with `@TmxProperty`. LITIENGINE's `MapObjectLoader` inspects fields and automatically injects matching map object property values at load time:

```java
package com.example.game.entities;

import de.gurkenlabs.litiengine.entities.Creature;
import de.gurkenlabs.litiengine.environment.tilemap.TmxProperty;

public class GoblinArcher extends Creature {

  @TmxProperty(name = "patrolRoute")
  private String patrolRoute;

  @TmxProperty(name = "aggroRadius")
  private double aggroRadius = 150.0;

  @TmxProperty(name = "dropKey")
  private boolean dropKey = false;

  public GoblinArcher(String spritesheetName) {
    super(spritesheetName);
  }

  public String getPatrolRoute() { return this.patrolRoute; }
  public double getAggroRadius() { return this.aggroRadius; }
  public boolean doesDropKey() { return this.dropKey; }
}
```

When placing `GoblinArcher` on a map in utiLITI or Tiled, simply set custom properties named `patrolRoute`, `aggroRadius`, and `dropKey`—they are injected into the instance with zero loader boilerplate.

---

## See Also

- [Map Objects](map-objects.md) - Placing and loading map objects
- [Tile Maps Overview](README.md) - Introduction to TMX maps
- [Entity Framework](../entity-framework/README.md) - Entity system documentation
