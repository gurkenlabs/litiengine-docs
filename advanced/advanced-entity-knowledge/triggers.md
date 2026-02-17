---
meta.description: "Learn how to use Trigger entities in LITIENGINE to create area-based events and scripting."
meta.keywords: "LITIENGINE, trigger, area, event, activate, scripting, Java"
---

# Triggers

Triggers are area-based entities that fire events when other entities enter or exit their bounds. Use them for scripting game events without writing code.

## Creating Triggers

### Via utiLITI

1. Add a **Trigger** entity to your map
2. Define the trigger area (bounding box)
3. Set activation properties

### Via Code

```java
Trigger trigger = new Trigger("myTrigger", TriggerActivation.PROPAGATE);
trigger.setLocation(100, 100);
trigger.setWidth(64);
trigger.setHeight(64);

// Add to environment
Game.world().environment().add(trigger);
```

## Trigger Properties

### Activation Type

- **PROPAGATE**: Triggers once, stays active
- **ONCE**: Triggers once, then disables
- **TOGGLE**: Activates/deactivates on each entry

```java
trigger.setActivationType(TriggerActivation.ONCE);
```

### Target Entities

Define which entities can activate the trigger:

```java
// Only player can activate
trigger.setTarget(Creature.class);

// Specific entity name
trigger.setTargetEntityName("player");
```

### Message on Activation

```java
trigger.setMessage("OPEN_DOOR");
trigger.setMessageTarget("door1");
```

## Trigger Events

### Activation Events

```java
trigger.onActivated(event -> {
  IEntity activator = event.getEntity();
  System.out.println("Triggered by: " + activator.getName());
  
  // Execute trigger logic
  spawnEnemies();
  closeDoors();
});
```

### Deactivation Events

```java
trigger.onDeactivated(event -> {
  System.out.println("Entity left trigger zone");
});
```

## Common Use Cases

### Level Transitions

```java
Trigger exit = new Trigger("exit", TriggerActivation.ONCE);
exit.onActivated(e -> {
  Game.world().loadEnvironment("level2");
});
```

### Enemy Spawning

```java
Trigger spawnZone = new Trigger("spawn_wave1", TriggerActivation.ONCE);
spawnZone.onActivated(e -> {
  for (int i = 0; i < 5; i++) {
    Enemy enemy = new Enemy();
    enemy.setLocation(spawnX + i * 50, spawnY);
    Game.world().environment().add(enemy);
  }
});
```

### Cutscenes

```java
Trigger cutscene = new Trigger("intro_cutscene", TriggerActivation.ONCE);
cutscene.onActivated(e -> {
  Player.instance().setControlEnabled(false);
  playDialog("welcome");
  Game.loop().execute(3000, () -> {
    Player.instance().setControlEnabled(true);
  });
});
```

## Chained Triggers

Triggers can activate other triggers or send messages:

```java
trigger1.onActivated(e -> {
  // Activate trigger2
  Trigger trigger2 = Game.world().environment().getTrigger("trigger2");
  trigger2.activate((IEntity) e.getEntity());
});
```

## See Also

- [Messaging System](/docs/control-entities/messaging-system/) - Entity communication
- [Behavior Controllers](/docs/control-entities/behavior-controller/) - AI scripting
- [Map Objects](/docs/tile-maps/map-objects/) - Placing entities
