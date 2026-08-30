---
title: HUD & UI Cookbook
icon: lucide/layout-grid
description: 'Ready-to-use recipes for common 2D game UI elements: Health Bars, Floating
  Combat Text, Speech Bubbles, and Pause Overlays.'
keywords: [LITIENGINE, UI, HUD, health bar, floating text, speech bubble, pause overlay,
  GuiComponent]
tags: [hud, health-bar, score, cookbook, recipes, overlay]
---
# HUD & UI Cookbook

This cookbook provides copy-paste ready implementations for common user interface elements in 2D games using LITIENGINE's `GuiComponent` and `SpeechBubble` frameworks.

---

## 1. Dynamic Health & Mana Bars

Draw a floating or fixed health bar that smoothly interpolates and changes color when damaged:

```java
import java.awt.Color;
import java.awt.Graphics2D;
import java.awt.geom.Rectangle2D;
import de.gurkenlabs.litiengine.entities.CombatEntity;
import de.gurkenlabs.litiengine.gui.GuiComponent;

public class HealthBar extends GuiComponent {
  private final CombatEntity entity;
  private static final int BAR_WIDTH = 50;
  private static final int BAR_HEIGHT = 6;

  public HealthBar(CombatEntity entity) {
    super(0, 0, BAR_WIDTH, BAR_HEIGHT);
    this.entity = entity;
  }

  @Override
  public void render(Graphics2D g) {
    super.render(g);
    if (this.entity == null || this.entity.isDead()) {
      return;
    }

    // Position health bar 10 pixels above the entity
    double screenX = this.entity.getX() - (BAR_WIDTH - this.entity.getWidth()) / 2.0;
    double screenY = this.entity.getY() - 10;

    double healthPercent = Math.max(0.0, (double) entity.getHitpoints() / entity.getMaxHitpoints());

    // 1. Background Bar (Dark Gray)
    g.setColor(new Color(40, 40, 40, 200));
    g.fill(new Rectangle2D.Double(screenX, screenY, BAR_WIDTH, BAR_HEIGHT));

    // 2. Health Fill (Green > Yellow > Red)
    Color healthColor = healthPercent > 0.5 ? Color.GREEN : (healthPercent > 0.2 ? Color.YELLOW : Color.RED);
    g.setColor(healthColor);
    g.fill(new Rectangle2D.Double(screenX, screenY, BAR_WIDTH * healthPercent, BAR_HEIGHT));

    // 3. Border Outline
    g.setColor(Color.BLACK);
    g.draw(new Rectangle2D.Double(screenX, screenY, BAR_WIDTH, BAR_HEIGHT));
  }
}
```

---

## 2. Floating Combat Damage Numbers

Spawn animated damage text that floats upwards and fades out:

```java
import java.awt.Color;
import java.awt.Font;
import java.awt.Graphics2D;
import java.awt.geom.Point2D;
import de.gurkenlabs.litiengine.Game;
import de.gurkenlabs.litiengine.IUpdateable;
import de.gurkenlabs.litiengine.graphics.TextRenderer;

public class FloatingText implements IUpdateable {
  private Point2D location;
  private final String text;
  private final Color color;
  private int alpha = 255;
  private int lifetime = 40; // 40 ticks = ~0.66s

  public FloatingText(String text, Point2D startLocation, Color color) {
    this.text = text;
    this.location = new Point2D.Double(startLocation.getX(), startLocation.getY());
    this.color = color;
    Game.loop().attach(this);
  }

  @Override
  public void update() {
    this.location.setLocation(this.location.getX(), this.location.getY() - 0.7);
    this.alpha = Math.max(0, this.alpha - (255 / lifetime));

    if (this.alpha <= 0) {
      Game.loop().detach(this);
    }
  }

  public void render(Graphics2D g) {
    if (this.alpha <= 0) return;

    Point2D screenPos = Game.world().camera().getViewportLocation(this.location.getX(), this.location.getY());
    g.setFont(new Font(Font.SANS_SERIF, Font.BOLD, 14));
    Color drawColor = new Color(color.getRed(), color.getGreen(), color.getBlue(), alpha);
    TextRenderer.renderWithOutline(g, text, screenPos.getX(), screenPos.getY(), drawColor, Color.BLACK);
  }
}
```

---

## 3. In-Game Speech Bubbles

Display dialogue bubbles over speaking entities:

```java
import de.gurkenlabs.litiengine.gui.SpeechBubble;

// Display a speech bubble for 3000 milliseconds
SpeechBubble bubble = SpeechBubble.create(npcEntity, "Welcome to our village, traveler!");
```

---

## 4. Pause Menu Overlay

Create a toggleable pause overlay that pauses game loop logic while allowing menu interaction:

```java
import java.awt.Color;
import java.awt.Graphics2D;
import de.gurkenlabs.litiengine.Game;
import de.gurkenlabs.litiengine.gui.Button;
import de.gurkenlabs.litiengine.gui.GuiComponent;

public class PauseOverlay extends GuiComponent {
  private final Button resumeButton;
  private final Button exitButton;

  public PauseOverlay() {
    super(0, 0, Game.window().getResolution().getWidth(), Game.window().getResolution().getHeight());

    double centerX = getWidth() / 2.0;
    double centerY = getHeight() / 2.0;

    this.resumeButton = new Button(centerX - 100, centerY - 40, 200, 40, "Resume");
    this.resumeButton.onClicked(e -> setVisible(false));

    this.exitButton = new Button(centerX - 100, centerY + 20, 200, 40, "Quit to Title");
    this.exitButton.onClicked(e -> Game.screens().display("TITLE"));

    this.getComponents().add(resumeButton);
    this.getComponents().add(exitButton);
    this.setVisible(false);
  }

  @Override
  public void render(Graphics2D g) {
    if (!isVisible()) return;

    // Semi-transparent backdrop
    g.setColor(new Color(0, 0, 0, 180));
    g.fillRect(0, 0, (int) getWidth(), (int) getHeight());

    super.render(g);
  }
}
```
