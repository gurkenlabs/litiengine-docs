---
title: "Tile Maps"
icon: "lucide/map"
description: ">-"
keywords: ["LITIENGINE", "java", "game engine", "2D", "tile maps"]
---

# Tile Maps

Once you have gained a basic understanding of LITIENGINE's general game infrastructure, it is time to actually create a world for your game to take place in. LITIENGINE uses [.tmx tile maps](https://doc.mapeditor.org/en/stable/reference/tmx-map-format/), a universally acclaimed standard format for 2D level building.

## Create a tile map

At the beginning of your world building workflow, you create a tile map with [Tiled map editor](../libraries-and-tools.md#tiled-map-editor). While we won't go into details here \(because the [official Tiled docs](https://doc.mapeditor.org/en/stable/manual/introduction/) do\), here's the rough workflow:

* First, you need to paint your Tileset in the [pixel art editor of your choice (e.g. Aseprite, LibreSprite, or GIMP)](https://www.aseprite.org/).
* Then, import the Tileset image into Tiled editor to create a [.tsx Tileset](https://doc.mapeditor.org/en/stable/reference/tmx-map-format/#tileset).
* Create [layers](https://doc.mapeditor.org/en/stable/manual/layers/) containing Tiles, Objects, and Images.
* Save your map.

## Loading and Accessing Tile Maps in Code

Load and manipulate tile maps dynamically at runtime:

```java
package com.example.game;

import de.gurkenlabs.litiengine.Game;
import de.gurkenlabs.litiengine.environment.tilemap.IMap;
import de.gurkenlabs.litiengine.environment.tilemap.ITileLayer;
import de.gurkenlabs.litiengine.resources.Resources;

public class MapManager {
 public static void loadLevel(String mapName) {
 // 1. Load the map from .litidata or filesystem
 IMap map = Resources.maps().get(mapName);

 // 2. Load into GameWorld environment
 Game.world().loadEnvironment(map);

 // 3. Inspect map dimensions
 int widthInPixels = map.getSizeInPixels().width;
 int heightInPixels = map.getSizeInPixels().height;

 // 4. Access tile layers
 for (ITileLayer layer : map.getTileLayers()) {
 System.out.println("Layer: " + layer.getName() + " (visible=" + layer.isVisible() + ")");
 }
 }
}
```
