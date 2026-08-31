---
title: "Game Configuration & Settings"
icon: "lucide/settings"
description: "Comprehensive guide to LITIENGINE's configuration system: built-in graphic/audio/client settings, custom INI groups, and disk persistence."
keywords: ["LITIENGINE configuration", "config.properties", "Game.config", "GraphicConfiguration", "SoundConfiguration", "ClientConfiguration", "ConfigurationGroup"]
tags: ["configuration", "settings", "properties", "preferences", "ini", "persistence"]
---

# Game Configuration & Settings

LITIENGINE includes a modular configuration management subsystem accessible via `Game.config()`. It automatically reads, validates, and persists game settings to a `config.properties` file in the application's working directory.

---

## Built-in Configuration Groups

LITIENGINE organizes engine settings into distinct configuration groups:

### 1. `ClientConfiguration` (`cl_`)
Manages general client runtime properties:

| Property Key | Type | Default | Description |
|:---|:---|:---|:---|
| `cl_maxFps` | `int` | `60` | Target framerate limit for the rendering thread. |
| `cl_updaterate` | `int` | `60` | Fixed tick update rate for physics, AI, and game loop logic. |
| `cl_showGameMetrics` | `boolean` | `false` | Displays live FPS, memory usage, and quadtree metric overlays. |
| `cl_country` | `String` | `"US"` | Active locale country code. |
| `cl_language` | `String` | `"en"` | Active ISO language string for localization bundles. |

---

### 2. `GraphicConfiguration` (`gfx_`)
Controls display resolution, window mode, and pixel scaling:

| Property Key | Type | Default | Description |
|:---|:---|:---|:---|
| `gfx_fullscreen` | `boolean` | `false` | Enables borderless exclusive fullscreen mode. |
| `gfx_enableResolutionScale` | `boolean` | `true` | Automatically scales virtual coordinates to monitor resolution. |
| `gfx_graphicQuality` | `Quality` | `VERYHIGH` | AWT anti-aliasing and rendering hint quality (`LOW`, `MEDIUM`, `HIGH`, `VERYHIGH`). |
| `gfx_antiAliasing` | `boolean` | `false` | Smooths vector geometries (recommended `false` for crisp pixel art). |

---

### 3. `SoundConfiguration` (`sfx_`)
Controls master, music, and sound effect volume buses:

| Property Key | Type | Default | Description |
|:---|:---|:---|:---|
| `sfx_soundVolume` | `float` | `0.5f` | Master volume multiplier for sound effects ($0.0$ to $1.0$). |
| `sfx_musicVolume` | `float` | `0.5f` | Master volume multiplier for background music ($0.0$ to $1.0$). |

---

## Creating Custom Configuration Groups

You can define custom configuration groups to persist gameplay options, custom keybindings, difficulty settings, and player preferences:

```java title="src/main/java/com/example/game/GameSettings.java"
package com.example.game;

import de.gurkenlabs.litiengine.configuration.ConfigurationGroup;
import de.gurkenlabs.litiengine.configuration.ConfigurationGroupInfo;

@ConfigurationGroupInfo(prefix = "game_")
public class GameSettings extends ConfigurationGroup {
  private boolean screenShake = true;
  private boolean damageNumbers = true;
  private int difficulty = 1; // 0 = Easy, 1 = Normal, 2 = Hard
  private String playerName = "Hero";

  public boolean isScreenShake() { return this.screenShake; }
  public void setScreenShake(boolean screenShake) { this.screenShake = screenShake; }

  public boolean isDamageNumbers() { return this.damageNumbers; }
  public void setDamageNumbers(boolean damageNumbers) { this.damageNumbers = damageNumbers; }

  public int getDifficulty() { return this.difficulty; }
  public void setDifficulty(int difficulty) { this.difficulty = difficulty; }

  public String getPlayerName() { return this.playerName; }
  public void setPlayerName(String playerName) { this.playerName = playerName; }
}
```

### Registering and Saving Configuration

Register your custom configuration group during game initialization:

```java title="Program.java"
package com.example.game;

import de.gurkenlabs.litiengine.Game;

public class Program {
  public static GameSettings settings;

  public static void main(String[] args) {
    // 1. Register custom configuration group before or right after Game.init
    settings = new GameSettings();
    Game.config().add(settings);

    Game.init(args);

    // 2. Read values from configuration
    if (settings.isScreenShake()) {
      System.out.println("Screen shake is enabled!");
    }

    // 3. Save changes back to config.properties on disk
    settings.setDifficulty(2);
    Game.config().save();

    Game.start();
  }
}
```

---

## Sample `config.properties` File

When saved, LITIENGINE formats all settings with their group prefixes:

```properties title="config.properties"
# LITIENGINE Configuration File
cl_country=US
cl_language=en
cl_maxFps=60
cl_showGameMetrics=false
cl_updaterate=60

gfx_antiAliasing=false
gfx_enableResolutionScale=true
gfx_fullscreen=false
gfx_graphicQuality=VERYHIGH

sfx_musicVolume=0.75
sfx_soundVolume=0.80

game_difficulty=2
game_damageNumbers=true
game_playerName=Hero
game_screenShake=true
```

---

## See Also

<div class="grid cards" markdown>

- :material-volume-high:{ .lg .middle } **[Sound Engine](../game-api/sound-engine.md)**

    ---

    Audio volume buses and playlist management.

- :material-monitor:{ .lg .middle } **[Game Window](../game-api/game-window.md)**

    ---

    Window resolution, display modes, and cursor configurations.

</div>

*[Game.config()]: Global configuration manager reading and saving config.properties
*[ConfigurationGroup]: Base class for modular INI configuration settings
*[ConfigurationGroupInfo]: Annotation specifying prefix for persisted settings
