---
title: Editing Tools & Viewport Operations in utiLITI
icon: lucide/pen-tool
description: 'Guide to utiLITI editing tools: Pointer, Tile Brush, Bucket Fill, Eraser,
  Stamp Brush, Wang Terrain Brush, Snapping, and Visual Overlays.'
keywords: [utiLITI, tools, tile brush, bucket fill, eraser, stamp brush, terrain brush,
  wang tiles, snapping, grid, collision overlay]
tags: [editing-tools, selection, brush, stamp, shapes]
---
# Editing Tools & Viewport Operations

utiLITI provides a suite of viewport editing tools designed for precise object placement, freeform tile painting, pattern stamping, and automated Wang terrain matching.

---

## The Tool Palette

The primary tools are available on the viewport toolbar and can be activated using hotkeys:

| Tool | Icon | Hotkey | Target Layer | Description |
| :--- | :---: | :---: | :--- | :--- |
| **Pointer Tool** | | `V` / `1` | Object / All | Selects, moves, resizes, and rotates map entities. |
| **Tile Brush Tool** |  | `B` / `2` | Tile Layer | Paints individual tiles selected from the Tileset panel. |
| **Bucket Fill Tool** | | `G` / `3` | Tile Layer | Flood-fills contiguous tile areas with the active tile GID. |
| **Eraser Tool** | | `E` / `4` | Tile Layer | Clears tile cells on the active tile layer. |
| **Stamp Brush Tool** | | `S` / `5` | Tile Layer | Stamps multi-tile patterns and rectangular tile arrangements. |
| **Terrain Brush Tool** | | `T` / `6` | Tile Layer | Paints Wang terrain sets, automatically resolving neighboring edge and corner transitions. |

---

## Detailed Tool Behaviors

### 1. Pointer Tool (`V`)
The **Pointer Tool** is the primary tool for interacting with map objects and entities:

- **Single Selection**: Left-click any entity in the viewport to focus it and load its properties into the inspector.
- **Box Selection**: Click and drag on empty canvas space to draw a selection rectangle and select multiple entities.
- **Additive Selection**: Hold `Shift` while clicking or box-selecting to add objects to the current selection.
- **Moving Entities**: Click and drag selected entities to move them across the map.
- **Resizing Entities**: Hover over the boundary handles (corners and edges) of a selected entity and drag to adjust width and height.
- **Transform Modes**:
 - `Move`: Standard translation.
 - `Rotate`: Adjust rotation angle.
 - `Scale`: Proportional resizing.

---

### 2. Tile Brush Tool (`B`)
The **Tile Brush** paints individual tiles onto the active tile layer:

1. Select the target **Tile Layer** in the **Layers** panel.
2. Select a tile from the **Tileset** panel at the bottom of the editor.
3. Left-click or click-and-drag across the viewport canvas to place tiles.
4. Right-click or use `Alt + Left Click` to pick a tile directly from the canvas (eyedropper mode).

---

### 3. Bucket Fill Tool (`G`)
The **Bucket Fill Tool** performs flood-filling on tile layers:

- Click any tile cell on the active layer to replace all connected identical tiles with the currently selected tile GID.
- Useful for rapidly filling large room floors, backgrounds, or water bodies.

---

### 4. Eraser Tool (`E`)
The **Eraser Tool** clears tile data from the active tile layer:

- Left-click or drag across tile cells to clear them (sets tile GID to `0`).
- Only affects the currently selected tile layer, leaving other tile and object layers intact.

---

### 5. Stamp Brush Tool (`S`)
The **Stamp Brush** places multi-tile selections and complex tile patterns in a single click:

1. In the **Tileset Editor** or tile grid, select a rectangular group of tiles (e.g. a 3x3 tree or building).
2. Switch to the **Stamp Brush Tool**.
3. Hover over the canvas to see a translucent preview of the entire stamp pattern.
4. Click to place the full multi-tile stamp onto the active tile layer.

---

### 6. Terrain Brush Tool (`T`) & Wang Tile Auto-Matching

The **Terrain Brush** uses Wang tilesets to automate natural terrain transitions (such as grass-to-dirt, water-to-sand, or wall corners) without requiring you to manually pick corner and edge tiles:

1. Configure a **Wang Set** in the [Tileset & Terrain Editor](/utiliti-editor/tileset-editor/).
2. Select the **Terrain Brush Tool** from the toolbar.
3. In the terrain dropdown attached to the tool, pick your desired terrain type (e.g. *Grass*, *Dirt*, *Water*).
4. Paint freely on the canvas: utiLITI automatically inspects all 8 neighboring cells and selects the correct edge, corner, inner-corner, or center tile variation seamlessly.

---

## Snapping & Alignment

utiLITI provides several snapping modes to maintain clean grid alignment during level editing:

```text
┌─────────────────────────────────────────────────────────────┐
│ [Snap to Grid] [Snap to Pixels] [Snap Division: 1/2] │
└─────────────────────────────────────────────────────────────┘
```

| Snapping Mode | Description |
| :--- | :--- |
| **Snap to Grid** | Aligns entity placement, moves, and resizing to the map's tile grid boundaries. |
| **Snap to Pixels** | Aligns entity coordinates and sizes to whole pixel integers, preventing sub-pixel rendering blur. |
| **Snap Divisions** | Allows snapping to fractions of a tile grid cell (`1/1` full tile, `1/2` half tile, `1/4` quarter tile) for flexible yet structured alignment. |
| **Clamp to Map** | Constrains entity dragging and camera panning within the physical boundaries of the map. |

> **Configuration:** You can customize snap divisions and grid properties in **File -> Settings -> Grid**.

---

## Viewport Visual Overlays

You can toggle visual debug overlays from the **View** menu or the viewport toolbar:

- **Show Grid (`Ctrl + G`)**: Renders grid lines across the entire map canvas. Custom line width and colors can be configured in settings.
- **Show Collision Boxes (`Ctrl + H`)**: Overlays magenta boundary boxes for all static and dynamic physics collision geometry.
- **Show Custom Map Objects (`Ctrl + K`)**: Visualizes custom non-rendered map markers and logic boundaries.
- **Show Map IDs (`Ctrl + I`)**: Displays integer entity IDs next to each placed map object.
- **Show Names**: Displays entity names directly above objects on the canvas.
- **Show Static Shadows (`Ctrl + 8`)**: Previews 2D shadow caster projections in real-time.
