# Godot 4 GDScript API Reference — Core

> GDScript-only reference. 39 classes.

### ClassDB
*Inherits: **Object***

Provides access to metadata stored for every available engine class.

**Methods**
- `bool can_instantiate(class: StringName) const`
- `Variant class_call_static(class: StringName, method: StringName, ...) vararg`
- `bool class_exists(class: StringName) const`
- `APIType class_get_api_type(class: StringName) const`
- `PackedStringArray class_get_enum_constants(class: StringName, enum: StringName, no_inheritance: bool = false) const`
- `PackedStringArray class_get_enum_list(class: StringName, no_inheritance: bool = false) const`
- `int class_get_integer_constant(class: StringName, name: StringName) const`
- `StringName class_get_integer_constant_enum(class: StringName, name: StringName, no_inheritance: bool = false) const`
- `PackedStringArray class_get_integer_constant_list(class: StringName, no_inheritance: bool = false) const`
- `int class_get_method_argument_count(class: StringName, method: StringName, no_inheritance: bool = false) const`
- `Array[Dictionary] class_get_method_list(class: StringName, no_inheritance: bool = false) const`
- `Variant class_get_property(object: Object, property: StringName) const`
- `Variant class_get_property_default_value(class: StringName, property: StringName) const`
- `StringName class_get_property_getter(class: StringName, property: StringName)`
- `Array[Dictionary] class_get_property_list(class: StringName, no_inheritance: bool = false) const`
- `StringName class_get_property_setter(class: StringName, property: StringName)`
- `Dictionary class_get_signal(class: StringName, signal: StringName) const`
- `Array[Dictionary] class_get_signal_list(class: StringName, no_inheritance: bool = false) const`
- `bool class_has_enum(class: StringName, name: StringName, no_inheritance: bool = false) const`
- `bool class_has_integer_constant(class: StringName, name: StringName) const`
- `bool class_has_method(class: StringName, method: StringName, no_inheritance: bool = false) const`
- `bool class_has_signal(class: StringName, signal: StringName) const`
- `Error class_set_property(object: Object, property: StringName, value: Variant) const`
- `PackedStringArray get_class_list() const`
- `PackedStringArray get_inheriters_from_class(class: StringName) const`
- `StringName get_parent_class(class: StringName) const`
- `Variant instantiate(class: StringName) const`
- `bool is_class_enabled(class: StringName) const`
- `bool is_class_enum_bitfield(class: StringName, enum: StringName, no_inheritance: bool = false) const`
- `bool is_parent_class(class: StringName, inherits: StringName) const`

### EngineDebugger
*Inherits: **Object***

EngineDebugger handles the communication between the editor and the running game. It is active in the running game. Messages can be sent/received through it. It also manages the profilers.

**Methods**
- `void clear_breakpoints()`
- `void debug(can_continue: bool = true, is_error_breakpoint: bool = false)`
- `int get_depth() const`
- `int get_lines_left() const`
- `bool has_capture(name: StringName)`
- `bool has_profiler(name: StringName)`
- `void insert_breakpoint(line: int, source: StringName)`
- `bool is_active()`
- `bool is_breakpoint(line: int, source: StringName) const`
- `bool is_profiling(name: StringName)`
- `bool is_skipping_breakpoints() const`
- `void line_poll()`
- `void profiler_add_frame_data(name: StringName, data: Array)`
- `void profiler_enable(name: StringName, enable: bool, arguments: Array = [])`
- `void register_message_capture(name: StringName, callable: Callable)`
- `void register_profiler(name: StringName, profiler: EngineProfiler)`
- `void remove_breakpoint(line: int, source: StringName)`
- `void script_debug(language: ScriptLanguage, can_continue: bool = true, is_error_breakpoint: bool = false)`
- `void send_message(message: String, data: Array)`
- `void set_depth(depth: int)`
- `void set_lines_left(lines: int)`
- `void unregister_message_capture(name: StringName)`
- `void unregister_profiler(name: StringName)`

### EngineProfiler
*Inherits: **RefCounted < Object***

This class can be used to implement custom profilers that are able to interact with the engine and editor debugger.

**Methods**
- `void _add_frame(data: Array) virtual`
- `void _tick(frame_time: float, process_time: float, physics_time: float, physics_frame_time: float) virtual`
- `void _toggle(enable: bool, options: Array) virtual`

### Engine
*Inherits: **Object***

The Engine singleton allows you to query and modify the project's run-time parameters, such as frames per second, time scale, and others. It also stores information about the current build of Godot, such as the current version.

**Properties**
- `int max_fps` = `0`
- `int max_physics_steps_per_frame` = `8`
- `float physics_jitter_fix` = `0.5`
- `int physics_ticks_per_second` = `60`
- `bool print_error_messages` = `true`
- `bool print_to_stdout` = `true`
- `float time_scale` = `1.0`

**Methods**
- `Array[ScriptBacktrace] capture_script_backtraces(include_variables: bool = false) const`
- `String get_architecture_name() const`
- `Dictionary get_author_info() const`
- `Array[Dictionary] get_copyright_info() const`
- `Dictionary get_donor_info() const`
- `int get_frames_drawn()`
- `float get_frames_per_second() const`
- `Dictionary get_license_info() const`
- `String get_license_text() const`
- `MainLoop get_main_loop() const`
- `int get_physics_frames() const`
- `float get_physics_interpolation_fraction() const`
- `int get_process_frames() const`
- `ScriptLanguage get_script_language(index: int) const`
- `int get_script_language_count()`
- `Object get_singleton(name: StringName) const`
- `PackedStringArray get_singleton_list() const`
- `Dictionary get_version_info() const`
- `String get_write_movie_path() const`
- `bool has_singleton(name: StringName) const`
- `bool is_editor_hint() const`
- `bool is_embedded_in_editor() const`
- `bool is_in_physics_frame() const`
- `Error register_script_language(language: ScriptLanguage)`
- `void register_singleton(name: StringName, instance: Object)`
- `Error unregister_script_language(language: ScriptLanguage)`
- `void unregister_singleton(name: StringName)`

**GDScript Examples**
```gdscript
func _physics_process(_delta):
    if Engine.get_physics_frames() % 2 == 0:
        pass # Run expensive logic only once every 2 physics frames here.
```
```gdscript
func _process(_delta):
    if Engine.get_process_frames() % 5 == 0:
        pass # Run expensive logic only once every 5 process (render) frames here.
```

### MainLoop
*Inherits: **Object** | Inherited by: SceneTree*

MainLoop is the abstract base class for a Godot project's game loop. It is inherited by SceneTree, which is the default game loop implementation used in Godot projects, though it is also possible to write and use one's own MainLoop subclass instead of the scene tree.

**Methods**
- `void _finalize() virtual`
- `void _initialize() virtual`
- `bool _physics_process(delta: float) virtual`
- `bool _process(delta: float) virtual`

**GDScript Examples**
```gdscript
class_name CustomMainLoop
extends MainLoop

var time_elapsed = 0

func _initialize():
    print("Initialized:")
    print("  Starting time: %s" % str(time_elapsed))

func _process(delta):
    time_elapsed += delta
    # Return true to end the main loop.
    return Input.get_mouse_button_mask() != 0 || Input.is_key_pressed(KEY_ESCAPE)

func _finalize():
    print("Finalized:")
    print("  End time: %s" % str(time_elapsed))
```

### Marshalls
*Inherits: **Object***

Provides data transformation and encoding utility functions.

**Methods**
- `PackedByteArray base64_to_raw(base64_str: String)`
- `String base64_to_utf8(base64_str: String)`
- `Variant base64_to_variant(base64_str: String, allow_objects: bool = false)`
- `String raw_to_base64(array: PackedByteArray)`
- `String utf8_to_base64(utf8_str: String)`
- `String variant_to_base64(variant: Variant, full_objects: bool = false)`

### Object
*Inherited by: AudioServer, CameraServer, ClassDB, DisplayServer, EditorFileSystemDirectory, EditorInterface, ...*

An advanced Variant type. All classes in the engine inherit from Object. Each class may define new properties, methods or signals, which are available to all inheriting classes. For example, a Sprite2D instance is able to call Node.add_child() because it inherits from Node.

**Methods**
- `Variant _get(property: StringName) virtual`
- `Array[Dictionary] _get_property_list() virtual`
- `void _init() virtual`
- `Variant _iter_get(iter: Variant) virtual`
- `bool _iter_init(iter: Array) virtual`
- `bool _iter_next(iter: Array) virtual`
- `void _notification(what: int) virtual`
- `bool _property_can_revert(property: StringName) virtual`
- `Variant _property_get_revert(property: StringName) virtual`
- `bool _set(property: StringName, value: Variant) virtual`
- `String _to_string() virtual`
- `void _validate_property(property: Dictionary) virtual`
- `void add_user_signal(signal: String, arguments: Array = [])`
- `Variant call(method: StringName, ...) vararg`
- `Variant call_deferred(method: StringName, ...) vararg`
- `Variant callv(method: StringName, arg_array: Array)`
- `bool can_translate_messages() const`
- `void cancel_free()`
- `Error connect(signal: StringName, callable: Callable, flags: int = 0)`
- `void disconnect(signal: StringName, callable: Callable)`
- `Error emit_signal(signal: StringName, ...) vararg`
- `void free()`
- `Variant get(property: StringName) const`
- `String get_class() const`
- `Array[Dictionary] get_incoming_connections() const`
- `Variant get_indexed(property_path: NodePath) const`
- `int get_instance_id() const`
- `Variant get_meta(name: StringName, default: Variant = null) const`
- `Array[StringName] get_meta_list() const`
- `int get_method_argument_count(method: StringName) const`
- `Array[Dictionary] get_method_list() const`
- `Array[Dictionary] get_property_list() const`
- `Variant get_script() const`
- `Array[Dictionary] get_signal_connection_list(signal: StringName) const`
- `Array[Dictionary] get_signal_list() const`
- `StringName get_translation_domain() const`
- `bool has_connections(signal: StringName) const`
- `bool has_meta(name: StringName) const`
- `bool has_method(method: StringName) const`
- `bool has_signal(signal: StringName) const`

**GDScript Examples**
```gdscript
func _get(property):
    if property == "fake_property":
        print("Getting my property!")
        return 4

func _get_property_list():
    return [
        { "name": "fake_property", "type": TYPE_INT }
    ]
```
```gdscript
@tool
extends Node

@export var number_count = 3:
    set(nc):
        number_count = nc
        numbers.resize(number_count)
        notify_property_list_changed()

var numbers = PackedInt32Array([0, 0, 0])

func _get_property_list():
    var properties = []

    for i in range(number_count):
        properties.append({
            "name": "number_%d" % i,
            "type": TYPE_INT,
            "hint": PROPERTY_HINT_ENUM,
            "hint_string": "ZERO,ONE,TWO,THREE,FOUR,FIVE",
        })

    return properties

func _get(property):
    if property.begins_with("number_"):
        var ind
# ...
```

### Performance
*Inherits: **Object***

This class provides access to a number of different monitors related to performance, such as memory usage, draw calls, and FPS. These are the same as the values displayed in the Monitor tab in the editor's Debugger panel. By using the get_monitor() method of this class, you can access this data from your code.

**Methods**
- `void add_custom_monitor(id: StringName, callable: Callable, arguments: Array = [], type: MonitorType = 0)`
- `Variant get_custom_monitor(id: StringName)`
- `Array[StringName] get_custom_monitor_names()`
- `PackedInt32Array get_custom_monitor_types()`
- `float get_monitor(monitor: Monitor) const`
- `int get_monitor_modification_time()`
- `bool has_custom_monitor(id: StringName)`
- `void remove_custom_monitor(id: StringName)`

**GDScript Examples**
```gdscript
func _ready():
    var monitor_value = Callable(self, "get_monitor_value")

    # Adds monitor with name "MyName" to category "MyCategory".
    Performance.add_custom_monitor("MyCategory/MyMonitor", monitor_value)

    # Adds monitor with name "MyName" to category "Custom".
    # Note: "MyCategory/MyMonitor" and "MyMonitor" have same name but different IDs, so the code is valid.
    Performance.add_custom_monitor("MyMonitor", monitor_value)

    # Adds monitor with name "MyName" to category "Custom".
    # Note: "MyMonitor" and "Custom/MyMonitor" have same name and same category but different
# ...
```
```gdscript
print(Performance.get_monitor(Performance.TIME_FPS)) # Prints the FPS to the console.
```

### RefCounted
*Inherits: **Object** | Inherited by: AESContext, AStar2D, AStar3D, AStarGrid2D, AudioEffectInstance, AudioSample, ...*

Base class for any object that keeps a reference count. Resource and many other helper objects inherit this class.

**Methods**
- `int get_reference_count() const`
- `bool init_ref()`
- `bool reference()`
- `bool unreference()`

### ResourceFormatLoader
*Inherits: **RefCounted < Object***

Godot loads resources in the editor or in exported games using ResourceFormatLoaders. They are queried automatically via the ResourceLoader singleton, or when a resource with internal dependencies is loaded. Each file type may load as a different resource type, so multiple ResourceFormatLoaders are registered in the engine.

**Methods**
- `bool _exists(path: String) virtual const`
- `PackedStringArray _get_classes_used(path: String) virtual const`
- `PackedStringArray _get_dependencies(path: String, add_types: bool) virtual const`
- `PackedStringArray _get_recognized_extensions() virtual const`
- `String _get_resource_script_class(path: String) virtual const`
- `String _get_resource_type(path: String) virtual const`
- `int _get_resource_uid(path: String) virtual const`
- `bool _handles_type(type: StringName) virtual const`
- `Variant _load(path: String, original_path: String, use_sub_threads: bool, cache_mode: int) virtual required const`
- `bool _recognize_path(path: String, type: StringName) virtual const`
- `Error _rename_dependencies(path: String, renames: Dictionary) virtual const`

**GDScript Examples**
```gdscript
func _get_dependencies(path, add_types):
    return [
        "uid://fqgvuwrkuixh::Script::res://script.gd",
        "uid://fqgvuwrkuixh::::res://script.gd",
        "res://script.gd::Script",
        "res://script.gd",
    ]
```

### ResourceFormatSaver
*Inherits: **RefCounted < Object***

The engine can save resources when you do it from the editor, or when you use the ResourceSaver singleton. This is accomplished thanks to multiple ResourceFormatSavers, each handling its own format and called automatically by the engine.

**Methods**
- `PackedStringArray _get_recognized_extensions(resource: Resource) virtual const`
- `bool _recognize(resource: Resource) virtual const`
- `bool _recognize_path(resource: Resource, path: String) virtual const`
- `Error _save(resource: Resource, path: String, flags: int) virtual`
- `Error _set_uid(path: String, uid: int) virtual`

### ResourceImporterBMFont
*Inherits: **ResourceImporter < RefCounted < Object***

The BMFont format is a format created by the BMFont program. Many BMFont-compatible programs also exist, like BMGlyph.

**Properties**
- `bool compress` = `true`
- `Array fallbacks` = `[]`
- `int scaling_mode` = `2`

### ResourceImporterBitMap
*Inherits: **ResourceImporter < RefCounted < Object***

BitMap resources are typically used as click masks in TextureButton and TouchScreenButton.

**Properties**
- `int create_from` = `0`
- `float threshold` = `0.5`

### ResourceImporterCSVTranslation
*Inherits: **ResourceImporter < RefCounted < Object***

Comma-separated values are a plain text table storage format. The format's simplicity makes it easy to edit in any text editor or spreadsheet software. This makes it a common choice for game localization.

**Properties**
- `int compress` = `1`
- `int delimiter` = `0`
- `bool unescape_keys` = `false`
- `bool unescape_translations` = `true`

### ResourceImporterDynamicFont
*Inherits: **ResourceImporter < RefCounted < Object***

Unlike bitmap fonts, dynamic fonts can be resized to any size and still look crisp. Dynamic fonts also optionally support MSDF font rendering, which allows for run-time scale changes with no re-rasterization cost.

**Properties**
- `bool allow_system_fallback` = `true`
- `int antialiasing` = `1`
- `bool compress` = `true`
- `bool disable_embedded_bitmaps` = `true`
- `Array fallbacks` = `[]`
- `bool force_autohinter` = `false`
- `bool generate_mipmaps` = `false`
- `int hinting` = `1`
- `bool keep_rounding_remainders` = `true`
- `Dictionary language_support` = `{}`
- `bool modulate_color_glyphs` = `false`
- `int msdf_pixel_range` = `8`
- `int msdf_size` = `48`
- `bool multichannel_signed_distance_field` = `false`
- `Dictionary opentype_features` = `{}`
- `float oversampling` = `0.0`
- `Array preload` = `[]`
- `Dictionary script_support` = `{}`
- `int subpixel_positioning` = `4`

### ResourceImporterImageFont
*Inherits: **ResourceImporter < RefCounted < Object***

This image-based workflow can be easier to use than ResourceImporterBMFont, but it requires all glyphs to have the same width and height, glyph advances and drawing offsets can be customized. This makes ResourceImporterImageFont most suited to fixed-width fonts.

**Properties**
- `int ascent` = `0`
- `Rect2i character_margin` = `Rect2i(0, 0, 0, 0)`
- `PackedStringArray character_ranges` = `PackedStringArray()`
- `int columns` = `1`
- `bool compress` = `true`
- `int descent` = `0`
- `Array fallbacks` = `[]`
- `Rect2i image_margin` = `Rect2i(0, 0, 0, 0)`
- `PackedStringArray kerning_pairs` = `PackedStringArray()`
- `int rows` = `1`
- `int scaling_mode` = `2`

### ResourceImporterImage
*Inherits: **ResourceImporter < RefCounted < Object***

This importer imports Image resources, as opposed to CompressedTexture2D. If you need to render the image in 2D or 3D, use ResourceImporterTexture instead.

### ResourceImporterLayeredTexture
*Inherits: **ResourceImporter < RefCounted < Object***

This imports a 3-dimensional texture, which can then be used in custom shaders, as a FogMaterial density map or as a GPUParticlesAttractorVectorField3D. See also ResourceImporterTexture and ResourceImporterTextureAtlas.

**Properties**
- `int compress/channel_pack` = `0`
- `int compress/hdr_compression` = `1`
- `bool compress/high_quality` = `false`
- `float compress/lossy_quality` = `0.7`
- `int compress/mode` = `1`
- `float compress/rdo_quality_loss` = `0.0`
- `int compress/uastc_level` = `0`
- `bool mipmaps/generate` = `true`
- `int mipmaps/limit` = `-1`
- `int slices/arrangement` = `1`

### ResourceImporterMP3
*Inherits: **ResourceImporter < RefCounted < Object***

MP3 is a lossy audio format, with worse audio quality compared to ResourceImporterOggVorbis at a given bitrate.

**Properties**
- `int bar_beats` = `4`
- `int beat_count` = `0`
- `float bpm` = `0`
- `bool loop` = `false`
- `float loop_offset` = `0`

### ResourceImporterOBJ
*Inherits: **ResourceImporter < RefCounted < Object***

Unlike ResourceImporterScene, ResourceImporterOBJ will import a single Mesh resource by default instead of importing a PackedScene. This makes it easier to use the Mesh resource in nodes that expect direct Mesh resources, such as GridMap, GPUParticles3D or CPUParticles3D. Note that it is still possible to save mesh resources from 3D scenes using the Advanced Import Settings dialog, regardless of the source format.

**Properties**
- `bool force_disable_mesh_compression` = `false`
- `bool generate_lightmap_uv2` = `false`
- `float generate_lightmap_uv2_texel_size` = `0.2`
- `bool generate_lods` = `true`
- `bool generate_shadow_mesh` = `true`
- `bool generate_tangents` = `true`
- `Vector3 offset_mesh` = `Vector3(0, 0, 0)`
- `Vector3 scale_mesh` = `Vector3(1, 1, 1)`

### ResourceImporterOggVorbis
*Inherits: **ResourceImporter < RefCounted < Object***

Ogg Vorbis is a lossy audio format, with better audio quality compared to ResourceImporterMP3 at a given bitrate.

**Properties**
- `int bar_beats` = `4`
- `int beat_count` = `0`
- `float bpm` = `0`
- `bool loop` = `false`
- `float loop_offset` = `0`

**Methods**
- `AudioStreamOggVorbis load_from_buffer(stream_data: PackedByteArray) static`
- `AudioStreamOggVorbis load_from_file(path: String) static`

### ResourceImporterSVG
*Inherits: **ResourceImporter < RefCounted < Object***

This importer imports DPITexture resources. See also ResourceImporterTexture and ResourceImporterImage.

**Properties**
- `float base_scale` = `1.0`
- `Dictionary color_map` = `{}`
- `bool compress` = `true`
- `float saturation` = `1.0`

### ResourceImporterScene
*Inherits: **ResourceImporter < RefCounted < Object***

See also ResourceImporterOBJ, which is used for OBJ models that can be imported as an independent Mesh or a scene.

**Properties**
- `Dictionary _subresources` = `{}`
- `float animation/fps` = `30`
- `bool animation/import` = `true`
- `bool animation/import_rest_as_RESET` = `false`
- `bool animation/remove_immutable_tracks` = `true`
- `bool animation/trimming` = `false`
- `String import_script/path` = `""`
- `int materials/extract` = `0`
- `int materials/extract_format` = `0`
- `String materials/extract_path` = `""`
- `bool meshes/create_shadow_meshes` = `true`
- `bool meshes/ensure_tangents` = `true`
- `bool meshes/force_disable_compression` = `false`
- `bool meshes/generate_lods` = `true`
- `int meshes/light_baking` = `1`
- `float meshes/lightmap_texel_size` = `0.2`
- `bool nodes/apply_root_scale` = `true`
- `bool nodes/import_as_skeleton_bones` = `false`
- `String nodes/root_name` = `""`
- `float nodes/root_scale` = `1.0`
- `Script nodes/root_script` = `null`
- `String nodes/root_type` = `""`
- `bool nodes/use_name_suffixes` = `true`
- `bool nodes/use_node_type_suffixes` = `true`
- `bool skins/use_named_skins` = `true`

### ResourceImporterShaderFile
*Inherits: **ResourceImporter < RefCounted < Object***

This imports native GLSL shaders as RDShaderFile resources, for use with low-level RenderingDevice operations. This importer does not handle .gdshader files.

### ResourceImporterTextureAtlas
*Inherits: **ResourceImporter < RefCounted < Object***

This imports a collection of textures from a PNG image into an AtlasTexture or 2D ArrayMesh. This can be used to save memory when importing 2D animations from spritesheets. Texture atlases are only supported in 2D rendering, not 3D. See also ResourceImporterTexture and ResourceImporterLayeredTexture.

**Properties**
- `String atlas_file` = `""`
- `bool crop_to_region` = `false`
- `int import_mode` = `0`
- `bool trim_alpha_border_from_region` = `true`

### ResourceImporterTexture
*Inherits: **ResourceImporter < RefCounted < Object***

This importer imports CompressedTexture2D resources. If you need to process the image in scripts in a more convenient way, use ResourceImporterImage instead. See also ResourceImporterLayeredTexture.

**Properties**
- `int compress/channel_pack` = `0`
- `int compress/hdr_compression` = `1`
- `bool compress/high_quality` = `false`
- `float compress/lossy_quality` = `0.7`
- `int compress/mode` = `0`
- `int compress/normal_map` = `0`
- `float compress/rdo_quality_loss` = `0.0`
- `int compress/uastc_level` = `0`
- `int detect_3d/compress_to` = `1`
- `bool editor/convert_colors_with_editor_theme` = `false`
- `bool editor/scale_with_editor_scale` = `false`
- `bool mipmaps/generate` = `false`
- `int mipmaps/limit` = `-1`
- `int process/channel_remap/alpha` = `3`
- `int process/channel_remap/blue` = `2`
- `int process/channel_remap/green` = `1`
- `int process/channel_remap/red` = `0`
- `bool process/fix_alpha_border` = `true`
- `bool process/hdr_as_srgb` = `false`
- `bool process/hdr_clamp_exposure` = `false`
- `bool process/normal_map_invert_y` = `false`
- `bool process/premult_alpha` = `false`
- `int process/size_limit` = `0`
- `int roughness/mode` = `0`
- `String roughness/src_normal` = `""`
- `float svg/scale` = `1.0`

### ResourceImporterWAV
*Inherits: **ResourceImporter < RefCounted < Object***

WAV is an uncompressed format, which can provide higher quality compared to Ogg Vorbis and MP3. It also has the lowest CPU cost to decode. This means high numbers of WAV sounds can be played at the same time, even on low-end devices.

**Properties**
- `int compress/mode` = `2`
- `int edit/loop_begin` = `0`
- `int edit/loop_end` = `-1`
- `int edit/loop_mode` = `0`
- `bool edit/normalize` = `false`
- `bool edit/trim` = `false`
- `bool force/8_bit` = `false`
- `bool force/max_rate` = `false`
- `float force/max_rate_hz` = `44100`
- `bool force/mono` = `false`

### ResourceImporter
*Inherits: **RefCounted < Object** | Inherited by: EditorImportPlugin, ResourceImporterBitMap, ResourceImporterBMFont, ResourceImporterCSVTranslation, ResourceImporterDynamicFont, ResourceImporterImage, ...*

This is the base class for Godot's resource importers. To implement your own resource importers using editor plugins, see EditorImportPlugin.

**Methods**
- `PackedStringArray _get_build_dependencies(path: String) virtual const`

**GDScript Examples**
```gdscript
func _get_build_dependencies(path):
    var resource = load(path)
    var dependencies = PackedStringArray()

    if resource.multichannel_signed_distance_field:
        dependencies.push_back("module_msdfgen_enabled")

    return dependencies
```

### ResourceLoader
*Inherits: **Object***

A singleton used to load resource files from the filesystem.

**Methods**
- `void add_resource_format_loader(format_loader: ResourceFormatLoader, at_front: bool = false)`
- `bool exists(path: String, type_hint: String = "")`
- `Resource get_cached_ref(path: String)`
- `PackedStringArray get_dependencies(path: String)`
- `PackedStringArray get_recognized_extensions_for_type(type: String)`
- `int get_resource_uid(path: String)`
- `bool has_cached(path: String)`
- `PackedStringArray list_directory(directory_path: String)`
- `Resource load(path: String, type_hint: String = "", cache_mode: CacheMode = 1)`
- `Resource load_threaded_get(path: String)`
- `ThreadLoadStatus load_threaded_get_status(path: String, progress: Array = [])`
- `Error load_threaded_request(path: String, type_hint: String = "", use_sub_threads: bool = false, cache_mode: CacheMode = 1)`
- `void remove_resource_format_loader(format_loader: ResourceFormatLoader)`
- `void set_abort_on_missing_resources(abort: bool)`

**GDScript Examples**
```gdscript
for dependency in ResourceLoader.get_dependencies(path):
    if dependency.contains("::"):
        print(dependency.get_slice("::", 0)) # Prints the UID.
        print(dependency.get_slice("::", 2)) # Prints the fallback path.
    else:
        print(dependency) # Prints the path.
```
```gdscript
# Prints ["extra_data/", "model.gltf", "model.tscn", "model_slime.png"]
print(ResourceLoader.list_directory("res://assets/enemies/slime"))
```

### ResourcePreloader
*Inherits: **Node < Object***

This node is used to preload sub-resources inside a scene, so when the scene is loaded, all the resources are ready to use and can be retrieved from the preloader. You can add the resources using the ResourcePreloader tab when the node is selected.

**Methods**
- `void add_resource(name: StringName, resource: Resource)`
- `Resource get_resource(name: StringName) const`
- `PackedStringArray get_resource_list() const`
- `bool has_resource(name: StringName) const`
- `void remove_resource(name: StringName)`
- `void rename_resource(name: StringName, newname: StringName)`

### ResourceSaver
*Inherits: **Object***

A singleton for saving resource types to the filesystem.

**Methods**
- `void add_resource_format_saver(format_saver: ResourceFormatSaver, at_front: bool = false)`
- `PackedStringArray get_recognized_extensions(type: Resource)`
- `int get_resource_id_for_path(path: String, generate: bool = false)`
- `void remove_resource_format_saver(format_saver: ResourceFormatSaver)`
- `Error save(resource: Resource, path: String = "", flags: BitField[SaverFlags] = 0)`
- `Error set_uid(resource: String, uid: int)`

### ResourceUID
*Inherits: **Object***

Resource UIDs (Unique IDentifiers) allow the engine to keep references between resources intact, even if files are renamed or moved. They can be accessed with uid://.

**Methods**
- `void add_id(id: int, path: String)`
- `int create_id()`
- `int create_id_for_path(path: String)`
- `String ensure_path(path_or_uid: String) static`
- `String get_id_path(id: int) const`
- `bool has_id(id: int) const`
- `String id_to_text(id: int) const`
- `String path_to_uid(path: String) static`
- `void remove_id(id: int)`
- `void set_id(id: int, path: String)`
- `int text_to_id(text_id: String) const`
- `String uid_to_path(uid: String) static`

### Resource
*Inherits: **RefCounted < Object** | Inherited by: Animation, AnimationLibrary, AnimationNode, AnimationNodeStateMachinePlayback, AnimationNodeStateMachineTransition, AudioBusLayout, ...*

Resource is the base class for all Godot-specific resource types, serving primarily as data containers. Since they inherit from RefCounted, resources are reference-counted and freed when no longer in use. They can also be nested within other resources, and saved on disk. PackedScene, one of the most common Objects in a Godot project, is also a resource, uniquely capable of storing and instantiating the Nodes it contains as many times as desired.

**Properties**
- `bool resource_local_to_scene` = `false`
- `String resource_name` = `""`
- `String resource_path` = `""`
- `String resource_scene_unique_id`

**Methods**
- `RID _get_rid() virtual const`
- `void _reset_state() virtual`
- `void _set_path_cache(path: String) virtual const`
- `void _setup_local_to_scene() virtual`
- `Resource duplicate(deep: bool = false) const`
- `Resource duplicate_deep(deep_subresources_mode: DeepDuplicateMode = 1) const`
- `void emit_changed()`
- `String generate_scene_unique_id() static`
- `String get_id_for_path(path: String) const`
- `Node get_local_scene() const`
- `RID get_rid() const`
- `bool is_built_in() const`
- `void reset_state()`
- `void set_id_for_path(path: String, id: String)`
- `void set_path_cache(path: String)`
- `void setup_local_to_scene()`
- `void take_over_path(path: String)`

**GDScript Examples**
```gdscript
extends Resource

var damage = 0

func _setup_local_to_scene():
    damage = randi_range(10, 40)
```
```gdscript
var damage:
    set(new_value):
        if damage != new_value:
            damage = new_value
            emit_changed()
```

### SceneTreeTimer
*Inherits: **RefCounted < Object***

A one-shot timer managed by the scene tree, which emits timeout on completion. See also SceneTree.create_timer().

**Properties**
- `float time_left`

**GDScript Examples**
```gdscript
func some_function():
    print("Timer started.")
    await get_tree().create_timer(1.0).timeout
    print("Timer ended.")
```

### SceneTree
*Inherits: **MainLoop < Object***

As one of the most important classes, the SceneTree manages the hierarchy of nodes in a scene, as well as scenes themselves. Nodes can be added, fetched and removed. The whole scene tree (and thus the current scene) can be paused. Scenes can be loaded, switched and reloaded.

**Properties**
- `bool auto_accept_quit` = `true`
- `Node current_scene`
- `bool debug_collisions_hint` = `false`
- `bool debug_navigation_hint` = `false`
- `bool debug_paths_hint` = `false`
- `Node edited_scene_root`
- `bool multiplayer_poll` = `true`
- `bool paused` = `false`
- `bool physics_interpolation` = `false`
- `bool quit_on_go_back` = `true`
- `Window root`

**Methods**
- `void call_group(group: StringName, method: StringName, ...) vararg`
- `void call_group_flags(flags: int, group: StringName, method: StringName, ...) vararg`
- `Error change_scene_to_file(path: String)`
- `Error change_scene_to_node(node: Node)`
- `Error change_scene_to_packed(packed_scene: PackedScene)`
- `SceneTreeTimer create_timer(time_sec: float, process_always: bool = true, process_in_physics: bool = false, ignore_time_scale: bool = false)`
- `Tween create_tween()`
- `Node get_first_node_in_group(group: StringName)`
- `int get_frame() const`
- `MultiplayerAPI get_multiplayer(for_path: NodePath = NodePath("")) const`
- `int get_node_count() const`
- `int get_node_count_in_group(group: StringName) const`
- `Array[Node] get_nodes_in_group(group: StringName)`
- `Array[Tween] get_processed_tweens()`
- `bool has_group(name: StringName) const`
- `bool is_accessibility_enabled() const`
- `bool is_accessibility_supported() const`
- `void notify_group(group: StringName, notification: int)`
- `void notify_group_flags(call_flags: int, group: StringName, notification: int)`
- `void queue_delete(obj: Object)`
- `void quit(exit_code: int = 0)`
- `Error reload_current_scene()`
- `void set_group(group: StringName, property: String, value: Variant)`
- `void set_group_flags(call_flags: int, group: StringName, property: String, value: Variant)`
- `void set_multiplayer(multiplayer: MultiplayerAPI, root_path: NodePath = NodePath(""))`
- `void unload_current_scene()`

**GDScript Examples**
```gdscript
func some_function():
    print("start")
    await get_tree().create_timer(1.0).timeout
    print("end")
```
```gdscript
# This code should be inside an autoload.
get_tree().change_scene_to_file(other_scene_path)
await get_tree().scene_changed
print(get_tree().current_scene) # Prints the new scene.
```

### Semaphore
*Inherits: **RefCounted < Object***

A synchronization semaphore that can be used to synchronize multiple Threads. Initialized to zero on creation. For a binary version, see Mutex.

**Methods**
- `void post(count: int = 1)`
- `bool try_wait()`
- `void wait()`

### Thread
*Inherits: **RefCounted < Object***

A unit of execution in a process. Can run methods on Objects simultaneously. The use of synchronization via Mutex or Semaphore is advised if working with shared objects.

**Methods**
- `String get_id() const`
- `bool is_alive() const`
- `bool is_main_thread() static`
- `bool is_started() const`
- `void set_thread_safety_checks_enabled(enabled: bool) static`
- `Error start(callable: Callable, priority: Priority = 1)`
- `Variant wait_to_finish()`

### WeakRef
*Inherits: **RefCounted < Object***

A weakref can hold a RefCounted without contributing to the reference counter. A weakref can be created from an Object using @GlobalScope.weakref(). If this object is not a reference, weakref still works, however, it does not have any effect on the object. Weakrefs are useful in cases where multiple classes have variables that refer to each other. Without weakrefs, using these classes could lead to memory leaks, since both references keep each other from being released. Making part of the variables a weakref can prevent this cyclic dependency, and allows the references to be released.

**Methods**
- `Variant get_ref() const`

### WorkerThreadPool
*Inherits: **Object***

The WorkerThreadPool singleton allocates a set of Threads (called worker threads) on project startup and provides methods for offloading tasks to them. This can be used for simple multithreading without having to create Threads.

**Methods**
- `int add_group_task(action: Callable, elements: int, tasks_needed: int = -1, high_priority: bool = false, description: String = "")`
- `int add_task(action: Callable, high_priority: bool = false, description: String = "")`
- `int get_caller_group_id() const`
- `int get_caller_task_id() const`
- `int get_group_processed_element_count(group_id: int) const`
- `bool is_group_task_completed(group_id: int) const`
- `bool is_task_completed(task_id: int) const`
- `void wait_for_group_task_completion(group_id: int)`
- `Error wait_for_task_completion(task_id: int)`

**GDScript Examples**
```gdscript
var enemies = [] # An array to be filled with enemies.

func process_enemy_ai(enemy_index):
    var processed_enemy = enemies[enemy_index]
    # Expensive logic...

func _process(delta):
    var task_id = WorkerThreadPool.add_group_task(process_enemy_ai, enemies.size())
    # Other code...
    WorkerThreadPool.wait_for_group_task_completion(task_id)
    # Other code that depends on the enemy AI already being processed.
```
