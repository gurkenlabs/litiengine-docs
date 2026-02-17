---
meta.description: "Learn how to use custom properties in LITIENGINE to configure map objects and entities with custom data."
meta.keywords: "LITIENGINE, custom properties, Tiled, tmx, map object, configuration, entity"
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

| Property | Type | Description |
|----------|------|-------------|
| `sprite` | String | Spritesheet name for the entity |
| `collision` | Boolean | Enable/disable collision |
| `collisionBoxWidth` | Int | Collision box width in pixels |
| `collisionBoxHeight` | Int | Collision box height in pixels |
| `align` | String | Horizontal alignment (LEFT, CENTER, RIGHT) |
| `valign` | String | Vertical alignment (TOP, MIDDLE, BOTTOM) |
| `velocity` | Float | Movement velocity |
| `acceleration` | Float | Movement acceleration |
| `deceleration` | Float | Movement deceleration |
| `hp` | Int | Hit points for combat entities |

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
```
name: "playerName"
value: "Hero"
```

### Integer
```
name: "maxHealth"
value: 100
```

### Float
```
name: "moveSpeed"
value: 2.5
```

### Boolean
```
name: "isInvulnerable"
value: true
```

### Color
```
name: "tintColor"
value: #FF5500
```

### File Path
```
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
    
    // Configure from properties
    enemy.setHealth(mapObject.getIntValue("hp", 100));
    enemy.setDamage(mapObject.getIntValue("damage", 10));
    enemy.setSpeed(mapObject.getFloatValue("speed", 1.0f));
    enemy.setPatrols(mapObject.getBoolValue("patrol", false));
    
    return List.of(enemy);
  }
}
```

## See Also

- [Map Objects](/docs/tile-maps/map-objects/) - Placing and loading map objects
- [Tile Maps Overview](/docs/tile-maps/README/) - Introduction to TMX maps
- [Entity Framework](/docs/entity-framework/README/) - Entity system documentation
