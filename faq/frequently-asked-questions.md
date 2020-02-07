---
description: >-
  Frequently asked questions about LITIengine and Java game development in
  general.
---

# Frequently Asked Questions

## LITIengine basics

### Is LITIengine a programming language or a library?

LITIengine is a 2D game library for Java. It is based on Java 8, but we plan to update to a later Java version soon.

### What's the current development status of LITIengine?

LITIengine is currently in Alpha. To find out what that means, please read our [Roadmap](../roadmap.md).

### Does LITIengine collect any user data?

LITIengine does not collect any user data via telemetry. However, if you register on our forum or subscribe to our newsletters, some of your information will be stored safely on our servers.  
We guarantee that your data is only used for the purposes you agreed with.

### What platforms can LITIengine deploy to?

With LITIengine, you can create games for Windows, Linux, and MacOS

### Whom is LITIengine made for?

LITIengine is made for anyone interested in creating 2D computer games with Java. Simple in nature, it is easy to pick up, yet powerful enough for creating massive worlds.

We think that if you are a relatively inexperienced Java developer seeking to create your first Java game, LITIengine might be the most hassle-free experience for you.

### Whom is LITIengine not made for?

If you are looking for a Java game engine able to deploy to mobile devices and browsers, LITIengine is unfortunately not your tool of choice.

Professional game developers experienced in using other engines might find LITIengine's capabilities a bit limiting, but we encourage you to request missing features [via GitHub issue](https://github.com/gurkenlabs/litiengine/issues).

### Since LITIengine is written in pure Java - what performance drawbacks can I expect?

LITIengine does not implement bindings for OpenGL or other graphics processing APIs. Hence, the CPU load is increased compared to other java game libraries, while the potential of GPU acceleration stays unexhausted. Most performance issues occur due to CPU-heavy computations \(e.g. updating too many particles or scaling lots of images at once\). Memory issues, on the other hand, occur rather rarely. While LITIengine per se runs on very low system specs, we have sometimes encountered poor performance when playing our previous games with older PCs, depending on the complexity of the game.

### Can I create LITIengine games without using the utiLITI editor?

Sure you can make a LITIengine game without using the editor. We've done that in the past and the editor is not a required piece in the development workflow. The main functionality of the utiLITI editor is to provide a convenient UI to position and configure [`Entities`](https://app.gitbook.com/@gurkenlabs/s/litiengine/~/drafts/-Lt4NljB3cbQX4NxqU4K/basics/entity-framework) in your maps and to ultimately provide a resource bundle for your game to simply load with a oneliner: e.g.[`Resources.load("game.litidata")`](https://www.javadoc.io/static/de.gurkenlabs/litiengine/0.4.19/de/gurkenlabs/litiengine/resources/Resources.html#load-java.net.URL-). Without such a resource bundle, you need to explicitly load all your resources from code using the [`Resources`](https://app.gitbook.com/@gurkenlabs/s/litiengine/~/drafts/-Lt4NljB3cbQX4NxqU4K/basics/resource-management) API.

Since the [`Entities`](https://app.gitbook.com/@gurkenlabs/s/litiengine/~/drafts/-Lt4NljB3cbQX4NxqU4K/basics/entity-framework) in the LITIengine can be loaded from [`MapObjects`](https://app.gitbook.com/@gurkenlabs/s/litiengine/~/drafts/-Lt4NljB3cbQX4NxqU4K/basics/manage-maps/map-objects), an alternative way to get things done is to directly add them in the _Tiled_ editor and provide the required [`MapObjectProperties`](https://www.javadoc.io/static/de.gurkenlabs/litiengine/0.4.19/de/gurkenlabs/litiengine/environment/tilemap/MapObjectProperty.html) if you want to use the engine's entity framework. This was, by the way, the workflow we went with before we had the editor. So you could say that the editor basically evolved from that. Everything that you see in the editor can also be done directly in code though, so if you want, you can totally skip the editor entirely, although it's not recommended.  
Btw: [`Entities`](https://app.gitbook.com/@gurkenlabs/s/litiengine/~/drafts/-Lt4NljB3cbQX4NxqU4K/basics/entity-framework)don't necessarily have to originate from [`MapObjects`](https://app.gitbook.com/@gurkenlabs/s/litiengine/~/drafts/-Lt4NljB3cbQX4NxqU4K/basics/manage-maps/map-objects), you can also add them to your [`GameWorld`](https://app.gitbook.com/@gurkenlabs/s/litiengine/~/drafts/-Lt4NljB3cbQX4NxqU4K/basics/game-api/game-world) directly from code.

### What's the best way to learn LITIengine?

We offer extensive tutorials on our website. It is also a good idea to look through the LITIengine docs pages. If concrete questions come up, you should visit the LITIengine forum. We do have a [YouTube channel](https://www.youtube.com/channel/UCN7-9zYTxip_Hl1LvCQ8RBA) as well, but due to video creation being such a time consuming task, don't expect many video tutorials being released from us anytime soon. Here's an overview over the most useful links for learning LITIengine:

* [LITIengine forum](https://forum.litiengine.com/)
* [LITIengine docs: Getting started](https://app.gitbook.com/@gurkenlabs/s/litiengine/~/drafts/-Lt4NljB3cbQX4NxqU4K/basics/getting-started)
* [LITIengine Javadocs](https://www.javadoc.io/doc/de.gurkenlabs/litiengine/latest/index.html)
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
* Code Examples
  * [Source Code of "GoIn -Behave or GET LOST!"](https://github.com/gurkenlabs/litiengine-ldjam42), made during LDJAM 42
  * [Source Code of "Servus Bonus"](https://github.com/gurkenlabs/litiengine-ldjam44), made during LDJAM 44

## Distribution

### How do I create executables for a Java game?

