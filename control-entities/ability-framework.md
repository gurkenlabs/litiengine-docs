---
meta.description: "Learn how to use the Ability Framework in LITIENGINE to create combat abilities with cooldowns, effects, and execution logic."
meta.keywords: "LITIENGINE, ability, combat, cooldown, effect, attack, Java"
---

# Ability Framework

The Ability Framework provides a structured way to implement combat abilities, spells, and special actions. It handles cooldowns, execution timing, and applying effects to targets.

## Basic Ability

```java
@AbilityInfo(cooldown = 500, duration = 300, value = 240)
public class Jump extends Ability {
  
  public Jump(Creature executor) {
    super(executor);
    this.addEffect(new JumpEffect(this));
  }
}
```

## AbilityInfo Annotation

Configure ability properties:

```java
@AbilityInfo(
  cooldown = 1000,              // Milliseconds between uses
  duration = 500,               // How long ability executes
  value = 100,                  // Custom value (damage, etc.)
  origin = EntityPivotType.CENTER,  // Where ability originates
  range = 200,                  // Maximum range
  multiTarget = false           // Can hit multiple targets
)
public class Fireball extends Ability {
  // ...
}
```

## Using Abilities

```java
Creature creature = ...;
Jump jumpAbility = new Jump(creature);

// Check if ability can be cast
if (jumpAbility.canCast()) {
  jumpAbility.cast();
}

// Check if currently executing
if (jumpAbility.isExecuting()) {
  // Ability in progress
}
```

## Ability Effects

Effects are applied when an ability executes:

```java
public class JumpEffect extends ForceEffect {
  
  public JumpEffect(Ability ability) {
    super(ability, ability.getAttributes().value().get(), EffectTarget.EXECUTINGENTITY);
  }
  
  @Override
  protected Force applyForce(IMobileEntity entity) {
    GravityForce force = new GravityForce(entity, getStrength(), Direction.UP);
    entity.movement().apply(force);
    return force;
  }
  
  @Override
  protected boolean hasEnded(EffectApplication appliance) {
    return super.hasEnded(appliance) || isTouchingCeiling();
  }
}
```

## Effect Targets

Define who receives the effect:

```java
// Affect the entity using the ability
EffectTarget.EXECUTINGENTITY

// Affect enemies
EffectTarget.ENEMY

// Affect all entities in range
EffectTarget.ALL
```

## Damage Abilities

Create combat abilities that deal damage:

```java
public class SwordSlash extends Ability {
  
  public SwordSlash(Creature executor) {
    super(executor);
    this.addEffect(new DamageEffect(this));
  }
}

public class DamageEffect extends Effect {
  
  public DamageEffect(Ability ability) {
    super(ability, EffectTarget.ENEMY);
  }
  
  @Override
  public void apply(IEntity entity) {
    if (entity instanceof ICombatEntity) {
      ICombatEntity target = (ICombatEntity) entity;
      int damage = getAbility().getAttributes().value().get();
      target.hit(damage);
    }
  }
}
```

## Ability Events

```java
ability.onCast(event -> {
  System.out.println("Ability cast!");
});

ability.onFinished(event -> {
  System.out.println("Ability finished!");
});
```

## Cooldown Management

```java
// Get remaining cooldown
float remaining = ability.getRemainingCooldownInSeconds();

// Check if ready
boolean ready = ability.canCast();

// Reset cooldown
ability.reset();
```

## Entity Actions

Mark methods as invokable abilities:

```java
public class Player extends Creature {
  
  @Action(description = "Perform a jump")
  public void jump() {
    if (jumpAbility.canCast()) {
      jumpAbility.cast();
    }
  }
  
  @Action(description = "Attack with sword")
  public void attack() {
    // Perform attack
  }
}

// Invoke by name
player.perform("jump");
player.perform("attack");
```

## See Also

- [Entity Controllers](/docs/control-entities/entity-controllers/) - Controller overview
- [Physics Engine](/docs/game-api/physics-engine/) - Forces and movement
- [Behavior Controller](/docs/control-entities/behavior-controller/) - AI abilities
