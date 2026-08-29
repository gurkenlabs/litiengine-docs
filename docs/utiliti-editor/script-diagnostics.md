---
title: "Script Diagnostics & Guidance"
icon: "lucide/activity"
description: "Discover script events, architecture guides, and startup configuration directly in utiLITI."
keywords: ["utiLITI", "Script Explorer", "GameScriptsDialog", "script guidance", "templates", "architecture"]
---

# Script Diagnostics & Guidance

utiLITI provides dedicated discovery tools, visual configuration panels, and interactive guidance to help developers explore engine APIs, understand the 3 script tiers, and configure project startup behavior.

---

## 1. Script Events & API Explorer

The **Script Events & API Explorer** is a searchable cheat sheet and interactive catalog of all engine events, lifecycle hooks, and scripting primitives.

### Accessing the Explorer
- **Menu Bar**: `Script` -> `Script Events & API Explorer...`
- **Script Workspace**: Click `[ 🔍 ]` in the **GLOBALS & APIS** dock panel.
- **Entity Inspector**: Click `[ 🔍 ]` in the **Scripts** section toolbar.

### Explorer Features
1. **Categorized Event Catalog**: Browse events categorized into Entity Lifecycle, Environment Lifecycle, Game Lifecycle, Combat & Abilities, Movement & Physics, Cinematics, and Spatial Queries.
2. **Instant Search & Filter**: Search by method name, parameter type, or code keyword.
3. **One-Click Insertion**: Click **"Insert into Active Script"** to automatically insert method stubs or code snippets into the active Monaco editor tab at your current cursor position.
4. **Copy Snippet**: Copy ready-to-use template code to your clipboard.

---

## 2. Scripting Architecture & Getting Started Guide

Located within the **Architecture & Getting Started Guide** tab of the explorer (accessible via `Script -> Scripting Guide & Getting Started...` or the `[ 📖 ]` button in the Script Workspace header):

- Explains the roles of **GameScript**, **EnvironmentScript**, and **CreatureScript**.
- Details how scripts communicate using `globals`, `sendMessage`, and `EntityQuery`.
- Features one-click **"Create Game Script"**, **"Create Map Script"**, and **"Create Creature Script"** action buttons.

---

## 3. Configure Game Scripts & Startup Dialog

The **Game Scripts & Startup Configuration Dialog** provides project-level management for your game entry points:

### Accessing the Configuration Dialog
- **Menu Bar**: `Script` -> `Configure Game Scripts...`
- **Script Workspace**: Click `[ ⚙ ]` in the Script Explorer header actions.

### What you can configure
- **Primary Startup Script**: Choose which `GameScript` automatically initializes on boot.
- **Fallback Map**: Specify a default map to load if the game script does not invoke `loadMap()`.
- **Active Game Scripts Table**: Enable, disable, add, remove, and open game-level scripts directly in the editor.

---

## 4. Rich Code Starter Templates

When creating a new script using **Script -> New Script...** or the `[ + ]` button in the Script Workspace, utiLITI generates fully commented starter code with working examples:

- **GameScript**: Generates map loading boilerplate, `globals` initialization, audio playback, and ESC pause input handlers.
- **EnvironmentScript**: Generates level start announcement banners, objective tracking via `onEntityRemoved`, and victory transitions.
- **CreatureScript**: Generates AI movement loops, ability casting, floating combat text on `onHit`, and mortality cleanup on `onDeath`.
