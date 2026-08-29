---
title: "LITIENGINE — Pure Java 2D Game Engine"
icon: "lucide/book-open"
description: "LITIENGINE is a free, open-source 2D Java Game Engine for creating tile-based 2D games with pure Java, AWT graphics, and zero external dependencies."
keywords: ["LITIENGINE", "java", "game engine", "2D", "open source", "awt", "panama ffm", "monaco", "mcp server"]
---

# LITIENGINE — Pure Java 2D Game Engine

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

- :material-school:{ .lg .middle } **[Step-by-Step Tutorials →](tutorials/2d-platformer.md)**

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

    Write game scripts, creature AI, and environment triggers in pure Java with instant in-editor execution and live reload.

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

```java title="src/main/java/com/example/game/Program.java" linenums="1"
package com.example.game;

import de.gurkenlabs.litiengine.Game;
import de.gurkenlabs.litiengine.resources.Resources;

public class Program {
  public static void main(String[] args) {
    Game.info().setName("My First LITIENGINE Game"); // (1)!
    Game.info().setVersion("v1.0.0");

    Game.init(args); // (2)!
    Resources.load("game.litidata"); // (3)!
    Game.world().loadEnvironment("level1"); // (4)!
    Game.start(); // (5)!
  }
}
```

1. Sets application metadata displayed in window title bars and logger outputs.
2. Initializes the graphics canvas, physics quadtrees, audio playback, and input devices.
3. Loads the binary asset archive containing maps, spritesheets, and sounds.
4. Initializes the environment and binds entities to the physics world.
5. Launches the decoupled 60 FPS update loop and rendering tick threads.

---

## Showcase & Open Source Games

Explore real-world games built with LITIENGINE:

* **[Gurk Nukem](https://github.com/gurkenlabs/litiengine-gurknukem)** — A classic 2D retro action platformer demo.
* **[Star Reaperz](https://github.com/gurkenlabs/litiengine-ldjam52)** — Fast-paced top-down twin-stick action game made for Ludum Dare 52.
* **[LITIENGINE Showcase](https://litiengine.com/showcase/)** — Community showcase of commercial and indie games.

---

## 💖 Support & Sponsor LITIENGINE

LITIENGINE is 100% free, independent, and open source. If LITIENGINE helps you build your games, please consider backing the project to fund dedicated engine development, maintenance, and community tooling:

<div class="grid cards" markdown>

- :material-heart:{ .lg .middle } **[Back LITIENGINE on Open Collective →](https://opencollective.com/litiengine)**

    ---

    Support the creators on Open Collective. Every recurring backer or one-time contribution helps keep the engine independent, modern, and actively developed.

</div>

---

## Community & Contributing

* 💖 **[Open Collective](https://opencollective.com/litiengine)** — Back the project and support ongoing development.
* 🐙 **[GitHub Repository](https://github.com/gurkenlabs/litiengine)** — Report issues, request features, and contribute.
* 💬 **[GitHub Discussions](https://github.com/gurkenlabs/litiengine/discussions)** — Ask questions, share progress, and chat with creators.
* 📖 **[API Quick Reference](getting-started/api-quick-reference.md)** — Complete engine method and class reference cheat sheet.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "SoftwareApplication",
  "name": "LITIENGINE",
  "operatingSystem": "Windows, macOS, Linux",
  "applicationCategory": "GameDevelopmentApplication",
  "programmingLanguage": "Java",
  "license": "https://github.com/gurkenlabs/litiengine/blob/master/LICENSE",
  "url": "https://docs.litiengine.com/",
  "description": "Free, open-source 2D Java Game Engine with AWT graphics, Panama FFM low-latency input, integrated utiLITI editor, physics quadtrees, and positional 2D audio.",
  "author": {
    "@type": "Organization",
    "name": "Gurkenlabs",
    "url": "https://gurkenlabs.com"
  },
  "offers": {
    "@type": "Offer",
    "price": "0",
    "priceCurrency": "USD"
  }
}
</script>
