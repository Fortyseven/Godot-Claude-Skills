# Godot 4 GDScript Tutorials — 3D (Part 9)

> 5 tutorials. GDScript-specific code examples.

## Using MultiMeshInstance3D

> **Work in progress:** The content of this page was not yet updated for Godot `4.6` and may be **outdated**. If you know how to improve this page or you can confirm that it's up to date, feel free to [open a pull request](https://github.com/godotengine/godot-docs).

### Introduction

In a normal scenario, you would use a [MeshInstance3D](../godot_gdscript_nodes_3d.md) node to display a 3D mesh like a human model for the main character, but in some cases, you would like to create multiple instances of the same mesh in a scene. You _could_ duplicate the same node multiple times and adjust the transforms manually. This may be a tedious process and the result may look mechanical. Also, this method is not conducive to rapid iterations. [MultiMeshInstance3D](../godot_gdscript_nodes_3d.md) is one of the possible solutions to this problem.

MultiMeshInstance3D, as the name suggests, creates multiple copies of a MeshInstance over a surface of a specific mesh. An example would be having a tree mesh populate a landscape mesh with trees of random scales and orientations.

### Setting up the nodes

The basic setup requires three nodes: the MultiMeshInstance3D node and two MeshInstance3D nodes.

One node is used as the target, the surface mesh that you want to place multiple meshes on. In the tree example, this would be the landscape.

The other node is used as the source, the mesh that you want to have duplicated. In the tree case, this would be the tree itself.

In our example, we would use a [Node3D](../godot_gdscript_nodes_3d.md) node as the root node of the scene. Your scene tree would look like this:

> **Note:** For simplicity's sake, this tutorial uses built-in primitives.

Now you have everything ready. Select the MultiMeshInstance3D node and look at the toolbar, you should see an extra button called `MultiMesh` next to `View`. Click it and select _Populate surface_ in the dropdown menu. A new window titled _Populate MultiMesh_ will pop up.

### MultiMesh settings

Below are descriptions of the options.

#### Target Surface

The mesh used as the target surface on which to place copies of your source mesh.

#### Source Mesh

The mesh you want duplicated on the target surface.

#### Mesh Up Axis

The axis used as the up axis of the source mesh.

#### Random Rotation

Randomizing the rotation around the up axis of the source mesh.

#### Random Tilt

Randomizing the overall rotation of the source mesh.

#### Random Scale

Randomizing the scale of the source mesh.

#### Scale

The scale of the source mesh that will be placed over the target surface.

#### Amount

The amount of mesh instances placed over the target surface.

Select the target surface. In the tree case, this should be the landscape node. The source mesh should be the tree node. Adjust the other parameters according to your preference. Press `Populate` and multiple copies of the source mesh will be placed over the target mesh. If you are satisfied with the result, you can delete the mesh instance used as the source mesh.

The end result should look like this:

To change the result, repeat the previous steps with different parameters.

---

## Using 3D transforms

### Introduction

If you have never made 3D games before, working with rotations in three dimensions can be confusing at first. Coming from 2D, the natural way of thinking is along the lines of _"Oh, it's just like rotating in 2D, except now rotations happen in X, Y and Z"_.

At first, this seems easy. For simple games, this way of thinking may even be enough. Unfortunately, it's often incorrect.

Angles in three dimensions are most commonly referred to as "Euler Angles".

Euler angles were introduced by mathematician Leonhard Euler in the early 1700s.

This way of representing 3D rotations was groundbreaking at the time, but it has several shortcomings when used in game development (which is to be expected from a guy with a funny hat). The idea of this document is to explain why, as well as outlining best practices for dealing with transforms when programming 3D games.

### Problems of Euler angles

While it may seem intuitive that each axis has a rotation, the truth is that it's just not practical.

#### Axis order

The main reason for this is that there isn't a _unique_ way to construct an orientation from the angles. There isn't a standard mathematical function that takes all the angles together and produces an actual 3D rotation. The only way an orientation can be produced from angles is to rotate the object angle by angle, in an _arbitrary order_.

This could be done by first rotating in _X_, then _Y_ and then in _Z_. Alternatively, you could first rotate in _Y_, then in _Z_ and finally in _X_. Anything works, but depending on the order, the final orientation of the object will _not necessarily be the same_. Indeed, this means that there are several ways to construct an orientation from 3 different angles, depending on _the order of the rotations_.

Following is a visualization of rotation axes (in X, Y, Z order) in a gimbal (from Wikipedia). As you can see, the orientation of each axis depends on the rotation of the previous one:

You may be wondering how this affects you. Let's look at a practical example:

Imagine you are working on a first-person controller (e.g. an FPS game). Moving the mouse left and right controls your view angle parallel to the ground, while moving it up and down moves the player's view up and down.

In this case to achieve the desired effect, rotation must be applied first in the _Y_ axis ("up" in this case, since Godot uses a "Y-Up" orientation), followed by rotation in the _X_ axis.

If we were to apply rotation in the _X_ axis first, and then in _Y_, the effect would be undesired:

Depending on the type of game or effect desired, the order in which you want axis rotations to be applied may differ. Therefore, applying rotations in X, Y, and Z is not enough: you also need a _rotation order_.

#### Interpolation

Another problem with using Euler angles is interpolation. Imagine you want to transition between two different camera or enemy positions (including rotations). One logical way to approach this is to interpolate the angles from one position to the next. One would expect it to look like this:

But this does not always have the expected effect when using angles:

The camera actually rotated the opposite direction!

There are a few reasons this may happen:

- Rotations don't map linearly to orientation, so interpolating them does not always result in the shortest path (i.e., to go from `270` to `0` degrees is not the same as going from `270` to `360`, even though the angles are equivalent).
- Gimbal lock is at play (first and last rotated axis align, so a degree of freedom is lost). See [Wikipedia's page on Gimbal Lock](https://en.wikipedia.org/wiki/Gimbal_lock) for a detailed explanation of this problem.

#### Say no to Euler angles

The result of all this is that you should **not use** the `rotation` property of [Node3D](../godot_gdscript_nodes_3d.md) nodes in Godot for games. It's there to be used mainly in the editor, for coherence with the 2D engine, and for simple rotations (generally just one axis, or even two in limited cases). As much as you may be tempted, don't use it.

Instead, there is a better way to solve your rotation problems.

### Introducing transforms

Godot uses the [Transform3D](../godot_gdscript_math_types.md) datatype for orientations. Each [Node3D](../godot_gdscript_nodes_3d.md) node contains a `transform` property which is relative to the parent's transform, if the parent is a Node3D-derived type.

It is also possible to access the world coordinate transform via the `global_transform` property.

A transform has a [Basis](../godot_gdscript_math_types.md) (transform.basis sub-property), which consists of three [Vector3](../godot_gdscript_math_types.md) vectors. These are accessed via the `transform.basis` property and can be accessed directly by `transform.basis.x`, `transform.basis.y`, and `transform.basis.z`. Each vector points in the direction its axis has been rotated, so they effectively describe the node's total rotation. The scale (as long as it's uniform) can also be inferred from the length of the axes. A _basis_ can also be interpreted as a 3x3 matrix and used as `transform.basis[x][y]`.

A default basis (unmodified) is akin to:

```gdscript
var basis = Basis()
# Contains the following default values:
basis.x = Vector3(1, 0, 0) # Vector pointing along the X axis
basis.y = Vector3(0, 1, 0) # Vector pointing along the Y axis
basis.z = Vector3(0, 0, 1) # Vector pointing along the Z axis
```

This is also an analog of a 3x3 identity matrix.

Following the OpenGL convention, `X` is the _Right_ axis, `Y` is the _Up_ axis and `Z` is the _Forward_ axis.

Together with the _basis_, a transform also has an _origin_. This is a _Vector3_ specifying how far away from the actual origin `(0, 0, 0)` this transform is. Combining the _basis_ with the _origin_, a _transform_ efficiently represents a unique translation, rotation, and scale in space.

One way to visualize a transform is to look at an object's 3D gizmo while in "local space" mode.

The gizmo's arrows show the `X`, `Y`, and `Z` axes (in red, green, and blue respectively) of the basis, while the gizmo's center is at the object's origin.

For more information on the mathematics of vectors and transforms, please read the [Vector math](tutorials_math.md) tutorials.

#### Manipulating transforms

Of course, transforms are not as straightforward to manipulate as angles and have problems of their own.

It is possible to rotate a transform, either by multiplying its basis by another (this is called accumulation), or by using the rotation methods.

```gdscript
var axis = Vector3(1, 0, 0) # Or Vector3.RIGHT
var rotation_amount = 0.1
# Rotate the transform around the X axis by 0.1 radians.
transform.basis = Basis(axis, rotation_amount) * transform.basis
# shortened
transform.basis = transform.basis.rotated(axis, rotation_amount)
```

A method in Node3D simplifies this:

```gdscript
# Rotate the transform around the X axis by 0.1 radians.
rotate(Vector3(1, 0, 0), 0.1)
# shortened
rotate_x(0.1)
```

This rotates the node relative to the parent node.

To rotate relative to object space (the node's own transform), use the following:

```gdscript
# Rotate around the object's local X axis by 0.1 radians.
rotate_object_local(Vector3(1, 0, 0), 0.1)
```

The axis should be defined in the local coordinate system of the object. For example, to rotate around the object's local X, Y, or Z axes, use `Vector3.RIGHT` for the X-axis, `Vector3.UP` for the Y-axis, and `Vector3.FORWARD` for the Z-axis.

#### Precision errors

Doing successive operations on transforms will result in a loss of precision due to floating-point error. This means the scale of each axis may no longer be exactly `1.0`, and they may not be exactly `90` degrees from each other.

If a transform is rotated every frame, it will eventually start deforming over time. This is unavoidable.

There are two different ways to handle this. The first is to _orthonormalize_ the transform after some time (maybe once per frame if you modify it every frame):

```gdscript
transform = transform.orthonormalized()
```

This will make all axes have `1.0` length again and be `90` degrees from each other. However, any scale applied to the transform will be lost.

It is recommended you not scale nodes that are going to be manipulated; scale their children nodes instead (such as MeshInstance3D). If you absolutely must scale the node, then re-apply it at the end:

```gdscript
transform = transform.orthonormalized()
transform = transform.scaled(scale)
```

#### Obtaining information

You might be thinking at this point: **"Ok, but how do I get angles from a transform?"**. The answer again is: you don't. You must do your best to stop thinking in angles.

Imagine you need to shoot a bullet in the direction your player is facing. Just use the forward axis.

```gdscript
# On RigidBody3D.

# Keep in mind that -Z is forward.
bullet.transform = transform
bullet.linear_velocity = -transform.basis.z * BULLET_SPEED
```

Is the enemy looking at the player? Use the dot product for this (see the [Vector math](tutorials_math.md) tutorial for an explanation of the dot product):

```gdscript
# Get the direction vector from player to enemy
var direction = enemy.transform.origin - player.transform.origin
if direction.dot(enemy.transform.basis.z) > 0:
    enemy.im_watching_you(player)
```

Strafe left:

```gdscript
# On CharacterBody3D.

# Keep in mind that -X is left.
if Input.is_action_pressed("strafe_left"):
    velocity = -transform.basis.x * MOVE_SPEED

move_and_slide()
```

Jump:

```gdscript
# On CharacterBody3D.

# Keep in mind that +Y is up.
if Input.is_action_just_pressed("jump"):
    velocity.y = JUMP_SPEED

move_and_slide()
```

All common behaviors and logic can be done with just vectors.

#### Setting information

There are, of course, cases where you want to set information to a transform. Imagine a first person controller or orbiting camera. Those are definitely done using angles, because you _do want_ the transforms to happen in a specific order.

For such cases, keep the angles and rotations _outside_ the transform and set them every frame. Don't try to retrieve and reuse them because the transform is not meant to be used this way.

Example of looking around, FPS style:

```gdscript
# accumulators
var rot_x = 0
var rot_y = 0

func _input(event):
    if event is InputEventMouseMotion and event.button_mask & 1:
        # modify accumulated mouse rotation
        rot_x -= event.screen_relative.x * LOOKAROUND_SPEED
        rot_y -= event.screen_relative.y * LOOKAROUND_SPEED
        transform.basis = Basis() # reset rotation
        rotate_object_local(Vector3(0, 1, 0), rot_x) # first rotate in Y
        rotate_object_local(Vector3(1, 0, 0), rot_y) # then rotate in X
```

As you can see, in such cases it's even simpler to keep the rotation outside, then use the transform as the _final_ orientation.

#### Interpolating with quaternions

Interpolating between two transforms can efficiently be done with quaternions. More information about how quaternions work can be found in other places around the Internet. For practical use, it's enough to understand that pretty much their main use is doing a closest path interpolation. As in, if you have two rotations, a quaternion will smoothly allow interpolation between them using the closest axis.

Converting a rotation to quaternion is straightforward.

```gdscript
# Convert basis to quaternion, keep in mind scale is lost
var a = Quaternion(transform.basis)
var b = Quaternion(transform2.basis)
# Interpolate using spherical-linear interpolation (SLERP).
var c = a.slerp(b,0.5) # find halfway point between a and b
# Apply back
transform.basis = Basis(c)
```

The [Quaternion](../godot_gdscript_math_types.md) type reference has more information on the datatype (it can also do transform accumulation, transform points, etc., though this is used less often). If you interpolate or apply operations to quaternions many times, keep in mind they need to be eventually normalized. Otherwise, they will also suffer from numerical precision errors.

Quaternions are useful when doing camera/path/etc. interpolations, as the result will always be correct and smooth.

### Transforms are your friend

For most beginners, getting used to working with transforms can take some time. However, once you get used to them, you will appreciate their simplicity and power.

Don't hesitate to ask for help on this topic in any of Godot's [online communities](https://godotengine.org/community) and, once you become confident enough, please help others!

---

## Variable rate shading

### What is variable rate shading?

In modern 3D rendering engines, shaders are much more complex compared to before. The advent of physically-based rendering, real-time global illumination and screen-space effects has increased the number of _per-pixel_ shading that must be performed to render each frame. Additionally, screen resolutions also have increased a lot, with 1440p and 4K now being common target resolutions. As a result, the total shading cost in scene rendering usually represents a significant amount of the time taken to render each frame.

Variable rate shading (VRS) is a method of decreasing this shading cost by reducing the resolution of _per-pixel_ shading (also called _fragment_ shading), while keeping the original resolution for rendering geometry. This means geometry edges remain as sharp as they would without VRS. VRS can be combined with any 3D antialiasing technique (MSAA, FXAA, TAA, SSAA).

VRS allows specifying the shading quality in a local manner, which makes it possible to have certain parts of the viewport receive more detailed shading than others. This is particularly useful in virtual reality (VR) to achieve _foveated rendering_, where the center of the viewport is more detailed than the edges.

Here's a scene rendered with rate shading disabled then enabled, using the density map linked at the bottom of this page:

When used in scenes with low-frequency detail (such as scenes with a stylized/low-poly aesthetic), it's possible to achieve similar performance gains, but with less reduction in visual quality:

### Hardware support

Variable rate shading is only supported on specific GPUs:

**Desktop:**

- NVIDIA Turing and newer (including GTX 1600 series)
- AMD RDNA2 and newer (both integrated and dedicated GPUs – including Steam Deck)
- Intel Arc Alchemist and newer **(dedicated GPUs only)**

- Intel integrated graphics do not support variable rate shading.

**Mobile SoCs:**

- Snapdragon 888 and newer
- MediaTek Dimensity 9000 and newer
- ARM Mali-G615 and newer

As of January 2023, Apple and Raspberry Pi GPUs do not support variable rate shading.

### Using variable rate shading in Godot

> **Note:** Both Forward+ and Mobile renderers support variable rate shading. VRS can be used in both pancake (non-XR) and XR display modes. The Compatibility renderer does **not** support variable rate shading. For XR, you can use [foveation level](tutorials_xr.md) as an alternative.

In the advanced Project Settings, the **Rendering > VRS** section offers settings to control variable rate shading on the root viewport:

- **Mode:** Controls the variable rate shading mode. **Disabled** disables variable rate shading. **Texture** uses a manually authored texture to set shading density (see the property below). **XR** automatically generates a texture suited for foveated rendering in virtual/augmented reality.
- **Texture:** The texture to use to control shading density on the root viewport. Only used if **Mode** is **Texture**.

For custom viewports, the VRS mode and texture must be set manually to the [Viewport](../godot_gdscript_rendering.md) node.

> **Note:** On unsupported hardware, there is no visual difference when variable rate shading is enabled. You can check whether hardware supports variable rate shading by running the editor or project with the `--verbose` [command line argument](tutorials_editor.md).

#### Creating a VRS density map

If using the **Texture** VRS mode, you _must_ set a texture to be used as a density map. Otherwise, no effect will be visible.

You can create your own VRS density map manually using an image editor, or generate it using another method (e.g. on the CPU using the Image class, or on the GPU using a shader). However, beware of performance implications when generating a VRS image dynamically. If opting for dynamic generation, make sure the VRS image generation process is fast enough to avoid outweighing the performance gains from VRS.

The texture must follow these rules:

- The texture _must_ use a lossless compression format so that colors can be matched precisely.
- The following VRS densities are mapped to various colors, with brighter colors representing a lower level of shading precision:

| Density              | Color                      | Comment                         |
| -------------------- | -------------------------- | ------------------------------- |
| 1×1 (highest detail) | rgb(0, 0, 0) - #000000     |                                 |
| 1×2                  | rgb(0, 85, 0) - #005500    |                                 |
| 2×1                  | rgb(85, 0, 0) - #550000    |                                 |
| 2×2                  | rgb(85, 85, 0) - #555500   |                                 |
| 2×4                  | rgb(85, 170, 0) - #55aa00  |                                 |
| 4×2                  | rgb(170, 85, 0) - #aa5500  |                                 |
| 4×4                  | rgb(170, 170, 0) - #aaaa00 |                                 |
| 4×8                  | rgb(170, 255, 0) - #aaff00 | Not supported on most hardware. |
| 8×4                  | rgb(255, 170, 0) - #ffaa00 | Not supported on most hardware. |
| 8×8 (lowest detail)  | rgb(255, 255, 0) - #ffff00 | Not supported on most hardware. |

For example, this VRS density texture provides the highest shading density in the center of the viewport, and the lowest shading density in the corners:

There are no size or aspect ratio requirements for the VRS density texture. However, there is no benefit to using a VRS density map that is larger than the viewport resolution divided by the GPU's _tile size_. The tile size is what determines the smallest area of pixels where the shading density can be changed separately from other tiles. On most GPUs, this tile size is 8×8 pixels. You can view the tile size by running Godot with the `--verbose` command line argument, as it's printed in the VRS debugging information.

Therefore, sticking to a relatively low resolution such as 256×256 (square) or 480×270 (16:9) is recommended. Depending on your use cases, a square texture may be more suited compared to a texture that matches the most common viewport aspect ratio in your project (such as 16:9).

> **Tip:** When using variable rate shading, you can use a negative texture mipmap LOD bias to reduce blurriness in areas with reduced shading rate. Note that the texture LOD bias is set globally, so this will also affect areas of the viewport with full shading rate. Don't use values that are too low, or textures will appear grainy.

#### Performance comparison

To give an idea of how much VRS can improve performance in theory, here's a performance comparison with the textured example scene shown at the top of this page. The VRS density map example present on this page is used.

Results were captured on a GeForce RTX 4090 with the NVIDIA 525.60.11 driver.

| Resolution          | VRS disabled | VRS enabled | Performance improvement |
| ------------------- | ------------ | ----------- | ----------------------- |
| 1920×1080 (Full HD) | 2832 FPS     | 3136 FPS    | +10.7%                  |
| 2560×1440 (QHD)     | 2008 FPS     | 2256 FPS    | +12.3%                  |
| 3840×2160 (4K)      | 1236 FPS     | 1436 FPS    | +16.2%                  |
| 7680×4320 (8K)      | 384 FPS      | 473 FPS     | +23.1%                  |

In terms of performance improvements, variable rate shading is more beneficial at higher target resolutions. The reduction in visual quality is also less noticeable at high resolutions.

> **Note:** For non-VR games, you will probably have to use a less aggressive VRS texture than what was used in this example. As a result, the effective performance gains will be lower.

---

## Visibility ranges (HLOD)

Along with Mesh level of detail (LOD) and Occlusion culling, visibility ranges are another tool to improve performance in large, complex 3D scenes.

On this page, you'll learn:

- What visibility ranges can do and which scenarios they are useful in.
- How to set up visibility ranges (manual LOD) in Godot.
- How to tune visibility ranges for best performance and quality.

> **See also:** If you only need meshes to become less detailed over distance, but don't have manually authored LOD meshes, consider relying on automatic Mesh level of detail (LOD) instead. Note that automatic mesh LOD and visibility ranges can be used at the same time, even on the same mesh.

### How it works

Visibility ranges can be used with any node that inherits from GeometryInstance3D. This means they can be used not only with MeshInstance3D and MultiMeshInstance3D for artist-controlled HLOD, but also GPUParticles3D, CPUParticles3D, Label3D, Sprite3D, AnimatedSprite3D and CSGShape3D.

Since visibility ranges are configured on a per-node basis, this makes it possible to use different node types as part of a LOD system. For example, you could display a MeshInstance3D representing a tree when up close, and replace it with a Sprite3D impostor in the distance to improve performance.

The benefit of HLOD over a traditional LOD system is its hierarchical nature. A single larger mesh can replace several smaller meshes, so that the number of draw calls can be reduced at a distance, but culling opportunities can be preserved when up close. For example, you can have a group of houses that uses individual MeshInstance3D nodes (one for each house) when up close, but turns into a single MeshInstance3D that represents a less detailed group of houses (or use a MultiMeshInstance3D).

Lastly, visibility ranges can also be used to fade certain objects entirely when the camera gets too close or too far. This can be used for gameplay purposes, but also to reduce visual clutter. For example, Label3D nodes can be faded using visibility ranges when they're too far away to be readable or relevant to the player.

### Setting up visibility range

This is a quick-start guide for configuring a basic LOD system. After following this guide, this LOD system will display a SphereMesh when up close and a BoxMesh when the camera is far away enough. A small hysteresis margin is also configured via the **Begin Margin** and **End Margin** properties. This prevents LODs from popping back and forth too quickly when the camera is moving at the "edge" of the LOD transition.

The visibility range properties can be found in the **Visibility Range** section of the GeometryInstance3D inspector after selecting the MeshInstance3D Node.

- Add a Node3D node that will be used to group the two MeshInstance3D nodes together.
- Add a first MeshInstance3D node as a child of the Node3D. Assign a new SphereMesh to its Mesh property.
- Set the first MeshInstance3D's visibility range **End** to `10.0` and **End Margin** to `1.0`.
- Add a second MeshInstance3D node as a child of the Node3D. Assign a new BoxMesh to its Mesh property.
- Set the second MeshInstance3D's visibility range **Begin** to `10.0` and **Begin Margin** to `1.0`.
- Move the camera away and back towards the object. Notice how the object will transition from a sphere to a box as the camera moves away.

### Visibility range properties

In the inspector of any node that inherits from GeometryInstance3D, you can adjust the following properties in the GeometryInstance3D's **Visibility Range** section:

- **Begin:** The instance will be hidden when the camera is closer to the _center of the instance's AABB_ (axis-aligned bounding box) than this value (in 3D units).
- **Begin Margin:** The hysteresis or alpha fade transition distance to use for the close-up transition (in 3D units). The behavior of this property depends on **Fade Mode**.
- **End:** The instance will be hidden when the camera is further away from the _center of the instance's AABB_ than this value (in 3D units).
- **End Margin:** The hysteresis or alpha fade transition distance to use for the far-away transition (in 3D units). The behavior of this property depends on **Fade Mode**.
- **Fade Mode:** Controls how the transition between LOD levels should be performed. See below for details.

#### Fade mode

> **Note:** The fade mode chosen only has a visible impact if either **Visibility Range > Begin Margin** or **Visibility Range > End Margin** is greater than `0.0`.

In the inspector's **Visibility Range** section, there are 3 fade modes to choose from:

- **Disabled:** Uses hysteresis to switch between LOD levels instantly. This prevents situations where LOD levels are switched back and forth quickly when the player moves forward and then backward at the LOD transition point. The hysteresis distance is determined by **Visibility Range > Begin Margin** and **Visibility Range > End Margin**. This mode provides the best performance as it doesn't force rendering to become transparent during the fade transition.
- **Self:** Uses alpha blending to smoothly fade between LOD levels. The node will fade-out itself when reaching the limits of its own visibility range. The fade transition distance is determined by **Visibility Range > Begin Margin** and **Visibility Range > End Margin**. This mode forces transparent rendering on the object during its fade transition, so it has a performance impact.
- **Dependencies:** Uses alpha blending to smoothly fade between LOD levels. The node will fade-in its dependencies when reaching the limits of its own visibility range. The fade transition distance is determined by **Visibility Range > Begin Margin** and **Visibility Range > End Margin**. This mode forces transparent rendering on the object during its fade transition, so it has a performance impact. This mode is intended for hierarchical LOD systems using **Visibility parent**. It acts the same as **Self** if visibility ranges are used to perform non-hierarchical LOD.

#### Visibility parent

The **Visibility Parent** property makes it easier to set up HLOD. It allows automatically hiding child nodes if its parent is visible given its current visibility range properties.

> **Note:** The target of **Visibility Parent** _must_ inherit from [GeometryInstance3D](../godot_gdscript_nodes_3d.md). Despite its name, the **Visibility Parent** property _can_ point to a node that is not a parent of the node in the scene tree. However, it is impossible to point **Visibility Parent** towards a child node, as this creates a dependency cycle which is not supported. You will get an error message in the Output panel if a dependency cycle occurs.

Given the following scene tree (where all nodes inherit from GeometryInstance3D):

```gdscript
┖╴BatchOfHouses
    ┠╴House1
    ┠╴House2
    ┠╴House3
    ┖╴House4
```

In this example, _BatchOfHouses_ is a large mesh designed to represent all child nodes when viewed at a distance. _House1_ to _House4_ are smaller MeshInstance3Ds representing individual houses. To configure HLOD in this example, we only need to configure two things:

- Set **Visibility Range Begin** to a number greater than 0.0 so that _BatchOfHouses_ only appears when far away enough from the camera. Below this distance, we want _House1_ to _House4_ to be displayed instead.
- On _House1_ to _House4_, assign the **Visibility Parent** property to _BatchOfHouses_.

This makes it easier to perform further adjustments, as you don't need to adjust the **Visibility Range Begin** of _BatchOfHouses_ and **Visibility Range End** of _House1_ to _House4_.

Fade mode is automatically handled by the **Visibility Parent** property, so that the child nodes only become hidden once the parent node is fully faded out. This is done to minimize visible pop-in. Depending on your HLOD setup, you may want to try both the **Self** and **Dependencies** **fade modes**.

> **Note:** Nodes hidden via the **Visible** property are essentially removed from the visibility dependency tree, so dependent instances will not take the hidden node or its ancestors into account. In practice, this means that if the target of the **Visibility Parent** node is hidden by setting its **Visible** property to `false`, the node will not be hidden according to the **Visibility Range Begin** value specified in the visibility parent.

### Configuration tips

#### Use simpler materials at a distance to improve performance

One way to further improve performance is to use simpler materials for distant LOD meshes. While using LOD meshes will reduce the number of vertices that need to be rendered, the per-pixel shading load for materials remains identical. However, per-pixel shading load is regularly a bottleneck on the GPU in complex 3D scenes. One way to reduce this shading load on the GPU is to use simpler materials when they don't make much of a visual difference.

Performance gains when doing so should be carefully measured, as increasing the number of _unique_ materials in a scene has a performance cost on its own. Still, using simpler materials for distant LOD meshes can still result in a net performance gain as a result of the fewer per-pixel calculations required.

For example, on the materials used by distant LOD meshes, you can disable expensive material features such as:

- Normal Map (especially on mobile platforms)
- Rim
- Clearcoat
- Anisotropy
- Height
- Subsurface Scattering
- Back Lighting
- Refraction
- Proximity Fade

#### Use dithering for LOD transitions

Godot currently only supports alpha-based fading for visibility ranges. You can however use dithering instead by using several different materials for different LOD levels.

There are two advantages to using dithering over alpha blending for LOD transitions:

- Higher performance, as dithering transparency is faster to render compared to alpha blending.
- No visual glitches due to transparency sorting issues during LOD transitions.

The downside of dithering is that a "noisy" pattern is visible during LOD fade transitions. This may not be as noticeable at higher viewport resolutions or when temporal antialiasing is enabled.

Also, as distance fade in BaseMaterial3D only supports fading up close _or_ fading when far away, this setup is best used with only two LODs as part of the setup.

- Ensure **Begin Margin** and **End Margin** is set to `0.0` on both MeshInstance3D nodes, as hysteresis or alpha fade are not desired here.
- On both MeshInstance3D nodes, _decrease_ **Begin** by the desired fade transition distance and _increase_ **End** by the same distance. This is required for the dithering transition to actually be visible.
- On the MeshInstance3D that is displayed up close, edit its material in the inspector. Set its **Distance Fade** mode to **Object Dither**. Set **Min Distance** to the same value as the visibility range **End**. Set **Max Distance** to the same value _minus_ the fade transition distance.
- On the MeshInstance3D that is displayed far away, edit its material in the inspector. Set its **Distance Fade** mode to **Object Dither**. Set **Min Distance** to the same value as the visibility range **Begin**. Set **Max Distance** to the same value _plus_ the fade transition distance.

---

## Volumetric fog and fog volumes

> **Note:** Volumetric fog is only supported in the Forward+ renderer, not the Mobile or Compatibility renderers.

As described in Environment and post-processing, Godot supports various visual effects including two types of fog: traditional (non-volumetric) fog and volumetric fog. Traditional fog affects the entire scene at once and cannot be customized with [Fog shaders](tutorials_shaders.md).

Volumetric fog can be used at the same time as non-volumetric fog if desired.

On this page, you'll learn:

- How to set up volumetric fog in Godot.
- What fog volumes are and how they differ from "global" volumetric fog.

> **See also:** You can see how volumetric fog works in action using the [Volumetric Fog demo project](https://github.com/godotengine/godot-demo-projects/tree/master/3d/volumetric_fog).

Here is a comparison between traditional fog (which does not interact with lighting) and volumetric fog, which is able to interact with lighting:

### Volumetric fog properties

After enabling volumetric fog in the WorldEnvironment node's Environment resource, you can edit the following properties:

- **Density:** The base _exponential_ density of the volumetric fog. Set this to the lowest density you want to have globally. FogVolumes can be used to add to or subtract from this density in specific areas. A value of `0.0` disables global volumetric fog while allowing FogVolumes to display volumetric fog in specific areas. Fog rendering is exponential as in real life.
- **Albedo:** The Color of the volumetric fog when interacting with lights. Mist and fog have an albedo close to white (`Color(1, 1, 1, 1)`) while smoke has a darker albedo.
- **Emission:** The emitted light from the volumetric fog. Even with emission, volumetric fog will not cast light onto other surfaces. Emission is useful to establish an ambient color. As the volumetric fog effect uses single-scattering only, fog tends to need a little bit of emission to soften the harsh shadows.
- **Emission Energy:** The brightness of the emitted light from the volumetric fog.
- **GI Inject:** Scales the strength of Global Illumination used in the volumetric fog's albedo color. A value of `0.0` means that Global Illumination will not impact the volumetric fog. This has a small performance cost when set above `0.0`.
- **Anisotropy:** The direction of scattered light as it goes through the volumetric fog. A value close to `1.0` means almost all light is scattered forward. A value close to `0.0` means light is scattered equally in all directions. A value close to `-1.0` means light is scattered mostly backward. Fog and mist scatter light slightly forward, while smoke scatters light equally in all directions.
- **Length:** The distance over which the volumetric fog is computed. Increase to compute fog over a greater range, decrease to add more detail when a long range is not needed. For best quality fog, keep this as low as possible.
- **Detail Spread:** The distribution of size down the length of the froxel buffer. A higher value compresses the froxels closer to the camera and places more detail closer to the camera.
- **Ambient Inject:** Scales the strength of ambient light used in the volumetric fog. A value of `0.0` means that ambient light will not impact the volumetric fog. This has a small performance cost when set above `0.0`.
- **Sky Affect:** Controls how much volumetric fog should be drawn onto the background sky. If set to `0.0`, volumetric fog won't affect sky rendering at all (including FogVolumes).

Two additional properties are offered in the **Temporal Reprojection** section:

- **Temporal Reprojection > Enabled:** Enables temporal reprojection in the volumetric fog. Temporal reprojection blends the current frame's volumetric fog with the last frame's volumetric fog to smooth out jagged edges. The performance cost is minimal, however it does lead to moving FogVolumes and Light3Ds "ghosting" and leaving a trail behind them. When temporal reprojection is enabled, try to avoid moving FogVolumes or Light3Ds too fast. Short-lived dynamic lighting effects should have **Volumetric Fog Energy** set to `0.0` to avoid ghosting.
- **Temporal Reprojection > Amount:** The amount by which to blend the last frame with the current frame. A higher number results in smoother volumetric fog, but makes "ghosting" much worse. A lower value reduces ghosting but can result in the per-frame temporal jitter becoming visible.

> **Note:** Unlike non-volumetric fog, volumetric fog has a _finite_ range. This means volumetric fog cannot entirely cover a large world, as it will eventually stop being rendered in the distance. If you wish to hide distant areas from the player, it's recommended to enable both non-volumetric fog and volumetric fog at the same time, and adjust their density accordingly.

### Light interaction with volumetric fog

To simulate fog light scattering behavior in real life, all light types will interact with volumetric fog. How much each light will affect volumetric fog can be adjusted using the **Volumetric Fog Energy** property on each light. Enabling shadows on a light will also make those shadows visible on volumetric fog.

If fog light interaction is not desired for artistic reasons, this can be globally disabled by setting **Volumetric Fog > Albedo** to a pure black color in the Environment resource. Fog light interaction can also be disabled for specific lights by setting its **Volumetric Fog Energy** to `0`. Doing so will also improve performance slightly by excluding the light from volumetric fog computations.

### Using volumetric fog as a volumetric lighting solution

While not physically accurate, it is possible to tune volumetric fog's settings to work as volumetric _lighting_ solution. This means that unlit parts of the environment will not be darkened anymore by fog, but light will still be able to make fog brighter in specific areas.

This can be done by setting volumetric fog density to the lowest permitted value _greater than zero_ (`0.0001`), then increasing the **Volumetric Fog Energy** property on lights to much higher values than the default to compensate. Values between `200.0` and `5000.0` usually work well for this.

### Balancing performance and quality

There are a few project settings available to adjust volumetric fog performance and quality:

- **Rendering > Environment > Volumetric Fog > Volume Size:** Base size used to determine size of froxel buffer in the camera X-axis and Y-axis. The final size is scaled by the aspect ratio of the screen, so actual values may differ from what is set. Set a larger size for more detailed fog, set a smaller size for better performance.
- **Rendering > Environment > Volumetric Fog > Volume Depth:** Number of slices to use along the depth of the froxel buffer for volumetric fog. A lower number will be more efficient, but may result in artifacts appearing during camera movement.
- **Rendering > Environment > Volumetric Fog > Use Filter:** Enables filtering of the volumetric fog effect prior to integration. This substantially blurs the fog which reduces fine details, but also smooths out harsh edges and aliasing artifacts. Disable when more detail is required.

> **Note:** Volumetric fog can cause banding to appear on the viewport, especially at higher density levels. See Color banding for guidance on reducing banding.

### Using fog volumes for local volumetric fog

Sometimes, you want fog to be constrained to specific areas. Conversely, you may want to have global volumetric fog, but fog should be excluded from certain areas. Both approaches can be followed using FogVolume nodes.

Here's a quick start guide to using FogVolumes:

- Make sure **Volumetric Fog** is enabled in the Environment properties. If global volumetric fog is undesired, set its **Density** to `0.0`.
- Create a FogVolume node.
- Assign a new FogMaterial to the FogVolume node's **Material** property.
- In the FogMaterial, set **Density** to a positive value to increase density within the FogVolume, or a negative value to subtract the density from global volumetric fog.
- Configure the FogVolume's extents and shape as needed.

> **Note:** Thin fog volumes may appear to flicker when the camera moves or rotates. This can be alleviated by increasing the **Rendering > Environment > Volumetric Fog > Volume Depth** project setting (at a performance cost) or by decreasing **Length** in the Environment volumetric fog properties (at no performance cost, but at the cost of lower fog range). Alternatively, the FogVolume can be made thicker and use a lower density in the **Material**.

### FogVolume properties

- **Extents:** The size of the FogVolume when **Shape** is **Ellipsoid**, **Cone**, **Cylinder** or **Box**. If **Shape** is **Cone** or **Cylinder**, the cone/cylinder will be adjusted to fit within the extents. Non-uniform scaling of cone/cylinder shapes via the **Extents** property is not supported, but you can scale the FogVolume node instead.
- **Shape:** The shape of the FogVolume. This can be set to **Ellipsoid**, **Cone**, **Cylinder**, **Box** or **World** (acts as global volumetric fog).
- **Material:** The material used by the FogVolume. Can be either a built-in FogMaterial or a custom ShaderMaterial ([Fog shaders](tutorials_shaders.md)).

After choosing **New FogMaterial** in the **Material** property, you can adjust the following properties in FogMaterial:

- **Density:** The density of the FogVolume. Denser objects are more opaque, but may suffer from under-sampling artifacts that look like stripes. Negative values can be used to subtract fog from other FogVolumes or global volumetric fog.
- **Albedo:** The single-scattering Color of the FogVolume. Internally, member albedo is converted into single-scattering, which is additively blended with other FogVolumes and global volumetric fog's **Albedo**.
- **Emission:** The Color of the light emitted by the FogVolume. Emitted light will not cast light or shadows on other objects, but can be useful for modulating the Color of the FogVolume independently from light sources.
- **Height Falloff:** The rate by which the height-based fog decreases in density as height increases in world space. A high falloff will result in a sharp transition, while a low falloff will result in a smoother transition. A value of `0.0` results in uniform-density fog. The height threshold is determined by the height of the associated FogVolume.
- **Edge Fade:** The hardness of the edges of the FogVolume. A higher value will result in softer edges, while a lower value will result in harder edges.
- **Density Texture:** The 3D texture that is used to scale the member density of the FogVolume. This can be used to vary fog density within the FogVolume with any kind of static pattern. For animated effects, consider using a custom [fog shader](tutorials_shaders.md). You can import any image as a 3D texture by [changing its import type in the Import dock](tutorials_assets_pipeline.md).

#### Using 3D noise density textures

Since Godot 4.1, there is a NoiseTexture3D resource that can be used to procedurally generate 3D noise. This is well-suited to FogMaterial density textures, which can result in more detailed fog effects:

To do so, select the **Density Texture** property and choose **New NoiseTexture3D**. Edit this NoiseTexture3D by clicking it, then click **Noise** at the bottom of the NoiseTexture3D properties and choose **New FastNoiseLite**. Adjust the noise texture's width, height and depth according to your fog volume's dimensions.

To improve performance, it's recommended to use low texture sizes (64×64×64 or lower), as high-frequency detail is difficult to notice in a FogVolume. If you wish to represent more detailed density variations, you will need to increase **Rendering > Environment > Volumetric Fog > Volume Size** in the project settings, which has a performance cost.

> **Note:** NoiseTexture3D's **Color Ramp** affects FogMaterial density textures, but since only the texture's red channel is sampled, only the color ramp's red channel will affect the resulting density. However, using a color ramp will _not_ tint the fog volume according to the texture. You would need to use a custom shader that reads a Texture3D to achieve this.

### Custom FogVolume shaders

This page only covers the built-in settings offered by FogMaterial. If you need to customize fog behavior within a FogVolume node (such as creating animated fog), FogVolume nodes' appearance can be customized using [Fog shaders](tutorials_shaders.md).

### Faking volumetric fog using quads

In some cases, it may be better to use specially configured QuadMeshes as an alternative to volumetric fog:

- Quads work with any rendering method, including Mobile and Compatibility.
- Quads do not require temporal reprojection to look smooth, which makes them suited to fast-moving dynamic effects such as lasers. They can also represent small details which volumetric fog cannot do efficiently.
- Quads generally have a lower performance cost than volumetric fog.

This approach has a few downsides though:

- The fog effect has less realistic falloff, especially if the camera enters the fog.
- Transparency sorting issues may occur when sprites overlap.
- Performance will not necessarily be better than volumetric fog if there are lots of sprites close to the camera.

To create a QuadMesh-based fog sprite:

1. Create a MeshInstance3D node with a QuadMesh resource in the **Mesh** property. Set the size as desired.
2. Create a new StandardMaterial3D in the mesh's **Material** property.
3. In the StandardMaterial3D, set **Shading > Shading Mode** to **Unshaded**, **Billboard > Mode** to **Enabled**, enable **Proximity Fade** and set **Distance Fade** to **Pixel Alpha**.
4. Set the **Albedo > Texture** to the texture below (right-click and choose **Save as…**):
5. _After_ setting the albedo texture, go to the Import dock, select the texture and change its compression mode to **Lossless** to improve quality.

The fog's color is set using the **Albedo > Color** property; its density is set using the color's alpha channel. For best results, you will have to adjust **Proximity Fade > Distance** and **Distance Fade > Max Distance** depending on the size of your QuadMesh.

Optionally, billboarding may be left disabled if you place the quad in a way where all of its corners are in solid geometry. This can be useful for fogging large planes that the camera cannot enter, such as bottomless pits.

---
