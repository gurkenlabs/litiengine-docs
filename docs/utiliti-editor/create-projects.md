---
title: "Project Management in utiLITI"
icon: "lucide/folder-plus"
description: "Learn how to create, configure, save, and manage LITIENGINE game projects (.litidata) in utiLITI, including auto-save and backups."
keywords: ["LITIENGINE", "utiLITI", "create project", "litidata", "game resource file", "auto save", "project management"]
---

# Project Management

## Game Resource Files (`.litidata`)

In LITIENGINE, all game assets, maps, blueprints, particle configurations, sounds, and script definitions are organized and bundled into a central **game resource file** (conventionally named with the `.litidata` extension).

A `.litidata` file is an XML-structured container that can either reference external assets or store base64-encoded compressed resources directly. This makes it effortless to package your entire game for distribution or version-control your assets cleanly.

### What is stored inside `.litidata`?

- **Maps**: All TMX map layouts, tile layer GID grids, and placed map objects.
- **Tilesets**: External and embedded TSX tilesets, Wang terrain definitions, tile animations, and custom tile collision shapes.
- **Spritesheets**: Image frame metrics, slice dimensions, and keyframe animation timing data.
- **Emitters**: Particle emitter configurations, physics properties, and color gradients.
- **Blueprints**: Reusable entity templates and pre-configured object blueprints.
- **Sounds**: Registered SFX and audio resources.
- **Script Definitions**: Declarations for game, environment, and entity scripts with their target bindings and `@ScriptProperty` parameter values.

---

## Creating a New Project

1. Launch the utiLITI editor.
2. Select **File -> New...** from the menu or press **`Ctrl + N`**.
3. In the file chooser dialog, navigate to your desired directory and specify your project name (for example, `game.litidata`).
4. Click **Save**.

An empty project will be initialized with a blank canvas, default layer setup, and ready-to-use asset containers.

---

## Opening, Saving & Reverting

### Opening Projects
- **File -> Open...** (`Ctrl + O`): Browse and open an existing `.litidata` project.
- **File -> Recent Projects**: Quickly reopen recently edited projects.
- **Drag-and-Drop**: Drag a `.litidata` file from your operating system file manager directly into the utiLITI window.

### Saving Changes
- **Save Project** (`Ctrl + S`): Writes all current map modifications, layer updates, and asset changes to the active `.litidata` file.
- **Save As...**: Saves the entire project bundle to a new `.litidata` destination path.
- **Compress Resource File**: In **Resources -> Compress Resource File**, toggle compression to drastically reduce `.litidata` bundle size when exporting.

### Reverting
- **File -> Revert**: Discards all unsaved in-memory changes and reloads the project from the disk version.

---

## Auto-Save & Crash Recovery

utiLITI includes a background **Auto-Save Manager** (`AutoSaveManager`) designed to protect your work against accidental closures or system crashes.

### How Auto-Save Works

1. **Periodic Background Saves**: Every 5 minutes (or as configured in preferences), if changes have been made since the last manual save, utiLITI silently writes a snapshot of your project.
2. **Backup Storage**: Auto-save snapshots are stored alongside your project file with a `.backup` or `.autosave` suffix.
3. **Recovery on Startup**: If utiLITI detects an unexpected shutdown or finds a backup file that is newer than the saved project, it prompts you on startup to restore the auto-saved session.

!!! tip
    You can configure the auto-save interval or disable automatic saving in **File -> Settings -> General**.

---

## Project Settings & Startup Restoration

In **File -> Settings -> General**:

- **Reopen Last Project on Startup**: When enabled, utiLITI automatically loads the most recently active `.litidata` project upon launch.
- **Gradle Launch Arguments**: Define JVM flags or task options used when launching or debugging the project from the editor.
- **Log Level**: Filter the console output verbosity (`ALL`, `INFO`, `WARNING`, `SEVERE`, `OFF`).

---

## Loading Projects in Code

Once you have saved your `.litidata` file in utiLITI, loading it into your LITIENGINE game requires only one line of code:

```java
import de.gurkenlabs.litiengine.Game;
import de.gurkenlabs.litiengine.resources.Resources;

public class MyGame {
  public static void main(String[] args) {
    Game.init(args);
    
    // Load the resource bundle created in utiLITI
    Resources.load("game.litidata");
    
    // Load the initial map and start the game
    Game.world().loadEnvironment("level1");
    Game.start();
  }
}
```
