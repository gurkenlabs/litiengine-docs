---
description: The TweenEngine is LITIENGINE's built-in interpolation framework.
---

# Tweening

The tweening framework is a powerful tool that allows you to animate properties of different types of objects in your game. It is a simple way to
create smooth interpolations, e.g. for position, size, rotation, opacity, and more.

## The Tweening Engine - `Game.tweens()`

The tweening engine is a part of the `Game` object and can be accessed via `Game.tweens()`. It is a singleton manager for all the Tween instances in
the game. The engine is responsible for updating all the active `Tweens` in the game, and it provides methods for creating, pausing, resuming, and stopping `Tweens`.
A `Tween` is an object that interpolates a value over time, using a specified easing function to create smooth transitions.
You can instantiate a `Tween` by calling the `Game.tweens().begin()` method and passing the target object, the type of value to interpolate, and the duration of the tween.
Then you can chain methods to set the starting and ending values, the easing function, and any additional properties.

```java
ImageComponent ic;
// Create a new Tween that moves the ImageComponent to the given location over 4 seconds, using a quadratic easing function.
Game.tweens().begin(ic, TweenType.LOCATION_XY, 4000)
    .target(100, 200)
    .ease(TweenFunction.QUAD_INOUT)
    .begin();
```

## TweenType

The `TweenType` enum defines the types of values that can be interpolated. Some examples include:

- `ANGLE`: Interpolates the angle of an object.
- `COLLISION_BOTH`: Interpolates both the width and height of the collision box.
- `COLLISION_HEIGHT`: Interpolates the height of the collision box.
- `COLLISION_WIDTH`: Interpolates the width of the collision box.
- `HITPOINTS`: Interpolates the hitpoints of a Combat Entity.
- `LOCATION_X`: Interpolates the X-coordinate of an object's location.
- `LOCATION_XY`: Interpolates the X- and Y-coordinate of an object's location.
- `LOCATION_XY`: Interpolates the Y-coordinate of an object's location.
- `SIZE_BOTH`: Interpolates both the width and height of an object.
- `SIZE_HEIGHT`: Interpolates the height of an object.
- `SIZE_WIDTH`: Interpolates the width of an object.
- `VELOCITY`: Interpolates the velocity of an object.
- `VOLUME`: Interpolates the volume of a Sound source.
- `FONTSIZE`: Interpolates the font size on GUI components.
- `OPACITY`: Interpolates the opacity of an object.

Note that not all types are supported by all objects. 
For example, the `VOLUME` type is supported by `VolumeControl`, but not by `GuiComponent`. 
To see which types are supported by a specific object, refer to the API documentation and the specific `Tweenable`'s implementation of `getTweenValues` and `setTweenValues`.

## TweenFunction

We have two ways of instatiating a `TweenFunction`: You can either call the `TweenFunction` enum to use one of our many pre-implemted Tween functions,
or create a custom `TweenFunction` by implementing a function that takes the progressed time as input and returns the modified Tween value as output.
The premade Tween functions are based on Robert Penner's easing equations, which are mathematical formulas that create smooth transitions.

Each enum constant represents a different easing function and is associated with a `TweenEquation` lambda expression that computes the easing value
based on the input time.

* The `LINEAR` function simply returns the input time, creating a linear transition.
* The `QUAD_IN` function represents a quadratic easing-in function, which accelerates from zero velocity. Similarly, `QUAD_OUT` and `QUAD_INOUT`
  provide quadratic easing-out and easing-in-out transitions, respectively. The `QUAD_OUT` function decelerates to zero velocity, while `QUAD_INOUT`
  combines both behaviors.
* The `CIRCLE_IN`, `CIRCLE_OUT`, and `CIRCLE_INOUT` functions use circular equations to create easing effects that mimic the motion of a circle.
* The `SINE_IN`, `SINE_OUT`, and `SINE_INOUT` functions use sine wave equations to create smooth sinusoidal transitions.
* The `EXPO_IN`, `EXPO_OUT`, and `EXPO_INOUT` functions use exponential equations to create transitions that start or end very quickly.
* The `BACK_IN`, `BACK_OUT`, and `BACK_INOUT` functions create transitions that overshoot their target value before settling.
* The `BOUNCE_OUT`, `BOUNCE_IN`, and `BOUNCE_INOUT` functions simulate a bouncing effect, where the value bounces back and forth before settling.
* Finally, the `ELASTIC_IN`, `ELASTIC_OUT`, and `ELASTIC_INOUT` functions create elastic transitions that oscillate before settling.

Each easing function is implemented as a lambda expression that takes a `float` time parameter (ranging from 0 to 1) and returns a `float` value
representing the eased progress. The `compute` method in the `TweenFunction` calls the associated lambda to calculate the eased value for a given
time.

