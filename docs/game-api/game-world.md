---
title: Game World
icon: lucide/globe
description: Game World documentation for LITIENGINE 2D Java game development.
keywords: [LITIENGINE, java, 2d, game engine, game api]
tags: [game-world, environment, levels, scene-management, spawning]
---
# Game World

## Introduction to Environments

Every game engine needs a container that holds all the visual and non-visual things that will, in the end, make up the game world. This container is called `Environment` in the LITIENGINE. Only one Environment is loaded at a time and the Game holds the currently active Environment. Every time you want to position something within the two-dimensional space of your game, you can do so by adding it to the Environment.

It’s important to point out, that the Environment is related to exactly one Map and that the LITIENGINE provides an interface to load MapObjects to the environment. The implementations that take care of this task are called MapObjectLoaders. They basically translate the information form the *.tmx map* format to objects that can be managed by the engine.

**Example usages:**

```java
// set the active environment on the game
Game.world().loadEnvironment(new Environment("level-1.tmx"));

// add an entity to the environment
Game.world().environment().add(new MyEntity("my-entity"));

// retrieve the entity from the enviroment by its name
IEntity entity = Game.world().environment().get("my-entity");
MyEntity myEntity = Game.world().environment().get(MyEntity.class, "my-entity");

// remove the entity by its name
Game.world().environment().remove("my-entity");

// add a entity listener to the current environment of the game
Game.world().environment().addEntityListener(new EnvironmentEntityListener(){
  @Override
  public void entityAdded(IEntity entity) {
    // do sth when entities are added
  }
});
```

### Layering

When the active Screen calls the `Environment.render(Graphics2D)` method, its internal rendering pipeline is executed which will render everything that was previously added/loaded to the environment. There are different `RenderType`s that define in which order the objects and tile layers will be rendered. Think of the `RenderType`s as layers that are painted on our canvas one after another.

The rendering order is as follows:

`BACKGROUND` &rarr; `GROUND` &rarr; `SURFACE` &rarr; `NORMAL` &rarr; *(static shadows)* &rarr; `OVERLAY` &rarr; *(ambient light)* &rarr; `UI`

Internally, the `Environment.render` method does the following for every `RenderType` (besides `RenderType.NONE`, which can, for example, be used to make objects invisible temporarily):

1. Render all Map Layers of that type
2. Render all registered `IRenderable` implementations of that type
3. Render all added `IEntities` of that type
4. Call-back on the `EnvironmentRenderListener.rendered` listeners for that type
5. If `dbg_logDetailedRenderTimes = true`: track the time it took to execute the rendering

!!! tip "Entity Tag Caching"
    Use `environment.getEntitiesByTag("enemy")` to efficiently query collections of entities instead of filtering through `environment().getAll()` on every frame.

## Fluent Entity Queries (`EntityQuery`)

LITIENGINE provides a fluent spatial query API via `Environment.query(Class)` (or `EntityQuery.in(environment, Class)`) that eliminates manual stream filtering and distance math:

```java
import de.gurkenlabs.litiengine.Game;
import de.gurkenlabs.litiengine.entities.Creature;
import java.util.List;
import java.util.Optional;

// 1. Find the nearest living enemy creature within 200 pixels
Optional<Creature> nearestTarget = Game.world().environment()
    .query(Creature.class)
    .alive()
    .enemyOf(player)
    .within(player.getCenter(), 200)
    .nearestTo(player.getCenter())
    .first();

// 2. Query all undead creatures with a specific tag
List<Creature> skeletons = Game.world().environment()
    .query(Creature.class)
    .tagged("undead")
    .matching(c -> c.getName().startsWith("skeleton_"))
    .list();

// 3. Count enemies on team 2
long enemyCount = Game.world().environment()
    .query(Creature.class)
    .team(2)
    .alive()
    .count();
```

### Available `EntityQuery` Filters & Operations

| Method | Description |
|:---|:---|
| `.within(Point2D center, double radius)` | Keeps entities whose center is at most `radius` pixels from `center`. |
| `.nearestTo(Point2D point)` | Orders results by increasing Euclidean distance to `point`. |
| `.alive()` / `.dead()` | Filters combat entities by alive or dead state. |
| `.team(int teamId)` | Matches combat entities belonging to a specific team. |
| `.enemyOf(ICombatEntity entity)` | Keeps combat entities whose team differs from `entity`. |
| `.tagged(String tag)` | Keeps entities that possess the given tag. |
| `.named(String name)` | Matches entities by exact name. |
| `.matching(Predicate<T> filter)` | Applies an arbitrary custom predicate filter. |
| `.first()` | Returns an `Optional<T>` containing the first match. |
| `.list()` | Evaluates the query into an unmodifiable snapshot `List<T>`. |
| `.count()` | Counts matching entities without sorting. |

## Code-Only Environments (Procedural Maps without utiLITI)

You can build and run games completely in code without creating `.tmx` maps or using the utiLITI visual editor:

```java
package com.example.game;

import de.gurkenlabs.litiengine.Game;
import de.gurkenlabs.litiengine.entities.Creature;
import de.gurkenlabs.litiengine.entities.Prop;
import de.gurkenlabs.litiengine.environment.Environment;
import de.gurkenlabs.litiengine.environment.tilemap.xml.TmxMap;
import java.awt.Color;

public class ProceduralWorld {
  public static void generateDungeon() {
    // 1. Create a blank in-memory map (e.g. 50x50 tiles, 16x16 pixels per tile)
    TmxMap proceduralMap = new TmxMap();
    proceduralMap.setWidth(50);
    proceduralMap.setHeight(50);
    proceduralMap.setTileWidth(16);
    proceduralMap.setTileHeight(16);

    // 2. Wrap into an Environment
    Environment env = new Environment(proceduralMap);

    // 3. Add entities programmatically
    Prop pillar = new Prop("rock");
    pillar.setLocation(100, 100);
    env.add(pillar);

    // 4. Set ambient lighting
    env.getAmbientLight().setColor(new Color(20, 25, 40, 200));

    // 5. Activate environment in GameWorld
    Game.world().loadEnvironment(env);
  }
}
```

---

## Coordinate Systems & Positioning

All positions within an `Environment` use a top-left `(0, 0)` origin where `+X` increases to the right and `+Y` increases downward. For a complete guide on converting between **World Coordinates**, **Screen Viewport Coordinates**, and **Tile Grid Coordinates**, as well as understanding entity anchors (`getLocation()` vs `getCenter()`), see the dedicated guide:

See **[Coordinate Systems & Spatial Spaces](coordinate-systems.md)**.
