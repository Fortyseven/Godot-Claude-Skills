# Godot 4 GDScript API Reference — Misc (Part 1)

> GDScript-only reference. 257 classes.

### @GDScript

A list of utility functions and annotations accessible from any script written in GDScript.

**Methods**
- `Color Color8(r8: int, g8: int, b8: int, a8: int = 255)`
- `void assert(condition: bool, message: String = "")`
- `String char(code: int)`
- `Variant convert(what: Variant, type: Variant.Type)`
- `Object dict_to_inst(dictionary: Dictionary)`
- `Array get_stack()`
- `Dictionary inst_to_dict(instance: Object)`
- `bool is_instance_of(value: Variant, type: Variant)`
- `int len(var: Variant)`
- `Resource load(path: String)`
- `int ord(char: String)`
- `Resource preload(path: String)`
- `void print_debug(...) vararg`
- `void print_stack()`
- `Array range(...) vararg`
- `bool type_exists(type: StringName)`

**GDScript Examples**
```gdscript
@abstract class Shape:
    @abstract func draw()

class Circle extends Shape:
    func draw():
        print("Drawing a circle.")

class Square extends Shape:
    func draw():
        print("Drawing a square.")
```
```gdscript
extends Node

enum Direction {LEFT, RIGHT, UP, DOWN}

# Built-in types.
@export var string = ""
@export var int_number = 5
@export var float_number: float = 5

# Enums.
@export var type: Variant.Type
@export var format: Image.Format
@export var direction: Direction

# Resources.
@export var image: Image
@export var custom_resource: CustomResource

# Nodes.
@export var node: Node
@export var custom_node: CustomNode

# Typed arrays.
@export var int_array: Array[int]
@export var direction_array: Array[Direction]
@export var image_array: Array[Image]
@export var node_array: Array[Node]
```

### @GlobalScope

A list of global scope enumerated constants and built-in functions. This is all that resides in the globals, constants regarding error codes, keycodes, property hints, etc.

**Properties**
- `AudioServer AudioServer`
- `CameraServer CameraServer`
- `ClassDB ClassDB`
- `DisplayServer DisplayServer`
- `EditorInterface EditorInterface`
- `Engine Engine`
- `EngineDebugger EngineDebugger`
- `GDExtensionManager GDExtensionManager`
- `Geometry2D Geometry2D`
- `Geometry3D Geometry3D`
- `IP IP`
- `Input Input`
- `InputMap InputMap`
- `JavaClassWrapper JavaClassWrapper`
- `JavaScriptBridge JavaScriptBridge`
- `Marshalls Marshalls`
- `NativeMenu NativeMenu`
- `NavigationMeshGenerator NavigationMeshGenerator`
- `NavigationServer2D NavigationServer2D`
- `NavigationServer2DManager NavigationServer2DManager`
- `NavigationServer3D NavigationServer3D`
- `NavigationServer3DManager NavigationServer3DManager`
- `OS OS`
- `Performance Performance`
- `PhysicsServer2D PhysicsServer2D`
- `PhysicsServer2DManager PhysicsServer2DManager`
- `PhysicsServer3D PhysicsServer3D`
- `PhysicsServer3DManager PhysicsServer3DManager`
- `ProjectSettings ProjectSettings`
- `RenderingServer RenderingServer`

**Methods**
- `Variant abs(x: Variant)`
- `float absf(x: float)`
- `int absi(x: int)`
- `float acos(x: float)`
- `float acosh(x: float)`
- `float angle_difference(from: float, to: float)`
- `float asin(x: float)`
- `float asinh(x: float)`
- `float atan(x: float)`
- `float atan2(y: float, x: float)`
- `float atanh(x: float)`
- `float bezier_derivative(start: float, control_1: float, control_2: float, end: float, t: float)`
- `float bezier_interpolate(start: float, control_1: float, control_2: float, end: float, t: float)`
- `Variant bytes_to_var(bytes: PackedByteArray)`
- `Variant bytes_to_var_with_objects(bytes: PackedByteArray)`
- `Variant ceil(x: Variant)`
- `float ceilf(x: float)`
- `int ceili(x: float)`
- `Variant clamp(value: Variant, min: Variant, max: Variant)`
- `float clampf(value: float, min: float, max: float)`
- `int clampi(value: int, min: int, max: int)`
- `float cos(angle_rad: float)`
- `float cosh(x: float)`
- `float cubic_interpolate(from: float, to: float, pre: float, post: float, weight: float)`
- `float cubic_interpolate_angle(from: float, to: float, pre: float, post: float, weight: float)`
- `float cubic_interpolate_angle_in_time(from: float, to: float, pre: float, post: float, weight: float, to_t: float, pre_t: float, post_t: float)`
- `float cubic_interpolate_in_time(from: float, to: float, pre: float, post: float, weight: float, to_t: float, pre_t: float, post_t: float)`
- `float db_to_linear(db: float)`
- `float deg_to_rad(deg: float)`
- `float ease(x: float, curve: float)`
- `String error_string(error: int)`
- `float exp(x: float)`
- `Variant floor(x: Variant)`
- `float floorf(x: float)`
- `int floori(x: float)`
- `float fmod(x: float, y: float)`
- `float fposmod(x: float, y: float)`
- `int hash(variable: Variant)`
- `Object instance_from_id(instance_id: int)`
- `float inverse_lerp(from: float, to: float, weight: float)`

**GDScript Examples**
```gdscript
# Array of elem_type.
hint_string = "%d:" % [elem_type]
hint_string = "%d/%d:%s" % [elem_type, elem_hint, elem_hint_string]
# Two-dimensional array of elem_type (array of arrays of elem_type).
hint_string = "%d:%d:" % [TYPE_ARRAY, elem_type]
hint_string = "%d:%d/%d:%s" % [TYPE_ARRAY, elem_type, elem_hint, elem_hint_string]
# Three-dimensional array of elem_type (array of arrays of arrays of elem_type).
hint_string = "%d:%d:%d:" % [TYPE_ARRAY, TYPE_ARRAY, elem_type]
hint_string = "%d:%d:%d/%d:%s" % [TYPE_ARRAY, TYPE_ARRAY, elem_type, elem_hint, elem_hint_string]
```
```gdscript
hint_string = "%d:" % [TYPE_INT] # Array of integers.
hint_string = "%d/%d:1,10,1" % [TYPE_INT, PROPERTY_HINT_RANGE] # Array of integers (in range from 1 to 10).
hint_string = "%d/%d:Zero,One,Two" % [TYPE_INT, PROPERTY_HINT_ENUM] # Array of integers (an enum).
hint_string = "%d/%d:Zero,One,Three:3,Six:6" % [TYPE_INT, PROPERTY_HINT_ENUM] # Array of integers (an enum).
hint_string = "%d/%d:*.png" % [TYPE_STRING, PROPERTY_HINT_FILE] # Array of strings (file paths).
hint_string = "%d/%d:Texture2D" % [TYPE_OBJECT, PROPERTY_HINT_RESOURCE_TYPE] # Array of textures.

hint_string = "%d:%d:" % [TYPE_ARR
# ...
```

### AABB

The AABB built-in Variant type represents an axis-aligned bounding box in a 3D space. It is defined by its position and size, which are Vector3. It is frequently used for fast overlap tests (see intersects()). Although AABB itself is axis-aligned, it can be combined with Transform3D to represent a rotated or skewed bounding box.

**Properties**
- `Vector3 end` = `Vector3(0, 0, 0)`
- `Vector3 position` = `Vector3(0, 0, 0)`
- `Vector3 size` = `Vector3(0, 0, 0)`

**Methods**
- `AABB abs() const`
- `bool encloses(with: AABB) const`
- `AABB expand(to_point: Vector3) const`
- `Vector3 get_center() const`
- `Vector3 get_endpoint(idx: int) const`
- `Vector3 get_longest_axis() const`
- `int get_longest_axis_index() const`
- `float get_longest_axis_size() const`
- `Vector3 get_shortest_axis() const`
- `int get_shortest_axis_index() const`
- `float get_shortest_axis_size() const`
- `Vector3 get_support(direction: Vector3) const`
- `float get_volume() const`
- `AABB grow(by: float) const`
- `bool has_point(point: Vector3) const`
- `bool has_surface() const`
- `bool has_volume() const`
- `AABB intersection(with: AABB) const`
- `bool intersects(with: AABB) const`
- `bool intersects_plane(plane: Plane) const`
- `Variant intersects_ray(from: Vector3, dir: Vector3) const`
- `Variant intersects_segment(from: Vector3, to: Vector3) const`
- `bool is_equal_approx(aabb: AABB) const`
- `bool is_finite() const`
- `AABB merge(with: AABB) const`

**GDScript Examples**
```gdscript
var box = AABB(Vector3(5, 0, 5), Vector3(-20, -10, -5))
var absolute = box.abs()
print(absolute.position) # Prints (-15.0, -10.0, 0.0)
print(absolute.size)     # Prints (20.0, 10.0, 5.0)
```
```gdscript
var a = AABB(Vector3(0, 0, 0), Vector3(4, 4, 4))
var b = AABB(Vector3(1, 1, 1), Vector3(3, 3, 3))
var c = AABB(Vector3(2, 2, 2), Vector3(8, 8, 8))

print(a.encloses(a)) # Prints true
print(a.encloses(b)) # Prints true
print(a.encloses(c)) # Prints false
```

### AStar2D
*Inherits: **RefCounted < Object***

An implementation of the A* algorithm, used to find the shortest path between two vertices on a connected graph in 2D space.

**Properties**
- `bool neighbor_filter_enabled` = `false`

**Methods**
- `float _compute_cost(from_id: int, to_id: int) virtual const`
- `float _estimate_cost(from_id: int, end_id: int) virtual const`
- `bool _filter_neighbor(from_id: int, neighbor_id: int) virtual const`
- `void add_point(id: int, position: Vector2, weight_scale: float = 1.0)`
- `bool are_points_connected(id: int, to_id: int, bidirectional: bool = true) const`
- `void clear()`
- `void connect_points(id: int, to_id: int, bidirectional: bool = true)`
- `void disconnect_points(id: int, to_id: int, bidirectional: bool = true)`
- `int get_available_point_id() const`
- `int get_closest_point(to_position: Vector2, include_disabled: bool = false) const`
- `Vector2 get_closest_position_in_segment(to_position: Vector2) const`
- `PackedInt64Array get_id_path(from_id: int, to_id: int, allow_partial_path: bool = false)`
- `int get_point_capacity() const`
- `PackedInt64Array get_point_connections(id: int)`
- `int get_point_count() const`
- `PackedInt64Array get_point_ids()`
- `PackedVector2Array get_point_path(from_id: int, to_id: int, allow_partial_path: bool = false)`
- `Vector2 get_point_position(id: int) const`
- `float get_point_weight_scale(id: int) const`
- `bool has_point(id: int) const`
- `bool is_point_disabled(id: int) const`
- `void remove_point(id: int)`
- `void reserve_space(num_nodes: int)`
- `void set_point_disabled(id: int, disabled: bool = true)`
- `void set_point_position(id: int, position: Vector2)`
- `void set_point_weight_scale(id: int, weight_scale: float)`

**GDScript Examples**
```gdscript
var astar = AStar2D.new()
astar.add_point(1, Vector2(1, 0), 4) # Adds the point (1, 0) with weight_scale 4 and id 1
```
```gdscript
var astar = AStar2D.new()
astar.add_point(1, Vector2(1, 1))
astar.add_point(2, Vector2(0, 5))
astar.connect_points(1, 2, false)
```

### AStar3D
*Inherits: **RefCounted < Object***

A* (A star) is a computer algorithm used in pathfinding and graph traversal, the process of plotting short paths among vertices (points), passing through a given set of edges (segments). It enjoys widespread use due to its performance and accuracy. Godot's A* implementation uses points in 3D space and Euclidean distances by default.

**Properties**
- `bool neighbor_filter_enabled` = `false`

**Methods**
- `float _compute_cost(from_id: int, to_id: int) virtual const`
- `float _estimate_cost(from_id: int, end_id: int) virtual const`
- `bool _filter_neighbor(from_id: int, neighbor_id: int) virtual const`
- `void add_point(id: int, position: Vector3, weight_scale: float = 1.0)`
- `bool are_points_connected(id: int, to_id: int, bidirectional: bool = true) const`
- `void clear()`
- `void connect_points(id: int, to_id: int, bidirectional: bool = true)`
- `void disconnect_points(id: int, to_id: int, bidirectional: bool = true)`
- `int get_available_point_id() const`
- `int get_closest_point(to_position: Vector3, include_disabled: bool = false) const`
- `Vector3 get_closest_position_in_segment(to_position: Vector3) const`
- `PackedInt64Array get_id_path(from_id: int, to_id: int, allow_partial_path: bool = false)`
- `int get_point_capacity() const`
- `PackedInt64Array get_point_connections(id: int)`
- `int get_point_count() const`
- `PackedInt64Array get_point_ids()`
- `PackedVector3Array get_point_path(from_id: int, to_id: int, allow_partial_path: bool = false)`
- `Vector3 get_point_position(id: int) const`
- `float get_point_weight_scale(id: int) const`
- `bool has_point(id: int) const`
- `bool is_point_disabled(id: int) const`
- `void remove_point(id: int)`
- `void reserve_space(num_nodes: int)`
- `void set_point_disabled(id: int, disabled: bool = true)`
- `void set_point_position(id: int, position: Vector3)`
- `void set_point_weight_scale(id: int, weight_scale: float)`

**GDScript Examples**
```gdscript
class_name MyAStar3D
extends AStar3D

func _compute_cost(u, v):
    var u_pos = get_point_position(u)
    var v_pos = get_point_position(v)
    return abs(u_pos.x - v_pos.x) + abs(u_pos.y - v_pos.y) + abs(u_pos.z - v_pos.z)

func _estimate_cost(u, v):
    var u_pos = get_point_position(u)
    var v_pos = get_point_position(v)
    return abs(u_pos.x - v_pos.x) + abs(u_pos.y - v_pos.y) + abs(u_pos.z - v_pos.z)
```
```gdscript
var astar = AStar3D.new()
astar.add_point(1, Vector3(1, 0, 0), 4) # Adds the point (1, 0, 0) with weight_scale 4 and id 1
```

### AStarGrid2D
*Inherits: **RefCounted < Object***

AStarGrid2D is a variant of AStar2D that is specialized for partial 2D grids. It is simpler to use because it doesn't require you to manually create points and connect them together. This class also supports multiple types of heuristics, modes for diagonal movement, and a jumping mode to speed up calculations.

**Properties**
- `CellShape cell_shape` = `0`
- `Vector2 cell_size` = `Vector2(1, 1)`
- `Heuristic default_compute_heuristic` = `0`
- `Heuristic default_estimate_heuristic` = `0`
- `DiagonalMode diagonal_mode` = `0`
- `bool jumping_enabled` = `false`
- `Vector2 offset` = `Vector2(0, 0)`
- `Rect2i region` = `Rect2i(0, 0, 0, 0)`
- `Vector2i size` = `Vector2i(0, 0)`

**Methods**
- `float _compute_cost(from_id: Vector2i, to_id: Vector2i) virtual const`
- `float _estimate_cost(from_id: Vector2i, end_id: Vector2i) virtual const`
- `void clear()`
- `void fill_solid_region(region: Rect2i, solid: bool = true)`
- `void fill_weight_scale_region(region: Rect2i, weight_scale: float)`
- `Array[Vector2i] get_id_path(from_id: Vector2i, to_id: Vector2i, allow_partial_path: bool = false)`
- `Array[Dictionary] get_point_data_in_region(region: Rect2i) const`
- `PackedVector2Array get_point_path(from_id: Vector2i, to_id: Vector2i, allow_partial_path: bool = false)`
- `Vector2 get_point_position(id: Vector2i) const`
- `float get_point_weight_scale(id: Vector2i) const`
- `bool is_dirty() const`
- `bool is_in_bounds(x: int, y: int) const`
- `bool is_in_boundsv(id: Vector2i) const`
- `bool is_point_solid(id: Vector2i) const`
- `void set_point_solid(id: Vector2i, solid: bool = true)`
- `void set_point_weight_scale(id: Vector2i, weight_scale: float)`
- `void update()`

**GDScript Examples**
```gdscript
var astar_grid = AStarGrid2D.new()
astar_grid.region = Rect2i(0, 0, 32, 32)
astar_grid.cell_size = Vector2(16, 16)
astar_grid.update()
print(astar_grid.get_id_path(Vector2i(0, 0), Vector2i(3, 4))) # Prints [(0, 0), (1, 1), (2, 2), (3, 3), (3, 4)]
print(astar_grid.get_point_path(Vector2i(0, 0), Vector2i(3, 4))) # Prints [(0, 0), (16, 16), (32, 32), (48, 48), (48, 64)]
```
```gdscript
dx = abs(to_id.x - from_id.x)
dy = abs(to_id.y - from_id.y)
result = sqrt(dx * dx + dy * dy)
```

### AnimatedSprite3D
*Inherits: **SpriteBase3D < GeometryInstance3D < VisualInstance3D < Node3D < Node < Object***

AnimatedSprite3D is similar to the Sprite3D node, except it carries multiple textures as animation sprite_frames. Animations are created using a SpriteFrames resource, which allows you to import image files (or a folder containing said files) to provide the animation frames for the sprite. The SpriteFrames resource can be configured in the editor via the SpriteFrames bottom panel.

**Properties**
- `StringName animation` = `&"default"`
- `String autoplay` = `""`
- `int frame` = `0`
- `float frame_progress` = `0.0`
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

### ArrayOccluder3D
*Inherits: **Occluder3D < Resource < RefCounted < Object***

ArrayOccluder3D stores an arbitrary 3D polygon shape that can be used by the engine's occlusion culling system. This is analogous to ArrayMesh, but for occluders.

**Properties**
- `PackedInt32Array indices` = `PackedInt32Array()`
- `PackedVector3Array vertices` = `PackedVector3Array()`

**Methods**
- `void set_arrays(vertices: PackedVector3Array, indices: PackedInt32Array)`

### Array

An array data structure that can contain a sequence of elements of any Variant type by default. Values can optionally be constrained to a specific type by creating a typed array. Elements are accessed by a numerical index starting at 0. Negative indices are used to count from the back (-1 is the last element, -2 is the second to last, etc.).

**Methods**
- `bool all(method: Callable) const`
- `bool any(method: Callable) const`
- `void append(value: Variant)`
- `void append_array(array: Array)`
- `void assign(array: Array)`
- `Variant back() const`
- `int bsearch(value: Variant, before: bool = true) const`
- `int bsearch_custom(value: Variant, func: Callable, before: bool = true) const`
- `void clear()`
- `int count(value: Variant) const`
- `Array duplicate(deep: bool = false) const`
- `Array duplicate_deep(deep_subresources_mode: int = 1) const`
- `void erase(value: Variant)`
- `void fill(value: Variant)`
- `Array filter(method: Callable) const`
- `int find(what: Variant, from: int = 0) const`
- `int find_custom(method: Callable, from: int = 0) const`
- `Variant front() const`
- `Variant get(index: int) const`
- `int get_typed_builtin() const`
- `StringName get_typed_class_name() const`
- `Variant get_typed_script() const`
- `bool has(value: Variant) const`
- `int hash() const`
- `int insert(position: int, value: Variant)`
- `bool is_empty() const`
- `bool is_read_only() const`
- `bool is_same_typed(array: Array) const`
- `bool is_typed() const`
- `void make_read_only()`
- `Array map(method: Callable) const`
- `Variant max() const`
- `Variant min() const`
- `Variant pick_random() const`
- `Variant pop_at(position: int)`
- `Variant pop_back()`
- `Variant pop_front()`
- `void push_back(value: Variant)`
- `void push_front(value: Variant)`
- `Variant reduce(method: Callable, accum: Variant = null) const`

**GDScript Examples**
```gdscript
var array = ["First", 2, 3, "Last"]
print(array[0])  # Prints "First"
print(array[2])  # Prints 3
print(array[-1]) # Prints "Last"

array[1] = "Second"
print(array[1])  # Prints "Second"
print(array[-3]) # Prints "Second"

# This typed array can only contain integers.
# Attempting to add any other type will result in an error.
var typed_array: Array[int] = [1, 2, 3]
```
```gdscript
func greater_than_5(number):
    return number > 5

func _ready():
    print([6, 10, 6].all(greater_than_5)) # Prints true (3/3 elements evaluate to true).
    print([4, 10, 4].all(greater_than_5)) # Prints false (1/3 elements evaluate to true).
    print([4, 4, 4].all(greater_than_5))  # Prints false (0/3 elements evaluate to true).
    print([].all(greater_than_5))         # Prints true (0/0 elements evaluate to true).

    # Same as the first line above, but using a lambda function.
    print([6, 10, 6].all(func(element): return element > 5)) # Prints true
```

### AudioListener2D
*Inherits: **Node2D < CanvasItem < Node < Object***

Once added to the scene tree and enabled using make_current(), this node will override the location sounds are heard from. Only one AudioListener2D can be current. Using make_current() will disable the previous AudioListener2D.

**Methods**
- `void clear_current()`
- `bool is_current() const`
- `void make_current()`

### AudioListener3D
*Inherits: **Node3D < Node < Object***

Once added to the scene tree and enabled using make_current(), this node will override the location sounds are heard from. This can be used to listen from a location different from the Camera3D.

**Properties**
- `DopplerTracking doppler_tracking` = `0`

**Methods**
- `void clear_current()`
- `Transform3D get_listener_transform() const`
- `bool is_current() const`
- `void make_current()`

### AudioSamplePlayback
*Inherits: **RefCounted < Object***

Meta class for playing back audio samples.

### AudioSample
*Inherits: **RefCounted < Object***

Base class for audio samples.

### BackBufferCopy
*Inherits: **Node2D < CanvasItem < Node < Object***

Node for back-buffering the currently-displayed screen. The region defined in the BackBufferCopy node is buffered with the content of the screen it covers, or the entire screen according to the copy_mode. It can be accessed in shader scripts using the screen texture (i.e. a uniform sampler with hint_screen_texture).

**Properties**
- `CopyMode copy_mode` = `1`
- `Rect2 rect` = `Rect2(-100, -100, 200, 200)`

### Basis

The Basis built-in Variant type is a 3×3 matrix used to represent 3D rotation, scale, and shear. It is frequently used within a Transform3D.

**Properties**
- `Vector3 x` = `Vector3(1, 0, 0)`
- `Vector3 y` = `Vector3(0, 1, 0)`
- `Vector3 z` = `Vector3(0, 0, 1)`

**Methods**
- `float determinant() const`
- `Basis from_euler(euler: Vector3, order: int = 2) static`
- `Basis from_scale(scale: Vector3) static`
- `Vector3 get_euler(order: int = 2) const`
- `Quaternion get_rotation_quaternion() const`
- `Vector3 get_scale() const`
- `Basis inverse() const`
- `bool is_conformal() const`
- `bool is_equal_approx(b: Basis) const`
- `bool is_finite() const`
- `Basis looking_at(target: Vector3, up: Vector3 = Vector3(0, 1, 0), use_model_front: bool = false) static`
- `Basis orthonormalized() const`
- `Basis rotated(axis: Vector3, angle: float) const`
- `Basis scaled(scale: Vector3) const`
- `Basis scaled_local(scale: Vector3) const`
- `Basis slerp(to: Basis, weight: float) const`
- `float tdotx(with: Vector3) const`
- `float tdoty(with: Vector3) const`
- `float tdotz(with: Vector3) const`
- `Basis transposed() const`

**GDScript Examples**
```gdscript
# Creates a Basis whose z axis points down.
var my_basis = Basis.from_euler(Vector3(TAU / 4, 0, 0))

print(my_basis.z) # Prints (0.0, -1.0, 0.0)
```
```gdscript
var my_basis = Basis.from_scale(Vector3(2, 4, 8))

print(my_basis.x) # Prints (2.0, 0.0, 0.0)
print(my_basis.y) # Prints (0.0, 4.0, 0.0)
print(my_basis.z) # Prints (0.0, 0.0, 8.0)
```

### Bone2D
*Inherits: **Node2D < CanvasItem < Node < Object***

A hierarchy of Bone2Ds can be bound to a Skeleton2D to control and animate other Node2D nodes.

**Properties**
- `Transform2D rest` = `Transform2D(0, 0, 0, 0, 0, 0)`

**Methods**
- `void apply_rest()`
- `bool get_autocalculate_length_and_angle() const`
- `float get_bone_angle() const`
- `int get_index_in_skeleton() const`
- `float get_length() const`
- `Transform2D get_skeleton_rest() const`
- `void set_autocalculate_length_and_angle(auto_calculate: bool)`
- `void set_bone_angle(angle: float)`
- `void set_length(length: float)`

### BoneConstraint3D
*Inherits: **SkeletonModifier3D < Node3D < Node < Object** | Inherited by: AimModifier3D, ConvertTransformModifier3D, CopyTransformModifier3D*

Base class of SkeletonModifier3D that modifies the bone set in set_apply_bone() based on the transform of the bone retrieved by get_reference_bone().

**Methods**
- `void clear_setting()`
- `float get_amount(index: int) const`
- `int get_apply_bone(index: int) const`
- `String get_apply_bone_name(index: int) const`
- `int get_reference_bone(index: int) const`
- `String get_reference_bone_name(index: int) const`
- `NodePath get_reference_node(index: int) const`
- `ReferenceType get_reference_type(index: int) const`
- `int get_setting_count() const`
- `void set_amount(index: int, amount: float)`
- `void set_apply_bone(index: int, bone: int)`
- `void set_apply_bone_name(index: int, bone_name: String)`
- `void set_reference_bone(index: int, bone: int)`
- `void set_reference_bone_name(index: int, bone_name: String)`
- `void set_reference_node(index: int, node: NodePath)`
- `void set_reference_type(index: int, type: ReferenceType)`
- `void set_setting_count(count: int)`

### BoneMap
*Inherits: **Resource < RefCounted < Object***

This class contains a dictionary that uses a list of bone names in SkeletonProfile as key names.

**Properties**
- `SkeletonProfile profile`

**Methods**
- `StringName find_profile_bone_name(skeleton_bone_name: StringName) const`
- `StringName get_skeleton_bone_name(profile_bone_name: StringName) const`
- `void set_skeleton_bone_name(profile_bone_name: StringName, skeleton_bone_name: StringName)`

### BoneTwistDisperser3D
*Inherits: **SkeletonModifier3D < Node3D < Node < Object***

This BoneTwistDisperser3D allows for smooth twist interpolation between multiple bones by dispersing the end bone's twist to the parents. This only changes the twist without changing the global position of each joint.

**Properties**
- `bool mutable_bone_axes` = `true`
- `int setting_count` = `0`

**Methods**
- `void clear_settings()`
- `Curve get_damping_curve(index: int) const`
- `DisperseMode get_disperse_mode(index: int) const`
- `int get_end_bone(index: int) const`
- `BoneDirection get_end_bone_direction(index: int) const`
- `String get_end_bone_name(index: int) const`
- `int get_joint_bone(index: int, joint: int) const`
- `String get_joint_bone_name(index: int, joint: int) const`
- `int get_joint_count(index: int) const`
- `float get_joint_twist_amount(index: int, joint: int) const`
- `int get_reference_bone(index: int) const`
- `String get_reference_bone_name(index: int) const`
- `int get_root_bone(index: int) const`
- `String get_root_bone_name(index: int) const`
- `Quaternion get_twist_from(index: int) const`
- `float get_weight_position(index: int) const`
- `bool is_end_bone_extended(index: int) const`
- `bool is_twist_from_rest(index: int) const`
- `void set_damping_curve(index: int, curve: Curve)`
- `void set_disperse_mode(index: int, disperse_mode: DisperseMode)`
- `void set_end_bone(index: int, bone: int)`
- `void set_end_bone_direction(index: int, bone_direction: BoneDirection)`
- `void set_end_bone_name(index: int, bone_name: String)`
- `void set_extend_end_bone(index: int, enabled: bool)`
- `void set_joint_twist_amount(index: int, joint: int, twist_amount: float)`
- `void set_root_bone(index: int, bone: int)`
- `void set_root_bone_name(index: int, bone_name: String)`
- `void set_twist_from(index: int, from: Quaternion)`
- `void set_twist_from_rest(index: int, enabled: bool)`
- `void set_weight_position(index: int, weight_position: float)`

### BoxOccluder3D
*Inherits: **Occluder3D < Resource < RefCounted < Object***

BoxOccluder3D stores a cuboid shape that can be used by the engine's occlusion culling system.

**Properties**
- `Vector3 size` = `Vector3(1, 1, 1)`

### BoxShape3D
*Inherits: **Shape3D < Resource < RefCounted < Object***

A 3D box shape, intended for use in physics. Usually used to provide a shape for a CollisionShape3D.

**Properties**
- `Vector3 size` = `Vector3(1, 1, 1)`

### CCDIK3D
*Inherits: **IterateIK3D < ChainIK3D < IKModifier3D < SkeletonModifier3D < Node3D < Node < Object***

CCDIK3D is rotation based IK, enabling fast and effective tracking even with large joint rotations. It's especially suitable for chains with limitations, providing smoother and more stable target tracking compared to FABRIK3D.

### CPUParticles3D
*Inherits: **GeometryInstance3D < VisualInstance3D < Node3D < Node < Object***

CPU-based 3D particle node used to create a variety of particle systems and effects.

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
- `Vector3 direction` = `Vector3(1, 0, 0)`
- `DrawOrder draw_order` = `0`
- `Vector3 emission_box_extents`
- `PackedColorArray emission_colors` = `PackedColorArray()`
- `PackedVector3Array emission_normals`
- `PackedVector3Array emission_points`
- `Vector3 emission_ring_axis`
- `float emission_ring_cone_angle`
- `float emission_ring_height`
- `float emission_ring_inner_radius`
- `float emission_ring_radius`

**Methods**
- `AABB capture_aabb() const`
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

### CSGBox3D
*Inherits: **CSGPrimitive3D < CSGShape3D < GeometryInstance3D < VisualInstance3D < Node3D < Node < Object***

This node allows you to create a box for use with the CSG system.

**Properties**
- `Material material`
- `Vector3 size` = `Vector3(1, 1, 1)`

### CSGCombiner3D
*Inherits: **CSGShape3D < GeometryInstance3D < VisualInstance3D < Node3D < Node < Object***

For complex arrangements of shapes, it is sometimes needed to add structure to your CSG nodes. The CSGCombiner3D node allows you to create this structure. The node encapsulates the result of the CSG operations of its children. In this way, it is possible to do operations on one set of shapes that are children of one CSGCombiner3D node, and a set of separate operations on a second set of shapes that are children of a second CSGCombiner3D node, and then do an operation that takes the two end results as its input to create the final shape.

### CSGCylinder3D
*Inherits: **CSGPrimitive3D < CSGShape3D < GeometryInstance3D < VisualInstance3D < Node3D < Node < Object***

This node allows you to create a cylinder (or cone) for use with the CSG system.

**Properties**
- `bool cone` = `false`
- `float height` = `2.0`
- `Material material`
- `float radius` = `0.5`
- `int sides` = `8`
- `bool smooth_faces` = `true`

### CSGMesh3D
*Inherits: **CSGPrimitive3D < CSGShape3D < GeometryInstance3D < VisualInstance3D < Node3D < Node < Object***

This CSG node allows you to use any mesh resource as a CSG shape, provided it is manifold. A manifold shape is closed, does not self-intersect, does not contain internal faces and has no edges that connect to more than two faces. See also CSGPolygon3D for drawing 2D extruded polygons to be used as CSG nodes.

**Properties**
- `Material material`
- `Mesh mesh`

### CSGPolygon3D
*Inherits: **CSGPrimitive3D < CSGShape3D < GeometryInstance3D < VisualInstance3D < Node3D < Node < Object***

An array of 2D points is extruded to quickly and easily create a variety of 3D meshes. See also CSGMesh3D for using 3D meshes as CSG nodes.

**Properties**
- `float depth` = `1.0`
- `Material material`
- `Mode mode` = `0`
- `bool path_continuous_u`
- `float path_interval`
- `PathIntervalType path_interval_type`
- `bool path_joined`
- `bool path_local`
- `NodePath path_node`
- `PathRotation path_rotation`
- `bool path_rotation_accurate`
- `float path_simplify_angle`
- `float path_u_distance`
- `PackedVector2Array polygon` = `PackedVector2Array(0, 0, 0, 1, 1, 1, 1, 0)`
- `bool smooth_faces` = `false`
- `float spin_degrees`
- `int spin_sides`

### CSGPrimitive3D
*Inherits: **CSGShape3D < GeometryInstance3D < VisualInstance3D < Node3D < Node < Object** | Inherited by: CSGBox3D, CSGCylinder3D, CSGMesh3D, CSGPolygon3D, CSGSphere3D, CSGTorus3D*

Parent class for various CSG primitives. It contains code and functionality that is common between them. It cannot be used directly. Instead use one of the various classes that inherit from it.

**Properties**
- `bool flip_faces` = `false`

### CSGShape3D
*Inherits: **GeometryInstance3D < VisualInstance3D < Node3D < Node < Object** | Inherited by: CSGCombiner3D, CSGPrimitive3D*

This is the CSG base class that provides CSG operation support to the various CSG nodes in Godot.

**Properties**
- `bool calculate_tangents` = `true`
- `int collision_layer` = `1`
- `int collision_mask` = `1`
- `float collision_priority` = `1.0`
- `Operation operation` = `0`
- `float snap`
- `bool use_collision` = `false`

**Methods**
- `ConcavePolygonShape3D bake_collision_shape()`
- `ArrayMesh bake_static_mesh()`
- `bool get_collision_layer_value(layer_number: int) const`
- `bool get_collision_mask_value(layer_number: int) const`
- `Array get_meshes() const`
- `bool is_root_shape() const`
- `void set_collision_layer_value(layer_number: int, value: bool)`
- `void set_collision_mask_value(layer_number: int, value: bool)`

### CSGSphere3D
*Inherits: **CSGPrimitive3D < CSGShape3D < GeometryInstance3D < VisualInstance3D < Node3D < Node < Object***

This node allows you to create a sphere for use with the CSG system.

**Properties**
- `Material material`
- `int radial_segments` = `12`
- `float radius` = `0.5`
- `int rings` = `6`
- `bool smooth_faces` = `true`

### CSGTorus3D
*Inherits: **CSGPrimitive3D < CSGShape3D < GeometryInstance3D < VisualInstance3D < Node3D < Node < Object***

This node allows you to create a torus for use with the CSG system.

**Properties**
- `float inner_radius` = `0.5`
- `Material material`
- `float outer_radius` = `1.0`
- `int ring_sides` = `6`
- `int sides` = `8`
- `bool smooth_faces` = `true`

### Callable

Callable is a built-in Variant type that represents a function. It can either be a method within an Object instance, or a custom callable used for different purposes (see is_custom()). Like all Variant types, it can be stored in variables and passed to other functions. It is most commonly used for signal callbacks.

**Methods**
- `Callable bind(...) vararg const`
- `Callable bindv(arguments: Array)`
- `Variant call(...) vararg const`
- `void call_deferred(...) vararg const`
- `Variant callv(arguments: Array) const`
- `Callable create(variant: Variant, method: StringName) static`
- `int get_argument_count() const`
- `Array get_bound_arguments() const`
- `int get_bound_arguments_count() const`
- `StringName get_method() const`
- `Object get_object() const`
- `int get_object_id() const`
- `int get_unbound_arguments_count() const`
- `int hash() const`
- `bool is_custom() const`
- `bool is_null() const`
- `bool is_standard() const`
- `bool is_valid() const`
- `void rpc(...) vararg const`
- `void rpc_id(peer_id: int, ...) vararg const`
- `Callable unbind(argcount: int) const`

**GDScript Examples**
```gdscript
func print_args(arg1, arg2, arg3 = ""):
    prints(arg1, arg2, arg3)

func test():
    var callable = Callable(self, "print_args")
    callable.call("hello", "world")  # Prints "hello world ".
    callable.call(Vector2.UP, 42, callable)  # Prints "(0.0, -1.0) 42 Node(node.gd)::print_args"
    callable.call("invalid")  # Invalid call, should have at least 2 arguments.
```
```gdscript
func _ready():
    grab_focus.call_deferred()
```

### CameraFeed
*Inherits: **RefCounted < Object***

A camera feed gives you access to a single physical camera attached to your device. When enabled, Godot will start capturing frames from the camera which can then be used. See also CameraServer.

**Properties**
- `bool feed_is_active` = `false`
- `Transform2D feed_transform` = `Transform2D(1, 0, 0, -1, 0, 1)`
- `Array formats` = `[]`

**Methods**
- `bool _activate_feed() virtual`
- `void _deactivate_feed() virtual`
- `FeedDataType get_datatype() const`
- `int get_id() const`
- `String get_name() const`
- `FeedPosition get_position() const`
- `int get_texture_tex_id(feed_image_type: FeedImage)`
- `void set_external(width: int, height: int)`
- `bool set_format(index: int, parameters: Dictionary)`
- `void set_name(name: String)`
- `void set_position(position: FeedPosition)`
- `void set_rgb_image(rgb_image: Image)`
- `void set_ycbcr_image(ycbcr_image: Image)`
- `void set_ycbcr_images(y_image: Image, cbcr_image: Image)`

### CameraServer
*Inherits: **Object***

The CameraServer keeps track of different cameras accessible in Godot. These are external cameras such as webcams or the cameras on your phone.

**Properties**
- `bool monitoring_feeds` = `false`

**Methods**
- `void add_feed(feed: CameraFeed)`
- `Array[CameraFeed] feeds()`
- `CameraFeed get_feed(index: int)`
- `int get_feed_count()`
- `void remove_feed(feed: CameraFeed)`

**GDScript Examples**
```gdscript
func _ready():
    CameraServer.camera_feeds_updated.connect(_on_camera_feeds_updated)
    CameraServer.monitoring_feeds = true

func _on_camera_feeds_updated():
    var feeds = CameraServer.feeds()
```

### CanvasGroup
*Inherits: **Node2D < CanvasItem < Node < Object***

Child CanvasItem nodes of a CanvasGroup are drawn as a single object. It allows to e.g. draw overlapping translucent 2D nodes without causing the overlapping sections to be more opaque than intended (set the CanvasItem.self_modulate property on the CanvasGroup to achieve this effect).

**Properties**
- `float clear_margin` = `10.0`
- `float fit_margin` = `10.0`
- `bool use_mipmaps` = `false`

**GDScript Examples**
```gdscript
shader_type canvas_item;
render_mode unshaded;

uniform sampler2D screen_texture : hint_screen_texture, repeat_disable, filter_nearest;

void fragment() {
    vec4 c = textureLod(screen_texture, SCREEN_UV, 0.0);

    if (c.a > 0.0001) {
        c.rgb /= c.a;
    }

    COLOR *= c;
}
```

### CanvasTexture
*Inherits: **Texture2D < Texture < Resource < RefCounted < Object***

CanvasTexture is an alternative to ImageTexture for 2D rendering. It allows using normal maps and specular maps in any node that inherits from CanvasItem. CanvasTexture also allows overriding the texture's filter and repeat mode independently of the node's properties (or the project settings).

**Properties**
- `Texture2D diffuse_texture`
- `Texture2D normal_texture`
- `bool resource_local_to_scene` = `false (overrides Resource)`
- `Color specular_color` = `Color(1, 1, 1, 1)`
- `float specular_shininess` = `1.0`
- `Texture2D specular_texture`
- `TextureFilter texture_filter` = `0`
- `TextureRepeat texture_repeat` = `0`

### CapsuleShape2D
*Inherits: **Shape2D < Resource < RefCounted < Object***

A 2D capsule shape, intended for use in physics. Usually used to provide a shape for a CollisionShape2D.

**Properties**
- `float height` = `30.0`
- `float mid_height`
- `float radius` = `10.0`

### CapsuleShape3D
*Inherits: **Shape3D < Resource < RefCounted < Object***

A 3D capsule shape, intended for use in physics. Usually used to provide a shape for a CollisionShape3D.

**Properties**
- `float height` = `2.0`
- `float mid_height`
- `float radius` = `0.5`

### ChainIK3D
*Inherits: **IKModifier3D < SkeletonModifier3D < Node3D < Node < Object** | Inherited by: IterateIK3D, SplineIK3D*

Base class of SkeletonModifier3D that automatically generates a joint list from the bones between the root bone and the end bone.

**Methods**
- `int get_end_bone(index: int) const`
- `BoneDirection get_end_bone_direction(index: int) const`
- `float get_end_bone_length(index: int) const`
- `String get_end_bone_name(index: int) const`
- `int get_joint_bone(index: int, joint: int) const`
- `String get_joint_bone_name(index: int, joint: int) const`
- `int get_joint_count(index: int) const`
- `int get_root_bone(index: int) const`
- `String get_root_bone_name(index: int) const`
- `bool is_end_bone_extended(index: int) const`
- `void set_end_bone(index: int, bone: int)`
- `void set_end_bone_direction(index: int, bone_direction: BoneDirection)`
- `void set_end_bone_length(index: int, length: float)`
- `void set_end_bone_name(index: int, bone_name: String)`
- `void set_extend_end_bone(index: int, enabled: bool)`
- `void set_root_bone(index: int, bone: int)`
- `void set_root_bone_name(index: int, bone_name: String)`

### CharFXTransform
*Inherits: **RefCounted < Object***

By setting various properties on this object, you can control how individual characters will be displayed in a RichTextEffect.

**Properties**
- `Color color` = `Color(0, 0, 0, 1)`
- `float elapsed_time` = `0.0`
- `Dictionary env` = `{}`
- `RID font` = `RID()`
- `int glyph_count` = `0`
- `int glyph_flags` = `0`
- `int glyph_index` = `0`
- `Vector2 offset` = `Vector2(0, 0)`
- `bool outline` = `false`
- `Vector2i range` = `Vector2i(0, 0)`
- `int relative_index` = `0`
- `Transform2D transform` = `Transform2D(1, 0, 0, 1, 0, 0)`
- `bool visible` = `true`

**GDScript Examples**
```gdscript
{"foo": "hello", "bar": true, "baz": 42, "color": Color(1, 1, 1, 1)}
```

### CircleShape2D
*Inherits: **Shape2D < Resource < RefCounted < Object***

A 2D circle shape, intended for use in physics. Usually used to provide a shape for a CollisionShape2D.

**Properties**
- `float radius` = `10.0`

### CodeHighlighter
*Inherits: **SyntaxHighlighter < Resource < RefCounted < Object***

By adjusting various properties of this resource, you can change the colors of strings, comments, numbers, and other text patterns inside a TextEdit control.

**Properties**
- `Dictionary color_regions` = `{}`
- `Color function_color` = `Color(0, 0, 0, 1)`
- `Dictionary keyword_colors` = `{}`
- `Dictionary member_keyword_colors` = `{}`
- `Color member_variable_color` = `Color(0, 0, 0, 1)`
- `Color number_color` = `Color(0, 0, 0, 1)`
- `Color symbol_color` = `Color(0, 0, 0, 1)`

**Methods**
- `void add_color_region(start_key: String, end_key: String, color: Color, line_only: bool = false)`
- `void add_keyword_color(keyword: String, color: Color)`
- `void add_member_keyword_color(member_keyword: String, color: Color)`
- `void clear_color_regions()`
- `void clear_keyword_colors()`
- `void clear_member_keyword_colors()`
- `Color get_keyword_color(keyword: String) const`
- `Color get_member_keyword_color(member_keyword: String) const`
- `bool has_color_region(start_key: String) const`
- `bool has_keyword_color(keyword: String) const`
- `bool has_member_keyword_color(member_keyword: String) const`
- `void remove_color_region(start_key: String)`
- `void remove_keyword_color(keyword: String)`
- `void remove_member_keyword_color(member_keyword: String)`

### CollisionObject3D
*Inherits: **Node3D < Node < Object** | Inherited by: Area3D, PhysicsBody3D*

Abstract base class for 3D physics objects. CollisionObject3D can hold any number of Shape3Ds for collision. Each shape must be assigned to a shape owner. Shape owners are not nodes and do not appear in the editor, but are accessible through code using the shape_owner_* methods.

**Properties**
- `int collision_layer` = `1`
- `int collision_mask` = `1`
- `float collision_priority` = `1.0`
- `DisableMode disable_mode` = `0`
- `bool input_capture_on_drag` = `false`
- `bool input_ray_pickable` = `true`

**Methods**
- `void _input_event(camera: Camera3D, event: InputEvent, event_position: Vector3, normal: Vector3, shape_idx: int) virtual`
- `void _mouse_enter() virtual`
- `void _mouse_exit() virtual`
- `int create_shape_owner(owner: Object)`
- `bool get_collision_layer_value(layer_number: int) const`
- `bool get_collision_mask_value(layer_number: int) const`
- `RID get_rid() const`
- `PackedInt32Array get_shape_owners()`
- `bool is_shape_owner_disabled(owner_id: int) const`
- `void remove_shape_owner(owner_id: int)`
- `void set_collision_layer_value(layer_number: int, value: bool)`
- `void set_collision_mask_value(layer_number: int, value: bool)`
- `int shape_find_owner(shape_index: int) const`
- `void shape_owner_add_shape(owner_id: int, shape: Shape3D)`
- `void shape_owner_clear_shapes(owner_id: int)`
- `Object shape_owner_get_owner(owner_id: int) const`
- `Shape3D shape_owner_get_shape(owner_id: int, shape_id: int) const`
- `int shape_owner_get_shape_count(owner_id: int) const`
- `int shape_owner_get_shape_index(owner_id: int, shape_id: int) const`
- `Transform3D shape_owner_get_transform(owner_id: int) const`
- `void shape_owner_remove_shape(owner_id: int, shape_id: int)`
- `void shape_owner_set_disabled(owner_id: int, disabled: bool)`
- `void shape_owner_set_transform(owner_id: int, transform: Transform3D)`

### ColorPalette
*Inherits: **Resource < RefCounted < Object***

The ColorPalette resource is designed to store and manage a collection of colors. This resource is useful in scenarios where a predefined set of colors is required, such as for creating themes, designing user interfaces, or managing game assets. The built-in ColorPicker control can also make use of ColorPalette without additional code.

**Properties**
- `PackedColorArray colors` = `PackedColorArray()`

### Color

A color represented in RGBA format by a red (r), green (g), blue (b), and alpha (a) component. Each component is a 32-bit floating-point value, usually ranging from 0.0 to 1.0. Some properties (such as CanvasItem.modulate) may support values greater than 1.0, for overbright or HDR (High Dynamic Range) colors.

**Properties**
- `float a` = `1.0`
- `int a8` = `255`
- `float b` = `0.0`
- `int b8` = `0`
- `float g` = `0.0`
- `int g8` = `0`
- `float h` = `0.0`
- `float ok_hsl_h` = `0.0`
- `float ok_hsl_l` = `0.0`
- `float ok_hsl_s` = `0.0`
- `float r` = `0.0`
- `int r8` = `0`
- `float s` = `0.0`
- `float v` = `0.0`

**Methods**
- `Color blend(over: Color) const`
- `Color clamp(min: Color = Color(0, 0, 0, 0), max: Color = Color(1, 1, 1, 1)) const`
- `Color darkened(amount: float) const`
- `Color from_hsv(h: float, s: float, v: float, alpha: float = 1.0) static`
- `Color from_ok_hsl(h: float, s: float, l: float, alpha: float = 1.0) static`
- `Color from_rgba8(r8: int, g8: int, b8: int, a8: int = 255) static`
- `Color from_rgbe9995(rgbe: int) static`
- `Color from_string(str: String, default: Color) static`
- `float get_luminance() const`
- `Color hex(hex: int) static`
- `Color hex64(hex: int) static`
- `Color html(rgba: String) static`
- `bool html_is_valid(color: String) static`
- `Color inverted() const`
- `bool is_equal_approx(to: Color) const`
- `Color lerp(to: Color, weight: float) const`
- `Color lightened(amount: float) const`
- `Color linear_to_srgb() const`
- `Color srgb_to_linear() const`
- `int to_abgr32() const`
- `int to_abgr64() const`
- `int to_argb32() const`
- `int to_argb64() const`
- `String to_html(with_alpha: bool = true) const`
- `int to_rgba32() const`
- `int to_rgba64() const`

**GDScript Examples**
```gdscript
var red = Color(Color.RED, 0.2) # 20% opaque red.
```
```gdscript
var color = Color(0.2, 1.0, 0.7) # Similar to `Color.from_rgba8(51, 255, 178, 255)`
```

### CompressedCubemapArray
*Inherits: **CompressedTextureLayered < TextureLayered < Texture < Resource < RefCounted < Object***

A cubemap array that is loaded from a .ccubearray file. This file format is internal to Godot; it is created by importing other image formats with the import system. CompressedCubemapArray can use one of 4 compression methods:

### CompressedCubemap
*Inherits: **CompressedTextureLayered < TextureLayered < Texture < Resource < RefCounted < Object***

A cubemap that is loaded from a .ccube file. This file format is internal to Godot; it is created by importing other image formats with the import system. CompressedCubemap can use one of 4 compression methods:

### CompressedTexture3D
*Inherits: **Texture3D < Texture < Resource < RefCounted < Object***

CompressedTexture3D is the VRAM-compressed counterpart of ImageTexture3D. The file extension for CompressedTexture3D files is .ctex3d. This file format is internal to Godot; it is created by importing other image formats with the import system.

**Properties**
- `String load_path` = `""`

**Methods**
- `Error load(path: String)`

### CompressedTextureLayered
*Inherits: **TextureLayered < Texture < Resource < RefCounted < Object** | Inherited by: CompressedCubemap, CompressedCubemapArray, CompressedTexture2DArray*

Base class for CompressedTexture2DArray and CompressedTexture3D. Cannot be used directly, but contains all the functions necessary for accessing the derived resource types. See also TextureLayered.

**Properties**
- `String load_path` = `""`

**Methods**
- `Error load(path: String)`

### ConcavePolygonShape2D
*Inherits: **Shape2D < Resource < RefCounted < Object***

A 2D polyline shape, intended for use in physics. Used internally in CollisionPolygon2D when it's in CollisionPolygon2D.BUILD_SEGMENTS mode.

**Properties**
- `PackedVector2Array segments` = `PackedVector2Array()`

### ConcavePolygonShape3D
*Inherits: **Shape3D < Resource < RefCounted < Object***

A 3D trimesh shape, intended for use in physics. Usually used to provide a shape for a CollisionShape3D.

**Properties**
- `bool backface_collision` = `false`

**Methods**
- `PackedVector3Array get_faces() const`
- `void set_faces(faces: PackedVector3Array)`

### ConvertTransformModifier3D
*Inherits: **BoneConstraint3D < SkeletonModifier3D < Node3D < Node < Object***

Apply the copied transform of the bone set by BoneConstraint3D.set_reference_bone() to the bone set by BoneConstraint3D.set_apply_bone() about the specific axis with remapping it with some options.

**Properties**
- `int setting_count` = `0`

**Methods**
- `Axis get_apply_axis(index: int) const`
- `float get_apply_range_max(index: int) const`
- `float get_apply_range_min(index: int) const`
- `TransformMode get_apply_transform_mode(index: int) const`
- `Axis get_reference_axis(index: int) const`
- `float get_reference_range_max(index: int) const`
- `float get_reference_range_min(index: int) const`
- `TransformMode get_reference_transform_mode(index: int) const`
- `bool is_additive(index: int) const`
- `bool is_relative(index: int) const`
- `void set_additive(index: int, enabled: bool)`
- `void set_apply_axis(index: int, axis: Axis)`
- `void set_apply_range_max(index: int, range_max: float)`
- `void set_apply_range_min(index: int, range_min: float)`
- `void set_apply_transform_mode(index: int, transform_mode: TransformMode)`
- `void set_reference_axis(index: int, axis: Axis)`
- `void set_reference_range_max(index: int, range_max: float)`
- `void set_reference_range_min(index: int, range_min: float)`
- `void set_reference_transform_mode(index: int, transform_mode: TransformMode)`
- `void set_relative(index: int, enabled: bool)`

### ConvexPolygonShape2D
*Inherits: **Shape2D < Resource < RefCounted < Object***

A 2D convex polygon shape, intended for use in physics. Used internally in CollisionPolygon2D when it's in CollisionPolygon2D.BUILD_SOLIDS mode.

**Properties**
- `PackedVector2Array points` = `PackedVector2Array()`

**Methods**
- `void set_point_cloud(point_cloud: PackedVector2Array)`

### ConvexPolygonShape3D
*Inherits: **Shape3D < Resource < RefCounted < Object***

A 3D convex polyhedron shape, intended for use in physics. Usually used to provide a shape for a CollisionShape3D.

**Properties**
- `PackedVector3Array points` = `PackedVector3Array()`

### CopyTransformModifier3D
*Inherits: **BoneConstraint3D < SkeletonModifier3D < Node3D < Node < Object***

Apply the copied transform of the bone set by BoneConstraint3D.set_reference_bone() to the bone set by BoneConstraint3D.set_apply_bone() with processing it with some masks and options.

**Properties**
- `int setting_count` = `0`

**Methods**
- `BitField[AxisFlag] get_axis_flags(index: int) const`
- `BitField[TransformFlag] get_copy_flags(index: int) const`
- `BitField[AxisFlag] get_invert_flags(index: int) const`
- `bool is_additive(index: int) const`
- `bool is_axis_x_enabled(index: int) const`
- `bool is_axis_x_inverted(index: int) const`
- `bool is_axis_y_enabled(index: int) const`
- `bool is_axis_y_inverted(index: int) const`
- `bool is_axis_z_enabled(index: int) const`
- `bool is_axis_z_inverted(index: int) const`
- `bool is_position_copying(index: int) const`
- `bool is_relative(index: int) const`
- `bool is_rotation_copying(index: int) const`
- `bool is_scale_copying(index: int) const`
- `void set_additive(index: int, enabled: bool)`
- `void set_axis_flags(index: int, axis_flags: BitField[AxisFlag])`
- `void set_axis_x_enabled(index: int, enabled: bool)`
- `void set_axis_x_inverted(index: int, enabled: bool)`
- `void set_axis_y_enabled(index: int, enabled: bool)`
- `void set_axis_y_inverted(index: int, enabled: bool)`
- `void set_axis_z_enabled(index: int, enabled: bool)`
- `void set_axis_z_inverted(index: int, enabled: bool)`
- `void set_copy_flags(index: int, copy_flags: BitField[TransformFlag])`
- `void set_copy_position(index: int, enabled: bool)`
- `void set_copy_rotation(index: int, enabled: bool)`
- `void set_copy_scale(index: int, enabled: bool)`
- `void set_invert_flags(index: int, axis_flags: BitField[AxisFlag])`
- `void set_relative(index: int, enabled: bool)`

### CubemapArray
*Inherits: **ImageTextureLayered < TextureLayered < Texture < Resource < RefCounted < Object***

CubemapArrays are made of an array of Cubemaps. Like Cubemaps, they are made of multiple textures, the amount of which must be divisible by 6 (one for each face of the cube).

**Methods**
- `Resource create_placeholder() const`

### Cubemap
*Inherits: **ImageTextureLayered < TextureLayered < Texture < Resource < RefCounted < Object***

A cubemap is made of 6 textures organized in layers. They are typically used for faking reflections in 3D rendering (see ReflectionProbe). It can be used to make an object look as if it's reflecting its surroundings. This usually delivers much better performance than other reflection methods.

**Methods**
- `Resource create_placeholder() const`

### CurveTexture
*Inherits: **Texture2D < Texture < Resource < RefCounted < Object***

A 1D texture where pixel brightness corresponds to points on a unit Curve resource, either in grayscale or in red. This visual representation simplifies the task of saving curves as image files.

**Properties**
- `Curve curve`
- `bool resource_local_to_scene` = `false (overrides Resource)`
- `TextureMode texture_mode` = `0`
- `int width` = `256`

### CurveXYZTexture
*Inherits: **Texture2D < Texture < Resource < RefCounted < Object***

A 1D texture where the red, green, and blue color channels correspond to points on 3 unit Curve resources. Compared to using separate CurveTextures, this further simplifies the task of saving curves as image files.

**Properties**
- `Curve curve_x`
- `Curve curve_y`
- `Curve curve_z`
- `bool resource_local_to_scene` = `false (overrides Resource)`
- `int width` = `256`

### Curve
*Inherits: **Resource < RefCounted < Object***

This resource describes a mathematical curve by defining a set of points and tangents at each point. By default, it ranges between 0 and 1 on the X and Y axes, but these ranges can be changed.

**Properties**
- `int bake_resolution` = `100`
- `float max_domain` = `1.0`
- `float max_value` = `1.0`
- `float min_domain` = `0.0`
- `float min_value` = `0.0`
- `int point_count` = `0`

**Methods**
- `int add_point(position: Vector2, left_tangent: float = 0, right_tangent: float = 0, left_mode: TangentMode = 0, right_mode: TangentMode = 0)`
- `void bake()`
- `void clean_dupes()`
- `void clear_points()`
- `float get_domain_range() const`
- `TangentMode get_point_left_mode(index: int) const`
- `float get_point_left_tangent(index: int) const`
- `Vector2 get_point_position(index: int) const`
- `TangentMode get_point_right_mode(index: int) const`
- `float get_point_right_tangent(index: int) const`
- `float get_value_range() const`
- `void remove_point(index: int)`
- `float sample(offset: float) const`
- `float sample_baked(offset: float) const`
- `void set_point_left_mode(index: int, mode: TangentMode)`
- `void set_point_left_tangent(index: int, tangent: float)`
- `int set_point_offset(index: int, offset: float)`
- `void set_point_right_mode(index: int, mode: TangentMode)`
- `void set_point_right_tangent(index: int, tangent: float)`
- `void set_point_value(index: int, y: float)`

### CylinderShape3D
*Inherits: **Shape3D < Resource < RefCounted < Object***

A 3D cylinder shape, intended for use in physics. Usually used to provide a shape for a CollisionShape3D.

**Properties**
- `float height` = `2.0`
- `float radius` = `0.5`

### DPITexture
*Inherits: **Texture2D < Texture < Resource < RefCounted < Object***

An automatically scalable Texture2D based on an SVG image. DPITextures are used to automatically re-rasterize icons and other texture based UI theme elements to match viewport scale and font oversampling. See also ProjectSettings.display/window/stretch/mode ("canvas_items" mode) and Viewport.oversampling_override.

**Properties**
- `float base_scale` = `1.0`
- `Dictionary color_map` = `{}`
- `bool resource_local_to_scene` = `false (overrides Resource)`
- `float saturation` = `1.0`

**Methods**
- `DPITexture create_from_string(source: String, scale: float = 1.0, saturation: float = 1.0, color_map: Dictionary = {}) static`
- `RID get_scaled_rid() const`
- `String get_source() const`
- `void set_size_override(size: Vector2i)`
- `void set_source(source: String)`

### Decal
*Inherits: **VisualInstance3D < Node3D < Node < Object***

Decals are used to project a texture onto a Mesh in the scene. Use Decals to add detail to a scene without affecting the underlying Mesh. They are often used to add weathering to building, add dirt or mud to the ground, or add variety to props. Decals can be moved at any time, making them suitable for things like blob shadows or laser sight dots.

**Properties**
- `float albedo_mix` = `1.0`
- `int cull_mask` = `1048575`
- `float distance_fade_begin` = `40.0`
- `bool distance_fade_enabled` = `false`
- `float distance_fade_length` = `10.0`
- `float emission_energy` = `1.0`
- `float lower_fade` = `0.3`
- `Color modulate` = `Color(1, 1, 1, 1)`
- `float normal_fade` = `0.0`
- `Vector3 size` = `Vector3(2, 2, 2)`
- `Texture2D texture_albedo`
- `Texture2D texture_emission`
- `Texture2D texture_normal`
- `Texture2D texture_orm`
- `float upper_fade` = `0.3`

**Methods**
- `Texture2D get_texture(type: DecalTexture) const`
- `void set_texture(type: DecalTexture, texture: Texture2D)`

**GDScript Examples**
```gdscript
for i in Decal.TEXTURE_MAX:
    $NewDecal.set_texture(i, $OldDecal.get_texture(i))
```
```gdscript
for i in Decal.TEXTURE_MAX:
    $NewDecal.set_texture(i, $OldDecal.get_texture(i))
```

### Dictionary

Dictionaries are associative containers that contain values referenced by unique keys. Dictionaries will preserve the insertion order when adding new entries. In other programming languages, this data structure is often referred to as a hash map or an associative array.

**Methods**
- `void assign(dictionary: Dictionary)`
- `void clear()`
- `Dictionary duplicate(deep: bool = false) const`
- `Dictionary duplicate_deep(deep_subresources_mode: int = 1) const`
- `bool erase(key: Variant)`
- `Variant find_key(value: Variant) const`
- `Variant get(key: Variant, default: Variant = null) const`
- `Variant get_or_add(key: Variant, default: Variant = null)`
- `int get_typed_key_builtin() const`
- `StringName get_typed_key_class_name() const`
- `Variant get_typed_key_script() const`
- `int get_typed_value_builtin() const`
- `StringName get_typed_value_class_name() const`
- `Variant get_typed_value_script() const`
- `bool has(key: Variant) const`
- `bool has_all(keys: Array) const`
- `int hash() const`
- `bool is_empty() const`
- `bool is_read_only() const`
- `bool is_same_typed(dictionary: Dictionary) const`
- `bool is_same_typed_key(dictionary: Dictionary) const`
- `bool is_same_typed_value(dictionary: Dictionary) const`
- `bool is_typed() const`
- `bool is_typed_key() const`
- `bool is_typed_value() const`
- `Array keys() const`
- `void make_read_only()`
- `void merge(dictionary: Dictionary, overwrite: bool = false)`
- `Dictionary merged(dictionary: Dictionary, overwrite: bool = false) const`
- `bool recursive_equal(dictionary: Dictionary, recursion_count: int) const`
- `bool set(key: Variant, value: Variant)`
- `int size() const`
- `void sort()`
- `Array values() const`

**GDScript Examples**
```gdscript
var my_dict = {} # Creates an empty dictionary.

var dict_variable_key = "Another key name"
var dict_variable_value = "value2"
var another_dict = {
    "Some key name": "value1",
    dict_variable_key: dict_variable_value,
}

var points_dict = { "White": 50, "Yellow": 75, "Orange": 100 }

# Alternative Lua-style syntax.
# Doesn't require quotes around keys, but only string constants can be used as key names.
# Additionally, key names must start with a letter or an underscore.
# Here, `some_key` is a string literal, not a variable!
another_dict = {
    some_key = 42,
}
```
```gdscript
@export_enum("White", "Yellow", "Orange") var my_color: String
var points_dict = { "White": 50, "Yellow": 75, "Orange": 100 }
func _ready():
    # We can't use dot syntax here as `my_color` is a variable.
    var points = points_dict[my_color]
```

### DirectionalLight2D
*Inherits: **Light2D < Node2D < CanvasItem < Node < Object***

A directional light is a type of Light2D node that models an infinite number of parallel rays covering the entire scene. It is used for lights with strong intensity that are located far away from the scene (for example: to model sunlight or moonlight).

**Properties**
- `float height` = `0.0`
- `float max_distance` = `10000.0`

### DisplayServer
*Inherits: **Object***

DisplayServer handles everything related to window management. It is separated from OS as a single operating system may support multiple display servers.

**Methods**
- `RID accessibility_create_element(window_id: int, role: AccessibilityRole)`
- `RID accessibility_create_sub_element(parent_rid: RID, role: AccessibilityRole, insert_pos: int = -1)`
- `RID accessibility_create_sub_text_edit_elements(parent_rid: RID, shaped_text: RID, min_height: float, insert_pos: int = -1, is_last_line: bool = false)`
- `Variant accessibility_element_get_meta(id: RID) const`
- `void accessibility_element_set_meta(id: RID, meta: Variant)`
- `void accessibility_free_element(id: RID)`
- `RID accessibility_get_window_root(window_id: int) const`
- `bool accessibility_has_element(id: RID) const`
- `int accessibility_screen_reader_active() const`
- `void accessibility_set_window_focused(window_id: int, focused: bool)`
- `void accessibility_set_window_rect(window_id: int, rect_out: Rect2, rect_in: Rect2)`
- `int accessibility_should_increase_contrast() const`
- `int accessibility_should_reduce_animation() const`
- `int accessibility_should_reduce_transparency() const`
- `void accessibility_update_add_action(id: RID, action: AccessibilityAction, callable: Callable)`
- `void accessibility_update_add_child(id: RID, child_id: RID)`
- `void accessibility_update_add_custom_action(id: RID, action_id: int, action_description: String)`
- `void accessibility_update_add_related_controls(id: RID, related_id: RID)`
- `void accessibility_update_add_related_described_by(id: RID, related_id: RID)`
- `void accessibility_update_add_related_details(id: RID, related_id: RID)`
- `void accessibility_update_add_related_flow_to(id: RID, related_id: RID)`
- `void accessibility_update_add_related_labeled_by(id: RID, related_id: RID)`
- `void accessibility_update_add_related_radio_group(id: RID, related_id: RID)`
- `void accessibility_update_set_active_descendant(id: RID, other_id: RID)`
- `void accessibility_update_set_background_color(id: RID, color: Color)`
- `void accessibility_update_set_bounds(id: RID, p_rect: Rect2)`
- `void accessibility_update_set_checked(id: RID, checekd: bool)`
- `void accessibility_update_set_classname(id: RID, classname: String)`
- `void accessibility_update_set_color_value(id: RID, color: Color)`
- `void accessibility_update_set_description(id: RID, description: String)`
- `void accessibility_update_set_error_message(id: RID, other_id: RID)`
- `void accessibility_update_set_extra_info(id: RID, name: String)`
- `void accessibility_update_set_flag(id: RID, flag: AccessibilityFlags, value: bool)`
- `void accessibility_update_set_focus(id: RID)`
- `void accessibility_update_set_foreground_color(id: RID, color: Color)`
- `void accessibility_update_set_in_page_link_target(id: RID, other_id: RID)`
- `void accessibility_update_set_language(id: RID, language: String)`
- `void accessibility_update_set_list_item_count(id: RID, size: int)`
- `void accessibility_update_set_list_item_expanded(id: RID, expanded: bool)`
- `void accessibility_update_set_list_item_index(id: RID, index: int)`

**GDScript Examples**
```gdscript
val uri = "content://com.android..." # URI of the selected file or folder.
val persist = true # Set to false to release the persistable permission.
var android_runtime = Engine.get_singleton("AndroidRuntime")
android_runtime.updatePersistableUriPermission(uri, persist)
```
```gdscript
# Set region, using Path2D node.
DisplayServer.window_set_mouse_passthrough($Path2D.curve.get_baked_points())

# Set region, using Polygon2D node.
DisplayServer.window_set_mouse_passthrough($Polygon2D.polygon)

# Reset region to default.
DisplayServer.window_set_mouse_passthrough([])
```

### EncodedObjectAsID
*Inherits: **RefCounted < Object***

Utility class which holds a reference to the internal identifier of an Object instance, as given by Object.get_instance_id(). This ID can then be used to retrieve the object instance with @GlobalScope.instance_from_id().

**Properties**
- `int object_id` = `0`

### Expression
*Inherits: **RefCounted < Object***

An expression can be made of any arithmetic operation, built-in math function call, method call of a passed instance, or built-in type construction call.

**Methods**
- `Variant execute(inputs: Array = [], base_instance: Object = null, show_error: bool = true, const_calls_only: bool = false)`
- `String get_error_text() const`
- `bool has_execute_failed() const`
- `Error parse(expression: String, input_names: PackedStringArray = PackedStringArray())`

**GDScript Examples**
```gdscript
var expression = Expression.new()

func _ready():
    $LineEdit.text_submitted.connect(self._on_text_submitted)

func _on_text_submitted(command):
    var error = expression.parse(command)
    if error != OK:
        print(expression.get_error_text())
        return
    var result = expression.execute()
    if not expression.has_execute_failed():
        $LineEdit.text = str(result)
```

### ExternalTexture
*Inherits: **Texture2D < Texture < Resource < RefCounted < Object***

Displays the content of an external buffer provided by the platform.

**Properties**
- `bool resource_local_to_scene` = `false (overrides Resource)`
- `Vector2 size` = `Vector2(256, 256)`

**Methods**
- `int get_external_texture_id() const`
- `void set_external_buffer_id(external_buffer_id: int)`

### FABRIK3D
*Inherits: **IterateIK3D < ChainIK3D < IKModifier3D < SkeletonModifier3D < Node3D < Node < Object***

FABRIK3D is position based IK, allowing precise and accurate tracking of targets. It's ideal for simple chains without limitations.

### FBXDocument
*Inherits: **GLTFDocument < Resource < RefCounted < Object***

The FBXDocument handles FBX documents. It provides methods to append data from buffers or files, generate scenes, and register/unregister document extensions.

### FBXState
*Inherits: **GLTFState < Resource < RefCounted < Object***

The FBXState handles the state data imported from FBX files.

**Properties**
- `bool allow_geometry_helper_nodes` = `false`

### FileSystemDock
*Inherits: **EditorDock < MarginContainer < Container < Control < CanvasItem < Node < Object***

This class is available only in EditorPlugins and can't be instantiated. You can access it using EditorInterface.get_file_system_dock().

**Methods**
- `void add_resource_tooltip_plugin(plugin: EditorResourceTooltipPlugin)`
- `void navigate_to_path(path: String)`
- `void remove_resource_tooltip_plugin(plugin: EditorResourceTooltipPlugin)`

### FogMaterial
*Inherits: **Material < Resource < RefCounted < Object***

A Material resource that can be used by FogVolumes to draw volumetric effects.

**Properties**
- `Color albedo` = `Color(1, 1, 1, 1)`
- `float density` = `1.0`
- `Texture3D density_texture`
- `float edge_fade` = `0.1`
- `Color emission` = `Color(0, 0, 0, 1)`
- `float height_falloff` = `0.0`

### FoldableContainer
*Inherits: **Container < Control < CanvasItem < Node < Object***

A container that can be expanded/collapsed, with a title that can be filled with controls, such as buttons. This is also called an accordion.

**Properties**
- `FocusMode focus_mode` = `2 (overrides Control)`
- `FoldableGroup foldable_group`
- `bool folded` = `false`
- `String language` = `""`
- `MouseFilter mouse_filter` = `0 (overrides Control)`
- `String title` = `""`
- `HorizontalAlignment title_alignment` = `0`
- `TitlePosition title_position` = `0`
- `TextDirection title_text_direction` = `0`
- `OverrunBehavior title_text_overrun_behavior` = `0`

**Methods**
- `void add_title_bar_control(control: Control)`
- `void expand()`
- `void fold()`
- `void remove_title_bar_control(control: Control)`

### FoldableGroup
*Inherits: **Resource < RefCounted < Object***

A group of FoldableContainer-derived nodes. Only one container can be expanded at a time.

**Properties**
- `bool allow_folding_all` = `false`
- `bool resource_local_to_scene` = `true (overrides Resource)`

**Methods**
- `Array[FoldableContainer] get_containers() const`
- `FoldableContainer get_expanded_container() const`

### Font
*Inherits: **Resource < RefCounted < Object** | Inherited by: FontFile, FontVariation, SystemFont*

Abstract base class for different font types. It has methods for drawing text and font character introspection.

**Properties**
- `Array[Font] fallbacks` = `[]`

**Methods**
- `float draw_char(canvas_item: RID, pos: Vector2, char: int, font_size: int, modulate: Color = Color(1, 1, 1, 1), oversampling: float = 0.0) const`
- `float draw_char_outline(canvas_item: RID, pos: Vector2, char: int, font_size: int, size: int = -1, modulate: Color = Color(1, 1, 1, 1), oversampling: float = 0.0) const`
- `void draw_multiline_string(canvas_item: RID, pos: Vector2, text: String, alignment: HorizontalAlignment = 0, width: float = -1, font_size: int = 16, max_lines: int = -1, modulate: Color = Color(1, 1, 1, 1), brk_flags: BitField[LineBreakFlag] = 3, justification_flags: BitField[JustificationFlag] = 3, direction: Direction = 0, orientation: Orientation = 0, oversampling: float = 0.0) const`
- `void draw_multiline_string_outline(canvas_item: RID, pos: Vector2, text: String, alignment: HorizontalAlignment = 0, width: float = -1, font_size: int = 16, max_lines: int = -1, size: int = 1, modulate: Color = Color(1, 1, 1, 1), brk_flags: BitField[LineBreakFlag] = 3, justification_flags: BitField[JustificationFlag] = 3, direction: Direction = 0, orientation: Orientation = 0, oversampling: float = 0.0) const`
- `void draw_string(canvas_item: RID, pos: Vector2, text: String, alignment: HorizontalAlignment = 0, width: float = -1, font_size: int = 16, modulate: Color = Color(1, 1, 1, 1), justification_flags: BitField[JustificationFlag] = 3, direction: Direction = 0, orientation: Orientation = 0, oversampling: float = 0.0) const`
- `void draw_string_outline(canvas_item: RID, pos: Vector2, text: String, alignment: HorizontalAlignment = 0, width: float = -1, font_size: int = 16, size: int = 1, modulate: Color = Color(1, 1, 1, 1), justification_flags: BitField[JustificationFlag] = 3, direction: Direction = 0, orientation: Orientation = 0, oversampling: float = 0.0) const`
- `RID find_variation(variation_coordinates: Dictionary, face_index: int = 0, strength: float = 0.0, transform: Transform2D = Transform2D(1, 0, 0, 1, 0, 0), spacing_top: int = 0, spacing_bottom: int = 0, spacing_space: int = 0, spacing_glyph: int = 0, baseline_offset: float = 0.0) const`
- `float get_ascent(font_size: int = 16) const`
- `Vector2 get_char_size(char: int, font_size: int) const`
- `float get_descent(font_size: int = 16) const`
- `int get_face_count() const`
- `String get_font_name() const`
- `int get_font_stretch() const`
- `BitField[FontStyle] get_font_style() const`
- `String get_font_style_name() const`
- `int get_font_weight() const`
- `float get_height(font_size: int = 16) const`
- `Vector2 get_multiline_string_size(text: String, alignment: HorizontalAlignment = 0, width: float = -1, font_size: int = 16, max_lines: int = -1, brk_flags: BitField[LineBreakFlag] = 3, justification_flags: BitField[JustificationFlag] = 3, direction: Direction = 0, orientation: Orientation = 0) const`
- `Dictionary get_opentype_features() const`
- `Dictionary get_ot_name_strings() const`
- `Array[RID] get_rids() const`
- `int get_spacing(spacing: SpacingType) const`
- `Vector2 get_string_size(text: String, alignment: HorizontalAlignment = 0, width: float = -1, font_size: int = 16, justification_flags: BitField[JustificationFlag] = 3, direction: Direction = 0, orientation: Orientation = 0) const`
- `String get_supported_chars() const`
- `Dictionary get_supported_feature_list() const`
- `Dictionary get_supported_variation_list() const`
- `float get_underline_position(font_size: int = 16) const`
- `float get_underline_thickness(font_size: int = 16) const`
- `bool has_char(char: int) const`
- `bool is_language_supported(language: String) const`
- `bool is_script_supported(script: String) const`
- `void set_cache_capacity(single_line: int, multi_line: int)`

**GDScript Examples**
```gdscript
var string_size = $Label.get_theme_font("font").get_string_size($Label.text, HORIZONTAL_ALIGNMENT_LEFT, -1, $Label.get_theme_font_size("font_size"))
```
```gdscript
var fv = FontVariation.new()
fv.base_font = load("res://RobotoFlex.ttf")
var variation_list = fv.get_supported_variation_list()
for tag in variation_list:
    var name = TextServerManager.get_primary_interface().tag_to_name(tag)
    var values = variation_list[tag]
    print("variation axis: %s (%d)\n\tmin, max, default: %s" % [name, tag, values])
```

### FramebufferCacheRD
*Inherits: **Object***

Framebuffer cache manager for RenderingDevice-based renderers. Provides a way to create a framebuffer and reuse it in subsequent calls for as long as the used textures exists. Framebuffers will automatically be cleaned up when dependent objects are freed.

**Methods**
- `RID get_cache_multipass(textures: Array[RID], passes: Array[RDFramebufferPass], views: int) static`

### GDExtensionManager
*Inherits: **Object***

The GDExtensionManager loads, initializes, and keeps track of all available GDExtension libraries in the project.

**Methods**
- `GDExtension get_extension(path: String)`
- `PackedStringArray get_loaded_extensions() const`
- `bool is_extension_loaded(path: String) const`
- `LoadStatus load_extension(path: String)`
- `LoadStatus load_extension_from_function(path: String, init_func: const GDExtensionInitializationFunction*)`
- `LoadStatus reload_extension(path: String)`
- `LoadStatus unload_extension(path: String)`

### GDExtension
*Inherits: **Resource < RefCounted < Object***

The GDExtension resource type represents a shared library which can expand the functionality of the engine. The GDExtensionManager singleton is responsible for loading, reloading, and unloading GDExtension resources.

**Methods**
- `InitializationLevel get_minimum_library_initialization_level() const`
- `bool is_library_open() const`

### GLTFAccessor
*Inherits: **Resource < RefCounted < Object***

GLTFAccessor is a data structure representing a glTF accessor that would be found in the "accessors" array. A buffer is a blob of binary data. A buffer view is a slice of a buffer. An accessor is a typed interpretation of the data in a buffer view.

**Properties**
- `GLTFAccessorType accessor_type` = `0`
- `int buffer_view` = `-1`
- `int byte_offset` = `0`
- `GLTFComponentType component_type` = `0`
- `int count` = `0`
- `PackedFloat64Array max` = `PackedFloat64Array()`
- `PackedFloat64Array min` = `PackedFloat64Array()`
- `bool normalized` = `false`
- `int sparse_count` = `0`
- `int sparse_indices_buffer_view` = `0`
- `int sparse_indices_byte_offset` = `0`
- `GLTFComponentType sparse_indices_component_type` = `0`
- `int sparse_values_buffer_view` = `0`
- `int sparse_values_byte_offset` = `0`
- `int type`

**Methods**
- `GLTFAccessor from_dictionary(dictionary: Dictionary) static`
- `Dictionary to_dictionary() const`

### GLTFAnimation
*Inherits: **Resource < RefCounted < Object***

There is currently no description for this class. Please help us by contributing one!

**Properties**
- `bool loop` = `false`
- `String original_name` = `""`

**Methods**
- `Variant get_additional_data(extension_name: StringName)`
- `void set_additional_data(extension_name: StringName, additional_data: Variant)`

### GLTFBufferView
*Inherits: **Resource < RefCounted < Object***

GLTFBufferView is a data structure representing a glTF bufferView that would be found in the "bufferViews" array. A buffer is a blob of binary data. A buffer view is a slice of a buffer that can be used to identify and extract data from the buffer.

**Properties**
- `int buffer` = `-1`
- `int byte_length` = `0`
- `int byte_offset` = `0`
- `int byte_stride` = `-1`
- `bool indices` = `false`
- `bool vertex_attributes` = `false`

**Methods**
- `GLTFBufferView from_dictionary(dictionary: Dictionary) static`
- `PackedByteArray load_buffer_view_data(state: GLTFState) const`
- `Dictionary to_dictionary() const`

### GLTFCamera
*Inherits: **Resource < RefCounted < Object***

Represents a camera as defined by the base glTF spec.

**Properties**
- `float depth_far` = `4000.0`
- `float depth_near` = `0.05`
- `float fov` = `1.3089969`
- `bool perspective` = `true`
- `float size_mag` = `0.5`

**Methods**
- `GLTFCamera from_dictionary(dictionary: Dictionary) static`
- `GLTFCamera from_node(camera_node: Camera3D) static`
- `Dictionary to_dictionary() const`
- `Camera3D to_node() const`

### GLTFDocumentExtensionConvertImporterMesh
*Inherits: **GLTFDocumentExtension < Resource < RefCounted < Object***

There is currently no description for this class. Please help us by contributing one!

### GLTFDocumentExtension
*Inherits: **Resource < RefCounted < Object** | Inherited by: GLTFDocumentExtensionConvertImporterMesh*

Extends the functionality of the GLTFDocument class by allowing you to run arbitrary code at various stages of glTF import or export.

**Methods**
- `void _convert_scene_node(state: GLTFState, gltf_node: GLTFNode, scene_node: Node) virtual`
- `Error _export_node(state: GLTFState, gltf_node: GLTFNode, json: Dictionary, node: Node) virtual`
- `GLTFObjectModelProperty _export_object_model_property(state: GLTFState, node_path: NodePath, godot_node: Node, gltf_node_index: int, target_object: Object, target_depth: int) virtual`
- `Error _export_post(state: GLTFState) virtual`
- `Error _export_post_convert(state: GLTFState, root: Node) virtual`
- `Error _export_preflight(state: GLTFState, root: Node) virtual`
- `Error _export_preserialize(state: GLTFState) virtual`
- `Node3D _generate_scene_node(state: GLTFState, gltf_node: GLTFNode, scene_parent: Node) virtual`
- `String _get_image_file_extension() virtual`
- `PackedStringArray _get_saveable_image_formats() virtual`
- `PackedStringArray _get_supported_extensions() virtual`
- `Error _import_node(state: GLTFState, gltf_node: GLTFNode, json: Dictionary, node: Node) virtual`
- `GLTFObjectModelProperty _import_object_model_property(state: GLTFState, split_json_pointer: PackedStringArray, partial_paths: Array[NodePath]) virtual`
- `Error _import_post(state: GLTFState, root: Node) virtual`
- `Error _import_post_parse(state: GLTFState) virtual`
- `Error _import_pre_generate(state: GLTFState) virtual`
- `Error _import_preflight(state: GLTFState, extensions: PackedStringArray) virtual`
- `Error _parse_image_data(state: GLTFState, image_data: PackedByteArray, mime_type: String, ret_image: Image) virtual`
- `Error _parse_node_extensions(state: GLTFState, gltf_node: GLTFNode, extensions: Dictionary) virtual`
- `Error _parse_texture_json(state: GLTFState, texture_json: Dictionary, ret_gltf_texture: GLTFTexture) virtual`
- `Error _save_image_at_path(state: GLTFState, image: Image, file_path: String, image_format: String, lossy_quality: float) virtual`
- `PackedByteArray _serialize_image_to_bytes(state: GLTFState, image: Image, image_dict: Dictionary, image_format: String, lossy_quality: float) virtual`
- `Error _serialize_texture_json(state: GLTFState, texture_json: Dictionary, gltf_texture: GLTFTexture, image_format: String) virtual`

### GLTFDocument
*Inherits: **Resource < RefCounted < Object** | Inherited by: FBXDocument*

GLTFDocument supports reading data from a glTF file, buffer, or Godot scene. This data can then be written to the filesystem, buffer, or used to create a Godot scene.

**Properties**
- `String fallback_image_format` = `"None"`
- `float fallback_image_quality` = `0.25`
- `String image_format` = `"PNG"`
- `float lossy_quality` = `0.75`
- `RootNodeMode root_node_mode` = `0`
- `VisibilityMode visibility_mode` = `0`

**Methods**
- `Error append_from_buffer(bytes: PackedByteArray, base_path: String, state: GLTFState, flags: int = 0)`
- `Error append_from_file(path: String, state: GLTFState, flags: int = 0, base_path: String = "")`
- `Error append_from_scene(node: Node, state: GLTFState, flags: int = 0)`
- `GLTFObjectModelProperty export_object_model_property(state: GLTFState, node_path: NodePath, godot_node: Node, gltf_node_index: int) static`
- `PackedByteArray generate_buffer(state: GLTFState)`
- `Node generate_scene(state: GLTFState, bake_fps: float = 30, trimming: bool = false, remove_immutable_tracks: bool = true)`
- `PackedStringArray get_supported_gltf_extensions() static`
- `GLTFObjectModelProperty import_object_model_property(state: GLTFState, json_pointer: String) static`
- `void register_gltf_document_extension(extension: GLTFDocumentExtension, first_priority: bool = false) static`
- `void unregister_gltf_document_extension(extension: GLTFDocumentExtension) static`
- `Error write_to_filesystem(state: GLTFState, path: String)`

### GLTFLight
*Inherits: **Resource < RefCounted < Object***

Represents a light as defined by the KHR_lights_punctual glTF extension.

**Properties**
- `Color color` = `Color(1, 1, 1, 1)`
- `float inner_cone_angle` = `0.0`
- `float intensity` = `1.0`
- `String light_type` = `""`
- `float outer_cone_angle` = `0.7853982`
- `float range` = `inf`

**Methods**
- `GLTFLight from_dictionary(dictionary: Dictionary) static`
- `GLTFLight from_node(light_node: Light3D) static`
- `Variant get_additional_data(extension_name: StringName)`
- `void set_additional_data(extension_name: StringName, additional_data: Variant)`
- `Dictionary to_dictionary() const`
- `Light3D to_node() const`

### GLTFMesh
*Inherits: **Resource < RefCounted < Object***

GLTFMesh handles 3D mesh data imported from glTF files. It includes properties for blend channels, blend weights, instance materials, and the mesh itself.

**Properties**
- `PackedFloat32Array blend_weights` = `PackedFloat32Array()`
- `Array[Material] instance_materials` = `[]`
- `ImporterMesh mesh`
- `String original_name` = `""`

**Methods**
- `Variant get_additional_data(extension_name: StringName)`
- `void set_additional_data(extension_name: StringName, additional_data: Variant)`

### GLTFNode
*Inherits: **Resource < RefCounted < Object***

Represents a glTF node. glTF nodes may have names, transforms, children (other glTF nodes), and more specialized properties (represented by their own classes).

**Properties**
- `int camera` = `-1`
- `PackedInt32Array children` = `PackedInt32Array()`
- `int height` = `-1`
- `int light` = `-1`
- `int mesh` = `-1`
- `String original_name` = `""`
- `int parent` = `-1`
- `Vector3 position` = `Vector3(0, 0, 0)`
- `Quaternion rotation` = `Quaternion(0, 0, 0, 1)`
- `Vector3 scale` = `Vector3(1, 1, 1)`
- `int skeleton` = `-1`
- `int skin` = `-1`
- `bool visible` = `true`
- `Transform3D xform` = `Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0)`

**Methods**
- `void append_child_index(child_index: int)`
- `Variant get_additional_data(extension_name: StringName)`
- `NodePath get_scene_node_path(gltf_state: GLTFState, handle_skeletons: bool = true)`
- `void set_additional_data(extension_name: StringName, additional_data: Variant)`

### GLTFObjectModelProperty
*Inherits: **RefCounted < Object***

GLTFObjectModelProperty defines a mapping between a property in the glTF object model and a NodePath in the Godot scene tree. This can be used to animate properties in a glTF file using the KHR_animation_pointer extension, or to access them through an engine-agnostic script such as a behavior graph as defined by the KHR_interactivity extension.

**Properties**
- `Expression gltf_to_godot_expression`
- `Expression godot_to_gltf_expression`
- `Array[PackedStringArray] json_pointers` = `[]`
- `Array[NodePath] node_paths` = `[]`
- `GLTFObjectModelType object_model_type` = `0`
- `Variant.Type variant_type` = `0`

**Methods**
- `void append_node_path(node_path: NodePath)`
- `void append_path_to_property(node_path: NodePath, prop_name: StringName)`
- `GLTFAccessorType get_accessor_type() const`
- `bool has_json_pointers() const`
- `bool has_node_paths() const`
- `void set_types(variant_type: Variant.Type, obj_model_type: GLTFObjectModelType)`

### GLTFPhysicsBody
*Inherits: **Resource < RefCounted < Object***

Represents a physics body as an intermediary between the OMI_physics_body glTF data and Godot's nodes, and it's abstracted in a way that allows adding support for different glTF physics extensions in the future.

**Properties**
- `Vector3 angular_velocity` = `Vector3(0, 0, 0)`
- `String body_type` = `"rigid"`
- `Vector3 center_of_mass` = `Vector3(0, 0, 0)`
- `Vector3 inertia_diagonal` = `Vector3(0, 0, 0)`
- `Quaternion inertia_orientation` = `Quaternion(0, 0, 0, 1)`
- `Basis inertia_tensor` = `Basis(0, 0, 0, 0, 0, 0, 0, 0, 0)`
- `Vector3 linear_velocity` = `Vector3(0, 0, 0)`
- `float mass` = `1.0`

**Methods**
- `GLTFPhysicsBody from_dictionary(dictionary: Dictionary) static`
- `GLTFPhysicsBody from_node(body_node: CollisionObject3D) static`
- `Dictionary to_dictionary() const`
- `CollisionObject3D to_node() const`

### GLTFPhysicsShape
*Inherits: **Resource < RefCounted < Object***

Represents a physics shape as defined by the OMI_physics_shape or OMI_collider glTF extensions. This class is an intermediary between the glTF data and Godot's nodes, and it's abstracted in a way that allows adding support for different glTF physics extensions in the future.

**Properties**
- `float height` = `2.0`
- `ImporterMesh importer_mesh`
- `bool is_trigger` = `false`
- `int mesh_index` = `-1`
- `float radius` = `0.5`
- `String shape_type` = `""`
- `Vector3 size` = `Vector3(1, 1, 1)`

**Methods**
- `GLTFPhysicsShape from_dictionary(dictionary: Dictionary) static`
- `GLTFPhysicsShape from_node(shape_node: CollisionShape3D) static`
- `GLTFPhysicsShape from_resource(shape_resource: Shape3D) static`
- `Dictionary to_dictionary() const`
- `CollisionShape3D to_node(cache_shapes: bool = false)`
- `Shape3D to_resource(cache_shapes: bool = false)`

### GLTFSkeleton
*Inherits: **Resource < RefCounted < Object***

There is currently no description for this class. Please help us by contributing one!

**Properties**
- `PackedInt32Array joints` = `PackedInt32Array()`
- `PackedInt32Array roots` = `PackedInt32Array()`

**Methods**
- `BoneAttachment3D get_bone_attachment(idx: int)`
- `int get_bone_attachment_count()`
- `Dictionary get_godot_bone_node()`
- `Skeleton3D get_godot_skeleton()`
- `Array[String] get_unique_names()`
- `void set_godot_bone_node(godot_bone_node: Dictionary)`
- `void set_unique_names(unique_names: Array[String])`

### GLTFSkin
*Inherits: **Resource < RefCounted < Object***

There is currently no description for this class. Please help us by contributing one!

**Properties**
- `Skin godot_skin`
- `PackedInt32Array joints` = `PackedInt32Array()`
- `PackedInt32Array joints_original` = `PackedInt32Array()`
- `PackedInt32Array non_joints` = `PackedInt32Array()`
- `PackedInt32Array roots` = `PackedInt32Array()`
- `int skeleton` = `-1`
- `int skin_root` = `-1`

**Methods**
- `Array[Transform3D] get_inverse_binds()`
- `Dictionary get_joint_i_to_bone_i()`
- `Dictionary get_joint_i_to_name()`
- `void set_inverse_binds(inverse_binds: Array[Transform3D])`
- `void set_joint_i_to_bone_i(joint_i_to_bone_i: Dictionary)`
- `void set_joint_i_to_name(joint_i_to_name: Dictionary)`

### GLTFSpecGloss
*Inherits: **Resource < RefCounted < Object***

KHR_materials_pbrSpecularGlossiness is an archived glTF extension. This means that it is deprecated and not recommended for new files. However, it is still supported for loading old files.

**Properties**
- `Color diffuse_factor` = `Color(1, 1, 1, 1)`
- `Image diffuse_img`
- `float gloss_factor` = `1.0`
- `Image spec_gloss_img`
- `Color specular_factor` = `Color(1, 1, 1, 1)`

### GLTFState
*Inherits: **Resource < RefCounted < Object** | Inherited by: FBXState*

Contains all nodes and resources of a glTF file. This is used by GLTFDocument as data storage, which allows GLTFDocument and all GLTFDocumentExtension classes to remain stateless.

**Properties**
- `float bake_fps` = `30.0`
- `String base_path` = `""`
- `Array[PackedByteArray] buffers` = `[]`
- `String copyright` = `""`
- `bool create_animations` = `true`
- `String filename` = `""`
- `PackedByteArray glb_data` = `PackedByteArray()`
- `HandleBinaryImageMode handle_binary_image_mode` = `1`
- `bool import_as_skeleton_bones` = `false`
- `Dictionary json` = `{}`
- `int major_version` = `0`
- `int minor_version` = `0`
- `PackedInt32Array root_nodes` = `PackedInt32Array()`
- `String scene_name` = `""`
- `bool use_named_skin_binds` = `false`

**Methods**
- `void add_used_extension(extension_name: String, required: bool)`
- `int append_data_to_buffers(data: PackedByteArray, deduplication: bool)`
- `int append_gltf_node(gltf_node: GLTFNode, godot_scene_node: Node, parent_node_index: int)`
- `Array[GLTFAccessor] get_accessors() const`
- `Variant get_additional_data(extension_name: StringName) const`
- `AnimationPlayer get_animation_player(anim_player_index: int) const`
- `int get_animation_players_count(anim_player_index: int) const`
- `Array[GLTFAnimation] get_animations() const`
- `Array[GLTFBufferView] get_buffer_views() const`
- `Array[GLTFCamera] get_cameras() const`
- `int get_handle_binary_image() const`
- `Array[Texture2D] get_images() const`
- `Array[GLTFLight] get_lights() const`
- `Array[Material] get_materials() const`
- `Array[GLTFMesh] get_meshes() const`
- `int get_node_index(scene_node: Node) const`
- `Array[GLTFNode] get_nodes() const`
- `Node get_scene_node(gltf_node_index: int) const`
- `Array[GLTFSkeleton] get_skeletons() const`
- `Array[GLTFSkin] get_skins() const`
- `Array[GLTFTextureSampler] get_texture_samplers() const`
- `Array[GLTFTexture] get_textures() const`
- `Array[String] get_unique_animation_names() const`
- `Array[String] get_unique_names() const`
- `void set_accessors(accessors: Array[GLTFAccessor])`
- `void set_additional_data(extension_name: StringName, additional_data: Variant)`
- `void set_animations(animations: Array[GLTFAnimation])`
- `void set_buffer_views(buffer_views: Array[GLTFBufferView])`
- `void set_cameras(cameras: Array[GLTFCamera])`
- `void set_handle_binary_image(method: int)`
- `void set_images(images: Array[Texture2D])`
- `void set_lights(lights: Array[GLTFLight])`
- `void set_materials(materials: Array[Material])`
- `void set_meshes(meshes: Array[GLTFMesh])`
- `void set_nodes(nodes: Array[GLTFNode])`
- `void set_skeletons(skeletons: Array[GLTFSkeleton])`
- `void set_skins(skins: Array[GLTFSkin])`
- `void set_texture_samplers(texture_samplers: Array[GLTFTextureSampler])`
- `void set_textures(textures: Array[GLTFTexture])`
- `void set_unique_animation_names(unique_animation_names: Array[String])`

### GLTFTextureSampler
*Inherits: **Resource < RefCounted < Object***

Represents a texture sampler as defined by the base glTF spec. Texture samplers in glTF specify how to sample data from the texture's base image, when rendering the texture on an object.

**Properties**
- `int mag_filter` = `9729`
- `int min_filter` = `9987`
- `int wrap_s` = `10497`
- `int wrap_t` = `10497`

### GLTFTexture
*Inherits: **Resource < RefCounted < Object***

GLTFTexture represents a texture in a glTF file.

**Properties**
- `int sampler` = `-1`
- `int src_image` = `-1`

### GPUParticles3D
*Inherits: **GeometryInstance3D < VisualInstance3D < Node3D < Node < Object***

3D particle node used to create a variety of particle systems and effects. GPUParticles3D features an emitter that generates some number of particles at a given rate.

**Properties**
- `int amount` = `8`
- `float amount_ratio` = `1.0`
- `float collision_base_size` = `0.01`
- `DrawOrder draw_order` = `0`
- `Mesh draw_pass_1`
- `Mesh draw_pass_2`
- `Mesh draw_pass_3`
- `Mesh draw_pass_4`
- `int draw_passes` = `1`
- `Skin draw_skin`
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
- `bool trail_enabled` = `false`
- `float trail_lifetime` = `0.3`
- `TransformAlign transform_align` = `0`
- `bool use_fixed_seed` = `false`
- `AABB visibility_aabb` = `AABB(-4, -4, -4, 8, 8, 8)`

**Methods**
- `AABB capture_aabb() const`
- `void convert_from_particles(particles: Node)`
- `void emit_particle(xform: Transform3D, velocity: Vector3, color: Color, custom: Color, flags: int)`
- `Mesh get_draw_pass_mesh(pass: int) const`
- `void request_particles_process(process_time: float)`
- `void restart(keep_seed: bool = false)`
- `void set_draw_pass_mesh(pass: int, mesh: Mesh)`

### GPUParticlesAttractor3D
*Inherits: **VisualInstance3D < Node3D < Node < Object** | Inherited by: GPUParticlesAttractorBox3D, GPUParticlesAttractorSphere3D, GPUParticlesAttractorVectorField3D*

Particle attractors can be used to attract particles towards the attractor's origin, or to push them away from the attractor's origin.

**Properties**
- `float attenuation` = `1.0`
- `int cull_mask` = `4294967295`
- `float directionality` = `0.0`
- `float strength` = `1.0`

### GPUParticlesAttractorBox3D
*Inherits: **GPUParticlesAttractor3D < VisualInstance3D < Node3D < Node < Object***

A box-shaped attractor that influences particles from GPUParticles3D nodes. Can be used to attract particles towards its origin, or to push them away from its origin.

**Properties**
- `Vector3 size` = `Vector3(2, 2, 2)`

### GPUParticlesAttractorSphere3D
*Inherits: **GPUParticlesAttractor3D < VisualInstance3D < Node3D < Node < Object***

A spheroid-shaped attractor that influences particles from GPUParticles3D nodes. Can be used to attract particles towards its origin, or to push them away from its origin.

**Properties**
- `float radius` = `1.0`

### GPUParticlesAttractorVectorField3D
*Inherits: **GPUParticlesAttractor3D < VisualInstance3D < Node3D < Node < Object***

A box-shaped attractor with varying directions and strengths defined in it that influences particles from GPUParticles3D nodes.

**Properties**
- `Vector3 size` = `Vector3(2, 2, 2)`
- `Texture3D texture`

### GPUParticlesCollision3D
*Inherits: **VisualInstance3D < Node3D < Node < Object** | Inherited by: GPUParticlesCollisionBox3D, GPUParticlesCollisionHeightField3D, GPUParticlesCollisionSDF3D, GPUParticlesCollisionSphere3D*

Particle collision shapes can be used to make particles stop or bounce against them.

**Properties**
- `int cull_mask` = `4294967295`

### GPUParticlesCollisionBox3D
*Inherits: **GPUParticlesCollision3D < VisualInstance3D < Node3D < Node < Object***

A box-shaped 3D particle collision shape affecting GPUParticles3D nodes.

**Properties**
- `Vector3 size` = `Vector3(2, 2, 2)`

### GPUParticlesCollisionHeightField3D
*Inherits: **GPUParticlesCollision3D < VisualInstance3D < Node3D < Node < Object***

A real-time heightmap-shaped 3D particle collision shape affecting GPUParticles3D nodes.

**Properties**
- `bool follow_camera_enabled` = `false`
- `int heightfield_mask` = `1048575`
- `Resolution resolution` = `2`
- `Vector3 size` = `Vector3(2, 2, 2)`
- `UpdateMode update_mode` = `0`

**Methods**
- `bool get_heightfield_mask_value(layer_number: int) const`
- `void set_heightfield_mask_value(layer_number: int, value: bool)`

### GPUParticlesCollisionSDF3D
*Inherits: **GPUParticlesCollision3D < VisualInstance3D < Node3D < Node < Object***

A baked signed distance field 3D particle collision shape affecting GPUParticles3D nodes.

**Properties**
- `int bake_mask` = `4294967295`
- `Resolution resolution` = `2`
- `Vector3 size` = `Vector3(2, 2, 2)`
- `Texture3D texture`
- `float thickness` = `1.0`

**Methods**
- `bool get_bake_mask_value(layer_number: int) const`
- `void set_bake_mask_value(layer_number: int, value: bool)`

### GPUParticlesCollisionSphere3D
*Inherits: **GPUParticlesCollision3D < VisualInstance3D < Node3D < Node < Object***

A sphere-shaped 3D particle collision shape affecting GPUParticles3D nodes.

**Properties**
- `float radius` = `1.0`

### Geometry2D
*Inherits: **Object***

Provides a set of helper functions to create geometric shapes, compute intersections between shapes, and process various other geometric operations in 2D.

**Methods**
- `Array[Vector2i] bresenham_line(from: Vector2i, to: Vector2i)`
- `Array[PackedVector2Array] clip_polygons(polygon_a: PackedVector2Array, polygon_b: PackedVector2Array)`
- `Array[PackedVector2Array] clip_polyline_with_polygon(polyline: PackedVector2Array, polygon: PackedVector2Array)`
- `PackedVector2Array convex_hull(points: PackedVector2Array)`
- `Array[PackedVector2Array] decompose_polygon_in_convex(polygon: PackedVector2Array)`
- `Array[PackedVector2Array] exclude_polygons(polygon_a: PackedVector2Array, polygon_b: PackedVector2Array)`
- `Vector2 get_closest_point_to_segment(point: Vector2, s1: Vector2, s2: Vector2)`
- `Vector2 get_closest_point_to_segment_uncapped(point: Vector2, s1: Vector2, s2: Vector2)`
- `PackedVector2Array get_closest_points_between_segments(p1: Vector2, q1: Vector2, p2: Vector2, q2: Vector2)`
- `Array[PackedVector2Array] intersect_polygons(polygon_a: PackedVector2Array, polygon_b: PackedVector2Array)`
- `Array[PackedVector2Array] intersect_polyline_with_polygon(polyline: PackedVector2Array, polygon: PackedVector2Array)`
- `bool is_point_in_circle(point: Vector2, circle_position: Vector2, circle_radius: float)`
- `bool is_point_in_polygon(point: Vector2, polygon: PackedVector2Array)`
- `bool is_polygon_clockwise(polygon: PackedVector2Array)`
- `Variant line_intersects_line(from_a: Vector2, dir_a: Vector2, from_b: Vector2, dir_b: Vector2)`
- `Dictionary make_atlas(sizes: PackedVector2Array)`
- `Array[PackedVector2Array] merge_polygons(polygon_a: PackedVector2Array, polygon_b: PackedVector2Array)`
- `Array[PackedVector2Array] offset_polygon(polygon: PackedVector2Array, delta: float, join_type: PolyJoinType = 0)`
- `Array[PackedVector2Array] offset_polyline(polyline: PackedVector2Array, delta: float, join_type: PolyJoinType = 0, end_type: PolyEndType = 3)`
- `bool point_is_inside_triangle(point: Vector2, a: Vector2, b: Vector2, c: Vector2) const`
- `float segment_intersects_circle(segment_from: Vector2, segment_to: Vector2, circle_position: Vector2, circle_radius: float)`
- `Variant segment_intersects_segment(from_a: Vector2, to_a: Vector2, from_b: Vector2, to_b: Vector2)`
- `PackedInt32Array triangulate_delaunay(points: PackedVector2Array)`
- `PackedInt32Array triangulate_polygon(polygon: PackedVector2Array)`

**GDScript Examples**
```gdscript
var from_a = Vector2.ZERO
var dir_a = Vector2.RIGHT
var from_b = Vector2.DOWN

# Returns Vector2(1, 0)
Geometry2D.line_intersects_line(from_a, dir_a, from_b, Vector2(1, -1))
# Returns Vector2(-1, 0)
Geometry2D.line_intersects_line(from_a, dir_a, from_b, Vector2(-1, -1))
# Returns null
Geometry2D.line_intersects_line(from_a, dir_a, from_b, Vector2.RIGHT)
```
```gdscript
var polygon = PackedVector2Array([Vector2(0, 0), Vector2(100, 0), Vector2(100, 100), Vector2(0, 100)])
var offset = Vector2(50, 50)
polygon = Transform2D(0, offset) * polygon
print(polygon) # Prints [(50.0, 50.0), (150.0, 50.0), (150.0, 150.0), (50.0, 150.0)]
```

### Geometry3D
*Inherits: **Object***

Provides a set of helper functions to create geometric shapes, compute intersections between shapes, and process various other geometric operations in 3D.

**Methods**
- `Array[Plane] build_box_planes(extents: Vector3)`
- `Array[Plane] build_capsule_planes(radius: float, height: float, sides: int, lats: int, axis: Axis = 2)`
- `Array[Plane] build_cylinder_planes(radius: float, height: float, sides: int, axis: Axis = 2)`
- `PackedVector3Array clip_polygon(points: PackedVector3Array, plane: Plane)`
- `PackedVector3Array compute_convex_mesh_points(planes: Array[Plane])`
- `Vector3 get_closest_point_to_segment(point: Vector3, s1: Vector3, s2: Vector3)`
- `Vector3 get_closest_point_to_segment_uncapped(point: Vector3, s1: Vector3, s2: Vector3)`
- `PackedVector3Array get_closest_points_between_segments(p1: Vector3, p2: Vector3, q1: Vector3, q2: Vector3)`
- `Vector3 get_triangle_barycentric_coords(point: Vector3, a: Vector3, b: Vector3, c: Vector3)`
- `Variant ray_intersects_triangle(from: Vector3, dir: Vector3, a: Vector3, b: Vector3, c: Vector3)`
- `PackedVector3Array segment_intersects_convex(from: Vector3, to: Vector3, planes: Array[Plane])`
- `PackedVector3Array segment_intersects_cylinder(from: Vector3, to: Vector3, height: float, radius: float)`
- `PackedVector3Array segment_intersects_sphere(from: Vector3, to: Vector3, sphere_position: Vector3, sphere_radius: float)`
- `Variant segment_intersects_triangle(from: Vector3, to: Vector3, a: Vector3, b: Vector3, c: Vector3)`
- `PackedInt32Array tetrahedralize_delaunay(points: PackedVector3Array)`

### GodotInstance
*Inherits: **Object***

GodotInstance represents a running Godot instance that is controlled from an outside codebase, without a perpetual main loop. It is created by the C API libgodot_create_godot_instance. Only one may be created per process.

**Methods**
- `void focus_in()`
- `void focus_out()`
- `bool is_started()`
- `bool iteration()`
- `void pause()`
- `void resume()`
- `bool start()`

### GraphElement
*Inherits: **Container < Control < CanvasItem < Node < Object** | Inherited by: GraphFrame, GraphNode*

GraphElement allows to create custom elements for a GraphEdit graph. By default such elements can be selected, resized, and repositioned, but they cannot be connected. For a graph element that allows for connections see GraphNode.

**Properties**
- `bool draggable` = `true`
- `Vector2 position_offset` = `Vector2(0, 0)`
- `bool resizable` = `false`
- `bool scaling_menus` = `false`
- `bool selectable` = `true`
- `bool selected` = `false`

### GridMapEditorPlugin
*Inherits: **EditorPlugin < Node < Object***

GridMapEditorPlugin provides access to the GridMap editor functionality.

**Methods**
- `void clear_selection()`
- `GridMap get_current_grid_map() const`
- `Array get_selected_cells() const`
- `int get_selected_palette_item() const`
- `AABB get_selection() const`
- `bool has_selection() const`
- `void set_selected_palette_item(item: int) const`
- `void set_selection(begin: Vector3i, end: Vector3i)`

### GridMap
*Inherits: **Node3D < Node < Object***

GridMap lets you place meshes on a grid interactively. It works both from the editor and from scripts, which can help you create in-game level editors.

**Properties**
- `bool bake_navigation` = `false`
- `bool cell_center_x` = `true`
- `bool cell_center_y` = `true`
- `bool cell_center_z` = `true`
- `int cell_octant_size` = `8`
- `float cell_scale` = `1.0`
- `Vector3 cell_size` = `Vector3(2, 2, 2)`
- `int collision_layer` = `1`
- `int collision_mask` = `1`
- `float collision_priority` = `1.0`
- `MeshLibrary mesh_library`
- `PhysicsMaterial physics_material`

**Methods**
- `void clear()`
- `void clear_baked_meshes()`
- `RID get_bake_mesh_instance(idx: int)`
- `Array get_bake_meshes()`
- `Basis get_basis_with_orthogonal_index(index: int) const`
- `int get_cell_item(position: Vector3i) const`
- `Basis get_cell_item_basis(position: Vector3i) const`
- `int get_cell_item_orientation(position: Vector3i) const`
- `bool get_collision_layer_value(layer_number: int) const`
- `bool get_collision_mask_value(layer_number: int) const`
- `Array get_meshes() const`
- `RID get_navigation_map() const`
- `int get_orthogonal_index_from_basis(basis: Basis) const`
- `Array[Vector3i] get_used_cells() const`
- `Array[Vector3i] get_used_cells_by_item(item: int) const`
- `Vector3i local_to_map(local_position: Vector3) const`
- `void make_baked_meshes(gen_lightmap_uv: bool = false, lightmap_uv_texel_size: float = 0.1)`
- `Vector3 map_to_local(map_position: Vector3i) const`
- `void resource_changed(resource: Resource)`
- `void set_cell_item(position: Vector3i, item: int, orientation: int = 0)`
- `void set_collision_layer_value(layer_number: int, value: bool)`
- `void set_collision_mask_value(layer_number: int, value: bool)`
- `void set_navigation_map(navigation_map: RID)`

### HFlowContainer
*Inherits: **FlowContainer < Container < Control < CanvasItem < Node < Object***

A variant of FlowContainer that can only arrange its child controls horizontally, wrapping them around at the borders. This is similar to how text in a book wraps around when no more words can fit on a line.

### HMACContext
*Inherits: **RefCounted < Object***

The HMACContext class is useful for advanced HMAC use cases, such as streaming the message as it supports creating the message over time rather than providing it all at once.

**Methods**
- `PackedByteArray finish()`
- `Error start(hash_type: HashType, key: PackedByteArray)`
- `Error update(data: PackedByteArray)`

**GDScript Examples**
```gdscript
extends Node
var ctx = HMACContext.new()

func _ready():
    var key = "supersecret".to_utf8_buffer()
    var err = ctx.start(HashingContext.HASH_SHA256, key)
    assert(err == OK)
    var msg1 = "this is ".to_utf8_buffer()
    var msg2 = "super duper secret".to_utf8_buffer()
    err = ctx.update(msg1)
    assert(err == OK)
    err = ctx.update(msg2)
    assert(err == OK)
    var hmac = ctx.finish()
    print(hmac.hex_encode())
```

### HSeparator
*Inherits: **Separator < Control < CanvasItem < Node < Object***

A horizontal separator used for separating other controls that are arranged vertically. HSeparator is purely visual and normally drawn as a StyleBoxLine.

### HeightMapShape3D
*Inherits: **Shape3D < Resource < RefCounted < Object***

A 3D heightmap shape, intended for use in physics to provide a shape for a CollisionShape3D. This type is most commonly used for terrain with vertices placed in a fixed-width grid.

**Properties**
- `PackedFloat32Array map_data` = `PackedFloat32Array(0, 0, 0, 0)`
- `int map_depth` = `2`
- `int map_width` = `2`

**Methods**
- `float get_max_height() const`
- `float get_min_height() const`
- `void update_map_data_from_image(image: Image, height_min: float, height_max: float)`

**GDScript Examples**
```gdscript
var heightmap_texture = ResourceLoader.load("res://heightmap_image.exr")
var heightmap_image = heightmap_texture.get_image()
heightmap_image.convert(Image.FORMAT_RF)

var height_min = 0.0
var height_max = 10.0

update_map_data_from_image(heightmap_image, height_min, height_max)
```

### IKModifier3D
*Inherits: **SkeletonModifier3D < Node3D < Node < Object** | Inherited by: ChainIK3D, TwoBoneIK3D*

Base class of SkeletonModifier3Ds that has some joint lists and applies inverse kinematics. This class has some structs, enums, and helper methods which are useful to solve inverse kinematics.

**Properties**
- `bool mutable_bone_axes` = `true`

**Methods**
- `void clear_settings()`
- `int get_setting_count() const`
- `void reset()`
- `void set_setting_count(count: int)`

### IP
*Inherits: **Object***

IP contains support functions for the Internet Protocol (IP). TCP/IP support is in different classes (see StreamPeerTCP and TCPServer). IP provides DNS hostname resolution support, both blocking and threaded.

**Methods**
- `void clear_cache(hostname: String = "")`
- `void erase_resolve_item(id: int)`
- `PackedStringArray get_local_addresses() const`
- `Array[Dictionary] get_local_interfaces() const`
- `String get_resolve_item_address(id: int) const`
- `Array get_resolve_item_addresses(id: int) const`
- `ResolverStatus get_resolve_item_status(id: int) const`
- `String resolve_hostname(host: String, ip_type: Type = 3)`
- `PackedStringArray resolve_hostname_addresses(host: String, ip_type: Type = 3)`
- `int resolve_hostname_queue_item(host: String, ip_type: Type = 3)`

**GDScript Examples**
```gdscript
{
    "index": "1", # Interface index.
    "name": "eth0", # Interface name.
    "friendly": "Ethernet One", # A friendly name (might be empty).
    "addresses": ["192.168.1.101"], # An array of IP addresses associated to this interface.
}
```

### ImageFormatLoaderExtension
*Inherits: **ImageFormatLoader < RefCounted < Object***

The engine supports multiple image formats out of the box (PNG, SVG, JPEG, WebP to name a few), but you can choose to implement support for additional image formats by extending this class.

**Methods**
- `PackedStringArray _get_recognized_extensions() virtual const`
- `Error _load_image(image: Image, fileaccess: FileAccess, flags: BitField[LoaderFlags], scale: float) virtual`
- `void add_format_loader()`
- `void remove_format_loader()`

### ImageFormatLoader
*Inherits: **RefCounted < Object** | Inherited by: ImageFormatLoaderExtension*

The engine supports multiple image formats out of the box (PNG, SVG, JPEG, WebP to name a few), but you can choose to implement support for additional image formats by extending ImageFormatLoaderExtension.

### Image
*Inherits: **Resource < RefCounted < Object***

Native image datatype. Contains image data which can be converted to an ImageTexture and provides commonly used image processing methods. The maximum width and height for an Image are MAX_WIDTH and MAX_HEIGHT.

**Properties**
- `Dictionary data` = `{ "data": PackedByteArray(), "format": "Lum8", "height": 0, "mipmaps": false, "width": 0 }`

**Methods**
- `void adjust_bcs(brightness: float, contrast: float, saturation: float)`
- `void blend_rect(src: Image, src_rect: Rect2i, dst: Vector2i)`
- `void blend_rect_mask(src: Image, mask: Image, src_rect: Rect2i, dst: Vector2i)`
- `void blit_rect(src: Image, src_rect: Rect2i, dst: Vector2i)`
- `void blit_rect_mask(src: Image, mask: Image, src_rect: Rect2i, dst: Vector2i)`
- `void bump_map_to_normal_map(bump_scale: float = 1.0)`
- `void clear_mipmaps()`
- `Error compress(mode: CompressMode, source: CompressSource = 0, astc_format: ASTCFormat = 0)`
- `Error compress_from_channels(mode: CompressMode, channels: UsedChannels, astc_format: ASTCFormat = 0)`
- `Dictionary compute_image_metrics(compared_image: Image, use_luma: bool)`
- `void convert(format: Format)`
- `void copy_from(src: Image)`
- `Image create(width: int, height: int, use_mipmaps: bool, format: Format) static`
- `Image create_empty(width: int, height: int, use_mipmaps: bool, format: Format) static`
- `Image create_from_data(width: int, height: int, use_mipmaps: bool, format: Format, data: PackedByteArray) static`
- `void crop(width: int, height: int)`
- `Error decompress()`
- `AlphaMode detect_alpha() const`
- `UsedChannels detect_used_channels(source: CompressSource = 0) const`
- `void fill(color: Color)`
- `void fill_rect(rect: Rect2i, color: Color)`
- `void fix_alpha_edges()`
- `void flip_x()`
- `void flip_y()`
- `Error generate_mipmaps(renormalize: bool = false)`
- `PackedByteArray get_data() const`
- `int get_data_size() const`
- `Format get_format() const`
- `int get_height() const`
- `int get_mipmap_count() const`
- `int get_mipmap_offset(mipmap: int) const`
- `Color get_pixel(x: int, y: int) const`
- `Color get_pixelv(point: Vector2i) const`
- `Image get_region(region: Rect2i) const`
- `Vector2i get_size() const`
- `Rect2i get_used_rect() const`
- `int get_width() const`
- `bool has_mipmaps() const`
- `bool is_compressed() const`
- `bool is_empty() const`

**GDScript Examples**
```gdscript
var img_width = 10
var img_height = 5
var img = Image.create(img_width, img_height, false, Image.FORMAT_RGBA8)

img.set_pixel(1, 2, Color.RED) # Sets the color at (1, 2) to red.
```
```gdscript
var img_width = 10
var img_height = 5
var img = Image.create(img_width, img_height, false, Image.FORMAT_RGBA8)

img.set_pixelv(Vector2i(1, 2), Color.RED) # Sets the color at (1, 2) to red.
```

### ImporterMeshInstance3D
*Inherits: **Node3D < Node < Object***

There is currently no description for this class. Please help us by contributing one!

**Properties**
- `ShadowCastingSetting cast_shadow` = `1`
- `int layer_mask` = `1`
- `ImporterMesh mesh`
- `NodePath skeleton_path` = `NodePath("")`
- `Skin skin`
- `float visibility_range_begin` = `0.0`
- `float visibility_range_begin_margin` = `0.0`
- `float visibility_range_end` = `0.0`
- `float visibility_range_end_margin` = `0.0`
- `VisibilityRangeFadeMode visibility_range_fade_mode` = `0`

### ImporterMesh
*Inherits: **Resource < RefCounted < Object***

ImporterMesh is a type of Resource analogous to ArrayMesh. It contains vertex array-based geometry, divided in surfaces. Each surface contains a completely separate array and a material used to draw it. Design wise, a mesh with multiple surfaces is preferred to a single surface, because objects created in 3D editing software commonly contain multiple materials.

**Methods**
- `void add_blend_shape(name: String)`
- `void add_surface(primitive: PrimitiveType, arrays: Array, blend_shapes: Array[Array] = [], lods: Dictionary = {}, material: Material = null, name: String = "", flags: int = 0)`
- `void clear()`
- `ImporterMesh from_mesh(mesh: Mesh) static`
- `void generate_lods(normal_merge_angle: float, normal_split_angle: float, bone_transform_array: Array)`
- `int get_blend_shape_count() const`
- `BlendShapeMode get_blend_shape_mode() const`
- `String get_blend_shape_name(blend_shape_idx: int) const`
- `Vector2i get_lightmap_size_hint() const`
- `ArrayMesh get_mesh(base_mesh: ArrayMesh = null)`
- `Array get_surface_arrays(surface_idx: int) const`
- `Array get_surface_blend_shape_arrays(surface_idx: int, blend_shape_idx: int) const`
- `int get_surface_count() const`
- `int get_surface_format(surface_idx: int) const`
- `int get_surface_lod_count(surface_idx: int) const`
- `PackedInt32Array get_surface_lod_indices(surface_idx: int, lod_idx: int) const`
- `float get_surface_lod_size(surface_idx: int, lod_idx: int) const`
- `Material get_surface_material(surface_idx: int) const`
- `String get_surface_name(surface_idx: int) const`
- `PrimitiveType get_surface_primitive_type(surface_idx: int)`
- `void set_blend_shape_mode(mode: BlendShapeMode)`
- `void set_lightmap_size_hint(size: Vector2i)`
- `void set_surface_material(surface_idx: int, material: Material)`
- `void set_surface_name(surface_idx: int, name: String)`

### Input
*Inherits: **Object***

The Input singleton handles key presses, mouse buttons and movement, gamepads, and input actions. Actions and their events can be set in the Input Map tab in Project > Project Settings, or with the InputMap class.

**Properties**
- `bool emulate_mouse_from_touch`
- `bool emulate_touch_from_mouse`
- `MouseMode mouse_mode`
- `bool use_accumulated_input`

**Methods**
- `void action_press(action: StringName, strength: float = 1.0)`
- `void action_release(action: StringName)`
- `void add_joy_mapping(mapping: String, update_existing: bool = false)`
- `void flush_buffered_events()`
- `Vector3 get_accelerometer() const`
- `float get_action_raw_strength(action: StringName, exact_match: bool = false) const`
- `float get_action_strength(action: StringName, exact_match: bool = false) const`
- `float get_axis(negative_action: StringName, positive_action: StringName) const`
- `Array[int] get_connected_joypads()`
- `CursorShape get_current_cursor_shape() const`
- `Vector3 get_gravity() const`
- `Vector3 get_gyroscope() const`
- `float get_joy_axis(device: int, axis: JoyAxis) const`
- `String get_joy_guid(device: int) const`
- `Dictionary get_joy_info(device: int) const`
- `String get_joy_name(device: int)`
- `float get_joy_vibration_duration(device: int)`
- `Vector2 get_joy_vibration_strength(device: int)`
- `Vector2 get_last_mouse_screen_velocity()`
- `Vector2 get_last_mouse_velocity()`
- `Vector3 get_magnetometer() const`
- `BitField[MouseButtonMask] get_mouse_button_mask() const`
- `Vector2 get_vector(negative_x: StringName, positive_x: StringName, negative_y: StringName, positive_y: StringName, deadzone: float = -1.0) const`
- `bool has_joy_light(device: int) const`
- `bool is_action_just_pressed(action: StringName, exact_match: bool = false) const`
- `bool is_action_just_pressed_by_event(action: StringName, event: InputEvent, exact_match: bool = false) const`
- `bool is_action_just_released(action: StringName, exact_match: bool = false) const`
- `bool is_action_just_released_by_event(action: StringName, event: InputEvent, exact_match: bool = false) const`
- `bool is_action_pressed(action: StringName, exact_match: bool = false) const`
- `bool is_anything_pressed() const`
- `bool is_joy_button_pressed(device: int, button: JoyButton) const`
- `bool is_joy_known(device: int)`
- `bool is_key_label_pressed(keycode: Key) const`
- `bool is_key_pressed(keycode: Key) const`
- `bool is_mouse_button_pressed(button: MouseButton) const`
- `bool is_physical_key_pressed(keycode: Key) const`
- `void parse_input_event(event: InputEvent)`
- `void remove_joy_mapping(guid: String)`
- `void set_accelerometer(value: Vector3)`
- `void set_custom_mouse_cursor(image: Resource, shape: CursorShape = 0, hotspot: Vector2 = Vector2(0, 0))`

**GDScript Examples**
```gdscript
var cancel_event = InputEventAction.new()
cancel_event.action = "ui_cancel"
cancel_event.pressed = true
Input.parse_input_event(cancel_event)
```

### InstancePlaceholder
*Inherits: **Node < Object***

Turning on the option Load As Placeholder for an instantiated scene in the editor causes it to be replaced by an InstancePlaceholder when running the game, this will not replace the node in the editor. This makes it possible to delay actually loading the scene until calling create_instance(). This is useful to avoid loading large scenes all at once by loading parts of it selectively.

**Methods**
- `Node create_instance(replace: bool = false, custom_scene: PackedScene = null)`
- `String get_instance_path() const`
- `Dictionary get_stored_values(with_order: bool = false)`

### IterateIK3D
*Inherits: **ChainIK3D < IKModifier3D < SkeletonModifier3D < Node3D < Node < Object** | Inherited by: CCDIK3D, FABRIK3D, JacobianIK3D*

Base class of SkeletonModifier3D to approach the goal by repeating small rotations.

**Properties**
- `float angular_delta_limit` = `0.034906585`
- `bool deterministic` = `false`
- `int max_iterations` = `4`
- `float min_distance` = `0.001`
- `int setting_count` = `0`

**Methods**
- `JointLimitation3D get_joint_limitation(index: int, joint: int) const`
- `SecondaryDirection get_joint_limitation_right_axis(index: int, joint: int) const`
- `Vector3 get_joint_limitation_right_axis_vector(index: int, joint: int) const`
- `Quaternion get_joint_limitation_rotation_offset(index: int, joint: int) const`
- `RotationAxis get_joint_rotation_axis(index: int, joint: int) const`
- `Vector3 get_joint_rotation_axis_vector(index: int, joint: int) const`
- `NodePath get_target_node(index: int) const`
- `void set_joint_limitation(index: int, joint: int, limitation: JointLimitation3D)`
- `void set_joint_limitation_right_axis(index: int, joint: int, direction: SecondaryDirection)`
- `void set_joint_limitation_right_axis_vector(index: int, joint: int, vector: Vector3)`
- `void set_joint_limitation_rotation_offset(index: int, joint: int, offset: Quaternion)`
- `void set_joint_rotation_axis(index: int, joint: int, axis: RotationAxis)`
- `void set_joint_rotation_axis_vector(index: int, joint: int, axis_vector: Vector3)`
- `void set_target_node(index: int, target_node: NodePath)`

### JNISingleton
*Inherits: **Object***

The JNISingleton is implemented only in the Android export. It's used to call methods and connect signals from an Android plugin written in Java or Kotlin. Methods and signals can be called and connected to the JNISingleton as if it is a Node. See Java Native Interface - Wikipedia for more information.

**Methods**
- `bool has_java_method(method: StringName) const`

### JSONRPC
*Inherits: **Object***

JSON-RPC is a standard which wraps a method call in a JSON object. The object has a particular structure and identifies which method is called, the parameters to that function, and carries an ID to keep track of responses. This class implements that standard on top of Dictionary; you will have to convert between a Dictionary and JSON with other functions.

**Methods**
- `Dictionary make_notification(method: String, params: Variant)`
- `Dictionary make_request(method: String, params: Variant, id: Variant)`
- `Dictionary make_response(result: Variant, id: Variant)`
- `Dictionary make_response_error(code: int, message: String, id: Variant = null) const`
- `Variant process_action(action: Variant, recurse: bool = false)`
- `String process_string(action: String)`
- `void set_method(name: String, callback: Callable)`

### JSON
*Inherits: **Resource < RefCounted < Object***

The JSON class enables all data types to be converted to and from a JSON string. This is useful for serializing data, e.g. to save to a file or send over the network.

**Properties**
- `Variant data` = `null`

**Methods**
- `Variant from_native(variant: Variant, full_objects: bool = false) static`
- `int get_error_line() const`
- `String get_error_message() const`
- `String get_parsed_text() const`
- `Error parse(json_text: String, keep_text: bool = false)`
- `Variant parse_string(json_string: String) static`
- `String stringify(data: Variant, indent: String = "", sort_keys: bool = true, full_precision: bool = false) static`
- `Variant to_native(json: Variant, allow_objects: bool = false) static`

**GDScript Examples**
```gdscript
var data_to_send = ["a", "b", "c"]
var json_string = JSON.stringify(data_to_send)
# Save data
# ...
# Retrieve data
var json = JSON.new()
var error = json.parse(json_string)
if error == OK:
    var data_received = json.data
    if typeof(data_received) == TYPE_ARRAY:
        print(data_received) # Prints the array.
    else:
        print("Unexpected data")
else:
    print("JSON Parse Error: ", json.get_error_message(), " in ", json_string, " at line ", json.get_error_line())
```
```gdscript
var data = JSON.parse_string(json_string) # Returns null if parsing failed.
```

### JacobianIK3D
*Inherits: **IterateIK3D < ChainIK3D < IKModifier3D < SkeletonModifier3D < Node3D < Node < Object***

JacobianIK3D calculates rotations for all joints simultaneously, producing natural and smooth movement. It is particularly suited for biological animations.

### JavaClassWrapper
*Inherits: **Object***

The JavaClassWrapper singleton provides a way for the Godot application to send and receive data through the Java Native Interface (JNI).

**Methods**
- `JavaObject get_exception()`
- `JavaClass wrap(name: String)`

**GDScript Examples**
```gdscript
var LocalDateTime = JavaClassWrapper.wrap("java.time.LocalDateTime")
var DateTimeFormatter = JavaClassWrapper.wrap("java.time.format.DateTimeFormatter")

var datetime = LocalDateTime.now()
var formatter = DateTimeFormatter.ofPattern("dd-MM-yyyy HH:mm:ss")

print(datetime.format(formatter))
```
```gdscript
var Intent = JavaClassWrapper.wrap("android.content.Intent")
var intent = Intent.Intent()
```

### JavaClass
*Inherits: **RefCounted < Object***

Represents a class from the Java Native Interface. It is returned from JavaClassWrapper.wrap().

**Methods**
- `String get_java_class_name() const`
- `Array[Dictionary] get_java_method_list() const`
- `JavaClass get_java_parent_class() const`
- `bool has_java_method(method: StringName) const`

### JavaObject
*Inherits: **RefCounted < Object***

Represents an object from the Java Native Interface. It can be returned from Java methods called on JavaClass or other JavaObjects. See JavaClassWrapper for an example.

**Methods**
- `JavaClass get_java_class() const`
- `bool has_java_method(method: StringName) const`

### JavaScriptBridge
*Inherits: **Object***

The JavaScriptBridge singleton is implemented only in the Web export. It's used to access the browser's JavaScript context. This allows interaction with embedding pages or calling third-party JavaScript APIs.

**Methods**
- `JavaScriptObject create_callback(callable: Callable)`
- `Variant create_object(object: String, ...) vararg`
- `void download_buffer(buffer: PackedByteArray, name: String, mime: String = "application/octet-stream")`
- `Variant eval(code: String, use_global_execution_context: bool = false)`
- `void force_fs_sync()`
- `JavaScriptObject get_interface(interface: String)`
- `bool is_js_buffer(javascript_object: JavaScriptObject)`
- `PackedByteArray js_buffer_to_packed_byte_array(javascript_buffer: JavaScriptObject)`
- `bool pwa_needs_update() const`
- `Error pwa_update()`

### JavaScriptObject
*Inherits: **RefCounted < Object***

JavaScriptObject is used to interact with JavaScript objects retrieved or created via JavaScriptBridge.get_interface(), JavaScriptBridge.create_object(), or JavaScriptBridge.create_callback().

**GDScript Examples**
```gdscript
extends Node

var _my_js_callback = JavaScriptBridge.create_callback(myCallback) # This reference must be kept
var console = JavaScriptBridge.get_interface("console")

func _init():
    var buf = JavaScriptBridge.create_object("ArrayBuffer", 10) # new ArrayBuffer(10)
    print(buf) # Prints [JavaScriptObject:OBJECT_ID]
    var uint8arr = JavaScriptBridge.create_object("Uint8Array", buf) # new Uint8Array(buf)
    uint8arr[1] = 255
    prints(uint8arr[1], uint8arr.byteLength) # Prints "255 10"

    # Prints "Uint8Array(10) [ 0, 255, 0, 0, 0, 0, 0, 0, 0, 0 ]" in the browser's console.
    console
# ...
```

### JointLimitation3D
*Inherits: **Resource < RefCounted < Object** | Inherited by: JointLimitationCone3D*

The limitation is attached to each joint and limits the rotation of the bone.

### JointLimitationCone3D
*Inherits: **JointLimitation3D < Resource < RefCounted < Object***

A cone shape limitation that interacts with ChainIK3D.

**Properties**
- `float angle` = `1.5707964`

### KinematicCollision2D
*Inherits: **RefCounted < Object***

Holds collision data from the movement of a PhysicsBody2D, usually from PhysicsBody2D.move_and_collide(). When a PhysicsBody2D is moved, it stops if it detects a collision with another body. If a collision is detected, a KinematicCollision2D object is returned.

**Methods**
- `float get_angle(up_direction: Vector2 = Vector2(0, -1)) const`
- `Object get_collider() const`
- `int get_collider_id() const`
- `RID get_collider_rid() const`
- `Object get_collider_shape() const`
- `int get_collider_shape_index() const`
- `Vector2 get_collider_velocity() const`
- `float get_depth() const`
- `Object get_local_shape() const`
- `Vector2 get_normal() const`
- `Vector2 get_position() const`
- `Vector2 get_remainder() const`
- `Vector2 get_travel() const`

### KinematicCollision3D
*Inherits: **RefCounted < Object***

Holds collision data from the movement of a PhysicsBody3D, usually from PhysicsBody3D.move_and_collide(). When a PhysicsBody3D is moved, it stops if it detects a collision with another body. If a collision is detected, a KinematicCollision3D object is returned.

**Methods**
- `float get_angle(collision_index: int = 0, up_direction: Vector3 = Vector3(0, 1, 0)) const`
- `Object get_collider(collision_index: int = 0) const`
- `int get_collider_id(collision_index: int = 0) const`
- `RID get_collider_rid(collision_index: int = 0) const`
- `Object get_collider_shape(collision_index: int = 0) const`
- `int get_collider_shape_index(collision_index: int = 0) const`
- `Vector3 get_collider_velocity(collision_index: int = 0) const`
- `int get_collision_count() const`
- `float get_depth() const`
- `Object get_local_shape(collision_index: int = 0) const`
- `Vector3 get_normal(collision_index: int = 0) const`
- `Vector3 get_position(collision_index: int = 0) const`
- `Vector3 get_remainder() const`
- `Vector3 get_travel() const`

### Label3D
*Inherits: **GeometryInstance3D < VisualInstance3D < Node3D < Node < Object***

A node for displaying plain text in 3D space. By adjusting various properties of this node, you can configure things such as the text's appearance and whether it always faces the camera.

**Properties**
- `float alpha_antialiasing_edge` = `0.0`
- `AlphaAntiAliasing alpha_antialiasing_mode` = `0`
- `AlphaCutMode alpha_cut` = `0`
- `float alpha_hash_scale` = `1.0`
- `float alpha_scissor_threshold` = `0.5`
- `AutowrapMode autowrap_mode` = `0`
- `BitField[LineBreakFlag] autowrap_trim_flags` = `192`
- `BillboardMode billboard` = `0`
- `ShadowCastingSetting cast_shadow` = `0 (overrides GeometryInstance3D)`
- `bool double_sided` = `true`
- `bool fixed_size` = `false`
- `Font font`
- `int font_size` = `32`
- `GIMode gi_mode` = `0 (overrides GeometryInstance3D)`
- `HorizontalAlignment horizontal_alignment` = `1`
- `BitField[JustificationFlag] justification_flags` = `163`
- `String language` = `""`
- `float line_spacing` = `0.0`
- `Color modulate` = `Color(1, 1, 1, 1)`
- `bool no_depth_test` = `false`
- `Vector2 offset` = `Vector2(0, 0)`
- `Color outline_modulate` = `Color(0, 0, 0, 1)`
- `int outline_render_priority` = `-1`
- `int outline_size` = `12`
- `float pixel_size` = `0.005`
- `int render_priority` = `0`
- `bool shaded` = `false`
- `StructuredTextParser structured_text_bidi_override` = `0`
- `Array structured_text_bidi_override_options` = `[]`
- `String text` = `""`

**Methods**
- `TriangleMesh generate_triangle_mesh() const`
- `bool get_draw_flag(flag: DrawFlags) const`
- `void set_draw_flag(flag: DrawFlags, enabled: bool)`

### LabelSettings
*Inherits: **Resource < RefCounted < Object***

LabelSettings is a resource that provides common settings to customize the text in a Label. It will take priority over the properties defined in Control.theme. The resource can be shared between multiple labels and changed on the fly, so it's convenient and flexible way to setup text style.

**Properties**
- `Font font`
- `Color font_color` = `Color(1, 1, 1, 1)`
- `int font_size` = `16`
- `float line_spacing` = `3.0`
- `Color outline_color` = `Color(1, 1, 1, 1)`
- `int outline_size` = `0`
- `float paragraph_spacing` = `0.0`
- `Color shadow_color` = `Color(0, 0, 0, 0)`
- `Vector2 shadow_offset` = `Vector2(1, 1)`
- `int shadow_size` = `1`
- `int stacked_outline_count` = `0`
- `int stacked_shadow_count` = `0`

**Methods**
- `void add_stacked_outline(index: int = -1)`
- `void add_stacked_shadow(index: int = -1)`
- `Color get_stacked_outline_color(index: int) const`
- `int get_stacked_outline_size(index: int) const`
- `Color get_stacked_shadow_color(index: int) const`
- `Vector2 get_stacked_shadow_offset(index: int) const`
- `int get_stacked_shadow_outline_size(index: int) const`
- `void move_stacked_outline(from_index: int, to_position: int)`
- `void move_stacked_shadow(from_index: int, to_position: int)`
- `void remove_stacked_outline(index: int)`
- `void remove_stacked_shadow(index: int)`
- `void set_stacked_outline_color(index: int, color: Color)`
- `void set_stacked_outline_size(index: int, size: int)`
- `void set_stacked_shadow_color(index: int, color: Color)`
- `void set_stacked_shadow_offset(index: int, offset: Vector2)`
- `void set_stacked_shadow_outline_size(index: int, size: int)`

### Label
*Inherits: **Control < CanvasItem < Node < Object***

A control for displaying plain text. It gives you control over the horizontal and vertical alignment and can wrap the text inside the node's bounding rectangle. It doesn't support bold, italics, or other rich text formatting. For that, use RichTextLabel instead.

**Properties**
- `AutowrapMode autowrap_mode` = `0`
- `BitField[LineBreakFlag] autowrap_trim_flags` = `192`
- `bool clip_text` = `false`
- `String ellipsis_char` = `"…"`
- `HorizontalAlignment horizontal_alignment` = `0`
- `BitField[JustificationFlag] justification_flags` = `163`
- `LabelSettings label_settings`
- `String language` = `""`
- `int lines_skipped` = `0`
- `int max_lines_visible` = `-1`
- `MouseFilter mouse_filter` = `2 (overrides Control)`
- `String paragraph_separator` = `"\\n"`
- `BitField[SizeFlags] size_flags_vertical` = `4 (overrides Control)`
- `StructuredTextParser structured_text_bidi_override` = `0`
- `Array structured_text_bidi_override_options` = `[]`
- `PackedFloat32Array tab_stops` = `PackedFloat32Array()`
- `String text` = `""`
- `TextDirection text_direction` = `0`
- `OverrunBehavior text_overrun_behavior` = `0`
- `bool uppercase` = `false`
- `VerticalAlignment vertical_alignment` = `0`
- `int visible_characters` = `-1`
- `VisibleCharactersBehavior visible_characters_behavior` = `0`
- `float visible_ratio` = `1.0`

**Methods**
- `Rect2 get_character_bounds(pos: int) const`
- `int get_line_count() const`
- `int get_line_height(line: int = -1) const`
- `int get_total_character_count() const`
- `int get_visible_line_count() const`

### LightmapperRD
*Inherits: **Lightmapper < RefCounted < Object***

LightmapperRD ("RD" stands for RenderingDevice) is the built-in GPU-based lightmapper for use with LightmapGI. On most dedicated GPUs, it can bake lightmaps much faster than most CPU-based lightmappers. LightmapperRD uses compute shaders to bake lightmaps, so it does not require CUDA or OpenCL libraries to be installed to be usable.

### Lightmapper
*Inherits: **RefCounted < Object** | Inherited by: LightmapperRD*

This class should be extended by custom lightmapper classes. Lightmappers can then be used with LightmapGI to provide fast baked global illumination in 3D.

### LimitAngularVelocityModifier3D
*Inherits: **SkeletonModifier3D < Node3D < Node < Object***

This modifier limits bone rotation angular velocity by comparing poses between previous and current frame.

**Properties**
- `int chain_count` = `0`
- `bool exclude` = `false`
- `int joint_count` = `0`
- `float max_angular_velocity` = `6.2831855`

**Methods**
- `void clear_chains()`
- `int get_end_bone(index: int) const`
- `String get_end_bone_name(index: int) const`
- `int get_root_bone(index: int) const`
- `String get_root_bone_name(index: int) const`
- `void reset()`
- `void set_end_bone(index: int, bone: int)`
- `void set_end_bone_name(index: int, bone_name: String)`
- `void set_root_bone(index: int, bone: int)`
- `void set_root_bone_name(index: int, bone_name: String)`

### Logger
*Inherits: **RefCounted < Object***

Custom logger to receive messages from the internal error/warning stream. Loggers are registered via OS.add_logger().

**Methods**
- `void _log_error(function: String, file: String, line: int, code: String, rationale: String, editor_notify: bool, error_type: int, script_backtraces: Array[ScriptBacktrace]) virtual`
- `void _log_message(message: String, error: bool) virtual`

### MenuBar
*Inherits: **Control < CanvasItem < Node < Object***

A horizontal menu bar that creates a menu for each PopupMenu child. New items are created by adding PopupMenus to this node. Item title is determined by Window.title, or node name if Window.title is empty. Item title can be overridden using set_menu_title().

**Properties**
- `bool flat` = `false`
- `FocusMode focus_mode` = `3 (overrides Control)`
- `String language` = `""`
- `bool prefer_global_menu` = `true`
- `int start_index` = `-1`
- `bool switch_on_hover` = `true`
- `TextDirection text_direction` = `0`

**Methods**
- `int get_menu_count() const`
- `PopupMenu get_menu_popup(menu: int) const`
- `String get_menu_title(menu: int) const`
- `String get_menu_tooltip(menu: int) const`
- `bool is_menu_disabled(menu: int) const`
- `bool is_menu_hidden(menu: int) const`
- `bool is_native_menu() const`
- `void set_disable_shortcuts(disabled: bool)`
- `void set_menu_disabled(menu: int, disabled: bool)`
- `void set_menu_hidden(menu: int, hidden: bool)`
- `void set_menu_title(menu: int, title: String)`
- `void set_menu_tooltip(menu: int, tooltip: String)`

### MeshConvexDecompositionSettings
*Inherits: **RefCounted < Object***

Parameters to be used with a Mesh convex decomposition operation.

**Properties**
- `bool convex_hull_approximation` = `true`
- `int convex_hull_downsampling` = `4`
- `float max_concavity` = `1.0`
- `int max_convex_hulls` = `1`
- `int max_num_vertices_per_convex_hull` = `32`
- `float min_volume_per_convex_hull` = `0.0001`
- `Mode mode` = `0`
- `bool normalize_mesh` = `false`
- `int plane_downsampling` = `4`
- `bool project_hull_vertices` = `true`
- `int resolution` = `10000`
- `float revolution_axes_clipping_bias` = `0.05`
- `float symmetry_planes_clipping_bias` = `0.05`

### MeshLibrary
*Inherits: **Resource < RefCounted < Object***

A library of meshes. Contains a list of Mesh resources, each with a name and ID. Each item can also include collision and navigation shapes. This resource is used in GridMap.

**Methods**
- `void clear()`
- `void create_item(id: int)`
- `int find_item_by_name(name: String) const`
- `PackedInt32Array get_item_list() const`
- `Mesh get_item_mesh(id: int) const`
- `ShadowCastingSetting get_item_mesh_cast_shadow(id: int) const`
- `Transform3D get_item_mesh_transform(id: int) const`
- `String get_item_name(id: int) const`
- `int get_item_navigation_layers(id: int) const`
- `NavigationMesh get_item_navigation_mesh(id: int) const`
- `Transform3D get_item_navigation_mesh_transform(id: int) const`
- `Texture2D get_item_preview(id: int) const`
- `Array get_item_shapes(id: int) const`
- `int get_last_unused_item_id() const`
- `void remove_item(id: int)`
- `void set_item_mesh(id: int, mesh: Mesh)`
- `void set_item_mesh_cast_shadow(id: int, shadow_casting_setting: ShadowCastingSetting)`
- `void set_item_mesh_transform(id: int, mesh_transform: Transform3D)`
- `void set_item_name(id: int, name: String)`
- `void set_item_navigation_layers(id: int, navigation_layers: int)`
- `void set_item_navigation_mesh(id: int, navigation_mesh: NavigationMesh)`
- `void set_item_navigation_mesh_transform(id: int, navigation_mesh: Transform3D)`
- `void set_item_preview(id: int, texture: Texture2D)`
- `void set_item_shapes(id: int, shapes: Array)`

### MeshTexture
*Inherits: **Texture2D < Texture < Resource < RefCounted < Object***

Simple texture that uses a mesh to draw itself. It's limited because flags can't be changed and region drawing is not supported.

**Properties**
- `Texture2D base_texture`
- `Vector2 image_size` = `Vector2(0, 0)`
- `Mesh mesh`
- `bool resource_local_to_scene` = `false (overrides Resource)`

### Mesh
*Inherits: **Resource < RefCounted < Object** | Inherited by: ArrayMesh, ImmediateMesh, PlaceholderMesh, PrimitiveMesh*

Mesh is a type of Resource that contains vertex array-based geometry, divided in surfaces. Each surface contains a completely separate array and a material used to draw it. Design wise, a mesh with multiple surfaces is preferred to a single surface, because objects created in 3D editing software commonly contain multiple materials. The maximum number of surfaces per mesh is RenderingServer.MAX_MESH_SURFACES.

**Properties**
- `Vector2i lightmap_size_hint` = `Vector2i(0, 0)`

**Methods**
- `AABB _get_aabb() virtual required const`
- `int _get_blend_shape_count() virtual required const`
- `StringName _get_blend_shape_name(index: int) virtual required const`
- `int _get_surface_count() virtual required const`
- `void _set_blend_shape_name(index: int, name: StringName) virtual required`
- `int _surface_get_array_index_len(index: int) virtual required const`
- `int _surface_get_array_len(index: int) virtual required const`
- `Array _surface_get_arrays(index: int) virtual required const`
- `Array[Array] _surface_get_blend_shape_arrays(index: int) virtual required const`
- `int _surface_get_format(index: int) virtual required const`
- `Dictionary _surface_get_lods(index: int) virtual required const`
- `Material _surface_get_material(index: int) virtual required const`
- `int _surface_get_primitive_type(index: int) virtual required const`
- `void _surface_set_material(index: int, material: Material) virtual required`
- `ConvexPolygonShape3D create_convex_shape(clean: bool = true, simplify: bool = false) const`
- `Mesh create_outline(margin: float) const`
- `Resource create_placeholder() const`
- `ConcavePolygonShape3D create_trimesh_shape() const`
- `TriangleMesh generate_triangle_mesh() const`
- `AABB get_aabb() const`
- `PackedVector3Array get_faces() const`
- `int get_surface_count() const`
- `Array surface_get_arrays(surf_idx: int) const`
- `Array[Array] surface_get_blend_shape_arrays(surf_idx: int) const`
- `Material surface_get_material(surf_idx: int) const`
- `void surface_set_material(surf_idx: int, material: Material)`

### MissingNode
*Inherits: **Node < Object***

This is an internal editor class intended for keeping data of nodes of unknown type (most likely this type was supplied by an extension that is no longer loaded). It can't be manually instantiated or placed in a scene.

**Properties**
- `String original_class`
- `String original_scene`
- `bool recording_properties`
- `bool recording_signals`

### MissingResource
*Inherits: **Resource < RefCounted < Object***

This is an internal editor class intended for keeping data of resources of unknown type (most likely this type was supplied by an extension that is no longer loaded). It can't be manually instantiated or placed in a scene.

**Properties**
- `String original_class`
- `bool recording_properties`

### MobileVRInterface
*Inherits: **XRInterface < RefCounted < Object***

This is a generic mobile VR implementation where you need to provide details about the phone and HMD used. It does not rely on any existing framework. This is the most basic interface we have. For the best effect, you need a mobile phone with a gyroscope and accelerometer.

**Properties**
- `float display_to_lens` = `4.0`
- `float display_width` = `14.5`
- `float eye_height` = `1.85`
- `float iod` = `6.0`
- `float k1` = `0.215`
- `float k2` = `0.215`
- `Rect2 offset_rect` = `Rect2(0, 0, 1, 1)`
- `float oversample` = `1.5`
- `float vrs_min_radius` = `20.0`
- `float vrs_strength` = `1.0`
- `PlayAreaMode xr_play_area_mode` = `1 (overrides XRInterface)`

**GDScript Examples**
```gdscript
var interface = XRServer.find_interface("Native mobile")
if interface and interface.initialize():
    get_viewport().use_xr = true
```

### ModifierBoneTarget3D
*Inherits: **SkeletonModifier3D < Node3D < Node < Object***

This node selects a bone in a Skeleton3D and attaches to it. This means that the ModifierBoneTarget3D node will dynamically copy the 3D transform of the selected bone.

**Properties**
- `int bone` = `-1`
- `String bone_name` = `""`

### MovieWriter
*Inherits: **Object***

Godot can record videos with non-real-time simulation. Like the --fixed-fps command line argument, this forces the reported delta in Node._process() functions to be identical across frames, regardless of how long it actually took to render the frame. This can be used to record high-quality videos with perfect frame pacing regardless of your hardware's capabilities.

**Methods**
- `int _get_audio_mix_rate() virtual required const`
- `SpeakerMode _get_audio_speaker_mode() virtual required const`
- `bool _handles_file(path: String) virtual required const`
- `Error _write_begin(movie_size: Vector2i, fps: int, base_path: String) virtual required`
- `void _write_end() virtual required`
- `Error _write_frame(frame_image: Image, audio_frame_block: const void*) virtual required`
- `void add_writer(writer: MovieWriter) static`

**GDScript Examples**
```gdscript
func _handles_file(path):
    # Allows specifying an output file with a `.mkv` file extension (case-insensitive),
    # either in the Project Settings or with the `--write-movie <path>` command line argument.
    return path.get_extension().to_lower() == "mkv"
```

### MultiplayerSpawner
*Inherits: **Node < Object***

Spawnable scenes can be configured in the editor or through code (see add_spawnable_scene()).

**Properties**
- `Callable spawn_function`
- `int spawn_limit` = `0`
- `NodePath spawn_path` = `NodePath("")`

**Methods**
- `void add_spawnable_scene(path: String)`
- `void clear_spawnable_scenes()`
- `String get_spawnable_scene(index: int) const`
- `int get_spawnable_scene_count() const`
- `Node spawn(data: Variant = null)`

### MultiplayerSynchronizer
*Inherits: **Node < Object***

By default, MultiplayerSynchronizer synchronizes configured properties to all peers.

**Properties**
- `float delta_interval` = `0.0`
- `bool public_visibility` = `true`
- `SceneReplicationConfig replication_config`
- `float replication_interval` = `0.0`
- `NodePath root_path` = `NodePath("..")`
- `VisibilityUpdateMode visibility_update_mode` = `0`

**Methods**
- `void add_visibility_filter(filter: Callable)`
- `bool get_visibility_for(peer: int) const`
- `void remove_visibility_filter(filter: Callable)`
- `void set_visibility_for(peer: int, visible: bool)`
- `void update_visibility(for_peer: int = 0)`

### Mutex
*Inherits: **RefCounted < Object***

A synchronization mutex (mutual exclusion). This is used to synchronize multiple Threads, and is equivalent to a binary Semaphore. It guarantees that only one thread can access a critical section at a time.

**Methods**
- `void lock()`
- `bool try_lock()`
- `void unlock()`

### NativeMenu
*Inherits: **Object***

NativeMenu handles low-level access to the OS native global menu bar and popup menus.

**Methods**
- `int add_check_item(rid: RID, label: String, callback: Callable = Callable(), key_callback: Callable = Callable(), tag: Variant = null, accelerator: Key = 0, index: int = -1)`
- `int add_icon_check_item(rid: RID, icon: Texture2D, label: String, callback: Callable = Callable(), key_callback: Callable = Callable(), tag: Variant = null, accelerator: Key = 0, index: int = -1)`
- `int add_icon_item(rid: RID, icon: Texture2D, label: String, callback: Callable = Callable(), key_callback: Callable = Callable(), tag: Variant = null, accelerator: Key = 0, index: int = -1)`
- `int add_icon_radio_check_item(rid: RID, icon: Texture2D, label: String, callback: Callable = Callable(), key_callback: Callable = Callable(), tag: Variant = null, accelerator: Key = 0, index: int = -1)`
- `int add_item(rid: RID, label: String, callback: Callable = Callable(), key_callback: Callable = Callable(), tag: Variant = null, accelerator: Key = 0, index: int = -1)`
- `int add_multistate_item(rid: RID, label: String, max_states: int, default_state: int, callback: Callable = Callable(), key_callback: Callable = Callable(), tag: Variant = null, accelerator: Key = 0, index: int = -1)`
- `int add_radio_check_item(rid: RID, label: String, callback: Callable = Callable(), key_callback: Callable = Callable(), tag: Variant = null, accelerator: Key = 0, index: int = -1)`
- `int add_separator(rid: RID, index: int = -1)`
- `int add_submenu_item(rid: RID, label: String, submenu_rid: RID, tag: Variant = null, index: int = -1)`
- `void clear(rid: RID)`
- `RID create_menu()`
- `int find_item_index_with_submenu(rid: RID, submenu_rid: RID) const`
- `int find_item_index_with_tag(rid: RID, tag: Variant) const`
- `int find_item_index_with_text(rid: RID, text: String) const`
- `void free_menu(rid: RID)`
- `Key get_item_accelerator(rid: RID, idx: int) const`
- `Callable get_item_callback(rid: RID, idx: int) const`
- `int get_item_count(rid: RID) const`
- `Texture2D get_item_icon(rid: RID, idx: int) const`
- `int get_item_indentation_level(rid: RID, idx: int) const`
- `Callable get_item_key_callback(rid: RID, idx: int) const`
- `int get_item_max_states(rid: RID, idx: int) const`
- `int get_item_state(rid: RID, idx: int) const`
- `RID get_item_submenu(rid: RID, idx: int) const`
- `Variant get_item_tag(rid: RID, idx: int) const`
- `String get_item_text(rid: RID, idx: int) const`
- `String get_item_tooltip(rid: RID, idx: int) const`
- `float get_minimum_width(rid: RID) const`
- `Callable get_popup_close_callback(rid: RID) const`
- `Callable get_popup_open_callback(rid: RID) const`
- `Vector2 get_size(rid: RID) const`
- `RID get_system_menu(menu_id: SystemMenus) const`
- `String get_system_menu_name(menu_id: SystemMenus) const`
- `String get_system_menu_text(menu_id: SystemMenus) const`
- `bool has_feature(feature: Feature) const`
- `bool has_menu(rid: RID) const`
- `bool has_system_menu(menu_id: SystemMenus) const`
- `bool is_item_checkable(rid: RID, idx: int) const`
- `bool is_item_checked(rid: RID, idx: int) const`
- `bool is_item_disabled(rid: RID, idx: int) const`

**GDScript Examples**
```gdscript
var menu

func _menu_callback(item_id):
    if item_id == "ITEM_CUT":
        cut()
    elif item_id == "ITEM_COPY":
        copy()
    elif item_id == "ITEM_PASTE":
        paste()

func _enter_tree():
    # Create new menu and add items:
    menu = NativeMenu.create_menu()
    NativeMenu.add_item(menu, "Cut", _menu_callback, Callable(), "ITEM_CUT")
    NativeMenu.add_item(menu, "Copy", _menu_callback, Callable(), "ITEM_COPY")
    NativeMenu.add_separator(menu)
    NativeMenu.add_item(menu, "Paste", _menu_callback, Callable(), "ITEM_PASTE")

func _on_button_pressed():
    # Show popup menu at
# ...
```

### NavigationMeshGenerator
*Inherits: **Object***

This class is responsible for creating and clearing 3D navigation meshes used as NavigationMesh resources inside NavigationRegion3D. The NavigationMeshGenerator has very limited to no use for 2D as the navigation mesh baking process expects 3D node types and 3D source geometry to parse.

**Methods**
- `void bake(navigation_mesh: NavigationMesh, root_node: Node)`
- `void bake_from_source_geometry_data(navigation_mesh: NavigationMesh, source_geometry_data: NavigationMeshSourceGeometryData3D, callback: Callable = Callable())`
- `void clear(navigation_mesh: NavigationMesh)`
- `void parse_source_geometry_data(navigation_mesh: NavigationMesh, source_geometry_data: NavigationMeshSourceGeometryData3D, root_node: Node, callback: Callable = Callable())`

### NavigationMeshSourceGeometryData2D
*Inherits: **Resource < RefCounted < Object***

Container for parsed source geometry data used in navigation mesh baking.

**Methods**
- `void add_obstruction_outline(shape_outline: PackedVector2Array)`
- `void add_projected_obstruction(vertices: PackedVector2Array, carve: bool)`
- `void add_traversable_outline(shape_outline: PackedVector2Array)`
- `void append_obstruction_outlines(obstruction_outlines: Array[PackedVector2Array])`
- `void append_traversable_outlines(traversable_outlines: Array[PackedVector2Array])`
- `void clear()`
- `void clear_projected_obstructions()`
- `Rect2 get_bounds()`
- `Array[PackedVector2Array] get_obstruction_outlines() const`
- `Array get_projected_obstructions() const`
- `Array[PackedVector2Array] get_traversable_outlines() const`
- `bool has_data()`
- `void merge(other_geometry: NavigationMeshSourceGeometryData2D)`
- `void set_obstruction_outlines(obstruction_outlines: Array[PackedVector2Array])`
- `void set_projected_obstructions(projected_obstructions: Array)`
- `void set_traversable_outlines(traversable_outlines: Array[PackedVector2Array])`

**GDScript Examples**
```gdscript
"vertices" : PackedFloat32Array
"carve" : bool
```

### NavigationMeshSourceGeometryData3D
*Inherits: **Resource < RefCounted < Object***

Container for parsed source geometry data used in navigation mesh baking.

**Methods**
- `void add_faces(faces: PackedVector3Array, xform: Transform3D)`
- `void add_mesh(mesh: Mesh, xform: Transform3D)`
- `void add_mesh_array(mesh_array: Array, xform: Transform3D)`
- `void add_projected_obstruction(vertices: PackedVector3Array, elevation: float, height: float, carve: bool)`
- `void append_arrays(vertices: PackedFloat32Array, indices: PackedInt32Array)`
- `void clear()`
- `void clear_projected_obstructions()`
- `AABB get_bounds()`
- `PackedInt32Array get_indices() const`
- `Array get_projected_obstructions() const`
- `PackedFloat32Array get_vertices() const`
- `bool has_data()`
- `void merge(other_geometry: NavigationMeshSourceGeometryData3D)`
- `void set_indices(indices: PackedInt32Array)`
- `void set_projected_obstructions(projected_obstructions: Array)`
- `void set_vertices(vertices: PackedFloat32Array)`

**GDScript Examples**
```gdscript
"vertices" : PackedFloat32Array
"elevation" : float
"height" : float
"carve" : bool
```

### NavigationMesh
*Inherits: **Resource < RefCounted < Object***

A navigation mesh is a collection of polygons that define which areas of an environment are traversable to aid agents in pathfinding through complicated spaces.

**Properties**
- `float agent_height` = `1.5`
- `float agent_max_climb` = `0.25`
- `float agent_max_slope` = `45.0`
- `float agent_radius` = `0.5`
- `float border_size` = `0.0`
- `float cell_height` = `0.25`
- `float cell_size` = `0.25`
- `float detail_sample_distance` = `6.0`
- `float detail_sample_max_error` = `1.0`
- `float edge_max_error` = `1.3`
- `float edge_max_length` = `0.0`
- `AABB filter_baking_aabb` = `AABB(0, 0, 0, 0, 0, 0)`
- `Vector3 filter_baking_aabb_offset` = `Vector3(0, 0, 0)`
- `bool filter_ledge_spans` = `false`
- `bool filter_low_hanging_obstacles` = `false`
- `bool filter_walkable_low_height_spans` = `false`
- `int geometry_collision_mask` = `4294967295`
- `ParsedGeometryType geometry_parsed_geometry_type` = `2`
- `SourceGeometryMode geometry_source_geometry_mode` = `0`
- `StringName geometry_source_group_name` = `&"navigation_mesh_source_group"`
- `float region_merge_size` = `20.0`
- `float region_min_size` = `2.0`
- `SamplePartitionType sample_partition_type` = `0`
- `float vertices_per_polygon` = `6.0`

**Methods**
- `void add_polygon(polygon: PackedInt32Array)`
- `void clear()`
- `void clear_polygons()`
- `void create_from_mesh(mesh: Mesh)`
- `bool get_collision_mask_value(layer_number: int) const`
- `PackedInt32Array get_polygon(idx: int)`
- `int get_polygon_count() const`
- `PackedVector3Array get_vertices() const`
- `void set_collision_mask_value(layer_number: int, value: bool)`
- `void set_vertices(vertices: PackedVector3Array)`

### NavigationPathQueryParameters2D
*Inherits: **RefCounted < Object***

By changing various properties of this object, such as the start and target position, you can configure path queries to the NavigationServer2D.

**Properties**
- `Array[RID] excluded_regions` = `[]`
- `Array[RID] included_regions` = `[]`
- `RID map` = `RID()`
- `BitField[PathMetadataFlags] metadata_flags` = `7`
- `int navigation_layers` = `1`
- `PathPostProcessing path_postprocessing` = `0`
- `float path_return_max_length` = `0.0`
- `float path_return_max_radius` = `0.0`
- `float path_search_max_distance` = `0.0`
- `int path_search_max_polygons` = `4096`
- `PathfindingAlgorithm pathfinding_algorithm` = `0`
- `float simplify_epsilon` = `0.0`
- `bool simplify_path` = `false`
- `Vector2 start_position` = `Vector2(0, 0)`
- `Vector2 target_position` = `Vector2(0, 0)`

### NavigationPathQueryParameters3D
*Inherits: **RefCounted < Object***

By changing various properties of this object, such as the start and target position, you can configure path queries to the NavigationServer3D.

**Properties**
- `Array[RID] excluded_regions` = `[]`
- `Array[RID] included_regions` = `[]`
- `RID map` = `RID()`
- `BitField[PathMetadataFlags] metadata_flags` = `7`
- `int navigation_layers` = `1`
- `PathPostProcessing path_postprocessing` = `0`
- `float path_return_max_length` = `0.0`
- `float path_return_max_radius` = `0.0`
- `float path_search_max_distance` = `0.0`
- `int path_search_max_polygons` = `4096`
- `PathfindingAlgorithm pathfinding_algorithm` = `0`
- `float simplify_epsilon` = `0.0`
- `bool simplify_path` = `false`
- `Vector3 start_position` = `Vector3(0, 0, 0)`
- `Vector3 target_position` = `Vector3(0, 0, 0)`

### NavigationPathQueryResult2D
*Inherits: **RefCounted < Object***

This class stores the result of a 2D navigation path query from the NavigationServer2D.

**Properties**
- `PackedVector2Array path` = `PackedVector2Array()`
- `float path_length` = `0.0`
- `PackedInt64Array path_owner_ids` = `PackedInt64Array()`
- `Array[RID] path_rids` = `[]`
- `PackedInt32Array path_types` = `PackedInt32Array()`

**Methods**
- `void reset()`

### NavigationPathQueryResult3D
*Inherits: **RefCounted < Object***

This class stores the result of a 3D navigation path query from the NavigationServer3D.

**Properties**
- `PackedVector3Array path` = `PackedVector3Array()`
- `float path_length` = `0.0`
- `PackedInt64Array path_owner_ids` = `PackedInt64Array()`
- `Array[RID] path_rids` = `[]`
- `PackedInt32Array path_types` = `PackedInt32Array()`

**Methods**
- `void reset()`

### NavigationPolygon
*Inherits: **Resource < RefCounted < Object***

A navigation mesh can be created either by baking it with the help of the NavigationServer2D, or by adding vertices and convex polygon indices arrays manually.

**Properties**
- `float agent_radius` = `10.0`
- `Rect2 baking_rect` = `Rect2(0, 0, 0, 0)`
- `Vector2 baking_rect_offset` = `Vector2(0, 0)`
- `float border_size` = `0.0`
- `float cell_size` = `1.0`
- `int parsed_collision_mask` = `4294967295`
- `ParsedGeometryType parsed_geometry_type` = `2`
- `SamplePartitionType sample_partition_type` = `0`
- `StringName source_geometry_group_name` = `&"navigation_polygon_source_geometry_group"`
- `SourceGeometryMode source_geometry_mode` = `0`

**Methods**
- `void add_outline(outline: PackedVector2Array)`
- `void add_outline_at_index(outline: PackedVector2Array, index: int)`
- `void add_polygon(polygon: PackedInt32Array)`
- `void clear()`
- `void clear_outlines()`
- `void clear_polygons()`
- `NavigationMesh get_navigation_mesh()`
- `PackedVector2Array get_outline(idx: int) const`
- `int get_outline_count() const`
- `bool get_parsed_collision_mask_value(layer_number: int) const`
- `PackedInt32Array get_polygon(idx: int)`
- `int get_polygon_count() const`
- `PackedVector2Array get_vertices() const`
- `void make_polygons_from_outlines()`
- `void remove_outline(idx: int)`
- `void set_outline(idx: int, outline: PackedVector2Array)`
- `void set_parsed_collision_mask_value(layer_number: int, value: bool)`
- `void set_vertices(vertices: PackedVector2Array)`

**GDScript Examples**
```gdscript
var new_navigation_mesh = NavigationPolygon.new()
var bounding_outline = PackedVector2Array([Vector2(0, 0), Vector2(0, 50), Vector2(50, 50), Vector2(50, 0)])
new_navigation_mesh.add_outline(bounding_outline)
NavigationServer2D.bake_from_source_geometry_data(new_navigation_mesh, NavigationMeshSourceGeometryData2D.new());
$NavigationRegion2D.navigation_polygon = new_navigation_mesh
```
```gdscript
var new_navigation_mesh = NavigationPolygon.new()
var new_vertices = PackedVector2Array([Vector2(0, 0), Vector2(0, 50), Vector2(50, 50), Vector2(50, 0)])
new_navigation_mesh.vertices = new_vertices
var new_polygon_indices = PackedInt32Array([0, 1, 2, 3])
new_navigation_mesh.add_polygon(new_polygon_indices)
$NavigationRegion2D.navigation_polygon = new_navigation_mesh
```

### NavigationServer2DManager
*Inherits: **Object***

NavigationServer2DManager is the API for registering NavigationServer2D implementations and setting the default implementation.

**Methods**
- `void register_server(name: String, create_callback: Callable)`
- `void set_default_server(name: String, priority: int)`

### NavigationServer2D
*Inherits: **Object***

NavigationServer2D is the server that handles navigation maps, regions and agents. It does not handle A* navigation from AStar2D or AStarGrid2D.

**Methods**
- `RID agent_create()`
- `bool agent_get_avoidance_enabled(agent: RID) const`
- `int agent_get_avoidance_layers(agent: RID) const`
- `int agent_get_avoidance_mask(agent: RID) const`
- `float agent_get_avoidance_priority(agent: RID) const`
- `RID agent_get_map(agent: RID) const`
- `int agent_get_max_neighbors(agent: RID) const`
- `float agent_get_max_speed(agent: RID) const`
- `float agent_get_neighbor_distance(agent: RID) const`
- `bool agent_get_paused(agent: RID) const`
- `Vector2 agent_get_position(agent: RID) const`
- `float agent_get_radius(agent: RID) const`
- `float agent_get_time_horizon_agents(agent: RID) const`
- `float agent_get_time_horizon_obstacles(agent: RID) const`
- `Vector2 agent_get_velocity(agent: RID) const`
- `bool agent_has_avoidance_callback(agent: RID) const`
- `bool agent_is_map_changed(agent: RID) const`
- `void agent_set_avoidance_callback(agent: RID, callback: Callable)`
- `void agent_set_avoidance_enabled(agent: RID, enabled: bool)`
- `void agent_set_avoidance_layers(agent: RID, layers: int)`
- `void agent_set_avoidance_mask(agent: RID, mask: int)`
- `void agent_set_avoidance_priority(agent: RID, priority: float)`
- `void agent_set_map(agent: RID, map: RID)`
- `void agent_set_max_neighbors(agent: RID, count: int)`
- `void agent_set_max_speed(agent: RID, max_speed: float)`
- `void agent_set_neighbor_distance(agent: RID, distance: float)`
- `void agent_set_paused(agent: RID, paused: bool)`
- `void agent_set_position(agent: RID, position: Vector2)`
- `void agent_set_radius(agent: RID, radius: float)`
- `void agent_set_time_horizon_agents(agent: RID, time_horizon: float)`
- `void agent_set_time_horizon_obstacles(agent: RID, time_horizon: float)`
- `void agent_set_velocity(agent: RID, velocity: Vector2)`
- `void agent_set_velocity_forced(agent: RID, velocity: Vector2)`
- `void bake_from_source_geometry_data(navigation_polygon: NavigationPolygon, source_geometry_data: NavigationMeshSourceGeometryData2D, callback: Callable = Callable())`
- `void bake_from_source_geometry_data_async(navigation_polygon: NavigationPolygon, source_geometry_data: NavigationMeshSourceGeometryData2D, callback: Callable = Callable())`
- `void free_rid(rid: RID)`
- `bool get_debug_enabled() const`
- `Array[RID] get_maps() const`
- `int get_process_info(process_info: ProcessInfo) const`
- `bool is_baking_navigation_polygon(navigation_polygon: NavigationPolygon) const`

### NavigationServer3DManager
*Inherits: **Object***

NavigationServer3DManager is the API for registering NavigationServer3D implementations and setting the default implementation.

**Methods**
- `void register_server(name: String, create_callback: Callable)`
- `void set_default_server(name: String, priority: int)`

### NavigationServer3D
*Inherits: **Object***

NavigationServer3D is the server that handles navigation maps, regions and agents. It does not handle A* navigation from AStar3D.

**Methods**
- `RID agent_create()`
- `bool agent_get_avoidance_enabled(agent: RID) const`
- `int agent_get_avoidance_layers(agent: RID) const`
- `int agent_get_avoidance_mask(agent: RID) const`
- `float agent_get_avoidance_priority(agent: RID) const`
- `float agent_get_height(agent: RID) const`
- `RID agent_get_map(agent: RID) const`
- `int agent_get_max_neighbors(agent: RID) const`
- `float agent_get_max_speed(agent: RID) const`
- `float agent_get_neighbor_distance(agent: RID) const`
- `bool agent_get_paused(agent: RID) const`
- `Vector3 agent_get_position(agent: RID) const`
- `float agent_get_radius(agent: RID) const`
- `float agent_get_time_horizon_agents(agent: RID) const`
- `float agent_get_time_horizon_obstacles(agent: RID) const`
- `bool agent_get_use_3d_avoidance(agent: RID) const`
- `Vector3 agent_get_velocity(agent: RID) const`
- `bool agent_has_avoidance_callback(agent: RID) const`
- `bool agent_is_map_changed(agent: RID) const`
- `void agent_set_avoidance_callback(agent: RID, callback: Callable)`
- `void agent_set_avoidance_enabled(agent: RID, enabled: bool)`
- `void agent_set_avoidance_layers(agent: RID, layers: int)`
- `void agent_set_avoidance_mask(agent: RID, mask: int)`
- `void agent_set_avoidance_priority(agent: RID, priority: float)`
- `void agent_set_height(agent: RID, height: float)`
- `void agent_set_map(agent: RID, map: RID)`
- `void agent_set_max_neighbors(agent: RID, count: int)`
- `void agent_set_max_speed(agent: RID, max_speed: float)`
- `void agent_set_neighbor_distance(agent: RID, distance: float)`
- `void agent_set_paused(agent: RID, paused: bool)`
- `void agent_set_position(agent: RID, position: Vector3)`
- `void agent_set_radius(agent: RID, radius: float)`
- `void agent_set_time_horizon_agents(agent: RID, time_horizon: float)`
- `void agent_set_time_horizon_obstacles(agent: RID, time_horizon: float)`
- `void agent_set_use_3d_avoidance(agent: RID, enabled: bool)`
- `void agent_set_velocity(agent: RID, velocity: Vector3)`
- `void agent_set_velocity_forced(agent: RID, velocity: Vector3)`
- `void bake_from_source_geometry_data(navigation_mesh: NavigationMesh, source_geometry_data: NavigationMeshSourceGeometryData3D, callback: Callable = Callable())`
- `void bake_from_source_geometry_data_async(navigation_mesh: NavigationMesh, source_geometry_data: NavigationMeshSourceGeometryData3D, callback: Callable = Callable())`
- `void free_rid(rid: RID)`

### NinePatchRect
*Inherits: **Control < CanvasItem < Node < Object***

Also known as 9-slice panels, NinePatchRect produces clean panels of any size based on a small texture. To do so, it splits the texture in a 3×3 grid. When you scale the node, it tiles the texture's edges horizontally or vertically, tiles the center on both axes, and leaves the corners unchanged.

**Properties**
- `AxisStretchMode axis_stretch_horizontal` = `0`
- `AxisStretchMode axis_stretch_vertical` = `0`
- `bool draw_center` = `true`
- `MouseFilter mouse_filter` = `2 (overrides Control)`
- `int patch_margin_bottom` = `0`
- `int patch_margin_left` = `0`
- `int patch_margin_right` = `0`
- `int patch_margin_top` = `0`
- `Rect2 region_rect` = `Rect2(0, 0, 0, 0)`
- `Texture2D texture`

**Methods**
- `int get_patch_margin(margin: Side) const`
- `void set_patch_margin(margin: Side, value: int)`

### NodePath

The NodePath built-in Variant type represents a path to a node or property in a hierarchy of nodes. It is designed to be efficiently passed into many built-in methods (such as Node.get_node(), Object.set_indexed(), Tween.tween_property(), etc.) without a hard dependence on the node or property they point to.

**Methods**
- `NodePath get_as_property_path() const`
- `StringName get_concatenated_names() const`
- `StringName get_concatenated_subnames() const`
- `StringName get_name(idx: int) const`
- `int get_name_count() const`
- `StringName get_subname(idx: int) const`
- `int get_subname_count() const`
- `int hash() const`
- `bool is_absolute() const`
- `bool is_empty() const`
- `NodePath slice(begin: int, end: int = 2147483647) const`

**GDScript Examples**
```gdscript
# node_path points to the "x" property of the child node named "position".
var node_path = ^"position:x"

# property_path points to the "position" in the "x" axis of this node.
var property_path = node_path.get_as_property_path()
print(property_path) # Prints ":position:x"
```
```gdscript
var node_path = ^"Sprite2D:texture:resource_name"
print(node_path.get_concatenated_subnames()) # Prints "texture:resource_name"
```

### Node
*Inherits: **Object** | Inherited by: AnimationMixer, AudioStreamPlayer, CanvasItem, CanvasLayer, EditorFileSystem, EditorPlugin, ...*

Nodes are Godot's building blocks. They can be assigned as the child of another node, resulting in a tree arrangement. A given node can contain any number of nodes as children with the requirement that all siblings (direct children of a node) should have unique names.

**Properties**
- `AutoTranslateMode auto_translate_mode` = `0`
- `String editor_description` = `""`
- `MultiplayerAPI multiplayer`
- `StringName name`
- `Node owner`
- `PhysicsInterpolationMode physics_interpolation_mode` = `0`
- `ProcessMode process_mode` = `0`
- `int process_physics_priority` = `0`
- `int process_priority` = `0`
- `ProcessThreadGroup process_thread_group` = `0`
- `int process_thread_group_order`
- `BitField[ProcessThreadMessages] process_thread_messages`
- `String scene_file_path`
- `bool unique_name_in_owner` = `false`

**Methods**
- `void _enter_tree() virtual`
- `void _exit_tree() virtual`
- `PackedStringArray _get_accessibility_configuration_warnings() virtual const`
- `PackedStringArray _get_configuration_warnings() virtual const`
- `RID _get_focused_accessibility_element() virtual const`
- `void _input(event: InputEvent) virtual`
- `void _physics_process(delta: float) virtual`
- `void _process(delta: float) virtual`
- `void _ready() virtual`
- `void _shortcut_input(event: InputEvent) virtual`
- `void _unhandled_input(event: InputEvent) virtual`
- `void _unhandled_key_input(event: InputEvent) virtual`
- `void add_child(node: Node, force_readable_name: bool = false, internal: InternalMode = 0)`
- `void add_sibling(sibling: Node, force_readable_name: bool = false)`
- `void add_to_group(group: StringName, persistent: bool = false)`
- `String atr(message: String, context: StringName = "") const`
- `String atr_n(message: String, plural_message: StringName, n: int, context: StringName = "") const`
- `Variant call_deferred_thread_group(method: StringName, ...) vararg`
- `Variant call_thread_safe(method: StringName, ...) vararg`
- `bool can_auto_translate() const`
- `bool can_process() const`
- `Tween create_tween()`
- `Node duplicate(flags: int = 15) const`
- `Node find_child(pattern: String, recursive: bool = true, owned: bool = true) const`
- `Array[Node] find_children(pattern: String, type: String = "", recursive: bool = true, owned: bool = true) const`
- `Node find_parent(pattern: String) const`
- `RID get_accessibility_element() const`
- `Node get_child(idx: int, include_internal: bool = false) const`
- `int get_child_count(include_internal: bool = false) const`
- `Array[Node] get_children(include_internal: bool = false) const`
- `Array[StringName] get_groups() const`
- `int get_index(include_internal: bool = false) const`
- `Window get_last_exclusive_window() const`
- `int get_multiplayer_authority() const`
- `Node get_node(path: NodePath) const`
- `Array get_node_and_resource(path: NodePath)`
- `Node get_node_or_null(path: NodePath) const`
- `Variant get_node_rpc_config() const`
- `Array[int] get_orphan_node_ids() static`
- `Node get_parent() const`

**GDScript Examples**
```gdscript
var child_node = get_child(0)
if child_node.get_parent():
    child_node.get_parent().remove_child(child_node)
add_child(child_node)
```
```gdscript
get_tree().create_tween().bind_node(self)
```

### NoiseTexture3D
*Inherits: **Texture3D < Texture < Resource < RefCounted < Object***

Uses the FastNoiseLite library or other noise generators to fill the texture data of your desired size.

**Properties**
- `Gradient color_ramp`
- `int depth` = `64`
- `int height` = `64`
- `bool invert` = `false`
- `Noise noise`
- `bool normalize` = `true`
- `bool seamless` = `false`
- `float seamless_blend_skirt` = `0.1`
- `int width` = `64`

**GDScript Examples**
```gdscript
var texture = NoiseTexture3D.new()
texture.noise = FastNoiseLite.new()
await texture.changed
var data = texture.get_data()
```

### Noise
*Inherits: **Resource < RefCounted < Object** | Inherited by: FastNoiseLite*

This class defines the interface for noise generation libraries to inherit from.

**Methods**
- `Image get_image(width: int, height: int, invert: bool = false, in_3d_space: bool = false, normalize: bool = true) const`
- `Array[Image] get_image_3d(width: int, height: int, depth: int, invert: bool = false, normalize: bool = true) const`
- `float get_noise_1d(x: float) const`
- `float get_noise_2d(x: float, y: float) const`
- `float get_noise_2dv(v: Vector2) const`
- `float get_noise_3d(x: float, y: float, z: float) const`
- `float get_noise_3dv(v: Vector3) const`
- `Image get_seamless_image(width: int, height: int, invert: bool = false, in_3d_space: bool = false, skirt: float = 0.1, normalize: bool = true) const`
- `Array[Image] get_seamless_image_3d(width: int, height: int, depth: int, invert: bool = false, skirt: float = 0.1, normalize: bool = true) const`

### OS
*Inherits: **Object***

The OS class wraps the most common functionalities for communicating with the host operating system, such as the video driver, delays, environment variables, execution of binaries, command line, etc.

**Properties**
- `bool delta_smoothing` = `true`
- `bool low_processor_usage_mode` = `false`
- `int low_processor_usage_mode_sleep_usec` = `6900`

**Methods**
- `void add_logger(logger: Logger)`
- `void alert(text: String, title: String = "Alert!")`
- `void close_midi_inputs()`
- `void crash(message: String)`
- `int create_instance(arguments: PackedStringArray)`
- `int create_process(path: String, arguments: PackedStringArray, open_console: bool = false)`
- `void delay_msec(msec: int) const`
- `void delay_usec(usec: int) const`
- `int execute(path: String, arguments: PackedStringArray, output: Array = [], read_stderr: bool = false, open_console: bool = false)`
- `Dictionary execute_with_pipe(path: String, arguments: PackedStringArray, blocking: bool = true)`
- `Key find_keycode_from_string(string: String) const`
- `String get_cache_dir() const`
- `PackedStringArray get_cmdline_args()`
- `PackedStringArray get_cmdline_user_args()`
- `String get_config_dir() const`
- `PackedStringArray get_connected_midi_inputs()`
- `String get_data_dir() const`
- `String get_distribution_name() const`
- `PackedByteArray get_entropy(size: int)`
- `String get_environment(variable: String) const`
- `String get_executable_path() const`
- `PackedStringArray get_granted_permissions() const`
- `String get_keycode_string(code: Key) const`
- `String get_locale() const`
- `String get_locale_language() const`
- `int get_main_thread_id() const`
- `Dictionary get_memory_info() const`
- `String get_model_name() const`
- `String get_name() const`
- `int get_process_exit_code(pid: int) const`
- `int get_process_id() const`
- `int get_processor_count() const`
- `String get_processor_name() const`
- `PackedStringArray get_restart_on_exit_arguments() const`
- `int get_static_memory_peak_usage() const`
- `int get_static_memory_usage() const`
- `StdHandleType get_stderr_type() const`
- `StdHandleType get_stdin_type() const`
- `StdHandleType get_stdout_type() const`
- `String get_system_ca_certificates()`

**GDScript Examples**
```gdscript
var pid = OS.create_process(OS.get_executable_path(), [])
```
```gdscript
var output = []
var exit_code = OS.execute("ls", ["-l", "/tmp"], output)
```

### OccluderPolygon2D
*Inherits: **Resource < RefCounted < Object***

Editor facility that helps you draw a 2D polygon used as resource for LightOccluder2D.

**Properties**
- `bool closed` = `true`
- `CullMode cull_mode` = `0`
- `PackedVector2Array polygon` = `PackedVector2Array()`

### OfflineMultiplayerPeer
*Inherits: **MultiplayerPeer < PacketPeer < RefCounted < Object***

This is the default MultiplayerAPI.multiplayer_peer for the Node.multiplayer. It mimics the behavior of a server with no peers connected.

### OggPacketSequencePlayback
*Inherits: **RefCounted < Object***

There is currently no description for this class. Please help us by contributing one!

### OggPacketSequence
*Inherits: **Resource < RefCounted < Object***

A sequence of Ogg packets.

**Properties**
- `PackedInt64Array granule_positions` = `PackedInt64Array()`
- `Array[Array] packet_data` = `[]`
- `float sampling_rate` = `0.0`

**Methods**
- `float get_length() const`

### OpenXRAPIExtension
*Inherits: **RefCounted < Object***

OpenXRAPIExtension makes OpenXR available for GDExtension. It provides the OpenXR API to GDExtension through the get_instance_proc_addr() method, and the OpenXR instance through get_instance().

**Methods**
- `int action_get_handle(action: RID)`
- `void begin_debug_label_region(label_name: String)`
- `bool can_render()`
- `void end_debug_label_region()`
- `RID find_action(name: String, action_set: RID)`
- `String get_error_string(result: int)`
- `int get_hand_tracker(hand_index: int)`
- `int get_instance()`
- `int get_instance_proc_addr(name: String)`
- `int get_next_frame_time()`
- `int get_openxr_version()`
- `int get_play_space()`
- `int get_predicted_display_time()`
- `int get_projection_layer()`
- `float get_render_state_z_far()`
- `float get_render_state_z_near()`
- `int get_session()`
- `PackedInt64Array get_supported_swapchain_formats()`
- `String get_swapchain_format_name(swapchain_format: int)`
- `int get_system_id()`
- `void insert_debug_label(label_name: String)`
- `OpenXRAlphaBlendModeSupport is_environment_blend_mode_alpha_supported()`
- `bool is_initialized()`
- `bool is_running()`
- `bool openxr_is_enabled(check_run_in_editor: bool) static`
- `void openxr_swapchain_acquire(swapchain: int)`
- `int openxr_swapchain_create(create_flags: int, usage_flags: int, swapchain_format: int, width: int, height: int, sample_count: int, array_size: int)`
- `void openxr_swapchain_free(swapchain: int)`
- `RID openxr_swapchain_get_image(swapchain: int)`
- `int openxr_swapchain_get_swapchain(swapchain: int)`
- `void openxr_swapchain_release(swapchain: int)`
- `void register_composition_layer_provider(extension: OpenXRExtensionWrapper)`
- `void register_frame_info_extension(extension: OpenXRExtensionWrapper)`
- `void register_projection_views_extension(extension: OpenXRExtensionWrapper)`
- `void set_custom_play_space(space: const void*)`
- `void set_emulate_environment_blend_mode_alpha_blend(enabled: bool)`
- `void set_object_name(object_type: int, object_handle: int, object_name: String)`
- `void set_render_region(render_region: Rect2i)`
- `void set_velocity_depth_texture(render_target: RID)`
- `void set_velocity_target_size(target_size: Vector2i)`

### OpenXRActionBindingModifier
*Inherits: **OpenXRBindingModifier < Resource < RefCounted < Object** | Inherited by: OpenXRAnalogThresholdModifier*

Binding modifier that applies on individual actions related to an interaction profile.

### OpenXRActionMap
*Inherits: **Resource < RefCounted < Object***

OpenXR uses an action system similar to Godots Input map system to bind inputs and outputs on various types of XR controllers to named actions. OpenXR specifies more detail on these inputs and outputs than Godot supports.

**Properties**
- `Array action_sets` = `[]`
- `Array interaction_profiles` = `[]`

**Methods**
- `void add_action_set(action_set: OpenXRActionSet)`
- `void add_interaction_profile(interaction_profile: OpenXRInteractionProfile)`
- `void create_default_action_sets()`
- `OpenXRActionSet find_action_set(name: String) const`
- `OpenXRInteractionProfile find_interaction_profile(name: String) const`
- `OpenXRActionSet get_action_set(idx: int) const`
- `int get_action_set_count() const`
- `OpenXRInteractionProfile get_interaction_profile(idx: int) const`
- `int get_interaction_profile_count() const`
- `void remove_action_set(action_set: OpenXRActionSet)`
- `void remove_interaction_profile(interaction_profile: OpenXRInteractionProfile)`

### OpenXRActionSet
*Inherits: **Resource < RefCounted < Object***

Action sets in OpenXR define a collection of actions that can be activated in unison. This allows games to easily change between different states that require different inputs or need to reinterpret inputs. For instance we could have an action set that is active when a menu is open, an action set that is active when the player is freely walking around and an action set that is active when the player is controlling a vehicle.

**Properties**
- `Array actions` = `[]`
- `String localized_name` = `""`
- `int priority` = `0`

**Methods**
- `void add_action(action: OpenXRAction)`
- `int get_action_count() const`
- `void remove_action(action: OpenXRAction)`

### OpenXRAction
*Inherits: **Resource < RefCounted < Object***

This resource defines an OpenXR action. Actions can be used both for inputs (buttons, joysticks, triggers, etc.) and outputs (haptics).

**Properties**
- `ActionType action_type` = `1`
- `String localized_name` = `""`
- `PackedStringArray toplevel_paths` = `PackedStringArray()`

### OpenXRAnalogThresholdModifier
*Inherits: **OpenXRActionBindingModifier < OpenXRBindingModifier < Resource < RefCounted < Object***

The analog threshold binding modifier can modify a float input to a boolean input with specified thresholds.

**Properties**
- `OpenXRHapticBase off_haptic`
- `float off_threshold` = `0.4`
- `OpenXRHapticBase on_haptic`
- `float on_threshold` = `0.6`

### OpenXRAnchorTracker
*Inherits: **OpenXRSpatialEntityTracker < XRPositionalTracker < XRTracker < RefCounted < Object***

Positional tracker for our OpenXR spatial entity anchor extension, it tracks a user defined location in real space and maps it to our virtual space.

**Properties**
- `String uuid` = `""`

**Methods**
- `bool has_uuid() const`

### OpenXRAndroidThreadSettingsExtension
*Inherits: **OpenXRExtensionWrapper < Object***

For XR to be comfortable, it is important for applications to deliver frames quickly and consistently. In order to make sure the important application threads get their full share of time, these threads must be identified to the system, which will adjust their scheduling priority accordingly.

**Methods**
- `bool set_application_thread_type(thread_type: ThreadType, thread_id: int = 0)`

### OpenXRBindingModifierEditor
*Inherits: **PanelContainer < Container < Control < CanvasItem < Node < Object***

This is the default binding modifier editor used in the OpenXR action map.

**Properties**
- `BitField[SizeFlags] size_flags_horizontal` = `3 (overrides Control)`

**Methods**
- `OpenXRBindingModifier get_binding_modifier() const`
- `void setup(action_map: OpenXRActionMap, binding_modifier: OpenXRBindingModifier)`

### OpenXRBindingModifier
*Inherits: **Resource < RefCounted < Object** | Inherited by: OpenXRActionBindingModifier, OpenXRIPBindingModifier*

Binding modifier base class. Subclasses implement various modifiers that alter how an OpenXR runtime processes inputs.

**Methods**
- `String _get_description() virtual required const`
- `PackedByteArray _get_ip_modification() virtual required`

### OpenXRCompositionLayerCylinder
*Inherits: **OpenXRCompositionLayer < Node3D < Node < Object***

An OpenXR composition layer that allows rendering a SubViewport on an internal slice of a cylinder.

**Properties**
- `float aspect_ratio` = `1.0`
- `float central_angle` = `1.5707964`
- `int fallback_segments` = `10`
- `float radius` = `1.0`

### OpenXRCompositionLayerEquirect
*Inherits: **OpenXRCompositionLayer < Node3D < Node < Object***

An OpenXR composition layer that allows rendering a SubViewport on an internal slice of a sphere.

**Properties**
- `float central_horizontal_angle` = `1.5707964`
- `int fallback_segments` = `10`
- `float lower_vertical_angle` = `0.7853982`
- `float radius` = `1.0`
- `float upper_vertical_angle` = `0.7853982`

### OpenXRCompositionLayerQuad
*Inherits: **OpenXRCompositionLayer < Node3D < Node < Object***

An OpenXR composition layer that allows rendering a SubViewport on a quad.

**Properties**
- `Vector2 quad_size` = `Vector2(1, 1)`

### OpenXRCompositionLayer
*Inherits: **Node3D < Node < Object** | Inherited by: OpenXRCompositionLayerCylinder, OpenXRCompositionLayerEquirect, OpenXRCompositionLayerQuad*

Composition layers allow 2D viewports to be displayed inside of the headset by the XR compositor through special projections that retain their quality. This allows for rendering clear text while keeping the layer at a native resolution.

**Properties**
- `bool alpha_blend` = `false`
- `Vector2i android_surface_size` = `Vector2i(1024, 1024)`
- `bool enable_hole_punch` = `false`
- `SubViewport layer_viewport`
- `bool protected_content` = `false`
- `int sort_order` = `1`
- `Swizzle swapchain_state_alpha_swizzle` = `3`
- `Swizzle swapchain_state_blue_swizzle` = `2`
- `Color swapchain_state_border_color` = `Color(0, 0, 0, 0)`
- `Swizzle swapchain_state_green_swizzle` = `1`
- `Wrap swapchain_state_horizontal_wrap` = `0`
- `Filter swapchain_state_mag_filter` = `1`
- `float swapchain_state_max_anisotropy` = `1.0`
- `Filter swapchain_state_min_filter` = `1`
- `MipmapMode swapchain_state_mipmap_mode` = `2`
- `Swizzle swapchain_state_red_swizzle` = `0`
- `Wrap swapchain_state_vertical_wrap` = `0`
- `bool use_android_surface` = `false`

**Methods**
- `JavaObject get_android_surface()`
- `Vector2 intersects_ray(origin: Vector3, direction: Vector3) const`
- `bool is_natively_supported() const`

### OpenXRDpadBindingModifier
*Inherits: **OpenXRIPBindingModifier < OpenXRBindingModifier < Resource < RefCounted < Object***

The DPad binding modifier converts an axis input to a dpad output, emulating a DPad. New input paths for each dpad direction will be added to the interaction profile. When bound to actions the DPad emulation will be activated. You should not combine dpad inputs with normal inputs in the same action set for the same control, this will result in an error being returned when suggested bindings are submitted to OpenXR.

**Properties**
- `OpenXRActionSet action_set`
- `float center_region` = `0.1`
- `String input_path` = `""`
- `bool is_sticky` = `false`
- `OpenXRHapticBase off_haptic`
- `OpenXRHapticBase on_haptic`
- `float threshold` = `0.6`
- `float threshold_released` = `0.4`
- `float wedge_angle` = `1.5707964`

### OpenXRExtensionWrapperExtension
*Inherits: **OpenXRExtensionWrapper < Object***

OpenXRExtensionWrapperExtension allows implementing OpenXR extensions with GDExtension. The extension should be registered with OpenXRExtensionWrapper.register_extension_wrapper().

### OpenXRExtensionWrapper
*Inherits: **Object** | Inherited by: OpenXRAndroidThreadSettingsExtension, OpenXRExtensionWrapperExtension, OpenXRFrameSynthesisExtension, OpenXRFutureExtension, OpenXRRenderModelExtension, OpenXRSpatialAnchorCapability, ...*

OpenXRExtensionWrapper allows implementing OpenXR extensions with GDExtension. The extension should be registered with register_extension_wrapper().

**Methods**
- `int _get_composition_layer(index: int) virtual`
- `int _get_composition_layer_count() virtual`
- `int _get_composition_layer_order(index: int) virtual`
- `Dictionary _get_requested_extensions(xr_version: int) virtual`
- `PackedStringArray _get_suggested_tracker_names() virtual`
- `Array[Dictionary] _get_viewport_composition_layer_extension_properties() virtual`
- `Dictionary _get_viewport_composition_layer_extension_property_defaults() virtual`
- `void _on_before_instance_created() virtual`
- `bool _on_event_polled(event: const void*) virtual`
- `void _on_instance_created(instance: int) virtual`
- `void _on_instance_destroyed() virtual`
- `void _on_main_swapchains_created() virtual`
- `void _on_post_draw_viewport(viewport: RID) virtual`
- `void _on_pre_draw_viewport(viewport: RID) virtual`
- `void _on_pre_render() virtual`
- `void _on_process() virtual`
- `void _on_register_metadata() virtual`
- `void _on_session_created(session: int) virtual`
- `void _on_session_destroyed() virtual`
- `void _on_state_exiting() virtual`
- `void _on_state_focused() virtual`
- `void _on_state_idle() virtual`
- `void _on_state_loss_pending() virtual`
- `void _on_state_ready() virtual`
- `void _on_state_stopping() virtual`
- `void _on_state_synchronized() virtual`
- `void _on_state_visible() virtual`
- `void _on_sync_actions() virtual`
- `void _on_viewport_composition_layer_destroyed(layer: const void*) virtual`
- `void _prepare_view_configuration(view_count: int) virtual`
- `void _print_view_configuration_info(view: int) virtual const`
- `int _set_android_surface_swapchain_create_info_and_get_next_pointer(property_values: Dictionary, next_pointer: void*) virtual`
- `int _set_frame_end_info_and_get_next_pointer(next_pointer: void*) virtual`
- `int _set_frame_wait_info_and_get_next_pointer(next_pointer: void*) virtual`
- `int _set_hand_joint_locations_and_get_next_pointer(hand_index: int, next_pointer: void*) virtual`
- `int _set_instance_create_info_and_get_next_pointer(xr_version: int, next_pointer: void*) virtual`
- `int _set_projection_views_and_get_next_pointer(view_index: int, next_pointer: void*) virtual`
- `int _set_reference_space_create_info_and_get_next_pointer(reference_space_type: int, next_pointer: void*) virtual`
- `int _set_session_create_and_get_next_pointer(next_pointer: void*) virtual`
- `int _set_swapchain_create_info_and_get_next_pointer(next_pointer: void*) virtual`

### OpenXRFrameSynthesisExtension
*Inherits: **OpenXRExtensionWrapper < Object***

This class implements the OpenXR Frame synthesis extension. When enabled in the project settings and supported by the XR runtime in use, frame synthesis uses advanced reprojection techniques to inject additional frames so that your XR experience hits the full frame rate of the device.

**Properties**
- `bool enabled` = `false`
- `bool relax_frame_interval` = `false`

**Methods**
- `bool is_available() const`
- `void skip_next_frame()`

### OpenXRFutureExtension
*Inherits: **OpenXRExtensionWrapper < Object***

This is a support extension in OpenXR that allows other OpenXR extensions to start asynchronous functions and get a callback after this function finishes. It is not intended for consumption within GDScript but can be accessed from GDExtension.

**Methods**
- `void cancel_future(future: int)`
- `bool is_active() const`
- `OpenXRFutureResult register_future(future: int, on_success: Callable = Callable())`

**GDScript Examples**
```gdscript
var future_result = OpenXRFutureExtension.register_future(future)
await future_result.completed
if future_result.get_status() == OpenXRFutureResult.RESULT_FINISHED:
    # Handle your success
    pass
```

### OpenXRFutureResult
*Inherits: **RefCounted < Object***

Result object tracking the asynchronous result of an OpenXR Future object, you can use this object to track the result status.

**Methods**
- `void cancel_future()`
- `int get_future() const`
- `Variant get_result_value() const`
- `ResultStatus get_status() const`
- `void set_result_value(result_value: Variant)`

### OpenXRHand
*Inherits: **Node3D < Node < Object***

This node enables OpenXR's hand tracking functionality. The node should be a child node of an XROrigin3D node, tracking will update its position to the player's tracked hand Palm joint location (the center of the middle finger's metacarpal bone). This node also updates the skeleton of a properly skinned hand or avatar model.

**Properties**
- `BoneUpdate bone_update` = `0`
- `Hands hand` = `0`
- `NodePath hand_skeleton` = `NodePath("")`
- `MotionRange motion_range` = `0`
- `SkeletonRig skeleton_rig` = `0`

### OpenXRHapticBase
*Inherits: **Resource < RefCounted < Object** | Inherited by: OpenXRHapticVibration*

This is a base class for haptic feedback resources.

### OpenXRHapticVibration
*Inherits: **OpenXRHapticBase < Resource < RefCounted < Object***

This haptic feedback resource makes it possible to define a vibration based haptic feedback pulse that can be triggered through actions in the OpenXR action map.

**Properties**
- `float amplitude` = `1.0`
- `int duration` = `-1`
- `float frequency` = `0.0`

### OpenXRIPBindingModifier
*Inherits: **OpenXRBindingModifier < Resource < RefCounted < Object** | Inherited by: OpenXRDpadBindingModifier*

Binding modifier that applies directly on an interaction profile.

### OpenXRIPBinding
*Inherits: **Resource < RefCounted < Object***

This binding resource binds an OpenXRAction to an input or output. As most controllers have left hand and right versions that are handled by the same interaction profile we can specify multiple bindings. For instance an action "Fire" could be bound to both "/user/hand/left/input/trigger" and "/user/hand/right/input/trigger". This would require two binding entries.

**Properties**
- `OpenXRAction action`
- `Array binding_modifiers` = `[]`
- `String binding_path` = `""`
- `PackedStringArray paths`

**Methods**
- `void add_path(path: String)`
- `OpenXRActionBindingModifier get_binding_modifier(index: int) const`
- `int get_binding_modifier_count() const`
- `int get_path_count() const`
- `bool has_path(path: String) const`
- `void remove_path(path: String)`

### OpenXRInteractionProfileEditorBase
*Inherits: **HBoxContainer < BoxContainer < Container < Control < CanvasItem < Node < Object** | Inherited by: OpenXRInteractionProfileEditor*

This is a base class for interaction profile editors used by the OpenXR action map editor. It can be used to create bespoke editors for specific interaction profiles.

**Properties**
- `BitField[SizeFlags] size_flags_horizontal` = `3 (overrides Control)`
- `BitField[SizeFlags] size_flags_vertical` = `3 (overrides Control)`

**Methods**
- `void setup(action_map: OpenXRActionMap, interaction_profile: OpenXRInteractionProfile)`

### OpenXRInteractionProfileEditor
*Inherits: **OpenXRInteractionProfileEditorBase < HBoxContainer < BoxContainer < Container < Control < CanvasItem < Node < Object***

This is the default OpenXR interaction profile editor that provides a generic interface for editing any interaction profile for which no custom editor has been defined.

### OpenXRInteractionProfileMetadata
*Inherits: **Object***

This class allows OpenXR core and extensions to register metadata relating to supported interaction devices such as controllers, trackers, haptic devices, etc. It is primarily used by the action map editor and to sanitize any action map by removing extension-dependent entries when applicable.

**Methods**
- `void register_interaction_profile(display_name: String, openxr_path: String, openxr_extension_names: String)`
- `void register_io_path(interaction_profile: String, display_name: String, toplevel_path: String, openxr_path: String, openxr_extension_names: String, action_type: ActionType)`
- `void register_path_rename(old_name: String, new_name: String)`
- `void register_profile_rename(old_name: String, new_name: String)`
- `void register_top_level_path(display_name: String, openxr_path: String, openxr_extension_names: String)`

### OpenXRInteractionProfile
*Inherits: **Resource < RefCounted < Object***

This object stores suggested bindings for an interaction profile. Interaction profiles define the metadata for a tracked XR device such as an XR controller.

**Properties**
- `Array binding_modifiers` = `[]`
- `Array bindings` = `[]`
- `String interaction_profile_path` = `""`

**Methods**
- `OpenXRIPBinding get_binding(index: int) const`
- `int get_binding_count() const`
- `OpenXRIPBindingModifier get_binding_modifier(index: int) const`
- `int get_binding_modifier_count() const`

### OpenXRInterface
*Inherits: **XRInterface < RefCounted < Object***

The OpenXR interface allows Godot to interact with OpenXR runtimes and make it possible to create XR experiences and games.

**Properties**
- `float display_refresh_rate` = `0.0`
- `bool foveation_dynamic` = `false`
- `int foveation_level` = `0`
- `float render_target_size_multiplier` = `1.0`
- `float vrs_min_radius` = `20.0`
- `float vrs_strength` = `1.0`

**Methods**
- `Array get_action_sets() const`
- `Array get_available_display_refresh_rates() const`
- `Vector3 get_hand_joint_angular_velocity(hand: Hand, joint: HandJoints) const`
- `BitField[HandJointFlags] get_hand_joint_flags(hand: Hand, joint: HandJoints) const`
- `Vector3 get_hand_joint_linear_velocity(hand: Hand, joint: HandJoints) const`
- `Vector3 get_hand_joint_position(hand: Hand, joint: HandJoints) const`
- `float get_hand_joint_radius(hand: Hand, joint: HandJoints) const`
- `Quaternion get_hand_joint_rotation(hand: Hand, joint: HandJoints) const`
- `HandTrackedSource get_hand_tracking_source(hand: Hand) const`
- `HandMotionRange get_motion_range(hand: Hand) const`
- `SessionState get_session_state()`
- `bool is_action_set_active(name: String) const`
- `bool is_eye_gaze_interaction_supported()`
- `bool is_foveation_supported() const`
- `bool is_hand_interaction_supported() const`
- `bool is_hand_tracking_supported()`
- `void set_action_set_active(name: String, active: bool)`
- `void set_cpu_level(level: PerfSettingsLevel)`
- `void set_gpu_level(level: PerfSettingsLevel)`
- `void set_motion_range(hand: Hand, motion_range: HandMotionRange)`

### OpenXRMarkerTracker
*Inherits: **OpenXRSpatialEntityTracker < XRPositionalTracker < XRTracker < RefCounted < Object***

Spatial entity tracker for our OpenXR spatial entity marker tracking extension. These trackers identify entities in our real space detected by a visual marker such as a QRCode or Aruco code, and map their location to our virtual space.

**Properties**
- `Vector2 bounds_size` = `Vector2(0, 0)`
- `int marker_id` = `0`
- `MarkerType marker_type` = `0`

**Methods**
- `Variant get_marker_data() const`
- `void set_marker_data(marker_data: Variant)`

### OpenXRPlaneTracker
*Inherits: **OpenXRSpatialEntityTracker < XRPositionalTracker < XRTracker < RefCounted < Object***

Spatial entity tracker for our OpenXR spatial entity plane tracking extension. These trackers identify entities in our real space such as walls, floors, tables, etc. and map their location to our virtual space.

**Properties**
- `Vector2 bounds_size` = `Vector2(0, 0)`
- `PlaneAlignment plane_alignment` = `0`
- `String plane_label` = `""`

**Methods**
- `void clear_mesh_data()`
- `Mesh get_mesh()`
- `Transform3D get_mesh_offset() const`
- `Shape3D get_shape(thickness: float = 0.01)`
- `void set_mesh_data(origin: Transform3D, vertices: PackedVector2Array, indices: PackedInt32Array = PackedInt32Array())`

### OpenXRRenderModelExtension
*Inherits: **OpenXRExtensionWrapper < Object***

This class implements the OpenXR Render Model Extension, if enabled it will maintain a list of active render models and provides an interface to the render model data.

**Methods**
- `bool is_active() const`
- `RID render_model_create(render_model_id: int)`
- `void render_model_destroy(render_model: RID)`
- `Array[RID] render_model_get_all()`
- `int render_model_get_animatable_node_count(render_model: RID) const`
- `String render_model_get_animatable_node_name(render_model: RID, index: int) const`
- `Transform3D render_model_get_animatable_node_transform(render_model: RID, index: int) const`
- `TrackingConfidence render_model_get_confidence(render_model: RID) const`
- `Transform3D render_model_get_root_transform(render_model: RID) const`
- `PackedStringArray render_model_get_subaction_paths(render_model: RID)`
- `String render_model_get_top_level_path(render_model: RID) const`
- `bool render_model_is_animatable_node_visible(render_model: RID, index: int) const`
- `Node3D render_model_new_scene_instance(render_model: RID) const`

### OpenXRRenderModelManager
*Inherits: **Node3D < Node < Object***

This helper node will automatically manage displaying render models. It will create new OpenXRRenderModel nodes as controllers and other hand held devices are detected, and remove those nodes when they are deactivated.

**Properties**
- `String make_local_to_pose` = `""`
- `RenderModelTracker tracker` = `0`

### OpenXRRenderModel
*Inherits: **Node3D < Node < Object***

This node will display an OpenXR render model by accessing the associated GLTF and processes all animation data (if supported by the XR runtime).

**Properties**
- `RID render_model` = `RID()`

**Methods**
- `String get_top_level_path() const`

### OpenXRSpatialAnchorCapability
*Inherits: **OpenXRExtensionWrapper < Object***

This is an internal class that handles the OpenXR anchor spatial entity extension.

**Methods**
- `OpenXRAnchorTracker create_new_anchor(transform: Transform3D, spatial_context: RID = RID())`
- `OpenXRFutureResult create_persistence_context(scope: PersistenceScope, user_callback: Callable = Callable())`
- `void free_persistence_context(persistence_context: RID)`
- `int get_persistence_context_handle(persistence_context: RID) const`
- `bool is_persistence_scope_supported(scope: PersistenceScope)`
- `bool is_spatial_anchor_supported()`
- `bool is_spatial_persistence_supported()`
- `OpenXRFutureResult persist_anchor(anchor_tracker: OpenXRAnchorTracker, persistence_context: RID = RID(), user_callback: Callable = Callable())`
- `void remove_anchor(anchor_tracker: OpenXRAnchorTracker)`
- `OpenXRFutureResult unpersist_anchor(anchor_tracker: OpenXRAnchorTracker, persistence_context: RID = RID(), user_callback: Callable = Callable())`

### OpenXRSpatialCapabilityConfigurationAnchor
*Inherits: **OpenXRSpatialCapabilityConfigurationBaseHeader < RefCounted < Object***

Configuration header for spatial anchors. Pass this to OpenXRSpatialEntityExtension.create_spatial_context() to create a spatial context with spatial anchor capabilities.

**Methods**
- `PackedInt64Array get_enabled_components() const`

### OpenXRSpatialCapabilityConfigurationAprilTag
*Inherits: **OpenXRSpatialCapabilityConfigurationBaseHeader < RefCounted < Object***

Configuration header for April tag markers. Pass this to OpenXRSpatialEntityExtension.create_spatial_context() to create a spatial context that can detect April tags.

**Properties**
- `AprilTagDict april_dict` = `4`

**Methods**
- `PackedInt64Array get_enabled_components() const`

### OpenXRSpatialCapabilityConfigurationAruco
*Inherits: **OpenXRSpatialCapabilityConfigurationBaseHeader < RefCounted < Object***

Configuration header for Aruco markers. Pass this to OpenXRSpatialEntityExtension.create_spatial_context() to create a spatial context that can detect Aruco markers.

**Properties**
- `ArucoDict aruco_dict` = `16`

**Methods**
- `PackedInt64Array get_enabled_components() const`

### OpenXRSpatialCapabilityConfigurationBaseHeader
*Inherits: **RefCounted < Object** | Inherited by: OpenXRSpatialCapabilityConfigurationAnchor, OpenXRSpatialCapabilityConfigurationAprilTag, OpenXRSpatialCapabilityConfigurationAruco, OpenXRSpatialCapabilityConfigurationMicroQrCode, OpenXRSpatialCapabilityConfigurationPlaneTracking, OpenXRSpatialCapabilityConfigurationQrCode*

Wrapper base class for OpenXR Spatial Capability Configuration headers. This class needs to be implemented for each capability configuration structure usable within OpenXR's spatial entities system.

**Methods**
- `int _get_configuration() virtual`
- `bool _has_valid_configuration() virtual const`
- `bool has_valid_configuration() const`

### OpenXRSpatialCapabilityConfigurationMicroQrCode
*Inherits: **OpenXRSpatialCapabilityConfigurationBaseHeader < RefCounted < Object***

Configuration header for QR code markers. Pass this to OpenXRSpatialEntityExtension.create_spatial_context() to create a spatial context that can detect QR code markers.

**Methods**
- `PackedInt64Array get_enabled_components() const`

### OpenXRSpatialCapabilityConfigurationPlaneTracking
*Inherits: **OpenXRSpatialCapabilityConfigurationBaseHeader < RefCounted < Object***

Configuration header for plane tracking. Pass this to OpenXRSpatialEntityExtension.create_spatial_context() to create a spatial context with plane tracking capabilities.

**Methods**
- `PackedInt64Array get_enabled_components() const`
- `bool supports_labels()`
- `bool supports_mesh_2d()`
- `bool supports_polygons()`

### OpenXRSpatialCapabilityConfigurationQrCode
*Inherits: **OpenXRSpatialCapabilityConfigurationBaseHeader < RefCounted < Object***

Configuration header for micro QR code markers. Pass this to OpenXRSpatialEntityExtension.create_spatial_context() to create a spatial context that can detect micro QR code markers.

**Methods**
- `PackedInt64Array get_enabled_components() const`

### OpenXRSpatialComponentAnchorList
*Inherits: **OpenXRSpatialComponentData < RefCounted < Object***

Object for storing the queries anchor result data when calling OpenXRSpatialEntityExtension.query_snapshot().

**Methods**
- `Transform3D get_entity_pose(index: int) const`

### OpenXRSpatialComponentBounded2DList
*Inherits: **OpenXRSpatialComponentData < RefCounted < Object***

Object for storing the queries 2D bounding rectangle result data when calling OpenXRSpatialEntityExtension.query_snapshot().

**Methods**
- `Transform3D get_center_pose(index: int) const`
- `Vector2 get_size(index: int) const`

### OpenXRSpatialComponentBounded3DList
*Inherits: **OpenXRSpatialComponentData < RefCounted < Object***

Object for storing the queries 3d bounding box result data when calling OpenXRSpatialEntityExtension.query_snapshot().

**Methods**
- `Transform3D get_center_pose(index: int) const`
- `Vector3 get_size(index: int) const`

### OpenXRSpatialComponentData
*Inherits: **RefCounted < Object** | Inherited by: OpenXRSpatialComponentAnchorList, OpenXRSpatialComponentBounded2DList, OpenXRSpatialComponentBounded3DList, OpenXRSpatialComponentMarkerList, OpenXRSpatialComponentMesh2DList, OpenXRSpatialComponentMesh3DList, ...*

Object for storing OpenXR spatial entity component data.

**Methods**
- `int _get_component_type() virtual const`
- `int _get_structure_data(next: int) virtual const`
- `void _set_capacity(capacity: int) virtual`
- `void set_capacity(capacity: int)`

### OpenXRSpatialComponentMarkerList
*Inherits: **OpenXRSpatialComponentData < RefCounted < Object***

Object for storing the queries marker result data when calling OpenXRSpatialEntityExtension.query_snapshot().

**Methods**
- `Variant get_marker_data(snapshot: RID, index: int) const`
- `int get_marker_id(index: int) const`
- `MarkerType get_marker_type(index: int) const`

### OpenXRSpatialComponentMesh2DList
*Inherits: **OpenXRSpatialComponentData < RefCounted < Object***

Object for storing the queries 2D mesh result data when calling OpenXRSpatialEntityExtension.query_snapshot().

**Methods**
- `PackedInt32Array get_indices(snapshot: RID, index: int) const`
- `Transform3D get_transform(index: int) const`
- `PackedVector2Array get_vertices(snapshot: RID, index: int) const`

### OpenXRSpatialComponentMesh3DList
*Inherits: **OpenXRSpatialComponentData < RefCounted < Object***

Object for storing the queries 3d mesh result data when calling OpenXRSpatialEntityExtension.query_snapshot().

**Methods**
- `Mesh get_mesh(index: int) const`
- `Transform3D get_transform(index: int) const`

### OpenXRSpatialComponentParentList
*Inherits: **OpenXRSpatialComponentData < RefCounted < Object***

Object for storing the queries parent result data when calling OpenXRSpatialEntityExtension.query_snapshot().

**Methods**
- `RID get_parent(index: int) const`

### OpenXRSpatialComponentPersistenceList
*Inherits: **OpenXRSpatialComponentData < RefCounted < Object***

Object for storing the query persistence result data when calling OpenXRSpatialEntityExtension.query_snapshot().

**Methods**
- `int get_persistent_state(index: int) const`
- `String get_persistent_uuid(index: int) const`

### OpenXRSpatialComponentPlaneAlignmentList
*Inherits: **OpenXRSpatialComponentData < RefCounted < Object***

Object for storing the queries plane alignment result data when calling OpenXRSpatialEntityExtension.query_snapshot().

**Methods**
- `PlaneAlignment get_plane_alignment(index: int) const`

### OpenXRSpatialComponentPlaneSemanticLabelList
*Inherits: **OpenXRSpatialComponentData < RefCounted < Object***

Object for storing the queries plane semantic label result data when calling OpenXRSpatialEntityExtension.query_snapshot().

**Methods**
- `PlaneSemanticLabel get_plane_semantic_label(index: int) const`

### OpenXRSpatialComponentPolygon2DList
*Inherits: **OpenXRSpatialComponentData < RefCounted < Object***

Object for storing the queries 2D polygon result data when calling OpenXRSpatialEntityExtension.query_snapshot().

**Methods**
- `Transform3D get_transform(index: int) const`
- `PackedVector2Array get_vertices(snapshot: RID, index: int) const`

### OpenXRSpatialContextPersistenceConfig
*Inherits: **OpenXRStructureBase < RefCounted < Object***

Configuration header for spatial persistence. Pass this to OpenXRSpatialEntityExtension.create_spatial_context() as the next parameter to create a spatial context with spatial persistence capabilities.

**Methods**
- `void add_persistence_context(persistence_context: RID)`
- `void remove_persistence_context(persistence_context: RID)`

### OpenXRSpatialEntityExtension
*Inherits: **OpenXRExtensionWrapper < Object***

OpenXR extension that handles spatial entities and, when enabled, allows querying those spatial entities. This extension will also automatically manage XRTracker objects for static entities.

**Methods**
- `RID add_spatial_entity(spatial_context: RID, entity_id: int, entity: int)`
- `OpenXRFutureResult create_spatial_context(capability_configurations: Array[OpenXRSpatialCapabilityConfigurationBaseHeader], next: OpenXRStructureBase = null, user_callback: Callable = Callable())`
- `OpenXRFutureResult discover_spatial_entities(spatial_context: RID, component_types: PackedInt64Array, next: OpenXRStructureBase = null, user_callback: Callable = Callable())`
- `RID find_spatial_entity(entity_id: int)`
- `void free_spatial_context(spatial_context: RID)`
- `void free_spatial_entity(entity: RID)`
- `void free_spatial_snapshot(spatial_snapshot: RID)`
- `PackedFloat32Array get_float_buffer(spatial_snapshot: RID, buffer_id: int) const`
- `int get_spatial_context_handle(spatial_context: RID) const`
- `bool get_spatial_context_ready(spatial_context: RID) const`
- `RID get_spatial_entity_context(entity: RID) const`
- `int get_spatial_entity_id(entity: RID) const`
- `RID get_spatial_snapshot_context(spatial_snapshot: RID) const`
- `int get_spatial_snapshot_handle(spatial_snapshot: RID) const`
- `String get_string(spatial_snapshot: RID, buffer_id: int) const`
- `PackedByteArray get_uint8_buffer(spatial_snapshot: RID, buffer_id: int) const`
- `PackedInt32Array get_uint16_buffer(spatial_snapshot: RID, buffer_id: int) const`
- `PackedInt32Array get_uint32_buffer(spatial_snapshot: RID, buffer_id: int) const`
- `PackedVector2Array get_vector2_buffer(spatial_snapshot: RID, buffer_id: int) const`
- `PackedVector3Array get_vector3_buffer(spatial_snapshot: RID, buffer_id: int) const`
- `RID make_spatial_entity(spatial_context: RID, entity_id: int)`
- `bool query_snapshot(spatial_snapshot: RID, component_data: Array[OpenXRSpatialComponentData], next: OpenXRStructureBase = null)`
- `bool supports_capability(capability: Capability)`
- `bool supports_component_type(capability: Capability, component_type: ComponentType)`
- `RID update_spatial_entities(spatial_context: RID, entities: Array[RID], component_types: PackedInt64Array, next: OpenXRStructureBase = null)`

### OpenXRSpatialEntityTracker
*Inherits: **XRPositionalTracker < XRTracker < RefCounted < Object** | Inherited by: OpenXRAnchorTracker, OpenXRMarkerTracker, OpenXRPlaneTracker*

These are trackers created and managed by OpenXR's spatial entity extensions that give access to specific data related to OpenXR's spatial entities. They will always be of type TRACKER_ANCHOR.

**Properties**
- `RID entity` = `RID()`
- `EntityTrackingState spatial_tracking_state` = `2`
- `TrackerType type` = `8 (overrides XRTracker)`

### OpenXRSpatialMarkerTrackingCapability
*Inherits: **OpenXRExtensionWrapper < Object***

This class handles the OpenXR marker tracking spatial entity extension.

**Methods**
- `bool is_april_tag_supported()`
- `bool is_aruco_supported()`
- `bool is_micro_qrcode_supported()`
- `bool is_qrcode_supported()`

### OpenXRSpatialPlaneTrackingCapability
*Inherits: **OpenXRExtensionWrapper < Object***

This class handles the OpenXR plane tracking spatial entity extension.

**Methods**
- `bool is_supported()`

### OpenXRSpatialQueryResultData
*Inherits: **OpenXRSpatialComponentData < RefCounted < Object***

Object for storing the main query result data when calling OpenXRSpatialEntityExtension.query_snapshot(). This must always be the first component requested.

**Methods**
- `int get_capacity() const`
- `int get_entity_id(index: int) const`
- `EntityTrackingState get_entity_state(index: int) const`

### OpenXRStructureBase
*Inherits: **RefCounted < Object** | Inherited by: OpenXRSpatialContextPersistenceConfig*

Object for storing OpenXR structure data that is passed when calling into OpenXR APIs.

**Properties**
- `OpenXRStructureBase next`

**Methods**
- `int _get_header(next: int) virtual`
- `int get_structure_type()`

### OpenXRVisibilityMask
*Inherits: **VisualInstance3D < Node3D < Node < Object***

The visibility mask allows us to black out the part of the render result that is invisible due to lens distortion.

### OptimizedTranslation
*Inherits: **Translation < Resource < RefCounted < Object***

An optimized translation. Uses real-time compressed translations, which results in very small dictionaries.

**Methods**
- `void generate(from: Translation)`

### PackedByteArray

An array specifically designed to hold bytes. Packs data tightly, so it saves memory for large array sizes.

**Methods**
- `bool append(value: int)`
- `void append_array(array: PackedByteArray)`
- `int bsearch(value: int, before: bool = true) const`
- `void bswap16(offset: int = 0, count: int = -1)`
- `void bswap32(offset: int = 0, count: int = -1)`
- `void bswap64(offset: int = 0, count: int = -1)`
- `void clear()`
- `PackedByteArray compress(compression_mode: int = 0) const`
- `int count(value: int) const`
- `float decode_double(byte_offset: int) const`
- `float decode_float(byte_offset: int) const`
- `float decode_half(byte_offset: int) const`
- `int decode_s8(byte_offset: int) const`
- `int decode_s16(byte_offset: int) const`
- `int decode_s32(byte_offset: int) const`
- `int decode_s64(byte_offset: int) const`
- `int decode_u8(byte_offset: int) const`
- `int decode_u16(byte_offset: int) const`
- `int decode_u32(byte_offset: int) const`
- `int decode_u64(byte_offset: int) const`
- `Variant decode_var(byte_offset: int, allow_objects: bool = false) const`
- `int decode_var_size(byte_offset: int, allow_objects: bool = false) const`
- `PackedByteArray decompress(buffer_size: int, compression_mode: int = 0) const`
- `PackedByteArray decompress_dynamic(max_output_size: int, compression_mode: int = 0) const`
- `PackedByteArray duplicate() const`
- `void encode_double(byte_offset: int, value: float)`
- `void encode_float(byte_offset: int, value: float)`
- `void encode_half(byte_offset: int, value: float)`
- `void encode_s8(byte_offset: int, value: int)`
- `void encode_s16(byte_offset: int, value: int)`
- `void encode_s32(byte_offset: int, value: int)`
- `void encode_s64(byte_offset: int, value: int)`
- `void encode_u8(byte_offset: int, value: int)`
- `void encode_u16(byte_offset: int, value: int)`
- `void encode_u32(byte_offset: int, value: int)`
- `void encode_u64(byte_offset: int, value: int)`
- `int encode_var(byte_offset: int, value: Variant, allow_objects: bool = false)`
- `bool erase(value: int)`
- `void fill(value: int)`
- `int find(value: int, from: int = 0) const`

**GDScript Examples**
```gdscript
var array = PackedByteArray([11, 46, 255])
print(array.hex_encode()) # Prints "0b2eff"
```

### PackedColorArray

An array specifically designed to hold Color. Packs data tightly, so it saves memory for large array sizes.

**Methods**
- `bool append(value: Color)`
- `void append_array(array: PackedColorArray)`
- `int bsearch(value: Color, before: bool = true) const`
- `void clear()`
- `int count(value: Color) const`
- `PackedColorArray duplicate() const`
- `bool erase(value: Color)`
- `void fill(value: Color)`
- `int find(value: Color, from: int = 0) const`
- `Color get(index: int) const`
- `bool has(value: Color) const`
- `int insert(at_index: int, value: Color)`
- `bool is_empty() const`
- `bool push_back(value: Color)`
- `void remove_at(index: int)`
- `int resize(new_size: int)`
- `void reverse()`
- `int rfind(value: Color, from: int = -1) const`
- `void set(index: int, value: Color)`
- `int size() const`
- `PackedColorArray slice(begin: int, end: int = 2147483647) const`
- `void sort()`
- `PackedByteArray to_byte_array() const`

**GDScript Examples**
```gdscript
var array = PackedColorArray([Color(0.1, 0.2, 0.3), Color(0.4, 0.5, 0.6)])
```

### PackedDataContainerRef
*Inherits: **RefCounted < Object***

When packing nested containers using PackedDataContainer, they are recursively packed into PackedDataContainerRef (only applies to Array and Dictionary). Their data can be retrieved the same way as from PackedDataContainer.

**Methods**
- `int size() const`

**GDScript Examples**
```gdscript
var packed = PackedDataContainer.new()
packed.pack([1, 2, 3, ["nested1", "nested2"], 4, 5, 6])

for element in packed:
    if element is PackedDataContainerRef:
        for subelement in element:
            print("::", subelement)
    else:
        print(element)
```

### PackedDataContainer
*Inherits: **Resource < RefCounted < Object***

PackedDataContainer can be used to efficiently store data from untyped containers. The data is packed into raw bytes and can be saved to file. Only Array and Dictionary can be stored this way.

**Methods**
- `Error pack(value: Variant)`
- `int size() const`

**GDScript Examples**
```gdscript
var data = { "key": "value", "another_key": 123, "lock": Vector2() }
var packed = PackedDataContainer.new()
packed.pack(data)
ResourceSaver.save(packed, "packed_data.res")
```
```gdscript
var container = load("packed_data.res")
for key in container:
    prints(key, container[key])
```

### PackedFloat32Array

An array specifically designed to hold 32-bit floating-point values (float). Packs data tightly, so it saves memory for large array sizes.

**Methods**
- `bool append(value: float)`
- `void append_array(array: PackedFloat32Array)`
- `int bsearch(value: float, before: bool = true) const`
- `void clear()`
- `int count(value: float) const`
- `PackedFloat32Array duplicate() const`
- `bool erase(value: float)`
- `void fill(value: float)`
- `int find(value: float, from: int = 0) const`
- `float get(index: int) const`
- `bool has(value: float) const`
- `int insert(at_index: int, value: float)`
- `bool is_empty() const`
- `bool push_back(value: float)`
- `void remove_at(index: int)`
- `int resize(new_size: int)`
- `void reverse()`
- `int rfind(value: float, from: int = -1) const`
- `void set(index: int, value: float)`
- `int size() const`
- `PackedFloat32Array slice(begin: int, end: int = 2147483647) const`
- `void sort()`
- `PackedByteArray to_byte_array() const`

### PackedFloat64Array

An array specifically designed to hold 64-bit floating-point values (double). Packs data tightly, so it saves memory for large array sizes.

**Methods**
- `bool append(value: float)`
- `void append_array(array: PackedFloat64Array)`
- `int bsearch(value: float, before: bool = true) const`
- `void clear()`
- `int count(value: float) const`
- `PackedFloat64Array duplicate() const`
- `bool erase(value: float)`
- `void fill(value: float)`
- `int find(value: float, from: int = 0) const`
- `float get(index: int) const`
- `bool has(value: float) const`
- `int insert(at_index: int, value: float)`
- `bool is_empty() const`
- `bool push_back(value: float)`
- `void remove_at(index: int)`
- `int resize(new_size: int)`
- `void reverse()`
- `int rfind(value: float, from: int = -1) const`
- `void set(index: int, value: float)`
- `int size() const`
- `PackedFloat64Array slice(begin: int, end: int = 2147483647) const`
- `void sort()`
- `PackedByteArray to_byte_array() const`
