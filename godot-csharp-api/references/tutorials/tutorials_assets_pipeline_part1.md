# Godot 4 C# Tutorials — Assets Pipeline (Part 1)

> 7 tutorials. C#-specific code examples.

## Exporting 3D scenes

### Overview

In Godot, it is possible to export 3D scenes as a glTF 2.0 file. You can export as a glTF binary (`.glb` file) or glTF embedded with textures (`gltf` + `.bin` + textures). This allows you to create scenes in Godot, such as a CSG mesh blockout for a level, export it to clean it up in a program such as Blender, and then bring it back into Godot.

> **Note:** Only Blender 2.83 and newer can import glTF files exported by Godot.

To export a scene in the editor go to **Scene > Export As... > glTF 2.0 Scene...**

### Limitations

There are several limitations with glTF export.

- No support for exporting particles since their implementation varies across engines.
- ShaderMaterials cannot be exported.
- No support for exporting 2D scenes.

> **See also:** 3D scenes can be saved at runtime using [runtime file loading and saving](tutorials_io.md), including from an exported project.

---

## Import process

### Importing assets in Godot

To import assets in Godot, place your assets (image files, scenes, audio files, fonts, etc) directly in the project folder. There are 2 ways to achieve this:

- **For any file type:** Copy files manually with your operating system's file manager.
- **For file types that can be imported by Godot:** Drag-and-drop files from the operating system's file manager to the editor's FileSystem dock. This only works with _resource_ file types (i.e. file types that Godot can import).

Godot will automatically import these files internally and keep the imported resources hidden in a `res://.godot/imported/` folder.

This means that when trying to access imported assets through code, you need to use the [Resource Loader](../godot_csharp_core.md) as it will automatically take into account where the internal files are saved. If you try and access an imported asset using the [FileAccess](../godot_csharp_filesystem.md) class, it will work in the editor, but **it will break in the exported project**.

However, the [Resource Loader](../godot_csharp_core.md) cannot access non-imported files. Only the [FileAccess](../godot_csharp_filesystem.md) class can.

### Changing import parameters

> **Note:** Import parameters are only present in _non-native_ Godot resource types. This means Godot's own scene and resource file formats (`.tscn`, `.scn`, `.tres`, `.res`) don't have import options you can select in the Import dock.

To change the import parameters of an asset in Godot, select the relevant resource in the FileSystem dock:

After adjusting the parameters, click **Reimport**. Be careful: if you select another file in the FileSystem dock before clicking **Reimport**, changes will be discarded. After clicking **Reimport**, the chosen parameters will only be used for this asset and on future reimports.

Changing the import parameters of several assets at the same time is also possible. Select all of them together in the FileSystem dock and the exposed parameters will apply to all of them when reimporting.

### Reimporting multiple assets

While working on a project you may find that several assets need to have the same parameters changed, such as enabling mipmaps, but you only want those specific parameters changed. To do this, select every asset you want to reimport in the file system. In the import tab there will now be a checkbox to the left of every import parameter.

Select the checkbox of the parameters you want to change on your imported assets, then change the parameters normally. Finally, click the reimport button and every selected asset will be reimported with only those parameters changed.

### Automatic reimport

When the MD5 checksum of the source asset changes, Godot will perform an automatic reimport of it, applying the preset configured for that specific asset.

### Files generated

Importing will add an extra `<asset>.import` file next to the source file, containing the import configuration.

**Make sure to commit these files to your version control system**, as these files contain important metadata.

Additionally, extra assets will be present in the hidden `res://.godot/imported/` folder:

If any of the files present in this folder is erased (or the whole folder), the asset or assets will be reimported automatically. As such, committing the `.godot/` folder to the version control system is not recommended. While committing this folder can shorten reimporting time when checking out on another computer, it requires considerably more space and bandwidth.

The default version control metadata that can be generated on project creation will automatically ignore the `.godot/` folder.

### Changing import resource type

Some source assets can be imported as different types of resources. For this, select the relevant type of resource desired then click **Reimport**:

Select `Keep File (exported as is)` as resource type to skip file import, files with this resource type will be preserved as is during project export.

Select `Skip File (not exported)` as resource type to skip file import and ignore file during project export.

### Changing default import parameters

Different types of projects might require different defaults. Changing the import options to a predefined set of options can be achieved by using the **Preset...** Menu. Besides some resource types offering presets, the default settings can be saved and cleared too:

The default import parameters for a given resource type can be changed project-wide using the **Import Defaults** tab of the Project Settings dialog:

### Further reading

This workflow takes a little time to get used to, but it enforces a more correct way to deal with resources.

There are many types of assets available for import. Continue reading to understand how to work with all of them:

- Importing images
- Importing audio samples
- Importing 3D scenes
- Importing translations

---

## Advanced Import Settings

While the regular import panel provides many essential options for imported 3D models, the advanced import settings provides per object options, model previews, and animation previews. To open it select the Advanced... button at the bottom of the import dock.

This is available for 3D models imported as scenes, as well as animation libraries.

> **Note:** This page does not go over options also available in the import dock, or anything outside of the advanced import settings. For information on those please read the Import configuration page.

### Using the Advanced Import Settings dialog

The first tab you'll see is the **Scene** tab. The options available in the panel on the right are identical to the Import dock, but you have access to a 3D preview. The 3D preview can be rotated by holding down the left mouse button then dragging the mouse. Zoom can be adjusted using the mouse wheel.

#### Configuring node import options

You can select individual nodes that compose the scene while in the **Scene** tab using the tree view at the left:

This exposes several per-node import options:

- **Skip Import:** If checked, the node will not be present in the final imported scene. Enabling this disables all other options.
- **Generate > Physics:** If checked, generates a PhysicsBody3D _parent_ node with collision shapes that are _siblings_ to the MeshInstance3D node.
- **Generate > NavMesh:** If checked, generates a NavigationRegion3D _child_ node for [navigation](tutorials_navigation.md). **Mesh + NavMesh** will keep the original mesh visible, while **NavMesh Only** will only import the navigation mesh (without a visual representation). **NavMesh Only** is meant to be used when you've manually authored a simplified mesh for navigation.
- **Generate > Occluder:** If checked, generates an OccluderInstance3D _sibling_ node for [occlusion culling](tutorials_3d.md) using the mesh's geometry as a basis for the occluder's shape. **Mesh + Occluder** will keep the original mesh visible, while **Occluder Only** will only import the occluder (without a visual representation). **Occluder Only** is meant to be used when you've manually authored a simplified mesh for occlusion culling.

These options are only visible if some of the above options are enabled:

- **Physics > Body Type:** Only visible if **Generate > Physics** is enabled. Controls the PhysicsBody3D that should be created. **Static** creates a StaticBody3D, **Dynamic** creates a RigidBody3D, **Area** creates an Area3D.
- **Physics > Shape Type:** Only visible if **Generate > Physics** is enabled. **Trimesh** allows for precise per-triangle collision, but it can only be used with a **Static** body type. Other types are less precise and may require manual configuration, but can be used with any body type. For static level geometry, use **Trimesh**. For dynamic geometry, use primitive shapes if possible for better performance, or use one of the convex decomposition modes if the shape is large and complex.
- **Decomposition > Advanced:** Only visible if **Physics > Shape Type** is **Decompose Convex**. If checked, allows adjusting advanced decomposition options. If disabled, only a preset **Precision** can be adjusted (which is usually sufficient).
- **Decomposition > Precision:** Only visible if **Physics > Shape Type** is **Decompose Convex**. Controls the precision to use for convex decomposition. Higher values result in more detailed collision, at the cost of slower generation and increased CPU usage during physics simulation. To improve performance, it's recommended to keep this value as low as possible for your use cases.
- **Occluder > Simplification Distance:** Only visible if **Generate > Occluder** is set to **Mesh + Occluder** or **Occluder Only**. Higher values result in an occluder mesh with fewer vertices (resulting in decreased CPU utilization), at the cost of more occlusion culling issues (such as false positives or false negatives). If you run into objects disappearing when they shouldn't when the camera is near a certain mesh, try decreasing this value.

#### Configuring mesh and material import options

In the Advanced Import Settings dialog, there are 2 ways to select individual meshes or materials:

- Switch to the **Meshes** or **Materials** tab in the top-left corner of the dialog.
- Stay in the **Scene** tab, but unfold the options on the tree view on the left. After choosing a mesh or material, this presents the same information as the **Meshes** and **Materials** tabs, but in a tree view instead of a list.

If you select a mesh, different options will appear in the panel on the right:

The options are as follows:

- **Save to File:** Saves the [Mesh](../godot_csharp_rendering.md) _resource_ to an external file (this isn't a scene file). You generally don't need to use this for placing the mesh in a 3D scene – instead, you should instance the 3D scene directly. However, having direct access to the Mesh resource is useful for specific nodes, such as [MeshInstance3D](../godot_csharp_nodes_3d.md), [MultiMeshInstance3D](../godot_csharp_nodes_3d.md), [GPUParticles3D](../godot_csharp_misc.md) or [CPUParticles3D](../godot_csharp_misc.md). - You will also need to specify an output file path using the option that appears after enabling **Save to File**. It's recommended to use the `.res` output file extension for smaller file sizes and faster loading speeds, as `.tres` is inefficient for writing large amounts of data.
- **Generate > Shadow Meshes:** Per-mesh override for the **Meshes > Create Shadow Meshes** scene-wide import option described in Using the Import dock. **Default** will use the scene-wide import option, while **Enable** or **Disable** can forcibly enable or disable this behavior on a specific mesh.
- **Generate > Lightmap UV:** Per-mesh override for the **Meshes > Light Baking** scene-wide import option described in Using the Import dock. **Default** will use the scene-wide import option, while **Enable** or **Disable** can forcibly enable or disable this behavior on a specific mesh. - Setting this to **Enable** on a scene with the **Static** light baking mode is equivalent to configuring this mesh to use **Static Lightmaps**. Setting this to **Disable** on a scene with the **Static Lightmaps** light baking mode is equivalent to configuring this mesh to use **Static** instead.
- **Generate > LODs:** Per-mesh override for the **Meshes > Generate LODs** scene-wide import option described in Using the Import dock. **Default** will use the scene-wide import option, while **Enable** or **Disable** can forcibly enable or disable this behavior on a specific mesh.
- **LODs > Normal Merge Angle:** The minimum angle difference between two vertices required to preserve a geometry edge in mesh LOD generation. If running into visual issues with LOD generation, decreasing this value may help (at the cost of less efficient LOD generation).

If you select a material, only one option will appear in the panel on the right:

When **Use External** is checked and an output path is specified, this lets you use an external material instead of the material that is included in the original 3D scene file; see the section below.

### Extracting materials to separate files

While Godot can import materials authored in 3D modeling software, the default configuration may not be suitable for your needs. For example:

- You want to configure material features not supported by your 3D application.
- You want to use a different texture filtering mode, as this option is configured in the material (and not in the image).
- You want to replace one of the materials with an entirely different material, such as a custom shader.

To be able to modify the 3D scene's materials in the Godot editor, you need to use _external_ material resources.

In the top-left corner of the Advanced Import Settings dialog, choose **Actions… > Extract Materials**:

After choosing this option, select a folder to extract material `.tres` files to, then confirm the extraction:

> **Note:** After extracting materials, the 3D scene will automatically be configured to use external material references. As a result, you don't need to manually enable **Use External** on every material to make the external `.tres` material effective.

When **Use External** is enabled, remember that the Advanced Import Settings dialog will keep displaying the mesh's original materials (the ones designed in the 3D modeling software). This means your customizations to the materials won't be visible within this dialog. To preview your modified materials, you need to place the imported 3D scene in another scene using the editor.

Godot will not overwrite changes made to extracted materials when the source 3D scene is reimported. However, if the material name is changed in the source 3D file, the link between the original material and the extracted material will be lost. As a result, you'll need to use the Advanced Import Settings dialog to associate the renamed material to the existing extracted material.

The above can be done in the dialog's **Materials** tab by selecting the material, enabling **Save to File**, then specifying the save path using the **Path** option that appears after enabling **Save to File**.

### Animation options

Several extra options are available for the generated [AnimationPlayer](../godot_csharp_resources.md) nodes, as well as their individual animations when they're selected in the **Scene** tab.

#### Optimizer

When animations are imported, an optimizer is run, which reduces the size of the animation considerably. In general, this should always be turned on unless you suspect that an animation might be broken due to it being enabled.

#### Save to file

By default, animations are saved as built-in. It is possible to save them to a file instead. This allows adding custom tracks to the animations and keeping them after a reimport.

#### Slices

It is possible to specify multiple animations from a single timeline as slices. For this to work, the model must have only one animation that is named `default`. To create slices, change the slice amount to something greater than zero. You can then name a slice, specify which frames it starts and stops on, and choose whether the animation loops or not.

---

## Available 3D formats

When dealing with 3D assets, Godot has a flexible and configurable importer.

Godot works with _scenes_. This means that the entire scene being worked on in your favorite 3D modeling software will be transferred as close as possible.

Godot supports the following 3D _scene file formats_:

- glTF 2.0 **(recommended)**. Godot has support for both text (`.gltf`) and binary (`.glb`) formats.
- `.blend` (Blender). This works by calling Blender to export to glTF in a transparent manner (requires Blender to be installed).
- DAE (COLLADA), an older format that is supported.
- OBJ (Wavefront) format + their MTL material files. This is also supported, but pretty limited given the format's limitations (no support for pivots, skeletons, animations, UV2, PBR materials, ...).
- FBX, supported via the [ufbx](https://github.com/ufbx/ufbx) library. The previous import workflow used [FBX2glTF](https://github.com/godotengine/FBX2glTF) integration. This requires installing an external program that links against the proprietary FBX SDK, so we recommend using the default ufbx method or other formats listed above (if suitable for your workflow).

Copy the scene file together with the textures and mesh data (if separate) to the project repository, then Godot will do a full import when focusing the editor window.

### Exporting glTF 2.0 files from Blender (recommended)

There are 3 ways to export glTF files from Blender:

- As a glTF binary file (`.glb`).
- As a glTF text-based file with separate binary data and textures (`.gltf` file + `.bin` file + textures).

glTF binary files (`.glb`) are the smaller option. They include the mesh and textures set up in Blender. When brought into Godot the textures are part of the object's material file.

There are two reasons to use glTF with the textures separate. One is to have the scene description in a text based format and the binary data in a separate binary file. This can be useful for version control if you want to review changes in a text-based format. The second is you need the texture files separate from the material file. If you don't need either of those, glTF binary files are fine.

The glTF import process first loads the glTF file's data into an in-memory GLTFState class. This data is then used to generate a Godot scene. When importing files at runtime, this scene can be directly added to the tree. The export process is the reverse of this, a Godot scene is converted to a GLTFState class, then the glTF file is generated from that.

When importing glTF files in the editor, there are two more steps. After generating the Godot scene, the ResourceImporterScene class is used to apply additional import settings, including settings you set through the Import dock and the Advanced Import Settings dialog. This is then saved as a Godot scene file, which is what gets used when you run/export your game.

> **Warning:** If your model contains blend shapes (also known as "shape keys" and "morph targets"), your glTF export setting **Data > Armature > Export Deformation Bones Only** needs to be configured to **Enabled**. Exporting non-deforming bones anyway will lead to incorrect shading.

> **Note:** Blender versions older than 3.2 do not export emissive textures with the glTF file. If your model uses one and you're using an older version of Blender, it must be brought in separately. By default, Blender has backface culling disabled on materials and will export materials to match how they render in Blender. This means that materials in Godot will have their cull mode set to **Disabled**. This can decrease performance since backfaces will be rendered, even when they are being culled by other faces. To resolve this, enable **Backface Culling** in Blender's Materials tab, then export the scene to glTF again.

### Importing .blend files directly within Godot

> **Note:** This functionality requires Blender 3.0 or later. For best results, we recommend using Blender 3.5 or later, as it includes many fixes to the glTF exporter. It is **strongly** recommended to use an official Blender release downloaded from blender.org, as opposed to a Linux distribution package or Flatpak. This avoids any issues related to packaging, such as different library versions that can cause incompatibilities or sandboxing restrictions.

The editor can directly import `.blend` files by calling [Blender](https://www.blender.org/)'s glTF export functionality in a transparent manner.

This allows you to iterate on your 3D scenes faster, as you can save the scene in Blender, alt-tab back to Godot then see your changes immediately. When working with version control, this is also more efficient as you no longer need to commit a copy of the exported glTF file to version control.

To use `.blend` import, you must install Blender before opening the Godot editor (if opening a project that already contains `.blend` files). If you keep Blender installed at its default location, Godot should be able to detect its path automatically. If this isn't the case, configure the path to the Blender executable in the Editor Settings (**Filesystem > Import > Blender > Blender Path**).

If you keep `.blend` files within your project folder but don't want them to be imported by Godot, disable **Filesystem > Import > Blender > Enabled** in the advanced Project Settings.

The `.blend` import process converts to glTF first, so it still uses Godot's glTF import code. Therefore, the `.blend` import process is the same as the glTF import process, but with an extra step at the beginning.

> **Note:** When working in a team, keep in mind using `.blend` files in your project will require _all_ team members to have Blender installed. While Blender is a free download, this may add friction when working on the project. `.blend` import is also not available on the Android and web editors, as these platforms can't call external programs. If this is problematic, consider using glTF scenes exported from Blender instead.

### Exporting DAE files from Blender

Blender has built-in COLLADA support, but it does not work properly for the needs of game engines and shouldn't be used as-is. However, scenes exported with the built-in Collada support may still work for simple scenes without animation.

For complex scenes or scenes that contain animations it is highly recommend to use glTF instead.

### Importing OBJ files in Godot

OBJ is one of the simplest 3D formats out there, so Godot should be able to import most OBJ files successfully. However, OBJ is also a very limited format: it doesn't support skinning, animation, UV2 or PBR materials.

There are 2 ways to use OBJ meshes in Godot:

- Load them directly in a MeshInstance3D node, or any other property that expects as mesh (such as GPUParticles3D). This is the default mode.
- Change their import mode to **OBJ as Scene** in the Import dock then restart the editor. This allows you to use the same import options as glTF or Collada scenes, such as unwrapping UV2 on import (for [Using Lightmap global illumination](tutorials_3d.md)).

> **Note:** Blender 3.4 and later can export RGB vertex colors in OBJ files (this is a nonstandard extension of the OBJ format). Godot is able to import those vertex colors, but they will not be displayed on the material unless you enable **Vertex Color > Use As Albedo** on the material. Vertex colors from OBJ meshes keep their original color space once imported (sRGB/linear), but their brightness is clamped to 1.0 (they can't be overbright).

### Importing FBX files in Godot

By default any FBX file added to a Godot project in Godot 4.3 or later will use the ufbx import method. Any file that was was added to a project in a previous version, such as 4.2, will continue to be imported via the FBX2glTF method unless you go into that files import settings, and change the importer to `ufbx`.

If you keep `.fbx` files within your project folder but don't want them to be imported by Godot, disable **Filesystem > Import > FBX > Enabled** in the advanced Project Settings.

If you want to setup the FBX2glTF workflow, which is generally not recommend unless you have a specific reason to use it, you need to download the [FBX2glTF](https://github.com/godotengine/FBX2glTF) executable, then specify the path to that executable in the editor settings under **Filesystem > Import > FBX > FBX2glTFPath**

The FBX2glTF import process converts to glTF first, so it still uses Godot's glTF import code. Therefore, the FBX import process is the same as the glTF import process, but with an extra step at the beginning.

> **See also:** The full installation process for using FBX2glTF in Godot is described on the [FBX import page of the Godot website](https://godotengine.org/fbx-import).

---

## Import configuration

Godot provides several ways to customize the imported data, such as the import dock, the advanced import setting dialog, and inherited scenes. This can be used to make further changes to the imported scene, such as adjusting meshes, adding physics information, and adding new nodes. You can also write a script that runs code at the end of the import process to perform arbitrary customization.

Note that, when applicable, modifying the original data should be preferred to configuring the scene after import. This helps minimize the differences between the 3D modeling application and the imported scene. See the Model export considerations and Node type customization using name suffixes articles for more information.

### Import workflows

Since Godot can only save its own scene format (`.tscn`/`.scn`), Godot cannot save over the original 3D scene file (which uses a different format). This is also a safer approach as it avoids making accidental changes to the source file.

To allow customizing the scene and its materials, Godot's scene importer allows for different workflows regarding how data is imported.

This import process is customizable using 3 separate interfaces, depending on your needs:

- The **Import** dock, after selecting the 3D scene by clicking it once in the FileSystem dock.
- The **Advanced Import Settings** dialog, which can be accessed by double-clicking the 3D scene in the FileSystem dock or by clicking the **Advanced…** button in the Import dock. This allows you to customize per-object options in Godot, and preview models and animations. please see the Advanced Import Settings page for more information.
- Import hints, which are special suffixes added to object names in the 3D modeling software. This allows you to customize per-object options in the 3D modeling software.

For basic customization, using the Import dock suffices. However, for more complex operations such as defining material overrides on a per-material basis, you'll need to use the Advanced Import Settings dialog, import hints, or possibly both.

#### Using the Import dock

The following options can be adjusted in the Import dock after selecting a 3D scene in the FileSystem dock:

- **Root Type:** The node type to use as a root node. Using node types that inherit from Node3D is recommended. Otherwise, you'll lose the ability to position the node directly in the 3D editor.
- **Root Name:** The name of the root node in the imported scene. This is generally not noticeable when instancing the scene in the editor (or drag-and-dropping from the FileSystem dock), as the root node is renamed to match the filename in this case.
- **Apply Root Scale:** If enabled, **Root Scale** will be _applied_ on the meshes and animations directly, while keeping the root node's scale to the default (1, 1, 1). This means that if you add a child node later on within the imported scene, it won't be scaled. If disabled, **Root Scale** will multiply the scale of the root node instead.

**Meshes**

- **Ensure Tangents:** If checked, generate vertex tangents using [Mikktspace](http://www.mikktspace.com/) if the input meshes don't have tangent data. When possible, it's recommended to let the 3D modeling software generate tangents on export instead on relying on this option. Tangents are required for correct display of normal and height maps, along with any material/shader features that require tangents. If you don't need material features that require tangents, disabling this can reduce output file size and speed up importing if the source 3D file doesn't contain tangents.
- **Generate LODs:** If checked, generates lower detail variants of the mesh which will be displayed in the distance to improve rendering performance. Not all meshes benefit from LOD, especially if they are never rendered from far away. Disabling this can reduce output file size and speed up importing. See [Mesh level of detail (LOD)](tutorials_3d.md) for more information.
- **Create Shadow Meshes:** If checked, enables the generation of shadow meshes on import. This optimizes shadow rendering without reducing quality by welding vertices together when possible. This in turn reduces the memory bandwidth required to render shadows. Shadow mesh generation currently doesn't support using a lower detail level than the source mesh (but shadow rendering will make use of LODs when relevant).
- **Light Baking:** Configures the meshes' [global illumination mode](../godot_csharp_misc.md) in the 3D scene. If set to **Static Lightmaps**, sets the meshes' GI mode to **Static** and generates UV2 on import for [lightmap baking](tutorials_3d.md).
- **Lightmap Texel Size:** Only visible if **Light Baking** is set to **Static Lightmaps**. Controls the size of each texel on the baked lightmap. A smaller value results in more precise lightmaps, at the cost of larger lightmap sizes and longer bake times.

**Skins**

- **Use Named Skins:** If checked, use named [Skins](../godot_csharp_misc.md) for animation. The [MeshInstance3D](../godot_csharp_nodes_3d.md) node contains 3 properties of relevance here: a skeleton NodePath pointing to the Skeleton3D node (usually `..`), a mesh, and a skin:

- The [Skeleton3D](../godot_csharp_nodes_3d.md) node contains a list of bones with names, their pose and rest, a name and a parent bone.
- The mesh is all of the raw vertex data needed to display a mesh. In terms of the mesh, it knows how vertices are weight-painted and uses some internal numbering often imported from 3D modeling software.
- The skin contains the information necessary to bind this mesh onto this Skeleton3D. For every one of the internal bone IDs chosen by the 3D modeling software, it contains two things. Firstly, a Matrix known as the Bind Pose Matrix, Inverse Bind Matrix, or IBM for short. Secondly, the Skin contains each bone's name (if **Use Named Skins** is enabled), or the bone's index within the Skeleton3D list (if **Use Named Skins** is disabled).

Together, this information is enough to tell Godot how to use the bone poses in the Skeleton3D node to render the mesh from each MeshInstance3D. Note that each MeshInstance3D may share binds, as is common in models exported from Blender, or each MeshInstance3D may use a separate Skin object, as is common in models exported from other tools such as Maya.

**Animation**

- **Import:** If checked, import animations from the 3D scene.
- **FPS:** The number of frames per second to use for baking animation curves to a series of points with linear interpolation. It's recommended to configure this value to match the value you're using as a baseline in your 3D modeling software. Higher values result in more precise animation with fast movement changes, at the cost of higher file sizes and memory usage. Thanks to interpolation, there is usually not much benefit in going above 30 FPS (as the animation will still appear smooth at higher rendering framerates).
- **Trimming:** Trim the beginning and end of animations if there are no keyframe changes. This can reduce output file size and memory usage with certain 3D scenes, depending on the contents of their animation tracks.
- **Remove Immutable Tracks:** Remove animation tracks that only contain default values. This can reduce output file size and memory usage with certain 3D scenes, depending on the contents of their animation tracks.

**Import Script**

- **Path:** Path to an import script, which can run code _after_ the import process has completed for custom processing. See **Using import scripts for automation** for more information.

**glTF**

- **Embedded Texture Handling:** Controls how textures embedded within glTF scenes should be handled. **Discard All Textures** will not import any textures, which is useful if you wish to manually set up materials in Godot instead. **Extract Textures** extracts textures to external images, resulting in smaller file sizes and more control over import options. **Embed as Basis Universal** and **Embed as Uncompressed** keeps the textures embedded in the imported scene, with and without VRAM compression respectively.

**FBX**

- **Importer** Which import method is used. ubfx handles fbx files as fbx files. FBX2glTF converts FBX files to glTF on import and requires additional setup. FBX2glTF is not recommended unless you have a specific reason to use it over ufbx or working with a different file format.
- **Allow Geometry Helper Nodes** enables or disables geometry helper nodes
- **Embedded Texture Handling:** Controls how textures embedded within fbx scenes should be handled. **Discard All Textures** will not import any textures, which is useful if you wish to manually set up materials in Godot instead. **Extract Textures** extracts textures to external images, resulting in smaller file sizes and more control over import options. **Embed as Basis Universal** and **Embed as Uncompressed** keeps the textures embedded in the imported scene, with and without VRAM compression respectively.

**Blender-specific options**

Only visible for `.blend` files.

**Nodes**

- **Visible:** **All** imports everything, even invisible objects. **Visible Only** only imports visible objects. **Renderable** only imports objects that are marked as renderable in Blender, regardless of whether they are actually visible. In Blender, renderability is toggled by clicking the camera icon next to each object in the Outliner, while visibility is toggled by the eye icon.
- **Active Collection Only:** If checked, only imports nodes that are in the active collection in Blender.
- **Punctual Lights:** If checked, imports lights (directional, omni, and spot) from Blender. "Punctual" is not to be confused with "positional", which is why directional lights are also included.
- **Cameras:** If checked, imports cameras from Blender.
- **Custom Properties:** If checked, imports custom properties from Blender as glTF extras. This data can then be used from an editor plugin that uses [GLTFDocument.register_gltf_document_extension()](../godot_csharp_misc.md), which can set node metadata on import (among other use cases).
- **Modifiers:** If set to **No Modifiers**, object modifiers are ignored on import. If set to **All Modifiers**, applies modifiers to objects on import.

**Meshes**

- **Colors:** If checked, imports vertex colors from Blender.
- **UVs:** If checked, imports vertex UV1 and UV2 from Blender.
- **Normals:** If checked, imports vertex normals from Blender.
- **Export Geometry Nodes Instances:** If checked, imports [geometry node](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/introduction.html) instances from Blender.
- **GPU Instances** If checked, imports instances and particle systems as GLTF's buffer/accessor data instead of numerous singular Mesh3D object. This does not include Geometry Nodes instancing.
- **Tangents:** If checked, imports vertex tangents from Blender.
- **Skins:** **None** skips skeleton skin data import from Blender. **4 Influences (Compatible)** imports skin data to be compatible with all renderers, at the cost of lower precision for certain rigs. **All Influences** imports skin data with all influences (up to 8 in Godot), which is more precise but may not be compatible with all renderers.
- **Export Bones Deforming Mesh Only:** If checked, only imports bones that deform the mesh from Blender.

**Materials**

- **Unpack Enabled:** If checked, unpacks the original images to the Godot filesystem and uses them. This allows changing image import settings like VRAM compression. If unchecked, allows Blender to convert the original images, such as repacking roughness and metallic into one roughness + metallic texture. In most cases, this option should be left checked, but if the `.blend` file's images aren't in the correct format, this must be disabled for correct behavior.
- **Export Materials:** If set to **Placeholder**, does not import materials, but keeps surface slots so that separate materials can be assigned to different surfaces. If set to **Export**, imports materials as-is (note that procedural Blender materials may not work correctly). If set to **Named Placeholder**, imports materials, but doesn't import images that are packed into the `.blend` file. Textures will have to be reassigned manually in the imported materials.

**Animation**

- **Limit Playback:** If checked, limits animation import to the playback range defined in Blender (the **Start** and **End** options at the right of the animation timeline in Blender). This can avoid including unused animation data, making the imported scene smaller and faster to load. However, this can also result in missing animation data if the playback range is not set correctly in Blender.
- **Always Sample:** If checked, forces animation sampling on import to ensure consistency between how Blender and glTF perform animation interpolation, at the cost of larger file sizes. If unchecked, there may be differences in how animations are interpolated between what you see in Blender and the imported scene in Godot, due to different interpolation semantics between both.
- **Group Tracks:** If checked, imports animations (actives and on NLA tracks) as separate tracks. If unchecked, all the currently assigned actions become one glTF animation.

#### Using import scripts for automation

A special script to process the whole scene after import can be provided. This is great for post-processing, changing materials, doing funny stuff with the geometry, and more.

Create a script that is not attached to any node by right-clicking in the FileSystem dock and choosing **New > Script…**. In the script editor, write the following:

The `_post_import(scene: Node)` function takes the imported scene as argument (the parameter is actually the root node of the scene). The scene that will finally be used **must** be returned (even if the scene can be entirely different).

To use your script, locate the script in the import tab's "Path" option under the "Import Script" category.

#### Using animation libraries

You can also choose to import **only** animations from a glTF file and nothing else. This is used in some asset pipelines to distribute animations separately from models. For example, this allows you to use one set of animations for several characters, without having to duplicate animation data in every character.

To do so, select the glTF file in the FileSystem dock, then change the import mode to Animation Library in the Import dock:

Click **Reimport** and restart the editor when prompted. After restarting, the glTF file will be imported as an [AnimationLibrary](../godot_csharp_resources.md) instead of a [PackedScene](../godot_csharp_resources.md). This animation library can then be referenced in an [AnimationPlayer](../godot_csharp_resources.md) node.

The import options that are visible after changing the import mode to Animation Library act the same as when using the Scene import mode. See **Using the Import dock** for more information.

#### Filter script

It is possible to specify a filter script in a special syntax to decide which tracks from which animations should be kept.

The filter script is executed against each imported animation. The syntax consists of two types of statements, the first for choosing which animations to filter, and the second for filtering individual tracks within the matched animation. All name patterns are performed using a case-insensitive expression match, with support for `?` and `*` wildcards (using [String.matchn()](../godot_csharp_misc.md) under the hood).

The script must start with an animation filter statement (as denoted by the line beginning with an `@`). For example, if we would like to apply filters to all imported animations which have a name ending in `"_Loop"`:

```text
@+*_Loop
```

Similarly, additional patterns can be added to the same line, separated by commas. Here is a modified example to additionally _include_ all animations with names that begin with `"Arm_Left"`, but also _exclude_ all animations which have names ending in `"Attack"`:

```text
@+*_Loop, +Arm_Left*, -*Attack
```

Following the animation selection filter statement, we add track filtering patterns to indicate which animation tracks should be kept or discarded. If no track filter patterns are specified, then all tracks within the matched animations will be discarded!

It's important to note that track filter statements are applied in order for each track within the animation, this means that one line may include a track, a later rule can still discard it. Similarly, a track excluded by an early rule may then be re-included once again by a filter rule further down in the filter script.

For example: include all tracks in animations with names ending in `"_Loop"`, but discard any tracks affecting a `"Skeleton"` which end in `"Control"`, unless they have `"Arm"` in their name:

In the above example, tracks like `"Skeleton:Leg_Control"` would be discarded, while tracks such as `"Skeleton:Head"` or `"Skeleton:Arm_Left_Control"` would be retained.

Any track filter lines that do not begin with a `+` or `-` are ignored.

### Scene inheritance

In many cases, it may be desired to make manual modifications to the imported scene. By default, this is not possible because if the source 3D asset changes, Godot will re-import the _whole_ scene.

However, it is possible to make local modifications by using _scene inheritance_. If you try to open the imported scene using **Scene > Open Scene…** or **Scene > Quick Open Scene…**, the following dialog will appear:

In inherited scenes, the only limitations for modification are:

- Nodes from the base scene can't be removed, but additional nodes can be added anywhere.
- Subresources can't be edited. Instead, you need to save them externally as described above.

Other than that, everything is allowed.

---

## Model export considerations

Before exporting a 3D model from a 3D modeling application, such as Blender, there are some considerations that should be taken into account to ensure that the model follows the conventions and best practices for Godot.

### 3D asset direction conventions

Godot uses a right-handed, Y-is-up coordinate system, with the -Z axis as the camera's forward direction. This is the same as OpenGL. This implies that +Z is back, +X is right, and -X is left for a camera.

The convention for 3D assets is to face the opposite direction as the camera, so that characters and other assets are facing the camera by default. This convention is extremely common in 3D modeling applications, and is [codified in glTF as part of the glTF 2.0 specification](https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html#coordinate-system-and-units). This means that for oriented 3D assets (such as characters), the +Z axis is the direction of the front, so -Z is the rear, +X is the left side, and -X is the right side for a 3D asset. In Blender, this means that +Y is rear and -Y is front for an asset.

When rotating an oriented 3D asset in Godot, use the `use_model_front` option on the `look_at` functions, and use the `Vector3.MODEL_*` constants to perform calculations in the oriented asset's local space.

For assets without an intrinsic front side or forward direction, such as a game map or terrain, take note of the cardinal directions instead. The convention in Godot and the vast majority of other applications is that +X is east and -X is west. Due to Godot's right-handed Y-is-up coordinate system, this implies that +Z is south and -Z is north. In Blender, this means that +Y is north and -Y is south.

### Exporting textures separately

While textures can be exported with a model in certain file formats, such as glTF 2.0, you can also export them separately. Godot uses PBR (physically based rendering) for its materials, so if a texturing program can export PBR textures, they can work in Godot. This includes the [Substance suite](https://www.adobe.com/creativecloud/3d-ar.html), [ArmorPaint (open source)](https://armorpaint.org/), and [Material Maker (open source)](https://github.com/RodZill4/material-maker).

> **See also:** For more information on Godot's materials, see [Standard Material 3D and ORM Material 3D](tutorials_3d.md).

### Exporting considerations

Since GPUs can only render triangles, meshes that contain quads or N-gons have to be _triangulated_ before they can be rendered. Godot can triangulate meshes on import, but results may be unpredictable or incorrect, especially with N-gons. Regardless of the target application, triangulating _before_ exporting the scene will lead to more consistent results and should be done whenever possible.

To avoid issues with incorrect triangulation after importing in Godot, it is recommended to make the 3D modeling software triangulate objects on its own. In Blender, this can be done by adding a Triangulate modifier to your objects and making sure **Apply Modifiers** is checked in the export dialog. Alternatively, depending on the exporter, you may be able to find and enable a **Triangulate Faces** option in the export dialog.

To avoid issues with 3D selection in the editor, it is recommended to apply the object transform in the 3D modeling software before exporting the scene.

> **Note:** It is important that the mesh is not deformed by bones when exporting. Make sure that the skeleton is reset to its T-pose or default rest pose before exporting with your favorite 3D editor.

### Lighting considerations

While it's possible to import lights from a 3D scene using the glTF, `.blend` or Collada formats, it's generally advised to design the scene's lighting in the Godot editor after importing the scene.

This allows you to get a more accurate feel for the final result, as different engines will render lights in a different manner. This also avoids any issues with lights appearing excessively strong or faint as a result of the import process.

---

## Node type customization using name suffixes

Many times, when editing a scene, there are common tasks that need to be done after exporting:

- Adding collision detection to objects.
- Setting objects as navigation meshes.
- Deleting nodes that are not used in the game engine (like specific lights used for modeling).

To simplify this workflow, Godot offers several suffixes that can be added to the names of the objects in your 3D modeling software. When imported, Godot will detect suffixes in object names and will perform actions automatically.

> **Warning:** All the suffixes described below can be used with `-`, `$`, and `_` and are **case-insensitive**.

### Opting out

If you do not want Godot to perform any of the actions described below, you can set the `nodes/use_node_type_suffixes` import option to `false`. This will disable all node type suffixes, which keeps nodes the same type as the original file indicated. However, the `-noimp` suffix will still be respected, as well as non-node suffixes like `-vcol` or `-loop`.

Alternatively, you can completely opt out of all name suffixes by setting the `nodes/use_name_suffixes` import option to `false`. This will completely stop the general scene import code from looking at name suffixes. However, the format-specific import code may still look at name suffixes, such as the glTF importer checking for the `-loop` suffix.

Disabling these options makes editor-imported files more similar to the original files, and more similar to importing files at runtime. For an import workflow that works at runtime, gives more predictable results, and only has explicitly defined behavior, consider setting these options to `false` and using [GLTFDocumentExtension](../godot_csharp_misc.md) instead.

### Remove nodes and animations (-noimp)

Nodes and animations that have the `-noimp` suffix will be removed at import time no matter what their type is. They will not appear in the imported scene.

This is equivalent to enabling **Skip Import** for a node in the Advanced Import Settings dialog.

### Create collisions (-col, -convcol, -colonly, -convcolonly)

The option `-col` will work only for Mesh objects. If it is detected, a child static collision node will be added, using the same geometry as the mesh. This will create a triangle mesh collision shape, which is a slow, but accurate option for collision detection. This option is usually what you want for level geometry (but see also `-colonly` below).

The option `-convcol` will create a [ConvexPolygonShape3D](../godot_csharp_misc.md) instead of a [ConcavePolygonShape3D](../godot_csharp_misc.md). Unlike triangle meshes which can be concave, a convex shape can only accurately represent a shape that doesn't have any concave angles (a pyramid is convex, but a hollow box is concave). Due to this, convex collision shapes are generally not suited for level geometry. When representing simple enough meshes, convex collision shapes can result in better performance compared to a triangle collision shape. This option is ideal for simple or dynamic objects that require mostly-accurate collision detection.

However, in both cases, the visual geometry may be too complex or not smooth enough for collisions. This can create physics glitches and slow down the engine unnecessarily.

To solve this, the `-colonly` modifier exists. It will remove the mesh upon importing and will create a [StaticBody3D](../godot_csharp_nodes_3d.md) collision instead. This helps the visual mesh and actual collision to be separated.

The option `-convcolonly` works in a similar way, but will create a [ConvexPolygonShape3D](../godot_csharp_misc.md) instead using convex decomposition.

With Collada files, the option `-colonly` can also be used with Blender's empty objects. On import, it will create a [StaticBody3D](../godot_csharp_nodes_3d.md) with a collision node as a child. The collision node will have one of a number of predefined shapes, depending on Blender's empty draw type:

- Single arrow will create a [SeparationRayShape3D](../godot_csharp_misc.md).
- Cube will create a [BoxShape3D](../godot_csharp_misc.md).
- Image will create a [WorldBoundaryShape3D](../godot_csharp_misc.md).
- Sphere (and the others not listed) will create a [SphereShape3D](../godot_csharp_misc.md).

When possible, **try to use a few primitive collision shapes** instead of triangle mesh or convex shapes. Primitive shapes often have the best performance and reliability.

> **Note:** For better visibility on Blender's editor, you can set the "X-Ray" option on collision empties and set some distinct color for them by changing **Edit > Preferences > Themes > 3D Viewport > Empty**. If using Blender 2.79 or older, follow these steps instead: **User Preferences > Themes > 3D View > Empty**.

> **See also:** See [Collision shapes (3D)](tutorials_physics.md) for a comprehensive overview of collision shapes.

### Create Occluder (-occ, -occonly)

If a mesh is imported with the `-occ` suffix an [Occluder3D](../godot_csharp_resources.md) node will be created based on the geometry of the mesh, it does not replace the mesh. A mesh node with the `-occonly` suffix will be converted to an [Occluder3D](../godot_csharp_resources.md) on import.

### Create navigation (-navmesh)

A mesh node with the `-navmesh` suffix will be converted to a navigation mesh. The original Mesh object will be removed at import-time.

### Create a VehicleBody (-vehicle)

A mesh node with the `-vehicle` suffix will be imported as a child to a [VehicleBody3D](../godot_csharp_nodes_3d.md) node.

### Create a VehicleWheel (-wheel)

A mesh node with the `-wheel` suffix will be imported as a child to a [VehicleWheel3D](../godot_csharp_nodes_3d.md) node.

### Rigid Body (-rigid)

A mesh node with the `-rigid` suffix will be imported as a [RigidBody3D](../godot_csharp_nodes_3d.md).

### Animation loop (-loop, -cycle)

Animation clips in the source 3D file that start or end with the token `loop` or `cycle` will be imported as a Godot [Animation](../godot_csharp_resources.md) with the loop flag set. **Unlike the other suffixes described above, this does not require a hyphen.**

In Blender, this requires using the NLA Editor and naming the Action with the `loop` or `cycle` prefix or suffix.

### Material alpha (-alpha)

A material with the `-alpha` suffix will be imported with the [TRANSPARENCY_ALPHA](../godot_csharp_misc.md) transparency mode.

### Material vertex color (-vcol)

A material with the `-vcol` suffix will be imported with the [FLAG_ALBEDO_FROM_VERTEX_COLOR](../godot_csharp_misc.md) and [FLAG_SRGB_VERTEX_COLOR](../godot_csharp_misc.md) flags set.

---
