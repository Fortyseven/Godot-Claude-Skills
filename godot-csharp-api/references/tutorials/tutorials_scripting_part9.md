# Godot 4 C# Tutorials — Scripting (Part 9)

> 4 tutorials. C#-specific code examples.

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

Alternatively, you can use inline documentation comments:

The script documentation will update in the editor help window every time the script is updated. If any member variable or function name starts with an underscore, it will be treated as private. It will not appear in the documentation and will be ignored in the help window.

### Complete script example

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

By default, `[codeblock]` highlights GDScript syntax. You can change it using the `lang` attribute. Currently supported options are:

- `[codeblock lang=text]` disables syntax highlighting;
- `[codeblock lang=gdscript]` highlights GDScript syntax;
- `[codeblock lang=csharp]` highlights C# syntax (only in .NET version).

---

## GDScript exported properties

In Godot, class members can be exported. This means their value gets saved along with the resource (such as the [scene](../godot_csharp_misc.md)) they're attached to, and get transferred over when using [RPCs](tutorials_networking.md). They will also be available for editing in the property editor. Exporting is done by using the `@export` annotation.

In that example the value `5` will be saved and visible in the property editor.

An exported variable must be initialized to a constant expression or have a type specifier in the variable. Some of the export annotations have a specific type and don't need the variable to be typed (see the _Examples_ section below).

One of the fundamental benefits of exporting member variables is to have them visible and editable in the editor. This way, artists and game designers can modify values that later influence how the program runs. For this, a special export syntax is provided. Additionally, documentation comments can be used for tooltip descriptions, visible on mouse over.

> **Note:** Exporting properties can also be done in other languages such as C#. The syntax varies depending on the language. See C# exported properties for information on C# exports.

### Basic use

If the exported value assigns a constant or constant expression, the type will be inferred and used in the editor.

If there's no default value, you can add a type to the variable.

Resources and nodes can be exported.

Even if a script is not executed in the editor, exported properties can still be edited. However, getters and setters will only be used if the script is in Tool mode.

### Grouping exports

It is possible to group your exported properties inside the Inspector with the `@export_group` annotation. Every exported property after this annotation will be added to the group. Start a new group or use `@export_group("")` to break out.

The second argument of the annotation can be used to only group properties with the specified prefix.

Groups cannot be nested, use `@export_subgroup` to create subgroups within a group.

You can also change the name of your main category, or create additional categories in the property list with the `@export_category` annotation.

> **Note:** The list of properties is organized based on the class inheritance and new categories break that expectation. Use them carefully, especially when creating projects for public use.

### Strings as paths

String as a path to a file. See `@export_file`.

String as a path to a directory. See `@export_dir`.

String as a path to a file, custom filter provided as hint. See again `@export_file`.

Using paths in the global filesystem is also possible, but only in scripts in tool mode.

String as a path to a PNG file in the global filesystem. See `@export_global_file`.

String as a path to a directory in the global filesystem. See `@export_global_dir`.

The multiline annotation tells the editor to show a large input field for editing over multiple lines. See `@export_multiline`.

### Limiting editor input ranges

See `@export_range` for all of the following.

Allow integer values from 0 to 20.

Allow integer values from -10 to 20.

Allow floats from -10 to 20 and snap the value to multiples of 0.2.

The limits can be made to affect only the slider if you add the hints `"or_less"` and/or `"or_greater"`. If either these hints are used, it will be possible for the user to enter any value or drag the value with the mouse when not using the slider, even if outside the specified range.

The `"exp"` hint can be used to make a value have an exponential slider instead of a linear slider. This means that when dragging the slider towards the right, changes will become progressively faster when dragging the mouse. This is useful to make editing values that can be either very small or very large easier, at the cost of being less intuitive.

For values that are meant to represent an easing factor, use **Floats with easing hint** instead.

The `"hide_slider"` hint can be used to hide the horizontal bar that appears below `float` properties, or the up/down arrows that appear besides `int` properties:

### Adding suffixes and handling degrees/radians

A suffix can also be defined to make the value more self-explanatory in the inspector. For example, to define a value that is meant to be configured as "meters" (`m`) by the user:

For angles that are stored in radians but displayed as degrees to the user, use the "radians_as_degrees" hint:

This performs automatic conversion when the value is displayed or modified in the inspector and also displays a degree (`°`) suffix. This approach is used by Godot's own rotation properties throughout the editor.

If the angle is stored in degrees instead, use the "degrees" hint to display the degree symbol while disabling the automatic degrees-to-radians conversion when the value is modified from the inspector.

### Floats with easing hint

Display a visual representation of the `ease()` function when editing. See `@export_exp_easing`.

### Colors

Regular color given as red-green-blue-alpha value.

Color given as red-green-blue value (alpha will always be 1). See `@export_color_no_alpha`.

### Nodes

Nodes can also be directly exported as properties in a script without having to use NodePaths:

Exporting NodePaths like in Godot 3.x is still possible, in case you need it:

If you want to limit the types of nodes for NodePaths, you can use the `@export_node_path` annotation:

### Resources

In the Inspector, you can then drag and drop a resource file from the FileSystem dock into the variable slot.

Opening the inspector dropdown may result in an extremely long list of possible classes to create, however. Therefore, if you specify an extension of Resource such as:

The drop-down menu will be limited to AnimationNode and all its derived classes.

### Exporting bit flags

See `@export_flags`.

Integers used as bit flags can store multiple `true`/`false` (boolean) values in one property. By using the `@export_flags` annotation, they can be set from the editor:

You must provide a string description for each flag. In this example, `Fire` has value 1, `Water` has value 2, `Earth` has value 4 and `Wind` corresponds to value 8. Usually, constants should be defined accordingly (e.g. `const ELEMENT_WIND = 8` and so on).

You can add explicit values using a colon:

Only power of 2 values are valid as bit flags options. The lowest allowed value is 1, as 0 means that nothing is selected. You can also add options that are a combination of other flags:

Export annotations are also provided for the physics, render, and navigation layers defined in the project settings:

Using bit flags requires some understanding of bitwise operations. If in doubt, use boolean variables instead.

### Exporting enums

See `@export_enum`.

Properties can be exported with a type hint referencing an enum to limit their values to the values of the enumeration. The editor will create a widget in the Inspector, enumerating the following as "Thing 1", "Thing 2", "Another Thing". The value will be stored as an integer.

Integer and string properties can also be limited to a specific list of values using the `@export_enum` annotation. The editor will create a widget in the Inspector, enumerating the following as Warrior, Magician, Thief. The value will be stored as an integer, corresponding to the index of the selected option (i.e. `0`, `1`, or `2`).

You can add explicit values using a colon:

If the type is String, the value will be stored as a string.

If you want to set an initial value, you must specify it explicitly:

### Exporting arrays

Exported arrays can have initializers, but they must be constant expressions.

If the exported array specifies a type which inherits from Resource, the array values can be set in the inspector by dragging and dropping multiple files from the FileSystem dock at once.

The default value **must** be a constant expression.

Exported arrays can specify type (using the same hints as before).

You can omit the default value, but it would then be `null` if not assigned.

Arrays with specified types which inherit from resource can be set by drag-and-dropping multiple files from the FileSystem dock.

Packed type arrays also work, but only initialized empty:

Other export variants can also be used when exporting arrays:

### @export_storage

See `@export_storage`.

By default, exporting a property has two effects:

1. makes the property stored in the scene/resource file (`PROPERTY_USAGE_STORAGE`);
2. adds a field to the Inspector (`PROPERTY_USAGE_EDITOR`).

However, sometimes you may want to make a property serializable, but not display it in the editor to prevent unintentional changes and cluttering the interface.

To do this you can use `@export_storage`. This can be useful for `@tool` scripts. Also the property value is copied when [Resource.duplicate()](../godot_csharp_core.md) or [Node.duplicate()](../godot_csharp_misc.md) is called, unlike non-exported variables.

### @export_custom

If you need more control than what's exposed with the built-in `@export` annotations, you can use `@export_custom` instead. This allows defining any property hint, hint string and usage flags, with a syntax similar to the one used by the editor for built-in nodes.

For example, this exposes the `altitude` property with no range limits but an `m` (meter) suffix defined:

The above is normally not feasible with the standard `@export_range` syntax, since it requires defining a range.

See the `class reference` for a list of parameters and their allowed values.

> **Warning:** When using `@export_custom`, GDScript does not perform any validation on the syntax. Invalid syntax may have unexpected behavior in the inspector.

### @export_tool_button

If you need to create a clickable inspector button, you can use `@export_tool_button`. This exports a `Callable` property as a clickable button. When the button is pressed, the callable is called.

You can specify a custom icon name, which must match one of the icon file names from the [editor/icons](https://github.com/godotengine/godot/tree/master/editor/icons) folder of the Godot source repository (case-sensitive). You can also browse the editor icons using the [Godot editor icons](https://godot-editor-icons.github.io/) website.

For example, if you wish to use `Node2D.svg` from that folder, you must specify `"Node2D"` as the second parameter of `@export_tool_button`. It is not currently possible to use custom icons from the project folder; only built-in editor icons can be used.

This exports a button with label `"Hello"` and icon `"Callable"` (which is the default if no icon is specified). When you press it, it will print `"Hello world!"`.

### Setting exported variables from a tool script

When changing an exported variable's value from a script in Tool mode, the value in the inspector won't be updated automatically. To update it, call [notify_property_list_changed()](../godot_csharp_misc.md) after setting the exported variable's value.

### Reading an exported variable's value early on

If you read an exported variable's value in [\_init()](../godot_csharp_misc.md), it will return the default value specified in the export annotation instead of the value that was set in the inspector. This is because assigning values from the saved scene/resource file occurs _after_ object initialization; until then, the default value is used.

To get the value that was set in the inspector (and therefore saved in the scene/resource file), you need to read it _after_ the object is constructed, such as in [Node.\_ready()](../godot_csharp_misc.md). You can also read the value in a setter that's defined on the exported property, which is useful in custom resources where `_ready()` is not available:

Results in:

```none
Initial value: 2
Inspector-set value: 3
```

### Advanced exports

Not every type of export can be provided on the level of the language itself to avoid unnecessary design complexity. The following describes some more or less common exporting features which can be implemented with a low-level API.

Before reading further, you should get familiar with the way properties are handled and how they can be customized with [\_set()](../godot_csharp_misc.md), [\_get()](../godot_csharp_misc.md), and [\_get_property_list()](../godot_csharp_misc.md) methods as described in [Accessing data or logic from an object](tutorials_best_practices.md).

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

Placeholders always start with a `%`, but the next character or characters, the _format specifier_, determines how the given value is converted to a string.

The `%s` seen in the example above is the simplest placeholder and works for most use cases: it converts the value by the same method by which an implicit String conversion or `str()` would convert it. Strings remain unchanged, booleans turn into either `"True"` or `"False"`, an `int` or `float` becomes a decimal, and other types usually return their data in a human-readable string.

There are other **format specifiers**.

### Multiple placeholders

Format strings may contain multiple placeholders. In such a case, the values are handed in the form of an array, one value per placeholder (unless using a format specifier with `*`, see **dynamic padding**):

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

If the integer starts with `0`, integer values are padded with zeroes instead of white space:

Precision can be specified for real numbers by adding a `.` (_dot_) with an integer following it. With no integer after `.`, a precision of 0 is used, rounding to integer values. The integer to use for padding must appear before the dot.

The `-` character will cause padding to the right rather than the left, useful for right text alignment:

#### Dynamic padding

By using the `*` (_asterisk_) character, the padding or precision can be set without modifying the format string. It is used in place of an integer in the format specifier. The values for padding and precision are then passed when formatting:

It is still possible to pad with zeroes in integer placeholders by adding `0` before `*`:

### Escape sequence

To insert a literal `%` character into a format string, it must be escaped to avoid reading it as a placeholder. This is done by doubling the character:

### String format method

There is also another way to format text in GDScript, namely the [String.format()](../godot_csharp_misc.md) method. It replaces all occurrences of a key in the string with the corresponding value. The method can handle arrays or dictionaries for the key/value pairs.

Arrays can be used as key, index, or mixed style (see below examples). Order only matters when the index or mixed style of Array is used.

A quick example in GDScript:

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

When using string concatenation, values that are not strings must be converted using the `str()` function. There is no way to specify the string format of converted values.

Because of these limitations, format strings or the `format()` method are often a better choice. In many cases, string concatenation is also less readable.

> **Note:** In Godot's C++ code, GDScript format strings can be accessed using the `vformat()` helper function in the [Variant](../godot_csharp_misc.md) header.

---

## GDScript style guide

This style guide lists conventions to write elegant GDScript. The goal is to encourage writing clean, readable code and promote consistency across projects, discussions, and tutorials. Hopefully, this will also support the development of auto-formatting tools.

Since GDScript is close to Python, this guide is inspired by Python's [PEP 8](https://www.python.org/dev/peps/pep-0008/) programming style guide.

Style guides aren't meant as hard rulebooks. At times, you may not be able to apply some of the guidelines below. When that happens, use your best judgment, and ask fellow developers for insights.

In general, keeping your code consistent in your projects and within your team is more important than following this guide to a tee.

> **Note:** Godot's built-in script editor uses a lot of these conventions by default. Let it help you.

Here is a complete class example based on these guidelines:

### Formatting

#### Encoding and special characters

- Use line feed (**LF**) characters to break lines, not CRLF or CR. _(editor default)_
- Use one line feed character at the end of each file. _(editor default)_
- Use **UTF-8** encoding without a [byte order mark](https://en.wikipedia.org/wiki/Byte_order_mark). _(editor default)_
- Use **Tabs** instead of spaces for indentation. _(editor default)_

#### Indentation

Each indent level should be one greater than the block containing it.

**Good**:

**Bad**:

Use 2 indent levels to distinguish continuation lines from regular code blocks.

**Good**:

**Bad**:

Exceptions to this rule are arrays, dictionaries, and enums. Use a single indentation level to distinguish continuation lines:

**Good**:

**Bad**:

#### Trailing comma

Use a trailing comma on the last line in arrays, dictionaries, and enums. This results in easier refactoring and better diffs in version control as the last line doesn't need to be modified when adding new elements.

**Good**:

**Bad**:

Trailing commas are unnecessary in single-line lists, so don't add them in this case.

**Good**:

**Bad**:

#### Blank lines

Surround functions and class definitions with two blank lines:

Use one blank line inside functions to separate logical sections.

> **Note:** We use a single line between classes and function definitions in the class reference and in short code snippets in this documentation.

#### Line length

Keep individual lines of code under 100 characters.

If you can, try to keep lines under 80 characters. This helps to read the code on small displays and with two scripts opened side-by-side in an external text editor. For example, when looking at a differential revision.

#### One statement per line

Avoid combining multiple statements on a single line, including conditional statements, to adhere to the GDScript style guidelines for readability.

**Good**:

**Bad**:

The only exception to that rule is the ternary operator:

#### Format multiline statements for readability

When you have particularly long `if` statements or nested ternary expressions, wrapping them over multiple lines improves readability. Since continuation lines are still part of the same expression, 2 indent levels should be used instead of one.

GDScript allows wrapping statements using multiple lines using parentheses or backslashes. Parentheses are favored in this style guide since they make for easier refactoring. With backslashes, you have to ensure that the last line never contains a backslash at the end. With parentheses, you don't have to worry about the last line having a backslash at the end.

When wrapping a conditional expression over multiple lines, the `and`/`or` keywords should be placed at the beginning of the line continuation, not at the end of the previous line.

**Good**:

**Bad**:

#### Avoid unnecessary parentheses

Avoid parentheses in expressions and conditional statements. Unless necessary for order of operations or wrapping over multiple lines, they only reduce readability.

**Good**:

**Bad**:

#### Boolean operators

Prefer the plain English versions of boolean operators, as they are the most accessible:

- Use `and` instead of `&&`.
- Use `or` instead of `||`.
- Use `not` instead of `!`.

You may also use parentheses around boolean operators to clear any ambiguity. This can make long expressions easier to read.

**Good**:

**Bad**:

#### Comment spacing

Regular comments (`#`) and documentation comments (`##`) should start with a space, but not code that you comment out. Additionally, code region comments (`#region`/`#endregion`) must follow that precise syntax, so they should not start with a space.

Using a space for regular and documentation comments helps differentiate text comments from disabled code.

**Good**:

**Bad**:

> **Note:** In the script editor, to toggle commenting of the selected code, press Ctrl + K. This feature adds/removes a single `#` sign before any code on the selected lines.

Prefer writing comments on their own line as opposed to inline comments (comments written on the same line as code). Inline comments are best used for short comments, typically a few words at most:

**Good**:

**Bad**:

#### Whitespace

Always use one space around operators and after commas. Also, avoid extra spaces in dictionary references and function calls. One exception to this is for single-line dictionary declarations, where a space should be added after the opening brace and before the closing brace. This makes the dictionary easier to visually distinguish from an array, as the `[]` characters look close to `{}` with most fonts.

**Good**:

**Bad**:

Don't use spaces to align expressions vertically:

#### Quotes

Use double quotes unless single quotes make it possible to escape fewer characters in a given string. See the examples below:

#### Numbers

Don't omit the leading or trailing zero in floating-point numbers. Otherwise, this makes them less readable and harder to distinguish from integers at a glance.

**Good**:

**Bad**:

Use lowercase for letters in hexadecimal numbers, as their lower height makes the number easier to read.

**Good**:

**Bad**:

Take advantage of GDScript's underscores in literals to make large numbers more readable.

**Good**:

**Bad**:

### Naming conventions

These naming conventions follow the Godot Engine style. Breaking these will make your code clash with the built-in naming conventions, leading to inconsistent code. As a summary table:

| Type         | Convention    | Example                   |
| ------------ | ------------- | ------------------------- |
| File names   | snake_case    | yaml_parser.gd            |
| Class names  | PascalCase    | class_name YAMLParser     |
| Node names   | PascalCase    | Camera3D, Player          |
| Functions    | snake_case    | func load_level():        |
| Variables    | snake_case    | var particle_effect       |
| Signals      | snake_case    | signal door_opened        |
| Constants    | CONSTANT_CASE | const MAX_SPEED = 200     |
| Enum names   | PascalCase    | enum Element              |
| Enum members | CONSTANT_CASE | {EARTH, WATER, AIR, FIRE} |

#### File names

Use snake_case for file names. For named classes, convert the PascalCase class name to snake_case:

This is consistent with how C++ files are named in Godot's source code. This also avoids case sensitivity issues that can crop up when exporting a project from Windows to other platforms.

#### Classes and nodes

Use PascalCase for class and node names:

Also use PascalCase when loading a class into a constant or a variable:

#### Functions and variables

Use snake_case to name functions and variables:

Prepend a single underscore (\_) to virtual methods functions the user must override, private functions, and private variables:

#### Signals

Use the past tense to name signals:

#### Constants and enums

Write constants with CONSTANT*CASE, that is to say in all caps with an underscore (*) to separate words:

Use PascalCase for enum _names_ and keep them singular, as they represent a type. Use CONSTANT_CASE for their members, as they are constants:

Write enums with each item on its own line. This allows adding documentation comments above each item more easily, and also makes for cleaner diffs in version control when items are added or removed.

**Good**:

**Bad**:

### Code order

This section focuses on code order. For formatting, see **Formatting**. For naming conventions, see **Naming conventions**.

We suggest to organize GDScript code this way:

And put the class methods and variables in the following order depending on their access modifiers:

We optimized the order to make it easy to read the code from top to bottom, to help developers reading the code for the first time understand how it works, and to avoid errors linked to the order of variable declarations.

This code order follows four rules of thumb:

1. Properties and signals come first, followed by methods.
2. Public comes before private.
3. Virtual callbacks come before the class's interface.
4. The object's construction and initialization functions, `_init` and `_ready`, come before functions that modify the object at runtime.

#### Class declaration

If the code is meant to run in the editor, place the `@tool` annotation on the first line of the script.

Follow with the optional `@icon` then the `class_name` if necessary. You can turn a GDScript file into a global type in your project using `class_name`. For more information, see Registering named classes. If the class is meant to be an abstract class, add `@abstract` _before_ the `class_name` keyword.

Then, add the `extends` keyword if the class extends a built-in type.

Following that, you should have the class's optional documentation comments. You can use that to explain the role of your class to your teammates, how it works, and how other developers should use it, for example.

For inner classes, use single-line declarations:

#### Signals and properties

Write signal declarations, followed by properties, that is to say, member variables, after the docstring.

Enums should come after signals, as you can use them as export hints for other properties.

Then, write constants, exported variables, public, private, and onready variables, in that order.

> **Note:** GDScript evaluates `@onready` variables right before the `_ready` callback. You can use that to cache node dependencies, that is to say, to get child nodes in the scene that your class relies on. This is what the example above shows.

#### Member variables

Don't declare member variables if they are only used locally in a method, as it makes the code more difficult to follow. Instead, declare them as local variables in the method's body.

#### Local variables

Declare local variables as close as possible to their first use. This makes it easier to follow the code, without having to scroll too much to find where the variable was declared.

#### Methods and static functions

After the class's properties come the methods.

Start with the `_init()` callback method, that the engine will call upon creating the object in memory. Follow with the `_ready()` callback, that Godot calls when it adds a node to the scene tree.

These functions should come first because they show how the object is initialized.

Other built-in virtual callbacks, like `_unhandled_input()` and `_physics_process`, should come next. These control the object's main loop and interactions with the game engine.

The rest of the class's interface, public and private methods, come after that, in that order.

### Static typing

GDScript supports optional static typing.

#### Declared types

To declare a variable's type, use `<variable>: <type>`:

To declare the return type of a function, use `-> <type>`:

#### Inferred types

In most cases, you can let the compiler infer the type using `:=`. Prefer `:=` when the type is written on the same line as the assignment, otherwise prefer writing the type explicitly.

**Good**:

Include the type hint when the type is ambiguous, and omit the type hint when it's redundant.

**Bad**:

In some cases, the type must be stated explicitly, otherwise the behavior will not be as expected because the compiler will only be able to use the function's return type. For example, `get_node()` cannot infer a type unless the scene or file of the node is loaded in memory. In this case, you should set the type explicitly.

**Good**:

**Bad**:

Alternatively, you can use the `as` keyword to cast the return type, and that type will be used to infer the type of the var.

> **Note:** This option is considered more type-safe than type hints, but also less null-safe as it silently casts the variable to `null` in case of a type mismatch at runtime, without an error/warning.

---
