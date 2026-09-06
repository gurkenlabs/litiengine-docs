---
title: Ability Framework
icon: lucide/swords
description: Learn how to use the Ability Framework in LITIENGINE to create combat
  abilities with cooldowns, effects, and execution logic.
keywords: [LITIENGINE, ability, combat, cooldown, effect, attack, Java]
tags: [abilities, spells, skills, combat, cooldowns, effects]
---
# Ability Framework

## Ability API Method Reference

| Method Signature | Return Type | Description |
| :--- | :--- | :--- |
| `cast()` | `boolean` | Executes the ability if not on cooldown; returns `true` on success. |
| `canCast()` | `boolean` | Checks if the ability is off cooldown and executor has required resources. |
| `getRemainingCooldown()` | `int` | Returns remaining cooldown duration in milliseconds. |
| `getExecutor()` | `Creature` | Returns the entity executing the ability. |
| `getAttributes()` | `AbilityAttributes` | Returns configured cooldown, range, and impact duration attributes. |
| `addEffect(IEffect effect)` | `void` | Attaches a modular status or damage effect applied on impact. |

---

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
cooldown = 1000, // Milliseconds between uses
duration = 500, // How long ability executes
value = 100, // Custom value (damage, etc.)
origin = EntityPivotType.CENTER, // Where ability originates
range = 200, // Maximum range
multiTarget = false // Can hit multiple targets
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
    super(
      new ExecutingEntityTargetingStrategy(),
      ability.getExecutor(),
      ability.getAttributes().value().get().floatValue(),
      ability.getAttributes().duration().getModifiedValue()
    );
  }

  @Override
  protected Force createForce(IMobileEntity entity) {
    return new GravityForce(entity, getStrength(), Direction.UP);
  }

  @Override
  protected boolean hasEnded(EffectApplication appliance) {
    return super.hasEnded(appliance) || isTouchingCeiling();
  }
}
```

## Targeting Strategies

In LITIENGINE, effects select their targets using implementations of `TargetingStrategy`:

```java
// Affect only the entity casting the ability
new ExecutingEntityTargetingStrategy()

// Affect hostile enemy combat entities
new EnemyTargetingStrategy()

// Affect friendly/allied entities
new FriendlyTargetingStrategy()

// Affect other entities (excluding the executor)
new OtherEntityTargetingStrategy()

// Custom lambda / predicate targeting
new CustomTargetingStrategy((executor, entity) -> entity.hasTag("burnable"))
```

## Damage Abilities

Create combat abilities that deal damage:

```java
public class SwordSlash extends Ability {

  public SwordSlash(Creature executor) {
    super(executor);
    this.addEffect(new SwordSlashEffect(this));
  }
}

public class SwordSlashEffect extends AbilityEffect {

  public SwordSlashEffect(Ability ability) {
    super(new EnemyTargetingStrategy(), ability);
  }

  @Override
  public void apply(ICombatEntity target) {
    super.apply(target);
    int damage = getAbility().getAttributes().value().get();
    target.hit(damage, getAbility());
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

- [Entity Controllers](entity-controllers.md) - Controller overview
- [Physics Engine](../game-api/physics-engine.md) - Forces and movement
- [Behavior Controller](behavior-controller.md) - AI abilities
