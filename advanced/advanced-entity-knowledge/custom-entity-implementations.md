---
meta.description: "Learn how to create custom entity implementations in LITIENGINE with specialized behavior."
meta.keywords: "LITIENGINE, custom entity, implementation, extend, Java"
---

# Custom Entity Implementations

While LITIENGINE provides built-in entity types like `Creature`, `Prop`, and `CombatEntity`, you'll often need custom implementations for specialized game objects.

## Extending Existing Types

The easiest approach is to extend an existing entity type:

```java
@EntityInfo(width = 32, height = 32)
@MovementInfo(velocity = 50)
@CombatInfo(hitpoints = 100)
public class Player extends Creature {
  
  private int experience;
  private List<Ability> abilities;
  
  public Player() {
    super("player");
    this.abilities = new ArrayList<>();
  }
  
  public void addExperience(int xp) {
    this.experience += xp;
    checkLevelUp();
  }
  
  public int getExperience() {
    return experience;
  }
  
  private void checkLevelUp() {
    // Level up logic
  }
}
```

## Creating from Scratch

For unique behaviors, extend `Entity` directly:

```java
@EntityInfo(width = 64, height = 64)
public class Portal extends Entity implements IUpdateable {
  
  private String targetMap;
  private String targetSpawnpoint;
  private boolean active;
  
  public Portal() {
    super("portal");
    Game.loop().attach(this);
  }
  
  @Override
  public void update() {
    if (!active) return;
    
    // Check for player collision
    Player player = Player.instance();
    if (this.getBoundingBox().contains(player.getCenter())) {
      teleport(player);
    }
  }
  
  private void teleport(Player player) {
    Game.world().loadEnvironment(targetMap);
    Game.world().environment().getSpawnpoint(targetSpawnpoint).spawn(player);
  }
  
  public void setTarget(String map, String spawnpoint) {
    this.targetMap = map;
    this.targetSpawnpoint = spawnpoint;
  }
  
  @Override
  public void dispose() {
    Game.loop().detach(this);
    super.dispose();
  }
}
```

## Overriding Controller Creation

Control which controllers your entity uses:

```java
public class FlyingEnemy extends Creature {
  
  @Override
  protected IMovementController createMovementController() {
    // Use custom flying movement
    return new FlyingMovementController<>(this);
  }
  
  @Override
  protected IEntityAnimationController<?> createAnimationController() {
    // Custom animation logic
    return new FlyingAnimationController(this);
  }
}
```

## Custom Rendering

Override rendering for unique visual effects:

```java
public class Ghost extends Creature {
  
  @Override
  public void render(Graphics2D g) {
    // Set ghost effect
    Composite old = g.getComposite();
    g.setComposite(AlphaComposite.getInstance(AlphaComposite.SRC_OVER, 0.5f));
    
    super.render(g);
    
    g.setComposite(old);
  }
}
```

## See Also

- [Default Entity Types](/docs/entity-framework/default-entity-types/) - Built-in types
- [Entity Controllers](/docs/control-entities/entity-controllers/) - Controller system
- [Custom MapObjectLoaders](/docs/advanced/custom-mapobjectloaders/) - Loading from maps
