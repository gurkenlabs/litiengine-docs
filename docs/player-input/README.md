---
title: "Player Input"
icon: "lucide/gamepad-2"
description: "Master LITIENGINE player input handling: Keyboard, Mouse, Gamepad (via Input4j and Java FFM), and custom Input Controllers."
keywords: ["LITIENGINE input", "keyboard", "mouse", "gamepad", "Input4j", "Java FFM", "Input.keyboard", "Input.mouse", "Input.gamepads"]
tags: ["input", "keyboard", "mouse", "gamepad", "controllers"]
---

# Player Input

LITIENGINE provides a unified, responsive input subsystem accessible globally via the static `Input` class. It manages keyboard key states, mouse position and dragging, gamepad axis polling (via `Input4j`), and customizable entity input controllers.

---

## Input Documentation Sections

<div class="grid cards" markdown>

- :material-keyboard-outline:{ .lg .middle } **[Keyboard Input](keyboard-input.md)**

    ---

    Key event listeners, keybinding registration, typed characters, and pressed state polling.

- :material-mouse-outline:{ .lg .middle } **[Mouse Input](mouse-input.md)**

    ---

    Mouse coordinates, screen-to-world coordinate transformations, drag events, and button clicks.

- :material-controller:{ .lg .middle } **[Gamepad Input](gamepad-input.md)**

    ---

    DirectInput, XInput, and multi-controller polling via Input4j and Java Panama Foreign Function & Memory APIs.

- :material-tune:{ .lg .middle } **[Movement Controllers](../control-entities/movement-controller.md)**

    ---

    Attaching 8-directional movement, platformer gravity, and custom keybinding controllers to entities.

</div>
