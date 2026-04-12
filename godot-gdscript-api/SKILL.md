---
name: godot-gdscript-api
description: Godot 4 GDScript API reference and tutorials skill. Use when answering questions about Godot 4 GDScript development, class methods, properties, signals, enums, constants, or how-to guides. Provides condensed GDScript-only API docs for all ~1,065 Godot 4 engine classes plus 347 official tutorials, split into domain-specific files.
---

# Godot 4 GDScript API Reference Skill

This skill provides access to condensed, GDScript-specific Godot 4 API reference documentation.

All content is GDScript-native:

- Method names are **snake_case** (e.g., `add_child`, `get_node`, `emit_signal`)
- Property names are **snake_case** (e.g., `global_position`, `process_mode`)
- Types use GDScript built-in names: `String`, `int`, `float`, `bool`, `Array`, `Dictionary`, `Callable`, `Signal`, `Variant`, `StringName`, `NodePath`, etc.
- Code examples are GDScript only; all C# has been stripped

## Skill Files — Load as needed

When the user asks about a Godot class or concept, identify its domain from the table below, then read the corresponding file from `references/` to answer the question. For broad questions, start with `godot_gdscript_core.md` as it contains the most fundamental classes.

| File                            | Domain / Contents                                                                                                                                                              |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `godot_gdscript_core.md`        | Object, Engine, OS, SceneTree, MainLoop, RefCounted, Resource, ResourceLoader/Saver, Performance, WorkerThreadPool, Thread, Mutex, Semaphore, ClassDB                          |
| `godot_gdscript_nodes_2d.md`    | Node2D, Sprite2D, AnimatedSprite2D, Camera2D, CanvasItem, CanvasLayer, TileMap, Line2D, Polygon2D, CollisionShape2D, RayCast2D, CharacterBody2D, RigidBody2D, Area2D, joints   |
| `godot_gdscript_nodes_3d.md`    | Node3D, MeshInstance3D, Camera3D, lights (Directional/Omni/Spot), GPUParticles3D, Skeleton3D, CharacterBody3D, RigidBody3D, Area3D, VehicleBody3D, navigation 3D               |
| `godot_gdscript_physics.md`     | PhysicsServer2D/3D, PhysicsBody2D/3D, PhysicsDirectBodyState, shape classes, joints 3D, collision query parameters                                                             |
| `godot_gdscript_ui_controls.md` | Control, Button, Label, LineEdit, TextEdit, RichTextLabel, Container variants, Panel, FileDialog, Window, PopupMenu, Tree, ItemList, Slider, ScrollBar, ColorPicker, GraphEdit |
| `godot_gdscript_rendering.md`   | RenderingServer, RenderingDevice, Viewport, SubViewport, Environment, Sky, Material variants, Shader, VisualShader, Mesh variants, MultiMesh, SurfaceTool, MeshDataTool        |
| `godot_gdscript_audio.md`       | AudioStreamPlayer (2D/3D), AudioServer, AudioStream variants, all AudioEffect\* classes                                                                                        |
| `godot_gdscript_input.md`       | Input, InputMap, InputEvent variants (Key, Mouse, Joypad, Action, Touch, MIDI)                                                                                                 |
| `godot_gdscript_animation.md`   | AnimationPlayer, AnimationTree, AnimationMixer, all AnimationNode\* classes, Tween, Tweener variants                                                                           |
| `godot_gdscript_resources.md`   | Texture variants, Image, Gradient, Curve, Font variants, TileSet, StyleBox variants, Theme, PackedScene, Animation, Noise/FastNoiseLite                                        |
| `godot_gdscript_networking.md`  | HTTPClient, HTTPRequest, WebSocketPeer, ENetMultiplayerPeer, MultiplayerAPI, StreamPeer variants, PacketPeer variants, Crypto, TLSOptions                                      |
| `godot_gdscript_filesystem.md`  | FileAccess, DirAccess, ProjectSettings, ConfigFile, JSON, XMLParser, ZIPReader, ZIPPacker                                                                                      |
| `godot_gdscript_math_types.md`  | Vector2/2i/3/3i/4/4i, Transform2D/3D, Basis, Quaternion, AABB, Rect2/2i, Plane, Color, Projection, RID                                                                         |
| `godot_gdscript_editor.md`      | All Editor\* classes (EditorPlugin, EditorScript, EditorInspector, EditorFileSystem, etc.)                                                                                     |
| `godot_gdscript_misc_part1.md`  | A–N classes not in other domains (~285 classes including Node, SceneTree-related, GDExtension, etc.)                                                                           |
| `godot_gdscript_misc_part2.md`  | N–Z classes not in other domains (~135 classes including Signal buses, XR, callable utilities, etc.)                                                                           |

## Tutorial References — Load for "how to" questions

When the user asks _how to do something_ (not just what a class/method is), load the relevant tutorial file from `references/tutorials/`. Tutorials show how to use classes together for specific tasks, complementing the API reference above.

| Category        | Files                                                        | Topics                                                                                                                                              |
| --------------- | ------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| 2D              | `tutorials/tutorials_2d_part1.md` … `_part3.md`              | 2D movement, sprites, animation, particles, tilemaps, parallax, lighting, antialiasing, canvas layers, custom drawing                               |
| 3D              | `tutorials/tutorials_3d_part1.md` … `_part9.md`              | 3D intro, lights/shadows, environment, materials, meshes, particles, procedural geometry, LOD, occlusion, fog, GI, text, CSG, GridMaps, decals, VRS |
| Animation       | `tutorials/tutorials_animation_part1.md` … `_part2.md`       | AnimationPlayer, AnimationTree, cutout animation, 2D skeletons, track types, video playback                                                         |
| Assets Pipeline | `tutorials/tutorials_assets_pipeline_part1.md` … `_part2.md` | Importing 3D scenes/images/audio, retargeting skeletons, export formats                                                                             |
| Audio           | `tutorials/tutorials_audio.md`                               | Audio buses, effects, streams, recording, sync, text-to-speech                                                                                      |
| Best Practices  | `tutorials/tutorials_best_practices_part1.md` … `_part2.md`  | Project/scene organization, autoloads, data preferences, node alternatives, version control                                                         |
| Editor          | `tutorials/tutorials_editor_part1.md` … `_part3.md`          | Editor introduction, project manager, default keybindings, command palette, external editor                                                         |
| Export          | `tutorials/tutorials_export_part1.md` … `_part3.md`          | Exporting projects, feature tags, platform-specific exports (Android, iOS, web, desktop)                                                            |
| I18n            | `tutorials/tutorials_i18n_part1.md` … `_part2.md`            | Internationalization, localization, translations                                                                                                    |
| Inputs          | `tutorials/tutorials_inputs.md`                              | Input handling, input map, controllers, mouse/keyboard, custom cursors                                                                              |
| I/O             | `tutorials/tutorials_io.md`                                  | File access, saving/loading, data paths, config files, encryption                                                                                   |
| Math            | `tutorials/tutorials_math_part1.md` … `_part2.md`            | Vector math, matrices, transforms, interpolation, random numbers, bezier curves                                                                     |
| Migrating       | `tutorials/tutorials_migrating_part1.md` … `_part3.md`       | Migrating from Godot 3 to 4, version-specific changes                                                                                               |
| Navigation      | `tutorials/tutorials_navigation_part1.md` … `_part3.md`      | Navigation meshes, agents, obstacles, pathfinding, avoidance                                                                                        |
| Networking      | `tutorials/tutorials_networking.md`                          | High-level multiplayer, RPCs, HTTP requests, WebSocket, ENet                                                                                        |
| Performance     | `tutorials/tutorials_performance_part1.md` … `_part2.md`     | Optimization, profiling, multithreading, vertex animation, batching                                                                                 |
| Physics         | `tutorials/tutorials_physics_part1.md` … `_part3.md`         | Physics bodies, collision layers, raycasting, joints, soft bodies, interpolation                                                                    |
| Platform        | `tutorials/tutorials_platform_part1.md` … `_part2.md`        | Android, iOS, web, Linux platform-specific guides                                                                                                   |
| Plugins         | `tutorials/tutorials_plugins_part1.md` … `_part2.md`         | EditorPlugin, inspector plugins, tool scripts, GDExtension                                                                                          |
| Rendering       | `tutorials/tutorials_rendering_part1.md` … `_part2.md`       | Viewports, render pipeline, 2D/3D rendering, screen-reading shaders                                                                                 |
| Scripting       | `tutorials/tutorials_scripting_part1.md` … `_part12.md`      | GDScript basics, signals, groups, resources, scenes, autoloads, debugging, cross-language, C#, GDExtension, C++                                     |
| Shaders         | `tutorials/tutorials_shaders_part1.md` … `_part7.md`         | Shader intro, shader language reference, spatial/canvas/particle/sky/fog shaders, visual shaders                                                    |
| UI              | `tutorials/tutorials_ui_part1.md` … `_part4.md`              | Control nodes, themes, containers, size/anchors, BBCode, custom GUI, fonts                                                                          |
| XR              | `tutorials/tutorials_xr_part1.md` … `_part4.md`              | OpenXR setup, VR/AR, hand tracking, passthrough, deploy to headset                                                                                  |
| General         | `tutorials/tutorials_general.md`                             | Troubleshooting                                                                                                                                     |

## Routing Heuristic

For **API questions** ("what does X do?"), use the API reference files above.
For **how-to questions** ("how do I move a character?"), load both the API reference AND the matching tutorial file.

- **Scene tree, nodes, lifecycle** → core.md + nodes_2d.md or nodes_3d.md
- **2D gameplay** → nodes*2d.md + physics.md + `tutorials/tutorials_2d*\*`
- **3D gameplay** → nodes*3d.md + physics.md + `tutorials/tutorials_3d*\*`
- **UI / HUD** → ui*controls.md + `tutorials/tutorials_ui*\*`
- **Visual effects, materials, shaders** → rendering.md + `tutorials/tutorials_shaders_*`
- **Sound** → audio.md + `tutorials/tutorials_audio.md`
- **Player input** → input.md + `tutorials/tutorials_inputs.md`
- **Animations, tweens** → animation.md + `tutorials/tutorials_animation_*`
- **Images, fonts, themes** → resources.md
- **Multiplayer, HTTP** → networking.md + `tutorials/tutorials_networking.md`
- **File I/O, settings** → filesystem.md + `tutorials/tutorials_io.md`
- **Math, geometry** → math*types.md + `tutorials/tutorials_math*\*`
- **Editor tooling / plugins** → editor.md + `tutorials/tutorials_plugins_*`
- **GDScript language** → `tutorials/tutorials_scripting_*`
- **Navigation / pathfinding** → `tutorials/tutorials_navigation_*`
- **Physics setup** → physics.md + `tutorials/tutorials_physics_*`
- **XR / VR / AR** → `tutorials/tutorials_xr_*`
- **Unknown class** → search misc_part1.md then misc_part2.md
- For broad questions, load core.md first as it contains the most fundamental classes

## Notes

- Godot version: **4.x** (stable)
- Generated from the official Godot HTML documentation
- Properties are listed as `Type name = default` — these are GDScript property accessors
- `[virtual]` methods are overridable in subclasses via `func _method_name()`
- `[static]` methods are called on the class, not an instance
- Method names use snake_case: `add_child()`, `get_node()`, `set_position()`, etc.
- Signal connections use `signal_name.connect(callable)` in GDScript 4.x
