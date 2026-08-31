---
title: "Build Systems & Dependency Setup"
icon: "lucide/wrench"
description: "Configure Gradle (Kotlin/Groovy) and Maven build automation with Java 21+ toolchains, Shadow JAR bundling, and LITIENGINE dependencies."
keywords: ["LITIENGINE build", "Gradle Kotlin DSL", "build.gradle.kts", "build.gradle", "pom.xml", "Java 21 toolchain", "shadowjar"]
tags: ["gradle", "maven", "build", "dependencies", "shadowjar", "toolchain"]
---

# Build Systems & Dependency Setup

Build automation utilities manage third-party libraries, compile Java source code, run automated tests, and package standalone executable archives.

LITIENGINE is distributed via **Maven Central** and is fully compatible with modern **Gradle** (Kotlin & Groovy DSL) and **Apache Maven**.

---

## Starter Build Configurations (Java 21+)

Select your preferred build tool below for a complete, production-ready configuration:

=== "Gradle (Kotlin DSL)"

    ```kotlin title="build.gradle.kts"
    plugins {
        java
        application
        id("com.gradleup.shadow") version "8.3.6"
    }

    group = "com.example.game"
    version = "1.0.0"

    repositories {
        mavenCentral()
    }

    java {
        toolchain {
            languageVersion.set(JavaLanguageVersion.of(21))
        }
    }

    dependencies {
        implementation("de.gurkenlabs:litiengine:0.11.1")
        testImplementation("org.junit.jupiter:junit-jupiter:5.11.4")
    }

    application {
        mainClass.set("com.example.game.Program")
    }

    tasks.shadowJar {
        archiveClassifier.set("all")
        manifest {
            attributes["Main-Class"] = "com.example.game.Program"
        }
    }
    ```

=== "Gradle (Groovy DSL)"

    ```groovy title="build.gradle"
    plugins {
        id 'java'
        id 'application'
        id 'com.gradleup.shadow' version '8.3.6'
    }

    group = 'com.example.game'
    version = '1.0.0'

    repositories {
        mavenCentral()
    }

    java {
        toolchain {
            languageVersion = JavaLanguageVersion.of(21)
        }
    }

    dependencies {
        implementation 'de.gurkenlabs:litiengine:0.11.1'
        testImplementation 'org.junit.jupiter:junit-jupiter:5.11.4'
    }

    application {
        mainClass = 'com.example.game.Program'
    }

    tasks.shadowJar {
        archiveClassifier.set('all')
        manifest {
            attributes 'Main-Class': 'com.example.game.Program'
        }
    }
    ```

=== "Maven (pom.xml)"

    ```xml title="pom.xml"
    <project xmlns="http://maven.apache.org/POM/4.0.0"
             xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
             xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
        <modelVersion>4.0.0</modelVersion>

        <groupId>com.example.game</groupId>
        <artifactId>my-litiengine-game</artifactId>
        <version>1.0.0</version>

        <properties>
            <maven.compiler.source>21</maven.compiler.source>
            <maven.compiler.target>21</maven.compiler.target>
            <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
        </properties>

        <dependencies>
            <dependency>
                <groupId>de.gurkenlabs</groupId>
                <artifactId>litiengine</artifactId>
                <version>0.11.1</version>
            </dependency>
        </dependencies>

        <build>
            <plugins>
                <plugin>
                    <groupId>org.apache.maven.plugins</groupId>
                    <artifactId>maven-shade-plugin</artifactId>
                    <version>3.5.2</version>
                    <executions>
                        <execution>
                            <phase>package</phase>
                            <goals>
                                <goal>shade</goal>
                            </goals>
                            <configuration>
                                <transformers>
                                    <transformer implementation="org.apache.maven.plugins.shade.resource.ManifestResourceTransformer">
                                        <mainClass>com.example.game.Program</mainClass>
                                    </transformer>
                                </transformers>
                            </configuration>
                        </execution>
                    </executions>
                </plugin>
            </plugins>
        </build>
    </project>
    ```

---

## IDE Setup & Project Importing

<div class="grid cards" markdown>

- :material-cube-outline:{ .lg .middle } **IntelliJ IDEA**

    ---

    1. Open IntelliJ and select **File &rarr; Open...**.
    2. Choose the root folder containing `build.gradle.kts` (or `pom.xml`).
    3. Select **Open as Project** and let Gradle sync dependencies automatically.

- :material-application-brackets-outline:{ .lg .middle } **Eclipse IDE**

    ---

    1. Select **File &rarr; Import... &rarr; Existing Gradle Project**.
    2. Browse to your project directory and click **Finish**.
    3. Ensure your Workspace Installed JRE is configured for **Java 21+**.

- :material-microsoft-visual-studio-code:{ .lg .middle } **VS Code**

    ---

    1. Install the **Extension Pack for Java** and **Gradle Extension for Java**.
    2. Open your project folder; VS Code will automatically detect and configure the Gradle wrapper.

</div>

---

## See Also

<div class="grid cards" markdown>

- :material-download-outline:{ .lg .middle } **[Get LITIENGINE](/getting-started/get-litiengine/)**

    ---

    Snapshot releases, JitPack builds, and manual JAR downloads.

- :material-play-box-outline:{ .lg .middle } **[Deployment & Packaging](/deployment/)**

    ---

    Packaging standalone native binaries with jpackage and Launch4j.

</div>
