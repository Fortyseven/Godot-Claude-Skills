# Godot 4 GDScript Tutorials — 3D (Part 5)

> 4 tutorials. GDScript-specific code examples.

## 3D lights and shadows

### Introduction

Light sources emit light that mixes with the materials and produces a visible result. Light can come from several types of sources in a scene:

- From the material itself, in the form of the emission color (though it does not affect nearby objects unless baked or screen-space indirect lighting is enabled).
- Light nodes: DirectionalLight3D, OmniLight3D and SpotLight3D.
- Ambient light in the [Environment](../godot_gdscript_rendering.md) or Reflection probes.
- Global illumination (LightmapGI, VoxelGI or SDFGI).

The emission color is a material property. You can read more about it in the Standard Material 3D and ORM Material 3D tutorial.

> **See also:** You can compare various types of lights in action using the [3D Lights and Shadows demo project](https://github.com/godotengine/godot-demo-projects/tree/master/3d/lights_and_shadows).

### Light nodes

There are three types of light nodes: [DirectionalLight3D](../godot_gdscript_nodes_3d.md), [OmniLight3D](../godot_gdscript_nodes_3d.md) and [SpotLight3D](../godot_gdscript_nodes_3d.md). Let's take a look at the common parameters for lights:

Each property has a specific function:

- **Color:** Base color for emitted light.
- **Energy:** Energy multiplier. This is useful for saturating lights or working with High dynamic range lighting.
- **Indirect Energy:** Secondary multiplier used with indirect light (light bounces). This works with Using Lightmap global illumination, VoxelGI or SDFGI.
- **Volumetric Fog Energy:** Secondary multiplier used with volumetric fog. This only has an effect when volumetric fog is enabled.
- **Negative:** Light becomes subtractive instead of additive. It's sometimes useful to manually compensate some dark corners.
- **Specular:** Affects the intensity of the specular blob in objects affected by this light. At zero, this light becomes a pure diffuse light.
- **Bake Mode:** Sets the bake mode for the light. See Using Lightmap global illumination.
- **Cull Mask:** Objects that are in the selected layers below will be affected by this light. Note that objects disabled via this cull mask will still cast shadows. If you don't want disabled objects to cast shadows, adjust the **Cast Shadow** property on the GeometryInstance3D to the desired value.

> **See also:** See Physical light and camera units if you wish to use real world units to configure your lights' intensity and color temperature.

### Light number limits

When using the Forward+ renderer, Godot uses a _clustering_ approach for real-time lighting. As many lights as desired can be added (as long as performance allows). However, there's still a default limit of 512 _clustered elements_ that can be present in the current camera view. A clustered element is an omni light, a spot light, a decal or a reflection probe. This limit can be increased by adjusting [Max Clustered Elements](../godot_gdscript_misc.md) in **Project Settings > Rendering > Limits > Cluster Builder**.

When using the Mobile renderer, there is a limitation of 8 OmniLights + 8 SpotLights per mesh resource. There is also a limit of 256 OmniLights + 256 SpotLights that can be rendered in the current camera view. These limits currently cannot be changed.

When using the Compatibility renderer, up to 8 OmniLights + 8 SpotLights can be rendered per mesh resource. This limit can be increased in the advanced Project Settings by adjusting [Max Renderable Elements](../godot_gdscript_misc.md) and/or [Max Lights per Object](../godot_gdscript_misc.md) in **Rendering > Limits > OpenGL**, at the cost of performance and longer shader compilation times. The limit can also be decreased to reduce shader compilation times and improve performance slightly.

With all rendering methods, up to 8 DirectionalLights can be visible at a time. However, each additional DirectionalLight with shadows enabled will reduce the effective shadow resolution of each DirectionalLight. This is because directional shadow atlas is shared between all lights.

If the rendering limit is exceeded, lights will start popping in and out during camera movement, which can be distracting. Enabling **Distance Fade** on light nodes can help reduce this issue while also improving performance. Splitting your meshes into smaller portions can also help, especially for level geometry (which also improves culling efficiency).

If you need to render more lights than possible in a given renderer, consider using baked lightmaps with lights' bake mode set to **Static**. This allows lights to be fully baked, which also makes them much faster to render. You can also use emissive materials with any global illumination technique as a replacement for light nodes that emit light over a large area.

### Shadow mapping

Lights can optionally cast shadows. This gives them greater realism (light does not reach occluded areas), but it can incur a bigger performance cost. There is a list of generic shadow parameters, each also has a specific function:

- **Enabled:** Check to enable shadow mapping in this light.
- **Opacity:** Areas occluded are darkened by this opacity factor. Shadows are fully opaque by default, but this can be changed to make shadows translucent for a given light.
- **Bias:** When this parameter is too low, self-shadowing occurs. When too high, shadows separate from the casters. Tweak to what works best for you.
- **Normal Bias:** When this parameter is too low, self-shadowing occurs. When too high, shadows appear misaligned from the casters. Tweak to what works best for you.
- **Transmittance Bias:** When this parameter is too low, self-shadowing occurs on materials that have transmittance enabled. When too high, shadows will not affect materials that have transmittance enabled consistently. Tweak to what works best for you.
- **Reverse Cull Face:** Some scenes work better when shadow mapping is rendered with face-culling inverted.
- **Blur:** Multiplies the shadow blur radius for this light. This works with both traditional shadow mapping and contact-hardening shadows (lights with **Angular Distance** or **Size** greater than `0.0`). Higher values result in softer shadows, which will also appear to be more temporally stable for moving objects. The downside of increasing shadow blur is that it will make the grainy pattern used for filtering more noticeable. See also **Shadow filter mode**.
- **Caster Mask:** Shadows are only cast by objects in these layers. Note that this mask does not affect which objects shadows are cast _onto_.

#### Tweaking shadow bias

Below is an image of what tweaking bias looks like. Default values work for most cases, but in general, it depends on the size and complexity of geometry.

If the **Shadow Bias** or **Shadow Normal Bias** is set too low for a given light, the shadow will be "smeared" onto the objects. This will cause the light's intended appearance to darken, and is called _shadow acne_:

On the other hand, if the **Shadow Bias** or **Shadow Normal Bias** is set too high for a given light, the shadow may appear to be disconnected from the object. This is called _peter-panning_:

In general, increasing **Shadow Normal Bias** is preferred over increasing **Shadow Bias**. Increasing **Shadow Normal Bias** does not cause as much peter-panning as increasing **Shadow Bias**, but it can still resolve most shadow acne issues efficiently. The downside of increasing **Shadow Normal Bias** is that it can make shadows appear thinner for certain objects.

Any sort of bias issues can be fixed by **increasing the shadow map resolution**, at the cost of decreased performance.

> **Note:** Tweaking shadow mapping settings is an art – there are no "one size fits all" settings. To achieve the best visuals, you may need to use different shadow bias values on a per-light basis.

**Note on Appearance Changes**: When enabling shadows on a light, be aware that the light's appearance might change compared to when it's rendered without shadows in the compatibility renderer. Due to limitations with older mobile devices, shadows are implemented using a multi-pass rendering approach so lights with shadows are rendered in sRGB space instead of linear space. This change in rendering space can sometimes drastically alter the light's appearance. To achieve a similar appearance to an unshadowed light, you may need to adjust the light's energy setting.

### Directional light

This is the most common type of light and represents a light source very far away (such as the sun). It is also the cheapest light to compute and should be used whenever possible (although it's not the cheapest shadow-map to compute, but more on that later).

Directional light models an infinite number of parallel light rays covering the whole scene. The directional light node is represented by a big arrow which indicates the direction of the light rays. However, the position of the node does not affect the lighting at all and can be anywhere.

Every face whose front-side is hit by the light rays is lit, while the others stay dark. Unlike most other light types, directional lights don't have specific parameters.

The directional light also offers an **Angular Distance** property, which determines the light's angular size in degrees. Increasing this above `0.0` will make shadows softer at greater distances from the caster, while also affecting the sun's appearance in procedural sky materials. This is called a _contact-hardening_ shadow (also known as PCSS).

For reference, the angular distance of the Sun viewed from the Earth is approximately `0.5`. This kind of shadow is expensive, so check the recommendations in **PCSS recommendations** if setting this value above `0.0` on lights with shadows enabled.

#### Directional shadow mapping

To compute shadow maps, the scene is rendered (only depth) from an orthogonal point of view that covers the whole scene (or up to the max distance). There is, however, a problem with this approach because objects closer to the camera receive low-resolution shadows that may appear blocky.

To fix this, a technique named _Parallel Split Shadow Maps_ (PSSM) is used. This splits the view frustum in 2 or 4 areas. Each area gets its own shadow map. This allows small areas close to the viewer to have the same shadow resolution as a huge, far-away area. When shadows are enabled for DirectionalLight3D, the default shadow mode is PSSM with 4 splits. In scenarios where an object is large enough to appear in all four splits, it results in increased draw calls. Specifically, such an object will be rendered five times in total: once for each of the four shadow splits and once for the final scene rendering. This can impact performance, understanding this behavior is important for optimizing your scene and managing performance expectations.

With this, shadows become more detailed:

To control PSSM, a number of parameters are exposed:

Each split distance is controlled relative to the camera far (or shadow **Max Distance** if greater than `0.0`). `0.0` is the eye position and `1.0` is where the shadow ends at a distance. Splits are in-between. Default values generally work well, but tweaking the first split a bit is common to give more detail to close objects (like a character in a third-person game).

Always make sure to set a shadow **Max Distance** according to what the scene needs. A lower maximum distance will result in better-looking shadows and better performance, as fewer objects will need to be included in shadow rendering. You can also adjust **Fade Start** to control how aggressive the shadow fade-out should be at a distance. For scenes where the **Max Distance** fully covers the scene at any given camera position, you can increase **Fade Start** to `1.0` to prevent the shadow from fading at a distance. This should not be done in scenes where **Max Distance** doesn't fully cover the scene, as the shadow will appear to be suddenly cut off at a distance.

Sometimes, the transition between a split and the next can look bad. To fix this, the **Blend Splits** option can be turned on, which sacrifices detail and performance in exchange for smoother transitions:

The **Shadow > Normal Bias** parameter can be used to fix special cases of self-shadowing when objects are perpendicular to the light. The only downside is that it makes the shadow a bit thinner. Consider increasing **Shadow > Normal Bias** before increasing **Shadow > Bias** in most situations.

Lastly, **Pancake Size** is a property that can be adjusted to fix missing shadows when using large objects with unsubdivided meshes. Only change this value if you notice missing shadows that are not related to shadow biasing issues.

### Omni light

Omni light is a point source that emits light spherically in all directions up to a given radius.

In real life, light attenuation is an inverse function, which means omni lights don't have a radius. This is a problem because it means computing several omni lights would become demanding.

To solve this, a **Range** parameter is introduced together with an attenuation function.

These two parameters allow tweaking how this works visually in order to find aesthetically pleasing results.

A **Size** parameter is also available in OmniLight3D. Increasing this value will make the light fade out slower and shadows appear blurrier when far away from the caster. This can be used to simulate area lights to an extent. This is called a _contact-hardening_ shadow (also known as PCSS). This kind of shadow is expensive, so check the recommendations in **PCSS recommendations** if setting this value above `0.0` on lights with shadows enabled.

#### Omni shadow mapping

Omni light shadow mapping is relatively straightforward. The main issue that needs to be considered is the algorithm used to render it.

Omni Shadows can be rendered as either **Dual Paraboloid** or **Cube** mapped. **Dual Paraboloid** renders quickly, but can cause deformations, while **Cube** is more correct, but slower. The default is **Cube**, but consider changing it to **Dual Paraboloid** for lights where it doesn't make much of a visual difference.

If the objects being rendered are mostly irregular and subdivided, Dual Paraboloid is usually enough. In any case, as these shadows are cached in a shadow atlas (more on that at the end), it may not make a difference in performance for most scenes.

Omni lights with shadows enabled can make use of projectors. The projector texture will _multiply_ the light's color by the color at a given point on the texture. As a result, lights will usually appear to be darker once a projector texture is assigned; you can increase **Energy** to compensate for this.

Omni light projector textures require a special 360° panorama mapping, similar to [PanoramaSkyMaterial](../godot_gdscript_misc.md) textures.

With the projector texture below, the following result is obtained:

> **Tip:** If you've acquired omni projectors in the form of cubemap images, you can use [this web-based conversion tool](https://danilw.github.io/GLSL-howto/cubemap_to_panorama_js/cubemap_to_panorama.html) to convert them to a single panorama image.

### Spot light

Spot lights are similar to omni lights, except they emit light only into a cone (or "cutoff"). They are useful to simulate flashlights, car lights, reflectors, spots, etc. This type of light is also attenuated towards the opposite direction it points to.

Spot lights share the same **Range**, **Attenuation** and **Size** as OmniLight3D, and add two extra parameters:

- **Angle:** The aperture angle of the light.
- **Angle Attenuation:** The cone attenuation, which helps soften the cone borders.

#### Spot shadow mapping

Spots feature the same parameters as omni lights for shadow mapping. Rendering spot shadow maps is significantly faster compared to omni lights, as only one shadow texture needs to be rendered (instead of rendering 6 faces, or 2 in dual paraboloid mode).

Spot lights with shadows enabled can make use of projectors. The projector texture will _multiply_ the light's color by the color at a given point on the texture. As a result, lights will usually appear to be darker once a projector texture is assigned; you can increase **Energy** to compensate for this.

Unlike omni light projectors, a spot light projector texture doesn't need to follow a special format to look correct. It will be mapped in a way similar to a decal.

With the projector texture below, the following result is obtained:

> **Note:** Spot lights with wide angles will have lower-quality shadows than spot lights with narrow angles, as the shadow map is spread over a larger surface. At angles wider than 89 degrees, spot light shadows will stop working entirely. If you need shadows for wider lights, use an omni light instead.

### Shadow atlas

Unlike Directional lights, which have their own shadow texture, omni and spot lights are assigned to slots of a shadow atlas. This atlas can be configured in the advanced Project Settings (**Rendering > Lights And Shadows > Positional Shadow**).

The resolution applies to the whole shadow atlas. This atlas is divided into four quadrants:

Each quadrant can be subdivided to allocate any number of shadow maps; the following is the default subdivision:

The shadow atlas allocates space as follows:

- The biggest shadow map size (when no subdivision is used) represents a light the size of the screen (or bigger).
- Subdivisions (smaller maps) represent shadows for lights that are further away from view and proportionally smaller.

Every frame, the following procedure is performed for all lights:

1. Check if the light is on a slot of the right size. If not, re-render it and move it to a larger/smaller slot.
2. Check if any object affecting the shadow map has changed. If it did, re-render the light.
3. If neither of the above has happened, nothing is done, and the shadow is left untouched.

If the slots in a quadrant are full, lights are pushed back to smaller slots, depending on size and distance. If all slots in all quadrants are full, some lights will not be able to render shadows even if shadows are enabled on them.

The default shadow allocation strategy allows rendering up to 88 lights with shadows enabled in the camera frustum (4 + 4 + 16 + 64):

1. The first and most detailed quadrant can store 4 shadows.
2. The second quadrant can store 4 other shadows.
3. The third quadrant can store 16 shadows, with less detail.
4. The fourth and least detailed quadrant can store 64 shadows, with even less detail.

Using a higher number of shadows per quadrant allows supporting a greater amount of total lights with shadows enabled, while also improving performance (as shadows will be rendered at a lower resolution for each light). However, increasing the number of shadows per quadrant comes at the cost of lower shadow quality.

In some cases, you may want to use a different allocation strategy. For example, in a top-down game where all lights are around the same size, you may want to set all quadrants to have the same subdivision so that all lights have shadows of similar quality level.

### Balancing performance and quality

Shadow rendering is a critical topic in 3D rendering performance. It's important to make the right choices here to avoid creating bottlenecks.

Directional shadow quality settings can be changed at runtime by calling the appropriate [RenderingServer](../godot_gdscript_rendering.md) methods.

Positional (omni/spot) shadow quality settings can be changed at runtime on the root [Viewport](../godot_gdscript_rendering.md).

#### Shadow map size

High shadow resolutions result in sharper shadows, but at a significant performance cost. It should also be noted that _sharper shadows are not always more realistic_. In most cases, this should be kept at its default value of `4096` or decreased to `2048` for low-end GPUs.

If positional shadows become too blurry after decreasing the shadow map size, you can counteract this by adjusting the **shadow atlas** quadrants to contain fewer shadows. This will allow each shadow to be rendered at a higher resolution.

#### Shadow filter mode

Several shadow map quality settings can be chosen here. The default **Soft Low** is a good balance between performance and quality for scenes with detailed textures, as the texture detail will help make the dithering pattern less noticeable.

However, in projects with less detailed textures, the shadow dithering pattern may be more visible. To hide this pattern, you can either enable Temporal antialiasing (TAA), AMD FidelityFX Super Resolution 2.2 (FSR2), Fast approximate antialiasing (FXAA), or increase the shadow filter quality to **Soft Medium** or higher.

The **Soft Very Low** setting will automatically decrease shadow blur to make artifacts from the low sample count less visible. Conversely, the **Soft High** and **Soft Ultra** settings will automatically increase shadow blur to better make use of the increased sample count.

#### 16-bits versus 32-bit

By default, Godot uses 16-bit depth textures for shadow map rendering. This is recommended in most cases as it performs better without a noticeable difference in quality.

If **16 Bits** is disabled, 32-bit depth textures will be used instead. This can result in less artifacting in large scenes and large lights with shadows enabled. However, the difference is often barely visible, yet this can have a significant performance cost.

#### Light/shadow distance fade

OmniLight3D and SpotLight3D offer several properties to hide distant lights. This can improve performance significantly in large scenes with dozens of lights or more.

- **Enabled:** Controls whether distance fade (a form of LOD) is enabled. The light will fade out over **Begin + Length**, after which it will be culled and not sent to the shader at all. Use this to reduce the number of active lights in a scene and thus improve performance.
- **Begin:** The distance from the camera at which the light begins to fade away (in 3D units).
- **Shadow:** The distance from the camera at which the shadow begins to fade away (in 3D units). This can be used to fade out shadows sooner compared to the light, further improving performance. Only available if shadows are enabled for the light.
- **Length:** The distance over which the light and shadow fades (in 3D units). The light becomes slowly more transparent over this distance and is completely invisible at the end. Higher values result in a smoother fade-out transition, which is more suited when the camera moves fast.

#### PCSS recommendations

Percentage-closer soft shadows (PCSS) provide a more realistic shadow mapping appearance, with the penumbra size varying depending on the distance between the caster and the surface receiving the shadow. This comes at a high performance cost, especially for directional lights.

To avoid performance issues, it's recommended to:

- Only use a handful of lights with PCSS shadows enabled at a given time. The effect is generally most visible on large, bright lights. Secondary light sources that are more faint usually don't benefit much from using PCSS shadows.
- Provide a setting for users to disable PCSS shadows. On directional lights, this can be done by setting the DirectionalLight3D's `light_angular_distance` property to `0.0` in a script. On positional lights, this can be done by setting the OmniLight3D or SpotLight3D's `light_size` property to `0.0` in a script.

#### Projector filter mode

The way projectors are rendered also has an impact on performance. The **Rendering > Textures > Light Projectors > Filter** advanced project setting lets you control how projector textures should be filtered. **Nearest/Linear** do not use mipmaps, which makes them faster to render. However, projectors will look grainy at distance. **Nearest/Linear Mipmaps** will look smoother at a distance, but projectors will look blurry when viewed from oblique angles. This can be resolved by using **Nearest/Linear Mipmaps Anisotropic**, which is the highest-quality mode, but also the most expensive.

If your project has a pixel art style, consider setting the filter to one of the **Nearest** values so that projectors use nearest-neighbor filtering. Otherwise, stick to **Linear**.

---

## Mesh level of detail (LOD)

Level of detail (LOD) is one of the most important ways to optimize rendering performance in a 3D project, along with Occlusion culling.

On this page, you'll learn:

- How mesh LOD can improve your 3D project's rendering performance.
- How to set up mesh LOD in Godot.
- How to measure mesh LOD's effectiveness in your project (and alternatives you can explore if it doesn't meet your expectations).

> **See also:** You can see how mesh LOD works in action using the [Occlusion Culling and Mesh LOD demo project](https://github.com/godotengine/godot-demo-projects/tree/master/3d/occlusion_culling_mesh_lod).

### Introduction

Historically, level of detail in 3D games involved manually authoring meshes with lower geometry density, then configuring the distance thresholds at which these lower-detailed meshes should be drawn. This approach is still used today when increased control is needed.

However, in projects that have a large amount of detailed 3D assets, setting up LOD manually can be a very time-consuming process. As a result, automatic mesh decimation and LOD configuration is becoming increasingly popular.

Godot provides a way to automatically generate less detailed meshes for LOD usage on import, then use those LOD meshes when needed automatically. This is completely transparent to the user. The [meshoptimizer](https://meshoptimizer.org/) library is used for LOD mesh generation behind the scenes.

Mesh LOD works with any node that draws 3D meshes. This includes MeshInstance3D, MultiMeshInstance3D, GPUParticles3D and CPUParticles3D.

### Visual comparison

Here is an example of LOD meshes generated on import. Lower detailed meshes will be used when the camera is far away from the object:

Here's the same image with wireframe rendering to make the decimation easier to see:

> **See also:** If you need to manually configure level of detail with artist-created meshes, use Visibility ranges (HLOD) instead of automatic mesh LOD.

### Generating mesh LOD

By default, mesh LOD generation happens automatically for imported 3D scenes (glTF, .blend, Collada, FBX). Once LOD meshes are generated, they will automatically be used when rendering the scene. You don't need to configure anything manually.

However, mesh LOD generation does **not** automatically happen for imported 3D meshes (OBJ). This is because OBJ files are not imported as full 3D scenes by default, but only as individual mesh resources to load into a MeshInstance3D node (or GPUParticles3D, CPUParticles3D, ...).

To make an OBJ file have mesh LOD generated for it, select it in the FileSystem dock, go to the Import dock, change its **Import As** option to **Scene** then click **Reimport**:

This will require restarting the editor after clicking **Reimport**.

> **Note:** The mesh LOD generation process is not perfect, and may occasionally introduce rendering issues (especially in skinned meshes). Mesh LOD generation can also take a while on complex meshes. If mesh LOD causes a specific mesh to look broken, you can disable LOD generation for it in the Import dock. This will also speed up resource importing. This can be done globally in the 3D scene's import options, or on a per-mesh basis using the Advanced Import Settings dialog. See [Importing 3D scenes](tutorials_assets_pipeline.md) for more information.

### Comparing mesh LOD visuals and performance

To disable mesh LOD in the editor for comparison purposes, use the **Disable Mesh LOD** advanced debug draw mode. This can be done using the menu in the top-left corner of the 3D viewport (labeled **Perspective** or **Orthogonal** depending on camera mode):

Enable **View Frame Time** in the same menu to view FPS in the top-right corner. Also enable **View Information** in the same menu to view the number of primitives (vertices + indices) rendered in the bottom-right corner.

If mesh LOD is working correctly in your scene and your camera is far away enough from the mesh, you should notice the number of drawn primitives decreasing and FPS increasing when mesh LOD is left enabled (unless you are CPU-bottlenecked).

To see mesh LOD decimation in action, change the debug draw mode to **Display Wireframe** in the menu specified above, then adjust the **Rendering > Mesh LOD > LOD Change > Threshold Pixels** project setting.

### Configuring mesh LOD performance and quality

You can adjust how aggressive mesh LOD transitions should be in the root viewport by changing the **Rendering > Mesh LOD > LOD Change > Threshold Pixels** project setting. To change this value at runtime, set `mesh_lod_threshold` on the root viewport as follows:

```gdscript
get_tree().root.mesh_lod_threshold = 4.0
```

Each viewport has its own `mesh_lod_threshold` property, which can be set independently from other viewports.

The default mesh LOD threshold of 1 pixel is tuned to look _perceptually_ lossless; it provides a significant performance gain with an unnoticeable loss in quality. Higher values will make LOD transitions happen sooner when the camera moves away, resulting in higher performance, but lower quality.

If you need to perform per-object adjustments to mesh LOD, you can adjust how aggressive LOD transitions should be by adjusting the **LOD Bias** property on any node that inherits from GeometryInstance3D. Values _above_ `1.0` will make LOD transitions happen later than usual (resulting in higher quality, but lower performance). Values _below_ `1.0` will make LOD transitions happen sooner than usual (resulting in lower quality, but higher performance).

Additionally, ReflectionProbe nodes have their own **Mesh LOD Threshold** property that can be adjusted to improve rendering performance when the reflection probe updates. This is especially important for ReflectionProbes that use the **Always** update mode.

> **Note:** When rendering the scene, mesh LOD selection uses a screen-space metric. This means it automatically takes camera field of view and viewport resolution into account. Higher camera FOV and lower viewport resolutions will make LOD selection more aggressive; the engine will display heavily decimated models earlier when the camera moves away. As a result, unlike Visibility ranges (HLOD), you don't need to do anything specific in your project to take camera FOV and viewport resolution into account.

### Using mesh LOD with MultiMesh and particles

For LOD selection, the point of the node's AABB that is the closest to the camera is used as a basis. This applies to any kind of mesh LOD (including for individual MeshInstance3D)s, but this has some implications for nodes that display multiple meshes at once, such as MultiMeshInstance3D, GPUParticles3D and GPUParticles3D. Most importantly, this means that all instances will be drawn with the same LOD level at a given time.

If you are noticing incorrect LOD selection with GPUParticles3D, make sure the node's visibility AABB is configured by selecting the GPUParticles3D node and using **GPUParticles3D > Generate AABB** at the top of the 3D viewport.

If you have instances in a MultiMesh that are far away from each other, they should be placed in a separate MultiMeshInstance3D node. Doing so will also improve rendering performance, as frustum and occlusion culling will be able to cull individual nodes (while they can't cull individual instances in a MultiMesh).

---

## Occlusion culling

In a 3D rendering engine, **occlusion culling** is the process of performing hidden geometry removal.

On this page, you'll learn:

- What are the advantages and pitfalls of occlusion culling.
- How to set up occlusion culling in Godot.
- Troubleshooting common issues with occlusion culling.

> **See also:** You can see how occlusion culling works in action using the [Occlusion Culling and Mesh LOD demo project](https://github.com/godotengine/godot-demo-projects/tree/master/3d/occlusion_culling_mesh_lod).

### Why use occlusion culling

In this example scene with hundreds of rooms stacked next to each other, a dynamic object (red sphere) is hidden behind the wall in the lit room (on the left of the door):

With occlusion culling disabled, all the rooms behind the lit room have to be rendered. The dynamic object also has to be rendered:

With occlusion culling enabled, only the rooms that are actually visible have to be rendered. The dynamic object is also occluded by the wall, and therefore no longer has to be rendered:

Since the engine has less work to do (fewer vertices to render and fewer draw calls), performance will increase as long as there are enough occlusion culling opportunities in the scene. This means occlusion culling is most effective in indoor scenes, preferably with many smaller rooms instead of fewer larger rooms. Combine this with Mesh level of detail (LOD) and Visibility ranges (HLOD) to further improve performance gains.

> **Note:** When using the Forward+ renderer, the engine already performs a _depth prepass_. This consists in rendering a depth-only version of the scene before rendering the scene's actual materials. This is used to ensure each opaque pixel is only shaded once, reducing the cost of overdraw significantly. The greatest performance benefits can be observed when using the Mobile renderer, as it does not feature a depth prepass for performance reasons. As a result, occlusion culling will actively decrease shading overdraw with that renderer. Nonetheless, even when using a depth prepass, there is still a noticeable benefit to occlusion culling in complex 3D scenes. However, in scenes with few occlusion culling opportunities, occlusion culling may not be worth the added setup and CPU usage.

### How occlusion culling works in Godot

> **Note:** "occluder" refers to the shape blocking the view, while "occludee" refers to the object being hidden.

In Godot, occlusion culling works by rasterizing the scene's occluder geometry to a low-resolution buffer on the CPU. This is done using the software raytracing library [Embree](https://github.com/embree/embree).

The engine then uses this low-resolution buffer to test the occludee's AABB against the occluder shapes. The occludee's AABB must be _fully occluded_ by the occluder shape to be culled.

As a result, smaller objects are more likely to be effectively culled than larger objects. Larger occluders (such as walls) also tend to be much more effective than smaller ones (such as decoration props).

### Setting up occlusion culling

The first step to using occlusion culling is to enable the **Rendering > **Occlusion Culling > Use Occlusion Culling** project setting. (Make sure the **Advanced\*\* toggle is enabled in the Project Settings dialog to be able to see it.)

This project setting applies immediately, so you don't need to restart the editor.

After enabling the project setting, you still need to create some occluders. For performance reasons, the engine doesn't automatically use all visible geometry as a basis for occlusion culling. Instead, the engine requires a simplified representation of the scene with only static objects to be baked.

There are two ways to set up occluders in a scene:

#### Automatically baking occluders (recommended)

> **Note:** Only MeshInstance3D nodes are currently taken into account in the _occluder_ baking process. MultiMeshInstance3D, GPUParticles3D, CPUParticles3D and CSG nodes are **not** taken into account when baking occluders. If you wish those to be treated as occluders, you have to manually create occluder shapes that (roughly) match their geometry. Since Godot 4.4, CSG nodes can be taken into account in the baking process if they are converted to a MeshInstance3D before baking occluders. This restriction does not apply to _occludees_. Any node type that inherits from GeometryInstance3D can be occluded.

After enabling the occlusion culling project setting mentioned above, add an OccluderInstance3D node to the scene containing your 3D level.

Select the OccluderInstance3D node, then click **Bake Occluders** at the top of the 3D editor viewport. After baking, the OccluderInstance3D node will contain an Occluder3D resource that stores a simplified version of your level's geometry. This occluder geometry appears as purple wireframe lines in the 3D view (as long as **View Gizmos** is enabled in the **Perspective** menu). This geometry is then used to provide occlusion culling for both static and dynamic occludees.

After baking, you may notice that your dynamic objects (such as the player, enemies, etc…) are included in the baked mesh. To prevent this, set the **Bake > Cull Mask** property on the OccluderInstance3D to exclude certain visual layers from being baked.

For example, you can disable layer 2 on the cull mask, then configure your dynamic objects' MeshInstance3D nodes to be located on the visual layer 2 (instead of layer 1). To do so, select the MeshInstance3D node in question, then on the **VisualInstance3D > Layers** property, uncheck layer 1 then check layer 2. After configuring both cull mask and layers, bake occluders again by following the above process.

#### Manually placing occluders

This approach is more suited for specialized use cases, such as creating occlusion for MultiMeshInstance3D setups or CSG nodes (due to the aforementioned limitation).

After enabling the occlusion culling project setting mentioned above, add an OccluderInstance3D node to the scene containing your 3D level. Select the OccluderInstance3D node, then choose an occluder type to add in the **Occluder** property:

- QuadOccluder3D (a single plane)
- BoxOccluder3D (a cuboid)
- SphereOccluder3D (a sphere-shaped occluder)
- PolygonOccluder3D (a 2D polygon with as many points as you want)

There is also ArrayOccluder3D, whose points can't be modified in the editor but can be useful for procedural generation from a script.

### Previewing occlusion culling

You can enable a debug draw mode to preview what the occlusion culling is actually "seeing". In the top-left corner of the 3D editor viewport, click the **Perspective** button (or **Orthogonal** depending on your current camera mode), then choose **Display Advanced… > Occlusion Culling Buffer**. This will display the low-resolution buffer that is used by the engine for occlusion culling.

In the same menu, you can also enable **View Information** and **View Frame Time** to view the number of draw calls and rendered primitives (vertices + indices) in the bottom-right corner, along with the number of frames per second rendered in the top-right corner.

If you toggle occlusion culling in the project settings while this information is displayed, you can see how much occlusion culling improves performance in your scene. Note that the performance benefit highly depends on the 3D editor camera's view angle, as occlusion culling is only effective if there are occluders in front of the camera.

To toggle occlusion culling at runtime, set `use_occlusion_culling` on the root viewport as follows:

```gdscript
get_tree().root.use_occlusion_culling = true
```

Toggling occlusion culling at runtime is useful to compare performance on a running project.

### Performance considerations

#### Design your levels to take advantage of occlusion culling

**This is the most important guideline.** A good level design is not just about what the gameplay demands; it should also be built with occlusion in mind.

For indoor environments, add opaque walls to "break" the line of sight at regular intervals and ensure not too much of the scene can be seen at once.

For large open scenes, use a pyramid-like structure for the terrain's elevation when possible. This provides the greatest culling opportunities compared to any other terrain shape.

#### Avoid moving OccluderInstance3D nodes during gameplay

This includes moving the parents of OccluderInstance3D nodes, as this will cause the nodes themselves to move in global space, therefore requiring the BVH to be rebuilt.

Toggling an OccluderInstance3D's visibility (or one of its parents' visibility) is not as expensive, as the update only needs to happen once (rather than continuously).

For example, if you have a sliding or rotating door, you can make the OccluderInstance3D node not be a child of the door itself (so that the occluder never moves), but you can hide the OccluderInstance3D visibility once the door starts opening. You can then reshow the OccluderInstance3D once the door is fully closed.

If you absolutely have to move an OccluderInstance3D node during gameplay, use a primitive Occluder3D shape for it instead of a complex baked shape.

#### Use the simplest possible occluder shapes

If you notice low performance or stuttering in complex 3D scenes, it may mean that the CPU is overloaded as a result of rendering detailed occluders. Select the OccluderInstance3D node, increase the **Bake > Simplification** property then bake occluders again.

Remember to keep the simplification value reasonable. Values that are too high for the level's geometry may cause incorrect occlusion culling to occur, as in **My occludee is being culled when it shouldn't be**.

If this still doesn't lead to low enough CPU usage, you can try adjusting the **Rendering > Occlusion Culling > BVH Build Quality** project setting and/or decreasing **Rendering > Occlusion Culling > Occlusion Rays Per Thread**. You'll need to enable the **Advanced** toggle in the Project Settings dialog to see those settings.

### Troubleshooting

#### My occludee isn't being culled when it should be

**On the occluder side:**

First, double-check that the **Bake > Cull Mask** property in the OccluderInstance3D is set to allow baking the meshes you'd like. The visibility layer of the MeshInstance3D nodes must be present within the cull mask for the mesh to be included in the bake.

Also note that occluder baking only takes meshes with _opaque_ materials into account. Surfaces will _transparent_ materials will **not** be included in the bake, even if the texture applied on them is fully opaque.

Lastly, remember that MultiMeshInstance3D, GPUParticles3D, CPUParticles3D and CSG nodes are **not** taken into account when baking occluders. As a workaround, you can add OccluderInstance3D nodes for those manually.

**On the occludee side:**

Make sure **Extra Cull Margin** is set as low as possible (it should usually be `0.0`), and that **Ignore Occlusion Culling** is disabled in the object's GeometryInstance3D section.

Also, check the AABB's size (which is represented by an orange box when selecting the node). This axis-aligned bounding box must be _fully_ occluded by the occluder shapes for the occludee to be hidden.

#### My occludee is being culled when it shouldn't be

The most likely cause for this is that objects that were included in the occluder bake have been moved after baking occluders. For instance, this can occur when moving your level geometry around or rearranging its layout. To fix this, select the OccluderInstance3D node and bake occluders again.

This can also happen because dynamic objects were included in the bake, even though they shouldn't be. Use the **occlusion culling debug draw mode** to look for occluder shapes that shouldn't be present, then **adjust the bake cull mask accordingly**.

The last possible cause for this is overly aggressive mesh simplification during the occluder baking process. Select the OccluderInstance3D node, decrease the **Bake > Simplification** property then bake occluders again.

As a last resort, you can enable the **Ignore Occlusion Culling** property on the occludee. This will negate the performance improvements of occlusion culling for that object, but it makes sense to do this for objects that will never be culled (such as a first-person view model).

---

## 3D Particle attractors

Particle attractors are nodes that apply a force to all particles within their reach. They pull particles closer or push them away based on the direction of that force. There are three types of attractors: [GPUParticlesAttractorBox3D](../godot_gdscript_misc.md), [GPUParticlesAttractorSphere3D](../godot_gdscript_misc.md), and [GPUParticlesAttractorVectorField3D](../godot_gdscript_misc.md). You can instantiate them at runtime and change their properties from gameplay code; you can even animate and combine them for complex attraction effects.

> **Note:** Particle attractors are not yet implemented for 2D particle systems.

The first thing you have to do if you want to use attractors is enable the `Attractor Interaction` property on the ParticleProcessMaterial. Do this for every particle system that needs to react to attractors. Like most properties in Godot, you can also change this at runtime.

### Common properties

There are some properties that you can find on all attractors. They're located in the `GPUParticlesAttractor3D` section in the inspector.

`Strength` controls how strong the attractor force is. A positive value pulls particles closer to the attractor's center, while a negative value pushes them away.

`Attenuation` controls the strength falloff within the attractor's influence region. Every particle attractor has a boundary. Its strength is weakest at the border of this boundary and strongest at its center. Particles outside of the boundary are not affected by the attractor at all. The attenuation curve controls how the strength weakens over that distance. A straight line means that the strength is proportional to the distance: if a particle is halfway between the boundary and the center, the attractor strength will be half of what it is at the center. Different curve shapes change how fast particles accelerate towards the attractor.

The `Directionality` property changes the direction towards which particles are pulled. At a value of `0.0`, there is no directionality, which means that particles are pulled towards the attractor's center. At `1.0`, the attractor is fully directional, which means particles will be pulled along the attractor's local `-Z`-axis. You can change the global direction by rotating the attractor. If `Strength` is negative, particles are instead pulled along the `+Z`-axis.

The `Cull Mask` property controls which particle systems are affected by an attractor based on each system's [visibility layers](../godot_gdscript_misc.md). A particle system is only affected by an attractor if at least one of the system's visibility layers is enabled in the attractor's cull mask.

### Box attractors

Box attractors have a box-shaped influence region. You control their size with the `Extents` property. Box extents always measure half of the sides of its bounds, so a value of `(X=1.0,Y=1.0,Z=1.0)` creates a box with an influence region that is 2 meters wide on each side.

To create a box attractor, add a new child node to your scene and select `GPUParticlesAttractorBox3D` from the list of available nodes. You can animate the box position or attach it to a moving node for more dynamic effects.

### Sphere attractors

Sphere attractors have a spherical influence region. You control their size with the `Radius` property. While box attractors don't have to be perfect cubes, sphere attractors will always be spheres: You can't set width independently from height. If you want to use a sphere attractor for elongated shapes, you have to change its `Scale` in the attractor's `Node3D` section.

To create a sphere attractor, add a new child node to your scene and select `GPUParticlesAttractorSphere3D` from the list of available nodes. You can animate the sphere position or attach it to a moving node for more dynamic effects.

### Vector field attractors

A vector field is a 3D area that contains vectors positioned on a grid. The grid density controls how many vectors there are and how far they're spread apart. Each vector in a vector field points in a specific direction. This can be completely random or aligned in a way that forms distinct patterns and paths.

When particles interact with a vector field, their movement direction changes to match the nearest vector in the field. As a particle moves closer to the next vector in the field, it changes direction to match that vector's direction. The particle's speed depends on the vector's length.

Like box attractors, vector field attractors have a box-shaped influence region. You control their size with the `Extents` property, where a value of `(X=1.0,Y=1.0,Z=1.0)` creates a box with an influence region that is 2 meters wide on each side. The `Texture` property takes a [3D texture](../godot_gdscript_misc.md) where every pixel represents a vector with the pixel's color interpreted as the vector's direction and size.

> **Note:** When a texture is used as a vector field, there are two types of conversion you need to be aware of: 1. The texture coordinates map to the attractor bounds. The image below shows which part of the texture corresponds to which part of the vector field volume. For example, the bottom half of the texture affects the top half of the vector field attractor because `+Y` points down in the texture UV space, but up in Godot's world space. 2. The pixel color values map to direction vectors in space. The image below provides an overview. Since particles can move in two directions along each axis, the lower half of the color range represents negative direction values while the upper half represents positive direction values. So a yellow pixel `(R=1,G=1,B=0)` maps to the vector `(X=1,Y=1,Z=-1)` while a neutral gray `(R=0.5,G=0.5,B=0.5)` results in no movement at all.

To create a vector field attractor, add a new child node to your scene and select `GPUParticlesAttractorVectorField3D` from the list of available nodes. You can animate the attractor's position or attach it to a moving node for more dynamic effects.

> **Tip:** If you don't have external tools to create vector field textures, you can use a NoiseTexture3D with a Color Ramp attached as a vector field texture. The Color Ramp can be modified to adjust how much each coordinate is affected by the vector field.

---
