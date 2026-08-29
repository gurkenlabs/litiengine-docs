---
meta.description: Documentation of LITIENGINE's physics engine.
meta.keywords: LITIENGINE, physics, movement, collision, entities, listeners
---

# 2D Physics
The PhysicsEngine provides functionality for simulating and handling physics interactions in your game. It holds collections of all  Collision Entities in your Environment and allows you to define and manage physical properties such as collision detection for shapes and entities, gravity, forces, and movement. Here's an overview of how you can use the PhysicsEngine in LITIENGINE through the `Game.physics()` method:

## Creating collision entities:
In order to make Entities interact with physics, they need to extend the `CollisionEntity` class. `CollisionBox`, `Creature`, `Prop`, and `Trigger` are the built-in entity types supporting physics simulation by default. Collision entities can e.g. manage their collision box properties, register collision listeners, or filter potential collision candidates by having a specific `Collision` type.

The `CollisionEntity` constructor will attempt to register the entity in the PhysicsEngine automatically.
If you ever need to register entities manually in the PhysicsEngine, use `Game.physics().add(ICollisionEntity e);`. Similarly, you can deregister entities using `Game.physics().remove(ICollisionEntity e);`.

If a collision entity is registered in the Physics engine and moved by it (rather than explicitly setting its X and Y coordinates), the `PhysicsEngine` will resolve potential collisions automatically and interrupt the moving accordingly.

## Collision types
```java
Prop p;
// [...]
// Only let the prop react to STATIC Collision.
p.setCollisionType(Collision.STATIC);
```
### *ANY*
Entities / Particles with this Collision type will react to collisions with ANY colliding object.
### *DYNAMIC*
Entities / Particles with this Collision type will react to collisions with moving objects only. Since the collisions have to be computed in every tick, this is more costly than STATIC collision.
### *NONE*
Entities / Particles with this Collision type do not react to collisions at all. This is equal to (temporarily) disabling physics for an entity.
### *STATIC*
Entities / Particles with this Collision type will react to collisions with static objects only. This is used for level architecture that does not move throughout the game.

## Forces and Movement
If you need a non-static collision entity that can also move, you will be using the `IMobileEntity` implementations.
The crucial difference between Props and Creatures is that the latter can be moved by the physics engine due to also being an `IMobileEntity`.
An `IMobileEntity` has movement properties such as velocity, acceleration, and deceleration. Most importantly, mobile entities have an `IMovementController` that you can access with `IMobileEntity.movement()`. Instead of having to apply all relevant forces, movement, and collisions by hand, the movement controller will take care of adding the forces accordingly, moving at the given speed and direction, and reacting to collisions.
If you want to apply a force to an entity's movement controller, it can be done like this:
```java
Creature c;
// [...]

// Instantiate gravity force pulling upwards.
GravityForce force = new GravityForce(c, 2f, Direction.UP);
// Apply gravity force to creature movement.
c.movement().apply(force);

```

You can also move entities directly with the physics engine using `Game.physics().move(IMobileEntity)`.

## Collision Listeners
The `CollisionEvent` class allows you to listen for specific types of collisions. To register a Collision listener on a Prop, for example, we can use the following logic:
```java
Prop p;
// [...]
p.onCollision(event -> {
    // Our prop is the source of the CollisionEvent.
    System.out.println("Source: " + event.getSource().getName());
    // getInvolvedEntities returns the list of all colliding entities.
    event.getInvolvedEntities().forEach(e -> {
        System.out.println("Involved entity: " + e.getName());
    });
});
```

## Ray casting
The physics engine can not only determine direct collision, but also cast rays from a given source point to a target, detecting collision in the way.
Use the different overloads of `Game.physics().raycast(...)` to cast a ray from point A to point B and detect whether anything collides with the ray.

## Enabling / disabling physics updates
The physics engine is tied to your game loop. When you call `Game.init()` at startup, you implicitly attach the physics engine to the Game loop, letting it update all physics in your game world on every tick. The PhysicsEngine is an `IUpdateable`, i.e. you can attach and detach it to any Loop using `Loop.attach(Game.physics())` and `Loop.detach(Game.physics())`.

