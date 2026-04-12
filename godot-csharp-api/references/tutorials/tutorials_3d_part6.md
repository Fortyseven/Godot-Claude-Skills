# Godot 4 C# Tutorials — 3D (Part 6)

> 8 tutorials. C#-specific code examples.

## 3D Particle collisions

Since GPU particles are processed entirely on the GPU, they don't have access to the game's physical world. If you need particles to collide with the environment, you have to set up particle collision nodes. There are four of them: [GPUParticlesCollisionBox3D](../godot_csharp_misc.md), [GPUParticlesCollisionSphere3D](../godot_csharp_misc.md), [GPUParticlesCollisionSDF3D](../godot_csharp_misc.md), and [GPUParticlesCollisionHeightField3D](../godot_csharp_misc.md).

### Common properties

There are some properties that you can find on all collision nodes. They're located in the `GPUParticlesCollision3D` section in the inspector.

The `Cull Mask` property controls which particle systems are affected by a collision node based on each system's [visibility layers](../godot_csharp_misc.md). A particle system collides with a collision node only if at least one of the system's visibility layers is enabled in the collider's cull mask.

### Box collision

Box collision nodes are shaped like a solid, rectangular box. You control their size with the `Extents` property. Box extents always measure half of the sides of its bounds, so a value of `(X=1.0,Y=1.0,Z=1.0)` creates a box that is 2 meters wide on each side. Box collision nodes are useful for simulating floor and wall geometry that particles should collide against.

To create a box collision node, add a new child node to your scene and select `GPUParticlesCollisionBox3D` from the list of available nodes. You can animate the box position or attach it to a moving node for more dynamic effects.

### Sphere collision

Sphere collision nodes are shaped like a solid sphere. The `Radius` property controls the size of the sphere. While box collision nodes don't have to be perfect cubes, sphere collision nodes will always be spheres. If you want to set width independently from height, you have to change the `Scale` property in the `Node3D` section.

To create a sphere collision node, add a new child node to your scene and select `GPUParticlesCollisionSphere3D` from the list of available nodes. You can animate the sphere's position or attach it to a moving node for more dynamic effects.

### Height field collision

Height field particle collision is very useful for large outdoor areas that need to collide with particles. At runtime, the node creates a height field from all the meshes within its bounds that match its cull mask. Particles collide against the mesh that this height field represents. Since the height field generation is done dynamically, it can follow the player camera around and react to changes in the level. Different settings for the height field density offer a wide range of performance adjustments.

To create a height field collision node, add a new child node to your scene and select `GPUParticlesCollisionHeightField3D` from the list of available nodes.

A height field collision node is shaped like a box. The `Extents` property controls its size. Extents always measure half of the sides of its bounds, so a value of `(X=1.0,Y=1.0,Z=1.0)` creates a box that is 2 meters wide on each side. Anything outside of the node's extents is ignored for height field creation.

The `Resolution` property controls how detailed the height field is. A lower resolution performs faster at the cost of accuracy. If the height field resolution is too low, it may look like particles penetrate level geometry or get stuck in the air during collision events. They might also ignore some smaller meshes completely.

The `Update Mode` property controls when the height field is recreated from the meshes within its bounds. Set it to `When Moved` to make it refresh only when it moves. This performs well and is suited for static scenes that don't change very often. If you need particles to collide with dynamic objects that change position frequently, you can select `Always` to refresh every frame. This comes with a cost to performance and should only be used when necessary.

> **Note:** It's important to remember that when `Update Mode` is set to `When Moved`, it is the _height field node_ whose movement triggers an update. The height field is not updated when one of the meshes inside it moves.

The `Follow Camera Enabled` property makes the height field follow the current camera when enabled. It will update whenever the camera moves. This property can be used to make sure that there is always particle collision around the player while not wasting performance on regions that are out of sight or too far away.

### SDF collision

> **Note:** Particle SDF collision is only supported in the Forward+ and Mobile renderers, not Compatibility.

SDF collision nodes create a [signed distance field](https://www.reddit.com/r/explainlikeimfive/comments/k2zbos/eli5_what_are_distance_fields_in_graphics) that particles can collide with. SDF collision is similar to height field collision in that it turns multiple meshes within its bounds into a single collision volume for particles. A major difference is that signed distance fields can represent holes, tunnels and overhangs, which is impossible to do with height fields alone. The performance overhead is larger compared to height fields, so they're best suited for small-to-medium-sized environments.

To create an SDF collision node, add a new child node to your scene and select `GPUParticlesCollisionSDF3D` from the list of available nodes. SDF collision nodes have to be baked in order to have any effect on particles in the level. To do that, click the Bake SDF button in the viewport toolbar while the SDF collision node is selected and choose a directory to store the baked data. Since SDF collision needs to be baked in the editor, it's static and cannot change at runtime.

An SDF collision node is shaped like a box. The `Extents` property controls its size. Extents always measure half of the sides of its bounds, so a value of `(X=1.0,Y=1.0,Z=1.0)` creates a box that is 2 meters wide on each side. Anything outside of the node's extents is ignored for collision.

The `Resolution` property controls how detailed the distance field is. A lower resolution performs faster at the cost of accuracy. If the resolution is too low, it may look like particles penetrate level geometry or get stuck in the air during collision events. They might also ignore some smaller meshes completely.

The `Thickness` property gives the distance field, which is usually hollow on the inside, a thickness to prevent particles from penetrating at high speeds. If you find that some particles don't collide with the level geometry and instead shoot right through it, try setting this property to a higher value.

The `Bake Mask` property controls which meshes will be considered when the SDF is baked. Only meshes that render on the active layers in the bake mask contribute to particle collision.

### Troubleshooting

For particle collision to work, the particle's visibility AABB must overlap with the collider's AABB. If collisions appear to be not working despite colliders being set up, generate an updated visibility AABB by selecting the GPUParticles3D node and choosing **GPUParticles3D > Generate Visibility AABB…** at the top of the 3D editor viewport.

If the particles move fast and colliders are thin. There are two solutions for this:

- Make the colliders thicker. For instance, if particles cannot get below a solid floor, you could make the collider representing the floor thicker than its actual visual representation. The heightfield collider automatically handles this by design, as heightfields cannot represent "room over room" collision.
- Increased `Fixed FPS` in the GPUParticles3D node, which will perform collision checks more often. This comes at a performance cost, so avoid setting this too high.

---

## Complex emission shapes

When it is not enough to emit particles from one of the simple shapes available in the process material, Godot provides a way to emit particles from arbitrary, complex shapes. The shapes are generated from meshes in the scene and stored as textures in the particle process material. This is a very versatile workflow that has allowed users to use particle systems for things that go beyond traditional use cases, like foliage, leaves on a tree, or complex holographic effects.

> **Note:** When you create emission points from meshes, you can only select a single node as emission source. If you want particles to emit from multiple shapes, you either have to create several particle systems or combine the meshes into one in an external DCC software.

To make use of this feature, start by creating a particle system in the current scene. Add a mesh instance that serves as the source of the particle emission points. With the particle system selected, navigate to the viewport menu and select the _GPUParticles3D_ entry. From there, select `Create Emission Points From Node`.

A dialog window will pop up and ask you to select a node as the emission source. Choose one of the mesh instances in the scene and confirm your selection. The next dialog window deals with the amount of points and how to generate them.

`Emission Points` controls the total number of points that you are about to generate. Particles will spawn from these points, so what to enter here depends on the size of the source mesh (how much area you have to cover) and the desired density of the particles.

`Emission Source` offers 3 different options for how the points are generated. Select `Surface Points` if all you want to do is distribute the emission points across the surface of the mesh. Select `Surface Points + Normal (Directed)` if you also want to generate information about the surface normals and make particles move in the direction that the normals point at. The last option, `Volume`, creates emission points everywhere inside the mesh, not just across its surface.

The emission points are stored in the particle system's local coordinate system, so you can move the particle node around and the emission points will follow. This might be useful when you want to use the same particle system in several different places. On the other hand, you might have to regenerate the emission points when you move either the particle system or the source mesh.

### Emission shape textures

All the data for complex particle emission shapes is stored in a set of textures. How many, depends on the type of emission shape you use. If you set the `Shape` property in the `Emission Shape` group on the particle process material to `Points`, you have access to 2 texture properties, the `Point Texture` and the `Color Texture`. Set it to `Directed Points` and there is a third property called `Normal Texture`.

`Point Texture` contains all possible emission points that were generated in the previous step. A point is randomly selected for every particle when it spawns. `Normal Texture`, if it exists, provides a direction vector at that same location. If the `Color Texture` property is also set, it provides color for the particle, sampled at the same location as the other two textures and modulating any other color that was set up on the process material.

There is also the `Point Count` property that you can use to change the number of emission points at any time after creating the emission shape. This includes dynamically at runtime while the playing the game.

---

## Creating a 3D particle system

To get started with particles, the first thing we need to do is add a `GPUParticles3D` node to the scene. Before we can actually see any particles, we have to set up two parameters on the node: the `Process Material` and at least one `Draw Pass`.

### The process material

To add a process material to your particles node, go to `Process Material` in the inspector panel. Click on the box next to `Process Material` and from the dropdown menu select `New ParticleProcessMaterial`.

[ParticleProcessMaterial](../godot_csharp_rendering.md) is a special kind of material. We don't use it to draw any objects. We use it to update particle data and behavior on the GPU instead of the CPU, which comes with a massive performance boost. A click on the newly added material displays a long list of properties that you can set to control each particle's behavior.

### Draw passes

In order to render any particles, at least one draw pass needs to be defined. To do that, go to `Draw Passes` in the inspector panel. Click on the box next to `Pass 1` and select `New QuadMesh` from the dropdown menu. After that, click on the mesh and set its `Size` to 0.1 for both `x` and `y`. Reducing the mesh's size makes it a little easier to tell the individual particle meshes apart at this stage.

You can use up to 4 draw passes per particle system. Each pass can render a different mesh with its own unique material. All draw passes use the data that is computed by the process material, which is an efficient method for composing complex effects: Compute particle behavior once and feed it to multiple render passes.

If you followed the steps above, your particle system should now be emitting particles in a waterfall-like fashion, making them move downwards and disappear after a few seconds. This is the foundation for all particle effects. Take a look at the documentation for particle and particle material properties to learn how to make particle effects more interesting.

### Particle conversion

You can convert GPU particles to CPU particles at any time using the entry in the viewport menu. When you do so, keep in mind that not every feature of GPU particles is available for CPU particles, so the resulting particle system will look and behave differently from the original.

You can also convert CPU particles to GPU particles if you no longer need to use CPU particles. This is also done from the viewport menu.

Some of the most notable features that are lost during the conversion include:

- multiple draw passes
- turbulence
- sub-emitters
- trails
- attractors
- collision

You also lose the following properties:

- `Amount Ratio`
- `Interp to End`
- `Damping as Friction`
- `Emission Shape Offset`
- `Emission Shape Scale`
- `Inherit Velocity Ratio`
- `Velocity Pivot`
- `Directional Velocity`
- `Radial Velocity`
- `Velocity Limit`
- `Scale Over Velocity`

Converting GPU particles to CPU particles can become necessary when you want to release a game on older devices that don't support modern graphics APIs.

---

## Process material properties

The properties in this material control how particles behave and change over their lifetime. A lot of them have `Min`, `Max`, and `Curve` values that allow you to fine-tune their behavior. The relationship between these values is this: When a particle is spawned, the property is set with a random value between `Min` and `Max`. If `Min` and `Max` are the same, the value will always be the same for every particle. If the `Curve` is also set, the value of the property will be multiplied by the value of the curve at the current point in a particle's lifetime. Use the curve to change a property over the particle lifetime. Very complex behavior can be expressed this way.

> **Note:** This page covers how to use ParticleProcessMaterial for 3D scenes specifically. For information on how to use it in a 2D Scene see [ParticleProcessMaterial 2D Usage](tutorials_2d.md).

### Time

The `Lifetime Randomness` property controls how much randomness to apply to each particle's lifetime. A value of `0` means there is no randomness at all and all particles live for the same amount of time, set by the Lifetime property. A value of `1` means that a particle's lifetime is completely random within the range of [0.0, `Lifetime`].

## Particle flags

The `Align Y` property aligns each particle's Y-axis with its velocity. Enabling this property is the same as setting the Transform Align property to `Y to Velocity`.

The `Rotate Y` property works with the properties in the **Angle** and **Angular Velocity** groups to control particle rotation. `Rotate Y` has to be enabled if you want to apply any rotation to particles. The exception to this is any particle that uses the Standard Material where the `Billboard` property is set to `Particle Billboard`. In that case, particles rotate even without `Rotate Y` enabled.

When the `Disable Z` property is enabled, particles will not move along the Z-axis. Whether that is going to be the particle system's local Z-axis or the world Z-axis is determined by the Local Coords property.

The `Damping as Friction` property changes the behavior of damping from a constant deceleration to a deceleration based on speed.

## Spawn

### Emission shape

Particles can emit from a single point in space or in a way that they fill out a shape. The `Shape` property controls that shape. `Point` is the default value. All particles emit from a single point in the center of the particle system. When set to `Sphere` or `Box`, particles emit in a way that they fill out a sphere or a box shape evenly. You have full control over the size of these shapes. `Sphere Surface` works like `Sphere`, but instead of filling it out, all particles spawn on the sphere's surface.

The `Ring` emission shape makes particles emit in the shape of a ring. You can control the ring's direction by changing the `Ring Axis` property. `Ring Height` controls the thickness of the ring along its axis. `Ring Radius` and `Ring Inner Radius` control how wide the ring is and how large the hole in the middle should be. The image shows a particle system with a radius of `2` and an inner radius of `1.5`, the axis points along the global Z-axis.

In addition to these relatively simple shapes, you can select the `Points` or `Directed Points` option to create highly complex emission shapes. See the Complex emission shapes section for a detailed explanation of how to set these up.

### Angle

The `Angle` property controls a particle's starting rotation **as described above**. In order to have an actual effect on the particle, you have to enable one of two properties: **Rotate Y** rotates the particle around the particle system's Y-axis. The `Billboard` property in the Standard Material, if it is set to `Particle Billboard`, rotates the particle around the axis that points from the particle to the camera.

### Direction

> **Note:** The `Direction` property alone is not enough to see any particle movement. Whatever values you set here only take effect once velocity or acceleration properties are set, too.

The `Direction` property is a vector that controls each particle's direction of movement at the moment it is spawned. A value of `(X=1,Y=0,Z=0)` would make all particles move sideways along the X-axis. For something like a fountain where particles shoot out up in the air, a value of `(X=0,Y=1,Z=0)` would be a good starting point.

After setting a direction, you will notice that all particles move in the same direction in a straight line. The `Spread` property adds some variation and randomness to each particle's direction. The higher the value, the stronger the deviation from the original path. A value of `0` means there is no spread at all while a value of `180` makes particles shoot out in every direction. You could use this for something like pieces of debris during an explosion effect.

The `Flatness` property limits the spread along the Y-axis. A value of `0` means there is no limit and a value of `1` will eliminate all particle movement along the Y-axis. The particles will spread out completely "flat".

You won't see any actual movement until you also set some values for the velocity and acceleration properties below, so let's take a look at those next.

### Initial velocity

While the `Direction` property controls a particle's movement direction, the `Initial Velocity` controls how fast it goes. It's separated into `Velocity Min` and `Velocity Max`, both set to `0` by default, which is why you don't see any movement initially. As soon as you set values for either of these properties **as described above**, the particles begin to move. The direction is multiplied by these values, so you can make particles move in the opposite direction by setting a negative velocity.

## Accelerations

### Gravity

The next few property groups work closely together to control particle movement and rotation. `Gravity` drags particles in the direction it points at, which is straight down at the strength of Earth's gravity by default. Gravity affects all particle movement. If your game uses physics and the world's gravity can change at runtime, you can use this property to keep the game's gravity in sync with particle gravity. A `Gravity` value of `(X=0,Y=0,Z=0)` means no particle will ever move at all if none of the other movement properties are set.

### Angular velocity

`Angular Velocity` controls a particle's speed of rotation **as described above**. You can reverse the direction by using negative numbers for `Velocity Min` or `Velocity Max`. Like the **Angle** property, the rotation will only be visible if the **Rotate Y** flag is set or the `Particle Billboard` mode is selected in the Standard Material.

> **Note:** The **Damping** property has no effect on the angular velocity.

### Linear acceleration

A particle's velocity is a constant value: once it's set, it doesn't change and the particle will always move at the same speed. You can use the `Linear Accel` property to change the speed of movement over a particle's lifetime **as described above**. Positive values will speed up the particle and make it move faster. Negative values will slow it down until it stops and starts moving in the other direction.

It's important to keep in mind that when we change acceleration, we're not changing the velocity directly, we're changing the _change_ in velocity. A value of `0` on the acceleration curve does not stop the particle's movement, it stops the change in the particle's movement. Whatever its velocity was at that moment, it will keep moving at that velocity until the acceleration is changed again.

### Radial acceleration

The `Radial Accel` property adds a gravity-like force to all particles, with the origin of that force at the particle system's current location. Negative values make particles move towards the center, like the force of gravity from a planet on objects in its orbit. Positive values make particles move away from the center.

### Tangential acceleration

This property adds particle acceleration in the direction of the tangent to a circle on the particle system's XZ-plane with the origin at the system's center and a radius the distance between each particle's current location and the system's center projected onto that plane.

Let's unpack that.

A tangent to a circle is a straight line that "touches" the circle in a right angle to the circle's radius at the touch point. A circle on the particle system's XZ-plane is the circle that you see when you look straight down at the particle system from above.

`Tangential Accel` is always limited to that plane and never move particles along the system's Y-axis. A particle's location is enough to define such a circle where the distance to the system's center is the radius if we ignore the vector's Y component.

The `Tangential Accel` property will make particles orbit the particle system's center, but the radius will increase constantly. Viewed from above, particles will move away from the center in a spiral. Negative values reverse the direction.

### Damping

The `Damping` property gradually stops all movement. Each frame, a particle's movement is slowed down a little unless the total acceleration is greater than the damping effect. If it isn't, the particle will keep slowing down until it doesn't move at all. The greater the value, the less time it takes to bring particles to a complete halt.

### Attractor interaction

If you want the particle system to interact with particle attractors, you have to check the `Enabled` property. When it is disabled, the particle system ignores all particle attractors.

## Display

### Scale

`Scale` controls a particle's size **as described above**. You can set different values for `Scale Min` and `Scale Max` to randomize each particle's size. Negative values are not allowed, so you won't be able to flip particles with this property. If you emit particles as billboards, the `Keep Size` property on the Standard Material in your draw passes has to be enabled for any scaling to have an effect.

### Color

The `Color` property controls a particle's initial color. It will have an effect only after the `Use As Albedo` property in the `Vertex Color` group of the Standard Material is enabled. This property is multiplied with color coming from the particle material's own `Color` or `Texture` property.

There are two `Ramp` properties in the `Color` group. These allow you to define a range of colors that are used to set the particle's color. The `Color Ramp` property changes a particle's color over the course of its lifetime. It moves through the entire range of colors you defined. The `Color Initial Ramp` property selects the particle's initial color from a random position on the color ramp.

To set up a color ramp, click on the box next to the property name and from the dropdown menu select `New GradientTexture1D`. Click on the box again to open the texture's details. Find the `Gradient` property, click on the box next to it and select `New Gradient`. Click on that box again and you will see a color range. Click anywhere on that range to insert a new marker. You can move the marker with the mouse and delete it by clicking the right mouse button. When a marker is selected, you can use the color picker next to the range to change its color.

### Hue variation

Like the `Color` property, `Hue Variation` controls a particle's color, but in a different way. It does so not by setting color values directly, but by _shifting the color's hue_.

Hue describes a color's pigment: red, orange, yellow, green and so on. It does not tell you anything about how bright or how saturated the color is. The `Hue Variation` property controls the range of available hues **as described above**.

It works on top of the particle's current color. The values you set for `Variation Min` and `Variation Max` control how far the hue is allowed to shift in either direction. A higher value leads to more color variation while a low value limits the available colors to the closest neighbors of the original color.

### Animation

The `Animation` property group controls the behavior of sprite sheet animations in the particle's Standard Material. The `Min`, `Max`, and `Curve` values work **as described above**.

An animated sprite sheet is a texture that contains several smaller images aligned on a grid. The images are shown one after the other so fast that they combine to play a short animation, like a flipbook. You can use them for animated particles like smoke or fire. These are the steps to create an animated particle system:

1. Import a sprite sheet texture into the engine. If you don't have one at hand, you can download the high-res version of the example image.
2. Set up a particle system with at least one draw pass and assign a `Standard Material` to the mesh in that draw pass.
3. Assign the sprite sheet to the `Texture` property in the `Albedo` group
4. Set the material's `Billboard` property to `Particle Billboard`. Doing so makes the `Particles Anim` group available in the material.
5. Set `H Frames` to the number of columns and `V Frames` to the number of rows in the sprite sheet.
6. Check `Loop` if you want the animation to keep repeating.

That's it for the Standard Material. You won't see any animation right away. This is where the `Animation` properties come in. The `Speed` properties control how fast the sprite sheet animates. Set `Speed Min` and `Speed Max` to `1` and you should see the animation playing. The `Offset` properties control where the animation starts on a newly spawned particle. By default, it will always be the first image in the sequence. You can add some variety by changing `Offset Min` and `Offset Max` to randomize the starting position.

Depending on how many images your sprite sheet contains and for how long your particle is alive, the animation might not look smooth. The relationship between particle lifetime, animation speed, and number of images in the sprite sheet is this:

> **Note:** At an animation speed of `1.0`, the animation will reach the last image in the sequence just as the particle's lifetime ends. \[Animation\ FPS = \frac{Number\ of\ images}{Lifetime}\]

If your sprite sheet contains 64 (8x8) images and the particle's lifetime is set to `1 second`, the animation will be very smooth at **64 FPS** (1 second / 64 images). if the lifetime is set to `2 seconds`, it will still be fairly smooth at **32 FPS**. But if the particle is alive for `8 seconds`, the animation will be visibly choppy at **8 FPS**. In order to make the animation smooth again, you need to increase the animation speed to something like `3` to reach an acceptable framerate.

Note that the GPUParticles3D node's **Fixed FPS** also affects animation playback. For smooth animation playback, it's recommended to set it to 0 so that the particle is simulated on every rendered frame. If this is not an option for your use case, set **Fixed FPS** to be equal to the effective framerate used by the flipbook animation (see above for the formula).

### Turbulence

Turbulence adds noise to particle movement, creating interesting and lively patterns. Check the box next to the `Enabled` property to activate it. A number of new properties show up that control the movement speed, noise pattern and overall influence on the particle system. You can find a detailed explanation of these in the section on particle turbulence.

## Collision

The `Mode` property controls how and if emitters collide with particle collision nodes. Set it to `Disabled` to disable any collision for this particle system. Set it to `Hide On Contact` if you want particles to disappear as soon as they collide. Set it to `Constant` to make particles collide and bounce around. You will see two new properties appear in the inspector. They control how particles behave during collision events.

A high `Friction` value will reduce sliding along surfaces. This is especially helpful if particles collide with sloped surfaces and you want them to stay in place instead of sliding all the way to the bottom, like snow falling on a mountain. A high `Bounce` value will make particles bounce off surfaces they collide with, like rubber balls on a solid floor.

If the `Use Scale` property is enabled, the collision base size is multiplied by the particle's **current scale**. You can use this to make sure that the rendered size and the collision size match for particles with random scale or scale that varies over time.

You can learn more about particle collisions in the Collisions section in this manual.

## Sub-emitter

The `Mode` property controls how and when sub-emitters are spawned. Set it to `Disabled` and no sub-emitters will ever be spawned. Set it to `Constant` to make sub-emitters spawn continuously at a constant rate. The `Frequency` property controls how often that happens within the span of one second. Set the mode to `At End` to make the sub-emitter spawn at the end of the parent particle's lifetime, right before it is destroyed. The `Amount At End` property controls how many sub-emitters will be spawned. Set the mode to `At Collision` to make sub-emitters spawn when a particle collides with the environment. The `Amount At Collision` property controls how many sub-emitters will be spawned.

When the `Keep Velocity` property is enabled, the newly spawned sub-emitter starts off with the parent particle's velocity at the time the sub-emitter is created.

See the Sub-emitters section in this manual for a detailed explanation of how to add a sub-emitter to a particle system.

## Customizing the process material

If you need to change or implement new behaviors in shader code, you can do so by converting the current ParticleProcessMaterial to a [ShaderMaterial](../godot_csharp_rendering.md). Existing properties are preserved by the conversion process. Features that are enabled will also affect what's present in the converted shader code.

To do so, right-click on the material in the FileSystem dock and choose **Convert to ShaderMaterial**. You can also do so by right-clicking on any property holding a reference to the material in the inspector.

---

## 3D Particle system properties

### Emitter properties

The checkbox next to the `Emitting` property activates and deactivates the particle system. Particles will only be processed and rendered if the box is checked. You can set this property at runtime if you want to activate or deactivate particle systems dynamically.

The `Amount` property controls the maximum number of particles visible at any given time. Increase the value to spawn more particles at the cost of performance.

The `Amount Ratio` property is the ratio of particles compared to the amount that will be emitted. If it's less than `1.0`, the amount of particles emitted through the lifetime will be the `Amount` \* `Amount Ratio`. Changing this value while emitted doesn't affect already created particles and doesn't cause the particle system to restart. It's useful for making effects where the number of emitted particles varies over time.

You can set another particle node as a `Sub Emitter`, which will be spawned as a child of each particle. See the Sub-emitters section in this manual for a detailed explanation of how to add a sub-emitter to a particle system.

### Time properties

The `Lifetime` property controls how long each particle exists before it disappears again. It is measured in seconds. A lot of particle properties can be set to change over the particle's lifetime and blend smoothly from one value to another.

`Lifetime` and `Amount` are related. They determine the particle system's emission rate. Whenever you want to know how many particles are spawned per second, this is the formula you would use:

\[Particles per second = \frac{Amount}{Lifetime}\]

Example: Emitting 32 particles with a lifetime of 4 seconds each would mean the system emits 8 particles per second.

The `Interp to End` property causes all the particles in the node to interpolate towards the end of their lifetime.

If the checkbox next to the `One Shot` property is checked, the particle system will emit `amount` particles and then disable itself. It "runs" only once. This property is unchecked by default, so the system will keep emitting particles until it is disabled or destroyed manually. One-shot particles are a good fit for effects that react to a single event, like item pickups or splinters that burst away when a bullet hits a wall.

The `Preprocess` property is a way to fast-forward to a point in the middle of the particle system's lifetime and start rendering from there. It is measured in seconds. A value of `1` means that when the particle system starts, it will look as if it has been running for one second already.

This can be useful if you want the particle system to look like it has been active for a while even though it was just loaded into the scene. Consider the example below. Both particle systems simulate dust flying around in the area. With a preprocess value of `0`, there wouldn't be any dust for the first couple of seconds because the system has not yet emitted enough particles for the effect to become noticeable. This can be seen in the video on the left. Compare that to the video on the right where the particle system is preprocessed for `4` seconds. The dust is fully visible from the very beginning because we skipped the first four seconds of "setup" time.

You can slow down or speed up the particle system with the `Speed Scale` property. This applies to processing the data as well as rendering the particles. Set it to `0` to pause the particle system completely or set it to something like `2` to make it move twice as fast.

The `Explosiveness` property controls whether particles are emitted sequentially or simultaneously. A value of `0` means that particles emit one after the other. A value of `1` means that all `amount` particles emit at the same time, giving the effect a more "explosive" appearance.

The `Randomness` property adds some randomness to the particle emission timing. When set to `0`, there is no randomness at all and the interval between the emission of one particle and the next is always the same: the particles are emitted at _regular_ intervals. A `Randomness` value of `1` makes the interval completely random. You can use this property to break up some of the uniformity in your effects. When `Explosiveness` is set to `1`, this property has no effect.

The `Fixed FPS` property limits how often the particle system is processed. This includes property updates as well as collision and attractors. This can improve performance a lot, especially in scenes that make heavy use of particle collision. Note that this does not change the speed at which particles move or rotate. You would use the `Speed Scale` property for that.

When you set `Fixed FPS` to very low values, you will notice that the particle animation starts to look choppy. This can sometimes be desired if it fits the art direction, but most of the time, you'll want particle systems to animate smoothly. That's what the `Interpolate` property does. It blends particle properties between updates so that even a particle system running at `10` FPS appears as smooth as running at `60`.

> **Note:** When using particle collision, tunneling can occur if the particles move fast and colliders are thin. This can be remedied by increasing `Fixed FPS` (at a performance cost).

### Collision properties

> **See also:** Setting up particle collision requires following further steps described in 3D Particle collisions.

The `Base Size` property defines each particle's default collision size, which is used to check whether a particle is currently colliding with the environment. You would usually want this to be about the same size as the particle. It can make sense to increase this value for particles that are very small and move very fast to prevent them from clipping through the collision geometry.

### Drawing properties

The `Visibility AABB` property defines a box around the particle system's origin. As long as any part of this box is in the camera's field of view, the particle system is visible. As soon as it leaves the camera's field of view, the particle system stops being rendered at all. You can use this property to boost performance by keeping the box as small as possible.

One thing to keep in mind when you set a size for the `Visibility AABB` is that particles that are outside of its bounds disappear instantly when it leaves the camera's field of view. Particle collision will also not occur outside the `Visibility AABB`. While not technically a bug, this can have a negative effect on the visual experience.

When the `Local Coords` property is checked, all particle calculations use the local coordinate system to determine things like up and down, gravity, and movement direction. Up and down, for example, would follow the particle system's or its parent node's rotation. When the property is unchecked, the global world space is used for these calculations: Down will always be -Y in world space, regardless of the particle system's rotation.

The `Draw Order` property controls the order in which individual particles are drawn. `Index` means that they are drawn in the order of emission: particles that are spawned later are drawn on top of earlier ones. `Lifetime` means that they are drawn in the order of their remaining lifetime. `Reverse Lifetime` reverses the `Lifetime` draw order. `View Depth` means particles are drawn according to their distance from the camera: The ones closer to the camera on top of those farther away.

The `Transform Align` property controls the particle's default rotation. `Disabled` means they don't align in any particular way. Instead, their rotation is determined by the values set in the process material. `Z-Billboard` means that the particles will always face the camera. This is similar to the `Billboard` property in the Standard Material. `Y to Velocity` means that each particle's Y-axis aligns with its movement direction. This can be useful for things like bullets or arrows, where you want particles to always point "forward". `Z-Billboard + Y to Velocity` combines the previous two modes. Each particle's Z-axis will point towards the camera while its Y-axis will align with their velocity.

### Trail properties

The `Enabled` property controls whether particles are rendered as trails. The box needs to be checked if you want to make use of particle trails.

The `Length Secs` property controls for how long a trail should be emitted. The longer this duration is, the longer the trail will be.

See the Particle trails section in this manual for a detailed explanation of how particle trails work and how to set them up.

---

## Particle sub-emitters

Sometimes a visual effect cannot be created with a single particle system alone. Sometimes a particle system needs to be spawned as a response to something that happens in another particle system. Fireworks are a good example of that. They usually consist of several stages of explosions that happen in sequence. Sub-emitters are a good way to achieve this kind of effect.

A sub-emitter is a particle system that spawns as a child of another particle system. You can add sub-emitters to sub-emitters, chaining particle effects as deep as you like.

To create a sub-emitter, you need at least two particle systems in the same scene. One of them will be the parent and one will be set as the child. Find the `Sub Emitter` property on the parent and click the box next to it to assign the sub-emitter. You will see a list of available particle systems in the scene. Select one and click the confirmation button.

Particle systems from instanced scenes can be set as sub-emitters too, as long as the `Editable Children` property is enabled on the instanced scene. This also works the other way around: You can assign a sub-emitter to a particle system in an instanced scene, even one coming from a different instanced scene.

> **Note:** When you set a particle system as the sub-emitter of another, the system stops emitting, even if the `Emitting` property was checked. Don't worry, it didn't break. This happens to every particle system as soon as it becomes a sub-emitter. You also won't be able to re-enable the property as long as the particle system is used as a sub-emitter.

> **Warning:** Even though the parent particle system can be selected from the list of available particle systems, a particle system which is its own sub-emitter does not work in Godot. It will simply not spawn. The same is true for any other kind of recursive or self-referential sub-emitter setup.

### Emitter mode

When you assign a sub-emitter, you don't see it spawn right away. Emitting is disabled by default and needs to be enabled first. Set the `Mode` property in the `Sub Emitter` group of the ParticleProcessMaterial to something other than `Disabled`.

The emitter mode also determines how many sub-emitter particles are spawned. `Constant` spawns a single particle at a frequency set by the `Frequency` property. For `At End` and `At Collision` you can set the amount directly with the `Amount At End` and the `Amount At Collision` properties.

### Limitations

One thing to keep in mind is that the total number of active particles from the sub-emitter is always capped by the `Amount` property on the sub-emitter particle system. If you find that there are not enough particles spawned from the sub-emitter, you might have to increase the amount in the particle system.

Some emitter properties are ignored when a particle system is spawned as a sub-emitter. The `Explosiveness` property, for example, has no effect. Depending on the emitter mode, the particles are either spawned sequentially at fixed intervals or explosively all at once.

---

## 3D Particle trails

> **Note:** Particle trails are only supported in the Forward+ and Mobile renderers, not Compatibility.

Godot provides several types of trails you can add to a particle system. Before you can work with trails, you need to set up a couple of parameters first. Create a new particle system and assign a process material as described before. In the `Trails` group of the particle system, check the box next to `Enabled` and increase the emission duration by setting `Lifetime` to something like `0.8`. On the process material, set `Direction` to `(X=0,Y=1.0,Z=0)` and `Initial Velocity` to `10.0` for both `Min` and `Max`.

The only thing that's still missing is a mesh for the draw pass. The type of mesh that you set here controls what kind of particle trail you will end up with.

### Ribbon trails

The simplest type of particle trail is the ribbon trail. Navigate to the `Draw Passes` section and select `New RibbonTrailMesh` from the options for `Pass 1`. A [RibbonTrailMesh](../godot_csharp_rendering.md) is a simple quad that is divided into sections and then stretched and repeated along those sections.

Assign a new Standard Material to the `Material` property and enable `Use Particle Trails` in the `Transform` property group. The particles should now be emitting in trails.

You have two options for the ribbon mesh `Shape` parameter. `Cross` creates two perpendicular quads, making the particle trail a little more three-dimensional. This really only makes sense if you don't draw the trails in `Particle Billboard` mode and helps when looking at the particles from different angles. The `Flat` option limits the mesh to a single quad and works best with billboard particles.

The `Size` parameter controls the trail's width. Use it to make trails wider or more narrow.

`Sections`, `Section Length` and `Section Segments` all work together to control how smooth the particle trail looks. When a particle trail does not travel in a straight line, the more sections it has the smoother it looks as it bends and swirls. `Section Length` controls the length of each section. Multiply this value by the number of sections to know the trail's total length.

The `Section Segments` parameter further subdivides each section into segments. It has no effect on the smoothness of the trail's sections, though. Instead, it controls the smoothness of the particle trail's overall shape. The `Curve` property defines this shape. Click the box next to `Curve` and assign or create a new curve. The trail will be shaped just like the curve with the curve's value at `0.0` at the trail's head and the curve's value at `1.0` at the trail's tail.

Depending on the complexity of the curve, the particle trail's shape will not look very smooth when the number of sections is low. This is where the `Section Segments` property comes in. Increasing the amount of section segments adds more vertices to the trail's sides so that it can follow the curve more closely.

### Tube trails

Tube trails share a lot of their properties with ribbon trails. The big difference between them is that tube trails emit cylindrical meshes instead of quads.

To create a tube trail, navigate to the `Draw Passes` section and select `New TubeTrailMesh` from the options for `Pass 1`. A [TubeTrailMesh](../godot_csharp_rendering.md) is a cylinder that is divided into sections and then stretched and repeated along those sections. Assign a new Standard Material to the `Material` property and enable `Use Particle Trails` in the `Transform` property group. The particles should now be emitting in long, cylindrical trails.

The `Radius` and `Radial Steps` properties are to tube trails what `Size` is to ribbon trails. `Radius` defines the radius of the tube and increases or decreases its overall size. `Radial Steps` controls the number of sides around the tube's circumference. A higher value increases the resolution of the tube's cap.

`Sections` and `Section Length` work the same for tube trails and ribbon trails. They control how smooth the tube trail looks when it is bending and twisting instead of moving in a straight line. Increasing the number of sections will make it look smoother. Change the `Section Length` property to change the length of each section and with it the total length of the trail. `Section Rings` is the tube equivalent of the `Section Segments` property for ribbons. It subdivides the sections and adds more geometry to the tube to better fit the custom shape defined in the `Curve` property.

You can shape tube trails with curves, just as you can with ribbon trails. Click the box next to the `Curve` property and assign or create a new curve. The trail will be shaped like the curve with the curve's value at `0.0` at the trail's head and the curve's value at `1.0` at the trail's tail.

An important property you might want to set is `Transform Align` in the particle system's `Drawing` group. If you leave it as is, the tubes will not preserve volume; they flatten out as they move because their Y-axis keeps pointing up even as they change direction. This can cause a lot of rendering artifacts. Set the property to `Y to Velocity` instead and each particle trail keeps its Y-axis aligned along the direction of its movement.

---

## Particle turbulence

Turbulence uses a noise texture to add variation and interesting patterns to particle movement. It can be combined with particle attractors and collision nodes to create even more complex looking behavior.

There are two things you have to do before turbulence has any effect on a particle system. First you must add movement to the particle system. Turbulence modifies a particle's movement direction and speed, but it doesn't create any. It is enough to give the particle system some gravity, but you can just as well create a number of attractors if you want the particles to follow a more complex movement path. Second, you need to enable turbulence in the particle process material. Once enabled, you have access to all the turbulence properties.

> **Warning:** Turbulence makes use of 3D noise, which has a high performance cost on the GPU. Only enable turbulence on a few particle systems on screen at most. Using turbulence is not recommended when targeting mobile/web platforms.

### Noise properties

The basis for particle turbulence is a noise pattern. There are several properties that allow you to manipulate different attributes of this pattern.

The `Noise Strength` property controls the pattern's contrast, which affects the overall turbulence sharpness. A lower value creates a softer pattern where individual movement paths are not as sharply separated from another. Set this to a higher number to make the pattern more distinct.

The `Noise Scale` property controls the pattern's frequency. It basically changes the noise texture's UV scale where a smaller value produces finer detail, but repeating patterns become noticeable faster. A larger value results in a weaker turbulence pattern overall, but the particle system can cover a larger area before repetition starts to become an issue.

The `Noise Speed` property takes a vector and controls the noise panning speed and direction. This allows you to move the noise pattern over time, which adds another layer of movement variation to the particle system.

> **Warning:** Don't mix up particle movement speed and noise panning speed! They are two different things. Particle movement is determined by a number of properties, including the turbulence noise. The `Noise Speed` property moves the pattern itself, which in turn changes where the noise affects the particles.

At a value of `(X=0,Y=0,Z=0)`, the noise pattern doesn't move at all. The influence on particle movement stays the same at any given point. Set the speed to `(X=1,Y=0,Z=0)` instead, and the noise pattern moves along the X-axis.

The `Noise Speed Random` property adds some randomness to the noise panning speed. This helps with breaking up visible patterns, especially at higher panning speeds when repetition becomes noticeable faster.

### Influence properties

The influence properties determine how much each particle is affected by turbulence. Use `Influence Min` to set a minimum value and `Influence Max` to set a maximum value. When a particle spawns, the influence is randomly chosen from within this range. You can also set up a curve with the `Influence Over Life` property that modifies that value over each particle's lifetime. These three properties together control the strength of the turbulence's effect on the particle system as described before.

Since these properties affect the overall influence of the turbulence over a particle system, both movement direction and speed change as you set different values. A stronger influence causes a particle to move faster and all particles to follow along narrower paths as a result of that.

### Displacement properties

Displacement changes a particle's starting position. Use `Initial Displacement Min` to set a lower limit and `Initial Displacement Max` to set an upper limit. When a particle spawns, the amount of displacement is randomly chosen from within this range and multiplied by a random direction.

Displacement is very useful to break up regular shapes or to create complex shapes from simpler ones. The only difference between the particle systems in the screenshot below is the value given to the displacement properties.

---
