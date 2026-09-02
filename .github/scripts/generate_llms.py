import sys
import re
from pathlib import Path

def generate_llms():
    root = Path(__file__).resolve().parent.parent.parent
    docs_dir = root / "docs"
    
    # 1. Summary llms.txt
    llms_txt = """# LITIENGINE Docs
> Free, open-source 2D Java Game Engine (Java 25+) with pure AWT graphics, low-latency Panama FFM input (Input4j), spatial quadtree physics, positional 2D audio, and the utiLITI companion level editor.

## Core Documentation

- [Getting Started](https://docs.litiengine.com/getting-started/): Installation, JDK 25+ setup, Gradle/Maven configuration, and first game.
- [API Quick Reference](https://docs.litiengine.com/getting-started/api-quick-reference/): Complete static cheat sheet covering Game.*, Resources.*, and Input.*.
- [2D Graphics](https://docs.litiengine.com/game-api/render-engine/): AWT rendering, sprite transformations, shape drawing, and TextRenderer outlines.
- [2D Physics](https://docs.litiengine.com/game-api/physics-engine/): Bounding-box collisions, spatial quadtree acceleration, and collision sliding.
- [2D Sound](https://docs.litiengine.com/game-api/sound-engine/): Positional 2D spatial audio, distance attenuation, and multi-bus volume controls.
- [Player Input](https://docs.litiengine.com/player-input/): Low-latency keyboard, mouse, and hardware gamepads via Input4j Panama FFM.
- [Entity Framework](https://docs.litiengine.com/entity-framework/): Creatures, Props, Emitters, LightSources, Spawnpoints, and Entity Annotations.
- [Java Scripting Engine](https://docs.litiengine.com/control-entities/scripting/): Pure Java runtime scripts (GameScript, EnvironmentScript, CreatureScript).
- [utiLITI Editor](https://docs.litiengine.com/utiliti-editor/): Visual 2D map editor, entity inspector, tilesets, Wang autotiling, and .litidata bundling.
- [Tutorials](https://docs.litiengine.com/tutorials/2d-platformer/): Step-by-step guides for 2D platformers, top-down shooters, and brick breakers.
- [Savegames & State Persistence](https://docs.litiengine.com/savegames/): Serializing player stats, inventory, and environment restoration.
- [Deployment](https://docs.litiengine.com/deployment/): Packaging standalone executables with jlink and Launch4j.

## Key APIs & Symbols

- `de.gurkenlabs.litiengine.Game`: Master engine entry point (`Game.init(args)`, `Game.start()`, `Game.world()`, `Game.physics()`, `Game.audio()`, `Game.window()`, `Game.graphics()`, `Game.screens()`).
- `de.gurkenlabs.litiengine.resources.Resources`: Central asset archive manager (`Resources.maps()`, `Resources.spritesheets()`, `Resources.sounds()`, `Resources.tracks()`, `Resources.fonts()`, `Resources.images()`).
- `de.gurkenlabs.litiengine.input.Input`: Unified input polling (`Input.keyboard()`, `Input.mouse()`, `Input.gamepads()`).
- `de.gurkenlabs.litiengine.entities.Creature`: Base class for living entities with movement and combat controllers.
- `de.gurkenlabs.litiengine.entities.Prop`: Base class for static or destructible interactive map objects.
- `de.gurkenlabs.litiengine.environment.Environment`: Level container holding tilemaps, lights, and entity instances.

## Full Context

- [Full Documentation Bundle](https://docs.litiengine.com/llms-full.txt): Complete concatenated markdown documentation for LLM consumption.
"""

    (docs_dir / "llms.txt").write_text(llms_txt.strip() + "\n", encoding="utf-8")
    
    # 2. Comprehensive llms-full.txt
    core_files = [
        "index.md",
        "getting-started/README.md",
        "getting-started/get-litiengine.md",
        "getting-started/install-jdk.md",
        "getting-started/development-environment.md",
        "getting-started/build-systems.md",
        "getting-started/run-the-game.md",
        "getting-started/api-quick-reference.md",
        "game-api/README.md",
        "game-api/render-engine.md",
        "game-api/sound-engine.md",
        "game-api/physics-engine.md",
        "game-api/loops.md",
        "game-api/game-world.md",
        "game-api/camera.md",
        "game-api/screens.md",
        "game-api/tweens.md",
        "player-input/README.md",
        "player-input/keyboard-input.md",
        "player-input/mouse-input.md",
        "player-input/gamepad-input.md",
        "entity-framework/README.md",
        "entity-framework/default-entity-types.md",
        "entity-framework/custom-entities.md",
        "entity-framework/triggers.md",
        "entity-framework/annotations.md",
        "entity-framework/entity-events.md",
        "entity-framework/props.md",
        "control-entities/README.md",
        "control-entities/entity-controllers.md",
        "control-entities/movement-controller.md",
        "control-entities/animation-controller.md",
        "control-entities/behavior-controller.md",
        "control-entities/ability-framework.md",
        "control-entities/scripting.md",
        "savegames.md",
        "deployment.md",
        "utiliti-editor/README.md",
        "utiliti-editor/create-projects.md",
        "utiliti-editor/maps-and-environments.md",
        "utiliti-editor/sprite-editor.md",
        "utiliti-editor/tileset-editor.md",
        "utiliti-editor/tools-and-editing.md",
        "utiliti-editor/entity-inspector.md",
        "utiliti-editor/scripts.md",
        "utiliti-editor/script-diagnostics.md",
        "utiliti-editor/settings-and-shortcuts.md",
        "frequently-asked-questions.md",
        "about/sponsors.md",
        "GLOSSARY.md"
    ]
    
    full_buffer = [
        "# LITIENGINE Complete Technical Documentation",
        "> Free, open-source 2D Java Game Engine (Java 25+)\n",
        "This file contains the complete technical documentation for LITIENGINE, optimized for retrieval-augmented generation and LLM consumption.\n",
        "---\n"
    ]
    
    for rel in core_files:
        f = docs_dir / rel
        if f.exists():
            text = f.read_text(encoding="utf-8")
            full_buffer.append(f"<!-- BEGIN CHAPTER: {rel} -->")
            full_buffer.append(text.strip())
            full_buffer.append(f"<!-- END CHAPTER: {rel} -->\n\n---\n")
            
    full_text = "\n\n".join(full_buffer)
    (docs_dir / "llms-full.txt").write_text(full_text.strip() + "\n", encoding="utf-8")
    print("Generated docs/llms.txt and docs/llms-full.txt successfully.")

if __name__ == "__main__":
    generate_llms()
