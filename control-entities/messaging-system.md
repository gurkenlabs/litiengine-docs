---
meta.description: "Learn how to use the Messaging System in LITIENGINE for entity-to-entity communication and event handling."
meta.keywords: "LITIENGINE, messaging, events, communication, entity, Java"
---

# Messaging System

The Messaging System allows entities to communicate with each other through messages and events. This decouples entity behavior and enables reactive game logic.

## Entity Messages

Send messages between entities:

```java
// Send message to specific entity
entity.sendMessage("targetEntity", "ATTACK", damageData);

// Broadcast message to all entities
Game.world().environment().broadcastMessage("LEVEL_COMPLETE");
```

## Receiving Messages

Implement message handling:

```java
public class TriggerEntity extends Entity implements IMessageReceiver {
  
  @Override
  public void sendMessage(Object sender, String message) {
    if ("ACTIVATE".equals(message)) {
      activate();
    }
  }
  
  private void activate() {
    // Handle activation
  }
}
```

## Entity Events

Subscribe to entity lifecycle events:

```java
// When entity is added to environment
entity.onAdded(e -> {
  System.out.println("Entity spawned!");
});

// When entity is removed
entity.onRemoved(e -> {
  System.out.println("Entity destroyed!");
});
```

## Combat Events

Listen for combat-related events:

```java
CombatEntity combatEntity = ...;

// When hit by attack
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

Handle collision events:

```java
CollisionEntity colliding = ...;

colliding.onCollision(event -> {
  IEntity other = event.getInvolvedEntities().stream()
    .filter(e -> e != colliding)
    .findFirst()
    .orElse(null);
    
  if (other != null) {
    handleCollision(other);
  }
});
```

## Movement Events

Track entity movement:

```java
MobileEntity mobile = ...;

mobile.onMoved(event -> {
  // Entity position changed
  checkForTriggers();
});
```

## Custom Events

Define custom event types:

```java
public class GameEvent {
  private String type;
  private Object data;
  
  public GameEvent(String type, Object data) {
    this.type = type;
    this.data = data;
  }
  
  public String getType() { return type; }
  public Object getData() { return data; }
}

// Fire custom event
entity.fireEvent(new GameEvent("POWERUP_COLLECTED", powerupType));
```

## Event Listeners

Add and remove listeners dynamically:

```java
// Add listener
Consumer<HitEvent> listener = event -> handleHit(event);
combatEntity.onHit(listener);

// Remove listener (keep reference)
combatEntity.removeHitListener(listener);
```

## Environment Events

Listen for environment-level events:

```java
// When environment is loaded
Game.world().onLoaded(env -> {
  initializeLevel();
});

// When environment is unloaded
Game.world().onUnloaded(env -> {
  cleanupLevel();
});

// When entity is added to environment
Game.world().environment().onEntityAdded(e -> {
  System.out.println("Entity added: " + e.getEntity().getName());
});
```

## Trigger System

Triggers are special entities that fire events when entered:

```java
Trigger trigger = Game.world().environment().getTrigger("myTrigger");

trigger.onActivated(e -> {
  // Player entered trigger zone
  spawnEnemies();
});
```

## See Also

- [Entity Controllers](/docs/control-entities/entity-controllers/) - Controller overview
- [Entity Framework](/docs/entity-framework/README/) - Entity system
- [Behavior Controller](/docs/control-entities/behavior-controller/) - AI reactions
