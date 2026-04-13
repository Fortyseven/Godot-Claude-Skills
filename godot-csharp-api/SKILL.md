---
name: godot-csharp-api
description: Godot 4 C# API reference and tutorials skill. Use when answering questions about Godot 4 C# development, class methods, properties, signals, enums, constants, or how-to guides. Provides condensed C#-only API docs for all ~1,065 Godot 4 engine classes plus 347 official tutorials, split into domain-specific files. Do NOT use for GDScript Godot development — use godot-gdscript-api instead.
---

# Godot 4 C# API Reference Skill

This skill provides access to condensed, C#-specific Godot 4 API reference documentation.

All content is C#-only:

- Method names are **PascalCase** (e.g., `AddChild`, `GetNode`, `EmitSignal`)
- Property names are **PascalCase** (e.g., `GlobalPosition`, `ProcessMode`)
- Types use C# and Godot C# bindings: `string`, `float`, `bool`, `Godot.Collections.Array`, `StringName`, `NodePath`, `Variant`, etc.
- Code examples are C# only; all GDScript has been stripped

## Skill Files — Load as needed

1. Identify the domain of the queried class or concept from the table below.
2. Read the corresponding file from `references/`.
3. Answer using the loaded content. For broad questions, start with `godot_csharp_core.md`.

| File                          | Domain / Contents                                                                                                                                                              |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `godot_csharp_core.md`        | Object, Engine, OS, SceneTree, MainLoop, RefCounted, Resource, ResourceLoader/Saver, Performance, WorkerThreadPool, Thread, Mutex, Semaphore, ClassDB                          |
| `godot_csharp_nodes_2d.md`    | Node2D, Sprite2D, AnimatedSprite2D, Camera2D, CanvasItem, CanvasLayer, TileMap, Line2D, Polygon2D, CollisionShape2D, RayCast2D, CharacterBody2D, RigidBody2D, Area2D, joints   |
| `godot_csharp_nodes_3d.md`    | Node3D, MeshInstance3D, Camera3D, lights (Directional/Omni/Spot), GPUParticles3D, Skeleton3D, CharacterBody3D, RigidBody3D, Area3D, VehicleBody3D, navigation 3D               |
| `godot_csharp_physics.md`     | PhysicsServer2D/3D, PhysicsBody2D/3D, PhysicsDirectBodyState, shape classes, joints 3D, collision query parameters                                                             |
| `godot_csharp_ui_controls.md` | Control, Button, Label, LineEdit, TextEdit, RichTextLabel, Container variants, Panel, FileDialog, Window, PopupMenu, Tree, ItemList, Slider, ScrollBar, ColorPicker, GraphEdit |
| `godot_csharp_rendering.md`   | RenderingServer, RenderingDevice, Viewport, SubViewport, Environment, Sky, Material variants, Shader, VisualShader, Mesh variants, MultiMesh, SurfaceTool, MeshDataTool        |
| `godot_csharp_audio.md`       | AudioStreamPlayer (2D/3D), AudioServer, AudioStream variants, all AudioEffect\* classes                                                                                        |
| `godot_csharp_input.md`       | Input, InputMap, InputEvent variants (Key, Mouse, Joypad, Action, Touch, MIDI)                                                                                                 |
| `godot_csharp_animation.md`   | AnimationPlayer, AnimationTree, AnimationMixer, all AnimationNode\* classes, Tween, Tweener variants                                                                           |
| `godot_csharp_resources.md`   | Texture variants, Image, Gradient, Curve, Font variants, TileSet, StyleBox variants, Theme, PackedScene, Animation, Noise/FastNoiseLite                                        |
| `godot_csharp_networking.md`  | HTTPClient, HTTPRequest, WebSocketPeer, ENetMultiplayerPeer, MultiplayerAPI, StreamPeer variants, PacketPeer variants, Crypto, TLSOptions                                      |
| `godot_csharp_filesystem.md`  | FileAccess, DirAccess, ProjectSettings, ConfigFile, JSON, XMLParser, ZIPReader, ZIPPacker                                                                                      |
| `godot_csharp_math_types.md`  | Vector2/2i/3/3i/4/4i, Transform2D/3D, Basis, Quaternion, AABB, Rect2/2i, Plane, Color, Projection, RID                                                                         |
| `godot_csharp_editor.md`      | All Editor\* classes (EditorPlugin, EditorScript, EditorInspector, EditorFileSystem, etc.)                                                                                     |
| `godot_csharp_misc_part1.md`  | A–N classes not in other domains (~285 classes including Node, SceneTree-related, GDExtension, etc.)                                                                           |
| `godot_csharp_misc_part2.md`  | N–Z classes not in other domains (~135 classes including Signal buses, XR, callable utilities, etc.)                                                                           |

## Tutorial References — Load for "how to" questions

For _how to_ questions (not just "what does X do?"), load the matching tutorial file from `references/tutorials/`. Tutorials show how to use classes together for specific tasks, complementing the API reference above.

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
| Scripting       | `tutorials/tutorials_scripting_part1.md` … `_part12.md`      | C# basics, signals, groups, resources, scenes, autoloads, debugging, cross-language, GDScript, GDExtension, C++                                     |
| Shaders         | `tutorials/tutorials_shaders_part1.md` … `_part7.md`         | Shader intro, shader language reference, spatial/canvas/particle/sky/fog shaders, visual shaders                                                    |
| UI              | `tutorials/tutorials_ui_part1.md` … `_part4.md`              | Control nodes, themes, containers, size/anchors, BBCode, custom GUI, fonts                                                                          |
| XR              | `tutorials/tutorials_xr_part1.md` … `_part4.md`              | OpenXR setup, VR/AR, hand tracking, passthrough, deploy to headset                                                                                  |
| General         | `tutorials/tutorials_general.md`                             | Troubleshooting                                                                                                                                     |

## Routing Heuristic

### Step 1: Specific term lookup (KEYWORD_INDEX.md)

If the query contains a **specific term, attribute, function, or pattern** (e.g., `[Export]`, `[GlobalClass]`, `GetNode`, `PackedScene`, `EditorPlugin`):
1. Load `references/KEYWORD_INDEX.md`.
2. Find the term and note which file(s) contain it.
3. Load those file(s) and answer from their content.

### Step 2: Topic-based lookup (tutorials_index.md)

If the query is a **how-to question** and the keyword index does not help:
1. Load `references/tutorials/tutorials_index.md`.
2. Scan section headers to find the relevant tutorial file.
3. Load that file and answer from its content.

### Step 3: Domain-based routing (fallback)

For **API questions** ("what does X do?"), load the matching API reference file from the table above.
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
- **C# scripting** → `tutorials/tutorials_scripting_*`
- **Navigation / pathfinding** → `tutorials/tutorials_navigation_*`
- **Physics setup** → physics.md + `tutorials/tutorials_physics_*`
- **XR / VR / AR** → `tutorials/tutorials_xr_*`
- **Unknown class** → search misc_part1.md then misc_part2.md
- For broad questions, load core.md first as it contains the most fundamental classes

## Notes

- Godot version: **4.x** (stable)
- Generated from the official Godot HTML documentation
- Properties are listed as `Type Name = default` — these are C# property accessors
- `[virtual]` methods are overridable in subclasses
- `[static]` methods are called on the class, not an instance
