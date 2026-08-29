---
title: "Tilesets & Wang Terrains in utiLITI"
description: "Comprehensive guide to the utiLITI Tileset Editor: tile properties, collision vector editing, animated tiles, and Wang terrain sets for auto-tiling."
keywords: ["utiLITI", "Tileset Editor", "tile collisions", "animated tiles", "Wang tiles", "terrain sets", "auto-tiling", "tile properties"]
---

# Tilesets & Wang Terrains

The **Tileset Editor** (accessible via the `Tilesets` tab or double-clicking any tileset asset in the asset tree) provides full control over tile graphics, custom tile collision shapes, multi-frame tile animations, and Wang terrain definitions.

---

## Editor Overview

```text
┌─────────────────────────────────────────────────────────────┐
│ Tileset: [dungeon_tileset ▼]   Tile Size: 16x16             │
│ Offsets: X: 0 | Y: 0          Custom Properties: [...]      │
├───────────────────────────────┬─────────────────────────────┤
│                               │ [Tile Properties]           │
│                               │ Type: solid_wall            │
│                               │ Probability: 1.0            │
│                               ├─────────────────────────────┤
│         TILE GRID             │ [Tile Collision Editor]     │
│    Interactive Atlas          │ ┌────────┐ Mode: Rectangle  │
│    Multi-tile Selection       │ │ ■■■■■■ │ Shapes: [Delete] │
│                               │ └────────┘                  │
│                               ├─────────────────────────────┤
│                               │ [Tile Animation]            │
│                               │ Frame 1 (100ms) -> Frame 2  │
│                               ├─────────────────────────────┤
│                               │ [Wang Terrain Sets]         │
│                               │ Set: Walls | Type: Corner   │
│                               │ 8-Slot Edge/Corner Mask     │
└───────────────────────────────┴─────────────────────────────┘
```

---

## 1. Tileset Properties & Management

- **Importing Tilesets**: Go to **Resources -> Import -> Import Tilesets...** or drag a `.tsx` or image file into the editor.
- **Tile Offsets**: Adjust `Tile Offset X` and `Tile Offset Y` spinners to offset tile rendering alignment relative to the map grid.
- **Custom Tileset Properties**: Define custom key-value pairs applicable to all tiles within the tileset.

---

## 2. Tile Properties & Probabilities

Select any tile in the tile grid to configure its individual metadata:
- **Type**: Custom string categorization (e.g. `water`, `wall`, `lava`) accessible via LITIENGINE's tile querying API.
- **Probability Slider**: Numeric weighting value (`0.0` to `1.0`) used by procedural generation algorithms and random tile scatters.
- **Tile Custom Properties**: Attach custom metadata specific to that single tile ID.

---

## 3. Integrated Tile Collision Editor (`TileCollisionEditorPanel`)

Instead of requiring separate external collision tools, utiLITI includes an integrated vector collision editor directly within the tileset view:

```text
┌──────────────────────────────────────────────┐
│ Tools: [↖️ Select] [🔲 Rectangle] [🗑️ Delete] │
├──────────────────────────────────────────────┤
│               ┌──────────────┐               │
│               │              │               │
│               │   ┌──────┐   │ ◄ Resize Grip │
│               │   │ RED  │   │               │
│               │   │ AREA │   │               │
│               │   └──────┘   │               │
│               └──────────────┘               │
└──────────────────────────────────────────────┘
```

### Collision Authoring Workflow:
1. Select a tile in the grid.
2. Under the **Collision Editor** section, click **Rectangle Mode** (`🔲`).
3. Click and drag across the tile image preview to define collision boundaries (e.g. half-height walls or isometric tops).
4. Switch to **Select Mode** (`↖️`) to move shapes or drag corner/edge handles to resize.
5. Click **Delete** (`🗑️`) or press `Delete` to remove collision geometry.

When painted on any map layer, tiles with defined collision shapes automatically generate static physics obstacles in LITIENGINE's physics engine.

---

## 4. Animated Tiles

Create animated water, spinning coins, flickering torches, and lava directly within the tileset:

1. Select the base tile you want to animate.
2. In the **Tile Animation** table, click **Add Frame** (`+`).
3. Select the next frame tile from the grid and enter its duration in milliseconds (e.g. `150ms`).
4. Add additional frames to complete the animation loop.
5. The live animation preview immediately plays back the frame sequence in real-time.

LITIENGINE automatically updates and renders animated tiles during runtime loops without manual code.

---

## 5. Wang Terrains & Auto-Tiling

Wang tiles allow the **Terrain Brush Tool** to automatically connect and blend terrains seamlessly.

### Wang Terrain Types:
- **Corner**: Matches tile transitions based on 4 corner colors.
- **Edge**: Matches transitions based on 4 edge colors (North, East, South, West).
- **Mixed**: Matches transitions based on all 8 directions (4 edges + 4 corners).

### Setting Up a Wang Terrain Set:
1. Under the **Wang Terrains** panel, create a new **Terrain Set** (e.g. `Grass_to_Stone`).
2. Select the terrain type (`Corner`, `Edge`, or `Mixed`).
3. Add **Wang Colors** (e.g. *Grass* as Green, *Stone* as Gray).
4. Select a tile in the tileset and use the **8-Slot Terrain Mask** to assign which edges and corners belong to each terrain color.
5. Once configured, switch to the [Terrain Brush Tool](tools-and-editing.md) to paint seamless terrain borders directly on your map!
