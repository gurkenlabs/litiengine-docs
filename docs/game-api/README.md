---
title: "Core Game API"
description: "Master LITIENGINE's core subsystems: 2D Graphics, Positional Sound, Physics Quadtrees, Game Loop, Cameras, and Screens."
keywords: ["LITIENGINE", "game api", "graphics", "audio", "physics", "game loop", "camera", "screens"]
---

# Core Game API

The **Game API** forms the static backbone of LITIENGINE, providing high-performance subsystems for rendering, spatial physics, audio playback, viewports, and display management.

---

## 🕹️ Core Subsystems

<div class="grid cards" markdown>

- :material-palette:{ .lg .middle } **[2D Graphics Engine](render-engine.md)**

    ---

    Double-buffered AWT rendering, sprite transformations, shape drawing, and `TextRenderer` outlines.

- :material-volume-high:{ .lg .middle } **[2D Sound Engine](sound-engine.md)**

    ---

    Spatial audio playback, background music streaming, 2D attenuation, and sound effects.

- :material-atom:{ .lg .middle } **[2D Physics Engine](physics-engine.md)**

    ---

    Bounding-box collisions, spatial quadtree acceleration, collision sliding, and raycasting.

- :material-clock-fast:{ .lg .middle } **[Game Loop & Timers](loops.md)**

    ---

    Decoupled 60 Hz physics update tick, fixed-rate logic timers, and delta-time interpolation.

- :material-video-vintage:{ .lg .middle } **[Camera & Viewport](camera.md)**

    ---

    Smooth target tracking, zoom levels, viewport shaking, and bounding constraints.

- :material-monitor-screenshot:{ .lg .middle } **[Screens & State Flow](screens.md)**

    ---

    Managing Title screens, Gameplay worlds, HUD overlays, and Pause menus.

- :material-animation-play:{ .lg .middle } **[Tweening Engine](tweens.md)**

    ---

    Smooth easing transitions for positions, alpha transparency, rotations, and UI scaling.

- :material-earth:{ .lg .middle } **[Game World](game-world.md)**

    ---

    Dynamic environment management, ambient lighting colors, and procedural map loading.

</div>
