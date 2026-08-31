---
title: Project Structure
icon: lucide/folder-tree
description: Learn best practices for organizing your LITIENGINE game project hierarchy and asset pipeline.
keywords: [LITIENGINE, java, gradle project structure, maven, 2D game architecture, litidata]
tags: [project-structure, architecture, organization, directories, assets]
---

# Project Structure

LITIENGINE follows modern Java application standards and integrates seamlessly with standard build tools like **Gradle** and **Maven**.

---

## Canonical Project Hierarchy

A standard Gradle-based LITIENGINE game project adheres to the standard `src/main/java` and `src/main/resources` structure:

```text
my-game/
├── build.gradle.kts (or build.gradle)
├── settings.gradle.kts (or settings.gradle)
├── gradlew
├── gradlew.bat
├── gradle/
│   └── wrapper/
│       ├── gradle-wrapper.jar
│       └── gradle-wrapper.properties
├── src/
│   ├── main/
│   │   ├── java/
│   │   │   └── com/example/game/
│   │   │       ├── Program.java
│   │   │       ├── entities/
│   │   │       │   └── Player.java
│   │   │       └── screens/
│   │   │           └── IngameScreen.java
│   │   └── resources/
│   │       ├── game.litidata
│   │       └── config.properties
│   └── test/
│       └── java/
│           └── com/example/game/
│               └── GameLogicTest.java
└── raw-assets/               (Optional source assets folder for utiLITI)
    ├── maps/
    │   ├── level1.tmx
    │   └── tileset.tsx
    ├── sprites/
    │   └── hero.png
    └── audio/
        └── battle.ogg
```

---

## Asset Pipeline: Raw Assets vs `.litidata`

LITIENGINE uses a streamlined two-tier asset workflow:

1. **Source Assets (`raw-assets/`)**: Individual `.png` spritesheets, `.tmx` maps from Tiled, `.tsx` tilesets, and `.ogg` audio files. You organize these in your filesystem and edit them with your favorite creative tools.
2. **Resource Bundle (`game.litidata`)**: The **utiLITI Editor** packages all referenced maps, tilesets, spritesheets, and sound metadata into a single optimized `.litidata` file. 
3. **Runtime Loading**: Place the resulting `game.litidata` inside `src/main/resources/`. When you compile your application into a standalone JAR, `Resources.load("game.litidata")` reads the packaged binary directly from the classpath with zero extra configuration.

---

## Directory Responsibilities

| Directory / File | Purpose |
| :--- | :--- |
| **`src/main/java/`** | Contains all Java source files, entity classes, screen managers, ability scripts, and game controllers. |
| **`src/main/resources/`** | Bundled classpath assets including `game.litidata`, string localization files (`strings.properties`), and default engine configs. |
| **`src/test/java/`** | Automated unit and integration tests (JUnit 5). |
| **`build.gradle.kts`** | Dependency declarations, Java toolchains, JVM compiler flags, and shadow JAR packaging tasks. |

---

## See Also

- [Build Systems & Dependency Setup](build-systems.md) - Gradle & Maven starter configs
- [Get LITIENGINE](get-litiengine.md) - Dependency installation
- [Project Management in utiLITI](../utiliti-editor/create-projects.md) - Creating `.litidata` files
