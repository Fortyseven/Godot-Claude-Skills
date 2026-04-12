# Godot 4 GDScript Tutorials — Shaders (Part 6)

> 4 tutorials. GDScript-specific code examples.

## Using a SubViewport as a texture

### Introduction

This tutorial will introduce you to using the [SubViewport](../godot_gdscript_rendering.md) as a texture that can be applied to 3D objects. In order to do so, it will walk you through the process of making a procedural planet like the one below:

> **Note:** This tutorial does not cover how to code a dynamic atmosphere like the one this planet has.

This tutorial assumes you are familiar with how to set up a basic scene including: a [Camera3D](../godot_gdscript_nodes_3d.md), a [light source](../godot_gdscript_misc.md), a [MeshInstance3D](../godot_gdscript_nodes_3d.md) with a [Primitive Mesh](../godot_gdscript_misc.md), and applying a [StandardMaterial3D](../godot_gdscript_rendering.md) to the mesh. The focus will be on using the [SubViewport](../godot_gdscript_rendering.md) to dynamically create textures that can be applied to the mesh.

In this tutorial, we'll cover the following topics:

- How to use a [SubViewport](../godot_gdscript_rendering.md) as a render texture
- Mapping a texture to a sphere with equirectangular mapping
- Fragment shader techniques for procedural planets
- Setting a Roughness map from a [Viewport Texture](../godot_gdscript_rendering.md)

### Setting up the scene

Create a new scene and add the following nodes exactly as shown below.

Go into the the MeshInstance3D and make the mesh a SphereMesh

### Setting up the SubViewport

Click on the [SubViewport](../godot_gdscript_rendering.md) node and set its size to `(1024, 512)`. The [SubViewport](../godot_gdscript_rendering.md) can actually be any size so long as the width is double the height. The width needs to be double the height so that the image will accurately map onto the sphere, as we will be using equirectangular projection, but more on that later.

Next disable 3D. We will be using a [ColorRect](../godot_gdscript_ui_controls.md) to render the surface, so we don't need 3D either.

Select the [ColorRect](../godot_gdscript_ui_controls.md) and in the inspector set the anchors preset to `Full Rect`. This will ensure that the [ColorRect](../godot_gdscript_ui_controls.md) takes up the entire [SubViewport](../godot_gdscript_rendering.md).

Next, we add a [Shader Material](../godot_gdscript_rendering.md) to the [ColorRect](../godot_gdscript_ui_controls.md) (ColorRect > CanvasItem > Material > Material > `New ShaderMaterial`).

> **Note:** Basic familiarity with shading is recommended for this tutorial. However, even if you are new to shaders, all the code will be provided, so you should have no problem following along.

Click the dropdown menu button for the shader material and click / Edit. From here go to Shader > `New Shader`. give it a name and click "Create". click the shader in the inspector to open the shader editor. Delete the default code and add the following:

```glsl
shader_type canvas_item;

void fragment() {
    COLOR = vec4(UV.x, UV.y, 0.5, 1.0);
}
```

save the shader code, you'll see in the inspector that the above code renders a gradient like the one below.

Now we have the basics of a [SubViewport](../godot_gdscript_rendering.md) that we render to and we have a unique image that we can apply to the sphere.

### Applying the texture

Now go into the [MeshInstance3D](../godot_gdscript_nodes_3d.md) and add a [StandardMaterial3D](../godot_gdscript_rendering.md) to it. No need for a special [Shader Material](../godot_gdscript_rendering.md) (although that would be a good idea for more advanced effects, like the atmosphere in the example above).

MeshInstance3D > GeometryInstance > Geometry > Material Override > `New StandardMaterial3D`

Then click the dropdown for the StandardMaterial3D and click "Edit"

Go to the "Resource" section and check the `Local to scene` box. Then, go to the "Albedo" section and click beside the "Texture" property to add an Albedo Texture. Here we will apply the texture we made. Choose "New ViewportTexture"

Click on the ViewportTexture you just created in the inspector, then click "Assign". Then, from the menu that pops up, select the Viewport that we rendered to earlier.

Your sphere should now be colored in with the colors we rendered to the Viewport.

Notice the ugly seam that forms where the texture wraps around? This is because we are picking a color based on UV coordinates and UV coordinates do not wrap around the texture. This is a classic problem in 2D map projection. Game developers often have a 2-dimensional map they want to project onto a sphere, but when it wraps around, it has large seams. There is an elegant workaround for this problem that we will illustrate in the next section.

### Making the planet texture

So now, when we render to our [SubViewport](../godot_gdscript_rendering.md), it appears magically on the sphere. But there is an ugly seam created by our texture coordinates. So how do we get a range of coordinates that wrap around the sphere in a nice way? One solution is to use a function that repeats on the domain of our texture. `sin` and `cos` are two such functions. Let's apply them to the texture and see what happens. Replace the existing color code in the shader with the following:

```glsl
COLOR.xyz = vec3(sin(UV.x * 3.14159 * 4.0) * cos(UV.y * 3.14159 * 4.0) * 0.5 + 0.5);
```

Not too bad. If you look around, you can see that the seam has now disappeared, but in its place, we have pinching at the poles. This pinching is due to the way Godot maps textures to spheres in its [StandardMaterial3D](../godot_gdscript_rendering.md). It uses a projection technique called equirectangular projection, which translates a spherical map onto a 2D plane.

> **Note:** If you are interested in a little extra information on the technique, we will be converting from spherical coordinates into Cartesian coordinates. Spherical coordinates map the longitude and latitude of the sphere, while Cartesian coordinates are, for all intents and purposes, a vector from the center of the sphere to the point.

For each pixel, we will calculate its 3D position on the sphere. From that, we will use 3D noise to determine a color value. By calculating the noise in 3D, we solve the problem of the pinching at the poles. To understand why, picture the noise being calculated across the surface of the sphere instead of across the 2D plane. When you calculate across the surface of the sphere, you never hit an edge, and hence you never create a seam or a pinch point on the pole. The following code converts the `UVs` into Cartesian coordinates.

```glsl
float theta = UV.y * 3.14159;
float phi = UV.x * 3.14159 * 2.0;
vec3 unit = vec3(0.0, 0.0, 0.0);

unit.x = sin(phi) * sin(theta);
unit.y = cos(theta) * -1.0;
unit.z = cos(phi) * sin(theta);
unit = normalize(unit);
```

And if we use `unit` as an output `COLOR` value, we get:

Now that we can calculate the 3D position of the surface of the sphere, we can use 3D noise to make the planet. We will be using this noise function directly from a [Shadertoy](https://www.shadertoy.com/view/Xsl3Dl):

```glsl
vec3 hash(vec3 p) {
    p = vec3(dot(p, vec3(127.1, 311.7, 74.7)),
             dot(p, vec3(269.5, 183.3, 246.1)),
             dot(p, vec3(113.5, 271.9, 124.6)));

    return -1.0 + 2.0 * fract(sin(p) * 43758.5453123);
}

float noise(vec3 p) {
  vec3 i = floor(p);
  vec3 f = fract(p);
  vec3 u = f * f * (3.0 - 2.0 * f);

  return mix(mix(mix(dot(hash(i + vec3(0.0, 0.0, 0.0)), f - vec3(0.0, 0.0, 0.0)),
                     dot(hash(i + vec3(1.0, 0.0, 0.0)), f - vec3(1.0, 0.0, 0.0)), u.x),
                 mix(dot(hash(i + vec3(0.0, 1.0, 0.0)), f - vec3(0.0, 1.0, 0.0)),
                     dot(hash(i + vec3(1.0, 1.0, 0.0)), f - vec3(1.0, 1.0, 0.0)), u.x), u.y),
             mix(mix(dot(hash(i + vec3(0.0, 0.0, 1.0)), f - vec3(0.0, 0.0, 1.0)),
                     dot(hash(i + vec3(1.0, 0.0,
# ...
```

> **Note:** All credit goes to the author, Inigo Quilez. It is published under the `MIT` licence.

Now to use `noise`, add the following to the `fragment` function:

```glsl
float n = noise(unit * 5.0);
COLOR.xyz = vec3(n * 0.5 + 0.5);
```

> **Note:** In order to highlight the texture, we set the material to unshaded.

You can see now that the noise indeed wraps seamlessly around the sphere. Although this looks nothing like the planet you were promised. So let's move onto something more colorful.

### Coloring the planet

Now to make the planet colors. While there are many ways to do this, for now, we will stick with a gradient between water and land.

To make a gradient in GLSL, we use the `mix` function. `mix` takes two values to interpolate between and a third argument to choose how much to interpolate between them; in essence, it _mixes_ the two values together. In other APIs, this function is often called `lerp`. However, `lerp` is typically reserved for mixing two floats together; `mix` can take any values whether it be floats or vector types.

```glsl
COLOR.xyz = mix(vec3(0.05, 0.3, 0.5), vec3(0.9, 0.4, 0.1), n * 0.5 + 0.5);
```

The first color is blue for the ocean. The second color is a kind of reddish color (because all alien planets need red terrain). And finally, they are mixed together by `n * 0.5 + 0.5`. `n` smoothly varies between `-1` and `1`. So we map it into the `0-1` range that `mix` expects. Now you can see that the colors change between blue and red.

That is a little more blurry than we want. Planets typically have a relatively clear separation between land and sea. In order to do that, we will change the last term to `smoothstep(-0.1, 0.0, n)`. And thus the whole line becomes:

```glsl
COLOR.xyz = mix(vec3(0.05, 0.3, 0.5), vec3(0.9, 0.4, 0.1), smoothstep(-0.1, 0.0, n));
```

What `smoothstep` does is return `0` if the third argument is below the first and `1` if the third argument is larger than the second and smoothly blends between `0` and `1` if the third number is between the first and the second. So in this line, `smoothstep` returns `0` whenever `n` is less than `-0.1` and it returns `1` whenever `n` is above `0`.

One more thing to make this a little more planet-y. The land shouldn't be so blobby; let's make the edges a little rougher. A trick that is often used in shaders to make rough looking terrain with noise is to layer levels of noise over one another at various frequencies. We use one layer to make the overall blobby structure of the continents. Then another layer breaks up the edges a bit, and then another, and so on. What we will do is calculate `n` with four lines of shader code instead of just one. `n` becomes:

```glsl
float n = noise(unit * 5.0) * 0.5;
n += noise(unit * 10.0) * 0.25;
n += noise(unit * 20.0) * 0.125;
n += noise(unit * 40.0) * 0.0625;
```

And now the planet looks like:

### Making an ocean

One final thing to make this look more like a planet. The ocean and the land reflect light differently. So we want the ocean to shine a little more than the land. We can do this by passing a fourth value into the `alpha` channel of our output `COLOR` and using it as a Roughness map.

```glsl
COLOR.a = 0.3 + 0.7 * smoothstep(-0.1, 0.0, n);
```

This line returns `0.3` for water and `1.0` for land. This means that the land is going to be quite rough, while the water will be quite smooth.

And then, in the material, under the "Metallic" section, make sure `Metallic` is set to `0` and `Specular` is set to `1`. The reason for this is the water reflects light really well, but isn't metallic. These values are not physically accurate, but they are good enough for this demo.

Next, under the "Roughness" section set the roughness texture to a [Viewport Texture](../godot_gdscript_rendering.md) pointing to our planet texture [SubViewport](../godot_gdscript_rendering.md). Finally, set the `Texture Channel` to `Alpha`. This instructs the renderer to use the `alpha` channel of our output `COLOR` as the `Roughness` value.

You'll notice that very little changes except that the planet is no longer reflecting the sky. This is happening because, by default, when something is rendered with an alpha value, it gets drawn as a transparent object over the background. And since the default background of the [SubViewport](../godot_gdscript_rendering.md) is opaque, the `alpha` channel of the [Viewport Texture](../godot_gdscript_rendering.md) is `1`, resulting in the planet texture being drawn with slightly fainter colors and a `Roughness` value of `1` everywhere. To correct this, we go into the [SubViewport](../godot_gdscript_rendering.md) and enable the "Transparent Bg" property. Since we are now rendering one transparent object on top of another, we want to enable `blend_premul_alpha`:

```glsl
render_mode blend_premul_alpha;
```

This pre-multiplies the colors by the `alpha` value and then blends them correctly together. Typically, when blending one transparent color on top of another, even if the background has an `alpha` of `0` (as it does in this case), you end up with weird color bleed issues. Setting `blend_premul_alpha` fixes that.

Now the planet should look like it is reflecting light on the ocean but not the land. move around the [OmniLight3D](../godot_gdscript_nodes_3d.md) in the scene so you can see the effect of the reflections on the ocean.

And there you have it. A procedural planet generated using a [SubViewport](../godot_gdscript_rendering.md).

---

## Using VisualShaders

VisualShaders are the visual alternative for creating shaders.

As shaders are inherently linked to visuals, the graph-based approach with previews of textures, materials, etc. offers a lot of additional convenience compared to purely script-based shaders. On the other hand, VisualShaders do not expose all features of the shader script and using both in parallel might be necessary for specific effects.

> **Note:** If you are not familiar with shaders, start by reading Introduction to shaders.

### Creating a VisualShader

VisualShaders can be created in any [ShaderMaterial](../godot_gdscript_rendering.md). To begin using VisualShaders, create a new `ShaderMaterial` in an object of your choice.

Then assign a [Shader](../godot_gdscript_rendering.md) resource to the `Shader` property.

Click on the new `Shader` resource and the Create Shader dialog will open automatically. Change the Type option to [VisualShader](../godot_gdscript_rendering.md) in the dropdown, then give it a name.

Click on the visual shader you just created to open the Shader Editor. The layout of the Shader Editor comprises four parts, a file list on the left, the upper toolbar, the graph itself, and a material preview on the right that can be toggled off

From left to right in the toolbar:

- The arrow can be used to toggle the files panel's visibility.
- The `File` button opens a dropdown menu for saving, loading, and creating files.
- The `Add Node` button displays a popup menu to let you add nodes to the shader graph.
- The drop-down menu is the shader type: Vertex, Fragment and Light. Like for script shaders, it defines what built-in nodes will be available.
- The following buttons and number input control the zooming level, grid snapping and distance between grid lines (in pixels).
- The toggle controls if the graph minimap in the bottom right of the editor is visible or not.
- The automatically arrange selected nodes button will try to organize any nodes you have selected as efficiently and cleanly as possible.
- The Manage Varyings button opens a dropdown that lets you add or remove a varying.
- The show generated code button shows shader code corresponding to your graph.
- The toggle turns the material preview on or off.
- The `Online Docs` button opens this documentation page in your web browser.
- The last button allows you to put the shader editor in its own window, separate from the rest of the editor.

> **Note:** Although VisualShaders do not require coding, they share the same logic with script shaders. It is advised to learn the basics of both to have a good understanding of the shading pipeline. The visual shader graph is converted to a script shader behind the scene, and you can see this code by pressing the last button in the toolbar. This can be convenient to understand what a given node does and how to reproduce it in scripts.

### Using the Visual Shader Editor

By default, every new `VisualShader` will have an output node. Every node connection ends at one of the output node's sockets. A node is the basic unit to create your shader. To add a new node, click on the `Add Node` button on the upper left corner or right click on any empty location in the graph, and a menu will pop up.

This popup has the following properties:

- If you right-click on the graph, this menu will be called at the cursor position and the created node, in that case, will also be placed under that position; otherwise, it will be created at the graph's center.
- It can be resized horizontally and vertically allowing more content to be shown. Size transform and tree content position are saved between the calls, so if you suddenly closed the popup you can easily restore its previous state.
- The `Expand All` and `Collapse All` options in the drop-down option menu can be used to easily list the available nodes.
- You can also drag and drop nodes from the popup onto the graph.

While the popup has nodes sorted in categories, it can seem overwhelming at first. Try to add some of the nodes, plug them in the output socket and observe what happens.

When connecting any `scalar` output to a `vector` input, all components of the vector will take the value of the scalar.

When connecting any `vector` output to a `scalar` input, the value of the scalar will be the average of the vector's components.

### Visual Shader node interface

Visual shader nodes have input and output ports. The input ports are located on the left side of the node, and output ports are located on the right side of the node.

These ports are colored to differentiate type of port:

| Type      | Color  | Description                                           | Example |
| --------- | ------ | ----------------------------------------------------- | ------- |
| Scalar    | Gray   | Scalar is a single value.                             |         |
| Vector    | Purple | Vector is a set of values.                            |         |
| Boolean   | Green  | On or off, true or false.                             |         |
| Transform | Pink   | A matrix, usually used to transform vertices.         |         |
| Sampler   | Orange | A texture sampler. It can be used to sample textures. |         |

All of the types are used in the calculations of vertices, fragments, and lights in the shader. For example: matrix multiplication, vector addition, or scalar division.

There are other types but these are the main ones.

### Visual Shader nodes

Below are some special nodes that are worth knowing about. The list is not exhaustive and might be expanded with more nodes and examples.

#### Expression node

The `Expression` node allows you to write Godot Shading Language (GLSL-like) expressions inside your visual shaders. The node has buttons to add any amount of required input and output ports and can be resized. You can also set up the name and type of each port. The expression you have entered will apply immediately to the material (once the focus leaves the expression text box). Any parsing or compilation errors will be printed to the Output tab. The outputs are initialized to their zero value by default. The node is located under the Special tab and can be used in all shader modes.

The possibilities of this node are almost limitless – you can write complex procedures, and use all the power of text-based shaders, such as loops, the `discard` keyword, extended types, etc. For example:

#### Reroute node

The `Reroute` node is used purely for organizational purposes. In a complicated shader with many nodes you may find that the paths between nodes can make things hard to read. Reroute, as its name suggests, allows you to adjust the path between nodes to make things easier to read. You can even have multiple reroute nodes for a single path, which can be used to make right angles.

To move a reroute node move your mouse cursor above it, and grab the handle that appears.

#### Fresnel node

The `Fresnel` node is designed to accept normal and view vectors and produces a scalar which is the saturated dot product between them. Additionally, you can setup the inversion and the power of equation. The `Fresnel` node is great for adding a rim-like lighting effect to objects.

#### Boolean node

The `Boolean` node can be converted to `Scalar` or `Vector` to represent `0` or `1` and `(0, 0, 0)` or `(1, 1, 1)` respectively. This property can be used to enable or disable some effect parts with one click.

#### If node

The `If` node allows you to setup a vector which will be returned the result of the comparison between `a` and `b`. There are three vectors which can be returned: `a == b` (in that case the tolerance parameter is provided as a comparison threshold – by default it is equal to the minimal value, i.e. `0.00001`), `a > b` and `a < b`.

#### Switch node

The `Switch` node returns a vector if the boolean condition is `true` or `false`. `Boolean` was introduced above. If you want to convert a vector to a true boolean, all components of the vector should be non-zero.

#### Mesh Emitter

The `Mesh Emitter` node is used for emitting particles from mesh vertices. This is only available for shaders that are in `Particles` mode.

Keep in mind that not all 3D objects are mesh files. a glTF file can't be dragged and dropped into the graph. However, you can create an inherited scene from it, save the mesh in that scene as its own file, and use that.

You can also drag and drop obj files into the graph editor to add the node for that specific mesh, other mesh files will not work for this.

---

## Your first 2D shader

### Introduction

Shaders are special programs that execute on the GPU and are used for rendering graphics. All modern rendering is done with shaders. For a more detailed description of what shaders are please see What are shaders.

This tutorial will focus on the practical aspects of writing shader programs by walking you through the process of writing a shader with both vertex and fragment functions. This tutorial targets absolute beginners to shaders.

> **Note:** If you have experience writing shaders and are just looking for an overview of how shaders work in Godot, see the Shading Reference.

### Setup

CanvasItem shaders are used to draw all 2D objects in Godot, while Spatial shaders are used to draw all 3D objects.

In order to use a shader it must be attached inside a [Material](../godot_gdscript_rendering.md) which must be attached to an object. Materials are a type of [Resource](tutorials_scripting.md). To draw multiple objects with the same material, the material must be attached to each object.

All objects derived from a [CanvasItem](../godot_gdscript_nodes_2d.md) have a material property. This includes all [GUI elements](../godot_gdscript_misc.md), [Sprite2Ds](../godot_gdscript_nodes_2d.md), [TileMapLayers](../godot_gdscript_nodes_2d.md), [MeshInstance2Ds](../godot_gdscript_nodes_2d.md) etc. They also have an option to inherit their parent's material. This can be useful if you have a large number of nodes that you want to use the same material.

To begin, create a Sprite2D node. [You can use any CanvasItem](tutorials_2d.md), so long as it is drawing to the canvas, so for this tutorial we will use a Sprite2D, as it is the easiest CanvasItem to start drawing with.

In the Inspector, click beside "Texture" where it says "[empty]" and select "Load", then select "icon.svg". For new projects, this is the Godot icon. You should now see the icon in the viewport.

Next, look down in the Inspector, under the CanvasItem section, click beside "Material" and select "New ShaderMaterial". This creates a new Material resource. Click on the sphere that appears. Godot currently doesn't know whether you are writing a CanvasItem Shader or a Spatial Shader and it previews the output of spatial shaders. So what you are seeing is the output of the default Spatial Shader.

> **Note:** Materials that inherit from the [Material](../godot_gdscript_rendering.md) resource, such as [StandardMaterial3D](../godot_gdscript_rendering.md) and [ParticleProcessMaterial](../godot_gdscript_rendering.md), can be converted to a [ShaderMaterial](../godot_gdscript_rendering.md) and their existing properties will be converted to an accompanying text shader. To do so, right-click on the material in the FileSystem dock and choose **Convert to ShaderMaterial**. You can also do so by right-clicking on any property holding a reference to the material in the inspector.

Click beside "Shader" and select "New Shader". Finally, click on the shader you just created and the shader editor will open. You are now ready to begin writing your first shader.

### Your first CanvasItem shader

In Godot, all shaders start with a line specifying what type of shader they are. It uses the following format:

```glsl
shader_type canvas_item;
```

Because we are writing a CanvasItem shader, we specify `canvas_item` in the first line. All our code will go beneath this declaration.

This line tells the engine which built-in variables and functionality to supply you with.

In Godot you can override three functions to control how the shader operates; `vertex`, `fragment`, and `light`. This tutorial will walk you through writing a shader with both vertex and fragment functions. Light functions are significantly more complex than vertex and fragment functions and so will not be covered here.

### Your first fragment function

The fragment function runs for every pixel in a Sprite2D and determines what color that pixel should be.

They are restricted to the pixels covered by the Sprite2D, that means you cannot use one to, for example, create an outline around a Sprite2D.

The most basic fragment function does nothing except assign a single color to every pixel.

We do so by writing a `vec4` to the built-in variable `COLOR`. `vec4` is shorthand for constructing a vector with 4 numbers. For more information about vectors see the [Vector math tutorial](tutorials_math.md). `COLOR` is both an input variable to the fragment function and the final output from it.

```glsl
void fragment(){
  COLOR = vec4(0.4, 0.6, 0.9, 1.0);
}
```

Congratulations! You're done. You have successfully written your first shader in Godot.

Now let's make things more complex.

There are many inputs to the fragment function that you can use for calculating `COLOR`. `UV` is one of them. UV coordinates are specified in your Sprite2D (without you knowing it!) and they tell the shader where to read from textures for each part of the mesh.

In the fragment function you can only read from `UV`, but you can use it in other functions or to assign values to `COLOR` directly.

`UV` varies between 0-1 from left-right and from top-bottom.

```glsl
void fragment() {
  COLOR = vec4(UV, 0.5, 1.0);
}
```

#### Using TEXTURE built-in

The default fragment function reads from the set Sprite2D texture and displays it.

When you want to adjust a color in a Sprite2D you can adjust the color from the texture manually like in the code below.

```glsl
void fragment(){
  // This shader will result in a blue-tinted icon
  COLOR.b = 1.0;
}
```

Certain nodes, like Sprite2Ds, have a dedicated texture variable that can be accessed in the shader using `TEXTURE`. If you want to use the Sprite2D texture to combine with other colors, you can use the `UV` with the `texture` function to access this variable. Use them to redraw the Sprite2D with the texture.

```glsl
void fragment(){
  COLOR = texture(TEXTURE, UV); // Read from texture again.
  COLOR.b = 1.0; //set blue channel to 1.0
}
```

#### Uniform input

Uniform input is used to pass data into a shader that will be the same across the entire shader.

You can use uniforms by defining them at the top of your shader like so:

```glsl
uniform float size;
```

For more information about usage see the Shading Language doc.

Add a uniform to change the amount of blue in our Sprite2D.

```glsl
uniform float blue = 1.0; // you can assign a default value to uniforms

void fragment(){
  COLOR = texture(TEXTURE, UV); // Read from texture
  COLOR.b = blue;
}
```

Now you can change the amount of blue in the Sprite2D from the editor. Look back at the Inspector under where you created your shader. You should see a section called "Shader Param". Unfold that section and you will see the uniform you just declared. If you change the value in the editor, it will overwrite the default value you provided in the shader.

#### Interacting with shaders from code

You can change uniforms from code using the function `set_shader_parameter()` which is called on the node's material resource. With a Sprite2D node, the following code can be used to set the `blue` uniform.

```gdscript
var blue_value = 1.0
material.set_shader_parameter("blue", blue_value)
```

Note that the name of the uniform is a string. The string must match exactly with how it is written in the shader, including spelling and case.

### Your first vertex function

Now that we have a fragment function, let's write a vertex function.

Use the vertex function to calculate where on the screen each vertex should end up.

The most important variable in the vertex function is `VERTEX`. Initially, it specifies the vertex coordinates in your model, but you also write to it to determine where to actually draw those vertices. `VERTEX` is a `vec2` that is initially presented in local-space (i.e. not relative to the camera, viewport, or parent nodes).

You can offset the vertices by directly adding to `VERTEX`.

```glsl
void vertex() {
  VERTEX += vec2(10.0, 0.0);
}
```

Combined with the `TIME` built-in variable, this can be used for basic animation.

```glsl
void vertex() {
  // Animate Sprite2D moving in big circle around its location
  VERTEX += vec2(cos(TIME)*100.0, sin(TIME)*100.0);
}
```

### Conclusion

At their core, shaders do what you have seen so far, they compute `VERTEX` and `COLOR`. It is up to you to dream up more complex mathematical strategies for assigning values to those variables.

For inspiration, take a look at some of the more advanced shader tutorials, and look at other sites like [Shadertoy](https://www.shadertoy.com/results?query=&sort=popular&from=10&num=4) and [The Book of Shaders](https://thebookofshaders.com).

---

## Your first 3D shader

You have decided to start writing your own custom Spatial shader. Maybe you saw a cool trick online that was done with shaders, or you have found that the [StandardMaterial3D](../godot_gdscript_rendering.md) isn't quite meeting your needs. Either way, you have decided to write your own and now you need to figure out where to start.

This tutorial will explain how to write a Spatial shader and will cover more topics than the CanvasItem tutorial.

Spatial shaders have more built-in functionality than CanvasItem shaders. The expectation with spatial shaders is that Godot has already provided the functionality for common use cases and all the user needs to do in the shader is set the proper parameters. This is especially true for a PBR (physically based rendering) workflow.

This is a two-part tutorial. In this first part we will create terrain using vertex displacement from a heightmap in the vertex function. In the second part we will take the concepts from this tutorial and set up custom materials in a fragment shader by writing an ocean water shader.

> **Note:** This tutorial assumes some basic shader knowledge such as types (`vec2`, `float`, `sampler2D`), and functions. If you are uncomfortable with these concepts it is best to get a gentle introduction from [The Book of Shaders](https://thebookofshaders.com) before completing this tutorial.

### Where to assign my material

In 3D, objects are drawn using [Meshes](../godot_gdscript_misc.md). Meshes are a resource type that store geometry (the shape of your object) and materials (the color and how the object reacts to light) in units called "surfaces". A Mesh can have multiple surfaces, or just one. Typically, you would import a mesh from another program (e.g. Blender). But Godot also has a few [PrimitiveMeshes](../godot_gdscript_rendering.md) that allow you to add basic geometry to a scene without importing Meshes.

There are multiple node types that you can use to draw a mesh. The main one is [MeshInstance3D](../godot_gdscript_nodes_3d.md), but you can also use [GPUParticles3D](../godot_gdscript_misc.md), [MultiMeshes](../godot_gdscript_rendering.md) (with a [MultiMeshInstance3D](../godot_gdscript_nodes_3d.md)), or others.

Typically, a material is associated with a given surface in a mesh, but some nodes, like MeshInstance3D, allow you to override the material for a specific surface, or for all surfaces.

If you set a material on the surface or mesh itself, then all MeshInstance3Ds that share that mesh will share that material. However, if you want to reuse the same mesh across multiple mesh instances, but have different materials for each instance then you should set the material on the MeshInstance3D.

For this tutorial we will set our material on the mesh itself rather than taking advantage of the MeshInstance3D's ability to override materials.

### Setting up

Add a new [MeshInstance3D](../godot_gdscript_nodes_3d.md) node to your scene.

In the inspector tab, set the MeshInstance3D's **Mesh** property to a new [PlaneMesh](../godot_gdscript_rendering.md) resource, by clicking on `<empty>` and choosing **New PlaneMesh**. Then expand the resource by clicking on the image of a plane that appears.

This adds a plane to our scene.

Then, in the viewport, click in the upper left corner on the **Perspective** button. In the menu that appears, select **Display Wireframe**.

This will allow you to see the triangles making up the plane.

Now set **Subdivide Width** and **Subdivide Depth** of the [PlaneMesh](../godot_gdscript_rendering.md) to `32`.

You can see that there are now many more triangles in the [MeshInstance3D](../godot_gdscript_nodes_3d.md). This will give us more vertices to work with and thus allow us to add more detail.

[PrimitiveMeshes](../godot_gdscript_rendering.md), like PlaneMesh, only have one surface, so instead of an array of materials there is only one. Set the **Material** to a new ShaderMaterial, then expand the material by clicking on the sphere that appears.

> **Note:** Materials that inherit from the [Material](../godot_gdscript_rendering.md) resource, such as [StandardMaterial3D](../godot_gdscript_rendering.md) and [ParticleProcessMaterial](../godot_gdscript_rendering.md), can be converted to a [ShaderMaterial](../godot_gdscript_rendering.md) and their existing properties will be converted to an accompanying text shader. To do so, right-click on the material in the FileSystem dock and choose **Convert to ShaderMaterial**. You can also do so by right-clicking on any property holding a reference to the material in the inspector.

Now set the material's **Shader** to a new Shader by clicking `<empty>` and select **New Shader...**. Leave the default settings, give your shader a name, and click **Create**.

Click on the shader in the inspector, and the shader editor should now pop up. You are ready to begin writing your first Spatial shader!

### Shader magic

The new shader is already generated with a `shader_type` variable, the `vertex()` function, and the `fragment()` function. The first thing Godot shaders need is a declaration of what type of shader they are. In this case the `shader_type` is set to `spatial` because this is a spatial shader.

```glsl
shader_type spatial;
```

The `vertex()` function determines where the vertices of your [MeshInstance3D](../godot_gdscript_nodes_3d.md) appear in the final scene. We will be using it to offset the height of each vertex and make our flat plane appear like a little terrain.

With nothing in the `vertex()` function, Godot will use its default vertex shader. We can start to make changes by adding a single line:

```glsl
void vertex() {
  VERTEX.y += cos(VERTEX.x) * sin(VERTEX.z);
}
```

Adding this line, you should get an image like the one below.

Okay, let's unpack this. The `y` value of the `VERTEX` is being increased. And we are passing the `x` and `z` components of the `VERTEX` as arguments to cos() and sin(); that gives us a wave-like appearance across the `x` and `z` axes.

What we want to achieve is the look of little hills; after all. `cos()` and `sin()` already look kind of like hills. We do so by scaling the inputs to the `cos()` and `sin()` functions.

```glsl
void vertex() {
  VERTEX.y += cos(VERTEX.x * 4.0) * sin(VERTEX.z * 4.0);
}
```

This looks better, but it is still too spiky and repetitive, let's make it a little more interesting.

### Noise heightmap

Noise is a very popular tool for faking the look of terrain. Think of it as similar to the cosine function where you have repeating hills except, with noise, each hill has a different height.

Godot provides the [NoiseTexture2D](../godot_gdscript_resources.md) resource for generating a noise texture that can be accessed from a shader.

To access a texture in a shader add the following code near the top of your shader, outside the `vertex()` function.

```glsl
uniform sampler2D noise;
```

This will allow you to send a noise texture to the shader. Now look in the inspector under your material. You should see a section called **Shader Parameters**. If you open it up, you'll see a parameter called "Noise".

Set this **Noise** parameter to a new [NoiseTexture2D](../godot_gdscript_resources.md). Then in your NoiseTexture2D, set its **Noise** property to a new [FastNoiseLite](../godot_gdscript_resources.md). The FastNoiseLite class is used by the NoiseTexture2D to generate a heightmap.

Once you set it up and should look like this.

Now, access the noise texture using the `texture()` function:

```glsl
void vertex() {
  float height = texture(noise, VERTEX.xz / 2.0 + 0.5).x;
  VERTEX.y += height;
}
```

texture() takes a texture as the first argument and a `vec2` for the position on the texture as the second argument. We use the `x` and `z` channels of `VERTEX` to determine where on the texture to look up.

Since the PlaneMesh coordinates are within the `[-1.0, 1.0]` range (for a size of `2.0`), while the texture coordinates are within `[0.0, 1.0]`, to remap the coordinates we divide by the size of the PlaneMesh by `2.0` and add `0.5` .

`texture()` returns a `vec4` of the `r, g, b, a` channels at the position. Since the noise texture is grayscale, all of the values are the same, so we can use any one of the channels as the height. In this case we'll use the `r`, or `x` channel.

> **Note:** `xyzw` is the same as `rgba` in GLSL, so instead of `texture().x` above, we could use `texture().r`. See the [OpenGL documentation](<https://www.khronos.org/opengl/wiki/Data_Type_(GLSL)#Vectors>) for more details.

Using this code you can see the texture creates random looking hills.

Right now it is too spiky, we want to soften the hills a bit. To do that, we will use a uniform. You already used a uniform above to pass in the noise texture, now let's learn how they work.

### Uniforms

Uniform variables allow you to pass data from the game into the shader. They are very useful for controlling shader effects. Uniforms can be almost any datatype that can be used in the shader. To use a uniform, you declare it in your [Shader](../godot_gdscript_rendering.md) using the keyword `uniform`.

Let's make a uniform that changes the height of the terrain.

```glsl
uniform float height_scale = 0.5;
```

Godot lets you initialize a uniform with a value; here, `height_scale` is set to `0.5`. You can set uniforms from GDScript by calling the function [set_shader_parameter()](../godot_gdscript_misc.md) on the material corresponding to the shader. The value passed from GDScript takes precedence over the value used to initialize it in the shader.

```gdscript
# called from the MeshInstance3D
mesh.material.set_shader_parameter("height_scale", 0.5)
```

> **Note:** Changing uniforms in Spatial-based nodes is different from CanvasItem-based nodes. Here, we set the material inside the PlaneMesh resource. In other mesh resources you may need to first access the material by calling `surface_get_material()`. While in the MeshInstance3D you would access the material using `get_surface_material()` or `material_override`.

Remember that the string passed into `set_shader_parameter()` must match the name of the uniform variable in the shader. You can use the uniform variable anywhere inside your shader. Here, we will use it to set the height value instead of arbitrarily multiplying by `0.5`.

```glsl
VERTEX.y += height * height_scale;
```

Now it looks much better.

Using uniforms, we can even change the value every frame to animate the height of the terrain. Combined with [Tweens](../godot_gdscript_misc.md), this can be especially useful for animations.

### Interacting with light

First, turn wireframe off. To do so, open the **Perspective** menu in the upper-left of the viewport again, and select **Display Normal**. Additionally in the 3D scene toolbar, turn off preview sunlight.

Note how the mesh color goes flat. This is because the lighting on it is flat. Let's add a light!

First, we will add an [OmniLight3D](../godot_gdscript_nodes_3d.md) to the scene, and drag it up so it is above the terrain.

You can see the light affecting the terrain, but it looks odd. The problem is the light is affecting the terrain as if it were a flat plane. This is because the light shader uses the normals from the [Mesh](../godot_gdscript_rendering.md) to calculate light.

The normals are stored in the Mesh, but we are changing the shape of the Mesh in the shader, so the normals are no longer correct. To fix this, we can recalculate the normals in the shader or use a normal texture that corresponds to our noise. Godot makes both easy for us.

You can calculate the new normal manually in the vertex function and then just set `NORMAL`. With `NORMAL` set, Godot will do all the difficult lighting calculations for us. We will cover this method in the next part of this tutorial, for now we will read normals from a texture.

Instead we will rely on the NoiseTexture again to calculate normals for us. We do that by passing in a second noise texture.

```glsl
uniform sampler2D normalmap;
```

Set this second uniform texture to another [NoiseTexture2D](../godot_gdscript_resources.md) with another [FastNoiseLite](../godot_gdscript_resources.md). But this time, check **As Normal Map**.

When we have normals that correspond to a specific vertex we set `NORMAL`, but if you have a normalmap that comes from a texture, set the normal using `NORMAL_MAP` in the `fragment()` function. This way Godot will handle wrapping the texture around the mesh automatically.

Lastly, in order to ensure that we are reading from the same places on the noise texture and the normalmap texture, we are going to pass the `VERTEX.xz` position from the `vertex()` function to the `fragment()` function. We do that using a varying.

Above the `vertex()` define a `varying vec2` called `tex_position`. And inside the `vertex()` function assign `VERTEX.xz` to `tex_position`.

```glsl
varying vec2 tex_position;

void vertex() {
  tex_position = VERTEX.xz / 2.0 + 0.5;
  float height = texture(noise, tex_position).x;
  VERTEX.y += height * height_scale;
}
```

And now we can access `tex_position` from the `fragment()` function.

```glsl
void fragment() {
  NORMAL_MAP = texture(normalmap, tex_position).xyz;
}
```

With the normals in place the light now reacts to the height of the mesh dynamically.

We can even drag the light around and the lighting will update automatically.

### Full code

Here is the full code for this tutorial. You can see it is not very long as Godot handles most of the difficult stuff for you.

```glsl
shader_type spatial;

uniform float height_scale = 0.5;
uniform sampler2D noise;
uniform sampler2D normalmap;

varying vec2 tex_position;

void vertex() {
  tex_position = VERTEX.xz / 2.0 + 0.5;
  float height = texture(noise, tex_position).x;
  VERTEX.y += height * height_scale;
}

void fragment() {
  NORMAL_MAP = texture(normalmap, tex_position).xyz;
}
```

That is everything for this part. Hopefully, you now understand the basics of vertex shaders in Godot. In the next part of this tutorial we will write a fragment function to accompany this vertex function and we will cover a more advanced technique to turn this terrain into an ocean of moving waves.

---
