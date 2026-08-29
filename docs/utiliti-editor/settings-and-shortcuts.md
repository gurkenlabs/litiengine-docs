---
title: "Settings & Keyboard Shortcuts in utiLITI"
icon: "lucide/command"
description: "Complete guide to utiLITI application settings, themes, grid configuration, keymap customization, and keyboard shortcuts reference."
keywords: ["utiLITI", "settings", "preferences", "shortcuts", "keymap", "theme", "dark mode", "grid settings", "mcp settings", "hotkeys"]
---

# Settings & Keyboard Shortcuts

Access the application preferences by selecting **File -> Settings...** or pressing **`Ctrl + Alt + S`**.

---

## Settings Dialog Categories

```text
┌─────────────────────────────────────────────────────────────┐
│ SETTINGS                                          [Search]  │
├───────────────────┬─────────────────────────────────────────┤
│ [🎨 Appearance]   │ Theme: (●) Dark  (○) Light              │
│ [⚙️ General]       │ UI Scale: [========|====] 1.25x         │
│ [📐 Grid]          │ Font Family: [Roboto ▼]  Size: [12]     │
│ [⌨️ Keymap]        │ Editor FPS Cap: [60]                    │
│ [🤖 MCP Server]   │                                         │
└───────────────────┴─────────────────────────────────────────┘
```

### 1. Appearance (`🎨`)
- **Theme**: Toggle between **Dark Theme** (default) and **Light Theme**.
- **UI Scale**: Adjust scaling factor from `0.5x` to `2.0x` for high-DPI (4K/Retina) displays.
- **Editor Font Family**: Choose between `Roboto`, `OpenSans`, or installed system monospace fonts for the code and property editors.
- **Editor Font Size**: Text point size (`8`–`32`).
- **Editor FPS Cap**: Limit viewport framerate (`1`–`1000` FPS, default: `60`) to reduce GPU/CPU consumption.

### 2. General (`⚙️`)
- **Language & Region**: Switch editor localization (English, German, etc.).
- **Reopen Last Project on Startup**: Automatically restores the most recently active `.litidata` project on launch.
- **Gradle Launch Arguments**: Additional JVM or Gradle flags passed when running projects.
- **Log Level**: Filter console output (`ALL`, `INFO`, `WARNING`, `SEVERE`, `OFF`).

### 3. Grid (`📐`)
- **Snap to Grid**: Global default toggle for grid alignment.
- **Snap to Pixels**: Global default toggle for integer pixel coordinates.
- **Snap Division**: Set subdivision precision (`1/1`, `1/2`, `1/4` of tile size).
- **Grid Line Width**: Thickness of viewport grid lines (in pixels).
- **Grid Color**: Custom color picker and opacity slider.
- **Live Preview**: Interactive box showing the active grid style.

### 4. Keymap (`⌨️`)
- Full interactive shortcut table.
- Filter commands with the search bar.
- Double-click any command row or press **Record Shortcut** to bind custom key combinations.
- **Reset Defaults**: Restore original factory keybindings.

### 5. MCP Server (`🤖`)
- **Enable MCP Server**: Enable or disable the embedded Model Context Protocol server.
- **Server Port**: Port for JSON-RPC / SSE connections (default: `8088`).
- **Endpoint Info**: Displays `http://localhost:8088/mcp` and `http://localhost:8088/sse` with one-click clipboard copy.

---

## Keyboard Shortcuts Reference

### File & Project
| Action | Windows / Linux | macOS |
| :--- | :--- | :--- |
| **New Project** | `<kbd>Ctrl</kbd> + <kbd>N</kbd>` | `Cmd + N` |
| **Open Project** | `<kbd>Ctrl</kbd> + <kbd>O</kbd>` | `Cmd + O` |
| **Save Project** | `<kbd>Ctrl</kbd> + <kbd>S</kbd>` | `Cmd + S` |
| **Exit** | `Ctrl + Q` | `Cmd + Q` |

### Edit & Viewport
| Action | Windows / Linux | macOS |
| :--- | :--- | :--- |
| **Undo** | `<kbd>Ctrl</kbd> + <kbd>Z</kbd>` | `Cmd + Z` |
| **Redo** | `<kbd>Ctrl</kbd> + <kbd>Y</kbd>` | `Cmd + Y` |
| **Cut** | `Ctrl + X` | `Cmd + X` |
| **Copy** | `Ctrl + C` | `Cmd + C` |
| **Paste** | `Ctrl + V` | `Cmd + V` |
| **<kbd>Delete</kbd> Selection** | `<kbd>Delete</kbd>` | `Backspace` |
| **Select All** | `Ctrl + A` | `Cmd + A` |
| **Deselect** | `Ctrl + D` | `Cmd + D` |
| **Quick Search Palette** | `Ctrl + P` | `Cmd + P` |
| **Inspector History Back** | `Alt + Left` | `Opt + Left` |
| **Inspector History Forward** | `Alt + Right` | `Opt + Right` |

### View & Camera
| Action | Windows / Linux | macOS |
| :--- | :--- | :--- |
| **Toggle Grid** | `Ctrl + G` | `Cmd + G` |
| **Toggle Collision Boxes** | `Ctrl + H` | `Cmd + H` |
| **Toggle Custom Objects** | `Ctrl + K` | `Cmd + K` |
| **Toggle Map IDs** | `Ctrl + I` | `Cmd + I` |
| **Zoom In** | `Ctrl + +` | `Cmd + +` |
| **Zoom Out** | `Ctrl + -` | `Cmd + -` |
| **Center on Selection** | `Space` | `Space` |
| **Center on Map** | `<kbd>Ctrl</kbd> + <kbd>S</kbd>pace` | `Cmd + Space` |

### Add Entities
| Action | Windows / Linux | macOS |
| :--- | :--- | :--- |
| **Add Prop** | `Ctrl + 1` | `Cmd + 1` |
| **Add Creature** | `Ctrl + 2` | `Cmd + 2` |
| **Add CollisionBox** | `Ctrl + 3` | `Cmd + 3` |
| **Add Trigger** | `Ctrl + 4` | `Cmd + 4` |
| **Add Spawnpoint** | `Ctrl + 5` | `Cmd + 5` |
| **Add Map Area** | `Ctrl + 6` | `Cmd + 6` |
| **Add Light Source** | `Ctrl + 7` | `Cmd + 7` |
| **Add Static Shadow** | `Ctrl + 8` | `Cmd + 8` |
| **Add Emitter** | `Ctrl + 9` | `Cmd + 9` |
| **Add Sound Source** | `Ctrl + 0` | `Cmd + 0` |

### Scripting & Execution
| Action | Windows / Linux | macOS |
| :--- | :--- | :--- |
| **Run Project** | `Shift + F10` | `Shift + F10` |
| **Debug Project** | `Shift + F9` | `Shift + F9` |
| **Stop Project** | `Ctrl + F2` | `Cmd + F2` |
| **Save Script** | `<kbd>Ctrl</kbd> + <kbd>S</kbd>` | `Cmd + S` |
| **Format Code** | `Ctrl + Alt + F` | `Cmd + Opt + F` |
| **Compile Script** | `Ctrl + F9` | `Cmd + F9` |
| **Reload Script** | `Ctrl + R` | `Cmd + R` |
