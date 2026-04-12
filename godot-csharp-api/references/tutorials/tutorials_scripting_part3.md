# Godot 4 C# Tutorials — Scripting (Part 3)

> 25 tutorials. C#-specific code examples.

## GD0003: Found multiple classes with the same name in the same script file

|                                 |              |
| ------------------------------- | ------------ |
| Rule ID                         | GD0003       |
| Category                        | Usage        |
| Fix is breaking or non-breaking | Non-breaking |
| Enabled by default              | Yes          |

### Cause

A script file contains multiple types that derives from `GodotObject` with a name that matches the script file. Only one type in the script file should match the file name.

### Rule description

Godot requires scripts to have a unique path so every type must be defined on its own file and the type name must match the file name.

```csharp
public partial class MyNode : Node { }

namespace DifferentNamespace
{
    // Invalid because there's already a type with the name MyNode in this file.
    public partial class MyNode : Node { }
}

// Invalid because there's already a type with the name MyNode in this file.
public partial class MyNode<T> : Node { }
```

### How to fix violations

To fix a violation of this rule, move each type declaration to a different file.

### When to suppress warnings

Do not suppress a warning from this rule. Types that derive from `GodotObject` must have a unique path otherwise the engine can't load the script by path, resulting in unexpected runtime errors.

---

## GD0101: The exported member is static

|                                 |                                                                                                 |
| ------------------------------- | ----------------------------------------------------------------------------------------------- |
| Rule ID                         | GD0101                                                                                          |
| Category                        | Usage                                                                                           |
| Fix is breaking or non-breaking | Breaking - If the static keyword is removed Non-breaking - If the [Export] attribute is removed |
| Enabled by default              | Yes                                                                                             |

### Cause

A static member is annotated with the `[Export]` attribute. Static members can't be exported.

### Rule description

Godot doesn't allow exporting static members.

```csharp
// Static members can't be exported.
[Export]
public static int InvalidProperty { get; set; }

// Instance members can be exported.
[Export]
public int ValidProperty { get; set; }
```

### How to fix violations

To fix a violation of this rule, remove the `[Export]` attribute or remove the `static` keyword.

### When to suppress warnings

Do not suppress a warning from this rule. Static members can't be exported so they will be ignored by Godot, resulting in runtime errors.

---

## GD0102: The type of the exported member is not supported

|                                 |                                                                                              |
| ------------------------------- | -------------------------------------------------------------------------------------------- |
| Rule ID                         | GD0102                                                                                       |
| Category                        | Usage                                                                                        |
| Fix is breaking or non-breaking | Breaking - If the member type is changed Non-breaking - If the [Export] attribute is removed |
| Enabled by default              | Yes                                                                                          |

### Cause

An unsupported type is specified for a member annotated with the `[Export]` attribute when a Variant-compatible type is expected.

### Rule description

Every exported member must be Variant-compatible so it can be marshalled by the engine.

```csharp
class SomeType { }

// SomeType is not a valid member type because it doesn't derive from GodotObject,
// so it's not compatible with Variant.
[Export]
public SomeType InvalidProperty { get; set; }

// System.Int32 is a valid type because it's compatible with Variant.
[Export]
public int ValidProperty { get; set; }
```

### How to fix violations

To fix a violation of this rule, change the member's type to be Variant-compatible or remove the `[Export]` attribute.

### When to suppress warnings

Do not suppress a warning from this rule. Members with types that can't be marshalled will result in runtime errors.

---

## GD0103: The exported member is read-only

|                                 |              |
| ------------------------------- | ------------ |
| Rule ID                         | GD0103       |
| Category                        | Usage        |
| Fix is breaking or non-breaking | Non-breaking |
| Enabled by default              | Yes          |

### Cause

A read-only member is annotated with the `[Export]` attribute. Read-only members can't be exported.

### Rule description

Godot doesn't allow exporting read-only members.

```csharp
// Read-only fields can't be exported.
[Export]
public readonly int invalidField;

// This field can be exported because it's not declared 'readonly'.
[Export]
public int validField;

// Read-only properties can't be exported.
[Export]
public int InvalidProperty { get; }

// This property can be exported because it has both a getter and a setter.
[Export]
public int ValidProperty { get; set; }
```

### How to fix violations

To fix a violation of this rule for fields, remove the `readonly` keyword or remove the `[Export]` attribute.

To fix a violation of this rule for properties, make sure the property declares both a getter and a setter, or remove the `[Export]` attribute.

### When to suppress warnings

Do not suppress a warning from this rule. Read-only members can't be exported so they will be ignored by Godot, resulting in runtime errors.

---

## GD0104: The exported property is write-only

|                                 |              |
| ------------------------------- | ------------ |
| Rule ID                         | GD0104       |
| Category                        | Usage        |
| Fix is breaking or non-breaking | Non-breaking |
| Enabled by default              | Yes          |

### Cause

A write-only property is annotated with the `[Export]` attribute. Write-only properties can't be exported.

### Rule description

Godot doesn't allow exporting write-only properties.

```csharp
private int _backingField;

// Write-only properties can't be exported.
[Export]
public int InvalidProperty { set => _backingField = value; }

// This property can be exported because it has both a getter and a setter.
[Export]
public int ValidProperty { get; set; }
```

### How to fix violations

To fix a violation of this rule, make sure the property declares both a getter and a setter, or remove the `[Export]` attribute.

### When to suppress warnings

Do not suppress a warning from this rule. Write-only members can't be exported so they will be ignored by Godot, resulting in runtime errors.

---

## GD0105: The exported property is an indexer

|                                 |              |
| ------------------------------- | ------------ |
| Rule ID                         | GD0105       |
| Category                        | Usage        |
| Fix is breaking or non-breaking | Non-breaking |
| Enabled by default              | Yes          |

### Cause

An indexer is annotated with the `[Export]` attribute. Indexers can't be exported.

### Rule description

Godot doesn't allow exporting indexer properties.

```csharp
private int[] _backingField;

// Indexers can't be exported.
[Export]
public int this[int index]
{
    get => _backingField[index];
    set => _backingField[index] = value;
}
```

### How to fix violations

To fix a violation of this rule, remove the `[Export]` attribute.

### When to suppress warnings

Do not suppress a warning from this rule. Indexers can't be exported so they will be ignored by Godot, resulting in runtime errors.

---

## GD0106: The exported property is an explicit interface implementation

|                                 |              |
| ------------------------------- | ------------ |
| Rule ID                         | GD0106       |
| Category                        | Usage        |
| Fix is breaking or non-breaking | Non-breaking |
| Enabled by default              | Yes          |

### Cause

An explicit interface property implementation is annotated with the `[Export]` attribute. Properties that implement an interface explicitly can't be exported.

### Rule description

Godot doesn't allow exporting explicit interface property implementations. When an interface member is implemented explicitly, the member is hidden and consumers can't access them unless the type is converted to the interface first. Explicitly implemented members can also share the same name of other members in the type, so it could create naming conflicts with other exported members.

```csharp
public interface MyInterface
{
    public int MyProperty { get; set; }
}

public class MyNode1 : Node, MyInterface
{
    // The property can be exported because it implements the interface implicitly.
    [Export]
    public int MyProperty { get; set; }
}

public class MyNode2 : Node, MyInterface
{
    // The property can't be exported because it implements the interface explicitly.
    [Export]
    int MyInterface.MyProperty { get; set; }
}
```

### How to fix violations

To fix a violation of this rule, implement the interface implicitly or remove the `[Export]` attribute.

### When to suppress warnings

Do not suppress a warning from this rule. Explicit interface property implementations can't be exported so they will be ignored by Godot, resulting in runtime errors.

---

## GD0107: Types not derived from Node should not export Node members

|                                 |          |
| ------------------------------- | -------- |
| Rule ID                         | GD0107   |
| Category                        | Usage    |
| Fix is breaking or non-breaking | Breaking |
| Enabled by default              | Yes      |

### Cause

A type that doesn't derive from `Node` contains an exported field or property of a type that derives from `Node`.

### Rule description

Exported nodes are serialized as `NodePath`. Only types derived from `Node` are able to get the node instance from the `NodePath`.

### How to fix violations

To fix a violation of this rule, avoid exporting `Node` members on a type that doesn't derive from `Node`, or consider exporting a `NodePath`.

### When to suppress warnings

Do not suppress a warning from this rule. Types that don't derive from `Node` will be unable to retrieve the right node instance for exported `Node` members, resulting in unexpected runtime errors.

---

## GD0108: The exported tool button is not in a tool class

|                                 |              |
| ------------------------------- | ------------ |
| Rule ID                         | GD0108       |
| Category                        | Usage        |
| Fix is breaking or non-breaking | Non-breaking |
| Enabled by default              | Yes          |

### Cause

A property is annotated with the `[ExportToolButton]` attribute in a class that is **not** annotated with the `[Tool]` attribute.

### Rule description

The `[ExportToolButton]` is used to create clickable buttons in the inspector so, like every other script that runs in the editor, it needs to be annotated with the `[Tool]` attribute.

```csharp
[Tool]
public partial class MyNode : Node
{
    [ExportToolButton("Click me!")]
    public Callable ClickMeButton => Callable.From(ClickMe);

    private static void ClickMe()
    {
        GD.Print("Hello world!");
    }
}
```

### How to fix violations

To fix a violation of this rule, add the `[Tool]` attribute to the class that contains the member annotated with the `[ExportToolButton]` attribute.

### When to suppress warnings

Do not suppress a warning from this rule. The clickable buttons in the inspector won't be functional if their script is not annotated with the `[Tool]` attribute.

---

## GD0109: The '[ExportToolButton]' attribute cannot be used with another '[Export]' attribute

|                                 |              |
| ------------------------------- | ------------ |
| Rule ID                         | GD0109       |
| Category                        | Usage        |
| Fix is breaking or non-breaking | Non-breaking |
| Enabled by default              | Yes          |

### Cause

A property is annotated with both the `[ExportToolButton]` and the `[Export]` attributes.

### Rule description

The `[ExportToolButton]` attribute already implies exporting the member, so the `[Export]` is unnecessary.

### How to fix violations

To fix a violation of this rule, remove the `[Export]` attribute.

### When to suppress warnings

Do not suppress a warning from this rule. Multiple export attributes may lead to duplicated members, resulting in unexpected runtime errors.

---

## GD0110: The exported tool button is not a Callable

|                                 |                                                                                                                             |
| ------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| Rule ID                         | GD0110                                                                                                                      |
| Category                        | Usage                                                                                                                       |
| Fix is breaking or non-breaking | Breaking - If the property's type is changed to Callable Non-breaking - If the [ExportToolButton] is replaced with [Export] |
| Enabled by default              | Yes                                                                                                                         |

### Cause

A property of a type different from `Callable` is annotated with the `[ExportToolButton]` attribute.

### Rule description

The `[ExportToolButton]` attribute is used to create clickable buttons in the inspector so, the property must be a `Callable` that will be executed when clicking the button.

### How to fix violations

To fix a violation of this rule, change the type of the property to `Callable`. Alternatively, if you intended to export a normal property, replace the `[ExportToolButton]` attribute with `[Export]`.

### When to suppress warnings

Do not suppress a warning from this rule. The exported property must be a `Callable` so it can executed in the editor when clicking the button in the inspector.

---

## GD0111: The exported tool button must be an expression-bodied property

|                                 |              |
| ------------------------------- | ------------ |
| Rule ID                         | GD0111       |
| Category                        | Usage        |
| Fix is breaking or non-breaking | Non-breaking |
| Enabled by default              | Yes          |

### Cause

A property is annotated with the `[ExportToolButton]` attribute but it's not an [expression-bodied property](https://learn.microsoft.com/en-us/dotnet/csharp/programming-guide/statements-expressions-operators/expression-bodied-members#properties).

### Rule description

When reloading the .NET assembly, Godot will attempt to serialize exported members to preserve their values. A field or a property with a backing field that stores a `Callable` may prevent the unloading of the assembly.

An expression-bodied property doesn't have a backing field and won't store the `Callable`, so Godot won't attempt to serialize it, which should result in the successful reloading of the .NET assembly.

```csharp
[ExportToolButton("Click me!")]
public Callable ValidClickMeButton => Callable.From(ClickMe);

// Invalid because the Callable will be stored in the property's backing field.
[ExportToolButton("Click me!")]
public Callable InvalidClickMeButton { get; } = Callable.From(ClickMe);
```

### How to fix violations

To fix a violation of this rule, replace the property implementation with an [expression-bodied property](https://learn.microsoft.com/en-us/dotnet/csharp/programming-guide/statements-expressions-operators/expression-bodied-members#properties).

### When to suppress warnings

Do not suppress a warning from this rule. `Callable` instances may prevent the .NET assembly from unloading.

---

## GD0201: The name of the delegate must end with 'EventHandler'

|                                 |          |
| ------------------------------- | -------- |
| Rule ID                         | GD0201   |
| Category                        | Usage    |
| Fix is breaking or non-breaking | Breaking |
| Enabled by default              | Yes      |

### Cause

A delegate annotated with the `[Signal]` attribute has a name that doesn't end with 'EventHandler'.

### Rule description

Godot source generators will generate C# events using the name of the delegate with the 'EventHandler' suffix removed. Adding the 'EventHandler' suffix to the name of delegates used in events is a [.NET naming convention](https://learn.microsoft.com/en-us/dotnet/standard/design-guidelines/names-of-classes-structs-and-interfaces#names-of-common-types).

Using a suffix for the delegate allows the generated event to use the name without the suffix avoiding a naming conflict.

```csharp
// This delegate is invalid since the name doesn't end with 'EventHandler'.
[Signal]
public void InvalidSignal();

// This delegate is valid since the name ends with 'EventHandler'.
[Signal]
public void ValidSignalEventHandler();
```

Take a look at the C# signals documentation for more information about how to declare and use signals.

### How to fix violations

To fix a violation of this rule, add 'EventHandler' to the end of the delegate name.

### When to suppress warnings

Do not suppress a warning from this rule. Signal delegates without the suffix will be ignored by the source generator, so the signal won't be registered.

---

## GD0202: The parameter of the delegate signature of the signal is not supported

|                                 |                                                                                                 |
| ------------------------------- | ----------------------------------------------------------------------------------------------- |
| Rule ID                         | GD0202                                                                                          |
| Category                        | Usage                                                                                           |
| Fix is breaking or non-breaking | Breaking - If the parameter type is changed Non-breaking - If the [Signal] attribute is removed |
| Enabled by default              | Yes                                                                                             |

### Cause

An unsupported type is specified for a parameter of a delegate annotated with the `[Signal]` attribute when a Variant-compatible type is expected.

### Rule description

Every signal parameter must be Variant-compatible so it can be marshalled when emitting the signal and invoking the callbacks.

```csharp
class SomeType { }

// SomeType is not a valid parameter type because it doesn't derive from GodotObject,
// so it's not compatible with Variant.
public void InvalidSignalEventHandler(SomeType someType);

// System.Int32 is a valid type because it's compatible with Variant.
public void ValidSignalEventHandler(int someInt);
```

Take a look at the C# signals documentation for more information about how to declare and use signals.

### How to fix violations

To fix a violation of this rule, change the parameter type to be Variant-compatible or remove the `[Signal]` attribute from the delegate. Note that removing the attribute will mean the signal is not registered.

> **Tip:** If the signal doesn't need to interact with Godot, consider using [C# events](https://learn.microsoft.com/en-us/dotnet/csharp/programming-guide/events/) directly. Pure C# events allow you to use any C# type for its parameters.

### When to suppress warnings

Do not suppress a warning from this rule. Signal delegates with parameters that can't be marshalled will result in runtime errors when emitting the signal or invoking the callbacks.

---

## GD0203: The delegate signature of the signal must return void

|                                 |                                                                                              |
| ------------------------------- | -------------------------------------------------------------------------------------------- |
| Rule ID                         | GD0203                                                                                       |
| Category                        | Usage                                                                                        |
| Fix is breaking or non-breaking | Breaking - If the return type is changed Non-breaking - If the [Signal] attribute is removed |
| Enabled by default              | Yes                                                                                          |

### Cause

A delegate annotated with the `[Signal]` attribute has a return type when `void` was expected.

### Rule description

Every signal must return `void`. There can be multiple callbacks registered for each signal, if signal callbacks could return something it wouldn't be possible to determine which of the returned values to use.

```csharp
// This signal delegate is invalid because it doesn't return void.
public int InvalidSignalEventHandler();

// This signal delegate is valid because it returns void.
public void ValidSignalEventHandler();
```

Take a look at the C# signals documentation for more information about how to declare and use signals.

### How to fix violations

To fix a violation of this rule, change the delegate to return `void` or remove the `[Signal]` attribute from the delegate. Note that removing the attribute will mean the signal is not registered.

> **Tip:** If the signal doesn't need to interact with Godot, consider using [C# events](https://learn.microsoft.com/en-us/dotnet/csharp/programming-guide/events/) directly. Pure C# events allow you to use any C# type for its parameters.

### When to suppress warnings

Do not suppress a warning from this rule. Signal delegates that return something will result in unexpected runtime errors.

---

## GD0301: The generic type argument must be a Variant compatible type

|                                 |          |
| ------------------------------- | -------- |
| Rule ID                         | GD0301   |
| Category                        | Usage    |
| Fix is breaking or non-breaking | Breaking |
| Enabled by default              | Yes      |

### Cause

An unsupported type is specified for a generic type argument when a Variant-compatible type is expected.

### Rule description

When a generic type parameter is annotated with the `[MustBeVariant]` attribute, the generic type is required to be a Variant-compatible type. For example, the generic `Godot.Collections.Array<T>` type only supports items of a type that can be converted to Variant.

```csharp
class SomeType { }

// SomeType is not a valid type because it doesn't derive from GodotObject,
// so it's not compatible with Variant.
var invalidArray = new Godot.Collections.Array<SomeType>();

// System.Int32 is a valid type because it's compatible with Variant.
var validArray = new Godot.Collections.Array<int>();
```

### How to fix violations

To fix a violation of this rule, change the generic type argument to be a Variant-compatible type or use a different API that doesn't require the generic type argument to be a Variant-compatible type.

### When to suppress warnings

Do not suppress a warning from this rule. API that contains generic type arguments annotated with the `[MustBeVariant]` attribute usually has this requirement because the values will be passed to the engine, if the type can't be marshalled it will result in runtime errors.

---

## GD0302: The generic type parameter must be annotated with the '[MustBeVariant]' attribute

|                                 |          |
| ------------------------------- | -------- |
| Rule ID                         | GD0302   |
| Category                        | Usage    |
| Fix is breaking or non-breaking | Breaking |
| Enabled by default              | Yes      |

### Cause

A generic type is specified for a generic type argument when a Variant-compatible type is expected, but the specified generic type is not annotated with the `[MustBeVariant]` attribute.

### Rule description

When a generic type parameter is annotated with the `[MustBeVariant]` attribute, the generic type is required to be a Variant-compatible type. When the type used is also a generic type, this generic type must be annotated with the `[MustBeVariant]` attribute as well. For example, the generic `Godot.Collections.Array<T>` type only supports items of a type that can be converted to Variant, a generic type can be specified if it's properly annotated.

```csharp
public void Method1<T>()
{
    // T is not valid here because it may not a Variant-compatible type.
    var invalidArray = new Godot.Collections.Array<T>();
}

public void Method2<[MustBeVariant] T>()
{
    // T is guaranteed to be a Variant-compatible type because it's annotated
    // with the [MustBeVariant] attribute, so it can be used here.
    var validArray = new Godot.Collections.Array<T>();
}
```

### How to fix violations

To fix a violation of this rule, add the `[MustBeVariant]` attribute to the generic type that is used as a generic type argument that must be Variant-compatible.

### When to suppress warnings

Do not suppress a warning from this rule. API that contains generic type arguments annotated with the `[MustBeVariant]` attribute usually has this requirement because the values will be passed to the engine, if the type can't be marshalled it will result in runtime errors.

---

## GD0303: The parent symbol of a type argument that must be Variant compatible was not handled

|                                 |             |
| ------------------------------- | ----------- |
| Rule ID                         | GD0303      |
| Category                        | Usage       |
| Fix is breaking or non-breaking | Not fixable |
| Enabled by default              | Yes         |

### Cause

This is a bug in the engine and must be reported.

### Rule description

The `MustBeVariantAnalyzer` has found an unhandled case in the user source code. Please, open an [issue](https://github.com/godotengine/godot/issues) and attach a minimal reproduction project so it can be fixed.

### How to fix violations

Violations of this rule can't be fixed.

### When to suppress warnings

Suppressing a warning from this rule may result in unexpected errors, since the case found by the analyzer may need to be handled by the user to prevent types that are not Variant-compatible from reaching the engine. Attempting to marshal incompatible types will result in runtime errors.

---

## GD0401: The class must derive from Godot.GodotObject or a derived class

|                                 |                                                                                                     |
| ------------------------------- | --------------------------------------------------------------------------------------------------- |
| Rule ID                         | GD0401                                                                                              |
| Category                        | Usage                                                                                               |
| Fix is breaking or non-breaking | Breaking - If changing the inheritance chain Non-breaking - If removing the [GlobalClass] attribute |
| Enabled by default              | Yes                                                                                                 |

### Cause

A type annotated with the `[GlobalClass]` attribute does not derive from `GodotObject`.

### Rule description

The `[GlobalClass]` has no effect for types that don't derive from `GodotObject`. Every global class must ultimately derive from `GodotObject` so it can be marshalled.

```csharp
// This type is not registered as a global class because it doesn't derive from GodotObject.
[GlobalClass]
class SomeType { }

// This type is a global class because it derives from Godot.Node
// which ultimately derives from GodotObject.
[GlobalClass]
class MyNode : Node { }

// This type is a global class because it derives from Godot.Resource
// which ultimately derives from GodotObject.
[GlobalClass]
class MyResource : Resource { }
```

### How to fix violations

To fix a violation of this rule, change the type to derive from `GodotObject` or remove the `[GlobalClass]` attribute.

### When to suppress warnings

Do not suppress a warning from this rule. Adding the `[GlobalClass]` to a type that doesn't derive from `GodotObject` is an easy mistake to make and this warning helps users realize that it may result in unexpected errors.

---

## GD0402: The class must not be generic

|                                 |          |
| ------------------------------- | -------- |
| Rule ID                         | GD0402   |
| Category                        | Usage    |
| Fix is breaking or non-breaking | Breaking |
| Enabled by default              | Yes      |

### Cause

A generic type is annotated with the `[GlobalClass]` attribute.

### Rule description

The Godot editor assumes every global class is instantiable, but generic types can't be instantiated because the type parameters are unbound.

```csharp
// This type is a valid global class because it's not generic.
[GlobalClass]
class SomeType : Node { }

// This type is not a valid global class because it's generic.
[GlobalClass]
class SomeGenericType<T> { }
```

### How to fix violations

To fix a violation of this rule, change the type to remove the generic type parameters or remove the `[GlobalClass]` attribute.

### When to suppress warnings

Do not suppress a warning from this rule. Adding the `[GlobalClass]` to a generic type is an easy mistake to make and this warning helps users realize that it may result in unexpected errors.

---

## Change scenes manually

Sometimes it helps to have more control over how you swap scenes around. A [Viewport](../godot_csharp_rendering.md)'s child nodes will render to the image it generates. This holds true even for nodes outside of the "current" scene. Autoloads fall into this category, and also scenes which you instantiate and add to the tree at runtime:

```csharp
public Node simultaneousScene;

public MyClass()
{
    simultaneousScene = ResourceLoader.Load<PackedScene>("res://levels/level2.tscn").Instantiate();
}

public void _AddASceneManually()
{
    // This is like autoloading the scene, only
    // it happens after already loading the main scene.
    GetTree().Root.AddChild(simultaneousScene);
}
```

To complete the cycle and swap out the new scene with the old one, you have a choice to make. Many strategies exist for removing a scene from view of the [Viewport](../godot_csharp_rendering.md). The tradeoffs involve balancing operation speed and memory consumption, as well as balancing data access and integrity.

1. **Delete the existing scene.** [SceneTree.change_scene_to_file()](../godot_csharp_core.md) and [SceneTree.change_scene_to_packed()](../godot_csharp_core.md) will delete the current scene immediately. You can also delete the main scene. Assuming the root node's name is "Main", you could do `get_node("/root/Main").free()` to delete the whole scene.

- Unloads memory.

- Pro: RAM is no longer dragging the dead weight.
- Con: Returning to that scene is now more expensive since it must be loaded back into memory again (takes time AND memory). Not a problem if returning soon is unnecessary.
- Con: No longer have access to that scene's data. Not a problem if using that data soon is unnecessary.
- Note: It can be useful to preserve the data in a soon-to-be-deleted scene by re-attaching one or more of its nodes to a different scene, or even directly to the [SceneTree](../godot_csharp_core.md).
- Processing stops.

- Pro: No nodes means no processing, physics processing, or input handling. The CPU is available to work on the new scene's contents.
- Con: Those nodes' processing and input handling no longer operate. Not a problem if using the updated data is unnecessary.

2. **Hide the existing scene.** By changing the visibility or collision detection of the nodes, you can hide the entire node sub-tree from the player's perspective. Use [CanvasItem.hide()](../godot_csharp_nodes_2d.md) to hide a scene and [CanvasItem.show()](../godot_csharp_nodes_2d.md) to show it again.

- Memory still exists.

- Pro: You can still access the data if needed.
- Pro: There's no need to move any more nodes around to save data.
- Con: More data is being kept in memory, which will be become a problem on memory-sensitive platforms like web or mobile.
- Processing continues.

- Pro: Data continues to receive processing updates, so the scene will keep any data within it that relies on delta time or frame data updated.
- Pro: Nodes are still members of groups (since groups belong to the [SceneTree](../godot_csharp_core.md)).
- Con: The CPU's attention is now divided between both scenes. Too much load could result in low frame rates. You should be sure to test performance as you go to ensure the target platform can support the load from this approach.

3. **Remove the existing scene from the tree.** Assign a variable to the existing scene's root node. Then use [Node.remove_child(Node)](../godot_csharp_misc.md) to detach the entire scene from the tree. To attach it later, use [Node.add_child(Node)](../godot_csharp_misc.md).

- Memory still exists (similar pros/cons as hiding it from view).
- Processing stops (similar pros/cons as deleting it completely).
- Pro: This variation of "hiding" it is much easier to show/hide. Rather than potentially keeping track of multiple changes to the scene, you only need to call the add/remove_child methods. This is similar to disabling game objects in other engines.
- Con: Unlike with hiding it from view only, the data contained within the scene will become stale if it relies on delta time, input, groups, or other data that is derived from [SceneTree](../godot_csharp_core.md) access.

There are also cases where you may wish to have many scenes present at the same time, such as adding your own singleton at runtime, or preserving a scene's data between scene changes (adding the scene to the root node).

```csharp
GetTree().Root.AddChild(scene);
```

Another case may be displaying multiple scenes at the same time using [SubViewportContainers](../godot_csharp_ui_controls.md). This is optimal for rendering different content in different parts of the screen (e.g. minimaps, split-screen multiplayer).

Each option will have cases where it is best appropriate, so you must examine the effects of each approach, and determine what path best fits your unique situation.

---

## About godot-cpp

[godot-cpp](https://github.com/godotengine/godot-cpp) are the official C++ GDExtension bindings, maintained as part of the Godot project.

godot-cpp is built with the GDExtension system, which allows access to Godot in almost the same way as modules: A lot of [engine code](https://github.com/godotengine/godot) can be used in your godot-cpp project almost exactly as it is.

In particular, godot-cpp has access to all functions that GDScript and C# have, and additional access to a few more for fast low-level access of data, or deeper integration with Godot.

### Differences between godot-cpp and C++ modules

You can use both [godot-cpp](https://github.com/godotengine/godot-cpp) and C++ modules to run C or C++ code in a Godot project.

They also both allow you to integrate third-party libraries into Godot. The one you should choose depends on your needs.

#### Advantages of godot-cpp

Unlike modules, godot-cpp (and GDExtensions, in general) don't require compiling the engine's source code, making it easier to distribute your work. It gives you access to most of the API available to GDScript and C#, allowing you to code game logic with full control regarding performance. It's ideal if you need high-performance code you'd like to distribute as an add-on in the asset library.

Also:

- You can use the same compiled godot-cpp library in the editor and exported project. With C++ modules, you have to recompile all the export templates you plan to use if you require its functionality at runtime.
- godot-cpp only requires you to compile your library, not the whole engine. That's unlike C++ modules, which are statically compiled into the engine. Every time you change a module, you need to recompile the engine. Even with incremental builds, this process is slower than using godot-cpp.

#### Advantages of C++ modules

We recommend C++ modules in cases where godot-cpp (or another GDExtension system) isn't enough:

- C++ modules provide deeper integration into the engine. GDExtension's access is not as deep as static modules.
- You can use C++ modules to provide additional features in a project without carrying native library files around. This extends to exported projects.

> **Note:** If you notice that specific systems are not accessible via godot-cpp but are via custom modules, feel free to open an issue on the [godot-cpp repository](https://github.com/godotengine/godot-cpp) to discuss implementation options for exposing the missing functionality.

### Version compatibility

GDExtensions targeting an earlier version of Godot should work in later minor versions, but not vice-versa. For example, a GDExtension targeting Godot 4.2 should work just fine in Godot 4.3, but one targeting Godot 4.3 won't work in Godot 4.2.

For this reason, when creating GDExtensions, you may want to target the lowest version of Godot that has the features you need, _not_ the most recent version of Godot. This can save you from needing to create multiple builds for different versions of Godot.

There is one exception to this: extensions targeting Godot 4.0 will **not** work with Godot 4.1 and later (see [Updating your GDExtension for 4.1](tutorials_migrating.md)).

GDExtensions are also only compatible with engine builds that use the same level of floating-point precision the extension was compiled for. This means that if you use an engine build with double-precision floats, the extension must also be compiled for double-precision floats and use an `extension_api.json` file generated by your custom engine build. See [Large world coordinates](tutorials_physics.md) for details.

Generally speaking, if you build a custom version of Godot, you should generate an `extension_api.json` from it for your GDExtensions, because it may have some differences from official Godot builds. You can learn more about the process of using custom `extension_api.json` files in the build system section.

---

## Secondary build system: Working with CMake

> **See also:** This page documents how to compile godot-cpp. If you're looking to compile Godot instead, see Introduction to the buildsystem.

Beside the [SCons](http://cmake.org) based build system, godot-cpp also provides a [CMakeLists.txt](https://github.com/godotengine/godot-cpp/blob/master/CMakeLists.txt) file to support users that prefer using [CMake](http://scons.org) over SCons for their build system.

While actively supported, the CMake system is considered secondary to the SCons build system. This means it may lack some features that are available to projects using SCons.

### Introduction

Compiling godot-cpp independently of an extension project is mainly for godot-cpp developers, package maintainers, and CI/CD.

Examples of how to use CMake to consume the godot-cpp library as part of an extension project:

- [godot-cpp-template](https://github.com/godotengine/godot-cpp-template/)
- [godot_roguelite](https://github.com/vorlac/godot-roguelite/)
- [godot-orchestrator](https://github.com/CraterCrash/godot-orchestrator/)

Examples for configuring godot-cpp are listed at the bottom of the page, many of which may help with configuring your project.

### CMake's Debug vs Godot's template_debug

Something that has come up during many discussions is the conflation of a compilation of C++ source code with debug symbols enabled, and compiling a Godot extension with debug features enabled. The two concepts are not mutually exclusive.

#### Debug Features

Enables a pre-processor definition to selectively compile code to help users of a Godot extension with their own project.

Debug features are enabled in `editor` and `template_debug` builds, which can be specified during the configure phase like so:

```shell
cmake -S godot-cpp -B cmake-build -DGODOTCPP_TARGET=<target choice>
```

#### Debug

Sets compiler flags so that debug symbols are generated to help godot extension developers debug their extension.

`Debug` is the default build type for CMake projects, the way to select another depends on the generator used:

- For single configuration generators, add `-DCMAKE_BUILD_TYPE=<type>` to the configure command.
- For multi-config generators, add `--config <type>` to the build command.

Where `<type>` is one of `Debug`, `Release`, `RelWithDebInfo`, and `MinSizeRel`.

### SCons Deviations

Not all code from the SCons system can be perfectly represented in CMake, here are the notable differences:

- `debug_symbols`

Is no longer an explicit option, and is enabled when using CMake build configurations; `Debug`, `RelWithDebInfo`.

- `dev_build`

Does not define `NDEBUG` when disabled, `NDEBUG` is set when using CMake build configurations; `Release`, `MinSizeRel`.

- `arch`

CMake sets the architecture via the toolchain files, macOS universal is controlled via the `CMAKE_OSX_ARCHITECTURES` property which is copied to targets when they are defined.

- `debug_crt`

CMake controls linking to Windows runtime libraries by copying the value of `CMAKE_MSVC_RUNTIME_LIBRARIES` to targets as they are defined. godot-cpp will set this variable if it isn't already set. So, include it before other dependencies to have the value propagate across the projects.

### Basic Walk-Through

#### Clone the git repository

```shell
git clone https://github.com/godotengine/godot-cpp.git
Cloning into 'godot-cpp'...
...
```

#### Configure the build

```shell
cmake -S godot-cpp -B cmake-build -G Ninja
```

- `-S` Specifies the source directory as `godot-cpp`
- `-B` Specifies the build directory as `cmake-build`
- `-G` Specifies the Generator as `Ninja`

The source directory in this example is the source root for the freshly cloned godot-cpp. CMake will also interpret the first path in the command as the source path, or if an existing build path is specified it will deduce the source path from the build cache.

The following three commands are equivalent:

```shell
# Current working directory is the godot-cpp source root.
cmake . -B build-dir

# Current working directory is an empty godot-cpp/build-dir.
cmake ../

# Current working directory is an existing build path.
cmake .
```

The build directory is specified so that generated files do not clutter the source tree with build artifacts.

CMake doesn't build the code, it generates the files that a build tool uses, in this case the `Ninja` generator creates [Ninja](https://ninja-build.org/) build files.

To see the list of generators run `cmake --help`.

#### Build Options

To list the available options use the `-L[AH]` command flags. `A` is for advanced, and `H` is for help strings:

```shell
cmake -S godot-cpp -LH
```

Options are specified on the command line when configuring, for example:

```shell
cmake -S godot-cpp -DGODOTCPP_USE_HOT_RELOAD:BOOL=ON \
    -DGODOTCPP_PRECISION:STRING=double \
    -DCMAKE_BUILD_TYPE:STRING=Debug
```

See [setting-build-variables](https://cmake.org/cmake/help/latest/guide/user-interaction/index.html#setting-build-variables) and [build-configurations](https://cmake.org/cmake/help/latest/manual/cmake-buildsystem.7.html#build-configurations) for more information.

##### A non-exhaustive list of options:

```text
// Path to a custom GDExtension API JSON file.
// (takes precedence over GODOTCPP_GDEXTENSION_DIR)
// ( /path/to/custom_api_file )
GODOTCPP_CUSTOM_API_FILE:FILEPATH=

// Force disabling exception handling code. (ON|OFF)
GODOTCPP_DISABLE_EXCEPTIONS:BOOL=ON

// Path to a custom directory containing the GDExtension interface
// header and API JSON file. ( /path/to/gdextension_dir )
GODOTCPP_GDEXTENSION_DIR:PATH=gdextension

// Set the floating-point precision level. (single|double)
GODOTCPP_PRECISION:STRING=single

// Enable the extra accounting required to support hot reload. (ON|OFF)
GODOTCPP_USE_HOT_RELOAD:BOOL=
```

#### Compiling

Tell CMake to invoke the build system it generated in the specified directory. The default target is `template_debug` and the default build configuration is Debug.

```shell
cmake --build cmake-build
```

### Examples

These examples, while intended for godot-cpp developers, package maintainers, and CI/CD may help you configure your own extension project.

Practical examples for how to consume the godot-cpp library as part of an extension project are listed in the **Introduction**.

#### Enabling Integration Testing

The testing target `godot-cpp-test` is guarded by `GODOTCPP_ENABLE_TESTING` which is off by default.

To configure and build the godot-cpp project to enable the integration testing targets the command will look something like:

```shell
cmake -S godot-cpp -B cmake-build -DGODOTCPP_ENABLE_TESTING=YES
cmake --build cmake-build --target godot-cpp-test
```

#### Windows and MSVC - Release

So long as CMake is installed from the [CMake Downloads](https://cmake.org/download/) page and in the PATH, and Microsoft Visual Studio is installed with C++ support, CMake will detect the MSVC compiler.

Note that Visual Studio is a Multi-Config Generator so the build configuration needs to be specified at build time, for example, `--config Release`.

```shell
cmake -S godot-cpp -B cmake-build -DGODOTCPP_ENABLE_TESTING=YES
cmake --build cmake-build -t godot-cpp-test --config Release
```

#### MSys2/clang64, "Ninja" - Debug

Assumes the `ming-w64-clang-x86_64`-toolchain is installed.

Note that Ninja is a Single-Config Generator so the build type needs to be specified at configuration time.

Using the `msys2/clang64` shell:

```shell
cmake -S godot-cpp -B cmake-build -G"Ninja" \
    -DGODOTCPP_ENABLE_TESTING=YES -DCMAKE_BUILD_TYPE=Release
cmake --build cmake-build -t godot-cpp-test
```

#### MSys2/clang64, "Ninja Multi-Config" - dev_build, Debug Symbols

Assumes the `ming-w64-clang-x86_64`-toolchain is installed.

This time we are choosing the 'Ninja Multi-Config' generator, so the build type is specified at build time.

Using the `msys2/clang64` shell:

```shell
cmake -S godot-cpp -B cmake-build -G"Ninja Multi-Config" \
    -DGODOTCPP_ENABLE_TESTING=YES -DGODOTCPP_DEV_BUILD:BOOL=ON
cmake --build cmake-build -t godot-cpp-test --config Debug
```

#### Emscripten for web platform

This has only been tested on Windows so far. You can use this example workflow:

- Clone and install the latest Emscripten tools to `c:\emsdk`.
- Use `C:\emsdk\emsdk.ps1 activate latest` to enable the environment from powershell in the current shell.
- The `emcmake.bat` utility adds the emscripten toolchain to the CMake command. It can also be added manually; the location is listed inside the `emcmake.bat` file

```powershell
C:\emsdk\emsdk.ps1 activate latest
emcmake.bat cmake -S godot-cpp -B cmake-build-web -DCMAKE_BUILD_TYPE=Release
cmake --build cmake-build-web
```

#### Android Cross Compile from Windows

There are two separate paths you can choose when configuring for android.

Use the `CMAKE_ANDROID_*` variables specified on the command line or in your own toolchain file as listed in the [cmake-toolchains](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#cross-compiling-for-android-with-the-ndk) documentation.

Or use the toolchain and scripts provided by the Android SDK and make changes using the `ANDROID_*` variables listed there. Where `<version>` is whatever NDK version you have installed (tested with 28.1.13356709) and `<platform>` is for the Android sdk platform, (tested with `android-29`).

> **Warning:** The Android SDK [website](https://developer.android.com/ndk/guides/cmake) explicitly states that they do not support using the CMake built-in method, and recommends you stick with their toolchain files.

##### Using your own toolchain file

As described in the CMake documentation:

```shell
cmake -S godot-cpp -B cmake-build --toolchain my_toolchain.cmake
cmake --build cmake-build -t template_release
```

Doing the equivalent just using the command line:

```shell
cmake -S godot-cpp -B cmake-build \
    -DCMAKE_SYSTEM_NAME=Android \
    -DCMAKE_SYSTEM_VERSION=<platform> \
    -DCMAKE_ANDROID_ARCH_ABI=<arch> \
    -DCMAKE_ANDROID_NDK=/path/to/android-ndk
cmake --build cmake-build
```

##### Using the Android SDK toolchain file

This defaults to the minimum supported version and armv7-a:

```shell
cmake -S godot-cpp -B cmake-build \
    --toolchain $ANDROID_HOME/ndk/<version>/build/cmake/android.toolchain.cmake
cmake --build cmake-build
```

Specifying the Android platform and ABI:

```shell
cmake -S godot-cpp -B cmake-build \
    --toolchain $ANDROID_HOME/ndk/<version>/build/cmake/android.toolchain.cmake \
    -DANDROID_PLATFORM:STRING=android-29 \
    -DANDROID_ABI:STRING=armeabi-v7a
cmake --build cmake-build
```

---

## Main build system: Working with SCons

> **See also:** This page documents how to compile godot-cpp. If you're looking to compile Godot instead, see Introduction to the buildsystem.

[godot-cpp](https://github.com/godotengine/godot-cpp) uses [SCons](https://scons.org) as its main build system. It is modeled after Godot's build system, and some commands available there are also available in godot-cpp projects.

### Getting started

To build a godot-cpp project, it is generally sufficient to install [SCons](https://scons.org), and simply run it in the project directory:

scons

You may want to learn about available options:

scons --help

To cleanly re-build your project, add `--clean` to your build command:

scons --clean

You can find more information about common SCons arguments and build patterns in the [SCons User Guide](https://scons.org/doc/latest/HTML/scons-user/index.html). Additional commands may be added by individual godot-cpp projects, so consult their specific documentation for more information on those.

### Configuring an IDE

Most IDEs can use a `compile_commands.json` file to understand a C++ project. You can generate it with godot-cpp using the following command:

```shell
# Generate compile_commands.json while compiling.
scons compiledb=yes

# Generate compile_commands.json without compiling.
scons compiledb=yes compile_commands.json
```

For more information, please check out the IDE configuration guides. Although written for Godot engine contributors, they are largely applicable to godot-cpp projects as well.

### Loading your GDExtension in Godot

Godot loads GDExtensions by finding .gdextension files in the project directory. `.gdextension` files are used to select and load a binary compatible with the current computer / operating system.

The [godot-cpp-template](https://github.com/godotengine/godot-cpp-template), as well as the Getting Started section, provide example `.gdextension` files for GDExtensions that are widely compatible to many different systems.

### Building for multiple platforms

GDExtensions are expected to run on many different systems, each with separate binaries and build configurations. If you are planning to publish your GDExtension, we recommend you provide binaries for all configurations that are mentioned in the [godot-cpp-template](https://github.com/godotengine/godot-cpp-template) [.gdextension file](https://github.com/godotengine/godot-cpp-template/blob/main/demo/bin/example.gdextension).

There are two popular ways by which cross platform builds can be achieved:

- Cross-platform build tools
- Continuous Integration (CI)

[godot-cpp-template](https://github.com/godotengine/godot-cpp-template) contains an [example setup](https://github.com/godotengine/godot-cpp-template/tree/main/.github/workflows) for a GitHub based CI workflow.

### Using a custom API file

Every branch of godot-cpp comes with an API file (`extension_api.json`) appropriate for the respective Godot version (e.g. the `4.3` branch comes with the API file compatible with Godot version `4.3` and later).

However, you may want to use a custom `extension_api.json`, for example:

- If you want to use the latest APIs from Godot `master`.
- If you build Godot yourself with different options than the official builds (e.g. `disable_3d=yes` or `precision=double`).
- If you want to use APIs exposed by custom modules.

To use a custom API file, you first have to generate it from the appropriate Godot executable:

```shell
godot --dump-extension-api
```

The resulting `extension_api.json` file will be created in the executable's directory. To use it, you can add `custom_api_file` to your build command:

```shell
scons platform=<platform> custom_api_file=<PATH_TO_FILE>
```

Alternatively, you can add it as the default API file to your project by adding the following line to your SConstruct file:

```python
localEnv["custom_api_file"] = "extension_api.json"
```

---

## Core functions and types

godot-cpp's API is designed to be as similar as possible to Godot's internal API.

This means that, in general, you can use the Engine details section to learn how to work with godot-cpp. In addition, it can often be useful to browse the [engine's code](https://github.com/godotengine/godot) for examples for how to work with Godot's API.

That being said, there are some differences to be aware of, which are documented here.

### Common functions and macros

Please refer to Common engine methods and macros for information on this. The functions and macros documented there are also available in godot-cpp.

### Core types

Godot's Core types are also available in godot-cpp, and the same recommendations apply as described in that article. The types are regularly synchronized with the Godot codebase.

In your own code, you can also use [C++ STL types](https://en.cppreference.com/w/cpp/container.html), or types from any library you choose, but they won't be compatible with Godot's APIs.

#### Packed arrays

While in Godot, the `Packed*Array` types are aliases of `Vector`, in godot-cpp, they're their own types, using the Godot bindings. This is because `Packed*Array` are exposed to Godot and limited to only Godot types, whereas `Vector` can hold any C++ type which Godot might not be able to understand.

In general, the `Packed*Array` types work the same way as their `Vector` aliases, however, there are some notable differences.

##### Data access

`Vector` keeps its data entirely within the GDExtension, whereas the `Packed*Array` types keep their data on the Godot side. This means that any time a `Packed*Array` is accessed, it needs to call into Godot.

To efficiently read or write a large amount of data into a `Packed*Array`, you should call `.ptr()` (for reading) or `.ptrw()` (for writing) to get a pointer directly to the array's memory:

```cpp
// BAD!
void my_bad_function(const PackedByteArray &p_array) {
    for (int i = 0; i < p_array.size(); i++) {
        // Each time this runs it needs to call into Godot.
        uint8_t byte = p_array[i];

        // .. do something with the byte.
    }
}

// GOOD :-)
void my_good_function(const PackedByteArray &p_array) {
    const uint8_t *array_ptr = p_array.ptr();
    for (int i = 0; i < p_array.size(); i++) {
        // This directly accesses the memory!
        uint8_t byte = array_ptr[i];

        // .. do something with the byte.
    }
}
```

##### Copying

`Variant` wrappers for `Packed*Array` treat them as pass-by-reference, while the `Packed*Array` types themselves are pass-by-value (implemented as copy-on-write).

In addition, it may be of interest that GDScript calls use the `Variant` call interface: Any `Packed*Array` arguments to your functions will be passed in a `Variant`, and unpacked from there. This can create copies of the types, so the argument you receive may be a copy of the argument that the function was called with. In practice, this means you cannot rely on that the argument passed to you can be modified at the caller's site.

### Variant class

Please refer to Variant class to learn about how to work with `Variant`.

Most importantly, you should be aware that all functions exposed through the GDExtension API must be compatible with `Variant`.

### Object class

Please refer to Object class to learn how to register and work with your own `Object` types.

We are not aware of any major differences between the godot-cpp `Object` API and Godot's internal `Object` API, except that some methods are available in Godot's internal API that are not available in godot-cpp.

You should be aware that the pointer to your godot-cpp `Object` is different from the pointer that Godot uses internally. This is because the godot-cpp version is an extension instance, allocated separately from the original `Object`. However, in practice, this difference is usually not noticeable.

---
