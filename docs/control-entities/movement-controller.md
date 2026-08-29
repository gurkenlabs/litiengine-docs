---
title: "Movement Controller"
description: "Learn how to use MovementController in LITIENGINE to control entity movement with velocity, direction, and collision response."
keywords: ["LITIENGINE", "movement controller", "velocity", "physics", "collision", "Java"]
---

# Movement Controller

## MovementController API Method Reference

| Method Signature | Return Type | Description |
| :--- | :--- | :--- |
| `setVelocity(double velocity)` | `void` | Sets the base movement speed of the controlled entity. |
| `applyForce(Point2D target, double strength)` | `void` | Applies a continuous directional force vector towards target. |
| `applyForce(double angle, double strength)` | `void` | Applies a directional force vector along an angle in degrees. |
| `onMoved(Consumer<MovementEvent> c)` | `void` | Registers a listener invoked every time the entity moves. |
| `getVelocity()` | `double` | Returns the current movement velocity. |
| `dx()` / `dy()` | `double` | Returns the current frame delta displacement along X and Y. |

---

The `MovementController` handles entity movement, including velocity, acceleration, direction, and collision response. It's the bridge between input/behavior systems and the physics engine.

## Basic Movement

### Direction-based Movement

```java
// Move entity in a direction (angle in degrees)
// 0 = right, 90 = down, 180 = left, 270 = up
Game.physics().move(entity, 90, entity.getVelocity());

// Move toward a target location
entity.movement().moveTo(targetLocation);
```

### Velocity

```java
// Set velocity directly
entity.setVelocity(100); // pixels per second

// Get current velocity
float speed = entity.getVelocity();

// Acceleration/deceleration
entity.setAcceleration(50);
entity.setDeceleration(50);
```

## Movement Direction Vectors

The controller tracks current movement direction:

```java
// Get/set movement direction
float dx = entity.movement().getDx(); // -1 to 1 (left to right)
float dy = entity.movement().getDy(); // -1 to 1 (up to down)

// Set direction manually
entity.movement().setDx(1);  // Move right
entity.movement().setDy(0);  // No vertical movement
```

## KeyboardEntityController

The built-in controller for keyboard-based movement:

```java
public class Player extends Creature {
  
  @Override
  protected IMovementController createMovementController() {
    KeyboardEntityController<Player> controller = new KeyboardEntityController<>(this);
    
    // Customize keys (default: arrow keys)
    controller.addUpKey(KeyEvent.VK_W);
    controller.addDownKey(KeyEvent.VK_S);
    controller.addLeftKey(KeyEvent.VK_A);
    controller.addRightKey(KeyEvent.VK_D);
    
    return controller;
  }
}
```

## PlatformingMovementController

For platformer-style movement with gravity:

```java
@Override
protected IMovementController createMovementController() {
  return new PlatformingMovementController<>(this);
}
```

Supports:

- Horizontal movement only
- Jumping via @Action annotated methods
- Gravity applied by PhysicsEngine

## Forces

Apply forces for physics-based movement:

```java
// Apply a one-time impulse
entity.movement().apply(new Force(entity, 100, Direction.RIGHT));

// Apply gravity force (continuous)
GravityForce gravity = new GravityForce(entity, 120, Direction.DOWN);
entity.movement().apply(gravity);
```

## Movement Events

```java
// When entity moves
entity.onMoved(e -> {
  System.out.println("Entity moved to: " + entity.getLocation());
});
```

## Collision During Movement

The PhysicsEngine handles collision response during movement:

```java
// Entity will stop at collision boundaries
Game.physics().move(entity, direction, distance);

// Check if touching ground (for platformers)
entity.isTouchingGround();
```

## Creating Custom Movement Controllers

```java
public class AStarMovementController extends MovementController<Creature> {
  
  private Queue<Point2D> path;
  
  public AStarMovementController(Creature entity) {
    super(entity);
  }
  
  @Override
  public void update() {
    if (path == null || path.isEmpty()) {
      return;
    }
    
    Point2D target = path.peek();
    if (getEntity().getLocation().distance(target) < 5) {
      path.poll();
      return;
    }
    
    // Move toward current waypoint
    double angle = getEntity().getAngleTo(target);
    Game.physics().move(getEntity(), angle, getEntity().getVelocity());
  }
  
  public void setPath(Queue<Point2D> path) {
    this.path = path;
  }
}
```

## Stopping Movement

```java
// Stop all movement
entity.movement().stop();

// Clear all active forces
entity.movement().clearForces();
```

## See Also

- [Entity Controllers](entity-controllers.md) - Controller overview
- [Physics Engine](../game-api/physics-engine.md) - Collision and physics
- [Behavior Controller](behavior-controller.md) - AI movement
