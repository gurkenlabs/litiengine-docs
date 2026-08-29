---
title: "Player Input"
description: "Player Input documentation for LITIENGINE 2D Java game development."
keywords: ["LITIENGINE", "java", "2d", "game engine", "player input"]
---

# Player Input

![Input API](../images/api-input.png)

Example snippet:

```java
if (Input.mouse().isPressed() && Input.mouse().isLeftMouseButtonDown()) {
  // do something when the left mouse button is pressed
}

Input.keyboard().onKeyReleased(KeyEvent.VK_ENTER, key -> {
 // do something when "enter" is released
});

Input.keyboard().onKeyPressed(event -> {
  if (event.getKeyCode() == KeyEvent.VK_BACK_SPACE) {
    // do something when "backspace" is pressed
  }
});

Input.gamepads().onPressed(Gamepad.Xbox.LEFT_STICK_Y, pollValue -> {
  if (pollValue > 0) {
    System.out.println("MOVE DOWN");
  } else if (pollValue < 0) {
    System.out.println("MOVE UP");
  }
});

Input.gamepads().onPressed((button, value) -> {
  // for simple buttons, the value doesn't really matter -> no need to check against it
  if (button.equals(Gamepad.Xbox.A)) {
    System.out.println("A PRESSED");
  } else if (button.equals(Gamepad.Xbox.B)) {
    System.out.println("B PRESSED");
  }
});
```

## Temporarily Locking Input (Dialogues & Cutscenes)

When entering cutscenes, modal dialogues, or pause menus, you can temporarily disable device polling without unregistering individual listeners:

```java
// 1. Lock all player input
Input.keyboard().stop();
Input.mouse().stop();
if (Input.gamepads() != null) {
  Input.gamepads().current().stop();
}

// 2. Resume player input when cutscene or dialogue finishes
Input.keyboard().start();
Input.mouse().start();
if (Input.gamepads() != null) {
  Input.gamepads().current().start();
}
```

!!! tip "Screen-Level Input Routing"
    Alternatively, using `ScreenManager` and modal `Screen` implementations will automatically isolate GUI component input events from gameplay entity controllers.
