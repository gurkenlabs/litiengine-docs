# utiLITI

## What is utiLITI?

utiLITI is the project management and map creation tool that comes with LITIENGINE. While you can use LITIENGINE entirely without it, especially beginners are advised to use the utiLITI. It offers the following benefits:

* **Project and Asset Management**:
  * When creating a project in utiLITI, a _game resource file_ will be created containing all necessary assets for your game.
  * Import Maps, Tilesets, Spritesheets, custom Emitters, and entity blueprints into your projects.
  * The assets will even be included in the project's xml file, which you can choose to encode when deploying your game to prevent plagiarism.
* **Map Creation**:
  * When creating .tmx maps with tiled, MapObjects are only Rectangles containing some String attributes.
  * With utiLITI, we offer a MapObject creation workflow that is directly forged into the LITIENGINE workflow:

    Create Props, Creatures, Lights, Triggers, SpawnPoints, CollisionBoxes, Areas, StaticShadows, and Emitters and instantly see your results rendered in LITIENGINE, allowing for more efficient adjustments.

  * Adjust your MapObjects' properties more comprehensively with sliders, spinners, checkboxes, dropdown menus, and add custom properties to MapObjects.
  * Set Map properties such as colors for ambient light and static shadows, Map title, and description.

## How to install utiLITI
The utiLITI editor is part of the [LITIENGINE SDK](https://litiengine.com/download/). Download it to get started.

![sdk-download](/getting-started/img/sdk_download.png)

* **Windows**: Unzip the downloaded file and execute `utiliti-win/utiliti-vX.X.X.exe`.
* **Linux/Mac**: Unzip the downloaded file and execute `utiliti/utiliti-vX.X.X.jar`.

> You might have to explicitly set execute permissions to the downloaded files. E.g. on Mac, try something like:
`chmod +x /Applications/litiengine-sdk-vX.X.X-beta-macos/utiliti/litiengine-utiliti.app/Contents/MacOS/*`. 


If nothing went wrong, you should see the following window with an empty project:

![empty_project](/getting-started/img/sdk-download_3.png)

