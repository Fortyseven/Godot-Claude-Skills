# Godot 4 C# Tutorials — Rendering (Part 1)

> 3 tutorials. C#-specific code examples.

## The Compositor

The compositor is a new feature in Godot 4 that allows control over the rendering pipeline when rendering the contents of a [Viewport](../godot_csharp_rendering.md).

It can be configured on a [WorldEnvironment](../godot_csharp_nodes_3d.md) node where it applies to all Viewports, or it can be configured on a [Camera3D](../godot_csharp_nodes_3d.md) and apply only to the Viewport using that camera.

The [Compositor](../godot_csharp_rendering.md) resource is used to configure the compositor. To get started, create a new compositor on the appropriate node:

> **Note:** The compositor is currently a feature that is only supported by the Mobile and Forward+ renderers.

### Compositor effects

Compositor effects allow you to insert additional logic into the rendering pipeline at various stages. This is an advanced feature that requires a high level of understanding of the rendering pipeline to use to its best advantage.

As the core logic of the compositor effect is called from the rendering pipeline it is important to note that this logic will thus run within the thread on which rendering takes place. Care needs to be taken to ensure we don't run into threading issues.

To illustrate how to use compositor effects we'll create a simple post processing effect that allows you to write your own shader code and apply this full screen through a compute shader. You can find the finished demo project [here](https://github.com/godotengine/godot-demo-projects/tree/master/compute/post_shader).

We start by creating a new script called `post_process_shader.gd`. We'll make this a tool script so we can see the compositor effect work in the editor. We need to extend our node from [CompositorEffect](../godot_csharp_rendering.md). We must also give our script a class name.

post_process_shader.gd

Next we're going to define a constant for our shader template code. This is the boilerplate code that makes our compute shader work.

For more information on how compute shaders work, please check [Using compute shaders](tutorials_shaders.md).

The important bit here is that for every pixel on our screen, our `main` function is executed and inside of this we load the current color value of our pixel, execute our user code, and write our modified color back to our color image.

`#COMPUTE_CODE` gets replaced by our user code.

In order to set our user code, we need an export variable. We'll also define a few script variables we'll be using:

Note the use of a [Mutex](../godot_csharp_core.md) in our code. Most of our implementation gets called from the rendering engine and thus runs within our rendering thread.

We need to ensure that we set our new shader code, and mark our shader code as dirty, without our render thread accessing this data at the same time.

Next we initialize our effect.

The main thing here is setting our `effect_callback_type` which tells the rendering engine at what stage of the render pipeline to call our code.

> **Note:** Currently we only have access to the stages of the 3D rendering pipeline!

We also get a reference to our rendering device, which will come in very handy.

We also need to clean up after ourselves, for this we react to the `NOTIFICATION_PREDELETE` notification:

Note that we do not use our mutex here even though we create our shader inside of our render thread. The methods on our rendering server are thread safe and `free_rid` will be postponed cleaning up the shader until after any frames currently being rendered are finished.

Also note that we are not freeing our pipeline. The rendering device does dependency tracking and as the pipeline is dependent on the shader, it will be automatically freed when the shader is destructed.

From this point onwards our code will run on the rendering thread.

Our next step is a helper function that will recompile the shader if the user code was changed.

At the top of this method we again use our mutex to protect accessing our user shader code and our is dirty flag. We make a local copy of the user shader code if our user shader code is dirty.

If we don't have a new code fragment, we return true if we already have a valid pipeline.

If we do have a new code fragment we embed it in our template code and then compile it.

> **Warning:** The code shown here compiles our new code in runtime. This is great for prototyping as we can immediately see the effect of the changed shader. This prevents precompiling and caching this shader which may be an issues on some platforms such as consoles. Note that the demo project comes with an alternative example where a `glsl` file contains the entire compute shader and this is used. Godot is able to precompile and cache the shader with this approach.

Finally we need to implement our effect callback, the rendering engine will call this at the right stage of rendering.

At the start of this method we check if we have a rendering device, if our callback type is the correct one, and check if we have our shader.

> **Note:** The check for the effect type is only a safety mechanism. We've set this in our `_init` function, however it is possible for the user to change this in the UI.

Our `p_render_data` parameter gives us access to an object that holds data specific to the frame we're currently rendering. We're currently only interested in our render scene buffers, which provide us access to all the internal buffers used by the rendering engine. Note that we cast this to [RenderSceneBuffersRD](../godot_csharp_misc.md) to expose the full API to this data.

Next we obtain our `internal size` which is the resolution of our 3D render buffers before they are upscaled (if applicable), upscaling happens after our post processes have run.

From our internal size we calculate our group size, see our local size in our template shader.

We also populate our push constant so our shader knows our size. Godot does not support structs here **yet** so we use a `PackedFloat32Array` to store this data into. Note that we have to pad this array with a 16 byte alignment. In other words, the length of our array needs to be a multiple of 4.

Now we loop through our views, this is in case we're using multiview rendering which is applicable for stereo rendering (XR). In most cases we will only have one view.

> **Note:** There is no performance benefit to use multiview for post processing here, handling the views separately like this will still enable the GPU to use parallelism if beneficial.

Next we obtain the color buffer for this view. This is the buffer into which our 3D scene has been rendered.

We then prepare a uniform set so we can communicate the color buffer to our shader.

Note the use of our [UniformSetCacheRD](../godot_csharp_misc.md) cache which ensures we can check for our uniform set each frame. As our color buffer can change from frame to frame and our uniform cache will automatically clean up uniform sets when buffers are freed, this is the safe way to ensure we do not leak memory or use an outdated set.

Finally we build our compute list by binding our pipeline, binding our uniform set, pushing our push constant data, and calling dispatch for our groups.

With our compositor effect completed, we now need to add it to our compositor.

On our compositor we expand the compositor effects property and press `Add Element`.

Now we can add our compositor effect:

After selecting our `PostProcessShader` we need to set our user shader code:

```glsl
float gray = color.r * 0.2125 + color.g * 0.7154 + color.b * 0.0721;
color.rgb = vec3(gray);
```

With that all done, our output is in grayscale.

> **Note:** For a more advanced example of post effects, check out the [Radial blur based sky rays](https://github.com/BastiaanOlij/RERadialSunRays) example project created by Bastiaan Olij.

---

## Fixing jitter, stutter and input lag

### What is jitter, stutter and input lag?

_Jitter_ and _stutter_ are two different alterations to visible motion of objects on screen that may affect a game, even when running at full speed. These effects are mostly visible in games where the world moves at a constant speed in a fixed direction, like runners or platformers.

_Input lag_ is unrelated to jitter and stutter, but is sometimes discussed alongside. Input lag refers to visible on-screen delay when performing actions with the mouse, keyboard, controller or touchscreen. It can be related to game code, engine code or external factors (such as hardware). Input lag is most noticeable in games that use the mouse to aim, such as first-person games. Input lag can't be completely eliminated, but it can be reduced in several ways.

### Distinguishing between jitter and stutter

A game running at a normal framerate without exhibiting any effect will appear smooth:

A game exhibiting _jitter_ will shake constantly in a very subtle way:

Finally, a game exhibiting _stutter_ will appear smooth, but appear to _stop_ or _roll back a frame_ every few seconds:

### Jitter

There can be many causes of jitter. The most typical one happens when the game _physics frequency_ (usually 60 Hz) runs at a different resolution than the monitor refresh rate. Check whether your monitor refresh rate is different from 60 Hz.

Sometimes, only some objects appear to jitter (character or background). This happens when they are processed in different time sources (one is processed in the physics step while another is processed in the idle step).

This cause of jitter can be alleviated by enabling [physics interpolation](tutorials_physics.md) in the Project Settings. Physics interpolation will smooth out physics updates by interpolating the transforms of physics objects between physics frames. This way, the visual representation of physics objects will always look smooth no matter the framerate and physics tick rate.

Enabling physics interpolation has some caveats you should be aware of. For example, care should be taken when teleporting objects so that they don't visibly interpolate between the old position and new position when it's not intended. See the [Physics Interpolation](tutorials_physics.md) documentation for details.

> **Note:** Enabling physics interpolation will increase input lag for behavior that depends on the physics tick, such as player movement. In most games, this is generally preferable to jitter, but consider this carefully for games that operate on a fixed framerate (like fighting or rhythm games). This increase in input lag can be compensated by increasing the physics tick rate as described in the **Input lag** section.

### Stutter

Stutter may happen due to several different reasons. One reason is the game not being able to keep full framerate performance due to a CPU or GPU bottleneck. Solving this is game-specific and will require [optimization](tutorials_performance.md).

Another common reason for stuttering is _shader compilation stutter_. This occurs when a shader needs to be compiled when a new material or particle effect is spawned for the first time in a game. This kind of stuttering generally only happens on the first playthrough, or after a graphics driver update when the shader cache is invalidated.

Since Godot 4.4, when using the Forward+ or Mobile renderers, the engine tries to avoid shader compilation stutter using an ubershader approach. For this approach to be most effective, care must be taken when designing scenes and resources so that Godot can gather as much information as possible when the scene/resource is loaded, as opposed as to when it's being drawn for the first time. See [Reducing stutter from shader (pipeline) compilations](tutorials_performance.md) for more information.

However, when using the Compatibility renderer, it is not possible to use this ubershader approach due to technical limitations in OpenGL. Therefore, to avoid shader compilation stutter in the Compatibility renderer, you need to spawn every mesh and visual effect in front of the camera for a single frame when the level is loading. This will ensure the shader is compiled when the level is loaded, as opposed to occurring during gameplay. This can be done behind solid 2D UI (such as a fullscreen [ColorRect](../godot_csharp_ui_controls.md) node) so that it's not visible to the player.

> **Note:** On platforms that support disabling V-Sync, stuttering can be made less noticeable by disabling V-Sync in the project settings. This will however cause tearing to appear, especially on monitors with low refresh rates. If your monitor supports it, consider enabling variable refresh rate (G-Sync/FreeSync) while leaving V-Sync enabled. This allows mitigating some forms of stuttering without introducing tearing. However, it will not help with large stutters, such as the ones caused by shader compilation stutter. Forcing your graphics card to use the maximum performance profile can also help reduce stuttering, at the cost of increased GPU power draw.

Additionally, stutter may be induced by the underlying operating system. Here is some information regarding stutter on different OSes:

#### Windows

Windows is known to cause stutter in windowed games. This mostly depends on the hardware installed, drivers version and processes running in parallel (e.g. having many browser tabs open may cause stutter in a running game). To avoid this, Godot raises the game priority to "Above Normal". This helps considerably, but may not completely eliminate stutter.

Eliminating this completely requires giving your game full privileges to become "Time Critical", which is not advised. Some games may do it, but it is advised to learn to live with this problem, as it is common for Windows games and most users won't play games windowed (games that are played in a window, e.g. puzzle games, will usually not exhibit this problem anyway).

For fullscreen, Windows gives special priority to the game so stutter is no longer visible and very rare. This is how most games are played.

When using a mouse with a polling rate of 1,000 Hz or more, consider using a fully up-to-date Windows 11 installation which comes with fixes related to high CPU utilization with high polling rate mice. These fixes are not available in Windows 10 and older versions.

> **Tip:** Games should use the **Exclusive Fullscreen** window mode, as opposed to **Fullscreen** which is designed to prevent Windows from automatically treating the window as if it was exclusive fullscreen. **Fullscreen** is meant to be used by GUI applications that want to use per-pixel transparency without a risk of having it disabled by the OS. It achieves this by leaving a 1-pixel line at the bottom of the screen. By contrast, **Exclusive Fullscreen** uses the actual screen size and allows Windows to reduce jitter and input lag for fullscreen games.

#### Linux

Stutter may be visible on desktop Linux, but this is usually associated with different video drivers and compositors. Some compositors may also trigger this problem (e.g. KWin), so it is advised to try using a different one to rule it out as the cause. Some window managers such as KWin and Xfwm allow you to manually disable compositing, which can improve performance (at the cost of tearing).

There is no workaround for driver or compositor stuttering, other than reporting it as an issue to the driver or compositor developers. Stutter may be more present when playing in windowed mode as opposed to fullscreen, even with compositing disabled.

[Feral GameMode](https://github.com/FeralInteractive/gamemode) can be used to automatically apply optimizations (such as forcing the GPU performance profile) when running specific processes.

#### macOS

Generally, macOS is stutter-free, although recently some bugs were reported when running on fullscreen (this is a macOS bug). If you have a machine exhibiting this behavior, please let us know.

#### Android

Generally, Android is stutter and jitter-free because the running activity gets all the priority. That said, there may be problematic devices (older Kindle Fire is known to be one). If you see this problem on Android, please let us know.

#### iOS

iOS devices are generally stutter-free, but older devices running newer versions of the operating system may exhibit problems. This is generally unavoidable.

### Input lag

#### Project configuration

On platforms that support disabling V-Sync, input lag can be made less noticeable by disabling V-Sync in the project settings. This will however cause tearing to appear, especially on monitors with low refresh rates. It's suggested to make V-Sync available as an option for players to toggle.

When using the Forward+ or Mobile rendering methods, another way to reduce visual latency when V-Sync is enabled is to use double-buffered V-Sync instead of the default triple-buffered V-Sync. Since Godot 4.3, this can be achieved by reducing the **Display > Window > V-Sync > Swapchain Image Count** project setting to `2`. The downside of using double buffering is that framerate will be less stable if the display refresh rate can't be reached due to a CPU or GPU bottleneck. For instance, on a 60 Hz display, if the framerate would normally drop to 55 FPS during gameplay with triple buffering, it will have to drop down to 30 FPS momentarily with double buffering (and then go back to 60 FPS when possible). As a result, double-buffered V-Sync is only recommended if you can _consistently_ reach the display refresh rate on the target hardware.

Increasing the number of physics iterations per second can also reduce physics-induced input latency. This is especially noticeable when using physics interpolation (which improves smoothness but increases latency). To do so, set **Physics > Common > Physics Ticks Per Second** to a value higher than the default `60`, or set `Engine.physics_ticks_per_second` at runtime in a script. Values that are a multiple of the monitor refresh rate (typically `60`) work best when physics interpolation is disabled, as they will avoid jitter. This means values such as `120`, `180` and `240` are good starting points. As a bonus, higher physics FPSes make tunneling and physics instability issues less likely to occur.

The downside of increasing physics FPS is that CPU usage will increase, which can lead to performance bottlenecks in games that have heavy physics simulation code. This can be alleviated by increasing physics FPS only in situations where low latency is critical, or by letting players adjust physics FPS to match their hardware. However, different physics FPS will lead to different outcomes in physics simulation, even when `delta` is consistently used in your game logic. This can give certain players an advantage over others. Therefore, allowing the player to change the physics FPS themselves should be avoided for competitive multiplayer games.

Lastly, you can disable input buffering on a per-rendered frame basis by calling `Input.set_use_accumulated_input(false)` in a script. This will make it so the `_input()` and `_unhandled_input()` functions in your scripts are called on every input, rather than accumulating inputs and waiting for a frame to be rendered. Disabling input accumulation will increase CPU usage, so it should be done with caution.

> **Tip:** On any Godot project, you can use the `--disable-vsync` [command line argument](tutorials_editor.md) to forcibly disable V-Sync. Since Godot 4.2, `--max-fps <fps>` can also be used to set an FPS limit (`0` is unlimited). These arguments can be used at the same time.

#### Hardware/OS-specific

If your monitor supports it, consider enabling variable refresh rate (G-Sync/FreeSync) while leaving V-Sync enabled, then cap the framerate in the project settings to a slightly lower value than your monitor's maximum refresh rate as per [this page](https://blurbusters.com/howto-low-lag-vsync-on/). For example, on a 144 Hz monitor, you can set the project's framerate cap to `141`. This may be counterintuitive at first, but capping the FPS below the maximum refresh rate range ensures that the OS never has to wait for vertical blanking to finish. This leads to _similar_ input lag as V-Sync disabled with the same framerate cap (usually less than 1 ms greater), but without any tearing.

This can be done by changing the **Application > Run > Max FPS** project setting or assigning `Engine.max_fps` at runtime in a script.

On some platforms, you can also opt into a low-latency mode in the graphics driver options (such as the NVIDIA Control Panel on Windows). The **Ultra** setting will give you the lowest possible latency, at the cost of slightly lower average framerates. Forcing the GPU to use the maximum performance profile can also further reduce input lag, at the cost of higher power consumption (and resulting heat/fan noise).

Finally, make sure your monitor is running at its highest possible refresh rate in the OS' display settings.

Also, ensure that your mouse is configured to use its highest polling rate (typically 1,000 Hz for gaming mice, sometimes more). High USB polling rates can however result in high CPU usage, so 500 Hz may be a safer bet on low-end CPUs. If your mouse offers multiple DPI settings, consider also [using the highest possible setting and reducing in-game sensitivity to reduce mouse latency](https://www.youtube.com/watch?v=6AoRfv9W110).

On Linux when using X11, disabling compositing in window managers that allow it (such as KWin or Xfwm) can reduce input lag significantly.

### Reporting jitter, stutter or input lag problems

If you are reporting a stutter or jitter problem (opening an issue) not caused by any of the above reasons, please specify very clearly all the information possible about device, operating system, driver versions, etc. This may help to better troubleshoot it.

If you are reporting input lag problems, please include a capture made with a high speed camera (such as your phone's slow motion video mode). The capture **must** have both the screen and the input device visible so that the number of frames between an input and the on-screen result can be counted. Also, make sure to mention your monitor's refresh rate and your input device's polling rate (especially for mice).

Also, make sure to use the correct term (jitter, stutter, input lag) based on the exhibited behavior. This will help understand your issue much faster. Provide a project that can be used to reproduce the issue, and if possible, include a screen capture demonstrating the bug.

---

## Multiple resolutions

### The problem of multiple resolutions

Developers often have trouble understanding how to best support multiple resolutions in their games. For desktop and console games, this is more or less straightforward, as most screen aspect ratios are 16:9 and resolutions are standard (720p, 1080p, 1440p, 4K, …).

For mobile games, at first, it was easy. For many years, the iPhone and iPad used the same resolution. When _Retina_ was implemented, they just doubled the pixel density; most developers had to supply assets in default and double resolutions.

Nowadays, this is no longer the case, as there are plenty of different screen sizes, densities, and aspect ratios. Non-conventional sizes are also becoming increasingly popular, such as ultrawide displays.

For 3D rendering, there is not much of a need to support multiple resolutions. Thanks to its vector-based nature, 3D geometry will just fill the screen based on the viewport size. For 2D and game UIs, this is a different matter, as art needs to be created using specific pixel sizes in software such as Photoshop, GIMP or Krita.

Since layouts, aspect ratios, resolutions, and pixel densities can change so much, it is no longer possible to design UIs for every specific screen. Another method must be used.

### One size fits all

The most common approach is to use a single _base_ resolution and then fit it to everything else. This resolution is how most players are expected to play the game (given their hardware). For mobile, Google has useful [stats](https://developer.android.com/about/dashboards) online, and for desktop, Steam [also does](https://store.steampowered.com/hwsurvey/).

As an example, Steam shows that the most common _primary display resolution_ is 1920×1080, so a sensible approach is to develop a game for this resolution, then handle scaling for different sizes and aspect ratios.

Godot provides several useful tools to do this easily.

> **See also:** You can see how Godot's support for multiple resolutions works in action using the [Multiple Resolutions and Aspect Ratios demo project](https://github.com/godotengine/godot-demo-projects/tree/master/gui/multiple_resolutions).

### Base size

A base size for the window can be specified in the Project Settings under **Display → Window**.

However, what it does is not completely obvious; the engine will _not_ attempt to switch the monitor to this resolution. Rather, think of this setting as the "design size", i.e. the size of the area that you work with in the editor. This setting corresponds directly to the size of the blue rectangle in the 2D editor.

There is often a need to support devices with screen and window sizes that are different from this base size. Godot offers many ways to control how the viewport will be resized and stretched to different screen sizes.

> **Note:** On this page, _window_ refers to the screen area allotted to your game by the system, while _viewport_ refers to the root object (accessible from `get_tree().root`) which the game controls to fill this screen area. This viewport is a [Window](../godot_csharp_ui_controls.md) instance. Recall from the introduction that _all_ Window objects are viewports.

To configure the stretch base size at runtime from a script, use the `get_tree().root.content_scale_size` property (see [Window.content_scale_size](../godot_csharp_ui_controls.md)). Changing this value can indirectly change the size of 2D elements. However, to provide a user-accessible scaling option, using **Stretch Scale** is recommended as it's easier to adjust.

> **Note:** Godot follows a modern approach to multiple resolutions. The engine will never change the monitor's resolution on its own. While changing the monitor's resolution is the most efficient approach, it's also the least reliable approach as it can leave the monitor stuck on a low resolution if the game crashes. This is especially common on macOS or Linux which don't handle resolution changes as well as Windows. Changing the monitor's resolution also removes any control from the game developer over filtering and aspect ratio stretching, which can be important to ensure correct display for pixel art games. On top of that, changing the monitor's resolution makes alt-tabbing in and out of a game much slower since the monitor has to change resolutions every time this is done.

### Resizing

There are several types of devices, with several types of screens, which in turn have different pixel density and resolutions. Handling all of them can be a lot of work, so Godot tries to make the developer's life a little easier. The [Viewport](../godot_csharp_rendering.md) node has several functions to handle resizing, and the root node of the scene tree is always a viewport (scenes loaded are instanced as a child of it, and it can always be accessed by calling `get_tree().root` or `get_node("/root")`).

In any case, while changing the root Viewport params is probably the most flexible way to deal with the problem, it can be a lot of work, code and guessing, so Godot provides a set of parameters in the project settings to handle multiple resolutions.

> **Tip:** To render 3D at a lower resolution than 2D elements (without needing separate viewports), you can use Godot's [resolution scaling](tutorials_3d.md) support. This is a good way to improve performance significantly in GPU-bottlenecked scenarios. This works with any stretch mode and stretch aspect combination.

### Stretch settings

Stretch settings are located in the project settings and provide several options:

#### Stretch Mode

The **Stretch Mode** setting defines how the base size is stretched to fit the resolution of the window or screen. The animations below use a "base size" of just 16×9 pixels to demonstrate the effect of different stretch modes. A single sprite, also 16×9 pixels in size, covers the entire viewport, and a diagonal [Line2D](../godot_csharp_nodes_2d.md) is added on top of it:

- **Stretch Mode = Disabled** (default): No stretching happens. One unit in the scene corresponds to one pixel on the screen. In this mode, the **Stretch Aspect** setting has no effect.
- **Stretch Mode = Canvas Items**: In this mode, the base size specified in width and height in the project settings is stretched to cover the whole screen (taking the **Stretch Aspect** setting into account). This means that everything is rendered directly at the target resolution. 3D is unaffected, while in 2D, there is no longer a 1:1 correspondence between sprite pixels and screen pixels, which may result in scaling artifacts.
- **Stretch Mode = Viewport**: Viewport scaling means that the size of the root [Viewport](../godot_csharp_rendering.md) is set precisely to the base size specified in the Project Settings' **Display** section. The scene is rendered to this viewport first. Finally, this viewport is scaled to fit the screen (taking the **Stretch Aspect** setting into account).

To configure the stretch mode at runtime from a script, use the `get_tree().root.content_scale_mode` property (see [Window.content_scale_mode](../godot_csharp_ui_controls.md) and the [ContentScaleMode](../godot_csharp_misc.md) enum).

#### Stretch Aspect

The second setting is the stretch aspect. Note that this only takes effect if **Stretch Mode** is set to something other than **Disabled**.

In the animations below, you will notice gray and black areas. The black areas are added by the engine and cannot be drawn into. The gray areas are part of your scene, and can be drawn to. The gray areas correspond to the region outside the blue frame you see in the 2D editor.

- **Stretch Aspect = Ignore**: Ignore the aspect ratio when stretching the screen. This means that the original resolution will be stretched to exactly fill the screen, even if it's wider or narrower. This may result in nonuniform stretching: things looking wider or taller than designed.
- **Stretch Aspect = Keep**: Keep aspect ratio when stretching the screen. This means that the viewport retains its original size regardless of the screen resolution, and black bars will be added to the top/bottom of the screen ("letterboxing") or the sides ("pillarboxing").

This is a good option if you know the aspect ratio of your target devices in advance, or if you don't want to handle different aspect ratios.

- **Stretch Aspect = Keep Width**: Keep aspect ratio when stretching the screen. If the screen is wider than the base size, black bars are added at the left and right (pillarboxing). But if the screen is taller than the base resolution, the viewport will be grown in the vertical direction (and more content will be visible to the bottom). You can also think of this as "Expand Vertically".

This is usually the best option for creating GUIs or HUDs that scale, so some controls can be anchored to the bottom ([Size and anchors](tutorials_ui.md)).

- **Stretch Aspect = Keep Height**: Keep aspect ratio when stretching the screen. If the screen is taller than the base size, black bars are added at the top and bottom (letterboxing). But if the screen is wider than the base resolution, the viewport will be grown in the horizontal direction (and more content will be visible to the right). You can also think of this as "Expand Horizontally".

This is usually the best option for 2D games that scroll horizontally (like runners or platformers).

- **Stretch Aspect = Expand**: Keep aspect ratio when stretching the screen, but keep neither the base width nor height. Depending on the screen aspect ratio, the viewport will either be larger in the horizontal direction (if the screen is wider than the base size) or in the vertical direction (if the screen is taller than the original size).

> **Tip:** To support both portrait and landscape mode with a similar automatically determined scale factor, set your project's base resolution to be a _square_ (1:1 aspect ratio) instead of a rectangle. For instance, if you wish to design for 1280×720 as the base resolution but wish to support both portrait and landscape mode, use 720×720 as the project's base window size in the Project Settings. To allow the user to choose their preferred screen orientation at runtime, remember to set **Display > Window > Handheld > Orientation** to `sensor`.

To configure the stretch aspect at runtime from a script, use the `get_tree().root.content_scale_aspect` property (see [Window.content_scale_aspect](../godot_csharp_ui_controls.md) and the [ContentScaleAspect](../godot_csharp_misc.md) enum).

#### Stretch Scale

The **Scale** setting allows you to add an extra scaling factor on top of what the **Stretch** options above already provide. The default value of `1.0` means that no additional scaling occurs.

For example, if you set **Scale** to `2.0` and leave **Stretch Mode** on **Disabled**, each unit in your scene will correspond to 2×2 pixels on the screen. This is a good way to provide scaling options for non-game applications.

If **Stretch Mode** is set to **canvas_items**, 2D elements will be scaled relative to the base window size, then multiplied by the **Scale** setting. This can be exposed to players to allow them to adjust the automatically determined scale to their liking, for better accessibility.

If **Stretch Mode** is set to **viewport**, the viewport's resolution is divided by **Scale**. This makes pixels look larger and reduces rendering resolution (with a given window size), which can improve performance.

To configure the stretch scale at runtime from a script, use the `get_tree().root.content_scale_factor` property (see [Window.content_scale_factor](../godot_csharp_ui_controls.md)).

You can also adjust the scale at which the default project theme is generated using the **GUI > Theme > Default Theme Scale** project setting. This can be used to create more logically-sized UIs at base resolutions that are significantly higher or lower than the default. However, this project setting cannot be changed at runtime, as its value is only read once when the project starts.

#### Stretch Scale Mode

Since Godot 4.2, the **Stretch Scale Mode** setting allows you to constrain the automatically determined scale factor (as well as the manually specified **Stretch Scale** setting) to integer values. By default, this setting is set to `fractional`, which allows any scale factor to be applied (including fractional values such as `2.5`). When set to `integer`, the value is rounded down to the nearest integer. For example, instead of using a scale factor of `2.5`, it would be rounded down to `2.0`. This is useful to prevent distortion when displaying pixel art.

Compare this pixel art which is displayed with the `viewport` stretch mode, with the stretch scale mode set to `fractional`:

This pixel art is also displayed with the `viewport` stretch mode, but the stretch scale mode is set to `integer` this time:

For example, if your viewport base size is 640×360 and the window size is 1366×768:

- When using `fractional`, the viewport is displayed at a resolution of 1366×768 (scale factor is roughly 2.133×). The entire window space is used. Each pixel in the viewport corresponds to 2.133×2.133 pixels in the displayed area. However, since displays can only display "whole" pixels, this will lead to uneven pixel scaling which results in incorrect appearance of pixel art.
- When using `integer`, the viewport is displayed at a resolution of 1280×720 (scale factor is 2×). The remaining space is filled with black bars on all four sides, so that each pixel in the viewport corresponds to 2×2 pixels in the displayed area.

This setting is effective with any stretch mode. However, when using the `disabled` stretch mode, it will only affect the **Stretch Scale** setting by rounding it _down_ to the nearest integer value. This can be used for 3D games that have a pixel art UI, so that the visible area in the 3D viewport doesn't reduce in size (which occurs when using `canvas_items` or `viewport` stretch mode with the `integer` scale mode).

> **Tip:** Games should use the **Exclusive Fullscreen** window mode, as opposed to **Fullscreen** which is designed to prevent Windows from automatically treating the window as if it was exclusive fullscreen. **Fullscreen** is meant to be used by GUI applications that want to use per-pixel transparency without a risk of having it disabled by the OS. It achieves this by leaving a 1-pixel line at the bottom of the screen. By contrast, **Exclusive Fullscreen** uses the actual screen size and allows Windows to reduce jitter and input lag for fullscreen games. When using integer scaling, this is particularly important as the 1-pixel height reduction from the **Fullscreen** mode can cause integer scaling to use a smaller scale factor than expected.

### Common use case scenarios

The following settings are recommended to support multiple resolutions and aspect ratios well.

#### Desktop game

**Non-pixel art:**

- Set the base window width to `1920` and window height to `1080`. If you have a display smaller than 1920×1080, set **Window Width Override** and **Window Height Override** to lower values to make the window smaller when the project starts.
- Alternatively, if you're targeting high-end devices primarily, set the base window width to `3840` and window height to `2160`. This allows you to provide higher resolution 2D assets, resulting in crisper visuals at the cost of higher memory usage and file sizes. You'll also want to increase **GUI > Theme > Default Theme Scale** to a value between `2.0` and `3.0` to ensure UI elements remain readable.

- Note that this will make non-mipmapped textures grainy on low resolution devices, so make sure to follow the instructions described in **Reducing aliasing on downsampling**.
- Set the stretch mode to `canvas_items`.
- Set the stretch aspect to `expand`. This allows for supporting multiple aspect ratios and makes better use of tall smartphone displays (such as 18:9 or 19:9 aspect ratios).
- Configure Control nodes' anchors to snap to the correct corners using the **Layout** menu.
- For 3D games, consider exposing [Resolution scaling](tutorials_3d.md) in the game's options menu to allow players to adjust the 3D rendering resolution separately from UI elements. This is useful for performance tuning, especially on lower-end hardware.

**Pixel art:**

- Set the base window size to the viewport size you intend to use. Most pixel art games use viewport sizes between 256×224 and 640×480. 640×360 is a good baseline, as it scales to 1280×720, 1920×1080, 2560×1440, and 3840×2160 without any black bars when using integer scaling. Higher viewport sizes will require using higher resolution artwork, unless you intend to show more of the game world at a given time.
- Set the stretch mode to `viewport`.
- Set the stretch aspect to `keep` to enforce a single aspect ratio (with black bars). As an alternative, you can set the stretch aspect to `expand` to support multiple aspect ratios.
- If using the `expand` stretch aspect, Configure Control nodes' anchors to snap to the correct corners using the **Layout** menu.
- Set the stretch scale mode to `integer`. This prevents uneven pixel scaling from occurring, which makes pixel art not display as intended.

> **Note:** The `viewport` stretch mode provides low-resolution rendering that is then stretched to the final window size. If you are OK with sprites being able to move or rotate in "sub-pixel" positions or wish to have a high resolution 3D viewport, you should use the `canvas_items` stretch mode instead of the `viewport` stretch mode.

#### Mobile game in landscape mode

Godot is configured to use landscape mode by default. This means you don't need to change the display orientation project setting.

- Set the base window width to `1280` and window height to `720`.
- Alternatively, if you're targeting high-end devices primarily, set the base window width to `1920` and window height to `1080`. This allows you to provide higher resolution 2D assets, resulting in crisper visuals at the cost of higher memory usage and file sizes. Many devices have even higher resolution displays (1440p), but the difference with 1080p is barely visible given the small size of smartphone displays. You'll also want to increase **GUI > Theme > Default Theme Scale** to a value between `1.5` and `2.0` to ensure UI elements remain readable.

- Note that this will make non-mipmapped textures grainy on low resolution devices, so make sure to follow the instructions described in **Reducing aliasing on downsampling**.
- Set the stretch mode to `canvas_items`.
- Set the stretch aspect to `expand`. This allows for supporting multiple aspect ratios and makes better use of tall smartphone displays (such as 18:9 or 19:9 aspect ratios).
- Configure Control nodes' anchors to snap to the correct corners using the **Layout** menu.

> **Tip:** To better support tablets and foldable phones (which frequently feature displays with aspect ratios close to 4:3), consider using a base resolution that has a 4:3 aspect ratio while following the rest of the instructions here. For instance, you can set the base window width to `1280` and the base window height to `960`.

#### Mobile game in portrait mode

- Set the base window width to `720` and window height to `1280`.
- Alternatively, if you're targeting high-end devices primarily, set the base window width to `1080` and window height to `1920`. This allows you to provide higher resolution 2D assets, resulting in crisper visuals at the cost of higher memory usage and file sizes. Many devices have even higher resolution displays (1440p), but the difference with 1080p is barely visible given the small size of smartphone displays. You'll also want to increase **GUI > Theme > Default Theme Scale** to a value between `1.5` and `2.0` to ensure UI elements remain readable.

- Note that this will make non-mipmapped textures grainy on low resolution devices, so make sure to follow the instructions described in **Reducing aliasing on downsampling**.
- Set **Display > Window > Handheld > Orientation** to `portrait`.
- Set the stretch mode to `canvas_items`.
- Set the stretch aspect to `expand`. This allows for supporting multiple aspect ratios and makes better use of tall smartphone displays (such as 18:9 or 19:9 aspect ratios).
- Configure Control nodes' anchors to snap to the correct corners using the **Layout** menu.

> **Tip:** To better support tablets and foldable phones (which frequently feature displays with aspect ratios close to 4:3), consider using a base resolution that has a 3:4 aspect ratio while following the rest of the instructions here. For instance, you can set the base window width to `960` and the base window height to `1280`.

#### Non-game application

- Set the base window width and height to the smallest window size that you intend to target. This is not required, but this ensures that you design your UI with small window sizes in mind.
- Keep the stretch mode to its default value, `disabled`.
- Keep the stretch aspect to its default value, `keep` (its value won't be used since the stretch mode is `disabled`).
- You can define a minimum window size by setting `get_window().min_size` in a script's `_ready()` function. This prevents the user from resizing the application below a certain size, which could break the UI layout.
- Add a setting in the application's settings to change the root viewport's **stretch scale**, so that the UI can be made larger to account for hiDPI displays. See also the section on hiDPI support below.

### hiDPI support

By default, Godot projects are considered DPI-aware by the operating system. This is controlled by the **Display > Window > DPI > Allow hiDPI** project setting, which should be left enabled whenever possible. Disabling DPI awareness can break fullscreen behavior on Windows.

Since Godot projects are DPI-aware, they may appear at a very small window size when launching on an hiDPI display (proportionally to the screen resolution). For a game, the most common way to work around this issue is to make them fullscreen by default. Alternatively, you could set the window size in an [autoload](tutorials_scripting.md)'s `_ready()` function according to the screen size.

To ensure 2D elements don't appear too small on hiDPI displays:

- For games, use the `canvas_items` or `viewport` stretch modes so that 2D elements are automatically resized according to the current window size.
- For non-game applications, use the `disabled` stretch mode and set the stretch scale to a value corresponding to the display scale factor in an [autoload](tutorials_scripting.md)'s `_ready()` function. The display scale factor is set in the operating system's settings and can be queried using [screen_get_scale](../godot_csharp_misc.md). This method is currently implemented on Android, iOS, Linux (Wayland only), macOS and Web. On other platforms, you'll have to implement a method to guess the display scale factor based on the screen resolution (with a setting to let the user override this if needed). This is the approach currently used by the Godot editor.

The **Allow hiDPI** setting is only effective on Windows and macOS. It's ignored on all other platforms.

> **Note:** The Godot editor itself is always marked as DPI-aware. Running the project from the editor will only be DPI-aware if **Allow hiDPI** is enabled in the Project Settings.

### Reducing aliasing on downsampling

If the game has a very high base resolution (e.g. 3840×2160), aliasing might appear when downsampling to something considerably lower like 1280×720.

To resolve this, you can [enable mipmaps](tutorials_assets_pipeline.md) on all your 2D textures. However, enabling mipmaps will increase memory usage which can be an issue on low-end mobile devices.

### Handling aspect ratios

Once scaling for different resolutions is accounted for, make sure that your _user interface_ also scales for different aspect ratios. This can be done using [anchors](tutorials_ui.md) and/or [containers](tutorials_ui.md).

### Field of view scaling

The 3D Camera node's **Keep Aspect** property defaults to the **Keep Height** scaling mode (also called _Hor+_). This is usually the best value for desktop games and mobile games in landscape mode, as widescreen displays will automatically use a wider field of view.

However, if your 3D game is intended to be played in portrait mode, it may make more sense to use **Keep Width** instead (also called _Vert-_). This way, smartphones with an aspect ratio taller than 16:9 (e.g. 19:9) will use a _taller_ field of view, which is more logical here.

### Scaling 2D and 3D elements differently

To render 3D at a different resolution from 2D elements (such as the UI), use Godot's [resolution scaling](tutorials_3d.md) functionality. This allows you to control the resolution scale factor used for 3D without needing to use a separate Viewport node. This can either be used to improve performance by rendering 3D at a lower resolution, or improve quality via supersampling.

---
