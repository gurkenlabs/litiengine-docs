---
meta.description: Learn about all possible ways to download LITIENGINE and include it in your project.
meta.keywords: LITIENGINE, java, game, gameengine, development, 2D, programming, library, SDK, repository, build
---

# Get LITIENGINE
Now, let us discuss how to actually download the LITIENGINE. The engine consists of two major parts: the **editor** and the **java library**.

## 1. Download the LITIENGINE SDK

The LITIENGINE SDK contains *utiLITI*, our project management and map creation tool. It is a stand-alone editor which produces project files that can then be loaded to your game. You can [download the LITIENGINE SDK from litiengine.com](https://litiengine.com/download/).

> **Note:** The utiLITI editor is not an IDE for Java development.

## 2. Get the LITIENGINE Java library via Gradle

The library itself is used by your game's implementation and provides you with the actual Java API.
Add the LITIENGINE dependency to your Gradle project by adding the following code to your project's `build.gradle` file:

> While it's also possible to reference the library via **Maven** or **Ant**, our recommended and supported way is to use gradle. 
> 

### Gradle (Groovy)
```groovy
apply plugin: 'java'
apply plugin: 'application'

repositories {
  mavenCentral()
}

dependencies {
  implementation 'de.gurkenlabs:litiengine:0.5.1'
}
```
> **Note:** if you failed build, try to modify apply plugin: 'java' to apply plugin: 'java-library'

### Gradle (Kotlin)
```kotlin
plugins {
  java
  application
}

repositories {
  mavenCentral()
}

dependencies {
  implementation("de.gurkenlabs:litiengine:0.5.1")
}
```

### Sample Project
A basic example for a Gradle based LITIENGINE project can be found [HERE](https://github.com/gurkenlabs/litiengine-gurk-nukem). Have a look at the project's `build.gradle` and `settings.gradle`.

## (Advanced) Build the LITIENGINE from source

 If you want to use recent features of the [LITIENGINE master branch](https://github.com/gurkenlabs/litiengine/tree/master) that haven't been part of a stable release yet, you can configure Gradle to include a local clone of the engine repository. Assuming you have cloned the engine to a folder in the same location as your project, you would have the following project structure:
```
project/settings.gradle
litiengine/setting.gradle.kts
```
Then in `project/settings.gradle`, add the following line:
```
includeBuild "../litiengine"
```
In `project/build.gradle`, define the dependency as usual:

```groovy
dependencies {
  implementation 'de.gurkenlabs:litiengine'
}
```
 Gradle will automatically replace any dependency with the version provided by `includeBuild` if it finds a matching module.