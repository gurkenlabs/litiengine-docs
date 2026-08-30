---
title: Run, Debug & Hot Reload in utiLITI
icon: lucide/play
description: Comprehensive guide to running, debugging, and hot-reloading LITIENGINE
  projects directly from utiLITI using JDI breakpoints and standalone runners.
keywords: [utiLITI, Run Project, Debug Project, JDI debugger, breakpoints, hot reload,
  GameLauncher, Gradle integration, IDE]
tags: [project-runner, testing, run, debugging, playtest]
---
# Run, Debug & Hot Reload

utiLITI provides a built-in project execution and debugging environment, allowing you to test, pause, step through, and hot-reload gameplay code without switching to an external terminal.

---

## 1. Running the Project (`Shift + F10`)

Click the green **Run Project** button (:material-play:{ .middle style="color: #4caf50;" }) on the toolbar or press <kbd>Shift</kbd> + <kbd>F10</kbd>:

1. **Automatic Build**: utiLITI invokes the project's build service to compile recent Java sources.
2. **Standalone Launch**: utiLITI starts the game process using `GameLauncher` (`de.gurkenlabs.litiengine.launch.GameLauncher`) or the project's configured Gradle `run` task.
3. **Status Indicator**: The toolbar indicator displays real-time phase transitions:
 `Compiling` -> `Launching` -> `Running` (Green).

---

## 2. Debugging with Breakpoints (`Shift + F9`)

Click the **Debug Project** button (:material-bug:{ .middle style="color: #29b6f6;" }) on the toolbar or press <kbd>Shift</kbd> + <kbd>F9</kbd>:

- utiLITI launches the game with an active **Java Debug Interface (JDI)** socket attached.
- The **Scripts Workspace** connects to the live execution backend.

```text
┌─────────────────────────────────────────────────────────────┐
│ 10 | @Override │
│ 11 | public void onLoaded() { │
│ 12 host().setHitPoints(100); ◄ [BREAKPOINT HIT] │
│ 13 | Game.audio().playSound("start.wav"); │
│ 14 | } │
├─────────────────────────────────────────────────────────────┤
│ [DEBUGGER PANEL] │
│ [Resume (F9)] [⤵ Step Over (F8)] [↳ Step Into (F7)] │
│ ├ Thread: Game Loop Thread (Suspended) │
│ └ Variables: │
│ ├ host = Creature (ID: 104, name: "goblin_guard") │
│ ├ hitPoints = 100 │
│ └ position = Point2D.Double[x=128.0, y=64.0] │
└─────────────────────────────────────────────────────────────┘
```

### Setting Breakpoints:
- Click the left gutter of any line in the Monaco code editor. A red circle indicator (:material-circle:{ .middle style="color: #ef5350;" }) marks an active breakpoint.
- Breakpoints are automatically saved across sessions in user preferences.

### Debugger Controls:
- **Resume (`F9`)**: Continues execution until the next breakpoint is encountered.
- **Step Over (`F8`)**: Executes the current line and pauses on the next line.
- **Step Into (`F7`)**: Steps inside the invoked method.
- **Variables Inspector**: Inspect live local variables, entity fields, and engine states during suspended frames.

---

## 3. Process Management
- **Stop Project (`Ctrl + F2`)**: Terminates the active game process.
- **Restart Project**: Stops and immediately re-launches the game with fresh state.

---

## 4. Hot Code Reloading

utiLITI supports runtime hot-reloading for gameplay scripts and compiled entities:

1. Edit your script source code in utiLITI's Monaco editor or an external IDE.
2. Choose **Save & Reload** (`Ctrl + R`).
3. utiLITI compiles a new generation of the script:
 - If compilation succeeds, active script instances on the running map are detached and replaced with fresh instances while preserving configured parameters.
 - If compilation fails, the active version continues running uninterrupted, and compiler errors are reported in the **Problems** dock.

---

## 5. Build Services & IDE Integration

utiLITI integrates seamlessly with external development environments:

- **Gradle Build Service**: Reads project classpath, dependencies, and compiled entity definitions from `build/classes/`.
- **IntelliJ & VS Code**: Choose **Open in IDE** to edit files in your preferred environment. Rebuilding in IntelliJ automatically updates available entity types in utiLITI's inspector.
- **Configurable Arguments**: Customize JVM flags and launcher arguments in **File -> Settings -> General -> Gradle Launch Arguments**.
