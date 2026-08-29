---
meta.description: "Overview of LITIENGINE utility classes for common operations like math, geometry, and collections."
meta.keywords: "LITIENGINE, utility, helper, math, geometry, collection, Java"
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
double rounded = MathUtilities.round(value, 2);  // 2 decimal places

// Interpolation
double lerped = MathUtilities.lerp(start, end, 0.5);

// Check even/odd
boolean even = MathUtilities.isEven(number);
```

> **Note:** Use `Game.random()` for random numbers instead of MathUtilities.random methods.

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

## ImagingUtilities

Image processing:

```java
import de.gurkenlabs.litiengine.util.ImagingUtilities;

// Scale image
BufferedImage scaled = ImagingUtilities.scale(image, 2.0f);

// Flip horizontally
BufferedImage flipped = ImagingUtilities.flipHorizontally(image);

// Set opacity
BufferedImage transparent = ImagingUtilities.setOpacity(image, 0.5f);
```

## ColorUtilities

Color operations:

```java
import de.gurkenlabs.litiengine.util.ColorUtilities;

// Parse hex color
Color color = ColorUtilities.decode("#FF5500");

// Color to hex
String hex = ColorUtilities.encode(color);

// Interpolate colors
Color blended = ColorUtilities.lerp(color1, color2, 0.5);
```

## TimeUtilities

Time formatting:

```java
import de.gurkenlabs.litiengine.util.TimeUtilities;

// Format milliseconds to readable time
String formatted = TimeUtilities.toReadableTime(125000);  // "2:05"
```

## See Also

- [API Reference](https://litiengine.com/api/) - Full Javadocs
