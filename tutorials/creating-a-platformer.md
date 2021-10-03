# Creating a platformer with LITIENGINE

So, you’ve learned about LITIENGINE – great!

You’ve created a project in eclipse and imported LITIENGINE.
If not, check out our [Download Page](https://litiengine.com/download/) that comes with detailed installation instructions.

Now you’ve probably come to the point where you’ve asked yourself:
> “How am I supposed to actually make a game with this?”

In this How-To-Series, we guide you through the steps necessary for creating a platformer game inspired by the old Duke Nukem games, made in a glorious four-colour gameboy look.

The this project is entirely open sourced (under the MIT license). You can find the code among all the assets in the [GitHub repository for Gurk Nukem](https://github.com/gurkenlabs/litiengine-gurk-nukem).
![Gurk Nukem Title](images/gurknukem-title.png)

Each blog chapter will represent the work that can be done in one day by following our step-by-step explanations.

## Chapter 1:  The first Level

### Creating a project in utiLITI
For a general idea about what utiLITI is, read the [docs page about utiLITI](https://litiengine.com/docs/utiliti-editor/) first.

Start the utiLITI editor. Hit "**File -> New...**"  (`CTRL+N`)

![utiLITI Create Project](images/utiliti-create-project.png)

In the file browser that pops up, navigate to your project directory and hit "**Open**".
Even if you still have done nothing, hit "**File -> Save...**" (`CTRL+S`) to create a game resource file.
You can name it whatever you want, we go for something like “game.litidata” in this guide.

### Importing Assets
Let’s assume that you’ve already created assets for your game. In our case, we picked a 4-colour GameBoy style for our project.
So what basic Assets do we have at this point?

**Player sprites:** 

For entities that are child classes of Creature, there are naming conventions for walking and idle sprites.

We need sprites named like `{SPRITE_PREFIX}-{STATE}-{DIRECTION}.{EXTENSION}`.
Following these naming conventions, we create **gurknukem-idle-left.png** and **gurknukem-walk-left.png**.
You only need to provide a left or a right sprite in both cases, the CreatureAnimationController will automatically flip it when necessary.

![Gurk Nukem Idle Left](images/gurknukem-walk-left.png)
 
*gurknukem-walk-left.png*

**Enemy sprites:** 

We also add two enemy designs to the game. The naming is done in the same way as for our main character, so we end up with four image files: **dean-idle-left.png**, **dean-walk-left.png**, **jorge-idle-left.png**, and **jorge-walk-left.png**.


![Dean Walk Left](images/Dean-walk-left.png)
 
*dean-walk-left.png*


![Jorge Walk Left](images/Jorge-walk-left.png)
 
*jorge-walk-left.png*

**Prop sprites:**

For now, we will only add two props: a bunker and a destructive barrel.
For props, there are naming conventions, too:
`prop-{PROPNAME}-{STATE}.{EXTENSION}`

This means that we need three image files for our destructible barrel:
**prop-barrel-intact.png**, **prop-barrel-damaged.png**, and **prop-barrel-destroyed.png**
Non-destructible props such as our bunker only need one animation file, in our case prop-bunker.png.

![Prop Bunker](images/prop-bunker.png)
 
*prop-bunker.png*

![Prop Barrel](images/prop-barrel.png)
 
*prop-barrel.png*

**Our game logo:**

![Gurk Nukem Logo](images/gurknukem-logo.png)

* **Our game icon:**

![Gurk Nukem Icon](images/gurknukem-icon.png)

We also need:
* **A music track**
* **A .tsx tileset created with Tiled editor from an image file**
* **A .tmx map created with Tiled editor using our Tileset**

To import Sprite files into utiLITI, either **drag&drop selected files into the Asset panel** on the lower end of the screen or hit "**Resources -> Import Spritesheets...**". The same goes for tilesets ("**Resources -> Import Tilesets...**"). Maps can be imported by clicking "**Map -> Import...**". If a map was successfully imported, it will be rendered in the map panel and listed in the map list right to it.

![An example map and some spritesheets loaded into utiLITI](images/2-levelLoaded-768x515.png)

### Basic mapping
Adjust your grid and snapping settings in the "**View**" menu.

In the **Layer** toolbox in the upper right corner, you can **Add, Delete, Recolor, Rename, Duplicate, Focus / Hide, and reorder** MapObjectLayers.
To maintain a comprehensive structure to our map files, we try to create at least one layer for each Entitytype (There is the “Entities” tab to help you navigate through entities by type, as well).

Let us now create your first `Entity`!
Select a MapObjectLayer, then right-click somewhere on the map and hit "**Add -> Add CollisionBox**".
**Click and drag** with your mouse to specify the bounding box of your Collision box as shown in the gif below.

![Creating a Collision Box in utiLITI](images/3-createCollision.gif)

In the same manner, create a `Spawnpoint` that will be used to spawn our player entity.
Edit the Spawnpoint’s Attributes in the Map Object Panel on the right as shown below.
You can give the Spawpoint a name for identification and set the spawn direction for our Player.

![Editing Spawnpoint attributes](images/4-spawnpointSetup.gif)

Before we look into coding now, we will set some basic properties for your map such as its name, description, and static shadow color.
Simply hit "**Map -> Properties**" and you will see a popup for editing Map properties.

![Editing Map properties in utiLITI](images/5-mapProperties.gif)

**Congratulations!** You’ve successfully completed the first steps on your way to creating a platforming shooter with LITIENGINE.
Learn about setting up the basic functionality of our game in the next chapter.

## Chapter 2: Time to pull out your hacker gloves

Now that you've created a first test map for your platforming game, we will show you how to load the map into your game, how to configure and spawn a Player entity, and how to implement basic gravity and jumping behaviours.

### Our Main Class

Let's start today by opening up the Eclipse IDE (as it is the IDE of choice for this how-to-series).

At this point, we assume that you've already created a Java project and referenced LITIENGINE in it as described [HERE](https://litiengine.com/docs/getting-started/).
Also, you have created resource folders and added them to your project's build path.
In our case, there are three resource folders: 'maps', 'sprites', and 'audio', which are located in the root folder of our project.

We proceed with creating a class containing our `main`-method to actually run our program like in the example shown below:

```java
public class Program { 
  public static void main(String[] args) { 
    // set meta information about the game 
    Game.info().setName("GURK NUKEM"); 
    Game.info().setSubTitle("");
    Game.info().setVersion("v0.0.1"); 
    Game.info().setWebsite("https://github.com/gurkenlabs/litiengine-gurk-nukem"); 
    Game.info().setDescription("An example 2D platformer with shooter elements made in the LITIENGINE"); 
    
    // init the game infrastructure 
    Game.init(args); 

    // set the icon for the game (this has to be done after initialization because the ScreenManager will not be present otherwise) 
    Game.window().setIcon(Resources.images().get("icon.png")); 
    Game.graphics().setBaseRenderScale(4f); 

    // load data from the utiLITI game file 
    Resources.load("game.litidata"); 
    
    // load the first level (resources for the map were implicitly loaded from the game file) 
    Game.world().loadEnvironment("level1"); 
    Game.start(); 
  }
}
```
-   First, we set some basic information for our game such as its name,
    subtitle, version, website, and description by using the respective
    setters of `Game.info()`.
-   Calling `Game.init()` is then needed to initialize the Game
    infrastructure (see the [Javadocs][] for an in-depth understanding
    of what this does).
-   Next, we set the window icon from the logo we created in Day 1 by
    calling `Game.window().setIcon()`. *Fancy!* Of course,
    the image file 'icon.png' has to be present in our project for this
    to work.
-   Our game world will be scaled by a factor of 4, which we achieve
    with `Game.graphics().setBaseRenderScale()`.
-   Now we load up our game resource file created with utiLITI in Day 1.
    Just call `Resources.load("game.litidata")` and all our
    maps, sprites, etc. will be accessible directly from code hereafter.
-   Let's try loading our 'level1' with
    `Game.world().loadEnvironment("level1")`.
-   The last thing needed to get our game running is `Game.start()`.

We've all been waiting for this moment, let's go ahead and **RUN THE GAME!**

But wait, what's this? Our game window is there, but it doesn't show anything.

### The Ingame Screen

As it would be nice to actually have our game shown in the empty window, we need to *render the game world*.
For this purpose, we create an `IngameScreen` that extends `GameScreen`.

```java
public class IngameScreen extends GameScreen { 
  public static final String NAME = "INGAME-SCREEN"; 

  public IngameScreen() { 
    super(NAME); 
  } 
}
```

Once we add the `IngameScreen` to the `ScreenManager` by calling `Game.screens().add(new IngameScreen())` in our main-method, two magic things happen:

-   Since there was previously no `Screen` present, adding a new one
    will also call `ScreenManager.display()`, making *the newly added*
    `IngameScreen` the currently visible screen.
-   Every `Screen` extending `GameScreen` contains a call to
    `Game.world().environment().render()`in its `render()`-method.
    **Just remember:** Once you override the
    `GameScreen.render()`-method, you'll need to reference the inherited
    behaviour with `super.render()` or else the game world won't be
    rendered.

Running the game again, we finally see something happening in our window!

![Ingame Screen](images/6-ingamescreen.png)

Right now, we only see the upper left corner of our map since we haven't defined any `Camera` yet. The default camera is locked to the map coordinates (0,0).
You can enable and disable the game metrics shown in the image above, as well as other debug options, by modifying the `config.properties`-file in your project's main directory:

 - Set the variable `cl_showGameMetrics` to **true** to see basic info about fps, ups, and networking performance.

### A noble Hero

Finally, we can put our awesomely edgy main protagonist inside the game!
For this, we utilize LITIENGINE's `Entity` framework. Let's go ahead and create a `Player`-class:

```java
@EntityInfo(width = 18, height = 18) 
@MovementInfo(velocity = 70) 
@CollisionInfo(collisionBoxWidth = 8, collisionBoxHeight = 16, collision = true) 
public class Player extends Creature implements IUpdateable { 
  private static Player instance; 
  
  public static Player instance() { 
    if (instance == null) { 
      instance = new Player(); 
    } 
    
    return instance; 
  } 
  
  private Player() { 
    super("gurknukem");
  } 
  
  @Override 
  public void update() { 
  }

  @Override
  protected IMovementController createMovementController() {
    // setup movement controller
    return new PlatformingMovementController<>(this);
  }
}
```

Right at the top, you'll notice the [annotations](https://docs.oracle.com/javase/tutorial/java/annotations/basics.html). This is what they do:

-   `EntityInfo` specifies basic properties that all `Entities` have,
    namely their width, height, and RenderType.
-   `MovementInfo` is exclusive to `MobileEntities`: It contains
    movement attributes such as velocity or acceleration.
-   `CollisionInfo`constitutes the size and alignment of a
    `CollisionEntity`'s collision box. .
-   Our Player is a child of `Creature`, meaning that it inherits
    everything from `CombatEntity`, `CollisionEntity`, and `Entity`,
    while also implementing the methods from `IMobileEntity` and
    `IUpdateable`. For a clearer unterstanding of the entity
    hierarchy, you can [have a look at the Javadocs](https://litiengine.com/api/) again.
-   We adopt a [Singleton pattern](https://community.oracle.com/docs/DOC-918906) for the `Player`-class, meaning
    that we only allow the existence of one single instance of `Player`
    at all times. Calling the public static `Player.instance()` will
    only invoke the private constructor on its first call. All future
    calls will return the same instance of `Player`.
-   In the `Player` 's private constructor, we invoke the constructor of
    superclass `Creature` with `super("gurknukem")`, where *'gurknukem'*
    is the so-called `spritePrefix` attribute of a `Creature`.
    We need to declare the `spritePrefix` so that the
    `CreatureAnimationController`, which is added in a  `Creature`'s
    constructor, will be able to associate the right Spritesheets with
    our Creature (remember the naming conventions for
    Spritesheets?).
-   Furthermore, we override the `createMovementController()`-method to add a `PlatformingMovementController` that allows us
    to move entities horizontally with player input. This method will be called upon the initialization of the `Player``.

For now, we leave the `update()`-method empty and focus on spawning our freshly created player into our game world.

### Where to put my Game logic?

To keep our `main()`-method as atomic and light as possible, we go ahead and create a class GurkNukemLogic, where we will initialize global game logic such as spawning behavior or defining cameras.

```java
public final class GurkNukemLogic { 

  private GurkNukemLogic() { 
  } 

  /** 
  * Initializes the game logic for the GURK NUKEM game. 
  */ 
  public static void init() { 
    // we'll use a camera in our game that is locked to the location of the player 
    Camera camera = new PositionLockCamera(Player.instance()); 
    camera.setClampToMap(true); 
    Game.world().setCamera(camera); 
    
    // set a basic gravity for all levels. 
    Game.world().setGravity(120); 
    
    // add default game logic for when a level was loaded 
    Game.world().onLoaded(e -> { 
      // spawn the player instance on the spawn point with the name "enter" 
      Spawnpoint enter = e.getSpawnpoint("enter"); 
      if (enter != null) { 
        enter.spawn(Player.instance()); 
      } 
    }); 
  }
}
```

-   LITIENGINE comes with a few basic pre-implemented cameras.
    Momentarily, we'll use a `PositionLockCamera` locked to the current
    position of our `Player` instance.
-   With `Game.world().setGravity(120)`, we apply a constant
    `GravityForce` to all `MobileEntities` in all levels.
-   Once an `Environment` is loaded, we want to spawn our player on the
    `Spawnpoint` with the name '*enter*'.

Note that `Entity` names are considered unique per level in LITIENGINE by design. If you want to retrieve a collection of  Spawnpoints from the environment to pick a random one from, you could add Tags to them in utiLITI and call 

```java
Game.world().environment().getByTag("tag1","tag2",...).
```

Once we call `GurkNukemLogic.init()` from our main()-method, we can now walk around the ground in our map and we'll even fall down into pits!

![Player walking on ground](images/7-walk-on-ground.gif)

Of course, there's one crucial thing missing here: **The ability to jump!**

But first, let's briefly create a class to manage all input (except player movement, which is already handled by the Player's **PlatformingMovementController**.

### Organizing Player Input

An odd thing you might have noticed by now is that you're not yet able to exit the game with any keypress.
For initializing our key bindings, we create the class `PlayerInput`:

```java
public final class PlayerInput { 
  
  private PlayerInput() { 
  } 
  
  public static void init() { 
    // make the game exit upon pressing ESCAPE (by default there is no such key binding and the window needs to be shutdown otherwise, e.g. ALT-F4 on Windows) 
    Input.keyboard().onKeyPressed(KeyEvent.VK_ESCAPE, e -> System.exit(0)); 
  } 
}
```

- For now, we bind `ESCAPE` to kill our program. Of course, this will change later on, but it will save some time in development.

Again, we need to call this code from our `main()`-method by adding `PlayerInput.init()` to it.

### Up we go - Implementing a Jump Ability

For the jump mechanic, we choose to utilize LITIENGINE's `Ability` framework. Go ahead and create the class `Jump`:

```java
@AbilityInfo(cooldown = 500, origin = EntityPivotType.COLLISIONBOX_CENTER, duration = 300, value = 240) 
public class Jump extends Ability { 
  
  public Jump(Creature executor) { 
    super(executor); 
    this.addEffect(new JumpEffect(this)); 
  } 
  
  private class JumpEffect extends ForceEffect { 

    protected JumpEffect(Ability ability) { 
      super(ability, ability.getAttributes().value().get().intValue(), EffectTarget.EXECUTINGENTITY); 
    } 
    
    @Override 
    protected Force applyForce(IMobileEntity affectedEntity) { 
      // create a new force and apply it to the player 
      GravityForce force = new GravityForce(affectedEntity, this.getStrength(), Direction.UP); 
      affectedEntity.movement().apply(force); 
      return force; 
    } 
    
    @Override 
    protected boolean hasEnded(final EffectApplication appliance) { 
      return super.hasEnded(appliance) || this.isTouchingCeiling(); 
    } 
    
    /** 
    * Make sure that the jump is cancelled when the entity touches a static collision box above it. 
    * 
    * @return True if the entity touches a static collision box above it. 
    */ 
    private boolean isTouchingCeiling() { 
      Optional opt = Game.world().environment().getCollisionBoxes().stream().filter(x -> x.getBoundingBox().intersects(this.getAbility().getExecutor().getBoundingBox())).findFirst(); 
      if (!opt.isPresent()) { 
        return false; 
      } 

      CollisionBox box = opt.get(); 
      return box.getCollisionBox().getMaxY() <= this.getAbility().getExecutor().getCollisionBox().getMinY(); 
    } 
  } 
}
```

-   As mentioned before, the class `Jump` is a child of LITIENGINE's
    `Ability`. As such, we can annotate the class with the
    `@AbilityInfo`-annotation to determine its cooldown, origin
    location, duration, and `value`, which is an abstract numeral used
    in different ways, depending on what your ability does.
-   In an `Ability`'s constructor, the `Creature` which casts the
    `Ability` is always passed as a parameter. In our case, we also add
    a `JumpEffect` to the `Jump`'s list of effects.
-   The inner class `JumpEffect` here is a `ForceEffect`, i.e. it will
    apply a given force to its affected entities. In its constructor, we
    establish its strength and `EffectTarget`.
-   In the `applyForce`-method, we create a `GravityForce` directed
    upward which adopts the `ForceEffect`'s strength. The force will
    then be applied to ability executor for the duration of the ability.
-   We also provide the `isTouchingCeiling`- condition for cancelling
    the `ForceEffect`, which determines if the jumping entity's
    collision box intersects any static collision box above it.

### Where it all comes together

Now, back to our `Player`-class, where we have to perform a few more adjustments, ending up with the following code:

```java
@EntityInfo(width = 18, height = 18) 
@MovementInfo(velocity = 70) 
@CollisionInfo(collisionBoxWidth = 8, collisionBoxHeight = 16, collision = true) 
public class Player extends Creature implements IUpdateable { 
  public static final int MAX_ADDITIONAL_JUMPS = 1; 

  private static Player instance; 
  private final Jump jump; 
  private int consecutiveJumps; 
  
  private Player() { 
    super("gurknukem"); 
    
    // setup the player's abilities 
    this.jump = new Jump(this); 
  } 
  
  public static Player instance() { 
    if (instance == null) { 
      instance = new Player(); 
    } 
    
    return instance; 
  } 
  
  @Override public void update() { 
    // reset the number of consecutive jumps when touching the ground 
    if (this.isTouchingGround()) { 
      this.consecutiveJumps = 0; 
    } 
  }

  @Override
  protected IMovementController createMovementController() {
    // setup movement controller
    return new PlatformingMovementController<>(this);
  }
  
  /** 
  * Checks whether this instance can currently jump and then performs the Jump ability. 
  *
  * Note that the name of this methods needs to be equal to {@link PlatformingMovementController#JUMP}} in order for the controller 
  * to be able to use this method.
  * Another option is to explicitly specify the Action.name() attribute on the annotation.
  */
  @Action(description = "This performs the jump ability for the player's entity.") 
  public void jump() { 
    if (this.consecutiveJumps >= MAX_ADDITIONAL_JUMPS || !this.jump.canCast()) { 
      return; 
    } 
    
    this.jump.cast(); 
    this.consecutiveJumps++; 
  } 
  
  private boolean isTouchingGround() { 
    // the idea of this ground check is to extend the current collision box by 
    // one pixel and see if 
    // a) it collides with any static collision box 
    Rectangle2D groundCheck = new Rectangle2D.Double(this.getCollisionBox().getX(), this.getCollisionBox().getY(), this.getCollisionBoxWidth(), this.getCollisionBoxHeight() + 1); 
    
    // b) it collides with the map's boundaries 
    if (groundCheck.getMaxY() > Game.physics().getBounds().getMaxY()) { 
      return true;
    } 
    
    return Game.physics().collides(groundCheck, Collision.STATIC); 
  } 
}
```

-   First, we declare the maximum number of mid-air-jumps, a `Jump`
    instance and the current number of consecutive jumps as fields.
-   Then, we write a `jump()`-method. It casts the Jump ability and
    raises the consecutive jump counter by one if the jump limit hasn't
    been reached and the `Jump` ability's `canCast()`-detection returns
    true. Adding the jump method at this point is also an
    introduction to a feature established in v0.5.0-beta:
    `EntityAction`s. For an intuition about their workings, let's have a
    look at the `PlatformingMovementController`: it can very well call
    all the methods that are declared by the `IMobileEntity` it is
    registered for. But what if we want the
    `PlatformingMovementController` to call logic that is exclusive to
    one single `Entity` implementing the `IMobileEntity` interface? For
    this purpose, there is a [reflection](https://docs.oracle.com/javase/tutorial/reflect/)-based system in LITIENGINE
    to call methods from `IEntities` that are otherwise inaccessible in
    certain places: Any  `IEntity` can declare an `@Action`-annotation
    on its methods. During runtime, these methods will be registered
    automatically by their method name and callable with
    `IEntity.perform(String actionName)`. Once the SPACEBAR (or any
    other declared jump key) is pressed, the
    `PlatformingMovementController` will call `Player.perform("jump")`
    to run the  `jump()`-method annotated with `@Action`.
    `EntityAction`s can also be registered explicitly without the
    annotation by using
    `IEntity.register(String name, Runnable action)`. However, you
    should try avoiding this approach whenever possible as using
    reflection can come with severe security risks (among other
    drawbacks)! In most cases, you should stick to the inheritance-based
    Entity framework that LITIENGINE provides.
-   Hereafter, we declare the `isTouchingGround()`-method, which returns
    true, if the player's collision box touches a static collision box
    or is intersecting with the lower map boundary.
-   In the `update()`-method, we reset the current jump counter to zero
    on collision.


![Player jumping around](images/8-jump-around.gif)

#### And that's it for today!

Sit back and enjoy your awesome player double-jumping around the platforms in your test map, just waiting for some foes to defeat!

There are binaries available on the ['Gurk Nukem' GitHub page](https://github.com/gurkenlabs/litiengine-gurk-nukem/releases). Head over there and compare your work to our reference project!
We can't wait to share more about the journey of creating games with LITIENGINE, so stay tuned.
