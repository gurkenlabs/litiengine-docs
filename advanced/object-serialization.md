---
meta.description: "Learn about serialization in LITIENGINE for saving and loading game data and configuration."
meta.keywords: "LITIENGINE, serialization, XML, save, load, Java"
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

// Save object to XML file
XmlUtilities.save(object, "path/to/file.xml");

// Load object from XML
MyObject obj = XmlUtilities.read(MyObject.class, "path/to/file.xml");

// Convert to XML string
String xml = XmlUtilities.toString(object);
```

## Serializable Objects

Objects must have proper annotations for XML serialization:

```java
import javax.xml.bind.annotation.*;

@XmlRootElement(name = "playerData")
public class PlayerData {
  
  @XmlAttribute
  private String name;
  
  @XmlElement
  private int level;
  
  @XmlElement
  private int experience;
  
  // Required no-arg constructor
  public PlayerData() {}
  
  // Getters and setters...
}
```

## Custom Save Data

```java
public class SaveData {
  private String playerName;
  private int currentLevel;
  
  public void save(String filename) {
    XmlUtilities.save(this, filename);
  }
  
  public static SaveData load(String filename) {
    return XmlUtilities.read(SaveData.class, filename);
  }
}
```

## See Also

- [Savegames](/docs/savegames/) - Game save system
- [Configuration](/docs/configuration/README/) - Config files
