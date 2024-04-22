---
description: How to save and load player progress
---

# Savegames

### XML savegames

Let's have a look at an example where we store and load savegames using XML files.
We need one class representing the savegame, as well as one method for saving and one method for loading the savegame.

Let's have a look at an example used in a legacy version of _Dr. Lepus._
This is what the `SaveGame` itself would look like:

```java
import javax.xml.bind.annotation.XmlElement;
import javax.xml.bind.annotation.XmlRootElement;
import javax.xml.bind.annotation.XmlTransient;

import de.gurkenlabs.lepus.entities.items.Items;
import de.gurkenlabs.lepus.inventory.Storage;

@XmlRootElement(name = "savegame")
public class SaveGame {

  @XmlElement(name = "chapter")
  private int chapter;

  @XmlElement(name = "part")
  private int part;

  @XmlElement(name = "spawn")
  private int spawn;

  @XmlElement(name = "name")
  private String name;

  @XmlElement(name = "upgrades")
  private UpgradeLevels upgrades;

  @XmlElement(name = "totalZombiesKilled")
  private int totalZombiesKilled;

  @XmlElement(name = "inventory")
  private Storage<Items> inventory;

  public SaveGame() {
  }

  public SaveGame(final int chapter, final int part, final int spawn, final String name) {
    this.chapter = chapter;
    this.part = part;
    this.spawn = spawn;
    this.name = name;
  }

  @XmlTransient
  public int getChapter() {
    return this.chapter;
  }

  @XmlTransient
  public int getPart() {
    return this.part;
  }

  @XmlTransient
  public int getSpawn() {
    return this.spawn;
  }

  @XmlTransient
  public String getName() {
    return this.name;
  }

  @XmlTransient
  public UpgradeLevels getUpgrades() {
    return this.upgrades;
  }

  @XmlTransient
  public int getTotalZombiesKilled() {
    return this.totalZombiesKilled;
  }

  @XmlTransient
  public Storage<Items> getInventory() {
    return this.inventory;
  }

  public void setChapter(int chapter) {
    this.chapter = chapter;
  }

  public void setPart(int part) {
    this.part = part;
  }

  public void setSpawn(int spawn) {
    this.spawn = spawn;
  }

  public void setUpgrades(UpgradeLevels upgrades) {
    this.upgrades = upgrades;
  }

  public void setName(String name) {
    this.name = name;
  }

  public void setTotalZombiesKilled(int totalZombiesKilled) {
    this.totalZombiesKilled = totalZombiesKilled;
  }

  public void setInventory(Storage<Items> inventory) {
    this.inventory = inventory;
  }
}
```

We can save the game state to the system user's directory with the `saveGame()`-method. Make sure that things like the player inventory and active upgrades / skills / traits are also serializable.

```java
  public static void saveGame() {
    Level level = GameOrchestrator.getCurrentLevel();
    if (level == null) {
      return;
    }

    // don't save in elevators
    if (level.getName().contains("elevator")) {
      return;
    }

    SaveGame saveGame = new SaveGame(level.getChapter(), level.getPart(), GameOrchestrator.getCurrentSpawn(), SAVE_FILE_NAME);
    saveGame.setUpgrades(Upgrades.save());
    saveGame.setInventory(Lepus.instance().getInventory());

    String dir = System.getProperty("user.home") + "/.drlepus/savefiles/";
    File dirFile = new File(dir);
    dirFile.mkdirs();
    String savegamePath = dir + saveGame.getName() + ".xml";
    XmlUtilities.save(saveGame,savgamePath);
  }
```

To load the savegame, we will call `loadSavedGameFile()`.

```java
  public static void loadSavedGameFile() {
    String path = System.getProperty("user.home") + "/.drlepus/savefiles/" + SAVE_FILE_NAME + ".xml";
    final SaveGame saveGame = XmlUtilities.read(SaveGame.class, Resources.getLocation(path));
    Upgrades.load(saveGame.getUpgrades());
    Lepus.instance().setupInventory(saveGame.getInventory());
    Level level = Level.getLevel(saveGame.getChapter(), saveGame.getPart());
    if (level == null) {
      log.log(java.util.logging.Level.SEVERE, "Invalid save file detected! Level {0}-{1} does not exist", new Object[] { saveGame.getChapter(), saveGame.getPart() });
      level = Level.LABORATORY;
    }
    loadEnvironment(level, saveGame.getSpawn());
  }
```

Remember, this is just one specific example how to load and save player progress. You can pick whatever information you like, in whichever format you like, and wherever you would like to store it. Get creative!
