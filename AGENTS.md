# AGENTS.md - LITIENGINE Docs

This repository contains the official documentation for LITIENGINE, a free, open-source 2D Java Game Engine. The docs are published at https://docs.litiengine.com/

## Repository Overview

This is a **technical documentation repository** powered by [Zensical](https://zensical.org/). The actual engine source code lives at https://github.com/gurkenlabs/litiengine.

- **Language**: Markdown (with Java code examples)
- **Engine Baseline**: Java 25+
- **Docs Engine**: Zensical (configured in `zensical.toml`)
- **CI/CD**: GitHub Actions (`docs-check.yml` for pull requests, `docs.yml` for GitHub Pages deployment)

## Build, Lint, and Validation Commands

All contributors and AI agents must run the following validation suite before submitting changes:

```bash
# 1. Lint markdown syntax, tables, and list spacing (requires Python 3.10+)
python .github/scripts/lint_markdown.py

# 2. Validate all internal markdown links and image references
python .github/scripts/validate_links.py

# 3. Synchronize llms.txt and llms-full.txt
python .github/scripts/generate_llms.py

# 4. Strict documentation build (must exit with 0 errors/warnings)
zensical build --clean --strict
```

### Pre-Commit Hook

A git pre-commit hook is provided under `.githooks/pre-commit`. Enable it locally via:

```bash
git config core.hooksPath .githooks
```

## Project Structure

```text
/
├── zensical.toml         # Site configuration, theme, and navigation tree
├── requirements-docs.txt # Python dependencies (Zensical, etc.)
├── .github/
│   ├── scripts/          # Python linters and validation tooling
│   └── workflows/        # CI validation & GitHub Pages deployment
├── .githooks/            # Pre-commit hook running validations
├── docs/                 # Documentation source files
│   ├── getting-started/  # Installation & setup guides
│   ├── game-api/         # Core API documentation (RenderEngine, SoundEngine, etc.)
│   ├── player-input/     # Input handling (keyboard, mouse, gamepad)
│   ├── configuration/    # Game configuration docs
│   ├── entity-framework/ # Entity system documentation
│   ├── control-entities/ # Controllers, abilities, AI, scripting
│   ├── tile-maps/        # Tiled map integration
│   ├── resource-management/ # Assets, sprites, textures
│   ├── user-interface/   # GUI components
│   ├── utiliti-editor/   # utiLITI editor docs
│   ├── tutorials/        # Step-by-step game tutorials
│   ├── advanced/         # Advanced engine topics
│   └── images/           # General screenshots and visual assets
└── AGENTS.md             # Contributor & AI Agent guidelines
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
  implementation 'de.gurkenlabs:litiengine:0.12.0-SNAPSHOT'
}
```

```xml
<dependency>
  <groupId>de.gurkenlabs</groupId>
  <artifactId>litiengine</artifactId>
  <version>0.12.0-SNAPSHOT</version>
</dependency>
```
````

### Links

- Internal links: Use standard relative paths with `.md` extension. `validate_links.py` verifies all internal links:
  ```markdown
  [Getting Started](getting-started/README.md)
  [Install JDK](../getting-started/install-jdk.md)
  ```
- External links: Full URL
  ```markdown
  [Tiled Editor](https://www.mapeditor.org/)
  ```
- API references: Link to API Quick Reference
  ```markdown
  [API Reference](getting-started/api-quick-reference.md)
  ```

### Admonitions / Callouts

Zensical natively supports standard admonitions (`note`, `tip`, `warning`, `caution`):

```markdown
!!! note "Informative Note"
    The utiLITI editor is not an IDE for Java development.

!!! tip "Performance"
    Pre-allocate vectors outside update loops to eliminate GC latency.

!!! warning "Snapshot Warning"
    If you use LITIENGINE snapshot versions, test against current main!
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

When adding new pages, register them in the `nav` section of [`zensical.toml`](zensical.toml):

```toml
{ "New Page Title" = "category/new-page.md" }
```

## Stub Files

If completing stubs or expanding documentation:

1. Check the main LITIENGINE repository (`gurkenlabs/litiengine`) for API details
2. Reference existing similar documentation for style
3. Include practical, compiling Java code examples
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
- Documentation website: https://docs.litiengine.com/
- Discord community: https://discord.gg/rRB9cKD
- Forum: https://forum.litiengine.com/
