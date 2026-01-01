# Game Configuration

## Set the basic game information

When starting a fresh game project with the LITIENGINE, we encourage you
to give your baby a name. Also, some additional information might be
very useful, like the game's version, author(s) or the website. For this
purpose, we've created the `GameInfo` class. It holds all the metadata
of your game and can be accessed via `Game.info()`. There are basically
two ways to set your information:

  - Directly from code, using  `Game.info().setXX()`
  - Via XML File by calling `Game.setInfo("gameinfo.xml")`

**Setting game info from code:**
```java
// set meta information about the game
Game.info().setName("My Testgame");
Game.info().setSubTitle("Made with LITIENGINE!");
Game.info().setVersion("v1.0.0");
Game.info().setWebsite("https://litiengine.com/");
...
```

**Example XML file:**

```xml
<?xml version="1.0" encoding="UTF-8"?>
<gameinfo>
 <name>My Testgame</name>
 <subtitle>Made with LITIENGINE!</subtitle>
 <description>A game, that was implemented with the LITIENGINE.</description>
 <website>https://litiengine.com</website>
 <version>v1.0.0</version>
 <company>gurkenlabs.de</company>
 <developer>Steffen Wilke</developer>
 <developer>Matthias Wilke</developer>
</gameinfo>
```

You need to set this information before `Game.init()` is called, because
some of this information is used by the LITIENGINE to e.g. set the
default JFrame title of the game.

## Configure Default Behavior and Appearance

All of the components that are provided by the LITIENGINE come with a
reasonable default configuration. However, they might not be applicable
to your type of game which is why you should at least know about these
configurations to be able to adjust them when necessary.

  - **Encoding for textual Resources**
    (default: `Resources.ENCODING_ISO_8859_1`) For some languages, you
    might prefer to store your text files with UTF-8 encoding. You can
    make the LITIENGINE aware of this by
    calling `Resources.setEncoding(Resources.ENCODING_UTF_8)`.
  - **Base Render Scale** (default: `RenderEngine.DEFAULT_RENDERSCALE
    = 3.0`) Depending on what type of Art Style you're going for, it is
    not uncommon to render the game with an adjusted render scale. A
    good example would be 8-Bit pixel art. Rendering such a game at a
    scale of 1 would not be very practical for today's high-resolution
    monitors. You can adjust this by
    calling `Game.graphics().setBaseRenderScale(5.0)`
  - **UI properties** If you intend to use our `GUIComponents` you might
    want to have a deeper look into the `GuiProperties` class. It
    provides global default appearance settings for all  `GUIComponents`
    e.g. you can set a default Font by
    calling `GuiProperties.setDefaultFont(Resources.getFont("some-font.ttf")).`
  - **Custom Mouse Cursor** If you intend to use the Mouse to control your
    LITIENGINE game you should consider providing a custom Cursor Image.
    `Game.world().cursor().set(CURSOR_IMAGE, 16, 16);`

## Game Configuration File `config.properties`

When you want to Configure a LITIENGINE Game, there are also
configurations that might have to be changed by the player or developer
on the fly without changing the actual implementation. This includes
things like Soundvolume, Resolution, Mouse Sensitivity or Debugging
options. LITIENGINE Games store this information in
a `config.properties` file in the application's execution folder. If no
such file exists, the Game will create one for you with all default
values upon starting up the game for the first time. When deploying your
game, it is recommended to provide a default configuration file for your
players with values that you consider reasonable for your game. The
configuration is organized in `ConfigurationGroups` with a custom prefix
each. You can also provide custom groups that hold configuration
relevant only for your particular game. 

**Add Custom ConfigurationGroup:**

```java
MyCustomConfigurationGroup customGroup = new MyCustomConfigurationGroup();
Game.config().add(customGroup);

// Example for a custom configuration group
@ConfigurationGroupInfo(prefix = "custom_")
public class MyCustomConfigurationGroup extends ConfigurationGroup {
  private int myInt = 123;

  public int getMyInt(){ return this.myInt }

  public void setMyInt(int myInt){ this.myInt = myInt; }
}
```

**Configuration File Excerpt:**

```java
cl_country=US
cl_language=en
cl_maxFps=60
cl_showGameMetrics=true
cl_updaterate=60
sfx_musicVolume=0.5
sfx_soundVolume=0.5
gfx_enableResolutionScale=true
gfx_fullscreen=false
gfx_graphicQuality=VERYHIGH
...
```

## Logging Configuration `logging.properties`

The LITIENGINE uses the `java.util.logging` framework to log information
and errors. It is possible to configure the output of the logging by
providing a `logging.properties` file in the Game's execution directory.
You can read more about
this [HERE](http://tutorials.jenkov.com/java-logging/configuration.html#configuration-file).

**Example Logging Configuration file**

```java
handlers=java.util.logging.FileHandler, java.util.logging.ConsoleHandler

java.util.logging.ConsoleHandler.level=WARNING
java.util.logging.ConsoleHandler.formatter=java.util.logging.SimpleFormatter

java.util.logging.FileHandler.level=WARNING
java.util.logging.FileHandler.pattern=game.log
java.util.logging.FileHandler.formatter=java.util.logging.SimpleFormatter
java.util.logging.FileHandler.append=true
java.util.logging.FileHandler.limit = 50000
java.util.logging.FileHandler.count = 1
```
