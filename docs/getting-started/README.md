---
title: Getting Started
icon: lucide/compass
description: Everything you need to set up your environment, install Java 25+, configure Gradle/Maven, and run your first 2D LITIENGINE game.
keywords: [LITIENGINE, getting started, java, gradle, installation, setup, tutorial]
tags: [getting-started, overview, installation, setup, quickstart]
---
# Getting Started

Welcome to **LITIENGINE**! This section guides you through installing the Java 25+ development kit, configuring your IDE, setting up Gradle or Maven build automation, and launching your first 2D game.

---

## Explore Getting Started

<div class="grid cards" markdown>

- :material-download:{ .lg .middle } **[Get LITIENGINE](get-litiengine.md)**

    ---

    Dependency coordinates for Gradle and Maven, Sonatype snapshot repositories, and standalone fat JARs.

- :material-coffee:{ .lg .middle } **[Install JDK 25+](install-jdk.md)**

    ---

    Set up Java 25 or newer across Windows, Linux, and macOS with modern Panama FFM support.

- :material-laptop:{ .lg .middle } **[Set Up Your IDE](development-environment.md)**

    ---

    Configuring IntelliJ IDEA, Eclipse, or VS Code with hot-reloading and debug profiles.

- :material-hammer-wrench:{ .lg .middle } **[Build Systems](build-systems.md)**

    ---

    Automated Gradle tasks, `shadowJar` packaging, and build automation workflows.

- :material-folder-cog:{ .lg .middle } **[Project Structure](project-structure.md)**

    ---

    Recommended directory layouts for assets, `.litidata` resource archives, maps, and source files.

- :material-play-circle:{ .lg .middle } **[Run the Game](run-the-game.md)**

    ---

    Your first program initializing `Game.init()`, creating your game window, and loading maps.

- :material-book-open-page-variant:{ .lg .middle } **[API Quick Reference](api-quick-reference.md)**

    ---

    Instant cheat sheet covering all core modules: `Game.*`, `Resources.*`, `Input.*`, and `Camera`.

- :material-package-variant-closed:{ .lg .middle } **[Deployment Guide](../deployment.md)**

    ---

    Bundling a JRE with `jlink` and creating standalone `.exe` executables with Launch4j.

</div>

---

## Frequently Asked Questions

??? question "Which Java version is required?"
    LITIENGINE requires **Java 25 or newer**.

??? question "Can I run LITIENGINE on Apple Silicon (M1–M4)?"
    Yes! LITIENGINE runs natively on macOS AArch64 using any standard ARM64 JDK 25+ (Temurin, Azul, or Oracle).
