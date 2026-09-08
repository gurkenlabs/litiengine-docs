---
title: Game Window
icon: lucide/app-window
description: Learn about LITIENGINE's Game.window() API for managing the game window,
  resolution scaling, fullscreen mode, custom cursors, and window icons.
keywords: [LITIENGINE, game window, fullscreen, resolution, cursor, icon, Java]
tags: [game-window, display, resolution, fullscreen, windowed, screen]
---
# Game Window

The `Game.window()` method provides access to the `GameWindow` class, which manages the window that hosts your game's rendering component. Use it to control window properties like title, icon, resolution, cursor, and display mode.

```java
// Access the game window
GameWindow window = Game.window();
```

## Window Setup

Set up the window before or after game initialization:

```java
public static void main(String[] args) {
  // Set game info first (used for window title)
  Game.info().setName("My Game");
  Game.info().setVersion("v1.0.0");

  Game.init(args);

  // Set window icon after initialization
  Game.window().setIcon(Resources.images().get("icon.png"));

  Game.start();
}
```

### Window Title

The window title defaults to your game's name from `Game.info()`. You can customize it:

```java
Game.window().setTitle("My Awesome Game - Main Menu");
```

### Window Icon

Set a custom window icon (displayed in the title bar and taskbar):

```java
BufferedImage icon = Resources.images().get("icon.png");
Game.window().setIcon(icon);
```

## Resolution and Scaling

### Getting Resolution

```java
// Get current window resolution
Dimension resolution = Game.window().getResolution();
int width = resolution.width;
int height = resolution.height;

// Get physical screen resolution via AWT Toolkit
Dimension screenSize = Toolkit.getDefaultToolkit().getScreenSize();

// Configure target resolution using preset aspect ratios
Game.config().graphics().setResolution(Resolution.Ratio16x9.RES_1920x1080.getDimension());
```

LITIENGINE provides predefined standard resolutions in `de.gurkenlabs.litiengine.gui.screens.Resolution` across common aspect ratios:

- **16:9**: `Resolution.Ratio16x9.RES_1920x1080`, `RES_1600x900`, `RES_1366x768`, `RES_1280x720`
- **16:10**: `Resolution.Ratio16x10.RES_1920x1200`, `RES_1680x1050`, `RES_1440x900`, `RES_1280x800`
- **4:3**: `Resolution.Ratio4x3.RES_1024x768`, `RES_800x600`, `RES_640x480`
- **5:4**: `Resolution.Ratio5x4.RES_1280x1024`

### Resolution Scaling

When resolution scaling is enabled, all players see the same proportional view of the game world regardless of their physical window size. When disabled, players with larger windows or higher resolutions see a wider viewport of the map.

Enable in `config.properties`:

```properties
gfx_enableResolutionScale=true
```

Or programmatically:

```java
Game.config().graphics().setEnableResolutionScale(true);
```

### Base Render Scale

Control how much the game is scaled up from its native resolution:

```java
// Set base render scale (default is 3.0)
Game.graphics().setBaseRenderScale(4f);
```

## Display Modes

LITIENGINE supports windowed, borderless window, and exclusive fullscreen modes via the `DisplayMode` enum:

```java
import de.gurkenlabs.litiengine.configuration.DisplayMode;

// Check current display mode
DisplayMode currentMode = Game.config().graphics().getDisplayMode();

// Switch to fullscreen
Game.window().setDisplayMode(DisplayMode.FULLSCREEN);

// Switch to borderless window (fills screen without window borders)
Game.window().setDisplayMode(DisplayMode.BORDERLESS);

// Return to standard windowed mode
Game.window().setDisplayMode(DisplayMode.WINDOWED);
```

Configure default in `config.properties`:

```properties
gfx_displayMode=FULLSCREEN
```

## Custom Cursor

LITIENGINE supports custom mouse cursors for a more polished game experience.

```java
// Set a custom cursor image
BufferedImage cursorImage = Resources.images().get("cursor.png");
Game.window().cursor().set(cursorImage, 16, 16);

// Enable/disable the cursor visibility
Game.window().cursor().setVisible(true);

// Reset to system default cursor
Game.window().cursor().reset();
```

The cursor offset parameters (16, 16) define the hotspot position relative to the top-left corner of the cursor image.

## Window Events

Listen for window state changes via `getHostControl()` (the underlying `JFrame`) or react to resolution changes:

```java
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;

// Listen to standard AWT window events
Game.window().getHostControl().addWindowListener(new WindowAdapter() {
  @Override
  public void windowGainedFocus(WindowEvent e) {
    // Game window gained focus
  }

  @Override
  public void windowLostFocus(WindowEvent e) {
    // Game window lost focus - consider pausing
  }
});

// React whenever the game resolution is changed
Game.window().onResolutionChanged(newRes -> {
  System.out.println("Resolution updated to: " + newRes.getWidth() + "x" + newRes.getHeight());
});
```

## Configuration Options

Key window-related settings in `config.properties`:

```properties
# Enable/disable resolution scaling
gfx_enableResolutionScale=true

# Display mode: WINDOWED, FULLSCREEN, or BORDERLESS
gfx_displayMode=WINDOWED

# Maximum FPS (0 = unlimited, syncs to monitor if vsync enabled)
cl_maxFps=60

# Show game metrics (FPS, UPS) in corner
cl_showGameMetrics=false
```

## Common Patterns

### Initialize Window with Custom Settings

```java
public static void main(String[] args) {
  Game.info().setName("My Game");
  Game.info().setVersion("v1.0.0");

  Game.init(args);

  // Configure window appearance
  Game.window().setIcon(Resources.images().get("icon.png"));
  Game.window().cursor().set(Resources.images().get("cursor.png"), 8, 8);

  // Set render scale for pixel art look
  Game.graphics().setBaseRenderScale(4f);

  Game.start();
}
```

### Toggle Fullscreen at Runtime

```java
import de.gurkenlabs.litiengine.configuration.DisplayMode;
import java.awt.event.KeyEvent;

Input.keyboard().onKeyPressed(KeyEvent.VK_F11, e -> {
  DisplayMode current = Game.config().graphics().getDisplayMode();
  Game.window().setDisplayMode(current == DisplayMode.FULLSCREEN ? DisplayMode.WINDOWED : DisplayMode.FULLSCREEN);
});
```

## See Also

- [Game.screens()](screens.md) - Screen management
- [Game.graphics()](render-engine.md) - Rendering engine
- [Configuration](../configuration/README.md) - Game configuration options
