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

- :material-cube-outline:{ .lg .middle } **[Default Entity Types](/entity-framework/default-entity-types/)**

    ---

    Complete overview of built-in classes: `Creature`, `Prop`, `Trigger`, `Spawnpoint`, `CollisionBox`, and `LightSource`.

- :material-tag-outline:{ .lg .middle } **[Annotations & Matrix](/entity-framework/annotations/)**

    ---

    Declarative metadata (`@EntityInfo`, `@CollisionInfo`, `@MovementInfo`, `@CombatInfo`) and the Entity Architecture Matrix.

- :material-wrench-outline:{ .lg .middle } **[Custom Entities](/entity-framework/custom-entities/)**

    ---

    Subclassing base entities, registering custom XML loaders, and binding specialized behaviors.

- :material-bell-ring-outline:{ .lg .middle } **[Entity Events & Listeners](/entity-framework/entity-events/)**

    ---

    Lifecycle callbacks: `onMoved`, `onHit`, `onDeath`, `onCollision`, and custom message dispatching.

</div>
