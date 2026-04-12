# Godot 4 GDScript Tutorials — Shaders (Part 2)

> 3 tutorials. GDScript-specific code examples.

## CanvasItem shaders

CanvasItem shaders are used to draw all 2D elements in Godot. These include all nodes that inherit from CanvasItems, and all GUI elements.

CanvasItem shaders contain fewer built-in variables and functionality than Spatial shaders, but they maintain the same basic structure with vertex, fragment, and light processor functions.

### Render modes

| Render mode           | Description                                                       |
| --------------------- | ----------------------------------------------------------------- |
| blend_mix             | Mix blend mode (alpha is transparency), default.                  |
| blend_add             | Additive blend mode.                                              |
| blend_sub             | Subtractive blend mode.                                           |
| blend_mul             | Multiplicative blend mode.                                        |
| blend_premul_alpha    | Pre-multiplied alpha blend mode.                                  |
| blend_disabled        | Disable blending, values (including alpha) are written as-is.     |
| unshaded              | Result is just albedo. No lighting/shading happens in material.   |
| light_only            | Only draw in the light pass.                                      |
| skip_vertex_transform | VERTEX needs to be transformed manually in the vertex() function. |
| world_vertex_coords   | VERTEX is modified in world coordinates instead of local.         |

### Built-ins

Values marked as `in` are read-only. Values marked as `out` can optionally be written to and will not necessarily contain sensible values. Values marked as `inout` provide a sensible default value, and can optionally be written to. Samplers cannot be written to so they are not marked.

Not all built-ins are available in all processing functions. To access a vertex built-in from the `fragment()` function, you can use a varying. The same applies for accessing fragment built-ins from the `light()` function.

### Global built-ins

Global built-ins are available everywhere, including custom functions.

| Built-in      | Description                                                                                                                                                                                                                                                                                                               |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| in float TIME | Global time since the engine has started, in seconds. It repeats after every 3,600 seconds (which can be changed with the rollover setting). It's affected by time_scale but not by pausing. If you need a TIME variable that is not affected by time scale, add your own global shader uniform and update it each frame. |
| in float PI   | A PI constant (3.141592). The ratio of a circle's circumference to its diameter and the number of radians in a half turn.                                                                                                                                                                                                 |
| in float TAU  | A TAU constant (6.283185). Equivalent to PI \* 2 and the number of radians in a full turn.                                                                                                                                                                                                                                |
| in float E    | An E constant (2.718281). Euler's number, the base of the natural logarithm.                                                                                                                                                                                                                                              |

### Vertex built-ins

Vertex data (`VERTEX`) is presented in local space (pixel coordinates, relative to the Node2D's origin). If not written to, these values will not be modified and be passed through as they came.

The user can disable the built-in model to world transform (world to screen and projection will still happen later) and do it manually with the following code:

```glsl
shader_type canvas_item;
render_mode skip_vertex_transform;

void vertex() {

    VERTEX = (MODEL_MATRIX * vec4(VERTEX, 0.0, 1.0)).xy;
}
```

Other built-ins, such as `UV` and `COLOR`, are also passed through to the `fragment()` function if not modified.

For instancing, the `INSTANCE_CUSTOM` variable contains the instance custom data. When using particles, this information is usually:

- **x**: Rotation angle in radians.
- **y**: Phase during lifetime (`0.0` to `1.0`).
- **z**: Animation frame.

| Built-in                   | Description                                                                                                                                                      |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| in mat4 MODEL_MATRIX       | Local space to world space transform. World space is the coordinates you normally use in the editor.                                                             |
| in mat4 CANVAS_MATRIX      | World space to canvas space transform. In canvas space the origin is the upper-left corner of the screen and coordinates range from (0.0, 0.0) to viewport size. |
| in mat4 SCREEN_MATRIX      | Canvas space to clip space transform. In clip space coordinates range from (-1.0, -1.0) to (1.0, 1.0).                                                           |
| in int INSTANCE_ID         | Instance ID for instancing.                                                                                                                                      |
| in vec4 INSTANCE_CUSTOM    | Instance custom data.                                                                                                                                            |
| in bool AT_LIGHT_PASS      | Always false.                                                                                                                                                    |
| in vec2 TEXTURE_PIXEL_SIZE | Normalized pixel size of the default 2D texture. For a Sprite2D with a texture of size 64x32px, TEXTURE_PIXEL_SIZE = vec2(1.0/64.0, 1.0/32.0)                    |
| inout vec2 VERTEX          | Vertex position, in local space.                                                                                                                                 |
| in int VERTEX_ID           | The index of the current vertex in the vertex buffer.                                                                                                            |
| inout vec2 UV              | Normalized texture coordinates. Range from 0.0 to 1.0.                                                                                                           |
| inout vec4 COLOR           | Color from vertex primitive multiplied by the CanvasItem's modulate multiplied by CanvasItem's self_modulate.                                                    |
| inout float POINT_SIZE     | Point size for point drawing.                                                                                                                                    |
| in vec4 CUSTOM0            | Custom value from vertex primitive.                                                                                                                              |
| in vec4 CUSTOM1            | Custom value from vertex primitive.                                                                                                                              |

### Fragment built-ins

#### COLOR and TEXTURE

The built-in variable `COLOR` is used for a few things:

- In the `vertex()` function, `COLOR` contains the color from the vertex primitive multiplied by the CanvasItem's [modulate](../godot_gdscript_misc.md) multiplied by the CanvasItem's [self_modulate](../godot_gdscript_misc.md).
- In the `fragment()` function, the input value `COLOR` is that same value multiplied by the color from the default `TEXTURE` (if present).
- In the `fragment()` function, `COLOR` is also the final output.

Certain nodes (for example, [Sprite2D](../godot_gdscript_nodes_2d.md)) display a texture by default, for example [texture](../godot_gdscript_misc.md). When using a custom `fragment()` function, you have a few options on how to sample this texture.

To read only the contents of the default texture, ignoring the vertex `COLOR`:

```glsl
void fragment() {
  COLOR = texture(TEXTURE, UV);
}
```

To read the contents of the default texture multiplied by vertex `COLOR`:

```glsl
void fragment() {
  // Equivalent to an empty fragment() function, since COLOR is also the output variable.
  COLOR = COLOR;
}
```

To read only the vertex `COLOR` in `fragment()`, ignoring the main texture, you must pass `COLOR` as a varying, then read it in `fragment()`:

```glsl
varying vec4 vertex_color;
void vertex() {
  vertex_color = COLOR;
}
void fragment() {
  COLOR = vertex_color;
}
```

#### NORMAL

Similarly, if a normal map is used in the [CanvasTexture](../godot_gdscript_misc.md), Godot uses it by default and assigns its value to the built-in `NORMAL` variable. If you are using a normal map meant for use in 3D, it will appear inverted. In order to use it in your shader, you must assign it to the `NORMAL_MAP` property. Godot will handle converting it for use in 2D and overwriting `NORMAL`.

```glsl
NORMAL_MAP = texture(NORMAL_TEXTURE, UV).rgb;
```

| Built-in                             | Description                                                                                                                                                                                     |
| ------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| in vec4 FRAGCOORD                    | Coordinate of pixel center. In screen space. xy specifies position in viewport. Upper-left of the viewport is the origin, (0.0, 0.0).                                                           |
| in vec2 SCREEN_PIXEL_SIZE            | Size of individual pixels. Equal to the inverse of resolution.                                                                                                                                  |
| in vec4 REGION_RECT                  | Visible area of the sprite region in format (x, y, width, height). Varies according to Sprite2D's region_enabled property.                                                                      |
| in vec2 POINT_COORD                  | Coordinate for drawing points.                                                                                                                                                                  |
| sampler2D TEXTURE                    | Default 2D texture.                                                                                                                                                                             |
| in vec2 TEXTURE_PIXEL_SIZE           | Normalized pixel size of the default 2D texture. For a Sprite2D with a texture of size 64x32px, TEXTURE_PIXEL_SIZE = vec2(1/64, 1/32)                                                           |
| in bool AT_LIGHT_PASS                | Always false.                                                                                                                                                                                   |
| sampler2D SPECULAR_SHININESS_TEXTURE | Specular shininess texture of this object.                                                                                                                                                      |
| in vec4 SPECULAR_SHININESS           | Specular shininess color, as sampled from the texture.                                                                                                                                          |
| in vec2 UV                           | UV from the vertex() function. For a Sprite2D with region enabled, this will sample the entire texture. Use REGION_RECT instead to sample only the region defined in the Sprite2D's properties. |
| in vec2 SCREEN_UV                    | Screen UV coordinate for the current pixel.                                                                                                                                                     |
| sampler2D SCREEN_TEXTURE             | Removed in Godot 4. Use a sampler2D with hint_screen_texture instead.                                                                                                                           |
| inout vec3 NORMAL                    | Normal read from NORMAL_TEXTURE. Writable.                                                                                                                                                      |
| sampler2D NORMAL_TEXTURE             | Default 2D normal texture.                                                                                                                                                                      |
| out vec3 NORMAL_MAP                  | Configures normal maps meant for 3D for use in 2D. If used, overrides NORMAL.                                                                                                                   |
| out float NORMAL_MAP_DEPTH           | Normal map depth for scaling.                                                                                                                                                                   |
| inout vec2 VERTEX                    | Pixel position in screen space.                                                                                                                                                                 |
| inout vec2 SHADOW_VERTEX             | Same as VERTEX but can be written to alter shadows.                                                                                                                                             |
| inout vec3 LIGHT_VERTEX              | Same as VERTEX but can be written to alter lighting. Z component represents height.                                                                                                             |
| inout vec4 COLOR                     | COLOR from the vertex() function multiplied by the TEXTURE color. Also output color value.                                                                                                      |

### Light built-ins

Light processor functions work differently in Godot 4.x than they did in Godot 3.x. In Godot 4.x all lighting is done during the regular draw pass. In other words, Godot no longer draws the object again for each light.

Use the `unshaded` render mode if you do not want the `light()` function to run. Use the `light_only` render mode if you only want to see the impact of lighting on an object; this can be useful when you only want the object visible where it is covered by light.

If you define a `light()` function it will replace the built-in light function, even if your light function is empty.

Below is an example of a light shader that takes a CanvasItem's normal map into account:

```glsl
void light() {
  float cNdotL = max(0.0, dot(NORMAL, LIGHT_DIRECTION));
  LIGHT = vec4(LIGHT_COLOR.rgb * COLOR.rgb * LIGHT_ENERGY * cNdotL, LIGHT_COLOR.a);
}
```

| Built-in                     | Description                                                                                                                           |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| in vec4 FRAGCOORD            | Coordinate of pixel center. In screen space. xy specifies position in viewport. Upper-left of the viewport is the origin, (0.0, 0.0). |
| in vec3 NORMAL               | Input normal.                                                                                                                         |
| in vec4 COLOR                | Input color. This is the output of the fragment() function.                                                                           |
| in vec2 UV                   | UV from the vertex() function, equivalent to the UV in the fragment() function.                                                       |
| sampler2D TEXTURE            | Current texture in use for the CanvasItem.                                                                                            |
| in vec2 TEXTURE_PIXEL_SIZE   | Normalized pixel size of TEXTURE. For a Sprite2D with a TEXTURE of size 64x32 pixels, TEXTURE_PIXEL_SIZE = vec2(1/64, 1/32)           |
| in vec2 SCREEN_UV            | Screen UV coordinate for the current pixel.                                                                                           |
| in vec2 POINT_COORD          | UV for Point Sprite.                                                                                                                  |
| in vec4 LIGHT_COLOR          | Color of the Light2D. If the light is a PointLight2D, multiplied by the light's texture.                                              |
| in float LIGHT_ENERGY        | Energy multiplier of the Light2D.                                                                                                     |
| in vec3 LIGHT_POSITION       | Position of the Light2D in screen space. If using a DirectionalLight2D this is always (0.0, 0.0, 0.0).                                |
| in vec3 LIGHT_DIRECTION      | Direction of the Light2D in screen space.                                                                                             |
| in bool LIGHT_IS_DIRECTIONAL | true if this pass is a DirectionalLight2D.                                                                                            |
| in vec3 LIGHT_VERTEX         | Pixel position, in screen space as modified in the fragment() function.                                                               |
| inout vec4 LIGHT             | Output color for this Light2D.                                                                                                        |
| in vec4 SPECULAR_SHININESS   | Specular shininess, as set in the object's texture.                                                                                   |
| out vec4 SHADOW_MODULATE     | Multiply shadows cast at this point by this color.                                                                                    |

### SDF functions

There are a few additional functions implemented to sample an automatically generated Signed Distance Field texture. These functions are available in the `fragment()` and `light()` functions of CanvasItem shaders. Custom functions may also use them as long as they are called from supported functions.

The signed distance field is generated from [LightOccluder2D](../godot_gdscript_nodes_2d.md) nodes present in the scene with the **SDF Collision** property enabled (which is the default). See the [2D lights and shadows](tutorials_2d.md) documentation for more information.

| Function                               | Description                               |
| -------------------------------------- | ----------------------------------------- |
| float texture_sdf (vec2 sdf_pos)       | Performs an SDF texture lookup.           |
| vec2 texture_sdf_normal (vec2 sdf_pos) | Calculates a normal from the SDF texture. |
| vec2 sdf_to_screen_uv (vec2 sdf_pos)   | Converts an SDF to screen UV.             |
| vec2 screen_uv_to_sdf (vec2 uv)        | Converts screen UV to an SDF.             |

---

## Fog shaders

Fog shaders are used to define how fog is added to (or subtracted from) a scene in a given area. Fog shaders are always used together with [FogVolumes](../godot_gdscript_nodes_3d.md) and volumetric fog. Fog shaders only have one processing function, the `fog()` function.

The resolution of the fog shaders depends on the resolution of the volumetric fog froxel grid. Accordingly, the level of detail that a fog shader can add depends on how close the [FogVolume](../godot_gdscript_nodes_3d.md) is to the camera.

Fog shaders are a special form of compute shader that is called once for every froxel that is touched by an axis-aligned bounding box of the associated [FogVolume](../godot_gdscript_nodes_3d.md). This means that froxels that just barely touch a given [FogVolume](../godot_gdscript_nodes_3d.md) will still be used.

### Built-ins

Values marked as `in` are read-only. Values marked as `out` can optionally be written to and will not necessarily contain sensible values. Samplers cannot be written to so they are not marked.

### Global built-ins

Global built-ins are available everywhere, including in custom functions.

| Built-in      | Description                                                                                                                                                                                                                                                                                                               |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| in float TIME | Global time since the engine has started, in seconds. It repeats after every 3,600 seconds (which can be changed with the rollover setting). It's affected by time_scale but not by pausing. If you need a TIME variable that is not affected by time scale, add your own global shader uniform and update it each frame. |
| in float PI   | A PI constant (3.141592). The ratio of a circle's circumference to its diameter and the number of radians in a half turn.                                                                                                                                                                                                 |
| in float TAU  | A TAU constant (6.283185). Equivalent to PI \* 2 and the number of radians in a full turn.                                                                                                                                                                                                                                |
| in float E    | An E constant (2.718281). Euler's number, the base of the natural logarithm.                                                                                                                                                                                                                                              |

### Fog built-ins

All of the output values of fog volumes overlap one another. This allows [FogVolumes](../godot_gdscript_nodes_3d.md) to be rendered efficiently as they can all be drawn at once.

| Built-in                | Description                                                                                                                                       |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| in vec3 WORLD_POSITION  | Position of current froxel cell in world space.                                                                                                   |
| in vec3 OBJECT_POSITION | Position of the center of the current FogVolume in world space.                                                                                   |
| in vec3 UVW             | 3-dimensional UV, used to map a 3D texture to the current FogVolume.                                                                              |
| in vec3 SIZE            | Size of the current FogVolume when its shape has a size.                                                                                          |
| in vec3 SDF             | Signed distance field to the surface of the FogVolume. Negative if inside volume, positive otherwise.                                             |
| out vec3 ALBEDO         | Output base color value, interacts with light to produce final color. Only written to fog volume if used.                                         |
| out float DENSITY       | Output density value. Can be negative to allow subtracting one volume from another. Density must be used for fog shader to write anything at all. |
| out vec3 EMISSION       | Output emission color value, added to color during light pass to produce final color. Only written to fog volume if used.                         |

---

## Particle shaders

Particle shaders are a special type of shader that runs before the object is drawn. They are used for calculating material properties such as color, position, and rotation. They can be drawn with any regular material for CanvasItem or Spatial, depending on whether they are 2D or 3D.

Particle shaders are unique because they are not used to draw the object itself; they are used to calculate particle properties, which are then used by a CanvasItem or Spatial shader. They contain two processor functions: `start()` and `process()`.

Unlike other shader types, particle shaders keep the data that was output the previous frame. Therefore, particle shaders can be used for complex effects that take place over multiple frames.

> **Note:** Particle shaders are only available with GPU-based particle nodes ([GPUParticles2D](../godot_gdscript_nodes_2d.md) and [GPUParticles3D](../godot_gdscript_misc.md)). CPU-based particle nodes ([CPUParticles2D](../godot_gdscript_nodes_2d.md) and [CPUParticles3D](../godot_gdscript_misc.md)) are _rendered_ on the GPU (which means they can use custom CanvasItem or Spatial shaders), but their motion is _simulated_ on the CPU.

### Render modes

| Render mode         | Description                               |
| ------------------- | ----------------------------------------- |
| keep_data           | Do not clear previous data on restart.    |
| disable_force       | Disable attractor force.                  |
| disable_velocity    | Ignore VELOCITY value.                    |
| collision_use_scale | Scale the particle's size for collisions. |

### Built-ins

Values marked as `in` are read-only. Values marked as `out` can optionally be written to and will not necessarily contain sensible values. Values marked as `inout` provide a sensible default value, and can optionally be written to. Samplers cannot be written to so they are not marked.

### Global built-ins

Global built-ins are available everywhere, including custom functions.

| Built-in      | Description                                                                                                                                                                                                                                                                                                               |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| in float TIME | Global time since the engine has started, in seconds. It repeats after every 3,600 seconds (which can be changed with the rollover setting). It's affected by time_scale but not by pausing. If you need a TIME variable that is not affected by time scale, add your own global shader uniform and update it each frame. |
| in float PI   | A PI constant (3.141592). The ratio of a circle's circumference to its diameter and the number of radians in a half turn.                                                                                                                                                                                                 |
| in float TAU  | A TAU constant (6.283185). Equivalent to PI \* 2 and the number of radians in a full turn.                                                                                                                                                                                                                                |
| in float E    | An E constant (2.718281). Euler's number, the base of the natural logarithm.                                                                                                                                                                                                                                              |

### Start and Process built-ins

These properties can be accessed from both the `start()` and `process()` functions.

| Function                    | Description                                                                                                                                                                                                         |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| in float LIFETIME           | Particle lifetime.                                                                                                                                                                                                  |
| in float DELTA              | Delta process time.                                                                                                                                                                                                 |
| in uint NUMBER              | Unique number since emission start.                                                                                                                                                                                 |
| in uint INDEX               | Particle index (from total particles).                                                                                                                                                                              |
| in mat4 EMISSION_TRANSFORM  | Emitter transform (used for non-local systems).                                                                                                                                                                     |
| in uint RANDOM_SEED         | Random seed used as base for random.                                                                                                                                                                                |
| inout bool ACTIVE           | true when the particle is active, can be set to false.                                                                                                                                                              |
| inout vec4 COLOR            | Particle color, can be written to and accessed in the mesh's vertex function.                                                                                                                                       |
| inout vec3 VELOCITY         | Particle velocity, can be modified.                                                                                                                                                                                 |
| inout mat4 TRANSFORM        | Particle transform.                                                                                                                                                                                                 |
| inout vec4 CUSTOM           | Custom particle data. Accessible from the mesh's shader as INSTANCE_CUSTOM.                                                                                                                                         |
| inout float MASS            | Particle mass, intended to be used with attractors. 1.0 by default.                                                                                                                                                 |
| in vec4 USERDATAX           | Vector that enables the integration of supplementary user-defined data into the particle process shader. USERDATAX are six built-ins identified by number, X can be numbers between 1 and 6, for example USERDATA3. |
| in uint FLAG_EMIT_POSITION  | A flag for the last argument of the emit_subparticle() function to assign a position to a new particle's transform.                                                                                                 |
| in uint FLAG_EMIT_ROT_SCALE | A flag for the last argument of the emit_subparticle() function to assign a rotation and scale to a new particle's transform.                                                                                       |
| in uint FLAG_EMIT_VELOCITY  | A flag for the last argument of the emit_subparticle() function to assign a velocity to a new particle.                                                                                                             |
| in uint FLAG_EMIT_COLOR     | A flag for the last argument of the emit_subparticle() function to assign a color to a new particle.                                                                                                                |
| in uint FLAG_EMIT_CUSTOM    | A flag for the last argument of the emit_subparticle() function to assign a custom data vector to a new particle.                                                                                                   |
| in vec3 EMITTER_VELOCITY    | Velocity of the Particles2D (3D) node.                                                                                                                                                                              |
| in float INTERPOLATE_TO_END | Value of the interp_to_end (3D) property of the Particles node.                                                                                                                                                     |
| in uint AMOUNT_RATIO        | Value of the amount_ratio (3D) property of the Particles node.                                                                                                                                                      |

> **Note:** In order to use the `COLOR` variable in a StandardMaterial3D, set `vertex_color_use_as_albedo` to `true`. In a ShaderMaterial, access it with the `COLOR` variable.

### Start built-ins

| Built-in                  | Description                                                                                                                                                               |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| in bool RESTART_POSITION  | true if particle is restarted, or emitted without a custom position (i.e. this particle was created by emit_subparticle() without the FLAG_EMIT_POSITION flag).           |
| in bool RESTART_ROT_SCALE | true if particle is restarted, or emitted without a custom rotation or scale (i.e. this particle was created by emit_subparticle() without the FLAG_EMIT_ROT_SCALE flag). |
| in bool RESTART_VELOCITY  | true if particle is restarted, or emitted without a custom velocity (i.e. this particle was created by emit_subparticle() without the FLAG_EMIT_VELOCITY flag).           |
| in bool RESTART_COLOR     | true if particle is restarted, or emitted without a custom color (i.e. this particle was created by emit_subparticle() without the FLAG_EMIT_COLOR flag).                 |
| in bool RESTART_CUSTOM    | true if particle is restarted, or emitted without a custom property (i.e. this particle was created by emit_subparticle() without the FLAG_EMIT_CUSTOM flag).             |

### Process built-ins

| Built-in                 | Description                                                                                         |
| ------------------------ | --------------------------------------------------------------------------------------------------- |
| in bool RESTART          | true if the current process frame is the first for the particle.                                    |
| in bool COLLIDED         | true when the particle has collided with a particle collider.                                       |
| in vec3 COLLISION_NORMAL | A normal of the last collision. If there is no collision detected it is equal to (0.0, 0.0, 0.0).   |
| in float COLLISION_DEPTH | A length of the normal of the last collision. If there is no collision detected it is equal to 0.0. |
| in vec3 ATTRACTOR_FORCE  | A combined force of the attractors at the moment on that particle.                                  |

### Process functions

`emit_subparticle()` is currently the only custom function supported by particle shaders. It allows users to add a new particle with specified parameters from a sub-emitter. The newly created particle will only use the properties that match the `flags` parameter. For example, the following code will emit a particle with a specified position, velocity, and color, but unspecified rotation, scale, and custom value:

```glsl
mat4 custom_transform = mat4(1.0);
custom_transform[3].xyz = vec3(10.5, 0.0, 4.0);
emit_subparticle(custom_transform, vec3(1.0, 0.5, 1.0), vec4(1.0, 0.0, 0.0, 1.0), vec4(1.0), FLAG_EMIT_POSITION | FLAG_EMIT_VELOCITY | FLAG_EMIT_COLOR);
```

| Function                                                                               | Description                          |
| -------------------------------------------------------------------------------------- | ------------------------------------ |
| bool emit_subparticle (mat4 xform, vec3 velocity, vec4 color, vec4 custom, uint flags) | Emits a particle from a sub-emitter. |

---
