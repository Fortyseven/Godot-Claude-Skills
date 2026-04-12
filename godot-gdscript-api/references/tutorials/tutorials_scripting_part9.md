# Godot 4 GDScript Tutorials — Scripting (Part 9)

> 3 tutorials. GDScript-specific code examples.

## GDScript documentation comments

In GDScript, comments can be used to document your code and add descriptions to the members of a script. There are two differences between a normal comment and a documentation comment. Firstly, a documentation comment should start with double hash symbols `##`. Secondly, it must immediately precede a script member, or for script descriptions, be placed at the top of the script. If an exported variable is documented, its description is used as a tooltip in the editor. This documentation can be generated as XML files by the editor.

### Documenting a script

Comments documenting a script must come before any member documentation. A suggested format for script documentation can be divided into three parts.

- A brief description of the script.
- Detailed description.
- Tutorials and deprecated/experimental marks.

To separate these from each other, the documentation comments use special tags. The tag must be at the beginning of a line (ignoring preceding white space) and must have the format `@`, followed by the keyword.

#### Tags

| Brief description | No tag. Lives at the very beginning of the documentation section. |
| Description | No tag. Use one blank line to separate the description from the brief. |
| Tutorial | @tutorial: https://example.com @tutorial(The Title Here): https://example.com |
| Deprecated | @deprecated @deprecated: Use [AnotherClass] instead. |
| Experimental | @experimental @experimental: This class is unstable. |

For example:

```gdscript
extends Node2D
## A brief description of the class's role and functionality.
##
## The description of the script, what it can do,
## and any further detail.
##
## @tutorial:             https://example.com/tutorial_1
## @tutorial(Tutorial 2): https://example.com/tutorial_2
## @experimental
```

> **Warning:** If there is any space in between the tag name and colon, for example `@tutorial :`, it won't be treated as a valid tag and will be ignored.

> **Note:** When the description spans multiple lines, the preceding and trailing white spaces will be stripped and joined with a single space. To preserve the line break use `[br]`. See also **BBCode and class reference** below.

### Documenting script members

Members that are applicable for documentation:

- Signal
- Enum
- Enum value
- Constant
- Variable
- Function
- Inner class

Documentation of a script member must immediately precede the member or its annotations if it has any. The description can have more than one line but every line must start with the double hash symbol `##` to be considered as part of the documentation.

#### Tags

| Description | No tag. |
| Deprecated | @deprecated @deprecated: Use [member another] instead. |
| Experimental | @experimental @experimental: This method is incomplete. |

For example:

```gdscript
## The description of the variable.
## @deprecated: Use [member other_var] instead.
var my_var
```

Alternatively, you can use inline documentation comments:

```gdscript
signal my_signal ## My signal.

enum MyEnum { ## My enum.
    VALUE_A = 0, ## Value A.
    VALUE_B = 1, ## Value B.
}

const MY_CONST = 1 ## My constant.

var my_var ## My variable.

func my_func(): ## My func.
    pass

class MyClass: ## My class.
    pass
```

The script documentation will update in the editor help window every time the script is updated. If any member variable or function name starts with an underscore, it will be treated as private. It will not appear in the documentation and will be ignored in the help window.

### Complete script example

```gdscript
extends Node2D
## A brief description of the class's role and functionality.
##
## The description of the script, what it can do,
## and any further detail.
##
## @tutorial:             https://example.com/tutorial_1
## @tutorial(Tutorial 2): https://example.com/tutorial_2
## @experimental

## The description of a signal.
signal my_signal

## This is a description of the below enum.
enum Direction {
    ## Direction up.
    UP = 0,
    ## Direction down.
    DOWN = 1,
    ## Direction left.
    LEFT = 2,
    ## Direction right.
    RIGHT = 3,
}

## The description of a constant.
const GRAVITY = 9.8

## The description of the variable v1.
var v1

## This is a multiline description of the variable v2.[br]
## The type information below will be extracted for the documentation.
var v2: int

##
# ...
```

### @deprecated and @experimental tags

You can mark a class or any of its members as deprecated or experimental. This will add the corresponding indicator in the built-in documentation viewer. Optionally, you can provide a short message explaining why the API is not recommended. This can be especially useful for plugin and library creators.

- **Deprecated** marks a non-recommended API that is subject to removal or incompatible change in a future major release. Usually the API is kept for backwards compatibility.
- **Experimental** marks a new unstable API that may be changed or removed in the current major branch. Using this API is not recommended in production code.

> **Note:** While technically you can use both `@deprecated` and `@experimental` tags on the same class/member, this is not recommended as it is against common conventions.

### BBCode and class reference

Godot's class reference supports BBCode-like tags. They add nice formatting to the text which could also be used in the documentation. See also class reference bbcode. Note that this is slightly different from the `RichTextLabel` [BBCode](tutorials_ui.md).

Whenever you link to a member of another class, you need to specify the class name. For links to the same class, the class name is optional and can be omitted.

Here's the list of available tags:

| Tag and Description                                   | Example                                                               | Result                       |
| ----------------------------------------------------- | --------------------------------------------------------------------- | ---------------------------- |
| [Class] Link to class                                 | Move the [Sprite2D].                                                  | Move the Sprite2D.           |
| [annotation Class.name] Link to annotation            | See [annotation @GDScript.@rpc].                                      | See @GDScript.@rpc.          |
| [constant Class.name] Link to constant                | See [constant Color.RED].                                             | See Color.RED.               |
| [enum Class.name] Link to enum                        | See [enum Mesh.ArrayType].                                            | See Mesh.ArrayType.          |
| [member Class.name] Link to member (property)         | Get [member Node2D.scale].                                            | Get Node2D.scale.            |
| [method Class.name] Link to method                    | Call [method Node3D.hide].                                            | Call Node3D.hide().          |
| [constructor Class.name] Link to built-in constructor | Use [constructor Color.Color].                                        | Use Color.Color.             |
| [operator Class.name] Link to built-in operator       | Use [operator Color.operator *].                                      | Use Color.operator \*.       |
| [signal Class.name] Link to signal                    | Emit [signal Node.renamed].                                           | Emit Node.renamed.           |
| [theme_item Class.name] Link to theme item            | See [theme_item Label.font].                                          | See Label.font.              |
| [param name] Parameter name (as code)                 | Takes [param size] for the size.                                      | Takes size for the size.     |
| [br] Line break                                       | Line 1.[br] Line 2.                                                   | Line 1. Line 2.              |
| [lb] [rb] [ and ] respectively                        | [lb]b[rb]text[lb]/b[rb]                                               | [b]text[/b]                  |
| [b] [/b] Bold                                         | Do [b]not[/b] call this method.                                       | Do not call this method.     |
| [i] [/i] Italic                                       | Returns the [i]global[/i] position.                                   | Returns the global position. |
| [u] [/u] Underline                                    | [u]Always[/u] use this method.                                        | Always use this method.      |
| [s] [/s] Strikethrough                                | [s]Outdated information.[/s]                                          | Outdated information.        |
| [color] [/color] Color                                | [color=red]Error![/color]                                             | Error!                       |
| [font] [/font] Font                                   | [font=res://mono.ttf]LICENSE[/font]                                   | LICENSE                      |
| [img] [/img] Image                                    | [img width=32]res://icon.svg[/img]                                    |                              |
| [url] [/url] Hyperlink                                | [url]https://example.com[/url] [url=https://example.com]Website[/url] | https://example.com Website  |
| [center] [/center] Horizontal centering               | [center]2 + 2 = 4[/center]                                            | 2 + 2 = 4                    |
| [kbd] [/kbd] Keyboard/mouse shortcut                  | Press [kbd]Ctrl + C[/kbd].                                            | Press Ctrl + C.              |
| [code] [/code] Inline code fragment                   | Returns [code]true[/code].                                            | Returns true.                |
| [codeblock] [/codeblock] Multiline code block         | See below.                                                            | See below.                   |

> **Note:** 1. Currently only `@GDScript` has annotations. 2. `[kbd]` disables BBCode until the parser encounters `[/kbd]`. 3. `[code]` disables BBCode until the parser encounters `[/code]`. 4. `[codeblock]` disables BBCode until the parser encounters `[/codeblock]`.

> **Warning:** Use `[codeblock]` for pre-formatted code blocks. Inside `[codeblock]`, always use **four spaces** for indentation (the parser will delete tabs).

```gdscript
## Do something for this plugin. Before using the method
## you first have to [method initialize] [MyPlugin].[br]
## [color=yellow]Warning:[/color] Always [method clean] after use.[br]
## Usage:
## [codeblock]
## func _ready():
##     the_plugin.initialize()
##     the_plugin.do_something()
##     the_plugin.clean()
## [/codeblock]
func do_something():
    pass
```

By default, `[codeblock]` highlights GDScript syntax. You can change it using the `lang` attribute. Currently supported options are:

- `[codeblock lang=text]` disables syntax highlighting;
- `[codeblock lang=gdscript]` highlights GDScript syntax;
- `[codeblock lang=csharp]` highlights C# syntax (only in .NET version).

---

## GDScript exported properties

In Godot, class members can be exported. This means their value gets saved along with the resource (such as the [scene](../godot_gdscript_misc.md)) they're attached to, and get transferred over when using [RPCs](tutorials_networking.md). They will also be available for editing in the property editor. Exporting is done by using the `@export` annotation.

```gdscript
@export var number: int = 5
```

In that example the value `5` will be saved and visible in the property editor.

An exported variable must be initialized to a constant expression or have a type specifier in the variable. Some of the export annotations have a specific type and don't need the variable to be typed (see the _Examples_ section below).

One of the fundamental benefits of exporting member variables is to have them visible and editable in the editor. This way, artists and game designers can modify values that later influence how the program runs. For this, a special export syntax is provided. Additionally, documentation comments can be used for tooltip descriptions, visible on mouse over.

> **Note:** Exporting properties can also be done in other languages such as C#. The syntax varies depending on the language. See C# exported properties for information on C# exports.

### Basic use

If the exported value assigns a constant or constant expression, the type will be inferred and used in the editor.

```gdscript
@export var number = 5
```

If there's no default value, you can add a type to the variable.

```gdscript
@export var number: int
```

Resources and nodes can be exported.

```gdscript
@export var resource: Resource
@export var node: Node
```

Even if a script is not executed in the editor, exported properties can still be edited. However, getters and setters will only be used if the script is in Tool mode.

### Grouping exports

It is possible to group your exported properties inside the Inspector with the `@export_group` annotation. Every exported property after this annotation will be added to the group. Start a new group or use `@export_group("")` to break out.

```gdscript
@export_group("My Properties")
@export var number = 3
```

The second argument of the annotation can be used to only group properties with the specified prefix.

Groups cannot be nested, use `@export_subgroup` to create subgroups within a group.

```gdscript
@export_subgroup("Extra Properties")
@export var string = ""
@export var flag = false
```

You can also change the name of your main category, or create additional categories in the property list with the `@export_category` annotation.

```gdscript
@export_category("Main Category")
@export var number = 3
@export var string = ""

@export_category("Extra Category")
@export var flag = false
```

> **Note:** The list of properties is organized based on the class inheritance and new categories break that expectation. Use them carefully, especially when creating projects for public use.

### Strings as paths

String as a path to a file. See `@export_file`.

```gdscript
@export_file var f
```

String as a path to a directory. See `@export_dir`.

```gdscript
@export_dir var f
```

String as a path to a file, custom filter provided as hint. See again `@export_file`.

```gdscript
@export_file("*.txt") var f
```

Using paths in the global filesystem is also possible, but only in scripts in tool mode.

String as a path to a PNG file in the global filesystem. See `@export_global_file`.

```gdscript
@export_global_file("*.png") var tool_image
```

String as a path to a directory in the global filesystem. See `@export_global_dir`.

```gdscript
@export_global_dir var tool_dir
```

The multiline annotation tells the editor to show a large input field for editing over multiple lines. See `@export_multiline`.

```gdscript
@export_multiline var text
```

### Limiting editor input ranges

See `@export_range` for all of the following.

Allow integer values from 0 to 20.

```gdscript
@export_range(0, 20) var i
```

Allow integer values from -10 to 20.

```gdscript
@export_range(-10, 20) var j
```

Allow floats from -10 to 20 and snap the value to multiples of 0.2.

```gdscript
@export_range(-10, 20, 0.2) var k: float
```

The limits can be made to affect only the slider if you add the hints `"or_less"` and/or `"or_greater"`. If either these hints are used, it will be possible for the user to enter any value or drag the value with the mouse when not using the slider, even if outside the specified range.

```gdscript
@export_range(0, 100, 1, "or_less", "or_greater") var l: int
```

The `"exp"` hint can be used to make a value have an exponential slider instead of a linear slider. This means that when dragging the slider towards the right, changes will become progressively faster when dragging the mouse. This is useful to make editing values that can be either very small or very large easier, at the cost of being less intuitive.

```gdscript
@export_range(0, 100000, 0.01, "exp") var exponential: float
```

For values that are meant to represent an easing factor, use **Floats with easing hint** instead.

The `"hide_slider"` hint can be used to hide the horizontal bar that appears below `float` properties, or the up/down arrows that appear besides `int` properties:

```gdscript
@export_range(0, 1000, 0.01, "hide_slider") var no_slider: float
```

### Adding suffixes and handling degrees/radians

A suffix can also be defined to make the value more self-explanatory in the inspector. For example, to define a value that is meant to be configured as "meters" (`m`) by the user:

```gdscript
@export_range(0, 100, 1, "suffix:m") var m: int
```

For angles that are stored in radians but displayed as degrees to the user, use the "radians_as_degrees" hint:

```gdscript
@export_range(0, 360, 0.1, "radians_as_degrees") var angle: float
```

This performs automatic conversion when the value is displayed or modified in the inspector and also displays a degree (`°`) suffix. This approach is used by Godot's own rotation properties throughout the editor.

If the angle is stored in degrees instead, use the "degrees" hint to display the degree symbol while disabling the automatic degrees-to-radians conversion when the value is modified from the inspector.

### Floats with easing hint

Display a visual representation of the `ease()` function when editing. See `@export_exp_easing`.

```gdscript
@export_exp_easing var transition_speed
```

### Colors

Regular color given as red-green-blue-alpha value.

```gdscript
@export var col: Color
```

Color given as red-green-blue value (alpha will always be 1). See `@export_color_no_alpha`.

```gdscript
@export_color_no_alpha var col: Color
```

### Nodes

Nodes can also be directly exported as properties in a script without having to use NodePaths:

```gdscript
# Allows any node.
@export var node: Node

# Allows any node that inherits from BaseButton.
# Custom classes declared with `class_name` can also be used.
@export var some_button: BaseButton
```

Exporting NodePaths like in Godot 3.x is still possible, in case you need it:

```gdscript
@export var node_path: NodePath
var node = get_node(node_path)
```

If you want to limit the types of nodes for NodePaths, you can use the `@export_node_path` annotation:

```gdscript
@export_node_path("Button", "TouchScreenButton") var some_button
```

### Resources

```gdscript
@export var resource: Resource
```

In the Inspector, you can then drag and drop a resource file from the FileSystem dock into the variable slot.

Opening the inspector dropdown may result in an extremely long list of possible classes to create, however. Therefore, if you specify an extension of Resource such as:

```gdscript
@export var resource: AnimationNode
```

The drop-down menu will be limited to AnimationNode and all its derived classes.

### Exporting bit flags

See `@export_flags`.

Integers used as bit flags can store multiple `true`/`false` (boolean) values in one property. By using the `@export_flags` annotation, they can be set from the editor:

```gdscript
# Set any of the given flags from the editor.
@export_flags("Fire", "Water", "Earth", "Wind") var spell_elements = 0
```

You must provide a string description for each flag. In this example, `Fire` has value 1, `Water` has value 2, `Earth` has value 4 and `Wind` corresponds to value 8. Usually, constants should be defined accordingly (e.g. `const ELEMENT_WIND = 8` and so on).

You can add explicit values using a colon:

```gdscript
@export_flags("Self:4", "Allies:8", "Foes:16") var spell_targets = 0
```

Only power of 2 values are valid as bit flags options. The lowest allowed value is 1, as 0 means that nothing is selected. You can also add options that are a combination of other flags:

```gdscript
@export_flags("Self:4", "Allies:8", "Self and Allies:12", "Foes:16")
var spell_targets = 0
```

Export annotations are also provided for the physics, render, and navigation layers defined in the project settings:

```gdscript
@export_flags_2d_physics var layers_2d_physics
@export_flags_2d_render var layers_2d_render
@export_flags_2d_navigation var layers_2d_navigation
@export_flags_3d_physics var layers_3d_physics
@export_flags_3d_render var layers_3d_render
@export_flags_3d_navigation var layers_3d_navigation
```

Using bit flags requires some understanding of bitwise operations. If in doubt, use boolean variables instead.

### Exporting enums

See `@export_enum`.

Properties can be exported with a type hint referencing an enum to limit their values to the values of the enumeration. The editor will create a widget in the Inspector, enumerating the following as "Thing 1", "Thing 2", "Another Thing". The value will be stored as an integer.

```gdscript
enum NamedEnum {THING_1, THING_2, ANOTHER_THING = -1}
@export var x: NamedEnum
```

Integer and string properties can also be limited to a specific list of values using the `@export_enum` annotation. The editor will create a widget in the Inspector, enumerating the following as Warrior, Magician, Thief. The value will be stored as an integer, corresponding to the index of the selected option (i.e. `0`, `1`, or `2`).

```gdscript
@export_enum("Warrior", "Magician", "Thief") var character_class: int
```

You can add explicit values using a colon:

```gdscript
@export_enum("Slow:30", "Average:60", "Very Fast:200") var character_speed: int
```

If the type is String, the value will be stored as a string.

```gdscript
@export_enum("Rebecca", "Mary", "Leah") var character_name: String
```

If you want to set an initial value, you must specify it explicitly:

```gdscript
@export_enum("Rebecca", "Mary", "Leah") var character_name: String = "Rebecca"
```

### Exporting arrays

Exported arrays can have initializers, but they must be constant expressions.

If the exported array specifies a type which inherits from Resource, the array values can be set in the inspector by dragging and dropping multiple files from the FileSystem dock at once.

The default value **must** be a constant expression.

```gdscript
@export var a = [1, 2, 3]
```

Exported arrays can specify type (using the same hints as before).

```gdscript
@export var ints: Array[int] = [1, 2, 3]

# Nested typed arrays such as `Array[Array[float]]` are not supported yet.
@export var two_dimensional: Array[Array] = [[1.0, 2.0], [3.0, 4.0]]
```

You can omit the default value, but it would then be `null` if not assigned.

```gdscript
@export var b: Array
@export var scenes: Array[PackedScene]
```

Arrays with specified types which inherit from resource can be set by drag-and-dropping multiple files from the FileSystem dock.

```gdscript
@export var textures: Array[Texture] = []
@export var scenes: Array[PackedScene] = []
```

Packed type arrays also work, but only initialized empty:

```gdscript
@export var vector3s = PackedVector3Array()
@export var strings = PackedStringArray()
```

Other export variants can also be used when exporting arrays:

```gdscript
@export_range(-360, 360, 0.001, "degrees") var laser_angles: Array[float] = []
@export_file("*.json") var skill_trees: Array[String] = []
@export_color_no_alpha var hair_colors = PackedColorArray()
@export_enum("Espresso", "Mocha", "Latte", "Capuccino") var barista_suggestions: Array[String] = []
```

### @export_storage

See `@export_storage`.

By default, exporting a property has two effects:

1. makes the property stored in the scene/resource file (`PROPERTY_USAGE_STORAGE`);
2. adds a field to the Inspector (`PROPERTY_USAGE_EDITOR`).

However, sometimes you may want to make a property serializable, but not display it in the editor to prevent unintentional changes and cluttering the interface.

To do this you can use `@export_storage`. This can be useful for `@tool` scripts. Also the property value is copied when [Resource.duplicate()](../godot_gdscript_core.md) or [Node.duplicate()](../godot_gdscript_misc.md) is called, unlike non-exported variables.

```gdscript
var a # Not stored in the file, not displayed in the editor.
@export_storage var b # Stored in the file, not displayed in the editor.
@export var c: int # Stored in the file, displayed in the editor.
```

### @export_custom

If you need more control than what's exposed with the built-in `@export` annotations, you can use `@export_custom` instead. This allows defining any property hint, hint string and usage flags, with a syntax similar to the one used by the editor for built-in nodes.

For example, this exposes the `altitude` property with no range limits but an `m` (meter) suffix defined:

```gdscript
@export_custom(PROPERTY_HINT_NONE, "suffix:m") var altitude: float
```

The above is normally not feasible with the standard `@export_range` syntax, since it requires defining a range.

See the `class reference` for a list of parameters and their allowed values.

> **Warning:** When using `@export_custom`, GDScript does not perform any validation on the syntax. Invalid syntax may have unexpected behavior in the inspector.

### @export_tool_button

If you need to create a clickable inspector button, you can use `@export_tool_button`. This exports a `Callable` property as a clickable button. When the button is pressed, the callable is called.

You can specify a custom icon name, which must match one of the icon file names from the [editor/icons](https://github.com/godotengine/godot/tree/master/editor/icons) folder of the Godot source repository (case-sensitive). You can also browse the editor icons using the [Godot editor icons](https://godot-editor-icons.github.io/) website.

For example, if you wish to use `Node2D.svg` from that folder, you must specify `"Node2D"` as the second parameter of `@export_tool_button`. It is not currently possible to use custom icons from the project folder; only built-in editor icons can be used.

This exports a button with label `"Hello"` and icon `"Callable"` (which is the default if no icon is specified). When you press it, it will print `"Hello world!"`.

```gdscript
@tool
extends Node

@export_tool_button("Hello", "Callable") var hello_action = hello

func hello():
    print("Hello world!")
```

### Setting exported variables from a tool script

When changing an exported variable's value from a script in Tool mode, the value in the inspector won't be updated automatically. To update it, call [notify_property_list_changed()](../godot_gdscript_misc.md) after setting the exported variable's value.

### Reading an exported variable's value early on

If you read an exported variable's value in [\_init()](../godot_gdscript_misc.md), it will return the default value specified in the export annotation instead of the value that was set in the inspector. This is because assigning values from the saved scene/resource file occurs _after_ object initialization; until then, the default value is used.

To get the value that was set in the inspector (and therefore saved in the scene/resource file), you need to read it _after_ the object is constructed, such as in [Node.\_ready()](../godot_gdscript_misc.md). You can also read the value in a setter that's defined on the exported property, which is useful in custom resources where `_ready()` is not available:

```gdscript
# Set this property to 3 in the inspector.
@export var exported_variable = 2:
    set(value):
        exported_variable = value
        print("Inspector-set value: ", exported_variable)

func _init():
    print("Initial value: ", exported_variable)
```

Results in:

```none
Initial value: 2
Inspector-set value: 3
```

### Advanced exports

Not every type of export can be provided on the level of the language itself to avoid unnecessary design complexity. The following describes some more or less common exporting features which can be implemented with a low-level API.

Before reading further, you should get familiar with the way properties are handled and how they can be customized with [\_set()](../godot_gdscript_misc.md), [\_get()](../godot_gdscript_misc.md), and [\_get_property_list()](../godot_gdscript_misc.md) methods as described in [Accessing data or logic from an object](tutorials_best_practices.md).

> **See also:** For binding properties using the above methods in C++, see Binding properties using \_set/\_get/\_get_property_list.

> **Warning:** The script must operate in the `@tool` mode so the above methods can work from within the editor.

---

## GDScript format strings

Godot offers multiple ways to dynamically change the contents of strings:

- Format strings: `var string = "I have %s cats." % "3"`
- The `String.format()` method: `var string = "I have {0} cats.".format([3])`
- String concatenation: `var string = "I have " + str(3) + " cats."`

This page explains how to use format strings, and briefly explains the `format()` method and string concatenation.

### Format strings

_Format strings_ are a way to reuse text templates to succinctly create different but similar strings.

Format strings are just like normal strings, except they contain certain placeholder character sequences such as `%s`. These placeholders can then be replaced by parameters handed to the format string.

Examine this concrete GDScript example:

```gdscript
# Define a format string with placeholder '%s'
var format_string = "We're waiting for %s."

# Using the '%' operator, the placeholder is replaced with the desired value
var actual_string = format_string % "Godot"

print(actual_string)
# Output: "We're waiting for Godot."
```

Placeholders always start with a `%`, but the next character or characters, the _format specifier_, determines how the given value is converted to a string.

The `%s` seen in the example above is the simplest placeholder and works for most use cases: it converts the value by the same method by which an implicit String conversion or `str()` would convert it. Strings remain unchanged, booleans turn into either `"True"` or `"False"`, an `int` or `float` becomes a decimal, and other types usually return their data in a human-readable string.

There are other **format specifiers**.

### Multiple placeholders

Format strings may contain multiple placeholders. In such a case, the values are handed in the form of an array, one value per placeholder (unless using a format specifier with `*`, see **dynamic padding**):

```gdscript
var format_string = "%s was reluctant to learn %s, but now he enjoys it."
var actual_string = format_string % ["Estragon", "GDScript"]

print(actual_string)
# Output: "Estragon was reluctant to learn GDScript, but now he enjoys it."
```

Note the values are inserted in order. Remember all placeholders must be replaced at once, so there must be an appropriate number of values.

### Format specifiers

There are format specifiers other than `s` that can be used in placeholders. They consist of one or more characters. Some of them work by themselves like `s`, some appear before other characters, some only work with certain values or characters.

#### Placeholder types

One and only one of these must always appear as the last character in a format specifier. Apart from `s`, these require certain types of parameters.

| s | Simple conversion to String by the same method as implicit String conversion. |
| c | A single Unicode character. Accepts a Unicode code point (integer) or a single-character string. Supports values beyond 255. |
| d | A decimal integer. Expects an integer or a real number (will be floored). |
| o | An octal integer. Expects an integer or a real number (will be floored). |
| x | A hexadecimal integer with lower-case letters. Expects an integer or a real number (will be floored). |
| X | A hexadecimal integer with upper-case letters. Expects an integer or a real number (will be floored). |
| f | A decimal real number. Expects an integer or a real number. |
| v | A vector. Expects any float or int-based vector object ( Vector2, Vector3, Vector4, Vector2i, Vector3i or Vector4i). Will display the vector coordinates in parentheses, formatting each coordinate as if it was an %f, and using the same modifiers. |

#### Placeholder modifiers

These characters appear before the above. Some of them work only under certain conditions.

| + | In number specifiers, show + sign if positive. |
| Integer | Set padding. Padded with spaces or with zeroes if integer starts with 0 in an integer or real number placeholder. The leading 0 is ignored if - is present. When used after ., see .. |
| . | Before f or v, set precision to 0 decimal places. Can be followed up with numbers to change. Padded with zeroes. |
| - | Pad to the right rather than the left. |
| \* | Dynamic padding, expects additional integer parameter to set padding or precision after ., see dynamic padding. |

### Padding

The `.` (_dot_), `*` (_asterisk_), `-` (_minus sign_) and digit (`0`-`9`) characters are used for padding. This allows printing several values aligned vertically as if in a column, provided a fixed-width font is used.

To pad a string to a minimum length, add an integer to the specifier:

```gdscript
print("%10d" % 12345)
# output: "     12345"
# 5 leading spaces for a total length of 10
```

If the integer starts with `0`, integer values are padded with zeroes instead of white space:

```gdscript
print("%010d" % 12345)
# output: "0000012345"
```

Precision can be specified for real numbers by adding a `.` (_dot_) with an integer following it. With no integer after `.`, a precision of 0 is used, rounding to integer values. The integer to use for padding must appear before the dot.

```gdscript
# Pad to minimum length of 10, round to 3 decimal places
print("%10.3f" % 10000.5555)
# Output: " 10000.556"
# 1 leading space
```

The `-` character will cause padding to the right rather than the left, useful for right text alignment:

```gdscript
print("%-10d" % 12345678)
# Output: "12345678  "
# 2 trailing spaces
```

#### Dynamic padding

By using the `*` (_asterisk_) character, the padding or precision can be set without modifying the format string. It is used in place of an integer in the format specifier. The values for padding and precision are then passed when formatting:

```gdscript
var format_string = "%*.*f"
# Pad to length of 7, round to 3 decimal places:
print(format_string % [7, 3, 8.8888])
# Output: "  8.889"
# 2 leading spaces
```

It is still possible to pad with zeroes in integer placeholders by adding `0` before `*`:

```gdscript
print("%0*d" % [2, 3])
# Output: "03"
```

### Escape sequence

To insert a literal `%` character into a format string, it must be escaped to avoid reading it as a placeholder. This is done by doubling the character:

```gdscript
var health = 56
print("Remaining health: %d%%" % health)
# Output: "Remaining health: 56%"
```

### String format method

There is also another way to format text in GDScript, namely the [String.format()](../godot_gdscript_misc.md) method. It replaces all occurrences of a key in the string with the corresponding value. The method can handle arrays or dictionaries for the key/value pairs.

Arrays can be used as key, index, or mixed style (see below examples). Order only matters when the index or mixed style of Array is used.

A quick example in GDScript:

```gdscript
# Define a format string
var format_string = "We're waiting for {str}"

# Using the 'format' method, replace the 'str' placeholder
var actual_string = format_string.format({"str": "Godot"})

print(actual_string)
# Output: "We're waiting for Godot"
```

#### Format method examples

The following are some examples of how to use the various invocations of the `String.format()` method.

| Type | Style | Example | Result |
| Dictionary | key | "Hi, {name} v{version}!".format({"name":"Godette", "version":"3.0"}) | Hi, Godette v3.0! |
| Dictionary | index | "Hi, {0} v{1}!".format({"0":"Godette", "1":"3.0"}) | Hi, Godette v3.0! |
| Dictionary | mix | "Hi, {0} v{version}!".format({"0":"Godette", "version":"3.0"}) | Hi, Godette v3.0! |
| Array | key | "Hi, {name} v{version}!".format([["version","3.0"], ["name","Godette"]]) | Hi, Godette v3.0! |
| Array | index | "Hi, {0} v{1}!".format(["Godette","3.0"]) | Hi, Godette v3.0! |
| Array | mix | "Hi, {name} v{0}!".format(["3.0", ["name","Godette"]]) | Hi, Godette v3.0! |
| Array | no index | "Hi, {} v{}!".format(["Godette", "3.0"], "{}") | Hi, Godette v3.0! |

Placeholders can also be customized when using `String.format`, here's some examples of that functionality.

| Type | Example | Result |
| Infix (default) | "Hi, {0} v{1}".format(["Godette", "3.0"], "{_}") | Hi, Godette v3.0 |
| Postfix | "Hi, 0% v1%".format(["Godette", "3.0"], "_%") | Hi, Godette v3.0 |
| Prefix | "Hi, %0 v%1".format(["Godette", "3.0"], "%\_") | Hi, Godette v3.0 |

Combining both the `String.format` method and the `%` operator could be useful, as `String.format` does not have a way to manipulate the representation of numbers.

| Example | Result |
| "Hi, {0} v{version}".format({0:"Godette", "version":"%0.2f" % 3.114}) | Hi, Godette v3.11 |

### String concatenation

You can also combine strings by _concatenating_ them together, using the `+` operator.

```gdscript
# Define a base string
var base_string = "We're waiting for "

# Concatenate the string
var actual_string = base_string + "Godot"

print(actual_string)
# Output: "We're waiting for Godot"
```

When using string concatenation, values that are not strings must be converted using the `str()` function. There is no way to specify the string format of converted values.

```gdscript
var name_string = "Godette"
var version = 3.0
var actual_string = "Hi, " + name_string + " v" + str(version) + "!"

print(actual_string)
# Output: "Hi, Godette v3!"
```

Because of these limitations, format strings or the `format()` method are often a better choice. In many cases, string concatenation is also less readable.

> **Note:** In Godot's C++ code, GDScript format strings can be accessed using the `vformat()` helper function in the [Variant](../godot_gdscript_misc.md) header.

---
