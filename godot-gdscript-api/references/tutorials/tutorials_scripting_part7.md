# Godot 4 GDScript Tutorials — Scripting (Part 7)

> 4 tutorials. GDScript-specific code examples.

## The .gdextension file

### Introduction

The `.gdextension` file in your project contains the instructions for how to load the GDExtension. The instructions are separated into specific sections. This page should give you a quick overview of the different options available to you. For an introduction how to get started with C++ (godot-cpp), take a look at the GDExtension C++ Example.

### Configuration section

| Property              | Type    | Description                                                                                                                                                                                                                                            |
| --------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| entry_symbol          | String  | Name of the entry function for initializing the GDExtension. This function should be defined in the register_types.cpp file when using godot-cpp. Adding this is necessary for the extension to work.                                                  |
| compatibility_minimum | String  | Minimum compatible version. This prevents older versions of Godot from loading extensions that depend on features from newer versions of Godot. Only supported in Godot 4.1 or later                                                                   |
| compatibility_maximum | String  | Maximum compatible version. This prevents newer versions of Godot from loading the extension. Only supported in Godot 4.3 or later                                                                                                                     |
| reloadable            | Boolean | Reloads the extension upon recompilation. Reloading is supported for the godot-cpp binding in Godot 4.2 or later. Other language bindings may or may not support it as well. This flag should be mainly used for developing or debugging an extension. |
| android_aar_plugin    | Boolean | The GDExtension is part of a v2 Android plugin. During export this flag will indicate to the editor that the GDExtension native shared libraries are exported by the Android plugin AAR binaries.                                                      |

### Libraries section

In this section you can set the paths to the compiled binaries of your GDExtension libraries. By specifying feature flags you can filter which version should be loaded and exported with your game depending on which feature flags are active. Every feature flag must match to Godot's feature flags or your custom export flags to be loaded in an exported game. For instance `macos.debug` means that it will be loaded if Godot has both the `macos` and `debug` flag active. Each line of the section is evaluated from top to bottom.

Here is an example of what that can look like:

```none
; A comment line starts with a semicolon. This line is ignored by the engine.
[libraries]

macos.debug = "./bin/libgdexample.macos.template_debug.dylib" ; Inline comments are also allowed.
macos.release = "./bin/libgdexample.macos.template_release.dylib"
windows.debug.x86_32 = "./bin/libgdexample.windows.template_debug.x86_32.dll"
windows.release.x86_32 = "./bin/libgdexample.windows.template_release.x86_32.dll"
windows.debug.x86_64 = "./bin/libgdexample.windows.template_debug.x86_64.dll"
windows.release.x86_64 = "./bin/libgdexample.windows.template_release.x86_64.dll"
linux.debug.x86_64 = "./bin/libgdexample.linux.template_debug.x86_64.so"
linux.release.x86_64 = "./bin/libgdexample.linux.template_release.x86_64.so"
linux.debug.arm64 = "./bin/libgdexample.linux.template_debug.arm64.so"
linu
# ...
```

Paths can be relative or absolute (starting with `res://`). Relative paths are recommended, as they allow the extension to keep working if it's installed to a different folder than what's specified in the path.

Entries are matched in order, so if two sets of feature tags could match the same system, be sure to put the more specific ones first:

```none
[libraries]

linux.release.editor.x86_64 = "./bin/libgdexample.linux.template_release.x86_64.so"
linux.release.x86_64 = "./bin/libgdexample.linux.noeditor.template_release.x86_64.so"
```

Here are lists of some of the available built-in options (for more look at the [feature tags](tutorials_export.md)):

#### Running system

| Flag     | Description                   |
| -------- | ----------------------------- |
| windows  | Windows operating system      |
| macos    | Mac operating system          |
| linux    | Linux operating system        |
| bsd      | BSD operating system          |
| linuxbsd | Linux or BSD operating system |
| android  | Android operating system      |
| ios      | iOS operating system          |
| web      | Web browser                   |

#### Build

| Flag    | Description                                                                  |
| ------- | ---------------------------------------------------------------------------- |
| debug   | Build with debugging features (editor builds always have debugging features) |
| release | Optimized build without debugging features                                   |
| editor  | Editor build                                                                 |

#### Architecture

| Flag   | Description                |
| ------ | -------------------------- |
| double | double-precision build     |
| single | single-precision build     |
| x86_64 | 64-bit x86 build           |
| arm64  | 64-bit ARM build           |
| rv64   | 64-bit RISC-V build        |
| riscv  | RISC-V build (any bitness) |
| wasm32 | 32-bit WebAssembly build   |

### Icons section

By default, Godot uses the Node icon in the scene dock for GDExtension nodes. A custom icon can be set by reference to its name and resource path of an SVG file.

For example:

```none
[icons]

GDExample = "res://icons/gd_example.svg"
```

The path should point to a 16×16 pixel SVG image, with two options enabled on the image in the Import dock:

- **Editor > Scale with Editor Scale**.
- **Editor > Convert Colors with Editor Theme**.

Enabling both options ensures the icon behaves as closely as possible to the stock editor icons. Read the guide for [creating icons](tutorials_editor.md) for more information.

### Dependencies section

In this section, you set the paths of the GDExtension dependencies. This is used internally to export the dependencies when exporting your game executable. You are able to set which dependency is loaded depending on the feature flags of the exported executable. In addition, you are able to set an optional subdirectory to move your dependencies into. If no path is supplied, Godot will move the libraries into the same directory as your game executable.

> **Warning:** On macOS, it is necessary to have shared libraries inside a folder called `Frameworks` with a directory structure like this: `Game.app/Contents/Frameworks`.

```none
[dependencies]

macos.debug = {
    "res://bin/libdependency.macos.template_debug.framework" : "Contents/Frameworks"
}
macos.release = {
    "res://bin/libdependency.macos.template_release.framework" : "Contents/Frameworks"
}
windows.debug = {
    "res://bin/libdependency.windows.template_debug.x86_64.dll" : "",
    "res://bin/libdependency.windows.template_debug.x86_32.dll" : ""
}
windows.release = {
    "res://bin/libdependency.windows.template_release.x86_64.dll" : "",
    "res://bin/libdependency.windows.template_release.x86_32.dll" : ""
}
linux.debug = {
    "res://bin/libdependency.linux.template_debug.x86_64.so" : "",
    "res://bin/libdependency.linux.template_debug.arm64.so" : "",
    "res://bin/libdependency.linux.template_debug.rv64.so" : ""
}
linux.release = {
    "res://bin/li
# ...
```

---

## The C interface JSON file

The `gdextension_interface.json` file is the "source of truth" for the C API that Godot uses to communicate with GDExtensions.

You can use the Godot executable to dump the file by using the following command:

```shell
godot --headless --dump-gdextension-interface-json
```

This file is intended to be used by GDExtension language bindings to generate code for using this API in whatever form makes the most sense for that language.

> **Note:** This is not to be confused with the `extension_api.json`, which is also used by GDExtension language bindings, and contains information about the classes and methods that are exposed by Godot. The `gdextension_interface.json` is more low-level, and is used to interact with those higher-level classes and methods.

For languages that can be extended via C, or provide tools for interacting with C code, it's also possible to use the Godot executable to dump a generated C header file:

```shell
godot --headless --dump-gdextension-interface
```

> **Note:** The header file is compatible with earlier versions of the header file that were included with Godot 4.5 and earlier, which means it preserves some typos in names in order to ensure compatibility.

The goal of this page is to explain the JSON format for the GDExtension language bindings that would like to do their own code generation from the JSON.

### Overall structure

The JSON file is broken up into 3 sections:

- The header, which includes some miscellaneous information at the top-level of the JSON file.
- The `types` key, which defines all the types used in the GDExtension interface.
- The `interface` key, which defines all the function pointers that can be loaded via the `GDExtensionInterfaceGetProcAddress` function pointer, which is passed to all GDExtensions when they are loaded.

There is a complete [JSON schema](https://github.com/godotengine/godot/blob/master/core/extension/gdextension_interface.schema.json) included in Godot's source code.

Even though we may add new types and interface functions with each minor release of Godot, we strive to **never** change them in a backwards incompatible way, or remove them. Every interface function is labeled with the version of Godot it was introduced in (the `since` key), so you can always use the latest version of the file, and simply refrain from using anything in versions of Godot that are newer than the version you are targeting.

### Header

The "header" is made up of 3 miscellaneous keys at the top-level of the file:

- `_copyright`: The standard copyright and license text that Godot includes in all source code files.
- `$schema`: Points to the JSON schema relative to this file. It can be useful to place the schema in the same directory, if you're viewing it with a code editor that understands JSON schema.
- `format_version`: An integer for the version of the file format (meaning the schema). Right now, there is only one format version (`1`). If we ever change the file format in an incompatible way, we will increment this number. This _doesn't_ reflect the version of the data in the file (so it won't change between Godot versions), only its format. Hopefully, we'll never have to use it, but it allows code generators to error early if they encounter an unexpected value here.

### Types

The `types` section is an array of types that will be used by other types, and the interface functions that will be in the last section.

The types should be evaluated in order. Later types may refer to earlier types, but earlier types will not refer to later types.

There is a small set of built-in types which aren't explicitly listed in the JSON:

- `void`
- `int8_t`
- `uint8_t`
- `int16_t`
- `uint16_t`
- `int32_t`
- `uint32_t`
- `int64_t`
- `uint64_t`
- `size_t` (`uint32_t` on 32-bit architectures, and `uint64_t` on 64-bit architectures)
- `char`
- `char16_t`
- `char32_t`
- `wchar_t`
- `float`
- `double`

These correspond to their equivalent C types.

Additionally, types can include modifiers such as:

- `*` (e.g. `int8_t*`) to indicate a pointer to the type
- `const` (e.g. `const int8_t*`) to indicate a const type

Each type defined in the JSON file falls into one of 5 "kinds":

- `enum`
- `handle`
- `alias`
- `struct`
- `function`

Regardless of the "kind", all types can have the following keys:

- `kind` (required): The type's "kind".
- `name` (required): The name of the type, which could be used as a valid C identifier.
- `description`: An array of strings documenting the type, where each string is a line of documentation (this format for `description` is used throughout the JSON file).
- `deprecated`: An object with its own keys for the Godot version the type was deprecated in (`since`), a message explaining the deprecation (`message`), and optionally a replacement to use instead (`replacement`).

#### Enums

Enums are 32-bit integers with a fixed set of possible values. In C, they could be represented as an `enum`.

They have the following keys:

- `is_bitfield`: If true, this enum is a bitfield, where the enum values can be bitwise OR'd together. It is false by default.
- `values`: The array of fixed values for this enum, each with a `name`, `value`, and `description`.

An enum should be represented as an `int32_t`, unless `is_bitfield` is true, in which case a `uint32_t` should be used.

##### Example

```json
{
    "name": "GDExtensionInitializationLevel",
    "kind": "enum",
    "values": [
        {
            "name": "GDEXTENSION_INITIALIZATION_CORE",
            "value": 0
        },
        {
            "name": "GDEXTENSION_INITIALIZATION_SERVERS",
            "value": 1
        },
        {
            "name": "GDEXTENSION_INITIALIZATION_SCENE",
            "value": 2
        },
        {
            "name": "GDEXTENSION_INITIALIZATION_EDITOR",
            "value": 3
        },
        {
            "name": "GDEXTENSION_MAX_INITIALIZATION_LEVEL",
            "value": 4
        }
    ]
}
```

#### Handles

Handles are pointers to opaque structs. In C, they could be represented as `void *` or `struct{} *`.

They have the following keys:

- `is_const`: If true, this handle type is to be treated as a "const pointer", meaning its internal data will not be changed. It is false by default.
- `is_uninitialized`: If true, this handle type is to be treated as pointing to uninitialized memory (which may be initialized using interface functions). It is false by default.
- `parent`: The optional name of another handle type, if this handle type is the const or uninitialized version of the parent type. This only makes sense if either `is_const` or `is_uninitialized` is true.

Handles are the size of pointers on the given architecture (so, 64-bit on x86_64 and 32-bit on x86_32, for example).

##### Example

```json
{
    "name": "GDExtensionStringNamePtr",
    "kind": "handle"
}
```

#### Aliases

Aliases are alternative names for a type. In C, they could be represented as a `typedef`.

They have only one additional key:

- `type`: The type the alias is an alternative name for. It may include modifiers as described above.

These should be represented using the same C type as the type they refer to.

##### Example

```json
{
    "name": "GDExtensionInt",
    "kind": "alias",
    "type": "int64_t"
}
```

#### Structs

Structs represent C `struct`s (aka a block of memory made up of the given members in order), and should follow all the same layout and alignment rules as C structs.

They have only one additional key:

- `members`: An array of objects which have a `name`, `type` (which may include modifiers), and `description`.

##### Example

```json
{
    "name": "GDExtensionCallError",
    "kind": "struct",
    "members": [
        {
            "name": "error",
            "type": "GDExtensionCallErrorType"
        },
        {
            "name": "argument",
            "type": "int32_t"
        },
        {
            "name": "expected",
            "type": "int32_t"
        }
    ]
}
```

#### Functions

Functions represent C function pointer types, with a list of arguments and a return type, and should follow the same size and alignment requirements as C function pointers.

They have the following members:

- `return_value`: An object which has a `type` (which may include modifiers) and `description`. If the function has no return value, this will be omitted.
- `arguments` (required): An array of function arguments which each has a `type` (which may include modifiers), `name`, and `description`.

##### Example

```json
{
    "name": "GDExtensionPtrConstructor",
    "kind": "function",
    "arguments": [
        {
            "name": "p_base",
            "type": "GDExtensionUninitializedTypePtr"
        },
        {
            "name": "p_args",
            "type": "const GDExtensionConstTypePtr*"
        }
    ]
}
```

### Interface

The `interface` section of the JSON file is the list of interface functions, which can be loaded by `name` using the `GDExtensionInterfaceGetProcAddress` function pointer, which is passed to all GDExtensions when they are loaded.

Interface functions have some of the same keys as types, including `name` (required), `deprecated`, and `description`.

And they also have `return_value` and `arguments` (required) that have the same format as the equivalent keys on function types (as described in the previous section).

There are only a handful of unique keys:

- `since` (required): The Godot version that introduced this interface function.
- `see`: An array of strings describing external references with more information, for example, names of classes or functions in the Godot source code, or URLs pointing to documentation.
- `legacy_type_name`: The legacy name used for the function pointer type in the header generated by Godot, when the legacy name doesn't match the pattern used for these type names. This field only exists so that we can generate the header in a way that is backwards compatible with the header from Godot 4.5 or earlier, and it shouldn't be used unless you also need to maintain compatibility with the old header.

#### Example

```json
{
    "name": "get_godot_version",
    "arguments": [
        {
            "name": "r_godot_version",
            "type": "GDExtensionGodotVersion*",
            "description": [
                "A pointer to the structure to write the version information into."
            ]
        }
    ],
    "description": [
        "Gets the Godot version that the GDExtension was loaded into."
    ],
    "since": "4.1",
    "deprecated": {
        "since": "4.5",
        "replace_with": "get_godot_version2"
    }
}
```

---

## What is GDExtension?

**GDExtension** is a Godot-specific technology that lets the engine interact with native [shared libraries](<https://en.wikipedia.org/wiki/Library_(computing)#Shared_libraries>) at runtime. You can use it to run native code without compiling it with the engine.

There are three primary methods with which this is achieved:

- `gdextension_interface.h`: A set of C functions that Godot and a GDExtension can use to communicate.
- `extension_api.json`: A list of C functions that are exposed from Godot APIs (Core Features).
- \*.gdextension: A file format read by Godot to load a GDExtension.

Most people create GDExtensions with some existing language binding, such as godot-cpp (for C++), or one of the community-made ones.

### Version compatibility

See godot-cpp Version Compatibility, which applies to all GDExtensions.

---

## GDScript: An introduction to dynamic languages

### About

This tutorial aims to be a quick reference for how to use GDScript more efficiently. It focuses on common cases specific to the language, but also covers a lot of information on dynamically typed languages.

It's meant to be especially useful for programmers with little or no previous experience with dynamically typed languages.

### Dynamic nature

#### Pros & cons of dynamic typing

GDScript is a Dynamically Typed language. As such, its main advantages are that:

- The language is easy to get started with.
- Most code can be written and changed quickly and without hassle.
- The code is easy to read (little clutter).
- No compilation is required to test.
- Runtime is tiny.
- It has duck-typing and polymorphism by nature.

While the main disadvantages are:

- Less performance than statically typed languages.
- More difficult to refactor (symbols can't be traced).
- Some errors that would typically be detected at compile time in statically typed languages only appear while running the code (because expression parsing is more strict).
- Less flexibility for code-completion (some variable types are only known at runtime).

This, translated to reality, means that Godot used with GDScript is a combination designed to create games quickly and efficiently. For games that are very computationally intensive and can't benefit from the engine built-in tools (such as the Vector types, Physics Engine, Math library, etc), the possibility of using C++ is present too. This allows you to still create most of the game in GDScript and add small bits of C++ in the areas that need a performance boost.

#### Variables & assignment

All variables in a dynamically typed language are "variant"-like. This means that their type is not fixed, and is only modified through assignment. Example:

Static:

```cpp
int a; // Value uninitialized.
a = 5; // This is valid.
a = "Hi!"; // This is invalid.
```

Dynamic:

```gdscript
var a # 'null' by default.
a = 5 # Valid, 'a' becomes an integer.
a = "Hi!" # Valid, 'a' changed to a string.
```

#### As function arguments:

Functions are of dynamic nature too, which means they can be called with different arguments, for example:

Static:

```cpp
void print_value(int value) {

    printf("value is %i\n", value);
}

[..]

print_value(55); // Valid.
print_value("Hello"); // Invalid.
```

Dynamic:

```gdscript
func print_value(value):
    print(value)

[..]

print_value(55) # Valid.
print_value("Hello") # Valid.
```

#### Pointers & referencing:

In static languages, such as C or C++ (and to some extent Java and C#), there is a distinction between a variable and a pointer/reference to a variable. The latter allows the object to be modified by other functions by passing a reference to the original one.

In C# or Java, everything not a built-in type (int, float, sometimes String) is always a pointer or a reference. References are also garbage-collected automatically, which means they are erased when no longer used. Dynamically typed languages tend to use this memory model, too. Some Examples:

- C++:

```cpp
void use_class(SomeClass *instance) {

    instance->use();
}

void do_something() {

    SomeClass *instance = new SomeClass; // Created as pointer.
    use_class(instance); // Passed as pointer.
    delete instance; // Otherwise it will leak memory.
}
```

- Java:

```java
@Override
public final void use_class(SomeClass instance) {

    instance.use();
}

public final void do_something() {

    SomeClass instance = new SomeClass(); // Created as reference.
    use_class(instance); // Passed as reference.
    // Garbage collector will get rid of it when not in
    // use and freeze your game randomly for a second.
}
```

- GDScript:

```gdscript
func use_class(instance): # Does not care about class type
    instance.use() # Will work with any class that has a ".use()" method.

func do_something():
    var instance = SomeClass.new() # Created as reference.
    use_class(instance) # Passed as reference.
    # Will be unreferenced and deleted.
```

In GDScript, only base types (int, float, string and the vector types) are passed by value to functions (value is copied). Everything else (instances, arrays, dictionaries, etc) is passed as reference. Classes that inherit [RefCounted](../godot_gdscript_core.md) (the default if nothing is specified) will be freed when not used, but manual memory management is allowed too if inheriting manually from [Object](../godot_gdscript_core.md).

### Arrays

Arrays in dynamically typed languages can contain many different mixed datatypes inside and are always dynamic (can be resized at any time). Compare for example arrays in statically typed languages:

```cpp
int *array = new int[4]; // Create array.
array[0] = 10; // Initialize manually.
array[1] = 20; // Can't mix types.
array[2] = 40;
array[3] = 60;
// Can't resize.
use_array(array); // Passed as pointer.
delete[] array; // Must be freed.

// or

std::vector<int> array;
array.resize(4);
array[0] = 10; // Initialize manually.
array[1] = 20; // Can't mix types.
array[2] = 40;
array[3] = 60;
array.resize(3); // Can be resized.
use_array(array); // Passed reference or value.
// Freed when stack ends.
```

And in GDScript:

```gdscript
var array = [10, "hello", 40, 60] # You can mix types.
array.resize(3) # Can be resized.
use_array(array) # Passed as reference.
# Freed when no longer in use.
```

In dynamically typed languages, arrays can also double as other datatypes, such as lists:

```gdscript
var array = []
array.append(4)
array.append(5)
array.pop_front()
```

Or unordered sets:

```gdscript
var a = 20
if a in [10, 20, 30]:
    print("We have a winner!")
```

### Dictionaries

Dictionaries are a powerful tool in dynamically typed languages. In GDScript, untyped dictionaries can be used for many cases where a statically typed language would tend to use another data structure.

Dictionaries can map any value to any other value with complete disregard for the datatype used as either key or value. Contrary to popular belief, they are efficient because they can be implemented with hash tables. They are, in fact, so efficient that some languages will go as far as implementing arrays as dictionaries.

Example of Dictionary:

```gdscript
var d = {"name": "John", "age": 22}
print("Name: ", d["name"], " Age: ", d["age"])
```

Dictionaries are also dynamic, keys can be added or removed at any point at little cost:

```gdscript
d["mother"] = "Rebecca" # Addition.
d["age"] = 11 # Modification.
d.erase("name") # Removal.
```

In most cases, two-dimensional arrays can often be implemented more easily with dictionaries. Here's a battleship game example:

```gdscript
# Battleship Game

const SHIP = 0
const SHIP_HIT = 1
const WATER_HIT = 2

var board = {}

func initialize():
    board[Vector2(1, 1)] = SHIP
    board[Vector2(1, 2)] = SHIP
    board[Vector2(1, 3)] = SHIP

func missile(pos):
    if pos in board: # Something at that position.
        if board[pos] == SHIP: # There was a ship! hit it.
            board[pos] = SHIP_HIT
        else:
            print("Already hit here!") # Hey dude you already hit here.
    else: # Nothing, mark as water.
        board[pos] = WATER_HIT

func game():
    initialize()
    missile(Vector2(1, 1))
    missile(Vector2(5, 8))
    missile(Vector2(2, 3))
```

Dictionaries can also be used as data markup or quick structures. While GDScript's dictionaries resemble python dictionaries, it also supports Lua style syntax and indexing, which makes it useful for writing initial states and quick structs:

```gdscript
# Same example, lua-style support.
# This syntax is a lot more readable and usable.
# Like any GDScript identifier, keys written in this form cannot start
# with a digit.

var d = {
    name = "John",
    age = 22
}

print("Name: ", d.name, " Age: ", d.age) # Used "." based indexing.

# Indexing

d["mother"] = "Rebecca"
d.mother = "Caroline" # This would work too to create a new key.
```

### For & while

Iterating using the C-style for loop in C-derived languages can be quite complex:

```cpp
const char** strings = new const char*[50];

[..]

for (int i = 0; i < 50; i++) {
    printf("Value: %c Index: %d\n", strings[i], i);
}

// Even in STL:
std::list<std::string> strings;

[..]

for (std::string::const_iterator it = strings.begin(); it != strings.end(); it++) {
    std::cout << *it << std::endl;
}
```

Because of this, GDScript makes the opinionated decision to have a for-in loop over iterables instead:

```gdscript
for s in strings:
    print(s)
```

Container datatypes (arrays and dictionaries) are iterable. Dictionaries allow iterating the keys:

```gdscript
for key in dict:
    print(key, " -> ", dict[key])
```

Iterating with indices is also possible:

```gdscript
for i in range(strings.size()):
    print(strings[i])
```

The range() function can take 3 arguments:

```gdscript
range(n) # Will count from 0 to n in steps of 1. The parameter n is exclusive.
range(b, n) # Will count from b to n in steps of 1. The parameters b is inclusive. The parameter n is exclusive.
range(b, n, s) # Will count from b to n, in steps of s. The parameters b is inclusive. The parameter n is exclusive.
```

Some examples involving C-style for loops:

```cpp
for (int i = 0; i < 10; i++) {}

for (int i = 5; i < 10; i++) {}

for (int i = 5; i < 10; i += 2) {}
```

Translate to:

```gdscript
for i in range(10):
    pass

for i in range(5, 10):
    pass

for i in range(5, 10, 2):
    pass
```

And backwards looping done through a negative counter:

```gdscript
for (int i = 10; i > 0; i--) {}
```

Becomes:

```gdscript
for i in range(10, 0, -1):
    pass
```

### While

while() loops are the same everywhere:

```gdscript
var i = 0

while i < strings.size():
    print(strings[i])
    i += 1
```

### Custom iterators

You can create custom iterators in case the default ones don't quite meet your needs by overriding the Variant class's `_iter_init`, `_iter_next`, and `_iter_get` functions in your script. An example implementation of a forward iterator follows:

```gdscript
class ForwardIterator:
    var start
    var current
    var end
    var increment

    func _init(start, stop, increment):
        self.start = start
        self.current = start
        self.end = stop
        self.increment = increment

    func should_continue():
        return (current < end)

    func _iter_init(arg):
        current = start
        return should_continue()

    func _iter_next(arg):
        current += increment
        return should_continue()

    func _iter_get(arg):
        return current
```

And it can be used like any other iterator:

```gdscript
var itr = ForwardIterator.new(0, 6, 2)
for i in itr:
    print(i) # Will print 0, 2, and 4.
```

Make sure to reset the state of the iterator in `_iter_init`, otherwise nested for-loops that use custom iterators will not work as expected.

### Duck typing

One of the most difficult concepts to grasp when moving from a statically typed language to a dynamic one is duck typing. Duck typing makes overall code design much simpler and straightforward to write, but it's not obvious how it works.

As an example, imagine a situation where a big rock is falling down a tunnel, smashing everything on its way. The code for the rock, in a statically typed language would be something like:

```cpp
void BigRollingRock::on_object_hit(Smashable *entity) {

    entity->smash();
}
```

This way, everything that can be smashed by a rock would have to inherit Smashable. If a character, enemy, piece of furniture, small rock were all smashable, they would need to inherit from the class Smashable, possibly requiring multiple inheritance. If multiple inheritance was undesired, then they would have to inherit a common class like Entity. Yet, it would not be very elegant to add a virtual method `smash()` to Entity only if a few of them can be smashed.

With dynamically typed languages, this is not a problem. Duck typing makes sure you only have to define a `smash()` function where required and that's it. No need to consider inheritance, base classes, etc.

```gdscript
func _on_object_hit(object):
    object.smash()
```

And that's it. If the object that hit the big rock has a smash() method, it will be called. No need for inheritance or polymorphism. Dynamically typed languages only care about the instance having the desired method or member, not what it inherits or the class type. The definition of Duck Typing should make this clearer:

_"When I see a bird that walks like a duck and swims like a duck and quacks like a duck, I call that bird a duck"_

In this case, it translates to:

_"If the object can be smashed, don't care what it is, just smash it."_

Yes, we should call it Hulk typing instead.

It's possible that the object being hit doesn't have a smash() function. Some dynamically typed languages simply ignore a method call when it doesn't exist, but GDScript is stricter, so checking if the function exists is desirable:

```gdscript
func _on_object_hit(object):
    if object.has_method("smash"):
        object.smash()
```

Then, define that method and anything the rock touches can be smashed.

---
