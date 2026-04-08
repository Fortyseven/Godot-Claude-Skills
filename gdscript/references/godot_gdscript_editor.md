# Godot 4 GDScript API Reference — Editor

> GDScript-only reference. 53 classes.

### EditorCommandPalette
*Inherits: **ConfirmationDialog < AcceptDialog < Window < Viewport < Node < Object***

Object that holds all the available Commands and their shortcuts text. These Commands can be accessed through Editor > Command Palette menu.

**Properties**
- `bool dialog_hide_on_ok` = `false (overrides AcceptDialog)`

**Methods**
- `void add_command(command_name: String, key_name: String, binded_callable: Callable, shortcut_text: String = "None")`
- `void remove_command(key_name: String)`

**GDScript Examples**
```gdscript
var command_palette = EditorInterface.get_command_palette()
# external_command is a function that will be called with the command is executed.
var command_callable = Callable(self, "external_command").bind(arguments)
command_palette.add_command("command", "test/command",command_callable)
```

### EditorContextMenuPlugin
*Inherits: **RefCounted < Object***

EditorContextMenuPlugin allows for the addition of custom options in the editor's context menu.

**Methods**
- `void _popup_menu(paths: PackedStringArray) virtual`
- `void add_context_menu_item(name: String, callback: Callable, icon: Texture2D = null)`
- `void add_context_menu_item_from_shortcut(name: String, shortcut: Shortcut, icon: Texture2D = null)`
- `void add_context_submenu_item(name: String, menu: PopupMenu, icon: Texture2D = null)`
- `void add_menu_shortcut(shortcut: Shortcut, callback: Callable)`

**GDScript Examples**
```gdscript
func _popup_menu(paths):
    if paths.is_empty():
        add_context_menu_item("New Image File...", create_image)
    else:
        add_context_menu_item("Image File...", create_image)
```
```gdscript
func _popup_menu(paths):
    var code_edit = Engine.get_main_loop().root.get_node(paths[0]);
```

### EditorDebuggerPlugin
*Inherits: **RefCounted < Object***

EditorDebuggerPlugin provides functions related to the editor side of the debugger.

**Methods**
- `void _breakpoint_set_in_tree(script: Script, line: int, enabled: bool) virtual`
- `void _breakpoints_cleared_in_tree() virtual`
- `bool _capture(message: String, data: Array, session_id: int) virtual`
- `void _goto_script_line(script: Script, line: int) virtual`
- `bool _has_capture(capture: String) virtual const`
- `void _setup_session(session_id: int) virtual`
- `EditorDebuggerSession get_session(id: int)`
- `Array get_sessions()`

**GDScript Examples**
```gdscript
@tool
extends EditorPlugin

class ExampleEditorDebugger extends EditorDebuggerPlugin:

    func _has_capture(capture):
        # Return true if you wish to handle messages with the prefix "my_plugin:".
        return capture == "my_plugin"

    func _capture(message, data, session_id):
        if message == "my_plugin:ping":
            get_session(session_id).send_message("my_plugin:echo", data)
            return true
        return false

    func _setup_session(session_id):
        # Add a new tab in the debugger session UI containing a label.
        var label = Label.new()
        label.
# ...
```
```gdscript
extends Node

func _ready():
    EngineDebugger.register_message_capture("my_plugin", _capture)
    EngineDebugger.send_message("my_plugin:ping", ["test"])

func _capture(message, data):
    # Note that the "my_plugin:" prefix is not used here.
    if message == "echo":
        prints("Echo received:", data)
        return true
    return false
```

### EditorDebuggerSession
*Inherits: **RefCounted < Object***

This class cannot be directly instantiated and must be retrieved via an EditorDebuggerPlugin.

**Methods**
- `void add_session_tab(control: Control)`
- `bool is_active()`
- `bool is_breaked()`
- `bool is_debuggable()`
- `void remove_session_tab(control: Control)`
- `void send_message(message: String, data: Array = [])`
- `void set_breakpoint(path: String, line: int, enabled: bool)`
- `void toggle_profiler(profiler: String, enable: bool, data: Array = [])`

### EditorDock
*Inherits: **MarginContainer < Container < Control < CanvasItem < Node < Object** | Inherited by: FileSystemDock*

EditorDock is a Container node that can be docked in one of the editor's dock slots. Docks are added by plugins to provide space for controls related to an EditorPlugin. The editor comes with a few built-in docks, such as the Scene dock, FileSystem dock, etc.

**Properties**
- `BitField[DockLayout] available_layouts` = `5`
- `bool closable` = `false`
- `DockSlot default_slot` = `-1`
- `Texture2D dock_icon`
- `Shortcut dock_shortcut`
- `bool force_show_icon` = `false`
- `bool global` = `true`
- `StringName icon_name` = `&""`
- `String layout_key` = `""`
- `String title` = `""`
- `Color title_color` = `Color(0, 0, 0, 0)`
- `bool transient` = `false`

**Methods**
- `void _load_layout_from_config(config: ConfigFile, section: String) virtual`
- `void _save_layout_to_config(config: ConfigFile, section: String) virtual const`
- `void _update_layout(layout: int) virtual`
- `void close()`
- `void make_visible()`
- `void open()`

**GDScript Examples**
```gdscript
@tool
extends EditorPlugin

# Dock reference.
var dock

# Plugin initialization.
func _enter_tree():
    dock = EditorDock.new()
    dock.title = "My Dock"
    dock.dock_icon = preload("./dock_icon.png")
    dock.default_slot = EditorDock.DOCK_SLOT_RIGHT_UL
    var dock_content = preload("./dock_content.tscn").instantiate()
    dock.add_child(dock_content)
    add_dock(dock)

# Plugin clean-up.
func _exit_tree():
    remove_dock(dock)
    dock.queue_free()
    dock = null
```
```gdscript
func _update_layout(layout):
    box_container.vertical = (layout == DOCK_LAYOUT_VERTICAL)
```

### EditorExportPlatformAndroid
*Inherits: **EditorExportPlatform < RefCounted < Object***

Exporter for Android.

**Properties**
- `String apk_expansion/SALT`
- `bool apk_expansion/enable`
- `String apk_expansion/public_key`
- `bool architectures/arm64-v8a`
- `bool architectures/armeabi-v7a`
- `bool architectures/x86`
- `bool architectures/x86_64`
- `String command_line/extra_args`
- `String custom_template/debug`
- `String custom_template/release`
- `bool gesture/swipe_to_dismiss`
- `String gradle_build/android_source_template`
- `bool gradle_build/compress_native_libraries`
- `Dictionary gradle_build/custom_theme_attributes`
- `int gradle_build/export_format`
- `String gradle_build/gradle_build_directory`
- `String gradle_build/min_sdk`
- `String gradle_build/target_sdk`
- `bool gradle_build/use_gradle_build`
- `bool graphics/opengl_debug`
- `String keystore/debug`
- `String keystore/debug_password`
- `String keystore/debug_user`
- `String keystore/release`
- `String keystore/release_password`
- `String keystore/release_user`
- `String launcher_icons/adaptive_background_432x432`
- `String launcher_icons/adaptive_foreground_432x432`
- `String launcher_icons/adaptive_monochrome_432x432`
- `String launcher_icons/main_192x192`

### EditorExportPlatformAppleEmbedded
*Inherits: **EditorExportPlatform < RefCounted < Object** | Inherited by: EditorExportPlatformIOS, EditorExportPlatformVisionOS*

The base class for Apple embedded platform exporters. These include iOS and visionOS, but not macOS. See the classes inheriting from this one for more details.

### EditorExportPlatformExtension
*Inherits: **EditorExportPlatform < RefCounted < Object***

External EditorExportPlatform implementations should inherit from this class.

**Methods**
- `bool _can_export(preset: EditorExportPreset, debug: bool) virtual const`
- `void _cleanup() virtual`
- `Error _export_pack(preset: EditorExportPreset, debug: bool, path: String, flags: BitField[DebugFlags]) virtual`
- `Error _export_pack_patch(preset: EditorExportPreset, debug: bool, path: String, patches: PackedStringArray, flags: BitField[DebugFlags]) virtual`
- `Error _export_project(preset: EditorExportPreset, debug: bool, path: String, flags: BitField[DebugFlags]) virtual required`
- `Error _export_zip(preset: EditorExportPreset, debug: bool, path: String, flags: BitField[DebugFlags]) virtual`
- `Error _export_zip_patch(preset: EditorExportPreset, debug: bool, path: String, patches: PackedStringArray, flags: BitField[DebugFlags]) virtual`
- `PackedStringArray _get_binary_extensions(preset: EditorExportPreset) virtual required const`
- `String _get_debug_protocol() virtual const`
- `String _get_device_architecture(device: int) virtual const`
- `bool _get_export_option_visibility(preset: EditorExportPreset, option: String) virtual const`
- `String _get_export_option_warning(preset: EditorExportPreset, option: StringName) virtual const`
- `Array[Dictionary] _get_export_options() virtual const`
- `Texture2D _get_logo() virtual required const`
- `String _get_name() virtual required const`
- `Texture2D _get_option_icon(device: int) virtual const`
- `String _get_option_label(device: int) virtual const`
- `String _get_option_tooltip(device: int) virtual const`
- `int _get_options_count() virtual const`
- `String _get_options_tooltip() virtual const`
- `String _get_os_name() virtual required const`
- `PackedStringArray _get_platform_features() virtual required const`
- `PackedStringArray _get_preset_features(preset: EditorExportPreset) virtual required const`
- `Texture2D _get_run_icon() virtual const`
- `bool _has_valid_export_configuration(preset: EditorExportPreset, debug: bool) virtual required const`
- `bool _has_valid_project_configuration(preset: EditorExportPreset) virtual required const`
- `void _initialize() virtual`
- `bool _is_executable(path: String) virtual const`
- `bool _poll_export() virtual`
- `Error _run(preset: EditorExportPreset, device: int, debug_flags: BitField[DebugFlags]) virtual`
- `bool _should_update_export_options() virtual`
- `String get_config_error() const`
- `bool get_config_missing_templates() const`
- `void set_config_error(error_text: String) const`
- `void set_config_missing_templates(missing_templates: bool) const`

### EditorExportPlatformIOS
*Inherits: **EditorExportPlatformAppleEmbedded < EditorExportPlatform < RefCounted < Object***

Exporter for iOS.

**Properties**
- `String application/additional_plist_content`
- `String application/app_store_team_id`
- `String application/bundle_identifier`
- `String application/code_sign_identity_debug`
- `String application/code_sign_identity_release`
- `bool application/delete_old_export_files_unconditionally`
- `int application/export_method_debug`
- `int application/export_method_release`
- `bool application/export_project_only`
- `int application/icon_interpolation`
- `String application/min_ios_version`
- `String application/provisioning_profile_specifier_debug`
- `String application/provisioning_profile_specifier_release`
- `String application/provisioning_profile_uuid_debug`
- `String application/provisioning_profile_uuid_release`
- `String application/short_version`
- `String application/signature`
- `int application/targeted_device_family`
- `String application/version`
- `bool architectures/arm64`
- `bool capabilities/access_wifi`
- `PackedStringArray capabilities/additional`
- `bool capabilities/performance_a12`
- `bool capabilities/performance_gaming_tier`
- `String custom_template/debug`
- `String custom_template/release`
- `String entitlements/additional`
- `bool entitlements/game_center`
- `bool entitlements/increased_memory_limit`
- `String entitlements/push_notifications`

### EditorExportPlatformLinuxBSD
*Inherits: **EditorExportPlatformPC < EditorExportPlatform < RefCounted < Object***

Exporter for Linux/BSD.

**Properties**
- `String binary_format/architecture`
- `bool binary_format/embed_pck`
- `String custom_template/debug`
- `String custom_template/release`
- `int debug/export_console_wrapper`
- `bool shader_baker/enabled`
- `String ssh_remote_deploy/cleanup_script`
- `bool ssh_remote_deploy/enabled`
- `String ssh_remote_deploy/extra_args_scp`
- `String ssh_remote_deploy/extra_args_ssh`
- `String ssh_remote_deploy/host`
- `String ssh_remote_deploy/port`
- `String ssh_remote_deploy/run_script`
- `bool texture_format/etc2_astc`
- `bool texture_format/s3tc_bptc`

### EditorExportPlatformMacOS
*Inherits: **EditorExportPlatform < RefCounted < Object***

Exporter for macOS.

**Properties**
- `String application/additional_plist_content`
- `String application/app_category`
- `String application/bundle_identifier`
- `String application/copyright`
- `Dictionary application/copyright_localized`
- `int application/export_angle`
- `String application/icon`
- `int application/icon_interpolation`
- `String application/liquid_glass_icon`
- `String application/min_macos_version_arm64`
- `String application/min_macos_version_x86_64`
- `String application/short_version`
- `String application/signature`
- `String application/version`
- `String binary_format/architecture`
- `String codesign/apple_team_id`
- `String codesign/certificate_file`
- `String codesign/certificate_password`
- `int codesign/codesign`
- `PackedStringArray codesign/custom_options`
- `String codesign/entitlements/additional`
- `bool codesign/entitlements/address_book`
- `bool codesign/entitlements/allow_dyld_environment_variables`
- `bool codesign/entitlements/allow_jit_code_execution`
- `bool codesign/entitlements/allow_unsigned_executable_memory`
- `bool codesign/entitlements/app_sandbox/device_bluetooth`
- `bool codesign/entitlements/app_sandbox/device_usb`
- `bool codesign/entitlements/app_sandbox/enabled`
- `int codesign/entitlements/app_sandbox/files_downloads`
- `int codesign/entitlements/app_sandbox/files_movies`

### EditorExportPlatformPC
*Inherits: **EditorExportPlatform < RefCounted < Object** | Inherited by: EditorExportPlatformLinuxBSD, EditorExportPlatformWindows*

The base class for the desktop platform exporters. These include Windows and Linux/BSD, but not macOS. See the classes inheriting from this one for more details.

### EditorExportPlatformVisionOS
*Inherits: **EditorExportPlatformAppleEmbedded < EditorExportPlatform < RefCounted < Object***

Exporter for visionOS.

**Properties**
- `String application/additional_plist_content`
- `String application/app_store_team_id`
- `String application/bundle_identifier`
- `String application/code_sign_identity_debug`
- `String application/code_sign_identity_release`
- `bool application/delete_old_export_files_unconditionally`
- `int application/export_method_debug`
- `int application/export_method_release`
- `bool application/export_project_only`
- `int application/icon_interpolation`
- `String application/min_visionos_version`
- `String application/provisioning_profile_specifier_debug`
- `String application/provisioning_profile_specifier_release`
- `String application/provisioning_profile_uuid_debug`
- `String application/provisioning_profile_uuid_release`
- `String application/short_version`
- `String application/signature`
- `String application/version`
- `bool architectures/arm64`
- `bool capabilities/access_wifi`
- `PackedStringArray capabilities/additional`
- `bool capabilities/performance_a12`
- `bool capabilities/performance_gaming_tier`
- `String custom_template/debug`
- `String custom_template/release`
- `String entitlements/additional`
- `bool entitlements/game_center`
- `bool entitlements/increased_memory_limit`
- `String entitlements/push_notifications`
- `String icons/icon_1024x1024`

### EditorExportPlatformWeb
*Inherits: **EditorExportPlatform < RefCounted < Object***

The Web exporter customizes how a web build is handled. In the editor's "Export" window, it is created when adding a new "Web" preset.

**Properties**
- `String custom_template/debug`
- `String custom_template/release`
- `int html/canvas_resize_policy`
- `String html/custom_html_shell`
- `bool html/experimental_virtual_keyboard`
- `bool html/export_icon`
- `bool html/focus_canvas_on_start`
- `String html/head_include`
- `Color progressive_web_app/background_color`
- `int progressive_web_app/display`
- `bool progressive_web_app/enabled`
- `bool progressive_web_app/ensure_cross_origin_isolation_headers`
- `String progressive_web_app/icon_144x144`
- `String progressive_web_app/icon_180x180`
- `String progressive_web_app/icon_512x512`
- `String progressive_web_app/offline_page`
- `int progressive_web_app/orientation`
- `int threads/emscripten_pool_size`
- `int threads/godot_pool_size`
- `bool variant/extensions_support`
- `bool variant/thread_support`
- `bool vram_texture_compression/for_desktop`
- `bool vram_texture_compression/for_mobile`

### EditorExportPlatformWindows
*Inherits: **EditorExportPlatformPC < EditorExportPlatform < RefCounted < Object***

The Windows exporter customizes how a Windows build is handled. In the editor's "Export" window, it is created when adding a new "Windows" preset.

**Properties**
- `String application/company_name`
- `String application/console_wrapper_icon`
- `String application/copyright`
- `bool application/d3d12_agility_sdk_multiarch`
- `int application/export_angle`
- `int application/export_d3d12`
- `String application/file_description`
- `String application/file_version`
- `String application/icon`
- `int application/icon_interpolation`
- `bool application/modify_resources`
- `String application/product_name`
- `String application/product_version`
- `String application/trademarks`
- `String binary_format/architecture`
- `bool binary_format/embed_pck`
- `PackedStringArray codesign/custom_options`
- `String codesign/description`
- `int codesign/digest_algorithm`
- `bool codesign/enable`
- `String codesign/identity`
- `int codesign/identity_type`
- `String codesign/password`
- `bool codesign/timestamp`
- `String codesign/timestamp_server_url`
- `String custom_template/debug`
- `String custom_template/release`
- `int debug/export_console_wrapper`
- `bool shader_baker/enabled`
- `String ssh_remote_deploy/cleanup_script`

### EditorExportPlatform
*Inherits: **RefCounted < Object** | Inherited by: EditorExportPlatformAndroid, EditorExportPlatformAppleEmbedded, EditorExportPlatformExtension, EditorExportPlatformMacOS, EditorExportPlatformPC, EditorExportPlatformWeb*

Base resource that provides the functionality of exporting a release build of a project to a platform, from the editor. Stores platform-specific metadata such as the name and supported features of the platform, and performs the exporting of projects, PCK files, and ZIP files. Uses an export template for the platform provided at the time of project exporting.

**Methods**
- `void add_message(type: ExportMessageType, category: String, message: String)`
- `void clear_messages()`
- `EditorExportPreset create_preset()`
- `Error export_pack(preset: EditorExportPreset, debug: bool, path: String, flags: BitField[DebugFlags] = 0)`
- `Error export_pack_patch(preset: EditorExportPreset, debug: bool, path: String, patches: PackedStringArray = PackedStringArray(), flags: BitField[DebugFlags] = 0)`
- `Error export_project(preset: EditorExportPreset, debug: bool, path: String, flags: BitField[DebugFlags] = 0)`
- `Error export_project_files(preset: EditorExportPreset, debug: bool, save_cb: Callable, shared_cb: Callable = Callable())`
- `Error export_zip(preset: EditorExportPreset, debug: bool, path: String, flags: BitField[DebugFlags] = 0)`
- `Error export_zip_patch(preset: EditorExportPreset, debug: bool, path: String, patches: PackedStringArray = PackedStringArray(), flags: BitField[DebugFlags] = 0)`
- `Dictionary find_export_template(template_file_name: String) const`
- `PackedStringArray gen_export_flags(flags: BitField[DebugFlags])`
- `Array get_current_presets() const`
- `PackedStringArray get_forced_export_files(preset: EditorExportPreset = null) static`
- `Dictionary get_internal_export_files(preset: EditorExportPreset, debug: bool)`
- `String get_message_category(index: int) const`
- `int get_message_count() const`
- `String get_message_text(index: int) const`
- `ExportMessageType get_message_type(index: int) const`
- `String get_os_name() const`
- `ExportMessageType get_worst_message_type() const`
- `Dictionary save_pack(preset: EditorExportPreset, debug: bool, path: String, embed: bool = false)`
- `Dictionary save_pack_patch(preset: EditorExportPreset, debug: bool, path: String)`
- `Dictionary save_zip(preset: EditorExportPreset, debug: bool, path: String)`
- `Dictionary save_zip_patch(preset: EditorExportPreset, debug: bool, path: String)`
- `Error ssh_push_to_remote(host: String, port: String, scp_args: PackedStringArray, src_file: String, dst_file: String) const`
- `Error ssh_run_on_remote(host: String, port: String, ssh_arg: PackedStringArray, cmd_args: String, output: Array = [], port_fwd: int = -1) const`
- `int ssh_run_on_remote_no_wait(host: String, port: String, ssh_args: PackedStringArray, cmd_args: String, port_fwd: int = -1) const`

### EditorExportPlugin
*Inherits: **RefCounted < Object***

EditorExportPlugins are automatically invoked whenever the user exports the project. Their most common use is to determine what files are being included in the exported project. For each plugin, _export_begin() is called at the beginning of the export process and then _export_file() is called for each exported file.

**Methods**
- `bool _begin_customize_resources(platform: EditorExportPlatform, features: PackedStringArray) virtual const`
- `bool _begin_customize_scenes(platform: EditorExportPlatform, features: PackedStringArray) virtual const`
- `Resource _customize_resource(resource: Resource, path: String) virtual required`
- `Node _customize_scene(scene: Node, path: String) virtual required`
- `void _end_customize_resources() virtual`
- `void _end_customize_scenes() virtual`
- `void _export_begin(features: PackedStringArray, is_debug: bool, path: String, flags: int) virtual`
- `void _export_end() virtual`
- `void _export_file(path: String, type: String, features: PackedStringArray) virtual`
- `PackedStringArray _get_android_dependencies(platform: EditorExportPlatform, debug: bool) virtual const`
- `PackedStringArray _get_android_dependencies_maven_repos(platform: EditorExportPlatform, debug: bool) virtual const`
- `PackedStringArray _get_android_libraries(platform: EditorExportPlatform, debug: bool) virtual const`
- `String _get_android_manifest_activity_element_contents(platform: EditorExportPlatform, debug: bool) virtual const`
- `String _get_android_manifest_application_element_contents(platform: EditorExportPlatform, debug: bool) virtual const`
- `String _get_android_manifest_element_contents(platform: EditorExportPlatform, debug: bool) virtual const`
- `int _get_customization_configuration_hash() virtual required const`
- `PackedStringArray _get_export_features(platform: EditorExportPlatform, debug: bool) virtual const`
- `bool _get_export_option_visibility(platform: EditorExportPlatform, option: String) virtual const`
- `String _get_export_option_warning(platform: EditorExportPlatform, option: String) virtual const`
- `Array[Dictionary] _get_export_options(platform: EditorExportPlatform) virtual const`
- `Dictionary _get_export_options_overrides(platform: EditorExportPlatform) virtual const`
- `String _get_name() virtual required const`
- `bool _should_update_export_options(platform: EditorExportPlatform) virtual const`
- `bool _supports_platform(platform: EditorExportPlatform) virtual const`
- `PackedByteArray _update_android_prebuilt_manifest(platform: EditorExportPlatform, manifest_data: PackedByteArray) virtual const`
- `void add_apple_embedded_platform_bundle_file(path: String)`
- `void add_apple_embedded_platform_cpp_code(code: String)`
- `void add_apple_embedded_platform_embedded_framework(path: String)`
- `void add_apple_embedded_platform_framework(path: String)`
- `void add_apple_embedded_platform_linker_flags(flags: String)`
- `void add_apple_embedded_platform_plist_content(plist_content: String)`
- `void add_apple_embedded_platform_project_static_lib(path: String)`
- `void add_file(path: String, file: PackedByteArray, remap: bool)`
- `void add_ios_bundle_file(path: String)`
- `void add_ios_cpp_code(code: String)`
- `void add_ios_embedded_framework(path: String)`
- `void add_ios_framework(path: String)`
- `void add_ios_linker_flags(flags: String)`
- `void add_ios_plist_content(plist_content: String)`
- `void add_ios_project_static_lib(path: String)`

**GDScript Examples**
```gdscript
class MyExportPlugin extends EditorExportPlugin:
    func _get_name() -> String:
        return "MyExportPlugin"

    func _supports_platform(platform) -> bool:
        if platform is EditorExportPlatformPC:
            # Run on all desktop platforms including Windows, MacOS and Linux.
            return true
        return false

    func _get_export_options_overrides(platform) -> Dictionary:
        # Override "Embed PCK" to always be enabled.
        return {
            "binary_format/embed_pck": true,
        }
```

### EditorExportPreset
*Inherits: **RefCounted < Object***

Represents the configuration of an export preset, as created by the editor's export dialog. An EditorExportPreset instance is intended to be used a read-only configuration passed to the EditorExportPlatform methods when exporting the project.

**Methods**
- `bool are_advanced_options_enabled() const`
- `String get_custom_features() const`
- `Dictionary get_customized_files() const`
- `int get_customized_files_count() const`
- `bool get_encrypt_directory() const`
- `bool get_encrypt_pck() const`
- `String get_encryption_ex_filter() const`
- `String get_encryption_in_filter() const`
- `String get_encryption_key() const`
- `String get_exclude_filter() const`
- `ExportFilter get_export_filter() const`
- `String get_export_path() const`
- `FileExportMode get_file_export_mode(path: String, default: FileExportMode = 0) const`
- `PackedStringArray get_files_to_export() const`
- `String get_include_filter() const`
- `Variant get_or_env(name: StringName, env_var: String) const`
- `PackedStringArray get_patches() const`
- `String get_preset_name() const`
- `Variant get_project_setting(name: StringName)`
- `ScriptExportMode get_script_export_mode() const`
- `String get_version(name: StringName, windows_version: bool) const`
- `bool has(property: StringName) const`
- `bool has_export_file(path: String)`
- `bool is_dedicated_server() const`
- `bool is_runnable() const`

### EditorFeatureProfile
*Inherits: **RefCounted < Object***

An editor feature profile can be used to disable specific features of the Godot editor. When disabled, the features won't appear in the editor, which makes the editor less cluttered. This is useful in education settings to reduce confusion or when working in a team. For example, artists and level designers could use a feature profile that disables the script editor to avoid accidentally making changes to files they aren't supposed to edit.

**Methods**
- `String get_feature_name(feature: Feature)`
- `bool is_class_disabled(class_name: StringName) const`
- `bool is_class_editor_disabled(class_name: StringName) const`
- `bool is_class_property_disabled(class_name: StringName, property: StringName) const`
- `bool is_feature_disabled(feature: Feature) const`
- `Error load_from_file(path: String)`
- `Error save_to_file(path: String)`
- `void set_disable_class(class_name: StringName, disable: bool)`
- `void set_disable_class_editor(class_name: StringName, disable: bool)`
- `void set_disable_class_property(class_name: StringName, property: StringName, disable: bool)`
- `void set_disable_feature(feature: Feature, disable: bool)`

### EditorFileDialog
*Inherits: **FileDialog < ConfirmationDialog < AcceptDialog < Window < Viewport < Node < Object***

EditorFileDialog is a FileDialog tweaked to work in the editor. It automatically handles favorite and recent directory lists, and synchronizes some properties with their corresponding editor settings.

**Properties**
- `bool disable_overwrite_warning` = `false`

**Methods**
- `void add_side_menu(menu: Control, title: String = "")`

### EditorFileSystemDirectory
*Inherits: **Object***

A more generalized, low-level variation of the directory concept.

**Methods**
- `int find_dir_index(name: String) const`
- `int find_file_index(name: String) const`
- `String get_file(idx: int) const`
- `int get_file_count() const`
- `bool get_file_import_is_valid(idx: int) const`
- `String get_file_path(idx: int) const`
- `String get_file_script_class_extends(idx: int) const`
- `String get_file_script_class_name(idx: int) const`
- `StringName get_file_type(idx: int) const`
- `String get_name()`
- `EditorFileSystemDirectory get_parent()`
- `String get_path() const`
- `EditorFileSystemDirectory get_subdir(idx: int)`
- `int get_subdir_count() const`

### EditorFileSystemImportFormatSupportQuery
*Inherits: **RefCounted < Object***

This class is used to query and configure a certain import format. It is used in conjunction with asset format import plugins.

**Methods**
- `PackedStringArray _get_file_extensions() virtual required const`
- `bool _is_active() virtual required const`
- `bool _query() virtual required const`

### EditorFileSystem
*Inherits: **Node < Object***

This object holds information of all resources in the filesystem, their types, etc.

**Methods**
- `String get_file_type(path: String) const`
- `EditorFileSystemDirectory get_filesystem()`
- `EditorFileSystemDirectory get_filesystem_path(path: String)`
- `float get_scanning_progress() const`
- `bool is_scanning() const`
- `void reimport_files(files: PackedStringArray)`
- `void scan()`
- `void scan_sources()`
- `void update_file(path: String)`

### EditorImportPlugin
*Inherits: **ResourceImporter < RefCounted < Object***

EditorImportPlugins provide a way to extend the editor's resource import functionality. Use them to import resources from custom files or to provide alternatives to the editor's existing importers.

**Methods**
- `bool _can_import_threaded() virtual const`
- `int _get_format_version() virtual const`
- `Array[Dictionary] _get_import_options(path: String, preset_index: int) virtual required const`
- `int _get_import_order() virtual const`
- `String _get_importer_name() virtual required const`
- `bool _get_option_visibility(path: String, option_name: StringName, options: Dictionary) virtual const`
- `int _get_preset_count() virtual const`
- `String _get_preset_name(preset_index: int) virtual required const`
- `float _get_priority() virtual const`
- `PackedStringArray _get_recognized_extensions() virtual required const`
- `String _get_resource_type() virtual required const`
- `String _get_save_extension() virtual required const`
- `String _get_visible_name() virtual required const`
- `Error _import(source_file: String, save_path: String, options: Dictionary, platform_variants: Array[String], gen_files: Array[String]) virtual required const`
- `Error append_import_external_resource(path: String, custom_options: Dictionary = {}, custom_importer: String = "", generator_parameters: Variant = null)`

**GDScript Examples**
```gdscript
@tool
extends EditorImportPlugin

func _get_importer_name():
    return "my.special.plugin"

func _get_visible_name():
    return "Special Mesh"

func _get_recognized_extensions():
    return ["special", "spec"]

func _get_save_extension():
    return "mesh"

func _get_resource_type():
    return "Mesh"

func _get_preset_count():
    return 1

func _get_preset_name(preset_index):
    return "Default"

func _get_import_options(path, preset_index):
    return [{"name": "my_option", "default_value": false}]

func _import(source_file, save_path, options, platform_variants, gen_files):
    var file
# ...
```
```gdscript
func _get_option_visibility(path, option_name, options):
    # Only show the lossy quality setting if the compression mode is set to "Lossy".
    if option_name == "compress/lossy_quality" and options.has("compress/mode"):
        return int(options["compress/mode"]) == COMPRESS_LOSSY # This is a constant that you set

    return true
```

### EditorInspectorPlugin
*Inherits: **RefCounted < Object***

EditorInspectorPlugin allows adding custom property editors to EditorInspector.

**Methods**
- `bool _can_handle(object: Object) virtual const`
- `void _parse_begin(object: Object) virtual`
- `void _parse_category(object: Object, category: String) virtual`
- `void _parse_end(object: Object) virtual`
- `void _parse_group(object: Object, group: String) virtual`
- `bool _parse_property(object: Object, type: Variant.Type, name: String, hint_type: PropertyHint, hint_string: String, usage_flags: BitField[PropertyUsageFlags], wide: bool) virtual`
- `void add_custom_control(control: Control)`
- `void add_property_editor(property: String, editor: Control, add_to_end: bool = false, label: String = "")`
- `void add_property_editor_for_multiple_properties(label: String, properties: PackedStringArray, editor: Control)`

### EditorInspector
*Inherits: **ScrollContainer < Container < Control < CanvasItem < Node < Object***

This is the control that implements property editing in the editor's Settings dialogs, the Inspector dock, etc. To get the EditorInspector used in the editor's Inspector dock, use EditorInterface.get_inspector().

**Properties**
- `bool draw_focus_border` = `true (overrides ScrollContainer)`
- `FocusMode focus_mode` = `2 (overrides Control)`
- `bool follow_focus` = `true (overrides ScrollContainer)`
- `ScrollMode horizontal_scroll_mode` = `0 (overrides ScrollContainer)`

**Methods**
- `void edit(object: Object)`
- `Object get_edited_object()`
- `String get_selected_path() const`
- `EditorProperty instantiate_property_editor(object: Object, type: Variant.Type, path: String, hint: PropertyHint, hint_text: String, usage: int, wide: bool = false) static`

### EditorInterface
*Inherits: **Object***

EditorInterface gives you control over Godot editor's window. It allows customizing the window, saving and (re-)loading scenes, rendering mesh previews, inspecting and editing resources and objects, and provides access to EditorSettings, EditorFileSystem, EditorResourcePreview, ScriptEditor, the editor viewport, and information about scenes.

**Properties**
- `bool distraction_free_mode`
- `bool movie_maker_enabled`

**Methods**
- `void add_root_node(node: Node)`
- `Error close_scene()`
- `void edit_node(node: Node)`
- `void edit_resource(resource: Resource)`
- `void edit_script(script: Script, line: int = -1, column: int = 0, grab_focus: bool = true)`
- `Control get_base_control() const`
- `EditorCommandPalette get_command_palette() const`
- `String get_current_directory() const`
- `String get_current_feature_profile() const`
- `String get_current_path() const`
- `Node get_edited_scene_root() const`
- `String get_editor_language() const`
- `VBoxContainer get_editor_main_screen() const`
- `EditorPaths get_editor_paths() const`
- `float get_editor_scale() const`
- `EditorSettings get_editor_settings() const`
- `Theme get_editor_theme() const`
- `EditorToaster get_editor_toaster() const`
- `EditorUndoRedoManager get_editor_undo_redo() const`
- `SubViewport get_editor_viewport_2d() const`
- `SubViewport get_editor_viewport_3d(idx: int = 0) const`
- `FileSystemDock get_file_system_dock() const`
- `EditorInspector get_inspector() const`
- `float get_node_3d_rotate_snap() const`
- `float get_node_3d_scale_snap() const`
- `float get_node_3d_translate_snap() const`
- `Array[Node] get_open_scene_roots() const`
- `PackedStringArray get_open_scenes() const`
- `String get_playing_scene() const`
- `EditorFileSystem get_resource_filesystem() const`
- `EditorResourcePreview get_resource_previewer() const`
- `ScriptEditor get_script_editor() const`
- `PackedStringArray get_selected_paths() const`
- `EditorSelection get_selection() const`
- `void inspect_object(object: Object, for_property: String = "", inspector_only: bool = false)`
- `bool is_multi_window_enabled() const`
- `bool is_node_3d_snap_enabled() const`
- `bool is_object_edited(object: Object) const`
- `bool is_playing_scene() const`
- `bool is_plugin_enabled(plugin: String) const`

**GDScript Examples**
```gdscript
var editor_settings = EditorInterface.get_editor_settings()
```
```gdscript
func _ready():
    if Engine.is_editor_hint():
        EditorInterface.popup_node_selector(_on_node_selected, ["Button"])

func _on_node_selected(node_path):
    if node_path.is_empty():
        print("node selection canceled")
    else:
        print("selected ", node_path)
```

### EditorNode3DGizmoPlugin
*Inherits: **Resource < RefCounted < Object***

EditorNode3DGizmoPlugin allows you to define a new type of Gizmo. There are two main ways to do so: extending EditorNode3DGizmoPlugin for the simpler gizmos, or creating a new EditorNode3DGizmo type. See the tutorial in the documentation for more info.

**Methods**
- `void _begin_handle_action(gizmo: EditorNode3DGizmo, handle_id: int, secondary: bool) virtual`
- `bool _can_be_hidden() virtual const`
- `void _commit_handle(gizmo: EditorNode3DGizmo, handle_id: int, secondary: bool, restore: Variant, cancel: bool) virtual`
- `void _commit_subgizmos(gizmo: EditorNode3DGizmo, ids: PackedInt32Array, restores: Array[Transform3D], cancel: bool) virtual`
- `EditorNode3DGizmo _create_gizmo(for_node_3d: Node3D) virtual const`
- `String _get_gizmo_name() virtual const`
- `String _get_handle_name(gizmo: EditorNode3DGizmo, handle_id: int, secondary: bool) virtual const`
- `Variant _get_handle_value(gizmo: EditorNode3DGizmo, handle_id: int, secondary: bool) virtual const`
- `int _get_priority() virtual const`
- `Transform3D _get_subgizmo_transform(gizmo: EditorNode3DGizmo, subgizmo_id: int) virtual const`
- `bool _has_gizmo(for_node_3d: Node3D) virtual const`
- `bool _is_handle_highlighted(gizmo: EditorNode3DGizmo, handle_id: int, secondary: bool) virtual const`
- `bool _is_selectable_when_hidden() virtual const`
- `void _redraw(gizmo: EditorNode3DGizmo) virtual`
- `void _set_handle(gizmo: EditorNode3DGizmo, handle_id: int, secondary: bool, camera: Camera3D, screen_pos: Vector2) virtual`
- `void _set_subgizmo_transform(gizmo: EditorNode3DGizmo, subgizmo_id: int, transform: Transform3D) virtual`
- `PackedInt32Array _subgizmos_intersect_frustum(gizmo: EditorNode3DGizmo, camera: Camera3D, frustum_planes: Array[Plane]) virtual const`
- `int _subgizmos_intersect_ray(gizmo: EditorNode3DGizmo, camera: Camera3D, screen_pos: Vector2) virtual const`
- `void add_material(name: String, material: StandardMaterial3D)`
- `void create_handle_material(name: String, billboard: bool = false, texture: Texture2D = null)`
- `void create_icon_material(name: String, texture: Texture2D, on_top: bool = false, color: Color = Color(1, 1, 1, 1))`
- `void create_material(name: String, color: Color, billboard: bool = false, on_top: bool = false, use_vertex_color: bool = false)`
- `StandardMaterial3D get_material(name: String, gizmo: EditorNode3DGizmo = null)`

### EditorNode3DGizmo
*Inherits: **Node3DGizmo < RefCounted < Object***

Gizmo that is used for providing custom visualization and editing (handles and subgizmos) for Node3D objects. Can be overridden to create custom gizmos, but for simple gizmos creating an EditorNode3DGizmoPlugin is usually recommended.

**Methods**
- `void _begin_handle_action(id: int, secondary: bool) virtual`
- `void _commit_handle(id: int, secondary: bool, restore: Variant, cancel: bool) virtual`
- `void _commit_subgizmos(ids: PackedInt32Array, restores: Array[Transform3D], cancel: bool) virtual`
- `String _get_handle_name(id: int, secondary: bool) virtual const`
- `Variant _get_handle_value(id: int, secondary: bool) virtual const`
- `Transform3D _get_subgizmo_transform(id: int) virtual const`
- `bool _is_handle_highlighted(id: int, secondary: bool) virtual const`
- `void _redraw() virtual`
- `void _set_handle(id: int, secondary: bool, camera: Camera3D, point: Vector2) virtual`
- `void _set_subgizmo_transform(id: int, transform: Transform3D) virtual`
- `PackedInt32Array _subgizmos_intersect_frustum(camera: Camera3D, frustum: Array[Plane]) virtual const`
- `int _subgizmos_intersect_ray(camera: Camera3D, point: Vector2) virtual const`
- `void add_collision_segments(segments: PackedVector3Array)`
- `void add_collision_triangles(triangles: TriangleMesh)`
- `void add_handles(handles: PackedVector3Array, material: Material, ids: PackedInt32Array, billboard: bool = false, secondary: bool = false)`
- `void add_lines(lines: PackedVector3Array, material: Material, billboard: bool = false, modulate: Color = Color(1, 1, 1, 1))`
- `void add_mesh(mesh: Mesh, material: Material = null, transform: Transform3D = Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0), skeleton: SkinReference = null)`
- `void add_unscaled_billboard(material: Material, default_scale: float = 1, modulate: Color = Color(1, 1, 1, 1))`
- `void clear()`
- `Node3D get_node_3d() const`
- `EditorNode3DGizmoPlugin get_plugin() const`
- `PackedInt32Array get_subgizmo_selection() const`
- `bool is_subgizmo_selected(id: int) const`
- `void set_hidden(hidden: bool)`
- `void set_node_3d(node: Node)`

### EditorPaths
*Inherits: **Object***

This editor-only singleton returns OS-specific paths to various data folders and files. It can be used in editor plugins to ensure files are saved in the correct location on each operating system.

**Methods**
- `String get_cache_dir() const`
- `String get_config_dir() const`
- `String get_data_dir() const`
- `String get_project_settings_dir() const`
- `String get_self_contained_file() const`
- `bool is_self_contained() const`

### EditorPlugin
*Inherits: **Node < Object** | Inherited by: GridMapEditorPlugin*

Plugins are used by the editor to extend functionality. The most common types of plugins are those which edit a given node or resource type, import plugins and export plugins. See also EditorScript to add functions to the editor.

**Methods**
- `void _apply_changes() virtual`
- `bool _build() virtual`
- `void _clear() virtual`
- `void _disable_plugin() virtual`
- `void _edit(object: Object) virtual`
- `void _enable_plugin() virtual`
- `void _forward_3d_draw_over_viewport(viewport_control: Control) virtual`
- `void _forward_3d_force_draw_over_viewport(viewport_control: Control) virtual`
- `int _forward_3d_gui_input(viewport_camera: Camera3D, event: InputEvent) virtual`
- `void _forward_canvas_draw_over_viewport(viewport_control: Control) virtual`
- `void _forward_canvas_force_draw_over_viewport(viewport_control: Control) virtual`
- `bool _forward_canvas_gui_input(event: InputEvent) virtual`
- `PackedStringArray _get_breakpoints() virtual const`
- `Texture2D _get_plugin_icon() virtual const`
- `String _get_plugin_name() virtual const`
- `Dictionary _get_state() virtual const`
- `String _get_unsaved_status(for_scene: String) virtual const`
- `void _get_window_layout(configuration: ConfigFile) virtual`
- `bool _handles(object: Object) virtual const`
- `bool _has_main_screen() virtual const`
- `void _make_visible(visible: bool) virtual`
- `PackedStringArray _run_scene(scene: String, args: PackedStringArray) virtual const`
- `void _save_external_data() virtual`
- `void _set_state(state: Dictionary) virtual`
- `void _set_window_layout(configuration: ConfigFile) virtual`
- `void add_autoload_singleton(name: String, path: String)`
- `void add_context_menu_plugin(slot: ContextMenuSlot, plugin: EditorContextMenuPlugin)`
- `Button add_control_to_bottom_panel(control: Control, title: String, shortcut: Shortcut = null)`
- `void add_control_to_container(container: CustomControlContainer, control: Control)`
- `void add_control_to_dock(slot: DockSlot, control: Control, shortcut: Shortcut = null)`
- `void add_custom_type(type: String, base: String, script: Script, icon: Texture2D)`
- `void add_debugger_plugin(script: EditorDebuggerPlugin)`
- `void add_dock(dock: EditorDock)`
- `void add_export_platform(platform: EditorExportPlatform)`
- `void add_export_plugin(plugin: EditorExportPlugin)`
- `void add_import_plugin(importer: EditorImportPlugin, first_priority: bool = false)`
- `void add_inspector_plugin(plugin: EditorInspectorPlugin)`
- `void add_node_3d_gizmo_plugin(plugin: EditorNode3DGizmoPlugin)`
- `void add_resource_conversion_plugin(plugin: EditorResourceConversionPlugin)`
- `void add_scene_format_importer_plugin(scene_format_importer: EditorSceneFormatImporter, first_priority: bool = false)`

**GDScript Examples**
```gdscript
func _forward_3d_draw_over_viewport(overlay):
    # Draw a circle at the cursor's position.
    overlay.draw_circle(overlay.get_local_mouse_position(), 64, Color.WHITE)

func _forward_3d_gui_input(camera, event):
    if event is InputEventMouseMotion:
        # Redraw the viewport when the cursor is moved.
        update_overlays()
        return EditorPlugin.AFTER_GUI_INPUT_STOP
    return EditorPlugin.AFTER_GUI_INPUT_PASS
```
```gdscript
# Prevents the InputEvent from reaching other Editor classes.
func _forward_3d_gui_input(camera, event):
    return EditorPlugin.AFTER_GUI_INPUT_STOP
```

### EditorProperty
*Inherits: **Container < Control < CanvasItem < Node < Object***

A custom control for editing properties that can be added to the EditorInspector. It is added via EditorInspectorPlugin.

**Properties**
- `bool checkable` = `false`
- `bool checked` = `false`
- `bool deletable` = `false`
- `bool draw_background` = `true`
- `bool draw_label` = `true`
- `bool draw_warning` = `false`
- `FocusMode focus_mode` = `3 (overrides Control)`
- `bool keying` = `false`
- `String label` = `""`
- `float name_split_ratio` = `0.5`
- `bool read_only` = `false`
- `bool selectable` = `true`
- `bool use_folding` = `false`

**Methods**
- `void _set_read_only(read_only: bool) virtual`
- `void _update_property() virtual`
- `void add_focusable(control: Control)`
- `void deselect()`
- `void emit_changed(property: StringName, value: Variant, field: StringName = &"", changing: bool = false)`
- `Object get_edited_object()`
- `StringName get_edited_property() const`
- `bool is_selected() const`
- `void select(focusable: int = -1)`
- `void set_bottom_editor(editor: Control)`
- `void set_label_reference(control: Control)`
- `void set_object_and_property(object: Object, property: StringName)`
- `void update_property()`

### EditorResourceConversionPlugin
*Inherits: **RefCounted < Object***

EditorResourceConversionPlugin is invoked when the context menu is brought up for a resource in the editor inspector. Relevant conversion plugins will appear as menu options to convert the given resource to a target type.

**Methods**
- `Resource _convert(resource: Resource) virtual const`
- `String _converts_to() virtual const`
- `bool _handles(resource: Resource) virtual const`

**GDScript Examples**
```gdscript
extends EditorResourceConversionPlugin

func _handles(resource: Resource):
    return resource is ImageTexture

func _converts_to():
    return "PortableCompressedTexture2D"

func _convert(itex: Resource):
    var ptex = PortableCompressedTexture2D.new()
    ptex.create_from_image(itex.get_image(), PortableCompressedTexture2D.COMPRESSION_MODE_LOSSLESS)
    return ptex
```

### EditorResourcePicker
*Inherits: **HBoxContainer < BoxContainer < Container < Control < CanvasItem < Node < Object** | Inherited by: EditorScriptPicker*

This Control node is used in the editor's Inspector dock to allow editing of Resource type properties. It provides options for creating, loading, saving and converting resources. Can be used with EditorInspectorPlugin to recreate the same behavior.

**Properties**
- `String base_type` = `""`
- `bool editable` = `true`
- `Resource edited_resource`
- `bool toggle_mode` = `false`

**Methods**
- `bool _handle_menu_selected(id: int) virtual`
- `void _set_create_options(menu_node: Object) virtual`
- `PackedStringArray get_allowed_types() const`
- `void set_toggle_pressed(pressed: bool)`

### EditorResourcePreviewGenerator
*Inherits: **RefCounted < Object***

Custom code to generate previews. Check EditorSettings.filesystem/file_dialog/thumbnail_size to find a proper size to generate previews at.

**Methods**
- `bool _can_generate_small_preview() virtual const`
- `Texture2D _generate(resource: Resource, size: Vector2i, metadata: Dictionary) virtual required const`
- `Texture2D _generate_from_path(path: String, size: Vector2i, metadata: Dictionary) virtual const`
- `bool _generate_small_preview_automatically() virtual const`
- `bool _handles(type: String) virtual required const`
- `void request_draw_and_wait(viewport: RID) const`

### EditorResourcePreview
*Inherits: **Node < Object***

This node is used to generate previews for resources or files.

**Methods**
- `void add_preview_generator(generator: EditorResourcePreviewGenerator)`
- `void check_for_invalidation(path: String)`
- `void queue_edited_resource_preview(resource: Resource, receiver: Object, receiver_func: StringName, userdata: Variant)`
- `void queue_resource_preview(path: String, receiver: Object, receiver_func: StringName, userdata: Variant)`
- `void remove_preview_generator(generator: EditorResourcePreviewGenerator)`

### EditorResourceTooltipPlugin
*Inherits: **RefCounted < Object***

Resource tooltip plugins are used by FileSystemDock to generate customized tooltips for specific resources. E.g. tooltip for a Texture2D displays a bigger preview and the texture's dimensions.

**Methods**
- `bool _handles(type: String) virtual const`
- `Control _make_tooltip_for_path(path: String, metadata: Dictionary, base: Control) virtual const`
- `void request_thumbnail(path: String, control: TextureRect) const`

**GDScript Examples**
```gdscript
func _make_tooltip_for_path(path, metadata, base):
    var t_rect = TextureRect.new()
    request_thumbnail(path, t_rect)
    base.add_child(t_rect) # The TextureRect will appear at the bottom of the tooltip.
    return base
```

### EditorSceneFormatImporterBlend
*Inherits: **EditorSceneFormatImporter < RefCounted < Object***

Imports Blender scenes in the .blend file format through the glTF 2.0 3D import pipeline. This importer requires Blender to be installed by the user, so that it can be used to export the scene as glTF 2.0.

### EditorSceneFormatImporterFBX2GLTF
*Inherits: **EditorSceneFormatImporter < RefCounted < Object***

Imports Autodesk FBX 3D scenes by way of converting them to glTF 2.0 using the FBX2glTF command line tool.

### EditorSceneFormatImporterGLTF
*Inherits: **EditorSceneFormatImporter < RefCounted < Object***

There is currently no description for this class. Please help us by contributing one!

### EditorSceneFormatImporterUFBX
*Inherits: **EditorSceneFormatImporter < RefCounted < Object***

EditorSceneFormatImporterUFBX is designed to load FBX files and supports both binary and ASCII FBX files from version 3000 onward. This class supports various 3D object types like meshes, skins, blend shapes, materials, and rigging information. The class aims for feature parity with the official FBX SDK and supports FBX 7.4 specifications.

### EditorSceneFormatImporter
*Inherits: **RefCounted < Object** | Inherited by: EditorSceneFormatImporterBlend, EditorSceneFormatImporterFBX2GLTF, EditorSceneFormatImporterGLTF, EditorSceneFormatImporterUFBX*

EditorSceneFormatImporter allows to define an importer script for a third-party 3D format.

**Methods**
- `PackedStringArray _get_extensions() virtual required const`
- `void _get_import_options(path: String) virtual`
- `Variant _get_option_visibility(path: String, for_animation: bool, option: String) virtual const`
- `Object _import_scene(path: String, flags: int, options: Dictionary) virtual required`
- `void add_import_option(name: String, value: Variant)`
- `void add_import_option_advanced(type: Variant.Type, name: String, default_value: Variant, hint: PropertyHint = 0, hint_string: String = "", usage_flags: int = 6)`

### EditorScenePostImportPlugin
*Inherits: **RefCounted < Object***

This plugin type exists to modify the process of importing scenes, allowing to change the content as well as add importer options at every stage of the process.

**Methods**
- `void _get_import_options(path: String) virtual`
- `void _get_internal_import_options(category: int) virtual`
- `Variant _get_internal_option_update_view_required(category: int, option: String) virtual const`
- `Variant _get_internal_option_visibility(category: int, for_animation: bool, option: String) virtual const`
- `Variant _get_option_visibility(path: String, for_animation: bool, option: String) virtual const`
- `void _internal_process(category: int, base_node: Node, node: Node, resource: Resource) virtual`
- `void _post_process(scene: Node) virtual`
- `void _pre_process(scene: Node) virtual`
- `void add_import_option(name: String, value: Variant)`
- `void add_import_option_advanced(type: Variant.Type, name: String, default_value: Variant, hint: PropertyHint = 0, hint_string: String = "", usage_flags: int = 6)`
- `Variant get_option_value(name: StringName) const`

### EditorScenePostImport
*Inherits: **RefCounted < Object***

Imported scenes can be automatically modified right after import by setting their Custom Script Import property to a tool script that inherits from this class.

**Methods**
- `Object _post_import(scene: Node) virtual`
- `String get_source_file() const`

**GDScript Examples**
```gdscript
@tool # Needed so it runs in editor.
extends EditorScenePostImport

# This sample changes all node names.
# Called right after the scene is imported and gets the root node.
func _post_import(scene):
    # Change all node names to "modified_[oldnodename]"
    iterate(scene)
    return scene # Remember to return the imported scene

func iterate(node):
    if node != null:
        node.name = "modified_" + node.name
        for child in node.get_children():
            iterate(child)
```

### EditorScriptPicker
*Inherits: **EditorResourcePicker < HBoxContainer < BoxContainer < Container < Control < CanvasItem < Node < Object***

Similar to EditorResourcePicker this Control node is used in the editor's Inspector dock, but only to edit the script property of a Node. Default options for creating new resources of all possible subtypes are replaced with dedicated buttons that open the "Attach Node Script" dialog. Can be used with EditorInspectorPlugin to recreate the same behavior.

**Properties**
- `Node script_owner`

### EditorScript
*Inherits: **RefCounted < Object***

Scripts extending this class and implementing its _run() method can be executed from the Script Editor's File > Run menu option (or by pressing Ctrl + Shift + X) while the editor is running. This is useful for adding custom in-editor functionality to Godot. For more complex additions, consider using EditorPlugins instead.

**Methods**
- `void _run() virtual required`
- `void add_root_node(node: Node)`
- `EditorInterface get_editor_interface() const`
- `Node get_scene() const`

**GDScript Examples**
```gdscript
@tool
extends EditorScript

func _run():
    print("Hello from the Godot Editor!")
```

### EditorSelection
*Inherits: **Object***

This object manages the SceneTree selection in the editor.

**Methods**
- `void add_node(node: Node)`
- `void clear()`
- `Array[Node] get_selected_nodes()`
- `Array[Node] get_top_selected_nodes()`
- `Array[Node] get_transformable_selected_nodes()`
- `void remove_node(node: Node)`

### EditorSpinSlider
*Inherits: **Range < Control < CanvasItem < Node < Object***

This Control node is used in the editor's Inspector dock to allow editing of numeric values. Can be used with EditorInspectorPlugin to recreate the same behavior.

**Properties**
- `ControlState control_state` = `0`
- `bool editing_integer` = `false`
- `bool flat` = `false`
- `FocusMode focus_mode` = `2 (overrides Control)`
- `bool hide_slider` = `false`
- `String label` = `""`
- `bool read_only` = `false`
- `BitField[SizeFlags] size_flags_vertical` = `1 (overrides Control)`
- `float step` = `1.0 (overrides Range)`
- `String suffix` = `""`

### EditorSyntaxHighlighter
*Inherits: **SyntaxHighlighter < Resource < RefCounted < Object** | Inherited by: GDScriptSyntaxHighlighter*

Base class that all SyntaxHighlighters used by the ScriptEditor extend from.

**Methods**
- `EditorSyntaxHighlighter _create() virtual const`
- `String _get_name() virtual const`
- `PackedStringArray _get_supported_languages() virtual const`

### EditorToaster
*Inherits: **HBoxContainer < BoxContainer < Container < Control < CanvasItem < Node < Object***

This object manages the functionality and display of toast notifications within the editor, ensuring immediate and informative alerts are presented to the user.

**Methods**
- `void push_toast(message: String, severity: Severity = 0, tooltip: String = "")`

### EditorTranslationParserPlugin
*Inherits: **RefCounted < Object***

EditorTranslationParserPlugin is invoked when a file is being parsed to extract strings that require translation. To define the parsing and string extraction logic, override the _parse_file() method in script.

**Methods**
- `PackedStringArray _get_recognized_extensions() virtual const`
- `Array[PackedStringArray] _parse_file(path: String) virtual`

**GDScript Examples**
```gdscript
@tool
extends EditorTranslationParserPlugin

func _parse_file(path):
    var ret: Array[PackedStringArray] = []
    var file = FileAccess.open(path, FileAccess.READ)
    var text = file.get_as_text()
    var split_strs = text.split(",", false)
    for s in split_strs:
        ret.append(PackedStringArray([s]))
        #print("Extracted string: " + s)

    return ret

func _get_recognized_extensions():
    return ["csv"]
```
```gdscript
# This will add a message with msgid "Test 1", msgctxt "context", msgid_plural "test 1 plurals", comment "test 1 comment", and source line "7".
ret.append(PackedStringArray(["Test 1", "context", "test 1 plurals", "test 1 comment", "7"]))
# This will add a message with msgid "A test without context" and msgid_plural "plurals".
ret.append(PackedStringArray(["A test without context", "", "plurals"]))
# This will add a message with msgid "Only with context" and msgctxt "a friendly context".
ret.append(PackedStringArray(["Only with context", "a friendly context"]))
```

### EditorUndoRedoManager
*Inherits: **Object***

EditorUndoRedoManager is a manager for UndoRedo objects associated with edited scenes. Each scene has its own undo history and EditorUndoRedoManager ensures that each action performed in the editor gets associated with a proper scene. For actions not related to scenes (ProjectSettings edits, external resources, etc.), a separate global history is used.

**Methods**
- `void add_do_method(object: Object, method: StringName, ...) vararg`
- `void add_do_property(object: Object, property: StringName, value: Variant)`
- `void add_do_reference(object: Object)`
- `void add_undo_method(object: Object, method: StringName, ...) vararg`
- `void add_undo_property(object: Object, property: StringName, value: Variant)`
- `void add_undo_reference(object: Object)`
- `void clear_history(id: int = -99, increase_version: bool = true)`
- `void commit_action(execute: bool = true)`
- `void create_action(name: String, merge_mode: MergeMode = 0, custom_context: Object = null, backward_undo_ops: bool = false, mark_unsaved: bool = true)`
- `void force_fixed_history()`
- `UndoRedo get_history_undo_redo(id: int) const`
- `int get_object_history_id(object: Object) const`
- `bool is_committing_action() const`

**GDScript Examples**
```gdscript
var scene_root = EditorInterface.get_edited_scene_root()
var undo_redo = EditorInterface.get_editor_undo_redo()
undo_redo.clear_history(undo_redo.get_object_history_id(scene_root))
```

### EditorVCSInterface
*Inherits: **Object***

Defines the API that the editor uses to extract information from the underlying VCS. The implementation of this API is included in VCS plugins, which are GDExtension plugins that inherit EditorVCSInterface and are attached (on demand) to the singleton instance of EditorVCSInterface. Instead of performing the task themselves, all the virtual functions listed below are calling the internally overridden functions in the VCS plugins to provide a plug-n-play experience. A custom VCS plugin is supposed to inherit from EditorVCSInterface and override each of these virtual functions.

**Methods**
- `bool _checkout_branch(branch_name: String) virtual required`
- `void _commit(msg: String) virtual required`
- `void _create_branch(branch_name: String) virtual required`
- `void _create_remote(remote_name: String, remote_url: String) virtual required`
- `void _discard_file(file_path: String) virtual required`
- `void _fetch(remote: String) virtual required`
- `Array[String] _get_branch_list() virtual required`
- `String _get_current_branch_name() virtual required`
- `Array[Dictionary] _get_diff(identifier: String, area: int) virtual required`
- `Array[Dictionary] _get_line_diff(file_path: String, text: String) virtual required`
- `Array[Dictionary] _get_modified_files_data() virtual required`
- `Array[Dictionary] _get_previous_commits(max_commits: int) virtual required`
- `Array[String] _get_remotes() virtual required`
- `String _get_vcs_name() virtual required`
- `bool _initialize(project_path: String) virtual required`
- `void _pull(remote: String) virtual required`
- `void _push(remote: String, force: bool) virtual required`
- `void _remove_branch(branch_name: String) virtual required`
- `void _remove_remote(remote_name: String) virtual required`
- `void _set_credentials(username: String, password: String, ssh_public_key_path: String, ssh_private_key_path: String, ssh_passphrase: String) virtual required`
- `bool _shut_down() virtual required`
- `void _stage_file(file_path: String) virtual required`
- `void _unstage_file(file_path: String) virtual required`
- `Dictionary add_diff_hunks_into_diff_file(diff_file: Dictionary, diff_hunks: Array[Dictionary])`
- `Dictionary add_line_diffs_into_diff_hunk(diff_hunk: Dictionary, line_diffs: Array[Dictionary])`
- `Dictionary create_commit(msg: String, author: String, id: String, unix_timestamp: int, offset_minutes: int)`
- `Dictionary create_diff_file(new_file: String, old_file: String)`
- `Dictionary create_diff_hunk(old_start: int, new_start: int, old_lines: int, new_lines: int)`
- `Dictionary create_diff_line(new_line_no: int, old_line_no: int, content: String, status: String)`
- `Dictionary create_status_file(file_path: String, change_type: ChangeType, area: TreeArea)`
- `void popup_error(msg: String)`
