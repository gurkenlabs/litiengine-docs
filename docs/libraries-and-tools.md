---
title: "Libraries and Tools"
icon: "lucide/wrench"
description: "Comprehensive overview of third-party libraries, developer tools, and asset pipelines used within the modern LITIENGINE ecosystem."
keywords: ["LITIENGINE libraries", "Input4j", "Java FFM", "Steamworks4j", "Tiled", "Aseprite", "utiLITI", "Monaco", "MCP server"]
tags: ["libraries", "tools", "dependencies", "ecosystem", "tiled", "aseprite", "input4j", "steamworks"]
---

# Libraries and Tools

LITIENGINE adheres to a lean, minimalist architecture. The engine relies on a carefully selected foundation of lightweight libraries and ecosystem tools to maximize developer productivity while eliminating native dependency conflicts.

---

## Core Engine Libraries

LITIENGINE intentionally avoids heavy native dynamic bindings (like C/C++ OpenGL layers), maintaining pure cross-platform portability across Windows, Linux, and macOS. The engine core only includes a minimal set of runtime dependencies:

| Library | Version / Source | Purpose |
|:---|:---|:---|
| **[Input4j](https://github.com/gurkenlabs/input4j)** | 1.3.1 | Gamepad, joystick, and controller input integration utilizing Java Panama Foreign Function & Memory (FFM) APIs with zero external DLL/so dependencies. |
| **[VorbisSPI](https://central.sonatype.com/artifact/com.googlecode.soundlibs/vorbisspi)** | 1.0.3.3 | Java Sound Service Provider Interface for decoding and streaming `.ogg` Vorbis audio files. |

---

## Game Development Tools & Integrations

<div class="grid cards" markdown>

- :material-cube-outline:{ .lg .middle } **[utiLITI Editor](utiliti-editor/README.md)**

    ---

    The official 2D level editor, tileset designer, asset packager, and live Java script executor bundled directly with LITIENGINE.

- :material-map-outline:{ .lg .middle } **[Tiled Map Editor](https://www.mapeditor.org/)**

    ---

    Full bi-directional support for importing and editing `.tmx` maps and `.tsx` tilesets exported from the industry-standard Tiled editor.

- :material-palette-outline:{ .lg .middle } **[Aseprite](https://www.aseprite.org/) & Pixel Art Tools**

    ---

    Seamless workflow for importing spritesheet grids, JSON texture atlases, and animation frame sequences exported from Aseprite.

- :material-robot-outline:{ .lg .middle } **[Model Context Protocol (MCP)](utiliti-editor/mcp-server.md)**

    ---

    Built-in JSON-RPC / SSE server in utiLITI enabling AI coding agents (OpenCode, Antigravity, Codex) to inspect and edit levels directly.

</div>

---

## Steam Integration (steamworks4j)

LITIENGINE does not bundle or require Steam libraries out of the box—games remain 100% independent with zero forced dependencies. 

However, if you plan to distribute your game commercially on Steam, the open-source **[steamworks4j](https://github.com/code-disaster/steamworks4j)** library is the recommended bridge for accessing Steamworks SDK features (achievements, cloud saves, leaderboards, and overlay).

### 1. Add steamworks4j Dependency
In your `build.gradle`:

```groovy title="build.gradle"
dependencies {
  implementation 'com.code-disaster.steamworks4j:steamworks4j:1.9.0'
  implementation 'com.code-disaster.steamworks4j:steamworks4j-server:1.9.0'
}
```

### 2. Configure App ID & Initialization
1. Register your title on the [Steamworks Partner Portal](https://partner.steamgames.com) to obtain your game's numerical **AppID**.
2. Create a text file named `steam_appid.txt` in your project root containing only your AppID (e.g. `480` for Spacewar test):
    ```text title="steam_appid.txt"
    480
    ```
3. Initialize the Steam API during game startup:
    ```java title="SteamProgram.java"
    package com.example.game;

    import com.codedisaster.steamworks.SteamAPI;
    import com.codedisaster.steamworks.SteamException;
    import de.gurkenlabs.litiengine.Game;

    public class SteamProgram {
      public static void main(String[] args) {
        try {
          if (SteamAPI.init()) {
            System.out.println("Steamworks initialized successfully!");
          }
        } catch (SteamException e) {
          System.err.println("Failed to initialize Steam: " + e.getMessage());
        }

        Game.init(args);
        Game.start();
      }
    }
    ```

---

## Standalone Distribution & Packaging Tools

When preparing your game for release, these tools allow you to package standalone binaries that require no pre-installed Java on the player's computer:

* **[jpackage](https://docs.oracle.com/en/java/javase/21/jpackage/using-jpackage.html)**: Bundled tool in JDK 21+ for generating native `.msi` / `.exe` (Windows), `.dmg` / `.app` (macOS), and `.deb` / `.rpm` (Linux) installers.
* **[jlink](https://docs.oracle.com/en/java/javase/21/docs/specs/man/jlink.html)**: Generates a lightweight, stripped-down Java runtime containing only the modules your game actively uses (~35–45 MB).
* **[Launch4j](https://launch4j.sourceforge.net/)**: Wraps your executable JAR into a lightweight Windows native `.exe` with customized icons and splash screens.
* **[Gradle Shadow Plugin](https://imperceptiblethoughts.com/shadow/)**: Bundles all compiled classes and third-party dependencies into a single executable fat JAR.

---

## Related Documentation

<div class="grid cards" markdown>

- :material-play-box-outline:{ .lg .middle } **[Deployment & Distribution](deployment.md)**

    ---

    Step-by-step instructions on bundling standalone executables with jlink and Launch4j.

- :material-map-legend:{ .lg .middle } **[Tile Maps Overview](tile-maps/README.md)**

    ---

    Guide to loading TMX maps, configuring layers, and reading custom map properties.

</div>
