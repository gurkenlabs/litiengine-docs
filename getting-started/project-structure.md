---
meta.description: Learn about best practices for setting up your game project hierarchy.
meta.keywords: LITIENGINE, java, game, gameengine, development, 2D, programming, file, project, hierarchy, structure
---

# Project Structure
## Initialize the project structure

Now, depending on the chosen build system, your project structure might look slightly different. LITIENGINE doesn't restrict you in how you can organize your project. However there are some common practices that we think are useful to apply for a Game project with the LITIENGINE:

* store your resources in `src` folders
* create multiple sub-folders for different types of resources
* save all the resources for your game within the project folder

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