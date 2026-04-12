# Godot 4 C# Tutorials — 3D (Part 3)

> 3 tutorials. C#-specific code examples.

## Introduction to global illumination

### What is global illumination?

_Global illumination_ is a catch-all term used to describe a system of lighting that uses both direct light (light that comes directly from a light source) and indirect light (light that bounces from a surface). In a 3D rendering engine, global illumination is one of the most important elements to achieving realistic lighting. Global illumination aims to mimic how light behaves in real life, such as light bouncing on surfaces and light being emitted from emissive materials.

In the example below, the entire scene is illuminated by an emissive material (the white square at the top). The white wall and ceiling on the back is tinted red and green close to the walls, as the light bouncing on the colored walls is being reflected back onto the rest of the scene.

Global illumination is composed of several key concepts:

#### Indirect diffuse lighting

This is the lighting that does not change depending on the camera's angle. There are two main sources of indirect diffuse lighting:

- Light _bouncing_ on surfaces. This bounced lighting is multiplied with the material's albedo color. The bounced lighting can then be reflected by other surfaces, with decreasing impact due to light attenuation. In real life, light bounces an infinite number of times. However, for performance reasons, this can't be simulated in a game engine. Instead, the number of bounces is typically limited to 1 or 2 (or up to 16 when baking lightmaps). A greater number of bounces will lead to more realistic light falloff in shaded areas, at the cost of lower performance or greater bake times.
- Emissive materials can also emit light that can be bounced on surfaces. This acts as a form of _area lighting_. Instead of having an infinitely small point emit light using an OmniLight3D or SpotLight3D node, an area of a determined size will emit light using its own surface.

Direct diffuse lighting is already handled by the light nodes themselves, which means that global illumination algorithms only try to represent indirect lighting.

Different global illumination techniques offer varying levels of accuracy to represent indirect diffuse lighting. See the comparison table at the bottom of this page for more information.

To provide more accurate ambient occlusion for small objects, screen-space ambient occlusion (SSAO) can be enabled in the environment settings. SSAO has a significant performance cost, so make sure to disable it when targeting low-end hardware.

> **Note:** Indirect diffuse lighting may be a source of color banding in scenes with no detailed textures. This results in light gradients not being smooth, but having a visible "stepping" effect instead. See the Color banding section in the 3D rendering limitations documentation for ways to reduce this effect.

#### Specular lighting

Specular lighting is also referred to as _reflections_. This is the lighting that changes in intensity depending on the camera's angle. This specular lighting can be _direct_ or _indirect_.

Most global illumination techniques offer a way to render specular lighting. However, the degree of accuracy at which specular lighting is rendered varies greatly from technique to technique. See the comparison table at the bottom of this page for more information.

To provide more accurate reflections for small objects, screen-space reflections (SSR) can be enabled in the environment settings. SSR has a significant performance cost (even more so than SSAO), so make sure to disable it when targeting low-end hardware.

### Which global illumination technique should I use?

When determining a global illumination (GI) technique to use, there are several criteria to keep in mind:

- **Performance.** Real-time GI techniques are usually more expensive compared to semi-real-time or baked techniques. Note that most of the cost in GI rendering is spent on the GPU, rather than the CPU.
- **Visuals.** On top of not performing the best, real-time GI techniques generally don't provide the best visual output. This is especially the case in a mostly static scene where the dynamic nature of real-time GI is not easily noticeable. If maximizing visual quality is your goal, baked techniques will often look better and will result in fewer light leaks.
- **Real-time ability.** Some GI techniques are fully real-time, whereas others are only semi-real-time or aren't real-time at all. Semi-real-time techniques have restrictions that fully real-time techniques don't. For instance, dynamic objects may not contribute emissive lighting to the scene. Non-real-time techniques do not support _any_ form of dynamic GI, so it must be faked using other techniques if needed (such as placing positional lights near emissive surfaces). Real-time ability also affects the GI technique's viability in procedurally generated levels.
- **User work needed.** Some GI techniques are fully automatic, whereas others require careful planning and manual work on the user's side. Depending on your time budget, some GI techniques may be preferable to others.

Here's a comparison of all the global illumination techniques available in Godot:

#### Performance

In order of performance from fastest to slowest:

- **ReflectionProbe:**

- ReflectionProbes with their update mode set to **Always** are much more expensive than probes with their update mode set to **Once** (the default). Suited for integrated graphics when using the **Once** update mode. _Available in all renderers._
- **LightmapGI:**

- Lights can be baked with indirect lighting only, or fully baked on a per-light basis to further improve performance. Hybrid setups can be used (such as having a real-time directional light and fully baked positional lights). Directional information can be enabled before baking to improve visuals at a small performance cost (and at the cost of larger file sizes). Suited for integrated graphics. _Available in all renderers. However, baking lightmaps requires hardware with RenderingDevice support._
- **VoxelGI:**

- The bake's number of subdivisions can be adjusted to balance between performance and quality. The VoxelGI rendering quality can be adjusted in the Project Settings. The rendering can optionally be performed at half resolution (and then linearly scaled) to improve performance significantly. **Not available** _when using the Mobile or Compatibility renderers._
- **Screen-space indirect lighting (SSIL):**

- The SSIL quality and number of blur passes can be adjusted in the Project Settings. By default, SSIL rendering is performed at half resolution (and then linearly scaled) to ensure a reasonable performance level. **Not available** _when using the Mobile or Compatibility renderers._
- **SDFGI:**

- The number of cascades can be adjusted to balance performance and quality. The number of rays thrown per frame can be adjusted in the Project Settings. The rendering can optionally be performed at half resolution (and then linearly scaled) to improve performance significantly. **Not available** _when using the Mobile or Compatibility renderers._

#### Visuals

For comparison, here's a 3D scene with no global illumination options used:

Here's how Godot's various global illumination techniques compare:

- **VoxelGI:** Good reflections and indirect lighting, but beware of leaks.

- Due to its voxel-based nature, VoxelGI will exhibit light leaks if walls and floors are too thin. It's recommended to make sure all solid surfaces are at least as thick as one voxel.

Streaking artifacts may also be visible on sloped surfaces. In this case, tweaking the bias properties or rotating the VoxelGI node can help combat this.

- **SDFGI:** Good reflections and indirect lighting, but beware of leaks and visible cascade shifts.

- GI level of detail varies depending on the distance between the camera and surface.

Leaks can be reduced significantly by enabling the **Use Occlusion** property. This has a small performance cost, but it often results in fewer leaks compared to VoxelGI.

Cascade shifts may be visible when the camera moves fast. This can be made less noticeable by adjusting the cascade sizes or using fog.

- **Screen-space indirect lighting (SSIL):** Good _secondary_ source of indirect lighting, but no reflections.

- SSIL is designed to be used as a complement to another GI technique such as VoxelGI, SDFGI or LightmapGI. SSIL works best for small-scale details, as it cannot provide accurate indirect lighting for large structures on its own. SSIL can provide real-time indirect lighting in situations where other GI techniques fail to capture small-scale details or dynamic objects. Its screen-space nature will result in some artifacts, especially when objects enter and leave the screen. SSIL works using the last frame's color (before post-processing) which means that emissive decals and custom shaders are included (as long as they're present on screen).
- **LightmapGI:** Excellent indirect lighting, decent reflections (optional).

- This is the only technique where the number of light bounces can be pushed above 2 (up to 16). When directional information is enabled, spherical harmonics (SH) are used to provide blurry reflections.
- **ReflectionProbe:** Good reflections, but poor indirect lighting.

- Indirect lighting can be disabled, set to a constant color spread throughout the probe, or automatically read from the probe's environment (and applied as a cubemap). This essentially acts as local ambient lighting. Reflections and indirect lighting are blended with other nearby probes.

#### Real-time ability

- **VoxelGI:** Fully real-time.

- Indirect lighting and reflections are fully real-time. Dynamic objects can receive GI _and_ contribute to it with their emissive surfaces. Custom shaders can also emit their own light, which will be emitted accurately.

Viable for procedurally generated levels _if they are generated in advance_ (and not during gameplay). Baking requires several seconds or more to complete, but it can be done from both the editor and an exported project.

- **SDFGI:** Semi-real-time.

- Cascades are generated in real-time, making SDFGI viable for procedurally generated levels (including when structures are generated during gameplay).

Dynamic objects can _receive_ GI, but not _contribute_ to it. Emissive lighting will only update when an object enters a cascade, so it may still work for slow-moving objects.

- **Screen-space indirect lighting (SSIL):** Fully real-time.

- SSIL works with both static and dynamic lights. It also works with both static and dynamic occluders (including emissive materials).
- **LightmapGI:** Baked, and therefore not real-time.

- Both indirect lighting and SH reflections are baked and can't be changed at runtime. Real-time GI must be simulated via other means, such as real-time positional lights. Dynamic objects receive indirect lighting via light probes, which can be placed automatically or manually by the user (LightmapProbe node). Not viable for procedurally generated levels, as baking lightmaps is only possible from the editor.
- **ReflectionProbe:** Optionally real-time.

- By default, reflections update when the probe is moved. They update as often as possible if the update mode is set to **Always** (which is expensive).
- Indirect lighting must be configured manually by the user, but can be changed at runtime without causing an expensive computation to happen behind the scenes. This makes ReflectionProbes viable for procedurally generated levels.

#### User work needed

- **VoxelGI:** One or more VoxelGI nodes need to be created and baked.

- Adjusting extents correctly is required to get good results. Additionally rotating the node and baking again can help combat leaks or streaking artifacts in certain situations. Bake times are fast – usually below 10 seconds for a scene of medium complexity.
- **SDFGI:** Very little.

- SDFGI is fully automatic; it only needs to be enabled in the Environment resource. The only manual work required is to set MeshInstances' bake mode property correctly. No node needs to be created, and no baking is required.
- **Screen-space indirect lighting (SSIL):** Very little.

- SSIL is fully automatic; it only needs to be enabled in the Environment resource. No node needs to be created, and no baking is required.
- **LightmapGI:** Requires UV2 setup and baking.

- Static meshes must be reimported with UV2 and lightmap generation enabled. On a dedicated GPU, bake times are relatively fast thanks to the GPU-based lightmap baking – usually below 1 minute for a scene of medium complexity.
- **ReflectionProbe:** Placed manually by the user.

#### Summary

If you are unsure about which GI technique to use:

- For desktop games, it's a good idea to start with SDFGI first as it requires the least amount of setup. Move to other GI techniques later if needed. To improve performance on low-end GPUs and integrated graphics, consider adding an option to disable SDFGI or VoxelGI in your game's settings. SDFGI can be disabled in the Environment resource, and VoxelGI can be disabled by hiding the VoxelGI node(s). To further improve visuals on high-end setups, add an option to enable SSIL in your game's settings.
- For mobile games, LightmapGI and ReflectionProbes are the only supported options. See also **Alternatives to GI techniques**.

> **See also:** You can compare global illumination techniques in action using the [Global Illumination demo project](https://github.com/godotengine/godot-demo-projects/tree/master/3d/global_illumination).

#### Which global illumination mode should I use on meshes and lights?

Regardless of which global illumination technique you use, there is no universally "better" global illumination mode. Still, here are some recommendations for meshes:

- For static level geometry, use the **Static** global illumination mode _(default)_.
- For small dynamic geometry and players/enemies, use the **Disabled** global illumination mode. Small dynamic geometry will not be able to contribute a significant amount of indirect lighting, due to the geometry being smaller than a voxel. If you need indirect lighting for small dynamic objects, it can be simulated using an OmniLight3D or SpotLight3D node parented to the object.
- For _large_ dynamic level geometry (such as a moving train), use the **Dynamic** global illumination mode. Note that this only has an effect with VoxelGI, as SDFGI and LightmapGI do not support global illumination with dynamic objects.

Here are some recommendations for light bake modes:

- For static level lighting, use the **Static** bake mode. The **Static** mode is also suitable for dynamic lights that don't change much during gameplay, such as a flickering torch.
- For short-lived dynamic effects (such as a weapon), use the **Disabled** bake mode to improve performance.
- For long-lived dynamic effects (such as a rotating alarm light), use the **Dynamic** bake mode to improve quality _(default)_. Note that this only has an effect with VoxelGI and SDFGI, as LightmapGI does not support global illumination with dynamic lights.

### Alternatives to GI techniques

If none of the GI techniques mentioned above fits, it's still possible to simulate GI by placing additional lights manually. This requires more manual work, but it can offer good performance _and_ good visuals if done right. This approach is still used in many modern games to this day.

When targeting low-end hardware in situations where using LightmapGI is not viable (such as procedurally generated levels), relying on environment lighting alone or a constant ambient light factor may be a necessity. This may result in flatter visuals, but adjusting the ambient light color and sky contribution still makes it possible to achieve acceptable results in most cases.

---

## Reflection probes

As stated in the Standard Material 3D and ORM Material 3D, objects can show reflected and/or diffuse light. Reflection probes are used as a source of reflected _and_ ambient light for objects inside their area of influence. They can be used to provide more accurate reflections than VoxelGI and SDFGI while being fairly cheap on system resources.

Since reflection probes can also store ambient light, they can be used as a low-end alternative to VoxelGI and SDFGI when baked lightmaps aren't viable (e.g. in procedurally generated levels).

Reflection probes can also be used at the same time as screen-space reflections to provide reflections for off-screen objects. In this case, Godot will blend together the screen-space reflections and reflections from reflection probes.

> **See also:** Not sure if ReflectionProbe is suited to your needs? See Which global illumination technique should I use? for a comparison of GI techniques available in Godot 4.

### Visual comparison

By combining reflection probes with screen-space reflections, you can get the best of both worlds: high-quality reflections for general room structure (that remain present when off-screen), while also having real-time reflections for small details.

### Setting up a ReflectionProbe

- Add a [ReflectionProbe](../godot_csharp_nodes_3d.md) node.
- Configure the ReflectionProbe's extents in the inspector to fit your scene. To get reasonably accurate reflections, you should generally have one ReflectionProbe node per room (sometimes more for large rooms).

> **Tip:** Remember that ReflectionProbe extents don't have to be square, and you can even rotate the ReflectionProbe node to fit rooms that aren't aligned with the X/Z grid. Use this to your advantage to better cover rooms without having to place too many ReflectionProbe nodes.

### ReflectionProbe properties

- **Update Mode:** Controls when the reflection probe updates. **Once** only renders the scene once every time the ReflectionProbe is moved. This makes it much faster to render compared to the **Always** update mode, which forces the probe to re-render everything around it every frame. Leave this property on **Once** (default) unless you need the reflection probe to update every frame.
- **Intensity:** The brightness of the reflections and ambient lighting. This usually doesn't need to be changed from its default value of `1.0`, but you can decrease it `1.0` if you find that reflections look too strong.
- **Max Distance:** Controls the maximum distance used by the ReflectionProbe's internal camera. The distance is always at least equal to the **Extents**, but this can be increased to make objects located outside the extents visible in reflections. _This property does not affect the maximum distance at which the ReflectionProbe itself is visible._
- **Extents:** The area that will be affected by the ReflectionProbe's lighting and reflections.
- **Origin Offset:** The origin to use for the internal camera used for reflection probe rendering. This must always be constrained within the **Extents**. If needed, adjust this to prevent the reflection from being obstructed by a solid object located exactly at the center of the ReflectionProbe.
- **Box Projection:** Controls whether parallax correction should be used when rendering the reflection probe. This adjusts the reflection's appearance depending on the camera's position (relative to the reflection probe). This has a small performance cost, but the quality increase is often worth it in box-shaped rooms. Note that this effect doesn't work quite as well in rooms with less regular shapes (such as ellipse-shaped rooms).
- **Interior:** If enabled, ambient lighting will not be sourced from the environment sky, and the background sky won't be rendered onto the reflection probe.
- **Enable Shadows:** Controls whether real-time light shadows should be rendered within the reflection probe. Enable this to improve reflection quality at the cost of performance. This should be left disabled for reflection probes with the **Always** mode, as it's very expensive to render reflections with shadows every frame. Fully baked light shadows are not affected by this setting and will be rendered in the reflection probe regardless.
- **Cull Mask:** Controls which objects are visible in the reflection. This can be used to improve performance by excluding small objects from the reflection. This can also be used to prevent an object from having self-reflection artifacts in situations where **Origin Offset** can't be used.
- **Mesh LOD Threshold:** The automatic level of detail threshold to use for rendering meshes within the reflection. This only affects meshes that have automatic LODs generated for them. Higher values can improve performance by using less detailed geometry, especially for objects that are far away from the reflection's origin. The visual difference of using less detailed objects is usually not very noticeable during gameplay, especially in rough reflections.

The Ambient category features several properties to adjust ambient lighting rendered by the ReflectionProbe:

- **Mode:** If set to **Disabled**, no ambient light is added by the probe. If set to **Environment**, the ambient light color is automatically sampled from the environment sky (if **Interior** is disabled) and the reflection's average color. If set to **Constant Color**, the color specified in the **Color** property is used instead. The **Constant Color** mode can be used as an approximation of area lighting.
- **Color:** The color to use when the ambient light mode is set to **Constant Mode**.
- **Color Energy:** The multiplier to use for the ambient light custom **Color**. This only has an effect when the ambient light mode is **Custom Color**.

### ReflectionProbe blending

To make transitions between reflection sources smoother, Godot supports automatic probe blending:

- Up to 4 ReflectionProbes can be blended together at a given location. A ReflectionProbe will also fade out smoothly back to environment lighting when it isn't touching any other ReflectionProbe node.
- SDFGI and VoxelGI will blend in smoothly with ReflectionProbes if used. This allows placing ReflectionProbes strategically to get more accurate (or fully real-time) reflections where needed, while still having rough reflections available in the VoxelGI or SDFGI's area of influence.

To make several ReflectionProbes blend with each other, you need to have part of each ReflectionProbe overlap each other's area. The extents should only overlap as little possible with other reflection probes to improve rendering performance (typically a few units in 3D space).

### Limitations

When using the Forward+ renderer, Godot uses a _clustering_ approach for reflection probe rendering. As many reflection probes as desired can be added (as long as performance allows). However, there's still a default limit of 512 _clustered elements_ that can be present in the current camera view. A clustered element is an omni light, a spot light, a decal or a **reflection probe**. This limit can be increased by adjusting [Max Clustered Elements](../godot_csharp_misc.md) in **Project Settings > Rendering > Limits > Cluster Builder**.

When using the Mobile renderer, only 8 reflection probes can be applied on each individual Mesh _resource_. If there are more reflection probes affecting a single mesh, not all of them will be rendered on the mesh.

Similarly, when using the Compatibility renderer, up to 2 reflection probes can be applied per mesh. If more than 2 reflection probes affect a single mesh, additional probes will not be rendered.

---

## Using Lightmap global illumination

Baked lightmaps are a workflow for adding indirect (or fully baked) lighting to a scene. Unlike the VoxelGI and SDFGI approaches, baked lightmaps work fine on low-end PCs and mobile devices, as they consume almost no resources at runtime. Also unlike VoxelGI and SDFGI, baked lightmaps can optionally be used to store direct lighting, which provides even further performance gains.

Unlike VoxelGI and SDFGI, baked lightmaps are completely static. Once baked, they can't be modified at all. They also don't provide the scene with reflections, so using Reflection probes together with it on interiors (or using a Sky on exteriors) is a requirement to get good quality.

As they are baked, they have fewer problems than VoxelGI and SDFGI regarding light bleeding, and indirect light will often look better. The downside is that baking lightmaps takes longer compared to baking VoxelGI. While baking VoxelGI can be done in a matter of seconds, baking lightmaps can take several minutes if not more. This can slow down iteration speed significantly, so it is recommended to bake lightmaps only when you actually need to see changes in lighting. Lightmaps are baked on the GPU, making light baking faster if you have a mid-range or high-end dedicated GPU.

Baking lightmaps will also reserve baked materials' UV2 slot, which means you can no longer use it for other purposes in materials (either in the built-in Standard Material 3D and ORM Material 3D or in custom shaders).

Despite their lack of flexibility, baked lightmaps typically offer both the best quality _and_ performance at the same time in (mostly) static scenes. This makes lightmaps still popular in game development, despite lightmaps being the oldest technique for global illumination in video games.

> **See also:** Not sure if LightmapGI is suited to your needs? See Which global illumination technique should I use? for a comparison of GI techniques available in Godot 4.

### Visual comparison

Here are some comparisons of how LightmapGI vs. VoxelGI look. Notice that lightmaps are more accurate, but also suffer from the fact that lighting is on an unwrapped texture, so transitions and resolution may not be that good. VoxelGI looks less accurate (as it's an approximation), but smoother overall.

SDFGI is also less accurate compared to LightmapGI. However, SDFGI can support large open worlds without any need for baking.

### Setting up

> **Warning:** Baking lightmaps in the web editors is not supported due to graphics API limitations. On the web platform, only _rendering_ lightmaps that were baked on a different platform is supported.

> **Note:** The LightmapGI node only bakes nodes that are on the same level as the LightmapGI node (siblings), or nodes that are children of the LightmapGI node. This allows you to use several LightmapGI nodes to bake different parts of the scene, independently from each other.

First of all, before the lightmapper can do anything, the objects to be baked need a UV2 layer and a texture size. A UV2 layer is a set of secondary texture coordinates that ensures any face in the object has its own place in the UV map. Faces must not share pixels in the texture.

There are a few ways to ensure your object has a unique UV2 layer and texture size:

#### Unwrap on scene import (recommended)

In most scenarios, this is the best approach to use. The only downside is that, on large models, unwrapping can take a while on import. Nonetheless, Godot will cache the UV2 across reimports, so it will only be regenerated when needed.

Select the imported scene in the filesystem dock, then go to the **Import** dock. There, the following option can be modified:

The **Meshes > Light Baking** option must be set to **Static Lightmaps (VoxelGI/SDFGI/LightmapGI)**:

When unwrapping on import, you can adjust the texture size using the **Meshes > Lightmap Texel Size** option. _Lower_ values will result in more detailed lightmaps, possibly resulting in higher visual quality at the cost of longer bake times and larger lightmap file sizes. The default value of `0.2` is suited for small/medium-sized scenes, but you may want to increase it to `0.5` or even more for larger scenes. This is especially the case if you're baking indirect lighting only, as indirect light is low-frequency data (which means it doesn't need high-resolution textures to be accurately represented).

The effect of setting this option is that all meshes within the scene will have their UV2 maps properly generated.

> **Warning:** When reusing a mesh within a scene, keep in mind that UVs will be generated for the first instance found. If the mesh is re-used with different scales (and the scales are wildly different, more than half or twice), this will result in inefficient lightmaps. To avoid this, adjust the **Lightmap Scale** property in the GeometryInstance3D section of a MeshInstance3D node. This lets you _increase_ the level of lightmap detail for specific MeshInstance3D nodes (but not decrease it). Also, the `*.unwrap_cache` files should _not_ be ignored in version control as these files guarantee that UV2 reimports are consistent across platforms and engine versions.

#### Unwrap from within Godot

> **Warning:** If this Mesh menu operation is used on an imported 3D scene, the generated UV2 will be lost when the scene is reloaded.

Godot has an option to unwrap meshes and visualize the UV channels. After selecting a MeshInstance3D node, it can be found in the **Mesh** menu at the top of the 3D editor viewport:

This will generate a second set of UV2 coordinates which can be used for baking. It will also set the texture size automatically.

#### Unwrap from your 3D modeling software

The last option is to do it from your favorite 3D app. This approach is generally **not recommended**, but it's explained so that you know it exists. The main advantage is that, on complex objects that you may want to re-import a lot, the texture generation process can be quite costly within Godot, so having it unwrapped before import can be faster.

Simply do an unwrap on the second UV2 layer.

Then import the 3D scene normally. Remember you will need to set the texture size on the mesh after import.

If you use external meshes on import, the size will be kept. Be wary that most unwrappers in 3D modeling software are not quality-oriented, as they are meant to work quickly. You will mostly need to use seams or other techniques to create better unwrapping.

#### Generating UV2 for primitive meshes

> **Note:** This option is only available for primitive meshes such as [BoxMesh](../godot_csharp_rendering.md), [CylinderMesh](../godot_csharp_rendering.md), [PlaneMesh](../godot_csharp_rendering.md), etc.

Enabling UV2 on primitive meshes allows you to make them receive and contribute to baked lighting. This can be used in certain lighting setups. For instance, you could hide a torus that has an emissive material after baking lightmaps to create an area light that follows the shape of a torus.

By default, primitive meshes do not have UV2 generated to save resources (as these meshes may be created during gameplay). You can edit a primitive mesh in the inspector and enable **Add UV2** to make the engine procedurally generate UV2 for a primitive mesh. The default **UV2 Padding** value is tuned to avoid most lightmap bleeding, without wasting too much space on the edges. If you notice lightmap bleeding on a specific primitive mesh only, you may have to increase **UV2 Padding**.

**Lightmap Size Hint** represents the size taken by a single mesh on the lightmap texture, which varies depending on the mesh's size properties and the **UV2 Padding** value. **Lightmap Size Hint** should not be manually changed, as any modifications will be lost when the scene is reloaded.

#### Generating UV2 for CSG nodes

Since Godot 4.4, you can convert a CSG node and its children to a MeshInstance3D. This can be used to bake lightmaps on a CSG node by following these steps:

- Select the root CSG node and choose **CSG > Bake Mesh Instance** at the top of the 3D editor viewport.
- Hide the root CSG node that was just baked (it is not hidden automatically).
- Select the newly created MeshInstance3D node and choose **Mesh > Unwrap UV2 for Lightmap/AO**.
- Bake lightmaps.

> **Tip:** Remember to keep the original CSG node in the scene tree, so that you can perform changes to the geometry later if needed. To make changes to the geometry, remove the MeshInstance3D node and make the root CSG node visible again.

#### Checking UV2

In the **Mesh** menu mentioned before, the UV2 texture coordinates can be visualized. If something is failing, double-check that the meshes have these UV2 coordinates:

### Setting up the scene

Before anything is done, a **LightmapGI** node needs to be added to a scene. This will enable light baking on all nodes (and sub-nodes) in that scene, even on instanced scenes.

A sub-scene can be instanced several times, as this is supported by the baker. Each instance will be assigned a lightmap of its own. To avoid issues with inconsistent lightmap texel scaling, make sure to respect the rule about mesh scaling mentioned before.

#### Setting up meshes

For a **MeshInstance3D** node to take part in the baking process, it needs to have its bake mode set to **Static**. Meshes that have their bake mode set to **Disabled** or **Dynamic** will be ignored by the lightmapper.

When auto-generating lightmaps on scene import, this is enabled automatically.

#### Setting up lights

Lights are baked with indirect light only by default. This means that shadowmapping and lighting are still dynamic and affect moving objects, but light bounces from that light will be baked.

Lights can be disabled (no bake) or be fully baked (direct and indirect). This can be controlled from the **Bake Mode** menu in lights:

The modes are:

#### Disabled

The light is ignored when baking lightmaps. This is the mode to use for dynamic lighting effects such as explosions and weapon effects.

> **Warning:** Hiding a light has no effect on the resulting lightmap bake. This means you must use the Disabled bake mode instead of hiding the Light node by disabling its **Visible** property.

#### Dynamic

This is the default mode, and is a compromise between performance and real-time friendliness. Only indirect lighting will be baked. Direct light and shadows are still real-time, as they would be without LightmapGI.

This mode allows performing _subtle_ changes to a light's color, energy and position while still looking fairly correct. For example, you can use this to create flickering static torches that have their indirect light baked.

Depending on the value of **Shadowmask Mode**, it is possible to still get distant baked shadows for DirectionalLight3D. This allows shadows up close to be real-time and show dynamic objects, while allowing static objects in the distance to still cast shadows.

#### Static

Both indirect and direct lighting will be baked. Since static surfaces can skip lighting and shadow computations entirely, this mode provides the best performance along with smooth shadows that never fade based on distance. The real-time light will not affect baked surfaces anymore, but it will still affect dynamic objects. When using the **All** bake mode on a light, dynamic objects will not cast real-time shadows onto baked surfaces, so you need to use a different approach such as blob shadows instead. Blob shadows can be implemented with a Decal node.

The light will not be adjustable at all during gameplay. Moving the light or changing its color (or energy) will not have any effect on static surfaces.

Since bake modes can be adjusted on a per-light basis, it is possible to create hybrid baked light setups. One popular option is to use a real-time DirectionalLight with its bake mode set to **Dynamic**, and use the **Static** bake mode for OmniLights and SpotLights. This provides good performance while still allowing dynamic objects to cast real-time shadows in outdoor areas.

Fully baked lights can also make use of light nodes' **Size** (omni/spot) or **Angular Distance** (directional) properties. This allows for shadows with realistic penumbra that increases in size as the distance between the caster and the shadow increases. This also has a lower performance cost compared to real-time PCSS shadows, as only dynamic objects have real-time shadows rendered on them.

### Baking

To begin the bake process, click the **Bake Lightmaps** button at the top of the 3D editor viewport when selecting the LightmapGI node:

This can take from seconds to minutes (or hours) depending on scene size, bake method and quality selected.

> **Warning:** Baking lightmaps is a process that can require a lot of video memory, especially if the resulting texture is large. Due to internal limitations, the engine may also crash if the generated texture size is too large (even on systems with a lot of video memory). To avoid crashes, make sure the lightmap texel size in the Import dock is set to a high enough value.

#### Tweaks

- **Quality:** Four bake quality modes are provided: Low, Medium, High, and Ultra. Higher quality takes more time, but result in a better-looking lightmap with less noise. The difference is especially noticeable with emissive materials or areas that get little to no direct lighting. Each bake quality mode can be further adjusted in the Project Settings.
- **Supersampling:** This creates the lightmap at a higher resolution and then downsamples it. This reduces noise and light leaking, and produces better shadows with small scale details. However, using it will increase bake times and memory usage during lightmap baking. The **Supersampling Factor** changes the size the lightmap is rendered at before downsampling.
- **Bounces:** The number of bounces to use for indirect lighting. The default value (`3`) is a good compromise between bake times and quality. Higher values will make light bounce around more times before it stops, which makes indirect lighting look smoother (but also possibly brighter depending on materials and geometry).
- **Bounce Indirect Energy:** The global multiplier to use when baking lights' indirect energy. This multiplies each light's own **Indirect Energy** value. Values different from `1.0` are not physically accurate, but can be used for artistic effect.
- **Directional:** If enabled, stores directional information for lightmaps. This improves normal mapped materials' appearance for baked surfaces, especially with fully baked lights (since they also have direct light baked). The downside is that directional lightmaps are slightly more expensive to render. They also require more time to bake and result in larger file sizes.
- **Shadowmask Mode:** If set to a mode other than **None**, the first DirectionalLight3D in the scene with the **Dynamic** global illumination mode will have its static shadows baked to a separate texture called a _shadowmask_. This can be used to allow distant static objects to cast shadows onto other static objects regardless of the distance from the camera. See the **section on shadowmasking** for further details.
- **Interior:** If enabled, environment lighting will not be sourced. Use this for purely indoor scenes to avoid light leaks.
- **Use Texture for Bounces:** If enabled, a texture with the lighting information will be generated to speed up the generation of indirect lighting at the cost of some accuracy. The geometry might exhibit extra light leak artifacts when using low resolution lightmaps or UVs that stretch the lightmap significantly across surfaces. Leave this enabled if unsure.
- **Use Denoiser:** If enabled, uses a denoising algorithm to make the lightmap significantly less noisy. This increases bake times and can occasionally introduce artifacts, but the result is often worth it. See **Denoising** for more information.
- **Denoiser Strength:** The strength of denoising step applied to the generated lightmaps. Higher values are more effective at removing noise, but can reduce shadow detail for static shadows. Only effective if denoising is enabled and the denoising method is JNLM (OIDN does not have a denoiser strength setting).
- **Bias:** The offset value to use for shadows in 3D units. You generally don't need to change this value, except if you run into issues with light bleeding or dark spots in your lightmap after baking. This setting does not affect real-time shadows casted on baked surfaces (for lights with **Dynamic** bake mode).
- **Max Texture Size:** The maximum texture size for the generated texture atlas. Higher values will result in fewer slices being generated, but may not work on all hardware as a result of hardware limitations on texture sizes. Leave this at its default value of `16384` if unsure.
- **Environment > Mode:** Controls how environment lighting is sourced when baking lightmaps. The default value of **Scene** is suited for levels with visible exterior parts. For purely indoor scenes, set this to **Disabled** to avoid light leaks and speed up baking. This can also be set to **Custom Sky** or **Custom Color** to use environment lighting that differs from the actual scene's environment sky.
- **Gen Probes > Subdiv:** See **Dynamic objects**.
- **Data > Light Data:** See **Lightmap data**.

### Using shadowmasking for distant directional shadows

When using a DirectionalLight3D, the maximum distance at which it can draw real-time shadows is limited by its **Shadow Max Distance** property. This can be an issue in large scenes, as distant objects won't appear to have any shadows from the DirectionalLight3D. While this can be resolved by using the **Static** global illumination mode on the DirectionalLight3D, this has several downsides:

- Since both direct and indirect light are baked, there is no way for dynamic objects to cast shadows onto static surfaces in a realistic manner. Godot skips shadow sampling entirely in this case to avoid "double lighting" artifacts.
- Static shadows up close lack in detail, as they only rely on the lightmap texture and not on real-time shadow cascades.

We can avoid these downsides while still benefiting from distant shadows by using _shadowmasking_. While dynamic objects won't receive shadows from the shadowmask, it still greatly improves visuals since most scenes are primarily comprised of static objects.

Since the lightmap texture alone doesn't contain shadow information, we can bake this shadow information to a separate texture called a _shadowmask_.

Shadowmasking only affects the first DirectionalLight3D in the scene (determined by tree order) that has the **Dynamic** global illumination mode. It is not possible to use shadowmasking with the **Static** global illumination mode, as this mode skips shadow sampling on static objects entirely. This is because the Static global illumination mode bakes both direct and indirect light.

Three shadowmasking modes are available:

- **None (default):** Don't bake a shadowmask texture. Directional shadows will not be visible outside the range specified by the DirectionalLight3D's **Shadow Max Distance** property.
- **Replace:** Bakes a shadowmask texture, and uses it to draw directional shadows when outside the range specified by the DirectionalLight3D's **Shadow Max Distance** property. Shadows within this range remain fully real-time. This option generally makes the most sense for most scenes, as it can deal well with static objects that exhibit subtle motion (e.g. foliage shadows).
- **Overlay:** Bakes a shadowmask texture, and uses it to draw directional shadows regardless of the distance from the camera. Shadows within the range of the DirectionalLight3D's **Shadow Max Distance** property will be overlaid with real-time shadows. This can make the transition between real-time and baked shadows less jarring, at the cost of a "smearing" effect present on static object shadows depending on lightmap texel density. Also, this mode can't deal as well with static objects that exhibit subtle motion (such as foliage), as the baked shadows can't be animated over time. Still, for scenes where the camera moves quickly, this may be a better choice than **Replace**.

Here's a visual comparison of the shadowmask modes with a scene where the **Shadow Max Distance** was set very low for comparison purposes. The blue boxes are dynamic objects, while the rest of the scene is a static object. There is only a single DirectionalLight3D in the scene with the Dynamic global illumination mode:

> **Note:** It is possible to switch between the **Replace** and **Overlay** shadowmask modes without having to bake lightmaps again.

### Balancing bake times with quality

Since high-quality bakes can take very long (up to dozens of minutes for large complex scenes), it is recommended to use lower quality settings at first. Then, once you are confident with your scene's lighting setup, raise the quality settings and perform a "final" bake before exporting your project.

Reducing the lightmap resolution by increasing **Lightmap Texel Size** on the imported 3D scenes will also speed up baking significantly. However, this will require you to reimport all lightmapped 3D scenes before you can bake lightmaps again.

### Denoising

Since baking lightmaps relies on raytracing, there will always be visible noise in the "raw" baked lightmap. Noise is especially visible in areas that are difficult to reach by bounced light, such as indoor areas with small openings where the sunlight can enter. Noise can be reduced by increasing bake quality, but doing so will increase bake times significantly.

To combat noise without increasing bake times too much, a denoiser can be used. A denoiser is an algorithm that runs on the final baked lightmap, detects patterns of noise and softens them while attempting to best preserve detail. Godot offers two denoising algorithms:

#### JNLM (Non-Local Means with Joint Filtering)

JNLM is the default denoising method and is included in Godot. It uses a simple but efficient denoising algorithm known as _non-local means_. JNLM runs on the GPU using a compute shader, and is compatible with any GPU that can run Godot 4's RenderingDevice-based renderers. No additional setup is required.

JNLM's denoising can be adjusted using the **Denoiser Strength** property that is visible when **Use Denoiser** enabled. Higher values can be more effective at removing noise, at the cost of suppressing shadow detail for static shadows.

#### OIDN (Open Image Denoise)

Unlike JNLM, OIDN uses a machine learning approach to denoising lightmaps. It features a model specifically trained to remove noise from lightmaps while preserving more shadow detail in most scenes compared to JNLM.

OIDN can run on the GPU if hardware acceleration is configured. With a modern high-end GPU, this can provide a speedup of over 50× over CPU-based denoising:

- On AMD GPUs, HIP must be installed and configured.
- On NVIDIA GPUs, CUDA must be installed and configured. This may automatically be done by the NVIDIA installer, but on Linux, CUDA libraries may not be installed by default. Double-check that the CUDA packages from your Linux distribution are installed.
- On Intel GPUs, SYCL must be installed and configured.

If hardware acceleration is not available, OIDN will fall back to multithreaded CPU-based denoising. To confirm whether GPU-based denoising is working, use a GPU utilization monitor while baking lightmaps and look at the GPU utilization percentage and VRAM utilization while the denoising step is shown in the Godot editor. The `nvidia-smi` command line tool can be useful for this.

OIDN is not included with Godot due to its relatively large download size. You can download precompiled OIDN binary packages from its [website](https://www.openimagedenoise.org/downloads.html). Extract the package to a location on your PC, then specify the path to the `oidnDenoise` executable in the Editor Settings (**FileSystem > Tools > OIDN > OIDN Denoise Path**). This executable is located within the `bin` folder of the binary package you extracted.

After specifying the path to the OIDN denoising executable, change the denoising method in the project settings by setting **Rendering > Lightmapping > Denoiser** to **OIDN**. This will affect all lightmap bakes on this project after the setting is changed.

> **Note:** The denoising method is configured in the project settings instead of the editor settings. This is done so that different team members working on the same project are assured to be using the same denoising method for consistent results.

### Dynamic objects

Unlike VoxelGI and SDFGI, dynamic objects receive indirect lighting differently compared to static objects. This is because lightmapping is only performed on static objects.

To display indirect lighting on dynamic objects, a 3D probe system is used, with light probes being spread throughout the scene. When baking lightmaps, the lightmapper will calculate the amount of _indirect_ light received by the probe. Direct light is not stored within light probes, even for lights that have their bake mode set to **Static** (as dynamic objects continue to be lit in real-time).

There are 2 ways to add light probes to a scene:

- **Automatic:** Set **Gen Probes > Subdiv** to a value other than **Disabled**, then bake lightmaps. The default is `8`, but you can choose a greater value to improve precision at the cost of longer bake times and larger output file size.
- **Manual:** In addition or as an alternative to generating probes automatically, you can add light probes manually by adding [LightmapProbe](../godot_csharp_nodes_3d.md) nodes to the scene. This can be used to improve lighting detail in areas frequently travelled by dynamic objects. After placing LightmapProbe nodes in the scene, you must bake lightmaps again for them to be effective.

> **Note:** After baking lightmaps, you will notice white spheres in the 3D scene that represent how baked lighting will affect dynamic objects. These spheres do **not** appear in the running project. If you want to hide these spheres in the editor, toggle **View > Gizmos > LightmapGI** at the top of the 3D editor (a "closed eye" icon indicates the gizmo is hidden).

### Lightmap data

The **Data > Light Data** property in the LightmapGI node contains the lightmap data after baking. Textures are saved to disk, but this also contains the capture data for dynamic objects, which can be heavy. If you are using a scene in `.tscn` format, you should save this resource to an external binary `.lmbake` file to avoid bloating the `.tscn` scene with binary data encoded in Base64.

> **Tip:** The generated EXR file can be viewed and even edited using an image editor to perform post-processing if needed. However, keep in mind that changes to the EXR file will be lost when baking lightmaps again.

### Reducing LightmapGI artifacts

If you notice LightmapGI nodes popping in and out of existence as the camera moves, this is most likely because the engine is rendering too many LightmapGI instances at once. Godot is limited to rendering 8 LightmapGI nodes at once, which means up to 8 instances can be in the camera view before some of them will start flickering.

---
