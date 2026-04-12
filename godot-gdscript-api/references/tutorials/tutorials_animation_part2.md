# Godot 4 GDScript Tutorials — Animation (Part 2)

> 3 tutorials. GDScript-specific code examples.

## Cutout animation

> **Work in progress:** The content of this page was not yet updated for Godot `4.6` and may be **outdated**. If you know how to improve this page or you can confirm that it's up to date, feel free to [open a pull request](https://github.com/godotengine/godot-docs).

### What is it?

Traditionally, [cutout animation](https://en.wikipedia.org/wiki/Cutout_animation) is a type of [stop motion animation](https://en.wikipedia.org/wiki/Stop_motion) in which pieces of paper (or other thin material) are cut into special shapes and arranged in two-dimensional representations of characters and objects. Characters' bodies are usually made out of several pieces. The pieces are arranged and photographed once for each frame of the film. The animator moves and rotates the parts in small increments between each shot to create the illusion of movement when the images are played back quickly in sequence.

Simulations of cutout animation can now be created using software as seen in [South Park](https://en.wikipedia.org/wiki/South_Park) and [Jake and the Never Land Pirates](https://en.wikipedia.org/wiki/Jake_and_the_Never_Land_Pirates).

In video games, this technique has also become popular. Examples of this are [Paper Mario](https://en.wikipedia.org/wiki/Super_Paper_Mario) or [Rayman Origins](https://en.wikipedia.org/wiki/Rayman_Origins) .

### Cutout animation in Godot

Godot provides tools for working with cutout rigs, and is ideal for the workflow:

- **The animation system is fully integrated with the engine**: This means animations can control much more than just motion of objects. Textures, sprite sizes, pivots, opacity, color modulation, and more, can all be animated and blended.
- **Combine animation styles**: AnimatedSprite2D allows traditional cel animation to be used alongside cutout animation. In cel animation different animation frames use entirely different drawings rather than the same pieces positioned differently. In an otherwise cutout-based animation, cel animation can be used selectively for complex parts such as hands, feet, changing facial expressions, etc.
- **Custom Shaped Elements**: Custom shapes can be created with [Polygon2D](../godot_gdscript_nodes_2d.md) allowing UV animation, deformations, etc.
- **Particle Systems**: A cutout animation rig can be combined with particle systems. This can be useful for magic effects, jetpacks, etc.
- **Custom Colliders**: Set colliders and influence areas in different parts of the skeletons, great for bosses and fighting games.
- **Animation Tree**: Allows complex combinations and blending between several animations, the same way it works in 3D.

And much more!

### Making of GBot

For this tutorial, we will use as demo content the pieces of the [GBot](https://www.youtube.com/watch?v=S13FrWuBMx4&list=UUckpus81gNin1aV8WSffRKw) character, created by Andreas Esau.

Get your assets: [cutout_animation_assets.zip](https://github.com/godotengine/godot-docs-project-starters/releases/download/latest-4.x/cutout_animation_assets.zip).

### Setting up the rig

Create an empty Node2D as root of the scene, we will work under it:

The first node of the model is the hip. Generally, both in 2D and 3D, the hip is the root of the skeleton. This makes it easier to animate:

Next will be the torso. The torso needs to be a child of the hip, so create a child sprite and load the torso texture, later accommodate it properly:

This looks good. Let's see if our hierarchy works as a skeleton by rotating the torso. We can do this be pressing E to enter rotate mode, and dragging with the left mouse button. To exit rotate mode hit ESC.

The rotation pivot is wrong and needs to be adjusted.

This small cross in the middle of the [Sprite2D](../godot_gdscript_nodes_2d.md) is the rotation pivot:

### Adjusting the pivot

The pivot can be adjusted by changing the _offset_ property in the Sprite2D:

The pivot can also be adjusted _visually_. While hovering over the desired pivot point, press V to move the pivot there for the selected Sprite2D. There is also a tool in the tool bar that has a similar function.

Continue adding body pieces, starting with the right arm. Make sure to put each sprite in its correct place in the hierarchy, so its rotations and translations are relative to its parent:

With the left arm there's a problem. In 2D, child nodes appear in front of their parents:

We want the left arm to appear _behind_ the hip and the torso. We could move the left arm nodes behind the hip (above the hip node in the scene hierarchy), but then the left arm is no longer in its proper place in the hierarchy. This means it wouldn't be affected by the movement of the torso. We'll fix this problem with `RemoteTransform2D` nodes.

> **Note:** You can also fix depth ordering problems by adjusting the Z property of any node inheriting from Node2D.

### RemoteTransform2D node

The [RemoteTransform2D](../godot_gdscript_nodes_2d.md) node transforms nodes somewhere else in the hierarchy. This node applies its own transform (including any transformation it inherits from its parents) to the remote node it targets.

This allows us to correct the visibility order of our elements, independently of the locations of those parts in the cutout hierarchy.

Create a `RemoteTransform2D` node as a child of the torso. Call it `remote_arm_l`. Create another RemoteTransform2D node inside the first and call it `remote_hand_l`. Use the `Remote Path` property of the two new nodes to target the `arm_l` and `hand_l` sprites respectively:

Moving the `RemoteTransform2D` nodes now moves the sprites. So we can create animations by adjusting the `RemoteTransform2D` transforms:

### Completing the skeleton

Complete the skeleton by following the same steps for the rest of the parts. The resulting scene should look similar to this:

The resulting rig will be easy to animate. By selecting the nodes and rotating them you can animate forward kinematics (FK) efficiently.

For simple objects and rigs this is fine, but there are limitations:

- Selecting sprites in the main viewport can become difficult in complex rigs. The scene tree ends up being used to select parts instead, which can be slower.
- Inverse Kinematics (IK) is useful for animating extremities like hands and feet, and can't be used with our rig in its current state.

To solve these problems we'll use Godot's skeletons.

### Skeletons

In Godot there is a helper to create "bones" between nodes. The bone-linked nodes are called skeletons.

As an example, let's turn the right arm into a skeleton. To create a skeleton, a chain of nodes must be selected from top to bottom:

Then, click on the Skeleton menu and select `Make Bones`.

This will add bones covering the arm, but the result may be surprising.

Why does the hand lack a bone? In Godot, a bone connects a node with its parent. And there's currently no child of the hand node. With this knowledge let's try again.

The first step is creating an endpoint node. Any kind of node will do, but [Marker2D](../godot_gdscript_nodes_2d.md) is preferred because it's visible in the editor. The endpoint node will ensure that the last bone has orientation.

Now select the whole chain, from the endpoint to the arm and create bones:

The result resembles a skeleton a lot more, and now the arm and forearm can be selected and animated.

Create endpoints for all important extremities. Generate bones for all articulable parts of the cutout, with the hip as the ultimate connection between all of them.

You may notice that an extra bone is created when connecting the hip and torso. Godot has connected the hip node to the scene root with a bone, and we don't want that. To fix this, select the root and hip node, open the Skeleton menu, click `clear bones`.

Your final skeleton should look something like this:

You might have noticed a second set of endpoints in the hands. This will make sense soon.

Now that the whole figure is rigged, the next step is setting up the IK chains. IK chains allow for more natural control of extremities.

### IK chains

IK stands for inverse kinematics. It's a convenient technique for animating the position of hands, feet and other extremities of rigs like the one we've made. Imagine you want to pose a character's foot in a specific position on the ground. Without IK chains, each motion of the foot would require rotating and positioning several other bones (the shin and the thigh at least). This would be quite complex and lead to imprecise results. IK allows us to move the foot directly while the shin and thigh self-adjust.

> **Note:** **IK chains in Godot currently work in the editor only**, not at runtime. They are intended to ease the process of setting keyframes, and are not currently useful for techniques like procedural animation.

To create an IK chain, select a chain of bones from endpoint to the base for the chain. For example, to create an IK chain for the right leg, select the following:

Then enable this chain for IK. Go to Edit > Make IK Chain.

As a result, the base of the chain will turn _Yellow_.

Once the IK chain is set up, grab any child or grand-child of the base of the chain (e.g. a foot), and move it. You'll see the rest of the chain adjust as you adjust its position.

### Animation tips

The following section will be a collection of tips for creating animation for your cutout rigs. For more information on how the animation system in Godot works, see Introduction to the animation features.

#### Setting keyframes and excluding properties

Special contextual elements appear in the top toolbar when the animation editor window is open:

The key button inserts location, rotation, and scale keyframes for the selected objects or bones at the current playhead position.

The "loc", "rot", and "scl" toggle buttons to the left of the key button modify its function, allowing you to specify which of the three properties keyframes will be created for.

Here's an illustration of how this can be useful: Imagine you have a node which already has two keyframes animating its scale only. You want to add an overlapping rotation movement to the same node. The rotation movement should begin and end at different times from the scale change that's already set up. You can use the toggle buttons to have only rotation information added when you add a new keyframe. This way, you can avoid adding unwanted scale keyframes which would disrupt the existing scale animation.

### Creating a rest pose

Think of a rest pose as a default pose that your cutout rig should be set to when no other pose is active in your game. Create a rest pose as follows:

1. Make sure the rig parts are positioned in what looks like a "resting" arrangement.

1. Create a new animation, rename it "rest".
1. Select all nodes in your rig (box selection should work fine).

1. Make sure the "loc", "rot", and "scl" toggle buttons are all active in the toolbar.

1. Press the key button. Keys will be inserted for all selected parts storing their current arrangement. This pose can now be recalled when necessary in your game by playing the "rest" animation you've created.

### Modifying rotation only

When animating a cutout rig, often it's only the rotation of the nodes that needs to change. Location and scale are rarely used.

So when inserting keys, you might find it convenient to have only the "rot" toggle active most of the time:

This will avoid the creation of unwanted animation tracks for position and scale.

### Keyframing IK chains

When editing IK chains, it's not necessary to select the whole chain to add keyframes. Selecting the endpoint of the chain and inserting a keyframe will automatically insert keyframes for all other parts of the chain too.

### Visually move a sprite behind its parent

Sometimes it is necessary to have a node change its visual depth relative to its parent node during an animation. Think of a character facing the camera, who pulls something out from behind his back and holds it out in front of him. During this animation the whole arm and the object in his hand would need to change their visual depth relative to the body of the character.

To help with this there's a keyframable "Behind Parent" property on all Node2D-inheriting nodes. When planning your rig, think about the movements it will need to perform and give some thought to how you'll use "Behind Parent" and/or RemoteTransform2D nodes. They provide overlapping functionality.

### Setting easing curves for multiple keys

To apply the same easing curve to multiple keyframes at once:

1. Select the relevant keys.
2. Click on the pencil icon in the bottom right of the animation panel. This will open the transition editor.
3. In the transition editor, click on the desired curve to apply it.

### 2D Skeletal deform

Skeletal deform can be used to augment a cutout rig, allowing single pieces to deform organically (e.g. antennae that wobble as an insect character walks).

This process is described in a separate tutorial.

---

## Introduction to the animation features

The [AnimationPlayer](../godot_gdscript_resources.md) node allows you to create anything from simple to complex animations.

In this guide you learn to:

- Work with the Animation Panel
- Animate any property of any node
- Create a simple animation

In Godot, you can animate anything available in the Inspector, such as Node transforms, sprites, UI elements, particles, visibility and color of materials, and so on. You can also modify values of script variables and even call functions.

### Create an AnimationPlayer node

To use the animation tools we first have to create an [AnimationPlayer](../godot_gdscript_resources.md) node.

The AnimationPlayer node type is the data container for your animations. One AnimationPlayer node can hold multiple animations, which can automatically transition to one another.

After you create an AnimationPlayer node, click on it to open the Animation Panel at the bottom of the viewport.

The animation panel consists of four parts:

- Animation controls (i.e. add, load, save, and delete animations)
- The tracks listing
- The timeline with keyframes
- The timeline and track controls, where you can zoom the timeline and edit tracks, for example.

### Computer animation relies on keyframes

A keyframe defines the value of a property at a point in time.

Diamond shapes represent keyframes in the timeline. A line between two keyframes indicates that the value doesn't change between them.

You set values of a node's properties and create animation keyframes for them. When the animation runs, the engine will interpolate the values between the keyframes, resulting in them gradually changing over time.

The timeline defines how long the animation will take. You can insert keyframes at various points, and change their timing.

Each line in the Animation Panel is an animation track that references a Normal or Transform property of a node. Each track stores a path to a node and its affected property. For example, the position track in the illustration refers to the `position` property of the Sprite2D node.

> **Tip:** If you animate the wrong property, you can edit a track's path at any time by double-clicking on it and typing the new path. Play the animation using the "Play from beginning" button (or pressing Shift + D on keyboard) to see the changes instantly.

### Tutorial: Creating a simple animation

#### Scene setup

For this tutorial, we'll create a Sprite node with an AnimationPlayer as its child. We will animate the sprite to move between two points on the screen.

> **Warning:** AnimationPlayer inherits from Node instead of Node2D or Node3D, which means that the child nodes will not inherit the transform from the parent nodes due to a bare Node being present in the hierarchy. Therefore, it is not recommended to add nodes that have a 2D/3D transform as a child of an AnimationPlayer node.

The sprite holds an image texture. For this tutorial, select the Sprite2D node, click Texture in the Inspector, and then click Load. Select the default Godot icon for the sprite's texture.

#### Adding an animation

Select the AnimationPlayer node and click the "Animation" button in the animation editor. From the list, select "New" () to add a new animation. Enter a name for the animation in the dialog box.

#### Managing animation libraries

For reusability, the animation is registered in a list in the animation library resource. If you add an animation to AnimationPlayer without specifying any particular settings, the animation will be registered in the [Global] animation library that AnimationPlayer has by default.

If there are multiple animation libraries and you try to add an animation, a dialog box will appear with options.

#### Adding a track

To add a new track for our sprite, select it and take a look at the toolbar:

These switches and buttons allow you to add keyframes for the selected node's location, rotation, and scale. Since we are only animating the sprite's position, make sure that only the location switch is selected. The selected switches are blue.

Click on the key button to create the first keyframe. Since we don't have a track set up for the Position property yet, Godot will offer to create it for us. Click **Create**.

Godot will create a new track and insert our first keyframe at the beginning of the timeline:

#### The second keyframe

We need to set our sprite's end location and how long it will take for it to get there.

Let's say we want it to take two seconds to move between the points. By default, the animation is set to last only one second, so change the animation length to 2 in the controls on the right side of the animation panel's timeline header.

Now, move the sprite right, to its final position. You can use the _Move tool_ in the toolbar or set the _Position_'s X value in the _Inspector_.

Click on the timeline header near the two-second mark in the animation panel and then click the key button in the toolbar to create the second keyframe.

#### Run the animation

Click on the "Play from beginning" () button.

Yay! Our animation runs:

#### Autoplay on load

You can make it so an animation plays automatically when the AnimationPlayer nodes scene starts, or joins another scene. To do this click the "Autoplay on load" button in the animation editor, it's right next to the edit button.

The icon for it will also appear in front of the name of the animation, so you can easily identify which one is the autoplay animation.

#### Back and forth

Godot has an interesting feature that we can use in animations. When Animation Looping is set but there's no keyframe specified at the end of the animation, the first keyframe is also the last.

This means we can extend the animation length to four seconds now, and Godot will also calculate the frames from the last keyframe to the first, moving our sprite back and forth.

You can change this behavior by changing the track's loop mode. This is covered in the next chapter.

#### Track settings

Each property track has a settings panel at the end, where you can set its update mode, track interpolation, and loop mode.

The update mode of a track tells Godot when to update the property values. This can be:

- **Continuous:** Update the property on each frame
- **Discrete:** Only update the property on keyframes
- **Capture:** if the first keyframe's time is greater than `0.0`, the current value of the property will be remembered and will be blended with the first animation key. For example, you could use the Capture mode to move a node that's located anywhere to a specific location.

You will usually use "Continuous" mode. The other types are used to script complex animations.

Track interpolation tells Godot how to calculate the frame values between keyframes. These interpolation modes are supported:

- Nearest: Set the nearest keyframe value
- Linear: Set the value based on a linear function calculation between the two keyframes
- Cubic: Set the value based on a cubic function calculation between the two keyframes
- Linear Angle (Only appears in rotation property): Linear mode with shortest path rotation
- Cubic Angle (Only appears in rotation property): Cubic mode with shortest path rotation

With Cubic interpolation, animation is slower at keyframes and faster between them, which leads to more natural movement. Cubic interpolation is commonly used for character animation. Linear interpolation animates changes at a fixed pace, resulting in a more robotic effect.

Godot supports two loop modes, which affect the animation when it's set to loop:

- Clamp loop interpolation: When this is selected, the animation stops after the last keyframe for this track. When the first keyframe is reached again, the animation will reset to its values.
- Wrap loop interpolation: When this is selected, Godot calculates the animation after the last keyframe to reach the values of the first keyframe again.

### Keyframes for other properties

Godot's animation system isn't restricted to position, rotation, and scale. You can animate any property.

If you select your sprite while the animation panel is visible, Godot will display a small keyframe button in the _Inspector_ for each of the sprite's properties. Click on one of these buttons to add a track and keyframe to the current animation.

### Edit keyframes

You can click on a keyframe in the animation timeline to display and edit its value in the _Inspector_.

You can also edit the easing value for a keyframe here by clicking and dragging its easing curve. This tells Godot how to interpolate the animated property when it reaches this keyframe.

You can tweak your animations this way until the movement "looks right."

### Using RESET tracks

You can set up a special _RESET_ animation to contain the "default pose". This is used to ensure that the default pose is restored when you save the scene and open it again in the editor.

For existing tracks, you can add an animation called "RESET" (case-sensitive), then add tracks for each property that you want to reset. The only keyframe should be at time 0, and give it the desired default value for each track.

If AnimationPlayer's **Reset On Save** property is set to `true`, the scene will be saved with the effects of the reset animation applied (as if it had been seeked to time `0.0`). This only affects the saved file – the property tracks in the editor stay where they were.

If you want to reset the tracks in the editor, select the AnimationPlayer node, open the **Animation** bottom panel then choose **Apply Reset** in the animation editor's **Edit** dropdown menu.

When using the keyframe icon next to a property in the inspector the editor will ask you to automatically create a RESET track.

> **Note:** RESET tracks are also used as reference values for blending. See also [For better blending](tutorials_animation.md).

### Onion Skinning

Godot's animation editor allows you use onion skinning while creating an animation. To turn this feature on click on the onion icon in the top right of the animation editor. Now there will be transparent red copies of what is being animated in its previous positions in the animation.

The three dots button next to the onion skinning button opens a dropdown menu that lets you adjust how it works, including the ability to use onion skinning for future frames.

### Animation Markers

Animation markers can be used to play a specific part of an animation rather than the whole thing. Here is a use case example, there's an animation file that has a character doing two distinct actions, and the project requires the whole animation, as well as both actions individually. Instead of making two additional animations, markers can be placed on the timeline, and both actions can now be played individually.

To add a marker to an animation right click the space above the timeline and select **Insert Marker...**.

All markers require a unique name within the animation. You can also set the color of the markers for improved organization.

To play the part of the animation between two markers use the [play_section_with_markers()](../godot_gdscript_misc.md) and [play_section_with_markers_backwards()](../godot_gdscript_misc.md) methods. If no start marker is specified then the beginning of the animation is used, and if no end marker is specified, then the end of the animation is used.

If the end marker is after the end of the animation then the `AnimationPlayer` will clamp the end of the section so it does not go past the end of the animation.

To preview the animation between two markers use Shift + Click to select the markers. When two are selected the space between them should be highlighted in red.

Now all of the play animation buttons will act as if the selected area is the whole animation. **Play Animation from Start** will treat the first marker as the start of the animation, **Play Animation Backwards from End** will treat the second marker as the end, and so on.

---

## Playing videos

Godot supports video playback with the [VideoStreamPlayer](../godot_gdscript_ui_controls.md) node.

### Supported playback formats

The only supported format in core is **Ogg Theora** (not to be confused with Ogg Vorbis audio) with optional Ogg Vorbis audio tracks. It's possible for extensions to bring support for additional formats.

H.264 and H.265 cannot be supported in core Godot, as they are both encumbered by software patents. AV1 is royalty-free, but it remains slow to decode on the CPU and hardware decoding support isn't readily available on all GPUs in use yet.

WebM was supported in core in Godot 3.x, but support for it was removed in 4.0 as it was too buggy and difficult to maintain.

> **Note:** You may find videos with a `.ogg` or `.ogx` extensions, which are generic extensions for data within an Ogg container. Renaming these file extensions to `.ogv` _may_ allow the videos to be imported in Godot. However, not all files with `.ogg` or `.ogx` extensions are videos - some of them may only contain audio.

### Setting up VideoStreamPlayer

1. Create a VideoStreamPlayer node using the Create New Node dialog.
2. Select the VideoStreamPlayer node in the scene tree dock, go to the inspector and load a `.ogv` file in the Stream property.

- If you don't have your video in Ogg Theora format yet, jump to **Recommended Theora encoding settings**.

3. If you want the video to play as soon as the scene is loaded, check **Autoplay** in the inspector. If not, leave **Autoplay** disabled and call `play()` on the VideoStreamPlayer node in a script to start playback when desired.

#### Handling resizing and different aspect ratios

By default, the VideoStreamPlayer will automatically be resized to match the video's resolution. You can make it follow usual [Control](../godot_gdscript_ui_controls.md) sizing by enabling **Expand** on the VideoStreamPlayer node.

To adjust how the VideoStreamPlayer node resizes depending on window size, adjust the anchors using the **Layout** menu at the top of the 2D editor viewport. However, this setup may not be powerful enough to handle all use cases, such as playing fullscreen videos without distorting the video (but with empty space on the edges instead). For more control, you can use an [AspectRatioContainer](../godot_gdscript_ui_controls.md) node, which is designed to handle this kind of use case:

Add an AspectRatioContainer node. Make sure it is not a child of any other container node. Select the AspectRatioContainer node, then set its **Layout** at the top of the 2D editor to **Full Rect**. Set **Ratio** in the AspectRatioContainer node to match your video's aspect ratio. You can use math formulas in the inspector to help yourself. Remember to make one of the operands a float. Otherwise, the division's result will always be an integer.

Once you've configured the AspectRatioContainer, reparent your VideoStreamPlayer node to be a child of the AspectRatioContainer node. Make sure **Expand** is enabled on the VideoStreamPlayer. Your video should now scale automatically to fit the whole screen while avoiding distortion.

> **See also:** See [Multiple resolutions](tutorials_rendering.md) for more tips on supporting multiple aspect ratios in your project.

#### Displaying a video on a 3D surface

Using a VideoStreamPlayer node as a child of a [SubViewport](../godot_gdscript_rendering.md) node, it's possible to display any 2D node on a 3D surface. For example, this can be used to display animated billboards when frame-by-frame animation would require too much memory.

This can be done with the following steps:

1. Create a [SubViewport](../godot_gdscript_rendering.md) node. Set its size to match your video's size in pixels.
2. Create a VideoStreamPlayer node _as a child of the SubViewport node_ and specify a video path in it. Make sure **Expand** is disabled, and enable **Autoplay** if needed.
3. Create a MeshInstance3D node with a PlaneMesh or QuadMesh resource in its Mesh property. Resize the mesh to match the video's aspect ratio (otherwise, it will appear distorted).
4. Create a new StandardMaterial3D resource in the **Material Override** property in the GeometryInstance3D section.
5. Enable **Local To Scene** in the StandardMaterial3D's Resource section (at the bottom). This is _required_ before you can use a ViewportTexture in its Albedo Texture property.
6. In the StandardMaterial3D, set the **Albedo > Texture** property to **New ViewportTexture**. Edit the new resource by clicking it, then specify the path to the SubViewport node in the **Viewport Path** property.
7. Enable **Albedo Texture Force sRGB** in the StandardMaterial3D to prevent colors from being washed out.
8. If the billboard is supposed to emit its own light, set **Shading Mode** to **Unshaded** to improve rendering performance.

See [Using Viewports](tutorials_rendering.md) and the [GUI in 3D demo](https://github.com/godotengine/godot-demo-projects/tree/master/viewport/gui_in_3d) for more information on setting this up.

#### Looping a video

For looping a video, the **Loop** property can be enabled. This will seamlessly restart the video when it reaches its end.

Note that setting the project setting **Video Delay Compensation** to a non-zero value might cause your loop to not be seamless, because the synchronization of audio and video takes place at the start of each loop causing occasional missed frames. Set **Video Delay Compensation** in your project settings to **0** to avoid frame drop issues.

### Video decoding conditions and recommended resolutions

Video decoding is performed on the CPU, as GPUs don't have hardware acceleration for decoding Theora videos. Modern desktop CPUs can decode Ogg Theora videos at 1440p @ 60 FPS or more, but low-end mobile CPUs will likely struggle with high-resolution videos.

To ensure your videos decode smoothly on varied hardware:

- When developing games for desktop platforms, it's recommended to encode in 1080p at most (preferably at 30 FPS). Most people are still using 1080p or lower resolution displays, so encoding higher-resolution videos may not be worth the increased file size and CPU requirements.
- When developing games for mobile or web platforms, it's recommended to encode in 720p at most (preferably at 30 FPS or even lower). The visual difference between 720p and 1080p videos on a mobile device is usually not that noticeable.

### Playback limitations

There are some limitations with the current implementation of video playback in Godot:

- Streaming a video from a URL is not supported.
- Only mono and stereo audio output is supported. Videos with 4, 5.1 and 7.1 audio channels are supported but down-mixed to stereo.

### Recommended Theora encoding settings

A word of advice is to **avoid relying on built-in Ogg Theora exporters** (most of the time). There are 2 reasons you may want to favor using an external program to encode your video:

- Some programs such as Blender can render to Ogg Theora. However, the default quality presets are usually very low by today's standards. You may be able to increase the quality options in the software you're using, but you may find the output quality to remain less than ideal (given the increased file size). This usually means that the software only supports encoding to constant bit rate (CBR), instead of variable bit rate (VBR). VBR encoding should be preferred in most scenarios as it provides a better quality to file size ratio.
- Some other programs can't render to Ogg Theora at all.

In this case, you can **render the video to an intermediate high-quality format** (such as a high-bitrate H.264 video) then re-encode it to Ogg Theora. Ideally, you should use a lossless or uncompressed format as an intermediate format to maximize the quality of the output Ogg Theora video, but this can require a lot of disk space.

[FFmpeg](https://ffmpeg.org/) (CLI) is a popular open source tool for this purpose. FFmpeg has a steep learning curve, but it's a powerful tool.

Here are example FFmpeg commands to convert an MP4 video to Ogg Theora. Since FFmpeg supports a lot of input formats, you should be able to use the commands below with almost any input video format (AVI, MOV, WebM, …).

> **Note:** Make sure your copy of FFmpeg is compiled with libtheora and libvorbis support. You can check this by running `ffmpeg` without any arguments, then looking at the `configuration:` line in the command output.

> **Warning:** Current official FFmpeg releases have some bugs in their Ogg/Theora multiplexer. It's highly recommended to use one of the latest static daily builds, or build from their master branch to get the latest fixes.

#### Balancing quality and file size

The **video quality** level (`-q:v`) must be between `1` and `10`. Quality `6` is a good compromise between quality and file size. If encoding at a high resolution (such as 1440p or 4K), you will probably want to decrease `-q:v` to `5` to keep file sizes reasonable. Since pixel density is higher on a 1440p or 4K video, lower quality presets at higher resolutions will look as good or better compared to low-resolution videos.

The **audio quality** level (`-q:a`) must be between `-1` and `10`. Quality `6` provides a good compromise between quality and file size. In contrast to video quality, increasing audio quality doesn't increase the output file size nearly as much. Therefore, if you want the cleanest audio possible, you can increase this to `9` to get _perceptually lossless_ audio. This is especially valuable if your input file already uses lossy audio compression. Higher quality audio does increase the CPU usage of the decoder, so it might lead to audio dropouts in case of high system load. See [this page](https://wiki.hydrogenaud.io/index.php?title=Recommended_Ogg_Vorbis#Recommended_Encoder_Settings) for a table listing Ogg Vorbis audio quality presets and their respective variable bitrates.

The **GOP (Group of Pictures) size** (`-g:v`) is the max interval between keyframes. Increasing this value can improve compression with almost no impact on quality. The default size (`12`) is too low for most types of content, it's therefore recommended using higher GOP values before reducing video quality. Compression benefits will fade away as the GOP size increases though. Values between `64` and `512` usually give the best compression.

> **Note:** Higher GOP sizes will increase max seek times with a sudden increase when going beyond powers of two starting at `64`. Max seek times with GOP size `65` can be almost twice as long as with GOP size `64`, depending on decoding speed.

#### FFmpeg: Convert while preserving original video resolution

The following command converts the video while keeping its original resolution. The video and audio's bitrate will be variable to maximize quality while saving space in parts of the video/audio that don't require a high bitrate (such as static scenes).

```gdscript
ffmpeg -i input.mp4 -q:v 6 -q:a 6 -g:v 64 output.ogv
```

#### FFmpeg: Resize the video then convert it

The following command resizes a video to be 720 pixels tall (720p), while preserving its existing aspect ratio. This helps decrease the file size significantly if the source is recorded at a higher resolution than 720p:

```gdscript
ffmpeg -i input.mp4 -vf "scale=-1:720" -q:v 6 -q:a 6 -g:v 64 output.ogv
```

### Chroma Key Videos

Chroma key, commonly known as the "green screen" or "blue screen" effect, allows you to remove a specific color from an image or video and replace it with another background. This effect is widely used in video production to composite different elements together seamlessly.

We will achieve the chroma key effect by writing a custom shader in GDScript and using a VideoStreamPlayer node to display the video content.

#### Scene Setup

Ensure that the scene contains a VideoStreamPlayer node to play the video and a Control node to hold the UI elements for controlling the chroma key effect.

#### Writing the Custom Shader

To implement the chroma key effect, follow these steps:

1. Select the VideoStreamPlayer node in the scene and go to its properties. Under CanvasItem > Material, create a new shader named "ChromaKeyShader.gdshader."
2. In the "ChromaKeyShader.gdshader" file, write the custom shader code as shown below:

```glsl
shader_type canvas_item;

// Uniform variables for chroma key effect
uniform vec3 chroma_key_color : source_color = vec3(0.0, 1.0, 0.0);
uniform float pickup_range : hint_range(0.0, 1.0) = 0.1;
uniform float fade_amount : hint_range(0.0, 1.0) = 0.1;

void fragment() {
    // Get the color from the texture at the given UV coordinates
    vec4 color = texture(TEXTURE, UV);

    // Calculate the distance between the current color and the chroma key color
    float distance = length(color.rgb - chroma_key_color);

    // If the distance is within the pickup range, discard the pixel
    // the lesser the distance more likely the colors are
    if (distance <= pickup_range) {
        discard;
    }

    // Calculate the fade factor based on the pickup range and fade amount
    float fade_factor
# ...
```

The shader uses the distance calculation to identify pixels close to the chroma key color and discards them, effectively removing the selected color. Pixels that are slightly further away from the chroma key color are faded based on the fade_factor, blending them smoothly with the surrounding colors. This process creates the desired chroma key effect, making it appear as if the background has been replaced with another image or video.

The code above represents a simple demonstration of the Chroma Key shader, and users can customize it according to their specific requirements.

#### UI Controls

To allow users to manipulate the chroma key effect in real-time, we created sliders in the Control node. The Control node's script contains the following functions:

```gdscript
extends Control

 func _on_color_picker_button_color_changed(color):
     # Update the "chroma_key_color" shader parameter of the VideoStreamPlayer's material.
     $VideoStreamPlayer.material.set("shader_parameter/chroma_key_color", color)

 func _on_h_slider_value_changed(value):
     # Update the "pickup_range" shader parameter of the VideoStreamPlayer's material.
     $VideoStreamPlayer.material.set("shader_parameter/pickup_range", value)

 func _on_h_slider_2_value_changed(value):
     # Update the "fade_amount" shader parameter of the VideoStreamPlayer's material.
     $VideoStreamPlayer.material.set("shader_parameter/fade_amount", value)

func _on_video_stream_player_finished():
     # Restart the video playback when it's finished.
     $VideoStreamPlayer.play()
```

also make sure that the range of the sliders are appropriate, our settings are :

#### Signal Handling

Connect the appropriate signal from the UI elements to the Control node's script. you created in the Control node's script to control the chroma key effect. These signal handlers will update the shader's uniform variables in response to user input.

Save and run the scene to see the chroma key effect in action! With the provided UI controls, you can now adjust the chroma key color, pickup range, and fade amount in real-time, achieving the desired chroma key functionality for your video content.

---
