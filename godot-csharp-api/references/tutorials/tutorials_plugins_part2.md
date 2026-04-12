# Godot 4 C# Tutorials — Plugins (Part 2)

> 1 tutorials. C#-specific code examples.

## Running code in the editor

### What is @tool?

`@tool` is a powerful line of code that, when added at the top of your script, makes it execute in the editor. You can also decide which parts of the script execute in the editor, which in game, and which in both.

You can use it for doing many things, but it is mostly useful in level design for visually presenting things that are hard to predict ourselves. Here are some use cases:

- If you have a cannon that shoots cannonballs affected by physics (gravity), you can draw the cannonball's trajectory in the editor, making level design a lot easier.
- If you have jumppads with varying jump heights, you can draw the maximum jump height a player would reach if it jumped on one, also making level design easier.
- If your player doesn't use a sprite, but draws itself using code, you can make that drawing code execute in the editor to see your player.

> **Danger:** `@tool` scripts run inside the editor, and let you access the scene tree of the currently edited scene. This is a powerful feature which also comes with caveats, as the editor does not include protections for potential misuse of `@tool` scripts. Be **extremely** cautious when manipulating the scene tree, especially via [Node.queue_free](../godot_csharp_misc.md), as it can cause crashes if you free a node while the editor runs logic involving it.

### How to use @tool

To turn a script into a tool, add the `@tool` annotation at the top of your code.

To check if you are currently in the editor, use: `Engine.is_editor_hint()`.

For example, if you want to execute some code only in the editor, use:

```csharp
if (Engine.IsEditorHint())
{
    // Code to execute when in editor.
}
```

On the other hand, if you want to execute code only in game, simply negate the same statement:

```csharp
if (!Engine.IsEditorHint())
{
    // Code to execute when in game.
}
```

Pieces of code that do not have either of the 2 conditions above will run both in-editor and in-game.

Here is how a `_process()` function might look for you:

```csharp
public override void _Process(double delta)
{
    if (Engine.IsEditorHint())
    {
        // Code to execute in editor.
    }

    if (!Engine.IsEditorHint())
    {
        // Code to execute in game.
    }

    // Code to execute both in editor and in game.
}
```

### Important information

The general rule is that **any other GDScript that your tool script uses must _also_ be a tool**. The editor is not able to construct instances from GDScript files without `@tool`, which means you cannot call methods or reference member variables from them otherwise. However, since static methods, constants and enums can be used without creating an instance, it is possible to call them or reference them from a `@tool` script onto other non-tool scripts. One exception to this are [static variables](tutorials_scripting.md). If you try to read a static variable's value in a script that does not have `@tool`, it will always return `null` but won't print a warning or error when doing so. This restriction does not apply to static methods, which can be called regardless of whether the target script is in tool mode.

Extending a `@tool` script does not automatically make the extending script a `@tool`. Omitting `@tool` from the extending script will disable tool behavior from the super class. Therefore, the extending script should also specify the `@tool` annotation.

Modifications in the editor are permanent, with no undo/redo possible. For example, in the next section when we remove the script, the node will keep its rotation. Be careful to avoid making unwanted modifications. Consider setting up [version control](tutorials_best_practices.md) to avoid losing work in case you make a mistake.

### Debugging

While the debugger and breakpoints cannot be used directly with tool scripts, it is possible to launch a new instance of the editor and debug from there. To do this, navigate to **Debug > Customize Run Instances...** and specify --editor in **Main Run Args**.

See [Overview of debugging tools](tutorials_scripting.md) for more information.

Additionally, you can use print statements to display the contents of variables instead.

### Try @tool out

Add a `Sprite2D` node to your scene and set the texture to Godot icon. Attach and open a script, and change it to this:

```csharp
using Godot;

[Tool]
public partial class MySprite : Sprite2D
{
    public override void _Process(double delta)
    {
        Rotation += Mathf.Pi * (float)delta;
    }
}
```

Save the script and return to the editor. You should now see your object rotate. If you run the game, it will also rotate.

> **Warning:** You may need to restart the editor. This is a known bug found in all Godot 4 versions: [GH-66381](https://github.com/godotengine/godot/issues/66381).

> **Note:** If you don't see the changes, reload the scene (close it and open it again).

Now let's choose which code runs when. Modify your `_process()` function to look like this:

```csharp
public override void _Process(double delta)
{
    if (Engine.IsEditorHint())
    {
        Rotation += Mathf.Pi * (float)delta;
    }
    else
    {
        Rotation -= Mathf.Pi * (float)delta;
    }
}
```

Save the script. Now the object will spin clockwise in the editor, but if you run the game, it will spin counter-clockwise.

### Editing variables

Add and export a variable speed to the script. To update the speed and also reset the rotation angle add a setter `set(new_speed)` which is executed with the input from the inspector. Modify `_process()` to include the rotation speed.

```csharp
using Godot;

[Tool]
public partial class MySprite : Sprite2D
{
    private float _speed = 1;

    [Export]
    public float Speed
    {
        get => _speed;
        set
        {
            // Update speed and reset the rotation.
            _speed = value;
            Rotation = 0;
        }
    }

    public override void _Process(double delta)
    {
        Rotation += Mathf.Pi * (float)delta * _speed;
    }
}
```

> **Note:** Code from other nodes doesn't run in the editor. Your access to other nodes is limited. You can access the tree and nodes, and their default properties, but you can't access user variables. If you want to do so, other nodes have to run in the editor too.

### Getting notified when resources change

Sometimes you want your tool to use a resource. However, when you change a property of that resource in the editor, the `set()` method of your tool will not be called.

```csharp
using Godot;

[Tool]
public partial class MyTool : Node
{
    private MyResource _resource;

    [Export]
    public MyResource Resource
    {
        get => _resource;
        set
        {
            _resource = value;
            OnResourceSet();
        }
    }

    // This will only be called when you create, delete, or paste a resource.
    // You will not get an update when tweaking properties of it.
    private void OnResourceSet()
    {
        GD.Print("My resource was set!");
    }
}
```

To get around this problem you first have to make your resource a tool and make it emit the `changed` signal whenever a property is set:

```csharp
using Godot;

[Tool]
public partial class MyResource : Resource
{
    private float _property = 1;

    [Export]
    public float Property
    {
        get => _property;
        set
        {
            _property = value;
            // Emit a signal when the property is changed.
            EmitChanged();
        }
    }
}
```

You then want to connect the signal when a new resource is set:

```csharp
using Godot;

[Tool]
public partial class MyTool : Node
{
    private MyResource _resource;

    [Export]
    public MyResource Resource
    {
        get => _resource;
        set
        {
            _resource = value;
            // Connect the changed signal as soon as a new resource is being added.
            if (_resource != null)
            {
                _resource.Changed += OnResourceChanged;
            }
        }
    }

    private void OnResourceChanged()
    {
        GD.Print("My resource just changed!");
    }
}
```

Lastly, remember to disconnect the signal as the old resource being used and changed somewhere else would cause unneeded updates.

```csharp
[Export]
public MyResource Resource
{
    get => _resource;
    set
    {
        // Disconnect the signal if the previous resource was not null.
        if (_resource != null)
        {
            _resource.Changed -= OnResourceChanged;
        }
        _resource = value;
        if (_resource != null)
        {
            _resource.Changed += OnResourceChanged;
        }
    }
}
```

### Reporting node configuration warnings

Godot uses a _node configuration warning_ system to warn users about incorrectly configured nodes. When a node isn't configured correctly, a yellow warning sign appears next to the node's name in the Scene dock. When you hover or click on the icon, a warning message pops up. You can use this feature in your scripts to help you and your team avoid mistakes when setting up scenes.

When using node configuration warnings, when any value that should affect or remove the warning changes, you need to call [update_configuration_warnings](../godot_csharp_misc.md) . By default, the warning only updates when closing and reopening the scene.

### Running one-off scripts using EditorScript

Sometimes, you need to run code just one time to automate a certain task that is not available in the editor out of the box. Some examples might be:

- Use as a playground for GDScript or C# scripting without having to run a project. `print()` output is displayed in the editor Output panel.
- Scale all light nodes in the currently edited scene, as you noticed your level ends up looking too dark or too bright after placing lights where desired.
- Replace nodes that were copy-pasted with scene instances to make them easier to modify later.

This is available in Godot by extending [EditorScript](../godot_csharp_editor.md) in a script. This provides a way to run individual scripts in the editor without having to create an editor plugin.

To create an EditorScript, right-click a folder or empty space in the FileSystem dock then choose **New > Script...**. In the script creation dialog, click the tree icon to choose an object to extend from (or enter `EditorScript` directly in the field on the left, though note this is case-sensitive):

This will automatically select a script template that is suited for EditorScripts, with a `_run()` method already inserted:

This `_run()` method is executed when you use any of the 4 approaches that can be used to run an EditorScript:

- Use File > Run at the top of the script editor with the EditorScript being the current tab.
- Press the keyboard shortcut Ctrl + Shift + X while the EditorScript is the current tab. This keyboard shortcut is only effective when focused on the script editor.
- Right-click the script in the FileSystem dock and choose Run.
- Add a `class_name <name>` at the top of the script, bring up the command palette by pressing Ctrl + Shift + P, and enter the class name to run it. The entry will be named according to the class name, with automatic capitalization applied.

Scripts that extend EditorScript **must** be `@tool` scripts to function.

> **Note:** EditorScripts can only be run from the Godot script editor. If you are using an external editor, use one of the last two approaches to run the script.

> **Danger:** EditorScripts have no undo/redo functionality, so **make sure to save your scene before running one** if the script is designed to modify any data.

To access nodes in the currently edited scene, use the [EditorInterface.get_edited_scene_root()](../godot_csharp_editor.md) method which returns the root Node of the currently edited scene. Here's an example that recursively gets all nodes in the currently edited scene and doubles the range of all OmniLight3D nodes:

In the above example, we also call [EditorScript.mark_scene_as_unsaved()](../godot_csharp_editor.md) after any modification that affects the scene's state. This allows the editor to display the scene as "unsaved" (i.e. with an asterisk next to the name). This way, you also get a confirmation when trying to close the scene with unsaved changes.

> **Tip:** You can change the currently edited scene at the top of the editor even while the Script view is open. This will affect the return value of [EditorInterface.get_edited_scene_root](../godot_csharp_editor.md), so make sure you've selected the scene you intend to iterate upon before running the script.

### Instancing scenes

You can instantiate packed scenes normally and add them to the scene currently opened in the editor. By default, nodes or scenes added with [Node.add_child(node)](../godot_csharp_misc.md) are **not** visible in the Scene tree dock and are **not** persisted to disk. If you wish the node or scene to be visible in the scene tree dock and persisted to disk when saving the scene, you need to set the child node's [owner](../godot_csharp_misc.md) property to the currently edited scene root.

If you are using `@tool`:

```csharp
public override void _Ready()
{
    var node = new Node3D();
    AddChild(node); // Parent could be any node in the scene

    // The line below is required to make the node visible in the Scene tree dock
    // and persist changes made by the tool script to the saved scene file.
    node.Owner = GetTree().EditedSceneRoot;
}
```

If you are using [EditorScript](../godot_csharp_editor.md):

```csharp
public override void _Run()
{
    // `parent` could be any node in the scene.
    var parent = GetScene().GetNode("Parent");
    var node = new Node3D();
    parent.AddChild(node);

    // The line below is required to make the node visible in the Scene tree dock
    // and persist changes made by the tool script to the saved scene file.
    node.Owner = GetScene();
}
```

> **Warning:** Using `@tool` improperly can yield many errors. It is advised to first write the code how you want it, and only then add the `@tool` annotation to the top. Also, make sure to separate code that runs in-editor from code that runs in-game. This way, you can find bugs more easily.

---
