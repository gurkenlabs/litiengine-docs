---
title: "Game API Overview"
icon: "lucide/code-2"
description: "Core LITIENGINE static API gateways: Game.world(), Game.physics(), Game.graphics(), Game.audio(), Game.loop(), and Game.tweens()."
keywords: ["LITIENGINE Game API", "Game.world", "Game.physics", "Game.graphics", "Game.audio", "Game.loop", "Game.tweens"]
tags: ["game-api", "world", "physics", "graphics", "audio", "loop", "tweens", "screens"]
---

# Game API Overview

The `Game` class acts as the central hub and orchestrator of LITIENGINE. It exposes specialized singleton managers providing access to every engine subsystem.

---

## Core Game Subsystems

<div class="grid cards" markdown>

- :material-earth:{ .lg .middle } **[Game World & Environments](game-world.md)**

    ---

    Loading `.tmx` maps, switching active scenes, entity lookup, and spatial query indexing.

- :material-camera-outline:{ .lg .middle } **[Camera & Viewport](camera.md)**

    ---

    Smooth target tracking, map clamping, zoom transitions, screen shake trauma, and coordinate conversion.

- :material-atom:{ .lg .middle } **[Physics & Collisions](physics-engine.md)**

    ---

    Spatial quadtrees, raycasting, velocity resolution, bounding box collisions, and force gravity.

- :material-palette-outline:{ .lg .middle } **[2D Graphics & Rendering](render-engine.md)**

    ---

    Double-buffered AWT rendering pipeline, Y-sorted render layers, shapes, and `TextRenderer`.

- :material-volume-high:{ .lg .middle } **[Sound & Audio Engine](sound-engine.md)**

    ---

    2D positional spatial audio falloff, `.ogg` Vorbis streaming, sound effect caching, and music playlists.

- :material-timer-outline:{ .lg .middle } **[Game Loop & Timing](loops.md)**

    ---

    Game loop execution, delta time calculations, update callbacks, and scheduled delay tasks.

- :material-creation:{ .lg .middle } **[Tweens & Easing](tweens.md)**

    ---

    Property interpolation framework with Robert Penner easing equations (`QUAD`, `BOUNCE`, `ELASTIC`).

- :material-monitor:{ .lg .middle } **[Screens & Game States](screens.md)**

    ---

    Scene state manager for Title Screen, Gameplay Screen, Pause Overlay, and Game Over sequences.

- :material-code-json:{ .lg .middle } **[Full Javadoc Reference](https://docs.litiengine.com/javadoc/)**

    ---

    Complete Java API documentation for all packages, classes, and methods across the engine.

</div>
