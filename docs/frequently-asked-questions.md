---
title: "Frequently Asked Questions"
icon: "lucide/help-circle"
description: "Comprehensive FAQ addressing LITIENGINE architecture, Java 21+ support, performance, game loops, persistence, multiplayer, and distribution."
keywords: ["LITIENGINE FAQ", "questions", "java 2D game", "performance", "platforms", "savegame", "multiplayer", "scaling", "licensing", "steam"]
tags: ["faq", "questions", "troubleshooting", "help", "basics", "architecture", "multiplayer"]
---

# Frequently Asked Questions

Quick answers to the most common questions about LITIENGINE architecture, performance, mechanics, persistence, and distribution.

---

## General & Architecture

??? question "Is LITIENGINE a library or a full game engine?"
    LITIENGINE is a **modular 2D Java Game Library and Framework**. It provides everything needed to build commercial-grade 2D games: a decoupled 60 FPS update loop, 2D tile-based physics with spatial quadtrees, AWT graphics pipeline, 2D positional audio, entity lifecycle management, and the companion **utiLITI Editor**.

??? question "What Java version is required?"
    LITIENGINE requires **Java 21 LTS or newer** (tested through JDK 25). It leverages modern Java features including Java Panama Foreign Function & Memory (FFM) APIs for low-latency gamepad polling via `Input4j` with zero JNI setup.

??? question "Why pure Java with AWT instead of OpenGL/Vulkan bindings?"
    By relying on pure Java AWT 2D graphics without heavy native dynamic C/C++ libraries (like LWJGL or libGDX bindings), LITIENGINE games run identically across Windows, macOS, and Linux without native DLL hell, driver crashes, or platform-specific compilation hurdles.

??? question "How does the decoupled game loop work?"
    LITIENGINE uses a **decoupled multi-threaded loop**:
    
    1. **Update Loop (`Game.loop()`)**: Runs at a fixed, deterministic rate (default: **60 ticks/second**) executing physics, entity logic, timers, and AI.
    2. **Render Loop (`Game.window().getRenderComponent()`)**: Runs on the AWT graphics pipeline, interpolating positions to deliver smooth rendering regardless of display refresh rate.

??? question "Does LITIENGINE collect any telemetry or user data?"
    **No.** LITIENGINE and the utiLITI Editor contain zero telemetry, tracking, or analytics code.

---

## Graphics, Scaling & Display

??? question "How do I handle pixel art scaling and high-DPI displays?"
    LITIENGINE provides integer pixel scaling through the camera and render component:
    
    ```java
    // Set base camera zoom to 3x for crisp pixel art on 1080p/4K
    Game.world().camera().setZoom(3.0f, 0);
    
    // Clamp coordinates to whole pixel integers
    Game.world().camera().setClampToMap(true);
    ```

??? question "Can I toggle fullscreen mode at runtime?"
    Yes! You can toggle between borderless windowed, windowed, and exclusive fullscreen:
    
    ```java
    // Toggle fullscreen mode
    Game.window().getRenderComponent().setFullscreen(!Game.window().getRenderComponent().isFullscreen());
    ```

---

## Mechanics, Audio & Persistence

??? question "What audio formats are supported and how are they cached?"
    LITIENGINE natively supports **`.wav`** and **`.ogg` (Vorbis)** audio files. Sounds are loaded once via the unified resource manager (`Resources.sounds().get("sfx/hit.ogg")`) and cached in memory. The audio engine supports 2D positional distance falloff, background music playlists, and volume master buses.

??? question "How do I save and load game states?"
    LITIENGINE supports state persistence via the `Savegame` API or by serializing custom entity state to JSON:
    
    ```java
    // Built-in Savegame class
    Savegame save = new Savegame();
    save.setString("player_name", "Hero");
    save.setInt("coins", 42);
    save.save("saves/slot1.sav");
    ```

??? question "Can I create multiplayer or networked games with LITIENGINE?"
    **Yes.** Because LITIENGINE is pure Java, you can integrate standard Java networking libraries such as **Netty**, **Java NIO (WebSockets/TCP/UDP)**, or **gRPC**. LITIENGINE's deterministic tick loop makes client-side prediction and server reconciliation straightforward. See our **[Network Communication Guide](/advanced/network-communication/)**.

---

## Platforms & Deployment

??? question "What platforms can I deploy my game to?"
    You can package and deploy standalone desktop games for **Windows**, **Linux**, and **macOS** (including native Apple Silicon M1–M4). Because the engine uses standard Java AWT graphics, mobile platforms (Android/iOS) and web browsers (WebAssembly) are not supported.

??? question "Can I sell my LITIENGINE game commercially on Steam or itch.io?"
    **Yes!** LITIENGINE is licensed under the permissive **MIT License**. You retain 100% ownership of your game source code, assets, and commercial revenue. You can freely sell your games on Steam, itch.io, GOG, or your own store.

??? question "How do players run my game without installing Java?"
    You can bundle a lightweight Java Runtime Environment (JRE) directly with your game using **jlink**, **jpackage**, or **Launch4j**. The player receives a standalone `.exe`, `.app`, or `.zip` bundle (~35 MB) and simply double-clicks to play. See our **[Deployment Guide](/deployment/)**.

---

## Tooling, Editors & AI Integration

??? question "Do I have to use the utiLITI editor to make a game?"
    **No.** You can build complete games purely in Java code using procedural generation or raw Tiled maps. However, **utiLITI** significantly accelerates level design, entity placement, tileset Wang autotiling, and binary `.litidata` resource archiving.

??? question "Can I use AI coding agents like OpenCode or Antigravity with LITIENGINE?"
    **Yes!** utiLITI includes an embedded **Model Context Protocol (MCP)** server on port `8088`. AI agents can inspect loaded maps, place entities, configure colliders, and generate code directly. Check out our **[AI-Assisted Game Development Guide](/tutorials/ai-game-development/)**.

??? question "Can I use Tiled Map Editor alongside utiLITI?"
    **Yes.** LITIENGINE natively parses `.tmx` map files and `.tsx` tilesets exported from [Tiled Map Editor](https://www.mapeditor.org/). You can import `.tmx` maps directly into your `.litidata` projects in utiLITI.

---

## Community & Support

??? question "Where can I get help, report bugs, or share my game?"

    * **Discord Community**: Join hundreds of 2D game developers on the [Official LITIENGINE Discord](https://discord.gg/9TqCq9C).
    * **GitHub Discussions**: [github.com/gurkenlabs/litiengine/discussions](https://github.com/gurkenlabs/litiengine/discussions)
    * **Issue Tracker**: Report bugs and feature requests at [github.com/gurkenlabs/litiengine/issues](https://github.com/gurkenlabs/litiengine/issues)
