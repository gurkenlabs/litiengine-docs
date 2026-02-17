---
meta.description: "Learn how to create custom MapObjectLoaders in LITIENGINE to load custom entity types from Tiled maps."
meta.keywords: "LITIENGINE, MapObjectLoader, custom entity, map, tmx, Java"
---

# Custom MapObjectLoaders

MapObjectLoaders convert MapObjects from your Tiled map into game entities. Create custom loaders when you define new entity types.

## How MapObjectLoaders Work

1. Map is loaded from .tmx file
2. Each MapObject has a `type` property
3. Registered loader matching the type is invoked
4. Loader creates entity/entities and adds to environment

## Creating a Custom Loader

```java
public class ChestLoader extends MapObjectLoader {
  
  public ChestLoader() {
    super("CHEST");  // MapObject type this loader handles
  }
  
  @Override
  public Collection<IEntity> load(Environment environment, IMapObject mapObject) {
    Collection<IEntity> entities = new ArrayList<>();
    
    // Validate map object
    if (mapObject.getType() == null || !mapObject.getType().equals("CHEST")) {
      return entities;
    }
    
    // Create entity from map object
    Chest chest = new Chest();
    chest.setLocation(mapObject.getLocation());
    chest.setWidth(mapObject.getWidth());
    chest.setHeight(mapObject.getHeight());
    chest.setMapId(mapObject.getId());
    chest.setName(mapObject.getName());
    
    // Read custom properties
    boolean locked = mapObject.getBoolValue("locked", false);
    String lootTable = mapObject.getStringValue("lootTable", "default");
    chest.setLocked(locked);
    chest.setLootTable(lootTable);
    
    entities.add(chest);
    return entities;
  }
}
```

## Registering Loaders

Register before loading maps:

```java
public static void main(String[] args) {
  Game.init(args);
  
  // Register custom loaders BEFORE loading environment
  Environment.registerMapObjectLoader(new ChestLoader());
  Environment.registerMapObjectLoader(new PortalLoader());
  
  Resources.load("game.litidata");
  Game.world().loadEnvironment("level1");
  
  Game.start();
}
```

## Reading Map Object Properties

```java
@Override
public Collection<IEntity> load(Environment environment, IMapObject mapObject) {
  // Basic properties
  String name = mapObject.getName();
  int id = mapObject.getId();
  Point2D location = mapObject.getLocation();
  double width = mapObject.getWidth();
  double height = mapObject.getHeight();
  
  // Custom properties (from Tiled Properties panel)
  String value = mapObject.getStringValue("myProperty");
  int count = mapObject.getIntValue("count", 0);
  float speed = mapObject.getFloatValue("speed", 1.0f);
  boolean enabled = mapObject.getBoolValue("enabled", true);
  
  // Using constants
  String sprite = mapObject.getStringValue(MapObjectProperty.SPRITE);
  
  // ...
}
```

## See Also

- [Map Objects](/docs/tile-maps/map-objects/) - MapObject overview
- [Custom Properties](/docs/tile-maps/custom-properties/) - Property configuration
- [Default Entity Types](/docs/entity-framework/default-entity-types/) - Built-in types
