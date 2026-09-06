---
title: Keyboard Input
icon: lucide/keyboard
description: Keyboard Input documentation for LITIENGINE 2D Java game development.
keywords: [LITIENGINE, java, 2d, game engine, player input]
tags: [keyboard, keys, wasd, key-bindings, input]
---
# Keyboard Input

## Keyboard API Method Reference

| Method Signature | Return Type | Description |
| :--- | :--- | :--- |
| `isPressed(int keyCode)` | `boolean` | Returns `true` if the key is currently held down. |
| `onKeyPressed(int keyCode, Consumer<KeyEvent> consumer)` | `void` | Registers a listener invoked once when the key is first pressed. |
| `onKeyReleased(int keyCode, Consumer<KeyEvent> consumer)` | `void` | Registers a listener invoked when the key is released. |
| `onKeyTyped(int keyCode, Consumer<KeyEvent> consumer)` | `void` | Registers a listener invoked when a character key is typed. |
| `consumeKeyEvent(KeyEvent event)` | `void` | Consumes the event so subsequent listeners do not process it. |

---

## Listening for Key Events

The `Input.keyboard()` manager allows you to register global listeners for key press, release, and typing events:

```java
import de.gurkenlabs.litiengine.input.Input;
import java.awt.event.KeyEvent;

// Listen for a specific key press
Input.keyboard().onKeyPressed(KeyEvent.VK_SPACE, event -> {
  System.out.println("Jump action triggered!");
});

// Listen for all key press events
Input.keyboard().onKeyPressed(event -> {
  if (event.getKeyCode() == KeyEvent.VK_ESCAPE) {
    Game.screens().display("PAUSE_MENU");
  }
});

// Listen for key release
Input.keyboard().onKeyReleased(KeyEvent.VK_SHIFT, event -> {
  System.out.println("Sprint released!");
});
```

---

## Polling Key State

You can query whether specific keys are currently pressed during the game loop or within entity update callbacks:

```java
// Check if a key is held down
if (Input.keyboard().isPressed(KeyEvent.VK_W)) {
  // Move up or accelerate
}

// Check multiple keys
boolean isSprinting = Input.keyboard().isPressed(KeyEvent.VK_SHIFT);
```

---

## Entity Movement with `KeyboardEntityController`

LITIENGINE includes a built-in `KeyboardEntityController` that binds directional keyboard input to any `IMobileEntity` (`Creature`, `Player`):

### Basic Setup

```java
Player player = new Player();

// Create keyboard movement controller (defaults to Arrow keys: UP, DOWN, LEFT, RIGHT)
KeyboardEntityController<Player> controller = new KeyboardEntityController<>(player);

// Attach the controller to the player entity
player.controllers().add(controller);
```

### Adding Alternative Bindings (WASD + Arrow Keys)

You can customize directional keys or bind multiple keys to the same direction:

```java
KeyboardEntityController<Player> controller = new KeyboardEntityController<>(player);

// Add WASD keys in addition to default arrow keys
controller.addUpKey(KeyEvent.VK_W);
controller.addDownKey(KeyEvent.VK_S);
controller.addLeftKey(KeyEvent.VK_A);
controller.addRightKey(KeyEvent.VK_D);

// Or replace key bindings completely
controller.setUpKeys(KeyEvent.VK_W);
controller.setDownKeys(KeyEvent.VK_S);
controller.setLeftKeys(KeyEvent.VK_A);
controller.setRightKeys(KeyEvent.VK_D);
```

---

## Consuming Key Events

When handling UI inputs (e.g. typing into text fields or navigating modal menus), consume events so that gameplay controllers do not process them simultaneously:

```java
Input.keyboard().onKeyPressed(event -> {
  if (isMenuOpen && event.getKeyCode() == KeyEvent.VK_ENTER) {
    selectMenuItem();
    Input.keyboard().consumeKeyEvent(event);
  }
});
```

---

## See Also

* **[Mouse Input](mouse-input.md)** - Mouse movement, clicks, and coordinate conversion
* **[Gamepad Input](gamepad-input.md)** - Controller support via Input4j
* **[Movement Controller](../control-entities/movement-controller.md)** - Custom entity physics and movement
* **[Entity Controllers](../control-entities/entity-controllers.md)** - Entity controller pipeline
