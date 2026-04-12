# Godot 4 C# Tutorials — Rendering (Part 2)

> 2 tutorials. C#-specific code examples.

## Overview of renderers

> **See also:** This page gives an overview of Godot's renderers, focusing on the differences between their rendering features. For more technical details on the renderers, see Internal rendering architecture.

### Introduction

Godot 4 includes three renderers:

- **Forward+**. The most advanced renderer, suited for desktop platforms only. Used by default on desktop platforms. This renderer uses **Vulkan**, **Direct3D 12**, or **Metal** as the rendering driver, and it uses the **RenderingDevice** backend.
- **Mobile**. Fewer features, but renders simple scenes faster. Suited for mobile and desktop platforms. Used by default on mobile platforms. This renderer uses **Vulkan**, **Direct3D 12**, or **Metal** as the rendering driver, and it uses the **RenderingDevice** backend.
- **Compatibility**, sometimes called **GL Compatibility**. The least advanced renderer, suited for low-end desktop and mobile platforms. Used by default on the web platform. This renderer uses **OpenGL** as the rendering driver.

#### Renderers, rendering drivers, and RenderingDevice

The _renderer_, or _rendering method_, determines which features are available. Most of the time, this is the only thing you need to think about. Godot's renderers are **Forward+**, **Mobile**, and **Compatibility**.

The _rendering driver_ tells the GPU what to do, using a graphics API. Godot can use the **OpenGL**, **Vulkan**, **Direct3D 12**, and **Metal** rendering drivers. Not every GPU supports every rendering driver, and therefore not every GPU supports all renderers. Vulkan, Direct3D 12, and Metal are modern, low-level graphics APIs, and requires newer hardware. OpenGL is an older graphics API that runs on most hardware.

RenderingDevice is a _rendering backend_, an abstraction layer between the renderer and the rendering driver. It is used by the Forward+ and Mobile renderers, and these renderers are sometimes called "RenderingDevice-based renderers".

### Choosing a renderer

Choosing a renderer is a complex question, and depends on your hardware and the which platforms you are developing for. As a starting point:

Choose **Forward+** if:

- You are developing for desktop.
- You have relatively new hardware which supports Vulkan, Direct3D 12, or Metal.
- You are developing a 3D game.
- You want to use the most advanced rendering features.

Choose **Mobile** if:

- You are developing for newer mobile devices, desktop XR, or desktop.
- You have relatively new hardware which supports Vulkan, Direct3D 12, or Metal.
- You are developing a 3D game.
- You want to use advanced rendering features, subject to the limitations of mobile hardware.

Choose **Compatibility** if:

- You are developing for older mobile devices, older desktop devices, or standalone XR. The Compatibility renderer supports the widest range of hardware.
- You are developing for web. In this case, Compatibility is the only choice.
- You have older hardware which does not support Vulkan. In this case, Compatibility is the only choice.
- You are developing a 2D game, or a 3D game which does not need advanced rendering features.
- You want the best performance possible on all devices and don't need advanced rendering features.

Keep in mind every game is unique, and this is only a starting point. For example, you might choose to use the Compatibility renderer even though you have the latest GPU, so you can support the widest range of hardware. Or you might want to use the Forward+ renderer for a 2D game, so you can use advanced features like compute shaders.

#### Switching between renderers

In the editor, you can always switch between renderers by clicking on the renderer name in the upper-right corner of the editor.

Switching between renderers may require some manual tweaks to your scene, lighting, and environment, since each renderer is different. In general, switching between the Mobile and Forward+ renderers will require fewer adjustments than switching between the Compatibility renderer and the Forward+ or Mobile renderers.

Since Godot 4.4, when using Forward+ or Mobile, if Vulkan is not supported, the engine will fall back to Direct3D 12 and vice versa. If the attempted fallback driver is not supported either, the engine will then fall back to Compatibility when the RenderingDevice backend is not supported. This allows the project to run anyway, but it may look different than the intended appearance due to the more limited renderer. This behavior can be disabled in the project settings by unchecking [Rendering > Rendering Device > Fallback to OpenGL 3](../godot_csharp_misc.md).

### Feature comparison

This is not a complete list of the features of each renderer. If a feature is not listed here, it is available in all renderers, though it may be much faster on some renderers. For a list of _all_ features in Godot, see List of features (see About docs).

Hardware with RenderingDevice support is hardware which can run Vulkan, Direct3D 12, or Metal.

#### Overall comparison

| Feature                                          | Compatibility                                                                                            | Mobile                                                                                                 | Forward+                                                                                                  |
| ------------------------------------------------ | -------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------- |
| Required hardware                                | Older or low-end.                                                                                        | Newer or high-end. Requires Vulkan, Direct3D 12, or Metal support.                                     | Newer or high-end. Requires Vulkan, Direct3D 12, or Metal support.                                        |
| Runs on new hardware                             | ✔️ Yes.                                                                                                  | ✔️ Yes.                                                                                                | ✔️ Yes.                                                                                                   |
| Runs on old and low-end hardware                 | ✔️ Yes.                                                                                                  | ✔️ Yes, but slower than Compatibility.                                                                 | ✔️ Yes, but slowest of all renderers.                                                                     |
| Runs on hardware without RenderingDevice support | ✔️ Yes.                                                                                                  | ❌ No.                                                                                                 | ❌ No.                                                                                                    |
| Target platforms                                 | Mobile, low-end desktop, web.                                                                            | Mobile, desktop.                                                                                       | Desktop.                                                                                                  |
| Desktop                                          | ✔️ Yes.                                                                                                  | ✔️ Yes.                                                                                                | ✔️ Yes.                                                                                                   |
| Mobile                                           | ✔️ Yes (low-end).                                                                                        | ✔️ Yes (high-end).                                                                                     | ⚠️ Supported, but poorly optimized. Use Mobile or Compatibility instead.                                  |
| XR                                               | ✔️ Yes. Recommended for standalone headsets.                                                             | ✔️ Yes. Recommended for desktop headsets.                                                              | ⚠️ Supported, but poorly optimized. Use Mobile or Compatibility instead.                                  |
| Web                                              | ✔️ Yes.                                                                                                  | ❌ No.                                                                                                 | ❌ No.                                                                                                    |
| 2D Games                                         | ✔️ Yes.                                                                                                  | ✔️ Yes, but Compatibility is usually good enough for 2D.                                               | ✔️ Yes, but Compatibility is usually good enough for 2D.                                                  |
| 3D Games                                         | ✔️ Yes.                                                                                                  | ✔️ Yes.                                                                                                | ✔️ Yes.                                                                                                   |
| Feature set                                      | 2D and core 3D features.                                                                                 | Most rendering features.                                                                               | All rendering features.                                                                                   |
| 2D rendering features                            | ✔️ Yes.                                                                                                  | ✔️ Yes.                                                                                                | ✔️ Yes.                                                                                                   |
| Core 3D rendering features                       | ✔️ Yes.                                                                                                  | ✔️ Yes.                                                                                                | ✔️ Yes.                                                                                                   |
| Advanced rendering features                      | ❌ No.                                                                                                   | ⚠️ Yes, limited by mobile hardware.                                                                    | ✔️ Yes. All rendering features are supported.                                                             |
| New features                                     | ⚠️ Some new rendering features are added to Compatibility. Features are added after Mobile and Forward+. | ✔️ Most new rendering features are added to Mobile. Mobile usually gets new features as Forward+ does. | ✔️ All new features are added to Forward+. As the focus of new development, Forward+ gets features first. |
| Rendering cost                                   | Low base cost, but high scaling cost.                                                                    | Medium base cost, and medium scaling cost.                                                             | Highest base cost, and low scaling cost.                                                                  |
| Rendering driver                                 | OpenGL.                                                                                                  | Vulkan, Direct3D 12, or Metal.                                                                         | Vulkan, Direct3D 12, or Metal.                                                                            |

#### Lights and shadows

See [3D lights and shadows](tutorials_3d.md) for more information.

| Feature                          | Compatibility                 | Mobile                    | Forward+                           |
| -------------------------------- | ----------------------------- | ------------------------- | ---------------------------------- |
| Lighting approach                | Forward                       | Forward                   | Clustered Forward                  |
| Maximum OmniLights               | 8 per mesh. Can be increased. | 8 per mesh, 256 per view. | 512 per cluster. Can be increased. |
| Maximum SpotLights               | 8 per mesh. Can be increased. | 8 per mesh, 256 per view. | 512 per cluster. Can be increased. |
| Maximum DirectionalLights        | 8                             | 8                         | 8                                  |
| PCSS for OmniLight and SpotLight | ❌ Not supported.             | ✔️ Supported.             | ✔️ Supported.                      |
| PCSS for DirectionalLight        | ❌ Not supported.             | ❌ Not supported.         | ✔️ Supported.                      |
| Light projector textures         | ❌ Not supported.             | ✔️ Supported.             | ✔️ Supported.                      |

#### Global Illumination

See [Introduction to global illumination](tutorials_3d.md) for more information.

| Feature                                           | Compatibility                                                                                        | Mobile                    | Forward+                 |
| ------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ------------------------- | ------------------------ |
| ReflectionProbe                                   | ✔️ Supported, 2 per mesh.                                                                            | ✔️ Supported, 8 per mesh. | ✔️ Supported, unlimited. |
| LightmapGI                                        | ⚠️ Rendering of baked lightmaps is supported. Baking requires hardware with RenderingDevice support. | ✔️ Supported.             | ✔️ Supported.            |
| VoxelGI                                           | ❌ Not supported.                                                                                    | ❌ Not supported.         | ✔️ Supported.            |
| Screen-Space Indirect Lighting (SSIL)             | ❌ Not supported.                                                                                    | ❌ Not supported.         | ✔️ Supported.            |
| Signed Distance Field Global Illumination (SDFGI) | ❌ Not supported.                                                                                    | ❌ Not supported.         | ✔️ Supported.            |

#### Environment and post-processing

See [Environment and post-processing](tutorials_3d.md) for more information.

| Feature                                           | Compatibility     | Mobile            | Forward+      |
| ------------------------------------------------- | ----------------- | ----------------- | ------------- |
| Fog (Depth and Height)                            | ✔️ Supported.     | ✔️ Supported.     | ✔️ Supported. |
| Volumetric Fog                                    | ❌ Not supported. | ❌ Not supported. | ✔️ Supported. |
| Tonemapping                                       | ✔️ Supported.     | ✔️ Supported.     | ✔️ Supported. |
| Screen-Space Reflections                          | ❌ Not supported. | ❌ Not supported. | ✔️ Supported. |
| Screen-Space Ambient Occlusion (SSAO)             | ✔️ Supported.     | ❌ Not supported. | ✔️ Supported. |
| Screen-Space Indirect Lighting (SSIL)             | ❌ Not supported. | ❌ Not supported. | ✔️ Supported. |
| Signed Distance Field Global Illumination (SDFGI) | ❌ Not supported. | ❌ Not supported. | ✔️ Supported. |
| Glow                                              | ✔️ Supported.     | ✔️ Supported.     | ✔️ Supported. |
| Adjustments                                       | ✔️ Supported.     | ✔️ Supported.     | ✔️ Supported. |
| Custom post-processing with fullscreen quad       | ✔️ Supported.     | ✔️ Supported.     | ✔️ Supported. |
| Custom post-processing with CompositorEffects     | ❌ Not supported. | ✔️ Supported.     | ✔️ Supported. |

#### Antialiasing

See [3D antialiasing](tutorials_3d.md) for more information.

| Feature                        | Compatibility     | Mobile            | Forward+      |
| ------------------------------ | ----------------- | ----------------- | ------------- |
| MSAA 3D                        | ✔️ Supported.     | ✔️ Supported.     | ✔️ Supported. |
| MSAA 2D                        | ❌ Not supported. | ✔️ Supported.     | ✔️ Supported. |
| TAA                            | ❌ Not supported. | ❌ Not supported. | ✔️ Supported. |
| FSR2                           | ❌ Not supported. | ❌ Not supported. | ✔️ Supported. |
| FXAA                           | ❌ Not supported. | ✔️ Supported.     | ✔️ Supported. |
| SSAA                           | ✔️ Supported.     | ✔️ Supported.     | ✔️ Supported. |
| Screen-space roughness limiter | ❌ Not supported. | ✔️ Supported.     | ✔️ Supported. |

#### StandardMaterial features

See [Standard Material 3D and ORM Material 3D](tutorials_3d.md) for more information.

| Feature                | Compatibility     | Mobile            | Forward+      |
| ---------------------- | ----------------- | ----------------- | ------------- |
| Sub-surface scattering | ❌ Not supported. | ❌ Not supported. | ✔️ Supported. |

#### Shader features

See [Shading reference](tutorials_shaders.md) for more information.

| Feature                 | Compatibility     | Mobile                                                               | Forward+      |
| ----------------------- | ----------------- | -------------------------------------------------------------------- | ------------- |
| Screen texture          | ✔️ Supported.     | ✔️ Supported.                                                        | ✔️ Supported. |
| Depth texture           | ✔️ Supported.     | ✔️ Supported.                                                        | ✔️ Supported. |
| Normal/Roughness buffer | ❌ Not supported. | ❌ Not supported.                                                    | ✔️ Supported. |
| Compute shaders         | ❌ Not supported. | ⚠️ Supported, but comes with a performance penalty on older devices. | ✔️ Supported. |

#### Other features

| Feature                          | Compatibility     | Mobile        | Forward+      |
| -------------------------------- | ----------------- | ------------- | ------------- |
| Variable rate shading            | ❌ Not supported. | ✔️ Supported. | ✔️ Supported. |
| Decals                           | ❌ Not supported. | ✔️ Supported. | ✔️ Supported. |
| Particle trails                  | ❌ Not supported. | ✔️ Supported. | ✔️ Supported. |
| Particle SDF collision           | ❌ Not supported. | ✔️ Supported. | ✔️ Supported. |
| Depth of field blur              | ❌ Not supported. | ✔️ Supported. | ✔️ Supported. |
| Adaptive and Mailbox VSync modes | ❌ Not supported. | ✔️ Supported. | ✔️ Supported. |
| 2D HDR Viewport                  | ❌ Not supported. | ✔️ Supported. | ✔️ Supported. |
| RenderingDevice access           | ❌ Not supported. | ✔️ Supported. | ✔️ Supported. |

---

## Using Viewports

### Introduction

Think of a [Viewport](../godot_csharp_rendering.md) as a screen onto which the game is projected. In order to see the game, we need to have a surface on which to draw it. That surface is the Root Viewport.

[SubViewports](../godot_csharp_rendering.md) are a kind of Viewport that can be added to the scene so that there are multiple surfaces to draw on. When we are drawing to a SubViewport, we call it a render target. We can access the contents of a render target by accessing its corresponding [texture](../godot_csharp_misc.md). By using a SubViewport as render target, we can either render multiple scenes simultaneously or we can render to a [ViewportTexture](../godot_csharp_rendering.md) which is applied to an object in the scene, for example a dynamic skybox.

[SubViewports](../godot_csharp_rendering.md) have a variety of use cases, including:

- Rendering 3D objects within a 2D game
- Rendering 2D elements in a 3D game
- Rendering dynamic textures
- Generating procedural textures at runtime
- Rendering multiple cameras in the same scene

What all these use cases have in common is that you are given the ability to draw objects to a texture as if it were another screen and can then choose what to do with the resulting texture.

Another kind of Viewports in Godot are [Windows](../godot_csharp_ui_controls.md). They allow their content to be projected onto a window. While the Root Viewport is a Window, they are less flexible. If you want to use the texture of a Viewport, you'll be working with [SubViewports](../godot_csharp_rendering.md) most of the time.

### Input

[Viewports](../godot_csharp_rendering.md) are also responsible for delivering properly adjusted and scaled input events to their children nodes. By default [SubViewports](../godot_csharp_rendering.md) don't automatically receive input, unless they receive it from their direct [SubViewportContainer](../godot_csharp_ui_controls.md) parent node. In this case, input can be disabled with the [Disable Input](../godot_csharp_misc.md) property.

For more information on how Godot handles input, please read the [Input Event Tutorial](tutorials_inputs.md).

### Listener

Godot supports 3D sound (in both 2D and 3D nodes). More on this can be found in the [Audio Streams Tutorial](tutorials_audio.md). For this type of sound to be audible, the [Viewport](../godot_csharp_rendering.md) needs to be enabled as a listener (for 2D or 3D). If you are using a [SubViewport](../godot_csharp_rendering.md) to display your [World3D](../godot_csharp_misc.md) or [World2D](../godot_csharp_misc.md), don't forget to enable this!

### Cameras (2D & 3D)

When using a [Camera3D](../godot_csharp_nodes_3d.md) or [Camera2D](../godot_csharp_nodes_2d.md), it will always display on the closest parent [Viewport](../godot_csharp_rendering.md) (going towards the root). For example, in the following hierarchy:

`CameraA` will display on the Root [Viewport](../godot_csharp_rendering.md) and it will draw `MeshA`. `CameraB` will be captured by the [SubViewport](../godot_csharp_rendering.md) along with `MeshB`. Even though `MeshB` is in the scene hierarchy, it will still not be drawn to the Root Viewport. Similarly, `MeshA` will not be visible from the SubViewport because SubViewports only capture nodes below them in the hierarchy.

There can only be one active camera per [Viewport](../godot_csharp_rendering.md), so if there is more than one, make sure that the desired one has the [current](../godot_csharp_misc.md) property set, or make it the current camera by calling:

```csharp
camera.MakeCurrent();
```

By default, cameras will render all objects in their world. In 3D, cameras can use their [cull_mask](../godot_csharp_misc.md) property combined with the [VisualInstance3D's](../godot_csharp_nodes_3d.md) [layer](../godot_csharp_misc.md) property to restrict which objects are rendered.

### Scale & stretching

[SubViewports](../godot_csharp_rendering.md) have a [size](../godot_csharp_misc.md) property, which represents the size of the SubViewport in pixels. For SubViewports which are children of [SubViewportContainers](../godot_csharp_ui_controls.md), these values are overridden, but for all others, this sets their resolution.

It is also possible to scale the 2D content and make the [SubViewport](../godot_csharp_rendering.md) resolution different from the one specified in size, by calling:

```csharp
subViewport.Size2DOverride = new Vector2I(width, height); // Custom size for 2D.
subViewport.Size2DOverrideStretch = true; // Enable stretch for custom size.
```

For information on scaling and stretching with the Root Viewport visit the Multiple Resolutions Tutorial

### Worlds

For 3D, a [Viewport](../godot_csharp_rendering.md) will contain a [World3D](../godot_csharp_misc.md). This is basically the universe that links physics and rendering together. Node3D-based nodes will register using the World3D of the closest Viewport. By default, newly created Viewports do not contain a World3D but use the same as their parent Viewport. The Root Viewport always contains a World3D, which is the one objects are rendered to by default.

A [World3D](../godot_csharp_misc.md) can be set in a [Viewport](../godot_csharp_rendering.md) using the [World 3D](../godot_csharp_misc.md) property, that will separate all children nodes of this [Viewport](../godot_csharp_rendering.md) and will prevent them from interacting with the parent Viewport's World3D. This is especially useful in scenarios where, for example, you might want to show a separate character in 3D imposed over the game (like in StarCraft).

As a helper for situations where you want to create [Viewports](../godot_csharp_rendering.md) that display single objects and don't want to create a [World3D](../godot_csharp_misc.md), Viewport has the option to use its [Own World3D](../godot_csharp_misc.md). This is useful when you want to instance 3D characters or objects in [World2D](../godot_csharp_misc.md).

For 2D, each [Viewport](../godot_csharp_rendering.md) always contains its own [World2D](../godot_csharp_misc.md). This suffices in most cases, but in case sharing them may be desired, it is possible to do so by setting [world_2d](../godot_csharp_misc.md) on the Viewport through code.

For an example of how this works, see the demo projects [3D in 2D](https://github.com/godotengine/godot-demo-projects/tree/master/viewport/3d_in_2d) and [2D in 3D](https://github.com/godotengine/godot-demo-projects/tree/master/viewport/2d_in_3d) respectively.

### Capture

It is possible to query a capture of the [Viewport](../godot_csharp_rendering.md) contents. For the Root Viewport, this is effectively a screen capture. This is done with the following code:

```csharp
// Retrieve the captured Image using get_image().
var img = GetViewport().GetTexture().GetImage();
// Convert Image to ImageTexture.
var tex = ImageTexture.CreateFromImage(img);
// Set sprite texture.
sprite.Texture = tex;
```

But if you use this in `_ready()` or from the first frame of the [Viewport's](../godot_csharp_rendering.md) initialization, you will get an empty texture because there is nothing to get as texture. You can deal with it using (for example):

```csharp
// Wait until the frame has finished before getting the texture.
await ToSignal(RenderingServer.Singleton, RenderingServer.SignalName.FramePostDraw);
// You can get the image after this.
```

### Viewport Container

If the [SubViewport](../godot_csharp_rendering.md) is a child of a [SubViewportContainer](../godot_csharp_ui_controls.md), it will become active and display anything it has inside. The layout looks like this:

The [SubViewport](../godot_csharp_rendering.md) will cover the area of its parent [SubViewportContainer](../godot_csharp_ui_controls.md) completely if [Stretch](../godot_csharp_misc.md) is set to `true` in the SubViewportContainer.

> **Note:** The size of the [SubViewportContainer](../godot_csharp_ui_controls.md) cannot be smaller than the size of the [SubViewport](../godot_csharp_rendering.md).

### Rendering

Due to the fact that the [Viewport](../godot_csharp_rendering.md) is an entryway into another rendering surface, it exposes a few rendering properties that can be different from the project settings. You can choose to use a different level of [MSAA](../godot_csharp_misc.md) for each Viewport. The default behavior is `Disabled`.

If you know that the [Viewport](../godot_csharp_rendering.md) is only going to be used for 2D, you can [Disable 3D](../godot_csharp_misc.md). Godot will then restrict how the Viewport is drawn. Disabling 3D is slightly faster and uses less memory compared to enabled 3D. It's a good idea to disable 3D if your viewport doesn't render anything in 3D.

> **Note:** If you need to render 3D shadows in the viewport, make sure to set the viewport's [positional_shadow_atlas_size](../godot_csharp_misc.md) property to a value higher than `0`. Otherwise, shadows won't be rendered. By default, the equivalent project setting is set to `4096` on desktop platforms and `2048` on mobile platforms.

Godot also provides a way of customizing how everything is drawn inside [Viewports](../godot_csharp_rendering.md) using [Debug Draw](../godot_csharp_misc.md). Debug Draw allows you to specify a mode which determines how the Viewport will display things drawn inside it. Debug Draw is `Disabled` by default. Some other options are `Unshaded`, `Overdraw`, and `Wireframe`. For a full list, refer to the [Viewport Documentation](../godot_csharp_rendering.md).

- **Debug Draw = Disabled** (default): The scene is drawn normally.

- **Debug Draw = Unshaded**: Unshaded draws the scene without using lighting information so all the objects appear flatly colored in their albedo color.

- **Debug Draw = Overdraw**: Overdraw draws the meshes semi-transparent with an additive blend so you can see how the meshes overlap.

- **Debug Draw = Wireframe**: Wireframe draws the scene using only the edges of triangles in the meshes.

> **Note:** Debug Draw modes are currently **not** supported when using the Compatibility rendering method. They will appear as regular draw modes.

### Render target

When rendering to a [SubViewport](../godot_csharp_rendering.md), whatever is inside will not be visible in the scene editor. To display the contents, you have to draw the SubViewport's [ViewportTexture](../godot_csharp_rendering.md) somewhere. This can be requested via code using (for example):

```csharp
// This gives us the ViewportTexture.
var tex = viewport.GetTexture();
sprite.Texture = tex;
```

Or it can be assigned in the editor by selecting "New ViewportTexture"

and then selecting the [Viewport](../godot_csharp_rendering.md) you want to use.

Every frame, the [Viewport's](../godot_csharp_rendering.md) texture is cleared away with the default clear color (or a transparent color if [Transparent BG](../godot_csharp_misc.md) is set to `true`). This can be changed by setting [Clear Mode](../godot_csharp_misc.md) to `Never` or `Next Frame`. As the name implies, Never means the texture will never be cleared, while next frame will clear the texture on the next frame and then set itself to Never.

By default, re-rendering of the [SubViewport](../godot_csharp_rendering.md) happens when its [ViewportTexture](../godot_csharp_rendering.md) has been drawn in a frame. If visible, it will be rendered, otherwise, it will not. This behavior can be changed by setting [Update Mode](../godot_csharp_misc.md) to `Never`, `Once`, `Always`, or `When Parent Visible`. Never and Always will never or always re-render respectively. Once will re-render the next frame and change to Never afterwards. This can be used to manually update the Viewport. This flexibility allows users to render an image once and then use the texture without incurring the cost of rendering every frame.

> **Note:** Make sure to check the Viewport demos. They are available in the viewport folder of the demos archive, or at [https://github.com/godotengine/godot-demo-projects/tree/master/viewport](https://github.com/godotengine/godot-demo-projects/tree/master/viewport).

---
