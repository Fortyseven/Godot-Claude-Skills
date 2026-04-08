# Godot 4 GDScript API Reference — Rendering

> GDScript-only reference. 148 classes.

### ArrayMesh
*Inherits: **Mesh < Resource < RefCounted < Object***

The ArrayMesh is used to construct a Mesh by specifying the attributes as arrays.

**Properties**
- `BlendShapeMode blend_shape_mode` = `1`
- `AABB custom_aabb` = `AABB(0, 0, 0, 0, 0, 0)`
- `ArrayMesh shadow_mesh`

**Methods**
- `void add_blend_shape(name: StringName)`
- `void add_surface_from_arrays(primitive: PrimitiveType, arrays: Array, blend_shapes: Array[Array] = [], lods: Dictionary = {}, flags: BitField[ArrayFormat] = 0)`
- `void clear_blend_shapes()`
- `void clear_surfaces()`
- `int get_blend_shape_count() const`
- `StringName get_blend_shape_name(index: int) const`
- `Error lightmap_unwrap(transform: Transform3D, texel_size: float)`
- `void regen_normal_maps()`
- `void set_blend_shape_name(index: int, name: StringName)`
- `int surface_find_by_name(name: String) const`
- `int surface_get_array_index_len(surf_idx: int) const`
- `int surface_get_array_len(surf_idx: int) const`
- `BitField[ArrayFormat] surface_get_format(surf_idx: int) const`
- `String surface_get_name(surf_idx: int) const`
- `PrimitiveType surface_get_primitive_type(surf_idx: int) const`
- `void surface_remove(surf_idx: int)`
- `void surface_set_name(surf_idx: int, name: String)`
- `void surface_update_attribute_region(surf_idx: int, offset: int, data: PackedByteArray)`
- `void surface_update_skin_region(surf_idx: int, offset: int, data: PackedByteArray)`
- `void surface_update_vertex_region(surf_idx: int, offset: int, data: PackedByteArray)`

**GDScript Examples**
```gdscript
var vertices = PackedVector3Array()
vertices.push_back(Vector3(0, 1, 0))
vertices.push_back(Vector3(1, 0, 0))
vertices.push_back(Vector3(0, 0, 1))

# Initialize the ArrayMesh.
var arr_mesh = ArrayMesh.new()
var arrays = []
arrays.resize(Mesh.ARRAY_MAX)
arrays[Mesh.ARRAY_VERTEX] = vertices

# Create the Mesh.
arr_mesh.add_surface_from_arrays(Mesh.PRIMITIVE_TRIANGLES, arrays)
var m = MeshInstance3D.new()
m.mesh = arr_mesh
```

### BaseMaterial3D
*Inherits: **Material < Resource < RefCounted < Object** | Inherited by: ORMMaterial3D, StandardMaterial3D*

This class serves as a default material with a wide variety of rendering features and properties without the need to write shader code. See the tutorial below for details.

**Properties**
- `Color albedo_color` = `Color(1, 1, 1, 1)`
- `Texture2D albedo_texture`
- `bool albedo_texture_force_srgb` = `false`
- `bool albedo_texture_msdf` = `false`
- `float alpha_antialiasing_edge`
- `AlphaAntiAliasing alpha_antialiasing_mode`
- `float alpha_hash_scale`
- `float alpha_scissor_threshold`
- `float anisotropy` = `0.0`
- `bool anisotropy_enabled` = `false`
- `Texture2D anisotropy_flowmap`
- `bool ao_enabled` = `false`
- `float ao_light_affect` = `0.0`
- `bool ao_on_uv2` = `false`
- `Texture2D ao_texture`
- `TextureChannel ao_texture_channel` = `0`
- `Color backlight` = `Color(0, 0, 0, 1)`
- `bool backlight_enabled` = `false`
- `Texture2D backlight_texture`
- `bool bent_normal_enabled` = `false`
- `Texture2D bent_normal_texture`
- `bool billboard_keep_scale` = `false`
- `BillboardMode billboard_mode` = `0`
- `BlendMode blend_mode` = `0`
- `float clearcoat` = `1.0`
- `bool clearcoat_enabled` = `false`
- `float clearcoat_roughness` = `0.5`
- `Texture2D clearcoat_texture`
- `CullMode cull_mode` = `0`
- `DepthDrawMode depth_draw_mode` = `0`

**Methods**
- `bool get_feature(feature: Feature) const`
- `bool get_flag(flag: Flags) const`
- `Texture2D get_texture(param: TextureParam) const`
- `void set_feature(feature: Feature, enable: bool)`
- `void set_flag(flag: Flags, enable: bool)`
- `void set_texture(param: TextureParam, texture: Texture2D)`

### BoxMesh
*Inherits: **PrimitiveMesh < Mesh < Resource < RefCounted < Object***

Generate an axis-aligned box PrimitiveMesh.

**Properties**
- `Vector3 size` = `Vector3(1, 1, 1)`
- `int subdivide_depth` = `0`
- `int subdivide_height` = `0`
- `int subdivide_width` = `0`

### CameraAttributesPhysical
*Inherits: **CameraAttributes < Resource < RefCounted < Object***

CameraAttributesPhysical is used to set rendering settings based on a physically-based camera's settings. It is responsible for exposure, auto-exposure, and depth of field.

**Properties**
- `float auto_exposure_max_exposure_value` = `10.0`
- `float auto_exposure_min_exposure_value` = `-8.0`
- `float exposure_aperture` = `16.0`
- `float exposure_shutter_speed` = `100.0`
- `float frustum_far` = `4000.0`
- `float frustum_focal_length` = `35.0`
- `float frustum_focus_distance` = `10.0`
- `float frustum_near` = `0.05`

**Methods**
- `float get_fov() const`

### CameraAttributesPractical
*Inherits: **CameraAttributes < Resource < RefCounted < Object***

Controls camera-specific attributes such as auto-exposure, depth of field, and exposure override.

**Properties**
- `float auto_exposure_max_sensitivity` = `800.0`
- `float auto_exposure_min_sensitivity` = `0.0`
- `float dof_blur_amount` = `0.1`
- `float dof_blur_far_distance` = `10.0`
- `bool dof_blur_far_enabled` = `false`
- `float dof_blur_far_transition` = `5.0`
- `float dof_blur_near_distance` = `2.0`
- `bool dof_blur_near_enabled` = `false`
- `float dof_blur_near_transition` = `1.0`

### CameraAttributes
*Inherits: **Resource < RefCounted < Object** | Inherited by: CameraAttributesPhysical, CameraAttributesPractical*

Controls camera-specific attributes such as depth of field and exposure override.

**Properties**
- `bool auto_exposure_enabled` = `false`
- `float auto_exposure_scale` = `0.4`
- `float auto_exposure_speed` = `0.5`
- `float exposure_multiplier` = `1.0`
- `float exposure_sensitivity` = `100.0`

### CapsuleMesh
*Inherits: **PrimitiveMesh < Mesh < Resource < RefCounted < Object***

Class representing a capsule-shaped PrimitiveMesh.

**Properties**
- `float height` = `2.0`
- `int radial_segments` = `64`
- `float radius` = `0.5`
- `int rings` = `8`

### CompositorEffect
*Inherits: **Resource < RefCounted < Object***

This resource defines a custom rendering effect that can be applied to Viewports through the viewports' Environment. You can implement a callback that is called during rendering at a given stage of the rendering pipeline and allows you to insert additional passes. Note that this callback happens on the rendering thread. CompositorEffect is an abstract base class and must be extended to implement specific rendering logic.

**Properties**
- `bool access_resolved_color`
- `bool access_resolved_depth`
- `EffectCallbackType effect_callback_type`
- `bool enabled`
- `bool needs_motion_vectors`
- `bool needs_normal_roughness`
- `bool needs_separate_specular`

**Methods**
- `void _render_callback(effect_callback_type: int, render_data: RenderData) virtual`

**GDScript Examples**
```gdscript
var render_scene_buffers = render_data.get_render_scene_buffers()
var color_buffer = render_scene_buffers.get_texture("render_buffers", "color")
```
```gdscript
var render_scene_buffers = render_data.get_render_scene_buffers()
var depth_buffer = render_scene_buffers.get_texture("render_buffers", "depth")
```

### Compositor
*Inherits: **Resource < RefCounted < Object***

The compositor resource stores attributes used to customize how a Viewport is rendered.

**Properties**
- `Array[CompositorEffect] compositor_effects` = `[]`

### CylinderMesh
*Inherits: **PrimitiveMesh < Mesh < Resource < RefCounted < Object***

Class representing a cylindrical PrimitiveMesh. This class can be used to create cones by setting either the top_radius or bottom_radius properties to 0.0.

**Properties**
- `float bottom_radius` = `0.5`
- `bool cap_bottom` = `true`
- `bool cap_top` = `true`
- `float height` = `2.0`
- `int radial_segments` = `64`
- `int rings` = `4`
- `float top_radius` = `0.5`

### Environment
*Inherits: **Resource < RefCounted < Object***

Resource for environment nodes (like WorldEnvironment) that define multiple environment operations (such as background Sky or Color, ambient light, fog, depth-of-field...). These parameters affect the final render of the scene. The order of these operations is:

**Properties**
- `float adjustment_brightness` = `1.0`
- `Texture adjustment_color_correction`
- `float adjustment_contrast` = `1.0`
- `bool adjustment_enabled` = `false`
- `float adjustment_saturation` = `1.0`
- `Color ambient_light_color` = `Color(0, 0, 0, 1)`
- `float ambient_light_energy` = `1.0`
- `float ambient_light_sky_contribution` = `1.0`
- `AmbientSource ambient_light_source` = `0`
- `int background_camera_feed_id` = `1`
- `int background_canvas_max_layer` = `0`
- `Color background_color` = `Color(0, 0, 0, 1)`
- `float background_energy_multiplier` = `1.0`
- `float background_intensity` = `30000.0`
- `BGMode background_mode` = `0`
- `float fog_aerial_perspective` = `0.0`
- `float fog_density` = `0.01`
- `float fog_depth_begin` = `10.0`
- `float fog_depth_curve` = `1.0`
- `float fog_depth_end` = `100.0`
- `bool fog_enabled` = `false`
- `float fog_height` = `0.0`
- `float fog_height_density` = `0.0`
- `Color fog_light_color` = `Color(0.518, 0.553, 0.608, 1)`
- `float fog_light_energy` = `1.0`
- `FogMode fog_mode` = `0`
- `float fog_sky_affect` = `1.0`
- `float fog_sun_scatter` = `0.0`
- `GlowBlendMode glow_blend_mode` = `1`
- `float glow_bloom` = `0.0`

**Methods**
- `float get_glow_level(idx: int) const`
- `void set_glow_level(idx: int, intensity: float)`

### ImmediateMesh
*Inherits: **Mesh < Resource < RefCounted < Object***

A mesh type optimized for creating geometry manually, similar to OpenGL 1.x immediate mode.

**Methods**
- `void clear_surfaces()`
- `void surface_add_vertex(vertex: Vector3)`
- `void surface_add_vertex_2d(vertex: Vector2)`
- `void surface_begin(primitive: PrimitiveType, material: Material = null)`
- `void surface_end()`
- `void surface_set_color(color: Color)`
- `void surface_set_normal(normal: Vector3)`
- `void surface_set_tangent(tangent: Plane)`
- `void surface_set_uv(uv: Vector2)`
- `void surface_set_uv2(uv2: Vector2)`

**GDScript Examples**
```gdscript
var mesh = ImmediateMesh.new()
mesh.surface_begin(Mesh.PRIMITIVE_TRIANGLES)
mesh.surface_add_vertex(Vector3.LEFT)
mesh.surface_add_vertex(Vector3.FORWARD)
mesh.surface_add_vertex(Vector3.ZERO)
mesh.surface_end()
```

### Material
*Inherits: **Resource < RefCounted < Object** | Inherited by: BaseMaterial3D, CanvasItemMaterial, FogMaterial, PanoramaSkyMaterial, ParticleProcessMaterial, PhysicalSkyMaterial, ...*

Material is a base resource used for coloring and shading geometry. All materials inherit from it and almost all VisualInstance3D derived nodes carry a Material. A few flags and parameters are shared between all material types and are configured here.

**Properties**
- `Material next_pass`
- `int render_priority`

**Methods**
- `bool _can_do_next_pass() virtual const`
- `bool _can_use_render_priority() virtual const`
- `Mode _get_shader_mode() virtual required const`
- `RID _get_shader_rid() virtual required const`
- `Resource create_placeholder() const`
- `void inspect_native_shader_code()`

### MeshDataTool
*Inherits: **RefCounted < Object***

MeshDataTool provides access to individual vertices in a Mesh. It allows users to read and edit vertex data of meshes. It also creates an array of faces and edges.

**Methods**
- `void clear()`
- `Error commit_to_surface(mesh: ArrayMesh, compression_flags: int = 0)`
- `Error create_from_surface(mesh: ArrayMesh, surface: int)`
- `int get_edge_count() const`
- `PackedInt32Array get_edge_faces(idx: int) const`
- `Variant get_edge_meta(idx: int) const`
- `int get_edge_vertex(idx: int, vertex: int) const`
- `int get_face_count() const`
- `int get_face_edge(idx: int, edge: int) const`
- `Variant get_face_meta(idx: int) const`
- `Vector3 get_face_normal(idx: int) const`
- `int get_face_vertex(idx: int, vertex: int) const`
- `int get_format() const`
- `Material get_material() const`
- `Vector3 get_vertex(idx: int) const`
- `PackedInt32Array get_vertex_bones(idx: int) const`
- `Color get_vertex_color(idx: int) const`
- `int get_vertex_count() const`
- `PackedInt32Array get_vertex_edges(idx: int) const`
- `PackedInt32Array get_vertex_faces(idx: int) const`
- `Variant get_vertex_meta(idx: int) const`
- `Vector3 get_vertex_normal(idx: int) const`
- `Plane get_vertex_tangent(idx: int) const`
- `Vector2 get_vertex_uv(idx: int) const`
- `Vector2 get_vertex_uv2(idx: int) const`
- `PackedFloat32Array get_vertex_weights(idx: int) const`
- `void set_edge_meta(idx: int, meta: Variant)`
- `void set_face_meta(idx: int, meta: Variant)`
- `void set_material(material: Material)`
- `void set_vertex(idx: int, vertex: Vector3)`
- `void set_vertex_bones(idx: int, bones: PackedInt32Array)`
- `void set_vertex_color(idx: int, color: Color)`
- `void set_vertex_meta(idx: int, meta: Variant)`
- `void set_vertex_normal(idx: int, normal: Vector3)`
- `void set_vertex_tangent(idx: int, tangent: Plane)`
- `void set_vertex_uv(idx: int, uv: Vector2)`
- `void set_vertex_uv2(idx: int, uv2: Vector2)`
- `void set_vertex_weights(idx: int, weights: PackedFloat32Array)`

**GDScript Examples**
```gdscript
var mesh = ArrayMesh.new()
mesh.add_surface_from_arrays(Mesh.PRIMITIVE_TRIANGLES, BoxMesh.new().get_mesh_arrays())
var mdt = MeshDataTool.new()
mdt.create_from_surface(mesh, 0)
for i in range(mdt.get_vertex_count()):
    var vertex = mdt.get_vertex(i)
    # In this example we extend the mesh by one unit, which results in separated faces as it is flat shaded.
    vertex += mdt.get_vertex_normal(i)
    # Save your change.
    mdt.set_vertex(i, vertex)
mesh.clear_surfaces()
mdt.commit_to_surface(mesh)
var mi = MeshInstance.new()
mi.mesh = mesh
add_child(mi)
```
```gdscript
var index = mesh_data_tool.get_face_vertex(0, 1) # Gets the index of the second vertex of the first face.
var position = mesh_data_tool.get_vertex(index)
var normal = mesh_data_tool.get_vertex_normal(index)
```

### MultiMesh
*Inherits: **Resource < RefCounted < Object***

MultiMesh provides low-level mesh instancing. Drawing thousands of MeshInstance3D nodes can be slow, since each object is submitted to the GPU then drawn individually.

**Properties**
- `PackedFloat32Array buffer` = `PackedFloat32Array()`
- `PackedColorArray color_array`
- `AABB custom_aabb` = `AABB(0, 0, 0, 0, 0, 0)`
- `PackedColorArray custom_data_array`
- `int instance_count` = `0`
- `Mesh mesh`
- `PhysicsInterpolationQuality physics_interpolation_quality` = `0`
- `PackedVector2Array transform_2d_array`
- `PackedVector3Array transform_array`
- `TransformFormat transform_format` = `0`
- `bool use_colors` = `false`
- `bool use_custom_data` = `false`
- `int visible_instance_count` = `-1`

**Methods**
- `AABB get_aabb() const`
- `Color get_instance_color(instance: int) const`
- `Color get_instance_custom_data(instance: int) const`
- `Transform3D get_instance_transform(instance: int) const`
- `Transform2D get_instance_transform_2d(instance: int) const`
- `void reset_instance_physics_interpolation(instance: int)`
- `void reset_instances_physics_interpolation()`
- `void set_buffer_interpolated(buffer_curr: PackedFloat32Array, buffer_prev: PackedFloat32Array)`
- `void set_instance_color(instance: int, color: Color)`
- `void set_instance_custom_data(instance: int, custom_data: Color)`
- `void set_instance_transform(instance: int, transform: Transform3D)`
- `void set_instance_transform_2d(instance: int, transform: Transform2D)`

### ORMMaterial3D
*Inherits: **BaseMaterial3D < Material < Resource < RefCounted < Object***

ORMMaterial3D's properties are inherited from BaseMaterial3D. Unlike StandardMaterial3D, ORMMaterial3D uses a single texture for ambient occlusion, roughness and metallic maps, known as an ORM texture.

### ParticleProcessMaterial
*Inherits: **Material < Resource < RefCounted < Object***

ParticleProcessMaterial defines particle properties and behavior. It is used in the process_material of the GPUParticles2D and GPUParticles3D nodes. Some of this material's properties are applied to each particle when emitted, while others can have a CurveTexture or a GradientTexture1D applied to vary numerical or color values over the lifetime of the particle.

**Properties**
- `Texture2D alpha_curve`
- `Texture2D angle_curve`
- `float angle_max` = `0.0`
- `float angle_min` = `0.0`
- `Texture2D angular_velocity_curve`
- `float angular_velocity_max` = `0.0`
- `float angular_velocity_min` = `0.0`
- `Texture2D anim_offset_curve`
- `float anim_offset_max` = `0.0`
- `float anim_offset_min` = `0.0`
- `Texture2D anim_speed_curve`
- `float anim_speed_max` = `0.0`
- `float anim_speed_min` = `0.0`
- `bool attractor_interaction_enabled` = `true`
- `float collision_bounce`
- `float collision_friction`
- `CollisionMode collision_mode` = `0`
- `bool collision_use_scale` = `false`
- `Color color` = `Color(1, 1, 1, 1)`
- `Texture2D color_initial_ramp`
- `Texture2D color_ramp`
- `Texture2D damping_curve`
- `float damping_max` = `0.0`
- `float damping_min` = `0.0`
- `Vector3 direction` = `Vector3(1, 0, 0)`
- `Texture2D directional_velocity_curve`
- `float directional_velocity_max`
- `float directional_velocity_min`
- `Vector3 emission_box_extents`
- `Texture2D emission_color_texture`

**Methods**
- `Vector2 get_param(param: Parameter) const`
- `float get_param_max(param: Parameter) const`
- `float get_param_min(param: Parameter) const`
- `Texture2D get_param_texture(param: Parameter) const`
- `bool get_particle_flag(particle_flag: ParticleFlags) const`
- `void set_param(param: Parameter, value: Vector2)`
- `void set_param_max(param: Parameter, value: float)`
- `void set_param_min(param: Parameter, value: float)`
- `void set_param_texture(param: Parameter, texture: Texture2D)`
- `void set_particle_flag(particle_flag: ParticleFlags, enable: bool)`

### PlaneMesh
*Inherits: **PrimitiveMesh < Mesh < Resource < RefCounted < Object** | Inherited by: QuadMesh*

Class representing a planar PrimitiveMesh. This flat mesh does not have a thickness. By default, this mesh is aligned on the X and Z axes; this default rotation isn't suited for use with billboarded materials. For billboarded materials, change orientation to FACE_Z.

**Properties**
- `Vector3 center_offset` = `Vector3(0, 0, 0)`
- `Orientation orientation` = `1`
- `Vector2 size` = `Vector2(2, 2)`
- `int subdivide_depth` = `0`
- `int subdivide_width` = `0`

### PrimitiveMesh
*Inherits: **Mesh < Resource < RefCounted < Object** | Inherited by: BoxMesh, CapsuleMesh, CylinderMesh, PlaneMesh, PointMesh, PrismMesh, ...*

Base class for all primitive meshes. Handles applying a Material to a primitive mesh. Examples include BoxMesh, CapsuleMesh, CylinderMesh, PlaneMesh, PrismMesh, and SphereMesh.

**Properties**
- `bool add_uv2` = `false`
- `AABB custom_aabb` = `AABB(0, 0, 0, 0, 0, 0)`
- `bool flip_faces` = `false`
- `Material material`
- `float uv2_padding` = `2.0`

**Methods**
- `Array _create_mesh_array() virtual const`
- `Array get_mesh_arrays() const`
- `void request_update()`

**GDScript Examples**
```gdscript
var c = CylinderMesh.new()
var arr_mesh = ArrayMesh.new()
arr_mesh.add_surface_from_arrays(Mesh.PRIMITIVE_TRIANGLES, c.get_mesh_arrays())
```

### QuadMesh
*Inherits: **PlaneMesh < PrimitiveMesh < Mesh < Resource < RefCounted < Object***

Class representing a square PrimitiveMesh. This flat mesh does not have a thickness. By default, this mesh is aligned on the X and Y axes; this rotation is more suited for use with billboarded materials. A QuadMesh is equivalent to a PlaneMesh except its default PlaneMesh.orientation is PlaneMesh.FACE_Z.

**Properties**
- `Orientation orientation` = `2 (overrides PlaneMesh)`
- `Vector2 size` = `Vector2(1, 1) (overrides PlaneMesh)`

### RDShaderFile
*Inherits: **Resource < RefCounted < Object***

Compiled shader file in SPIR-V form.

**Properties**
- `String base_error` = `""`

**Methods**
- `RDShaderSPIRV get_spirv(version: StringName = &"") const`
- `Array[StringName] get_version_list() const`
- `void set_bytecode(bytecode: RDShaderSPIRV, version: StringName = &"")`

### RenderingDevice
*Inherits: **Object***

RenderingDevice is an abstraction for working with modern low-level graphics APIs such as Vulkan. Compared to RenderingServer (which works with Godot's own rendering subsystems), RenderingDevice is much lower-level and allows working more directly with the underlying graphics APIs. RenderingDevice is used in Godot to provide support for several modern low-level graphics APIs while reducing the amount of code duplication required. RenderingDevice can also be used in your own projects to perform things that are not exposed by RenderingServer or high-level nodes, such as using compute shaders.

**Methods**
- `void barrier(from: BitField[BarrierMask] = 32767, to: BitField[BarrierMask] = 32767)`
- `Error buffer_clear(buffer: RID, offset: int, size_bytes: int)`
- `Error buffer_copy(src_buffer: RID, dst_buffer: RID, src_offset: int, dst_offset: int, size: int)`
- `PackedByteArray buffer_get_data(buffer: RID, offset_bytes: int = 0, size_bytes: int = 0)`
- `Error buffer_get_data_async(buffer: RID, callback: Callable, offset_bytes: int = 0, size_bytes: int = 0)`
- `int buffer_get_device_address(buffer: RID)`
- `Error buffer_update(buffer: RID, offset: int, size_bytes: int, data: PackedByteArray)`
- `void capture_timestamp(name: String)`
- `void compute_list_add_barrier(compute_list: int)`
- `int compute_list_begin()`
- `void compute_list_bind_compute_pipeline(compute_list: int, compute_pipeline: RID)`
- `void compute_list_bind_uniform_set(compute_list: int, uniform_set: RID, set_index: int)`
- `void compute_list_dispatch(compute_list: int, x_groups: int, y_groups: int, z_groups: int)`
- `void compute_list_dispatch_indirect(compute_list: int, buffer: RID, offset: int)`
- `void compute_list_end()`
- `void compute_list_set_push_constant(compute_list: int, buffer: PackedByteArray, size_bytes: int)`
- `RID compute_pipeline_create(shader: RID, specialization_constants: Array[RDPipelineSpecializationConstant] = [])`
- `bool compute_pipeline_is_valid(compute_pipeline: RID)`
- `RenderingDevice create_local_device()`
- `void draw_command_begin_label(name: String, color: Color)`
- `void draw_command_end_label()`
- `void draw_command_insert_label(name: String, color: Color)`
- `int draw_list_begin(framebuffer: RID, draw_flags: BitField[DrawFlags] = 0, clear_color_values: PackedColorArray = PackedColorArray(), clear_depth_value: float = 1.0, clear_stencil_value: int = 0, region: Rect2 = Rect2(0, 0, 0, 0), breadcrumb: int = 0)`
- `int draw_list_begin_for_screen(screen: int = 0, clear_color: Color = Color(0, 0, 0, 1))`
- `PackedInt64Array draw_list_begin_split(framebuffer: RID, splits: int, initial_color_action: InitialAction, final_color_action: FinalAction, initial_depth_action: InitialAction, final_depth_action: FinalAction, clear_color_values: PackedColorArray = PackedColorArray(), clear_depth: float = 1.0, clear_stencil: int = 0, region: Rect2 = Rect2(0, 0, 0, 0), storage_textures: Array[RID] = [])`
- `void draw_list_bind_index_array(draw_list: int, index_array: RID)`
- `void draw_list_bind_render_pipeline(draw_list: int, render_pipeline: RID)`
- `void draw_list_bind_uniform_set(draw_list: int, uniform_set: RID, set_index: int)`
- `void draw_list_bind_vertex_array(draw_list: int, vertex_array: RID)`
- `void draw_list_bind_vertex_buffers_format(draw_list: int, vertex_format: int, vertex_count: int, vertex_buffers: Array[RID], offsets: PackedInt64Array = PackedInt64Array())`
- `void draw_list_disable_scissor(draw_list: int)`
- `void draw_list_draw(draw_list: int, use_indices: bool, instances: int, procedural_vertex_count: int = 0)`
- `void draw_list_draw_indirect(draw_list: int, use_indices: bool, buffer: RID, offset: int = 0, draw_count: int = 1, stride: int = 0)`
- `void draw_list_enable_scissor(draw_list: int, rect: Rect2 = Rect2(0, 0, 0, 0))`
- `void draw_list_end()`
- `void draw_list_set_blend_constants(draw_list: int, color: Color)`
- `void draw_list_set_push_constant(draw_list: int, buffer: PackedByteArray, size_bytes: int)`
- `int draw_list_switch_to_next_pass()`
- `PackedInt64Array draw_list_switch_to_next_pass_split(splits: int)`
- `RID framebuffer_create(textures: Array[RID], validate_with_format: int = -1, view_count: int = 1)`

**GDScript Examples**
```gdscript
rd = RenderingServer.get_rendering_device()

if rd.has_feature(RenderingDevice.SUPPORTS_BUFFER_DEVICE_ADDRESS):
    storage_buffer = rd.storage_buffer_create(bytes.size(), bytes, RenderingDevice.STORAGE_BUFFER_USAGE_SHADER_DEVICE_ADDRESS)
    storage_buffer_address = rd.buffer_get_device_address(storage_buffer)
```
```gdscript
func _buffer_get_data_callback(array):
    value = array.decode_u32(0)

...

rd.buffer_get_data_async(buffer, _buffer_get_data_callback)
```

### RenderingServer
*Inherits: **Object***

The rendering server is the API backend for everything visible. The whole scene system mounts on it to display. The rendering server is completely opaque: the internals are entirely implementation-specific and cannot be accessed.

**Properties**
- `bool render_loop_enabled`

**Methods**
- `Array[Image] bake_render_uv2(base: RID, material_overrides: Array[RID], image_size: Vector2i)`
- `void call_on_render_thread(callable: Callable)`
- `RID camera_attributes_create()`
- `void camera_attributes_set_auto_exposure(camera_attributes: RID, enable: bool, min_sensitivity: float, max_sensitivity: float, speed: float, scale: float)`
- `void camera_attributes_set_dof_blur(camera_attributes: RID, far_enable: bool, far_distance: float, far_transition: float, near_enable: bool, near_distance: float, near_transition: float, amount: float)`
- `void camera_attributes_set_dof_blur_bokeh_shape(shape: DOFBokehShape)`
- `void camera_attributes_set_dof_blur_quality(quality: DOFBlurQuality, use_jitter: bool)`
- `void camera_attributes_set_exposure(camera_attributes: RID, multiplier: float, normalization: float)`
- `RID camera_create()`
- `void camera_set_camera_attributes(camera: RID, effects: RID)`
- `void camera_set_compositor(camera: RID, compositor: RID)`
- `void camera_set_cull_mask(camera: RID, layers: int)`
- `void camera_set_environment(camera: RID, env: RID)`
- `void camera_set_frustum(camera: RID, size: float, offset: Vector2, z_near: float, z_far: float)`
- `void camera_set_orthogonal(camera: RID, size: float, z_near: float, z_far: float)`
- `void camera_set_perspective(camera: RID, fovy_degrees: float, z_near: float, z_far: float)`
- `void camera_set_transform(camera: RID, transform: Transform3D)`
- `void camera_set_use_vertical_aspect(camera: RID, enable: bool)`
- `RID canvas_create()`
- `void canvas_item_add_animation_slice(item: RID, animation_length: float, slice_begin: float, slice_end: float, offset: float = 0.0)`
- `void canvas_item_add_circle(item: RID, pos: Vector2, radius: float, color: Color, antialiased: bool = false)`
- `void canvas_item_add_clip_ignore(item: RID, ignore: bool)`
- `void canvas_item_add_ellipse(item: RID, pos: Vector2, major: float, minor: float, color: Color, antialiased: bool = false)`
- `void canvas_item_add_lcd_texture_rect_region(item: RID, rect: Rect2, texture: RID, src_rect: Rect2, modulate: Color)`
- `void canvas_item_add_line(item: RID, from: Vector2, to: Vector2, color: Color, width: float = -1.0, antialiased: bool = false)`
- `void canvas_item_add_mesh(item: RID, mesh: RID, transform: Transform2D = Transform2D(1, 0, 0, 1, 0, 0), modulate: Color = Color(1, 1, 1, 1), texture: RID = RID())`
- `void canvas_item_add_msdf_texture_rect_region(item: RID, rect: Rect2, texture: RID, src_rect: Rect2, modulate: Color = Color(1, 1, 1, 1), outline_size: int = 0, px_range: float = 1.0, scale: float = 1.0)`
- `void canvas_item_add_multiline(item: RID, points: PackedVector2Array, colors: PackedColorArray, width: float = -1.0, antialiased: bool = false)`
- `void canvas_item_add_multimesh(item: RID, mesh: RID, texture: RID = RID())`
- `void canvas_item_add_nine_patch(item: RID, rect: Rect2, source: Rect2, texture: RID, topleft: Vector2, bottomright: Vector2, x_axis_mode: NinePatchAxisMode = 0, y_axis_mode: NinePatchAxisMode = 0, draw_center: bool = true, modulate: Color = Color(1, 1, 1, 1))`
- `void canvas_item_add_particles(item: RID, particles: RID, texture: RID)`
- `void canvas_item_add_polygon(item: RID, points: PackedVector2Array, colors: PackedColorArray, uvs: PackedVector2Array = PackedVector2Array(), texture: RID = RID())`
- `void canvas_item_add_polyline(item: RID, points: PackedVector2Array, colors: PackedColorArray, width: float = -1.0, antialiased: bool = false)`
- `void canvas_item_add_primitive(item: RID, points: PackedVector2Array, colors: PackedColorArray, uvs: PackedVector2Array, texture: RID)`
- `void canvas_item_add_rect(item: RID, rect: Rect2, color: Color, antialiased: bool = false)`
- `void canvas_item_add_set_transform(item: RID, transform: Transform2D)`
- `void canvas_item_add_texture_rect(item: RID, rect: Rect2, texture: RID, tile: bool = false, modulate: Color = Color(1, 1, 1, 1), transpose: bool = false)`
- `void canvas_item_add_texture_rect_region(item: RID, rect: Rect2, texture: RID, src_rect: Rect2, modulate: Color = Color(1, 1, 1, 1), transpose: bool = false, clip_uv: bool = true)`
- `void canvas_item_add_triangle_array(item: RID, indices: PackedInt32Array, points: PackedVector2Array, colors: PackedColorArray, uvs: PackedVector2Array = PackedVector2Array(), bones: PackedInt32Array = PackedInt32Array(), weights: PackedFloat32Array = PackedFloat32Array(), texture: RID = RID(), count: int = -1)`
- `void canvas_item_attach_skeleton(item: RID, skeleton: RID)`

**GDScript Examples**
```gdscript
func _ready():
    RenderingServer.viewport_attach_to_screen(get_viewport().get_viewport_rid(), Rect2())
    RenderingServer.viewport_attach_to_screen($Viewport.get_viewport_rid(), Rect2(0, 0, 600, 600))
```
```gdscript
func get_exposure_normalization(ev100: float):
    return 1.0 / (pow(2.0, ev100) * 1.2)
```

### RibbonTrailMesh
*Inherits: **PrimitiveMesh < Mesh < Resource < RefCounted < Object***

RibbonTrailMesh represents a straight ribbon-shaped mesh with variable width. The ribbon is composed of a number of flat or cross-shaped sections, each with the same section_length and number of section_segments. A curve is sampled along the total length of the ribbon, meaning that the curve determines the size of the ribbon along its length.

**Properties**
- `Curve curve`
- `float section_length` = `0.2`
- `int section_segments` = `3`
- `int sections` = `5`
- `Shape shape` = `1`
- `float size` = `1.0`

### ShaderGlobalsOverride
*Inherits: **Node < Object***

Similar to how a WorldEnvironment node can be used to override the environment while a specific scene is loaded, ShaderGlobalsOverride can be used to override global shader parameters temporarily. Once the node is removed, the project-wide values for the global shader parameters are restored. See the RenderingServer global_shader_parameter_* methods for more information.

### ShaderIncludeDB
*Inherits: **Object***

This object contains shader fragments from Godot's internal shaders. These can be used when access to internal uniform buffers and/or internal functions is required for instance when composing compositor effects or compute shaders. Only fragments for the current rendering device are loaded.

**Methods**
- `String get_built_in_include_file(filename: String) static`
- `bool has_built_in_include_file(filename: String) static`
- `PackedStringArray list_built_in_include_files() static`

### ShaderInclude
*Inherits: **Resource < RefCounted < Object***

A shader include file, saved with the .gdshaderinc extension. This class allows you to define a custom shader snippet that can be included in a Shader by using the preprocessor directive #include, followed by the file path (e.g. #include "res://shader_lib.gdshaderinc"). The snippet doesn't have to be a valid shader on its own.

**Properties**
- `String code` = `""`

### ShaderMaterial
*Inherits: **Material < Resource < RefCounted < Object***

A material that uses a custom Shader program to render visual items (canvas items, meshes, skies, fog), or to process particles. Compared to other materials, ShaderMaterial gives deeper control over the generated shader code. For more information, see the shaders documentation index below.

**Properties**
- `Shader shader`

**Methods**
- `Variant get_shader_parameter(param: StringName) const`
- `void set_shader_parameter(param: StringName, value: Variant)`

### Shader
*Inherits: **Resource < RefCounted < Object** | Inherited by: VisualShader*

A custom shader program implemented in the Godot shading language, saved with the .gdshader extension.

**Properties**
- `String code` = `""`

**Methods**
- `Texture get_default_texture_parameter(name: StringName, index: int = 0) const`
- `Mode get_mode() const`
- `Array get_shader_uniform_list(get_groups: bool = false)`
- `void inspect_native_shader_code()`
- `void set_default_texture_parameter(name: StringName, texture: Texture, index: int = 0)`

### SphereMesh
*Inherits: **PrimitiveMesh < Mesh < Resource < RefCounted < Object***

Class representing a spherical PrimitiveMesh.

**Properties**
- `float height` = `1.0`
- `bool is_hemisphere` = `false`
- `int radial_segments` = `64`
- `float radius` = `0.5`
- `int rings` = `32`

### StandardMaterial3D
*Inherits: **BaseMaterial3D < Material < Resource < RefCounted < Object***

StandardMaterial3D's properties are inherited from BaseMaterial3D. StandardMaterial3D uses separate textures for ambient occlusion, roughness and metallic maps. To use a single ORM map for all 3 textures, use an ORMMaterial3D instead.

### SubViewport
*Inherits: **Viewport < Node < Object***

SubViewport Isolates a rectangular region of a scene to be displayed independently. This can be used, for example, to display UI in 3D space.

**Properties**
- `ClearMode render_target_clear_mode` = `0`
- `UpdateMode render_target_update_mode` = `2`
- `Vector2i size` = `Vector2i(512, 512)`
- `Vector2i size_2d_override` = `Vector2i(0, 0)`
- `bool size_2d_override_stretch` = `false`

### SurfaceTool
*Inherits: **RefCounted < Object***

The SurfaceTool is used to construct a Mesh by specifying vertex attributes individually. It can be used to construct a Mesh from a script. All properties except indices need to be added before calling add_vertex(). For example, to add vertex colors and UVs:

**Methods**
- `void add_index(index: int)`
- `void add_triangle_fan(vertices: PackedVector3Array, uvs: PackedVector2Array = PackedVector2Array(), colors: PackedColorArray = PackedColorArray(), uv2s: PackedVector2Array = PackedVector2Array(), normals: PackedVector3Array = PackedVector3Array(), tangents: Array[Plane] = [])`
- `void add_vertex(vertex: Vector3)`
- `void append_from(existing: Mesh, surface: int, transform: Transform3D)`
- `void begin(primitive: PrimitiveType)`
- `void clear()`
- `ArrayMesh commit(existing: ArrayMesh = null, flags: int = 0)`
- `Array commit_to_arrays()`
- `void create_from(existing: Mesh, surface: int)`
- `void create_from_arrays(arrays: Array, primitive_type: PrimitiveType = 3)`
- `void create_from_blend_shape(existing: Mesh, surface: int, blend_shape: String)`
- `void deindex()`
- `PackedInt32Array generate_lod(nd_threshold: float, target_index_count: int = 3)`
- `void generate_normals(flip: bool = false)`
- `void generate_tangents()`
- `AABB get_aabb() const`
- `CustomFormat get_custom_format(channel_index: int) const`
- `PrimitiveType get_primitive_type() const`
- `SkinWeightCount get_skin_weight_count() const`
- `void index()`
- `void optimize_indices_for_cache()`
- `void set_bones(bones: PackedInt32Array)`
- `void set_color(color: Color)`
- `void set_custom(channel_index: int, custom_color: Color)`
- `void set_custom_format(channel_index: int, format: CustomFormat)`
- `void set_material(material: Material)`
- `void set_normal(normal: Vector3)`
- `void set_skin_weight_count(count: SkinWeightCount)`
- `void set_smooth_group(index: int)`
- `void set_tangent(tangent: Plane)`
- `void set_uv(uv: Vector2)`
- `void set_uv2(uv2: Vector2)`
- `void set_weights(weights: PackedFloat32Array)`

**GDScript Examples**
```gdscript
var st = SurfaceTool.new()
st.begin(Mesh.PRIMITIVE_TRIANGLES)
st.set_color(Color(1, 0, 0))
st.set_uv(Vector2(0, 0))
st.add_vertex(Vector3(0, 0, 0))
```

### TubeTrailMesh
*Inherits: **PrimitiveMesh < Mesh < Resource < RefCounted < Object***

TubeTrailMesh represents a straight tube-shaped mesh with variable width. The tube is composed of a number of cylindrical sections, each with the same section_length and number of section_rings. A curve is sampled along the total length of the tube, meaning that the curve determines the radius of the tube along its length.

**Properties**
- `bool cap_bottom` = `true`
- `bool cap_top` = `true`
- `Curve curve`
- `int radial_steps` = `8`
- `float radius` = `0.5`
- `float section_length` = `0.2`
- `int section_rings` = `3`
- `int sections` = `5`

### ViewportTexture
*Inherits: **Texture2D < Texture < Resource < RefCounted < Object***

A ViewportTexture provides the content of a Viewport as a dynamic Texture2D. This can be used to combine the rendering of Control, Node2D and Node3D nodes. For example, you can use this texture to display a 3D scene inside a TextureRect, or a 2D overlay in a Sprite3D.

**Properties**
- `NodePath viewport_path` = `NodePath("")`

**GDScript Examples**
```gdscript
img.convert(Image.FORMAT_RGBA8)
img.linear_to_srgb()
```

### Viewport
*Inherits: **Node < Object** | Inherited by: SubViewport, Window*

A Viewport creates a different view into the screen, or a sub-view inside another viewport. Child 2D nodes will display on it, and child Camera3D 3D nodes will render on it too.

**Properties**
- `AnisotropicFiltering anisotropic_filtering_level` = `2`
- `bool audio_listener_enable_2d` = `false`
- `bool audio_listener_enable_3d` = `false`
- `int canvas_cull_mask` = `4294967295`
- `DefaultCanvasItemTextureFilter canvas_item_default_texture_filter` = `1`
- `DefaultCanvasItemTextureRepeat canvas_item_default_texture_repeat` = `0`
- `Transform2D canvas_transform`
- `DebugDraw debug_draw` = `0`
- `bool disable_3d` = `false`
- `float fsr_sharpness` = `0.2`
- `Transform2D global_canvas_transform`
- `bool gui_disable_input` = `false`
- `int gui_drag_threshold` = `10`
- `bool gui_embed_subwindows` = `false`
- `bool gui_snap_controls_to_pixels` = `true`
- `bool handle_input_locally` = `true`
- `float mesh_lod_threshold` = `1.0`
- `MSAA msaa_2d` = `0`
- `MSAA msaa_3d` = `0`
- `bool oversampling` = `true`
- `float oversampling_override` = `0.0`
- `bool own_world_3d` = `false`
- `PhysicsInterpolationMode physics_interpolation_mode` = `1 (overrides Node)`
- `bool physics_object_picking` = `false`
- `bool physics_object_picking_first_only` = `false`
- `bool physics_object_picking_sort` = `false`
- `bool positional_shadow_atlas_16_bits` = `true`
- `PositionalShadowAtlasQuadrantSubdiv positional_shadow_atlas_quad_0` = `2`
- `PositionalShadowAtlasQuadrantSubdiv positional_shadow_atlas_quad_1` = `2`
- `PositionalShadowAtlasQuadrantSubdiv positional_shadow_atlas_quad_2` = `3`

**Methods**
- `World2D find_world_2d() const`
- `World3D find_world_3d() const`
- `AudioListener2D get_audio_listener_2d() const`
- `AudioListener3D get_audio_listener_3d() const`
- `Camera2D get_camera_2d() const`
- `Camera3D get_camera_3d() const`
- `bool get_canvas_cull_mask_bit(layer: int) const`
- `Array[Window] get_embedded_subwindows() const`
- `Transform2D get_final_transform() const`
- `Vector2 get_mouse_position() const`
- `float get_oversampling() const`
- `PositionalShadowAtlasQuadrantSubdiv get_positional_shadow_atlas_quadrant_subdiv(quadrant: int) const`
- `int get_render_info(type: RenderInfoType, info: RenderInfo)`
- `Transform2D get_screen_transform() const`
- `Transform2D get_stretch_transform() const`
- `ViewportTexture get_texture() const`
- `RID get_viewport_rid() const`
- `Rect2 get_visible_rect() const`
- `void gui_cancel_drag()`
- `Variant gui_get_drag_data() const`
- `String gui_get_drag_description() const`
- `Control gui_get_focus_owner() const`
- `Control gui_get_hovered_control() const`
- `bool gui_is_drag_successful() const`
- `bool gui_is_dragging() const`
- `void gui_release_focus()`
- `void gui_set_drag_description(description: String)`
- `bool is_input_handled() const`
- `void notify_mouse_entered()`
- `void notify_mouse_exited()`
- `void push_input(event: InputEvent, in_local_coords: bool = false)`
- `void push_text_input(text: String)`
- `void push_unhandled_input(event: InputEvent, in_local_coords: bool = false)`
- `void set_canvas_cull_mask_bit(layer: int, enable: bool)`
- `void set_input_as_handled()`
- `void set_positional_shadow_atlas_quadrant_subdiv(quadrant: int, subdiv: PositionalShadowAtlasQuadrantSubdiv)`
- `void update_mouse_cursor_state()`
- `void warp_mouse(position: Vector2)`

**GDScript Examples**
```gdscript
func _ready():
    await RenderingServer.frame_post_draw
    $Viewport.get_texture().get_image().save_png("user://Screenshot.png")
```

### VisualShaderNodeBillboard
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

The output port of this node needs to be connected to Model View Matrix port of VisualShaderNodeOutput.

**Properties**
- `BillboardType billboard_type` = `1`
- `bool keep_scale` = `false`

### VisualShaderNodeBooleanConstant
*Inherits: **VisualShaderNodeConstant < VisualShaderNode < Resource < RefCounted < Object***

Has only one output port and no inputs.

**Properties**
- `bool constant` = `false`

### VisualShaderNodeBooleanParameter
*Inherits: **VisualShaderNodeParameter < VisualShaderNode < Resource < RefCounted < Object***

Translated to uniform bool in the shader language.

**Properties**
- `bool default_value` = `false`
- `bool default_value_enabled` = `false`

### VisualShaderNodeClamp
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

Constrains a value to lie between min and max values.

**Properties**
- `OpType op_type` = `0`

### VisualShaderNodeColorConstant
*Inherits: **VisualShaderNodeConstant < VisualShaderNode < Resource < RefCounted < Object***

Has two output ports representing RGB and alpha channels of Color.

**Properties**
- `Color constant` = `Color(1, 1, 1, 1)`

### VisualShaderNodeColorFunc
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

Accept a Color to the input port and transform it according to function.

**Properties**
- `Function function` = `0`

**GDScript Examples**
```gdscript
vec3 c = input;
float max1 = max(c.r, c.g);
float max2 = max(max1, c.b);
float max3 = max(max1, max2);
return vec3(max3, max3, max3);
```
```gdscript
vec3 c = input;
float r = (c.r * 0.393) + (c.g * 0.769) + (c.b * 0.189);
float g = (c.r * 0.349) + (c.g * 0.686) + (c.b * 0.168);
float b = (c.r * 0.272) + (c.g * 0.534) + (c.b * 0.131);
return vec3(r, g, b);
```

### VisualShaderNodeColorOp
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

Applies operator to two color inputs.

**Properties**
- `Operator operator` = `0`

**GDScript Examples**
```gdscript
result = vec3(1.0) - (vec3(1.0) - a) * (vec3(1.0) - b);
```
```gdscript
result = abs(a - b);
```

### VisualShaderNodeColorParameter
*Inherits: **VisualShaderNodeParameter < VisualShaderNode < Resource < RefCounted < Object***

Translated to uniform vec4 in the shader language.

**Properties**
- `Color default_value` = `Color(1, 1, 1, 1)`
- `bool default_value_enabled` = `false`

### VisualShaderNodeComment
*Inherits: **VisualShaderNodeFrame < VisualShaderNodeResizableBase < VisualShaderNode < Resource < RefCounted < Object***

This node was replaced by VisualShaderNodeFrame and only exists to preserve compatibility. In the VisualShader editor it behaves exactly like VisualShaderNodeFrame.

**Properties**
- `String description` = `""`

### VisualShaderNodeCompare
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

Compares a and b of type by function. Returns a boolean scalar. Translates to if instruction in shader code.

**Properties**
- `Condition condition` = `0`
- `Function function` = `0`
- `ComparisonType type` = `0`

### VisualShaderNodeConstant
*Inherits: **VisualShaderNode < Resource < RefCounted < Object** | Inherited by: VisualShaderNodeBooleanConstant, VisualShaderNodeColorConstant, VisualShaderNodeFloatConstant, VisualShaderNodeIntConstant, VisualShaderNodeTransformConstant, VisualShaderNodeUIntConstant, ...*

This is an abstract class. See the derived types for descriptions of the possible values.

### VisualShaderNodeCubemapParameter
*Inherits: **VisualShaderNodeTextureParameter < VisualShaderNodeParameter < VisualShaderNode < Resource < RefCounted < Object***

Translated to uniform samplerCube in the shader language. The output value can be used as port for VisualShaderNodeCubemap.

### VisualShaderNodeCubemap
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

Translated to texture(cubemap, vec3) in the shader language. Returns a color vector and alpha channel as scalar.

**Properties**
- `TextureLayered cube_map`
- `Source source` = `0`
- `TextureType texture_type` = `0`

### VisualShaderNodeCurveTexture
*Inherits: **VisualShaderNodeResizableBase < VisualShaderNode < Resource < RefCounted < Object***

Comes with a built-in editor for texture's curves.

**Properties**
- `CurveTexture texture`

### VisualShaderNodeCurveXYZTexture
*Inherits: **VisualShaderNodeResizableBase < VisualShaderNode < Resource < RefCounted < Object***

Comes with a built-in editor for texture's curves.

**Properties**
- `CurveXYZTexture texture`

### VisualShaderNodeCustom
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

By inheriting this class you can create a custom VisualShader script addon which will be automatically added to the Visual Shader Editor. The VisualShaderNode's behavior is defined by overriding the provided virtual methods.

**Methods**
- `String _get_category() virtual const`
- `String _get_code(input_vars: Array[String], output_vars: Array[String], mode: Mode, type: Type) virtual const`
- `int _get_default_input_port(type: PortType) virtual const`
- `String _get_description() virtual const`
- `String _get_func_code(mode: Mode, type: Type) virtual const`
- `String _get_global_code(mode: Mode) virtual const`
- `int _get_input_port_count() virtual const`
- `Variant _get_input_port_default_value(port: int) virtual const`
- `String _get_input_port_name(port: int) virtual const`
- `PortType _get_input_port_type(port: int) virtual const`
- `String _get_name() virtual const`
- `int _get_output_port_count() virtual const`
- `String _get_output_port_name(port: int) virtual const`
- `PortType _get_output_port_type(port: int) virtual const`
- `int _get_property_count() virtual const`
- `int _get_property_default_index(index: int) virtual const`
- `String _get_property_name(index: int) virtual const`
- `PackedStringArray _get_property_options(index: int) virtual const`
- `PortType _get_return_icon_type() virtual const`
- `bool _is_available(mode: Mode, type: Type) virtual const`
- `bool _is_highend() virtual const`
- `int get_option_index(option: int) const`

**GDScript Examples**
```gdscript
@tool
extends VisualShaderNodeCustom
class_name VisualShaderNodeNoise
```

### VisualShaderNodeDerivativeFunc
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

This node is only available in Fragment and Light visual shaders.

**Properties**
- `Function function` = `0`
- `OpType op_type` = `0`
- `Precision precision` = `0`

### VisualShaderNodeDeterminant
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

Translates to determinant(x) in the shader language.

### VisualShaderNodeDistanceFade
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

The distance fade effect fades out each pixel based on its distance to another object.

### VisualShaderNodeDotProduct
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

Translates to dot(a, b) in the shader language.

### VisualShaderNodeExpression
*Inherits: **VisualShaderNodeGroupBase < VisualShaderNodeResizableBase < VisualShaderNode < Resource < RefCounted < Object** | Inherited by: VisualShaderNodeGlobalExpression*

Custom Godot Shading Language expression, with a custom number of input and output ports.

**Properties**
- `String expression` = `""`

### VisualShaderNodeFaceForward
*Inherits: **VisualShaderNodeVectorBase < VisualShaderNode < Resource < RefCounted < Object***

Translates to faceforward(N, I, Nref) in the shader language. The function has three vector parameters: N, the vector to orient, I, the incident vector, and Nref, the reference vector. If the dot product of I and Nref is smaller than zero the return value is N. Otherwise, -N is returned.

### VisualShaderNodeFloatConstant
*Inherits: **VisualShaderNodeConstant < VisualShaderNode < Resource < RefCounted < Object***

Translated to float in the shader language.

**Properties**
- `float constant` = `0.0`

### VisualShaderNodeFloatFunc
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

Accept a floating-point scalar (x) to the input port and transform it according to function.

**Properties**
- `Function function` = `13`

### VisualShaderNodeFloatOp
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

Applies operator to two floating-point inputs: a and b.

**Properties**
- `Operator operator` = `0`

### VisualShaderNodeFloatParameter
*Inherits: **VisualShaderNodeParameter < VisualShaderNode < Resource < RefCounted < Object***

Translated to uniform float in the shader language.

**Properties**
- `float default_value` = `0.0`
- `bool default_value_enabled` = `false`
- `Hint hint` = `0`
- `float max` = `1.0`
- `float min` = `0.0`
- `float step` = `0.1`

### VisualShaderNodeFrame
*Inherits: **VisualShaderNodeResizableBase < VisualShaderNode < Resource < RefCounted < Object** | Inherited by: VisualShaderNodeComment*

A rectangular frame that can be used to group visual shader nodes together to improve organization.

**Properties**
- `PackedInt32Array attached_nodes` = `PackedInt32Array()`
- `bool autoshrink` = `true`
- `Color tint_color` = `Color(0.3, 0.3, 0.3, 0.75)`
- `bool tint_color_enabled` = `false`
- `String title` = `"Title"`

**Methods**
- `void add_attached_node(node: int)`
- `void remove_attached_node(node: int)`

### VisualShaderNodeFresnel
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

Returns falloff based on the dot product of surface normal and view direction of camera (pass associated inputs to it).

### VisualShaderNodeGlobalExpression
*Inherits: **VisualShaderNodeExpression < VisualShaderNodeGroupBase < VisualShaderNodeResizableBase < VisualShaderNode < Resource < RefCounted < Object***

Custom Godot Shader Language expression, which is placed on top of the generated shader. You can place various function definitions inside to call later in VisualShaderNodeExpressions (which are injected in the main shader functions). You can also declare varyings, uniforms and global constants.

### VisualShaderNodeGroupBase
*Inherits: **VisualShaderNodeResizableBase < VisualShaderNode < Resource < RefCounted < Object** | Inherited by: VisualShaderNodeExpression*

Currently, has no direct usage, use the derived classes instead.

**Methods**
- `void add_input_port(id: int, type: int, name: String)`
- `void add_output_port(id: int, type: int, name: String)`
- `void clear_input_ports()`
- `void clear_output_ports()`
- `int get_free_input_port_id() const`
- `int get_free_output_port_id() const`
- `int get_input_port_count() const`
- `String get_inputs() const`
- `int get_output_port_count() const`
- `String get_outputs() const`
- `bool has_input_port(id: int) const`
- `bool has_output_port(id: int) const`
- `bool is_valid_port_name(name: String) const`
- `void remove_input_port(id: int)`
- `void remove_output_port(id: int)`
- `void set_input_port_name(id: int, name: String)`
- `void set_input_port_type(id: int, type: int)`
- `void set_inputs(inputs: String)`
- `void set_output_port_name(id: int, name: String)`
- `void set_output_port_type(id: int, type: int)`
- `void set_outputs(outputs: String)`

### VisualShaderNodeIf
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

This visual shader node has six input ports:

### VisualShaderNodeInput
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

Gives access to input variables (built-ins) available for the shader. See the shading reference for the list of available built-ins for each shader type (check Tutorials section for link).

**Properties**
- `String input_name` = `"[None]"`

**Methods**
- `String get_input_real_name() const`

### VisualShaderNodeIntConstant
*Inherits: **VisualShaderNodeConstant < VisualShaderNode < Resource < RefCounted < Object***

Translated to int in the shader language.

**Properties**
- `int constant` = `0`

### VisualShaderNodeIntFunc
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

Accept an integer scalar (x) to the input port and transform it according to function.

**Properties**
- `Function function` = `2`

### VisualShaderNodeIntOp
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

Applies operator to two integer inputs: a and b.

**Properties**
- `Operator operator` = `0`

### VisualShaderNodeIntParameter
*Inherits: **VisualShaderNodeParameter < VisualShaderNode < Resource < RefCounted < Object***

A VisualShaderNodeParameter of type int. Offers additional customization for range of accepted values.

**Properties**
- `int default_value` = `0`
- `bool default_value_enabled` = `false`
- `PackedStringArray enum_names` = `PackedStringArray()`
- `Hint hint` = `0`
- `int max` = `100`
- `int min` = `0`
- `int step` = `1`

### VisualShaderNodeIs
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

Returns the boolean result of the comparison between INF or NaN and a scalar parameter.

**Properties**
- `Function function` = `0`

### VisualShaderNodeLinearSceneDepth
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

This node can be used in fragment shaders.

### VisualShaderNodeMix
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

Translates to mix(a, b, weight) in the shader language.

**Properties**
- `OpType op_type` = `0`

### VisualShaderNodeMultiplyAdd
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

Uses three operands to compute (a * b + c) expression.

**Properties**
- `OpType op_type` = `0`

### VisualShaderNodeOuterProduct
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

OuterProduct treats the first parameter c as a column vector (matrix with one column) and the second parameter r as a row vector (matrix with one row) and does a linear algebraic matrix multiply c * r, yielding a matrix whose number of rows is the number of components in c and whose number of columns is the number of components in r.

### VisualShaderNodeOutput
*Inherits: **VisualShaderNode < Resource < RefCounted < Object** | Inherited by: VisualShaderNodeParticleOutput*

This visual shader node is present in all shader graphs in form of "Output" block with multiple output value ports.

### VisualShaderNodeParameterRef
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

Creating a reference to a VisualShaderNodeParameter allows you to reuse this parameter in different shaders or shader stages easily.

**Properties**
- `String parameter_name` = `"[None]"`

### VisualShaderNodeParameter
*Inherits: **VisualShaderNode < Resource < RefCounted < Object** | Inherited by: VisualShaderNodeBooleanParameter, VisualShaderNodeColorParameter, VisualShaderNodeFloatParameter, VisualShaderNodeIntParameter, VisualShaderNodeTextureParameter, VisualShaderNodeTransformParameter, ...*

A parameter represents a variable in the shader which is set externally, i.e. from the ShaderMaterial. Parameters are exposed as properties in the ShaderMaterial and can be assigned from the Inspector or from a script.

**Properties**
- `int instance_index` = `0`
- `String parameter_name` = `""`
- `Qualifier qualifier` = `0`

### VisualShaderNodeParticleAccelerator
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

Particle accelerator can be used in "process" step of particle shader. It will accelerate the particles. Connect it to the Velocity output port.

**Properties**
- `Mode mode` = `0`

### VisualShaderNodeParticleBoxEmitter
*Inherits: **VisualShaderNodeParticleEmitter < VisualShaderNode < Resource < RefCounted < Object***

VisualShaderNodeParticleEmitter that makes the particles emitted in box shape with the specified extents.

### VisualShaderNodeParticleConeVelocity
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

This node can be used in "start" step of particle shader. It defines the initial velocity of the particles, making them move in cone shape starting from the center, with a given spread.

### VisualShaderNodeParticleEmitter
*Inherits: **VisualShaderNode < Resource < RefCounted < Object** | Inherited by: VisualShaderNodeParticleBoxEmitter, VisualShaderNodeParticleMeshEmitter, VisualShaderNodeParticleRingEmitter, VisualShaderNodeParticleSphereEmitter*

Particle emitter nodes can be used in "start" step of particle shaders and they define the starting position of the particles. Connect them to the Position output port.

**Properties**
- `bool mode_2d` = `false`

### VisualShaderNodeParticleEmit
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

This node internally calls emit_subparticle shader method. It will emit a particle from the configured sub-emitter and also allows to customize how its emitted. Requires a sub-emitter assigned to the particles node with this shader.

**Properties**
- `EmitFlags flags` = `31`

### VisualShaderNodeParticleMeshEmitter
*Inherits: **VisualShaderNodeParticleEmitter < VisualShaderNode < Resource < RefCounted < Object***

VisualShaderNodeParticleEmitter that makes the particles emitted in a shape of the assigned mesh. It will emit from the mesh's surfaces, either all or only the specified one.

**Properties**
- `Mesh mesh`
- `int surface_index` = `0`
- `bool use_all_surfaces` = `true`

### VisualShaderNodeParticleMultiplyByAxisAngle
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

This node helps to multiply a position input vector by rotation using specific axis. Intended to work with emitters.

**Properties**
- `bool degrees_mode` = `true`

### VisualShaderNodeParticleOutput
*Inherits: **VisualShaderNodeOutput < VisualShaderNode < Resource < RefCounted < Object***

This node defines how particles are emitted. It allows to customize e.g. position and velocity. Available ports are different depending on which function this node is inside (start, process, collision) and whether custom data is enabled.

### VisualShaderNodeParticleRandomness
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

Randomness node will output pseudo-random values of the given type based on the specified minimum and maximum values.

**Properties**
- `OpType op_type` = `0`

### VisualShaderNodeParticleRingEmitter
*Inherits: **VisualShaderNodeParticleEmitter < VisualShaderNode < Resource < RefCounted < Object***

VisualShaderNodeParticleEmitter that makes the particles emitted in ring shape with the specified inner and outer radii and height.

### VisualShaderNodeParticleSphereEmitter
*Inherits: **VisualShaderNodeParticleEmitter < VisualShaderNode < Resource < RefCounted < Object***

VisualShaderNodeParticleEmitter that makes the particles emitted in sphere shape with the specified inner and outer radii.

### VisualShaderNodeProximityFade
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

The proximity fade effect fades out each pixel based on its distance to another object.

### VisualShaderNodeRandomRange
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

Random range node will output a pseudo-random scalar value in the specified range, based on the seed. The value is always the same for the given seed and range, so you should provide a changing input, e.g. by using time.

### VisualShaderNodeRemap
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

Remap will transform the input range into output range, e.g. you can change a 0..1 value to -2..2 etc. See @GlobalScope.remap() for more details.

**Properties**
- `OpType op_type` = `0`

### VisualShaderNodeReroute
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

Automatically adapts its port type to the type of the incoming connection and ensures valid connections.

**Methods**
- `PortType get_port_type() const`

### VisualShaderNodeResizableBase
*Inherits: **VisualShaderNode < Resource < RefCounted < Object** | Inherited by: VisualShaderNodeCurveTexture, VisualShaderNodeCurveXYZTexture, VisualShaderNodeFrame, VisualShaderNodeGroupBase*

Resizable nodes have a handle that allows the user to adjust their size as needed.

**Properties**
- `Vector2 size` = `Vector2(0, 0)`

### VisualShaderNodeRotationByAxis
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

RotationByAxis node will transform the vertices of a mesh with specified axis and angle in radians. It can be used to rotate an object in an arbitrary axis.

### VisualShaderNodeSDFRaymarch
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

Casts a ray against the screen SDF (signed-distance field) and returns the distance travelled.

### VisualShaderNodeSDFToScreenUV
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

Translates to sdf_to_screen_uv(sdf_pos) in the shader language.

### VisualShaderNodeSample3D
*Inherits: **VisualShaderNode < Resource < RefCounted < Object** | Inherited by: VisualShaderNodeTexture2DArray, VisualShaderNodeTexture3D*

A virtual class, use the descendants instead.

**Properties**
- `Source source` = `0`

### VisualShaderNodeScreenNormalWorldSpace
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

The ScreenNormalWorldSpace node allows to create outline effects.

### VisualShaderNodeScreenUVToSDF
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

Translates to screen_uv_to_sdf(uv) in the shader language. If the UV port isn't connected, SCREEN_UV is used instead.

### VisualShaderNodeSmoothStep
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

Translates to smoothstep(edge0, edge1, x) in the shader language.

**Properties**
- `OpType op_type` = `0`

### VisualShaderNodeStep
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

Translates to step(edge, x) in the shader language.

**Properties**
- `OpType op_type` = `0`

### VisualShaderNodeSwitch
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

Returns an associated value of the op_type type if the provided boolean value is true or false.

**Properties**
- `OpType op_type` = `0`

### VisualShaderNodeTexture2DArrayParameter
*Inherits: **VisualShaderNodeTextureParameter < VisualShaderNodeParameter < VisualShaderNode < Resource < RefCounted < Object***

This parameter allows to provide a collection of textures for the shader. You can use VisualShaderNodeTexture2DArray to extract the textures from array.

### VisualShaderNodeTexture2DArray
*Inherits: **VisualShaderNodeSample3D < VisualShaderNode < Resource < RefCounted < Object***

Translated to uniform sampler2DArray in the shader language.

**Properties**
- `TextureLayered texture_array`

### VisualShaderNodeTexture2DParameter
*Inherits: **VisualShaderNodeTextureParameter < VisualShaderNodeParameter < VisualShaderNode < Resource < RefCounted < Object***

Translated to uniform sampler2D in the shader language.

### VisualShaderNodeTexture3DParameter
*Inherits: **VisualShaderNodeTextureParameter < VisualShaderNodeParameter < VisualShaderNode < Resource < RefCounted < Object***

Translated to uniform sampler3D in the shader language.

### VisualShaderNodeTexture3D
*Inherits: **VisualShaderNodeSample3D < VisualShaderNode < Resource < RefCounted < Object***

Performs a lookup operation on the provided texture, with support for multiple texture sources to choose from.

**Properties**
- `Texture3D texture`

### VisualShaderNodeTextureParameterTriplanar
*Inherits: **VisualShaderNodeTextureParameter < VisualShaderNodeParameter < VisualShaderNode < Resource < RefCounted < Object***

Performs a lookup operation on the texture provided as a uniform for the shader, with support for triplanar mapping.

### VisualShaderNodeTextureParameter
*Inherits: **VisualShaderNodeParameter < VisualShaderNode < Resource < RefCounted < Object** | Inherited by: VisualShaderNodeCubemapParameter, VisualShaderNodeTexture2DArrayParameter, VisualShaderNodeTexture2DParameter, VisualShaderNodeTexture3DParameter, VisualShaderNodeTextureParameterTriplanar*

Performs a lookup operation on the texture provided as a uniform for the shader.

**Properties**
- `ColorDefault color_default` = `0`
- `TextureFilter texture_filter` = `0`
- `TextureRepeat texture_repeat` = `0`
- `TextureSource texture_source` = `0`
- `TextureType texture_type` = `0`

### VisualShaderNodeTextureSDFNormal
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

Translates to texture_sdf_normal(sdf_pos) in the shader language.

### VisualShaderNodeTextureSDF
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

Translates to texture_sdf(sdf_pos) in the shader language.

### VisualShaderNodeTexture
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

Performs a lookup operation on the provided texture, with support for multiple texture sources to choose from.

**Properties**
- `Source source` = `0`
- `Texture2D texture`
- `TextureType texture_type` = `0`

### VisualShaderNodeTransformCompose
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

Creates a 4×4 transform matrix using four vectors of type vec3. Each vector is one row in the matrix and the last column is a vec4(0, 0, 0, 1).

### VisualShaderNodeTransformConstant
*Inherits: **VisualShaderNodeConstant < VisualShaderNode < Resource < RefCounted < Object***

A constant Transform3D, which can be used as an input node.

**Properties**
- `Transform3D constant` = `Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0)`

### VisualShaderNodeTransformDecompose
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

Takes a 4×4 transform matrix and decomposes it into four vec3 values, one from each row of the matrix.

### VisualShaderNodeTransformFunc
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

Computes an inverse or transpose function on the provided Transform3D.

**Properties**
- `Function function` = `0`

### VisualShaderNodeTransformOp
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

Applies operator to two transform (4×4 matrices) inputs.

**Properties**
- `Operator operator` = `0`

### VisualShaderNodeTransformParameter
*Inherits: **VisualShaderNodeParameter < VisualShaderNode < Resource < RefCounted < Object***

Translated to uniform mat4 in the shader language.

**Properties**
- `Transform3D default_value` = `Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0)`
- `bool default_value_enabled` = `false`

### VisualShaderNodeTransformVecMult
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

A multiplication operation on a transform (4×4 matrix) and a vector, with support for different multiplication operators.

**Properties**
- `Operator operator` = `0`

### VisualShaderNodeUIntConstant
*Inherits: **VisualShaderNodeConstant < VisualShaderNode < Resource < RefCounted < Object***

Translated to uint in the shader language.

**Properties**
- `int constant` = `0`

### VisualShaderNodeUIntFunc
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

Accept an unsigned integer scalar (x) to the input port and transform it according to function.

**Properties**
- `Function function` = `0`

### VisualShaderNodeUIntOp
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

Applies operator to two unsigned integer inputs: a and b.

**Properties**
- `Operator operator` = `0`

### VisualShaderNodeUIntParameter
*Inherits: **VisualShaderNodeParameter < VisualShaderNode < Resource < RefCounted < Object***

A VisualShaderNodeParameter of type unsigned int. Offers additional customization for range of accepted values.

**Properties**
- `int default_value` = `0`
- `bool default_value_enabled` = `false`

### VisualShaderNodeUVFunc
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

UV functions are similar to Vector2 functions, but the input port of this node uses the shader's UV value by default.

**Properties**
- `Function function` = `0`

### VisualShaderNodeUVPolarCoord
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

UV polar coord node will transform UV values into polar coordinates, with specified scale, zoom strength and repeat parameters. It can be used to create various swirl distortions.

### VisualShaderNodeVaryingGetter
*Inherits: **VisualShaderNodeVarying < VisualShaderNode < Resource < RefCounted < Object***

Outputs a value of a varying defined in the shader. You need to first create a varying that can be used in the given function, e.g. varying getter in Fragment shader requires a varying with mode set to VisualShader.VARYING_MODE_VERTEX_TO_FRAG_LIGHT.

### VisualShaderNodeVaryingSetter
*Inherits: **VisualShaderNodeVarying < VisualShaderNode < Resource < RefCounted < Object***

Inputs a value to a varying defined in the shader. You need to first create a varying that can be used in the given function, e.g. varying setter in Fragment shader requires a varying with mode set to VisualShader.VARYING_MODE_FRAG_TO_LIGHT.

### VisualShaderNodeVarying
*Inherits: **VisualShaderNode < Resource < RefCounted < Object** | Inherited by: VisualShaderNodeVaryingGetter, VisualShaderNodeVaryingSetter*

Varying values are shader variables that can be passed between shader functions, e.g. from Vertex shader to Fragment shader.

**Properties**
- `String varying_name` = `"[None]"`
- `VaryingType varying_type` = `0`

### VisualShaderNodeVec2Constant
*Inherits: **VisualShaderNodeConstant < VisualShaderNode < Resource < RefCounted < Object***

A constant Vector2, which can be used as an input node.

**Properties**
- `Vector2 constant` = `Vector2(0, 0)`

### VisualShaderNodeVec2Parameter
*Inherits: **VisualShaderNodeParameter < VisualShaderNode < Resource < RefCounted < Object***

Translated to uniform vec2 in the shader language.

**Properties**
- `Vector2 default_value` = `Vector2(0, 0)`
- `bool default_value_enabled` = `false`

### VisualShaderNodeVec3Constant
*Inherits: **VisualShaderNodeConstant < VisualShaderNode < Resource < RefCounted < Object***

A constant Vector3, which can be used as an input node.

**Properties**
- `Vector3 constant` = `Vector3(0, 0, 0)`

### VisualShaderNodeVec3Parameter
*Inherits: **VisualShaderNodeParameter < VisualShaderNode < Resource < RefCounted < Object***

Translated to uniform vec3 in the shader language.

**Properties**
- `Vector3 default_value` = `Vector3(0, 0, 0)`
- `bool default_value_enabled` = `false`

### VisualShaderNodeVec4Constant
*Inherits: **VisualShaderNodeConstant < VisualShaderNode < Resource < RefCounted < Object***

A constant 4D vector, which can be used as an input node.

**Properties**
- `Quaternion constant` = `Quaternion(0, 0, 0, 1)`

### VisualShaderNodeVec4Parameter
*Inherits: **VisualShaderNodeParameter < VisualShaderNode < Resource < RefCounted < Object***

Translated to uniform vec4 in the shader language.

**Properties**
- `Vector4 default_value` = `Vector4(0, 0, 0, 0)`
- `bool default_value_enabled` = `false`

### VisualShaderNodeVectorBase
*Inherits: **VisualShaderNode < Resource < RefCounted < Object** | Inherited by: VisualShaderNodeFaceForward, VisualShaderNodeVectorCompose, VisualShaderNodeVectorDecompose, VisualShaderNodeVectorDistance, VisualShaderNodeVectorFunc, VisualShaderNodeVectorLen, ...*

This is an abstract class. See the derived types for descriptions of the possible operations.

**Properties**
- `OpType op_type` = `1`

### VisualShaderNodeVectorCompose
*Inherits: **VisualShaderNodeVectorBase < VisualShaderNode < Resource < RefCounted < Object***

Creates a vec2, vec3 or vec4 using scalar values that can be provided from separate inputs.

### VisualShaderNodeVectorDecompose
*Inherits: **VisualShaderNodeVectorBase < VisualShaderNode < Resource < RefCounted < Object***

Takes a vec2, vec3 or vec4 and decomposes it into scalar values that can be used as separate outputs.

### VisualShaderNodeVectorDistance
*Inherits: **VisualShaderNodeVectorBase < VisualShaderNode < Resource < RefCounted < Object***

Calculates distance from point represented by vector p0 to vector p1.

### VisualShaderNodeVectorFunc
*Inherits: **VisualShaderNodeVectorBase < VisualShaderNode < Resource < RefCounted < Object***

A visual shader node able to perform different functions using vectors.

**Properties**
- `Function function` = `0`

### VisualShaderNodeVectorLen
*Inherits: **VisualShaderNodeVectorBase < VisualShaderNode < Resource < RefCounted < Object***

Translated to length(p0) in the shader language.

### VisualShaderNodeVectorOp
*Inherits: **VisualShaderNodeVectorBase < VisualShaderNode < Resource < RefCounted < Object***

A visual shader node for use of vector operators. Operates on vector a and vector b.

**Properties**
- `Operator operator` = `0`

### VisualShaderNodeVectorRefract
*Inherits: **VisualShaderNodeVectorBase < VisualShaderNode < Resource < RefCounted < Object***

Translated to refract(I, N, eta) in the shader language, where I is the incident vector, N is the normal vector and eta is the ratio of the indices of the refraction.

### VisualShaderNodeWorldPositionFromDepth
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

The WorldPositionFromDepth node reconstructs the depth position of the pixel in world space. This can be used to obtain world space UVs for projection mapping like Caustics.

### VisualShaderNode
*Inherits: **Resource < RefCounted < Object** | Inherited by: VisualShaderNodeBillboard, VisualShaderNodeClamp, VisualShaderNodeColorFunc, VisualShaderNodeColorOp, VisualShaderNodeCompare, VisualShaderNodeConstant, ...*

Visual shader graphs consist of various nodes. Each node in the graph is a separate object and they are represented as a rectangular boxes with title and a set of properties. Each node also has connection ports that allow to connect it to another nodes and control the flow of the shader.

**Properties**
- `int linked_parent_graph_frame` = `-1`
- `int output_port_for_preview` = `-1`

**Methods**
- `void clear_default_input_values()`
- `int get_default_input_port(type: PortType) const`
- `Array get_default_input_values() const`
- `Variant get_input_port_default_value(port: int) const`
- `void remove_input_port_default_value(port: int)`
- `void set_default_input_values(values: Array)`
- `void set_input_port_default_value(port: int, value: Variant, prev_value: Variant = null)`

### VisualShader
*Inherits: **Shader < Resource < RefCounted < Object***

This class provides a graph-like visual editor for creating a Shader. Although VisualShaders do not require coding, they share the same logic with script shaders. They use VisualShaderNodes that can be connected to each other to control the flow of the shader. The visual shader graph is converted to a script shader behind the scenes.

**Properties**
- `Vector2 graph_offset`

**Methods**
- `void add_node(type: Type, node: VisualShaderNode, position: Vector2, id: int)`
- `void add_varying(name: String, mode: VaryingMode, type: VaryingType)`
- `void attach_node_to_frame(type: Type, id: int, frame: int)`
- `bool can_connect_nodes(type: Type, from_node: int, from_port: int, to_node: int, to_port: int) const`
- `Error connect_nodes(type: Type, from_node: int, from_port: int, to_node: int, to_port: int)`
- `void connect_nodes_forced(type: Type, from_node: int, from_port: int, to_node: int, to_port: int)`
- `void detach_node_from_frame(type: Type, id: int)`
- `void disconnect_nodes(type: Type, from_node: int, from_port: int, to_node: int, to_port: int)`
- `VisualShaderNode get_node(type: Type, id: int) const`
- `Array[Dictionary] get_node_connections(type: Type) const`
- `PackedInt32Array get_node_list(type: Type) const`
- `Vector2 get_node_position(type: Type, id: int) const`
- `int get_valid_node_id(type: Type) const`
- `bool has_varying(name: String) const`
- `bool is_node_connection(type: Type, from_node: int, from_port: int, to_node: int, to_port: int) const`
- `void remove_node(type: Type, id: int)`
- `void remove_varying(name: String)`
- `void replace_node(type: Type, id: int, new_class: StringName)`
- `void set_mode(mode: Mode)`
- `void set_node_position(type: Type, id: int, position: Vector2)`
