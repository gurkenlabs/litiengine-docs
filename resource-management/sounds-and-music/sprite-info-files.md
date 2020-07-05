---
description: A method of batch importing spritesheets.
---

# Sprite Info Files

If you want to import many Spritesheets at once, you can use the Spritesheet batch import feature using so-called _sprite info files._ A _sprite info file_ is a plain text file located in one of your project's resource folders. Each line contains a Spritesheet to import, file names and frame dimensions, as well as animation keyframe durations, if you want to override the default. Comments are supported following the '\#' character.

{% hint style="warning" %}
The entries need to comply with this schema:

{FILENAME}.{EXTENSTION},{FRAME-WIDTH},{FRAME-HEIGHT}\(;{KEYFRAME\_DURATIONS}\)

where

* {FILENAME} is the file name
* {EXTENSTION} is the file extension
* {FRAME-WIDTH} is the width of each frame in the Spritesheet
* {FRAME-HEIGHT} is the height of each frame in the Spritesheet
* {KEYFRAME\_DURATIONS} is a comma-separated list of custom keyframe durations in milliseconds. This part, as well as the semicolon before it, is optional.
{% endhint %}

See an example sprite info file below:

```text
#mobs
gnome1_walk.png,16,16
gnome1-dead.png,16,13
civilian1-walk.png,16,32
civilian2-walk.png,16,32
civilian3-walk.png,16,32


#clown
clown-walk-down.png,18,34
clown-walk-up.png,18,34
clown-cakethrow-preparation-down.png,20,34
clown-cakethrow-preparation-up.png,20,34
clown-victory.png,18,45;200,120,200,200,200,120,120,300,120,4000,200,200

#props
prop-tent1-intact.png,83,60
prop-car1-intact.png,43,20
prop-car2-intact.png,43,20
prop-bookshelf1-intact.png,32,16
prop-bed1-intact.png,16,8

#misc
arrow-throw.png,8,8
arrow-throw-red.png,8,8
projectile-cake.png,8,6
nose.png,5,9
```

Load all Spritesheets declared in a sprite info file into your game as follows:

```text
List<Spritesheet> loaded = Resources.spritesheets().loadFrom("sprites.info");
```

