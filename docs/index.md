---
title: Documentation Overview
icon: lucide/book-open
description: Official technical documentation, API guides, tutorials, and tooling
  reference for LITIENGINE, the free, open-source 2D Java Game Engine.
keywords: [LITIENGINE, java, game engine, 2D, docs, api reference, tutorials, utiliti]
tags: [overview, quickstart, getting-started, java, 2d-engine, game-development]
---
# LITIENGINE Documentation

Welcome to the official technical documentation for **LITIENGINE**, the free and open-source 2D Java Game Engine.

> **Main Website & Community:** Looking for general game engine news, indie showcase games, forum discussions, or downloads? Visit the **[Official LITIENGINE Website](https://litiengine.com/)** and the **[LITIENGINE Community Showcase](https://litiengine.com/showcase/)**.

---

## Documentation Sections

<div class="grid cards" markdown>

- :material-rocket-launch:{ .lg .middle } **[Get Started](getting-started/README.md)**

    ---

    Install Java 21 LTS+, configure Gradle or Maven, and run your first 2D game in 15 lines of pure Java.

- :material-code-json:{ .lg .middle } **[Core Game API](game-api/README.md)**

    ---

    Explore decoupled game loops, 2D physics, camera tracking, input handling, and positional spatial audio.

- :material-hammer-wrench:{ .lg .middle } **[utiLITI Editor](utiliti-editor/README.md)**

    ---

    Design maps, manage tilesets, edit sprite sheets, and script live game entities with the Monaco workspace.

- :material-school:{ .lg .middle } **[Tutorials](tutorials/2d-platformer.md)**

    ---

    Step-by-step guides building a 2D Platformer, an Arkanoid clone, or a Top-Down Action Twin-Stick Shooter.

- :material-tune:{ .lg .middle } **[Advanced Topics](advanced/dynamic-lighting.md)**

    ---

    Dynamic 2D lighting, particle systems, performance tuning, string localization, and serialization.

- :material-help-circle-outline:{ .lg .middle } **[Project & Reference](frequently-asked-questions.md)**

    ---

    Frequently asked questions, release notes, engine roadmap, dependencies, and term glossary.

</div>

---

## Quick Setup

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

## Support & Sponsor LITIENGINE

LITIENGINE is 100% free, independent, and open source. If LITIENGINE helps you build your games, please consider backing the project:

<div class="grid cards" markdown>

- :material-heart:{ .lg .middle } **Support Independent Open-Source Game Tech**

    ---

    Every recurring backer or one-time contribution directly funds engine maintenance, documentation, and tooling.

    [Become a Backer on Open Collective](https://opencollective.com/litiengine){ .md-button .md-button--primary style="background: linear-gradient(135deg, #ea4c89 0%, #ff5e7e 100%); border-color: #ea4c89; color: white; font-weight: bold; margin-top: 0.5rem;" }

</div>

---

## Community & Resources

* **[Official Website](https://litiengine.com/)** — Engine overview, news, and official releases.
* **[Community Showcase](https://litiengine.com/showcase/)** — Featured games built by the community.
* **[Community Forum](https://forum.litiengine.com/)** — Discussion boards and technical Q&A.
* **[GitHub Repository](https://github.com/gurkenlabs/litiengine)** — Source code, issue tracker, and feature requests.
* **[API Quick Reference](getting-started/api-quick-reference.md)** — Core engine method and class cheat sheet.
