---
title: "Maps & Environment Management"
description: "Learn how to create, import, export, and configure 2D maps in utiLITI, including ambient lighting, shadows, and ID management."
keywords: ["utiLITI", "map management", "import map", "export map", "TMX", "ambient light", "static shadow", "map properties", "reassign map ids"]
---

# Maps & Environment Management

utiLITI provides robust map authoring and management features supporting standard TMX formats while adding LITIENGINE-specific environment properties like ambient lighting, shadow tinting, and ID synchronization.

---

## 1. Creating a New Map

1. Select **Map -> New...** from the menu or press **`Ctrl + Shift + N`**.
2. In the **New Map Dialog**:
   - **Name**: Unique internal map identifier.
   - **Width & Height**: Map size in tile units.
   - **Tile Width & Tile Height**: Grid cell pixel dimensions (e.g. `16x16`, `32x32`).
3. Click **Create** to initialize the map and add it to your project bundle.

---

## 2. Importing & Exporting Maps

### Importing Maps
- **Map -> Import...**: Browse and import one or more `.tmx` map files into your project.
- utiLITI imports all tile layers, object layers, and external tileset references directly into `.litidata`.

### Exporting Maps
- **Map -> Export...**: Export the active map back into a standalone `.tmx` file for use in external tools like Tiled.

---

## 3. Map Properties & Atmospheric Lighting

Select the map background or choose **Map Properties** in the inspector to configure environment-wide settings:

```text
┌─────────────────────────────────────────────────────────────┐
│ MAP PROPERTIES                                              │
│ Name: dungeon_level_1  | Title: "The Sunken Catacombs"       │
│ Description: "First underground level of the dungeon."      │
├─────────────────────────────────────────────────────────────┤
│ Ambient Light Color: [ #3C0029 (Alpha: 200) ]  [🎨 Picker]  │
│ Static Shadow Color: [ #000000 (Alpha: 140) ]  [🎨 Picker]  │
├─────────────────────────────────────────────────────────────┤
│ [Live Ambient Light & Shadow Preview]                       │
└─────────────────────────────────────────────────────────────┘
```

- **Map Name & Title**: Internal identifier and user-facing title.
- **Ambient Light Color**: Color picker and alpha opacity slider determining global environmental darkness. When ambient alpha is greater than 0, dark levels require `LightSource` entities for visibility.
- **Static Shadow Color**: Tint and darkness level for all static shadow casters on the map.
- **Ambient Preview Panel**: Live interactive swatch demonstrating the lighting composite in real-time.

---

## 4. Map Snapshots & Maintenance Tools

- **Save Map Snapshot (`Shift + PrintScreen`)**: Renders the entire full-resolution map canvas to a PNG image file—ideal for level overviews, mini-maps, or documentation.
- **Sync Maps**: When **Map -> Sync Maps** is checked, external modifications to `.tmx` files on disk are automatically detected and reloaded into utiLITI.
- **Reassign Map IDs**: Opens **Map -> Reassign Map IDs...** to re-index all entity IDs starting from a specified minimum integer, resolving ID collisions across merged levels.
- **Delete Map**: Removes the selected map from the project bundle.
