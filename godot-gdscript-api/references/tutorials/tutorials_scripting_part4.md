# Godot 4 GDScript Tutorials — Scripting (Part 4)

> 8 tutorials. GDScript-specific code examples.

## Adding documentation

> **Note:** Adding documentation for GDExtensions is only possible with Godot 4.3 and later.

The GDExtension documentation system works in a similar manner to the built-in engine documentation: It uses XML files (one per class) to document the exposed constructors, properties, methods, constants, signals, and more.

To get started, identify your project's test project folder, which should contain a Godot project with your extension installed and working. If you are using [godot-cpp-template](https://github.com/godotengine/godot-cpp-template), your GDExtension project already has a `project` folder. Alternatively, you can add one by following the steps described in Getting started. Inside the `project` folder, run the following terminal command:

```shell
# Replace "godot" with the full path to a Godot editor binary
# if Godot is not installed in your `PATH`.
godot --doctool ../ --gdextension-docs
```

This command instructs Godot to generate documentation via the `--doctool` and `--gdextension-docs` commands. The `../` argument specifies the base path of your GDExtension.

After running this command, you should find XML files for your registered GDExtension classes inside the `doc_classes` folder in your GDExtension project. You could edit them now, but for this tutorial, the empty files will suffice.

Now that you have XML files containing your documentation, the next step is to include them in your GDExtension binary. Assuming you are using SCons as your build system, you can add the following lines to your `SConstruct` file. If you are using [godot-cpp-template](https://github.com/godotengine/godot-cpp-template), your file already contains code for this.

```py
if env["target"] in ["editor", "template_debug"]:
    doc_data = env.GodotCPPDocData("src/gen/doc_data.gen.cpp", source=Glob("doc_classes/*.xml"))
    sources.append(doc_data)
```

The `if` statement avoids adding the documentation to release builds of your GDExtension, where it is not needed. SCons then loads all the XML files inside the `doc_classes` directory, and appends the resulting targets to the `sources` array, to be included in your GDExtension build.

After building, launch your Godot project again. You can open the documentation of one of your extension classes either using Ctrl + Click on a class name in the script editor, or inside by finding it in the Editor help dialog. If everything went well, you should see something like this:

### Writing and styling documentation

The format of the class reference XML files is the same as the one used by Godot. Is is documented in Class reference primer.

If you are looking for pointers to write high quality documentation, feel free to refer to Godot's [documentation guidelines](https://contributing.godotengine.org/en/latest/documentation/guidelines/index.html).

### Publishing documentation online

You may want to publish an online reference for your GDExtension, similar to this website. The most important step is to build reStructuredText (`.rst`) files from your XML class reference:

```shell
# You need a version.py file, so download it first.
curl -sSLO https://raw.githubusercontent.com/godotengine/godot/refs/heads/master/version.py

# Edit version.py according to your project before proceeding.
# Then, run the rst generator. You'll need to have Python installed for this command to work.
curl -sSL https://raw.githubusercontent.com/godotengine/godot/master/doc/tools/make_rst.py | python3 - -o "docs/classes" -l "en" doc_classes
```

Your `.rst` files will now be available in `docs/classes/`. From here, you can use any documentation builder that supports reStructuredText syntax to create a website from them.

[godot-docs](https://github.com/godotengine/godot-docs) uses [Sphinx](https://www.sphinx-doc.org/en/master/). You can use the repository as a basis to build your own documentation system. The following guide describes the basic steps, but they are not exhaustive: you will need a bit of personal insight to make it work.

1. Add [godot-docs](https://github.com/godotengine/godot-docs) as a submodule to your `docs/` folder.
2. Copy over its `conf.py`, `index.rst`, `.readthedocs.yaml` files into `/docs/`. You may later decide to copy over and edit more of godot-docs' files, like `_templates/layout.html`.
3. Modify these files according to your project. This mostly involves adjusting paths to point to the `godot-docs` subfolder, as well as strings to reflect it's your project rather than Godot you're building the docs for.
4. Create an account on [readthedocs.org](http://readthedocs.org). Import your project, and modify its base `.readthedocs.yaml` file path to `/docs/.readthedocs.yaml`.

Once you have completed all these steps, your documentation should be available at `<repo-name>.readthedocs.io`.

---

## Creating script templates

Godot provides a way to use script templates as seen in the `Script Create Dialog` while creating a new script:

A set of built-in script templates are provided with the editor, but it is also possible to create new ones and set them by default, both per project and at editor scope.

Templates are linked to a specific node type, so when you create a script you will only see the templates corresponding to that particular node, or one of its parent types. For example, if you are creating a script for a CharacterBody3D, you will only see templates defined for CharacterBody3Ds, Node3Ds or Nodes.

### Locating the templates

There are two places where templates can be managed.

#### Editor-defined templates

These are available globally throughout any project. The location of these templates are determined per each OS:

- Windows: `%APPDATA%\Godot\script_templates\`
- Linux: `$HOME/.config/godot/script_templates/`
- macOS: `$HOME/Library/Application Support/Godot/script_templates/`

If you're getting Godot from somewhere other than the official website, such as Steam, the folder might be in a different location. You can find it using the Godot editor. Go to `Editor > Open Editor Data/Settings Folder` and it will open a folder in your file browser, inside that folder is the `script_templates` folder.

#### Project-defined templates

The default path to search for templates is the `res://script_templates/` directory. The path can be changed by configuring the project setting [Editor > Script > Templates Search Path](../godot_gdscript_editor.md), both via code and the editor.

If no `script_templates` directory is found within a project, it is simply ignored.

#### Template organization and naming

Both editor and project defined templates are organized in the following way:

```gdscript
template_path/node_type/file.extension
```

where:

- `template_path` is one of the 2 locations discussed in the previous two sections.
- `node_type` is the node it will apply to (for example, [Node](../godot_gdscript_core.md), or [CharacterBody3D](../godot_gdscript_nodes_3d.md)), This is **case-sensitive**. If a script isn't in the proper `node_type` folder, it won't be detected.
- `file` is the custom name you can chose for the template (for example, `platformer_movement` or `smooth_camera`).
- `extension` indicates which language the template will apply to (it should be `gd` for GDScript or `cs` for C#).

For example:

- `script_templates/Node/smooth_camera.gd`
- `script_templates/CharacterBody3D/platformer_movement.gd`

### Default behavior and overriding it

By default:

- the template's name is the same as the file name (minus the extension, prettyfied)
- the description is empty
- the space indent is set to 4
- the template will not be set as the default for the given node

It is possible to customize this behavior by adding meta headers at the start of your file, like this:

```gdscript
# meta-name: Platformer movement
# meta-description: Predefined movement for classical platformers
# meta-default: true
# meta-space-indent: 4
```

In this case, the name will be set to "Platformer movement", with the given custom description, and it will be set as the default template for the node in which directory it has been saved.

This is an example of utilizing custom templates at editor and project level:

> **Note:** The script templates have the same extension as the regular script files. This may lead to an issue of a script parser treating those templates as actual scripts within a project. To avoid this, make sure to ignore the directory containing them by creating an empty `.gdignore` file. The directory won't be visible throughout the project's filesystem anymore, yet the templates can be modified by an external text editor anytime.

> **Tip:** By default, every C# file inside the project directory is included in the compilation. Script templates must be manually excluded from the C# project to avoid build errors. See [Exclude files from the build](https://learn.microsoft.com/en-us/visualstudio/msbuild/how-to-exclude-files-from-the-build) in the Microsoft documentation.

It is possible to create editor-level templates that have the same level as a project-specific templates, and also that have the same name as a built-in one, all will be shown on the new script dialog.

### Default template

To override the default template, create a custom template at editor or project level inside a `Node` directory (or a more specific type, if only a subtype wants to be overridden) and start the file with the `meta-default: true` header.

Only one template can be set as default at the same time for the same node type.

The `Default` templates for basic Nodes, for both GDScript and C#, are shown here so you can use these as the base for creating other templates:

```gdscript
# meta-description: Base template for Node with default Godot cycle methods

extends _BASE_

# Called when the node enters the scene tree for the first time.
func _ready() -> void:
    pass # Replace with function body.

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
    pass
```

The Godot editor provides a set of useful built-in node-specific templates, such as `basic_movement` for both [CharacterBody2D](../godot_gdscript_nodes_2d.md) and [CharacterBody3D](../godot_gdscript_nodes_3d.md) and `plugin` for [EditorPlugin](../godot_gdscript_editor.md).

### List of template placeholders

The following describes the complete list of built-in template placeholders which are currently implemented.

#### Base placeholders

| Placeholder          | Description                                                                                                                                                                                                                                                                               |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| _BINDINGS_NAMESPACE_ | The name of the Godot namespace (used in C# only).                                                                                                                                                                                                                                        |
| _CLASS_              | The name of the new class.                                                                                                                                                                                                                                                                |
| _CLASS_SNAKE_CASE_   | The name of the new class as snake_case (used in GDScript only).                                                                                                                                                                                                                          |
| _BASE_               | The base type a new script inherits from.                                                                                                                                                                                                                                                 |
| _TS_                 | Indentation placeholder. The exact type and number of whitespace characters used for indentation is determined by the text_editor/indent/type and text_editor/indent/size settings in the EditorSettings respectively. Can be overridden by the meta-space-indent header on the template. |

#### Type placeholders

There used to be, in Godot 3.x, placeholders for GDScript type hints that would get replaced whenever a template was used to create a new script, such as: `%INT_TYPE%`, `%STRING_TYPE%`, `%FLOAT_TYPE%` or `%VOID_RETURN%`.

The placeholders no longer work for Godot 4.x, but if the setting `text_editor/completion/add_type_hints` from [EditorSettings](../godot_gdscript_filesystem.md) is disabled, type hints for parameters and return types will be automatically removed for a few base types:

- `int`
- `String`
- `Array[String]`
- `float`
- `void`
- `:=` will be transformed into `=`

---

## Cross-language scripting

Godot allows you to mix and match scripting languages to suit your needs. This means a single project can define nodes in both C# and GDScript. This page will go through the possible interactions between two nodes written in different languages.

The following two scripts will be used as references throughout this page.

```gdscript
extends Node

var my_property: String = "my gdscript value":
    get:
        return my_property
    set(value):
        my_property = value

signal my_signal
signal my_signal_with_params(msg: String, n: int)

func print_node_name(node: Node) -> void:
    print(node.get_name())

func print_array(arr: Array) -> void:
    for element in arr:
        print(element)

func print_n_times(msg: String, n: int) -> void:
    for i in range(n):
        print(msg)

func my_signal_handler():
    print("The signal handler was called!")

func my_signal_with_params_handler(msg: String, n: int):
    print_n_times(msg, n)
```

### Instantiating nodes

If you're not using nodes from the scene tree, you'll probably want to instantiate nodes directly from the code.

#### Instantiating C# nodes from GDScript

Using C# from GDScript doesn't need much work. Once loaded (see Classes as resources), the script can be instantiated with [new()](../godot_gdscript_misc.md).

```gdscript
var MyCSharpScript = load("res://Path/To/MyCSharpNode.cs")
var my_csharp_node = MyCSharpScript.new()
```

> **Warning:** When creating `.cs` scripts, you should always keep in mind that the class Godot will use is the one named like the `.cs` file itself. If that class does not exist in the file, you'll see the following error: `Invalid call. Nonexistent function `new` in base`. For example, MyCoolNode.cs should contain a class named MyCoolNode. The C# class needs to derive a Godot class, for example `GodotObject`. Otherwise, the same error will occur. You also need to check your `.cs` file is referenced in the project's `.csproj` file. Otherwise, the same error will occur.

#### Instantiating GDScript nodes from C#

From the C# side, everything work the same way. Once loaded, the GDScript can be instantiated with [GDScript.New()](../godot_gdscript_resources.md).

Here we are using an [Object](../godot_gdscript_core.md), but you can use type conversion like explained in Type conversion and casting.

### Accessing fields

#### Accessing C# fields from GDScript

Accessing C# fields from GDScript is straightforward, you shouldn't have anything to worry about.

```gdscript
# Output: "my c# value".
print(my_csharp_node.MyProperty)
my_csharp_node.MyProperty = "MY C# VALUE"
# Output: "MY C# VALUE".
print(my_csharp_node.MyProperty)
```

#### Accessing GDScript fields from C#

As C# is statically typed, accessing GDScript from C# is a bit more convoluted. You will have to use [GodotObject.Get()](../godot_gdscript_misc.md) and [GodotObject.Set()](../godot_gdscript_misc.md). The first argument is the name of the field you want to access.

Keep in mind that when setting a field value you should only use types the GDScript side knows about. Essentially, you want to work with built-in types as described in Built-in types or classes extending [Object](../godot_gdscript_core.md).

### Calling methods

#### Calling C# methods from GDScript

Again, calling C# methods from GDScript should be straightforward. The marshalling process will do its best to cast the arguments to match function signatures. If that's impossible, you'll see the following error: `Invalid call. Nonexistent function `FunctionName``.

```gdscript
# Output: "my_gd_script_node" (or name of node where this code is placed).
my_csharp_node.PrintNodeName(self)
# This line will fail.
# my_csharp_node.PrintNodeName()

# Outputs "Hello there!" twice, once per line.
my_csharp_node.PrintNTimes("Hello there!", 2)

# Output: "a", "b", "c" (one per line).
my_csharp_node.PrintArray(["a", "b", "c"])
# Output: "1", "2", "3"  (one per line).
my_csharp_node.PrintArray([1, 2, 3])
```

#### Calling GDScript methods from C#

To call GDScript methods from C# you'll need to use [GodotObject.Call()](../godot_gdscript_misc.md). The first argument is the name of the method you want to call. The following arguments will be passed to said method.

### Connecting to signals

#### Connecting to C# signals from GDScript

Connecting to a C# signal from GDScript is the same as connecting to a signal defined in GDScript:

```gdscript
my_csharp_node.MySignal.connect(my_signal_handler)

my_csharp_node.MySignalWithParams.connect(my_signal_with_params_handler)
```

#### Connecting to GDScript signals from C#

Connecting to a GDScript signal from C# only works with the `Connect` method because no C# static types exist for signals defined by GDScript:

### Inheritance

A GDScript file may not inherit from a C# script. Likewise, a C# script may not inherit from a GDScript file. Due to how complex this would be to implement, this limitation is unlikely to be lifted in the future. See [this GitHub issue](https://github.com/godotengine/godot/issues/38352) for more information.

---

## Custom performance monitors

### Introduction

As explained in the Debugger panel documentation, Godot features a **Debugger > Monitors** bottom panel that allows tracking various values with graphs showing their evolution over time. The data for those graphs is sourced from the engine's [Performance](../godot_gdscript_core.md) singleton.

Godot lets you declare custom values to be displayed in the Monitors tab. Example use cases for custom performance monitors include:

- Displaying performance metrics that are specific to your project. For instance, in a voxel game, you could create a performance monitor to track the number of chunks that are loaded every second.
- Displaying in-game metrics that are not strictly related to performance, but are still useful to graph for debugging purposes. For instance, you could track the number of enemies present in the game to make sure your spawning mechanic works as intended.

### Creating a custom performance monitor

In this example, we'll create a custom performance monitor to track how many enemies are present in the currently running project.

The main scene features a [Timer](../godot_gdscript_misc.md) node with the following script attached:

```gdscript
extends Timer

func _ready():
    # The slash delimiter is used to determine the category of the monitor.
    # If there is no slash in the monitor name, a generic "Custom" category
    # will be used instead.
    Performance.add_custom_monitor("game/enemies", get_enemy_count)
    timeout.connect(_on_timeout)
    # Spawn 20 enemies per second.
    wait_time = 0.05
    start()

func _on_timeout():
    var enemy = preload("res://enemy.tscn").instantiate()
    get_parent().add_child(enemy)

# This function is called every time the performance monitor is queried
# (this occurs once per second in the editor, more if called manually).
# The function must return a number greater than or equal to 0 (int or float).
func get_enemy_count():
    return get_tree().get_nodes_in_group("enemies").size(
# ...
```

The second parameter of [Performance.add_custom_monitor](../godot_gdscript_core.md) is a [Callable](../godot_gdscript_misc.md).

`enemy.tscn` is a scene with a Node2D root node and Timer child node. The Node2D has the following script attached:

```gdscript
extends Node2D

func _ready():
    add_to_group("enemies")
    $Timer.timeout.connect(_on_timer_timeout)
    # Despawn enemies 2.5 seconds after they spawn.
    $Timer.wait_time = 2.5
    $Timer.start()

func _on_timer_timeout():
    queue_free()
```

In this example, since we spawn 20 enemies per second, and each enemy despawns 2.5 seconds after they spawn, we expect the number of enemies present in the scene to stabilize to 50. We can make sure about this by looking at the graph.

To visualize the graph created from this custom performance monitor, run the project, switch to the editor while the project is running and open **Debugger > Monitors** at the bottom of the editor window. Scroll down to the newly available **Game** section and check **Enemies**. You should see a graph appearing as follows:

> **Note:** The performance monitor handling code doesn't have to live in the same script as the nodes themselves. You may choose to move the performance monitor registration and getter function to an autoload instead.

### Querying a performance monitor in a project

If you wish to display the value of the performance monitor in the running project's window (rather than the editor), use `Performance.get_custom_monitor("category/name")` to fetch the value of the custom monitor. You can display the value using a [Label](../godot_gdscript_ui_controls.md), [RichTextLabel](../godot_gdscript_ui_controls.md), [Custom drawing in 2D](tutorials_2d.md), [3D text](tutorials_3d.md), etc.

This method can be used in exported projects as well (debug and release mode), which allows you to create visualizations outside the editor.

---

## Debugger panel

Many of Godot's debugging tools, including the debugger, can be found in the debugger panel at the bottom of the screen. Click on **Debugger** to open it.

The debugger panel is split into several tabs, each focusing on a specific task.

### Stack Trace

The Stack Trace tab opens automatically when the GDScript compiler reaches a breakpoint in your code.

It gives you a [stack trace](https://en.wikipedia.org/wiki/Stack_trace), information about the state of the object, and buttons to control the program's execution. When the debugger breaks on a breakpoint, a green triangle arrow is visible in the script editor's gutter. This arrow indicates the line of code the debugger broke on.

> **Tip:** You can create a breakpoint by clicking the gutter in the left of the script editor (on the left of the line numbers). When hovering this gutter, you will see a transparent red dot appearing, which turns into an opaque red dot after the breakpoint is placed by clicking. Click the red dot again to remove the breakpoint. Breakpoints created this way persist across editor restarts, even if the script wasn't saved when exiting the editor. You can also use the `breakpoint` keyword in GDScript to create a breakpoint that is stored in the script itself. Unlike breakpoints created by clicking in the gutter, this keyword-based breakpoint is persistent across different machines when using version control.

You can use the buttons in the top-right corner to:

- Skip all breakpoints. That way, you can save breakpoints for future debugging sessions.
- Copy the current error message.
- **Step Into** the code. This button takes you to the next line of code, and if it's a function, it steps line-by-line through the function.
- **Step Over** the code. This button goes to the next line of code, but it doesn't step line-by-line through functions.
- **Break**. This button pauses the game's execution.
- **Continue**. This button resumes the game after a breakpoint or pause.

> **Note:** Using the debugger and breakpoints on [tool scripts](tutorials_plugins.md) is not currently supported. Breakpoints placed in the script editor or using the `breakpoint` keyword are ignored. You can use print statements to display the contents of variables instead.

### Errors

This is where error and warning messages are printed while running the game.

You can disable specific warnings in **Project Settings > Debug > GDScript**.

### Evaluator

This tab contains an expression evaluator, also known as a REPL. This is a more powerful complement to the Stack Variables tree available in the Stack Trace tab.

When the project is interrupted in the debugger (due to a breakpoint or script error), you can enter an expression in the text field at the top. If the project is running, the expression field won't be editable, so you will need to set a breakpoint first. Expressions can be persisted across runs by unchecking **Clear on Run**, although they will be lost when the editor quits.

Expressions are evaluated using Godot's expression language, which allows you to perform arithmetic and call some functions within the expression. Expressions can refer to member variables, or local variables within the same scope as the line the breakpoint is on. You can also enter constant values, which makes it usable as a built-in calculator.

Consider the following script:

```gdscript
var counter = 0

func _process(delta):
    counter += 1
    if counter == 5:
        var text = "Some text"
        breakpoint
    elif counter >= 6:
        var other_text = "Some other text"
        breakpoint
```

If the debugger breaks on the **first** line containing `breakpoint`, the following expressions return non-null values:

- **Constant expression:** `2 * PI + 5`
- **Member variable:** `counter`, `counter ** 2`, `sqrt(counter)`
- **Local variable or function parameter:** `delta`, `text`, `text.to_upper()`

If the debugger breaks on the **second** line containing `breakpoint`, the following expressions return non-null values:

- **Constant expression:** `2 * PI + 5`
- **Member variable:** `counter`, `counter ** 2`, `sqrt(counter)`
- **Local variable or function parameter:** `delta`, `other_text`, `other_text.to_upper()`

### Profiler

The profiler is used to see what code is running while your project is in use, and how that effects performance.

> **See also:** A detailed explanation of how to use the profiler can be found in the dedicated The Profiler page.

### Visual Profiler

The Visual Profiler can be used to monitor what is taking the most time when rendering a frame on the CPU and GPU respectively. This allows tracking sources of potential CPU and GPU bottlenecks caused by rendering.

> **Warning:** The Visual Profiler only measures CPU time taken for rendering tasks, such as performing draw calls. The Visual Profiler does **not** include CPU time taken for other tasks such as scripting and physics. Use the standard Profiler tab to track non-rendering-related CPU tasks.

To use the visual profiler, run the project, switch to the **Visual Profiler** tab within the Debugger bottom panel, then click **Start**:

> **Tip:** You can also check **Autostart**, which will make the visual profiler automatically start when the project is run the next time. Note that the **Autostart** checkbox's state is not preserved across editor sessions.

You will see categories and results appearing as the profiler is running. Graph lines also appear, with the left side being a CPU framegraph and the right side being a GPU framegraph.

Click **Stop** to finish profiling, which will keep the results visible but frozen in place. Results remain visible after stopping the running project, but not after exiting the editor.

Click on result categories on the left to highlight them in the CPU and GPU graphs on the right. You can also click on the graph to move the cursor to a specific frame number and highlight the selected data type in the result categories on the left.

You can switch the result display between a time value (in milliseconds per frame) or a percentage of the target frametime (which is currently hardcoded to 16.67 milliseconds, or 60 FPS).

If framerate spikes occur during profiling, this can cause the graph to be poorly scaled. Disable **Fit to Frame** so that the graph will zoom onto the 60 FPS+ portion.

> **Note:** Remember that Visual Profiler results can vary **heavily** based on viewport resolution, which is determined by the window size if using the `disabled` or `canvas_items` [stretch modes](tutorials_rendering.md). When comparing results across different runs, make sure to use the same viewport size for all runs.

Visual Profiler is supported when using any rendering method (Forward+, Mobile or Compatibility), but the reported categories will vary depending on the current rendering method as well as the enabled graphics features. For example, when using Forward+, a simple 2D scene with shadow-casting lights will result in the following categories appearing:

To give another example with Forward+, a 3D scene with shadow-casting lights and various effects enabled will result in the following categories enabled:

Notice how in the 3D example, several of the categories have **(Parallel)** appended to their name. This hints that multiple tasks are being performed in parallel on the GPU. This generally means that disabling only one of the features involved won't improve performance as much as anticipated, as the other task still needs to be performed sequentially.

> **Note:** The Visual Profiler is not supported when using the Compatibility renderer on macOS, due to platform limitations.

### Network Profiler

The Network Profiler contains a list of all the nodes that communicate over the multiplayer API and, for each one, some counters on the amount of incoming and outgoing network interactions. It also features a bandwidth meter that displays the total bandwidth usage at any given moment.

> **Note:** The bandwidth meter does **not** take the [High-level multiplayer](tutorials_networking.md) API's own compression system into account. This means that changing the compression algorithm used will not change the metrics reported by the bandwidth meter.

### Monitors

The monitors are graphs of several aspects of the game while it's running such as FPS, memory usage, how many nodes are in a scene and more. All monitors keep track of stats automatically, so even if one monitor isn't open while the game is running, you can open it later and see how the values changed.

> **See also:** In addition to the default performance monitors, you can also create custom performance monitors to track arbitrary values in your project.

### Video RAM

The **Video RAM** tab shows the video RAM usage of the game while it is running. It provides a list of every resource using video RAM by resource path, the type of resource it is, what format it is in, and how much Video RAM that resource is using. There is also a total video RAM usage number at the top right of the panel.

### Misc

The **Misc** tab contains tools to identify the control nodes you are clicking at runtime:

- **Clicked Control** tells you where the clicked node is in the scene tree.
- **Clicked Control Type** tells you the type of the node you clicked is.

---

## Using the ObjectDB profiler

Since Godot 4.6, there is a new **ObjectDB Profiler** tab in the Debugger bottom panel. This profiler allows you to take snapshots of the current state of the ObjectDB, which is the database that contains all the [Object](../godot_gdscript_core.md)-derived classes currently allocated in memory. This is useful for identifying memory leaks and understanding the memory usage of your project.

Additionally, this tool is able to visualize differences between two snapshots. This can be used to identify improvements or regressions in memory usage after making changes to your project. Reducing memory usage can lead to better performance, even in cases where memory is not a bottleneck. By reducing memory usage, you can perform fewer allocations, which can be a costly operation, especially if performed in large amounts during gameplay.

> **See also:** See [When and how to avoid using nodes for everything](tutorials_best_practices.md) for information on using lighter-weight alternatives to nodes, which can help reduce memory usage in your project.

> **Warning:** The ObjectDB profiler does **not** track every bit of memory used by the engine or by external libraries. Native engine classes that are not exposed to the scripting API will not appear in snapshots. Consider using external memory profiling tools if you need access to this information.

### Usage

Open the ObjectDB Profiler tab in the Debugger bottom panel. You will land on the summary page with no snapshots taken yet.

Run the project, then get to a point where you'd like to take a snapshot (for example, after loading a level). Click Take ObjectDB Snapshot to take a snapshot at the current point in time. If the button appears grayed out, make sure the project is running first.

You can take multiple snapshots during a single run of the project. Also, you can right-click a snapshot in the snapshot list to rename it, show it in the file manager, or delete it.

> **Tip:** It's a good idea to rename snapshots after taking them to give them descriptive names (e.g., `before_optimization`, `after_optimization`). Regardless of the name, the date at which the snapshot was taken remains saved in the snapshot file itself. Snapshot files have a `.odb_snapshot` extension and are located in `user://objectdb_snapshots/` (see [Data paths](tutorials_io.md) details). These can safely be copied across devices, as they're platform-independent.

#### Viewing differences between snapshots

After taking at least two snapshots, the Diff Against dropdown becomes available. Here, you can select another snapshot to compare the currently selected snapshot with.

The summary page will then show the differences between the two snapshots:

This also applies to every other tab in the ObjectDB profiler, which will show the differences between the two snapshots in additional columns.

#### Classes

In the Classes tab, you can view how many instances of each class have been created at the moment the snapshot was taken:

When in diff mode, it will show the class instance count for the currently selected snapshot (column A) and the snapshot that is being diffed against (column B). It will also show the difference in instance count in the column Delta.

You can click on a class in the list on the right to view it in the inspector.

> **Tip:** Previewing instances in the inspector is also available in other tabs (Nodes, Objects, and RefCounted).

#### Objects

The Objects tab is similar, but differs in the way it presents data. Here, every instance is listed in a linear fashion, instead of grouping them by class. When selecting an object, you will see a list of other objects it references on the right (Outbound References), as well as a list of objects it's being referenced by (Inbound References).

This allows you to view objects either in a "top-down" manner (viewing what objects a given object references) or in a "bottom-up" manner (viewing what objects reference a given object).

In the above image, clicking the `default_font` object in the list will switch the view to the perspective of that object. This object is being referenced by a lot of other objects as well, which effectively switches to a "bottom-up" perspective.

#### Nodes

Next, the Nodes tab shows the scene tree at the time the snapshot was taken.

This tab is particularly interesting in diff view, since it supports showing the difference between the two snapshots in a more visual manner. When Combined Diff is unchecked, you can see the differences side by side.

When Combined Diff is checked, you can see the differences merged into a single tree, with added nodes highlighted in green and removed nodes highlighted in red.

Additionally, you can view a list of orphan nodes (nodes that are not attached to the scene tree root) at the end of the tree view. You can view it more easily by collapsing the root node, since these are listed outside the main scene tree.

#### RefCounted

The last tab is the RefCounted tab. This tab is similar to the Objects tab, but it shows the reference counts of [RefCounted](../godot_gdscript_core.md)-derived classes directly in the table. The table has four columns:

- **Native Refs:** The number of native engine references to the object.
- **ObjectDB Refs:** The number of ObjectDB references to the object.
- **Total Refs:** The sum of native references and ObjectDB references.
- **ObjectDB Cycles:** The number of circular references detected.

When in diff view, snapshot B is always listed _above_ snapshot A if a RefCounted instance exists in both snapshots.

The list on the right shows details on the selected instance, including a list of references and whether these are duplicates.

> **Note:** The RefCounted tab does **not** list objects that derive directly from [Object](../godot_gdscript_core.md), as these don't use reference counting.

---

## Output panel

The output panel is found at the bottom of the screen. Click on **Output** to open it.

The output panel provides several features to make viewing text printed by the project (and editor) easier.

> **Note:** The output panel automatically opens when running a project by default. You can control this behavior by changing the **Run > Bottom Panel > Action on Play** editor setting.

### Message categories

Four message categories are available:

- **Log:** Standard messages printed by the project. Displayed in white or black (depending on the editor theme).
- **Error:** Messages printed by the project or editor that indicate a failure of some kind. Displayed in red.
- **Warning:** Messages printed by the project or editor that report important information, but do not indicate a failure. Displayed in yellow.
- **Editor:** Messages printed by the editor, typically intended to be traces of undo/redo actions. Displayed in gray.

### Filtering messages

By clicking on the buttons on the right, you can hide certain message categories. This can make it easier to find specific messages you're looking for.

You can also filter messages by their text content using the **Filter Messages** box at the bottom of the Output panel.

### Clearing messages

When running the project, existing messages are automatically cleared by default. This is controlled by the **Run > Output > Always Clear Output on Play** editor setting. Additionally, you can manually clear messages by clicking the "cleaning brush" icon in the top-right corner of the Output panel.

### Printing messages

Several methods are available to print messages:

- `print()`: Prints a message. This method accepts multiple arguments which are concatenated together upon printing. This method has variants that separate arguments with tabs and spaces respectively: `printt()` and `prints()`.
- `print_rich()`: Same as `print()`, but BBCode can be used to format the text that is printed (see below).
- `push_error()`: Prints an error message. When an error is printed in a running project, it's displayed in the **Debugger > Errors** tab instead.
- `push_warning()`: Prints a warning message. When a warning is printed in a running project, it's displayed in the **Debugger > Errors** tab instead.

For more complex use cases, these can be used:

- `print_verbose()`: Same as `print()`, but only prints when verbose mode is enabled in the Project Settings or the project is run with the `--verbose` command line argument.
- `printerr()`: Same as `print()`, but prints to the standard error stream instead of the standard output string. `push_error()` should be preferred in most cases.
- `printraw()`: Same as `print()`, but prints without a blank line at the end. This is the only method that does **not** print to the editor Output panel. It prints to the standard output stream _only_, which means it's still included in file logging.
- `print_stack()`: Print a stack trace from the current location. Only supported when running from the editor, or when the project is exported in debug mode.
- [print_tree()](../godot_gdscript_misc.md): Prints the scene tree relative to the current node. Useful for debugging node structures created at runtime.
- [print_tree_pretty()](../godot_gdscript_misc.md): Same as `print_tree()`, but with Unicode characters for a more tree-like appearance. This relies on [box-drawing characters](https://en.wikipedia.org/wiki/Box-drawing_characters), so it may not render correctly with all fonts.

To get more advanced formatting capabilities, consider using GDScript format strings along with the above printing functions.

> **See also:** The engine's logging facilities are covered in the logging documentation.

#### Printing rich text

Using `print_rich()`, you can print rich text to the editor Output panel and standard output (visible when the user runs the project from a terminal). This works by converting the BBCode to [ANSI escape codes](https://en.wikipedia.org/wiki/ANSI_escape_code) that the terminal understands.

In the editor output, all BBCode tags are recognized as usual. In the terminal output, only a subset of BBCode tags will work, as documented in the linked `print_rich()` method description above. In the terminal, the colors will look different depending on the user's theme, while colors in the editor will use the same colors as they would in the project.

> **Note:** ANSI escape code support varies across terminal emulators. The exact colors displayed in terminal output also depend on the terminal theme chosen by the user.

---

## Overview of debugging tools

This guide will give you an overview of the available debugging tools in the engine.

Godot comes with a powerful debugger and profilers to track down bugs, inspect your game at runtime, monitor essential metrics, and measure performances. It also offers options to visualize collision boxes and navigation polygons in the running game.

Finally, you have options to debug the game running on a remote device and to reload changes to your scenes or your code while the game is running.

### Output Panel

The output panel allows you to see text printed by the project, but also by the editor (e.g. from `@tool` scripts). You can find information about in Output panel.

### Debugger Panel

Many of Godot's debugging tools are part of the Debugger panel, which you can find information about in Debugger panel.

### Debug menu options

There are a few common debug options you can toggle on or off when running your game in the editor, which can help you in debugging your game.

You can find these options in the **Debug** editor menu.

Here are the descriptions of the options:

#### Deploy with Remote Debug

When this option is enabled, using one-click deploy will make the executable attempt to connect to this computer's IP so the running project can be debugged. This option is intended to be used for remote debugging (typically with a mobile device). You don't need to enable it to use the GDScript debugger locally.

#### Small Deploy with Network Filesystem

This option speeds up testing for games with a large footprint on remote devices.

When **Small Deploy with Network Filesystem** is on, instead of exporting the full game, deploying the game builds a minimal executable. The editor then provides files from the project over the network.

Also, on Android, the game is deployed using the USB cable to speed up deployment.

#### Visible Collision Shapes

When this option is enabled, collision shapes and raycast nodes (for 2D and 3D) will be visible in the running project.

#### Visible Paths

When this option is enabled, curve resources used by path nodes will be visible in the running project.

#### Visible Navigation

When this option is enabled, navigation meshes, and polygons will be visible in the running project.

#### Visible Avoidance

When this option is enabled, avoidance object shapes, radiuses, and velocities will be visible in the running project.

#### Debug CanvasItem Redraws

When this option is enabled, redraw requests of 2D objects will become visible (as a short flash) in the running project. This is useful to troubleshoot low processor mode.

#### Synchronize Scene Changes

When this option is enabled, any changes made to the scene in the editor will be replicated in the running project. When used remotely on a device, this is more efficient when the network filesystem option is enabled.

#### Synchronize Script Changes

When this option is enabled, any changes made to the script in the editor will be reloaded in the running project. When used remotely on a device, this is more efficient with the network filesystem.

#### Keep Debug Server Open

When this option is enabled, the editor debug server will stay open and listen for new sessions started outside of the editor itself.

#### Customize Run Instances...

This opens a dialog allowing you to tell Godot to run multiple instances of the game at once, and to specify the command line arguments for each instance. This is especially useful when building and debugging multiplayer games.

##### Enable Multiple Instances

When this option is enabled, the editor will run multiple instances of the project at once when you Run Project.

Below this checkbox is a selector to pick how many instances to run.

Checking the box and setting this to only 1 is the same as not checking this box at all.

##### Main Run Args

These are the arguments that will be passed to **every** instance of the project when you Run Project, unless you select "Enabled" under "Override Main Run Args" for a specific instance.

Note that these arguments are space-separated.

> **Tip:** These arguments can be accessed in your script by using [get_cmdline_args](../godot_gdscript_misc.md).

> **Warning:** Even if you uncheck "Enable Multiple Instances" these arguments will be passed when you Run Project.

##### Main Feature Tags

These are the feature tags that will be passed to **every** instance of the project when you Run Project, unless you select "Enabled" under "Override Main Tags" for a specific instance.

##### Override Main Run Args

When this is enabled, the arguments in the "Main Run Args" field will **not be passed** to this specific instance of the project when you Run Project.

##### Launch Arguments

These are the arguments that will be passed to this specific instance of the project when you Run Project. They will be **combined with** the "Main Run Args" unless you select "Enabled" under "Override Main Run Args".

##### Override Main Tags

When this is enabled, the tags in the "Main Feature Tags" field will **not be passed** to this specific instance of the project when you Run Project.

##### Feature Tags

These are the feature tags that will be passed to this specific instance of the project when you Run Project. They will be **combined with** the "Main Feature Tags" unless you select "Enabled" under "Override Main Tags".

> **Warning:** If you want to pass "User" arguments, that can be accessed with [get_cmdline_user_args](../godot_gdscript_misc.md) then you must prefix them with two dashes **and a space** like -- one two three. Be aware that these dashes will apply to arguments added later in the "Launch Arguments" on a per instance basis, which can cause some confusion when combining the Main Run Args and Launch Arguments. If you place -- one two three in the "Main Run Args" and -- four five six in the "Launch Arguments" then the final command line arguments will be one two three -- four five six. This is because the -- is repeated in the "Launch Arguments".

### Script editor debug tools and options

The script editor has its own set of debug tools for use with breakpoints and two options. The breakpoint tools can also be found in the **Debugger** tab of the debugger.

> **Tip:** You can create a breakpoint by clicking the gutter in the left of the script editor (on the left of the line numbers). When hovering this gutter, you will see a transparent red dot appearing, which turns into an opaque red dot after the breakpoint is placed by clicking. Click the red dot again to remove the breakpoint. Breakpoints created this way persist across editor restarts, even if the script wasn't saved when exiting the editor. You can also use the `breakpoint` keyword in GDScript to create a breakpoint that is stored in the script itself. Unlike breakpoints created by clicking in the gutter, this keyword-based breakpoint is persistent across different machines when using version control.

The **Break** button causes a break in the script like a breakpoint would. **Continue** makes the game continue after pausing at a breakpoint. **Step Over** goes to the next line of code, and **Step Into** goes into a function if possible. Otherwise, it does the same thing as **Step Over**.

The **Debug with External Editor** option lets you debug your game with an external editor. You can set a shortcut for it in **Editor Settings > Shortcuts > Debugger**.

When the debugger breaks on a breakpoint, a green triangle arrow is visible in the script editor's gutter. This arrow indicates the line of code the debugger broke on.

### Debug project settings

In the project settings, there is a **Debug** category with subcategories which control different things. Enable **Advanced Settings** to change these settings.

#### Settings

These are some general settings such as printing the current FPS to the **Output** panel, the maximum amount of functions when profiling and others.

#### File Logging

These settings allow you to log console output and error messages to files.

#### GDScript

These settings allow you to toggle specific GDScript warnings, such as for unused variables. You can also turn off warnings completely. See GDScript warning system for more information.

#### Shader Language

These settings allow you to toggle specific shader warnings, such as for unused variables. You can also turn off warnings completely.

#### Canvas Items

These settings are for canvas item redraw debugging.

#### Shapes

Shapes are where you can adjust the color of shapes that only appear for debugging purposes, such as collision and navigation shapes.

### Remote in scene dock

When running a game in the editor two options appear at the top of the **Scene** dock, **Remote** and **Local**. While using **Remote** you can inspect or change the nodes' parameters in the running project.

> **Note:** Some editor settings related to debugging can be found inside the **Editor Settings**, under the **Network > Debug** and **Debugger** sections.

---
