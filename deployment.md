---
description: How to distribute LITIENGINE games
---
> These are wip notes for the documentation

# TODO: Deployment

## How to relase your game

### Preparation

#### Update version

* Increment the build of the game \(e.g. v1.0.1 to v1.0.2\)
* Update version build in `MyGame.java` \(or whatever your Main class is called\)
* Update version build `build.gradle`
  * Update .exe version in `launch4j` configuration group 
* Commit the change

#### Create new release draft on github

* Go to your repository's _releases_ page
* List all the changes that have been made to the game here
  * Closed issues
  * Check all commits since last build
  * **This is crucial since the text will be reused for patch notes on different platforms**

### Build with Gradle

Build automation is a blessing! Let's have a look at how to build and deploy your game using Gradle.  
To build Windows executables, we are going to use the _launch4j_ plugin. We set up different Gradle tasks for each target platform as well.

Your project's `build.gradle` should look something like this:

```groovy
plugins {
  id 'edu.sc.seis.launch4j' version '2.4.4'
}

apply plugin: 'java'
apply plugin: 'eclipse'
apply plugin: 'maven'

archivesBaseName = "mygame"
version = "v1.0.2"
targetCompatibility = "1.8.0"

sourceSets {
  main.java.srcDir "src"
  main.java.srcDir "resources"
  main.java.srcDir "sounds"
  main.java.srcDir "maps"
  main.java.srcDir "localization"

  main.resources.includes = ["game.litidata"]
}

repositories {
   mavenCentral()
}

dependencies {
 compile project(':litiengine')
}

compileJava.options.encoding = 'UTF-8'

jar {
  from {
    configurations.runtime.collect {
      it.isDirectory() ? it : zipTree(it)
    }
    configurations.compile.collect {
      it.isDirectory() ? it : zipTree(it)
    }
  }  {
     exclude 'META-INF/services/**'
  }

  // make sure to only include service providers from the litiengine when directly referencing the project
  from ("${project(':litiengine').projectDir}/resources/") {
    include 'META-INF/services/**'
  }

  from('resources') 
  { 
    include '**/*' 
    exclude 'sprites/*'
  }

  from('sounds') { include '**/*' }
  exclude '**/*.dll'
  exclude '**/*.jnilib'
  exclude '**/*.dylib'
  exclude '**/*.so'
  exclude 'junit**/**'

  from 'game.litidata'

  manifest {
    attributes 'Class-Path': ".",
               'Main-Class': "de.gurkenlabs.mygame.MyGame"
  }
}

launch4j {
  mainClassName = 'de.gurkenlabs.mygame.MyGame'
  icon = 'icon.ico'
  outputDir = 'libs'
  outfile = archivesBaseName +'.exe'
  companyName = 'gurkenlabs.de'
  version = '1.0.2'
  textVersion = '1.0.2'
  copyright = '2020 gurkenlabs.de'
  bundledJrePath = 'jre'
  jvmOptions = ['-Xms256m', '-Xmx1024m']
  cmdLine = '-release'
}

task copyNativeLibs(type: Copy) { 
  def litiengineLibs ='../litiengine/build/libs'
  def buildFolder = new File(buildDir, 'libs')

  from(litiengineLibs) { 
   include '**/*'
   exclude '**/*.jar'
   exclude '**/*.zip'
   exclude 'LICENSE'
   exclude 'lib/**'
  }

  from('/dist/'){
    include 'icon.ico'
    include 'config.properties'
    include 'steam_appid.txt'
    include 'jre/**'
  }

  into buildFolder
}

build.dependsOn copyNativeLibs

task distZipWindow(type: Zip) {
   group 'build'
   from 'build/libs/'
   include '*.exe'
   include '*.dll'
   include 'config.properties'
   include 'jre/**'

   archiveName archivesBaseName + '-' + version + '-win.zip'
   exclude archiveName
   exclude 'jinput-dx8_64.dll'
   exclude 'jinput-raw_64.dll'
   exclude 'steam_api64.dll'
   exclude 'steamworks4j64.dll'
   destinationDir(file('build/libs/'))
}

task distZipLinux(type: Zip) {
   group 'build'
   from 'build/libs/'
   include '*.jar'
   include '*.so'
   include 'config.properties'

   archiveName archivesBaseName + '-' + version + '-linux.zip'
   exclude archiveName
   destinationDir(file('build/libs/'))
}

task distZipOSX(type: Zip) {
   group 'build'
   from 'build/libs/'
   include '*.jar'
   include '*.jnilib'
   include '*.dylib'

   include 'config.properties'

   archiveName archivesBaseName + '-' + version + '-osx.zip'
   exclude archiveName
   destinationDir(file('build/libs/'))
}

tasks.withType(JavaCompile) {
    options.encoding = 'UTF-8'
}
```

* Disable debug settings in the `config.properties`
* Set `Game.DEBUG = false` in `MyGame.java` before building anything that is released
* Execute the following Gradle tasks your game project \(order matters\)
  * _clear_
  * _fullbuild_
  * _build_ 
  * _createAllExecutables_
  * _distZipWindow, distZipLinux, distZipOSX_
* There should now be three archive files, one for each target platform: `mygame\build\libs\mygame-v1.X.X-win.zip mygame\build\libs\mygame-v1.X.X-linux.zip mygame\build\libs\mygame-v1.X.X-osx.zip`
  * Make sure that they contain the `jre` folder, the `jinput` and `steamworks` x86 native assemblies, the `config.properties` file \(and the `mygame.exe` executable in the Windows archive\).
  * These are the archives you are going to deploy to the players.

### Test

* Before deployment, we should quickly check if the game runs properly
* Copy the archive somewhere \(Desktop\), extract it and run the executable
* Ideally: Copy it to an empty VM instance \(e.g. a freshly created Windows 7\) and see if it runs

### Deploy

#### GitHub

* Upload created archive to the github release draft
* Polish the release description
* Publish the release

#### Steamworks

* Login to [https://partner.steamgames.com/?goto=%2Fhome](https://partner.steamgames.com/?goto=%2Fhome)
* Select "MyGame" App and go to `Edit Steamworks Settings/Steampipe/Builds`
* Since "MyGame" is probably &lt; 256MB, we can usually directly upload it here. 
* Upload new build
  * Describe it with something like "Update to version 1.X.X" so that we can later on identify what happend in that build by the patchnotes
* Set the build live on the development and default branches
* Update the game from Steam \(might need to restart the client\) and see if it runs properly

#### itch.io

* Edit your Game page
* Scroll down to `Uploads`
* Click `Upload files` and select the archive
* Select "Executable" for "Windows"
* Disable the old build for download and set the new one as default

### Share

#### Post the patch notes

* Possible headline: **Patch 1.X.X is live now!** 
* Create new patchnotes image
* Post patchnotes as new announcement on Steam Community `http://steamcommunity.com/games/{mygameid}/announcements/create/`
  * Make sure to check "Tag as Patch Notes"
  * Link it in 
    * twitter
    * fb
    * reddit/r/IndieGames/
    * instagram
    * tumblr
* Post patchnotes as new devlog on itch.io  `https://itch.io/dashboard/game/{mygameid}/devlog`

