---
title: "Frequently Asked Questions"
icon: "lucide/help-circle"
description: "Comprehensive FAQ addressing LITIENGINE architecture, Java 25+ support, performance, game loops, persistence, multiplayer, and distribution."
keywords: ["LITIENGINE FAQ", "questions", "java 2D game", "performance", "platforms", "savegame", "multiplayer", "scaling", "licensing", "steam", "Java 25"]
tags: ["faq", "questions", "troubleshooting", "help", "basics", "architecture", "multiplayer"]
---

# Frequently Asked Questions

Quick, fact-checked answers to the most common questions about LITIENGINE architecture, performance, mechanics, persistence, tooling, and distribution.

---

## General & Architecture

??? question "Is LITIENGINE a library or a full game engine?"
    LITIENGINE is a **modular 2D Java Game Engine and Framework**. Unlike monolithic engines (such as Unity or Godot) that require proprietary scripting environments and heavy runtime editors, LITIENGINE is **code-first**:

    * It is distributed as a standard Java library dependency (`implementation 'de.gurkenlabs:litiengine:{{ version }}'`).
    * You write standard, idiomatic Java in your favorite IDE (IntelliJ IDEA, Eclipse, or VS Code).
    * It provides all core engine subsystems out of the box: a fixed-tick game loop, spatial quadtree physics, hardware-accelerated 2D rendering, 2D positional audio, dynamic lighting, particle systems, tweening, and entity lifecycles.
    * The companion **utiLITI Editor** is an optional visual level design, asset compilation, and debugging tool.

??? question "What Java version is required?"
    LITIENGINE requires **Java {{ java_version }} or newer**.
    
    The engine takes full advantage of modern Java platform capabilities:
    
    * **Foreign Function & Memory (FFM) API (JEP 454)**: Powers low-latency gamepad polling via `Input4j` with zero native JNI dynamic link libraries.
    * **Modern Language Features**: Pattern matching for switch, record patterns, and virtual threads.
    * **JVM Flag**: When running your game or packaging distributions, add `--enable-native-access=ALL-UNNAMED` to authorize the FFM API for gamepad support without runtime warnings.

??? question "Why pure Java with AWT instead of OpenGL/Vulkan bindings?"
    LITIENGINE deliberately avoids heavy native dynamic C/C++ bindings (such as LWJGL or libGDX JNI wrappers):

    * **Zero Native Library Hassle**: No platform-specific DLL/so/dylib extraction, driver incompatibilities, or architecture mismatch crashes (especially seamless across x86_64 and Apple Silicon ARM64).
    * **Hardware Accelerated**: The underlying Java 2D pipeline automatically uses hardware-accelerated backends provided by the host OS (Direct3D on Windows, Metal on macOS, and OpenGL/X11 on Linux).
    * **High Performance**: Combined with double/triple buffering via `BufferStrategy`, spatial quadtree indexing, and offscreen surfaces, LITIENGINE easily renders thousands of animated sprites and particles at solid 60+ FPS.

??? question "How does the game loop work?"
    LITIENGINE coordinates updates, input polling, physics, and rendering through a unified tick loop (`Game.loop()`):

    1. **Invariable Update Phase**: Polls connected hardware devices (`Input.keyboard()`, `Input.mouse()`, `Input.gamepads()`) and updates internal timing metrics.
    2. **Scaled Update Phase (`super.process()`)**: Executes registered `IUpdateable` components, physics simulation, spatial quadtree indexing, entity behaviors, and tweens.
    3. **Timed Actions**: Dispatches delayed callbacks registered via `Game.loop().perform(delayMs, action)`.
    4. **Camera Focus Update**: Calculates camera target interpolation and screen shake.
    5. **Render Phase**: Renders the active `Screen`, map layers, entities, and GUI components via the `RenderComponent` Graphics2D pipeline.
    6. **Metrics Tracking**: Records tick execution times and frame rates.

    You can adjust the simulation speed at runtime using `Game.loop().setTimeScale(float)` (e.g. `0.0f` to pause, `0.5f` for slow-motion, or `2.0f` for fast-forward).

??? question "Can LITIENGINE run in headless mode (e.g. for dedicated servers or tests)?"
    **Yes.** LITIENGINE natively supports headless execution via `Game.hideGUI(true)` or the command-line argument `-nogui` (`Game.COMMANDLINE_ARG_NOGUI`):

    ```java
    public static void main(String[] args) {
      Game.init(args); // Pass -nogui flag
      Game.world().loadEnvironment("arena");
      Game.start();
    }
    ```

    In headless mode, the window, canvas, cursor, and AWT graphics subsystems are skipped entirely, while the fixed-tick `GameLoop`, physics engine, spatial quadtree, and game entities run at full fidelity. This is ideal for dedicated multiplayer servers, AI simulation benchmarks, and CI unit tests.

??? question "Does LITIENGINE collect any telemetry or user data?"
    **No.** Neither the LITIENGINE runtime library nor the utiLITI Editor collects any analytics, crash reports, tracking pixels, or user telemetry.

---

## Graphics, Scaling & Display

??? question "How do I handle pixel art scaling and high-DPI displays?"
    To keep retro pixel art crisp and prevent blurriness on 1080p, 1440p, or 4K displays:

    ```java
    // 1. Disable bilinear filtering for nearest-neighbor pixel rendering
    Game.config().graphics().setColorInterpolation(false);

    // 2. Set camera zoom scale (e.g. 3x or 4x)
    Game.world().camera().setZoom(3.0f, 0);

    // 3. Clamp camera movement to whole map boundaries
    Game.world().camera().setClampToMap(true);
    ```

??? question "Can I toggle fullscreen mode at runtime?"
    **Yes.** LITIENGINE supports three runtime display modes via `Game.window().setDisplayMode(...)`:

    ```java
    import de.gurkenlabs.litiengine.configuration.DisplayMode;

    // Switch to borderless fullscreen (recommended for modern multi-monitor setups)
    Game.window().setDisplayMode(DisplayMode.BORDERLESS);

    // Switch to exclusive fullscreen mode
    Game.window().setDisplayMode(DisplayMode.FULLSCREEN);

    // Switch back to standard windowed mode
    Game.window().setDisplayMode(DisplayMode.WINDOWED);
    ```

    You can check the active mode anytime with `Game.config().graphics().getDisplayMode()`.

??? question "How does LITIENGINE's coordinate system work?"
    LITIENGINE uses a **top-left origin `(0, 0)`** convention inherited from standard 2D computer graphics:

    * `+X` increases to the right.
    * `+Y` increases downward.

    The engine works with three primary coordinate spaces:

    1. **Tile Coordinates**: Discrete grid indices `(tileX, tileY)` representing cells on a tile map.
    2. **World / Map Coordinates**: Continuous floating-point pixel positions on the level map.
    3. **Viewport / Screen Coordinates**: Window pixel positions adjusted for camera focus and zoom.

    For more details, see **[Coordinate Systems & Spatial Spaces](game-api/coordinate-systems.md)**.

??? question "How do I convert between Screen, World, and Tile coordinates?"
    LITIENGINE provides built-in conversion helpers on `Input.mouse()`, `Camera`, and `MapUtilities`:

    * **Mouse &rarr; World (Map)**: `Input.mouse().getMapLocation()`
    * **Mouse &rarr; Tile Grid**: `Input.mouse().getTile()`
    * **Screen Point &rarr; World**: `Game.world().camera().getMapLocation(screenPoint)`
    * **World &rarr; Screen Point**: `Game.world().camera().getViewportLocation(mapPoint)`
    * **World &rarr; Tile Grid**: `MapUtilities.getTile(mapLocation)`
    * **Tile Grid &rarr; World**: `MapUtilities.getMapLocation(map, tilePoint)`

??? question "Why are my collision checks or tile queries off by half a tile?"
    `entity.getLocation()` returns the **top-left corner** of an entity's sprite bounding box.
    
    When performing distance checks, line-of-sight calculations, pathfinding queries, or tile lookups, use:
    
    * **`entity.getCenter()`**: Geometric center of the entity's bounding box.
    * **`entity.getCollisionBoxCenter()`**: Exact center of the entity's physical collision box.
    * **`entity.getCollisionBox()`**: Bounding rectangle of the collider (configured via `@CollisionInfo`).

??? question "Does LITIENGINE support dynamic lighting and particle systems?"
    **Yes, both are built-in:**

    * **Lighting**: The `LightEngine` renders dynamic light sources (`LightSource`) with customizable radius, colors, alpha, and ambient dark overlay masks.
    * **Particles**: The `Emitter` system supports gravity, velocity vectors, fade effects, collision particles, and custom particle shapes (rectangles, circles, text, or sprites).

    Both can be placed visually in utiLITI or spawned dynamically via code.

---

## Mechanics, Audio & Persistence

??? question "What audio formats are supported and how are they cached?"
    LITIENGINE natively supports **`.ogg` (Vorbis)**, **`.mp3`**, and **`.wav`** files:

    * **Caching**: Audio files are loaded through `Resources.sounds().get("audio/sfx.ogg")` and decoded once into memory.
    * **2D Positional Audio**: `Game.audio().playSound("hit.ogg", enemyEntity)` automatically attenuates volume and pans audio based on the entity's distance from the camera focus.
    * **Music & Buses**: Background music streams via `Game.audio().playMusic("music/theme.ogg")`. Volume can be adjusted globally via `Game.audio().setMasterVolume(float)` or separated by sound and music channels in `Game.config().sound()`.

??? question "How do I save and load game states?"
    LITIENGINE does not force an opinionated save format. Instead, you define structured data models (such as Java Records or POJOs) and serialize them using standard JSON, XML, or binary serialization:

    ```java
    // 1. Define save data model
    public record PlayerSave(String name, double x, double y, int health, int coins) {}

    // 2. Save state to disk
    PlayerSave data = new PlayerSave("Hero", player.getX(), player.getY(), player.getHitPoints(), 150);
    Files.writeString(Path.of("save1.json"), jsonSerializer.toJson(data));

    // 3. Restore state on load
    PlayerSave loaded = jsonSerializer.fromJson(Files.readString(Path.of("save1.json")), PlayerSave.class);
    player.setLocation(loaded.x(), loaded.y());
    ```

    See the comprehensive architecture walkthrough in **[Savegames & State Persistence](savegames.md)**.

??? question "Can I create multiplayer or networked games with LITIENGINE?"
    **Yes.** Because LITIENGINE is pure Java without native UI lock-in, you can use any Java networking library (such as **Netty**, **Java NIO**, **WebSockets**, or **gRPC**):

    * **Authoritative Servers**: Run the game in headless mode (`Game.hideGUI(true)`) on your server to simulate physics, entity collision, and game logic identically to the client.
    * **Deterministic Updates**: The fixed-tick `GameLoop` ensures consistent physics simulation steps across clients and servers.

??? question "How does collision detection and physics simulation work?"
    LITIENGINE includes a dedicated **PhysicsEngine** and **CollisionEngine**:

    * **Broad-Phase Optimization**: Uses a 2D **Spatial Quadtree** (`SpatialIndex`) to rapidly eliminate non-colliding entities in $O(\log N)$ time.
    * **Narrow-Phase Geometry**: Resolves collisions using 2D geometric shapes (rectangles, polygons, circles) and raycasts (`Game.physics().raycast(...)`).
    * **Collision Types**: Entities can be static colliders (`CollisionBox`), movable collision entities (`ICollisionEntity`), or trigger zones (`Trigger`).

---

## Platforms & Deployment

??? question "What platforms can I deploy my game to?"
    You can package standalone games for:

    * **Windows** (x86_64)
    * **Linux** (x86_64 and ARM64, including **Steam Deck**)
    * **macOS** (x86_64 and Apple Silicon M1–M4 ARM64)

    Because LITIENGINE relies on the desktop Java AWT pipeline, mobile operating systems (Android/iOS) and web browsers (WebAssembly) are not supported.

??? question "Can I sell my LITIENGINE game commercially on Steam or itch.io?"
    **Yes!** LITIENGINE is licensed under the permissive **MIT License**:

    * You retain **100% ownership** of your game code, artwork, music, and commercial proceeds.
    * No royalties, engine licensing fees, or revenue shares are required.
    * For Steam integration (achievements, cloud saves, leaderboards), you can use open-source Java wrappers such as `steamworks4j`.

??? question "How do players run my game without installing Java?"
    You can bundle a minimal, self-contained Java Runtime Environment (JRE) directly with your game using **`jpackage`** (built into JDK 25) or **Launch4j**:

    * The final distribution is a native installer or portable folder (`.exe` on Windows, `.app`/`.dmg` on macOS, `.deb`/`.rpm`/tarball on Linux).
    * End users double-click an executable just like any native game without needing to install or configure Java.
    * Review the full setup in our **[Deployment Guide](deployment.md)**.

---

## Tooling, Editors & AI Integration

??? question "Do I have to use the utiLITI editor to make a game?"
    **No.** You can build games entirely in Java code using procedural world generation or raw Tiled maps.

    However, **utiLITI** provides visual workflows that save hundreds of hours:
    
    * Visual placement of entities, triggers, lights, spawnpoints, and collision boxes.
    * Wang terrain auto-tiling and tileset collision editors.
    * Sprite animation previewing and `.litidata` resource archiving.
    * Live in-editor playtesting and debugging (`Shift + F10` to run, `Shift + F9` to debug).

??? question "What is the `.litidata` file format?"
    A `.litidata` file is a consolidated binary resource package container created by utiLITI (internally compressed like a ZIP bundle). It packages maps, tilesets, spritesheets, audio files, and custom properties into a single file, loaded with one line in code:

    ```java
    Resources.load("game.litidata");
    ```

??? question "Can I use AI coding agents like OpenCode or Antigravity with LITIENGINE?"
    **Yes!** utiLITI includes an embedded **Model Context Protocol (MCP)** server:

    * **Listening Port**: Runs by default on `http://localhost:8080/mcp` (or port `8088` if reconfigured in Settings).
    * **Live Automation**: AI agents can query live maps, add entities, inspect properties, build terrain, and run playability audits in real time.
    * Check out our **[AI-Assisted Game Development Guide](tutorials/ai-game-development.md)**.

??? question "Can I use Tiled Map Editor alongside utiLITI?"
    **Yes.** LITIENGINE natively supports `.tmx` maps and `.tsx` tilesets exported from [Tiled Map Editor](https://www.mapeditor.org/). You can import `.tmx` maps into utiLITI projects or load them directly in code via `Resources.maps().get("map.tmx")`.

---

## Community & Support

??? question "Where can I get help, report bugs, or share my game?"

    * **Discord Community**: Join hundreds of 2D game developers on the [Official LITIENGINE Discord](https://discord.gg/9TqCq9C).
    * **GitHub Discussions**: Ask architectural questions and share projects at [github.com/gurkenlabs/litiengine/discussions](https://github.com/gurkenlabs/litiengine/discussions).
    * **Issue Tracker**: Report bugs and submit feature requests at [github.com/gurkenlabs/litiengine/issues](https://github.com/gurkenlabs/litiengine/issues).
    * **Official Forum**: Browse community guides and announcements at [forum.litiengine.com](https://forum.litiengine.com/).
