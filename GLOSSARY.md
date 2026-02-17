---
description: Glossary of terms used in LITIENGINE documentation.
---

# Glossary

This glossary defines key terms used throughout LITIENGINE documentation.

## Core Concepts

### Entity
A game object that exists in the game world. Entities have a name, location, size, and can be rendered. Base class for most game objects in LITIENGINE.

### Environment
A game level or scene containing entities, maps, and game state. Only one environment can be active at a time. Accessed via `Game.world().environment()`.

### MapObject
An abstract object placed on a Tiled map. Contains properties that define how the object is processed when the map is loaded. MapObjects are converted to Entities by MapObjectLoaders.

### Spritesheet
A single image file containing multiple frames of animation or multiple sprites arranged in a grid. Used for entity animations and tiles.

## Entity Types

### Creature
An entity with collision, combat, movement, and animation capabilities. The most feature-rich entity type, typically used for players, enemies, and NPCs.

### Prop
A static or interactive object in the game world. Props can have health and transition through states (intact, damaged, destroyed).

### CollisionEntity
An entity that participates in collision detection. Has a defined collision box that can interact with other collidable entities and the environment.

### CombatEntity
An entity with health points and combat mechanics. Can take damage, die, and be resurrected.

### Trigger
An area-based entity that fires events when other entities enter or exit its bounds. Used for scripting game events.

### Emitter
An entity that spawns and manages particles for visual effects like fire, smoke, or magic.

### LightSource
An entity that illuminates the surrounding area with dynamic lighting.

### Spawnpoint
A marker that defines where entities should appear when spawned.

## Controllers

### EntityController
A component attached to an entity that controls a specific aspect of its behavior. Controllers are updated every tick.

### AnimationController
Manages which spritesheet animation is displayed for an entity. Determines animation based on entity state.

### MovementController
Handles entity movement, velocity, acceleration, and collision response during movement.

### BehaviorController
Controls AI behavior, typically using a state machine to switch between different behaviors.

## Game Architecture

### Game Loop
The core update cycle that runs at a fixed tick rate (default 60 ticks/second). Handles game logic and rendering.

### Screen
A container for GUI components and game rendering. Screens manage different game states (menu, gameplay, pause, etc.).

### Camera
Determines which portion of the game world is visible. Controls viewport position and zoom level.

### Resources
Static access point for loading and caching game assets (images, sounds, fonts, spritesheets).

## Physics

### Collision Box
A rectangular area used for collision detection. Can be smaller than the entity's visual bounds.

### Collision Type
Defines what an entity collides with: STATIC, DYNAMIC, ANY, or NONE.

### Force
A physics effect that applies movement to an entity over time. Can be one-time impulse or continuous (like gravity).

## Input

### Input4j
The input handling library used by LITIENGINE for gamepad support. Replaces JInput as of version 0.11.1.

### KeyboardEntityController
A movement controller that translates keyboard input into entity movement.

## utiLITI Editor

### utiLITI
The dedicated project management and map editor tool that comes with LITIENGINE.

### .litidata
The resource bundle file format used by LITIENGINE. Contains spritesheets, sounds, maps, and other assets.

### Resource Bundle
A collection of game assets packaged into a single .litidata file for easy loading.

## Animation

### Keyframe
A single frame in an animation sequence. Animations advance through keyframes at a specified duration.

### Frame Duration
How long each keyframe is displayed, measured in milliseconds.

### Sprite Prefix
A naming convention prefix used to identify spritesheets for an entity (e.g., "player" matches "player-idle-left.png").

## Combat

### Hitpoints (HP)
A combat entity's health value. When HP reaches zero, the entity dies.

### Team
An identifier used to distinguish friend from foe in combat. Entities on the same team typically don't damage each other.

### Ability
A special action that can be executed by a creature. Has cooldown, duration, and optional effects.

### Cooldown
The time in milliseconds before an ability can be used again.

## Rendering

### RenderType
The layer an entity renders on: BACKGROUND, GROUND, NORMAL, OVERLAY, or UI.

### RenderEngine
The system responsible for drawing entities, shapes, text, and images to the screen.

### Resolution Scaling
A rendering mode where all players see the same portion of the game world regardless of window size.

## Configuration

### config.properties
A file containing game configuration settings (resolution, audio, input, etc.).

### Annotation
Java annotations used to define static entity properties (@EntityInfo, @CollisionInfo, @MovementInfo, etc.).

## Tiled Map Editor

### TMX
The Tile Map XML format used by Tiled editor. LITIENGINE loads .tmx files as game levels.

### TSX
Tile Set XML format. Defines a tileset's properties and image reference.

### Tileset
A collection of tiles used to build map layers. Contains the source image and tile definitions.

### Layer
A horizontal slice of a map. Can contain tiles, objects, or images. Layers are rendered in order.

### Object Layer
A map layer containing MapObjects (entities, triggers, collision boxes, etc.).
