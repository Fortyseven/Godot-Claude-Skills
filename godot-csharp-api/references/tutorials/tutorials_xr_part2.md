# Godot 4 C# Tutorials — Xr (Part 2)

> 3 tutorials. C#-specific code examples.

## OpenXR Render Models

A cornerstone of OpenXR's API design is being as platform agnostic as possible. A great example of this is OpenXR's action map system where XR runtimes have to support core interaction profiles to fall back on, if no interaction profile exists for the hardware being used. This ensures that OpenXR applications keep functioning even when used on hardware that didn't exist when the application was released, or that the developers of the application did not have access too.

A consequence of this is that the application developer doesn't know with any certainty what hardware is being used, as the XR runtime could be mimicking other hardware. The application developer thus can't show anything in relation to the actual hardware used, the most common use case being showing the controllers the user is currently holding.

Showing the correct controller models and having these models correctly positioned is important to a proper sense of immersion.

This is where OpenXR's [render models API](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_EXT_render_models) comes in. This API allows us to query the XR runtime for 3D assets that are correct for the physical hardware being used. The API also allows us to query the position of this hardware within the tracking volume and the correct positioning of subcomponents of this hardware.

For instance, we can correctly position and animate the trigger or show buttons being pressed.

For those runtimes that support the [controller data source for hand tracking](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_EXT_hand_tracking_data_source) , we can also correctly position the user's fingers and hand according to the shape of the controller. Do note that this works in combination with the [hand joints motion range extension](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_EXT_hand_joints_motion_range) to prevent clipping of the fingers.

### OpenXR Render models node

The [OpenXRRenderModelManager](../godot_csharp_misc.md) node can be used to automate most of the render models functionality. This node keeps track of the active render models currently made available by the XR runtime.

It will create child nodes for each active render model resulting in that render model being displayed.

This node must have an [XROrigin3D](../godot_csharp_misc.md) node as an ancestor.

If `tracker` is set to `Any` our node will show all render models currently being tracked. In this scenario this node must be a direct child of our [XROrigin3D](../godot_csharp_misc.md) node.

If `tracker` is set to `None set` our node will only show render models for which no tracker has been identified. In this scenario this node must also be a direct child of our [XROrigin3D](../godot_csharp_misc.md) node.

If `tracker` is set to `Left Hand` or `Right Hand` our node will only show render models related to our left or right hand respectively. In this scenario, our node can be placed deeper in the scene tree.

> **Warning:** For most XR runtimes this means the render model represents a controller that is actually being held by the user but this is not a guarantee. Some XR runtimes will always set the tracker to either the left or right hand even if the controller is not currently held but is being tracked. You should always test this as this will lead to unwanted behavior.

In this scenario we can also specify an action for a pose in the action map by setting the `make_local_to_pose` property to the pose action. Use this in combination with an [XRController3D](../godot_csharp_misc.md) node that is using the same pose and you can now add a layer that allows you to deviate from the tracked position of both your controller and the related render model (see example below).

> **Note:** Combining the above with hand tracking does introduce the problem that hand tracking is completely independent from the action map system. You will need to combine the hand tracking and controller tracking poses to properly offset the render models. This falls beyond the scope of this documentation.

#### Render model manager example

You can download [our render models demo](https://github.com/godotengine/godot-demo-projects/tree/master/xr/openxr_render_models) which implements the setup described below.

In this setup we find an [OpenXRRenderModelManager](../godot_csharp_misc.md) node directly underneath our [XROrigin3D](../godot_csharp_misc.md) node. On this node our `target` property is set to `None set` and will handle showing all render models that are currently not related to our left or right hand controllers.

We then see the same setup for our left and right hand so we'll focus on just the left hand.

We have an [XRController3D](../godot_csharp_misc.md) that will track the location of our hand.

> **Note:** We are using the `grip` pose in this example. The `palm` pose is arguably more suitable and predictable however it is not supported by all XR runtimes. See the hand tracking demo project for a solution to switching between these poses based on what is supported.

As a child of the node we have an [AnimatableBody3D](../godot_csharp_nodes_3d.md) node that follows the tracked location of the hand **but** will interact with physics objects to stop the player's hand from going through walls etc. This node has a collision shape that encapsulates the hand.

> **Note:** It is important to set the physics priority so that this logic runs after any physics logic that moves the XROrigin3D node or the hand will lag a frame behind.

The script below shows a basic implementation for this that you can build upon.

Finally we see another [OpenXRRenderModelManager](../godot_csharp_misc.md) node, this one with `target` set to the appropriate hand and `make_local_to_pose` set to the correct pose. This will ensure that the render models related to this hand are properly shown and offset if our collision handler has altered the location.

### Render model node

The [OpenXRRenderModel](../godot_csharp_misc.md) node implements all the logic to display and position a given render model provided by the render models API.

Instances of this node are added by the render model manager node we used up above but you can interact with these directly if you wish.

Whenever Godot obtains information about a new render model an RID is created to reference that render model.

By assigning that RID to the `render_model` property on this node, the node will start displaying the render model and manage both the transform that places the render model in the correct place and animates all the sub objects.

The `get_top_level_path` function will return the top level path associated with this render model. This will point to either the left or right hand. As the top level path can be set or cleared depending on whether the user picks up, or puts down, the controller you can connect to the `render_model_top_level_path_changes` signal and react to these changes.

Depending on your setup of the [OpenXRRenderModelManager](../godot_csharp_misc.md) nodes, render models will be removed or added as their top level path changes.

### Backend access

The nodes we've detailed out above handle all the display logic for us but it is possible to interact with the data that drives this directly and create your own implementation.

For this you can access the [OpenXRRenderModelExtension](../godot_csharp_misc.md) singleton.

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

This setting enables the OpenXR module when Godot starts. This is required when the Vulkan backend is used. For other backends you can enable OpenXR at any time by calling `initialize` on the [OpenXRInterface](../godot_csharp_misc.md).

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

This reference space is the best option for games like flight simulators or racing simulators where we want to place the [XROrigin3D](../godot_csharp_misc.md) node where the player's head should be.

When the user enacts the recenter option on their headset, the method of which is different per XR runtime, the XR runtime will move the [XRCamera3D](../godot_csharp_misc.md) to the [XROrigin3D](../godot_csharp_misc.md) node. The [OpenXRInterface](../godot_csharp_misc.md) will also emit the `pose_recentered` signal so your game can react accordingly.

> **Note:** Any other XR tracked elements such as controllers or anchors will also be adjusted accordingly.

> **Warning:** You should **not** call `center_on_hmd` when using this reference space.

##### Stage

The stage reference space is our default reference space and places our origin point at the center of our play space. For XR runtimes that allow you to draw out a guardian boundary this location and its orientation is often set by the user. Other XR runtimes may decide on the placement of this point by other means. It is however a stationary point in the real world.

This reference space is the best option for room scale games where the user is expected to walk around a larger space, or for games where there is a need to switch between game modes. See Room Scale for more information.

When the user enacts the recenter option on their headset, the method of which is different per XR runtime, the XR runtime will not change the origin point. The [OpenXRInterface](../godot_csharp_misc.md) will emit the `pose_recentered` signal and it is up to the game to react appropriately. Not doing so will prevent your game from being accepted on various stores.

In Godot you can do this by calling the `center_on_hmd` function on the [XRServer](../godot_csharp_misc.md):

- Calling `XRServer.center_on_hmd(XRServer.RESET_BUT_KEEP_TILT, false)` will move the [XRCamera3D](../godot_csharp_misc.md) node to the [XROrigin3D](../godot_csharp_misc.md) node similar to the `Local` reference space.
- Calling `XRServer.center_on_hmd(XRServer.RESET_BUT_KEEP_TILT, true)` will move the [XRCamera3D](../godot_csharp_misc.md) node above the [XROrigin3D](../godot_csharp_misc.md) node keeping the player's height, similar to the `Local Floor` reference space.

> **Note:** Any other XR tracked elements such as controllers or anchors will also be adjusted accordingly.

##### Local Floor

The local floor reference space is similar to the local reference space as it positions the origin point where the player is. In this mode however the height of the player is kept. Same as with the local reference space, some XR runtimes will persist this location over sessions.

It is thus not guaranteed the player will be standing on the origin point, the only guarantee is that they were standing there when the user last recentered. The player is thus also free to walk away.

This reference space is the best option of games where the user is expected to stand in the same location or for AR type games where the user's interface elements are bound to the origin node and are quickly placed at the player's location on recenter.

When the user enacts the recenter option on their headset, the method of which is different per XR runtime, the XR runtime will move the [XRCamera3D](../godot_csharp_misc.md) above the [XROrigin3D](../godot_csharp_misc.md) node but keeping the player's height. The [OpenXRInterface](../godot_csharp_misc.md) will also emit the `pose_recentered` signal so your game can react accordingly.

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

> **Note:** **Compatibility renderer only**, for Mobile and Forward+ renderer, set the `vrs_mode` property on [Viewport](../godot_csharp_rendering.md) to `VRS_XR`.

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

Next add a new [XRController3D](../godot_csharp_misc.md) node to your origin node and set its `tracker` property to `/user/eyes_ext` and set its `pose` property to `eye_pose`.

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

## OpenXR spatial entities

For any sort of augmented reality application you need to access real world information, and be able to track real world locations. OpenXR's spatial entities API was introduced for this exact purpose.

It has a very modular design. The core of the API defines how real world entities are structured, how they are found, and how information about them is stored and accessed.

Various extensions are added on top, which implement specific systems such as marker tracking, plane tracking, and anchors. These are referred to as spatial capabilities.

Each entity that can be handled by the system is broken up into smaller components, which makes it easy to extend the system and add new capabilities.

Vendors have the ability to implement and expose additional capabilities and component types that can be used with the core API. For Godot these can be implemented in extensions. These implementations however fall outside of the scope of this manual.

Finally it is important to note that the spatial entity system makes use of asynchronous functions. This means that you can start a process, and then get informed of it finishing later on.

### Setup

In order to use spatial entities you need to enable the related project settings. You can find these in the OpenXR section:

| Setting                          | Description                                                                                                                                                      |
| -------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Enabled                          | Enables the core of the spatial entities system. This must be enabled for any of the spatial entities systems to work.                                           |
| Enable spatial anchors           | Enables the spatial anchors capability that allow creating and tracking spatial anchors.                                                                         |
| Enable persistent anchors        | Enables the ability to make spatial anchors persistent. This means that their location is stored and can be retrieved in subsequent sessions.                    |
| Enable built-in anchor detection | Enables our built-in anchor detection logic, this will automatically retrieve persistent anchors and adjust the positioning of anchors when tracking is updated. |
| Enable plane tracking            | Enables the plane tracking capability that allows detection of surfaces such as floors, walls, ceilings, and tables.                                             |
| Enable built-in plane detection  | Enables our built-in plane detection logic, this will automatically react to new plane data becoming available.                                                  |
| Enable marker tracking           | Enables our marker tracking capability that allows detection of markers such as QR codes, Aruco markers, and April tags.                                         |
| Enable built-in marker tracking  | Enables our built-in marker detection logic, this will automatically react to new markers being found or markers being moved around the player's space.          |

> **Note:** Note that various XR devices also require permission flags to be set. These will need to be enabled in the export preset settings.

Enabling the different capabilities activates the related OpenXR APIs, but additional logic is needed to interact with this data. For each core system we have built-in logic that can be enabled that will do this for you.

We'll discuss the spatial entities system under the assumption that the built-in logic is enabled first. We will then take a look at the underlying APIs and how you can implement this yourself, however it should be noted that this is often overkill and that the underlying APIs are mostly exposed to allow GDExtension plugins to implement additional capabilities.

### Creating our spatial manager

When spatial entities are detected or created an [OpenXRSpatialEntityTracker](../godot_csharp_misc.md) object is instantiated and registered with the [XRServer](../godot_csharp_misc.md).

Each type of spatial entity will implement its own subclass and we can thus react differently to each type of entity.

Generally speaking we will instance different subscenes for each type of entity. As the tracker objects can be used with [XRAnchor3D](../godot_csharp_misc.md) nodes, these subscenes should have such a node as their root node.

All entity trackers will expose their location through the `default` pose.

We can automate creating these subscenes and adding them to our scene tree by creating a manager object. As all locations are local to the [XROrigin3D](../godot_csharp_misc.md) node, we should create our manager as a child node of our origin node.

Below is the basis of the script that implements our manager logic:

### Spatial anchors

Spatial anchors allow us to map real world locations in our virtual world in such a way that the XR runtime will keep track of these locations and adjust them as needed. If supported, anchors can be made persistent which means the anchors will be recreated in the correct location when your application starts again.

You can think of use cases such as: - placing virtual windows around your space that are recreated when your application restarts - placing virtual objects on your table or on your walls and have them recreated

Spatial anchors are tracked using [OpenXRAnchorTracker](../godot_csharp_misc.md) objects registered with the XRServer.

When needed, the location of the spatial anchor will be updated automatically; the pose on the related tracker will be updated and thus the [XRAnchor3D](../godot_csharp_misc.md) node will reposition.

When a spatial anchor has been made persistent, a Universally Unique Identifier (or UUID) is assigned to the anchor. You will need to store this with whatever information you need to reconstruct the scene. In our example code below we'll simply call `set_scene_path` and `get_scene_path`, but you will need to supply your own implementations for these functions.

In order to create a persistent anchor you need to follow a specific flow: - Create the spatial anchor - Wait until the tracking status changes to `ENTITY_TRACKING_STATE_TRACKING` - Make the anchor persistent - Obtain the UUID and save it

When an existing persistent anchor is found a new tracker is added that has the UUID already set. It is this difference in workflow that allows us to correctly react to new and existing persistent anchors.

> **Note:** If you unpersist an anchor, the UUID is destroyed but the anchor is not removed automatically. You will need to react to the completion of unpersisting an anchor and then clean it up. Also you will get an error if you try to destroy an anchor that is still persistent.

To complete our anchor system we start by creating a scene that we'll set as the scene to instantiate for anchors on our spatial manager node.

This scene should have an [XRAnchor3D](../godot_csharp_misc.md) node as the root but nothing else. We will add a script to it that will load a subscene that contains the actual visual aspect of our anchor so we can create different anchors in our scene. We'll assume the intention is to make these anchors persistent and save the path to this subscene as metadata for our UUID.

With our anchor scene in place we can add a couple of functions to our spatial manager script to create or remove anchors:

> **Note:** There seems to be a bit of magic going on in the code above. Whenever a spatial anchor is created or removed on our anchor capability, the related tracker object is created or destroyed. This results in the spatial manager adding or removing the child scene for this anchor. Hence we can rely on this here.

### Plane tracking

Plane tracking allows us to detect surfaces such as walls, floors, ceilings, and tables in the player's vicinity. This data could come from a room capture performed by the user at any time in the past, or detected live by optical sensors. The plane tracking extension doesn't make a distinction here.

> **Note:** Some XR runtimes do require vendor extensions to enable and/or configure this process but the data will be exposed through this extension.

The code we wrote up above for the spatial manager will already detect our new planes. We do need to set up a new scene and assign that scene to the spatial manager.

The root node for this scene must be an [XRAnchor3D](../godot_csharp_misc.md) node. We'll add a [StaticBody3D](../godot_csharp_nodes_3d.md) node as a child and add a [CollisionShape3D](../godot_csharp_physics.md) and [MeshInstance3D](../godot_csharp_nodes_3d.md) node as children of the static body.

The static body and collision shape will allow us to make the plane interactable.

The mesh instance node allows us to apply a "hole punch" material to the plane, when combined with passthrough this turns our plane into a visual occluder. Alternatively we can assign a material that will visualize the plane for debugging.

We configure this material as the `material_override` material on our MeshInstance3D. For our "hole punch" material, create a [ShaderMaterial](../godot_csharp_rendering.md) and use the following code as the shader code:

```glsl
shader_type spatial;
render_mode unshaded, shadow_to_opacity;

void fragment() {
    ALBEDO = vec3(0.0, 0.0, 0.0);
}
```

We also need to add a script to our scene to ensure our collision and mesh are applied.

If supported by the XR runtime there is additional metadata you can query on the plane tracker object. Of specific note is the `plane_label` property that, if available, identifies the type of surface. Please consult the [OpenXRPlaneTracker](../godot_csharp_misc.md) class documentation for further information.

### Marker tracking

Marker tracking detects specific markers in the real world. These are usually printed images such as QR codes.

The API exposes support for 4 different codes, QR codes, Micro QR codes, Aruco codes, and April tags, however XR runtimes are not required to support them all.

When markers are detected, [OpenXRMarkerTracker](../godot_csharp_misc.md) objects are instantiated and registered with the XRServer.

Our existing spatial manager code already detects these, all we need to do is create a scene with an [XRAnchor3D](../godot_csharp_misc.md) node at the root, save this, and assign it to the spatial manager as the scene to instantiate for markers.

The marker tracker should be fully configured when assigned, so all that is needed is a `_ready` function that reacts to the marker data. Below is a template for the required code:

As we can see, QR Codes provide a data block that is either a string or a byte array. Aruco and April tags provide an ID that is read from the code.

It's up to your use case how best to link the marker data to the scene that needs to be loaded. An example would be to encode the name of the asset you wish to display in a QR code.

### Backend access

For most purposes the core system, along with any vendor extensions, should be what most users would use as provided.

For those who are implementing vendor extensions, or those for whom the built-in logic doesn't suffice, backend access is provided through a set of singleton objects.

These objects can also be used to query what capabilities are supported by the headset in use. We've already added code that checks for these in our spatial manager and spatial anchor code in the sections above.

> **Note:** The spatial entities system will encapsulate many OpenXR entities in resources that are returned as RIDs.

#### Spatial entity core

The core spatial entity functionality is exposed through the [OpenXRSpatialEntityExtension](../godot_csharp_misc.md) singleton.

Specific logic is exposed through capabilities that introduce specialised component types, and give access to specific types of entities, however they all use the same mechanisms for accessing the entity data managed by the spatial entity system.

We'll start by having a look at the individual components that make up the core system.

##### Spatial contexts

A spatial context is the main object through which we query the spatial entities system. Spatial contexts allow us to configure how we interact with one or more capabilities.

It's recommended to create a spatial context for each capability that you wish to interact with, in fact, this is what Godot does for its built-in logic.

We start by setting the capability configuration objects for the capabilities we wish to access. Each capability will enable the components we support for that capability. Settings can determine which components will be enabled. We'll look at these configuration objects in more detail as we look at each supported capability.

Creating a spatial context is an asynchronous action. This means we ask the XR runtime to create a spatial context, and at a point in the future the XR runtime will provide us with the result.

The following script is the start of our example and can be added as a node to your scene. It shows the creation of a spatial context for plane tracking, and sets up our entity discovery.

##### Discovery snapshots

Once our spatial context has been created the XR runtime will start managing spatial entities according to the configuration of the specified capabilities.

In order to find new entities, or to get information about our current entities, we can create a discovery snapshot. This will tell the XR runtime to gather specific data related to all the spatial entities currently managed by the spatial context.

This function is asynchronous as it may take some time to gather this data and offer its results. Generally speaking you will want to perform a discovery snapshot when new entities are found. OpenXR emits an event when there are new entities to be processed, this results in the `spatial_discovery_recommended` signal being emitted by our [OpenXRSpatialEntityExtension](../godot_csharp_misc.md) singleton.

Note in the example code shown above, we're already connecting to this signal and calling the `_on_perform_discovery` method on our node. Let's implement this:

Note that when calling `discover_spatial_entities` we specify a list of components. The discovery query will find any entity that is managed by the spatial context and has at least one of the specified components.

##### Update snapshots

Performing an update snapshot allows us to get updated information about entities we already found previously with our discovery snapshot. This function is synchronous, and is mainly meant to obtain status and positioning data and can be run every frame.

Generally speaking you would only perform update snapshots when it's likely entities change or have a lifetime process. A good example of this are persistent anchors and markers. Consult the documentation about a capability to determine if this is needed.

It is not needed for plane tracking however to complete our example, here is an example of what an update snapshot would look like for plane tracking if we needed one:

Note that in our example here we're using the same `_process_snapshot` function to process the snapshot. This makes sense in most situations. However if the components you've specified when creating the snapshot are different between your discovery snapshot and your update snapshot, you have to take the different components into account.

##### Querying snapshots

Once we have a snapshot we can run queries over that snapshot to obtain the data held within. The snapshot is guaranteed to remain unchanged until you free it.

For each component we've added to our snapshot we have an accompanying data object. This data object has a double function, adding it to your query ensures we query that component type, and it is the object into which the queried data is loaded.

There is one special data object that must always be added to our request list as the very first entry and that is [OpenXRSpatialQueryResultData](../godot_csharp_misc.md). This object will hold an entry for every returned entity with its unique ID and the current state of the entity.

Completing our discovery logic we add the following:

> **Note:** In the above example we're relying on `ENTITY_TRACKING_STATE_STOPPED` to clean up spatial entities that are no longer being tracked. This is only available with update snapshots. For capabilities that only rely on discovery snapshots you may wish to do a cleanup based on entities that are no longer part of the snapshot instead of relying on the state change.

##### Spatial entities

With the above information we now know how to query our spatial entities and get information about them, but there is a little more we need to look at when it comes to the entities themselves.

In theory we're getting all our data from our snapshots, however OpenXR has an extra API where we create a spatial entity object from our entity ID. While this object exists the XR runtime knows that we are using this entity and that the entity is not cleaned up early. This is a prerequisite for performing an update query on this entity.

In our example code we do so by calling `OpenXRSpatialEntityExtension.make_spatial_entity`.

Some spatial entity APIs will automatically create the object for us. In this case we need to call `OpenXRSpatialEntityExtension.add_spatial_entity` to register the created object with our implementation.

Both functions return an RID that we can use in further functions that require our entity object.

When we're done we can call `OpenXRSpatialEntityExtension.free_spatial_entity`.

Note that we didn't do so in our example code. This is automatically handled when our [OpenXRSpatialEntityTracker](../godot_csharp_misc.md) instance is destroyed.

#### Spatial anchor capability

Spatial anchors are managed by our [OpenXRSpatialAnchorCapability](../godot_csharp_misc.md) singleton object. After the OpenXR session has been created you can call `OpenXRSpatialAnchorCapability.is_spatial_anchor_supported` to check if the spatial anchor feature is supported on your hardware.

The spatial anchor capability breaks the mold a little from what we've shown above.

The spatial anchor system allows us to identify, track, persist, and share a physical location. What makes this different is that we're creating and destroying the anchor and are thus managing its lifecycle.

We thus only use the discovery system to discover anchors created and persisted in previous sessions, or anchors shared with us.

> **Note:** Sharing of anchors is currently not supported in the spatial entities specification.

As we showed in our example before we always start with creating a spatial context but now using the [OpenXRSpatialCapabilityConfigurationAnchor](../godot_csharp_misc.md) configuration object. We'll show an example of this code after we discuss persistence scopes. First we'll look at managing local anchors.

There is no difference in creating spatial anchors from what we've discussed around the built-in logic. The only important thing is to pass your own spatial context as a parameter to `OpenXRSpatialAnchorCapability.create_new_anchor`.

Making an anchor persistent requires you to wait until the anchor is tracking, this means that you must perform update queries for any anchor you create so you can process state changes.

In order to enable making anchors persistent you also have to set up a persistence scope. In the core of OpenXR two types of persistence scopes are supported:

| Enum                             | Description                                                                                                                                                                                                                                                                                         |
| -------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| PERSISTENCE_SCOPE_SYSTEM_MANAGED | Provides the application with read-only access (i.e. applications cannot modify this store) to spatial entities persisted and managed by the system. The application can use the UUID in the persistence component for this store to correlate entities across spatial contexts and device reboots. |
| PERSISTENCE_SCOPE_LOCAL_ANCHORS  | Persistence operations and data access is limited to spatial anchors, on the same device, for the same user and app (using persist_anchor and unpersist_anchor functions)                                                                                                                           |

We'll start with a new script that handles our spatial anchors. It will be similar to the script presented earlier but with a few differences.

The first being the creation of our persistence scope.

With our persistence scope created, we can now create our spatial context.

Creating our discovery snapshot for our anchors is nearly the same as we did before, however it only makes sense to create our snapshot for persistent anchors. We already know the anchors we created during our session, we just want access to those coming from the XR runtime.

We also want to perform regular update queries, here we are only interested in the state so we do want to process our snapshot slightly differently.

The anchor system gives us access to two components:

| Component                  | Data class                            | Description                                                       |
| -------------------------- | ------------------------------------- | ----------------------------------------------------------------- |
| COMPONENT_TYPE_ANCHOR      | OpenXRSpatialComponentAnchorList      | Provides us with the pose (location + orientation) of each anchor |
| COMPONENT_TYPE_PERSISTENCE | OpenXRSpatialComponentPersistenceList | Provides us with the persistence state and UUID of each anchor    |

Finally we can process our snapshot. Note that we are using [OpenXRAnchorTracker](../godot_csharp_misc.md) as our tracker class as this already has all the support for anchors built in.

#### Plane tracking capability

Plane tracking is handled by the [OpenXRSpatialPlaneTrackingCapability](../godot_csharp_misc.md) singleton class.

After the OpenXR session has been created you can call `OpenXRSpatialPlaneTrackingCapability.is_supported` to check if the plane tracking feature is supported on your hardware.

While we've provided most of the code for plane tracking up above, we'll present the full implementation below as it has a few small tweaks. There is no need to update snapshots here, we just do our discovery snapshot and implement our process function.

Plane tracking gives access to two components that are guaranteed to be supported, and three optional components.

| Component                           | Data class                                   | Description                                                             |
| ----------------------------------- | -------------------------------------------- | ----------------------------------------------------------------------- |
| COMPONENT_TYPE_BOUNDED_2D           | OpenXRSpatialComponentBounded2DList          | Provides us with the center pose and bounding rectangle for each plane. |
| COMPONENT_TYPE_PLANE_ALIGNMENT      | OpenXRSpatialComponentPlaneAlignmentList     | Provides us with the alignment of each plane                            |
| COMPONENT_TYPE_MESH_2D              | OpenXRSpatialComponentMesh2DList             | Provides us with a 2D mesh that shapes each plane                       |
| COMPONENT_TYPE_POLYGON_2D           | OpenXRSpatialComponentPolygon2DList          | Provides us with a 2D polygon that shapes each plane                    |
| COMPONENT_TYPE_PLANE_SEMANTIC_LABEL | OpenXRSpatialComponentPlaneSemanticLabelList | Provides us with a type identification of each plane                    |

Our plane tracking configuration object already enables all supported components, but we'll need to interrogate it so we'll store our instance in a member variable. We can use our [OpenXRPlaneTracker](../godot_csharp_misc.md) tracker object to store our component data.

#### Marker tracking capability

Marker tracking is handled by the [OpenXRSpatialMarkerTrackingCapability](../godot_csharp_misc.md) singleton class.

Marker tracking works similarly to plane tracking, however we're now tracking specific entities in the real world based on some code printed on an object like a piece of paper.

There are various different marker tracking options. OpenXR supports 4 out of the box, the following table provides more information and the function name with which to check if your headset supports a given option:

| Option        | Check for support         | Configuration object                            |
| ------------- | ------------------------- | ----------------------------------------------- |
| April tag     | april_tag_is_supported    | OpenXRSpatialCapabilityConfigurationAprilTag    |
| Aruco         | aruco_is_supported        | OpenXRSpatialCapabilityConfigurationAruco       |
| QR code       | qrcode_is_supported       | OpenXRSpatialCapabilityConfigurationQrCode      |
| Micro QR code | micro_qrcode_is_supported | OpenXRSpatialCapabilityConfigurationMicroQrCode |

Each option has its own configuration object that you can use when creating a spatial entity.

QR codes allow you to encode a string which is decoded by the XR runtime and accessible when a marker is found. With April tags and Aruco markers, binary data is encoded which you again can access when a marker is found, however you need to configure the detection with the correct decoding format.

As an example we'll create a spatial context that will find QR codes and Aruco markers.

Every marker regardless of typer will consist of two components:

| Component                 | Data class                          | Description                                                                                 |
| ------------------------- | ----------------------------------- | ------------------------------------------------------------------------------------------- |
| COMPONENT_TYPE_MARKER     | OpenXRSpatialComponentMarkerList    | Provides us with the type, ID (Aruco and April Tag), and/or data (QR Code) for each marker. |
| COMPONENT_TYPE_BOUNDED_2D | OpenXRSpatialComponentBounded2DList | Provides us with the center pose and bounding rectangle for each plane.                     |

We add our discovery implementation:

And we add our update functionality:

---
