# Godot 4 GDScript Tutorials — Scripting (Part 11)

> 9 tutorials. GDScript-specific code examples.

## Instancing with signals

Signals provide a way to decouple game objects, allowing you to avoid forcing a fixed arrangement of nodes. One sign that a signal might be called for is when you find yourself using `get_parent()`. Referring directly to a node's parent means that you can't easily move that node to another location in the scene tree. This can be especially problematic when you are instancing objects at runtime and may want to place them in an arbitrary location in the running scene tree.

Below we'll consider an example of such a situation: firing bullets.

### Shooting example

Consider a player character that can rotate and shoot towards the mouse. Every time the mouse button is clicked, we create an instance of the bullet at the player's location. See Creating instances (see Getting Started docs) for details.

We'll use an `Area2D` for the bullet, which moves in a straight line at a given velocity:

```gdscript
extends Area2D

var velocity = Vector2.RIGHT

func _physics_process(delta):
    position += velocity * delta
```

However, if the bullets are added as children of the player, then they will remain "attached" to the player as it rotates:

Instead, we need the bullets to be independent of the player's movement - once fired, they should continue traveling in a straight line and the player can no longer affect them. Instead of being added to the scene tree as a child of the player, it makes more sense to add the bullet as a child of the "main" game scene, which may be the player's parent or even further up the tree.

You could do this by adding the bullet to the main scene directly:

```gdscript
var bullet_instance = Bullet.instantiate()
get_parent().add_child(bullet_instance)
```

However, this will lead to a different problem. Now if you try to test your "Player" scene independently, it will crash on shooting, because there is no parent node to access. This makes it a lot harder to test your player code independently and also means that if you decide to change your main scene's node structure, the player's parent may no longer be the appropriate node to receive the bullets.

The solution to this is to use a signal to "emit" the bullets from the player. The player then has no need to "know" what happens to the bullets after that - whatever node is connected to the signal can "receive" the bullets and take the appropriate action to spawn them.

Here is the code for the player using signals to emit the bullet:

```gdscript
extends Sprite2D

signal shoot(bullet, direction, location)

var Bullet = preload("res://bullet.tscn")

func _input(event):
    if event is InputEventMouseButton:
        if event.button_index == MOUSE_BUTTON_LEFT and event.pressed:
            shoot.emit(Bullet, rotation, position)

func _process(delta):
    look_at(get_global_mouse_position())
```

In the main scene, we then connect the player's signal (it will appear in the "Node" tab of the Inspector)

```gdscript
func _on_player_shoot(Bullet, direction, location):
    var spawned_bullet = Bullet.instantiate()
    add_child(spawned_bullet)
    spawned_bullet.rotation = direction
    spawned_bullet.position = location
    spawned_bullet.velocity = spawned_bullet.velocity.rotated(direction)
```

Now the bullets will maintain their own movement independent of the player's rotation:

---

## Logging

Godot comes with several ways to organize and collect log messages.

### Printing messages

> **See also:** See Printing messages for instructions on printing messages. The printed output is generally identical to the logged output. When running a project from the editor, the editor will display logged text in the Output panel.

### Project settings

There are several project settings to control logging behavior in Godot:

- **Application > Run > Disable stdout:** Disables logging to standard output entirely. This also affects what custom loggers receive. This can be controlled at runtime by setting [Engine.print_to_stdout](../godot_gdscript_core.md).
- **Application > Run > Disable stderr:** Disables logging to standard error entirely. This also affects what custom loggers receive. This can be controlled at runtime by setting [Engine.print_error_messages](../godot_gdscript_core.md).
- **Debug > Settings > stdout > Verbose stdout:** Enables verbose logging to standard output. Prints from `print_verbose()` are only visible if verbose mode is enabled.
- **Debug > Settings > stdout > Print FPS:** Prints the frames per second every second, as well as the V-Sync status on startup (as it can effectively cap the maximum framerate).
- **Debug > Settings > stdout > Print GPU Profile:** Prints a report of GPU utilization every second, using the same data source as the Visual Profiler.

Some of these project settings can also be overridden using [command line arguments](tutorials_editor.md) such as `--quiet`, `--verbose`, and `--print-fps`.

The engine's own file logging is also configurable, as described in the section below.

### Built-in file logging

By default, Godot writes log files in `user://logs/godot.log` on desktop platforms. You can change this location by modifying the `debug/file_logging/log_path` project setting. Logs are rotated to keep older files available for inspection. Each session creates a new log file, with the old file renamed to contain the date at which it was rotated. Up to 5 log files are kept by default, which can be adjusted using the `debug/file_logging/max_log_files` project setting.

File logging can also be disabled completely using the `debug/file_logging/enable_file_logging` project setting.

When the project crashes, crash logs are written to the same file as the log file. The crash log will only contain a usable backtrace if the binary that was run contains debugging symbols, or if it can find a debug symbols file that matches the binary. Official binaries don't provide debugging symbols, so this requires a custom build to work. See Debugging symbols for guidance on compiling binaries with debugging symbols enabled.

> **Note:** Log files for `print()` statements are updated when standard output is _flushed_ by the engine. Standard output is flushed on every print in debug builds only. In projects that are exported in release mode, standard output is only flushed when the project exits or crashes to improve performance, especially if the project is often printing text to standard output. On the other hand, the standard error stream (used by `printerr()`, `push_error()`, and `push_warning()`) is always flushed on every print, even in projects exported in release mode. For some use cases like dedicated servers, it can be preferred to have release builds always flush stdout on print, so that logging services like journald can collect logs while the process is running. This can be done by enabling `application/run/flush_stdout_on_print` in the Project Settings.

### Script backtraces

Since Godot 4.5, when GDScript code encounters an error, it will log a backtrace that points to the origin of the error, while also containing the call stack leading to it. This behavior is always enabled when running in the editor, or when the project is exported in debug mode.

In projects exported in release mode, backtraces are disabled by default for performance reasons. You can enable them by checking **Debug > Settings > GDScript > Always Track Call Stacks** in the Project Settings. If you use a custom logging system that reports exceptions to a remote service, it's recommended to enable this to make reported errors more actionable.

### Crash backtraces

> **Warning:** Crash backtraces are only useful if they were recorded in a build that contains debugging symbols. Official Godot binaries do not contain debugging symbols, so you must compile a custom editor or export template binary to get useful crash backtraces.

When the project crashes, a crash backtrace is printed to the standard error stream. This is what it can look like in a build with debug symbols:

```none
================================================================
handle_crash: Program crashed with signal 4
Engine version: Godot Engine v4.5.beta.custom_build (6c9aa4c7d3b9b91cd50714c40eeb234874df7075)
Dumping the backtrace. Please include this when reporting the bug to the project developer.
[1] /lib64/libc.so.6(+0x1a070) [0x7f6e5e277070] (??:0)
[2] godot() [0x4da3358] (/path/to/godot/core/core_bind.cpp:336 (discriminator 2))
[3] godot() [0xdf5f2f] (/path/to/godot/modules/gdscript/gdscript.h:591)
[4] godot() [0xbffd46] (/path/to/godot/modules/gdscript/gdscript.cpp:2065 (discriminator 1))
[5] godot() [0x30f2ea4] (/path/to/godot/core/variant/variant.h:870)
[6] godot() [0x550d4e1] (/path/to/godot/core/object/object.cpp:933)
[7] godot() [0x30d996a] (/path/to/godot/scene/main/node.cpp:318 (d
# ...
```

On the other hand, without debug symbols, it will look like this instead:

```none
================================================================
handle_crash: Program crashed with signal 4
Engine version: Godot Engine v4.5.beta.custom_build (6c9aa4c7d3b9b91cd50714c40eeb234874df7075)
Dumping the backtrace. Please include this when reporting the bug to the project developer.
[1] /lib64/libc.so.6(+0x1a070) [0x7fdfaf666070] (??:0)
[2] godot() [0x4da3358] (??:0)
[3] godot() [0xdf5f2f] (??:0)
[4] godot() [0xbffd46] (??:0)
[5] godot() [0x30f2ea4] (??:0)
[6] godot() [0x550d4e1] (??:0)
[7] godot() [0x30d996a] (??:0)
[8] godot() [0x3131a7f] (??:0)
[9] godot() [0x424589] (??:0)
[10] /lib64/libc.so.6(+0x3575) [0x7fdfaf64f575] (??:0)
[11] /lib64/libc.so.6(__libc_start_main+0x88) [0x7fdfaf64f628] (??:0)
[12] godot() [0x464df5] (??:0)
-- END OF C++ BACKTRACE --
=====================
# ...
```

This backtrace is also logged to the file for the current session, but it is **not** visible in the editor Output panel. Since the engine's scripting system is not running anymore when the engine is crashing, it is not possible to access it from scripting in the same session. However, you can still read the crash backtrace on the next session by loading log files and searching for the crash backtrace string (`Program crashed with signal`) using [FileAccess](../godot_gdscript_filesystem.md). This allows you to access the backtrace information even after a crash, as long as the user restarts the project and file logging is enabled:

```gdscript
# This script can be made an autoload, so that it runs when the project starts.
extends Node

func _ready() -> void:
  var log_dir: String = String(ProjectSettings.get_setting("debug/file_logging/log_path")).get_base_dir()
  # Get the last log file by alphabetical order.
  # Since the timestamp is featured in the file name, it should always be the most recent
  # log file that was rotated. The non-timestamped log file is for the current session,
  # so we don't want to read that one.
  var last_log_file: String = log_dir.path_join(DirAccess.get_files_at(log_dir)[-1])
  var last_long_contents: String = FileAccess.get_file_as_string(last_log_file)

  var crash_begin_idx: int = last_long_contents.find("Program crashed with signal")
  if crash_begin_idx != -1:
      print("The previous session
# ...
```

You can customize the message that appears at the top of the backtrace using the **Debug > Settings > Crash Handler > Message** project setting. This can be used to point to a URL or email address that users can report issues to.

### Creating custom loggers

Since Godot 4.5, it is possible to create custom loggers. This custom logging can be used for many purposes:

- Show an in-game console with the same messages as printed by the engine, without requiring other scripts to be modified.
- Report printed errors from the player's machine to a remote server. This can make it easier for developers to fix bugs when the game is already released, or during playtesting.
- Integrate a dedicated server export with monitoring platforms.

A custom logger can be registered by creating a class that inherits from [Logger](../godot_gdscript_misc.md), then passing an instance of this class to [OS.add_logger](../godot_gdscript_misc.md), in a script's [\_init()](../godot_gdscript_misc.md) method. A good place to do this is an autoload.

The class must define two methods: [\_log_message()](../godot_gdscript_misc.md) and [\_log_error()](../godot_gdscript_misc.md).

Here is a minimal working example of a custom logger, with the script added as an autoload:

```gdscript
extends Node

class CustomLogger extends Logger:
    # Note that this method is not called for messages that use
    # `push_error()` and `push_warning()`, even though these are printed to stderr.
    func _log_message(message: String, error: bool) -> void:
        # Do something with `message`.
        # `error` is `true` for messages printed to the standard error stream (stderr) with `print_error()`.
        # Note that this method will be called from threads other than the main thread, possibly at the same
        # time, so you will need to have some kind of thread-safety as part of it, like a Mutex.
        pass

    func _log_error(
            function: String,
            file: String,
            line: int,
            code: String,
            rationale: String,
            edito
# ...
```

Note that to avoid infinite recursion, you cannot effectively use `print()` and its related methods in `_log_message()`. You also can't effectively use `push_error()` or `push_warning()` in `_log_error()`. Attempting to do so will print a message to the same stream as the original message. This message is not available in the custom logger, which is what prevents infinite recursion from occurring:

```none
While attempting to print a message, another message was printed:
...

While attempting to print an error, another error was printed:
...
```

> **See also:** You can find an example of an in-game console built with a custom logger in the [Custom Logging demo project](https://github.com/godotengine/godot-demo-projects/tree/master/misc/custom_logging).

---

## Nodes and scene instances

This guide explains how to get nodes, create nodes, add them as a child, and instantiate scenes from code.

> **See also:** Check the Creating instances (see Getting Started docs) tutorial to learn about Godot's approach to scene instancing.

### Getting nodes

You can get a reference to a node by calling the [Node.get_node()](../godot_gdscript_misc.md) method. For this to work, the child node must be present in the scene tree. Getting it in the parent node's `_ready()` function guarantees that.

If, for example, you have a scene tree like this, and you want to get a reference to the Sprite2D and Camera2D nodes to access them in your script.

To do so, you can use the following code.

```gdscript
var sprite2d
var camera2d

func _ready():
    sprite2d = get_node("Sprite2D")
    camera2d = get_node("Camera2D")
```

Note that you get nodes using their name, not their type. Above, "Sprite2D" and "Camera2D" are the nodes' names in the scene.

If you rename the Sprite2D node as Skin in the Scene dock, you have to change the line that gets the node to `get_node("Skin")` in the script.

### Node paths

When getting a reference to a node, you're not limited to getting a direct child. The `get_node()` function supports paths, a bit like when working with a file browser. Add a slash to separate nodes.

Take the following example scene, with the script attached to the UserInterface node.

To get the AnimationPlayer node, you would use the following code.

```gdscript
var animation_player

func _ready():
    animation_player = get_node("ShieldBar/AnimationPlayer")
```

> **Note:** As with file paths, you can use ".." to get a parent node. The best practice is to avoid doing that though not to break encapsulation. You can also start the path with a forward slash to make it absolute, in which case your topmost node would be "/root", the application's predefined root viewport.

#### Syntactic sugar

You can use two shorthands to shorten your code in GDScript. Firstly, putting the `@onready` annotation before a member variable makes it initialize right before the `_ready()` callback.

```gdscript
@onready var sprite2d = get_node("Sprite2D")
```

There is also a short notation for `get_node()`: the dollar sign, "$". You place it before the name or path of the node you want to get.

```gdscript
@onready var sprite2d = $Sprite2D
@onready var animation_player = $ShieldBar/AnimationPlayer
```

### Creating nodes

To create a node from code, call its `new()` method like for any other class-based datatype.

You can store the newly created node's reference in a variable and call `add_child()` to add it as a child of the node to which you attached the script.

```gdscript
var sprite2d

func _ready():
    var sprite2d = Sprite2D.new() # Create a new Sprite2D.
    add_child(sprite2d) # Add it as a child of this node.
```

To delete a node and free it from memory, you can call its `queue_free()` method. Doing so queues the node for deletion at the end of the current frame after it has finished processing. At that point, the engine removes the node from the scene and frees the object in memory.

```gdscript
sprite2d.queue_free()
```

Before calling `sprite2d.queue_free()`, the remote scene tree looks like this.

After the engine freed the node, the remote scene tree doesn't display the sprite anymore.

You can alternatively call `free()` to immediately destroy the node. You should do this with care as any reference to it will instantly become `null`. We recommend using `queue_free()` unless you know what you're doing.

When you free a node, it also frees all its children. Thanks to this, to delete an entire branch of the scene tree, you only have to free the topmost parent node.

### Instancing scenes

Scenes are templates from which you can create as many reproductions as you'd like. This operation is called instancing, and doing it from code happens in two steps:

1. Loading the scene from the local drive.
2. Creating an instance of the loaded [PackedScene](../godot_gdscript_resources.md) resource.

```gdscript
var scene = load("res://my_scene.tscn")
```

Preloading the scene can improve the user's experience as the load operation happens when the compiler reads the script and not at runtime. This feature is only available with GDScript.

```gdscript
var scene = preload("res://my_scene.tscn")
```

At that point, `scene` is a packed scene resource, not a node. To create the actual node, you need to call [PackedScene.instantiate()](../godot_gdscript_resources.md). It returns a tree of nodes that you can use as a child of your current node.

```gdscript
var instance = scene.instantiate()
add_child(instance)
```

The advantage of this two-step process is you can keep a packed scene loaded and create new instances on the fly. For example, to quickly instance several enemies or bullets.

---

## Other languages

The Godot developers officially support the following languages for Godot:

- GDScript (all versions)
- C# (.NET version)
- C++ (via GDExtension)

> **Note:** There are no plans to support additional languages officially. That said, the community offers several bindings for other languages (see below).

The bindings below are developed and maintained by the community:

- [D](https://github.com/godot-dlang/godot-dlang)
- [Go](https://github.com/grow-graphics/gd)
- [Java/Kotlin](https://github.com/utopia-rise/godot-kotlin-jvm)
- [Nim](https://github.com/godot-nim/gdext-nim)
- [Rust](https://github.com/godot-rust/gdext)
- [Swift](https://github.com/migueldeicaza/SwiftGodot)
- [Odin](https://github.com/dresswithpockets/odin-godot)

> **Note:** Not all bindings mentioned here may be production-ready. Make sure to research options thoroughly before starting a project with one of those. Also, double-check whether the binding is compatible with the Godot version you're using.

---

## Overridable functions

Godot's Node class provides virtual functions you can override to update nodes every frame or on specific events, like when they enter the scene tree.

This document presents the ones you'll use most often.

> **See also:** Under the hood, these functions rely on Godot's low-level notifications system. To learn more about it, see [Godot notifications](tutorials_best_practices.md).

Two functions allow you to initialize and get nodes besides the class's constructor: `_enter_tree()` and `_ready()`.

When the node enters the Scene Tree, it becomes active and the engine calls its `_enter_tree()` method. That node's children may not be part of the active scene yet. As you can remove and re-add nodes to the scene tree, this function may be called multiple times throughout a node's lifetime.

Most of the time, you'll use `_ready()` instead. This function is called only once in a node's lifetime, after `_enter_tree()`. `_ready()` ensures that all children have entered the scene tree first, so you can safely call `get_node()` on them.

> **See also:** To learn more about getting node references, read Nodes and scene instances.

Another related callback is `_exit_tree()`, which the engine calls every time a node is about to exit the scene tree. This can be when you call [Node.remove_child()](../godot_gdscript_misc.md) or when you free a node.

```gdscript
# Called every time the node enters the scene tree.
func _enter_tree():
    pass

# Called when both the node and its children have entered the scene tree.
func _ready():
    pass

# Called when the node is about to leave the scene tree, after all its
# children received the _exit_tree() callback.
func _exit_tree():
    pass
```

The two virtual methods `_process()` and `_physics_process()` allow you to update the node, every frame and every physics frame respectively. For more information, read the dedicated documentation: Idle and Physics Processing.

```gdscript
# Called every frame.
func _process(delta):
    pass

# Called every physics frame.
func _physics_process(delta):
    pass
```

Two more essential built-in node callback functions are [Node.\_unhandled_input()](../godot_gdscript_misc.md) and [Node.\_input()](../godot_gdscript_misc.md), which you use to both receive and process individual input events. The `_unhandled_input()` method receives every key press, mouse click, etc. that have not been handled already in an `_input()` callback or in a user interface component. You want to use it for gameplay input in general. The `_input()` callback allows you to intercept and process input events before `_unhandled_input()` gets them.

To learn more about inputs in Godot, see the [Input section](tutorials_inputs.md).

```gdscript
# Called once for every event.
func _unhandled_input(event):
    pass

# Called once for every event before _unhandled_input(), allowing you to
# consume some events.
func _input(event):
    pass
```

There are some more overridable functions like [Node.\_get_configuration_warnings()](../godot_gdscript_misc.md). Specialized node types provide more callbacks like [CanvasItem.\_draw()](../godot_gdscript_nodes_2d.md) to draw programmatically or [Control.\_gui_input()](../godot_gdscript_ui_controls.md) to handle clicks and input on UI elements.

---

## Pausing games and process mode

### Introduction

In most games it is desirable to, at some point, interrupt the game to do something else, such as taking a break or changing options. Implementing a fine-grained control for what can be paused (and what cannot) is a lot of work, so a simple framework for pausing is provided in Godot.

### How pausing works

To pause the game the pause state must be set. This is done by assigning `true` to the [SceneTree.paused](../godot_gdscript_core.md) property:

```gdscript
get_tree().paused = true
```

Doing this will cause two things. First, 2D and 3D physics will be stopped for all nodes. Second, the behavior of certain nodes will stop or start depending on their process mode.

> **Note:** The physics servers can be made active while the game is paused by using their `set_active` methods.

### Process Modes

Each node in Godot has a "Process Mode" that defines when it processes. It can be found and changed under a node's [Node](../godot_gdscript_core.md) properties in the inspector.

You can also alter the property with code:

```gdscript
func _ready():
    process_mode = Node.PROCESS_MODE_PAUSABLE
```

This is what each mode tells a node to do:

- **Inherit**: Process depending on the state of the parent, grandparent, etc. The first parent that has a non-Inherit state.
- **Pausable**: Process the node (and its children in Inherit mode) only when the game is not paused.
- **WhenPaused**: Process the node (and its children in Inherit mode) _only_ when the game is paused.
- **Always**: Process the node (and its children in Inherit mode) no matter what. Paused or not, this node will process.
- **Disabled**: The node (and its children in Inherit mode) will not process at all.

By default, all nodes have this property in the "Inherit" state. If the parent is set to "Inherit", then the grandparent will be checked and so on. If a state can't be found in any of the grandparents, the pause state in SceneTree is used. This means that, by default, when the game is paused every node will be paused. Several things happen when a node stops processing.

The `_process`, `_physics_process`, `_input`, and `_input_event` functions will not be called. However signals still work and cause their connected function to run, even if that function's script is attached to a node that is not currently being processed.

Animation nodes will pause their current animation, audio nodes will pause their current audio stream, and particles will pause. These resume automatically when the game is no longer paused.

It is important to note that even if a node is processing while the game is paused physics will **NOT** work for it by default. As stated earlier this is because the physics servers are turned off. The physics servers can be made active while the game is paused by using their `set_active` methods.

### Pause menu example

Start by creating a button that will be used to pause the game.

Create a menu containing a close button, set the **Process Mode** of the menu's root node to **When Paused**, then hide the menu. Since the process mode is set to **When Paused** on the root node, all its children and grandchildren will inherit that process mode. This way, all the nodes in the menu will start processing when the game is paused.

Attach a script to the menu's root node, connect the pause button created earlier to a new method in the script, and inside that method pause the game and show the pause menu.

```gdscript
func _on_pause_button_pressed():
    get_tree().paused = true
    show()
```

Finally, connect the menu's close button to a new method in the script. Inside that method, unpause the game and hide the pause menu.

```gdscript
func _on_close_button_pressed():
    hide()
    get_tree().paused = false
```

You should now have a working pause menu.

---

## Resources

### Nodes and resources

Up to this tutorial, we focused on the [Node](../godot_gdscript_core.md) class in Godot as that's the one you use to code behavior and most of the engine's features rely on it. There is another datatype that is just as important: [Resource](../godot_gdscript_core.md).

_Nodes_ give you functionality: they draw sprites, 3D models, simulate physics, arrange user interfaces, etc. **Resources** are **data containers**. They don't do anything on their own: instead, nodes use the data contained in resources.

Anything Godot saves or loads from disk is a resource. Be it a scene (a `.tscn` or a `.scn` file), an image, a script... Here are some [Resource](../godot_gdscript_core.md) examples:

- [Texture](../godot_gdscript_resources.md)
- [Script](../godot_gdscript_resources.md)
- [Mesh](../godot_gdscript_rendering.md)
- [Animation](../godot_gdscript_resources.md)
- [AudioStream](../godot_gdscript_audio.md)
- [Font](../godot_gdscript_resources.md)
- [Translation](../godot_gdscript_misc.md)

When the engine loads a resource from disk, **it only loads it once**. If a copy of that resource is already in memory, trying to load the resource again will return the same copy every time. As resources only contain data, there is no need to duplicate them.

Every object, be it a Node or a Resource, can export properties. There are many types of Properties, like String, integer, Vector2, etc., and any of these types can become a resource. This means that both nodes and resources can contain resources as properties:

### External vs built-in

There are two ways to save resources. They can be:

1. **External** to a scene, saved on the disk as individual files.
2. **Built-in**, saved inside the `.tscn` or the `.scn` file they're attached to.

To be more specific, here's a [Texture2D](../godot_gdscript_resources.md) in a [Sprite2D](../godot_gdscript_nodes_2d.md) node:

Clicking the resource preview allows us to view the resource's properties.

The path property tells us where the resource comes from. In this case, it comes from a PNG image called `robi.png`. When the resource comes from a file like this, it is an external resource. If you erase the path or this path is empty, it becomes a built-in resource.

The switch between built-in and external resources happens when you save the scene. In the example above, if you erase the path `"res://robi.png"` and save, Godot will save the image inside the `.tscn` scene file.

> **Note:** Even if you save a built-in resource, when you instance a scene multiple times, the engine will only load one copy of it.

### Loading resources from code

There are two ways to load resources from code. First, you can use the `load()` function anytime:

```gdscript
func _ready():
    # Godot loads the Resource when it reads this very line.
    var imported_resource = load("res://robi.png")
    $sprite.texture = imported_resource
```

You can also `preload` resources. Unlike `load`, this function will read the file from disk and load it at compile-time. As a result, you cannot call `preload` with a variable path: you need to use a constant string.

```gdscript
func _ready():
    # Godot loads the resource at compile-time
    var imported_resource = preload("res://robi.png")
    get_node("sprite").texture = imported_resource
```

### Loading scenes

Scenes are also resources, but there is a catch. Scenes saved to disk are resources of type [PackedScene](../godot_gdscript_resources.md). The scene is packed inside a [Resource](../godot_gdscript_core.md).

To get an instance of the scene, you have to use the [PackedScene.instantiate()](../godot_gdscript_resources.md) method.

```gdscript
func _on_shoot():
        var bullet = preload("res://bullet.tscn").instantiate()
        add_child(bullet)
```

This method creates the nodes in the scene's hierarchy, configures them, and returns the root node of the scene. You can then add it as a child of any other node.

The approach has several advantages. As the [PackedScene.instantiate()](../godot_gdscript_resources.md) function is fast, you can create new enemies, bullets, effects, etc. without having to load them again from disk each time. Remember that, as always, images, meshes, etc. are all shared between the scene instances.

### Freeing resources

When a [Resource](../godot_gdscript_core.md) is no longer in use, it will automatically free itself. Since, in most cases, Resources are contained in Nodes, when you free a node, the engine frees all the resources it owns as well if no other node uses them.

### Creating your own resources

Like any Object in Godot, users can also script Resources. Resource scripts inherit the ability to freely translate between object properties and serialized text or binary data (_.tres, _.res). They also inherit the reference-counting memory management from the RefCounted type.

This comes with many distinct advantages over alternative data structures, such as JSON, CSV, or custom TXT files. Users can only import these assets as a [Dictionary](../godot_gdscript_misc.md) (JSON) or as a [FileAccess](../godot_gdscript_filesystem.md) to parse. What sets Resources apart is their inheritance of [Object](../godot_gdscript_core.md), [RefCounted](../godot_gdscript_core.md), and [Resource](../godot_gdscript_core.md) features:

- They can define constants, so constants from other data fields or objects are not needed.
- They can define methods, including setter/getter methods for properties. This allows for abstraction and encapsulation of the underlying data. If the Resource script's structure needs to change, the game using the Resource need not also change.
- They can define signals, so Resources can trigger responses to changes in the data they manage.
- They have defined properties, so users know 100% that their data will exist.
- Resource auto-serialization and deserialization is a built-in Godot Engine feature. Users do not need to implement custom logic to import/export a resource file's data.
- Resources can even serialize sub-Resources recursively, meaning users can design even more sophisticated data structures.
- Users can save Resources as version-control-friendly text files (_.tres). Upon exporting a game, Godot serializes resource files as binary files (_.res) for increased speed and compression.
- Godot Engine's Inspector renders and edits Resource files out-of-the-box. As such, users often do not need to implement custom logic to visualize or edit their data. To do so, double-click the resource file in the FileSystem dock or click the folder icon in the Inspector and open the file in the dialog.
- They can extend **other** resource types besides just the base Resource.

Godot makes it easy to create custom Resources in the Inspector.

1. Create a new Resource object in the Inspector. This can even be a type that derives Resource, so long as your script is extending that type.
2. Set the `script` property in the Inspector to be your script.

The Inspector will now display your Resource script's custom properties. If one edits those values and saves the resource, the Inspector serializes the custom properties too! To save a resource from the Inspector, click the save icon at the top of the Inspector, and select "Save" or "Save As...".

If the script's language supports script classes, then it streamlines the process. Defining a name for your script alone will add it to the Inspector's creation dialog. This will auto-add your script to the Resource object you create.

Let's see some examples. Create a [Resource](../godot_gdscript_core.md) and name it `bot_stats`. It should appear in your file tab with the full name `bot_stats.tres`. Without a script, it's useless, so let's add some data and logic! Attach a script to it named `bot_stats.gd` (or just create a new script, and then drag it to it).

> **Note:** To make the new resource class appear in the Create Resource GUI you need to provide a class name for GDScript, or use the [GlobalClass] attribute in C#.

```gdscript
class_name BotStats
extends Resource

@export var health: int
@export var sub_resource: Resource
@export var strings: PackedStringArray

# Make sure that every parameter has a default value.
# Otherwise, there will be problems with creating and editing
# your resource via the inspector.
func _init(p_health = 0, p_sub_resource = null, p_strings = []):
    health = p_health
    sub_resource = p_sub_resource
    strings = p_strings
```

Now, create a [CharacterBody3D](../godot_gdscript_nodes_3d.md), name it `Bot`, and add the following script to it:

```gdscript
extends CharacterBody3D

@export var stats: Resource

func _ready():
    # Uses an implicit, duck-typed interface for any 'health'-compatible resources.
    if stats:
        stats.health = 10
        print(stats.health)
        # Prints "10"
```

Now, select the [CharacterBody3D](../godot_gdscript_nodes_3d.md) node which we named `bot`, and drag&drop the `bot_stats.tres` resource onto the Inspector. It should print 10! Obviously, this setup can be used for more advanced features than this, but as long you really understand _how_ it all worked, you should figure out everything else related to Resources.

> **Note:** Resource scripts are similar to Unity's ScriptableObjects. The Inspector provides built-in support for custom resources. If desired though, users can even design their own Control-based tool scripts and combine them with an [EditorPlugin](../godot_gdscript_editor.md) to create custom visualizations and editors for their data. Unreal Engine's DataTables and CurveTables are also easy to recreate with Resource scripts. DataTables are a String mapped to a custom struct, similar to a Dictionary mapping a String to a secondary custom Resource script. ```gdscript

# bot_stats_table.gd

extends Resource

const BotStats = preload("bot_stats.gd")

var data = {
"GodotBot": BotStats.new(10), # Creates instance with 10 health.
"DifferentBot": BotStats.new(20) # A different one with 20 health.
}

func \_init():
print(data)

````Instead of inlining the Dictionary values, one could also, alternatively: 1. Import a table of values from a spreadsheet and generate these key-value pairs.
2. Design a visualization within the editor and create a plugin that adds it to the Inspector when you open these types of Resources. CurveTables are the same thing, except mapped to an Array of float values or a [Curve](../godot_gdscript_resources.md)/[Curve2D](../godot_gdscript_resources.md) resource object.



> **Warning:** Beware that resource files (*.tres/*.res) will store the path of the script they use in the file. When loaded, they will fetch and load this script as an extension of their type. This means that trying to assign an inner class of a script (i.e. using the `class` keyword in GDScript) won't work. Godot will not serialize the custom properties on the script inner class properly. In the example below, Godot would load the `Node` script, see that it doesn't extend `Resource`, and then determine that the script failed to load for the Resource object since the types are incompatible. ```gdscript
extends Node

class MyResource:
    extends Resource
    @export var value = 5

func _ready():
    var my_res = MyResource.new()

    # This will NOT serialize the 'value' property.
    ResourceSaver.save(my_res, "res://my_res.tres")
````

---

## Using SceneTree

### Introduction

In previous tutorials, everything revolved around the concept of nodes. Scenes are collections of nodes. They become active once they enter the _scene tree_.

### MainLoop

The way Godot works internally is as follows. There is the [OS](../godot_gdscript_core.md) class, which is the only instance that runs at the beginning. Afterwards, all drivers, servers, scripting languages, scene system, etc are loaded.

When initialization is complete, [OS](../godot_gdscript_core.md) needs to be supplied a [MainLoop](../godot_gdscript_core.md) to run. Up to this point, all this is internals working (you can check main/main.cpp file in the source code if you are ever interested to see how this works internally).

The user program, or game, starts in the MainLoop. This class has a few methods, for initialization, idle (frame-synchronized callback), fixed (physics-synchronized callback), and input. Again, this is low level and when making games in Godot, writing your own MainLoop seldom makes sense.

### SceneTree

One of the ways to explain how Godot works is that it's a high-level game engine over a low-level middleware.

The scene system is the game engine, while the [OS](../godot_gdscript_core.md) and servers are the low-level API.

The scene system provides its own main loop to OS, [SceneTree](../godot_gdscript_core.md). This is automatically instanced and set when running a scene, no need to do any extra work.

It's important to know that this class exists because it has a few important uses:

- It contains the root [Viewport](../godot_gdscript_rendering.md), to which a scene is added as a child when it's first opened to become part of the _Scene Tree_ (more on that next).
- It contains information about the groups and has the means to call all nodes in a group or get a list of them.
- It contains some global state functionality, such as setting pause mode or quitting the process.

When a node is part of the Scene Tree, the [SceneTree](../godot_gdscript_core.md) singleton can be obtained by calling [Node.get_tree()](../godot_gdscript_misc.md).

### Root viewport

The root [Viewport](../godot_gdscript_rendering.md) is always at the top of the scene. From a node, it can be obtained in two different ways:

```gdscript
get_tree().root # Access via scene main loop.
get_node("/root") # Access via absolute path.
```

This node contains the main viewport. Anything that is a child of a [Viewport](../godot_gdscript_rendering.md) is drawn inside of it by default, so it makes sense that the top of all nodes is always a node of this type otherwise nothing would be seen.

While other viewports can be created in the scene (for split-screen effects and such), this one is the only one that is never created by the user. It's created automatically inside SceneTree.

### Scene tree

When a node is connected, directly or indirectly, to the root viewport, it becomes part of the _scene tree_.

This means that as explained in previous tutorials, it will get the `_enter_tree()` and `_ready()` callbacks (as well as `_exit_tree()`).

When nodes enter the _Scene Tree_, they become active. They get access to everything they need to process, get input, display 2D and 3D visuals, receive and send notifications, play sounds, etc. When they are removed from the _scene tree_, they lose these abilities.

### Tree order

Most node operations in Godot, such as drawing 2D, processing, or getting notifications are done in _tree order_, or top to bottom as seen in the editor (also known as pre-order traversal):

For example, the top node in a scene has its `_process()` function called first, then the node below it has its `_process()` function called, then the node below that and so on.

An important exception is the `_ready()` function: each parent node has its `_ready()` function called only after all its child nodes have their `_ready()` functions called, so that the parent knows its children are completely ready to be accessed. This is also known as post-order traversal. In the above image, `NameLabel` would be notified first (but only after its children, if it had any!), followed by `Name`, etc., and `Panel` would be notified last.

The order of operations can also be overridden using the `process_priority` node property. Nodes with a lower number are called first. For example, nodes with the priorities "0, 1, 2, 3" would be called in that order from left to right.

### "Becoming active" by entering the Scene Tree

1. A scene is loaded from disk or created by scripting.
2. The root node of that scene (only one root, remember?) is added as either a child of the "root" Viewport (from SceneTree), or to any of its descendants.
3. Every node of the newly added scene will receive the "enter_tree" notification ( `_enter_tree()` callback in GDScript) in top-to-bottom order (pre-order traversal).
4. Every node will receive the "ready" notification ( `_ready()` callback in GDScript) for convenience, once all its children have received the "ready" notification (post-order traversal).
5. When a scene (or part of it) is removed, they receive the "exit scene" notification ( `_exit_tree()` callback in GDScript) in bottom-to-top order (the exact reverse of top-to-bottom order).

### Changing current scene

After a scene is loaded, you may want to change this scene for another one. One way to do this is to use the [SceneTree.change_scene_to_file()](../godot_gdscript_core.md) function:

```gdscript
func _my_level_was_completed():
    get_tree().change_scene_to_file("res://levels/level2.tscn")
```

Rather than using file paths, one can also use ready-made [PackedScene](../godot_gdscript_resources.md) resources using the equivalent function [SceneTree.change_scene_to_packed(PackedScene scene)](../godot_gdscript_core.md):

```gdscript
var next_scene = preload("res://levels/level2.tscn")

func _my_level_was_completed():
    get_tree().change_scene_to_packed(next_scene)
```

These are quick and useful ways to switch scenes but have the drawback that the game will stall until the new scene is loaded and running. At some point in the development of your game, it may be preferable to create proper loading screens with progress bar, animated indicators or threaded (background) loading. This must be done manually using Singletons (Autoload) and [Background loading](tutorials_io.md).

---

## Scene Unique Nodes

### Introduction

Using `get_node()` to reference nodes from a script can sometimes be fragile. If you move a button in a UI scene from one panel to another, the button's node path changes, and if a script uses `get_node()` with a hard-coded node path, the script will not be able to find the button anymore.

In situations like this, the node can be turned into a scene unique node to avoid having to update the script every time the node's path is changed.

### Creation and usage

There are two ways to create a scene unique node.

In the Scene tree dock, right-click on a node and select **Access as Unique Name** in the context menu.

After selecting the option, the node will now have a percent symbol (**%**) next to its name in the scene tree:

You can also do this while renaming the node by adding "%" to the beginning of the name. Once you confirm, the percent symbol will appear next to its name.

You can now use the node in your script. For example, you can reference it with a `get_node()` method call by typing the % symbol, followed by the node's name:

```gdscript
get_node("%RedButton").text = "Hello"
%RedButton.text = "Hello" # Shorter syntax
```

### Same-scene limitation

A scene unique node can only be retrieved by a node inside the same scene. To demonstrate this limitation, consider this example **Player** scene that instances a **Sword** scene:

Here are the results of `get_node()` calls inside the **Player** script:

- `get_node("%Eyes")` returns the **Eyes** node.
- `get_node("%Hilt")` returns `null`.

These are the results of `get_node()` calls inside the **Sword** script:

- `get_node("%Eyes")` returns `null`.
- `get_node("%Hilt")` returns the **Hilt** node.

If a script has access to a node in another scene, it can call `get_node()` on that node to get scene unique nodes from that node's scene. This also works in a node path, which avoids multiple `get_node()` calls. Here are two ways to get the **Hilt** node from the **Player** script using scene unique nodes:

- `get_node("Hand/Sword").get_node("%Hilt")` returns the **Hilt** node.
- `get_node("Hand/Sword/%Hilt")` also returns the **Hilt** node.

Scene unique names don't only work at the end of a node path. They can be used in the middle to navigate from one node to another. For example, the **Sword** node is marked as a scene unique node in the **Player** scene, so this is possible:

- `get_node("%Sword/%Hilt")` returns the **Hilt** node.

### Alternatives

Scene unique nodes are a useful tool to navigate a scene. However, there are some situations where other techniques may be better.

A Group allows locating a node (or a group of many nodes) from any other node, no matter what scene the two nodes are located in.

A Singleton (Autoload) is an always loaded node that can be accessed directly by any node regardless of the scene. These are useful when some data or functionality is shared globally.

[Node.find_child()](../godot_gdscript_misc.md) finds a node by name without knowing its full path. This seems similar to a scene unique node, but this method is able to find nodes in nested scenes, and doesn't require marking the node in the scene editor in any way. However, this method is slow. Scene unique nodes are cached by Godot and are fast to retrieve, but each time the method is called, `find_child()` needs to check every descendant (every child, grandchild, and so on).

---
