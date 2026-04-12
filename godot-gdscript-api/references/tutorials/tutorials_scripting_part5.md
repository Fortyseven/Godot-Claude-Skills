# Godot 4 GDScript Tutorials — Scripting (Part 5)

> 3 tutorials. GDScript-specific code examples.

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

```gdscript
# Measuring the time it takes for worker_function() to run
var start = Time.get_ticks_usec()
worker_function()
var end = Time.get_ticks_usec()
var worker_time = (end-start)/1000000.0

# Measuring the time spent running a calculation over each element of an array
start = Time.get_ticks_usec()
for calc in calculations:
    result = pow(2, calc.power) * calc.product
end = Time.get_ticks_usec()
var loop_time = (end-start)/1000000.0

print("Worker time: %s\nLoop time: %s" % [worker_time, loop_time])
```

As you become a more experienced programmer, this technique becomes less necessary. You begin to learn what parts of a running program are slow. Knowing that loops and branches can be slow comes from experience, and you gain experience by measuring and doing research.

But between the profiler and the ticks functions, you should have enough to get started finding which parts of your code need optimization.

---

## Evaluating expressions

Godot provides an [Expression](../godot_gdscript_misc.md) class you can use to evaluate expressions.

An expression can be:

- A mathematical expression such as `(2 + 4) * 16/4.0`.
- A boolean expression such as `true && false`.
- A built-in method call like `deg_to_rad(90)`.
- A method call on a user-provided script like `update_health()`, if `base_instance` is set to a value other than `null` when calling [Expression.execute()](../godot_gdscript_misc.md).

> **Note:** The Expression class is independent from GDScript. It's available even if you compile Godot with the GDScript module disabled.

### Basic usage

To evaluate a mathematical expression, use:

```gdscript
var expression = Expression.new()
expression.parse("20 + 10*2 - 5/2.0")
var result = expression.execute()
print(result)  # 37.5
```

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

```gdscript
# Returns 1.
[1, 2][0]

# Returns 3. Negative indices can be used to count from the end of the array.
[1, 3][-1]

# Returns "green".
{"favorite_color": "green"}["favorite_color"]

# All 3 lines below return 7.0 (Vector3 is floating-point).
Vector3(5, 6, 7)[2]
Vector3(5, 6, 7)["z"]
Vector3(5, 6, 7).z
```

### Passing variables to an expression

You can pass variables to an expression. These variables will then become available in the expression's "context" and will be substituted when used in the expression:

```gdscript
var expression = Expression.new()
# Define the variable names first in the second parameter of `parse()`.
# In this example, we use `x` for the variable name.
expression.parse("20 + 2 * x", ["x"])
# Then define the variable values in the first parameter of `execute()`.
# Here, `x` is assigned the integer value 5.
var result = expression.execute([5])
print(result)  # 30
```

Both the variable names and variable values **must** be specified as an array, even if you only define one variable. Also, variable names are **case-sensitive**.

### Setting a base instance for the expression

By default, an expression has a base instance of `null`. This means the expression has no base instance associated to it.

When calling [Expression.execute()](../godot_gdscript_misc.md), you can set the value of the `base_instance` parameter to a specific object instance such as `self`, another script instance or even a singleton:

```gdscript
func double(number):
    return number * 2

func _ready():
    var expression = Expression.new()
    expression.parse("double(10)")

    # This won't work since we're not passing the current script as the base instance.
    var result = expression.execute([], null)
    print(result)  # null

    # This will work since we're passing the current script (i.e. self)
    # as the base instance.
    result = expression.execute([], self)
    print(result)  # 20
```

Associating a base instance allows doing the following:

- Reference the instance's constants (`const`) in the expression.
- Reference the instance's member variables (`var`) in the expression.
- Call methods defined in the instance and use their return values in the expression.

> **Warning:** Setting a base instance to a value other than `null` allows referencing constants, member variables, and calling all methods defined in the script attached to the instance. Allowing users to enter expressions may allow cheating in your game, or may even introduce security vulnerabilities if you allow arbitrary clients to run expressions on other players' devices.

### Example script

The script below demonstrates what the Expression class is capable of:

```gdscript
const DAYS_IN_YEAR = 365
var script_member_variable = 1000

func _ready():
    # Constant boolean expression.
    evaluate("true && false")
    # Boolean expression with variables.
    evaluate("!(a && b)", ["a", "b"], [true, false])

    # Constant mathexpression.
    evaluate("2 + 2")
    # Math expression with variables.
    evaluate("x + y", ["x", "y"], [60, 100])

    # Call built-in method (built-in math function call).
    evaluate("deg_to_rad(90)")

    # Call user method (defined in the script).
    # We can do this because the expression execution is bound to `self`
    # in the `evaluate()` method.
    # Since this user method returns a value, we can use it in math expressions.
    evaluate("call_me() + DAYS_IN_YEAR + script_member_variable")
    evaluate("call_me(42)")
    eva
# ...
```

The output from the script will be:

```gdscript
false
true
4
160
1.5707963267949

You called 'call_me()' in the expression text.
1365

You called 'call_me()' in the expression text.
Argument passed: 42
0

You called 'call_me()' in the expression text.
Argument passed: some string
0
```

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
