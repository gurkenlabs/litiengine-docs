---
meta.description: Release notes for the LITIENGINE that include a complete changelog with all fixes, changes, improvements and a list of added and removed features.
meta.keywords: FAQ, questions, LITIENGINE, java, game, gameengine, development, 2D, programming
---


# LITIENGINE Release notes

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