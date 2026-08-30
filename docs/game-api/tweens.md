---
title: "Tweening"
icon: "lucide/sparkles"
description: "Master LITIENGINE's TweenEngine for smooth interpolations, position/size/opacity transitions, and Robert Penner easing equations."
keywords: ["LITIENGINE", "java", "game engine", "2D", "tweening", "easing", "interpolation", "Penner equations"]
tags: ["tweens", "tweening", "interpolation", "easing", "animation", "transitions"]
---

# Tweening

The **TweenEngine** (`Game.tweens()`) provides a high-performance property interpolation framework. It allows you to animate entity positions, camera zoom, opacity, sound volume, collision box dimensions, and UI components using mathematical easing equations.

---

## Interactive Easing Curve Playground

Select an easing equation below to preview the interpolation curve and watch the live animation in real time:

<div class="interactive-card">
<div style="display: flex; gap: 1.5rem; flex-wrap: wrap; align-items: flex-start;">
<div style="flex: 1; min-width: 280px;">
<label for="tween-func-select" style="font-weight: 600; display: block; margin-bottom: 0.5rem;">Select Easing Function:</label>
<select id="tween-func-select" style="width: 100%; padding: 0.5rem; border-radius: 4px; background: var(--md-code-bg-color); color: var(--md-default-fg-color); border: 1px solid var(--md-default-fg-color--lighter);">
<option value="LINEAR">LINEAR (Constant Speed)</option>
<option value="QUAD_IN">QUAD_IN (Accelerating)</option>
<option value="QUAD_OUT" selected>QUAD_OUT (Decelerating)</option>
<option value="QUAD_INOUT">QUAD_INOUT (Smooth S-Curve)</option>
<option value="CUBIC_OUT">CUBIC_OUT (Smooth Stop)</option>
<option value="BOUNCE_OUT">BOUNCE_OUT (Physical Bouncing)</option>
<option value="ELASTIC_OUT">ELASTIC_OUT (Spring Oscillator)</option>
<option value="BACK_OUT">BACK_OUT (Overshoot & Settle)</option>
<option value="SINE_INOUT">SINE_INOUT (Gentle Wave)</option>
</select>
<div style="margin-top: 1rem;">
<button id="btn-play-tween" class="md-button md-button--primary" style="width: 100%;">Play Animation</button>
</div>
<div style="margin-top: 1rem; font-size: 0.8rem;">
<strong>Generated Java Code:</strong>
<pre style="margin-top: 0.25rem; padding: 0.5rem; border-radius: 4px; background: var(--md-code-bg-color); overflow-x: auto;"><code id="tween-code-preview">Game.tweens().begin(entity, TweenType.LOCATION_X, 1000)
    .target(400)
    .ease(TweenFunction.QUAD_OUT)
    .begin();</code></pre>
</div>
</div>
<div style="flex: 1; min-width: 280px; text-align: center;">
<canvas id="tween-canvas" width="320" height="220" style="border: 1px solid var(--md-default-fg-color--lighter); border-radius: 6px; background: var(--md-code-bg-color); max-width: 100%; height: auto;"></canvas>
<div style="font-size: 0.75rem; color: var(--md-default-fg-color--lighter); margin-top: 0.25rem;">Curve Graph & Position Preview</div>
</div>
</div>
</div>

</div>

<script>
(function() {
  function initTweenPlayground() {
    const canvas = document.getElementById('tween-canvas');
    const select = document.getElementById('tween-func-select');
    const playBtn = document.getElementById('btn-play-tween');
    const codePreview = document.getElementById('tween-code-preview');
    if (!canvas || !select || !playBtn || !codePreview) return;

    const ctx = canvas.getContext('2d');
    let progress = 1.0;
    let animId = null;
    let startTime = 0;
    const duration = 1200;

    const equations = {
      LINEAR: t => t,
      QUAD_IN: t => t * t,
      QUAD_OUT: t => t * (2 - t),
      QUAD_INOUT: t => t < 0.5 ? 2 * t * t : -1 + (4 - 2 * t) * t,
      CUBIC_OUT: t => (--t) * t * t + 1,
      BOUNCE_OUT: t => {
        const n1 = 7.5625, d1 = 2.75;
        if (t < 1 / d1) return n1 * t * t;
        if (t < 2 / d1) return n1 * (t -= 1.5 / d1) * t + 0.75;
        if (t < 2.5 / d1) return n1 * (t -= 2.25 / d1) * t + 0.9375;
        return n1 * (t -= 2.625 / d1) * t + 0.984375;
      },
      ELASTIC_OUT: t => {
        if (t === 0) return 0; if (t === 1) return 1;
        return Math.pow(2, -10 * t) * Math.sin((t * 10 - 0.75) * ((2 * Math.PI) / 3)) + 1;
      },
      BACK_OUT: t => {
        const s = 1.70158;
        return --t * t * ((s + 1) * t + s) + 1;
      },
      SINE_INOUT: t => -(Math.cos(Math.PI * t) - 1) / 2
    };

    function updateCode() {
      const funcName = select.value;
      codePreview.textContent = "Game.tweens().begin(entity, TweenType.LOCATION_X, 1000)\n    .target(400)\n    .ease(TweenFunction." + funcName + ")\n    .begin();";
    }

    function render() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      const fn = equations[select.value] || equations.LINEAR;

      // Draw Grid & Axes
      ctx.strokeStyle = "rgba(128, 128, 128, 0.2)";
      ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.moveTo(30, 20); ctx.lineTo(30, 160); ctx.lineTo(300, 160);
      ctx.stroke();

      // Draw Easing Curve
      ctx.strokeStyle = "#00b0ff";
      ctx.lineWidth = 2;
      ctx.beginPath();
      for (let x = 0; x <= 270; x++) {
        const t = x / 270;
        const val = fn(t);
        const y = 160 - val * 120;
        if (x === 0) ctx.moveTo(30 + x, y);
        else ctx.lineTo(30 + x, y);
      }
      ctx.stroke();

      // Current Animated Value
      const eased = fn(Math.min(1.0, progress));
      const currX = 30 + progress * 270;
      const currY = 160 - eased * 120;

      // Point on curve
      ctx.fillStyle = "#ff4081";
      ctx.beginPath();
      ctx.arc(currX, currY, 5, 0, Math.PI * 2);
      ctx.fill();

      // Moving Box preview at bottom
      ctx.fillStyle = "rgba(128, 128, 128, 0.15)";
      ctx.fillRect(30, 180, 270, 24);
      
      const ballX = 30 + eased * 246;
      ctx.fillStyle = "#00e676";
      ctx.fillRect(ballX, 182, 24, 20);
      ctx.fillStyle = "#ffffff";
      ctx.font = "10px sans-serif";
      ctx.fillText(Math.round(eased * 100) + "%", ballX + 2, 196);
    }

    function animate(now) {
      if (!startTime) startTime = now;
      progress = (now - startTime) / duration;
      if (progress >= 1.0) {
        progress = 1.0;
        render();
      } else {
        render();
        animId = requestAnimationFrame(animate);
      }
    }

    playBtn.addEventListener('click', function() {
      if (animId) cancelAnimationFrame(animId);
      startTime = 0;
      animId = requestAnimationFrame(animate);
    });

    select.addEventListener('change', function() {
      updateCode();
      if (animId) cancelAnimationFrame(animId);
      progress = 1.0;
      render();
    });

    updateCode();
    render();
  }

  if (typeof document$ !== 'undefined') {
    document$.subscribe(initTweenPlayground);
  } else {
    document.addEventListener('DOMContentLoaded', initTweenPlayground);
  }
})();
</script>

---

## The Tweening Engine — `Game.tweens()`

The tweening engine is a singleton manager accessed via `Game.tweens()`. It updates all active `Tween` instances during each engine update tick.

A `Tween` smoothly transitions numerical attributes from a starting value to an end value over a given duration:

```java title="TweenExample.java"
ImageComponent ic = new ImageComponent(0, 0, 100, 100);

// Smoothly move ImageComponent to (100, 200) over 4 seconds using quadratic easing
Game.tweens().begin(ic, TweenType.LOCATION_XY, 4000)
    .target(100, 200)
    .ease(TweenFunction.QUAD_INOUT)
    .begin();
```

---

## TweenType Reference

The `TweenType` enum defines all interpolatable entity and component properties:

| `TweenType` | Target Component | Interpolated Property |
|:---|:---|:---|
| `LOCATION_X` | `IEntity` / `GuiComponent` | X-coordinate map/screen position |
| `LOCATION_Y` | `IEntity` / `GuiComponent` | Y-coordinate map/screen position |
| `LOCATION_XY` | `IEntity` / `GuiComponent` | Simultaneous X and Y position coordinates |
| `SIZE_WIDTH` | `IEntity` / `GuiComponent` | Object bounding box width |
| `SIZE_HEIGHT` | `IEntity` / `GuiComponent` | Object bounding box height |
| `SIZE_BOTH` | `IEntity` / `GuiComponent` | Simultaneous width and height dimensions |
| `ANGLE` | `IEntity` | Rotation angle in degrees |
| `COLLISION_WIDTH` | `ICollisionEntity` | Physics collision box width |
| `COLLISION_HEIGHT` | `ICollisionEntity` | Physics collision box height |
| `COLLISION_BOTH` | `ICollisionEntity` | Physics collision box dimensions |
| `HITPOINTS` | `ICombatEntity` | Entity health pool (for smooth damage healthbars) |
| `VELOCITY` | `IMobileEntity` | Entity movement velocity |
| `VOLUME` | `Sound` / `SoundSource` | Audio volume multiplier ($0.0$ to $1.0$) |
| `OPACITY` | `IEntity` / `GuiComponent` | Visual alpha transparency |
| `FONTSIZE` | `GuiComponent` | Text font rendering point size |

---

## TweenFunction Reference

LITIENGINE includes Robert Penner's complete collection of mathematical easing functions:

* **Linear**: `LINEAR` (constant velocity without acceleration).
* **Quadratic ($t^2$)**: `QUAD_IN`, `QUAD_OUT`, `QUAD_INOUT` (smooth, subtle curve).
* **Cubic ($t^3$)**: `CUBIC_IN`, `CUBIC_OUT`, `CUBIC_INOUT` (pronounced acceleration/deceleration).
* **Circular**: `CIRCLE_IN`, `CIRCLE_OUT`, `CIRCLE_INOUT` (mimics circular arc momentum).
* **Sinusoidal**: `SINE_IN`, `SINE_OUT`, `SINE_INOUT` (gentle wave ease).
* **Exponential**: `EXPO_IN`, `EXPO_OUT`, `EXPO_INOUT` (fast ramp-up/down).
* **Back (Overshoot)**: `BACK_IN`, `BACK_OUT`, `BACK_INOUT` (pulls back or overshoots target before settling).
* **Bounce**: `BOUNCE_IN`, `BOUNCE_OUT`, `BOUNCE_INOUT` (simulates gravity rebounds).
* **Elastic**: `ELASTIC_IN`, `ELASTIC_OUT`, `ELASTIC_INOUT` (spring-like oscillation).

---

## Chaining & Lifecycle Listeners

```java title="TweenListeners.java"
Game.tweens().begin(player, TweenType.LOCATION_XY, 1000)
    .target(500, 300)
    .ease(TweenFunction.BOUNCE_OUT)
    .onStart(tween -> System.out.println("Tween started!"))
    .onProgress((tween, value) -> System.out.println("Progress: " + value))
    .onComplete(tween -> {
      System.out.println("Tween completed!");
      // Chain another tween or play sound effect
      Resources.sounds().get("audio/land.ogg").play();
    })
    .begin();
```

---

## See Also

<div class="grid cards" markdown>

- :material-camera-outline:{ .lg .middle } **[Camera & Viewport](/game-api/camera/)**

    ---

    Animate camera zoom and panning transitions with tweens.

- :material-cube-outline:{ .lg .middle } **[Entity Framework](/entity-framework/README/)**

    ---

    Overview of interpolatable entities, creatures, and props.

</div>

*[Game.tweens()]: Singleton manager updating and executing active Tween interpolations
*[TweenType]: Enumeration of interpolatable object properties
*[TweenFunction]: Predefined easing mathematical equations (Penner curves)
*[IEntity]: Base interface for all interactive objects in the environment
*[ICombatEntity]: Entity with hitpoints, combat stats, and damage listeners
*[ICollisionEntity]: Entity with spatial physics bounding box
