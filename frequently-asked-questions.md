---
title: "Frequently Asked Questions"
description: "Answers to frequently asked questions about LITIENGINE, supported platforms, performance, and Java game development."
keywords: ["LITIENGINE", "FAQ", "questions", "java", "game", "performance", "platforms", "editor"]
---

# Frequently Asked Questions

## LITIENGINE Basics

### Is LITIENGINE a programming language or a library?

LITIENGINE is a 2D game library for Java. It requires **Java 21 or later**.

### What's the current development status of LITIENGINE?

LITIENGINE is actively maintained with modular sub-projects, a built-in scripting engine, and editor tooling. To learn more, read our **[Roadmap](/docs/roadmap/)**.

### Does LITIENGINE collect any user data?

LITIENGINE does not collect any user data via telemetry. However, if you register on our forum or subscribe to our newsletters, your information is stored securely on our servers and only used for the purposes you agreed to.

### What platforms can LITIENGINE deploy to?

With LITIENGINE, you can create and deploy standalone desktop games for **Windows**, **Linux**, and **macOS**.
Because the 2D rendering pipeline uses pure Java AWT/Swing graphics, mobile platforms (Android/iOS) and console ports (which lack AWT support) are not supported.

### Whom is LITIENGINE made for?

LITIENGINE is designed for anyone interested in creating 2D computer games in pure Java. Simple in nature, it is easy to pick up, yet powerful enough to create massive worlds, RPGs, top-down shooters, and platformers.

### Since LITIENGINE is written in pure Java - what performance drawbacks can I expect?

LITIENGINE uses optimized software rendering via Java AWT Graphics rather than direct native OpenGL bindings. While this keeps the engine 100% portable and free of complex native dependencies, CPU load is higher when rendering thousands of simultaneous dynamic particles or rapidly scaling large unbuffered images. Memory usage remains very low, and standard 2D games run at solid 60+ FPS on standard hardware.

### Can I create LITIENGINE games without using the utiLITI editor?

Yes! You can write entire LITIENGINE games purely in Java code without opening the editor. However, the **utiLITI Editor** provides an integrated visual workflow for configuring entities, importing tilesets, packing `.litidata` resource bundles, and scripting game logic.

---

## Distribution

### How do I create standalone executables for players?

See our comprehensive **[Deployment Guide](/docs/deployment/)** for instructions on bundling a JRE and building Windows `.exe`, macOS, and Linux packages using Gradle and Launch4j.
