---
meta.description: "Quick reference cheat sheet for LITIENGINE API - essential methods and classes at a glance."
meta.keywords: "LITIENGINE, cheat sheet, quick reference, API, Java"
---

# API Quick Reference

A cheat sheet of essential LITIENGINE API methods and patterns.

## Game Lifecycle

```java
Game.init(args);                           // Initialize engine
Game.start();                              // Start game loop
Game.exit();                               // Terminate game

Game.info().setName("My Game");            // Set game name
Game.info().setVersion("v1.0.0");          // Set version
```

## Game Components

```java
Game.loop()              // Game loop (logic + rendering)
Game.graphics()          // Render engine
Game.audio()             // Sound engine
Game.physics()           // Physics engine
Game.tweens()            // Tween engine
Game.world()             // World/environment manager
Game.window()            // Game window
Game.screens()           // Screen manager
Game.config()            // Configuration
Game.info()              // Game metadata
Game.metrics()           // Performance metrics
Game.time()              // Game time utilities
Game.random()            // Random number generator
```

## World & Environment

```java
Game.world().loadEnvironment("level1");              // Load by name
Game.world().loadEnvironment(new Environment(map));  // Load instance
Game.world().environment();                          // Current environment
Game.world().camera();                               // Current camera

Game.world().environment().get("entityName");        // Get entity by name
Game.world().environment().getByType(Creature.class); // Get by type
Game.world().environment().getByTag("enemy");        // Get by tag
Game.world().environment().add(entity);              // Add entity
Game.world().environment().remove(entity);           // Remove entity
```

## Game Loop

```java
Game.loop().attach(updateable);           // Register for updates
Game.loop().detach(updateable);           // Unregister
Game.loop().getDeltaTime();               // Ms since last tick
Game.loop().getTicks();                   // Total ticks
Game.loop().getTickRate();                // Ticks per second
Game.loop().setTickRate(30);              // Change tick rate
Game.loop().execute(60, () -> {...});     // Execute after 60 ticks
```

## Input

```java
Input.keyboard()                          // Keyboard access
Input.mouse()                             // Mouse access
Input.gamepads()                          // Gamepad manager

// Keyboard
Input.keyboard().onKeyPressed(KeyEvent.VK_SPACE, e -> {...});
Input.keyboard().onKeyReleased(KeyEvent.VK_SPACE, e -> {...});
Input.keyboard().isPressed(KeyEvent.VK_SPACE);

// Mouse
Input.mouse().getLocation();              // Current position
Input.mouse().isLeftMouseButtonDown();
Input.mouse().isRightMouseButtonDown();
Input.mouse().onClicked(e -> {...});
Input.mouse().onMoved(e -> {...});

// Gamepad
Input.gamepads().getCurrent();
Input.gamepadManager().onPressed(Gamepad.Xbox.A, value -> {...});
```

## Rendering

```java
Game.graphics().renderText(g, "text", x, y);
Game.graphics().renderShape(g, shape);
Game.graphics().renderImage(g, image, x, y);
Game.graphics().setBaseRenderScale(3f);
```

## Audio

```java
Game.audio().playSound("sound.wav");
Game.audio().playSound("sound.wav", x, y);     // At location
Game.audio().playMusic("music.mp3");
Game.audio().stopMusic();
Game.audio().setSoundVolume(0.5f);
Game.audio().setMusicVolume(0.8f);
```

## Physics

```java
Game.physics().move(entity, angle, pixels);
Game.physics().add(collisionEntity);
Game.physics().remove(collisionEntity);
Game.physics().raycast(start, end);
```

## Resources

```java
Resources.load("game.litidata");                    // Load bundle

Resources.images().get("image.png");                // Load image
Resources.sounds().get("sound.wav");                // Load sound
Resources.fonts().get("font.ttf", 24f);             // Load font
Resources.spritesheets().get("player-idle");        // Get spritesheet
```

## Entities

### Creating

```java
@EntityInfo(width = 32, height = 32)
@CollisionInfo(collision = true, collisionBoxWidth = 28, collisionBoxHeight = 28)
@MovementInfo(velocity = 100)
@CombatInfo(hitpoints = 50)
public class Enemy extends Creature {
  public Enemy() {
    super("enemy");
  }
}
```

### Common Methods

```java
entity.getName();
entity.getLocation();
entity.setLocation(x, y);
entity.getWidth() / entity.getHeight();
entity.getBoundingBox();
entity.getCenter();
entity.getTags();
entity.hasTag("enemy");

// Collision
collisionEntity.hasCollision();
collisionEntity.getCollisionBox();

// Combat
combatEntity.getHitpoints();
combatEntity.getMaxHitpoints();
combatEntity.hit(damage);
combatEntity.isDead();

// Movement
mobileEntity.getVelocity();
mobileEntity.setVelocity(100);
mobileEntity.getAngle();
```

## Entity Events

```java
entity.onAdded(e -> {...});
entity.onRemoved(e -> {...});
combatEntity.onHit(e -> {...});
combatEntity.onDeath(e -> {...});
mobileEntity.onMoved(e -> {...});
collisionEntity.onCollision(e -> {...});
```

## Animation

```java
entity.getAnimationController().play("walk");
entity.getAnimationController().getCurrentAnimation();
```

## Screens

```java
public class MenuScreen extends Screen {
  public MenuScreen() {
    super("MENU");
  }
  
  @Override
  protected void initializeComponents() {
    // Add GUI components
  }
  
  @Override
  public void render(Graphics2D g) {
    // Custom rendering
  }
}

Game.screens().add(new MenuScreen());
Game.screens().display("MENU");
Game.screens().current();
```

## Tweens

```java
Game.tweens().begin(entity, TweenType.LOCATION_XY, 1000)
    .target(200, 300)
    .ease(TweenFunction.QUAD_INOUT)
    .begin();
```

## Camera

```java
Game.world().camera();
camera.setFocus(entity);
camera.setZoom(2f);
camera.getViewport();
```

## Configuration

```properties
# config.properties
gfx_fullscreen=false
gfx_enableResolutionScale=true
cl_maxFps=60
cl_showGameMetrics=true
client_updaterate=60
```

## Common Patterns

### Basic Game Setup

```java
public static void main(String[] args) {
  Game.info().setName("My Game");
  Game.init(args);
  Resources.load("game.litidata");
  Game.world().loadEnvironment("level1");
  Game.start();
}
```

### Entity with Update Logic

```java
public class Enemy extends Creature implements IUpdateable {
  public Enemy() {
    super("enemy");
    Game.loop().attach(this);
  }
  
  @Override
  public void update() {
    if (isDead()) {
      Game.loop().detach(this);
      return;
    }
    // AI logic
  }
}
```

### Custom Movement Controller

```java
@Override
protected IMovementController createMovementController() {
  KeyboardEntityController<Player> c = new KeyboardEntityController<>(this);
  c.addUpKey(KeyEvent.VK_W);
  c.addDownKey(KeyEvent.VK_S);
  c.addLeftKey(KeyEvent.VK_A);
  c.addRightKey(KeyEvent.VK_D);
  return c;
}
```
