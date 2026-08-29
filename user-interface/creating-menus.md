---
title: "Creating Game Menus"
description: "Learn how to build interactive game menus, title screens, keyboard/mouse navigation, and screen transitions in LITIENGINE."
keywords: ["LITIENGINE", "menu", "MenuScreen", "Screen", "GuiComponent", "UI", "Java", "title screen", "keyboard navigation"]
---

# Creating Game Menus

Game menus and title screens are the entry points for players into your game. In LITIENGINE, menus are built by subclassing `Screen` and composing `GuiComponent` instances like `Menu`, `ImageComponent`, and `Button`.

```text
┌─────────────────────────────────────────────────────────────┐
│                       MenuScreen                            │
│                                                             │
│   ┌─────────────────────────────────────────────────────┐   │
│   │                 Game Title / Logo                   │   │
│   └─────────────────────────────────────────────────────┘   │
│                                                             │
│                  ┌──────────────────────┐                   │
│                  │       ► Play         │  (Selected)       │
│                  ├──────────────────────┤                   │
│                  │      Settings        │                   │
│                  ├──────────────────────┤                   │
│                  │        Exit          │                   │
│                  └──────────────────────┘                   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Step 1: The Screen Lifecycle

A `Screen` represents an isolated visual mode in your game. When creating a menu, we override three key lifecycle methods:

1. **`initializeComponents()`**: Called once during construction. Instantiate UI components, configure layout coordinates, register click/change listeners, and add components to `getComponents()`.
2. **`prepare()`**: Called every time the screen becomes active (right before it is displayed). Use this to reset menu selections or reload player settings.
3. **`render(Graphics2D g)`**: Called on every render tick. Draw custom background art, particle effects, or logos, then call `super.render(g)` to render all registered `GuiComponent` elements.

## Step 2: Complete `MenuScreen` Implementation

Here is a complete, production-ready `MenuScreen` featuring a background image, centered title logo, interactive vertical `Menu`, keyboard/mouse navigation, and sub-view switching:

```java
package com.mygame.screens;

import de.gurkenlabs.litiengine.Game;
import de.gurkenlabs.litiengine.graphics.ImageRenderer;
import de.gurkenlabs.litiengine.gui.ImageComponent;
import de.gurkenlabs.litiengine.gui.ImageScaleMode;
import de.gurkenlabs.litiengine.gui.Menu;
import de.gurkenlabs.litiengine.gui.Orientation;
import de.gurkenlabs.litiengine.gui.screens.Screen;
import de.gurkenlabs.litiengine.resources.Resources;
import java.awt.Color;
import java.awt.Font;
import java.awt.Graphics2D;
import java.awt.image.BufferedImage;

public class MenuScreen extends Screen {
  public static final String NAME = "MENU";

  private Menu mainMenu;
  private ImageComponent instructionsPanel;
  private ImageComponent backButton;

  public MenuScreen() {
    super(NAME);
  }

  @Override
  protected void initializeComponents() {
    super.initializeComponents();

    double screenWidth = Game.window().getResolution().getWidth();
    double screenHeight = Game.window().getResolution().getHeight();

    double menuWidth = screenWidth * 0.25;
    double menuHeight = screenHeight * 0.25;
    double menuX = (screenWidth - menuWidth) / 2.0;
    double menuY = screenHeight * 0.50;

    // 1. Create vertical menu with 3 options
    this.mainMenu = new Menu(menuX, menuY, menuWidth, menuHeight, 
        Orientation.VERTICAL, "Play", "Instructions", "Exit");

    // Style the menu buttons
    Font menuFont = Resources.fonts().get("custom-font.ttf", 20f);
    this.mainMenu.getCellComponents().forEach(btn -> {
      btn.setFont(menuFont);
      btn.getAppearance().setForegroundColor(Color.LIGHT_GRAY);
      btn.getAppearanceHovered().setForegroundColor(Color.WHITE);
      btn.getAppearanceSelected().setForegroundColor(Color.YELLOW);
      btn.getAppearance().setBackgroundColor1(new Color(20, 20, 20, 200));
    });

    // 2. Handle selection & clicks
    this.mainMenu.onChange(index -> {
      switch (index) {
        case 0 -> startGame();
        case 1 -> showInstructions();
        case 2 -> System.exit(0);
      }
    });

    // 3. Instructions Sub-Panel
    this.instructionsPanel = new ImageComponent(
        screenWidth * 0.2, screenHeight * 0.4, 
        screenWidth * 0.6, screenHeight * 0.4, 
        "Use ARROW KEYS / WASD to move.\nSPACE to jump.\nLEFT CLICK to attack.");
    this.instructionsPanel.setImageScaleMode(ImageScaleMode.FIT);
    this.instructionsPanel.getAppearance().setForegroundColor(Color.WHITE);

    // 4. Back Button for instructions view
    this.backButton = new ImageComponent(menuX, screenHeight * 0.85, menuWidth, 40, "Back");
    this.backButton.onClicked(e -> showMainMenu());

    // Register all components to the Screen
    this.getComponents().add(this.mainMenu);
    this.getComponents().add(this.instructionsPanel);
    this.getComponents().add(this.backButton);
  }

  @Override
  public void prepare() {
    super.prepare();
    showMainMenu();
  }

  @Override
  public void render(Graphics2D g) {
    // 1. Draw menu background
    BufferedImage bg = Resources.images().get("menu-bg.png");
    if (bg != null) {
      ImageRenderer.render(g, bg, 0, 0);
    }

    // 2. Draw Title Logo centered above the menu
    BufferedImage logo = Resources.images().get("logo.png");
    if (logo != null) {
      double logoX = (Game.window().getResolution().getWidth() - logo.getWidth()) / 2.0;
      ImageRenderer.render(g, logo, logoX, 50);
    }

    // 3. Render all UI components
    super.render(g);
  }

  private void showMainMenu() {
    this.mainMenu.setVisible(true);
    this.mainMenu.setEnabled(true);
    this.instructionsPanel.setVisible(false);
    this.backButton.setVisible(false);
  }

  private void showInstructions() {
    this.mainMenu.setVisible(false);
    this.mainMenu.setEnabled(false);
    this.instructionsPanel.setVisible(true);
    this.backButton.setVisible(true);
  }

  private void startGame() {
    // Switch to ingame screen and load world
    Game.screens().display("INGAME");
    Game.world().loadEnvironment("level1");
  }
}
```

## Step 3: Registering & Displaying Screens

In your `Program.java` entry point, register both your `MenuScreen` and `GameScreen` before launching:

```java
package com.mygame;

import com.mygame.screens.MenuScreen;
import de.gurkenlabs.litiengine.Game;
import de.gurkenlabs.litiengine.gui.screens.GameScreen;
import de.gurkenlabs.litiengine.resources.Resources;

public class Program {
  public static void main(String[] args) {
    Game.init(args);

    // 1. Preload resource bundles
    Resources.load("game.litidata");

    // 2. Add screens to the ScreenManager
    Game.screens().add(new MenuScreen());
    Game.screens().add(new GameScreen("INGAME"));

    // 3. Display the menu screen initially
    Game.screens().display("MENU");

    // 4. Start the engine
    Game.start();
  }
}
```

## Keyboard and Mouse Navigation

The `Menu` component handles user input out of the box:
* **Vertical Menus**: Pressing `UP` and `DOWN` arrow keys navigates items; hitting `ENTER` triggers selection.
* **Horizontal Menus**: Pressing `LEFT` and `RIGHT` arrow keys navigates items.
* **Mouse Navigation**: Hovering over menu items triggers the `getAppearanceHovered()` state, and clicking an item sets `currentSelection` and invokes `onChange()`.

## Best Practices

> [!TIP]
> - **Scale Relative to Resolution**: Calculate positions and sizes using `Game.window().getResolution().getWidth()` and `getHeight()` to ensure your menu scales properly on different screen resolutions.
> - **Focus Management**: Call `component.setFocusable(true)` if you create custom keyboard-navigable components.
> - **Clean Screen Transitions**: When switching screens with `Game.screens().display()`, use `prepare()` to reset timers, selections, and transient UI states.

## See Also

- **[GuiComponents: An Overview](/docs/user-interface/guicomponents-an-overview/)** - Component hierarchy and properties
- **[Screens API](/docs/game-api/screens/)** - Resolution scaling and display management
