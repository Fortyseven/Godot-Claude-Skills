# Godot 4 C# Tutorials — Physics (Part 3)

> 4 tutorials. C#-specific code examples.

## Troubleshooting physics issues

When working with a physics engine, you may encounter unexpected results.

While many of these issues can be resolved through configuration, some of them are the result of engine bugs. For known issues related to the physics engine, see [open physics-related issues on GitHub](https://github.com/godotengine/godot/issues?q=is%3Aopen+is%3Aissue+label%3Atopic%3Aphysics). Looking through [closed issues](https://github.com/godotengine/godot/issues?q=+is%3Aclosed+is%3Aissue+label%3Atopic%3Aphysics) can also help answer questions related to physics engine behavior.

### Objects are passing through each other at high speeds

This is known as _tunneling_. Enabling **Continuous CD** in the RigidBody properties can sometimes resolve this issue. If this does not help, there are other solutions you can try:

- Make your static collision shapes thicker. For example, if you have a thin floor that the player can't get below in some way, you can make the collider thicker than the floor's visual representation.
- Modify your fast-moving object's collision shape depending on its movement speed. The faster the object moves, the larger the collision shape should extend outside of the object to ensure it can collide with thin walls more reliably.
- Increase [Physics Ticks per Second](../godot_csharp_misc.md) in the advanced Project Settings. While this has other benefits (such as more stable simulation and reduced input lag), this increases CPU utilization and may not be viable for mobile/web platforms. Multipliers of the default value of `60` (such as `120`, `180` or `240`) should be preferred for a smooth appearance on most displays.

### Stacked objects are unstable and wobbly

Despite seeming like a simple problem, stable RigidBody simulation with stacked objects is difficult to implement in a physics engine. This is caused by integrating forces going against each other. The more stacked objects are present, the stronger the forces will be against each other. This eventually causes the simulation to become wobbly, making the objects unable to rest on top of each other without moving.

Increasing the physics simulation rate can help alleviate this issue. To do so, increase [Physics Ticks per Second](../godot_csharp_misc.md) in the advanced Project Settings. Note that increases CPU utilization and may not be viable for mobile/web platforms. Multipliers of the default value of `60` (such as `120`, `180` or `240`) should be preferred for a smooth appearance on most displays.

In 3D, switching the physics engine from the default GodotPhysics to Jolt can also improve stability. See Using Jolt Physics for more information.

### Scaled physics bodies or collision shapes do not collide correctly

Godot does not currently support scaling of physics bodies or collision shapes. As a workaround, change the collision shape's extents instead of changing its scale. If you want the visual representation's scale to change as well, change the scale of the underlying visual representation (Sprite2D, MeshInstance3D, …) and change the collision shape's extents separately. Make sure the collision shape is not a child of the visual representation in this case.

Since resources are shared by default, you'll have to make the collision shape resource unique if you don't want the change to be applied to all nodes using the same collision shape resource in the scene. This can be done by calling `duplicate()` in a script on the collision shape resource _before_ changing its size.

### Thin objects are wobbly when resting on the floor

This can be due to one of two causes:

- The floor's collision shape is too thin.
- The RigidBody's collision shape is too thin.

In the first case, this can be alleviated by making the floor's collision shape thicker. For example, if you have a thin floor that the player can't get below in some way, you can make the collider thicker than the floor's visual representation.

In the second case, this can usually only be resolved by increasing the physics simulation rate (as making the shape thicker would cause a disconnect between the RigidBody's visual representation and its collision).

In both cases, increasing the physics simulation rate can also help alleviate this issue. To do so, increase [Physics Ticks per Second](../godot_csharp_misc.md) in the advanced Project Settings. Note that this increases CPU utilization and may not be viable for mobile/web platforms. Multipliers of the default value of `60` (such as `120`, `180` or `240`) should be preferred for a smooth appearance on most displays.

### Cylinder collision shapes are unstable

Switching the physics engine from the default GodotPhysics to Jolt should make cylinder collision shapes more reliable. See Using Jolt Physics for more information.

During the transition from Bullet to GodotPhysics in Godot 4, cylinder collision shapes had to be reimplemented from scratch. However, cylinder collision shapes are one of the most difficult shapes to support, which is why many other physics engines don't provide any support for them. There are several known bugs with cylinder collision shapes currently.

If you are sticking to GodotPhysics, we recommend using box or capsule collision shapes for characters for now. Boxes generally provide the best reliability, but have the downside of making the character take more space diagonally. Capsule collision shapes do not have this downside, but their shape can make precision platforming more difficult.

### VehicleBody simulation is unstable, especially at high speeds

When a physics body moves at a high speed, it travels a large distance between each physics step. For instance, when using the 1 unit = 1 meter convention in 3D, a vehicle moving at 360 km/h will travel 100 units per second. With the default physics simulation rate of 60 Hz, the vehicle moves by ~1.67 units each physics tick. This means that small objects may be ignored entirely by the vehicle (due to tunneling), but also that the simulation has little data to work with in general at such a high speed.

Fast-moving vehicles can benefit a lot from an increased physics simulation rate. To do so, increase [Physics Ticks per Second](../godot_csharp_misc.md) in the advanced Project Settings. Note that this increases CPU utilization and may not be viable for mobile/web platforms. Multipliers of the default value of `60` (such as `120`, `180` or `240`) should be preferred for a smooth appearance on most displays.

### Collision results in bumps when an object moves across tiles

This is a known issue in the physics engine caused by the object bumping on a shape's edges, even though that edge is covered by another shape. This can occur in both 2D and 3D.

The best way to work around this issue is to create a "composite" collider. This means that instead of individual tiles having their collision, you create a single collision shape representing the collision for a group of tiles. Typically, you should split composite colliders on a per-island basis (which means each group of touching tiles gets its own collider).

Using a composite collider can also improve physics simulation performance in certain cases. However, since the composite collision shape is much more complex, this may not be a net performance win in all cases.

> **Tip:** In Godot 4.5 and later, creating a composite collider is automatically done when using a TileMapLayer node. The chunk size (`16` tiles on each axis by default) can be set using the **Physics Quadrant Size** property in the TileMapLayer inspector. Larger values provide more reliable collision, at the cost of slower updates when the TileMap is changed.

### Framerate drops when an object touches another object

This is likely due to one of the objects using a collision shape that is too complex. Convex collision shapes should use a number of shapes as low as possible for performance reasons. When relying on Godot's automatic generation, it's possible that you ended up with dozens if not hundreds of shapes created for a single convex shape collision resource.

In some cases, replacing a convex collider with a couple of primitive collision shapes (box, sphere, or capsule) can deliver better performance.

This issue can also occur with StaticBodies that use very detailed trimesh (concave) collisions. In this case, use a simplified representation of the level geometry as a collider. Not only this will improve physics simulation performance significantly, but this can also improve stability by letting you remove small fixtures and crevices from being considered by collision.

In 3D, switching the physics engine from the default GodotPhysics to Jolt can also improve performance. See Using Jolt Physics for more information.

### Framerate suddenly drops to a very low value beyond a certain amount of physics simulation

This occurs because the physics engine can't keep up with the expected simulation rate. In this case, the framerate will start dropping, but the engine is only allowed to simulate a certain number of physics steps per rendered frame. This snowballs into a situation where framerate keeps dropping until it reaches a very low framerate (typically 1-2 FPS) and is called the _physics spiral of death_.

To avoid this, you should check for situations in your project that can cause excessive number of physics simulations to occur at the same time (or with excessively complex collision shapes). If these situations cannot be avoided, you can increase the **Max Physics Steps per Frame** project setting and/or reduce **Physics Ticks per Second** to alleviate this.

### Physics simulation is unreliable when far away from the world origin

This is caused by floating-point precision errors, which become more pronounced as the physics simulation occurs further away from the world origin. This issue also affects rendering, which results in wobbly camera movement when far away from the world origin. See Large world coordinates for more information.

---

## Using Area2D

### Introduction

Godot offers a number of collision objects to provide both collision detection and response. Trying to decide which one to use for your project can be confusing. You can avoid problems and simplify development if you understand how each of them works and what their pros and cons are. In this tutorial, we'll look at the [Area2D](../godot_csharp_physics.md) node and show some examples of how it can be used.

> **Note:** This document assumes you're familiar with Godot's various physics bodies. Please read Physics introduction first.

### What is an area?

An Area2D defines a region of 2D space. In this space you can detect other [CollisionObject2D](../godot_csharp_nodes_2d.md) nodes overlapping, entering, and exiting. Areas also allow for overriding local physics properties. We'll explore each of these functions below.

### Area properties

Areas have many properties you can use to customize their behavior.

The `Gravity`, `Linear Damp`, and `Angular Damp` sections are used to configure the area's physics override behavior. We'll look at how to use those in the _Area influence_ section below.

`Monitoring` and `Monitorable` are used to enable and disable the area.

The `Audio Bus` section allows you to override audio in the area, for example to apply an audio effect when the player moves through.

Note that Area2D extends [CollisionObject2D](../godot_csharp_nodes_2d.md), so it also provides properties inherited from that class. The `Collision` section of `CollisionObject2D` is where you configure the area's collision layer(s) and mask(s).

### Overlap detection

Perhaps the most common use of Area2D nodes is for contact and overlap detection. When you need to know that two objects have touched, but don't need physical collision, you can use an area to notify you of the contact.

For example, let's say we're making a coin for the player to pick up. The coin is not a solid object - the player can't stand on it or push it - we just want it to disappear when the player touches it.

Here's the node setup for the coin:

To detect the overlap, we'll connect the appropriate signal on the Area2D. Which signal to use depends on the player's node type. If the player is another area, use `area_entered`. However, let's assume our player is a `CharacterBody2D` (and therefore a `CollisionObject2D` type), so we'll connect the `body_entered` signal.

> **Note:** If you're not familiar with using signals, see Using signals (see Getting Started docs) for an introduction.

```csharp
using Godot;

public partial class Coin : Area2D
{
    private void OnCoinBodyEntered(PhysicsBody2D body)
    {
        QueueFree();
    }
}
```

Now our player can collect the coins!

Some other usage examples:

- Areas are great for bullets and other projectiles that hit and deal damage, but don't need any other physics such as bouncing.
- Use a large circular area around an enemy to define its "detect" radius. When the player is outside the area, the enemy can't "see" it.
- "Security cameras" - In a large level with multiple cameras, attach areas to each camera and activate them when the player enters.

See the Your first 2D game (see Getting Started docs) for an example of using Area2D in a game.

### Area influence

The second major use for area nodes is to alter physics. By default, the area won't do this, but you can enable this with the `Space Override` property. When areas overlap, they are processed in `Priority` order (higher priority areas are processed first). There are four options for override:

- _Combine_ - The area adds its values to what has been calculated so far.
- _Replace_ - The area replaces physics properties, and lower priority areas are ignored.
- _Combine-Replace_ - The area adds its gravity/damping values to whatever has been calculated so far (in priority order), ignoring any lower priority areas.
- _Replace-Combine_ - The area replaces any gravity/damping calculated so far, but keeps calculating the rest of the areas.

Using these properties, you can create very complex behavior with multiple overlapping areas.

The physics properties that can be overridden are:

- _Gravity_ - Gravity's strength inside the area.
- _Gravity Direction_ - This vector does not need to be normalized.
- _Linear Damp_ - How quickly objects stop moving - linear velocity lost per second.
- _Angular Damp_ - How quickly objects stop spinning - angular velocity lost per second.

#### Point gravity

The `Gravity Point` property allows you to create an "attractor". Gravity in the area will be calculated towards a point, given by the `Point Center` property. Values are relative to the Area2D, so for example using `(0, 0)` will attract objects to the center of the area.

#### Examples

The example project attached below has three areas demonstrating physics override.

You can download this project here: [area_2d_starter.zip](https://github.com/godotengine/godot-docs-project-starters/releases/download/latest-4.x/area_2d_starter.zip)

---

## Using CharacterBody2D/3D

### Introduction

Godot offers several collision objects to provide both collision detection and response. Trying to decide which one to use for your project can be confusing. You can avoid problems and simplify development if you understand how each of them works and what their pros and cons are. In this tutorial, we'll look at the [CharacterBody2D](../godot_csharp_nodes_2d.md) node and show some examples of how to use it.

> **Note:** While this document uses `CharacterBody2D` in its examples, the same concepts apply in 3D as well.

### What is a character body?

`CharacterBody2D` is for implementing bodies that are controlled via code. Character bodies detect collisions with other bodies when moving, but are not affected by engine physics properties, like gravity or friction. While this means that you have to write some code to create their behavior, it also means you have more precise control over how they move and react.

> **Note:** This document assumes you're familiar with Godot's various physics bodies. Please read Physics introduction first, for an overview of the physics options.

> **Tip:** A CharacterBody2D can be affected by gravity and other forces, but you must calculate the movement in code. The physics engine will not move a CharacterBody2D.

### Movement and collision

When moving a `CharacterBody2D`, you should not set its `position` property directly. Instead, you use the `move_and_collide()` or `move_and_slide()` methods. These methods move the body along a given vector and detect collisions.

> **Warning:** You should handle physics body movement in the `_physics_process()` callback.

The two movement methods serve different purposes, and later in this tutorial, you'll see examples of how they work.

#### move_and_collide

This method takes one required parameter: a [Vector2](../godot_csharp_math_types.md) indicating the body's relative movement. Typically, this is your velocity vector multiplied by the frame timestep (`delta`). If the engine detects a collision anywhere along this vector, the body will immediately stop moving. If this happens, the method will return a [KinematicCollision2D](../godot_csharp_misc.md) object.

`KinematicCollision2D` is an object containing data about the collision and the colliding object. Using this data, you can calculate your collision response.

`move_and_collide` is most useful when you just want to move the body and detect collision, but don't need any automatic collision response. For example, if you need a bullet that ricochets off a wall, you can directly change the angle of the velocity when you detect a collision. See below for an example.

#### move_and_slide

The `move_and_slide()` method is intended to simplify the collision response in the common case where you want one body to slide along the other. It is especially useful in platformers or top-down games, for example.

When calling `move_and_slide()`, the function uses a number of node properties to calculate its slide behavior. These properties can be found in the Inspector, or set in code.

- `velocity` - _default value:_ `Vector2( 0, 0 )`

This property represents the body's velocity vector in pixels per second. `move_and_slide()` will modify this value automatically when colliding.

- `motion_mode` - _default value:_ `MOTION_MODE_GROUNDED`

This property is typically used to distinguish between side-scrolling and top-down movement. When using the default value, you can use the `is_on_floor()`, `is_on_wall()`, and `is_on_ceiling()` methods to detect what type of surface the body is in contact with, and the body will interact with slopes. When using `MOTION_MODE_FLOATING`, all collisions will be considered "walls".

- `up_direction` - _default value:_ `Vector2( 0, -1 )`

This property allows you to define what surfaces the engine should consider being the floor. Its value lets you use the `is_on_floor()`, `is_on_wall()`, and `is_on_ceiling()` methods to detect what type of surface the body is in contact with. The default value means that the top side of horizontal surfaces will be considered "ground".

- `floor_stop_on_slope` - _default value:_ `true`

This parameter prevents a body from sliding down slopes when standing still.

- `wall_min_slide_angle` - _default value:_ `0.261799` (in radians, equivalent to `15` degrees)

This is the minimum angle where the body is allowed to slide when it hits a slope.

- `floor_max_angle` - _default value:_ `0.785398` (in radians, equivalent to `45` degrees)

This parameter is the maximum angle before a surface is no longer considered a "floor."

There are many other properties that can be used to modify the body's behavior under specific circumstances. See the [CharacterBody2D](../godot_csharp_nodes_2d.md) docs for full details.

### Detecting collisions

When using `move_and_collide()` the function returns a `KinematicCollision2D` directly, and you can use this in your code.

When using `move_and_slide()` it's possible to have multiple collisions occur, as the slide response is calculated. To process these collisions, use `get_slide_collision_count()` and `get_slide_collision()`:

```csharp
// Using MoveAndCollide.
var collision = MoveAndCollide(Velocity * (float)delta);
if (collision != null)
{
    GD.Print("I collided with ", ((Node)collision.GetCollider()).Name);
}

// Using MoveAndSlide.
MoveAndSlide();
for (int i = 0; i < GetSlideCollisionCount(); i++)
{
    var collision = GetSlideCollision(i);
    GD.Print("I collided with ", ((Node)collision.GetCollider()).Name);
}
```

> **Note:** get_slide_collision_count() only counts times the body has collided and changed direction.

See [KinematicCollision2D](../godot_csharp_misc.md) for details on what collision data is returned.

### Which movement method to use?

A common question from new Godot users is: "How do you decide which movement function to use?" Often, the response is to use `move_and_slide()` because it seems simpler, but this is not necessarily the case. One way to think of it is that `move_and_slide()` is a special case, and `move_and_collide()` is more general. For example, the following two code snippets result in the same collision response:

```csharp
// using MoveAndCollide
var collision = MoveAndCollide(Velocity * (float)delta);
if (collision != null)
{
    Velocity = Velocity.Slide(collision.GetNormal());
}

// using MoveAndSlide
MoveAndSlide();
```

Anything you do with `move_and_slide()` can also be done with `move_and_collide()`, but it might take a little more code. However, as we'll see in the examples below, there are cases where `move_and_slide()` doesn't provide the response you want.

In the example above, `move_and_slide()` automatically alters the `velocity` variable. This is because when the character collides with the environment, the function recalculates the speed internally to reflect the slowdown.

For example, if your character fell on the floor, you don't want it to accumulate vertical speed due to the effect of gravity. Instead, you want its vertical speed to reset to zero.

`move_and_slide()` may also recalculate the kinematic body's velocity several times in a loop as, to produce a smooth motion, it moves the character and collides up to five times by default. At the end of the process, the character's new velocity is available for use on the next frame.

### Examples

To see these examples in action, download the sample project: [character_body_2d_starter.zip](https://github.com/godotengine/godot-docs-project-starters/releases/download/latest-4.x/character_body_2d_starter.zip)

#### Movement and walls

If you've downloaded the sample project, this example is in "basic_movement.tscn".

For this example, add a `CharacterBody2D` with two children: a `Sprite2D` and a `CollisionShape2D`. Use the Godot "icon.svg" as the Sprite2D's texture (drag it from the Filesystem dock to the _Texture_ property of the `Sprite2D`). In the `CollisionShape2D`'s _Shape_ property, select "New RectangleShape2D" and size the rectangle to fit over the sprite image.

> **Note:** See [2D movement overview](tutorials_2d.md) for examples of implementing 2D movement schemes.

Attach a script to the CharacterBody2D and add the following code:

```csharp
using Godot;

public partial class MyCharacterBody2D : CharacterBody2D
{
    private int _speed = 300;

    public void GetInput()
    {
        Vector2 inputDir = Input.GetVector("ui_left", "ui_right", "ui_up", "ui_down");
        Velocity = inputDir * _speed;
    }

    public override void _PhysicsProcess(double delta)
    {
        GetInput();
        MoveAndCollide(Velocity * (float)delta);
    }
}
```

Run this scene and you'll see that `move_and_collide()` works as expected, moving the body along the velocity vector. Now let's see what happens when you add some obstacles. Add a [StaticBody2D](../godot_csharp_nodes_2d.md) with a rectangular collision shape. For visibility, you can use a Sprite2D, a Polygon2D, or turn on "Visible Collision Shapes" from the "Debug" menu.

Run the scene again and try moving into the obstacle. You'll see that the `CharacterBody2D` can't penetrate the obstacle. However, try moving into the obstacle at an angle and you'll find that the obstacle acts like glue - it feels like the body gets stuck.

This happens because there is no _collision response_. `move_and_collide()` stops the body's movement when a collision occurs. We need to code whatever response we want from the collision.

Try changing the function to `move_and_slide()` and running again.

`move_and_slide()` provides a default collision response of sliding the body along the collision object. This is useful for a great many game types, and may be all you need to get the behavior you want.

#### Bouncing/reflecting

What if you don't want a sliding collision response? For this example ("bounce_and_collide.tscn" in the sample project), we have a character shooting bullets and we want the bullets to bounce off the walls.

This example uses three scenes. The main scene contains the Player and Walls. The Bullet and Wall are separate scenes so that they can be instanced.

The Player is controlled by the `w` and `s` keys for forward and back. Aiming uses the mouse pointer. Here is the code for the Player, using `move_and_slide()`:

```csharp
using Godot;

public partial class MyCharacterBody2D : CharacterBody2D
{
    private PackedScene _bullet = GD.Load<PackedScene>("res://Bullet.tscn");
    private int _speed = 200;

    public void GetInput()
    {
        // Add these actions in Project Settings -> Input Map.
        float inputDir = Input.GetAxis("backward", "forward");
        Velocity = Transform.X * inputDir * _speed;
        if (Input.IsActionPressed("shoot"))
        {
            Shoot();
        }
    }

    public void Shoot()
    {
        // "Muzzle" is a Marker2D placed at the barrel of the gun.
        var b = (Bullet)_bullet.Instantiate();
        b.Start(GetNode<Node2D>("Muzzle").GlobalPosition, Rotation);
        GetTree().Root.AddChild(b);
    }

    public override void _PhysicsProcess(double delta)
    {
// ...
```

And the code for the Bullet:

```csharp
using Godot;

public partial class Bullet : CharacterBody2D
{
    public int _speed = 750;

    public void Start(Vector2 position, float direction)
    {
        Rotation = direction;
        Position = position;
        Velocity = new Vector2(speed, 0).Rotated(Rotation);
    }

    public override void _PhysicsProcess(double delta)
    {
        var collision = MoveAndCollide(Velocity * (float)delta);
        if (collision != null)
        {
            Velocity = Velocity.Bounce(collision.GetNormal());
            if (collision.GetCollider().HasMethod("Hit"))
            {
                collision.GetCollider().Call("Hit");
            }
        }
    }

    private void OnVisibilityNotifier2DScreenExited()
    {
        // Deletes the bullet when it exits the screen.
        QueueFree
// ...
```

The action happens in `_physics_process()`. After using `move_and_collide()`, if a collision occurs, a `KinematicCollision2D` object is returned (otherwise, the return is `null`).

If there is a returned collision, we use the `normal` of the collision to reflect the bullet's `velocity` with the `Vector2.bounce()` method.

If the colliding object (`collider`) has a `hit` method, we also call it. In the example project, we've added a flashing color effect to the Wall to demonstrate this.

#### Platformer movement

Let's try one more popular example: the 2D platformer. `move_and_slide()` is ideal for quickly getting a functional character controller up and running. If you've downloaded the sample project, you can find this in "platformer.tscn".

For this example, we'll assume you have a level made of one or more `StaticBody2D` objects. They can be any shape and size. In the sample project, we're using [Polygon2D](../godot_csharp_nodes_2d.md) to create the platform shapes.

Here's the code for the player body:

```csharp
using Godot;

public partial class MyCharacterBody2D : CharacterBody2D
{
    private float _speed = 100.0f;
    private float _jumpSpeed = -400.0f;

    // Get the gravity from the project settings so you can sync with rigid body nodes.
    public float Gravity = ProjectSettings.GetSetting("physics/2d/default_gravity").AsSingle();

    public override void _PhysicsProcess(double delta)
    {
        Vector2 velocity = Velocity;

        // Add the gravity.
        velocity.Y += Gravity * (float)delta;

        // Handle jump.
        if (Input.IsActionJustPressed("jump") && IsOnFloor())
        {
            velocity.Y = _jumpSpeed;
        }

        // Get the input direction.
        float direction = Input.GetAxis("ui_left", "ui_right");
        velocity.X = direction * _speed;


// ...
```

In this code we're using `move_and_slide()` as described above - to move the body along its velocity vector, sliding along any collision surfaces such as the ground or a platform. We're also using `is_on_floor()` to check if a jump should be allowed. Without this, you'd be able to "jump" in midair; great if you're making Flappy Bird, but not for a platformer game.

There is a lot more that goes into a complete platformer character: acceleration, double-jumps, coyote-time, and many more. The code above is just a starting point. You can use it as a base to expand into whatever movement behavior you need for your own projects.

---

## Using Jolt Physics

### Introduction

The Jolt physics engine was added as an alternative to the existing Godot Physics physics engine in 4.4. Jolt is developed by Jorrit Rouwe with a focus on games and VR applications. Previously it was available as an extension but is now built into Godot. By default, new projects will use it as the physics engine.

The existing extension is now considered in maintenance mode. That means bug fixes will be merged, and it will be kept compatible with new versions of Godot until the built-in module has feature parity with the extension. The only thing missing at this point is related joints, which you can read about on this page. The extension can be found [here on GitHub](https://github.com/godot-jolt/godot-jolt) and in Godot's asset library.

To change the 3D physics engine to be Jolt Physics, set [Project Settings > Physics > 3D > Physics Engine](../godot_csharp_misc.md) to `Jolt Physics`. Once you've done that, click the **Save & Restart** button. When the editor opens again, 3D scenes should now be using Jolt for physics.

### Notable differences to Godot Physics

There are many differences between the existing Godot Physics engine and Jolt.

#### Joint properties

The current interfaces for the 3D joint nodes don't quite line up with the interface of Jolt's own joints. As such, there are a number of joint properties that are not supported, mainly ones related to configuring the joint's soft limits.

The unsupported properties are:

- PinJoint3D: `bias`, `damping`, `impulse_clamp`
- HingeJoint3D: `bias`, `softness`, `relaxation`
- SliderJoint3D: `angular_\*`, `\*_limit/softness`, `\*_limit/restitution`, `\*_limit/damping`
- ConeTwistJoint3D: `bias`, `relaxation`, `softness`
- Generic6DOFJoint3D: `*_limit_*/softness`, `*_limit_*/restitution`, `*_limit_*/damping`, `*_limit_*/erp`

Currently a warning is emitted if you set these properties to anything but their default values.

#### Single-body joints

You can, in Godot, omit one of the joint bodies for a two-body joint and effectively have "the world" be the other body. However, the node path that you assign your body to ([node_a](../godot_csharp_misc.md) vs [node_b](../godot_csharp_misc.md)) is ignored. Godot Physics will always behave as if you assigned it to `node_a`, and since `node_a` is also what defines the frame of reference for the joint limits, you end up with inverted limits and a potentially strange limit shape, especially if your limits allow both linear and angular degrees of freedom.

Jolt will behave as if you assigned the body to `node_b` instead, with `node_a` representing "the world". There is a project setting called [Physics > Jolt Physics 3D > Joints > World Node](../godot_csharp_misc.md) that lets you toggle this behavior, if you need compatibility for an existing project.

#### Collision margins

Jolt (and other similar physics engines) uses something that Jolt refers to as "convex radius" to help improve the performance and behavior of the types of collision detection that Jolt relies on for convex shapes. Other physics engines (Godot included) might refer to these as "collision margins" instead. Godot exposes these as the `margin` property on every Shape3D-derived class, but Godot Physics itself does not use them for anything.

What these collision margins sometimes do in other engines (as described in Godot's documentation) is effectively add a "shell" around the shape, slightly increasing its size while also rounding off any edges/corners. In Jolt however, these margins are first used to shrink the shape, and then the "shell" is applied, resulting in edges/corners being similarly rounded off, but without increasing the size of the shape.

To prevent having to tweak this margin property manually, since its default value can be problematic for smaller shapes, the Jolt module exposes a project setting called [Physics > Jolt Physics 3D > Collisions > Collision Margin Fraction](../godot_csharp_misc.md) which is multiplied with the smallest axis of the shape's AABB to calculate the actual margin. The margin property of the shape is then instead used as an upper bound.

These margins should, for most use-cases, be more or less transparent, but can sometimes result in odd collision normals when performing shape queries. You can lower the above mentioned project setting to mitigate some of this, including setting it to `0.0`, but too small of a margin can also cause odd collision results, so is generally not recommended.

#### Baumgarte stabilization

Baumgarte stabilization is a method to resolve penetrating bodies and push them to a state where they are just touching. In Godot Physics this works like a spring. This means that bodies can accelerate and may cause the bodies to overshoot and separate completely. With Jolt, the stabilization is only applied to the position and not to the velocity of the body. This means it cannot overshoot but it may take longer to resolve the penetration.

The strength of this stabilization can be tweaked using the project setting [Physics > Jolt Physics 3D > Simulation > Baumgarte Stabilization Factor](../godot_csharp_misc.md). Setting this project setting to `0.0` will turn Baumgarte stabilization off. Setting it to `1.0` will resolve penetration in 1 simulation step. This is fast but often also unstable.

#### Ghost collisions

Jolt employs two techniques to mitigate ghost collisions, meaning collisions with internal edges of shapes/bodies that result in collision normals that oppose the direction of movement.

The first technique, called "active edge detection", marks edges of triangles in [ConcavePolygonShape3D](../godot_csharp_misc.md) or [HeightMapShape3D](../godot_csharp_misc.md) as either "active" or "inactive", based on the angle to the neighboring triangle. When a collision happens with an inactive edge the collision normal will be replaced with the triangle's normal instead, to lessen the effect of ghost collisions.

The angle threshold for this active edge detection is configurable through the project setting [Physics >Jolt Physics 3D > Collisions > Active Edge Threshold](../godot_csharp_misc.md).

The second technique, called "enhanced internal edge removal", instead adds runtime checks to detect whether an edge is active or inactive, based on the contact points of the two bodies. This has the benefit of applying not only to collisions with [ConcavePolygonShape3D](../godot_csharp_misc.md) and [HeightMapShape3D](../godot_csharp_misc.md), but also edges between any shapes within the same body.

Enhanced internal edge removal can be toggled on and off for the various contexts to which it's applied, using the [Physics >Jolt Physics 3D > Simulation > Use Enhanced Internal Edge Removal](../godot_csharp_misc.md), project setting, and the similar settings for [queries](../godot_csharp_misc.md) and [motion queries](../godot_csharp_misc.md).

Note that neither the active edge detection nor enhanced internal edge removal apply when dealing with ghost collisions between two different bodies.

#### Memory usage

Jolt uses a stack allocator for temporary allocations within its simulation step. This stack allocator requires allocating a set amount of memory up front, which can be configured using the [Physics > Jolt Physics 3D > Limits > Temporary Memory Buffer Size](../godot_csharp_misc.md) project setting.

#### Ray-cast face index

The `face_index` property returned in the results of [intersect_ray()](../godot_csharp_misc.md) and RayCast3D will by default always be `-1` with Jolt. The project setting [Physics > Jolt Physics 3D > Queries > Enable Ray Cast Face Index](../godot_csharp_misc.md) will enable them.

Note that enabling this setting will increase the memory requirement of [ConcavePolygonShape3D](../godot_csharp_misc.md) with about 25%.

#### Kinematic RigidBody3D contacts

When using Jolt, a [RigidBody3D](../godot_csharp_nodes_3d.md) frozen with [FREEZE_MODE_KINEMATIC](../godot_csharp_misc.md) will by default not report contacts from collisions with other static/kinematic bodies, for performance reasons, even when setting a non-zero [max_contacts_reported](../godot_csharp_misc.md). If you have many/large kinematic bodies overlapping with complex static geometry, such as [ConcavePolygonShape3D](../godot_csharp_misc.md) or [HeightMapShape3D](../godot_csharp_misc.md), you can end up wasting a significant amount of CPU performance and memory without realizing it.

For this reason this behavior is opt-in through the project setting [Physics > Jolt Physics 3D > Simulation > Generate All Kinematic Contacts](../godot_csharp_misc.md).

#### Contact impulses

Due to limitations internal to Jolt, the contact impulses provided by [PhysicsDirectBodyState3D.get_contact_impulse()](../godot_csharp_physics.md) are estimated ahead of time based on things like the contact manifold and velocities of the colliding bodies. This means that the reported impulses will only be accurate in cases where the two bodies in question are not colliding with any other bodies.

#### Area3D and SoftBody3D

Jolt does not currently support any interactions between [SoftBody3D](../godot_csharp_nodes_3d.md) and [Area3D](../godot_csharp_physics.md), such as the wind and gravity properties found on [Area3D](../godot_csharp_physics.md).

#### WorldBoundaryShape3D

[WorldBoundaryShape3D](../godot_csharp_misc.md), which is meant to represent an infinite plane, is implemented a bit differently in Jolt compared to Godot Physics. Both engines have an upper limit for how big the effective size of this plane can be, but this size is much smaller when using Jolt, in order to avoid precision issues.

You can configure this size using the [Physics > Jolt Physics 3D > Limits > World Boundary Shape Size](../godot_csharp_misc.md) project setting.

### Notable differences to the Godot Jolt extension

While the built-in Jolt module is largely a straight port of the Godot Jolt extension, there are a few things that are different.

#### Project settings

All project settings have been moved from the `physics/jolt_3d` category to `physics/jolt_physics_3d`.

On top of that, there's been some renaming and refactoring of the individual project settings as well. These include:

- `sleep/enabled` is now `simulation/allow_sleep.`
- `sleep/velocity_threshold` is now `simulation/sleep_velocity_threshold.`
- `sleep/time_threshold` is now `simulation/sleep_time_threshold.`
- `collisions/use_shape_margins` is now `collisions/collision_margin_fraction`, where a value of 0 is equivalent to disabling it.
- `collisions/use_enhanced_internal_edge_removal` is now `simulation/use_enhanced_internal_edge_removal.`
- `collisions/areas_detect_static_bodies` is now `simulation/areas_detect_static_bodies.`
- `collisions/report_all_kinematic_contacts` is now `simulation/generate_all_kinematic_contacts.`
- `collisions/soft_body_point_margin` is now `simulation/soft_body_point_radius.`
- `collisions/body_pair_cache_enabled is now simulation/body_pair_contact_cache_enabled.`
- `collisions/body_pair_cache_distance_threshold` is `now simulation/body_pair_contact_cache_distance_threshold.`
- `collisions/body_pair_cache_angle_threshold is now simulation/body_pair_contact_cache_angle_threshold.`
- `continuous_cd/movement_threshold` is now `simulation/continuous_cd_movement_threshold`, but expressed as a fraction instead of a percentage.
- `continuous_cd/max_penetration` is now `simulation/continuous_cd_max_penetration`, but expressed as a fraction instead of a percentage.
- `kinematics/use_enhanced_internal_edge_removal` is now `motion_queries/use_enhanced_internal_edge_removal.`
- `kinematics/recovery_iterations` is now `motion_queries/recovery_iterations`, but expressed as a fraction instead of a percentage.
- `kinematics/recovery_amount` is now `motion_queries/recovery_amount.`
- `queries/use_legacy_ray_casting` has been removed.
- `solver/position_iterations` is now `simulation/position_steps.`
- `solver/velocity_iterations` is now `simulation/velocity_steps.`
- `solver/position_correction` is now `simulation/baumgarte_stabilization_factor`, but expressed as a fraction instead of a percentage.
- `solver/active_edge_threshold` is now `collisions/active_edge_threshold.`
- `solver/bounce_velocity_threshold` is now `simulation/bounce_velocity_threshold.`
- `solver/contact_speculative_distance` is now `simulation/speculative_contact_distance.`
- `solver/contact_allowed_penetration` is now `simulation/penetration_slop.`
- `limits/max_angular_velocity` is now stored as radians instead.
- `limits/max_temporary_memory` is now `limits/temporary_memory_buffer_size.`

#### Joint nodes

The joint nodes that are exposed in the Godot Jolt extension (JoltPinJoint3D, JoltHingeJoint3D, JoltSliderJoint3D, JoltConeTwistJoint3D, and JoltGeneric6DOFJoint) have not been included in the Jolt module.

#### Thread safety

Unlike the Godot Jolt extension, the Jolt module does have thread-safety, including support for the [Physics > 3D > Run On Separate Thread](../godot_csharp_misc.md) project setting. However this has not been tested very thoroughly, so it should be considered experimental.

---
