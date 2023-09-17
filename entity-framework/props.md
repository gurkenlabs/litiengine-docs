---
meta.description: How to register a custom Prop implementation in LITIENGINE.
meta.keywords: LITIENGINE, prop, entities, entity, custom, register, mapobject, loader
---

# Props
Creating props is among the most frequent things you're going to be doing with LITIENGINE. 
Let us first show you a simple example of creating a box to decorate your map. After we've created the box, we will show you how you can enhance the standard Prop implementation with custom logic.

## Creating a prop spritesheet
Make sure to name the spritesheet `prop-box`. The `prop-` part is called a `spritePrefix` and is used internally to simplify the process of creating a prop from this spritesheet. The `box` part is called the `spritesheetName` and will be used to identify your spritesheet.
## Importing a prop spritesheet
In the top toolbar, use `Resources -> Import -> Sprites...` to open the Spritesheet import dialogue.

![prop-spritesheet-import](/entity-framework/img/prop-spritesheet-import.png)

In the dialogue, edit the sprite dimensions. This step is important if your spritesheet is an animation with more than one frame. For this box example, we are using a non-animated one-frame spritesheet. 

![prop-spritesheet-edit](/entity-framework/img/prop-spritesheet-edit.png)

Confirm your changes and you will see that the spritesheet is now added to the Resources tab:

![prop-spritesheet-resourceview](/entity-framework/img/prop-spritesheet-resourceview.png)

## Adding props to a map
Create an object layer on your map to store all Props. We will simply call this `props`, but you can of course get as detailed as you want with layer naming. Then select the layer to add objects to it.

![prop-layer](/entity-framework/img/prop-layer.png)

### Adding props from the right-click menu / via shortcut
You can right-click anywhere on the map view to open the `Add...` dialogue that lets you place props. This is equivalent to simply hitting `Ctrl + 1`. 

![prop-add-rightclick](/entity-framework/img/prop-add-rightclick.png)

You are now in add mode and can left-click + drag a rectangle on the map that will be your prop object's bounding box.

![prop-add-boundingbox](/entity-framework/img/prop-add-boundingbox.png)

Once you release the mouse button, the object will be created.
Now, select the correct spritesheet from the `Sprite` dropdown menu.

![prop-add-spriteselect](/entity-framework/img/prop-add-spriteselect.png)

You've created your first Prop! To make sure its collision behaves correctly, go to the `Collision` tab and adjust the collision box dimensions. Or just deactivate collision entirely - it's up to you!

![prop-add-collision](/entity-framework/img/prop-add-collision.png)


### Adding props from the resources tab
There is an even more convenient way to add props! You can just add them directly from the resources tab by selecting a prop spritesheet and then hitting the little `+` button below:

![prop-add-direct](/entity-framework/img/prop-add-direct.png)

On the currently selected object layer, this will magically create a new object that already has its bounding box and spritesheet preconfigured.

## Behold! A box!
Once you've added the prop object and configured it to your liking, you're done! Save your map, load up the game, and marvel at our glorious box:

![prop-ingame](/entity-framework/img/prop-ingame.png)

The box will be loaded from the Map as an instance of the `de.gurkenlabs.litiengine.entities.Prop` class. I.e., the box can be animated, has collision, and can be damaged in combat.

## PropStates

As a rough approximation for the visual destruction of a prop, it will take one of three states, depending on how many of its initial hitpoints it has left.
* INTACT: The prop is indestructible OR has more than half of its hitpoints left.
* DAMAGED: The prop has less than half of its hitpoints (but more than zero) left.
* DESTROYED: The prop has no hitpoints left

While the `prop-box` or `prop-box-intact` spritesheet will be used to animate our box as long as it is INTACT, we can also import spritesheets for the damaged and destroyed box. Call them `prop-box-damaged` and `prop-box-destroyed` and import them just like our intact spritesheet. The `PropAnimationController` will make sure to switch the spritesheet automatically as soon as our box takes enough damage. The reverse is also true: once a damaged prop's hitpoints are restored, it will show the INTACT spritesheet again.


## Registering custom Prop Types
If you have a Prop placed on your Map already and want it to be an instance of a custom Prop implementation rather than a generic `Prop`, there is a simple mechanism to register custom prop types.

Start by implementing a class that extends the Prop class. It is important to add an `@AnimationInfo` annotation and set the `spritePrefix` to `prop-box`.

```java
import de.gurkenlabs.litiengine.Game;
import de.gurkenlabs.litiengine.entities.AnimationInfo;
import de.gurkenlabs.litiengine.entities.Prop;
import java.awt.Color;

@AnimationInfo(spritePrefix = "prop-box")
public class Box extends Prop {

  public Box(String spritesheetName) {
    super(spritesheetName);
    System.out.println("Box constructed!");
    onRendered(rl -> {
      rl.getGraphics().setColor(Color.CYAN);
      Game.graphics().renderOutline(rl.getGraphics(), getHitBox());
    });
  }
}
```

Now there is only one step left:
Register a custom MapObjectLoader that creates a `Box` instance from all prop objects on our map with the `prop-box` sprite prefix.

During early initialization of your game (usually even before `Game.init()` in the main method), Use `PropMapObjectLoader.registerCustomPropType(Box.class);`, to apply our custom Box implementation to the box props. 

With the example implementation above, we can see the hitboxes of our props rendered. Of course, this is just a trivial example to demonstrate the concept of custom props. Experiment with custom prop types to add Emitters, interaction, sounds, or whatever you come up with!

![prop-custom-ingame](/entity-framework/img/prop-custom-ingame.png)
