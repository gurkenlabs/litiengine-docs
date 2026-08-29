---
title: "GameLauncher CLI & Standalone Runner"
description: "Run standalone LITIENGINE projects without boilerplate Java main classes using GameLauncher."
keywords: ["LITIENGINE", "GameLauncher", "standalone runner", "CLI", "litidata", "game distribution"]
---

# GameLauncher CLI & Standalone Runner

`GameLauncher` (`de.gurkenlabs.litiengine.launch.GameLauncher`) is LITIENGINE's standalone CLI launcher. It boots and runs `.litidata` resource bundles without requiring you to compile a custom `public static void main` class.

---

## Quick Start

Run any `.litidata` game directly:

```bash
java -cp litiengine.jar de.gurkenlabs.litiengine.launch.GameLauncher --project game.litidata
```

---

## CLI Options

| Option | Argument | Description |
| :--- | :--- | :--- |
| `--project` | `<path>` | Path to the `.litidata` resource bundle file (e.g. `--project mygame.litidata`). |
| `--startup-script` | `<id>` | ID or class of the primary `GameScript` to execute on boot. If omitted, the first bound `GameScript` is run automatically. |
| `--map` | `<name>` | Initial map to load. If omitted, the first map in the project bundle is loaded. |
| `--scale` | `<float>` | Default render scale factor (e.g. `--scale 2.0` for pixel art). |
| `--title` | `<string>` | Custom window title text. |
| `--gravity` | `<int>` | 2D physics gravity value (default: 0). |
| `--release` | None | Run in production release mode (disables debug overlays). |
| `--help`, `-h` | None | Print command line usage and available flags. |
| `--version`, `-v` | None | Display engine version information. |

---

## Auto-Detection & Fallback Rules

When executing `GameLauncher`:
1. **Startup Script**: If `--startup-script` is not specified, `GameLauncher` inspects the project's bound `GameScript`s and boots the first active one. If none are bound, it searches for any registered `GameScript` definition.
2. **Initial Map**: If `--map` is not specified, `GameLauncher` checks if the active `GameScript` loaded a map in its `onStarted()` hook. If no map was loaded, it loads the first map found in `.litidata`.
3. **Audio & Physics**: Audio and physics engines are automatically initialized before any scripts are attached.
