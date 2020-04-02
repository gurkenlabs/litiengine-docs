# 2D Graphics

## The Render Engine - `Game.graphics()`

The 2D `RenderEngine` is used to render texts, shapes, images and entities at their location in the `Environment` and with respect to the `Camera`'s location and zoom. Notice that the location lies within the coordinate space of the current `Environment`. The `RenderEngine` will translate the coordinates to a location on the screen.

Internally, it uses the static renderer implementations to actually execute the drawing operations on the `Graphics2D` object. This class basically prepares the specified render subject and passes them to a renderer with the current correct context.

```java
// render "my text" at the environment location (50/100)
Game.graphics().renderText(g, "my text", 50, 100);

// render "my text" at the location of an entity
Game.graphics().renderText(g, "my text", myEntity.getX(), myEntity.getY());

// render a rectangle (50x50 px) at the environment location (50/100)
Rectangle2D rect = new Rectangle2D.Double(50, 100, 50, 50);
Game.graphics().renderShape(g, rect);
```

> Rendering an `Entity` explicitly over the `RenderEngine` should never be necessary as long as the Entity was added to the game's current `Environment`. The rendering process of the current `Environment` takes care of drawing all the entities and implicitly calls these methods on the `RenderEngine`.

### Available Renderers

These classes can be useful when composing a GUI with images, text or shapes which are rendered at a certain location on the screen.

* **Image Renderer** \(renders `Images`\)
* **Shape Renderer** \(renders `Shapes`\)
* **Text Renderer** \(renders `Strings`\)

## Rendering Entities with a `Spritesheet`

The engine facilitates the usage of **Single-purpose spritesheets** to render entities with a matching sprite for their current state. Rendering an `Entity` is controlled by its assigned `AnimationController`. There is a pre-defined convention-based set of animation rules, that allows you to get quick results without having to write too much code. The LITIEngine works best with **single-purpose spritesheets**, i.e. every animation should have a dedicated spritesheet.

> It's possible to use a single spritesheet with multiple animations but the provided infrastructure for this is limited and it would probably end up in some custom code that defines which part of the spritesheet should be used by the animations.

### Animation

Any entity that uses a spritesheet needs an `AnimationController` which decides the spritesheet that should be rendered and provides the appropriate sprite for the `RenderEngine`.

In the following example, we use a `Player` entity that inherits from the default entity type `Creature`. The `CreatureAnimationController` which is assigned to all creatures provides the default animation rules for this type of entity.

![Example: Spritesheet for walking left - gurknukem-walk-left.png](../../.gitbook/assets/gurknukem-walk-left.png)

Notice the name of the spritesheet file above: `gurknukem-walk-left.png` - It follows the pattern: "SPRITE\_PREFIX"-"STATE"-"DIRECTION".png.

* The "SPRITE\_PREFIX" is determined by `Creature.getSpritePrefix()` which can either be set directly or specified in the creature's constructor.
* The default animation rules for creatures distinguish between 3 different "STATES": `idle`, `walk` and `dead`.
* As "DIRECTION" you can specify any value of the `Direction` enum. 

By default, the option to use flipped horizontal sprites as fallback is enabled, which means that you must only specify a sprite with either right or left direction.

Specifying a direction is optional and the `CreatureAnimationController` will also search for and use any fallback sprites without a defined direction.

In general, you are not limited to any of the pre-defined animation rules. You can decide to extend the animation controller or write one from scratch that better suits your needs.

More details on this can be found in the [Animation Controller](https://app.gitbook.com/@gurkenlabs/s/litiengine/basics/control-entities/animation-controller) chapter.

## The Graphics instance - `Graphics2D`

All of LITIengine's rendering happens on a **Java AWT** `Canvas` component and there's **no expicit OpenGL** involved. By that, the engine is one of the very few on the market that achieves an efficient rendering process with **plain Java**.

The `Canvas` provides a `Graphics2D` object which is passed though the engine on every frame and receives all the drawing operations. This object is basically an empty canvas we're drawing the elements of our game on.

For more information, read the [Official Java Documentation on Graphics2D](https://docs.oracle.com/javase/7/docs/api/java/awt/Graphics2D.html).

