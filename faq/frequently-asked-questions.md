---
description: Frequently asked questions about LITIENGINE and Java game development in general.
meta.title: Frequently Asked Questions
meta.description: Frequently asked questions about LITIENGINE and Java game development in general.
---

# Frequently Asked Questions

## LITIENGINE basics

### Is LITIENGINE a programming language or a library?

LITIENGINE is a 2D game library for Java. It is based on Java 8, but we plan to update to a later Java version soon.

### What's the current development status of LITIENGINE?

LITIENGINE is currently in Alpha. To find out what that means, please read our [Roadmap](../roadmap.md).

### Does LITIENGINE collect any user data?

LITIENGINE does not collect any user data via telemetry. However, if you register on our forum or subscribe to our newsletters, some of your information will be stored safely on our servers.  
We guarantee that your data is only used for the purposes you agreed with.

### What platforms can LITIENGINE deploy to?

With LITIENGINE, you can create games for Windows, Linux, and MacOS

### Whom is LITIENGINE made for?

LITIENGINE is made for anyone interested in creating 2D computer games with Java. Simple in nature, it is easy to pick up, yet powerful enough for creating massive worlds.

We think that if you are a relatively inexperienced Java developer seeking to create your first Java game, LITIENGINE might be the most hassle-free experience for you.

### Whom is LITIENGINE not made for?

If you are looking for a Java game engine able to deploy to mobile devices and browsers, LITIENGINE is unfortunately not your tool of choice.

Professional game developers experienced in using other engines might find LITIENGINE's capabilities a bit limiting, but we encourage you to request missing features [via GitHub issue](https://github.com/gurkenlabs/litiengine/issues).

### Since LITIENGINE is written in pure Java - what performance drawbacks can I expect?

LITIENGINE does not implement bindings for OpenGL or other graphics processing APIs. Hence, the CPU load is increased compared to other java game libraries, while the potential of GPU acceleration stays unexhausted. Most performance issues occur due to CPU-heavy computations \(e.g. updating too many particles or scaling lots of images at once\). Memory issues, on the other hand, occur rather rarely. While LITIENGINE per se runs on very low system specs, we have sometimes encountered poor performance when playing our previous games with older PCs, depending on the complexity of the game.

### Can I create LITIENGINE games without using the utiLITI editor?

Sure you can make a LITIENGINE game without using the editor. We've done that in the past and the editor is not a required piece in the development workflow. The main functionality of the utiLITI editor is to provide a convenient UI to position and configure [`Entities`](https://app.gitbook.com/@gurkenlabs/s/litiengine/~/drafts/-Lt4NljB3cbQX4NxqU4K/basics/entity-framework) in your maps and to ultimately provide a resource bundle for your game to simply load with a oneliner: e.g.[`Resources.load("game.litidata")`](https://www.javadoc.io/static/de.gurkenlabs/litiengine/0.4.20/de/gurkenlabs/litiengine/resources/Resources.html#load-java.net.URL-). Without such a resource bundle, you need to explicitly load all your resources from code using the [`Resources`](https://app.gitbook.com/@gurkenlabs/s/litiengine/~/drafts/-Lt4NljB3cbQX4NxqU4K/basics/resource-management) API.

Since the [`Entities`](https://app.gitbook.com/@gurkenlabs/s/litiengine/~/drafts/-Lt4NljB3cbQX4NxqU4K/basics/entity-framework) in the LITIENGINE can be loaded from [`MapObjects`](https://app.gitbook.com/@gurkenlabs/s/litiengine/~/drafts/-Lt4NljB3cbQX4NxqU4K/basics/manage-maps/map-objects), an alternative way to get things done is to directly add them in the _Tiled_ editor and provide the required [`MapObjectProperties`](https://www.javadoc.io/static/de.gurkenlabs/litiengine/0.4.20/de/gurkenlabs/litiengine/environment/tilemap/MapObjectProperty.html) if you want to use the engine's entity framework. This was, by the way, the workflow we went with before we had the editor. So you could say that the editor basically evolved from that. Everything that you see in the editor can also be done directly in code though, so if you want, you can totally skip the editor entirely, although it's not recommended.  
Btw: [`Entities`](https://app.gitbook.com/@gurkenlabs/s/litiengine/~/drafts/-Lt4NljB3cbQX4NxqU4K/basics/entity-framework)don't necessarily have to originate from [`MapObjects`](https://app.gitbook.com/@gurkenlabs/s/litiengine/~/drafts/-Lt4NljB3cbQX4NxqU4K/basics/manage-maps/map-objects), you can also add them to your [`GameWorld`](https://app.gitbook.com/@gurkenlabs/s/litiengine/~/drafts/-Lt4NljB3cbQX4NxqU4K/basics/game-api/game-world) directly from code.

## Distribution

### How do I create executables for a Java game?

See our [Deployment ](../basics/deployment.md)guide for LITIENGINE games.

