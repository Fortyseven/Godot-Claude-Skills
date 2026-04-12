# Godot 4 GDScript Tutorials — Best Practices (Part 1)

> 8 tutorials. GDScript-specific code examples.

## Autoloads versus regular nodes

Godot offers a feature to automatically load nodes at the root of your project, allowing you to access them globally, that can fulfill the role of a Singleton: [Singletons (Autoload)](tutorials_scripting.md). These autoloaded nodes are not freed when you change the scene from code with [SceneTree.change_scene_to_file](../godot_gdscript_core.md).

In this guide, you will learn when to use the Autoload feature, and techniques you can use to avoid it.

### The cutting audio issue

Other engines can encourage the use of creating manager classes, singletons that organize a lot of functionality into a globally accessible object. Godot offers many ways to avoid global state thanks to the node tree and signals.

For example, let's say we are building a platformer and want to collect coins that play a sound effect. There's a node for that: the [AudioStreamPlayer](../godot_gdscript_audio.md). But if we call the `AudioStreamPlayer` while it is already playing a sound, the new sound interrupts the first.

A solution is to code a global, autoloaded sound manager class. It generates a pool of `AudioStreamPlayer` nodes that cycle through as each new request for sound effects comes in. Say we call that class `Sound`, you can use it from anywhere in your project by calling `Sound.play("coin_pickup.ogg")`. This solves the problem in the short term but causes more problems:

1. **Global state**: one object is now responsible for all objects' data. If the `Sound` class has errors or doesn't have an AudioStreamPlayer available, all the nodes calling it can break.
2. **Global access**: now that any object can call `Sound.play(sound_path)` from anywhere, there's no longer an easy way to find the source of a bug.
3. **Global resource allocation**: with a pool of `AudioStreamPlayer` nodes stored from the start, you can either have too few and face bugs, or too many and use more memory than you need.

> **Note:** About global access, the problem is that any code anywhere could pass wrong data to the `Sound` autoload in our example. As a result, the domain to explore to fix the bug spans the entire project. When you keep code inside a scene, only one or two scripts may be involved in audio.

Contrast this with each scene keeping as many `AudioStreamPlayer` nodes as it needs within itself and all these problems go away:

1. Each scene manages its own state information. If there is a problem with the data, it will only cause issues in that one scene.
2. Each scene accesses only its own nodes. Now, if there is a bug, it's easy to find which node is at fault.
3. Each scene allocates exactly the amount of resources it needs.

### Managing shared functionality or data

Another reason to use an Autoload can be that you want to reuse the same method or data across many scenes.

In the case of functions, you can create a new type of `Node` that provides that feature for an individual scene using the [class_name](tutorials_scripting.md) keyword in GDScript.

When it comes to data, you can either:

1. Create a new type of [Resource](../godot_gdscript_core.md) to share the data.
2. Store the data in an object to which each node has access, for example using the `owner` property to access the scene's root node.

### When you should use an Autoload

GDScript supports the creation of `static` functions using `static func`. When combined with `class_name`, this makes it possible to create libraries of helper functions without having to create an instance to call them. The limitation of static functions is that they can't reference member variables, non-static functions or `self`.

Since Godot 4.1, GDScript also supports `static` variables using `static var`. This means you can now share variables across instances of a class without having to create a separate autoload.

Still, autoloaded nodes can simplify your code for systems with a wide scope. If the autoload is managing its own information and not invading the data of other objects, then it's a great way to create systems that handle broad-scoped tasks. For example, a quest or a dialogue system.

> **Note:** An autoload is _not_ necessarily a singleton. Nothing prevents you from instantiating copies of an autoloaded node. An autoload is only a tool that makes a node load automatically as a child of the root of your scene tree, regardless of your game's node structure or which scene you run, e.g. by pressing the F6 key. As a result, you can get the autoloaded node, for example an autoload called `Sound`, by calling `get_node("/root/Sound")`.

---

## Data preferences

> **Work in progress:** The content of this page was not yet updated for Godot `4.6` and may be **outdated**. If you know how to improve this page or you can confirm that it's up to date, feel free to [open a pull request](https://github.com/godotengine/godot-docs).

Ever wondered whether one should approach problem X with data structure Y or Z? This article covers a variety of topics related to these dilemmas.

> **Note:** This article makes references to "[something]-time" operations. This terminology comes from algorithm analysis' [Big O Notation](https://rob-bell.net/2009/06/a-beginners-guide-to-big-o-notation/). Long-story short, it describes the worst-case scenario of runtime length. In laymen's terms: "As the size of a problem domain increases, the runtime length of the algorithm..." - Constant-time, `O(1)`: "...does not increase."

- Logarithmic-time, `O(log n)`: "...increases at a slow rate."
- Linear-time, `O(n)`: "...increases at the same rate."
- Etc. Imagine if one had to process 3 million data points within a single frame. It would be impossible to craft the feature with a linear-time algorithm since the sheer size of the data would increase the runtime far beyond the time allotted. In comparison, using a constant-time algorithm could handle the operation without issue. By and large, developers want to avoid engaging in linear-time operations as much as possible. But, if one keeps the scale of a linear-time operation small, and if one does not need to perform the operation often, then it may be acceptable. Balancing these requirements and choosing the right algorithm / data structure for the job is part of what makes programmers' skills valuable.

### Array vs. Dictionary vs. Object

Godot stores all variables in the scripting API in the Variant class. Variants can store Variant-compatible data structures such as [Array](../godot_gdscript_misc.md) and [Dictionary](../godot_gdscript_misc.md) as well as [Objects](../godot_gdscript_core.md).

Godot implements Array as a `Vector<Variant>`. The engine stores the Array contents in a contiguous section of memory, i.e. they are in a row adjacent to each other.

> **Note:** For those unfamiliar with C++, a Vector is the name of the array object in traditional C++ libraries. It is a "templated" type, meaning that its records can only contain a particular type (denoted by angled brackets). So, for example, a [PackedStringArray](../godot_gdscript_misc.md) would be something like a `Vector<String>`.

Contiguous memory stores imply the following operation performance:

- **Iterate:** Fastest. Great for loops.

- Op: All it does is increment a counter to get to the next record.
- **Insert, Erase, Move:** Position-dependent. Generally slow.

- Op: Adding/removing/moving content involves moving the adjacent records over (to make room / fill space).
- Fast add/remove _from the end_.
- Slow add/remove _from an arbitrary position_.
- Slowest add/remove _from the front_.
- If doing many inserts/removals _from the front_, then...

1. invert the array.
2. do a loop which executes the Array changes _at the end_.
3. re-invert the array.

This makes only 2 copies of the array (still constant time, but slow) versus copying roughly 1/2 of the array, on average, N times (linear time).

- **Get, Set:** Fastest _by position_. E.g. can request 0th, 2nd, 10th record, etc. but cannot specify which record you want.

- Op: 1 addition operation from array start position up to desired index.
- **Find:** Slowest. Identifies the index/position of a value.

- Op: Must iterate through array and compare values until one finds a match.

- Performance is also dependent on whether one needs an exhaustive search.
- If kept ordered, custom search operations can bring it to logarithmic time (relatively fast). Laymen users won't be comfortable with this though. Done by re-sorting the Array after every edit and writing an ordered-aware search algorithm.

Godot implements Dictionary as a `HashMap<Variant, Variant, VariantHasher, StringLikeVariantComparator>`. The engine stores a small array (initialized to 2^3 or 8 records) of key-value pairs. When one attempts to access a value, they provide it a key. It then _hashes_ the key, i.e. converts it into a number. The "hash" is used to calculate the index into the array. As an array, the HM then has a quick lookup within the "table" of keys mapped to values. When the HashMap becomes too full, it increases to the next power of 2 (so, 16 records, then 32, etc.) and rebuilds the structure.

Hashes are to reduce the chance of a key collision. If one occurs, the table must recalculate another index for the value that takes the previous position into account. In all, this results in constant-time access to all records at the expense of memory and some minor operational efficiency.

1. Hashing every key an arbitrary number of times.

- Hash operations are constant-time, so even if an algorithm must do more than one, as long as the number of hash calculations doesn't become too dependent on the density of the table, things will stay fast. Which leads to...

2. Maintaining an ever-growing size for the table.

- HashMaps maintain gaps of unused memory interspersed in the table on purpose to reduce hash collisions and maintain the speed of accesses. This is why it constantly increases in size exponentially by powers of 2.

As one might be able to tell, Dictionaries specialize in tasks that Arrays do not. An overview of their operational details is as follows:

- **Iterate:** Fast.

- Op: Iterate over the map's internal vector of hashes. Return each key. Afterwards, users then use the key to jump to and return the desired value.
- **Insert, Erase, Move:** Fastest.

- Op: Hash the given key. Do 1 addition operation to look up the appropriate value (array start + offset). Move is two of these (one insert, one erase). The map must do some maintenance to preserve its capabilities:

- update ordered List of records.
- determine if table density mandates a need to expand table capacity.
- The Dictionary remembers in what order users inserted its keys. This enables it to execute reliable iterations.
- **Get, Set:** Fastest. Same as a lookup _by key_.

- Op: Same as insert/erase/move.
- **Find:** Slowest. Identifies the key of a value.

- Op: Must iterate through records and compare the value until a match is found.
- Note that Godot does not provide this feature out-of-the-box (because they aren't meant for this task).

Godot implements Objects as stupid, but dynamic containers of data content. Objects query data sources when posed questions. For example, to answer the question, "do you have a property called, 'position'?", it might ask its [script](../godot_gdscript_misc.md) or the [ClassDB](../godot_gdscript_core.md). One can find more information about what objects are and how they work in the Applying object-oriented principles in Godot article.

The important detail here is the complexity of the Object's task. Every time it performs one of these multi-source queries, it runs through _several_ iteration loops and HashMap lookups. What's more, the queries are linear-time operations dependent on the Object's inheritance hierarchy size. If the class the Object queries (its current class) doesn't find anything, the request defers to the next base class, all the way up until the original Object class. While these are each fast operations in isolation, the fact that it must make so many checks is what makes them slower than both of the alternatives for looking up data.

> **Note:** When developers mention how slow the scripting API is, it is this chain of queries they refer to. Compared to compiled C++ code where the application knows exactly where to go to find anything, it is inevitable that scripting API operations will take much longer. They must locate the source of any relevant data before they can attempt to access it. The reason GDScript is slow is because every operation it performs passes through this system. C# can process some content at higher speeds via more optimized bytecode. But, if the C# script calls into an engine class' content or if the script tries to access something external to it, it will go through this pipeline. NativeScript C++ goes even further and keeps everything internal by default. Calls into external structures will go through the scripting API. In NativeScript C++, registering methods to expose them to the scripting API is a manual task. It is at this point that external, non-C++ classes will use the API to locate them.

So, assuming one extends from Reference to create a data structure, like an Array or Dictionary, why choose an Object over the other two options?

1. **Control:** With objects comes the ability to create more sophisticated structures. One can layer abstractions over the data to ensure the external API doesn't change in response to internal data structure changes. What's more, Objects can have signals, allowing for reactive behavior.
2. **Clarity:** Objects are a reliable data source when it comes to the data that scripts and engine classes define for them. Properties may not hold the values one expects, but one doesn't need to worry about whether the property exists in the first place.
3. **Convenience:** If one already has a similar data structure in mind, then extending from an existing class makes the task of building the data structure much easier. In comparison, Arrays and Dictionaries don't fulfill all use cases one might have.

Objects also give users the opportunity to create even more specialized data structures. With it, one can design their own List, Binary Search Tree, Heap, Splay Tree, Graph, Disjoint Set, and any host of other options.

"Why not use Node for tree structures?" one might ask. Well, the Node class contains things that won't be relevant to one's custom data structure. As such, it can be helpful to construct one's own node type when building tree structures.

```gdscript
class_name TreeNode
extends Object

var _parent: TreeNode = null
var _children := []

func _notification(p_what):
    match p_what:
        NOTIFICATION_PREDELETE:
            # Destructor.
            for a_child in _children:
                a_child.free()
```

From here, one can then create their own structures with specific features, limited only by their imagination.

### Enumerations: int vs. string

Most languages offer an enumeration type option. GDScript is no different, but unlike most other languages, it allows one to use either integers or strings for the enum values (the latter only when using the `@export_enum` annotation in GDScript). The question then arises, "which should one use?"

The short answer is, "whichever you are more comfortable with." This is a feature specific to GDScript and not Godot scripting in general; The languages prioritizes usability over performance.

On a technical level, integer comparisons (constant-time) will happen faster than string comparisons (linear-time). If one wants to keep up other languages' conventions though, then one should use integers.

The primary issue with using integers comes up when one wants to _print_ an enum value. As integers, attempting to print `MY_ENUM` will print `5` or what-have-you, rather than something like `"MyEnum"`. To print an integer enum, one would have to write a Dictionary that maps the corresponding string value for each enum.

If the primary purpose of using an enum is for printing values and one wishes to group them together as related concepts, then it makes sense to use them as strings. That way, a separate data structure to execute on the printing is unnecessary.

### AnimatedTexture vs. AnimatedSprite2D vs. AnimationPlayer vs. AnimationTree

Under what circumstances should one use each of Godot's animation classes? The answer may not be immediately clear to new Godot users.

[AnimatedTexture](../godot_gdscript_resources.md) is a texture that the engine draws as an animated loop rather than a static image. Users can manipulate...

1. the rate at which it moves across each section of the texture (FPS).
2. the number of regions contained within the texture (frames).

Godot's [RenderingServer](../godot_gdscript_rendering.md) then draws the regions in sequence at the prescribed rate. The good news is that this involves no extra logic on the part of the engine. The bad news is that users have very little control.

Also note that AnimatedTexture is a [Resource](../godot_gdscript_core.md) unlike the other [Node](../godot_gdscript_core.md) objects discussed here. One might create a [Sprite2D](../godot_gdscript_nodes_2d.md) node that uses AnimatedTexture as its texture. Or (something the others can't do) one could add AnimatedTextures as tiles in a [TileSet](../godot_gdscript_resources.md) and integrate it with a [TileMapLayer](../godot_gdscript_nodes_2d.md) for many auto-animating backgrounds that all render in a single batched draw call.

The [AnimatedSprite2D](../godot_gdscript_nodes_2d.md) node, in combination with the [SpriteFrames](../godot_gdscript_misc.md) resource, allows one to create a variety of animation sequences through spritesheets, flip between animations, and control their speed, regional offset, and orientation. This makes them well-suited to controlling 2D frame-based animations.

If one needs to trigger other effects in relation to animation changes (for example, create particle effects, call functions, or manipulate other peripheral elements besides the frame-based animation), then one will need to use an [AnimationPlayer](../godot_gdscript_resources.md) node in conjunction with the AnimatedSprite2D.

AnimationPlayers are also the tool one will need to use if they wish to design more complex 2D animation systems, such as...

1. **Cut-out animations:** editing sprites' transforms at runtime.
2. **2D Mesh animations:** defining a region for the sprite's texture and rigging a skeleton to it. Then one animates the bones which stretch and bend the texture in proportion to the bones' relationships to each other.
3. A mix of the above.

While one needs an AnimationPlayer to design each of the individual animation sequences for a game, it can also be useful to combine animations for blending, i.e. enabling smooth transitions between these animations. There may also be a hierarchical structure between animations that one plans out for their object. These are the cases where the [AnimationTree](../godot_gdscript_resources.md) shines. One can find an in-depth guide on using the AnimationTree [here](tutorials_animation.md).

---

## Godot interfaces

Often one needs scripts that rely on other objects for features. There are 2 parts to this process:

1. Acquiring a reference to the object that presumably has the features.
2. Accessing the data or logic from the object.

The rest of this tutorial outlines the various ways of doing all this.

### Acquiring object references

For all [Object](../godot_gdscript_core.md)s, the most basic way of referencing them is to get a reference to an existing object from another acquired instance.

```gdscript
var obj = node.object # Property access.
var obj = node.get_object() # Method access.
```

The same principle applies for [RefCounted](../godot_gdscript_core.md) objects. While users often access [Node](../godot_gdscript_core.md) and [Resource](../godot_gdscript_core.md) this way, alternative measures are available.

Instead of property or method access, one can get Resources by load access.

```gdscript
# If you need an "export const var" (which doesn't exist), use a conditional
# setter for a tool script that checks if it's executing in the editor.
# The `@tool` annotation must be placed at the top of the script.
@tool

# Load resource during scene load.
var preres = preload(path)
# Load resource when program reaches statement.
var res = load(path)

# Note that users load scenes and scripts, by convention, with PascalCase
# names (like typenames), often into constants.
const MyScene = preload("my_scene.tscn") # Static load
const MyScript = preload("my_script.gd")

# This type's value varies, i.e. it is a variable, so it uses snake_case.
@export var script_type: Script

# Must configure from the editor, defaults to null.
@export var const_script: Script:
    set(value):
        if Engine.
# ...
```

Note the following:

1. There are many ways in which a language can load such resources.
2. When designing how objects will access data, don't forget that one can pass resources around as references as well.
3. Keep in mind that loading a resource fetches the cached resource instance maintained by the engine. To get a new object, one must [duplicate](../godot_gdscript_misc.md) an existing reference or instantiate one from scratch with `new()`.

Nodes likewise have an alternative access point: the SceneTree.

```gdscript
extends Node

# Slow.
func dynamic_lookup_with_dynamic_nodepath():
    print(get_node("Child"))

# Faster. GDScript only.
func dynamic_lookup_with_cached_nodepath():
    print($Child)

# Fastest. Doesn't break if node moves later.
# Note that `@onready` annotation is GDScript-only.
# Other languages must do...
#     var child
#     func _ready():
#         child = get_node("Child")
@onready var child = $Child
func lookup_and_cache_for_future_access():
    print(child)

# Fastest. Doesn't break if node is moved in the Scene tree dock.
# Node must be selected in the inspector as it's an exported property.
@export var child: Node
func lookup_and_cache_for_future_access():
    print(child)

# Delegate reference assignment to an external source.
# Con: need to perform a validation check.
# Pro:
# ...
```

### Accessing data or logic from an object

Godot's scripting API is duck-typed. This means that if a script executes an operation, Godot doesn't validate that it supports the operation by **type**. It instead checks that the object **implements** the individual method.

For example, the [CanvasItem](../godot_gdscript_nodes_2d.md) class has a `visible` property. All properties exposed to the scripting API are in fact a setter and getter pair bound to a name. If one tried to access [CanvasItem.visible](../godot_gdscript_nodes_2d.md), then Godot would do the following checks, in order:

- If the object has a script attached, it will attempt to set the property through the script. This leaves open the opportunity for scripts to override a property defined on a base object by overriding the setter method for the property.
- If the script does not have the property, it performs a HashMap lookup in the ClassDB for the "visible" property against the CanvasItem class and all of its inherited types. If found, it will call the bound setter or getter. For more information about HashMaps, see the data preferences docs.
- If not found, it does an explicit check to see if the user wants to access the "script" or "meta" properties.
- If not, it checks for a `_set`/`_get` implementation (depending on type of access) in the CanvasItem and its inherited types. These methods can execute logic that gives the impression that the Object has a property. This is also the case with the `_get_property_list` method.

- Note that this happens even for non-legal symbol names, such as names starting with a digit or containing a slash.

As a result, this duck-typed system can locate a property either in the script, the object's class, or any class that object inherits, but only for things which extend Object.

Godot provides a variety of options for performing runtime checks on these accesses:

- A duck-typed property access. These will be property checks (as described above). If the operation isn't supported by the object, execution will halt.

```gdscript
# All Objects have duck-typed get, set, and call wrapper methods.
get_parent().set("visible", false)

# Using a symbol accessor, rather than a string in the method call,
# will implicitly call the `set` method which, in turn, calls the
# setter method bound to the property through the property lookup
# sequence.
get_parent().visible = false

# Note that if one defines a _set and _get that describe a property's
# existence, but the property isn't recognized in any _get_property_list
# method, then the set() and get() methods will work, but the symbol
# access will claim it can't find the property.
```

- A method check. In the case of [CanvasItem.visible](../godot_gdscript_nodes_2d.md), one can access the methods, `set_visible` and `is_visible` like any other method.

```gdscript
var child = get_child(0)

# Dynamic lookup.
child.call("set_visible", false)

# Symbol-based dynamic lookup.
# GDScript aliases this into a 'call' method behind the scenes.
child.set_visible(false)

# Dynamic lookup, checks for method existence first.
if child.has_method("set_visible"):
    child.set_visible(false)

# Cast check, followed by dynamic lookup.
# Useful when you make multiple "safe" calls knowing that the class
# implements them all. No need for repeated checks.
# Tricky if one executes a cast check for a user-defined type as it
# forces more dependencies.
if child is CanvasItem:
    child.set_visible(false)
    child.show_on_top = true

# If one does not wish to fail these checks without notifying users,
# one can use an assert instead. These will trigger runtime errors
# imm
# ...
```

- Outsource the access to a [Callable](../godot_gdscript_misc.md). These may be useful in cases where one needs the max level of freedom from dependencies. In this case, one relies on an external context to setup the method.

```gdscript
# child.gd
extends Node
var fn = null

func my_method():
    if fn:
        fn.call()

# parent.gd
extends Node

@onready var child = $Child

func _ready():
    child.fn = print_me
    child.my_method()

func print_me():
    print(name)
```

These strategies contribute to Godot's flexible design. Between them, users have a breadth of tools to meet their specific needs.

---

## Godot notifications

Every Object in Godot implements a [\_notification](../godot_gdscript_misc.md) method. Its purpose is to allow the Object to respond to a variety of engine-level callbacks that may relate to it. For example, if the engine tells a [CanvasItem](../godot_gdscript_nodes_2d.md) to "draw", it will call `_notification(NOTIFICATION_DRAW)`.

Some of these notifications, like draw, are useful to override in scripts. So much so that Godot exposes many of them with dedicated functions:

- `_ready()`: `NOTIFICATION_READY`
- `_enter_tree()`: `NOTIFICATION_ENTER_TREE`
- `_exit_tree()`: `NOTIFICATION_EXIT_TREE`
- `_process(delta)`: `NOTIFICATION_PROCESS`
- `_physics_process(delta)`: `NOTIFICATION_PHYSICS_PROCESS`
- `_draw()`: `NOTIFICATION_DRAW`

What users might _not_ realize is that notifications exist for types other than Node alone, for example:

- [Object::NOTIFICATION_POSTINITIALIZE](../godot_gdscript_core.md): a callback that triggers during object initialization. Not accessible to scripts.
- [Object::NOTIFICATION_PREDELETE](../godot_gdscript_core.md): a callback that triggers before the engine deletes an Object, i.e. a "destructor".

And many of the callbacks that _do_ exist in Nodes don't have any dedicated methods, but are still quite useful.

- [Node::NOTIFICATION_PARENTED](../godot_gdscript_misc.md): a callback that triggers anytime one adds a child node to another node.
- [Node::NOTIFICATION_UNPARENTED](../godot_gdscript_misc.md): a callback that triggers anytime one removes a child node from another node.

One can access all these custom notifications from the universal `_notification()` method.

> **Note:** Methods in the documentation labeled as "virtual" are also intended to be overridden by scripts. A classic example is the [\_init](../godot_gdscript_misc.md) method in Object. While it has no `NOTIFICATION_*` equivalent, the engine still calls the method. Most languages (except C#) rely on it as a constructor.

So, in which situation should one use each of these notifications or virtual functions?

### \_process vs. \_physics_process vs. \*\_input

Use `_process()` when one needs a framerate-dependent delta time between frames. If code that updates object data needs to update as often as possible, this is the right place. Recurring logic checks and data caching often execute here, but it comes down to the frequency at which one needs the evaluations to update. If they don't need to execute every frame, then implementing a Timer-timeout loop is another option.

```gdscript
# Allows for recurring operations that don't trigger script logic
# every frame (or even every fixed frame).
func _ready():
    var timer = Timer.new()
    timer.autostart = true
    timer.wait_time = 0.5
    add_child(timer)
    timer.timeout.connect(func():
        print("This block runs every 0.5 seconds")
    )
```

Use `_physics_process()` when one needs a framerate-independent delta time between frames. If code needs consistent updates over time, regardless of how fast or slow time advances, this is the right place. Recurring kinematic and object transform operations should execute here.

While it is possible, to achieve the best performance, one should avoid making input checks during these callbacks. `_process()` and `_physics_process()` will trigger at every opportunity (they do not "rest" by default). In contrast, `*_input()` callbacks will trigger only on frames in which the engine has actually detected the input.

One can check for input actions within the input callbacks just the same. If one wants to use delta time, one can fetch it from the related delta time methods as needed.

```gdscript
# Called every frame, even when the engine detects no input.
func _process(delta):
    if Input.is_action_just_pressed("ui_select"):
        print(delta)

# Called during every input event.
func _unhandled_input(event):
    match event.get_class():
        "InputEventKey":
            if Input.is_action_just_pressed("ui_accept"):
                print(get_process_delta_time())
```

### \_init vs. initialization vs. export

If the script initializes its own node subtree, without a scene, that code should execute in `_init()`. Other property or SceneTree-independent initializations should also run here.

> **Note:** The C# equivalent to GDScript's `_init()` method is the constructor.

`_init()` triggers before `_enter_tree()` or `_ready()`, but after a script creates and initializes its properties. When instantiating a scene, property values will set up according to the following sequence:

1. **Initial value assignment:** the property is assigned its initialization value, or its default value if one is not specified. If a setter exists, it is not used.
2. `_init()` **assignment:** the property's value is replaced by any assignments made in `_init()`, triggering the setter.
3. **Exported value assignment:** an exported property's value is again replaced by any value set in the Inspector, triggering the setter.

```gdscript
# test is initialized to "one", without triggering the setter.
@export var test: String = "one":
    set(value):
        test = value + "!"

func _init():
    # Triggers the setter, changing test's value from "one" to "two!".
    test = "two"

# If someone sets test to "three" from the Inspector, it would trigger
# the setter, changing test's value from "two!" to "three!".
```

As a result, instantiating a script versus a scene may affect both the initialization _and_ the number of times the engine calls the setter.

### \_ready vs. \_enter_tree vs. NOTIFICATION_PARENTED

When instantiating a scene connected to the first executed scene, Godot will instantiate nodes down the tree (making `_init()` calls) and build the tree going downwards from the root. This causes `_enter_tree()` calls to cascade down the tree. Once the tree is complete, leaf nodes call `_ready`. A node will call this method once all child nodes have finished calling theirs. This then causes a reverse cascade going up back to the tree's root.

When instantiating a script or a standalone scene, nodes are not added to the SceneTree upon creation, so no `_enter_tree()` callbacks trigger. Instead, only the `_init()` call occurs. When the scene is added to the SceneTree, the `_enter_tree()` and `_ready()` calls occur.

If one needs to trigger behavior that occurs as nodes parent to another, regardless of whether it occurs as part of the main/active scene or not, one can use the [PARENTED](../godot_gdscript_misc.md) notification. For example, here is a snippet that connects a node's method to a custom signal on the parent node without failing. Useful on data-centric nodes that one might create at runtime.

```gdscript
extends Node

var parent_cache

func connection_check():
    return parent_cache.has_user_signal("interacted_with")

func _notification(what):
    match what:
        NOTIFICATION_PARENTED:
            parent_cache = get_parent()
            if connection_check():
                parent_cache.interacted_with.connect(_on_parent_interacted_with)
        NOTIFICATION_UNPARENTED:
            if connection_check():
                parent_cache.interacted_with.disconnect(_on_parent_interacted_with)

func _on_parent_interacted_with():
    print("I'm reacting to my parent's interaction!")
```

---

## Introduction

This series is a collection of best practices to help you work efficiently with Godot.

Godot allows for a great amount of flexibility in how you structure a project's codebase and break it down into scenes. Each approach has its pros and cons, and they can be hard to weigh until you've worked with the engine for long enough.

There are always many ways to structure your code and solve specific programming problems. It would be impossible to cover them all here.

That is why each article starts from a real-world problem. We will break down each problem in fundamental questions, suggest solutions, analyze the pros and cons of each option, and highlight the best course of action for the problem at hand.

You should start by reading Applying object-oriented principles in Godot. It explains how Godot's nodes and scenes relate to classes and objects in other Object-Oriented programming languages. It will help you make sense of the rest of the series.

> **Note:** The best practices in Godot rely on Object-Oriented design principles. We use tools like the [single responsibility](https://en.wikipedia.org/wiki/Single_responsibility_principle) principle and [encapsulation](<https://en.wikipedia.org/wiki/Encapsulation_(computer_programming)>).

---

## Logic preferences

Ever wondered whether one should approach problem X with strategy Y or Z? This article covers a variety of topics related to these dilemmas.

### Adding nodes and changing properties: which first?

When initializing nodes from a script at runtime, you may need to change properties such as the node's name or position. A common dilemma is, when should you change those values?

It is the best practice to change values on a node before adding it to the scene tree. Some properties' setters have code to update other corresponding values, and that code can be slow! For most cases, this code has no impact on your game's performance, but in heavy use cases such as procedural generation, it can bring your game to a crawl.

For these reasons, it is usually best practice to set the initial values of a node before adding it to the scene tree. There are some exceptions where values _can't_ be set before being added to the scene tree, like setting global position.

### Loading vs. preloading

In GDScript, there exists the global `preload` method. It loads resources as early as possible to front-load the "loading" operations and avoid loading resources while in the middle of performance-sensitive code.

Its counterpart, the `load` method, loads a resource only when it reaches the load statement. That is, it will load a resource in-place which can cause slowdowns when it occurs in the middle of sensitive processes. The `load()` function is also an alias for [ResourceLoader.load(path)](../godot_gdscript_core.md) which is accessible to _all_ scripting languages.

So, when exactly does preloading occur versus loading, and when should one use either? Let's see an example:

```gdscript
# my_buildings.gd
extends Node

# Note how constant scripts/scenes have a different naming scheme than
# their property variants.

# This value is a constant, so it spawns when the Script object loads.
# The script is preloading the value. The advantage here is that the editor
# can offer autocompletion since it must be a static path.
const BuildingScn = preload("res://building.tscn")

# 1. The script preloads the value, so it will load as a dependency
#    of the 'my_buildings.gd' script file. But, because this is a
#    property rather than a constant, the object won't copy the preloaded
#    PackedScene resource into the property until the script instantiates
#    with .new().
#
# 2. The preloaded value is inaccessible from the Script object alone. As
#    such, preloading the value her
# ...
```

Preloading allows the script to handle all the loading the moment one loads the script. Preloading is useful, but there are also times when one doesn't wish to use it. Here are a few considerations when determining which to use:

1. If one cannot determine when the script might load, then preloading a resource (especially a scene or script) could result in additional loads one does not expect. This could lead to unintentional, variable-length load times on top of the original script's load operations.
2. If something else could replace the value (like a scene's exported initialization), then preloading the value has no meaning. This point isn't a significant factor if one intends to always create the script on its own.
3. If one wishes only to 'import' another class resource (script or scene), then using a preloaded constant is often the best course of action. However, in exceptional cases, one may wish not to do this:

4. If the 'imported' class is liable to change, then it should be a property instead, initialized either using an `@export` or a `load()` (and perhaps not even initialized until later).
5. If the script requires a great many dependencies, and one does not wish to consume so much memory, then one may wish to load and unload various dependencies at runtime as circumstances change. If one preloads resources into constants, then the only way to unload these resources would be to unload the entire script. If they are instead loaded as properties, then one can set these properties to `null` and remove all references to the resource (which, as a [RefCounted](../godot_gdscript_core.md)-extending type, will cause the resources to delete themselves from memory).

### Large levels: static vs. dynamic

If one is creating a large level, which circumstances are most appropriate? Is it better to create the level as one static space? Or is it better to load the level in pieces and shift the world's content as needed?

Well, the simple answer is, "when the performance requires it." The dilemma associated with the two options is one of the age-old programming choices: does one optimize memory over speed, or vice versa?

The naive answer is to use a static level that loads everything at once. But, depending on the project, this could consume a large amount of memory. Wasting users' RAM leads to programs running slow or outright crashing from everything else the computer tries to do at the same time.

No matter what, one should break larger scenes into smaller ones (to aid in reusability of assets). Developers can then design a node that manages the creation/loading and deletion/unloading of resources and nodes in real-time. Games with large and varied environments or procedurally generated elements often implement these strategies to avoid wasting memory.

On the flip side, coding a dynamic system is more complex; it uses more programmed logic which results in opportunities for errors and bugs. If one isn't careful, they can develop a system that bloats the technical debt of the application.

As such, the best options would be...

1. Use static levels for smaller games.
2. If one has the time/resources on a medium/large game, create a library or plugin that can manage nodes and resources with code. If refined over time so as to improve usability and stability, then it could evolve into a reliable tool across projects.
3. Use dynamic logic for a medium/large game because one has the coding skills, but not the time or resources to refine the code (game's gotta get done). Could potentially refactor later to outsource the code into a plugin.

For an example of the various ways one can swap scenes around at runtime, please see the ["Change scenes manually"](tutorials_scripting.md) documentation.

---

## When and how to avoid using nodes for everything

Nodes are cheap to produce, but even they have their limits. A project may have tens of thousands of nodes all doing things. The more complex their behavior though, the larger the strain each one adds to a project's performance.

Godot provides more lightweight objects for creating APIs which nodes use. Be sure to keep these in mind as options when designing how you wish to build your project's features.

1. [Object](../godot_gdscript_core.md): The ultimate lightweight object, the original Object must use manual memory management. With that said, it isn't too difficult to create one's own custom data structures, even node structures, that are also lighter than the [Node](../godot_gdscript_core.md) class.

- **Example:** See the [Tree](../godot_gdscript_ui_controls.md) node. It supports a high level of customization for a table of content with an arbitrary number of rows and columns. The data that it uses to generate its visualization though is actually a tree of [TreeItem](../godot_gdscript_misc.md) Objects.
- **Advantages:** Simplifying one's API to smaller scoped objects helps improve its accessibility and improve iteration time. Rather than working with the entire Node library, one creates an abbreviated set of Objects from which a node can generate and manage the appropriate sub-nodes.

> **Note:** One should be careful when handling them. One can store an Object into a variable, but these references can become invalid without warning. For example, if the object's creator decides to delete it out of nowhere, this would trigger an error state when one next accesses it. 2. [RefCounted](../godot_gdscript_core.md): Only a little more complex than Object. They track references to themselves, only deleting loaded memory when no further references to themselves exist. These are useful in the majority of cases where one needs data in a custom class.

- **Example:** See the [FileAccess](../godot_gdscript_filesystem.md) object. It functions just like a regular Object except that one need not delete it themselves.
- **Advantages:** same as the Object.

3. [Resource](../godot_gdscript_core.md): Only slightly more complex than RefCounted. They have the innate ability to serialize/deserialize (i.e. save and load) their object properties to/from Godot resource files.

- **Example:** Scripts, PackedScene (for scene files), and other types like each of the [AudioEffect](../godot_gdscript_audio.md) classes. Each of these can be saved and loaded, therefore they extend from Resource.
- **Advantages:** Much has [already been said](tutorials_scripting.md) on [Resource](../godot_gdscript_core.md)'s advantages over traditional data storage methods. In the context of using Resources over Nodes though, their main advantage is in Inspector-compatibility. While nearly as lightweight as Object/RefCounted, they can still display and export properties in the Inspector. This allows them to fulfill a purpose much like sub-Nodes on the usability front, but also improve performance if one plans to have many such Resources/Nodes in their scenes.

---

## Project organization

### Introduction

Since Godot has no restrictions on project structure or filesystem usage, organizing files when learning the engine can seem challenging. This tutorial suggests a workflow which should be a good starting point. We will also cover using version control with Godot.

### Organization

Godot is scene-based in nature, and uses the filesystem as-is, without metadata or an asset database.

Unlike other engines, many resources are contained within the scene itself, so the amount of files in the filesystem is considerably lower.

Considering that, the most common approach is to group assets as close to scenes as possible; when a project grows, it makes it more maintainable.

As an example, one can usually place into a single folder their basic assets, such as sprite images, 3D model meshes, materials, and music, etc. They can then use a separate folder to store built levels that use them.

```none
/project.godot
/docs/.gdignore  # See "Ignoring specific folders" below
/docs/learning.html
/models/town/house/house.dae
/models/town/house/window.png
/models/town/house/door.png
/characters/player/cubio.dae
/characters/player/cubio.png
/characters/enemies/goblin/goblin.dae
/characters/enemies/goblin/goblin.png
/characters/npcs/suzanne/suzanne.dae
/characters/npcs/suzanne/suzanne.png
/levels/riverdale/riverdale.scn
```

### Style guide

For consistency across projects, we recommend following these guidelines:

- Use **snake_case** for folder and file names (with the exception of C# scripts). This sidesteps case sensitivity issues that can crop up after exporting a project on Windows. C# scripts are an exception to this rule, as the convention is to name them after the class name which should be in PascalCase.
- Use **PascalCase** for node names, as this matches built-in node casing.
- In general, keep third-party resources in a top-level `addons/` folder, even if they aren't editor plugins. This makes it easier to track which files are third-party. There are some exceptions to this rule; for instance, if you use third-party game assets for a character, it makes more sense to include them within the same folder as the character scenes and scripts.

### Importing

Godot versions prior to 3.0 did the import process from files outside the project. While this can be useful in large projects, it resulted in an organization hassle for most developers.

Because of this, assets are now transparently imported from within the project folder.

#### Ignoring specific folders

To prevent Godot from importing files contained in a specific folder, create an empty file called `.gdignore` in the folder (the leading `.` is required). This can be useful to speed up the initial project importing.

> **Note:** To create a file whose name starts with a dot on Windows, place a dot at both the beginning and end of the filename (".gdignore."). Windows will automatically remove the trailing dot when you confirm the name. Alternatively, you can use a text editor such as Notepad++ or use the following command in a command prompt: `type nul > .gdignore`

Once the folder is ignored, resources in that folder can't be loaded anymore using the `load()` and `preload()` methods. Ignoring a folder will also automatically hide it from the FileSystem dock, which can be useful to reduce clutter.

Note that the `.gdignore` file's contents are ignored, which is why the file should be empty. It does not support patterns like `.gitignore` files do.

### Case sensitivity

Windows and recent macOS versions use case-insensitive filesystems by default, whereas Linux distributions use a case-sensitive filesystem by default. This can cause issues after exporting a project, since Godot's PCK virtual filesystem is case-sensitive. To avoid this, it's recommended to stick to `snake_case` naming for all files in the project (and lowercase characters in general).

> **Note:** You can break this rule when style guides say otherwise (such as the C# style guide). Still, be consistent to avoid mistakes.

On Windows 10, to further avoid mistakes related to case sensitivity, you can also make the project folder case-sensitive. After enabling the Windows Subsystem for Linux feature, run the following command in a PowerShell window:

```gdscript
# To enable case-sensitivity:
fsutil file setcasesensitiveinfo <path to project folder> enable

# To disable case-sensitivity:
fsutil file setcasesensitiveinfo <path to project folder> disable
```

If you haven't enabled the Windows Subsystem for Linux, you can enter the following line in a PowerShell window _running as Administrator_ then reboot when asked:

```gdscript
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux
```

---
