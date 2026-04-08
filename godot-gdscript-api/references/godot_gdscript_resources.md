# Godot 4 GDScript API Reference — Resources

> GDScript-only reference. 85 classes.

### AnimatedTexture
*Inherits: **Texture2D < Texture < Resource < RefCounted < Object***

AnimatedTexture is a resource format for frame-based animations, where multiple textures can be chained automatically with a predefined delay for each frame. Unlike AnimationPlayer or AnimatedSprite2D, it isn't a Node, but has the advantage of being usable anywhere a Texture2D resource can be used, e.g. in a TileSet.

**Properties**
- `int current_frame`
- `int frames` = `1`
- `bool one_shot` = `false`
- `bool pause` = `false`
- `bool resource_local_to_scene` = `false (overrides Resource)`
- `float speed_scale` = `1.0`

**Methods**
- `float get_frame_duration(frame: int) const`
- `Texture2D get_frame_texture(frame: int) const`
- `void set_frame_duration(frame: int, duration: float)`
- `void set_frame_texture(frame: int, texture: Texture2D)`

### AnimationLibrary
*Inherits: **Resource < RefCounted < Object***

An animation library stores a set of animations accessible through StringName keys, for use with AnimationPlayer nodes.

**Methods**
- `Error add_animation(name: StringName, animation: Animation)`
- `Animation get_animation(name: StringName) const`
- `Array[StringName] get_animation_list() const`
- `int get_animation_list_size() const`
- `bool has_animation(name: StringName) const`
- `void remove_animation(name: StringName)`
- `void rename_animation(name: StringName, newname: StringName)`

### AnimationMixer
*Inherits: **Node < Object** | Inherited by: AnimationPlayer, AnimationTree*

Base class for AnimationPlayer and AnimationTree to manage animation lists. It also has general properties and methods for playback and blending.

**Properties**
- `bool active` = `true`
- `int audio_max_polyphony` = `32`
- `AnimationCallbackModeDiscrete callback_mode_discrete` = `1`
- `AnimationCallbackModeMethod callback_mode_method` = `0`
- `AnimationCallbackModeProcess callback_mode_process` = `1`
- `bool deterministic` = `false`
- `bool reset_on_save` = `true`
- `bool root_motion_local` = `false`
- `NodePath root_motion_track` = `NodePath("")`
- `NodePath root_node` = `NodePath("..")`

**Methods**
- `Variant _post_process_key_value(animation: Animation, track: int, value: Variant, object_id: int, object_sub_idx: int) virtual const`
- `Error add_animation_library(name: StringName, library: AnimationLibrary)`
- `void advance(delta: float)`
- `void capture(name: StringName, duration: float, trans_type: TransitionType = 0, ease_type: EaseType = 0)`
- `void clear_caches()`
- `StringName find_animation(animation: Animation) const`
- `StringName find_animation_library(animation: Animation) const`
- `Animation get_animation(name: StringName) const`
- `AnimationLibrary get_animation_library(name: StringName) const`
- `Array[StringName] get_animation_library_list() const`
- `PackedStringArray get_animation_list() const`
- `Vector3 get_root_motion_position() const`
- `Vector3 get_root_motion_position_accumulator() const`
- `Quaternion get_root_motion_rotation() const`
- `Quaternion get_root_motion_rotation_accumulator() const`
- `Vector3 get_root_motion_scale() const`
- `Vector3 get_root_motion_scale_accumulator() const`
- `bool has_animation(name: StringName) const`
- `bool has_animation_library(name: StringName) const`
- `void remove_animation_library(name: StringName)`
- `void rename_animation_library(name: StringName, newname: StringName)`

**GDScript Examples**
```gdscript
var global_library = mixer.get_animation_library("")
global_library.add_animation("animation_name", animation_resource)
```
```gdscript
var current_rotation

func _process(delta):
    if Input.is_action_just_pressed("animate"):
        current_rotation = get_quaternion()
        state_machine.travel("Animate")
    var velocity = current_rotation * animation_tree.get_root_motion_position() / delta
    set_velocity(velocity)
    move_and_slide()
```

### AnimationNodeAdd2
*Inherits: **AnimationNodeSync < AnimationNode < Resource < RefCounted < Object***

A resource to add to an AnimationNodeBlendTree. Blends two animations additively based on the amount value.

### AnimationNodeAdd3
*Inherits: **AnimationNodeSync < AnimationNode < Resource < RefCounted < Object***

A resource to add to an AnimationNodeBlendTree. Blends two animations out of three additively out of three based on the amount value.

### AnimationNodeAnimation
*Inherits: **AnimationRootNode < AnimationNode < Resource < RefCounted < Object***

A resource to add to an AnimationNodeBlendTree. Only has one output port using the animation property. Used as an input for AnimationNodes that blend animations together.

**Properties**
- `bool advance_on_start` = `false`
- `StringName animation` = `&""`
- `LoopMode loop_mode`
- `PlayMode play_mode` = `0`
- `float start_offset`
- `bool stretch_time_scale`
- `float timeline_length`
- `bool use_custom_timeline` = `false`

### AnimationNodeBlend2
*Inherits: **AnimationNodeSync < AnimationNode < Resource < RefCounted < Object***

A resource to add to an AnimationNodeBlendTree. Blends two animations linearly based on the amount value.

### AnimationNodeBlend3
*Inherits: **AnimationNodeSync < AnimationNode < Resource < RefCounted < Object***

A resource to add to an AnimationNodeBlendTree. Blends two animations out of three linearly out of three based on the amount value.

### AnimationNodeBlendSpace1D
*Inherits: **AnimationRootNode < AnimationNode < Resource < RefCounted < Object***

A resource used by AnimationNodeBlendTree.

**Properties**
- `BlendMode blend_mode` = `0`
- `float max_space` = `1.0`
- `float min_space` = `-1.0`
- `float snap` = `0.1`
- `bool sync` = `false`
- `String value_label` = `"value"`

**Methods**
- `void add_blend_point(node: AnimationRootNode, pos: float, at_index: int = -1)`
- `int get_blend_point_count() const`
- `AnimationRootNode get_blend_point_node(point: int) const`
- `float get_blend_point_position(point: int) const`
- `void remove_blend_point(point: int)`
- `void set_blend_point_node(point: int, node: AnimationRootNode)`
- `void set_blend_point_position(point: int, pos: float)`

### AnimationNodeBlendSpace2D
*Inherits: **AnimationRootNode < AnimationNode < Resource < RefCounted < Object***

A resource used by AnimationNodeBlendTree.

**Properties**
- `bool auto_triangles` = `true`
- `BlendMode blend_mode` = `0`
- `Vector2 max_space` = `Vector2(1, 1)`
- `Vector2 min_space` = `Vector2(-1, -1)`
- `Vector2 snap` = `Vector2(0.1, 0.1)`
- `bool sync` = `false`
- `String x_label` = `"x"`
- `String y_label` = `"y"`

**Methods**
- `void add_blend_point(node: AnimationRootNode, pos: Vector2, at_index: int = -1)`
- `void add_triangle(x: int, y: int, z: int, at_index: int = -1)`
- `int get_blend_point_count() const`
- `AnimationRootNode get_blend_point_node(point: int) const`
- `Vector2 get_blend_point_position(point: int) const`
- `int get_triangle_count() const`
- `int get_triangle_point(triangle: int, point: int)`
- `void remove_blend_point(point: int)`
- `void remove_triangle(triangle: int)`
- `void set_blend_point_node(point: int, node: AnimationRootNode)`
- `void set_blend_point_position(point: int, pos: Vector2)`

### AnimationNodeBlendTree
*Inherits: **AnimationRootNode < AnimationNode < Resource < RefCounted < Object***

This animation node may contain a sub-tree of any other type animation nodes, such as AnimationNodeTransition, AnimationNodeBlend2, AnimationNodeBlend3, AnimationNodeOneShot, etc. This is one of the most commonly used animation node roots.

**Properties**
- `Vector2 graph_offset` = `Vector2(0, 0)`

**Methods**
- `void add_node(name: StringName, node: AnimationNode, position: Vector2 = Vector2(0, 0))`
- `void connect_node(input_node: StringName, input_index: int, output_node: StringName)`
- `void disconnect_node(input_node: StringName, input_index: int)`
- `AnimationNode get_node(name: StringName) const`
- `Array[StringName] get_node_list() const`
- `Vector2 get_node_position(name: StringName) const`
- `bool has_node(name: StringName) const`
- `void remove_node(name: StringName)`
- `void rename_node(name: StringName, new_name: StringName)`
- `void set_node_position(name: StringName, position: Vector2)`

### AnimationNodeExtension
*Inherits: **AnimationNode < Resource < RefCounted < Object***

AnimationNodeExtension exposes the APIs of AnimationRootNode to allow users to extend it from GDScript, C#, or C++. This class is not meant to be used directly, but to be extended by other classes. It is used to create custom nodes for the AnimationTree system.

**Methods**
- `PackedFloat32Array _process_animation_node(playback_info: PackedFloat64Array, test_only: bool) virtual required`
- `float get_remaining_time(node_info: PackedFloat32Array, break_loop: bool) static`
- `bool is_looping(node_info: PackedFloat32Array) static`

### AnimationNodeOneShot
*Inherits: **AnimationNodeSync < AnimationNode < Resource < RefCounted < Object***

A resource to add to an AnimationNodeBlendTree. This animation node will execute a sub-animation and return once it finishes. Blend times for fading in and out can be customized, as well as filters.

**Properties**
- `bool abort_on_reset` = `false`
- `bool autorestart` = `false`
- `float autorestart_delay` = `1.0`
- `float autorestart_random_delay` = `0.0`
- `bool break_loop_at_end` = `false`
- `Curve fadein_curve`
- `float fadein_time` = `0.0`
- `Curve fadeout_curve`
- `float fadeout_time` = `0.0`
- `MixMode mix_mode` = `0`

**GDScript Examples**
```gdscript
# Play child animation connected to "shot" port.
animation_tree.set("parameters/OneShot/request", AnimationNodeOneShot.ONE_SHOT_REQUEST_FIRE)
# Alternative syntax (same result as above).
animation_tree["parameters/OneShot/request"] = AnimationNodeOneShot.ONE_SHOT_REQUEST_FIRE

# Abort child animation connected to "shot" port.
animation_tree.set("parameters/OneShot/request", AnimationNodeOneShot.ONE_SHOT_REQUEST_ABORT)
# Alternative syntax (same result as above).
animation_tree["parameters/OneShot/request"] = AnimationNodeOneShot.ONE_SHOT_REQUEST_ABORT

# Abort child animation with fading out c
# ...
```

### AnimationNodeOutput
*Inherits: **AnimationNode < Resource < RefCounted < Object***

A node created automatically in an AnimationNodeBlendTree that outputs the final animation.

### AnimationNodeStateMachinePlayback
*Inherits: **Resource < RefCounted < Object***

Allows control of AnimationTree state machines created with AnimationNodeStateMachine. Retrieve with $AnimationTree.get("parameters/playback").

**Properties**
- `bool resource_local_to_scene` = `true (overrides Resource)`

**Methods**
- `float get_current_length() const`
- `StringName get_current_node() const`
- `float get_current_play_position() const`
- `float get_fading_from_length() const`
- `StringName get_fading_from_node() const`
- `float get_fading_from_play_position() const`
- `float get_fading_length() const`
- `float get_fading_position() const`
- `Array[StringName] get_travel_path() const`
- `bool is_playing() const`
- `void next()`
- `void start(node: StringName, reset: bool = true)`
- `void stop()`
- `void travel(to_node: StringName, reset_on_teleport: bool = true)`

**GDScript Examples**
```gdscript
var state_machine = $AnimationTree.get("parameters/playback")
state_machine.travel("some_state")
```

### AnimationNodeStateMachineTransition
*Inherits: **Resource < RefCounted < Object***

The path generated when using AnimationNodeStateMachinePlayback.travel() is limited to the nodes connected by AnimationNodeStateMachineTransition.

**Properties**
- `StringName advance_condition` = `&""`
- `String advance_expression` = `""`
- `AdvanceMode advance_mode` = `1`
- `bool break_loop_at_end` = `false`
- `int priority` = `1`
- `bool reset` = `true`
- `SwitchMode switch_mode` = `0`
- `Curve xfade_curve`
- `float xfade_time` = `0.0`

**GDScript Examples**
```gdscript
$animation_tree.set("parameters/conditions/idle", is_on_floor and (linear_velocity.x == 0))
```

### AnimationNodeStateMachine
*Inherits: **AnimationRootNode < AnimationNode < Resource < RefCounted < Object***

Contains multiple AnimationRootNodes representing animation states, connected in a graph. State transitions can be configured to happen automatically or via code, using a shortest-path algorithm. Retrieve the AnimationNodeStateMachinePlayback object from the AnimationTree node to control it programmatically.

**Properties**
- `bool allow_transition_to_self` = `false`
- `bool reset_ends` = `false`
- `StateMachineType state_machine_type` = `0`

**Methods**
- `void add_node(name: StringName, node: AnimationNode, position: Vector2 = Vector2(0, 0))`
- `void add_transition(from: StringName, to: StringName, transition: AnimationNodeStateMachineTransition)`
- `Vector2 get_graph_offset() const`
- `AnimationNode get_node(name: StringName) const`
- `Array[StringName] get_node_list() const`
- `StringName get_node_name(node: AnimationNode) const`
- `Vector2 get_node_position(name: StringName) const`
- `AnimationNodeStateMachineTransition get_transition(idx: int) const`
- `int get_transition_count() const`
- `StringName get_transition_from(idx: int) const`
- `StringName get_transition_to(idx: int) const`
- `bool has_node(name: StringName) const`
- `bool has_transition(from: StringName, to: StringName) const`
- `void remove_node(name: StringName)`
- `void remove_transition(from: StringName, to: StringName)`
- `void remove_transition_by_index(idx: int)`
- `void rename_node(name: StringName, new_name: StringName)`
- `void replace_node(name: StringName, node: AnimationNode)`
- `void set_graph_offset(offset: Vector2)`
- `void set_node_position(name: StringName, position: Vector2)`

**GDScript Examples**
```gdscript
var state_machine = $AnimationTree.get("parameters/playback")
state_machine.travel("some_state")
```

### AnimationNodeSub2
*Inherits: **AnimationNodeSync < AnimationNode < Resource < RefCounted < Object***

A resource to add to an AnimationNodeBlendTree. Blends two animations subtractively based on the amount value.

### AnimationNodeSync
*Inherits: **AnimationNode < Resource < RefCounted < Object** | Inherited by: AnimationNodeAdd2, AnimationNodeAdd3, AnimationNodeBlend2, AnimationNodeBlend3, AnimationNodeOneShot, AnimationNodeSub2, ...*

An animation node used to combine, mix, or blend two or more animations together while keeping them synchronized within an AnimationTree.

**Properties**
- `bool sync` = `false`

### AnimationNodeTimeScale
*Inherits: **AnimationNode < Resource < RefCounted < Object***

Allows to scale the speed of the animation (or reverse it) in any child AnimationNodes. Setting it to 0.0 will pause the animation.

### AnimationNodeTimeSeek
*Inherits: **AnimationNode < Resource < RefCounted < Object***

This animation node can be used to cause a seek command to happen to any sub-children of the animation graph. Use to play an Animation from the start or a certain playback position inside the AnimationNodeBlendTree.

**Properties**
- `bool explicit_elapse` = `true`

**GDScript Examples**
```gdscript
# Play child animation from the start.
animation_tree.set("parameters/TimeSeek/seek_request", 0.0)
# Alternative syntax (same result as above).
animation_tree["parameters/TimeSeek/seek_request"] = 0.0

# Play child animation from 12 second timestamp.
animation_tree.set("parameters/TimeSeek/seek_request", 12.0)
# Alternative syntax (same result as above).
animation_tree["parameters/TimeSeek/seek_request"] = 12.0
```

### AnimationNodeTransition
*Inherits: **AnimationNodeSync < AnimationNode < Resource < RefCounted < Object***

Simple state machine for cases which don't require a more advanced AnimationNodeStateMachine. Animations can be connected to the inputs and transition times can be specified.

**Properties**
- `bool allow_transition_to_self` = `false`
- `int input_count` = `0`
- `Curve xfade_curve`
- `float xfade_time` = `0.0`

**Methods**
- `bool is_input_loop_broken_at_end(input: int) const`
- `bool is_input_reset(input: int) const`
- `bool is_input_set_as_auto_advance(input: int) const`
- `void set_input_as_auto_advance(input: int, enable: bool)`
- `void set_input_break_loop_at_end(input: int, enable: bool)`
- `void set_input_reset(input: int, enable: bool)`

**GDScript Examples**
```gdscript
# Play child animation connected to "state_2" port.
animation_tree.set("parameters/Transition/transition_request", "state_2")
# Alternative syntax (same result as above).
animation_tree["parameters/Transition/transition_request"] = "state_2"

# Get current state name (read-only).
animation_tree.get("parameters/Transition/current_state")
# Alternative syntax (same result as above).
animation_tree["parameters/Transition/current_state"]

# Get current state index (read-only).
animation_tree.get("parameters/Transition/current_index")
# Alternative syntax (same result as above).
animation_tree["par
# ...
```

### AnimationNode
*Inherits: **Resource < RefCounted < Object** | Inherited by: AnimationNodeExtension, AnimationNodeOutput, AnimationNodeSync, AnimationNodeTimeScale, AnimationNodeTimeSeek, AnimationRootNode*

Base resource for AnimationTree nodes. In general, it's not used directly, but you can create custom ones with custom blending formulas.

**Properties**
- `bool filter_enabled`

**Methods**
- `String _get_caption() virtual const`
- `AnimationNode _get_child_by_name(name: StringName) virtual const`
- `Dictionary _get_child_nodes() virtual const`
- `Variant _get_parameter_default_value(parameter: StringName) virtual const`
- `Array _get_parameter_list() virtual const`
- `bool _has_filter() virtual const`
- `bool _is_parameter_read_only(parameter: StringName) virtual const`
- `float _process(time: float, seek: bool, is_external_seeking: bool, test_only: bool) virtual`
- `bool add_input(name: String)`
- `void blend_animation(animation: StringName, time: float, delta: float, seeked: bool, is_external_seeking: bool, blend: float, looped_flag: LoopedFlag = 0)`
- `float blend_input(input_index: int, time: float, seek: bool, is_external_seeking: bool, blend: float, filter: FilterAction = 0, sync: bool = true, test_only: bool = false)`
- `float blend_node(name: StringName, node: AnimationNode, time: float, seek: bool, is_external_seeking: bool, blend: float, filter: FilterAction = 0, sync: bool = true, test_only: bool = false)`
- `int find_input(name: String) const`
- `int get_input_count() const`
- `String get_input_name(input: int) const`
- `Variant get_parameter(name: StringName) const`
- `int get_processing_animation_tree_instance_id() const`
- `bool is_path_filtered(path: NodePath) const`
- `bool is_process_testing() const`
- `void remove_input(index: int)`
- `void set_filter_path(path: NodePath, enable: bool)`
- `bool set_input_name(input: int, name: String)`
- `void set_parameter(name: StringName, value: Variant)`

**GDScript Examples**
```gdscript
var current_length = $AnimationTree["parameters/AnimationNodeName/current_length"]
var current_position = $AnimationTree["parameters/AnimationNodeName/current_position"]
var current_delta = $AnimationTree["parameters/AnimationNodeName/current_delta"]
```

### AnimationPlayer
*Inherits: **AnimationMixer < Node < Object***

An animation player is used for general-purpose playback of animations. It contains a dictionary of AnimationLibrary resources and custom blend times between animation transitions.

**Properties**
- `StringName assigned_animation`
- `StringName autoplay` = `&""`
- `StringName current_animation` = `&""`
- `float current_animation_length`
- `float current_animation_position`
- `bool movie_quit_on_finish` = `false`
- `bool playback_auto_capture` = `true`
- `float playback_auto_capture_duration` = `-1.0`
- `EaseType playback_auto_capture_ease_type` = `0`
- `TransitionType playback_auto_capture_transition_type` = `0`
- `float playback_default_blend_time` = `0.0`
- `float speed_scale` = `1.0`

**Methods**
- `StringName animation_get_next(animation_from: StringName) const`
- `void animation_set_next(animation_from: StringName, animation_to: StringName)`
- `void clear_queue()`
- `float get_blend_time(animation_from: StringName, animation_to: StringName) const`
- `AnimationMethodCallMode get_method_call_mode() const`
- `float get_playing_speed() const`
- `AnimationProcessCallback get_process_callback() const`
- `Array[StringName] get_queue()`
- `NodePath get_root() const`
- `float get_section_end_time() const`
- `float get_section_start_time() const`
- `bool has_section() const`
- `bool is_animation_active() const`
- `bool is_playing() const`
- `void pause()`
- `void play(name: StringName = &"", custom_blend: float = -1, custom_speed: float = 1.0, from_end: bool = false)`
- `void play_backwards(name: StringName = &"", custom_blend: float = -1)`
- `void play_section(name: StringName = &"", start_time: float = -1, end_time: float = -1, custom_blend: float = -1, custom_speed: float = 1.0, from_end: bool = false)`
- `void play_section_backwards(name: StringName = &"", start_time: float = -1, end_time: float = -1, custom_blend: float = -1)`
- `void play_section_with_markers(name: StringName = &"", start_marker: StringName = &"", end_marker: StringName = &"", custom_blend: float = -1, custom_speed: float = 1.0, from_end: bool = false)`
- `void play_section_with_markers_backwards(name: StringName = &"", start_marker: StringName = &"", end_marker: StringName = &"", custom_blend: float = -1)`
- `void play_with_capture(name: StringName = &"", duration: float = -1.0, custom_blend: float = -1, custom_speed: float = 1.0, from_end: bool = false, trans_type: TransitionType = 0, ease_type: EaseType = 0)`
- `void queue(name: StringName)`
- `void reset_section()`
- `void seek(seconds: float, update: bool = false, update_only: bool = false)`
- `void set_blend_time(animation_from: StringName, animation_to: StringName, sec: float)`
- `void set_method_call_mode(mode: AnimationMethodCallMode)`
- `void set_process_callback(mode: AnimationProcessCallback)`
- `void set_root(path: NodePath)`
- `void set_section(start_time: float = -1, end_time: float = -1)`
- `void set_section_with_markers(start_marker: StringName = &"", end_marker: StringName = &"")`
- `void stop(keep_state: bool = false)`

**GDScript Examples**
```gdscript
var is_paused = not is_playing() and is_animation_active()
var is_stopped = not is_playing() and not is_animation_active()
```
```gdscript
capture(name, duration, trans_type, ease_type)
play(name, custom_blend, custom_speed, from_end)
```

### AnimationRootNode
*Inherits: **AnimationNode < Resource < RefCounted < Object** | Inherited by: AnimationNodeAnimation, AnimationNodeBlendSpace1D, AnimationNodeBlendSpace2D, AnimationNodeBlendTree, AnimationNodeStateMachine*

AnimationRootNode is a base class for AnimationNodes that hold a complete animation. A complete animation refers to the output of an AnimationNodeOutput in an AnimationNodeBlendTree or the output of another AnimationRootNode. Used for AnimationTree.tree_root or in other AnimationRootNodes.

### AnimationTree
*Inherits: **AnimationMixer < Node < Object***

A node used for advanced animation transitions in an AnimationPlayer.

**Properties**
- `NodePath advance_expression_base_node` = `NodePath(".")`
- `NodePath anim_player` = `NodePath("")`
- `AnimationCallbackModeDiscrete callback_mode_discrete` = `2 (overrides AnimationMixer)`
- `bool deterministic` = `true (overrides AnimationMixer)`
- `AnimationRootNode tree_root`

**Methods**
- `AnimationProcessCallback get_process_callback() const`
- `void set_process_callback(mode: AnimationProcessCallback)`

### Animation
*Inherits: **Resource < RefCounted < Object***

This resource holds data that can be used to animate anything in the engine. Animations are divided into tracks and each track must be linked to a node. The state of that node can be changed through time, by adding timed keys (events) to the track.

**Properties**
- `bool capture_included` = `false`
- `float length` = `1.0`
- `LoopMode loop_mode` = `0`
- `float step` = `0.033333335`

**Methods**
- `void add_marker(name: StringName, time: float)`
- `int add_track(type: TrackType, at_position: int = -1)`
- `StringName animation_track_get_key_animation(track_idx: int, key_idx: int) const`
- `int animation_track_insert_key(track_idx: int, time: float, animation: StringName)`
- `void animation_track_set_key_animation(track_idx: int, key_idx: int, animation: StringName)`
- `float audio_track_get_key_end_offset(track_idx: int, key_idx: int) const`
- `float audio_track_get_key_start_offset(track_idx: int, key_idx: int) const`
- `Resource audio_track_get_key_stream(track_idx: int, key_idx: int) const`
- `int audio_track_insert_key(track_idx: int, time: float, stream: Resource, start_offset: float = 0, end_offset: float = 0)`
- `bool audio_track_is_use_blend(track_idx: int) const`
- `void audio_track_set_key_end_offset(track_idx: int, key_idx: int, offset: float)`
- `void audio_track_set_key_start_offset(track_idx: int, key_idx: int, offset: float)`
- `void audio_track_set_key_stream(track_idx: int, key_idx: int, stream: Resource)`
- `void audio_track_set_use_blend(track_idx: int, enable: bool)`
- `Vector2 bezier_track_get_key_in_handle(track_idx: int, key_idx: int) const`
- `Vector2 bezier_track_get_key_out_handle(track_idx: int, key_idx: int) const`
- `float bezier_track_get_key_value(track_idx: int, key_idx: int) const`
- `int bezier_track_insert_key(track_idx: int, time: float, value: float, in_handle: Vector2 = Vector2(0, 0), out_handle: Vector2 = Vector2(0, 0))`
- `float bezier_track_interpolate(track_idx: int, time: float) const`
- `void bezier_track_set_key_in_handle(track_idx: int, key_idx: int, in_handle: Vector2, balanced_value_time_ratio: float = 1.0)`
- `void bezier_track_set_key_out_handle(track_idx: int, key_idx: int, out_handle: Vector2, balanced_value_time_ratio: float = 1.0)`
- `void bezier_track_set_key_value(track_idx: int, key_idx: int, value: float)`
- `int blend_shape_track_insert_key(track_idx: int, time: float, amount: float)`
- `float blend_shape_track_interpolate(track_idx: int, time_sec: float, backward: bool = false) const`
- `void clear()`
- `void compress(page_size: int = 8192, fps: int = 120, split_tolerance: float = 4.0)`
- `void copy_track(track_idx: int, to_animation: Animation)`
- `int find_track(path: NodePath, type: TrackType) const`
- `StringName get_marker_at_time(time: float) const`
- `Color get_marker_color(name: StringName) const`
- `PackedStringArray get_marker_names() const`
- `float get_marker_time(name: StringName) const`
- `StringName get_next_marker(time: float) const`
- `StringName get_prev_marker(time: float) const`
- `int get_track_count() const`
- `bool has_marker(name: StringName) const`
- `StringName method_track_get_name(track_idx: int, key_idx: int) const`
- `Array method_track_get_params(track_idx: int, key_idx: int) const`
- `void optimize(allowed_velocity_err: float = 0.01, allowed_angular_err: float = 0.01, precision: int = 3)`
- `int position_track_insert_key(track_idx: int, time: float, position: Vector3)`

**GDScript Examples**
```gdscript
# This creates an animation that makes the node "Enemy" move to the right by
# 100 pixels in 2.0 seconds.
var animation = Animation.new()
var track_index = animation.add_track(Animation.TYPE_VALUE)
animation.track_set_path(track_index, "Enemy:position:x")
animation.track_insert_key(track_index, 0.0, 0)
animation.track_insert_key(track_index, 2.0, 100)
animation.length = 2.0
```

### AtlasTexture
*Inherits: **Texture2D < Texture < Resource < RefCounted < Object***

Texture2D resource that draws only part of its atlas texture, as defined by the region. An additional margin can also be set, which is useful for small adjustments.

**Properties**
- `Texture2D atlas`
- `bool filter_clip` = `false`
- `Rect2 margin` = `Rect2(0, 0, 0, 0)`
- `Rect2 region` = `Rect2(0, 0, 0, 0)`
- `bool resource_local_to_scene` = `false (overrides Resource)`

### BitMap
*Inherits: **Resource < RefCounted < Object***

A two-dimensional array of boolean values, can be used to efficiently store a binary matrix (every matrix element takes only one bit) and query the values using natural cartesian coordinates.

**Methods**
- `Image convert_to_image() const`
- `void create(size: Vector2i)`
- `void create_from_image_alpha(image: Image, threshold: float = 0.1)`
- `bool get_bit(x: int, y: int) const`
- `bool get_bitv(position: Vector2i) const`
- `Vector2i get_size() const`
- `int get_true_bit_count() const`
- `void grow_mask(pixels: int, rect: Rect2i)`
- `Array[PackedVector2Array] opaque_to_polygons(rect: Rect2i, epsilon: float = 2.0) const`
- `void resize(new_size: Vector2i)`
- `void set_bit(x: int, y: int, bit: bool)`
- `void set_bit_rect(rect: Rect2i, bit: bool)`
- `void set_bitv(position: Vector2i, bit: bool)`

**GDScript Examples**
```gdscript
Rect2(Vector2(), get_size())
```

### CSharpScript
*Inherits: **Script < Resource < RefCounted < Object***

This class represents a C# script. It is the C# equivalent of the GDScript class and is only available in Mono-enabled Godot builds.

**Methods**
- `Variant new(...) vararg`

### CameraTexture
*Inherits: **Texture2D < Texture < Resource < RefCounted < Object***

This texture gives access to the camera texture provided by a CameraFeed.

**Properties**
- `int camera_feed_id` = `0`
- `bool camera_is_active` = `false`
- `bool resource_local_to_scene` = `false (overrides Resource)`
- `FeedImage which_feed` = `0`

### CompressedTexture2DArray
*Inherits: **CompressedTextureLayered < TextureLayered < Texture < Resource < RefCounted < Object***

A texture array that is loaded from a .ctexarray file. This file format is internal to Godot; it is created by importing other image formats with the import system. CompressedTexture2DArray can use one of 4 compression methods:

### CompressedTexture2D
*Inherits: **Texture2D < Texture < Resource < RefCounted < Object***

A texture that is loaded from a .ctex file. This file format is internal to Godot; it is created by importing other image formats with the import system. CompressedTexture2D can use one of 4 compression methods (including a lack of any compression):

**Properties**
- `String load_path` = `""`
- `bool resource_local_to_scene` = `false (overrides Resource)`

**Methods**
- `Error load(path: String)`

### Curve2D
*Inherits: **Resource < RefCounted < Object***

This class describes a Bézier curve in 2D space. It is mainly used to give a shape to a Path2D, but can be manually sampled for other purposes.

**Properties**
- `float bake_interval` = `5.0`
- `int point_count` = `0`

**Methods**
- `void add_point(position: Vector2, in: Vector2 = Vector2(0, 0), out: Vector2 = Vector2(0, 0), index: int = -1)`
- `void clear_points()`
- `float get_baked_length() const`
- `PackedVector2Array get_baked_points() const`
- `float get_closest_offset(to_point: Vector2) const`
- `Vector2 get_closest_point(to_point: Vector2) const`
- `Vector2 get_point_in(idx: int) const`
- `Vector2 get_point_out(idx: int) const`
- `Vector2 get_point_position(idx: int) const`
- `void remove_point(idx: int)`
- `Vector2 sample(idx: int, t: float) const`
- `Vector2 sample_baked(offset: float = 0.0, cubic: bool = false) const`
- `Transform2D sample_baked_with_rotation(offset: float = 0.0, cubic: bool = false) const`
- `Vector2 samplef(fofs: float) const`
- `void set_point_in(idx: int, position: Vector2)`
- `void set_point_out(idx: int, position: Vector2)`
- `void set_point_position(idx: int, position: Vector2)`
- `PackedVector2Array tessellate(max_stages: int = 5, tolerance_degrees: float = 4) const`
- `PackedVector2Array tessellate_even_length(max_stages: int = 5, tolerance_length: float = 20.0) const`

**GDScript Examples**
```gdscript
var baked = curve.sample_baked_with_rotation(offset)
# The returned Transform2D can be set directly.
transform = baked
# You can also read the origin and rotation separately from the returned Transform2D.
position = baked.get_origin()
rotation = baked.get_rotation()
```

### Curve3D
*Inherits: **Resource < RefCounted < Object***

This class describes a Bézier curve in 3D space. It is mainly used to give a shape to a Path3D, but can be manually sampled for other purposes.

**Properties**
- `float bake_interval` = `0.2`
- `bool closed` = `false`
- `int point_count` = `0`
- `bool up_vector_enabled` = `true`

**Methods**
- `void add_point(position: Vector3, in: Vector3 = Vector3(0, 0, 0), out: Vector3 = Vector3(0, 0, 0), index: int = -1)`
- `void clear_points()`
- `float get_baked_length() const`
- `PackedVector3Array get_baked_points() const`
- `PackedFloat32Array get_baked_tilts() const`
- `PackedVector3Array get_baked_up_vectors() const`
- `float get_closest_offset(to_point: Vector3) const`
- `Vector3 get_closest_point(to_point: Vector3) const`
- `Vector3 get_point_in(idx: int) const`
- `Vector3 get_point_out(idx: int) const`
- `Vector3 get_point_position(idx: int) const`
- `float get_point_tilt(idx: int) const`
- `void remove_point(idx: int)`
- `Vector3 sample(idx: int, t: float) const`
- `Vector3 sample_baked(offset: float = 0.0, cubic: bool = false) const`
- `Vector3 sample_baked_up_vector(offset: float, apply_tilt: bool = false) const`
- `Transform3D sample_baked_with_rotation(offset: float = 0.0, cubic: bool = false, apply_tilt: bool = false) const`
- `Vector3 samplef(fofs: float) const`
- `void set_point_in(idx: int, position: Vector3)`
- `void set_point_out(idx: int, position: Vector3)`
- `void set_point_position(idx: int, position: Vector3)`
- `void set_point_tilt(idx: int, tilt: float)`
- `PackedVector3Array tessellate(max_stages: int = 5, tolerance_degrees: float = 4) const`
- `PackedVector3Array tessellate_even_length(max_stages: int = 5, tolerance_length: float = 0.2) const`

### FastNoiseLite
*Inherits: **Noise < Resource < RefCounted < Object***

This class generates noise using the FastNoiseLite library, which is a collection of several noise algorithms including Cellular, Perlin, Value, and more.

**Properties**
- `CellularDistanceFunction cellular_distance_function` = `0`
- `float cellular_jitter` = `1.0`
- `CellularReturnType cellular_return_type` = `1`
- `float domain_warp_amplitude` = `30.0`
- `bool domain_warp_enabled` = `false`
- `float domain_warp_fractal_gain` = `0.5`
- `float domain_warp_fractal_lacunarity` = `6.0`
- `int domain_warp_fractal_octaves` = `5`
- `DomainWarpFractalType domain_warp_fractal_type` = `1`
- `float domain_warp_frequency` = `0.05`
- `DomainWarpType domain_warp_type` = `0`
- `float fractal_gain` = `0.5`
- `float fractal_lacunarity` = `2.0`
- `int fractal_octaves` = `5`
- `float fractal_ping_pong_strength` = `2.0`
- `FractalType fractal_type` = `1`
- `float fractal_weighted_strength` = `0.0`
- `float frequency` = `0.01`
- `NoiseType noise_type` = `1`
- `Vector3 offset` = `Vector3(0, 0, 0)`
- `int seed` = `0`

### FontFile
*Inherits: **Font < Resource < RefCounted < Object***

FontFile contains a set of glyphs to represent Unicode characters imported from a font file, as well as a cache of rasterized glyphs, and a set of fallback Fonts to use.

**Properties**
- `bool allow_system_fallback` = `true`
- `FontAntialiasing antialiasing` = `1`
- `PackedByteArray data` = `PackedByteArray()`
- `bool disable_embedded_bitmaps` = `true`
- `int fixed_size` = `0`
- `FixedSizeScaleMode fixed_size_scale_mode` = `0`
- `String font_name` = `""`
- `int font_stretch` = `100`
- `BitField[FontStyle] font_style` = `0`
- `int font_weight` = `400`
- `bool force_autohinter` = `false`
- `bool generate_mipmaps` = `false`
- `Hinting hinting` = `1`
- `bool keep_rounding_remainders` = `true`
- `bool modulate_color_glyphs` = `false`
- `int msdf_pixel_range` = `16`
- `int msdf_size` = `48`
- `bool multichannel_signed_distance_field` = `false`
- `Dictionary opentype_feature_overrides` = `{}`
- `float oversampling` = `0.0`
- `String style_name` = `""`
- `SubpixelPositioning subpixel_positioning` = `1`

**Methods**
- `void clear_cache()`
- `void clear_glyphs(cache_index: int, size: Vector2i)`
- `void clear_kerning_map(cache_index: int, size: int)`
- `void clear_size_cache(cache_index: int)`
- `void clear_textures(cache_index: int, size: Vector2i)`
- `float get_cache_ascent(cache_index: int, size: int) const`
- `int get_cache_count() const`
- `float get_cache_descent(cache_index: int, size: int) const`
- `float get_cache_scale(cache_index: int, size: int) const`
- `float get_cache_underline_position(cache_index: int, size: int) const`
- `float get_cache_underline_thickness(cache_index: int, size: int) const`
- `int get_char_from_glyph_index(size: int, glyph_index: int) const`
- `float get_embolden(cache_index: int) const`
- `float get_extra_baseline_offset(cache_index: int) const`
- `int get_extra_spacing(cache_index: int, spacing: SpacingType) const`
- `int get_face_index(cache_index: int) const`
- `Vector2 get_glyph_advance(cache_index: int, size: int, glyph: int) const`
- `int get_glyph_index(size: int, char: int, variation_selector: int) const`
- `PackedInt32Array get_glyph_list(cache_index: int, size: Vector2i) const`
- `Vector2 get_glyph_offset(cache_index: int, size: Vector2i, glyph: int) const`
- `Vector2 get_glyph_size(cache_index: int, size: Vector2i, glyph: int) const`
- `int get_glyph_texture_idx(cache_index: int, size: Vector2i, glyph: int) const`
- `Rect2 get_glyph_uv_rect(cache_index: int, size: Vector2i, glyph: int) const`
- `Vector2 get_kerning(cache_index: int, size: int, glyph_pair: Vector2i) const`
- `Array[Vector2i] get_kerning_list(cache_index: int, size: int) const`
- `bool get_language_support_override(language: String) const`
- `PackedStringArray get_language_support_overrides() const`
- `bool get_script_support_override(script: String) const`
- `PackedStringArray get_script_support_overrides() const`
- `Array[Vector2i] get_size_cache_list(cache_index: int) const`
- `int get_texture_count(cache_index: int, size: Vector2i) const`
- `Image get_texture_image(cache_index: int, size: Vector2i, texture_index: int) const`
- `PackedInt32Array get_texture_offsets(cache_index: int, size: Vector2i, texture_index: int) const`
- `Transform2D get_transform(cache_index: int) const`
- `Dictionary get_variation_coordinates(cache_index: int) const`
- `Error load_bitmap_font(path: String)`
- `Error load_dynamic_font(path: String)`
- `void remove_cache(cache_index: int)`
- `void remove_glyph(cache_index: int, size: Vector2i, glyph: int)`
- `void remove_kerning(cache_index: int, size: int, glyph_pair: Vector2i)`

**GDScript Examples**
```gdscript
var f = load("res://BarlowCondensed-Bold.ttf")
$Label.add_theme_font_override("font", f)
$Label.add_theme_font_size_override("font_size", 64)
```

### FontVariation
*Inherits: **Font < Resource < RefCounted < Object***

Provides OpenType variations, simulated bold / slant, and additional font settings like OpenType features and extra spacing.

**Properties**
- `Font base_font`
- `float baseline_offset` = `0.0`
- `Dictionary opentype_features` = `{}`
- `int spacing_bottom` = `0`
- `int spacing_glyph` = `0`
- `int spacing_space` = `0`
- `int spacing_top` = `0`
- `float variation_embolden` = `0.0`
- `int variation_face_index` = `0`
- `Dictionary variation_opentype` = `{}`
- `Transform2D variation_transform` = `Transform2D(1, 0, 0, 1, 0, 0)`

**Methods**
- `void set_spacing(spacing: SpacingType, value: int)`

**GDScript Examples**
```gdscript
var fv = FontVariation.new()
fv.base_font = load("res://BarlowCondensed-Regular.ttf")
fv.variation_embolden = 1.2
$Label.add_theme_font_override("font", fv)
$Label.add_theme_font_size_override("font_size", 64)
```
```gdscript
var fv = FontVariation.new();
var ts = TextServerManager.get_primary_interface()
fv.base_font = load("res://BarlowCondensed-Regular.ttf")
fv.variation_opentype = { ts.name_to_tag("wght"): 900, ts.name_to_tag("custom_hght"): 900 }
```

### GDScriptSyntaxHighlighter
*Inherits: **EditorSyntaxHighlighter < SyntaxHighlighter < Resource < RefCounted < Object***

Note: This class can only be used for editor plugins because it relies on editor settings.

**GDScript Examples**
```gdscript
var code_preview = TextEdit.new()
var highlighter = GDScriptSyntaxHighlighter.new()
code_preview.syntax_highlighter = highlighter
```

### GDScript
*Inherits: **Script < Resource < RefCounted < Object***

A script implemented in the GDScript programming language, saved with the .gd extension. The script extends the functionality of all objects that instantiate it.

**Methods**
- `Variant new(...) vararg`

**GDScript Examples**
```gdscript
var MyClass = load("myclass.gd")
var instance = MyClass.new()
print(instance.get_script() == MyClass) # Prints true
```

### GradientTexture1D
*Inherits: **Texture2D < Texture < Resource < RefCounted < Object***

A 1D texture that obtains colors from a Gradient to fill the texture data. The texture is filled by sampling the gradient for each pixel. Therefore, the texture does not necessarily represent an exact copy of the gradient, as it may miss some colors if there are not enough pixels. See also GradientTexture2D, CurveTexture and CurveXYZTexture.

**Properties**
- `Gradient gradient`
- `bool resource_local_to_scene` = `false (overrides Resource)`
- `bool use_hdr` = `false`
- `int width` = `256`

### GradientTexture2D
*Inherits: **Texture2D < Texture < Resource < RefCounted < Object***

A 2D texture that obtains colors from a Gradient to fill the texture data. This texture is able to transform a color transition into different patterns such as a linear or a radial gradient. The texture is filled by interpolating colors starting from fill_from to fill_to offsets by default, but the gradient fill can be repeated to cover the entire texture.

**Properties**
- `Fill fill` = `0`
- `Vector2 fill_from` = `Vector2(0, 0)`
- `Vector2 fill_to` = `Vector2(1, 0)`
- `Gradient gradient`
- `int height` = `64`
- `Repeat repeat` = `0`
- `bool resource_local_to_scene` = `false (overrides Resource)`
- `bool use_hdr` = `false`
- `int width` = `64`

### Gradient
*Inherits: **Resource < RefCounted < Object***

This resource describes a color transition by defining a set of colored points and how to interpolate between them.

**Properties**
- `PackedColorArray colors` = `PackedColorArray(0, 0, 0, 1, 1, 1, 1, 1)`
- `ColorSpace interpolation_color_space` = `0`
- `InterpolationMode interpolation_mode` = `0`
- `PackedFloat32Array offsets` = `PackedFloat32Array(0, 1)`

**Methods**
- `void add_point(offset: float, color: Color)`
- `Color get_color(point: int)`
- `float get_offset(point: int)`
- `int get_point_count() const`
- `void remove_point(point: int)`
- `void reverse()`
- `Color sample(offset: float)`
- `void set_color(point: int, color: Color)`
- `void set_offset(point: int, offset: float)`

### ImageTexture3D
*Inherits: **Texture3D < Texture < Resource < RefCounted < Object***

ImageTexture3D is a 3-dimensional ImageTexture that has a width, height, and depth. See also ImageTextureLayered.

**Methods**
- `Error create(format: Format, width: int, height: int, depth: int, use_mipmaps: bool, data: Array[Image])`
- `void update(data: Array[Image])`

### ImageTextureLayered
*Inherits: **TextureLayered < Texture < Resource < RefCounted < Object** | Inherited by: Cubemap, CubemapArray, Texture2DArray*

Base class for Texture2DArray, Cubemap and CubemapArray. Cannot be used directly, but contains all the functions necessary for accessing the derived resource types. See also Texture3D.

**Methods**
- `Error create_from_images(images: Array[Image])`
- `void update_layer(image: Image, layer: int)`

**GDScript Examples**
```gdscript
# Fill in an array of Images with different colors.
var images = []
const LAYERS = 6
for i in LAYERS:
    var image = Image.create_empty(128, 128, false, Image.FORMAT_RGB8)
    if i % 3 == 0:
        image.fill(Color.RED)
    elif i % 3 == 1:
        image.fill(Color.GREEN)
    else:
        image.fill(Color.BLUE)
    images.push_back(image)

# Create and save a 2D texture array. The array of images must have at least 1 Image.
var texture_2d_array = Texture2DArray.new()
texture_2d_array.create_from_images(images)
ResourceSaver.save(texture_2d_array, "res://texture_2d_array.res", ResourceSaver.
# ...
```

### ImageTexture
*Inherits: **Texture2D < Texture < Resource < RefCounted < Object***

A Texture2D based on an Image. For an image to be displayed, an ImageTexture has to be created from it using the create_from_image() method:

**Properties**
- `bool resource_local_to_scene` = `false (overrides Resource)`

**Methods**
- `ImageTexture create_from_image(image: Image) static`
- `Format get_format() const`
- `void set_image(image: Image)`
- `void set_size_override(size: Vector2i)`
- `void update(image: Image)`

**GDScript Examples**
```gdscript
var image = Image.load_from_file("res://icon.svg")
var texture = ImageTexture.create_from_image(image)
$Sprite2D.texture = texture
```
```gdscript
var texture = load("res://icon.svg")
$Sprite2D.texture = texture
```

### NoiseTexture2D
*Inherits: **Texture2D < Texture < Resource < RefCounted < Object***

Uses the FastNoiseLite library or other noise generators to fill the texture data of your desired size. NoiseTexture2D can also generate normal map textures.

**Properties**
- `bool as_normal_map` = `false`
- `float bump_strength` = `8.0`
- `Gradient color_ramp`
- `bool generate_mipmaps` = `true`
- `int height` = `512`
- `bool in_3d_space` = `false`
- `bool invert` = `false`
- `Noise noise`
- `bool normalize` = `true`
- `bool resource_local_to_scene` = `false (overrides Resource)`
- `bool seamless` = `false`
- `float seamless_blend_skirt` = `0.1`
- `int width` = `512`

**GDScript Examples**
```gdscript
var texture = NoiseTexture2D.new()
texture.noise = FastNoiseLite.new()
await texture.changed
var image = texture.get_image()
var data = image.get_data()
```

### Occluder3D
*Inherits: **Resource < RefCounted < Object** | Inherited by: ArrayOccluder3D, BoxOccluder3D, PolygonOccluder3D, QuadOccluder3D, SphereOccluder3D*

Occluder3D stores an occluder shape that can be used by the engine's occlusion culling system.

**Methods**
- `PackedInt32Array get_indices() const`
- `PackedVector3Array get_vertices() const`

### OccluderInstance3D
*Inherits: **VisualInstance3D < Node3D < Node < Object***

Occlusion culling can improve rendering performance in closed/semi-open areas by hiding geometry that is occluded by other objects.

**Properties**
- `int bake_mask` = `4294967295`
- `float bake_simplification_distance` = `0.1`
- `Occluder3D occluder`

**Methods**
- `bool get_bake_mask_value(layer_number: int) const`
- `void set_bake_mask_value(layer_number: int, value: bool)`

### PackedScene
*Inherits: **Resource < RefCounted < Object***

A simplified interface to a scene file. Provides access to operations and checks that can be performed on the scene resource itself.

**Methods**
- `bool can_instantiate() const`
- `SceneState get_state() const`
- `Node instantiate(edit_state: GenEditState = 0) const`
- `Error pack(path: Node)`

**GDScript Examples**
```gdscript
# Use load() instead of preload() if the path isn't known at compile-time.
var scene = preload("res://scene.tscn").instantiate()
# Add the node as a child of the node the script is attached to.
add_child(scene)
```
```gdscript
# Create the objects.
var node = Node2D.new()
var body = RigidBody2D.new()
var collision = CollisionShape2D.new()

# Create the object hierarchy.
body.add_child(collision)
node.add_child(body)

# Change owner of `body`, but not of `collision`.
body.owner = node
var scene = PackedScene.new()

# Only `node` and `body` are now packed.
var result = scene.pack(node)
if result == OK:
    var error = ResourceSaver.save(scene, "res://path/name.tscn")  # Or "user://..."
    if error != OK:
        push_error("An error occurred while saving the scene to disk.")
```

### PlaceholderTexture2DArray
*Inherits: **PlaceholderTextureLayered < TextureLayered < Texture < Resource < RefCounted < Object***

This class is used when loading a project that uses a Texture2D subclass in 2 conditions:

### PlaceholderTexture2D
*Inherits: **Texture2D < Texture < Resource < RefCounted < Object***

This class is used when loading a project that uses a Texture2D subclass in 2 conditions:

**Properties**
- `bool resource_local_to_scene` = `false (overrides Resource)`
- `Vector2 size` = `Vector2(1, 1)`

### PortableCompressedTexture2D
*Inherits: **Texture2D < Texture < Resource < RefCounted < Object***

This class allows storing compressed textures as self contained (not imported) resources.

**Properties**
- `bool keep_compressed_buffer` = `false`
- `bool resource_local_to_scene` = `false (overrides Resource)`
- `Vector2 size_override` = `Vector2(0, 0)`

**Methods**
- `void create_from_image(image: Image, compression_mode: CompressionMode, normal_map: bool = false, lossy_quality: float = 0.8)`
- `CompressionMode get_compression_mode() const`
- `Format get_format() const`
- `bool is_keeping_all_compressed_buffers() static`
- `void set_basisu_compressor_params(uastc_level: int, rdo_quality_loss: float)`
- `void set_keep_all_compressed_buffers(keep: bool) static`

### SceneState
*Inherits: **RefCounted < Object***

Maintains a list of resources, nodes, exported and overridden properties, and built-in scripts associated with a scene. They cannot be modified from a SceneState, only accessed. Useful for peeking into what a PackedScene contains without instantiating it.

**Methods**
- `SceneState get_base_scene_state() const`
- `Array get_connection_binds(idx: int) const`
- `int get_connection_count() const`
- `int get_connection_flags(idx: int) const`
- `StringName get_connection_method(idx: int) const`
- `StringName get_connection_signal(idx: int) const`
- `NodePath get_connection_source(idx: int) const`
- `NodePath get_connection_target(idx: int) const`
- `int get_connection_unbinds(idx: int) const`
- `int get_node_count() const`
- `PackedStringArray get_node_groups(idx: int) const`
- `int get_node_index(idx: int) const`
- `PackedScene get_node_instance(idx: int) const`
- `String get_node_instance_placeholder(idx: int) const`
- `StringName get_node_name(idx: int) const`
- `NodePath get_node_owner_path(idx: int) const`
- `NodePath get_node_path(idx: int, for_parent: bool = false) const`
- `int get_node_property_count(idx: int) const`
- `StringName get_node_property_name(idx: int, prop_idx: int) const`
- `Variant get_node_property_value(idx: int, prop_idx: int) const`
- `StringName get_node_type(idx: int) const`
- `String get_path() const`
- `bool is_node_instance_placeholder(idx: int) const`

### ScriptBacktrace
*Inherits: **RefCounted < Object***

ScriptBacktrace holds an already captured backtrace of a specific script language, such as GDScript or C#, which are captured using Engine.capture_script_backtraces().

**Methods**
- `String format(indent_all: int = 0, indent_frames: int = 4) const`
- `int get_frame_count() const`
- `String get_frame_file(index: int) const`
- `String get_frame_function(index: int) const`
- `int get_frame_line(index: int) const`
- `int get_global_variable_count() const`
- `String get_global_variable_name(variable_index: int) const`
- `Variant get_global_variable_value(variable_index: int) const`
- `String get_language_name() const`
- `int get_local_variable_count(frame_index: int) const`
- `String get_local_variable_name(frame_index: int, variable_index: int) const`
- `Variant get_local_variable_value(frame_index: int, variable_index: int) const`
- `int get_member_variable_count(frame_index: int) const`
- `String get_member_variable_name(frame_index: int, variable_index: int) const`
- `Variant get_member_variable_value(frame_index: int, variable_index: int) const`
- `bool is_empty() const`

### ScriptCreateDialog
*Inherits: **ConfirmationDialog < AcceptDialog < Window < Viewport < Node < Object***

The ScriptCreateDialog creates script files according to a given template for a given scripting language. The standard use is to configure its fields prior to calling one of the Window.popup() methods.

**Properties**
- `bool dialog_hide_on_ok` = `false (overrides AcceptDialog)`
- `String ok_button_text` = `"Create" (overrides AcceptDialog)`
- `String title` = `"Attach Node Script" (overrides Window)`

**Methods**
- `void config(inherits: String, path: String, built_in_enabled: bool = true, load_enabled: bool = true)`

**GDScript Examples**
```gdscript
func _ready():
    var dialog = ScriptCreateDialog.new();
    dialog.config("Node", "res://new_node.gd") # For in-engine types.
    dialog.config("\"res://base_node.gd\"", "res://derived_node.gd") # For script types.
    dialog.popup_centered()
```

### ScriptEditorBase
*Inherits: **VBoxContainer < BoxContainer < Container < Control < CanvasItem < Node < Object***

Base editor for editing scripts in the ScriptEditor. This does not include documentation items.

**Methods**
- `void add_syntax_highlighter(highlighter: EditorSyntaxHighlighter)`
- `Control get_base_editor() const`

### ScriptEditor
*Inherits: **PanelContainer < Container < Control < CanvasItem < Node < Object***

Godot editor's script editor.

**Methods**
- `void clear_docs_from_script(script: Script)`
- `PackedStringArray get_breakpoints()`
- `ScriptEditorBase get_current_editor() const`
- `Script get_current_script()`
- `Array[ScriptEditorBase] get_open_script_editors() const`
- `Array[Script] get_open_scripts() const`
- `void goto_help(topic: String)`
- `void goto_line(line_number: int)`
- `void open_script_create_dialog(base_name: String, base_path: String)`
- `void register_syntax_highlighter(syntax_highlighter: EditorSyntaxHighlighter)`
- `void unregister_syntax_highlighter(syntax_highlighter: EditorSyntaxHighlighter)`
- `void update_docs_from_script(script: Script)`

**GDScript Examples**
```gdscript
# Shows help for the Node class.
class_name:Node
# Shows help for the global min function.
# Global objects are accessible in the `@GlobalScope` namespace, shown here.
class_method:@GlobalScope:min
# Shows help for get_viewport in the Node class.
class_method:Node:get_viewport
# Shows help for the Input constant MOUSE_BUTTON_MIDDLE.
class_constant:Input:MOUSE_BUTTON_MIDDLE
# Shows help for the BaseButton signal pressed.
class_signal:BaseButton:pressed
# Shows help for the CanvasItem property visible.
class_property:CanvasItem:visible
# Shows help for the GDScript annotation export.
# Annotatio
# ...
```

### ScriptExtension
*Inherits: **Script < Resource < RefCounted < Object***

There is currently no description for this class. Please help us by contributing one!

**Methods**
- `bool _can_instantiate() virtual required const`
- `bool _editor_can_reload_from_file() virtual required`
- `Script _get_base_script() virtual required const`
- `String _get_class_icon_path() virtual const`
- `Dictionary _get_constants() virtual required const`
- `StringName _get_doc_class_name() virtual required const`
- `Array[Dictionary] _get_documentation() virtual required const`
- `StringName _get_global_name() virtual required const`
- `StringName _get_instance_base_type() virtual required const`
- `ScriptLanguage _get_language() virtual required const`
- `int _get_member_line(member: StringName) virtual required const`
- `Array[StringName] _get_members() virtual required const`
- `Dictionary _get_method_info(method: StringName) virtual required const`
- `Variant _get_property_default_value(property: StringName) virtual required const`
- `Variant _get_rpc_config() virtual required const`
- `Variant _get_script_method_argument_count(method: StringName) virtual const`
- `Array[Dictionary] _get_script_method_list() virtual required const`
- `Array[Dictionary] _get_script_property_list() virtual required const`
- `Array[Dictionary] _get_script_signal_list() virtual required const`
- `String _get_source_code() virtual required const`
- `bool _has_method(method: StringName) virtual required const`
- `bool _has_property_default_value(property: StringName) virtual required const`
- `bool _has_script_signal(signal: StringName) virtual required const`
- `bool _has_source_code() virtual required const`
- `bool _has_static_method(method: StringName) virtual required const`
- `bool _inherits_script(script: Script) virtual required const`
- `void* _instance_create(for_object: Object) virtual required const`
- `bool _instance_has(object: Object) virtual required const`
- `bool _is_abstract() virtual const`
- `bool _is_placeholder_fallback_enabled() virtual required const`
- `bool _is_tool() virtual required const`
- `bool _is_valid() virtual required const`
- `void _placeholder_erased(placeholder: void*) virtual`
- `void* _placeholder_instance_create(for_object: Object) virtual required const`
- `Error _reload(keep_state: bool) virtual required`
- `void _set_source_code(code: String) virtual required`
- `void _update_exports() virtual required`

### ScriptLanguageExtension
*Inherits: **ScriptLanguage < Object***

There is currently no description for this class. Please help us by contributing one!

**Methods**
- `void _add_global_constant(name: StringName, value: Variant) virtual required`
- `void _add_named_global_constant(name: StringName, value: Variant) virtual required`
- `String _auto_indent_code(code: String, from_line: int, to_line: int) virtual required const`
- `bool _can_inherit_from_file() virtual required const`
- `bool _can_make_function() virtual required const`
- `Dictionary _complete_code(code: String, path: String, owner: Object) virtual required const`
- `Object _create_script() virtual required const`
- `Array[Dictionary] _debug_get_current_stack_info() virtual required`
- `String _debug_get_error() virtual required const`
- `Dictionary _debug_get_globals(max_subitems: int, max_depth: int) virtual required`
- `int _debug_get_stack_level_count() virtual required const`
- `String _debug_get_stack_level_function(level: int) virtual required const`
- `void* _debug_get_stack_level_instance(level: int) virtual required`
- `int _debug_get_stack_level_line(level: int) virtual required const`
- `Dictionary _debug_get_stack_level_locals(level: int, max_subitems: int, max_depth: int) virtual required`
- `Dictionary _debug_get_stack_level_members(level: int, max_subitems: int, max_depth: int) virtual required`
- `String _debug_get_stack_level_source(level: int) virtual required const`
- `String _debug_parse_stack_level_expression(level: int, expression: String, max_subitems: int, max_depth: int) virtual required`
- `int _find_function(function: String, code: String) virtual required const`
- `void _finish() virtual required`
- `void _frame() virtual required`
- `Array[Dictionary] _get_built_in_templates(object: StringName) virtual required const`
- `PackedStringArray _get_comment_delimiters() virtual required const`
- `PackedStringArray _get_doc_comment_delimiters() virtual const`
- `String _get_extension() virtual required const`
- `Dictionary _get_global_class_name(path: String) virtual required const`
- `String _get_name() virtual required const`
- `Array[Dictionary] _get_public_annotations() virtual required const`
- `Dictionary _get_public_constants() virtual required const`
- `Array[Dictionary] _get_public_functions() virtual required const`
- `PackedStringArray _get_recognized_extensions() virtual required const`
- `PackedStringArray _get_reserved_words() virtual required const`
- `PackedStringArray _get_string_delimiters() virtual required const`
- `String _get_type() virtual required const`
- `bool _handles_global_class_type(type: String) virtual required const`
- `bool _has_named_classes() virtual const`
- `void _init() virtual required`
- `bool _is_control_flow_keyword(keyword: String) virtual required const`
- `bool _is_using_templates() virtual required`
- `Dictionary _lookup_code(code: String, symbol: String, path: String, owner: Object) virtual required const`

### ScriptLanguage
*Inherits: **Object** | Inherited by: ScriptLanguageExtension*

There is currently no description for this class. Please help us by contributing one!

### Script
*Inherits: **Resource < RefCounted < Object** | Inherited by: CSharpScript, GDScript, ScriptExtension*

A class stored as a resource. A script extends the functionality of all objects that instantiate it.

**Properties**
- `String source_code`

**Methods**
- `bool can_instantiate() const`
- `Script get_base_script() const`
- `StringName get_global_name() const`
- `StringName get_instance_base_type() const`
- `Variant get_property_default_value(property: StringName)`
- `Variant get_rpc_config() const`
- `Dictionary get_script_constant_map()`
- `Array[Dictionary] get_script_method_list()`
- `Array[Dictionary] get_script_property_list()`
- `Array[Dictionary] get_script_signal_list()`
- `bool has_script_signal(signal_name: StringName) const`
- `bool has_source_code() const`
- `bool instance_has(base_object: Object) const`
- `bool is_abstract() const`
- `bool is_tool() const`
- `Error reload(keep_state: bool = false)`

**GDScript Examples**
```gdscript
class_name MyNode
extends Node
```

### StyleBoxEmpty
*Inherits: **StyleBox < Resource < RefCounted < Object***

An empty StyleBox that can be used to display nothing instead of the default style (e.g. it can "disable" focus styles).

### StyleBoxFlat
*Inherits: **StyleBox < Resource < RefCounted < Object***

By configuring various properties of this style box, you can achieve many common looks without the need of a texture. This includes optionally rounded borders, antialiasing, shadows, and skew.

**Properties**
- `bool anti_aliasing` = `true`
- `float anti_aliasing_size` = `1.0`
- `Color bg_color` = `Color(0.6, 0.6, 0.6, 1)`
- `bool border_blend` = `false`
- `Color border_color` = `Color(0.8, 0.8, 0.8, 1)`
- `int border_width_bottom` = `0`
- `int border_width_left` = `0`
- `int border_width_right` = `0`
- `int border_width_top` = `0`
- `int corner_detail` = `8`
- `int corner_radius_bottom_left` = `0`
- `int corner_radius_bottom_right` = `0`
- `int corner_radius_top_left` = `0`
- `int corner_radius_top_right` = `0`
- `bool draw_center` = `true`
- `float expand_margin_bottom` = `0.0`
- `float expand_margin_left` = `0.0`
- `float expand_margin_right` = `0.0`
- `float expand_margin_top` = `0.0`
- `Color shadow_color` = `Color(0, 0, 0, 0.6)`
- `Vector2 shadow_offset` = `Vector2(0, 0)`
- `int shadow_size` = `0`
- `Vector2 skew` = `Vector2(0, 0)`

**Methods**
- `int get_border_width(margin: Side) const`
- `int get_border_width_min() const`
- `int get_corner_radius(corner: Corner) const`
- `float get_expand_margin(margin: Side) const`
- `void set_border_width(margin: Side, width: int)`
- `void set_border_width_all(width: int)`
- `void set_corner_radius(corner: Corner, radius: int)`
- `void set_corner_radius_all(radius: int)`
- `void set_expand_margin(margin: Side, size: float)`
- `void set_expand_margin_all(size: float)`

### StyleBoxLine
*Inherits: **StyleBox < Resource < RefCounted < Object***

A StyleBox that displays a single line of a given color and thickness. The line can be either horizontal or vertical. Useful for separators.

**Properties**
- `Color color` = `Color(0, 0, 0, 1)`
- `float grow_begin` = `1.0`
- `float grow_end` = `1.0`
- `int thickness` = `1`
- `bool vertical` = `false`

### StyleBoxTexture
*Inherits: **StyleBox < Resource < RefCounted < Object***

A texture-based nine-patch StyleBox, in a way similar to NinePatchRect. This stylebox performs a 3×3 scaling of a texture, where only the center cell is fully stretched. This makes it possible to design bordered styles regardless of the stylebox's size.

**Properties**
- `AxisStretchMode axis_stretch_horizontal` = `0`
- `AxisStretchMode axis_stretch_vertical` = `0`
- `bool draw_center` = `true`
- `float expand_margin_bottom` = `0.0`
- `float expand_margin_left` = `0.0`
- `float expand_margin_right` = `0.0`
- `float expand_margin_top` = `0.0`
- `Color modulate_color` = `Color(1, 1, 1, 1)`
- `Rect2 region_rect` = `Rect2(0, 0, 0, 0)`
- `Texture2D texture`
- `float texture_margin_bottom` = `0.0`
- `float texture_margin_left` = `0.0`
- `float texture_margin_right` = `0.0`
- `float texture_margin_top` = `0.0`

**Methods**
- `float get_expand_margin(margin: Side) const`
- `float get_texture_margin(margin: Side) const`
- `void set_expand_margin(margin: Side, size: float)`
- `void set_expand_margin_all(size: float)`
- `void set_texture_margin(margin: Side, size: float)`
- `void set_texture_margin_all(size: float)`

### StyleBox
*Inherits: **Resource < RefCounted < Object** | Inherited by: StyleBoxEmpty, StyleBoxFlat, StyleBoxLine, StyleBoxTexture*

StyleBox is an abstract base class for drawing stylized boxes for UI elements. It is used for panels, buttons, LineEdit backgrounds, Tree backgrounds, etc. and also for testing a transparency mask for pointer signals. If mask test fails on a StyleBox assigned as mask to a control, clicks and motion signals will go through it to the one below.

**Properties**
- `float content_margin_bottom` = `-1.0`
- `float content_margin_left` = `-1.0`
- `float content_margin_right` = `-1.0`
- `float content_margin_top` = `-1.0`

**Methods**
- `void _draw(to_canvas_item: RID, rect: Rect2) virtual required const`
- `Rect2 _get_draw_rect(rect: Rect2) virtual const`
- `Vector2 _get_minimum_size() virtual const`
- `bool _test_mask(point: Vector2, rect: Rect2) virtual const`
- `void draw(canvas_item: RID, rect: Rect2) const`
- `float get_content_margin(margin: Side) const`
- `CanvasItem get_current_item_drawn() const`
- `float get_margin(margin: Side) const`
- `Vector2 get_minimum_size() const`
- `Vector2 get_offset() const`
- `void set_content_margin(margin: Side, offset: float)`
- `void set_content_margin_all(offset: float)`
- `bool test_mask(point: Vector2, rect: Rect2) const`

### SystemFont
*Inherits: **Font < Resource < RefCounted < Object***

SystemFont loads a font from a system font with the first matching name from font_names.

**Properties**
- `bool allow_system_fallback` = `true`
- `FontAntialiasing antialiasing` = `1`
- `bool disable_embedded_bitmaps` = `true`
- `bool font_italic` = `false`
- `PackedStringArray font_names` = `PackedStringArray()`
- `int font_stretch` = `100`
- `int font_weight` = `400`
- `bool force_autohinter` = `false`
- `bool generate_mipmaps` = `false`
- `Hinting hinting` = `1`
- `bool keep_rounding_remainders` = `true`
- `bool modulate_color_glyphs` = `false`
- `int msdf_pixel_range` = `16`
- `int msdf_size` = `48`
- `bool multichannel_signed_distance_field` = `false`
- `float oversampling` = `0.0`
- `SubpixelPositioning subpixel_positioning` = `1`

### Texture2DArrayRD
*Inherits: **TextureLayeredRD < TextureLayered < Texture < Resource < RefCounted < Object***

This texture array class allows you to use a 2D array texture created directly on the RenderingDevice as a texture for materials, meshes, etc.

### Texture2DArray
*Inherits: **ImageTextureLayered < TextureLayered < Texture < Resource < RefCounted < Object***

A Texture2DArray is different from a Texture3D: The Texture2DArray does not support trilinear interpolation between the Images, i.e. no blending. See also Cubemap and CubemapArray, which are texture arrays with specialized cubemap functions.

**Methods**
- `Resource create_placeholder() const`

### Texture2DRD
*Inherits: **Texture2D < Texture < Resource < RefCounted < Object***

This texture class allows you to use a 2D texture created directly on the RenderingDevice as a texture for materials, meshes, etc.

**Properties**
- `bool resource_local_to_scene` = `false (overrides Resource)`
- `RID texture_rd_rid`

### Texture2D
*Inherits: **Texture < Resource < RefCounted < Object** | Inherited by: AnimatedTexture, AtlasTexture, CameraTexture, CanvasTexture, CompressedTexture2D, CurveTexture, ...*

A texture works by registering an image in the video hardware, which then can be used in 3D models or 2D Sprite2D or GUI Control.

**Methods**
- `void _draw(to_canvas_item: RID, pos: Vector2, modulate: Color, transpose: bool) virtual const`
- `void _draw_rect(to_canvas_item: RID, rect: Rect2, tile: bool, modulate: Color, transpose: bool) virtual const`
- `void _draw_rect_region(to_canvas_item: RID, rect: Rect2, src_rect: Rect2, modulate: Color, transpose: bool, clip_uv: bool) virtual const`
- `int _get_height() virtual required const`
- `int _get_width() virtual required const`
- `bool _has_alpha() virtual const`
- `bool _is_pixel_opaque(x: int, y: int) virtual const`
- `Resource create_placeholder() const`
- `void draw(canvas_item: RID, position: Vector2, modulate: Color = Color(1, 1, 1, 1), transpose: bool = false) const`
- `void draw_rect(canvas_item: RID, rect: Rect2, tile: bool, modulate: Color = Color(1, 1, 1, 1), transpose: bool = false) const`
- `void draw_rect_region(canvas_item: RID, rect: Rect2, src_rect: Rect2, modulate: Color = Color(1, 1, 1, 1), transpose: bool = false, clip_uv: bool = true) const`
- `int get_height() const`
- `Image get_image() const`
- `Vector2 get_size() const`
- `int get_width() const`
- `bool has_alpha() const`

### Texture3DRD
*Inherits: **Texture3D < Texture < Resource < RefCounted < Object***

This texture class allows you to use a 3D texture created directly on the RenderingDevice as a texture for materials, meshes, etc.

**Properties**
- `RID texture_rd_rid`

### Texture3D
*Inherits: **Texture < Resource < RefCounted < Object** | Inherited by: CompressedTexture3D, ImageTexture3D, NoiseTexture3D, PlaceholderTexture3D, Texture3DRD*

Base class for ImageTexture3D and CompressedTexture3D. Cannot be used directly, but contains all the functions necessary for accessing the derived resource types. Texture3D is the base class for all 3-dimensional texture types. See also TextureLayered.

**Methods**
- `Array[Image] _get_data() virtual required const`
- `int _get_depth() virtual required const`
- `Format _get_format() virtual required const`
- `int _get_height() virtual required const`
- `int _get_width() virtual required const`
- `bool _has_mipmaps() virtual required const`
- `Resource create_placeholder() const`
- `Array[Image] get_data() const`
- `int get_depth() const`
- `Format get_format() const`
- `int get_height() const`
- `int get_width() const`
- `bool has_mipmaps() const`

### TextureCubemapArrayRD
*Inherits: **TextureLayeredRD < TextureLayered < Texture < Resource < RefCounted < Object***

This texture class allows you to use a cubemap array texture created directly on the RenderingDevice as a texture for materials, meshes, etc.

### TextureCubemapRD
*Inherits: **TextureLayeredRD < TextureLayered < Texture < Resource < RefCounted < Object***

This texture class allows you to use a cubemap texture created directly on the RenderingDevice as a texture for materials, meshes, etc.

### TextureLayeredRD
*Inherits: **TextureLayered < Texture < Resource < RefCounted < Object** | Inherited by: Texture2DArrayRD, TextureCubemapArrayRD, TextureCubemapRD*

Base class for Texture2DArrayRD, TextureCubemapRD and TextureCubemapArrayRD. Cannot be used directly, but contains all the functions necessary for accessing the derived resource types.

**Properties**
- `RID texture_rd_rid`

### TextureLayered
*Inherits: **Texture < Resource < RefCounted < Object** | Inherited by: CompressedTextureLayered, ImageTextureLayered, PlaceholderTextureLayered, TextureLayeredRD*

Base class for ImageTextureLayered and CompressedTextureLayered. Cannot be used directly, but contains all the functions necessary for accessing the derived resource types. See also Texture3D.

**Methods**
- `Format _get_format() virtual required const`
- `int _get_height() virtual required const`
- `Image _get_layer_data(layer_index: int) virtual required const`
- `int _get_layered_type() virtual required const`
- `int _get_layers() virtual required const`
- `int _get_width() virtual required const`
- `bool _has_mipmaps() virtual required const`
- `Format get_format() const`
- `int get_height() const`
- `Image get_layer_data(layer: int) const`
- `LayeredType get_layered_type() const`
- `int get_layers() const`
- `int get_width() const`
- `bool has_mipmaps() const`

### TextureProgressBar
*Inherits: **Range < Control < CanvasItem < Node < Object***

TextureProgressBar works like ProgressBar, but uses up to 3 textures instead of Godot's Theme resource. It can be used to create horizontal, vertical and radial progress bars.

**Properties**
- `int fill_mode` = `0`
- `MouseFilter mouse_filter` = `1 (overrides Control)`
- `bool nine_patch_stretch` = `false`
- `Vector2 radial_center_offset` = `Vector2(0, 0)`
- `float radial_fill_degrees` = `360.0`
- `float radial_initial_angle` = `0.0`
- `BitField[SizeFlags] size_flags_vertical` = `1 (overrides Control)`
- `float step` = `1.0 (overrides Range)`
- `int stretch_margin_bottom` = `0`
- `int stretch_margin_left` = `0`
- `int stretch_margin_right` = `0`
- `int stretch_margin_top` = `0`
- `Texture2D texture_over`
- `Texture2D texture_progress`
- `Vector2 texture_progress_offset` = `Vector2(0, 0)`
- `Texture2D texture_under`
- `Color tint_over` = `Color(1, 1, 1, 1)`
- `Color tint_progress` = `Color(1, 1, 1, 1)`
- `Color tint_under` = `Color(1, 1, 1, 1)`

**Methods**
- `int get_stretch_margin(margin: Side) const`
- `void set_stretch_margin(margin: Side, value: int)`

### Texture
*Inherits: **Resource < RefCounted < Object** | Inherited by: Texture2D, Texture3D, TextureLayered*

Texture is the base class for all texture types. Common texture types are Texture2D and ImageTexture. See also Image.

### TileData
*Inherits: **Object***

TileData object represents a single tile in a TileSet. It is usually edited using the tileset editor, but it can be modified at runtime using TileMapLayer._tile_data_runtime_update().

**Properties**
- `bool flip_h` = `false`
- `bool flip_v` = `false`
- `Material material`
- `Color modulate` = `Color(1, 1, 1, 1)`
- `float probability` = `1.0`
- `int terrain` = `-1`
- `int terrain_set` = `-1`
- `Vector2i texture_origin` = `Vector2i(0, 0)`
- `bool transpose` = `false`
- `int y_sort_origin` = `0`
- `int z_index` = `0`

**Methods**
- `void add_collision_polygon(layer_id: int)`
- `void add_occluder_polygon(layer_id: int)`
- `float get_collision_polygon_one_way_margin(layer_id: int, polygon_index: int) const`
- `PackedVector2Array get_collision_polygon_points(layer_id: int, polygon_index: int) const`
- `int get_collision_polygons_count(layer_id: int) const`
- `float get_constant_angular_velocity(layer_id: int) const`
- `Vector2 get_constant_linear_velocity(layer_id: int) const`
- `Variant get_custom_data(layer_name: String) const`
- `Variant get_custom_data_by_layer_id(layer_id: int) const`
- `NavigationPolygon get_navigation_polygon(layer_id: int, flip_h: bool = false, flip_v: bool = false, transpose: bool = false) const`
- `OccluderPolygon2D get_occluder(layer_id: int, flip_h: bool = false, flip_v: bool = false, transpose: bool = false) const`
- `OccluderPolygon2D get_occluder_polygon(layer_id: int, polygon_index: int, flip_h: bool = false, flip_v: bool = false, transpose: bool = false) const`
- `int get_occluder_polygons_count(layer_id: int) const`
- `int get_terrain_peering_bit(peering_bit: CellNeighbor) const`
- `bool has_custom_data(layer_name: String) const`
- `bool is_collision_polygon_one_way(layer_id: int, polygon_index: int) const`
- `bool is_valid_terrain_peering_bit(peering_bit: CellNeighbor) const`
- `void remove_collision_polygon(layer_id: int, polygon_index: int)`
- `void remove_occluder_polygon(layer_id: int, polygon_index: int)`
- `void set_collision_polygon_one_way(layer_id: int, polygon_index: int, one_way: bool)`
- `void set_collision_polygon_one_way_margin(layer_id: int, polygon_index: int, one_way_margin: float)`
- `void set_collision_polygon_points(layer_id: int, polygon_index: int, polygon: PackedVector2Array)`
- `void set_collision_polygons_count(layer_id: int, polygons_count: int)`
- `void set_constant_angular_velocity(layer_id: int, velocity: float)`
- `void set_constant_linear_velocity(layer_id: int, velocity: Vector2)`
- `void set_custom_data(layer_name: String, value: Variant)`
- `void set_custom_data_by_layer_id(layer_id: int, value: Variant)`
- `void set_navigation_polygon(layer_id: int, navigation_polygon: NavigationPolygon)`
- `void set_occluder(layer_id: int, occluder_polygon: OccluderPolygon2D)`
- `void set_occluder_polygon(layer_id: int, polygon_index: int, polygon: OccluderPolygon2D)`
- `void set_occluder_polygons_count(layer_id: int, polygons_count: int)`
- `void set_terrain_peering_bit(peering_bit: CellNeighbor, terrain: int)`

### TileSetAtlasSource
*Inherits: **TileSetSource < Resource < RefCounted < Object***

An atlas is a grid of tiles laid out on a texture. Each tile in the grid must be exposed using create_tile(). Those tiles are then indexed using their coordinates in the grid.

**Properties**
- `Vector2i margins` = `Vector2i(0, 0)`
- `Vector2i separation` = `Vector2i(0, 0)`
- `Texture2D texture`
- `Vector2i texture_region_size` = `Vector2i(16, 16)`
- `bool use_texture_padding` = `true`

**Methods**
- `void clear_tiles_outside_texture()`
- `int create_alternative_tile(atlas_coords: Vector2i, alternative_id_override: int = -1)`
- `void create_tile(atlas_coords: Vector2i, size: Vector2i = Vector2i(1, 1))`
- `Vector2i get_atlas_grid_size() const`
- `int get_next_alternative_tile_id(atlas_coords: Vector2i) const`
- `Texture2D get_runtime_texture() const`
- `Rect2i get_runtime_tile_texture_region(atlas_coords: Vector2i, frame: int) const`
- `int get_tile_animation_columns(atlas_coords: Vector2i) const`
- `float get_tile_animation_frame_duration(atlas_coords: Vector2i, frame_index: int) const`
- `int get_tile_animation_frames_count(atlas_coords: Vector2i) const`
- `TileAnimationMode get_tile_animation_mode(atlas_coords: Vector2i) const`
- `Vector2i get_tile_animation_separation(atlas_coords: Vector2i) const`
- `float get_tile_animation_speed(atlas_coords: Vector2i) const`
- `float get_tile_animation_total_duration(atlas_coords: Vector2i) const`
- `Vector2i get_tile_at_coords(atlas_coords: Vector2i) const`
- `TileData get_tile_data(atlas_coords: Vector2i, alternative_tile: int) const`
- `Vector2i get_tile_size_in_atlas(atlas_coords: Vector2i) const`
- `Rect2i get_tile_texture_region(atlas_coords: Vector2i, frame: int = 0) const`
- `PackedVector2Array get_tiles_to_be_removed_on_change(texture: Texture2D, margins: Vector2i, separation: Vector2i, texture_region_size: Vector2i)`
- `bool has_room_for_tile(atlas_coords: Vector2i, size: Vector2i, animation_columns: int, animation_separation: Vector2i, frames_count: int, ignored_tile: Vector2i = Vector2i(-1, -1)) const`
- `bool has_tiles_outside_texture() const`
- `void move_tile_in_atlas(atlas_coords: Vector2i, new_atlas_coords: Vector2i = Vector2i(-1, -1), new_size: Vector2i = Vector2i(-1, -1))`
- `void remove_alternative_tile(atlas_coords: Vector2i, alternative_tile: int)`
- `void remove_tile(atlas_coords: Vector2i)`
- `void set_alternative_tile_id(atlas_coords: Vector2i, alternative_tile: int, new_id: int)`
- `void set_tile_animation_columns(atlas_coords: Vector2i, frame_columns: int)`
- `void set_tile_animation_frame_duration(atlas_coords: Vector2i, frame_index: int, duration: float)`
- `void set_tile_animation_frames_count(atlas_coords: Vector2i, frames_count: int)`
- `void set_tile_animation_mode(atlas_coords: Vector2i, mode: TileAnimationMode)`
- `void set_tile_animation_separation(atlas_coords: Vector2i, separation: Vector2i)`
- `void set_tile_animation_speed(atlas_coords: Vector2i, speed: float)`

**GDScript Examples**
```gdscript
var alternate_id = $TileMapLayer.get_cell_alternative_tile(Vector2i(2, 2))
if not alternate_id & TileSetAtlasSource.TRANSFORM_FLIP_H:
    # If tile is not already flipped, flip it.
    $TileMapLayer.set_cell(Vector2i(2, 2), source_id, atlas_coords, alternate_id | TileSetAtlasSource.TRANSFORM_FLIP_H)
```
```gdscript
enum TileTransform {
    ROTATE_0 = 0,
    ROTATE_90 = TileSetAtlasSource.TRANSFORM_TRANSPOSE | TileSetAtlasSource.TRANSFORM_FLIP_H,
    ROTATE_180 = TileSetAtlasSource.TRANSFORM_FLIP_H | TileSetAtlasSource.TRANSFORM_FLIP_V,
    ROTATE_270 = TileSetAtlasSource.TRANSFORM_TRANSPOSE | TileSetAtlasSource.TRANSFORM_FLIP_V,
}
```

### TileSetScenesCollectionSource
*Inherits: **TileSetSource < Resource < RefCounted < Object***

When placed on a TileMapLayer, tiles from TileSetScenesCollectionSource will automatically instantiate an associated scene at the cell's position in the TileMapLayer.

**Methods**
- `int create_scene_tile(packed_scene: PackedScene, id_override: int = -1)`
- `int get_next_scene_tile_id() const`
- `bool get_scene_tile_display_placeholder(id: int) const`
- `int get_scene_tile_id(index: int)`
- `PackedScene get_scene_tile_scene(id: int) const`
- `int get_scene_tiles_count()`
- `bool has_scene_tile_id(id: int)`
- `void remove_scene_tile(id: int)`
- `void set_scene_tile_display_placeholder(id: int, display_placeholder: bool)`
- `void set_scene_tile_id(id: int, new_id: int)`
- `void set_scene_tile_scene(id: int, packed_scene: PackedScene)`

**GDScript Examples**
```gdscript
var source_id = tile_map_layer.get_cell_source_id(Vector2i(x, y))
if source_id > -1:
    var scene_source = tile_map_layer.tile_set.get_source(source_id)
    if scene_source is TileSetScenesCollectionSource:
        var alt_id = tile_map_layer.get_cell_alternative_tile(Vector2i(x, y))
        # The assigned PackedScene.
        var scene = scene_source.get_scene_tile_scene(alt_id)
```

### TileSetSource
*Inherits: **Resource < RefCounted < Object** | Inherited by: TileSetAtlasSource, TileSetScenesCollectionSource*

Exposes a set of tiles for a TileSet resource.

**Methods**
- `int get_alternative_tile_id(atlas_coords: Vector2i, index: int) const`
- `int get_alternative_tiles_count(atlas_coords: Vector2i) const`
- `Vector2i get_tile_id(index: int) const`
- `int get_tiles_count() const`
- `bool has_alternative_tile(atlas_coords: Vector2i, alternative_tile: int) const`
- `bool has_tile(atlas_coords: Vector2i) const`

### TileSet
*Inherits: **Resource < RefCounted < Object***

A TileSet is a library of tiles for a TileMapLayer. A TileSet handles a list of TileSetSource, each of them storing a set of tiles.

**Properties**
- `TileLayout tile_layout` = `0`
- `TileOffsetAxis tile_offset_axis` = `0`
- `TileShape tile_shape` = `0`
- `Vector2i tile_size` = `Vector2i(16, 16)`
- `bool uv_clipping` = `false`

**Methods**
- `void add_custom_data_layer(to_position: int = -1)`
- `void add_navigation_layer(to_position: int = -1)`
- `void add_occlusion_layer(to_position: int = -1)`
- `int add_pattern(pattern: TileMapPattern, index: int = -1)`
- `void add_physics_layer(to_position: int = -1)`
- `int add_source(source: TileSetSource, atlas_source_id_override: int = -1)`
- `void add_terrain(terrain_set: int, to_position: int = -1)`
- `void add_terrain_set(to_position: int = -1)`
- `void cleanup_invalid_tile_proxies()`
- `void clear_tile_proxies()`
- `Array get_alternative_level_tile_proxy(source_from: int, coords_from: Vector2i, alternative_from: int)`
- `Array get_coords_level_tile_proxy(source_from: int, coords_from: Vector2i)`
- `int get_custom_data_layer_by_name(layer_name: String) const`
- `String get_custom_data_layer_name(layer_index: int) const`
- `Variant.Type get_custom_data_layer_type(layer_index: int) const`
- `int get_custom_data_layers_count() const`
- `bool get_navigation_layer_layer_value(layer_index: int, layer_number: int) const`
- `int get_navigation_layer_layers(layer_index: int) const`
- `int get_navigation_layers_count() const`
- `int get_next_source_id() const`
- `int get_occlusion_layer_light_mask(layer_index: int) const`
- `bool get_occlusion_layer_sdf_collision(layer_index: int) const`
- `int get_occlusion_layers_count() const`
- `TileMapPattern get_pattern(index: int = -1)`
- `int get_patterns_count()`
- `int get_physics_layer_collision_layer(layer_index: int) const`
- `int get_physics_layer_collision_mask(layer_index: int) const`
- `float get_physics_layer_collision_priority(layer_index: int) const`
- `PhysicsMaterial get_physics_layer_physics_material(layer_index: int) const`
- `int get_physics_layers_count() const`
- `TileSetSource get_source(source_id: int) const`
- `int get_source_count() const`
- `int get_source_id(index: int) const`
- `int get_source_level_tile_proxy(source_from: int)`
- `Color get_terrain_color(terrain_set: int, terrain_index: int) const`
- `String get_terrain_name(terrain_set: int, terrain_index: int) const`
- `TerrainMode get_terrain_set_mode(terrain_set: int) const`
- `int get_terrain_sets_count() const`
- `int get_terrains_count(terrain_set: int) const`
- `bool has_alternative_level_tile_proxy(source_from: int, coords_from: Vector2i, alternative_from: int)`
