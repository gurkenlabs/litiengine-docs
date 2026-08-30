# AGENTS.md - LITIENGINE Game Repository Guide

This repository contains a 2D game built with **LITIENGINE**, a free, open-source 2D Java Game Engine. This document provides technical rules, project architecture, build instructions, and coding standards for AI coding agents (Claude, Cursor, Copilot, Antigravity, etc.).

---

## 1. Project Overview & Tech Stack

- **Engine**: LITIENGINE (Java 2D Game Engine)
- **Language**: Java 21 LTS or newer (tested with JDK 21-25)
- **Build System**: Gradle 8.x / 9.x (or Maven)
- **Graphics Pipeline**: Pure Java AWT 2D (zero OpenGL/Vulkan C-bindings)
- **Input System**: Input4j (powered by Java Panama Foreign Function & Memory APIs)
- **Asset Packaging**: Single binary archive `game.litidata` created via the utiLITI Editor
- **Game Architecture**: Decoupled 60 FPS update loop with independent rendering interpolation

---

## 2. Build, Run, and Test Commands

Execute all tasks via the Gradle wrapper from the repository root:

```bash
# Run the game locally in development mode
./gradlew run

# Execute all unit tests and headless GameTestSuites
./gradlew test

# Build a standalone executable fat JAR (with all dependencies bundled)
./gradlew shadowJar

# Enforce code style and formatting (Google Java Format / Spotless)
./gradlew spotlessApply
```

---

## 3. Directory Structure

```text
/
├── src/
│   ├── main/
│   │   ├── java/com/example/game/
│   │   │   ├── Program.java             # Main application entry point
│   │   │   ├── entities/                # Custom entity classes (Player, Enemies, Props)
│   │   │   ├── controllers/             # Movement, AI, and Combat controllers
│   │   │   ├── screens/                 # Ingame UI screens (Title, GameScreen, HUD)
│   │   │   └── abilities/               # Spell and combat ability implementations
│   │   └── resources/
│   │       ├── game.litidata            # Bundled asset archive (maps, sprites, sounds)
│   │       └── config.properties        # Game configuration defaults
│   └── test/
│       └── java/com/example/game/       # Automated unit tests and headless game tests
├── build.gradle                         # Gradle dependencies & shadowJar config
└── AGENTS.md                            # AI Agent development instructions
```

---

## 4. Core Architecture Guidelines for AI Agents

### Application Lifecycle (`Program.java`)

Always follow the standard LITIENGINE startup sequence:

```java
package com.example.game;

import de.gurkenlabs.litiengine.Game;
import de.gurkenlabs.litiengine.resources.Resources;

public class Program {
  public static void main(String[] args) {
    // 1. Configure engine metadata
    Game.info().setName("My Game");
    Game.info().setVersion("v1.0.0");

    // 2. Initialize graphics, audio, physics, and input
    Game.init(args);

    // 3. Load asset archives
    Resources.load("game.litidata");

    // 4. Load initial level and launch loops
    Game.world().loadEnvironment("level1");
    Game.start();
  }
}
```

### Entity Creation & Annotations

- Derive characters from `Creature` and interactive objects from `Prop` or `CollisionEntity`.
- Use declarative annotations for physics, locomotion, and spritesheet bindings:

```java
package com.example.game.entities;

import de.gurkenlabs.litiengine.Align;
import de.gurkenlabs.litiengine.Valign;
import de.gurkenlabs.litiengine.entities.AnimationInfo;
import de.gurkenlabs.litiengine.entities.CollisionInfo;
import de.gurkenlabs.litiengine.entities.Creature;
import de.gurkenlabs.litiengine.entities.EntityInfo;
import de.gurkenlabs.litiengine.entities.MovementInfo;

@EntityInfo(width = 24, height = 32)
@MovementInfo(velocity = 90)
@CollisionInfo(collision = true, collisionBoxWidth = 16, collisionBoxHeight = 12, align = Align.CENTER, valign = Valign.DOWN)
@AnimationInfo(spritePrefix = "hero")
public class Player extends Creature {
  public Player() {
    super("hero");
  }
}
```

### Asset Access Rules

- **Never instantiate `ImageIcon` or `ImageIO.read()` directly in render loops.**
- Always retrieve assets via the static `Resources` hub:
  - `Resources.spritesheets().get("hero-walk")`
  - `Resources.sounds().get("audio/sfx/jump.wav")`
  - `Resources.maps().get("maps/level1.tmx")`
  - `Resources.fonts().get("fonts/retro.ttf", 16f)`

### Input Handling

- Use `Input.keyboard()` for discrete keys and action listeners.
- Use `Input.gamepads()` for analog stick axes and controller buttons.

```java
// Keyboard listener
Input.keyboard().onKeyTyped(KeyEvent.VK_SPACE, event -> player.jump());

// Gamepad polling
Input.gamepads().onPressed(Gamepad.Xbox.A, value -> player.interact());
```

---

## 5. Critical Pitfalls & Anti-Patterns to Avoid

1. ❌ **Do NOT introduce OpenGL, LWJGL, or Vulkan dependencies.** LITIENGINE relies on pure Java 2D AWT rendering.
2. ❌ **Do NOT perform disk I/O inside `render()` or `update()`.** Preload all assets in `Program.main()` or loading screens.
3. ❌ **Do NOT use Groovy for game scripting.** LITIENGINE supports pure Java scripting with runtime hot-reloading.
4. ❌ **Do NOT hardcode screen coordinates.** Use camera viewport coordinates (`Game.world().camera().viewportToWorld(...)`) or scaled resolution layouts.

---

## 6. utiLITI Editor & MCP Integration

- When modifying maps, entity properties, or tilesets, AI coding agents can communicate with the active **utiLITI Editor** via its embedded **Model Context Protocol (MCP)** server on `http://localhost:8088/mcp`.
- Use the MCP server to inspect active levels, place entities, adjust collision boxes, and trigger hot-reloads during development.
