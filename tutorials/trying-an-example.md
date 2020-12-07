# Trying an example with LITIENGINE

## Chapter 1:  Start trying the example

### What is the gradle?

Gradle is a build automation system using groovy. It adopts a domain language similar to Groovy, and is also the official build system of Android Studio, which is required to create Android apps. It supports several languages such as Java, C / C++ , and Python. [Wikipedia contributors. (2020b, November 26). Gradle. Wikipedia. https://en.wikipedia.org/wiki/Gradle](https://en.wikipedia.org/wiki/Gradle)

To install gradle and execute it firstable download <https://gradle.org/install/>. Next set $PATH and $CLASSPATH. For more specific settings about the environment variable visit [getting-started/start-gradle.md].

If things are going well, type gradle -v and check. 
```bash
gradle -v 
``` 

Make a JAVA project and file to build, and in the project folder make buld.gradle file. In this file apply plugin:'java'
```bash
plugin:'java' 
``` 
Now, almost there!
```bash
gradle build
```  
If you do "gradle build", gradle tests, compiles and then makes jar file.
This is it for basic gradle execution. For more complicated project dependency resolution process is needed. However, in this example, SERVUS BONUS, gradle wrapper is used. So, I will wrap it up here. 

### Gradle Wrapper

In this tutorial, SERVUS BONUS, gradle wrapper which is preferred way to build project is used. The biggest advantage of using it is when executing an project that already exists on a new environment, it enables direct build without any installation nor settings for different version of JAVA or Gradle. 

However, in this case, executing "./gradlew build" makes an error message telling that JAVA version does not match with the SERVUS BONUS project. The SERVUS BONUS requires some JAVA 8 library which does not match with latest JAVA version,11. 

Therefore, check the below code, and if JAVA version is other than JAVA 8, download JAVA 8 and set environment variable accordingly where the jdk file exist.

```bash
java --version
``` 
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

### 1.UtiLITL run and utilize 

먼저 utiLITL 를 실행하기 위해서 litiengine 에서 제공해주는 utiliti-v0.5.0-beta.jar를 다운 받게 된다면 map editor인 utiLITI 기본 툴이 다운 받아진다. 이제 여기서 SERVUS BONUS의 map 을 edit 하기 위해서 utiLITI- File-Open을 통해서 위에서 미리 다운 받은 Litiengine-ldjam44 폴더 내부에 있는 game.litidata를 실행한다

### 2. Modify the map directly

위에서 Code를 통해 수정할 요소 3가지1) 공격 속도, 2) 이동속도, 3) 점프를 대시로 변경 을 utiLITI로 가능한지 알아보자. 먼저 아이콘을 만들고 이 아이콘을 아래와 같은 방식으로 수정이 가능하다.

#### 1) 공격속도

#### 2) 이동속도

utiLITI에서 아이콘을 클릭하면 해당 아이콘의 Movement 수치를 볼수 있다. utiLITL는 acceleration, deceleration, velocity를 제공하는데 이를 이용하여 아이콘의 이동 속도를 바꿀수 있는지 알아보았다. example로 사용한 아이콘은 slave 이며 code 에서와는 다르게 단순 map editor 이므로 주인공을 제외한 주변 사물처럼 취급되는 아이콘들만 utiLITI에서 변경 가능하다 (단, 주인공 아이콘의 이미지에 관련된 것은 여기서 바꿀 수 있다).
결과적으로 utiLITI만으로는 아이콘의 이동 속도를 변경할 수 없다. 

#### 3) 점프를 대시로 변경

점프를 대시로 변경하기 위해선 두가지 방법이 있다. 첫번째 코드를 바꾸는 방법. "monger-jump" 아이콘 자체를 "dash"로 바꾸기. utiLITI로는 두번째 방법이 가능하다.


## Chapter 5. What's the difference of the utiLITI and the code?
