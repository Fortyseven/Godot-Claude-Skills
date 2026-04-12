# Godot 4 GDScript Tutorials — 3D (Part 4)

> 4 tutorials. GDScript-specific code examples.

## Signed distance field global illumination (SDFGI)

Signed distance field global illumination (SDFGI) is a novel technique available in Godot. It provides semi-real-time global illumination that scales to any world size and works with procedurally generated levels.

SDFGI supports dynamic lights, but _not_ dynamic occluders or dynamic emissive surfaces. Therefore, SDFGI provides better real-time ability than baked lightmaps, but worse real-time ability than VoxelGI.

From a performance standpoint, SDFGI is one of the most demanding global illumination techniques in Godot. Like with VoxelGI, there are still many settings available to tweak its performance requirements at the cost of quality.

> **Important:** SDFGI is only supported when using the Forward+ renderer, not the Mobile or Compatibility renderers.

> **See also:** Not sure if SDFGI is suited to your needs? See Which global illumination technique should I use? for a comparison of GI techniques available in Godot 4.

### Visual comparison

### Setting up SDFGI

In Godot, SDFGI is the global illumination technique with the fewest required steps to enable:

1. Make sure your MeshInstance nodes have their **Global Illumination > Mode** property set to **Static** in the inspector.

- For imported 3D scenes, the bake mode can be configured in the Import dock after selecting the 3D scene file in the FileSystem dock.

1. Add a WorldEnvironment node and create an Environment resource for it.
2. Edit the Environment resource, scroll down to the **SDFGI** section and unfold it.
3. Enable **SDFGI > Enabled**. SDFGI will automatically follow the camera when it moves, so you do not need to configure extents (unlike VoxelGI).

### Environment SDFGI properties

In the Environment resource, there are several properties available to adjust SDFGI appearance and quality:

- **Use Occlusion:** If enabled, SDFGI will throw additional rays to find and reduce light leaks. This has a performance cost, so only enable this property if you actually need it.
- **Read Sky Light:** If enabled, the environment lighting is represented in the global illumination. This should be enabled in outdoor scenes and disabled in fully indoor scenes.
- **Bounce Feedback:** By default, indirect lighting only bounces once when using SDFGI. Setting this value above `0.0` will cause SDFGI to bounce more than once, which provides more realistic indirect lighting at a small performance cost. Sensible values are usually between `0.3` and `1.0` depending on the scene. Note that in some scenes, values above `0.5` can cause infinite feedback loops to happen, causing the scene to become extremely bright in a few seconds' time. If your indirect lighting looks "splotchy", consider increasing this value above `0.0` to get more uniform-looking lighting. If your lighting ends up looking too bright as a result, decrease **Energy** to compensate.
- **Cascades:** Higher values result in more detailed GI information (and/or greater maximum distance), but are significantly more expensive on the CPU and GPU. The performance cost of having more cascades especially increases when the camera moves fast, so consider decreasing this to `4` or lower if your camera moves fast.
- **Min Cell Size:** The minimum SDFGI cell size to use for the nearest, most detailed cascade. Lower values result in more accurate indirect lighting and reflection at the cost of lower performance. Adjusting this setting also affects **Cascade 0 Distance** and **Max Distance** automatically.
- **Cascade 0 Distance:** The distance at which the nearest, most detailed cascade ends. Greater values make the nearest cascade transition less noticeable, at the cost of reducing the level of detail in the nearest cascade. Adjusting this setting also affects **Min Cell Size** and **Max Distance** automatically.
- **Max Distance:** Controls how far away the signed distance field will be computed (for the least detailed cascade). SDFGI will not have any effect past this distance. This value should always be set below the Camera's Far value, as there is no benefit in computing SDFGI past the viewing distance. Adjusting this setting also affects **Min Cell Size** and **Cascade 0 Distance** automatically.
- **Y Scale:** Controls how far apart SDFGI probes are spread _vertically_. By default, vertical spread is the same as horizontal. However, since most game scenes aren't highly vertical, setting the Y Scale to `75%` or even `50%` can provide better quality and reduce light leaks without impacting performance.
- **Energy:** The brightness multiplier for SDFGI's indirect lighting.
- **Normal Bias:** The normal bias to use for SDFGI's probe ray bounces. Unlike **Probe Bias**, this only increases the value in relation to the mesh's normals. This makes the bias adjustment more nuanced and avoids increasing the bias too much for no reason. Increase this value if you notice striping artifacts in indirect lighting or reflections.
- **Probe Bias:** The bias to use for SDFGI's probe ray bounces. Increase this value if you notice striping artifacts in indirect lighting or reflections.

### SDFGI interaction with lights and objects

The amount of indirect energy emitted by a light is governed by its color, energy _and_ indirect energy properties. To make a specific light emit more or less indirect energy without affecting the amount of direct light emitted by the light, adjust the **Indirect Energy** property in the Light3D inspector.

To ensure correct visuals when using SDFGI, you must configure your meshes and lights' global illumination properties according to their _purpose_ in the scene (static or dynamic).

There are 3 global illumination modes available for meshes:

- **Disabled:** The mesh won't be taken into account in SDFGI generation. The mesh will receive indirect lighting from the scene, but it will not contribute indirect lighting to the scene.
- **Static (default):** The mesh will be taken into account in SDFGI generation. The mesh will both receive _and_ contribute indirect lighting to the scene. If the mesh is changed in any way after SDFGI is generated, the camera must move away from the object then move back close to it for SDFGI to regenerate. Alternatively, SDFGI can be toggled off and back on. If neither is done, indirect lighting will look incorrect.
- **Dynamic (not supported with SDFGI):** The mesh won't be taken into account in SDFGI generation. The mesh will receive indirect lighting from the scene, but it will not contribute indirect lighting to the scene. _This acts identical to the **Disabled** bake mode when using SDFGI._

Additionally, there are 3 bake modes available for lights (DirectionalLight3D, OmniLight3D and SpotLight3D):

- **Disabled:** The light won't be taken into account for SDFGI baking. The light won't contribute indirect lighting to the scene.
- **Static:** The light will be taken into account for SDFGI baking. The light will contribute indirect lighting to the scene. If the light is changed in any way after baking, indirect lighting will look incorrect until the camera moves away from the light and back (which causes SDFGI to be baked again). will look incorrect. If in doubt, use this mode for level lighting.
- **Dynamic (default):** The light won't be taken into account for SDFGI baking, but it will still contribute indirect lighting to the scene in real-time. This option is slower compared to **Static**. Only use the **Dynamic** global illumination mode on lights that will change significantly during gameplay.

> **Note:** The amount of indirect energy emitted by a light depends on its color, energy _and_ indirect energy properties. To make a specific light emit more or less indirect energy without affecting the amount of direct light emitted by the light, adjust the **Indirect Energy** property in the Light3D inspector.

> **See also:** See Which global illumination mode should I use on meshes and lights? for general usage recommendations.

### Adjusting SDFGI performance and quality

Since SDFGI is relatively demanding, it will perform best on systems with recent dedicated GPUs. On older dedicated GPUs and integrated graphics, tweaking the settings is necessary to achieve reasonable performance.

In the Project Settings' **Rendering > Global Illumination** section, SDFGI quality can also be adjusted in several ways:

- **Sdfgi > Probe Ray Count:** Higher values result in better quality, at the cost of higher GPU usage. If this value is set too low, this can cause surfaces to have visible "splotches" of indirect lighting on them due to the number of rays thrown being very low.
- **Sdfgi > Frames To Converge:** Higher values result in better quality, but GI will take more time to fully converge. The effect of this setting is especially noticeable when first loading a scene, or when lights with a bake mode other than **Disabled** are moving fast. If this value is set too low, this can cause surfaces to have visible "splotches" of indirect lighting on them due to the number of rays thrown being very low. If your scene's lighting doesn't have fast-moving lights that contribute to GI, consider setting this to `30` to improve quality without impacting performance.
- **Sdfgi > Frames To Update Light:** Lower values result in moving lights being reflected faster, at the cost of higher GPU usage. If your scene's lighting doesn't have fast-moving lights that contribute to GI, consider setting this to `16` to improve performance.
- **Gi > Use Half Resolution:** If enabled, both SDFGI and VoxelGI will have their GI buffer rendering at halved resolution. For instance, when rendering in 3840×2160, the GI buffer will be computed at a 1920×1080 resolution. Enabling this option saves a lot of GPU time, but it can introduce visible aliasing around thin details.

SDFGI rendering performance also depends on the number of cascades and the cell size chosen in the Environment resource (see above).

### SDFGI caveats

SDFGI has some downsides due to its cascaded nature. When the camera moves, cascade shifts may be visible in indirect lighting. This can be alleviated by adjusting the cascade size, but also by adding fog (which will make distant cascade shifts less noticeable).

Additionally, performance will suffer if the camera moves too fast. This can be fixed in two ways:

- Ensuring the camera doesn't move too fast in any given situation.
- Temporarily disabling SDFGI in the Environment resource if the camera needs to be moved at a high speed, then enabling SDFGI once the camera speed slows down.

When SDFGI is enabled, it will also take some time for global illumination to be fully converged (25 frames by default). This can create a noticeable transition effect while GI is still converging. To hide this, you can use a ColorRect node that spans the whole viewport and fade it out when switching scenes using an AnimationPlayer node.

The signed distance field is only updated when the camera moves in and out of a cascade. This means that if geometry is modified in the distance, the global illumination appearance will be correct once the camera gets closer. However, if a nearby object with a bake mode set to **Static** or **Dynamic** is moved (such as a door), the global illumination will appear incorrect until the camera moves away from the object.

SDFGI's sharp reflections are only visible on opaque materials. Transparent materials will only use rough reflections, even if the material's roughness is lower than 0.2.

---

## Using Voxel global illumination

VoxelGI is a form of fully real-time global illumination, intended to be used for small/medium-scale 3D scenes. VoxelGI is fairly demanding on the GPU, so it's best used when targeting dedicated graphics cards.

> **Important:** VoxelGI is only supported when using the Forward+ renderer, not the Mobile or Compatibility renderers.

> **See also:** Not sure if VoxelGI is suited to your needs? See Which global illumination technique should I use? for a comparison of GI techniques available in Godot 4.

### Visual comparison

### Setting up VoxelGI

1. Make sure your static level geometry is imported with the Light Baking option set to **Static** or **Static Lightmaps** in the Import dock. For manually added MeshInstance3D nodes, make sure the **Global Illumination > Mode** property is set to **Static** in the inspector.
2. Create a VoxelGI node in the Scene tree dock.
3. Move the VoxelGI node to the center of the area you want it to cover by dragging the manipulation gizmo in the 3D viewport. Then adjust the VoxelGI's extents by dragging the red points in the 3D viewport (or enter values in the inspector). Make sure the VoxelGI's extents aren't unnecessarily large, or quality will suffer.
4. Select the VoxelGI node and click **Bake** at the top of the 3D editor viewport. This will take at least a few seconds to complete (depending on the number of VoxelGI subdivisions and scene complexity).

If at least one mesh contained within the VoxelGI's extents has its global illumination mode set to **Static**, you should see indirect lighting appear within the scene.

> **Note:** To avoid bloating text-based scene files with large amounts of binary data, make sure the VoxelGIData resource is _always_ saved to an external binary file. This file must be saved with a `.res` (binary resource) extension instead of `.tres` (text-based resource). Using an external binary resource for VoxelGIData will keep your text-based scene small while ensuring it loads and saves quickly.

### VoxelGI node properties

The following properties can be adjusted in the VoxelGI node inspector before baking:

- **Subdiv:** Higher values result in more precise indirect lighting, at the cost of lower performance, longer bake times and increased storage requirements.
- **Extents:** Represents the size of the box in which indirect lighting should be baked. Extents are centered around the VoxelGI node's origin.

The following properties can be adjusted in the VoxelGIData _resource_ that is contained within a VoxelGI node after it has been baked:

- **Dynamic Range:** The maximum brightness that can be represented in indirect lighting. Higher values make it possible to represent brighter indirect light, at the cost of lower precision (which can result in visible banding). If in doubt, leave this unchanged.
- **Energy:** The indirect lighting's overall energy. This also effects the energy of direct lighting emitted by meshes with emissive materials.
- **Bias:** Optional bias added to lookups into the voxel buffer at runtime. This helps avoid self-occlusion artifacts.
- **Normal Bias:** Similar to **Bias**, but offsets the lookup into the voxel buffer by the surface normal. This also helps avoid self-occlusion artifacts. Higher values reduce self-reflections visible in non-rough materials, at the cost of more visible light leaking and flatter-looking indirect lighting. To prioritize hiding self-reflections over lighting quality, set **Bias** to `0.0` and **Normal Bias** to a value between `1.0` and `2.0`.
- **Propagation:** The energy factor to use for bounced indirect lighting. Higher values will result in brighter, more diffuse lighting (which may end up looking too flat). When **Use Two Bounces** is enabled, you may want to decrease **Propagation** to compensate for the overall brighter indirect lighting.
- **Use Two Bounces:** If enabled, lighting will bounce twice instead of just once. This results in more realistic-looking indirect lighting, and makes indirect lighting visible in reflections as well. Enabling this generally has no noticeable performance cost.
- **Interior:** If enabled, environment sky lighting will not be taken into account by VoxelGI. This should be enabled in indoor scenes to avoid light leaking from the environment.

### VoxelGI interaction with lights and objects

To ensure correct visuals when using VoxelGI, you must configure your meshes and lights' global illumination properties according to their _purpose_ in the scene (static or dynamic).

There are 3 global illumination modes available for meshes:

- **Disabled:** The mesh won't be taken into account for VoxelGI baking. The mesh will _receive_ indirect lighting from the scene, but it will not _contribute_ indirect lighting to the scene.
- **Static (default):** The mesh will be taken into account for VoxelGI baking. The mesh will both receive _and_ contribute indirect lighting to the scene. If the mesh is changed in any way after baking, the VoxelGI node must be baked again. Otherwise, indirect lighting will look incorrect.
- **Dynamic:** The mesh won't be taken into account for VoxelGI baking, but it will still receive _and_ contribute indirect lighting to the scene in real-time. This option is much slower compared to **Static**. Only use the **Dynamic** global illumination mode on large meshes that will change significantly during gameplay.

> **Note:** For meshes with the **Static** bake mode, the VoxelGI baking system is not able to make use of custom shaders ([ShaderMaterial](../godot_gdscript_rendering.md)). These meshes will be considered to be pure black, only acting as light blockers. You can make VoxelGI take custom shaders into account by using the **Dynamic** bake mode for these objects, but this has a performance cost. For [BaseMaterial3D](../godot_gdscript_rendering.md), some properties are currently ignored during baking. This can impact visuals if the material's albedo or emission texture was designed around using certain UV mappings: - **UV1 > Offset**

- **UV1 > Scale**
- **UV1 > Triplanar**
- **Emission > On UV2**

Additionally, there are 3 bake modes available for lights (DirectionalLight3D, OmniLight3D and SpotLight3D):

- **Disabled:** The light won't be taken into account for VoxelGI baking. The light won't contribute indirect lighting to the scene.
- **Static:** The light will be taken into account for VoxelGI baking. The light will contribute indirect lighting to the scene. If the light is changed in any way after baking, the VoxelGI node must be baked again or indirect lighting will look incorrect. If in doubt, use this mode for level lighting.
- **Dynamic (default):** The light won't be taken into account for VoxelGI baking, but it will still contribute indirect lighting to the scene in real-time. This option is slower compared to **Static**. Only use the **Dynamic** global illumination mode on lights that will change significantly during gameplay.

> **Note:** The amount of indirect energy emitted by a light depends on its color, energy _and_ indirect energy properties. To make a specific light emit more or less indirect energy without affecting the amount of direct light emitted by the light, adjust the **Indirect Energy** property in the Light3D inspector.

> **See also:** See Which global illumination mode should I use on meshes and lights? for general usage recommendations.

### Adjusting VoxelGI performance and quality

Since VoxelGI is relatively demanding, it will perform best on systems with recent dedicated GPUs. On older dedicated GPUs and integrated graphics, tweaking the settings is necessary to achieve reasonable performance.

In the Project Settings' **Rendering > Global Illumination** section, VoxelGI quality can also be adjusted in two ways:

- **Voxel Gi > Quality:** If set to **Low** instead of **High**, voxel cone tracing will only use 4 taps instead of 6. This speeds up rendering at the cost of less pronounced ambient occlusion.
- **Gi > Use Half Resolution:** If enabled, both VoxelGI and SDFGI will have their GI buffer rendering at halved resolution. For instance, when rendering in 3840×2160, the GI buffer will be computed at a 1920×1080 resolution. Enabling this option saves a lot of GPU time, but it can introduce visible aliasing around thin details.

Note that the **Advanced** toggle must be enabled in the project settings dialog for the above settings to be visible.

Additionally, VoxelGI can be disabled entirely by hiding the VoxelGI node. This can be used for comparison purposes or to improve performance on low-end systems.

### Reducing VoxelGI light leaks and artifacts

After baking VoxelGI, you may notice indirect light is leaking at some spots in your level geometry. This can be remedied in several ways:

- For both light leaking and artifacts, try moving or rotating the VoxelGI node then bake it again.
- To combat light leaking in general, ensure your level geometry is fully sealed. This is best done in the 3D modeling software used to design the level, but primitive MeshInstance3D nodes with their global illumination mode set to **Static** can also be used.
- To combat light leaking with thin geometry, it's recommended to make the geometry in question thicker. If this is not possible, then add a primitive MeshInstance3D node with its global illumination mode set to **Static**. Bake VoxelGI again, then hide the primitive MeshInstance3D node (it will still be taken into account by VoxelGI). For optimal results, the MeshInstance3D should have a material whose color matches the original thin geometry.
- To combat artifacts that can appear on reflective surfaces, try increasing **Bias** and/or **Normal Bias** in the VoxelGIData resource as described above. Do not increase these values too high, or light leaking will become more pronounced.

If you notice VoxelGI nodes popping in and out of existence as the camera moves, this is most likely because the engine is rendering too many VoxelGI instances at once. Godot is limited to rendering 8 VoxelGI nodes at once, which means up to 8 instances can be in the camera view before some of them will start flickering.

Additionally, for performance reasons, Godot can only blend between 2 VoxelGI nodes at a given pixel on the screen. If you have more than 2 VoxelGI nodes overlapping, global illumination may appear to flicker as the camera moves or rotates.

---

## High dynamic range lighting

> **Work in progress:** The content of this page was not yet updated for Godot `4.6` and may be **outdated**. If you know how to improve this page or you can confirm that it's up to date, feel free to [open a pull request](https://github.com/godotengine/godot-docs).

### Introduction

Normally, an artist does all the 3D modeling, then all the texturing, looks at their awesome looking model in the 3D modeling software and says "looks fantastic, ready for integration!" then goes into the game, lighting is setup and the game runs.

So at what point does all this "HDR" business come into play? To understand the answer, we need to look at how displays behave.

Your display outputs linear light ratios from some maximum to some minimum intensity. Modern game engines perform complex math on linear light values in their respective scenes. So what's the problem?

The display has a limited range of intensity, depending on the display type. The game engine renders to an unlimited range of intensity values, however. While "maximum intensity" means something to an sRGB display, it has no bearing in the game engine; there is only a potentially infinitely wide range of intensity values generated per frame of rendering.

This means that some transformation of the scene light intensity, also known as _scene-referred_ light ratios, need to be transformed and mapped to fit within the particular output range of the chosen display. This can be most easily understood if we consider virtually photographing our game engine scene through a virtual camera. Here, our virtual camera would apply a particular camera rendering transform to the scene data, and the output would be ready for display on a particular display type.

> **Note:** Godot does not support high dynamic range _output_ yet. It can only perform lighting in HDR and tonemap the result to a low dynamic range image. For advanced users, it is still possible to get a non-tonemapped image of the viewport with full HDR data, which can then be saved to an OpenEXR file.

### Computer displays

Almost all displays require a nonlinear encoding for the code values sent to them. The display in turn, using its unique transfer characteristic, "decodes" the code value into linear light ratios of output, and projects the ratios out of the uniquely colored lights at each reddish, greenish, and blueish emission site.

For a majority of computer displays, the specifications of the display are outlined in accordance with IEC 61966-2-1, also known as the 1996 sRGB specification. This specification outlines how an sRGB display is to behave, including the color of the lights in the LED pixels as well as the transfer characteristics of the input (OETF) and output (EOTF).

Not all displays use the same OETF and EOTF as a computer display. For example, television broadcast displays use the BT.1886 EOTF. However, Godot currently only supports sRGB displays.

The sRGB standard is based around the nonlinear relationship between the current to light output of common desktop computing CRT displays.

The mathematics of a scene-referred model require that we multiply the scene by different values to adjust the intensities and exposure to different light ranges. The transfer function of the display can't appropriately render the wider dynamic range of the game engine's scene output using the simple transfer function of the display. A more complex approach to encoding is required.

### Scene linear & asset pipelines

Working in scene-linear sRGB is more complex than pressing a single switch. First, imported image assets must be converted to linear light ratios on import. Even when linearized, those assets may not be perfectly well-suited for use as textures, depending on how they were generated.

There are two ways to do this:

#### sRGB transfer function to display linear ratios on image import

This is the easiest method of using sRGB assets, but it's not the most ideal. One issue with this is loss of quality. Using 8 bits per channel to represent linear light ratios is not sufficient to quantize the values correctly. These textures may also be compressed later, which can exacerbate the problem.

#### Hardware sRGB transfer function to display linear conversion

The GPU will do the conversion after reading the texel using floating-point. This works fine on PC and consoles, but most mobile devices don't support it, or they don't support it on compressed texture formats (iOS for example).

#### Scene linear to display-referred nonlinear

After all the rendering is done, the scene linear render requires transforming to a suitable output such as an sRGB display. To do this, enable sRGB conversion in the current [Environment](../godot_gdscript_rendering.md) (more on that below).

Keep in mind that the **sRGB -> Display Linear** and **Display Linear -> sRGB** conversions must always be **both** enabled. Failing to enable one of them will result in horrible visuals suitable only for avant-garde experimental indie games.

### Parameters of HDR

HDR settings can be found in the [Environment](../godot_gdscript_rendering.md) resource. Most of the time, these are found inside a [WorldEnvironment](../godot_gdscript_nodes_3d.md) node or set in a Camera node. For more information, see Environment and post-processing.

---

## Introduction to 3D

Creating a 3D game can be challenging. That extra Z coordinate makes many of the common techniques that helped to make 2D games simpler no longer work. To aid in this transition, it is worth mentioning that Godot uses similar APIs for 2D and 3D. Most nodes are the same and are present in both 2D and 3D versions. In fact, it is worth checking the 3D platformer tutorial, or the 3D kinematic character tutorials, which are almost identical to their 2D counterparts.

In 3D, math is a little more complex than in 2D. For an introduction to the relevant math written for game developers, not mathemeticians or engineers, check out [Vector math](tutorials_math.md) and Using 3D transforms.

### 3D workspace

Editing 3D scenes is done in the 3D workspace. This workspace can be selected manually, but it will be automatically selected when a Node3D node is selected.

Similar to 2D, the tabs below the workspace selector are used to change between currently opened scenes or create a new one using the plus (+) button. The left and right docks should be familiar from [editor introduction](tutorials_editor.md).

Below the scene selector, the main toolbar is visible, and beneath the main toolbar is the 3D viewport.

#### Main toolbar

Some buttons in the main toolbar are the same as those in the 2D workspace. A brief explanation is given with the shortcut if the mouse cursor is hovered over a button for one second. Some buttons may have additional functionality if another keypress is performed. A recap of main functionality of each button with its default shortcut is provided below from left to right:

- **Select Mode** (Q): Allows selection of nodes in the viewport. Left clicking on a node to select one. Left clicking and dragging a rectangle selects all nodes within the rectangle's boundaries, once released. Holding Shift while selecting adds more nodes to the selection. Clicking on a selected node while holding Shift deselects the node. In this mode, you can use the gizmos to perform movement or rotation.
- **Move Mode** (W): Enables move (or translate) mode for the selected nodes. See **Space and manipulation gizmos** for more details.
- **Rotate Mode** (E): Enables rotation mode for the selected nodes. See **Space and manipulation gizmos** for more details.
- **Scale Mode** (R): Enables scaling and displays scaling gizmos in different axes for the selected nodes. See **Space and manipulation gizmos** for more details.
- **Show the list of selectable nodes at the clicked position**: As the description suggests, this provides a list of selectable nodes at the clicked position as a context menu, if there is more than one node in the clicked area.
- **Lock** (Ctrl + L) the selected nodes, preventing selection and movement in the viewport. Clicking the button again (or using Ctrl + Shift + L) unlocks the selected nodes. Locked nodes can only be selected in the scene tree. They can easily be identified with a padlock next to their node names in the scene tree. Clicking on this padlock also unlocks the nodes.
- **Group selected nodes** (Ctrl + G). This allows selection of the root node if any of the children are selected. Using Ctrl + G ungroups them. Additionally, clicking the ungroup button in the scene tree performs the same action.
- **Ruler Mode** (M): When enabled you can click and drag to measure distance in the scene in meters.
- **Use Local Space** (T): If enabled, gizmos of a node are drawn using the current node's rotation angle instead of the **global viewport axes**.
- **Use Snap** (Y): If enabled, movement, and rotation snap to grid. Snapping can also temporarily be activated using Ctrl while performing the action. The settings for changing snap options are explained below.
- **Toggle preview sunlight**: If no DirectionalLight3D exist in the scene, a preview of sunlight can be used as a light source. See **Preview environment and light** for more details.
- **Toggle preview environment**: If no WorldEnvironment exists in the scene, a preview of the environment can be used as a placeholder. See **Preview environment and light** for more details.
- **Edit Sun and Environment Settings (three dots)**: Opens the menu to configure preview sunlight and environment settings. See **Preview environment and light** for more details.
- **Transform menu**: It has three options:

- _Snap Object to Floor_: Snaps an object to a solid floor.
- _Transform Dialog_: Opens a dialog to adjust transform parameters (translate, rotate, scale, and transform) manually.
- _Snap Settings_: Allows you to change transform, rotate snap (in degrees), and scale snap (in percent) settings.
- **View menu**: Controls the view options and enables additional viewports:

In this menu, you can also show/hide grids, which are set to 1x1 meter by default, and the origin, where the blue, green, and red axis lines intersect. Moreover, specific types of gizmos can be toggled in this menu.

An open eye means that the gizmo is visible, a closed eye means it is hidden. A half-open eye means that it is also visible through opaque surfaces.

Clicking on _Settings_ in this view menu opens a window to change the _Vertical Field of View (VFOV)_ parameter (in degrees), _Z-Near_, and _Z-Far_ values.

Next to the View menu, additional buttons may be visible. In the toolbar image at the beginning of this chapter, an additional _Mesh_ button appears because a MeshInstance3D is selected. This menu provides some quick actions or tools to work on a specific node or selection.

#### View menu of viewport

Below the _Select_ tool, in the 3D viewport, clicking on the three dots opens the **View menu** for the viewport. Hiding all shown gizmos in the editor's 3D view can also be performed through this menu:

This menu also displays the current view type and enables quick adjustment of the viewport's viewing angle. Additionally, it offers options to modify the appearance of nodes within the viewport.

#### Coordinate system

Godot uses the [metric](https://en.wikipedia.org/wiki/Metric_system) system for everything in 3D, with 1 unit being equal to 1 meter. Physics and other areas are tuned for this scale. Therefore, attempting to use a different scale is usually a bad idea (unless you know what you are doing).

When working with 3D assets, it's always best to work in the correct scale (set the unit to metric in your 3D modeling software). Godot allows scaling post-import and, while this works in most cases, in rare situations it may introduce floating-point precision issues (and thus, glitches or artifacts) in delicate areas such as rendering or physics. Make sure your artists always work in the right scale!

The Y coordinate is used for "up". As for the horizontal X/Z axes, Godot uses a **right-handed** coordinate system. This means that for most objects that need alignment (such as lights or cameras), the Z axis is used as a "pointing towards" direction. This convention roughly means that:

- **X** is sides
- **Y** is up/down
- **Z** is front/back

See this chart for comparison with other 3D software:

#### Space and manipulation gizmos

Moving, rotating, and scaling objects in the 3D view is done through the manipulator gizmos. Each axis is represented by a color: Red, Green, Blue represent X, Y, Z respectively. This convention applies to the grid and other gizmos too (and also to the shader language, ordering of components for Vector3, Color, etc.).

Some useful keybindings:

- To snap placement or rotation, press Ctrl while moving, scaling, or rotating.
- To center the view on the selected object, press F.

In the viewport, the arrows can be clicked and held to move the object on an axis. The arcs can be clicked and held to rotate the object. To lock one axis and move the object freely in the other two axes, the colored rectangles can be clicked, held, and dragged.

If the transform mode is changed from _Select Mode_ to _Scale Mode_, the arrows will be replaced by cubes, which can be dragged to scale an object as if the object is being moved.

#### Navigating the 3D environment

In 3D environments, it is often important to adjust the viewpoint or angle from which you are viewing the scene. In Godot, navigating the 3D environment in the viewport (or spatial editor) can be done in multiple ways.

The default 3D scene navigation controls are similar to Blender (aiming to have some sort of consistency in the free software pipeline), but options are included to customize mouse buttons and behavior to be similar to other tools in the Editor Settings. To change the controls to Maya or Modo controls, you can navigate to **Editor Settings > Editors > 3D**. Then, under _Navigation_, search for _Navigation Scheme_.

Using the default settings, the following shortcuts control how one can navigate in the viewport:

Pressing the middle mouse button and dragging the mouse allows you to orbit around the center of what is on the screen.

It is also possible to left-click and hold the manipulator gizmo located on the top right of the viewport to orbit around the center:

Left-clicking on one of the colored circles will set the view to the chosen orthogonal and the viewport's view menu will be updated accordingly.

If the _Perspective_ view is enabled on the viewport (can be seen on the viewport's View menu, not the View menu on the main toolbar), holding down the right mouse button on the viewport or pressing Shift + F switches to "free-look" mode. In this mode you can move the mouse to look around, use the W A S D keys to fly around the view, E to go up, and Q to go down. To disable this mode, release the right mouse button or press Shift + F again.

In the free-look mode, you can temporarily increase the flying speed using Shift or decrease it using Alt. To change and keep the speed modifier use mouse wheel up or mouse wheel down, to increase or decrease it, respectively.

In orthogonal mode, holding the right mouse button will pan the view instead. Use Keypad 5 to toggle between perspective and orthogonal view.

#### Using Blender-style transform shortcuts

Since Godot 4.2, you can enable Blender-style shortcuts for translating, rotating and scaling nodes. In Blender, these shortcuts are:

- G for translating
- R for rotating
- S for scaling

After pressing a shortcut key while focusing on the 3D editor viewport, move the mouse or enter a number to move the selected node(s) by the specified amount in 3D units. You can constrain movement to a specific axis by specifying the axis as a letter, then the distance (if entering a value with the keyboard).

For instance, to move the selection upwards by 2.5 units, enter the following sequence in order (Y+ is upwards in Godot):

G-Y-2-.-5-Enter

To use Blender-style transform shortcuts in Godot, go to the Editor Settings' **Shortcuts** tab, then in the Spatial Editor section:

- Bind **Begin Translate Transformation** to G.
- Bind **Begin Rotate Transformation** to R.
- Bind **Begin Scale Transformation** to S.
- Finally, unbind **Scale Mode** so that its shortcut won't conflict with **Begin Rotate Transformation**.

> **Tip:** More shortcuts can be found on the [3D / Spatial editor](tutorials_editor.md) page.

### Node3D node

[Node2D](../godot_gdscript_nodes_2d.md) is the base node for 2D. [Control](../godot_gdscript_ui_controls.md) is the base node for everything GUI. Following this reasoning, the 3D engine uses the [Node3D](../godot_gdscript_nodes_3d.md) node for everything 3D.

Node3Ds have a local transform, which is relative to the parent node (as long as the parent node is also of **or inherits from** the type Node3D). This transform can be accessed as a 3×4 [Transform3D](../godot_gdscript_math_types.md), or as 3 [Vector3](../godot_gdscript_math_types.md) members representing location, Euler rotation (X, Y and Z angles) and scale.

### 3D content

Unlike 2D, where loading image content and drawing is straightforward, 3D is a little more difficult. The content needs to be created with special 3D tools (also called Digital Content Creation tools, or DCCs) and exported to an exchange file format to be imported in Godot. This is required since 3D formats are not as standardized as images.

#### Manually authored models (using 3D modeling software)

It is possible to import 3D models in Godot created in external tools. Depending on the format, you can import entire scenes (exactly as they look in the 3D modeling software), including animation, skeletal rigs, blend shapes, or as simple resources.

> **See also:** See [Importing 3D scenes](tutorials_assets_pipeline.md) for more on importing.

#### Generated geometry

It is possible to create custom geometry by using the [ArrayMesh](../godot_gdscript_rendering.md) resource directly. Simply create your arrays and use the [ArrayMesh.add_surface_from_arrays()](../godot_gdscript_rendering.md) function. A helper class is also available, [SurfaceTool](../godot_gdscript_rendering.md), which provides a more straightforward API and helpers for indexing, generating normals, tangents, etc.

In any case, this method is meant for generating static geometry (models that will not be updated often), as creating vertex arrays and submitting them to the 3D API has a significant performance cost.

> **Note:** To learn about prototyping inside Godot or using external tools, see Prototyping levels with CSG.

#### Immediate geometry

If, instead, you need to generate simple geometry that will be updated often, Godot provides a special [ImmediateMesh](../godot_gdscript_rendering.md) resource that can be used in a [MeshInstance3D](../godot_gdscript_nodes_3d.md) node. This provides an OpenGL 1.x-style immediate-mode API to create points, lines, triangles, etc.

#### 2D in 3D

While Godot packs a powerful 2D engine, many types of games use 2D in a 3D environment. By using a fixed camera (either orthogonal or perspective) that does not rotate, nodes such as [Sprite3D](../godot_gdscript_misc.md) and [AnimatedSprite3D](../godot_gdscript_misc.md) can be used to create 2D games that take advantage of mixing with 3D backgrounds, more realistic parallax, lighting/shadow effects, etc.

The disadvantage is, of course, that added complexity and reduced performance in comparison to plain 2D, as well as the lack of reference of working in pixels.

### Environment

Besides editing a scene, it is often common to edit the environment. Godot provides a [WorldEnvironment](../godot_gdscript_nodes_3d.md) node that allows changing the background color, mode (as in, put a skybox), and applying several types of built-in post-processing effects. Environments can also be overridden in the Camera.

#### Preview environment and light

By default, any 3D scene that doesn't have a [WorldEnvironment](../godot_gdscript_nodes_3d.md) node, or a [DirectionalLight3D](../godot_gdscript_nodes_3d.md), will have a preview turned on for what it's missing to light the scene.

The preview light and environment will only be visible in the scene while in the editor. If you run the scene or export the project they will not affect the scene.

The preview light and environment can be turned on or off from the top menu by clicking on their respective icon.

The three dots dropdown menu next to those icons can be used to adjust the properties of the preview environment and light if they are enabled.

The same preview sun and environment is used for every scene in the same project, So only make adjustments that would apply to all of the scenes you will need a preview light and environment for.

#### Cameras

No matter how many objects are placed in the 3D space, nothing will be displayed unless a [Camera3D](../godot_gdscript_nodes_3d.md) is also added to the scene. Cameras can work in either orthogonal or perspective projections:

Cameras are associated with (and only display to) a parent or grandparent viewport. Since the root of the scene tree is a viewport, cameras will display on it by default, but if sub-viewports (either as render target or picture-in-picture) are desired, they need their own children cameras to display.

When dealing with multiple cameras, the following rules are enforced for each viewport:

- If no cameras are present in the scene tree, the first one that enters it will become the active camera. Further cameras entering the scene will be ignored (unless they are set as _current_).
- If a camera has the "_current_" property set, it will be used regardless of any other camera in the scene. If the property is set, it will become active, replacing the previous camera.
- If an active camera leaves the scene tree, the first camera in tree-order will take its place.

#### Lights

The background environment emits some ambient light which appears on surfaces. Still, without any light sources placed in the scene, the scene will appear quite dark unless the background environment is very bright.

Most outdoor scenes have a directional light (the sun or moon), while indoor scenes typically have several positional lights (lamps, torches, …). See 3D lights and shadows for more information on setting up lights in Godot.

---
