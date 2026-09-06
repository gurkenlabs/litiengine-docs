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

// Clamping values
int clamped = MathUtilities.clamp(value, 0, 100);

// Rounding
double rounded = MathUtilities.round(value, 2); // 2 decimal places

// Interpolation
double lerped = MathUtilities.lerp(start, end, 0.5);

// Check even/odd
boolean even = MathUtilities.isEven(number);
```

!!! note
    Use `Game.random()` for random numbers instead of MathUtilities.random methods.

## GeometricUtilities

Geometry operations:

```java
import de.gurkenlabs.litiengine.util.geom.GeometricUtilities;

// Distance between points
double dist = GeometricUtilities.distance(x1, y1, x2, y2);

// Angle between points
double angle = GeometricUtilities.calcAngle(p1, p2);

// Point rotation
Point2D rotated = GeometricUtilities.rotate(p, center, angle);

// Point in shape
boolean inside = GeometricUtilities.shapeContains(shape, point);
```

## Imaging

Image manipulation and raster processing:

```java
import de.gurkenlabs.litiengine.util.Imaging;

// Scale image
BufferedImage scaled = Imaging.scale(image, 2.0);

// Flip horizontally
BufferedImage flipped = Imaging.horizontalFlip(image);

// Set opacity (0.0f to 1.0f)
BufferedImage transparent = Imaging.setOpacity(image, 0.5f);
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

## TimeUtilities

Time formatting:

```java
import de.gurkenlabs.litiengine.util.TimeUtilities;

// Format milliseconds to readable time
String formatted = TimeUtilities.toReadableTime(125000); // "2:05"
```

## See Also

- [API Quick Reference](../getting-started/api-quick-reference.md) - Core engine method cheat sheet
