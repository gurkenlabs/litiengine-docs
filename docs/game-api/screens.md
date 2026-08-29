---
title: "Screens"
description: "Screens documentation for LITIENGINE 2D Java game development."
keywords: ["LITIENGINE", "java", "2d", "game engine", "game api"]
---

# Screens

## ScreenManager API Method Reference

| Method Signature | Return Type | Description |
| :--- | :--- | :--- |
| `Game.screens().display(String screenName)` | `void` | Transitions the active display to the registered screen by name. |
| `Game.screens().display(Screen screen)` | `void` | Displays the specified screen instance immediately. |
| `Game.screens().add(Screen screen)` | `void` | Registers a new screen instance with the global screen manager. |
| `Game.screens().remove(Screen screen)` | `void` | Unregisters a screen instance from the manager. |
| `Game.screens().current()` | `Screen` | Returns the currently active and visible screen instance. |
| `Game.screens().onScreenChanged(Consumer c)` | `void` | Listener invoked whenever a screen transition occurs. |

---

**Screens** are the containers that allow you to organize the visible contents of your game. They render the game’s Environment and are considered the parent of all GUI components you want to display in a particular state of your game. The screen itself inherits from `GuiComponent` and thereby provides support to define an Appearance and listen to all kinds of Input events (e.g. `onMouseMoved(…)`). Everything that should be visible to the player needs to be rendered to the currently active screen.

Screens are identified and addressed by a unique name. The ScreenManager holds instances of all available screen and handles whenever a different Screen should be shown to the player. It provides the currently active Screen for the Game’s RenderComponent which calls the `Screen.render(Graphics2D)` method on every tick of the RenderLoop. Overwriting this method provides the ability to define a customized render pipeline that suits the need of a particular Screen implementation. With the GameScreen, the LITIENGINE provides a simple default Screen implementation that renders the current Environment and all its GuiComponents.

Examples for screens include: Menu Screen, Credits Screen, Game Screen, Inventory Screen

**Example usages:**

```java
// add some custom screens to the ScreenManager
Game.screens().add(new MenuScreen());
Game.screens().add(new IngameScreen());
Game.screens().add(new EndOfLevelScreen());

// display the screen with the name "MENU"
Game.screens().display("MENU");

// print the name of the currently active screen
System.out.println("Currently active screen: " + Game.screens().current().getName());

// a custom screen implementation that renders "Test text" on the screen
public class TestScreen extends GameScreen {
  public TestScreen() {
    super("TEST");
  }
  @Override
  public void render(final Graphics2D g) {
    super.render(g);
    g.setFont(Resources.fonts().get("customfont.ttf",32f));
    g.setColor(Color.RED);
    TextRenderer.render(g, "Test text", 100, 100);
  }
}
```

## Custom Screen Implementation Example

Here is a complete, runnable `GameOverScreen` with animated text rendering and keyboard restart input:

```java title="src/main/java/com/example/game/screens/GameOverScreen.java" linenums="1"
package com.example.game.screens;

import de.gurkenlabs.litiengine.Game;
import de.gurkenlabs.litiengine.gui.screens.Screen;
import de.gurkenlabs.litiengine.input.Input;
import java.awt.Color;
import java.awt.Font;
import java.awt.Graphics2D;
import java.awt.event.KeyEvent;

public class GameOverScreen extends Screen {
  public static final String NAME = "GAME_OVER";

  public GameOverScreen() {
    super(NAME);
  }

  @Override
  protected void initializeComponents() {
    super.initializeComponents();

    // Listen for Space key to restart
    Input.keyboard().onKeyTyped(KeyEvent.VK_SPACE, event -> {
      if (Game.screens().current().equals(this)) {
        Game.world().loadEnvironment("level1");
        Game.screens().display("INGAME-SCREEN");
      }
    });
  }

  @Override
  public void render(Graphics2D g) {
    // Fill dark background
    g.setColor(new Color(15, 10, 20, 230));
    g.fillRect(0, 0, (int) Game.window().getResolution().getWidth(), (int) Game.window().getResolution().getHeight());

    // Draw game over banner
    g.setColor(Color.RED);
    g.setFont(new Font("Monospaced", Font.BOLD, 48));
    g.drawString("GAME OVER", (int) (Game.window().getCenter().getX() - 140), (int) (Game.window().getCenter().getY() - 20));

    // Draw prompt
    g.setColor(Color.WHITE);
    g.setFont(new Font("Monospaced", Font.PLAIN, 18));
    g.drawString("Press [SPACE] to Restart", (int) (Game.window().getCenter().getX() - 120), (int) (Game.window().getCenter().getY() + 40));

    super.render(g);
  }
}
```

### Registering and Displaying Screens

```java
// Register in your main game initialization
Game.screens().add(new GameOverScreen());

// Switch to Game Over screen when player dies
Game.screens().display(GameOverScreen.NAME);
```
