---
name: godot-gdscript-api
description: Godot 4 GDScript API reference skill. Use when answering questions about Godot 4 GDScript development, class methods, properties, signals, enums, or constants. Provides condensed GDScript-only API docs for all ~1,065 Godot 4 engine classes, split into domain-specific files.
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

## Routing Heuristic

- **Scene tree, nodes, lifecycle** → core.md + nodes_2d.md or nodes_3d.md
- **2D gameplay** → nodes_2d.md + physics.md
- **3D gameplay** → nodes_3d.md + physics.md
- **UI / HUD** → ui_controls.md
- **Visual effects, materials, shaders** → rendering.md
- **Sound** → audio.md
- **Player input** → input.md
- **Animations, tweens** → animation.md
- **Images, fonts, themes** → resources.md
- **Multiplayer, HTTP** → networking.md
- **File I/O, settings** → filesystem.md
- **Math, geometry** → math_types.md
- **Editor tooling / plugins** → editor.md
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
