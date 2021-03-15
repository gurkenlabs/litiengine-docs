---
meta.description: Learn about build automation utilities in general and how to set up the most common build tools for Java development.
meta.keywords: LITIENGINE, java, game, gameengine, development, 2D, programming, build, gradle, maven, ant
---

# Build Systems
## Choose a build system

Have you heard of build automation utilities? If you don't want to manage and compile your software and dependencies by hand with every release, you can rely on build automation utilities to compile and package your source code, manage dependencies, and run automated tests.
Three build systems are predominantly used for Java development:
* [Gradle](https://gradle.org/)
* [Apache Maven](https://maven.apache.org/)
* [Apache Ant](https://ant.apache.org/) 

> Of course, it is possible to just download the LITIENGINE .jar and import and use the library manually the "oldschool" way. However, we don't encourage using the manually downloaded library for your game project as managing the whole life cycle of your software is *much* more straightforward using a dedicated build system.

LITIENGINE itself is built upon **Gradle** and uses it to seamlessly manage its build steps and dependent libraries.

## Install and set up a build system

### Example: Eclipse + Gradle
Assuming that you chose [Eclipse IDE](https://www.eclipse.org/downloads/packages/release/kepler/sr1/eclipse-ide-java-developers) and [Gradle](https://gradle.org/), you can create a Gradle project with these steps:
* [download Gradle](https://gradle.org/install/).
* create a new directory `C:\Gradle` and unzip the downloaded file there. 
* add `C:\Gradle\[your-gradle-version]\bin` to your system's *PATH* environment variable.
* if there is no gradle plugin in your Eclipse installation, go to Help -> Eclipse Marketplace to search and install Gradle integration.
* click File > New > Other and select Gradle Project as wizard.
* two files are required in a Gradle project's root folder: `build.gradle`, containing the build tasks, and `settings.gradle`, containing Gradle settings.

### Example: IntelliJ + Gradle
