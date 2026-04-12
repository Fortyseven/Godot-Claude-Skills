# Godot 4 GDScript Tutorials — Animation (Part 1)

> 4 tutorials. GDScript-specific code examples.

## 2D skeletons

> **Work in progress:** The content of this page was not yet updated for Godot `4.6` and may be **outdated**. If you know how to improve this page or you can confirm that it's up to date, feel free to [open a pull request](https://github.com/godotengine/godot-docs).

### Introduction

When working with 3D, skeletal deforms are common for characters and creatures and most 3D modeling applications support it. For 2D, as this function is not used as often, it's difficult to find mainstream software aimed for this.

One option is to create animations in third-party software such as Spine or Dragonbones. This functionality is also supported built-in.

Why would you want to do skeletal animations directly in Godot? The answer is that there are many advantages to it:

- Better integration with the engine, so less hassle importing and editing from an external tool.
- Ability to control particle systems, shaders, sounds, call scripts, colors, transparency, etc. in animations.
- The built-in skeletal system in Godot is very efficient and designed for performance.

The following tutorial will, then, explain 2D skeletal deformations.

### Setup

> **See also:** Before starting, we recommend you to go through the Cutout animation tutorial to gain a general understanding of animating within Godot.

For this tutorial, we will be using a single image to construct our character. Download it from gBot_pieces.png or save the image below.

It is also advised to download the final character image gBot_complete.png to have a good reference for putting the different pieces together.

### Creating the polygons

Create a new scene for your model (if it's going to be an animated character, you may want to use a `CharacterBody2D`). For ease of use, an empty 2D node is created as a root for the polygons.

Begin with a `Polygon2D` node. There is no need to place it anywhere in the scene for now, so simply create it like this:

Select it and assign the texture with the character pieces you have downloaded before:

Drawing a polygon directly is not advised. Instead, open the "UV" dialog for the polygon:

Head over to the _Points_ mode, select the pencil and draw a polygon around the desired piece:

Duplicate the polygon node and give it a proper name. Then, enter the "UV" dialog again and replace the old polygon with another one in the new desired piece.

When you duplicate nodes and the next piece has a similar shape, you can edit the previous polygon instead of drawing a new one.

After moving the polygon, remember to update the UV by selecting **Edit > Copy Polygon to UV** in the Polygon 2D UV Editor.

Keep doing this until you mapped all pieces.

You will notice that pieces for nodes appear in the same layout as they do in the original texture. This is because by default, when you draw a polygon, the UV and points are the same.

Rearrange the pieces and build the character. This should be pretty quick. There is no need to change pivots, so don't bother making sure rotation pivots for each piece are right; you can leave them be for now.

Ah, the visual order of the pieces is not correct yet, as some are covering wrong pieces. Rearrange the order of the nodes to fix this:

And there you go! It was definitely much easier than in the cutout tutorial.

### Creating the skeleton

Create a `Skeleton2D` node as a child of the root node. This will be the base of our skeleton:

Create a `Bone2D` node as a child of the skeleton. Put it on the hip (usually skeletons start here). The bone will be pointing to the right, but you can ignore this for now.

Keep creating bones in hierarchy and naming them accordingly.

At the end of this chain, there will be a _jaw_ node. It is, again, very short and pointing to the right. This is normal for bones without children. The length of _tip_ bones can be changed with a property in the inspector:

In this case, we don't need to rotate the bone (coincidentally the jaw points right in the sprite), but in case you need to, feel free to do it. Again, this is only really needed for tip bones as nodes with children don't usually need a length or a specific rotation.

Keep going and build the whole skeleton:

You will notice that all bones raise a warning about a missing rest pose. A rest pose is the default pose for a skeleton, you can come back to it anytime you want (which is very handy for animating). To set one click on the _skeleton_ node in the scene tree, then click on the Skeleton2D button in the toolbar, and select `Overwrite Rest Pose` from the dropdown menu.

The warnings will go away. If you modify the skeleton (add/remove bones) you will need to set the rest pose again.

### Deforming the polygons

Select the previously created polygons and assign the skeleton node to their `Skeleton` property. This will ensure that they can eventually be deformed by it.

Click the property highlighted above and select the skeleton node:

Again, open the UV editor for the polygon and go to the _Bones_ section.

You will not be able to paint weights yet. For this you need to synchronize the list of bones from the skeleton with the polygon. This step is done only once and manually (unless you modify the skeleton by adding/removing/renaming bones). It ensures that your rigging information is kept in the polygon, even if a skeleton node is accidentally lost or the skeleton modified. Push the "Sync Bones to Polygon" button to sync the list.

The list of bones will automatically appear. By default, your polygon has no weight assigned to any of them. Select the bones you want to assign weight to and paint them:

Points in white have a full weight assigned, while points in black are not influenced by the bone. If the same point is painted white for multiple bones, the influence will be distributed amongst them (so usually there is not that much need to use shades in-between unless you want to polish the bending effect).

After painting the weights, animating the bones (NOT the polygons!) will have the desired effect of modifying and bending the polygons accordingly. As you only need to animate bones in this approach, work becomes much easier!

But it's not all roses. Trying to animate bones that bend the polygon will often yield unexpected results:

This happens because Godot generates internal triangles that connect the points when drawing the polygon. They don't always bend the way you would expect. To solve this, you need to set hints in the geometry to clarify how you expect it to deform.

### Internal vertices

Open the UV menu for each bone again and go to the _Points_ section. Add some internal vertices in the regions where you expect the geometry to bend:

Now, go to the _Polygon_ section and redraw your own polygons with more detail. Imagine that, as your polygons bend, you need to make sure they deform the least possible, so experiment a bit to find the right setup.

Once you start drawing, the original polygon will disappear and you will be free to create your own:

This amount of detail is usually fine, though you may want to have more fine-grained control over where triangles go. Experiment by yourself until you get the results you like.

**Note:** Don't forget that your newly added internal vertices also need weight painting! Go to the _Bones_ section again to assign them to the right bones.

Once you are all set, you will get much better results:

---

## Animation Track types

This page gives an overview of the track types available for Godot's animation player node on top of the default property tracks.

> **See also:** We assume you already read Introduction to the animation features, which covers the basics, including property tracks.

### Property Track

The most basic track type. See Introduction to the animation features.

### Position 3D / Rotation 3D / Scale 3D Track

These 3D transform tracks control the location, rotation, and scale of a 3D object. They make it easier to animate a 3D object's transform compared to using regular property tracks.

It is designed for animations imported from external 3D models and can reduce resource capacity through compression.

### Blend Shape Track

A blend shape track is optimized for animating blend shape in [MeshInstance3D](../godot_gdscript_nodes_3d.md).

It is designed for animations imported from external 3D models and can reduce resource capacity through compression.

### Call Method Track

A call method track allow you to call a function at a precise time from within an animation. For example, you can call `queue_free()` to delete a node at the end of a death animation.

> **Note:** The events placed on the call method track are not executed when the animation is previewed in the editor for safety.

To create such a track in the editor, click "Add Track -> Call Method Track." Then, a window opens and lets you select the node to associate with the track. To call one of the node's methods, right-click the timeline and select "Insert Key". A window opens with a list of available methods. Double-click one to finish creating the keyframe.

To change the method call or its arguments, click on the key and head to the inspector dock. There, you can change the method to call. If you expand the "Args" section, you will see a list of arguments you can edit.

To create such a track through code, pass a dictionary that contains the target method's name and parameters as the Variant for `key` in `Animation.track_insert_key()`. The keys and their expected values are as follows:

| Key      | Value                                             |
| -------- | ------------------------------------------------- |
| "method" | The name of the method as a String                |
| "args"   | The arguments to pass to the function as an Array |

```gdscript
# Create a call method track.
func create_method_animation_track():
    # Get or create the animation the target method will be called from.
    var animation = $AnimationPlayer.get_animation("idle")
    # Get or create the target method's animation track.
    var track_index = animation.add_track(Animation.TYPE_METHOD)
    # Make the arguments for the target method jump().
    var jump_velocity = -400.0
    var multiplier = randf_range(.8, 1.2)
    # Get or create a dictionary with the target method's name and arguments.
    var method_dictionary = {
        "method": "jump",
        "args": [jump_velocity, multiplier],
    }

    # Set scene-tree path to node with target method.
    animation.track_set_path(track_index, ".")
    # Add the dictionary as the animation method track's key.

# ...
```

### Bezier Curve Track

A bezier curve track is similar to a property track, except it allows you to animate a property's value using a bezier curve.

> **Note:** Bezier curve track and property track cannot be blended in [AnimationPlayer](../godot_gdscript_resources.md) and [AnimationTree](../godot_gdscript_resources.md).

To create one, click "Add Track -> Bezier Curve Track". As with property tracks, you need to select a node and a property to animate. To open the bezier curve editor, click the curve icon to the right of the animation track.

In the editor, keys are represented by filled diamonds and the outlined diamonds connected to them by a line control curve's shape.

> **Tip:** For better precision while manually working with curves, you might want to alter the zoom levels of the editor. The slider on the bottom right of the editor can be used to zoom in and out on the time axis, you can also do that with Ctrl + Shift + Mouse wheel. Using Ctrl + Alt + Mouse wheel will zoom in and out on the Y axis

While a keyframe is selected (not the handle), in the right click panel of the editor, you can select the handle mode:

- Free: Allows you to orient a manipulator in any direction without affecting the other's position.
- Linear: Does not allow rotation of the manipulator and draws a linear graph.
- Balanced: Makes it so manipulators rotate together, but the distance between the key and a manipulator is not mirrored.
- Mirrored: Makes the position of one manipulator perfectly mirror the other, including their distance to the key.

### Audio Playback Track

If you want to create an animation with audio, you need to create an audio playback track. To create one, your scene must have either an AudioStreamPlayer, AudioStreamPlayer2D, or AudioStreamPlayer3D node. When creating the track, you must select one of those nodes.

To play a sound in your animation, drag and drop an audio file from the file system dock onto the animation track. You should see the waveform of your audio file in the track.

To remove a sound from the animation, you can right-click it and select "Delete Key(s)" or click on it and press the Del key.

The blend mode allows you to choose whether or not to adjust the audio volume when blending in the [AnimationTree](../godot_gdscript_resources.md).

### Animation Playback Track

Animation playback tracks allow you to sequence the animations of other animation player nodes in a scene. For example, you can use it to animate several characters in a cut-scene.

To create an animation playback track, select "New Track -> Animation Playback Track."

Then, select the animation player you want to associate with the track.

To add an animation to the track, right-click on it and insert a key. Select the key you just created to select an animation in the inspector dock.

If an animation is already playing and you want to stop it early, you can create a key and have it set to [STOP] in the inspector.

> **Note:** If you instanced a scene that contains an animation player into your scene, you need to enable "Editable Children" in the scene tree to access its animation player. Also, an animation player cannot reference itself.

---

## Using AnimationTree

### Introduction

With [AnimationPlayer](../godot_gdscript_resources.md), Godot has one of the most flexible animation systems that you can find in any game engine. It is pretty much unique in its ability to animate almost any property in any node or resource, and its dedicated transform, bezier, function calling, audio, and sub-animation tracks.

However, the support for blending those animations via `AnimationPlayer` is limited, as you can only set a fixed cross-fade transition time.

[AnimationTree](../godot_gdscript_resources.md) is a node designed to deal with advanced transitions.

### AnimationTree and AnimationPlayer

Before starting, know that an `AnimationTree` node does not contain its own animations. Instead, it uses animations contained in an `AnimationPlayer` node. You create, edit, or import your animations in an `AnimationPlayer` and then use an `AnimationTree` to control the playback.

`AnimationPlayer` and `AnimationTree` can be used in both 2D and 3D scenes. When importing 3D scenes and their animations, you can use [name suffixes](https://docs.godotengine.org/en/stable/tutorials/assets_pipeline/importing_3d_scenes/node_type_customization.html#animation-loop-loop-cycle) to simplify the process and import with the correct properties. At the end, the imported Godot scene will contain the animations in an `AnimationPlayer` node. Since you rarely use imported scenes directly in Godot (they are either instantiated or inherited from), you can place the `AnimationTree` node in your new scene which contains the imported one. Afterwards, point the `AnimationTree` node to the `AnimationPlayer` that was created in the imported scene.

This is how it's done in the [Third Person Shooter demo](https://godotengine.org/asset-library/asset/2710), for reference:

A new scene was created for the player with a `CharacterBody3D` as root. Inside this scene, the original `.dae` (Collada) file was instantiated and an `AnimationTree` node was created.

### Creating a tree

To use an `AnimationTree`, you have to set a root node. An animation root node is a class that contains and evaluates sub-nodes and outputs an animation. There are 3 types of sub-nodes:

1. Animation nodes, which reference an animation from the linked `AnimationPlayer`.
2. Animation Root nodes, which are used to blend sub-nodes and can be nested.
3. Animation Blend nodes, which are used in an `AnimationNodeBlendTree`, a 2D graph of nodes. Blend nodes take multiple input ports and give one output port.

A few types of root nodes are available:

- `AnimationNodeAnimation`: Selects an animation from the list and plays it. This is the simplest root node, and generally not used as a root.
- `AnimationNodeBlendTree`: Contains multiple nodes as children in a graph. Many blend nodes are available, such as mix, blend2, blend3, one shot, etc.
- `AnimationNodeBlendSpace1D`: Allows linear blending between two animation nodes. Control the blend position in a 1D blend space to mix between animations.
- `AnimationNodeBlendSpace2D`: Allows linear blending between three animation nodes. Control the blend position in a 2D blend space to mix between animations.
- `AnimationNodeStateMachine`: Contains multiple nodes as children in a graph. Each node is used as a state, with multiple functions used to alternate between states.

### Blend tree

When you make an `AnimationNodeBlendTree`, you get an empty 2d graph in the bottom panel, under the AnimationTree tab. It contains only an `Output` node by default.

In order for animations to play, a node has to be connected to the output. You can add nodes from the **Add Node..** menu or by right clicking an empty space:

The simplest connection to make is to connect an `Animation` node to the output directly, which will just play back the animation.

Following is a description of the other available nodes:

#### Blend2 / Blend3

These nodes will blend between two or three inputs by a user-specified blend value:

Blending can use **filters** to control individually which tracks get blended and which do not. This can be useful for layering animations on top of each other.

For more complex blending, it is recommended to use blend spaces instead.

#### OneShot

This node will execute an animation once and return when it finishes. You can customize blend times for fading in and out, as well as filters.

```gdscript
# Play child animation connected to "shot" port.
animation_tree.set("parameters/OneShot/request", AnimationNodeOneShot.ONE_SHOT_REQUEST_FIRE)
# Alternative syntax (same result).
animation_tree["parameters/OneShot/request"] = AnimationNodeOneShot.ONE_SHOT_REQUEST_FIRE

# Abort child animation connected to "shot" port.
animation_tree.set("parameters/OneShot/request", AnimationNodeOneShot.ONE_SHOT_REQUEST_ABORT)
# Alternative syntax (same result).
animation_tree["parameters/OneShot/request"] = AnimationNodeOneShot.ONE_SHOT_REQUEST_ABORT

# Get current state (read-only).
animation_tree.get("parameters/OneShot/active"))
# Alternative syntax (same result).
animation_tree["parameters/OneShot/active"]
```

#### TimeSeek

This node allows you to seek to a time in the animation connected to its in input. Use this node to play an `Animation` starting from a certain playback position. Note that the seek request value is measured in seconds, so if you would like to play an animation from the beginning, set the value to `0.0`, or if you would like to play an animation from 3 seconds in, set the value to `3.0`.

```gdscript
# Play child animation from the start.
animation_tree.set("parameters/TimeSeek/seek_request", 0.0)
# Alternative syntax (same result).
animation_tree["parameters/TimeSeek/seek_request"] = 0.0

# Play child animation from 12 second timestamp.
animation_tree.set("parameters/TimeSeek/seek_request", 12.0)
# Alternative syntax (same result).
animation_tree["parameters/TimeSeek/seek_request"] = 12.0
```

#### TimeScale

This node allows you to scale the speed of the animation connected to its in input. The speed of the animation will be multiplied by the number in the scale parameter. Setting the scale to 0 will pause the animation. Setting the scale to a negative number will play the animation backwards.

#### Transition

This node is a simplified version of a StateMachine. You connect animations to the inputs, and the current state index determines which animation to play. You may specify a crossfade transition time. In the Inspector, you may change the number of input ports, rearrange inputs, or delete inputs.

```gdscript
# Play child animation connected to "state_2" port.
animation_tree.set("parameters/Transition/transition_request", "state_2")
# Alternative syntax (same result).
animation_tree["parameters/Transition/transition_request"] = "state_2"

# Get current state name (read-only).
animation_tree.get("parameters/Transition/current_state")
# Alternative syntax (same result).
animation_tree["parameters/Transition/current_state"]

# Get current state index (read-only).
animation_tree.get("parameters/Transition/current_index"))
# Alternative syntax (same result).
animation_tree["parameters/Transition/current_index"]
```

#### StateMachine

When you make an `AnimationNodeStateMachine`, you get an empty 2d graph in the bottom panel, under the AnimationTree tab. It contains a `Start` and `End` state by default.

To add states, right click or use the **create new nodes** button, whose icon is a plus in a box. You can add animations, blendspaces, blendtrees, or even another StateMachine. To edit one of these more complex sub-nodes, click on the pencil icon on the right of the state. To return to the original StateMachine, click **Root** on the top left of the panel.

Before the StateMachine can do anything useful, the states must be connected with transitions. To add a transition, click the **connect nodes** button, which is a line with a right-facing arrow, and drag between two states. You can create 2 transitions between states, one going in each direction.

There are 3 types of transitions:

- _Immediate_: Will switch to the next state immediately.
- _Sync_: Will switch to the next state immediately, but will seek the new state to the playback position of the old state.
- _At End_: Will wait for the current state playback to end, then switch to the beginning of the next state animation.

Transitions also have a few properties. Click a transition and it will be displayed in the inspector:

- _Xfade Time_ is the time to cross-fade between this state and the next.
- _Xfade Curve_ is a cross-fade following a curve rather than a linear blend.
- _Reset_ determines whether the state you are switching into plays from the beginning (true) or not (false).
- _Priority_ is used together with the `travel()` function from code (more on this later). Lower priority transitions are preferred when travelling through the tree.
- _Switch Mode_ is the transition type (see above). It can be changed after creation here.
- _Advance Mode_ determines the advance mode. If `Disabled`, the transition will not be used. If `Enabled`, the transition will only be used during `travel()`. If `Auto`, the transition will be used if the advance condition and expression are true, or if there are no advance conditions/expressions.

##### Advance Condition and Advance Expression

The last 2 properties in a StateMachine transition are `Advance Condition` and `Advance Expression.` When the Advance Mode is set to _Auto_, these determine if the transition will advance or not.

Advance Condition is a true/false check. You may put a custom variable name in the text field, and when the StateMachine reaches this transition, it will check if your variable is _true_. If so, the transition continues. Note that the advance condition **only** checks if a variable is _true_, and it cannot check for falseness.

This gives the Advance Condition a very limited capability. If you wanted to make a transition back and forth based on one property, you would need to make 2 variables that have opposite values, and check if either of them are true. This is why, in Godot 4, the Advance Expression was added.

The Advance Expression works similar to the Advance Condition, but instead of checking if one variable is true, it evaluates any expression. An expression is anything you could put in an `if` statement. These are all examples of expressions that would work in the Advance Expression:

- `is_walking`
- `is_walking == true` (behaves the same as the one above)
- `is_walking && !is_idle`
- `velocity > 0`
- `player.is_on_floor()`

> **Warning:** The expression is **case-sensitive**. If you reference engine properties, such as `velocity` on a [CharacterBody3D](../godot_gdscript_nodes_3d.md) node, you should use `snake_case` naming conventions. If you reference script properties, you should match the style used in the script, which is typically `snake_case` in GDScript and `PascalCase` in C#.

Here is an example of an improperly-set-up StateMachine transition using Advance Condition:

This is not working because there is a `!` variable in the Advance Condition, which cannot be checked.

Here is the same example, set up properly, using two opposite variables:

Here is the same example, but using Advance Expression rather than Advance Condition, which eliminates the need for two variables:

In order to use Advance Expressions, the Advance Expression Base Node has to be set from the Inspector of the AnimationTree node. By default, it is set to the AnimationTree node itself, but it needs to point to whatever node contains the script with your animation variables.

> **See also:** The Advance Expression is evaluated using Godot's [Expression](../godot_gdscript_misc.md) class. See [Evaluating expressions](tutorials_scripting.md) for more information on writing expressions.

##### StateMachine travel

One of the nice features in Godot's `StateMachine` implementation is the ability to travel. You can instruct the graph to go from the current state to another one, while visiting all the intermediate ones. This is done via the A\* algorithm. If there is no path of transitions starting at the current state and finishing at the destination state, the graph teleports to the destination state.

To use the travel ability, you should first retrieve the [AnimationNodeStateMachinePlayback](../godot_gdscript_resources.md) object from the `AnimationTree` node (it is exported as a property), and then call one of its many functions:

```gdscript
var state_machine = animation_tree["parameters/playback"]
state_machine.travel("SomeState")
```

The StateMachine must be running before you can travel. Make sure to either call `start()` or connect a node to **Start**.

### BlendSpace2D and BlendSpace1D

`BlendSpace2D` is a node to do advanced blending in two dimensions. Points representing animations are added to a 2D space and then a position between them is controlled to determine the blending:

You may place these points anywhere on the graph by right clicking or using the **add point** button, whose icon is a pen and point. Wherever you place the points, the triangle between them will be generated automatically using Delaunay. You may also control and label the ranges in X and Y.

Finally, you may also change the blend mode. By default, blending happens by interpolating points inside the closest triangle. When dealing with 2D animations (frame by frame), you may want to switch to _Discrete_ mode. Alternatively, if you want to keep the current play position when switching between discrete animations, there is a _Carry_ mode. This mode can be changed in the _Blend_ menu:

BlendSpace1D works just like BlendSpace2D, but in one dimension (a line). Triangles are not used.

### For better blending

For the blending results to be deterministic (reproducible and always consistent), the blended property values must have a specific initial value. For example, in the case of two animations to be blended, if one animation has a property track and the other does not, the blended animation is calculated as if the latter animation had a property track with the initial value.

When using Position/Rotation/Scale 3D tracks for Skeleton3D bones, the initial value is Bone Rest. For other properties, the initial value is `0` and if the track is present in the `RESET` animation, the value of its first keyframe is used instead.

For example, the following AnimationPlayer has two animations, but one of them lacks a Property track for Position.

This means that the animation lacking that will treat those Positions as `Vector2(0, 0)`.

This problem can be solved by adding a Property track for Position as an initial value to the `RESET` animation.

> **Note:** Be aware that the `RESET` animation exists to define the default pose when loading an object originally. It is assumed to have only one frame and is not expected to be played back using the timeline.

Also keep in mind that the Rotation 3D tracks and the Property tracks for 2D rotation with Interpolation Type set to Linear Angle or Cubic Angle will prevent rotations greater than 180 degrees from the initial value as blended animation.

This can be useful for Skeleton3Ds to prevent the bones penetrating the body when blending animations. Therefore, Skeleton3D's Bone Rest values should be as close to the midpoint of the movable range as possible. **This means that for humanoid models, it is preferable to import them in a T-pose**.

You can see that the shortest rotation path from Bone Rests is prioritized rather than the shortest rotation path between animations.

If you need to rotate Skeleton3D itself more than 180 degrees by blend animations for movement, you can use Root Motion.

### Root motion

When working with 3D animations, a popular technique is for animators to use the root skeleton bone to give motion to the rest of the skeleton. This allows animating characters in a way where steps actually match the floor below. It also allows precise interaction with objects during cinematics.

When playing back the animation in Godot, it is possible to select this bone as the _root motion track_. Doing so will cancel the bone transformation visually (the animation will stay in place).

Afterwards, the actual motion can be retrieved via the [AnimationTree](../godot_gdscript_resources.md) API as a transform:

```gdscript
# Get the motion delta.
animation_tree.get_root_motion_position()
animation_tree.get_root_motion_rotation()
animation_tree.get_root_motion_scale()

# Get the actual blended value of the animation.
animation_tree.get_root_motion_position_accumulator()
animation_tree.get_root_motion_rotation_accumulator()
animation_tree.get_root_motion_scale_accumulator()
```

This can be fed to functions such as [CharacterBody3D.move_and_slide](../godot_gdscript_nodes_3d.md) to control the character movement.

There is also a tool node, `RootMotionView`, you can place a scene that will act as a custom floor for your character and animations (this node is disabled by default during the game).

### Controlling from code

After building the tree and previewing it, the only question remaining is "How is all this controlled from code?".

Keep in mind that the animation nodes are just resources, so they are shared between all instances using them. Setting values in the nodes directly will affect all instances of the scene that uses this `AnimationTree`. This is generally undesirable, but does have some cool use cases, e.g. you can copy and paste parts of your animation tree, or reuse nodes with a complex layout (such as a StateMachine or blend space) in different animation trees.

The actual animation data is contained in the `AnimationTree` node and is accessed via properties. Check the "Parameters" section of the `AnimationTree` node to see all the parameters that can be modified in real-time:

This is handy because it makes it possible to animate them from an `AnimationPlayer`, or even the `AnimationTree` itself, allowing very complex animation logic.

To modify these values from code, you must obtain the property path. You can find them by hovering your mouse over any of the parameters:

Then you can set or read them:

```gdscript
animation_tree.set("parameters/eye_blend/blend_amount", 1.0)
# Alternate syntax (same result)
animation_tree["parameters/eye_blend/blend_amount"] = 1.0
```

> **Note:** Advance Expressions from a StateMachine will not be found under the parameters. This is because they are held in another script rather than the AnimationTree itself. Advance Conditions will be found under parameters.

---

## Creating movies

Godot can record **non-real-time** video and audio from any 2D or 3D project. This kind of recording is also called _offline rendering_. There are many scenarios where this is useful:

- Recording game trailers for promotional use.
- Recording cutscenes that will be displayed as pre-recorded videos in the final game. This allows for using higher quality settings (at the cost of file size), regardless of the player's hardware.
- Recording procedurally generated animations or motion design. User interaction remains possible during video recording, and audio can be included as well (although you won't be able to hear it while the video is recording).
- Comparing the visual output of graphics settings, shaders, or rendering techniques in an animated scene.

With Godot's animation features such as the AnimationPlayer node, Tweeners, particles and shaders, it can effectively be used to create any kind of 2D and 3D animations (and still images).

If you are already used to Godot's workflow, you may find yourself more productive by using Godot for video rendering compared to Blender. That said, renderers designed for non-real-time usage such as Cycles and Eevee can result in better visuals (at the cost of longer rendering times).

Compared to real-time video recording, some advantages of non-real-time recording include:

- Use any graphics settings (including extremely demanding settings) regardless of your hardware's capabilities. The output video will _always_ have perfect frame pacing; it will never exhibit dropped frames or stuttering. Faster hardware will allow you to render a given animation in less time, but the visual output remains identical.
- Render at a higher resolution than the screen resolution, without having to rely on driver-specific tools such as NVIDIA's Dynamic Super Resolution or AMD's Virtual Super Resolution.
- Render at a higher framerate than the video's target framerate, then **post-process to generate high-quality motion blur**. This also makes effects that converge over several frames (such as temporal antialiasing, SDFGI and volumetric fog) look better.

> **Warning:** **This feature is not designed for capturing real-time footage during gameplay.** Players should use something like [OBS Studio](https://obsproject.com/) or [SimpleScreenRecorder](https://www.maartenbaert.be/simplescreenrecorder/) to record gameplay videos, as they do a much better job at intercepting the compositor than Godot can do using Vulkan or OpenGL natively. That said, if your game runs at near-real-time speeds when capturing, you can still use this feature (but it will lack audible sound playback, as sound is saved directly to the video file).

### Enabling Movie Maker mode

To enable Movie Maker mode, click the "movie reel" button in the top-right corner of the editor _before_ running the project:

A menu will be displayed with options to enable Movie Maker mode and to go to the settings. The icon gets a background matching the accent color when Movie Maker mode is enabled:

Movie Maker status is **not** persisted when the editor quits, so you must re-enable Movie Maker mode again after restarting the editor if needed.

> **Note:** Toggling Movie Maker mode while running the project will not have any effect until the project is restarted.

Before you can record video by running the project, you still need to configure the output file path. This path can be set for all scenes in the Project Settings:

Alternatively, you can set the output file path on a per-scene basis by adding a String metadata with the name `movie_file` to the scene's **root node**. This is only used when the main scene is set to the scene in question, or when running the scene directly by pressing F6 (Cmd + R on macOS).

The path specified in the project settings or metadata can be either absolute, or relative to the project root.

Once you've configured and enabled Movie Maker mode, it will be automatically used when running the project from the editor.

#### Command line usage

Movie Maker can also be enabled from the [command line](tutorials_editor.md):

```gdscript
godot --path /path/to/your_project --write-movie output.avi
```

If the output path is relative, then it is **relative to the project folder**, not the current working directory. In the above example, the file will be written to `/path/to/your_project/output.avi`. This behavior is similar to the `--export-release` command line argument.

Since Movie Maker's output resolution is set by the viewport size, you can adjust the window size on startup to override it if the project uses the `disabled` or `canvas_items` [stretch mode](tutorials_rendering.md):

```gdscript
godot --path /path/to/your_project --write-movie output.avi --resolution 1280x720
```

Note that the window size is clamped by your display's resolution. See **Rendering at a higher resolution than the screen resolution** if you need to record a video at a higher resolution than the screen resolution.

The recording FPS can also be overridden on the command line, without having to edit the Project Settings:

```gdscript
godot --path /path/to/your_project --write-movie output.avi --fixed-fps 30
```

> **Note:** The `--write-movie` and `--fixed-fps` command line arguments are both available in exported projects. Movie Maker mode cannot be toggled while the project is running, but you can use the [OS.execute()](../godot_gdscript_misc.md) method to run a second instance of the exported project that will record a video file.

### Choosing an output format

Output formats are provided by the [MovieWriter](../godot_gdscript_misc.md) class. Godot has 3 built-in [MovieWriters](../godot_gdscript_misc.md), and more can be implemented by extensions:

#### OGV (recommended)

OGV container with Theora for video and Vorbis for audio. Features lossy video and audio compression with a good balance of file size and encoding speed, with a better image quality than MJPEG. It has 4 speed levels that can be adjusted by changing **Editor > Movie Writer > Encoding Speed** with the fastest one being around as fast as AVI with better compression. At slower speed levels, it can compress even better while keeping the same image quality. The lossy compression quality can be adjusted by changing **Editor > Movie Writer > Video Quality** for video and **Editor > Movie Writer > Audio Quality** for audio.

The Keyframe Interval can be adjusted by changing **Editor > Movie Writer > Keyframe Interval**. In some cases, increasing this setting can improve compression efficiency without downsides.

The resulting file can be viewed in Godot with [VideoStreamPlayer](../godot_gdscript_ui_controls.md) and most video players but not web browsers. OGV does not support transparency.

To use OGV, specify a path to a `.ogv` file to be created in the **Editor > Movie Writer > Movie File** project setting.

> **Note:** OGV can only be recorded in editor builds. On the other hand, OGV playback is possible in both editor and export template builds.

#### AVI

AVI container with MJPEG for video and uncompressed audio. Features lossy video compression, resulting in medium file sizes and fast encoding. The lossy compression quality can be adjusted by changing **Editor > Movie Writer > Video Quality**.

The resulting file can be viewed in most video players, but it must be converted to another format for viewing on the web or by Godot with the VideoStreamPlayer node. MJPEG does not support transparency. AVI output is currently limited to a file of 4 GB in size at most.

To use AVI, specify a path to a `.avi` file to be created in the **Editor > Movie Writer > Movie File** project setting.

#### PNG

PNG image sequence for video and WAV for audio. Features lossless video compression, at the cost of large file sizes and slow encoding. This is designed to be **encoded to a video file with an external tool after recording**.

Transparency is supported, but the root viewport **must** have its `transparent_bg` property set to `true` for transparency to be visible on the output image. This can be achieved by enabling the **Rendering > Transparent Background** advanced project setting. **Display > Window > Size > Transparent** and **Display > Window > Per Pixel Transparency > Enabled** can optionally be enabled to allow transparency to be previewed while recording the video, but they do not have to be enabled for the output image to contain transparency.

To use PNG, specify a `.png` file to be created in the **Editor > Movie Writer > Movie File** project setting. The generated `.wav` file will have the same name as the `.png` file (minus the extension).

#### Custom

If you need to encode directly to a different format or pipe a stream through third-party software, you can extend the MovieWriter class to create your own movie writers. This should typically be done using GDExtension for performance reasons.

### Configuration

In the **Editor > Movie Writer** section of the Project Settings, there are several options you can configure. Some of them are only visible after enabling the **Advanced** toggle in the top-right corner of the Project Settings dialog.

- **Mix Rate Hz:** The audio mix rate to use in the recorded audio when writing a movie. This can be different from the project's mix rate, but this value must be divisible by the recorded FPS to prevent audio from desynchronizing over time.
- **Speaker Mode:** The speaker mode to use in the recorded audio when writing a movie (stereo, 5.1 surround or 7.1 surround).
- **Video Quality:** The image quality to use when writing a video to an OGV or AVI file, between `0.01` and `1.0` (inclusive). Higher quality values result in better-looking output at the cost of larger file sizes. Recommended quality values are between `0.75` and `0.9`. Even at quality `1.0`, compression remains lossy. This setting does not affect audio quality and is ignored when writing to a PNG image sequence.
- **Movie File:** The output path for the movie. This can be absolute or relative to the project root.
- **Disable V-Sync:** If enabled, requests V-Sync to be disabled when writing a movie. This can speed up video writing if the hardware is fast enough to render, encode and save the video at a framerate higher than the monitor's refresh rate. This setting has no effect if the operating system or graphics driver forces V-Sync with no way for applications to disable it.
- **FPS:** The rendered frames per second in the output movie. Higher values result in smoother animation, at the cost of longer rendering times and larger output file sizes. Most video hosting platforms do not support FPS values higher than 60, but you can use a higher value and use that to generate motion blur.
- **Audio Quality:** The audio quality to use when writing a video to an OGV file, between `-0.1` and `1.0` (inclusive). Higher quality values result in better audio quality at the cost of very slightly larger file sizes. Recommended quality values are between `0.3` and `0.5`. Even at quality `1.0`, compression remains lossy.
- **Encoding Speed:** The speed level to use when writing a video to an OGV file. Faster speed levels have less compression efficiency. The image quality stays barely the same.
- **Keyframe Interval:** Also known as GOP (Group Of Pictures), the maximum number of inter-frames to use when writing to an OGV file. Higher values can improve compression efficiency without quality loss but at the cost of slower video seeks.

> **Note:** When using the `disabled` or `2d` [stretch modes](tutorials_rendering.md), the output file's resolution is set by the window size. Make sure to resize the window _before_ the splash screen has ended. For this purpose, it's recommended to adjust the **Display > Window > Size > Window Width Override** and **Window Height Override** advanced project settings. See also **Rendering at a higher resolution than the screen resolution**.

### Quitting Movie Maker mode

To safely quit a project that is using Movie Maker mode, use the X button at the top of the window, or call `get_tree().quit()` in a script. You can also use the `--quit-after N` command line argument where `N` is the number of frames to render before quitting.

Pressing F8 (Cmd + . on macOS) or pressing Ctrl + C on the terminal running Godot is **not recommended**, as it will result in an improperly formatted AVI file with no duration information. For PNG image sequences, PNG images will not be negatively altered, but the associated WAV file will still lack duration information. OGV files might end up with slightly different duration video and audio tracks but still valid.

Some video players may still be able to play the AVI or WAV file with working video and audio. However, software that makes use of the AVI or WAV file such as video editors may not be able to open the file. **Using a video converter program** can help in those cases.

If you're using an AnimationPlayer to control a "main action" in the scene (such as camera movement), you can enable the **Movie Quit On Finish** property on the AnimationPlayer node in question. When enabled, this property will make Godot quit on its own when an animation is done playing _and_ the engine is running in Movie Maker mode. Note that _this property has no effect on looping animations_. Therefore, you need to make sure that the animation is set as non-looping.

### Using high-quality graphics settings

The `movie` [feature tag](tutorials_export.md) can be used to override specific project settings. This is useful to enable high-quality graphics settings that wouldn't be fast enough to run in real-time speeds on your hardware. Remember that putting every setting to its maximum value can still slow down movie saving speed, especially when recording at higher resolutions. Therefore, it's still recommended to only increase graphics settings if they make a meaningful difference in the output image.

This feature tag can also be queried in a script to increase quality settings that are set in the Environment resource. For example, to further improve SDFGI detail and reduce light leaking:

```gdscript
extends Node3D

func _ready():
    if OS.has_feature("movie"):
        # When recording a movie, improve SDFGI cell density
        # without decreasing its maximum distance.
        get_viewport().world_3d.environment.sdfgi_min_cell_size *= 0.25
        get_viewport().world_3d.environment.sdfgi_cascades = 8
```

### Rendering at a higher resolution than the screen resolution

The overall rendering quality can be improved significantly by rendering at high resolutions such as 4K or 8K.

> **Note:** For 3D rendering, Godot provides a **Rendering > Scaling 3D > Scale** advanced project setting, which can be set above `1.0` to obtain _supersample antialiasing_. The 3D rendering is then _downsampled_ when it's drawn on the viewport. This provides an expensive but high-quality form of antialiasing, without increasing the final output resolution. Consider using this project setting first, as it avoids slowing down movie writing speeds and increasing output file size compared to actually increasing the output resolution.

If you wish to render 2D at a higher resolution, or if you actually need the higher raw pixel output for 3D rendering, you can increase the resolution above what the screen allows.

By default, Godot uses the `disabled` [stretch modes](tutorials_rendering.md) in projects. If using `disabled` or `canvas_items` stretch mode, the window size dictates the output video resolution.

On the other hand, if the project is configured to use the `viewport` stretch mode, the viewport resolution dictates the output video resolution. The viewport resolution is set using the **Display > Window > Size > Viewport Width** and **Viewport Height** project settings. This can be used to render a video at a higher resolution than the screen resolution.

To make the window smaller during recording without affecting the output video resolution, you can set the **Display > Window > Size > Window Width Override** and **Window Height Override** advanced project settings to values greater than `0`.

To apply a resolution override only when recording a movie, you can override those settings with the `movie` [feature tag](tutorials_export.md).

### Post-processing steps

Some common post-processing steps are listed below.

> **Note:** When using several post-processing steps, try to perform all of them in a single FFmpeg command. This will save encoding time and improve quality by avoiding multiple lossy encoding steps.

#### Converting OGV/AVI video to MP4

While some platforms such as YouTube support uploading the AVI file directly, many others will require a conversion step beforehand. [HandBrake](https://handbrake.fr/) (GUI) and [FFmpeg](https://ffmpeg.org/) (CLI) are popular open source tools for this purpose. FFmpeg has a steeper learning curve, but it's more powerful.

The command below converts an OGV/AVI video to an MP4 (H.264) video with a Constant Rate Factor (CRF) of 15. This results in a relatively large file, but is well-suited for platforms that will re-encode your videos to reduce their size (such as most video sharing websites):

```gdscript
ffmpeg -i input.avi -crf 15 output.mp4
```

To get a smaller file at the cost of quality, _increase_ the CRF value in the above command.

To get a file with a better size/quality ratio (at the cost of slower encoding times), add `-preset veryslow` before `-crf 15` in the above command. On the contrary, `-preset veryfast` can be used to achieve faster encoding at the cost of a worse size/quality ratio.

#### Converting PNG image sequence + WAV audio to a video

If you chose to record a PNG image sequence with a WAV file beside it, you need to convert it to a video before you can use it elsewhere.

The filename for the PNG image sequence generated by Godot always contains 8 digits, starting at 0 with zero-padded numbers. If you specify an output path `folder/example.png`, Godot will write `folder/example00000000.png`, `folder/example00000001.png`, and so on in that folder. The audio will be saved at `folder/example.wav`.

The FPS is specified using the `-r` argument. It should match the FPS specified during recording. Otherwise, the video will appear to be slowed down or sped up, and audio will be out of sync with the video.

```gdscript
ffmpeg -r 60 -i input%08d.png -i input.wav -crf 15 output.mp4
```

If you recorded a PNG image sequence with transparency enabled, you need to use a video format that supports storing transparency. MP4/H.264 doesn't support storing transparency, so you can use WebM/VP9 as an alternative:

```gdscript
ffmpeg -r 60 -i input%08d.png -i input.wav -c:v libvpx-vp9 -crf 15 -pix_fmt yuva420p output.webm
```

#### Cutting video

You can trim parts of the video you don't want to keep after the video is recorded. For example, to discard everything before 12.1 seconds and keep only 5.2 seconds of video after that point:

```gdscript
ffmpeg -i input.avi -ss 00:00:12.10 -t 00:00:05.20 -crf 15 output.mp4
```

Cutting videos can also be done with the GUI tool [LosslessCut](https://mifi.github.io/lossless-cut/).

#### Resizing video

The following command resizes a video to be 1080 pixels tall (1080p), while preserving its existing aspect ratio:

```gdscript
ffmpeg -i input.avi -vf "scale=-1:1080" -crf 15 output.mp4
```

#### Reducing framerate

The following command changes a video's framerate to 30 FPS, dropping some of the original frames if there are more in the input video:

```gdscript
ffmpeg -i input.avi -r 30 -crf 15 output.mp4
```

#### Generating accumulation motion blur with FFmpeg

Godot does not have built-in support for motion blur, but it can still be created in recorded videos.

If you record the video at a multiple of the original framerate, you can blend the frames together then reduce the frameate to produce a video with _accumulation motion blur_. This motion blur can look very good, but it can take a long time to generate since you have to render many more frames per second (on top of the time spent on post-processing).

Example with a 240 FPS source video, generating 4× motion blur and decreasing its output framerate to 60 FPS:

```gdscript
ffmpeg -i input.avi -vf "tmix=frames=4, fps=60" -crf 15 output.mp4
```

This also makes effects that converge over several frames (such as temporal antialiasing, SDFGI and volumetric fog) converge faster and therefore look better, since they'll be able to work with more data at a given time. See **Reducing framerate** if you want to get this benefit without adding motion blur.

---
