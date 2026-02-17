---
meta.description: "Learn how to handle gamepad input in LITIENGINE using Input.gamepadManager() with Input4j for cross-platform controller support."
meta.keywords: "LITIENGINE, gamepad, controller, Input4j, Xbox, button, axis, Java"
---

# Gamepad Input

LITIENGINE uses [Input4j](https://github.com/gurkenlabs/input4j) for gamepad support, utilizing the Java FFM API for cross-platform compatibility. This eliminates the need for native library deployment.

> **Note:** As of LITIENGINE 0.11.1, gamepad support uses Input4j instead of JInput. No native libraries are required.

## Accessing Gamepads

```java
// Get the gamepad manager
GamepadManager manager = Input.gamepadManager();

// Get all connected gamepads
List<Gamepad> gamepads = Input.gamepads().getAll();

// Get the first connected gamepad
Gamepad gamepad = Input.gamepads().getCurrent();
```

## Button Events

### Handling Button Presses

```java
// Using button-specific listener
Input.gamepadManager().onPressed(Gamepad.Xbox.A, value -> {
  System.out.println("A button pressed!");
});

// Using generic button listener
Input.gamepadManager().onPressed((button, value) -> {
  if (button.equals(Gamepad.Xbox.A)) {
    System.out.println("A PRESSED");
  } else if (button.equals(Gamepad.Xbox.B)) {
    System.out.println("B PRESSED");
  }
});
```

### Button Release Events

```java
Input.gamepadManager().onReleased((button, value) -> {
  if (button.equals(Gamepad.Xbox.START)) {
    // Pause game
  }
});
```

## Xbox Controller Buttons

The `Gamepad.Xbox` class provides constants for standard Xbox controller buttons:

| Button | Description |
|--------|-------------|
| `A` | A button (bottom) |
| `B` | B button (right) |
| `X` | X button (left) |
| `Y` | Y button (top) |
| `LB` | Left bumper |
| `RB` | Right bumper |
| `LT` | Left trigger |
| `RT` | Right trigger |
| `START` | Start button |
| `BACK` | Back/Select button |
| `LEFT_STICK` | Left stick press |
| `RIGHT_STICK` | Right stick press |
| `DPAD_UP` | D-Pad up |
| `DPAD_DOWN` | D-Pad down |
| `DPAD_LEFT` | D-Pad left |
| `DPAD_RIGHT` | D-Pad right |

## Analog Sticks

Read analog values from thumbsticks:

```java
Input.gamepadManager().onPressed(Gamepad.Xbox.LEFT_STICK_Y, pollValue -> {
  if (pollValue > 0.5) {
    System.out.println("MOVE UP");
  } else if (pollValue < -0.5) {
    System.out.println("MOVE DOWN");
  }
});

Input.gamepadManager().onPressed(Gamepad.Xbox.LEFT_STICK_X, pollValue -> {
  if (pollValue > 0.5) {
    System.out.println("MOVE RIGHT");
  } else if (pollValue < -0.5) {
    System.out.println("MOVE LEFT");
  }
});
```

## Polling Current State

Check gamepad state directly without event listeners:

```java
Gamepad gamepad = Input.gamepads().getCurrent();
if (gamepad != null) {
  // Get button state
  if (gamepad.isPressed(Gamepad.Xbox.A)) {
    // A button is pressed
  }
  
  // Get axis value (-1.0 to 1.0)
  float x = gamepad.getPollValue(Gamepad.Xbox.LEFT_STICK_X);
  float y = gamepad.getPollValue(Gamepad.Xbox.LEFT_STICK_Y);
}
```

## Gamepad Connection Events

```java
// When a gamepad is connected
Input.gamepadManager().onAdded(gamepad -> {
  System.out.println("Gamepad connected: " + gamepad.getName());
});

// When a gamepad is disconnected
Input.gamepadManager().onRemoved(gamepad -> {
  System.out.println("Gamepad disconnected");
});
```

## GamepadEntityController

Control entities with gamepad input:

```java
public class GamepadEntityController<T extends IMobileEntity> extends MovementController<T> {
  
  public GamepadEntityController(T entity) {
    super(entity);
    Input.gamepadManager().onPressed(Gamepad.Xbox.LEFT_STICK_X, x -> {
      this.setDx((float) x);
    });
    Input.gamepadManager().onPressed(Gamepad.Xbox.LEFT_STICK_Y, y -> {
      this.setDy((float) y);
    });
  }
}
```

## Dead Zones

Handle stick dead zones to prevent drift:

```java
private static final float DEAD_ZONE = 0.2f;

private float applyDeadZone(float value) {
  if (Math.abs(value) < DEAD_ZONE) {
    return 0;
  }
  return value;
}

// Usage
Input.gamepadManager().onPressed(Gamepad.Xbox.LEFT_STICK_X, x -> {
  float adjustedX = applyDeadZone((float) x);
  if (adjustedX != 0) {
    controller.setDx(adjustedX);
  }
});
```

## See Also

- [Keyboard Input](/docs/player-input/keyboard-input/) - Keyboard handling
- [Mouse Input](/docs/player-input/mouse-input/) - Mouse handling
- [Player Input Overview](/docs/player-input/README/) - Input API overview
