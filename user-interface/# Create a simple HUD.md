# Create a simple HUD

A HUD (heads-up display) is used to render Graphics used for game information, like a health bar or a toolbar. 
LITIENGINE provides a broad kit of Components for this with the [`GuiComponent`](https://litiengine.com/docs/user-interface/guicomponents-an-overview/) framework. 

Lets implement a simple HUD that creates a healthbar for us.

* ![Healthbar](https://user-images.githubusercontent.com/105820458/173564612-9c57bf97-95b5-4c22-9058-8ed1ed3e28b2.PNG)


## 1. our HUD class

```java
package org.example;

import de.gurkenlabs.litiengine.Game;
import de.gurkenlabs.litiengine.graphics.ImageRenderer;
import de.gurkenlabs.litiengine.graphics.Spritesheet;
import de.gurkenlabs.litiengine.gui.GuiComponent;
import de.gurkenlabs.litiengine.resources.Resources;
import de.gurkenlabs.litiengine.util.Imaging;

import javax.tools.Tool;
import java.awt.*;
import java.awt.image.BufferedImage;

public class HUD extends GuiComponent {
    //create variables for our images that we want to render later, and scale them to the desired size
    private static final BufferedImage HEART = Imaging.scale(Resources.images().get("src/main/resources/hud/life.png"), 5.0);
    private static final BufferedImage HEARTEMPTY = Imaging.scale(Resources.images().get("src/main/resources/hud/herzleer.png"), 5.0);
   
    //optional / intialize a Padding variable, to change positioning easier later on
    private static final int PADDING = 10;
    
    //call the super constructor, with the current game Windows Width and Hight to create a new HUD
    protected HUD() {
    super(0, 0, Game.window().getResolution().getWidth(), Game.window().getResolution().getHeight());
    }
    
```
- It's important to know that the Image files for our `BufferedImage`s can't be received from the [game resource file](https://litiengine.com/docs/resource-management/), so be sure to provide the complete path in the file system.

## The render methods

now lets get to the visual part, the render methods of our `HUD` class:

```java
 @Override
    public void render(Graphics2D g) {
        super.render(g);
        
        //if there is no enviroment loaded we dont need to render anything
        if (Game.world().environment() == null ) {
            return;

        }
        this.renderHP(g);
        }

    private void renderHP(Graphics2D g) {

        //define the x and y coordinates of our Healtbar 
        double y = Game.window().getResolution().getHeight() - Game.window().getResolution().getHeight() + PADDING * 7 - HEART.getHeight();
        double x = Game.window().getResolution().getWidth()  - ((Player.instance().getHitPoints().getMax() * (HEART.getWidth() + PADDING) * 1.28) - PADDING);
        
        //decides weather to render a full or empty heart depending on the players current Hitpoints
        for (int i = 0; i < Player.instance().getHitPoints().getMax(); i++) {
            BufferedImage img = i < Player.instance().getHitPoints().get() ? HEART : HEARTEMPTY;
            ImageRenderer.render(g, img, x + i * img.getWidth() + PADDING, y);

        }
    }

```
- the x and y coorinates of this example place the bar in the upper left corner of the screen, but you can adjust these to your liking of course.



### you could also adjust how many Hitpoints a heart should represent by dividing it by 2 for example :

```java
private void renderHP(Graphics2D g) {

        //define the x and y coordinates of our Healtbar 
        double y = Game.window().getResolution().getHeight() - Game.window().getResolution().getHeight() + PADDING * 7 - HEART.getHeight();
        double x = Game.window().getResolution().getWidth()  - ((Player.instance().getHitPoints().getMax() * (HEART.getWidth() + PADDING) * 1.28) - PADDING);
        
        //decides weather to render a full or empty heart depending on the players current Hitpoints
        for (int i = 0; i < Player.instance().getHitPoints().getMax() /2; i++) {
            BufferedImage img = i < Math.ceil( Player.instance().getHitPoints().get()/2) ? HEART : HEARTEMPTY;
            ImageRenderer.render(g, img, x + i * img.getWidth() + PADDING, y);

        }
    }

```
- now one heart would represent 2 Hitpoints of the Player
- we use the `Math.ceil()` method to get the next bigger int and not a double

But now we have render methods, so why can't we see our precous health? 

## initializing a new HUD in the `GameScreen` class

Now to actually see our HUD, we first need to instantiate it in our `GameScreen` class


```java
package org.example;

import de.gurkenlabs.litiengine.Game;
import de.gurkenlabs.litiengine.gui.screens.GameScreen;
import java.awt.*;

public class  InGameScreen extends GameScreen {
   
    private HUD hud;

    public static final String NAME = "INGAME-SCREEN";

    public InGameScreen() {
    super(NAME);
    }
@Override
    protected void initializeComponents() {

    //initialize a new HUD object, and add it to the GameScreen components
    this.hud = new HUD();
    this.getComponents().add(this.hud);

    }
    @Override
    public void render(Graphics2D g) {
        super.render(g);

        if (Game.world().environment() != null) {
            Game.world().environment().render(g);
        }
    }
}
```
And there you have it your own Health bar, customizable as you wish :D
