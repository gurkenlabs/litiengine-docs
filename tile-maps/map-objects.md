---
meta.description: "Learn about MapObjects in LITIENGINE tile maps - how to place, configure, and load entities from Tiled map objects."
meta.keywords: "LITIENGINE, map objects, Tiled, tmx, entity, spawnpoint, collision, trigger"
---

# Map Objects

MapObjects are objects placed on your tile map using the Tiled editor or utiLITI. They define where and how entities spawn in your game world. When a map is loaded, LITIENGINE's `MapObjectLoader` implementations translate these map objects into game entities.

## Map Object Types

LITIENGINE supports several built-in map object types:

| Type | Description | Entity Class |
|------|-------------|--------------|
| `CollisionBox` | Static collision geometry | `CollisionBox` |
| `Creature` | Movable combat entities | `Creature` |
| `Prop` | Static or destructible objects | `Prop` |
| `Spawnpoint` | Entity spawn locations | `Spawnpoint` |
| `Trigger` | Area-based event triggers | `Trigger` |
| `LightSource` | Dynamic lighting | `LightSource` |
| `Emitter` | Particle effects | `Emitter` |
| `MapArea` | Named areas for scripting | `MapArea` |

## Adding Map Objects in utiLITI

### Via Right-Click Menu

1. Select an object layer in the map
2. Right-click on the map view
3. Choose **Add -> [Object Type]**
4. Click and drag to define the bounding box

### Via Resources Panel

1. In the Resources tab, find your spritesheet
2. Click the **+** button to create a map object
3. The object is created with pre-configured dimensions

## Map Object Properties

Each map object has configurable properties accessible in the utiLITI properties panel:

### Common Properties

- **Name**: Unique identifier for the object
- **Type**: Entity type (CollisionBox, Prop, Creature, etc.)
- **X, Y**: Position in tile coordinates
- **Width, Height**: Bounding box dimensions
- **Layer**: Which object layer the object belongs to

### Entity Properties

For entity-type objects:

- **Sprite**: Spritesheet to use for rendering
- **Collision**: Collision box dimensions and settings
- **Tags**: Comma-separated tags for entity queries

## Loading Map Objects

Map objects are automatically loaded when loading an environment:

```java
Game.world().loadEnvironment("level1");
// All MapObjects are converted to entities by MapObjectLoaders
```

### Accessing Loaded Entities

```java
// Get entity by name
IEntity entity = Game.world().environment().get("my-entity-name");

// Get entities by type
Collection<Creature> creatures = Game.world().environment().getByType(Creature.class);

// Get entities by tag
Collection<IEntity> tagged = Game.world().environment().getByTag("enemy", "flying");
```

## Custom MapObjectLoaders

Create custom loaders for your own entity types:

```java
public class MyEntityLoader extends MapObjectLoader {
  
  public MyEntityLoader() {
    super("MY_ENTITY_TYPE");
  }
  
  @Override
  public Collection<IEntity> load(Environment environment, IMapObject mapObject) {
    Collection<IEntity> entities = new ArrayList<>();
    
    MyEntity entity = new MyEntity();
    entity.setLocation(mapObject.getLocation());
    entity.setWidth(mapObject.getWidth());
    entity.setHeight(mapObject.getHeight());
    
    entities.add(entity);
    return entities;
  }
}

// Register before Game.start()
Environment.registerMapObjectLoader(new MyEntityLoader());
```

## Spawnpoints

Spawnpoints define where entities appear in the level:

```java
// Get a spawnpoint by name
Spawnpoint spawn = Game.world().environment().getSpawnpoint("enter");

// Spawn an entity at the spawnpoint
spawn.spawn(Player.instance());

// Use spawnpoint in world loaded event
Game.world().onLoaded(env -> {
  Spawnpoint start = env.getSpawnpoint("start");
  if (start != null) {
    start.spawn(Player.instance());
  }
});
```

## See Also

- [Tile Maps Overview](/docs/tile-maps/README/) - Introduction to TMX maps
- [Custom Properties](/docs/tile-maps/custom-properties/) - Entity property configuration
- [Entity Framework](/docs/entity-framework/README/) - Entity system documentation
