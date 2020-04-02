---
description: How to distribute LITIengine games
---

# Deployment

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

* Disable debug settings in the `config.properties`
* Set `Game.DEBUG = false` in `MyGame.java` before building anything that is released
* Execute the following Gradle tasks your game project \(order matters\)
  * _clear_
  * _fullbuild_
  * _build_ 
  * _createAllExecutables_
  * _distZipWindow_
* There should now be an archive file `mygame\build\libs\mygame-v1.X.X-win.zip`
  * Make sure that it contains the `jre` folder, the `jinput` and `steamworks` x86 native assemblies, the `config.properties` file and the `mygame.exe` executable
  * This is the archive that will be deployed to players on Windows

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

