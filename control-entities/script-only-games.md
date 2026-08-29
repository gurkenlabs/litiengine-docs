---
meta.description: "Build complete LITIENGINE games using only scripts with zero boilerplate main classes."
meta.keywords: "LITIENGINE, script-only games, GameScript, EnvironmentScript, CreatureScript, game development"
meta.title: "Script-Only Game Architecture"
---

# Script-Only Game Architecture

LITIENGINE allows developers to build entire games using pure scripts—without writing custom `Program.java` entry points, manual game loop setup, or standalone boilerplate classes.

With the **3-tier scripting architecture** and the built-in `GameLauncher`, your entire game logic can live in modular, hot-reloadable Java or Groovy scripts authored directly in utiLITI or IntelliJ.

```text
 ┌──────────────────────────────────────────────────────────┐
 │  🎮 GameScript (Global Game Lifecycle & Entry Point)     │
 │  • Persistent across all map transitions                 │
 │  • Loads initial maps: loadMap("level1")                 │
 │  • Global player state: globals.put("score", 0)          │
 │  • Soundtrack & audio: playMusic("bg_theme")             │
 │  • Global keybindings: Pause menu on ESC                 │
 └────────────────────────────┬─────────────────────────────┘
                              │ loads & transitions
                              ▼
 ┌──────────────────────────────────────────────────────────┐
 │  🗺 EnvironmentScript (Map / Level Controller)           │
 │  • Active while a specific map is loaded                 │
 │  • Wave spawning & map objectives                        │
 │  • onEntityRemoved -> Level clear & transition           │
 │  • Cinematics & camera: cameraPanTo(boss, 60)            │
 └────────────────────────────┬─────────────────────────────┘
                              │ spawns & contains
                              ▼
 ┌──────────────────────────────────────────────────────────┐
 │  ⚔ CreatureScript / EntityScript (Entity Behaviors & AI) │
 │  • Attached to players, enemies, NPCs, chests, traps     │
 │  • AI movement: moveTowards(target)                      │
 │  • Combat abilities: createAbility("Fireball").cast()    │
 │  • Projectiles: spawnProjectile()                        │
 │  • Feedback: onHit (floatText), onDeath (remove())       │
 └──────────────────────────────────────────────────────────┘
```

---

## The 3 Script Tiers Explained

| Script Type | Host Base Class | Scope & Purpose |
| :--- | :--- | :--- |
| **Game Script** | `GameScript` | **Global Game Orchestrator & Entry Point** (the script equivalent of `main()`). Boots on game start, persists across map transitions, manages persistent state, background music, and global inputs. |
| **Environment Script** | `EnvironmentScript` | **Map-Level Controller**. Active while a specific map is loaded. Coordinates enemy wave spawning, map objectives, boss fights, level victory transitions, and cutscenes. |
| **Creature / Entity Script** | `CreatureScript` / `EntityScript<T>` | **Entity AI & Behaviors**. Attached to creatures, NPCs, props, or triggers. Governs movement, combat abilities, projectiles, floating damage text, and player interactions. |

---

## Inter-Script Communication & Shared State

Script-only games require a clean way for different scripts to share state and coordinate actions:

### 1. Global State (`globals`)
Use `globals` (an instance of `ScriptGlobals`) to share persistent player progress, scores, inventory, or unlocked levels across maps and entities:

```java
// In GameScript or CreatureScript:
globals.put("player_score", 1500);
globals.put("player_lives", 3);

// In any other script:
int score = (int) globals.getOrDefault("player_score", 0);
```

### 2. Entity Messaging (`sendMessage` and `onMessage`)
Entities can send directed or broadcast messages without hardcoded coupling:

```java
// Broadcast an event to all entity scripts on this entity:
sendMessage("enrage");

// Send a message directly to another entity:
sendMessage(targetCreature, "heal:50");

// Receive and handle messages:
@Override
protected void onMessage(String message, Object sender) {
  if ("enrage".equals(message)) {
    host().getVelocity().setBaseValue(300);
  }
}
```

### 3. Spatial Queries (`EntityQuery`)
Scripts can query and filter entities in the active environment:

```java
// Find the closest alive monster within 200 pixels:
var target = EntityQuery.in(environment(), Creature.class)
    .alive()
    .enemyOf(host())
    .within(host().getCenter(), 200)
    .nearestTo(host().getCenter())
    .first();
```

---

## Running a Script-Only Game

### 1. Testing in utiLITI
In the utiLITI editor, open the **Scripts Workspace** and click **Run** (or press `F5`). The editor automatically builds and launches the game session with hot-reloading enabled.

### 2. Running Standalone via `GameLauncher`
You can launch your project without writing a single line of Java startup code using the built-in CLI:

```bash
java -cp litiengine.jar de.gurkenlabs.litiengine.launch.GameLauncher --project game.litidata
```

CLI options supported by `GameLauncher`:
- `--project <path>`: Path to `.litidata` resource file.
- `--startup-script <id>`: Primary `GameScript` to execute on boot.
- `--map <name>`: Initial map to load.
- `--scale <float>`: Default render scale factor.
- `--title <text>`: Custom window title.
- `--gravity <int>`: Default 2D platformer gravity.
- `--release`: Run in production mode.
