---
title: "Frequently Asked Questions"
description: "Answers to frequently asked questions about LITIENGINE architecture, Java 21+ support, performance, distribution, and commercial licensing."
keywords: ["LITIENGINE", "FAQ", "questions", "java", "game engine", "performance", "platforms", "editor", "licensing", "steam"]
---

# Frequently Asked Questions

Quick answers to the most common questions about LITIENGINE, architecture, performance, tooling, and distribution.

---

## 🎯 General & Architecture

??? question "Is LITIENGINE a library or a full game engine?"
    LITIENGINE is a **modular 2D Java Game Library and Framework**. It provides everything needed to build commercial-grade 2D games: a decoupled 60 FPS game loop, 2D tile-based physics with spatial quadtrees, AWT graphics pipeline, 2D positional audio, entity lifecycle management, and the companion **utiLITI Editor**.

??? question "What Java version is required?"
    LITIENGINE requires **Java 21 LTS or newer** (tested through JDK 25). It leverages modern Java features including Java Panama Foreign Function & Memory (FFM) APIs for low-latency gamepad polling via `Input4j`.

??? question "Why pure Java with AWT instead of OpenGL/Vulkan bindings?"
    By relying on pure Java AWT 2D graphics without heavy native dynamic C/C++ libraries (like LWJGL or libGDX bindings), LITIENGINE games run identically across Windows, macOS, and Linux without native DLL hell, driver crashes, or platform-specific compilation hurdles.

??? question "Does LITIENGINE collect any telemetry or user data?"
    **No.** LITIENGINE and the utiLITI Editor contain zero telemetry, tracking, or analytics code.

---

## 💻 Platforms & Deployment

??? question "What platforms can I deploy my game to?"
    You can package and deploy standalone desktop games for **Windows**, **Linux**, and **macOS** (including Apple Silicon M1–M4). Because the engine uses standard Java AWT graphics, mobile platforms (Android/iOS) and web browsers (WebAssembly) are not supported.

??? question "Can I sell my LITIENGINE game commercially on Steam or itch.io?"
    **Yes!** LITIENGINE is licensed under the permissive **MIT License** (or compatible open-source terms). You retain 100% ownership of your game source code, assets, and commercial revenue. You can freely sell your games on Steam, itch.io, GOG, or your own store.

??? question "How do players run my game without installing Java?"
    You can bundle a lightweight Java Runtime Environment (JRE) directly with your game using **jlink**, **jpackage**, or **Launch4j**. The player receives a standalone `.exe`, `.app`, or `.zip` bundle and simply double-clicks to play. See our **[Deployment Guide](deployment.md)**.

---

## ⚡ Performance & Engine Limits

??? question "What kind of performance can I expect from software AWT rendering?"
    LITIENGINE easily achieves a steady **60+ FPS** with hundreds of active entities and complex tile layers on standard desktop hardware. While it is not designed for 3D shaders or tens of thousands of simultaneous particles, it is exceptionally fast and memory-efficient for 2D pixel art, RPGs, platformers, and top-down action games.

??? question "How does LITIENGINE handle physics and collision detection?"
    LITIENGINE features a custom 2D bounding-box physics engine optimized with spatial quadtrees (`Game.physics()`). It supports collision sliding, raycasting, custom gravity forces, and entity velocity resolution without the overhead of heavy external physics engines like Box2D.

---

## 🛠️ Tooling & Workflows

??? question "Do I have to use the utiLITI editor to make a game?"
    **No.** You can build complete games purely in Java code using `new Environment(new TmxMap())` or procedural level generation. However, **utiLITI** significantly accelerates level design, entity placement, tileset Wang autotiling, and `.litidata` resource archiving.

??? question "Can I use Tiled Map Editor with LITIENGINE?"
    **Yes.** LITIENGINE natively supports `.tmx` map files and `.tsx` tilesets exported from [Tiled Map Editor](https://www.mapeditor.org/). You can import `.tmx` maps directly into your `.litidata` projects in utiLITI.

??? question "Does LITIENGINE support scripting languages?"
    Yes! LITIENGINE includes a dedicated multi-tier scripting engine supporting **Groovy** and **Java** with hot-reloading at runtime, plus Monaco editor integration inside utiLITI.

---

## 🤝 Community & Support

??? question "Where can I report bugs or ask for help?"
    * **GitHub Discussions**: [github.com/gurkenlabs/litiengine/discussions](https://github.com/gurkenlabs/litiengine/discussions)
    * **Issue Tracker**: [github.com/gurkenlabs/litiengine/issues](https://github.com/gurkenlabs/litiengine/issues)
