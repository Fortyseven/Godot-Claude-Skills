# Godot 4 GDScript API Reference — Physics

> GDScript-only reference. 40 classes.

### Area2D
*Inherits: **CollisionObject2D < Node2D < CanvasItem < Node < Object***

Area2D is a region of 2D space defined by one or multiple CollisionShape2D or CollisionPolygon2D child nodes. It detects when other CollisionObject2Ds enter or exit it, and it also keeps track of which collision objects haven't exited it yet (i.e. which one are overlapping it).

**Properties**
- `float angular_damp` = `1.0`
- `SpaceOverride angular_damp_space_override` = `0`
- `StringName audio_bus_name` = `&"Master"`
- `bool audio_bus_override` = `false`
- `float gravity` = `980.0`
- `Vector2 gravity_direction` = `Vector2(0, 1)`
- `bool gravity_point` = `false`
- `Vector2 gravity_point_center` = `Vector2(0, 1)`
- `float gravity_point_unit_distance` = `0.0`
- `SpaceOverride gravity_space_override` = `0`
- `float linear_damp` = `0.1`
- `SpaceOverride linear_damp_space_override` = `0`
- `bool monitorable` = `true`
- `bool monitoring` = `true`
- `int priority` = `0`

**Methods**
- `Array[Area2D] get_overlapping_areas() const`
- `Array[Node2D] get_overlapping_bodies() const`
- `bool has_overlapping_areas() const`
- `bool has_overlapping_bodies() const`
- `bool overlaps_area(area: Node) const`
- `bool overlaps_body(body: Node) const`

**GDScript Examples**
```gdscript
var other_shape_owner = area.shape_find_owner(area_shape_index)
var other_shape_node = area.shape_owner_get_owner(other_shape_owner)

var local_shape_owner = shape_find_owner(local_shape_index)
var local_shape_node = shape_owner_get_owner(local_shape_owner)
```
```gdscript
var body_shape_owner = body.shape_find_owner(body_shape_index)
var body_shape_node = body.shape_owner_get_owner(body_shape_owner)

var local_shape_owner = shape_find_owner(local_shape_index)
var local_shape_node = shape_owner_get_owner(local_shape_owner)
```

### Area3D
*Inherits: **CollisionObject3D < Node3D < Node < Object***

Area3D is a region of 3D space defined by one or multiple CollisionShape3D or CollisionPolygon3D child nodes. It detects when other CollisionObject3Ds enter or exit it, and it also keeps track of which collision objects haven't exited it yet (i.e. which one are overlapping it).

**Properties**
- `float angular_damp` = `0.1`
- `SpaceOverride angular_damp_space_override` = `0`
- `StringName audio_bus_name` = `&"Master"`
- `bool audio_bus_override` = `false`
- `float gravity` = `9.8`
- `Vector3 gravity_direction` = `Vector3(0, -1, 0)`
- `bool gravity_point` = `false`
- `Vector3 gravity_point_center` = `Vector3(0, -1, 0)`
- `float gravity_point_unit_distance` = `0.0`
- `SpaceOverride gravity_space_override` = `0`
- `float linear_damp` = `0.1`
- `SpaceOverride linear_damp_space_override` = `0`
- `bool monitorable` = `true`
- `bool monitoring` = `true`
- `int priority` = `0`
- `float reverb_bus_amount` = `0.0`
- `bool reverb_bus_enabled` = `false`
- `StringName reverb_bus_name` = `&"Master"`
- `float reverb_bus_uniformity` = `0.0`
- `float wind_attenuation_factor` = `0.0`
- `float wind_force_magnitude` = `0.0`
- `NodePath wind_source_path` = `NodePath("")`

**Methods**
- `Array[Area3D] get_overlapping_areas() const`
- `Array[Node3D] get_overlapping_bodies() const`
- `bool has_overlapping_areas() const`
- `bool has_overlapping_bodies() const`
- `bool overlaps_area(area: Node) const`
- `bool overlaps_body(body: Node) const`

**GDScript Examples**
```gdscript
var other_shape_owner = area.shape_find_owner(area_shape_index)
var other_shape_node = area.shape_owner_get_owner(other_shape_owner)

var local_shape_owner = shape_find_owner(local_shape_index)
var local_shape_node = shape_owner_get_owner(local_shape_owner)
```
```gdscript
var body_shape_owner = body.shape_find_owner(body_shape_index)
var body_shape_node = body.shape_owner_get_owner(body_shape_owner)

var local_shape_owner = shape_find_owner(local_shape_index)
var local_shape_node = shape_owner_get_owner(local_shape_owner)
```

### CollisionPolygon3D
*Inherits: **Node3D < Node < Object***

A node that provides a thickened polygon shape (a prism) to a CollisionObject3D parent and allows it to be edited. The polygon can be concave or convex. This can give a detection shape to an Area3D or turn a PhysicsBody3D into a solid object.

**Properties**
- `Color debug_color` = `Color(0, 0, 0, 0)`
- `bool debug_fill` = `true`
- `float depth` = `1.0`
- `bool disabled` = `false`
- `float margin` = `0.04`
- `PackedVector2Array polygon` = `PackedVector2Array()`

### CollisionShape3D
*Inherits: **Node3D < Node < Object***

A node that provides a Shape3D to a CollisionObject3D parent and allows it to be edited. This can give a detection shape to an Area3D or turn a PhysicsBody3D into a solid object.

**Properties**
- `Color debug_color` = `Color(0, 0, 0, 0)`
- `bool debug_fill` = `true`
- `bool disabled` = `false`
- `Shape3D shape`

**Methods**
- `void make_convex_from_siblings()`
- `void resource_changed(resource: Resource)`

### ConeTwistJoint3D
*Inherits: **Joint3D < Node3D < Node < Object***

A physics joint that connects two 3D physics bodies in a way that simulates a ball-and-socket joint. The twist axis is initiated as the X axis of the ConeTwistJoint3D. Once the physics bodies swing, the twist axis is calculated as the middle of the X axes of the joint in the local space of the two physics bodies. Useful for limbs like shoulders and hips, lamps hanging off a ceiling, etc.

**Properties**
- `float bias` = `0.3`
- `float relaxation` = `1.0`
- `float softness` = `0.8`
- `float swing_span` = `0.7853982`
- `float twist_span` = `3.1415927`

**Methods**
- `float get_param(param: Param) const`
- `void set_param(param: Param, value: float)`

### Generic6DOFJoint3D
*Inherits: **Joint3D < Node3D < Node < Object***

The Generic6DOFJoint3D (6 Degrees Of Freedom) joint allows for implementing custom types of joints by locking the rotation and translation of certain axes.

**Properties**
- `float angular_limit_x/damping` = `1.0`
- `bool angular_limit_x/enabled` = `true`
- `float angular_limit_x/erp` = `0.5`
- `float angular_limit_x/force_limit` = `0.0`
- `float angular_limit_x/lower_angle` = `0.0`
- `float angular_limit_x/restitution` = `0.0`
- `float angular_limit_x/softness` = `0.5`
- `float angular_limit_x/upper_angle` = `0.0`
- `float angular_limit_y/damping` = `1.0`
- `bool angular_limit_y/enabled` = `true`
- `float angular_limit_y/erp` = `0.5`
- `float angular_limit_y/force_limit` = `0.0`
- `float angular_limit_y/lower_angle` = `0.0`
- `float angular_limit_y/restitution` = `0.0`
- `float angular_limit_y/softness` = `0.5`
- `float angular_limit_y/upper_angle` = `0.0`
- `float angular_limit_z/damping` = `1.0`
- `bool angular_limit_z/enabled` = `true`
- `float angular_limit_z/erp` = `0.5`
- `float angular_limit_z/force_limit` = `0.0`
- `float angular_limit_z/lower_angle` = `0.0`
- `float angular_limit_z/restitution` = `0.0`
- `float angular_limit_z/softness` = `0.5`
- `float angular_limit_z/upper_angle` = `0.0`
- `bool angular_motor_x/enabled` = `false`
- `float angular_motor_x/force_limit` = `300.0`
- `float angular_motor_x/target_velocity` = `0.0`
- `bool angular_motor_y/enabled` = `false`
- `float angular_motor_y/force_limit` = `300.0`
- `float angular_motor_y/target_velocity` = `0.0`

**Methods**
- `bool get_flag_x(flag: Flag) const`
- `bool get_flag_y(flag: Flag) const`
- `bool get_flag_z(flag: Flag) const`
- `float get_param_x(param: Param) const`
- `float get_param_y(param: Param) const`
- `float get_param_z(param: Param) const`
- `void set_flag_x(flag: Flag, value: bool)`
- `void set_flag_y(flag: Flag, value: bool)`
- `void set_flag_z(flag: Flag, value: bool)`
- `void set_param_x(param: Param, value: float)`
- `void set_param_y(param: Param, value: float)`
- `void set_param_z(param: Param, value: float)`

### HingeJoint3D
*Inherits: **Joint3D < Node3D < Node < Object***

A physics joint that restricts the rotation of a 3D physics body around an axis relative to another physics body. For example, Body A can be a StaticBody3D representing a door hinge that a RigidBody3D rotates around.

**Properties**
- `float angular_limit/bias` = `0.3`
- `bool angular_limit/enable` = `false`
- `float angular_limit/lower` = `-1.5707964`
- `float angular_limit/relaxation` = `1.0`
- `float angular_limit/softness` = `0.9`
- `float angular_limit/upper` = `1.5707964`
- `bool motor/enable` = `false`
- `float motor/max_impulse` = `1.0`
- `float motor/target_velocity` = `1.0`
- `float params/bias` = `0.3`

**Methods**
- `bool get_flag(flag: Flag) const`
- `float get_param(param: Param) const`
- `void set_flag(flag: Flag, enabled: bool)`
- `void set_param(param: Param, value: float)`

### Joint3D
*Inherits: **Node3D < Node < Object** | Inherited by: ConeTwistJoint3D, Generic6DOFJoint3D, HingeJoint3D, PinJoint3D, SliderJoint3D*

Abstract base class for all joints in 3D physics. 3D joints bind together two physics bodies (node_a and node_b) and apply a constraint. If only one body is defined, it is attached to a fixed StaticBody3D without collision shapes.

**Properties**
- `bool exclude_nodes_from_collision` = `true`
- `NodePath node_a` = `NodePath("")`
- `NodePath node_b` = `NodePath("")`
- `int solver_priority` = `1`

**Methods**
- `RID get_rid() const`

### PhysicsBody2D
*Inherits: **CollisionObject2D < Node2D < CanvasItem < Node < Object** | Inherited by: CharacterBody2D, RigidBody2D, StaticBody2D*

PhysicsBody2D is an abstract base class for 2D game objects affected by physics. All 2D physics bodies inherit from it.

**Properties**
- `bool input_pickable` = `false (overrides CollisionObject2D)`

**Methods**
- `void add_collision_exception_with(body: Node)`
- `Array[PhysicsBody2D] get_collision_exceptions()`
- `Vector2 get_gravity() const`
- `KinematicCollision2D move_and_collide(motion: Vector2, test_only: bool = false, safe_margin: float = 0.08, recovery_as_collision: bool = false)`
- `void remove_collision_exception_with(body: Node)`
- `bool test_move(from: Transform2D, motion: Vector2, collision: KinematicCollision2D = null, safe_margin: float = 0.08, recovery_as_collision: bool = false)`

### PhysicsBody3D
*Inherits: **CollisionObject3D < Node3D < Node < Object** | Inherited by: CharacterBody3D, PhysicalBone3D, RigidBody3D, StaticBody3D*

PhysicsBody3D is an abstract base class for 3D game objects affected by physics. All 3D physics bodies inherit from it.

**Properties**
- `bool axis_lock_angular_x` = `false`
- `bool axis_lock_angular_y` = `false`
- `bool axis_lock_angular_z` = `false`
- `bool axis_lock_linear_x` = `false`
- `bool axis_lock_linear_y` = `false`
- `bool axis_lock_linear_z` = `false`

**Methods**
- `void add_collision_exception_with(body: Node)`
- `bool get_axis_lock(axis: BodyAxis) const`
- `Array[PhysicsBody3D] get_collision_exceptions()`
- `Vector3 get_gravity() const`
- `KinematicCollision3D move_and_collide(motion: Vector3, test_only: bool = false, safe_margin: float = 0.001, recovery_as_collision: bool = false, max_collisions: int = 1)`
- `void remove_collision_exception_with(body: Node)`
- `void set_axis_lock(axis: BodyAxis, lock: bool)`
- `bool test_move(from: Transform3D, motion: Vector3, collision: KinematicCollision3D = null, safe_margin: float = 0.001, recovery_as_collision: bool = false, max_collisions: int = 1)`

### PhysicsDirectBodyState2DExtension
*Inherits: **PhysicsDirectBodyState2D < Object***

This class extends PhysicsDirectBodyState2D by providing additional virtual methods that can be overridden. When these methods are overridden, they will be called instead of the internal methods of the physics server.

**Methods**
- `void _add_constant_central_force(force: Vector2) virtual required`
- `void _add_constant_force(force: Vector2, position: Vector2) virtual required`
- `void _add_constant_torque(torque: float) virtual required`
- `void _apply_central_force(force: Vector2) virtual required`
- `void _apply_central_impulse(impulse: Vector2) virtual required`
- `void _apply_force(force: Vector2, position: Vector2) virtual required`
- `void _apply_impulse(impulse: Vector2, position: Vector2) virtual required`
- `void _apply_torque(torque: float) virtual required`
- `void _apply_torque_impulse(impulse: float) virtual required`
- `float _get_angular_velocity() virtual required const`
- `Vector2 _get_center_of_mass() virtual required const`
- `Vector2 _get_center_of_mass_local() virtual required const`
- `int _get_collision_layer() virtual required const`
- `int _get_collision_mask() virtual required const`
- `Vector2 _get_constant_force() virtual required const`
- `float _get_constant_torque() virtual required const`
- `RID _get_contact_collider(contact_idx: int) virtual required const`
- `int _get_contact_collider_id(contact_idx: int) virtual required const`
- `Object _get_contact_collider_object(contact_idx: int) virtual required const`
- `Vector2 _get_contact_collider_position(contact_idx: int) virtual required const`
- `int _get_contact_collider_shape(contact_idx: int) virtual required const`
- `Vector2 _get_contact_collider_velocity_at_position(contact_idx: int) virtual required const`
- `int _get_contact_count() virtual required const`
- `Vector2 _get_contact_impulse(contact_idx: int) virtual required const`
- `Vector2 _get_contact_local_normal(contact_idx: int) virtual required const`
- `Vector2 _get_contact_local_position(contact_idx: int) virtual required const`
- `int _get_contact_local_shape(contact_idx: int) virtual required const`
- `Vector2 _get_contact_local_velocity_at_position(contact_idx: int) virtual required const`
- `float _get_inverse_inertia() virtual required const`
- `float _get_inverse_mass() virtual required const`
- `Vector2 _get_linear_velocity() virtual required const`
- `PhysicsDirectSpaceState2D _get_space_state() virtual required`
- `float _get_step() virtual required const`
- `float _get_total_angular_damp() virtual required const`
- `Vector2 _get_total_gravity() virtual required const`
- `float _get_total_linear_damp() virtual required const`
- `Transform2D _get_transform() virtual required const`
- `Vector2 _get_velocity_at_local_position(local_position: Vector2) virtual required const`
- `void _integrate_forces() virtual required`
- `bool _is_sleeping() virtual required const`

### PhysicsDirectBodyState2D
*Inherits: **Object** | Inherited by: PhysicsDirectBodyState2DExtension*

Provides direct access to a physics body in the PhysicsServer2D, allowing safe changes to physics properties. This object is passed via the direct state callback of RigidBody2D, and is intended for changing the direct state of that body. See RigidBody2D._integrate_forces().

**Properties**
- `float angular_velocity`
- `Vector2 center_of_mass`
- `Vector2 center_of_mass_local`
- `int collision_layer`
- `int collision_mask`
- `float inverse_inertia`
- `float inverse_mass`
- `Vector2 linear_velocity`
- `bool sleeping`
- `float step`
- `float total_angular_damp`
- `Vector2 total_gravity`
- `float total_linear_damp`
- `Transform2D transform`

**Methods**
- `void add_constant_central_force(force: Vector2 = Vector2(0, 0))`
- `void add_constant_force(force: Vector2, position: Vector2 = Vector2(0, 0))`
- `void add_constant_torque(torque: float)`
- `void apply_central_force(force: Vector2 = Vector2(0, 0))`
- `void apply_central_impulse(impulse: Vector2)`
- `void apply_force(force: Vector2, position: Vector2 = Vector2(0, 0))`
- `void apply_impulse(impulse: Vector2, position: Vector2 = Vector2(0, 0))`
- `void apply_torque(torque: float)`
- `void apply_torque_impulse(impulse: float)`
- `Vector2 get_constant_force() const`
- `float get_constant_torque() const`
- `RID get_contact_collider(contact_idx: int) const`
- `int get_contact_collider_id(contact_idx: int) const`
- `Object get_contact_collider_object(contact_idx: int) const`
- `Vector2 get_contact_collider_position(contact_idx: int) const`
- `int get_contact_collider_shape(contact_idx: int) const`
- `Vector2 get_contact_collider_velocity_at_position(contact_idx: int) const`
- `int get_contact_count() const`
- `Vector2 get_contact_impulse(contact_idx: int) const`
- `Vector2 get_contact_local_normal(contact_idx: int) const`
- `Vector2 get_contact_local_position(contact_idx: int) const`
- `int get_contact_local_shape(contact_idx: int) const`
- `Vector2 get_contact_local_velocity_at_position(contact_idx: int) const`
- `PhysicsDirectSpaceState2D get_space_state()`
- `Vector2 get_velocity_at_local_position(local_position: Vector2) const`
- `void integrate_forces()`
- `void set_constant_force(force: Vector2)`
- `void set_constant_torque(torque: float)`

### PhysicsDirectBodyState3DExtension
*Inherits: **PhysicsDirectBodyState3D < Object***

This class extends PhysicsDirectBodyState3D by providing additional virtual methods that can be overridden. When these methods are overridden, they will be called instead of the internal methods of the physics server.

**Methods**
- `void _add_constant_central_force(force: Vector3) virtual required`
- `void _add_constant_force(force: Vector3, position: Vector3) virtual required`
- `void _add_constant_torque(torque: Vector3) virtual required`
- `void _apply_central_force(force: Vector3) virtual required`
- `void _apply_central_impulse(impulse: Vector3) virtual required`
- `void _apply_force(force: Vector3, position: Vector3) virtual required`
- `void _apply_impulse(impulse: Vector3, position: Vector3) virtual required`
- `void _apply_torque(torque: Vector3) virtual required`
- `void _apply_torque_impulse(impulse: Vector3) virtual required`
- `Vector3 _get_angular_velocity() virtual required const`
- `Vector3 _get_center_of_mass() virtual required const`
- `Vector3 _get_center_of_mass_local() virtual required const`
- `int _get_collision_layer() virtual required const`
- `int _get_collision_mask() virtual required const`
- `Vector3 _get_constant_force() virtual required const`
- `Vector3 _get_constant_torque() virtual required const`
- `RID _get_contact_collider(contact_idx: int) virtual required const`
- `int _get_contact_collider_id(contact_idx: int) virtual required const`
- `Object _get_contact_collider_object(contact_idx: int) virtual required const`
- `Vector3 _get_contact_collider_position(contact_idx: int) virtual required const`
- `int _get_contact_collider_shape(contact_idx: int) virtual required const`
- `Vector3 _get_contact_collider_velocity_at_position(contact_idx: int) virtual required const`
- `int _get_contact_count() virtual required const`
- `Vector3 _get_contact_impulse(contact_idx: int) virtual required const`
- `Vector3 _get_contact_local_normal(contact_idx: int) virtual required const`
- `Vector3 _get_contact_local_position(contact_idx: int) virtual required const`
- `int _get_contact_local_shape(contact_idx: int) virtual required const`
- `Vector3 _get_contact_local_velocity_at_position(contact_idx: int) virtual required const`
- `Vector3 _get_inverse_inertia() virtual required const`
- `Basis _get_inverse_inertia_tensor() virtual required const`
- `float _get_inverse_mass() virtual required const`
- `Vector3 _get_linear_velocity() virtual required const`
- `Basis _get_principal_inertia_axes() virtual required const`
- `PhysicsDirectSpaceState3D _get_space_state() virtual required`
- `float _get_step() virtual required const`
- `float _get_total_angular_damp() virtual required const`
- `Vector3 _get_total_gravity() virtual required const`
- `float _get_total_linear_damp() virtual required const`
- `Transform3D _get_transform() virtual required const`
- `Vector3 _get_velocity_at_local_position(local_position: Vector3) virtual required const`

### PhysicsDirectBodyState3D
*Inherits: **Object** | Inherited by: PhysicsDirectBodyState3DExtension*

Provides direct access to a physics body in the PhysicsServer3D, allowing safe changes to physics properties. This object is passed via the direct state callback of RigidBody3D, and is intended for changing the direct state of that body. See RigidBody3D._integrate_forces().

**Properties**
- `Vector3 angular_velocity`
- `Vector3 center_of_mass`
- `Vector3 center_of_mass_local`
- `int collision_layer`
- `int collision_mask`
- `Vector3 inverse_inertia`
- `Basis inverse_inertia_tensor`
- `float inverse_mass`
- `Vector3 linear_velocity`
- `Basis principal_inertia_axes`
- `bool sleeping`
- `float step`
- `float total_angular_damp`
- `Vector3 total_gravity`
- `float total_linear_damp`
- `Transform3D transform`

**Methods**
- `void add_constant_central_force(force: Vector3 = Vector3(0, 0, 0))`
- `void add_constant_force(force: Vector3, position: Vector3 = Vector3(0, 0, 0))`
- `void add_constant_torque(torque: Vector3)`
- `void apply_central_force(force: Vector3 = Vector3(0, 0, 0))`
- `void apply_central_impulse(impulse: Vector3 = Vector3(0, 0, 0))`
- `void apply_force(force: Vector3, position: Vector3 = Vector3(0, 0, 0))`
- `void apply_impulse(impulse: Vector3, position: Vector3 = Vector3(0, 0, 0))`
- `void apply_torque(torque: Vector3)`
- `void apply_torque_impulse(impulse: Vector3)`
- `Vector3 get_constant_force() const`
- `Vector3 get_constant_torque() const`
- `RID get_contact_collider(contact_idx: int) const`
- `int get_contact_collider_id(contact_idx: int) const`
- `Object get_contact_collider_object(contact_idx: int) const`
- `Vector3 get_contact_collider_position(contact_idx: int) const`
- `int get_contact_collider_shape(contact_idx: int) const`
- `Vector3 get_contact_collider_velocity_at_position(contact_idx: int) const`
- `int get_contact_count() const`
- `Vector3 get_contact_impulse(contact_idx: int) const`
- `Vector3 get_contact_local_normal(contact_idx: int) const`
- `Vector3 get_contact_local_position(contact_idx: int) const`
- `int get_contact_local_shape(contact_idx: int) const`
- `Vector3 get_contact_local_velocity_at_position(contact_idx: int) const`
- `PhysicsDirectSpaceState3D get_space_state()`
- `Vector3 get_velocity_at_local_position(local_position: Vector3) const`
- `void integrate_forces()`
- `void set_constant_force(force: Vector3)`
- `void set_constant_torque(torque: Vector3)`

### PhysicsDirectSpaceState2DExtension
*Inherits: **PhysicsDirectSpaceState2D < Object***

This class extends PhysicsDirectSpaceState2D by providing additional virtual methods that can be overridden. When these methods are overridden, they will be called instead of the internal methods of the physics server.

**Methods**
- `bool _cast_motion(shape_rid: RID, transform: Transform2D, motion: Vector2, margin: float, collision_mask: int, collide_with_bodies: bool, collide_with_areas: bool, closest_safe: float*, closest_unsafe: float*) virtual required`
- `bool _collide_shape(shape_rid: RID, transform: Transform2D, motion: Vector2, margin: float, collision_mask: int, collide_with_bodies: bool, collide_with_areas: bool, results: void*, max_results: int, result_count: int32_t*) virtual required`
- `int _intersect_point(position: Vector2, canvas_instance_id: int, collision_mask: int, collide_with_bodies: bool, collide_with_areas: bool, results: PhysicsServer2DExtensionShapeResult*, max_results: int) virtual required`
- `bool _intersect_ray(from: Vector2, to: Vector2, collision_mask: int, collide_with_bodies: bool, collide_with_areas: bool, hit_from_inside: bool, result: PhysicsServer2DExtensionRayResult*) virtual required`
- `int _intersect_shape(shape_rid: RID, transform: Transform2D, motion: Vector2, margin: float, collision_mask: int, collide_with_bodies: bool, collide_with_areas: bool, result: PhysicsServer2DExtensionShapeResult*, max_results: int) virtual required`
- `bool _rest_info(shape_rid: RID, transform: Transform2D, motion: Vector2, margin: float, collision_mask: int, collide_with_bodies: bool, collide_with_areas: bool, rest_info: PhysicsServer2DExtensionShapeRestInfo*) virtual required`
- `bool is_body_excluded_from_query(body: RID) const`

### PhysicsDirectSpaceState2D
*Inherits: **Object** | Inherited by: PhysicsDirectSpaceState2DExtension*

Provides direct access to a physics space in the PhysicsServer2D. It's used mainly to do queries against objects and areas residing in a given space.

**Methods**
- `PackedFloat32Array cast_motion(parameters: PhysicsShapeQueryParameters2D)`
- `Array[Vector2] collide_shape(parameters: PhysicsShapeQueryParameters2D, max_results: int = 32)`
- `Dictionary get_rest_info(parameters: PhysicsShapeQueryParameters2D)`
- `Array[Dictionary] intersect_point(parameters: PhysicsPointQueryParameters2D, max_results: int = 32)`
- `Dictionary intersect_ray(parameters: PhysicsRayQueryParameters2D)`
- `Array[Dictionary] intersect_shape(parameters: PhysicsShapeQueryParameters2D, max_results: int = 32)`

### PhysicsDirectSpaceState3DExtension
*Inherits: **PhysicsDirectSpaceState3D < Object***

This class extends PhysicsDirectSpaceState3D by providing additional virtual methods that can be overridden. When these methods are overridden, they will be called instead of the internal methods of the physics server.

**Methods**
- `bool _cast_motion(shape_rid: RID, transform: Transform3D, motion: Vector3, margin: float, collision_mask: int, collide_with_bodies: bool, collide_with_areas: bool, closest_safe: float*, closest_unsafe: float*, info: PhysicsServer3DExtensionShapeRestInfo*) virtual required`
- `bool _collide_shape(shape_rid: RID, transform: Transform3D, motion: Vector3, margin: float, collision_mask: int, collide_with_bodies: bool, collide_with_areas: bool, results: void*, max_results: int, result_count: int32_t*) virtual required`
- `Vector3 _get_closest_point_to_object_volume(object: RID, point: Vector3) virtual required const`
- `int _intersect_point(position: Vector3, collision_mask: int, collide_with_bodies: bool, collide_with_areas: bool, results: PhysicsServer3DExtensionShapeResult*, max_results: int) virtual required`
- `bool _intersect_ray(from: Vector3, to: Vector3, collision_mask: int, collide_with_bodies: bool, collide_with_areas: bool, hit_from_inside: bool, hit_back_faces: bool, pick_ray: bool, result: PhysicsServer3DExtensionRayResult*) virtual required`
- `int _intersect_shape(shape_rid: RID, transform: Transform3D, motion: Vector3, margin: float, collision_mask: int, collide_with_bodies: bool, collide_with_areas: bool, result_count: PhysicsServer3DExtensionShapeResult*, max_results: int) virtual required`
- `bool _rest_info(shape_rid: RID, transform: Transform3D, motion: Vector3, margin: float, collision_mask: int, collide_with_bodies: bool, collide_with_areas: bool, rest_info: PhysicsServer3DExtensionShapeRestInfo*) virtual required`
- `bool is_body_excluded_from_query(body: RID) const`

### PhysicsDirectSpaceState3D
*Inherits: **Object** | Inherited by: PhysicsDirectSpaceState3DExtension*

Provides direct access to a physics space in the PhysicsServer3D. It's used mainly to do queries against objects and areas residing in a given space.

**Methods**
- `PackedFloat32Array cast_motion(parameters: PhysicsShapeQueryParameters3D)`
- `Array[Vector3] collide_shape(parameters: PhysicsShapeQueryParameters3D, max_results: int = 32)`
- `Dictionary get_rest_info(parameters: PhysicsShapeQueryParameters3D)`
- `Array[Dictionary] intersect_point(parameters: PhysicsPointQueryParameters3D, max_results: int = 32)`
- `Dictionary intersect_ray(parameters: PhysicsRayQueryParameters3D)`
- `Array[Dictionary] intersect_shape(parameters: PhysicsShapeQueryParameters3D, max_results: int = 32)`

### PhysicsMaterial
*Inherits: **Resource < RefCounted < Object***

Holds physics-related properties of a surface, namely its roughness and bounciness. This class is used to apply these properties to a physics body.

**Properties**
- `bool absorbent` = `false`
- `float bounce` = `0.0`
- `float friction` = `1.0`
- `bool rough` = `false`

### PhysicsPointQueryParameters2D
*Inherits: **RefCounted < Object***

By changing various properties of this object, such as the point position, you can configure the parameters for PhysicsDirectSpaceState2D.intersect_point().

**Properties**
- `int canvas_instance_id` = `0`
- `bool collide_with_areas` = `false`
- `bool collide_with_bodies` = `true`
- `int collision_mask` = `4294967295`
- `Array[RID] exclude` = `[]`
- `Vector2 position` = `Vector2(0, 0)`

### PhysicsPointQueryParameters3D
*Inherits: **RefCounted < Object***

By changing various properties of this object, such as the point position, you can configure the parameters for PhysicsDirectSpaceState3D.intersect_point().

**Properties**
- `bool collide_with_areas` = `false`
- `bool collide_with_bodies` = `true`
- `int collision_mask` = `4294967295`
- `Array[RID] exclude` = `[]`
- `Vector3 position` = `Vector3(0, 0, 0)`

### PhysicsRayQueryParameters2D
*Inherits: **RefCounted < Object***

By changing various properties of this object, such as the ray position, you can configure the parameters for PhysicsDirectSpaceState2D.intersect_ray().

**Properties**
- `bool collide_with_areas` = `false`
- `bool collide_with_bodies` = `true`
- `int collision_mask` = `4294967295`
- `Array[RID] exclude` = `[]`
- `Vector2 from` = `Vector2(0, 0)`
- `bool hit_from_inside` = `false`
- `Vector2 to` = `Vector2(0, 0)`

**Methods**
- `PhysicsRayQueryParameters2D create(from: Vector2, to: Vector2, collision_mask: int = 4294967295, exclude: Array[RID] = []) static`

**GDScript Examples**
```gdscript
var query = PhysicsRayQueryParameters2D.create(global_position, global_position + Vector2(0, 100))
var collision = get_world_2d().direct_space_state.intersect_ray(query)
```

### PhysicsRayQueryParameters3D
*Inherits: **RefCounted < Object***

By changing various properties of this object, such as the ray position, you can configure the parameters for PhysicsDirectSpaceState3D.intersect_ray().

**Properties**
- `bool collide_with_areas` = `false`
- `bool collide_with_bodies` = `true`
- `int collision_mask` = `4294967295`
- `Array[RID] exclude` = `[]`
- `Vector3 from` = `Vector3(0, 0, 0)`
- `bool hit_back_faces` = `true`
- `bool hit_from_inside` = `false`
- `Vector3 to` = `Vector3(0, 0, 0)`

**Methods**
- `PhysicsRayQueryParameters3D create(from: Vector3, to: Vector3, collision_mask: int = 4294967295, exclude: Array[RID] = []) static`

**GDScript Examples**
```gdscript
var query = PhysicsRayQueryParameters3D.create(position, position + Vector3(0, -10, 0))
var collision = get_world_3d().direct_space_state.intersect_ray(query)
```

### PhysicsServer2DExtension
*Inherits: **PhysicsServer2D < Object***

This class extends PhysicsServer2D by providing additional virtual methods that can be overridden. When these methods are overridden, they will be called instead of the internal methods of the physics server.

**Methods**
- `void _area_add_shape(area: RID, shape: RID, transform: Transform2D, disabled: bool) virtual required`
- `void _area_attach_canvas_instance_id(area: RID, id: int) virtual required`
- `void _area_attach_object_instance_id(area: RID, id: int) virtual required`
- `void _area_clear_shapes(area: RID) virtual required`
- `RID _area_create() virtual required`
- `int _area_get_canvas_instance_id(area: RID) virtual required const`
- `int _area_get_collision_layer(area: RID) virtual required const`
- `int _area_get_collision_mask(area: RID) virtual required const`
- `int _area_get_object_instance_id(area: RID) virtual required const`
- `Variant _area_get_param(area: RID, param: AreaParameter) virtual required const`
- `RID _area_get_shape(area: RID, shape_idx: int) virtual required const`
- `int _area_get_shape_count(area: RID) virtual required const`
- `Transform2D _area_get_shape_transform(area: RID, shape_idx: int) virtual required const`
- `RID _area_get_space(area: RID) virtual required const`
- `Transform2D _area_get_transform(area: RID) virtual required const`
- `void _area_remove_shape(area: RID, shape_idx: int) virtual required`
- `void _area_set_area_monitor_callback(area: RID, callback: Callable) virtual required`
- `void _area_set_collision_layer(area: RID, layer: int) virtual required`
- `void _area_set_collision_mask(area: RID, mask: int) virtual required`
- `void _area_set_monitor_callback(area: RID, callback: Callable) virtual required`
- `void _area_set_monitorable(area: RID, monitorable: bool) virtual required`
- `void _area_set_param(area: RID, param: AreaParameter, value: Variant) virtual required`
- `void _area_set_pickable(area: RID, pickable: bool) virtual required`
- `void _area_set_shape(area: RID, shape_idx: int, shape: RID) virtual required`
- `void _area_set_shape_disabled(area: RID, shape_idx: int, disabled: bool) virtual required`
- `void _area_set_shape_transform(area: RID, shape_idx: int, transform: Transform2D) virtual required`
- `void _area_set_space(area: RID, space: RID) virtual required`
- `void _area_set_transform(area: RID, transform: Transform2D) virtual required`
- `void _body_add_collision_exception(body: RID, excepted_body: RID) virtual required`
- `void _body_add_constant_central_force(body: RID, force: Vector2) virtual required`
- `void _body_add_constant_force(body: RID, force: Vector2, position: Vector2) virtual required`
- `void _body_add_constant_torque(body: RID, torque: float) virtual required`
- `void _body_add_shape(body: RID, shape: RID, transform: Transform2D, disabled: bool) virtual required`
- `void _body_apply_central_force(body: RID, force: Vector2) virtual required`
- `void _body_apply_central_impulse(body: RID, impulse: Vector2) virtual required`
- `void _body_apply_force(body: RID, force: Vector2, position: Vector2) virtual required`
- `void _body_apply_impulse(body: RID, impulse: Vector2, position: Vector2) virtual required`
- `void _body_apply_torque(body: RID, torque: float) virtual required`
- `void _body_apply_torque_impulse(body: RID, impulse: float) virtual required`
- `void _body_attach_canvas_instance_id(body: RID, id: int) virtual required`

### PhysicsServer2DManager
*Inherits: **Object***

PhysicsServer2DManager is the API for registering PhysicsServer2D implementations and for setting the default implementation.

**Methods**
- `void register_server(name: String, create_callback: Callable)`
- `void set_default_server(name: String, priority: int)`

### PhysicsServer2D
*Inherits: **Object** | Inherited by: PhysicsServer2DExtension*

PhysicsServer2D is the server responsible for all 2D physics. It can directly create and manipulate all physics objects:

**Methods**
- `void area_add_shape(area: RID, shape: RID, transform: Transform2D = Transform2D(1, 0, 0, 1, 0, 0), disabled: bool = false)`
- `void area_attach_canvas_instance_id(area: RID, id: int)`
- `void area_attach_object_instance_id(area: RID, id: int)`
- `void area_clear_shapes(area: RID)`
- `RID area_create()`
- `int area_get_canvas_instance_id(area: RID) const`
- `int area_get_collision_layer(area: RID) const`
- `int area_get_collision_mask(area: RID) const`
- `int area_get_object_instance_id(area: RID) const`
- `Variant area_get_param(area: RID, param: AreaParameter) const`
- `RID area_get_shape(area: RID, shape_idx: int) const`
- `int area_get_shape_count(area: RID) const`
- `Transform2D area_get_shape_transform(area: RID, shape_idx: int) const`
- `RID area_get_space(area: RID) const`
- `Transform2D area_get_transform(area: RID) const`
- `void area_remove_shape(area: RID, shape_idx: int)`
- `void area_set_area_monitor_callback(area: RID, callback: Callable)`
- `void area_set_collision_layer(area: RID, layer: int)`
- `void area_set_collision_mask(area: RID, mask: int)`
- `void area_set_monitor_callback(area: RID, callback: Callable)`
- `void area_set_monitorable(area: RID, monitorable: bool)`
- `void area_set_param(area: RID, param: AreaParameter, value: Variant)`
- `void area_set_shape(area: RID, shape_idx: int, shape: RID)`
- `void area_set_shape_disabled(area: RID, shape_idx: int, disabled: bool)`
- `void area_set_shape_transform(area: RID, shape_idx: int, transform: Transform2D)`
- `void area_set_space(area: RID, space: RID)`
- `void area_set_transform(area: RID, transform: Transform2D)`
- `void body_add_collision_exception(body: RID, excepted_body: RID)`
- `void body_add_constant_central_force(body: RID, force: Vector2)`
- `void body_add_constant_force(body: RID, force: Vector2, position: Vector2 = Vector2(0, 0))`
- `void body_add_constant_torque(body: RID, torque: float)`
- `void body_add_shape(body: RID, shape: RID, transform: Transform2D = Transform2D(1, 0, 0, 1, 0, 0), disabled: bool = false)`
- `void body_apply_central_force(body: RID, force: Vector2)`
- `void body_apply_central_impulse(body: RID, impulse: Vector2)`
- `void body_apply_force(body: RID, force: Vector2, position: Vector2 = Vector2(0, 0))`
- `void body_apply_impulse(body: RID, impulse: Vector2, position: Vector2 = Vector2(0, 0))`
- `void body_apply_torque(body: RID, torque: float)`
- `void body_apply_torque_impulse(body: RID, impulse: float)`
- `void body_attach_canvas_instance_id(body: RID, id: int)`
- `void body_attach_object_instance_id(body: RID, id: int)`

### PhysicsServer3DExtension
*Inherits: **PhysicsServer3D < Object***

This class extends PhysicsServer3D by providing additional virtual methods that can be overridden. When these methods are overridden, they will be called instead of the internal methods of the physics server.

**Methods**
- `void _area_add_shape(area: RID, shape: RID, transform: Transform3D, disabled: bool) virtual required`
- `void _area_attach_object_instance_id(area: RID, id: int) virtual required`
- `void _area_clear_shapes(area: RID) virtual required`
- `RID _area_create() virtual required`
- `int _area_get_collision_layer(area: RID) virtual required const`
- `int _area_get_collision_mask(area: RID) virtual required const`
- `int _area_get_object_instance_id(area: RID) virtual required const`
- `Variant _area_get_param(area: RID, param: AreaParameter) virtual required const`
- `RID _area_get_shape(area: RID, shape_idx: int) virtual required const`
- `int _area_get_shape_count(area: RID) virtual required const`
- `Transform3D _area_get_shape_transform(area: RID, shape_idx: int) virtual required const`
- `RID _area_get_space(area: RID) virtual required const`
- `Transform3D _area_get_transform(area: RID) virtual required const`
- `void _area_remove_shape(area: RID, shape_idx: int) virtual required`
- `void _area_set_area_monitor_callback(area: RID, callback: Callable) virtual required`
- `void _area_set_collision_layer(area: RID, layer: int) virtual required`
- `void _area_set_collision_mask(area: RID, mask: int) virtual required`
- `void _area_set_monitor_callback(area: RID, callback: Callable) virtual required`
- `void _area_set_monitorable(area: RID, monitorable: bool) virtual required`
- `void _area_set_param(area: RID, param: AreaParameter, value: Variant) virtual required`
- `void _area_set_ray_pickable(area: RID, enable: bool) virtual required`
- `void _area_set_shape(area: RID, shape_idx: int, shape: RID) virtual required`
- `void _area_set_shape_disabled(area: RID, shape_idx: int, disabled: bool) virtual required`
- `void _area_set_shape_transform(area: RID, shape_idx: int, transform: Transform3D) virtual required`
- `void _area_set_space(area: RID, space: RID) virtual required`
- `void _area_set_transform(area: RID, transform: Transform3D) virtual required`
- `void _body_add_collision_exception(body: RID, excepted_body: RID) virtual required`
- `void _body_add_constant_central_force(body: RID, force: Vector3) virtual required`
- `void _body_add_constant_force(body: RID, force: Vector3, position: Vector3) virtual required`
- `void _body_add_constant_torque(body: RID, torque: Vector3) virtual required`
- `void _body_add_shape(body: RID, shape: RID, transform: Transform3D, disabled: bool) virtual required`
- `void _body_apply_central_force(body: RID, force: Vector3) virtual required`
- `void _body_apply_central_impulse(body: RID, impulse: Vector3) virtual required`
- `void _body_apply_force(body: RID, force: Vector3, position: Vector3) virtual required`
- `void _body_apply_impulse(body: RID, impulse: Vector3, position: Vector3) virtual required`
- `void _body_apply_torque(body: RID, torque: Vector3) virtual required`
- `void _body_apply_torque_impulse(body: RID, impulse: Vector3) virtual required`
- `void _body_attach_object_instance_id(body: RID, id: int) virtual required`
- `void _body_clear_shapes(body: RID) virtual required`
- `RID _body_create() virtual required`

### PhysicsServer3DManager
*Inherits: **Object***

PhysicsServer3DManager is the API for registering PhysicsServer3D implementations and for setting the default implementation.

**Methods**
- `void register_server(name: String, create_callback: Callable)`
- `void set_default_server(name: String, priority: int)`

### PhysicsServer3DRenderingServerHandler
*Inherits: **Object***

A class used to provide PhysicsServer3DExtension._soft_body_update_rendering_server() with a rendering handler for soft bodies.

**Methods**
- `void _set_aabb(aabb: AABB) virtual required`
- `void _set_normal(vertex_id: int, normal: Vector3) virtual required`
- `void _set_vertex(vertex_id: int, vertex: Vector3) virtual required`
- `void set_aabb(aabb: AABB)`
- `void set_normal(vertex_id: int, normal: Vector3)`
- `void set_vertex(vertex_id: int, vertex: Vector3)`

### PhysicsServer3D
*Inherits: **Object** | Inherited by: PhysicsServer3DExtension*

PhysicsServer3D is the server responsible for all 3D physics. It can directly create and manipulate all physics objects:

**Methods**
- `void area_add_shape(area: RID, shape: RID, transform: Transform3D = Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0), disabled: bool = false)`
- `void area_attach_object_instance_id(area: RID, id: int)`
- `void area_clear_shapes(area: RID)`
- `RID area_create()`
- `int area_get_collision_layer(area: RID) const`
- `int area_get_collision_mask(area: RID) const`
- `int area_get_object_instance_id(area: RID) const`
- `Variant area_get_param(area: RID, param: AreaParameter) const`
- `RID area_get_shape(area: RID, shape_idx: int) const`
- `int area_get_shape_count(area: RID) const`
- `Transform3D area_get_shape_transform(area: RID, shape_idx: int) const`
- `RID area_get_space(area: RID) const`
- `Transform3D area_get_transform(area: RID) const`
- `void area_remove_shape(area: RID, shape_idx: int)`
- `void area_set_area_monitor_callback(area: RID, callback: Callable)`
- `void area_set_collision_layer(area: RID, layer: int)`
- `void area_set_collision_mask(area: RID, mask: int)`
- `void area_set_monitor_callback(area: RID, callback: Callable)`
- `void area_set_monitorable(area: RID, monitorable: bool)`
- `void area_set_param(area: RID, param: AreaParameter, value: Variant)`
- `void area_set_ray_pickable(area: RID, enable: bool)`
- `void area_set_shape(area: RID, shape_idx: int, shape: RID)`
- `void area_set_shape_disabled(area: RID, shape_idx: int, disabled: bool)`
- `void area_set_shape_transform(area: RID, shape_idx: int, transform: Transform3D)`
- `void area_set_space(area: RID, space: RID)`
- `void area_set_transform(area: RID, transform: Transform3D)`
- `void body_add_collision_exception(body: RID, excepted_body: RID)`
- `void body_add_constant_central_force(body: RID, force: Vector3)`
- `void body_add_constant_force(body: RID, force: Vector3, position: Vector3 = Vector3(0, 0, 0))`
- `void body_add_constant_torque(body: RID, torque: Vector3)`
- `void body_add_shape(body: RID, shape: RID, transform: Transform3D = Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0), disabled: bool = false)`
- `void body_apply_central_force(body: RID, force: Vector3)`
- `void body_apply_central_impulse(body: RID, impulse: Vector3)`
- `void body_apply_force(body: RID, force: Vector3, position: Vector3 = Vector3(0, 0, 0))`
- `void body_apply_impulse(body: RID, impulse: Vector3, position: Vector3 = Vector3(0, 0, 0))`
- `void body_apply_torque(body: RID, torque: Vector3)`
- `void body_apply_torque_impulse(body: RID, impulse: Vector3)`
- `void body_attach_object_instance_id(body: RID, id: int)`
- `void body_clear_shapes(body: RID)`
- `RID body_create()`

### PhysicsShapeQueryParameters2D
*Inherits: **RefCounted < Object***

By changing various properties of this object, such as the shape, you can configure the parameters for PhysicsDirectSpaceState2D's methods.

**Properties**
- `bool collide_with_areas` = `false`
- `bool collide_with_bodies` = `true`
- `int collision_mask` = `4294967295`
- `Array[RID] exclude` = `[]`
- `float margin` = `0.0`
- `Vector2 motion` = `Vector2(0, 0)`
- `Resource shape`
- `RID shape_rid` = `RID()`
- `Transform2D transform` = `Transform2D(1, 0, 0, 1, 0, 0)`

**GDScript Examples**
```gdscript
var shape_rid = PhysicsServer2D.circle_shape_create()
var radius = 64
PhysicsServer2D.shape_set_data(shape_rid, radius)

var params = PhysicsShapeQueryParameters2D.new()
params.shape_rid = shape_rid

# Execute physics queries here...

# Release the shape when done with physics queries.
PhysicsServer2D.free_rid(shape_rid)
```

### PhysicsShapeQueryParameters3D
*Inherits: **RefCounted < Object***

By changing various properties of this object, such as the shape, you can configure the parameters for PhysicsDirectSpaceState3D's methods.

**Properties**
- `bool collide_with_areas` = `false`
- `bool collide_with_bodies` = `true`
- `int collision_mask` = `4294967295`
- `Array[RID] exclude` = `[]`
- `float margin` = `0.0`
- `Vector3 motion` = `Vector3(0, 0, 0)`
- `Resource shape`
- `RID shape_rid` = `RID()`
- `Transform3D transform` = `Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0)`

**GDScript Examples**
```gdscript
var shape_rid = PhysicsServer3D.sphere_shape_create()
var radius = 2.0
PhysicsServer3D.shape_set_data(shape_rid, radius)

var params = PhysicsShapeQueryParameters3D.new()
params.shape_rid = shape_rid

# Execute physics queries here...

# Release the shape when done with physics queries.
PhysicsServer3D.free_rid(shape_rid)
```

### PhysicsTestMotionParameters2D
*Inherits: **RefCounted < Object***

By changing various properties of this object, such as the motion, you can configure the parameters for PhysicsServer2D.body_test_motion().

**Properties**
- `bool collide_separation_ray` = `false`
- `Array[RID] exclude_bodies` = `[]`
- `Array[int] exclude_objects` = `[]`
- `Transform2D from` = `Transform2D(1, 0, 0, 1, 0, 0)`
- `float margin` = `0.08`
- `Vector2 motion` = `Vector2(0, 0)`
- `bool recovery_as_collision` = `false`

### PhysicsTestMotionParameters3D
*Inherits: **RefCounted < Object***

By changing various properties of this object, such as the motion, you can configure the parameters for PhysicsServer3D.body_test_motion().

**Properties**
- `bool collide_separation_ray` = `false`
- `Array[RID] exclude_bodies` = `[]`
- `Array[int] exclude_objects` = `[]`
- `Transform3D from` = `Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0)`
- `float margin` = `0.001`
- `int max_collisions` = `1`
- `Vector3 motion` = `Vector3(0, 0, 0)`
- `bool recovery_as_collision` = `false`

### PhysicsTestMotionResult2D
*Inherits: **RefCounted < Object***

Describes the motion and collision result from PhysicsServer2D.body_test_motion().

**Methods**
- `Object get_collider() const`
- `int get_collider_id() const`
- `RID get_collider_rid() const`
- `int get_collider_shape() const`
- `Vector2 get_collider_velocity() const`
- `float get_collision_depth() const`
- `int get_collision_local_shape() const`
- `Vector2 get_collision_normal() const`
- `Vector2 get_collision_point() const`
- `float get_collision_safe_fraction() const`
- `float get_collision_unsafe_fraction() const`
- `Vector2 get_remainder() const`
- `Vector2 get_travel() const`

### PhysicsTestMotionResult3D
*Inherits: **RefCounted < Object***

Describes the motion and collision result from PhysicsServer3D.body_test_motion().

**Methods**
- `Object get_collider(collision_index: int = 0) const`
- `int get_collider_id(collision_index: int = 0) const`
- `RID get_collider_rid(collision_index: int = 0) const`
- `int get_collider_shape(collision_index: int = 0) const`
- `Vector3 get_collider_velocity(collision_index: int = 0) const`
- `int get_collision_count() const`
- `float get_collision_depth(collision_index: int = 0) const`
- `int get_collision_local_shape(collision_index: int = 0) const`
- `Vector3 get_collision_normal(collision_index: int = 0) const`
- `Vector3 get_collision_point(collision_index: int = 0) const`
- `float get_collision_safe_fraction() const`
- `float get_collision_unsafe_fraction() const`
- `Vector3 get_remainder() const`
- `Vector3 get_travel() const`

### PinJoint3D
*Inherits: **Joint3D < Node3D < Node < Object***

A physics joint that attaches two 3D physics bodies at a single point, allowing them to freely rotate. For example, a RigidBody3D can be attached to a StaticBody3D to create a pendulum or a seesaw.

**Properties**
- `float params/bias` = `0.3`
- `float params/damping` = `1.0`
- `float params/impulse_clamp` = `0.0`

**Methods**
- `float get_param(param: Param) const`
- `void set_param(param: Param, value: float)`

### Shape2D
*Inherits: **Resource < RefCounted < Object** | Inherited by: CapsuleShape2D, CircleShape2D, ConcavePolygonShape2D, ConvexPolygonShape2D, RectangleShape2D, SegmentShape2D, ...*

Abstract base class for all 2D shapes, intended for use in physics.

**Properties**
- `float custom_solver_bias` = `0.0`

**Methods**
- `bool collide(local_xform: Transform2D, with_shape: Shape2D, shape_xform: Transform2D)`
- `PackedVector2Array collide_and_get_contacts(local_xform: Transform2D, with_shape: Shape2D, shape_xform: Transform2D)`
- `bool collide_with_motion(local_xform: Transform2D, local_motion: Vector2, with_shape: Shape2D, shape_xform: Transform2D, shape_motion: Vector2)`
- `PackedVector2Array collide_with_motion_and_get_contacts(local_xform: Transform2D, local_motion: Vector2, with_shape: Shape2D, shape_xform: Transform2D, shape_motion: Vector2)`
- `void draw(canvas_item: RID, color: Color)`
- `Rect2 get_rect() const`

### Shape3D
*Inherits: **Resource < RefCounted < Object** | Inherited by: BoxShape3D, CapsuleShape3D, ConcavePolygonShape3D, ConvexPolygonShape3D, CylinderShape3D, HeightMapShape3D, ...*

Abstract base class for all 3D shapes, intended for use in physics.

**Properties**
- `float custom_solver_bias` = `0.0`
- `float margin` = `0.04`

**Methods**
- `ArrayMesh get_debug_mesh()`

### SliderJoint3D
*Inherits: **Joint3D < Node3D < Node < Object***

A physics joint that restricts the movement of a 3D physics body along an axis relative to another physics body. For example, Body A could be a StaticBody3D representing a piston base, while Body B could be a RigidBody3D representing the piston head, moving up and down.

**Properties**
- `float angular_limit/damping` = `0.0`
- `float angular_limit/lower_angle` = `0.0`
- `float angular_limit/restitution` = `0.7`
- `float angular_limit/softness` = `1.0`
- `float angular_limit/upper_angle` = `0.0`
- `float angular_motion/damping` = `1.0`
- `float angular_motion/restitution` = `0.7`
- `float angular_motion/softness` = `1.0`
- `float angular_ortho/damping` = `1.0`
- `float angular_ortho/restitution` = `0.7`
- `float angular_ortho/softness` = `1.0`
- `float linear_limit/damping` = `1.0`
- `float linear_limit/lower_distance` = `-1.0`
- `float linear_limit/restitution` = `0.7`
- `float linear_limit/softness` = `1.0`
- `float linear_limit/upper_distance` = `1.0`
- `float linear_motion/damping` = `0.0`
- `float linear_motion/restitution` = `0.7`
- `float linear_motion/softness` = `1.0`
- `float linear_ortho/damping` = `1.0`
- `float linear_ortho/restitution` = `0.7`
- `float linear_ortho/softness` = `1.0`

**Methods**
- `float get_param(param: Param) const`
- `void set_param(param: Param, value: float)`
