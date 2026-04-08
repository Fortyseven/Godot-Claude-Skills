# Godot 4 GDScript API Reference — Nodes 2D

> GDScript-only reference. 43 classes.

### AnimatableBody2D
*Inherits: **StaticBody2D < PhysicsBody2D < CollisionObject2D < Node2D < CanvasItem < Node < Object***

An animatable 2D physics body. It can't be moved by external forces or contacts, but can be moved manually by other means such as code, AnimationMixers (with AnimationMixer.callback_mode_process set to AnimationMixer.ANIMATION_CALLBACK_MODE_PROCESS_PHYSICS), and RemoteTransform2D.

**Properties**
- `bool sync_to_physics` = `true`

### AnimatedSprite2D
*Inherits: **Node2D < CanvasItem < Node < Object***

AnimatedSprite2D is similar to the Sprite2D node, except it carries multiple textures as animation frames. Animations are created using a SpriteFrames resource, which allows you to import image files (or a folder containing said files) to provide the animation frames for the sprite. The SpriteFrames resource can be configured in the editor via the SpriteFrames bottom panel.

**Properties**
- `StringName animation` = `&"default"`
- `String autoplay` = `""`
- `bool centered` = `true`
- `bool flip_h` = `false`
- `bool flip_v` = `false`
- `int frame` = `0`
- `float frame_progress` = `0.0`
- `Vector2 offset` = `Vector2(0, 0)`
- `float speed_scale` = `1.0`
- `SpriteFrames sprite_frames`

**Methods**
- `float get_playing_speed() const`
- `bool is_playing() const`
- `void pause()`
- `void play(name: StringName = &"", custom_speed: float = 1.0, from_end: bool = false)`
- `void play_backwards(name: StringName = &"")`
- `void set_frame_and_progress(frame: int, progress: float)`
- `void stop()`

**GDScript Examples**
```gdscript
var current_frame = animated_sprite.get_frame()
var current_progress = animated_sprite.get_frame_progress()
animated_sprite.play("walk_another_skin")
animated_sprite.set_frame_and_progress(current_frame, current_progress)
```

### CPUParticles2D
*Inherits: **Node2D < CanvasItem < Node < Object***

CPU-based 2D particle node used to create a variety of particle systems and effects.

**Properties**
- `int amount` = `8`
- `Curve angle_curve`
- `float angle_max` = `0.0`
- `float angle_min` = `0.0`
- `Curve angular_velocity_curve`
- `float angular_velocity_max` = `0.0`
- `float angular_velocity_min` = `0.0`
- `Curve anim_offset_curve`
- `float anim_offset_max` = `0.0`
- `float anim_offset_min` = `0.0`
- `Curve anim_speed_curve`
- `float anim_speed_max` = `0.0`
- `float anim_speed_min` = `0.0`
- `Color color` = `Color(1, 1, 1, 1)`
- `Gradient color_initial_ramp`
- `Gradient color_ramp`
- `Curve damping_curve`
- `float damping_max` = `0.0`
- `float damping_min` = `0.0`
- `Vector2 direction` = `Vector2(1, 0)`
- `DrawOrder draw_order` = `0`
- `PackedColorArray emission_colors`
- `PackedVector2Array emission_normals`
- `PackedVector2Array emission_points`
- `Vector2 emission_rect_extents`
- `float emission_ring_inner_radius`
- `float emission_ring_radius`
- `EmissionShape emission_shape` = `0`
- `float emission_sphere_radius`
- `bool emitting` = `true`

**Methods**
- `void convert_from_particles(particles: Node)`
- `Curve get_param_curve(param: Parameter) const`
- `float get_param_max(param: Parameter) const`
- `float get_param_min(param: Parameter) const`
- `bool get_particle_flag(particle_flag: ParticleFlags) const`
- `void request_particles_process(process_time: float)`
- `void restart(keep_seed: bool = false)`
- `void set_param_curve(param: Parameter, curve: Curve)`
- `void set_param_max(param: Parameter, value: float)`
- `void set_param_min(param: Parameter, value: float)`
- `void set_particle_flag(particle_flag: ParticleFlags, enable: bool)`

### Camera2D
*Inherits: **Node2D < CanvasItem < Node < Object***

Camera node for 2D scenes. It forces the screen (current layer) to scroll following this node. This makes it easier (and faster) to program scrollable scenes than manually changing the position of CanvasItem-based nodes.

**Properties**
- `AnchorMode anchor_mode` = `1`
- `Node custom_viewport`
- `float drag_bottom_margin` = `0.2`
- `bool drag_horizontal_enabled` = `false`
- `float drag_horizontal_offset` = `0.0`
- `float drag_left_margin` = `0.2`
- `float drag_right_margin` = `0.2`
- `float drag_top_margin` = `0.2`
- `bool drag_vertical_enabled` = `false`
- `float drag_vertical_offset` = `0.0`
- `bool editor_draw_drag_margin` = `false`
- `bool editor_draw_limits` = `false`
- `bool editor_draw_screen` = `true`
- `bool enabled` = `true`
- `bool ignore_rotation` = `true`
- `int limit_bottom` = `10000000`
- `bool limit_enabled` = `true`
- `int limit_left` = `-10000000`
- `int limit_right` = `10000000`
- `bool limit_smoothed` = `false`
- `int limit_top` = `-10000000`
- `Vector2 offset` = `Vector2(0, 0)`
- `bool position_smoothing_enabled` = `false`
- `float position_smoothing_speed` = `5.0`
- `Camera2DProcessCallback process_callback` = `1`
- `bool rotation_smoothing_enabled` = `false`
- `float rotation_smoothing_speed` = `5.0`
- `Vector2 zoom` = `Vector2(1, 1)`

**Methods**
- `void align()`
- `void force_update_scroll()`
- `float get_drag_margin(margin: Side) const`
- `int get_limit(margin: Side) const`
- `Vector2 get_screen_center_position() const`
- `float get_screen_rotation() const`
- `Vector2 get_target_position() const`
- `bool is_current() const`
- `void make_current()`
- `void reset_smoothing()`
- `void set_drag_margin(margin: Side, drag_margin: float)`
- `void set_limit(margin: Side, limit: int)`

### CanvasItemMaterial
*Inherits: **Material < Resource < RefCounted < Object***

CanvasItemMaterials provide a means of modifying the textures associated with a CanvasItem. They specialize in describing blend and lighting behaviors for textures. Use a ShaderMaterial to more fully customize a material's interactions with a CanvasItem.

**Properties**
- `BlendMode blend_mode` = `0`
- `LightMode light_mode` = `0`
- `int particles_anim_h_frames`
- `bool particles_anim_loop`
- `int particles_anim_v_frames`
- `bool particles_animation` = `false`

### CanvasItem
*Inherits: **Node < Object** | Inherited by: Control, Node2D*

Abstract base class for everything in 2D space. Canvas items are laid out in a tree; children inherit and extend their parent's transform. CanvasItem is extended by Control for GUI-related nodes, and by Node2D for 2D game objects.

**Properties**
- `ClipChildrenMode clip_children` = `0`
- `int light_mask` = `1`
- `Material material`
- `Color modulate` = `Color(1, 1, 1, 1)`
- `Color self_modulate` = `Color(1, 1, 1, 1)`
- `bool show_behind_parent` = `false`
- `TextureFilter texture_filter` = `0`
- `TextureRepeat texture_repeat` = `0`
- `bool top_level` = `false`
- `bool use_parent_material` = `false`
- `int visibility_layer` = `1`
- `bool visible` = `true`
- `bool y_sort_enabled` = `false`
- `bool z_as_relative` = `true`
- `int z_index` = `0`

**Methods**
- `void _draw() virtual`
- `void draw_animation_slice(animation_length: float, slice_begin: float, slice_end: float, offset: float = 0.0)`
- `void draw_arc(center: Vector2, radius: float, start_angle: float, end_angle: float, point_count: int, color: Color, width: float = -1.0, antialiased: bool = false)`
- `void draw_char(font: Font, pos: Vector2, char: String, font_size: int = 16, modulate: Color = Color(1, 1, 1, 1), oversampling: float = 0.0) const`
- `void draw_char_outline(font: Font, pos: Vector2, char: String, font_size: int = 16, size: int = -1, modulate: Color = Color(1, 1, 1, 1), oversampling: float = 0.0) const`
- `void draw_circle(position: Vector2, radius: float, color: Color, filled: bool = true, width: float = -1.0, antialiased: bool = false)`
- `void draw_colored_polygon(points: PackedVector2Array, color: Color, uvs: PackedVector2Array = PackedVector2Array(), texture: Texture2D = null)`
- `void draw_dashed_line(from: Vector2, to: Vector2, color: Color, width: float = -1.0, dash: float = 2.0, aligned: bool = true, antialiased: bool = false)`
- `void draw_ellipse(position: Vector2, major: float, minor: float, color: Color, filled: bool = true, width: float = -1.0, antialiased: bool = false)`
- `void draw_ellipse_arc(center: Vector2, major: float, minor: float, start_angle: float, end_angle: float, point_count: int, color: Color, width: float = -1.0, antialiased: bool = false)`
- `void draw_end_animation()`
- `void draw_lcd_texture_rect_region(texture: Texture2D, rect: Rect2, src_rect: Rect2, modulate: Color = Color(1, 1, 1, 1))`
- `void draw_line(from: Vector2, to: Vector2, color: Color, width: float = -1.0, antialiased: bool = false)`
- `void draw_mesh(mesh: Mesh, texture: Texture2D, transform: Transform2D = Transform2D(1, 0, 0, 1, 0, 0), modulate: Color = Color(1, 1, 1, 1))`
- `void draw_msdf_texture_rect_region(texture: Texture2D, rect: Rect2, src_rect: Rect2, modulate: Color = Color(1, 1, 1, 1), outline: float = 0.0, pixel_range: float = 4.0, scale: float = 1.0)`
- `void draw_multiline(points: PackedVector2Array, color: Color, width: float = -1.0, antialiased: bool = false)`
- `void draw_multiline_colors(points: PackedVector2Array, colors: PackedColorArray, width: float = -1.0, antialiased: bool = false)`
- `void draw_multiline_string(font: Font, pos: Vector2, text: String, alignment: HorizontalAlignment = 0, width: float = -1, font_size: int = 16, max_lines: int = -1, modulate: Color = Color(1, 1, 1, 1), brk_flags: BitField[LineBreakFlag] = 3, justification_flags: BitField[JustificationFlag] = 3, direction: Direction = 0, orientation: Orientation = 0, oversampling: float = 0.0) const`
- `void draw_multiline_string_outline(font: Font, pos: Vector2, text: String, alignment: HorizontalAlignment = 0, width: float = -1, font_size: int = 16, max_lines: int = -1, size: int = 1, modulate: Color = Color(1, 1, 1, 1), brk_flags: BitField[LineBreakFlag] = 3, justification_flags: BitField[JustificationFlag] = 3, direction: Direction = 0, orientation: Orientation = 0, oversampling: float = 0.0) const`
- `void draw_multimesh(multimesh: MultiMesh, texture: Texture2D)`
- `void draw_polygon(points: PackedVector2Array, colors: PackedColorArray, uvs: PackedVector2Array = PackedVector2Array(), texture: Texture2D = null)`
- `void draw_polyline(points: PackedVector2Array, color: Color, width: float = -1.0, antialiased: bool = false)`
- `void draw_polyline_colors(points: PackedVector2Array, colors: PackedColorArray, width: float = -1.0, antialiased: bool = false)`
- `void draw_primitive(points: PackedVector2Array, colors: PackedColorArray, uvs: PackedVector2Array, texture: Texture2D = null)`
- `void draw_rect(rect: Rect2, color: Color, filled: bool = true, width: float = -1.0, antialiased: bool = false)`
- `void draw_set_transform(position: Vector2, rotation: float = 0.0, scale: Vector2 = Vector2(1, 1))`
- `void draw_set_transform_matrix(xform: Transform2D)`
- `void draw_string(font: Font, pos: Vector2, text: String, alignment: HorizontalAlignment = 0, width: float = -1, font_size: int = 16, modulate: Color = Color(1, 1, 1, 1), justification_flags: BitField[JustificationFlag] = 3, direction: Direction = 0, orientation: Orientation = 0, oversampling: float = 0.0) const`
- `void draw_string_outline(font: Font, pos: Vector2, text: String, alignment: HorizontalAlignment = 0, width: float = -1, font_size: int = 16, size: int = 1, modulate: Color = Color(1, 1, 1, 1), justification_flags: BitField[JustificationFlag] = 3, direction: Direction = 0, orientation: Orientation = 0, oversampling: float = 0.0) const`
- `void draw_style_box(style_box: StyleBox, rect: Rect2)`
- `void draw_texture(texture: Texture2D, position: Vector2, modulate: Color = Color(1, 1, 1, 1))`
- `void draw_texture_rect(texture: Texture2D, rect: Rect2, tile: bool, modulate: Color = Color(1, 1, 1, 1), transpose: bool = false)`
- `void draw_texture_rect_region(texture: Texture2D, rect: Rect2, src_rect: Rect2, modulate: Color = Color(1, 1, 1, 1), transpose: bool = false, clip_uv: bool = true)`
- `void force_update_transform()`
- `RID get_canvas() const`
- `RID get_canvas_item() const`
- `CanvasLayer get_canvas_layer_node() const`
- `Transform2D get_canvas_transform() const`
- `Vector2 get_global_mouse_position() const`
- `Transform2D get_global_transform() const`

**GDScript Examples**
```gdscript
draw_string(ThemeDB.fallback_font, Vector2(64, 64), "Hello world", HORIZONTAL_ALIGNMENT_LEFT, -1, ThemeDB.fallback_font_size)
```
```gdscript
dst.r = texture.r * modulate.r * modulate.a + dst.r * (1.0 - texture.r * modulate.a);
dst.g = texture.g * modulate.g * modulate.a + dst.g * (1.0 - texture.g * modulate.a);
dst.b = texture.b * modulate.b * modulate.a + dst.b * (1.0 - texture.b * modulate.a);
dst.a = modulate.a + dst.a * (1.0 - modulate.a);
```

### CanvasLayer
*Inherits: **Node < Object** | Inherited by: ParallaxBackground*

CanvasItem-derived nodes that are direct or indirect children of a CanvasLayer will be drawn in that layer. The layer is a numeric index that defines the draw order. The default 2D scene renders with index 0, so a CanvasLayer with index -1 will be drawn below, and a CanvasLayer with index 1 will be drawn above. This order will hold regardless of the CanvasItem.z_index of the nodes within each layer.

**Properties**
- `Node custom_viewport`
- `bool follow_viewport_enabled` = `false`
- `float follow_viewport_scale` = `1.0`
- `int layer` = `1`
- `Vector2 offset` = `Vector2(0, 0)`
- `float rotation` = `0.0`
- `Vector2 scale` = `Vector2(1, 1)`
- `Transform2D transform` = `Transform2D(1, 0, 0, 1, 0, 0)`
- `bool visible` = `true`

**Methods**
- `RID get_canvas() const`
- `Transform2D get_final_transform() const`
- `void hide()`
- `void show()`

### CanvasModulate
*Inherits: **Node2D < CanvasItem < Node < Object***

CanvasModulate applies a color tint to all nodes on a canvas. Only one can be used to tint a canvas, but CanvasLayers can be used to render things independently.

**Properties**
- `Color color` = `Color(1, 1, 1, 1)`

### CharacterBody2D
*Inherits: **PhysicsBody2D < CollisionObject2D < Node2D < CanvasItem < Node < Object***

CharacterBody2D is a specialized class for physics bodies that are meant to be user-controlled. They are not affected by physics at all, but they affect other physics bodies in their path. They are mainly used to provide high-level API to move objects with wall and slope detection (move_and_slide() method) in addition to the general collision detection provided by PhysicsBody2D.move_and_collide(). This makes it useful for highly configurable physics bodies that must move in specific ways and collide with the world, as is often the case with user-controlled characters.

**Properties**
- `bool floor_block_on_wall` = `true`
- `bool floor_constant_speed` = `false`
- `float floor_max_angle` = `0.7853982`
- `float floor_snap_length` = `1.0`
- `bool floor_stop_on_slope` = `true`
- `int max_slides` = `4`
- `MotionMode motion_mode` = `0`
- `int platform_floor_layers` = `4294967295`
- `PlatformOnLeave platform_on_leave` = `0`
- `int platform_wall_layers` = `0`
- `float safe_margin` = `0.08`
- `bool slide_on_ceiling` = `true`
- `Vector2 up_direction` = `Vector2(0, -1)`
- `Vector2 velocity` = `Vector2(0, 0)`
- `float wall_min_slide_angle` = `0.2617994`

**Methods**
- `void apply_floor_snap()`
- `float get_floor_angle(up_direction: Vector2 = Vector2(0, -1)) const`
- `Vector2 get_floor_normal() const`
- `Vector2 get_last_motion() const`
- `KinematicCollision2D get_last_slide_collision()`
- `Vector2 get_platform_velocity() const`
- `Vector2 get_position_delta() const`
- `Vector2 get_real_velocity() const`
- `KinematicCollision2D get_slide_collision(slide_idx: int)`
- `int get_slide_collision_count() const`
- `Vector2 get_wall_normal() const`
- `bool is_on_ceiling() const`
- `bool is_on_ceiling_only() const`
- `bool is_on_floor() const`
- `bool is_on_floor_only() const`
- `bool is_on_wall() const`
- `bool is_on_wall_only() const`
- `bool move_and_slide()`

**GDScript Examples**
```gdscript
for i in get_slide_collision_count():
    var collision = get_slide_collision(i)
    print("Collided with: ", collision.get_collider().name)
```

### CollisionObject2D
*Inherits: **Node2D < CanvasItem < Node < Object** | Inherited by: Area2D, PhysicsBody2D*

Abstract base class for 2D physics objects. CollisionObject2D can hold any number of Shape2Ds for collision. Each shape must be assigned to a shape owner. Shape owners are not nodes and do not appear in the editor, but are accessible through code using the shape_owner_* methods.

**Properties**
- `int collision_layer` = `1`
- `int collision_mask` = `1`
- `float collision_priority` = `1.0`
- `DisableMode disable_mode` = `0`
- `bool input_pickable` = `true`

**Methods**
- `void _input_event(viewport: Viewport, event: InputEvent, shape_idx: int) virtual`
- `void _mouse_enter() virtual`
- `void _mouse_exit() virtual`
- `void _mouse_shape_enter(shape_idx: int) virtual`
- `void _mouse_shape_exit(shape_idx: int) virtual`
- `int create_shape_owner(owner: Object)`
- `bool get_collision_layer_value(layer_number: int) const`
- `bool get_collision_mask_value(layer_number: int) const`
- `RID get_rid() const`
- `float get_shape_owner_one_way_collision_margin(owner_id: int) const`
- `PackedInt32Array get_shape_owners()`
- `bool is_shape_owner_disabled(owner_id: int) const`
- `bool is_shape_owner_one_way_collision_enabled(owner_id: int) const`
- `void remove_shape_owner(owner_id: int)`
- `void set_collision_layer_value(layer_number: int, value: bool)`
- `void set_collision_mask_value(layer_number: int, value: bool)`
- `int shape_find_owner(shape_index: int) const`
- `void shape_owner_add_shape(owner_id: int, shape: Shape2D)`
- `void shape_owner_clear_shapes(owner_id: int)`
- `Object shape_owner_get_owner(owner_id: int) const`
- `Shape2D shape_owner_get_shape(owner_id: int, shape_id: int) const`
- `int shape_owner_get_shape_count(owner_id: int) const`
- `int shape_owner_get_shape_index(owner_id: int, shape_id: int) const`
- `Transform2D shape_owner_get_transform(owner_id: int) const`
- `void shape_owner_remove_shape(owner_id: int, shape_id: int)`
- `void shape_owner_set_disabled(owner_id: int, disabled: bool)`
- `void shape_owner_set_one_way_collision(owner_id: int, enable: bool)`
- `void shape_owner_set_one_way_collision_margin(owner_id: int, margin: float)`
- `void shape_owner_set_transform(owner_id: int, transform: Transform2D)`

### CollisionPolygon2D
*Inherits: **Node2D < CanvasItem < Node < Object***

A node that provides a polygon shape to a CollisionObject2D parent and allows it to be edited. The polygon can be concave or convex. This can give a detection shape to an Area2D, turn a PhysicsBody2D into a solid object, or give a hollow shape to a StaticBody2D.

**Properties**
- `BuildMode build_mode` = `0`
- `bool disabled` = `false`
- `bool one_way_collision` = `false`
- `float one_way_collision_margin` = `1.0`
- `PackedVector2Array polygon` = `PackedVector2Array()`

### CollisionShape2D
*Inherits: **Node2D < CanvasItem < Node < Object***

A node that provides a Shape2D to a CollisionObject2D parent and allows it to be edited. This can give a detection shape to an Area2D or turn a PhysicsBody2D into a solid object.

**Properties**
- `Color debug_color` = `Color(0, 0, 0, 0)`
- `bool disabled` = `false`
- `bool one_way_collision` = `false`
- `float one_way_collision_margin` = `1.0`
- `Shape2D shape`

### DampedSpringJoint2D
*Inherits: **Joint2D < Node2D < CanvasItem < Node < Object***

A physics joint that connects two 2D physics bodies with a spring-like force. This behaves like a spring that always wants to stretch to a given length.

**Properties**
- `float damping` = `1.0`
- `float length` = `50.0`
- `float rest_length` = `0.0`
- `float stiffness` = `20.0`

### GPUParticles2D
*Inherits: **Node2D < CanvasItem < Node < Object***

2D particle node used to create a variety of particle systems and effects. GPUParticles2D features an emitter that generates some number of particles at a given rate.

**Properties**
- `int amount` = `8`
- `float amount_ratio` = `1.0`
- `float collision_base_size` = `1.0`
- `DrawOrder draw_order` = `1`
- `bool emitting` = `true`
- `float explosiveness` = `0.0`
- `int fixed_fps` = `30`
- `bool fract_delta` = `true`
- `float interp_to_end` = `0.0`
- `bool interpolate` = `true`
- `float lifetime` = `1.0`
- `bool local_coords` = `false`
- `bool one_shot` = `false`
- `float preprocess` = `0.0`
- `Material process_material`
- `float randomness` = `0.0`
- `int seed` = `0`
- `float speed_scale` = `1.0`
- `NodePath sub_emitter` = `NodePath("")`
- `Texture2D texture`
- `bool trail_enabled` = `false`
- `float trail_lifetime` = `0.3`
- `int trail_section_subdivisions` = `4`
- `int trail_sections` = `8`
- `bool use_fixed_seed` = `false`
- `Rect2 visibility_rect` = `Rect2(-100, -100, 200, 200)`

**Methods**
- `Rect2 capture_rect() const`
- `void convert_from_particles(particles: Node)`
- `void emit_particle(xform: Transform2D, velocity: Vector2, color: Color, custom: Color, flags: int)`
- `void request_particles_process(process_time: float)`
- `void restart(keep_seed: bool = false)`

### GrooveJoint2D
*Inherits: **Joint2D < Node2D < CanvasItem < Node < Object***

A physics joint that restricts the movement of two 2D physics bodies to a fixed axis. For example, a StaticBody2D representing a piston base can be attached to a RigidBody2D representing the piston head, moving up and down.

**Properties**
- `float initial_offset` = `25.0`
- `float length` = `50.0`

### Joint2D
*Inherits: **Node2D < CanvasItem < Node < Object** | Inherited by: DampedSpringJoint2D, GrooveJoint2D, PinJoint2D*

Abstract base class for all joints in 2D physics. 2D joints bind together two physics bodies (node_a and node_b) and apply a constraint.

**Properties**
- `float bias` = `0.0`
- `bool disable_collision` = `true`
- `NodePath node_a` = `NodePath("")`
- `NodePath node_b` = `NodePath("")`

**Methods**
- `RID get_rid() const`

### Light2D
*Inherits: **Node2D < CanvasItem < Node < Object** | Inherited by: DirectionalLight2D, PointLight2D*

Casts light in a 2D environment. A light is defined as a color, an energy value, a mode (see constants), and various other parameters (range and shadows-related).

**Properties**
- `BlendMode blend_mode` = `0`
- `Color color` = `Color(1, 1, 1, 1)`
- `bool editor_only` = `false`
- `bool enabled` = `true`
- `float energy` = `1.0`
- `int range_item_cull_mask` = `1`
- `int range_layer_max` = `0`
- `int range_layer_min` = `0`
- `int range_z_max` = `1024`
- `int range_z_min` = `-1024`
- `Color shadow_color` = `Color(0, 0, 0, 0)`
- `bool shadow_enabled` = `false`
- `ShadowFilter shadow_filter` = `0`
- `float shadow_filter_smooth` = `0.0`
- `int shadow_item_cull_mask` = `1`

**Methods**
- `float get_height() const`
- `void set_height(height: float)`

### LightOccluder2D
*Inherits: **Node2D < CanvasItem < Node < Object***

Occludes light cast by a Light2D, casting shadows. The LightOccluder2D must be provided with an OccluderPolygon2D in order for the shadow to be computed.

**Properties**
- `OccluderPolygon2D occluder`
- `int occluder_light_mask` = `1`
- `bool sdf_collision` = `true`

### Line2D
*Inherits: **Node2D < CanvasItem < Node < Object***

This node draws a 2D polyline, i.e. a shape consisting of several points connected by segments. Line2D is not a mathematical polyline, i.e. the segments are not infinitely thin. It is intended for rendering and it can be colored and optionally textured.

**Properties**
- `bool antialiased` = `false`
- `LineCapMode begin_cap_mode` = `0`
- `bool closed` = `false`
- `Color default_color` = `Color(1, 1, 1, 1)`
- `LineCapMode end_cap_mode` = `0`
- `Gradient gradient`
- `LineJointMode joint_mode` = `0`
- `PackedVector2Array points` = `PackedVector2Array()`
- `int round_precision` = `8`
- `float sharp_limit` = `2.0`
- `Texture2D texture`
- `LineTextureMode texture_mode` = `0`
- `float width` = `10.0`
- `Curve width_curve`

**Methods**
- `void add_point(position: Vector2, index: int = -1)`
- `void clear_points()`
- `int get_point_count() const`
- `Vector2 get_point_position(index: int) const`
- `void remove_point(index: int)`
- `void set_point_position(index: int, position: Vector2)`

### Marker2D
*Inherits: **Node2D < CanvasItem < Node < Object***

Generic 2D position hint for editing. It's just like a plain Node2D, but it displays as a cross in the 2D editor at all times. You can set the cross' visual size by using the gizmo in the 2D editor while the node is selected.

**Properties**
- `float gizmo_extents` = `10.0`

### MeshInstance2D
*Inherits: **Node2D < CanvasItem < Node < Object***

Node used for displaying a Mesh in 2D. This can be faster to render compared to displaying a Sprite2D node with large transparent areas, especially if the node takes up a lot of space on screen at high viewport resolutions. This is because using a mesh designed to fit the sprite's opaque areas will reduce GPU fill rate utilization (at the cost of increased vertex processing utilization).

**Properties**
- `Mesh mesh`
- `Texture2D texture`

### MultiMeshInstance2D
*Inherits: **Node2D < CanvasItem < Node < Object***

MultiMeshInstance2D is a specialized node to instance a MultiMesh resource in 2D. This can be faster to render compared to displaying many Sprite2D nodes with large transparent areas, especially if the nodes take up a lot of space on screen at high viewport resolutions. This is because using a mesh designed to fit the sprites' opaque areas will reduce GPU fill rate utilization (at the cost of increased vertex processing utilization).

**Properties**
- `MultiMesh multimesh`
- `Texture2D texture`

### NavigationAgent2D
*Inherits: **Node < Object***

A 2D agent used to pathfind to a position while avoiding static and dynamic obstacles. The calculation can be used by the parent node to dynamically move it along the path. Requires navigation data to work correctly.

**Properties**
- `bool avoidance_enabled` = `false`
- `int avoidance_layers` = `1`
- `int avoidance_mask` = `1`
- `float avoidance_priority` = `1.0`
- `bool debug_enabled` = `false`
- `Color debug_path_custom_color` = `Color(1, 1, 1, 1)`
- `float debug_path_custom_line_width` = `-1.0`
- `float debug_path_custom_point_size` = `4.0`
- `bool debug_use_custom` = `false`
- `int max_neighbors` = `10`
- `float max_speed` = `100.0`
- `int navigation_layers` = `1`
- `float neighbor_distance` = `500.0`
- `float path_desired_distance` = `20.0`
- `float path_max_distance` = `100.0`
- `BitField[PathMetadataFlags] path_metadata_flags` = `7`
- `PathPostProcessing path_postprocessing` = `0`
- `float path_return_max_length` = `0.0`
- `float path_return_max_radius` = `0.0`
- `float path_search_max_distance` = `0.0`
- `int path_search_max_polygons` = `4096`
- `PathfindingAlgorithm pathfinding_algorithm` = `0`
- `float radius` = `10.0`
- `float simplify_epsilon` = `0.0`
- `bool simplify_path` = `false`
- `float target_desired_distance` = `10.0`
- `Vector2 target_position` = `Vector2(0, 0)`
- `float time_horizon_agents` = `1.0`
- `float time_horizon_obstacles` = `0.0`
- `Vector2 velocity` = `Vector2(0, 0)`

**Methods**
- `float distance_to_target() const`
- `bool get_avoidance_layer_value(layer_number: int) const`
- `bool get_avoidance_mask_value(mask_number: int) const`
- `PackedVector2Array get_current_navigation_path() const`
- `int get_current_navigation_path_index() const`
- `NavigationPathQueryResult2D get_current_navigation_result() const`
- `Vector2 get_final_position()`
- `bool get_navigation_layer_value(layer_number: int) const`
- `RID get_navigation_map() const`
- `Vector2 get_next_path_position()`
- `float get_path_length() const`
- `RID get_rid() const`
- `bool is_navigation_finished()`
- `bool is_target_reachable()`
- `bool is_target_reached() const`
- `void set_avoidance_layer_value(layer_number: int, value: bool)`
- `void set_avoidance_mask_value(mask_number: int, value: bool)`
- `void set_navigation_layer_value(layer_number: int, value: bool)`
- `void set_navigation_map(navigation_map: RID)`
- `void set_velocity_forced(velocity: Vector2)`

### NavigationLink2D
*Inherits: **Node2D < CanvasItem < Node < Object***

A link between two positions on NavigationRegion2Ds that agents can be routed through. These positions can be on the same NavigationRegion2D or on two different ones. Links are useful to express navigation methods other than traveling along the surface of the navigation polygon, such as ziplines, teleporters, or gaps that can be jumped across.

**Properties**
- `bool bidirectional` = `true`
- `bool enabled` = `true`
- `Vector2 end_position` = `Vector2(0, 0)`
- `float enter_cost` = `0.0`
- `int navigation_layers` = `1`
- `Vector2 start_position` = `Vector2(0, 0)`
- `float travel_cost` = `1.0`

**Methods**
- `Vector2 get_global_end_position() const`
- `Vector2 get_global_start_position() const`
- `bool get_navigation_layer_value(layer_number: int) const`
- `RID get_navigation_map() const`
- `RID get_rid() const`
- `void set_global_end_position(position: Vector2)`
- `void set_global_start_position(position: Vector2)`
- `void set_navigation_layer_value(layer_number: int, value: bool)`
- `void set_navigation_map(navigation_map: RID)`

### NavigationObstacle2D
*Inherits: **Node2D < CanvasItem < Node < Object***

An obstacle needs a navigation map and outline vertices defined to work correctly. The outlines can not cross or overlap.

**Properties**
- `bool affect_navigation_mesh` = `false`
- `bool avoidance_enabled` = `true`
- `int avoidance_layers` = `1`
- `bool carve_navigation_mesh` = `false`
- `float radius` = `0.0`
- `Vector2 velocity` = `Vector2(0, 0)`
- `PackedVector2Array vertices` = `PackedVector2Array()`

**Methods**
- `bool get_avoidance_layer_value(layer_number: int) const`
- `RID get_navigation_map() const`
- `RID get_rid() const`
- `void set_avoidance_layer_value(layer_number: int, value: bool)`
- `void set_navigation_map(navigation_map: RID)`

### NavigationRegion2D
*Inherits: **Node2D < CanvasItem < Node < Object***

A traversable 2D region based on a NavigationPolygon that NavigationAgent2Ds can use for pathfinding.

**Properties**
- `bool enabled` = `true`
- `float enter_cost` = `0.0`
- `int navigation_layers` = `1`
- `NavigationPolygon navigation_polygon`
- `float travel_cost` = `1.0`
- `bool use_edge_connections` = `true`

**Methods**
- `void bake_navigation_polygon(on_thread: bool = true)`
- `Rect2 get_bounds() const`
- `bool get_navigation_layer_value(layer_number: int) const`
- `RID get_navigation_map() const`
- `RID get_region_rid() const`
- `RID get_rid() const`
- `bool is_baking() const`
- `void set_navigation_layer_value(layer_number: int, value: bool)`
- `void set_navigation_map(navigation_map: RID)`

### Node2D
*Inherits: **CanvasItem < Node < Object** | Inherited by: AnimatedSprite2D, AudioListener2D, AudioStreamPlayer2D, BackBufferCopy, Bone2D, Camera2D, ...*

A 2D game object, with a transform (position, rotation, and scale). All 2D nodes, including physics objects and sprites, inherit from Node2D. Use Node2D as a parent node to move, scale and rotate children in a 2D project. Also gives control of the node's render order.

**Properties**
- `Vector2 global_position`
- `float global_rotation`
- `float global_rotation_degrees`
- `Vector2 global_scale`
- `float global_skew`
- `Transform2D global_transform`
- `Vector2 position` = `Vector2(0, 0)`
- `float rotation` = `0.0`
- `float rotation_degrees`
- `Vector2 scale` = `Vector2(1, 1)`
- `float skew` = `0.0`
- `Transform2D transform`

**Methods**
- `void apply_scale(ratio: Vector2)`
- `float get_angle_to(point: Vector2) const`
- `Transform2D get_relative_transform_to_parent(parent: Node) const`
- `void global_translate(offset: Vector2)`
- `void look_at(point: Vector2)`
- `void move_local_x(delta: float, scaled: bool = false)`
- `void move_local_y(delta: float, scaled: bool = false)`
- `void rotate(radians: float)`
- `Vector2 to_global(local_point: Vector2) const`
- `Vector2 to_local(global_point: Vector2) const`
- `void translate(offset: Vector2)`

### Path2D
*Inherits: **Node2D < CanvasItem < Node < Object***

Can have PathFollow2D child nodes moving along the Curve2D. See PathFollow2D for more information on usage.

**Properties**
- `Curve2D curve`

### PathFollow2D
*Inherits: **Node2D < CanvasItem < Node < Object***

This node takes its parent Path2D, and returns the coordinates of a point within it, given a distance from the first vertex.

**Properties**
- `bool cubic_interp` = `true`
- `float h_offset` = `0.0`
- `bool loop` = `true`
- `float progress` = `0.0`
- `float progress_ratio` = `0.0`
- `bool rotates` = `true`
- `float v_offset` = `0.0`

### PinJoint2D
*Inherits: **Joint2D < Node2D < CanvasItem < Node < Object***

A physics joint that attaches two 2D physics bodies at a single point, allowing them to freely rotate. For example, a RigidBody2D can be attached to a StaticBody2D to create a pendulum or a seesaw.

**Properties**
- `bool angular_limit_enabled` = `false`
- `float angular_limit_lower` = `0.0`
- `float angular_limit_upper` = `0.0`
- `bool motor_enabled` = `false`
- `float motor_target_velocity` = `0.0`
- `float softness` = `0.0`

### Polygon2D
*Inherits: **Node2D < CanvasItem < Node < Object***

A Polygon2D is defined by a set of points. Each point is connected to the next, with the final point being connected to the first, resulting in a closed polygon. Polygon2Ds can be filled with color (solid or gradient) or filled with a given texture.

**Properties**
- `bool antialiased` = `false`
- `Color color` = `Color(1, 1, 1, 1)`
- `int internal_vertex_count` = `0`
- `float invert_border` = `100.0`
- `bool invert_enabled` = `false`
- `Vector2 offset` = `Vector2(0, 0)`
- `PackedVector2Array polygon` = `PackedVector2Array()`
- `Array polygons` = `[]`
- `NodePath skeleton` = `NodePath("")`
- `Texture2D texture`
- `Vector2 texture_offset` = `Vector2(0, 0)`
- `float texture_rotation` = `0.0`
- `Vector2 texture_scale` = `Vector2(1, 1)`
- `PackedVector2Array uv` = `PackedVector2Array()`
- `PackedColorArray vertex_colors` = `PackedColorArray()`

**Methods**
- `void add_bone(path: NodePath, weights: PackedFloat32Array)`
- `void clear_bones()`
- `void erase_bone(index: int)`
- `int get_bone_count() const`
- `NodePath get_bone_path(index: int) const`
- `PackedFloat32Array get_bone_weights(index: int) const`
- `void set_bone_path(index: int, path: NodePath)`
- `void set_bone_weights(index: int, weights: PackedFloat32Array)`

### RayCast2D
*Inherits: **Node2D < CanvasItem < Node < Object***

A raycast represents a ray from its origin to its target_position that finds the closest object along its path, if it intersects any.

**Properties**
- `bool collide_with_areas` = `false`
- `bool collide_with_bodies` = `true`
- `int collision_mask` = `1`
- `bool enabled` = `true`
- `bool exclude_parent` = `true`
- `bool hit_from_inside` = `false`
- `Vector2 target_position` = `Vector2(0, 50)`

**Methods**
- `void add_exception(node: CollisionObject2D)`
- `void add_exception_rid(rid: RID)`
- `void clear_exceptions()`
- `void force_raycast_update()`
- `Object get_collider() const`
- `RID get_collider_rid() const`
- `int get_collider_shape() const`
- `bool get_collision_mask_value(layer_number: int) const`
- `Vector2 get_collision_normal() const`
- `Vector2 get_collision_point() const`
- `bool is_colliding() const`
- `void remove_exception(node: CollisionObject2D)`
- `void remove_exception_rid(rid: RID)`
- `void set_collision_mask_value(layer_number: int, value: bool)`

**GDScript Examples**
```gdscript
var target = get_collider() # A CollisionObject2D.
var shape_id = get_collider_shape() # The shape index in the collider.
var owner_id = target.shape_find_owner(shape_id) # The owner ID in the collider.
var shape = target.shape_owner_get_owner(owner_id)
```

### RemoteTransform2D
*Inherits: **Node2D < CanvasItem < Node < Object***

RemoteTransform2D pushes its own Transform2D to another Node2D derived node (called the remote node) in the scene.

**Properties**
- `NodePath remote_path` = `NodePath("")`
- `bool update_position` = `true`
- `bool update_rotation` = `true`
- `bool update_scale` = `true`
- `bool use_global_coordinates` = `true`

**Methods**
- `void force_update_cache()`

### RigidBody2D
*Inherits: **PhysicsBody2D < CollisionObject2D < Node2D < CanvasItem < Node < Object** | Inherited by: PhysicalBone2D*

RigidBody2D implements full 2D physics. It cannot be controlled directly, instead, you must apply forces to it (gravity, impulses, etc.), and the physics simulation will calculate the resulting movement, rotation, react to collisions, and affect other physics bodies in its path.

**Properties**
- `float angular_damp` = `0.0`
- `DampMode angular_damp_mode` = `0`
- `float angular_velocity` = `0.0`
- `bool can_sleep` = `true`
- `Vector2 center_of_mass` = `Vector2(0, 0)`
- `CenterOfMassMode center_of_mass_mode` = `0`
- `Vector2 constant_force` = `Vector2(0, 0)`
- `float constant_torque` = `0.0`
- `bool contact_monitor` = `false`
- `CCDMode continuous_cd` = `0`
- `bool custom_integrator` = `false`
- `bool freeze` = `false`
- `FreezeMode freeze_mode` = `0`
- `float gravity_scale` = `1.0`
- `float inertia` = `0.0`
- `float linear_damp` = `0.0`
- `DampMode linear_damp_mode` = `0`
- `Vector2 linear_velocity` = `Vector2(0, 0)`
- `bool lock_rotation` = `false`
- `float mass` = `1.0`
- `int max_contacts_reported` = `0`
- `PhysicsMaterial physics_material_override`
- `bool sleeping` = `false`

**Methods**
- `void _integrate_forces(state: PhysicsDirectBodyState2D) virtual`
- `void add_constant_central_force(force: Vector2)`
- `void add_constant_force(force: Vector2, position: Vector2 = Vector2(0, 0))`
- `void add_constant_torque(torque: float)`
- `void apply_central_force(force: Vector2)`
- `void apply_central_impulse(impulse: Vector2 = Vector2(0, 0))`
- `void apply_force(force: Vector2, position: Vector2 = Vector2(0, 0))`
- `void apply_impulse(impulse: Vector2, position: Vector2 = Vector2(0, 0))`
- `void apply_torque(torque: float)`
- `void apply_torque_impulse(torque: float)`
- `Array[Node2D] get_colliding_bodies() const`
- `int get_contact_count() const`
- `void set_axis_velocity(axis_velocity: Vector2)`

**GDScript Examples**
```gdscript
@onready var ball = $Ball

func get_ball_inertia():
    return 1.0 / PhysicsServer2D.body_get_direct_state(ball.get_rid()).inverse_inertia
```

### Skeleton2D
*Inherits: **Node2D < CanvasItem < Node < Object***

Skeleton2D parents a hierarchy of Bone2D nodes. It holds a reference to each Bone2D's rest pose and acts as a single point of access to its bones.

**Methods**
- `void execute_modifications(delta: float, execution_mode: int)`
- `Bone2D get_bone(idx: int)`
- `int get_bone_count() const`
- `Transform2D get_bone_local_pose_override(bone_idx: int)`
- `SkeletonModificationStack2D get_modification_stack() const`
- `RID get_skeleton() const`
- `void set_bone_local_pose_override(bone_idx: int, override_pose: Transform2D, strength: float, persistent: bool)`
- `void set_modification_stack(modification_stack: SkeletonModificationStack2D)`

### Sprite2D
*Inherits: **Node2D < CanvasItem < Node < Object***

A node that displays a 2D texture. The texture displayed can be a region from a larger atlas texture, or a frame from a sprite sheet animation.

**Properties**
- `bool centered` = `true`
- `bool flip_h` = `false`
- `bool flip_v` = `false`
- `int frame` = `0`
- `Vector2i frame_coords` = `Vector2i(0, 0)`
- `int hframes` = `1`
- `Vector2 offset` = `Vector2(0, 0)`
- `bool region_enabled` = `false`
- `bool region_filter_clip_enabled` = `false`
- `Rect2 region_rect` = `Rect2(0, 0, 0, 0)`
- `Texture2D texture`
- `int vframes` = `1`

**Methods**
- `Rect2 get_rect() const`
- `bool is_pixel_opaque(pos: Vector2) const`

**GDScript Examples**
```gdscript
func _input(event):
    if event is InputEventMouseButton and event.pressed and event.button_index == MOUSE_BUTTON_LEFT:
        if get_rect().has_point(to_local(event.position)):
            print("A click!")
```

### StaticBody2D
*Inherits: **PhysicsBody2D < CollisionObject2D < Node2D < CanvasItem < Node < Object** | Inherited by: AnimatableBody2D*

A static 2D physics body. It can't be moved by external forces or contacts, but can be moved manually by other means such as code, AnimationMixers (with AnimationMixer.callback_mode_process set to AnimationMixer.ANIMATION_CALLBACK_MODE_PROCESS_PHYSICS), and RemoteTransform2D.

**Properties**
- `float constant_angular_velocity` = `0.0`
- `Vector2 constant_linear_velocity` = `Vector2(0, 0)`
- `PhysicsMaterial physics_material_override`

### TileMapLayer
*Inherits: **Node2D < CanvasItem < Node < Object***

Node for 2D tile-based maps. A TileMapLayer uses a TileSet which contain a list of tiles which are used to create grid-based maps. Unlike the TileMap node, which is deprecated, TileMapLayer has only one layer of tiles. You can use several TileMapLayer to achieve the same result as a TileMap node.

**Properties**
- `bool collision_enabled` = `true`
- `DebugVisibilityMode collision_visibility_mode` = `0`
- `bool enabled` = `true`
- `bool navigation_enabled` = `true`
- `DebugVisibilityMode navigation_visibility_mode` = `0`
- `bool occlusion_enabled` = `true`
- `int physics_quadrant_size` = `16`
- `int rendering_quadrant_size` = `16`
- `PackedByteArray tile_map_data` = `PackedByteArray()`
- `TileSet tile_set`
- `bool use_kinematic_bodies` = `false`
- `bool x_draw_order_reversed` = `false`
- `int y_sort_origin` = `0`

**Methods**
- `void _tile_data_runtime_update(coords: Vector2i, tile_data: TileData) virtual`
- `void _update_cells(coords: Array[Vector2i], forced_cleanup: bool) virtual`
- `bool _use_tile_data_runtime_update(coords: Vector2i) virtual`
- `void clear()`
- `void erase_cell(coords: Vector2i)`
- `void fix_invalid_tiles()`
- `int get_cell_alternative_tile(coords: Vector2i) const`
- `Vector2i get_cell_atlas_coords(coords: Vector2i) const`
- `int get_cell_source_id(coords: Vector2i) const`
- `TileData get_cell_tile_data(coords: Vector2i) const`
- `Vector2i get_coords_for_body_rid(body: RID) const`
- `RID get_navigation_map() const`
- `Vector2i get_neighbor_cell(coords: Vector2i, neighbor: CellNeighbor) const`
- `TileMapPattern get_pattern(coords_array: Array[Vector2i])`
- `Array[Vector2i] get_surrounding_cells(coords: Vector2i)`
- `Array[Vector2i] get_used_cells() const`
- `Array[Vector2i] get_used_cells_by_id(source_id: int = -1, atlas_coords: Vector2i = Vector2i(-1, -1), alternative_tile: int = -1) const`
- `Rect2i get_used_rect() const`
- `bool has_body_rid(body: RID) const`
- `bool is_cell_flipped_h(coords: Vector2i) const`
- `bool is_cell_flipped_v(coords: Vector2i) const`
- `bool is_cell_transposed(coords: Vector2i) const`
- `Vector2i local_to_map(local_position: Vector2) const`
- `Vector2i map_pattern(position_in_tilemap: Vector2i, coords_in_pattern: Vector2i, pattern: TileMapPattern)`
- `Vector2 map_to_local(map_position: Vector2i) const`
- `void notify_runtime_tile_data_update()`
- `void set_cell(coords: Vector2i, source_id: int = -1, atlas_coords: Vector2i = Vector2i(-1, -1), alternative_tile: int = 0)`
- `void set_cells_terrain_connect(cells: Array[Vector2i], terrain_set: int, terrain: int, ignore_empty_terrains: bool = true)`
- `void set_cells_terrain_path(path: Array[Vector2i], terrain_set: int, terrain: int, ignore_empty_terrains: bool = true)`
- `void set_navigation_map(map: RID)`
- `void set_pattern(position: Vector2i, pattern: TileMapPattern)`
- `void update_internals()`

**GDScript Examples**
```gdscript
func get_clicked_tile_power():
    var clicked_cell = tile_map_layer.local_to_map(tile_map_layer.get_local_mouse_position())
    var data = tile_map_layer.get_cell_tile_data(clicked_cell)
    if data:
        return data.get_custom_data("power")
    else:
        return 0
```

### TileMapPattern
*Inherits: **Resource < RefCounted < Object***

This resource holds a set of cells to help bulk manipulations of TileMap.

**Methods**
- `int get_cell_alternative_tile(coords: Vector2i) const`
- `Vector2i get_cell_atlas_coords(coords: Vector2i) const`
- `int get_cell_source_id(coords: Vector2i) const`
- `Vector2i get_size() const`
- `Array[Vector2i] get_used_cells() const`
- `bool has_cell(coords: Vector2i) const`
- `bool is_empty() const`
- `void remove_cell(coords: Vector2i, update_size: bool)`
- `void set_cell(coords: Vector2i, source_id: int = -1, atlas_coords: Vector2i = Vector2i(-1, -1), alternative_tile: int = -1)`
- `void set_size(size: Vector2i)`

### TileMap
*Inherits: **Node2D < CanvasItem < Node < Object***

Node for 2D tile-based maps. Tilemaps use a TileSet which contain a list of tiles which are used to create grid-based maps. A TileMap may have several layers, layouting tiles on top of each other.

**Properties**
- `bool collision_animatable` = `false`
- `VisibilityMode collision_visibility_mode` = `0`
- `VisibilityMode navigation_visibility_mode` = `0`
- `int rendering_quadrant_size` = `16`
- `TileSet tile_set`

**Methods**
- `void _tile_data_runtime_update(layer: int, coords: Vector2i, tile_data: TileData) virtual`
- `bool _use_tile_data_runtime_update(layer: int, coords: Vector2i) virtual`
- `void add_layer(to_position: int)`
- `void clear()`
- `void clear_layer(layer: int)`
- `void erase_cell(layer: int, coords: Vector2i)`
- `void fix_invalid_tiles()`
- `void force_update(layer: int = -1)`
- `int get_cell_alternative_tile(layer: int, coords: Vector2i, use_proxies: bool = false) const`
- `Vector2i get_cell_atlas_coords(layer: int, coords: Vector2i, use_proxies: bool = false) const`
- `int get_cell_source_id(layer: int, coords: Vector2i, use_proxies: bool = false) const`
- `TileData get_cell_tile_data(layer: int, coords: Vector2i, use_proxies: bool = false) const`
- `Vector2i get_coords_for_body_rid(body: RID)`
- `int get_layer_for_body_rid(body: RID)`
- `Color get_layer_modulate(layer: int) const`
- `String get_layer_name(layer: int) const`
- `RID get_layer_navigation_map(layer: int) const`
- `int get_layer_y_sort_origin(layer: int) const`
- `int get_layer_z_index(layer: int) const`
- `int get_layers_count() const`
- `RID get_navigation_map(layer: int) const`
- `Vector2i get_neighbor_cell(coords: Vector2i, neighbor: CellNeighbor) const`
- `TileMapPattern get_pattern(layer: int, coords_array: Array[Vector2i])`
- `Array[Vector2i] get_surrounding_cells(coords: Vector2i)`
- `Array[Vector2i] get_used_cells(layer: int) const`
- `Array[Vector2i] get_used_cells_by_id(layer: int, source_id: int = -1, atlas_coords: Vector2i = Vector2i(-1, -1), alternative_tile: int = -1) const`
- `Rect2i get_used_rect() const`
- `bool is_cell_flipped_h(layer: int, coords: Vector2i, use_proxies: bool = false) const`
- `bool is_cell_flipped_v(layer: int, coords: Vector2i, use_proxies: bool = false) const`
- `bool is_cell_transposed(layer: int, coords: Vector2i, use_proxies: bool = false) const`
- `bool is_layer_enabled(layer: int) const`
- `bool is_layer_navigation_enabled(layer: int) const`
- `bool is_layer_y_sort_enabled(layer: int) const`
- `Vector2i local_to_map(local_position: Vector2) const`
- `Vector2i map_pattern(position_in_tilemap: Vector2i, coords_in_pattern: Vector2i, pattern: TileMapPattern)`
- `Vector2 map_to_local(map_position: Vector2i) const`
- `void move_layer(layer: int, to_position: int)`
- `void notify_runtime_tile_data_update(layer: int = -1)`
- `void remove_layer(layer: int)`
- `void set_cell(layer: int, coords: Vector2i, source_id: int = -1, atlas_coords: Vector2i = Vector2i(-1, -1), alternative_tile: int = 0)`

**GDScript Examples**
```gdscript
func get_clicked_tile_power():
    var clicked_cell = tile_map.local_to_map(tile_map.get_local_mouse_position())
    var data = tile_map.get_cell_tile_data(0, clicked_cell)
    if data:
        return data.get_custom_data("power")
    else:
        return 0
```

### TouchScreenButton
*Inherits: **Node2D < CanvasItem < Node < Object***

TouchScreenButton allows you to create on-screen buttons for touch devices. It's intended for gameplay use, such as a unit you have to touch to move. Unlike Button, TouchScreenButton supports multitouch out of the box. Several TouchScreenButtons can be pressed at the same time with touch input.

**Properties**
- `String action` = `""`
- `BitMap bitmask`
- `bool passby_press` = `false`
- `Shape2D shape`
- `bool shape_centered` = `true`
- `bool shape_visible` = `true`
- `Texture2D texture_normal`
- `Texture2D texture_pressed`
- `VisibilityMode visibility_mode` = `0`

**Methods**
- `bool is_pressed() const`

### VisibleOnScreenEnabler2D
*Inherits: **VisibleOnScreenNotifier2D < Node2D < CanvasItem < Node < Object***

VisibleOnScreenEnabler2D contains a rectangular region of 2D space and a target node. The target node will be automatically enabled (via its Node.process_mode property) when any part of this region becomes visible on the screen, and automatically disabled otherwise. This can for example be used to activate enemies only when the player approaches them.

**Properties**
- `EnableMode enable_mode` = `0`
- `NodePath enable_node_path` = `NodePath("..")`

### VisibleOnScreenNotifier2D
*Inherits: **Node2D < CanvasItem < Node < Object** | Inherited by: VisibleOnScreenEnabler2D*

VisibleOnScreenNotifier2D represents a rectangular region of 2D space. When any part of this region becomes visible on screen or in a viewport, it will emit a screen_entered signal, and likewise it will emit a screen_exited signal when no part of it remains visible.

**Properties**
- `Rect2 rect` = `Rect2(-10, -10, 20, 20)`
- `bool show_rect` = `true`

**Methods**
- `bool is_on_screen() const`
