---
title: "Java and Groovy scripting"
description: "Add Java or Groovy gameplay scripts to LITIENGINE games while keeping a normal IntelliJ and Gradle development workflow."
keywords: ["LITIENGINE", "scripting", "Groovy", "Java", "IntelliJ", "utiLITI", "game behavior"]
---

# Java and Groovy scripting

LITIENGINE scripts are ordinary JVM classes attached to the game, an environment, or an entity. They use the same public API as the rest of your game. Groovy reduces ceremony for small behaviors, while Java remains fully supported for larger systems.

Script source stays in your project. The game resource file stores only definitions, bindings, and configured parameter values. This keeps the source useful in IntelliJ, Git, Gradle, and other JVM tools.

> **Warning:** Project scripts are trusted game code. Running a game or the utiLITI preview can execute that code.

## Add Groovy support

Add the Groovy plugin and scripting provider to the game build:

```groovy
plugins {
  id 'java'
  id 'groovy'
}

dependencies {
  implementation 'de.gurkenlabs:litiengine:VERSION'
  implementation 'de.gurkenlabs:litiengine-groovy:VERSION'
}
```

Place Groovy classes under `src/main/groovy`. Java scripts remain under `src/main/java` and require no Groovy provider.

## Write an entity script

Extend one of the lifecycle base classes and give the implementation a stable ID:

```groovy
import de.gurkenlabs.litiengine.entities.Creature
import de.gurkenlabs.litiengine.scripting.CreatureScript
import de.gurkenlabs.litiengine.scripting.ScriptHostType
import de.gurkenlabs.litiengine.scripting.ScriptInfo
import de.gurkenlabs.litiengine.scripting.ScriptProperty

@ScriptInfo(id = 'enemy.guard', name = 'Guard behavior', host = ScriptHostType.ENTITY,
  target = Creature)
class GuardBehavior extends CreatureScript {
  @ScriptProperty(name = 'Detection range', min = 0, unit = 'px')
  double detectionRange = 160

  @Override
  void update() {
    def target = context().entities(Creature)
      .alive()
      .enemyOf(host())
      .within(host().center, detectionRange)
      .nearestTo(host().center)
      .first()

    if (target.isEmpty()) {
      host().movement().dx = 0
      host().movement().dy = 0
      return
    }

    def dx = target.get().center.x - host().center.x
    def dy = target.get().center.y - host().center.y
    def length = Math.hypot(dx, dy)
    host().movement().dx = length == 0 ? 0 : dx / length
    host().movement().dy = length == 0 ? 0 : dy / length
  }
}
```

The equivalent Java implementation uses the same base class and API:

```java
@ScriptInfo(
  id = "enemy.guard",
  name = "Guard behavior",
  host = ScriptHostType.ENTITY,
  target = Creature.class)
public final class GuardBehavior extends CreatureScript {
  @ScriptProperty(name = "Detection range", min = 0, unit = "px")
  private double detectionRange = 160;

  @Override
  public void update() {
    var target = context().entities(Creature.class)
      .alive()
      .enemyOf(host())
      .within(host().getCenter(), this.detectionRange)
      .nearestTo(host().getCenter())
      .first();

    // Use the normal Creature, movement, ability, and resource APIs here.
  }
}
```

## Entity scripts are controllers

Bindings loaded from map objects are owned by an `EntityScriptController`. This makes scripting follow the same lifecycle as movement, animation, and behavior controllers:

```java
EntityScriptController<?> scripts = entity.scripts();
scripts.getBindings();
```

The environment attaches the controller first. The controller waits for the entity's `loaded` event before it creates script instances, so `host().getEnvironment()` is already valid inside `onLoaded`. Removing or unloading the entity detaches the controller, cancels managed work, and calls `onUnloaded`.

Use direct `Game.scripts().attach(...)` calls for temporary or entirely code-driven attachments. Controller-owned and direct attachments are tracked independently.

## Lifecycle base classes

Choose the narrowest base class for the behavior:

| Base class | Host | Lifecycle |
| --- | --- | --- |
| `GameScript` | Game | `started`, `update`, `stopped` |
| `EnvironmentScript` | Environment | `loaded`, `update`, `unloaded` |
| `EntityScript<T>` | Any entity type | `loaded`, `message`, `update`, `unloaded` |
| `CreatureScript` | Creature | Creature-oriented `EntityScript` |

The runtime calls lifecycle methods on the game thread. An exception faults only that binding and is reported through `Game.scripts().getDiagnostics()`.

The lifecycle entry points intentionally mirror the stable engine events:

| Scope | Entry points |
| --- | --- |
| Game | `onStarted`, `update`, `onStopped` |
| Environment | `onLoaded`, `onCleared`, `update`, `onUnloaded` |
| Entity | `onLoaded`, `onMessage`, `update`, `onUnloaded` |

Transform, collision, combat, input, and custom gameplay events are explicit subscriptions rather than dozens of lifecycle overrides. Register those through the normal engine listener APIs and pass their cleanup to `context().manage(...)`. This keeps the beginner-facing lifecycle small while retaining the full engine API.

The former `started`, `stopped`, `loaded`, `message`, and `unloaded` overrides remain source-compatible but are deprecated for new scripts.

## Parameters

Annotate non-final fields with `@ScriptProperty`. Bindings store values as strings and the engine converts primitive values, strings, enums, arrays, materials, and attributes using the same typed reflection path used by map objects.

```java
@ScriptProperty(name = "Delay", defaultValue = "500", min = 0, unit = "ms")
private int delay;
```

Use `required = true` when a missing value should prevent the script from attaching. utiLITI reads the annotation and presents the field in the binding inspector.

## Managed listeners and delayed work

A script context owns registrations added with `context().manage(...)` and delayed actions created with `context().schedule(...)`:

```java
context().schedule(500, () -> host().sendMessage(this, "ready"));

context().manage(() -> host().removeListener(myListener));
```

The runtime releases these automatically when the host is removed, its map unloads, the game terminates, or the script reloads. This prevents old script generations from leaving listeners or callbacks behind.

For multi-step behavior, use a managed sequence instead of nesting delayed callbacks:

```java
context().sequence()
  .then(() -> host().sendMessage(this, "engaging"))
  .waitFor(500)
  .then(() -> host().castAbility("charge"))
  .waitFor(1_000)
  .then(() -> host().sendMessage(this, "ready"))
  .start();
```

Detaching or reloading the script cancels the remaining steps.

## Register definitions and bindings from Java

The editor normally persists definitions in the game resource file. They can also be configured through the API:

```java
var definition = new ScriptDefinition(
  "enemy.guard",
  "groovy",
  "src/main/groovy/com/example/GuardBehavior.groovy",
  "com.example.GuardBehavior",
  ScriptHostType.ENTITY);
definition.setTargetType(Creature.class.getName());

Game.scripts().setProjectRoot(Path.of("."));
Game.scripts().setDefinitions(List.of(definition));

var binding = new ScriptBinding("enemy.guard");
binding.setParameter("detectionRange", "220");
Game.scripts().attach(creature, binding);
```

Use `Game.scripts().reload("enemy.guard")` for an explicit source reload. Compilation happens before active instances are replaced. If compilation fails, the last working generation continues to run.

## Entity queries

`Environment.query(...)` and `ScriptContext.entities(...)` provide reusable filters for logic that otherwise tends to be repeated in controllers:

```java
var nearestEnemy = environment.query(Creature.class)
  .tagged("guard")
  .alive()
  .enemyOf(player)
  .within(player.getCenter(), 300)
  .nearestTo(player.getCenter())
  .first();
```

Queries operate on the environment's current entity snapshot and preserve deterministic ordering when a comparator such as `nearestTo` is applied.

## Production builds

Gradle and IntelliJ compile both Java and Groovy classes normally. Packaged games can bind precompiled classes by using the `java` language provider. Runtime Groovy compilation is primarily intended for explicit editor reloads and moddable games.

For normal releases, compile scripts with the project and decide separately whether to include their source files.
