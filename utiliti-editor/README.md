---
meta.description: "Comprehensive introduction to the utiLITI editor for LITIENGINE, covering workspaces, level design, entity inspection, scripting, and tooling."
meta.keywords: "LITIENGINE, utiLITI, editor, 2D game editor, level design, map editor, java game development"
meta.title: "utiLITI Overview & Getting Started"
---

# utiLITI

## What is utiLITI?

**utiLITI** is the official visual level design, asset management, and development editor for **LITIENGINE**. It provides an integrated environment tailored specifically to the engine's entity-component architecture, rendering pipeline, and physics model.

While you can build LITIENGINE games entirely via code or generic external tools, utiLITI streamlines game development by combining map editing, live asset packaging, script authoring, and project debugging into a single unified application.

![utiLITI Editor Overview](/images/utiliti-screenshot.png)
*The utiLITI visual editor in action with loaded maps, entity inspector, and asset manager.*

---

## Core Workspaces

utiLITI features a dual-workspace architecture accessible via the workspace rail on the left edge of the window:

```text
┌──────┬────────────────────────────────────────────────────────────────────────┐
│      │                           VIEWPORT TOOLBAR                             │
│      ├─────────────────────────────────────────┬──────────────────────────────┤
│  M   │                                         │       OBJECTS / LAYERS       │
│  A   │                                         │  Hierarchy & Layer Manager   │
│  P   │              MAP VIEWPORT               ├──────────────────────────────┤
│      │        Visual 2D Level Canvas           │       ENTITY INSPECTOR       │
│  ─── │                                         │  Properties, Combat, Physics │
│  S   ├─────────────────────────────────────────┴──────────────────────────────┤
│  C   │                      RESOURCES / CONSOLE / ASSETS                      │
│  R   │           Spritesheets, Tilesets, Blueprints, Logs                     │
└──────┴────────────────────────────────────────────────────────────────────────┘
```

1. **Map Workspace**:
   - Visual 2D map viewport with real-time LITIENGINE rendering and physics previews.
   - Dedicated tools for object placement, tile painting, multi-tile stamps, and seamless Wang terrain painting.
   - Scene graph entity hierarchy and multi-layer management (tile layers and object layers).
   - Comprehensive entity inspector for configuring props, creatures, lights, triggers, emitters, sounds, and custom project classes.
   - Integrated tile collision shape editor and sprite animation configurator.

2. **Scripts Workspace**:
   - Embedded Monaco code editor with full Java and Groovy syntax highlighting, IntelliSense autocomplete, and error diagnostics.
   - Hierarchical script explorer, class outline, and project usages panel.
   - Integrated JDI debugger with gutter breakpoints, step-by-step execution, and live runtime snapshot inspection.
   - One-click script creation templates and project startup configuration dialogs.

---

## Key Feature Matrix

| Feature Area | Capabilities |
| :--- | :--- |
| **Project & Assets** | Packages maps, tilesets, spritesheets, emitters, blueprints, sounds, and scripts into portable `.litidata` resource bundles. Supports compression and XML encoding. |
| **Level Design** | Full TMX map support, tile layers, object layers, flood fill, eraser, multi-tile stamp brushes, and Wang terrain auto-matching. |
| **Entity Framework** | Visual authoring of all LITIENGINE entities (`Prop`, `Creature`, `Trigger`, `LightSource`, `Emitter`, `SoundSource`, `Spawnpoint`, `CollisionBox`, `StaticShadow`, `MapArea`) plus custom project entity classes. |
| **Physics & Collisions** | Static and dynamic collision boxes, custom tile-level polygon/rectangle collision editor, and raycast reachability analysis. |
| **Lighting & Effects** | Real-time ambient lighting previews, point/fan/cone dynamic lights, directional static shadows, and comprehensive particle emitter designer. |
| **Scripting & Code** | Tabbed code editor, `@ScriptProperty` inspector reflection, automatic `@ScriptInfo` synchronization, hot code reloading, and JDI debugging. |
| **Project Execution** | One-click **Run Project** (`Shift+F10`) and **Debug Project** (`Shift+F9`) with live process lifecycle indicator and compiler diagnostics. |
| **Model Context Protocol** | Built-in **MCP Server** on port `8088` exposing Level A semantic tools and Level B raw primitives for external AI coding agents. |
| **Productivity** | Full Undo/Redo history stack, inspector navigation history (`Alt+Left`/`Alt+Right`), quick search command palette (`Ctrl+P`), customizable keymap, dark/light themes, and automatic background saving. |

---

## Installation & Launch

utiLITI is distributed as part of the official [LITIENGINE SDK](https://litiengine.com/download/) and can also be built directly from the source repository.

### Prerequisites

- **Java Development Kit (JDK)**: Version 17 or higher (JDK 21 recommended).
- **Display**: Minimum resolution of 1280x800.

### Running utiLITI

* **Windows**: Run `utiliti.exe` or execute `java -jar utiliti.jar`.
* **macOS / Linux**: Run the launcher script or execute:
  ```bash
  java -jar utiliti.jar
  ```

> **Note on macOS Permissions:** If macOS prevents execution, set the executable flag using:
> ```bash
> chmod +x /Applications/litiengine-sdk/utiliti/litiengine-utiliti.app/Contents/MacOS/*
> ```

### Command-Line Arguments

You can pass CLI arguments to launch utiLITI directly with specific project files or settings:

```bash
java -jar utiliti.jar [OPTIONS] [PROJECT_FILE]
```

| Argument | Description |
| :--- | :--- |
| `path/to/game.litidata` | Automatically loads the specified `.litidata` resource file on startup. |
| `--theme <dark\|light>` | Overrides the active UI theme. |
| `--scale <float>` | Overrides the UI scaling factor (e.g. `--scale 1.5` for HiDPI displays). |
| `--no-mcp` | Disables the embedded Model Context Protocol server. |

---

## Next Steps

- [Create and Manage Projects](/docs/utiliti-editor/create-projects/) — Learn about `.litidata` project files, saving, and auto-backups.
- [User Interface & Workspaces](/docs/utiliti-editor/ui-and-workspaces/) — Explore the layout, viewport controls, and panels.
- [Editing Tools & Viewport](/docs/utiliti-editor/tools-and-editing/) — Master the pointer, tile brush, bucket fill, and Wang terrain tools.
- [Entity & Object Inspector](/docs/utiliti-editor/entity-inspector/) — Configure properties, combat stats, and behaviors.
- [Tilesets & Wang Terrains](/docs/utiliti-editor/tileset-editor/) — Set up animated tiles, collision shapes, and terrain sets.
- [Run, Debug & Hot Reload](/docs/utiliti-editor/project-runner/) — Launch and debug your game directly from the editor.
