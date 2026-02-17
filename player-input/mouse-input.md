---
meta.description: "Learn how to handle mouse input in LITIENGINE using Input.mouse() for clicks, movement, and drag events."
meta.keywords: "LITIENGINE, mouse input, click, drag, mouse events, Java"
---

# Mouse Input

The `Input.mouse()` method provides access to the `IMouse` interface for handling mouse input in your game. This includes detecting button presses, tracking mouse position, and responding to mouse events.

## Basic Usage

### Getting Mouse Location

```java
// Get current mouse location (window coordinates)
Point2D location = Input.mouse().getLocation();
double x = location.getX();
double y = location.getY();
```

> **Note:** The coordinates are relative to the game window, not the game world. To get world coordinates, account for camera position.

### Checking Button State

```java
// Check if any mouse button is pressed
if (Input.mouse().isPressed()) {
  // Mouse button is currently pressed
}

// Check specific buttons
if (Input.mouse().isLeftMouseButtonDown()) {
  // Left mouse button is pressed
}

if (Input.mouse().isRightMouseButtonDown()) {
  // Right mouse button is pressed
}
```

## Event Listeners

Register listeners to respond to mouse events:

### Click Events

```java
Input.mouse().onClicked(e -> {
  System.out.println("Mouse clicked at: " + e.getX() + ", " + e.getY());
});
```

### Press and Release Events

```java
// When mouse button is pressed down
Input.mouse().onPressed(e -> {
  System.out.println("Mouse pressed: " + e.getButton());
});

// When mouse button is released
Input.mouse().onReleased(e -> {
  System.out.println("Mouse released: " + e.getButton());
});

// Continuously while mouse is pressed
Input.mouse().onPressing(e -> {
  // Handle dragging operations
});
```

### Movement Events

```java
// When mouse moves
Input.mouse().onMoved(e -> {
  Point2D location = Input.mouse().getLocation();
  // Update cursor effects, hover states, etc.
});

// When mouse is dragged (moved while button pressed)
Input.mouse().onDragged(e -> {
  // Handle drag operations
});
```

## Common Patterns

### World Coordinate Conversion

Convert screen coordinates to game world coordinates:

```java
Input.mouse().onClicked(e -> {
  // Get screen position
  Point2D screenPos = Input.mouse().getLocation();
  
  // Convert to world position (account for camera)
  Point2D worldPos = Game.world().camera().getMapLocation(screenPos);
  
  // Now you can use worldPos for game logic
});
```

### Entity Selection

```java
Input.mouse().onClicked(e -> {
  Point2D mousePos = Input.mouse().getLocation();
  Point2D worldPos = Game.world().camera().getMapLocation(mousePos);
  
  // Check if clicked on any entity
  for (IEntity entity : Game.world().environment().getEntities()) {
    if (entity.getBoundingBox().contains(worldPos)) {
      System.out.println("Clicked on: " + entity.getName());
      break;
    }
  }
});
```

### Click-to-Move

```java
Input.mouse().onClicked(e -> {
  Point2D worldPos = Game.world().camera().getMapLocation(
    Input.mouse().getLocation()
  );
  
  // Move player to clicked location
  Player player = Player.instance();
  Game.physics().move(player, player.getAngleTo(worldPos), player.getVelocity());
});
```

## Mouse Wheel

Handle mouse wheel events for zooming or scrolling:

```java
Game.window().getRenderComponent().addMouseWheelListener(e -> {
  int rotation = e.getWheelRotation();
  if (rotation < 0) {
    // Scroll up / zoom in
  } else {
    // Scroll down / zoom out
  }
});
```

## Utility Methods

```java
// Check if event was left button
if (Input.mouse().isLeftButton(event)) {
  // ...
}

// Check if event was right button  
if (Input.mouse().isRightButton(event)) {
  // ...
}

// Set mouse location programmatically
Input.mouse().setLocation(100, 100);
```

## See Also

- [Keyboard Input](/docs/player-input/keyboard-input/) - Keyboard handling
- [Gamepad Input](/docs/player-input/gamepad-input/) - Gamepad handling
- [Player Input Overview](/docs/player-input/README/) - Input API overview
