## DAY 1: The first Level

#### Creating a project in utiLITI

For a general idea about what utiLITI is, read the [docs page about utiLITI](https://docs.litiengine.com/getting-started/creating-a-project/utiliti-editor) first. Start the utiLITI editor. Hit "**File -> Create project**" (Shortcut: **CTRL+N**). [caption id="attachment_317" align="aligncenter" width="650"]![utiLITI-createProject](https://staging.litiengine.com/wp-content/uploads/2018/12/1-createProject-300x201.png) Creating a project with utiLITI[/caption] In the file browser that pops up, navigate to your project directory and hit **open**. Even if you still have done nothing, hit **save** to create a game resource file. You can name it whatever you want, we go for something like "game.litidata" in this guide.

#### Importing Assets

Let's assume that you've already created assets for your game. In our case, we picked a 4-colour GameBoy style for our project. So what basic Assets do we have at this point?

*   Player sprites: For entities that are child classes of `Creature`, there are naming conventions for walking and idle sprites. We need sprites named like {SPRITE_PREFIX}-{STATE}-{DIRECTION}.{EXTENSION}. Following these naming conventions, we create **gurknukem-idle-left.png** and **gurknukem-walk-left.png.** You only need to provide a _left_ or a _right_ sprite in both cases, the `CreatureAnimationController` will automatically flip it when necessary. 

[caption id="attachment_327" align="aligncenter" width="256"]![gurknukem-idle-left](https://staging.litiengine.com/wp-content/uploads/2018/12/gurknukem-idle-left.jpg) gurknukem-idle-left.png[/caption]

[caption id="attachment_328" align="aligncenter" width="512"]![gurknukem-walk-left](https://staging.litiengine.com/wp-content/uploads/2018/12/gurknukem-walk-left.jpg) gurknukem-walk-left.png[/caption]
*   Enemy sprites: We also add two enemy designs to the game. The naming is done in the same way as for our main character, so we end up with four image files: **dean-idle-left.png**, **dean-walk-left.png**, **jorge-idle-left.png**, **and jorge-walk-left.png**. 

[caption id="attachment_331" align="aligncenter" width="512"]![Dean-walk-left](https://staging.litiengine.com/wp-content/uploads/2018/12/Dean-walk-left.png) dean-walk-left.png[/caption]

[caption id="attachment_332" align="aligncenter" width="512"]![Jorge-walk-left](https://staging.litiengine.com/wp-content/uploads/2018/12/Jorge-walk-left.png) jorge-walk-left.png[/caption]

*   Prop sprites For now, we will only add two props: a bunker and a destructive barrel. For props, there are naming conventions, too: prop-{PROPNAME}-{STATE}.{EXTENSION} This means that we need three image files for our destructible barrel: **prop-barrel-intact.png**, **prop-barrel-damaged.png**, **and prop-barrel-destroyed.png** Non-destructible props such as our bunker only need one animation file, in our case **prop-bunker.png**. 

[caption id="attachment_340" align="aligncenter" width="832"]![prop-bunker](https://staging.litiengine.com/wp-content/uploads/2018/12/prop-bunker.png) prop-bunker.png[/caption] 

[caption id="attachment_341" align="aligncenter" width="240"]![prop-barrel](https://staging.litiengine.com/wp-content/uploads/2018/12/prop-barrel.png) destructible barrel states[/caption]

*   Our game logo: 

![Gurk Nukem Logo](https://staging.litiengine.com/wp-content/uploads/2018/12/Logo-1.png)
*   Our game icon: 

![Gurk Nukem window icon](https://staging.litiengine.com/wp-content/uploads/2018/12/icon-150x150.png)
*   A music track
*   A .tsx tileset created with Tiled editor from an image file
*   A .tmx map created with Tiled editor using our Tileset

To import Sprite files into utiLITI, either **drag&drop selected files into the Asset panel** on the lower end of the screen or hit "**Project -> import Spritesheets**". The same goes for tilesets ("**Project -> import Tilesets**"). Maps can be imported by clicking "**Map -> import...**". If a map was successfully imported, it will be rendered in the map panel and listed in the map list right to it. 

[caption id="attachment_355" align="aligncenter" width="650"]![utiLITI-levelLoaded](https://staging.litiengine.com/wp-content/uploads/2018/12/2-levelLoaded.png) An example map and some spritesheets loaded into utiLITI[/caption]

#### Basic Mapping

Adjust your grid and snapping settings in the **View** menu. In the **Layer** toolbox in the upper right corner, you can **Add, Delete, Recolor, Rename, Duplicate, Focus / Hide, and reorder `MapObjectLayers`**. To maintain a comprehensive structure to our map files, we try to create at least one layer for each `Entity`type (There is the "Entities" tab to help you navigate through entities by type, as well). _Let us now create your first entity!_ Select a MapObjectLayer, then right-click somewhere on the map and hit "**Add -> Add CollisionBox**" or use the "Add MapObject" icon in the toolbar. **Click and drag** with your mouse to specify the bounding box of your Collision box as shown in the gif below.

[caption id="attachment_359" align="aligncenter" width="600"]![utiLITI-createCollision](https://staging.litiengine.com/wp-content/uploads/2018/12/3-createCollision.gif) Creating a Collision Box in utiLITI[/caption]

In the same manner, create a `Spawnpoint`that will be used to spawn our player entity. Edit the Spawnpoint's Attributes in the Map Object Panel on the right as shown below. You can give the Spawpoint a name for identification and set the spawn direction for our Player.

[caption id="attachment_361" align="aligncenter" width="601"]![utiLITI-spawnpointSetup](https://staging.litiengine.com/wp-content/uploads/2018/12/4-spawnpointSetup.gif) Editing Spawnpoint attributes[/caption]

Before we look into coding now, we will set some basic properties for your map such as its name, description, and static shadow color. Simply hit "**Map -> Properties**" and you will see a popup for editing Map properties.

[caption id="attachment_363" align="aligncenter" width="599"]![utiLITI-mapProperties](https://staging.litiengine.com/wp-content/uploads/2018/12/5-mapProperties.gif) Editing Map properties in utiLITI[/caption]

Congratulations! You've successfully completed the first steps on your way to creating a platforming shooter with LITIengine. Learn about setting up the basic functionality of our game in **Chapter 2: Time to pull out your hacker gloves**.