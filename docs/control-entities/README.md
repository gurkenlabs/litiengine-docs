---
title: "Control Entities Overview"
description: "Master entity control in LITIENGINE: controllers, animation, movement, AI behaviors, abilities, and modern Groovy/Java scripting."
keywords: ["LITIENGINE", "controllers", "movement", "animation", "behavior", "AI", "scripting", "Groovy", "Java"]
---

# Control Entities

In LITIENGINE, entity behaviors, animations, locomotion, combat actions, and artificial intelligence are managed through a modular and extensible control architecture. This architecture allows developers to separate game object state (`IEntity`) from dynamic runtime logic.

```mermaid
graph TD
  EC["<b>Entity Control Architecture</b>"]
  EC --> M["MovementController<br/><i>Physics & Input Forces</i>"]
  EC --> A["AnimationController<br/><i>Spritesheets & States</i>"]
  EC --> B["BehaviorController<br/><i>AI & State Trees</i>"]
  EC --> S["Scripting Engine<br/><i>Groovy & Java Logic</i>"]
```

## The Four Control Paradigms

LITIENGINE offers four distinct yet interoperable ways to drive entity behavior:

### 1. Built-in Entity Controllers (`IEntityController`)
Controllers handle low-level continuous tasks such as keyboard/gamepad-driven movement, pathfinding locomotion, or sprite state transitions:

* **`IMovementController`**: Translates input vectors or navigation paths into 2D velocity forces within the physics engine.
* **`IEntityAnimationController`**: Evaluates entity state flags (e.g. `isIdle`, `isMoving`, `isDead`, custom states) and plays corresponding spritesheet sequences.

### 2. AI & Behavior Controllers
For enemy NPCs, companions, and bosses:

* **`BehaviorController`**: State-machine and behavior-tree implementations for patrol routes, target acquisition, aggro radiuses, and combat sequences.

### 3. Ability & Combat Framework
Structured spell, skill, and combat action system:

* **`Ability`**: Modular spells or physical attacks with cooldowns, range checks, impact effects, and mana/resource costs.

### 4. Modern Scripting Engine (Groovy & Java)
Write hot-reloadable game logic directly in **utiLITI** or external scripts:

* **Entity Scripts (`EntityScript`)**: Attach custom logic to individual entities without writing boilerplate Java classes.
* **Environment Scripts (`EnvironmentScript`)**: Control level-wide triggers, cutscenes, wave spawners, and interactive puzzles.
* **Game Scripts (`GameScript`)**: Manage game startup, global progression flags, inventory, and cross-map state.

## Chapter Topics

| Topic | Description |
| :--- | :--- |
| **[Entity Controllers](entity-controllers.md)** | Understand the controller lifecycle (`addController`, `getController`, `update`). |
| **[Animation Controller](animation-controller.md)** | Configure sprite animation rules, frame durations, and custom animation states. |
| **[Movement Controller](movement-controller.md)** | Handle keyboard input, gamepad locomotion, velocity, and collision avoidance. |
| **[Behavior Controller](behavior-controller.md)** | Build intelligent AI entities with state machines and behavior trees. |
| **[Messaging System](messaging-system.md)** | Decouple entity communication via typed message events. |
| **[Ability Framework](ability-framework.md)** | Implement cooldown-driven spells, attacks, effects, and area-of-effect abilities. |
| **[Java & Groovy Scripting](scripting.md)** | Write interactive scripts that run dynamically inside the engine. |
| **[Script-Only Game Architecture](script-only-games.md)** | Build full LITIENGINE games using scripts and utiLITI without custom Java builds. |
| **[Script Types Guide](script-types-guide.md)** | Deep dive into `GameScript`, `EnvironmentScript`, and `EntityScript`. |
| **[Combat & Action Scripting](combat-scripting.md)** | Script damage handlers, health bars, weapon swings, and projectile mechanics. |

## Quick Example: Attaching a Custom Controller

```java
public class Player extends Creature {
  public Player() {
    super("player");

    // Add standard keyboard movement controller
    addController(new KeyboardEntityController<>(this));

    // Listen to movement events
    movement().onMoved(e -> {
      // Custom footsteps, trail effects, or stamina drain
    });
  }
}
```
