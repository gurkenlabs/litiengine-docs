---
meta.description: "Learn about LITIENGINE's Game.window() API for managing the game window, resolution scaling, fullscreen mode, custom cursors, and window icons."
meta.keywords: "LITIENGINE, game window, fullscreen, resolution, cursor, icon, Java"
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

// Get host screen resolution
Dimension screenResolution = Game.window().getHostScreenResolution();
```

### Resolution Scaling

![Resolution Scaling Comparison](images/scaling.png)

When resolution scaling is enabled, all players see the same portion of the game world regardless of their window size. When disabled, players with larger windows see more of the game world.

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

## Fullscreen Mode

Toggle between windowed and fullscreen display:

```java
// Check if fullscreen
boolean isFullscreen = Game.window().isFullscreen();

// Enable fullscreen
Game.window().setFullscreen(true);

// Return to windowed mode
Game.window().setFullscreen(false);
```

Configure default in `config.properties`:

```properties
gfx_fullscreen=false
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

Listen for window state changes:

```java
Game.window().addWindowListener(new WindowAdapter() {
  @Override
  public void windowGainedFocus(WindowEvent e) {
    // Game window gained focus
  }
  
  @Override
  public void windowLostFocus(WindowEvent e) {
    // Game window lost focus - consider pausing
  }
});
```

## Configuration Options

Key window-related settings in `config.properties`:

```properties
# Enable/disable resolution scaling
gfx_enableResolutionScale=true

# Start in fullscreen mode
gfx_fullscreen=false

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
Input.keyboard().onKeyPressed(KeyEvent.VK_F11, e -> {
  Game.window().setFullscreen(!Game.window().isFullscreen());
});
```

## See Also

- [Game.screens()](/docs/game-api/screens/) - Screen management
- [Game.graphics()](/docs/game-api/render-engine/) - Rendering engine
- [Configuration](/docs/configuration/README/) - Game configuration options
