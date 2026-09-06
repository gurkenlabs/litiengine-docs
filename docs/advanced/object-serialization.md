---
title: Object Serialization
icon: lucide/hard-drive
description: Learn about serialization in LITIENGINE for saving and loading game data
  and configuration.
keywords: [LITIENGINE, serialization, XML, save, load, Java]
tags: [serialization, savegames, persistence, xml, json, reflection]
---
# Object Serialization

LITIENGINE uses XML serialization for saving and loading game data, including resource bundles and configuration.

## Built-in Serialization

The engine automatically handles:

- `.litidata` resource bundles
- `config.properties` configuration
- Map data (.tmx format)

## XmlUtilities

XML serialization utilities:

```java
import de.gurkenlabs.litiengine.util.io.XmlUtilities;
import java.net.URL;
import java.nio.file.Path;

// Save JAXB object to XML file
Path savedPath = XmlUtilities.save(object, Path.of("saves/player.xml"));

// Load JAXB object from an XML URL (file or classpath resource)
URL fileUrl = Path.of("saves/player.xml").toUri().toURL();
PlayerData data = XmlUtilities.read(PlayerData.class, fileUrl);
```

## Serializable Objects

Objects use standard Jakarta XML Binding annotations (`jakarta.xml.bind`):

```java
import jakarta.xml.bind.annotation.XmlAttribute;
import jakarta.xml.bind.annotation.XmlElement;
import jakarta.xml.bind.annotation.XmlRootElement;

@XmlRootElement(name = "playerData")
public class PlayerData {

  @XmlAttribute
  private String name;

  @XmlElement
  private int level;

  @XmlElement
  private int experience;

  // Required public no-arg constructor
  public PlayerData() {}

  // Getters and setters...
}
```

## Custom Save Data

```java
import de.gurkenlabs.litiengine.util.io.XmlUtilities;
import jakarta.xml.bind.annotation.XmlAccessType;
import jakarta.xml.bind.annotation.XmlAccessorType;
import jakarta.xml.bind.annotation.XmlElement;
import jakarta.xml.bind.annotation.XmlRootElement;
import java.nio.file.Path;

@XmlRootElement(name = "saveData")
@XmlAccessorType(XmlAccessType.FIELD)
public class SaveData {

  @XmlElement
  private String playerName;

  @XmlElement
  private int currentLevel;

  // Required public no-arg constructor for JAXB
  public SaveData() {}

  public SaveData(String playerName, int currentLevel) {
    this.playerName = playerName;
    this.currentLevel = currentLevel;
  }

  public String getPlayerName() {
    return playerName;
  }

  public void setPlayerName(String playerName) {
    this.playerName = playerName;
  }

  public int getCurrentLevel() {
    return currentLevel;
  }

  public void setCurrentLevel(int currentLevel) {
    this.currentLevel = currentLevel;
  }

  public Path save(Path filePath) {
    return XmlUtilities.save(this, filePath);
  }

  public static SaveData load(Path filePath) throws Exception {
    return XmlUtilities.read(SaveData.class, filePath.toUri().toURL());
  }
}
```

## See Also

- [Savegames](../savegames.md) - Game save system
- [Configuration](../configuration/README.md) - Config files
