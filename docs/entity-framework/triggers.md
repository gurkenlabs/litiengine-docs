---
title: Triggers
icon: lucide/door-open
description: Learn how to use Trigger entities in LITIENGINE for area-based events, door sensors, and script activation.
keywords: [LITIENGINE, trigger, area, event, activate, scripting, Java]
tags: [triggers, events, collision-trigger, interact, zones]
---

# Triggers

Triggers are area-based sensor entities that fire events when other entities enter or interact with their bounding box. They are commonly used for map transitions, cutscenes, trap zones, and door switches.

---

## Creating Triggers

### Via utiLITI

1. Add a **Trigger** entity to your map.
2. Define the trigger area (bounding box).
3. Set activation properties and target tags in the Entity Inspector.

### Via Code

```java
// Constructor: (activationType, name, message)
Trigger trigger = new Trigger(TriggerActivation.COLLISION, "exit_trigger", "exit_level");
trigger.setLocation(100, 100);
trigger.setWidth(64);
trigger.setHeight(64);

// Add to active environment
Game.world().environment().add(trigger);
```

---

## Trigger Activation Modes

The `TriggerActivation` enum defines how the trigger detects activation when instantiated:

- **`COLLISION`**: Activates automatically whenever an entity collides with or enters the trigger bounding box.
- **`INTERACT`**: Activated when game logic explicitly invokes `trigger.interact(entity)` (e.g. from an input listener or action key).

```java
// Create an interaction trigger: (activationType, name, message)
Trigger talkTrigger = new Trigger(TriggerActivation.INTERACT, "npc_trigger", "talk_elder");

// Explicitly trigger interaction from player input logic
talkTrigger.interact(player);
```

---

## Trigger Listeners

### Activation Listeners

```java
trigger.addActivatedListener(event -> {
  IEntity activator = event.getEntity();
  System.out.println("Trigger activated by: " + activator.getName());

  // Execute trigger logic
  spawnEnemies();
});
```

### Deactivation Listeners

```java
trigger.addDeactivatedListener(event -> {
  System.out.println("Entity left trigger zone: " + event.getEntity().getName());
});
```

### Unified TriggerListener

```java
trigger.addTriggerListener(new TriggerListener() {
  @Override
  public void activated(TriggerEvent event) {
    // Fired on activation
  }

  @Override
  public void deactivated(TriggerEvent event) {
    // Fired on deactivation
  }
});
```

---

## Common Use Cases

### Level Transitions

```java
Trigger exit = new Trigger(TriggerActivation.COLLISION, "exit_to_level2");
exit.addActivatedListener(e -> {
  Game.world().loadEnvironment("level2");
});
```

### Enemy Spawning

```java
Trigger spawnZone = new Trigger(TriggerActivation.COLLISION, "spawn_wave1");
spawnZone.addActivatedListener(e -> {
  for (int i = 0; i < 5; i++) {
    Enemy enemy = new Enemy();
    enemy.setLocation(200 + i * 40, 150);
    Game.world().environment().add(enemy);
  }
});
```

---

## See Also

- [Entity Event System](entity-events.md) - Entity listeners and callbacks
- [Messaging System](../control-entities/messaging-system.md) - Entity communication
- [Behavior Controllers](../control-entities/behavior-controller.md) - AI scripting
- [Map Objects](../tile-maps/map-objects.md) - Placing entities in utiLITI
