# Godot 4 C# Tutorials — Performance (Part 1)

> 4 tutorials. C#-specific code examples.

## CPU optimization

### Measuring performance

We have to know where the "bottlenecks" are to know how to speed up our program. Bottlenecks are the slowest parts of the program that limit the rate that everything can progress. Focusing on bottlenecks allows us to concentrate our efforts on optimizing the areas which will give us the greatest speed improvement, instead of spending a lot of time optimizing functions that will lead to small performance improvements.

For the CPU, the easiest way to identify bottlenecks is to use a profiler.

### CPU profilers

Profilers run alongside your program and take timing measurements to work out what proportion of time is spent in each function.

The Godot IDE conveniently has a built-in profiler. It does not run every time you start your project: it must be manually started and stopped. This is because, like most profilers, recording these timing measurements can slow down your project significantly.

After profiling, you can look back at the results for a frame.

> **Note:** We can see the cost of built-in processes such as physics and audio, as well as seeing the cost of our own scripting functions at the bottom. Time spent waiting for various built-in servers may not be counted in the profilers. This is a known bug.

When a project is running slowly, you will often see an obvious function or process taking a lot more time than others. This is your primary bottleneck, and you can usually increase speed by optimizing this area.

For more info about using Godot's built-in profiler, see [Debugger panel](tutorials_scripting.md).

### External profilers

Although the Godot IDE profiler is very convenient and useful, sometimes you need more power, and the ability to profile the Godot engine source code itself.

You can use a number of third-party C++ profilers to do this.

From the left, Callgrind is listing the percentage of time within a function and its children (Inclusive), the percentage of time spent within the function itself, excluding child functions (Self), the number of times the function is called, the function name, and the file or module.

In this example, we can see nearly all time is spent under the `Main::iteration()` function. This is the master function in the Godot source code that is called repeatedly. It causes frames to be drawn, physics ticks to be simulated, and nodes and scripts to be updated. A large proportion of the time is spent in the functions to render a canvas (66%), because this example uses a 2D benchmark. Below this, we see that almost 50% of the time is spent outside Godot code in `libglapi` and `i965_dri` (the graphics driver). This tells us the a large proportion of CPU time is being spent in the graphics driver.

This is actually an excellent example because, in an ideal world, only a very small proportion of time would be spent in the graphics driver. This is an indication that there is a problem with too much communication and work being done in the graphics API. This specific profiling led to the development of 2D batching, which greatly speeds up 2D rendering by reducing bottlenecks in this area.

### Manually timing functions

Another handy technique, especially once you have identified the bottleneck using a profiler, is to manually time the function or area under test. The specifics vary depending on the language, but in GDScript, you would do the following:

```csharp
var timeStart = Time.GetTicksUsec();

// Your function you want to time.
UpdateEnemies();

var timeEnd = Time.GetTicksUsec();
GD.Print($"UpdateEnemies() took {timeEnd - timeStart} microseconds");
```

When manually timing functions, it is usually a good idea to run the function many times (1,000 or more times), instead of just once (unless it is a very slow function). The reason for doing this is that timers often have limited accuracy. Moreover, CPUs will schedule processes in a haphazard manner. Therefore, an average over a series of runs is more accurate than a single measurement.

As you attempt to optimize functions, be sure to either repeatedly profile or time them as you go. This will give you crucial feedback as to whether the optimization is working (or not).

### Caches

CPU caches are something else to be particularly aware of, especially when comparing timing results of two different versions of a function. The results can be highly dependent on whether the data is in the CPU cache or not. CPUs don't load data directly from the system RAM, even though it's huge in comparison to the CPU cache (several gigabytes instead of a few megabytes). This is because system RAM is very slow to access. Instead, CPUs load data from a smaller, faster bank of memory called cache. Loading data from cache is very fast, but every time you try and load a memory address that is not stored in cache, the cache must make a trip to main memory and slowly load in some data. This delay can result in the CPU sitting around idle for a long time, and is referred to as a "cache miss".

This means that the first time you run a function, it may run slowly because the data is not in the CPU cache. The second and later times, it may run much faster because the data is in the cache. Due to this, always use averages when timing, and be aware of the effects of cache.

Understanding caching is also crucial to CPU optimization. If you have an algorithm (routine) that loads small bits of data from randomly spread out areas of main memory, this can result in a lot of cache misses, a lot of the time, the CPU will be waiting around for data instead of doing any work. Instead, if you can make your data accesses localised, or even better, access memory in a linear fashion (like a continuous list), then the cache will work optimally and the CPU will be able to work as fast as possible.

Godot usually takes care of such low-level details for you. For example, the Server APIs make sure data is optimized for caching already for things like rendering and physics. Still, you should be especially aware of caching when writing GDExtensions.

### Languages

Godot supports a number of different languages, and it is worth bearing in mind that there are trade-offs involved. Some languages are designed for ease of use at the cost of speed, and others are faster but more difficult to work with.

Built-in engine functions run at the same speed regardless of the scripting language you choose. If your project is making a lot of calculations in its own code, consider moving those calculations to a faster language.

#### GDScript

[GDScript](tutorials_scripting.md) is designed to be easy to use and iterate, and is ideal for making many types of games. However, in this language, ease of use is considered more important than performance. If you need to make heavy calculations, consider moving some of your project to one of the other languages.

#### C#

[C#](tutorials_scripting.md) is popular and has first-class support in Godot. It offers a good compromise between speed and ease of use. Beware of possible garbage collection pauses and leaks that can occur during gameplay, though. A common approach to workaround issues with garbage collection is to use _object pooling_, which is outside the scope of this guide.

#### Other languages

Third parties provide support for several other languages, including [Rust](https://github.com/godot-rust/gdext).

#### C++

Godot is written in C++. Using C++ will usually result in the fastest code. However, on a practical level, it is the most difficult to deploy to end users' machines on different platforms. Options for using C++ include GDExtensions and custom modules.

### Threads

Consider using threads when making a lot of calculations that can run in parallel to each other. Modern CPUs have multiple cores, each one capable of doing a limited amount of work. By spreading work over multiple threads, you can move further towards peak CPU efficiency.

The disadvantage of threads is that you have to be incredibly careful. As each CPU core operates independently, they can end up trying to access the same memory at the same time. One thread can be reading to a variable while another is writing: this is called a _race condition_. Before you use threads, make sure you understand the dangers and how to try and prevent these race conditions. Threads can make debugging considerably more difficult.

For more information on threads, see Using multiple threads.

### SceneTree

Although Nodes are an incredibly powerful and versatile concept, be aware that every node has a cost. Built-in functions such as `_process()` and `_physics_process()` propagate through the tree. This housekeeping can reduce performance when you have a very large numbers of nodes (how many exactly depends on the target platform and can range from thousands to tens of thousands so ensure that you profile performance on all target platforms during development).

Each node is handled individually in the Godot renderer. Therefore, a smaller number of nodes with more in each can lead to better performance.

One quirk of the [SceneTree](../godot_csharp_core.md) is that you can sometimes get much better performance by removing nodes from the SceneTree, rather than by pausing or hiding them. You don't have to delete a detached node. You can for example, keep a reference to a node, detach it from the scene tree using [Node.remove_child(node)](../godot_csharp_misc.md), then reattach it later using [Node.add_child(node)](../godot_csharp_misc.md). This can be very useful for adding and removing areas from a game, for example.

You can avoid the SceneTree altogether by using Server APIs. For more information, see Optimization using Servers.

### Physics

In some situations, physics can end up becoming a bottleneck. This is particularly the case with complex worlds and large numbers of physics objects.

Here are some techniques to speed up physics:

- Try using simplified versions of your rendered geometry for collision shapes. Often, this won't be noticeable for end users, but can greatly increase performance.
- Try removing objects from physics when they are out of view / outside the current area, or reusing physics objects (maybe you allow 8 monsters per area, for example, and reuse these).

Another crucial aspect to physics is the physics tick rate. In some games, you can greatly reduce the tick rate, and instead of for example, updating physics 60 times per second, you may update them only 30 or even 20 times per second. This can greatly reduce the CPU load.

The downside of changing physics tick rate is you can get jerky movement or jitter when the physics update rate does not match the frames per second rendered. Also, decreasing the physics tick rate will increase input lag. It's recommended to stick to the default physics tick rate (60 Hz) in most games that feature real-time player movement.

The solution to jitter is to use _fixed timestep interpolation_, which involves smoothing the rendered positions and rotations over multiple frames to match the physics. Godot has built-in physics interpolation which you can read about [here](tutorials_physics.md). Performance-wise, interpolation is a very cheap operation compared to running a physics tick. It's orders of magnitude faster, so this can be a significant performance win while also reducing jitter.

---

## General optimization tips

### Introduction

In an ideal world, computers would run at infinite speed. The only limit to what we could achieve would be our imagination. However, in the real world, it's all too easy to produce software that will bring even the fastest computer to its knees.

Thus, designing games and other software is a compromise between what we would like to be possible, and what we can realistically achieve while maintaining good performance.

To achieve the best results, we have two approaches:

- Work faster.
- Work smarter.

And preferably, we will use a blend of the two.

#### Smoke and mirrors

Part of working smarter is recognizing that, in games, we can often get the player to believe they're in a world that is far more complex, interactive, and graphically exciting than it really is. A good programmer is a magician, and should strive to learn the tricks of the trade while trying to invent new ones.

#### The nature of slowness

To the outside observer, performance problems are often lumped together. But in reality, there are several different kinds of performance problems:

- A slow process that occurs every frame, leading to a continuously low frame rate.
- An intermittent process that causes "spikes" of slowness, leading to stalls.
- A slow process that occurs outside of normal gameplay, for instance, when loading a level.

Each of these are annoying to the user, but in different ways.

### Measuring performance

Probably the most important tool for optimization is the ability to measure performance - to identify where bottlenecks are, and to measure the success of our attempts to speed them up.

There are several methods of measuring performance, including:

- Putting a start/stop timer around code of interest.
- Using the [Godot profiler](tutorials_scripting.md).
- Using external CPU profilers.
- Using external GPU profilers/debuggers such as [NVIDIA Nsight Graphics](https://developer.nvidia.com/nsight-graphics), [Radeon GPU Profiler](https://gpuopen.com/rgp/), [PIX](https://devblogs.microsoft.com/pix/download/) (Direct3D 12 only), [Xcode](https://developer.apple.com/documentation/xcode/optimizing-gpu-performance) (Metal only), or [Arm Performance Studio](https://developer.arm.com/Tools%20and%20Software/Arm%20Performance%20Studio).
- Checking the frame rate (with V-Sync disabled). Third-party utilities such as [RivaTuner Statistics Server](https://www.guru3d.com/files-details/rtss-rivatuner-statistics-server-download.html) (Windows), [Special K](https://www.special-k.info/) (Windows), or [MangoHud](https://github.com/flightlessmango/MangoHud) (Linux) can also be useful here.
- Using an unofficial [debug menu add-on](https://github.com/godot-extended-libraries/godot-debug-menu).

Be very aware that the relative performance of different areas can vary on different hardware. It's often a good idea to measure timings on more than one device. This is especially the case if you're targeting mobile devices.

#### Limitations

CPU profilers are often the go-to method for measuring performance. However, they don't always tell the whole story.

- Bottlenecks are often on the GPU, "as a result" of instructions given by the CPU.
- Spikes can occur in the operating system processes (outside of Godot) "as a result" of instructions used in Godot (for example, dynamic memory allocation).
- You may not always be able to profile specific devices like a mobile phone due to the initial setup required.
- You may have to solve performance problems that occur on hardware you don't have access to.

As a result of these limitations, you often need to use detective work to find out where bottlenecks are.

### Detective work

Detective work is a crucial skill for developers (both in terms of performance, and also in terms of bug fixing). This can include hypothesis testing, and binary search.

#### Hypothesis testing

Say, for example, that you believe sprites are slowing down your game. You can test this hypothesis by:

- Measuring the performance when you add more sprites, or take some away.

This may lead to a further hypothesis: does the size of the sprite determine the performance drop?

- You can test this by keeping everything the same, but changing the sprite size, and measuring performance.

#### Binary search

If you know that frames are taking much longer than they should, but you're not sure where the bottleneck lies. You could begin by commenting out approximately half the routines that occur on a normal frame. Has the performance improved more or less than expected?

Once you know which of the two halves contains the bottleneck, you can repeat this process until you've pinned down the problematic area.

### Profilers

Profilers allow you to time your program while running it. Profilers then provide results telling you what percentage of time was spent in different functions and areas, and how often functions were called.

This can be very useful both to identify bottlenecks and to measure the results of your improvements. Sometimes, attempts to improve performance can backfire and lead to slower performance. **Always use profiling and timing to guide your efforts.**

For more info about using Godot's built-in profiler, see [The Profiler](tutorials_scripting.md).

### Principles

[Donald Knuth](https://en.wikipedia.org/wiki/Donald_Knuth) said:

_Programmers waste enormous amounts of time thinking about, or worrying about, the speed of noncritical parts of their programs, and these attempts at efficiency actually have a strong negative impact when debugging and maintenance are considered. We should forget about small efficiencies, say about 97% of the time: premature optimization is the root of all evil. Yet we should not pass up our opportunities in that critical 3%._

The messages are very important:

- Developer time is limited. Instead of blindly trying to speed up all aspects of a program, we should concentrate our efforts on the aspects that really matter.
- Efforts at optimization often end up with code that is harder to read and debug than non-optimized code. It is in our interests to limit this to areas that will really benefit.

Just because we _can_ optimize a particular bit of code, it doesn't necessarily mean that we _should_. Knowing when and when not to optimize is a great skill to develop.

One misleading aspect of the quote is that people tend to focus on the subquote _"premature optimization is the root of all evil"_. While _premature_ optimization is (by definition) undesirable, performant software is the result of performant design.

#### Performant design

The danger with encouraging people to ignore optimization until necessary, is that it conveniently ignores that the most important time to consider performance is at the design stage, before a key has even hit a keyboard. If the design or algorithms of a program are inefficient, then no amount of polishing the details later will make it run fast. It may run _faster_, but it will never run as fast as a program designed for performance.

This tends to be far more important in game or graphics programming than in general programming. A performant design, even without low-level optimization, will often run many times faster than a mediocre design with low-level optimization.

#### Incremental design

Of course, in practice, unless you have prior knowledge, you are unlikely to come up with the best design the first time. Instead, you'll often make a series of versions of a particular area of code, each taking a different approach to the problem, until you come to a satisfactory solution. It's important not to spend too much time on the details at this stage until you have finalized the overall design. Otherwise, much of your work will be thrown out.

It's difficult to give general guidelines for performant design because this is so dependent on the problem. One point worth mentioning though, on the CPU side, is that modern CPUs are nearly always limited by memory bandwidth. This has led to a resurgence in data-oriented design, which involves designing data structures and algorithms for _cache locality_ of data and linear access, rather than jumping around in memory.

#### The optimization process

Assuming we have a reasonable design, and taking our lessons from Knuth, our first step in optimization should be to identify the biggest bottlenecks - the slowest functions, the low-hanging fruit.

Once we've successfully improved the speed of the slowest area, it may no longer be the bottleneck. So we should test/profile again and find the next bottleneck on which to focus.

The process is thus:

1. Profile / Identify bottleneck.
2. Optimize bottleneck.
3. Return to step 1.

#### Optimizing bottlenecks

Some profilers will even tell you which part of a function (which data accesses, calculations) are slowing things down.

As with design, you should concentrate your efforts first on making sure the algorithms and data structures are the best they can be. Data access should be local (to make best use of CPU cache), and it can often be better to use compact storage of data (again, always profile to test results). Often, you precalculate heavy computations ahead of time. This can be done by performing the computation when loading a level, by loading a file containing precalculated data, or by storing the results of complex calculations into a script constant and reading its value.

Once algorithms and data are good, you can often make small changes in routines which improve performance. For instance, you can move some calculations outside of loops or transform nested `for` loops into non-nested loops. (This should be feasible if you know a 2D array's width or height in advance.)

Always retest your timing/bottlenecks after making each change. Some changes will increase speed, others may have a negative effect. Sometimes, a small positive effect will be outweighed by the negatives of more complex code, and you may choose to leave out that optimization.

### Appendix

#### Bottleneck math

The proverb _"a chain is only as strong as its weakest link"_ applies directly to performance optimization. If your project is spending 90% of the time in function `A`, then optimizing `A` can have a massive effect on performance.

```none
A: 9 ms
Everything else: 1 ms
Total frame time: 10 ms
```

```none
A: 1 ms
Everything else: 1ms
Total frame time: 2 ms
```

In this example, improving this bottleneck `A` by a factor of 9× decreases overall frame time by 5× while increasing frames per second by 5×.

However, if something else is running slowly and also bottlenecking your project, then the same improvement can lead to less dramatic gains:

```none
A: 9 ms
Everything else: 50 ms
Total frame time: 59 ms
```

```none
A: 1 ms
Everything else: 50 ms
Total frame time: 51 ms
```

In this example, even though we have hugely optimized function `A`, the actual gain in terms of frame rate is quite small.

In games, things become even more complicated because the CPU and GPU run independently of one another. Your total frame time is determined by the slower of the two.

```none
CPU: 9 ms
GPU: 50 ms
Total frame time: 50 ms
```

```none
CPU: 1 ms
GPU: 50 ms
Total frame time: 50 ms
```

In this example, we optimized the CPU hugely again, but the frame time didn't improve because we are GPU-bottlenecked.

---

## GPU optimization

### Introduction

The demand for new graphics features and progress almost guarantees that you will encounter graphics bottlenecks. Some of these can be on the CPU side, for instance in calculations inside the Godot engine to prepare objects for rendering. Bottlenecks can also occur on the CPU in the graphics driver, which sorts instructions to pass to the GPU, and in the transfer of these instructions. And finally, bottlenecks also occur on the GPU itself.

Where bottlenecks occur in rendering is highly hardware-specific. Mobile GPUs in particular may struggle with scenes that run easily on desktop.

Understanding and investigating GPU bottlenecks is slightly different to the situation on the CPU. This is because, often, you can only change performance indirectly by changing the instructions you give to the GPU. Also, it may be more difficult to take measurements. In many cases, the only way of measuring performance is by examining changes in the time spent rendering each frame.

### Draw calls, state changes, and APIs

> **Note:** The following section is not relevant to end-users, but is useful to provide background information that is relevant in later sections.

Godot sends instructions to the GPU via a graphics API (Vulkan, OpenGL, OpenGL ES or WebGL). The communication and driver activity involved can be quite costly, especially in OpenGL, OpenGL ES and WebGL. If we can provide these instructions in a way that is preferred by the driver and GPU, we can greatly increase performance.

Nearly every API command in OpenGL requires a certain amount of validation to make sure the GPU is in the correct state. Even seemingly simple commands can lead to a flurry of behind-the-scenes housekeeping. Therefore, the goal is to reduce these instructions to a bare minimum and group together similar objects as much as possible so they can be rendered together, or with the minimum number of these expensive state changes.

#### 2D batching

In 2D, the costs of treating each item individually can be prohibitively high - there can easily be thousands of them on the screen. This is why 2D _batching_ is used. Multiple similar items are grouped together and rendered in a batch, via a single draw call, rather than making a separate draw call for each item. In addition, this means state changes, material and texture changes can be kept to a minimum.

#### 3D batching

In 3D, we still aim to minimize draw calls and state changes. However, it can be more difficult to batch together several objects into a single draw call. 3D meshes tend to comprise hundreds or thousands of triangles, and combining large meshes in real-time is prohibitively expensive. The costs of joining them quickly exceeds any benefits as the number of triangles grows per mesh. A much better alternative is to **join meshes ahead of time** (static meshes in relation to each other). This can be done by artists, or programmatically within Godot using an add-on.

There is also a cost to batching together objects in 3D. Several objects rendered as one cannot be individually culled. An entire city that is off-screen will still be rendered if it is joined to a single blade of grass that is on screen. Thus, you should always take objects' locations and culling into account when attempting to batch 3D objects together. Despite this, the benefits of joining static objects often outweigh other considerations, especially for large numbers of distant or low-poly objects.

For more information on 3D specific optimizations, see Optimizing 3D performance.

#### Reuse shaders and materials

The Godot renderer is a little different to what is out there. It's designed to minimize GPU state changes as much as possible. [StandardMaterial3D](../godot_csharp_rendering.md) does a good job at reusing materials that need similar shaders. If custom shaders are used, make sure to reuse them as much as possible. Godot's priorities are:

- **Reusing Materials:** The fewer different materials in the scene, the faster the rendering will be. If a scene has a huge amount of objects (in the hundreds or thousands), try reusing the materials. In the worst case, use atlases to decrease the amount of texture changes.
- **Reusing Shaders:** If materials can't be reused, at least try to reuse shaders. Note: shaders are automatically reused between StandardMaterial3Ds that share the same configuration (features that are enabled or disabled with a check box) even if they have different parameters.

If a scene has, for example, 20,000 objects with 20,000 different materials each, rendering will be slow. If the same scene has 20,000 objects, but only uses 100 materials, rendering will be much faster.

### Pixel cost versus vertex cost

You may have heard that the lower the number of polygons in a model, the faster it will be rendered. This is _really_ relative and depends on many factors.

On a modern PC and console, vertex cost is low. GPUs originally only rendered triangles. This meant that every frame:

1. All vertices had to be transformed by the CPU (including clipping).
2. All vertices had to be sent to the GPU memory from the main RAM.

Nowadays, all this is handled inside the GPU, greatly increasing performance. 3D artists usually have the wrong feeling about polycount performance because 3D modeling software (such as Blender, 3ds Max, etc.) need to keep geometry in CPU memory for it to be edited, reducing actual performance. Game engines rely on the GPU more, so they can render many triangles much more efficiently.

On mobile devices, the story is different. PC and console GPUs are brute-force monsters that can pull as much electricity as they need from the power grid. Mobile GPUs are limited to a tiny battery, so they need to be a lot more power efficient.

To be more efficient, mobile GPUs attempt to avoid _overdraw_. Overdraw occurs when the same pixel on the screen is being rendered more than once. Imagine a town with several buildings. GPUs don't know what is visible and what is hidden until they draw it. For example, a house might be drawn and then another house in front of it (which means rendering happened twice for the same pixel). PC GPUs normally don't care much about this and just throw more pixel processors to the hardware to increase performance (which also increases power consumption).

Using more power is not an option on mobile so mobile devices use a technique called _tile-based rendering_ which divides the screen into a grid. Each cell keeps the list of triangles drawn to it and sorts them by depth to minimize _overdraw_. This technique improves performance and reduces power consumption, but takes a toll on vertex performance. As a result, fewer vertices and triangles can be processed for drawing.

Additionally, tile-based rendering struggles when there are small objects with a lot of geometry within a small portion of the screen. This forces mobile GPUs to put a lot of strain on a single screen tile, which considerably decreases performance as all the other cells must wait for it to complete before displaying the frame.

To summarize, don't worry about vertex count on mobile, but **avoid concentration of vertices in small parts of the screen**. If a character, NPC, vehicle, etc. is far away (which means it looks tiny), use a smaller level of detail (LOD) model. Even on desktop GPUs, it's preferable to avoid having triangles smaller than the size of a pixel on screen.

Pay attention to the additional vertex processing required when using:

- Skinning (skeletal animation)
- Morphs (shape keys)
- Vertex-lit objects (common on mobile)

### Pixel/fragment shaders and fill rate

In contrast to vertex processing, the costs of fragment (per-pixel) shading have increased dramatically over the years. Screen resolutions have increased: the area of a 4K screen is 8,294,400 pixels, versus 307,200 for an old 640×480 VGA screen. That is 27 times the area! Also, the complexity of fragment shaders has exploded. Physically-based rendering requires complex calculations for each fragment.

You can test whether a project is fill rate-limited quite easily. Turn off V-Sync to prevent capping the frames per second, then compare the frames per second when running with a large window, to running with a very small window. You may also benefit from similarly reducing your shadow map size if using shadows. Usually, you will find the FPS increases quite a bit using a small window, which indicates you are to some extent fill rate-limited. On the other hand, if there is little to no increase in FPS, then your bottleneck lies elsewhere.

You can increase performance in a fill rate-limited project by reducing the amount of work the GPU has to do. You can do this by simplifying the shader (perhaps turn off expensive options if you are using a [StandardMaterial3D](../godot_csharp_rendering.md)), or reducing the number and size of textures used. Also, when using non-unshaded particles, consider forcing vertex shading in their material to decrease the shading cost.

> **See also:** On supported hardware, [Variable rate shading](tutorials_3d.md) can be used to reduce shading processing costs without impacting the sharpness of edges on the final image.

**When targeting mobile devices, consider using the simplest possible shaders you can reasonably afford to use.**

#### Reading textures

The other factor in fragment shaders is the cost of reading textures. Reading textures is an expensive operation, especially when reading from several textures in a single fragment shader. Also, consider that filtering may slow it down further (trilinear filtering between mipmaps, and averaging). Reading textures is also expensive in terms of power usage, which is a big issue on mobiles.

**If you use third-party shaders or write your own shaders, try to use algorithms that require as few texture reads as possible.**

#### Texture compression

By default, Godot compresses textures of 3D models when imported using video RAM (VRAM) compression. Video RAM compression isn't as efficient in size as PNG or JPG when stored, but increases performance enormously when drawing large enough textures.

This is because the main goal of texture compression is bandwidth reduction between memory and the GPU.

In 3D, the shapes of objects depend more on the geometry than the texture, so compression is generally not noticeable. In 2D, compression depends more on shapes inside the textures, so the artifacts resulting from 2D compression are more noticeable.

As a warning, most Android devices do not support texture compression of textures with transparency (only opaque), so keep this in mind.

> **Note:** Even in 3D, "pixel art" textures should have VRAM compression disabled as it will negatively affect their appearance, without improving performance significantly due to their low resolution.

#### Post-processing and shadows

Post-processing effects and shadows can also be expensive in terms of fragment shading activity. Always test the impact of these on different hardware.

**Reducing the size of shadowmaps can increase performance**, both in terms of writing and reading the shadowmaps. On top of that, the best way to improve performance of shadows is to turn shadows off for as many lights and objects as possible. Smaller or distant OmniLights/SpotLights can often have their shadows disabled with only a small visual impact.

### Transparency and blending

Transparent objects present particular problems for rendering efficiency. Opaque objects (especially in 3D) can be essentially rendered in any order and the Z-buffer will ensure that only the front most objects get shaded. Transparent or blended objects are different. In most cases, they cannot rely on the Z-buffer and must be rendered in "painter's order" (i.e. from back to front) to look correct.

Transparent objects are also particularly bad for fill rate, because every item has to be drawn even if other transparent objects will be drawn on top later on.

Opaque objects don't have to do this. They can usually take advantage of the Z-buffer by writing to the Z-buffer only first, then only performing the fragment shader on the "winning" fragment, the object that is at the front at a particular pixel.

Transparency is particularly expensive where multiple transparent objects overlap. It is usually better to use transparent areas as small as possible to minimize these fill rate requirements, especially on mobile, where fill rate is very expensive. Indeed, in many situations, rendering more complex opaque geometry can end up being faster than using transparency to "cheat".

### Multi-platform advice

If you are aiming to release on multiple platforms, test _early_ and test _often_ on all your platforms, especially mobile. Developing a game on desktop but attempting to port it to mobile at the last minute is a recipe for disaster.

In general, you should design your game for the lowest common denominator, then add optional enhancements for more powerful platforms. For example, you may want to use the Compatibility rendering method for both desktop and mobile platforms where you target both.

### Mobile/tiled renderers

As described above, GPUs on mobile devices work in dramatically different ways from GPUs on desktop. Most mobile devices use tile renderers. Tile renderers split up the screen into regular-sized tiles that fit into super fast cache memory, which reduces the number of read/write operations to the main memory.

There are some downsides though. Tiled rendering can make certain techniques much more complicated and expensive to perform. Tiles that rely on the results of rendering in different tiles or on the results of earlier operations being preserved can be very slow. Be very careful to test the performance of shaders, viewport textures and post processing.

---

## Optimizing 3D performance

### Culling

Godot will automatically perform view frustum culling in order to prevent rendering objects that are outside the viewport. This works well for games that take place in a small area, however things can quickly become problematic in larger levels.

#### Occlusion culling

Walking around a town for example, you may only be able to see a few buildings in the street you are in, as well as the sky and a few birds flying overhead. As far as a naive renderer is concerned however, you can still see the entire town. It won't just render the buildings in front of you, it will render the street behind that, with the people on that street, the buildings behind that. You quickly end up in situations where you are attempting to render 10× or 100× more than what is visible.

Things aren't quite as bad as they seem, because the Z-buffer usually allows the GPU to only fully shade the objects that are at the front. This is called _depth prepass_ and is enabled by default in Godot when using the Forward+ or Compatibility rendering methods. However, unneeded objects are still reducing performance.

One way we can potentially reduce the amount to be rendered is to **take advantage of occlusion**. Godot offers an approach to occlusion culling using occluder nodes. See [Occlusion culling](tutorials_3d.md) for instructions on setting up occlusion culling in your scene.

> **Note:** In some cases, you may have to adapt your level design to add more occlusion opportunities. For example, you may have to add more walls to prevent the player from seeing too far away, which would decrease performance due to the lost opportunities for occlusion culling.

### Transparent objects

Godot sorts objects by [Material](../godot_csharp_rendering.md) and [Shader](../godot_csharp_rendering.md) to improve performance. This, however, can not be done with transparent objects. Transparent objects are rendered from back to front to make blending with what is behind work. As a result, **try to use as few transparent objects as possible**. If an object has a small section with transparency, try to make that section a separate surface with its own material.

For more information, see the GPU optimizations doc.

### Level of detail (LOD)

In some situations, particularly at a distance, it can be a good idea to **replace complex geometry with simpler versions**. The end user will probably not be able to see much difference. Consider looking at a large number of trees in the far distance. There are several strategies for replacing models at varying distance. You could use lower poly models, or use transparency to simulate more complex geometry.

Godot 4 offers several ways to control level of detail:

- An automatic approach on mesh import using [Mesh level of detail (LOD)](tutorials_3d.md).
- A manual approach configured in the 3D node using [Visibility ranges (HLOD)](tutorials_3d.md).
- [Decals](tutorials_3d.md) and [lights](tutorials_3d.md) can also benefit from level of detail using their respective **Distance Fade** properties.

While they can be used independently, these approaches are most effective when used together. For example, you can set up visibility ranges to hide particle effects that are too far away from the player to notice. At the same time, you can rely on mesh LOD to make the particle effect's meshes rendered with less detail at a distance.

Visibility ranges are also a good way to set up _impostors_ for distant geometry (see below).

#### Billboards and imposters

The simplest version of using transparency to deal with LOD is billboards. For example, you can use a single transparent quad to represent a tree at distance. This can be very cheap to render, unless of course, there are many trees in front of each other. In this case, transparency may start eating into fill rate (for more information on fill rate, see GPU optimization).

An alternative is to render not just one tree, but a number of trees together as a group. This can be especially effective if you can see an area but cannot physically approach it in a game.

You can make imposters by pre-rendering views of an object at different angles. Or you can even go one step further, and periodically re-render a view of an object onto a texture to be used as an imposter. At a distance, you need to move the viewer a considerable distance for the angle of view to change significantly. This can be complex to get working, but may be worth it depending on the type of project you are making.

#### Use automatic instancing

_This is only implemented in the Forward+ renderer, not Mobile or Compatibility._

If you have many identical objects in your scene, you can use automatic instancing to reduce the number of draw calls. This automatically happens for MeshInstance3D nodes that use the same mesh and material: no manual setup is required.

For automatic instancing to be effective, the material must be opaque or alpha-tested (alpha scissor or alpha hash). Alpha-blended or depth pre-pass materials are never instanced this way. Instead, you must use MultiMesh as described below.

#### Use manual instancing (MultiMesh)

If several identical objects have to be drawn in the same place or nearby, try using [MultiMesh](../godot_csharp_rendering.md) instead. MultiMesh allows the drawing of many thousands of objects at very little performance cost, making it ideal for flocks, grass, particles, and anything else where you have thousands of identical objects.

See also the Using MultiMesh documentation.

### Bake lighting

Lighting objects is one of the most costly rendering operations. Realtime lighting, shadows (especially multiple lights), and [global illumination](tutorials_3d.md) are especially expensive. They may simply be too much for lower power mobile devices to handle.

**Consider using baked lighting**, especially for mobile. This can look fantastic, but has the downside that it will not be dynamic. Sometimes, this is a tradeoff worth making.

See [Using Lightmap global illumination](tutorials_3d.md) for instructions on using baked lightmaps. For best performance, you should set lights' bake mode to **Static** as opposed to the default **Dynamic**, as this will skip real-time lighting on meshes that have baked lighting.

The downside of lights with the **Static** bake mode is that they can't cast shadows onto meshes with baked lighting. This can make scenes with outdoor environments and dynamic objects look flat. A good balance between performance and quality is to keep **Dynamic** for the [DirectionalLight3D](../godot_csharp_nodes_3d.md) node, and use **Static** for most (if not all) omni and spot lights.

### Animation and skinning

Animation and vertex animation such as skinning and morphing can be very expensive on some platforms. You may need to lower the polycount considerably for animated models, or limit the number of them on screen at any given time. You can also reduce the animation rate for distant or occluded meshes, or pause the animation entirely if the player is unlikely to notice the animation being stopped.

The [VisibleOnScreenEnabler3D](../godot_csharp_misc.md) and [VisibleOnScreenNotifier3D](../godot_csharp_misc.md) nodes can be useful for this purpose.

### Large worlds

If you are making large worlds, there are different considerations than what you may be familiar with from smaller games.

Large worlds may need to be built in tiles that can be loaded on demand as you move around the world. This can prevent memory use from getting out of hand, and also limit the processing needed to the local area.

There may also be rendering and physics glitches due to floating point error in large worlds. This can be resolved using [Large world coordinates](tutorials_physics.md). If using large world coordinates is not an option, you may be able to use techniques such as orienting the world around the player (rather than the other way around), or shifting the origin periodically to keep things centred around `Vector3(0, 0, 0)`.

---
