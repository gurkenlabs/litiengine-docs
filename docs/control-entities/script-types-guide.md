---
meta.description: "Comprehensive guide to GameScript, EnvironmentScript, and CreatureScript in LITIENGINE."
meta.keywords: "LITIENGINE, GameScript, EnvironmentScript, CreatureScript, lifecycle, scripting guide"
meta.title: "Game, Environment & Entity Scripts Guide"
---

# Game, Environment & Entity Scripts Guide

Every script in LITIENGINE extends a specialized lifecycle base class corresponding to its operational scope. This guide explains each script tier and provides actionable examples.

---

## 1. 🎮 Game Scripts (`GameScript`)

### What is a Game Script?
A `GameScript` is the **global entry point and orchestrator** of your game. It starts as soon as the game engine boots up and continues running uninterrupted across all map transitions.

### What should you do in a Game Script?
- **Load the starting map**: Call `loadMap("level1")` on startup or whenever you want to trigger a world transition.
- **Initialize global game state**: Set up persistent scores, player inventory, unlocked levels, and life counts in `globals`.
- **Background soundtracks**: Manage music with `playMusic("main_theme")` and `stopMusic()`.
- **Global input hotkeys**: Listen for Pause (`ESC`), Mute (`M`), or Restart (`R`) keys.
- **Global game-over / victory screens**: Coordinate level transitions when objectives are met.

### Example: MainGame.java
```java
package scripts;

import de.gurkenlabs.litiengine.*;
import de.gurkenlabs.litiengine.input.Input;
import de.gurkenlabs.litiengine.resources.*;
import de.gurkenlabs.litiengine.scripting.*;
import java.awt.event.KeyEvent;

@ScriptInfo(id = "MainGame", host = ScriptHostType.GAME)
public class MainGame extends GameScript {

  @Override
  public void onStarted() {
    // 1. Initialize persistent player state
    globals.put("player_score", 0);
    globals.put("player_lives", 3);
    globals.put("current_stage", 1);

    // 2. Play background music
    playMusic("overworld_theme");

    // 3. Load initial map if not already loaded by launcher
    if (Game.world().environment() == null) {
      loadMap("level_1");
    }

    // 4. Global shortcut: Pause game on Escape
    Input.keyboard().onKeyTyped(KeyEvent.VK_ESCAPE, event -> {
      // Toggle pause menu or game state
    });
  }

  @Override
  public void update() {
    // Global update loop running every tick
  }

  @Override
  public void onStopped() {
    // Clean up when game shuts down
    stopMusic();
  }
}
```

---

## 2. 🗺 Environment Scripts (`EnvironmentScript`)

### What is an Environment Script?
An `EnvironmentScript` is attached to a **specific map**. It activates when that map is loaded into the world and terminates when the map unloads.

### What should you do in an Environment Script?
- **Map initialization & setup**: Announce level start banners, configure ambient lighting, and initialize enemy wave timers.
- **Objective monitoring**: Listen to `onEntityRemoved(IEntity)` to detect when all boss minions or targets are defeated.
- **Level clear transitions**: Trigger victory cinematics, award bonuses, and call `loadMap("level_2")`.
- **Camera cinematics**: Direct cutscenes using `context().sequence().cameraPanTo(...)` and `cameraZoom(...)`.

### Example: DungeonLevel.java
```java
package scripts;

import de.gurkenlabs.litiengine.*;
import de.gurkenlabs.litiengine.entities.*;
import de.gurkenlabs.litiengine.environment.Environment;
import de.gurkenlabs.litiengine.resources.*;
import de.gurkenlabs.litiengine.scripting.*;

@ScriptInfo(id = "DungeonLevel", host = ScriptHostType.ENVIRONMENT)
public class DungeonLevel extends EnvironmentScript {

  @Override
  public void onLoaded() {
    // Map is active: show opening banner
    context().ui().showBanner("DUNGEON ENTRANCE", "Defeat all skeletons to advance!", 3000);
  }

  @Override
  protected void onEntityRemoved(IEntity entity) {
    // Check if all enemy creatures in this environment are defeated
    var remainingEnemies = EntityQuery.in(environment(), Creature.class).alive().list();
    if (remainingEnemies.isEmpty()) {
      context().ui().showBanner("VICTORY!", "Dungeon Cleared!", 3500);

      // Transition to next level after a brief delay
      context().schedule(3500, () -> {
        var game = Game.scripts().getGameScript(MainGame.class);
        if (game != null) {
          game.loadMap("dungeon_boss");
        }
      });
    }
  }

  @Override
  public void update() {
    // Map-level polling logic
  }
}
```

---

## 3. ⚔ Creature & Entity Scripts (`CreatureScript` / `EntityScript`)

### What is a Creature Script?
A `CreatureScript` is attached to an individual **creature entity** (players, monsters, NPCs, bosses). It executes while the entity is alive in an active environment.

### What should you do in a Creature Script?
- **AI Movement**: Chase players using `moveTowards(target)` or patrol using `moveInDirection(Direction)`.
- **Combat Abilities**: Create and cast abilities using `createAbility("Fireball")` and launch projectiles using `spawnProjectile()`.
- **Combat Reactions**: Intercept damage in `onHit(event)`, show floating combat numbers (`context().ui().floatText(...)`), and despawn on `onDeath(...)`.
- **Interactions**: Handle player talk/activate triggers in `onInteract(source)`.

### Example: GoblinAI.java
```java
package scripts;

import de.gurkenlabs.litiengine.*;
import de.gurkenlabs.litiengine.entities.*;
import de.gurkenlabs.litiengine.resources.*;
import de.gurkenlabs.litiengine.scripting.*;
import java.awt.Color;

@ScriptInfo(id = "GoblinAI", host = ScriptHostType.ENTITY, target = Creature.class)
public class GoblinAI extends CreatureScript {
  @ScriptProperty(name = "Aggro Range", defaultValue = "180", min = 50, unit = "px")
  private double aggroRange = 180;

  @Override
  public void update() {
    if (isDead()) return;

    // Find nearest player creature
    var player = EntityQuery.in(environment(), Creature.class)
        .alive()
        .within(host().getCenter(), aggroRange)
        .nearestTo(host().getCenter())
        .first();

    if (player.isPresent()) {
      moveTowards(player.get());

      // Attack if close enough
      if (host().getCenter().distance(player.get().getCenter()) < 40) {
        createAbility("Slash").range(50).cooldown(1200).onCast(exec -> {
          player.get().hit(15);
        }).cast();
      }
    }
  }

  @Override
  protected void onHit(EntityHitEvent event) {
    // Display floating combat damage number above goblin
    context().ui().floatText("-" + event.getDamage(), host(), Color.RED);
  }

  @Override
  protected void onDeath(ICombatEntity entity, EntityHitEvent hitEvent) {
    // Reward score and remove entity
    int score = (int) globals.getOrDefault("player_score", 0);
    globals.put("player_score", score + 100);

    remove();
  }
}
```

---

## Lifecycle Method Reference

| Lifecycle Hook | Base Class | Trigger Condition |
| :--- | :--- | :--- |
| `onStarted()` | `GameScript` | Called once when the game loop starts. |
| `onStopped()` | `GameScript` | Called when the game terminates. |
| `onLoaded()` | `EnvironmentScript`, `EntityScript` | Called when map/entity is loaded and ready. |
| `onUnloaded()` | `EnvironmentScript`, `EntityScript` | Called when map/entity unloads. |
| `update()` | All | Called once per game loop tick. |
| `onHit(EntityHitEvent)` | `EntityScript` | Called when host receives combat damage. |
| `onDeath(ICombatEntity, EntityHitEvent)` | `EntityScript` | Called when host entity's hitpoints drop to zero. |
| `onCollision(CollisionEvent)` | `EntityScript` | Called when colliding with static geometry or obstacles. |
| `onInteract(IEntity)` | `EntityScript` | Called when another entity interacts with host. |
| `onMessage(String, Object)` | `EntityScript` | Called when a message is received via `sendMessage(...)`. |
| `onEntityAdded(IEntity)` | `EnvironmentScript` | Called when an entity is spawned into the map. |
| `onEntityRemoved(IEntity)` | `EnvironmentScript` | Called when an entity is despawned or removed from the map. |
