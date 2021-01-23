# Creating an Arkanoid 2D Block Breaker Game

> This LITIENGINE tutorial was written by [@YannikSchoeberl](https://github.com/YannikSchoeberl) and originally published on the LITIENGINE community forum.

## Tutorial Introduction

Hi there!

Three weeks ago, I started working with the LITIENGINE. I'm using the engine to program my own version of Arkanoid (a breakout game) as my student research project for university.

In the beginning, it wasn't easy to figure out how to get things done with the LITIENGINE because at the moment, there is just few documentation. Nevertheless, the docs pages for the most basic things of the engine are there, you can find them here: https://litiengine.com/docs

To understand the more specific parts of the engine and how to use them to achieve what I want to, I had a few looks into the game **"SERVUS BONUS"** which was made for LDJAM 44 with the LITIENGINE. You can find the source code of this game here: https://github.com/gurkenlabs/litiengine-ldjam44

Back to my game:

Currently, the basics of Arkanoid are there, which means there are blocks to break, a ball to break those blocks, and a pad that can be moved by the player to prevent the ball from falling down. In the picture below, you can see my first level out of three total.

![Arkanoid Clone Screenshot](images/arkanoid-screenshot1.jpeg)

The third level is a boss level, as you can see below. The boss has 25 lives in my case.

![Arkanoid Clone Boss Level](images/arkanoid-screenshot2.jpeg)

My game also contains a **menu** to reach different options:
1. Start the game
2. How to play
3. Highscore list with player names and scores
4. Settings (currently you only can choose between three difficulties, the more difficult the more faster is the ball)
5. Gallery (just showing 4 retro images of original Arkanoid game covers
6. Exit the game

In this **LITIENGINE tutorial**, you will learn how to create the most important parts of the block breaker game I created with the LITIENGINE.

## How to create maps, use them with utiLITI and import them as a .litidata file

In this first chapter of my tutorial, we will have a look on how to create maps and add them to a game.

First of all, we need to create one or more maps with the Tiled Map Editor which you can download here: https://www.mapeditor.org/

After downloading the editor, you need a picture that contains your tiles and open it in the Tiled Map Editor to create a tileset. To do that, you have to open the editor and choose `New Tileset...`

![Tiled Editor Screenshot](images/tiled1.jpeg)

After that, the following window shows up:

![Tiled Editor New Tileset](images/tiled2.jpeg)

Here you need to specify the image containing your tiles and the width and height of your tiles. After saving the tileset, go to the context menu in the upper left corner of the Tiled Map Editor and select `File -> New -> New Map...`. After that, the following window shows up:

![Tiled Editor New Map](images/tiled3.jpeg)

Here you can specify the size of your map or choose an infinite sized map. The next step is then to create the map with tiles from the created tileset and save it. That's all you need to know about the Tiled Map Editor. Let's have a look at the next step: processing the map(s) in the **utiLITI editor**. To get things started, you need to have the utiLITI editor on your computer. If you don't have the editor, get it here: [LITIENGINE SDK Download](https://litiengine.com/download/)

How to create a new game file and import your map is well documented in the LITIENGINE docs: https://litiengine.com/docs/utiliti-editor/

With `Edit -> Add...` you can add Props, Creatures, Spawnpoints, etc. to your map(s) and within the "Resources" context menu you can import all sprites, sounds, etc. you need for your game. After saving your .litidata file, we proceed to the last step of this first chapter of the tutorial: importing the .lititdata file via source code. In your main method, after the call of

```java
Game.init(args);
```

you then have to import the .litidata file like this:

```java
Resources.load("sample.litidata");
```

If the file is located in your game's root folder, then you only have to specify the name. If the file is not in your game's directory, then you have to specify the full path. That's how to create and import maps to use them. Let's have a quick look at how to display a map. To display a map, you have to create a class that extends the Screen class. In a GameHandler/GameManager class then call

```java
Game.world().loadEnvironment("mapName");
```

After that, you have to add a render method to your screen like this:

```java
@Override 
public void render(Graphics2D graphics) { 
  if (Game.world().environment() != null) { 
    Game.world().environment().render(graphics); 
  }

  super.render(graphics); 
}
```

That's it! Now your map should be rendered on your screen so that you can see it. Screens can be displayed with

```java
Game.screens().display("screenName");
```

## How to create the pad

In this chapter, we will have a look on how I created the pad, which means the player in my game. First, we will create a class **Player**. This class extends `Creature`, it implements `IUpdateable` and `IRenderable`.

```java
public class Player extends Creature implements IUpdateable, IRenderable 
{...}
```

Right above the class, we add some annotations which contain information about our player entity (sample from my game):

```java
@EntityInfo(width = 216, height = 16) 
@MovementInfo(velocity = 2000) 
@CollisionInfo(collisionBoxWidth = 216, collisionBoxHeight = 16, collision = true)
```

Let's have a look at the constructor. In my case it's a private constructor in which the sprite(s) of the player is set and a movement controller is added:

```java
private Player() { 
  super("vaus"); 
  KeyboardEntityController playerController = new KeyboardEntityController<>(this); 
  playerController.addLeftKey(KeyEvent.VK_LEFT); 
  playerController.addRightKey(KeyEvent.VK_RIGHT); 
  this.setController(IMovementController.class, playerController); 
}
```

In my case, the movement controller only needs the right and the left key. The sprites you want to use for your player need to be added to your .litidata file in the utiLITI editor and have to follow the naming conventions you can find here: https://litiengine.com/docs/tutorials/creating-a-platformer/

The class also keeps track of its instance, so it needs a variable for this:

```java
private static Player instance;
```

The last thing we need for our Player class is a public method to get the instance of our player from everywhere in our source code. We achieve this with the following method:

```java
public static Player instance() { 
  if (instance == null) { 
    instance = new Player(); 
  } 

  return instance; 
}
```

That's everything I needed inside my player class (except some member variables to keep track of the player's lives, name, and score and getter/setter methods for those variables).

To let our player instance appear in our game, we then need to spawn it. In my game, I added a LoadedListener in the init() method of my GameHandler class which then spawns my pad (the player) if a level was loaded and sets its location to the center bottom of the screen:

```java
Game.world().addLoadedListener(e -> { 
  Spawnpoint enter = e.getSpawnpoint("enter"); 
  if (enter != null) { 
    enter.spawn(Player.instance()); 
  } 
  
  Player.instance().setLocation(Game.window().getResolution().getWidth() / 2 - Player.instance().getWidth() / 2, 
                                Game.window().getResolution().getHeight() * 0.95); 
}
```

This code snippet only works if there's a `Spawnpoint` with the name "enter".

That's it! We successfully created the pad of the game.

## How to create the ball

In this chapter of the tutorial, we will deal with the creation of the ball and its behavior. As this is the most complex part of my game, this chapter will be the largest of this tutorial. To keep it in a reasonable size, I will not go into every detail.
Let's start with the class Ball:

```java
public class Ball extends Creature implements IUpdateable, IRenderable 
{...}
```

The class Ball extends Creature and implements IUpdateable and IRenderable just like our Player class. We also add some annotations to deliver some information about our ball entity:

```java
@EntityInfo(width = 64, height = 64) 
@MovementInfo(velocity = 2000) 
@CollisionInfo(collisionBoxWidth = 64, collisionBoxHeight = 64, collision = true)
```

To keep track if the ball is currently moving or not, the class contains an enum BallState:

```java
public enum BallState { 
  IDLE, 
  INGAME 
}
```

Also, we need variables to save the current state and the current instance:

```java
private static BallState state; 
private static Ball instance;
```

The constructor of the class is quite simple:

```java
private Ball() { 
  super("ball"); 
}
```

So everything is just like inside the Player class but without a movement controller. Additionally, we again need a method to get the current instance of the ball from everywhere in our source code:

```java
public static Ball instance() { 
  if (instance == null) { 
    instance = new Ball(); 
  } 

  return instance; 
}
```

The last two methods of the Ball class are the most important ones: `update()` and `render()`.

Let's start with the update method:
The update method checks if the ball touches the bottom of the screen which then results in losing a life for the player:

```java
@Override 
public void update() { 
  if (Ball.instance().getLocation().getY() + Ball.instance().getHeight() >= Game.window().getResolution().getHeight()) { 
    GameHandler.lifeLost(); 
  } 
}
```

I won't further go into the `lifeLost()` method because this doesn't belong to the ball. Last but not least there's the render method:

```java
@Override 
public void render(Graphics2D graphics2D) { 
  if (state == BallState.INGAME) { 
    boolean isMoving = Game.physics().move(Ball.instance(), Ball.instance().getAngle(), Ball.instance().getTickVelocity()); 
    if (!isMoving) { 
      double newAngle;

      if (Ball.instance().getLocation().getY() + Ball.instance().getHeight() >= Player.instance().getLocation().getY()) { 
        newAngle = getAngleOfDynamicCollision(); 
      } else { 
        newAngle = getAngleOfStaticCollision(); 
      } 

      Ball.instance().setAngle(newAngle); Game.physics().move(Ball.instance(), Ball.instance().getAngle(), Ball.instance().getTickVelocity()); 
    } 
  } 
}
```

To move the ball, an angle is needed. Initially, the angle is set to 180° which is straight-up (is set in the GameHandler class). The move method returns a boolean which turns false if the ball stops moving because of a collision. If this happens, my game distinguishes between a collision with the pad and any other object because the pad has two zones on the sides where the ball is deflected with a greater angle than it came in on the pad. I won't go into detail on how the new angle is calculated because this would go too far for this tutorial.

After calculating the new angle, this angle is set and the ball is moved again with the new angle after the collision.

Later on, when there are blocks in the game, there has to be a mechanism to detect which block was hit by the ball. But as seen, the move method only returns a boolean and not the hit object. So I just used simple maths to solve this: if there's a collision with a block I calculate the distance from the center of the ball to the center of every block. The block with the smallest distance is the one which was hit.

That was a lot of code for the Ball class. To get the ball working, we also need some more code in the GameHandler class. Just like the player, the ball is spawned on the map when a map was loaded. You need to add:

```java
Spawnpoint enterBall = e.getSpawnpoint("enter_ball"); 
if (enterBall != null) { 
  enterBall.spawn(Ball.instance()); 
}
```

to the `LoadedListener` inside the `init()` method of the GameHandler class. This will only work if a Spawnpoint with the name "enter_ball" was defined in the loaded map.

Also, we add a listener for the space key of the keyboard inside the `init()` method of the GameHandler which then calls the `startBall()` method:

```java
Input.keyboard().onKeyPressed(e -> { 
  if (e.getKeyCode() == KeyEvent.VK_SPACE) { 
    if (GameHandler.getState() == GameState.INGAME && Ball.getState() == Ball.BallState.IDLE) { 
      startBall(); 
    } 
  } 
});

private static void startBall() { 
  Ball.instance().setAngle(180);  
  Ball.instance().setVelocity(GAMESPEED);  
  Ball.instance().setAcceleration(500);  
  Ball.setState(Ball.BallState.INGAME); 
}
```

The `startBall()` method sets the initial speed (depends on selected difficulty) and acceleration of the ball. Also, the initial angle (180°) is set. By setting the BallState to INGAME, the render method of the ball will start to move it.
Finally, we need one more snippet of code to handle the ball's behavior when its state is IDLE:

```java
@Override 
public void update() { 
  if (Ball.getState() == Ball.BallState.IDLE) { 
    Point2D locationOfPlayer = Player.instance().getLocation(); 
    Ball.instance().setLocation(locationOfPlayer.getX() + 76, locationOfPlayer.getY() - 67); 
  } 
}
```

This snippet is the update method of my IngameScreen class. It updates the ball's position when the pad is moved so that the ball is always centered on top of the pad.
That's it! We created the ball of the game.

## How to create the blocks

To get the blocks in our map, we need to add the sprites of them to our **utiLITI** project. The image below shows my first level and at the bottom, you can see all imported sprites.

![utiLITI Block Breaker](images/utiliti-block-breaker.jpeg)

On the right, you can see the options you have to configure the block. You can set its size, its sprite, and its location. If you want to add another block from a loaded sprite, just click on the sprite and then on the "+" symbol.

We also need to specify the collision properties of each block. The corresponding menu is also on the right and looks like this:

![utiLITI configure collision](images/utiliti-configure-collision.jpeg)

In this menu, you can set the size, type, and location of the collision box of the block.

After adding the desired blocks and saving the .litidata file, we need to write a little bit of source code.
We add the following lines to the Ball class in a method which handles the collision of the ball with a block:

```java
int points = Block.getPointsOfBlock(hitObject.getSpritesheetName()); 
GameHandler.increasePoints(points); Game.world().environment().remove(hitObject);
```

The method `getPointsOfBlock()` returns the points the player earns for destroying a block depending on its color which is retrieved from the spritesheet name of the block. The last line then removes the block.
If the game is restarted later, the block will still be destroyed. To let it appear again, I just used the following code snippet to iterate over all levels and reset them:

```java
for (int i = 0; i <= MAX_LEVEL; i++) { 
  Game.world().reset(Resources.maps().get("level" + i)); 
}
```

That's it! We created the blocks of the game.

## How to add sounds and music

In this chapter of the tutorial, we will have a look at how to play a sound or music in a game. First of all, you need to add all sounds and music to the .litidata file of your game. After that, you can play a sound everywhere in the code with:

```java
Game.audio().playSound("name_of_sound_in_.litidata_file");
```

To play some music, you have to write the following code inside the update method of the screen you want to play the music on:

```java
@Override 
public void update() { 
  if (this.lastPlayed == 0) { 
    Game.audio().playMusic("menu_music"); 
    this.lastPlayed = Game.loop().getTicks(); 
  }
}
```

To get this working, the class you wrote this in needs a variable:

```java
public long lastPlayed;
```

As I experienced, sometimes the music doesn't start playing. In this case, simply call

```java
update();
```

inside the `prepare()` method of your screen.

Now you can add music and sound effects to your game!
You've reached the end of this tutorial, **thanks for reading** 😊

I hope this tutorial helped you.