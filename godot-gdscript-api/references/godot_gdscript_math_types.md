# Godot 4 GDScript API Reference — Math Types

> GDScript-only reference. 11 classes.

### Projection

A 4×4 matrix used for 3D projective transformations. It can represent transformations such as translation, rotation, scaling, shearing, and perspective division. It consists of four Vector4 columns.

**Properties**
- `Vector4 w` = `Vector4(0, 0, 0, 1)`
- `Vector4 x` = `Vector4(1, 0, 0, 0)`
- `Vector4 y` = `Vector4(0, 1, 0, 0)`
- `Vector4 z` = `Vector4(0, 0, 1, 0)`

**Methods**
- `Projection create_depth_correction(flip_y: bool) static`
- `Projection create_fit_aabb(aabb: AABB) static`
- `Projection create_for_hmd(eye: int, aspect: float, intraocular_dist: float, display_width: float, display_to_lens: float, oversample: float, z_near: float, z_far: float) static`
- `Projection create_frustum(left: float, right: float, bottom: float, top: float, z_near: float, z_far: float) static`
- `Projection create_frustum_aspect(size: float, aspect: float, offset: Vector2, z_near: float, z_far: float, flip_fov: bool = false) static`
- `Projection create_light_atlas_rect(rect: Rect2) static`
- `Projection create_orthogonal(left: float, right: float, bottom: float, top: float, z_near: float, z_far: float) static`
- `Projection create_orthogonal_aspect(size: float, aspect: float, z_near: float, z_far: float, flip_fov: bool = false) static`
- `Projection create_perspective(fovy: float, aspect: float, z_near: float, z_far: float, flip_fov: bool = false) static`
- `Projection create_perspective_hmd(fovy: float, aspect: float, z_near: float, z_far: float, flip_fov: bool, eye: int, intraocular_dist: float, convergence_dist: float) static`
- `float determinant() const`
- `Projection flipped_y() const`
- `float get_aspect() const`
- `Vector2 get_far_plane_half_extents() const`
- `float get_fov() const`
- `float get_fovy(fovx: float, aspect: float) static`
- `float get_lod_multiplier() const`
- `int get_pixels_per_meter(for_pixel_width: int) const`
- `Plane get_projection_plane(plane: int) const`
- `Vector2 get_viewport_half_extents() const`
- `float get_z_far() const`
- `float get_z_near() const`
- `Projection inverse() const`
- `bool is_orthogonal() const`
- `Projection jitter_offseted(offset: Vector2) const`
- `Projection perspective_znear_adjusted(new_znear: float) const`

### Quaternion

The Quaternion built-in Variant type is a 4D data structure that represents rotation in the form of a Hamilton convention quaternion. Compared to the Basis type which can store both rotation and scale, quaternions can only store rotation.

**Properties**
- `float w` = `1.0`
- `float x` = `0.0`
- `float y` = `0.0`
- `float z` = `0.0`

**Methods**
- `float angle_to(to: Quaternion) const`
- `float dot(with: Quaternion) const`
- `Quaternion exp() const`
- `Quaternion from_euler(euler: Vector3) static`
- `float get_angle() const`
- `Vector3 get_axis() const`
- `Vector3 get_euler(order: int = 2) const`
- `Quaternion inverse() const`
- `bool is_equal_approx(to: Quaternion) const`
- `bool is_finite() const`
- `bool is_normalized() const`
- `float length() const`
- `float length_squared() const`
- `Quaternion log() const`
- `Quaternion normalized() const`
- `Quaternion slerp(to: Quaternion, weight: float) const`
- `Quaternion slerpni(to: Quaternion, weight: float) const`
- `Quaternion spherical_cubic_interpolate(b: Quaternion, pre_a: Quaternion, post_b: Quaternion, weight: float) const`
- `Quaternion spherical_cubic_interpolate_in_time(b: Quaternion, pre_a: Quaternion, post_b: Quaternion, weight: float, b_t: float, pre_a_t: float, post_b_t: float) const`

### Rect2i

The Rect2i built-in Variant type represents an axis-aligned rectangle in a 2D space, using integer coordinates. It is defined by its position and size, which are Vector2i. Because it does not rotate, it is frequently used for fast overlap tests (see intersects()).

**Properties**
- `Vector2i end` = `Vector2i(0, 0)`
- `Vector2i position` = `Vector2i(0, 0)`
- `Vector2i size` = `Vector2i(0, 0)`

**Methods**
- `Rect2i abs() const`
- `bool encloses(b: Rect2i) const`
- `Rect2i expand(to: Vector2i) const`
- `int get_area() const`
- `Vector2i get_center() const`
- `Rect2i grow(amount: int) const`
- `Rect2i grow_individual(left: int, top: int, right: int, bottom: int) const`
- `Rect2i grow_side(side: int, amount: int) const`
- `bool has_area() const`
- `bool has_point(point: Vector2i) const`
- `Rect2i intersection(b: Rect2i) const`
- `bool intersects(b: Rect2i) const`
- `Rect2i merge(b: Rect2i) const`

**GDScript Examples**
```gdscript
var rect = Rect2i(25, 25, -100, -50)
var absolute = rect.abs() # absolute is Rect2i(-75, -25, 100, 50)
```
```gdscript
var rect = Rect2i(0, 0, 5, 2)

rect = rect.expand(Vector2i(10, 0)) # rect is Rect2i(0, 0, 10, 2)
rect = rect.expand(Vector2i(-5, 5)) # rect is Rect2i(-5, 0, 15, 5)
```

### Transform2D

The Transform2D built-in Variant type is a 2×3 matrix representing a transformation in 2D space. It contains three Vector2 values: x, y, and origin. Together, they can represent translation, rotation, scale, and skew.

**Properties**
- `Vector2 origin` = `Vector2(0, 0)`
- `Vector2 x` = `Vector2(1, 0)`
- `Vector2 y` = `Vector2(0, 1)`

**Methods**
- `Transform2D affine_inverse() const`
- `Vector2 basis_xform(v: Vector2) const`
- `Vector2 basis_xform_inv(v: Vector2) const`
- `float determinant() const`
- `Vector2 get_origin() const`
- `float get_rotation() const`
- `Vector2 get_scale() const`
- `float get_skew() const`
- `Transform2D interpolate_with(xform: Transform2D, weight: float) const`
- `Transform2D inverse() const`
- `bool is_conformal() const`
- `bool is_equal_approx(xform: Transform2D) const`
- `bool is_finite() const`
- `Transform2D looking_at(target: Vector2 = Vector2(0, 0)) const`
- `Transform2D orthonormalized() const`
- `Transform2D rotated(angle: float) const`
- `Transform2D rotated_local(angle: float) const`
- `Transform2D scaled(scale: Vector2) const`
- `Transform2D scaled_local(scale: Vector2) const`
- `Transform2D translated(offset: Vector2) const`
- `Transform2D translated_local(offset: Vector2) const`

**GDScript Examples**
```gdscript
var my_transform = Transform2D(
    Vector2(2, 0),
    Vector2(0, 4),
    Vector2(0, 0)
)
# Rotating the Transform2D in any way preserves its scale.
my_transform = my_transform.rotated(TAU / 2)

print(my_transform.get_scale()) # Prints (2.0, 4.0)
```
```gdscript
var transform = Transform2D.IDENTITY
print("| X | Y | Origin")
print("| %.f | %.f | %.f" % [transform.x.x, transform.y.x, transform.origin.x])
print("| %.f | %.f | %.f" % [transform.x.y, transform.y.y, transform.origin.y])
# Prints:
# | X | Y | Origin
# | 1 | 0 | 0
# | 0 | 1 | 0
```

### Transform3D

The Transform3D built-in Variant type is a 3×4 matrix representing a transformation in 3D space. It contains a Basis, which on its own can represent rotation, scale, and shear. Additionally, combined with its own origin, the transform can also represent a translation.

**Properties**
- `Basis basis` = `Basis(1, 0, 0, 0, 1, 0, 0, 0, 1)`
- `Vector3 origin` = `Vector3(0, 0, 0)`

**Methods**
- `Transform3D affine_inverse() const`
- `Transform3D interpolate_with(xform: Transform3D, weight: float) const`
- `Transform3D inverse() const`
- `bool is_equal_approx(xform: Transform3D) const`
- `bool is_finite() const`
- `Transform3D looking_at(target: Vector3, up: Vector3 = Vector3(0, 1, 0), use_model_front: bool = false) const`
- `Transform3D orthonormalized() const`
- `Transform3D rotated(axis: Vector3, angle: float) const`
- `Transform3D rotated_local(axis: Vector3, angle: float) const`
- `Transform3D scaled(scale: Vector3) const`
- `Transform3D scaled_local(scale: Vector3) const`
- `Transform3D translated(offset: Vector3) const`
- `Transform3D translated_local(offset: Vector3) const`

**GDScript Examples**
```gdscript
var transform = Transform3D.IDENTITY
var basis = transform.basis
print("| X | Y | Z | Origin")
print("| %.f | %.f | %.f | %.f" % [basis.x.x, basis.y.x, basis.z.x, transform.origin.x])
print("| %.f | %.f | %.f | %.f" % [basis.x.y, basis.y.y, basis.z.y, transform.origin.y])
print("| %.f | %.f | %.f | %.f" % [basis.x.z, basis.y.z, basis.z.z, transform.origin.z])
# Prints:
# | X | Y | Z | Origin
# | 1 | 0 | 0 | 0
# | 0 | 1 | 0 | 0
# | 0 | 0 | 1 | 0
```

### Vector2i

A 2-element structure that can be used to represent 2D grid coordinates or any other pair of integers.

**Properties**
- `int x` = `0`
- `int y` = `0`

**Methods**
- `Vector2i abs() const`
- `float aspect() const`
- `Vector2i clamp(min: Vector2i, max: Vector2i) const`
- `Vector2i clampi(min: int, max: int) const`
- `int distance_squared_to(to: Vector2i) const`
- `float distance_to(to: Vector2i) const`
- `float length() const`
- `int length_squared() const`
- `Vector2i max(with: Vector2i) const`
- `int max_axis_index() const`
- `Vector2i maxi(with: int) const`
- `Vector2i min(with: Vector2i) const`
- `int min_axis_index() const`
- `Vector2i mini(with: int) const`
- `Vector2i sign() const`
- `Vector2i snapped(step: Vector2i) const`
- `Vector2i snappedi(step: int) const`

**GDScript Examples**
```gdscript
print(Vector2i(10, -20) % Vector2i(7, 8)) # Prints (3, -4)
```
```gdscript
print(Vector2i(10, -20) % 7) # Prints (3, -6)
```

### Vector2

A 2-element structure that can be used to represent 2D coordinates or any other pair of numeric values.

**Properties**
- `float x` = `0.0`
- `float y` = `0.0`

**Methods**
- `Vector2 abs() const`
- `float angle() const`
- `float angle_to(to: Vector2) const`
- `float angle_to_point(to: Vector2) const`
- `float aspect() const`
- `Vector2 bezier_derivative(control_1: Vector2, control_2: Vector2, end: Vector2, t: float) const`
- `Vector2 bezier_interpolate(control_1: Vector2, control_2: Vector2, end: Vector2, t: float) const`
- `Vector2 bounce(n: Vector2) const`
- `Vector2 ceil() const`
- `Vector2 clamp(min: Vector2, max: Vector2) const`
- `Vector2 clampf(min: float, max: float) const`
- `float cross(with: Vector2) const`
- `Vector2 cubic_interpolate(b: Vector2, pre_a: Vector2, post_b: Vector2, weight: float) const`
- `Vector2 cubic_interpolate_in_time(b: Vector2, pre_a: Vector2, post_b: Vector2, weight: float, b_t: float, pre_a_t: float, post_b_t: float) const`
- `Vector2 direction_to(to: Vector2) const`
- `float distance_squared_to(to: Vector2) const`
- `float distance_to(to: Vector2) const`
- `float dot(with: Vector2) const`
- `Vector2 floor() const`
- `Vector2 from_angle(angle: float) static`
- `bool is_equal_approx(to: Vector2) const`
- `bool is_finite() const`
- `bool is_normalized() const`
- `bool is_zero_approx() const`
- `float length() const`
- `float length_squared() const`
- `Vector2 lerp(to: Vector2, weight: float) const`
- `Vector2 limit_length(length: float = 1.0) const`
- `Vector2 max(with: Vector2) const`
- `int max_axis_index() const`
- `Vector2 maxf(with: float) const`
- `Vector2 min(with: Vector2) const`
- `int min_axis_index() const`
- `Vector2 minf(with: float) const`
- `Vector2 move_toward(to: Vector2, delta: float) const`
- `Vector2 normalized() const`
- `Vector2 orthogonal() const`
- `Vector2 posmod(mod: float) const`
- `Vector2 posmodv(modv: Vector2) const`
- `Vector2 project(b: Vector2) const`

**GDScript Examples**
```gdscript
print(Vector2.from_angle(0)) # Prints (1.0, 0.0)
print(Vector2(1, 0).angle()) # Prints 0.0, which is the angle used above.
print(Vector2.from_angle(PI / 2)) # Prints (0.0, 1.0)
```
```gdscript
print(Vector2(10, 20) * Vector2(3, 4)) # Prints (30.0, 80.0)
```

### Vector3i

A 3-element structure that can be used to represent 3D grid coordinates or any other triplet of integers.

**Properties**
- `int x` = `0`
- `int y` = `0`
- `int z` = `0`

**Methods**
- `Vector3i abs() const`
- `Vector3i clamp(min: Vector3i, max: Vector3i) const`
- `Vector3i clampi(min: int, max: int) const`
- `int distance_squared_to(to: Vector3i) const`
- `float distance_to(to: Vector3i) const`
- `float length() const`
- `int length_squared() const`
- `Vector3i max(with: Vector3i) const`
- `int max_axis_index() const`
- `Vector3i maxi(with: int) const`
- `Vector3i min(with: Vector3i) const`
- `int min_axis_index() const`
- `Vector3i mini(with: int) const`
- `Vector3i sign() const`
- `Vector3i snapped(step: Vector3i) const`
- `Vector3i snappedi(step: int) const`

**GDScript Examples**
```gdscript
print(Vector3i(10, -20, 30) % Vector3i(7, 8, 9)) # Prints (3, -4, 3)
```
```gdscript
print(Vector3i(10, -20, 30) % 7) # Prints (3, -6, 2)
```

### Vector3

A 3-element structure that can be used to represent 3D coordinates or any other triplet of numeric values.

**Properties**
- `float x` = `0.0`
- `float y` = `0.0`
- `float z` = `0.0`

**Methods**
- `Vector3 abs() const`
- `float angle_to(to: Vector3) const`
- `Vector3 bezier_derivative(control_1: Vector3, control_2: Vector3, end: Vector3, t: float) const`
- `Vector3 bezier_interpolate(control_1: Vector3, control_2: Vector3, end: Vector3, t: float) const`
- `Vector3 bounce(n: Vector3) const`
- `Vector3 ceil() const`
- `Vector3 clamp(min: Vector3, max: Vector3) const`
- `Vector3 clampf(min: float, max: float) const`
- `Vector3 cross(with: Vector3) const`
- `Vector3 cubic_interpolate(b: Vector3, pre_a: Vector3, post_b: Vector3, weight: float) const`
- `Vector3 cubic_interpolate_in_time(b: Vector3, pre_a: Vector3, post_b: Vector3, weight: float, b_t: float, pre_a_t: float, post_b_t: float) const`
- `Vector3 direction_to(to: Vector3) const`
- `float distance_squared_to(to: Vector3) const`
- `float distance_to(to: Vector3) const`
- `float dot(with: Vector3) const`
- `Vector3 floor() const`
- `Vector3 inverse() const`
- `bool is_equal_approx(to: Vector3) const`
- `bool is_finite() const`
- `bool is_normalized() const`
- `bool is_zero_approx() const`
- `float length() const`
- `float length_squared() const`
- `Vector3 lerp(to: Vector3, weight: float) const`
- `Vector3 limit_length(length: float = 1.0) const`
- `Vector3 max(with: Vector3) const`
- `int max_axis_index() const`
- `Vector3 maxf(with: float) const`
- `Vector3 min(with: Vector3) const`
- `int min_axis_index() const`
- `Vector3 minf(with: float) const`
- `Vector3 move_toward(to: Vector3, delta: float) const`
- `Vector3 normalized() const`
- `Vector3 octahedron_decode(uv: Vector2) static`
- `Vector2 octahedron_encode() const`
- `Basis outer(with: Vector3) const`
- `Vector3 posmod(mod: float) const`
- `Vector3 posmodv(modv: Vector3) const`
- `Vector3 project(b: Vector3) const`
- `Vector3 reflect(n: Vector3) const`

**GDScript Examples**
```gdscript
print(Vector3(10, 20, 30) * Vector3(3, 4, 5)) # Prints (30.0, 80.0, 150.0)
```
```gdscript
print(Vector3(10, 20, 30) + Vector3(3, 4, 5)) # Prints (13.0, 24.0, 35.0)
```

### Vector4i

A 4-element structure that can be used to represent 4D grid coordinates or any other quadruplet of integers.

**Properties**
- `int w` = `0`
- `int x` = `0`
- `int y` = `0`
- `int z` = `0`

**Methods**
- `Vector4i abs() const`
- `Vector4i clamp(min: Vector4i, max: Vector4i) const`
- `Vector4i clampi(min: int, max: int) const`
- `int distance_squared_to(to: Vector4i) const`
- `float distance_to(to: Vector4i) const`
- `float length() const`
- `int length_squared() const`
- `Vector4i max(with: Vector4i) const`
- `int max_axis_index() const`
- `Vector4i maxi(with: int) const`
- `Vector4i min(with: Vector4i) const`
- `int min_axis_index() const`
- `Vector4i mini(with: int) const`
- `Vector4i sign() const`
- `Vector4i snapped(step: Vector4i) const`
- `Vector4i snappedi(step: int) const`

**GDScript Examples**
```gdscript
print(Vector4i(10, -20, 30, -40) % Vector4i(7, 8, 9, 10)) # Prints (3, -4, 3, 0)
```
```gdscript
print(Vector4i(10, -20, 30, -40) % 7) # Prints (3, -6, 2, -5)
```

### Vector4

A 4-element structure that can be used to represent 4D coordinates or any other quadruplet of numeric values.

**Properties**
- `float w` = `0.0`
- `float x` = `0.0`
- `float y` = `0.0`
- `float z` = `0.0`

**Methods**
- `Vector4 abs() const`
- `Vector4 ceil() const`
- `Vector4 clamp(min: Vector4, max: Vector4) const`
- `Vector4 clampf(min: float, max: float) const`
- `Vector4 cubic_interpolate(b: Vector4, pre_a: Vector4, post_b: Vector4, weight: float) const`
- `Vector4 cubic_interpolate_in_time(b: Vector4, pre_a: Vector4, post_b: Vector4, weight: float, b_t: float, pre_a_t: float, post_b_t: float) const`
- `Vector4 direction_to(to: Vector4) const`
- `float distance_squared_to(to: Vector4) const`
- `float distance_to(to: Vector4) const`
- `float dot(with: Vector4) const`
- `Vector4 floor() const`
- `Vector4 inverse() const`
- `bool is_equal_approx(to: Vector4) const`
- `bool is_finite() const`
- `bool is_normalized() const`
- `bool is_zero_approx() const`
- `float length() const`
- `float length_squared() const`
- `Vector4 lerp(to: Vector4, weight: float) const`
- `Vector4 max(with: Vector4) const`
- `int max_axis_index() const`
- `Vector4 maxf(with: float) const`
- `Vector4 min(with: Vector4) const`
- `int min_axis_index() const`
- `Vector4 minf(with: float) const`
- `Vector4 normalized() const`
- `Vector4 posmod(mod: float) const`
- `Vector4 posmodv(modv: Vector4) const`
- `Vector4 round() const`
- `Vector4 sign() const`
- `Vector4 snapped(step: Vector4) const`
- `Vector4 snappedf(step: float) const`

**GDScript Examples**
```gdscript
print(Vector4(10, 20, 30, 40) * Vector4(3, 4, 5, 6)) # Prints (30.0, 80.0, 150.0, 240.0)
```
```gdscript
print(Vector4(10, 20, 30, 40) * 2) # Prints (20.0, 40.0, 60.0, 80.0)
```
