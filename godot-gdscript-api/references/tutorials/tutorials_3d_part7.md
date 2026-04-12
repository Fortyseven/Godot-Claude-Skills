# Godot 4 GDScript Tutorials — 3D (Part 7)

> 7 tutorials. GDScript-specific code examples.

## Physical light and camera units

### Why use physical light and camera units?

Godot uses arbitrary units for many physical properties that apply to light like color, energy, camera field of view, and exposure. By default, these properties use arbitrary units, because using accurate physical units comes with a few tradeoffs that aren't worth it for many games. As Godot favors ease of use by default, physical light units are disabled by default.

#### Advantages of physical units

If you aim for photorealism in your project, using real world units as a basis can help make things easier to adjust. References for real world materials, lights and scene brightness are wildly available on websites such as [Physically Based](https://physicallybased.info/).

Using real world units in Godot can also be useful when porting a scene from other 3D software that uses physical light units (such as Blender).

#### Disadvantages of physical units

The biggest disadvantage of using physical light units is you will have to pay close attention to the dynamic range in use at a given time. You can run into floating point precision errors when mixing very high light intensities with very low light intensities.

In practice, this means that you will have to manually manage your exposure settings to ensure that you aren't over-exposing or under-exposing your scene too much. Auto-exposure can help you balance the light in a scene to bring it into a normal range, but it can't recover lost precision from a dynamic range that is too high.

Using physical light and camera units will not automatically make your project look _better_. Sometimes, moving away from realism can actually make a scene look better to the human eye. Also, using physical units requires a greater amount of rigor compared to non-physical units. Most benefits of physical units can only be obtained if the units are correctly set to match real world reference.

> **Note:** Physical light units are only available in 3D rendering, not 2D.

### Setting up physical light units

Physical light units can be enabled separately from physical camera units.

To enable physical light units correctly, there are 4 steps required:

1. Enable the project setting.
2. Configure the camera.
3. Configure the environment.
4. Configure Light3D nodes.

Since physical light and camera units only require a handful of calculations to handle unit conversion, enabling them doesn't have any noticeable performance impact on the CPU. However, on the GPU side, physical camera units currently enforce depth of field. This has a moderate performance impact. To alleviate this performance impact, depth of field quality can be decreased in the advanced Project Settings.

#### Enable the project setting

Open the Project Settings, enable the **Advanced** toggle then enable **Rendering > Lights And Shadows > Use Physical Light Units**. Restart the editor.

#### Configure the camera

> **Warning:** When physical light units are enabled and if you have a WorldEnvironment node in your scene (i.e. the editor Environment is disabled), you **must** have a [CameraAttributes](../godot_gdscript_rendering.md) resource assigned to the WorldEnvironment node. Otherwise, the 3D editor viewport will appear extremely bright if you have a visible DirectionalLight3D node.

On the Camera3D node, you can add a [CameraAttributes](../godot_gdscript_rendering.md) resource to its **Attributes** property. This resource is used to control the camera's depth of field and exposure. When using [CameraAttributesPhysical](../godot_gdscript_rendering.md), its focal length property is also used to adjust the camera's field of view.

When physical light units are enabled, the following additional properties become available in CameraAttributesPhysical's **Exposure** section:

- **Aperture:** The size of the aperture of the camera, measured in f-stops. An f-stop is a unitless ratio between the focal length of the camera and the diameter of the aperture. A high aperture setting will result in a smaller aperture which leads to a dimmer image and sharper focus. A low aperture results in a wide aperture which lets in more light resulting in a brighter, less-focused image.
- **Shutter Speed:** The time for shutter to open and close, measured in _inverse seconds_ (`1/N`). A lower value will let in more light leading to a brighter image, while a higher value will let in less light leading to a darker image. _When getting or setting this property with a script, the unit is in seconds instead of inverse seconds._
- **Sensitivity:** The sensitivity of camera sensors, measured in ISO. A higher sensitivity results in a brighter image. When auto exposure is enabled, this can be used as a method of exposure compensation. Doubling the value will increase the exposure value (measured in EV100) by 1 stop.
- **Multiplier:** A _non-physical_ exposure multiplier. Higher values will increase the scene's brightness. This can be used for post-processing adjustments or for animation purposes.

The default **Aperture** value of 16 f-stops is appropriate for outdoors at daytime (i.e. for use with a default DirectionalLight3D). For indoor lighting, a value between 2 and 4 is more appropriate.

Typical shutter speed used in photography and movie production is 1/50 (0.02 seconds). Night-time photography generally uses a shutter around 1/10 (0.1 seconds), while sports photography uses a shutter speed between 1/250 (0.004 seconds) and 1/1000 (0.001 seconds) to reduce motion blur.

In real life, sensitivity is usually set between 50 ISO and 400 ISO for daytime outdoor photography depending on weather conditions. Higher values are used for indoor or night-time photography.

> **Note:** Unlike real life cameras, the adverse effects of increasing ISO sensitivity or decreasing shutter speed (such as visible grain or light trails) are not simulated in Godot.

See **Setting up physical camera units** for a description of CameraAttributesPhysical properties that are also available when **not** using physical light units.

#### Configure the environment

> **Warning:** The default configuration is designed for daytime outdoor scenes. Night-time and indoor scenes will need adjustments to the DirectionalLight3D and WorldEnvironment background intensity to look correct. Otherwise, positional lights will be barely visible at their default intensity.

If you haven't added a [WorldEnvironment](../godot_gdscript_nodes_3d.md) and [Camera3D](../godot_gdscript_nodes_3d.md) node to the current scene yet, do so now by clicking the 3 vertical dots at the top of the 3D editor viewport. Click **Add Sun to Scene**, open the dialog again then click **Add Environment to Scene**.

After enabling physical light units, a new property becomes available to edit in the [Environment](../godot_gdscript_rendering.md) resource:

- **Background Intensity:** The background sky's intensity in [nits](https://en.wikipedia.org/wiki/Candela_per_square_metre) (candelas per square meter). This also affects ambient and reflected light if their respective modes are set to **Background**. If a custom **Background Energy** is set, this energy is multiplied by the intensity.

#### Configure the light nodes

After enabling physical light units, 2 new properties become available in Light3D nodes:

- **Intensity:** The light's intensity in [lux](https://en.wikipedia.org/wiki/Lux) (DirectionalLight3D) or [lumens](<https://en.wikipedia.org/wiki/Lumen_(unit)>) (OmniLight3D/SpotLight3D). If a custom **Energy** is set, this energy is multiplied by the intensity.
- **Temperature:** The light's _color temperature_ defined in Kelvin. If a custom **Color** is set, this color is multiplied by the color temperature.

**OmniLight3D/SpotLight3D intensity**

Lumens are a measure of luminous flux, which is the total amount of visible light emitted by a light source per unit of time.

For SpotLight3Ds, we assume that the area outside the visible cone is surrounded by a perfect light absorbing material. Accordingly, the apparent brightness of the cone area does _not_ change as the cone increases and decreases in size.

A typical household lightbulb can range from around 600 lumens to 1200 lumens. A candle is about 13 lumens, while a streetlight can be approximately 60000 lumens.

**DirectionalLight3D intensity**

Lux is a measure pf luminous flux per unit area, it is equal to one lumen per square metre. Lux is the measure of how much light hits a surface at a given time.

With DirectionalLight3D, on a clear sunny day, a surface in direct sunlight may receive approximately 100000 lux. A typical room in a home may receive approximately 50 lux, while the moonlit ground may receive approximately 0.1 lux.

**Color temperature**

6500 Kelvin is white. Higher values result in colder (bluer) colors, while lower values result in warmer (more orange) colors.

The sun on a cloudy day is approximately 6500 Kelvin. On a clear day, the sun is between 5500 to 6000 Kelvin. On a clear day at sunrise or sunset, the sun ranges to around 1850 Kelvin.

Other Light3D properties such as **Energy** and **Color** remain editable for animation purposes, and when you occasionally need to create lights with non-realistic properties.

### Setting up physical camera units

Physical camera units can be enabled separately from physical light units.

After adding a [CameraAttributesPhysical](../godot_gdscript_rendering.md) resource to the **Camera Attributes** property of a Camera3D nodes, some properties such as **FOV** will no longer be editable. Instead, these properties are now governed by the CameraAttributesPhysical's properties, such as focal length and aperture.

CameraAttributesPhysical offers the following properties in its **Frustum** section:

- **Focus Distance:** Distance from camera of object that will be in focus, measured in meters. Internally, this will be clamped to be at least 1 millimeter larger than the **Focal Length**.
- **Focal Length:** Distance between camera lens and camera aperture, measured in millimeters. Controls field of view and depth of field. A larger focal length will result in a smaller field of view and a narrower depth of field meaning fewer objects will be in focus. A smaller focal length will result in a wider field of view and a larger depth of field, which means more objects will be in focus. This property overrides the Camera3D's **FOV** and **Keep Aspect** properties, making them read-only in the inspector.
- **Near/Far:** The near and far clip distances in meters. These behave the same as the Camera3D properties of the same name. Lower **Near** values allow the camera to display objects that are very close, at the cost of potential precision (Z-fighting) issues in the distance. Higher **Far** values allow the camera to see further away, also at the cost of potential precision (Z-fighting) issues in the distance.

The default focal length of 35 mm corresponds to a wide angle lens. It still results in a field of view that is noticeably narrower compared to the default "practical" vertical FOV of 75 degrees. This is because non-gaming use cases such as filmmaking and photography favor using a narrower field of view for a more cinematic appearance.

Common focal length values used in filmmaking and photography are:

- **Fisheye (ultrawide angle):** Below 15 mm. Nearly no depth of field visible.
- **Wide angle:** Between 15 mm and 50 mm. Reduced depth of field.
- **Standard:** Between 50 mm and 100 mm. Standard depth of field.
- **Telephoto:** Greater than 100 mm. Increased depth of field.

Like when using the **Keep Height** aspect mode, the effective field of view depends on the viewport's aspect ratio, with wider aspect ratios automatically resulting in a wider _horizontal_ field of view.

Automatic exposure adjustment based on the camera's average brightness level can also be enabled in the **Auto Exposure** section, with the following properties:

- **Min Sensitivity:** The darkest brightness the camera is allowed to get to, measured in EV100.
- **Max Sensitivity:** The brightest the camera is allowed to get to, measured in EV100.
- **Speed:** The speed of the auto exposure effect. Affects the time needed for the camera to perform auto exposure. Higher values allow for faster transitions, but the resulting adjustments may look distracting depending on the scene.
- **Scale:** The scale of the auto exposure effect. Affects the intensity of auto exposure.

EV100 is an exposure value (EV) measured at an ISO sensitivity of 100. See [this table](https://en.wikipedia.org/wiki/Exposure_value#Tabulated_exposure_values) for common EV100 values found in real life.

---

## Using the ArrayMesh

This tutorial will present the basics of using an [ArrayMesh](../godot_gdscript_rendering.md).

To do so, we will use the function [add_surface_from_arrays()](../godot_gdscript_misc.md), which takes up to five parameters. The first two are required, while the last three are optional.

The first parameter is the `PrimitiveType`, an OpenGL concept that instructs the GPU how to arrange the primitive based on the vertices given, i.e. whether they represent triangles, lines, points, etc. See [Mesh.PrimitiveType](../godot_gdscript_misc.md) for the options available.

The second parameter, `arrays`, is the actual Array that stores the mesh information. The array is a normal Godot array that is constructed with empty brackets `[]`. It stores a `Packed**Array` (e.g. PackedVector3Array, PackedInt32Array, etc.) for each type of information that will be used to build the surface.

Common elements of `arrays` are listed below, together with the position they must have within `arrays`. See [Mesh.ArrayType](../godot_gdscript_misc.md) for a full list.

| Index | Mesh.ArrayType Enum | Array type                                                                                                                                                         |
| ----- | ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 0     | ARRAY_VERTEX        | PackedVector3Array or PackedVector2Array                                                                                                                           |
| 1     | ARRAY_NORMAL        | PackedVector3Array                                                                                                                                                 |
| 2     | ARRAY_TANGENT       | PackedFloat32Array or PackedFloat64Array of groups of 4 floats. The first 3 floats determine the tangent, and the last float the binormal direction as -1 or 1.    |
| 3     | ARRAY_COLOR         | PackedColorArray                                                                                                                                                   |
| 4     | ARRAY_TEX_UV        | PackedVector2Array or PackedVector3Array                                                                                                                           |
| 5     | ARRAY_TEX_UV2       | PackedVector2Array or PackedVector3Array                                                                                                                           |
| 10    | ARRAY_BONES         | PackedFloat32Array of groups of 4 floats or PackedInt32Array of groups of 4 ints. Each group lists indexes of 4 bones that affects a given vertex.                 |
| 11    | ARRAY_WEIGHTS       | PackedFloat32Array or PackedFloat64Array of groups of 4 floats. Each float lists the amount of weight the corresponding bone in ARRAY_BONES has on a given vertex. |
| 12    | ARRAY_INDEX         | PackedInt32Array                                                                                                                                                   |

In most cases when creating a mesh, we define it by its vertex positions. So usually, the array of vertices (at index 0) is required, while the index array (at index 12) is optional and will only be used if included. It is also possible to create a mesh with only the index array and no vertex array, but that's beyond the scope of this tutorial.

All the other arrays carry information about the vertices. They are optional and will only be used if included. Some of these arrays (e.g. `ARRAY_COLOR`) use one entry per vertex to provide extra information about vertices. They must have the same size as the vertex array. Other arrays (e.g. `ARRAY_TANGENT`) use four entries to describe a single vertex. These must be exactly four times larger than the vertex array.

For normal usage, the last three parameters in [add_surface_from_arrays()](../godot_gdscript_misc.md) are typically left empty.

### Setting up the ArrayMesh

In the editor, create a [MeshInstance3D](../godot_gdscript_nodes_3d.md) and add an [ArrayMesh](../godot_gdscript_rendering.md) to it in the Inspector. Normally, adding an ArrayMesh in the editor is not useful, but in this case it allows us to access the ArrayMesh from code without creating one.

Next, add a script to the MeshInstance3D.

Under `_ready()`, create a new Array.

```gdscript
var surface_array = []
```

This will be the array that we keep our surface information in - it will hold all the arrays of data that the surface needs. Godot will expect it to be of size `Mesh.ARRAY_MAX`, so resize it accordingly.

```gdscript
var surface_array = []
surface_array.resize(Mesh.ARRAY_MAX)
```

Next create the arrays for each data type you will use.

```gdscript
var verts = PackedVector3Array()
var uvs = PackedVector2Array()
var normals = PackedVector3Array()
var indices = PackedInt32Array()
```

Once you have filled your data arrays with your geometry you can create a mesh by adding each array to `surface_array` and then committing to the mesh.

```gdscript
surface_array[Mesh.ARRAY_VERTEX] = verts
surface_array[Mesh.ARRAY_TEX_UV] = uvs
surface_array[Mesh.ARRAY_NORMAL] = normals
surface_array[Mesh.ARRAY_INDEX] = indices

# No blendshapes, lods, or compression used.
mesh.add_surface_from_arrays(Mesh.PRIMITIVE_TRIANGLES, surface_array)
```

> **Note:** In this example, we used `Mesh.PRIMITIVE_TRIANGLES`, but you can use any primitive type available from mesh.

Put together, the full code looks like:

```gdscript
extends MeshInstance3D

func _ready():
    var surface_array = []
    surface_array.resize(Mesh.ARRAY_MAX)

    # PackedVector**Arrays for mesh construction.
    var verts = PackedVector3Array()
    var uvs = PackedVector2Array()
    var normals = PackedVector3Array()
    var indices = PackedInt32Array()

    #######################################
    ## Insert code here to generate mesh ##
    #######################################

    # Assign arrays to surface array.
    surface_array[Mesh.ARRAY_VERTEX] = verts
    surface_array[Mesh.ARRAY_TEX_UV] = uvs
    surface_array[Mesh.ARRAY_NORMAL] = normals
    surface_array[Mesh.ARRAY_INDEX] = indices

    # Create mesh surface from mesh array.
    # No blendshapes, lods, or compression used.
    mesh.add_surface_from_arrays(Mesh.PRIMITIVE_
# ...
```

The code that goes in the middle can be whatever you want. Below we will present some example code for generating shapes, starting with a rectangle.

### Generating a rectangle

Since we are using `Mesh.PRIMITIVE_TRIANGLES` to render, we will construct a rectangle with triangles.

A rectangle is formed by two triangles sharing four vertices. For our example, we will create a rectangle with its top left point at `(0, 0, 0)` with a width and length of one as shown below:

To draw this rectangle, define the coordinates of each vertex in the `verts` array.

```gdscript
verts = PackedVector3Array([
        Vector3(0, 0, 0),
        Vector3(0, 0, 1),
        Vector3(1, 0, 0),
        Vector3(1, 0, 1),
    ])
```

The `uvs` array helps describe where parts of a texture should go onto the mesh. The values range from 0 to 1. Depending on your texture, you may want to change these values.

```gdscript
uvs = PackedVector2Array([
        Vector2(0, 0),
        Vector2(1, 0),
        Vector2(0, 1),
        Vector2(1, 1),
    ])
```

The `normals` array is used to describe the direction the vertices face and is used in lighting calculations. For this example, we will default to the `Vector3.UP` direction.

```gdscript
normals = PackedVector3Array([
        Vector3.UP,
        Vector3.UP,
        Vector3.UP,
        Vector3.UP,
    ])
```

The `indices` array defines the order vertices are drawn. Godot renders in a _clockwise_ direction, meaning that we must specify the vertices of a triangle we want to draw in clockwise order.

For example, to draw the first triangle, we will want to draw the vertices `(0, 0, 0)`, `(1, 0, 0)`, and `(0, 0, 1)` in that order. This is the same as drawing `vert[0]`, `vert[2]`, and `vert[1]`, i.e., indices 0, 2, and 1, in the `verts` array. These index values are what the `indices` array defines.

| Index | verts[Index] | uvs[Index] | normals[Index] |
| ----- | ------------ | ---------- | -------------- |
| 0     | (0, 0, 0)    | (0, 0)     | Vector3.UP     |
| 1     | (0, 0, 1)    | (1, 0)     | Vector3.UP     |
| 2     | (1, 0, 0)    | (0, 1)     | Vector3.UP     |
| 3     | (1, 0, 1)    | (1, 1)     | Vector3.UP     |

```gdscript
indices = PackedInt32Array([
        0, 2, 1, # Draw the first triangle.
        2, 3, 1, # Draw the second triangle.
    ])
```

Put together, the rectangle generation code looks like:

```gdscript
extends MeshInstance3D

func _ready():

  # Insert setting up the PackedVector**Arrays here.

  verts = PackedVector3Array([
          Vector3(0, 0, 0),
          Vector3(0, 0, 1),
          Vector3(1, 0, 0),
          Vector3(1, 0, 1),
      ])

  uvs = PackedVector2Array([
          Vector2(0, 0),
          Vector2(1, 0),
          Vector2(0, 1),
          Vector2(1, 1),
      ])

  normals = PackedVector3Array([
          Vector3.UP,
          Vector3.UP,
          Vector3.UP,
          Vector3.UP,
      ])

  indices = PackedInt32Array([
          0, 2, 1,
          2, 3, 1,
      ])

  # Insert committing to the ArrayMesh here.
```

For a more complex example, see the sphere generation section below.

### Generating a sphere

Here is sample code for generating a sphere. Although the code is presented in GDScript, there is nothing Godot specific about the approach to generating it. This implementation has nothing in particular to do with ArrayMeshes and is just a generic approach to generating a sphere. If you are having trouble understanding it or want to learn more about procedural geometry in general, you can use any tutorial that you find online.

```gdscript
extends MeshInstance3D

var rings = 50
var radial_segments = 50
var radius = 1

func _ready():

    # Insert setting up the PackedVector**Arrays here.

    # Vertex indices.
    var thisrow = 0
    var prevrow = 0
    var point = 0

    # Loop over rings.
    for i in range(rings + 1):
        var v = float(i) / rings
        var w = sin(PI * v)
        var y = cos(PI * v)

        # Loop over segments in ring.
        for j in range(radial_segments + 1):
            var u = float(j) / radial_segments
            var x = sin(u * PI * 2.0)
            var z = cos(u * PI * 2.0)
            var vert = Vector3(x * radius * w, y * radius, z * radius * w)
            verts.append(vert)
            normals.append(vert.normalized())
            uvs.append(Vector2(u, v))
            point += 1


# ...
```

### Saving

Finally, we can use the [ResourceSaver](../godot_gdscript_core.md) class to save the ArrayMesh. This is useful when you want to generate a mesh and then use it later without having to re-generate it.

```gdscript
# Saves mesh to a .tres file with compression enabled.
ResourceSaver.save(mesh, "res://sphere.tres", ResourceSaver.FLAG_COMPRESS)
```

---

## Using ImmediateMesh

The [ImmediateMesh](../godot_gdscript_rendering.md) is a convenient tool to create dynamic geometry using an OpenGL 1.x-style API. Which makes it both approachable to use and efficient for meshes which need to be updated every frame.

Generating complex geometry (several thousand vertices) with this tool is inefficient, even if it's done only once. Instead, it is designed to generate simple geometry that changes every frame.

First, you need to create a [MeshInstance3D](../godot_gdscript_nodes_3d.md) and add an [ImmediateMesh](../godot_gdscript_rendering.md) to it in the Inspector.

Next, add a script to the MeshInstance3D. The code for the ImmediateMesh should go in the `_process()` function if you want it to update each frame, or in the `_ready()` function if you want to create the mesh once and not update it. If you only generate a surface once, the ImmediateMesh is just as efficient as any other kind of mesh as the generated mesh is cached and reused.

To begin generating geometry you must call `surface_begin()`. `surface_begin()` takes a `PrimitiveType` as an argument. `PrimitiveType` instructs the GPU how to arrange the primitive based on the vertices given whether it is triangles, lines, points, etc. A complete list can be found under the [Mesh](../godot_gdscript_rendering.md) class reference page.

Once you have called `surface_begin()` you are ready to start adding vertices. You add vertices one at a time. First you add vertex specific attributes such as normals or UVs using `surface_set_****()` (e.g. `surface_set_normal()`). Then you call `surface_add_vertex()` to add a vertex with those attributes. For example:

```gdscript
# Add a vertex with normal and uv.
surface_set_normal(Vector3(0, 1, 0))
surface_set_uv(Vector2(1, 1))
surface_add_vertex(Vector3(0, 0, 1))
```

Only attributes added before the call to `surface_add_vertex()` will be included in that vertex. If you add an attribute twice before calling `surface_add_vertex()`, only the second call will be used.

Finally, once you have added all your vertices call `surface_end()` to signal that you have finished generating the surface. You can call `surface_begin()` and `surface_end()` multiple times to generate multiple surfaces for the mesh.

The example code below draws a single triangle in the `_ready()` function.

```gdscript
extends MeshInstance3D

func _ready():
    # Begin draw.
    mesh.surface_begin(Mesh.PRIMITIVE_TRIANGLES)

    # Prepare attributes for add_vertex.
    mesh.surface_set_normal(Vector3(0, 0, 1))
    mesh.surface_set_uv(Vector2(0, 0))
    # Call last for each vertex, adds the above attributes.
    mesh.surface_add_vertex(Vector3(-1, -1, 0))

    mesh.surface_set_normal(Vector3(0, 0, 1))
    mesh.surface_set_uv(Vector2(0, 1))
    mesh.surface_add_vertex(Vector3(-1, 1, 0))

    mesh.surface_set_normal(Vector3(0, 0, 1))
    mesh.surface_set_uv(Vector2(1, 1))
    mesh.surface_add_vertex(Vector3(1, 1, 0))

    # End drawing.
    mesh.surface_end()
```

The ImmediateMesh can also be used across frames. Each time you call `surface_begin()` and `surface_end()`, you are adding a new surface to the ImmediateMesh. If you want to recreate the mesh from scratch each frame, call `clear_surfaces()` before calling `surface_begin()`.

```gdscript
extends MeshInstance3D

func _process(delta):

    # Clean up before drawing.
    mesh.clear_surfaces()

    # Begin draw.
    mesh.surface_begin(Mesh.PRIMITIVE_TRIANGLES)

    # Draw mesh.

    # End drawing.
    mesh.surface_end()
```

The above code will dynamically create and draw a single surface each frame.

---

## Using the MeshDataTool

The [MeshDataTool](../godot_gdscript_rendering.md) is not used to generate geometry. But it is helpful for dynamically altering geometry, for example if you want to write a script to tessellate, simplify, or deform meshes.

The MeshDataTool is not as fast as altering arrays directly using [ArrayMesh](../godot_gdscript_rendering.md). However, it provides more information and tools to work with meshes than the ArrayMesh does. When the MeshDataTool is used, it calculates mesh data that is not available in ArrayMeshes such as faces and edges, which are necessary for certain mesh algorithms. If you do not need this extra information then it may be better to use an ArrayMesh.

> **Note:** MeshDataTool can only be used on Meshes that use the PrimitiveType `Mesh.PRIMITIVE_TRIANGLES`.

We initialize the MeshDataTool from an ArrayMesh by calling [create_from_surface()](../godot_gdscript_misc.md). If there is already data initialized in the MeshDataTool, calling `create_from_surface()` will clear it for you. Alternatively, you can call [clear()](../godot_gdscript_misc.md) yourself before re-using the MeshDataTool.

In the examples below, assume an ArrayMesh called `mesh` has already been created. See ArrayMesh tutorial for an example of mesh generation.

```gdscript
var mdt = MeshDataTool.new()
mdt.create_from_surface(mesh, 0)
```

`create_from_surface()` uses the vertex arrays from the ArrayMesh to calculate two additional arrays, one for edges and one for faces, for a total of three arrays.

An edge is a connection between any two vertices. Each edge in the edge array contains a reference to the two vertices it is composed of, and up to two faces that it is contained within.

A face is a triangle made up of three vertices and three corresponding edges. Each face in the face array contains a reference to the three vertices and three edges it is composed of.

The vertex array contains edge, face, normal, color, tangent, uv, uv2, bone, and weight information connected with each vertex.

To access information from these arrays you use a function of the form `get_****()`:

```gdscript
mdt.get_vertex_count() # Returns the number of vertices in the vertex array.
mdt.get_vertex_faces(0) # Returns an array of faces that contain vertex[0].
mdt.get_face_normal(1) # Calculates and returns the face normal of the second face.
mdt.get_edge_vertex(10, 1) # Returns the second vertex comprising the edge at index 10.
```

What you choose to do with these functions is up to you. A common use case is to iterate over all vertices and transform them in some way:

```gdscript
for i in range(mdt.get_vertex_count()):
    var vert = mdt.get_vertex(i)
    vert *= 2.0 # Scales the vertex by doubling its size.
    mdt.set_vertex(i, vert)
```

These modifications are not done in place on the ArrayMesh. If you are dynamically updating an existing ArrayMesh, first delete the existing surface before adding a new one using [commit_to_surface()](../godot_gdscript_misc.md):

```gdscript
mesh.clear_surfaces() # Deletes all of the mesh's surfaces.
mdt.commit_to_surface(mesh)
```

Below is a complete example that turns a spherical mesh called `mesh` into a randomly deformed blob complete with updated normals and vertex colors. See ArrayMesh tutorial for how to generate the base mesh.

```gdscript
extends MeshInstance3D

var fnl = FastNoiseLite.new()
var mdt = MeshDataTool.new()

func _ready():
    fnl.frequency = 0.7

    mdt.create_from_surface(mesh, 0)

    for i in range(mdt.get_vertex_count()):
        var vertex = mdt.get_vertex(i).normalized()
        # Scale the vertices using noise.
        vertex = vertex * (fnl.get_noise_3dv(vertex) * 0.5 + 0.75)
        mdt.set_vertex(i, vertex)

    # Calculate the vertex normals, face-by-face.
    for i in range(mdt.get_face_count()):
        # Get the index in the vertex array.
        var a = mdt.get_face_vertex(i, 0)
        var b = mdt.get_face_vertex(i, 1)
        var c = mdt.get_face_vertex(i, 2)
        # Get the vertex position using the vertex index.
        var ap = mdt.get_vertex(a)
        var bp = mdt.get_vertex(b)

# ...
```

---

## Using the SurfaceTool

The [SurfaceTool](../godot_gdscript_rendering.md) provides a useful interface for constructing geometry. The interface is similar to the [ImmediateMesh](../godot_gdscript_rendering.md) class. You set each per-vertex attribute (e.g. normal, uv, color) and then when you add a vertex it captures the attributes.

The SurfaceTool also provides some useful helper functions like `index()` and `generate_normals()`.

Attributes are added before each vertex is added:

```gdscript
var st = SurfaceTool.new()

st.begin(Mesh.PRIMITIVE_TRIANGLES)

st.set_normal() # Overwritten by normal below.
st.set_normal() # Added to next vertex.
st.set_color() # Added to next vertex.
st.add_vertex() # Captures normal and color above.
st.set_normal() # Normal never added to a vertex.
```

When finished generating your geometry with the [SurfaceTool](../godot_gdscript_rendering.md), call `commit()` to finish generating the mesh. If an [ArrayMesh](../godot_gdscript_rendering.md) is passed to `commit()`, then it appends a new surface to the end of the ArrayMesh. While if nothing is passed in, `commit()` returns an ArrayMesh.

```gdscript
# Add surface to existing ArrayMesh.
st.commit(mesh)

# -- Or Alternatively --

# Create new ArrayMesh.
var mesh = st.commit()
```

The code below creates a triangle without indices.

```gdscript
var st = SurfaceTool.new()

st.begin(Mesh.PRIMITIVE_TRIANGLES)

# Prepare attributes for add_vertex.
st.set_normal(Vector3(0, 0, 1))
st.set_uv(Vector2(0, 0))
# Call last for each vertex, adds the above attributes.
st.add_vertex(Vector3(-1, -1, 0))

st.set_normal(Vector3(0, 0, 1))
st.set_uv(Vector2(0, 1))
st.add_vertex(Vector3(-1, 1, 0))

st.set_normal(Vector3(0, 0, 1))
st.set_uv(Vector2(1, 1))
st.add_vertex(Vector3(1, 1, 0))

# Commit to a mesh.
var mesh = st.commit()
```

You can optionally add an index array, either by calling `add_index()` and adding vertices to the index array manually, or by calling `index()` once, which generates the index array automatically and shrinks the vertex array to remove duplicate vertices.

```gdscript
# Suppose we have a quad defined by 6 vertices as follows
st.add_vertex(Vector3(-1, 1, 0))
st.add_vertex(Vector3(1, 1, 0))
st.add_vertex(Vector3(-1, -1, 0))

st.add_vertex(Vector3(1, 1, 0))
st.add_vertex(Vector3(1, -1, 0))
st.add_vertex(Vector3(-1, -1, 0))

# We can make the quad more efficient by using an index array and only utilizing 4 vertices:

st.add_vertex(Vector3(-1, 1, 0))
st.add_vertex(Vector3(1, 1, 0))
st.add_vertex(Vector3(-1, -1, 0))
st.add_vertex(Vector3(1, -1, 0))

# Creates a quad from four corner vertices.
# add_index() can be called before or after add_vertex()
# since it's not an attribute of a vertex itself.
st.add_index(0)
st.add_index(1)
st.add_index(2)

st.add_index(1)
st.add_index(3)
st.add_index(2)

# Alternatively we can use ``st.index()`` which will create the qu
# ...
```

Similarly, if you have an index array, but you want each vertex to be unique (e.g. because you want to use unique normals or colors per face instead of per-vertex), you can call `deindex()`.

```gdscript
st.deindex()
```

If you don't add custom normals yourself, you can add them using `generate_normals()`, which should be called after generating geometry and before committing the mesh using `commit()` or `commit_to_arrays()`. Calling `generate_normals(true)` will flip the resulting normals. As a side note, `generate_normals()` only works if the primitive type is set to `Mesh.PRIMITIVE_TRIANGLES`.

You may notice that normal mapping or other material properties look broken on the generated mesh. This is because normal mapping **requires** the mesh to feature _tangents_, which are separate from _normals_. You can either add custom tangents manually, or generate them automatically with `generate_tangents()`. This method requires that each vertex have UVs and normals set already.

```gdscript
st.generate_normals()
st.generate_tangents()

st.commit(mesh)
```

By default, when generating normals, they will be calculated on a per-vertex basis (i.e. they will be "smooth normals"). If you want flat vertex normals (i.e. a single normal vector per face), when adding vertices, call `add_smooth_group(i)` where `i` is a unique number per vertex. `add_smooth_group()` needs to be called while building the geometry, e.g. before the call to `add_vertex()`.

---

## Resolution scaling

### Why use resolution scaling?

With the ever-increasing rendering complexity of modern games, rendering at native resolution isn't always viable anymore, especially on lower-end GPUs.

Resolution scaling is one of the most direct ways to influence the GPU requirements of a scene. In scenes that are bottlenecked by the GPU (rather than by the CPU), decreasing the resolution scale can improve performance significantly. Resolution scaling is particularly important on mobile GPUs where performance and power budgets are limited.

While resolution scaling is an important tool to have, remember that resolution scaling is not intended to be a replacement for decreasing graphics settings on lower-end hardware. Consider exposing both resolution scale and graphics settings in your in-game menus.

> **See also:** You can compare resolution scaling modes and factors in action using the [3D Antialiasing demo project](https://github.com/godotengine/godot-demo-projects/tree/master/3d/antialiasing).

> **Note:** Resolution scaling is currently not available for 2D rendering, but it can be simulated using the `viewport` stretch mode. See [Multiple resolutions](tutorials_rendering.md) for more information.

### Resolution scaling options

In the advanced Project Settings' **Rendering > Scaling 3D** section, you can find several options for 3D resolution scaling:

#### Scaling mode

- **Bilinear:** Standard bilinear filtering (default). This is used as a fallback when the current renderer doesn't support FSR 1.0 or FSR 2.2. _Available in all renderers._
- **FSR 1.0:** [AMD FidelityFX Super Resolution 1.0](https://gpuopen.com/fidelityfx-superresolution/). Slower, but higher quality compared to bilinear scaling. On very slow GPUs, the cost of FSR1 may be too expensive to be worth using it over bilinear scaling. _Only available when using the Forward+ renderer._
- **FSR 2.2:** AMD FidelityFX Super Resolution 2.2 (since Godot 4.2). Slowest, but even higher quality compared to FSR1 and bilinear scaling. On slow GPUs, the cost of FSR2 may be too expensive to be worth using it over bilinear scaling or FSR1. To match FSR2 performance with FSR1, you need to use a lower resolution scale factor. _Only available when using the Forward+ renderer._

Here are comparison images between native resolution, bilinear scaling with 50% resolution scale, FSR1, and FSR2 scaling with 50% resolution scale:

FSR1 upscaling works best when coupled with another form of antialiasing. Temporal antialiasing (TAA) or multisample antialiasing (MSAA) should preferably be used in this case, as FXAA does not add temporal information and introduces more blurring to the image.

On the other hand, FSR2 provides its own temporal antialiasing. This means you don't need to enable other antialiasing methods for the resulting image to look smooth. The **Use TAA** project setting is ignored when FSR2 is used as the 3D scaling method, since FSR2's temporal antialiasing takes priority.

Here's the same comparison, but with 4× MSAA enabled on all images:

Notice how the edge upscaling of FSR1 becomes much more convincing once 4× MSAA is enabled. However, FSR2 doesn't benefit much from enabling MSAA since it already performs temporal antialiasing.

#### Rendering scale

The **Rendering > Scaling 3D > Scale** setting adjusts the resolution scale. `1.0` represents the full resolution scale, with the 3D rendering resolution matching the 2D rendering resolution. Resolution scales _below_ `1.0` can be used to speed up rendering, at the cost of a blurrier final image and more aliasing.

The rendering scale can be adjusted at runtime by changing the `scaling_3d_scale` property on a [Viewport](../godot_gdscript_rendering.md) node.

Resolution scales _above_ `1.0` can be used for supersample antialiasing (SSAA). This will provide antialiasing at a _very_ high performance cost, and is **not recommended** for most use cases. See 3D antialiasing for more information.

The tables below list common screen resolutions, the resulting 3D rendering resolution and the number of megapixels that need to be rendered each frame depending on the rendering scale option. Rows are sorted from fastest to slowest in each table.

> **Note:** The resolution scale is defined on a **per-axis** basis. For example, this means that halving the resolution scale factor will reduce the number of rendered megapixels per frame by a factor of 4, not 2. Therefore, very low or very high resolution scale factors can have a greater performance impact than expected.

**1920×1080 (Full HD)**

| Resolution scale factor | 3D rendering resolution | Megapixels rendered per frame |
| ----------------------- | ----------------------- | ----------------------------- |
| 0.50                    | 960×540                 | 0.52 MPix                     |
| 0.67                    | 1286×723                | 0.93 MPix                     |
| 0.75                    | 1440×810                | 1.17 MPix                     |
| 0.85                    | 1632×918                | 1.50 MPix                     |
| 1.00 (native)           | 1920×1080               | 2.07 MPix                     |
| 1.33 (supersampling)    | 2553×1436               | 3.67 MPix                     |
| 1.50 (supersampling)    | 2880×1620               | 4.67 MPix                     |
| 2.00 (supersampling)    | 3840×2160               | 8.29 MPix                     |

**2560×1440 (QHD)**

| Resolution scale factor | 3D rendering resolution | Megapixels rendered per frame |
| ----------------------- | ----------------------- | ----------------------------- |
| 0.50                    | 1280×720                | 0.92 MPix                     |
| 0.67                    | 1715×964                | 1.65 MPix                     |
| 0.75                    | 1920×1080               | 2.07 MPix                     |
| 0.85                    | 2176×1224               | 2.66 MPix                     |
| 1.00 (native)           | 2560×1440               | 3.69 MPix                     |
| 1.33 (supersampling)    | 3404×1915               | 6.52 MPix                     |
| 1.50 (supersampling)    | 3840×2160               | 8.29 MPix                     |
| 2.00 (supersampling)    | 5120×2880               | 14.75 MPix                    |

**3840×2160 (Ultra HD "4K")**

| Resolution scale factor | 3D rendering resolution | Megapixels rendered per frame |
| ----------------------- | ----------------------- | ----------------------------- |
| 0.50                    | 1920×1080               | 2.07 MPix                     |
| 0.67                    | 2572×1447               | 3.72 MPix                     |
| 0.75                    | 2880×1620               | 4.67 MPix                     |
| 0.85                    | 3264×1836               | 5.99 MPix                     |
| 1.00 (native)           | 3840×2160               | 8.29 MPix                     |
| 1.33 (supersampling)    | 5107×2872               | 14.67 MPix                    |
| 1.50 (supersampling)    | 5760×3240               | 18.66 MPix                    |
| 2.00 (supersampling)    | 7680×4320               | 33.18 MPix                    |

#### FSR Sharpness

_This is only available in the Forward+ renderer, not the Mobile or Compatibility renderers._

When using the FSR1 or FSR2 scaling modes, the sharpness can be controlled using the **Rendering > Scaling 3D > FSR Sharpness** advanced project setting.

The intensity is inverted compared to most other sharpness sliders: _lower_ values will result in a sharper final image, while _higher_ values will _reduce_ the impact of the sharpening filter. `0.0` is the sharpest, while `2.0` is the least sharp. The default value of `0.2` provides a balance between preserving the original image's sharpness and avoiding additional aliasing due to oversharpening.

> **Note:** If you wish to use sharpening when rendering at native resolution, Godot currently doesn't allow using the sharpening component of FSR1 (RCAS) independently from the upscaling component (EASU). As a workaround, you can set the 3D rendering scale to `0.99`, set the scaling mode to **FSR 1.0** then adjust FSR sharpness as needed. This allows using FSR1 while rendering at a near-native resolution. Alternatively, you can set the scaling mode to **FSR 2.2** with the 3D rendering scale set to `1.0` if you have enough GPU headroom. This also provides high-quality temporal antialiasing. The **FSR Sharpness** setting remains functional in this case.

#### Mipmap bias

_This is only available in the Forward+ and Mobile renderers, not the Compatibility renderer._

Godot automatically uses a negative texture mipmap bias when the 3D resolution scale is set below `1.0`. This allows for better preservation of texture detail at the cost of a grainy appearance on detailed textures.

The texture LOD bias currently affects both 2D and 3D rendering in the same way. However, keep in mind it only has an effect on textures with mipmaps enabled. Textures used in 2D don't have mipmaps enabled by default, which means only 3D rendering is affected unless you enabled mipmaps on 2D textures in the Import dock.

The formula used to determine the texture mipmap bias is: `log2f(min(scaling_3d_scale, 1.0)) + custom_texture_mipmap_bias`

To counteract the blurriness added by some antialiasing methods, Godot also adds a `-0.25` offset when FXAA is enabled, and a `-0.5` offset when TAA is enabled. If both are enabled at the same time, a `-0.75` offset is used. This mipmap bias offset is applied _before_ the resolution scaling offset, so it does not change depending on resolution scale.

The texture LOD bias can manually be changed by adjusting the **Rendering > Textures > Default Filters > Texture Mipmap Bias** advanced project setting. It can also be changed at runtime on [Viewports](../godot_gdscript_rendering.md) by adjusting the `texture_mipmap_bias` property.

> **Warning:** Adjusting the mipmap LOD bias manually can be useful in certain scenarios, but this should be done carefully to prevent the final image from looking grainy in motion. _Negative_ mipmap LOD bias can also decrease performance due to higher-resolution mips having to be sampled further away. Recommended values for a manual offset are between `-0.5` and `0.0`. _Positive_ mipmap LOD bias will make mipmapped textures appear blurrier than intended. This may improve performance slightly, but is otherwise not recommended as the loss in visual quality is usually not worth the performance gain.

The example below shows an extreme case, with a mipmap LOD bias of `-1.0` and anisotropic filtering disabled to make the difference more noticeable:

### Troubleshooting

#### Performance does not increase much when decreasing resolution scale

If performance doesn't increase much when decreasing resolution scale to a value like `0.5`, it likely means the performance bottleneck is elsewhere in your scene. For example, your scene could have too many draw calls, causing a CPU bottleneck to occur. Likewise, you may have too many graphics effects enabled for your GPU to handle (such as SDFGI, SSAO or SSR).

See the [Performance](tutorials_performance.md) tutorials for more information.

---

## Third-person camera with spring arm

### Introduction

3D games will often have a third-person camera that follows and rotates around something such as a player character or a vehicle.

In Godot, this can be done by setting a [Camera3D](../godot_gdscript_nodes_3d.md) as a child of a node. However, if you try this without any extra steps, you'll notice that the camera clips through geometry and hides the scene.

This is where the [SpringArm3D](../godot_gdscript_nodes_3d.md) node comes in.

### What is a spring arm?

A spring arm has two main components that affect its behavior.

The "length" of the spring arm is how far from its global position to check for collisions:

The "shape" of the spring arm is what it uses to check for collisions. The spring arm will "sweep" this shape from its origin out towards its length.

The spring arm tries to keep all of its children at the end of its length. When the shape collides with something, the children are instead placed at or near that collision point:

### Spring arm with a camera

When a camera is placed as a child of a spring arm, a pyramid representing the camera will be used as the shape.

This pyramid represents the **near plane** of the camera:

> **Note:** If the spring arm is given a specific shape, then that shape will **always** be used. The camera's shape is only used if the camera is a **direct child** of the spring arm. If no shape is provided and the camera is not a direct child, the spring arm will fall back to using a ray cast which is inaccurate for camera collisions and not recommended.

Every physics process frame, the spring arm will perform a motion cast to check if anything is collided with:

When the shape hits something, the camera will be placed at or near the collision point:

### Setting up the spring arm and camera

Let's add a spring arm camera setup to the platformer demo.

> **Note:** You can download the Platformer 3D demo on [GitHub](https://github.com/godotengine/godot-demo-projects/tree/master/3d/platformer) or using the [Asset Library](https://godotengine.org/asset-library/asset/2748).

In general, for a third-person camera setup, you will have three nodes as children of the node that you're following:

- Node3D (the "pivot point" for the camera)

- SpringArm3D

- Camera3D

Open the `player/player.tscn` scene. Set these up as children of our player and give them unique names so we can find them in our script. **Make sure to delete the existing camera node!**

Let's move the pivot point up by `2` on the Y-axis so that it's not on the ground:

Give the spring arm a length of `3` so that it is placed behind the character:

> **Note:** Leave the **Shape** of the spring arm as `<empty>`. This way, it will use the camera's pyramid shape. If you want, you can also try other shapes - a sphere is a common choice since it slides smoothly along edges.

Update the top of `player/player.gd` to grab the camera and the pivot points by their unique names:

player/player.gd

```gdscript
# Comment out this existing camera line.
# @onready var _camera := $Target/Camera3D as Camera3D

@onready var _camera := %Camera3D as Camera3D
@onready var _camera_pivot := %CameraPivot as Node3D
```

Add an `_unhandled_input` function to check for camera movement and then rotate the pivot point accordingly:

player/player.gd

```gdscript
@export_range(0.0, 1.0) var mouse_sensitivity = 0.01
@export var tilt_limit = deg_to_rad(75)

func _unhandled_input(event: InputEvent) -> void:
    # Mouselook implemented using `screen_relative` for resolution-independent sensitivity.
    if event is InputEventMouseMotion:
        _camera_pivot.rotation.x -= event.screen_relative.y * mouse_sensitivity
        # Prevent the camera from rotating too far up or down.
        _camera_pivot.rotation.x = clampf(_camera_pivot.rotation.x, -tilt_limit, tilt_limit)
        _camera_pivot.rotation.y += -event.screen_relative.x * mouse_sensitivity
```

By rotating the pivot point, the spring arm will also be rotated and it will change where the camera is positioned. Run the game and notice that mouse movement now rotates the camera around the character. If the camera moves into a wall, it collides with it.

---
