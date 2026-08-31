---
title: "2D Physics & Spatial Quadtrees"
icon: "lucide/atom"
description: "Master LITIENGINE's 2D physics engine: spatial quadtree indexing, collision boxes, line-of-sight raycasting, force vectors, and knockback mechanics."
keywords: ["LITIENGINE physics", "collision detection", "spatial quadtree", "raycast", "knockback", "GravityForce", "CollisionType", "Game.physics"]
tags: ["physics", "collision", "gravity", "velocity", "quadtree", "raycasting", "forces"]
---

# 2D Physics & Spatial Quadtrees

The **PhysicsEngine** (`Game.physics()`) handles 2D collision detection, velocity resolution, physical forces, and spatial indexing. It uses optimized **spatial quadtrees** to maintain a steady 60 FPS update rate even with hundreds of colliders.

---

## Physics Engine Method Reference

| Method | Return Type | Description |
|:---|:---|:---|
| `add(ICollisionEntity entity)` | `void` | Registers a collision entity in the physics quadtree. |
| `remove(ICollisionEntity entity)` | `void` | Deregisters an entity from the physics world. |
| `move(IMobileEntity entity, double angle, double delta)` | `boolean` | Moves a mobile entity along a heading while resolving obstacle sliding. |
| `raycast(Point2D start, Point2D end, RaycastType type)` | `RaycastHit` | Casts a line segment through the world to detect obstructing colliders. |
| `getCollisionEntities(Shape area)` | `Collection<ICollisionEntity>` | Returns all solid entities overlapping a spatial area (circle, rectangle). |
| `collides(Shape shape)` | `boolean` | Checks if a shape intersects any solid physics geometry. |

---

## Collision Entities & Types

Entities inheriting from `CollisionEntity` (`Creature`, `Prop`, `CollisionBox`, `Trigger`) are automatically registered in the physics simulation.

```java title="CollisionSetup.java"
Prop rock = new Prop(100, 150, "rock");

// 1. Enable solid physics collision
rock.setCollision(true);
rock.setCollisionBoxWidth(24);
rock.setCollisionBoxHeight(16);
rock.setCollisionBoxAlign(Align.CENTER);
rock.setCollisionBoxValign(Valign.DOWN);

// 2. Set collision filtering type
rock.setCollisionType(Collision.STATIC);
```

### Collision Types

| `Collision` Type | Performance Impact | Behavior & Use Case |
|:---|:---|:---|
| `STATIC` | High Performance | Stationary level architecture (walls, cliffs, trees, buildings). Spatial quadtree caches bounds statically. |
| `DYNAMIC` | Normal Tick Check | Moving entities (player, enemies, projectiles, movable crates). Evaluated on every physics tick. |
| `ANY` | Normal Tick Check | Reacts to both static architecture and moving entities. |
| `NONE` | Zero Physics Check | Physics disabled (ghost mode, intangible sensors). |

---

## Line-of-Sight Raycasting

Raycasting allows AI enemies to check if a player is visible or if line-of-sight is blocked by walls:

```java title="EnemyLineOfSight.java"
package com.example.game.ai;

import de.gurkenlabs.litiengine.Game;
import de.gurkenlabs.litiengine.entities.Creature;
import de.gurkenlabs.litiengine.physics.RaycastHit;
import de.gurkenlabs.litiengine.physics.RaycastType;
import java.awt.geom.Point2D;

public class EnemyVision {
  public static boolean canSeeTarget(Creature enemy, Creature target) {
    Point2D start = enemy.getCenter();
    Point2D end = target.getCenter();

    // Cast a ray from enemy to target checking for solid obstacles
    RaycastHit hit = Game.physics().raycast(start, end, RaycastType.STATIC);

    // If ray reached the target without hitting a solid wall, line of sight is clear
    return hit == null || hit.getPoint().distance(start) >= start.distance(end);
  }
}
```

---

## Knockback & Impulse Force Vectors

You can apply directional impulse forces (explosions, weapon knockback, wind currents) using `Force`:

```java title="CombatKnockback.java"
package com.example.game.combat;

import de.gurkenlabs.litiengine.Direction;
import de.gurkenlabs.litiengine.entities.Creature;
import de.gurkenlabs.litiengine.physics.Force;
import de.gurkenlabs.litiengine.physics.GravityForce;
import java.awt.geom.Point2D;

public class KnockbackApplier {
  public static void applyKnockback(Creature target, Point2D attackerCenter, float strength) {
    // 1. Calculate angle away from attacker
    double angle = attackerCenter.angle(target.getCenter());

    // 2. Create impulse force that decelerates smoothly over 30 ticks
    Force knockback = new Force(target.getCenter(), strength, (float) angle);
    knockback.setCancelOnCollision(true);

    // 3. Apply to target's movement controller
    target.movement().apply(knockback);
  }

  public static void applyGravity(Creature target, float pullStrength) {
    // Continuous gravity pull towards the bottom
    GravityForce gravity = new GravityForce(target, pullStrength, Direction.DOWN);
    target.movement().apply(gravity);
  }
}
```

---

## Spatial Area Queries (Quadtree Searches)

Query all colliders within an area (e.g. for AoE explosions or pickup radii) without looping through all world entities:

```java title="ExplosionRadius.java"
package com.example.game.combat;

import de.gurkenlabs.litiengine.Game;
import de.gurkenlabs.litiengine.entities.ICollisionEntity;
import java.awt.geom.Ellipse2D;
import java.awt.geom.Point2D;
import java.util.Collection;

public class AreaOfEffectQuery {
  public static void triggerExplosion(Point2D center, double radius) {
    // 1. Define radial explosion circle
    Ellipse2D blastArea = new Ellipse2D.Double(
        center.getX() - radius,
        center.getY() - radius,
        radius * 2,
        radius * 2
    );

    // 2. Efficiently query quadtree for overlapping collision entities
    Collection<ICollisionEntity> victims = Game.physics().getCollisionEntities(blastArea);

    victims.forEach(entity -> {
      System.out.println("Hit entity in blast: " + entity.getName());
    });
  }
}
```

---

## Collision Listeners & Callbacks

```java title="CollisionListeners.java"
Prop barrel = Game.world().environment().getProp("explosive_barrel");

if (barrel != null) {
  barrel.onCollision(event -> {
    System.out.println("Collision detected on: " + event.getSource().getName());
    event.getInvolvedEntities().forEach(other -> {
      System.out.println("Collided with: " + other.getName());
    });
  });
}
```

---

## See Also

<div class="grid cards" markdown>

- :material-walk:{ .lg .middle } **[Movement Controllers](../control-entities/movement-controller.md)**

    ---

    Steering heading, acceleration rates, and collision sliding.

- :material-tag-outline:{ .lg .middle } **[Entity Annotations & Matrix](../entity-framework/annotations.md)**

    ---

    Declarative `@CollisionInfo` setup and 2.5D feet alignment visualizer.

</div>

*[Game.physics()]: Quadtree-backed 2D collision detection and spatial queries
*[ICollisionEntity]: Entity with spatial physics bounding box
*[IMobileEntity]: Entity supporting locomotion, velocity, and force impulses
*[RaycastHit]: Intersection result containing hit point and colliding geometry
*[Force]: Directional impulse vector applied to an entity's movement controller
