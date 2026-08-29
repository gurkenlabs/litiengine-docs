---
title: "Combat & Action Scripting"
icon: "lucide/crosshair"
description: "Script abilities, projectiles, floating combat text, and cinematics in LITIENGINE."
keywords: ["LITIENGINE", "abilities", "projectiles", "combat scripting", "floating text", "camera cutscenes"]
---

# Combat & Action Scripting

LITIENGINE provides fluent builders for creating scripted abilities, projectile trajectories, combat visual feedback, and cinematic sequences directly from scripts.

---

## 1. Scripted Abilities (`createAbility`)

Use `createAbility(name)` on any `CreatureScript` (or `ScriptedAbility.builder(name)`) to construct abilities with cooldowns, range limits, casting costs, and lambda execution actions:

```java
createAbility("Fireball")
  .range(220)
  .cooldown(1500)
  .onCast(execution -> {
    // Spawn projectile towards current target
    spawnProjectile()
      .from(host().getCenter())
      .towards(targetPoint)
      .speed(350)
      .damage(30)
      .splash(40, 15)
      .spawn();
  })
  .cast();
```

---

## 2. Scripted Projectiles (`spawnProjectile`)

`ScriptedProjectileBuilder` allows launching ballistic projectiles with custom speeds, collision boxes, pierce counts, splash damage, and expiration hooks:

```java
spawnProjectile()
  .from(host().getCenter())
  .towards(targetCreature.getCenter())
  .speed(300)
  .damage(25)
  .splash(45, 10)              // Splash radius 45px, 10 bonus splash damage
  .piercing(2)                 // Hits up to 2 enemies before expiring
  .collisionBox(8, 8)          // Custom hitbox
  .onHit((victim, hitEvent) -> {
    context().ui().floatText("-" + hitEvent.getDamage(), victim, Color.ORANGE);
  })
  .onExpire(proj -> {
    // Trigger explosion effect or sound on expire
  })
  .spawn();
```

---

## 3. Floating Combat Text & HUD Overlays

Provide instant visual feedback to players using `context().ui()` methods:

### Floating Damage Numbers in World-Space
Spawns rising, fading combat text directly over an entity:

```java
// Red damage text:
context().ui().floatText("-45", host(), Color.RED);

// Green healing text:
context().ui().floatText("+20 HP", host(), Color.GREEN);

// Custom offset, velocity, and duration:
context().ui().floatText("CRITICAL!", host().getCenter(), Color.YELLOW, 12.0f, 1500);
```

### Screen-Space HUD Text
Draws static text anchored to screen coordinates (useful for scores, wave counters, or debug info):

```java
context().ui().drawScreenText("SCORE: " + score, 16, 24, Color.WHITE);
context().ui().drawScreenText("WAVE: 3 / 10", 16, 44, Color.YELLOW);
```

### Announcement Banners
Displays centered animated title and subtitle banners for level start, stage clear, or boss introduction:

```java
context().ui().showBanner("BOSS INCOMING", "The Shadow Dragon Awakens", 4000);
```

---

## 4. Camera Cinematics & Sequences

Direct cinematic camera movements and cutscenes using `context().sequence()`:

```java
// Pan camera smoothly to boss, zoom in, and shake screen:
context().sequence()
  .then(() -> context().sequence().cameraPanTo(bossEntity, 60))
  .waitFor(1000)
  .then(() -> context().sequence().cameraZoom(1.5f, 500))
  .waitFor(500)
  .then(() -> context().sequence().screenShake(8.0f, 30, 20))
  .waitFor(1500)
  .then(() -> context().sequence().cameraZoom(1.0f, 500))
  .play();
```
