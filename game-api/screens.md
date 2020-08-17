# Screens

**Screens** are the containers that allow you to organize the visible contents of your game. They render the game’s Environment and are considered the parent of all GUI components you want to display in a particular state of your game. The screen itself inherits from `GuiComponent` and thereby provides support to define an Appearance and listen to all kinds of Input events (e.g. `onMouseMoved(…)`). Everything that should be visible to the player needs to be rendered to the currently active screen.

Screens are identified and addressed by a unique name. The ScreenManager holds instances of all available screen and handles whenever a different Screen should be shown to the player. It provides the currently active Screen for the Game’s RenderComponent which calls the `Screen.render(Graphics2D)` method on every tick of the RenderLoop. Overwriting this method provides the ability to define a customized render pipeline that suits the need of a particular Screen implementation. With the GameScreen, the LITIengine provides a simple default Screen implementation that renders the current Environment and all its GuiComponents.

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