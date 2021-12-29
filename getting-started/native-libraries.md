---
meta.description: Learn about managing native libraries in your LITIENGINE project.
meta.keywords: LITIENGINE, java, game, gameengine, development, 2D, programming, library, build, natives
---

# Native Libraries

## Managing Native Libraries

> *Managing (and deploying) the native libraries is mainly necessary for
> **Controller Support** or when using other libraries that require native assemblies (like **steamworks4j**).*

The LITIENGINE has some native dependencies that allow supporting
Controller Input. This requires platform dependent binaries to be available 
at runtime to work properly.
Our java library .jar archive contains all of the necessary binaries, hence the simplest
way to access them is to tell gradle to extract them to the application directory.

### Gradle (Kotlin)
Add the following code to your project's `build.gradle.kts` file to extract LITIENGINE's native libraries to the '*libs*' folder
whenever the project is being built.

```kotlin
tasks.register<Copy>("natives") {
  for (dep in configurations.runtimeClasspath.get().files) {
    from(zipTree(dep).files)
    include("**/*.dll", "**/*.so", "**/*.jnilib", "**/*.dylib")
    into(File(buildDir, "libs"))
  }
}

tasks.named("build") {
  dependsOn("natives")
}
```
