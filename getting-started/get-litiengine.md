# Get LITIENGINE

## Get the Java library

So you want to build a 2D Java game with the _LITIengine_, that's great! Now, the first thing you want to do is to actually download the library. There are multiple ways to achieve this. The library is distributed over the [Maven Central Repository](https://search.maven.org/artifact/de.gurkenlabs/litiengine/) and you can grab the necessary .jar-file\(s\) from there by using your favorite build automation tool or manually download the library.

### Gradle \(Groovy\)

```groovy
compile 'de.gurkenlabs:litiengine:0.5.0'
```

A basic example for a Gradle based LITIENGINE project can be found [HERE](https://github.com/gurkenlabs/litiengine-gurk-nukem). Have a look at the project's `build.gradle` and `settings.gradle`.

### Apache Maven

```xml
<dependency>
  <groupId>de.gurkenlabs</groupId>
  <artifactId>litiengine</artifactId>
  <version>0.5.0</version>
</dependency>
```

### Download the LITIENGINE SDK

The LITIENGINE comes with an editor that supports you with creating game environments and managing your resources. It is a stand alone product which produces a `.litidata` game project files that can then be loaded to your game.

> **Note:** The editor is not an IDE for Java development.

[Download LITIENGINE SDK](https://litiengine.com/download/)

## Managing Native Libraries

> *Managing (and deploying) the native libraries is only necessary for
> **Controller Support** and Accessing the **Steamworks** library.*

The LITIengine has some native dependencies that allow supporting
Controller Input and access to Steamworks. In case you want to use these
features, you can either use a build tool plugin (e.g.  the [Gradle
Natives Plugin](https://github.com/cjstehno/gradle-natives)) or get the
native libraries from the downloadable LITIengine package. Either way,
you need to add the location of the natives to the *.classpath* of your
project if you want to use the functionality when your Game is being run
from within your IDE. The following `build.gradle` file extracts all
native libraries of the LITIengine to the '*libs*' folder upon
calling `gradle includeNatives`

```groovy
plugins {
  id 'com.stehno.natives' version '0.3.1'
}

natives {
  configurations = ['runtime']
  outputDir = 'libs'
}

apply plugin: 'java'
apply plugin: 'maven'

repositories {
  mavenCentral()
}

dependencies {
  compile 'de.gurkenlabs:litiengine:0.5.0'
}
```
