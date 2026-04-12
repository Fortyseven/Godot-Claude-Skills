# Godot 4 GDScript Tutorials — 2D (Part 1)

> 8 tutorials. GDScript-specific code examples.

## 2D antialiasing

> **See also:** Godot also supports antialiasing in 3D rendering. This is covered on the [3D antialiasing](tutorials_3d.md) page.

### Introduction

Due to their limited resolution, scenes rendered in 2D can exhibit aliasing artifacts. These artifacts usually manifest in the form of a "staircase" effect on geometry edges, and are most noticeable when using nodes such as [Line2D](../godot_gdscript_nodes_2d.md), [Polygon2D](../godot_gdscript_nodes_2d.md) or [TextureProgressBar](../godot_gdscript_resources.md). Custom drawing in 2D can also have aliasing artifacts for methods that don't support antialiasing.

In the example below, you can notice how edges have a blocky appearance:

To combat this, Godot supports several methods of enabling antialiasing on 2D rendering.

### Antialiasing property in Line2D and custom drawing

This is the recommended method, as it has a lower performance impact in most cases.

Line2D has an **Antialiased** property which you can enable in the inspector. Also, several methods for Custom drawing in 2D support an optional `antialiased` parameter, which can be set to `true` when calling the function.

These methods do not require MSAA to be enabled, which makes their _baseline_ performance cost low. In other words, there is no permanent added cost if you're not drawing any antialiased geometry at some point.

The downside of these antialiasing methods is that they work by generating additional geometry. If you're generating complex 2D geometry that's updated every frame, this may be a bottleneck. Also, Polygon2D, TextureProgressBar, and several custom drawing methods don't feature an antialiased property. For these nodes, you can use 2D multisample antialiasing instead.

### Multisample antialiasing (MSAA)

_This is only available in the Forward+ and Mobile renderers, not the Compatibility renderer._

Before enabling MSAA in 2D, it's important to understand what MSAA will operate on. MSAA in 2D follows similar restrictions as in 3D. While it does not introduce any blurriness, its scope of application is limited. The main applications of 2D MSAA are:

- Geometry edges, such as line and polygon drawing.
- Sprite edges _only for pixels touching one of the texture's edges_. This works for both linear and nearest-neighbor filtering. Sprite edges created using transparency on the image are not affected by MSAA.

The downside of MSAA is that it only operates on edges. This is because MSAA increases the number of _coverage_ samples, but not the number of _color_ samples. However, since the number of color samples did not increase, fragment shaders are still run for each pixel only once. As a result, MSAA will **not affect** the following kinds of aliasing in any way:

- Aliasing _within_ nearest-neighbor filtered textures (pixel art).
- Aliasing caused by custom 2D shaders.
- Specular aliasing when using Light2D.
- Aliasing in font rendering.

MSAA can be enabled in the Project Settings by changing the value of the [Rendering > Anti Aliasing > Quality > MSAA 2D](../godot_gdscript_misc.md) setting. It's important to change the value of the **MSAA 2D** setting and not **MSAA 3D**, as these are entirely separate settings.

Comparison between no antialiasing (left) and various MSAA levels (right). The top-left corner contains a Line2D node, the top-right corner contains 2 TextureProgressBar nodes. The bottom contains 8 pixel art sprites, with 4 of them touching the edges (green background) and 4 of them not touching the edges (Godot logo):

---

## 2D lights and shadows

### Introduction

By default, 2D scenes in Godot are unshaded, with no lights and shadows visible. While this is fast to render, unshaded scenes can look bland. Godot provides the ability to use real-time 2D lighting and shadows, which can greatly enhance the sense of depth in your project.

### Nodes

There are several nodes involved in a complete 2D lighting setup:

- [CanvasModulate](../godot_gdscript_nodes_2d.md) (to darken the rest of the scene)
- [PointLight2D](../godot_gdscript_misc.md) (for omnidirectional or spot lights)
- [DirectionalLight2D](../godot_gdscript_misc.md) (for sunlight or moonlight)
- [LightOccluder2D](../godot_gdscript_nodes_2d.md) (for light shadow casters)
- Other 2D nodes that receive lighting, such as Sprite2D or TileMapLayer.

[CanvasModulate](../godot_gdscript_nodes_2d.md) is used to darken the scene by specifying a color that will act as the base "ambient" color. This is the final lighting color in areas that are _not_ reached by any 2D light. Without a CanvasModulate node, the final scene would look too bright as 2D lights would only brighten the existing unshaded appearance (which appears fully lit).

[Sprite2Ds](../godot_gdscript_nodes_2d.md) are used to display the textures for the light blobs, the background, and for the shadow casters.

[PointLight2Ds](../godot_gdscript_misc.md) are used to light the scene. The way a light typically works is by adding a selected texture over the rest of the scene to simulate lighting.

[LightOccluder2Ds](../godot_gdscript_nodes_2d.md) are used to tell the shader which parts of the scene cast shadows. These occluders can be placed as independent nodes or can be part of a TileMapLayer node.

The shadows appear only on areas covered by the [PointLight2D](../godot_gdscript_misc.md) and their direction is based on the center of the [Light](../godot_gdscript_misc.md).

> **Note:** The background color does **not** receive any lighting. If you want light to be cast on the background, you need to add a visual representation for the background, such as a Sprite2D. The Sprite2D's **Region** properties can be helpful to quickly create a repeating background texture, but remember to also set **Texture > Repeat** to **Enabled** in the Sprite2D's properties.

### Point lights

Point lights (also called positional lights) are the most common element in 2D lighting. Point lights can be used to represent light from torches, fire, projectiles, etc.

PointLight2D offers the following properties to tweak in the inspector:

- **Texture:** The texture to use as a light source. The texture's size determines the size of the light. The texture may have an alpha channel, which is useful when using Light2D's **Mix** blend mode, but it is not required if using the **Add** (default) or **Subtract** blend modes.
- **Offset:** The offset for the light texture. Unlike when you move the light node, changing the offset does _not_ cause shadows to move.
- **Texture Scale:** The multiplier for the light's size. Higher values will make the light extend out further. Larger lights have a higher performance cost as they affect more pixels on screen, so consider this before increasing a light's size.
- **Height:** The light's virtual height with regards to normal mapping. By default, the light is very close to surfaces receiving lights. This will make lighting hardly visible if normal mapping is used, so consider increasing this value. Adjusting the light's height only makes a visible difference on surfaces that use normal mapping.

If you don't have a pre-made texture to use in a light, you can use this "neutral" point light texture (right-click > **Save Image As…**):

If you need different falloff, you can procedurally create a texture by assigning a **New GradientTexture2D** on the light's **Texture** property. After creating the resource, expand its **Fill** section and set the fill mode to **Radial**. You will then have to adjust the gradient itself to start from opaque white to transparent white, and move its starting location to be in the center.

### Directional light

Directional lighting is used to represent sunlight or moonlight. Light rays are casted parallel to each other, as if the sun or moon was infinitely far away from the surface that is receiving the light.

DirectionalLight2D offers the following properties:

- **Height:** The light's virtual height with regards to normal mapping (`0.0` = parallel to surfaces, `1.0` = perpendicular to surfaces). By default, the light is fully parallel with the surfaces receiving lights. This will make lighting hardly visible if normal mapping is used, so consider increasing this value. Adjusting the light's height only makes a visual difference on surfaces that use normal mapping. **Height** does not affect shadows' appearance.
- **Max Distance:** The maximum distance from the camera center objects can be before their shadows are culled (in pixels). Decreasing this value can prevent objects located outside the camera from casting shadows (while also improving performance). Camera2D zoom is not taken into account by **Max Distance**, which means that at higher zoom values, shadows will appear to fade out sooner when zooming onto a given point.

> **Note:** Directional shadows will always appear to be infinitely long, regardless of the value of the **Height** property. This is a limitation of the shadow rendering method used for 2D lights in Godot. To have directional shadows that are not infinitely long, you should disable shadows in the DirectionalLight2D and use a custom shader that reads from the 2D signed distance field instead. This distance field is automatically generated from LightOccluder2D nodes present in the scene.

### Common light properties

Both PointLight2D and DirectionalLight2D offer common properties, which are part of the Light2D base class:

- **Enabled:** Allows toggling the light's visibility. Unlike hiding the light node, disabling this property will not hide the light's children.
- **Editor Only:** If enabled, the light is only visible within the editor. It will be automatically disabled in the running project.
- **Color:** The light's color.
- **Energy:** The light's intensity multiplier. Higher values result in a brighter light.
- **Blend Mode:** The blending formula used for light computations. The default **Add** is suited for most use cases. **Subtract** can be used for negative lights, which are not physically accurate but can be used for special effects. The **Mix** blend mode mixes the value of pixels corresponding to the light's texture with the values of pixels under it by linear interpolation.
- **Range > Z Min:** The lowest Z index affected by the light.
- **Range > Z Max:** The highest Z index affected by the light.
- **Range > Layer Min:** The lowest visual layer affected by the light.
- **Range > Layer Max:** The highest visual layer affected by the light.
- **Range > Item Cull Mask:** Controls which nodes receive light from this node, depending on the other nodes' enabled visual layers **Occluder Light Mask**. This can be used to prevent certain objects from receiving light.

### Setting up shadows

After enabling the **Shadow > Enabled** property on a PointLight2D or DirectionalLight2D node, you will not see any visual difference initially. This is because no nodes in your scene have any _occluders_ yet, which are used as a basis for shadow casting.

For shadows to appear in the scene, LightOccluder2D nodes must be added to the scene. These nodes must also have occluder polygons that are designed to match the sprite's outline.

Along with their polygon resource (which must be set to have any visual effect), LightOccluder2D nodes have 2 properties:

- **SDF Collision:** If enabled, the occluder will be part of a real-time generated _signed distance field_ that can be used in custom shaders. When not using custom shaders that read from this SDF, enabling this makes no visual difference and has no performance cost, so this is enabled by default for convenience.
- **Occluder Light Mask:** This is used in tandem with PointLight2D and DirectionalLight2D's **Shadow > Item Cull Mask** property to control which objects cast shadows for each light. This can be used to prevent specific objects from casting shadows.

There are two ways to create light occluders:

#### Automatically generating a light occluder

Occluders can be created automatically from Sprite2D nodes by selecting the node, clicking the **Sprite2D** menu at the top of the 2D editor then choosing **Create LightOccluder2D Sibling**.

In the dialog that appears, an outline will surround your sprite's edges. If the outline matches the sprite's edges closely, you can click **OK**. If the outline is too far away from the sprite's edges (or is "eating" into the sprite's edges), adjust **Grow (pixels)** and **Shrink (pixels)**, then click **Update Preview**. Repeat this operation until you get satisfactory results.

#### Manually drawing a light occluder

Create a LightOccluder2D node, then select the node and click the "+" button at the top of the 2D editor. When asked to create a polygon resource, answer **Yes**. You can then start drawing an occluder polygon by clicking to create new points. You can remove existing points by right-clicking them, and you can create new points from the existing line by clicking on the line then dragging.

The following properties can be adjusted on 2D lights that have shadows enabled:

- **Color:** The color of shaded areas. By default, shaded areas are fully black, but this can be changed for artistic purposes. The color's alpha channel controls how much the shadow is tinted by the specified color.
- **Filter:** The filter mode to use for shadows. The default **None** is the fastest to render, and is well suited for games with a pixel art aesthetic (due to its "blocky" visuals). If you want a soft shadow, use **PCF5** instead. **PCF13** is even softer, but is the most demanding to render. PCF13 should only be used for a few lights at once due to its high rendering cost.
- **Filter Smooth:** Controls how much softening is applied to shadows when **Filter** is set to **PCF5** or **PCF13**. Higher values result in a softer shadow, but may cause banding artifacts to be visible (especially with PCF5).
- **Item Cull Mask:** Controls which LightOccluder2D nodes cast shadows, depending on their respective **Occluder Light Mask** properties.

> **Note:** **Lighting and shadow resolution in pixel-art games** The engine computes 2D lighting and shadows at the **Viewport's pixel resolution**, not at the source texture's texel resolution. The appearance of lights and shadows depends on your window or Viewport resolution, not on the resolution of individual sprite textures. If you create a pixel-art game and want pixelated or blocky lighting and shadows that match your art style, **Nearest** texture filtering will **not** achieve this effect. Nearest filtering affects only how the engine samples textures — it does not change how the engine renders lighting and shadows. To achieve pixelated lighting and shadows, use a custom shader to modify `LIGHT_VERTEX` and `SHADOW_VERTEX` to snap light sampling to a pixel grid. The following shader snaps lighting to a grid using the `floor()` function: ```glsl
> shader_type canvas_item;

uniform float pixel_size = 4.0;

void fragment() {
// Snap lighting and shadows to pixel grid.
LIGHT_VERTEX.xy = floor(LIGHT_VERTEX.xy / pixel_size) _ pixel_size;
SHADOW_VERTEX = floor(SHADOW_VERTEX / pixel_size) _ pixel_size;

    // Normal rendering.
    COLOR = texture(TEXTURE, UV);

}
```This works by dividing the position by`pixel_size`to convert to grid space, using`floor()` to round down to the nearest grid point, then multiplying back to convert to screen space. The result forces the engine to sample lighting from discrete grid positions, which creates the pixelated effect. For more information on canvas item shaders, see [CanvasItem shaders](tutorials_shaders.md).

### Normal and specular maps

Normal maps and specular maps can greatly enhance the sense of depth of your 2D lighting. Similar to how these work in 3D rendering, normal maps can help make lighting look less flat by varying its intensity depending on the direction of the surface receiving light (on a per-pixel basis). Specular maps further help improve visuals by making some of the light reflect back to the viewer.

Both PointLight2D and DirectionalLight2D support normal mapping and specular mapping. Normal and specular maps can be assigned to any 2D element, including nodes that inherit from Node2D or Control.

A normal map represents the direction in which each pixel is "pointing" towards. This information is then used by the engine to correctly apply lighting to 2D surfaces in a physically plausible way. Normal maps are typically created from hand-painted height maps, but they can also be automatically generated from other textures.

A specular map defines how much each pixel should reflect light (and in which color, if the specular map contains color). Brighter values will result in a brighter reflection at that given spot on the texture. Specular maps are typically created with manual editing, using the diffuse texture as a base.

> **Tip:** If you don't have normal or specular maps for your sprites, you can generate them using the free and open source [Laigter](https://azagaya.itch.io/laigter) tool.

To set up normal maps and/or specular maps on a 2D node, create a new CanvasTexture resource for the property that draws the node's texture. For example, on a Sprite2D:

Expand the newly created resource. You can find several properties you will need to adjust:

- **Diffuse > Texture:** The base color texture. In this property, load the texture you're using for the sprite itself.
- **Normal Map > Texture:** The normal map texture. In this property, load a normal map texture you've generated from a height map (see the tip above).
- **Specular > Texture:** The specular map texture, which controls the specular intensity of each pixel on the diffuse texture. The specular map is usually grayscale, but it can also contain color to multiply the color of reflections accordingly. In this property, load a specular map texture you've created (see the tip above).
- **Specular > Color:** The color multiplier for specular reflections.
- **Specular > Shininess:** The specular exponent to use for reflections. Lower values will increase the brightness of reflections and make them more diffuse, while higher values will make reflections more localized. High values are more suited for wet-looking surfaces.
- **Texture > Filter:** Can be set to override the texture filtering mode, regardless of what the node's property is set to (or the **Rendering > Textures > Canvas Textures > Default Texture Filter** project setting).
- **Texture > Repeat:** Can be set to override the texture filtering mode, regardless of what the node's property is set to (or the **Rendering > Textures > Canvas Textures > Default Texture Repeat** project setting).

After enabling normal mapping, you may notice that your lights appear to be weaker. To resolve this, increase the **Height** property on your PointLight2D and DirectionalLight2D nodes. You may also want to increase the lights's **Energy** property slightly to get closer to how your lighting's intensity looked prior to enabling normal mapping.

### Using additive sprites as a faster alternative to 2D lights

If you run into performance issues when using 2D lights, it may be worth replacing some of them with Sprite2D nodes that use additive blending. This is particularly suited for short-lived dynamic effects, such as bullets or explosions.

Additive sprites are much faster to render, since they don't need to go through a separate rendering pipeline. Additionally, it is possible to use this approach with AnimatedSprite2D (or Sprite2D + AnimationPlayer), which allows for animated 2D "lights" to be created.

However, additive sprites have a few downsides compared to 2D lights:

- The blending formula is inaccurate compared to "actual" 2D lighting. This is usually not a problem in sufficiently lit areas, but this prevents additive sprites from correctly lighting up areas that are fully dark.
- Additive sprites cannot cast shadows, since they are not lights.
- Additive sprites ignore normal and specular maps used on other sprites.

To display a sprite with additive blending, create a Sprite2D node and assign a texture to it. In the inspector, scroll down to the **CanvasItem > Material** section, unfold it and click the dropdown next to the **Material** property. Choose **New CanvasItemMaterial**, click the newly created material to edit it, then set **Blend Mode** to **Add**.

---

## 2D meshes

> **Work in progress:** The content of this page was not yet updated for Godot `4.6` and may be **outdated**. If you know how to improve this page or you can confirm that it's up to date, feel free to [open a pull request](https://github.com/godotengine/godot-docs).

### Introduction

In 3D, meshes are used to display the world. In 2D, they are rare as images are used more often. Godot's 2D engine is a pure two-dimensional engine, so it can't really display 3D meshes directly (although it can be done via `Viewport` and `ViewportTexture`).

> **See also:** If you are interested in displaying 3D meshes on a 2D viewport, see the [Using a SubViewport as a texture](tutorials_shaders.md) tutorial.

2D meshes are meshes that contain two-dimensional geometry (Z can be omitted or ignored) instead of 3D. You can experiment creating them yourself using `SurfaceTool` from code and displaying them in a `MeshInstance2D` node.

Currently, the only way to generate a 2D mesh within the editor is by either importing an OBJ file as a mesh, or converting it from a Sprite2D.

### Optimizing pixels drawn

This workflow is useful for optimizing 2D drawing in some situations. When drawing large images with transparency, Godot will draw the whole quad to the screen. The large transparent areas will still be drawn.

This can affect performance, especially on mobile devices, when drawing very large images (generally screen sized), or layering multiple images on top of each other with large transparent areas (for example, when using `ParallaxBackground`).

Converting to a mesh will ensure that only the opaque parts will be drawn and the rest will be ignored.

### Converting Sprite2Ds to 2D meshes

You can take advantage of this optimization by converting a `Sprite2D` to a `MeshInstance2D`. Start with an image that contains large amounts of transparency on the edges, like this tree:

Put it in a `Sprite2D` and select "Convert to MeshInstance2D" from the menu:

A dialog will appear, showing a preview of how the 2D mesh will be created:

The default values are good enough for many cases, but you can change growth and simplification according to your needs:

Finally, push the Convert 2D Mesh button and your Sprite2D will be replaced:

---

## 2D movement overview

### Introduction

Every beginner has been there: "How do I move my character?" Depending on the style of game you're making, you may have special requirements, but in general the movement in most 2D games is based on a small number of designs.

We'll use [CharacterBody2D](../godot_gdscript_nodes_2d.md) for these examples, but the principles will apply to other node types (Area2D, RigidBody2D) as well.

### Setup

Each example below uses the same scene setup. Start with a `CharacterBody2D` with two children: `Sprite2D` and `CollisionShape2D`. You can use the Godot icon ("icon.png") for the Sprite2D's texture or use any other 2D image you have.

Open `Project -> Project Settings` and select the "Input Map" tab. Add the following input actions (see [InputEvent](tutorials_inputs.md) for details):

### 8-way movement

In this scenario, you want the user to press the four directional keys (up/left/down/right or W/A/S/D) and move in the selected direction. The name "8-way movement" comes from the fact that the player can move diagonally by pressing two keys at the same time.

Add a script to the character body and add the following code:

```gdscript
extends CharacterBody2D

@export var speed = 400

func get_input():
    var input_direction = Input.get_vector("left", "right", "up", "down")
    velocity = input_direction * speed

func _physics_process(delta):
    get_input()
    move_and_slide()
```

In the `get_input()` function, we use [Input](../godot_gdscript_input.md) `get_vector()` to check for the four key events and sum return a direction vector.

We can then set our velocity by multiplying this direction vector, which has a length of `1`, by our desired speed.

> **Tip:** If you've never used vector math before, or need a refresher, you can see an explanation of vector usage in Godot at [Vector math](tutorials_math.md).

> **Note:** If the code above does nothing when you press the keys, double-check that you've set up input actions correctly as described in the **Setup** part of this tutorial.

### Rotation + movement

This type of movement is sometimes called "Asteroids-style" because it resembles how that classic arcade game worked. Pressing left/right rotates the character, while up/down moves it forward or backward in whatever direction it's facing.

```gdscript
extends CharacterBody2D

@export var speed = 400
@export var rotation_speed = 1.5

var rotation_direction = 0

func get_input():
    rotation_direction = Input.get_axis("left", "right")
    velocity = transform.x * Input.get_axis("down", "up") * speed

func _physics_process(delta):
    get_input()
    rotation += rotation_direction * rotation_speed * delta
    move_and_slide()
```

Here we've added two variables to track our rotation direction and speed. The rotation is applied directly to the body's `rotation` property.

To set the velocity, we use the body's `transform.x` which is a vector pointing in the body's "forward" direction, and multiply that by the speed.

### Rotation + movement (mouse)

This style of movement is a variation of the previous one. This time, the direction is set by the mouse position instead of the keyboard. The character will always "look at" the mouse pointer. The forward/back inputs remain the same, however.

```gdscript
extends CharacterBody2D

@export var speed = 400

func get_input():
    look_at(get_global_mouse_position())
    velocity = transform.x * Input.get_axis("down", "up") * speed

func _physics_process(delta):
    get_input()
    move_and_slide()
```

Here we're using the [Node2D](../godot_gdscript_nodes_2d.md) `look_at()` method to point the player towards the mouse's position. Without this function, you could get the same effect by setting the angle like this:

```gdscript
rotation = get_global_mouse_position().angle_to_point(position)
```

### Click-and-move

This last example uses only the mouse to control the character. Clicking on the screen will cause the player to move to the target location.

```gdscript
extends CharacterBody2D

@export var speed = 400

var target = position

func _input(event):
    # Use is_action_pressed to only accept single taps as input instead of mouse drags.
    if event.is_action_pressed(&"click"):
        target = get_global_mouse_position()

func _physics_process(delta):
    velocity = position.direction_to(target) * speed
    # look_at(target)
    if position.distance_to(target) > 10:
        move_and_slide()
```

Note the `distance_to()` check we make prior to movement. Without this test, the body would "jitter" upon reaching the target position, as it moves slightly past the position and tries to move back, only to move too far and repeat.

Uncommenting the `look_at()` line will also turn the body to point in its direction of motion if you prefer.

> **Tip:** This technique can also be used as the basis of a "following" character. The `target` position can be that of any object you want to move to.

### Summary

You may find these code samples useful as starting points for your own projects. Feel free to use them and experiment with them to see what you can make.

You can download this sample project here: [2d_movement_starter.zip](https://github.com/godotengine/godot-docs-project-starters/releases/download/latest-4.x/2d_movement_starter.zip)

---

## 2D Parallax

### Introduction

Parallax is an effect used to simulate depth by having textures move at different speeds relative to the camera. Godot provides the [Parallax2D](../godot_gdscript_misc.md) node to achieve this effect. It can still be easy to get tripped up though, so this page provides in-depth descriptions of some properties and how to fix some common mistakes.

> **Note:** This page covers how to use [Parallax2D](../godot_gdscript_misc.md), which is recommended to use over the [ParallaxLayer](../godot_gdscript_misc.md) and [ParallaxBackground](../godot_gdscript_misc.md) nodes.

### Getting started

The parallax node supports adding nodes that render things as children, so you can use one or many nodes to make up each layer. To begin, place each node or nodes you want to have scroll independently as a child of their own parallax node. Make sure that the top left of the textures used are at the `(0, 0)` crossing, like in the image below. See the section on **positioning** for why this is important.

The scene above uses one prepared texture for the higher clouds in a [Sprite2D](../godot_gdscript_nodes_2d.md), but you could just as easily use multiple nodes spaced out to compose the layer.

### Scroll scale

The backbone of the parallax effect is the [scroll_scale](../godot_gdscript_misc.md) property. It works as a scroll-speed multiplier, allowing layers to move at a different speed than the camera for each axis set. A value of 1 makes the parallax node scroll at the same speed as the camera. If you want your image to look further away when scrolling, use a value lower than 1, with 0 bringing it to a complete stop. If you want something to appear closer to the camera, use a value higher than 1, making it scroll faster.

The scene above is comprised of five layers. Some good [scroll_scale](../godot_gdscript_misc.md) values might be:

- `(0.7, 1)` - Forest
- `(0.5, 1)` - Hills
- `(0.3, 1)` - Lower Clouds
- `(0.2, 1)` - Higher Clouds
- `(0.1, 1)` - Sky

The video below displays how these values affect scrolling while in-game:

### Infinite repeat

[Parallax2D](../godot_gdscript_misc.md) provides a bonus effect that gives textures the illusion of repeating infinitely. [repeat_size](../godot_gdscript_misc.md) tells the node to snap its position forward or back when the camera scrolls by the set value. This effect is achieved by adding a single repeat to all the child canvas items offset by the value. While the camera scrolls between the image and its repeat, it invisibly snaps back giving the appearance of a looping image.

Being a delicate effect, it's easy for unfamiliar users to make mistakes with their setup. Let's go over the "how" and "why" of a few common problems users encounter.

#### Poor sizing

The infinite repeat effect is easiest to work with when you have an image designed to repeat seamlessly and is the same size or larger than your viewport **before** setting the [repeat_size](../godot_gdscript_misc.md). If you aren't able to obtain assets that are designed for this task, there are some other things you can do to better prepare your image in regards to size.

Here is an example of a texture that is too small for its viewport:

We can see that the viewport size is 500x300 but the texture is 288x208. If we set the [repeat_size](../godot_gdscript_misc.md) to the size of our image, the infinite repeat effect doesn't scroll properly because the original texture doesn't cover the viewport. If we set the [repeat_size](../godot_gdscript_misc.md) to the size of the viewport, we have a large gap. What can we do?

##### Make the viewport smaller

The simplest answer is to make the viewport the same size or smaller than your textures. In **Project Settings > Display > Window**, change the [Viewport Width](../godot_gdscript_rendering.md) and [Viewport Height](../godot_gdscript_rendering.md) settings to match your background.

##### Scale the Parallax2D

If you're not aiming for a pixel-perfect style, or don't mind a little blurriness, you may opt to scale the textures larger to fit your screen. Set the [scale](../godot_gdscript_misc.md) of the [Parallax2D](../godot_gdscript_misc.md), and all child textures scale with it.

##### Scale the child nodes

Similar to scaling the [Parallax2D](../godot_gdscript_misc.md), you can scale your [Sprite2D](../godot_gdscript_nodes_2d.md) nodes to be large enough to cover the screen. Keep in mind that some settings like [Parallax2D.repeat_size](../godot_gdscript_misc.md) and [Sprite2D.region_rect](../godot_gdscript_nodes_2d.md) do not take scaling into account, so it's necessary to adjust these values based on the scale.

##### Repeat the textures

You can also start off on the right foot by preparing child nodes earlier in the process. If you have a [Sprite2D](../godot_gdscript_nodes_2d.md) you'd like to repeat, but is too small, you can do the following to repeat it:

- set [texture_repeat](../godot_gdscript_misc.md) to [CanvasItem.TEXTURE_REPEAT_ENABLED](../godot_gdscript_nodes_2d.md)
- set [region_enabled](../godot_gdscript_misc.md) to `true`
- set the [region_rect](../godot_gdscript_misc.md) to a multiple of the size of your texture large enough to cover the viewport.

Below, you can see that repeating the image twice makes it large enough to cover the screen.

#### Poor positioning

It's common to see users mistakenly set all of their textures to be centered at `(0,0)`:

This creates problems with the infinite repeat effect and should be avoided. The "infinite repeat canvas" starts at `(0,0)` and expands down and to the right to the size of the [repeat_size](../godot_gdscript_misc.md) value.

If the textures are centered on the `(0,0)` crossing, the infinite repeat canvas is only partly covered, so it only partly repeats.

##### Would increasing repeat_times fix this?

Increasing [repeat_times](../godot_gdscript_misc.md) technically _would_ work in some scenarios, but is a brute force solution and not the problem it is designed to solve (we'll go over this in a bit). A better fix is to understand how the repeat effect works and set up the parallax textures appropriately to begin with.

First, check to see if any textures are spilling over onto the negative parts of the canvas. Make sure the textures used in the parallax nodes fit inside the "infinite repeat canvas" starting at `(0,0)`. That way, if [Parallax2D.repeat_size](../godot_gdscript_misc.md) is set correctly, it should look something like this, with one single loop of the image the same size or larger than the viewport:

If you think of how the image scrolls across the screen, it starts by displaying what's inside the red rectangle (determined by [repeat_size](../godot_gdscript_misc.md)), and when it reaches what's inside the yellow rectangle it zips the image forward to give the illusion of scrolling forever.

If you have the image positioned away from the "infinite repeat canvas", when the camera reaches the yellow rectangle, half of the image is cut off before it jumps forward like in the image below:

### Scroll offset

If your parallax textures are already working correctly, but you prefer it to start at a different point, [Parallax2D](../godot_gdscript_misc.md) comes with a [scroll_offset](../godot_gdscript_misc.md) property used to offset where the infinite repeat canvas starts. As an example, if your image is 288x208, setting the [scroll_offset](../godot_gdscript_misc.md) to `(-144,0)` or `(144,0)` allows it to begin halfway across the image.

### Repeat times

Ideally, following this guide, your parallax textures are large enough to cover the screen even when zoomed out. Until now, we have had a perfectly fitting 288x208 texture inside of a 288x208 viewport. However, problems occur when we zoom out by setting the [Camera2D.zoom](../godot_gdscript_nodes_2d.md) to `(0.5, 0.5)`:

Even though everything is correctly set for the viewport at the default zoom level, zooming out makes it smaller than the viewport, breaking the infinite repeat effect. This is where [repeat_times](../godot_gdscript_misc.md) can help out. Setting a value of `3` (one extra repeat behind and in front), it is now large enough to accommodate the infinite repeat effect.

If these textures were meant to be repeated vertically, we would have specified a `y` value for the [repeat_size](../godot_gdscript_misc.md). The [repeat_times](../godot_gdscript_misc.md) would automatically add a repeat above and below as well. This is only a horizontal parallax, so it leaves an empty block above and below the image. How do we solve this? We need to get creative! In this example, we stretch the sky higher, and grass sprite lower. The textures now support the normal zoom level and zooming out to half size.

### Split screen

Most tutorials for making a split screen game in Godot begin by writing a small script to assign the [Viewport.world_2d](../godot_gdscript_rendering.md) of the first SubViewport to the second, so they have a shared display. Questions often pop up about how to share a parallax effect between both screens.

The parallax effect fakes a perspective by moving the positions of different textures in relation to the camera. This is understandably problematic if you have multiple cameras, because your textures can't be in two places at once!

This is still achievable by cloning the parallax nodes into the second (or third or fourth) [SubViewport](../godot_gdscript_rendering.md). Here's how a setup looks for a two player game:

Of course, now both backgrounds show in both SubViewports. What we want is for each parallax to only show in their corresponding viewport. We can achieve this by doing the following:

- Leave all parallax nodes at their default [visibility_layer](../godot_gdscript_misc.md) of 1.
- Set the first SubViewport's [canvas_cull_mask](../godot_gdscript_misc.md) to only layers 1 and 2.
- Do the same for the second SubViewport but use layers 1 and 3.
- Give your parallax nodes in the first SubViewport a common parent and set its [visibility_layer](../godot_gdscript_misc.md) to 2.
- Do the same for the second SubViewport's parallax nodes, but use a layer of 3.

How does this work? If a canvas item has a [visibility_layer](../godot_gdscript_misc.md) that doesn't match the SubViewport's [canvas_cull_mask](../godot_gdscript_misc.md), it will hide all children, even if they do. We use this to our advantage, letting the SubViewports cut off rendering of parallax nodes whose parent doesn't have a supported [visibility_layer](../godot_gdscript_misc.md).

### Previewing in the editor

Prior to 4.3, the recommendation was to place every layer in their own [ParallaxBackground](../godot_gdscript_misc.md), enable the [follow_viewport_enabled](../godot_gdscript_misc.md) property, and scale the individual layer. This method has always been tricky to get right, but is still achievable by using a [CanvasLayer](../godot_gdscript_nodes_2d.md) instead of a [ParallaxBackground](../godot_gdscript_misc.md).

> **Note:** Another recommendation is [KoBeWi's "Parallax2D Preview" addon](https://github.com/KoBeWi/Godot-Parallax2D-Preview). It provides a few different preview modes and is very handy!

---

## 2D sprite animation

### Introduction

In this tutorial, you'll learn how to create 2D animated characters with the AnimatedSprite2D class and the AnimationPlayer. Typically, when you create or download an animated character, it will come in one of two ways: as individual images or as a single sprite sheet containing all the animation's frames. Both can be animated in Godot with the AnimatedSprite2D class.

First, we'll use [AnimatedSprite2D](../godot_gdscript_nodes_2d.md) to animate a collection of individual images. Then we will animate a sprite sheet using this class. Finally, we will learn another way to animate a sprite sheet with [AnimationPlayer](../godot_gdscript_resources.md) and the _Animation_ property of [Sprite2D](../godot_gdscript_nodes_2d.md).

> **Note:** Art for the following examples by [https://opengameart.org/users/ansimuz](https://opengameart.org/users/ansimuz) and tgfcoder.

### Individual images with AnimatedSprite2D

In this scenario, you have a collection of images, each containing one of your character's animation frames. For this example, we'll use the following animation:

You can download the images here: [2d_sprite_animation_assets.zip](https://github.com/godotengine/godot-docs-project-starters/releases/download/latest-4.x/2d_sprite_animation_assets.zip)

Unzip the images and place them in your project folder. Set up your scene tree with the following nodes:

> **Note:** The root node could also be [Area2D](../godot_gdscript_physics.md) or [RigidBody2D](../godot_gdscript_nodes_2d.md). The animation will still be made in the same way. Once the animation is completed, you can assign a shape to the CollisionShape2D. See [Physics Introduction](tutorials_physics.md) for more information.

Now select the `AnimatedSprite2D` and in its _SpriteFrames_ property, select "New SpriteFrames".

Click on the new SpriteFrames resource and you'll see a new panel appear at the bottom of the editor window:

From the FileSystem dock on the left side, drag the 8 individual images into the center part of the SpriteFrames panel. On the left side, change the name of the animation from "default" to "run".

Use the "Play" buttons on the top-right of the _Filter Animations_ input to preview the animation. You should now see the animation playing in the viewport. However, it is a bit slow. To fix this, change the _Speed (FPS)_ setting in the SpriteFrames panel to 10.

You can add additional animations by clicking the "Add Animation" button and adding additional images.

#### Controlling the animation

Once the animation is complete, you can control the animation via code using the `play()` and `stop()` methods. Here is a brief example to play the animation while the right arrow key is held, and stop it when the key is released.

```gdscript
extends CharacterBody2D

@onready var _animated_sprite = $AnimatedSprite2D

func _process(_delta):
    if Input.is_action_pressed("ui_right"):
        _animated_sprite.play("run")
    else:
        _animated_sprite.stop()
```

### Sprite sheet with AnimatedSprite2D

You can also easily animate from a sprite sheet with the class `AnimatedSprite2D`. We will use this public domain sprite sheet:

Right-click the image and choose "Save Image As" to download it, and then copy the image into your project folder.

Set up your scene tree the same way you did previously when using individual images. Select the `AnimatedSprite2D` and in its _SpriteFrames_ property, select "New SpriteFrames".

Click on the new SpriteFrames resource. This time, when the bottom panel appears, select "Add frames from a Sprite Sheet".

You will be prompted to open a file. Select your sprite sheet.

A new window will open, showing your sprite sheet. The first thing you will need to do is to change the number of vertical and horizontal images in your sprite sheet. In this sprite sheet, we have four images horizontally and two images vertically.

Next, select the frames from the sprite sheet that you want to include in your animation. We will select the top four, then click "Add 4 frames" to create the animation.

You will now see your animation under the list of animations in the bottom panel. Double click on default to change the name of the animation to jump.

Finally, check the play button on the SpriteFrames editor to see your frog jump!

### Sprite sheet with AnimationPlayer

Another way that you can animate when using a sprite sheet is to use a standard [Sprite2D](../godot_gdscript_nodes_2d.md) node to display the texture, and then animating the change from texture to texture with [AnimationPlayer](../godot_gdscript_resources.md).

Consider this sprite sheet, which contains 6 frames of animation:

Right-click the image and choose "Save Image As" to download, then copy the image into your project folder.

Our goal is to display these images one after another in a loop. Start by setting up your scene tree:

> **Note:** The root node could also be [Area2D](../godot_gdscript_physics.md) or [RigidBody2D](../godot_gdscript_nodes_2d.md). The animation will still be made in the same way. Once the animation is completed, you can assign a shape to the CollisionShape2D. See [Physics Introduction](tutorials_physics.md) for more information.

Drag the spritesheet into the Sprite's _Texture_ property, and you'll see the whole sheet displayed on the screen. To slice it up into individual frames, expand the _Animation_ section in the Inspector and set the _Hframes_ to `6`. _Hframes_ and _Vframes_ are the number of horizontal and vertical frames in your sprite sheet.

Now try changing the value of the _Frame_ property. You'll see that it ranges from `0` to `5` and the image displayed by the Sprite2D changes accordingly. This is the property we'll be animating.

Select the `AnimationPlayer` and click the "Animation" button followed by "New". Name the new animation "walk". Set the animation length to `0.6` and click the "Loop" button so that our animation will repeat.

Now select the `Sprite2D` node and click the key icon to add a new track.

Continue adding frames at each point in the timeline (`0.1` seconds by default), until you have all the frames from 0 to 5. You'll see the frames actually appearing in the animation track:

Press "Play" on the animation to see how it looks.

#### Controlling an AnimationPlayer animation

Like with AnimatedSprite2D, you can control the animation via code using the `play()` and `stop()` methods. Again, here is an example to play the animation while the right arrow key is held, and stop it when the key is released.

```gdscript
extends CharacterBody2D

@onready var _animation_player = $AnimationPlayer

func _process(_delta):
    if Input.is_action_pressed("ui_right"):
        _animation_player.play("walk")
    else:
        _animation_player.stop()
```

> **Note:** If updating both an animation and a separate property at once (for example, a platformer may update the sprite's `h_flip`/`v_flip` properties when a character turns while starting a 'turning' animation), it's important to keep in mind that `play()` isn't applied instantly. Instead, it's applied the next time the [AnimationPlayer](../godot_gdscript_resources.md) is processed. This may end up being on the next frame, causing a 'glitch' frame, where the property change was applied, but the animation was not. If this turns out to be a problem, after calling `play()`, you can call `advance(0)` to update the animation immediately.

### Summary

These examples illustrate the two classes you can use in Godot for 2D animation. `AnimationPlayer` is a bit more complex than `AnimatedSprite2D`, but it provides additional functionality, since you can also animate other properties like position or scale. The class `AnimationPlayer` can also be used with an `AnimatedSprite2D`. Experiment to see what works best for your needs.

---

## Viewport and canvas transforms

### Introduction

This is an overview of the 2D transforms going on for nodes from the moment they draw their content locally to the time they are drawn onto the screen. This overview discusses very low-level details of the engine.

The goal of this tutorial is to teach a way for feeding input events to the Input with a position in the correct coordinate system.

A more extensive description of all coordinate systems and 2d transforms is available in 2D coordinate systems and 2D transforms.

### Canvas transform

As mentioned in the previous tutorial, Canvas layers, every CanvasItem node (remember that Node2D and Control based nodes use CanvasItem as their common root) will reside in a _Canvas Layer_. Every canvas layer has a transform (translation, rotation, scale, etc.) that can be accessed as a [Transform2D](../godot_gdscript_math_types.md).

Also covered in the previous tutorial, nodes are drawn by default in Layer 0, in the built-in canvas. To put nodes in a different layer, a [CanvasLayer](../godot_gdscript_nodes_2d.md) node can be used.

### Global canvas transform

Viewports also have a Global Canvas transform (also a [Transform2D](../godot_gdscript_math_types.md)). This is the master transform and affects all individual _Canvas Layer_ transforms. Generally, this is primarily used in Godot's CanvasItem Editor.

### Stretch transform

Finally, viewports have a _Stretch Transform_, which is used when resizing or stretching the screen. This transform is used internally (as described in [Multiple resolutions](tutorials_rendering.md)), but can also be manually set on each viewport.

Input events are multiplied by this transform, but lack the ones above. To convert InputEvent coordinates to local CanvasItem coordinates, the [CanvasItem.make_input_local()](../godot_gdscript_nodes_2d.md) function was added for convenience.

### Window transform

The root viewport is a [Window](../godot_gdscript_ui_controls.md). In order to scale and position the _Window's_ content as described in [Multiple resolutions](tutorials_rendering.md), each [Window](../godot_gdscript_ui_controls.md) contains a _window transform_. It is for example responsible for the black bars at the _Window's_ sides so that the _Viewport_ is displayed with a fixed aspect ratio.

### Transform order

To convert a CanvasItem local coordinate to an actual screen coordinate, the following chain of transforms must be applied:

### Transform functions

The above graphic shows some available transform functions. All transforms are directed from right to left, this means multiplying a transform with a coordinate results in a coordinate system further to the left, multiplying the [affine inverse](../godot_gdscript_misc.md) of a transform results in a coordinate system further to the right:

```gdscript
# Called from a CanvasItem.
canvas_pos = get_global_transform() * local_pos
local_pos = get_global_transform().affine_inverse() * canvas_pos
```

Finally, then, to convert a CanvasItem local coordinates to screen coordinates, just multiply in the following order:

```gdscript
var screen_coord = get_viewport().get_screen_transform() * get_global_transform_with_canvas() * local_pos
```

Keep in mind, however, that it is generally not desired to work with screen coordinates. The recommended approach is to simply work in Canvas coordinates (`CanvasItem.get_global_transform()`), to allow automatic screen resolution resizing to work properly.

### Feeding custom input events

It is often desired to feed custom input events to the game. With the above knowledge, to correctly do this in the focused window, it must be done the following way:

```gdscript
var local_pos = Vector2(10, 20) # Local to Control/Node2D.
var ie = InputEventMouseButton.new()
ie.button_index = MOUSE_BUTTON_LEFT
ie.position = get_viewport().get_screen_transform() * get_global_transform_with_canvas() * local_pos
Input.parse_input_event(ie)
```

---

## Canvas layers

### Viewport and Canvas items

[CanvasItem](../godot_gdscript_nodes_2d.md) is the base for all 2D nodes, be it regular 2D nodes, such as [Node2D](../godot_gdscript_nodes_2d.md), or [Control](../godot_gdscript_ui_controls.md). Both inherit from [CanvasItem](../godot_gdscript_nodes_2d.md). You can arrange canvas items in trees. Each item will inherit its parent's transform: when the parent moves, its children move too.

CanvasItem nodes, and nodes inheriting from them, are direct or indirect children of a [Viewport](../godot_gdscript_rendering.md), that displays them.

The Viewport's property [Viewport.canvas_transform](../godot_gdscript_rendering.md), allows to apply a custom [Transform2D](../godot_gdscript_math_types.md) transform to the CanvasItem hierarchy it contains. Nodes such as [Camera2D](../godot_gdscript_nodes_2d.md) work by changing that transform.

To achieve effects like scrolling, manipulating the canvas transform property is more efficient than moving the root canvas item and the entire scene with it.

Usually though, we don't want _everything_ in the game or app to be subject to the canvas transform. For example:

- **Parallax Backgrounds**: Backgrounds that move slower than the rest of the stage.
- **UI**: Think of a user interface (UI) or head-up display (HUD) superimposed on our view of the game world. We want a life counter, score display and other elements to retain their screen positions even when our view of the game world changes.
- **Transitions**: We may want visual effects used for transitions (fades, blends) to remain at a fixed screen location.

How to solve these problems in a single scene tree?

### CanvasLayers

The answer is [CanvasLayer](../godot_gdscript_nodes_2d.md), which is a node that adds a separate 2D rendering layer for all its children and grand-children. Viewport children will draw by default at layer "0", while a CanvasLayer will draw at any numeric layer. Layers with a greater number will be drawn above those with a smaller number. CanvasLayers also have their own transform and do not depend on the transform of other layers. This allows the UI to be fixed in screen-space while our view on the game world changes.

An example of this is creating a parallax background. This can be done with a CanvasLayer at layer "-1". The screen with the points, life counter and pause button can also be created at layer "1".

Here's a diagram of how it looks:

CanvasLayers are independent of tree order, and they only depend on their layer number, so they can be instantiated when needed.

> **Note:** CanvasLayers aren't necessary to control the drawing order of nodes. The standard way to ensuring that a node is correctly drawn 'in front' or 'behind' others is to manipulate the order of the nodes in the scene panel. Perhaps counterintuitively, the topmost nodes in the scene panel are drawn on _behind_ lower ones in the viewport. 2D nodes also have the [CanvasItem.z_index](../godot_gdscript_nodes_2d.md) property for controlling their drawing order.

---
