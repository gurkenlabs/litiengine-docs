---
title: Entity Event System
icon: lucide/zap
description: Subscribe to entity lifecycle, combat, movement, transform, and messaging events in LITIENGINE.
keywords: [LITIENGINE, entity events, EntityListener, onHit, onDeath, onMoved, EntityTransformListener, Java]
tags: [entity-events, listeners, callbacks, lifecycle, events, messaging]
---

# Entity Event System

LITIENGINE entities support an event-driven architecture through typed listener registrations. Subscribing to listeners allows reacting to entity state transitions, collisions, and lifecycles without polling loops.

---

## Lifecycle Events

### Entity Added / Removed (`EntityListener`)

Track when an entity enters or leaves the active `Environment`:

```java
entity.addListener(new EntityListener() {
  @Override
  public void loaded(IEntity entity, Environment environment) {
    System.out.println("Entity added to environment: " + entity.getName());
  }

  @Override
  public void removed(IEntity entity, Environment environment) {
    System.out.println("Entity removed from environment: " + entity.getName());
  }
});
```

### Environment-Level Entity Tracking

To monitor all entities spawned or despawned in the active scene:

```java
Game.world().environment().addEntityListener(new EnvironmentEntityListener() {
  @Override
  public void entityAdded(IEntity entity) {
    System.out.println("Spawned in environment: " + entity.getName());
  }

  @Override
  public void entityRemoved(IEntity entity) {
    System.out.println("Despawned from environment: " + entity.getName());
  }
});
```

---

## Transform & Movement Events

### Location & Size Changes (`EntityTransformListener`)

```java
entity.addTransformListener(new EntityTransformListener() {
  @Override
  public void locationChanged(IEntity entity) {
    // React to position updates
    checkForSensors(entity.getLocation());
  }

  @Override
  public void sizeChanged(IEntity entity) {
    // React to bounding box dimension changes
  }
});
```

### MobileEntity Movement Callbacks

For `Creature` or `IMobileEntity` instances with a movement controller:

```java
IMobileEntity mobile = ...;

mobile.onMoved(event -> {
  // Executes whenever velocity translates the entity position
  updateFootsteps(event.getEntity().getLocation());
});
```

---

## Combat Events (`ICombatEntity`)

### Taking Damage, Death & Resurrection

```java
ICombatEntity combatEntity = ...;

// Taking damage
combatEntity.onHit(event -> {
  double damage = event.getDamage();
  ICombatEntity attacker = event.getExecutor();

  System.out.println("Took " + damage + " damage from " + (attacker != null ? attacker.getName() : "environment"));
  playHitSound();
});

// Death (CombatEntityDeathListener receives the victim entity and the fatal hit event)
combatEntity.onDeath((victim, hitEvent) -> {
  System.out.println("Entity died: " + victim.getName());
  spawnDeathParticles(victim.getLocation());
});

// Resurrection (CombatEntityResurrectListener receives the resurrected entity)
combatEntity.onResurrect(resurrected -> {
  System.out.println("Entity revived: " + resurrected.getName());
  resurrected.setHitpoints(resurrected.getMaxHitpoints());
});
```

---

## Collision Events (`ICollisionEntity`)

```java
ICollisionEntity collisionEntity = ...;

collisionEntity.onCollision(event -> {
  ICollisionEntity other = event.getInvolvedEntity();
  if (other != null) {
    handleCollisionWith(other);
  }
});
```

---

## Animation Events (`entity.animations()`)

Access the entity's animation controller and register playback listeners via `entity.animations()`:

```java
IEntityAnimationController<?> controller = entity.animations();
if (controller != null) {
  controller.addListener(new AnimationListener() {
    @Override
    public void played(Animation animation) {
      // Triggered when an animation track begins playing
    }

    @Override
    public void finished(Animation animation) {
      // Triggered when a non-looping animation track completes
      if ("attack".equals(animation.getName())) {
        onAttackCompleted();
      }
    }
  });
}
```

---

## Trigger Events (`Trigger`)

```java
Trigger trigger = ...;

trigger.addActivatedListener(event -> {
  IEntity activator = event.getEntity();
  System.out.println("Trigger activated by: " + activator.getName());
  openDoor();
});

trigger.addDeactivatedListener(event -> {
  System.out.println("Entity left trigger bounds: " + event.getEntity().getName());
});
```

---

## Entity Messaging System

LITIENGINE entities can send and receive structured string messages:

```java
// Sending a message
targetEntity.sendMessage(this, "DAMAGE:25");

// Listening for incoming messages on an entity
entity.onMessage(event -> {
  String message = event.getMessage();
  Object sender = event.getSource();

  if (message != null && message.startsWith("DAMAGE:")) {
    int amount = Integer.parseInt(message.split(":")[1]);
    takeDamage(amount);
  }
});
```

---

## World Lifecycle Events

Subscribe to global environment transitions on `Game.world()`:

```java
// Environment loaded
Game.world().onLoaded(env -> {
  initializeLevel(env);
});

// Environment unloaded
Game.world().onUnloaded(env -> {
  cleanupLevel(env);
});
```

---

## See Also

- [Default Entity Types](default-entity-types.md) - Entity inheritance & base types
- [Messaging System](../control-entities/messaging-system.md) - Inter-entity communication
- [Ability Framework](../control-entities/ability-framework.md) - Combat abilities & cooldowns
