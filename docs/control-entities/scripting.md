---
title: "Java Scripting Engine"
description: "Add pure Java gameplay scripts to LITIENGINE games with dynamic runtime execution and hot reload."
keywords: ["LITIENGINE", "scripting", "Java", "IntelliJ", "utiLITI", "game behavior", "hot reload"]
---

# Java Scripting Engine

LITIENGINE scripts are ordinary pure Java classes attached to the game, an environment, or an entity. They use the same public API as the rest of your game, allowing you to write modular, hot-reloadable gameplay logic directly in Java.

---

## 1. Script Architecture (3-Tier Model)

LITIENGINE defines three distinct script types:

1. **`GameScript`**: Global game lifecycle, master timers, and cross-level progression.
2. **`EnvironmentScript`**: Level-specific triggers, zone objectives, and ambient world events.
3. **`CreatureScript`**: Entity AI behaviors, custom combat actions, and status effects.

---

## 2. Writing a Creature Script in Java

Create a Java class in your project (e.g. `src/main/java/com/example/game/scripts/GuardBehavior.java`):

```java
package com.example.game.scripts;

import de.gurkenlabs.litiengine.Game;
import de.gurkenlabs.litiengine.entities.Creature;
import de.gurkenlabs.litiengine.scripting.CreatureScript;
import de.gurkenlabs.litiengine.scripting.ScriptInfo;

@ScriptInfo(
  name = "Guard Patrol Behavior",
  description = "Patrols between waypoints and chases the player on sight."
)
public class GuardBehavior extends CreatureScript {

  @Override
  public void onLoaded(Creature entity) {
    System.out.println("Guard loaded: " + entity.getName());
  }

  @Override
  public void update(Creature entity) {
    // Continuous logic executed on every game loop tick
  }
}
```

---

## 3. Writing an Environment Script in Java

```java
package com.example.game.scripts;

import de.gurkenlabs.litiengine.environment.Environment;
import de.gurkenlabs.litiengine.scripting.EnvironmentScript;
import de.gurkenlabs.litiengine.scripting.ScriptInfo;
import java.awt.Color;

@ScriptInfo(
  name = "Dungeon Ambience & Waves",
  description = "Controls dungeon torch lighting and monster wave spawning."
)
public class DungeonLevelScript extends EnvironmentScript {

  @Override
  public void onLoaded(Environment environment) {
    // Set sinister dungeon ambient darkness
    environment.getAmbientLight().setColor(new Color(15, 10, 25, 220));
  }

  @Override
  public void update(Environment environment) {
    // Monitor wave objectives
  }
}
```

---

## 4. Script Binding & Hot Reload

Scripts can be bound to map objects in the **utiLITI Editor** Inspector or registered programmatically via Java code:

```java
// Bind script dynamically at runtime
Game.world().environment().getCreature("guard-1").attachScript(new GuardBehavior());
```

!!! tip "Zero Overhead"
    Because LITIENGINE scripts are standard compiled Java bytecode running on the JVM, they execute at maximum native CPU speed with zero JNI reflection overhead or garbage collection penalty.
