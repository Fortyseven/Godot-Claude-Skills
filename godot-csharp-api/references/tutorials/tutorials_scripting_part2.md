# Godot 4 C# Tutorials — Scripting (Part 2)

> 8 tutorials. C#-specific code examples.

## C# exported properties

In Godot, class members can be exported. This means their value gets saved along with the resource (such as the [scene](../godot_csharp_misc.md)) they're attached to. They will also be available for editing in the property editor. Exporting is done by using the `[Export]` attribute.

```csharp
using Godot;

public partial class ExportExample : Node3D
{
    [Export]
    public int Number { get; set; } = 5;
}
```

In that example the value `5` will be saved, and after building the current project it will be visible in the property editor.

One of the fundamental benefits of exporting member variables is to have them visible and editable in the editor. This way, artists and game designers can modify values that later influence how the program runs. For this, a special export syntax is provided.

Exporting can only be done with Variant-compatible types.

> **Note:** Exporting properties can also be done in GDScript, for information on that see GDScript exported properties.

### Basic use

Exporting works with fields and properties. They can have any access modifier.

```csharp
[Export]
private int _number;

[Export]
public int Number { get; set; }
```

Exported members can specify a default value; otherwise, the [default value of the type](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/default-values) is used instead.

An `int` like `Number` defaults to `0`. `Text` defaults to null because `string` is a reference type.

```csharp
[Export]
public int Number { get; set; }

[Export]
public string Text { get; set; }
```

Default values can be specified for fields and properties.

```csharp
[Export]
private string _greeting = "Hello World";

[Export]
public string Greeting { get; set; } = "Hello World";
```

Properties with a backing field use the default value of the backing field.

```csharp
private int _number = 2;

[Export]
public int NumberWithBackingField
{
    get => _number;
    set => _number = value;
}
```

> **Note:** A property's `get` is not actually executed to determine the default value. Instead, Godot analyzes the C# source code. This works fine for most cases, such as the examples on this page. However, some properties are too complex for the analyzer to understand. For example, the following property attempts to use math to display the default value as `5` in the property editor, but it doesn't work: ```csharp
> [Export]
> public int NumberWithBackingField
> {

    get => _number + 3;
    set => _number = value - 3;

}

private int \_number = 2;
```The analyzer doesn't understand this code and falls back to the default value for`int`, `0`. However, when running the scene or inspecting a node with an attached tool script, `\_number`will be`2`, and `NumberWithBackingField`will return`5`. This difference may cause confusing behavior. To avoid this, don't use complex properties. Alternatively, if the default value can be explicitly specified, it can be overridden with the [\_PropertyCanRevert()](../godot_csharp_misc.md) and [\_PropertyGetRevert()](../godot_csharp_misc.md) methods.

Any type of `Resource` or `Node` can be exported. The property editor shows a user-friendly assignment dialog for these types. This can be used instead of `GD.Load` and `GetNode`. See **Nodes and Resources**.

```csharp
[Export]
public PackedScene PackedScene { get; set; }

[Export]
public RigidBody2D RigidBody2D { get; set; }
```

### Grouping exports

It is possible to group your exported properties inside the Inspector with the `[ExportGroup]` attribute. Every exported property after this attribute will be added to the group. Start a new group or use `[ExportGroup("")]` to break out.

```csharp
[ExportGroup("My Properties")]
[Export]
public int Number { get; set; } = 3;
```

The second argument of the attribute can be used to only group properties with the specified prefix.

Groups cannot be nested, use `[ExportSubgroup]` to create subgroups within a group.

```csharp
[ExportSubgroup("Extra Properties")]
[Export]
public string Text { get; set; } = "";
[Export]
public bool Flag { get; set; } = false;
```

You can also change the name of your main category, or create additional categories in the property list with the `[ExportCategory]` attribute.

```csharp
[ExportCategory("Main Category")]
[Export]
public int Number { get; set; } = 3;
[Export]
public string Text { get; set; } = "";

[ExportCategory("Extra Category")]
[Export]
public bool Flag { get; set; } = false;
```

> **Note:** The list of properties is organized based on the class inheritance, and new categories break that expectation. Use them carefully, especially when creating projects for public use.

### Strings as paths

Property hints can be used to export strings as paths

String as a path to a file.

```csharp
[Export(PropertyHint.File)]
public string GameFile { get; set; }
```

String as a path to a directory.

```csharp
[Export(PropertyHint.Dir)]
public string GameDirectory { get; set; }
```

String as a path to a file, custom filter provided as hint.

```csharp
[Export(PropertyHint.File, "*.txt,")]
public string GameFile { get; set; }
```

Using paths in the global filesystem is also possible, but only in scripts in tool mode.

String as a path to a PNG file in the global filesystem.

```csharp
[Export(PropertyHint.GlobalFile, "*.png")]
public string ToolImage { get; set; }
```

String as a path to a directory in the global filesystem.

```csharp
[Export(PropertyHint.GlobalDir)]
public string ToolDir { get; set; }
```

The multiline annotation tells the editor to show a large input field for editing over multiple lines.

```csharp
[Export(PropertyHint.MultilineText)]
public string Text { get; set; }
```

### Limiting editor input ranges

Using the range property hint allows you to limit what can be input as a value using the editor.

Allow integer values from 0 to 20.

```csharp
[Export(PropertyHint.Range, "0,20,")]
public int Number { get; set; }
```

Allow integer values from -10 to 20.

```csharp
[Export(PropertyHint.Range, "-10,20,")]
public int Number { get; set; }
```

Allow floats from -10 to 20 and snap the value to multiples of 0.2.

```csharp
[Export(PropertyHint.Range, "-10,20,0.2")]
public float Number { get; set; }
```

If you add the hints "or_greater" and/or "or_less" you can go above or below the limits when adjusting the value by typing it instead of using the slider.

```csharp
[Export(PropertyHint.Range, "0,100,1,or_greater,or_less")]
public int Number { get; set; }
```

### Floats with easing hint

Display a visual representation of the `ease` function when editing.

```csharp
[Export(PropertyHint.ExpEasing)]
public float TransitionSpeed { get; set; }
```

### Export with suffix hint

Display a unit hint suffix for exported variables. Works with numeric types, such as floats or vectors:

```csharp
[Export(PropertyHint.None, "suffix:m/s\u00b2")]
public float Gravity { get; set; } = 9.8f;
[Export(PropertyHint.None, "suffix:m/s")]
public Vector3 Velocity { get; set; }
```

In the above example, `\u00b2` is used to write the "squared" character (`²`).

### Colors

Regular color given as red-green-blue-alpha value.

```csharp
[Export]
public Color Color { get; set; }
```

Color given as red-green-blue value (alpha will always be 1).

```csharp
[Export(PropertyHint.ColorNoAlpha)]
public Color Color { get; set; }
```

### Nodes

Nodes can also be directly exported without having to use NodePaths.

```csharp
[Export]
public Node Node { get; set; }
```

A specific type of node can also be directly exported. The list of nodes shown after pressing "Assign" in the inspector is filtered to the specified type, and only a correct node can be assigned.

```csharp
[Export]
public Sprite2D Sprite2D { get; set; }
```

Custom node classes can also be exported directly. The filtering behavior depends on whether the custom class is a global class.

Exporting NodePaths like in Godot 3.x is still possible, in case you need it:

```csharp
[Export]
public NodePath NodePath { get; set; }

public override void _Ready()
{
    var node = GetNode(NodePath);
}
```

### Resources

```csharp
[Export]
public Resource Resource { get; set; }
```

In the Inspector, you can then drag and drop a resource file from the FileSystem dock into the variable slot.

Opening the inspector dropdown may result in an extremely long list of possible classes to create, however. Therefore, if you specify a type derived from Resource such as:

```csharp
[Export]
public AnimationNode AnimationNode { get; set; }
```

The drop-down menu will be limited to AnimationNode and all its derived classes. Custom resource classes can also be used, see C# global classes.

It must be noted that even if the script is not being run while in the editor, the exported properties are still editable. This can be used in conjunction with a script in "tool" mode.

### Exporting bit flags

Members whose type is an enum with the `[Flags]` attribute can be exported and their values are limited to the members of the enum type. The editor will create a widget in the Inspector, allowing to select none, one, or multiple of the enum members. The value will be stored as an integer.

A flags enum uses powers of 2 for the values of the enum members. Members that combine multiple flags using logical OR (`|`) are also possible.

```csharp
[Flags]
public enum SpellElements
{
    Fire = 1 << 1,
    Water = 1 << 2,
    Earth = 1 << 3,
    Wind = 1 << 4,

    FireAndWater = Fire | Water,
}

[Export]
public SpellElements MySpellElements { get; set; }
```

Integers used as bit flags can store multiple `true`/`false` (boolean) values in one property. By using the `Flags` property hint, any of the given flags can be set from the editor.

```csharp
[Export(PropertyHint.Flags, "Fire,Water,Earth,Wind")]
public int SpellElements { get; set; } = 0;
```

You must provide a string description for each flag. In this example, `Fire` has value 1, `Water` has value 2, `Earth` has value 4 and `Wind` corresponds to value 8. Usually, constants should be defined accordingly (e.g. `private const int ElementWind = 8` and so on).

You can add explicit values using a colon:

```csharp
[Export(PropertyHint.Flags, "Self:4,Allies:8,Foes:16")]
public int SpellTargets { get; set; } = 0;
```

Only power of 2 values are valid as bit flags options. The lowest allowed value is 1, as 0 means that nothing is selected. You can also add options that are a combination of other flags:

```csharp
[Export(PropertyHint.Flags, "Self:4,Allies:8,Self and Allies:12,Foes:16")]
public int SpellTargets { get; set; } = 0;
```

Export annotations are also provided for the physics and render layers defined in the project settings.

```csharp
[Export(PropertyHint.Layers2DPhysics)]
public uint Layers2DPhysics { get; set; }
[Export(PropertyHint.Layers2DRender)]
public uint Layers2DRender { get; set; }
[Export(PropertyHint.Layers3DPhysics)]
public uint Layers3DPhysics { get; set; }
[Export(PropertyHint.Layers3DRender)]
public uint Layers3DRender { get; set; }
```

Using bit flags requires some understanding of bitwise operations. If in doubt, use boolean variables instead.

### Exporting enums

Members whose type is an enum can be exported and their values are limited to the members of the enum type. The editor will create a widget in the Inspector, enumerating the following as "Thing 1", "Thing 2", "Another Thing". The value will be stored as an integer.

```csharp
public enum MyEnum
{
    Thing1,
    Thing2,
    AnotherThing = -1,
}

[Export]
public MyEnum MyEnumCurrent { get; set; }
```

Integer and string members can also be limited to a specific list of values using the `[Export]` annotation with the `PropertyHint.Enum` hint. The editor will create a widget in the Inspector, enumerating the following as Warrior, Magician, Thief. The value will be stored as an integer, corresponding to the index of the selected option (i.e. `0`, `1`, or `2`).

```csharp
[Export(PropertyHint.Enum, "Warrior,Magician,Thief")]
public int CharacterClass { get; set; }
```

You can add explicit values using a colon:

```csharp
[Export(PropertyHint.Enum, "Slow:30,Average:60,Very Fast:200")]
public int CharacterSpeed { get; set; }
```

If the type is `string`, the value will be stored as a string.

```csharp
[Export(PropertyHint.Enum, "Rebecca,Mary,Leah")]
public string CharacterName { get; set; }
```

If you want to set an initial value, you must specify it explicitly:

```csharp
[Export(PropertyHint.Enum, "Rebecca,Mary,Leah")]
public string CharacterName { get; set; } = "Rebecca";
```

### Exporting inspector buttons with [ExportToolButton]

If you want to create a clickable button in the inspector, you can use the `[ExportToolButton]` attribute. This exports a Callable property or field as a clickable button. Since this runs in the editor, usage of the [[Tool]](tutorials_plugins.md) attribute is required. When the button is pressed, the callable is called:

```csharp
[Tool]
public partial class MyNode : Node
{
    [ExportToolButton("Click me!")]
    public Callable ClickMeButton => Callable.From(ClickMe);

    public void ClickMe()
    {
        GD.Print("Hello world!");
    }
}
```

You can also set an icon for the button with a second argument. If specified, an icon will be fetched via [GetThemeIcon()](../godot_csharp_misc.md), from the `"EditorIcons"` theme type.

```csharp
[ExportToolButton("Click me!", Icon = "CharacterBody2D")]
public Callable ClickMeButton => Callable.From(ClickMe);
```

### Exporting collections

As explained in the C# Variant documentation, only certain C# arrays and the collection types defined in the `Godot.Collections` namespace are Variant-compatible, therefore, only those types can be exported.

#### Exporting Godot arrays

```csharp
[Export]
public Godot.Collections.Array Array { get; set; }
```

Using the generic `Godot.Collections.Array<T>` allows specifying the type of the array elements, which will be used as a hint for the editor. The Inspector will restrict the elements to the specified type.

```csharp
[Export]
public Godot.Collections.Array<string> Array { get; set; }
```

The default value of Godot arrays is null. A different default can be specified:

```csharp
[Export]
public Godot.Collections.Array<string> CharacterNames { get; set; } =
[
    "Rebecca",
    "Mary",
    "Leah",
];
```

Arrays with specified types which inherit from resource can be set by drag-and-dropping multiple files from the FileSystem dock.

```csharp
[Export]
public Godot.Collections.Array<Texture> Textures { get; set; }

[Export]
public Godot.Collections.Array<PackedScene> Scenes { get; set; }
```

#### Exporting Godot dictionaries

```csharp
[Export]
public Godot.Collections.Dictionary Dictionary { get; set; }
```

Using the generic `Godot.Collections.Dictionary<TKey, TValue>` allows specifying the types of the key and value elements of the dictionary.

```csharp
[Export]
public Godot.Collections.Dictionary<string, int> Dictionary { get; set; }
```

The default value of Godot dictionaries is null. A different default can be specified:

```csharp
[Export]
public Godot.Collections.Dictionary<string, int> CharacterLives { get; set; } = new Godot.Collections.Dictionary<string, int>
{
    ["Rebecca"] = 10,
    ["Mary"] = 42,
    ["Leah"] = 0,
};
```

#### Exporting C# arrays

C# arrays can exported as long as the element type is a Variant-compatible type.

```csharp
[Export]
public Vector3[] Vectors { get; set; }

[Export]
public NodePath[] NodePaths { get; set; }
```

The default value of C# arrays is null. A different default can be specified:

```csharp
[Export]
public Vector3[] Vectors { get; set; } =
[
    new Vector3(1, 2, 3),
    new Vector3(3, 2, 1),
];
```

### Setting exported variables from a tool script

When changing an exported variable's value from a script in Tool mode, the value in the inspector won't be updated automatically. To update it, call [NotifyPropertyListChanged()](../godot_csharp_misc.md) after setting the exported variable's value.

### Advanced exports

Not every type of export can be provided on the level of the language itself to avoid unnecessary design complexity. The following describes some more or less common exporting features which can be implemented with a low-level API.

Before reading further, you should get familiar with the way properties are handled and how they can be customized with [\_Set()](../godot_csharp_misc.md), [\_Get()](../godot_csharp_misc.md), and [\_GetPropertyList()](../godot_csharp_misc.md) methods as described in [Accessing data or logic from an object](tutorials_best_practices.md).

> **See also:** For binding properties using the above methods in C++, see Binding properties using \_set/\_get/\_get_property_list.

> **Warning:** The script must operate in the `tool` mode so the above methods can work from within the editor.

---

## C# language features

This page provides an overview of the commonly used features of both C# and Godot and how they are used together.

### Type conversion and casting

C# is a statically typed language. Therefore, you can't do the following:

```csharp
var mySprite = GetNode("MySprite");
mySprite.SetFrame(0);
```

The method `GetNode()` returns a `Node` instance. You must explicitly convert it to the desired derived type, `Sprite2D` in this case.

For this, you have various options in C#.

**Casting and Type Checking**

Throws `InvalidCastException` if the returned node cannot be cast to Sprite2D. You would use it instead of the `as` operator if you are pretty sure it won't fail.

```csharp
Sprite2D mySprite = (Sprite2D)GetNode("MySprite");
mySprite.SetFrame(0);
```

**Using the AS operator**

The `as` operator returns `null` if the node cannot be cast to Sprite2D, and for that reason, it cannot be used with value types.

```csharp
Sprite2D mySprite = GetNode("MySprite") as Sprite2D;
// Only call SetFrame() if mySprite is not null
mySprite?.SetFrame(0);
```

**Using the generic methods**

Generic methods are also provided to make this type conversion transparent.

`GetNode<T>()` casts the node before returning it. It will throw an `InvalidCastException` if the node cannot be cast to the desired type.

```csharp
Sprite2D mySprite = GetNode<Sprite2D>("MySprite");
mySprite.SetFrame(0);
```

`GetNodeOrNull<T>()` uses the `as` operator and will return `null` if the node cannot be cast to the desired type.

```csharp
Sprite2D mySprite = GetNodeOrNull<Sprite2D>("MySprite");
// Only call SetFrame() if mySprite is not null
mySprite?.SetFrame(0);
```

**Type checking using the IS operator**

To check if the node can be cast to Sprite2D, you can use the `is` operator. The `is` operator returns false if the node cannot be cast to Sprite2D, otherwise it returns true. Note that when the `is` operator is used against `null` the result is always going to be `false`.

```csharp
if (GetNode("MySprite") is Sprite2D)
{
    // Yup, it's a Sprite2D!
}

if (null is Sprite2D)
{
    // This block can never happen.
}
```

You can also declare a new variable to conditionally store the result of the cast if the `is` operator returns `true`.

```csharp
if (GetNode("MySprite") is Sprite2D mySprite)
{
    // The mySprite variable only exists inside this block, and it's never null.
    mySprite.SetFrame(0);
}
```

For more advanced type checking, you can look into [Pattern Matching](https://docs.microsoft.com/en-us/dotnet/csharp/pattern-matching).

### Preprocessor defines

Godot has a set of defines that allow you to change your C# code depending on the environment you are compiling to.

#### Examples

For example, you can change code based on the platform:

```csharp
public override void _Ready()
    {
#if (GODOT_MOBILE || GODOT_WEB)
        // Use simple objects when running on less powerful systems.
        SpawnSimpleObjects();
#else
        SpawnComplexObjects();
#endif
    }
```

Or you can detect which engine your code is in, useful for making cross-engine libraries:

```csharp
public void MyPlatformPrinter()
    {
#if GODOT
        GD.Print("This is Godot.");
#elif UNITY_5_3_OR_NEWER
        print("This is Unity.");
#else
        throw new NotSupportedException("Only Godot and Unity are supported.");
#endif
    }
```

Or you can write scripts that target multiple Godot versions and take advantage of features that are only available on some of those versions:

```csharp
public void UseCoolFeature()
    {
#if GODOT4_3_OR_GREATER || GODOT4_2_2_OR_GREATER
        // Use CoolFeature, that was added to Godot in 4.3 and cherry-picked into 4.2.2, here.
#else
        // Use a workaround for the absence of CoolFeature here.
#endif
    }
```

#### Full list of defines

- `GODOT` is always defined for Godot projects.
- `TOOLS` is defined when building with the Debug configuration (editor and editor player).
- `GODOT_REAL_T_IS_DOUBLE` is defined when the `GodotFloat64` property is set to `true`.
- One of `GODOT_LINUXBSD`, `GODOT_WINDOWS`, `GODOT_OSX`, `GODOT_ANDROID`, `GODOT_IOS`, `GODOT_WEB` depending on the OS. These names may change in the future. These are created from the `get_name()` method of the [OS](../godot_csharp_core.md) singleton, but not every possible OS the method returns is an OS that Godot with .NET runs on.
- `GODOTX`, `GODOTX_Y`, `GODOTX_Y_Z`, `GODOTx_OR_GREATER`, `GODOTX_y_OR_GREATER`, and `GODOTX_Y_z_OR_GREATER`, where `X`, `Y`, and `Z` are replaced by the current major, minor and patch version of Godot. `x`, `y`, and `z` are replaced by all values from 0 to the current version number for that component.

> **Note:** These defines were first added in Godot 4.0.4 and 4.1. Version defines for prior versions do not exist, regardless of the current Godot version.

For example: Godot 4.0.5 defines `GODOT4`, `GODOT4_OR_GREATER`, `GODOT4_0`, `GODOT4_0_OR_GREATER`, `GODOT4_0_5`, `GODOT4_0_4_OR_GREATER`, and `GODOT4_0_5_OR_GREATER`. Godot 4.3.2 defines `GODOT4`, `GODOT4_OR_GREATER`, `GODOT4_3`, `GODOT4_0_OR_GREATER`, `GODOT4_1_OR_GREATER`, `GODOT4_2_OR_GREATER`, `GODOT4_3_OR_GREATER`, `GODOT4_3_2`, `GODOT4_3_0_OR_GREATER`, `GODOT4_3_1_OR_GREATER`, and `GODOT4_3_2_OR_GREATER`.

When **exporting**, the following may also be defined depending on the export features:

- One of `GODOT_PC`, `GODOT_MOBILE`, or `GODOT_WEB` depending on the platform type.
- One of `GODOT_WINDOWS`, `GODOT_LINUXBSD`, `GODOT_MACOS`, `GODOT_ANDROID`, `GODOT_IOS`, or `GODOT_WEB` depending on the platform.

To see an example project, see the OS testing demo: [https://github.com/godotengine/godot-demo-projects/tree/master/misc/os_test](https://github.com/godotengine/godot-demo-projects/tree/master/misc/os_test)

---

## C# global classes

Global classes (also known as named scripts) are types registered in Godot's editor so they can be used more conveniently. In GDScript, this is achieved using the `class_name` keyword at the top of a script. This page describes how to achieve the same effect in C#.

- Global classes show up in the _Add Node_ and _Create Resource_ dialogs.
- If an exported property is a global class, the inspector restricts assignment, allowing only instances of that global class or any derived classes.

Global classes are registered with the `[GlobalClass]` attribute.

```csharp
using Godot;

[GlobalClass]
public partial class MyNode : Node
{
}
```

> **Warning:** The file name must match the class name in **case-sensitive** fashion. For example, a global class named "MyNode" must have a file name of `MyNode.cs`, not `myNode.cs`.

The `MyNode` type will be registered as a global class with the same name as the type's name.

The _Select a Node_ window for the `MyNode` exported property filters the list of nodes in the scene to match the assignment restriction.

```csharp
public partial class Main : Node
{
    [Export]
    public MyNode MyNode { get; set; }
}
```

If a custom type isn't registered as a global class, the assignment is restricted to the Godot type the custom type is based on. For example, inspector assignments to an export of the type `MySimpleSprite2D` are restricted to `Sprite2D` and derived types.

```csharp
public partial class MySimpleSprite2D : Sprite2D
{
}
```

When combined with the `[GlobalClass]` attribute, the `[Icon]` attribute allows providing a path to an icon to show when the class is displayed in the editor.

```csharp
using Godot;

[GlobalClass, Icon("res://Stats/StatsIcon.svg")]
public partial class Stats : Resource
{
    [Export]
    public int Strength { get; set; }

    [Export]
    public int Defense { get; set; }

    [Export]
    public int Speed { get; set; }
}
```

The `Stats` class is a custom resource registered as a global class. Exporting properties of the type `Stats` will only allow instances of this resource type to be assigned, and the inspector will let you create and load instances of this type easily.

> **Warning:** The Godot editor will hide these custom classes with names that begin with the prefix "Editor" in the "Create New Node" or "Create New Scene" dialog windows. The classes are available for instantiation at runtime via their class names, but are automatically hidden by the editor windows along with the built-in editor nodes used by the Godot editor.

---

## C# signals

For a detailed explanation of signals in general, see the Using signals (see Getting Started docs) section in the step by step tutorial.

Signals are implemented using C# events, the idiomatic way to represent the observer pattern (see Getting Started docs) in C#. This is the recommended way to use signals in C# and the focus of this page.

In some cases it's necessary to use the older [Connect()](../godot_csharp_misc.md) and [Disconnect()](../godot_csharp_misc.md) APIs. See **Using Connect and Disconnect** for more details.

If you encounter a `System.ObjectDisposedException` while handling a signal, you might be missing a signal disconnection. See **Disconnecting automatically when the receiver is freed** for more details.

### Signals as C# events

To provide more type-safety, Godot signals are also all available through [events](https://learn.microsoft.com/en-us/dotnet/csharp/events-overview). You can handle these events, as any other event, with the `+=` and `-=` operators.

```csharp
Timer myTimer = GetNode<Timer>("Timer");
myTimer.Timeout += () => GD.Print("Timeout!");
```

In addition, you can always access signal names associated with a node type through its nested `SignalName` class. This is useful when, for example, you want to await on a signal (see await keyword).

```csharp
await ToSignal(GetTree(), SceneTree.SignalName.ProcessFrame);
```

### Custom signals as C# events

To declare a custom event in your C# script, use the `[Signal]` attribute on a public delegate type. Note that the name of this delegate needs to end with `EventHandler`.

```csharp
[Signal]
public delegate void MySignalEventHandler();

[Signal]
public delegate void MySignalWithArgumentEventHandler(string myString);
```

Once this is done, Godot will create the appropriate events automatically behind the scenes. You can then use said events as you'd do for any other Godot signal. Note that events are named using your delegate's name minus the final `EventHandler` part.

```csharp
public override void _Ready()
{
    MySignal += () => GD.Print("Hello!");
    MySignalWithArgument += SayHelloTo;
}

private void SayHelloTo(string name)
{
    GD.Print($"Hello {name}!");
}
```

> **Warning:** If you want to connect to these signals in the editor, you will need to (re)build the project to see them appear. You can click the **Build** button in the upper-right corner of the editor to do so.

### Signal emission

To emit signals, use the `EmitSignal` method. Note that, as for signals defined by the engine, your custom signal names are listed under the nested `SignalName` class.

```csharp
public void MyMethodEmittingSignals()
{
    EmitSignal(SignalName.MySignal);
    EmitSignal(SignalName.MySignalWithArgument, "World");
}
```

In contrast with other C# events, you cannot use `Invoke` to raise events tied to Godot signals.

Signals support arguments of any Variant-compatible type.

Consequently, any `Node` or `RefCounted` will be compatible automatically, but custom data objects will need to inherit from `GodotObject` or one of its subclasses.

```csharp
using Godot;

public partial class DataObject : GodotObject
{
    public string MyFirstString { get; set; }
    public string MySecondString { get; set; }
}
```

### Bound values

Sometimes you'll want to bind values to a signal when the connection is established, rather than (or in addition to) when the signal is emitted. To do so, you can use an anonymous function like in the following example.

Here, the [Button.Pressed](../godot_csharp_ui_controls.md) signal does not take any argument. But we want to use the same `ModifyValue` for both the "plus" and "minus" buttons. So we bind the modifier value at the time we're connecting the signals.

```csharp
public int Value { get; private set; } = 1;

public override void _Ready()
{
    Button plusButton = GetNode<Button>("PlusButton");
    plusButton.Pressed += () => ModifyValue(1);

    Button minusButton = GetNode<Button>("MinusButton");
    minusButton.Pressed += () => ModifyValue(-1);
}

private void ModifyValue(int modifier)
{
    Value += modifier;
}
```

### Signal creation at runtime

Finally, you can create custom signals directly while your game is running. Use the `AddUserSignal` method for that. Be aware that it should be executed before any use of said signals (either connecting to them or emitting them). Also, note that signals created this way won't be visible through the `SignalName` nested class.

```csharp
public override void _Ready()
{
    AddUserSignal("MyCustomSignal");
    EmitSignal("MyCustomSignal");
}
```

### Using Connect and Disconnect

In general, it isn't recommended to use [Connect()](../godot_csharp_misc.md) and [Disconnect()](../godot_csharp_misc.md). These APIs don't provide as much type safety as the events. However, they're necessary for connecting to signals defined by GDScript and passing [ConnectFlags](../godot_csharp_misc.md).

In the following example, pressing the button for the first time prints `Greetings!`. `OneShot` disconnects the signal, so pressing the button again does nothing.

```csharp
public override void _Ready()
{
    Button button = GetNode<Button>("GreetButton");
    button.Connect(Button.SignalName.Pressed, Callable.From(OnButtonPressed), (uint)GodotObject.ConnectFlags.OneShot);
}

public void OnButtonPressed()
{
    GD.Print("Greetings!");
}
```

### Disconnecting automatically when the receiver is freed

Normally, when any `GodotObject` is freed (such as any `Node`), Godot automatically disconnects all connections associated with that object. This happens for both signal emitters and signal receivers.

For example, a node with this code will print "Hello!" when the button is pressed, then free itself. Freeing the node disconnects the signal, so pressing the button again doesn't do anything:

```csharp
public override void _Ready()
{
    Button myButton = GetNode<Button>("../MyButton");
    myButton.Pressed += SayHello;
}

private void SayHello()
{
    GD.Print("Hello!");
    Free();
}
```

When a signal receiver is freed while the signal emitter is still alive, in some cases automatic disconnection won't happen:

- The signal is connected to a lambda expression that captures a variable.
- The signal is a custom signal.

The following sections explain these cases in more detail and include suggestions for how to disconnect manually.

> **Note:** Automatic disconnection is totally reliable if a signal emitter is freed before any of its receivers are freed. With a project style that prefers this pattern, the above limits may not be a concern.

#### No automatic disconnection: a lambda expression that captures a variable

If you connect to a lambda expression that captures variables, Godot can't tell that the lambda is associated with the instance that created it. This causes this example to have potentially unexpected behavior:

```csharp
Timer myTimer = GetNode<Timer>("../Timer");
int x = 0;
myTimer.Timeout += () =>
{
    x++; // This lambda expression captures x.
    GD.Print($"Tick {x} my name is {Name}");
    if (x == 3)
    {
        GD.Print("Time's up!");
        Free();
    }
};
```

```text
Tick 1, my name is ExampleNode
Tick 2, my name is ExampleNode
Tick 3, my name is ExampleNode
Time's up!
[...] System.ObjectDisposedException: Cannot access a disposed object.
```

On tick 4, the lambda expression tries to access the `Name` property of the node, but the node has already been freed. This causes the exception.

To disconnect, keep a reference to the delegate created by the lambda expression and pass that to `-=`. For example, this node connects and disconnects using the `_EnterTree` and `_ExitTree` lifecycle methods:

```csharp
[Export]
public Timer MyTimer { get; set; }

private Action _tick;

public override void _EnterTree()
{
    int x = 0;
    _tick = () =>
    {
        x++;
        GD.Print($"Tick {x} my name is {Name}");
        if (x == 3)
        {
            GD.Print("Time's up!");
            Free();
        }
    };
    MyTimer.Timeout += _tick;
}

public override void _ExitTree()
{
    MyTimer.Timeout -= _tick;
}
```

In this example, `Free` causes the node to leave the tree, which calls `_ExitTree`. `_ExitTree` disconnects the signal, so `_tick` is never called again.

The lifecycle methods to use depend on what the node does. Another option is to connect to signals in `_Ready` and disconnect in `Dispose`.

> **Note:** Godot uses [Delegate.Target](https://learn.microsoft.com/en-us/dotnet/api/system.delegate.target) to determine what instance a delegate is associated with. When a lambda expression doesn't capture a variable, the generated delegate's `Target` is the instance that created the delegate. When a variable is captured, the `Target` instead points at a generated type that stores the captured variable. This is what breaks the association. If you want to see if a delegate will be automatically cleaned up, try checking its `Target`. `Callable.From` doesn't affect the `Delegate.Target`, so connecting a lambda that captures variables using `Connect` doesn't work any better than `+=`.

#### No automatic disconnection: a custom signal

Connecting to a custom signal using `+=` doesn't disconnect automatically when the receiving node is freed.

To disconnect, use `-=` at an appropriate time. For example:

```csharp
[Export]
public MyClass Target { get; set; }

public override void _EnterTree()
{
    Target.MySignal += OnMySignal;
}

public override void _ExitTree()
{
    Target.MySignal -= OnMySignal;
}
```

Another solution is to use `Connect`, which does disconnect automatically with custom signals:

```csharp
[Export]
public MyClass Target { get; set; }

public override void _EnterTree()
{
    Target.Connect(MyClass.SignalName.MySignal, Callable.From(OnMySignal));
}
```

---

## C# style guide

Having well-defined and consistent coding conventions is important for every project, and Godot is no exception to this rule.

This page contains a coding style guide, which is followed by developers of and contributors to Godot itself. As such, it is mainly intended for those who want to contribute to the project, but since the conventions and guidelines mentioned in this article are those most widely adopted by the users of the language, we encourage you to do the same, especially if you do not have such a guide yet.

> **Note:** This article is by no means an exhaustive guide on how to follow the standard coding conventions or best practices. If you feel unsure of an aspect which is not covered here, please refer to more comprehensive documentation, such as [C# Coding Conventions](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/inside-a-program/coding-conventions) or [Framework Design Guidelines](https://docs.microsoft.com/en-us/dotnet/standard/design-guidelines/naming-guidelines).

### Language specification

Godot currently uses **C# version 12.0** in its engine and example source code, as this is the version supported by .NET 8.0 (the current baseline requirement). So, before we move to a newer version, care must be taken to avoid mixing language features only available in C# 13.0 or later.

For detailed information on C# features in different versions, please see [What's New in C#](https://docs.microsoft.com/en-us/dotnet/csharp/whats-new/).

### Formatting

#### General guidelines

- Use line feed (**LF**) characters to break lines, not CRLF or CR.
- Use one line feed character at the end of each file, except for csproj files.
- Use **UTF-8** encoding without a [byte order mark](https://en.wikipedia.org/wiki/Byte_order_mark).
- Use **4 spaces** instead of tabs for indentation (which is referred to as "soft tabs").
- Consider breaking a line into several if it's longer than 100 characters.

#### Line breaks and blank lines

For a general indentation rule, follow [the "Allman Style"](https://en.wikipedia.org/wiki/Indentation_style#Allman_style) which recommends placing the brace associated with a control statement on the next line, indented to the same level:

```csharp
// Use this style:
if (x > 0)
{
    DoSomething();
}

// NOT this:
if (x > 0) {
    DoSomething();
}
```

However, you may choose to omit line breaks inside brackets:

- For simple property accessors.
- For simple object, array, or collection initializers.
- For abstract auto property, indexer, or event declarations.

```csharp
// You may put the brackets in a single line in following cases:
public interface MyInterface
{
    int MyProperty { get; set; }
}

public class MyClass : ParentClass
{
    public int Value
    {
        get { return 0; }
        set
        {
            ArrayValue = new [] {value};
        }
    }
}
```

Insert a blank line:

- After a list of `using` statements.
- Between method, properties, and inner type declarations.
- At the end of each file.

Field and constant declarations can be grouped together according to relevance. In that case, consider inserting a blank line between the groups for easier reading.

Avoid inserting a blank line:

- After `{`, the opening brace.
- Before `}`, the closing brace.
- After a comment block or a single-line comment.
- Adjacent to another blank line.

```csharp
using System;
using Godot;
                                          // Blank line after `using` list.
public class MyClass
{                                         // No blank line after `{`.
    public enum MyEnum
    {
        Value,
        AnotherValue                      // No blank line before `}`.
    }
                                          // Blank line around inner types.
    public const int SomeConstant = 1;
    public const int AnotherConstant = 2;

    private Vector3 _x;                  // Related constants or fields can be
    private Vector3 _y;                  // grouped together.

    private float _width;
    private float _height;

    public int MyProperty { get; set; }
                                          // Blank line around properties.
    public void
// ...
```

#### Using spaces

Insert a space:

- Around a binary and ternary operator.
- Between an opening parenthesis and `if`, `for`, `foreach`, `catch`, `while`, `lock` or `using` keywords.
- Before and within a single line accessor block.
- Between accessors in a single line accessor block.
- After a comma which is not at the end of a line.
- After a semicolon in a `for` statement.
- After a colon in a single line `case` statement.
- Around a colon in a type declaration.
- Around a lambda arrow.
- After a single-line comment symbol (`//`), and before it if used at the end of a line.
- After the opening brace, and before the closing brace in a single line initializer.

Do not use a space:

- After type cast parentheses.

The following example shows a proper use of spaces, according to some of the above mentioned conventions:

```csharp
public class MyClass<A, B> : Parent<A, B>
{
    public float MyProperty { get; set; }

    public float AnotherProperty
    {
        get { return MyProperty; }
    }

    public void MyMethod()
    {
        int[] values = { 1, 2, 3, 4 };
        int sum = 0;

        // Single line comment.
        for (int i = 0; i < values.Length; i++)
        {
            switch (i)
            {
                case 3: return;
                default:
                    sum += i > 2 ? 0 : 1;
                    break;
            }
        }

        i += (int)MyProperty; // No space after a type cast.
    }
}
```

### Naming conventions

Use **PascalCase** for all namespaces, type names and member level identifiers (i.e. methods, properties, constants, events), except for private fields:

```csharp
namespace ExampleProject
{
    public class PlayerCharacter
    {
        public const float DefaultSpeed = 10f;

        public float CurrentSpeed { get; set; }

        protected int HitPoints;

        private void CalculateWeaponDamage()
        {
        }
    }
}
```

Use **camelCase** for all other identifiers (i.e. local variables, method arguments), and use an underscore (`_`) as a prefix for private fields (but not for methods or properties, as explained above):

```csharp
private Vector3 _aimingAt; // Use an `_` prefix for private fields.

private void Attack(float attackStrength)
{
    Enemy targetFound = FindTarget(_aimingAt);

    targetFound?.Hit(attackStrength);
}
```

There's an exception with acronyms which consist of two letters, like `UI`, which should be written in uppercase letters where PascalCase would be expected, and in lowercase letters otherwise.

Note that `id` is **not** an acronym, so it should be treated as a normal identifier:

```csharp
public string Id { get; }

public UIManager UI
{
    get { return uiManager; }
}
```

It is generally discouraged to use a type name as a prefix of an identifier, like `string strText` or `float fPower`, for example. An exception is made, however, for interfaces, which **should**, in fact, have an uppercase letter `I` prefixed to their names, like `IInventoryHolder` or `IDamageable`.

Lastly, consider choosing descriptive names and do not try to shorten them too much if it affects readability.

For instance, if you want to write code to find a nearby enemy and hit it with a weapon, prefer:

```csharp
FindNearbyEnemy()?.Damage(weaponDamage);
```

Rather than:

```csharp
FindNode()?.Change(wpnDmg);
```

### Member variables

Don't declare member variables if they are only used locally in a method, as it makes the code more difficult to follow. Instead, declare them as local variables in the method's body.

### Local variables

Declare local variables as close as possible to their first use. This makes it easier to follow the code, without having to scroll too much to find where the variable was declared.

### Implicitly typed local variables

Consider using implicitly typing (`var`) for declaration of a local variable, but do so **only when the type is evident** from the right side of the assignment:

```csharp
// You can use `var` for these cases:

var direction = new Vector2(1, 0);

var value = (int)speed;

var text = "Some value";

for (var i = 0; i < 10; i++)
{
}

// But not for these:

var value = GetValue();

var velocity = direction * 1.5;

// It's generally a better idea to use explicit typing for numeric values, especially with
// the existence of the `real_t` alias in Godot, which can either be double or float
// depending on the build configuration.

var value = 1.5;
```

### Other considerations

- Use explicit access modifiers.
- Use properties instead of non-private fields.
- Use modifiers in this order: `public`/`protected`/`private`/`internal`/`virtual`/`override`/`abstract`/`new`/`static`/`readonly`.
- Avoid using fully-qualified names or `this.` prefix for members when it's not necessary.
- Remove unused `using` statements and unnecessary parentheses.
- Consider omitting the default initial value for a type.
- Consider using null-conditional operators or type initializers to make the code more compact.
- Use safe cast when there is a possibility of the value being a different type, and use direct cast otherwise.

---

## C# Variant

For a detailed explanation of Variant in general, see the [Variant](../godot_csharp_misc.md) documentation page.

`Godot.Variant` is used to represent Godot's native [Variant](../godot_csharp_misc.md) type. Any **Variant-compatible type** can be converted from/to it. We recommend avoiding `Godot.Variant` unless it is necessary to interact with untyped engine APIs. Take advantage of C#'s type safety when possible.

Converting from a Variant-compatible C# type to `Godot.Variant` can be done using implicit conversions. There are also `CreateFrom` method overloads and the generic `Variant.From<T>` methods. Only the syntax is different: the behavior is the same.

```csharp
int x = 42;
Variant numberVariant = x;
Variant helloVariant = "Hello, World!";

Variant numberVariant2 = Variant.CreateFrom(x);
Variant numberVariant3 = Variant.From(x);
```

Implicit conversions to `Godot.Variant` make passing variants as method arguments very convenient. For example, the third argument of [tween_property](../godot_csharp_misc.md) specifying the final color of the tween is a `Godot.Variant`.

```csharp
Tween tween = CreateTween();
tween.TweenProperty(GetNode("Sprite"), "modulate", Colors.Red, 1.0f);
```

Converting from `Godot.Variant` to a C# type can be done using explicit conversions. There are also `Variant.As{TYPE}` methods and the generic `Variant.As<T>` method. All of these behave the same.

```csharp
int number = (int)numberVariant;
string hello = (string)helloVariant;

int number2 = numberVariant.As<int>();
int number3 = numberVariant.AsInt32();
```

> **Note:** The `Variant.As{TYPE}` methods are typically named after C# types (`Int32`), not C# keywords (`int`).

If the Variant type doesn't match the conversion target type, the consequences vary depending on the source and target values.

- The conversion may examine the value and return a similar but potentially unexpected value of the target type. For example, the string `"42a"` may be converted to the integer `42`.
- The default value of the target type may be returned.
- An empty array may be returned.
- An exception may be thrown.

Converting to the correct type avoids complicated behavior and should be preferred.

The `Variant.Obj` property returns a C# `object` with the correct value for any variant. This may be useful when the type of Variant is completely unknown. However, when possible, prefer more specific conversions. `Variant.Obj` evaluates a `switch` on `Variant.VariantType` and it may not be necessary. Also, if the result is a value type, it is boxed.

For example, if the potential for `Variant.As<MyNode>()` to throw an invalid cast exception isn't acceptable, consider using a `Variant.As<GodotObject>() is MyNode n` type pattern instead.

> **Note:** Since the Variant type in C# is a struct, it can't be null. To create a "null" Variant, use the `default` keyword or the `Godot.Variant` parameterless constructor.

### Variant-compatible types

A Variant-compatible type can be converted to and from a `Godot.Variant`. These C# types are Variant-compatible:

- All the [built-in value types](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/built-in-types-table), except `decimal`, `nint` and `nuint`.
- `string`.
- Classes derived from [GodotObject](../godot_csharp_misc.md).
- Collections types defined in the `Godot.Collections` namespace.

Full list of Variant types and their equivalent C# type:

| Variant.Type       | C# Type                                        |
| ------------------ | ---------------------------------------------- |
| Nil                | null (Not a type)                              |
| Bool               | bool                                           |
| Int                | long (Godot stores 64-bit integers in Variant) |
| Float              | double (Godot stores 64-bit floats in Variant) |
| String             | string                                         |
| Vector2            | Godot.Vector2                                  |
| Vector2I           | Godot.Vector2I                                 |
| Rect2              | Godot.Rect2                                    |
| Rect2I             | Godot.Rect2I                                   |
| Vector3            | Godot.Vector3                                  |
| Vector3I           | Godot.Vector3I                                 |
| Transform2D        | Godot.Transform2D                              |
| Vector4            | Godot.Vector4                                  |
| Vector4I           | Godot.Vector4I                                 |
| Plane              | Godot.Plane                                    |
| Quaternion         | Godot.Quaternion                               |
| Aabb               | Godot.Aabb                                     |
| Basis              | Godot.Basis                                    |
| Transform3D        | Godot.Transform3D                              |
| Projection         | Godot.Projection                               |
| Color              | Godot.Color                                    |
| StringName         | Godot.StringName                               |
| NodePath           | Godot.NodePath                                 |
| Rid                | Godot.Rid                                      |
| Object             | Godot.GodotObject or any derived type.         |
| Callable           | Godot.Callable                                 |
| Signal             | Godot.Signal                                   |
| Dictionary         | Godot.Collections.Dictionary                   |
| Array              | Godot.Collections.Array                        |
| PackedByteArray    | byte[]                                         |
| PackedInt32Array   | int[]                                          |
| PackedInt64Array   | long[]                                         |
| PackedFloat32Array | float[]                                        |
| PackedFloat64Array | double[]                                       |
| PackedStringArray  | string[]                                       |
| PackedVector2Array | Godot.Vector2[]                                |
| PackedVector3Array | Godot.Vector3[]                                |
| PackedVector4Array | Godot.Vector4[]                                |
| PackedColorArray   | Godot.Color[]                                  |

> **Warning:** Godot uses 64-bit integers and floats in Variant. Smaller integer and float types such as `int`, `short` and `float` are supported since they can fit in the bigger type. Be aware that when a conversion is performed, using the wrong type will result in potential precision loss.

> **Warning:** Enums are supported by `Godot.Variant` since their underlying type is an integer type which are all compatible. However, implicit conversions don't exist, enums must be manually converted to their underlying integer type before they can converted to/from `Godot.Variant` or use the generic `Variant.As<T>` and `Variant.From<T>` methods to convert them. ```csharp
> enum MyEnum { A, B, C }

Variant variant1 = (int)MyEnum.A;
MyEnum enum1 = (MyEnum)(int)variant1;

Variant variant2 = Variant.From(MyEnum.A);
MyEnum enum2 = variant2.As<MyEnum>();

````



### Using Variant in a generic context



When using generics, you may be interested in restricting the generic `T` type to be only one of the Variant-compatible types. This can be achieved using the `[MustBeVariant]` attribute.


```csharp
public void MethodThatOnlySupportsVariants<[MustBeVariant] T>(T onlyVariant)
{
    // Do something with the Variant-compatible value.
}
````

Combined with the generic `Variant.From<T>` allows you to obtain an instance of `Godot.Variant` from an instance of a generic `T` type. Then it can be used in any API that only supports the `Godot.Variant` struct.

```csharp
public void Method1<[MustBeVariant] T>(T variantCompatible)
{
    Variant variant = Variant.From(variantCompatible);
    Method2(variant);
}

public void Method2(Variant variant)
{
    // Do something with variant.
}
```

In order to invoke a method with a generic parameter annotated with the `[MustBeVariant]` attribute, the value must be a Variant-compatible type or a generic `T` type annotated with the `[MustBeVariant]` attribute as well.

```csharp
public class ObjectDerivedClass : GodotObject { }

public class NonObjectDerivedClass { }

public void Main<[MustBeVariant] T1, T2>(T1 someGeneric1, T2 someGeneric2)
{
    MyMethod(42); // Works because `int` is a Variant-compatible type.
    MyMethod(new ObjectDerivedClass()); // Works because any type that derives from `GodotObject` is a Variant-compatible type.
    MyMethod(new NonObjectDerivedClass()); // Does NOT work because the type is not Variant-compatible.
    MyMethod(someGeneric1); // Works because `T1` is annotated with the `[MustBeVariant]` attribute.
    MyMethod(someGeneric2); // Does NOT work because `T2` is NOT annotated with the `[MustBeVariant]` attribute.
}

public void MyMethod<[MustBeVariant] T>(T variant)
{
    // Do something with variant.
}
```

---

## GD0001: Missing partial modifier on declaration of type that derives from GodotObject

|                                 |              |
| ------------------------------- | ------------ |
| Rule ID                         | GD0001       |
| Category                        | Usage        |
| Fix is breaking or non-breaking | Non-breaking |
| Enabled by default              | Yes          |

### Cause

A type that derives from `GodotObject` is not declared partial.

### Rule description

Godot source generators add generated code to user-defined types to implement the integration with the engine. Source generators can't add generated code to types that aren't declared partial.

```csharp
// The source generators can't enhance this type to work with Godot.
public class InvalidNode : Node { }

// The source generators can enhance this type to work with Godot.
public partial class ValidNode : Node { }
```

### How to fix violations

To fix a violation of this rule, add the `partial` keyword to the type declaration.

### When to suppress warnings

Do not suppress a warning from this rule. Types that derive from `GodotObject` but aren't partial can't be enhanced by the source generators, resulting in unexpected runtime errors.

---

## GD0002: Missing partial modifier on declaration of type which contains nested classes that derive from GodotObject

|                                 |              |
| ------------------------------- | ------------ |
| Rule ID                         | GD0002       |
| Category                        | Usage        |
| Fix is breaking or non-breaking | Non-breaking |
| Enabled by default              | Yes          |

### Cause

A type that derives from `GodotObject` is contained in a non-partial type declaration.

### Rule description

Godot source generators add generated code to user-defined types to implement the integration with the engine. Source generators can't add generated code to types that aren't declared partial.

```csharp
public class InvalidParentType
{
    // MyNode is contained in a non-partial type so the source generators
    // can't enhance this type to work with Godot.
    public partial class MyNode : Node { }
}

public partial class ValidParentType
{
    // MyNode is contained in a partial type so the source generators
    // can enhance this type to work with Godot.
    public partial class MyNode : Node { }
}
```

### How to fix violations

To fix a violation of this rule, add the `partial` keyword to the type declaration.

### When to suppress warnings

Do not suppress a warning from this rule. Types that derive from `GodotObject` but aren't partial can't be enhanced by the source generators, resulting in unexpected runtime errors.

---
