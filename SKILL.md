---
name: godot-csharp-api
description: Godot 4 C# API reference skill. Use when answering questions about Godot 4 C# development, class methods, properties, signals, enums, or constants. Provides condensed C#-only API docs for all ~1,065 Godot 4 engine classes, split into domain-specific files.
---

# Godot 4 C# API Reference Skill

This skill provides access to condensed, C#-specific Godot 4 API reference documentation.

All content is C#-only:

- Method names are **PascalCase** (e.g., `AddChild`, `GetNode`, `EmitSignal`)
- Property names are **PascalCase** (e.g., `GlobalPosition`, `ProcessMode`)
- Types use C# and Godot C# bindings: `string`, `float`, `bool`, `Godot.Collections.Array`, `StringName`, `NodePath`, `Variant`, etc.
- Code examples are C# only; all GDScript has been stripped

## Skill Files — Load as needed

When the user asks about a Godot class or concept, identify its domain from the table below, then read the corresponding file from `refernces/` to answer the question. For broad questions, start with `godot_csharp_core.md` as it contains the most fundamental classes.

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
- Properties are listed as `Type Name = default` — these are C# property accessors
- `[virtual]` methods are overridable in subclasses
- `[static]` methods are called on the class, not an instance
