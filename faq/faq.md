---
description: >-
  Frequently asked questions about LITIengine and Java game development in
  general.
---

# Frequently Asked Questions

## LITIengine basics

### Is LITIengine a programming language or a library?

LITIengine is a 2D game library for Java. It is based on Java 8, but we plan to update to a later Java version soon. 

### What platforms can LITIengine deploy to?

With LITIengine, you can create games for Windows, Linux, and MacOS 

### Whom is LITIengine made for?

LITIengine is made for anyone interested in creating 2D computer games with Java. Simple in nature, it is easy to pick up, yet powerful enough for creating massive worlds. 

We think that if you are a relatively inexperienced Java developer seeking to create your first Java game, LITIengine might be the most hassle-free experience for you.

### Whom is LITIengine not made for

If you are looking for a Java game engine able to deploy to mobile devices and browsers, LITIengine is unfortunately not your tool of choice.

Professional game developers experienced in using other engines might find LITIengine's capabilities a bit limiting, but we encourage you to request missing features [via GitHub issue](https://github.com/gurkenlabs/litiengine/issues). 

### Since LITIengine is written in pure Java - what performance drawbacks can I expect?

LITIengine does not implement bindings for OpenGL or other graphics processing APIs. Hence, the CPU load is increased compared to other java game libraries, while the potential of GPU acceleration stays unexhausted. Most performance issues occur due to CPU-heavy computations \(e.g. updating too many particles or scaling lots of images at once\). Memory issues, on the other hand, occur rather rarely. While LITIengine per se runs on very low system specs, we have sometimes encountered poor performance when playing our previous games with older PCs, depending on the complexity of the game.

### Can I create LITIengine games without using the utiLITI editor?

Sure you can make a LITIengine game without using the editor. We've done that in the past and the editor is not a required piece in the development workflow. The main functionality of the utiLITI editor is to provide a convenient UI to position and configure [`Entities`](https://app.gitbook.com/@gurkenlabs/s/litiengine/~/drafts/-Lt4NljB3cbQX4NxqU4K/basics/entity-framework) in your maps and to ultimately provide a resource bundle for your game to simply load with a oneliner: e.g.[`Resources.load("game.litidata")`](https://www.javadoc.io/static/de.gurkenlabs/litiengine/0.4.17/de/gurkenlabs/litiengine/resources/Resources.html#load-java.net.URL-). Without such a resource bundle, you need to explicitly load all your resources from code using the [`Resources`](https://app.gitbook.com/@gurkenlabs/s/litiengine/~/drafts/-Lt4NljB3cbQX4NxqU4K/basics/resource-management) API.

Since the [`Entities`](https://app.gitbook.com/@gurkenlabs/s/litiengine/~/drafts/-Lt4NljB3cbQX4NxqU4K/basics/entity-framework) in the LITIengine can be loaded from [`MapObjects`](https://app.gitbook.com/@gurkenlabs/s/litiengine/~/drafts/-Lt4NljB3cbQX4NxqU4K/basics/manage-maps/map-objects), an alternative way to get things done is to directly add them in the _Tiled_ editor and provide the required [`MapObjectProperties`](https://www.javadoc.io/static/de.gurkenlabs/litiengine/0.4.17/de/gurkenlabs/litiengine/environment/tilemap/MapObjectProperty.html) if you want to use the engine's entity framework. This was, by the way, the workflow we went with before we had the editor. So you could say that the editor basically evolved from that. Everything that you see in the editor can also be done directly in code though, so if you want, you can totally skip the editor entirely, although it's not recommended.  
 Btw: [`Entities`](https://app.gitbook.com/@gurkenlabs/s/litiengine/~/drafts/-Lt4NljB3cbQX4NxqU4K/basics/entity-framework)don't necessarily have to originate from [`MapObjects`](https://app.gitbook.com/@gurkenlabs/s/litiengine/~/drafts/-Lt4NljB3cbQX4NxqU4K/basics/manage-maps/map-objects), you can also add them to your [`GameWorld`](https://app.gitbook.com/@gurkenlabs/s/litiengine/~/drafts/-Lt4NljB3cbQX4NxqU4K/basics/game-api/game-world) directly from code.

### What's the best way to learn LITIengine?

We offer extensive tutorials on our website. It is also a good idea to look through the LITIengine docs pages. If concrete questions come up, you should visit the LITIengine forum. We do have a [YouTube channel](https://www.youtube.com/channel/UCN7-9zYTxip_Hl1LvCQ8RBA) as well, but due to video creation being such a time consuming task, don't expect many video tutorials being released from us anytime soon. Here's an overview over the most useful links for learning LITIengine:

* [LITIengine forum](https://forum.litiengine.com/)
* [LITIengine docs: Getting started](https://app.gitbook.com/@gurkenlabs/s/litiengine/~/drafts/-Lt4NljB3cbQX4NxqU4K/basics/getting-started)
* User Guides
  * Getting started with LITIengine
    * [Part 1](https://litiengine.com/getting-started-setup-the-game-project/): Project setup
    * [Part 2](https://litiengine.com/getting-started-learning-the-basics/): Basic infrastructure
    * [Part 3](https://litiengine.com/getting-started-configuring-the-game/): Game Configuration
* Tutorials
  * Creating a platformer with LITIengine
    * [Part 1](https://litiengine.com/creating-a-platformer-1/)
    * [Part 2](https://litiengine.com/creating-a-platformer-2/)
* How-To's
  * [Importing .tmx maps in utiLITI](https://www.youtube.com/watch?v=RR3QxOhV8hM&t=1s)

## Libraries and Tools

This section contains useful information for external libraries related to Java Game Development.

### How to use steamworks4j SteamAPI from Eclipse?

LITIengine uses the **steamworks4j** wrapper for the SteamAPI to grant access to Steam features from java. When developing a game that uses these features, you need to execute a few extra steps in order to support the functionality from the IDE.

1. You need to have created the game on [Steamworks](https://partner.steamgames.com) in order to have an _appID_
2. Create an `steam_appid.txt` file containing only the _appID_ of your game
3. Copy the `steam_appid.txt` to the _working directory_ of your app.

   > For debugging and running your app from Eclipse \(or other IDEs\), the application will be run, using the `javaw.exe`. Your _working directory_ will typically be something like _C:\Program Files\Java\jdkX.X.X\_XXX\bin_, which is where your `javaw.exe` is located. This, of course, depends on your environment \(workspace/project\) _Java Build Path_ configuration of the editor

4. From here on, you can just follow the original tutorial [here](http://code-disaster.github.io/steamworks4j/getting-started.html#initialization).

### Tiled Map Editor

#### What is '_Tiled_'?

From the official [Tiled docs page](https://doc.mapeditor.org/en/stable/manual/introduction/):

> Tiled is a 2D level editor that helps you develop the content of your game. Its primary feature is to edit tile maps of various forms, but it also supports free image placement as well as powerful ways to annotate your level with extra information used by the game. Tiled focuses on general flexibility while trying to stay intuitive.

With Tiled editor, you can create orthogonal, hexagonal, and isometric Tile maps in no time. It is the absolute go-to tool for 2D Tile-based mapping.

#### How do I use Tiled?

For a general understanding of the mapping process with Tiled editor, we encourage you to have a look at its [plentiful documentation](https://doc.mapeditor.org/en/stable/manual/introduction/#creating-a-new-map). However, we will refer to a few LITIengine specific aspects of creating maps with Tiled in the sections about [Map Objects](https://docs.litiengine.com/basics/manage-maps/map-objects) and [custom properties](https://docs.litiengine.com/basics/manage-maps/custom-properties)

* First, you need to paint your Tileset in the [pixel painting program of your choice](https://www.slant.co/topics/1547/~best-pixel-art-sprite-editors).
* Then, import the Tileset image into Tiled editor to create a [.tsx Tileset](https://doc.mapeditor.org/en/stable/reference/tmx-map-format/#tileset).
* Create [layers](https://doc.mapeditor.org/en/stable/manual/layers/) containing Tiles, Objects, and Images.
* Save your map.

#### Why is tile mapping not a part of the utiLITI editor?

LITIengine had its origin in the idea of writing a Java 2D game engine without including _any_ external libraries \(what were we _thinking_?\). Yet, we believe that it is key to success to be able to sometimes rely on other people's expertise, especially when having limited resources. The Tiled editor has been developed by a vivid community for approximately ten years, offering a universal standard for tile maps. In other words, _it just works_. There is simply no need to reinvent the wheel when it comes to tile mapping.



## Distribution

### How do I create executables for a Java game?

