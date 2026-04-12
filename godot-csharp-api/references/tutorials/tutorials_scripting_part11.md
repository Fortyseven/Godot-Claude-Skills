# Godot 4 C# Tutorials — Scripting (Part 11)

> 4 tutorials. C#-specific code examples.

## Resources

### Nodes and resources

Up to this tutorial, we focused on the [Node](../godot_csharp_core.md) class in Godot as that's the one you use to code behavior and most of the engine's features rely on it. There is another datatype that is just as important: [Resource](../godot_csharp_core.md).

_Nodes_ give you functionality: they draw sprites, 3D models, simulate physics, arrange user interfaces, etc. **Resources** are **data containers**. They don't do anything on their own: instead, nodes use the data contained in resources.

Anything Godot saves or loads from disk is a resource. Be it a scene (a `.tscn` or a `.scn` file), an image, a script... Here are some [Resource](../godot_csharp_core.md) examples:

- [Texture](../godot_csharp_resources.md)
- [Script](../godot_csharp_resources.md)
- [Mesh](../godot_csharp_rendering.md)
- [Animation](../godot_csharp_resources.md)
- [AudioStream](../godot_csharp_audio.md)
- [Font](../godot_csharp_resources.md)
- [Translation](../godot_csharp_misc.md)

When the engine loads a resource from disk, **it only loads it once**. If a copy of that resource is already in memory, trying to load the resource again will return the same copy every time. As resources only contain data, there is no need to duplicate them.

Every object, be it a Node or a Resource, can export properties. There are many types of Properties, like String, integer, Vector2, etc., and any of these types can become a resource. This means that both nodes and resources can contain resources as properties:

### External vs built-in

There are two ways to save resources. They can be:

1. **External** to a scene, saved on the disk as individual files.
2. **Built-in**, saved inside the `.tscn` or the `.scn` file they're attached to.

To be more specific, here's a [Texture2D](../godot_csharp_resources.md) in a [Sprite2D](../godot_csharp_nodes_2d.md) node:

Clicking the resource preview allows us to view the resource's properties.

The path property tells us where the resource comes from. In this case, it comes from a PNG image called `robi.png`. When the resource comes from a file like this, it is an external resource. If you erase the path or this path is empty, it becomes a built-in resource.

The switch between built-in and external resources happens when you save the scene. In the example above, if you erase the path `"res://robi.png"` and save, Godot will save the image inside the `.tscn` scene file.

> **Note:** Even if you save a built-in resource, when you instance a scene multiple times, the engine will only load one copy of it.

### Loading resources from code

There are two ways to load resources from code. First, you can use the `load()` function anytime:

```csharp
public override void _Ready()
{
    // Godot loads the Resource when it executes this line.
    var texture = GD.Load<Texture>("res://Robi.png");
    var sprite = GetNode<Sprite2D>("sprite");
    sprite.Texture = texture;
}
```

You can also `preload` resources. Unlike `load`, this function will read the file from disk and load it at compile-time. As a result, you cannot call `preload` with a variable path: you need to use a constant string.

```csharp
// 'preload()' is unavailable in C Sharp.
```

### Loading scenes

Scenes are also resources, but there is a catch. Scenes saved to disk are resources of type [PackedScene](../godot_csharp_resources.md). The scene is packed inside a [Resource](../godot_csharp_core.md).

To get an instance of the scene, you have to use the [PackedScene.instantiate()](../godot_csharp_resources.md) method.

```csharp
private PackedScene _bulletScene = GD.Load<PackedScene>("res://Bullet.tscn");

private void OnShoot()
{
    Node bullet = _bulletScene.Instantiate();
    AddChild(bullet);
}
```

This method creates the nodes in the scene's hierarchy, configures them, and returns the root node of the scene. You can then add it as a child of any other node.

The approach has several advantages. As the [PackedScene.instantiate()](../godot_csharp_resources.md) function is fast, you can create new enemies, bullets, effects, etc. without having to load them again from disk each time. Remember that, as always, images, meshes, etc. are all shared between the scene instances.

### Freeing resources

When a [Resource](../godot_csharp_core.md) is no longer in use, it will automatically free itself. Since, in most cases, Resources are contained in Nodes, when you free a node, the engine frees all the resources it owns as well if no other node uses them.

### Creating your own resources

Like any Object in Godot, users can also script Resources. Resource scripts inherit the ability to freely translate between object properties and serialized text or binary data (_.tres, _.res). They also inherit the reference-counting memory management from the RefCounted type.

This comes with many distinct advantages over alternative data structures, such as JSON, CSV, or custom TXT files. Users can only import these assets as a [Dictionary](../godot_csharp_misc.md) (JSON) or as a [FileAccess](../godot_csharp_filesystem.md) to parse. What sets Resources apart is their inheritance of [Object](../godot_csharp_core.md), [RefCounted](../godot_csharp_core.md), and [Resource](../godot_csharp_core.md) features:

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

Let's see some examples. Create a [Resource](../godot_csharp_core.md) and name it `bot_stats`. It should appear in your file tab with the full name `bot_stats.tres`. Without a script, it's useless, so let's add some data and logic! Attach a script to it named `bot_stats.gd` (or just create a new script, and then drag it to it).

> **Note:** To make the new resource class appear in the Create Resource GUI you need to provide a class name for GDScript, or use the [GlobalClass] attribute in C#.

```csharp
// BotStats.cs
using Godot;

namespace ExampleProject
{
    [GlobalClass]
    public partial class BotStats : Resource
    {
        [Export]
        public int Health { get; set; }

        [Export]
        public Resource SubResource { get; set; }

        [Export]
        public string[] Strings { get; set; }

        // Make sure you provide a parameterless constructor.
        // In C#, a parameterless constructor is different from a
        // constructor with all default values.
        // Without a parameterless constructor, Godot will have problems
        // creating and editing your resource via the inspector.
        public BotStats() : this(0, null, null) {}

        public BotStats(int health, Resource subResource, string[] strings)
        {
            Health = health;

// ...
```

Now, create a [CharacterBody3D](../godot_csharp_nodes_3d.md), name it `Bot`, and add the following script to it:

```csharp
// Bot.cs
using Godot;

namespace ExampleProject
{
    public partial class Bot : CharacterBody3D
    {
        [Export]
        public Resource Stats;

        public override void _Ready()
        {
            if (Stats is BotStats botStats)
            {
                GD.Print(botStats.Health); // Prints '10'.
            }
        }
    }
}
```

Now, select the [CharacterBody3D](../godot_csharp_nodes_3d.md) node which we named `bot`, and drag&drop the `bot_stats.tres` resource onto the Inspector. It should print 10! Obviously, this setup can be used for more advanced features than this, but as long you really understand _how_ it all worked, you should figure out everything else related to Resources.

> **Note:** Resource scripts are similar to Unity's ScriptableObjects. The Inspector provides built-in support for custom resources. If desired though, users can even design their own Control-based tool scripts and combine them with an [EditorPlugin](../godot_csharp_editor.md) to create custom visualizations and editors for their data. Unreal Engine's DataTables and CurveTables are also easy to recreate with Resource scripts. DataTables are a String mapped to a custom struct, similar to a Dictionary mapping a String to a secondary custom Resource script. ```csharp
> using Godot;

[GlobalClass]
public partial class BotStatsTable : Resource
{
private Godot.Collections.Dictionary<string, BotStats> \_stats = new Godot.Collections.Dictionary<string, BotStats>();

    public BotStatsTable()
    {
        _stats["GodotBot"] = new BotStats(10); // Creates instance with 10 health.
        _stats["DifferentBot"] = new BotStats(20); // A different one with 20 health.
        GD.Print(_stats);
    }

}

````Instead of inlining the Dictionary values, one could also, alternatively: 1. Import a table of values from a spreadsheet and generate these key-value pairs.
2. Design a visualization within the editor and create a plugin that adds it to the Inspector when you open these types of Resources. CurveTables are the same thing, except mapped to an Array of float values or a [Curve](../godot_csharp_resources.md)/[Curve2D](../godot_csharp_resources.md) resource object.



> **Warning:** Beware that resource files (*.tres/*.res) will store the path of the script they use in the file. When loaded, they will fetch and load this script as an extension of their type. This means that trying to assign an inner class of a script (i.e. using the `class` keyword in GDScript) won't work. Godot will not serialize the custom properties on the script inner class properly. In the example below, Godot would load the `Node` script, see that it doesn't extend `Resource`, and then determine that the script failed to load for the Resource object since the types are incompatible. ```csharp
using Godot;

public partial class MyNode : Node
{
    [GlobalClass]
    public partial class MyResource : Resource
    {
        [Export]
        public int Value { get; set; } = 5;
    }

    public override void _Ready()
    {
        var res = new MyResource();

        // This will NOT serialize the 'Value' property.
        ResourceSaver.Save(res, "res://MyRes.tres");
    }
}
````

---

## Using SceneTree

### Introduction

In previous tutorials, everything revolved around the concept of nodes. Scenes are collections of nodes. They become active once they enter the _scene tree_.

### MainLoop

The way Godot works internally is as follows. There is the [OS](../godot_csharp_core.md) class, which is the only instance that runs at the beginning. Afterwards, all drivers, servers, scripting languages, scene system, etc are loaded.

When initialization is complete, [OS](../godot_csharp_core.md) needs to be supplied a [MainLoop](../godot_csharp_core.md) to run. Up to this point, all this is internals working (you can check main/main.cpp file in the source code if you are ever interested to see how this works internally).

The user program, or game, starts in the MainLoop. This class has a few methods, for initialization, idle (frame-synchronized callback), fixed (physics-synchronized callback), and input. Again, this is low level and when making games in Godot, writing your own MainLoop seldom makes sense.

### SceneTree

One of the ways to explain how Godot works is that it's a high-level game engine over a low-level middleware.

The scene system is the game engine, while the [OS](../godot_csharp_core.md) and servers are the low-level API.

The scene system provides its own main loop to OS, [SceneTree](../godot_csharp_core.md). This is automatically instanced and set when running a scene, no need to do any extra work.

It's important to know that this class exists because it has a few important uses:

- It contains the root [Viewport](../godot_csharp_rendering.md), to which a scene is added as a child when it's first opened to become part of the _Scene Tree_ (more on that next).
- It contains information about the groups and has the means to call all nodes in a group or get a list of them.
- It contains some global state functionality, such as setting pause mode or quitting the process.

When a node is part of the Scene Tree, the [SceneTree](../godot_csharp_core.md) singleton can be obtained by calling [Node.get_tree()](../godot_csharp_misc.md).

### Root viewport

The root [Viewport](../godot_csharp_rendering.md) is always at the top of the scene. From a node, it can be obtained in two different ways:

```csharp
GetTree().Root // Access via scene main loop.
GetNode("/root"); // Access via absolute path.
```

This node contains the main viewport. Anything that is a child of a [Viewport](../godot_csharp_rendering.md) is drawn inside of it by default, so it makes sense that the top of all nodes is always a node of this type otherwise nothing would be seen.

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

After a scene is loaded, you may want to change this scene for another one. One way to do this is to use the [SceneTree.change_scene_to_file()](../godot_csharp_core.md) function:

```csharp
public void _MyLevelWasCompleted()
{
    GetTree().ChangeSceneToFile("res://levels/level2.tscn");
}
```

Rather than using file paths, one can also use ready-made [PackedScene](../godot_csharp_resources.md) resources using the equivalent function [SceneTree.change_scene_to_packed(PackedScene scene)](../godot_csharp_core.md):

```csharp
public void _MyLevelWasCompleted()
{
    var nextScene = (PackedScene)ResourceLoader.Load("res://levels/level2.tscn");
    GetTree().ChangeSceneToPacked(nextScene);
}
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

```csharp
GetNode<Button>("%RedButton").Text = "Hello";
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

[Node.find_child()](../godot_csharp_misc.md) finds a node by name without knowing its full path. This seems similar to a scene unique node, but this method is able to find nodes in nested scenes, and doesn't require marking the node in the scene editor in any way. However, this method is slow. Scene unique nodes are cached by Godot and are fast to retrieve, but each time the method is called, `find_child()` needs to check every descendant (every child, grandchild, and so on).

---

## Singletons (Autoload)

### Introduction

Godot's scene system, while powerful and flexible, has a drawback: there is no method for storing information (e.g. a player's score or inventory) that is needed by more than one scene.

It's possible to address this with some workarounds, but they come with their own limitations:

- You can use a "master" scene that loads and unloads other scenes as its children. However, this means you can no longer run those scenes individually and expect them to work correctly.
- Information can be stored to disk in `user://` and then loaded by scenes that require it, but frequently saving and loading data is cumbersome and may be slow.

The [Singleton pattern](https://en.wikipedia.org/wiki/Singleton_pattern) is a useful tool for solving the common use case where you need to store persistent information between scenes. In our case, it's possible to reuse the same scene or class for multiple singletons as long as they have different names.

Using this concept, you can create objects that:

- Are always loaded, no matter which scene is currently running.
- Can store global variables such as player information.
- Can handle switching scenes and between-scene transitions.
- _Act_ like a singleton, since GDScript does not support global variables by design.

Autoloading nodes and scripts can give us these characteristics.

> **Note:** Godot won't make an Autoload a "true" singleton as per the singleton design pattern. It may still be instanced more than once by the user if desired.

> **Tip:** If you're creating an autoload as part of an editor plugin, consider [registering it automatically in the Project Settings](tutorials_editor.md) when the plugin is enabled.

### Autoload

You can create an Autoload to load a scene or a script that inherits from [Node](../godot_csharp_core.md).

> **Note:** When autoloading a script, a [Node](../godot_csharp_core.md) will be created and the script will be attached to it. This node will be added to the root viewport before any other scenes are loaded.

To autoload a scene or script, start from the menu and navigate to **Project > Project Settings > Globals > Autoload**.

Here you can add any number of scenes or scripts. Each entry in the list requires a name, which is assigned as the node's `name` property. The order of the entries as they are added to the global scene tree can be manipulated using the up/down arrow keys. Like regular scenes, the engine will read these nodes in top-to-bottom order.

If the **Enable** column is checked (which is the default), then the singleton can be accessed directly in GDScript:

The **Enable** column has no effect in C# code. However, if the singleton is a C# script, a similar effect can be achieved by including a static property called `Instance` and assigning it in `_Ready()`:

```csharp
public partial class PlayerVariables : Node
{
    public static PlayerVariables Instance { get; private set; }

    public int Health { get; set; }

    public override void _Ready()
    {
        Instance = this;
    }
}
```

This allows the singleton to be accessed from C# code without `GetNode()` and without a typecast:

```csharp
PlayerVariables.Instance.Health -= 10;
```

Note that autoload objects (scripts and/or scenes) are accessed just like any other node in the scene tree. In fact, if you look at the running scene tree, you'll see the autoloaded nodes appear:

> **Warning:** Autoloads must **not** be removed using `free()` or `queue_free()` at runtime, or the engine will crash.

### Custom scene switcher

This tutorial will demonstrate building a scene switcher using autoloads. For basic scene switching, you can use the [SceneTree.change_scene_to_file()](../godot_csharp_core.md) method (see Using SceneTree for details). However, if you need more complex behavior when changing scenes, this method provides more functionality.

To begin, download the template from here: [singleton_autoload_starter.zip](https://github.com/godotengine/godot-docs-project-starters/releases/download/latest-4.x/singleton_autoload_starter.zip) and open it in Godot.

A window notifying you that the project was last opened in an older Godot version may appear, that's not an issue. Click _Ok_ to open the project.

The project contains two scenes: `scene_1.tscn` and `scene_2.tscn`. Each scene contains a label displaying the scene name and a button with its `pressed()` signal connected. When you run the project, it starts in `scene_1.tscn`. However, pressing the button does nothing.

#### Creating the script

Open the **Script** window and create a new script called `global.gd`. Make sure it inherits from `Node`:

The next step is to add this script to the autoload list. Starting from the menu, open **Project > Project Settings > Globals > Autoload** and select the script by clicking the browse button or typing its path: `res://global.gd`. Press **Add** to add it to the autoload list and name it "Global", which is required for scripts to access it by the name "Global":

Now whenever we run any scene in the project, this script will always be loaded.

Returning to the script, it needs to fetch the current scene in the \_ready() function. Both the current scene (the one with the button) and `global.gd` are children of root, but autoloaded nodes are always first. This means that the last child of root is always the loaded scene.

```csharp
using Godot;

public partial class Global : Node
{
    public Node CurrentScene { get; set; }

    public override void _Ready()
    {
        Viewport root = GetTree().Root;
        // Using a negative index counts from the end, so this gets the last child node of `root`.
        CurrentScene = root.GetChild(-1);
    }
}
```

Now we need a function for changing the scene. This function needs to free the current scene and replace it with the requested one.

```csharp
public void GotoScene(string path)
{
    // This function will usually be called from a signal callback,
    // or some other function from the current scene.
    // Deleting the current scene at this point is
    // a bad idea, because it may still be executing code.
    // This will result in a crash or unexpected behavior.

    // The solution is to defer the load to a later time, when
    // we can be sure that no code from the current scene is running:

    CallDeferred(MethodName.DeferredGotoScene, path);
}

public void DeferredGotoScene(string path)
{
    // It is now safe to remove the current scene.
    CurrentScene.Free();

    // Load a new scene.
    var nextScene = GD.Load<PackedScene>(path);

    // Instance the new scene.
    CurrentScene = nextScene.Instantiate();

    // A
// ...
```

Using [Object.call_deferred()](../godot_csharp_core.md), the second function will only run once all code from the current scene has completed. Thus, the current scene will not be removed while it is still being used (i.e. its code is still running).

Finally, we need to fill the empty callback functions in the two scenes:

```csharp
// Add to 'Scene1.cs'.

private void OnButtonPressed()
{
    var global = GetNode<Global>("/root/Global");
    global.GotoScene("res://Scene2.tscn");
}
```

and

```csharp
// Add to 'Scene2.cs'.

private void OnButtonPressed()
{
    var global = GetNode<Global>("/root/Global");
    global.GotoScene("res://Scene1.tscn");
}
```

Run the project and test that you can switch between scenes by pressing the button.

> **Note:** When scenes are small, the transition is instantaneous. However, if your scenes are more complex, they may take a noticeable amount of time to appear. To learn how to handle this, see the next tutorial: [Background loading](tutorials_io.md). Alternatively, if the loading time is relatively short (less than 3 seconds or so), you can display a "loading plaque" by showing some kind of 2D element just before changing the scene. You can then hide it just after the scene is changed. This can be used to indicate to the player that a scene is being loaded.

---
