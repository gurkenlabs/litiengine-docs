---
title: Core Game API
icon: lucide/gamepad-2
description: 'Master LITIENGINE''s core subsystems: 2D Graphics, Positional Sound,
  Physics Quadtrees, Game Loop, Cameras, and Screens.'
keywords: [LITIENGINE, game api, graphics, audio, physics, game loop, camera, screens]
tags: [game-api, architecture, core, systems, subsystems]
---
# Core Game API

The **Game API** forms the static backbone of LITIENGINE, providing high-performance subsystems for rendering, spatial physics, audio playback, viewports, and display management.

---

## Core Subsystems

<div class="grid cards" markdown>

- :material-palette:{ .lg .middle } **[2D Graphics Engine](/game-api/render-engine/)**

    ---

    Double-buffered AWT rendering, sprite transformations, shape drawing, and `TextRenderer` outlines.

- :material-volume-high:{ .lg .middle } **[2D Sound Engine](/game-api/sound-engine/)**

    ---

    Spatial audio playback, background music streaming, 2D attenuation, and sound effects.

- :material-atom:{ .lg .middle } **[2D Physics Engine](/game-api/physics-engine/)**

    ---

    Bounding-box collisions, spatial quadtree acceleration, collision sliding, and raycasting.

- :material-clock-fast:{ .lg .middle } **[Game Loop & Timers](/game-api/loops/)**

    ---

    Decoupled 60 Hz physics update tick, fixed-rate logic timers, and delta-time interpolation.

- :material-video-vintage:{ .lg .middle } **[Camera & Viewport](/game-api/camera/)**

    ---

    Smooth target tracking, zoom levels, viewport shaking, and bounding constraints.

- :material-monitor-screenshot:{ .lg .middle } **[Screens & State Flow](/game-api/screens/)**

    ---

    Managing Title screens, Gameplay worlds, HUD overlays, and Pause menus.

- :material-animation-play:{ .lg .middle } **[Tweening Engine](/game-api/tweens/)**

    ---

    Smooth easing transitions for positions, alpha transparency, rotations, and UI scaling.

- :material-earth:{ .lg .middle } **[Game World](/game-api/game-world/)**

    ---

    Dynamic environment management, ambient lighting colors, and procedural map loading.

</div>
