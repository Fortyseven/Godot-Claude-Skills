# Godot 4 GDScript Tutorials — Xr (Part 2)

> 3 tutorials. GDScript-specific code examples.

## OpenXR hand tracking

### Introduction

> **Note:** This page focuses specifically on the feature set exposed through OpenXR. Parts of the functionality presented here also applies to WebXR and can by provided by other XR interfaces.

When discussing hand tracking it is important to know that there are differences of opinion as to where lines are drawn. The practical result of this is that there are differences in implementation between the different OpenXR runtimes. You may find yourself in a place where chosen hardware doesn't support a piece of the puzzle or does things differently enough from the other platforms that you need to do extra work.

That said, recent improvements to the OpenXR specification are closing these gaps and as platforms implement these improvements we are getting closer to a future where we have either full portability between platforms or at least a clear way to detect the capabilities of a platform.

When we look at the early days of VR the focus of the major platforms was on tracked controller based input. Here we are tracking a physical device that also has buttons for further input. From the tracking data we can infer the location of the player's hands but no further information is known, traditionally it was left up to the game to implement a mechanism to display the player's hand and animate the fingers based on further input from the controller, be it due to buttons being pressed or through proximity sensors. Often fingers are also placed based on context, what the user is holding, and what action a user is performing.

More recently optical hand tracking has become a popular solution, where cameras track the user's hands and full tracking data for the hand and finger positions becomes available. Many vendors saw this as completely separate from controller tracking and introduced independent APIs to access hand and finger positions and orientation data. When handling input, it was up to the game developer to implement a gesture detection mechanism.

This split also exists in OpenXR, where controller tracking is handled primarily by the action map system, while optical hand tracking is primarily handled by the hand tracking API extension.

However, the world is not that black and white and we're seeing a number of scenarios where we cross the line:

- Devices that fit in both categories, such as tracked gloves and controllers such as the Index controller that also perform finger tracking.
- XR Runtimes that implement inferred hand tracking from controller data as a means to solve proper finger placement for multiple controllers.
- XR applications that wish to seamlessly switch between controller and hand tracking offering the same user experience regardless of approach used.

OpenXR is answering this call by introducing further extensions that lets us query the capabilities of the XR runtime/hardware or that add further functionality across this divide. The problem that currently does remain is that there are gaps in adopting these extensions, with some platforms thus not reporting capabilities to their full extent. As such you may need to test for the features available on specific hardware and adjust your approach accordingly.

### Demo project

The information presented on this page was used to create a demo project that can be found [here](https://github.com/godotengine/godot-demo-projects/tree/master/xr/openxr_hand_tracking_demo).

### The Hand Tracking API

As mentioned in our introduction, the hand tracking API is primarily used with optical hand tracking and on many platforms only works when the user is not holding a controller. Some platforms support controller inferred hand tracking meaning that you will get hand tracking data even if the user is holding a controller. This includes SteamVR, Meta Quest (currently native only but Meta link support is likely coming), and hopefully soon others as well.

The hand tracking implementation in Godot has been standardized around the Godot Humanoid Skeleton and works both in OpenXR and WebXR. The instructions below will thus work in both environments.

In order to use the hand tracking API with OpenXR you first need to enable it. This can be done in the project settings:

For some standalone XR devices you also need to configure the hand tracking extension in export settings, for instance for Meta Quest:

Now you need to add 3 components into your scene for each hand:

- A tracked node to position the hand.
- A properly skinned hand mesh with skeleton.
- A skeleton modifier that applies finger tracking data to the skeleton.

#### Hand tracking node

The hand tracking system uses separate hand trackers to track the position of the player's hands within our tracking space.

This information has been separated out for the following use cases:

- Tracking happens in the local space of the [XROrigin3D](../godot_gdscript_misc.md) node. This node must be a child of the XROrigin3D node in order to be correctly placed.
- This node can be used as an IK target when an upper body mesh with arms is used instead of separate hand meshes.
- Actual placement of the hands may be loosely bound to the tracking in scenarios such as avatar creation UIs, fake mirrors, or similar situations resulting in the hand mesh and finger tracking being localized elsewhere.

We'll concentrate on the first use case only.

For this you need to add an [XRNode3D](../godot_gdscript_misc.md) node to your `XROrigin3D` node.

- On this node the `tracker` should be set to `/user/hand_tracker/left` or `/user/hand_tracker/right` for the left or right hand respectively.
- The `pose` should remain set to `default`, no other option will work here.
- The checkbox `Show When Tracked` will automatically hide this node if no tracking data is available, or make this node visible if tracking data is available.

#### Rigged hand mesh

In order to display our hand we need a hand mesh that is properly rigged and skinned. For this Godot uses the hand bone structure as defined for the [Godot Humanoid](../godot_gdscript_misc.md) but optionally supporting an extra tip bone for each finger.

The [OpenXR hand tracking demo](https://github.com/godotengine/godot-demo-projects/tree/master/xr/openxr_hand_tracking_demo) contains example glTF files of properly rigged hands.

We will be using those here and add them as a child to our `XRNode3D` node. We also need to enable editable children to gain access to our [Skeleton3D](../godot_gdscript_nodes_3d.md) node.

#### The hand skeleton modifier

Finally we need to add an [XRHandModifier3D](../godot_gdscript_misc.md) node as a child to our `Skeleton3D` node. This node will obtain the finger tracking data from OpenXR and apply it the hand model.

You need to set the `Hand Tracker` property to either `/user/hand_tracker/left` or `/user/hand_tracker/right` depending on whether we are apply the tracking data of respectively the left or right hand.

You can also set the `Bone Update` mode on this node.

- `Full` applies the hand tracking data fully. This does mean that the skeleton positioning will potentially reflect the size of the actual hand of the user. This can lead to scrunching effect if meshes aren't weighted properly to account for this. Make sure you test your game with players of all sizes when optical hand tracking is used!
- `Rotation Only` will only apply rotation to the bones of the hands and keep the bone length as is. In this mode the size of the hand mesh doesn't change.

With this added, when we run the project we should see the hand correctly displayed if hand tracking is supported.

### The hand tracking data source

This is an OpenXR extension that provides information about the source of the hand tracking data. At this moment only a few runtimes implement it but if it is available, Godot will activate it.

If this extension is not supported and thus unknown is returned, you can make the following assumptions:

- If you are using SteamVR (including Steam link), only controller based hand tracking is supported.
- For any other runtime, if hand tracking is supported, only optical hand tracking is supported (Note, Meta Link currently fall into this category).
- In all other cases, no hand tracking is supported at all.

You can access this information through code:

```gdscript
var hand_tracker : XRHandTracker = XRServer.get_tracker('/user/hand_tracker/left')
if hand_tracker:
    if hand_tracker.has_tracking_data:
        if hand_tracker.hand_tracking_source == XRHandTracker.HAND_TRACKING_SOURCE_UNKNOWN:
            print("Hand tracking source unknown")
        elif hand_tracker.hand_tracking_source == XRHandTracker.HAND_TRACKING_SOURCE_UNOBSTRUCTED:
            print("Hand tracking source is optical hand tracking")
        elif hand_tracker.hand_tracking_source == XRHandTracker.HAND_TRACKING_SOURCE_CONTROLLER:
            print("Hand tracking data is inferred from controller data")
        else:
            print("Unknown hand tracking source ", hand_tracker.hand_tracking_source)
    else:
        print("Hand is currently not being tracked")
else:
    print("No
# ...
```

This example logs the state for the left hand.

If in this example no hand tracker is returned by `get_tracker`, this means the hand tracking API is not supported on the XR runtime at all.

If there is a tracker but has_tracking_data is false, the user's hand is currently not being tracked. This is likely caused by one of the following reasons:

- The player's hand is not visible by any of the tracking cameras on the headset
- The player is currently using a controller and the headset only supports optical hand tracking
- The controller is turned off and only controller hand tracking is supported.

### Handling user input

Reacting to actions performed by the user is handled through The XR action map if controllers are used. In the action map you can map various inputs like the trigger or joystick on the controller to an action. This can then drive logic in your game.

When hand tracking is used we originally had no such inputs, inputs are driven by gestures made by the user such as making a fist to grab or pinching the thumb and index finger together to select something. It was up to the game developer to implement this.

Recognizing that there is an increasing demand for applications that can switch seamlessly between controller and hand tracking and the need some form of basic input capability, a number of extensions were added to the specification that provide some basic gesture recognition and can be used with the action map.

#### The hand interaction profile

The [hand interaction profile extension](https://github.khronos.org/OpenXR-Inventory/extension_support.html#XR_EXT_hand_interaction) is a new core extension which supports pinch, grasp, and poke gestures and related poses. There is still limited support for this extension but it should become available in more runtimes in the near future.

The pinch gesture is triggered by pinching your thumb and index finger together. This is often used as a select gesture for menu systems, similar to using your controller to point at an object and press the trigger to select and is thus often mapped as such.

- The `pinch pose` is a pose positioned in the middle between the tip of the thumb and the tip of the index finger and oriented such that a ray cast can be used to identify a target.
- The `pinch` float input is a value between 0.0 (the tip of the thumb and index finger are apart) and 1.0 (the tip of the thumb and index finger are touching).
- The `pinch ready` input is true when the tips of the fingers are (close to) touching.

The grasp gesture is triggered by making a fist and is often used to pick items up, similar to engaging the squeeze input on controllers.

- The `grasp` float input is a value between 0.0 (open hand) and 1.0 (fist).
- The `grasp ready` input is true when the user made a fist.

The poke gesture is triggered by extending your index finger, this one is a bit of an exception as the pose at the tip of your index finger is often used to poke an interactable object. The `poke pose` is a pose positioned on the tip of the index finger.

Finally the `aim activate (ready)` input is defined as an input that is 1.0/true when the index finger is extended and pointing at a target that can be activated. How runtimes interpret this, is not clear.

With this setup the normal `left_hand` and `right_hand` trackers are used and you can thus seamlessly switch between controller and hand tracking input.

> **Note:** You need to enable the hand interaction profile extension in the OpenXR project settings.

#### Microsoft hand interaction profile

The [Microsoft hand interaction profile extension](https://github.khronos.org/OpenXR-Inventory/extension_support.html#XR_MSFT_hand_interaction) was introduced by Microsoft and loosely mimics the simple controller profile. Meta has also added support for this extension but only on their native OpenXR client, it is currently not available over Meta Link.

Pinch support is exposed through the `select` input, the value of which is 0.0 when the tip of the thumb and index finger are apart and 1.0 when they are together.

Note that in this profile the `aim pose` is redefined as a pose between thumb and index finger, oriented so a ray cast can be used to identify a target.

Grasp support is exposed through the `squeeze` input, the value of which is 0.0 when the hand is open, and 1.0 when a fist is made.

With this setup the normal `left_hand` and `right_hand` trackers are used and you can thus seamlessly switch between controller and hand tracking input.

#### HTC hand interaction profile

The [HTC hand interaction profile extension](https://github.khronos.org/OpenXR-Inventory/extension_support.html#XR_HTC_hand_interaction) was introduced by HTC and is defined similarly to the Microsoft extension. It is only supported by HTC for the Focus 3 and Elite XR headsets.

See the Microsoft hand interaction profile for the gesture support.

The defining difference is that this extension introduces two new trackers, `/user/hand_htc/left` and `/user/hand_htc/right`. This means that extra logic needs to be implemented to switch between the default trackers and the HTC specific trackers when the user puts down, or picks up, their controller.

#### Simple controller profile

The simple controller profile is a standard core profile defined as a fallback profile when a controller is used for which no profile exists.

There are a number of OpenXR runtimes that will mimic controllers through the simple controller profile when hand tracking is used.

Unfortunately there is no sound way to determine whether an unknown controller is used or whether hand tracking is emulating a controller through this profile.

XR runtimes are free to define how the simple controller profile operates, so there is also no certainty to how this profile is mapped to gestures.

The most common mapping seems to be that `select click` is true when the tip of the thumb and index fingers are touching while the user's palm is facing away from the user. `menu click` will be true when tip of the thumb and index fingers are touching while the user's palm is facing towards the user.

With this setup the normal `left_hand` and `right_hand` trackers are used and you can thus seamlessly switch between controller and hand tracking input.

> **Note:** As some of these interaction profiles have overlap it is important to know that you can add each profile to your action map and the XR runtime will choose the best fitting profile. For instance, a Meta Quest supports both the Microsoft hand interaction profile and simple controller profile. If both are specified the Microsoft hand interaction profile will take precedence and will be used. The expectation is that once Meta supports the core hand interaction profile extension, that profile will take precedence over both Microsoft and simple controller profiles.

#### Gesture based input

If the platform doesn't support any interaction profiles when hand tracking is used, or if you're building an application where you need more complicated gesture support you're going to need to build your own gesture recognition system.

You can obtain the full hand tracking data through the [XRHandTracker](../godot_gdscript_misc.md) resource for each hand. You can obtain the hand tracker by calling `XRServer.get_tracker` and using either `/user/hand_tracker/left` or `/user/hand_tracker/left` as the tracker. This resource provides access to all the joint information for the given hand.

Detailing out a full gesture recognition algorithm goes beyond the scope of this manual however there are a number of community projects you can look at:

- [Julian Todd's Auto hands library](https://github.com/Godot-Dojo/Godot-XR-AH)
- [Malcolm Nixons Hand Pose Detector](https://github.com/Malcolmnixon/GodotXRHandPoseDetector)

---

## OpenXR Render Models

A cornerstone of OpenXR's API design is being as platform agnostic as possible. A great example of this is OpenXR's action map system where XR runtimes have to support core interaction profiles to fall back on, if no interaction profile exists for the hardware being used. This ensures that OpenXR applications keep functioning even when used on hardware that didn't exist when the application was released, or that the developers of the application did not have access too.

A consequence of this is that the application developer doesn't know with any certainty what hardware is being used, as the XR runtime could be mimicking other hardware. The application developer thus can't show anything in relation to the actual hardware used, the most common use case being showing the controllers the user is currently holding.

Showing the correct controller models and having these models correctly positioned is important to a proper sense of immersion.

This is where OpenXR's [render models API](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_EXT_render_models) comes in. This API allows us to query the XR runtime for 3D assets that are correct for the physical hardware being used. The API also allows us to query the position of this hardware within the tracking volume and the correct positioning of subcomponents of this hardware.

For instance, we can correctly position and animate the trigger or show buttons being pressed.

For those runtimes that support the [controller data source for hand tracking](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_EXT_hand_tracking_data_source) , we can also correctly position the user's fingers and hand according to the shape of the controller. Do note that this works in combination with the [hand joints motion range extension](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_EXT_hand_joints_motion_range) to prevent clipping of the fingers.

### OpenXR Render models node

The [OpenXRRenderModelManager](../godot_gdscript_misc.md) node can be used to automate most of the render models functionality. This node keeps track of the active render models currently made available by the XR runtime.

It will create child nodes for each active render model resulting in that render model being displayed.

This node must have an [XROrigin3D](../godot_gdscript_misc.md) node as an ancestor.

If `tracker` is set to `Any` our node will show all render models currently being tracked. In this scenario this node must be a direct child of our [XROrigin3D](../godot_gdscript_misc.md) node.

If `tracker` is set to `None set` our node will only show render models for which no tracker has been identified. In this scenario this node must also be a direct child of our [XROrigin3D](../godot_gdscript_misc.md) node.

If `tracker` is set to `Left Hand` or `Right Hand` our node will only show render models related to our left or right hand respectively. In this scenario, our node can be placed deeper in the scene tree.

> **Warning:** For most XR runtimes this means the render model represents a controller that is actually being held by the user but this is not a guarantee. Some XR runtimes will always set the tracker to either the left or right hand even if the controller is not currently held but is being tracked. You should always test this as this will lead to unwanted behavior.

In this scenario we can also specify an action for a pose in the action map by setting the `make_local_to_pose` property to the pose action. Use this in combination with an [XRController3D](../godot_gdscript_misc.md) node that is using the same pose and you can now add a layer that allows you to deviate from the tracked position of both your controller and the related render model (see example below).

> **Note:** Combining the above with hand tracking does introduce the problem that hand tracking is completely independent from the action map system. You will need to combine the hand tracking and controller tracking poses to properly offset the render models. This falls beyond the scope of this documentation.

#### Render model manager example

You can download [our render models demo](https://github.com/godotengine/godot-demo-projects/tree/master/xr/openxr_render_models) which implements the setup described below.

In this setup we find an [OpenXRRenderModelManager](../godot_gdscript_misc.md) node directly underneath our [XROrigin3D](../godot_gdscript_misc.md) node. On this node our `target` property is set to `None set` and will handle showing all render models that are currently not related to our left or right hand controllers.

We then see the same setup for our left and right hand so we'll focus on just the left hand.

We have an [XRController3D](../godot_gdscript_misc.md) that will track the location of our hand.

> **Note:** We are using the `grip` pose in this example. The `palm` pose is arguably more suitable and predictable however it is not supported by all XR runtimes. See the hand tracking demo project for a solution to switching between these poses based on what is supported.

As a child of the node we have an [AnimatableBody3D](../godot_gdscript_nodes_3d.md) node that follows the tracked location of the hand **but** will interact with physics objects to stop the player's hand from going through walls etc. This node has a collision shape that encapsulates the hand.

> **Note:** It is important to set the physics priority so that this logic runs after any physics logic that moves the XROrigin3D node or the hand will lag a frame behind.

The script below shows a basic implementation for this that you can build upon.

```gdscript
class_name CollisionHands3D
extends AnimatableBody3D

func _ready():
    # Make sure these are set correctly.
    top_level = true
    sync_to_physics = false
    process_physics_priority = -90

func _physics_process(_delta):
    # Follow our parent node around.
    var dest_transform = get_parent().global_transform

    # We just apply rotation for this example.
    global_basis = dest_transform.basis

    # Attempt to move to where our tracked hand is.
    move_and_collide(dest_transform.origin - global_position)
```

Finally we see another [OpenXRRenderModelManager](../godot_gdscript_misc.md) node, this one with `target` set to the appropriate hand and `make_local_to_pose` set to the correct pose. This will ensure that the render models related to this hand are properly shown and offset if our collision handler has altered the location.

### Render model node

The [OpenXRRenderModel](../godot_gdscript_misc.md) node implements all the logic to display and position a given render model provided by the render models API.

Instances of this node are added by the render model manager node we used up above but you can interact with these directly if you wish.

Whenever Godot obtains information about a new render model an RID is created to reference that render model.

By assigning that RID to the `render_model` property on this node, the node will start displaying the render model and manage both the transform that places the render model in the correct place and animates all the sub objects.

The `get_top_level_path` function will return the top level path associated with this render model. This will point to either the left or right hand. As the top level path can be set or cleared depending on whether the user picks up, or puts down, the controller you can connect to the `render_model_top_level_path_changes` signal and react to these changes.

Depending on your setup of the [OpenXRRenderModelManager](../godot_gdscript_misc.md) nodes, render models will be removed or added as their top level path changes.

### Backend access

The nodes we've detailed out above handle all the display logic for us but it is possible to interact with the data that drives this directly and create your own implementation.

For this you can access the [OpenXRRenderModelExtension](../godot_gdscript_misc.md) singleton.

This object also lets you query whether render models are supported and enabled on the device currently being used by calling the `is_active` function on this object.

The built-in logic implements the [interaction render model API](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_EXT_interaction_render_model) that lists all render models related to controllers and similar devices that are present in the action map. It will automatically create and remove render model entities that are exposed through this API.

As other extensions become available these can be implemented in a GDExtension plugin. Such a plugin can call `render_model_create` and `render_model_destroy` to create the object that will provide access to that render model through the core render models API.

You should not destroy a render model outside of this logic.

You can connect to the `render_model_added` and `render_model_removed` signals to be informed when new render models are added or removed.

The core methods for working with this API are listed below:

| Function                                   | Description                                                                                                                                          |
| ------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| render_model_get_all                       | Provides an array of RIDs for all render models that are being tracked.                                                                              |
| render_model_new_scene_instance            | Provides a new scene that contains all meshes needed to display the render model.                                                                    |
| render_model_get_subaction_paths           | Provides a list of subaction paths from your action map related to this render mode.                                                                 |
| render_model_get_top_level_path            | Returns the top level path associated with this render model (if any). Use the render_model_top_level_path_changed signal to react to this changing. |
| render_model_get_confidence                | Returns the tracking confidence for the tracking data for this render model.                                                                         |
| render_model_get_root_transform            | Returns the root transform for this render model within our current reference space. This can be used to place the render model in space.            |
| render_model_get_animatable_node_count     | Returns the number of nodes in our render model scene that can be animated                                                                           |
| render_model_get_animatable_node_name      | Returns the name of the node that we can animate. Note that this node can be any number of levels deep within the scene.                             |
| render_model_is_animatable_node_visible    | Returns true if this animatable node should be visible                                                                                               |
| render_model_get_animatable_node_transform | Returns the transform for this animatable node. This is a local transform that can be directly applied.                                              |

---

## OpenXR Settings

OpenXR has its own set of settings that are applied when OpenXR starts. While it is possible for OpenXR extensions implemented through Godot plugins to add additional settings, we will only discuss the settings in the core of Godot here.

### General settings

#### Enabled

This setting enables the OpenXR module when Godot starts. This is required when the Vulkan backend is used. For other backends you can enable OpenXR at any time by calling `initialize` on the [OpenXRInterface](../godot_gdscript_misc.md).

This also needs to be enabled to get access to the action map editor.

You can use the `--xr-mode on` command line switch to force this to on.

#### Default Action Map

This specifies the path of the action map file that OpenXR will load and communicate to the XR Runtime.

#### Form Factor

This specifies whether your game is designed for:

- `Head Mounted` devices such as a Meta Quest, Valve Index, or Magic Leap,
- `Handheld` devices such as phones.

If the device on which you run your game does not match the selection here, OpenXR will fail to initialise.

#### View Configuration

This specifies the view configuration your game is designed for:

- `Mono`, your game provides a single image output. E.g. phone based AR;
- `Stereo`, your game provides stereo image output. E.g. head mounted devices.

If the device on which you run your game does not match the selection here, OpenXR will fail to initialise.

> **Note:** OpenXR has additional view configurations for very specific devices that Godot doesn't support yet. For instance, Varjo headsets have a quad view configuration that outputs two sets of stereo images. These may be supported in the near future.

#### Reference Space

Within XR all elements like the player's head and hands are tracked within a tracking volume. At the base of this tracking volume is our origin point, which maps our virtual space to the real space. There are however different scenarios that place this point in different locations, depending on the XR system used. In OpenXR these scenarios are well defined and selected by setting a reference space.

##### Local

The local reference space places our origin point at the player's head by default. Some XR runtimes will do this each time your game starts, others will make the position persist over sessions.

This reference space however does not prevent the user from walking away so you will need to detect if the user does so if you wish to prevent the user from leaving the vehicle they are controlling, which could potentially be game breaking.

This reference space is the best option for games like flight simulators or racing simulators where we want to place the [XROrigin3D](../godot_gdscript_misc.md) node where the player's head should be.

When the user enacts the recenter option on their headset, the method of which is different per XR runtime, the XR runtime will move the [XRCamera3D](../godot_gdscript_misc.md) to the [XROrigin3D](../godot_gdscript_misc.md) node. The [OpenXRInterface](../godot_gdscript_misc.md) will also emit the `pose_recentered` signal so your game can react accordingly.

> **Note:** Any other XR tracked elements such as controllers or anchors will also be adjusted accordingly.

> **Warning:** You should **not** call `center_on_hmd` when using this reference space.

##### Stage

The stage reference space is our default reference space and places our origin point at the center of our play space. For XR runtimes that allow you to draw out a guardian boundary this location and its orientation is often set by the user. Other XR runtimes may decide on the placement of this point by other means. It is however a stationary point in the real world.

This reference space is the best option for room scale games where the user is expected to walk around a larger space, or for games where there is a need to switch between game modes. See Room Scale for more information.

When the user enacts the recenter option on their headset, the method of which is different per XR runtime, the XR runtime will not change the origin point. The [OpenXRInterface](../godot_gdscript_misc.md) will emit the `pose_recentered` signal and it is up to the game to react appropriately. Not doing so will prevent your game from being accepted on various stores.

In Godot you can do this by calling the `center_on_hmd` function on the [XRServer](../godot_gdscript_misc.md):

- Calling `XRServer.center_on_hmd(XRServer.RESET_BUT_KEEP_TILT, false)` will move the [XRCamera3D](../godot_gdscript_misc.md) node to the [XROrigin3D](../godot_gdscript_misc.md) node similar to the `Local` reference space.
- Calling `XRServer.center_on_hmd(XRServer.RESET_BUT_KEEP_TILT, true)` will move the [XRCamera3D](../godot_gdscript_misc.md) node above the [XROrigin3D](../godot_gdscript_misc.md) node keeping the player's height, similar to the `Local Floor` reference space.

> **Note:** Any other XR tracked elements such as controllers or anchors will also be adjusted accordingly.

##### Local Floor

The local floor reference space is similar to the local reference space as it positions the origin point where the player is. In this mode however the height of the player is kept. Same as with the local reference space, some XR runtimes will persist this location over sessions.

It is thus not guaranteed the player will be standing on the origin point, the only guarantee is that they were standing there when the user last recentered. The player is thus also free to walk away.

This reference space is the best option of games where the user is expected to stand in the same location or for AR type games where the user's interface elements are bound to the origin node and are quickly placed at the player's location on recenter.

When the user enacts the recenter option on their headset, the method of which is different per XR runtime, the XR runtime will move the [XRCamera3D](../godot_gdscript_misc.md) above the [XROrigin3D](../godot_gdscript_misc.md) node but keeping the player's height. The [OpenXRInterface](../godot_gdscript_misc.md) will also emit the `pose_recentered` signal so your game can react accordingly.

> **Warning:** Be careful using this mode in combination with virtual movement of the player. The user recentering in this scenario can be unpredictable unless you counter the move when handling the recenter signal. This can even be game breaking as the effect in this scenario would be the player teleporting to whatever abstract location the origin point was placed at during virtual movement, including the ability for players teleporting into locations that should be off limits. It is better to use the Stage mode in this scenario and limit resetting to orientation only when a `pose_recentered` signal is received.

> **Note:** Any other XR tracked elements such as controllers or anchors will also be adjusted accordingly.

> **Warning:** You should **not** call `center_on_hmd` when using this reference space.

#### Environment Blend Mode

The environment blend mode defines how our rendered output is blended into "the real world" provided this is supported by the headset.

- `Opaque` means our output obscures the real world, we are in VR mode.
- `Additive` means our output is added to the real world, this is an AR mode where optics do not allow us to fully obscure the real world (e.g. Hololens),
- `Alpha` means our output is blended with the real world using the alpha output (viewport should have transparent background enabled), this is an AR mode where optics can fully obscure the real world (Magic Leap, all pass through devices, etc.).

If a mode is selected that is not supported by the headset, the first available mode will be selected.

> **Note:** Some OpenXR devices have separate systems for enabling/disabling passthrough. From Godot 4.3 onwards selecting the alpha blend mode will also perform these extra steps. This does require the latest vendor plugin to be installed.

#### Foveation Level

Sets the foveation level used when rendering provided this feature is supported by the hardware used. Foveation is a technique where the further away from the center of the viewport we render content, the lower resolution we render at. Most XR runtimes only support fixed foveation, but some will take eye tracking into account and use the focal point for this effect.

The higher the level, the better the performance gains, but also the more reduction in quality there is in the user's peripheral vision.

> **Note:** **Compatibility renderer only**, for Mobile and Forward+ renderer, set the `vrs_mode` property on [Viewport](../godot_gdscript_rendering.md) to `VRS_XR`.

> **Warning:** This feature is disabled if post effects are used such as glow, bloom, or DOF.

#### Foveation Dynamic

When enabled the foveation level will be adjusted automatically depending on current GPU load. It will be adjusted between low and the select foveation level in the previous setting. It is therefore best to combine this setting with foveation level set to high.

> **Note:** **Compatibility renderer only**

#### Submit Depth Buffer

If enabled an OpenXR supplied depth buffer will be used while rendering which is submitted alongside the rendered image. The XR runtime can use this for improved reprojection.

> **Note:** Enabling this feature will disable stencil support during rendering. Not many XR runtimes make use of this, it is advised to leave this setting off unless it provides noticeable benefits for your use case.

#### Startup Alert

If enabled, this will result in an alert message presented to the user if OpenXR fails to start. We don't always receive feedback from the XR system as to why starting fails. If we do, we log this to the console. Common failure reasons are:

- No OpenXR runtime is installed on the host system.
- Microsoft's WMR OpenXR runtime is currently active, this only supports DirectX and will fail if OpenGL or Vulkan is used.
- SteamVR is used but no headset is connected/turned on.

Disable this if you support a fallback mode in your game so it can be played in desktop mode when no VR headset is connected, or if you're handling the failure condition yourself by checking `OpenXRInterface.is_initialized()`.

### Extensions

This subsection allows you to enable to various optional OpenXR extensions. Keep in mind that the extensions will only work if the OpenXR runtime (SteamVR, Oculus, etc) the project is ran with supports them.

#### Debug Utils

Enabling this will log debug messages from the XR runtime.

#### Debug Message Types

This allows you to choose which debug messages are logged.

#### Frame Synthesis

When enabled, provided it's supported by the XR runtime, lower resolution motion vector and depth buffers are rendered and provided to the XR runtime. The XR runtime can now inject reprojection frames and compensate for lower framerates.

It currently has the following limitations:

- Does NOT work in the Forward+ renderer.
- Only works with stereo rendering.

#### Hand Tracking

This enables the hand tracking extension when supported by the device used. This is on by default for legacy reasons. The hand tracking extension provides access to data that allows you to visualise the user's hands with correct finger positions. Depending on platform capabilities the hand tracking data can be inferred from controller inputs, come from data gloves, come from optical hand tracking sensors or any other applicable source.

If your game only supports controllers this should be turned off.

See the page on hand tracking for additional details.

#### Hand Tracking Unobstructed Data Source

Enabling this means hand tracking may use the exact position of fingers, usually what a headset camera sees.

#### Hand Tracking Controller Data Source

Enabling this means hand tracking may use the controller itself, and infer where fingers are based on controller input or sensors on the controller.

#### Hand Interaction Profile

Enabling this extension allows the use of two new hand tracking poses. Pinch pose which is the location between the thumb and index finger pointing forward, and poke pose which is at the tip of the index finger.

This also allows 3 more gesture based inputs. Pinch, when the user pinches their thumb and index finger together. Aim activation, when the index finger is fully extended. And Grasps, when the user makes a fist.

When a hand interaction profile and controller interaction profile are supplied, the runtime will switch between profiles depending on if optical tracking is used or if the user is holding a controller.

If only a hand interaction profile is supplied any runtime should use hand interaction even if a controller is being held.

#### Spatial Entities

This extension and its settings are used to obtain and interact with information about the user's real world environment. You can find more detailed information on how it works on the spatial entities page.

#### Eye Gaze Interaction

This enables the eye gaze interaction extension when supported by the device used. When enabled we will get feedback from eye tracking through a pose situated between the user's eyes orientated in the direction the user is looking. This will be a unified orientation.

In order to use this functionality you need to edit your action map and add a new pose action, say `eye_pose`. Now add a new interaction profile for the eye gaze interaction and map the `eye_pose`:

Don't forget to save!

Next add a new [XRController3D](../godot_gdscript_misc.md) node to your origin node and set its `tracker` property to `/user/eyes_ext` and set its `pose` property to `eye_pose`.

Now you can add things to this controller node such as a raycast, and control things with your eyes.

#### Render Models

This extension is used to query the XR runtime for 3D assets of the hardware being used, usually a controller, as well as the position of that hardware. You can find a detailed guide on how to use it here.

### Binding Modifiers

These control whether or not binding modifiers can be used. Binding modifiers are used to apply thresholds or offset values. You can find information on how to use and set them up on the XR action map page here.

#### Analog Threshold

Allow analog threshold binding modifiers.

#### Dpad Binding

Allow D-pad binding modifiers.

---
