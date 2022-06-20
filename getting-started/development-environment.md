---
meta.description: Learn how to set up a development environment.
meta.keywords: LITIENGINE, java, game, gameengine, development, 2D, programming, ide, eclipse, intellij, netbeans
---

# Development Environment

## Setup IDE

>We highly recommend you to develop your LITIENGINE game with an IDE \(Integrated Development Environment\). This will serve you with a ton of useful development tools, like _code completion_, _debugging_, _build tools_, _unit test execution_ and much more that a plain text editor simply doesn't provide.

The most prominent IDEs for Java development are [Eclipse](https://www.eclipse.org/), [IntelliJ IDEA](https://www.jetbrains.com/idea/), and [Apache NetBeans](https://netbeans.org/) - **All of them are free to use!**

In our tutorials, we mostly reference the procedure for Eclipse, but the required steps are often very similar in other IDEs.

Currently, there is no built-in LITIENGINE support for any IDE but for future releases we plan to develop plugins that will help you bootstrapping and developing a LITIENGINE project.

### Eclipse
> We've already started development on a [LITIENGINE Eclipse Plugin](https://github.com/gurkenlabs/litiengine-eclipse-plugin).

If you've chosen Eclipse as your IDE, you need to set up a workspace before launching it. Even if your IDE usually will detect a Java runtime when it's installed in the standard location, you should double-check that your IDE is aware of the correct path to the Java runtime.
To do this in Eclipse, unfold `Java` in the `Preferences` menu. Double click the `Installed JREs`, and click `Add`. Select `Standard VM` and go next. Click the `Directory...` button and find the JDK folder that you installed. Click `Finish` and `Apply and Close`. Now you are ready to use Eclipse for developing Java applications.

![eclipse-download-5](/getting-started/img/eclipse_download_5.png)

### IntelliJ IDEA
To make sure the JDK got installed correctly, open the `New Project` dialogue and expand the `JDK` dropdown menu. If you see your installed JDK in the list, you're set. If you don't, you have to click on the `Add JDK...` button. A file picker dialogue will open, choose your JDK folder there.

> If you're on linux or mac, you can also use [SKDMAN!](https://sdkman.io/) to manager your JDK installation . If you installed sdk man, type `sdk install java` in your terminal. The latest recommend JDK will be installed automatically for you. It should be registered in your IDE after you restart it. For further information look up the [SDKMAN! Docs](https://sdkman.io/usage).

![intellij-picker](../images/intellij_picker.png)
