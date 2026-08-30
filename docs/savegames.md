---
title: "Savegames & State Persistence"
icon: "lucide/save"
description: "Architecture guide for serializing player stats, inventory, quest progress, and environment states into JSON or binary save files."
keywords: ["LITIENGINE", "save game", "persistence", "serialization", "json", "load game", "state", "game state"]
tags: ["save game", "persistence", "serialization", "json", "load game", "state"]
---

# Savegames & State Persistence

Building a robust save system in LITIENGINE involves serializing transient game data (player health, coordinates, inventory, and environment flags) into a persistent format (such as JSON or binary files) and restoring that state into an active `Environment`.

---

## 1. Defining the Save Data Model

Use structured POJOs / Records to represent persistent game state:

```java title="src/main/java/com/example/game/save/SaveData.java" linenums="1"
package com.example.game.save;

import java.io.Serializable;
import java.util.ArrayList;
import java.util.List;

public class SaveData implements Serializable {
  private static final long serialVersionUID = 1L;

  // Metadata
  public String saveSlotName = "Slot 1";
  public long timestamp = System.currentTimeMillis();
  public String currentMapName = "level1";

  // Player State
  public double playerX = 100.0;
  public double playerY = 150.0;
  public int playerHealth = 100;
  public int playerMaxHealth = 100;
  public int gold = 0;
  public List<String> inventoryItems = new ArrayList<>();

  // World Progress Flags
  public List<String> defeatedBosses = new ArrayList<>();
  public List<String> openedChests = new ArrayList<>();
}
```

---

## 2. Implementing the Save/Load Controller

Save and load state to the user's application directory:

```java title="src/main/java/com/example/game/save/SaveManager.java" linenums="1"
package com.example.game.save;

import de.gurkenlabs.litiengine.Game;
import de.gurkenlabs.litiengine.entities.Creature;
import de.gurkenlabs.litiengine.entities.Prop;
import java.io.*;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

public class SaveManager {
  private static final String SAVE_FOLDER = "saves/";

  public static void saveGame(String fileName, Creature player) {
    try {
      Path folder = Paths.get(SAVE_FOLDER);
      if (!Files.exists(folder)) {
        Files.createDirectories(folder);
      }

      SaveData data = new SaveData();
      data.currentMapName = Game.world().environment().getMap().getName();
      data.playerX = player.getX();
      data.playerY = player.getY();
      data.playerHealth = player.getHitPoints();

      // Write binary serialized file (or JSON via Jackson/Gson)
      try (ObjectOutputStream oos = new ObjectOutputStream(
      new FileOutputStream(SAVE_FOLDER + fileName))) {
        oos.writeObject(data);
      }

      System.out.println("Game saved successfully to " + fileName);
    } catch (IOException e) {
      e.printStackTrace();
    }
  }

  public static void loadGame(String fileName, Creature player) {
    File saveFile = new File(SAVE_FOLDER + fileName);
    if (!saveFile.exists()) {
      System.err.println("Save file does not exist: " + fileName);
      return;
    }

    try (ObjectInputStream ois = new ObjectInputStream(
    new FileInputStream(saveFile))) {
      SaveData data = (SaveData) ois.readObject();

      // 1. Load the recorded map environment
      Game.world().loadEnvironment(data.currentMapName);

      // 2. Restore player coordinates & stats
      player.setLocation(data.playerX, data.playerY);
      player.setHitPoints(data.playerHealth);

      // 3. Add player to the newly loaded environment
      Game.world().environment().add(player);
      Game.world().camera().setFocus(player);

      System.out.println("Game state loaded from " + fileName);
    } catch (Exception e) {
      e.printStackTrace();
    }
  }
}
```

---

## 3. Restoring Map Entities & Opened Chests

To prevent chests from closing or dead bosses from respawning when reloading an environment:

```java
// On environment loaded callback:
Game.world().onLoaded(env -> {
  for (String chestId : currentSaveData.openedChests) {
    Prop chest = env.getProp(chestId);
    if (chest != null) {
      chest.setHitPoints(0); // Mark chest as opened/looted
    }
  }
});
```

---

## 4. Best Practices for Game Saves

!!! tip "Atomic File Writing"
    Write save data to a temporary file (`save1.tmp`) before renaming it to `save1.dat`. This ensures that if the game crashes or is closed mid-save, the player's existing save file is never corrupted.
    <script type="application/ld+json">
    {
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "LITIENGINE Savegames & State Persistence Architecture",
    "description": "Serializing player stats, inventory, and environment state restoration into JSON/binary save files.",
    "author": {
    "@type": "Organization",
    "name": "Gurkenlabs",
    "url": "https://gurkenlabs.com"
    },
    "inLanguage": "en"
    }
    </script>
