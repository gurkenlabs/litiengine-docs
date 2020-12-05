# Start Gradle

## Chose a build system
LITIENGNINE supports Gradle and Maven. You can just download the .jar file and import it to use the library, but it is not recommended. Thus, here we will discuss how to install and start Gradle in Windows.  

## Download Gradle
You can download Gradle [Here](https://gradle.org/install/). 
![gradle-download](./img/gradle_download.png)
In the first step for **Installing manually**, click the **Download** and find latest version. If you need docs and sources, choose complete or binary-only.  
Then create a new directory `C:\Gradle` and unzip the downloaded file in this folder.  
Search the `Advanced system setting` on windows search and click click `Environment Variables`. Under `Systemp Variables` selet `Path`, then double click it. Add `C:\Gradle\[your-gradle-version]\bin` and click OK to save.  
Now you can use Gradle. There are two way you will use: import existing Gradle project or create new project. We will explain how to import projects becuase it will be used when you proceed the tutorial.

## Import Existing Gradle Project

Of course, you need to download a poject before importing it. [Gurk Nuckem](https://github.com/gurkenlabs/litiengine-gurk-nukem) is the example for this tutorial. Download the .zip file and unzip it.  
Then open Eclipse, right click on Package Explorer. Double click the `Gradle` folder and selet `Existing Gradle Project`. 
![import-existing-project](./img/import_existing_project)
Click Next button twice and Browse the path of folder which you downloaded before. Click the `Finish` button and wait for the project to be successfully imported.  
![import-existing-project-2](./img/import_existing_project_2)
Now your Package Explorer will be like this. Right click the Project folder and click `Run As`, `Java Application`. Then the game will be executed.

## Make New Gradle Project

1. new project
2. build.gradle
3. build
