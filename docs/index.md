---
title: "LITIENGINE — Pure Java 2D Game Engine"
description: "LITIENGINE is a free, open-source 2D Java Game Engine for creating tile-based 2D games with pure Java, AWT graphics, and zero external dependencies."
keywords: ["LITIENGINE", "java", "game engine", "2D", "open source", "awt", "panama ffm", "monaco", "mcp server"]
---

# LITIENGINE

<div class="grid cards" markdown>

- :material-rocket-launch:{ .lg .middle } **[Getting Started →](getting-started/README.md)**

    ---

    Install JDK 21+, configure Gradle/Maven, and boot up your first game window in less than 5 minutes.

- :material-hammer-wrench:{ .lg .middle } **[utiLITI Editor →](utiliti-editor/README.md)**

    ---

    Design maps, manage tilesets, edit sprite sheets, and script live game entities with the Monaco workspace.

- :material-code-json:{ .lg .middle } **[Game API Guide →](game-api/README.md)**

    ---

    Explore decoupled game loops, 2D physics, camera tracking, and positional spatial sound systems.

- :material-school:{ .lg .middle } **[Step-by-Step Tutorials →](tutorials/creating-a-platformer.md)**

    ---

    Build a 2D Platformer, an Arkanoid clone, or a Top-Down Action Twin-Stick Shooter from scratch.

</div>

---

## Why LITIENGINE?

**LITIENGINE** is a free, open-source 2D Java Game Engine engineered to give you the complete infrastructure for tile-based 2D games — platformers, top-down action shooters, tactical RPGs, and arcade games — with pure Java and zero external C-dependencies.

<div class="grid cards" markdown>

- :material-palette-outline: **Pure Java AWT 2D Rendering**

    ---

    Render crisp pixel art and scaled graphics using Java's built-in 2D Graphics. No complex OpenGL / Vulkan boilerplate required.

- :material-gamepad-variant-outline: **Modern Panama FFM Input**

    ---

    Low-latency cross-platform keyboard, mouse, and gamepad integration powered by Panama Foreign Function & Memory APIs via Input4j.

- :material-vector-polygon: **Integrated 2D Physics Engine**

    ---

    Tile collision maps, entity bounding boxes, velocity controllers, raycasting, and obstacle avoidance built directly into the engine core.

- :material-code-braces: **3-Tier Hot-Reload Scripting**

    ---

    Write game scripts, creature AI, and environment triggers in Groovy or Java with instant in-editor execution and live reload.

- :material-volume-high: **Positional 2D Spatial Sound**

    ---

    Stereo sound effects with automatic listener-distance falloff and background music streaming for `.wav`, `.mp3`, and `.ogg` formats.

- :material-robot-outline: **AI-Ready MCP Server Integration**

    ---

    Native Model Context Protocol (MCP) server integration allowing AI coding agents to inspect maps, edit entities, and run live diagnostic queries.

</div>

---

## Quick Start

Add LITIENGINE to your project build configuration:

=== "Gradle (Kotlin)"

    ```kotlin
    dependencies {
        implementation("de.gurkenlabs:litiengine:0.13.0-SNAPSHOT")
    }
    ```

=== "Gradle (Groovy)"

    ```groovy
    dependencies {
        implementation 'de.gurkenlabs:litiengine:0.13.0-SNAPSHOT'
    }
    ```

=== "Maven"

    ```xml
    <dependency>
        <groupId>de.gurkenlabs</groupId>
        <artifactId>litiengine</artifactId>
        <version>0.13.0-SNAPSHOT</version>
    </dependency>
    ```

### Your First Game in 15 Lines

```java
package com.example.game;

import de.gurkenlabs.litiengine.Game;
import de.gurkenlabs.litiengine.resources.Resources;

public class Program {
  public static void main(String[] args) {
    Game.info().setName("My First LITIENGINE Game");
    Game.info().setVersion("v1.0.0");

    Game.init(args);
    Resources.load("game.litidata");
    Game.world().loadEnvironment("level1");
    Game.start();
  }
}
```

---

## Showcase & Open Source Games

Explore real-world games built with LITIENGINE:

* **[Gurk Nukem](https://github.com/gurkenlabs/gurk-nukem)** — A classic 2D retro action platformer demo.
* **[Star Reaperz](https://github.com/gurkenlabs/litiengine-ldjam52)** — Fast-paced top-down twin-stick action game made for Ludum Dare 52.
* **[LITIENGINE Showcase](https://litiengine.com/showcase/)** — Community showcase of commercial and indie games.

---

## Community & Contributing

* 💬 **[LITIENGINE Forum](https://forum.litiengine.com/)** — Ask questions and share your projects.
* 🐙 **[GitHub Repository](https://github.com/gurkenlabs/litiengine)** — Report issues, request features, and contribute.
* 📖 **[Javadocs](https://litiengine.com/api/)** — Browse the complete class and method API documentation.
