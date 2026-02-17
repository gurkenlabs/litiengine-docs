---
meta.description: Learn about the Java Development Kit (JDK) and its different distributions.
meta.keywords: LITIENGINE, java, game, gameengine, development, 2D, programming, ide, eclipse, intellij, netbeans
---

# Install JDK

## Installing the Java Development Kit 
First of all, you should download a Java development kit (**JDK**), containing the Java virtual machine (**JVM**) and other resources for developing Java applications.
Since LITIENGINE has been created with Java 25, you need at least JDK 21 on your machine.
> In case you are on linux or mac, you can also use [SKDMAN!](https://sdkman.io/) to manager your JDK installation. Once you've installed sdk man, type `sdk install java` in your terminal. The latest recommend JDK will be installed automatically for you. It should be registered in your IDE after you restart it. For further information look up the [SDKMAN! Docs](https://sdkman.io/usage).

> **The official Oracle JDK has seen some severe licensing changes in 2019, requiring a paid license for developing commercial applications! You should use another JDK distribution with a permissive free license instead.** 

Here is a short overview over some entirely free JDK distributions:

name | implementations
:---- | :------
Eclipse Temurin      | [JDK 25](https://adoptium.net/temurin/releases/?version=25)
Amazon Correto    | [JDK 25](https://docs.aws.amazon.com/corretto/latest/corretto-25-ug/downloads-list.html)
Oracle Open JDK | [JDK 25](http://jdk.java.net/25/)
Red Hat OpenJDK | [JDK 25](https://developers.redhat.com/products/openjdk/download)
GraalVM | [JDK 25](https://www.graalvm.org/downloads/#)
