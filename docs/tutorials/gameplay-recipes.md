---
title: "Gameplay Recipes & Cookbook"
icon: "lucide/utensils"
description: "Practical code examples and recipes for common 2D game mechanics in LITIENGINE - camera shake, damage numbers, enemy aggro, abilities, and portals."
keywords: ["LITIENGINE recipes", "cookbook", "camera shake", "damage numbers", "enemy ai", "ability cooldown", "portal transition", "floating text", "Java 2D game"]
tags: ["recipes", "cookbook", "gameplay", "camera-shake", "damage-text", "abilities", "particles", "portals", "ai"]
---

# Gameplay Recipes & Cookbook

A curated collection of practical code examples illustrating common 2D game mechanics in LITIENGINE. Adapt these patterns to your project's architecture, entity definitions, and target version.

---

## 1. Screen Shake on Hit

Add impact to explosions, heavy attacks, or damage events by shaking the camera:

```java title="CameraShakeRecipe.java"
package com.example.game.recipes;

import de.gurkenlabs.litiengine.Game;

public class CameraShakeRecipe {
  /**
   * Shakes the active camera viewport.
   *
   * @param intensity Maximum pixel offset delta (e.g. 4.0 - 12.0)
   * @param durationMs Duration of shake effect in milliseconds (e.g. 200 - 500)
   */
  public static void triggerScreenShake(double intensity, int durationMs) {
    Game.world().camera().shake(intensity, -1, durationMs);
  }
}
```

---

## 2. Floating Combat Damage Numbers

Spawn floating damage numbers that rise and fade when an entity is struck:

```java title="DamageTextRecipe.java"
package com.example.game.recipes;

import de.gurkenlabs.litiengine.Game;
import de.gurkenlabs.litiengine.entities.ICombatEntity;
import de.gurkenlabs.litiengine.graphics.emitters.Emitter;
import de.gurkenlabs.litiengine.graphics.emitters.particles.Particle;
import de.gurkenlabs.litiengine.graphics.emitters.particles.TextParticle;
import java.awt.Color;
import java.awt.geom.Point2D;

public class DamageTextRecipe {
  public static void registerDamageTextListener(ICombatEntity entity) {
    entity.onHit(event -> {
      double damageTaken = event.getDamage();
      Point2D location = entity.getCenter();

      // Spawn a floating text particle via a dedicated emitter
      Emitter emitter = new Emitter(location.getX(), location.getY() - 10) {
        @Override
        protected Particle createNewParticle() {
          TextParticle textParticle = new TextParticle("-" + (int) damageTaken);
          textParticle.setColor(event.wasKilled() ? Color.RED : Color.YELLOW);
          textParticle.setVelocityY(-0.8f); // Float upwards
          textParticle.setTimeToLive(800);  // Lifetime in ms
          return textParticle;
        }
      };
      emitter.data().setEmitterDuration(800);
      emitter.data().setMaxParticles(1);
      emitter.data().setSpawnAmount(1);
      Game.world().environment().add(emitter);
      emitter.activate();
    });
  }
}
```

---

## 3. Portal & Level Transition Triggers

Trigger level transitions when the player walks into a map doorway or teleporter:

```java title="LevelTransitionRecipe.java"
package com.example.game.recipes;

import de.gurkenlabs.litiengine.Game;
import de.gurkenlabs.litiengine.entities.IEntity;
import de.gurkenlabs.litiengine.entities.Spawnpoint;
import de.gurkenlabs.litiengine.entities.Trigger;

public class LevelTransitionRecipe {
  public static void setupPortal(Trigger portalTrigger, String targetMapName, String targetSpawnpoint) {
    portalTrigger.addActivatedListener(event -> {
      IEntity player = event.getEntity();
      if (player != null && "player".equals(player.getName())) {
        // Fade out and load the target environment
        Game.window().getRenderComponent().fadeOut(300);
        Game.loop().perform(350, () -> {
          Game.world().loadEnvironment(targetMapName);
          Spawnpoint spawn = Game.world().environment().getSpawnpoint(targetSpawnpoint);
          if (spawn != null) {
            spawn.spawn(player);
          }
          Game.window().getRenderComponent().fadeIn(300);
        });
      }
    });
  }
}
```

---

## 4. Cooldown-Based Attack Ability

Implement an attack skill with cooldown tracking and visual range validation:

```java title="FireballAbilityRecipe.java"
package com.example.game.recipes;

import de.gurkenlabs.litiengine.Game;
import de.gurkenlabs.litiengine.abilities.Ability;
import de.gurkenlabs.litiengine.abilities.AbilityInfo;
import de.gurkenlabs.litiengine.abilities.CastType;
import de.gurkenlabs.litiengine.entities.Creature;
import de.gurkenlabs.litiengine.resources.Resources;
import de.gurkenlabs.litiengine.sound.Sound;

@AbilityInfo(
    name = "Fireball",
    cooldown = 1500, // 1.5 second cooldown
    duration = 300,
    range = 180,
    castType = CastType.ONCONFIRM
)
public class FireballAbilityRecipe extends Ability {
  public FireballAbilityRecipe(Creature executor) {
    super(executor);

    // Play casting sound effect upon cast
    this.onCast(event -> {
      Sound sound = Resources.sounds().get("audio/sfx/fireball.wav");
      if (sound != null) {
        Game.audio().playSound(sound, executor);
      }
    });
  }
}
```

---

## 5. Simple Distance-Based Enemy Aggro AI

An enemy behavior controller that steers toward the player when they enter detection range:

```java title="EnemyAggroRecipe.java"
package com.example.game.recipes;

import de.gurkenlabs.litiengine.Game;
import de.gurkenlabs.litiengine.entities.Creature;
import de.gurkenlabs.litiengine.entities.IEntity;
import de.gurkenlabs.litiengine.entities.behavior.EntityController;
import de.gurkenlabs.litiengine.util.geom.GeometricUtilities;

public class EnemyAggroRecipe extends EntityController<Creature> {
  private static final double AGGRO_RADIUS = 150.0;

  public EnemyAggroRecipe(Creature enemy) {
    super(enemy);
  }

  @Override
  public void update() {
    IEntity player = Game.world().environment().get("player");
    if (player == null || getEntity().isDead()) {
      return;
    }

    double distance = getEntity().getCenter().distance(player.getCenter());
    if (distance <= AGGRO_RADIUS) {
      // Calculate rotation angle towards player and move creature via physics engine
      double angle = GeometricUtilities.calcRotationAngleInDegrees(getEntity().getCenter(), player.getCenter());
      Game.physics().move(getEntity(), angle, getEntity().getTickVelocity());
    }
  }
}
```

---

## 6. 2D Positional Audio with Falloff

Play audio sound effects whose volume automatically attenuates based on distance from the player camera:

```java title="PositionalAudioRecipe.java"
package com.example.game.recipes;

import de.gurkenlabs.litiengine.Game;
import de.gurkenlabs.litiengine.entities.IEntity;
import de.gurkenlabs.litiengine.resources.Resources;
import de.gurkenlabs.litiengine.sound.Sound;

public class PositionalAudioRecipe {
  public static void playPositionalSfx(String soundPath, IEntity sourceEntity) {
    Sound sound = Resources.sounds().get(soundPath);
    if (sound != null) {
      // Audio engine automatically calculates volume falloff based on camera distance
      Game.audio().playSound(sound, sourceEntity);
    }
  }
}
```

---

## 7. Particle Explosion on Entity Death

Create a visual explosion when an entity is defeated:

```java title="DeathExplosionRecipe.java"
package com.example.game.recipes;

import de.gurkenlabs.litiengine.Game;
import de.gurkenlabs.litiengine.entities.ICombatEntity;
import de.gurkenlabs.litiengine.graphics.emitters.Emitter;
import de.gurkenlabs.litiengine.graphics.emitters.particles.Particle;
import de.gurkenlabs.litiengine.graphics.emitters.particles.RectangleParticle;
import java.awt.Color;
import java.awt.geom.Point2D;

public class DeathExplosionRecipe {
  public static void registerExplosionOnDeath(ICombatEntity entity) {
    entity.onDeath((victim, hitEvent) -> {
      Point2D center = victim.getCenter();
      Emitter emitter = new Emitter(center.getX(), center.getY()) {
        @Override
        protected Particle createNewParticle() {
          RectangleParticle particle = new RectangleParticle(4, 4);
          particle.setColor(Color.ORANGE);
          particle.setTimeToLive(500);
          return particle;
        }
      };
      emitter.data().setEmitterDuration(600);
      emitter.data().setMaxParticles(15);
      emitter.data().setSpawnAmount(15);
      Game.world().environment().add(emitter);
      emitter.activate();
    });
  }
}
```

---

## Related Documentation

<div class="grid cards" markdown>

- :material-robot-outline:{ .lg .middle } **[AI-Assisted Game Development](ai-game-development.md)**

    ---

    Pair with AI tools to generate custom mechanics and controllers.

- :material-gamepad-variant-outline:{ .lg .middle } **[Top-Down Shooter Tutorial](topdown-shooter.md)**

    ---

    Complete step-by-step game tutorial building movement, projectiles, and enemy waves.

- :material-book-open-page-variant:{ .lg .middle } **[API Quick Reference](../getting-started/api-quick-reference.md)**

    ---

    Core engine method and class cheat sheet.

</div>
