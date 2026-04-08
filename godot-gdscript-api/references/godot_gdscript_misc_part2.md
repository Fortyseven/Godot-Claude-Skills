# Godot 4 GDScript API Reference — Misc (Part 2)

> GDScript-only reference. 163 classes.

### PackedInt32Array

An array specifically designed to hold 32-bit integer values. Packs data tightly, so it saves memory for large array sizes.

**Methods**
- `bool append(value: int)`
- `void append_array(array: PackedInt32Array)`
- `int bsearch(value: int, before: bool = true) const`
- `void clear()`
- `int count(value: int) const`
- `PackedInt32Array duplicate() const`
- `bool erase(value: int)`
- `void fill(value: int)`
- `int find(value: int, from: int = 0) const`
- `int get(index: int) const`
- `bool has(value: int) const`
- `int insert(at_index: int, value: int)`
- `bool is_empty() const`
- `bool push_back(value: int)`
- `void remove_at(index: int)`
- `int resize(new_size: int)`
- `void reverse()`
- `int rfind(value: int, from: int = -1) const`
- `void set(index: int, value: int)`
- `int size() const`
- `PackedInt32Array slice(begin: int, end: int = 2147483647) const`
- `void sort()`
- `PackedByteArray to_byte_array() const`

### PackedInt64Array

An array specifically designed to hold 64-bit integer values. Packs data tightly, so it saves memory for large array sizes.

**Methods**
- `bool append(value: int)`
- `void append_array(array: PackedInt64Array)`
- `int bsearch(value: int, before: bool = true) const`
- `void clear()`
- `int count(value: int) const`
- `PackedInt64Array duplicate() const`
- `bool erase(value: int)`
- `void fill(value: int)`
- `int find(value: int, from: int = 0) const`
- `int get(index: int) const`
- `bool has(value: int) const`
- `int insert(at_index: int, value: int)`
- `bool is_empty() const`
- `bool push_back(value: int)`
- `void remove_at(index: int)`
- `int resize(new_size: int)`
- `void reverse()`
- `int rfind(value: int, from: int = -1) const`
- `void set(index: int, value: int)`
- `int size() const`
- `PackedInt64Array slice(begin: int, end: int = 2147483647) const`
- `void sort()`
- `PackedByteArray to_byte_array() const`

### PackedStringArray

An array specifically designed to hold Strings. Packs data tightly, so it saves memory for large array sizes.

**Methods**
- `bool append(value: String)`
- `void append_array(array: PackedStringArray)`
- `int bsearch(value: String, before: bool = true) const`
- `void clear()`
- `int count(value: String) const`
- `PackedStringArray duplicate() const`
- `bool erase(value: String)`
- `void fill(value: String)`
- `int find(value: String, from: int = 0) const`
- `String get(index: int) const`
- `bool has(value: String) const`
- `int insert(at_index: int, value: String)`
- `bool is_empty() const`
- `bool push_back(value: String)`
- `void remove_at(index: int)`
- `int resize(new_size: int)`
- `void reverse()`
- `int rfind(value: String, from: int = -1) const`
- `void set(index: int, value: String)`
- `int size() const`
- `PackedStringArray slice(begin: int, end: int = 2147483647) const`
- `void sort()`
- `PackedByteArray to_byte_array() const`

**GDScript Examples**
```gdscript
var string_array = PackedStringArray(["hello", "world"])
var string = " ".join(string_array)
print(string) # "hello world"
```

### PackedVector2Array

An array specifically designed to hold Vector2. Packs data tightly, so it saves memory for large array sizes.

**Methods**
- `bool append(value: Vector2)`
- `void append_array(array: PackedVector2Array)`
- `int bsearch(value: Vector2, before: bool = true) const`
- `void clear()`
- `int count(value: Vector2) const`
- `PackedVector2Array duplicate() const`
- `bool erase(value: Vector2)`
- `void fill(value: Vector2)`
- `int find(value: Vector2, from: int = 0) const`
- `Vector2 get(index: int) const`
- `bool has(value: Vector2) const`
- `int insert(at_index: int, value: Vector2)`
- `bool is_empty() const`
- `bool push_back(value: Vector2)`
- `void remove_at(index: int)`
- `int resize(new_size: int)`
- `void reverse()`
- `int rfind(value: Vector2, from: int = -1) const`
- `void set(index: int, value: Vector2)`
- `int size() const`
- `PackedVector2Array slice(begin: int, end: int = 2147483647) const`
- `void sort()`
- `PackedByteArray to_byte_array() const`

**GDScript Examples**
```gdscript
var array = PackedVector2Array([Vector2(12, 34), Vector2(56, 78)])
```

### PackedVector3Array

An array specifically designed to hold Vector3. Packs data tightly, so it saves memory for large array sizes.

**Methods**
- `bool append(value: Vector3)`
- `void append_array(array: PackedVector3Array)`
- `int bsearch(value: Vector3, before: bool = true) const`
- `void clear()`
- `int count(value: Vector3) const`
- `PackedVector3Array duplicate() const`
- `bool erase(value: Vector3)`
- `void fill(value: Vector3)`
- `int find(value: Vector3, from: int = 0) const`
- `Vector3 get(index: int) const`
- `bool has(value: Vector3) const`
- `int insert(at_index: int, value: Vector3)`
- `bool is_empty() const`
- `bool push_back(value: Vector3)`
- `void remove_at(index: int)`
- `int resize(new_size: int)`
- `void reverse()`
- `int rfind(value: Vector3, from: int = -1) const`
- `void set(index: int, value: Vector3)`
- `int size() const`
- `PackedVector3Array slice(begin: int, end: int = 2147483647) const`
- `void sort()`
- `PackedByteArray to_byte_array() const`

**GDScript Examples**
```gdscript
var array = PackedVector3Array([Vector3(12, 34, 56), Vector3(78, 90, 12)])
```

### PackedVector4Array

An array specifically designed to hold Vector4. Packs data tightly, so it saves memory for large array sizes.

**Methods**
- `bool append(value: Vector4)`
- `void append_array(array: PackedVector4Array)`
- `int bsearch(value: Vector4, before: bool = true) const`
- `void clear()`
- `int count(value: Vector4) const`
- `PackedVector4Array duplicate() const`
- `bool erase(value: Vector4)`
- `void fill(value: Vector4)`
- `int find(value: Vector4, from: int = 0) const`
- `Vector4 get(index: int) const`
- `bool has(value: Vector4) const`
- `int insert(at_index: int, value: Vector4)`
- `bool is_empty() const`
- `bool push_back(value: Vector4)`
- `void remove_at(index: int)`
- `int resize(new_size: int)`
- `void reverse()`
- `int rfind(value: Vector4, from: int = -1) const`
- `void set(index: int, value: Vector4)`
- `int size() const`
- `PackedVector4Array slice(begin: int, end: int = 2147483647) const`
- `void sort()`
- `PackedByteArray to_byte_array() const`

**GDScript Examples**
```gdscript
var array = PackedVector4Array([Vector4(12, 34, 56, 78), Vector4(90, 12, 34, 56)])
```

### Panel
*Inherits: **Control < CanvasItem < Node < Object***

Panel is a GUI control that displays a StyleBox. See also PanelContainer.

### PanoramaSkyMaterial
*Inherits: **Material < Resource < RefCounted < Object***

A resource referenced in a Sky that is used to draw a background. PanoramaSkyMaterial functions similar to skyboxes in other engines, except it uses an equirectangular sky map instead of a Cubemap.

**Properties**
- `float energy_multiplier` = `1.0`
- `bool filter` = `true`
- `Texture2D panorama`

### Parallax2D
*Inherits: **Node2D < CanvasItem < Node < Object***

A Parallax2D is used to create a parallax effect. It can move at a different speed relative to the camera movement using scroll_scale. This creates an illusion of depth in a 2D game. If manual scrolling is desired, the Camera2D position can be ignored with ignore_camera_scroll.

**Properties**
- `Vector2 autoscroll` = `Vector2(0, 0)`
- `bool follow_viewport` = `true`
- `bool ignore_camera_scroll` = `false`
- `Vector2 limit_begin` = `Vector2(-10000000, -10000000)`
- `Vector2 limit_end` = `Vector2(10000000, 10000000)`
- `PhysicsInterpolationMode physics_interpolation_mode` = `2 (overrides Node)`
- `Vector2 repeat_size` = `Vector2(0, 0)`
- `int repeat_times` = `1`
- `Vector2 screen_offset` = `Vector2(0, 0)`
- `Vector2 scroll_offset` = `Vector2(0, 0)`
- `Vector2 scroll_scale` = `Vector2(1, 1)`

### ParallaxBackground
*Inherits: **CanvasLayer < Node < Object***

A ParallaxBackground uses one or more ParallaxLayer child nodes to create a parallax effect. Each ParallaxLayer can move at a different speed using ParallaxLayer.motion_offset. This creates an illusion of depth in a 2D game. If not used with a Camera2D, you must manually calculate the scroll_offset.

**Properties**
- `int layer` = `-100 (overrides CanvasLayer)`
- `Vector2 scroll_base_offset` = `Vector2(0, 0)`
- `Vector2 scroll_base_scale` = `Vector2(1, 1)`
- `bool scroll_ignore_camera_zoom` = `false`
- `Vector2 scroll_limit_begin` = `Vector2(0, 0)`
- `Vector2 scroll_limit_end` = `Vector2(0, 0)`
- `Vector2 scroll_offset` = `Vector2(0, 0)`

### ParallaxLayer
*Inherits: **Node2D < CanvasItem < Node < Object***

A ParallaxLayer must be the child of a ParallaxBackground node. Each ParallaxLayer can be set to move at different speeds relative to the camera movement or the ParallaxBackground.scroll_offset value.

**Properties**
- `Vector2 motion_mirroring` = `Vector2(0, 0)`
- `Vector2 motion_offset` = `Vector2(0, 0)`
- `Vector2 motion_scale` = `Vector2(1, 1)`
- `PhysicsInterpolationMode physics_interpolation_mode` = `2 (overrides Node)`

### PhysicalBone2D
*Inherits: **RigidBody2D < PhysicsBody2D < CollisionObject2D < Node2D < CanvasItem < Node < Object***

The PhysicalBone2D node is a RigidBody2D-based node that can be used to make Bone2Ds in a Skeleton2D react to physics.

**Properties**
- `bool auto_configure_joint` = `true`
- `int bone2d_index` = `-1`
- `NodePath bone2d_nodepath` = `NodePath("")`
- `bool follow_bone_when_simulating` = `false`
- `bool simulate_physics` = `false`

**Methods**
- `Joint2D get_joint() const`
- `bool is_simulating_physics() const`

### PhysicalBone3D
*Inherits: **PhysicsBody3D < CollisionObject3D < Node3D < Node < Object***

The PhysicalBone3D node is a physics body that can be used to make bones in a Skeleton3D react to physics.

**Properties**
- `float angular_damp` = `0.0`
- `DampMode angular_damp_mode` = `0`
- `Vector3 angular_velocity` = `Vector3(0, 0, 0)`
- `Transform3D body_offset` = `Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0)`
- `float bounce` = `0.0`
- `bool can_sleep` = `true`
- `bool custom_integrator` = `false`
- `float friction` = `1.0`
- `float gravity_scale` = `1.0`
- `Transform3D joint_offset` = `Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0)`
- `Vector3 joint_rotation` = `Vector3(0, 0, 0)`
- `JointType joint_type` = `0`
- `float linear_damp` = `0.0`
- `DampMode linear_damp_mode` = `0`
- `Vector3 linear_velocity` = `Vector3(0, 0, 0)`
- `float mass` = `1.0`

**Methods**
- `void _integrate_forces(state: PhysicsDirectBodyState3D) virtual`
- `void apply_central_impulse(impulse: Vector3)`
- `void apply_impulse(impulse: Vector3, position: Vector3 = Vector3(0, 0, 0))`
- `int get_bone_id() const`
- `bool get_simulate_physics()`
- `bool is_simulating_physics()`

### PhysicalBoneSimulator3D
*Inherits: **SkeletonModifier3D < Node3D < Node < Object***

Node that can be the parent of PhysicalBone3D and can apply the simulation results to Skeleton3D.

**Methods**
- `bool is_simulating_physics() const`
- `void physical_bones_add_collision_exception(exception: RID)`
- `void physical_bones_remove_collision_exception(exception: RID)`
- `void physical_bones_start_simulation(bones: Array[StringName] = [])`
- `void physical_bones_stop_simulation()`

### PhysicalSkyMaterial
*Inherits: **Material < Resource < RefCounted < Object***

The PhysicalSkyMaterial uses the Preetham analytic daylight model to draw a sky based on physical properties. This results in a substantially more realistic sky than the ProceduralSkyMaterial, but it is slightly slower and less flexible.

**Properties**
- `float energy_multiplier` = `1.0`
- `Color ground_color` = `Color(0.1, 0.07, 0.034, 1)`
- `float mie_coefficient` = `0.005`
- `Color mie_color` = `Color(0.69, 0.729, 0.812, 1)`
- `float mie_eccentricity` = `0.8`
- `Texture2D night_sky`
- `float rayleigh_coefficient` = `2.0`
- `Color rayleigh_color` = `Color(0.3, 0.405, 0.6, 1)`
- `float sun_disk_scale` = `1.0`
- `float turbidity` = `10.0`
- `bool use_debanding` = `true`

### PlaceholderCubemapArray
*Inherits: **PlaceholderTextureLayered < TextureLayered < Texture < Resource < RefCounted < Object***

This class replaces a CubemapArray or a CubemapArray-derived class in 2 conditions:

### PlaceholderCubemap
*Inherits: **PlaceholderTextureLayered < TextureLayered < Texture < Resource < RefCounted < Object***

This class replaces a Cubemap or a Cubemap-derived class in 2 conditions:

### PlaceholderMaterial
*Inherits: **Material < Resource < RefCounted < Object***

This class is used when loading a project that uses a Material subclass in 2 conditions:

### PlaceholderMesh
*Inherits: **Mesh < Resource < RefCounted < Object***

This class is used when loading a project that uses a Mesh subclass in 2 conditions:

**Properties**
- `AABB aabb` = `AABB(0, 0, 0, 0, 0, 0)`

### PlaceholderTexture3D
*Inherits: **Texture3D < Texture < Resource < RefCounted < Object***

This class is used when loading a project that uses a Texture3D subclass in 2 conditions:

**Properties**
- `Vector3i size` = `Vector3i(1, 1, 1)`

### PlaceholderTextureLayered
*Inherits: **TextureLayered < Texture < Resource < RefCounted < Object** | Inherited by: PlaceholderCubemap, PlaceholderCubemapArray, PlaceholderTexture2DArray*

This class is used when loading a project that uses a TextureLayered subclass in 2 conditions:

**Properties**
- `int layers` = `1`
- `Vector2i size` = `Vector2i(1, 1)`

### Plane

Represents a normalized plane equation. normal is the normal of the plane (a, b, c normalized), and d is the distance from the origin to the plane (in the direction of "normal"). "Over" or "Above" the plane is considered the side of the plane towards where the normal is pointing.

**Properties**
- `float d` = `0.0`
- `Vector3 normal` = `Vector3(0, 0, 0)`
- `float x` = `0.0`
- `float y` = `0.0`
- `float z` = `0.0`

**Methods**
- `float distance_to(point: Vector3) const`
- `Vector3 get_center() const`
- `bool has_point(point: Vector3, tolerance: float = 1e-05) const`
- `Variant intersect_3(b: Plane, c: Plane) const`
- `Variant intersects_ray(from: Vector3, dir: Vector3) const`
- `Variant intersects_segment(from: Vector3, to: Vector3) const`
- `bool is_equal_approx(to_plane: Plane) const`
- `bool is_finite() const`
- `bool is_point_over(point: Vector3) const`
- `Plane normalized() const`
- `Vector3 project(point: Vector3) const`

### PointLight2D
*Inherits: **Light2D < Node2D < CanvasItem < Node < Object***

Casts light in a 2D environment. This light's shape is defined by a (usually grayscale) texture.

**Properties**
- `float height` = `0.0`
- `Vector2 offset` = `Vector2(0, 0)`
- `Texture2D texture`
- `float texture_scale` = `1.0`

### PointMesh
*Inherits: **PrimitiveMesh < Mesh < Resource < RefCounted < Object***

A PointMesh is a primitive mesh composed of a single point. Instead of relying on triangles, points are rendered as a single rectangle on the screen with a constant size. They are intended to be used with particle systems, but can also be used as a cheap way to render billboarded sprites (for example in a point cloud).

### PolygonOccluder3D
*Inherits: **Occluder3D < Resource < RefCounted < Object***

PolygonOccluder3D stores a polygon shape that can be used by the engine's occlusion culling system. When an OccluderInstance3D with a PolygonOccluder3D is selected in the editor, an editor will appear at the top of the 3D viewport so you can add/remove points. All points must be placed on the same 2D plane, which means it is not possible to create arbitrary 3D shapes with a single PolygonOccluder3D. To use arbitrary 3D shapes as occluders, use ArrayOccluder3D or OccluderInstance3D's baking feature instead.

**Properties**
- `PackedVector2Array polygon` = `PackedVector2Array()`

### PolygonPathFinder
*Inherits: **Resource < RefCounted < Object***

There is currently no description for this class. Please help us by contributing one!

**Methods**
- `PackedVector2Array find_path(from: Vector2, to: Vector2)`
- `Rect2 get_bounds() const`
- `Vector2 get_closest_point(point: Vector2) const`
- `PackedVector2Array get_intersections(from: Vector2, to: Vector2) const`
- `float get_point_penalty(idx: int) const`
- `bool is_point_inside(point: Vector2) const`
- `void set_point_penalty(idx: int, penalty: float)`
- `void setup(points: PackedVector2Array, connections: PackedInt32Array)`

**GDScript Examples**
```gdscript
var polygon_path_finder = PolygonPathFinder.new()
var points = [Vector2(0.0, 0.0), Vector2(1.0, 0.0), Vector2(0.0, 1.0)]
var connections = [0, 1, 1, 2, 2, 0]
polygon_path_finder.setup(points, connections)
print(polygon_path_finder.is_point_inside(Vector2(0.2, 0.2))) # Prints true
print(polygon_path_finder.is_point_inside(Vector2(1.0, 1.0))) # Prints false
```
```gdscript
var polygon_path_finder = PolygonPathFinder.new()
var points = [Vector2(0.0, 0.0), Vector2(1.0, 0.0), Vector2(0.0, 1.0)]
var connections = [0, 1, 1, 2, 2, 0]
polygon_path_finder.setup(points, connections)
```

### Popup
*Inherits: **Window < Viewport < Node < Object** | Inherited by: PopupMenu, PopupPanel*

Popup is a base class for contextual windows and panels with fixed position. It's a modal by default (see Window.popup_window) and provides methods for implementing custom popup behavior.

**Properties**
- `bool borderless` = `true (overrides Window)`
- `bool maximize_disabled` = `true (overrides Window)`
- `bool minimize_disabled` = `true (overrides Window)`
- `bool popup_window` = `true (overrides Window)`
- `bool popup_wm_hint` = `true (overrides Window)`
- `bool transient` = `true (overrides Window)`
- `bool unresizable` = `true (overrides Window)`
- `bool visible` = `false (overrides Window)`
- `bool wrap_controls` = `true (overrides Window)`

### PrismMesh
*Inherits: **PrimitiveMesh < Mesh < Resource < RefCounted < Object***

Class representing a prism-shaped PrimitiveMesh.

**Properties**
- `float left_to_right` = `0.5`
- `Vector3 size` = `Vector3(1, 1, 1)`
- `int subdivide_depth` = `0`
- `int subdivide_height` = `0`
- `int subdivide_width` = `0`

### ProceduralSkyMaterial
*Inherits: **Material < Resource < RefCounted < Object***

ProceduralSkyMaterial provides a way to create an effective background quickly by defining procedural parameters for the sun, the sky and the ground. The sky and ground are defined by a main color, a color at the horizon, and an easing curve to interpolate between them. Suns are described by a position in the sky, a color, and a max angle from the sun at which the easing curve ends. The max angle therefore defines the size of the sun in the sky.

**Properties**
- `float energy_multiplier` = `1.0`
- `Color ground_bottom_color` = `Color(0.2, 0.169, 0.133, 1)`
- `float ground_curve` = `0.02`
- `float ground_energy_multiplier` = `1.0`
- `Color ground_horizon_color` = `Color(0.6463, 0.6558, 0.6708, 1)`
- `Texture2D sky_cover`
- `Color sky_cover_modulate` = `Color(1, 1, 1, 1)`
- `float sky_curve` = `0.15`
- `float sky_energy_multiplier` = `1.0`
- `Color sky_horizon_color` = `Color(0.6463, 0.6558, 0.6708, 1)`
- `Color sky_top_color` = `Color(0.385, 0.454, 0.55, 1)`
- `float sun_angle_max` = `30.0`
- `float sun_curve` = `0.15`
- `bool use_debanding` = `true`

### QuadOccluder3D
*Inherits: **Occluder3D < Resource < RefCounted < Object***

QuadOccluder3D stores a flat plane shape that can be used by the engine's occlusion culling system. See also PolygonOccluder3D if you need to customize the quad's shape.

**Properties**
- `Vector2 size` = `Vector2(1, 1)`

### RDAttachmentFormat
*Inherits: **RefCounted < Object***

This object is used by RenderingDevice.

**Properties**
- `DataFormat format` = `36`
- `TextureSamples samples` = `0`
- `int usage_flags` = `0`

### RDFramebufferPass
*Inherits: **RefCounted < Object***

This class contains the list of attachment descriptions for a framebuffer pass. Each points with an index to a previously supplied list of texture attachments.

**Properties**
- `PackedInt32Array color_attachments` = `PackedInt32Array()`
- `int depth_attachment` = `-1`
- `PackedInt32Array input_attachments` = `PackedInt32Array()`
- `PackedInt32Array preserve_attachments` = `PackedInt32Array()`
- `PackedInt32Array resolve_attachments` = `PackedInt32Array()`

### RDPipelineColorBlendStateAttachment
*Inherits: **RefCounted < Object***

Controls how blending between source and destination fragments is performed when using RenderingDevice.

**Properties**
- `BlendOperation alpha_blend_op` = `0`
- `BlendOperation color_blend_op` = `0`
- `BlendFactor dst_alpha_blend_factor` = `0`
- `BlendFactor dst_color_blend_factor` = `0`
- `bool enable_blend` = `false`
- `BlendFactor src_alpha_blend_factor` = `0`
- `BlendFactor src_color_blend_factor` = `0`
- `bool write_a` = `true`
- `bool write_b` = `true`
- `bool write_g` = `true`
- `bool write_r` = `true`

**Methods**
- `void set_as_mix()`

**GDScript Examples**
```gdscript
var attachment = RDPipelineColorBlendStateAttachment.new()
attachment.enable_blend = true
attachment.color_blend_op = RenderingDevice.BLEND_OP_ADD
attachment.src_color_blend_factor = RenderingDevice.BLEND_FACTOR_SRC_ALPHA
attachment.dst_color_blend_factor = RenderingDevice.BLEND_FACTOR_ONE_MINUS_SRC_ALPHA
attachment.alpha_blend_op = RenderingDevice.BLEND_OP_ADD
attachment.src_alpha_blend_factor = RenderingDevice.BLEND_FACTOR_ONE
attachment.dst_alpha_blend_factor = RenderingDevice.BLEND_FACTOR_ONE_MINUS_SRC_ALPHA
```
```gdscript
var attachment = RDPipelineColorBlendStateAttachment.new()
attachment.enable_blend = true
attachment.alpha_blend_op = RenderingDevice.BLEND_OP_ADD
attachment.color_blend_op = RenderingDevice.BLEND_OP_ADD
attachment.src_color_blend_factor = RenderingDevice.BLEND_FACTOR_SRC_ALPHA
attachment.dst_color_blend_factor = RenderingDevice.BLEND_FACTOR_ONE
attachment.src_alpha_blend_factor = RenderingDevice.BLEND_FACTOR_SRC_ALPHA
attachment.dst_alpha_blend_factor = RenderingDevice.BLEND_FACTOR_ONE
```

### RDPipelineColorBlendState
*Inherits: **RefCounted < Object***

This object is used by RenderingDevice.

**Properties**
- `Array[RDPipelineColorBlendStateAttachment] attachments` = `[]`
- `Color blend_constant` = `Color(0, 0, 0, 1)`
- `bool enable_logic_op` = `false`
- `LogicOperation logic_op` = `0`

### RDPipelineDepthStencilState
*Inherits: **RefCounted < Object***

RDPipelineDepthStencilState controls the way depth and stencil comparisons are performed when sampling those values using RenderingDevice.

**Properties**
- `CompareOperator back_op_compare` = `7`
- `int back_op_compare_mask` = `0`
- `StencilOperation back_op_depth_fail` = `1`
- `StencilOperation back_op_fail` = `1`
- `StencilOperation back_op_pass` = `1`
- `int back_op_reference` = `0`
- `int back_op_write_mask` = `0`
- `CompareOperator depth_compare_operator` = `7`
- `float depth_range_max` = `0.0`
- `float depth_range_min` = `0.0`
- `bool enable_depth_range` = `false`
- `bool enable_depth_test` = `false`
- `bool enable_depth_write` = `false`
- `bool enable_stencil` = `false`
- `CompareOperator front_op_compare` = `7`
- `int front_op_compare_mask` = `0`
- `StencilOperation front_op_depth_fail` = `1`
- `StencilOperation front_op_fail` = `1`
- `StencilOperation front_op_pass` = `1`
- `int front_op_reference` = `0`
- `int front_op_write_mask` = `0`

### RDPipelineMultisampleState
*Inherits: **RefCounted < Object***

RDPipelineMultisampleState is used to control how multisample or supersample antialiasing is being performed when rendering using RenderingDevice.

**Properties**
- `bool enable_alpha_to_coverage` = `false`
- `bool enable_alpha_to_one` = `false`
- `bool enable_sample_shading` = `false`
- `float min_sample_shading` = `0.0`
- `TextureSamples sample_count` = `0`
- `Array[int] sample_masks` = `[]`

### RDPipelineRasterizationState
*Inherits: **RefCounted < Object***

This object is used by RenderingDevice.

**Properties**
- `PolygonCullMode cull_mode` = `0`
- `float depth_bias_clamp` = `0.0`
- `float depth_bias_constant_factor` = `0.0`
- `bool depth_bias_enabled` = `false`
- `float depth_bias_slope_factor` = `0.0`
- `bool discard_primitives` = `false`
- `bool enable_depth_clamp` = `false`
- `PolygonFrontFace front_face` = `0`
- `float line_width` = `1.0`
- `int patch_control_points` = `1`
- `bool wireframe` = `false`

### RDPipelineSpecializationConstant
*Inherits: **RefCounted < Object***

A specialization constant is a way to create additional variants of shaders without actually increasing the number of shader versions that are compiled. This allows improving performance by reducing the number of shader versions and reducing if branching, while still allowing shaders to be flexible for different use cases.

**Properties**
- `int constant_id` = `0`
- `Variant value`

### RDSamplerState
*Inherits: **RefCounted < Object***

This object is used by RenderingDevice.

**Properties**
- `float anisotropy_max` = `1.0`
- `SamplerBorderColor border_color` = `2`
- `CompareOperator compare_op` = `7`
- `bool enable_compare` = `false`
- `float lod_bias` = `0.0`
- `SamplerFilter mag_filter` = `0`
- `float max_lod` = `1e+20`
- `SamplerFilter min_filter` = `0`
- `float min_lod` = `0.0`
- `SamplerFilter mip_filter` = `0`
- `SamplerRepeatMode repeat_u` = `2`
- `SamplerRepeatMode repeat_v` = `2`
- `SamplerRepeatMode repeat_w` = `2`
- `bool unnormalized_uvw` = `false`
- `bool use_anisotropy` = `false`

### RDShaderSPIRV
*Inherits: **Resource < RefCounted < Object***

RDShaderSPIRV represents an RDShaderFile's SPIR-V code for various shader stages, as well as possible compilation error messages. SPIR-V is a low-level intermediate shader representation. This intermediate representation is not used directly by GPUs for rendering, but it can be compiled into binary shaders that GPUs can understand. Unlike compiled shaders, SPIR-V is portable across GPU models and driver versions.

**Properties**
- `PackedByteArray bytecode_compute` = `PackedByteArray()`
- `PackedByteArray bytecode_fragment` = `PackedByteArray()`
- `PackedByteArray bytecode_tesselation_control` = `PackedByteArray()`
- `PackedByteArray bytecode_tesselation_evaluation` = `PackedByteArray()`
- `PackedByteArray bytecode_vertex` = `PackedByteArray()`
- `String compile_error_compute` = `""`
- `String compile_error_fragment` = `""`
- `String compile_error_tesselation_control` = `""`
- `String compile_error_tesselation_evaluation` = `""`
- `String compile_error_vertex` = `""`

**Methods**
- `PackedByteArray get_stage_bytecode(stage: ShaderStage) const`
- `String get_stage_compile_error(stage: ShaderStage) const`
- `void set_stage_bytecode(stage: ShaderStage, bytecode: PackedByteArray)`
- `void set_stage_compile_error(stage: ShaderStage, compile_error: String)`

### RDShaderSource
*Inherits: **RefCounted < Object***

Shader source code in text form.

**Properties**
- `ShaderLanguage language` = `0`
- `String source_compute` = `""`
- `String source_fragment` = `""`
- `String source_tesselation_control` = `""`
- `String source_tesselation_evaluation` = `""`
- `String source_vertex` = `""`

**Methods**
- `String get_stage_source(stage: ShaderStage) const`
- `void set_stage_source(stage: ShaderStage, source: String)`

### RDTextureFormat
*Inherits: **RefCounted < Object***

This object is used by RenderingDevice.

**Properties**
- `int array_layers` = `1`
- `int depth` = `1`
- `DataFormat format` = `8`
- `int height` = `1`
- `bool is_discardable` = `false`
- `bool is_resolve_buffer` = `false`
- `int mipmaps` = `1`
- `TextureSamples samples` = `0`
- `TextureType texture_type` = `1`
- `BitField[TextureUsageBits] usage_bits` = `0`
- `int width` = `1`

**Methods**
- `void add_shareable_format(format: DataFormat)`
- `void remove_shareable_format(format: DataFormat)`

### RDTextureView
*Inherits: **RefCounted < Object***

This object is used by RenderingDevice.

**Properties**
- `DataFormat format_override` = `232`
- `TextureSwizzle swizzle_a` = `6`
- `TextureSwizzle swizzle_b` = `5`
- `TextureSwizzle swizzle_g` = `4`
- `TextureSwizzle swizzle_r` = `3`

### RDUniform
*Inherits: **RefCounted < Object***

This object is used by RenderingDevice.

**Properties**
- `int binding` = `0`
- `UniformType uniform_type` = `3`

**Methods**
- `void add_id(id: RID)`
- `void clear_ids()`
- `Array[RID] get_ids() const`

### RDVertexAttribute
*Inherits: **RefCounted < Object***

This object is used by RenderingDevice.

**Properties**
- `int binding` = `4294967295`
- `DataFormat format` = `232`
- `VertexFrequency frequency` = `0`
- `int location` = `0`
- `int offset` = `0`
- `int stride` = `0`

### RID

The RID Variant type is used to access a low-level resource by its unique ID. RIDs are opaque, which means they do not grant access to the resource by themselves. They are used by the low-level server classes, such as DisplayServer, RenderingServer, TextServer, etc.

**Methods**
- `int get_id() const`
- `bool is_valid() const`

### RandomNumberGenerator
*Inherits: **RefCounted < Object***

RandomNumberGenerator is a class for generating pseudo-random numbers. It currently uses PCG32.

**Properties**
- `int seed` = `0`
- `int state` = `0`

**Methods**
- `int rand_weighted(weights: PackedFloat32Array)`
- `float randf()`
- `float randf_range(from: float, to: float)`
- `float randfn(mean: float = 0.0, deviation: float = 1.0)`
- `int randi()`
- `int randi_range(from: int, to: int)`
- `void randomize()`

**GDScript Examples**
```gdscript
var rng = RandomNumberGenerator.new()

var my_array = ["one", "two", "three", "four"]
var weights = PackedFloat32Array([0.5, 1, 1, 2])

# Prints one of the four elements in `my_array`.
# It is more likely to print "four", and less likely to print "one".
print(my_array[rng.rand_weighted(weights)])
```
```gdscript
var rng = RandomNumberGenerator.new()
func _ready():
    var my_random_number = rng.randf_range(-10.0, 10.0)
```

### Range
*Inherits: **Control < CanvasItem < Node < Object** | Inherited by: EditorSpinSlider, ProgressBar, ScrollBar, Slider, SpinBox, TextureProgressBar*

Range is an abstract base class for controls that represent a number within a range, using a configured step and page size. See e.g. ScrollBar and Slider for examples of higher-level nodes using Range.

**Properties**
- `bool allow_greater` = `false`
- `bool allow_lesser` = `false`
- `bool exp_edit` = `false`
- `float max_value` = `100.0`
- `float min_value` = `0.0`
- `float page` = `0.0`
- `float ratio`
- `bool rounded` = `false`
- `BitField[SizeFlags] size_flags_vertical` = `0 (overrides Control)`
- `float step` = `0.01`
- `float value` = `0.0`

**Methods**
- `void _value_changed(new_value: float) virtual`
- `void set_value_no_signal(value: float)`
- `void share(with: Node)`
- `void unshare()`

### Rect2

The Rect2 built-in Variant type represents an axis-aligned rectangle in a 2D space. It is defined by its position and size, which are Vector2. It is frequently used for fast overlap tests (see intersects()). Although Rect2 itself is axis-aligned, it can be combined with Transform2D to represent a rotated or skewed rectangle.

**Properties**
- `Vector2 end` = `Vector2(0, 0)`
- `Vector2 position` = `Vector2(0, 0)`
- `Vector2 size` = `Vector2(0, 0)`

**Methods**
- `Rect2 abs() const`
- `bool encloses(b: Rect2) const`
- `Rect2 expand(to: Vector2) const`
- `float get_area() const`
- `Vector2 get_center() const`
- `Vector2 get_support(direction: Vector2) const`
- `Rect2 grow(amount: float) const`
- `Rect2 grow_individual(left: float, top: float, right: float, bottom: float) const`
- `Rect2 grow_side(side: int, amount: float) const`
- `bool has_area() const`
- `bool has_point(point: Vector2) const`
- `Rect2 intersection(b: Rect2) const`
- `bool intersects(b: Rect2, include_borders: bool = false) const`
- `bool is_equal_approx(rect: Rect2) const`
- `bool is_finite() const`
- `Rect2 merge(b: Rect2) const`

**GDScript Examples**
```gdscript
var rect = Rect2(25, 25, -100, -50)
var absolute = rect.abs() # absolute is Rect2(-75, -25, 100, 50)
```
```gdscript
var rect = Rect2(0, 0, 5, 2)

rect = rect.expand(Vector2(10, 0)) # rect is Rect2(0, 0, 10, 2)
rect = rect.expand(Vector2(-5, 5)) # rect is Rect2(-5, 0, 15, 5)
```

### RectangleShape2D
*Inherits: **Shape2D < Resource < RefCounted < Object***

A 2D rectangle shape, intended for use in physics. Usually used to provide a shape for a CollisionShape2D.

**Properties**
- `Vector2 size` = `Vector2(20, 20)`

### ReferenceRect
*Inherits: **Control < CanvasItem < Node < Object***

A rectangular box that displays only a colored border around its rectangle (see Control.get_rect()). It can be used to visualize the extents of a Control node, for testing purposes.

**Properties**
- `Color border_color` = `Color(1, 0, 0, 1)`
- `float border_width` = `1.0`
- `bool editor_only` = `true`

### RegExMatch
*Inherits: **RefCounted < Object***

Contains the results of a single RegEx match returned by RegEx.search() and RegEx.search_all(). It can be used to find the position and range of the match and its capturing groups, and it can extract its substring for you.

**Properties**
- `Dictionary names` = `{}`
- `PackedStringArray strings` = `PackedStringArray()`
- `String subject` = `""`

**Methods**
- `int get_end(name: Variant = 0) const`
- `int get_group_count() const`
- `int get_start(name: Variant = 0) const`
- `String get_string(name: Variant = 0) const`

### RegEx
*Inherits: **RefCounted < Object***

A regular expression (or regex) is a compact language that can be used to recognize strings that follow a specific pattern, such as URLs, email addresses, complete sentences, etc. For example, a regex of ab[0-9] would find any string that is ab followed by any number from 0 to 9. For a more in-depth look, you can easily find various tutorials and detailed explanations on the Internet.

**Methods**
- `void clear()`
- `Error compile(pattern: String, show_error: bool = true)`
- `RegEx create_from_string(pattern: String, show_error: bool = true) static`
- `int get_group_count() const`
- `PackedStringArray get_names() const`
- `String get_pattern() const`
- `bool is_valid() const`
- `RegExMatch search(subject: String, offset: int = 0, end: int = -1) const`
- `Array[RegExMatch] search_all(subject: String, offset: int = 0, end: int = -1) const`
- `String sub(subject: String, replacement: String, all: bool = false, offset: int = 0, end: int = -1) const`

**GDScript Examples**
```gdscript
var regex = RegEx.new()
regex.compile("\\w-(\\d+)")
# Shorthand to create and compile a regex (used in the examples below):
var regex2 = RegEx.create_from_string("\\w-(\\d+)")
```
```gdscript
var regex = RegEx.create_from_string("\\w-(\\d+)")
var result = regex.search("abc n-0123")
if result:
    print(result.get_string()) # Prints "n-0123"
```

### RenderDataExtension
*Inherits: **RenderData < Object***

This class allows for a RenderData implementation to be made in GDExtension.

**Methods**
- `RID _get_camera_attributes() virtual const`
- `RID _get_environment() virtual const`
- `RenderSceneBuffers _get_render_scene_buffers() virtual const`
- `RenderSceneData _get_render_scene_data() virtual const`

### RenderDataRD
*Inherits: **RenderData < Object***

This object manages all render data for the RenderingDevice-based renderers. See also RenderData, RenderSceneData, and RenderSceneDataRD.

### RenderData
*Inherits: **Object** | Inherited by: RenderDataExtension, RenderDataRD*

Abstract render data object, exists for the duration of rendering a single viewport. See also RenderDataRD, RenderSceneData, and RenderSceneDataRD.

**Methods**
- `RID get_camera_attributes() const`
- `RID get_environment() const`
- `RenderSceneBuffers get_render_scene_buffers() const`
- `RenderSceneData get_render_scene_data() const`

### RenderSceneBuffersConfiguration
*Inherits: **RefCounted < Object***

This configuration object is created and populated by the render engine on a viewport change and used to (re)configure a RenderSceneBuffers object.

**Properties**
- `ViewportAnisotropicFiltering anisotropic_filtering_level` = `2`
- `float fsr_sharpness` = `0.0`
- `Vector2i internal_size` = `Vector2i(0, 0)`
- `ViewportMSAA msaa_3d` = `0`
- `RID render_target` = `RID()`
- `ViewportScaling3DMode scaling_3d_mode` = `255`
- `ViewportScreenSpaceAA screen_space_aa` = `0`
- `Vector2i target_size` = `Vector2i(0, 0)`
- `float texture_mipmap_bias` = `0.0`
- `int view_count` = `1`

### RenderSceneBuffersExtension
*Inherits: **RenderSceneBuffers < RefCounted < Object***

This class allows for a RenderSceneBuffer implementation to be made in GDExtension.

**Methods**
- `void _configure(config: RenderSceneBuffersConfiguration) virtual`
- `void _set_anisotropic_filtering_level(anisotropic_filtering_level: int) virtual`
- `void _set_fsr_sharpness(fsr_sharpness: float) virtual`
- `void _set_texture_mipmap_bias(texture_mipmap_bias: float) virtual`
- `void _set_use_debanding(use_debanding: bool) virtual`

### RenderSceneBuffersRD
*Inherits: **RenderSceneBuffers < RefCounted < Object***

This object manages all 3D rendering buffers for the rendering device based renderers. An instance of this object is created for every viewport that has 3D rendering enabled. See also RenderSceneBuffers.

**Methods**
- `void clear_context(context: StringName)`
- `RID create_texture(context: StringName, name: StringName, data_format: DataFormat, usage_bits: int, texture_samples: TextureSamples, size: Vector2i, layers: int, mipmaps: int, unique: bool, discardable: bool)`
- `RID create_texture_from_format(context: StringName, name: StringName, format: RDTextureFormat, view: RDTextureView, unique: bool)`
- `RID create_texture_view(context: StringName, name: StringName, view_name: StringName, view: RDTextureView)`
- `RID get_color_layer(layer: int, msaa: bool = false)`
- `RID get_color_texture(msaa: bool = false)`
- `RID get_depth_layer(layer: int, msaa: bool = false)`
- `RID get_depth_texture(msaa: bool = false)`
- `float get_fsr_sharpness() const`
- `Vector2i get_internal_size() const`
- `ViewportMSAA get_msaa_3d() const`
- `RID get_render_target() const`
- `ViewportScaling3DMode get_scaling_3d_mode() const`
- `ViewportScreenSpaceAA get_screen_space_aa() const`
- `Vector2i get_target_size() const`
- `RID get_texture(context: StringName, name: StringName) const`
- `RDTextureFormat get_texture_format(context: StringName, name: StringName) const`
- `TextureSamples get_texture_samples() const`
- `RID get_texture_slice(context: StringName, name: StringName, layer: int, mipmap: int, layers: int, mipmaps: int)`
- `Vector2i get_texture_slice_size(context: StringName, name: StringName, mipmap: int)`
- `RID get_texture_slice_view(context: StringName, name: StringName, layer: int, mipmap: int, layers: int, mipmaps: int, view: RDTextureView)`
- `bool get_use_debanding() const`
- `bool get_use_taa() const`
- `RID get_velocity_layer(layer: int, msaa: bool = false)`
- `RID get_velocity_texture(msaa: bool = false)`
- `int get_view_count() const`
- `bool has_texture(context: StringName, name: StringName) const`

### RenderSceneBuffers
*Inherits: **RefCounted < Object** | Inherited by: RenderSceneBuffersExtension, RenderSceneBuffersRD*

Abstract scene buffers object, created for each viewport for which 3D rendering is done. It manages any additional buffers used during rendering and will discard buffers when the viewport is resized. See also RenderSceneBuffersRD.

**Methods**
- `void configure(config: RenderSceneBuffersConfiguration)`

### RenderSceneDataExtension
*Inherits: **RenderSceneData < Object***

This class allows for a RenderSceneData implementation to be made in GDExtension.

**Methods**
- `Projection _get_cam_projection() virtual const`
- `Transform3D _get_cam_transform() virtual const`
- `RID _get_uniform_buffer() virtual const`
- `int _get_view_count() virtual const`
- `Vector3 _get_view_eye_offset(view: int) virtual const`
- `Projection _get_view_projection(view: int) virtual const`

### RenderSceneDataRD
*Inherits: **RenderSceneData < Object***

Object holds scene data related to rendering a single frame of a viewport. See also RenderSceneData, RenderData, and RenderDataRD.

### RenderSceneData
*Inherits: **Object** | Inherited by: RenderSceneDataExtension, RenderSceneDataRD*

Abstract scene data object, exists for the duration of rendering a single viewport. See also RenderSceneDataRD, RenderData, and RenderDataRD.

**Methods**
- `Projection get_cam_projection() const`
- `Transform3D get_cam_transform() const`
- `RID get_uniform_buffer() const`
- `int get_view_count() const`
- `Vector3 get_view_eye_offset(view: int) const`
- `Projection get_view_projection(view: int) const`

### RetargetModifier3D
*Inherits: **SkeletonModifier3D < Node3D < Node < Object***

Retrieves the pose (or global pose) relative to the parent Skeleton's rest in model space and transfers it to the child Skeleton.

**Properties**
- `BitField[TransformFlag] enable` = `7`
- `SkeletonProfile profile`
- `bool use_global_pose` = `false`

**Methods**
- `bool is_position_enabled() const`
- `bool is_rotation_enabled() const`
- `bool is_scale_enabled() const`
- `void set_position_enabled(enabled: bool)`
- `void set_rotation_enabled(enabled: bool)`
- `void set_scale_enabled(enabled: bool)`

### RichTextEffect
*Inherits: **Resource < RefCounted < Object***

A custom effect for a RichTextLabel, which can be loaded in the RichTextLabel inspector or using RichTextLabel.install_effect().

**Methods**
- `bool _process_custom_fx(char_fx: CharFXTransform) virtual const`

**GDScript Examples**
```gdscript
# The RichTextEffect will be usable like this: `[example]Some text[/example]`
var bbcode = "example"
```

### RootMotionView
*Inherits: **VisualInstance3D < Node3D < Node < Object***

Root motion refers to an animation technique where a mesh's skeleton is used to give impulse to a character. When working with 3D animations, a popular technique is for animators to use the root skeleton bone to give motion to the rest of the skeleton. This allows animating characters in a way where steps actually match the floor below. It also allows precise interaction with objects during cinematics. See also AnimationMixer.

**Properties**
- `NodePath animation_path` = `NodePath("")`
- `float cell_size` = `1.0`
- `Color color` = `Color(0.5, 0.5, 1, 1)`
- `float radius` = `10.0`
- `bool zero_y` = `true`

### SceneReplicationConfig
*Inherits: **Resource < RefCounted < Object***

Configuration for properties to synchronize with a MultiplayerSynchronizer.

**Methods**
- `void add_property(path: NodePath, index: int = -1)`
- `Array[NodePath] get_properties() const`
- `bool has_property(path: NodePath) const`
- `int property_get_index(path: NodePath) const`
- `ReplicationMode property_get_replication_mode(path: NodePath)`
- `bool property_get_spawn(path: NodePath)`
- `bool property_get_sync(path: NodePath)`
- `bool property_get_watch(path: NodePath)`
- `void property_set_replication_mode(path: NodePath, mode: ReplicationMode)`
- `void property_set_spawn(path: NodePath, enabled: bool)`
- `void property_set_sync(path: NodePath, enabled: bool)`
- `void property_set_watch(path: NodePath, enabled: bool)`
- `void remove_property(path: NodePath)`

### SegmentShape2D
*Inherits: **Shape2D < Resource < RefCounted < Object***

A 2D line segment shape, intended for use in physics. Usually used to provide a shape for a CollisionShape2D.

**Properties**
- `Vector2 a` = `Vector2(0, 0)`
- `Vector2 b` = `Vector2(0, 10)`

### SeparationRayShape2D
*Inherits: **Shape2D < Resource < RefCounted < Object***

A 2D ray shape, intended for use in physics. Usually used to provide a shape for a CollisionShape2D. When a SeparationRayShape2D collides with an object, it tries to separate itself from it by moving its endpoint to the collision point. For example, a SeparationRayShape2D next to a character can allow it to instantly move up when touching stairs.

**Properties**
- `float length` = `20.0`
- `bool slide_on_slope` = `false`

### SeparationRayShape3D
*Inherits: **Shape3D < Resource < RefCounted < Object***

A 3D ray shape, intended for use in physics. Usually used to provide a shape for a CollisionShape3D. When a SeparationRayShape3D collides with an object, it tries to separate itself from it by moving its endpoint to the collision point. For example, a SeparationRayShape3D next to a character can allow it to instantly move up when touching stairs.

**Properties**
- `float length` = `1.0`
- `bool slide_on_slope` = `false`

### Separator
*Inherits: **Control < CanvasItem < Node < Object** | Inherited by: HSeparator, VSeparator*

Abstract base class for separators, used for separating other controls. Separators are purely visual and normally drawn as a StyleBoxLine.

### ShapeCast2D
*Inherits: **Node2D < CanvasItem < Node < Object***

Shape casting allows to detect collision objects by sweeping its shape along the cast direction determined by target_position. This is similar to RayCast2D, but it allows for sweeping a region of space, rather than just a straight line. ShapeCast2D can detect multiple collision objects. It is useful for things like wide laser beams or snapping a simple shape to a floor.

**Properties**
- `bool collide_with_areas` = `false`
- `bool collide_with_bodies` = `true`
- `int collision_mask` = `1`
- `Array collision_result` = `[]`
- `bool enabled` = `true`
- `bool exclude_parent` = `true`
- `float margin` = `0.0`
- `int max_results` = `32`
- `Shape2D shape`
- `Vector2 target_position` = `Vector2(0, 50)`

**Methods**
- `void add_exception(node: CollisionObject2D)`
- `void add_exception_rid(rid: RID)`
- `void clear_exceptions()`
- `void force_shapecast_update()`
- `float get_closest_collision_safe_fraction() const`
- `float get_closest_collision_unsafe_fraction() const`
- `Object get_collider(index: int) const`
- `RID get_collider_rid(index: int) const`
- `int get_collider_shape(index: int) const`
- `int get_collision_count() const`
- `bool get_collision_mask_value(layer_number: int) const`
- `Vector2 get_collision_normal(index: int) const`
- `Vector2 get_collision_point(index: int) const`
- `bool is_colliding() const`
- `void remove_exception(node: CollisionObject2D)`
- `void remove_exception_rid(rid: RID)`
- `void set_collision_mask_value(layer_number: int, value: bool)`

### Shortcut
*Inherits: **Resource < RefCounted < Object***

Shortcuts (also known as hotkeys) are containers of InputEvent resources. They are commonly used to interact with a Control element from an InputEvent.

**Properties**
- `Array events` = `[]`

**Methods**
- `String get_as_text() const`
- `bool has_valid_event() const`
- `bool matches_event(event: InputEvent) const`

**GDScript Examples**
```gdscript
extends Node

var save_shortcut = Shortcut.new()
func _ready():
    var key_event = InputEventKey.new()
    key_event.keycode = KEY_S
    key_event.ctrl_pressed = true
    key_event.command_or_control_autoremap = true # Swaps Ctrl for Command on Mac.
    save_shortcut.events = [key_event]

func _input(event):
    if save_shortcut.matches_event(event) and event.is_pressed() and not event.is_echo():
        print("Save shortcut pressed!")
        get_viewport().set_input_as_handled()
```

### Signal

Signal is a built-in Variant type that represents a signal of an Object instance. Like all Variant types, it can be stored in variables and passed to functions. Signals allow all connected Callables (and by extension their respective objects) to listen and react to events, without directly referencing one another. This keeps the code flexible and easier to manage. You can check whether an Object has a given signal name using Object.has_signal().

**Methods**
- `int connect(callable: Callable, flags: int = 0)`
- `void disconnect(callable: Callable)`
- `void emit(...) vararg const`
- `Array get_connections() const`
- `StringName get_name() const`
- `Object get_object() const`
- `int get_object_id() const`
- `bool has_connections() const`
- `bool is_connected(callable: Callable) const`
- `bool is_null() const`

**GDScript Examples**
```gdscript
signal attacked

# Additional arguments may be declared.
# These arguments must be passed when the signal is emitted.
signal item_dropped(item_name, amount)
```
```gdscript
func _ready():
    var button = Button.new()
    # `button_down` here is a Signal Variant type. We therefore call the Signal.connect() method, not Object.connect().
    # See discussion below for a more in-depth overview of the API.
    button.button_down.connect(_on_button_down)

    # This assumes that a `Player` class exists, which defines a `hit` signal.
    var player = Player.new()
    # We use Signal.connect() again, and we also use the Callable.bind() method,
    # which returns a new Callable with the parameter binds.
    player.hit.connect(_on_player_hit.bind("sword", 100))

func _on
# ...
```

### SkeletonProfileHumanoid
*Inherits: **SkeletonProfile < Resource < RefCounted < Object***

A SkeletonProfile as a preset that is optimized for the human form. This exists for standardization, so all parameters are read-only.

**Properties**
- `int bone_size` = `56 (overrides SkeletonProfile)`
- `int group_size` = `4 (overrides SkeletonProfile)`
- `StringName root_bone` = `&"Root" (overrides SkeletonProfile)`
- `StringName scale_base_bone` = `&"Hips" (overrides SkeletonProfile)`

### SkeletonProfile
*Inherits: **Resource < RefCounted < Object** | Inherited by: SkeletonProfileHumanoid*

This resource is used in EditorScenePostImport. Some parameters are referring to bones in Skeleton3D, Skin, Animation, and some other nodes are rewritten based on the parameters of SkeletonProfile.

**Properties**
- `int bone_size` = `0`
- `int group_size` = `0`
- `StringName root_bone` = `&""`
- `StringName scale_base_bone` = `&""`

**Methods**
- `int find_bone(bone_name: StringName) const`
- `StringName get_bone_name(bone_idx: int) const`
- `StringName get_bone_parent(bone_idx: int) const`
- `StringName get_bone_tail(bone_idx: int) const`
- `StringName get_group(bone_idx: int) const`
- `StringName get_group_name(group_idx: int) const`
- `Vector2 get_handle_offset(bone_idx: int) const`
- `Transform3D get_reference_pose(bone_idx: int) const`
- `TailDirection get_tail_direction(bone_idx: int) const`
- `Texture2D get_texture(group_idx: int) const`
- `bool is_required(bone_idx: int) const`
- `void set_bone_name(bone_idx: int, bone_name: StringName)`
- `void set_bone_parent(bone_idx: int, bone_parent: StringName)`
- `void set_bone_tail(bone_idx: int, bone_tail: StringName)`
- `void set_group(bone_idx: int, group: StringName)`
- `void set_group_name(group_idx: int, group_name: StringName)`
- `void set_handle_offset(bone_idx: int, handle_offset: Vector2)`
- `void set_reference_pose(bone_idx: int, bone_name: Transform3D)`
- `void set_required(bone_idx: int, required: bool)`
- `void set_tail_direction(bone_idx: int, tail_direction: TailDirection)`
- `void set_texture(group_idx: int, texture: Texture2D)`

### SkinReference
*Inherits: **RefCounted < Object***

An internal object containing a mapping from a Skin used within the context of a particular MeshInstance3D to refer to the skeleton's RID in the RenderingServer.

**Methods**
- `RID get_skeleton() const`
- `Skin get_skin() const`

### Skin
*Inherits: **Resource < RefCounted < Object***

There is currently no description for this class. Please help us by contributing one!

**Methods**
- `void add_bind(bone: int, pose: Transform3D)`
- `void add_named_bind(name: String, pose: Transform3D)`
- `void clear_binds()`
- `int get_bind_bone(bind_index: int) const`
- `int get_bind_count() const`
- `StringName get_bind_name(bind_index: int) const`
- `Transform3D get_bind_pose(bind_index: int) const`
- `void set_bind_bone(bind_index: int, bone: int)`
- `void set_bind_count(bind_count: int)`
- `void set_bind_name(bind_index: int, name: StringName)`
- `void set_bind_pose(bind_index: int, pose: Transform3D)`

### Sky
*Inherits: **Resource < RefCounted < Object***

The Sky class uses a Material to render a 3D environment's background and the light it emits by updating the reflection/radiance cubemaps.

**Properties**
- `ProcessMode process_mode` = `0`
- `RadianceSize radiance_size` = `3`
- `Material sky_material`

### SocketServer
*Inherits: **RefCounted < Object** | Inherited by: TCPServer, UDSServer*

A socket server.

**Methods**
- `bool is_connection_available() const`
- `bool is_listening() const`
- `void stop()`
- `StreamPeerSocket take_socket_connection()`

### SphereOccluder3D
*Inherits: **Occluder3D < Resource < RefCounted < Object***

SphereOccluder3D stores a sphere shape that can be used by the engine's occlusion culling system.

**Properties**
- `float radius` = `1.0`

### SphereShape3D
*Inherits: **Shape3D < Resource < RefCounted < Object***

A 3D sphere shape, intended for use in physics. Usually used to provide a shape for a CollisionShape3D.

**Properties**
- `float radius` = `0.5`

### SplineIK3D
*Inherits: **ChainIK3D < IKModifier3D < SkeletonModifier3D < Node3D < Node < Object***

A SkeletonModifier3D for aligning bones along a Path3D. The smoothness of the fitting depends on the Curve3D.bake_interval.

**Properties**
- `int setting_count` = `0`

**Methods**
- `NodePath get_path_3d(index: int) const`
- `int get_tilt_fade_in(index: int) const`
- `int get_tilt_fade_out(index: int) const`
- `bool is_tilt_enabled(index: int) const`
- `void set_path_3d(index: int, path_3d: NodePath)`
- `void set_tilt_enabled(index: int, enabled: bool)`
- `void set_tilt_fade_in(index: int, size: int)`
- `void set_tilt_fade_out(index: int, size: int)`

### SpringBoneCollision3D
*Inherits: **Node3D < Node < Object** | Inherited by: SpringBoneCollisionCapsule3D, SpringBoneCollisionPlane3D, SpringBoneCollisionSphere3D*

A collision can be a child of SpringBoneSimulator3D. If it is not a child of SpringBoneSimulator3D, it has no effect.

**Properties**
- `int bone` = `-1`
- `String bone_name` = `""`
- `Vector3 position_offset`
- `Quaternion rotation_offset`

**Methods**
- `Skeleton3D get_skeleton() const`

### SpringBoneCollisionCapsule3D
*Inherits: **SpringBoneCollision3D < Node3D < Node < Object***

A capsule shape collision that interacts with SpringBoneSimulator3D.

**Properties**
- `float height` = `0.5`
- `bool inside` = `false`
- `float mid_height`
- `float radius` = `0.1`

### SpringBoneCollisionPlane3D
*Inherits: **SpringBoneCollision3D < Node3D < Node < Object***

An infinite plane collision that interacts with SpringBoneSimulator3D. It is an infinite size XZ plane, and the +Y direction is treated as normal.

### SpringBoneCollisionSphere3D
*Inherits: **SpringBoneCollision3D < Node3D < Node < Object***

A sphere shape collision that interacts with SpringBoneSimulator3D.

**Properties**
- `bool inside` = `false`
- `float radius` = `0.1`

### SpringBoneSimulator3D
*Inherits: **SkeletonModifier3D < Node3D < Node < Object***

This SkeletonModifier3D can be used to wiggle hair, cloth, and tails. This modifier behaves differently from PhysicalBoneSimulator3D as it attempts to return the original pose after modification.

**Properties**
- `Vector3 external_force` = `Vector3(0, 0, 0)`
- `bool mutable_bone_axes` = `true`
- `int setting_count` = `0`

**Methods**
- `bool are_all_child_collisions_enabled(index: int) const`
- `void clear_collisions(index: int)`
- `void clear_exclude_collisions(index: int)`
- `void clear_settings()`
- `int get_center_bone(index: int) const`
- `String get_center_bone_name(index: int) const`
- `CenterFrom get_center_from(index: int) const`
- `NodePath get_center_node(index: int) const`
- `int get_collision_count(index: int) const`
- `NodePath get_collision_path(index: int, collision: int) const`
- `float get_drag(index: int) const`
- `Curve get_drag_damping_curve(index: int) const`
- `int get_end_bone(index: int) const`
- `BoneDirection get_end_bone_direction(index: int) const`
- `float get_end_bone_length(index: int) const`
- `String get_end_bone_name(index: int) const`
- `int get_exclude_collision_count(index: int) const`
- `NodePath get_exclude_collision_path(index: int, collision: int) const`
- `float get_gravity(index: int) const`
- `Curve get_gravity_damping_curve(index: int) const`
- `Vector3 get_gravity_direction(index: int) const`
- `int get_joint_bone(index: int, joint: int) const`
- `String get_joint_bone_name(index: int, joint: int) const`
- `int get_joint_count(index: int) const`
- `float get_joint_drag(index: int, joint: int) const`
- `float get_joint_gravity(index: int, joint: int) const`
- `Vector3 get_joint_gravity_direction(index: int, joint: int) const`
- `float get_joint_radius(index: int, joint: int) const`
- `RotationAxis get_joint_rotation_axis(index: int, joint: int) const`
- `Vector3 get_joint_rotation_axis_vector(index: int, joint: int) const`
- `float get_joint_stiffness(index: int, joint: int) const`
- `float get_radius(index: int) const`
- `Curve get_radius_damping_curve(index: int) const`
- `int get_root_bone(index: int) const`
- `String get_root_bone_name(index: int) const`
- `RotationAxis get_rotation_axis(index: int) const`
- `Vector3 get_rotation_axis_vector(index: int) const`
- `float get_stiffness(index: int) const`
- `Curve get_stiffness_damping_curve(index: int) const`
- `bool is_config_individual(index: int) const`

### Sprite3D
*Inherits: **SpriteBase3D < GeometryInstance3D < VisualInstance3D < Node3D < Node < Object***

A node that displays a 2D texture in a 3D environment. The texture displayed can be a region from a larger atlas texture, or a frame from a sprite sheet animation. See also SpriteBase3D where properties such as the billboard mode are defined.

**Properties**
- `int frame` = `0`
- `Vector2i frame_coords` = `Vector2i(0, 0)`
- `int hframes` = `1`
- `bool region_enabled` = `false`
- `Rect2 region_rect` = `Rect2(0, 0, 0, 0)`
- `Texture2D texture`
- `int vframes` = `1`

### SpriteBase3D
*Inherits: **GeometryInstance3D < VisualInstance3D < Node3D < Node < Object** | Inherited by: AnimatedSprite3D, Sprite3D*

A node that displays 2D texture information in a 3D environment. See also Sprite3D where many other properties are defined.

**Properties**
- `float alpha_antialiasing_edge` = `0.0`
- `AlphaAntiAliasing alpha_antialiasing_mode` = `0`
- `AlphaCutMode alpha_cut` = `0`
- `float alpha_hash_scale` = `1.0`
- `float alpha_scissor_threshold` = `0.5`
- `Axis axis` = `2`
- `BillboardMode billboard` = `0`
- `bool centered` = `true`
- `bool double_sided` = `true`
- `bool fixed_size` = `false`
- `bool flip_h` = `false`
- `bool flip_v` = `false`
- `Color modulate` = `Color(1, 1, 1, 1)`
- `bool no_depth_test` = `false`
- `Vector2 offset` = `Vector2(0, 0)`
- `float pixel_size` = `0.01`
- `int render_priority` = `0`
- `bool shaded` = `false`
- `TextureFilter texture_filter` = `3`
- `bool transparent` = `true`

**Methods**
- `TriangleMesh generate_triangle_mesh() const`
- `bool get_draw_flag(flag: DrawFlags) const`
- `Rect2 get_item_rect() const`
- `void set_draw_flag(flag: DrawFlags, enabled: bool)`

### SpriteFrames
*Inherits: **Resource < RefCounted < Object***

Sprite frame library for an AnimatedSprite2D or AnimatedSprite3D node. Contains frames and animation data for playback.

**Methods**
- `void add_animation(anim: StringName)`
- `void add_frame(anim: StringName, texture: Texture2D, duration: float = 1.0, at_position: int = -1)`
- `void clear(anim: StringName)`
- `void clear_all()`
- `void duplicate_animation(anim_from: StringName, anim_to: StringName)`
- `bool get_animation_loop(anim: StringName) const`
- `PackedStringArray get_animation_names() const`
- `float get_animation_speed(anim: StringName) const`
- `int get_frame_count(anim: StringName) const`
- `float get_frame_duration(anim: StringName, idx: int) const`
- `Texture2D get_frame_texture(anim: StringName, idx: int) const`
- `bool has_animation(anim: StringName) const`
- `void remove_animation(anim: StringName)`
- `void remove_frame(anim: StringName, idx: int)`
- `void rename_animation(anim: StringName, newname: StringName)`
- `void set_animation_loop(anim: StringName, loop: bool)`
- `void set_animation_speed(anim: StringName, fps: float)`
- `void set_frame(anim: StringName, idx: int, texture: Texture2D, duration: float = 1.0)`

**GDScript Examples**
```gdscript
absolute_duration = relative_duration / (animation_fps * abs(playing_speed))
```

### StatusIndicator
*Inherits: **Node < Object***

Application status indicator (aka notification area icon).

**Properties**
- `Texture2D icon`
- `NodePath menu` = `NodePath("")`
- `String tooltip` = `""`
- `bool visible` = `true`

**Methods**
- `Rect2 get_rect() const`

### StringName

StringNames are immutable strings designed for general-purpose representation of unique names (also called "string interning"). Two StringNames with the same value are the same object. Comparing them is extremely fast compared to regular Strings.

**Methods**
- `bool begins_with(text: String) const`
- `PackedStringArray bigrams() const`
- `int bin_to_int() const`
- `String c_escape() const`
- `String c_unescape() const`
- `String capitalize() const`
- `int casecmp_to(to: String) const`
- `bool contains(what: String) const`
- `bool containsn(what: String) const`
- `int count(what: String, from: int = 0, to: int = 0) const`
- `int countn(what: String, from: int = 0, to: int = 0) const`
- `String dedent() const`
- `bool ends_with(text: String) const`
- `String erase(position: int, chars: int = 1) const`
- `int filecasecmp_to(to: String) const`
- `int filenocasecmp_to(to: String) const`
- `int find(what: String, from: int = 0) const`
- `int findn(what: String, from: int = 0) const`
- `String format(values: Variant, placeholder: String = "{_}") const`
- `String get_base_dir() const`
- `String get_basename() const`
- `String get_extension() const`
- `String get_file() const`
- `String get_slice(delimiter: String, slice: int) const`
- `int get_slice_count(delimiter: String) const`
- `String get_slicec(delimiter: int, slice: int) const`
- `int hash() const`
- `PackedByteArray hex_decode() const`
- `int hex_to_int() const`
- `String indent(prefix: String) const`
- `String insert(position: int, what: String) const`
- `bool is_absolute_path() const`
- `bool is_empty() const`
- `bool is_relative_path() const`
- `bool is_subsequence_of(text: String) const`
- `bool is_subsequence_ofn(text: String) const`
- `bool is_valid_ascii_identifier() const`
- `bool is_valid_filename() const`
- `bool is_valid_float() const`
- `bool is_valid_hex_number(with_prefix: bool = false) const`

**GDScript Examples**
```gdscript
print("101".bin_to_int())   # Prints 5
print("0b101".bin_to_int()) # Prints 5
print("-0b10".bin_to_int()) # Prints -2
```
```gdscript
"move_local_x".capitalize()   # Returns "Move Local X"
"sceneFile_path".capitalize() # Returns "Scene File Path"
"2D, FPS, PNG".capitalize()   # Returns "2d, Fps, Png"
```

### String

This is the built-in string Variant type (and the one used by GDScript). Strings may contain any number of Unicode characters, and expose methods useful for manipulating and generating strings. Strings are reference-counted and use a copy-on-write approach (every modification to a string returns a new String), so passing them around is cheap in resources.

**Methods**
- `bool begins_with(text: String) const`
- `PackedStringArray bigrams() const`
- `int bin_to_int() const`
- `String c_escape() const`
- `String c_unescape() const`
- `String capitalize() const`
- `int casecmp_to(to: String) const`
- `String chr(code: int) static`
- `bool contains(what: String) const`
- `bool containsn(what: String) const`
- `int count(what: String, from: int = 0, to: int = 0) const`
- `int countn(what: String, from: int = 0, to: int = 0) const`
- `String dedent() const`
- `bool ends_with(text: String) const`
- `String erase(position: int, chars: int = 1) const`
- `int filecasecmp_to(to: String) const`
- `int filenocasecmp_to(to: String) const`
- `int find(what: String, from: int = 0) const`
- `int findn(what: String, from: int = 0) const`
- `String format(values: Variant, placeholder: String = "{_}") const`
- `String get_base_dir() const`
- `String get_basename() const`
- `String get_extension() const`
- `String get_file() const`
- `String get_slice(delimiter: String, slice: int) const`
- `int get_slice_count(delimiter: String) const`
- `String get_slicec(delimiter: int, slice: int) const`
- `int hash() const`
- `PackedByteArray hex_decode() const`
- `int hex_to_int() const`
- `String humanize_size(size: int) static`
- `String indent(prefix: String) const`
- `String insert(position: int, what: String) const`
- `bool is_absolute_path() const`
- `bool is_empty() const`
- `bool is_relative_path() const`
- `bool is_subsequence_of(text: String) const`
- `bool is_subsequence_ofn(text: String) const`
- `bool is_valid_ascii_identifier() const`
- `bool is_valid_filename() const`

**GDScript Examples**
```gdscript
print("101".bin_to_int())   # Prints 5
print("0b101".bin_to_int()) # Prints 5
print("-0b10".bin_to_int()) # Prints -2
```
```gdscript
"move_local_x".capitalize()   # Returns "Move Local X"
"sceneFile_path".capitalize() # Returns "Scene File Path"
"2D, FPS, PNG".capitalize()   # Returns "2d, Fps, Png"
```

### SubtweenTweener
*Inherits: **Tweener < RefCounted < Object***

SubtweenTweener is used to execute a Tween as one step in a sequence defined by another Tween. See Tween.tween_subtween() for more usage information.

**Methods**
- `SubtweenTweener set_delay(delay: float)`

### SyntaxHighlighter
*Inherits: **Resource < RefCounted < Object** | Inherited by: CodeHighlighter, EditorSyntaxHighlighter*

Base class for syntax highlighters. Provides syntax highlighting data to a TextEdit. The associated TextEdit will call into the SyntaxHighlighter on an as-needed basis.

**Methods**
- `void _clear_highlighting_cache() virtual`
- `Dictionary _get_line_syntax_highlighting(line: int) virtual const`
- `void _update_cache() virtual`
- `void clear_highlighting_cache()`
- `Dictionary get_line_syntax_highlighting(line: int)`
- `TextEdit get_text_edit() const`
- `void update_cache()`

**GDScript Examples**
```gdscript
{
    0: {
        "color": Color(1, 0, 0)
    },
    5: {
        "color": Color(0, 1, 0)
    }
}
```

### TextLine
*Inherits: **RefCounted < Object***

Abstraction over TextServer for handling a single line of text.

**Properties**
- `HorizontalAlignment alignment` = `0`
- `Direction direction` = `0`
- `String ellipsis_char` = `"…"`
- `BitField[JustificationFlag] flags` = `3`
- `Orientation orientation` = `0`
- `bool preserve_control` = `false`
- `bool preserve_invalid` = `true`
- `OverrunBehavior text_overrun_behavior` = `3`
- `float width` = `-1.0`

**Methods**
- `bool add_object(key: Variant, size: Vector2, inline_align: InlineAlignment = 5, length: int = 1, baseline: float = 0.0)`
- `bool add_string(text: String, font: Font, font_size: int, language: String = "", meta: Variant = null)`
- `void clear()`
- `void draw(canvas: RID, pos: Vector2, color: Color = Color(1, 1, 1, 1), oversampling: float = 0.0) const`
- `void draw_outline(canvas: RID, pos: Vector2, outline_size: int = 1, color: Color = Color(1, 1, 1, 1), oversampling: float = 0.0) const`
- `TextLine duplicate() const`
- `Direction get_inferred_direction() const`
- `float get_line_ascent() const`
- `float get_line_descent() const`
- `float get_line_underline_position() const`
- `float get_line_underline_thickness() const`
- `float get_line_width() const`
- `Rect2 get_object_rect(key: Variant) const`
- `Array get_objects() const`
- `RID get_rid() const`
- `Vector2 get_size() const`
- `bool has_object(key: Variant) const`
- `int hit_test(coords: float) const`
- `bool resize_object(key: Variant, size: Vector2, inline_align: InlineAlignment = 5, baseline: float = 0.0)`
- `void set_bidi_override(override: Array)`
- `void tab_align(tab_stops: PackedFloat32Array)`

### TextMesh
*Inherits: **PrimitiveMesh < Mesh < Resource < RefCounted < Object***

Generate a PrimitiveMesh from the text.

**Properties**
- `AutowrapMode autowrap_mode` = `0`
- `float curve_step` = `0.5`
- `float depth` = `0.05`
- `Font font`
- `int font_size` = `16`
- `HorizontalAlignment horizontal_alignment` = `1`
- `BitField[JustificationFlag] justification_flags` = `163`
- `String language` = `""`
- `float line_spacing` = `0.0`
- `Vector2 offset` = `Vector2(0, 0)`
- `float pixel_size` = `0.01`
- `StructuredTextParser structured_text_bidi_override` = `0`
- `Array structured_text_bidi_override_options` = `[]`
- `String text` = `""`
- `Direction text_direction` = `0`
- `bool uppercase` = `false`
- `VerticalAlignment vertical_alignment` = `1`
- `float width` = `500.0`

### TextParagraph
*Inherits: **RefCounted < Object***

Abstraction over TextServer for handling a single paragraph of text.

**Properties**
- `HorizontalAlignment alignment` = `0`
- `BitField[LineBreakFlag] break_flags` = `3`
- `String custom_punctuation` = `""`
- `Direction direction` = `0`
- `String ellipsis_char` = `"…"`
- `BitField[JustificationFlag] justification_flags` = `163`
- `float line_spacing` = `0.0`
- `int max_lines_visible` = `-1`
- `Orientation orientation` = `0`
- `bool preserve_control` = `false`
- `bool preserve_invalid` = `true`
- `OverrunBehavior text_overrun_behavior` = `0`
- `float width` = `-1.0`

**Methods**
- `bool add_object(key: Variant, size: Vector2, inline_align: InlineAlignment = 5, length: int = 1, baseline: float = 0.0)`
- `bool add_string(text: String, font: Font, font_size: int, language: String = "", meta: Variant = null)`
- `void clear()`
- `void clear_dropcap()`
- `void draw(canvas: RID, pos: Vector2, color: Color = Color(1, 1, 1, 1), dc_color: Color = Color(1, 1, 1, 1), oversampling: float = 0.0) const`
- `void draw_dropcap(canvas: RID, pos: Vector2, color: Color = Color(1, 1, 1, 1), oversampling: float = 0.0) const`
- `void draw_dropcap_outline(canvas: RID, pos: Vector2, outline_size: int = 1, color: Color = Color(1, 1, 1, 1), oversampling: float = 0.0) const`
- `void draw_line(canvas: RID, pos: Vector2, line: int, color: Color = Color(1, 1, 1, 1), oversampling: float = 0.0) const`
- `void draw_line_outline(canvas: RID, pos: Vector2, line: int, outline_size: int = 1, color: Color = Color(1, 1, 1, 1), oversampling: float = 0.0) const`
- `void draw_outline(canvas: RID, pos: Vector2, outline_size: int = 1, color: Color = Color(1, 1, 1, 1), dc_color: Color = Color(1, 1, 1, 1), oversampling: float = 0.0) const`
- `TextParagraph duplicate() const`
- `int get_dropcap_lines() const`
- `RID get_dropcap_rid() const`
- `Vector2 get_dropcap_size() const`
- `Direction get_inferred_direction() const`
- `float get_line_ascent(line: int) const`
- `int get_line_count() const`
- `float get_line_descent(line: int) const`
- `Rect2 get_line_object_rect(line: int, key: Variant) const`
- `Array get_line_objects(line: int) const`
- `Vector2i get_line_range(line: int) const`
- `RID get_line_rid(line: int) const`
- `Vector2 get_line_size(line: int) const`
- `float get_line_underline_position(line: int) const`
- `float get_line_underline_thickness(line: int) const`
- `float get_line_width(line: int) const`
- `Vector2 get_non_wrapped_size() const`
- `Vector2i get_range() const`
- `RID get_rid() const`
- `Vector2 get_size() const`
- `bool has_object(key: Variant) const`
- `int hit_test(coords: Vector2) const`
- `bool resize_object(key: Variant, size: Vector2, inline_align: InlineAlignment = 5, baseline: float = 0.0)`
- `void set_bidi_override(override: Array)`
- `bool set_dropcap(text: String, font: Font, font_size: int, dropcap_margins: Rect2 = Rect2(0, 0, 0, 0), language: String = "")`
- `void tab_align(tab_stops: PackedFloat32Array)`

### TextServerAdvanced
*Inherits: **TextServerExtension < TextServer < RefCounted < Object***

An implementation of TextServer that uses HarfBuzz, ICU and SIL Graphite to support BiDi, complex text layouts and contextual OpenType features. This is Godot's default primary TextServer interface.

### TextServerDummy
*Inherits: **TextServerExtension < TextServer < RefCounted < Object***

A dummy TextServer interface that doesn't do anything. Useful for freeing up memory when rendering text is not needed, as text servers are resource-intensive. It can also be used for performance comparisons in complex GUIs to check the impact of text rendering.

**GDScript Examples**
```gdscript
var dummy_text_server = TextServerManager.find_interface("Dummy")
if dummy_text_server != null:
    TextServerManager.set_primary_interface(dummy_text_server)
    # If the other text servers are unneeded, they can be removed:
    for i in TextServerManager.get_interface_count():
        var text_server = TextServerManager.get_interface(i)
        if text_server != dummy_text_server:
            TextServerManager.remove_interface(text_server)
```

### TextServerExtension
*Inherits: **TextServer < RefCounted < Object** | Inherited by: TextServerAdvanced, TextServerDummy, TextServerFallback*

External TextServer implementations should inherit from this class.

**Methods**
- `void _cleanup() virtual`
- `RID _create_font() virtual required`
- `RID _create_font_linked_variation(font_rid: RID) virtual`
- `RID _create_shaped_text(direction: Direction, orientation: Orientation) virtual required`
- `void _draw_hex_code_box(canvas: RID, size: int, pos: Vector2, index: int, color: Color) virtual const`
- `void _font_clear_glyphs(font_rid: RID, size: Vector2i) virtual required`
- `void _font_clear_kerning_map(font_rid: RID, size: int) virtual`
- `void _font_clear_size_cache(font_rid: RID) virtual required`
- `void _font_clear_system_fallback_cache() virtual`
- `void _font_clear_textures(font_rid: RID, size: Vector2i) virtual required`
- `void _font_draw_glyph(font_rid: RID, canvas: RID, size: int, pos: Vector2, index: int, color: Color, oversampling: float) virtual required const`
- `void _font_draw_glyph_outline(font_rid: RID, canvas: RID, size: int, outline_size: int, pos: Vector2, index: int, color: Color, oversampling: float) virtual required const`
- `FontAntialiasing _font_get_antialiasing(font_rid: RID) virtual const`
- `float _font_get_ascent(font_rid: RID, size: int) virtual required const`
- `float _font_get_baseline_offset(font_rid: RID) virtual const`
- `int _font_get_char_from_glyph_index(font_rid: RID, size: int, glyph_index: int) virtual required const`
- `float _font_get_descent(font_rid: RID, size: int) virtual required const`
- `bool _font_get_disable_embedded_bitmaps(font_rid: RID) virtual const`
- `float _font_get_embolden(font_rid: RID) virtual const`
- `int _font_get_face_count(font_rid: RID) virtual const`
- `int _font_get_face_index(font_rid: RID) virtual const`
- `int _font_get_fixed_size(font_rid: RID) virtual required const`
- `FixedSizeScaleMode _font_get_fixed_size_scale_mode(font_rid: RID) virtual required const`
- `bool _font_get_generate_mipmaps(font_rid: RID) virtual const`
- `float _font_get_global_oversampling() virtual const`
- `Vector2 _font_get_glyph_advance(font_rid: RID, size: int, glyph: int) virtual required const`
- `Dictionary _font_get_glyph_contours(font_rid: RID, size: int, index: int) virtual const`
- `int _font_get_glyph_index(font_rid: RID, size: int, char: int, variation_selector: int) virtual required const`
- `PackedInt32Array _font_get_glyph_list(font_rid: RID, size: Vector2i) virtual required const`
- `Vector2 _font_get_glyph_offset(font_rid: RID, size: Vector2i, glyph: int) virtual required const`
- `Vector2 _font_get_glyph_size(font_rid: RID, size: Vector2i, glyph: int) virtual required const`
- `int _font_get_glyph_texture_idx(font_rid: RID, size: Vector2i, glyph: int) virtual required const`
- `RID _font_get_glyph_texture_rid(font_rid: RID, size: Vector2i, glyph: int) virtual required const`
- `Vector2 _font_get_glyph_texture_size(font_rid: RID, size: Vector2i, glyph: int) virtual required const`
- `Rect2 _font_get_glyph_uv_rect(font_rid: RID, size: Vector2i, glyph: int) virtual required const`
- `Hinting _font_get_hinting(font_rid: RID) virtual const`
- `bool _font_get_keep_rounding_remainders(font_rid: RID) virtual const`
- `Vector2 _font_get_kerning(font_rid: RID, size: int, glyph_pair: Vector2i) virtual const`
- `Array[Vector2i] _font_get_kerning_list(font_rid: RID, size: int) virtual const`
- `bool _font_get_language_support_override(font_rid: RID, language: String) virtual`

### TextServerFallback
*Inherits: **TextServerExtension < TextServer < RefCounted < Object***

A fallback implementation of Godot's text server. This fallback is faster than TextServerAdvanced for processing a lot of text, but it does not support BiDi and complex text layout.

### TextServerManager
*Inherits: **Object***

TextServerManager is the API backend for loading, enumerating, and switching TextServers.

**Methods**
- `void add_interface(interface: TextServer)`
- `TextServer find_interface(name: String) const`
- `TextServer get_interface(idx: int) const`
- `int get_interface_count() const`
- `Array[Dictionary] get_interfaces() const`
- `TextServer get_primary_interface() const`
- `void remove_interface(interface: TextServer)`
- `void set_primary_interface(index: TextServer)`

### TextServer
*Inherits: **RefCounted < Object** | Inherited by: TextServerExtension*

TextServer is the API backend for managing fonts and rendering text.

**Methods**
- `RID create_font()`
- `RID create_font_linked_variation(font_rid: RID)`
- `RID create_shaped_text(direction: Direction = 0, orientation: Orientation = 0)`
- `void draw_hex_code_box(canvas: RID, size: int, pos: Vector2, index: int, color: Color) const`
- `void font_clear_glyphs(font_rid: RID, size: Vector2i)`
- `void font_clear_kerning_map(font_rid: RID, size: int)`
- `void font_clear_size_cache(font_rid: RID)`
- `void font_clear_system_fallback_cache()`
- `void font_clear_textures(font_rid: RID, size: Vector2i)`
- `void font_draw_glyph(font_rid: RID, canvas: RID, size: int, pos: Vector2, index: int, color: Color = Color(1, 1, 1, 1), oversampling: float = 0.0) const`
- `void font_draw_glyph_outline(font_rid: RID, canvas: RID, size: int, outline_size: int, pos: Vector2, index: int, color: Color = Color(1, 1, 1, 1), oversampling: float = 0.0) const`
- `FontAntialiasing font_get_antialiasing(font_rid: RID) const`
- `float font_get_ascent(font_rid: RID, size: int) const`
- `float font_get_baseline_offset(font_rid: RID) const`
- `int font_get_char_from_glyph_index(font_rid: RID, size: int, glyph_index: int) const`
- `float font_get_descent(font_rid: RID, size: int) const`
- `bool font_get_disable_embedded_bitmaps(font_rid: RID) const`
- `float font_get_embolden(font_rid: RID) const`
- `int font_get_face_count(font_rid: RID) const`
- `int font_get_face_index(font_rid: RID) const`
- `int font_get_fixed_size(font_rid: RID) const`
- `FixedSizeScaleMode font_get_fixed_size_scale_mode(font_rid: RID) const`
- `bool font_get_generate_mipmaps(font_rid: RID) const`
- `float font_get_global_oversampling() const`
- `Vector2 font_get_glyph_advance(font_rid: RID, size: int, glyph: int) const`
- `Dictionary font_get_glyph_contours(font: RID, size: int, index: int) const`
- `int font_get_glyph_index(font_rid: RID, size: int, char: int, variation_selector: int) const`
- `PackedInt32Array font_get_glyph_list(font_rid: RID, size: Vector2i) const`
- `Vector2 font_get_glyph_offset(font_rid: RID, size: Vector2i, glyph: int) const`
- `Vector2 font_get_glyph_size(font_rid: RID, size: Vector2i, glyph: int) const`
- `int font_get_glyph_texture_idx(font_rid: RID, size: Vector2i, glyph: int) const`
- `RID font_get_glyph_texture_rid(font_rid: RID, size: Vector2i, glyph: int) const`
- `Vector2 font_get_glyph_texture_size(font_rid: RID, size: Vector2i, glyph: int) const`
- `Rect2 font_get_glyph_uv_rect(font_rid: RID, size: Vector2i, glyph: int) const`
- `Hinting font_get_hinting(font_rid: RID) const`
- `bool font_get_keep_rounding_remainders(font_rid: RID) const`
- `Vector2 font_get_kerning(font_rid: RID, size: int, glyph_pair: Vector2i) const`
- `Array[Vector2i] font_get_kerning_list(font_rid: RID, size: int) const`
- `bool font_get_language_support_override(font_rid: RID, language: String)`
- `PackedStringArray font_get_language_support_overrides(font_rid: RID)`

**GDScript Examples**
```gdscript
var ts = TextServerManager.get_primary_interface()
```
```gdscript
var ts = TextServerManager.get_primary_interface()
print(ts.string_get_character_breaks("Test ❤️‍🔥 Test")) # Prints [1, 2, 3, 4, 5, 9, 10, 11, 12, 13, 14]
```

### ThemeDB
*Inherits: **Object***

This singleton provides access to static information about Theme resources used by the engine and by your projects. You can fetch the default engine theme, as well as your project configured theme.

**Properties**
- `float fallback_base_scale` = `1.0`
- `Font fallback_font`
- `int fallback_font_size` = `16`
- `Texture2D fallback_icon`
- `StyleBox fallback_stylebox`

**Methods**
- `Theme get_default_theme()`
- `Theme get_project_theme()`

### Theme
*Inherits: **Resource < RefCounted < Object***

A resource used for styling/skinning Control and Window nodes. While individual controls can be styled using their local theme overrides (see Control.add_theme_color_override()), theme resources allow you to store and apply the same settings across all controls sharing the same type (e.g. style all Buttons the same). One theme resource can be used for the entire project, but you can also set a separate theme resource to a branch of control nodes. A theme resource assigned to a control applies to the control itself, as well as all of its direct and indirect children (as long as a chain of controls is uninterrupted).

**Properties**
- `float default_base_scale` = `0.0`
- `Font default_font`
- `int default_font_size` = `-1`

**Methods**
- `void add_type(theme_type: StringName)`
- `void clear()`
- `void clear_color(name: StringName, theme_type: StringName)`
- `void clear_constant(name: StringName, theme_type: StringName)`
- `void clear_font(name: StringName, theme_type: StringName)`
- `void clear_font_size(name: StringName, theme_type: StringName)`
- `void clear_icon(name: StringName, theme_type: StringName)`
- `void clear_stylebox(name: StringName, theme_type: StringName)`
- `void clear_theme_item(data_type: DataType, name: StringName, theme_type: StringName)`
- `void clear_type_variation(theme_type: StringName)`
- `Color get_color(name: StringName, theme_type: StringName) const`
- `PackedStringArray get_color_list(theme_type: String) const`
- `PackedStringArray get_color_type_list() const`
- `int get_constant(name: StringName, theme_type: StringName) const`
- `PackedStringArray get_constant_list(theme_type: String) const`
- `PackedStringArray get_constant_type_list() const`
- `Font get_font(name: StringName, theme_type: StringName) const`
- `PackedStringArray get_font_list(theme_type: String) const`
- `int get_font_size(name: StringName, theme_type: StringName) const`
- `PackedStringArray get_font_size_list(theme_type: String) const`
- `PackedStringArray get_font_size_type_list() const`
- `PackedStringArray get_font_type_list() const`
- `Texture2D get_icon(name: StringName, theme_type: StringName) const`
- `PackedStringArray get_icon_list(theme_type: String) const`
- `PackedStringArray get_icon_type_list() const`
- `StyleBox get_stylebox(name: StringName, theme_type: StringName) const`
- `PackedStringArray get_stylebox_list(theme_type: String) const`
- `PackedStringArray get_stylebox_type_list() const`
- `Variant get_theme_item(data_type: DataType, name: StringName, theme_type: StringName) const`
- `PackedStringArray get_theme_item_list(data_type: DataType, theme_type: String) const`
- `PackedStringArray get_theme_item_type_list(data_type: DataType) const`
- `PackedStringArray get_type_list() const`
- `StringName get_type_variation_base(theme_type: StringName) const`
- `PackedStringArray get_type_variation_list(base_type: StringName) const`
- `bool has_color(name: StringName, theme_type: StringName) const`
- `bool has_constant(name: StringName, theme_type: StringName) const`
- `bool has_default_base_scale() const`
- `bool has_default_font() const`
- `bool has_default_font_size() const`
- `bool has_font(name: StringName, theme_type: StringName) const`

### Timer
*Inherits: **Node < Object***

The Timer node is a countdown timer and is the simplest way to handle time-based logic in the engine. When a timer reaches the end of its wait_time, it will emit the timeout signal.

**Properties**
- `bool autostart` = `false`
- `bool ignore_time_scale` = `false`
- `bool one_shot` = `false`
- `bool paused`
- `TimerProcessCallback process_callback` = `1`
- `float time_left`
- `float wait_time` = `1.0`

**Methods**
- `bool is_stopped() const`
- `void start(time_sec: float = -1)`
- `void stop()`

**GDScript Examples**
```gdscript
func _on_timer_timeout():
    print("Time to attack!")
```

### Time
*Inherits: **Object***

The Time singleton allows converting time between various formats and also getting time information from the system.

**Methods**
- `Dictionary get_date_dict_from_system(utc: bool = false) const`
- `Dictionary get_date_dict_from_unix_time(unix_time_val: int) const`
- `String get_date_string_from_system(utc: bool = false) const`
- `String get_date_string_from_unix_time(unix_time_val: int) const`
- `Dictionary get_datetime_dict_from_datetime_string(datetime: String, weekday: bool) const`
- `Dictionary get_datetime_dict_from_system(utc: bool = false) const`
- `Dictionary get_datetime_dict_from_unix_time(unix_time_val: int) const`
- `String get_datetime_string_from_datetime_dict(datetime: Dictionary, use_space: bool) const`
- `String get_datetime_string_from_system(utc: bool = false, use_space: bool = false) const`
- `String get_datetime_string_from_unix_time(unix_time_val: int, use_space: bool = false) const`
- `String get_offset_string_from_offset_minutes(offset_minutes: int) const`
- `int get_ticks_msec() const`
- `int get_ticks_usec() const`
- `Dictionary get_time_dict_from_system(utc: bool = false) const`
- `Dictionary get_time_dict_from_unix_time(unix_time_val: int) const`
- `String get_time_string_from_system(utc: bool = false) const`
- `String get_time_string_from_unix_time(unix_time_val: int) const`
- `Dictionary get_time_zone_from_system() const`
- `int get_unix_time_from_datetime_dict(datetime: Dictionary) const`
- `int get_unix_time_from_datetime_string(datetime: String) const`
- `float get_unix_time_from_system() const`

### TorusMesh
*Inherits: **PrimitiveMesh < Mesh < Resource < RefCounted < Object***

Class representing a torus PrimitiveMesh.

**Properties**
- `float inner_radius` = `0.5`
- `float outer_radius` = `1.0`
- `int ring_segments` = `32`
- `int rings` = `64`

### TranslationDomain
*Inherits: **RefCounted < Object***

TranslationDomain is a self-contained collection of Translation resources. Translations can be added to or removed from it.

**Properties**
- `bool enabled` = `true`
- `bool pseudolocalization_accents_enabled` = `true`
- `bool pseudolocalization_double_vowels_enabled` = `false`
- `bool pseudolocalization_enabled` = `false`
- `float pseudolocalization_expansion_ratio` = `0.0`
- `bool pseudolocalization_fake_bidi_enabled` = `false`
- `bool pseudolocalization_override_enabled` = `false`
- `String pseudolocalization_prefix` = `"["`
- `bool pseudolocalization_skip_placeholders_enabled` = `true`
- `String pseudolocalization_suffix` = `"]"`

**Methods**
- `void add_translation(translation: Translation)`
- `void clear()`
- `Array[Translation] find_translations(locale: String, exact: bool) const`
- `String get_locale_override() const`
- `Translation get_translation_object(locale: String) const`
- `Array[Translation] get_translations() const`
- `bool has_translation(translation: Translation) const`
- `bool has_translation_for_locale(locale: String, exact: bool) const`
- `StringName pseudolocalize(message: StringName) const`
- `void remove_translation(translation: Translation)`
- `void set_locale_override(locale: String)`
- `StringName translate(message: StringName, context: StringName = &"") const`
- `StringName translate_plural(message: StringName, message_plural: StringName, n: int, context: StringName = &"") const`

### TranslationServer
*Inherits: **Object***

The translation server is the API backend that manages all language translations.

**Properties**
- `bool pseudolocalization_enabled` = `false`

**Methods**
- `void add_translation(translation: Translation)`
- `void clear()`
- `int compare_locales(locale_a: String, locale_b: String) const`
- `Array[Translation] find_translations(locale: String, exact: bool) const`
- `String format_number(number: String, locale: String) const`
- `PackedStringArray get_all_countries() const`
- `PackedStringArray get_all_languages() const`
- `PackedStringArray get_all_scripts() const`
- `String get_country_name(country: String) const`
- `String get_language_name(language: String) const`
- `PackedStringArray get_loaded_locales() const`
- `String get_locale() const`
- `String get_locale_name(locale: String) const`
- `TranslationDomain get_or_add_domain(domain: StringName)`
- `String get_percent_sign(locale: String) const`
- `String get_plural_rules(locale: String) const`
- `String get_script_name(script: String) const`
- `String get_tool_locale()`
- `Translation get_translation_object(locale: String)`
- `Array[Translation] get_translations() const`
- `bool has_domain(domain: StringName) const`
- `bool has_translation(translation: Translation) const`
- `bool has_translation_for_locale(locale: String, exact: bool) const`
- `String parse_number(number: String, locale: String) const`
- `StringName pseudolocalize(message: StringName) const`
- `void reload_pseudolocalization()`
- `void remove_domain(domain: StringName)`
- `void remove_translation(translation: Translation)`
- `void set_locale(locale: String)`
- `String standardize_locale(locale: String, add_defaults: bool = false) const`
- `StringName translate(message: StringName, context: StringName = &"") const`
- `StringName translate_plural(message: StringName, plural_message: StringName, n: int, context: StringName = &"") const`

### Translation
*Inherits: **Resource < RefCounted < Object** | Inherited by: OptimizedTranslation*

Translation maps a collection of strings to their individual translations, and also provides convenience methods for pluralization.

**Properties**
- `String locale` = `"en"`
- `String plural_rules_override` = `""`

**Methods**
- `StringName _get_message(src_message: StringName, context: StringName) virtual const`
- `StringName _get_plural_message(src_message: StringName, src_plural_message: StringName, n: int, context: StringName) virtual const`
- `void add_message(src_message: StringName, xlated_message: StringName, context: StringName = &"")`
- `void add_plural_message(src_message: StringName, xlated_messages: PackedStringArray, context: StringName = &"")`
- `void erase_message(src_message: StringName, context: StringName = &"")`
- `StringName get_message(src_message: StringName, context: StringName = &"") const`
- `int get_message_count() const`
- `PackedStringArray get_message_list() const`
- `StringName get_plural_message(src_message: StringName, src_plural_message: StringName, n: int, context: StringName = &"") const`
- `PackedStringArray get_translated_message_list() const`

**GDScript Examples**
```gdscript
for key in translation.get_message_list():
    var p = key.find("\u0004")
    if p == -1:
        var untranslated = key
        print("Message %s" % untranslated)
    else:
        var context = key.substr(0, p)
        var untranslated = key.substr(p + 1)
        print("Message %s with context %s" % [untranslated, context])
```

### TreeItem
*Inherits: **Object***

A single item of a Tree control. It can contain other TreeItems as children, which allows it to create a hierarchy. It can also contain text and buttons. TreeItem is not a Node, it is internal to the Tree.

**Properties**
- `bool collapsed`
- `int custom_minimum_height`
- `bool disable_folding`
- `bool visible`

**Methods**
- `void add_button(column: int, button: Texture2D, id: int = -1, disabled: bool = false, tooltip_text: String = "", description: String = "")`
- `void add_child(child: TreeItem)`
- `void call_recursive(method: StringName, ...) vararg`
- `void clear_buttons()`
- `void clear_custom_bg_color(column: int)`
- `void clear_custom_color(column: int)`
- `TreeItem create_child(index: int = -1)`
- `void deselect(column: int)`
- `void erase_button(column: int, button_index: int)`
- `AutoTranslateMode get_auto_translate_mode(column: int) const`
- `AutowrapMode get_autowrap_mode(column: int) const`
- `Texture2D get_button(column: int, button_index: int) const`
- `int get_button_by_id(column: int, id: int) const`
- `Color get_button_color(column: int, id: int) const`
- `int get_button_count(column: int) const`
- `int get_button_id(column: int, button_index: int) const`
- `String get_button_tooltip_text(column: int, button_index: int) const`
- `TreeCellMode get_cell_mode(column: int) const`
- `TreeItem get_child(index: int)`
- `int get_child_count()`
- `Array[TreeItem] get_children()`
- `Color get_custom_bg_color(column: int) const`
- `Color get_custom_color(column: int) const`
- `Callable get_custom_draw_callback(column: int) const`
- `Font get_custom_font(column: int) const`
- `int get_custom_font_size(column: int) const`
- `StyleBox get_custom_stylebox(column: int) const`
- `String get_description(column: int) const`
- `bool get_expand_right(column: int) const`
- `TreeItem get_first_child() const`
- `Texture2D get_icon(column: int) const`
- `int get_icon_max_width(column: int) const`
- `Color get_icon_modulate(column: int) const`
- `Texture2D get_icon_overlay(column: int) const`
- `Rect2 get_icon_region(column: int) const`
- `int get_index()`
- `String get_language(column: int) const`
- `Variant get_metadata(column: int) const`
- `TreeItem get_next() const`
- `TreeItem get_next_in_tree(wrap: bool = false)`

### Tree
*Inherits: **Control < CanvasItem < Node < Object***

A control used to show a set of internal TreeItems in a hierarchical structure. The tree items can be selected, expanded and collapsed. The tree can have multiple columns with custom controls like LineEdits, buttons and popups. It can be useful for structured displays and interactions.

**Properties**
- `bool allow_reselect` = `false`
- `bool allow_rmb_select` = `false`
- `bool allow_search` = `true`
- `bool auto_tooltip` = `true`
- `bool clip_contents` = `true (overrides Control)`
- `bool column_titles_visible` = `false`
- `int columns` = `1`
- `int drop_mode_flags` = `0`
- `bool enable_drag_unfolding` = `true`
- `bool enable_recursive_folding` = `true`
- `FocusMode focus_mode` = `2 (overrides Control)`
- `bool hide_folding` = `false`
- `bool hide_root` = `false`
- `ScrollHintMode scroll_hint_mode` = `0`
- `bool scroll_horizontal_enabled` = `true`
- `bool scroll_vertical_enabled` = `true`
- `SelectMode select_mode` = `0`
- `bool tile_scroll_hint` = `false`

**Methods**
- `void clear()`
- `TreeItem create_item(parent: TreeItem = null, index: int = -1)`
- `void deselect_all()`
- `bool edit_selected(force_edit: bool = false)`
- `void ensure_cursor_is_visible()`
- `int get_button_id_at_position(position: Vector2) const`
- `int get_column_at_position(position: Vector2) const`
- `int get_column_expand_ratio(column: int) const`
- `String get_column_title(column: int) const`
- `HorizontalAlignment get_column_title_alignment(column: int) const`
- `TextDirection get_column_title_direction(column: int) const`
- `String get_column_title_language(column: int) const`
- `String get_column_title_tooltip_text(column: int) const`
- `int get_column_width(column: int) const`
- `Rect2 get_custom_popup_rect() const`
- `int get_drop_section_at_position(position: Vector2) const`
- `TreeItem get_edited() const`
- `int get_edited_column() const`
- `Rect2 get_item_area_rect(item: TreeItem, column: int = -1, button_index: int = -1) const`
- `TreeItem get_item_at_position(position: Vector2) const`
- `TreeItem get_next_selected(from: TreeItem)`
- `int get_pressed_button() const`
- `TreeItem get_root() const`
- `Vector2 get_scroll() const`
- `TreeItem get_selected() const`
- `int get_selected_column() const`
- `bool is_column_clipping_content(column: int) const`
- `bool is_column_expanding(column: int) const`
- `void scroll_to_item(item: TreeItem, center_on_item: bool = false)`
- `void set_column_clip_content(column: int, enable: bool)`
- `void set_column_custom_minimum_width(column: int, min_width: int)`
- `void set_column_expand(column: int, expand: bool)`
- `void set_column_expand_ratio(column: int, ratio: int)`
- `void set_column_title(column: int, title: String)`
- `void set_column_title_alignment(column: int, title_alignment: HorizontalAlignment)`
- `void set_column_title_direction(column: int, direction: TextDirection)`
- `void set_column_title_language(column: int, language: String)`
- `void set_column_title_tooltip_text(column: int, tooltip_text: String)`
- `void set_selected(item: TreeItem, column: int)`

**GDScript Examples**
```gdscript
func _ready():
    var tree = Tree.new()
    var root = tree.create_item()
    tree.hide_root = true
    var child1 = tree.create_item(root)
    var child2 = tree.create_item(root)
    var subchild1 = tree.create_item(child1)
    subchild1.set_text(0, "Subchild1")
```
```gdscript
func _ready():
    $Tree.item_edited.connect(on_Tree_item_edited)

func on_Tree_item_edited():
    print($Tree.get_edited()) # This item just got edited (e.g. checked).
```

### TriangleMesh
*Inherits: **RefCounted < Object***

Creates a bounding volume hierarchy (BVH) tree structure around triangle geometry.

**Methods**
- `bool create_from_faces(faces: PackedVector3Array)`
- `PackedVector3Array get_faces() const`
- `Dictionary intersect_ray(begin: Vector3, dir: Vector3) const`
- `Dictionary intersect_segment(begin: Vector3, end: Vector3) const`

### Tween
*Inherits: **RefCounted < Object***

Tweens are mostly useful for animations requiring a numerical property to be interpolated over a range of values. The name tween comes from in-betweening, an animation technique where you specify keyframes and the computer interpolates the frames that appear between them. Animating something with a Tween is called tweening.

**Methods**
- `Tween bind_node(node: Node)`
- `Tween chain()`
- `bool custom_step(delta: float)`
- `int get_loops_left() const`
- `float get_total_elapsed_time() const`
- `Variant interpolate_value(initial_value: Variant, delta_value: Variant, elapsed_time: float, duration: float, trans_type: TransitionType, ease_type: EaseType) static`
- `bool is_running()`
- `bool is_valid()`
- `void kill()`
- `Tween parallel()`
- `void pause()`
- `void play()`
- `Tween set_ease(ease: EaseType)`
- `Tween set_ignore_time_scale(ignore: bool = true)`
- `Tween set_loops(loops: int = 0)`
- `Tween set_parallel(parallel: bool = true)`
- `Tween set_pause_mode(mode: TweenPauseMode)`
- `Tween set_process_mode(mode: TweenProcessMode)`
- `Tween set_speed_scale(speed: float)`
- `Tween set_trans(trans: TransitionType)`
- `void stop()`
- `CallbackTweener tween_callback(callback: Callable)`
- `IntervalTweener tween_interval(time: float)`
- `MethodTweener tween_method(method: Callable, from: Variant, to: Variant, duration: float)`
- `PropertyTweener tween_property(object: Object, property: NodePath, final_val: Variant, duration: float)`
- `SubtweenTweener tween_subtween(subtween: Tween)`

**GDScript Examples**
```gdscript
var tween = get_tree().create_tween()
tween.tween_property($Sprite, "modulate", Color.RED, 1.0)
tween.tween_property($Sprite, "scale", Vector2(), 1.0)
tween.tween_callback($Sprite.queue_free)
```
```gdscript
var tween = get_tree().create_tween()
tween.tween_property($Sprite, "modulate", Color.RED, 1.0).set_trans(Tween.TRANS_SINE)
tween.tween_property($Sprite, "scale", Vector2(), 1.0).set_trans(Tween.TRANS_BOUNCE)
tween.tween_callback($Sprite.queue_free)
```

### TwoBoneIK3D
*Inherits: **IKModifier3D < SkeletonModifier3D < Node3D < Node < Object***

This IKModifier3D requires a pole target. It provides deterministic results by constructing a plane from each joint and pole target and finding the intersection of two circles (disks in 3D).

**Properties**
- `int setting_count` = `0`

**Methods**
- `int get_end_bone(index: int) const`
- `BoneDirection get_end_bone_direction(index: int) const`
- `float get_end_bone_length(index: int) const`
- `String get_end_bone_name(index: int) const`
- `int get_middle_bone(index: int) const`
- `String get_middle_bone_name(index: int) const`
- `SecondaryDirection get_pole_direction(index: int) const`
- `Vector3 get_pole_direction_vector(index: int) const`
- `NodePath get_pole_node(index: int) const`
- `int get_root_bone(index: int) const`
- `String get_root_bone_name(index: int) const`
- `NodePath get_target_node(index: int) const`
- `bool is_end_bone_extended(index: int) const`
- `bool is_using_virtual_end(index: int) const`
- `void set_end_bone(index: int, bone: int)`
- `void set_end_bone_direction(index: int, bone_direction: BoneDirection)`
- `void set_end_bone_length(index: int, length: float)`
- `void set_end_bone_name(index: int, bone_name: String)`
- `void set_extend_end_bone(index: int, enabled: bool)`
- `void set_middle_bone(index: int, bone: int)`
- `void set_middle_bone_name(index: int, bone_name: String)`
- `void set_pole_direction(index: int, direction: SecondaryDirection)`
- `void set_pole_direction_vector(index: int, vector: Vector3)`
- `void set_pole_node(index: int, pole_node: NodePath)`
- `void set_root_bone(index: int, bone: int)`
- `void set_root_bone_name(index: int, bone_name: String)`
- `void set_target_node(index: int, target_node: NodePath)`
- `void set_use_virtual_end(index: int, enabled: bool)`

### UDSServer
*Inherits: **SocketServer < RefCounted < Object***

A Unix Domain Socket (UDS) server. Listens to connections on a socket path and returns a StreamPeerUDS when it gets an incoming connection. Unix Domain Sockets provide inter-process communication on the same machine using the filesystem namespace.

**Methods**
- `Error listen(path: String)`
- `StreamPeerUDS take_connection()`

### UPNPDevice
*Inherits: **RefCounted < Object***

Universal Plug and Play (UPnP) device. See UPNP for UPnP discovery and utility functions. Provides low-level access to UPNP control commands. Allows to manage port mappings (port forwarding) and to query network information of the device (like local and external IP address and status). Note that methods on this class are synchronous and block the calling thread.

**Properties**
- `String description_url` = `""`
- `String igd_control_url` = `""`
- `String igd_our_addr` = `""`
- `String igd_service_type` = `""`
- `IGDStatus igd_status` = `9`
- `String service_type` = `""`

**Methods**
- `int add_port_mapping(port: int, port_internal: int = 0, desc: String = "", proto: String = "UDP", duration: int = 0) const`
- `int delete_port_mapping(port: int, proto: String = "UDP") const`
- `bool is_valid_gateway() const`
- `String query_external_address() const`

### UPNP
*Inherits: **RefCounted < Object***

This class can be used to discover compatible UPNPDevices on the local network and execute commands on them, like managing port mappings (for port forwarding/NAT traversal) and querying the local and remote network IP address. Note that methods on this class are synchronous and block the calling thread.

**Properties**
- `bool discover_ipv6` = `false`
- `int discover_local_port` = `0`
- `String discover_multicast_if` = `""`

**Methods**
- `void add_device(device: UPNPDevice)`
- `int add_port_mapping(port: int, port_internal: int = 0, desc: String = "", proto: String = "UDP", duration: int = 0) const`
- `void clear_devices()`
- `int delete_port_mapping(port: int, proto: String = "UDP") const`
- `int discover(timeout: int = 2000, ttl: int = 2, device_filter: String = "InternetGatewayDevice")`
- `UPNPDevice get_device(index: int) const`
- `int get_device_count() const`
- `UPNPDevice get_gateway() const`
- `String query_external_address() const`
- `void remove_device(index: int)`
- `void set_device(index: int, device: UPNPDevice)`

**GDScript Examples**
```gdscript
var upnp = UPNP.new()
upnp.discover()
upnp.add_port_mapping(7777)
```
```gdscript
upnp.delete_port_mapping(port)
```

### UndoRedo
*Inherits: **Object***

UndoRedo works by registering methods and property changes inside "actions". You can create an action, then provide ways to do and undo this action using function calls and property changes, then commit the action.

**Properties**
- `int max_steps` = `0`

**Methods**
- `void add_do_method(callable: Callable)`
- `void add_do_property(object: Object, property: StringName, value: Variant)`
- `void add_do_reference(object: Object)`
- `void add_undo_method(callable: Callable)`
- `void add_undo_property(object: Object, property: StringName, value: Variant)`
- `void add_undo_reference(object: Object)`
- `void clear_history(increase_version: bool = true)`
- `void commit_action(execute: bool = true)`
- `void create_action(name: String, merge_mode: MergeMode = 0, backward_undo_ops: bool = false)`
- `void end_force_keep_in_merge_ends()`
- `String get_action_name(id: int)`
- `int get_current_action()`
- `String get_current_action_name() const`
- `int get_history_count()`
- `int get_version() const`
- `bool has_redo() const`
- `bool has_undo() const`
- `bool is_committing_action() const`
- `bool redo()`
- `void start_force_keep_in_merge_ends()`
- `bool undo()`

**GDScript Examples**
```gdscript
var undo_redo = UndoRedo.new()

func do_something():
    pass # Put your code here.

func undo_something():
    pass # Put here the code that reverts what's done by "do_something()".

func _on_my_button_pressed():
    var node = get_node("MyNode2D")
    undo_redo.create_action("Move the node")
    undo_redo.add_do_method(do_something)
    undo_redo.add_undo_method(undo_something)
    undo_redo.add_do_property(node, "position", Vector2(100, 100))
    undo_redo.add_undo_property(node, "position", node.position)
    undo_redo.commit_action()
```
```gdscript
undo_redo.create_action("Add object")

# DO
undo_redo.add_do_method(_create_object)
undo_redo.add_do_method(_add_object_to_singleton)

# UNDO
undo_redo.add_undo_method(_remove_object_from_singleton)
undo_redo.add_undo_method(_destroy_that_object)

undo_redo.commit_action()
```

### UniformSetCacheRD
*Inherits: **Object***

Uniform set cache manager for RenderingDevice-based renderers. Provides a way to create a uniform set and reuse it in subsequent calls for as long as the uniform set exists. Uniform set will automatically be cleaned up when dependent objects are freed.

**Methods**
- `RID get_cache(shader: RID, set: int, uniforms: Array[RDUniform]) static`

### VFlowContainer
*Inherits: **FlowContainer < Container < Control < CanvasItem < Node < Object***

A variant of FlowContainer that can only arrange its child controls vertically, wrapping them around at the borders. This is similar to how text in a book wraps around when no more words can fit on a line, except vertically.

### VSeparator
*Inherits: **Separator < Control < CanvasItem < Node < Object***

A vertical separator used for separating other controls that are arranged horizontally. VSeparator is purely visual and normally drawn as a StyleBoxLine.

### Variant

In computer programming, a Variant class is a class that is designed to store a variety of other types. Dynamic programming languages like PHP, Lua, JavaScript and GDScript like to use them to store variables' data on the backend. With these Variants, properties are able to change value types freely.

**GDScript Examples**
```gdscript
var foo = 2 # foo is dynamically an integer
foo = "Now foo is a string!"
foo = RefCounted.new() # foo is an Object
var bar: int = 2 # bar is a statically typed integer.
# bar = "Uh oh! I can't make statically typed variables become a different type!"
```
```gdscript
var foo = 2
match typeof(foo):
    TYPE_NIL:
        print("foo is null")
    TYPE_INT:
        print("foo is an integer")
    TYPE_OBJECT:
        # Note that Objects are their own special category.
        # To get the name of the underlying Object type, you need the `get_class()` method.
        print("foo is a(n) %s" % foo.get_class()) # inject the class name into a formatted string.
        # Note that this does not get the script's `class_name` global identifier.
        # If the `class_name` is needed, use `foo.get_script().get_global_name()` instead.
```

### VideoStreamPlayback
*Inherits: **Resource < RefCounted < Object***

This class is intended to be overridden by video decoder extensions with custom implementations of VideoStream.

**Methods**
- `int _get_channels() virtual const`
- `float _get_length() virtual const`
- `int _get_mix_rate() virtual const`
- `float _get_playback_position() virtual const`
- `Texture2D _get_texture() virtual const`
- `bool _is_paused() virtual const`
- `bool _is_playing() virtual const`
- `void _play() virtual`
- `void _seek(time: float) virtual`
- `void _set_audio_track(idx: int) virtual`
- `void _set_paused(paused: bool) virtual`
- `void _stop() virtual`
- `void _update(delta: float) virtual required`
- `int mix_audio(num_frames: int, buffer: PackedFloat32Array = PackedFloat32Array(), offset: int = 0)`

### VideoStreamTheora
*Inherits: **VideoStream < Resource < RefCounted < Object***

VideoStream resource handling the Ogg Theora video format with .ogv extension. The Theora codec is decoded on the CPU.

### VideoStream
*Inherits: **Resource < RefCounted < Object** | Inherited by: VideoStreamTheora*

Base resource type for all video streams. Classes that derive from VideoStream can all be used as resource types to play back videos in VideoStreamPlayer.

**Properties**
- `String file` = `""`

**Methods**
- `VideoStreamPlayback _instantiate_playback() virtual required`

### VisibleOnScreenEnabler3D
*Inherits: **VisibleOnScreenNotifier3D < VisualInstance3D < Node3D < Node < Object***

VisibleOnScreenEnabler3D contains a box-shaped region of 3D space and a target node. The target node will be automatically enabled (via its Node.process_mode property) when any part of this region becomes visible on the screen, and automatically disabled otherwise. This can for example be used to activate enemies only when the player approaches them.

**Properties**
- `EnableMode enable_mode` = `0`
- `NodePath enable_node_path` = `NodePath("..")`

### VisibleOnScreenNotifier3D
*Inherits: **VisualInstance3D < Node3D < Node < Object** | Inherited by: VisibleOnScreenEnabler3D*

VisibleOnScreenNotifier3D represents a box-shaped region of 3D space. When any part of this region becomes visible on screen or in a Camera3D's view, it will emit a screen_entered signal, and likewise it will emit a screen_exited signal when no part of it remains visible.

**Properties**
- `AABB aabb` = `AABB(-1, -1, -1, 2, 2, 2)`

**Methods**
- `bool is_on_screen() const`

### WebRTCDataChannelExtension
*Inherits: **WebRTCDataChannel < PacketPeer < RefCounted < Object***

There is currently no description for this class. Please help us by contributing one!

**Methods**
- `void _close() virtual required`
- `int _get_available_packet_count() virtual required const`
- `int _get_buffered_amount() virtual required const`
- `int _get_id() virtual required const`
- `String _get_label() virtual required const`
- `int _get_max_packet_life_time() virtual required const`
- `int _get_max_packet_size() virtual required const`
- `int _get_max_retransmits() virtual required const`
- `Error _get_packet(r_buffer: const uint8_t **, r_buffer_size: int32_t*) virtual`
- `String _get_protocol() virtual required const`
- `ChannelState _get_ready_state() virtual required const`
- `WriteMode _get_write_mode() virtual required const`
- `bool _is_negotiated() virtual required const`
- `bool _is_ordered() virtual required const`
- `Error _poll() virtual required`
- `Error _put_packet(p_buffer: const uint8_t*, p_buffer_size: int) virtual`
- `void _set_write_mode(p_write_mode: WriteMode) virtual required`
- `bool _was_string_packet() virtual required const`

### WebRTCDataChannel
*Inherits: **PacketPeer < RefCounted < Object** | Inherited by: WebRTCDataChannelExtension*

There is currently no description for this class. Please help us by contributing one!

**Properties**
- `WriteMode write_mode` = `1`

**Methods**
- `void close()`
- `int get_buffered_amount() const`
- `int get_id() const`
- `String get_label() const`
- `int get_max_packet_life_time() const`
- `int get_max_retransmits() const`
- `String get_protocol() const`
- `ChannelState get_ready_state() const`
- `bool is_negotiated() const`
- `bool is_ordered() const`
- `Error poll()`
- `bool was_string_packet() const`

### WebRTCMultiplayerPeer
*Inherits: **MultiplayerPeer < PacketPeer < RefCounted < Object***

This class constructs a full mesh of WebRTCPeerConnection (one connection for each peer) that can be used as a MultiplayerAPI.multiplayer_peer.

**Methods**
- `Error add_peer(peer: WebRTCPeerConnection, peer_id: int, unreliable_lifetime: int = 1)`
- `Error create_client(peer_id: int, channels_config: Array = [])`
- `Error create_mesh(peer_id: int, channels_config: Array = [])`
- `Error create_server(channels_config: Array = [])`
- `Dictionary get_peer(peer_id: int)`
- `Dictionary get_peers()`
- `bool has_peer(peer_id: int)`
- `void remove_peer(peer_id: int)`

### WebRTCPeerConnectionExtension
*Inherits: **WebRTCPeerConnection < RefCounted < Object***

There is currently no description for this class. Please help us by contributing one!

**Methods**
- `Error _add_ice_candidate(p_sdp_mid_name: String, p_sdp_mline_index: int, p_sdp_name: String) virtual required`
- `void _close() virtual required`
- `WebRTCDataChannel _create_data_channel(p_label: String, p_config: Dictionary) virtual required`
- `Error _create_offer() virtual required`
- `ConnectionState _get_connection_state() virtual required const`
- `GatheringState _get_gathering_state() virtual required const`
- `SignalingState _get_signaling_state() virtual required const`
- `Error _initialize(p_config: Dictionary) virtual required`
- `Error _poll() virtual required`
- `Error _set_local_description(p_type: String, p_sdp: String) virtual required`
- `Error _set_remote_description(p_type: String, p_sdp: String) virtual required`

### WebRTCPeerConnection
*Inherits: **RefCounted < Object** | Inherited by: WebRTCPeerConnectionExtension*

A WebRTC connection between the local computer and a remote peer. Provides an interface to connect, maintain, and monitor the connection.

**Methods**
- `Error add_ice_candidate(media: String, index: int, name: String)`
- `void close()`
- `WebRTCDataChannel create_data_channel(label: String, options: Dictionary = {})`
- `Error create_offer()`
- `ConnectionState get_connection_state() const`
- `GatheringState get_gathering_state() const`
- `SignalingState get_signaling_state() const`
- `Error initialize(configuration: Dictionary = {})`
- `Error poll()`
- `void set_default_extension(extension_class: StringName) static`
- `Error set_local_description(type: String, sdp: String)`
- `Error set_remote_description(type: String, sdp: String)`

**GDScript Examples**
```gdscript
{
    "negotiated": true, # When set to true (default off), means the channel is negotiated out of band. "id" must be set too. "data_channel_received" will not be called.
    "id": 1, # When "negotiated" is true this value must also be set to the same value on both peer.

    # Only one of maxRetransmits and maxPacketLifeTime can be specified, not both. They make the channel unreliable (but also better at real time).
    "maxRetransmits": 1, # Specify the maximum number of attempt the peer will make to retransmits packets if they are not acknowledged.
    "maxPacketLifeTime": 100, # Specify th
# ...
```
```gdscript
{
    "iceServers": [
        {
            "urls": [ "stun:stun.example.com:3478" ], # One or more STUN servers.
        },
        {
            "urls": [ "turn:turn.example.com:3478" ], # One or more TURN servers.
            "username": "a_username", # Optional username for the TURN server.
            "credential": "a_password", # Optional password for the TURN server.
        }
    ]
}
```

### WebXRInterface
*Inherits: **XRInterface < RefCounted < Object***

WebXR is an open standard that allows creating VR and AR applications that run in the web browser.

**Properties**
- `String enabled_features`
- `String optional_features`
- `String reference_space_type`
- `String requested_reference_space_types`
- `String required_features`
- `String session_mode`
- `String visibility_state`

**Methods**
- `Array get_available_display_refresh_rates() const`
- `float get_display_refresh_rate() const`
- `TargetRayMode get_input_source_target_ray_mode(input_source_id: int) const`
- `XRControllerTracker get_input_source_tracker(input_source_id: int) const`
- `bool is_input_source_active(input_source_id: int) const`
- `void is_session_supported(session_mode: String)`
- `void set_display_refresh_rate(refresh_rate: float)`

**GDScript Examples**
```gdscript
extends Node3D

var webxr_interface
var vr_supported = false

func _ready():
    # We assume this node has a button as a child.
    # This button is for the user to consent to entering immersive VR mode.
    $Button.pressed.connect(self._on_button_pressed)

    webxr_interface = XRServer.find_interface("WebXR")
    if webxr_interface:
        # WebXR uses a lot of asynchronous callbacks, so we connect to various
        # signals in order to receive them.
        webxr_interface.session_supported.connect(self._webxr_session_supported)
        webxr_interface.session_started.connect(self._webxr
# ...
```

### World2D
*Inherits: **Resource < RefCounted < Object***

Class that has everything pertaining to a 2D world: A physics space, a canvas, and a sound space. 2D nodes register their resources into the current 2D world.

**Properties**
- `RID canvas`
- `PhysicsDirectSpaceState2D direct_space_state`
- `RID navigation_map`
- `RID space`

### World3D
*Inherits: **Resource < RefCounted < Object***

Class that has everything pertaining to a world: A physics space, a visual scenario, and a sound space. 3D nodes register their resources into the current 3D world.

**Properties**
- `CameraAttributes camera_attributes`
- `PhysicsDirectSpaceState3D direct_space_state`
- `Environment environment`
- `Environment fallback_environment`
- `RID navigation_map`
- `RID scenario`
- `RID space`

### WorldBoundaryShape2D
*Inherits: **Shape2D < Resource < RefCounted < Object***

A 2D world boundary shape, intended for use in physics. WorldBoundaryShape2D works like an infinite straight line that forces all physics bodies to stay above it. The line's normal determines which direction is considered as "above" and in the editor, the smaller line over it represents this direction. It can for example be used for endless flat floors.

**Properties**
- `float distance` = `0.0`
- `Vector2 normal` = `Vector2(0, -1)`

### WorldBoundaryShape3D
*Inherits: **Shape3D < Resource < RefCounted < Object***

A 3D world boundary shape, intended for use in physics. WorldBoundaryShape3D works like an infinite plane that forces all physics bodies to stay above it. The plane's normal determines which direction is considered as "above" and in the editor, the line over the plane represents this direction. It can for example be used for endless flat floors.

**Properties**
- `Plane plane` = `Plane(0, 1, 0, 0)`

### XRAnchor3D
*Inherits: **XRNode3D < Node3D < Node < Object***

The XRAnchor3D point is an XRNode3D that maps a real world location identified by the AR platform to a position within the game world. For example, as long as plane detection in ARKit is on, ARKit will identify and update the position of planes (tables, floors, etc.) and create anchors for them.

**Methods**
- `Plane get_plane() const`
- `Vector3 get_size() const`

### XRBodyModifier3D
*Inherits: **SkeletonModifier3D < Node3D < Node < Object***

This node uses body tracking data from an XRBodyTracker to pose the skeleton of a body mesh.

**Properties**
- `StringName body_tracker` = `&"/user/body_tracker"`
- `BitField[BodyUpdate] body_update` = `7`
- `BoneUpdate bone_update` = `0`

### XRBodyTracker
*Inherits: **XRPositionalTracker < XRTracker < RefCounted < Object***

A body tracking system will create an instance of this object and add it to the XRServer. This tracking system will then obtain skeleton data, convert it to the Godot Humanoid skeleton and store this data on the XRBodyTracker object.

**Properties**
- `BitField[BodyFlags] body_flags` = `0`
- `bool has_tracking_data` = `false`
- `TrackerType type` = `32 (overrides XRTracker)`

**Methods**
- `BitField[JointFlags] get_joint_flags(joint: Joint) const`
- `Transform3D get_joint_transform(joint: Joint) const`
- `void set_joint_flags(joint: Joint, flags: BitField[JointFlags])`
- `void set_joint_transform(joint: Joint, transform: Transform3D)`

### XRCamera3D
*Inherits: **Camera3D < Node3D < Node < Object***

This is a helper 3D node for our camera. Note that, if stereoscopic rendering is applicable (VR-HMD), most of the camera properties are ignored, as the HMD information overrides them. The only properties that can be trusted are the near and far planes.

**Properties**
- `PhysicsInterpolationMode physics_interpolation_mode` = `2 (overrides Node)`

### XRController3D
*Inherits: **XRNode3D < Node3D < Node < Object***

This is a helper 3D node that is linked to the tracking of controllers. It also offers several handy passthroughs to the state of buttons and such on the controllers.

**Methods**
- `float get_float(name: StringName) const`
- `Variant get_input(name: StringName) const`
- `TrackerHand get_tracker_hand() const`
- `Vector2 get_vector2(name: StringName) const`
- `bool is_button_pressed(name: StringName) const`

### XRControllerTracker
*Inherits: **XRPositionalTracker < XRTracker < RefCounted < Object***

An instance of this object represents a controller that is tracked.

**Properties**
- `TrackerType type` = `2 (overrides XRTracker)`

### XRFaceModifier3D
*Inherits: **Node3D < Node < Object***

This node applies weights from an XRFaceTracker to a mesh with supporting face blend shapes.

**Properties**
- `StringName face_tracker` = `&"/user/face_tracker"`
- `NodePath target` = `NodePath("")`

### XRFaceTracker
*Inherits: **XRTracker < RefCounted < Object***

An instance of this object represents a tracked face and its corresponding blend shapes. The blend shapes come from the Unified Expressions standard, and contain extended details and visuals for each blend shape. Additionally the Tracking Standard Comparison page documents the relationship between Unified Expressions and other standards.

**Properties**
- `PackedFloat32Array blend_shapes` = `PackedFloat32Array()`
- `TrackerType type` = `64 (overrides XRTracker)`

**Methods**
- `float get_blend_shape(blend_shape: BlendShapeEntry) const`
- `void set_blend_shape(blend_shape: BlendShapeEntry, weight: float)`

### XRHandModifier3D
*Inherits: **SkeletonModifier3D < Node3D < Node < Object***

This node uses hand tracking data from an XRHandTracker to pose the skeleton of a hand mesh.

**Properties**
- `BoneUpdate bone_update` = `0`
- `StringName hand_tracker` = `&"/user/hand_tracker/left"`

### XRHandTracker
*Inherits: **XRPositionalTracker < XRTracker < RefCounted < Object***

A hand tracking system will create an instance of this object and add it to the XRServer. This tracking system will then obtain skeleton data, convert it to the Godot Humanoid hand skeleton and store this data on the XRHandTracker object.

**Properties**
- `TrackerHand hand` = `1 (overrides XRPositionalTracker)`
- `HandTrackingSource hand_tracking_source` = `0`
- `bool has_tracking_data` = `false`
- `TrackerType type` = `16 (overrides XRTracker)`

**Methods**
- `Vector3 get_hand_joint_angular_velocity(joint: HandJoint) const`
- `BitField[HandJointFlags] get_hand_joint_flags(joint: HandJoint) const`
- `Vector3 get_hand_joint_linear_velocity(joint: HandJoint) const`
- `float get_hand_joint_radius(joint: HandJoint) const`
- `Transform3D get_hand_joint_transform(joint: HandJoint) const`
- `void set_hand_joint_angular_velocity(joint: HandJoint, angular_velocity: Vector3)`
- `void set_hand_joint_flags(joint: HandJoint, flags: BitField[HandJointFlags])`
- `void set_hand_joint_linear_velocity(joint: HandJoint, linear_velocity: Vector3)`
- `void set_hand_joint_radius(joint: HandJoint, radius: float)`
- `void set_hand_joint_transform(joint: HandJoint, transform: Transform3D)`

### XRInterfaceExtension
*Inherits: **XRInterface < RefCounted < Object***

External XR interface plugins should inherit from this class.

**Methods**
- `void _end_frame() virtual`
- `bool _get_anchor_detection_is_enabled() virtual const`
- `int _get_camera_feed_id() virtual const`
- `Transform3D _get_camera_transform() virtual`
- `int _get_capabilities() virtual const`
- `RID _get_color_texture() virtual`
- `RID _get_depth_texture() virtual`
- `StringName _get_name() virtual const`
- `PackedVector3Array _get_play_area() virtual const`
- `PlayAreaMode _get_play_area_mode() virtual const`
- `PackedFloat64Array _get_projection_for_view(view: int, aspect: float, z_near: float, z_far: float) virtual`
- `Vector2 _get_render_target_size() virtual`
- `PackedStringArray _get_suggested_pose_names(tracker_name: StringName) virtual const`
- `PackedStringArray _get_suggested_tracker_names() virtual const`
- `Dictionary _get_system_info() virtual const`
- `TrackingStatus _get_tracking_status() virtual const`
- `Transform3D _get_transform_for_view(view: int, cam_transform: Transform3D) virtual`
- `RID _get_velocity_texture() virtual`
- `int _get_view_count() virtual`
- `RID _get_vrs_texture() virtual`
- `VRSTextureFormat _get_vrs_texture_format() virtual`
- `bool _initialize() virtual`
- `bool _is_initialized() virtual const`
- `void _post_draw_viewport(render_target: RID, screen_rect: Rect2) virtual`
- `bool _pre_draw_viewport(render_target: RID) virtual`
- `void _pre_render() virtual`
- `void _process() virtual`
- `void _set_anchor_detection_is_enabled(enabled: bool) virtual`
- `bool _set_play_area_mode(mode: PlayAreaMode) virtual const`
- `bool _supports_play_area_mode(mode: PlayAreaMode) virtual const`
- `void _trigger_haptic_pulse(action_name: String, tracker_name: StringName, frequency: float, amplitude: float, duration_sec: float, delay_sec: float) virtual`
- `void _uninitialize() virtual`
- `void add_blit(render_target: RID, src_rect: Rect2, dst_rect: Rect2i, use_layer: bool, layer: int, apply_lens_distortion: bool, eye_center: Vector2, k1: float, k2: float, upscale: float, aspect_ratio: float)`
- `RID get_color_texture()`
- `RID get_depth_texture()`
- `RID get_render_target_texture(render_target: RID)`
- `RID get_velocity_texture()`

### XRInterface
*Inherits: **RefCounted < Object** | Inherited by: MobileVRInterface, OpenXRInterface, WebXRInterface, XRInterfaceExtension*

This class needs to be implemented to make an AR or VR platform available to Godot and these should be implemented as C++ modules or GDExtension modules. Part of the interface is exposed to GDScript so you can detect, enable and configure an AR or VR platform.

**Properties**
- `bool ar_is_anchor_detection_enabled` = `false`
- `EnvironmentBlendMode environment_blend_mode` = `0`
- `bool interface_is_primary` = `false`
- `PlayAreaMode xr_play_area_mode` = `0`

**Methods**
- `int get_camera_feed_id()`
- `int get_capabilities() const`
- `StringName get_name() const`
- `PackedVector3Array get_play_area() const`
- `Projection get_projection_for_view(view: int, aspect: float, near: float, far: float)`
- `Vector2 get_render_target_size()`
- `Array get_supported_environment_blend_modes()`
- `Dictionary get_system_info()`
- `TrackingStatus get_tracking_status() const`
- `Transform3D get_transform_for_view(view: int, cam_transform: Transform3D)`
- `int get_view_count()`
- `bool initialize()`
- `bool is_initialized() const`
- `bool is_passthrough_enabled()`
- `bool is_passthrough_supported()`
- `bool set_environment_blend_mode(mode: EnvironmentBlendMode)`
- `bool set_play_area_mode(mode: PlayAreaMode)`
- `bool start_passthrough()`
- `void stop_passthrough()`
- `bool supports_play_area_mode(mode: PlayAreaMode)`
- `void trigger_haptic_pulse(action_name: String, tracker_name: StringName, frequency: float, amplitude: float, duration_sec: float, delay_sec: float)`
- `void uninitialize()`

**GDScript Examples**
```gdscript
func _ready():
    var xr_interface = XRServer.find_interface("OpenXR")
    if xr_interface and xr_interface.is_initialized():
        var vp = get_viewport()
        vp.use_xr = true
        var acceptable_modes = [XRInterface.XR_ENV_BLEND_MODE_OPAQUE, XRInterface.XR_ENV_BLEND_MODE_ADDITIVE]
        var modes = xr_interface.get_supported_environment_blend_modes()
        for mode in acceptable_modes:
            if mode in modes:
                xr_interface.set_environment_blend_mode(mode)
                break
```

### XRNode3D
*Inherits: **Node3D < Node < Object** | Inherited by: XRAnchor3D, XRController3D*

This node can be bound to a specific pose of an XRPositionalTracker and will automatically have its Node3D.transform updated by the XRServer. Nodes of this type must be added as children of the XROrigin3D node.

**Properties**
- `PhysicsInterpolationMode physics_interpolation_mode` = `2 (overrides Node)`
- `StringName pose` = `&"default"`
- `bool show_when_tracked` = `false`
- `StringName tracker` = `&""`

**Methods**
- `bool get_has_tracking_data() const`
- `bool get_is_active() const`
- `XRPose get_pose()`
- `void trigger_haptic_pulse(action_name: String, frequency: float, amplitude: float, duration_sec: float, delay_sec: float)`

### XROrigin3D
*Inherits: **Node3D < Node < Object***

This is a special node within the AR/VR system that maps the physical location of the center of our tracking space to the virtual location within our game world.

**Properties**
- `bool current` = `false`
- `float world_scale` = `1.0`

### XRPose
*Inherits: **RefCounted < Object***

XR runtimes often identify multiple locations on devices such as controllers that are spatially tracked.

**Properties**
- `Vector3 angular_velocity` = `Vector3(0, 0, 0)`
- `bool has_tracking_data` = `false`
- `Vector3 linear_velocity` = `Vector3(0, 0, 0)`
- `StringName name` = `&""`
- `TrackingConfidence tracking_confidence` = `0`
- `Transform3D transform` = `Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0)`

**Methods**
- `Transform3D get_adjusted_transform() const`

### XRPositionalTracker
*Inherits: **XRTracker < RefCounted < Object** | Inherited by: OpenXRSpatialEntityTracker, XRBodyTracker, XRControllerTracker, XRHandTracker*

An instance of this object represents a device that is tracked, such as a controller or anchor point. HMDs aren't represented here as they are handled internally.

**Properties**
- `TrackerHand hand` = `0`
- `String profile` = `""`

**Methods**
- `Variant get_input(name: StringName) const`
- `XRPose get_pose(name: StringName) const`
- `bool has_pose(name: StringName) const`
- `void invalidate_pose(name: StringName)`
- `void set_input(name: StringName, value: Variant)`
- `void set_pose(name: StringName, transform: Transform3D, linear_velocity: Vector3, angular_velocity: Vector3, tracking_confidence: TrackingConfidence)`

### XRServer
*Inherits: **Object***

The AR/VR server is the heart of our Advanced and Virtual Reality solution and handles all the processing.

**Properties**
- `bool camera_locked_to_origin` = `false`
- `XRInterface primary_interface`
- `Transform3D world_origin` = `Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0)`
- `float world_scale` = `1.0`

**Methods**
- `void add_interface(interface: XRInterface)`
- `void add_tracker(tracker: XRTracker)`
- `void center_on_hmd(rotation_mode: RotationMode, keep_height: bool)`
- `void clear_reference_frame()`
- `XRInterface find_interface(name: String) const`
- `Transform3D get_hmd_transform()`
- `XRInterface get_interface(idx: int) const`
- `int get_interface_count() const`
- `Array[Dictionary] get_interfaces() const`
- `Transform3D get_reference_frame() const`
- `XRTracker get_tracker(tracker_name: StringName) const`
- `Dictionary get_trackers(tracker_types: int)`
- `void remove_interface(interface: XRInterface)`
- `void remove_tracker(tracker: XRTracker)`

### XRTracker
*Inherits: **RefCounted < Object** | Inherited by: XRFaceTracker, XRPositionalTracker*

This object is the base of all XR trackers.

**Properties**
- `String description` = `""`
- `StringName name` = `&"Unknown"`
- `TrackerType type` = `128`

### XRVRS
*Inherits: **Object***

This class is used by various XR interfaces to generate VRS textures that can be used to speed up rendering.

**Properties**
- `float vrs_min_radius` = `20.0`
- `Rect2i vrs_render_region` = `Rect2i(0, 0, 0, 0)`
- `float vrs_strength` = `1.0`

**Methods**
- `RID make_vrs_texture(target_size: Vector2, eye_foci: PackedVector2Array)`

### bool

The bool is a built-in Variant type that may only store one of two values: true or false. You can imagine it as a switch that can be either turned on or off, or as a binary digit that can either be 1 or 0.

**GDScript Examples**
```gdscript
var can_shoot = true
if can_shoot:
    launch_bullet()
```
```gdscript
if bullets > 0 and not is_reloading():
    launch_bullet()

if bullets == 0 or is_reloading():
    play_clack_sound()
```

### float

The float built-in type is a 64-bit double-precision floating-point number, equivalent to double in C++. This type has 14 reliable decimal digits of precision. The maximum value of float is approximately 1.79769e308, and the minimum is approximately -1.79769e308.

**GDScript Examples**
```gdscript
print(1.5 * Color(0.5, 0.5, 0.5)) # Prints (0.75, 0.75, 0.75, 1.5)
```
```gdscript
print(2.5 * Vector2(1, 3)) # Prints (2.5, 7.5)
```

### int

Signed 64-bit integer type. This means that it can take values from -2^63 to 2^63 - 1, i.e. from -9223372036854775808 to 9223372036854775807. When it exceeds these bounds, it will wrap around.

**GDScript Examples**
```gdscript
var x: int = 1 # x is 1
x = 4.2 # x is 4, because 4.2 gets truncated
var max_int = 9223372036854775807 # Biggest value an int can store
max_int += 1 # max_int is -9223372036854775808, because it wrapped around
```
```gdscript
var x = 0b1001 # x is 9
var y = 0xF5 # y is 245
var z = 10_000_000 # z is 10000000
```
