# Godot 4 C# Tutorials — Scripting (Part 5)

> 6 tutorials. C#-specific code examples.

## Using the ObjectDB profiler

Since Godot 4.6, there is a new **ObjectDB Profiler** tab in the Debugger bottom panel. This profiler allows you to take snapshots of the current state of the ObjectDB, which is the database that contains all the [Object](../godot_csharp_core.md)-derived classes currently allocated in memory. This is useful for identifying memory leaks and understanding the memory usage of your project.

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

The last tab is the RefCounted tab. This tab is similar to the Objects tab, but it shows the reference counts of [RefCounted](../godot_csharp_core.md)-derived classes directly in the table. The table has four columns:

- **Native Refs:** The number of native engine references to the object.
- **ObjectDB Refs:** The number of ObjectDB references to the object.
- **Total Refs:** The sum of native references and ObjectDB references.
- **ObjectDB Cycles:** The number of circular references detected.

When in diff view, snapshot B is always listed _above_ snapshot A if a RefCounted instance exists in both snapshots.

The list on the right shows details on the selected instance, including a list of references and whether these are duplicates.

> **Note:** The RefCounted tab does **not** list objects that derive directly from [Object](../godot_csharp_core.md), as these don't use reference counting.

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
- [print_tree()](../godot_csharp_misc.md): Prints the scene tree relative to the current node. Useful for debugging node structures created at runtime.
- [print_tree_pretty()](../godot_csharp_misc.md): Same as `print_tree()`, but with Unicode characters for a more tree-like appearance. This relies on [box-drawing characters](https://en.wikipedia.org/wiki/Box-drawing_characters), so it may not render correctly with all fonts.

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

> **Tip:** These arguments can be accessed in your script by using [get_cmdline_args](../godot_csharp_misc.md).

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

> **Warning:** If you want to pass "User" arguments, that can be accessed with [get_cmdline_user_args](../godot_csharp_misc.md) then you must prefix them with two dashes **and a space** like -- one two three. Be aware that these dashes will apply to arguments added later in the "Launch Arguments" on a per instance basis, which can cause some confusion when combining the Main Run Args and Launch Arguments. If you place -- one two three in the "Main Run Args" and -- four five six in the "Launch Arguments" then the final command line arguments will be one two three -- four five six. This is because the -- is repeated in the "Launch Arguments".

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

## The Profiler

You run your game from Godot and play around. It's fun, it's becoming feature complete, and you feel it's getting close to release.

But then, you open the skill tree, and it grinds to a halt as something snags in your code. Watching the skill tree scroll by like it's a slide show is unacceptable. What went wrong? Is it positioning the skill tree elements, the UI, or rendering?

You could try to optimize everything and run the game repeatedly, but you can be smarter about this and narrow down the possibilities. Enter Godot's profiler.

### An overview of the profiler

You can open the profiler by opening the **Debugger** panel and clicking on the **Profiler** tab.

Godot's profiler does not automatically run because profiling is performance-intensive. It has to continually measure everything happening in the game and report back to the debugger, so it's off by default.

To begin profiling, run your game then focus back on the editor. Click on the **Start** button in the top-left corner of the **Profiler** tab. You can also check **Autostart**, which will make the profiler automatically start when the project is run the next time. Note that the **Autostart** checkbox's state is not preserved across editor sessions.

> **Note:** The profiler does not currently support C# scripts. C# scripts can be profiled using JetBrains Rider and JetBrains dotTrace with the Godot support plugin.

You can clear the data by clicking the **Clear** button anytime. Use the **Measure** drop-down menu to change the type of data you measure. The measurements panel and the graph will update accordingly.

### The measured data

The profiler's interface is split into two. There is a list of functions on the left and the performance graph on the right.

The main measurements are frame time, physics frame, idle time, and physics time.

- The **frame time** is the time it takes Godot to execute all the logic for an entire image, from physics to rendering.
- **Physics frame** is the time Godot has allocated between physics updates. In an ideal scenario, the frame time is whatever you chose: 16.66 milliseconds by default, which corresponds to 60FPS. It's a frame of reference you can use for everything else around it.
- **Idle time** is the time Godot took to update logic other than physics, such as code that lives in \_process or timers and cameras set to update on **Idle**.
- **Physics time** is the time Godot took to update physics tasks, like \_physics_process and built-in nodes set to **Physics** update.

> **Note:** **Frame Time** includes rendering time. Say you find a mysterious spike of lag in your game, but your physics and scripts are all running fast. The delay could be due to the appearance of particles or visual effects!

By default, Godot ticks on Frame Time and Physics Time. This gives you an overview of how long each frame takes relative to the allocated desired physics FPS. You can toggle functions on and off by clicking the checkboxes on the left. Other facilities make appearances as you go down the list, like Physics 2D, Physics, and Audio, before reaching Script functions, where your code appears.

If you click on the graph, you change which frame's information appears on the left. In the top right, there is also a frame counter where you can manually adjust the frame you are looking at more granularly.

### Scope of measurement and measurement windows

You can change what measurement you are looking at using the **Measure** drop-down menu. By default, it starts with Frame Time and lists the time it takes to go through the frame in milliseconds. The average time is the average time any given function took when called more than once. For example, a function that took 0.05 milliseconds to run five times should give you an average of 0.01 milliseconds.

If accurate milliseconds count is not important, and you want to see proportions of time relative to the rest of the frame, use percentage measurements. Frame % is relative to Frame Time, and Physics % is relative to Physics Time.

The last option is the scope of the time. **Inclusive** measures the time a function took **with** any nested function calls. For example:

get_neighbors, find_nearest_neighbor and move_subject all took a lot of time. You could be fooled into thinking that this is because all three of them are slow.

But when changed to **Self**, Godot measures the time spent in the function body without considering function calls it made itself.

You can see that get_neighbors and move_subject have lost a lot of their importance. In effect, that means that get_neighbors and move_subject have spent more time waiting for some other function call to finish than not, and find_nearest_neighbor is **actually** slow.

### Debugging slow code with the profiler

Finding slow code with the profiler boils down to running your game and watching the performance graph as it draws. When an unacceptable spike occurs in the frame time, you can click on the graph to pause your game and narrow the _Frame #_ to the spike's start. You may need to jump back and forth between frames and functions to find the root cause.

Under the Script functions, turn on the checkboxes for some functions to find which take time. These are the functions you need to review and optimize.

### Measuring manually in microseconds

If your function is complex, it could be challenging to figure out which part needs optimization. Is it your math or the way you access other pieces of data to do the math with? Is it the for loop? The if statements?

You can narrow down the measurement by manually counting ticks as the code runs with some temporary functions. The two functions are part of the Time class object. They are get_ticks_msec and get_ticks_usec. The first measures in milliseconds (1,000 per second), and the second measures in microseconds (1,000,000 per second).

Either one returns the amount of time since the game engine started in their respective time frame.

If you wrap a piece of code with a start and end count of microseconds, the difference between the two is the amount of time it took to run that piece of code.

As you become a more experienced programmer, this technique becomes less necessary. You begin to learn what parts of a running program are slow. Knowing that loops and branches can be slow comes from experience, and you gain experience by measuring and doing research.

But between the profiler and the ticks functions, you should have enough to get started finding which parts of your code need optimization.

---

## Evaluating expressions

Godot provides an [Expression](../godot_csharp_misc.md) class you can use to evaluate expressions.

An expression can be:

- A mathematical expression such as `(2 + 4) * 16/4.0`.
- A boolean expression such as `true && false`.
- A built-in method call like `deg_to_rad(90)`.
- A method call on a user-provided script like `update_health()`, if `base_instance` is set to a value other than `null` when calling [Expression.execute()](../godot_csharp_misc.md).

> **Note:** The Expression class is independent from GDScript. It's available even if you compile Godot with the GDScript module disabled.

### Basic usage

To evaluate a mathematical expression, use:

The following operators are available:

| Operator            | Notes                                                                                                                                            |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| Addition +          | Can also be used to concatenate strings and arrays: - "hello" + " world" = hello world - [1, 2] + [3, 4] = [1, 2, 3, 4]                          |
| Subtraction (-)     |                                                                                                                                                  |
| Multiplication (\*) |                                                                                                                                                  |
| Division (/)        | Performs and integer division if both operands are integers. If at least one of them is a floating-point number, returns a floating-point value. |
| Remainder (%)       | Returns the remainder of an integer division (modulo). The result will always have the sign of the dividend.                                     |
| Conjunction (&&)    | Returns the result of a boolean AND.                                                                                                             |
| Disjunction (\|\|)  | Returns the result of a boolean OR.                                                                                                              |
| Negation (!)        | Returns the result of a boolean NOT.                                                                                                             |

Spaces around operators are optional. Also, keep in mind the usual [order of operations](https://en.wikipedia.org/wiki/Order_of_operations) applies. Use parentheses to override the order of operations if needed.

All the Variant types supported in Godot can be used: integers, floating-point numbers, strings, arrays, dictionaries, colors, vectors, …

Arrays and dictionaries can be indexed like in GDScript:

### Passing variables to an expression

You can pass variables to an expression. These variables will then become available in the expression's "context" and will be substituted when used in the expression:

Both the variable names and variable values **must** be specified as an array, even if you only define one variable. Also, variable names are **case-sensitive**.

### Setting a base instance for the expression

By default, an expression has a base instance of `null`. This means the expression has no base instance associated to it.

When calling [Expression.execute()](../godot_csharp_misc.md), you can set the value of the `base_instance` parameter to a specific object instance such as `self`, another script instance or even a singleton:

Associating a base instance allows doing the following:

- Reference the instance's constants (`const`) in the expression.
- Reference the instance's member variables (`var`) in the expression.
- Call methods defined in the instance and use their return values in the expression.

> **Warning:** Setting a base instance to a value other than `null` allows referencing constants, member variables, and calling all methods defined in the script attached to the instance. Allowing users to enter expressions may allow cheating in your game, or may even introduce security vulnerabilities if you allow arbitrary clients to run expressions on other players' devices.

### Example script

The script below demonstrates what the Expression class is capable of:

The output from the script will be:

### Built-in functions

All methods in the `Global Scope` are available in the Expression class, even if no base instance is bound to the expression. The same parameters and return types are available.

However, unlike GDScript, parameters are **always required** even if they're specified as being optional in the class reference. In contrast, this restriction on arguments doesn't apply to user-made functions when you bind a base instance to the expression.

---

## File system

### Introduction

A file system manages how assets are stored and how they are accessed. A well-designed file system also allows multiple developers to edit the same source files and assets while collaborating. Godot stores all assets as files in its file system.

### Implementation

The file system stores resources on disk. Anything, from a script, to a scene or a PNG image is a resource to the engine. If a resource contains properties that reference other resources on disk, the paths to those resources are also included. If a resource has sub-resources that are built-in, the resource is saved in a single file together with all the bundled sub-resources. For example, a font resource is often bundled together with the font textures.

The Godot file system avoids using metadata files. Existing asset managers and VCSs are better than anything we can implement, so Godot tries its best to play along with Subversion, Git, Mercurial, etc.

Example of file system contents:

```none
/project.godot
/enemy/enemy.tscn
/enemy/enemy.gd
/enemy/enemysprite.png
/player/player.gd
```

### project.godot

The `project.godot` file is the project description file, and it is always found at the root of the project. In fact, its location defines where the root is. This is the first file that Godot looks for when opening a project.

This file contains the project configuration in plain text, using the win.ini format. Even an empty `project.godot` can function as a basic definition of a blank project.

### Path delimiter

Godot only supports `/` as a path delimiter. This is done for portability reasons. All operating systems support this, even Windows, so a path such as `C:\project\project.godot` needs to be typed as `C:/project/project.godot`.

### Resource path

When accessing resources, using the host OS file system layout can be cumbersome and non-portable. To solve this problem, the special path `res://` was created.

The path `res://` will always point at the project root (where `project.godot` is located, so `res://project.godot` is always valid).

This file system is read-write only when running the project locally from the editor. When exported or when running on different devices (such as phones or consoles, or running from DVD), the file system will become read-only and writing will no longer be permitted.

### User path

Writing to disk is still needed for tasks such as saving game state or downloading content packs. To this end, the engine ensures that there is a special path `user://` that is always writable. This path resolves differently depending on the OS the project is running on. Local path resolution is further explained in [File paths in Godot projects](tutorials_io.md).

### Host file system

Alternatively host file system paths can also be used, but this is not recommended for a released product as these paths are not guaranteed to work on all platforms. However, using host file system paths can be useful when writing development tools in Godot.

### Drawbacks

There are some drawbacks to this file system design. The first issue is that moving assets around (renaming them or moving them from one path to another inside the project) will break existing references to these assets. These references will have to be re-defined to point at the new asset location.

To avoid this, do all your move, delete and rename operations from within Godot, on the FileSystem dock. When you delete files in Godot, it will prompt you with a confirmation dialog listing all selected files and any scenes that depend on those files. Never move assets from outside Godot, or dependencies will have to be fixed manually (Godot detects this and helps you fix them anyway, but why go the hard route?).

The second is that, under Windows and macOS, file and path names are case insensitive. If a developer working in a case insensitive host file system saves an asset as `myfile.PNG`, but then references it as `myfile.png`, it will work fine on their platform, but not on other platforms, such as Linux, Android, etc. This may also apply to exported binaries, which use a compressed package to store all files.

It is recommended that your team clearly define a naming convention for files when working with Godot. One fool-proof convention is to only allow lowercase file and path names.

---
