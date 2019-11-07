# Introduction

The **LITIengine** is a free, open source and easy to learn **2D Java Game Engine**. It provides the infrastructure to create a 2D tile-based Java Game, be it a platformer, a top-down shooter or an RPG. The main features include a **2D Physics Engine**, a **2D Render Engine**, a **2D Sound Engine**, a **Particle System**, support for **Tiled Maps \(.tmx\)** and a clean API for the **Basic Game Infrastructure**. LITIengine is invented, written and maintained by the two bavarian brothers **Steffen and Matthias** and it has become a [considerably popular open source project](https://github.com/gurkenlabs/litiengine) with a rising number of contributors and an active [Community](https://forum.litiengine.com/).

One major difference to other engines is that the **2D Render Engine** is entirely based on plain **Java AWT Graphics**. If you've learned or starting to learn Java this will instantly give you great results and highly optimized rendering performance with what you already know. We think that this is a great and simple way to start making video games without having to care about a lot of vector math or "OpenGL shenanigans". The graphics can then be further enhanced by the **Particle System** to create beautiful visual effects \(like fire or smoke\). There is only a bare minimum of third party libraries included in LITIengine, which we want to mention here thankfully:

* [JInput](https://github.com/jinput/jinput) for Gamepad support
* [MP3 SPI](http://www.javazoom.net/mp3spi/mp3spi.html) for .mp3 audio file support
* [Ogg Vorbis SPI](http://www.javazoom.net/vorbisspi/vorbisspi.html) for .ogg audio file support
* [Steamworks4j](https://github.com/code-disaster/steamworks4j) for supporting the steamworks SDK

The `Environments` in the LITIengine are based on `.tmx` tile maps which can be created and edited with the well known [Tiled Level Editor](https://www.mapeditor.org/) and brought to life with LITIengine entities.

Moreover, the `SoundEngine` supports **two dimensional audio** that can be played relatively to a position in the environment.

