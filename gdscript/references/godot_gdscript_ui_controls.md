# Godot 4 GDScript API Reference — Ui Controls

> GDScript-only reference. 54 classes.

### AcceptDialog
*Inherits: **Window < Viewport < Node < Object** | Inherited by: ConfirmationDialog*

The default use of AcceptDialog is to allow it to only be accepted or closed, with the same result. However, the confirmed and canceled signals allow to make the two actions different, and the add_button() method allows to add custom buttons and actions.

**Properties**
- `bool dialog_autowrap` = `false`
- `bool dialog_close_on_escape` = `true`
- `bool dialog_hide_on_ok` = `true`
- `String dialog_text` = `""`
- `bool exclusive` = `true (overrides Window)`
- `bool keep_title_visible` = `true (overrides Window)`
- `bool maximize_disabled` = `true (overrides Window)`
- `bool minimize_disabled` = `true (overrides Window)`
- `String ok_button_text` = `""`
- `String title` = `"Alert!" (overrides Window)`
- `bool transient` = `true (overrides Window)`
- `bool visible` = `false (overrides Window)`
- `bool wrap_controls` = `true (overrides Window)`

**Methods**
- `Button add_button(text: String, right: bool = false, action: String = "")`
- `Button add_cancel_button(name: String)`
- `Label get_label()`
- `Button get_ok_button()`
- `void register_text_enter(line_edit: LineEdit)`
- `void remove_button(button: Button)`

### AspectRatioContainer
*Inherits: **Container < Control < CanvasItem < Node < Object***

A container type that arranges its child controls in a way that preserves their proportions automatically when the container is resized. Useful when a container has a dynamic size and the child nodes must adjust their sizes accordingly without losing their aspect ratios.

**Properties**
- `AlignmentMode alignment_horizontal` = `1`
- `AlignmentMode alignment_vertical` = `1`
- `float ratio` = `1.0`
- `StretchMode stretch_mode` = `2`

### BaseButton
*Inherits: **Control < CanvasItem < Node < Object** | Inherited by: Button, LinkButton, TextureButton*

BaseButton is an abstract base class for GUI buttons. It doesn't display anything by itself.

**Properties**
- `ActionMode action_mode` = `1`
- `ButtonGroup button_group`
- `BitField[MouseButtonMask] button_mask` = `1`
- `bool button_pressed` = `false`
- `bool disabled` = `false`
- `FocusMode focus_mode` = `2 (overrides Control)`
- `bool keep_pressed_outside` = `false`
- `Shortcut shortcut`
- `bool shortcut_feedback` = `true`
- `bool shortcut_in_tooltip` = `true`
- `bool toggle_mode` = `false`

**Methods**
- `void _pressed() virtual`
- `void _toggled(toggled_on: bool) virtual`
- `DrawMode get_draw_mode() const`
- `bool is_hovered() const`
- `void set_pressed_no_signal(pressed: bool)`

### BoxContainer
*Inherits: **Container < Control < CanvasItem < Node < Object** | Inherited by: HBoxContainer, VBoxContainer*

A container that arranges its child controls horizontally or vertically, rearranging them automatically when their minimum size changes.

**Properties**
- `AlignmentMode alignment` = `0`
- `bool vertical` = `false`

**Methods**
- `Control add_spacer(begin: bool)`

### ButtonGroup
*Inherits: **Resource < RefCounted < Object***

A group of BaseButton-derived buttons. The buttons in a ButtonGroup are treated like radio buttons: No more than one button can be pressed at a time. Some types of buttons (such as CheckBox) may have a special appearance in this state.

**Properties**
- `bool allow_unpress` = `false`
- `bool resource_local_to_scene` = `true (overrides Resource)`

**Methods**
- `Array[BaseButton] get_buttons()`
- `BaseButton get_pressed_button()`

### Button
*Inherits: **BaseButton < Control < CanvasItem < Node < Object** | Inherited by: CheckBox, CheckButton, ColorPickerButton, MenuButton, OptionButton*

Button is the standard themed button. It can contain text and an icon, and it will display them according to the current Theme.

**Properties**
- `HorizontalAlignment alignment` = `1`
- `AutowrapMode autowrap_mode` = `0`
- `BitField[LineBreakFlag] autowrap_trim_flags` = `128`
- `bool clip_text` = `false`
- `bool expand_icon` = `false`
- `bool flat` = `false`
- `Texture2D icon`
- `HorizontalAlignment icon_alignment` = `0`
- `String language` = `""`
- `String text` = `""`
- `TextDirection text_direction` = `0`
- `OverrunBehavior text_overrun_behavior` = `0`
- `VerticalAlignment vertical_icon_alignment` = `1`

**GDScript Examples**
```gdscript
func _ready():
    var button = Button.new()
    button.text = "Click me"
    button.pressed.connect(_button_pressed)
    add_child(button)

func _button_pressed():
    print("Hello world!")
```

### CenterContainer
*Inherits: **Container < Control < CanvasItem < Node < Object***

CenterContainer is a container that keeps all of its child controls in its center at their minimum size.

**Properties**
- `bool use_top_left` = `false`

### CheckBox
*Inherits: **Button < BaseButton < Control < CanvasItem < Node < Object***

CheckBox allows the user to choose one of only two possible options. It's similar to CheckButton in functionality, but it has a different appearance. To follow established UX patterns, it's recommended to use CheckBox when toggling it has no immediate effect on something. For example, it could be used when toggling it will only do something once a confirmation button is pressed.

**Properties**
- `HorizontalAlignment alignment` = `0 (overrides Button)`
- `bool toggle_mode` = `true (overrides BaseButton)`

### CheckButton
*Inherits: **Button < BaseButton < Control < CanvasItem < Node < Object***

CheckButton is a toggle button displayed as a check field. It's similar to CheckBox in functionality, but it has a different appearance. To follow established UX patterns, it's recommended to use CheckButton when toggling it has an immediate effect on something. For example, it can be used when pressing it shows or hides advanced settings, without asking the user to confirm this action.

**Properties**
- `HorizontalAlignment alignment` = `0 (overrides Button)`
- `bool toggle_mode` = `true (overrides BaseButton)`

### CodeEdit
*Inherits: **TextEdit < Control < CanvasItem < Node < Object***

CodeEdit is a specialized TextEdit designed for editing plain text code files. It has many features commonly found in code editors such as line numbers, line folding, code completion, indent management, and string/comment management.

**Properties**
- `bool auto_brace_completion_enabled` = `false`
- `bool auto_brace_completion_highlight_matching` = `false`
- `Dictionary auto_brace_completion_pairs` = `{ "\"": "\"", "'": "'", "(": ")", "[": "]", "{": "}" }`
- `bool code_completion_enabled` = `false`
- `Array[String] code_completion_prefixes` = `[]`
- `Array[String] delimiter_comments` = `[]`
- `Array[String] delimiter_strings` = `["' '", "\" \""]`
- `bool gutters_draw_bookmarks` = `false`
- `bool gutters_draw_breakpoints_gutter` = `false`
- `bool gutters_draw_executing_lines` = `false`
- `bool gutters_draw_fold_gutter` = `false`
- `bool gutters_draw_line_numbers` = `false`
- `int gutters_line_numbers_min_digits` = `3`
- `bool gutters_zero_pad_line_numbers` = `false`
- `bool indent_automatic` = `false`
- `Array[String] indent_automatic_prefixes` = `[":", "{", "[", "("]`
- `int indent_size` = `4`
- `bool indent_use_spaces` = `false`
- `LayoutDirection layout_direction` = `2 (overrides Control)`
- `bool line_folding` = `false`
- `Array[int] line_length_guidelines` = `[]`
- `bool symbol_lookup_on_click` = `false`
- `bool symbol_tooltip_on_hover` = `false`
- `TextDirection text_direction` = `1 (overrides TextEdit)`

**Methods**
- `void _confirm_code_completion(replace: bool) virtual`
- `Array[Dictionary] _filter_code_completion_candidates(candidates: Array[Dictionary]) virtual const`
- `void _request_code_completion(force: bool) virtual`
- `void add_auto_brace_completion_pair(start_key: String, end_key: String)`
- `void add_code_completion_option(type: CodeCompletionKind, display_text: String, insert_text: String, text_color: Color = Color(1, 1, 1, 1), icon: Resource = null, value: Variant = null, location: int = 1024)`
- `void add_comment_delimiter(start_key: String, end_key: String, line_only: bool = false)`
- `void add_string_delimiter(start_key: String, end_key: String, line_only: bool = false)`
- `bool can_fold_line(line: int) const`
- `void cancel_code_completion()`
- `void clear_bookmarked_lines()`
- `void clear_breakpointed_lines()`
- `void clear_comment_delimiters()`
- `void clear_executing_lines()`
- `void clear_string_delimiters()`
- `void confirm_code_completion(replace: bool = false)`
- `void convert_indent(from_line: int = -1, to_line: int = -1)`
- `void create_code_region()`
- `void delete_lines()`
- `void do_indent()`
- `void duplicate_lines()`
- `void duplicate_selection()`
- `void fold_all_lines()`
- `void fold_line(line: int)`
- `String get_auto_brace_completion_close_key(open_key: String) const`
- `PackedInt32Array get_bookmarked_lines() const`
- `PackedInt32Array get_breakpointed_lines() const`
- `Dictionary get_code_completion_option(index: int) const`
- `Array[Dictionary] get_code_completion_options() const`
- `int get_code_completion_selected_index() const`
- `String get_code_region_end_tag() const`
- `String get_code_region_start_tag() const`
- `String get_delimiter_end_key(delimiter_index: int) const`
- `Vector2 get_delimiter_end_position(line: int, column: int) const`
- `String get_delimiter_start_key(delimiter_index: int) const`
- `Vector2 get_delimiter_start_position(line: int, column: int) const`
- `PackedInt32Array get_executing_lines() const`
- `Array[int] get_folded_lines() const`
- `String get_text_for_code_completion() const`
- `String get_text_for_symbol_lookup() const`
- `String get_text_with_cursor_char(line: int, column: int) const`

### ColorPickerButton
*Inherits: **Button < BaseButton < Control < CanvasItem < Node < Object***

Encapsulates a ColorPicker, making it accessible by pressing a button. Pressing the button will toggle the ColorPicker's visibility.

**Properties**
- `Color color` = `Color(0, 0, 0, 1)`
- `bool edit_alpha` = `true`
- `bool edit_intensity` = `true`
- `bool toggle_mode` = `true (overrides BaseButton)`

**Methods**
- `ColorPicker get_picker()`
- `PopupPanel get_popup()`

### ColorPicker
*Inherits: **VBoxContainer < BoxContainer < Container < Control < CanvasItem < Node < Object***

A widget that provides an interface for selecting or modifying a color. It can optionally provide functionalities like a color sampler (eyedropper), color modes, and presets.

**Properties**
- `bool can_add_swatches` = `true`
- `Color color` = `Color(1, 1, 1, 1)`
- `ColorModeType color_mode` = `0`
- `bool color_modes_visible` = `true`
- `bool deferred_mode` = `false`
- `bool edit_alpha` = `true`
- `bool edit_intensity` = `true`
- `bool hex_visible` = `true`
- `PickerShapeType picker_shape` = `0`
- `bool presets_visible` = `true`
- `bool sampler_visible` = `true`
- `bool sliders_visible` = `true`

**Methods**
- `void add_preset(color: Color)`
- `void add_recent_preset(color: Color)`
- `void erase_preset(color: Color)`
- `void erase_recent_preset(color: Color)`
- `PackedColorArray get_presets() const`
- `PackedColorArray get_recent_presets() const`

### ColorRect
*Inherits: **Control < CanvasItem < Node < Object***

Displays a rectangle filled with a solid color. If you need to display the border alone, consider using a Panel instead.

**Properties**
- `Color color` = `Color(1, 1, 1, 1)`

### ConfirmationDialog
*Inherits: **AcceptDialog < Window < Viewport < Node < Object** | Inherited by: EditorCommandPalette, FileDialog, ScriptCreateDialog*

A dialog used for confirmation of actions. This window is similar to AcceptDialog, but pressing its Cancel button can have a different outcome from pressing the OK button. The order of the two buttons varies depending on the host OS.

**Properties**
- `String cancel_button_text` = `"Cancel"`
- `Vector2i min_size` = `Vector2i(200, 70) (overrides Window)`
- `Vector2i size` = `Vector2i(200, 100) (overrides Window)`
- `String title` = `"Please Confirm..." (overrides Window)`

**Methods**
- `Button get_cancel_button()`

**GDScript Examples**
```gdscript
get_cancel_button().pressed.connect(_on_canceled)
```

### Container
*Inherits: **Control < CanvasItem < Node < Object** | Inherited by: AspectRatioContainer, BoxContainer, CenterContainer, EditorProperty, FlowContainer, FoldableContainer, ...*

Base class for all GUI containers. A Container automatically arranges its child controls in a certain way. This class can be inherited to make custom container types.

**Properties**
- `MouseFilter mouse_filter` = `1 (overrides Control)`

**Methods**
- `PackedInt32Array _get_allowed_size_flags_horizontal() virtual const`
- `PackedInt32Array _get_allowed_size_flags_vertical() virtual const`
- `void fit_child_in_rect(child: Control, rect: Rect2)`
- `void queue_sort()`

### Control
*Inherits: **CanvasItem < Node < Object** | Inherited by: BaseButton, ColorRect, Container, GraphEdit, ItemList, Label, ...*

Base class for all UI-related nodes. Control features a bounding rectangle that defines its extents, an anchor position relative to its parent control or the current viewport, and offsets relative to the anchor. The offsets update automatically when the node, any of its parents, or the screen size change.

**Properties**
- `Array[NodePath] accessibility_controls_nodes` = `[]`
- `Array[NodePath] accessibility_described_by_nodes` = `[]`
- `String accessibility_description` = `""`
- `Array[NodePath] accessibility_flow_to_nodes` = `[]`
- `Array[NodePath] accessibility_labeled_by_nodes` = `[]`
- `AccessibilityLiveMode accessibility_live` = `0`
- `String accessibility_name` = `""`
- `float anchor_bottom` = `0.0`
- `float anchor_left` = `0.0`
- `float anchor_right` = `0.0`
- `float anchor_top` = `0.0`
- `bool auto_translate`
- `bool clip_contents` = `false`
- `Vector2 custom_minimum_size` = `Vector2(0, 0)`
- `FocusBehaviorRecursive focus_behavior_recursive` = `0`
- `FocusMode focus_mode` = `0`
- `NodePath focus_neighbor_bottom` = `NodePath("")`
- `NodePath focus_neighbor_left` = `NodePath("")`
- `NodePath focus_neighbor_right` = `NodePath("")`
- `NodePath focus_neighbor_top` = `NodePath("")`
- `NodePath focus_next` = `NodePath("")`
- `NodePath focus_previous` = `NodePath("")`
- `Vector2 global_position`
- `GrowDirection grow_horizontal` = `1`
- `GrowDirection grow_vertical` = `1`
- `LayoutDirection layout_direction` = `0`
- `bool localize_numeral_system` = `true`
- `MouseBehaviorRecursive mouse_behavior_recursive` = `0`
- `CursorShape mouse_default_cursor_shape` = `0`
- `MouseFilter mouse_filter` = `0`

**Methods**
- `String _accessibility_get_contextual_info() virtual const`
- `bool _can_drop_data(at_position: Vector2, data: Variant) virtual const`
- `void _drop_data(at_position: Vector2, data: Variant) virtual`
- `String _get_accessibility_container_name(node: Node) virtual const`
- `Variant _get_drag_data(at_position: Vector2) virtual`
- `Vector2 _get_minimum_size() virtual const`
- `String _get_tooltip(at_position: Vector2) virtual const`
- `void _gui_input(event: InputEvent) virtual`
- `bool _has_point(point: Vector2) virtual const`
- `Object _make_custom_tooltip(for_text: String) virtual const`
- `Array[Vector3i] _structured_text_parser(args: Array, text: String) virtual const`
- `void accept_event()`
- `void accessibility_drag()`
- `void accessibility_drop()`
- `void add_theme_color_override(name: StringName, color: Color)`
- `void add_theme_constant_override(name: StringName, constant: int)`
- `void add_theme_font_override(name: StringName, font: Font)`
- `void add_theme_font_size_override(name: StringName, font_size: int)`
- `void add_theme_icon_override(name: StringName, texture: Texture2D)`
- `void add_theme_stylebox_override(name: StringName, stylebox: StyleBox)`
- `void begin_bulk_theme_override()`
- `void end_bulk_theme_override()`
- `Control find_next_valid_focus() const`
- `Control find_prev_valid_focus() const`
- `Control find_valid_focus_neighbor(side: Side) const`
- `void force_drag(data: Variant, preview: Control)`
- `float get_anchor(side: Side) const`
- `Vector2 get_begin() const`
- `Vector2 get_combined_minimum_size() const`
- `Vector2 get_combined_pivot_offset() const`
- `CursorShape get_cursor_shape(position: Vector2 = Vector2(0, 0)) const`
- `Vector2 get_end() const`
- `FocusMode get_focus_mode_with_override() const`
- `NodePath get_focus_neighbor(side: Side) const`
- `Rect2 get_global_rect() const`
- `Vector2 get_minimum_size() const`
- `MouseFilter get_mouse_filter_with_override() const`
- `float get_offset(offset: Side) const`
- `Vector2 get_parent_area_size() const`
- `Control get_parent_control() const`

**GDScript Examples**
```gdscript
var style_box = StyleBoxFlat.new()
style_box.set_bg_color(Color(1, 1, 0))
style_box.set_border_width_all(2)
# We assume here that the `theme` property has been assigned a custom Theme beforehand.
theme.set_stylebox("panel", "TooltipPanel", style_box)
theme.set_color("font_color", "TooltipLabel", Color(0, 1, 1))
```
```gdscript
func _can_drop_data(position, data):
    # Check position if it is relevant to you
    # Otherwise, just check data
    return typeof(data) == TYPE_DICTIONARY and data.has("expected")
```

### FileDialog
*Inherits: **ConfirmationDialog < AcceptDialog < Window < Viewport < Node < Object** | Inherited by: EditorFileDialog*

FileDialog is a preset dialog used to choose files and directories in the filesystem. It supports filter masks. FileDialog automatically sets its window title according to the file_mode. If you want to use a custom title, disable this by setting mode_overrides_title to false.

**Properties**
- `Access access` = `0`
- `String current_dir`
- `String current_file`
- `String current_path`
- `bool deleting_enabled` = `true`
- `bool dialog_hide_on_ok` = `false (overrides AcceptDialog)`
- `DisplayMode display_mode` = `0`
- `bool favorites_enabled` = `true`
- `bool file_filter_toggle_enabled` = `true`
- `FileMode file_mode` = `4`
- `bool file_sort_options_enabled` = `true`
- `String filename_filter` = `""`
- `PackedStringArray filters` = `PackedStringArray()`
- `bool folder_creation_enabled` = `true`
- `bool hidden_files_toggle_enabled` = `true`
- `bool layout_toggle_enabled` = `true`
- `bool mode_overrides_title` = `true`
- `int option_count` = `0`
- `bool overwrite_warning_enabled` = `true`
- `bool recent_list_enabled` = `true`
- `String root_subfolder` = `""`
- `bool show_hidden_files` = `false`
- `Vector2i size` = `Vector2i(640, 360) (overrides Window)`
- `String title` = `"Save a File" (overrides Window)`
- `bool use_native_dialog` = `false`

**Methods**
- `void add_filter(filter: String, description: String = "", mime_type: String = "")`
- `void add_option(name: String, values: PackedStringArray, default_value_index: int)`
- `void clear_filename_filter()`
- `void clear_filters()`
- `void deselect_all()`
- `PackedStringArray get_favorite_list() static`
- `LineEdit get_line_edit()`
- `int get_option_default(option: int) const`
- `String get_option_name(option: int) const`
- `PackedStringArray get_option_values(option: int) const`
- `PackedStringArray get_recent_list() static`
- `Dictionary get_selected_options() const`
- `VBoxContainer get_vbox()`
- `void invalidate()`
- `bool is_customization_flag_enabled(flag: Customization) const`
- `void popup_file_dialog()`
- `void set_customization_flag_enabled(flag: Customization, enabled: bool)`
- `void set_favorite_list(favorites: PackedStringArray) static`
- `void set_get_icon_callback(callback: Callable) static`
- `void set_get_thumbnail_callback(callback: Callable) static`
- `void set_option_default(option: int, default_value_index: int)`
- `void set_option_name(option: int, name: String)`
- `void set_option_values(option: int, values: PackedStringArray)`
- `void set_recent_list(recents: PackedStringArray) static`

**GDScript Examples**
```gdscript
func _ready():
    FileDialog.set_get_thumbnail_callback(thumbnail_method)

func thumbnail_method(path):
    var image_texture = ImageTexture.new()
    make_thumbnail_async(path, image_texture)
    return image_texture

func make_thumbnail_async(path, image_texture):
    var thumbnail_texture = await generate_thumbnail(path) # Some method that generates a thumbnail.
    image_texture.set_image(thumbnail_texture.get_image())
```

### FlowContainer
*Inherits: **Container < Control < CanvasItem < Node < Object** | Inherited by: HFlowContainer, VFlowContainer*

A container that arranges its child controls horizontally or vertically and wraps them around at the borders. This is similar to how text in a book wraps around when no more words can fit on a line.

**Properties**
- `AlignmentMode alignment` = `0`
- `LastWrapAlignmentMode last_wrap_alignment` = `0`
- `bool reverse_fill` = `false`
- `bool vertical` = `false`

**Methods**
- `int get_line_count() const`

### GraphEdit
*Inherits: **Control < CanvasItem < Node < Object***

GraphEdit provides tools for creation, manipulation, and display of various graphs. Its main purpose in the engine is to power the visual programming systems, such as visual shaders, but it is also available for use in user projects.

**Properties**
- `bool clip_contents` = `true (overrides Control)`
- `bool connection_lines_antialiased` = `true`
- `float connection_lines_curvature` = `0.5`
- `float connection_lines_thickness` = `4.0`
- `Array[Dictionary] connections` = `[]`
- `FocusMode focus_mode` = `2 (overrides Control)`
- `GridPattern grid_pattern` = `0`
- `bool minimap_enabled` = `true`
- `float minimap_opacity` = `0.65`
- `Vector2 minimap_size` = `Vector2(240, 160)`
- `PanningScheme panning_scheme` = `0`
- `bool right_disconnects` = `false`
- `Vector2 scroll_offset` = `Vector2(0, 0)`
- `bool show_arrange_button` = `true`
- `bool show_grid` = `true`
- `bool show_grid_buttons` = `true`
- `bool show_menu` = `true`
- `bool show_minimap_button` = `true`
- `bool show_zoom_buttons` = `true`
- `bool show_zoom_label` = `false`
- `int snapping_distance` = `20`
- `bool snapping_enabled` = `true`
- `Dictionary type_names` = `{}`
- `float zoom` = `1.0`
- `float zoom_max` = `2.0736003`
- `float zoom_min` = `0.23256795`
- `float zoom_step` = `1.2`

**Methods**
- `PackedVector2Array _get_connection_line(from_position: Vector2, to_position: Vector2) virtual const`
- `bool _is_in_input_hotzone(in_node: Object, in_port: int, mouse_position: Vector2) virtual`
- `bool _is_in_output_hotzone(in_node: Object, in_port: int, mouse_position: Vector2) virtual`
- `bool _is_node_hover_valid(from_node: StringName, from_port: int, to_node: StringName, to_port: int) virtual`
- `void add_valid_connection_type(from_type: int, to_type: int)`
- `void add_valid_left_disconnect_type(type: int)`
- `void add_valid_right_disconnect_type(type: int)`
- `void arrange_nodes()`
- `void attach_graph_element_to_frame(element: StringName, frame: StringName)`
- `void clear_connections()`
- `Error connect_node(from_node: StringName, from_port: int, to_node: StringName, to_port: int, keep_alive: bool = false)`
- `void detach_graph_element_from_frame(element: StringName)`
- `void disconnect_node(from_node: StringName, from_port: int, to_node: StringName, to_port: int)`
- `void force_connection_drag_end()`
- `Array[StringName] get_attached_nodes_of_frame(frame: StringName)`
- `Dictionary get_closest_connection_at_point(point: Vector2, max_distance: float = 4.0) const`
- `int get_connection_count(from_node: StringName, from_port: int)`
- `PackedVector2Array get_connection_line(from_node: Vector2, to_node: Vector2) const`
- `Array[Dictionary] get_connection_list_from_node(node: StringName) const`
- `Array[Dictionary] get_connections_intersecting_with_rect(rect: Rect2) const`
- `GraphFrame get_element_frame(element: StringName)`
- `HBoxContainer get_menu_hbox()`
- `bool is_node_connected(from_node: StringName, from_port: int, to_node: StringName, to_port: int)`
- `bool is_valid_connection_type(from_type: int, to_type: int) const`
- `void remove_valid_connection_type(from_type: int, to_type: int)`
- `void remove_valid_left_disconnect_type(type: int)`
- `void remove_valid_right_disconnect_type(type: int)`
- `void set_connection_activity(from_node: StringName, from_port: int, to_node: StringName, to_port: int, amount: float)`
- `void set_selected(node: Node)`

**GDScript Examples**
```gdscript
func _is_node_hover_valid(from, from_port, to, to_port):
    return from != to
```
```gdscript
var connection = get_closest_connection_at_point(mouse_event.get_position())
```

### GraphFrame
*Inherits: **GraphElement < Container < Control < CanvasItem < Node < Object***

GraphFrame is a special GraphElement to which other GraphElements can be attached. It can be configured to automatically resize to enclose all attached GraphElements. If the frame is moved, all the attached GraphElements inside it will be moved as well.

**Properties**
- `bool autoshrink_enabled` = `true`
- `int autoshrink_margin` = `40`
- `int drag_margin` = `16`
- `MouseFilter mouse_filter` = `0 (overrides Control)`
- `Color tint_color` = `Color(0.3, 0.3, 0.3, 0.75)`
- `bool tint_color_enabled` = `false`
- `String title` = `""`

**Methods**
- `HBoxContainer get_titlebar_hbox()`

### GraphNode
*Inherits: **GraphElement < Container < Control < CanvasItem < Node < Object***

GraphNode allows to create nodes for a GraphEdit graph with customizable content based on its child controls. GraphNode is derived from Container and it is responsible for placing its children on screen. This works similar to VBoxContainer. Children, in turn, provide GraphNode with so-called slots, each of which can have a connection port on either side.

**Properties**
- `FocusMode focus_mode` = `3 (overrides Control)`
- `bool ignore_invalid_connection_type` = `false`
- `MouseFilter mouse_filter` = `0 (overrides Control)`
- `FocusMode slots_focus_mode` = `3`
- `String title` = `""`

**Methods**
- `void _draw_port(slot_index: int, position: Vector2i, left: bool, color: Color) virtual`
- `void clear_all_slots()`
- `void clear_slot(slot_index: int)`
- `Color get_input_port_color(port_idx: int)`
- `int get_input_port_count()`
- `Vector2 get_input_port_position(port_idx: int)`
- `int get_input_port_slot(port_idx: int)`
- `int get_input_port_type(port_idx: int)`
- `Color get_output_port_color(port_idx: int)`
- `int get_output_port_count()`
- `Vector2 get_output_port_position(port_idx: int)`
- `int get_output_port_slot(port_idx: int)`
- `int get_output_port_type(port_idx: int)`
- `Color get_slot_color_left(slot_index: int) const`
- `Color get_slot_color_right(slot_index: int) const`
- `Texture2D get_slot_custom_icon_left(slot_index: int) const`
- `Texture2D get_slot_custom_icon_right(slot_index: int) const`
- `Variant get_slot_metadata_left(slot_index: int) const`
- `Variant get_slot_metadata_right(slot_index: int) const`
- `int get_slot_type_left(slot_index: int) const`
- `int get_slot_type_right(slot_index: int) const`
- `HBoxContainer get_titlebar_hbox()`
- `bool is_slot_draw_stylebox(slot_index: int) const`
- `bool is_slot_enabled_left(slot_index: int) const`
- `bool is_slot_enabled_right(slot_index: int) const`
- `void set_slot(slot_index: int, enable_left_port: bool, type_left: int, color_left: Color, enable_right_port: bool, type_right: int, color_right: Color, custom_icon_left: Texture2D = null, custom_icon_right: Texture2D = null, draw_stylebox: bool = true)`
- `void set_slot_color_left(slot_index: int, color: Color)`
- `void set_slot_color_right(slot_index: int, color: Color)`
- `void set_slot_custom_icon_left(slot_index: int, custom_icon: Texture2D)`
- `void set_slot_custom_icon_right(slot_index: int, custom_icon: Texture2D)`
- `void set_slot_draw_stylebox(slot_index: int, enable: bool)`
- `void set_slot_enabled_left(slot_index: int, enable: bool)`
- `void set_slot_enabled_right(slot_index: int, enable: bool)`
- `void set_slot_metadata_left(slot_index: int, value: Variant)`
- `void set_slot_metadata_right(slot_index: int, value: Variant)`
- `void set_slot_type_left(slot_index: int, type: int)`
- `void set_slot_type_right(slot_index: int, type: int)`

### GridContainer
*Inherits: **Container < Control < CanvasItem < Node < Object***

GridContainer arranges its child controls in a grid layout. The number of columns is specified by the columns property, whereas the number of rows depends on how many are needed for the child controls. The number of rows and columns is preserved for every size of the container.

**Properties**
- `int columns` = `1`

### HBoxContainer
*Inherits: **BoxContainer < Container < Control < CanvasItem < Node < Object** | Inherited by: EditorResourcePicker, EditorToaster, OpenXRInteractionProfileEditorBase*

A variant of BoxContainer that can only arrange its child controls horizontally. Child controls are rearranged automatically when their minimum size changes.

### HScrollBar
*Inherits: **ScrollBar < Range < Control < CanvasItem < Node < Object***

A horizontal scrollbar, typically used to navigate through content that extends beyond the visible width of a control. It is a Range-based control and goes from left (min) to right (max).

### HSlider
*Inherits: **Slider < Range < Control < CanvasItem < Node < Object***

A horizontal slider, used to adjust a value by moving a grabber along a horizontal axis. It is a Range-based control and goes from left (min) to right (max).

### HSplitContainer
*Inherits: **SplitContainer < Container < Control < CanvasItem < Node < Object***

A container that accepts only two child controls, then arranges them horizontally and creates a divisor between them. The divisor can be dragged around to change the size relation between the child controls.

### ItemList
*Inherits: **Control < CanvasItem < Node < Object***

This control provides a vertical list of selectable items that may be in a single or in multiple columns, with each item having options for text and an icon. Tooltips are supported and may be different for every item in the list.

**Properties**
- `bool allow_reselect` = `false`
- `bool allow_rmb_select` = `false`
- `bool allow_search` = `true`
- `bool auto_height` = `false`
- `bool auto_width` = `false`
- `bool clip_contents` = `true (overrides Control)`
- `int fixed_column_width` = `0`
- `Vector2i fixed_icon_size` = `Vector2i(0, 0)`
- `FocusMode focus_mode` = `2 (overrides Control)`
- `IconMode icon_mode` = `1`
- `float icon_scale` = `1.0`
- `int item_count` = `0`
- `int max_columns` = `1`
- `int max_text_lines` = `1`
- `bool same_column_width` = `false`
- `ScrollHintMode scroll_hint_mode` = `0`
- `SelectMode select_mode` = `0`
- `OverrunBehavior text_overrun_behavior` = `3`
- `bool tile_scroll_hint` = `false`
- `bool wraparound_items` = `true`

**Methods**
- `int add_icon_item(icon: Texture2D, selectable: bool = true)`
- `int add_item(text: String, icon: Texture2D = null, selectable: bool = true)`
- `void clear()`
- `void deselect(idx: int)`
- `void deselect_all()`
- `void ensure_current_is_visible()`
- `void force_update_list_size()`
- `HScrollBar get_h_scroll_bar()`
- `int get_item_at_position(position: Vector2, exact: bool = false) const`
- `AutoTranslateMode get_item_auto_translate_mode(idx: int) const`
- `Color get_item_custom_bg_color(idx: int) const`
- `Color get_item_custom_fg_color(idx: int) const`
- `Texture2D get_item_icon(idx: int) const`
- `Color get_item_icon_modulate(idx: int) const`
- `Rect2 get_item_icon_region(idx: int) const`
- `String get_item_language(idx: int) const`
- `Variant get_item_metadata(idx: int) const`
- `Rect2 get_item_rect(idx: int, expand: bool = true) const`
- `String get_item_text(idx: int) const`
- `TextDirection get_item_text_direction(idx: int) const`
- `String get_item_tooltip(idx: int) const`
- `PackedInt32Array get_selected_items()`
- `VScrollBar get_v_scroll_bar()`
- `bool is_anything_selected()`
- `bool is_item_disabled(idx: int) const`
- `bool is_item_icon_transposed(idx: int) const`
- `bool is_item_selectable(idx: int) const`
- `bool is_item_tooltip_enabled(idx: int) const`
- `bool is_selected(idx: int) const`
- `void move_item(from_idx: int, to_idx: int)`
- `void remove_item(idx: int)`
- `void select(idx: int, single: bool = true)`
- `void set_item_auto_translate_mode(idx: int, mode: AutoTranslateMode)`
- `void set_item_custom_bg_color(idx: int, custom_bg_color: Color)`
- `void set_item_custom_fg_color(idx: int, custom_fg_color: Color)`
- `void set_item_disabled(idx: int, disabled: bool)`
- `void set_item_icon(idx: int, icon: Texture2D)`
- `void set_item_icon_modulate(idx: int, modulate: Color)`
- `void set_item_icon_region(idx: int, rect: Rect2)`
- `void set_item_icon_transposed(idx: int, transposed: bool)`

### LineEdit
*Inherits: **Control < CanvasItem < Node < Object***

LineEdit provides an input field for editing a single line of text.

**Properties**
- `HorizontalAlignment alignment` = `0`
- `bool backspace_deletes_composite_character_enabled` = `false`
- `bool caret_blink` = `false`
- `float caret_blink_interval` = `0.65`
- `int caret_column` = `0`
- `bool caret_force_displayed` = `false`
- `bool caret_mid_grapheme` = `false`
- `bool clear_button_enabled` = `false`
- `bool context_menu_enabled` = `true`
- `bool deselect_on_focus_loss_enabled` = `true`
- `bool drag_and_drop_selection_enabled` = `true`
- `bool draw_control_chars` = `false`
- `bool editable` = `true`
- `bool emoji_menu_enabled` = `true`
- `bool expand_to_text_length` = `false`
- `bool flat` = `false`
- `FocusMode focus_mode` = `2 (overrides Control)`
- `ExpandMode icon_expand_mode` = `0`
- `bool keep_editing_on_text_submit` = `false`
- `String language` = `""`
- `int max_length` = `0`
- `bool middle_mouse_paste_enabled` = `true`
- `CursorShape mouse_default_cursor_shape` = `1 (overrides Control)`
- `String placeholder_text` = `""`
- `Texture2D right_icon`
- `float right_icon_scale` = `1.0`
- `bool secret` = `false`
- `String secret_character` = `"•"`
- `bool select_all_on_focus` = `false`
- `bool selecting_enabled` = `true`

**Methods**
- `void apply_ime()`
- `void cancel_ime()`
- `void clear()`
- `void delete_char_at_caret()`
- `void delete_text(from_column: int, to_column: int)`
- `void deselect()`
- `void edit(hide_focus: bool = false)`
- `PopupMenu get_menu() const`
- `int get_next_composite_character_column(column: int) const`
- `int get_previous_composite_character_column(column: int) const`
- `float get_scroll_offset() const`
- `String get_selected_text()`
- `int get_selection_from_column() const`
- `int get_selection_to_column() const`
- `bool has_ime_text() const`
- `bool has_redo() const`
- `bool has_selection() const`
- `bool has_undo() const`
- `void insert_text_at_caret(text: String)`
- `bool is_editing() const`
- `bool is_menu_visible() const`
- `void menu_option(option: int)`
- `void select(from: int = 0, to: int = -1)`
- `void select_all()`
- `void unedit()`

**GDScript Examples**
```gdscript
text = "Hello world"
max_length = 5
# `text` becomes "Hello".
max_length = 10
text += " goodbye"
# `text` becomes "Hello good".
# `text_change_rejected` is emitted with "bye" as a parameter.
```
```gdscript
func _ready():
    var menu = get_menu()
    # Remove all items after "Redo".
    menu.item_count = menu.get_item_index(MENU_REDO) + 1
    # Add custom items.
    menu.add_separator()
    menu.add_item("Insert Date", MENU_MAX + 1)
    # Connect callback.
    menu.id_pressed.connect(_on_item_pressed)

func _on_item_pressed(id):
    if id == MENU_MAX + 1:
        insert_text_at_caret(Time.get_date_string_from_system())
```

### LinkButton
*Inherits: **BaseButton < Control < CanvasItem < Node < Object***

A button that represents a link. This type of button is primarily used for interactions that cause a context change (like linking to a web page).

**Properties**
- `String ellipsis_char` = `"…"`
- `FocusMode focus_mode` = `3 (overrides Control)`
- `String language` = `""`
- `CursorShape mouse_default_cursor_shape` = `2 (overrides Control)`
- `StructuredTextParser structured_text_bidi_override` = `0`
- `Array structured_text_bidi_override_options` = `[]`
- `String text` = `""`
- `TextDirection text_direction` = `0`
- `OverrunBehavior text_overrun_behavior` = `0`
- `UnderlineMode underline` = `0`
- `String uri` = `""`

**GDScript Examples**
```gdscript
uri = "https://godotengine.org"  # Opens the URL in the default web browser.
uri = "C:\SomeFolder"  # Opens the file explorer at the given path.
uri = "C:\SomeImage.png"  # Opens the given image in the default viewing app.
```

### MarginContainer
*Inherits: **Container < Control < CanvasItem < Node < Object** | Inherited by: EditorDock*

MarginContainer adds an adjustable margin on each side of its child controls. The margins are added around all children, not around each individual one. To control the MarginContainer's margins, use the margin_* theme properties listed below.

**GDScript Examples**
```gdscript
# This code sample assumes the current script is extending MarginContainer.
var margin_value = 100
add_theme_constant_override("margin_top", margin_value)
add_theme_constant_override("margin_left", margin_value)
add_theme_constant_override("margin_bottom", margin_value)
add_theme_constant_override("margin_right", margin_value)
```

### MenuButton
*Inherits: **Button < BaseButton < Control < CanvasItem < Node < Object***

A button that brings up a PopupMenu when clicked. To create new items inside this PopupMenu, use get_popup().add_item("My Item Name"). You can also create them directly from Godot editor's inspector.

**Properties**
- `ActionMode action_mode` = `0 (overrides BaseButton)`
- `bool flat` = `true (overrides Button)`
- `FocusMode focus_mode` = `3 (overrides Control)`
- `int item_count` = `0`
- `bool switch_on_hover` = `false`
- `bool toggle_mode` = `true (overrides BaseButton)`

**Methods**
- `PopupMenu get_popup() const`
- `void set_disable_shortcuts(disabled: bool)`
- `void show_popup()`

### OptionButton
*Inherits: **Button < BaseButton < Control < CanvasItem < Node < Object***

OptionButton is a type of button that brings up a dropdown with selectable items when pressed. The item selected becomes the "current" item and is displayed as the button text.

**Properties**
- `ActionMode action_mode` = `0 (overrides BaseButton)`
- `HorizontalAlignment alignment` = `0 (overrides Button)`
- `bool allow_reselect` = `false`
- `bool fit_to_longest_item` = `true`
- `int item_count` = `0`
- `int selected` = `-1`
- `bool toggle_mode` = `true (overrides BaseButton)`

**Methods**
- `void add_icon_item(texture: Texture2D, label: String, id: int = -1)`
- `void add_item(label: String, id: int = -1)`
- `void add_separator(text: String = "")`
- `void clear()`
- `AutoTranslateMode get_item_auto_translate_mode(idx: int) const`
- `Texture2D get_item_icon(idx: int) const`
- `int get_item_id(idx: int) const`
- `int get_item_index(id: int) const`
- `Variant get_item_metadata(idx: int) const`
- `String get_item_text(idx: int) const`
- `String get_item_tooltip(idx: int) const`
- `PopupMenu get_popup() const`
- `int get_selectable_item(from_last: bool = false) const`
- `int get_selected_id() const`
- `Variant get_selected_metadata() const`
- `bool has_selectable_items() const`
- `bool is_item_disabled(idx: int) const`
- `bool is_item_separator(idx: int) const`
- `void remove_item(idx: int)`
- `void select(idx: int)`
- `void set_disable_shortcuts(disabled: bool)`
- `void set_item_auto_translate_mode(idx: int, mode: AutoTranslateMode)`
- `void set_item_disabled(idx: int, disabled: bool)`
- `void set_item_icon(idx: int, texture: Texture2D)`
- `void set_item_id(idx: int, id: int)`
- `void set_item_metadata(idx: int, metadata: Variant)`
- `void set_item_text(idx: int, text: String)`
- `void set_item_tooltip(idx: int, tooltip: String)`
- `void show_popup()`

### PanelContainer
*Inherits: **Container < Control < CanvasItem < Node < Object** | Inherited by: OpenXRBindingModifierEditor, ScriptEditor*

A container that keeps its child controls within the area of a StyleBox. Useful for giving controls an outline.

**Properties**
- `MouseFilter mouse_filter` = `0 (overrides Control)`

### PopupMenu
*Inherits: **Popup < Window < Viewport < Node < Object***

PopupMenu is a modal window used to display a list of options. Useful for toolbars and context menus.

**Properties**
- `bool allow_search` = `true`
- `bool hide_on_checkable_item_selection` = `true`
- `bool hide_on_item_selection` = `true`
- `bool hide_on_state_item_selection` = `false`
- `int item_count` = `0`
- `bool prefer_native_menu` = `false`
- `bool shrink_height` = `true`
- `bool shrink_width` = `true`
- `float submenu_popup_delay` = `0.2`
- `SystemMenus system_menu_id` = `0`
- `bool transparent` = `true (overrides Window)`
- `bool transparent_bg` = `true (overrides Viewport)`

**Methods**
- `bool activate_item_by_event(event: InputEvent, for_global_only: bool = false)`
- `void add_check_item(label: String, id: int = -1, accel: Key = 0)`
- `void add_check_shortcut(shortcut: Shortcut, id: int = -1, global: bool = false)`
- `void add_icon_check_item(texture: Texture2D, label: String, id: int = -1, accel: Key = 0)`
- `void add_icon_check_shortcut(texture: Texture2D, shortcut: Shortcut, id: int = -1, global: bool = false)`
- `void add_icon_item(texture: Texture2D, label: String, id: int = -1, accel: Key = 0)`
- `void add_icon_radio_check_item(texture: Texture2D, label: String, id: int = -1, accel: Key = 0)`
- `void add_icon_radio_check_shortcut(texture: Texture2D, shortcut: Shortcut, id: int = -1, global: bool = false)`
- `void add_icon_shortcut(texture: Texture2D, shortcut: Shortcut, id: int = -1, global: bool = false, allow_echo: bool = false)`
- `void add_item(label: String, id: int = -1, accel: Key = 0)`
- `void add_multistate_item(label: String, max_states: int, default_state: int = 0, id: int = -1, accel: Key = 0)`
- `void add_radio_check_item(label: String, id: int = -1, accel: Key = 0)`
- `void add_radio_check_shortcut(shortcut: Shortcut, id: int = -1, global: bool = false)`
- `void add_separator(label: String = "", id: int = -1)`
- `void add_shortcut(shortcut: Shortcut, id: int = -1, global: bool = false, allow_echo: bool = false)`
- `void add_submenu_item(label: String, submenu: String, id: int = -1)`
- `void add_submenu_node_item(label: String, submenu: PopupMenu, id: int = -1)`
- `void clear(free_submenus: bool = false)`
- `int get_focused_item() const`
- `Key get_item_accelerator(index: int) const`
- `AutoTranslateMode get_item_auto_translate_mode(index: int) const`
- `Texture2D get_item_icon(index: int) const`
- `int get_item_icon_max_width(index: int) const`
- `Color get_item_icon_modulate(index: int) const`
- `int get_item_id(index: int) const`
- `int get_item_indent(index: int) const`
- `int get_item_index(id: int) const`
- `String get_item_language(index: int) const`
- `Variant get_item_metadata(index: int) const`
- `int get_item_multistate(index: int) const`
- `int get_item_multistate_max(index: int) const`
- `Shortcut get_item_shortcut(index: int) const`
- `String get_item_submenu(index: int) const`
- `PopupMenu get_item_submenu_node(index: int) const`
- `String get_item_text(index: int) const`
- `TextDirection get_item_text_direction(index: int) const`
- `String get_item_tooltip(index: int) const`
- `bool is_item_checkable(index: int) const`
- `bool is_item_checked(index: int) const`
- `bool is_item_disabled(index: int) const`

**GDScript Examples**
```gdscript
func _ready():
    add_multistate_item("Item", 3, 0)

    index_pressed.connect(func(index: int):
            toggle_item_multistate(index)
            match get_item_multistate(index):
                0:
                    print("First state")
                1:
                    print("Second state")
                2:
                    print("Third state")
        )
```

### PopupPanel
*Inherits: **Popup < Window < Viewport < Node < Object***

A popup with a configurable panel background. Any child controls added to this node will be stretched to fit the panel's size (similar to how PanelContainer works). If you are making windows, see Window.

**Properties**
- `bool transparent` = `true (overrides Window)`
- `bool transparent_bg` = `true (overrides Viewport)`

### ProgressBar
*Inherits: **Range < Control < CanvasItem < Node < Object***

A control used for visual representation of a percentage. Shows the fill percentage in the center. Can also be used to show indeterminate progress. For more fill modes, use TextureProgressBar instead.

**Properties**
- `bool editor_preview_indeterminate`
- `int fill_mode` = `0`
- `bool indeterminate` = `false`
- `bool show_percentage` = `true`

### RichTextLabel
*Inherits: **Control < CanvasItem < Node < Object***

A control for displaying text that can contain custom fonts, images, and basic formatting. RichTextLabel manages these as an internal tag stack. It also adapts itself to given width/heights.

**Properties**
- `AutowrapMode autowrap_mode` = `3`
- `BitField[LineBreakFlag] autowrap_trim_flags` = `192`
- `bool bbcode_enabled` = `false`
- `bool clip_contents` = `true (overrides Control)`
- `bool context_menu_enabled` = `false`
- `Array custom_effects` = `[]`
- `bool deselect_on_focus_loss_enabled` = `true`
- `bool drag_and_drop_selection_enabled` = `true`
- `bool fit_content` = `false`
- `FocusMode focus_mode` = `3 (overrides Control)`
- `bool hint_underlined` = `true`
- `HorizontalAlignment horizontal_alignment` = `0`
- `BitField[JustificationFlag] justification_flags` = `163`
- `String language` = `""`
- `bool meta_underlined` = `true`
- `int progress_bar_delay` = `1000`
- `bool scroll_active` = `true`
- `bool scroll_following` = `false`
- `bool scroll_following_visible_characters` = `false`
- `bool selection_enabled` = `false`
- `bool shortcut_keys_enabled` = `true`
- `StructuredTextParser structured_text_bidi_override` = `0`
- `Array structured_text_bidi_override_options` = `[]`
- `int tab_size` = `4`
- `PackedFloat32Array tab_stops` = `PackedFloat32Array()`
- `String text` = `""`
- `TextDirection text_direction` = `0`
- `bool threaded` = `false`
- `VerticalAlignment vertical_alignment` = `0`
- `int visible_characters` = `-1`

**Methods**
- `void add_hr(width: int = 90, height: int = 2, color: Color = Color(1, 1, 1, 1), alignment: HorizontalAlignment = 1, width_in_percent: bool = true, height_in_percent: bool = false)`
- `void add_image(image: Texture2D, width: int = 0, height: int = 0, color: Color = Color(1, 1, 1, 1), inline_align: InlineAlignment = 5, region: Rect2 = Rect2(0, 0, 0, 0), key: Variant = null, pad: bool = false, tooltip: String = "", width_in_percent: bool = false, height_in_percent: bool = false, alt_text: String = "")`
- `void add_text(text: String)`
- `void append_text(bbcode: String)`
- `void clear()`
- `void deselect()`
- `int get_character_line(character: int)`
- `int get_character_paragraph(character: int)`
- `int get_content_height() const`
- `int get_content_width() const`
- `int get_line_count() const`
- `int get_line_height(line: int) const`
- `float get_line_offset(line: int)`
- `Vector2i get_line_range(line: int)`
- `int get_line_width(line: int) const`
- `PopupMenu get_menu() const`
- `int get_paragraph_count() const`
- `float get_paragraph_offset(paragraph: int)`
- `String get_parsed_text() const`
- `String get_selected_text() const`
- `int get_selection_from() const`
- `float get_selection_line_offset() const`
- `int get_selection_to() const`
- `int get_total_character_count() const`
- `VScrollBar get_v_scroll_bar()`
- `Rect2i get_visible_content_rect() const`
- `int get_visible_line_count() const`
- `int get_visible_paragraph_count() const`
- `void install_effect(effect: Variant)`
- `bool invalidate_paragraph(paragraph: int)`
- `bool is_finished() const`
- `bool is_menu_visible() const`
- `bool is_ready() const`
- `void menu_option(option: int)`
- `void newline()`
- `void parse_bbcode(bbcode: String)`
- `Dictionary parse_expressions_for_values(expressions: PackedStringArray)`
- `void pop()`
- `void pop_all()`
- `void pop_context()`

**GDScript Examples**
```gdscript
# This assumes RichTextLabel's `meta_clicked` signal was connected to
# the function below using the signal connection dialog.
func _richtextlabel_on_meta_clicked(meta):
    # `meta` is of Variant type, so convert it to a String to avoid script errors at run-time.
    OS.shell_open(str(meta))
```
```gdscript
func _ready():
    var menu = get_menu()
    # Remove "Select All" item.
    menu.remove_item(MENU_SELECT_ALL)
    # Add custom items.
    menu.add_separator()
    menu.add_item("Duplicate Text", MENU_MAX + 1)
    # Connect callback.
    menu.id_pressed.connect(_on_item_pressed)

func _on_item_pressed(id):
    if id == MENU_MAX + 1:
        add_text("\n" + get_parsed_text())
```

### ScrollBar
*Inherits: **Range < Control < CanvasItem < Node < Object** | Inherited by: HScrollBar, VScrollBar*

Abstract base class for scrollbars, typically used to navigate through content that extends beyond the visible area of a control. Scrollbars are Range-based controls.

**Properties**
- `float custom_step` = `-1.0`
- `FocusMode focus_mode` = `3 (overrides Control)`
- `float step` = `0.0 (overrides Range)`

### ScrollContainer
*Inherits: **Container < Control < CanvasItem < Node < Object** | Inherited by: EditorInspector*

A container used to provide a child control with scrollbars when needed. Scrollbars will automatically be drawn at the right (for vertical) or bottom (for horizontal) and will enable dragging to move the viewable Control (and its children) within the ScrollContainer. Scrollbars will also automatically resize the grabber based on the Control.custom_minimum_size of the Control relative to the ScrollContainer.

**Properties**
- `bool clip_contents` = `true (overrides Control)`
- `bool draw_focus_border` = `false`
- `bool follow_focus` = `false`
- `ScrollMode horizontal_scroll_mode` = `1`
- `int scroll_deadzone` = `0`
- `ScrollHintMode scroll_hint_mode` = `0`
- `int scroll_horizontal` = `0`
- `float scroll_horizontal_custom_step` = `-1.0`
- `int scroll_vertical` = `0`
- `float scroll_vertical_custom_step` = `-1.0`
- `bool tile_scroll_hint` = `false`
- `ScrollMode vertical_scroll_mode` = `1`

**Methods**
- `void ensure_control_visible(control: Control)`
- `HScrollBar get_h_scroll_bar()`
- `VScrollBar get_v_scroll_bar()`

**GDScript Examples**
```gdscript
func _ready():
    set_deferred("scroll_horizontal", 600)
```
```gdscript
func _ready():
    set_deferred("scroll_vertical", 600)
```

### Slider
*Inherits: **Range < Control < CanvasItem < Node < Object** | Inherited by: HSlider, VSlider*

Abstract base class for sliders, used to adjust a value by moving a grabber along a horizontal or vertical axis. Sliders are Range-based controls.

**Properties**
- `bool editable` = `true`
- `FocusMode focus_mode` = `2 (overrides Control)`
- `bool scrollable` = `true`
- `float step` = `1.0 (overrides Range)`
- `int tick_count` = `0`
- `bool ticks_on_borders` = `false`
- `TickPosition ticks_position` = `0`

### SpinBox
*Inherits: **Range < Control < CanvasItem < Node < Object***

SpinBox is a numerical input text field. It allows entering integers and floating-point numbers. The SpinBox also has up and down buttons that can be clicked increase or decrease the value. The value can also be changed by dragging the mouse up or down over the SpinBox's arrows.

**Properties**
- `HorizontalAlignment alignment` = `0`
- `bool custom_arrow_round` = `false`
- `float custom_arrow_step` = `0.0`
- `bool editable` = `true`
- `String prefix` = `""`
- `bool select_all_on_focus` = `false`
- `BitField[SizeFlags] size_flags_vertical` = `1 (overrides Control)`
- `float step` = `1.0 (overrides Range)`
- `String suffix` = `""`
- `bool update_on_text_changed` = `false`

**Methods**
- `void apply()`
- `LineEdit get_line_edit()`

**GDScript Examples**
```gdscript
var spin_box = SpinBox.new()
add_child(spin_box)
var line_edit = spin_box.get_line_edit()
line_edit.context_menu_enabled = false
spin_box.horizontal_alignment = LineEdit.HORIZONTAL_ALIGNMENT_RIGHT
```

### SplitContainer
*Inherits: **Container < Control < CanvasItem < Node < Object** | Inherited by: HSplitContainer, VSplitContainer*

A container that arranges child controls horizontally or vertically and creates grabbers between them. The grabbers can be dragged around to change the size relations between the child controls.

**Properties**
- `bool collapsed` = `false`
- `bool drag_area_highlight_in_editor` = `false`
- `int drag_area_margin_begin` = `0`
- `int drag_area_margin_end` = `0`
- `int drag_area_offset` = `0`
- `DraggerVisibility dragger_visibility` = `0`
- `bool dragging_enabled` = `true`
- `int split_offset` = `0`
- `PackedInt32Array split_offsets` = `PackedInt32Array(0)`
- `bool touch_dragger_enabled` = `false`
- `bool vertical` = `false`

**Methods**
- `void clamp_split_offset(priority_index: int = 0)`
- `Control get_drag_area_control()`
- `Array[Control] get_drag_area_controls()`

**GDScript Examples**
```gdscript
$BarnacleButton.reparent($SplitContainer.get_drag_area_control())
```
```gdscript
$BarnacleButton.reparent($SplitContainer.get_drag_area_controls()[0])
```

### SubViewportContainer
*Inherits: **Container < Control < CanvasItem < Node < Object***

A container that displays the contents of underlying SubViewport child nodes. It uses the combined size of the SubViewports as minimum size, unless stretch is enabled.

**Properties**
- `FocusMode focus_mode` = `1 (overrides Control)`
- `bool mouse_target` = `false`
- `bool stretch` = `false`
- `int stretch_shrink` = `1`

**Methods**
- `bool _propagate_input_event(event: InputEvent) virtual const`

### TabBar
*Inherits: **Control < CanvasItem < Node < Object***

A control that provides a horizontal bar with tabs. Similar to TabContainer but is only in charge of drawing tabs, not interacting with children.

**Properties**
- `bool clip_tabs` = `true`
- `bool close_with_middle_mouse` = `true`
- `int current_tab` = `-1`
- `bool deselect_enabled` = `false`
- `bool drag_to_rearrange_enabled` = `false`
- `FocusMode focus_mode` = `2 (overrides Control)`
- `int max_tab_width` = `0`
- `bool scroll_to_selected` = `true`
- `bool scrolling_enabled` = `true`
- `bool select_with_rmb` = `false`
- `bool switch_on_drag_hover` = `true`
- `AlignmentMode tab_alignment` = `0`
- `CloseButtonDisplayPolicy tab_close_display_policy` = `0`
- `int tab_count` = `0`
- `int tabs_rearrange_group` = `-1`

**Methods**
- `void add_tab(title: String = "", icon: Texture2D = null)`
- `void clear_tabs()`
- `void ensure_tab_visible(idx: int)`
- `bool get_offset_buttons_visible() const`
- `int get_previous_tab() const`
- `Texture2D get_tab_button_icon(tab_idx: int) const`
- `Texture2D get_tab_icon(tab_idx: int) const`
- `int get_tab_icon_max_width(tab_idx: int) const`
- `int get_tab_idx_at_point(point: Vector2) const`
- `String get_tab_language(tab_idx: int) const`
- `Variant get_tab_metadata(tab_idx: int) const`
- `int get_tab_offset() const`
- `Rect2 get_tab_rect(tab_idx: int) const`
- `TextDirection get_tab_text_direction(tab_idx: int) const`
- `String get_tab_title(tab_idx: int) const`
- `String get_tab_tooltip(tab_idx: int) const`
- `bool is_tab_disabled(tab_idx: int) const`
- `bool is_tab_hidden(tab_idx: int) const`
- `void move_tab(from: int, to: int)`
- `void remove_tab(tab_idx: int)`
- `bool select_next_available()`
- `bool select_previous_available()`
- `void set_tab_button_icon(tab_idx: int, icon: Texture2D)`
- `void set_tab_disabled(tab_idx: int, disabled: bool)`
- `void set_tab_hidden(tab_idx: int, hidden: bool)`
- `void set_tab_icon(tab_idx: int, icon: Texture2D)`
- `void set_tab_icon_max_width(tab_idx: int, width: int)`
- `void set_tab_language(tab_idx: int, language: String)`
- `void set_tab_metadata(tab_idx: int, metadata: Variant)`
- `void set_tab_text_direction(tab_idx: int, direction: TextDirection)`
- `void set_tab_title(tab_idx: int, title: String)`
- `void set_tab_tooltip(tab_idx: int, tooltip: String)`

**GDScript Examples**
```gdscript
$TabBar.tab_close_pressed.connect($TabBar.remove_tab)
```

### TabContainer
*Inherits: **Container < Control < CanvasItem < Node < Object***

Arranges child controls into a tabbed view, creating a tab for each one. The active tab's corresponding control is made visible, while all other child controls are hidden. Ignores non-control children.

**Properties**
- `bool all_tabs_in_front` = `false`
- `bool clip_tabs` = `true`
- `int current_tab` = `-1`
- `bool deselect_enabled` = `false`
- `bool drag_to_rearrange_enabled` = `false`
- `bool switch_on_drag_hover` = `true`
- `AlignmentMode tab_alignment` = `0`
- `FocusMode tab_focus_mode` = `2`
- `TabPosition tabs_position` = `0`
- `int tabs_rearrange_group` = `-1`
- `bool tabs_visible` = `true`
- `bool use_hidden_tabs_for_min_size` = `false`

**Methods**
- `Control get_current_tab_control() const`
- `Popup get_popup() const`
- `int get_previous_tab() const`
- `TabBar get_tab_bar() const`
- `Texture2D get_tab_button_icon(tab_idx: int) const`
- `Control get_tab_control(tab_idx: int) const`
- `int get_tab_count() const`
- `Texture2D get_tab_icon(tab_idx: int) const`
- `int get_tab_icon_max_width(tab_idx: int) const`
- `int get_tab_idx_at_point(point: Vector2) const`
- `int get_tab_idx_from_control(control: Control) const`
- `Variant get_tab_metadata(tab_idx: int) const`
- `String get_tab_title(tab_idx: int) const`
- `String get_tab_tooltip(tab_idx: int) const`
- `bool is_tab_disabled(tab_idx: int) const`
- `bool is_tab_hidden(tab_idx: int) const`
- `bool select_next_available()`
- `bool select_previous_available()`
- `void set_popup(popup: Node)`
- `void set_tab_button_icon(tab_idx: int, icon: Texture2D)`
- `void set_tab_disabled(tab_idx: int, disabled: bool)`
- `void set_tab_hidden(tab_idx: int, hidden: bool)`
- `void set_tab_icon(tab_idx: int, icon: Texture2D)`
- `void set_tab_icon_max_width(tab_idx: int, width: int)`
- `void set_tab_metadata(tab_idx: int, metadata: Variant)`
- `void set_tab_title(tab_idx: int, title: String)`
- `void set_tab_tooltip(tab_idx: int, tooltip: String)`

### TextEdit
*Inherits: **Control < CanvasItem < Node < Object** | Inherited by: CodeEdit*

A multiline text editor. It also has limited facilities for editing code, such as syntax highlighting support. For more advanced facilities for editing code, see CodeEdit.

**Properties**
- `AutowrapMode autowrap_mode` = `3`
- `bool backspace_deletes_composite_character_enabled` = `false`
- `bool caret_blink` = `false`
- `float caret_blink_interval` = `0.65`
- `bool caret_draw_when_editable_disabled` = `false`
- `bool caret_mid_grapheme` = `false`
- `bool caret_move_on_right_click` = `true`
- `bool caret_multiple` = `true`
- `CaretType caret_type` = `0`
- `bool context_menu_enabled` = `true`
- `String custom_word_separators` = `""`
- `bool deselect_on_focus_loss_enabled` = `true`
- `bool drag_and_drop_selection_enabled` = `true`
- `bool draw_control_chars` = `false`
- `bool draw_spaces` = `false`
- `bool draw_tabs` = `false`
- `bool editable` = `true`
- `bool emoji_menu_enabled` = `true`
- `bool empty_selection_clipboard_enabled` = `true`
- `FocusMode focus_mode` = `2 (overrides Control)`
- `bool highlight_all_occurrences` = `false`
- `bool highlight_current_line` = `false`
- `bool indent_wrapped_lines` = `false`
- `String language` = `""`
- `bool middle_mouse_paste_enabled` = `true`
- `bool minimap_draw` = `false`
- `int minimap_width` = `80`
- `CursorShape mouse_default_cursor_shape` = `1 (overrides Control)`
- `String placeholder_text` = `""`
- `bool scroll_fit_content_height` = `false`

**Methods**
- `void _backspace(caret_index: int) virtual`
- `void _copy(caret_index: int) virtual`
- `void _cut(caret_index: int) virtual`
- `void _handle_unicode_input(unicode_char: int, caret_index: int) virtual`
- `void _paste(caret_index: int) virtual`
- `void _paste_primary_clipboard(caret_index: int) virtual`
- `int add_caret(line: int, column: int)`
- `void add_caret_at_carets(below: bool)`
- `void add_gutter(at: int = -1)`
- `void add_selection_for_next_occurrence()`
- `void adjust_carets_after_edit(caret: int, from_line: int, from_col: int, to_line: int, to_col: int)`
- `void adjust_viewport_to_caret(caret_index: int = 0)`
- `void apply_ime()`
- `void backspace(caret_index: int = -1)`
- `void begin_complex_operation()`
- `void begin_multicaret_edit()`
- `void cancel_ime()`
- `void center_viewport_to_caret(caret_index: int = 0)`
- `void clear()`
- `void clear_undo_history()`
- `void collapse_carets(from_line: int, from_column: int, to_line: int, to_column: int, inclusive: bool = false)`
- `void copy(caret_index: int = -1)`
- `void cut(caret_index: int = -1)`
- `void delete_selection(caret_index: int = -1)`
- `void deselect(caret_index: int = -1)`
- `void end_action()`
- `void end_complex_operation()`
- `void end_multicaret_edit()`
- `int get_caret_column(caret_index: int = 0) const`
- `int get_caret_count() const`
- `Vector2 get_caret_draw_pos(caret_index: int = 0) const`
- `PackedInt32Array get_caret_index_edit_order()`
- `int get_caret_line(caret_index: int = 0) const`
- `int get_caret_wrap_index(caret_index: int = 0) const`
- `int get_first_non_whitespace_column(line: int) const`
- `int get_first_visible_line() const`
- `int get_gutter_count() const`
- `String get_gutter_name(gutter: int) const`
- `GutterType get_gutter_type(gutter: int) const`
- `int get_gutter_width(gutter: int) const`

**GDScript Examples**
```gdscript
func _ready():
    var menu = get_menu()
    # Remove all items after "Redo".
    menu.item_count = menu.get_item_index(MENU_REDO) + 1
    # Add custom items.
    menu.add_separator()
    menu.add_item("Insert Date", MENU_MAX + 1)
    # Connect callback.
    menu.id_pressed.connect(_on_item_pressed)

func _on_item_pressed(id):
    if id == MENU_MAX + 1:
        insert_text_at_caret(Time.get_date_string_from_system())
```
```gdscript
var result = search("print", SEARCH_WHOLE_WORDS, 0, 0)
if result.x != -1:
    # Result found.
    var line_number = result.y
    var column_number = result.x
```

### TextureButton
*Inherits: **BaseButton < Control < CanvasItem < Node < Object***

TextureButton has the same functionality as Button, except it uses sprites instead of Godot's Theme resource. It is faster to create, but it doesn't support localization like more complex Controls.

**Properties**
- `bool flip_h` = `false`
- `bool flip_v` = `false`
- `bool ignore_texture_size` = `false`
- `StretchMode stretch_mode` = `2`
- `BitMap texture_click_mask`
- `Texture2D texture_disabled`
- `Texture2D texture_focused`
- `Texture2D texture_hover`
- `Texture2D texture_normal`
- `Texture2D texture_pressed`

### TextureRect
*Inherits: **Control < CanvasItem < Node < Object***

A control that displays a texture, for example an icon inside a GUI. The texture's placement can be controlled with the stretch_mode property. It can scale, tile, or stay centered inside its bounding rectangle.

**Properties**
- `ExpandMode expand_mode` = `0`
- `bool flip_h` = `false`
- `bool flip_v` = `false`
- `MouseFilter mouse_filter` = `1 (overrides Control)`
- `StretchMode stretch_mode` = `0`
- `Texture2D texture`

### VBoxContainer
*Inherits: **BoxContainer < Container < Control < CanvasItem < Node < Object** | Inherited by: ColorPicker, ScriptEditorBase*

A variant of BoxContainer that can only arrange its child controls vertically. Child controls are rearranged automatically when their minimum size changes.

### VScrollBar
*Inherits: **ScrollBar < Range < Control < CanvasItem < Node < Object***

A vertical scrollbar, typically used to navigate through content that extends beyond the visible height of a control. It is a Range-based control and goes from top (min) to bottom (max). Note that this direction is the opposite of VSlider's.

**Properties**
- `BitField[SizeFlags] size_flags_horizontal` = `0 (overrides Control)`
- `BitField[SizeFlags] size_flags_vertical` = `1 (overrides Control)`

### VSlider
*Inherits: **Slider < Range < Control < CanvasItem < Node < Object***

A vertical slider, used to adjust a value by moving a grabber along a vertical axis. It is a Range-based control and goes from bottom (min) to top (max). Note that this direction is the opposite of VScrollBar's.

**Properties**
- `BitField[SizeFlags] size_flags_horizontal` = `0 (overrides Control)`
- `BitField[SizeFlags] size_flags_vertical` = `1 (overrides Control)`

### VSplitContainer
*Inherits: **SplitContainer < Container < Control < CanvasItem < Node < Object***

A container that accepts only two child controls, then arranges them vertically and creates a divisor between them. The divisor can be dragged around to change the size relation between the child controls.

### VideoStreamPlayer
*Inherits: **Control < CanvasItem < Node < Object***

A control used for playback of VideoStream resources.

**Properties**
- `int audio_track` = `0`
- `bool autoplay` = `false`
- `int buffering_msec` = `500`
- `StringName bus` = `&"Master"`
- `bool expand` = `false`
- `bool loop` = `false`
- `bool paused` = `false`
- `float speed_scale` = `1.0`
- `VideoStream stream`
- `float stream_position`
- `float volume`
- `float volume_db` = `0.0`

**Methods**
- `float get_stream_length() const`
- `String get_stream_name() const`
- `Texture2D get_video_texture() const`
- `bool is_playing() const`
- `void play()`
- `void stop()`

### Window
*Inherits: **Viewport < Node < Object** | Inherited by: AcceptDialog, Popup*

A node that creates a window. The window can either be a native system window or embedded inside another Window (see Viewport.gui_embed_subwindows).

**Properties**
- `String accessibility_description` = `""`
- `String accessibility_name` = `""`
- `bool always_on_top` = `false`
- `bool auto_translate`
- `bool borderless` = `false`
- `ContentScaleAspect content_scale_aspect` = `0`
- `float content_scale_factor` = `1.0`
- `ContentScaleMode content_scale_mode` = `0`
- `Vector2i content_scale_size` = `Vector2i(0, 0)`
- `ContentScaleStretch content_scale_stretch` = `0`
- `int current_screen`
- `bool exclude_from_capture` = `false`
- `bool exclusive` = `false`
- `bool extend_to_title` = `false`
- `bool force_native` = `false`
- `WindowInitialPosition initial_position` = `0`
- `bool keep_title_visible` = `false`
- `Vector2i max_size` = `Vector2i(0, 0)`
- `bool maximize_disabled` = `false`
- `Vector2i min_size` = `Vector2i(0, 0)`
- `bool minimize_disabled` = `false`
- `Mode mode` = `0`
- `bool mouse_passthrough` = `false`
- `PackedVector2Array mouse_passthrough_polygon` = `PackedVector2Array()`
- `Rect2i nonclient_area` = `Rect2i(0, 0, 0, 0)`
- `bool popup_window` = `false`
- `bool popup_wm_hint` = `false`
- `Vector2i position` = `Vector2i(0, 0)`
- `bool sharp_corners` = `false`
- `Vector2i size` = `Vector2i(100, 100)`

**Methods**
- `Vector2 _get_contents_minimum_size() virtual const`
- `void add_theme_color_override(name: StringName, color: Color)`
- `void add_theme_constant_override(name: StringName, constant: int)`
- `void add_theme_font_override(name: StringName, font: Font)`
- `void add_theme_font_size_override(name: StringName, font_size: int)`
- `void add_theme_icon_override(name: StringName, texture: Texture2D)`
- `void add_theme_stylebox_override(name: StringName, stylebox: StyleBox)`
- `void begin_bulk_theme_override()`
- `bool can_draw() const`
- `void child_controls_changed()`
- `void end_bulk_theme_override()`
- `Vector2 get_contents_minimum_size() const`
- `bool get_flag(flag: Flags) const`
- `Window get_focused_window() static`
- `LayoutDirection get_layout_direction() const`
- `Vector2i get_position_with_decorations() const`
- `Vector2i get_size_with_decorations() const`
- `Color get_theme_color(name: StringName, theme_type: StringName = &"") const`
- `int get_theme_constant(name: StringName, theme_type: StringName = &"") const`
- `float get_theme_default_base_scale() const`
- `Font get_theme_default_font() const`
- `int get_theme_default_font_size() const`
- `Font get_theme_font(name: StringName, theme_type: StringName = &"") const`
- `int get_theme_font_size(name: StringName, theme_type: StringName = &"") const`
- `Texture2D get_theme_icon(name: StringName, theme_type: StringName = &"") const`
- `StyleBox get_theme_stylebox(name: StringName, theme_type: StringName = &"") const`
- `int get_window_id() const`
- `void grab_focus()`
- `bool has_focus() const`
- `bool has_theme_color(name: StringName, theme_type: StringName = &"") const`
- `bool has_theme_color_override(name: StringName) const`
- `bool has_theme_constant(name: StringName, theme_type: StringName = &"") const`
- `bool has_theme_constant_override(name: StringName) const`
- `bool has_theme_font(name: StringName, theme_type: StringName = &"") const`
- `bool has_theme_font_override(name: StringName) const`
- `bool has_theme_font_size(name: StringName, theme_type: StringName = &"") const`
- `bool has_theme_font_size_override(name: StringName) const`
- `bool has_theme_icon(name: StringName, theme_type: StringName = &"") const`
- `bool has_theme_icon_override(name: StringName) const`
- `bool has_theme_stylebox(name: StringName, theme_type: StringName = &"") const`

**GDScript Examples**
```gdscript
# Set region, using Path2D node.
$Window.mouse_passthrough_polygon = $Path2D.curve.get_baked_points()

# Set region, using Polygon2D node.
$Window.mouse_passthrough_polygon = $Polygon2D.polygon

# Reset region to default.
$Window.mouse_passthrough_polygon = []
```
```gdscript
func _ready():
    get_window().files_dropped.connect(on_files_dropped)

func on_files_dropped(files):
    print(files)
```
