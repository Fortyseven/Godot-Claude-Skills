# Godot 4 GDScript Tutorials — Physics (Part 2)

> 6 tutorials. GDScript-specific code examples.

## Large world coordinates

> **Note:** Large world coordinates are mainly useful in 3D projects; they are rarely required in 2D projects. Also, unlike 3D rendering, 2D rendering currently doesn't benefit from increased precision when large world coordinates are enabled.

### Why use large world coordinates?

In Godot, physics simulation and rendering both rely on _floating-point_ numbers. However, in computing, floating-point numbers have **limited precision and range**. This can be a problem for games with huge worlds, such as space or planetary-scale simulation games.

Precision is the greatest when the value is close to `0.0`. Precision becomes gradually lower as the value increases or decreases away from `0.0`. This occurs every time the floating-point number's _exponent_ increases, which happens when the floating-point number surpasses a power of 2 value (2, 4, 8, 16, …). Every time this occurs, the number's minimum step will _increase_, resulting in a loss of precision.

In practice, this means that as the player moves away from the world origin (`Vector2(0, 0)` in 2D games or `Vector3(0, 0, 0)` in 3D games), precision will decrease.

This loss of precision can result in objects appearing to "vibrate" when far away from the world origin, as the model's position will snap to the nearest value that can be represented in a floating-point number. This can also result in physics glitches that only occur when the player is far from the world origin.

The range determines the minimum and maximum values that can be stored in the number. If the player tries to move past this range, they will simply not be able to. However, in practice, floating-point precision almost always becomes a problem before the range does.

The range and precision (minimum step between two exponent intervals) are determined by the floating-point number type. The _theoretical_ range allows extremely high values to be stored in single-precision floats, but with very low precision. In practice, a floating-point type that cannot represent all integer values is not very useful. At extreme values, precision becomes so low that the number cannot even distinguish two separate _integer_ values from each other.

This is the range where individual integer values can be represented in a floating-point number:

- **Single-precision float range (represent all integers):** Between -16,777,216 and 16,777,216
- **Double-precision float range (represent all integers):** Between -9 quadrillion and 9 quadrillion

| Range | Single step | Double step | Comment |
| [1; 2] | ~0.0000001 | ~1e-15 | Precision becomes greater near 0.0 (this table is abbreviated). |
| [2; 4] | ~0.0000002 | ~1e-15 | |
| [4; 8] | ~0.0000005 | ~1e-15 | |
| [8; 16] | ~0.000001 | ~1e-14 | |
| [16; 32] | ~0.000002 | ~1e-14 | |
| [32; 64] | ~0.000004 | ~1e-14 | |
| [64; 128] | ~0.000008 | ~1e-13 | |
| [128; 256] | ~0.000015 | ~1e-13 | |
| [256; 512] | ~0.00003 | ~1e-13 | |
| [512; 1024] | ~0.00006 | ~1e-12 | |
| [1024; 2048] | ~0.0001 | ~1e-12 | |
| [2048; 4096] | ~0.0002 | ~1e-12 | Maximum recommended single-precision range for a first-person 3D game without rendering artifacts or physics glitches. |
| [4096; 8192] | ~0.0005 | ~1e-12 | Maximum recommended single-precision range for a third-person 3D game without rendering artifacts or physics glitches. |
| [8192; 16384] | ~0.001 | ~1e-12 | |
| [16384; 32768] | ~0.0019 | ~1e-11 | Maximum recommended single-precision range for a top-down 3D game without rendering artifacts or physics glitches. |
| [32768; 65536] | ~0.0039 | ~1e-11 | Maximum recommended single-precision range for any 3D game. Double precision (large world coordinates) is usually required past this point. |
| [65536; 131072] | ~0.0078 | ~1e-11 | |
| [131072; 262144] | ~0.0156 | ~1e-10 | |
| > 262144 | > ~0.0313 | ~1e-10 (0.0000000001) | Double-precision remains far more precise than single-precision past this value. |

When using single-precision floats, it is possible to go past the suggested ranges, but more visible artifacting will occur and physics glitches will be more common (such as the player not walking straight in certain directions).

> **See also:** See the [Demystifying Floating Point Precision](https://blog.demofox.org/2017/11/21/) article for more information.

### How large world coordinates work

Large world coordinates (also known as **double-precision physics**) increase the precision level of all floating-point computations within the engine.

By default, [float](../godot_gdscript_misc.md) is 64-bit in GDScript, but [Vector2](../godot_gdscript_math_types.md), [Vector3](../godot_gdscript_math_types.md) and [Vector4](../godot_gdscript_math_types.md) are 32-bit. This means that the precision of vector types is much more limited. To resolve this, we can increase the number of bits used to represent a floating-point number in a Vector type. This results in an _exponential_ increase in precision, which means the final value is not just twice as precise, but potentially thousands of times more precise at high values. The maximum value that can be represented is also greatly increased by going from a single-precision float to a double-precision float.

To avoid model snapping issues when far away from the world origin, Godot's 3D rendering engine will increase its precision for rendering operations when large world coordinates are enabled. The shaders do not use double-precision floats for performance reasons, but an [alternative solution](https://github.com/godotengine/godot/pull/66178) is used to emulate double precision for rendering using single-precision floats.

> **Note:** Enabling large world coordinates comes with a performance and memory usage penalty, especially on 32-bit CPUs. Only enable large world coordinates if you actually need them. This feature is tailored towards mid-range/high-end desktop platforms. Large world coordinates may not perform well on low-end mobile devices, unless you take steps to reduce CPU usage with other means (such as decreasing the number of physics ticks per second). On low-end platforms, an _origin shifting_ approach can be used instead to allow for large worlds without using double-precision physics and rendering. Origin shifting works with single-precision floats, but it introduces more complexity to game logic, especially in multiplayer games. Therefore, origin shifting is not detailed on this page.

### Who are large world coordinates for?

Large world coordinates are typically required for 3D space or planetary-scale simulation games. This extends to games that require supporting _very_ fast movement speeds, but also very slow _and_ precise movements at times.

On the other hand, it's important to only use large world coordinates when actually required (for performance reasons). Large world coordinates are usually **not** required for:

- 2D games, as precision issues are usually less noticeable.
- Games with small-scale or medium-scale worlds.
- Games with large worlds, but split into different levels with loading sequences in between. You can center each level portion around the world origin to avoid precision issues without a performance penalty.
- Open world games with a _playable on-foot area_ not exceeding 8192×8192 meters (centered around the world origin). As shown in the above table, the level of precision remains acceptable within that range, even for a first-person game.

**If in doubt**, you probably don't need to use large world coordinates in your project. For reference, most modern AAA open world titles don't use a large world coordinates system and still rely on single-precision floats for both rendering and physics.

### Enabling large world coordinates

This process requires recompiling the editor and all export template binaries you intend to use. If you only intend to export your project in release mode, you can skip the compilation of debug export templates. In any case, you'll need to compile an editor build so you can test your large precision world without having to export the project every time.

See the Compiling section for compiling instructions for each target platform. You will need to add the `precision=double` SCons option when compiling the editor and export templates.

The resulting binaries will be named with a `.double` suffix to distinguish them from single-precision binaries (which lack any precision suffix). You can then specify the binaries as custom export templates in your project's export presets in the Export dialog.

### Compatibility between single-precision and double-precision builds

When saving a _binary_ resource using the [ResourceSaver](../godot_gdscript_core.md) singleton, a special flag is stored in the file if the resource was saved using a build that uses double-precision numbers. As a result, all binary resources will change on disk when you switch to a double-precision build and save over them.

Both single-precision and double-precision builds support using the [ResourceLoader](../godot_gdscript_core.md) singleton on resources that use this special flag. This means single-precision builds can load resources saved using double-precision builds and vice versa. Text-based resources don't store a double-precision flag, as they don't require such a flag for correct reading.

#### Known incompatibilities

- In a networked multiplayer game, the server and all clients should be using the same build type to ensure precision remains consistent across clients. Using different build types _may_ work, but various issues can occur.
- The GDExtension API changes in an incompatible way in double-precision builds. This means extensions **must** be rebuilt to work with double-precision builds. On the extension developer's end, the `REAL_T_IS_DOUBLE` define is enabled when building a GDExtension with `precision=double`. `real_t` can be used as an alias for `float` in single-precision builds, and `double` in double-precision builds.

### Limitations

Since 3D rendering shaders don't actually use double-precision floats, there are some limitations when it comes to 3D rendering precision:

- [Triplanar mapping](tutorials_3d.md) doesn't benefit from increased precision. Materials using triplanar mapping will exhibit visible jittering when far away from the world origin.
- [GPUParticles3D](../godot_gdscript_misc.md) nodes with **Local Coords** disabled will not benefit from increased precision. This can cause visible particle snapping to occur when far away from the world origin. Nodes with **Local Coords** enabled, as well as [CPUParticles3D](../godot_gdscript_misc.md) nodes, will still benefit from increased precision.
- Shaders using the `skip_vertex_transform` or `world_vertex_coords` render modes don't benefit from increased precision.
- In double-precision builds, world space coordinates in a shader `fragment()` function can't be reconstructed from view space, for example:

```glsl
vec3 world = (INV_VIEW_MATRIX * vec4(VERTEX, 1.0)).xyz;
```

Instead, calculate the world space coordinates in the `vertex()` function and pass them using a [varying](tutorials_shaders.md), for example:

```glsl
varying vec3 world;
void vertex() {
    world = (MODEL_MATRIX * vec4(VERTEX, 1.0)).xyz;
}
```

2D rendering currently doesn't benefit from increased precision when large world coordinates are enabled. This can cause visible model snapping to occur when far away from the world origin (starting from a few million pixels at typical zoom levels). 2D physics calculations will still benefit from increased precision though.

---

## Physics introduction

In game development, you often need to know when two objects in the game intersect or come into contact. This is known as **collision detection**. When a collision is detected, you typically want something to happen. This is known as **collision response**.

Godot offers a number of collision objects in 2D and 3D to provide both collision detection and response. Trying to decide which one to use for your project can be confusing. You can avoid problems and simplify development if you understand how each works and what their pros and cons are.

In this guide, you will learn:

- Godot's four collision object types
- How each collision object works
- When and why to choose one type over another

> **Note:** This document's examples will use 2D objects. Every 2D physics object and collision shape has a direct equivalent in 3D and in most cases they work in much the same way.

### Collision objects

Godot offers four kinds of collision objects which all extend [CollisionObject2D](../godot_gdscript_nodes_2d.md). The last three listed below are physics bodies and additionally extend [PhysicsBody2D](../godot_gdscript_physics.md).

- **Area2D**
  : `Area2D` nodes provide **detection** and **influence**. They can detect when objects overlap and can emit signals when bodies enter or exit. An `Area2D` can also be used to override physics properties, such as gravity or damping, in a defined area.
- **StaticBody2D**
  : A static body is one that is not moved by the physics engine. It participates in collision detection, but does not move in response to the collision. They are most often used for objects that are part of the environment or that do not need to have any dynamic behavior.
- **RigidBody2D**
  : This is the node that implements simulated 2D physics. You do not control a `RigidBody2D` directly, but instead you apply forces to it (gravity, impulses, etc.) and the physics engine calculates the resulting movement. Read more about using rigid bodies.
- **CharacterBody2D**
  : A body that provides collision detection, but no physics. All movement and collision response must be implemented in code.

#### Physics material

Static bodies and rigid bodies can be configured to use a [PhysicsMaterial](../godot_gdscript_physics.md). This allows adjusting the friction and bounce of an object, and set if it's absorbent and/or rough.

#### Collision shapes

A physics body can hold any number of [Shape2D](../godot_gdscript_physics.md) objects as children. These shapes are used to define the object's collision bounds and to detect contact with other objects.

> **Note:** In order to detect collisions, at least one `Shape2D` must be assigned to the object.

The most common way to assign a shape is by adding a [CollisionShape2D](../godot_gdscript_nodes_2d.md) or [CollisionPolygon2D](../godot_gdscript_nodes_2d.md) as a child of the object. These nodes allow you to draw the shape directly in the editor workspace.

> **Important:** Be careful to never scale your collision shapes in the editor. The "Scale" property in the Inspector should remain `(1, 1)`. When changing the size of the collision shape, you should always use the size handles, **not** the `Node2D` scale handles. Scaling a shape can result in unexpected collision behavior.

#### Physics process callback

The physics engine runs at a fixed rate (a default of 60 iterations per second). This rate is typically different from the frame rate which fluctuates based on what is rendered and available resources.

It is important that all physics related code runs at this fixed rate. Therefore Godot differentiates [between physics and idle processing](tutorials_scripting.md). Code that runs each frame is called idle processing and code that runs on each physics tick is called physics processing. Godot provides two different callbacks, one for each of those processing rates.

The physics callback, [Node.\_physics_process()](../godot_gdscript_misc.md), is called before each physics step. Any code that needs to access a body's properties should be run in here. This method will be passed a `delta` parameter, which is a floating-point number equal to the time passed in _seconds_ since the last step. When using the default 60 Hz physics update rate, it will typically be equal to `0.01666...` (but not always, see below).

> **Note:** It's recommended to always use the `delta` parameter when relevant in your physics calculations, so that the game behaves correctly if you change the physics update rate or if the player's device can't keep up.

#### Collision layers and masks

One of the most powerful, but frequently misunderstood, collision features is the collision layer system. This system allows you to build up complex interactions between a variety of objects. The key concepts are **layers** and **masks**. Each `CollisionObject2D` has 32 different physics layers it can interact with.

Let's look at each of the properties in turn:

- **collision_layer**
  : This describes the layers that the object appears **in**. By default, all bodies are on layer `1`.
- **collision_mask**
  : This describes what layers the body will **scan** for collisions. If an object isn't in one of the mask layers, the body will ignore it. By default, all bodies scan layer `1`.

These properties can be configured via code, or by editing them in the Inspector.

Keeping track of what you're using each layer for can be difficult, so you may find it useful to assign names to the layers you're using. Names can be assigned in **Project Settings > Layer Names > 2D Physics**.

##### GUI example

You have four node types in your game: Walls, Player, Enemy, and Coin. Both Player and Enemy should collide with Walls. The Player node should detect collisions with both Enemy and Coin, but Enemy and Coin should ignore each other.

Start by naming layers 1-4 "walls", "player", "enemies", and "coins" and place each node type in its respective layer using the "Layer" property. Then set each node's "Mask" property by selecting the layers it should interact with. For example, the Player's settings would look like this:

##### Code example

In function calls, layers are specified as a bitmask. Where a function enables all layers by default, the layer mask will be given as `0xffffffff`. Your code can use binary, hexadecimal, or decimal notation for layer masks, depending on your preference.

The code equivalent of the above example where layers 1, 3 and 4 were enabled would be as follows:

```gdscript
# Example: Setting mask value for enabling layers 1, 3 and 4

# Binary - set the bit corresponding to the layers you want to enable (1, 3, and 4) to 1, set all other bits to 0.
# Note: Layer 32 is the first bit, layer 1 is the last. The mask for layers 4, 3 and 1 is therefore:
0b00000000_00000000_00000000_00001101
# (This can be shortened to 0b1101)

# Hexadecimal equivalent (1101 binary converted to hexadecimal).
0x000d
# (This value can be shortened to 0xd.)

# Decimal - Add the results of 2 to the power of (layer to be enabled - 1).
# (2^(1-1)) + (2^(3-1)) + (2^(4-1)) = 1 + 4 + 8 = 13
#
# We can use the `<<` operator to shift the bit to the left by the layer number we want to enable.
# This is a faster way to multiply by powers of 2 than `pow()`.
# Additionally, we use the `|` (binary O
# ...
```

You can also set bits independently by calling `set_collision_layer_value(layer_number, value)` or `set_collision_mask_value(layer_number, value)` on any given [CollisionObject2D](../godot_gdscript_nodes_2d.md) as follows:

```gdscript
# Example: Setting mask value to enable layers 1, 3, and 4.

var collider: CollisionObject2D = $CollisionObject2D  # Any given collider.
collider.set_collision_mask_value(1, true)
collider.set_collision_mask_value(3, true)
collider.set_collision_mask_value(4, true)
```

Export annotations can be used to export bitmasks in the editor with a user-friendly GUI:

```gdscript
@export_flags_2d_physics var layers_2d_physics
```

Additional export annotations are available for render and navigation layers, in both 2D and 3D. See [Exporting bit flags](tutorials_scripting.md).

### Area2D

Area nodes provide **detection** and **influence**. They can detect when objects overlap and emit signals when bodies enter or exit. Areas can also be used to override physics properties, such as gravity or damping, in a defined area.

There are three main uses for [Area2D](../godot_gdscript_physics.md):

- Overriding physics parameters (such as gravity) in a given region.
- Detecting when other bodies enter or exit a region or what bodies are currently in a region.
- Checking other areas for overlap.

By default, areas also receive mouse and touchscreen input.

### StaticBody2D

A static body is one that is not moved by the physics engine. It participates in collision detection, but does not move in response to the collision. However, it can impart motion or rotation to a colliding body **as if** it were moving, using its `constant_linear_velocity` and `constant_angular_velocity` properties.

`StaticBody2D` nodes are most often used for objects that are part of the environment or that do not need to have any dynamic behavior.

Example uses for `StaticBody2D`:

- Platforms (including moving platforms)
- Conveyor belts
- Walls and other obstacles

### RigidBody2D

This is the node that implements simulated 2D physics. You do not control a [RigidBody2D](../godot_gdscript_nodes_2d.md) directly. Instead, you apply forces to it and the physics engine calculates the resulting movement, including collisions with other bodies, and collision responses, such as bouncing, rotating, etc.

You can modify a rigid body's behavior via properties such as "Mass", "Friction", or "Bounce", which can be set in the Inspector.

The body's behavior is also affected by the world's properties, as set in **Project Settings > Physics**, or by entering an [Area2D](../godot_gdscript_physics.md) that is overriding the global physics properties.

When a rigid body is at rest and hasn't moved for a while, it goes to sleep. A sleeping body acts like a static body, and its forces are not calculated by the physics engine. The body will wake up when forces are applied, either by a collision or via code.

#### Using RigidBody2D

One of the benefits of using a rigid body is that a lot of behavior can be had "for free" without writing any code. For example, if you were making an "Angry Birds"-style game with falling blocks, you would only need to create RigidBody2Ds and adjust their properties. Stacking, falling, and bouncing would automatically be calculated by the physics engine.

However, if you do wish to have some control over the body, you should take care - altering the `position`, `linear_velocity`, or other physics properties of a rigid body can result in unexpected behavior. If you need to alter any of the physics-related properties, you should use the [\_integrate_forces()](../godot_gdscript_misc.md) callback instead of `_physics_process()`. In this callback, you have access to the body's [PhysicsDirectBodyState2D](../godot_gdscript_physics.md), which allows for safely changing properties and synchronizing them with the physics engine.

For example, here is the code for an "Asteroids" style spaceship:

```gdscript
extends RigidBody2D

var thrust = Vector2(0, -250)
var torque = 20000

func _integrate_forces(state):
    if Input.is_action_pressed("ui_up"):
        state.apply_force(thrust.rotated(rotation))
    else:
        state.apply_force(Vector2())
    var rotation_direction = 0
    if Input.is_action_pressed("ui_right"):
        rotation_direction += 1
    if Input.is_action_pressed("ui_left"):
        rotation_direction -= 1
    state.apply_torque(rotation_direction * torque)
```

Note that we are not setting the `linear_velocity` or `angular_velocity` properties directly, but rather applying forces (`thrust` and `torque`) to the body and letting the physics engine calculate the resulting movement.

> **Note:** When a rigid body goes to sleep, the `_integrate_forces()` function will not be called. To override this behavior, you will need to keep the body awake by creating a collision, applying a force to it, or by disabling the [can_sleep](../godot_gdscript_misc.md) property. Be aware that this can have a negative effect on performance.

#### Contact reporting

By default, rigid bodies do not keep track of contacts, because this can require a huge amount of memory if many bodies are in the scene. To enable contact reporting, set the [max_contacts_reported](../godot_gdscript_misc.md) property to a non-zero value. The contacts can then be obtained via [PhysicsDirectBodyState2D.get_contact_count()](../godot_gdscript_physics.md) and related functions.

Contact monitoring via signals can be enabled via the [contact_monitor](../godot_gdscript_misc.md) property. See [RigidBody2D](../godot_gdscript_nodes_2d.md) for the list of available signals.

### CharacterBody2D

[CharacterBody2D](../godot_gdscript_nodes_2d.md) bodies detect collisions with other bodies, but are not affected by physics properties like gravity or friction. Instead, they must be controlled by the user via code. The physics engine will not move a character body.

When moving a character body, you should not set its `position` directly. Instead, you use the `move_and_collide()` or `move_and_slide()` methods. These methods move the body along a given vector, and it will instantly stop if a collision is detected with another body. After the body has collided, any collision response must be coded manually.

#### Character collision response

After a collision, you may want the body to bounce, to slide along a wall, or to alter the properties of the object it hit. The way you handle collision response depends on which method you used to move the CharacterBody2D.

##### move_and_collide

When using `move_and_collide()`, the function returns a [KinematicCollision2D](../godot_gdscript_misc.md) object, which contains information about the collision and the colliding body. You can use this information to determine the response.

For example, if you want to find the point in space where the collision occurred:

```gdscript
extends PhysicsBody2D

var velocity = Vector2(250, 250)

func _physics_process(delta):
    var collision_info = move_and_collide(velocity * delta)
    if collision_info:
        var collision_point = collision_info.get_position()
```

Or to bounce off of the colliding object:

```gdscript
extends PhysicsBody2D

var velocity = Vector2(250, 250)

func _physics_process(delta):
    var collision_info = move_and_collide(velocity * delta)
    if collision_info:
        velocity = velocity.bounce(collision_info.get_normal())
```

##### move_and_slide

Sliding is a common collision response; imagine a player moving along walls in a top-down game or running up and down slopes in a platformer. While it's possible to code this response yourself after using `move_and_collide()`, `move_and_slide()` provides a convenient way to implement sliding movement without writing much code.

> **Warning:** `move_and_slide()` automatically includes the timestep in its calculation, so you should **not** multiply the velocity vector by `delta`. This does **not** apply to `gravity` as it is an acceleration and is time dependent, and needs to be scaled by `delta`.

For example, use the following code to make a character that can walk along the ground (including slopes) and jump when standing on the ground:

```gdscript
extends CharacterBody2D

var run_speed = 350
var jump_speed = -1000
var gravity = 2500

func get_input():
    velocity.x = 0
    var right = Input.is_action_pressed('ui_right')
    var left = Input.is_action_pressed('ui_left')
    var jump = Input.is_action_just_pressed('ui_select')

    if is_on_floor() and jump:
        velocity.y = jump_speed
    if right:
        velocity.x += run_speed
    if left:
        velocity.x -= run_speed

func _physics_process(delta):
    velocity.y += gravity * delta
    get_input()
    move_and_slide()
```

See Kinematic character (2D) for more details on using `move_and_slide()`, including a demo project with detailed code.

---

## Ragdoll system

### Introduction

Godot supports ragdoll physics. Ragdolls rely on physics simulation to create realistic procedural animation. They are used for death animations in many games.

In this tutorial, we will be using the Platformer 3D demo to set up a ragdoll.

> **Note:** You can download the Platformer 3D demo on [GitHub](https://github.com/godotengine/godot-demo-projects/tree/master/3d/platformer) or using the [Asset Library](https://godotengine.org/asset-library/asset/2748). You can also check out an example of a complete ragdoll setup in the [Ragdoll Physics demo](https://github.com/godotengine/godot-demo-projects/tree/master/3d/ragdoll_physics).

### Setting up the ragdoll

#### Creating physical bones

Like many other features in the engine, there are two nodes which are used to set up a ragdoll:

- A [PhysicalBoneSimulator3D](../godot_gdscript_misc.md) node. This node is the parent of all physical bones and is responsible for controlling the simulation.
- One or more [PhysicalBone3D](../godot_gdscript_misc.md) children. Each node represents a single bone in the ragdoll.

Open the platformer demo in Godot, and then the `player/player.tscn` scene. Select the `Skeleton3D` node. A skeleton button appears at the top of the 3D editor viewport:

Click it and select the Create Physical Skeleton option. Godot will generate PhysicalBone3D nodes and collision shapes for each bone in the skeleton and pin joints to connect them together:

Some of the generated bones aren't necessary, such as the `MASTER` bone in this scene. We're going to clean up the skeleton by removing them.

#### Clean up and optimize the skeleton

For each PhysicalBone3D the engine needs to simulate, there is a performance cost. You'll want to remove every bone that is too small to make a difference in the simulation, as well as all utility bones.

For example, if we take a humanoid, you don't need to have physical bones for each finger. You can use a single bone for the entire hand instead, or one for the palm, one for the thumb, and a last one for the other four fingers.

Remove these PhysicalBone3D nodes: `MASTER`, `waist`, `neck`, `headtracker`. This gives us an optimized skeleton and makes it easier to control the ragdoll.

#### Adjust joints and constraints

Once you adjusted the collision shapes, your ragdoll is almost ready. Now, you need to adjust the pin joints to get a better simulation. PhysicalBone3D nodes have an unconstrained pin joint assigned to them by default. To change the pin joint, select a PhysicalBone3D node and change the constraint type in the Joint section of the inspector. There, you can change the constraint's orientation and its limits.

Joints have a gizmo visible in the 3D editor as well, so you can see their constraints in action.

> **Tip:** To get a better view when editing joints and collision shapes, you can do the following: - Hide PhysicalBone3D nodes you aren't currently working on, so you can focus on the ones you're adjusting.

- Hide the MeshInstance3D of the character by clicking the eye icon next to it in the scene tree dock.
- Hide the Skeleton3D gizmos, so that the orange triangles that represent the skeleton don't clutter the viewport while leaving the rest visible. To do so, click View > Gizmos > Skeleton3D at the top of the 3D editor viewport until the eye icon appears closed.
- Disable the preview environment by clicking the globe icon at the top of the 3D editor viewport.
- Set the **Default Clear Color** project setting to pure black in the Project Settings. This is only effective if the preview environment is disabled.
- Change the debug draw mode using the Perspective button in the top-left corner of the 3D editor viewport. The Display Wireframe and Display Overdraw options are particularly useful when adjusting collision shapes, as they allow you to see through the original mesh.
- Use the orthographic camera by clicking the X/Y/Z buttons in the top-right corner of the 3D editor viewport.

Here is the list of joints available:

- **None:** Does not perform any constraint.
- **ConeJoint:** Ball-and-socket. Useful for shoulders, hips, neck.
- **HingeJoint:** Provides an angular constraint; think of it like a door hinge. Useful for elbows and knees.
- **PinJoint:** Keeps two bodies connected _(default)_. Leads to "crumpling" of the bones, so it's recommended to use other joint types for most characters instead.
- **SliderJoint:** Slides one bone along another on a specific axis.
- **6DOFJoint:** Most powerful joint, offering both linear and angular constraints, but also the most complex to configure.

If in doubt, start with HingeJoint and ConeJoint, as they cover most use cases:

- For HingeJoint, make sure to enable **Angular Limit** in the Joint Constraints section of the inspector. After enabling it, you can see the angle that it's being constrained to in the viewport. You can rotate the PhysicalBone3D to change the axis where the joint is constrained, then adjust the angles.
- For ConeJoint, it's usually best to limit **Swing Span** between 20 and 90 degrees, and the **Twist Span** between 20 and 45 degrees.

#### Adjust collision shapes

The next task is adjusting the collision shape and the size of the physical bones to match the part of the body that each bone should simulate.

It's recommended to adjust collision shapes _after_ adjusting joints and constraints, as rotating a joint will also rotate the collision shape. To avoid having to adjust collision shapes twice, it's better to adjust joints first.

Note that it's possible to have multiple collision shapes as a child of a PhysicalBone3D node. This can be useful to represent particularly complex shapes of limbs that are otherwise rigid.

> **Tip:** To pause animation playback while adjusting the ragdoll, select the `AnimationTree` node and disable the **Active** property in the Inspector. Remember to enable it again when you're done, as it controls animation playback during gameplay.

This is the final result:

### Simulate the ragdoll

The ragdoll is now ready to use. To start the simulation and play the ragdoll animation, you need to call the [PhysicalBoneSimulator3D.physical_bones_start_simulation()](../godot_gdscript_misc.md) method. Attach a script to the [PhysicalBoneSimulator3D](../godot_gdscript_misc.md) node that is the parent of all the PhysicalBone3D nodes in our scene, then call it in the script's `_ready` method:

```gdscript
func _ready():
    physical_bones_start_simulation()
```

To stop the simulation, call the [PhysicalBoneSimulator3D.physical_bones_stop_simulation()](../godot_gdscript_misc.md) method.

You can also limit the simulation to only a few bones. This can be useful to create effects such as ragdoll limbs or attachments that can interact with the world. To do so, pass the bone names (_not_ the PhysicalBone3D node names) as a parameter. To see the bone name, look at the **Bone Name** property in the inspector after selecting a PhysicalBone3D node.

> **Tip:** When using an automatically generated physical skeleton as shown in this tutorial, the bone name is also contained in the node name. For example, in `Physical Bone l-arm`, `l-arm` is the bone name.

```gdscript
func _ready():
    physical_bones_start_simulation(["l-arm", "r-arm"])
```

Note that nonexistent bone names will not print any error or warning. If nothing happens when starting the simulation (or if the whole body is ragdolled instead of only specific bones), double-check the list of provided bones.

Here's an example of partial ragdoll simulation:

> **Tip:** To control how strongly the partial ragdoll simulation affects the overall animation, you can adjust the **Influence** property in the [PhysicalBoneSimulator3D](../godot_gdscript_misc.md) node that is the parent of all PhysicalBone3D nodes. By default, it's set to `1.0`, which means the ragdoll simulation fully overrides the rest of the animation.

#### Collision layer and mask

Make sure to set up your collision layers and masks properly so the CharacterBody3D's capsule doesn't get in the way of the physics simulation. Remember to adjust the collision layer and mask in the coin scene as well, so that the player can still collect coins:

You can find the GridMap in the 3D platformer demo in `stage/grid_map.scn`. The coin's Area3D node (on which the layers and masks must be adjusted) can be found at `coin/coin.tscn`.

> **Tip:** To select all PhysicalBone3D nodes quickly, enter `t:PhysicalBone3D` in the search bar at the top of the scene tree dock. This filters the scene tree to only show PhysicalBone3D nodes, which allows you to select them all at once using Shift + Left mouse button on the first and last entries.

If this is not done, collision will behave incorrectly as the player will collide with its own (inactive) ragdoll. This can cause the player to wildly bounce around or get stuck.

Like RigidBody3D, PhysicalBone3D supports collision exceptions through code using the [physical_bones_add_collision_exception()](../godot_gdscript_misc.md) and [physical_bones_remove_collision_exception()](../godot_gdscript_misc.md) methods. This can be used to prevent collisions with a specific object without relying on layers and masks.

> **See also:** For more information, see Collision layers and masks.

---

## Ray-casting

### Introduction

One of the most common tasks in game development is casting a ray (or custom shaped object) and checking what it hits. This enables complex behaviors, AI, etc. to take place. This tutorial will explain how to do this in 2D and 3D.

Godot stores all the low-level game information in servers, while the scene is only a frontend. As such, ray casting is generally a lower-level task. For simple raycasts, nodes like [RayCast3D](../godot_gdscript_nodes_3d.md) and [RayCast2D](../godot_gdscript_nodes_2d.md) will work, as they return every frame what the result of a raycast is.

Many times, though, ray-casting needs to be a more interactive process so a way to do this by code must exist.

### Space

In the physics world, Godot stores all the low-level collision and physics information in a _space_. The current 2d space (for 2D Physics) can be obtained by accessing [CanvasItem.get_world_2d().space](../godot_gdscript_nodes_2d.md). For 3D, it's [Node3D.get_world_3d().space](../godot_gdscript_nodes_3d.md).

The resulting space [RID](../godot_gdscript_math_types.md) can be used in [PhysicsServer3D](../godot_gdscript_physics.md) and [PhysicsServer2D](../godot_gdscript_physics.md) respectively for 3D and 2D.

### Accessing space

Godot physics runs by default in the same thread as game logic, but may be set to run on a separate thread to work more efficiently. Due to this, the only time accessing space is safe is during the [Node.\_physics_process()](../godot_gdscript_misc.md) callback. Accessing it from outside this function may result in an error due to space being _locked_.

To perform queries into physics space, the [PhysicsDirectSpaceState2D](../godot_gdscript_physics.md) and [PhysicsDirectSpaceState3D](../godot_gdscript_physics.md) must be used.

Use the following code in 2D:

```gdscript
func _physics_process(delta):
    var space_rid = get_world_2d().space
    var space_state = PhysicsServer2D.space_get_direct_state(space_rid)
```

Or more directly:

```gdscript
func _physics_process(delta):
    var space_state = get_world_2d().direct_space_state
```

And in 3D:

```gdscript
func _physics_process(delta):
    var space_state = get_world_3d().direct_space_state
```

### Raycast query

For performing a 2D raycast query, the method [PhysicsDirectSpaceState2D.intersect_ray()](../godot_gdscript_physics.md) may be used. For example:

```gdscript
func _physics_process(delta):
    var space_state = get_world_2d().direct_space_state
    # use global coordinates, not local to node
    var query = PhysicsRayQueryParameters2D.create(Vector2(0, 0), Vector2(50, 100))
    var result = space_state.intersect_ray(query)
```

The result is a dictionary. If the ray didn't hit anything, the dictionary will be empty. If it did hit something, it will contain collision information:

```gdscript
if result:
    print("Hit at point: ", result.position)
```

The `result` dictionary when a collision occurs contains the following data:

```gdscript
{
   position: Vector2 # point in world space for collision
   normal: Vector2 # normal in world space for collision
   collider: Object # Object collided or null (if unassociated)
   collider_id: ObjectID # Object it collided against
   rid: RID # RID it collided against
   shape: int # shape index of collider
   metadata: Variant() # metadata of collider
}
```

The data is similar in 3D space, using Vector3 coordinates. Note that to enable collisions with Area3D, the boolean parameter `collide_with_areas` must be set to `true`.

```gdscript
const RAY_LENGTH = 1000

func _physics_process(delta):
    var space_state = get_world_3d().direct_space_state
    var cam = $Camera3D
    var mousepos = get_viewport().get_mouse_position()

    var origin = cam.project_ray_origin(mousepos)
    var end = origin + cam.project_ray_normal(mousepos) * RAY_LENGTH
    var query = PhysicsRayQueryParameters3D.create(origin, end)
    query.collide_with_areas = true

    var result = space_state.intersect_ray(query)
```

### Collision exceptions

A common use case for ray casting is to enable a character to gather data about the world around it. One problem with this is that the same character has a collider, so the ray will only detect its parent's collider, as shown in the following image:

To avoid self-intersection, the `intersect_ray()` parameters object can take an array of exceptions via its `exclude` property. This is an example of how to use it from a CharacterBody2D or any other collision object node:

```gdscript
extends CharacterBody2D

func _physics_process(delta):
    var space_state = get_world_2d().direct_space_state
    var query = PhysicsRayQueryParameters2D.create(global_position, player_position)
    query.exclude = [self]
    var result = space_state.intersect_ray(query)
```

The exceptions array can contain objects or RIDs.

### Collision Mask

While the exceptions method works fine for excluding the parent body, it becomes very inconvenient if you need a large and/or dynamic list of exceptions. In this case, it is much more efficient to use the collision layer/mask system.

The `intersect_ray()` parameters object can also be supplied a collision mask. For example, to use the same mask as the parent body, use the `collision_mask` member variable. The array of exceptions can be supplied as the last argument as well:

```gdscript
extends CharacterBody2D

func _physics_process(delta):
    var space_state = get_world_2d().direct_space_state
    var query = PhysicsRayQueryParameters2D.create(global_position, target_position,
        collision_mask, [self])
    var result = space_state.intersect_ray(query)
```

See Code example for details on how to set the collision mask.

### 3D ray casting from screen

Casting a ray from screen to 3D physics space is useful for object picking. There is not much need to do this because [CollisionObject3D](../godot_gdscript_misc.md) has an "input_event" signal that will let you know when it was clicked, but in case there is any desire to do it manually, here's how.

To cast a ray from the screen, you need a [Camera3D](../godot_gdscript_nodes_3d.md) node. A `Camera3D` can be in two projection modes: perspective and orthogonal. Because of this, both the ray origin and direction must be obtained. This is because `origin` changes in orthogonal mode, while `normal` changes in perspective mode:

To obtain it using a camera, the following code can be used:

```gdscript
const RAY_LENGTH = 1000.0

func _input(event):
    if event is InputEventMouseButton and event.pressed and event.button_index == 1:
        var camera3d = $Camera3D
        var from = camera3d.project_ray_origin(event.position)
        var to = from + camera3d.project_ray_normal(event.position) * RAY_LENGTH
```

Remember that during `_input()`, the space may be locked, so in practice this query should be run in `_physics_process()`.

---

## Using RigidBody

### What is a rigid body?

A rigid body is one that is directly controlled by the physics engine in order to simulate the behavior of physical objects. In order to define the shape of the body, it must have one or more [Shape3D](../godot_gdscript_physics.md) objects assigned. Note that setting the position of these shapes will affect the body's center of mass.

### How to control a rigid body

A rigid body's behavior can be altered by setting its properties, such as mass and weight. A physics material needs to be added to the rigid body to adjust its friction and bounce, and set if it's absorbent and/or rough. These properties can be set in the Inspector or via code. See [RigidBody3D](../godot_gdscript_nodes_3d.md) and [PhysicsMaterial](../godot_gdscript_physics.md) for the full list of properties and their effects.

There are several ways to control a rigid body's movement, depending on your desired application.

If you only need to place a rigid body once, for example to set its initial location, you can use the methods provided by the [Node3D](../godot_gdscript_nodes_3d.md) node, such as `set_global_transform()` or `look_at()`. However, these methods cannot be called every frame or the physics engine will not be able to correctly simulate the body's state. As an example, consider a rigid body that you want to rotate so that it points towards another object. A common mistake when implementing this kind of behavior is to use `look_at()` every frame, which breaks the physics simulation. Below, we'll demonstrate how to implement this correctly.

The fact that you can't use `set_global_transform()` or `look_at()` methods doesn't mean that you can't have full control of a rigid body. Instead, you can control it by using the `_integrate_forces()` callback. In this method, you can add _forces_, apply _impulses_, or set the _velocity_ in order to achieve any movement you desire.

### The "look at" method

As described above, using the Node3D's `look_at()` method can't be used each frame to follow a target. Here is a custom `look_at()` method called `look_follow()` that will work with rigid bodies:

```gdscript
extends RigidBody3D

var speed: float = 0.1

func look_follow(state: PhysicsDirectBodyState3D, current_transform: Transform3D, target_position: Vector3) -> void:
    var forward_local_axis: Vector3 = Vector3(1, 0, 0)
    var forward_dir: Vector3 = (current_transform.basis * forward_local_axis).normalized()
    var target_dir: Vector3 = (target_position - current_transform.origin).normalized()
    var local_speed: float = clampf(speed, 0, acos(forward_dir.dot(target_dir)))
    if forward_dir.dot(target_dir) > 1e-4:
        state.angular_velocity = local_speed * forward_dir.cross(target_dir) / state.step

func _integrate_forces(state):
    var target_position = $my_target_node3d_node.global_transform.origin
    look_follow(state, global_transform, target_position)
```

This method uses the rigid body's `angular_velocity` property to rotate the body. The axis to rotate around is given by the cross product between the current forward direction and the direction one wants to look in. The `clamp` is a simple method used to prevent the amount of rotation from going past the direction which is wanted to be looked in, as the total amount of rotation needed is given by the arccosine of the dot product. This method can be used with `axis_lock_angular_*` as well. If more precise control is needed, solutions such as ones relying on [Quaternion](../godot_gdscript_math_types.md) may be required, as discussed in [Using 3D transforms](tutorials_3d.md).

---

## Using SoftBody3D

Soft bodies (or _soft-body dynamics_) simulate movement, changing shape and other physical properties of deformable objects. For example, this can be used to simulate cloth or to create more realistic characters.

### Physics engine considerations

Support for soft bodies is generally more robust in Jolt Physics compared to GodotPhysics3D. You can switch physics engines by changing **Physics > 3D > Physics Engine** in the Project Settings. Projects created in Godot 4.6 and later use Jolt Physics by default, but existing projects will have to be switched over manually.

Additionally, physics interpolation currently does not affect soft bodies. If you want soft body simulation to look smoother at higher framerates, you'll have to increase the **Physics > Common > Physics Ticks per Second** project setting, which comes at a performance cost.

### Basic setup

A [SoftBody3D](../godot_gdscript_nodes_3d.md) node is used for soft body simulations. Unlike other physics body nodes like [RigidBody3D](../godot_gdscript_nodes_3d.md) or [StaticBody3D](../godot_gdscript_nodes_3d.md), it does **not** have a [CollisionShape3D](../godot_gdscript_physics.md) or a [MeshInstance3D](../godot_gdscript_nodes_3d.md) child node. Instead, the collision shape is derived from the mesh assigned to the node. This mesh is also directly used for rendering, which means you don't need to create any child nodes for a functional, visible setup.

We will create a bouncy cube to demonstrate the setup of a soft body.

Create a new scene with a Node3D node as root. Then, create a SoftBody3D node. Add a BoxMesh in the **Mesh** property of the node in the inspector and increase the subdivision of the mesh for simulation.

The subdivision level determines the precision level of the deformation, with higher values allowing for smaller and more detailed deformations, at the cost of performance. In this example, we'll set it to 3 on each axis:

Now, set the parameters to obtain the type of soft body you aim for. Try to keep the **Simulation Precision** above 5; otherwise, the soft body may collapse.

> **Note:** Handle some parameters with care, as some values can lead to strange results. For example, if the shape is not completely closed and you set pressure to a value greater than `0.0`, the soft body will fly around like a plastic bag under strong wind.

Run the scene to view the simulation. Here's an example of what it should look like:

> **Tip:** To improve the simulation's result, increase the **Simulation Precision**. This can give a significant improvement at the cost of performance. Alternatively, you can increase the **Physics > Common > Physics Ticks per Second** project setting, which will also affect soft body simulation quality.

### Cloak simulation

Let's make a cloak in the Platformer 3D demo.

> **Note:** You can download the Platformer 3D demo on [GitHub](https://github.com/godotengine/godot-demo-projects/tree/master/3d/platformer) or [the Asset Library](https://godotengine.org/asset-library/asset/2748).

Open the `player/player.tscn` scene, add a `SoftBody3D` node below the root node, then assign a PlaneMesh resource to it in its **Mesh** property.

Open the PlaneMesh's properties and set the size to `(0.5, 1.0)`, then set **Subdivide Width** and **Subdivide Depth** to `5`. Adjust the SoftBody3D node's position and rotation so that the plane appears to be close to the character's back. You should end up with something like this:

> **Tip:** Subdivision generates a more tessellated mesh for better simulations. However, higher subdivision levels will impact performance. Try to find a balance between performance and quality. This depends on the number of soft body simulations that you expect to be active at a given time, as well as the distance between the camera and the soft body.

Add a [BoneAttachment3D](../godot_gdscript_nodes_3d.md) node under the skeleton node and select the Neck bone to attach the cloak to the character skeleton.

> **Note:** The BoneAttachment3D node is used to attach objects to a bone of an armature. The attached object will follow the bone's movement. For example, a character's held weapon can be attached this way. Do **not** move the SoftBody3D node under the BoneAttachment3D node as of now. Instead, we'll configure its _pinned points_ to follow the BoneAttachment3D node.

To create pinned points, select the upper vertices in the SoftBody3D node. A pinned point appears blue in the 3D editor viewport:

The pinned joints can be found in SoftBody3D's **Attachments** section, which is under the **Collision** section that must be expanded first. Choose the BoneAttachment3D node as the **Spatial Attachment Path** for each pinned joint. The pinned joints are now attached to the neck.

> **Tip:** To assign the properties faster, you can drag-and-drop the BoneAttachment3D node from the scene tree dock to the **Spatial Attachment Path** property field.

Note that you may have to deselect then reselect the SoftBody3D node for the **Attachments** section to appear.

The last step is to avoid clipping by adding the CharacterBody3D `Player` (the scene's root node) to the **Parent Collision Ignore** property of the SoftBody3D.

Play the scene and the cloak should simulate correctly.

This covers the basic settings of a soft body simulation. Experiment with the parameters to achieve the effect you are aiming for when making your game.

> **Note:** The cloak will not appear when viewed from certain angles due to backface culling. To resolve this, you can disable backface culling by assigning a new StandardMaterial3D, then setting its cull mode to **Disabled**. This will make the material render both sides of the plane.

### Using imported meshes

The **Save to File** option in the Advanced Import Settings dialog allows you to save a mesh to a standalone resource file that you can then attach to SoftBody3D nodes.

You may also want to disable LOD generation or change the LOD generation options when importing a mesh for use with SoftBody3D. The default import settings will produce an LOD that merges adjacent faces that are nearly flat with respect to each other, even at very close render distances. This works well for static meshes, but is often undesirable for use with SoftBody3D if you want these faces to be able to bend and move with respect to each other, instead of being rendered as a single plane.

See [Import configuration](tutorials_assets_pipeline.md) and [Mesh level of detail (LOD)](tutorials_3d.md) for more details.

---
