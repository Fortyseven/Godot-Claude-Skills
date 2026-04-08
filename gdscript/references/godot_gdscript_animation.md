# Godot 4 GDScript API Reference — Animation

> GDScript-only reference. 18 classes.

### AimModifier3D
*Inherits: **BoneConstraint3D < SkeletonModifier3D < Node3D < Node < Object***

This is a simple version of LookAtModifier3D that only allows bone to the reference without advanced options such as angle limitation or time-based interpolation.

**Properties**
- `int setting_count` = `0`

**Methods**
- `BoneAxis get_forward_axis(index: int) const`
- `Axis get_primary_rotation_axis(index: int) const`
- `bool is_relative(index: int) const`
- `bool is_using_euler(index: int) const`
- `bool is_using_secondary_rotation(index: int) const`
- `void set_forward_axis(index: int, axis: BoneAxis)`
- `void set_primary_rotation_axis(index: int, axis: Axis)`
- `void set_relative(index: int, enabled: bool)`
- `void set_use_euler(index: int, enabled: bool)`
- `void set_use_secondary_rotation(index: int, enabled: bool)`

### CallbackTweener
*Inherits: **Tweener < RefCounted < Object***

CallbackTweener is used to call a method in a tweening sequence. See Tween.tween_callback() for more usage information.

**Methods**
- `CallbackTweener set_delay(delay: float)`

**GDScript Examples**
```gdscript
var tween = get_tree().create_tween()
tween.tween_callback(queue_free).set_delay(2)
```

### IntervalTweener
*Inherits: **Tweener < RefCounted < Object***

IntervalTweener is used to make delays in a tweening sequence. See Tween.tween_interval() for more usage information.

### LookAtModifier3D
*Inherits: **SkeletonModifier3D < Node3D < Node < Object***

This SkeletonModifier3D rotates a bone to look at a target. This is helpful for moving a character's head to look at the player, rotating a turret to look at a target, or any other case where you want to make a bone rotate towards something quickly and easily.

**Properties**
- `int bone` = `-1`
- `String bone_name` = `""`
- `float duration` = `0.0`
- `EaseType ease_type` = `0`
- `BoneAxis forward_axis` = `4`
- `int origin_bone`
- `String origin_bone_name`
- `NodePath origin_external_node`
- `OriginFrom origin_from` = `0`
- `Vector3 origin_offset` = `Vector3(0, 0, 0)`
- `float origin_safe_margin` = `0.1`
- `float primary_damp_threshold`
- `float primary_limit_angle`
- `float primary_negative_damp_threshold`
- `float primary_negative_limit_angle`
- `float primary_positive_damp_threshold`
- `float primary_positive_limit_angle`
- `Axis primary_rotation_axis` = `1`
- `bool relative` = `true`
- `float secondary_damp_threshold`
- `float secondary_limit_angle`
- `float secondary_negative_damp_threshold`
- `float secondary_negative_limit_angle`
- `float secondary_positive_damp_threshold`
- `float secondary_positive_limit_angle`
- `bool symmetry_limitation`
- `NodePath target_node` = `NodePath("")`
- `TransitionType transition_type` = `0`
- `bool use_angle_limitation` = `false`
- `bool use_secondary_rotation` = `true`

**Methods**
- `float get_interpolation_remaining() const`
- `bool is_interpolating() const`
- `bool is_target_within_limitation() const`

### MethodTweener
*Inherits: **Tweener < RefCounted < Object***

MethodTweener is similar to a combination of CallbackTweener and PropertyTweener. It calls a method providing an interpolated value as a parameter. See Tween.tween_method() for more usage information.

**Methods**
- `MethodTweener set_delay(delay: float)`
- `MethodTweener set_ease(ease: EaseType)`
- `MethodTweener set_trans(trans: TransitionType)`

### PropertyTweener
*Inherits: **Tweener < RefCounted < Object***

PropertyTweener is used to interpolate a property in an object. See Tween.tween_property() for more usage information.

**Methods**
- `PropertyTweener as_relative()`
- `PropertyTweener from(value: Variant)`
- `PropertyTweener from_current()`
- `PropertyTweener set_custom_interpolator(interpolator_method: Callable)`
- `PropertyTweener set_delay(delay: float)`
- `PropertyTweener set_ease(ease: EaseType)`
- `PropertyTweener set_trans(trans: TransitionType)`

**GDScript Examples**
```gdscript
var tween = get_tree().create_tween()
tween.tween_property(self, "position", Vector2.RIGHT * 100, 1).as_relative()
```
```gdscript
var tween = get_tree().create_tween()
tween.tween_property(self, "position", Vector2(200, 100), 1).from(Vector2(100, 100))
```

### SkeletonIK3D
*Inherits: **SkeletonModifier3D < Node3D < Node < Object***

SkeletonIK3D is used to rotate all bones of a Skeleton3D bone chain a way that places the end bone at a desired 3D position. A typical scenario for IK in games is to place a character's feet on the ground or a character's hands on a currently held object. SkeletonIK uses FabrikInverseKinematic internally to solve the bone chain and applies the results to the Skeleton3D bones_global_pose_override property for all affected bones in the chain. If fully applied, this overwrites any bone transform from Animations or bone custom poses set by users. The applied amount can be controlled with the SkeletonModifier3D.influence property.

**Properties**
- `float interpolation`
- `Vector3 magnet` = `Vector3(0, 0, 0)`
- `int max_iterations` = `10`
- `float min_distance` = `0.01`
- `bool override_tip_basis` = `true`
- `StringName root_bone` = `&""`
- `Transform3D target` = `Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0)`
- `NodePath target_node` = `NodePath("")`
- `StringName tip_bone` = `&""`
- `bool use_magnet` = `false`

**Methods**
- `Skeleton3D get_parent_skeleton() const`
- `bool is_running()`
- `void start(one_time: bool = false)`
- `void stop()`

**GDScript Examples**
```gdscript
# Apply IK effect automatically on every new frame (not the current)
skeleton_ik_node.start()

# Apply IK effect only on the current frame
skeleton_ik_node.start(true)

# Stop IK effect and reset bones_global_pose_override on Skeleton
skeleton_ik_node.stop()

# Apply full IK effect
skeleton_ik_node.set_influence(1.0)

# Apply half IK effect
skeleton_ik_node.set_influence(0.5)

# Apply zero IK effect (a value at or below 0.01 also removes bones_global_pose_override on Skeleton)
skeleton_ik_node.set_influence(0.0)
```

### SkeletonModification2DCCDIK
*Inherits: **SkeletonModification2D < Resource < RefCounted < Object***

This SkeletonModification2D uses an algorithm called Cyclic Coordinate Descent Inverse Kinematics, or CCDIK, to manipulate a chain of bones in a Skeleton2D so it reaches a defined target.

**Properties**
- `int ccdik_data_chain_length` = `0`
- `NodePath target_nodepath` = `NodePath("")`
- `NodePath tip_nodepath` = `NodePath("")`

**Methods**
- `NodePath get_ccdik_joint_bone2d_node(joint_idx: int) const`
- `int get_ccdik_joint_bone_index(joint_idx: int) const`
- `bool get_ccdik_joint_constraint_angle_invert(joint_idx: int) const`
- `float get_ccdik_joint_constraint_angle_max(joint_idx: int) const`
- `float get_ccdik_joint_constraint_angle_min(joint_idx: int) const`
- `bool get_ccdik_joint_enable_constraint(joint_idx: int) const`
- `bool get_ccdik_joint_rotate_from_joint(joint_idx: int) const`
- `void set_ccdik_joint_bone2d_node(joint_idx: int, bone2d_nodepath: NodePath)`
- `void set_ccdik_joint_bone_index(joint_idx: int, bone_idx: int)`
- `void set_ccdik_joint_constraint_angle_invert(joint_idx: int, invert: bool)`
- `void set_ccdik_joint_constraint_angle_max(joint_idx: int, angle_max: float)`
- `void set_ccdik_joint_constraint_angle_min(joint_idx: int, angle_min: float)`
- `void set_ccdik_joint_enable_constraint(joint_idx: int, enable_constraint: bool)`
- `void set_ccdik_joint_rotate_from_joint(joint_idx: int, rotate_from_joint: bool)`

### SkeletonModification2DFABRIK
*Inherits: **SkeletonModification2D < Resource < RefCounted < Object***

This SkeletonModification2D uses an algorithm called Forward And Backward Reaching Inverse Kinematics, or FABRIK, to rotate a bone chain so that it reaches a target.

**Properties**
- `int fabrik_data_chain_length` = `0`
- `NodePath target_nodepath` = `NodePath("")`

**Methods**
- `NodePath get_fabrik_joint_bone2d_node(joint_idx: int) const`
- `int get_fabrik_joint_bone_index(joint_idx: int) const`
- `Vector2 get_fabrik_joint_magnet_position(joint_idx: int) const`
- `bool get_fabrik_joint_use_target_rotation(joint_idx: int) const`
- `void set_fabrik_joint_bone2d_node(joint_idx: int, bone2d_nodepath: NodePath)`
- `void set_fabrik_joint_bone_index(joint_idx: int, bone_idx: int)`
- `void set_fabrik_joint_magnet_position(joint_idx: int, magnet_position: Vector2)`
- `void set_fabrik_joint_use_target_rotation(joint_idx: int, use_target_rotation: bool)`

### SkeletonModification2DJiggle
*Inherits: **SkeletonModification2D < Resource < RefCounted < Object***

This modification moves a series of bones, typically called a bone chain, towards a target. What makes this modification special is that it calculates the velocity and acceleration for each bone in the bone chain, and runs a very light physics-like calculation using the inputted values. This allows the bones to overshoot the target and "jiggle" around. It can be configured to act more like a spring, or sway around like cloth might.

**Properties**
- `float damping` = `0.75`
- `Vector2 gravity` = `Vector2(0, 6)`
- `int jiggle_data_chain_length` = `0`
- `float mass` = `0.75`
- `float stiffness` = `3.0`
- `NodePath target_nodepath` = `NodePath("")`
- `bool use_gravity` = `false`

**Methods**
- `int get_collision_mask() const`
- `NodePath get_jiggle_joint_bone2d_node(joint_idx: int) const`
- `int get_jiggle_joint_bone_index(joint_idx: int) const`
- `float get_jiggle_joint_damping(joint_idx: int) const`
- `Vector2 get_jiggle_joint_gravity(joint_idx: int) const`
- `float get_jiggle_joint_mass(joint_idx: int) const`
- `bool get_jiggle_joint_override(joint_idx: int) const`
- `float get_jiggle_joint_stiffness(joint_idx: int) const`
- `bool get_jiggle_joint_use_gravity(joint_idx: int) const`
- `bool get_use_colliders() const`
- `void set_collision_mask(collision_mask: int)`
- `void set_jiggle_joint_bone2d_node(joint_idx: int, bone2d_node: NodePath)`
- `void set_jiggle_joint_bone_index(joint_idx: int, bone_idx: int)`
- `void set_jiggle_joint_damping(joint_idx: int, damping: float)`
- `void set_jiggle_joint_gravity(joint_idx: int, gravity: Vector2)`
- `void set_jiggle_joint_mass(joint_idx: int, mass: float)`
- `void set_jiggle_joint_override(joint_idx: int, override: bool)`
- `void set_jiggle_joint_stiffness(joint_idx: int, stiffness: float)`
- `void set_jiggle_joint_use_gravity(joint_idx: int, use_gravity: bool)`
- `void set_use_colliders(use_colliders: bool)`

### SkeletonModification2DLookAt
*Inherits: **SkeletonModification2D < Resource < RefCounted < Object***

This SkeletonModification2D rotates a bone to look a target. This is extremely helpful for moving character's head to look at the player, rotating a turret to look at a target, or any other case where you want to make a bone rotate towards something quickly and easily.

**Properties**
- `NodePath bone2d_node` = `NodePath("")`
- `int bone_index` = `-1`
- `NodePath target_nodepath` = `NodePath("")`

**Methods**
- `float get_additional_rotation() const`
- `bool get_constraint_angle_invert() const`
- `float get_constraint_angle_max() const`
- `float get_constraint_angle_min() const`
- `bool get_enable_constraint() const`
- `void set_additional_rotation(rotation: float)`
- `void set_constraint_angle_invert(invert: bool)`
- `void set_constraint_angle_max(angle_max: float)`
- `void set_constraint_angle_min(angle_min: float)`
- `void set_enable_constraint(enable_constraint: bool)`

### SkeletonModification2DPhysicalBones
*Inherits: **SkeletonModification2D < Resource < RefCounted < Object***

This modification takes the transforms of PhysicalBone2D nodes and applies them to Bone2D nodes. This allows the Bone2D nodes to react to physics thanks to the linked PhysicalBone2D nodes.

**Properties**
- `int physical_bone_chain_length` = `0`

**Methods**
- `void fetch_physical_bones()`
- `NodePath get_physical_bone_node(joint_idx: int) const`
- `void set_physical_bone_node(joint_idx: int, physicalbone2d_node: NodePath)`
- `void start_simulation(bones: Array[StringName] = [])`
- `void stop_simulation(bones: Array[StringName] = [])`

### SkeletonModification2DStackHolder
*Inherits: **SkeletonModification2D < Resource < RefCounted < Object***

This SkeletonModification2D holds a reference to a SkeletonModificationStack2D, allowing you to use multiple modification stacks on a single Skeleton2D.

**Methods**
- `SkeletonModificationStack2D get_held_modification_stack() const`
- `void set_held_modification_stack(held_modification_stack: SkeletonModificationStack2D)`

### SkeletonModification2DTwoBoneIK
*Inherits: **SkeletonModification2D < Resource < RefCounted < Object***

This SkeletonModification2D uses an algorithm typically called TwoBoneIK. This algorithm works by leveraging the law of cosines and the lengths of the bones to figure out what rotation the bones currently have, and what rotation they need to make a complete triangle, where the first bone, the second bone, and the target form the three vertices of the triangle. Because the algorithm works by making a triangle, it can only operate on two bones.

**Properties**
- `bool flip_bend_direction` = `false`
- `float target_maximum_distance` = `0.0`
- `float target_minimum_distance` = `0.0`
- `NodePath target_nodepath` = `NodePath("")`

**Methods**
- `NodePath get_joint_one_bone2d_node() const`
- `int get_joint_one_bone_idx() const`
- `NodePath get_joint_two_bone2d_node() const`
- `int get_joint_two_bone_idx() const`
- `void set_joint_one_bone2d_node(bone2d_node: NodePath)`
- `void set_joint_one_bone_idx(bone_idx: int)`
- `void set_joint_two_bone2d_node(bone2d_node: NodePath)`
- `void set_joint_two_bone_idx(bone_idx: int)`

### SkeletonModification2D
*Inherits: **Resource < RefCounted < Object** | Inherited by: SkeletonModification2DCCDIK, SkeletonModification2DFABRIK, SkeletonModification2DJiggle, SkeletonModification2DLookAt, SkeletonModification2DPhysicalBones, SkeletonModification2DStackHolder, ...*

This resource provides an interface that can be expanded so code that operates on Bone2D nodes in a Skeleton2D can be mixed and matched together to create complex interactions.

**Properties**
- `bool enabled` = `true`
- `int execution_mode` = `0`

**Methods**
- `void _draw_editor_gizmo() virtual`
- `void _execute(delta: float) virtual`
- `void _setup_modification(modification_stack: SkeletonModificationStack2D) virtual`
- `float clamp_angle(angle: float, min: float, max: float, invert: bool)`
- `bool get_editor_draw_gizmo() const`
- `bool get_is_setup() const`
- `SkeletonModificationStack2D get_modification_stack()`
- `void set_editor_draw_gizmo(draw_gizmo: bool)`
- `void set_is_setup(is_setup: bool)`

### SkeletonModificationStack2D
*Inherits: **Resource < RefCounted < Object***

This resource is used by the Skeleton and holds a stack of SkeletonModification2Ds.

**Properties**
- `bool enabled` = `false`
- `int modification_count` = `0`
- `float strength` = `1.0`

**Methods**
- `void add_modification(modification: SkeletonModification2D)`
- `void delete_modification(mod_idx: int)`
- `void enable_all_modifications(enabled: bool)`
- `void execute(delta: float, execution_mode: int)`
- `bool get_is_setup() const`
- `SkeletonModification2D get_modification(mod_idx: int) const`
- `Skeleton2D get_skeleton() const`
- `void set_modification(mod_idx: int, modification: SkeletonModification2D)`
- `void setup()`

### SkeletonModifier3D
*Inherits: **Node3D < Node < Object** | Inherited by: BoneConstraint3D, BoneTwistDisperser3D, IKModifier3D, LimitAngularVelocityModifier3D, LookAtModifier3D, ModifierBoneTarget3D, ...*

SkeletonModifier3D retrieves a target Skeleton3D by having a Skeleton3D parent.

**Properties**
- `bool active` = `true`
- `float influence` = `1.0`

**Methods**
- `void _process_modification() virtual`
- `void _process_modification_with_delta(delta: float) virtual`
- `void _skeleton_changed(old_skeleton: Skeleton3D, new_skeleton: Skeleton3D) virtual`
- `void _validate_bone_names() virtual`
- `Skeleton3D get_skeleton() const`

### Tweener
*Inherits: **RefCounted < Object** | Inherited by: CallbackTweener, IntervalTweener, MethodTweener, PropertyTweener, SubtweenTweener*

Tweeners are objects that perform a specific animating task, e.g. interpolating a property or calling a method at a given time. A Tweener can't be created manually, you need to use a dedicated method from Tween.
