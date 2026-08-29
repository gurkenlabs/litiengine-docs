---
meta.description: Release notes for the LITIENGINE that include a complete changelog with all fixes, changes, improvements and a list of added and removed features.
meta.keywords: FAQ, questions, LITIENGINE, java, game, gameengine, development, 2D, programming
---


# LITIENGINE Release notes

## 0.11.1 - "Input4j Migration"

This release brings major improvements across the engine, editor (utiLITI), input system, file I/O, iconography, documentation, build tooling, and overall stability. The most notable change is our migration towards our own custom input framework: Say goodbye to *JInput*, say hello to [Input4j](https://github.com/gurkenlabs/input4j), improving the cross platform support and eliminating the need to deploy native third party binaries along the engine by utilizing the Java FFM API. We've also migrated the engine to Java 25 and Gradle 9.

### Engine & Core Improvements
- Rewrote the input system to use Input4J instead of JInput
- Significantly improved JavaDocs coverage
- Improved physics and collision handling
- Added copy constructors
- Attribute system improvements with event support for value and modifier changes
- Added a new transparency image effect
- Improved state machine behavior

### utiLITI Enhancements
- Major File I/O overhaul with unified use of Path/Paths
- Refactored package structure toward MVC
- Replaced all raster icons with scalable vector icons
- Added light and dark icon theme variants

### Build Updates
- Migrated to Java 25, producing artifacts compatible with JDK 17
- Updated Gradle wrapper to 9.2.1
- Adopted the Reckon plugin for versioning
- Configured Gradle Maven Publish plugin to publish to Sonatype Central Portal

## 0.10.7

- Fixed memory leak in SoundEngine (contributed by @Gamebuster19901)
- Upgrade to Java 23
- Implemented automatic itch.io deployment for Linux & Windows
- Various dependency updates

## 0.9.0

- Enhanced sprite dimension determination in sprite import panel
- Fixed alignment of text that overflows boundaries
- Fixed NullPointerException in TextRenderer#renderWithLinebreaks
- Added horizontal Menus
- Adjusted Creature sprite naming conventions
- Various dependency updates

## 0.8.0

> You might wonder why we've skipped version 0.7.x. This has been due to tests on our automated release pipeline that have created some release versions with 0.6.x and 0.7.x tags.

- Enhanced sprite dimension determination in sprite import panel
- Upgraded Gradle wrapper from 8.4 to 8.5
- Added TMX 1.10 support
- Improved test coverage
- Automate release announcements

## 0.6.0 - "Trick or Treat!"
![LITIENGINE 0.6.0 banner](https://litiengine.com/wp-content/uploads/2023/10/litiengine-patch-banner-0.6.0.png)

Surprise! After a quiet period of not releasing a new engine version since January 2022, we proudly present LITIENGINE 0.6.0. This is a release packed mostly with invisible infrastructure changes and refactorings, but also enhanced documentation, tests, and important bugfixes.

There had been some crucial problems in our build and deploy toolchain, which prevented us from releasing new versions for quite a while, but these problems have been resolved and now we are even releasing nightly snapshot builds for you to test out the latest changes!

You may have noticed the versioning of LITIENGINE has changed too. 
Instead of e.g. `v0.5.2-beta`, we are now using plain semantic versions for stable releases (starting with this release `0.6.0`) and a modified `git describe` variant (e.g. `0.5.2-166-gb2e597fe-SNAPSHOT/`) for snapshot versions.

Since the last release, we have updated to a more recent Java version several times, and recently we have finally moved to the new LTS version Java 21. That means you can now use all the new cutting-edge Java features in your LITIENGINE games!

    Of course, we want to thank all our contributors, sponsors, users, and community members for keeping LITIENGINE alive even when we maintainers get lazy. You are the heart of this project!

Here's a quick overview of the changes in this release:

**Build Infrastructure:**
* Updated project to Java 21
* Restored releasability through GitHub actions
* Introduced nightly snapshot builds
* Switched versioning to Semantic Versions (assisted bySemVerGuru Gradle plugin.)
* Cleaned up Gradle dependency management and updateddependencies
* Rename master branch to main.
* Restored SonarQube analysis
* Cleaned up and refactored Gradle project structure

**Improvements:**
* Implemented multi-target ForceEffects. 
* Implemented StateEvents to register actions when a State isentered/exited.
* Implemented 9-sliced image scaling. 
* Added 9-slice scaling option for ImageComponent backgrounds. 
* Added shortcut methods to determine a GuiComponent's centerpoint.
* Added color interpolation helper.
* Turned AntiAliasing on for rendering object boxes in utiLITI
* Added image scaling overloads for bilinear and bicubicinterpolation.
* Separated emitter saving in utiLITI from blueprint definition.
    
**Bugfixes:**
* Fixed EntityEmitter location jittering.
* Fixed Particle opacity calculation.
* Fixed SoundPlaybacks. (contributed by @Gamebuster19901)
* Fixed Ability impact area calculation.
* Fixed particle spritesheet assignment dropdown in utiLITI.
* Fixed an issue with sticky forces
* Fixed a bug that prevented the utiLITI asset panel fromrefreshing.
* Fixed threading issues in GameTests by introducingGameTestSuite (contributed by @Gamebuster19901)
* Fixed duplicate attribute modification in GuiComponentlocation setters. (contributed by @ecchilds)

**API changes:**
* Renamed `Effect.canAttackEntity` to `canAffectEntity`.

**Removals / Deprecations:**
* Removed CompressionUtilities (and tests). There were vulnerabilities in our implementation and the utilities have never actually been used. End users will have a much better experience using libraries such as zip4j.

**Documentation and Miscellaneous:**
* Updated license.
* Updated contribution guide.
* Added star history to readme.
* Removed individual developers' funding links.
* Added .cff citation file.
* Improved JavaDocs
* Added more projects to [LITIENGINE showcase](https://litiengine.com/showcase/) 

## v0.5.2-beta - "Java 17 Migration"

![LITIENGINE v0.5.1-beta featureimage](https://litiengine.com/wp-content/uploads/2021/12/litiengine-patch-banner-0.5.2.png)

Just in time for making your new year's resolution of creating amazing games with LITIENGINE, we proudly present our latest update, packed with 250 commits over the last ten months!

Let's talk about the elephant in the room: LITIENGINE is now fully running on Java 17! In the future, we plan to keep the library updated to the latest stable jdk versions for you to utilize all the juicy new features Java has to offer.

To make building ingame UI more pleasant, the `Slider`, `TextFieldComponent`, and `SpeechBubble` components have seen massive updates.

Bugfixes and UX improvements for utiLITI will ensure a more smooth experience when handling the editor.

Apart from that, a lot has changed in our build and deployment pipeline and the repository is now utilizing GitHub actions instead of Travis CI. This goes along with a completely revised directory structure and proper separation of submodules. The way we bundle native libraries has been adapted and the dependency on steamworks4j has been removed. Please also take note of our changed contribution guidelines: it is now required to comply with the Java code style conventions we provide in the repository (see [CONTRIBUTING.md](https://github.com/gurkenlabs/litiengine/blob/master/CONTRIBUTING.md)).

Finally, a huge THANK YOU is in order: To all our new code contributors, to the community involved in discussing issues, to everyone providing help in our forum and on Discord, and lastly:
Thank you to our new Sponsors [RajBet](https://raj.bet/), [Trust My Paper](https://www.trustmypaper.com/), [CasinoHex Canada](https://onlinecasinohex.ca/), and [ej-technologies](https://www.ej-technologies.com/products/jprofiler/overview.html) (in chronological order of sponsorships)!

What are you waiting for? Start the new year the right way: making games with LITIENGINE.

#### ✅ Fixes

* [#373](https://github.com/gurkenlabs/litiengine/pull/373) Fixed `ArrayIndexOutOfBoundsException` (contributed by [@Gamebuster19901](https://github.com/Gamebuster19901))
* [#378](https://github.com/gurkenlabs/litiengine/pull/378) Fixed deadlock in `StatusBar` (contributed by [@Gamebuster19901](https://github.com/Gamebuster19901))
* [#394](https://github.com/gurkenlabs/litiengine/pull/394) Fixed endless recursion for `ResourcesContainer::getAsync(String)` (contributed by [@EagleoutIce](https://github.com/EagleoutIce))
* [847c523](https://github.com/gurkenlabs/litiengine/commit/847c523b453169e20fa86d0c404e17da0702c160), [5fffe4f](https://github.com/gurkenlabs/litiengine/commit/5fffe4f639e7840b16f9983aaf9b139effecee25) Prevented two `NullPointerExceptions` in SoundSources
* [87085d7](https://github.com/gurkenlabs/litiengine/commit/87085d7bc5d36359bf39f23e1ad3ca6449d59b3c) Crucially improved robustness and usability of slider GuiComponents
* [1f27427](https://github.com/gurkenlabs/litiengine/commit/1f2742708e64c3a48d439c923bc1cea8573e68a9) Removed `final` modifiers from serializable Tmx properties in Triggers
* [01da7e0](https://github.com/gurkenlabs/litiengine/commit/01da7e03196548bf286de84317d864896c53ea90) Ensured animation caching
* [7beda04](https://github.com/gurkenlabs/litiengine/commit/7beda046338c75516bad9662d4f853f86ba2f6c1) Fixed Polygon particle rounding errors.
* [#441](https://github.com/gurkenlabs/litiengine/pull/441) Fixed wrong type of EntityController being removed with `clearControllers()` (contributed by [@Gamebuster19901](https://github.com/Gamebuster19901))
#### ⭐ Features/Improvements

* [#376](https://github.com/gurkenlabs/litiengine/pull/376), [#377](https://github.com/gurkenlabs/litiengine/pull/377), [#381](https://github.com/gurkenlabs/litiengine/pull/381), [#382](https://github.com/gurkenlabs/litiengine/pull/382), [#383](https://github.com/gurkenlabs/litiengine/pull/383), [#385](https://github.com/gurkenlabs/litiengine/pull/385), [#386](https://github.com/gurkenlabs/litiengine/pull/386), [#388](https://github.com/gurkenlabs/litiengine/pull/388), [#389](https://github.com/gurkenlabs/litiengine/pull/389), [#390](https://github.com/gurkenlabs/litiengine/pull/390), [#396](https://github.com/gurkenlabs/litiengine/pull/396), [#397](https://github.com/gurkenlabs/litiengine/pull/397), [#398](https://github.com/gurkenlabs/litiengine/pull/398), [#403](https://github.com/gurkenlabs/litiengine/pull/403) Vastly improved test coverage (contributed by [@DanielH4](https://github.com/DanielH4), [@nwessman](https://github.com/nwessman), [@jluech](https://github.com/jluech), [@ddreimane](https://github.com/ddreimane), [@niels89](https://github.com/niels89))
* [c42dc23](https://github.com/gurkenlabs/litiengine/commit/c42dc231c8e17b4791553ad3b96b76aa890e002b) Added gamepad mapping for DualShock4 controller
* [8469c67](https://github.com/gurkenlabs/litiengine/commit/8469c674e4e43f371f008e236e43ea4f33afef53) Guess type of connected gamepads from the most probable variants.
* [d6449ee](https://github.com/gurkenlabs/litiengine/commit/d6449eebdacde3bf9a877be5d682a221a518d46c), [0cac85a](https://github.com/gurkenlabs/litiengine/commit/0cac85af937d2ccd2d930f639a8697caff0a2ff3) Add TweenType OPACITY and implement opacity Tweening on GuiComponents.
* [d930a8b](https://github.com/gurkenlabs/litiengine/commit/d930a8b6234f91cff1715a1d801a9229d7aa4b52) Added EntityNavigator overload for using an uninitialized PathFinder.
* [7047c83](https://github.com/gurkenlabs/litiengine/commit/7047c835aa2ad9befcdaf83dfb2cb4634ae18f31) Disable collision just before firing death events.
* [f4fa77b](https://github.com/gurkenlabs/litiengine/commit/f4fa77b12144d44ae5b30de5ba271d436b27256d) Added support for setting int and double array fields via `ReflectionUtilities`
* [5e126bf](https://github.com/gurkenlabs/litiengine/commit/5e126bf1daa6da3bf55842c1dd03668c30c8b6ed), [5227848](https://github.com/gurkenlabs/litiengine/commit/52278485b4e5af6149c2d37d8a67e230f7cff077), [350c137](https://github.com/gurkenlabs/litiengine/commit/350c1377f5881eeca6878b5bd2809e067ec54cb1), [4a24304](https://github.com/gurkenlabs/litiengine/commit/4a243046d7bc1f4ee8ce67c13b17b9a618b5e768) `TextFieldComponent` improvements:
  * Made blinking cursor configurable
  * Enabled automatic line breaks
  * Ensured input termination on mouse clicks outside an active text field
* [1bcdf2a](https://github.com/gurkenlabs/litiengine/commit/1bcdf2a235b4ec0ef3791f11dc1fd93649ada840) Excluded entities that cannot collide with a Trigger from activating it
* [bfc8d2f](https://github.com/gurkenlabs/litiengine/commit/bfc8d2fe350ff67edc008fd32f87e56b726b78cf) Added events for GuiComponent rendering
* [0ee92fa](https://github.com/gurkenlabs/litiengine/commit/0ee92faaede4d9411ebbce2b601c12ddc8244cf5), [634ba28](https://github.com/gurkenlabs/litiengine/commit/634ba28701a07547569421fc673dcda2baa92cec), [bd81b76](https://github.com/gurkenlabs/litiengine/commit/bd81b76becf7a70175c75435cf084e14043f4e0f) Performance optimizations
* [09bccf3](https://github.com/gurkenlabs/litiengine/commit/09bccf320c777e27b9e6a821ad3dcc417a311455) Made VAlign xml names consistent with enum names
* [b3c47f9](https://github.com/gurkenlabs/litiengine/commit/b3c47f9c135d80d3b762a186b127fef714481b5e) Ensured that event registrations are passed through to the current gamepad
* [2e055a2](https://github.com/gurkenlabs/litiengine/commit/2e055a238504952cd83dae793b520f4524455202) Set default color for particles on initialization
* [64ea5c8](https://github.com/gurkenlabs/litiengine/commit/64ea5c8d9fb80ddbd46b19d9e7f978bf5fcf48bc) Reimplemented `SpeechBubble` as a GuiComponent for more configurabiLITI

#### 🔀 Changes

* Migrated project to Java 17
* Migrated deployment pipeline from Travis to GitHub actions
* Updated Gradle Wrapper from 6.8 -> 7.2
* Established Java code style conventions and enforced them via spotless Gradle plugin.
* Introduced workflow to build nightly snapshots
* [bc869ef](https://github.com/gurkenlabs/litiengine/commit/bc869ef528cb1e26c6866d4d8c06d3e777ad927e) Defined Google Java code style as a convention for the repository
* [#413](https://github.com/gurkenlabs/litiengine/pull/413), [#423](https://github.com/gurkenlabs/litiengine/pull/423), [#424](https://github.com/gurkenlabs/litiengine/pull/424) Major refactorings to build scripts, project layout, and Sonar scan configuration(contributed by [@weisJ](https://github.com/weisJ))
* [c9d2e4e](https://github.com/gurkenlabs/litiengine/commit/c9d2e4ed7cae791883c16e017bcfb19e0f8af06e) Reduced unit test visibility to `default` due to JUnit 5 migration
* [df8cf8b](https://github.com/gurkenlabs/litiengine/commit/df8cf8b288b159d253e53bb2e45afbfb3cd9f739) Replaced Gradle Natives plugin with a manual approach
* [c31fffd](https://github.com/gurkenlabs/litiengine/commit/c31fffdfc521682e0a31f68cdc28bed929a030e4) Retrieve gamepads by ID instead of index
* [6ce69b5](https://github.com/gurkenlabs/litiengine/commit/6ce69b5c22fd1ec156af386d3b3abfc75ef73a91) Removed steamworks4j as a required library
* [ae42e12](https://github.com/gurkenlabs/litiengine/commit/ae42e1249b2f816c2b5d83116d324b94eaacb756) Included native libraries in the litiengine jar

#### 🔧 utiLITI Editor

* [#409](https://github.com/gurkenlabs/litiengine/pull/409) UI updates. (contributed by [@weisJ](https://github.com/weisJ))
* [49a299e](https://github.com/gurkenlabs/litiengine/commit/49a299e4e2c21653c171648db517e20e77a6e008) Changed visibility of GuiComponent.getCurrentAppearance() to public. Made text align, antialiasing, and shadows available as GuiProperties.
* [b802ae7](https://github.com/gurkenlabs/litiengine/commit/b802ae7e90b2983fdf088d4329869d9816022767), [#420](https://github.com/gurkenlabs/litiengine/pull/420) Resource panel improvements. (contributed by [@jdeblander](https://github.com/jdeblander))
* [52d100c](https://github.com/gurkenlabs/litiengine/commit/52d100c5a765db2b9d5468b21098d159963739d7) Fixed creature sprite names in CreaturePanel
* [f052c5d](https://github.com/gurkenlabs/litiengine/commit/f052c5dcf25a6a938c4ab061404eea6777ebe0f4) Fixed issue that prevented utiLITI from shutting down properly
* [#387](https://github.com/gurkenlabs/litiengine/pull/387), [#391](https://github.com/gurkenlabs/litiengine/pull/391), [#395](https://github.com/gurkenlabs/litiengine/pull/395), [#399](https://github.com/gurkenlabs/litiengine/pull/399) Enhanced crash handling and added debug functionality. (contributed by [@Gamebuster19901](https://github.com/Gamebuster19901))
* [73d9fa1](https://github.com/gurkenlabs/litiengine/commit/73d9fa14194d439d58fff5f984c608b61523b8b6) Added some basic sanity checks around editing emitters
* [a1571c1](https://github.com/gurkenlabs/litiengine/commit/a1571c1cfffbc946539a0e8d47329f9ad79079d9) Improved `GridRenderer` memory usage  
* [21e56de](https://github.com/gurkenlabs/litiengine/commit/21e56de74be2272e7323383de5b639e4d9cd9e9b) Increased available heap space
* [d299c54](https://github.com/gurkenlabs/litiengine/commit/d299c543a44c49cafcd6bdeeda1509b895a0c18d) Set year in the help menu dynamically
* [61aa52c](https://github.com/gurkenlabs/litiengine/commit/61aa52c158e3688a71f02342d9c151577534eb57) Set panel focus globally to prevent unnecessary UI updates
* [a9be599](https://github.com/gurkenlabs/litiengine/commit/a9be599fbc5315ed6cd284cbc94efeb1733c8fc8) Fixed a potential NullReference
* [ad969f4](https://github.com/gurkenlabs/litiengine/commit/ad969f479aa9c9eb9169f6a9f06bba80ff24b85c) Ensured that the game resource file is saved right after creating a new project
* [be0132e](https://github.com/gurkenlabs/litiengine/commit/be0132e85581af7ca73398c0c61225cf93a6abc1) Ensured that only affected nodes in the entity list get updated when entities change
* [1e7b4ff](https://github.com/gurkenlabs/litiengine/commit/1e7b4ff29380fe6787b899315ca898cc12132b7c) Skipped unnecessary UI updates and data binding
* [f3ce2ca](https://github.com/gurkenlabs/litiengine/commit/f3ce2ca84902123f6da4399caaaa160da80f0090) Prevented UndoManager from updating the same object multiple times
* [8306abd](https://github.com/gurkenlabs/litiengine/commit/8306abdf548cb0ec8006b2b5ad4402fca505f114) Prevented entity list from completely rebuilding upon entity deletion

#### 👩‍💻 New Contributors 👨‍💻

* @DanielH4 in [#376](https://github.com/gurkenlabs/litiengine/pull/376)
* @nwessman in [#377](https://github.com/gurkenlabs/litiengine/pull/377)
* @jluech in [#381](https://github.com/gurkenlabs/litiengine/pull/381)
* @ddreimane in [#383](https://github.com/gurkenlabs/litiengine/pull/383)
* @EagleoutIce in [#394](https://github.com/gurkenlabs/litiengine/pull/394)
* @niels89 in [#396](https://github.com/gurkenlabs/litiengine/pull/396)

#### 💵 New Sponsors

* [RajBet](https://raj.bet/) (Bronze sponsorship on OpenCollective)
* [Trust My Paper](https://www.trustmypaper.com/) (Bronze sponsorship on OpenCollective)
* [CasinoHex Canada](https://onlinecasinohex.ca/) (Bronze sponsorship on OpenCollective)
* [ej-technologies](https://www.ej-technologies.com/products/jprofiler/overview.html)  (kindly provided us with a license for their powerful Java profiler `JProfiler`.)

## v0.5.1-beta - "No more Netcode"

![LITIENGINE v0.5.1-beta featureimage](https://litiengine.com/wp-content/uploads/2021/02/litiengine-changelog-featureimage-v0.5.1.png)

This release brings tons of bugfixes and quality-of-life improvements. Feature-wise, the highlight of this version is the addition of a [Tweening framework](https://github.com/gurkenlabs/litiengine/pull/352) that lets you interpolate values over time, e.g. to let your `GuiComponents` bounce or your `Entities` wiggle.
As the engine's networking code had been an unmaintained, untested, and even unsafe mess, we have decided to [remove the networking package entirely](https://github.com/gurkenlabs/litiengine/pull/368).

Our [Discord server](https://discord.gg/T8hVpun) has seen some upgrades and we gladly welcome our first community moderator, [Conifer](https://forum.litiengine.com/u/Conifer)! In order to give back some of your love, we have introduced some special roles for our forum and the Discord server:

* @Supporter : Members that have supported us with donations.
* @Contributor : Members that have contributed to our open source code repositories
* @Early Bird : Members that have been part of our community since the Alpha days of LITIENGINE.

We try to assign these roles to the best of our knowledge, but if we forgot you - please don't hesitate to complain. :)

Apart from that, we've updated the sponsoring tiers in [the LITIENGINE Open Collective](https://opencollective.com/litiengine), allowing you to support our work financially and with full transparency. We have also started a [spreadshirt shop](https://shop.spreadshirt.co.uk/gurkenlabs/) where you can buy all kinds of LITIENGINE related swag and promote the cause (feel free to suggest additional motives)!

As always, huge thanks to all contributors and fans! This is an exciting journey for us and we are grateful to share it with you.

#### ✅ Fixes 

* [5bce248](https://github.com/gurkenlabs/litiengine/commit/5bce24853eab3f233e809b47ec4cbe5279776b8f) Fixed unsupported Javadoc tags
* [ab5529a](https://github.com/gurkenlabs/litiengine/commit/ab5529a4478c1430b3a87b87cd22f7899c4ebb7e) Fixed keyframe durations for automatically flipped animations in `CreatureAnimationControllers`
* [1ca3997](https://github.com/gurkenlabs/litiengine/commit/1ca39971c4f9032949a5afb641ef1f736c4180c4) Fixed flickering particle opacity when fading
* [9a5c829](https://github.com/gurkenlabs/litiengine/commit/9a5c829b6fea6e3b985624d613058f65a339cc85) Fixed ImageComponent image scaling
* [0d4cbec](https://github.com/gurkenlabs/litiengine/commit/0d4cbec4b3906d5a15fdde44a2325968a0236163) Fixed `URLAdapter` initialization in `XmlUtilities` 
* [71aa62d](https://github.com/gurkenlabs/litiengine/commit/71aa62d8d641f332ba412589f6c5629df9c82158) Fixed `ImageLayer` rendering for unbound maps
* [eddb149](https://github.com/gurkenlabs/litiengine/commit/eddb14905889a4ae263dd334a3b63aa40a995b9d) Added a collision box update right after unmarshalling `CollisionEntities`
* [#355](https://github.com/gurkenlabs/litiengine/pull/355) Fixed diagonal Entity movement speed
* [f2bfbbb](https://github.com/gurkenlabs/litiengine/commit/f2bfbbb67e1c8cf501836937a81094e70a30a93d) Fixed Text alignment for `GuiComponents` with text outlines
* [#365](https://github.com/gurkenlabs/litiengine/pull/365) Fixed threading issue with Swing tests 
* [10673e2](https://github.com/gurkenlabs/litiengine/commit/10673e2be1637793fbb7e4dd2b940544a8c1aa9b) Fixed vertical alignment for `GuiComponent` text with outlines
* [63fb8cf](https://github.com/gurkenlabs/litiengine/commit/63fb8cf16c68f3f4cf9d1a2640471b66b17503e4) Fixed issue where `CombatEntityListeners` would not fire hit and death events
* [#367](https://github.com/gurkenlabs/litiengine/pull/367) Improved precision of rotation angle calculations
* [21a7171](https://github.com/gurkenlabs/litiengine/commit/21a71711a38076042ebfddb793a55db7655daaf1) Fixed the first `Animation` frame being skipped
* [4512029](https://github.com/gurkenlabs/litiengine/commit/4512029232bd20112351dcb6b202fec245033843) Ensured that the first `Animation` in an `AnimationController` is used as default
* [a29e62d](https://github.com/gurkenlabs/litiengine/commit/a29e62d04594c5c6cf9dee9c733fea7f4580649e) Ensured that the `PhysicsEngine` is cleared when the game world is cleared
* [94acb5b](https://github.com/gurkenlabs/litiengine/commit/94acb5b5a830e91b9129b317995e58d98ca3569c) Fixed threading issue when drawing maps
* [07eec17](https://github.com/gurkenlabs/litiengine/commit/07eec170806d496624e40d98f1097c9c10fbdb96) Fixed a long-standing shape rendering issue ([#275](https://github.com/gurkenlabs/litiengine/pull/275))

#### ⭐ Features/Improvements

* [1296cfa](https://github.com/gurkenlabs/litiengine/commit/1296cfa13cd54313a7bddd5fdefd608d22357b18) Enabled single-value ParticleParameter initialization
* [2840217](https://github.com/gurkenlabs/litiengine/commit/28402172ee2ff7c95f54c753de0ca8d8ae3076cd) Implemented `SoundSource` entities. Added individual falloff ranges for `SFXPlaybacks`
* [973d78a](https://github.com/gurkenlabs/litiengine/commit/973d78a586c6543d938dc9fb2d45af8bbc9c7f55) Added individual volume modifiers for `SFXPlaybacks`
* [ec49e60](https://github.com/gurkenlabs/litiengine/commit/ec49e60c0cb76280def0b2627bbb3f4a41b9b30b) Added CopyConstructor for `Tiles`
* [#352](https://github.com/gurkenlabs/litiengine/pull/352) Added Tweening framework
* [3e604fc](https://github.com/gurkenlabs/litiengine/commit/3e604fcc3b9a443c8de404bc811e91cc830ea3de) Enabled automatic font resizing when resizing `GuiComponents`
* [9a5c829](https://github.com/gurkenlabs/litiengine/commit/9a5c829b6fea6e3b985624d613058f65a339cc85) Enabled setting rowHeight and columnWidth in  `ImageComponentList` externally
* [c6fb37b](https://github.com/gurkenlabs/litiengine/commit/c6fb37b34eac26d0543cb8c20eea514844f00b4c) Enabled automatically attaching / detaching `IEntityControllers` to the Game loop when adding / removing.
* [57d0394](https://github.com/gurkenlabs/litiengine/commit/57d0394d0d5133d04baf46fc98d73cc6cb0bc08d) Added reflection helper method to recursively retrieve methods.
* [2a0e41d](https://github.com/gurkenlabs/litiengine/commit/2a0e41d8a8254c470d5f1f78d8e34225f38eadad) Added possibility to extend `MapObject` unmarshalling behaviour
* [b721dc9](https://github.com/gurkenlabs/litiengine/commit/b721dc9920a8d0ffaa42d23edf00f73f762d7278) Check inheritance by default when retrieving fields via reflection
* [c9076fd](https://github.com/gurkenlabs/litiengine/commit/c9076fd14eaaf4274c38b7d6fea73023bb58c9d3) Enabled getting gamepads by index
* [75a3ff0](https://github.com/gurkenlabs/litiengine/commit/75a3ff004da1e30446a9e99e672a7e53dcaeb7e6) Added method overload for modifying `Attribute` values
* [5e0fe1d](https://github.com/gurkenlabs/litiengine/commit/5e0fe1d12d7ed1eb19cb52249d3fa98c2f01c312) [2e042e7](https://github.com/gurkenlabs/litiengine/commit/2e042e70e7a4100fe9ff30f8bc7b962e1c34443d) Added event listeners for `Animation` keyframes
* [#357](https://github.com/gurkenlabs/litiengine/pull/357) Added Tests for Attribute, RangeAttribute and AttributeModifier
* [fc42199](https://github.com/gurkenlabs/litiengine/commit/fc42199a3d03337ae378db2e791fbe092e1a548b) Added optional automatic line breaks to `GuiComponents`
* [0f39631](https://github.com/gurkenlabs/litiengine/commit/0f39631850817b98d5c8efd8dded059965618491) Added Image scaling and alignment defaults to `ImageComponents`
* [bf8087f](https://github.com/gurkenlabs/litiengine/commit/bf8087f009be41af99dcb38338a554c51613b50d) Added shortcuts to distinguish left/right mouse click events
* [2afebd4](https://github.com/gurkenlabs/litiengine/commit/2afebd470220e638c3ec6175d2e6a21c3dca6566) Added `Material` support for setting values via reflection
* [a319301](https://github.com/gurkenlabs/litiengine/commit/a319301266ea6fba040f0d5d1708d59b088cd579) Cache `AnimationController` instance on `Entities`
* [63fb8cf](https://github.com/gurkenlabs/litiengine/commit/63fb8cf16c68f3f4cf9d1a2640471b66b17503e4) Added resurrection listener for `CombatEntities`
* [853eefd](https://github.com/gurkenlabs/litiengine/commit/853eefd49768ba522ef644e77438764310333354) Added time attribute to hit events
* [38d9238](https://github.com/gurkenlabs/litiengine/commit/38d9238da8dc30771fa01ddcbfa17319ee706877) Added fading and anti aliasing for `TextParticles`
* [bad4b34](https://github.com/gurkenlabs/litiengine/commit/bad4b342be7ee552f5f927bbea3880377bb42407) Extended environment API to get entities by tag.
* [10298b0](https://github.com/gurkenlabs/litiengine/commit/10298b0bcc3b71e809190527a637e1b083ac3dee) Unified game shutdowns
* [7df8c11](https://github.com/gurkenlabs/litiengine/commit/7df8c11a01ad8362bef2354abe30ecf4045b7de7) Improved `GameMetrics` java version output 

#### 🔀 Changes

* [9775b9c](https://github.com/gurkenlabs/litiengine/commit/9775b9c85c720d821d339519aa411da5fdf7f4e9) Set Trigger collision box size implicitly
* [1ca3997](https://github.com/gurkenlabs/litiengine/commit/1ca39971c4f9032949a5afb641ef1f736c4180c4) Removed distinction between particle color alpha and opacity
* [3b88928](https://github.com/gurkenlabs/litiengine/commit/3b889282091be009a675f8964292d2d24390f774) Made `VolumeControl` public
* [cdaa903](https://github.com/gurkenlabs/litiengine/commit/cdaa903506ff90e0889175610d55c39b2785c2f0) and others: Enforce capitalization of the LITIENGINE brand.
* [c9076fd](https://github.com/gurkenlabs/litiengine/commit/c9076fd14eaaf4274c38b7d6fea73023bb58c9d3) Renamed gamepad index to id to better reflect its purpose
* [#355](https://github.com/gurkenlabs/litiengine/pull/355) Merged the `InputLoop` into the `GameLoop`. The `SoundEngine` will now also be updated by the `GameLoop`.
* [7a5a553](https://github.com/gurkenlabs/litiengine/commit/7a5a553de3f5cdc5e05aaa37be671b9a61405d59) [5a5b666](https://github.com/gurkenlabs/litiengine/commit/5a5b666fa0efc9f0494d8f37a52a18917b7b64b1) [a36cce6](https://github.com/gurkenlabs/litiengine/commit/a36cce602ff3eb5e5227544521678f8382bd2ac8) Made `MovementController` velocity and angle available publicly
* [0da9f5a](https://github.com/gurkenlabs/litiengine/commit/0da9f5a7afe3909cc507a0027fd658b329da77e9) [fde640a](https://github.com/gurkenlabs/litiengine/commit/fde640a3d9e3f8d949a1b8fe92ef39745462f407) Centered `Ability` impact area
* [649ceea](https://github.com/gurkenlabs/litiengine/commit/649ceeacc6c164314cfc900ad734ebda0bd5ba12) Made retrieving flipped `Animations` from `AnimationControllers` available as a static method
* [179f192](https://github.com/gurkenlabs/litiengine/commit/179f192f76689c54789c19215a73dc8a35f9c7a9) Pulled `GuiComponent` text anti aliasing out of the `Appearance`
* [c68821f](https://github.com/gurkenlabs/litiengine/commit/c68821f64b7c8c7e8b56d6bc5d1bf67d25b73c67) [f4a2233](https://github.com/gurkenlabs/litiengine/commit/f4a22335de266462035d8fdd6e28b4899cf9e793) Changed tag serialization behaviour
* [63fb8cf](https://github.com/gurkenlabs/litiengine/commit/63fb8cf16c68f3f4cf9d1a2640471b66b17503e4) Renamed instances of `removeChangedListener` to `removeListener`
* [366ed6b](https://github.com/gurkenlabs/litiengine/commit/366ed6be63a4e806cde71c871d04611a0f400968) Don't set custom `RenderType` for all `Particle` instances.
* [33d588b](https://github.com/gurkenlabs/litiengine/commit/33d588b4c1ffe8b4d628816e6a2806a3f6647097) Made `Effect` target evaluations protected
* [c7c1deb](https://github.com/gurkenlabs/litiengine/commit/c7c1deb59fcaa9a52a20cafea493913f1b52eaea) Made `Ability` effects available publicly
* [#368](https://github.com/gurkenlabs/litiengine/pull/368) Removed the networking package
* [c8288e5](https://github.com/gurkenlabs/litiengine/commit/c8288e5e8bfd216318afbdc591fd795f93d3b48e) Set moved events on `Creatures` to be fired implicitly

#### 🔧 utiLITI Editor
* [6ba6af3](https://github.com/gurkenlabs/litiengine/commit/6ba6af3885f9de3207ac54dd53b018181a666172) [269a495](https://github.com/gurkenlabs/litiengine/commit/269a495490215029adb943174875aeaeaadb3630) Bumped Darklaf version
* [#362](https://github.com/gurkenlabs/litiengine/pull/) Added "clear" and "scroll to bottom" buttons to console view
* [66b4051](https://github.com/gurkenlabs/litiengine/commit/66b405163302491702701935f4b35dbf7be45df8) Fixed Mouse Wheel scrolling bug
* [b6c5e58](https://github.com/gurkenlabs/litiengine/commit/b6c5e58f0fc78c251c7820fdb4b0d42343c60730) Bumped JUnit version
* [912ecd2](https://github.com/gurkenlabs/litiengine/commit/912ecd2a13dd88fe1d745b542d67039e7c9c73f2) Improved map id rendering
* [a87fee9](https://github.com/gurkenlabs/litiengine/commit/a87fee99c85cc9f94e596efde9c5843f8e184471) Removed redundant lighting updates when setting control values
* [4e909ac](https://github.com/gurkenlabs/litiengine/commit/4e909ac602e209e292b139d5ae068b1bd10cce06) Changed MapObject refresh behaviour for undoing / redoing operations
* [cf79b6e](https://github.com/gurkenlabs/litiengine/commit/cf79b6efda29c3eb58c80193fc89dea1870d52bb) [c9146ed](https://github.com/gurkenlabs/litiengine/commit/c9146edb2583013fd13609ee8d8bf3cf66bd4a39) Adjusted threading behaviour for arrow key presses
* [10298b0](https://github.com/gurkenlabs/litiengine/commit/10298b0bcc3b71e809190527a637e1b083ac3dee) Made `GridRenderer` more robust when no camera is set.
* [54b8163](https://github.com/gurkenlabs/litiengine/commit/54b8163752416bea417d9441d1f31cde81784793) Improved tag visualizations
* [09d7a0e](https://github.com/gurkenlabs/litiengine/commit/09d7a0e463253ea5274de3d7a9782578b9a15540) Fixed issue where the wrong Tree nodes in `EntityList` would be focused
* [d3dfd67](https://github.com/gurkenlabs/litiengine/commit/d3dfd67fff713edcd105e3001f643f3c8b3b4167) Improved `GridRenderer` performance
* [0905394](https://github.com/gurkenlabs/litiengine/commit/0905394c05e1308a611f2ff22bac453d218deb84) Ensured that the grid cache is cleared when deleting and importing maps
* [49708b4](https://github.com/gurkenlabs/litiengine/commit/49708b4a0c9723e7eac1cf724a7cb0163e971845) Improved focus renderer
* [34b183f](https://github.com/gurkenlabs/litiengine/commit/34b183f0db46ab005cb21fcaf3ade3d03f2a7963) Ensured there is enough space for all components in the spritesheet import panel

#### 💬 Misc
* The [LITIENGINE Open Collective](https://opencollective.com/litiengine) now lets you support our work financially. A warm welcome to our first sponsors!
* [193bde3](https://github.com/gurkenlabs/litiengine/commit/193bde390631c243406def95f530fcb5190f01c6) Updated readme banner to be visible in both light and dark GitHub themes.
* [37ca653](https://github.com/gurkenlabs/litiengine/commit/37ca6532fc5cccd55ae9bc251031cb923357081b) Arrived in the year 2021
* [1d6a691](https://github.com/gurkenlabs/litiengine/commit/1d6a69176d00eeaf4acd22178f49b37270458722) Bumped Gradle wrapper version
* [ddc1caf](https://github.com/gurkenlabs/litiengine/commit/ddc1cafed9db40801e0f886e7f5c822be45dc5b3) (and others): Removed redundant modifiers from interfaces
* [0af1561](https://github.com/gurkenlabs/litiengine/commit/0af15618018744f7c9d832fe98a7e91210b465a1) Added Java version to bug report template

 


## v0.5.0-beta - "Farewell, Alpha!" 
![LITIENGINE v0.5.0-beta featureimage](https://litiengine.com/wp-content/uploads/2020/08/litiengine-changelog-featureimage-v0.5.0.png)

This release marks the beginning of a new era for the LITIENGINE. We consider most of the API to be stable and we pretty much settled on the current API design.
With the release of our new Website, the documentation and other information about the engine are easier to use and everything can be found in one place.

It's been a long journey but, finally, we're leaving the Alpha status and are looking forward to even more fruitful experiences with the LITIENGINE in the future.
A big thank you to all members of this community. Without your feedback and contributions we wouldn't be here today. You're awesome! 

#### ✅ Fixes 
 * [00178dd](https://github.com/gurkenlabs/litiengine/commit/00178dd052d21a5aab3c237c4849161614f89645) Fixed NullPointerException when rendering Shapes
 * [00178dd](https://github.com/gurkenlabs/litiengine/commit/00178dd052d21a5aab3c237c4849161614f89645) Fixed vertical position when rendering Text with Alignment.
 * [2c55195](https://github.com/gurkenlabs/litiengine/commit/2c5519506f858fe13432fb91b529a680c41d19f4) Fixed NullPointerException when setting opacity on an image.
 * [7c46a6f](https://github.com/gurkenlabs/litiengine/commit/7c46a6f20039d09bb12a51283b45321b0d477975) Fixed issue with collision dimension <= 0
 * [0deffc4](https://github.com/gurkenlabs/litiengine/commit/0deffc4bf72f14afbf02333d93a8222595513497) Zoom changed event is now fired after changing the zoom
 * [eb1ca1e](https://github.com/gurkenlabs/litiengine/commit/eb1ca1e8bf386c18f74d6d89ec0280b44a5cdd8f) Fixed issue with "stuttering" `PositionLockCamera`
 * [afe8639](https://github.com/gurkenlabs/litiengine/commit/afe863922ad3b9e45cc9e9f3048034cdc2dff577) Fixed `EntityEmitters` to update their position correctly once the corresponding entity moves.

#### ⭐ Features/Improvements
 * [3455fa6](https://github.com/gurkenlabs/litiengine/commit/3455fa6b1b98ccc4cd8e6fbd15ed34f273776937) Make TileData constructor visibility being non public.
 * [1c9642a](https://github.com/gurkenlabs/litiengine/commit/1c9642a1caf97571a7f852d51a04ba516614a48f) Allow comma separated parameters for random methods.
 * [#139](https://github.com/gurkenlabs/litiengine/issues/139) Add API that supports generating maps from code
 * [#332](https://github.com/gurkenlabs/litiengine/pull/332) Improved `GeometricUtilities`
 * [14eb43c](https://github.com/gurkenlabs/litiengine/commit/14eb43cc4f100306d0eb24e40c084568621dbaa6) Extended `Game.random()` API with support for choosing a random string
 * [8d3f564](https://github.com/gurkenlabs/litiengine/commit/8d3f564407f8bd7aa51d12d32be64af3a0262e0a) Extended `Environment` with the possibility to retrieve entities by a specified `Predicate`
 * [e756f53](https://github.com/gurkenlabs/litiengine/commit/e756f530138898a4b33dfb37435766e7751102f5) Extended `SoundEffect` with the possibility to provide sounds by name
 * [6da1d94](https://github.com/gurkenlabs/litiengine/commit/6da1d94a110024a870c5311e55a306f58a6ce969) Trigger entity moved event from the `EntityNavigator`
 * [c09c1ca](https://github.com/gurkenlabs/litiengine/commit/c09c1cab3c07b7b6e45d92255424fcce15066aa0) Extended the `TextRenderer` with several new method overloads
 * [714dd6e](https://github.com/gurkenlabs/litiengine/commit/714dd6e5659f1b92b5c3de93ca9577a51913568d) Extended `TilesetEntry` with support for collision info


#### 🔀 Changes
 * [7909f05](https://github.com/gurkenlabs/litiengine/commit/7909f057e8aa010b49e14727f4624ec4712cc8e9) Adjusted the handling of the anim controller affine transform
 * [30093d7](https://github.com/gurkenlabs/litiengine/commit/30093d701e2b7dd2ebb73e91bbfb6203661e565b) Renamed events to suit the naming conventions
 * [#336](https://github.com/gurkenlabs/litiengine/issues/336) Fixed inconsistent Entity Hierarchy by removing `MobileEntity`
 * [bfa2d98](https://github.com/gurkenlabs/litiengine/commit/bfa2d98bf4240ed649e1ea7908a7ee8b73bfb11a) Make the local ID sequence unique globally (over all `Environments`)


#### 🔧 utiLITI Editor
 * [06b8d0e](https://github.com/gurkenlabs/litiengine/commit/06b8d0eae82569a64869ca8b6c8e25c4c675608f) Improved scrollbar granularity
 * [24cd048](https://github.com/gurkenlabs/litiengine/commit/24cd048ed9a9f2dd9cece9c21d27b654b5a17a18) Added Spawnpoint pivot fields to the editor
 * [3af2988](https://github.com/gurkenlabs/litiengine/commit/3af298878fe8e66287f0ab80338a1458ad013470) Fixed potential exception when removing custom properties
 * [#312](https://github.com/gurkenlabs/litiengine/issues/312) Added a Zoom Combobox
 * [a5436f3](https://github.com/gurkenlabs/litiengine/commit/a5436f312d4303798430f18bb61efa3ae6b6d756) Fixed capitalization on many UI strings
 * [b20fbdd](https://github.com/gurkenlabs/litiengine/commit/b20fbdd41d3a3c9d3ae48aac0f49415474bbefea) Added support for custom properties for `MapArea`
 * [18a7735](https://github.com/gurkenlabs/litiengine/commit/18a7735cd4690eae3f040b430abe8d931bf98a37) Clear map list when opening another game project
 * [160e563](https://github.com/gurkenlabs/litiengine/commit/160e5634e2698913726da5253e92fcc3b1996682) Added right-click shortcut menu to the map list

##### Added Dark Theme and overhauled Light Theme [#340](https://github.com/gurkenlabs/litiengine/pull/340)

With this version, we've introduced theming support for the utiLITI editor with the [DarkLaf](https://github.com/weisJ/darklaf) library.
The theme can be switch at runtime 

**Dark Theme utiLITI**
![utiLITI: Dark Theme](images/darktheme.png)

**Light Theme utiLITI**
![utiLITI: Light Theme](images/lighttheme.png)

##### Revamped the Emitter UI (make it actually usable)

With this version, we revamped the `Emitter` UI in the utiLITI editor such that changes to the emitter are instantly applied. The different parameters have been categorized and the overall usability has been drastically improved.
In addition, we've also added the possibility to configure particle rotation for even more vivid visual effects.

See the related implementations on GitHub:
[#346](https://github.com/gurkenlabs/litiengine/pull/346) [#298](https://github.com/gurkenlabs/litiengine/issues/298) [#345](https://github.com/gurkenlabs/litiengine/issues/345)

![Example: Emitter Panel overhaul](images/emitterpanel.gif)

#### 💬 Misc
 * Added PR templates
 * Added issue templates
