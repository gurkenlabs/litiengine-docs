---
title: Messaging System
icon: lucide/message-square
description: Learn how to use the Messaging System in LITIENGINE for entity-to-entity
  communication and event handling.
keywords: [LITIENGINE, messaging, events, communication, entity, Java]
tags: [messaging, events, communication, entity-messages]
---
# Messaging System

The Messaging System allows entities to communicate with each other through messages and events. This decouples entity behavior and enables reactive game logic.

## Entity Messages

The core messaging API in LITIENGINE sends string-based messages from a sender object to an `IEntity` receiver:

```java
// Send a message to a specific target entity
IEntity target = Game.world().environment().getEntity("lever");
if (target != null) {
  target.sendMessage(player, "ACTIVATE");
}

// Broadcast a message to all entities in the active environment
for (IEntity entity : Game.world().environment().getEntities()) {
  entity.sendMessage(this, "LEVEL_COMPLETE");
}
```

## Receiving Messages

Entities register message listeners via `onMessage()`:

```java
// Listen for any incoming message
door.onMessage(event -> {
  System.out.println("Message: " + event.getMessage() + " from " + event.getSource());
});

// Listen for a specific message string
door.onMessage("OPEN_DOOR", event -> {
  openDoor();
});
```

Subclasses of `Entity` can also intercept messages by overriding `sendMessage`:

```java
public class LeverEntity extends Entity {
  public LeverEntity() {
    super("lever");
  }

  @Override
  public String sendMessage(Object sender, String message) {
    super.sendMessage(sender, message);
    if ("TOGGLE".equalsIgnoreCase(message)) {
      toggleLever();
      return "toggled";
    }
    return null;
  }

  private void toggleLever() {
    // Handle toggle logic
  }
}
```

## Built-In Message Support

Several built-in LITIENGINE entities already support predefined messages out of the box:

- **`LightSource`**: Listens for `"toggle"` to invert its illumination state:
  ```java
  LightSource torch = Game.world().environment().getLightSource("dungeon_torch");
  if (torch != null) {
    torch.sendMessage(this, LightSource.TOGGLE_MESSAGE);
  }
  ```
- **`Trigger`**: Can be configured in utiLITI with a custom message that is automatically dispatched to target entities when activated.

## Entity Lifecycle Events

Subscribe to entity lifecycle callbacks:

```java
// When entity is loaded into an active environment
entity.onLoaded(e -> {
  System.out.println("Entity loaded: " + e.getName());
});

// When entity is removed from an environment
entity.onRemoved(e -> {
  System.out.println("Entity removed: " + e.getName());
});
```

## Combat Events

Listen for combat-related events on `CombatEntity` (`Creature`, `Prop`):

```java
CombatEntity combatEntity = ...;

// When hit by an attack
combatEntity.onHit(event -> {
  int damage = event.getDamage();
  System.out.println("Took " + damage + " damage!");
});

// When entity dies
combatEntity.onDeath(event -> {
  System.out.println("Entity died!");
  spawnLoot();
});

// When entity is resurrected
combatEntity.onResurrect(event -> {
  System.out.println("Entity revived!");
});
```

## Collision Events

Handle collisions on `CollisionEntity`:

```java
CollisionEntity colliding = ...;

colliding.onCollision(event -> {
  for (ICollisionEntity other : event.getInvolvedEntities()) {
    if (other != colliding) {
      handleCollision(other);
    }
  }
});
```

## Movement Events

Track entity movement on `IMobileEntity`:

```java
Creature mobile = ...;

mobile.onMoved(event -> {
  // Entity position changed
  checkProximityTriggers(event.getDeltaX(), event.getDeltaY());
});
```

## Event Listeners Management

Register and deregister listeners:

```java
// Register listener
CombatEntityHitListener listener = event -> handleHit(event);
combatEntity.onHit(listener);

// Deregister listener
combatEntity.removeListener(listener);
```

## Environment Events

Listen for map load and unload events:

```java
// When an environment is loaded
Game.world().onLoaded(env -> {
  initializeLevel(env);
});

// When an environment is unloaded
Game.world().onUnloaded(env -> {
  cleanupLevel(env);
});

// When an entity is added to the active environment
Game.world().environment().onEntityAdded(e -> {
  System.out.println("Entity added: " + e.getEntity().getName());
});
```

## Trigger System

Triggers fire events when crossed or interacted with:

```java
Trigger trigger = Game.world().environment().getTrigger("dungeon_exit");
if (trigger != null) {
  trigger.addActivatedListener(event -> {
    // Player entered trigger zone
    IEntity activator = event.getEntity();
    loadNextLevel();
  });
}
```

## See Also

- [Entity Controllers](entity-controllers.md) - Controller overview
- [Entity Framework](../entity-framework/README.md) - Entity system
- [Behavior Controller](behavior-controller.md) - AI reactions
