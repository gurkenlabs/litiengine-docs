---
meta.description: "Learn how to subscribe to entity events in LITIENGINE for movement, combat, lifecycle, and custom events."
meta.keywords: "LITIENGINE, entity events, listener, callback, onHit, onDeath, onMoved, Java"
---

# Subscribe to Entity Events

LITIENGINE entities support event-driven programming through listener registration. Subscribe to events to react to entity state changes without polling.

## Lifecycle Events

### Entity Spawned/Removed

```java
entity.onAdded(e -> {
  System.out.println("Entity added to environment");
});

entity.onRemoved(e -> {
  System.out.println("Entity removed from environment");
});
```

### Environment Events

```java
Game.world().environment().onEntityAdded(e -> {
  IEntity entity = e.getEntity();
  System.out.println("Spawned: " + entity.getName());
});

Game.world().environment().onEntityRemoved(e -> {
  IEntity entity = e.getEntity();
  System.out.println("Despawned: " + entity.getName());
});
```

## Combat Events

### Taking Damage

```java
CombatEntity combat = ...;

combat.onHit(event -> {
  int damage = event.getDamage();
  ICombatEntity attacker = event.getExecutor();
  
  System.out.println("Took " + damage + " damage!");
  
  // Play hit effect
  playHitSound();
  flashRed();
});
```

### Death and Resurrection

```java
combat.onDeath(event -> {
  System.out.println("Entity died!");
  
  // Handle death
  spawnLoot(combat.getLocation());
  Game.world().environment().remove(combat);
});

combat.onResurrect(event -> {
  System.out.println("Entity revived!");
  combat.setHitpoints(combat.getMaxHitpoints());
});
```

## Movement Events

### Position Changed

```java
MobileEntity mobile = ...;

mobile.onMoved(event -> {
  // Entity position updated
  checkForTriggers(mobile.getLocation());
  updateMinimap();
});
```

## Collision Events

```java
CollisionEntity colliding = ...;

colliding.onCollision(event -> {
  // Get other entities involved
  for (IEntity other : event.getInvolvedEntities()) {
    if (other != colliding) {
      handleCollisionWith(other);
    }
  }
});
```

## Animation Events

```java
entity.getAnimationController().onKeyFrameChanged((anim, frame) -> {
  // Specific frame reached
  if (frame == 3 && anim.getName().contains("walk")) {
    playFootstepSound();
  }
});

entity.getAnimationController().onFinished(anim -> {
  // Animation completed
  if (anim.getName().equals("attack")) {
    entity.setAttacking(false);
  }
});
```

## Trigger Events

```java
Trigger trigger = ...;

trigger.onActivated(event -> {
  IEntity activator = event.getEntity();
  System.out.println("Trigger activated by: " + activator.getName());
  
  // Execute trigger logic
  spawnEnemies();
  closeDoors();
});

trigger.onDeactivated(event -> {
  System.out.println("Entity left trigger zone");
});
```

## Custom Events

Define and fire custom events:

```java
public class PowerUpEvent {
  private String powerUpType;
  private IEntity target;
  
  // constructor, getters...
}

// Fire event
entity.fireEvent(new PowerUpEvent("speed", entity));

// Listen for events
entity.onEvent(PowerUpEvent.class, event -> {
  if ("speed".equals(event.getPowerUpType())) {
    applySpeedBoost();
  }
});
```

## Removing Listeners

Store listener references to remove them later:

```java
Consumer<HitEvent> hitListener = event -> handleHit(event);

// Add listener
combatEntity.onHit(hitListener);

// Remove specific listener
combatEntity.removeHitListener(hitListener);

// Remove all listeners of a type
combatEntity.clearHitListeners();
```

## Multiple Listeners

Multiple listeners can be registered for the same event:

```java
// Sound handler
entity.onHit(event -> playHitSound());

// Visual effect handler  
entity.onHit(event -> showDamageNumber());

// Game logic handler
entity.onHit(event -> updateHealthBar());
```

## World Events

Subscribe to global game world events:

```java
// Environment loaded
Game.world().onLoaded(env -> {
  initializeLevel();
});

// Environment unloaded
Game.world().onUnloaded(env -> {
  cleanupLevel();
});

// Camera changed
Game.world().onCameraMoved(camera -> {
  updateParallax();
});
```

## See Also

- [Default Entity Types](/docs/entity-framework/default-entity-types/) - Entity hierarchy
- [Messaging System](/docs/control-entities/messaging-system/) - Entity communication
- [Ability Framework](/docs/control-entities/ability-framework/) - Ability events
