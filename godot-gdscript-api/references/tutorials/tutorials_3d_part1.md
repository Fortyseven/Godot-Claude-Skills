# Godot 4 GDScript Tutorials — 3D (Part 1)

> 4 tutorials. GDScript-specific code examples.

## 3D antialiasing

> **See also:** Godot also supports antialiasing in 2D rendering. This is covered on the [2D antialiasing](tutorials_2d.md) page.

### Introduction

Due to their limited resolution, scenes rendered in 3D can exhibit aliasing artifacts. These artifacts commonly manifest as a "staircase" effect on surface edges (edge aliasing) and as flickering and/or sparkles on reflective surfaces (specular aliasing).

In the example below, you can notice how edges have a blocky appearance. The vegetation is also flickering in and out, and thin lines on top of the box have almost disappeared:

To combat this, various antialiasing techniques can be used in Godot. These are detailed below.

> **See also:** You can compare antialiasing algorithms in action using the [3D Antialiasing demo project](https://github.com/godotengine/godot-demo-projects/tree/master/3d/antialiasing).

### Multisample antialiasing (MSAA)

_This is available in all renderers._

This technique is the "historical" way of dealing with aliasing. MSAA is very effective on geometry edges (especially at higher levels). MSAA does not introduce any blurriness whatsoever.

MSAA is available in 3 levels: 2×, 4×, 8×. Higher levels are more effective at antialiasing edges, but are significantly more demanding. In games with modern visuals, sticking to 2× or 4× MSAA is highly recommended as 8× MSAA is usually too demanding.

The downside of MSAA is that it only operates on edges. This is because MSAA increases the number of _coverage_ samples, but not the number of _color_ samples. However, since the number of color samples did not increase, fragment shaders are still run for each pixel only once. Therefore, MSAA does not reduce transparency aliasing for materials using the **Alpha Scissor** transparency mode (1-bit transparency). MSAA is also ineffective on specular aliasing.

To mitigate aliasing on alpha scissor materials, alpha antialiasing (also called _alpha to coverage_) can be enabled on specific materials in the StandardMaterial3D or ORMMaterial3D properties. Alpha to coverage has a moderate performance cost, but it's effective at reducing aliasing on transparent materials without introducing any blurriness.

To make specular aliasing less noticeable, use the **Screen-space roughness limiter**, which is enabled by default.

MSAA can be enabled in the Project Settings by changing the value of the [Rendering > Anti Aliasing > Quality > MSAA 3D](../godot_gdscript_misc.md) setting. It's important to change the value of the **MSAA 3D** setting and not **MSAA 2D**, as these are entirely separate settings.

Comparison between no antialiasing (left) and various MSAA levels (right). Note that alpha antialiasing is not used here:

### Temporal antialiasing (TAA)

_This is only available in the Forward+ renderer, not the Mobile or Compatibility renderers._

Temporal antialiasing works by _converging_ the result of previously rendered frames into a single, high-quality frame. This is a continuous process that works by jittering the position of all vertices in the scene every frame. This jittering is done to capture sub-pixel detail and should be unnoticeable except in extreme situations.

This technique is commonly used in modern games, as it provides the most effective form of antialiasing against specular aliasing and other shader-induced artifacts. TAA also provides full support for transparency antialiasing.

TAA introduces a small amount of blur when enabled in still scenes, but this blurring effect becomes more pronounced when the camera is moving. Another downside of TAA is that it can exhibit _ghosting_ artifacts behind moving objects. Rendering at a higher framerate will allow TAA to converge faster, therefore making those ghosting artifacts less visible.

Temporal antialiasing can be enabled in the Project Settings by changing the value of the [Rendering > Anti Aliasing > Quality > TAA](../godot_gdscript_misc.md) setting.

Comparison between no antialiasing (left) and TAA (right):

### AMD FidelityFX Super Resolution 2.2 (FSR2)

_This is only available in the Forward+ renderer, not the Mobile or Compatibility renderers._

Since Godot 4.2, there is built-in support for [AMD FidelityFX Super Resolution](https://www.amd.com/en/products/graphics/technologies/fidelityfx/super-resolution.html) 2.2. This is an upscaling method compatible with all recent GPUs from any vendor. FSR2 is normally designed to improve performance by lowering the internal 3D rendering resolution, then upscaling to the output resolution.

However, unlike FSR1, FSR2 also provides temporal antialiasing. This means FSR2 can be used at native resolution for high-quality antialiasing, with the input resolution being equal to the output resolution. In this situation, enabling FSR2 will actually _decrease_ performance, but it will significantly improve rendering quality.

Using FSR2 at native resolution is more demanding than using TAA at native resolution, so its use is only recommended if you have significant GPU headroom. On the bright side, FSR2 provides better antialiasing coverage with less blurriness compared to TAA, especially in motion.

Comparison between no antialiasing (left) and FSR2 at native resolution (right):

> **Note:** By default, the **FSR Sharpness** project setting is set to `0.2` (higher values result in less sharpening). For the purposes of comparison, FSR sharpening has been disabled by setting it to `2.0` on the above screenshot.

### Fast approximate antialiasing (FXAA)

_This is only available in the Forward+ and Mobile renderers, not the Compatibility renderer._

Fast approximate antialiasing is a post-processing antialiasing solution. It is faster to run than any other antialiasing technique and also supports antialiasing transparency. However, since it lacks temporal information, it will not do much against specular aliasing.

This technique is still sometimes used in mobile games. However, on desktop platforms, FXAA generally fell out of fashion in favor of temporal antialiasing, which is much more effective against specular aliasing. Nonetheless, exposing FXAA as an in-game option may still be worthwhile for players with low-end GPUs.

FXAA introduces a moderate amount of blur when enabled (more than TAA when still, but less than TAA when the camera is moving).

FXAA can be enabled in the Project Settings by changing the value of the [Rendering > Anti Aliasing > Quality > Screen Space AA](../godot_gdscript_misc.md) setting to `FXAA`.

Comparison between no antialiasing (left) and FXAA (right):

### Sub-pixel Morphological Antialiasing (SMAA 1x)

_This is only available in the Forward+ and Mobile renderers, not the Compatibility renderer._

Sub-pixel Morphological Antialiasing is a post-processing antialiasing solution. It runs slightly slower than FXAA, but produces less blurriness. This is very helpful when the screen resolution is 1080p or below. Just like FXAA, SMAA 1x lacks temporal information and will therefore not do much against specular aliasing.

Use SMAA 1x if you can't afford MSAA, but find FXAA too blurry.

Combine it with TAA, or even FSR2, to maximize antialiasing at a higher GPU cost and some added blurriness. This is most beneficial in fast-moving scenes or just after a camera cut, especially at lower FPS.

SMAA 1x can be enabled in the Project Settings by changing the value of the [Rendering > Anti Aliasing > Quality > Screen Space AA](../godot_gdscript_misc.md) setting to `SMAA`.

Comparison between no antialiasing (left) and SMAA 1x (right):

### Supersample antialiasing (SSAA)

_This is available in all renderers._

Supersampling provides the highest quality of antialiasing possible, but it's also the most expensive. It works by shading every pixel in the scene multiple times. This allows SSAA to antialias edges, transparency _and_ specular aliasing at the same time, without introducing potential ghosting artifacts.

The downside of SSAA is its _extremely_ high cost. This cost generally makes SSAA difficult to use for game purposes, but you may still find supersampling useful for [offline rendering](tutorials_animation.md).

Supersample antialiasing is performed by increasing the [Rendering > Scaling 3D > Scale](../godot_gdscript_misc.md) advanced project setting above `1.0` while ensuring [Rendering > Scaling 3D > Mode](../godot_gdscript_misc.md) is set to `Bilinear` (the default). Since the scale factor is defined per-axis, a scale factor of `1.5` will result in 2.25× SSAA while a scale factor of `2.0` will result in 4× SSAA. Since Godot uses the hardware's own bilinear filtering to perform the downsampling, the result will look crisper at integer scale factors (namely, `2.0`).

Comparison between no antialiasing (left) and various SSAA levels (right):

> **Warning:** Supersampling also has high video RAM requirements, since it needs to render in the target resolution then _downscale_ to the window size. For example, displaying a project in 3840×2160 (4K resolution) with 4× SSAA will require rendering the scene in 7680×4320 (8K resolution), which is 4 times more pixels. If you are using a high window size such as 4K, you may find that increasing the resolution scale past a certain value will cause a heavy slowdown (or even a crash) due to running out of VRAM.

### Screen-space roughness limiter

_This is only available in the Forward+ and Mobile renderers, not the Compatibility renderer._

This is not an edge antialiasing method, but it is a way of reducing specular aliasing in 3D.

The screen-space roughness limiter works best on detailed geometry. While it has an effect on roughness map rendering itself, its impact is limited there.

The screen-space roughness limiter is enabled by default; it doesn't require any manual setup. It has a small performance impact, so consider disabling it if your project isn't affected by specular aliasing much. You can disable it with the **Rendering > Quality > Screen Space Filters > Screen Space Roughness Limiter** project setting.

### Texture roughness limiter on import

Like the screen-space roughness limiter, this is not an edge antialiasing method, but it is a way of reducing specular aliasing in 3D.

Roughness limiting on import works by specifying a normal map to use as a guide for limiting roughness. This is done by selecting the roughness map in the FileSystem dock, then going to the Import dock and setting **Roughness > Mode** to the color channel the roughness map is stored in (typically **Green**), then setting the path to the material's normal map. Remember to click **Reimport** at the bottom of the Import dock after setting the path to the normal map.

Since this processing occurs purely on import, it has no performance cost whatsoever. However, its visual impact is limited. Limiting roughness on import only helps reduce specular aliasing within textures, not the aliasing that occurs on geometry edges on detailed meshes.

### Which antialiasing technique should I use?

**There is no "one size fits all" antialiasing technique.** Since antialiasing is often demanding on the GPU or can introduce unwanted blurriness, you'll want to add a setting to allow players to disable antialiasing.

For projects with a photorealistic art direction, TAA is generally the most suitable option. While TAA can introduce ghosting artifacts, there is no other technique that combats specular aliasing as well as TAA does. The screen-space roughness limiter helps a little, but is far less effective against specular aliasing overall. If you have spare GPU power, you can use FSR2 at native resolution for a better-looking form of temporal antialiasing compared to standard TAA.

For projects with a low amount of reflective surfaces (such as a cartoon artstyle), MSAA can work well. MSAA is also a good option if avoiding blurriness and temporal artifacts is important, such as in competitive games.

When targeting low-end platforms such as mobile or integrated graphics, FXAA is usually the only viable option. 2× MSAA may be usable in some circumstances, but higher MSAA levels are unlikely to run smoothly on mobile GPUs.

Godot allows using multiple antialiasing techniques at the same time. This is usually unnecessary, but it can provide better visuals on high-end GPUs or for [non-real-time rendering](tutorials_animation.md). For example, to make moving edges look better when TAA is enabled, you can also enable MSAA at the same time.

#### Antialiasing comparison

| Feature                   | MSAA        | TAA        | FSR2       | FXAA        | SMAA 1x | SSAA         | SSRL    |
| ------------------------- | ----------- | ---------- | ---------- | ----------- | ------- | ------------ | ------- |
| Edge antialiasing         | 🟢 Yes      | 🟢 Yes     | 🟢 Yes     | 🟢 Yes      | 🟢 Yes  | 🟢 Yes       | 🔴 No   |
| Specular antialiasing     | 🟡 Some     | 🟢 Yes     | 🟢 Yes     | 🟡 Some     | 🟡 Some | 🟢 Yes       | 🟢 Yes  |
| Transparency antialiasing | 🟡 Some [1] | 🟢 Yes [2] | 🟢 Yes [2] | 🟢 Yes      | 🟢 Yes  | 🟢 Yes       | 🔴 No   |
| Added blur                | 🟢 None     | 🟡 Some    | 🟡 Some    | 🟡 Some     | 🟢 Low  | 🟡 Some [3]  | 🟢 None |
| Ghosting artifacts        | 🟢 None     | 🔴 Yes     | 🔴 Yes     | 🟢 None     | 🟢 None | 🟢 None      | 🟢 None |
| Performance cost          | 🟡 Medium   | 🟡 Medium  | 🔴 High    | 🟢 Very Low | 🟢 Low  | 🔴 Very High | 🟢 Low  |
| Forward+                  | ✔️ Yes      | ✔️ Yes     | ✔️ Yes     | ✔️ Yes      | ✔️ Yes  | ✔️ Yes       | ✔️ Yes  |
| Mobile                    | ✔️ Yes      | ❌ No      | ❌ No      | ✔️ Yes      | ✔️ Yes  | ✔️ Yes       | ✔️ Yes  |
| Compatibility             | ✔️ Yes      | ❌ No      | ❌ No      | ❌ No       | ❌ No   | ✔️ Yes       | ❌ No   |

[**1**]

MSAA does not work well with materials with Alpha Scissor (1-bit transparency). This can be mitigated by enabling `alpha antialiasing` on the material.

[2] (**1**,**2**)

TAA/FSR2 transparency antialiasing is most effective when using Alpha Scissor.

[**3**]

SSAA has some blur from bilinear downscaling. This can be mitigated by using an integer scaling factor of `2.0`.

---

## 3D rendering limitations

### Introduction

Due to their focus on performance, real-time rendering engines have many limitations. Godot's renderer is no exception. To work effectively with those limitations, you need to understand them.

### Texture size limits

On desktops and laptops, textures larger than 8192×8192 may not be supported on older devices. You can check your target GPU's limitations on [GPUinfo.org](https://www.gpuinfo.org/).

Mobile GPUs are typically limited to 4096×4096 textures. Also, some mobile GPUs don't support repeating non-power-of-two-sized textures. Therefore, if you want your texture to display correctly on all platforms, you should avoid using textures larger than 4096×4096 and use a power of two size if the texture needs to repeat.

To limit the size of a specific texture that may be too large to render, you can set the **Process > Size Limit** import option to a value greater than `0`. This will reduce the texture's dimensions on import (preserving aspect ratio) without affecting the source file.

### Color banding

When using the Forward+ or Mobile rendering methods, Godot's 3D engine renders internally in HDR. However, the rendering output will be tonemapped to a low dynamic range so it can be displayed on the screen. This can result in visible banding, especially when using untextured materials. For performance reasons, color precision is also lower when using the Mobile rendering method compared to Forward+.

When using the Compatibility rendering method, HDR is not used and the color precision is the lowest of all rendering methods. This also applies to 2D rendering, where banding may be visible when using smooth gradient textures.

There are two main ways to alleviate banding:

- If using the Forward+ or Forward Mobile rendering methods, enable [Use Debanding](../godot_gdscript_misc.md) in **Project Settings > Rendering > Anti Aliasing**. This applies a fullscreen debanding shader as a post-processing effect and is very cheap.
- Alternatively, bake some noise into your textures. This is mainly effective in 2D, e.g. for vignetting effects. In 3D, you can also use a [custom debanding shader](https://github.com/fractilegames/godot-gles2-debanding-material) to be applied on your _materials_. This technique works even if your project is rendered with low color precision, which means it will work when using the Mobile and Compatibility rendering methods.

> **See also:** See [Banding in Games: A Noisy Rant (PDF)](https://loopit.dk/banding_in_games.pdf) for more details about banding and ways to combat it.

### Depth buffer precision

To sort objects in 3D space, rendering engines rely on a _depth buffer_ (also called _Z-buffer_). This buffer has a finite precision: 24-bit on desktop platforms, sometimes 16-bit on mobile platforms (for performance reasons). If two different objects end up on the same buffer value, then Z-fighting will occur. This will materialize as textures flickering back and forth as the camera moves or rotates.

To make the depth buffer more precise over the rendered area, you should _increase_ the Camera node's **Near** property. However, be careful: if you set it too high, players will be able to see through nearby geometry. You should also _decrease_ the Camera node's **Far** property to the lowest permissible value for your use case, though keep in mind it won't impact precision as much as the **Near** property.

If you only need high precision when the player can see far away, you could change it dynamically based on the game conditions. For instance, if the player enters an airplane, the **Near** property can be temporarily increased to avoid Z-fighting in the distance. It can then be decreased once the player leaves the airplane.

Depending on the scene and viewing conditions, you may also be able to move the Z-fighting objects further apart without the difference being visible to the player.

### Transparency sorting

In Godot, transparent materials are drawn after opaque materials. Transparent objects are sorted back to front before being drawn based on the Node3D's position, not the vertex position in world space. Due to this, overlapping objects may often be sorted out of order. To fix improperly sorted objects, tweak the material's [Render Priority](../godot_gdscript_misc.md) property or the node's [Sorting Offset](../godot_gdscript_misc.md). Render Priority will force specific materials to appear in front of or behind other transparent materials, while Sorting Offset will move the object forward or backward for the purpose of sorting. Even then, these may not always be sufficient.

Transparent objects are not rendered to the normal-roughness buffer, as they are drawn after opaque geometry. As a result, features that rely on the normal-roughness buffer will not affect transparent materials.

Some rendering engines feature _order-independent transparency_ techniques to alleviate this, but this is costly on the GPU. Godot currently doesn't provide this feature. There are still several ways to avoid this problem:

- Only make materials transparent if you actually need it. If a material only has a small transparent part, consider splitting it into a separate material. This will allow the opaque part to cast shadows and will also improve performance.
- If your texture mostly has fully opaque and fully transparent areas, you can use alpha testing instead of alpha blending. This transparency mode is faster to render and doesn't suffer from transparency issues. Enable **Transparency > Transparency** to **Alpha Scissor** in StandardMaterial3D, and adjust **Transparency > Alpha Scissor Threshold** accordingly if needed. Note that MSAA will not antialias the texture's edges unless alpha antialiasing is enabled in the material's properties. However, FXAA, TAA and supersampling will be able to antialias the texture's edges regardless of whether alpha antialiasing is enabled on the material.
- If you need to render semi-transparent areas of the texture, alpha scissor isn't suitable. Instead, setting the StandardMaterial3D's **Transparency > Transparency** property to **Depth Pre-Pass** can sometimes work (at a performance cost). You can also try the **Alpha Hash** mode.
- If you want a material to fade with distance, use the StandardMaterial3D distance fade mode **Pixel Dither** or **Object Dither** instead of **Pixel Alpha**. This will make the material opaque, which also speeds up rendering.

---

## 3D text

### Introduction

In a project, there may be times when text needs to be created as part of a 3D scene and not just in the HUD. Godot provides 2 methods to do this: the Label3D node and the TextMesh _resource_ for a MeshInstance3D node.

Additionally, Godot makes it possible to position Control nodes according to a 3D point's position on the camera. This can be used as an alternative to "true" 3D text in situations where Label3D and TextMesh aren't flexible enough.

> **See also:** You can see 3D text in action using the [3D Labels and Texts demo project](https://github.com/godotengine/godot-demo-projects/tree/master/3d/labels_and_texts). This page does **not** cover how to display a GUI scene within a 3D environment. For information on how to achieve that, see the [GUI in 3D](https://github.com/godotengine/godot-demo-projects/tree/master/viewport/gui_in_3d) demo project.

### Label3D

Label3D behaves like a Label node, but in 3D space. Unlike the Label node, this Label3D node does **not** inherit properties of a GUI theme. However, its look remains customizable and uses the same font subresource as Control nodes (including support for MSDF font rendering).

#### Advantages

- Label3D is faster to generate than TextMesh. While both use a caching mechanism to only render new glyphs once, Label3D will still be faster to (re)generate, especially for long text. This can avoid stuttering during gameplay on low-end CPUs or mobile.
- Label3D can use bitmap fonts and dynamic fonts (with and without MSDF or mipmaps). This makes it more flexible on that aspect compared to TextMesh, especially for rendering fonts with self-intersecting outlines or colored fonts (emoji).

> **See also:** See [Using Fonts](tutorials_ui.md) for guidelines on configuring font imports.

#### Limitations

By default, Label3D has limited interaction with a 3D environment. It can be occluded by geometry and lit by light sources if the **Shaded** flag is enabled. However, it will not cast shadows even if **Cast Shadow** is set to **On** in the Label3D's GeometryInstance3D properties. This is because the node internally generates a quad mesh (one glyph per quad) with transparent textures and has the same limitations as Sprite3D. Transparency sorting issues can also become apparent when several Label3Ds overlap, especially if they have outlines.

This can be mitigated by setting the Label3D's transparency mode to **Alpha Cut**, at the cost of less smooth text rendering. The **Opaque Pre-Pass** transparency mode can preserve text smoothness while allowing the Label3D to cast shadows, but some transparency sorting issues will remain.

See Transparency sorting section in the 3D rendering limitations page for more information.

Text rendering quality can also suffer when the Label3D is viewed at a distance. To improve text rendering quality, [enable mipmaps on the font](tutorials_ui.md) or [switch the font to use MSDF rendering](tutorials_ui.md).

### TextMesh

The TextMesh resource has similarities to Label3D. They both display text in a 3D scene, and will use the same font subresource. However, instead of generating transparent quads, TextMesh generates 3D geometry that represents the glyphs' contours and has the properties of a mesh. As a result, a TextMesh is shaded by default and automatically casts shadows onto the environment. A TextMesh can also have a material applied to it (including custom shaders).

Here is an example of a texture and how it's applied to the mesh. You can use the texture below as a reference for the generated mesh's UV map:

#### Advantages

TextMesh has a few advantages over Label3D:

- TextMesh can use a texture to modify text color on a per-side basis.
- TextMesh geometry can have actual depth to it, giving glyphs a 3D look.
- TextMesh can use custom shaders, unlike Label3D.

#### Limitations

There are some limitations to TextMesh:

- No built-in outline support, unlike Label3D. This can be simulated using custom shaders though.
- Only dynamic fonts are supported (`.ttf`, `.otf`, `.woff`, `.woff2`). Bitmap fonts in the `.fnt` or `.font` formats are **not** supported.
- Fonts with self-intersecting outlines will not render correctly. If you notice rendering issues on fonts downloaded from websites such as Google Fonts, try downloading the font from the font author's official website instead.
- Antialiasing the text rendering requires a full-scene antialiasing method to be enabled such as MSAA, FXAA and temporal antialiasing (TAA). If no antialiasing method is enabled, text will appear grainy, especially at a distance. See 3D antialiasing for more information.

### Projected Label node (or any other Control)

There is a last solution that is more complex to set up, but provides the most flexibility: projecting a 2D node onto 3D space. This can be achieved using the return value of [unproject_position](../godot_gdscript_misc.md) method on a Camera3D node in a script's `_process()` function. This return value should then be used to set the `position` property of a Control node.

See the [3D waypoints](https://github.com/godotengine/godot-demo-projects/tree/master/3d/waypoints) demo for an example of this.

#### Advantages

- Any Control node can be used, including Label, RichTextLabel or even nodes such as Button. This allows for powerful formatting and GUI interaction.
- The script-based approach allows for complete freedom in positioning. For example, this makes it considerably easier to pin Controls to the screen's edges when they go off-screen (for in-game 3D markers).
- Control theming is obeyed. This allows for easier customization that globally applies to the project.

#### Limitations

- Projected Controls cannot be occluded by 3D geometry in any way. You can use a RayCast to fully hide the control if its target position is occluded by a collider, but this doesn't allow for partially hiding the control behind a wall.
- Changing text size depending on distance by adjusting the Control's `scale` property is possible, but it needs to be done manually. Label3D and TextMesh automatically take care of this, at the cost of less flexibility (can't set a minimum/maximum text size in pixels).
- Handling resolution and aspect ratio changes must be taken into account in the script, which can be challenging.

### Should I use Label3D, TextMesh or a projected Control?

In most scenarios, Label3D is recommended as it's easier to set up and provides higher rendering quality (especially if 3D antialiasing is disabled).

For advanced use cases, TextMesh is more flexible as it allows styling the text with custom shaders. Custom shaders allow for modifying the final geometry, such as curving the text along a surface. Since the text is actual 3D geometry, the text can optionally have depth to it and can also contribute to global illumination.

If you need features such as BBCode or Control theming support, then using a projected RichTextLabel node is the only way to go.

---

## Prototyping levels with CSG

> **Work in progress:** The content of this page was not yet updated for Godot `4.6` and may be **outdated**. If you know how to improve this page or you can confirm that it's up to date, feel free to [open a pull request](https://github.com/godotengine/godot-docs).

CSG stands for **Constructive Solid Geometry**, and is a tool to combine basic shapes or custom meshes to create more complex shapes. In 3D modeling software, CSG is mostly known as "Boolean Operators".

Level prototyping is one of the main uses of CSG in Godot. This technique allows users to create the most common shapes by combining primitives. Interior environments can be created by using inverted primitives.

> **Note:** The CSG nodes in Godot are mainly intended for prototyping. There is no built-in support for UV mapping or editing 3D polygons (though extruded 2D polygons can be used with the CSGPolygon3D node). If you're looking for an easy to use level design tool for a project, you may want to use [FuncGodot](https://github.com/func-godot/func_godot_plugin) or [Cyclops Level Builder](https://github.com/blackears/cyclopsLevelBuilder) instead.

> **See also:** You can check how to use CSG nodes to build various shapes (such as stairs or roads) using the [Constructive Solid Geometry demo project](https://github.com/godotengine/godot-demo-projects/tree/master/3d/csg).

### Introduction to CSG nodes

Like other features of Godot, CSG is supported in the form of nodes. These are the CSG nodes:

- [CSGBox3D](../godot_gdscript_misc.md)
- [CSGCylinder3D](../godot_gdscript_misc.md) (also supports cone)
- [CSGSphere3D](../godot_gdscript_misc.md)
- [CSGTorus3D](../godot_gdscript_misc.md)
- [CSGPolygon3D](../godot_gdscript_misc.md)
- [CSGMesh3D](../godot_gdscript_misc.md)
- [CSGCombiner3D](../godot_gdscript_misc.md)

#### CSG tools features

Every CSG node supports 3 kinds of boolean operations:

- **Union:** Geometry of both primitives is merged, intersecting geometry is removed.
- **Intersection:** Only intersecting geometry remains, the rest is removed.
- **Subtraction:** The second shape is subtracted from the first, leaving a dent with its shape.

#### CSGPolygon

The [CSGPolygon3D](../godot_gdscript_misc.md) node extrude along a Polygon drawn in 2D (in X, Y coordinates) in the following ways:

- **Depth:** Extruded back a given amount.
- **Spin:** Extruded while spinning around its origin.
- **Path:** Extruded along a Path node. This operation is commonly called lofting.

> **Note:** The **Path** mode must be provided with a [Path3D](../godot_gdscript_nodes_3d.md) node to work. In the Path node, draw the path and the polygon in CSGPolygon3D will extrude along the given path.

#### Custom meshes

Custom meshes can be used for [CSGMesh3D](../godot_gdscript_misc.md) as long as the mesh is _manifold_. The mesh can be modeled in other software and imported into Godot. Multiple materials are supported.

For a mesh to be used as a CSG mesh, it is required to:

- be closed
- have each edge connect to only two faces
- have volume

And it is recommended to avoid:

- negative volume
- self-intersection
- interior faces

Godot uses the [manifold](https://github.com/elalish/manifold) library to implement CSG meshes. The technical definition of "manifold" used by Godot is the following, adapted from that library's [definition of "manifold"](https://github.com/elalish/manifold/wiki/Manifold-Library#manifoldness-definition):

Every edge of every triangle must contain the same two vertices (by index) as exactly one other triangle edge, and the start and end vertices must switch places between these two edges. The triangle vertices must appear in clockwise order when viewed from the outside of the Godot Engine manifold mesh.

##### Making an existing mesh manifold with Blender

If you have an existing mesh that is not already manifold, you can make it manifold using Blender.

In Blender, install and enable the [3D Print Toolbox](https://extensions.blender.org/add-ons/print3d-toolbox/) addon.

Select the mesh you want to make manifold. Open the sidebar by clicking on the arrow:

In the **3D Print** tab, under **Clean Up**, click the **Make Manifold** button:

The mesh should now be manifold, and can be used as a custom mesh.

#### CSGCombiner3D

The [CSGCombiner3D](../godot_gdscript_misc.md) node is an empty shape used for organization. It will only combine children nodes.

#### Processing order

Every CSG node will first process its children nodes and their operations: union, intersection, or subtraction, in tree order, and apply them to itself one after the other.

> **Note:** In the interest of performance, make sure CSG geometry remains relatively simple, as complex meshes can take a while to process. If adding objects together (such as table and room objects), create them as separate CSG trees. Forcing too many objects in a single tree will eventually start affecting performance. Only use binary operations where you actually need them.

### Prototyping a level

We will prototype a room to practice the use of CSG tools.

> **Tip:** Working in **Orthogonal** projection gives a better view when combining the CSG shapes.

Our level will contain these objects:

- a room,
- a bed,
- a lamp,
- a desk,
- a bookshelf.

Create a scene with a Node3D node as root node.

> **Tip:** The default lighting of the environment doesn't provide clear shading at some angles. Change the display mode using **Display Overdraw** in the 3D viewport menu, or add a DirectionalLight node to help you see clearly.

Create a CSGBox3D and name it `room`, enable **Invert Faces** and change the dimensions of your room.

Next, create a CSGCombiner3D and name it `desk`.

A desk has one surface and 4 legs:

- Create 1 CSGBox3D children node in **Union** mode for the surface and adjust the dimensions.
- Create 4 CSGBox3D children nodes in **Union** mode for the legs and adjust the dimensions.

Adjust their placement to resemble a desk.

> **Note:** CSG nodes inside a CSGCombiner3D will only process their operation within the combiner. Therefore, CSGCombiner3Ds are used to organize CSG nodes.

Create a CSGCombiner3D and name it `bed`.

Our bed consists of 3 parts: the bed, the mattress and a pillow. Create a CSGBox3D and adjust its dimension for the bed. Create another CSGBox3D and adjust its dimension for the mattress.

We will create another CSGCombiner3D named `pillow` as the child of `bed`. The scene tree should look like this:

We will combine 3 CSGSphere3D nodes in **Union** mode to form a pillow. Scale the Y axis of the spheres and enable **Smooth Faces**.

Select the `pillow` node and switch the mode to **Subtraction**; the combined spheres will cut a hole into the mattress.

Try to re-parent the `pillow` node to the root `Node3D` node; the hole will disappear.

> **Note:** This is to illustrate the effect of CSG processing order. Since the root node is not a CSG node, the CSGCombiner3D nodes are the end of the operations; this shows the use of CSGCombiner3D to organize the CSG scene.

Undo the re-parent after observing the effect. The bed you've built should look like this:

Create a CSGCombiner3D and name it `lamp`.

A lamp consists of 3 parts: the stand, the pole and the lampshade. Create a CSGCylinder3D, enable the **Cone** option and make it the stand. Create another CSGCylinder3D and adjust the dimensions to use it as a pole.

We will use a CSGPolygon3D for the lampshade. Use the **Spin** mode for the CSGPolygon3D and draw a [trapezoid](https://en.wikipedia.org/wiki/Trapezoid) while in **Front View** (numeric keypad 1); this shape will extrude around the origin and form the lampshade.

Adjust the placement of the 3 parts to make it look like a lamp.

Create a CSGCombiner3D and name it `bookshelf`.

We will use 3 CSGBox3D nodes for the bookshelf. Create a CSGBox3D and adjust its dimensions; this will be the size of the bookshelf.

Duplicate the CSGBox3D and shorten the dimensions of each axis and change the mode to **Subtraction**.

You've almost built a shelf. Create one more CSGBox3D for dividing the shelf into two levels.

Position your furniture in your room as you like and your scene should look this:

You've successfully prototyped a room level with the CSG tools in Godot. CSG tools can be used for designing all kinds of levels, such as a maze or a city; explore its limitations when designing your game.

### Using prototype textures

Godot's Standard Material 3D and ORM Material 3D supports _triplanar mapping_, which can be used to automatically apply a texture to arbitrary objects without distortion. This is handy when using CSG as Godot doesn't support editing UV maps on CSG nodes yet. Triplanar mapping is relatively slow, which usually restricts its usage to organic surfaces like terrain. Still, when prototyping, it can be used to quickly apply textures to CSG-based levels.

> **Note:** If you need some textures for prototyping, Kenney made a [set of CC0-licensed prototype textures](https://kenney.nl/assets/prototype-textures).

There are two ways to apply a material to a CSG node:

- Applying it to a CSGCombiner3D node as a material override (**Geometry > Material Override** in the Inspector). This will affect its children automatically, but will make it impossible to change the material in individual children.
- Applying a material to individual nodes (**Material** in the Inspector). This way, each CSG node can have its own appearance. Subtractive CSG nodes will apply their material to the nodes they're "digging" into.

To apply triplanar mapping to a CSG node, select it, go to the Inspector, click the **[empty]** text next to **Material Override** (or **Material** for individual CSG nodes). Choose **New StandardMaterial3D**. Click the newly created material's icon to edit it. Unfold the **Albedo** section and load a texture into the **Texture** property. Now, unfold the **Uv1** section and check **Triplanar**. You can change the texture offset and scale on each axis by playing with the **Scale** and **Offset** properties just above. Higher values in the **Scale** property will cause the texture to repeat more often.

> **Tip:** You can copy a StandardMaterial3D to reuse it across CSG nodes. To do so, click the dropdown arrow next to a material property in the Inspector and choose **Copy**. To paste it, select the node you'd like to apply the material onto, click the dropdown arrow next to its material property then choose **Paste**.

### Converting to MeshInstance3D

Since Godot 4.4, you can convert a CSG node and its children to a [MeshInstance3D](../godot_gdscript_nodes_3d.md) node.

This has several benefits:

- Bake lightmaps, since UV2 can be generated on a MeshInstance3D.
- Bake occlusion culling, since the occlusion culling bake process only takes MeshInstance3D into account.
- Faster loading times, since the CSG mesh no longer needs to be rebuilt when the scene loads.
- Better performance when updating the node's transform if using the mesh within another CSG node.

To convert a CSG node to a MeshInstance3D node, select it, then choose **CSG > Bake Mesh Instance** in the toolbar. The MeshInstance3D node will be created as a sibling. Note that the CSG node that was used for baking is **not** hidden automatically, so remember to hide it to prevent its geometry from overlapping with the newly created MeshInstance3D.

You can also create a trimesh collision shape using **CSG > Bake Collision Shape**. The generated [CollisionShape3D](../godot_gdscript_physics.md) node must be a child of a [StaticBody3D](../godot_gdscript_nodes_3d.md) or [AnimatableBody3D](../godot_gdscript_nodes_3d.md) node to be effective.

> **Tip:** Remember to keep the original CSG node in the scene tree, so that you can perform changes to the geometry later if needed. To make changes to the geometry, remove the MeshInstance3D node and make the root CSG node visible again.

### Exporting as glTF

It can be useful to block out a level using CSG, then export it as a 3d model, to import into 3D modeling software. You can do this by selecting **Scene > Export As... > glTF 2.0 Scene**.

---
