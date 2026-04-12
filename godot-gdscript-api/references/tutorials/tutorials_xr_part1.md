# Godot 4 GDScript Tutorials — Xr (Part 1)

> 7 tutorials. GDScript-specific code examples.

## A better XR start script

In Setting up XR we introduced a startup script that initialises our setup which we used as our script on our main node. This script performs the minimum steps required for any given interface.

When using OpenXR there are a number of improvements we should do here. For this we've created a more elaborate starting script. You will find these used in our demo projects.

Alternatively, if you are using XR Tools (see Introducing XR tools) it contains a version of this script updated with some features related to XR tools.

Below we will detail out the script used in our demos and explain the parts that are added.

### Signals for our script

We are introducing 3 signals to our script so that our game can add further logic:

- `focus_lost` is emitted when the player takes off their headset or when the player enters the menu system of the headset.
- `focus_gained` is emitted when the player puts their headset back on or exits the menu system and returns to the game.
- `pose_recentered` is emitted when the headset requests the player's position to be reset.

Our game should react accordingly to these signals.

```gdscript
extends Node3D

signal focus_lost
signal focus_gained
signal pose_recentered

...
```

### Variables for our script

We introduce a few new variables to our script as well:

- `maximum_refresh_rate` will control the headsets refresh rate if this is supported by the headset.
- `xr_interface` holds a reference to our XR interface, this already existed but we now type it to get full access to our [XRInterface](../godot_gdscript_misc.md) API.
- `xr_is_focussed` will be set to true whenever our game has focus.

```gdscript
...

@export var maximum_refresh_rate : int = 90

var xr_interface : OpenXRInterface
var xr_is_focussed = false

...
```

### Our updated ready function

We add a few things to the ready function.

If we're using the mobile or forward+ renderer we set the viewport's `vrs_mode` to `VRS_XR`. On platforms that support this, this will enable foveated rendering.

If we're using the compatibility renderer, we check if the OpenXR foveated rendering settings are configured and if not, we output a warning. See OpenXR Settings for further details.

We hook up a number of signals that will be emitted by the [XRInterface](../godot_gdscript_misc.md). We'll provide more detail about these signals as we implement them.

We also quit our application if we couldn't successfully initialise OpenXR. Now this can be a choice. If you are making a mixed mode game you setup the VR mode of your game on success, and setup the non-VR mode of your game on failure. However, when running a VR only application on a standalone headset, it is nicer to exit on failure than to hang the system.

```gdscript
...

# Called when the node enters the scene tree for the first time.
func _ready():
    xr_interface = XRServer.find_interface("OpenXR")
    if xr_interface and xr_interface.is_initialized():
        print("OpenXR instantiated successfully.")
        var vp : Viewport = get_viewport()

        # Enable XR on our viewport
        vp.use_xr = true

        # Make sure v-sync is off, v-sync is handled by OpenXR
        DisplayServer.window_set_vsync_mode(DisplayServer.VSYNC_DISABLED)

        # Enable VRS
        if RenderingServer.get_rendering_device():
            vp.vrs_mode = Viewport.VRS_XR
        elif int(ProjectSettings.get_setting("xr/openxr/foveation_level")) == 0:
            push_warning("OpenXR: Recommend setting Foveation level to High in Project Settings")

        # Connect
# ...
```

### On session begun

This signal is emitted by OpenXR when our session is setup. This means the headset has run through setting everything up and is ready to begin receiving content from us. Only at this time various information is properly available.

The main thing we do here is to check our headset's refresh rate. We also check the available refresh rates reported by the XR runtime to determine if we want to set our headset to a higher refresh rate.

Finally we match our physics update rate to our headset update rate. Godot runs at a physics update rate of 60 updates per second by default while headsets run at a minimum of 72, and for modern headsets often up to 144 frames per second. Not matching the physics update rate will cause stuttering as frames are rendered without objects moving.

```gdscript
...

# Handle OpenXR session ready
func _on_openxr_session_begun() -> void:
    # Get the reported refresh rate
    var current_refresh_rate = xr_interface.get_display_refresh_rate()
    if current_refresh_rate > 0:
        print("OpenXR: Refresh rate reported as ", str(current_refresh_rate))
    else:
        print("OpenXR: No refresh rate given by XR runtime")

    # See if we have a better refresh rate available
    var new_rate = current_refresh_rate
    var available_rates : Array = xr_interface.get_available_display_refresh_rates()
    if available_rates.size() == 0:
        print("OpenXR: Target does not support refresh rate extension")
    elif available_rates.size() == 1:
        # Only one available, so use it
        new_rate = available_rates[0]
    else:
        for rate in av
# ...
```

### On visible state

This signal is emitted by OpenXR when our game becomes visible but is not focused. This is a bit of a weird description in OpenXR but it basically means that our game has just started and we're about to switch to the focused state next, that the user has opened a system menu or the user has just took their headset off.

On receiving this signal we'll update our focused state, we'll change the process mode of our node to disabled which will pause processing on this node and its children, and emit our `focus_lost` signal.

If you've added this script to your root node, this means your game will automatically pause when required. If you haven't, you can connect a method to the signal that performs additional changes.

> **Note:** While your game is in visible state because the user has opened a system menu, Godot will keep rendering frames and head tracking will remain active so your game will remain visible in the background. However controller and hand tracking will be disabled until the user exits the system menu.

```gdscript
...

# Handle OpenXR visible state
func _on_openxr_visible_state() -> void:
    # We always pass this state at startup,
    # but the second time we get this it means our player took off their headset
    if xr_is_focussed:
        print("OpenXR lost focus")

        xr_is_focussed = false

        # pause our game
        get_tree().paused = true

        emit_signal("focus_lost")

...
```

### On focussed state

This signal is emitted by OpenXR when our game gets focus. This is done at the completion of our startup, but it can also be emitted when the user exits a system menu, or put their headset back on.

Note also that when your game starts while the user is not wearing their headset, the game stays in 'visible' state until the user puts their headset on.

> **Warning:** It is thus important to keep your game paused while in visible mode. If you don't the game will keep on running while your user isn't interacting with your game. Also when the game returns to the focused mode, suddenly all controller and hand tracking is re-enabled and could have game breaking consequences if you do not react to this accordingly. Be sure to test this behavior in your game!

While handling our signal we will update the focuses state, unpause our node and emit our `focus_gained` signal.

```gdscript
...

# Handle OpenXR focused state
func _on_openxr_focused_state() -> void:
    print("OpenXR gained focus")
    xr_is_focussed = true

    # unpause our game
    get_tree().paused = false

    emit_signal("focus_gained")

...
```

### On stopping state

This signal is emitted by OpenXR when we enter our stop state. There are some differences between platforms when this happens. On some platforms this is only emitted when the game is being closed. But on other platforms this will also be emitted every time the player takes off their headset.

For now this method is only a place holder.

```gdscript
...

# Handle OpenXR stopping state
func _on_openxr_stopping() -> void:
    # Our session is being stopped.
    print("OpenXR is stopping")

...
```

### On pose recentered

This signal is emitted by OpenXR when the user requests their view to be recentered. Basically this communicates to your game that the user is now facing forward and you should re-orient the player so they are facing forward in the virtual world.

As doing so is dependent on your game, your game needs to react accordingly.

All we do here is emit the `pose_recentered` signal. You can connect to this signal and implement the actual recenter code. Often it is enough to call [center_on_hmd()](../godot_gdscript_misc.md).

```gdscript
...

# Handle OpenXR pose recentered signal
func _on_openxr_pose_recentered() -> void:
    # User recentered view, we have to react to this by recentering the view.
    # This is game implementation dependent.
    emit_signal("pose_recentered")
```

And that finished our script. It was written so that it can be re-used over multiple projects. Just add it as the script on your main node (and extend it if needed) or add it on a child node specific for this script.

---

## AR / Passthrough

Augmented Reality is supported through various methods depending on the capabilities of the hardware.

Headsets such as the Magic Leap and glasses such as TiltFive show the rendered result on [see-through displays](https://en.wikipedia.org/wiki/See-through_display) allowing the user to see the real world.

Headsets such as the Quest, HTC Elite, and Lynx R1 implement this through a technique called video passthrough, where cameras record the real world and these images are used as the background on top of which our rendered result is used.

> **Note:** Passthrough is implemented very differently across platforms. In Godot 4.3 we have implemented a unified approach that is explained on this help page so you don't need to worry about these differences, the [XRInterface](../godot_gdscript_misc.md) implementation is now responsible for applying the correct platform-dependent method **[1]**. For headsets such as the Meta Quest and HTC Elite you will need to use the [OpenXR vendors plugin v3.0.0](https://github.com/GodotVR/godot_openxr_vendors/releases) or later to enable video passthrough. For backwards compatibility the old API for passthrough is still available but it is recommended to follow the new instructions below.

### Environment blend modes

The way we configure VR or AR functionality is through setting the environment blend mode. This mode determines how the (real world) environment is blended with the virtual world.

| Blend mode                    | Description                                                                                                                                                                                                                                                                            |
| ----------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| XR_ENV_BLEND_MODE_OPAQUE      | The rendered image is opaque, we do not see the real world. We're in VR mode. This will turn off passthrough if video-passthrough is used.                                                                                                                                             |
| XR_ENV_BLEND_MODE_ADDITIVE    | The rendered image is added to the real world and will look semi transparent. This mode is generally used with see-through devices that are unable to obscure the real world. This will turn on passthrough if video-passthrough is used.                                              |
| XR_ENV_BLEND_MODE_ALPHA_BLEND | The rendered image is alpha blended with the real world. On see-through devices that support this, the alpha will control the translucency of the optics. On video-passthrough devices alpha blending is applied with the video image. passthrough will also be enabled if applicable. |

You can set the environment blend mode for your application through the `environment_blend_mode` property of the [XRInterface](../godot_gdscript_misc.md) instance.

You can query the supported blend modes on the hardware using the `get_supported_environment_blend_modes` property on the same instance.

### Configuring your background

When setting the blend mode to `XR_ENV_BLEND_MODE_ALPHA_BLEND` you must set the `transparent_bg` property on [Viewport](../godot_gdscript_rendering.md) to true. When using the `XR_ENV_BLEND_MODE_ADDITIVE` blend mode you should set your background color to black.

Either solution will result in the background rendering not contributing to lighting. It is thus also recommended you adjust your environment settings accordingly and ensure there is adequate ambient light set to illuminate your scene.

> **Note:** Some AR SDKs do provide ambient lighting information or even provide a full radiance map to allow for real world reflections in your virtual objects. The core Godot XR functionality doesn't currently have support for this, however this functionality can be exposed through plugins.

### OpenXR specific

In OpenXR you can configure the default blend mode you want to use. Godot will select this blend mode at startup if available. If not available Godot will default to the first supported blend mode provided by the XR runtime.

For passthrough devices OpenXR requires additional settings to be configured. These settings are platform-dependent and provided through the OpenXR vendors plugin.

For example, these are the settings required on Meta Quest:

The `Passthrough` setting defines whether passthrough is supported or even required.

The `Boundary Mode` allows you to define whether the guardian is needed, disabling this fully requires passthrough to be enabled at all times.

### Putting it together

Putting the above together we can use the following code as a base:

```gdscript
@onready var viewport : Viewport = get_viewport()
@onready var environment : Environment = $WorldEnvironment.environment

func switch_to_ar() -> bool:
    var xr_interface: XRInterface = XRServer.primary_interface
    if xr_interface:
        var modes = xr_interface.get_supported_environment_blend_modes()
        if XRInterface.XR_ENV_BLEND_MODE_ALPHA_BLEND in modes:
            xr_interface.environment_blend_mode = XRInterface.XR_ENV_BLEND_MODE_ALPHA_BLEND
            viewport.transparent_bg = true
        elif XRInterface.XR_ENV_BLEND_MODE_ADDITIVE in modes:
            xr_interface.environment_blend_mode = XRInterface.XR_ENV_BLEND_MODE_ADDITIVE
            viewport.transparent_bg = false
    else:
        return false

    environment.background_mode = Environment.BG_COLOR
    environm
# ...
```

### Shadow to opacity

Shadow to opacity is a render mode for Godot spatial shaders that was introduced in Godot 3 specifically for AR. It is a special render mode where the more a surface is in shadow, the more opaque the surface becomes. When a surface is fully lit, the surface becomes fully transparent and thus shows the real world.

However the surface is rendered during the opaque state effectively. This has two consequences:

- As both the depth buffer and color buffer are written to, we occlude any geometry behind our surface even when fully transparent.
- As we are making the surface opaque if in shadow, we can have virtual objects cast shadows on real world objects **[2]**.

This enabled the following use cases:

- You can render a box mesh around a real world table, this ensures the table remains visible even if a virtual object is placed underneath it. The virtual object will be correctly occluded. Placing a virtual object on top of the real world table, will result in a shadow being cast on the table.
- You can use a shader with this render mode when render a hand mesh using the hand tracking functionality, and ensure your hands properly occlude virtual objects.

The following shader code is a good base for this functionality:

```glsl
shader_type spatial;
render_mode blend_mix, depth_draw_opaque, cull_back, shadow_to_opacity;

void fragment() {
    ALBEDO = vec3(0.0, 0.0, 0.0);
}
```

[**1**]

Restrictions may apply depending on XR interface implementation.

[**2**]

This feature is still being perfected.

---

## Basic XR Locomotion

For basic locomotion we're going to continue using our Godot XR Tools library. The library contains both basic movement features as more advanced features.

### Adding our player body

The first step we need to do is to add a helper node to our [XROrigin3D](../godot_gdscript_misc.md) node. Because XR supports roomscale tracking you can't simply add your XR setup to a [CharacterBody3D](../godot_gdscript_nodes_3d.md) node and expect things to work. You will run into trouble when the user moves around their physical space and is no longer standing in the center of their room. Godot XR Tools embeds the needed logic into a helper node called `PlayerBody`.

Select your [XROrigin3D](../godot_gdscript_misc.md) node and click on the Instantiate Child Scene button to add a child scene. Select `addons/godot-xr-tools/player/player_body.tscn` and add this node.

### Adding a floor

This node governs the in game movement of your character and will immediately react to gravity. So to prevent our player from infinitely falling down we'll quickly add a floor to our scene.

We start by adding a [StaticBody3D](../godot_gdscript_nodes_3d.md) node to our root node and we rename this to `Floor`. We add a [MeshInstance3D](../godot_gdscript_nodes_3d.md) node as a child node for our `Floor`. Then create a new [PlaneMesh](../godot_gdscript_rendering.md) as its mesh. For now we set the size of the mesh to 100 x 100 meters. Next we add a [CollisionShape3D](../godot_gdscript_physics.md) node as a child node for our `Floor`. Then create a `BoxShape` as our shape. We set the size of this box shape to 100 x 1 x 100 meters. We also need to move our collision shape down by 0.5 meters so the top of our box is flush with the floor.

To make it easier to see that we're actually moving around our world, a white floor isn't going to do it. Create a texture using [Wahooneys excellent free texture generator](https://wahooney.itch.io/texture-grid-generator). Once you've created the texture add it to your project. Then create a new material for the MeshInstance3D node, add your texture as the albedo, and enable **Triplaner** under **UV1** in the material properties.

### Direct movement

We're going to start adding some basic direct movement to our setup. This allows the user to move through the virtual world using joystick input.

> **Note:** It is important to note that moving through the virtual world while the player is standing still in the real world, can be nausea inducing especially for players who are new to VR. The default settings on our movement functions are fairly conservative. We advise you to stick to these defaults but offer features in game to enable less comfortable settings for more experienced users who are used to playing VR games.

We want to enable this on the right hand controller. We do this by adding a subscene to the right hand [XRController3D](../godot_gdscript_misc.md) node. Select `addons/godot-xr-tools/functions/movement_direct.tscn` as the scene to add.

This function adds forward and backwards movement to the player by using the joystick on the right hand controller. It has an option to also add left/right strafe but by default this is disabled.

Instead, we are going to add the ability for the player to also turn with this joystick. We will add another subscene to our controller node, select `addons/godot-xr-tools/functions/movement_turn.tscn` for this.

The turn system by default uses a snap turn approach. This means that turning happens in steps. This may seem jarring however it is a tried and tested method of combating motion sickness. You can easily switch to a mode that offers smooth turning by changing the `mode` property on the turn node.

If you run your game at this point in time you will find that you can move through the world freely using the right hand joystick.

### Teleport

An alternative to direct movement that some users find more pleasant is the ability to teleport to another location within your game world. Godot XR Tools supports this through the teleport function and we will be adding this to our left hand controller.

Add a new child scene to your left hand [XRController3D](../godot_gdscript_misc.md) node by selecting the `addons/godot-xr-tools/functions/function_teleport.tscn` scene.

With this scene added the player will be able to teleport around the world by pressing the trigger on the left hand controller, pointing where they want to go, and then releasing the trigger. The player can also adjust the orientation by using the left hand controller's joystick.

If you've followed all instructions correctly your scene should now look something like this:

### More advanced movement features

Godot XR Tools adds many more movement features such as gliding, a grapple hook implementation, a jetpack, climbing mechanics, etc.

Most work similarly to the basic movement features we've handled so far, simply add the relevant subscene from the plugin to the controller that implements it.

We'll look at some of these in more detail later on in this tutorial where additional setup is required (such as climbing) but for others please look at Godot XR Tools own help pages for details.

---

## Deploying to Android

### Setup

Most standalone headsets run on Android and OpenXR support is making its way to these platforms.

Before following the OpenXR-specific instructions here, you'll need to first setup your system to export to Android in general, including:

- Installing OpenJDK 17
- Installing Android Studio
- Configuring the location of the Android SDK in Godot

See [Exporting for Android](tutorials_export.md) for the full details, and return here when you've finished these steps.

> **Warning:** While the Mobile Vulkan renderer has many optimizations targeted at mobile devices, we're still working out the kinks. It is highly advisable to use the compatibility renderer (OpenGL) for the time being when targeting Android based XR devices.

### Gradle Android build

> **Note:** Official support for the Android platform wasn't added to the OpenXR specification initially resulting in various vendors creating custom loaders to make OpenXR available on their headsets. While the long term expectation is that all vendors will adopt the official OpenXR loader, for now these loaders need to be added to your project.

In order to include the vendor-specific OpenXR loader into your project, you will need to setup a gradle Android build.

Select **Install Android Build Template...** from the **Project** menu:

This will create a folder called **android** inside of your project that contains all the runtime files needed on Android. You can now customize this installation. Godot won't show this in the editor but you can find it with a file browser.

You can read more about gradle builds here: [Gradle builds for Android](tutorials_export.md).

### Installing the vendors plugin

The vendors plugin can be downloaded from the asset library, search for "OpenXR vendors" and install the one named "Godot OpenXR Vendors plugin v4".

You will find the installed files inside the **addons** folder. Alternatively you can manually install the vendors plugin by downloading it [from the release page here](https://github.com/GodotVR/godot_openxr_vendors/releases). You will need to copy the assets/addons/godotopenxrvendors folder from the zip file into your projects addons folder.

You can find the main repository of the vendors plugin [here](https://github.com/GodotVR/godot_openxr_vendors).

> **Note:** From Godot 4.6 onwards, the vendor plugin is now an optional but recommended plugin. Godot can export directly to most Android-compatible devices. This can be useful for demonstration and tutorial projects where a single APK can be deployed to multiple devices. The vendor plugin unlocks vendor specific implementations and settings, and may be required to release on app stores.

### Creating the export presets

You will need to setup a separate export preset for each device, as each device will need its own loader included.

Open **Project** and select **Export..**. Click on **Add..** and select **Android**. Next change the name of the export preset for the device you're setting this up for, say **Meta Quest**. And enable **Use Gradle Build**. Next change the **XR Mode** to **OpenXR**. If you want to use one-click deploy (described below), ensure that **Runnable** is enabled.

If you've installed the vendor plugin you will also find entries for the different headsets under **XR Features**. Select the entry for your headset, if you see one. Otherwise, enable the Khronos plugin.

Scroll to the bottom of the list and you'll find additional XR feature sections, currently only **Meta XR Features**, **Pico XR Features**, **Magicleap XR Features** and **Khronos XR Features** for HTC are available. You will need to select the appropriate settings if you wish to use these features.

### Running on your device from the Godot editor

If you've setup your export settings as described above, and your headset is connected to your computer and correctly recognized, you can launch it directly from the Godot editor using [One-click deploy](tutorials_export.md):

For some devices on some platforms, you may need to perform some extra steps in order for your device to be recognized correctly, so be sure to check the developer documentation from your headset vendor.

For example, with the Meta Quest 2, you need to enable developer mode on the headset, and if you're on Windows, you'll need to install special ADB drivers. See the [official Meta Quest developer documentation](https://developer.oculus.com/documentation/native/android/mobile-device-setup/) for more details.

If you're having any issues with one-click deploy, check the [Troubleshooting section](tutorials_export.md).

---

## Introducing XR tools

Out of the box Godot gives you all the basic support to setup an XR project. XR specific game mechanics however need to be implemented on top of this foundation. While Godot makes this relatively easy this can still be a daunting task.

For this reason Godot has developed a toolkit called [Godot XR Tools](https://github.com/GodotVR/godot-xr-tools) that implements many of the basic mechanics found in XR games, from locomotion to object interaction to UI interaction.

This toolkit is designed to work with both OpenXR and WebXR runtimes. We'll be using this as a base for our documentation here. It helps developers hit the ground running but for more specific use cases building your own logic is just as valid. In that case XR tools can help in providing inspiration.

### Installing XR Tools

Continuing on from our project we started in Setting up XR we want to add in the Godot XR Tools library. This can be downloaded from the [Godot XR Tools releases page](https://github.com/GodotVR/godot-xr-tools/releases). Find the latest release for Godot 4, and under **Assets**, download the `godot-xr-tools.zip` file. You can also find it in the asset library with the title "Godot XR Tools for Godot 4".

If you're using the zip file, once it's downloaded unzip it. You will notice the files are held within a `godot-xr-tools` subfolder. Inside of this folder you will find an `addons` folder. It is this folder that you want to copy in its entirety to your Godot project folder. Your project should now look something like this:

Now open up your project in Godot, if you haven't already, and give it a minute or so to import all the resources of the plugin. If it asks for a path to Blender to be set you can just click the option to disable blender import and restart the editor.

After the import finishes you may notice that several "failed to load script" messages popped up, that's normal, the plugin just needs to be enabled in the project settings.

Next open the `Project` menu and select `Project Settings..`. Now go to the `Plugins` tab and enable the plugin.

After doing that you need to close and re-open your project so everything is properly enabled.

### Basic hands

Just to get a feel of things we're going to add a few standard components that dress up our scene starting with hands for our player.

OpenXR supports full hand tracking however there currently are significant differences in capabilities between the different XR Runtimes.

As a reliable alternative Godot XR Tools comes with a number of rigged hand scenes that react on trigger and grip inputs of your controller. These hands come in low and high poly versions, come in a few configurations, a number of animation files to control finger positions and a number of different textures.

In your scene tree select your left hand [XRController3D](../godot_gdscript_misc.md) node. Now click on the **instantiate Child Scene** button to add a child scene. Click the **addons** toggle so the addons folder can be searched. Then search for `left_hand_low.tscn`, and select it.

As you can see from the path of this scene, low poly models are in the `lowpoly` subfolder while high poly models are in the `highpoly` subfolder. You will want to use the low poly versions if you plan to release your game on mobile devices.

The default hand we chose is just a hand. The other options are:

- tac_glove - the hand is wearing a glove with fingers exposed
- full_glove - the hand is wearing a glove that covers the entire hand

Finally each hand comes in a `physics` version. This exposes all the bones. We'll look at how that can be used in another tutorial.

We repeat the same for the right hand.

### More information

We'll continue with adding features to our tutorial project using Godot XR tools in the next couple of pages. More detailed information about the toolkit can be found [on the toolkits help pages](https://godotvr.github.io/godot-xr-tools/).

---

## OpenXR body tracking

Support for full body tracking in OpenXR is only just becoming available for a select few platforms. As support solidifies information will be added to this page.

### HTC Tracker support

An option that has been available for some time is doing full body tracking using HTC trackers. These are currently supported through SteamVR and on HTC Elite XR headsets. They are exposed through the action map system.

These trackers are identified by their roles which are assigned to them when configured. Simply add [XRController3D](../godot_gdscript_misc.md) nodes as children to the [XROrigin3D](../godot_gdscript_misc.md) node and assign one of the following trackers:

| /user/vive_tracker_htcx/role/handheld_object |
| /user/vive_tracker_htcx/role/left_foot |
| /user/vive_tracker_htcx/role/right_foot |
| /user/vive_tracker_htcx/role/left_shoulder |
| /user/vive_tracker_htcx/role/right_shoulder |
| /user/vive_tracker_htcx/role/left_elbow |
| /user/vive_tracker_htcx/role/right_elbow |
| /user/vive_tracker_htcx/role/left_knee |
| /user/vive_tracker_htcx/role/right_knee |
| /user/vive_tracker_htcx/role/waist |
| /user/vive_tracker_htcx/role/chest |
| /user/vive_tracker_htcx/role/camera |
| /user/vive_tracker_htcx/role/keyboard |

You can now use these as targets for IK modifiers on a full body avatar.

---

## OpenXR composition layers

### Introduction

In XR games you generally want to create user interactions that happen in 3D space and involve users touching objects as if they are touching them in real life.

Sometimes however creating a more traditional 2D interface is unavoidable. In XR however you can't just add 2D components to your scene. Godot needs depth information to properly position these elements so they appear at a comfortable place for the user. Even with depth information there are headsets with slanted displays that make it impossible for the standard 2D pipeline to correctly render the 2D elements.

The solution then is to render the UI to a [SubViewport](../godot_gdscript_rendering.md) and display the result of this using a [ViewportTexture](../godot_gdscript_rendering.md) on a 3D mesh. The [QuadMesh](../godot_gdscript_rendering.md) is a suitable option for this.

> **Note:** See the [GUI in 3D](https://github.com/godotengine/godot-demo-projects/tree/master/viewport/gui_in_3d) example project for an example of this approach.

The problem with displaying the viewport in this way is that the rendered result is sampled for lens distortion by the XR runtime and the resulting quality loss can make UI text hard to read.

OpenXR offers a solution to this problem through composition layers. With composition layers it is possible for the contents of a viewport to be projected on a surface after lens distortion resulting in a much higher quality end result.

> **Note:** As not all XR runtimes support all composition layer types, Godot implements a fallback solution where we render the viewport as part of the normal scene but with the aforementioned quality limitations.

> **Warning:** When the composition layer is supported, it is the XR runtime that presents the subviewport. This means the UI is only visible in the headset, it will not be accessible by Godot and will thus not be shown when you have a spectator view on the desktop.

There are currently 3 nodes that expose this functionality:

- [OpenXRCompositionLayerCylinder](../godot_gdscript_misc.md) shows the contents of the SubViewport on the inside of a cylinder (or "slice" of a cylinder).
- [OpenXRCompositionLayerEquirect](../godot_gdscript_misc.md) shows the contents of the SubViewport on the interior of a sphere (or "slice" of a sphere).
- [OpenXRCompositionLayerQuad](../godot_gdscript_misc.md) shows the contents of the SubViewport on a flat rectangle.

### Setting up the SubViewport

The first step is adding a SubViewport for our 2D UI, this doesn't require any specific steps. For our example we do mark the viewport as transparent.

You can now create the 2D UI by adding child nodes to the SubViewport as you normally would. It is advisable to save the 2D UI in a subscene, this makes it easier to do your layout.

> **Warning:** The update mode "When Visible" will not work as Godot can't determine whether the viewport is visible to the user. When assigning our viewport to a composition layer Godot will automatically adjust this.

### Adding a composition layer

The second step is adding our composition layer. We can add the correct composition layer node as a child node of our [XROrigin3D](../godot_gdscript_misc.md) node. This is very important as the XR runtime positions everything in relation to our origin.

We want to position the composition layer so it is at eye height and roughly 1 to 1.5 meters away from the player.

We now assign the SubViewport to the `Layer Viewport` property and enable Alpha Blend.

> **Note:** As the player can walk away from the origin point, you will want to reposition the composition layer when the player recenters the view. Using the reference space `Local Floor` will apply this logic automatically.

### Making the interface work

So far we're only displaying our UI, to make it work we need to add some code. For this example we're going to keep things simple and make one of the controllers work as a pointer. We'll then simulate mouse actions with this pointer.

This code also requires a `MeshInstance3D` node called `Pointer` to be added as a child to our `OpenXRCompositionLayerQuad` node. We configure a `SphereMesh` with a radius `0.01` meters. We'll be using this as a helper to visualize where the user is pointing.

The main function that drives this functionality is the `intersects_ray` function on our composition layer node. This function takes the global position and orientation of our pointer and returns the UV where our ray intersects our viewport. It returns `Vector2(-1.0, -1.0)` if we're not pointing at our viewport.

We start with setting up some variables, important here are the export variables which identify our controller node with which we point to our screen.

```gdscript
extends OpenXRCompositionLayerQuad

const NO_INTERSECTION = Vector2(-1.0, -1.0)

@export var controller : XRController3D
@export var button_action : String = "trigger_click"

var was_pressed : bool = false
var was_intersect : Vector2 = NO_INTERSECTION

...
```

Next we define a helper function that takes the value returned from `intersects_ray` and gives us the global position for that intersection point. This implementation only works for our `OpenXRCompositionLayerQuad` node.

```gdscript
...

func _intersect_to_global_pos(intersect : Vector2) -> Vector3:
    if intersect != NO_INTERSECTION:
        var local_pos : Vector2 = (intersect - Vector2(0.5, 0.5)) * quad_size
        return global_transform * Vector3(local_pos.x, -local_pos.y, 0.0)
    else:
        return Vector3()

...
```

We also define a helper function that takes our `intersect` value and returns our location in the viewport's local coordinate system:

```gdscript
...

func _intersect_to_viewport_pos(intersect : Vector2) -> Vector2i:
    if layer_viewport and intersect != NO_INTERSECTION:
        var pos : Vector2 = intersect * Vector2(layer_viewport.size)
        return Vector2i(pos)
    else:
        return Vector2i(-1, -1)

...
```

The main logic happens in our `_process` function. Here we start by hiding our pointer, we then check if we have a valid controller and viewport, and we call `intersects_ray` with the position and orientation of our controller:

```gdscript
...

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(_delta):
    # Hide our pointer, we'll make it visible if we're interacting with the viewport.
    $Pointer.visible = false

    if controller and layer_viewport:
        var controller_t : Transform3D = controller.global_transform
        var intersect : Vector2 = intersects_ray(controller_t.origin, -controller_t.basis.z)

...
```

Next we check if we're intersecting with our viewport. If so, we check if our button is pressed and place our pointer at our intersection point.

```gdscript
...

        if intersect != NO_INTERSECTION:
            var is_pressed : bool = controller.is_button_pressed(button_action)

            # Place our pointer where we're pointing
            var pos : Vector3 = _intersect_to_global_pos(intersect)
            $Pointer.visible = true
            $Pointer.global_position = pos

...
```

If we were intersecting in our previous process call and our pointer has moved, we prepare an [InputEventMouseMotion](../godot_gdscript_input.md) object to simulate our mouse moving and send that to our viewport for further processing.

```gdscript
...

            if was_intersect != NO_INTERSECTION and intersect != was_intersect:
                # Pointer moved
                var event : InputEventMouseMotion = InputEventMouseMotion.new()
                var from : Vector2 = _intersect_to_viewport_pos(was_intersect)
                var to : Vector2 = _intersect_to_viewport_pos(intersect)
                if was_pressed:
                    event.button_mask = MOUSE_BUTTON_MASK_LEFT
                event.relative = to - from
                event.position = to
                layer_viewport.push_input(event)

...
```

If we've just released our button we also prepare an [InputEventMouseButton](../godot_gdscript_input.md) object to simulate a button release and send that to our viewport for further processing.

```gdscript
...

            if not is_pressed and was_pressed:
                # Button was let go?
                var event : InputEventMouseButton = InputEventMouseButton.new()
                event.button_index = 1
                event.pressed = false
                event.position = _intersect_to_viewport_pos(intersect)
                layer_viewport.push_input(event)

...
```

Or if we've just pressed our button we prepare an [InputEventMouseButton](../godot_gdscript_input.md) object to simulate a button press and send that to our viewport for further processing.

```gdscript
...

            elif is_pressed and not was_pressed:
                # Button was pressed?
                var event : InputEventMouseButton = InputEventMouseButton.new()
                event.button_index = 1
                event.button_mask = MOUSE_BUTTON_MASK_LEFT
                event.pressed = true
                event.position = _intersect_to_viewport_pos(intersect)
                layer_viewport.push_input(event)

...
```

Next we remember our state for next frame.

```gdscript
...

            was_pressed = is_pressed
            was_intersect = intersect

...
```

Finally, if we aren't intersecting, we clear our state.

```gdscript
...

        else:
            was_pressed = false
            was_intersect = NO_INTERSECTION
```

### Hole punching

As the composition layer is composited on top of the render result, it can be rendered in front of objects that are actually forward of the viewport.

By enabling hole punch you instruct Godot to render a transparent object where our viewport is displayed. It does this in a way that fills the depth buffer and clears the current rendering result. Anything behind our viewport will now be cleared, while anything in front of our viewport will be rendered as usual.

You also need to set `Sort Order` to a negative value, the XR compositor will now draw the viewport first, and then overlay our rendering result.

---
