# Godot 4 C# Tutorials — Shaders (Part 1)

> 7 tutorials. C#-specific code examples.

## Advanced post-processing

### Introduction

This tutorial describes an advanced method for post-processing in Godot. In particular, it will explain how to write a post-processing shader that uses the depth buffer. You should already be familiar with post-processing generally and, in particular, with the methods outlined in the custom post-processing tutorial.

### Full screen quad

One way to make custom post-processing effects is by using a viewport. However, there are two main drawbacks of using a Viewport:

1. The depth buffer cannot be accessed
2. The effect of the post-processing shader is not visible in the editor

To get around the limitation on using the depth buffer, use a [MeshInstance3D](../godot_csharp_nodes_3d.md) with a [QuadMesh](../godot_csharp_rendering.md) primitive. This allows us to use a shader and to access the depth texture of the scene. Next, use a vertex shader to make the quad cover the screen at all times so that the post-processing effect will be applied at all times, including in the editor.

First, create a new MeshInstance3D and set its mesh to a QuadMesh. This creates a quad centered at position `(0, 0, 0)` with a width and height of `1`. Set the width and height to `2` and enable **Flip Faces**. Right now, the quad occupies a position in world space at the origin. However, we want it to move with the camera so that it always covers the entire screen. To do this, we will bypass the coordinate transforms that translate the vertex positions through the difference coordinate spaces and treat the vertices as if they were already in clip space.

The vertex shader expects coordinates to be output in clip space, which are coordinates ranging from `-1` at the left and bottom of the screen to `1` at the top and right of the screen. This is why the QuadMesh needs to have height and width of `2`. Godot handles the transform from model to view space to clip space behind the scenes, so we need to nullify the effects of Godot's transformations. We do this by setting the `POSITION` built-in to our desired position. `POSITION` bypasses the built-in transformations and sets the vertex position in clip space directly.

```glsl
shader_type spatial;
// Prevent the quad from being affected by lighting and fog. This also improves performance.
render_mode unshaded, fog_disabled;

void vertex() {
  POSITION = vec4(VERTEX.xy, 1.0, 1.0);
}
```

> **Note:** In versions of Godot earlier than 4.3, this code recommended using `POSITION = vec4(VERTEX, 1.0);` which implicitly assumed the clip-space near plane was at `0.0`. That code is now incorrect and will not work in versions 4.3+ as we use a "reversed-z" depth buffer now where the near plane is at `1.0`.

Even with this vertex shader, the quad keeps disappearing. This is due to frustum culling, which is done on the CPU. Frustum culling uses the camera matrix and the AABBs of Meshes to determine if the Mesh will be visible _before_ passing it to the GPU. The CPU has no knowledge of what we are doing with the vertices, so it assumes the coordinates specified refer to world positions, not clip space positions, which results in Godot culling the quad when we turn away from the center of the scene. In order to keep the quad from being culled, there are a few options:

1. Add the QuadMesh as a child to the camera, so the camera is always pointed at it
2. Set the Geometry property `extra_cull_margin` as large as possible in the QuadMesh

The second option ensures that the quad is visible in the editor, while the first option guarantees that it will still be visible even if the camera moves outside the cull margin. You can also use both options.

### Depth texture

To read from the depth texture, we first need to create a texture uniform set to the depth buffer by using `hint_depth_texture`.

```glsl
uniform sampler2D depth_texture : hint_depth_texture;
```

Once defined, the depth texture can be read with the `texture()` function.

```glsl
float depth = texture(depth_texture, SCREEN_UV).x;
```

> **Note:** Similar to accessing the screen texture, accessing the depth texture is only possible when reading from the current viewport. The depth texture cannot be accessed from another viewport to which you have rendered.

The values returned by `depth_texture` are between `1.0` and `0.0` (corresponding to the near and far plane, respectively, because of using a "reverse-z" depth buffer) and are nonlinear. When displaying depth directly from the `depth_texture`, everything will look almost black unless it is very close due to that nonlinearity. In order to make the depth value align with world or model coordinates, we need to linearize the value. When we apply the projection matrix to the vertex position, the z value is made nonlinear, so to linearize it, we multiply it by the inverse of the projection matrix, which in Godot, is accessible with the variable `INV_PROJECTION_MATRIX`.

Firstly, take the screen space coordinates and transform them into normalized device coordinates (NDC). NDC run `-1.0` to `1.0` in `x` and `y` directions and from `0.0` to `1.0` in the `z` direction when using the Vulkan backend. Reconstruct the NDC using `SCREEN_UV` for the `x` and `y` axis, and the depth value for `z`.

```glsl
void fragment() {
  float depth = texture(depth_texture, SCREEN_UV).x;
  vec3 ndc = vec3(SCREEN_UV * 2.0 - 1.0, depth);
}
```

> **Note:** This tutorial assumes the use of the Forward+ or Mobile renderers, which both use Vulkan NDCs with a Z-range of `[0.0, 1.0]`. In contrast, the Compatibility renderer uses OpenGL NDCs with a Z-range of `[-1.0, 1.0]`. For the Compatibility renderer, replace the NDC calculation with this instead: `glsl
vec3 ndc = vec3(SCREEN_UV, depth) * 2.0 - 1.0;
` You can also use the `CURRENT_RENDERER` and `RENDERER_COMPATIBILITY` built-in defines for a shader that will work in all renderers: ```glsl
> #if CURRENT_RENDERER == RENDERER_COMPATIBILITY
> vec3 ndc = vec3(SCREEN_UV, depth) _ 2.0 - 1.0;
> #else
> vec3 ndc = vec3(SCREEN_UV _ 2.0 - 1.0, depth);
> #endif

````



Convert NDC to view space by multiplying the NDC by `INV_PROJECTION_MATRIX`. Recall that view space gives positions relative to the camera, so the `z` value will give us the distance to the point.


```glsl
void fragment() {
  ...
  vec4 view = INV_PROJECTION_MATRIX * vec4(ndc, 1.0);
  view.xyz /= view.w;
  float linear_depth = -view.z;
}
````

Because the camera is facing the negative `z` direction, the position will have a negative `z` value. In order to get a usable depth value, we have to negate `view.z`.

The world position can be constructed from the depth buffer using the following code, using the `INV_VIEW_MATRIX` to transform the position from view space into world space.

```glsl
void fragment() {
  ...
  vec4 world = INV_VIEW_MATRIX * INV_PROJECTION_MATRIX * vec4(ndc, 1.0);
  vec3 world_position = world.xyz / world.w;
}
```

### Example shader

Once we add a line to output to `ALBEDO`, we have a complete shader that looks something like this. This shader lets you visualize the linear depth or world space coordinates, depending on which line is commented out.

```glsl
shader_type spatial;
// Prevent the quad from being affected by lighting and fog. This also improves performance.
render_mode unshaded, fog_disabled;

uniform sampler2D depth_texture : hint_depth_texture;

void vertex() {
  POSITION = vec4(VERTEX.xy, 1.0, 1.0);
}

void fragment() {
  float depth = texture(depth_texture, SCREEN_UV).x;
  vec3 ndc = vec3(SCREEN_UV * 2.0 - 1.0, depth);
  vec4 view = INV_PROJECTION_MATRIX * vec4(ndc, 1.0);
  view.xyz /= view.w;
  float linear_depth = -view.z;

  vec4 world = INV_VIEW_MATRIX * INV_PROJECTION_MATRIX * vec4(ndc, 1.0);
  vec3 world_position = world.xyz / world.w;

  // Visualize linear depth
  ALBEDO.rgb = vec3(fract(linear_depth));

  // Visualize world coordinates
  //ALBEDO.rgb = fract(world_position).xyz;
}
```

### An optimization

You can benefit from using a single large triangle rather than using a full screen quad. The reason for this is explained [here](https://michaldrobot.com/2014/04/01/gcn-execution-patterns-in-full-screen-passes). However, the benefit is quite small and only beneficial when running especially complex fragment shaders.

Set the Mesh in the MeshInstance3D to an [ArrayMesh](../godot_csharp_rendering.md). An ArrayMesh is a tool that allows you to easily construct a Mesh from Arrays for vertices, normals, colors, etc.

Now, attach a script to the MeshInstance3D and use the following code:

> **Note:** The triangle is specified in normalized device coordinates. Recall, NDC run from `-1.0` to `1.0` in both the `x` and `y` directions. This makes the screen `2` units wide and `2` units tall. In order to cover the entire screen with a single triangle, use a triangle that is `4` units wide and `4` units tall, double its height and width.

Assign the same vertex shader from above and everything should look exactly the same.

The one drawback to using an ArrayMesh over using a QuadMesh is that the ArrayMesh is not visible in the editor because the triangle is not constructed until the scene is run. To get around that, construct a single triangle Mesh in a modeling program and use that in the MeshInstance3D instead.

---

## Using compute shaders

This tutorial will walk you through the process of creating a minimal compute shader. But first, a bit of background on compute shaders and how they work with Godot.

> **Note:** This tutorial assumes you are familiar with shaders generally. If you are new to shaders please read Introduction to shaders and your first shader before proceeding with this tutorial.

A compute shader is a special type of shader program that is orientated towards general purpose programming. In other words, they are more flexible than vertex shaders and fragment shaders as they don't have a fixed purpose (i.e. transforming vertices or writing colors to an image). Unlike fragment shaders and vertex shaders, compute shaders have very little going on behind the scenes. The code you write is what the GPU runs and very little else. This can make them a very useful tool to offload heavy calculations to the GPU.

Now let's get started by creating a short compute shader.

First, in the **external** text editor of your choice, create a new file called `compute_example.glsl` in your project folder. When you write compute shaders in Godot, you write them in GLSL directly. The Godot shader language is based on GLSL. If you are familiar with normal shaders in Godot, the syntax below will look somewhat familiar.

> **Note:** Compute shaders can only be used from RenderingDevice-based renderers (the Forward+ or Mobile renderer). To follow along with this tutorial, ensure that you are using the Forward+ or Mobile renderer. The setting for which is located in the top right-hand corner of the editor. Note that compute shader support is generally poor on mobile devices (due to driver bugs), even if they are technically supported.

Let's take a look at this compute shader code:

```glsl
#[compute]
#version 450

// Invocations in the (x, y, z) dimension
layout(local_size_x = 2, local_size_y = 1, local_size_z = 1) in;

// A binding to the buffer we create in our script
layout(set = 0, binding = 0, std430) restrict buffer MyDataBuffer {
    float data[];
}
my_data_buffer;

// The code we want to execute in each invocation
void main() {
    // gl_GlobalInvocationID.x uniquely identifies this invocation across all work groups
    my_data_buffer.data[gl_GlobalInvocationID.x] *= 2.0;
}
```

This code takes an array of floats, multiplies each element by 2 and store the results back in the buffer array. Now let's look at it line-by-line.

```glsl
#[compute]
#version 450
```

These two lines communicate two things:

1. The following code is a compute shader. This is a Godot-specific hint that is needed for the editor to properly import the shader file.
2. The code is using GLSL version 450.

You should never have to change these two lines for your custom compute shaders.

```glsl
// Invocations in the (x, y, z) dimension
layout(local_size_x = 2, local_size_y = 1, local_size_z = 1) in;
```

Next, we communicate the number of invocations to be used in each workgroup. Invocations are instances of the shader that are running within the same workgroup. When we launch a compute shader from the CPU, we tell it how many workgroups to run. Workgroups run in parallel to each other. While running one workgroup, you cannot access information in another workgroup. However, invocations in the same workgroup can have some limited access to other invocations.

Think about workgroups and invocations as a giant nested `for` loop.

```glsl
for (int x = 0; x < workgroup_size_x; x++) {
  for (int y = 0; y < workgroup_size_y; y++) {
     for (int z = 0; z < workgroup_size_z; z++) {
        // Each workgroup runs independently and in parallel.
        for (int local_x = 0; local_x < invocation_size_x; local_x++) {
           for (int local_y = 0; local_y < invocation_size_y; local_y++) {
              for (int local_z = 0; local_z < invocation_size_z; local_z++) {
                 // Compute shader runs here.
              }
           }
        }
     }
  }
}
```

Workgroups and invocations are an advanced topic. For now, remember that we will be running two invocations per workgroup.

```glsl
// A binding to the buffer we create in our script
layout(set = 0, binding = 0, std430) restrict buffer MyDataBuffer {
    float data[];
}
my_data_buffer;
```

Here we provide information about the memory that the compute shader will have access to. The `layout` property allows us to tell the shader where to look for the buffer, we will need to match these `set` and `binding` positions from the CPU side later.

The `restrict` keyword tells the shader that this buffer is only going to be accessed from one place in this shader. In other words, we won't bind this buffer in another `set` or `binding` index. This is important as it allows the shader compiler to optimize the shader code. Always use `restrict` when you can.

This is an _unsized_ buffer, which means it can be any size. So we need to be careful not to read from an index larger than the size of the buffer.

```glsl
// The code we want to execute in each invocation
void main() {
    // gl_GlobalInvocationID.x uniquely identifies this invocation across all work groups
    my_data_buffer.data[gl_GlobalInvocationID.x] *= 2.0;
}
```

Finally, we write the `main` function which is where all the logic happens. We access a position in the storage buffer using the `gl_GlobalInvocationID` built-in variables. `gl_GlobalInvocationID` gives you the global unique ID for the current invocation.

To continue, write the code above into your newly created `compute_example.glsl` file.

### Create a local RenderingDevice

To interact with and execute a compute shader, we need a script. Create a new script in the language of your choice and attach it to any Node in your scene.

Now to execute our shader we need a local [RenderingDevice](../godot_csharp_rendering.md) which can be created using the [RenderingServer](../godot_csharp_rendering.md):

```csharp
// Create a local rendering device.
var rd = RenderingServer.CreateLocalRenderingDevice();
```

After that, we can load the newly created shader file `compute_example.glsl` and create a precompiled version of it using this:

```csharp
// Load GLSL shader
var shaderFile = GD.Load<RDShaderFile>("res://compute_example.glsl");
var shaderBytecode = shaderFile.GetSpirV();
var shader = rd.ShaderCreateFromSpirV(shaderBytecode);
```

> **Warning:** Local RenderingDevices cannot be debugged using tools such as [RenderDoc](https://renderdoc.org/).

### Provide input data

As you might remember, we want to pass an input array to our shader, multiply each element by 2 and get the results.

We need to create a buffer to pass values to a compute shader. We are dealing with an array of floats, so we will use a storage buffer for this example. A storage buffer takes an array of bytes and allows the CPU to transfer data to and from the GPU.

So let's initialize an array of floats and create a storage buffer:

```csharp
// Prepare our data. We use floats in the shader, so we need 32 bit.
float[] input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
var inputBytes = new byte[input.Length * sizeof(float)];
Buffer.BlockCopy(input, 0, inputBytes, 0, inputBytes.Length);

// Create a storage buffer that can hold our float values.
// Each float has 4 bytes (32 bit) so 10 x 4 = 40 bytes
var buffer = rd.StorageBufferCreate((uint)inputBytes.Length, inputBytes);
```

With the buffer in place we need to tell the rendering device to use this buffer. To do that we will need to create a uniform (like in normal shaders) and assign it to a uniform set which we can pass to our shader later.

```csharp
// Create a uniform to assign the buffer to the rendering device
var uniform = new RDUniform
{
    UniformType = RenderingDevice.UniformType.StorageBuffer,
    Binding = 0
};
uniform.AddId(buffer);
var uniformSet = rd.UniformSetCreate([uniform], shader, 0);
```

### Defining a compute pipeline

The next step is to create a set of instructions our GPU can execute. We need a pipeline and a compute list for that.

The steps we need to do to compute our result are:

1. Create a new pipeline.
2. Begin a list of instructions for our GPU to execute.
3. Bind our compute list to our pipeline
4. Bind our buffer uniform to our pipeline
5. Specify how many workgroups to use
6. End the list of instructions

```csharp
// Create a compute pipeline
var pipeline = rd.ComputePipelineCreate(shader);
var computeList = rd.ComputeListBegin();
rd.ComputeListBindComputePipeline(computeList, pipeline);
rd.ComputeListBindUniformSet(computeList, uniformSet, 0);
rd.ComputeListDispatch(computeList, xGroups: 5, yGroups: 1, zGroups: 1);
rd.ComputeListEnd();
```

Note that we are dispatching the compute shader with 5 work groups in the X axis, and one in the others. Since we have 2 local invocations in the X axis (specified in our shader), 10 compute shader invocations will be launched in total. If you read or write to indices outside of the range of your buffer, you may access memory outside of your shaders control or parts of other variables which may cause issues on some hardware.

### Execute a compute shader

After all of this we are almost done, but we still need to execute our pipeline. So far we have only recorded what we would like the GPU to do; we have not actually run the shader program.

To execute our compute shader we need to submit the pipeline to the GPU and wait for the execution to finish:

```csharp
// Submit to GPU and wait for sync
rd.Submit();
rd.Sync();
```

Ideally, you would not call `sync()` to synchronize the RenderingDevice right away as it will cause the CPU to wait for the GPU to finish working. In our example, we synchronize right away because we want our data available for reading right away. In general, you will want to wait _at least_ 2 or 3 frames before synchronizing so that the GPU is able to run in parallel with the CPU.

> **Warning:** Long computations can cause Windows graphics drivers to "crash" due to TDR being triggered by Windows. This is a mechanism that reinitializes the graphics driver after a certain amount of time has passed without any activity from the graphics driver (usually 5 to 10 seconds). Depending on the duration your compute shader takes to execute, you may need to split it into multiple dispatches to reduce the time each dispatch takes and reduce the chances of triggering a TDR. Given TDR is time-dependent, slower GPUs may be more prone to TDRs when running a given compute shader compared to a faster GPU.

### Retrieving results

You may have noticed that, in the example shader, we modified the contents of the storage buffer. In other words, the shader read from our array and stored the data in the same array again so our results are already there. Let's retrieve the data and print the results to our console.

```csharp
// Read back the data from the buffers
var outputBytes = rd.BufferGetData(buffer);
var output = new float[input.Length];
Buffer.BlockCopy(outputBytes, 0, output, 0, outputBytes.Length);
GD.Print("Input: ", string.Join(", ", input));
GD.Print("Output: ", string.Join(", ", output));
```

### Freeing memory

The `buffer`, `pipeline`, and `uniform_set` variables we've been using are each an [RID](../godot_csharp_math_types.md). Because RenderingDevice is meant to be a lower-level API, RIDs aren't freed automatically. This means that once you're done using `buffer` or any other RID, you are responsible for freeing its memory manually using the RenderingDevice's [free_rid()](../godot_csharp_misc.md) method.

With that, you have everything you need to get started working with compute shaders.

> **See also:** The demo projects repository contains a [Compute Shader Heightmap demo](https://github.com/godotengine/godot-demo-projects/tree/master/compute/heightmap) This project performs heightmap image generation on the CPU and GPU separately, which lets you compare how a similar algorithm can be implemented in two different ways (with the GPU implementation being faster in most cases).

---

## Converting GLSL to Godot shaders

This document explains the differences between Godot's shading language and GLSL and gives practical advice on how to migrate shaders from other sources, such as Shadertoy and The Book of Shaders, into Godot shaders.

For detailed information on Godot's shading language, please refer to the Shading Language reference.

### GLSL

Godot uses a shading language based on GLSL with the addition of a few quality-of-life features. Accordingly, most features available in GLSL are available in Godot's shading language.

#### Shader programs

In GLSL, each shader uses a separate program. You have one program for the vertex shader and one for the fragment shader. In Godot, you have a single shader that contains a `vertex` and/or a `fragment` function. If you only choose to write one, Godot will supply the other.

Godot allows uniform variables and functions to be shared by defining the fragment and vertex shaders in one file. In GLSL, the vertex and fragment programs cannot share variables except when varyings are used.

#### Vertex attributes

In GLSL, you can pass in per-vertex information using attributes and have the flexibility to pass in as much or as little as you want. In Godot, you have a set number of input attributes, including `VERTEX` (position), `COLOR`, `UV`, `UV2`, `NORMAL`. Each shaders' page in the shader reference section of the documentation comes with a complete list of its vertex attributes.

#### gl_Position

`gl_Position` receives the final position of a vertex specified in the vertex shader. It is specified by the user in clip space. Typically, in GLSL, the model space vertex position is passed in using a vertex attribute called `position` and you handle the conversion from model space to clip space manually.

In Godot, `VERTEX` specifies the vertex position in model space at the beginning of the `vertex` function. Godot also handles the final conversion to clip space after the user-defined `vertex` function is run. If you want to skip the conversion from model to view space, you can set the `render_mode` to `skip_vertex_transform`. If you want to skip all transforms, set `render_mode` to `skip_vertex_transform` and set the `PROJECTION_MATRIX` to `mat4(1.0)` in order to nullify the final transform from view space to clip space.

#### Varyings

Varyings are a type of variable that can be passed from the vertex shader to the fragment shader. In modern GLSL (3.0 and up), varyings are defined with the `in` and `out` keywords. A variable going out of the vertex shader is defined with `out` in the vertex shader and `in` inside the fragment shader.

#### Main

In GLSL, each shader program looks like a self-contained C-style program. Accordingly, the main entry point is `main`. If you are copying a vertex shader, rename `main` to `vertex` and if you are copying a fragment shader, rename `main` to `fragment`.

#### Macros

The Godot shader preprocessor supports the following macros:

- `#define` / `#undef`
- `#if`, `#elif`, `#else`, `#endif`, `defined()`, `#ifdef`, `#ifndef`
- `#include` (only `.gdshaderinc` files and with a maximum depth of 25)
- `#pragma disable_preprocessor`, which disables preprocessing for the rest of the file

#### Variables

GLSL has many built-in variables that are hard-coded. These variables are not uniforms, so they are not editable from the main program.

| Variable       | Type     | Equivalent   | Description                                       |
| -------------- | -------- | ------------ | ------------------------------------------------- |
| gl_FragColor   | out vec4 | COLOR        | Output color for each pixel.                      |
| gl_FragCoord   | vec4     | FRAGCOORD    | For full screen quads. For smaller quads, use UV. |
| gl_Position    | vec4     | VERTEX       | Position of Vertex, output from Vertex Shader.    |
| gl_PointSize   | float    | POINT_SIZE   | Size of Point primitive.                          |
| gl_PointCoord  | vec2     | POINT_COORD  | Position on point when drawing Point primitives.  |
| gl_FrontFacing | bool     | FRONT_FACING | True if front face of primitive.                  |

#### Coordinates

`gl_FragCoord` in GLSL and `FRAGCOORD` in the Godot shading language use the same coordinate system. If using UV in Godot, the y-coordinate will be flipped upside down.

#### Precision

In GLSL, you can define the precision of a given type (float or int) at the top of the shader with the `precision` keyword. In Godot, you can set the precision of individual variables as you need by placing precision qualifiers `lowp`, `mediump`, and `highp` before the type when defining the variable. For more information, see the Shading Language reference.

### Shadertoy

[Shadertoy](https://www.shadertoy.com/results?query=&sort=popular&from=10&num=4) is a website that makes it easy to write fragment shaders and create [pure magic](https://www.shadertoy.com/view/4tjGRh).

Shadertoy does not give the user full control over the shader. It handles all the input and uniforms and only lets the user write the fragment shader.

#### Types

Shadertoy uses the webgl spec, so it runs a slightly different version of GLSL. However, it still has the regular types, including constants and macros.

#### mainImage

The main point of entry to a Shadertoy shader is the `mainImage` function. `mainImage` has two parameters, `fragColor` and `fragCoord`, which correspond to `COLOR` and `FRAGCOORD` in Godot, respectively. These parameters are handled automatically in Godot, so you do not need to include them as parameters yourself. Anything in the `mainImage` function should be copied into the `fragment` function when porting to Godot.

#### Variables

In order to make writing fragment shaders straightforward and easy, Shadertoy handles passing a lot of helpful information from the main program into the fragment shader for you. A few of these have no equivalents in Godot because Godot has chosen not to make them available by default. This is okay because Godot gives you the ability to make your own uniforms. For variables whose equivalents are listed as "Provide with Uniform", users are responsible for creating that uniform themselves. The description gives the reader a hint about what they can pass in as a substitute.

| Variable              | Type      | Equivalent               | Description                                           |
| --------------------- | --------- | ------------------------ | ----------------------------------------------------- |
| fragColor             | out vec4  | COLOR                    | Output color for each pixel.                          |
| fragCoord             | vec2      | FRAGCOORD.xy             | For full screen quads. For smaller quads, use UV.     |
| iResolution           | vec3      | 1.0 / SCREEN_PIXEL_SIZE  | Can also pass in manually.                            |
| iTime                 | float     | TIME                     | Time since shader started.                            |
| iTimeDelta            | float     | Provide with Uniform     | Time to render previous frame.                        |
| iFrame                | float     | Provide with Uniform     | Frame number.                                         |
| iChannelTime[4]       | float     | Provide with Uniform     | Time since that particular texture started.           |
| iMouse                | vec4      | Provide with Uniform     | Mouse position in pixel coordinates.                  |
| iDate                 | vec4      | Provide with Uniform     | Current date, expressed in seconds.                   |
| iChannelResolution[4] | vec3      | 1.0 / TEXTURE_PIXEL_SIZE | Resolution of particular texture.                     |
| iChanneli             | Sampler2D | TEXTURE                  | Godot provides only one built-in; user can make more. |

#### Coordinates

`fragCoord` behaves the same as `gl_FragCoord` in **GLSL** and `FRAGCOORD` in Godot.

### The Book of Shaders

Similar to Shadertoy, [The Book of Shaders](https://thebookofshaders.com) provides access to a fragment shader in the web browser, with which the user may interact. The user is restricted to writing fragment shader code with a set list of uniforms passed in and with no ability to add additional uniforms.

For further help on porting shaders to various frameworks generally, The Book of Shaders provides a [page](https://thebookofshaders.com/04) on running shaders in various frameworks.

#### Types

The Book of Shaders uses the webgl spec, so it runs a slightly different version of GLSL. However, it still has the regular types, including constants and macros.

#### Main

The entry point for a Book of Shaders fragment shader is `main`, just like in GLSL. Everything written in a Book of Shaders `main` function should be copied into Godot's `fragment` function.

#### Variables

The Book of Shaders sticks closer to plain GLSL than Shadertoy does. It also implements fewer uniforms than Shadertoy.

| Variable     | Type     | Equivalent              | Description                                       |
| ------------ | -------- | ----------------------- | ------------------------------------------------- |
| gl_FragColor | out vec4 | COLOR                   | Output color for each pixel.                      |
| gl_FragCoord | vec4     | FRAGCOORD               | For full screen quads. For smaller quads, use UV. |
| u_resolution | vec2     | 1.0 / SCREEN_PIXEL_SIZE | Can also pass in manually.                        |
| u_time       | float    | TIME                    | Time since shader started.                        |
| u_mouse      | vec2     | Provide with Uniform    | Mouse position in pixel coordinates.              |

#### Coordinates

The Book of Shaders uses the same coordinate system as **GLSL**.

---

## Custom post-processing

### Introduction

Godot provides many post-processing effects out of the box, including Bloom, DOF, and SSAO, which are described in [Environment and post-processing](tutorials_3d.md). However, advanced use cases may require custom effects. This article explains how to write your own custom effects.

The easiest way to implement a custom post-processing shader is to use Godot's built-in ability to read from the screen texture. If you're not familiar with this, you should read the Screen Reading Shaders Tutorial first.

### Single pass post-processing

Post-processing effects are shaders applied to a frame after Godot has rendered it. To apply a shader to a frame, create a [CanvasLayer](../godot_csharp_nodes_2d.md), and give it a [ColorRect](../godot_csharp_ui_controls.md). Assign a new [ShaderMaterial](../godot_csharp_rendering.md) to the newly created `ColorRect`, and set the `ColorRect`'s anchor preset to Full Rect:

Your scene tree will look something like this:

> **Note:** Another more efficient method is to use a [BackBufferCopy](../godot_csharp_misc.md) to copy a region of the screen to a buffer and to access it in a shader script through a `sampler2D` using `hint_screen_texture`.

> **Note:** As of the time of writing, Godot does not support rendering to multiple buffers at the same time. Your post-processing shader will not have access to other render passes and buffers not exposed by Godot (such as depth or normal/roughness). You only have access to the rendered frame and buffers exposed by Godot as samplers.

For this demo, we will use this [Sprite](../godot_csharp_misc.md) of a sheep.

Assign a new [Shader](../godot_csharp_rendering.md) to the `ColorRect`'s `ShaderMaterial`. You can access the frame's texture and UV with a `sampler2D` using `hint_screen_texture` and the built-in `SCREEN_UV` uniforms.

Copy the following code to your shader. The code below is a hex pixelization shader by [arlez80](https://bitbucket.org/arlez80/hex-mosaic/src/master/),

```glsl
shader_type canvas_item;

uniform vec2 size = vec2(32.0, 28.0);
// If you intend to read from mipmaps with `textureLod()` LOD values greater than `0.0`,
// use `filter_nearest_mipmap` instead. This shader doesn't require it.
uniform sampler2D screen_texture : hint_screen_texture, repeat_disable, filter_nearest;

void fragment() {
        vec2 norm_size = size * SCREEN_PIXEL_SIZE;
        bool less_than_half = mod(SCREEN_UV.y / 2.0, norm_size.y) / norm_size.y < 0.5;
        vec2 uv = SCREEN_UV + vec2(norm_size.x * 0.5 * float(less_than_half), 0.0);
        vec2 center_uv = floor(uv / norm_size) * norm_size;
        vec2 norm_uv = mod(uv, norm_size) / norm_size;
        center_uv += mix(vec2(0.0, 0.0),
                         mix(mix(vec2(norm_size.x, -norm_size.y),

# ...
```

The sheep will look something like this:

### Multi-pass post-processing

Some post-processing effects like blurs are resource intensive. You can make them run a lot faster if you break them down in multiple passes. In a multipass material, each pass takes the result from the previous pass as an input and processes it.

To produce a multi-pass post-processing shader, you stack `CanvasLayer` and `ColorRect` nodes. In the example above, you use a `CanvasLayer` object to render a shader using the frame on the layer below. Apart from the node structure, the steps are the same as with the single-pass post-processing shader.

Your scene tree will look something like this:

As an example, you could write a full screen Gaussian blur effect by attaching the following pieces of code to each of the `ColorRect` nodes. The order in which you apply the shaders depends on the position of the `CanvasLayer` in the scene tree, higher means sooner. For this blur shader, the order does not matter.

```glsl
shader_type canvas_item;

uniform sampler2D screen_texture : hint_screen_texture, repeat_disable, filter_nearest;

// Blurs the screen in the X-direction.
void fragment() {
    vec3 col = texture(screen_texture, SCREEN_UV).xyz * 0.16;
    col += texture(screen_texture, SCREEN_UV + vec2(SCREEN_PIXEL_SIZE.x, 0.0)).xyz * 0.15;
    col += texture(screen_texture, SCREEN_UV + vec2(-SCREEN_PIXEL_SIZE.x, 0.0)).xyz * 0.15;
    col += texture(screen_texture, SCREEN_UV + vec2(2.0 * SCREEN_PIXEL_SIZE.x, 0.0)).xyz * 0.12;
    col += texture(screen_texture, SCREEN_UV + vec2(2.0 * -SCREEN_PIXEL_SIZE.x, 0.0)).xyz * 0.12;
    col += texture(screen_texture, SCREEN_UV + vec2(3.0 * SCREEN_PIXEL_SIZE.x, 0.0)).xyz * 0.09;
    col += texture(screen_texture, SCREEN_UV + vec2(3.0 * -SCREEN_PIXEL_SIZE.x, 0.0)).xyz
# ...
```

```glsl
shader_type canvas_item;

uniform sampler2D screen_texture : hint_screen_texture, repeat_disable, filter_nearest;

// Blurs the screen in the Y-direction.
void fragment() {
    vec3 col = texture(screen_texture, SCREEN_UV).xyz * 0.16;
    col += texture(screen_texture, SCREEN_UV + vec2(0.0, SCREEN_PIXEL_SIZE.y)).xyz * 0.15;
    col += texture(screen_texture, SCREEN_UV + vec2(0.0, -SCREEN_PIXEL_SIZE.y)).xyz * 0.15;
    col += texture(screen_texture, SCREEN_UV + vec2(0.0, 2.0 * SCREEN_PIXEL_SIZE.y)).xyz * 0.12;
    col += texture(screen_texture, SCREEN_UV + vec2(0.0, 2.0 * -SCREEN_PIXEL_SIZE.y)).xyz * 0.12;
    col += texture(screen_texture, SCREEN_UV + vec2(0.0, 3.0 * SCREEN_PIXEL_SIZE.y)).xyz * 0.09;
    col += texture(screen_texture, SCREEN_UV + vec2(0.0, 3.0 * -SCREEN_PIXEL_SIZE.y)).xyz
# ...
```

Using the above code, you should end up with a full screen blur effect like below.

---

## Introduction to shaders

This page explains what shaders are and will give you an overview of how they work in Godot. For a detailed reference of the engine's shading language, see Shading language.

Shaders are a special kind of program that runs on Graphics Processing Units (GPUs). They were initially used to shade 3D scenes but can nowadays do much more. You can use them to control how the engine draws geometry and pixels on the screen, allowing you to achieve all sorts of effects.

Modern rendering engines like Godot draw everything with shaders: graphics cards can run thousands of instructions in parallel, leading to incredible rendering speed.

Because of their parallel nature, though, shaders don't process information the way a typical program does. Shader code runs on each vertex or pixel in isolation. You cannot store data between frames either. As a result, when working with shaders, you need to code and think differently from other programming languages.

Suppose you want to update all the pixels in a texture to a given color. In GDScript, your code would use `for` loops:

Your code is already part of a loop in a shader, so the corresponding code would look like this.

```glsl
void fragment() {
    COLOR = some_color;
}
```

> **Note:** The graphics card calls the `fragment()` function once or more for each pixel it has to draw. More on that below.

### Shaders in Godot

Godot provides a shading language based on the popular OpenGL Shading Language (GLSL) but simplified. The engine handles some of the lower-level initialization work for you, making it easier to write complex shaders.

In Godot, shaders are made up of main functions called "processor functions". Processor functions are the entry point for your shader into the program. There are seven different processor functions.

1. The `vertex()` function runs over all the vertices in the mesh and sets their positions and some other per-vertex variables. Used in canvas_item shaders and spatial shaders.
2. The `fragment()` function runs for every pixel covered by the mesh. It uses values output by the `vertex()` function, interpolated between the vertices. Used in canvas_item shaders and spatial shaders.
3. The `light()` function runs for every pixel and for every light. It takes variables from the `fragment()` function and from its previous runs. Used in canvas_item shaders and spatial shaders.
4. The `start()` function runs for every particle in a particle system once when the particle is first spawned. Used in particles shaders.
5. The `process()` function runs for every particle in a particle system for each frame. Used in particles shaders.
6. The `sky()` function runs for every pixel in the radiance cubemap when the radiance cubemap needs to be updated, and for every pixel on the current screen. Used in sky shaders.
7. The `fog()` function runs for every froxel in the volumetric fog froxel buffer that intersects with the [FogVolume](../godot_csharp_nodes_3d.md). Used by fog shaders.

> **Warning:** The `light()` function won't run if the `vertex_lighting` render mode is enabled, or if **Rendering > Quality > Shading > Force Vertex Shading** is enabled in the Project Settings. It's enabled by default on mobile platforms.

> **Note:** Godot also exposes an API for users to write totally custom GLSL shaders. For more information see Using compute shaders.

### Shader types

Instead of supplying a general-purpose configuration for all uses (2D, 3D, particles, sky, fog), you must specify the type of shader you're writing. Different types support different render modes, built-in variables, and processing functions.

In Godot, all shaders need to specify their type in the first line, like so:

```glsl
shader_type spatial;
```

Here are the available types:

- spatial for 3D rendering.
- canvas_item for 2D rendering.
- particles for particle systems.
- sky to render [Skies](../godot_csharp_misc.md).
- fog to render [FogVolumes](../godot_csharp_nodes_3d.md)

### Render modes

Shaders have optional render modes you can specify on the second line, after the shader type, like so:

```glsl
shader_type spatial;
render_mode unshaded, cull_disabled;
```

Render modes alter the way Godot applies the shader. For example, the `unshaded` mode makes the engine skip the built-in light processor function.

Each shader type has different render modes. See the reference for each shader type for a complete list of render modes.

#### Vertex processor

The `vertex()` processing function is called once for every vertex in `spatial` and `canvas_item` shaders.

Each vertex in your world's geometry has properties like a position and color. The function modifies those values and passes them to the fragment function. You can also use it to send extra data to the fragment function using varyings.

By default, Godot transforms your vertex information for you, which is necessary to project geometry onto the screen. You can use render modes to transform the data yourself; see the Spatial shader doc for an example.

#### Fragment processor

The `fragment()` processing function is used to set up the Godot material parameters per pixel. This code runs on every visible pixel the object or primitive draws. It is only available in `spatial` and `canvas_item` shaders.

The standard use of the fragment function is to set up material properties used to calculate lighting. For example, you would set values for `ROUGHNESS`, `RIM`, or `TRANSMISSION`, which would tell the light function how the lights respond to that fragment. This makes it possible to control a complex shading pipeline without the user having to write much code. If you don't need this built-in functionality, you can ignore it and write your own light processing function, and Godot will optimize it away. For example, if you do not write a value to `RIM`, Godot will not calculate rim lighting. During compilation, Godot checks to see if `RIM` is used; if not, it cuts all the corresponding code out. Therefore, you will not waste calculations on the effects that you do not use.

#### Light processor

The `light()` processor runs per pixel too, and it runs once for every light that affects the object. It does not run if no lights affect the object. It exists as a function called inside the `fragment()` processor and typically operates on the material properties setup inside the `fragment()` function.

The `light()` processor works differently in 2D than it does in 3D; for a description of how it works in each, see their documentation, CanvasItem shaders and Spatial shaders, respectively.

---

## Making trees

This is a short tutorial on how to make trees and other types of vegetation from scratch.

The aim is to not focus on the modeling techniques (there are plenty of tutorials about that), but how to make them look good in Godot.

### Start with a tree

I took this tree from SketchFab:

[https://sketchfab.com/models/ea5e6ed7f9d6445ba69589d503e8cebf](https://sketchfab.com/models/ea5e6ed7f9d6445ba69589d503e8cebf)

and opened it in Blender.

### Paint with vertex colors

The first thing you may want to do is to use the vertex colors to paint how much the tree will sway when there is wind. Just use the vertex color painting tool of your favorite 3D modeling program and paint something like this:

This is a bit exaggerated, but the idea is that color indicates how much sway affects every part of the tree. This scale here represents it better:

### Write a custom shader for the leaves

This is an example of a shader for leaves:

```glsl
shader_type spatial;
render_mode depth_prepass_alpha, cull_disabled, world_vertex_coords;
```

This is a spatial shader. There is no front/back culling (so leaves can be seen from both sides), and alpha prepass is used, so there are less depth artifacts that result from using transparency (and leaves cast shadow). Finally, for the sway effect, world coordinates are recommended, so the tree can be duplicated, moved, etc. and it will still work together with other trees.

```glsl
uniform sampler2D texture_albedo : source_color;
uniform vec4 transmission : source_color;
```

Here, the texture is read, as well as a transmission color, which is used to add some back-lighting to the leaves, simulating subsurface scattering.

```glsl
uniform float sway_speed = 1.0;
uniform float sway_strength = 0.05;
uniform float sway_phase_len = 8.0;

void vertex() {
    float strength = COLOR.r * sway_strength;
    VERTEX.x += sin(VERTEX.x * sway_phase_len * 1.123 + TIME * sway_speed) * strength;
    VERTEX.y += sin(VERTEX.y * sway_phase_len + TIME * sway_speed * 1.12412) * strength;
    VERTEX.z += sin(VERTEX.z * sway_phase_len * 0.9123 + TIME * sway_speed * 1.3123) * strength;
}
```

This is the code to create the sway of the leaves. It's basic (just uses a sinewave multiplying by the time and axis position, but works well). Notice that the strength is multiplied by the color. Every axis uses a different small near 1.0 multiplication factor so axes don't appear in sync.

Finally, all that's left is the fragment shader:

```glsl
void fragment() {
    vec4 albedo_tex = texture(texture_albedo, UV);
    ALBEDO = albedo_tex.rgb;
    ALPHA = albedo_tex.a;
    METALLIC = 0.0;
    ROUGHNESS = 1.0;
    SSS_TRANSMITTANCE_COLOR = transmission.rgba;
}
```

And this is pretty much it.

The trunk shader is similar, except it does not write to the alpha channel (thus no alpha prepass is needed) and does not require transmission to work. Both shaders can be improved by adding normal mapping, AO and other maps.

### Improving the shader

There are many more resources on how to do this that you can read. Now that you know the basics, a recommended read is the chapter from GPU Gems3 about how Crysis does this (focus mostly on the sway code, as many other techniques shown there are obsolete):

[https://developer.nvidia.com/gpugems/GPUGems3/gpugems3_ch16.html](https://developer.nvidia.com/gpugems/GPUGems3/gpugems3_ch16.html)

---

## Screen-reading shaders

### Introduction

It is often desired to make a shader that reads from the same screen to which it's writing. 3D APIs, such as OpenGL or DirectX, make this very difficult because of internal hardware limitations. GPUs are extremely parallel, so reading and writing causes all sorts of cache and coherency problems. As a result, not even the most modern hardware supports this properly.

The workaround is to make a copy of the screen, or a part of the screen, to a back-buffer and then read from it while drawing. Godot provides a few tools that make this process easy.

### Screen texture

Godot Shading language has a special texture to access the already rendered contents of the screen. It is used by specifying a hint when declaring a `sampler2D` uniform: `hint_screen_texture`. A special built-in varying `SCREEN_UV` can be used to obtain the UV relative to the screen for the current fragment. As a result, this canvas_item fragment shader results in an invisible object, because it only shows what lies behind:

```glsl
shader_type canvas_item;

uniform sampler2D screen_texture : hint_screen_texture, repeat_disable, filter_nearest;

void fragment() {
    COLOR = textureLod(screen_texture, SCREEN_UV, 0.0);
}
```

`textureLod` is used here as we only want to read from the bottom mipmap. If you want to read from a blurred version of the texture instead, you can increase the third argument to `textureLod` and change the hint `filter_nearest` to `filter_nearest_mipmap` (or any other filter with mipmaps enabled). If using a filter with mipmaps, Godot will automatically calculate the blurred texture for you.

> **Warning:** If the filter mode is not changed to a filter mode that contains `mipmap` in its name, `textureLod` with an LOD parameter greater than `0.0` will have the same appearance as with the `0.0` LOD parameter.

### Screen texture example

The screen texture can be used for many things. There is a special demo for _Screen Space Shaders_, that you can download to see and learn. One example is a simple shader to adjust brightness, contrast and saturation:

```glsl
shader_type canvas_item;

uniform sampler2D screen_texture : hint_screen_texture, repeat_disable, filter_nearest;

uniform float brightness = 1.0;
uniform float contrast = 1.0;
uniform float saturation = 1.0;

void fragment() {
    vec3 c = textureLod(screen_texture, SCREEN_UV, 0.0).rgb;

    c.rgb = mix(vec3(0.0), c.rgb, brightness);
    c.rgb = mix(vec3(0.5), c.rgb, contrast);
    c.rgb = mix(vec3(dot(vec3(1.0), c.rgb) * 0.33333), c.rgb, saturation);

    COLOR.rgb = c;
}
```

### Behind the scenes

While this seems magical, it's not. In 2D, when `hint_screen_texture` is first found in a node that is about to be drawn, Godot does a full-screen copy to a back-buffer. Subsequent nodes that use it in shaders will not have the screen copied for them, because this ends up being inefficient. In 3D, the screen is copied after the opaque geometry pass, but before the transparent geometry pass, so transparent objects will not be captured in the screen texture.

As a result, in 2D, if shaders that use `hint_screen_texture` overlap, the second one will not use the result of the first one, resulting in unexpected visuals:

In the above image, the second sphere (top right) is using the same source for the screen texture as the first one below, so the first one "disappears", or is not visible.

In 2D, this can be corrected via the [BackBufferCopy](../godot_csharp_misc.md) node, which can be instantiated between both spheres. BackBufferCopy can work by either specifying a screen region or the whole screen:

With correct back-buffer copying, the two spheres blend correctly:

> **Warning:** In 3D, materials that use `hint_screen_texture` are considered transparent themselves and will not appear in the resulting screen texture of other materials. If you plan to instance a scene that uses a material with `hint_screen_texture`, you will need to use a BackBufferCopy node.

In 3D, there is less flexibility to solve this particular issue because the screen texture is only captured once. Be careful when using the screen texture in 3D as it won't capture transparent objects and may capture some opaque objects that are in front of the object using the screen texture.

You can reproduce the back-buffer logic in 3D by creating a [Viewport](../godot_csharp_rendering.md) with a camera in the same position as your object, and then use the [Viewport's](../godot_csharp_rendering.md) texture instead of the screen texture.

### Back-buffer logic

So, to make it clearer, here's how the backbuffer copying logic works in 2D in Godot:

- If a node uses `hint_screen_texture`, the entire screen is copied to the back buffer before drawing that node. This only happens the first time; subsequent nodes do not trigger this.
- If a BackBufferCopy node was processed before the situation in the point above (even if `hint_screen_texture` was not used), the behavior described in the point above does not happen. In other words, automatic copying of the entire screen only happens if `hint_screen_texture` is used in a node for the first time and no BackBufferCopy node (not disabled) was found before in tree-order.
- BackBufferCopy can copy either the entire screen or a region. If set to only a region (not the whole screen) and your shader uses pixels not in the region copied, the result of that read is undefined (most likely garbage from previous frames). In other words, it's possible to use BackBufferCopy to copy back a region of the screen and then read the screen texture from a different region. Avoid this behavior!

### Depth texture

For 3D shaders, it's also possible to access the screen depth buffer. For this, the `hint_depth_texture` hint is used. This texture is not linear; it must be converted using the inverse projection matrix.

The following code retrieves the 3D position below the pixel being drawn:

```glsl
uniform sampler2D depth_texture : hint_depth_texture, repeat_disable, filter_nearest;

void fragment() {
    float depth = textureLod(depth_texture, SCREEN_UV, 0.0).r;
    vec4 upos = INV_PROJECTION_MATRIX * vec4(SCREEN_UV * 2.0 - 1.0, depth, 1.0);
    vec3 pixel_position = upos.xyz / upos.w;
}
```

### Normal-roughness texture

> **Note:** Normal-roughness texture is only supported in the Forward+ rendering method, not Mobile or Compatibility.

Similarly, the normal-roughness texture can be used to read the normals and roughness of objects rendered in the depth prepass. The normal is stored in the `.xyz` channels (mapped to the 0-1 range) while the roughness is stored in the `.w` channel.

```glsl
uniform sampler2D normal_roughness_texture : hint_normal_roughness_texture, repeat_disable, filter_nearest;

void fragment() {
    float screen_roughness = texture(normal_roughness_texture, SCREEN_UV).w;
    vec3 screen_normal = texture(normal_roughness_texture, SCREEN_UV).xyz;
    screen_normal = screen_normal * 2.0 - 1.0;
```

### Redefining screen textures

The screen texture hints (`hint_screen_texture`, `hint_depth_texture`, and `hint_normal_roughness_texture`) can be used with multiple uniforms. For example, you may want to read from the texture multiple times with a different repeat flag or filter flag.

The following example shows a shader that reads the screen space normal with linear filtering, but reads the screen space roughness using nearest neighbor filtering.

```glsl
uniform sampler2D normal_roughness_texture : hint_normal_roughness_texture, repeat_disable, filter_nearest;
uniform sampler2D normal_roughness_texture2 : hint_normal_roughness_texture, repeat_enable, filter_linear;

void fragment() {
    float screen_roughness = texture(normal_roughness_texture, SCREEN_UV).w;
    vec3 screen_normal = texture(normal_roughness_texture2, SCREEN_UV).xyz;
    screen_normal = screen_normal * 2.0 - 1.0;
```

---
