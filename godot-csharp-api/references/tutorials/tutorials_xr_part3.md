# Godot 4 C# Tutorials — Xr (Part 3)

> 5 tutorials. C#-specific code examples.

## Setting up XR

### Introduction to the XR system in Godot

Godot provides a modular XR system that abstracts many of the different XR platform specifics away from the user. At the core sits the [XRServer](../godot_csharp_misc.md) which acts as a central interface to the XR system that allows users to discover interfaces and interact with the components of the XR system.

Each supported XR platform is implemented as an [XRInterface](../godot_csharp_misc.md). A list of supported platforms can be found on the list of features page here (see About docs). Supported interfaces register themselves with the [XRServer](../godot_csharp_misc.md) and can be queried with the `find_interface` method on the [XRServer](../godot_csharp_misc.md). When the desired interface is found it can be initialized by calling `initialize` on the interface.

> **Warning:** A registered interface means nothing more than that the interface is available, if the interface is not supported by the host system, initialization may fail and return `false`. This can have many reasons and sadly the reasons differ from platform to platform. It can be because the user hasn't installed the required software, or that the user simply hasn't plugged in their headset. You as a developer must thus react properly on an interface failing to initialize.

Due to the special requirements for output in XR, especially for head mounted devices that supply different images to each eye, the [XRServer](../godot_csharp_misc.md) in Godot will override various features in the rendering system. For stand-alone devices this means the final output is handled by the [XRInterface](../godot_csharp_misc.md) and Godot's usual output system is disabled. For desktop XR devices that work as a second screen it is possible to dedicate a separate [Viewport](../godot_csharp_rendering.md) to handle the XR output, leaving the main Godot window available for displaying alternative content.

> **Note:** Note that only one interface can be responsible for handling the output to an XR device, this is known as the primary interface and by default will be the first interface that is initialized. Godot currently thus only supports implementations with a single headset. It is possible, but increasingly uncommon, to have a secondary interface, for example to add tracking to an otherwise 3DOF only device.

There are three XR specific node types that you will find in nearly all XR applications:

- [XROrigin3D](../godot_csharp_misc.md) represents, for all intents and purposes, the center point of your play space. That is an oversimplified statement but we'll go into more detail later. All objects tracked in physical space by the XR platform are positioned in relation to this point.
- [XRCamera3D](../godot_csharp_misc.md) represents the (stereo) camera that is used when rendering output for the XR device. The positioning of this node is controlled by the XR system and updated automatically using the tracking information provided by the XR platform.
- [XRController3D](../godot_csharp_misc.md) represents a controller used by the player, commonly there are two, one held in each hand. These nodes give access to various states on these controllers and send out signals when the player presses buttons on them. The positioning of this node is controlled by the XR system and updated automatically using the tracking information provided by the XR platform.

There are other XR related nodes and there is much more to say about these three nodes, but we'll get into that later on.

### Which Renderer to use

Godot has 3 renderer options for projects: Compatibility, Mobile, and Forward+. The current recommendation is to use the Mobile renderer for any desktop VR project, and use the Compatibility renderer for any project running on a standalone headset like the Meta Quest 3. XR projects will run with the Forward+ renderer, but it isn't well optimized for XR right now compared to the other two.

### OpenXR

OpenXR is a new industry standard that allows different XR platforms to present themselves through a standardized API to XR applications. This standard is an open standard maintained by the Khronos Group and thus aligns very well with Godot's interests.

The Vulkan implementation of OpenXR is closely integrated with Vulkan, taking over part of the Vulkan system. This requires tight integration of certain core graphics features in the Vulkan renderer which are needed before the XR system is setup. This was one of the main deciding factors to include OpenXR as a core interface.

This also means OpenXR needs to be enabled when Godot starts in order to set things up correctly. Check the [Enabled](../godot_csharp_misc.md) setting in your project settings under **XR > OpenXR**.

You can find several other settings related to OpenXR here as well. These can't be changed while your application is running. The default settings will get us started, but for more information on what's here see OpenXR Settings.

You'll also need to go to **XR > Shaders** in the project settings and check the [Enabled](../godot_csharp_misc.md) box to enable them. Once you've done that click the **Save & Restart** button.

> **Warning:** Many post process effects have not yet been updated to support stereoscopic rendering. Using these will have adverse effects.

### Setting up the XR scene

Every XR application needs at least an [XROrigin3D](../godot_csharp_misc.md) and an [XRCamera3D](../godot_csharp_misc.md) node. Most will have two [XRController3D](../godot_csharp_misc.md), one for the left hand and one for the right. Keep in mind that the camera and controller nodes should be children of the origin node. Add these nodes to a new scene and rename the controller nodes to `LeftHand` and `RightHand`, your scene should look something like this:

The warning icons are expected and should go away after you configure the controllers. Select the left hand and set it up as follows:

And the right hand:

Right now all these nodes are on the floor, they will be positioned correctly in runtime. To help during development, it can be helpful to move the camera upwards so its `y` is set to `1.7`, and move the controller nodes to `-0.5, 1.0, -0.5` and `0.5, 1.0, -0.5` for respectively the left and right hand.

Next we need to add a script to our root node. Add the following code into this script:

```csharp
using Godot;

public partial class MyNode3D : Node3D
{
    private XRInterface _xrInterface;

    public override void _Ready()
    {
        _xrInterface = XRServer.FindInterface("OpenXR");
        if(_xrInterface != null && _xrInterface.IsInitialized())
        {
            GD.Print("OpenXR initialized successfully");

            // Turn off v-sync!
            DisplayServer.WindowSetVsyncMode(DisplayServer.VSyncMode.Disabled);

            // Change our main viewport to output to the HMD
            GetViewport().UseXR = true;
        }
        else
        {
            GD.Print("OpenXR not initialized, please check if your headset is connected");
        }
    }
}
```

This code fragment assumes we are using OpenXR, if you wish to use any of the other interfaces you can change the `find_interface` call.

> **Warning:** As you can see in the code snippet above, we turn off v-sync. When using OpenXR you are outputting the rendering results to an HMD that often requires us to run at 90Hz or higher. If your monitor is a 60hz monitor and v-sync is turned on, you will limit the output to 60 frames per second. XR interfaces like OpenXR perform their own sync. Also note that by default the physics engine runs at 60Hz as well and this can result in choppy physics. You should set `Engine.physics_ticks_per_second` to a higher value.

If you run your project at this point in time, everything will work but you will be in a dark world. So to finish off our starting point add a [DirectionalLight3D](../godot_csharp_nodes_3d.md) and a [WorldEnvironment](../godot_csharp_nodes_3d.md) node to your scene. You may wish to also add a mesh instance as a child to each controller node just to temporarily visualise them. Make sure you configure a sky in your world environment.

Now run your project, you should be floating somewhere in space and be able to look around.

> **Note:** While traditional level switching can definitely be used with XR applications, where this scene setup is repeated in each level, most find it easier to set this up once and loading levels as a subscene. If you do switch scenes and replicate the XR setup in each one, do make sure you do not run `initialize` multiple times. The effect can be unpredictable depending on the XR interface used. For the rest of this basic tutorial series we will create a game that uses a single scene.

---

## The XR action map

Godot has an action map feature as part of the XR system. At this point in time this system is part of the OpenXR module. There are plans to encompass WebXR into this in the near future hence we call it the XR action map system in this document. It implements the built-in action map system of OpenXR mostly exactly as it is offered.

The XR action map system exposes input, positional data and output for XR controllers to your game/application. It does this by exposing named actions that can be tailored to your game/application and binding these to the actual inputs and outputs on your XR devices.

As the XR action map is currently part of the OpenXR module, OpenXR needs to be enabled in your project settings to expose it:

You will then find the XR Action Map interface in the bottom of the screen:

> **Note:** Godot's built-in input system has many things in common with the XR action map system. In fact our original idea was to add functionality to the existing input system and expose the data to the OpenXR action map system. We may revisit that idea at some point but as it turns out there were just too many problems to overcome. To name a few: - Godot's input system mainly centers around button inputs, XR adds triggers, axis, poses and haptics (output) into the mix. This would greatly complicate the input system with features that won't work for normal controllers or contrast with the current approach. It was felt this would lead to confusion for the majority of Godot users.

- Godot's input system works with raw input data that is parsed and triggers emitting actions. This input data is made available to the end user. OpenXR completely hides raw data and does all the parsing for us, we only get access to already parsed action data. This inconsistency is likely to lead to bugs when an unsuspecting user tries to use an XR device as a normal input device.
- Godot's input system allows changes to what inputs are bound to actions in runtime, OpenXR does not.
- Godot's input system is based on device ids which are meaningless in OpenXR. This does mean that a game/application that mixes traditional inputs with XR controllers will have a separation. For most applications either one or the other is used and this is not seen as a problem. In the end, it's a limitation of the system.

### The default action map

Godot will automatically create a default action map if no action map file is found.

> **Warning:** This default map was designed to help developers port their XR games/applications from Godot 3 to Godot 4. As a result this map essentially binds all known inputs on all controllers supported by default, to actions one on one. This is not a good example of setting up an action map. It does allow a new developer to have a starting point when they want to become familiar with Godot XR. It prevents having to design a proper action map for their game/application first.

For this walkthrough we're going to start with a blank action map. You can delete the "Godot action set" entry at the top by pressing the trash can icon. This will clear out all actions. You might also want to remove the controllers that you do not wish to setup, more on this later.

### Action sets

> **Note:** Before we dive in, you will see the term XR runtime used throughout this document. With XR runtime we mean the software that is controlling and interacting with the AR or VR headset. The XR runtime then exposes this to us through an API such as OpenXR. So: - for Steam this is SteamVR,

- for Meta on desktop this is the Oculus Client (including when using Quest link),
- for Meta on Quest this is the Quest's native OpenXR client,
- on Linux this could be Monado, etc.

The action map allows us to organize our actions in sets. Each set can be enabled or disabled on its own.

The concept here is that you could have different sets that provide bindings in different scenarios. You could have:

- a `Character control` set for when you're walking around,
- a `Vehicle control` set for when you're operating a vehicle,
- a `Menu` set for when a menu is open.

Only the action set applicable to the current state of your game/application can then be enabled.

This is especially important if you wish to bind the same input on a controller to a different action. For instance:

- in your `Character control` set you may have an action `Jump`,
- in your `Vehicle control` set you may have an action `Accelerate`,
- in your `Menu` set you may have an action `Select`.

All are bound to the trigger on your controller.

OpenXR will only bind an input or output to a single action. If the same input or output is bound to multiple actions the one in the active action set with the highest priority will be the one updated/used. So in our above example it will thus be important that only one action set is active.

For your first XR game/application we highly recommend starting with just a single action set and to not over-engineer things.

For our walkthrough in this document we will thus create a single action set called `my_first_action_set`. We do this by pressing the Add action set button:

The columns in our table are as follows:

| Col | Value               | Description                                                                                                                                                                                                                     |
| --- | ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | my_first_action_set | This is the internal name of the action set. OpenXR doesn't specify specific restrictions on this name other than size, however some XR runtimes will not like spaces or special characters.                                    |
| 2   | My first action set | This is a human-readable name for the action set. Some XR runtimes will display this name to the end user, for example in configuration dialogs.                                                                                |
| 3   | 0                   | This is the priority of the action set. If multiple active action sets have actions bound to the same controller's inputs or outputs, the action set with the highest priority value will determine the action that is updated. |

### Actions

In the XR action map, actions are the entities that your game/application will interact with. For instance, we can define an action `Shoot` and the input bound to that action will trigger the `button_pressed` signal on the relevant [XRController3D](../godot_csharp_misc.md) node in your scene with `Shoot` as the `name` parameter of the signal.

You can also poll the current state of an action. [XRController3D](../godot_csharp_misc.md) for instance has an `is_button_pressed` method.

Actions can be used for both input and output and each action has a type that defines its behavior.

- The `Bool` type is used for discrete input like buttons.
- The `Float` type is used for analogue input like triggers.

These two are special as they are the only ones that are interchangeable. OpenXR will handle conversions between `Bool` and `Float` inputs and actions. You can get the value of a `Float` type action by calling the method `get_float` on your [XRController3D](../godot_csharp_misc.md) node. It emits the `input_float_changed` signal when changed.

> **Note:** Where analogue inputs are queried as buttons a threshold is applied. This threshold is currently managed exclusively by the XR runtime. There are plans to extend Godot to provide some level of control over these thresholds in the future.

The `Vector2` type defines the input as an axis input. Touchpads, thumbsticks and similar inputs are exposed as vectors. You can get the value of a `Vector2` type action by calling the method `get_vector2` on your [XRController3D](../godot_csharp_misc.md) node. It emits the `input_vector2_changed` signal when changed.

The `Pose` type defines a spatially tracked input. Multiple "pose" inputs are available in OpenXR: `aim`, `grip` and `palm`. Your [XRController3D](../godot_csharp_misc.md) node is automatically positioned based on the pose action assigned to `pose` property of this node. More about poses later.

> **Note:** The OpenXR implementation in Godot also exposes a special pose called `Skeleton`. This is part of the hand tracking implementation. This pose is exposed through the `skeleton` action that is supported outside of the action map system. It is thus always present if hand tracking is supported. You don't need to bind actions to this pose to use it.

Finally, the only output type is `Haptic` and it allows us to set the intensity of haptic feedback, such as controller vibration. Controllers can have multiple haptic outputs and support for haptic vests is coming to OpenXR.

So lets add an action for our aim pose, we do this by clicking on the `+` button for our action set:

The columns in our table are as follows:

| Col | Value    | Description                                                                                                                                                                              |
| --- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | aim_pose | This is the internal name of the action. OpenXR doesn't specify specific restrictions on this name other then size, however some XR runtimes will not like spaces or special characters. |
| 2   | Aim pose | This is a human-readable name for the action. Some XR runtimes will display this name to the end user, for example in configuration dialogs.                                             |
| 3   | Pose     | The type of this action.                                                                                                                                                                 |

OpenXR defines a number of bindable input poses that are commonly available for controllers. There are no rules for which poses are supported for different controllers. The poses OpenXR currently defines are:

- The aim pose on most controllers is positioned slightly in front of the controller and aims forward. This is a great pose to use for laser pointers or to align the muzzle of a weapon with.
- The grip pose on most controllers is positioned where the grip button is placed on the controller. The orientation of this pose differs between controllers and can differ for the same controller on different XR runtimes.
- The palm pose on most controllers is positioned in the center of the palm of the hand holding the controller. This is a new pose that is not available on all XR runtimes.

> **Note:** If hand tracking is used, there are currently big differences in implementations between the different XR runtimes. As a result the action map is currently not suitable for hand tracking. Work is being done on this so stay tuned.

Let's complete our list of actions for a very simple shooting game/application:

The actions we have added are:

- movement, which allows the user to move around outside of normal room scale tracking.
- grab, which detects that the user wants to hold something.
- shoot, which detects that the user wants to fire the weapon they are holding.
- haptic, which allows us to output haptic feedback.

Now note that we don't distinguish between the left and right hand. This is something that is determined at the next stage. We've implemented the action system in such a way that you can bind the same action to both hands. The appropriate [XRController3D](../godot_csharp_misc.md) node will emit the signal.

> **Warning:** For both grab and shoot we've used the `Bool` type. As mentioned before, OpenXR does automatic conversions from an analogue controls however not all XR Runtimes currently apply sensible thresholds. We recommend as a workaround to use the `Float` type when interacting with triggers and grip buttons and apply your own threshold. For buttons like A/B/X/Y and similar where there is no analogue option, the `Bool` type works fine.

> **Note:** You can bind the same action to multiple inputs for the same controller on the same profile. In this case the XR runtime will attempt to combine the inputs. - For `Bool` inputs, this will perform an `OR` operation between the buttons.

- For `Float` inputs, this will take the highest value of the bound inputs.
- The behavior for `Pose` inputs is undefined, but the first bound input is likely to be used. You shouldn't bind multiple actions of the same action set to the same controller input. If you do this, or if actions are bound from multiple action sets but they have overlapping priorities, the behavior is undefined. The XR runtime may simply not accept your action map, or it may take this on a first come first serve basis. We are still investigating the restrictions around binding multiple actions to the same output as this scenario makes sense. The OpenXR specification seems to not allow this.

Now that we have our basic actions defined, it's time to hook them up.

### Profiles

In OpenXR controller bindings are captured in so-called "Interaction Profiles". We've shortened it to "Profiles" because it takes up less space.

This generic name is chosen because controllers don't cover the entire system. Currently there are also profiles for trackers, remotes and tracked pens. There are also provisions for devices such as treadmills, haptic vests and such even though those are not part of the specification yet.

> **Warning:** It is important to know that OpenXR has strict checking on supported devices. The core specification identifies a number of controllers and similar devices with their supported inputs and outputs. Every XR runtime must accept these interaction profiles even if they aren't applicable. New devices are added through extensions and XR runtimes must specify which ones they support. XR runtimes that do not support a device added through extensions will not accept these profiles. XR runtimes that do not support added input or output types will often crash if supplied. As such Godot keeps meta data of all available devices, their inputs and outputs and which extension adds support for them. You can create interaction profiles for all devices you wish to support. Godot will filter out those not supported by the XR runtime the user is using. This does mean that in order to support new devices, you might need to update to a more recent version of Godot.

It is however also important to note that the action map has been designed with this in mind. When new devices enter the market, or when your users use devices that you do not have access to, the action map system relies on the XR runtime. It is the XR runtime's job to choose the best fitting interaction profile that has been specified and adapt it for the controller the user is using.

How the XR runtime does this is left to the implementation of the runtime and there are thus vast differences between the runtimes. Some runtimes might even permit users to edit the bindings themselves.

A common approach for a runtime is to look for a matching interaction profile first. If this is not found it will check the most common profiles such as that of the "Touch controller" and do a conversion. If all else fails, it will check the generic **"Simple controller"**.

> **Note:** There is an important conclusion to be made here: When a controller is found, and the action map is applied to it, the XR runtime is not limited to the exact configurations you set up in Godot's action map editor. While the runtime will generally choose a suitable mapping based on one of the bindings you set up in the action map, it can deviate from it. For example, when the Touch controller profile is used any of the following scenarios could be true: - we could be using a Quest 1 controller,

- we could be using a Quest 2 controller,
- we could be using a Quest Pro controller but no Quest Pro profile was given or the XR runtime being used does not support the Quest Pro controller,
- it could be a completely different controller for which no profile was given but the XR runtime is using the touch bindings as a base. Ergo, there currently is no way to know with certainty, which controller the user is actually using.

> **Warning:** Finally, and this trips up a lot of people, the bindings aren't set in stone. It is fully allowed, and even expected, that an XR runtime allows a user to customise the bindings. At the moment none of the XR runtimes offer this functionality though SteamVR has an existing UI from OpenVRs action map system that is still accessible. This is actively being worked on however.

### Our first controller binding

Let's set up our first controller binding, using the Touch controller as an example.

Press "Add profile", find the Touch controller, and add it. If it is not in the list, then it may already have been added.

Our UI now shows panels for both the left and right controllers. The panels contain all of the possible inputs and outputs for each controller. We can use the `+` next to each entry to bind it to an action:

Let's finish our configuration:

Each action is bound the given input or output for both controllers to indicate that we support the action on either controller. The exception is the movement action which is bound only to the right hand controller. It is likely that we would want to use the left hand thumbstick for a different purpose, say a teleport function.

In developing your game/application you have to account for the possibility that the user changes the binding and binds the movement to the left hand thumbstick.

Also note that our shoot and grab boolean actions are linked to inputs of type `Float`. As mentioned before OpenXR will do conversions between the two, but do read the warning given on that subject earlier in this document.

> **Note:** Some of the inputs seem to appear in our list multiple times. For instance we can find the `X` button twice, once as `X click` and then as `X touch`. This is due to the Touch controller having a capacitive sensor. - `X touch` will be true if the user is merely touching the X button.

- `X click` will be true when the user is actually pressing down on the button. Similarly for the thumbstick we have: - `Thumbstick touch` which will be true if the user is touching the thumbstick.
- `Thumbstick` which gives a value for the direction the thumbstick is pushed to.
- `Thumbstick click` which is true when the user is pressing down on the thumbstick. It is important to note that only a select number of XR controllers support touch sensors or have click features on thumbsticks. Keep that in mind when designing your game/application. Make sure these are used for optional features of your game/application.

### The simple controller

The "Simple controller" is a generic controller that OpenXR offers as a fallback. We'll apply our mapping:

As becomes painfully clear, the simple controller is often far too simple and falls short for anything but the simplest of VR games/applications.

This is why many XR runtimes only use it as a last resort and will attempt to use bindings from one of the more popular systems as a fallback first.

> **Note:** Due to the simple controller likely not covering the needs of your game, it is tempting to provide bindings for every controller supported by OpenXR. The default action map seems to suggest this as a valid course of action. As mentioned before, the default action map was designed for ease of migration from Godot 3. It is the recommendation from the OpenXR Working Group that only bindings for controllers actually tested by the developer are setup. The XR runtimes are designed with this in mind. They can perform a better job of rebinding a provided binding than a developer can make educated guesses. Especially as the developer can't test if this leads to a comfortable experience for the end user. This is our advice as well: limit your action map to the interaction profiles for devices you have actually tested your game with. The Oculus Touch controller is widely used as a fallback controller by many runtimes. If you are able to test your game using a Meta Rift or Quest and add this profile there is a high probability your game will work with other headsets.

### Binding Modifiers

One of the main goals of the action map is to remove the need for the application to know the hardware used. However, sometimes the hardware has physical differences that require inputs to be altered in ways other than how they are bound to actions. This need ranges from setting thresholds, to altering the inputs available on a controller.

Binding modifiers are not enabled by default and require enabling in the OpenXR project settings. Also there is no guarantee that these modifiers are supported by every runtime. You will need to consult the support for the runtimes you are targeting and decide whether to rely on the modifiers or implement some form of fallback mechanism.

If you are targeting multiple runtimes that have support for the same controllers, you may need to create separate action maps for each runtime. You can control which action map Godot uses by using different export templates for each runtime and using a custom [feature tag](tutorials_export.md) to set the action map.

In Godot, binding modifiers are divided into two groups: modifiers that work on the interaction profile level, and modifiers that work on individual bindings.

#### Binding modifiers on an interaction profile

Binding modifiers that are applied to the whole interaction profile can be accessed through the modifier button on the right side of the interaction profile editor.

You can add a new modifier by pressing the Add binding modifier button.

> **Warning:** As Godot doesn't know which controllers and runtimes support a modifier, there is no restriction to adding modifiers. Unsupported modifiers will be ignored.

##### Dpad Binding modifier

The dpad binding modifier adds new inputs to an interaction profile for each joystick and thumbpad input on this controller. It turns the input into a dpad with separate up, down, left and right inputs that are exposed as buttons:

> **Note:** Inputs related to extensions are denoted with an asterix.

In order to use the dpad binding modifier you need to enable the dpad binding modifier extension in project settings:

Enabling the extension is enough to make this functionality work using default settings.

Adding the modifier is optional and allows you to fine tune the way the dpad functionality behaves. You can add the modifier multiple times to set different settings for different inputs.

These settings are used as follows:

- `Action Set` defines the action set to which these settings are applied.
- `Input Path` defines the original input that is mapped to the new dpad inputs.
- `Threshold` specifies the threshold value that will enable a dpad action, e.g. a value of `0.6` means that if the distance from center goes above `0.6` the dpad action is pressed.
- `Threshold Released` specifies the threshold value that will disable a dpad action, e.g. a value of `0.4` means that if the distance from center goes below `0.4` the dpad action is released.
- `Center Region` specifies the distance from center that enabled the center action, this is only supported for trackpads.
- `Wedge Angle` specifies the angle of each wedge. A value of `90 degrees` or lower means that up, down, left and right each have a separate slice in which they are in the pressed state. A value above `90 degrees` means that the slices overlap and that multiple actions can be in the pressed state.
- `Is Sticky`, when enabled means that an action stays in the pressed state until the thumbstick or trackpad moves into another wedge even if it has left the wedge for that action.
- `On Haptic` lets us define a haptic output that is automatically activated when an action becomes pressed.
- `Off Haptic` lets us define a haptic output that is automatically activated when an action is released.

#### Binding modifiers on individual bindings

Binding modifiers that are applied to individual bindings can be accessed through the binding modifier button next to action attached to an input:

You can add a new modifier by pressing the Add binding modifier button.

> **Warning:** As Godot doesn't know which inputs on each runtime support a modifier, there is no restriction to adding modifiers. If the modifier extension is unsupported, modifiers will be filtered out at runtime. Modifiers added to the wrong input may result in a runtime error. You should test your action map on the actual hardware and runtime to verify the proper setup.

##### Analog threshold modifier

The analog threshold modifier allows you to specify the thresholds used for any analog input, like the trigger, that has a boolean input. This controls when the input is in the pressed state.

In order to use this modifier you must enable the analog threshold extension in the project settings:

The analog threshold modifier has the following settings:

These are defined as follows:

- `On Threshold` specifies the threshold value that will enable the action, e.g. a value of `0.6` means that when the analog value gets above `0.6` the action is set to the pressed state.
- `Off Threshold` specifies the threshold value that will disable the action, e.g. a value of `0.4` means that when the analog value goes below `0.4` the action is set in to the released state.
- `On Haptic` lets us define a haptic output that is automatically activated when the input is pressed.
- `Off Haptic` lets us define a haptic output that is automatically activated when the input is released.

#### Haptics on modifiers

Modifiers can support automatic haptic output that is triggered when thresholds are reached.

> **Note:** Currently both available modifiers support this feature however there is no rule future modifiers also have this capability. Only one type of haptic feedback is supported but in the future other options may become available.

##### Haptic vibration

The haptic vibration allows us to specify a simple haptic pulse:

It has the following options:

- `Duration` is the duration of the pulse in nanoseconds. `-1` lets the runtime choose an optimal value for a short pulse suitable for the current hardware.
- `Frequency` is the frequency of the pulse in Hz. `0` lets the runtime choose an optimal frequency for a short pulse suitable for the current hardware.
- `Amplitude` is the amplitude of the pulse.

---

## XR full screen effects

When adding custom full screen effects to your XR application, one approach is using a full screen quad and applying effects to that quad's shader. Add a [MeshInstance3D](../godot_csharp_nodes_3d.md) node to your scene as a child of your [XRCamera3D](../godot_csharp_misc.md), and set the `mesh` property to a [QuadMesh](../godot_csharp_rendering.md). Set the width and height of the quad to `2`.

You can then add a shader to your quad to make it cover the screen. This is done by setting the vertex shader's `POSITION` built-in to `vec4(VERTEX.xy, 1.0, 1.0)`. However, when creating an effect that is centered straight ahead in the user's view (such as a vignette effect), the end result may look incorrect in XR.

Below shows captures of the right-eye view with a vignette shader, both from the headset and the render target itself. The left captures are an unmodified shader; the right captures adjust the full screen quad using the projection matrix. While the capture on the left is centered in the render target, it is off-center in the headset view. But, after applying the projection matrix, we see that the effect is centered in the headset itself.

### Applying the projection matrix

To properly center the effect, the `POSITION` of the full screen quad needs to take the asymmetric field of view into account. To do this while also ensuring the quad has full coverage of the entire render target, we can subdivide the quad and apply the projection matrix to the inner vertices. Let's increase the subdivide width and depth of the quad.

Then, in the vertex function of our shader, we apply an offset from the projection matrix to the inner vertices. Here's an example of how you might do this with the above simple vignette shader:

```glsl
shader_type spatial;
render_mode depth_test_disabled, skip_vertex_transform, unshaded, cull_disabled;

// Modify VERTEX.xy using the projection matrix to correctly center the effect.
void vertex() {
        vec2 vert_pos = VERTEX.xy;

        if (length(vert_pos) < 0.99) {
                vec4 offset = PROJECTION_MATRIX * vec4(0.0, 0.0, 1.0, 1.0);
                vert_pos += (offset.xy / offset.w);
        }

        POSITION = vec4(vert_pos, 1.0, 1.0);
}

void fragment() {
        ALBEDO = vec3(0.0);
        ALPHA = dot(UV * 2.0 - 1.0, UV * 2.0 - 1.0) * 2.0;
}
```

> **Note:** For more info on asymmetric FOV and its purpose, see this [Meta Asymmetric Field of View FAQ](https://developers.meta.com/horizon/documentation/unity/unity-asymmetric-fov-faq/).

### Limitations

This full screen effect method has no performance concerns for per-pixel effects such as the above vignette shader. However, it is not recommended to read from the screen texture when using this technique. Full screen effects that require reading from the screen texture effectively disable all rendering performance optimizations in XR. This is because, when reading from the screen texture, Godot makes a full copy of the render buffer; this drastically increases the workload for the GPU and can create performance concerns.

---

## Where to go from here

Now that we have the basics covered there are several options to look at for your XR game dev journey:

- You can take a look at the Advanced topics section.
- You can look at a number of [XR demos here](https://github.com/godotengine/godot-demo-projects/tree/master/xr).
- You can find 3rd party tutorials on our Tutorials and resources page.

### Godot OpenXR vendor plugin

The vendor plugin isn't just for deploying to Android. In the vendor plugin, we implement many OpenXR vendor extensions that unlock unique features on certain devices, or features that are new enough that a standardized implementation is not available yet.

Together with the OpenXR working group we maintain a [client support matrix](https://github.khronos.org/OpenXR-Inventory/extension_support.html#client_matrix) that lists all the OpenXR extensions Godot supports and whether they require the vendor plugin.

### XR Toolkits

There are various XR toolkits available that implement more complex XR logic ready for you to use. We have a small introduction to Godot XR Tools that you can look at, a toolkit developed by core contributors of Godot.

There are more toolkits available for Godot:

- [Godot XR handtracking toolkit](https://github.com/RevolNoom/godot_xr_handtracking) (GDScript)
- [Godot XR Kit](https://github.com/patrykkalinowski/godot-xr-kit) (GDScript)
- [Godot XR Tools](https://github.com/godotvr/godot-xr-tools) (GDScript)
- [NXR](https://github.com/stumpynub/NXR) (C#)

---

## Room scale in XR

One of the staples of XR projects is the ability to walk around freely in a large space. This space is often constrained by the room the player is physically in with tracking sensors placed within this space. With the advent of inside out tracking however ever larger play spaces are possible.

As a developer this introduces a number of interesting challenges. In this document we will look at a number of the challenges you may face and outline some solutions. We'll discuss the issues and challenges for seated XR games in another document.

> **Note:** Often developers sit behind their desk while building the foundation to their game. In this mode the issues with developing for room scale don't show themselves until it is too late. The advice here is to start testing while standing up and walking around as early as possible. Once you are happy your foundation is solid, you can develop in comfort while remaining seated.

In traditional first person games a player is represented by a [CharacterBody3D](../godot_csharp_nodes_3d.md) node. This node is moved by processing traditional controller, mouse or keyboard input. A camera is attached to this node at a location roughly where the player's head will be.

Applying this model to the XR setup, we add an [XROrigin3D](../godot_csharp_misc.md) node as a child of the character body, and add an [XRCamera3D](../godot_csharp_misc.md) as a child of the origin node. At face value this seems to work. However, upon closer examination this model does not take into account that there are two forms of movement in XR. The movement through controller input, and the physical movement of the player in the real world.

As a result, the origin node does not represent the position of the player. It represents the center, or start of, the tracking space in which the player can physically move. As the player moves around their room this movement is represented through the tracking of the player's headset. In game this translates to the camera node's position being updated accordingly. For all intents and purposes, we are tracking a disembodied head. Unless body tracking is available, we have no knowledge of the position or orientation of the player's body.

The first problem this causes is fairly obvious. When the player moves with controller input, we can use the same approach in normal games and move the player in a forward direction. However the player isn't where we think they are and as we move forward we're checking collisions in the wrong location.

The second problem really shows itself when the player walks further away from the center of the tracking space and uses controller input to turn. If we rotate our character body, the player will be moved around the room in a circular fashion.

If we fix the above issues, we will find a third issue. When the path for the player is blocked in the virtual world, the player can still physically move forward.

We will look at solving the first two problem with two separate solutions, and then discuss dealing with the third.

### Origin centric solution

Looking at the first approach for solving this we are going to change our structure. This is the approach currently implemented in XR Tools.

In this setup we mark the character body as top level so it does not move with the origin.

We also have a helper node that tells us where our neck joint is in relation to our camera. We use this to determine where our body center is.

Processing our character movement is now done in three steps.

> **Note:** The [Origin centric movement demo](https://github.com/godotengine/godot-demo-projects/tree/master/xr/openxr_origin_centric_movement) contains a more elaborate example of the technique described below.

### Step 1

In the first step we're going to process the physical movement of the player. We determine where the player is right now, and attempt to move our character body there.

Note that we're returning `true` from our `_process_on_physical_movement` function when we couldn't move our player all the way.

### Step 2

The second step is to handle rotation of the player as a result of user input.

As the input used can differ based on your needs we are simply calling the function `_get_rotational_input`. This function should obtain the necessary input and return the rotational speed in radians per second.

> **Note:** For our example we are going to keep this simple and straight forward. We are not going to worry about comfort features such as snap turning and applying a vignette. We highly recommend implementing such comfort features.

> **Note:** We've added the call for processing our rotation to our physics process but we are only executing this if we were able to move our player fully. This means that if the player moves somewhere they shouldn't, we don't process further movement.

### Step 3

The third and final step is moving the player forwards, backwards or sideways as a result of user input.

Just like with the rotation the inputs differ from project to project so we are simply calling the function `_get_movement_input`. This function should obtain the necessary input and return a directional vector scaled to the required velocity.

> **Note:** Just like with rotation we're keeping it simple. Here too it is advisable to look at adding comfort settings.

### Character body centric solution

In this setup we are going to keep our character body as our root node and as such is easier to combine with traditional game mechanics.

Here we have a standard character body with collision shape, and our XR origin node and camera as normal children. We also have our neck helper node.

Processing our character movement is done in the same three steps but implemented slightly differently.

> **Note:** The [Character centric movement demo](https://github.com/godotengine/godot-demo-projects/tree/master/xr/openxr_character_centric_movement) contains a more elaborate example of the technique described below.

### Step 1

In this approach step 1 is where all the magic happens. Just like with our previous approach we will be applying our physical movement to the character body, but we will counter that movement on the origin node.

This will ensure that the player's location stays in sync with the character body's location.

In essence the code above will move the character body to where the player is, and then move the origin node back in equal amounts. The result is that the player stays centered above the character body.

We start with applying the rotation. The character body should be facing where the player was looking the previous frame. We calculate our camera orientation in the space of the character body. We can now calculate the angle by which the player has rotated their head. We rotate our character body by the same amount so our character body faces the same direction as the player. And then we reverse the rotation on the origin node so the camera ends up aligned with the player again.

For the movement we do much the same. The character body should be where the player was standing the previous frame. We calculate by how much the player has moved from this location. Then we attempt to move the character body to this location.

As the player may hit a collision body and be stopped, we only move the origin point back by the amount we actually moved the character body. The player may thus move away from this location but that will be reflected in the positioning of the player.

As with our previous solution we return true if this is the case.

### Step 2

In this step we again apply the rotation based on controller input. However in this case the code is nearly identical to how one would implement this in a normal first person game.

As the input used can differ based on your needs we are simply calling the function `_get_rotational_input`. This function should obtain the necessary input and return the rotational speed in radians per second.

### Step 3

For step three we again apply the movement based on controller input. However just like at step 2, we can now implement this as we would in a normal first person game.

Just like with the rotation the inputs differ from project to project so we are simply calling the function `_get_movement_input`. This function should obtain the necessary input and return a directional vector scaled to the required velocity.

### When the player walks to somewhere they shouldn't

Think of a situation where the player is outside a locked room. You don't want the player to go into that room until the door is unlocked. You also don't want the player to see what is in this room.

The logic for moving the player through controller input nicely prevents this. The player encounters a static body, and the code prevents the player from moving into the room.

However with XR, nothing is preventing the player from taking a real step forward.

With both the approaches worked out up above we will prevent the character body from moving where the player can't go. As the player has physically moved to this location, the camera will now have moved into the room.

The logical solution would be to prevent the movement altogether and adjust the placement of the XR origin point so the player stays outside of the room.

The problem with this approach is that physical movement is now not replicated in the virtual space. This will cause nausea for the player.

What many XR games do instead, is to measure the distance between where the player physically is, and where the player's virtual body has been left behind. As this distance increases, usually to a distance of a few centimeters, the screen slowly blacks out.

Our solutions up above would allow us to add this logic into the code at the end of step 1.

Further improvements to the code presented could be:

- allowing controller input as long as this distance is still small,
- still applying gravity to the player even when controller input is disabled.

> **Note:** The movement demos in our demo repository contain an example of blacking out the screen when a user walks into restricted areas.

### Further suggestions for improvements

The above provides two good options as starting points for implementing room scale XR games.

A few more things that are worth pointing out that you will likely want to implement:

- The height of the camera can be used to detect whether the player is standing up, crouching, jumping or lying down. You can adjust the size and orientation of the collision shape accordingly. Extra bonus points for adding multiple collision shapes so the head and body have their own, more accurately sized, shapes.
- When a scene first loads, the player may be far away from the center of the tracking space. This could result in the player spawning into a different room than our origin point. The game will now attempt, and fail, to move the player body from the starting point to where the player is standing. You should implement a reset function that moves the origin point so the player is in the correct starting position.

Both of the above improvements require the player to be ready and standing up straight. There is no guarantee as the player may still be putting their headset on.

Many games, including XR Tools, solve this by introducing an intro screen or loading screen where the player must press a button when they are ready. This starting environment is often a large location where the positioning of the player has little impact on what the player sees. When the player is ready, and presses the button, this is the moment you record the position and height of the camera.

---
