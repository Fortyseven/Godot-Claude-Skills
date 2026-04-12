# Godot 4 C# Tutorials — Shaders (Part 5)

> 3 tutorials. C#-specific code examples.

## Sky shaders

Sky shaders are a special type of shader used for drawing sky backgrounds and for updating radiance cubemaps which are used for image-based lighting (IBL). Sky shaders only have one processing function, the `sky()` function.

There are three places the sky shader is used.

- First the sky shader is used to draw the sky when you have selected to use a Sky as the background in your scene.
- Second, the sky shader is used to update the radiance cubemap when using the Sky for ambient color or reflections.
- Third, the sky shader is used to draw the lower res subpasses which can be used in the high-res background or cubemap pass.

In total, this means the sky shader can run up to six times per frame, however, in practice it will be much less than that because the radiance cubemap does not need to be updated every frame, and not all subpasses will be used. You can change the behavior of the shader based on where it is called by checking the `AT_*_PASS` booleans. For example:

```glsl
shader_type sky;

void sky() {
    if (AT_CUBEMAP_PASS) {
        // Sets the radiance cubemap to a nice shade of blue instead of doing
        // expensive sky calculations
        COLOR = vec3(0.2, 0.6, 1.0);
    } else {
        // Do expensive sky calculations for background sky only
        COLOR = get_sky_color(EYEDIR);
    }
}
```

When using the sky shader to draw a background, the shader will be called for all non-occluded fragments on the screen. However, for the background's subpasses, the shader will be called for every pixel of the subpass.

When using the sky shader to update the radiance cubemap, the sky shader will be called for every pixel in the cubemap. On the other hand, the shader will only be called when the radiance cubemap needs to be updated. The radiance cubemap needs to be updated when any of the shader parameters are updated. For example, if `TIME` is used in the shader, then the radiance cubemap will update every frame. The following list of changes force an update of the radiance cubemap:

- `TIME` is used.
- `POSITION` is used and the camera position changes.
- If any `LIGHTX_*` properties are used and any [DirectionalLight3D](../godot_csharp_nodes_3d.md) changes.
- If any uniform is changed in the shader.
- If the screen is resized and either of the subpasses are used.

Try to avoid updating the radiance cubemap needlessly. If you do need to update the radiance cubemap each frame, make sure your [Sky process mode](../godot_csharp_misc.md) is set to [PROCESS_MODE_REALTIME](../godot_csharp_misc.md).

Note that the [process mode](../godot_csharp_misc.md) only affects the rendering of the radiance cubemap. The visible sky is always rendered by calling the fragment shader for every pixel. With complex fragment shaders, this can result in a high rendering overhead. If the sky is static (the conditions listed above are met) or changes slowly, running the full fragment shader every frame is not needed. This can be avoided by rendering the full sky into the radiance cubemap, and reading from this cubemap when rendering the visible sky. With a completely static sky, this means that it needs to be rendered only once.

The following code renders the full sky into the radiance cubemap and reads from that cubemap for displaying the visible sky:

```glsl
shader_type sky;

void sky() {
    if (AT_CUBEMAP_PASS) {
        vec3 dir = EYEDIR;

        vec4 col = vec4(0.0);

        // Complex color calculation

        COLOR = col.xyz;
        ALPHA = 1.0;
    } else {
        COLOR = texture(RADIANCE, EYEDIR).rgb;
    }
}
```

This way, the complex calculations happen only in the cubemap pass, which can be optimized by setting the sky's [process mode](../godot_csharp_misc.md) and the [radiance size](../godot_csharp_misc.md) to get the desired balance between performance and visual fidelity.

### Render modes

Subpasses allow you to do more expensive calculations at a lower resolution to speed up your shaders. For example the following code renders clouds at a lower resolution than the rest of the sky:

```glsl
shader_type sky;
render_mode use_half_res_pass;

void sky() {
    if (AT_HALF_RES_PASS) {
        // Run cloud calculation for 1/4 of the pixels
        vec4 color = generate_clouds(EYEDIR);
        COLOR = color.rgb;
        ALPHA = color.a;
    } else {
        // At full resolution pass, blend sky and clouds together
        vec3 color = generate_sky(EYEDIR);
        COLOR = color + HALF_RES_COLOR.rgb * HALF_RES_COLOR.a;
    }
}
```

| Render mode          | Description                                                           |
| -------------------- | --------------------------------------------------------------------- |
| use_half_res_pass    | Allows the shader to write to and access the half resolution pass.    |
| use_quarter_res_pass | Allows the shader to write to and access the quarter resolution pass. |
| disable_fog          | If used, fog will not affect the sky.                                 |

### Built-ins

Values marked as `in` are read-only. Values marked as `out` can optionally be written to and will not necessarily contain sensible values. Samplers cannot be written to so they are not marked.

### Global built-ins

Global built-ins are available everywhere, including in custom functions.

There are 4 `LIGHTX` lights, accessed as `LIGHT0`, `LIGHT1`, `LIGHT2`, and `LIGHT3`.

| Built-in                    | Description                                                                                                                                                                                                                                                                                                               |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| in float TIME               | Global time since the engine has started, in seconds. It repeats after every 3,600 seconds (which can be changed with the rollover setting). It's affected by time_scale but not by pausing. If you need a TIME variable that is not affected by time scale, add your own global shader uniform and update it each frame. |
| in vec3 POSITION            | Camera position, in world space.                                                                                                                                                                                                                                                                                          |
| samplerCube RADIANCE        | Radiance cubemap. Can only be read from during the background pass. Check !AT_CUBEMAP_PASS before using.                                                                                                                                                                                                                  |
| in bool AT_HALF_RES_PASS    | true when rendering to the half resolution pass.                                                                                                                                                                                                                                                                          |
| in bool AT_QUARTER_RES_PASS | true when rendering to the quarter resolution pass.                                                                                                                                                                                                                                                                       |
| in bool AT_CUBEMAP_PASS     | true when rendering to the radiance cubemap.                                                                                                                                                                                                                                                                              |
| in bool LIGHTX_ENABLED      | true if LIGHTX is visible and in the scene. If false, other light properties may be garbage.                                                                                                                                                                                                                              |
| in float LIGHTX_ENERGY      | Energy multiplier for LIGHTX.                                                                                                                                                                                                                                                                                             |
| in vec3 LIGHTX_DIRECTION    | Direction that LIGHTX is facing.                                                                                                                                                                                                                                                                                          |
| in vec3 LIGHTX_COLOR        | Color of LIGHTX.                                                                                                                                                                                                                                                                                                          |
| in float LIGHTX_SIZE        | Angular diameter of LIGHTX in the sky. Expressed in radians. For reference, the sun from earth is about .0087 radians (0.5 degrees).                                                                                                                                                                                      |
| in float PI                 | A PI constant (3.141592). The ratio of a circle's circumference to its diameter and the number of radians in a half turn.                                                                                                                                                                                                 |
| in float TAU                | A TAU constant (6.283185). Equivalent to PI \* 2 and the number of radians in a full turn.                                                                                                                                                                                                                                |
| in float E                  | An E constant (2.718281). Euler's number, the base of the natural logarithm.                                                                                                                                                                                                                                              |

### Sky built-ins

| Built-in                  | Description                                                                                         |
| ------------------------- | --------------------------------------------------------------------------------------------------- |
| in vec3 EYEDIR            | Normalized direction of the current pixel. Use this as your basic direction for procedural effects. |
| in vec2 SCREEN_UV         | Screen UV coordinate for the current pixel. Used to map a texture to the full screen.               |
| in vec2 SKY_COORDS        | Sphere UV. Used to map a panorama texture to the sky.                                               |
| in vec4 HALF_RES_COLOR    | Color value of the corresponding pixel from the half resolution pass. Uses linear filter.           |
| in vec4 QUARTER_RES_COLOR | Color value of the corresponding pixel from the quarter resolution pass. Uses linear filter.        |
| out vec3 COLOR            | Output color.                                                                                       |
| out float ALPHA           | Output alpha value, can only be used in subpasses.                                                  |
| out vec4 FOG              |                                                                                                     |

---

## Spatial shaders

Spatial shaders are used for shading 3D objects. They are the most complex type of shader Godot offers. Spatial shaders are highly configurable with different render modes and different rendering options (e.g. Subsurface Scattering, Transmission, Ambient Occlusion, Rim lighting, etc.). Users can optionally write vertex, fragment, and light processor functions to affect how objects are drawn.

### Render modes

For visual examples of these render modes, see [Standard Material 3D and ORM Material 3D](tutorials_3d.md).

| Render mode               | Description                                                                                                                                                     |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| blend_mix                 | Mix blend mode (alpha is transparency), default.                                                                                                                |
| blend_add                 | Additive blend mode.                                                                                                                                            |
| blend_sub                 | Subtractive blend mode.                                                                                                                                         |
| blend_mul                 | Multiplicative blend mode.                                                                                                                                      |
| blend_premul_alpha        | Premultiplied alpha blend mode (fully transparent = add, fully opaque = mix).                                                                                   |
| depth_draw_opaque         | Only draw depth for opaque geometry (not transparent).                                                                                                          |
| depth_draw_always         | Always draw depth (opaque and transparent).                                                                                                                     |
| depth_draw_never          | Never draw depth.                                                                                                                                               |
| depth_prepass_alpha       | Do opaque depth pre-pass for transparent geometry.                                                                                                              |
| depth_test_disabled       | Disable depth testing.                                                                                                                                          |
| depth_test_default        | Depth test will discard the pixel if it is behind other pixels. In Forward+ only, the pixel is also discarded if it's at the exact same depth as another pixel. |
| depth_test_inverted       | Depth test will discard the pixel if it is in front of other pixels. Useful for stencil effects.                                                                |
| sss_mode_skin             | Subsurface Scattering mode for skin (optimizes visuals for human skin, e.g. boosted red channel).                                                               |
| cull_back                 | Cull back-faces (default).                                                                                                                                      |
| cull_front                | Cull front-faces.                                                                                                                                               |
| cull_disabled             | Culling disabled (double sided).                                                                                                                                |
| unshaded                  | Result is just albedo. No lighting/shading happens in material, making it faster to render.                                                                     |
| wireframe                 | Geometry draws using lines (useful for troubleshooting).                                                                                                        |
| debug_shadow_splits       | Directional shadows are drawn using different colors for each split (useful for troubleshooting).                                                               |
| diffuse_burley            | Burley (Disney PBS) for diffuse (default).                                                                                                                      |
| diffuse_lambert           | Lambert shading for diffuse.                                                                                                                                    |
| diffuse_lambert_wrap      | Lambert-wrap shading (roughness-dependent) for diffuse.                                                                                                         |
| diffuse_toon              | Toon shading for diffuse.                                                                                                                                       |
| specular_schlick_ggx      | Schlick-GGX for direct light specular lobes (default).                                                                                                          |
| specular_toon             | Toon for direct light specular lobes.                                                                                                                           |
| specular_disabled         | Disable direct light specular lobes. Doesn't affect reflected light (use SPECULAR = 0.0 instead).                                                               |
| skip_vertex_transform     | VERTEX, NORMAL, TANGENT, and BITANGENT need to be transformed manually in the vertex() function.                                                                |
| world_vertex_coords       | VERTEX, NORMAL, TANGENT, and BITANGENT are modified in world space instead of model space.                                                                      |
| ensure_correct_normals    | Use when non-uniform scale is applied to mesh (note: currently unimplemented).                                                                                  |
| shadows_disabled          | Disable computing shadows in shader. The shader will not receive shadows, but can still cast them.                                                              |
| ambient_light_disabled    | Disable contribution from ambient light and radiance map.                                                                                                       |
| shadow_to_opacity         | Lighting modifies the alpha so shadowed areas are opaque and non-shadowed areas are transparent. Useful for overlaying shadows onto a camera feed in AR.        |
| vertex_lighting           | Use vertex-based lighting instead of per-pixel lighting.                                                                                                        |
| particle_trails           | Enables the trails when used on particle geometry.                                                                                                              |
| alpha_to_coverage         | Alpha antialiasing mode, see here for more.                                                                                                                     |
| alpha_to_coverage_and_one | Alpha antialiasing mode, see here for more.                                                                                                                     |
| fog_disabled              | Disable receiving depth-based or volumetric fog. Useful for blend_add materials like particles.                                                                 |

### Stencil modes

> **Note:** Stencil support is experimental, use at your own risk. We will try to not break compatibility as much as possible, but if significant flaws are found in the API, it may change in the next minor version.

Stencil operations are a set of operations that allow writing to an efficient buffer in an hardware-accelerated manner. This is generally used to mask in or out parts of the scene.

Some of the most well-known uses are:

- Outlines: Mask out the inner mesh that is being outlined to avoid inner outlines.
- X-Ray: Display a mesh behind other objects.
- Portals: Draw geometry that is normally "impossible" (non-Euclidian) by masking objects.

> **Note:** You can only read from the stencil buffer in the transparent pass. Any attempt to read in the opaque pass will fail, as it's currently not supported behavior. Note that for compositor effects, the main renderer's stencil buffer can't be copied to a custom texture.

| Stencil mode             | Description                                                                                    |
| ------------------------ | ---------------------------------------------------------------------------------------------- |
| read                     | Read from the stencil buffer.                                                                  |
| write                    | Write reference value to the stencil buffer.                                                   |
| write_if_depth_fail      | Write reference value to the stencil buffer if the depth test fails.                           |
| compare_always           | Always pass stencil test.                                                                      |
| compare_equal            | Pass stencil test if the reference value is equal to the stencil buffer value.                 |
| compare_not_equal        | Pass stencil test if the reference value is not equal to the stencil buffer value.             |
| compare_less             | Pass stencil test if the reference value is less than the stencil buffer value.                |
| compare_less_or_equal    | Pass stencil test if the reference value is less than or equal to the stencil buffer value.    |
| compare_greater          | Pass stencil test if the reference value is greater than the stencil buffer value.             |
| compare_greater_or_equal | Pass stencil test if the reference value is greater than or equal to the stencil buffer value. |

### Built-ins

Values marked as `in` are read-only. Values marked as `out` can optionally be written to and will not necessarily contain sensible values. Values marked as `inout` provide a sensible default value, and can optionally be written to. Samplers cannot be written to so they are not marked.

Not all built-ins are available in all processing functions. To access a vertex built-in from the `fragment()` function, you can use a varying. The same applies for accessing fragment built-ins from the `light()` function.

### Global built-ins

Global built-ins are available everywhere, including custom functions.

| Built-in                | Description                                                                                                                                                                                                                                                                                                               |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| in float TIME           | Global time since the engine has started, in seconds. It repeats after every 3,600 seconds (which can be changed with the rollover setting). It's affected by time_scale but not by pausing. If you need a TIME variable that is not affected by time scale, add your own global shader uniform and update it each frame. |
| in float PI             | A PI constant (3.141592). The ratio of a circle's circumference to its diameter and the number of radians in a half turn.                                                                                                                                                                                                 |
| in float TAU            | A TAU constant (6.283185). Equivalent to PI \* 2 and the number of radians in a full turn.                                                                                                                                                                                                                                |
| in float E              | An E constant (2.718281). Euler's number, the base of the natural logarithm.                                                                                                                                                                                                                                              |
| in bool OUTPUT_IS_SRGB  | true when output is in sRGB color space (this is true in the Compatibility renderer, false in Forward+ and Mobile).                                                                                                                                                                                                       |
| in float CLIP_SPACE_FAR | Clip space far z value. In the Forward+ or Mobile renderers, it's 0.0. In the Compatibility renderer, it's -1.0.                                                                                                                                                                                                          |

### Vertex built-ins

Vertex data (`VERTEX`, `NORMAL`, `TANGENT`, and `BITANGENT`) are presented in model space (also called local space). If not written to, these values will not be modified and be passed through as they came, then transformed into view space to be used in `fragment()`.

They can optionally be presented in world space by using the `world_vertex_coords` render mode.

Users can disable the built-in modelview transform (projection will still happen later) and do it manually with the following code:

```glsl
shader_type spatial;
render_mode skip_vertex_transform;

void vertex() {
    VERTEX = (MODELVIEW_MATRIX * vec4(VERTEX, 1.0)).xyz;
    NORMAL = normalize((MODELVIEW_MATRIX * vec4(NORMAL, 0.0)).xyz);
    BINORMAL = normalize((MODELVIEW_MATRIX * vec4(BINORMAL, 0.0)).xyz);
    TANGENT = normalize((MODELVIEW_MATRIX * vec4(TANGENT, 0.0)).xyz);
}
```

Other built-ins, such as `UV`, `UV2`, and `COLOR`, are also passed through to the `fragment()` function if not modified.

Users can override the modelview and projection transforms using the `POSITION` built-in. If `POSITION` is written to anywhere in the shader, it will always be used, so the user becomes responsible for ensuring that it always has an acceptable value. When `POSITION` is used, the value from `VERTEX` is ignored and projection does not happen. However, the value passed to the fragment shader still comes from `VERTEX`.

For instancing, the `INSTANCE_CUSTOM` variable contains the instance custom data. When using particles, this information is usually:

- **x**: Rotation angle in radians.
- **y**: Phase during lifetime (`0.0` to `1.0`).
- **z**: Animation frame.

This allows you to easily adjust the shader to a particle system using default particle material. When writing a custom particle shader, this value can be used as desired.

| Built-in                           | Description                                                                                                                                                                                                                                                                                                                           |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| in vec2 VIEWPORT_SIZE              | Size of viewport (in pixels).                                                                                                                                                                                                                                                                                                         |
| in mat4 VIEW_MATRIX                | World space to view space transform.                                                                                                                                                                                                                                                                                                  |
| in mat4 INV_VIEW_MATRIX            | View space to world space transform.                                                                                                                                                                                                                                                                                                  |
| in mat4 MAIN_CAM_INV_VIEW_MATRIX   | View space to world space transform of the camera used to draw the current viewport.                                                                                                                                                                                                                                                  |
| in mat4 INV_PROJECTION_MATRIX      | Clip space to view space transform.                                                                                                                                                                                                                                                                                                   |
| in vec3 NODE_POSITION_WORLD        | Node position, in world space.                                                                                                                                                                                                                                                                                                        |
| in vec3 NODE_POSITION_VIEW         | Node position, in view space.                                                                                                                                                                                                                                                                                                         |
| in vec3 CAMERA_POSITION_WORLD      | Camera position, in world space. Represents the midpoint of the two eyes when in multiview/stereo rendering.                                                                                                                                                                                                                          |
| in vec3 CAMERA_DIRECTION_WORLD     | Camera direction, in world space.                                                                                                                                                                                                                                                                                                     |
| in uint CAMERA_VISIBLE_LAYERS      | Cull layers of the camera rendering the current pass.                                                                                                                                                                                                                                                                                 |
| in int INSTANCE_ID                 | Instance ID for instancing.                                                                                                                                                                                                                                                                                                           |
| in vec4 INSTANCE_CUSTOM            | Instance custom data (for particles, mostly).                                                                                                                                                                                                                                                                                         |
| in int VIEW_INDEX                  | The view that we are rendering. VIEW_MONO_LEFT (0) for Mono (not multiview) or left eye, VIEW_RIGHT (1) for right eye.                                                                                                                                                                                                                |
| in int VIEW_MONO_LEFT              | Constant for Mono or left eye, always 0.                                                                                                                                                                                                                                                                                              |
| in int VIEW_RIGHT                  | Constant for right eye, always 1.                                                                                                                                                                                                                                                                                                     |
| in vec3 EYE_OFFSET                 | Position offset for the eye being rendered, in view space. Only applicable for multiview rendering.                                                                                                                                                                                                                                   |
| inout vec3 VERTEX                  | Position of the vertex, in model space. In world space if world_vertex_coords is used.                                                                                                                                                                                                                                                |
| in int VERTEX_ID                   | The index of the current vertex in the vertex buffer.                                                                                                                                                                                                                                                                                 |
| inout vec3 NORMAL                  | Normal in model space. In world space if world_vertex_coords is used.                                                                                                                                                                                                                                                                 |
| inout vec3 TANGENT                 | Tangent in model space. In world space if world_vertex_coords is used.                                                                                                                                                                                                                                                                |
| inout vec3 BINORMAL                | Binormal in model space. In world space if world_vertex_coords is used.                                                                                                                                                                                                                                                               |
| out vec4 POSITION                  | If written to, overrides final vertex position in clip space.                                                                                                                                                                                                                                                                         |
| inout vec2 UV                      | UV main channel.                                                                                                                                                                                                                                                                                                                      |
| inout vec2 UV2                     | UV secondary channel.                                                                                                                                                                                                                                                                                                                 |
| inout vec4 COLOR                   | Color from vertices. Limited to values between 0.0 and 1.0 for each channel and 8 bits per channel precision (256 possible levels). Alpha channel is supported. Values outside the allowed range are clamped, and values may be rounded due to precision limitations. Use CUSTOM0-CUSTOM3 to pass data with more precision if needed. |
| out float ROUGHNESS                | Roughness for vertex lighting.                                                                                                                                                                                                                                                                                                        |
| inout float POINT_SIZE             | Point size for point rendering.                                                                                                                                                                                                                                                                                                       |
| inout mat4 MODELVIEW_MATRIX        | Model/local space to view space transform (use if possible).                                                                                                                                                                                                                                                                          |
| inout mat3 MODELVIEW_NORMAL_MATRIX |                                                                                                                                                                                                                                                                                                                                       |
| in mat4 MODEL_MATRIX               | Model/local space to world space transform.                                                                                                                                                                                                                                                                                           |
| in mat3 MODEL_NORMAL_MATRIX        |                                                                                                                                                                                                                                                                                                                                       |
| inout mat4 PROJECTION_MATRIX       | View space to clip space transform.                                                                                                                                                                                                                                                                                                   |
| in uvec4 BONE_INDICES              |                                                                                                                                                                                                                                                                                                                                       |
| in vec4 BONE_WEIGHTS               |                                                                                                                                                                                                                                                                                                                                       |
| in vec4 CUSTOM0                    | Custom value from vertex primitive. When using extra UVs, xy is UV3 and zw is UV4.                                                                                                                                                                                                                                                    |
| in vec4 CUSTOM1                    | Custom value from vertex primitive. When using extra UVs, xy is UV5 and zw is UV6.                                                                                                                                                                                                                                                    |
| in vec4 CUSTOM2                    | Custom value from vertex primitive. When using extra UVs, xy is UV7 and zw is UV8.                                                                                                                                                                                                                                                    |
| in vec4 CUSTOM3                    | Custom value from vertex primitive.                                                                                                                                                                                                                                                                                                   |
| out float Z_CLIP_SCALE             | If written to, scales the vertex towards the camera to avoid clipping into things like walls. Lighting and shadows will continue to work correctly when this is written to, but screen-space effects like SSAO and SSR may break with lower scales. Try to keep this value as close to 1.0 as possible.                               |

> **Note:** `MODELVIEW_MATRIX` combines both the `MODEL_MATRIX` and `VIEW_MATRIX` and is better suited when floating point issues may arise. For example, if the object is very far away from the world origin, you may run into floating point issues when using the separated `MODEL_MATRIX` and `VIEW_MATRIX`.

> **Note:** `INV_VIEW_MATRIX` is the matrix used for rendering the object in that pass, unlike `MAIN_CAM_INV_VIEW_MATRIX`, which is the matrix of the camera in the scene. In the shadow pass, `INV_VIEW_MATRIX`'s view is based on the camera that is located at the position of the light.

### Fragment built-ins

The default use of a Godot fragment processor function is to set up the material properties of your object and to let the built-in renderer handle the final shading. However, you are not required to use all these properties, and if you don't write to them, Godot will optimize away the corresponding functionality.

| Built-in                          | Description                                                                                                                                                                                                                                                 |
| --------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| in vec2 VIEWPORT_SIZE             | Size of viewport (in pixels).                                                                                                                                                                                                                               |
| in vec4 FRAGCOORD                 | Coordinate of pixel center in screen space. xy specifies position in window. Origin is upper left. z specifies fragment depth. It is also used as the output value for the fragment depth unless DEPTH is written to.                                       |
| in bool FRONT_FACING              | true if current face is front facing, false otherwise.                                                                                                                                                                                                      |
| in vec3 VIEW                      | Normalized vector from fragment position to camera (in view space). This is the same for both perspective and orthogonal cameras.                                                                                                                           |
| in vec2 UV                        | UV that comes from the vertex() function.                                                                                                                                                                                                                   |
| in vec2 UV2                       | UV2 that comes from the vertex() function.                                                                                                                                                                                                                  |
| in vec4 COLOR                     | COLOR that comes from the vertex() function.                                                                                                                                                                                                                |
| in vec2 POINT_COORD               | Point coordinate for drawing points with POINT_SIZE.                                                                                                                                                                                                        |
| in mat4 MODEL_MATRIX              | Model/local space to world space transform.                                                                                                                                                                                                                 |
| in mat3 MODEL_NORMAL_MATRIX       | Model/local space to world space transform for normals. This is the same as MODEL_MATRIX by default unless the object is scaled non-uniformly, in which case this is set to transpose(inverse(mat3(MODEL_MATRIX))).                                         |
| in mat4 VIEW_MATRIX               | World space to view space transform.                                                                                                                                                                                                                        |
| in mat4 INV_VIEW_MATRIX           | View space to world space transform.                                                                                                                                                                                                                        |
| in mat4 PROJECTION_MATRIX         | View space to clip space transform.                                                                                                                                                                                                                         |
| in mat4 INV_PROJECTION_MATRIX     | Clip space to view space transform.                                                                                                                                                                                                                         |
| in vec3 NODE_POSITION_WORLD       | Node position, in world space.                                                                                                                                                                                                                              |
| in vec3 NODE_POSITION_VIEW        | Node position, in view space.                                                                                                                                                                                                                               |
| in vec3 CAMERA_POSITION_WORLD     | Camera position, in world space. Represents the midpoint of the two eyes when in multiview/stereo rendering.                                                                                                                                                |
| in vec3 CAMERA_DIRECTION_WORLD    | Camera direction, in world space.                                                                                                                                                                                                                           |
| in uint CAMERA_VISIBLE_LAYERS     | Cull layers of the camera rendering the current pass.                                                                                                                                                                                                       |
| in vec3 VERTEX                    | Position of the fragment (pixel), in view space. It is the VERTEX value from vertex() interpolated between the face's vertices and transformed into view space. If skip_vertex_transform is enabled, it may not be in view space.                           |
| inout vec3 LIGHT_VERTEX           | A writable version of VERTEX that can be used to alter light and shadows. Writing to this will not change the position of the fragment.                                                                                                                     |
| in int VIEW_INDEX                 | The view that we are rendering. Used to distinguish between views in multiview/stereo rendering. VIEW_MONO_LEFT (0) for Mono (not multiview) or left eye, VIEW_RIGHT (1) for right eye.                                                                     |
| in int VIEW_MONO_LEFT             | Constant for Mono or left eye, always 0.                                                                                                                                                                                                                    |
| in int VIEW_RIGHT                 | Constant for right eye, always 1.                                                                                                                                                                                                                           |
| in vec3 EYE_OFFSET                | Position offset for the eye being rendered, in view space. Only applicable for multiview rendering.                                                                                                                                                         |
| sampler2D SCREEN_TEXTURE          | Removed in Godot 4. Use a sampler2D with hint_screen_texture instead.                                                                                                                                                                                       |
| in vec2 SCREEN_UV                 | Screen UV coordinate for the current pixel.                                                                                                                                                                                                                 |
| sampler2D DEPTH_TEXTURE           | Removed in Godot 4. Use a sampler2D with hint_depth_texture instead.                                                                                                                                                                                        |
| out float DEPTH                   | Custom depth value (range [0.0, 1.0]). If DEPTH is written to in any shader branch, then you are responsible for setting DEPTH for all other branches. Otherwise, the graphics API will leave them uninitialized.                                           |
| inout vec3 NORMAL                 | Normal that comes from the vertex() function, in view space. If skip_vertex_transform is enabled, it may not be in view space.                                                                                                                              |
| inout vec3 TANGENT                | Tangent that comes from the vertex() function, in view space. If skip_vertex_transform is enabled, it may not be in view space.                                                                                                                             |
| inout vec3 BINORMAL               | Binormal that comes from the vertex() function, in view space. If skip_vertex_transform is enabled, it may not be in view space.                                                                                                                            |
| out vec3 NORMAL_MAP               | Set normal here if reading normal from a texture instead of NORMAL.                                                                                                                                                                                         |
| out float NORMAL_MAP_DEPTH        | Depth from NORMAL_MAP. Defaults to 1.0.                                                                                                                                                                                                                     |
| out vec3 ALBEDO                   | Albedo (default white). Base color.                                                                                                                                                                                                                         |
| out float ALPHA                   | Alpha (range [0.0, 1.0]). If read from or written to, the material will go to the transparent pipeline.                                                                                                                                                     |
| out float ALPHA_SCISSOR_THRESHOLD | If written to, values below a certain amount of alpha are discarded.                                                                                                                                                                                        |
| out float ALPHA_HASH_SCALE        | Alpha hash scale when using the alpha hash transparency mode. Defaults to 1.0. Higher values result in more visible pixels in the dithering pattern.                                                                                                        |
| out float ALPHA_ANTIALIASING_EDGE | The threshold below which alpha to coverage antialiasing should be used. Defaults to 0.0. Requires the alpha_to_coverage render mode. Should be set to a value lower than ALPHA_SCISSOR_THRESHOLD to be effective.                                          |
| out vec2 ALPHA_TEXTURE_COORDINATE | The texture coordinate to use for alpha-to-coverge antialiasing. Requires the alpha_to_coverage render mode. Typically set to UV \* vec2(albedo_texture_size) where albedo_texture_size is the size of the albedo texture in pixels.                        |
| out float PREMUL_ALPHA_FACTOR     | Premultiplied alpha factor. Only effective if render_mode blend_premul_alpha; is used. This should be written to when using a shaded material with premultiplied alpha blending for interaction with lighting. This is not required for unshaded materials. |
| out float METALLIC                | Metallic (range [0.0, 1.0]).                                                                                                                                                                                                                                |
| out float SPECULAR                | Specular (not physically accurate to change). Defaults to 0.5. 0.0 disables reflections.                                                                                                                                                                    |
| out float ROUGHNESS               | Roughness (range [0.0, 1.0]).                                                                                                                                                                                                                               |
| out float RIM                     | Rim (range [0.0, 1.0]). If used, Godot calculates rim lighting. Rim size depends on ROUGHNESS.                                                                                                                                                              |
| out float RIM_TINT                | Rim Tint, range from 0.0 (white) to 1.0 (albedo). If used, Godot calculates rim lighting.                                                                                                                                                                   |
| out float CLEARCOAT               | Small specular blob added on top of the existing one. If used, Godot calculates clearcoat.                                                                                                                                                                  |
| out float CLEARCOAT_GLOSS         | Gloss of clearcoat. If used, Godot calculates clearcoat.                                                                                                                                                                                                    |
| out float ANISOTROPY              | For distorting the specular blob according to tangent space.                                                                                                                                                                                                |
| out vec2 ANISOTROPY_FLOW          | Distortion direction, use with flowmaps.                                                                                                                                                                                                                    |
| out float SSS_STRENGTH            | Strength of subsurface scattering. If used, subsurface scattering will be applied to the object.                                                                                                                                                            |
| out vec4 SSS_TRANSMITTANCE_COLOR  | Color of subsurface scattering transmittance. If used, subsurface scattering transmittance will be applied to the object.                                                                                                                                   |
| out float SSS_TRANSMITTANCE_DEPTH | Depth of subsurface scattering transmittance. Higher values allow the effect to reach deeper into the object.                                                                                                                                               |
| out float SSS_TRANSMITTANCE_BOOST | Boosts the subsurface scattering transmittance if set above 0.0. This makes the effect show up even on directly lit surfaces                                                                                                                                |
| inout vec3 BACKLIGHT              | Color of backlighting (works like direct light, but it's received even if the normal is slightly facing away from the light). If used, backlighting will be applied to the object. Can be used as a cheaper approximation of subsurface scattering.         |
| out float AO                      | Strength of ambient occlusion. For use with pre-baked AO.                                                                                                                                                                                                   |
| out float AO_LIGHT_AFFECT         | How much ambient occlusion affects direct light (range [0.0, 1.0], default 0.0).                                                                                                                                                                            |
| out vec3 EMISSION                 | Emission color (can go over (1.0, 1.0, 1.0) for HDR).                                                                                                                                                                                                       |
| out vec4 FOG                      | If written to, blends final pixel color with FOG.rgb based on FOG.a.                                                                                                                                                                                        |
| out vec4 RADIANCE                 | If written to, blends environment map radiance with RADIANCE.rgb based on RADIANCE.a.                                                                                                                                                                       |
| out vec4 IRRADIANCE               | If written to, blends environment map irradiance with IRRADIANCE.rgb based on IRRADIANCE.a.                                                                                                                                                                 |

> **Note:** Shaders going through the transparent pipeline when `ALPHA` is written to may exhibit transparency sorting issues. Read the [transparency sorting section in the 3D rendering limitations page](tutorials_3d.md) for more information and ways to avoid issues.

### Light built-ins

Writing light processor functions is completely optional. You can skip the `light()` function by using the `unshaded` render mode. If no light function is written, Godot will use the material properties written to in the `fragment()` function to calculate the lighting for you (subject to the render mode).

The `light()` function is called for every light in every pixel. It is called within a loop for each light type.

Below is an example of a custom `light()` function using a Lambertian lighting model:

```glsl
void light() {
    DIFFUSE_LIGHT += clamp(dot(NORMAL, LIGHT), 0.0, 1.0) * ATTENUATION * LIGHT_COLOR / PI;
}
```

If you want the lights to add together, add the light contribution to `DIFFUSE_LIGHT` using `+=`, rather than overwriting it.

> **Warning:** The `light()` function won't be run if the `vertex_lighting` render mode is enabled, or if [Rendering > Quality > Shading > Force Vertex Shading](../godot_csharp_misc.md) is enabled in the Project Settings. (It's enabled by default on mobile platforms.)

| Built-in                      | Description                                                                                                                                                  |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| in vec2 VIEWPORT_SIZE         | Size of viewport (in pixels).                                                                                                                                |
| in vec4 FRAGCOORD             | Coordinate of pixel center in screen space. xy specifies position in window, z specifies fragment depth if DEPTH is not used. Origin is lower-left.          |
| in mat4 MODEL_MATRIX          | Model/local space to world space transform.                                                                                                                  |
| in mat4 INV_VIEW_MATRIX       | View space to world space transform.                                                                                                                         |
| in mat4 VIEW_MATRIX           | World space to view space transform.                                                                                                                         |
| in mat4 PROJECTION_MATRIX     | View space to clip space transform.                                                                                                                          |
| in mat4 INV_PROJECTION_MATRIX | Clip space to view space transform.                                                                                                                          |
| in vec3 NORMAL                | Normal vector, in view space.                                                                                                                                |
| in vec2 SCREEN_UV             | Screen UV coordinate for the current pixel.                                                                                                                  |
| in vec2 UV                    | UV that comes from the vertex() function.                                                                                                                    |
| in vec2 UV2                   | UV2 that comes from the vertex() function.                                                                                                                   |
| in vec3 VIEW                  | View vector, in view space.                                                                                                                                  |
| in vec3 LIGHT                 | Light vector, in view space.                                                                                                                                 |
| in vec3 LIGHT_COLOR           | Light color multiplied by light energy multiplied by PI. The PI multiplication is present because physically-based lighting models include a division by PI. |
| in float SPECULAR_AMOUNT      | For OmniLight3D and SpotLight3D, 2.0 multiplied by light_specular. For DirectionalLight3D, 1.0.                                                              |
| in bool LIGHT_IS_DIRECTIONAL  | true if this pass is a DirectionalLight3D.                                                                                                                   |
| in float ATTENUATION          | Attenuation based on distance or shadow.                                                                                                                     |
| in vec3 ALBEDO                | Base albedo.                                                                                                                                                 |
| in vec3 BACKLIGHT             |                                                                                                                                                              |
| in float METALLIC             | Metallic.                                                                                                                                                    |
| in float ROUGHNESS            | Roughness.                                                                                                                                                   |
| out vec3 DIFFUSE_LIGHT        | Diffuse light result.                                                                                                                                        |
| out vec3 SPECULAR_LIGHT       | Specular light result.                                                                                                                                       |
| out float ALPHA               | Alpha (range [0.0, 1.0]). If written to, the material will go to the transparent pipeline.                                                                   |

> **Note:** Shaders going through the transparent pipeline when `ALPHA` is written to may exhibit transparency sorting issues. Read the [transparency sorting section in the 3D rendering limitations page](tutorials_3d.md) for more information and ways to avoid issues. Transparent materials also cannot cast shadows or appear in `hint_screen_texture` and `hint_depth_texture` uniforms. This in turn prevents those materials from appearing in screen-space reflections or refraction. [SDFGI](tutorials_3d.md) sharp reflections are not visible on transparent materials (only rough reflections are visible on transparent materials).

---

## Shaders style guide

This style guide lists conventions to write elegant shaders. The goal is to encourage writing clean, readable code and promote consistency across projects, discussions, and tutorials. Hopefully, this will also support the development of auto-formatting tools.

Since the Godot shader language is close to C-style languages and GLSL, this guide is inspired by Godot's own GLSL formatting. You can view examples of GLSL files in Godot's source code [here](https://github.com/godotengine/godot/blob/master/drivers/gles3/shaders/).

Style guides aren't meant as hard rulebooks. At times, you may not be able to apply some of the guidelines below. When that happens, use your best judgment, and ask fellow developers for insights.

In general, keeping your code consistent in your projects and within your team is more important than following this guide to a tee.

> **Note:** Godot's built-in shader editor uses a lot of these conventions by default. Let it help you.

Here is a complete shader example based on these guidelines:

```glsl
shader_type canvas_item;
// Screen-space shader to adjust a 2D scene's brightness, contrast
// and saturation. Taken from
// https://github.com/godotengine/godot-demo-projects/blob/master/2d/screen_space_shaders/shaders/BCS.gdshader

uniform sampler2D screen_texture : hint_screen_texture, filter_linear_mipmap;
uniform float brightness = 0.8;
uniform float contrast = 1.5;
uniform float saturation = 1.8;

void fragment() {
    vec3 c = textureLod(screen_texture, SCREEN_UV, 0.0).rgb;

    c.rgb = mix(vec3(0.0), c.rgb, brightness);
    c.rgb = mix(vec3(0.5), c.rgb, contrast);
    c.rgb = mix(vec3(dot(vec3(1.0), c.rgb) * 0.33333), c.rgb, saturation);

    COLOR.rgb = c;
}
```

### Formatting

#### Encoding and special characters

- Use line feed (**LF**) characters to break lines, not CRLF or CR. _(editor default)_
- Use one line feed character at the end of each file. _(editor default)_
- Use **UTF-8** encoding without a [byte order mark](https://en.wikipedia.org/wiki/Byte_order_mark). _(editor default)_
- Use **Tabs** instead of spaces for indentation. _(editor default)_

#### Indentation

Each indent level should be one tab greater than the block containing it.

**Good**:

```glsl
void fragment() {
    COLOR = vec3(1.0, 1.0, 1.0);
}
```

**Bad**:

```glsl
void fragment() {
        COLOR = vec3(1.0, 1.0, 1.0);
}
```

Use 2 indent levels to distinguish continuation lines from regular code blocks.

**Good**:

```glsl
vec2 st = vec2(
        atan(NORMAL.x, NORMAL.z),
        acos(NORMAL.y));
```

**Bad**:

```glsl
vec2 st = vec2(
    atan(NORMAL.x, NORMAL.z),
    acos(NORMAL.y));
```

#### Line breaks and blank lines

For a general indentation rule, follow [the "1TBS Style"](<https://en.wikipedia.org/wiki/Indentation_style#Variant:_1TBS_(OTBS)>) which recommends placing the brace associated with a control statement on the same line. Always use braces for statements, even if they only span one line. This makes them easier to refactor and avoids mistakes when adding more lines to an `if` statement or similar.

**Good**:

```glsl
void fragment() {
    if (true) {
        // ...
    }
}
```

**Bad**:

```glsl
void fragment()
{
    if (true)
        // ...
}
```

#### Blank lines

Surround function definitions with one (and only one) blank line:

```glsl
void do_something() {
    // ...
}

void fragment() {
    // ...
}
```

Use one (and only one) blank line inside functions to separate logical sections.

#### Line length

Keep individual lines of code under 100 characters.

If you can, try to keep lines under 80 characters. This helps to read the code on small displays and with two shaders opened side-by-side in an external text editor. For example, when looking at a differential revision.

#### One statement per line

Never combine multiple statements on a single line.

**Good**:

```glsl
void fragment() {
    ALBEDO = vec3(1.0);
    EMISSION = vec3(1.0);
}
```

**Bad**:

```glsl
void fragment() {
    ALBEDO = vec3(1.0); EMISSION = vec3(1.0);
}
```

The only exception to that rule is the ternary operator:

```glsl
void fragment() {
     bool should_be_white = true;
     ALBEDO = should_be_white ? vec3(1.0) : vec3(0.0);
 }
```

#### Comment spacing

Regular comments should start with a space, but not code that you comment out. This helps differentiate text comments from disabled code.

**Good**:

```glsl
// This is a comment.
//return;
```

**Bad**:

```glsl
//This is a comment.
// return;
```

Don't use multiline comment syntax if your comment can fit on a single line:

```glsl
/* This is another comment. */
```

> **Note:** In the shader editor, to make the selected code a comment (or uncomment it), press Ctrl + K. This feature adds or removes `//` at the start of the selected lines.

#### Documentation comments

Use the following format for documentation comments above uniforms, with **two** leading asterisks (`/**`) and follow-up asterisks on every line:

```glsl
/**
 * This is a documentation comment.
 * These lines will appear in the inspector when hovering the shader parameter
 * named "Something".
 * You can use [b]BBCode[/b] [i]formatting[/i] in the comment.
 */
uniform int something = 1;
```

These comments will appear when hovering a property in the inspector. If you don't wish the comment to be visible in the inspector, use the standard comment syntax instead (`// ...` or `/* ... */` with only one leading asterisk).

#### Whitespace

Always use one space around operators and after commas. Also, avoid extraneous spaces in function calls.

**Good**:

```glsl
COLOR.r = 5.0;
COLOR.r = COLOR.g + 0.1;
COLOR.b = some_function(1.0, 2.0);
```

**Bad**:

```glsl
COLOR.r=5.0;
COLOR.r = COLOR.g+0.1;
COLOR.b = some_function (1.0,2.0);
```

Don't use spaces to align expressions vertically:

```glsl
ALBEDO.r   = 1.0;
EMISSION.r = 1.0;
```

#### Floating-point numbers

Always specify at least one digit for both the integer and fractional part. This makes it easier to distinguish floating-point numbers from integers, as well as distinguishing numbers greater than 1 from those lower than 1.

**Good**:

```glsl
void fragment() {
    ALBEDO.rgb = vec3(5.0, 0.1, 0.2);
}
```

**Bad**:

```glsl
void fragment() {
    ALBEDO.rgb = vec3(5., .1, .2);
}
```

### Accessing vector members

Use `r`, `g`, `b`, and `a` when accessing a vector's members if it contains a color. If the vector contains anything else than a color, use `x`, `y`, `z`, and `w`. This allows those reading your code to better understand what the underlying data represents.

**Good**:

```glsl
COLOR.rgb = vec3(5.0, 0.1, 0.2);
```

**Bad**:

```glsl
COLOR.xyz = vec3(5.0, 0.1, 0.2);
```

### Naming conventions

These naming conventions follow the Godot Engine style. Breaking these will make your code clash with the built-in naming conventions, leading to inconsistent code.

#### Functions and variables

Use snake_case to name functions and variables:

```glsl
void some_function() {
     float some_variable = 0.5;
}
```

#### Constants

Write constants with CONSTANT*CASE, that is to say in all caps with an underscore (*) to separate words:

```glsl
const float GOLDEN_RATIO = 1.618;
```

#### Preprocessor directives

Shader preprocessor directives should be written in CONSTANT\_\_CASE. Directives should be written without any indentation before them, even if nested within a function.

To preserve the natural flow of indentation when shader errors are printed to the console, extra indentation should **not** be added within `#if`, `#ifdef` or `#ifndef` blocks:

**Good**:

```glsl
#define HEIGHTMAP_ENABLED

void fragment() {
    vec2 position = vec2(1.0, 2.0);

#ifdef HEIGHTMAP_ENABLED
    sample_heightmap(position);
#endif
}
```

**Bad**:

```glsl
#define heightmap_enabled

void fragment() {
    vec2 position = vec2(1.0, 2.0);

    #ifdef heightmap_enabled
        sample_heightmap(position);
    #endif
}
```

### Applying formatting automatically

To automatically format shader files, you can use [clang-format](https://clang.llvm.org/docs/ClangFormat.html) on one or several `.gdshader` files, as the syntax is close enough to a C-style language.

However, the default style in clang-format doesn't follow this style guide, so you need to save this file as `.clang-format` in your project's root folder:

```yaml
BasedOnStyle: LLVM
AlignAfterOpenBracket: DontAlign
AlignOperands: DontAlign
AlignTrailingComments:
    Kind: Never
    OverEmptyLines: 0
AllowAllParametersOfDeclarationOnNextLine: false
AllowShortFunctionsOnASingleLine: Inline
BreakConstructorInitializers: AfterColon
ColumnLimit: 0
ContinuationIndentWidth: 8
IndentCaseLabels: true
IndentWidth: 4
InsertBraces: true
KeepEmptyLinesAtTheStartOfBlocks: false
RemoveSemicolon: true
SpacesInLineCommentPrefix:
    Minimum: 0 # We want a minimum of 1 for comments, but allow 0 for disabled code.
    Maximum: -1
TabWidth: 4
UseTab: Always
```

While in the project root, you can then call `clang-format -i path/to/shader.gdshader` in a terminal to format a single shader file, or `clang-format -i path/to/folder/*.gdshader` to format all shaders in a folder.

### Code order

We suggest to organize shader code this way:

```glsl
01. shader type declaration
02. render mode declaration
03. // docstring

04. uniforms
05. constants
06. varyings

07. other functions
08. vertex() function
09. fragment() function
10. light() function
```

We optimized the order to make it easy to read the code from top to bottom, to help developers reading the code for the first time understand how it works, and to avoid errors linked to the order of variable declarations.

This code order follows two rules of thumb:

1. Metadata and properties first, followed by methods.
2. "Public" comes before "private". In a shader language's context, "public" refers to what's easily adjustable by the user (uniforms).

#### Local variables

Declare local variables as close as possible to their first use. This makes it easier to follow the code, without having to scroll too much to find where the variable was declared.

---
