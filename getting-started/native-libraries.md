---
meta.description: Learn about managing native libraries in your LITIENGINE project.
meta.keywords: LITIENGINE, java, game, gameengine, development, 2D, programming, library, build, natives
---

# Native Libraries

## Managing Native Libraries

> *Managing (and deploying) the native libraries is only necessary for
> **Controller Support** and Accessing the **Steamworks** library.*

The LITIENGINE has some native dependencies that allow supporting
Controller Input and access to Steamworks. In case you want to use these
features, you can either use a build tool plugin (e.g.  the [Gradle
Natives Plugin](https://github.com/cjstehno/gradle-natives)) or get the
native libraries from the downloadable LITIENGINE package. Either way,
you need to add the location of the natives to the *.classpath* of your
project if you want to use the functionality when your Game is being run
from within your IDE. 

### Gradle
Add the following code to your project's `build.gradle` file to extract LITIENGINE's native libraries to the '*libs*' folder upon
calling `gradle includeNatives`

```groovy
plugins {
  id 'com.stehno.natives' version '0.3.1'
}

natives {
  configurations = ['runtimeClasspath']
  outputDir = 'libs'
}
```
