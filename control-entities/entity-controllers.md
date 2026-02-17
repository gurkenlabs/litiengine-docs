---
meta.description: "Learn about Entity Controllers in LITIENGINE - how to control entity behavior with animation, movement, and custom controllers."
meta.keywords: "LITIENGINE, entity controller, animation, movement, behavior, Java"
---

# Entity Controllers

Entity Controllers are the primary mechanism for defining how entities behave in LITIENGINE. Each controller manages a specific aspect of an entity's functionality, such as animation, movement, or AI behavior.

## Controller Architecture

Controllers implement the `IEntityController` interface and are attached to entities. The engine provides several built-in controller types:

- **AnimationController** - Manages spritesheet animations
- **MovementController** - Handles entity movement
- **BehaviorController** - Controls AI and state machines

### Adding Controllers to Entities

```java
public class Player extends Creature {
  
  public Player() {
    super("player");
    
    // Add custom controller
    this.addController(new MyCustomController(this));
  }
  
  @Override
  protected IMovementController createMovementController() {
    return new KeyboardEntityController<>(this);
  }
}
```

### The Controller Lifecycle

Controllers are automatically attached to the game loop when added to an entity:

```java
public interface IEntityController extends IUpdateable {
  void attach();
  void detach();
  IEntity getEntity();
}
```

## Built-in Controller Types

### AnimationController

Controls which spritesheet animation is displayed for an entity. See [Animation Controller](/docs/control-entities/animation-controller/) for details.

### MovementController

Handles entity movement, including velocity, direction, and collision response. See [Movement Controller](/docs/control-entities/movement-controller/) for details.

### BehaviorController / StateController

Manages AI behavior and state machines. See [Behavior Controller](/docs/control-entities/behavior-controller/) for details.

## Creating Custom Controllers

Extend `EntityController` for custom behavior:

```java
public class MyCustomController extends EntityController<MyEntity> {
  
  public MyCustomController(MyEntity entity) {
    super(entity);
  }
  
  @Override
  public void update() {
    // Called every tick while attached
    MyEntity entity = getEntity();
    
    // Custom logic here
    if (entity.isAlive()) {
      performCustomBehavior();
    }
  }
  
  private void performCustomBehavior() {
    // Custom behavior implementation
  }
}
```

## Overriding Default Controllers

Entities can override which controllers are created:

```java
@EntityInfo(width = 32, height = 32)
public class FlyingEnemy extends Creature {
  
  public FlyingEnemy() {
    super("flying-enemy");
  }
  
  @Override
  protected IMovementController createMovementController() {
    // Use custom flying movement instead of default
    return new FlyingMovementController<>(this);
  }
  
  @Override
  protected IEntityAnimationController<?> createAnimationController() {
    // Custom animation controller
    return new FlyingEnemyAnimationController(this);
  }
}
```

## Accessing Controllers

```java
// Get specific controller type
MovementController movement = entity.getController(MovementController.class);

// Get animation controller
IEntityAnimationController<?> anim = entity.getAnimationController();

// Get all controllers
List<IEntityController> controllers = entity.getControllers();
```

## Controller Events

Controllers can define and fire custom events:

```java
public class CombatController extends EntityController<Creature> {
  
  public void attack() {
    // Perform attack
    fireAttackEvent();
  }
  
  private void fireAttackEvent() {
    // Notify listeners
    getEntity().getListeners().forEach(l -> l.onAttack());
  }
}
```

## See Also

- [Animation Controller](/docs/control-entities/animation-controller/) - Animation management
- [Movement Controller](/docs/control-entities/movement-controller/) - Movement handling
- [Behavior Controller](/docs/control-entities/behavior-controller/) - AI and state machines
- [Ability Framework](/docs/control-entities/ability-framework/) - Combat abilities
