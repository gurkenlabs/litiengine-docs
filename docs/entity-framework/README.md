---
title: "Entity Framework"
icon: "lucide/box"
description: "Comprehensive guide to LITIENGINE's Entity Component System: Creature, Prop, Trigger, Annotations, and Custom Entity loaders."
keywords: ["LITIENGINE", "entity framework", "Creature", "Prop", "Trigger", "CollisionEntity", "annotations", "custom entities"]
tags: ["entity-framework", "entities", "creatures", "props", "triggers", "annotations"]
---

# Entity Framework

Entities represent all interactive, physical, or visual objects living within a game `Environment`. The entity system provides spatial indexing, life cycles, message dispatching, and declarative metadata configuration.

---

## Entity System Documentation Sections

<div class="grid cards" markdown>

- :lucide-box:{ .lg .middle } **[Default Entity Types](default-entity-types.md)**

    ---

    Complete overview of built-in classes: `Creature`, `Prop`, `Trigger`, `Spawnpoint`, `CollisionBox`, and `LightSource`.

- :lucide-tag:{ .lg .middle } **[Annotations & Matrix](annotations.md)**

    ---

    Declarative metadata (`@EntityInfo`, `@CollisionInfo`, `@MovementInfo`, `@CombatInfo`) and the Entity Architecture Matrix.

- :lucide-wrench:{ .lg .middle } **[Custom Entities](custom-entities.md)**

    ---

    Subclassing base entities, registering custom XML loaders, and binding specialized behaviors.

- :lucide-zap:{ .lg .middle } **[Entity Events & Listeners](entity-events.md)**

    ---

    Lifecycle callbacks: `onMoved`, `onHit`, `onDeath`, `onCollision`, and custom message dispatching.

</div>

---

## Spatial Entity Queries (`EntityQuery`)

To find, filter, and sort entities within an environment without writing repetitive stream filters or distance calculations, use `environment.query(Class)`:

```java
// Find closest living enemy within 250px
Optional<Creature> target = Game.world().environment()
    .query(Creature.class)
    .alive()
    .enemyOf(player)
    .within(player.getCenter(), 250)
    .nearestTo(player.getCenter())
    .first();
```

See **[Fluent Entity Queries](../game-api/game-world.md#fluent-entity-queries-entityquery)** in the Game World guide for a complete method reference.

