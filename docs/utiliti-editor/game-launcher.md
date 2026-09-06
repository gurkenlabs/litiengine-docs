---
title: GameLauncher CLI & Standalone Runner
icon: lucide/terminal
description: Run standalone LITIENGINE projects without boilerplate Java main classes
  using GameLauncher.
keywords: [LITIENGINE, GameLauncher, standalone runner, CLI, litidata, game distribution]
tags: [game-launcher, standalone-runner, playtesting, execution]
---
# GameLauncher CLI & Standalone Runner

`GameLauncher` (`de.gurkenlabs.litiengine.launch.GameLauncher`) is LITIENGINE's standalone CLI launcher. It boots and runs `.litidata` resource bundles without requiring you to compile a custom `public static void main` class.

---

## Quick Start

Run any `.litidata` game or project directory directly:

```bash
# Pass the project bundle or directory as an argument
java -cp litiengine.jar de.gurkenlabs.litiengine.launch.GameLauncher game.litidata

# Or use explicit CLI options
java -cp litiengine.jar de.gurkenlabs.litiengine.launch.GameLauncher -p ./mygame --map overworld --scale 2.0
```

---

## CLI Options

```text
Usage: java -jar litiengine.jar [OPTIONS] [PROJECT_DIR_OR_LITIDATA]
```

| Option | Argument | Description |
| :--- | :--- | :--- |
| `-p`, `--project` | `<path>` | Path to the game project root folder or `.litidata` bundle. |
| `-s`, `--startup-script` | `<name>` | Specify the initial `GameScript` definition to execute on boot. |
| `-m`, `--map` | `<name>` | Specify the initial map/environment to load. |
| `-t`, `--title` | `<title>` | Custom game window title. |
| `--scale` | `<float>` | Set base render scale factor (e.g. `--scale 2.0` for pixel art). |
| `--gravity` | `<int>` | Set global physics gravity in pixels/sec (default: `0`). |
| `--release` | `<int>` | Java language level for runtime script compilation (e.g. `--release 25`). |
| `-h`, `--help` | None | Display command-line usage and available options. |
| `-v`, `--version` | None | Display engine version information. |

---

## Auto-Detection & Fallback Rules

When executing `GameLauncher`:

1. **Startup Script**: If `--startup-script` is not specified, `GameLauncher` inspects the project's bound `GameScript`s and boots the first active one. If none are bound, it searches for any registered `GameScript` definition.
2. **Initial Map**: If `--map` is not specified, `GameLauncher` checks if the active `GameScript` loaded a map in its `onStarted()` hook. If no map was loaded, it loads the first map found in `.litidata`.
3. **Audio & Physics**: Audio and physics engines are automatically initialized before any scripts are attached.
