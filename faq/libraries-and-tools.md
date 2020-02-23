---
description: >-
  This section contains useful information for external libraries and tools
  related to LITIengine Game Development.
---

# Libraries and Tools

## 3rd-Party Libraries

There is only a bare minimum of third party libraries included in the LITIengine, which we want to mention here thankfully:

* [JInput](https://github.com/jinput/jinput) for Gamepad support
* [MP3 SPI](http://www.javazoom.net/mp3spi/mp3spi.html) for .mp3 audio file support
* [Ogg Vorbis SPI](http://www.javazoom.net/vorbisspi/vorbisspi.html) for .ogg audio file support
* [Steamworks4j](https://github.com/code-disaster/steamworks4j) for supporting the steamworks SDK

## Steamworks

### How to use steamworks4j SteamAPI from Eclipse?

LITIengine uses the **steamworks4j** wrapper for the SteamAPI to grant access to Steam features from java. When developing a game that uses these features, you need to execute a few extra steps in order to support the functionality from the IDE.

1. You need to have created the game on [Steamworks](https://partner.steamgames.com) in order to have an _appID_
2. Create an `steam_appid.txt` file containing only the _appID_ of your game
3. Copy the `steam_appid.txt` to the _working directory_ of your app.

   > For debugging and running your app from Eclipse \(or other IDEs\), the application will be run, using the `javaw.exe`. Your _working directory_ will typically be something like _C:\Program Files\Java\jdkX.X.X\_XXX\bin_, which is where your `javaw.exe` is located. This, of course, depends on your environment \(workspace/project\) _Java Build Path_ configuration of the editor

4. From here on, you can just follow the original tutorial [here](http://code-disaster.github.io/steamworks4j/getting-started.html#initialization).

## Tiled Map Editor

### What is '_Tiled_'?

From the official [Tiled docs page](https://doc.mapeditor.org/en/stable/manual/introduction/):

> Tiled is a 2D level editor that helps you develop the content of your game. Its primary feature is to edit tile maps of various forms, but it also supports free image placement as well as powerful ways to annotate your level with extra information used by the game. Tiled focuses on general flexibility while trying to stay intuitive.

With Tiled editor, you can create orthogonal, hexagonal, and isometric Tile maps in no time. It is the absolute go-to tool for 2D Tile-based mapping.

#### How do I use Tiled?

For a general understanding of the mapping process with Tiled editor, we encourage you to have a look at its [plentiful documentation](https://doc.mapeditor.org/en/stable/manual/introduction/#creating-a-new-map). However, we will refer to a few LITIengine specific aspects of creating maps with Tiled in the sections about [Map Objects](https://docs.litiengine.com/basics/manage-maps/map-objects) and [custom properties](https://docs.litiengine.com/basics/manage-maps/custom-properties)

#### Why is tile mapping not a part of the utiLITI editor?

LITIengine had its origin in the idea of writing a Java 2D game engine without including _any_ external libraries \(what were we _thinking_?\). Yet, we believe that it is key to success to be able to sometimes rely on other people's expertise, especially when having limited resources. The Tiled editor has been developed by a vivid community for approximately ten years, offering a universal standard for tile maps. In other words, _it just works_. There is simply no need to reinvent the wheel when it comes to tile mapping.

