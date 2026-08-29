---
title: "Project Structure"
icon: "lucide/folder-tree"
description: "Learn about best practices for setting up your game project hierarchy."
keywords: ["LITIENGINE", "java", "game", "gameengine", "development", "2D", "programming", "file", "project", "hierarchy", "structure"]
---

# Project Structure
## Initialize the project structure

Now, depending on the chosen build system, your project structure might look slightly different. LITIENGINE doesn't restrict you in how you can organize your project. However there are some common practices that we think are useful to apply for a Game project with the LITIENGINE:

* store your resources in `src` folders
* create multiple sub-folders for different types of resources
* save all the resources for your game within the project folder

## Content Authoring vs. Runtime Logic

In a typical LITIENGINE game project, responsibilities are clearly split between content authoring and game runtime logic:

* **Content & Resource Data (`.litidata`)**: Stored in a `.litidata` container file alongside maps (`.tmx`), tilesets (`.tsx`), spritesheets, sound assets, emitters, and entity blueprints. Created and authored using **utiLITI** or via the built-in **MCP (Model Context Protocol) Server**.
* **Game Logic & Behavior (`src/`)**: Implemented in the sibling Java/Gradle project. Custom entity types (`Creature`, `Prop`, `Trigger`), abilities (`Ability`, `Effect`), AI behavior controllers (`IBehaviorController`), game states/screens, and automated unit tests live in Java code.

> **Key Takeaway:** Game logic is typically implemented in the sibling Java/Gradle project beside the `.litidata` game-data project. Use utiLITI / MCP for content authoring and inspect the Gradle project for runtime behavior, APIs, and tests.

## An example LITIENGINE project structure

```text
game-project
└─── sprites
│   │─── sprite1.png
│   └─── ...
│─── audio
│   │─── sound1.ogg
│   └─── ...
│─── maps
│   │─── map1.tmx
│   │─── tileset.tsx
│   │─── tileset.png
│   └─── ...
│─── localization
│   │─── strings.properties
│   │─── strings_de_DE.properties
│   └─── ...
│─── src
│   └─── com
│        └─── mygame
│             │─── Program.java
│             └─── ...
│─── .classpath
│─── game.litidata
│─── config.properties
│─── build.gradle
│─── settings.gradle
└───...
```