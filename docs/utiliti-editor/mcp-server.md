---
title: MCP Server Integration & Tool Reference
icon: lucide/bot
description: Exhaustive reference documentation for the utiLITI Model Context Protocol
  (MCP) Server, covering Level B Raw Scene Building Primitives, Level A High-Level
  Semantic Tools, Godot-style scene composition, JSON Schema specifications, and live
  editor automation.
keywords: [LITIENGINE, utiLITI, MCP, Model Context Protocol, raw tools, scene building,
  godot-mcp, level design, entity placement, tile mapping, JSON Schema 2020-12]
tags: [mcp, model-context-protocol, ai-agents, automation, json-rpc]
---
# MCP Server Integration & Tool Reference

utiLITI includes an embedded **Model Context Protocol (MCP)** server running on port `8088` (default). The server provides **Dual API Surfaces** for scene composition, level design, and editor automation:

1. **Level B: Raw Scene-Building & Editor Primitives (~60+ Tools)**: Granular, atomic editor operations for direct scene node/entity manipulation, property editing, raw tile writing, and editor control (inspired by Godot MCP workflows like `godot-mcp-go`).
2. **Level A: High-Level Semantic Map Mutation API (32 Tools)**: Intent-oriented, batch-capable, revision-tracked, and 100% stateless map operations optimized for autonomous LLM agents.

> **Design Choice**: Use **Level B Raw Primitives** for direct, step-by-step entity placement, fine-grained property tweaks (`set-entity-property`), and Godot-style node tree composition. Use **Level A Semantic Tools** for bulk map generation, spatial region queries, multimodal visual rendering, and atomic transaction dry-runs.

---

## Overview & Architecture
- **Endpoint**: `http://localhost:8088/mcp`
- **SSE Stream**: `http://localhost:8088/sse`
- **Protocol Specification**: MCP JSON-RPC 2.0 with **JSON Schema 2020-12** (SEP-1613)
- **Live Editor Integration**: All mutations run directly inside the active utiLITI editor instance with full **Undo/Redo integration** and live AWT viewport refresh.

---

## Level B: Raw Scene Building & Editor Primitives

Level B tools provide raw, direct access to utiLITI editor operations and map objects.

### 1. Scene & Entity Placement (Raw Nodes)

| Tool Name | Description | Key Parameters |
| :--- | :--- | :--- |
| `add-prop` | Spawns a native `Prop` entity onto the active map layer. | `spritesheetName` *(string)*, `material` *(string)*, `addShadow` *(bool)*, `x` *(number)*, `y` *(number)*, `width` *(number)*, `height` *(number)*, `layer` *(string)*, `name` *(string)*. |
| `add-creature` | Spawns a native `Creature` NPC or enemy entity. | `spritesheetName` *(string)*, `scaleSprite` *(bool)*, `x` *(number)*, `y` *(number)*, `width` *(number)*, `height` *(number)*, `layer` *(string)*. |
| `add-trigger` | Spawns an interactive `Trigger` entity with message and target binding. | `message` *(string)*, `activation` *(COLLISION/INTERACT/TOGGLE)*, `targets` *(string or array)*, `cooldown` *(int)*, `oneTime` *(bool)*, `x` *(number)*, `y` *(number)*. |
| `add-light` | Spawns a dynamic `LightSource` entity. | `color` *(hex string)*, `intensity` *(int 0-255)*, `shape` *(CIRCLE/RECTANGLE/FAN)*, `active` *(bool)*, `x` *(number)*, `y` *(number)*, `width` *(number)*, `height` *(number)*. |
| `add-spawnpoint` | Spawns a player or creature `Spawnpoint`. | `spawnType` *(string)*, `direction` *(UP/DOWN/LEFT/RIGHT)*, `x` *(number)*, `y` *(number)*. |
| `add-collisionbox` | Spawns a static `CollisionBox` physics obstacle. | `x` *(number)*, `y` *(number)*, `width` *(number)*, `height` *(number)*. |
| `add-area` | Spawns a rectangular `MapArea` region for zone triggers and script boundaries. | `name` *(string)*, `x` *(number)*, `y` *(number)*, `width` *(number)*, `height` *(number)*. |
| `add-sound-source` | Spawns a positional 2D `SoundSource` emitter. | `soundName` *(string)*, `volume` *(float 0-1)*, `loop` *(bool)*, `range` *(float)*, `x` *(number)*, `y` *(number)*. |
| `add-emitter` | Spawns a particle `Emitter` entity. | `emitterType` *(string)*, `x` *(number)*, `y` *(number)*. |
| `add-entity` | Generic map object creator for custom TMX entity types. | `type` *(string, required)*, `name` *(string)*, `x` *(number)*, `y` *(number)*, `width` *(number)*, `height` *(number)*, `layer` *(string)*. |
| `batch-add-entities` | Bulk places an array of raw entity definitions onto the active map in a single call. | `entities` *(array of entity objects, required)*. |

---

### 2. Entity Inspection & Property Editing

| Tool Name | Description | Key Parameters |
| :--- | :--- | :--- |
| `set-entity-property` | Sets any custom TMX or built-in property on an entity by ID or name. | `id` *(integer)* or `name` *(string)*, `property` *(string, required)*, `value` *(string/number/bool, required)*. |
| `configure-prop` | Configures prop-specific attributes. | `id` *(integer)* or `name` *(string)*, `spritesheetName` *(string)*, `material` *(valid: WOOD, STONE, STEEL, PLASTIC, CERAMIC, FLESH, FOLIAGE, UNDEFINED)*, `addShadow` *(bool)*. |
| `configure-creature` | Configures creature-specific attributes. | `id` *(integer)* or `name` *(string)*, `spritesheetName` *(string)*, `scaleSprite` *(bool)*. |
| `configure-trigger` | Configures trigger-specific attributes. | `id` *(integer)* or `name` *(string)*, `message` *(string)*, `activation` *(string)*, `targets` *(string)*, `cooldown` *(int)*, `oneTime` *(bool)*. |
| `configure-light` | Configures light source attributes. | `id` *(integer)* or `name` *(string)*, `color` *(hex string)*, `intensity` *(int)*, `shape` *(string)*, `active` *(bool)*. |
| `configure-collision` | Configures collision box physics attributes. | `id` *(integer)* or `name` *(string)*, `collision` *(bool)*, `collisionType` *(STATIC/DYNAMIC)*, `collisionboxWidth` *(float)*, `collisionboxHeight` *(float)*. |
| `move-entity` | Moves entity to absolute coordinates or by relative delta offsets. | `id` *(integer)* or `name` *(string)*, `x` *(number)*, `y` *(number)*, `dx` *(number)*, `dy` *(number)*. |
| `resize-entity` | Resizes entity width and height dimensions. | `id` *(integer)* or `name` *(string)*, `width` *(number, required)*, `height` *(number, required)*. |
| `remove-entity` | Deletes an entity from the active map by ID or name. | `id` *(integer)* or `name` *(string)*. |
| `get-entity-info` | Returns complete transform, type, and custom property key-value map for an entity. | `id` *(integer)* or `name` *(string)*. |

---

### 3. Map & Layer Control

| Tool Name | Description | Key Parameters |
| :--- | :--- | :--- |
| `create-map` | Creates a new map with dimensions, tile size, tilesets, initial layers, and overwrite option. Tilesets must be attached here in GID order before the map can be painted. | `name` *(string)*, `width` *(int)*, `height` *(int)*, `tileWidth` *(int)*, `tileHeight` *(int)*, `tilesets` *(array)*, `initialLayers` *(array)*, `overwrite` *(bool)*. |
| `select-map` | Switches the active editor view and environment to the target map. | `name` *(string, required)*. |
| `delete-map` | Removes a map from the project file. | `name` *(string, required)*. |
| `save-project` | Saves all map and asset changes to the `.litidata` project file. | *None* |
| `load-project` | Opens a project `.litidata` file into the editor. | `path` *(string, required)*. |
| `get-layers` | Lists all tile and object layers on the active map. | *None* |
| `add-layer` | Adds a new tile or object layer to the map. | `name` *(string, required)*, `type` *(tile/object)*. |
| `remove-layer` | Deletes a layer by name. | `name` *(string, required)*. |
| `set-tile` | Sets single tile GID cell coordinate on a tile layer. | `layer` *(string)*, `x` *(int)*, `y` *(int)*, `gid` *(int)*. |
| `fill-tiles` | Fills a rectangular tile grid region with a tile GID. | `layer` *(string)*, `x` *(int)*, `y` *(int)*, `width` *(int)*, `height` *(int)*, `gid` *(int)*. |
| `list-terrains` | Lists Wang terrain sets, terrain names, local tile assignments, and painting guidance for a project tileset. | `tileset` *(string, required)*. |
| `paint-terrain` | Paints a named Wang terrain, resolving neighboring transitions automatically. The referenced tileset must already be attached to the active map. | `tileset`, `set`, `terrain`, `layer` *(strings, required)*, plus `cells`, `regions`, or `x`, `y`, `width`, `height`. |

> **Tileset attachment rule:** `create-map` is currently the API operation that attaches project tilesets to a map. Include existing project tileset names in its `tilesets` array (for example, `["tiles-hospital"]`) and create at least one tile layer before calling `paint-terrain`. An existing map with `tilesets: []` cannot be terrain-painted until tileset attachment is added through the editor or a future map-attachment API.

---

### 4. Scripting & Code Automation

| Tool Name | Description | Key Parameters |
| :--- | :--- | :--- |
| `list-scripts` | Lists all registered scripts in the active project with host types, targets, property metadata, and diagnostic summaries. | `host` *(GAME/ENVIRONMENT/ENTITY)*, `query` *(string)*. |
| `get-script` | Fetches script metadata and complete source code text. | `id` *(string, required)*. |
| `create-script` | Generates a new script file with 3-tier template code (`GameScript`, `EnvironmentScript`, `CreatureScript`), registers it with the project, and opens it in Monaco. | `name` *(string, required)*, `host` *(GAME/ENVIRONMENT/ENTITY)*, `targetType` *(string)*, `content` *(string)*, `package` *(string)*. |
| `update-script` | Updates source code on disk, triggers compiler diagnostics, and hot-reloads open editor tabs. | `id` *(string, required)*, `content` *(string, required)*. |
| `delete-script` | Removes a script definition and optionally deletes its source file from disk with Undo support. | `id` *(string, required)*, `deleteFile` *(bool, default true)*. |
| `get-script-diagnostics` | Retrieves compiler errors and warnings across all project scripts or filtered by ID. | `id` *(string)*. |
| `bind-script` | Attaches a script to an entity (`mapObjectId`), map environment (`mapName`), or game orchestrator (`game`) with parameter values. | `script` *(string, required)*, `targetType` *(entity/map/game)*, `targetId` *(string)*, `enabled` *(bool)*, `order` *(int)*, `parameters` *(object)*. |
| `unbind-script` | Removes a script binding from an entity, map environment, or game orchestrator. | `script` *(string, required)*, `targetType` *(entity/map/game)*, `targetId` *(string)*. |
| `get-script-bindings` | Lists all attached script bindings for an entity, map, or game. | `targetType` *(entity/map/game)*, `targetId` *(string)*. |

---

## Level A: High-Level Semantic Level-Design API

Level A tools provide stateless, batch-capable map operations with optimistic revision control.

### 1. Context & Inspection

| Tool Name | Description | Key Parameters |
| :--- | :--- | :--- |
| `get_project_context` | Returns complete project state: map list, tile sizes, tilesets, blueprints, valid `materials` list, and categorized `spritesheets` catalog (`props`, `creatures`). | *None* |
| `get_map` | Retrieves detailed map structure, dimensions, layer list, and revision lock. | `mapId` *(string, required)*. |
| `query_region` | Spatial bounding-box query returning entities, tile GIDs, and collision bounds in region `(x, y, w, h)`. | `mapId` *(string, required)*, `x`, `y`, `width`, `height`. |
| `search_entities` | Semantic entity search by query string, type, layer, or tag. | `mapId` *(string, required)*, `query` *(string)*. |
| `render_tileset` | Renders a project tileset atlas with grid lines and enlarged local tile IDs. Returns JSON metadata/base64 plus native MCP image content. | `tileset` *(string, required)*, `scale` *(int, default 4)*. |
| `find_tile_usage` | Finds a tileset's use across maps and reports directional neighbor frequencies for tile-family inference. | `tileset` *(string, required)*, `mapId`, `tileId`. |
| `render_tile_context` | Renders a local tile neighborhood as a selected layer, composited layers, or a layer-stack contact sheet. Returns native MCP image content. | `mapId`, `layer`, `x`, `y`, `radius`, `mode`, `scale`. |
| `preview_tile_edits` | Renders transient candidate tile edits without persisting them, reporting affected bounds, collision-bearing tiles, and warnings. Returns native MCP image content. | `mapId`, `layer`, `edits`, `padding`, `scale`. |

---

### 2. Batch Entity & Tile Mutations

| Tool Name | Description | Key Parameters |
| :--- | :--- | :--- |
| `create_entities` | Batch creates entities with explicit properties and prop collision auto-setup. | `mapId` *(string)*, `entities` *(array)*, `expectedRevision` *(int)*. |
| `update_entities` | Batch updates entity transforms and properties. | `mapId` *(string)*, `updates` *(array)*, `expectedRevision` *(int)*. |
| `edit_tiles` | Sparse tile GID placement on a tile layer. | `mapId` *(string)*, `layer` *(string)*, `tiles` *(array of {x, y, gid})*. |
| `fill_region` | Fills rectangular region with tile GID. | `mapId` *(string)*, `layer` *(string)*, `x`, `y`, `width`, `height`, `gid`. |
| `set_ambient_light` | Sets map-wide ambient light hex color and alpha opacity intensity. | `mapId` *(string)*, `color` *(hex string)*, `alpha` *(0-255)*. |
| `scatter_floor_details` | Scatters detail tiles (blood stains, rust, grime) across floor region. | `mapId` *(string)*, `layer` *(string)*, `x`, `y`, `width`, `height`, `gids` *(array)*, `density` *(float)*. |

---

### 3. Rendering & Diagnostics

| Tool Name | Description | Key Parameters |
| :--- | :--- | :--- |
| `render_map` | Renders complete map canvas and returns Base64 PNG image string. | `mapId` *(string, required)*. |
| `render_region` | Renders bounding-box region PNG for visual audit. | `mapId` *(string)*, `x`, `y`, `width`, `height`. |
| `analyze_map` | Runs automated validation checks (duplicate IDs, unlinked targets, missing assets). | `mapId` *(string, required)*. |
| `analyze_collision` | Analyzes collision layer geometry to detect isolated/inaccessible areas. | `mapId` *(string, required)*. |
| `analyze_playability` | Validates player-footprint-aware collision, spawn, and required-target reachability. `FAIL` contains hard gameplay failures. | `mapId`, `actorProfile` *(width, height, optional clearance)*, `requiredTargets`. |
| `get_navigation_graph` | Returns computed navigation connectivity and required-target reachability using the supplied actor footprint. | `mapId`, `actorProfile`, `requiredTargets`. |
| `render_playability` | Renders collision in magenta, reachable cells in green, and unreachable cells in red. Returns native MCP image content. | `mapId`, `actorProfile`, `requiredTargets`. |

---

## Scene Composition Examples (Godot Parity)

### Example 1: Direct Raw Node Placement (Level B)

```json
// 1. Create Prop
{"tool": "add-prop", "arguments": {"name": "hospital_bed_1", "spritesheetName": "prop-bed3-intact", "material": "STEEL", "x": 128, "y": 64, "width": 32, "height": 32}}

// 2. Set Custom Property
{"tool": "set-entity-property", "arguments": {"name": "hospital_bed_1", "property": "searchable", "value": "true"}}

// 3. Add Light Source
{"tool": "add-light", "arguments": {"name": "room_light", "color": "#ffaa44", "intensity": 180, "shape": "CIRCLE", "x": 128, "y": 64, "width": 64, "height": 64}}

// 4. Save Project
{"tool": "save-project"}
```

### Example 2: High-Level Semantic Room Authoring (Level A)

```json
// 1. Set Atmospheric Ambient Light
{"tool": "set_ambient_light", "arguments": {"mapId": "triage_room", "color": "#3c0029", "alpha": 200}}

// 2. Batch Place Props & Creatures
{"tool": "create_entities", "arguments": {
    "mapId": "triage_room",
    "entities": [{"type": "PROP", "name": "bed1", "spritesheetName": "bed3", "material": "STEEL", "x": 64, "y": 64, "width": 32, "height": 32, "collision": true},
      {"type": "CREATURE", "name": "zombie1", "spritesheetName": "zombie-doctor", "x": 96, "y": 64, "width": 16, "height": 16}]
  }}

// 3. Scatter Blood Stains
{"tool": "scatter_floor_details", "arguments": {"mapId": "triage_room", "layer": "details", "x": 4, "y": 4, "width": 10, "height": 10, "gids": [140, 141, 142], "density": 0.25}}
```

### Example 3: Script Creation & Entity Binding

```json
// 1. Create a Creature Combat Script
{"tool": "create-script", "arguments": {
    "name": "SkeletonWarriorAI",
    "host": "ENTITY",
    "targetType": "Creature"
  }}

// 2. Attach Script to an Enemy on the Active Map
{"tool": "bind-script", "arguments": {
    "script": "SkeletonWarriorAI",
    "targetType": "entity",
    "targetId": "101",
    "parameters": {"aggroRadius": "120", "attackPower": "15"}
  }}
```

---

## MCP Resources & Prompts

### Resources
- `uti://project/info`: Project path, active map, and resource statistics.
- `uti://project/scripts`: Manifest of all script definitions in the project.
- `uti://project/scripts/diagnostics`: Live compiler diagnostics and syntax errors across scripts.
- `uti://project/scripts/game-bindings`: Configured game-level startup scripts.
- `uti://project/scripts/{name}`: Full source code and property metadata for any script.

### Prompts
- `create_litiengine_script`: Architectural guide for authoring scripts conforming to the 3-tier model (`GameScript`, `EnvironmentScript`, `CreatureScript`), fluent combat builders, and `@ScriptProperty` annotations.
- `debug_litiengine_script`: Diagnostic troubleshooting guide for analyzing and correcting script compiler and runtime errors.
- `analyze_litiengine_project`: Autonomous map analysis and level-design profiling.
- `plan_litiengine_map`: Staged Big -> Medium -> Small level authoring workflow.
- `review_litiengine_map`: 9-point level design audit.

---

## Script Workspace & Editor Status Badge

utiLITI provides a live, interactive `[MCP • 1]` status badge rendered directly inside both the main **Status Bar** and the **Script Workspace**:

- **Live Status Dot**: Green when the MCP server is listening and ready.
- **Pulsing Animation**: Automatically pulses during active tool executions.
- **Client Count**: Displays the number of connected external LLM agents/tools in real-time.
- **Interactive Server Popup**: Clicking the badge opens the connection details popup with port, endpoint URL, one-click clipboard copy, and the list of active connected clients.

