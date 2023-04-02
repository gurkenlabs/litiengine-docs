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
plugins {
    id("java")
    id("application")
}

repositories {
  mavenCentral()
}

dependencies {
  implementation 'de.gurkenlabs:litiengine:0.5.2'
}
```

### Sample Project
A basic example for a Gradle based LITIENGINE project can be found [HERE](https://github.com/gurkenlabs/litiengine-gurk-nukem). Have a look at the project's `build.gradle` and `settings.gradle`.

## Consuming LITIENGINE snapshot versions
Feeling bold and adventurous?
Try one of LITIENGINE's nightly snapshot builds!
> If you use LITIENGINE snapshot versions, expect untested code and API that might still change!

Consuming the snapshot artifacts is as simple as adding the sonatype snapshots repository to your dependency management, and choosing your preferred snapshot version. Browse all available snapshots [here](https://oss.sonatype.org/content/repositories/snapshots/de/gurkenlabs/litiengine/)!

in your `build.gradle`:
```groovy
plugins {
    id("java")
    id("application")
}

repositories {
  mavenCentral()
  maven{
    url "https://oss.sonatype.org/content/repositories/snapshots/"
  }

}

dependencies {
  implementation 'de.gurkenlabs:litiengine:0.5.2-dev3r+8cdbfc82-SNAPSHOT'
}
```


## (Advanced) Composite build with a local copy of the LITIENGINE repository

 You can configure Gradle to include a local clone of the LITIENGINE repository in your build. This way, you can test how changes in LITIENGINE translate to your game without having to deploy the engine as an artifact first. Assuming you have cloned the engine to a folder parallel to your project, you would have the following project structure:
```
.
└── root/
    ├── my_project/
    │   ├── build.gradle
    │   ├── settings.gradle
    │   ├── src/
    │   │   └── ...
    │   └── ...
    └── litiengine-sdk/
        ├── .git/
        │   └── ...
        ├── build.gradle
        ├── settings.gradle
        ├── litiengine/
        │   └── ...
        ├── shared/
        │   └── ...
        ├── utiliti/
        │   └── ...
        └── ...
```
Then in `my_project/settings.gradle`, add the following block:
```
includeBuild ("../litiengine"){
    dependencySubstitution {
        substitute module('de.gurkenlabs:litiengine') using project(':litiengine')
    }
}
```
In `my_project/build.gradle`, define the dependency without a version:

```groovy
dependencies {
  implementation 'de.gurkenlabs:litiengine'
}
```
 Gradle will automatically replace any dependency with the version provided by `includeBuild` if it finds a matching module.