---
title: "Install JDK"
description: "Learn about the Java Development Kit (JDK 21+ / JDK 25) requirements, distributions, and installation methods for LITIENGINE."
keywords: ["LITIENGINE", "java", "JDK", "JVM", "SDKMAN", "Temurin", "GraalVM", "Java 21", "Java 25"]
---

# Install JDK

## Installing the Java Development Kit

To develop games with LITIENGINE, you need a Java Development Kit (**JDK**) containing the Java Virtual Machine (**JVM**) and Java compiler.

LITIENGINE requires **JDK 21 LTS or later** (with modern snapshots targeting **JDK 25**).

> [!TIP]
> On macOS and Linux, you can easily install and manage multiple JDK versions using [SDKMAN!](https://sdkman.io/):
> ```bash
> sdk install java
> ```

## Recommended Free JDK Distributions

We recommend using an OpenJDK distribution with a permissive open-source license:

| Distribution | Supported Versions & Download |
| :--- | :--- |
| **Eclipse Temurin** (Adoptium) | [Download Temurin JDK](https://adoptium.net/temurin/releases/) |
| **Amazon Corretto** | [Download Amazon Corretto](https://docs.aws.amazon.com/corretto/) |
| **Oracle OpenJDK** | [Download OpenJDK](https://jdk.java.net/) |
| **Red Hat OpenJDK** | [Download Red Hat OpenJDK](https://developers.redhat.com/products/openjdk/download) |
| **GraalVM** | [Download GraalVM](https://www.graalvm.org/downloads/) |

## Verifying Your Installation

Once installed, open your terminal or command prompt and verify your Java version:

```bash
java --version
javac --version
```

Both commands should return version `21` (or higher).

## Next Steps

Now that your JDK is ready, proceed to **[Set Up Your IDE](development-environment.md)**.
