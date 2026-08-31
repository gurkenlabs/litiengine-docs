---
title: Documentation Overview
icon: lucide/book-open
description: Official technical documentation, API guides, tutorials, and tooling reference for LITIENGINE, the free, open-source 2D Java Game Engine.
keywords: [LITIENGINE, java, game engine, 2D, docs, api reference, tutorials, utiliti]
tags: [overview, quickstart, getting-started, java, 2d-engine, game-development]
---

# LITIENGINE Documentation

Welcome to the official technical documentation for **LITIENGINE**, the free and open-source 2D Java Game Engine.

---

## Documentation Sections

<div class="grid cards" markdown>

- :material-rocket-launch:{ .lg .middle } **[Get Started](getting-started/README.md)**

    ---

    Install Java {{ java_version }} LTS+, configure Gradle or Maven, and start your first LITIENGINE application in a few lines of Java.

- :material-code-json:{ .lg .middle } **[Core Game API](game-api/README.md)**

    ---

    Explore game loops, 2D physics, camera tracking, input handling, and positional spatial audio.

- :material-hammer-wrench:{ .lg .middle } **[utiLITI Editor](utiliti-editor/README.md)**

    ---

    Design maps, manage tilesets, edit sprite sheets, and script live game entities with the integrated Java scripting workspace.

- :material-school:{ .lg .middle } **[Tutorials](tutorials/topdown-shooter.md)**

    ---

    Step-by-step guides building a Top-Down Action Shooter, gameplay mechanics, and community recipe cookbooks.

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
    repositories {
      mavenCentral()
    }

    dependencies {
      implementation("de.gurkenlabs:litiengine:{{ version }}")
    }
    ```

=== "Gradle (Groovy)"

    ```groovy
    repositories {
      mavenCentral()
    }

    dependencies {
      implementation 'de.gurkenlabs:litiengine:{{ version }}'
    }
    ```

=== "Maven"

    ```xml
    <dependency>
      <groupId>de.gurkenlabs</groupId>
      <artifactId>litiengine</artifactId>
      <version>{{ version }}</version>
    </dependency>
    ```

---

!!! tip "Development Builds"
    Looking for development builds and bleeding-edge features? See **[Snapshot Versions](getting-started/get-litiengine.md#snapshot-versions)**.

---

## Your First LITIENGINE Window

Start your first LITIENGINE application in a few lines of Java:

```java title="src/main/java/com/example/game/Program.java" linenums="1"
package com.example.game;

import de.gurkenlabs.litiengine.Game;

public class Program {
  public static void main(String[] args) {
    Game.info().setName("My First LITIENGINE Game"); // (1)!
    Game.info().setVersion("1.0.0"); // (2)!

    Game.init(args); // (3)!
    Game.start(); // (4)!
  }
}
```

1. Sets application metadata displayed in window title bars and logger outputs.
2. Sets application version string (`1.0.0`).
3. Initializes LITIENGINE's core infrastructure, including configuration, window and rendering infrastructure, input, physics, the game loop, and the default camera.
4. Starts the game loop and runtime systems such as audio and tweens.

Run this class and LITIENGINE opens your first game window!

---

## Next Step: Load Your First Map

Once you create a `.litidata` resource bundle in the **utiLITI Editor**, load and start your game environment:

```java title="src/main/java/com/example/game/Program.java" linenums="1"
package com.example.game;

import de.gurkenlabs.litiengine.Game;
import de.gurkenlabs.litiengine.resources.Resources;

public class Program {
  public static void main(String[] args) {
    Game.info().setName("My First LITIENGINE Game");
    Game.info().setVersion("1.0.0");

    Game.init(args);
    Resources.load("game.litidata"); // (1)!
    Game.world().loadEnvironment("level1"); // (2)!
    Game.start();
  }
}
```

1. Loads a `.litidata` resource bundle created with utiLITI.
2. Loads the specified map as the active game environment.

Ready to build your world? Follow the next guide:

Next: **[Create Your First Project & Map with utiLITI](utiliti-editor/create-projects.md)** &rarr;

---

## Community & Resources

Looking for general game engine news, indie showcase games, forum discussions, or downloads?

* **[Official Website](https://litiengine.com/)** — Engine overview, news, and official releases.
* **[Community Showcase](https://litiengine.com/showcase/)** — Featured games built by the community.
* **[Community Forum](https://forum.litiengine.com/)** — Discussion boards and technical Q&A.
* **[Discord Community](https://discord.gg/9TqCq9C)** — Chat in real-time with fellow developers.
* **[GitHub Repository](https://github.com/gurkenlabs/litiengine)** — Source code, issue tracker, and feature requests.
* **[API Quick Reference](getting-started/api-quick-reference.md)** — Core engine method and class cheat sheet.

---

## Support & Sponsor LITIENGINE

LITIENGINE is 100% free, independent, and open source. If LITIENGINE helps you build your games, please consider backing the project:

<div class="grid cards" markdown>

- :material-heart:{ .lg .middle } **Support Independent Open-Source Game Tech**

    ---

    Every recurring backer or one-time contribution directly funds engine maintenance, documentation, and tooling.

    [Become a Backer on Open Collective](https://opencollective.com/litiengine){ .md-button .md-button--primary style="background: linear-gradient(135deg, #ea4c89 0%, #ff5e7e 100%); border-color: #ea4c89; color: white; font-weight: bold; margin-top: 0.5rem;" }

</div>
