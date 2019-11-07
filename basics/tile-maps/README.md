---
description: >-
  Learn about the internal structure of .tmx tile maps and how to load maps into
  your game project.
---

# Tile Maps

Once you have gained a basic understanding of LITIengine's general game infrastructure, it is time to actually create a world for your game to take place in. LITIengine uses [.tmx tile maps](https://doc.mapeditor.org/en/stable/reference/tmx-map-format/), a universally acclaimed standard format for 2D level building. 

## Create a tile map

At the beginning of your world building workflow, you create a tile map with [Tiled map editor](https://app.gitbook.com/@gurkenlabs/s/litiengine/~/drafts/-Lt4NljB3cbQX4NxqU4K/faq/faq#tiled-map-editor). While we won't go into details here \(because the [official Tiled docs](https://doc.mapeditor.org/en/stable/manual/introduction/) do\), here's the rough workflow:

* First, you need to paint your Tileset in the [pixel painting program of your choice](https://www.slant.co/topics/1547/~best-pixel-art-sprite-editors).
* Then, import the Tileset image into Tiled editor to create a [.tsx Tileset](https://doc.mapeditor.org/en/stable/reference/tmx-map-format/#tileset).
* Create [layers](https://doc.mapeditor.org/en/stable/manual/layers/) containing Tiles, Objects, and Images.
* Save your map.



