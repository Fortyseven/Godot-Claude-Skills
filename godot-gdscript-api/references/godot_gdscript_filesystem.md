# Godot 4 GDScript API Reference — Filesystem

> GDScript-only reference. 9 classes.

### ConfigFile
*Inherits: **RefCounted < Object***

This helper class can be used to store Variant values on the filesystem using INI-style formatting. The stored values are identified by a section and a key:

**Methods**
- `void clear()`
- `String encode_to_text() const`
- `void erase_section(section: String)`
- `void erase_section_key(section: String, key: String)`
- `PackedStringArray get_section_keys(section: String) const`
- `PackedStringArray get_sections() const`
- `Variant get_value(section: String, key: String, default: Variant = null) const`
- `bool has_section(section: String) const`
- `bool has_section_key(section: String, key: String) const`
- `Error load(path: String)`
- `Error load_encrypted(path: String, key: PackedByteArray)`
- `Error load_encrypted_pass(path: String, password: String)`
- `Error parse(data: String)`
- `Error save(path: String)`
- `Error save_encrypted(path: String, key: PackedByteArray)`
- `Error save_encrypted_pass(path: String, password: String)`
- `void set_value(section: String, key: String, value: Variant)`

**GDScript Examples**
```gdscript
# Create new ConfigFile object.
var config = ConfigFile.new()

# Store some values.
config.set_value("Player1", "player_name", "Steve")
config.set_value("Player1", "best_score", 10)
config.set_value("Player2", "player_name", "V3geta")
config.set_value("Player2", "best_score", 9001)

# Save it to a file (overwrite if already exists).
config.save("user://scores.cfg")
```
```gdscript
var score_data = {}
var config = ConfigFile.new()

# Load data from a file.
var err = config.load("user://scores.cfg")

# If the file didn't load, ignore it.
if err != OK:
    return

# Iterate over all sections.
for player in config.get_sections():
    # Fetch the data for each section.
    var player_name = config.get_value(player, "player_name")
    var player_score = config.get_value(player, "best_score")
    score_data[player_name] = player_score
```

### DirAccess
*Inherits: **RefCounted < Object***

This class is used to manage directories and their content, even outside of the project folder.

**Properties**
- `bool include_hidden`
- `bool include_navigational`

**Methods**
- `Error change_dir(to_dir: String)`
- `Error copy(from: String, to: String, chmod_flags: int = -1)`
- `Error copy_absolute(from: String, to: String, chmod_flags: int = -1) static`
- `Error create_link(source: String, target: String)`
- `DirAccess create_temp(prefix: String = "", keep: bool = false) static`
- `bool current_is_dir() const`
- `bool dir_exists(path: String)`
- `bool dir_exists_absolute(path: String) static`
- `bool file_exists(path: String)`
- `String get_current_dir(include_drive: bool = true) const`
- `int get_current_drive()`
- `PackedStringArray get_directories()`
- `PackedStringArray get_directories_at(path: String) static`
- `int get_drive_count() static`
- `String get_drive_name(idx: int) static`
- `PackedStringArray get_files()`
- `PackedStringArray get_files_at(path: String) static`
- `String get_filesystem_type() const`
- `String get_next()`
- `Error get_open_error() static`
- `int get_space_left()`
- `bool is_bundle(path: String) const`
- `bool is_case_sensitive(path: String) const`
- `bool is_equivalent(path_a: String, path_b: String) const`
- `bool is_link(path: String)`
- `Error list_dir_begin()`
- `void list_dir_end()`
- `Error make_dir(path: String)`
- `Error make_dir_absolute(path: String) static`
- `Error make_dir_recursive(path: String)`
- `Error make_dir_recursive_absolute(path: String) static`
- `DirAccess open(path: String) static`
- `String read_link(path: String)`
- `Error remove(path: String)`
- `Error remove_absolute(path: String) static`
- `Error rename(from: String, to: String)`
- `Error rename_absolute(from: String, to: String) static`

**GDScript Examples**
```gdscript
func dir_contents(path):
    var dir = DirAccess.open(path)
    if dir:
        dir.list_dir_begin()
        var file_name = dir.get_next()
        while file_name != "":
            if dir.current_is_dir():
                print("Found directory: " + file_name)
            else:
                print("Found file: " + file_name)
            file_name = dir.get_next()
    else:
        print("An error occurred when trying to access the path.")
```
```gdscript
# Standard
var dir = DirAccess.open("user://levels")
dir.make_dir("world1")
# Static
DirAccess.make_dir_absolute("user://levels/world1")
```

### EditorSettings
*Inherits: **Resource < RefCounted < Object***

Object that holds the project-independent editor settings. These settings are generally visible in the Editor > Editor Settings menu.

**Properties**
- `bool asset_library/use_threads`
- `bool debugger/auto_switch_to_remote_scene_tree`
- `bool debugger/auto_switch_to_stack_trace`
- `int debugger/max_node_selection`
- `bool debugger/profile_native_calls`
- `int debugger/profiler_frame_history_size`
- `int debugger/profiler_frame_max_functions`
- `int debugger/profiler_target_fps`
- `float debugger/remote_inspect_refresh_interval`
- `float debugger/remote_scene_tree_refresh_interval`
- `bool docks/filesystem/always_show_folders`
- `String docks/filesystem/other_file_extensions`
- `String docks/filesystem/textfile_extensions`
- `int docks/filesystem/thumbnail_size`
- `float docks/property_editor/auto_refresh_interval`
- `float docks/property_editor/subresource_hue_tint`
- `bool docks/scene_tree/accessibility_warnings`
- `bool docks/scene_tree/ask_before_deleting_related_animation_tracks`
- `bool docks/scene_tree/ask_before_revoking_unique_name`
- `bool docks/scene_tree/auto_expand_to_selected`
- `bool docks/scene_tree/center_node_on_reparent`
- `bool docks/scene_tree/hide_filtered_out_parents`
- `bool docks/scene_tree/start_create_dialog_fully_expanded`
- `float editors/2d/auto_resample_delay`
- `Color editors/2d/bone_color1`
- `Color editors/2d/bone_color2`
- `Color editors/2d/bone_ik_color`
- `Color editors/2d/bone_outline_color`
- `float editors/2d/bone_outline_size`
- `Color editors/2d/bone_selected_color`

**Methods**
- `void add_property_info(info: Dictionary)`
- `void add_shortcut(path: String, shortcut: Shortcut)`
- `bool check_changed_settings_in_group(setting_prefix: String) const`
- `void erase(property: String)`
- `PackedStringArray get_changed_settings() const`
- `PackedStringArray get_favorites() const`
- `Variant get_project_metadata(section: String, key: String, default: Variant = null) const`
- `PackedStringArray get_recent_dirs() const`
- `Variant get_setting(name: String) const`
- `Shortcut get_shortcut(path: String) const`
- `PackedStringArray get_shortcut_list()`
- `bool has_setting(name: String) const`
- `bool has_shortcut(path: String) const`
- `bool is_shortcut(path: String, event: InputEvent) const`
- `void mark_setting_changed(setting: String)`
- `void remove_shortcut(path: String)`
- `void set_builtin_action_override(name: String, actions_list: Array[InputEvent])`
- `void set_favorites(dirs: PackedStringArray)`
- `void set_initial_value(name: StringName, value: Variant, update_current: bool)`
- `void set_project_metadata(section: String, key: String, data: Variant)`
- `void set_recent_dirs(dirs: PackedStringArray)`
- `void set_setting(name: String, value: Variant)`

**GDScript Examples**
```gdscript
var settings = EditorInterface.get_editor_settings()
# `settings.set("some/property", 10)` also works as this class overrides `_set()` internally.
settings.set_setting("some/property", 10)
# `settings.get("some/property")` also works as this class overrides `_get()` internally.
settings.get_setting("some/property")
var list_of_settings = settings.get_property_list()
```
```gdscript
var settings = EditorInterface.get_editor_settings()
settings.set("category/property_name", 0)

var property_info = {
    "name": "category/property_name",
    "type": TYPE_INT,
    "hint": PROPERTY_HINT_ENUM,
    "hint_string": "one,two,three"
}

settings.add_property_info(property_info)
```

### FileAccess
*Inherits: **RefCounted < Object***

This class can be used to permanently store data in the user device's file system and to read from it. This is useful for storing game save data or player configuration files.

**Properties**
- `bool big_endian`

**Methods**
- `void close()`
- `FileAccess create_temp(mode_flags: ModeFlags, prefix: String = "", extension: String = "", keep: bool = false) static`
- `bool eof_reached() const`
- `bool file_exists(path: String) static`
- `void flush()`
- `int get_8() const`
- `int get_16() const`
- `int get_32() const`
- `int get_64() const`
- `int get_access_time(file: String) static`
- `String get_as_text() const`
- `PackedByteArray get_buffer(length: int) const`
- `PackedStringArray get_csv_line(delim: String = ",") const`
- `float get_double() const`
- `Error get_error() const`
- `PackedByteArray get_extended_attribute(file: String, attribute_name: String) static`
- `String get_extended_attribute_string(file: String, attribute_name: String) static`
- `PackedStringArray get_extended_attributes_list(file: String) static`
- `PackedByteArray get_file_as_bytes(path: String) static`
- `String get_file_as_string(path: String) static`
- `float get_float() const`
- `float get_half() const`
- `bool get_hidden_attribute(file: String) static`
- `int get_length() const`
- `String get_line() const`
- `String get_md5(path: String) static`
- `int get_modified_time(file: String) static`
- `Error get_open_error() static`
- `String get_pascal_string()`
- `String get_path() const`
- `String get_path_absolute() const`
- `int get_position() const`
- `bool get_read_only_attribute(file: String) static`
- `float get_real() const`
- `String get_sha256(path: String) static`
- `int get_size(file: String) static`
- `BitField[UnixPermissionFlags] get_unix_permissions(file: String) static`
- `Variant get_var(allow_objects: bool = false) const`
- `bool is_open() const`
- `FileAccess open(path: String, flags: ModeFlags) static`

**GDScript Examples**
```gdscript
func save_to_file(content):
    var file = FileAccess.open("user://save_game.dat", FileAccess.WRITE)
    file.store_string(content)

func load_from_file():
    var file = FileAccess.open("user://save_game.dat", FileAccess.READ)
    var content = file.get_as_text()
    return content
```
```gdscript
while file.get_position() < file.get_length():
    # Read data
```

### PCKPacker
*Inherits: **RefCounted < Object***

The PCKPacker is used to create packages that can be loaded into a running project using ProjectSettings.load_resource_pack().

**Methods**
- `Error add_file(target_path: String, source_path: String, encrypt: bool = false)`
- `Error add_file_removal(target_path: String)`
- `Error flush(verbose: bool = false)`
- `Error pck_start(pck_path: String, alignment: int = 32, key: String = "0000000000000000000000000000000000000000000000000000000000000000", encrypt_directory: bool = false)`

**GDScript Examples**
```gdscript
var packer = PCKPacker.new()
packer.pck_start("test.pck")
packer.add_file("res://text.txt", "text.txt")
packer.flush()
```

### ProjectSettings
*Inherits: **Object***

Stores variables that can be accessed from everywhere. Use get_setting(), set_setting() or has_setting() to access them. Variables stored in project.godot are also loaded into ProjectSettings, making this object very useful for reading custom game configuration options.

**Properties**
- `int accessibility/general/accessibility_support` = `0`
- `int accessibility/general/updates_per_second` = `60`
- `bool animation/compatibility/default_parent_skeleton_in_mesh_instance_3d` = `false`
- `bool animation/warnings/check_angle_interpolation_type_conflicting` = `true`
- `bool animation/warnings/check_invalid_track_paths` = `true`
- `Color application/boot_splash/bg_color` = `Color(0.14, 0.14, 0.14, 1)`
- `String application/boot_splash/image` = `""`
- `int application/boot_splash/minimum_display_time` = `0`
- `bool application/boot_splash/show_image` = `true`
- `int application/boot_splash/stretch_mode` = `1`
- `bool application/boot_splash/use_filter` = `true`
- `bool application/config/auto_accept_quit` = `true`
- `String application/config/custom_user_dir_name` = `""`
- `String application/config/description` = `""`
- `bool application/config/disable_project_settings_override` = `false`
- `String application/config/icon` = `""`
- `String application/config/macos_native_icon` = `""`
- `String application/config/name` = `""`
- `Dictionary application/config/name_localized` = `{}`
- `String application/config/project_settings_override` = `""`
- `bool application/config/quit_on_go_back` = `true`
- `bool application/config/use_custom_user_dir` = `false`
- `bool application/config/use_hidden_project_data_directory` = `true`
- `String application/config/version` = `""`
- `String application/config/windows_native_icon` = `""`
- `bool application/run/delta_smoothing` = `true`
- `bool application/run/disable_stderr` = `false`
- `bool application/run/disable_stdout` = `false`
- `bool application/run/enable_alt_space_menu` = `false`
- `bool application/run/flush_stdout_on_print` = `false`

**Methods**
- `void add_property_info(hint: Dictionary)`
- `bool check_changed_settings_in_group(setting_prefix: String) const`
- `void clear(name: String)`
- `PackedStringArray get_changed_settings() const`
- `Array[Dictionary] get_global_class_list()`
- `int get_order(name: String) const`
- `Variant get_setting(name: String, default_value: Variant = null) const`
- `Variant get_setting_with_override(name: StringName) const`
- `Variant get_setting_with_override_and_custom_features(name: StringName, features: PackedStringArray) const`
- `String globalize_path(path: String) const`
- `bool has_setting(name: String) const`
- `bool load_resource_pack(pack: String, replace_files: bool = true, offset: int = 0)`
- `String localize_path(path: String) const`
- `Error save()`
- `Error save_custom(file: String)`
- `void set_as_basic(name: String, basic: bool)`
- `void set_as_internal(name: String, internal: bool)`
- `void set_initial_value(name: String, value: Variant)`
- `void set_order(name: String, position: int)`
- `void set_restart_if_changed(name: String, restart: bool)`
- `void set_setting(name: String, value: Variant)`

**GDScript Examples**
```gdscript
# Set the default gravity strength to 980.
PhysicsServer2D.area_set_param(get_viewport().find_world_2d().space, PhysicsServer2D.AREA_PARAM_GRAVITY, 980)
```
```gdscript
# Set the default gravity direction to `Vector2(0, 1)`.
PhysicsServer2D.area_set_param(get_viewport().find_world_2d().space, PhysicsServer2D.AREA_PARAM_GRAVITY_VECTOR, Vector2.DOWN)
```

### XMLParser
*Inherits: **RefCounted < Object***

Provides a low-level interface for creating parsers for XML files. This class can serve as base to make custom XML parsers.

**Methods**
- `int get_attribute_count() const`
- `String get_attribute_name(idx: int) const`
- `String get_attribute_value(idx: int) const`
- `int get_current_line() const`
- `String get_named_attribute_value(name: String) const`
- `String get_named_attribute_value_safe(name: String) const`
- `String get_node_data() const`
- `String get_node_name() const`
- `int get_node_offset() const`
- `NodeType get_node_type()`
- `bool has_attribute(name: String) const`
- `bool is_empty() const`
- `Error open(file: String)`
- `Error open_buffer(buffer: PackedByteArray)`
- `Error read()`
- `Error seek(position: int)`
- `void skip_section()`

**GDScript Examples**
```gdscript
var parser = XMLParser.new()
parser.open("path/to/file.svg")
while parser.read() != ERR_FILE_EOF:
    if parser.get_node_type() == XMLParser.NODE_ELEMENT:
        var node_name = parser.get_node_name()
        var attributes_dict = {}
        for idx in range(parser.get_attribute_count()):
            attributes_dict[parser.get_attribute_name(idx)] = parser.get_attribute_value(idx)
        print("The ", node_name, " element has the following attributes: ", attributes_dict)
```

### ZIPPacker
*Inherits: **RefCounted < Object***

This class implements a writer that allows storing the multiple blobs in a ZIP archive. See also ZIPReader and PCKPacker.

**Properties**
- `int compression_level` = `-1`

**Methods**
- `Error close()`
- `Error close_file()`
- `Error open(path: String, append: ZipAppend = 0)`
- `Error start_file(path: String)`
- `Error write_file(data: PackedByteArray)`

**GDScript Examples**
```gdscript
# Create a ZIP archive with a single file at its root.
func write_zip_file():
    var writer = ZIPPacker.new()
    var err = writer.open("user://archive.zip")
    if err != OK:
        return err
    writer.start_file("hello.txt")
    writer.write_file("Hello World".to_utf8_buffer())
    writer.close_file()

    writer.close()
    return OK
```

### ZIPReader
*Inherits: **RefCounted < Object***

This class implements a reader that can extract the content of individual files inside a ZIP archive. See also ZIPPacker.

**Methods**
- `Error close()`
- `bool file_exists(path: String, case_sensitive: bool = true)`
- `int get_compression_level(path: String, case_sensitive: bool = true)`
- `PackedStringArray get_files()`
- `Error open(path: String)`
- `PackedByteArray read_file(path: String, case_sensitive: bool = true)`

**GDScript Examples**
```gdscript
# Read a single file from a ZIP archive.
func read_zip_file():
    var reader = ZIPReader.new()
    var err = reader.open("user://archive.zip")
    if err != OK:
        return PackedByteArray()
    var res = reader.read_file("hello.txt")
    reader.close()
    return res

# Extract all files from a ZIP archive, preserving the directories within.
# This acts like the "Extract all" functionality from most archive managers.
func extract_all_from_zip():
    var reader = ZIPReader.new()
    reader.open("res://archive.zip")

    # Destination directory for the extracted files (this folder must exis
# ...
```
