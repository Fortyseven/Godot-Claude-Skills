# Godot 4 GDScript Tutorials — Migrating (Part 1)

> 4 tutorials. GDScript-specific code examples.

## Upgrading from Godot 4.0 to Godot 4.1

For most games and apps made with 4.0, it should be relatively safe to migrate to 4.1. This page intends to cover everything you need to pay attention to when migrating your project.

### Breaking changes

If you are migrating from 4.0 to 4.1, the breaking changes listed here might affect you. Changes are grouped by areas/systems.

> **Warning:** The GDExtension API completely breaks compatibility in 4.1, so it's not included in the table below. See the **Updating your GDExtension for 4.1** section for more information.

This article indicates whether each breaking change affects GDScript and whether the C# breaking change is _binary compatible_ or _source compatible_:

- **Binary compatible** - Existing binaries will load and execute successfully without recompilation, and the runtime behavior won't change.
- **Source compatible** - Source code will compile successfully without changes when upgrading Godot.

#### Core

| Change                                                                               | GDScript Compatible | C# Binary Compatible | C# Source Compatible | Introduced |
| ------------------------------------------------------------------------------------ | ------------------- | -------------------- | -------------------- | ---------- |
| Basis                                                                                |                     |                      |                      |            |
| Method looking_at adds a new use_model_front optional parameter                      | ✔️                  | ✔️                   | ✔️                   | GH-76082   |
| Object                                                                               |                     |                      |                      |            |
| Method get_meta_list changes return type from PackedStringArray to Array[StringName] | ✔️                  | ❌                   | ❌                   | GH-76418   |
| Transform3D                                                                          |                     |                      |                      |            |
| Method looking_at adds a new use_model_front optional parameter                      | ✔️                  | ✔️                   | ✔️                   | GH-76082   |
| UndoRedo                                                                             |                     |                      |                      |            |
| Method create_action adds a new backward_undo_ops optional parameter                 | ✔️                  | ✔️                   | ✔️                   | GH-76688   |
| WorkerThreadPool                                                                     |                     |                      |                      |            |
| Method wait_for_task_completion changes return type from void to Error               | ✔️                  | ❌                   | ✔️                   | GH-77143   |

#### Animation

| Change                                                                                 | GDScript Compatible | C# Binary Compatible | C# Source Compatible | Introduced |
| -------------------------------------------------------------------------------------- | ------------------- | -------------------- | -------------------- | ---------- |
| AnimationNode                                                                          |                     |                      |                      |            |
| Method \_process adds a new test_only parameter                                        | ❌                  | ❌                   | ❌                   | GH-75759   |
| Method blend_input adds a new test_only optional parameter                             | ✔️                  | ✔️                   | ✔️                   | GH-75759   |
| Method blend_node adds a new test_only optional parameter                              | ✔️                  | ✔️                   | ✔️                   | GH-75759   |
| AnimationNodeStateMachinePlayback                                                      |                     |                      |                      |            |
| Method get_travel_path changes return type from PackedStringArray to Array[StringName] | ✔️                  | ❌                   | ❌                   | GH-76418   |

#### 2D nodes

| Change                     | GDScript Compatible | C# Binary Compatible | C# Source Compatible | Introduced |
| -------------------------- | ------------------- | -------------------- | -------------------- | ---------- |
| PathFollow2D               |                     |                      |                      |            |
| Property lookahead removed | ❌                  | ❌                   | ❌                   | GH-72842   |

#### 3D nodes

| Change                                                                                            | GDScript Compatible | C# Binary Compatible | C# Source Compatible | Introduced |
| ------------------------------------------------------------------------------------------------- | ------------------- | -------------------- | -------------------- | ---------- |
| Geometry3D                                                                                        |                     |                      |                      |            |
| Method segment_intersects_convex changes planes parameter type from untyped Array to Array[Plane] | ✔️                  | ✔️                   | ❌                   | GH-76418   |
| MeshInstance3D                                                                                    |                     |                      |                      |            |
| Method create_multiple_convex_collisions adds a new settings optional parameter                   | ✔️                  | ✔️                   | ✔️                   | GH-72152   |
| Node3D                                                                                            |                     |                      |                      |            |
| Method look_at adds a new use_model_front optional parameter                                      | ✔️                  | ✔️                   | ✔️                   | GH-76082   |
| Method look_at_from_position adds a new use_model_front optional parameter                        | ✔️                  | ✔️                   | ✔️                   | GH-76082   |

#### GUI nodes

| Change                                                                   | GDScript Compatible | C# Binary Compatible | C# Source Compatible | Introduced |
| ------------------------------------------------------------------------ | ------------------- | -------------------- | -------------------- | ---------- |
| CodeEdit                                                                 |                     |                      |                      |            |
| Method add_code_completion_option adds a new location optional parameter | ✔️                  | ✔️                   | ✔️                   | GH-75746   |
| RichTextLabel                                                            |                     |                      |                      |            |
| Method push_list adds a new bullet optional parameter                    | ✔️                  | ✔️                   | ✔️                   | GH-75017   |
| Method push_paragraph adds a new justification_flags optional parameter  | ✔️                  | ✔️                   | ✔️                   | GH-75250   |
| Method push_paragraph adds a new tab_stops optional parameter            | ✔️                  | ✔️                   | ✔️                   | GH-76401   |
| Tree                                                                     |                     |                      |                      |            |
| Method edit_selected adds a new force_edit optional parameter            | ✔️                  | ✔️                   | ✔️                   | GH-76794   |

#### Physics

| Change                                                                                    | GDScript Compatible | C# Binary Compatible | C# Source Compatible | Introduced |
| ----------------------------------------------------------------------------------------- | ------------------- | -------------------- | -------------------- | ---------- |
| Area2D                                                                                    |                     |                      |                      |            |
| Property priority changes type from float to int                                          | ❌                  | ❌                   | ❌                   | GH-72749   |
| Area3D                                                                                    |                     |                      |                      |            |
| Property priority changes type from float to int                                          | ❌                  | ❌                   | ❌                   | GH-72749   |
| PhysicsDirectSpaceState2D                                                                 |                     |                      |                      |            |
| Method collide_shape changes return type from Array[PackedVector2Array] to Array[Vector2] | ❌                  | ❌                   | ❌                   | GH-75260   |
| PhysicsDirectSpaceState3D                                                                 |                     |                      |                      |            |
| Method collide_shape changes return type from Array[PackedVector3Array] to Array[Vector3] | ❌                  | ❌                   | ❌                   | GH-75260   |

#### Rendering

| Change                                                                                                  | GDScript Compatible | C# Binary Compatible | C# Source Compatible | Introduced |
| ------------------------------------------------------------------------------------------------------- | ------------------- | -------------------- | -------------------- | ---------- |
| RDShaderFile                                                                                            |                     |                      |                      |            |
| Method get_version_list changes return type from PackedStringArray to Array[StringName]                 | ✔️                  | ❌                   | ❌                   | GH-76418   |
| RenderingDevice                                                                                         |                     |                      |                      |            |
| Method draw_list_begin changes storage_textures parameter type from untyped Array to Array[RID]         | ✔️                  | ✔️                   | ❌                   | GH-76418   |
| RenderingServer                                                                                         |                     |                      |                      |            |
| Method global_shader_parameter_get_list changes return type from PackedStringArray to Array[StringName] | ✔️                  | ❌                   | ❌                   | GH-76418   |
| SurfaceTool                                                                                             |                     |                      |                      |            |
| Method add_triangle_fan changes tangents parameter type from untyped Array to Array[Plane]              | ✔️                  | ✔️                   | ❌                   | GH-76418   |

#### Navigation

| Change                                                                                                      | GDScript Compatible | C# Binary Compatible | C# Source Compatible | Introduced |
| ----------------------------------------------------------------------------------------------------------- | ------------------- | -------------------- | -------------------- | ---------- |
| NavigationAgent2D                                                                                           |                     |                      |                      |            |
| Method set_velocity replaced with velocity property                                                         | ✔️                  | ❌                   | ❌                   | GH-69988   |
| Property time_horizon split into time_horizon_agents and time_horizon_obstacles                             | ❌                  | ❌                   | ❌                   | GH-69988   |
| NavigationAgent3D                                                                                           |                     |                      |                      |            |
| Property agent_height_offset renamed to path_height_offset                                                  | ❌                  | ❌                   | ❌                   | GH-69988   |
| Property ignore_y removed                                                                                   | ❌                  | ❌                   | ❌                   | GH-69988   |
| Method set_velocity replaced with velocity property                                                         | ✔️                  | ❌                   | ❌                   | GH-69988   |
| Property time_horizon split into time_horizon_agents and time_horizon_obstacles                             | ❌                  | ❌                   | ❌                   | GH-69988   |
| NavigationObstacle2D                                                                                        |                     |                      |                      |            |
| Property estimate_radius removed                                                                            | ❌                  | ❌                   | ❌                   | GH-69988   |
| Method get_rid renamed to get_agent_rid                                                                     | ❌                  | ❌                   | ❌                   | GH-69988   |
| NavigationObstacle3D                                                                                        |                     |                      |                      |            |
| Property estimate_radius removed                                                                            | ❌                  | ❌                   | ❌                   | GH-69988   |
| Method get_rid renamed to get_agent_rid                                                                     | ❌                  | ❌                   | ❌                   | GH-69988   |
| NavigationServer2D                                                                                          |                     |                      |                      |            |
| Method agent_set_callback renamed to agent_set_avoidance_callback                                           | ❌                  | ❌                   | ❌                   | GH-69988   |
| Method agent_set_target_velocity removed                                                                    | ❌                  | ❌                   | ❌                   | GH-69988   |
| Method agent_set_time_horizon split into agent_set_time_horizon_agents and agent_set_time_horizon_obstacles | ❌                  | ❌                   | ❌                   | GH-69988   |
| NavigationServer3D                                                                                          |                     |                      |                      |            |
| Method agent_set_callback renamed to agent_set_avoidance_callback                                           | ❌                  | ❌                   | ❌                   | GH-69988   |
| Method agent_set_target_velocity removed                                                                    | ❌                  | ❌                   | ❌                   | GH-69988   |
| Method agent_set_time_horizon split into agent_set_time_horizon_agents and agent_set_time_horizon_obstacles | ❌                  | ❌                   | ❌                   | GH-69988   |

#### Networking

| Change                                                                            | GDScript Compatible | C# Binary Compatible | C# Source Compatible | Introduced |
| --------------------------------------------------------------------------------- | ------------------- | -------------------- | -------------------- | ---------- |
| WebRTCPeerConnectionExtension                                                     |                     |                      |                      |            |
| Method \_create_data_channel changes return type from Object to WebRTCDataChannel | ✔️                  | ❌                   | ✔️                   | GH-78237   |

#### Editor plugins

| Change                                                                    | GDScript Compatible | C# Binary Compatible | C# Source Compatible | Introduced |
| ------------------------------------------------------------------------- | ------------------- | -------------------- | -------------------- | ---------- |
| AnimationTrackEditPlugin                                                  |                     |                      |                      |            |
| Type AnimationTrackEditPlugin removed                                     | ❌                  | ❌                   | ❌                   | GH-76413   |
| EditorInterface                                                           |                     |                      |                      |            |
| Type EditorInterface changes inheritance from Node to Object              | ✔️                  | ❌                   | ❌                   | GH-76176   |
| Method set_movie_maker_enabled replaced with movie_maker_enabled property | ✔️                  | ❌                   | ❌                   | GH-76176   |
| Method is_movie_maker_enabled replaced with movie_maker_enabled property  | ✔️                  | ❌                   | ❌                   | GH-76176   |
| EditorResourcePreviewGenerator                                            |                     |                      |                      |            |
| Method \_generate adds a new metadata parameter                           | ❌                  | ❌                   | ❌                   | GH-64628   |
| Method \_generate_from_path adds a new metadata parameter                 | ❌                  | ❌                   | ❌                   | GH-64628   |
| EditorUndoRedoManager                                                     |                     |                      |                      |            |
| Method create_action adds a new backward_undo_ops optional parameter      | ✔️                  | ✔️                   | ✔️                   | GH-76688   |

### Behavior changes

In 4.1, some behavior changes have been introduced, which might require you to adjust your project.

| Change                                                                                                                                                                              | Introduced |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| SubViewportContainer                                                                                                                                                                |            |
| When input events should reach SubViewports and their children, SubViewportContainer.mouse_filter now needs to be MOUSE_FILTER_STOP or MOUSE_FILTER_PASS. See GH-79271 for details. | GH-57894   |
| Multiple layered SubViewportContainer nodes, that should all receive mouse input events, now need to be replaced by Area2D nodes. See GH-79128 for details.                         | GH-57894   |
| Viewport                                                                                                                                                                            |            |
| Viewport nodes, that have Physics Picking enabled, now automatically set InputEvents as handled. See GH-79897 for workarounds.                                                      | GH-77595   |

### Updating your GDExtension for 4.1

In order to fix a serious bug, in Godot 4.1 we had to break binary compatibility in a big way and source compatibility in a small way.

This means that GDExtensions made for Godot 4.0 will need to be recompiled for Godot 4.1 (using the `4.1` branch of godot-cpp), with a small change to their source code.

In Godot 4.0, your "entry_symbol" function looks something like this:

```cpp
GDExtensionBool GDE_EXPORT example_library_init(const GDExtensionInterface *p_interface, const GDExtensionClassLibraryPtr p_library, GDExtensionInitialization *r_initialization) {
    godot::GDExtensionBinding::InitObject init_obj(p_interface, p_library, r_initialization);

    init_obj.register_initializer(initialize_example_module);
    init_obj.register_terminator(uninitialize_example_module);
    init_obj.set_minimum_library_initialization_level(MODULE_INITIALIZATION_LEVEL_SCENE);

    return init_obj.init();
}
```

However, for Godot 4.1, it should look like:

```cpp
GDExtensionBool GDE_EXPORT example_library_init(GDExtensionInterfaceGetProcAddress p_get_proc_address, const GDExtensionClassLibraryPtr p_library, GDExtensionInitialization *r_initialization) {
    godot::GDExtensionBinding::InitObject init_obj(p_get_proc_address, p_library, r_initialization);

    init_obj.register_initializer(initialize_example_module);
    init_obj.register_terminator(uninitialize_example_module);
    init_obj.set_minimum_library_initialization_level(MODULE_INITIALIZATION_LEVEL_SCENE);

    return init_obj.init();
}
```

There are two small changes:

1. The first argument changes from `const GDExtensionInterface *p_interface` to `GDExtensionInterfaceGetProcAddress p_get_proc_address`
2. The constructor for the init_obj variable now receives `p_get_proc_address` as its first parameter

You also need to add an extra `compatibility_minimum` line to your `.gdextension` file, so that it looks something like:

```gdscript
[configuration]

entry_symbol = "example_library_init"
compatibility_minimum = 4.1
```

This lets Godot know that your GDExtension has been updated and is safe to load in Godot 4.1.

---

## Upgrading from Godot 4.1 to Godot 4.2

For most games and apps made with 4.1 it should be relatively safe to migrate to 4.2. This page intends to cover everything you need to pay attention to when migrating your project.

### Breaking changes

If you are migrating from 4.1 to 4.2, the breaking changes listed here might affect you. Changes are grouped by areas/systems.

> **Warning:** The [Mesh](../godot_gdscript_rendering.md) resource format has changed in 4.2 to allow for [vertex and attribute compression](https://github.com/godotengine/godot/pull/81138). This allows for improved rendering performance, especially on platforms constrained by memory bandwidth such as mobile. It is still possible to load the Godot 4.0-4.1 Mesh formats, but it is **not** possible to load the Godot 4.2 Mesh format in prior Godot versions. When opening a Godot project made with a version prior to 4.2, you may be presented with an upgrade dialog that offers two options: - **Restart & Upgrade:** Upgrades the mesh format for all meshes in the project and saves the result to disk. Once chosen, this option prevents downgrading the project to a Godot version prior to 4.2. Set up a version control system and push your changes _before_ choosing this option!

- **Upgrade Only:** Upgrades the mesh format in-memory without writing it to disk. This allows downgrading the project to a Godot version older than 4.2 if you need to do so in the future. The downside is that loading the project will be slower every time as the mesh format needs to be upgraded every time the project is loaded. These increased loading times will also affect the exported project. The number and complexity of Mesh resources determines how much loading times are affected. If this dialog doesn't appear, use **Project > Tools > Upgrade Mesh Surfaces…** at the top of the editor.

This article indicates whether each breaking change affects GDScript and whether the C# breaking change is _binary compatible_ or _source compatible_:

- **Binary compatible** - Existing binaries will load and execute successfully without recompilation, and the runtime behavior won't change.
- **Source compatible** - Source code will compile successfully without changes when upgrading Godot.

#### Core

| Change                                               | GDScript Compatible | C# Binary Compatible | C# Source Compatible | Introduced |
| ---------------------------------------------------- | ------------------- | -------------------- | -------------------- | ---------- |
| Node                                                 |                     |                      |                      |            |
| Constant NOTIFICATION_NODE_RECACHE_REQUESTED removed | ❌                  | ✔️                   | ❌                   | GH-84419   |

#### Animation

| Change                                                                                                 | GDScript Compatible | C# Binary Compatible | C# Source Compatible | Introduced |
| ------------------------------------------------------------------------------------------------------ | ------------------- | -------------------- | -------------------- | ---------- |
| AnimationPlayer                                                                                        |                     |                      |                      |            |
| Method \_post_process_key_value moved to base class AnimationMixer                                     | ✔️                  | ✔️                   | ✔️                   | GH-80813   |
| Method add_animation_library moved to base class AnimationMixer                                        | ✔️                  | ✔️                   | ✔️                   | GH-80813   |
| Method advance moved to base class AnimationMixer                                                      | ✔️                  | ✔️                   | ✔️                   | GH-80813   |
| Signal animation_finished moved to base class AnimationMixer                                           | ✔️                  | ❌                   | ❌                   | GH-80813   |
| Signal animation_started moved to base class AnimationMixer                                            | ✔️                  | ❌                   | ❌                   | GH-80813   |
| Signal animation_libraries_updated moved to base class AnimationMixer                                  | ✔️                  | ✔️                   | ✔️                   | GH-80813   |
| Signal animation_list_changed moved to base class AnimationMixer                                       | ✔️                  | ✔️                   | ✔️                   | GH-80813   |
| Property audio_max_polyphony moved to base class AnimationMixer                                        | ✔️                  | ✔️                   | ✔️                   | GH-80813   |
| Signal caches_cleared moved to base class AnimationMixer                                               | ✔️                  | ✔️                   | ✔️                   | GH-80813   |
| Method clear_caches moved to base class AnimationMixer                                                 | ✔️                  | ✔️                   | ✔️                   | GH-80813   |
| Method find_animation moved to base class AnimationMixer                                               | ✔️                  | ✔️                   | ✔️                   | GH-80813   |
| Method find_animation_library moved to base class AnimationMixer                                       | ✔️                  | ✔️                   | ✔️                   | GH-80813   |
| Method get_animation moved to base class AnimationMixer                                                | ✔️                  | ✔️                   | ✔️                   | GH-80813   |
| Method get_animation_library moved to base class AnimationMixer                                        | ✔️                  | ✔️                   | ✔️                   | GH-80813   |
| Method get_animation_library_list moved to base class AnimationMixer                                   | ✔️                  | ✔️                   | ✔️                   | GH-80813   |
| Method get_animation_list moved to base class AnimationMixer                                           | ✔️                  | ✔️                   | ✔️                   | GH-80813   |
| Method has_animation moved to base class AnimationMixer                                                | ✔️                  | ✔️                   | ✔️                   | GH-80813   |
| Method has_animation_library moved to base class AnimationMixer                                        | ✔️                  | ✔️                   | ✔️                   | GH-80813   |
| Property method_call_mode renamed to callback_mode_method and moved to base class AnimationMixer       | ✔️                  | ✔️                   | ✔️                   | GH-80813   |
| Property playback_active renamed to active and moved to base class AnimationMixer                      | ✔️                  | ✔️                   | ✔️                   | GH-80813   |
| Property playback_process_mode renamed to callback_mode_process and moved to base class AnimationMixer | ✔️                  | ✔️                   | ✔️                   | GH-80813   |
| Method remove_animation_library moved to base class AnimationMixer                                     | ✔️                  | ✔️                   | ✔️                   | GH-80813   |
| Method rename_animation_library moved to base class AnimationMixer                                     | ✔️                  | ✔️                   | ✔️                   | GH-80813   |
| Property reset_on_save moved to base class AnimationMixer                                              | ✔️                  | ✔️                   | ✔️                   | GH-80813   |
| Property root_node moved to base class AnimationMixer                                                  | ✔️                  | ✔️                   | ✔️                   | GH-80813   |
| Method set_reset_on_save_enabled moved to base class AnimationMixer                                    | ✔️                  | ✔️                   | ✔️                   | GH-80813   |
| Method seek adds a new update_only optional parameter                                                  | ✔️                  | ✔️                   | ✔️                   | GH-80813   |
| AnimationTree                                                                                          |                     |                      |                      |            |
| Method \_post_process_key_value moved to base class AnimationMixer                                     | ✔️                  | ✔️                   | ✔️                   | GH-80813   |
| Property active moved to base class AnimationMixer                                                     | ✔️                  | ✔️                   | ✔️                   | GH-80813   |
| Method advance moved to base class AnimationMixer                                                      | ✔️                  | ✔️                   | ✔️                   | GH-80813   |
| Signal animation_finished moved to base class AnimationMixer                                           | ✔️                  | ❌                   | ❌                   | GH-80813   |
| Signal animation_started moved to base class AnimationMixer                                            | ✔️                  | ❌                   | ❌                   | GH-80813   |
| Property audio_max_polyphony moved to base class AnimationMixer                                        | ✔️                  | ✔️                   | ✔️                   | GH-80813   |
| Method get_root_motion_position moved to base class AnimationMixer                                     | ✔️                  | ✔️                   | ✔️                   | GH-80813   |
| Method get_root_motion_position_accumulator moved to base class AnimationMixer                         | ✔️                  | ✔️                   | ✔️                   | GH-80813   |
| Method get_root_motion_rotation moved to base class AnimationMixer                                     | ✔️                  | ✔️                   | ✔️                   | GH-80813   |
| Method get_root_motion_rotation_accumulator moved to base class AnimationMixer                         | ✔️                  | ✔️                   | ✔️                   | GH-80813   |
| Method get_root_motion_scale moved to base class AnimationMixer                                        | ✔️                  | ✔️                   | ✔️                   | GH-80813   |
| Method get_root_motion_scale_accumulator moved to base class AnimationMixer                            | ✔️                  | ✔️                   | ✔️                   | GH-80813   |
| Property process_callback renamed to callback_mode_process and moved to base class AnimationMixer      | ✔️                  | ✔️                   | ✔️                   | GH-80813   |
| Property root_motion_track moved to base class AnimationMixer                                          | ✔️                  | ✔️                   | ✔️                   | GH-80813   |
| Property tree_root changes type from AnimationNode to AnimationRootNode                                | ✔️                  | ❌                   | ❌                   | GH-80813   |

#### GUI nodes

| Change                                                                               | GDScript Compatible | C# Binary Compatible | C# Source Compatible | Introduced |
| ------------------------------------------------------------------------------------ | ------------------- | -------------------- | -------------------- | ---------- |
| PopupMenu                                                                            |                     |                      |                      |            |
| Method add_icon_shortcut adds a new allow_echo optional parameter                    | ✔️                  | ✔️                   | ✔️                   | GH-36493   |
| Method add_shortcut adds a new allow_echo optional parameter                         | ✔️                  | ✔️                   | ✔️                   | GH-36493   |
| Method clear adds a new free_submenus optional parameter                             | ✔️                  | ✔️                   | ✔️                   | GH-79965   |
| RichTextLabel                                                                        |                     |                      |                      |            |
| Method add_image adds new key, pad, tooltip, and size_in_percent optional parameters | ✔️                  | ✔️                   | ✔️                   | GH-80410   |

#### Rendering

| Change                                                                                 | GDScript Compatible | C# Binary Compatible | C# Source Compatible | Introduced |
| -------------------------------------------------------------------------------------- | ------------------- | -------------------- | -------------------- | ---------- |
| ImporterMesh                                                                           |                     |                      |                      |            |
| Method add_surface changes flags parameter type from uint32 to uint64                  | ✔️                  | ✔️                   | ✔️                   | GH-81138   |
| Method get_surface_format changes return type from uint32 to uint64                    | ✔️                  | ❌                   | ❌                   | GH-81138   |
| MeshDataTool                                                                           |                     |                      |                      |            |
| Method commit_to_surface adds a new compression_flags optional parameter               | ✔️                  | ✔️                   | ✔️                   | GH-81138   |
| Method get_format changes return type from uint32 to uint64                            | ✔️                  | ❌                   | ❌                   | GH-81138   |
| RenderingDevice                                                                        |                     |                      |                      |            |
| Enum field BarrierMask.BARRIER_MASK_RASTER changes value from 1 to 9                   | ✔️                  | ✔️                   | ✔️                   | GH-79911   |
| Enum field BarrierMask.BARRIER_MASK_ALL_BARRIERS changes value from 7 to 32767         | ✔️                  | ✔️                   | ✔️                   | GH-79911   |
| Enum field BarrierMask.BARRIER_MASK_NO_BARRIER changes value from 8 to 32768           | ✔️                  | ✔️                   | ✔️                   | GH-79911   |
| Method shader_create_from_bytecode adds a new placeholder_rid optional parameter       | ✔️                  | ✔️                   | ✔️                   | GH-79606   |
| Method shader_get_vertex_input_attribute_ask changes return type from uint32 to uint64 | ✔️                  | ❌                   | ❌                   | GH-81138   |
| SurfaceTool                                                                            |                     |                      |                      |            |
| Method commit changes flags parameter type from uint32 to uint64                       | ✔️                  | ✔️                   | ✔️                   | GH-81138   |

#### Text

| Change                                                                                                           | GDScript Compatible | C# Binary Compatible | C# Source Compatible | Introduced |
| ---------------------------------------------------------------------------------------------------------------- | ------------------- | -------------------- | -------------------- | ---------- |
| Font                                                                                                             |                     |                      |                      |            |
| Method set_fallbacks replaced with fallbacks property                                                            | ✔️                  | ❌                   | ❌                   | GH-78266   |
| Method get_fallbacks replaced with fallbacks property                                                            | ✔️                  | ❌                   | ❌                   | GH-78266   |
| Method find_variation adds new spacing_top, spacing_bottom, spacing_space, and spacing_glyph optional parameters | ✔️                  | ✔️                   | ✔️                   | GH-80954   |

#### GraphEdit

| Change                                                                              | GDScript Compatible | C# Binary Compatible | C# Source Compatible | Introduced |
| ----------------------------------------------------------------------------------- | ------------------- | -------------------- | -------------------- | ---------- |
| GraphEdit                                                                           |                     |                      |                      |            |
| Property arrange_nodes_button_hidden renamed to show_arrange_button                 | ❌                  | ✔️                   | ✔️                   | GH-81582   |
| Method get_zoom_hbox renamed to get_menu_hbox                                       | ❌                  | ✔️                   | ✔️                   | GH-79308   |
| Property snap_distance renamed to snapping_distance                                 | ❌                  | ✔️                   | ✔️                   | GH-79308   |
| Property use_snap renamed to snapping_enabled                                       | ❌                  | ✔️                   | ✔️                   | GH-79308   |
| GraphNode                                                                           |                     |                      |                      |            |
| Property comment removed                                                            | ❌                  | ❌                   | ❌                   | GH-79307   |
| Signal close_request renamed to delete_request and moved to base class GraphElement | ❌                  | ✔️                   | ✔️                   | GH-79311   |
| Property draggable moved to base class GraphElement                                 | ✔️                  | ✔️                   | ✔️                   | GH-79311   |
| Property draggable moved to base class GraphElement                                 | ✔️                  | ✔️                   | ✔️                   | GH-79311   |
| Signal dragged moved to base class GraphElement                                     | ✔️                  | ❌                   | ❌                   | GH-79311   |
| Method get_connection_input_color removed                                           | ❌                  | ❌                   | ❌                   | GH-79311   |
| Method get_connection_input_count removed                                           | ❌                  | ❌                   | ❌                   | GH-79311   |
| Method get_connection_input_height removed                                          | ❌                  | ❌                   | ❌                   | GH-79311   |
| Method get_connection_input_position removed                                        | ❌                  | ❌                   | ❌                   | GH-79311   |
| Method get_connection_input_slot removed                                            | ❌                  | ❌                   | ❌                   | GH-79311   |
| Method get_connection_input_type removed                                            | ❌                  | ❌                   | ❌                   | GH-79311   |
| Method get_connection_output_color removed                                          | ❌                  | ❌                   | ❌                   | GH-79311   |
| Method get_connection_output_count removed                                          | ❌                  | ❌                   | ❌                   | GH-79311   |
| Method get_connection_output_height removed                                         | ❌                  | ❌                   | ❌                   | GH-79311   |
| Method get_connection_output_position removed                                       | ❌                  | ❌                   | ❌                   | GH-79311   |
| Method get_connection_output_slot removed                                           | ❌                  | ❌                   | ❌                   | GH-79311   |
| Method get_connection_output_type removed                                           | ❌                  | ❌                   | ❌                   | GH-79311   |
| Property language removed                                                           | ❌                  | ❌                   | ❌                   | GH-79311   |
| Signal node_deselected moved to base class GraphElement                             | ✔️                  | ✔️                   | ✔️                   | GH-79311   |
| Signal node_selected moved to base class GraphElement                               | ✔️                  | ✔️                   | ✔️                   | GH-79311   |
| Property overlay removed                                                            | ❌                  | ❌                   | ❌                   | GH-79311   |
| Property position_offset moved to base class GraphElement                           | ✔️                  | ✔️                   | ✔️                   | GH-79311   |
| Signal position_offset_changed moved to base class GraphElement                     | ✔️                  | ✔️                   | ✔️                   | GH-79311   |
| Signal raise_request moved to base class GraphElement                               | ✔️                  | ✔️                   | ✔️                   | GH-79311   |
| Property resizable moved to base class GraphElement                                 | ✔️                  | ✔️                   | ✔️                   | GH-79311   |
| Signal resize_request moved to base class GraphElement                              | ✔️                  | ❌                   | ❌                   | GH-79311   |
| Property selectable moved to base class GraphElement                                | ✔️                  | ✔️                   | ✔️                   | GH-79311   |
| Property selected moved to base class GraphElement                                  | ✔️                  | ✔️                   | ✔️                   | GH-79311   |
| Property show_close removed                                                         | ❌                  | ❌                   | ❌                   | GH-79311   |
| Property text_direction removed                                                     | ❌                  | ❌                   | ❌                   | GH-79311   |

#### TileMap

| Change                                                         | GDScript Compatible | C# Binary Compatible | C# Source Compatible | Introduced |
| -------------------------------------------------------------- | ------------------- | -------------------- | -------------------- | ---------- |
| TileMap                                                        |                     |                      |                      |            |
| Property cell_quadrant_size renamed to rendering_quadrant_size | ❌                  | ✔️                   | ✔️                   | GH-81070   |

#### XR

| Change                                | GDScript Compatible | C# Binary Compatible | C# Source Compatible | Introduced |
| ------------------------------------- | ------------------- | -------------------- | -------------------- | ---------- |
| XRInterface                           |                     |                      |                      |            |
| Property environment_blend_mode added | ✔️                  | ❌                   | ❌                   | GH-81561   |

> **Note:** This change breaks compatibility in C# because the new property conflicts with the name of an existing enum and the C# bindings generator gives priority to properties, so the enum type was renamed from `EnvironmentBlendMode` to `EnvironmentBlendModeEnum`.

---

## Upgrading from Godot 4.2 to Godot 4.3

For most games and apps made with 4.2 it should be relatively safe to migrate to 4.3. This page intends to cover everything you need to pay attention to when migrating your project.

### Breaking changes

If you are migrating from 4.2 to 4.3, the breaking changes listed here might affect you. Changes are grouped by areas/systems.

This article indicates whether each breaking change affects GDScript and whether the C# breaking change is _binary compatible_ or _source compatible_:

- **Binary compatible** - Existing binaries will load and execute successfully without recompilation, and the runtime behavior won't change.
- **Source compatible** - Source code will compile successfully without changes when upgrading Godot.

#### GDExtension

| Change                            | GDScript Compatible | C# Binary Compatible | C# Source Compatible | Introduced |
| --------------------------------- | ------------------- | -------------------- | -------------------- | ---------- |
| GDExtension                       |                     |                      |                      |            |
| Method close_library removed      | ❌                  | ❌                   | ❌                   | GH-88418   |
| Method initialize_library removed | ❌                  | ❌                   | ❌                   | GH-88418   |
| Method open_library removed       | ❌                  | ❌                   | ❌                   | GH-88418   |

Since it was basically impossible to use these methods in any useful way, these methods have been removed. Use `GDExtensionManager::load_extension` and `GDExtensionManager::unload_extension` instead to correctly load and unload a GDExtension.

#### Animation

| Change                                                                              | GDScript Compatible | C# Binary Compatible | C# Source Compatible | Introduced |
| ----------------------------------------------------------------------------------- | ------------------- | -------------------- | -------------------- | ---------- |
| Animation                                                                           |                     |                      |                      |            |
| Method position_track_interpolate adds a new backward optional parameter            | ✔️                  | ✔️                   | ✔️                   | GH-86629   |
| Method rotation_track_interpolate adds a new backward optional parameter            | ✔️                  | ✔️                   | ✔️                   | GH-86629   |
| Method scale_track_interpolate adds a new backward optional parameter               | ✔️                  | ✔️                   | ✔️                   | GH-86629   |
| Method blend_shape_track_interpolate adds a new backward optional parameter         | ✔️                  | ✔️                   | ✔️                   | GH-86629   |
| Method value_track_interpolate adds a new backward optional parameter               | ✔️                  | ✔️                   | ✔️                   | GH-86629   |
| Method track_find_key adds a new limit optional parameter                           | ✔️                  | ✔️                   | ✔️                   | GH-86661   |
| Method track_find_key adds a new backward optional parameter                        | ✔️                  | ✔️                   | ✔️                   | GH-92861   |
| AnimationMixer                                                                      |                     |                      |                      |            |
| Method \_post_process_key_value changes object parameter type from Object to uint64 | ✔️                  | ❌                   | ❌                   | GH-86687   |
| Skeleton3D                                                                          |                     |                      |                      |            |
| Method add_bone changes return type from void to int32                              | ✔️                  | ❌                   | ✔️                   | GH-88791   |
| Signal bone_pose_changed replaced by skeleton_updated                               | ❌                  | ❌                   | ❌                   | GH-90575   |
| BoneAttachment3D                                                                    |                     |                      |                      |            |
| Method on_bone_pose_update replaced by on_skeleton_update                           | ✔️                  | ✔️                   | ✔️                   | GH-90575   |

#### GUI nodes

| Change                                                                               | GDScript Compatible | C# Binary Compatible | C# Source Compatible | Introduced |
| ------------------------------------------------------------------------------------ | ------------------- | -------------------- | -------------------- | ---------- |
| AcceptDialog                                                                         |                     |                      |                      |            |
| Method register_text_enter changes parameter line_edit type from Control to LineEdit | ✔️                  | ✔️                   | ✔️                   | GH-89419   |
| Method remove_button changes parameter button type from Control to Button            | ✔️                  | ✔️                   | ✔️                   | GH-89419   |

#### Physics

| Change                                               | GDScript Compatible | C# Binary Compatible | C# Source Compatible | Introduced |
| ---------------------------------------------------- | ------------------- | -------------------- | -------------------- | ---------- |
| PhysicsShapeQueryParameters3D                        |                     |                      |                      |            |
| Property motion changes type from Vector2 to Vector3 | ❌                  | ❌                   | ❌                   | GH-85393   |

> **Note:** In C#, the enum `PhysicsServer3D.G6DofJointAxisFlag` breaks compatibility because of the way the bindings generator detects the enum prefix. New members were added in [GH-89851](https://github.com/godotengine/godot/pull/89851) to the enum that caused the enum members to be renamed.

#### Rendering

| Change                                                                                  | GDScript Compatible | C# Binary Compatible | C# Source Compatible | Introduced |
| --------------------------------------------------------------------------------------- | ------------------- | -------------------- | -------------------- | ---------- |
| RenderingDevice                                                                         |                     |                      |                      |            |
| Enum field FinalAction.FINAL_ACTION_CONTINUE changes value from 2 to 0                  | ✔️                  | ❌                   | ❌                   | GH-84976   |
| Enum field InitialAction.INITIAL_ACTION_CLEAR changes value from 0 to 1                 | ✔️                  | ❌                   | ❌                   | GH-84976   |
| Enum field InitialAction.INITIAL_ACTION_CLEAR_REGION_CONTINUE changes value from 2 to 1 | ✔️                  | ❌                   | ❌                   | GH-84976   |
| Enum field InitialAction.INITIAL_ACTION_CONTINUE changes value from 5 to 0              | ✔️                  | ❌                   | ❌                   | GH-84976   |
| Enum field InitialAction.INITIAL_ACTION_DROP changes value from 4 to 2                  | ✔️                  | ❌                   | ❌                   | GH-84976   |
| Enum field InitialAction.INITIAL_ACTION_KEEP changes value from 3 to 0                  | ✔️                  | ❌                   | ❌                   | GH-84976   |
| Method buffer_clear removes post_barrier parameter                                      | ✔️                  | ✔️                   | ✔️                   | GH-84976   |
| Method buffer_update removes post_barrier parameter                                     | ✔️                  | ✔️                   | ✔️                   | GH-84976   |
| Method compute_list_begin removes allow_draw_overlap parameter                          | ✔️                  | ✔️                   | ✔️                   | GH-84976   |
| Method compute_list_end removes post_barrier parameter                                  | ✔️                  | ✔️                   | ✔️                   | GH-84976   |
| Method draw_list_begin removes storage_textures parameter                               | ✔️                  | ✔️                   | ✔️                   | GH-84976   |
| Method draw_list_end removes post_barrier parameter                                     | ✔️                  | ✔️                   | ✔️                   | GH-84976   |
| Method texture_clear removes post_barrier parameter                                     | ✔️                  | ✔️                   | ✔️                   | GH-84976   |
| Method texture_copy removes post_barrier parameter                                      | ✔️                  | ✔️                   | ✔️                   | GH-84976   |
| Method texture_resolve_multisample removes post_barrier parameter                       | ✔️                  | ✔️                   | ✔️                   | GH-84976   |
| Method texture_update removes post_barrier parameter                                    | ✔️                  | ✔️                   | ✔️                   | GH-84976   |
| RenderingServer                                                                         |                     |                      |                      |            |
| Method environment_set_fog adds a new fog_mode optional parameter                       | ✔️                  | ✔️                   | ✔️                   | GH-84792   |
| RenderSceneBuffersRD                                                                    |                     |                      |                      |            |
| Method get_color_layer adds a new msaa optional parameter                               | ✔️                  | ✔️                   | ✔️                   | GH-80214   |
| Method get_depth_layer adds a new msaa optional parameter                               | ✔️                  | ✔️                   | ✔️                   | GH-80214   |
| Method get_velocity_layer adds a new msaa optional parameter                            | ✔️                  | ✔️                   | ✔️                   | GH-80214   |
| Method get_color_texture adds a new msaa optional parameter                             | ✔️                  | ✔️                   | ✔️                   | GH-80214   |
| Method get_depth_texture adds a new msaa optional parameter                             | ✔️                  | ✔️                   | ✔️                   | GH-80214   |
| Method get_velocity_texture adds a new msaa optional parameter                          | ✔️                  | ✔️                   | ✔️                   | GH-80214   |

> **Note:** While the values of the enum fields in `RenderingDevice.InitialAction` and `RenderingDevice.FinalAction` changed, the only method that consumed them (`draw_list_begin`) added a compatibility method which supports the old values. So in practice it doesn't break compatibility.

> **Note:** In C#, the enum `RenderingDevice.DriverResource` breaks compatibility because of the way the bindings generator detects the enum prefix. New members were added in [GH-83452](https://github.com/godotengine/godot/pull/83452) to the enum that caused the enum members to be renamed.

#### Text

| Change                                                                               | GDScript Compatible | C# Binary Compatible | C# Source Compatible | Introduced |
| ------------------------------------------------------------------------------------ | ------------------- | -------------------- | -------------------- | ---------- |
| Font                                                                                 |                     |                      |                      |            |
| Method find_variation adds a new baseline_offset optional parameter                  | ✔️                  | ✔️                   | ✔️                   | GH-87668   |
| RichTextLabel                                                                        |                     |                      |                      |            |
| Method push_meta adds a new underline_mode optional parameter                        | ✔️                  | ✔️                   | ✔️                   | GH-89024   |
| TextServer                                                                           |                     |                      |                      |            |
| Method shaped_text_get_word_breaks adds a new optional skip_grapheme_flags parameter | ✔️                  | ✔️                   | ✔️                   | GH-90732   |
| TextServerExtension                                                                  |                     |                      |                      |            |
| Method \_shaped_text_get_word_breaks adds a new skip_grapheme_flags parameter        | ❌                  | ❌                   | ❌                   | GH-90732   |

#### Audio

| Change                                                                 | GDScript Compatible | C# Binary Compatible | C# Source Compatible | Introduced |
| ---------------------------------------------------------------------- | ------------------- | -------------------- | -------------------- | ---------- |
| AudioStreamPlaybackPolyphonic                                          |                     |                      |                      |            |
| Method play_stream adds new playback_type, and bus optional parameters | ✔️                  | ✔️                   | ✔️                   | GH-91382   |

#### Navigation

| Change                                                               | GDScript Compatible | C# Binary Compatible | C# Source Compatible | Introduced |
| -------------------------------------------------------------------- | ------------------- | -------------------- | -------------------- | ---------- |
| AStar2D                                                              |                     |                      |                      |            |
| Method get_id_path adds new allow_partial_path optional parameter    | ✔️                  | ✔️                   | ✔️                   | GH-88047   |
| Method get_point_path adds new allow_partial_path optional parameter | ✔️                  | ✔️                   | ✔️                   | GH-88047   |
| AStar3D                                                              |                     |                      |                      |            |
| Method get_id_path adds new allow_partial_path optional parameter    | ✔️                  | ✔️                   | ✔️                   | GH-88047   |
| Method get_point_path adds new allow_partial_path optional parameter | ✔️                  | ✔️                   | ✔️                   | GH-88047   |
| AStarGrid2D                                                          |                     |                      |                      |            |
| Method get_id_path adds new allow_partial_path optional parameter    | ✔️                  | ✔️                   | ✔️                   | GH-88047   |
| Method get_point_path adds new allow_partial_path optional parameter | ✔️                  | ✔️                   | ✔️                   | GH-88047   |
| NavigationRegion2D                                                   |                     |                      |                      |            |
| Property avoidance_layers removed                                    | ❌                  | ❌                   | ❌                   | GH-90747   |
| Property constrain_avoidance removed                                 | ❌                  | ❌                   | ❌                   | GH-90747   |
| Method get_avoidance_layer_value removed                             | ❌                  | ❌                   | ❌                   | GH-90747   |
| Method set_avoidance_layer_value removed                             | ❌                  | ❌                   | ❌                   | GH-90747   |

> **Note:** The constrain avoidance feature in `NavigationRegion2D` was experimental and has been discontinued with no replacement.

#### TileMap

| Change                                                                                   | GDScript Compatible | C# Binary Compatible | C# Source Compatible | Introduced |
| ---------------------------------------------------------------------------------------- | ------------------- | -------------------- | -------------------- | ---------- |
| TileData                                                                                 |                     |                      |                      |            |
| Method get_navigation_polygon adds new flip_h, flip_v, and transpose optional parameters | ✔️                  | ✔️                   | ✔️                   | GH-84660   |
| Method get_occluder adds new flip_h, flip_v, and transpose optional parameters           | ✔️                  | ✔️                   | ✔️                   | GH-84660   |

#### XR

| Change                                                                                              | GDScript Compatible | C# Binary Compatible | C# Source Compatible | Introduced |
| --------------------------------------------------------------------------------------------------- | ------------------- | -------------------- | -------------------- | ---------- |
| WebXRInterface                                                                                      |                     |                      |                      |            |
| Method get_input_source_tracker changes return type from XRPositionalTracker to XRControllerTracker | ✔️                  | ❌                   | ✔️                   | GH-90645   |
| XRServer                                                                                            |                     |                      |                      |            |
| Method get_tracker changes return type from XRPositionalTracker to XRTracker                        | ✔️                  | ❌                   | ❌                   | GH-90645   |

#### Editor plugins

| Change                                                                    | GDScript Compatible | C# Binary Compatible | C# Source Compatible | Introduced |
| ------------------------------------------------------------------------- | ------------------- | -------------------- | -------------------- | ---------- |
| EditorInspectorPlugin                                                     |                     |                      |                      |            |
| Method add_property_editor adds a new label optional parameter            | ✔️                  | ✔️                   | ✔️                   | GH-92322   |
| EditorPlugin                                                              |                     |                      |                      |            |
| Method add_control_to_bottom_panel adds a new shortcut optional parameter | ✔️                  | ✔️                   | ✔️                   | GH-88081   |
| Method add_control_to_dock adds a new shortcut optional parameter         | ✔️                  | ✔️                   | ✔️                   | GH-88081   |
| EditorSceneFormatImporterFBX                                              |                     |                      |                      |            |
| Type renamed to EditorSceneFormatImporterFBX2GLTF                         | ❌                  | ❌                   | ❌                   | GH-81746   |

### Behavior changes

In 4.3, some behavior changes have been introduced, which might require you to adjust your project.

#### Core

> **Note:** Binary serialization was modified to fix some issues with the serialization of scripted Objects and typed Arrays ([GH-78219](https://github.com/godotengine/godot/pull/78219)). This breaks compat with script encoding/decoding.

> **Note:** `PackedByteArray` is now able to use a more compact base64 encoding for storage. But the trade-off is that it breaks compatibility, meaning that older versions of Godot may not be able to open resources saved by 4.3 ([GH-89186](https://github.com/godotengine/godot/pull/89186)). To maximize compatibility, this new storage format will only be enabled for resources and scenes that contain large PackedByteArrays for now. Support for this new format will also be added in patch updates for older versions of Godot. Once all supported Godot versions are able to read the new format, we will gradually retire the compatibility measures and have all resources and scenes use the new storage format.

> **Note:** In C#, the `Transform3D.InterpolateWith` implementation was fixed to use the right order of operations, applying the rotation before the scale ([GH-89843](https://github.com/godotengine/godot/pull/89843)).

> **Note:** In C#, the `Aabb.GetSupport` implementation was fixed to properly return the support vector ([GH-88919](https://github.com/godotengine/godot/pull/88919)).

> **Note:** In C#, the Variant types' `ToString` implementation now defaults to using the `InvariantCulture` ([GH-89547](https://github.com/godotengine/godot/pull/89547)) which means `Vector2(1.2, 3.4)` is formatted using `.` as the decimal separator independently of the language of the operating system that the program is running on.

#### Animation

> **Note:** `AnimationMixer` replaced its Capture mode with a new Capture feature that works much better than the old one, this replaces the existing cache ([GH-86715](https://github.com/godotengine/godot/pull/86715)).

> **Note:** `AnimationNode` has a reworked process for retrieving the semantic time info. This ensures that time-related behavior works as expected, but changes the blending behavior. Implementors of the `_process` virtual method should also note that this method is now deprecated and will be replaced by a new one in the future ([GH-87171](https://github.com/godotengine/godot/pull/87171)).

More information about the changes to Animation can be found in the [Migrating Animations from Godot 4.0 to 4.3](https://godotengine.org/article/migrating-animations-from-godot-4-0-to-4-3) article.

#### GUI nodes

> **Note:** The default font outline color was changed from white to black ([GH-54641](https://github.com/godotengine/godot/pull/54641)).

> **Note:** The `auto_translate` property is deprecated in favor of the `auto_translate_mode` property which is now in `Node` ([GH-87530](https://github.com/godotengine/godot/pull/87530)). The default value for `auto_translate_mode` is `AUTO_TRANSLATE_INHERIT`, which means nodes inherit the `auto_translate_mode` value from their parent. This means, existing nodes with the `auto_translate` property set to `true` may no longer be translated if they are children of a node with the `auto_translate` property set to `false`.

#### Multiplayer

> **Note:** The `SceneMultiplayer` caching protocol was changed to send the received ID instead of the Node path when sending a node removal confirmation packet ([GH-90027](https://github.com/godotengine/godot/pull/90027)). This is a breaking change for the high-level multiplayer protocol making it incompatible with previous Godot versions. Upgrade both your server and client versions to Godot 4.3 to handle this change gracefully. Note that high-level multiplayer facilities are only ever meant to be compatible with server and client using the same Godot version. It is recommended to implement some kind of version checking.

#### Rendering

> **Note:** Decals now convert the modulate color from an sRGB color to a linear color, like all other inputs, to ensure proper blending ([GH-89849](https://github.com/godotengine/godot/pull/89849)). Existing projects that were using the decal's modulate property will notice a change in their visuals.

> **Note:** The reverse Z depth buffer technique is now implemented. This may break compatibility for some shaders. Read the [Introducing Reverse Z (AKA I'm sorry for breaking your shader)](https://godotengine.org/article/introducing-reverse-z/) article for more information and guidance on how to fix common scenarios.

#### TileMap

> **Note:** `TileMap` layers were moved to individual nodes ([GH-87379](https://github.com/godotengine/godot/pull/87379) and [GH-89179](https://github.com/godotengine/godot/pull/89179)).

#### Android

> **Note:** Android permissions are no longer requested automatically because it goes against the recommended best practices ([GH-87080](https://github.com/godotengine/godot/pull/87080)). Use the `request_permission` method in `OS` and the `on_request_permissions_result` signal on `MainLoop` to request permissions and wait for the user response.

---

## Upgrading from Godot 4.3 to Godot 4.4

For most games and apps made with 4.3 it should be relatively safe to migrate to 4.4. This page intends to cover everything you need to pay attention to when migrating your project.

### Breaking changes

If you are migrating from 4.3 to 4.4, the breaking changes listed here might affect you. Changes are grouped by areas/systems.

This article indicates whether each breaking change affects GDScript and whether the C# breaking change is _binary compatible_ or _source compatible_:

- **Binary compatible** - Existing binaries will load and execute successfully without recompilation, and the run-time behavior won't change.
- **Source compatible** - Source code will compile successfully without changes when upgrading Godot.

#### Core

| Change                                                               | GDScript Compatible | C# Binary Compatible | C# Source Compatible | Introduced |
| -------------------------------------------------------------------- | ------------------- | -------------------- | -------------------- | ---------- |
| FileAccess                                                           |                     |                      |                      |            |
| Method open_encrypted adds a new iv optional parameter               | ✔️                  | ✔️                   | ✔️                   | GH-98918   |
| Method store_8 changes return type from void to bool                 | ✔️                  | ❌                   | ✔️                   | GH-78289   |
| Method store_16 changes return type from void to bool                | ✔️                  | ❌                   | ✔️                   | GH-78289   |
| Method store_32 changes return type from void to bool                | ✔️                  | ❌                   | ✔️                   | GH-78289   |
| Method store_64 changes return type from void to bool                | ✔️                  | ❌                   | ✔️                   | GH-78289   |
| Method store_buffer changes return type from void to bool            | ✔️                  | ❌                   | ✔️                   | GH-78289   |
| Method store_csv_line changes return type from void to bool          | ✔️                  | ❌                   | ✔️                   | GH-78289   |
| Method store_double changes return type from void to bool            | ✔️                  | ❌                   | ✔️                   | GH-78289   |
| Method store_float changes return type from void to bool             | ✔️                  | ❌                   | ✔️                   | GH-78289   |
| Method store_half changes return type from void to bool              | ✔️                  | ❌                   | ✔️                   | GH-78289   |
| Method store_line changes return type from void to bool              | ✔️                  | ❌                   | ✔️                   | GH-78289   |
| Method store_pascal_string changes return type from void to bool     | ✔️                  | ❌                   | ✔️                   | GH-78289   |
| Method store_real changes return type from void to bool              | ✔️                  | ❌                   | ✔️                   | GH-78289   |
| Method store_string changes return type from void to bool            | ✔️                  | ❌                   | ✔️                   | GH-78289   |
| Method store_var changes return type from void to bool               | ✔️                  | ❌                   | ✔️                   | GH-78289   |
| OS                                                                   |                     |                      |                      |            |
| Method execute_with_pipe adds a new blocking optional parameter      | ✔️                  | ✔️                   | ✔️                   | GH-94434   |
| Method read_string_from_stdin adds a new buffer_size parameter [1]   | ❌                  | ✔️                   | ✔️                   | GH-91201   |
| RegEx                                                                |                     |                      |                      |            |
| Method compile adds a new show_error optional parameter              | ✔️                  | ✔️                   | ✔️                   | GH-95212   |
| Method create_from_string adds a new show_error optional parameter   | ✔️                  | ✔️                   | ✔️                   | GH-95212   |
| Semaphore                                                            |                     |                      |                      |            |
| Method post adds a new count optional parameter                      | ✔️                  | ✔️                   | ✔️                   | GH-93605   |
| TranslationServer                                                    |                     |                      |                      |            |
| Method standardize_locale adds a new add_defaults optional parameter | ✔️                  | ✔️                   | ✔️                   | GH-98972   |

**Export annotations**

> **Warning:** The behavior of `@export_file` changed in Godot 4.4. When assigning a new value from the Inspector, the path is now stored and returned as a `uid://` reference instead of the traditional `res://` path([GH-97912](https://github.com/godotengine/godot/pull/97912)). This is a **breaking change** and may cause issues if you're expecting `res://`-based paths in scripts or serialized files. For example, exported arrays of files may now contain a mix of `uid://` and `res://` paths, especially if they were partially edited in the Inspector. In 4.4, the only way to retain the `res://` format is to **manually edit** the .tscn or .tres files in a text editor. Starting in Godot 4.5, a new annotation `@export_file_path` can be used to explicitly retain the old behavior and export raw `res://` paths.

[**1**]

Default buffer size in 4.3 is `1024`.

#### GUI nodes

| Change                                                                          | GDScript Compatible | C# Binary Compatible | C# Source Compatible | Introduced |
| ------------------------------------------------------------------------------- | ------------------- | -------------------- | -------------------- | ---------- |
| RichTextLabel                                                                   |                     |                      |                      |            |
| Method push_meta adds a new tooltip optional parameter                          | ✔️                  | ✔️                   | ✔️                   | GH-99481   |
| Method set_table_column_expand adds a new shrink optional parameter             | ✔️                  | ✔️                   | ✔️                   | GH-101482  |
| GraphEdit                                                                       |                     |                      |                      |            |
| Method connect_node adds a new keep_alive optional parameter                    | ✔️                  | ✔️                   | ✔️                   | GH-97449   |
| Signal frame_rect_changed changes new_rect parameter type from Vector2 to Rect2 | ❌                  | ❌                   | ❌                   | GH-102796  |

#### Physics

| Change                                                          | GDScript Compatible | C# Binary Compatible | C# Source Compatible | Introduced |
| --------------------------------------------------------------- | ------------------- | -------------------- | -------------------- | ---------- |
| SoftBody3D                                                      |                     |                      |                      |            |
| Method set_point_pinned adds a new insert_at optional parameter | ✔️                  | ✔️                   | ✔️                   | GH-94684   |

#### Rendering

| Change                                                                                        | GDScript Compatible | C# Binary Compatible | C# Source Compatible | Introduced |
| --------------------------------------------------------------------------------------------- | ------------------- | -------------------- | -------------------- | ---------- |
| CPUParticles2D                                                                                |                     |                      |                      |            |
| Method restart adds a new keep_seed optional parameter                                        | ✔️                  | ✔️                   | ✔️                   | GH-92089   |
| CPUParticles3D                                                                                |                     |                      |                      |            |
| Method restart adds a new keep_seed optional parameter                                        | ✔️                  | ✔️                   | ✔️                   | GH-92089   |
| GPUParticles2D                                                                                |                     |                      |                      |            |
| Method restart adds a new keep_seed optional parameter                                        | ✔️                  | ✔️                   | ✔️                   | GH-92089   |
| GPUParticles3D                                                                                |                     |                      |                      |            |
| Method restart adds a new keep_seed optional parameter                                        | ✔️                  | ✔️                   | ✔️                   | GH-92089   |
| RenderingDevice                                                                               |                     |                      |                      |            |
| Method draw_list_begin adds a new breadcrumb optional parameter                               | ✔️                  | ✔️                   | ✔️                   | GH-90993   |
| Method draw_list_begin removes many parameters                                                | ❌                  | ✔️                   | ✔️                   | GH-98670   |
| Method index_buffer_create adds a new enable_device_address optional parameter                | ✔️                  | ✔️                   | ✔️                   | GH-100062  |
| Method uniform_buffer_create adds a new enable_device_address optional parameter              | ✔️                  | ✔️                   | ✔️                   | GH-100062  |
| Method vertex_buffer_create adds a new enable_device_address optional parameter               | ✔️                  | ✔️                   | ✔️                   | GH-100062  |
| RenderingServer                                                                               |                     |                      |                      |            |
| Method multimesh_allocate_data adds a new use_indirect optional parameter                     | ✔️                  | ✔️                   | ✔️                   | GH-99455   |
| Shader                                                                                        |                     |                      |                      |            |
| Method get_default_texture_parameter changes return type from Texture2D to Texture            | ✔️                  | ❌                   | ❌                   | GH-95126   |
| Method set_default_texture_parameter changes texture parameter type from Texture2D to Texture | ✔️                  | ❌                   | ✔️                   | GH-95126   |
| VisualShaderNodeCubemap                                                                       |                     |                      |                      |            |
| Property cube_map changes type from Cubemap to TextureLayered                                 | ✔️                  | ❌                   | ❌                   | GH-95126   |
| VisualShaderNodeTexture2DArray                                                                |                     |                      |                      |            |
| Property texture_array changes type from Texture2DArray to TextureLayered                     | ✔️                  | ❌                   | ❌                   | GH-95126   |

> **Note:** In C#, the enum `RenderingDevice.StorageBufferUsage` breaks compatibility because of the way the bindings generator detects the enum prefix. New members where added in [GH-100062](https://github.com/godotengine/godot/pull/100062) to the enum that caused the enum members to be renamed.

#### Navigation

| Change                                                   | GDScript Compatible | C# Binary Compatible | C# Source Compatible | Introduced |
| -------------------------------------------------------- | ------------------- | -------------------- | -------------------- | ---------- |
| NavigationServer2D                                       |                     |                      |                      |            |
| Method query_path adds a new callback optional parameter | ✔️                  | ✔️                   | ✔️                   | GH-100129  |
| NavigationServer3D                                       |                     |                      |                      |            |
| Method query_path adds a new callback optional parameter | ✔️                  | ✔️                   | ✔️                   | GH-100129  |

#### Editor plugins

| Change                                                                                                   | GDScript Compatible | C# Binary Compatible | C# Source Compatible | Introduced |
| -------------------------------------------------------------------------------------------------------- | ------------------- | -------------------- | -------------------- | ---------- |
| EditorInterface                                                                                          |                     |                      |                      |            |
| Method open_scene_from_path adds a new set_inherited optional parameter                                  | ✔️                  | ✔️                   | ✔️                   | GH-90057   |
| Method popup_node_selector adds a new current_value optional parameter                                   | ✔️                  | ✔️                   | ✔️                   | GH-94323   |
| Method popup_property_selector adds a new current_value optional parameter                               | ✔️                  | ✔️                   | ✔️                   | GH-94323   |
| EditorSceneFormatImporter                                                                                |                     |                      |                      |            |
| Method \_get_import_flags removed                                                                        | ❌                  | ❌                   | ❌                   | GH-101531  |
| EditorTranslationParserPlugin                                                                            |                     |                      |                      |            |
| Method \_parse_file changes return type to Array and removes msgids and msgids_context_plural parameters | ❌                  | ❌                   | ❌                   | GH-99297   |

> **Note:** The method `_get_import_flags` was never used by the engine. It was removed despite the compatibility breakage as there's no way for users to rely on this affecting engine behavior.

### Behavior changes

#### Core

> **Note:** The `Curve` resource now enforces its value range, so `min_value` and `max_value` need to be changed if any of the points fall outside of the default `[0, 1]` range.

#### Rendering

> **Note:** The `VisualShaderNodeVec4Constant` shader node had its input type changed to `Vector4`. Users need to recreate the values in their constants.

#### CSG

> **Note:** The CSG implementation now uses Emmett Lalish's [Manifold](https://github.com/elalish/manifold) library ([GH-94321](https://github.com/godotengine/godot/pull/94321)). The new implementation is more consistent with manifold definitions and fixes a number of bugs and stability issues. As a result, non-manifold meshes are no longer supported. You can use `MeshInstance3D` for rendering non-manifold geometry, such as quads or planes.

#### Android

> **Note:** Android sensor events are no longer enabled by default ([GH-94799](https://github.com/godotengine/godot/pull/94799)). Projects that use sensor events can enable them as needed in Project Settings under **Input Devices > Sensors**.

---
