# Godot 4 C# Tutorials — Scripting (Part 10)

> 11 tutorials. C#-specific code examples.

## Static typing in GDScript

In this guide, you will learn:

- how to use static typing in GDScript;
- that static types can help you avoid bugs;
- that static typing improves your experience with the editor.

Where and how you use this language feature is entirely up to you: you can use it only in some sensitive GDScript files, use it everywhere, or don't use it at all.

Static types can be used on variables, constants, functions, parameters, and return types.

### A brief look at static typing

With static typing, GDScript can detect more errors without even running the code. Also type hints give you and your teammates more information as you're working, as the arguments' types show up when you call a method. Static typing improves editor autocompletion and documentation of your scripts.

Imagine you're programming an inventory system. You code an `Item` class, then an `Inventory`. To add items to the inventory, the people who work with your code should always pass an `Item` to the `Inventory.add()` method. With types, you can enforce this:

Static types also give you better code completion options. Below, you can see the difference between a dynamic and a static typed completion options.

You've probably encountered a lack of autocomplete suggestions after a dot:

This is due to dynamic code. Godot cannot know what value type you're passing to the function. If you write the type explicitly however, you will get all methods, properties, constants, etc. from the value:

> **Tip:** If you prefer static typing, we recommend enabling the **Text Editor > Completion > Add Type Hints** editor setting. Also consider enabling **some warnings** that are disabled by default.

Also, typed GDScript improves performance by using optimized opcodes when operand/argument types are known at compile time. More GDScript optimizations are planned in the future, such as JIT/AOT compilation.

Overall, typed programming gives you a more structured experience. It helps prevent errors and improves the self-documenting aspect of your scripts. This is especially helpful when you're working in a team or on a long-term project: studies have shown that developers spend most of their time reading other people's code, or scripts they wrote in the past and forgot about. The clearer and the more structured the code, the faster it is to understand, the faster you can move forward.

### How to use static typing

To define the type of a variable, parameter, or constant, write a colon after the name, followed by its type. E.g. `var health: int`. This forces the variable's type to always stay the same:

Godot will try to infer types if you write a colon, but you omit the type:

> **Note:** 1. There is no difference between `=` and `:=` for constants. 2. You don't need to write type hints for constants, as Godot sets it automatically from the assigned value. But you can still do so to make the intent of your code clearer. Also, this is useful for typed arrays (like `const A: Array[int] = [1, 2, 3]`), since untyped arrays are used by default.

#### What can be a type hint

Here is a complete list of what can be used as a type hint:

1. `Variant`. Any type. In most cases this is not much different from an untyped declaration, but increases readability. As a return type, forces the function to explicitly return some value.
2. _(Only return type)_ `void`. Indicates that the function does not return any value.
3. Built-in types.
4. Native classes (`Object`, `Node`, `Area2D`, `Camera2D`, etc.).
5. Global classes.
6. Inner classes.
7. Global, native and custom named enums. Note that an enum type is just an `int`, there is no guarantee that the value belongs to the set of enum values.
8. Constants (including local ones) if they contain a preloaded class or enum.

You can use any class, including your custom classes, as types. There are two ways to use them in scripts. The first method is to preload the script you want to use as a type in a constant:

The second method is to use the `class_name` keyword when you create the script. For the example above, your `rifle.gd` would look like this:

If you use `class_name`, Godot registers the `Rifle` type globally in the editor, and you can use it anywhere, without having to preload it into a constant:

#### Specify the return type of a function with the arrow ->

To define the return type of a function, write a dash and a right angle bracket `->` after its declaration, followed by the return type:

The type `void` means the function does not return anything. You can use any type, as with variables:

You can also use your own classes as return types:

#### Covariance and contravariance

When inheriting base class methods, you should follow the [Liskov substitution principle](https://en.wikipedia.org/wiki/Liskov_substitution_principle).

**Covariance:** When you inherit a method, you can specify a return type that is more specific (**subtype**) than the parent method.

**Contravariance:** When you inherit a method, you can specify a parameter type that is less specific (**supertype**) than the parent method.

Example:

#### Specify the element type of an Array

To define the type of an `Array`, enclose the type name in `[]`.

An array's type applies to `for` loop variables, as well as some operators like `[]`, `[...] =` (assignment), and `+`. Array methods (such as `push_back`) and other operators (such as `==`) are still untyped. Built-in types, native and custom classes, and enums may be used as element types. Nested array types (like `Array[Array[int]]`) are not supported.

Since Godot 4.2, you can also specify a type for the loop variable in a `for` loop. For instance, you can write:

The array will remain untyped, but the `name` variable within the `for` loop will always be of `String` type.

#### Specify the element type of a Dictionary

To define the type of a `Dictionary`'s keys and values, enclose the type name in `[]` and separate the key and value type with a comma.

A dictionary's value type applies to `for` loop variables, as well as some operators like `[]` and `[...] =` (assignment). Dictionary methods that return values and other operators (such as `==`) are still untyped. Built-in types, native and custom classes, and enums may be used as element types. Nested typed collections (like `Dictionary[String, Dictionary[String, int]]`) are not supported.

#### Type casting

Type casting is an important concept in typed languages. Casting is the conversion of a value from one type to another.

Imagine an `Enemy` in your game, that `extends Area2D`. You want it to collide with the `Player`, a `CharacterBody2D` with a script called `PlayerController` attached to it. You use the `body_entered` signal to detect the collision. With typed code, the body you detect is going to be a generic `PhysicsBody2D`, and not your `PlayerController` on the `_on_body_entered` callback.

You can check if this `PhysicsBody2D` is your `Player` with the `as` keyword, and using the colon `:` again to force the variable to use this type. This forces the variable to stick to the `PlayerController` type:

As we're dealing with a custom type, if the `body` doesn't extend `PlayerController`, the `player` variable will be set to `null`. We can use this to check if the body is the player or not. We will also get full autocompletion on the player variable thanks to that cast.

> **Note:** The `as` keyword silently casts the variable to `null` in case of a type mismatch at runtime, without an error/warning. While this may be convenient in some cases, it can also lead to bugs. Use the `as` keyword only if this behavior is intended. A safer alternative is to use the `is` keyword: You can also simplify the code by using the `is not` operator: Alternatively, you can use the `assert()` statement:

> **Note:** If you try to cast with a built-in type and it fails, Godot will throw an error.

##### Safe lines

You can also use casting to ensure safe lines. Safe lines are a tool to tell you when ambiguous lines of code are type-safe. As you can mix and match typed and dynamic code, at times, Godot doesn't have enough information to know if an instruction will trigger an error or not at runtime.

This happens when you get a child node. Let's take a timer for example: with dynamic code, you can get the node with `$Timer`. GDScript supports [duck-typing](https://stackoverflow.com/a/4205163/8125343), so even if your timer is of type `Timer`, it is also a `Node` and an `Object`, two classes it extends. With dynamic GDScript, you also don't care about the node's type as long as it has the methods you need to call.

You can use casting to tell Godot the type you expect when you get a node: `($Timer as Timer)`, `($Player as CharacterBody2D)`, etc. Godot will ensure the type works and if so, the line number will turn green at the left of the script editor.

> **Note:** Safe lines do not always mean better or more reliable code. See the note above about the `as` keyword. For example: Even though `node_2` declaration is marked as an unsafe line, it is more reliable than `node_1` declaration. Because if you change the node type in the scene and accidentally forget to change it in the script, the error will be detected immediately when the scene is loaded. Unlike `node_1`, which will be silently cast to `null` and the error will be detected later.

> **Note:** You can turn off safe lines or change their color in the editor settings.

### Typed or dynamic: stick to one style

Typed GDScript and dynamic GDScript can coexist in the same project. But it's recommended to stick to either style for consistency in your codebase, and for your peers. It's easier for everyone to work together if you follow the same guidelines, and faster to read and understand other people's code.

Typed code takes a little more writing, but you get the benefits we discussed above. Here's an example of the same, empty script, in a dynamic style:

And with static typing:

As you can see, you can also use types with the engine's virtual methods. Signal callbacks, like any methods, can also use types. Here's a `body_entered` signal in a dynamic style:

And the same callback, with type hints:

### Warning system

> **Note:** Detailed documentation about the GDScript warning system has been moved to GDScript warning system.

Godot gives you warnings about your code as you write it. The engine identifies sections of your code that may lead to issues at runtime, but lets you decide whether or not you want to leave the code as it is.

We have a number of warnings aimed specifically at users of typed GDScript. By default, these warnings are disabled, you can enable them in Project Settings (**Debug > GDScript**, make sure **Advanced Settings** is enabled).

You can enable the `UNTYPED_DECLARATION` warning if you want to always use static types. Additionally, you can enable the `INFERRED_DECLARATION` warning if you prefer a more readable and reliable, but more verbose syntax.

`UNSAFE_*` warnings make unsafe operations more noticeable, than unsafe lines. Currently, `UNSAFE_*` warnings do not cover all cases that unsafe lines cover.

### Common unsafe operations and their safe counterparts

#### Global scope methods

The following global scope methods are not statically typed, but they have typed counterparts available. These methods return statically typed values:

| Method    | Statically typed equivalents                                                                                                                                                    |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| abs()     | absf(), absi() Vector2.abs(), Vector2i.abs() Vector3.abs(), Vector3i.abs() Vector4.abs(), Vector4i.abs()                                                                        |
| ceil()    | ceilf(), ceili() Vector2.ceil() Vector3.ceil() Vector4.ceil()                                                                                                                   |
| clamp()   | clampf(), clampi() Vector2.clamp(), Vector2i.clamp() Vector3.clamp(), Vector3i.clamp() Vector4.clamp(), Vector4i.clamp() Color.clamp() (untyped clamp() does not work on Color) |
| floor()   | floorf(), floori() Vector2.floor() Vector3.floor() Vector4.floor()                                                                                                              |
| lerp()    | lerpf() Vector2.lerp() Vector3.lerp() Vector4.lerp() Color.lerp() Quaternion.slerp() Basis.slerp() Transform2D.interpolate_with() Transform3D.interpolate_with()                |
| round()   | roundf(), roundi() Vector2.round() Vector3.round() Vector4.round()                                                                                                              |
| sign()    | signf() signi() Vector2.sign(), Vector2i.sign() Vector3.sign(), Vector3i.sign() Vector4.sign(), Vector4i.sign()                                                                 |
| snapped() | snappedf() snappedi() Vector2.snapped(), Vector2i.snapped() Vector3.snapped(), Vector3i.snapped() Vector4.snapped(), Vector4i.snapped()                                         |

When using static typing, use the typed global scope methods whenever possible. This ensures you have safe lines and benefit from typed instructions for better performance.

#### UNSAFE_PROPERTY_ACCESS and UNSAFE_METHOD_ACCESS warnings

In this example, we aim to set a property and call a method on an object that has a script attached with `class_name MyScript` and that `extends Node2D`. If we have a reference to the object as a `Node2D` (for instance, as it was passed to us by the physics system), we can first check if the property and method exist and then set and call them if they do:

However, this code will produce `UNSAFE_PROPERTY_ACCESS` and `UNSAFE_METHOD_ACCESS` warnings as the property and method are not present in the referenced type - in this case a `Node2D`. To make these operations safe, you can first check if the object is of type `MyScript` using the `is` keyword and then declare a variable with the type `MyScript` on which you can set its properties and call its methods:

Alternatively, you can declare a variable and use the `as` operator to try to cast the object. You'll then want to check whether the cast was successful by confirming that the variable was assigned:

#### UNSAFE_CAST warning

In this example, we would like the label connected to an object entering our collision area to show the area's name. Once the object enters the collision area, the physics system sends a signal with a `Node2D` object, and the most straightforward (but not statically typed) solution to do what we want could be achieved like this:

This piece of code produces an `UNSAFE_PROPERTY_ACCESS` warning because `label` is not defined in `Node2D`. To solve this, we could first check if the `label` property exist and cast it to type `Label` before settings its text property like so:

However, this produces an `UNSAFE_CAST` warning because `body.label` is of a `Variant` type. To safely get the property in the type you want, you can use the `Object.get()` method which returns the object as a `Variant` value or returns `null` if the property doesn't exist. You can then determine whether the property contains an object of the right type using the `is` keyword, and finally declare a statically typed variable with the object:

### Cases where you can't specify types

To wrap up this introduction, let's mention cases where you can't use type hints. This will trigger a **syntax error**.

1. You can't specify the type of individual elements in an array or a dictionary:

1. Nested types are not currently supported:

### Summary

Typed GDScript is a powerful tool. It helps you write more structured code, avoid common errors, and create scalable and reliable systems. Static types improve GDScript performance and more optimizations are planned for the future.

---

## GDScript warning system

The GDScript warning system complements static typing (but it can work without static typing too). It's here to help you avoid mistakes that are hard to spot during development, and that may lead to runtime errors.

You can configure warnings in the Project Settings under the section called **GDScript**:

> **Note:** You must enable **Advanced Settings** in order to see the GDScript section in the sidebar. You can also search for "GDScript" when Advanced Settings is off.

You can find a list of warnings for the active GDScript file in the script editor's status bar. The example below has 2 warnings:

To ignore single warnings within a file, use the `@warning_ignore` annotation. You can click on the ignore link to the left of the warning's description. Godot will add an annotation above the corresponding line and the code won't trigger the corresponding warning anymore:

To ignore multiple warnings in a region within a file, use the `@warning_ignore_start` and `@warning_ignore_restore` annotations. You can omit `@warning_ignore_restore` if you want to ignore the specified warning types until the end of the file.

Warnings won't prevent the game from running, but you can turn them into errors if you'd like. This way your game won't compile unless you fix all warnings. Head to the `GDScript` section of the Project Settings to turn on this option to the warning that you want. Here's the same file as the previous example with the warning `unused_variable` as an error turned on:

---

## Groups

Groups in Godot work like tags in other software. You can add a node to as many groups as you want. Then, in code, you can use the SceneTree to:

- Get a list of nodes in a group.
- Call a method on all nodes in a group.
- Send a notification to all nodes in a group.

This is a useful feature to organize large scenes and decouple code.

### Managing groups

Groups are created by adding a node to a new group name, and likewise they are removed by removing all nodes from a given group.

There are two ways to add/remove nodes to groups:

- During design, by using the Node dock in the editor, or the Global Groups in project settings.
- During execution, by calling [Node.add_to_group()](../godot_csharp_misc.md) or [Node.remove_from_group()](../godot_csharp_misc.md).

#### Using the Node dock

You can create new groups using the Groups tab in the Node dock.

Select a node in the Scene dock then click the add button with the + symbol.

You should now see the Create New Group modal appear. Write the group name in the field.

You can optionally mark the option "Global", which will make the group visible project-wide, and able to be reused in any project scene. This will also allow you to give it a description.

When done, press Ok to create it.

You should see the new groups appear in the Groups tab under Scene Groups if the Global option was unmarked, or under Global Groups if that option was marked.

A selected Node from the Scene dock can be added into groups by marking the checkbox on the left side of the groups in the Groups dock. The node you had selected when creating a new group will be automatically checked.

All groups present in the project that were marked as Global, created from any scene, will be visible under Global Groups.

Any other group derived from nodes in the current scene will appear under Scene Groups.

> **Warning:** The same underlying logic is used for both Global and Scene groups. Groups with the same name are considered one and the same. This feature is purely organizational.

You can manage Global Groups in the Global Groups dock, inside Project Settings. There, you will be able to add new global groups, or change existing groups' names and descriptions.

#### Using code

You can also manage groups from scripts. The following code adds the node to which you attach the script to the `guards` group as soon as it enters the scene tree.

```csharp
public override void _Ready()
{
    base._Ready();

    AddToGroup("guards");
}
```

Imagine you're creating an infiltration game. When an enemy spots the player, you want all guards and robots to be on alert.

In the fictional example below, we use `SceneTree.call_group()` to alert all enemies that the player was spotted.

```csharp
public void _OnPlayerDiscovered()
{
    GetTree().CallGroup("guards", "enter_alert_mode");
}
```

The above code calls the function `enter_alert_mode` on every member of the group `guards`.

To get the full list of nodes in the `guards` group as an array, you can call [SceneTree.get_nodes_in_group()](../godot_csharp_core.md):

```csharp
var guards = GetTree().GetNodesInGroup("guards");
```

The [SceneTree](../godot_csharp_core.md) class provides many more useful methods to interact with scenes, their node hierarchy, and groups. It allows you to switch scenes easily or reload them, quit the game or pause and unpause it. It also provides useful signals.

---

## How to read the Godot API

On this page, you'll learn how to read the class reference for the Godot API.

The API, or Application Programming Interface, is an index of what Godot offers users. It provides a brief summary of which classes exist, how they are related to each other, what features they have, and how to use them.

### Inheritance

At the top of each file, you will see the name of the class.

The "Inherits" section lists each class the current one inherits. Here `CanvasItem` inherits `Node` and `Node` inherits `Object`.

The "Inherited By" section lists each class which directly inherits the current class. Here `Control` and `Node2D` both inherit `CanvasItem`.

### Brief Description

Next a brief description of the class. This text appears in Godot Editor popups for creating Nodes, Resources, and other types.

### Description

Next a more detailed description the class, its features, and its use case(s).

Things you may find here:

1. Specifics of how the class works.
2. Code samples of common use cases.
3. Usage details which are shared between each of the class's methods.
4. Warnings about required dependencies or configuration.
5. Links to other related parts of the Godot API.

### Tutorials

The page then provides links to parts of the manual which mention or make use of the current class.

### Properties

The Properties table lists the variables which belong to each instance of the class, also known as the "properties."

The left column contains the data type of the property. The text is also a link to that data type's Godot API page.

The center column contains the name of the property. The text is also a link to that property's full description on the page. Use this name to get the property's data or set a new value to it.

The right column contains the default value of the property. To initialize it with a different value, you must set a different value via script or the Inspector.

### Methods

The Methods table lists the functions which belong to each instance of the class, also known as the "methods."

The left column contains the data type of the method's return value.

The right column contains the name, parameters, and qualifiers of the method. The name is the text before the opening parenthesis. It is also a link to the method's full description on the page. Use this name to call the method.

For each parameter, the page details its data type, name, and default value, if any.

Possible qualifiers include...

- `const`: the method does not change any data in the class instance.
- `virtual`: the method does nothing but wait for a script to override it.
- `vararg`: the method can accept an arbitrary number of arguments.

### Signals

The Signals list details the names and parameters of events which "signal" a change in game state to other class instances.

Like the Methods table, any parameters will include their data type and name.

Each signal also has a detailed explanation of when the signal is emitted.

### Enumerations

The Enumerations list details the enumerable data types associated with the current class.

For each enumeration, the page states its name and then lists its possible values.

For each enumeration value, the page states its name, its integer value, and an explanation of its use case(s) and/or affects.

### Constants

The Constants list details named integer constants in the current class.

For each constant, the page states its name, its integer value, and an explanation of its use case(s) and/or affects.

`NOTIFICATION_*` constants' descriptions will state which engine event triggers the notification.

### Property Descriptions

The Property Descriptions list details everything about each property.

It restates the data type and name of the property.

Every property in the Godot API is bound to a pair of setter and getter functions. Using either is equivalent. They are listed here.

Below that is a detailed summary of what the property's data represents, its use case(s) and/or the affects of changing it. It may include code samples and/or links to relevant parts of the Godot API.

> **Note:** Knowing the setter and getter names is useful when one must bind a method name or [Callable](../godot_csharp_misc.md) to something.

### Method Descriptions

The Method Descriptions list details everything about each method.

It restates the method's return data type, parameter names/types/defaults, and qualifiers.

Below that is a detailed summary of what the method does and its use case(s). It may include code samples and/or links to relevant parts of the Godot API.

---

## Idle and Physics Processing

Games run in a loop. Each frame, you need to update the state of your game world before drawing it on screen. Godot provides two virtual methods in the Node class to do so: [Node.\_process()](../godot_csharp_misc.md) and [Node.\_physics_process()](../godot_csharp_misc.md). If you define either or both in a script, the engine will call them automatically.

There are two types of processing available to you:

1. **Idle processing** allows you to run code that updates a node every frame, as often as possible.
2. **Physics processing** happens at a fixed rate, 60 times per second by default. This is independent of your game's actual framerate, and keeps physics running smoothly. You should use it for anything that involves the physics engine, like moving a body that collides with the environment.

You can activate idle processing by defining the `_process()` method in a script. You can turn it off and back on by calling [Node.set_process()](../godot_csharp_misc.md).

The engine calls this method every time it draws a frame:

```csharp
public override void _Process(double delta)
{
    // Do something...
}
```

Keep in mind that the frequency at which the engine calls `_process()` depends on your application's framerate, which varies over time and across devices.

The function's `delta` parameter is the time elapsed in seconds since the previous call to `_process()`. Use this parameter to make calculations independent of the framerate. For example, you should always multiply a speed value by `delta` to animate a moving object.

Physics processing works with a similar virtual function: `_physics_process()`. Use it for calculations that must happen before each physics step, like moving a character that collides with the game world. As mentioned above, `_physics_process()` runs at fixed time intervals as much as possible to keep the physics interactions stable. You can change the interval between physics steps in the Project Settings, under Physics -> Common -> Physics Fps. By default, it's set to run 60 times per second.

The engine calls this method before every physics step:

```csharp
public override void _PhysicsProcess(double delta)
{
    // Do something...
}
```

The function `_process()` is not synchronized with physics. Its rate depends on hardware and game optimization. It also runs after the physics step in single-threaded games.

You can see the `_process()` function at work by creating a scene with a single Label node, with the following script attached to it:

```csharp
using Godot;

public partial class CustomLabel : Label
{
    private double _time;

    public override void _Process(double delta)
    {
        _time += delta;
        Text = _time.ToString(); // 'Text' is a built-in Label property.
    }
}
```

When you run the scene, you should see a counter increasing each frame.

---

## Instancing with signals

Signals provide a way to decouple game objects, allowing you to avoid forcing a fixed arrangement of nodes. One sign that a signal might be called for is when you find yourself using `get_parent()`. Referring directly to a node's parent means that you can't easily move that node to another location in the scene tree. This can be especially problematic when you are instancing objects at runtime and may want to place them in an arbitrary location in the running scene tree.

Below we'll consider an example of such a situation: firing bullets.

### Shooting example

Consider a player character that can rotate and shoot towards the mouse. Every time the mouse button is clicked, we create an instance of the bullet at the player's location. See Creating instances (see Getting Started docs) for details.

We'll use an `Area2D` for the bullet, which moves in a straight line at a given velocity:

```csharp
using Godot;

public partial class Bullet : Area2D
{
    public Vector2 Velocity { get; set; } = Vector2.Right;

    public override void _PhysicsProcess(double delta)
    {
        Position += Velocity * (float)delta;
    }
}
```

However, if the bullets are added as children of the player, then they will remain "attached" to the player as it rotates:

Instead, we need the bullets to be independent of the player's movement - once fired, they should continue traveling in a straight line and the player can no longer affect them. Instead of being added to the scene tree as a child of the player, it makes more sense to add the bullet as a child of the "main" game scene, which may be the player's parent or even further up the tree.

You could do this by adding the bullet to the main scene directly:

```csharp
Node bulletInstance = Bullet.Instantiate();
GetParent().AddChild(bulletInstance);
```

However, this will lead to a different problem. Now if you try to test your "Player" scene independently, it will crash on shooting, because there is no parent node to access. This makes it a lot harder to test your player code independently and also means that if you decide to change your main scene's node structure, the player's parent may no longer be the appropriate node to receive the bullets.

The solution to this is to use a signal to "emit" the bullets from the player. The player then has no need to "know" what happens to the bullets after that - whatever node is connected to the signal can "receive" the bullets and take the appropriate action to spawn them.

Here is the code for the player using signals to emit the bullet:

```csharp
using Godot;

public partial class Player : Sprite2D
{
    [Signal]
    public delegate void ShootEventHandler(PackedScene bullet, float direction, Vector2 location);

    private PackedScene _bullet = GD.Load<PackedScene>("res://Bullet.tscn");

    public override void _Input(InputEvent @event)
    {
        if (@event is InputEventMouseButton mouseButton)
        {
            if (mouseButton.ButtonIndex == MouseButton.Left && mouseButton.Pressed)
            {
                EmitSignal(SignalName.Shoot, _bullet, Rotation, Position);
            }
        }
    }

    public override void _Process(double delta)
    {
        LookAt(GetGlobalMousePosition());
    }
}
```

In the main scene, we then connect the player's signal (it will appear in the "Node" tab of the Inspector)

```csharp
private void OnPlayerShoot(PackedScene bullet, float direction, Vector2 location)
{
    var spawnedBullet = bullet.Instantiate<Bullet>();
    AddChild(spawnedBullet);
    spawnedBullet.Rotation = direction;
    spawnedBullet.Position = location;
    spawnedBullet.Velocity = spawnedBullet.Velocity.Rotated(direction);
}
```

Now the bullets will maintain their own movement independent of the player's rotation:

---

## Logging

Godot comes with several ways to organize and collect log messages.

### Printing messages

> **See also:** See Printing messages for instructions on printing messages. The printed output is generally identical to the logged output. When running a project from the editor, the editor will display logged text in the Output panel.

### Project settings

There are several project settings to control logging behavior in Godot:

- **Application > Run > Disable stdout:** Disables logging to standard output entirely. This also affects what custom loggers receive. This can be controlled at runtime by setting [Engine.print_to_stdout](../godot_csharp_core.md).
- **Application > Run > Disable stderr:** Disables logging to standard error entirely. This also affects what custom loggers receive. This can be controlled at runtime by setting [Engine.print_error_messages](../godot_csharp_core.md).
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

This backtrace is also logged to the file for the current session, but it is **not** visible in the editor Output panel. Since the engine's scripting system is not running anymore when the engine is crashing, it is not possible to access it from scripting in the same session. However, you can still read the crash backtrace on the next session by loading log files and searching for the crash backtrace string (`Program crashed with signal`) using [FileAccess](../godot_csharp_filesystem.md). This allows you to access the backtrace information even after a crash, as long as the user restarts the project and file logging is enabled:

You can customize the message that appears at the top of the backtrace using the **Debug > Settings > Crash Handler > Message** project setting. This can be used to point to a URL or email address that users can report issues to.

### Creating custom loggers

Since Godot 4.5, it is possible to create custom loggers. This custom logging can be used for many purposes:

- Show an in-game console with the same messages as printed by the engine, without requiring other scripts to be modified.
- Report printed errors from the player's machine to a remote server. This can make it easier for developers to fix bugs when the game is already released, or during playtesting.
- Integrate a dedicated server export with monitoring platforms.

A custom logger can be registered by creating a class that inherits from [Logger](../godot_csharp_misc.md), then passing an instance of this class to [OS.add_logger](../godot_csharp_misc.md), in a script's [\_init()](../godot_csharp_misc.md) method. A good place to do this is an autoload.

The class must define two methods: [\_log_message()](../godot_csharp_misc.md) and [\_log_error()](../godot_csharp_misc.md).

Here is a minimal working example of a custom logger, with the script added as an autoload:

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

You can get a reference to a node by calling the [Node.get_node()](../godot_csharp_misc.md) method. For this to work, the child node must be present in the scene tree. Getting it in the parent node's `_ready()` function guarantees that.

If, for example, you have a scene tree like this, and you want to get a reference to the Sprite2D and Camera2D nodes to access them in your script.

To do so, you can use the following code.

```csharp
private Sprite2D _sprite2D;
private Camera2D _camera2D;

public override void _Ready()
{
    base._Ready();

    _sprite2D = GetNode<Sprite2D>("Sprite2D");
    _camera2D = GetNode<Camera2D>("Camera2D");
}
```

Note that you get nodes using their name, not their type. Above, "Sprite2D" and "Camera2D" are the nodes' names in the scene.

If you rename the Sprite2D node as Skin in the Scene dock, you have to change the line that gets the node to `get_node("Skin")` in the script.

### Node paths

When getting a reference to a node, you're not limited to getting a direct child. The `get_node()` function supports paths, a bit like when working with a file browser. Add a slash to separate nodes.

Take the following example scene, with the script attached to the UserInterface node.

To get the AnimationPlayer node, you would use the following code.

```csharp
private AnimationPlayer _animationPlayer;

public override void _Ready()
{
    base._Ready();

    _animationPlayer = GetNode<AnimationPlayer>("ShieldBar/AnimationPlayer");
}
```

> **Note:** As with file paths, you can use ".." to get a parent node. The best practice is to avoid doing that though not to break encapsulation. You can also start the path with a forward slash to make it absolute, in which case your topmost node would be "/root", the application's predefined root viewport.

#### Syntactic sugar

You can use two shorthands to shorten your code in GDScript. Firstly, putting the `@onready` annotation before a member variable makes it initialize right before the `_ready()` callback.

There is also a short notation for `get_node()`: the dollar sign, "$". You place it before the name or path of the node you want to get.

### Creating nodes

To create a node from code, call its `new()` method like for any other class-based datatype.

You can store the newly created node's reference in a variable and call `add_child()` to add it as a child of the node to which you attached the script.

```csharp
private Sprite2D _sprite2D;

public override void _Ready()
{
    base._Ready();

    _sprite2D = new Sprite2D(); // Create a new Sprite2D.
    AddChild(_sprite2D); // Add it as a child of this node.
}
```

To delete a node and free it from memory, you can call its `queue_free()` method. Doing so queues the node for deletion at the end of the current frame after it has finished processing. At that point, the engine removes the node from the scene and frees the object in memory.

```csharp
_sprite2D.QueueFree();
```

Before calling `sprite2d.queue_free()`, the remote scene tree looks like this.

After the engine freed the node, the remote scene tree doesn't display the sprite anymore.

You can alternatively call `free()` to immediately destroy the node. You should do this with care as any reference to it will instantly become `null`. We recommend using `queue_free()` unless you know what you're doing.

When you free a node, it also frees all its children. Thanks to this, to delete an entire branch of the scene tree, you only have to free the topmost parent node.

### Instancing scenes

Scenes are templates from which you can create as many reproductions as you'd like. This operation is called instancing, and doing it from code happens in two steps:

1. Loading the scene from the local drive.
2. Creating an instance of the loaded [PackedScene](../godot_csharp_resources.md) resource.

```csharp
var scene = GD.Load<PackedScene>("res://MyScene.tscn");
```

Preloading the scene can improve the user's experience as the load operation happens when the compiler reads the script and not at runtime. This feature is only available with GDScript.

At that point, `scene` is a packed scene resource, not a node. To create the actual node, you need to call [PackedScene.instantiate()](../godot_csharp_resources.md). It returns a tree of nodes that you can use as a child of your current node.

```csharp
var instance = scene.Instantiate();
AddChild(instance);
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

Another related callback is `_exit_tree()`, which the engine calls every time a node is about to exit the scene tree. This can be when you call [Node.remove_child()](../godot_csharp_misc.md) or when you free a node.

```csharp
// Called every time the node enters the scene tree.
public override void _EnterTree()
{
    base._EnterTree();
}

// Called when both the node and its children have entered the scene tree.
public override void _Ready()
{
    base._Ready();
}

// Called when the node is about to leave the scene tree, after all its
// children.
public override void _ExitTree()
{
    base._ExitTree();
}
```

The two virtual methods `_process()` and `_physics_process()` allow you to update the node, every frame and every physics frame respectively. For more information, read the dedicated documentation: Idle and Physics Processing.

```csharp
public override void _Process(double delta)
{
    // Called every frame.
    base._Process(delta);
}

public override void _PhysicsProcess(double delta)
{
    // Called every physics frame.
    base._PhysicsProcess(delta);
}
```

Two more essential built-in node callback functions are [Node.\_unhandled_input()](../godot_csharp_misc.md) and [Node.\_input()](../godot_csharp_misc.md), which you use to both receive and process individual input events. The `_unhandled_input()` method receives every key press, mouse click, etc. that have not been handled already in an `_input()` callback or in a user interface component. You want to use it for gameplay input in general. The `_input()` callback allows you to intercept and process input events before `_unhandled_input()` gets them.

To learn more about inputs in Godot, see the [Input section](tutorials_inputs.md).

```csharp
// Called once for every event.
public override void _UnhandledInput(InputEvent @event)
{
    base._UnhandledInput(@event);
}

// Called once for every event before _UnhandledInput(), allowing you to
// consume some events.
public override void _Input(InputEvent @event)
{
    base._Input(@event);
}
```

There are some more overridable functions like [Node.\_get_configuration_warnings()](../godot_csharp_misc.md). Specialized node types provide more callbacks like [CanvasItem.\_draw()](../godot_csharp_nodes_2d.md) to draw programmatically or [Control.\_gui_input()](../godot_csharp_ui_controls.md) to handle clicks and input on UI elements.

---

## Pausing games and process mode

### Introduction

In most games it is desirable to, at some point, interrupt the game to do something else, such as taking a break or changing options. Implementing a fine-grained control for what can be paused (and what cannot) is a lot of work, so a simple framework for pausing is provided in Godot.

### How pausing works

To pause the game the pause state must be set. This is done by assigning `true` to the [SceneTree.paused](../godot_csharp_core.md) property:

```csharp
GetTree().Paused = true;
```

Doing this will cause two things. First, 2D and 3D physics will be stopped for all nodes. Second, the behavior of certain nodes will stop or start depending on their process mode.

> **Note:** The physics servers can be made active while the game is paused by using their `set_active` methods.

### Process Modes

Each node in Godot has a "Process Mode" that defines when it processes. It can be found and changed under a node's [Node](../godot_csharp_core.md) properties in the inspector.

You can also alter the property with code:

```csharp
public override void _Ready()
{
    ProcessMode = Node.ProcessModeEnum.Pausable;
}
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

```csharp
private void OnPauseButtonPressed()
{
    GetTree().Paused = true;
    Show();
}
```

Finally, connect the menu's close button to a new method in the script. Inside that method, unpause the game and hide the pause menu.

```csharp
private void OnCloseButtonPressed()
{
    Hide();
    GetTree().Paused = false;
}
```

You should now have a working pause menu.

---
