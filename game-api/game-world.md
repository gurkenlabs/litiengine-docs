# Game World

## Introduction to Environments

Every game engine needs a container that holds all the visual and non-visual things that will, in the end, make up the game world. This container is called `Environment` in the LITIENGINE. Only one Environment is loaded at a time and the Game holds the currently active Environment. Every time you want to position something within the two-dimensional space of your game, you can do so by adding it to the Environment.

It’s important to point out, that the Environment is related to exactly one Map and that the LITIENGINE provides an interface to load MapObjects to the environment. The implementations that take care of this task are called MapObjectLoaders. They basically translate the information form the *.tmx map* format to objects that can be managed by the engine.

**Example usages:**

```java
// set the active environment on the game
Game.world().loadEnvironment(new Environment("level-1.tmx"));

// add an entity to the environment
Game.world().environment().add(new MyEntity("my-entity"));

// retrieve the entity from the enviroment by its name
IEntity entity = Game.world().environment().get("my-entity");
MyEntity myEntity = Game.world().environment().get(MyEntity.class, "my-entity");

// remove the entity by its name
Game.world().environment().remove("my-entity");

// add a entity listener to the current environment of the game
Game.world().environment().addEntityListener(new EnvironmentEntityListener(){
  @Override
  public void entityAdded(IEntity entity) {
    // do sth when entities are added
  }
});
```
 ### Layering
 When the active Screen calls the `Environment.render(Graphics2D)` method, its internal rendering pipeline is executed which will render everything that was previously added/loaded to the environment. There are different `RenderType`s that define in which order the objects and tile layers will be rendered. Think of the `RenderType`s as layers that are painted on our canvas one after another. 

 The rendering order is as follows:

 `BACKGROUND` -> `GROUND` -> `SURFACE` -> `NORMAL` -> (static shadows) -> `OVERLAY` -> (ambient light) -> `UI`

 Internally, the Environment.render method does the following for every `RenderType` (besides `RenderType.NONE`, which can, for example, be used to make objects invisible temporarily):

  1.  Render all Map Layers of that type
  2.  Render all registered `IRenderable` implementations of that type
  3.  Render all added `IEntities` of that type
  4.  Call-back on the `EnvironmentRenderListener.rendered` listeners for that type
  5.  If `dbg_logDetailedRenderTimes = true`: track the time it took to execute the rendering

