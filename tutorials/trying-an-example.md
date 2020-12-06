# Trying an example with LITIENGINE

서두

## Chapter 1:  Start trying the example

### What is the gradle?

### Where is the example code?

## Chapter 2:  SERVUS BONUS
![](https://static.jam.vg/raw/f36/2/z/23631.png)

SERVUS BONUS is a 2D game made by Steffen with Litienine. Steffen's github address is https://github.com/steffen-wilke. Currently, it is provided with the MIT license, so it can be modified freely.

**A good slave is a good servant. A great slave is currency!**

Play the tale of a slave monger with only one wish… to get admission to the great Roman open-air bath. Coming from the slums of Memphis, you have a long way of hardship before you. Gain respect by becoming the greatest slave monger of the Imperium Romanum.

SERVUS BONUS is a 2D action game about the story of defeating Roman soldiers and rescuing slaves as described above.  Use this example to check how to execute and modify the example and the results of the modification.

### How can I modify the example code?

Let's run the example first to see what it looked like before the modification.
The process of building and running the example code will be carried out through the gradle. The environment was conducted at ubuntu 20.04 WSL, but it also works normally with normal native or virtual machine Linux.

#### 1. For WSL
WSL users should set up the environment so that they can float the display of the window using the ubuntu terminal.
 
##### 1) Setting up .bashrc
```bash
vi ~/.bashrc
```
Using the above command. Enter the bashrc file and add the following command to the last line.
```bash
export DISPLAY=0:0
```

##### 2) Installing Xming
Xming performs when wsl users request to float the display of the window using the ubuntu terminal to configure the display. To run a game made with Litiengine on WSL, Xming must be installed so that the game screen can be printed out.

By the end of the above process, WSL users can complete the WSL setup to float the Litienine-based game.

## Chapter 2: Build and Run with gradle

Gradle's usage is detailed above, so omit it. However, it is not necessary to install the gradle directly to run SERVUS BONUS. If you use the gradlew file inside the *litienine-ldjam44* folder, you can download and run the appropriate version of the gradle to install SERVUS BONUS. However, if you run `./gradlew build` from the litienine-ldjam44 folder, the code folder of SERVUS BONUS, the build will fail. The reason is that the litiengine folder inside the litienine-ldjam44 folder is empty. SERVUS BONUS uses the library code inside the litienine folder, and if this litienine folder is empty, it does not run because there is no code in the API used by SERVUS BONUS. 

### 1. Downloading the litienine code

The Litienine code can be downloaded from github. Use the command below to download the Litienine code.
```bash
git clone https://github.com/gurkenlabs/litiengine.git/
```
Use this command to insert the downloaded Litiengine code into the litienine-ldjam44 folder.
The Litiengine code downloaded at this time is the latest code created by the efforts of the people who participated in the Litiengine project. However, SERVUS BONUS needs a code as of April 2019, not the most recent one. As Litiengine develops, SERVUS BONUS is using some of the deprecated codes, so it is necessary to downgrade them to the previous version.
```bash
git log 
```
Use the above command to check the litiignine commit log. If you lower this page, you will find a commit entitled **Allow holding a speechbubble.**

If you find this log, use the command below to downgrade the liti engine. Use the *\-\-hard* option because subsequent codes are unnecessary when using this example.
```bash
git reset --hard 61dbc657e772b3a05e262078e13a636b60c29e9
```
So we prepare the appropriate version of the Litienine code for SERVUS BONUS.

### 2. Get Permission of Gradlew
*gradlew* files allow you to proceed with build and run processes without installing *gradle*. However, the first time you download the litienine-ldjam44 code, you cannot run it because you do not have the execution permission in the *gradlew* file. Use the command below to give the execution permission.
```bash
sudo chmod 775 ./gradlew
```

### 3. Build and Run

Now that we're all set, let's run with build. Use the commands below to build and execute SERVUS BONUS.
```bash
./gradlew build
./gradlew run
```
If you do not insert **./** in front of the gridlew, an error may appear that there is no command called *gridlew*, so please insert ./ to specify that the gridlew inside the folder is executed.
After completing all of the above steps, the screen below is output and you can run SERVUS BONUS.

[!Alt_text](../images/run.gif)

## Chapter 3. Modify the code

Let's modify the downloaded SERVUS BONUS code so that the game can do what we want. There are three parts to modify through the code. 1) Attack speed, 2) Movement speed, 3) Change jump to dash. To modify the code, you must access the *src/de/gurkenlabs/ldjam44* folder inside the litienine-ldjam44 folder. Inside the final folder, ldjam44, there are codes that implement SERVUS BONUS's game operating mechanism.

### 1. Attack speed
Let's open the *Strike.java* file inside the *abilities* folder. Then you can find the code below.
```java
@AbilityInfo(name = "Strike", cooldown = 700, range = 0, impact = 15, impactAngle     = 360, value = 1, duration = 400, multiTarget = true, origin = AbilityOrigin.DIM    ENSION_CENTER)
```
This code applies information about the ability of the character to be a Strike. The lower the cooldown, the more attacks can be carried out, so let's reduce the cooldown.
```java
@AbilityInfo(name = "Strike", cooldown = 60, range = 0, impact = 15, impactAngle     = 360, value = 1, duration = 400, multiTarget = true, origin = AbilityOrigin.DIM    ENSION_CENTER)
```
Cooldown was reduced to 60 for much faster attack speed. Then try building and running and you'll get the following results.

[Alt_text](../images/cooldown_before.gif)
**Before**

[Alt_text](../images/cooldown_after.gif)
**After**

We can see the speed of attack that has been overwhelmingly faster.

### 2. Moving speed
Let's open the *Player.java* file inside the *entities* folder. Then you can find the code below.
```java
@MovementInfo(velocity = 30)
```
This code applies information about the movement speed of the character of the player. Let's increase Velocity to increase the speed of movement speed.
```java
@MovementInfo(velocity = 100)
```
Increase the Velocity to 100 for much faster movement speed. Then try building and running and you'll get the following results.


[Alt_text](../images/velocity_before.gif)
**Before**

[Alt_text](../images/velocity_after.gif)
**After**

We can see the speed of movement that has been overwhelmingly faster.

### 3. Change Jump to Dash
Let's open the *JumpEffect.java* file inside the *abilities* folder. Then you can find the code below.

```java
String jumpAnimation = "monger-jump";
if (this.angle < 180) {
	jumpAnimation = "monger-jump-right";
}
```
This code allows the player to take an action called *monger-jump* or *monger-jump-right*, which is set in advance when the player requests a jump. These actions are printed on the screen through the code below.

```java
Spritesheet jump = Resources.spritesheets().get("monger-jump");
controller.add(new Animation(jump, false));

final BufferedImage rightJump = Imaging.flipSpritesHorizontally(jump);
Spritesheet rightJumpSprite = Resources.spritesheets().load(rightJump, "monger-jump-right", jump.getSpriteWidth(), jump.getSpriteHeight());
controller.add(new Animation(rightJumpSprite, false));
```

The jump is carried out by reading *monger-jump* or *monger-jump-right* from spritesheets and printing them on the screen. These spritesheets are stored inside the *game.litidata* file in the litienine-ldjam44 folder.

```html
<sprite width="14" height="20" name="monger-jump">
  <image>iVBORw0KGgoAAAANSUhEUgAAACoAAAAUCAYAAAD7s6+GAAABGklEQVR42uWTMQ7CMAxFew     AmJFbYutCtHIEViZtwD47BAZgZ2bkCB0AqKytBrvRRcO20cUqEhCWrkWP3Od9JUfyjVfOpg/8s1M/P1m     wslPZPu23HLYeMajIWSnuL2aR1ysWafMghTZOwQCm+39StUw3WfeCkSVigIeC3JmGGUs69aVofqox1Ei     Yo7WF9KGtHDmDKe4h6WACGoM/jyuFL7gMRG0uUjjoxUNQgh9dgnSqIqI7fWHV7ON44b5Q3hxo/rvEsU3     hDcblRhJ8hroGlGn6PtXxJkL5JiEr5RdoPyuXacUczIYYkSIgzqFENTDHJtHvNlZME6b0CmjqhQ/mNni     /Xj0ZDylgmZ1In1WIEGU2dWMspiNlyCpLVXjWC/o8GBZLKAAAAAElFTkSuQmCC</image>
   <keyframes>150,200,150</keyframes>
</sprite>
```

The code above shows that a specific image is called up and printed on the screen. This is data that cannot be modified through code. It is something that needs to be modified in utiLITI.

## Chapter 4. Modify the example in the utiLITI

## Chapter 5. What's the difference of the utiLITI and the code?