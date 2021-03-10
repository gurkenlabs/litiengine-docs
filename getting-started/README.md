# Getting Started

## Install JDK

First of all, you should download a Java development kit (**JDK**), containing the Java virtual machine (**JVM**) and other resources for developing Java applications. Since LITIENGINE has been created with Java 8, you need at least JDK 8 on your machine.

> **The official Oracle JDK has seen some severe licensing changes in 2019, requiring a paid license for developing commercial applications!** 

Here is a short overview over some entirely free JDK distributions:

name | implementations
---- | ------
AdoptOpenJDK      | [JDK 8](https://adoptopenjdk.net/index.html?variant=openjdk8&jvmVariant=hotspot), [JDK 11](https://adoptopenjdk.net/index.html?variant=openjdk11&jvmVariant=hotspot), [JDK 15](https://adoptopenjdk.net/index.html?variant=openjdk15&jvmVariant=hotspot)
Amazon Correto    | [JDK 8](https://docs.aws.amazon.com/corretto/latest/corretto-8-ug/downloads-list.html), [JDK 11](https://docs.aws.amazon.com/corretto/latest/corretto-11-ug/downloads-list.html), [JDK 15](https://docs.aws.amazon.com/corretto/latest/corretto-15-ug/downloads-list.html)
Oracle Open JDK | [JDK 15](http://jdk.java.net/15/)
Red Hat OpenJDK | [JDK 8, JDK 11, JDK 15](https://developers.redhat.com/products/openjdk/overview)


## Setup IDE

>We highly recommend you to develop your LITIENGINE game with an IDE \(Integrated Development Environment\). This will serve you with a ton of useful development tools, like _code completion_, _debugging_, _build tools_, _unit test execution_ and much more that a plain text editor simply doesn't provide.

The most prominent IDEs for Java development are [Eclipse](https://www.eclipse.org/), [IntelliJ IDEA](https://www.jetbrains.com/idea/), and [Apache NetBeans](https://netbeans.org/) - **All of them are free to use!**

In our tutorials, we mostly reference the procedure for Eclipse, but the required steps are often very similar in other IDEs.

Currently, there is no built-in LITIENGINE support for any IDE but for future releases we plan to develop plugins that will help you bootstrapping and developing a LITIENGINE project.

> We've already started development on a [LITIENGINE Eclipse Plugin](https://github.com/gurkenlabs/litiengine-eclipse-plugin).

If you've chosen Eclipse as your IDE, you need to set up a workspace before launching it. Even if your IDE usually will detect a Java runtime when it's installed in the standard location, you should double-check that your IDE is aware of the correct path to the Java runtime.
To do this in Eclipse, unfold `Java` in the `Preferences` menu. Double click the `Installed JREs`, and click `Add`. Select `Standard VM` and go next. Click the `Directory...` button and find the JDK folder that you installed. Click `Finish` and `Apply and Close`. Now you are ready to use Eclipse for developing Java applications.

![eclipse-download-5](/getting-started/img/eclipse_download_5.png)


## Choose a build system

Have you heard of build automation utilities? If you don't want to manage and compile your software and dependencies by hand with every release, you can rely on build automation utilities to compile and package your source code, manage dependencies, and run automated tests.
Three build systems are predominantly used for Java development:
* [Gradle](https://gradle.org/)
* [Apache Maven](https://maven.apache.org/)
* [Apache Ant](https://ant.apache.org/) 

> Of course, it is possible to just download the LITIENGINE .jar and import and use the library manually the "oldschool" way. However, we don't encourage using a manually downloaded .jar for your game project as managing the whole life cycle of your software is *much* more straightforward using a dedicated build system.

LITIENGINE itself is built upon **Gradle** and uses it to seamlessly manage its build steps and dependent libraries.

Assuming that you chose [Eclipse IDE](https://www.eclipse.org/downloads/packages/release/kepler/sr1/eclipse-ide-java-developers) and [Gradle](https://gradle.org/), you can create gradle project with these steps:
* [download Gradle](https://gradle.org/install/).
* create a new directory `C:\Gradle` and unzip the downloaded file there. 
* add `C:\Gradle\[your-gradle-version]\bin` to your system's *PATH* environment variable.
* if there is no gradle plugin in your Eclipse installation, go to Help -> Eclipse Marketplace to search and install Gradle integration.
* click File > New > Other and select Gradle Project as wizard.
* two files are required in a Gradle project's root folder: `build.gradle`, containing the build tasks, and `settings.gradle`, containing Gradle settings.

## Initialize the project structure

Now, depending on the chosen build system, your project structure might look slightly different. LITIENGINE doesn't restrict you in how you can organize your project. However there are some common practices that we think are useful to apply for a Game project with the LITIENGINE:

* store your resources in `src` folders
* create multiple sub-folders for different types of resources
* save all the resources for your game within the project folder

### An example LITIENGINE project structure

```text
game-project
└─── sprites
│   │─── sprite1.png
│   └─── ...
│─── audio
│   │─── sound1.ogg
│   └─── ...
│─── maps
│   │─── map1.tmx
│   │─── tileset.tsx
│   │─── tileset.png
│   └─── ...
│─── localization
│   │─── strings.properties
│   │─── strings_de_DE.properties
│   └─── ...
│─── src
│   └─── com
│        └─── mygame
│             │─── Program.java
│             └─── ...
│─── .classpath
│─── game.litidata
│─── config.properties
└───...
```

