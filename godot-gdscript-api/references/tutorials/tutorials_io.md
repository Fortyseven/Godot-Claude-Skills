# Godot 4 GDScript Tutorials — Io

> 5 tutorials. GDScript-specific code examples.

## Background loading

Commonly, games need to load resources asynchronously. When switching the main scene of your game (e.g. going to a new level), you might want to show a loading screen with some indication that progress is being made, or you may want to load additional resources during gameplay.

The standard load method ([ResourceLoader.load](../godot_gdscript_core.md) or GDScript's simpler `load`) blocks your thread, making your game appear unresponsive while the resource is being loaded.

One way around this is using `ResourceLoader` to load resources asynchronously in background threads.

### Using ResourceLoader

Generally, you queue requests to load resources for a path using [ResourceLoader.load_threaded_request](../godot_gdscript_core.md), which will then be loaded in threads in the background.

You can check the status with [ResourceLoader.load_threaded_get_status](../godot_gdscript_core.md). Progress can be obtained by passing an array variable via progress which will return a one element array containing the percentage.

Finally, you retrieve loaded resources by calling [ResourceLoader.load_threaded_get](../godot_gdscript_core.md).

Once you call `load_threaded_get()`, either the resource finished loading in the background and will be returned instantly or the load will block at this point like `load()` would. If you want to guarantee this does not block, you either need to ensure there is enough time between requesting the load and retrieving the resource or you need to check the status manually.

### Example

This example demonstrates how to load a scene in the background. We will have a button spawn an enemy when pressed. The enemy will be `Enemy.tscn` which we will load on `_ready` and instantiate when pressed. The path will be `"Enemy.tscn"` which is located at `res://Enemy.tscn`.

First, we will start a request to load the resource and connect the button:

```gdscript
const ENEMY_SCENE_PATH : String = "Enemy.tscn"

func _ready():
    ResourceLoader.load_threaded_request(ENEMY_SCENE_PATH)
    self.pressed.connect(_on_button_pressed)
```

Now `_on_button_pressed` will be called when the button is pressed. This method will be used to spawn an enemy.

```gdscript
func _on_button_pressed(): # Button was pressed.
    # Obtain the resource now that we need it.
    var enemy_scene = ResourceLoader.load_threaded_get(ENEMY_SCENE_PATH)
    # Instantiate the enemy scene and add it to the current scene.
    var enemy = enemy_scene.instantiate()
    add_child(enemy)
```

---

## Binary serialization API

> **Work in progress:** The content of this page was not yet updated for Godot `4.6` and may be **outdated**. If you know how to improve this page or you can confirm that it's up to date, feel free to [open a pull request](https://github.com/godotengine/godot-docs).

### Introduction

Godot has a serialization API based on Variant. It's used for converting data types to an array of bytes efficiently. This API is exposed via the global `bytes_to_var()` and `var_to_bytes()` functions, but it is also used in the `get_var` and `store_var` methods of [FileAccess](../godot_gdscript_filesystem.md) as well as the packet APIs for [PacketPeer](../godot_gdscript_networking.md). This format is _not_ used for binary scenes and resources.

### Full Objects vs Object instance IDs

If a variable is serialized with `full_objects = true`, then any Objects contained in the variable will be serialized and included in the result. This is recursive.

If `full_objects = false`, then only the instance IDs will be serialized for any Objects contained in the variable.

### Packet specification

The packet is designed to be always padded to 4 bytes. All values are little-endian-encoded. All packets have a 4-byte header representing an integer, specifying the type of data.

The lowest value two bytes are used to determine the type, while the highest value two bytes contain flags:

```gdscript
base_type = val & 0xFFFF;
flags = val >> 16;
```

| Type | Value         |
| ---- | ------------- |
| 0    | null          |
| 1    | bool          |
| 2    | integer       |
| 3    | float         |
| 4    | string        |
| 5    | vector2       |
| 6    | rect2         |
| 7    | vector3       |
| 8    | transform2d   |
| 9    | plane         |
| 10   | quaternion    |
| 11   | aabb          |
| 12   | basis         |
| 13   | transform3d   |
| 14   | color         |
| 15   | node path     |
| 16   | rid           |
| 17   | object        |
| 18   | dictionary    |
| 19   | array         |
| 20   | raw array     |
| 21   | int32 array   |
| 22   | int64 array   |
| 23   | float32 array |
| 24   | float64 array |
| 25   | string array  |
| 26   | vector2 array |
| 27   | vector3 array |
| 28   | color array   |
| 29   | max           |

Following this is the actual packet contents, which varies for each type of packet. Note that this assumes Godot is compiled with single-precision floats, which is the default. If Godot was compiled with double-precision floats, the length of "Float" fields within data structures should be 8, and the offset should be `(offset - 4) * 2 + 4`. The "float" type itself always uses double precision.

#### 0: null

#### 1: bool

| Offset | Len | Type    | Description             |
| ------ | --- | ------- | ----------------------- |
| 4      | 4   | Integer | 0 for False, 1 for True |

#### 2: int

If no flags are set (flags == 0), the integer is sent as a 32 bit integer:

| Offset | Len | Type    | Description           |
| ------ | --- | ------- | --------------------- |
| 4      | 4   | Integer | 32-bit signed integer |

If flag `ENCODE_FLAG_64` is set (`flags & 1 == 1`), the integer is sent as a 64-bit integer:

| Offset | Len | Type    | Description           |
| ------ | --- | ------- | --------------------- |
| 4      | 8   | Integer | 64-bit signed integer |

#### 3: float

If no flags are set (flags == 0), the float is sent as a 32 bit single precision:

| Offset | Len | Type  | Description                     |
| ------ | --- | ----- | ------------------------------- |
| 4      | 4   | Float | IEEE 754 single-precision float |

If flag `ENCODE_FLAG_64` is set (`flags & 1 == 1`), the float is sent as a 64-bit double precision number:

| Offset | Len | Type  | Description                     |
| ------ | --- | ----- | ------------------------------- |
| 4      | 8   | Float | IEEE 754 double-precision float |

#### 4: String

| Offset | Len | Type    | Description              |
| ------ | --- | ------- | ------------------------ |
| 4      | 4   | Integer | String length (in bytes) |
| 8      | X   | Bytes   | UTF-8 encoded string     |

This field is padded to 4 bytes.

#### 5: Vector2

| Offset | Len | Type  | Description  |
| ------ | --- | ----- | ------------ |
| 4      | 4   | Float | X coordinate |
| 8      | 4   | Float | Y coordinate |

#### 6: Rect2

| Offset | Len | Type  | Description  |
| ------ | --- | ----- | ------------ |
| 4      | 4   | Float | X coordinate |
| 8      | 4   | Float | Y coordinate |
| 12     | 4   | Float | X size       |
| 16     | 4   | Float | Y size       |

#### 7: Vector3

| Offset | Len | Type  | Description  |
| ------ | --- | ----- | ------------ |
| 4      | 4   | Float | X coordinate |
| 8      | 4   | Float | Y coordinate |
| 12     | 4   | Float | Z coordinate |

#### 8: Transform2D

| Offset | Len | Type  | Description                                                 |
| ------ | --- | ----- | ----------------------------------------------------------- |
| 4      | 4   | Float | The X component of the X column vector, accessed via [0][0] |
| 8      | 4   | Float | The Y component of the X column vector, accessed via [0][1] |
| 12     | 4   | Float | The X component of the Y column vector, accessed via [1][0] |
| 16     | 4   | Float | The Y component of the Y column vector, accessed via [1][1] |
| 20     | 4   | Float | The X component of the origin vector, accessed via [2][0]   |
| 24     | 4   | Float | The Y component of the origin vector, accessed via [2][1]   |

#### 9: Plane

| Offset | Len | Type  | Description |
| ------ | --- | ----- | ----------- |
| 4      | 4   | Float | Normal X    |
| 8      | 4   | Float | Normal Y    |
| 12     | 4   | Float | Normal Z    |
| 16     | 4   | Float | Distance    |

#### 10: Quaternion

| Offset | Len | Type  | Description |
| ------ | --- | ----- | ----------- |
| 4      | 4   | Float | Imaginary X |
| 8      | 4   | Float | Imaginary Y |
| 12     | 4   | Float | Imaginary Z |
| 16     | 4   | Float | Real W      |

#### 11: AABB

| Offset | Len | Type  | Description  |
| ------ | --- | ----- | ------------ |
| 4      | 4   | Float | X coordinate |
| 8      | 4   | Float | Y coordinate |
| 12     | 4   | Float | Z coordinate |
| 16     | 4   | Float | X size       |
| 20     | 4   | Float | Y size       |
| 24     | 4   | Float | Z size       |

#### 12: Basis

| Offset | Len | Type  | Description                                                 |
| ------ | --- | ----- | ----------------------------------------------------------- |
| 4      | 4   | Float | The X component of the X column vector, accessed via [0][0] |
| 8      | 4   | Float | The Y component of the X column vector, accessed via [0][1] |
| 12     | 4   | Float | The Z component of the X column vector, accessed via [0][2] |
| 16     | 4   | Float | The X component of the Y column vector, accessed via [1][0] |
| 20     | 4   | Float | The Y component of the Y column vector, accessed via [1][1] |
| 24     | 4   | Float | The Z component of the Y column vector, accessed via [1][2] |
| 28     | 4   | Float | The X component of the Z column vector, accessed via [2][0] |
| 32     | 4   | Float | The Y component of the Z column vector, accessed via [2][1] |
| 36     | 4   | Float | The Z component of the Z column vector, accessed via [2][2] |

#### 13: Transform3D

| Offset | Len | Type  | Description                                                 |
| ------ | --- | ----- | ----------------------------------------------------------- |
| 4      | 4   | Float | The X component of the X column vector, accessed via [0][0] |
| 8      | 4   | Float | The Y component of the X column vector, accessed via [0][1] |
| 12     | 4   | Float | The Z component of the X column vector, accessed via [0][2] |
| 16     | 4   | Float | The X component of the Y column vector, accessed via [1][0] |
| 20     | 4   | Float | The Y component of the Y column vector, accessed via [1][1] |
| 24     | 4   | Float | The Z component of the Y column vector, accessed via [1][2] |
| 28     | 4   | Float | The X component of the Z column vector, accessed via [2][0] |
| 32     | 4   | Float | The Y component of the Z column vector, accessed via [2][1] |
| 36     | 4   | Float | The Z component of the Z column vector, accessed via [2][2] |
| 40     | 4   | Float | The X component of the origin vector, accessed via [3][0]   |
| 44     | 4   | Float | The Y component of the origin vector, accessed via [3][1]   |
| 48     | 4   | Float | The Z component of the origin vector, accessed via [3][2]   |

#### 14: Color

| Offset | Len | Type  | Description                                                  |
| ------ | --- | ----- | ------------------------------------------------------------ |
| 4      | 4   | Float | Red (typically 0..1, can be above 1 for overbright colors)   |
| 8      | 4   | Float | Green (typically 0..1, can be above 1 for overbright colors) |
| 12     | 4   | Float | Blue (typically 0..1, can be above 1 for overbright colors)  |
| 16     | 4   | Float | Alpha (0..1)                                                 |

#### 15: NodePath

| Offset | Len | Type    | Description                                                                   |
| ------ | --- | ------- | ----------------------------------------------------------------------------- |
| 4      | 4   | Integer | String length, or new format (val&0x80000000!=0 and NameCount=val&0x7FFFFFFF) |

#### For old format:

| Offset | Len | Type  | Description          |
| ------ | --- | ----- | -------------------- |
| 8      | X   | Bytes | UTF-8 encoded string |

Padded to 4 bytes.

#### For new format:

| Offset | Len | Type    | Description                   |
| ------ | --- | ------- | ----------------------------- |
| 4      | 4   | Integer | Sub-name count                |
| 8      | 4   | Integer | Flags (absolute: val&1 != 0 ) |

For each Name and Sub-Name

| Offset | Len | Type    | Description          |
| ------ | --- | ------- | -------------------- |
| X+0    | 4   | Integer | String length        |
| X+4    | X   | Bytes   | UTF-8 encoded string |

Every name string is padded to 4 bytes.

#### 16: RID (unsupported)

#### 17: Object

An Object could be serialized in three different ways: as a null value, with `full_objects = false`, or with `full_objects = true`.

##### A null value

| Offset | Len | Type    | Description                  |
| ------ | --- | ------- | ---------------------------- |
| 4      | 4   | Integer | Zero (32-bit signed integer) |

##### full_objects disabled

| Offset | Len | Type    | Description                                    |
| ------ | --- | ------- | ---------------------------------------------- |
| 4      | 8   | Integer | The Object instance ID (64-bit signed integer) |

##### full_objects enabled

| Offset | Len | Type    | Description                                  |
| ------ | --- | ------- | -------------------------------------------- |
| 4      | 4   | Integer | Class name (String length)                   |
| 8      | X   | Bytes   | Class name (UTF-8 encoded string)            |
| X+8    | 4   | Integer | The number of properties that are serialized |

For each property:

| Offset | Len | Type       | Description                            |
| ------ | --- | ---------- | -------------------------------------- |
| Y      | 4   | Integer    | Property name (String length)          |
| Y+4    | Z   | Bytes      | Property name (UTF-8 encoded string)   |
| Y+4+Z  | W   | <variable> | Property value, using this same format |

> **Note:** Not all properties are included. Only properties that are configured with the `PROPERTY_USAGE_STORAGE` flag set will be serialized. You can add a new usage flag to a property by overriding the [\_get_property_list](../godot_gdscript_misc.md) method in your class. You can also check how property usage is configured by calling `Object._get_property_list` See `PropertyUsageFlags` for the possible usage flags.

#### 18: Dictionary

| Offset | Len | Type    | Description                                               |
| ------ | --- | ------- | --------------------------------------------------------- |
| 4      | 4   | Integer | val&0x7FFFFFFF = elements, val&0x80000000 = shared (bool) |

Then what follows is, for amount of "elements", pairs of key and value, one after the other, using this same format.

#### 19: Array

| Offset | Len | Type    | Description                                               |
| ------ | --- | ------- | --------------------------------------------------------- |
| 4      | 4   | Integer | val&0x7FFFFFFF = elements, val&0x80000000 = shared (bool) |

Then what follows is, for amount of "elements", values one after the other, using this same format.

#### 20: PackedByteArray

| Offset      | Len | Type    | Description          |
| ----------- | --- | ------- | -------------------- |
| 4           | 4   | Integer | Array length (Bytes) |
| 8..8+length | 1   | Byte    | Byte (0..255)        |

The array data is padded to 4 bytes.

#### 21: PackedInt32Array

| Offset         | Len | Type    | Description             |
| -------------- | --- | ------- | ----------------------- |
| 4              | 4   | Integer | Array length (Integers) |
| 8..8+length\*4 | 4   | Integer | 32-bit signed integer   |

#### 22: PackedInt64Array

| Offset         | Len | Type    | Description             |
| -------------- | --- | ------- | ----------------------- |
| 4              | 8   | Integer | Array length (Integers) |
| 8..8+length\*8 | 8   | Integer | 64-bit signed integer   |

#### 23: PackedFloat32Array

| Offset         | Len | Type    | Description                            |
| -------------- | --- | ------- | -------------------------------------- |
| 4              | 4   | Integer | Array length (Floats)                  |
| 8..8+length\*4 | 4   | Integer | 32-bit IEEE 754 single-precision float |

#### 24: PackedFloat64Array

| Offset         | Len | Type    | Description                            |
| -------------- | --- | ------- | -------------------------------------- |
| 4              | 4   | Integer | Array length (Floats)                  |
| 8..8+length\*8 | 8   | Integer | 64-bit IEEE 754 double-precision float |

#### 25: PackedStringArray

| Offset | Len | Type    | Description            |
| ------ | --- | ------- | ---------------------- |
| 4      | 4   | Integer | Array length (Strings) |

For each String:

| Offset | Len | Type    | Description          |
| ------ | --- | ------- | -------------------- |
| X+0    | 4   | Integer | String length        |
| X+4    | X   | Bytes   | UTF-8 encoded string |

Every string is padded to 4 bytes.

#### 26: PackedVector2Array

| Offset          | Len | Type    | Description  |
| --------------- | --- | ------- | ------------ |
| 4               | 4   | Integer | Array length |
| 8..8+length\*8  | 4   | Float   | X coordinate |
| 8..12+length\*8 | 4   | Float   | Y coordinate |

#### 27: PackedVector3Array

| Offset           | Len | Type    | Description  |
| ---------------- | --- | ------- | ------------ |
| 4                | 4   | Integer | Array length |
| 8..8+length\*12  | 4   | Float   | X coordinate |
| 8..12+length\*12 | 4   | Float   | Y coordinate |
| 8..16+length\*12 | 4   | Float   | Z coordinate |

#### 28: PackedColorArray

| Offset           | Len | Type    | Description                                                  |
| ---------------- | --- | ------- | ------------------------------------------------------------ |
| 4                | 4   | Integer | Array length                                                 |
| 8..8+length\*16  | 4   | Float   | Red (typically 0..1, can be above 1 for overbright colors)   |
| 8..12+length\*16 | 4   | Float   | Green (typically 0..1, can be above 1 for overbright colors) |
| 8..16+length\*16 | 4   | Float   | Blue (typically 0..1, can be above 1 for overbright colors)  |
| 8..20+length\*16 | 4   | Float   | Alpha (0..1)                                                 |

---

## File paths in Godot projects

This page explains how file paths work inside Godot projects. You will learn how to access paths in your projects using the `res://` and `user://` notations, and where Godot stores project and editor files on your and your users' systems.

### Path separators

To make supporting multiple platforms easier, Godot uses **UNIX-style path separators** (forward slash `/`). These work on all platforms, **including Windows**.

Instead of writing paths like `C:\Projects\Game`, in Godot, you should write `C:/Projects/Game`.

Windows-style path separators (backward slash `\`) are also supported in some path-related methods, but they need to be doubled (`\\`), as `\` is normally used as an escape for characters with a special meaning.

This makes it possible to work with paths returned by other Windows applications. We still recommend using only forward slashes in your own code to guarantee that everything will work as intended.

> **Tip:** The String class offers over a dozen methods to work with strings that represent file paths: - [String.filecasecmp_to()](../godot_gdscript_misc.md)

- [String.filenocasecmp_to()](../godot_gdscript_misc.md)
- [String.get_base_dir()](../godot_gdscript_misc.md)
- [String.get_basename()](../godot_gdscript_misc.md)
- [String.get_extension()](../godot_gdscript_misc.md)
- [String.get_file()](../godot_gdscript_misc.md)
- [String.is_absolute_path()](../godot_gdscript_misc.md)
- [String.is_relative_path()](../godot_gdscript_misc.md)
- [String.is_valid_filename()](../godot_gdscript_misc.md)
- [String.path_join()](../godot_gdscript_misc.md)
- [String.simplify_path()](../godot_gdscript_misc.md)
- [String.validate_filename()](../godot_gdscript_misc.md)

### Accessing files in the project folder (res://)

Godot considers that a project exists in any folder that contains a `project.godot` text file, even if the file is empty. The folder that contains this file is your project's root folder.

You can access any file relative to it by writing paths starting with `res://`, which stands for resources. For example, you can access an image file `character.png` located in the project's root folder in code with the following path: `res://character.png`.

### Accessing persistent user data (user://)

To store persistent data files, like the player's save or settings, you want to use `user://` instead of `res://` as your path's prefix. This is because when the game is running, the project's file system will likely be read-only.

The `user://` prefix points to a different directory on the user's device. Unlike `res://`, the directory pointed at by `user://` is created automatically and _guaranteed_ to be writable to, even in an exported project.

The location of the `user://` folder depends on what is configured in the Project Settings:

- By default, the `user://` folder is created within Godot's **editor data path** in the `app_userdata/[project_name]` folder. This is the default so that prototypes and test projects stay self-contained within Godot's data folder.
- If [application/config/use_custom_user_dir](../godot_gdscript_misc.md) is enabled in the Project Settings, the `user://` folder is created **next to** Godot's editor data path, i.e. in the standard location for applications data.

- By default, the folder name will be inferred from the project name, but it can be further customized with [application/config/custom_user_dir_name](../godot_gdscript_misc.md). This path can contain path separators, so you can use it e.g. to group projects of a given studio with a `Studio Name/Game Name` structure.

On desktop platforms, the actual directory paths for `user://` are:

| Type                | Location                                                                                                                                                                            |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Default             | Windows: %APPDATA%\Godot\app_userdata\[project_name] macOS: ~/Library/Application Support/Godot/app_userdata/[project_name] Linux: ~/.local/share/godot/app_userdata/[project_name] |
| Custom dir          | Windows: %APPDATA%\[project_name] macOS: ~/Library/Application Support/[project_name] Linux: ~/.local/share/[project_name]                                                          |
| Custom dir and name | Windows: %APPDATA%\[custom_user_dir_name] macOS: ~/Library/Application Support/[custom_user_dir_name] Linux: ~/.local/share/[custom_user_dir_name]                                  |

`[project_name]` is based on the application name defined in the Project Settings, but you can override it on a per-platform basis using [feature tags](tutorials_export.md).

On mobile platforms, this path is unique to the project and is not accessible by other applications for security reasons.

On HTML5 exports, `user://` will refer to a virtual filesystem stored on the device via IndexedDB. (Interaction with the main filesystem can still be performed through the [JavaScriptBridge](../godot_gdscript_misc.md) singleton.)

### File logging

> **See also:** Documentation on file logging has been moved to [Logging](tutorials_scripting.md).

### Converting paths to absolute paths or "local" paths

You can use [ProjectSettings.globalize_path()](../godot_gdscript_filesystem.md) to convert a "local" path like `res://path/to/file.txt` to an absolute OS path. For example, [ProjectSettings.globalize_path()](../godot_gdscript_filesystem.md) can be used to open "local" paths in the OS file manager using [OS.shell_open()](../godot_gdscript_misc.md) since it only accepts native OS paths.

To convert an absolute OS path to a "local" path starting with `res://` or `user://`, use [ProjectSettings.localize_path()](../godot_gdscript_filesystem.md). This only works for absolute paths that point to files or folders in your project's root or `user://` folders.

### Editor data paths

The editor uses different paths for editor data, editor settings, and cache, depending on the platform. By default, these paths are:

| Type            | Location                                                                                           |
| --------------- | -------------------------------------------------------------------------------------------------- |
| Editor data     | Windows: %APPDATA%\Godot\ macOS: ~/Library/Application Support/Godot/ Linux: ~/.local/share/godot/ |
| Editor settings | Windows: %APPDATA%\Godot\ macOS: ~/Library/Application Support/Godot/ Linux: ~/.config/godot/      |
| Cache           | Windows: %TEMP%\Godot\ macOS: ~/Library/Caches/Godot/ Linux: ~/.cache/godot/                       |

- **Editor data** contains export templates and project-specific data.
- **Editor settings** contains the main editor settings configuration file as well as various other user-specific customizations (editor layouts, feature profiles, script templates, etc.).
- **Cache** contains data generated by the editor, or stored temporarily. It can safely be removed when Godot is closed.

Godot complies with the [XDG Base Directory Specification](https://specifications.freedesktop.org/basedir-spec/basedir-spec-latest.html) on Linux/\*BSD. You can override the `XDG_DATA_HOME`, `XDG_CONFIG_HOME` and `XDG_CACHE_HOME` environment variables to change the editor and project data paths.

> **Note:** If you use [Godot packaged as a Flatpak](https://flathub.org/apps/details/org.godotengine.Godot), the editor data paths will be located in subfolders in `~/.var/app/org.godotengine.Godot/`.

#### Self-contained mode

If you create a file called `._sc_` or `_sc_` in the same directory as the editor binary (or in MacOS/Contents/ for a macOS editor .app bundle), Godot will enable _self-contained mode_. This mode makes Godot write all editor data, settings, and cache to a directory named `editor_data/` in the same directory as the editor binary. You can use it to create a portable installation of the editor.

The [Steam release of Godot](https://store.steampowered.com/app/404790/) uses self-contained mode by default.

> **Note:** Self-contained mode is not supported in exported projects yet. To read and write files relative to the executable path, use [OS.get_executable_path()](../godot_gdscript_misc.md). Note that writing files in the executable path only works if the executable is placed in a writable location (i.e. **not** Program Files or another directory that is read-only for regular users).

---

## Runtime file loading and saving

> **See also:** See Saving games for information on saving and loading game progression.

Sometimes, [exporting packs, patches, and mods](tutorials_export.md) is not ideal when you want players to be able to load user-generated content in your project. It requires users to generate a PCK or ZIP file through the Godot editor, which contains resources imported by Godot.

Example use cases for runtime file loading and saving include:

- Loading texture packs designed for the game.
- Loading user-provided audio tracks and playing them back in an in-game radio station.
- Loading custom levels or 3D models that can be designed with any 3D DCC that can export to glTF or FBX (including glTF scenes saved by Godot at runtime).
- Using user-provided fonts for menus and HUD.
- Saving/loading a file format that can contain multiple files but can still easily be read by other applications (ZIP).
- Loading files created by another game or program, or even game data files from another game not made with Godot.

Runtime file loading can be combined with [HTTP requests](tutorials_networking.md) to load resources from the Internet directly.

> **Warning:** Do **not** use this runtime loading approach to load resources that are part of the project, as it's less efficient and doesn't allow benefiting from Godot's resource handling functionality (such as translation remaps). See [Import process](tutorials_assets_pipeline.md) for details.

> **See also:** You can see how saving and loading works in action using the [Run-time File Saving and Loading (Serialization) demo project](https://github.com/godotengine/godot-demo-projects/blob/master/loading/runtime_save_load).

### Plain text and binary files

Godot's [FileAccess](../godot_gdscript_filesystem.md) class provides methods to access files on the filesystem for reading and writing:

```gdscript
func save_file(content):
    var file = FileAccess.open("/path/to/file.txt", FileAccess.WRITE)
    file.store_string(content)

func load_file():
    var file = FileAccess.open("/path/to/file.txt", FileAccess.READ)
    var content = file.get_as_text()
    return content
```

To handle custom binary formats (such as loading file formats not supported by Godot), [FileAccess](../godot_gdscript_filesystem.md) provides several methods to read/write integers, floats, strings and more. These FileAccess methods have names that start with `get_` and `store_`.

If you need more control over reading binary files or need to read binary streams that are not part of a file, [PackedByteArray](../godot_gdscript_misc.md) provides several helper methods to decode/encode series of bytes to integers, floats, strings and more. These PackedByteArray methods have names that start with `decode_` and `encode_`. See also Binary serialization API.

### Images

Image's [Image.load_from_file](../godot_gdscript_misc.md) static method handles everything, from format detection based on file extension to reading the file from disk.

If you need error handling or more control (such as changing the scale an SVG is loaded at), use one of the following methods depending on the file format:

- [Image.load_jpg_from_buffer](../godot_gdscript_misc.md)
- [Image.load_ktx_from_buffer](../godot_gdscript_misc.md)
- [Image.load_png_from_buffer](../godot_gdscript_misc.md)
- [Image.load_svg_from_buffer](../godot_gdscript_misc.md) or [Image.load_svg_from_string](../godot_gdscript_misc.md)
- [Image.load_tga_from_buffer](../godot_gdscript_misc.md)
- [Image.load_webp_from_buffer](../godot_gdscript_misc.md)

Several image formats can also be saved by Godot at runtime using the following methods:

- [Image.save_png](../godot_gdscript_misc.md) or [Image.save_png_to_buffer](../godot_gdscript_misc.md)
- [Image.save_webp](../godot_gdscript_misc.md) or [Image.save_webp_to_buffer](../godot_gdscript_misc.md)
- [Image.save_jpg](../godot_gdscript_misc.md) or [Image.save_jpg_to_buffer](../godot_gdscript_misc.md)
- [Image.save_exr](../godot_gdscript_misc.md) or [Image.save_exr_to_buffer](../godot_gdscript_misc.md) _(only available in editor builds, cannot be used in exported projects)_

The methods with the `to_buffer` suffix save the image to a PackedByteArray instead of the filesystem. This is useful to send the image over the network or into a ZIP archive without having to write it on the filesystem. This can increase performance by reducing I/O utilization.

> **Note:** If displaying the loaded image on a 3D surface, make sure to call [Image.generate_mipmaps](../godot_gdscript_misc.md) so that the texture doesn't look grainy when viewed at a distance. This is also useful in 2D when following instructions on [reducing aliasing when downsampling](tutorials_rendering.md).

Example of loading an image and displaying it in a [TextureRect](../godot_gdscript_ui_controls.md) node (which requires conversion to [ImageTexture](../godot_gdscript_resources.md)):

```gdscript
# Load an image of any format supported by Godot from the filesystem.
var image = Image.load_from_file(path)
# Optionally, generate mipmaps if displaying the texture on a 3D surface
# so that the texture doesn't look grainy when viewed at a distance.
#image.generate_mipmaps()
$TextureRect.texture = ImageTexture.create_from_image(image)

# Save the loaded Image to a PNG image.
image.save_png("/path/to/file.png")

# Save the converted ImageTexture to a PNG image.
$TextureRect.texture.get_image().save_png("/path/to/file.png")
```

### Audio/video files

Godot supports loading Ogg Vorbis, MP3, and WAV audio at runtime. Note that not _all_ files with a `.ogg` extension are Ogg Vorbis files. Some may be Ogg Theora videos, or contain Opus audio within an Ogg container. These files will **not** load correctly as audio files in Godot.

Example of loading an Ogg Vorbis audio file in an [AudioStreamPlayer](../godot_gdscript_audio.md) node:

```gdscript
$AudioStreamPlayer.stream = AudioStreamOggVorbis.load_from_file(path)
```

Example of loading an Ogg Theora video file in a [VideoStreamPlayer](../godot_gdscript_ui_controls.md) node:

```gdscript
var video_stream_theora = VideoStreamTheora.new()
# File extension is ignored, so it is possible to load Ogg Theora videos
# that have a `.ogg` extension this way.
video_stream_theora.file = "/path/to/file.ogv"
$VideoStreamPlayer.stream = video_stream_theora

# VideoStreamPlayer's Autoplay property won't work if the stream is empty
# before this property is set, so call `play()` after setting `stream`.
$VideoStreamPlayer.play()
```

### 3D scenes

Godot has first-class support for glTF 2.0, both in the editor and exported projects. Using [GLTFDocument](../godot_gdscript_misc.md) and [GLTFState](../godot_gdscript_misc.md) together, Godot can load and save glTF files in exported projects, in both text (`.gltf`) and binary (`.glb`) formats. The binary format should be preferred as it's faster to write and smaller, but the text format is easier to debug.

Since Godot 4.3, FBX scenes can also be loaded (but not saved) at runtime using the [FBXDocument](../godot_gdscript_misc.md) and [FBXState](../godot_gdscript_misc.md) classes. The code to do so is the same as glTF, but you will need to replace all instances of `GLTFDocument` and `GLTFState` with `FBXDocument` and `FBXState` in the code samples below.

Example of loading a glTF scene and appending its root node to the scene:

```gdscript
# Load an existing glTF scene.
# GLTFState is used by GLTFDocument to store the loaded scene's state.
# GLTFDocument is the class that handles actually loading glTF data into a Godot node tree,
# which means it supports glTF features such as lights and cameras.
var gltf_document_load = GLTFDocument.new()
var gltf_state_load = GLTFState.new()
var error = gltf_document_load.append_from_file("/path/to/file.gltf", gltf_state_load)
if error == OK:
    var gltf_scene_root_node = gltf_document_load.generate_scene(gltf_state_load)
    add_child(gltf_scene_root_node)
else:
    show_error("Couldn't load glTF scene (error code: %s)." % error_string(error))

# Save a new glTF scene.
var gltf_document_save := GLTFDocument.new()
var gltf_state_save := GLTFState.new()
gltf_document_save.append_from_scene
# ...
```

> **Note:** When loading a glTF scene, a _base path_ must be set so that external resources like textures can be loaded correctly. When loading from a file, the base path is automatically set to the folder containing the file. When loading from a buffer, this base path must be manually set as there is no way for Godot to infer this path. To set the base path, set [GLTFState.base_path](../godot_gdscript_misc.md) on your GLTFState instance _before_ calling [GLTFDocument.append_from_buffer](../godot_gdscript_misc.md) or [GLTFDocument.append_from_file](../godot_gdscript_misc.md).

### Fonts

[FontFile.load_dynamic_font](../godot_gdscript_resources.md) supports the following font file formats: TTF, OTF, WOFF, WOFF2, PFB, PFM

On the other hand, [FontFile.load_bitmap_font](../godot_gdscript_resources.md) supports the [BMFont](https://www.angelcode.com/products/bmfont/) format (`.fnt` or `.font`).

Additionally, it is possible to load any font that is installed on the system using Godot's support for [System fonts](tutorials_ui.md).

Example of loading a font file automatically according to its file extension, then adding it as a theme override to a [Label](../godot_gdscript_ui_controls.md) node:

```gdscript
var path = "/path/to/font.ttf"
var path_lower = path.to_lower()
var font_file = FontFile.new()
if (
        path_lower.ends_with(".ttf")
        or path_lower.ends_with(".otf")
        or path_lower.ends_with(".woff")
        or path_lower.ends_with(".woff2")
        or path_lower.ends_with(".pfb")
        or path_lower.ends_with(".pfm")
):
    font_file.load_dynamic_font(path)
elif path_lower.ends_with(".fnt") or path_lower.ends_with(".font"):
    font_file.load_bitmap_font(path)
else:
    push_error("Invalid font file format.")

if not font_file.data.is_empty():
    # If font was loaded successfully, add it as a theme override.
    $Label.add_theme_font_override("font", font_file)
```

### ZIP archives

Godot supports reading and writing ZIP archives using the [ZIPReader](../godot_gdscript_filesystem.md) and [ZIPPacker](../godot_gdscript_filesystem.md) classes. This supports any ZIP file, including files generated by Godot's "Export PCK/ZIP" functionality (although these will contain imported Godot resources rather than the original project files).

> **Note:** Use [ProjectSettings.load_resource_pack](../godot_gdscript_filesystem.md) to load PCK or ZIP files exported by Godot as [additional data packs](tutorials_export.md). That approach is preferred for DLCs, as it makes interacting with additional data packs seamless (virtual filesystem).

This ZIP archive support can be combined with runtime image, 3D scene and audio loading to provide a seamless modding experience without requiring users to go through the Godot editor to generate PCK/ZIP files.

Example that lists files in a ZIP archive in an [ItemList](../godot_gdscript_ui_controls.md) node, then writes contents read from it to a new ZIP archive (essentially duplicating the archive):

```gdscript
# Load an existing ZIP archive.
var zip_reader = ZIPReader.new()
zip_reader.open(path)
var files = zip_reader.get_files()
# The list of files isn't sorted by default. Sort it for more consistent processing.
files.sort()
for file in files:
    $ItemList.add_item(file, null)
    # Make folders disabled in the list.
    $ItemList.set_item_disabled(-1, file.ends_with("/"))

# Save a new ZIP archive.
var zip_packer = ZIPPacker.new()
var error = zip_packer.open(path)
if error != OK:
    push_error("Couldn't open path for saving ZIP archive (error code: %s)." % error_string(error))
    return

# Reuse the above ZIPReader instance to read files from an existing ZIP archive.
for file in zip_reader.get_files():
    zip_packer.start_file(file)
    zip_packer.write_file(zip_reader.read_file(file))

# ...
```

---

## Saving games

### Introduction

Save games can be complicated. For example, it may be desirable to store information from multiple objects across multiple levels. Advanced save game systems should allow for additional information about an arbitrary number of objects. This will allow the save function to scale as the game grows more complex.

> **Note:** If you're looking to save user configuration, you can use the [ConfigFile](../godot_gdscript_filesystem.md) class for this purpose.

> **See also:** You can see how saving and loading works in action using the [Saving and Loading (Serialization) demo project](https://github.com/godotengine/godot-demo-projects/blob/master/loading/serialization).

### Identify persistent objects

Firstly, we should identify what objects we want to keep between game sessions and what information we want to keep from those objects. For this tutorial, we will use groups to mark and handle objects to be saved, but other methods are certainly possible.

We will start by adding objects we wish to save to the "Persist" group. We can do this through either the GUI or script. Let's add the relevant nodes using the GUI:

Once this is done, when we need to save the game, we can get all objects to save them and then tell them all to save with this script:

```gdscript
var save_nodes = get_tree().get_nodes_in_group("Persist")
for node in save_nodes:
    # Now, we can call our save function on each node.
```

### Serializing

The next step is to serialize the data. This makes it much easier to read from and store to disk. In this case, we're assuming each member of group Persist is an instanced node and thus has a path. GDScript has the helper class [JSON](../godot_gdscript_filesystem.md) to convert between dictionary and string. Our node needs to contain a save function that returns this data. The save function will look like this:

```gdscript
func save():
    var save_dict = {
        "filename" : get_scene_file_path(),
        "parent" : get_parent().get_path(),
        "pos_x" : position.x, # Vector2 is not supported by JSON
        "pos_y" : position.y,
        "attack" : attack,
        "defense" : defense,
        "current_health" : current_health,
        "max_health" : max_health,
        "damage" : damage,
        "regen" : regen,
        "experience" : experience,
        "tnl" : tnl,
        "level" : level,
        "attack_growth" : attack_growth,
        "defense_growth" : defense_growth,
        "health_growth" : health_growth,
        "is_alive" : is_alive,
        "last_attack" : last_attack
    }
    return save_dict
```

This gives us a dictionary with the style `{ "variable_name":value_of_variable }`, which will be useful when loading.

### Saving and reading data

As covered in the [File system](tutorials_scripting.md) tutorial, we'll need to open a file so we can write to it or read from it. Now that we have a way to call our groups and get their relevant data, let's use the class [JSON](../godot_gdscript_filesystem.md) to convert it into an easily stored string and store them in a file. Doing it this way ensures that each line is its own object, so we have an easy way to pull the data out of the file as well.

```gdscript
# Note: This can be called from anywhere inside the tree. This function is
# path independent.
# Go through everything in the persist category and ask them to return a
# dict of relevant variables.
func save_game():
    var save_file = FileAccess.open("user://savegame.save", FileAccess.WRITE)
    var save_nodes = get_tree().get_nodes_in_group("Persist")
    for node in save_nodes:
        # Check the node is an instanced scene so it can be instanced again during load.
        if node.scene_file_path.is_empty():
            print("persistent node '%s' is not an instanced scene, skipped" % node.name)
            continue

        # Check the node has a save function.
        if !node.has_method("save"):
            print("persistent node '%s' is missing a save() function, skipped" % node.nam
# ...
```

Game saved! Now, to load, we'll read each line. Use the [parse](../godot_gdscript_misc.md) method to read the JSON string back to a dictionary, and then iterate over the dict to read our values. But we'll need to first create the object and we can use the filename and parent values to achieve that. Here is our load function:

```gdscript
# Note: This can be called from anywhere inside the tree. This function
# is path independent.
func load_game():
    if not FileAccess.file_exists("user://savegame.save"):
        return # Error! We don't have a save to load.

    # We need to revert the game state so we're not cloning objects
    # during loading. This will vary wildly depending on the needs of a
    # project, so take care with this step.
    # For our example, we will accomplish this by deleting saveable objects.
    var save_nodes = get_tree().get_nodes_in_group("Persist")
    for i in save_nodes:
        i.queue_free()

    # Load the file line by line and process that dictionary to restore
    # the object it represents.
    var save_file = FileAccess.open("user://savegame.save", FileAccess.READ)
    while save_file.
# ...
```

Now we can save and load an arbitrary number of objects laid out almost anywhere across the scene tree! Each object can store different data depending on what it needs to save.

### Some notes

We have glossed over setting up the game state for loading. It's ultimately up to the project creator where much of this logic goes. This is often complicated and will need to be heavily customized based on the needs of the individual project.

Additionally, our implementation assumes no Persist objects are children of other Persist objects. Otherwise, invalid paths would be created. To accommodate nested Persist objects, consider saving objects in stages. Load parent objects first so they are available for the [add_child()](../godot_gdscript_misc.md) call when child objects are loaded. You will also need a way to link children to parents as the [NodePath](../godot_gdscript_misc.md) will likely be invalid.

### JSON vs binary serialization

For simple game state, JSON may work and it generates human-readable files that are easy to debug.

But JSON has many limitations. If you need to store more complex game state or a lot of it, binary serialization may be a better approach.

#### JSON limitations

Here are some important gotchas to know about when using JSON.

- **Filesize:** JSON stores data in text format, which is much larger than binary formats.
- **Data types:** JSON only offers a limited set of data types. If you have data types that JSON doesn't have, you will need to translate your data to and from types that JSON can handle. For example, some important types that JSON can't parse are: `Vector2`, `Vector3`, `Color`, `Rect2`, and `Quaternion`.
- **Custom logic needed for encoding/decoding:** If you have any custom classes that you want to store with JSON, you will need to write your own logic for encoding and decoding those classes.

#### Binary serialization

Binary serialization is an alternative approach for storing game state, and you can use it with the functions `get_var` and `store_var` of [FileAccess](../godot_gdscript_filesystem.md).

- Binary serialization should produce smaller files than JSON.
- Binary serialization can handle most common data types.
- Binary serialization requires less custom logic for encoding and decoding custom classes.

Note that not all properties are included. Only properties that are configured with the `PROPERTY_USAGE_STORAGE` flag set will be serialized. You can add a new usage flag to a property by overriding the [\_get_property_list](../godot_gdscript_misc.md) method in your class. You can also check how property usage is configured by calling `Object._get_property_list`. See `PropertyUsageFlags` for the possible usage flags.

---
