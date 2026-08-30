---
title: "Gamepad Input"
icon: "lucide/gamepad-2"
description: "Learn how to handle gamepad input in LITIENGINE using Input.gamepads() with Input4j for cross-platform controller support."
keywords: ["LITIENGINE", "gamepad", "controller", "Input4j", "Xbox", "button", "axis", "Java"]
tags: ["gamepad", "controller", "joystick", "input4j", "panama ffm", "buttons"]
---

# Gamepad Input

## Gamepad API Method Reference

| Method Signature | Return Type | Description |
| :--- | :--- | :--- |
| `Input.gamepads().current()` | `Gamepad` | Returns the currently active primary gamepad controller. |
| `Input.gamepads().getAll()` | `List<Gamepad>` | Returns a list of all detected, connected gamepad devices. |
| `Input.gamepads().onAdded(Consumer<Gamepad> c)` | `void` | Registers a listener invoked when a controller is plugged in. |
| `Input.gamepads().onRemoved(Consumer<Gamepad> c)` | `void` | Registers a listener invoked when a controller is disconnected. |
| `gamepad.getAxis(String axis)` | `float` | Reads analog stick/trigger value between `-1.0` and `1.0`. |
| `gamepad.isPressed(String button)` | `boolean` | Checks if a digital button (e.g. `Gamepad.Buttons.A`) is held down. |
| `gamepad.onPressed(String button, Consumer c)` | `void` | Registers a listener triggered when a button is first pressed. |

---

LITIENGINE uses [Input4j](https://github.com/gurkenlabs/input4j) for gamepad support, utilizing the Java FFM API for cross-platform compatibility. This eliminates the need for native library deployment.

!!! note
    As of LITIENGINE 0.11.1, gamepad support uses Input4j instead of JInput. No native libraries are required.

## Accessing Gamepads

```java
// Get the gamepad manager
GamepadManager manager = Input.gamepads();

// Get all connected gamepads
List<Gamepad> gamepads = Input.gamepads().getAll();

// Get the first connected gamepad
Gamepad gamepad = Input.gamepads().getCurrent();
```

## Button Events

### Handling Button Presses

```java
// Using button-specific listener
Input.gamepads().onPressed(Gamepad.Xbox.A, value -> {
  System.out.println("A button pressed!");
});

// Using generic button listener
Input.gamepads().onPressed((button, value) -> {
  if (button.equals(Gamepad.Xbox.A)) {
    System.out.println("A PRESSED");
  } else if (button.equals(Gamepad.Xbox.B)) {
    System.out.println("B PRESSED");
  }
});
```

### Button Release Events

```java
Input.gamepads().onReleased((button, value) -> {
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
Input.gamepads().onPressed(Gamepad.Xbox.LEFT_STICK_Y, pollValue -> {
  if (pollValue > 0.5) {
    System.out.println("MOVE UP");
  } else if (pollValue < -0.5) {
    System.out.println("MOVE DOWN");
  }
});

Input.gamepads().onPressed(Gamepad.Xbox.LEFT_STICK_X, pollValue -> {
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
Input.gamepads().onAdded(gamepad -> {
  System.out.println("Gamepad connected: " + gamepad.getName());
});

// When a gamepad is disconnected
Input.gamepads().onRemoved(gamepad -> {
  System.out.println("Gamepad disconnected");
});
```

## GamepadEntityController

Control entities with gamepad input:

```java
public class GamepadEntityController<T extends IMobileEntity> extends MovementController<T> {

  public GamepadEntityController(T entity) {
    super(entity);
    Input.gamepads().onPressed(Gamepad.Xbox.LEFT_STICK_X, x -> {
      this.setDx((float) x);
    });
    Input.gamepads().onPressed(Gamepad.Xbox.LEFT_STICK_Y, y -> {
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
Input.gamepads().onPressed(Gamepad.Xbox.LEFT_STICK_X, x -> {
  float adjustedX = applyDeadZone((float) x);
  if (adjustedX != 0) {
    controller.setDx(adjustedX);
  }
});
```

## See Also

- [Keyboard Input](/player-input/keyboard-input/) - Keyboard handling
- [Mouse Input](/player-input/mouse-input/) - Mouse handling
- [Player Input Overview](/player-input/) - Input API overview

!!! important "Panama FFM Foreign Memory"
    LITIENGINE uses `Input4j` via Java Panama Foreign Function & Memory (FFM) APIs. Run your JVM on Java 21 or later to enable native controller polling without JNI overhead.
