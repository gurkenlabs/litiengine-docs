---
title: Modifying Example Projects
icon: lucide/code-xml
description: Learn how to clone, inspect, and customize existing LITIENGINE sample
  games like SERVUS BONUS using both Java code and the utiLITI Editor.
keywords: [LITIENGINE, tutorial, sample game, servus bonus, gradle, utiLITI, customization,
  modding]
tags: [tutorial, examples, modding, customization, learning]
---
# Modifying Example Projects

A great way to learn LITIENGINE is to clone, run, and experiment with existing sample projects. This tutorial walks you through modifying **SERVUS BONUS**, an open-source 2D action game created with LITIENGINE.

---

## 1. Getting the Project

Clone the repository and build the project using Gradle:

```bash
git clone https://github.com/gurkenlabs/litiengine-ldjam44.git
cd litiengine-ldjam44
./gradlew run
```

---

## 2. Code vs. utiLITI: Where to Make Changes

When modifying a LITIENGINE game, changes are typically divided between **Java Code** (logic, controllers, physics) and the **utiLITI Editor** (sprites, animations, maps, entity placement):

| Game Aspect | Best Modified In | How It's Configured |
| :--- | :--- | :--- |
| **Movement Speed** | **Java Code** | `@MovementInfo(velocity = ...)` on Entity class |
| **Combat Cooldowns & Abilities** | **Java Code** | `Ability` subclass or `@AbilityInfo` attributes |
| **Creature Sprites & Animations** | **utiLITI Editor** | Sprite Editor & Keyframe durations in `game.litidata` |
| **Map Layout & Enemy Placements** | **utiLITI Editor** | Drag-and-drop objects onto map layers |

---

## 3. Practical Modification Examples

### A. Adjusting Player Movement Speed (Code)

Open `src/main/java/de/gurkenlabs/ldjam44/entities/Player.java`:

```java
// Increase velocity from 70 to 140 for double movement speed
@MovementInfo(velocity = 140)
@CollisionInfo(collisionBoxWidth = 8, collisionBoxHeight = 16, collision = true)
public class Player extends Creature {
  // ...
}
```

### B. Customizing Attack Cooldown (Code)

Open the combat ability class (e.g. `Hit.java`):

```java
// Reduce cooldown from 1000ms to 250ms for rapid attacks
@AbilityInfo(cooldown = 250, range = 24)
public class Hit extends Ability {
  public Hit(Creature executor) {
    super(executor);
  }
}
```

### C. Modifying Spritesheets and Animations (utiLITI)

1. Launch **utiLITI** and open `game.litidata` from the project directory.
2. In the **Spritesheet** shelf, select `monger-walk` or `monger-attack`.
3. Adjust keyframe durations (e.g. changing `100, 100, 100` to `50, 50, 50` to speed up the animation).
4. Save the `.litidata` file and restart the game to see the updated visual pacing!

---

## 4. Next Steps

* Explore creating custom maps in utiLITI: **[Import Maps with utiLITI](../utiliti-editor/maps-and-environments.md)**
* Learn about the full entity lifecycle: **[Entity Framework Overview](../entity-framework/README.md)**
