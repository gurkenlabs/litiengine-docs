---
title: "Script Diagnostics & Guidance"
icon: "lucide/activity"
description: "Discover script events, architecture guides, live diagnostics, and batch entity automation scripts directly inside utiLITI."
keywords: ["utiLITI", "Script Explorer", "Monaco", "script guidance", "diagnostics", "batch automation", "Java scripting"]
tags: ["diagnostics", "compiler", "errors", "warnings", "linter", "scripts", "monaco"]
---

# Script Diagnostics & Guidance

utiLITI provides dedicated discovery tools, live console diagnostics, and an integrated **Monaco Code Editor** with real-time compilation and hot-reloading for Java scripts.

---

## 1. Script Events & API Explorer

The **Script Events & API Explorer** is an interactive, searchable catalog of all engine events, lifecycle hooks, and scripting primitives:

### Accessing the Explorer
* **Menu Bar**: `Script` -> `Script Events & API Explorer...`
* **Script Workspace**: Click `Explorer` in the **GLOBALS & APIS** dock panel.
* **Entity Inspector**: Click the script icon in the **Scripts** section toolbar.

### Explorer Capabilities
1. **Categorized Event Catalog**: Browse events categorized into Entity Lifecycle, Environment Lifecycle, Game Lifecycle, Combat & Abilities, Movement & Physics, and Spatial Queries.
2. **Instant Search & Filter**: Search by method name, parameter type, or keyword.
3. **One-Click Insertion**: Click **"Insert into Active Script"** to insert boilerplate method stubs directly into the active Monaco tab.

---

## 2. Practical Script Examples for utiLITI

You can write and execute pure Java scripts directly inside utiLITI to automate map design, inspect entities, and test game mechanics in real time:

### Example A: Batch Collider Application to Props
Automatically applies standardized 2.5D feet collision bounding boxes to all decorative props matching a naming prefix:

```java title="BatchApplyColliders.java"
import de.gurkenlabs.litiengine.Align;
import de.gurkenlabs.litiengine.Valign;
import de.gurkenlabs.litiengine.Game;
import de.gurkenlabs.litiengine.entities.Prop;

// Find all props with names starting with "tree_" or "rock_"
Game.world().environment().getProps().forEach(prop -> {
  if (prop.getName() != null && (prop.getName().startsWith("tree_") || prop.getName().startsWith("rock_"))) {
    // Enable solid collision anchored to the base
    prop.setCollision(true);
    prop.setCollisionBoxWidth(prop.getWidth() * 0.5);
    prop.setCollisionBoxHeight(prop.getHeight() * 0.3);
    prop.setCollisionBoxAlign(Align.CENTER);
    prop.setCollisionBoxValign(Valign.DOWN);
    System.out.println("Updated collider for: " + prop.getName());
  }
});
```

---

### Example B: Live Quadtree Spatial & Memory Diagnostics
Inspect active entity counts, memory usage, and quadtree spatial partitions:

```java title="SpatialDiagnostics.java"
import de.gurkenlabs.litiengine.Game;
import de.gurkenlabs.litiengine.entities.IEntity;
import java.util.Collection;

public class DiagnosticsRunner {
  public static void runDiagnostics() {
    Collection<IEntity> allEntities = Game.world().environment().all();
    long totalMem = Runtime.getRuntime().totalMemory() / (1024 * 1024);
    long freeMem = Runtime.getRuntime().freeMemory() / (1024 * 1024);
    long usedMem = totalMem - freeMem;

    System.out.println("=== LITIENGINE LIVE DIAGNOSTICS ===");
    System.out.println("Active Entities: " + allEntities.size());
    System.out.println("Creatures: " + Game.world().environment().getCreatures().size());
    System.out.println("Props: " + Game.world().environment().getProps().size());
    System.out.println("Triggers: " + Game.world().environment().getTriggers().size());
    System.out.println("Memory Used: " + usedMem + " MB / " + totalMem + " MB");
    System.out.println("===================================");
  }
}
```

---

## 3. Configure Game Scripts & Startup Dialog

The **Game Scripts & Startup Configuration Dialog** (`Script -> Configure Game Scripts...`) allows you to define default boot sequences:

* **Primary Startup Script**: Choose which `GameScript` automatically initializes on project launch.
* **Fallback Map**: Specify a default `.tmx` environment if the game script does not invoke `loadMap()`.
* **Active Game Scripts Table**: Enable, disable, and rearrange game-level scripts.

---

## See Also

<div class="grid cards" markdown>

- :material-code-braces:{ .lg .middle } **[UI & Workspaces](ui-and-workspaces.md)**

    ---

    Overview of dock panels, Monaco code editor, and asset inspectors.

- :material-play-outline:{ .lg .middle } **[Project Runner](project-runner.md)**

    ---

    Launching, debugging, and testing projects directly from utiLITI.

</div>
