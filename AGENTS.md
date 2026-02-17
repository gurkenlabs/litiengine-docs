# AGENTS.md - LITIENGINE Documentation

This repository contains the documentation for LITIENGINE, a free, open-source 2D Java Game Engine. The docs are published at https://litiengine.com/docs/

## Repository Overview

This is a **documentation-only repository**. The actual engine code lives at https://github.com/gurkenlabs/litiengine

- **Language**: Markdown (with Java/Groovy code examples)
- **Purpose**: Technical documentation for a 2D game engine library
- **No build tools, package managers, or CI/CD configured**

## Build/Lint/Test Commands

**Not applicable** - this repository contains only markdown files and images. There are no build, test, or lint commands.

For quality assurance:
- Preview markdown locally with your editor
- Check links manually before committing
- Verify images display correctly

## Project Structure

```
/
├── README.md              # Introduction page
├── SUMMARY.md             # Navigation/table of contents (DO NOT REMOVE)
├── CHANGELOG.md           # Release notes
├── GLOSSARY.md            # Term definitions
├── getting-started/       # Installation & setup guides
├── game-api/              # Core API documentation (Game.graphics(), etc.)
├── player-input/          # Input handling (keyboard, mouse, gamepad)
├── configuration/         # Game configuration docs
├── entity-framework/      # Entity system documentation
├── control-entities/      # Controllers, abilities, AI
├── tile-maps/             # Tiled map integration
├── resource-management/   # Assets, sprites, textures
├── user-interface/        # GUI components
├── utiliti-editor/        # utiLITI editor docs
├── tutorials/             # Step-by-step tutorials
├── advanced/              # Advanced topics
└── images/                # General images/assets
```

## Markdown Style Guidelines

### YAML Front Matter

Use front matter for SEO metadata on important pages:

```yaml
---
meta.description: "Brief description for SEO (150-160 characters)"
meta.keywords: "LITIENGINE, java, game, keyword1, keyword2"
meta.title: "Page Title for SEO"
---
```

### Headings

- Use `#` for page title (H1) - one per file
- Use `##` for major sections (H2)
- Use `###` for subsections (H3)
- Use `####` for sub-subsections (H4) - use sparingly

### Code Blocks

Always specify language for syntax highlighting:

````markdown
```java
Game.init(args);
Game.start();
```

```groovy
dependencies {
  implementation 'de.gurkenlabs:litiengine:0.11.1'
}
```

```xml
<dependency>
  <groupId>de.gurkenlabs</groupId>
  <artifactId>litiengine</artifactId>
  <version>0.11.1</version>
</dependency>
```
````

### Links

- Internal links: Use `/docs/` prefix with trailing slash
  ```markdown
  [Getting Started](/docs/getting-started/README/)
  [Install JDK](/docs/getting-started/install-jdk/)
  ```
- External links: Full URL
  ```markdown
  [Tiled Editor](https://www.mapeditor.org/)
  ```
- API references: Link to Javadocs
  ```markdown
  [Javadocs](https://litiengine.com/api/)
  ```

### Callouts/Notes

Use blockquotes for notes and warnings:

```markdown
> **Note:** The utiLITI editor is not an IDE for Java development.

> **Warning:** If you use LITIENGINE snapshot versions, expect untested code!
```

### Images

- Store images in `images/` or `img/` subdirectory within the topic folder
- Use relative paths: `![Alt text](images/screenshot.png)`
- Include image captions in italics below: `*Description of the image*`
- Supported formats: PNG, GIF, JPG, JPEG, WEBP

## Code Example Guidelines

### Java Code Standards

- Use LITIENGINE API conventions (e.g., `Game.init()`, `Game.start()`)
- Include necessary imports when showing complete examples
- Follow Java naming conventions (camelCase for methods/variables)
- Add brief comments explaining key operations

```java
public class Program {
  public static void main(String[] args) {
    Game.info().setName("My Game");
    Game.info().setVersion("v1.0.0");
    
    Game.init(args);
    Resources.load("game.litidata");
    Game.world().loadEnvironment("level1");
    Game.start();
  }
}
```

### Annotation Examples

Show LITIENGINE annotations with their common attributes:

```java
@EntityInfo(width = 18, height = 18)
@MovementInfo(velocity = 70)
@CollisionInfo(collisionBoxWidth = 8, collisionBoxHeight = 16, collision = true)
public class Player extends Creature {
  // ...
}
```

## Navigation Updates

When adding new pages, update `SUMMARY.md`:

```markdown
* [New Page Title](/docs/category/new-page/)
```

The navigation structure uses `<span>Category Name</span>` for section headers.

## Stub Files

Many files in this repository are stubs (contain only a title header). When completing stubs:

1. Check the main LITIENGINE repository for API details
2. Reference existing similar documentation for style
3. Include practical code examples
4. Add images/screenshots where helpful

## Writing Style

- Be concise but thorough
- Use second person ("you") to address the reader
- Explain concepts before showing code
- Link to related documentation pages
- Use bold for UI elements: `**File -> Save**`
- Use backticks for: code, method names, file names, keyboard shortcuts

## Common Terms

- **LITIENGINE** - Always uppercase
- **utiLITI** - The editor tool (camelCase, lowercase 'u')
- **Entity** - Game objects in the engine
- **Environment** - A game level/scene
- **Spritesheet** - Image containing animation frames

## External References

- Main repository: https://github.com/gurkenlabs/litiengine
- Javadocs: https://litiengine.com/api/
- Website: https://litiengine.com/
- Forum: https://forum.litiengine.com/
