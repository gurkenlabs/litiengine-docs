---
meta.description: Learn about all possible ways to download LITIENGINE and include it in your project.
meta.keywords: LITIENGINE, java, game, gameengine, development, 2D, programming, library, SDK, repository, build
---

# Get LITIENGINE
Now, let us discuss how to actually download the LITIENGINE library. There are multiple ways to achieve this:

## Download the LITIENGINE Java library manually

### From the Maven central repository
The Maven Central Repository is the default repository for Apache Maven, SBT and other build systems and can be easily used from Apache Ant/Ivy, Gradle and many other tools. You can [download the LITIENGINE library directly from the Maven Central Repository](https://search.maven.org/artifact/de.gurkenlabs/litiengine/) if you do not want to use a dedicated build system or need only specific files.

### From the LITIENGINE SDK

The LITIENGINE SDK consists of the *LITIENGINE Java library* and *utiLITI*, our project management and map creation tool. It is a stand-alone editor which produces project files that can then be loaded to your game. You can [download the LITIENGINE SDK from litiengine.com](https://litiengine.com/download/).

> **Note:** The utiLITI editor is not an IDE for Java development.

### Add the downloaded library to your project
#### Eclipse
* Open the context menu on your project
* Select `Properties > Java Build Path > Libraries`. From here, you can add JAR files to the build path, whether they are inside your workspace or not. You can also add a class folder, a directory containing Java class files that are not in a JAR.

> **Example**: The LITIENGINE library is in the `lib` folder inside your project. Simply go to `Project -> Properties -> Java Build Path -> Libraries -> Add JAR` and add `lib/litiengine-0.5.1.jar` to your project's build path.

#### IntelliJ IDEA
* Go to `File -> Project Structure` (Ctrl+Alt+Shift+S)
* Go to `Project Settings -> Libraries`
* Hit `New Project Library` / `+` (Alt+Insert) and locate `litiengine-0.5.1.jar`

## Download the LITIENGINE Java library via Build Automation Utilities
### Gradle
Add the LITIENGINE dependency to your Gradle project by adding the following code to your project's `build.gradle` file:

```groovy
apply plugin: 'java'
apply plugin: 'application'

repositories {
  mavenCentral()
}

dependencies {
  // For Gradle versions below 3.0
  compile 'de.gurkenlabs:litiengine:0.5.1'

  // For Gradle versions above 3.0
  implementation 'de.gurkenlabs:litiengine:0.5.1'
}
```
> **Note:** if you failed build, try to modify apply plugin: 'java' to apply plugin: 'java-library'

> The `compile` step has been deprecated since Gradle 3.0 - use `implementation` instead for newer versions!

A basic example for a Gradle based LITIENGINE project can be found [HERE](https://github.com/gurkenlabs/litiengine-gurk-nukem). Have a look at the project's `build.gradle` and `settings.gradle`.

### Apache Maven
Add the following code to your project's `pom.xml`:
```xml
<dependency>
  <groupId>de.gurkenlabs</groupId>
  <artifactId>litiengine</artifactId>
  <version>0.5.1</version>
</dependency>
```

### Apache Ant
To manage dependencies in Ant, you can [use Apache Ivy](https://emptyhammock.com/blog/download-dependencies-with-ant-and-ivy.html). 
Add the following code to `ivy.xml`:
```xml
<dependencies>
  <dependency org="de.gurkenlabs" name="litiengine" rev="0.5.1" />
</dependencies>
```