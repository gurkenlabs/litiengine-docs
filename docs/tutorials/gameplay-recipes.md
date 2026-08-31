---
title: "Gameplay Recipes & Cookbook"
icon: "lucide/utensils"
description: "Quick copy-paste code recipes and solutions for common 2D game mechanics in LITIENGINE - camera shake, damage numbers, enemy aggro, abilities, and portals."
keywords: ["LITIENGINE recipes", "cookbook", "camera shake", "damage numbers", "enemy ai", "ability cooldown", "portal transition", "floating text", "Java 2D game"]
tags: ["recipes", "cookbook", "gameplay", "camera-shake", "damage-text", "abilities", "particles", "portals", "ai"]
---

# Gameplay Recipes & Cookbook

A curated collection of concise, production-ready code recipes for common 2D game mechanics. Each snippet is self-contained and designed to be dropped directly into your LITIENGINE project.

---

## 1. Screen Shake on Hit

Add visceral impact to explosions, heavy attacks, or taking damage by shaking the camera:

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
import de.gurkenlabs.litiengine.graphics.emitters.xml.TextParticle;
import java.awt.Color;
import java.awt.geom.Point2D;

public class DamageTextRecipe {
  public static void registerDamageTextListener(ICombatEntity entity) {
    entity.onHit(event -> {
      int damageTaken = event.getDamage();
      Point2D location = entity.getCenter();

      // Spawn a floating text particle above the entity
      TextParticle textParticle = new TextParticle(
          "-" + damageTaken,
          event.isCritical() ? Color.YELLOW : Color.RED,
          location.getX(),
          location.getY() - 10,
          800 // lifetime in ms
      );
      textParticle.setVelocityY(-0.8f); // Float upwards
      Game.world().environment().add(textParticle);
    });
  }
}
```

---

## 3. Portal & Level Transition Triggers

Trigger seamless level transitions when the player walks into a map doorway or teleporter:

```java title="LevelTransitionRecipe.java"
package com.example.game.recipes;

import de.gurkenlabs.litiengine.Game;
import de.gurkenlabs.litiengine.entities.IEntity;
import de.gurkenlabs.litiengine.entities.Trigger;

public class LevelTransitionRecipe {
  public static void setupPortal(Trigger portalTrigger, String targetMapName, String targetSpawnpoint) {
    portalTrigger.addEntityListener(new Trigger.TriggerListener() {
      @Override
      public void activated(Trigger.TriggerEvent event) {
        IEntity player = event.getEntity();
        if (player.getName().equals("player")) {
          // Fade out and load the target environment
          Game.window().getRenderComponent().fadeOut(300);
          Game.loop().perform(350, () -> {
            Game.world().loadEnvironment(targetMapName);
            Game.world().environment().getSpawnpoint(targetSpawnpoint).spawn(player);
            Game.window().getRenderComponent().fadeIn(300);
          });
        }
      }
    });
  }
}
```

---

## 4. Cooldown-Based Attack Ability

Implement an attack skill with cooldown tracking, casting sound, and visual range validation:

```java title="FireballAbilityRecipe.java"
package com.example.game.recipes;

import de.gurkenlabs.litiengine.abilities.Ability;
import de.gurkenlabs.litiengine.abilities.AbilityInfo;
import de.gurkenlabs.litiengine.abilities.CastType;
import de.gurkenlabs.litiengine.entities.Creature;
import de.gurkenlabs.litiengine.resources.Resources;

@AbilityInfo(
    name = "Fireball",
    cooldown = 1500, // 1.5 second cooldown
    duration = 300,
    range = 180,
    castType = CastType.ONCONFIRMATION
)
public class FireballAbilityRecipe extends Ability {
  public FireballAbilityRecipe(Creature executor) {
    super(executor);

    // Play casting sound effect upon cast
    this.onCast(event -> {
      Resources.sounds().get("audio/sfx/fireball.wav").play();
    });
  }
}
```

---

## 5. Simple Distance-Based Enemy Aggro AI

An enemy behavior controller that pursues the player when they step inside detection range:

```java title="EnemyAggroRecipe.java"
package com.example.game.recipes;

import de.gurkenlabs.litiengine.Game;
import de.gurkenlabs.litiengine.entities.Creature;
import de.gurkenlabs.litiengine.entities.IEntity;
import de.gurkenlabs.litiengine.entities.behavior.EntityController;

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
      // Pathfind and move towards the player
      getEntity().getNavigator().navigate(player.getCenter());
    } else {
      // Stop moving when player exits detection radius
      getEntity().getNavigator().stop();
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

Create a visual explosion of dust or sparks when an enemy is destroyed:

```java title="DeathExplosionRecipe.java"
package com.example.game.recipes;

import de.gurkenlabs.litiengine.Game;
import de.gurkenlabs.litiengine.entities.ICombatEntity;
import de.gurkenlabs.litiengine.graphics.emitters.Emitter;
import de.gurkenlabs.litiengine.graphics.emitters.particles.RectangleParticle;
import java.awt.Color;
import java.awt.geom.Point2D;

public class DeathExplosionRecipe {
  public static void registerExplosionOnDeath(ICombatEntity entity) {
    entity.onDeath(event -> {
      Point2D center = entity.getCenter();
      Emitter emitter = new Emitter(center.getX(), center.getY()) {
        @Override
        protected Particle createNewParticle() {
          return new RectangleParticle(4, 4, Color.ORANGE, 500);
        }
      };
      emitter.setTimeToLive(600);
      Game.world().environment().add(emitter);
    });
  }
}
```

---

## Related Documentation

<div class="grid cards" markdown>

- :material-robot-outline:{ .lg .middle } **[AI-Assisted Game Development](ai-game-development.md)**

    ---

    Pair with OpenCode, Antigravity, or Codex to generate custom mechanics and controllers.

- :material-gamepad-variant-outline:{ .lg .middle } **[2D Platformer Tutorial](2d-platformer.md)**

    ---

    Step-by-step tutorial creating jumping mechanics, coins, and enemies from scratch.

- :material-book-open-page-variant:{ .lg .middle } **[API Quick Reference](../getting-started/api-quick-reference.md)**

    ---

    Instant cheat sheet covering all engine classes, method signatures, and annotations.

</div>
