# Godot 4 GDScript API Reference — Nodes 3D

> GDScript-only reference. 39 classes.

### AnimatableBody3D
*Inherits: **StaticBody3D < PhysicsBody3D < CollisionObject3D < Node3D < Node < Object***

An animatable 3D physics body. It can't be moved by external forces or contacts, but can be moved manually by other means such as code, AnimationMixers (with AnimationMixer.callback_mode_process set to AnimationMixer.ANIMATION_CALLBACK_MODE_PROCESS_PHYSICS), and RemoteTransform3D.

**Properties**
- `bool sync_to_physics` = `true`

### BoneAttachment3D
*Inherits: **Node3D < Node < Object***

This node selects a bone in a Skeleton3D and attaches to it. This means that the BoneAttachment3D node will either dynamically copy or override the 3D transform of the selected bone.

**Properties**
- `int bone_idx` = `-1`
- `String bone_name` = `""`
- `NodePath external_skeleton`
- `bool override_pose` = `false`
- `PhysicsInterpolationMode physics_interpolation_mode` = `2 (overrides Node)`
- `bool use_external_skeleton` = `false`

**Methods**
- `Skeleton3D get_skeleton()`
- `void on_skeleton_update()`

### Camera3D
*Inherits: **Node3D < Node < Object** | Inherited by: XRCamera3D*

Camera3D is a special node that displays what is visible from its current location. Cameras register themselves in the nearest Viewport node (when ascending the tree). Only one camera can be active per viewport. If no viewport is available ascending the tree, the camera will register in the global viewport. In other words, a camera just provides 3D display capabilities to a Viewport, and, without one, a scene registered in that Viewport (or higher viewports) can't be displayed.

**Properties**
- `CameraAttributes attributes`
- `Compositor compositor`
- `int cull_mask` = `1048575`
- `bool current` = `false`
- `DopplerTracking doppler_tracking` = `0`
- `Environment environment`
- `float far` = `4000.0`
- `float fov` = `75.0`
- `Vector2 frustum_offset` = `Vector2(0, 0)`
- `float h_offset` = `0.0`
- `KeepAspect keep_aspect` = `1`
- `float near` = `0.05`
- `ProjectionType projection` = `0`
- `float size` = `1.0`
- `float v_offset` = `0.0`

**Methods**
- `void clear_current(enable_next: bool = true)`
- `Projection get_camera_projection() const`
- `RID get_camera_rid() const`
- `Transform3D get_camera_transform() const`
- `bool get_cull_mask_value(layer_number: int) const`
- `Array[Plane] get_frustum() const`
- `RID get_pyramid_shape_rid()`
- `bool is_position_behind(world_point: Vector3) const`
- `bool is_position_in_frustum(world_point: Vector3) const`
- `void make_current()`
- `Vector3 project_local_ray_normal(screen_point: Vector2) const`
- `Vector3 project_position(screen_point: Vector2, z_depth: float) const`
- `Vector3 project_ray_normal(screen_point: Vector2) const`
- `Vector3 project_ray_origin(screen_point: Vector2) const`
- `void set_cull_mask_value(layer_number: int, value: bool)`
- `void set_frustum(size: float, offset: Vector2, z_near: float, z_far: float)`
- `void set_orthogonal(size: float, z_near: float, z_far: float)`
- `void set_perspective(fov: float, z_near: float, z_far: float)`
- `Vector2 unproject_position(world_point: Vector3) const`

**GDScript Examples**
```gdscript
# This code block is part of a script that inherits from Node3D.
# `control` is a reference to a node inheriting from Control.
control.visible = not get_viewport().get_camera_3d().is_position_behind(global_transform.origin)
control.position = get_viewport().get_camera_3d().unproject_position(global_transform.origin)
```

### CharacterBody3D
*Inherits: **PhysicsBody3D < CollisionObject3D < Node3D < Node < Object***

CharacterBody3D is a specialized class for physics bodies that are meant to be user-controlled. They are not affected by physics at all, but they affect other physics bodies in their path. They are mainly used to provide high-level API to move objects with wall and slope detection (move_and_slide() method) in addition to the general collision detection provided by PhysicsBody3D.move_and_collide(). This makes it useful for highly configurable physics bodies that must move in specific ways and collide with the world, as is often the case with user-controlled characters.

**Properties**
- `bool floor_block_on_wall` = `true`
- `bool floor_constant_speed` = `false`
- `float floor_max_angle` = `0.7853982`
- `float floor_snap_length` = `0.1`
- `bool floor_stop_on_slope` = `true`
- `int max_slides` = `6`
- `MotionMode motion_mode` = `0`
- `int platform_floor_layers` = `4294967295`
- `PlatformOnLeave platform_on_leave` = `0`
- `int platform_wall_layers` = `0`
- `float safe_margin` = `0.001`
- `bool slide_on_ceiling` = `true`
- `Vector3 up_direction` = `Vector3(0, 1, 0)`
- `Vector3 velocity` = `Vector3(0, 0, 0)`
- `float wall_min_slide_angle` = `0.2617994`

**Methods**
- `void apply_floor_snap()`
- `float get_floor_angle(up_direction: Vector3 = Vector3(0, 1, 0)) const`
- `Vector3 get_floor_normal() const`
- `Vector3 get_last_motion() const`
- `KinematicCollision3D get_last_slide_collision()`
- `Vector3 get_platform_angular_velocity() const`
- `Vector3 get_platform_velocity() const`
- `Vector3 get_position_delta() const`
- `Vector3 get_real_velocity() const`
- `KinematicCollision3D get_slide_collision(slide_idx: int)`
- `int get_slide_collision_count() const`
- `Vector3 get_wall_normal() const`
- `bool is_on_ceiling() const`
- `bool is_on_ceiling_only() const`
- `bool is_on_floor() const`
- `bool is_on_floor_only() const`
- `bool is_on_wall() const`
- `bool is_on_wall_only() const`
- `bool move_and_slide()`

### DirectionalLight3D
*Inherits: **Light3D < VisualInstance3D < Node3D < Node < Object***

A directional light is a type of Light3D node that models an infinite number of parallel rays covering the entire scene. It is used for lights with strong intensity that are located far away from the scene to model sunlight or moonlight.

**Properties**
- `bool directional_shadow_blend_splits` = `false`
- `float directional_shadow_fade_start` = `0.8`
- `float directional_shadow_max_distance` = `100.0`
- `ShadowMode directional_shadow_mode` = `2`
- `float directional_shadow_pancake_size` = `20.0`
- `float directional_shadow_split_1` = `0.1`
- `float directional_shadow_split_2` = `0.2`
- `float directional_shadow_split_3` = `0.5`
- `SkyMode sky_mode` = `0`

### FogVolume
*Inherits: **VisualInstance3D < Node3D < Node < Object***

FogVolumes are used to add localized fog into the global volumetric fog effect. FogVolumes can also remove volumetric fog from specific areas if using a FogMaterial with a negative FogMaterial.density.

**Properties**
- `Material material`
- `FogVolumeShape shape` = `3`
- `Vector3 size` = `Vector3(2, 2, 2)`

### GeometryInstance3D
*Inherits: **VisualInstance3D < Node3D < Node < Object** | Inherited by: CPUParticles3D, CSGShape3D, GPUParticles3D, Label3D, MeshInstance3D, MultiMeshInstance3D, ...*

Base node for geometry-based visual instances. Shares some common functionality like visibility and custom materials.

**Properties**
- `ShadowCastingSetting cast_shadow` = `1`
- `AABB custom_aabb` = `AABB(0, 0, 0, 0, 0, 0)`
- `float extra_cull_margin` = `0.0`
- `LightmapScale gi_lightmap_scale` = `0`
- `float gi_lightmap_texel_scale` = `1.0`
- `GIMode gi_mode` = `1`
- `bool ignore_occlusion_culling` = `false`
- `float lod_bias` = `1.0`
- `Material material_overlay`
- `Material material_override`
- `float transparency` = `0.0`
- `float visibility_range_begin` = `0.0`
- `float visibility_range_begin_margin` = `0.0`
- `float visibility_range_end` = `0.0`
- `float visibility_range_end_margin` = `0.0`
- `VisibilityRangeFadeMode visibility_range_fade_mode` = `0`

**Methods**
- `Variant get_instance_shader_parameter(name: StringName) const`
- `void set_instance_shader_parameter(name: StringName, value: Variant)`

### Light3D
*Inherits: **VisualInstance3D < Node3D < Node < Object** | Inherited by: DirectionalLight3D, OmniLight3D, SpotLight3D*

Light3D is the abstract base class for light nodes. As it can't be instantiated, it shouldn't be used directly. Other types of light nodes inherit from it. Light3D contains the common variables and parameters used for lighting.

**Properties**
- `float distance_fade_begin` = `40.0`
- `bool distance_fade_enabled` = `false`
- `float distance_fade_length` = `10.0`
- `float distance_fade_shadow` = `50.0`
- `bool editor_only` = `false`
- `float light_angular_distance` = `0.0`
- `BakeMode light_bake_mode` = `2`
- `Color light_color` = `Color(1, 1, 1, 1)`
- `int light_cull_mask` = `4294967295`
- `float light_energy` = `1.0`
- `float light_indirect_energy` = `1.0`
- `float light_intensity_lumens`
- `float light_intensity_lux`
- `bool light_negative` = `false`
- `Texture2D light_projector`
- `float light_size` = `0.0`
- `float light_specular` = `1.0`
- `float light_temperature`
- `float light_volumetric_fog_energy` = `1.0`
- `float shadow_bias` = `0.1`
- `float shadow_blur` = `1.0`
- `int shadow_caster_mask` = `4294967295`
- `bool shadow_enabled` = `false`
- `float shadow_normal_bias` = `2.0`
- `float shadow_opacity` = `1.0`
- `bool shadow_reverse_cull_face` = `false`
- `float shadow_transmittance_bias` = `0.05`

**Methods**
- `Color get_correlated_color() const`
- `float get_param(param: Param) const`
- `void set_param(param: Param, value: float)`

### LightmapGIData
*Inherits: **Resource < RefCounted < Object***

LightmapGIData contains baked lightmap and dynamic object probe data for LightmapGI. It is replaced every time lightmaps are baked in LightmapGI.

**Properties**
- `TextureLayered light_texture`
- `Array[TextureLayered] lightmap_textures` = `[]`
- `Array[TextureLayered] shadowmask_textures` = `[]`

**Methods**
- `void add_user(path: NodePath, uv_scale: Rect2, slice_index: int, sub_instance: int)`
- `void clear_users()`
- `int get_user_count() const`
- `NodePath get_user_path(user_idx: int) const`
- `bool is_using_spherical_harmonics() const`
- `void set_uses_spherical_harmonics(uses_spherical_harmonics: bool)`

### LightmapGI
*Inherits: **VisualInstance3D < Node3D < Node < Object***

The LightmapGI node is used to compute and store baked lightmaps. Lightmaps are used to provide high-quality indirect lighting with very little light leaking. LightmapGI can also provide rough reflections using spherical harmonics if directional is enabled. Dynamic objects can receive indirect lighting thanks to light probes, which can be automatically placed by setting generate_probes_subdiv to a value other than GENERATE_PROBES_DISABLED. Additional lightmap probes can also be added by creating LightmapProbe nodes. The downside is that lightmaps are fully static and cannot be baked in an exported project. Baking a LightmapGI node is also slower compared to VoxelGI.

**Properties**
- `float bias` = `0.0005`
- `float bounce_indirect_energy` = `1.0`
- `int bounces` = `3`
- `CameraAttributes camera_attributes`
- `int denoiser_range` = `10`
- `float denoiser_strength` = `0.1`
- `bool directional` = `false`
- `Color environment_custom_color` = `Color(1, 1, 1, 1)`
- `float environment_custom_energy` = `1.0`
- `Sky environment_custom_sky`
- `EnvironmentMode environment_mode` = `1`
- `GenerateProbes generate_probes_subdiv` = `2`
- `bool interior` = `false`
- `LightmapGIData light_data`
- `int max_texture_size` = `16384`
- `BakeQuality quality` = `1`
- `ShadowmaskMode shadowmask_mode` = `0`
- `bool supersampling` = `false`
- `float supersampling_factor` = `2.0`
- `float texel_scale` = `1.0`
- `bool use_denoiser` = `true`
- `bool use_texture_for_bounces` = `true`

### LightmapProbe
*Inherits: **Node3D < Node < Object***

LightmapProbe represents the position of a single manually placed probe for dynamic object lighting with LightmapGI. Lightmap probes affect the lighting of GeometryInstance3D-derived nodes that have their GeometryInstance3D.gi_mode set to GeometryInstance3D.GI_MODE_DYNAMIC.

### Marker3D
*Inherits: **Node3D < Node < Object***

Generic 3D position hint for editing. It's just like a plain Node3D, but it displays as a cross in the 3D editor at all times.

**Properties**
- `float gizmo_extents` = `0.25`

### MeshInstance3D
*Inherits: **GeometryInstance3D < VisualInstance3D < Node3D < Node < Object** | Inherited by: SoftBody3D*

MeshInstance3D is a node that takes a Mesh resource and adds it to the current scenario by creating an instance of it. This is the class most often used to render 3D geometry and can be used to instance a single Mesh in many places. This allows reusing geometry, which can save on resources. When a Mesh has to be instantiated more than thousands of times at close proximity, consider using a MultiMesh in a MultiMeshInstance3D instead.

**Properties**
- `Mesh mesh`
- `NodePath skeleton` = `NodePath("")`
- `Skin skin`

**Methods**
- `ArrayMesh bake_mesh_from_current_blend_shape_mix(existing: ArrayMesh = null)`
- `ArrayMesh bake_mesh_from_current_skeleton_pose(existing: ArrayMesh = null)`
- `void create_convex_collision(clean: bool = true, simplify: bool = false)`
- `void create_debug_tangents()`
- `void create_multiple_convex_collisions(settings: MeshConvexDecompositionSettings = null)`
- `void create_trimesh_collision()`
- `int find_blend_shape_by_name(name: StringName)`
- `Material get_active_material(surface: int) const`
- `int get_blend_shape_count() const`
- `float get_blend_shape_value(blend_shape_idx: int) const`
- `SkinReference get_skin_reference() const`
- `Material get_surface_override_material(surface: int) const`
- `int get_surface_override_material_count() const`
- `void set_blend_shape_value(blend_shape_idx: int, value: float)`
- `void set_surface_override_material(surface: int, material: Material)`

### MultiMeshInstance3D
*Inherits: **GeometryInstance3D < VisualInstance3D < Node3D < Node < Object***

MultiMeshInstance3D is a specialized node to instance GeometryInstance3Ds based on a MultiMesh resource.

**Properties**
- `MultiMesh multimesh`

### NavigationAgent3D
*Inherits: **Node < Object***

A 3D agent used to pathfind to a position while avoiding static and dynamic obstacles. The calculation can be used by the parent node to dynamically move it along the path. Requires navigation data to work correctly.

**Properties**
- `bool avoidance_enabled` = `false`
- `int avoidance_layers` = `1`
- `int avoidance_mask` = `1`
- `float avoidance_priority` = `1.0`
- `bool debug_enabled` = `false`
- `Color debug_path_custom_color` = `Color(1, 1, 1, 1)`
- `float debug_path_custom_point_size` = `4.0`
- `bool debug_use_custom` = `false`
- `float height` = `1.0`
- `bool keep_y_velocity` = `true`
- `int max_neighbors` = `10`
- `float max_speed` = `10.0`
- `int navigation_layers` = `1`
- `float neighbor_distance` = `50.0`
- `float path_desired_distance` = `1.0`
- `float path_height_offset` = `0.0`
- `float path_max_distance` = `5.0`
- `BitField[PathMetadataFlags] path_metadata_flags` = `7`
- `PathPostProcessing path_postprocessing` = `0`
- `float path_return_max_length` = `0.0`
- `float path_return_max_radius` = `0.0`
- `float path_search_max_distance` = `0.0`
- `int path_search_max_polygons` = `4096`
- `PathfindingAlgorithm pathfinding_algorithm` = `0`
- `float radius` = `0.5`
- `float simplify_epsilon` = `0.0`
- `bool simplify_path` = `false`
- `float target_desired_distance` = `1.0`
- `Vector3 target_position` = `Vector3(0, 0, 0)`
- `float time_horizon_agents` = `1.0`

**Methods**
- `float distance_to_target() const`
- `bool get_avoidance_layer_value(layer_number: int) const`
- `bool get_avoidance_mask_value(mask_number: int) const`
- `PackedVector3Array get_current_navigation_path() const`
- `int get_current_navigation_path_index() const`
- `NavigationPathQueryResult3D get_current_navigation_result() const`
- `Vector3 get_final_position()`
- `bool get_navigation_layer_value(layer_number: int) const`
- `RID get_navigation_map() const`
- `Vector3 get_next_path_position()`
- `float get_path_length() const`
- `RID get_rid() const`
- `bool is_navigation_finished()`
- `bool is_target_reachable()`
- `bool is_target_reached() const`
- `void set_avoidance_layer_value(layer_number: int, value: bool)`
- `void set_avoidance_mask_value(mask_number: int, value: bool)`
- `void set_navigation_layer_value(layer_number: int, value: bool)`
- `void set_navigation_map(navigation_map: RID)`
- `void set_velocity_forced(velocity: Vector3)`

### NavigationLink3D
*Inherits: **Node3D < Node < Object***

A link between two positions on NavigationRegion3Ds that agents can be routed through. These positions can be on the same NavigationRegion3D or on two different ones. Links are useful to express navigation methods other than traveling along the surface of the navigation mesh, such as ziplines, teleporters, or gaps that can be jumped across.

**Properties**
- `bool bidirectional` = `true`
- `bool enabled` = `true`
- `Vector3 end_position` = `Vector3(0, 0, 0)`
- `float enter_cost` = `0.0`
- `int navigation_layers` = `1`
- `Vector3 start_position` = `Vector3(0, 0, 0)`
- `float travel_cost` = `1.0`

**Methods**
- `Vector3 get_global_end_position() const`
- `Vector3 get_global_start_position() const`
- `bool get_navigation_layer_value(layer_number: int) const`
- `RID get_navigation_map() const`
- `RID get_rid() const`
- `void set_global_end_position(position: Vector3)`
- `void set_global_start_position(position: Vector3)`
- `void set_navigation_layer_value(layer_number: int, value: bool)`
- `void set_navigation_map(navigation_map: RID)`

### NavigationObstacle3D
*Inherits: **Node3D < Node < Object***

An obstacle needs a navigation map and outline vertices defined to work correctly. The outlines can not cross or overlap and are restricted to a plane projection. This means the y-axis of the vertices is ignored, instead the obstacle's global y-axis position is used for placement. The projected shape is extruded by the obstacles height along the y-axis.

**Properties**
- `bool affect_navigation_mesh` = `false`
- `bool avoidance_enabled` = `true`
- `int avoidance_layers` = `1`
- `bool carve_navigation_mesh` = `false`
- `float height` = `1.0`
- `float radius` = `0.0`
- `bool use_3d_avoidance` = `false`
- `Vector3 velocity` = `Vector3(0, 0, 0)`
- `PackedVector3Array vertices` = `PackedVector3Array()`

**Methods**
- `bool get_avoidance_layer_value(layer_number: int) const`
- `RID get_navigation_map() const`
- `RID get_rid() const`
- `void set_avoidance_layer_value(layer_number: int, value: bool)`
- `void set_navigation_map(navigation_map: RID)`

### NavigationRegion3D
*Inherits: **Node3D < Node < Object***

A traversable 3D region based on a NavigationMesh that NavigationAgent3Ds can use for pathfinding.

**Properties**
- `bool enabled` = `true`
- `float enter_cost` = `0.0`
- `int navigation_layers` = `1`
- `NavigationMesh navigation_mesh`
- `float travel_cost` = `1.0`
- `bool use_edge_connections` = `true`

**Methods**
- `void bake_navigation_mesh(on_thread: bool = true)`
- `AABB get_bounds() const`
- `bool get_navigation_layer_value(layer_number: int) const`
- `RID get_navigation_map() const`
- `RID get_region_rid() const`
- `RID get_rid() const`
- `bool is_baking() const`
- `void set_navigation_layer_value(layer_number: int, value: bool)`
- `void set_navigation_map(navigation_map: RID)`

### Node3DGizmo
*Inherits: **RefCounted < Object** | Inherited by: EditorNode3DGizmo*

This abstract class helps connect the Node3D scene with the editor-specific EditorNode3DGizmo class.

### Node3D
*Inherits: **Node < Object** | Inherited by: AudioListener3D, AudioStreamPlayer3D, BoneAttachment3D, Camera3D, CollisionObject3D, CollisionPolygon3D, ...*

The Node3D node is the base representation of a node in 3D space. All other 3D nodes inherit from this class.

**Properties**
- `Basis basis`
- `Basis global_basis`
- `Vector3 global_position`
- `Vector3 global_rotation`
- `Vector3 global_rotation_degrees`
- `Transform3D global_transform`
- `Vector3 position` = `Vector3(0, 0, 0)`
- `Quaternion quaternion`
- `Vector3 rotation` = `Vector3(0, 0, 0)`
- `Vector3 rotation_degrees`
- `RotationEditMode rotation_edit_mode` = `0`
- `EulerOrder rotation_order` = `2`
- `Vector3 scale` = `Vector3(1, 1, 1)`
- `bool top_level` = `false`
- `Transform3D transform` = `Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0)`
- `NodePath visibility_parent` = `NodePath("")`
- `bool visible` = `true`

**Methods**
- `void add_gizmo(gizmo: Node3DGizmo)`
- `void clear_gizmos()`
- `void clear_subgizmo_selection()`
- `void force_update_transform()`
- `Array[Node3DGizmo] get_gizmos() const`
- `Transform3D get_global_transform_interpolated()`
- `Node3D get_parent_node_3d() const`
- `World3D get_world_3d() const`
- `void global_rotate(axis: Vector3, angle: float)`
- `void global_scale(scale: Vector3)`
- `void global_translate(offset: Vector3)`
- `void hide()`
- `bool is_local_transform_notification_enabled() const`
- `bool is_scale_disabled() const`
- `bool is_transform_notification_enabled() const`
- `bool is_visible_in_tree() const`
- `void look_at(target: Vector3, up: Vector3 = Vector3(0, 1, 0), use_model_front: bool = false)`
- `void look_at_from_position(position: Vector3, target: Vector3, up: Vector3 = Vector3(0, 1, 0), use_model_front: bool = false)`
- `void orthonormalize()`
- `void rotate(axis: Vector3, angle: float)`
- `void rotate_object_local(axis: Vector3, angle: float)`
- `void rotate_x(angle: float)`
- `void rotate_y(angle: float)`
- `void rotate_z(angle: float)`
- `void scale_object_local(scale: Vector3)`
- `void set_disable_scale(disable: bool)`
- `void set_identity()`
- `void set_ignore_transform_notification(enabled: bool)`
- `void set_notify_local_transform(enable: bool)`
- `void set_notify_transform(enable: bool)`
- `void set_subgizmo_selection(gizmo: Node3DGizmo, id: int, transform: Transform3D)`
- `void show()`
- `Vector3 to_global(local_point: Vector3) const`
- `Vector3 to_local(global_point: Vector3) const`
- `void translate(offset: Vector3)`
- `void translate_object_local(offset: Vector3)`
- `void update_gizmos()`

### OmniLight3D
*Inherits: **Light3D < VisualInstance3D < Node3D < Node < Object***

An Omnidirectional light is a type of Light3D that emits light in all directions. The light is attenuated by distance and this attenuation can be configured by changing its energy, radius, and attenuation parameters.

**Properties**
- `float light_specular` = `0.5 (overrides Light3D)`
- `float omni_attenuation` = `1.0`
- `float omni_range` = `5.0`
- `ShadowMode omni_shadow_mode` = `1`
- `float shadow_normal_bias` = `1.0 (overrides Light3D)`

### Path3D
*Inherits: **Node3D < Node < Object***

Can have PathFollow3D child nodes moving along the Curve3D. See PathFollow3D for more information on the usage.

**Properties**
- `Curve3D curve`
- `Color debug_custom_color` = `Color(0, 0, 0, 1)`

### PathFollow3D
*Inherits: **Node3D < Node < Object***

This node takes its parent Path3D, and returns the coordinates of a point within it, given a distance from the first vertex.

**Properties**
- `bool cubic_interp` = `true`
- `float h_offset` = `0.0`
- `bool loop` = `true`
- `float progress` = `0.0`
- `float progress_ratio` = `0.0`
- `RotationMode rotation_mode` = `3`
- `bool tilt_enabled` = `true`
- `bool use_model_front` = `false`
- `float v_offset` = `0.0`

**Methods**
- `Transform3D correct_posture(transform: Transform3D, rotation_mode: RotationMode) static`

### RayCast3D
*Inherits: **Node3D < Node < Object***

A raycast represents a ray from its origin to its target_position that finds the closest object along its path, if it intersects any.

**Properties**
- `bool collide_with_areas` = `false`
- `bool collide_with_bodies` = `true`
- `int collision_mask` = `1`
- `Color debug_shape_custom_color` = `Color(0, 0, 0, 1)`
- `int debug_shape_thickness` = `2`
- `bool enabled` = `true`
- `bool exclude_parent` = `true`
- `bool hit_back_faces` = `true`
- `bool hit_from_inside` = `false`
- `Vector3 target_position` = `Vector3(0, -1, 0)`

**Methods**
- `void add_exception(node: CollisionObject3D)`
- `void add_exception_rid(rid: RID)`
- `void clear_exceptions()`
- `void force_raycast_update()`
- `Object get_collider() const`
- `RID get_collider_rid() const`
- `int get_collider_shape() const`
- `int get_collision_face_index() const`
- `bool get_collision_mask_value(layer_number: int) const`
- `Vector3 get_collision_normal() const`
- `Vector3 get_collision_point() const`
- `bool is_colliding() const`
- `void remove_exception(node: CollisionObject3D)`
- `void remove_exception_rid(rid: RID)`
- `void set_collision_mask_value(layer_number: int, value: bool)`

**GDScript Examples**
```gdscript
var target = get_collider() # A CollisionObject3D.
var shape_id = get_collider_shape() # The shape index in the collider.
var owner_id = target.shape_find_owner(shape_id) # The owner ID in the collider.
var shape = target.shape_owner_get_owner(owner_id)
```

### ReflectionProbe
*Inherits: **VisualInstance3D < Node3D < Node < Object***

Captures its surroundings as a cubemap, and stores versions of it with increasing levels of blur to simulate different material roughnesses.

**Properties**
- `Color ambient_color` = `Color(0, 0, 0, 1)`
- `float ambient_color_energy` = `1.0`
- `AmbientMode ambient_mode` = `1`
- `float blend_distance` = `1.0`
- `bool box_projection` = `false`
- `int cull_mask` = `1048575`
- `bool enable_shadows` = `false`
- `float intensity` = `1.0`
- `bool interior` = `false`
- `float max_distance` = `0.0`
- `float mesh_lod_threshold` = `1.0`
- `Vector3 origin_offset` = `Vector3(0, 0, 0)`
- `int reflection_mask` = `1048575`
- `Vector3 size` = `Vector3(20, 20, 20)`
- `UpdateMode update_mode` = `0`

### RemoteTransform3D
*Inherits: **Node3D < Node < Object***

RemoteTransform3D pushes its own Transform3D to another Node3D derived Node (called the remote node) in the scene.

**Properties**
- `NodePath remote_path` = `NodePath("")`
- `bool update_position` = `true`
- `bool update_rotation` = `true`
- `bool update_scale` = `true`
- `bool use_global_coordinates` = `true`

**Methods**
- `void force_update_cache()`

### RigidBody3D
*Inherits: **PhysicsBody3D < CollisionObject3D < Node3D < Node < Object** | Inherited by: VehicleBody3D*

RigidBody3D implements full 3D physics. It cannot be controlled directly, instead, you must apply forces to it (gravity, impulses, etc.), and the physics simulation will calculate the resulting movement, rotation, react to collisions, and affect other physics bodies in its path.

**Properties**
- `float angular_damp` = `0.0`
- `DampMode angular_damp_mode` = `0`
- `Vector3 angular_velocity` = `Vector3(0, 0, 0)`
- `bool can_sleep` = `true`
- `Vector3 center_of_mass` = `Vector3(0, 0, 0)`
- `CenterOfMassMode center_of_mass_mode` = `0`
- `Vector3 constant_force` = `Vector3(0, 0, 0)`
- `Vector3 constant_torque` = `Vector3(0, 0, 0)`
- `bool contact_monitor` = `false`
- `bool continuous_cd` = `false`
- `bool custom_integrator` = `false`
- `bool freeze` = `false`
- `FreezeMode freeze_mode` = `0`
- `float gravity_scale` = `1.0`
- `Vector3 inertia` = `Vector3(0, 0, 0)`
- `float linear_damp` = `0.0`
- `DampMode linear_damp_mode` = `0`
- `Vector3 linear_velocity` = `Vector3(0, 0, 0)`
- `bool lock_rotation` = `false`
- `float mass` = `1.0`
- `int max_contacts_reported` = `0`
- `PhysicsMaterial physics_material_override`
- `bool sleeping` = `false`

**Methods**
- `void _integrate_forces(state: PhysicsDirectBodyState3D) virtual`
- `void add_constant_central_force(force: Vector3)`
- `void add_constant_force(force: Vector3, position: Vector3 = Vector3(0, 0, 0))`
- `void add_constant_torque(torque: Vector3)`
- `void apply_central_force(force: Vector3)`
- `void apply_central_impulse(impulse: Vector3)`
- `void apply_force(force: Vector3, position: Vector3 = Vector3(0, 0, 0))`
- `void apply_impulse(impulse: Vector3, position: Vector3 = Vector3(0, 0, 0))`
- `void apply_torque(torque: Vector3)`
- `void apply_torque_impulse(impulse: Vector3)`
- `Array[Node3D] get_colliding_bodies() const`
- `int get_contact_count() const`
- `Basis get_inverse_inertia_tensor() const`
- `void set_axis_velocity(axis_velocity: Vector3)`

**GDScript Examples**
```gdscript
@onready var ball = $Ball

func get_ball_inertia():
    return PhysicsServer3D.body_get_direct_state(ball.get_rid()).inverse_inertia.inverse()
```

### ShapeCast3D
*Inherits: **Node3D < Node < Object***

Shape casting allows to detect collision objects by sweeping its shape along the cast direction determined by target_position. This is similar to RayCast3D, but it allows for sweeping a region of space, rather than just a straight line. ShapeCast3D can detect multiple collision objects. It is useful for things like wide laser beams or snapping a simple shape to a floor.

**Properties**
- `bool collide_with_areas` = `false`
- `bool collide_with_bodies` = `true`
- `int collision_mask` = `1`
- `Array collision_result` = `[]`
- `Color debug_shape_custom_color` = `Color(0, 0, 0, 1)`
- `bool enabled` = `true`
- `bool exclude_parent` = `true`
- `float margin` = `0.0`
- `int max_results` = `32`
- `Shape3D shape`
- `Vector3 target_position` = `Vector3(0, -1, 0)`

**Methods**
- `void add_exception(node: CollisionObject3D)`
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
- `Vector3 get_collision_normal(index: int) const`
- `Vector3 get_collision_point(index: int) const`
- `bool is_colliding() const`
- `void remove_exception(node: CollisionObject3D)`
- `void remove_exception_rid(rid: RID)`
- `void resource_changed(resource: Resource)`
- `void set_collision_mask_value(layer_number: int, value: bool)`

### Skeleton3D
*Inherits: **Node3D < Node < Object***

Skeleton3D provides an interface for managing a hierarchy of bones, including pose, rest and animation (see Animation). It can also use ragdoll physics.

**Properties**
- `bool animate_physical_bones` = `true`
- `ModifierCallbackModeProcess modifier_callback_mode_process` = `1`
- `float motion_scale` = `1.0`
- `bool show_rest_only` = `false`

**Methods**
- `int add_bone(name: String)`
- `void advance(delta: float)`
- `void clear_bones()`
- `void clear_bones_global_pose_override()`
- `Skin create_skin_from_rest_transforms()`
- `int find_bone(name: String) const`
- `void force_update_all_bone_transforms()`
- `void force_update_bone_child_transform(bone_idx: int)`
- `PackedInt32Array get_bone_children(bone_idx: int) const`
- `int get_bone_count() const`
- `Transform3D get_bone_global_pose(bone_idx: int) const`
- `Transform3D get_bone_global_pose_no_override(bone_idx: int) const`
- `Transform3D get_bone_global_pose_override(bone_idx: int) const`
- `Transform3D get_bone_global_rest(bone_idx: int) const`
- `Variant get_bone_meta(bone_idx: int, key: StringName) const`
- `Array[StringName] get_bone_meta_list(bone_idx: int) const`
- `String get_bone_name(bone_idx: int) const`
- `int get_bone_parent(bone_idx: int) const`
- `Transform3D get_bone_pose(bone_idx: int) const`
- `Vector3 get_bone_pose_position(bone_idx: int) const`
- `Quaternion get_bone_pose_rotation(bone_idx: int) const`
- `Vector3 get_bone_pose_scale(bone_idx: int) const`
- `Transform3D get_bone_rest(bone_idx: int) const`
- `StringName get_concatenated_bone_names() const`
- `PackedInt32Array get_parentless_bones() const`
- `int get_version() const`
- `bool has_bone_meta(bone_idx: int, key: StringName) const`
- `bool is_bone_enabled(bone_idx: int) const`
- `void localize_rests()`
- `void physical_bones_add_collision_exception(exception: RID)`
- `void physical_bones_remove_collision_exception(exception: RID)`
- `void physical_bones_start_simulation(bones: Array[StringName] = [])`
- `void physical_bones_stop_simulation()`
- `SkinReference register_skin(skin: Skin)`
- `void reset_bone_pose(bone_idx: int)`
- `void reset_bone_poses()`
- `void set_bone_enabled(bone_idx: int, enabled: bool = true)`
- `void set_bone_global_pose(bone_idx: int, pose: Transform3D)`
- `void set_bone_global_pose_override(bone_idx: int, pose: Transform3D, amount: float, persistent: bool = false)`
- `void set_bone_meta(bone_idx: int, key: StringName, value: Variant)`

### SoftBody3D
*Inherits: **MeshInstance3D < GeometryInstance3D < VisualInstance3D < Node3D < Node < Object***

A deformable 3D physics mesh. Used to create elastic or deformable objects such as cloth, rubber, or other flexible materials.

**Properties**
- `int collision_layer` = `1`
- `int collision_mask` = `1`
- `float damping_coefficient` = `0.01`
- `DisableMode disable_mode` = `0`
- `float drag_coefficient` = `0.0`
- `float linear_stiffness` = `0.5`
- `NodePath parent_collision_ignore` = `NodePath("")`
- `float pressure_coefficient` = `0.0`
- `bool ray_pickable` = `true`
- `float shrinking_factor` = `0.0`
- `int simulation_precision` = `5`
- `float total_mass` = `1.0`

**Methods**
- `void add_collision_exception_with(body: Node)`
- `void apply_central_force(force: Vector3)`
- `void apply_central_impulse(impulse: Vector3)`
- `void apply_force(point_index: int, force: Vector3)`
- `void apply_impulse(point_index: int, impulse: Vector3)`
- `Array[PhysicsBody3D] get_collision_exceptions()`
- `bool get_collision_layer_value(layer_number: int) const`
- `bool get_collision_mask_value(layer_number: int) const`
- `RID get_physics_rid() const`
- `Vector3 get_point_transform(point_index: int)`
- `bool is_point_pinned(point_index: int) const`
- `void remove_collision_exception_with(body: Node)`
- `void set_collision_layer_value(layer_number: int, value: bool)`
- `void set_collision_mask_value(layer_number: int, value: bool)`
- `void set_point_pinned(point_index: int, pinned: bool, attachment_path: NodePath = NodePath(""), insert_at: int = -1)`

### SpotLight3D
*Inherits: **Light3D < VisualInstance3D < Node3D < Node < Object***

A Spotlight is a type of Light3D node that emits lights in a specific direction, in the shape of a cone. The light is attenuated through the distance. This attenuation can be configured by changing the energy, radius and attenuation parameters of Light3D.

**Properties**
- `float light_specular` = `0.5 (overrides Light3D)`
- `float shadow_bias` = `0.03 (overrides Light3D)`
- `float shadow_normal_bias` = `1.0 (overrides Light3D)`
- `float spot_angle` = `45.0`
- `float spot_angle_attenuation` = `1.0`
- `float spot_attenuation` = `1.0`
- `float spot_range` = `5.0`

### SpringArm3D
*Inherits: **Node3D < Node < Object***

SpringArm3D casts a ray or a shape along its Z axis and moves all its direct children to the collision point, with an optional margin. This is useful for 3rd person cameras that move closer to the player when inside a tight space (you may need to exclude the player's collider from the SpringArm3D's collision check).

**Properties**
- `int collision_mask` = `1`
- `float margin` = `0.01`
- `Shape3D shape`
- `float spring_length` = `1.0`

**Methods**
- `void add_excluded_object(RID: RID)`
- `void clear_excluded_objects()`
- `float get_hit_length()`
- `bool remove_excluded_object(RID: RID)`

### StaticBody3D
*Inherits: **PhysicsBody3D < CollisionObject3D < Node3D < Node < Object** | Inherited by: AnimatableBody3D*

A static 3D physics body. It can't be moved by external forces or contacts, but can be moved manually by other means such as code, AnimationMixers (with AnimationMixer.callback_mode_process set to AnimationMixer.ANIMATION_CALLBACK_MODE_PROCESS_PHYSICS), and RemoteTransform3D.

**Properties**
- `Vector3 constant_angular_velocity` = `Vector3(0, 0, 0)`
- `Vector3 constant_linear_velocity` = `Vector3(0, 0, 0)`
- `PhysicsMaterial physics_material_override`

### VehicleBody3D
*Inherits: **RigidBody3D < PhysicsBody3D < CollisionObject3D < Node3D < Node < Object***

This physics body implements all the physics logic needed to simulate a car. It is based on the raycast vehicle system commonly found in physics engines. Aside from a CollisionShape3D for the main body of the vehicle, you must also add a VehicleWheel3D node for each wheel. You should also add a MeshInstance3D to this node for the 3D model of the vehicle, but this model should generally not include meshes for the wheels. You can control the vehicle by using the brake, engine_force, and steering properties. The position or orientation of this node shouldn't be changed directly.

**Properties**
- `float brake` = `0.0`
- `float engine_force` = `0.0`
- `float mass` = `40.0 (overrides RigidBody3D)`
- `float steering` = `0.0`

### VehicleWheel3D
*Inherits: **Node3D < Node < Object***

A node used as a child of a VehicleBody3D parent to simulate the behavior of one of its wheels. This node also acts as a collider to detect if the wheel is touching a surface.

**Properties**
- `float brake` = `0.0`
- `float damping_compression` = `0.83`
- `float damping_relaxation` = `0.88`
- `float engine_force` = `0.0`
- `PhysicsInterpolationMode physics_interpolation_mode` = `2 (overrides Node)`
- `float steering` = `0.0`
- `float suspension_max_force` = `6000.0`
- `float suspension_stiffness` = `5.88`
- `float suspension_travel` = `0.2`
- `bool use_as_steering` = `false`
- `bool use_as_traction` = `false`
- `float wheel_friction_slip` = `10.5`
- `float wheel_radius` = `0.5`
- `float wheel_rest_length` = `0.15`
- `float wheel_roll_influence` = `0.1`

**Methods**
- `Node3D get_contact_body() const`
- `Vector3 get_contact_normal() const`
- `Vector3 get_contact_point() const`
- `float get_rpm() const`
- `float get_skidinfo() const`
- `bool is_in_contact() const`

### VisualInstance3D
*Inherits: **Node3D < Node < Object** | Inherited by: Decal, FogVolume, GeometryInstance3D, GPUParticlesAttractor3D, GPUParticlesCollision3D, Light3D, ...*

The VisualInstance3D is used to connect a resource to a visual representation. All visual 3D nodes inherit from the VisualInstance3D. In general, you should not access the VisualInstance3D properties directly as they are accessed and managed by the nodes that inherit from VisualInstance3D. VisualInstance3D is the node representation of the RenderingServer instance.

**Properties**
- `int layers` = `1`
- `float sorting_offset` = `0.0`
- `bool sorting_use_aabb_center`

**Methods**
- `AABB _get_aabb() virtual const`
- `AABB get_aabb() const`
- `RID get_base() const`
- `RID get_instance() const`
- `bool get_layer_mask_value(layer_number: int) const`
- `void set_base(base: RID)`
- `void set_layer_mask_value(layer_number: int, value: bool)`

### VoxelGIData
*Inherits: **Resource < RefCounted < Object***

VoxelGIData contains baked voxel global illumination for use in a VoxelGI node. VoxelGIData also offers several properties to adjust the final appearance of the global illumination. These properties can be adjusted at run-time without having to bake the VoxelGI node again.

**Properties**
- `float bias` = `1.5`
- `float dynamic_range` = `2.0`
- `float energy` = `1.0`
- `bool interior` = `false`
- `float normal_bias` = `0.0`
- `float propagation` = `0.5`
- `bool use_two_bounces` = `true`

**Methods**
- `void allocate(to_cell_xform: Transform3D, aabb: AABB, octree_size: Vector3, octree_cells: PackedByteArray, data_cells: PackedByteArray, distance_field: PackedByteArray, level_counts: PackedInt32Array)`
- `AABB get_bounds() const`
- `PackedByteArray get_data_cells() const`
- `PackedInt32Array get_level_counts() const`
- `PackedByteArray get_octree_cells() const`
- `Vector3 get_octree_size() const`
- `Transform3D get_to_cell_xform() const`

### VoxelGI
*Inherits: **VisualInstance3D < Node3D < Node < Object***

VoxelGIs are used to provide high-quality real-time indirect light and reflections to scenes. They precompute the effect of objects that emit light and the effect of static geometry to simulate the behavior of complex light in real-time. VoxelGIs need to be baked before having a visible effect. However, once baked, dynamic objects will receive light from them. Furthermore, lights can be fully dynamic or baked.

**Properties**
- `CameraAttributes camera_attributes`
- `VoxelGIData data`
- `Vector3 size` = `Vector3(20, 20, 20)`
- `Subdiv subdiv` = `1`

**Methods**
- `void bake(from_node: Node = null, create_visual_debug: bool = false)`
- `void debug_bake()`

### WorldEnvironment
*Inherits: **Node < Object***

The WorldEnvironment node is used to configure the default Environment for the scene.

**Properties**
- `CameraAttributes camera_attributes`
- `Compositor compositor`
- `Environment environment`
