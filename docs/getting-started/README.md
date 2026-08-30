---
title: Getting Started
icon: lucide/compass
description: Everything you need to set up your environment, install Java 21+, configure
  Gradle/Maven, and run your first 2D LITIENGINE game.
keywords: [LITIENGINE, getting started, java, gradle, installation, setup, tutorial]
tags: [getting-started, overview, installation, setup, quickstart]
---
# Getting Started

Welcome to **LITIENGINE**! This section guides you through installing the Java 21+ development kit, configuring your IDE, setting up Gradle or Maven build automation, and launching your first 2D game.

---

## Explore Getting Started

<div class="grid cards" markdown>

- :material-download:{ .lg .middle } **[Get LITIENGINE](/getting-started/get-litiengine/)**

    ---

    Dependency coordinates for Gradle and Maven, Sonatype snapshot repositories, and standalone fat JARs.

- :material-coffee:{ .lg .middle } **[Install JDK 21+](/getting-started/install-jdk/)**

    ---

    Set up Java 21 LTS or newer across Windows, Linux, and macOS with modern Panama FFM support.

- :material-laptop:{ .lg .middle } **[Set Up Your IDE](/getting-started/development-environment/)**

    ---

    Configuring IntelliJ IDEA, Eclipse, or VS Code with hot-reloading and debug profiles.

- :material-hammer-wrench:{ .lg .middle } **[Build Systems](/getting-started/build-systems/)**

    ---

    Automated Gradle tasks, `shadowJar` packaging, and build automation workflows.

- :material-folder-cog:{ .lg .middle } **[Project Structure](/getting-started/project-structure/)**

    ---

    Recommended directory layouts for assets, `.litidata` resource archives, maps, and source files.

- :material-play-circle:{ .lg .middle } **[Run the Game](/getting-started/run-the-game/)**

    ---

    Your first 15-line program initializing `Game.init()`, loading maps, and starting the 60 FPS loop.

- :material-book-open-page-variant:{ .lg .middle } **[API Quick Reference](/getting-started/api-quick-reference/)**

    ---

    Instant cheat sheet covering all core modules: `Game.*`, `Resources.*`, `Input.*`, and `Camera`.

- :material-package-variant-closed:{ .lg .middle } **[Deployment Guide](/deployment/)**

    ---

    Bundling a JRE with `jlink` and creating standalone `.exe` executables with Launch4j.

</div>

---

## Frequently Asked Questions

??? question "Which Java version is required?"
    LITIENGINE requires **Java 21 LTS or newer** (tested through JDK 25).

??? question "Can I run LITIENGINE on Apple Silicon (M1–M4)?"
    Yes! LITIENGINE runs natively on macOS AArch64 using any standard ARM64 JDK (Temurin, Azul, or Oracle).
