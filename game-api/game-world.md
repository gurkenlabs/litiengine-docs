# Game World

## Introduction to Environments

Every game engine needs a container that holds all the visual and non-visual things that will, in the end, make up the game world. This container is called `Environment` in the LITIENGINE. Only one Environment is loaded at a time and the Game holds the currently active Environment. Every time you want to position something within the two-dimensional space of your game, you can do so by adding it to the Environment. When the active Screen calls the `Environment.render(Graphics2D)` method, it’s internal rendering pipeline is executed which will render everything that was previously added/loaded to the environment. There are different render types (`BACKGROUND`, `OVERLAY`, …) that define in which order the objects will be rendered, but more on that topic in a later tutorial.

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