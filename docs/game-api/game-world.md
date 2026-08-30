---
title: "Game World"
icon: "lucide/globe"
description: "Game World documentation for LITIENGINE 2D Java game development."
keywords: ["LITIENGINE", "java", "2d", "game engine", "game api"]
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

 `BACKGROUND` -> `GROUND` -> `SURFACE` -> `NORMAL` -> (static shadows) -> `OVERLAY` -> (ambient light) -> `UI`

 Internally, the Environment.render method does the following for every `RenderType` (besides `RenderType.NONE`, which can, for example, be used to make objects invisible temporarily):

 1. Render all Map Layers of that type
 2. Render all registered `IRenderable` implementations of that type
 3. Render all added `IEntities` of that type
 4. Call-back on the `EnvironmentRenderListener.rendered` listeners for that type
 5. If `dbg_logDetailedRenderTimes = true`: track the time it took to execute the rendering

!!! tip "Entity Tag Caching"
    Use `environment.getEntitiesByTag("enemy")` to efficiently query collections of entities instead of filtering through `environment().getAll()` on every frame.

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
