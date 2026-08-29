---
title: "Getting Started with LITIENGINE"
description: "Learn how to set up your Java 21+ development environment, install LITIENGINE, configure build tools, and run your first 2D game."
keywords: ["LITIENGINE", "java", "game engine", "getting started", "setup", "quickstart", "gradle", "maven"]
---

# Getting Started

Welcome to **LITIENGINE**, the lightweight, free, and open-source 2D Java Game Engine! This chapter provides everything you need to set up your development environment, configure your project build system, and run your very first game window.

## Quick-Start Roadmap

```text
1. Install JDK 21+  ──►  2. Set Up IDE  ──►  3. Configure Gradle/Maven  ──►  4. Run Your First Game!
   (Temurin / GraalVM)      (IntelliJ / Eclipse)   (Dependency Management)        (Game.init & Game.start)
```

## Chapter Topics

| Guide | Description |
| :--- | :--- |
| **[Install JDK](/docs/getting-started/install-jdk/)** | Download and install Java 21 or later (Temurin, Corretto, GraalVM, or via SDKMAN). |
| **[Set Up IDE](/docs/getting-started/development-environment/)** | Configure your IDE (IntelliJ IDEA, Eclipse, NetBeans, or VS Code) for Java development. |
| **[Build Systems](/docs/getting-started/build-systems/)** | Set up Gradle or Maven to manage dependencies and build automation. |
| **[Project Structure](/docs/getting-started/project-structure/)** | Understand recommended directory layouts, resource locations, and asset folders. |
| **[Get LITIENGINE](/docs/getting-started/get-litiengine/)** | Add LITIENGINE dependencies or clone the engine snapshot builds. |
| **[Manage Native Libraries](/docs/getting-started/native-libraries/)** | Understand how LITIENGINE bundles native audio/gamepad libraries. |
| **[Run the Game](/docs/getting-started/run-the-game/)** | Write your `Program.java` entry point, initialize the game window, and launch the engine. |
| **[API Quick Reference](/docs/getting-started/api-quick-reference/)** | Cheat sheet with the most frequently used LITIENGINE APIs and one-liners. |

## Hello LITIENGINE: A Minimal Game

Here is the smallest complete LITIENGINE game:

```java
package com.mygame;

import de.gurkenlabs.litiengine.Game;
import de.gurkenlabs.litiengine.resources.Resources;

public class Program {
  public static void main(String[] args) {
    // 1. Set game metadata
    Game.info().setName("My First LITIENGINE Game");
    Game.info().setVersion("v1.0.0");

    // 2. Initialize engine subsystems
    Game.init(args);

    // 3. (Optional) Load resource bundle & world environment
    // Resources.load("game.litidata");
    // Game.world().loadEnvironment("level1");

    // 4. Start the game loop
    Game.start();
  }
}
```

## Next Steps

Follow the guides in order: begin by **[Installing the JDK](/docs/getting-started/install-jdk/)** and **[Setting Up Your IDE](/docs/getting-started/development-environment/)**.
