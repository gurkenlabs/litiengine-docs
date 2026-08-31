---
title: Get LITIENGINE
icon: lucide/download
description: Learn about all possible ways to download LITIENGINE and include it in
  your project.
keywords: [LITIENGINE, java, game, gameengine, development, 2D, programming, library,
  SDK, repository, build]
tags: [installation, dependency, gradle, maven, download, snapshot]
---
# Get LITIENGINE
Now, let us discuss how to actually download the LITIENGINE. The engine consists of two major parts: the **editor** and the **java library**.

## 1. Download the LITIENGINE SDK

The LITIENGINE SDK contains *utiLITI*, our project management and map creation tool. It is a stand-alone editor which produces project files that can then be loaded to your game. You can [download the LITIENGINE SDK from litiengine.com](https://litiengine.com/download/).

!!! note
    The utiLITI editor is not an IDE for Java development.

## 2. Get the LITIENGINE Java library via Gradle

The library itself is used by your game's implementation and provides you with the actual Java API.
Add the LITIENGINE dependency to your Gradle project by adding the following code to your project's `build.gradle` file:

> While it's also possible to reference the library via **Maven** or **Ant**, our recommended and supported way is to use gradle. 
> 

### Stable Release (Maven Central)

=== "Gradle (Kotlin DSL)"

    ```kotlin
    repositories {
      mavenCentral()
    }

    dependencies {
      implementation("de.gurkenlabs:litiengine:0.12.0")
    }
    ```

=== "Gradle (Groovy DSL)"

    ```groovy
    repositories {
      mavenCentral()
    }

    dependencies {
      implementation 'de.gurkenlabs:litiengine:0.12.0'
    }
    ```

=== "Maven"

    ```xml
    <dependency>
      <groupId>de.gurkenlabs</groupId>
      <artifactId>litiengine</artifactId>
      <version>0.12.0</version>
    </dependency>
    ```

### Sample Project

A basic example for a Gradle-based LITIENGINE project can be found on GitHub: **[LITIENGINE Gurk Nukem](https://github.com/gurkenlabs/litiengine-gurk-nukem)**.

---

## Snapshot Versions

Feeling adventurous? Try one of LITIENGINE's nightly snapshot builds!

> **Warning:** If you use LITIENGINE snapshot versions, expect untested code and APIs that might still change!

Consuming snapshot artifacts is as simple as adding the Sonatype snapshots repository to your build configuration:

=== "Gradle (Kotlin DSL)"

    ```kotlin
    repositories {
      mavenCentral()
      maven {
        url = uri("https://oss.sonatype.org/content/repositories/snapshots/")
      }
    }

    dependencies {
      implementation("de.gurkenlabs:litiengine:0.13.0-SNAPSHOT")
    }
    ```

=== "Gradle (Groovy DSL)"

    ```groovy
    repositories {
      mavenCentral()
      maven {
        url "https://oss.sonatype.org/content/repositories/snapshots/"
      }
    }

    dependencies {
      implementation 'de.gurkenlabs:litiengine:0.13.0-SNAPSHOT'
    }
    ```

=== "Maven"

    ```xml
    <repositories>
      <repository>
        <id>sonatype-snapshots</id>
        <url>https://oss.sonatype.org/content/repositories/snapshots/</url>
        <snapshots><enabled>true</enabled></snapshots>
      </repository>
    </repositories>

    <dependencies>
      <dependency>
        <groupId>de.gurkenlabs</groupId>
        <artifactId>litiengine</artifactId>
        <version>0.13.0-SNAPSHOT</version>
      </dependency>
    </dependencies>
    ```


## (Advanced) Composite build with a local copy of the LITIENGINE repository

 You can configure Gradle to include a local clone of the LITIENGINE repository in your build. This way, you can test how changes in LITIENGINE translate to your game without having to deploy the engine as an artifact first. Assuming you have cloned the engine to a folder parallel to your project, you would have the following project structure:
```text
.
└── root/
 ├── my_project/
 │ ├── build.gradle
 │ ├── settings.gradle
 │ ├── src/
 │ │ └── ...
 │ └── ...
 └── litiengine-sdk/
 ├── .git/
 │ └── ...
 ├── build.gradle
 ├── settings.gradle
 ├── litiengine/
 │ └── ...
 ├── shared/
 │ └── ...
 ├── utiliti/
 │ └── ...
 └── ...
```
Then in `my_project/settings.gradle`, add the following block:
```java
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
