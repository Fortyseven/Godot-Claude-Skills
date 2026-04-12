# Godot 4 C# Tutorials — Performance (Part 2)

> 7 tutorials. C#-specific code examples.

## Reducing stutter from shader (pipeline) compilations

> **Warning:** This page only applies to the Forward+ and Mobile renderers, not Compatibility. Ubershaders and pipeline precompilation rely on functionality only available in modern low-level graphics APIs (Vulkan, Direct3D 12, Metal). The Compatibility renderer uses OpenGL 3.3, OpenGL ES 3.0, or WebGL 2.0 depending on the platform. These versions lack the functionality to effectively implement ubershaders and pipeline precompilation. To avoid shader stutters in Compatibility, you need to use the legacy approach of preloading materials, shaders, and particles by displaying them for at least one frame in the view frustum when the level is loading.

Pipeline compilation, also commonly known as shader compilation, is an expensive operation required by the engine to be able to draw any kind of content with the GPU.

In more precise terms, _shader compilation_ involves the translation of the GLSL code that Godot generates into an intermediate format that can be shared across systems (such as SPIR-V when using Vulkan). However, this format can't be used by the GPU directly.

_Pipeline compilation_ is the step where the GPU driver converts the intermediate shader format (the result from shader compilation) to something the GPU can actually use for rendering. Drivers usually keep a cache of pipelines stored somewhere in the system to avoid repeating the process every time a game is run. This cache is usually deleted when the driver is updated.

Pipelines contain more information than just the shader code, which means that for each shader, there can be dozens of pipelines or more! This makes it difficult for an engine to compile them ahead of time, both because it would be very slow, and because it would take up a lot of memory. On top of that, this step can only be performed on the user's system and it is very tough to share the result between users unless they have the exact same hardware and driver version.

Before Godot 4.4, there was no solution to pipeline compilation other than generating them when an object shows up inside the camera's view, leading to the infamous _shader stutter_ or hitches that only occur during the first playthrough. **With Godot 4.4, new mechanisms have been introduced to mitigate stutters from pipeline compilation.**

- **Ubershaders**: Godot makes use of specialization constants, a feature that allows the driver to optimize a pipeline's code around a set of parameters such as lighting, shadow quality, etc. Specialization constants are used to optimize a shader by limiting unnecessary features. Changing a specialization constant requires recompiling the pipeline. Ubershaders are a special version of the shader that are able to change these constants while rendering, which means Godot can precompile just one pipeline ahead of time and compile the more optimized versions on the background during gameplay. This reduces the amount of pipelines that need to be created significantly.
- **Pipeline precompilation**: By using ubershaders, the engine can precompile pipelines ahead of time in multiple places such as when meshes are loaded or when nodes are added to the scene. By being part of the resource loading process, pipelines can even be precompiled in multiple background threads if possible during loading screens or even gameplay.

Starting in Godot 4.4, Godot will detect which pipelines are needed and precompile them at load-time. This detection system is mostly automatic, but it relies on the RenderingServer seeing evidence of all shaders, meshes, or rendering features at load-time. For example, if you load a mesh and shader while the game is running, the pipeline for that mesh/shader combination won't be compiled until the mesh/shader is loaded. Similarly, things like enabling MSAA, or instancing a VoxelGI node while the game is running will trigger pipeline recompilations.

### Pipeline precompilation monitors

Compiling pipelines ahead of time is the main mechanism Godot uses to mitigate shader stutters, but it's not a perfect solution. Being aware of the situations that can lead to pipeline stutters can be very helpful, and the workarounds are pretty straightforward compared to previous versions. These workarounds may be less necessary over time with future versions of Godot as more detection techniques are implemented.

The Godot debugger offers monitors for tracking the amount of pipelines created by the game and the step that triggered their compilation. You can keep an eye on these monitors as the game runs to identify potential sources of shader stutters without having to wipe your driver cache every time you wish to test. Sudden increases of these values outside of loading screens can show up as hitches during gameplay the first time someone plays the game on their system. **It is recommended you take a look at these monitors to identify possible sources of stutter for your players**, as you might be unable to experience them yourself without deleting your driver cache or testing on a weaker system.

> **Note:** We can see the pipelines compiled during gameplay and verify which steps could possibly cause stuttters. Note that these values will only increase and never go down, as deleted pipelines are not tracked by these monitors and pipelines may be erased and recreated during gameplay.

- **Canvas**: Compiled when drawing a 2D node. The engine does not currently feature precompilation for 2D elements and stutters will show up when the 2D node is drawn for the first time.
- **Mesh**: Compiled as part of loading a 3D mesh and identifying what pipelines can be precompiled from its properties. These can lead to stutters if a mesh is loaded during gameplay, but they can be mitigated if the mesh is loaded by using a background thread. **Modifiers that are part of nodes such as material overrides can't be compiled on this step**.
- **Surface**: Compiled when a frame is about to be drawn and 3D objects were instanced on the scene tree for the first time. This can also include compilation for nodes that aren't even visible on the scene tree. The stutter will occur only on the first frame the node is added to the scene, which won't result in an obvious stutter if it happens right after a loading screen.
- **Draw**: Compiled on demand when a 3D object needs to be drawn and an ubershader was not precompiled ahead of time. The engine is unable to precompile this pipeline due to triggering a case that hasn't been covered yet or a modification that was done to the engine's code. Leads to stutters during gameplay. This is identical to Godot versions before 4.4. If you see compilations here, please [let the developers know](https://github.com/godotengine/godot/issues) as this should never happen with the Ubershader system. Make sure to attach a minimal reproduction project when doing so.
- **Specialization**: Compiled in the background during gameplay to optimize the framerate. Unable to cause stutters, but may result in reduced framerates if there are many happening per frame.

### Pipeline precompilation features

Godot offers a lot of rendering features that are not necessarily used by every game. Unfortunately, pipeline precompilation can't know ahead of time if a particular feature is used by a project. Some of these features can only be detected when a user adds a node to the scene or toggles a particular setting in the project or the environment. The pipeline precompilation system will keep track of these features as they're encountered for the first time and enable precompilation of them for any meshes or surfaces that are created afterwards.

If your game makes use of these features, **make sure to have a scene that uses them as early as possible** before loading the majority of the assets. This scene can be very simple and will do the job as long as it uses the features the game plans to use. It can even be rendered off-screen for at least one frame if necessary, e.g. by covering it with a [ColorRect](../godot_csharp_ui_controls.md) node or using a [SubViewport](../godot_csharp_rendering.md) located outside the window bounds.

You should also keep in mind that changing any of these features during gameplay will result in immediate stutters. Make sure to only change these features from configuration screens if necessary and insert loading screens and messages when the changes are applied.

- **MSAA Level**: Enabled when the level of 3D MSAA is changed on the project settings. Unfortunately, different MSAA levels being used on different viewports will lead to stutters as the engine only keeps track of one level at a time to perform precompilation.
- **Reflection Probes**: Enabled when a ReflectionProbe node is placed on the scene.
- **Separate Specular**: Enabled when using effects like sub-surface scattering or a compositor effect that relies on sampling the specularity directly off the screen.
- **Motion Vectors**: Enabled when using effects such as TAA, FSR2 or a compositor effect that requires motion vectors (such as motion blur).
- **Normal and Roughness**: Enabled when using SDFGI, VoxelGI, screen-space reflections, SSAO, SSIL, or using the `normal_roughness_buffer` in a custom shader or [CompositorEffect](../godot_csharp_rendering.md).
- **Lightmaps**: Enabled when a LightmapGI node is placed on the scene and a node uses a baked lightmap.
- **VoxelGI**: Enabled when a VoxelGI node is placed on the scene.
- **SDFGI**: Enabled when the WorldEnvironment enables SDFGI.
- **Multiview**: Enabled for XR projects.
- **16/32-bit Shadows**: Enabled when the configuration of the depth precision of shadowmaps is changed on the project settings.
- **Omni Shadow Dual Paraboloid**: Enabled when an omni light casts shadows and uses the dual paraboloid mode.
- **Omni Shadow Cubemap**: Enabled when an omni light casts shadows and uses the cubemap mode (which is the default).

If you witness stutters during gameplay and the monitors report a sudden increase in compilations during the **Surface** step, it is very likely a feature was not enabled ahead of time. Ensuring that this effect is enabled while loading your game will likely mitigate the issue.

### Pipeline precompilation instancing

One common source of stutters in games is the fact that some effects are only instanced on the scene because of interactions that only happen during gameplay. For example, if you have a particle effect that is only added to the scene through a script when a player does an action. Even if the scene is preloaded, the engine might be unable to precompile the pipelines until the effect is added to the scene at least once.

Luckily, it's possible for Godot 4.4 and later to precompile these pipelines as long as the scene is instantiated at least once on the scene, even if it's completely invisible or outside of the camera's view.

If you're aware of any effects that are added to the scene dynamically during gameplay and are seeing sudden increases on the compilations monitor when these effects show up, a workaround is to attach a hidden version of the effect somewhere that is guaranteed to show up.

For example, if the player character is able to cause some sort of explosion, you can attach the effect as a child of the player as an invisible node. Make sure to disable the script attached to the hidden node or to hide any other nodes that could cause issues, which can be done by enabling **Editable Children** on the node.

### Shader baker

Since Godot 4.5, you can choose to bake shaders on export to improve initial startup time. This will generally not resolve existing stutters, but it will reduce the time it takes to load the game for the first time. This is especially the case when using Direct3D 12 or Metal, which have significantly slower initial shader compilation times than Vulkan due to the conversion step required. Godot's own shaders use GLSL and SPIR-V, but Direct3D 12 and Metal use different formats.

> **Note:** The shader baker can only bake the source into the intermediate format (SPIR-V for Vulkan, DXIL for Direct3D 12, MIL for Metal). It cannot bake the intermediate format into the final pipeline, as this is dependent on the GPU driver and the hardware. The shader baker is not a replacement for pipeline precompilation, but it aims to complement it.

When enabled, the shader baker will bundle compiled shader code into the PCK, which results in the shader compilation step being skipped entirely. The downside is that exporting will take slightly longer. The PCK file will be larger by a few megabytes.

The shader baker is disabled by default, but you can enable it in each export preset in the Export dialog by ticking the Shader Baker > Enabled export option.

Note that shader baking will only be able to export shaders for drivers supported by the platform the editor is currently running on:

- The editor running on Windows can export shaders for Vulkan and Direct3D 12.
- The editor running on macOS can export shaders for Vulkan and Metal.
- The editor running on Linux can export shaders for Vulkan only.
- The editor running on Android can export shaders for Vulkan only.

The shader baker will only export shaders that match the `rendering/rendering_device/driver` project setting for the target platform.

> **Note:** The shader baker is only supported for the Forward+ and Mobile renderers. It will have no effect if the project uses the Compatibility renderer, or for users who make use of the Compatibility fallback due to their hardware not supporting the Forward+ or Mobile renderer. This also means the shader baker is not supported on the web platform, as the web platform only supports the Compatibility renderer.

---

## Thread-safe APIs

### Threads

Threads are used to balance processing power across CPUs and cores. Godot supports multithreading, but not in the whole engine.

Below is a list of ways multithreading can be used in different areas of Godot.

### Global scope

Most `Global Scope` singletons are thread-safe by default. Accessing servers from threads is supported. However, for the **rendering** and **physics** servers, thread-safe operation must be enabled in the project settings first.

This makes singletons ideal for code that creates dozens of thousands of instances in servers and controls them from threads. Of course, it requires a bit more code, as this is used directly and not within the scene tree.

### Scene tree

Interacting with the active scene tree is **not** thread-safe. Make sure to use mutexes when sending data between threads. If you want to call functions or set properties from a thread, you may use [call_deferred](../godot_csharp_misc.md) or [set_deferred](../godot_csharp_misc.md):

```csharp
// Unsafe:
node.AddChild(childNode);
// Safe:
node.CallDeferred(Node.MethodName.AddChild, childNode);
```

However, creating scene chunks (nodes in tree arrangement) outside the active tree is fine. This way, parts of a scene can be built or instantiated in a thread, then added in the main thread:

```csharp
PackedScene enemyScene = GD.Load<PackedScene>("res://EnemyScene.scn");
Node enemy = enemyScene.Instantiate<Node>();
enemy.AddChild(weapon);
world.CallDeferred(Node.MethodName.AddChild, enemy);
```

Still, this is only really useful if you have **one** thread loading data. Attempting to load or create scene chunks from multiple threads may work, but you risk resources (which are only loaded once in Godot) being tweaked by the multiple threads, resulting in unexpected behaviors or crashes.

Only use more than one thread to generate scene data if you _really_ know what you are doing and you are sure that a single resource is not being used or set in multiple ones. Otherwise, you are safer just using the servers API (which is fully thread-safe) directly and not touching scene or resources.

### Rendering

Instancing nodes that render anything in 2D or 3D (such as [Sprite2D](../godot_csharp_nodes_2d.md) or [MeshInstance3D](../godot_csharp_nodes_3d.md)) is _not_ thread-safe by default. To run the rendering driver on a separate thread, set the [Rendering > Driver > Thread Model](../godot_csharp_misc.md) project setting to **Separate**.

Note that the **Separate** thread model has several known bugs, so it may not be usable in all scenarios.

> **Warning:** You should avoid calling functions involving direct interaction with the GPU on other threads, such as creating new textures or modifying and retrieving image data. These operations can lead to performance stalls because they require synchronization with the [RenderingServer](../godot_csharp_rendering.md), as data needs to be transmitted to or updated on the GPU.

### Physics

Physics simulation is _not_ thread-safe by default. To run the physics servers on separate threads (making them thread-safe), enable the following project settings:

- **PhysicsServer2D:** [Physics > 2D > Run on Separate Thread](../godot_csharp_misc.md).
- **PhysicsServer3D:** [Physics > 3D > Run on Separate Thread](../godot_csharp_misc.md).

### Navigation

[NavigationServer2D](../godot_csharp_misc.md) and [NavigationServer3D](../godot_csharp_misc.md) are both thread-safe and thread-friendly.

The navigation-related query functions can be called by threads and run in true parallel.

By default, a conservative number of threads is supported running in true parallel on navigation maps before additional threads have to wait for map data access at a semaphore. To increase the number of threads that can run simultaneously on map data, set [Navigation > Pathfinding > Max Threads](../godot_csharp_misc.md).

The navigation server-related resources like NavigationSourceGeometryData, NavigationMesh, and NavigationPolygon are all thread-safe but not necessarily thread-friendly. They use internal read-write locks for thread-safety so editing the same resource (e.g. a single big navmesh) on multiple threads at the same time can cause thread congestion.

The navigation-related helper classes like [AStar2D](../godot_csharp_misc.md), [AStar3D](../godot_csharp_misc.md), and [AStarGrid2D](../godot_csharp_misc.md) are **not** thread-safe. They can be used with threads to some limited capacity, but using two or more threads on the same AStar object causes corruption. For example, using a dedicated background thread per AStar object to populate points or do queries works, but two threads using the same AStar object would corrupt each other's data.

### GDScript arrays and dictionaries

In GDScript, reading and writing elements from multiple threads is OK, but anything that changes the container size (resizing, adding, or removing elements) requires locking a mutex.

### Resources

Modifying a unique resource from multiple threads is not supported. However, handling references on multiple threads _is_ supported. Hence loading resources on a thread is as well - scenes, textures, meshes, etc - can be loaded and manipulated on a thread and then added to the active scene on the main thread. The limitation here is as described above: one must be careful not to load the same resource from multiple threads at once. Therefore, it's easiest to use **one** thread for loading and modifying resources, and then the main thread for adding them.

---

## Optimization using MultiMeshes

> **Work in progress:** The content of this page was not yet updated for Godot `4.6` and may be **outdated**. If you know how to improve this page or you can confirm that it's up to date, feel free to [open a pull request](https://github.com/godotengine/godot-docs).

For large amount of instances (in the thousands), that need to be constantly processed (and certain amount of control needs to be retained), using servers directly is the recommended optimization.

When the amount of objects reach the hundreds of thousands or millions, none of these approaches are efficient anymore. Still, depending on the requirements, there is one more optimization possible.

### MultiMeshes

A [MultiMesh](../godot_csharp_rendering.md) is a single draw primitive that can draw up to millions of objects in one go. It's extremely efficient because it uses the GPU hardware to do this.

The only drawback is that there is no _screen_ or _frustum_ culling possible for individual instances. This means, that millions of objects will be _always_ or _never_ drawn, depending on the visibility of the whole MultiMesh. It is possible to provide a custom visibility rect for them, but it will always be _all-or-none_ visibility.

If the objects are simple enough (just a couple of vertices), this is generally not much of a problem as most modern GPUs are optimized for this use case. A workaround is to create several MultiMeshes for different areas of the world.

It is also possible to execute some logic inside the vertex shader (using the `INSTANCE_ID` or `INSTANCE_CUSTOM` built-in constants). For an example of animating thousands of objects in a MultiMesh, see the Animating thousands of fish tutorial. Information to the shader can be provided via textures (there are floating-point [Image](../godot_csharp_resources.md) formats which are ideal for this).

Another alternative is to use a GDExtension and C++, which should be extremely efficient (it's possible to set the entire state for all objects using linear memory via the [RenderingServer.multimesh_set_buffer()](../godot_csharp_rendering.md) function). This way, the array can be created with multiple threads, then set in one call, providing high cache efficiency.

Finally, it's not required to have all MultiMesh instances visible. The amount of visible ones can be controlled with the [MultiMesh.visible_instance_count](../godot_csharp_rendering.md) property. The typical workflow is to allocate the maximum amount of instances that will be used, then change the amount visible depending on how many are currently needed.

### Multimesh example

Here is an example of using a MultiMesh from code. Languages other than GDScript may be more efficient for millions of objects, but for a few thousands, GDScript should be fine.

```csharp
using Godot;

public partial class MyMultiMeshInstance3D : MultiMeshInstance3D
{
    public override void _Ready()
    {
        // Create the multimesh.
        Multimesh = new MultiMesh();
        // Set the format first.
        Multimesh.TransformFormat = MultiMesh.TransformFormatEnum.Transform3D;
        // Then resize (otherwise, changing the format is not allowed)
        Multimesh.InstanceCount = 1000;
        // Maybe not all of them should be visible at first.
        Multimesh.VisibleInstanceCount = 1000;

        // Set the transform of the instances.
        for (int i = 0; i < Multimesh.VisibleInstanceCount; i++)
        {
            Multimesh.SetInstanceTransform(i, new Transform3D(Basis.Identity, new Vector3(i * 20, 0, 0)));
        }
    }
}
```

---

## Using multiple threads

> **See also:** For a list of multithreading primitives in C++, see Multithreading / Concurrency.

### Threads

Threads allow simultaneous execution of code. It allows off-loading work from the main thread.

Godot supports threads and provides many handy functions to use them.

> **Note:** If using other languages (C#, C++), it may be easier to use the threading classes they support.

> **Warning:** Before using a built-in class in a thread, read Thread-safe APIs first to check whether it can be safely used in a thread.

### Creating a Thread

To create a thread, use the following code:

Your function will, then, run in a separate thread until it returns. Even if the function has returned already, the thread must collect it, so call [Thread.wait_to_finish()](../godot_csharp_core.md), which will wait until the thread is done (if not done yet), then properly dispose of it.

> **Warning:** Creating threads is a slow operation, especially on Windows. To avoid unnecessary performance overhead, make sure to create threads before heavy processing is needed instead of creating threads just-in-time. For example, if you need multiple threads during gameplay, you can create threads while the level is loading and only actually start processing with them later on. Additionally, locking and unlocking of mutexes can also be an expensive operation. Locking should be done carefully; avoid locking too often (or for too long).

### Mutexes

Accessing objects or data from multiple threads is not always supported (if you do it, it will cause unexpected behaviors or crashes). Read the Thread-safe APIs documentation to understand which engine APIs support multiple thread access.

When processing your own data or calling your own functions, as a rule, try to avoid accessing the same data directly from different threads. You may run into synchronization problems, as the data is not always updated between CPU cores when modified. Always use a [Mutex](../godot_csharp_core.md) when accessing a piece of data from different threads.

When calling [Mutex.lock()](../godot_csharp_misc.md), a thread ensures that all other threads will be blocked (put on suspended state) if they try to _lock_ the same mutex. When the mutex is unlocked by calling [Mutex.unlock()](../godot_csharp_misc.md), the other threads will be allowed to proceed with the lock (but only one at a time).

Here is an example of using a Mutex:

### Semaphores

Sometimes you want your thread to work _"on demand"_. In other words, tell it when to work and let it suspend when it isn't doing anything. For this, [Semaphores](../godot_csharp_core.md) are used. The function [Semaphore.wait()](../godot_csharp_core.md) is used in the thread to suspend it until some data arrives.

The main thread, instead, uses [Semaphore.post()](../godot_csharp_core.md) to signal that data is ready to be processed:

---

## Optimization using Servers

Engines like Godot provide increased ease of use thanks to their high-level constructs and features. Most of them are accessed and used via the [scene system](tutorials_scripting.md). Using nodes and resources simplifies project organization and asset management in complex games.

There are several drawbacks to this:

- There is an extra layer of complexity.
- Performance is lower than when using simple APIs directly.
- It is not possible to use multiple threads to control them.
- More memory is needed.

In most cases, this is not really a problem. Godot is well-optimized, and most operations are handled with signals, which means no polling is required. Still, sometimes, we want to extract better performance from the hardware when other avenues of optimization have been exhausted. For example, dealing with tens of thousands of instances for something that needs to be processed every frame can be a bottleneck.

This type of situation makes programmers regret they are using a game engine and wish they could go back to a more handcrafted, low-level implementation of game code.

Still, Godot is designed to work around this problem.

> **See also:** You can see how using low-level servers works in action using the [Bullet Shower demo project](https://github.com/godotengine/godot-demo-projects/tree/master/2d/bullet_shower).

### Servers

One of the most interesting design decisions for Godot is the fact that the whole scene system is _optional_. While it is not possible to compile it out, it can be completely bypassed.

At the core, Godot uses the concept of Servers. They are low-level APIs to control rendering, physics, sound, etc. The scene system is built on top of them and uses them directly. The most common servers are:

- [RenderingServer](../godot_csharp_rendering.md): Handles everything related to graphics.
- [PhysicsServer3D](../godot_csharp_physics.md): Handles everything related to 3D physics.
- [PhysicsServer2D](../godot_csharp_physics.md): Handles everything related to 2D physics.
- [AudioServer](../godot_csharp_audio.md): Handles everything related to audio.

Explore their APIs, and you will realize that all the functions provided are low-level implementations of everything Godot allows you to do using nodes.

### RIDs

The key to using servers is understanding Resource ID ([RID](../godot_csharp_math_types.md)) objects. These are opaque handles to the server implementation. They are allocated and freed manually. Almost every function in the servers requires RIDs to access the actual resource.

Most Godot nodes and resources contain these RIDs from the servers internally, and they can be obtained with different functions. In fact, anything that inherits [Resource](../godot_csharp_core.md) can be directly casted to an RID. Not all resources contain an RID, though: in such cases, the RID will be empty. The resource can then be passed to server APIs as an RID.

> **Warning:** Resources are reference-counted (see [RefCounted](../godot_csharp_core.md)), and references to a resource's RID are _not_ counted when determining whether the resource is still in use. Make sure to **keep a reference** to the resource outside the server. Otherwise, both the resource and its RID will be erased.

For nodes, there are many functions available:

- For CanvasItem, the [CanvasItem.get_canvas_item()](../godot_csharp_nodes_2d.md) method will return the canvas item RID in the server.
- For CanvasLayer, the [CanvasLayer.get_canvas()](../godot_csharp_nodes_2d.md) method will return the canvas RID in the server.
- For Viewport, the [Viewport.get_viewport_rid()](../godot_csharp_rendering.md) method will return the viewport RID in the server.
- For 2D, the [World2D](../godot_csharp_misc.md) resource (obtainable in the [Viewport](../godot_csharp_rendering.md) and [CanvasItem](../godot_csharp_nodes_2d.md) nodes) contains functions to get the _RenderingServer Canvas_, and the _PhysicsServer2D Space_. This allows creating 2D objects directly with the server API and using them.
- For 3D, the [World3D](../godot_csharp_misc.md) resource (obtainable in the [Viewport](../godot_csharp_rendering.md) and [Node3D](../godot_csharp_nodes_3d.md) nodes) contains functions to get the _RenderingServer Scenario_, and the _PhysicsServer Space_. This allows creating 3D objects directly with the server API and using them.
- The [VisualInstance3D](../godot_csharp_nodes_3d.md) class, allows getting the scenario _instance_ and _instance base_ via the [VisualInstance3D.get_instance()](../godot_csharp_nodes_3d.md) and [VisualInstance3D.get_base()](../godot_csharp_nodes_3d.md) respectively.

Try exploring the nodes and resources you are familiar with and find the functions to obtain the server _RIDs_.

It is not advised to control RIDs from objects that already have a node associated. Instead, server functions should always be used for creating and controlling new ones and interacting with the existing ones.

### Creating a sprite

This is an example of how to create a sprite from code and move it using the low-level [CanvasItem](../godot_csharp_nodes_2d.md) API.

> **Note:** When creating canvas items using the RenderingServer, you should reset physics interpolation on the first frame using [RenderingServer.canvas_item_reset_physics_interpolation()](../godot_csharp_rendering.md). This ensures proper synchronization between the rendering and physics systems. If this is not done, the canvas item may appear to teleport in when the scene is loaded, rather than appearing directly at its intended location.

```csharp
public partial class MyNode2D : Node2D
{
    // RenderingServer expects references to be kept around.
    private Texture2D _texture;

    public override void _Ready()
    {
        // Create a canvas item, child of this node.
        Rid ciRid = RenderingServer.CanvasItemCreate();
        // Make this node the parent.
        RenderingServer.CanvasItemSetParent(ciRid, GetCanvasItem());
        // Draw a texture on it.
        // Remember to keep this reference.
        _texture = ResourceLoader.Load<Texture2D>("res://my_texture.png");
        // Add it, centered.
        RenderingServer.CanvasItemAddTextureRect(ciRid, new Rect2(-_texture.GetSize() / 2, _texture.GetSize()), _texture.GetRid());
        // Add the item, rotated 45 degrees and translated.
        Transform2D xform = Transfor
// ...
```

The Canvas Item API in the server allows you to add draw primitives to it. Once added, they can't be modified. The Item needs to be cleared and the primitives re-added. This is not the case for setting the transform, which can be done as many times as desired.

Primitives are cleared this way:

```csharp
RenderingServer.CanvasItemClear(ciRid);
```

### Instantiating a Mesh into 3D space

The 3D APIs are different from the 2D ones, so the instantiation API must be used.

```csharp
public partial class MyNode3D : Node3D
{
    // RenderingServer expects references to be kept around.
    private Mesh _mesh;

    public override void _Ready()
    {
        // Create a visual instance (for 3D).
        Rid instance = RenderingServer.InstanceCreate();
        // Set the scenario from the world. This ensures it
        // appears with the same objects as the scene.
        Rid scenario = GetWorld3D().Scenario;
        RenderingServer.InstanceSetScenario(instance, scenario);
        // Add a mesh to it.
        // Remember to keep this reference.
        _mesh = ResourceLoader.Load<Mesh>("res://my_mesh.obj");
        RenderingServer.InstanceSetBase(instance, _mesh.GetRid());
        // Move the mesh around.
        Transform3D xform = new Transform3D(Basis.Identity, new Vec
// ...
```

### Creating a 2D RigidBody and moving a sprite with it

This creates a [RigidBody2D](../godot_csharp_nodes_2d.md) using the [PhysicsServer2D](../godot_csharp_physics.md) API, and moves a [CanvasItem](../godot_csharp_nodes_2d.md) when the body moves.

```csharp
using Godot;

public partial class MyNode2D : Node2D
{
    private Rid _canvasItem;

    private void BodyMoved(PhysicsDirectBodyState2D state, int index)
    {
        // Created your own canvas item; use it here.
        // `ciRid` from the sprite example above needs to be moved to a
        // member variable (instead of within `_Ready()`) so it can be referenced here.
        RenderingServer.CanvasItemSetTransform(_canvasItem, state.Transform);
    }

    public override void _Ready()
    {
        // Create the body.
        var body = PhysicsServer2D.BodyCreate();
        PhysicsServer2D.BodySetMode(body, PhysicsServer2D.BodyMode.Rigid);
        // Add a shape.
        var shape = PhysicsServer2D.RectangleShapeCreate();
        // Set rectangle extents.
        PhysicsServer2D.ShapeS
// ...
```

The 3D version should be very similar, as the 2D and 3D physics servers are identical (using [RigidBody3D](../godot_csharp_nodes_3d.md) and [PhysicsServer3D](../godot_csharp_physics.md) respectively).

### Getting data from the servers

Try to **never** request any information from [RenderingServer](../godot_csharp_rendering.md), [PhysicsServer2D](../godot_csharp_physics.md), or [PhysicsServer3D](../godot_csharp_physics.md) by calling functions unless you know what you are doing. These servers will often run asynchronously for performance and calling any function that returns a value will stall them and force them to process anything pending until the function is actually called. This will severely decrease performance if you call them every frame (and it won't be obvious why).

Because of this, most APIs in such servers are designed so it's not even possible to request information back, until it's actual data that can be saved.

---

## Animating thousands of fish with MultiMeshInstance3D

> **Work in progress:** The content of this page was not yet updated for Godot `4.6` and may be **outdated**. If you know how to improve this page or you can confirm that it's up to date, feel free to [open a pull request](https://github.com/godotengine/godot-docs).

This tutorial explores a technique used in the game [ABZU](https://www.gdcvault.com/play/1024409/Creating-the-Art-of-ABZ) for rendering and animating thousands of fish using vertex animation and static mesh instancing.

In Godot, this can be accomplished with a custom [Shader](../godot_csharp_rendering.md) and a [MultiMeshInstance3D](../godot_csharp_nodes_3d.md). Using the following technique you can render thousands of animated objects, even on low-end hardware.

We will start by animating one fish. Then, we will see how to extend that animation to thousands of fish.

### Animating one Fish

We will start with a single fish. Load your fish model into a [MeshInstance3D](../godot_csharp_nodes_3d.md) and add a new [ShaderMaterial](../godot_csharp_rendering.md).

Here is the fish we will be using for the example images, you can use any fish model you like.

> **Note:** The fish model in this tutorial is made by [QuaterniusDev](https://quaternius.com) and is shared with a creative commons license. CC0 1.0 Universal (CC0 1.0) Public Domain Dedication [https://creativecommons.org/publicdomain/zero/1.0/](https://creativecommons.org/publicdomain/zero/1.0/)

Typically, you would use bones and a [Skeleton3D](../godot_csharp_nodes_3d.md) to animate objects. However, bones are animated on the CPU and so you end having to calculate thousands of operations every frame and it becomes impossible to have thousands of objects. Using vertex animation in a vertex shader, you avoid using bones and can instead calculate the full animation in a few lines of code and completely on the GPU.

The animation will be made of four key motions:

1. A side to side motion
2. A pivot motion around the center of the fish
3. A panning wave motion
4. A panning twist motion

All the code for the animation will be in the vertex shader with uniforms controlling the amount of motion. We use uniforms to control the strength of the motion so that you can tweak the animation in editor and see the results in real time, without the shader having to recompile.

All the motions will be made using cosine waves applied to `VERTEX` in model space. We want the vertices to be in model space so that the motion is always relative to the orientation of the fish. For example, side-to-side will always move the fish back and forth in its left to right direction, instead of on the `x` axis in the world orientation.

In order to control the speed of the animation, we will start by defining our own time variable using `TIME`.

```glsl
//time_scale is a uniform float
float time = TIME * time_scale;
```

The first motion we will implement is the side to side motion. It can be made by offsetting `VERTEX.x` by `cos` of `TIME`. Each time the mesh is rendered, all the vertices will move to the side by the amount of `cos(time)`.

```glsl
//side_to_side is a uniform float
VERTEX.x += cos(time) * side_to_side;
```

The resulting animation should look something like this:

Next, we add the pivot. Because the fish is centered at (0, 0), all we have to do is multiply `VERTEX` by a rotation matrix for it to rotate around the center of the fish.

We construct a rotation matrix like so:

```glsl
//angle is scaled by 0.1 so that the fish only pivots and doesn't rotate all the way around
//pivot is a uniform float
float pivot_angle = cos(time) * 0.1 * pivot;
mat2 rotation_matrix = mat2(vec2(cos(pivot_angle), -sin(pivot_angle)), vec2(sin(pivot_angle), cos(pivot_angle)));
```

And then we apply it in the `x` and `z` axes by multiplying it by `VERTEX.xz`.

```glsl
VERTEX.xz = rotation_matrix * VERTEX.xz;
```

With only the pivot applied you should see something like this:

The next two motions need to pan down the spine of the fish. For that, we need a new variable, `body`. `body` is a float that is `0` at the tail of the fish and `1` at its head.

```glsl
float body = (VERTEX.z + 1.0) / 2.0; //for a fish centered at (0, 0) with a length of 2
```

The next motion is a cosine wave that moves down the length of the fish. To make it move along the spine of the fish, we offset the input to `cos` by the position along the spine, which is the variable we defined above, `body`.

```glsl
//wave is a uniform float
VERTEX.x += cos(time + body) * wave;
```

This looks very similar to the side to side motion we defined above, but in this one, by using `body` to offset `cos` each vertex along the spine has a different position in the wave making it look like a wave is moving along the fish.

The last motion is the twist, which is a panning roll along the spine. Similarly to the pivot, we first construct a rotation matrix.

```glsl
//twist is a uniform float
float twist_angle = cos(time + body) * 0.3 * twist;
mat2 twist_matrix = mat2(vec2(cos(twist_angle), -sin(twist_angle)), vec2(sin(twist_angle), cos(twist_angle)));
```

We apply the rotation in the `xy` axes so that the fish appears to roll around its spine. For this to work, the fish's spine needs to be centered on the `z` axis.

```glsl
VERTEX.xy = twist_matrix * VERTEX.xy;
```

Here is the fish with twist applied:

If we apply all these motions one after another, we get a fluid jelly-like motion.

Normal fish swim mostly with the back half of their body. Accordingly, we need to limit the panning motions to the back half of the fish. To do this, we create a new variable, `mask`.

`mask` is a float that goes from `0` at the front of the fish to `1` at the end using `smoothstep` to control the point at which the transition from `0` to `1` happens.

```glsl
//mask_black and mask_white are uniforms
float mask = smoothstep(mask_black, mask_white, 1.0 - body);
```

Below is an image of the fish with `mask` used as `COLOR`:

For the wave, we multiply the motion by `mask` which will limit it to the back half.

```glsl
//wave motion with mask
VERTEX.x += cos(time + body) * mask * wave;
```

In order to apply the mask to the twist, we use `mix`. `mix` allows us to mix the vertex position between a fully rotated vertex and one that is not rotated. We need to use `mix` instead of multiplying `mask` by the rotated `VERTEX` because we are not adding the motion to the `VERTEX` we are replacing the `VERTEX` with the rotated version. If we multiplied that by `mask`, we would shrink the fish.

```glsl
//twist motion with mask
VERTEX.xy = mix(VERTEX.xy, twist_matrix * VERTEX.xy, mask);
```

Putting the four motions together gives us the final animation.

Go ahead and play with the uniforms in order to alter the swim cycle of the fish. You will find that you can create a wide variety of swim styles using these four motions.

### Making a school of fish

Godot makes it easy to render thousands of the same object using a MultiMeshInstance3D node.

A MultiMeshInstance3D node is created and used the same way you would make a MeshInstance3D node. For this tutorial, we will name the MultiMeshInstance3D node `School`, because it will contain a school of fish.

Once you have a MultiMeshInstance3D add a [MultiMesh](../godot_csharp_rendering.md), and to that MultiMesh add your [Mesh](../godot_csharp_rendering.md) with the shader from above.

MultiMeshes draw your Mesh with three additional per-instance properties: Transform (rotation, translation, scale), Color, and Custom. Custom is used to pass in 4 multi-use variables using a [Color](../godot_csharp_math_types.md).

`instance_count` specifies how many instances of the mesh you want to draw. For now, leave `instance_count` at `0` because you cannot change any of the other parameters while `instance_count` is larger than `0`. We will set `instance count` in GDScript later.

`transform_format` specifies whether the transforms used are 3D or 2D. For this tutorial, select 3D.

For both `color_format` and `custom_data_format` you can choose between `None`, `Byte`, and `Float`. `None` means you won't be passing in that data (either a per-instance `COLOR` variable, or `INSTANCE_CUSTOM`) to the shader. `Byte` means each number making up the color you pass in will be stored with 8 bits while `Float` means each number will be stored in a floating-point number (32 bits). `Float` is slower but more precise, `Byte` will take less memory and be faster, but you may see some visual artifacts.

Now, set `instance_count` to the number of fish you want to have.

Next we need to set the per-instance transforms.

There are two ways to set per-instance transforms for MultiMeshes. The first is entirely in editor and is described in the [MultiMeshInstance3D tutorial](tutorials_3d.md).

The second is to loop over all the instances and set their transforms in code. Below, we use GDScript to loop over all the instances and set their transform to a random position.

Running this script will place the fish in random positions in a box around the position of the MultiMeshInstance3D.

> **Note:** If performance is an issue for you, try running the scene with fewer fish.

Notice how all the fish are all in the same position in their swim cycle? It makes them look very robotic. The next step is to give each fish a different position in the swim cycle so the entire school looks more organic.

### Animating a school of fish

One of the benefits of animating the fish using `cos` functions is that they are animated with one parameter, `time`. In order to give each fish a unique position in the swim cycle, we only need to offset `time`.

We do that by adding the per-instance custom value `INSTANCE_CUSTOM` to `time`.

```glsl
float time = (TIME * time_scale) + (6.28318 * INSTANCE_CUSTOM.x);
```

Next, we need to pass a value into `INSTANCE_CUSTOM`. We do that by adding one line into the `for` loop from above. In the `for` loop we assign each instance a set of four random floats to use.

Now the fish all have unique positions in the swim cycle. You can give them a little more individuality by using `INSTANCE_CUSTOM` to make them swim faster or slower by multiplying by `TIME`.

```glsl
//set speed from 50% - 150% of regular speed
float time = (TIME * (0.5 + INSTANCE_CUSTOM.y) * time_scale) + (6.28318 * INSTANCE_CUSTOM.x);
```

You can even experiment with changing the per-instance color the same way you changed the per-instance custom value.

One problem that you will run into at this point is that the fish are animated, but they are not moving. You can move them by updating the per-instance transform for each fish every frame. Although doing so will be faster than moving thousands of MeshInstance3Ds per frame, it'll still likely be slow.

In the next tutorial we will cover how to use [GPUParticles3D](../godot_csharp_misc.md) to take advantage of the GPU and move each fish around individually while still receiving the benefits of instancing.

---

## Controlling thousands of fish with Particles

> **Work in progress:** The content of this page was not yet updated for Godot `4.6` and may be **outdated**. If you know how to improve this page or you can confirm that it's up to date, feel free to [open a pull request](https://github.com/godotengine/godot-docs).

The problem with [MeshInstance3D](../godot_csharp_nodes_3d.md) is that it is expensive to update their transform array. It is great for placing many static objects around the scene. But it is still difficult to move the objects around the scene.

To make each instance move in an interesting way, we will use a [GPUParticles3D](../godot_csharp_misc.md) node. Particles take advantage of GPU acceleration by computing and setting the per-instance information in a [Shader](../godot_csharp_rendering.md).

First create a Particles node. Then, under "Draw Passes" set the Particle's "Draw Pass 1" to your [Mesh](../godot_csharp_rendering.md). Then under "Process Material" create a new [ShaderMaterial](../godot_csharp_rendering.md).

Set the `shader_type` to `particles`.

```glsl
shader_type particles
```

Then add the following two functions:

```glsl
float rand_from_seed(in uint seed) {
  int k;
  int s = int(seed);
  if (s == 0)
    s = 305420679;
  k = s / 127773;
  s = 16807 * (s - k * 127773) - 2836 * k;
  if (s < 0)
    s += 2147483647;
  seed = uint(s);
  return float(seed % uint(65536)) / 65535.0;
}

uint hash(uint x) {
  x = ((x >> uint(16)) ^ x) * uint(73244475);
  x = ((x >> uint(16)) ^ x) * uint(73244475);
  x = (x >> uint(16)) ^ x;
  return x;
}
```

These functions come from the default [ParticleProcessMaterial](../godot_csharp_rendering.md). They are used to generate a random number from each particle's `RANDOM_SEED`.

A unique thing about particle shaders is that some built-in variables are saved across frames. `TRANSFORM`, `COLOR`, and `CUSTOM` can all be accessed in the shader of the mesh, and also in the particle shader the next time it is run.

Next, setup your `start()` function. Particles shaders contain a `start()` function and a `process()` function.

The code in the `start()` function only runs when the particle system starts. The code in the `process()` function will always run.

We need to generate 4 random numbers: 3 to create a random position and one for the random offset of the swim cycle.

First, generate 4 seeds inside the `start()` function using the `hash()` function provided above:

```glsl
uint alt_seed1 = hash(NUMBER + uint(1) + RANDOM_SEED);
uint alt_seed2 = hash(NUMBER + uint(27) + RANDOM_SEED);
uint alt_seed3 = hash(NUMBER + uint(43) + RANDOM_SEED);
uint alt_seed4 = hash(NUMBER + uint(111) + RANDOM_SEED);
```

Then, use those seeds to generate random numbers using `rand_from_seed`:

```glsl
CUSTOM.x = rand_from_seed(alt_seed1);
vec3 position = vec3(rand_from_seed(alt_seed2) * 2.0 - 1.0,
                     rand_from_seed(alt_seed3) * 2.0 - 1.0,
                     rand_from_seed(alt_seed4) * 2.0 - 1.0);
```

Finally, assign `position` to `TRANSFORM[3].xyz`, which is the part of the transform that holds the position information.

```glsl
TRANSFORM[3].xyz = position * 20.0;
```

Remember, all this code so far goes inside the `start()` function.

The vertex shader for your mesh can stay the exact same as it was in the previous tutorial.

Now you can move each fish individually each frame, either by adding to the `TRANSFORM` directly or by writing to `VELOCITY`.

Let's transform the fish by setting their `VELOCITY` in the `start()` function.

```glsl
VELOCITY.z = 10.0;
```

This is the most basic way to set `VELOCITY` every particle (or fish) will have the same velocity.

Just by setting `VELOCITY` you can make the fish swim however you want. For example, try the code below.

```glsl
VELOCITY.z = cos(TIME + CUSTOM.x * 6.28) * 4.0 + 6.0;
```

This will give each fish a unique speed between `2` and `10`.

You can also let each fish change its velocity over time if you set the velocity in the `process()` function.

If you used `CUSTOM.y` in the last tutorial, you can also set the speed of the swim animation based on the `VELOCITY`. Just use `CUSTOM.y`.

```glsl
CUSTOM.y = VELOCITY.z * 0.1;
```

This code gives you the following behavior:

Using a ParticleProcessMaterial you can make the fish behavior as simple or complex as you like. In this tutorial we only set Velocity, but in your own Shaders you can also set `COLOR`, rotation, scale (through `TRANSFORM`). Please refer to the [Particles Shader Reference](tutorials_shaders.md) for more information on particle shaders.

---
