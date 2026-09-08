---
title: Utility Classes
icon: lucide/wrench
description: Overview of LITIENGINE utility classes for common operations like math,
  geometry, and collections.
keywords: [LITIENGINE, utility, helper, math, geometry, collection, Java]
tags: [utilities, math, geometry, helpers, reflection, files]
---
# Utility Classes

LITIENGINE provides utility classes for common operations. These static helpers simplify repetitive tasks.

## MathUtilities

Mathematical operations:

```java
import de.gurkenlabs.litiengine.util.MathUtilities;

// Rounding numbers
double rounded = MathUtilities.round(3.14159, 2); // 3.14
float roundedFloat = MathUtilities.round(3.14159f, 2);

// Check if a number is odd
boolean odd = MathUtilities.isOddNumber(7); // true

// Calculate percentage and average
int percent = MathUtilities.getFullPercent(25.0, 100.0); // 25
double avg = MathUtilities.getAverage(new double[] { 10.0, 20.0, 30.0 }); // 20.0

// Clamping values (standard Java 21+)
int clamped = Math.clamp(value, 0, 100);
```

!!! note
    Use `Game.random()` for game-specific random sampling and `Math.clamp()` for clamping numeric bounds.

## GeometricUtilities

Geometry operations:

```java
import de.gurkenlabs.litiengine.util.geom.GeometricUtilities;
import java.awt.geom.Point2D;
import java.awt.geom.Rectangle2D;

// Distance between coordinates or points
double dist = GeometricUtilities.distance(x1, y1, x2, y2);
double pDist = GeometricUtilities.distance(p1, p2);

// Rotation angle from center to target point in degrees
double angle = GeometricUtilities.calcRotationAngleInDegrees(centerPt, targetPt);

// Project a point along an angle by a given delta distance
Point2D projected = GeometricUtilities.project(start, angle, 50.0);

// Point in rectangle bounds
boolean inside = GeometricUtilities.contains(rect, point);

// Check intersection between shapes or rectangles
boolean hit = GeometricUtilities.intersects(rectA, rectB);
```

## Imaging

Image manipulation and raster processing:

```java
import de.gurkenlabs.litiengine.util.Imaging;
import java.awt.image.BufferedImage;

// Scale image
BufferedImage scaled = Imaging.scale(image, 2.0);

// Flip horizontally or vertically
BufferedImage flipped = Imaging.horizontalFlip(image);
BufferedImage vFlipped = Imaging.verticalFlip(image);

// Set opacity / alpha (0.0f to 1.0f)
BufferedImage transparent = Imaging.setAlpha(image, 0.5f);
```

## ColorHelper

Color encoding, decoding, and blending utilities:

```java
import de.gurkenlabs.litiengine.util.ColorHelper;

// Parse hex color string (#RRGGBB or #AARRGGBB)
Color color = ColorHelper.decode("#FF5500");

// Color to hex string
String hex = ColorHelper.encode(color);

// Blend / interpolate between two colors
Color blended = ColorHelper.interpolate(color1, color2, 0.5);

// Premultiply alpha
Color premultiplied = ColorHelper.premultiply(color);
```

## Vector2D

`Vector2D` (`de.gurkenlabs.litiengine.util.geom.Vector2D`) provides 2D Euclidean vector mathematics for velocity calculations, knockbacks, raycasting directions, and angles:

```java
import de.gurkenlabs.litiengine.util.geom.Vector2D;
import java.awt.geom.Point2D;

// Create vectors
Vector2D v1 = new Vector2D(10.0, 5.0);
Vector2D v2 = new Vector2D(new Point2D.Double(0, 0), new Point2D.Double(3, 4));

// Vector arithmetic
Vector2D sum = v1.add(v2);
Vector2D diff = v1.sub(v2);
Vector2D scaled = v1.scale(2.5);

// Linear algebra
double length = v2.length();           // 5.0
Vector2D unit = v2.unitVector();       // Direction vector normalized to length 1.0
Vector2D normal = v2.normalVector();   // Perpendicular normal vector (90 deg clockwise)
double dot = v1.dotProduct(v2);        // Dot product
```

---

## GameRandom

`Game.random()` returns an enhanced `GameRandom` instance (`de.gurkenlabs.litiengine.GameRandom`) with game-specific sampling, geometry positioning, and shuffling:

```java
import de.gurkenlabs.litiengine.Game;
import java.awt.Color;
import java.awt.geom.Ellipse2D;
import java.awt.geom.Point2D;
import java.util.List;

// 1. Array & collection selection
String[] lootTable = {"Potion", "Gold", "Sword", "Shield"};
String randomDrop = Game.random().choose(lootTable);

// 2. Sampling with or without replacement
List<String> deck = List.of("Card A", "Card B", "Card C", "Card D", "Card E");
List<String> hand = (List<String>) Game.random().sample(deck, 3, false); // No duplicates!

// 3. Geometry & world location sampling
Point2D mapPoint = Game.random().getLocation(Game.world().environment().getMap());
Point2D circlePoint = Game.random().getLocation(new Ellipse2D.Double(100, 100, 50, 50));

// 4. Color variance and randomization
Color base = new Color(180, 50, 50);
Color tinted = Game.random().nextColor(base, 0.2f, 0.0f); // Randomized RGB variance

// 5. Algebraic sign shuffling
int direction = Game.random().nextSign(); // 1 or -1
```

---

## GameTime

`Game.time()` provides `GameTime` (`de.gurkenlabs.litiengine.GameTime`) for tracking ticks, delta timestamps, and game/environment lifetimes:

```java
import de.gurkenlabs.litiengine.Game;

// Current tick count in the game loop
long currentTick = Game.time().now();

// Elapsed milliseconds since a past event/tick
long elapsedMs = Game.time().since(lastCastTick);

// Lifetime tracking
long sessionDurationMs = Game.time().sinceGameStart();
long levelDurationMs = Game.time().sinceEnvironmentLoad();

// Tick <-> Millisecond conversions
long ticksForTwoSeconds = Game.time().toTicks(2000);
long msFromTicks = Game.time().toMilliseconds(120);
```

---

## CommandManager

`CommandManager` (`de.gurkenlabs.litiengine.util.CommandManager`) provides an extensible console command interface powered by Java virtual threads, listening to `System.in`:

```java
import de.gurkenlabs.litiengine.Game;
import de.gurkenlabs.litiengine.util.CommandManager;

CommandManager commands = new CommandManager();

// Bind a console command
commands.bind("heal", args -> {
  if (args.length > 1) {
    int amount = Integer.parseInt(args[1]);
    System.out.println("Healing player for: " + amount);
    return true;
  }
  return false;
});

// Start listening for terminal inputs in the background
commands.start();

// Or execute programmatically
commands.executeCommand("heal 50");
```

---

## Aseprite Format Support

`AsepriteFormat` (`de.gurkenlabs.litiengine.resources.AsepriteFormat`) reads JSON sprite sheet metadata exported by the [Aseprite](https://www.aseprite.org) CLI (supporting both hash and array frame layouts):

```java
import de.gurkenlabs.litiengine.resources.AsepriteFormat;
import java.nio.file.Path;

// Load Aseprite JSON metadata exported alongside the spritesheet PNG
AsepriteFormat format = AsepriteFormat.read(Path.of("sprites/character.json"));

for (AsepriteFormat.Frame frame : format.getFrames()) {
  System.out.println("Frame: " + frame.getName()
    + " [" + frame.getX() + ", " + frame.getY()
    + " " + frame.getWidth() + "x" + frame.getHeight() + "]"
    + " duration: " + frame.getDuration() + "ms");
}
```

---

## Blueprints & Templates

`Blueprints` (`de.gurkenlabs.litiengine.resources.Blueprints`) manages prefabricated map object templates (`.tx` Tiled object templates and `.xtx` multi-object blueprints):

```java
import de.gurkenlabs.litiengine.Game;
import de.gurkenlabs.litiengine.environment.tilemap.IMapObject;
import de.gurkenlabs.litiengine.environment.tilemap.xml.Blueprint;
import de.gurkenlabs.litiengine.resources.Resources;
import java.util.List;

// Load blueprint from game resources
Blueprint houseTemplate = Resources.blueprints().get("house.xtx");

// Instantiate all objects from the blueprint at map coordinates (200, 350)
List<IMapObject> spawnedObjects = houseTemplate.build(200f, 350f);

// Add spawned objects to the active environment
for (IMapObject obj : spawnedObjects) {
  Game.world().environment().load(obj);
}
```

---

## TimeUtilities

Time formatting:

```java
import de.gurkenlabs.litiengine.util.TimeUtilities;
import de.gurkenlabs.litiengine.util.TimeUtilities.TimerFormat;

// Format milliseconds using standard TimerFormat
String mmss = TimeUtilities.toTimerFormat(125000, TimerFormat.MM_SS_0);    // "02:05.0"
String precise = TimeUtilities.toTimerFormat(125000, TimerFormat.MM_SS_000); // "02:05.000"
String hhmmss = TimeUtilities.toTimerFormat(3665000, TimerFormat.HH_MM_SS); // "01:01:05"

// Extract components
long minutes = TimeUtilities.getMinutes(125000); // 2
long seconds = TimeUtilities.getRemainingSeconds(125000); // 5
```

---

## See Also

<div class="grid cards" markdown>

- :lucide-book-open:{ .lg .middle } **[API Quick Reference](../getting-started/api-quick-reference.md)**

    ---

    Core engine method cheat sheet and quick syntax reference.

- :lucide-settings:{ .lg .middle } **[Game Configuration](../configuration/README.md)**

    ---

    Engine configuration groups, graphics pipelines, and debugging flags.

</div>

