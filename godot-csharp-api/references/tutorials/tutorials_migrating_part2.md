# Godot 4 C# Tutorials — Migrating (Part 2)

> 2 tutorials. C#-specific code examples.

## Upgrading from Godot 4.4 to Godot 4.5

For most games and apps made with 4.4 it should be relatively safe to migrate to 4.5. This page intends to cover everything you need to pay attention to when migrating your project.

### Breaking changes

If you are migrating from 4.4 to 4.5, the breaking changes listed here might affect you. Changes are grouped by areas/systems.

> **Warning:** In order to support [new Google Play requirements](https://android-developers.googleblog.com/2025/05/prepare-play-apps-for-devices-with-16kb-page-size.html) Android now requires targeting .NET 9 when exporting C# projects to Android, other platforms continue to use .NET 8 as the minimum required version but newer versions are supported and encouraged. If you are using C# in your project and want to export to Android, you will need to upgrade your project to .NET 9 (see [Upgrading to a new .NET version](https://learn.microsoft.com/en-us/dotnet/core/install/upgrade) for instructions).

This article indicates whether each breaking change affects GDScript and whether the C# breaking change is _binary compatible_ or _source compatible_:

- **Binary compatible** - Existing binaries will load and execute successfully without recompilation, and the run-time behavior won't change.
- **Source compatible** - Source code will compile successfully without changes when upgrading Godot.

#### Core

| Change                                                                | GDScript Compatible | C# Binary Compatible | C# Source Compatible | Introduced |
| --------------------------------------------------------------------- | ------------------- | -------------------- | -------------------- | ---------- |
| JSONRPC                                                               |                     |                      |                      |            |
| Method set_scope replaced by set_method                               | ❌                  | ❌                   | ❌                   | GH-104890  |
| Node                                                                  |                     |                      |                      |            |
| Method get_rpc_config renamed to get_node_rpc_config                  | ❌                  | ✔️                   | ✔️                   | GH-106848  |
| Method set_name changes name parameter type from String to StringName | ✔️                  | ✔️                   | ✔️                   | GH-76560   |

#### Rendering

| Change                                                                              | GDScript Compatible | C# Binary Compatible | C# Source Compatible | Introduced |
| ----------------------------------------------------------------------------------- | ------------------- | -------------------- | -------------------- | ---------- |
| DisplayServer                                                                       |                     |                      |                      |            |
| Method file_dialog_show adds a new parent_window_id optional parameter              | ✔️                  | ✔️                   | ✔️                   | GH-98194   |
| Method file_dialog_with_options_show adds a new parent_window_id optional parameter | ✔️                  | ✔️                   | ✔️                   | GH-98194   |
| RenderingDevice                                                                     |                     |                      |                      |            |
| Method texture_create_from_extension adds a new mipmaps optional parameter          | ✔️                  | ✔️                   | ✔️                   | GH-105570  |
| RenderingServer                                                                     |                     |                      |                      |            |
| Method instance_reset_physics_interpolation removed                                 | ❌                  | ✔️                   | ✔️                   | GH-104269  |
| Method instance_set_interpolated removed                                            | ❌                  | ✔️                   | ✔️                   | GH-104269  |

> **Note:** In C#, the enum `RenderingDevice.Features` breaks compatibility because of the way the bindings generator detects the enum prefix. New members were added to the enum in [GH-103941](https://github.com/godotengine/godot/pull/103941) that caused the enum member `Address` to be renamed to `BufferDeviceAddress`.

#### GLTF

| Change                                                                                          | GDScript Compatible | C# Binary Compatible | C# Source Compatible | Introduced |
| ----------------------------------------------------------------------------------------------- | ------------------- | -------------------- | -------------------- | ---------- |
| GLTFAccessor                                                                                    |                     |                      |                      |            |
| Property byte_offset changes type metadata from int32 to int64                                  | ✔️                  | ❌                   | ❌                   | GH-106220  |
| Property component_type changes type from int to GLTFAccessor::GLTFComponentType                | ✔️                  | ❌                   | ❌                   | GH-106220  |
| Property count changes type metadata from int32 to int64                                        | ✔️                  | ❌                   | ❌                   | GH-106220  |
| Property sparse_count changes type metadata from int32 to int64                                 | ✔️                  | ❌                   | ❌                   | GH-106220  |
| Property sparse_indices_byte_offset changes type metadata from int32 to int64                   | ✔️                  | ❌                   | ❌                   | GH-106220  |
| Property sparse_indices_component_type changes type from int to GLTFAccessor::GLTFComponentType | ✔️                  | ❌                   | ❌                   | GH-106220  |
| Property sparse_values_byte_offset changes type metadata from int32 to int64                    | ✔️                  | ❌                   | ❌                   | GH-106220  |
| GLTFBufferView                                                                                  |                     |                      |                      |            |
| Property byte_length changes type metadata from int32 to int64                                  | ✔️                  | ❌                   | ❌                   | GH-106220  |
| Property byte_offset changes type metadata from int32 to int64                                  | ✔️                  | ❌                   | ❌                   | GH-106220  |
| Property byte_stride changes type metadata from int32 to int64                                  | ✔️                  | ❌                   | ❌                   | GH-106220  |

> **Note:** As a result of changing the type metadata, the C# bindings changed the type from `int` (32-bytes) to `long` (64-bytes).

#### Text

| Change                                                                                           | GDScript Compatible | C# Binary Compatible | C# Source Compatible | Introduced |
| ------------------------------------------------------------------------------------------------ | ------------------- | -------------------- | -------------------- | ---------- |
| CanvasItem                                                                                       |                     |                      |                      |            |
| Method draw_char adds a new oversampling optional parameter                                      | ✔️                  | ✔️                   | ✔️                   | GH-104872  |
| Method draw_char_outline adds a new oversampling optional parameter                              | ✔️                  | ✔️                   | ✔️                   | GH-104872  |
| Method draw_multiline_string adds a new oversampling optional parameter                          | ✔️                  | ✔️                   | ✔️                   | GH-104872  |
| Method draw_multiline_string_outline adds a new oversampling optional parameter                  | ✔️                  | ✔️                   | ✔️                   | GH-104872  |
| Method draw_string adds a new oversampling optional parameter                                    | ✔️                  | ✔️                   | ✔️                   | GH-104872  |
| Method draw_string_outline adds a new oversampling optional parameter                            | ✔️                  | ✔️                   | ✔️                   | GH-104872  |
| Font                                                                                             |                     |                      |                      |            |
| Method draw_char adds a new oversampling optional parameter                                      | ✔️                  | ✔️                   | ✔️                   | GH-104872  |
| Method draw_char_outline adds a new oversampling optional parameter                              | ✔️                  | ✔️                   | ✔️                   | GH-104872  |
| Method draw_multiline_string adds a new oversampling optional parameter                          | ✔️                  | ✔️                   | ✔️                   | GH-104872  |
| Method draw_multiline_string_outline adds a new oversampling optional parameter                  | ✔️                  | ✔️                   | ✔️                   | GH-104872  |
| Method draw_string adds a new oversampling optional parameter                                    | ✔️                  | ✔️                   | ✔️                   | GH-104872  |
| Method draw_string_outline adds a new oversampling optional parameter                            | ✔️                  | ✔️                   | ✔️                   | GH-104872  |
| RichTextLabel                                                                                    |                     |                      |                      |            |
| Method add_image adds a new alt_text optional parameter                                          | ✔️                  | ✔️                   | ✔️                   | GH-76829   |
| Method add_image replaced size_in_percent parameter by width_in_percent and height_in_percent    | ✔️                  | ✔️                   | ✔️                   | GH-107347  |
| Method push_strikethrough adds optional color parameter                                          | ✔️                  | ✔️                   | ✔️                   | GH-106300  |
| Method push_table adds a new name optional parameter                                             | ✔️                  | ✔️                   | ✔️                   | GH-76829   |
| Method push_underline adds optional color parameter                                              | ✔️                  | ✔️                   | ✔️                   | GH-106300  |
| Method update_image replaced size_in_percent parameter by width_in_percent and height_in_percent | ✔️                  | ✔️                   | ✔️                   | GH-107347  |
| TextLine                                                                                         |                     |                      |                      |            |
| Method draw adds a new oversampling optional parameter                                           | ✔️                  | ✔️                   | ✔️                   | GH-104872  |
| Method draw_outline adds a new oversampling optional parameter                                   | ✔️                  | ✔️                   | ✔️                   | GH-104872  |
| TextParagraph                                                                                    |                     |                      |                      |            |
| Method draw adds a new oversampling optional parameter                                           | ✔️                  | ✔️                   | ✔️                   | GH-104872  |
| Method draw_dropcap adds a new oversampling optional parameter                                   | ✔️                  | ✔️                   | ✔️                   | GH-104872  |
| Method draw_dropcap_outline adds a new oversampling optional parameter                           | ✔️                  | ✔️                   | ✔️                   | GH-104872  |
| Method draw_line adds a new oversampling optional parameter                                      | ✔️                  | ✔️                   | ✔️                   | GH-104872  |
| Method draw_line_outline adds a new oversampling optional parameter                              | ✔️                  | ✔️                   | ✔️                   | GH-104872  |
| Method draw_outline adds a new oversampling optional parameter                                   | ✔️                  | ✔️                   | ✔️                   | GH-104872  |
| TextServer                                                                                       |                     |                      |                      |            |
| Method font_draw_glyph adds a new oversampling optional parameter                                | ✔️                  | ✔️                   | ✔️                   | GH-104872  |
| Method font_draw_glyph_outline adds a new oversampling optional parameter                        | ✔️                  | ✔️                   | ✔️                   | GH-104872  |
| Method shaped_text_draw adds a new oversampling optional parameter                               | ✔️                  | ✔️                   | ✔️                   | GH-104872  |
| Method shaped_text_draw_outline adds a new oversampling optional parameter                       | ✔️                  | ✔️                   | ✔️                   | GH-104872  |
| TreeItem                                                                                         |                     |                      |                      |            |
| Method add_button adds a new alt_text optional parameter                                         | ✔️                  | ✔️                   | ✔️                   | GH-76829   |
| TextServerExtension                                                                              |                     |                      |                      |            |
| Method \_font_draw_glyph adds a new oversampling optional parameter                              | ❌                  | ❌                   | ❌                   | GH-104872  |
| Method \_font_draw_glyph_outline adds a new oversampling optional parameter                      | ❌                  | ❌                   | ❌                   | GH-104872  |
| Method \_shaped_text_draw adds a new oversampling optional parameter                             | ❌                  | ❌                   | ❌                   | GH-104872  |
| Method \_shaped_text_draw_outline adds a new oversampling optional parameter                     | ❌                  | ❌                   | ❌                   | GH-104872  |

#### XR

| Change                                                                                                                                       | GDScript Compatible | C# Binary Compatible | C# Source Compatible | Introduced |
| -------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- | -------------------- | -------------------- | ---------- |
| OpenXRAPIExtension                                                                                                                           |                     |                      |                      |            |
| Method register_composition_layer_provider changes extension parameter type from OpenXRExtensionWrapperExtension to OpenXRExtensionWrapper   | ✔️                  | ✔️                   | ✔️                   | GH-104087  |
| Method register_projection_views_extension changes extension parameter type from OpenXRExtensionWrapperExtension to OpenXRExtensionWrapper   | ✔️                  | ✔️                   | ✔️                   | GH-104087  |
| Method unregister_composition_layer_provider changes extension parameter type from OpenXRExtensionWrapperExtension to OpenXRExtensionWrapper | ✔️                  | ✔️                   | ✔️                   | GH-104087  |
| Method unregister_projection_views_extension changes extension parameter type from OpenXRExtensionWrapperExtension to OpenXRExtensionWrapper | ✔️                  | ✔️                   | ✔️                   | GH-104087  |
| OpenXRBindingModifierEditor                                                                                                                  |                     |                      |                      |            |
| Type OpenXRBindingModifierEditor changed API type from Core to Editor                                                                        | ❌                  | ❌                   | ❌                   | GH-103869  |
| OpenXRInteractionProfileEditor                                                                                                               |                     |                      |                      |            |
| Type OpenXRInteractionProfileEditor changed API type from Core to Editor                                                                     | ❌                  | ❌                   | ❌                   | GH-103869  |
| OpenXRInteractionProfileEditorBase                                                                                                           |                     |                      |                      |            |
| Type OpenXRInteractionProfileEditorBase changed API type from Core to Editor                                                                 | ❌                  | ❌                   | ❌                   | GH-103869  |

> **Note:** Classes `OpenXRBindingModifierEditor`, `OpenXRInteractionProfileEditor`, and `OpenXRInteractionProfileEditorBase` are only available in the editor. Using them outside of the editor will result in a compilation error. In C#, this means the types are moved from the `GodotSharp` assembly to the `GodotSharpEditor` assembly. Make sure to wrap code that uses these types in a `#if TOOLS` block to ensure they are not included in an exported game. **This change was also backported to 4.4.1.**

#### Editor plugins

| Change                                                                      | GDScript Compatible | C# Binary Compatible | C# Source Compatible | Introduced |
| --------------------------------------------------------------------------- | ------------------- | -------------------- | -------------------- | ---------- |
| EditorExportPlatform                                                        |                     |                      |                      |            |
| Method get_forced_export_files adds a new preset optional parameter         | ✔️                  | ✔️                   | ✔️                   | GH-71542   |
| EditorUndoRedoManager                                                       |                     |                      |                      |            |
| Method create_action adds a new mark_unsaved optional parameter             | ✔️                  | ✔️                   | ✔️                   | GH-106121  |
| EditorExportPlatformExtension                                               |                     |                      |                      |            |
| Method \_get_option_icon changes return type from ImageTexture to Texture2D | ✔️                  | ❌                   | ❌                   | GH-108825  |

### Behavior changes

In 4.5, some behavior changes have been introduced, which might require you to adjust your project.

#### TileMapLayer

[TileMapLayer.get_coords_for_body_rid()](../godot_csharp_nodes_2d.md) will return different values in 4.5 compared to 4.4, as TileMapLayer physics chunking is enabled by default. Higher values of [TileMapLayer.physics_quadrant_size](../godot_csharp_nodes_2d.md) will make this function less precise. To get the exact cell coordinates like in 4.4 and prior versions, you need to set [TileMapLayer.physics_quadrant_size](../godot_csharp_nodes_2d.md) to `1`, which disables physics chunking.

#### 3D Model Import

A fix has been made to the 3D model importers to correctly handle non-joint nodes within a skeleton hierarchy ([GH-104184](https://github.com/godotengine/godot/pull/104184)). To preserve compatibility, the default behavior is to import existing files with the same behavior as before ([GH-107352](https://github.com/godotengine/godot/pull/107352)). New `.gltf`, `.glb`, `.blend`, and `.fbx` files (without a corresponding `.import` file) will be imported with the new behavior. However, for existing files, if you want to use the new behavior, you must change the "Naming Version" option at the bottom of the Import dock:

#### Core

> **Note:** [Resource.duplicate(true)](../godot_csharp_core.md) (which performs deep duplication) now only duplicates resources internal to the resource file it's called on. In 4.4, this duplicated everything instead, including external resources. If you were deep-duplicating a resource that contained references to other external resources, those external resources aren't duplicated anymore. You must call [Resource.duplicate_deep(DEEP_DUPLICATE_ALL)](../godot_csharp_core.md) instead to keep the old behavior.

> **Note:** [ProjectSettings.add_property_info()](../godot_csharp_filesystem.md) now prints a warning when the dictionary parameter has missing keys or invalid keys. Most importantly, it will now warn when a `usage` key is passed, as this key is not used. This was also the case before 4.5, but it was silently ignored instead. As a reminder, to set property usage information correctly, you must use [ProjectSettings.set_as_basic()](../godot_csharp_filesystem.md), [ProjectSettings.set_restart_if_changed()](../godot_csharp_filesystem.md), or [ProjectSettings.set_as_internal()](../godot_csharp_filesystem.md) instead.

> **Note:** In C#, `StringExtensions.PathJoin` now avoids adding an extra path separator when the original string is empty, or when the appended path starts with a path separator ([GH-105281](https://github.com/godotengine/godot/pull/105281)).

> **Note:** In C#, `StringExtensions.GetExtension` now returns an empty string instead of the original string when the original string does not contain an extension ([GH-108041](https://github.com/godotengine/godot/pull/108041)).

> **Note:** In C#, the `Quaternion(Vector3, Vector3)` constructor now correctly creates a quaternion representing the shortest arc between the two input vectors. Previously, it would return incorrect values for certain inputs ([GH-107618](https://github.com/godotengine/godot/pull/107618)).

#### Navigation

> **Note:** By default, the regions in a NavigationServer map now update asynchronously using threads to improve performance. This can cause additional delay in the update due to thread synchronisation. The asynchronous region update can be toggled with the `navigation/world/region_use_async_iterations` project setting.

> **Note:** The merging of navmeshes in the NavigationServer has changed processing order. Regions now merge and cache internal navmeshes first, then the remaining free edges are merged by the navigation map. If a project had navigation map synchronisation errors before, it might now have shifted affected edges, making already existing errors in a layout more noticeable in the pathfinding. The `navigation/2d_or_3d/merge_rasterizer_cell_scale` project setting can be set to a lower value to increase the detail of the rasterization grid (with 0.01 being the smallest cell size possible). If edge merge errors still persist with the lowest possible rasterization scale value, the error may be caused by overlap: two navmeshes are stacked on top of each other, causing geometry conflict.

#### Physics

> **Note:** When the 3D physics engine is set to Jolt Physics, you will now always have overlaps between `Area3D` and static bodies reported by default, as the `physics/jolt_physics_3d/simulation/areas_detect_static_bodies` project setting has been removed ([GH-105746](https://github.com/godotengine/godot/pull/105746)). If you still want such overlaps to be ignored, you will need to change the collision mask or layer of either the `Area3D` or the static body instead.

#### Text

> **Note:** In GDScript, calls to functions `RichTextLabel::add_image` and `RichTextLabel::update_image` will continue to work, but the `size_in_percent` argument will now be used as the value for `width_in_percent` and `height_in_percent` will default to `false` ([GH-107347](https://github.com/godotengine/godot/pull/107347)). To restore the previous behavior, you can explicitly set `height_in_percent` to the same value you were passing as `size_in_percent`.

---

## Upgrading from Godot 4.5 to Godot 4.6

For most games and apps made with 4.5 it should be relatively safe to migrate to 4.6. This page intends to cover everything you need to pay attention to when migrating your project.

### Breaking changes

If you are migrating from 4.5 to 4.6, the breaking changes listed here might affect you. Changes are grouped by areas/systems.

This article indicates whether each breaking change affects GDScript and whether the C# breaking change is _binary compatible_ or _source compatible_:

- **Binary compatible** - Existing binaries will load and execute successfully without recompilation, and the run-time behavior won't change.
- **Source compatible** - Source code will compile successfully without changes when upgrading Godot.

#### Core

| Change                                                                                | GDScript Compatible | C# Binary Compatible | C# Source Compatible | Introduced |
| ------------------------------------------------------------------------------------- | ------------------- | -------------------- | -------------------- | ---------- |
| FileAccess                                                                            |                     |                      |                      |            |
| Method create_temp changes mode_flags parameter type from int to FileAccess.ModeFlags | ✔️                  | ✔️                   | ✔️                   | GH-114053  |
| Method get_as_text removes skip_cr parameter                                          | ✔️                  | ✔️                   | ✔️                   | GH-110867  |
| Performance                                                                           |                     |                      |                      |            |
| Method add_custom_monitor adds a new type optional parameter                          | ✔️                  | ✔️                   | ✔️                   | GH-110433  |

#### Animation

| Change                                                                                 | GDScript Compatible | C# Binary Compatible | C# Source Compatible | Introduced |
| -------------------------------------------------------------------------------------- | ------------------- | -------------------- | -------------------- | ---------- |
| AnimationPlayer                                                                        |                     |                      |                      |            |
| Property assigned_animation changes type from String to StringName                     | ✔️                  | ❌                   | ❌                   | GH-110767  |
| Property autoplay changes type from String to StringName                               | ✔️                  | ❌                   | ❌                   | GH-110767  |
| Property current_animation changes type from String to StringName                      | ✔️                  | ❌                   | ❌                   | GH-110767  |
| Method get_queue changes return type from PackedStringArray to StringName[]            | ✔️                  | ❌                   | ❌                   | GH-110767  |
| Signal current_animation_changed changes name parameter type from String to StringName | ✔️                  | ❌                   | ❌                   | GH-110767  |

#### 3D

| Change                                                                                                                                           | GDScript Compatible | C# Binary Compatible | C# Source Compatible | Introduced |
| ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------- | -------------------- | -------------------- | ---------- |
| SpringBoneSimulator3D                                                                                                                            |                     |                      |                      |            |
| Method get_end_bone_direction changes return type from SpringBoneSimulator3D.BoneDirection to SkeletonModifier3D.BoneDirection                   | ✔️                  | ❌                   | ✔️                   | GH-110120  |
| Method get_joint_rotation_axis changes return type from SpringBoneSimulator3D.RotationAxis to SkeletonModifier3D.RotationAxis                    | ✔️                  | ❌                   | ✔️                   | GH-110120  |
| Method get_rotation_axis changes return type from SpringBoneSimulator3D.RotationAxis to SkeletonModifier3D.RotationAxis                          | ✔️                  | ❌                   | ✔️                   | GH-110120  |
| Method set_end_bone_direction changes bone_direction parameter type from SpringBoneSimulator3D.BoneDirection to SkeletonModifier3D.BoneDirection | ✔️                  | ❌                   | ✔️                   | GH-110120  |
| Method set_joint_rotation_axis changes axis parameter type from SpringBoneSimulator3D.RotationAxis to SkeletonModifier3D.RotationAxis            | ✔️                  | ❌                   | ✔️                   | GH-110120  |
| Method set_rotation_axis changes axis parameter type from SpringBoneSimulator3D.RotationAxis to SkeletonModifier3D.RotationAxis                  | ✔️                  | ❌                   | ✔️                   | GH-110120  |

#### Rendering

| Change                                                                                        | GDScript Compatible | C# Binary Compatible | C# Source Compatible | Introduced |
| --------------------------------------------------------------------------------------------- | ------------------- | -------------------- | -------------------- | ---------- |
| DisplayServer                                                                                 |                     |                      |                      |            |
| Method accessibility_create_sub_text_edit_elements adds a new is_last_line optional parameter | ✔️                  | ✔️                   | ✔️                   | GH-113459  |
| Method tts_speak changes utterance_id parameter type metadata from int32 to int64             | ✔️                  | ✔️                   | ✔️                   | GH-112379  |

#### GUI nodes

| Change                                                                 | GDScript Compatible | C# Binary Compatible | C# Source Compatible | Introduced |
| ---------------------------------------------------------------------- | ------------------- | -------------------- | -------------------- | ---------- |
| Control                                                                |                     |                      |                      |            |
| Method grab_focus adds a new hide_focus optional parameter             | ✔️                  | ✔️                   | ✔️                   | GH-110250  |
| Method has_focus adds a new ignore_hidden_focus optional parameter     | ✔️                  | ✔️                   | ✔️                   | GH-110250  |
| FileDialog                                                             |                     |                      |                      |            |
| Method add_filter adds a new mime_type optional parameter              | ✔️                  | ✔️                   | ✔️                   | GH-111439  |
| LineEdit                                                               |                     |                      |                      |            |
| Method edit adds a new hide_focus optional parameter                   | ✔️                  | ✔️                   | ✔️                   | GH-111117  |
| SplitContainer                                                         |                     |                      |                      |            |
| Method clamp_split_offset adds a new priority_index optional parameter | ✔️                  | ✔️                   | ✔️                   | GH-90411   |

#### Networking

| Change                                                           | GDScript Compatible | C# Binary Compatible | C# Source Compatible | Introduced |
| ---------------------------------------------------------------- | ------------------- | -------------------- | -------------------- | ---------- |
| StreamPeerTCP                                                    |                     |                      |                      |            |
| Method disconnect_from_host moved to base class StreamPeerSocket | ✔️                  | ✔️                   | ✔️                   | GH-107954  |
| Method get_status moved to base class StreamPeerSocket           | ✔️                  | ❌                   | ✔️                   | GH-107954  |
| Method poll moved to base class StreamPeerSocket                 | ✔️                  | ✔️                   | ✔️                   | GH-107954  |
| TCPServer                                                        |                     |                      |                      |            |
| Method is_connection_available moved to base class SocketServer  | ✔️                  | ✔️                   | ✔️                   | GH-107954  |
| Method is_listening moved to base class SocketServer             | ✔️                  | ✔️                   | ✔️                   | GH-107954  |
| Method stop moved to base class SocketServer                     | ✔️                  | ✔️                   | ✔️                   | GH-107954  |

#### OpenXR

| Change                                                                                 | GDScript Compatible | C# Binary Compatible | C# Source Compatible | Introduced |
| -------------------------------------------------------------------------------------- | ------------------- | -------------------- | -------------------- | ---------- |
| OpenXRExtensionWrapper                                                                 |                     |                      |                      |            |
| Method \_get_requested_extensions adds a new xr_version parameter                      | ❌                  | ❌                   | ❌                   | GH-109302  |
| Method \_set_instance_create_info_and_get_next_pointer adds a new xr_version parameter | N/A                 | N/A                  | N/A                  | GH-109302  |

> **Note:** The `OpenXRExtensionWrapper` type is intended to be subclassed from GDExtensions. The method `_set_instance_create_info_and_get_next_pointer` has a `void*` parameter so it's not exposed to scripting.

#### Editor

| Change                                                                                            | GDScript Compatible | C# Binary Compatible | C# Source Compatible | Introduced |
| ------------------------------------------------------------------------------------------------- | ------------------- | -------------------- | -------------------- | ---------- |
| EditorExportPreset                                                                                |                     |                      |                      |            |
| Method get_script_export_mode changes return type from int to EditorExportPreset.ScriptExportMode | ✔️                  | ❌                   | ❌                   | GH-107167  |
| EditorFileDialog                                                                                  |                     |                      |                      |            |
| Method add_filter moved to base class FileDialog                                                  | ✔️                  | ✔️                   | ✔️                   | GH-111212  |
| Method add_option moved to base class FileDialog                                                  | ✔️                  | ✔️                   | ✔️                   | GH-111212  |
| Method add_side_menu removed                                                                      | ❌                  | ❌                   | ❌                   | GH-111162  |
| Method clear_filename_filter moved to base class FileDialog                                       | ✔️                  | ✔️                   | ✔️                   | GH-111212  |
| Method clear_filters moved to base class FileDialog                                               | ✔️                  | ✔️                   | ✔️                   | GH-111212  |
| Method get_filename_filter moved to base class FileDialog                                         | ✔️                  | ✔️                   | ✔️                   | GH-111212  |
| Method get_line_edit moved to base class FileDialog                                               | ✔️                  | ✔️                   | ✔️                   | GH-111212  |
| Method get_option_default moved to base class FileDialog                                          | ✔️                  | ✔️                   | ✔️                   | GH-111212  |
| Method get_option_name moved to base class FileDialog                                             | ✔️                  | ✔️                   | ✔️                   | GH-111212  |
| Method get_option_values moved to base class FileDialog                                           | ✔️                  | ✔️                   | ✔️                   | GH-111212  |
| Method get_selected_options moved to base class FileDialog                                        | ✔️                  | ✔️                   | ✔️                   | GH-111212  |
| Method get_vbox moved to base class FileDialog                                                    | ✔️                  | ✔️                   | ✔️                   | GH-111212  |
| Method invalidate moved to base class FileDialog                                                  | ✔️                  | ✔️                   | ✔️                   | GH-111212  |
| Method popup_file_dialog moved to base class FileDialog                                           | ✔️                  | ✔️                   | ✔️                   | GH-111212  |
| Method set_filename_filter moved to base class FileDialog                                         | ✔️                  | ✔️                   | ✔️                   | GH-111212  |
| Method set_option_default moved to base class FileDialog                                          | ✔️                  | ✔️                   | ✔️                   | GH-111212  |
| Method set_option_name moved to base class FileDialog                                             | ✔️                  | ✔️                   | ✔️                   | GH-111212  |
| Method set_option_values moved to base class FileDialog                                           | ✔️                  | ✔️                   | ✔️                   | GH-111212  |
| Property access moved to base class FileDialog                                                    | ✔️                  | ❌                   | ✔️                   | GH-111212  |
| Property current_dir moved to base class FileDialog                                               | ✔️                  | ✔️                   | ✔️                   | GH-111212  |
| Property current_file moved to base class FileDialog                                              | ✔️                  | ✔️                   | ✔️                   | GH-111212  |
| Property current_path moved to base class FileDialog                                              | ✔️                  | ✔️                   | ✔️                   | GH-111212  |
| Property display_mode moved to base class FileDialog                                              | ✔️                  | ❌                   | ✔️                   | GH-111212  |
| Property file_mode moved to base class FileDialog                                                 | ✔️                  | ❌                   | ✔️                   | GH-111212  |
| Property filters moved to base class FileDialog                                                   | ✔️                  | ✔️                   | ✔️                   | GH-111212  |
| Property option_count moved to base class FileDialog                                              | ✔️                  | ✔️                   | ✔️                   | GH-111212  |
| Property show_hidden_files moved to base class FileDialog                                         | ✔️                  | ✔️                   | ✔️                   | GH-111212  |
| Signal dir_selected moved to base class FileDialog                                                | ✔️                  | ❌                   | ✔️                   | GH-111212  |
| Signal filename_filter_changed moved to base class FileDialog                                     | ✔️                  | ❌                   | ✔️                   | GH-111212  |
| Signal file_selected moved to base class FileDialog                                               | ✔️                  | ❌                   | ✔️                   | GH-111212  |
| Signal files_selected moved to base class FileDialog                                              | ✔️                  | ❌                   | ✔️                   | GH-111212  |

### Behavior changes

#### Android

> **Note:** The source sets configuration for Android export templates has been updated to match the default Android Studio project structure ([GH-110829](https://github.com/godotengine/godot/pull/110829)). This affects the directory layout of the Android project: - Files previously in `[Project root]/android/build/src/` are now in `[Project root]/android/build/src/main/java/`.

- Android manifest file and assets directory have been moved to `src/main/` subdirectories. For example, `GodotApp.java` moved from `src/com/godot/game/GodotApp.java` to `src/main/java/com/godot/game/GodotApp.java`.

#### Core

> **Note:** The TSCN file format has changed in two ways in Godot 4.6: - `load_steps` is no longer written in scene files. This attribute wasn't used by the editor.

- Unique node IDs are now saved to scene files to help track nodes when they are moved or renamed. This makes scene refactoring significantly more robust. The changes are backwards-compatible and forwards-compatible, which means scenes saved in Godot 4.5 can still be loaded in Godot 4.6 and vice-versa (notwithstanding other incompatible changes performed in the scene itself). As a result, when saving a scene that was last edited in Godot 4.5 in Godot 4.6, significant diffs will occur in version control programs. These diffs are expected. As a reminder, you can upgrade all files in a project to the latest format using Project > Tools > Upgrade Project Files... in the editor, then committing the changes to version control. This allows you to avoid large diffs later on when editing scenes.

#### Rendering

> **Note:** The default blend mode for Glow is now Screen, which looks more correct but is significantly brighter than the previous Soft Light mode ([GH-110671](https://github.com/godotengine/godot/pull/110671)). Several other glow defaults were changed to ensure the glow didn't become too strong, but you will likely need to tweak glow properties in Environment after upgrading. In addition, glow's Soft Light blend mode now always behaves as it did previously with `use_hdr_2d`, regardless of the Viewport's `use_hdr_2d` setting ([GH-109971](https://github.com/godotengine/godot/pull/109971)). When using the Mobile renderer, the rewritten glow effect will look significantly different to the previous one for performance reasons ([GH-110077](https://github.com/godotengine/godot/pull/110077)). You may need to further adjust glow settings in Environment to achieve a similar look to before.

> **Note:** Volumetric fog blending has been changed to be more physically accurate ([GH-112494](https://github.com/godotengine/godot/pull/112494)). This will cause volumetric fog to appear brighter in most scenes. To compensate for this, you will need to decrease volumetric fog density or brightness in Environment, or decrease the **Volumetric Fog Energy** property on specific lights.

#### Navigation

> **Note:** `AStar2D.get_point_path`, `AStar3D.get_point_path`, `AStarGrid2D.get_id_path` and `AStarGrid2D.get_point_path` will now return an empty path when `from_id` is a disabled/solid point ([GH-113988](https://github.com/godotengine/godot/pull/113988)).

### Changed defaults

The following default values have been changed. If your project relies on the previous defaults, you may need to explicitly set them to the old values.

> **Note:** The default rendering driver on Windows for **newly created** projects is now D3D12 ([GH-113213](https://github.com/godotengine/godot/pull/113213)). This can be changed in Project Settings under `rendering/rendering_device/driver.windows`.

> **Note:** The default 3D physics engine for **newly created** projects is now Jolt Physics ([GH-105737](https://github.com/godotengine/godot/pull/105737)). This can be changed in Project Settings under `physics/3d/physics_engine`.

#### 3D

| Member            | Old Value      | New Value    | Introduced |
| ----------------- | -------------- | ------------ | ---------- |
| MeshInstance3D    |                |              |            |
| Property skeleton | NodePath("..") | NodePath("") | GH-112267  |

> **Note:** The default value of `skeleton` has changed. Enable `animation/compatibility/default_parent_skeleton_in_mesh_instance_3d` in Project Settings if the old behavior is needed for compatibility.

#### Rendering

| Member                                                          | Old Value | New Value | Introduced |
| --------------------------------------------------------------- | --------- | --------- | ---------- |
| ProjectSettings                                                 |           |           |            |
| Property rendering/reflections/sky_reflections/roughness_layers | 8         | 7         | GH-107902  |
| Property rendering/rendering_device/d3d12/agility_sdk_version   | 613       | 618       | GH-114043  |
| Environment                                                     |           |           |            |
| Property glow_blend_mode                                        | 2         | 1         | GH-110671  |
| Property glow_intensity                                         | 0.8       | 0.3       | GH-110671  |
| Property glow_levels/2                                          | 0.0       | 0.8       | GH-110671  |
| Property glow_levels/3                                          | 1.0       | 0.4       | GH-110671  |
| Property glow_levels/4                                          | 0.0       | 0.1       | GH-110671  |
| Property glow_levels/5                                          | 1.0       | 0.0       | GH-110671  |
| Property ssr_depth_tolerance                                    | 0.2       | 0.5       | GH-111210  |

#### GUI nodes

| Property/Parameter             | Old Value | New Value | Introduced |
| ------------------------------ | --------- | --------- | ---------- |
| PopupMenu                      |           |           |            |
| Property submenu_popup_delay   | 0.3       | 0.2       | GH-110256  |
| ResourceImporterCSVTranslation |           |           |            |
| Property compress              | true      | 1         | GH-112073  |

---
