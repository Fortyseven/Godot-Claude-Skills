# Godot 4 GDScript Tutorials — Physics (Part 1)

> 8 tutorials. GDScript-specific code examples.

## Collision shapes (2D)

This guide explains:

- The types of collision shapes available in 2D in Godot.
- Using an image converted to a polygon as a collision shape.
- Performance considerations regarding 2D collisions.

Godot provides many kinds of collision shapes, with different performance and accuracy tradeoffs.

You can define the shape of a [PhysicsBody2D](../godot_gdscript_physics.md) by adding one or more [CollisionShape2Ds](../godot_gdscript_nodes_2d.md) or [CollisionPolygon2Ds](../godot_gdscript_nodes_2d.md) as _direct_ child nodes. Indirect child nodes (i.e. children of child nodes) will be ignored and won't be used as collision shapes. Also, note that you must add a [Shape2D](../godot_gdscript_physics.md) _resource_ to collision shape nodes in the Inspector dock.

> **Note:** When you add multiple collision shapes to a single PhysicsBody2D, you don't have to worry about them overlapping. They won't "collide" with each other.

### Primitive collision shapes

Godot provides the following primitive collision shape types:

- [RectangleShape2D](../godot_gdscript_misc.md)
- [CircleShape2D](../godot_gdscript_misc.md)
- [CapsuleShape2D](../godot_gdscript_misc.md)
- [SegmentShape2D](../godot_gdscript_misc.md)
- [SeparationRayShape2D](../godot_gdscript_misc.md) (designed for characters)
- [WorldBoundaryShape2D](../godot_gdscript_misc.md) (infinite plane)

You can represent the collision of most smaller objects using one or more primitive shapes. However, for more complex objects, such as a large ship or a whole level, you may need convex or concave shapes instead. More on that below.

We recommend favoring primitive shapes for dynamic objects such as RigidBodies and CharacterBodies as their behavior is the most reliable. They often provide better performance as well.

### Convex collision shapes

> **Warning:** Godot currently doesn't offer a built-in way to create 2D convex collision shapes. This section is mainly here for reference purposes.

[Convex collision shapes](../godot_gdscript_misc.md) are a compromise between primitive collision shapes and concave collision shapes. They can represent shapes of any complexity, but with an important caveat. As their name implies, an individual shape can only represent a _convex_ shape. For instance, a pyramid is _convex_, but a hollow box is _concave_. To define a concave object with a single collision shape, you need to use a concave collision shape.

Depending on the object's complexity, you may get better performance by using multiple convex shapes instead of a concave collision shape. Godot lets you use _convex decomposition_ to generate convex shapes that roughly match a hollow object. Note this performance advantage no longer applies after a certain amount of convex shapes. For large and complex objects such as a whole level, we recommend using concave shapes instead.

### Concave or trimesh collision shapes

[Concave collision shapes](../godot_gdscript_misc.md), also called trimesh collision shapes, can take any form, from a few triangles to thousands of triangles. Concave shapes are the slowest option but are also the most accurate in Godot. **You can only use concave shapes within StaticBodies.** They will not work with CharacterBodies or RigidBodies unless the RigidBody's mode is Static.

> **Note:** Even though concave shapes offer the most accurate _collision_, contact reporting can be less precise than primitive shapes.

When not using TileMaps for level design, concave shapes are the best approach for a level's collision.

You can configure the CollisionPolygon2D node's _build mode_ in the inspector. If it is set to **Solids** (the default), collisions will include the polygon and its contained area. If it is set to **Segments**, collisions will only include the polygon edges.

You can generate a concave collision shape from the editor by selecting a Sprite2D and using the **Sprite2D** menu at the top of the 2D viewport. The Sprite2D menu dropdown exposes an option called **Create CollisionPolygon2D Sibling**. Once you click it, it displays a menu with 3 settings:

- **Simplification:** Higher values will result in a less detailed shape, which improves performance at the cost of accuracy.
- **Shrink (Pixels):** Higher values will shrink the generated collision polygon relative to the sprite's edges.
- **Grow (Pixels):** Higher values will grow the generated collision polygon relative to the sprite's edges. Note that setting Grow and Shrink to equal values may yield different results than leaving both of them on 0.

> **Note:** If you have an image with many small details, it's recommended to create a simplified version and use it to generate the collision polygon. This can result in better performance and game feel, since the player won't be blocked by small, decorative details. To use a separate image for collision polygon generation, create another Sprite2D, generate a collision polygon sibling from it then remove the Sprite2D node. This way, you can exclude small details from the generated collision.

### Performance caveats

You aren't limited to a single collision shape per PhysicsBody. Still, we recommend keeping the number of shapes as low as possible to improve performance, especially for dynamic objects like RigidBodies and CharacterBodies. On top of that, avoid translating, rotating, or scaling CollisionShapes to benefit from the physics engine's internal optimizations.

When using a single non-transformed collision shape in a StaticBody, the engine's _broad phase_ algorithm can discard inactive PhysicsBodies. The _narrow phase_ will then only have to take into account the active bodies' shapes. If a StaticBody has many collision shapes, the broad phase will fail. The narrow phase, which is slower, must then perform a collision check against each shape.

If you run into performance issues, you may have to make tradeoffs in terms of accuracy. Most games out there don't have a 100% accurate collision. They find creative ways to hide it or otherwise make it unnoticeable during normal gameplay.

---

## Collision shapes (3D)

This guide explains:

- The types of collision shapes available in 3D in Godot.
- Using a convex or a concave mesh as a collision shape.
- Performance considerations regarding 3D collisions.

Godot provides many kinds of collision shapes, with different performance and accuracy tradeoffs.

You can define the shape of a [PhysicsBody3D](../godot_gdscript_physics.md) by adding one or more [CollisionShape3Ds](../godot_gdscript_physics.md) as _direct_ child nodes. Indirect child nodes (i.e. children of child nodes) will be ignored and won't be used as collision shapes. Also, note that you must add a [Shape3D](../godot_gdscript_physics.md) _resource_ to collision shape nodes in the Inspector dock.

> **Note:** When you add multiple collision shapes to a single PhysicsBody, you don't have to worry about them overlapping. They won't "collide" with each other.

### Primitive collision shapes

Godot provides the following primitive collision shape types:

- [BoxShape3D](../godot_gdscript_misc.md)
- [SphereShape3D](../godot_gdscript_misc.md)
- [CapsuleShape3D](../godot_gdscript_misc.md)
- [CylinderShape3D](../godot_gdscript_misc.md)

You can represent the collision of most smaller objects using one or more primitive shapes. However, for more complex objects, such as a large ship or a whole level, you may need convex or concave shapes instead. More on that below.

We recommend favoring primitive shapes for dynamic objects such as RigidBodies and CharacterBodies as their behavior is the most reliable. They often provide better performance as well.

### Convex collision shapes

[Convex collision shapes](../godot_gdscript_misc.md) are a compromise between primitive collision shapes and concave collision shapes. They can represent shapes of any complexity, but with an important caveat. As their name implies, an individual shape can only represent a _convex_ shape. For instance, a pyramid is _convex_, but a hollow box is _concave_. To define a concave object with a single collision shape, you need to use a concave collision shape.

Depending on the object's complexity, you may get better performance by using multiple convex shapes instead of a concave collision shape. Godot lets you use _convex decomposition_ to generate convex shapes that roughly match a hollow object. Note this performance advantage no longer applies after a certain amount of convex shapes. For large and complex objects such as a whole level, we recommend using concave shapes instead.

You can generate one or several convex collision shapes from the editor by selecting a MeshInstance3D and using the **Mesh** menu at the top of the 3D viewport. The editor exposes two generation modes:

- **Create Single Convex Collision Sibling** uses the Quickhull algorithm. It creates one CollisionShape node with an automatically generated convex collision shape. Since it only generates a single shape, it provides good performance and is ideal for small objects.
- **Create Multiple Convex Collision Siblings** uses the V-HACD algorithm. It creates several CollisionShape nodes, each with a convex shape. Since it generates multiple shapes, it is more accurate for concave objects at the cost of performance. For objects with medium complexity, it will likely be faster than using a single concave collision shape.

### Concave or trimesh collision shapes

[Concave collision shapes](../godot_gdscript_misc.md), also called trimesh collision shapes, can take any form, from a few triangles to thousands of triangles. Concave shapes are the slowest option but are also the most accurate in Godot. **You can only use concave shapes within StaticBodies.** They will not work with CharacterBodies or RigidBodies unless the RigidBody's mode is Static.

> **Note:** Even though concave shapes offer the most accurate _collision_, contact reporting can be less precise than primitive shapes.

When not using GridMaps for level design, concave shapes are the best approach for a level's collision. That said, if your level has small details, you may want to exclude those from collision for performance and game feel. To do so, you can build a simplified collision mesh in a 3D modeler and have Godot generate a collision shape for it automatically. More on that below

Note that unlike primitive and convex shapes, a concave collision shape doesn't have an actual "volume". You can place objects both _outside_ of the shape as well as _inside_.

You can generate a concave collision shape from the editor by selecting a MeshInstance3D and using the **Mesh** menu at the top of the 3D viewport. The editor exposes two options:

- **Create Trimesh Static Body** is a convenient option. It creates a StaticBody containing a concave shape matching the mesh's geometry.
- **Create Trimesh Collision Sibling** creates a CollisionShape node with a concave shape matching the mesh's geometry.

> **See also:** See [Importing 3D scenes](tutorials_assets_pipeline.md) for information on how to export models for Godot and automatically generate collision shapes on import.

### Performance caveats

You aren't limited to a single collision shape per PhysicsBody. Still, we recommend keeping the number of shapes as low as possible to improve performance, especially for dynamic objects like RigidBodies and CharacterBodies. On top of that, avoid translating, rotating, or scaling CollisionShapes to benefit from the physics engine's internal optimizations.

When using a single non-transformed collision shape in a StaticBody, the engine's _broad phase_ algorithm can discard inactive PhysicsBodies. The _narrow phase_ will then only have to take into account the active bodies' shapes. If a StaticBody has many collision shapes, the broad phase will fail. The narrow phase, which is slower, must then perform a collision check against each shape.

If you run into performance issues, you may have to make tradeoffs in terms of accuracy. Most games out there don't have a 100% accurate collision. They find creative ways to hide it or otherwise make it unnoticeable during normal gameplay.

---

## 2D and 3D physics interpolation

Generally 2D and 3D physics interpolation work in very similar ways. However, there are a few differences, which will be described here.

### Global versus local interpolation

- In 3D, physics interpolation is performed _independently_ on the **global transform** of each 3D instance.
- In 2D by contrast, physics interpolation is performed on the **local transform** of each 2D instance.

This has some implications:

- In 3D, it is easy to turn interpolation on and off at the level of each `Node`, via the [physics_interpolation_mode](../godot_gdscript_misc.md) property in the Inspector, which can be set to `On`, `Off`, or `Inherited`.

- However this means that in 3D, pivots that occur in the `SceneTree` (due to parent child relationships) can only be interpolated **approximately** over the physics tick. In most cases this will not matter, but in some situations the interpolation can look slightly wrong.
- In 2D, interpolated local transforms are passed down to children during rendering. This means that if a parent has `physics_interpolation_mode` set to `On`, but the child is set to `Off`, the child will still be interpolated if the parent is moving. _Only the child's local transform is uninterpolated._ Controlling the on / off behavior of 2D nodes therefore requires a little more thought and planning.
- On the positive side, pivot behavior in the scene tree is perfectly preserved during interpolation in 2D, which gives super smooth behavior.

### Resetting physics interpolation

Whenever objects are moved to a completely new position, and interpolation is not desired (so as to prevent a "streaking" artefact), it is the responsibility of the user to call `reset_physics_interpolation()`.

The good news is that in 2D, this is automatically done for you when nodes first enter the tree. This reduces boiler plate, and reduces the effort required to get an existing project working.

> **Note:** If you move objects _after_ adding to the scene tree, you will still need to call `reset_physics_interpolation()` as with 3D.

### 2D Particles

Currently only `CPUParticles2D` are supported for physics interpolation in 2D. It is recommended to use a physics tick rate of at least 20-30 ticks per second to keep particles looking fluid.

`Particles2D` (GPU particles) are not yet interpolated, so for now it is recommended to convert to `CPUParticles2D` (but keep a backup of your `Particles2D` in case we get these working).

### Other

- `get_global_transform_interpolated()` is currently only available for 3D.
- `MultiMeshes` are supported in both 2D and 3D.
- Physics interpolation in 2D is implemented on the server side, which means it's effective on physics bodies created using [low-level servers](tutorials_performance.md). In contrast, physics interpolation in 3D is implemented on the scene side. This means it does not affect physics bodies created using servers. These must be interpolated manually instead. See the [pull request description](https://github.com/godotengine/godot/pull/104269) for the rationale on this design decision.

---

## Advanced physics interpolation

Although the previous instructions will give satisfactory results in a lot of games, in some cases you will want to go a stage further to get the best possible results and the smoothest possible experience.

### Exceptions to automatic physics interpolation

Even with physics interpolation active, there may be some local situations where you would benefit from disabling automatic interpolation for a [Node](../godot_gdscript_core.md) (or branch of the [SceneTree](../godot_gdscript_core.md)), and have the finer control of performing interpolation manually.

This is possible using the [Node.physics_interpolation_mode](../godot_gdscript_misc.md) property which is present in all Nodes. If you for example, turn off interpolation for a Node, the children will recursively also be affected (as they default to inheriting the parent setting). This means you can easily disable interpolation for an entire subscene.

The most common situation where you may want to perform your own interpolation is Cameras.

#### Cameras

In many cases, a [Camera3D](../godot_gdscript_nodes_3d.md) can use automatic interpolation just like any other node. However, for best results, especially at low physics tick rates, it is recommended that you take a manual approach to camera interpolation.

This is because viewers are very sensitive to camera movement. For instance, a Camera3D that realigns slightly every 1/10th of a second (at 10tps tick rate) will often be noticeable. You can get a much smoother result by moving the camera each frame in `_process`, and following an interpolated target manually.

#### Manual camera interpolation

##### Ensure the camera is using global coordinate space

The very first step when performing manual camera interpolation is to make sure the Camera3D transform is specified in _global space_ rather than inheriting the transform of a moving parent. This is because feedback can occur between the movement of a parent node of a Camera3D and the movement of the camera Node itself, which can mess up the interpolation.

There are two ways of doing this:

1. Move the Camera3D so it is independent on its own branch, rather than being a child of a moving object.

1. Call [Node3D.top_level](../godot_gdscript_nodes_3d.md) and set this to `true`, which will make the Camera ignore the transform of its parent.

##### Typical example

A typical example of a custom approach is to use the `look_at` function in the Camera3D every frame in `_process()` to look at a target node (such as the player).

But there is a problem. If we use the traditional `get_global_transform()` on a Camera3D "target" node, this transform will only focus the Camera3D on the target _at the current physics tick_. This is _not_ what we want, as the camera will jump about on each physics tick as the target moves. Even though the camera may be updated each frame, this does not help give smooth motion if the _target_ is only changing each physics tick.

##### get_global_transform_interpolated()

What we really want to focus the camera on, is not the position of the target on the physics tick, but the _interpolated_ position, i.e. the position at which the target will be rendered.

We can do this using the [Node3D.get_global_transform_interpolated](../godot_gdscript_nodes_3d.md) function. This acts exactly like getting [Node3D.global_transform](../godot_gdscript_nodes_3d.md) but it gives you the _interpolated_ transform (during a `_process()` call).

> **Important:** `get_global_transform_interpolated()` should only be used once or twice for special cases such as cameras. It should **not** be used all over the place in your code (both for performance reasons, and to give correct gameplay).

> **Note:** Aside from exceptions like the camera, in most cases, your game logic should be in `_physics_process()`. In game logic you should be calling `get_global_transform()` or `get_transform()`, which will give the current physics transform (in global or local space respectively), which is usually what you will want for gameplay code.

##### Example manual camera script

Here is an example of a simple fixed camera which follows an interpolated target:

```gdscript
extends Camera3D

# Node that the camera will follow
var _target

# We will smoothly lerp to follow the target
# rather than follow exactly
var _target_pos : Vector3 = Vector3()

func _ready() -> void:
    # Find the target node
    _target = get_node("../Player")

    # Turn off automatic physics interpolation for the Camera3D,
    # we will be doing this manually
    set_physics_interpolation_mode(Node.PHYSICS_INTERPOLATION_MODE_OFF)

func _process(delta: float) -> void:
    # Find the current interpolated transform of the target
    var tr : Transform = _target.get_global_transform_interpolated()

    # Provide some delayed smoothed lerping towards the target position
    _target_pos = lerp(_target_pos, tr.origin, min(delta, 1.0))

    # Fixed camera position, but it will follow the tar
# ...
```

##### Mouse look

Mouse look is a very common way of controlling cameras. But there is a problem. Unlike keyboard input which can be sampled periodically on the physics tick, mouse move events can come in continuously. The camera will be expected to react and follow these mouse movements on the next frame, rather than waiting until the next physics tick.

In this situation, it can be better to disable physics interpolation for the camera node (using [Node.physics_interpolation_mode](../godot_gdscript_misc.md)) and directly apply the mouse input to the camera rotation, rather than apply it in `_physics_process`.

Sometimes, especially with cameras, you will want to use a combination of interpolation and non-interpolation:

- A first person camera may position the camera at a player location (perhaps using [Node3D.get_global_transform_interpolated](../godot_gdscript_nodes_3d.md)), but control the Camera rotation from mouse look _without_ interpolation.
- A third person camera may similarly determine the look at (target location) of the camera using [Node3D.get_global_transform_interpolated](../godot_gdscript_nodes_3d.md), but position the camera using mouse look _without_ interpolation.

There are many permutations and variations of camera types, but it should be clear that in many cases, disabling automatic physics interpolation and handling this yourself can give a better result.

#### Disabling interpolation on other nodes

Although cameras are the most common example, there are a number of cases when you may wish other nodes to control their own interpolation, or be non-interpolated. Consider for example, a player in a top view game whose rotation is controlled by mouse look. Disabling physics rotation allows the player rotation to match the mouse in real-time.

#### MultiMeshes

Although most visual Nodes follow the single Node single visual instance paradigm, MultiMeshes can control several instances from the same Node. Therefore, they have some extra functions for controlling interpolation functionality on a _per-instance_ basis. You should explore these functions if you are using interpolated MultiMeshes.

- [MultiMesh.reset_instance_physics_interpolation](../godot_gdscript_rendering.md)
- [MultiMesh.set_buffer_interpolated](../godot_gdscript_rendering.md)

Full details are in the [MultiMesh](../godot_gdscript_rendering.md) documentation.

---

## Introduction

### Physics ticks and rendered frames

One key concept to understand in Godot is the distinction between physics ticks (sometimes referred to as iterations or physics frames), and rendered frames. The physics proceeds at a fixed tick rate (set in [Project Settings > Physics > Common > Physics Tick per Second](../godot_gdscript_misc.md)), which defaults to 60 ticks per second.

However, the engine does not necessarily **render** at the same rate. Although many monitors refresh at 60 Hz (cycles per second), many refresh at completely different frequencies (e.g. 75 Hz, 144 Hz, 240 Hz or more). Even though a monitor may be able to show a new frame e.g. 60 times a second, there is no guarantee that the CPU and GPU will be able to _supply_ frames at this rate. For instance, when running with V-Sync, the computer may be too slow for 60 and only reach the deadlines for 30 FPS, in which case the frames you see will change at 30 FPS (resulting in stuttering).

But there is a problem here. What happens if the physics ticks do not coincide with frames? What happens if the physics tick rate is out of phase with the frame rate? Or worse, what happens if the physics tick rate is _lower_ than the rendered frame rate?

This problem is easier to understand if we consider an extreme scenario. If you set the physics tick rate to 10 ticks per second, in a simple game with a rendered frame rate of 60 FPS. If we plot a graph of the positions of an object against the rendered frames, you can see that the positions will appear to "jump" every 1/10th of a second, rather than giving a smooth motion. When the physics calculates a new position for a new object, it is not rendered in this position for just one frame, but for 6 frames.

This jump can be seen in other combinations of tick / frame rate as glitches, or jitter, caused by this staircasing effect due to the discrepancy between physics tick time and rendered frame time.

### What can we do about frames and ticks being out of sync?

#### Lock the tick / frame rate together?

The most obvious solution is to get rid of the problem, by ensuring there is a physics tick that coincides with every frame. This used to be the approach on old consoles and fixed hardware computers. If you know that every player will be using the same hardware, you can ensure it is fast enough to calculate ticks and frames at e.g. 50 FPS, and you will be sure it will work great for everybody.

However, modern games are often no longer made for fixed hardware. You will often be planning to release on desktop computers, mobiles, and more. All of which have huge variations in performance, as well as different monitor refresh rates. We need to come up with a better way of dealing with the problem.

#### Adapt the tick rate?

Instead of designing the game at a fixed physics tick rate, we could allow the tick rate to scale according to the end user's hardware. We could for example use a fixed tick rate that works for that hardware, or even vary the duration of each physics tick to match a particular frame duration.

This works, but there is a problem. Physics (_and game logic_, which is often also run in the `_physics_process`) work best and most consistently when run at a **fixed**, predetermined tick rate. If you attempt to run a racing game physics that has been designed for 60 TPS (ticks per second) at e.g. 10 TPS, the physics will behave completely differently. Controls may be less responsive, collisions / trajectories can be completely different. You may test your game thoroughly at 60 TPS, then find it breaks on end users' machines when it runs at a different tick rate.

This can make quality assurance difficult with hard to reproduce bugs, especially in AAA games where problems of this sort can be very costly. This can also be problematic for multiplayer games for competitive integrity, as running the game at certain tick rates may be more advantageous than others.

#### Lock the tick rate, but use interpolation to smooth frames in between physics ticks

This has become one of the most popular approaches to deal with the problem, although it is optional and disabled by default.

We have established that the most desirable physics/game logic arrangement for consistency and predictability is a physics tick rate that is fixed at design-time. The problem is the discrepancy between the physics position recorded, and where we "want" a physics object to be shown on a frame to give smooth motion.

The answer turns out to be simple, but can be a little hard to get your head around at first.

Instead of keeping track of just the current position of a physics object in the engine, we keep track of _both the current position of the object, and the previous position_ on the previous physics tick.

Why do we need the previous position _(in fact the entire transform, including rotation and scaling)_? By using a little math magic, we can use **interpolation** to calculate what the transform of the object would be between those two points, in our ideal world of smooth continuous movement.

#### Linear interpolation

The simplest way to achieve this is linear interpolation, or lerping, which you may have used before.

Let us consider only the position, and a situation where we know that the previous physics tick X coordinate was 10 units, and the current physics tick X coordinate is 30 units.

> **Note:** Although the maths is explained here, you do not have to worry about the details, as this step will be performed for you. Under the hood, Godot may use more complex forms of interpolation, but linear interpolation is the easiest in terms of explanation.

#### The physics interpolation fraction

If our physics ticks are happening 10 times per second (for this example), what happens if our rendered frame takes place at time 0.12 seconds? We can do some math to figure out where the object would be to obtain a smooth motion between the two ticks.

First of all, we have to calculate how far through the physics tick we want the object to be. If the last physics tick took place at 0.1 seconds, we are 0.02 seconds _(0.12 - 0.1)_ through a tick that we know will take 0.1 seconds (10 ticks per second). The fraction through the tick is thus:

```gdscript
fraction = 0.02 / 0.10
fraction = 0.2
```

This is called the **physics interpolation fraction**, and is handily calculated for you by Godot. It can be retrieved on any frame by calling [Engine.get_physics_interpolation_fraction](../godot_gdscript_core.md).

#### Calculating the interpolated position

Once we have the interpolation fraction, we can insert it into a standard linear interpolation equation. The X coordinate would thus be:

```gdscript
x_interpolated = x_prev + ((x_curr - x_prev) * 0.2)
```

So substituting our `x_prev` as 10, and `x_curr` as 30:

```gdscript
x_interpolated = 10 + ((30 - 10) * 0.2)
x_interpolated = 10 + 4
x_interpolated = 14
```

Let's break that down:

- We know the X starts from the coordinate on the previous tick (`x_prev`) which is 10 units.
- We know that after the full tick, the difference between the current tick and the previous tick will have been added (`x_curr - x_prev`) (which is 20 units).
- The only thing we need to vary is the proportion of this difference we add, according to how far we are through the physics tick.

> **Note:** Although this example interpolates the position, the same thing can be done with the rotation and scale of objects. It is not necessary to know the details as Godot will do all this for you.

#### Smoothed transformations between physics ticks?

Putting all this together shows that it should be possible to have a nice smooth estimation of the transform of objects between the current and previous physics tick.

But wait, you may have noticed something. If we are interpolating between the current and previous ticks, we are not estimating the position of the object _now_, we are estimating the position of the object in the past. To be exact, we are estimating the position of the object _between 1 and 2 ticks_ into the past.

#### In the past

What does this mean? This scheme does work, but it does mean we are effectively introducing a delay between what we see on the screen, and where the objects _should_ be.

In practice, most people won't notice this delay, or rather, it is typically not _objectionable_. There are already significant delays involved in games, we just don't typically notice them. The most significant effect is there can be a slight delay to input, which can be a factor in fast twitch games. In some of these fast input situations, you may wish to turn off physics interpolation and use a different scheme, or use a high tick rate, which mitigates these delays.

#### Why look into the past? Why not predict the future?

There is an alternative to this scheme, which is: instead of interpolating between the previous and current tick, we use maths to _extrapolate_ into the future. We try to predict where the object _will be_, rather than show it where it was. This can be done and may be offered as an option in future, but there are some significant downsides:

- The prediction may not be correct, especially when an object collides with another object during the physics tick.
- Where a prediction was incorrect, the object may extrapolate into an "impossible" position, like inside a wall.
- Providing the movement speed is slow, these incorrect predictions may not be too much of a problem.
- When a prediction was incorrect, the object may have to jump or snap back onto the corrected path. This can be visually jarring.

#### Fixed timestep interpolation

In Godot this whole system is referred to as physics interpolation, but you may also hear it referred to as **"fixed timestep interpolation"**, as it is interpolating between objects moved with a fixed timestep (physics ticks per second). In some ways the second term is more accurate, because it can also be used to interpolate objects that are not driven by physics.

> **Tip:** Although physics interpolation is usually a good choice, there are exceptions where you may choose not to use Godot's built-in physics interpolation (or use it in a limited fashion). An example category is internet multiplayer games. Multiplayer games often receive tick or timing based information from other players or a server and these may not coincide with local physics ticks, so a custom interpolation technique can often be a better fit.

---

## Quick start guide

- Turn on physics interpolation: [Project Settings > Physics > Common > Physics Interpolation](../godot_gdscript_misc.md)
- Make sure you move objects and run your game logic in `_physics_process()` rather than `_process()`. This includes moving objects directly _and indirectly_ (by e.g. moving a parent, or using another mechanism to automatically move nodes).
- Be sure to call [Node.reset_physics_interpolation](../godot_gdscript_misc.md) on nodes _after_ you first position or teleport them, to prevent "streaking".
- Temporarily try setting [Project Settings > Physics > Common > Physics Ticks per Second](../godot_gdscript_misc.md) to 10 to see the difference with and without interpolation.

---

## Using physics interpolation

How do we incorporate physics interpolation into a Godot game? Are there any caveats?

We have tried to make the system as easy to use as possible, and many existing games will work with few changes. That said there are some situations which require special treatment, and these will be described.

### Turn on the physics interpolation setting

The first step is to turn on physics interpolation in [Project Settings > Physics > Common > Physics Interpolation](../godot_gdscript_misc.md) You can now run your game.

It is likely that nothing looks hugely different, particularly if you are running physics at 60 TPS or a multiple of it. However, quite a bit more is happening behind the scenes.

> **Tip:** To convert an existing game to use interpolation, it is highly recommended that you temporarily set [Project Settings > Physics > Common > Physics Tick per Second](../godot_gdscript_misc.md) to a low value such as `10`, which will make interpolation problems more obvious.

### Move (almost) all game logic from \_process to \_physics_process

The most fundamental requirement for physics interpolation (which you may be doing already) is that you should be moving and performing game logic on your objects within `_physics_process` (which runs at a physics tick) rather than `_process` (which runs on a rendered frame). This means your scripts should typically be doing the bulk of their processing within `_physics_process`, including responding to input and AI.

Setting the transform of objects only within physics ticks allows the automatic interpolation to deal with transforms _between_ physics ticks, and ensures the game will run the same whatever machine it is run on. As a bonus, this also reduces CPU usage if the game is rendering at high FPS, since AI logic (for example) will no longer run on every rendered frame.

> **Note:** If you attempt to set the transform of interpolated objects _outside_ the physics tick, the calculations for the interpolated position will be incorrect, and you will get jitter. This jitter may not be visible on your machine, but it _will_ occur for some players. For this reason, setting the transform of interpolated objects should be avoided outside of the physics tick. Godot will attempt to produce warnings in the editor if this case is detected.

> **Tip:** This is only a _soft rule_. There are some occasions where you might want to teleport objects outside of the physics tick (for instance when starting a level, or respawning objects). Still, in general, you should be applying transforms from the physics tick.

### Ensure that all indirect movement happens during physics ticks

Consider that in Godot, nodes can be moved not just directly in your own scripts, but also by automatic methods such as tweening, animation, and navigation. All these methods should also have their timing set to operate on the physics tick rather than each frame ("idle"), **if** you are using them to move objects (_these methods can also be used to control properties that are not interpolated_).

> **Note:** Also consider that nodes can be moved not just by moving themselves, but also by moving parent nodes in the [SceneTree](../godot_gdscript_core.md). The movement of parents should therefore also only occur during physics ticks.

### Choose a physics tick rate

When using physics interpolation, the rendering is decoupled from physics, and you can choose any value that makes sense for your game. You are no longer limited to values that are multiples of the user's monitor refresh rate (for stutter-free gameplay if the target FPS is reached).

As a rough guide:

| Low tick rates (10-30)   | Medium tick rates (30-60)               | High tick rates (60+)  |
| ------------------------ | --------------------------------------- | ---------------------- |
| Better CPU performance   | Good physics behavior in complex scenes | Good with fast physics |
| Add some delay to input  | Good for first person games             | Good for racing games  |
| Simple physics behaviour |                                         |                        |

> **Note:** You can always change the tick rate as you develop, it is as simple as changing the project setting.

### Call reset_physics_interpolation() when teleporting objects

Most of the time, interpolation is what you want between two physics ticks. However, there is one situation in which it may _not_ be what you want. That is when you are initially placing objects, or moving them to a new location. Here, you don't want a smooth motion between where the object was (e.g. the origin) and the initial position - you want an instantaneous move.

The solution to this is to call the [Node.reset_physics_interpolation](../godot_gdscript_misc.md) function. What this function does under the hood is set the internally stored _previous transform_ of the object to be equal to the _current transform_. This ensures that when interpolating between these two equal transforms, there will be no movement.

Even if you forget to call this, it will usually not be a problem in most situations (especially at high tick rates). This is something you can easily leave to the polishing phase of your game. The worst that will happen is seeing a streaking motion for a frame or so when you move them - you will know when you need it!

There are actually two ways to use `reset_physics_interpolation()`:

_Standing start (e.g. player)_

1. Set the initial transform
2. Call `reset_physics_interpolation()`

The previous and current transforms will be identical, resulting in no initial movement.

_Moving start (e.g. bullet)_

1. Set the initial transform
2. Call `reset_physics_interpolation()`
3. Immediately set the transform expected after the first tick of motion

The previous transform will be the starting position, and the current transform will act as though a tick of simulation has already taken place. This will immediately start moving the object, instead of having a tick delay standing still.

> **Important:** Make sure you set the transform and call `reset_physics_interpolation()` in the correct order as shown above, otherwise you will see unwanted "streaking".

### Testing and debugging tips

Even if you intend to run physics at 60 TPS, in order to thoroughly test your interpolation and get the smoothest gameplay, it is highly recommended to temporarily set the physics tick rate to a low value such as 10 TPS.

The gameplay may not work perfectly, but it should enable you to more easily see cases where you should be calling [Node.reset_physics_interpolation](../godot_gdscript_misc.md), or where you should be using your own custom interpolation on e.g. a [Camera3D](../godot_gdscript_nodes_3d.md). Once you have these cases fixed, you can set the physics tick rate back to the desired setting.

The other great advantage to testing at a low tick rate is you can often notice other game systems that are synchronized to the physics tick and creating glitches which you may want to work around. Typical examples include setting animation blend values, which you may decide to set in `_process()` and interpolate manually.

> **Note:** In 2D, the position of visible collision shapes shown by the Debug > Visible Collision Shapes option **will** take physics interpolation into account. By contrast, in 3D, the position of visible collision shapes **will not** take physics interpolation into account. This means the visible collision shapes can appear to move less smoothly and appear slightly in front of the object's visual representation when the object is moving. This is not a bug, but a consequence of how physics interpolation is implemented in 3D.

---

## Kinematic character (2D)

### Introduction

Yes, the name sounds strange. "Kinematic Character". What is that? The reason for the name is that, when physics engines came out, they were called "Dynamics" engines (because they dealt mainly with collision responses). Many attempts were made to create a character controller using the dynamics engines, but it wasn't as easy as it seemed. Godot has one of the best implementations of dynamic character controller you can find (as it can be seen in the 2d/platformer demo), but using it requires a considerable level of skill and understanding of physics engines (or a lot of patience with trial and error).

Some physics engines, such as Havok seem to swear by dynamic character controllers as the best option, while others (PhysX) would rather promote the kinematic one.

So, what is the difference?:

- A **dynamic character controller** uses a rigid body with an infinite inertia tensor. It's a rigid body that can't rotate. Physics engines always let objects move and collide, then solve their collisions all together. This makes dynamic character controllers able to interact with other physics objects seamlessly, as seen in the platformer demo. However, these interactions are not always predictable. Collisions can take more than one frame to be solved, so a few collisions may seem to displace a tiny bit. Those problems can be fixed, but require a certain amount of skill.
- A **kinematic character controller** is assumed to always begin in a non-colliding state, and will always move to a non-colliding state. If it starts in a colliding state, it will try to free itself like rigid bodies do, but this is the exception, not the rule. This makes their control and motion a lot more predictable and easier to program. However, as a downside, they can't directly interact with other physics objects, unless done by hand in code.

This short tutorial focuses on the kinematic character controller. It uses the old-school way of handling collisions, which is not necessarily simpler under the hood, but well hidden and presented as an API.

### Physics process

To manage the logic of a kinematic body or character, it is always advised to use physics process, because it's called before physics step and its execution is in sync with physics server, also it is called the same amount of times per second, always. This makes physics and motion calculation work in a more predictable way than using regular process, which might have spikes or lose precision if the frame rate is too high or too low.

```gdscript
extends CharacterBody2D

func _physics_process(delta):
    pass
```

### Scene setup

To have something to test, here's the scene (from the tilemap tutorial): [kinematic_character_2d_starter.zip](https://github.com/godotengine/godot-docs-project-starters/releases/download/latest-4.x/kinematic_character_2d_starter.zip). We'll be creating a new scene for the character. Use the robot sprite and create a scene like this:

You'll notice that there's a warning icon next to our CollisionShape2D node; that's because we haven't defined a shape for it. Create a new CircleShape2D in the shape property of CollisionShape2D. Click on <CircleShape2D> to go to the options for it, and set the radius to 30:

**Note: As mentioned before in the physics tutorial, the physics engine can't handle scale on most types of shapes (only collision polygons, planes and segments work), so always change the parameters (such as radius) of the shape instead of scaling it. The same is also true for the kinematic/rigid/static bodies themselves, as their scale affects the shape scale.**

Now, create a script for the character, the one used as an example above should work as a base.

Finally, instance that character scene in the tilemap, and make the map scene the main one, so it runs when pressing play.

### Moving the kinematic character

Go back to the character scene, and open the script, the magic begins now! Kinematic body will do nothing by default, but it has a useful function called `CharacterBody2D.move_and_collide()`. This function takes a [Vector2](../godot_gdscript_math_types.md) as an argument, and tries to apply that motion to the kinematic body. If a collision happens, it stops right at the moment of the collision.

So, let's move our sprite downwards until it hits the floor:

```gdscript
extends CharacterBody2D

func _physics_process(delta):
    move_and_collide(Vector2(0, 1)) # Move down 1 pixel per physics frame
```

The result is that the character will move, but stop right when hitting the floor. Pretty cool, huh?

The next step will be adding gravity to the mix, this way it behaves a little more like a regular game character:

```gdscript
extends CharacterBody2D

const GRAVITY = 200.0

func _physics_process(delta):
    velocity.y += delta * GRAVITY

    var motion = velocity * delta
    move_and_collide(motion)
```

Now the character falls smoothly. Let's make it walk to the sides, left and right when touching the directional keys. Remember that the values being used (for speed at least) are pixels/second.

This adds basic support for walking when pressing left and right:

```gdscript
extends CharacterBody2D

const GRAVITY = 200.0
const WALK_SPEED = 200

func _physics_process(delta):
    velocity.y += delta * GRAVITY

    if Input.is_action_pressed("ui_left"):
        velocity.x = -WALK_SPEED
    elif Input.is_action_pressed("ui_right"):
        velocity.x =  WALK_SPEED
    else:
        velocity.x = 0

    # "move_and_slide" already takes delta time into account.
    move_and_slide()
```

And give it a try.

This is a good starting point for a platformer. A more complete demo can be found in the demo zip distributed with the engine, or in the [https://github.com/godotengine/godot-demo-projects/tree/master/2d/kinematic_character](https://github.com/godotengine/godot-demo-projects/tree/master/2d/kinematic_character).

---
