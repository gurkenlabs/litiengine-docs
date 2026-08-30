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

- :material-earth:{ .lg .middle } **[Game World & Environments](/game-api/game-world/)**

    ---

    Loading `.tmx` maps, switching active scenes, entity lookup, and spatial query indexing.

- :material-camera-outline:{ .lg .middle } **[Camera & Viewport](/game-api/camera/)**

    ---

    Smooth target tracking, map clamping, zoom transitions, screen shake trauma, and coordinate conversion.

- :material-atom:{ .lg .middle } **[Physics & Collisions](/game-api/physics-engine/)**

    ---

    Spatial quadtrees, raycasting, velocity resolution, bounding box collisions, and force gravity.

- :material-palette-outline:{ .lg .middle } **[2D Graphics & Rendering](/game-api/render-engine/)**

    ---

    Double-buffered AWT rendering pipeline, Y-sorted render layers, shapes, and `TextRenderer`.

- :material-volume-high:{ .lg .middle } **[Sound & Audio Engine](/game-api/sound-engine/)**

    ---

    2D positional spatial audio falloff, `.ogg` Vorbis streaming, sound effect caching, and music playlists.

- :material-timer-outline:{ .lg .middle } **[Game Loop & Timing](/game-api/loops/)**

    ---

    Deterministic 60 FPS update loop, delta time calculations, timers, and scheduled delay tasks.

- :material-creation:{ .lg .middle } **[Tweens & Easing](/game-api/tweens/)**

    ---

    Property interpolation framework with Robert Penner easing equations (`QUAD`, `BOUNCE`, `ELASTIC`).

- :material-monitor:{ .lg .middle } **[Screens & Game States](/game-api/screens/)**

    ---

    Scene state manager for Title Screen, Gameplay Screen, Pause Overlay, and Game Over sequences.

</div>
