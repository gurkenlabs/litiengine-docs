---
title: Player Input
icon: lucide/gamepad
description: Handle low-latency keyboard, mouse, and gamepad controls in LITIENGINE
  with Panama FFM integration.
keywords: [LITIENGINE, input, keyboard, mouse, gamepad, input4j, panama ffm]
tags: [input, player-input, controls, event-listeners]
---
# Player Input

LITIENGINE provides a unified, low-latency input polling and event system across keyboards, mouse pointers, and hardware gamepads.

---

## Input Devices

<div class="grid cards" markdown>

- :material-keyboard:{ .lg .middle } **[Keyboard Input](/player-input/keyboard-input/)**

    ---

    Key listener bindings, continuous key state polling, and configurable directional mapping.

- :material-mouse:{ .lg .middle } **[Mouse Input](/player-input/mouse-input/)**

    ---

    Pointer coordinates in screen/map space, mouse wheel scrolling, and drag-and-drop interactions.

- :material-controller:{ .lg .middle } **[Gamepad Input](/player-input/gamepad-input/)**

    ---

    Multi-controller gamepad polling powered by `Input4j` with zero native DLL configuration.

</div>

---

## Temporary Input Locking (Cutscenes & Dialogues)

To disable input during cutscenes, pause menus, or dialogue sequences:

```java
// Lock input during cutscene
Input.keyboard().stop();
Input.mouse().stop();

// Resume input after cutscene
Input.keyboard().start();
Input.mouse().start();
```
