# Godot 4 C# Tutorials — Xr (Part 1)

> 8 tutorials. C#-specific code examples.

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

```csharp
using Godot;

public partial class MyNode3D : Node3D
{
    [Signal]
    public delegate void FocusLostEventHandler();

    [Signal]
    public delegate void FocusGainedEventHandler();

    [Signal]
    public delegate void PoseRecenteredEventHandler();

...
```

### Variables for our script

We introduce a few new variables to our script as well:

- `maximum_refresh_rate` will control the headsets refresh rate if this is supported by the headset.
- `xr_interface` holds a reference to our XR interface, this already existed but we now type it to get full access to our [XRInterface](../godot_csharp_misc.md) API.
- `xr_is_focussed` will be set to true whenever our game has focus.

```csharp
...

    [Export]
    public int MaximumRefreshRate { get; set; } = 90;

    private OpenXRInterface _xrInterface;

    private bool _xrIsFocused;

...
```

### Our updated ready function

We add a few things to the ready function.

If we're using the mobile or forward+ renderer we set the viewport's `vrs_mode` to `VRS_XR`. On platforms that support this, this will enable foveated rendering.

If we're using the compatibility renderer, we check if the OpenXR foveated rendering settings are configured and if not, we output a warning. See OpenXR Settings for further details.

We hook up a number of signals that will be emitted by the [XRInterface](../godot_csharp_misc.md). We'll provide more detail about these signals as we implement them.

We also quit our application if we couldn't successfully initialise OpenXR. Now this can be a choice. If you are making a mixed mode game you setup the VR mode of your game on success, and setup the non-VR mode of your game on failure. However, when running a VR only application on a standalone headset, it is nicer to exit on failure than to hang the system.

```csharp
...

    /// <summary>
    /// Called when the node enters the scene tree for the first time.
    /// </summary>
    public override void _Ready()
    {
        _xrInterface = (OpenXRInterface)XRServer.FindInterface("OpenXR");
        if (_xrInterface != null && _xrInterface.IsInitialized())
        {
            GD.Print("OpenXR instantiated successfully.");
            var vp = GetViewport();

            // Enable XR on our viewport
            vp.UseXR = true;

            // Make sure v-sync is off, v-sync is handled by OpenXR
            DisplayServer.WindowSetVsyncMode(DisplayServer.VSyncMode.Disabled);

            // Enable VRS
            if (RenderingServer.GetRenderingDevice() != null)
            {
                vp.VrsMode = Viewport.VrsModeEnum.XR;
            }

// ...
```

### On session begun

This signal is emitted by OpenXR when our session is setup. This means the headset has run through setting everything up and is ready to begin receiving content from us. Only at this time various information is properly available.

The main thing we do here is to check our headset's refresh rate. We also check the available refresh rates reported by the XR runtime to determine if we want to set our headset to a higher refresh rate.

Finally we match our physics update rate to our headset update rate. Godot runs at a physics update rate of 60 updates per second by default while headsets run at a minimum of 72, and for modern headsets often up to 144 frames per second. Not matching the physics update rate will cause stuttering as frames are rendered without objects moving.

```csharp
...

    /// <summary>
    /// Handle OpenXR session ready
    /// </summary>
    private void OnOpenXRSessionBegun()
    {
        // Get the reported refresh rate
        var currentRefreshRate = _xrInterface.DisplayRefreshRate;
        GD.Print(currentRefreshRate > 0.0F
            ? $"OpenXR: Refresh rate reported as {currentRefreshRate}"
            : "OpenXR: No refresh rate given by XR runtime");

        // See if we have a better refresh rate available
        var newRate = currentRefreshRate;
        var availableRates = _xrInterface.GetAvailableDisplayRefreshRates();
        if (availableRates.Count == 0)
        {
            GD.Print("OpenXR: Target does not support refresh rate extension");
        }
        else if (availableRates.Count == 1)
        {
            // Only on
// ...
```

### On visible state

This signal is emitted by OpenXR when our game becomes visible but is not focused. This is a bit of a weird description in OpenXR but it basically means that our game has just started and we're about to switch to the focused state next, that the user has opened a system menu or the user has just took their headset off.

On receiving this signal we'll update our focused state, we'll change the process mode of our node to disabled which will pause processing on this node and its children, and emit our `focus_lost` signal.

If you've added this script to your root node, this means your game will automatically pause when required. If you haven't, you can connect a method to the signal that performs additional changes.

> **Note:** While your game is in visible state because the user has opened a system menu, Godot will keep rendering frames and head tracking will remain active so your game will remain visible in the background. However controller and hand tracking will be disabled until the user exits the system menu.

```csharp
...

    /// <summary>
    /// Handle OpenXR visible state
    /// </summary>
    private void OnOpenXRVisibleState()
    {
        // We always pass this state at startup,
        // but the second time we get this it means our player took off their headset
        if (_xrIsFocused)
        {
            GD.Print("OpenXR lost focus");

            _xrIsFocused = false;

            // Pause our game
            GetTree().Paused = true;

            EmitSignal(SignalName.FocusLost);
        }
    }

...
```

### On focussed state

This signal is emitted by OpenXR when our game gets focus. This is done at the completion of our startup, but it can also be emitted when the user exits a system menu, or put their headset back on.

Note also that when your game starts while the user is not wearing their headset, the game stays in 'visible' state until the user puts their headset on.

> **Warning:** It is thus important to keep your game paused while in visible mode. If you don't the game will keep on running while your user isn't interacting with your game. Also when the game returns to the focused mode, suddenly all controller and hand tracking is re-enabled and could have game breaking consequences if you do not react to this accordingly. Be sure to test this behavior in your game!

While handling our signal we will update the focuses state, unpause our node and emit our `focus_gained` signal.

```csharp
...

    /// <summary>
    /// Handle OpenXR focused state
    /// </summary>
    private void OnOpenXRFocusedState()
    {
        GD.Print("OpenXR gained focus");
        _xrIsFocused = true;

        // Un-pause our game
        GetTree().Paused = false;

        EmitSignal(SignalName.FocusGained);
    }

...
```

### On stopping state

This signal is emitted by OpenXR when we enter our stop state. There are some differences between platforms when this happens. On some platforms this is only emitted when the game is being closed. But on other platforms this will also be emitted every time the player takes off their headset.

For now this method is only a place holder.

```csharp
...

    /// <summary>
    /// Handle OpenXR stopping state
    /// </summary>
    private void OnOpenXRStopping()
    {
        // Our session is being stopped.
        GD.Print("OpenXR is stopping");
    }

...
```

### On pose recentered

This signal is emitted by OpenXR when the user requests their view to be recentered. Basically this communicates to your game that the user is now facing forward and you should re-orient the player so they are facing forward in the virtual world.

As doing so is dependent on your game, your game needs to react accordingly.

All we do here is emit the `pose_recentered` signal. You can connect to this signal and implement the actual recenter code. Often it is enough to call [center_on_hmd()](../godot_csharp_misc.md).

```csharp
...

    /// <summary>
    /// Handle OpenXR pose recentered signal
    /// </summary>
    private void OnOpenXRPoseRecentered()
    {
        // User recentered view, we have to react to this by recentering the view.
        // This is game implementation dependent.
        EmitSignal(SignalName.PoseRecentered);
    }
}
```

And that finished our script. It was written so that it can be re-used over multiple projects. Just add it as the script on your main node (and extend it if needed) or add it on a child node specific for this script.

---

## AR / Passthrough

Augmented Reality is supported through various methods depending on the capabilities of the hardware.

Headsets such as the Magic Leap and glasses such as TiltFive show the rendered result on [see-through displays](https://en.wikipedia.org/wiki/See-through_display) allowing the user to see the real world.

Headsets such as the Quest, HTC Elite, and Lynx R1 implement this through a technique called video passthrough, where cameras record the real world and these images are used as the background on top of which our rendered result is used.

> **Note:** Passthrough is implemented very differently across platforms. In Godot 4.3 we have implemented a unified approach that is explained on this help page so you don't need to worry about these differences, the [XRInterface](../godot_csharp_misc.md) implementation is now responsible for applying the correct platform-dependent method **[1]**. For headsets such as the Meta Quest and HTC Elite you will need to use the [OpenXR vendors plugin v3.0.0](https://github.com/GodotVR/godot_openxr_vendors/releases) or later to enable video passthrough. For backwards compatibility the old API for passthrough is still available but it is recommended to follow the new instructions below.

### Environment blend modes

The way we configure VR or AR functionality is through setting the environment blend mode. This mode determines how the (real world) environment is blended with the virtual world.

| Blend mode                    | Description                                                                                                                                                                                                                                                                            |
| ----------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| XR_ENV_BLEND_MODE_OPAQUE      | The rendered image is opaque, we do not see the real world. We're in VR mode. This will turn off passthrough if video-passthrough is used.                                                                                                                                             |
| XR_ENV_BLEND_MODE_ADDITIVE    | The rendered image is added to the real world and will look semi transparent. This mode is generally used with see-through devices that are unable to obscure the real world. This will turn on passthrough if video-passthrough is used.                                              |
| XR_ENV_BLEND_MODE_ALPHA_BLEND | The rendered image is alpha blended with the real world. On see-through devices that support this, the alpha will control the translucency of the optics. On video-passthrough devices alpha blending is applied with the video image. passthrough will also be enabled if applicable. |

You can set the environment blend mode for your application through the `environment_blend_mode` property of the [XRInterface](../godot_csharp_misc.md) instance.

You can query the supported blend modes on the hardware using the `get_supported_environment_blend_modes` property on the same instance.

### Configuring your background

When setting the blend mode to `XR_ENV_BLEND_MODE_ALPHA_BLEND` you must set the `transparent_bg` property on [Viewport](../godot_csharp_rendering.md) to true. When using the `XR_ENV_BLEND_MODE_ADDITIVE` blend mode you should set your background color to black.

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

The first step we need to do is to add a helper node to our [XROrigin3D](../godot_csharp_misc.md) node. Because XR supports roomscale tracking you can't simply add your XR setup to a [CharacterBody3D](../godot_csharp_nodes_3d.md) node and expect things to work. You will run into trouble when the user moves around their physical space and is no longer standing in the center of their room. Godot XR Tools embeds the needed logic into a helper node called `PlayerBody`.

Select your [XROrigin3D](../godot_csharp_misc.md) node and click on the Instantiate Child Scene button to add a child scene. Select `addons/godot-xr-tools/player/player_body.tscn` and add this node.

### Adding a floor

This node governs the in game movement of your character and will immediately react to gravity. So to prevent our player from infinitely falling down we'll quickly add a floor to our scene.

We start by adding a [StaticBody3D](../godot_csharp_nodes_3d.md) node to our root node and we rename this to `Floor`. We add a [MeshInstance3D](../godot_csharp_nodes_3d.md) node as a child node for our `Floor`. Then create a new [PlaneMesh](../godot_csharp_rendering.md) as its mesh. For now we set the size of the mesh to 100 x 100 meters. Next we add a [CollisionShape3D](../godot_csharp_physics.md) node as a child node for our `Floor`. Then create a `BoxShape` as our shape. We set the size of this box shape to 100 x 1 x 100 meters. We also need to move our collision shape down by 0.5 meters so the top of our box is flush with the floor.

To make it easier to see that we're actually moving around our world, a white floor isn't going to do it. Create a texture using [Wahooneys excellent free texture generator](https://wahooney.itch.io/texture-grid-generator). Once you've created the texture add it to your project. Then create a new material for the MeshInstance3D node, add your texture as the albedo, and enable **Triplaner** under **UV1** in the material properties.

### Direct movement

We're going to start adding some basic direct movement to our setup. This allows the user to move through the virtual world using joystick input.

> **Note:** It is important to note that moving through the virtual world while the player is standing still in the real world, can be nausea inducing especially for players who are new to VR. The default settings on our movement functions are fairly conservative. We advise you to stick to these defaults but offer features in game to enable less comfortable settings for more experienced users who are used to playing VR games.

We want to enable this on the right hand controller. We do this by adding a subscene to the right hand [XRController3D](../godot_csharp_misc.md) node. Select `addons/godot-xr-tools/functions/movement_direct.tscn` as the scene to add.

This function adds forward and backwards movement to the player by using the joystick on the right hand controller. It has an option to also add left/right strafe but by default this is disabled.

Instead, we are going to add the ability for the player to also turn with this joystick. We will add another subscene to our controller node, select `addons/godot-xr-tools/functions/movement_turn.tscn` for this.

The turn system by default uses a snap turn approach. This means that turning happens in steps. This may seem jarring however it is a tried and tested method of combating motion sickness. You can easily switch to a mode that offers smooth turning by changing the `mode` property on the turn node.

If you run your game at this point in time you will find that you can move through the world freely using the right hand joystick.

### Teleport

An alternative to direct movement that some users find more pleasant is the ability to teleport to another location within your game world. Godot XR Tools supports this through the teleport function and we will be adding this to our left hand controller.

Add a new child scene to your left hand [XRController3D](../godot_csharp_misc.md) node by selecting the `addons/godot-xr-tools/functions/function_teleport.tscn` scene.

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

In your scene tree select your left hand [XRController3D](../godot_csharp_misc.md) node. Now click on the **instantiate Child Scene** button to add a child scene. Click the **addons** toggle so the addons folder can be searched. Then search for `left_hand_low.tscn`, and select it.

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

These trackers are identified by their roles which are assigned to them when configured. Simply add [XRController3D](../godot_csharp_misc.md) nodes as children to the [XROrigin3D](../godot_csharp_misc.md) node and assign one of the following trackers:

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

The solution then is to render the UI to a [SubViewport](../godot_csharp_rendering.md) and display the result of this using a [ViewportTexture](../godot_csharp_rendering.md) on a 3D mesh. The [QuadMesh](../godot_csharp_rendering.md) is a suitable option for this.

> **Note:** See the [GUI in 3D](https://github.com/godotengine/godot-demo-projects/tree/master/viewport/gui_in_3d) example project for an example of this approach.

The problem with displaying the viewport in this way is that the rendered result is sampled for lens distortion by the XR runtime and the resulting quality loss can make UI text hard to read.

OpenXR offers a solution to this problem through composition layers. With composition layers it is possible for the contents of a viewport to be projected on a surface after lens distortion resulting in a much higher quality end result.

> **Note:** As not all XR runtimes support all composition layer types, Godot implements a fallback solution where we render the viewport as part of the normal scene but with the aforementioned quality limitations.

> **Warning:** When the composition layer is supported, it is the XR runtime that presents the subviewport. This means the UI is only visible in the headset, it will not be accessible by Godot and will thus not be shown when you have a spectator view on the desktop.

There are currently 3 nodes that expose this functionality:

- [OpenXRCompositionLayerCylinder](../godot_csharp_misc.md) shows the contents of the SubViewport on the inside of a cylinder (or "slice" of a cylinder).
- [OpenXRCompositionLayerEquirect](../godot_csharp_misc.md) shows the contents of the SubViewport on the interior of a sphere (or "slice" of a sphere).
- [OpenXRCompositionLayerQuad](../godot_csharp_misc.md) shows the contents of the SubViewport on a flat rectangle.

### Setting up the SubViewport

The first step is adding a SubViewport for our 2D UI, this doesn't require any specific steps. For our example we do mark the viewport as transparent.

You can now create the 2D UI by adding child nodes to the SubViewport as you normally would. It is advisable to save the 2D UI in a subscene, this makes it easier to do your layout.

> **Warning:** The update mode "When Visible" will not work as Godot can't determine whether the viewport is visible to the user. When assigning our viewport to a composition layer Godot will automatically adjust this.

### Adding a composition layer

The second step is adding our composition layer. We can add the correct composition layer node as a child node of our [XROrigin3D](../godot_csharp_misc.md) node. This is very important as the XR runtime positions everything in relation to our origin.

We want to position the composition layer so it is at eye height and roughly 1 to 1.5 meters away from the player.

We now assign the SubViewport to the `Layer Viewport` property and enable Alpha Blend.

> **Note:** As the player can walk away from the origin point, you will want to reposition the composition layer when the player recenters the view. Using the reference space `Local Floor` will apply this logic automatically.

### Making the interface work

So far we're only displaying our UI, to make it work we need to add some code. For this example we're going to keep things simple and make one of the controllers work as a pointer. We'll then simulate mouse actions with this pointer.

This code also requires a `MeshInstance3D` node called `Pointer` to be added as a child to our `OpenXRCompositionLayerQuad` node. We configure a `SphereMesh` with a radius `0.01` meters. We'll be using this as a helper to visualize where the user is pointing.

The main function that drives this functionality is the `intersects_ray` function on our composition layer node. This function takes the global position and orientation of our pointer and returns the UV where our ray intersects our viewport. It returns `Vector2(-1.0, -1.0)` if we're not pointing at our viewport.

We start with setting up some variables, important here are the export variables which identify our controller node with which we point to our screen.

Next we define a helper function that takes the value returned from `intersects_ray` and gives us the global position for that intersection point. This implementation only works for our `OpenXRCompositionLayerQuad` node.

We also define a helper function that takes our `intersect` value and returns our location in the viewport's local coordinate system:

The main logic happens in our `_process` function. Here we start by hiding our pointer, we then check if we have a valid controller and viewport, and we call `intersects_ray` with the position and orientation of our controller:

Next we check if we're intersecting with our viewport. If so, we check if our button is pressed and place our pointer at our intersection point.

If we were intersecting in our previous process call and our pointer has moved, we prepare an [InputEventMouseMotion](../godot_csharp_input.md) object to simulate our mouse moving and send that to our viewport for further processing.

If we've just released our button we also prepare an [InputEventMouseButton](../godot_csharp_input.md) object to simulate a button release and send that to our viewport for further processing.

Or if we've just pressed our button we prepare an [InputEventMouseButton](../godot_csharp_input.md) object to simulate a button press and send that to our viewport for further processing.

Next we remember our state for next frame.

Finally, if we aren't intersecting, we clear our state.

### Hole punching

As the composition layer is composited on top of the render result, it can be rendered in front of objects that are actually forward of the viewport.

By enabling hole punch you instruct Godot to render a transparent object where our viewport is displayed. It does this in a way that fills the depth buffer and clears the current rendering result. Anything behind our viewport will now be cleared, while anything in front of our viewport will be rendered as usual.

You also need to set `Sort Order` to a negative value, the XR compositor will now draw the viewport first, and then overlay our rendering result.

---

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

- Tracking happens in the local space of the [XROrigin3D](../godot_csharp_misc.md) node. This node must be a child of the XROrigin3D node in order to be correctly placed.
- This node can be used as an IK target when an upper body mesh with arms is used instead of separate hand meshes.
- Actual placement of the hands may be loosely bound to the tracking in scenarios such as avatar creation UIs, fake mirrors, or similar situations resulting in the hand mesh and finger tracking being localized elsewhere.

We'll concentrate on the first use case only.

For this you need to add an [XRNode3D](../godot_csharp_misc.md) node to your `XROrigin3D` node.

- On this node the `tracker` should be set to `/user/hand_tracker/left` or `/user/hand_tracker/right` for the left or right hand respectively.
- The `pose` should remain set to `default`, no other option will work here.
- The checkbox `Show When Tracked` will automatically hide this node if no tracking data is available, or make this node visible if tracking data is available.

#### Rigged hand mesh

In order to display our hand we need a hand mesh that is properly rigged and skinned. For this Godot uses the hand bone structure as defined for the [Godot Humanoid](../godot_csharp_misc.md) but optionally supporting an extra tip bone for each finger.

The [OpenXR hand tracking demo](https://github.com/godotengine/godot-demo-projects/tree/master/xr/openxr_hand_tracking_demo) contains example glTF files of properly rigged hands.

We will be using those here and add them as a child to our `XRNode3D` node. We also need to enable editable children to gain access to our [Skeleton3D](../godot_csharp_nodes_3d.md) node.

#### The hand skeleton modifier

Finally we need to add an [XRHandModifier3D](../godot_csharp_misc.md) node as a child to our `Skeleton3D` node. This node will obtain the finger tracking data from OpenXR and apply it the hand model.

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

You can obtain the full hand tracking data through the [XRHandTracker](../godot_csharp_misc.md) resource for each hand. You can obtain the hand tracker by calling `XRServer.get_tracker` and using either `/user/hand_tracker/left` or `/user/hand_tracker/left` as the tracker. This resource provides access to all the joint information for the given hand.

Detailing out a full gesture recognition algorithm goes beyond the scope of this manual however there are a number of community projects you can look at:

- [Julian Todd's Auto hands library](https://github.com/Godot-Dojo/Godot-XR-AH)
- [Malcolm Nixons Hand Pose Detector](https://github.com/Malcolmnixon/GodotXRHandPoseDetector)

---
