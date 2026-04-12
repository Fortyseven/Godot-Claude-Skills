# Godot 4 GDScript Tutorials — Scripting (Part 10)

> 6 tutorials. GDScript-specific code examples.

## GDScript style guide

This style guide lists conventions to write elegant GDScript. The goal is to encourage writing clean, readable code and promote consistency across projects, discussions, and tutorials. Hopefully, this will also support the development of auto-formatting tools.

Since GDScript is close to Python, this guide is inspired by Python's [PEP 8](https://www.python.org/dev/peps/pep-0008/) programming style guide.

Style guides aren't meant as hard rulebooks. At times, you may not be able to apply some of the guidelines below. When that happens, use your best judgment, and ask fellow developers for insights.

In general, keeping your code consistent in your projects and within your team is more important than following this guide to a tee.

> **Note:** Godot's built-in script editor uses a lot of these conventions by default. Let it help you.

Here is a complete class example based on these guidelines:

```gdscript
class_name StateMachine
extends Node
## Hierarchical State machine for the player.
##
## Initializes states and delegates engine callbacks ([method Node._physics_process],
## [method Node._unhandled_input]) to the state.

signal state_changed(previous, new)

@export var initial_state: Node
var is_active = true:
    set = set_is_active

@onready var _state = initial_state:
    set = set_state
@onready var _state_name = _state.name

func _init():
    add_to_group("state_machine")

func _enter_tree():
    print("this happens before the ready method!")

func _ready():
    state_changed.connect(_on_state_changed)
    _state.enter()

func _unhandled_input(event):
    _state.unhandled_input(event)

func _physics_process(delta):
    _state.physics_process(delta)

func transition_to(target_st
# ...
```

### Formatting

#### Encoding and special characters

- Use line feed (**LF**) characters to break lines, not CRLF or CR. _(editor default)_
- Use one line feed character at the end of each file. _(editor default)_
- Use **UTF-8** encoding without a [byte order mark](https://en.wikipedia.org/wiki/Byte_order_mark). _(editor default)_
- Use **Tabs** instead of spaces for indentation. _(editor default)_

#### Indentation

Each indent level should be one greater than the block containing it.

**Good**:

```gdscript
for i in range(10):
    print("hello")
```

**Bad**:

```gdscript
for i in range(10):
  print("hello")

for i in range(10):
        print("hello")
```

Use 2 indent levels to distinguish continuation lines from regular code blocks.

**Good**:

```gdscript
effect.interpolate_property(sprite, "transform/scale",
        sprite.get_scale(), Vector2(2.0, 2.0), 0.3,
        Tween.TRANS_QUAD, Tween.EASE_OUT)
```

**Bad**:

```gdscript
effect.interpolate_property(sprite, "transform/scale",
    sprite.get_scale(), Vector2(2.0, 2.0), 0.3,
    Tween.TRANS_QUAD, Tween.EASE_OUT)
```

Exceptions to this rule are arrays, dictionaries, and enums. Use a single indentation level to distinguish continuation lines:

**Good**:

```gdscript
var party = [
    "Godot",
    "Godette",
    "Steve",
]

var character_dict = {
    "Name": "Bob",
    "Age": 27,
    "Job": "Mechanic",
}

enum Tile {
    BRICK,
    FLOOR,
    SPIKE,
    TELEPORT,
}
```

**Bad**:

```gdscript
var party = [
        "Godot",
        "Godette",
        "Steve",
]

var character_dict = {
        "Name": "Bob",
        "Age": 27,
        "Job": "Mechanic",
}

enum Tile {
        BRICK,
        FLOOR,
        SPIKE,
        TELEPORT,
}
```

#### Trailing comma

Use a trailing comma on the last line in arrays, dictionaries, and enums. This results in easier refactoring and better diffs in version control as the last line doesn't need to be modified when adding new elements.

**Good**:

```gdscript
var array = [
    1,
    2,
    3,
]
```

**Bad**:

```gdscript
var array = [
    1,
    2,
    3
]
```

Trailing commas are unnecessary in single-line lists, so don't add them in this case.

**Good**:

```gdscript
var array = [1, 2, 3]
```

**Bad**:

```gdscript
var array = [1, 2, 3,]
```

#### Blank lines

Surround functions and class definitions with two blank lines:

```gdscript
func heal(amount):
    health += amount
    health = min(health, max_health)
    health_changed.emit(health)

func take_damage(amount, effect=null):
    health -= amount
    health = max(0, health)
    health_changed.emit(health)
```

Use one blank line inside functions to separate logical sections.

> **Note:** We use a single line between classes and function definitions in the class reference and in short code snippets in this documentation.

#### Line length

Keep individual lines of code under 100 characters.

If you can, try to keep lines under 80 characters. This helps to read the code on small displays and with two scripts opened side-by-side in an external text editor. For example, when looking at a differential revision.

#### One statement per line

Avoid combining multiple statements on a single line, including conditional statements, to adhere to the GDScript style guidelines for readability.

**Good**:

```gdscript
if position.x > width:
    position.x = 0

if flag:
    print("flagged")
```

**Bad**:

```gdscript
if position.x > width: position.x = 0

if flag: print("flagged")
```

The only exception to that rule is the ternary operator:

```gdscript
next_state = "idle" if is_on_floor() else "fall"
```

#### Format multiline statements for readability

When you have particularly long `if` statements or nested ternary expressions, wrapping them over multiple lines improves readability. Since continuation lines are still part of the same expression, 2 indent levels should be used instead of one.

GDScript allows wrapping statements using multiple lines using parentheses or backslashes. Parentheses are favored in this style guide since they make for easier refactoring. With backslashes, you have to ensure that the last line never contains a backslash at the end. With parentheses, you don't have to worry about the last line having a backslash at the end.

When wrapping a conditional expression over multiple lines, the `and`/`or` keywords should be placed at the beginning of the line continuation, not at the end of the previous line.

**Good**:

```gdscript
var angle_degrees = 135
var quadrant = (
        "northeast" if angle_degrees <= 90
        else "southeast" if angle_degrees <= 180
        else "southwest" if angle_degrees <= 270
        else "northwest"
)

var position = Vector2(250, 350)
if (
        position.x > 200 and position.x < 400
        and position.y > 300 and position.y < 400
):
    pass
```

**Bad**:

```gdscript
var angle_degrees = 135
var quadrant = "northeast" if angle_degrees <= 90 else "southeast" if angle_degrees <= 180 else "southwest" if angle_degrees <= 270 else "northwest"

var position = Vector2(250, 350)
if position.x > 200 and position.x < 400 and position.y > 300 and position.y < 400:
    pass
```

#### Avoid unnecessary parentheses

Avoid parentheses in expressions and conditional statements. Unless necessary for order of operations or wrapping over multiple lines, they only reduce readability.

**Good**:

```gdscript
if is_colliding():
    queue_free()
```

**Bad**:

```gdscript
if (is_colliding()):
    queue_free()
```

#### Boolean operators

Prefer the plain English versions of boolean operators, as they are the most accessible:

- Use `and` instead of `&&`.
- Use `or` instead of `||`.
- Use `not` instead of `!`.

You may also use parentheses around boolean operators to clear any ambiguity. This can make long expressions easier to read.

**Good**:

```gdscript
if (foo and bar) or not baz:
    print("condition is true")
```

**Bad**:

```gdscript
if foo && bar || !baz:
    print("condition is true")
```

#### Comment spacing

Regular comments (`#`) and documentation comments (`##`) should start with a space, but not code that you comment out. Additionally, code region comments (`#region`/`#endregion`) must follow that precise syntax, so they should not start with a space.

Using a space for regular and documentation comments helps differentiate text comments from disabled code.

**Good**:

```gdscript
# This is a comment.
#print("This is disabled code")
```

**Bad**:

```gdscript
#This is a comment.
# print("This is disabled code")
```

> **Note:** In the script editor, to toggle commenting of the selected code, press Ctrl + K. This feature adds/removes a single `#` sign before any code on the selected lines.

Prefer writing comments on their own line as opposed to inline comments (comments written on the same line as code). Inline comments are best used for short comments, typically a few words at most:

**Good**:

```gdscript
# This is a long comment that would make the line below too long if written inline.
print("Example") # Short comment.
```

**Bad**:

```gdscript
print("Example") # This is a long comment that would make this line too long if written inline.
```

#### Whitespace

Always use one space around operators and after commas. Also, avoid extra spaces in dictionary references and function calls. One exception to this is for single-line dictionary declarations, where a space should be added after the opening brace and before the closing brace. This makes the dictionary easier to visually distinguish from an array, as the `[]` characters look close to `{}` with most fonts.

**Good**:

```gdscript
position.x = 5
position.y = target_position.y + 10
dict["key"] = 5
my_array = [4, 5, 6]
my_dictionary = { key = "value" }
print("foo")
```

**Bad**:

```gdscript
position.x=5
position.y = mpos.y+10
dict ["key"] = 5
myarray = [4,5,6]
my_dictionary = {key = "value"}
print ("foo")
```

Don't use spaces to align expressions vertically:

```gdscript
x        = 100
y        = 100
velocity = 500
```

#### Quotes

Use double quotes unless single quotes make it possible to escape fewer characters in a given string. See the examples below:

```gdscript
# Normal string.
print("hello world")

# Use double quotes as usual to avoid escapes.
print("hello 'world'")

# Use single quotes as an exception to the rule to avoid escapes.
print('hello "world"')

# Both quote styles would require 2 escapes; prefer double quotes if it's a tie.
print("'hello' \"world\"")
```

#### Numbers

Don't omit the leading or trailing zero in floating-point numbers. Otherwise, this makes them less readable and harder to distinguish from integers at a glance.

**Good**:

```gdscript
var float_number = 0.234
var other_float_number = 13.0
```

**Bad**:

```gdscript
var float_number = .234
var other_float_number = 13.
```

Use lowercase for letters in hexadecimal numbers, as their lower height makes the number easier to read.

**Good**:

```gdscript
var hex_number = 0xfb8c0b
```

**Bad**:

```gdscript
var hex_number = 0xFB8C0B
```

Take advantage of GDScript's underscores in literals to make large numbers more readable.

**Good**:

```gdscript
var large_number = 1_234_567_890
var large_hex_number = 0xffff_f8f8_0000
var large_bin_number = 0b1101_0010_1010
# Numbers lower than 1000000 generally don't need separators.
var small_number = 12345
```

**Bad**:

```gdscript
var large_number = 1234567890
var large_hex_number = 0xfffff8f80000
var large_bin_number = 0b110100101010
# Numbers lower than 1000000 generally don't need separators.
var small_number = 12_345
```

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

```gdscript
# This file should be saved as `weapon.gd`.
class_name Weapon
extends Node
```

```gdscript
# This file should be saved as `yaml_parser.gd`.
class_name YAMLParser
extends Object
```

This is consistent with how C++ files are named in Godot's source code. This also avoids case sensitivity issues that can crop up when exporting a project from Windows to other platforms.

#### Classes and nodes

Use PascalCase for class and node names:

```gdscript
extends CharacterBody3D
```

Also use PascalCase when loading a class into a constant or a variable:

```gdscript
const Weapon = preload("res://weapon.gd")
```

#### Functions and variables

Use snake_case to name functions and variables:

```gdscript
var particle_effect
func load_level():
```

Prepend a single underscore (\_) to virtual methods functions the user must override, private functions, and private variables:

```gdscript
var _counter = 0
func _recalculate_path():
```

#### Signals

Use the past tense to name signals:

```gdscript
signal door_opened
signal score_changed
```

#### Constants and enums

Write constants with CONSTANT*CASE, that is to say in all caps with an underscore (*) to separate words:

```gdscript
const MAX_SPEED = 200
```

Use PascalCase for enum _names_ and keep them singular, as they represent a type. Use CONSTANT_CASE for their members, as they are constants:

```gdscript
enum Element {
    EARTH,
    WATER,
    AIR,
    FIRE,
}
```

Write enums with each item on its own line. This allows adding documentation comments above each item more easily, and also makes for cleaner diffs in version control when items are added or removed.

**Good**:

```gdscript
enum Element {
    EARTH,
    WATER,
    AIR,
    FIRE,
}
```

**Bad**:

```gdscript
enum Element { EARTH, WATER, AIR, FIRE }
```

### Code order

This section focuses on code order. For formatting, see **Formatting**. For naming conventions, see **Naming conventions**.

We suggest to organize GDScript code this way:

```gdscript
01. @tool, @icon, @static_unload
02. class_name
03. extends
04. ## doc comment

05. signals
06. enums
07. constants
08. static variables
09. @export variables
10. remaining regular variables
11. @onready variables

12. _static_init()
13. remaining static methods
14. overridden built-in virtual methods:
    1. _init()
    2. _enter_tree()
    3. _ready()
    4. _process()
    5. _physics_process()
    6. remaining virtual methods
15. overridden custom methods
16. remaining methods
17. inner classes
```

And put the class methods and variables in the following order depending on their access modifiers:

```gdscript
1. public
2. private
```

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

```gdscript
@abstract
class_name MyNode
extends Node
## A brief description of the class's role and functionality.
##
## The description of the script, what it can do,
## and any further detail.
```

For inner classes, use single-line declarations:

```gdscript
## A brief description of the class's role and functionality.
##
## The description of the script, what it can do,
## and any further detail.
@abstract class MyNode extends Node:
    pass
```

#### Signals and properties

Write signal declarations, followed by properties, that is to say, member variables, after the docstring.

Enums should come after signals, as you can use them as export hints for other properties.

Then, write constants, exported variables, public, private, and onready variables, in that order.

```gdscript
signal player_spawned(position)

enum Job {
    KNIGHT,
    WIZARD,
    ROGUE,
    HEALER,
    SHAMAN,
}

const MAX_LIVES = 3

@export var job: Job = Job.KNIGHT
@export var max_health = 50
@export var attack = 5

var health = max_health:
    set(new_health):
        health = new_health

var _speed = 300.0

@onready var sword = get_node("Sword")
@onready var gun = get_node("Gun")
```

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

```gdscript
func _init():
    add_to_group("state_machine")

func _ready():
    state_changed.connect(_on_state_changed)
    _state.enter()

func _unhandled_input(event):
    _state.unhandled_input(event)

func transition_to(target_state_path, msg={}):
    if not has_node(target_state_path):
        return

    var target_state = get_node(target_state_path)
    assert(target_state.is_composite == false)

    _state.exit()
    self._state = target_state
    _state.enter(msg)
    Events.player_state_changed.emit(_state.name)

func _on_state_changed(previous, new):
    print("state changed")
    state_changed.emit()
```

### Static typing

GDScript supports optional static typing.

#### Declared types

To declare a variable's type, use `<variable>: <type>`:

```gdscript
var health: int = 0
```

To declare the return type of a function, use `-> <type>`:

```gdscript
func heal(amount: int) -> void:
```

#### Inferred types

In most cases, you can let the compiler infer the type using `:=`. Prefer `:=` when the type is written on the same line as the assignment, otherwise prefer writing the type explicitly.

**Good**:

```gdscript
# The type can be int or float, and thus should be stated explicitly.
var health: int = 0

# The type is clearly inferred as Vector3.
var direction := Vector3(1, 2, 3)
```

Include the type hint when the type is ambiguous, and omit the type hint when it's redundant.

**Bad**:

```gdscript
# Typed as int, but it could be that float was intended.
var health := 0

# The type hint has redundant information.
var direction: Vector3 = Vector3(1, 2, 3)

# What type is this? It's not immediately clear to the reader, so it's bad.
var value := complex_function()
```

In some cases, the type must be stated explicitly, otherwise the behavior will not be as expected because the compiler will only be able to use the function's return type. For example, `get_node()` cannot infer a type unless the scene or file of the node is loaded in memory. In this case, you should set the type explicitly.

**Good**:

```gdscript
@onready var health_bar: ProgressBar = get_node("UI/LifeBar")
```

**Bad**:

```gdscript
# The compiler can't infer the exact type and will use Node
# instead of ProgressBar.
@onready var health_bar := get_node("UI/LifeBar")
```

Alternatively, you can use the `as` keyword to cast the return type, and that type will be used to infer the type of the var.

```gdscript
@onready var health_bar := get_node("UI/LifeBar") as ProgressBar
# health_bar will be typed as ProgressBar
```

> **Note:** This option is considered more type-safe than type hints, but also less null-safe as it silently casts the variable to `null` in case of a type mismatch at runtime, without an error/warning.

---

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

```gdscript
class_name Inventory

func add(reference: Item, amount: int = 1):
    var item := find_item(reference)
    if not item:
        item = _instance_item_from_db(reference)
    item.amount += amount
```

Static types also give you better code completion options. Below, you can see the difference between a dynamic and a static typed completion options.

You've probably encountered a lack of autocomplete suggestions after a dot:

This is due to dynamic code. Godot cannot know what value type you're passing to the function. If you write the type explicitly however, you will get all methods, properties, constants, etc. from the value:

> **Tip:** If you prefer static typing, we recommend enabling the **Text Editor > Completion > Add Type Hints** editor setting. Also consider enabling **some warnings** that are disabled by default.

Also, typed GDScript improves performance by using optimized opcodes when operand/argument types are known at compile time. More GDScript optimizations are planned in the future, such as JIT/AOT compilation.

Overall, typed programming gives you a more structured experience. It helps prevent errors and improves the self-documenting aspect of your scripts. This is especially helpful when you're working in a team or on a long-term project: studies have shown that developers spend most of their time reading other people's code, or scripts they wrote in the past and forgot about. The clearer and the more structured the code, the faster it is to understand, the faster you can move forward.

### How to use static typing

To define the type of a variable, parameter, or constant, write a colon after the name, followed by its type. E.g. `var health: int`. This forces the variable's type to always stay the same:

```gdscript
var damage: float = 10.5
const MOVE_SPEED: float = 50.0
func sum(a: float = 0.0, b: float = 0.0) -> float:
    return a + b
```

Godot will try to infer types if you write a colon, but you omit the type:

```gdscript
var damage := 10.5
const MOVE_SPEED := 50.0
func sum(a := 0.0, b := 0.0) -> float:
    return a + b
```

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

```gdscript
const Rifle = preload("res://player/weapons/rifle.gd")
var my_rifle: Rifle
```

The second method is to use the `class_name` keyword when you create the script. For the example above, your `rifle.gd` would look like this:

```gdscript
class_name Rifle
extends Node2D
```

If you use `class_name`, Godot registers the `Rifle` type globally in the editor, and you can use it anywhere, without having to preload it into a constant:

```gdscript
var my_rifle: Rifle
```

#### Specify the return type of a function with the arrow ->

To define the return type of a function, write a dash and a right angle bracket `->` after its declaration, followed by the return type:

```gdscript
func _process(delta: float) -> void:
    pass
```

The type `void` means the function does not return anything. You can use any type, as with variables:

```gdscript
func hit(damage: float) -> bool:
    health_points -= damage
    return health_points <= 0
```

You can also use your own classes as return types:

```gdscript
# Adds an item to the inventory and returns it.
func add(reference: Item, amount: int) -> Item:
    var item: Item = find_item(reference)
    if not item:
        item = ItemDatabase.get_instance(reference)

    item.amount += amount
    return item
```

#### Covariance and contravariance

When inheriting base class methods, you should follow the [Liskov substitution principle](https://en.wikipedia.org/wiki/Liskov_substitution_principle).

**Covariance:** When you inherit a method, you can specify a return type that is more specific (**subtype**) than the parent method.

**Contravariance:** When you inherit a method, you can specify a parameter type that is less specific (**supertype**) than the parent method.

Example:

```gdscript
class_name Parent

func get_property(param: Label) -> Node:
    # ...
```

```gdscript
class_name Child extends Parent

# `Control` is a supertype of `Label`.
# `Node2D` is a subtype of `Node`.
func get_property(param: Control) -> Node2D:
    # ...
```

#### Specify the element type of an Array

To define the type of an `Array`, enclose the type name in `[]`.

An array's type applies to `for` loop variables, as well as some operators like `[]`, `[...] =` (assignment), and `+`. Array methods (such as `push_back`) and other operators (such as `==`) are still untyped. Built-in types, native and custom classes, and enums may be used as element types. Nested array types (like `Array[Array[int]]`) are not supported.

```gdscript
var scores: Array[int] = [10, 20, 30]
var vehicles: Array[Node] = [$Car, $Plane]
var items: Array[Item] = [Item.new()]
var array_of_arrays: Array[Array] = [[], []]
# var arrays: Array[Array[int]] -- disallowed

for score in scores:
    # score has type `int`

# The following would be errors:
scores += vehicles
var s: String = scores[0]
scores[0] = "lots"
```

Since Godot 4.2, you can also specify a type for the loop variable in a `for` loop. For instance, you can write:

```gdscript
var names = ["John", "Marta", "Samantha", "Jimmy"]
for name: String in names:
    pass
```

The array will remain untyped, but the `name` variable within the `for` loop will always be of `String` type.

#### Specify the element type of a Dictionary

To define the type of a `Dictionary`'s keys and values, enclose the type name in `[]` and separate the key and value type with a comma.

A dictionary's value type applies to `for` loop variables, as well as some operators like `[]` and `[...] =` (assignment). Dictionary methods that return values and other operators (such as `==`) are still untyped. Built-in types, native and custom classes, and enums may be used as element types. Nested typed collections (like `Dictionary[String, Dictionary[String, int]]`) are not supported.

```gdscript
var fruit_costs: Dictionary[String, int] = { "apple": 5, "orange": 10 }
var vehicles: Dictionary[String, Node] = { "car": $Car, "plane": $Plane }
var item_tiles: Dictionary[Vector2i, Item] = { Vector2i(0, 0): Item.new(), Vector2i(0, 1): Item.new() }
var dictionary_of_dictionaries: Dictionary[String, Dictionary] = { { } }
# var dicts: Dictionary[String, Dictionary[String, int]] -- disallowed

for cost in fruit_costs:
    # cost has type `int`

# The following would be errors:
fruit_costs["pear"] += vehicles
var s: String = fruit_costs["apple"]
fruit_costs["orange"] = "lots"
```

#### Type casting

Type casting is an important concept in typed languages. Casting is the conversion of a value from one type to another.

Imagine an `Enemy` in your game, that `extends Area2D`. You want it to collide with the `Player`, a `CharacterBody2D` with a script called `PlayerController` attached to it. You use the `body_entered` signal to detect the collision. With typed code, the body you detect is going to be a generic `PhysicsBody2D`, and not your `PlayerController` on the `_on_body_entered` callback.

You can check if this `PhysicsBody2D` is your `Player` with the `as` keyword, and using the colon `:` again to force the variable to use this type. This forces the variable to stick to the `PlayerController` type:

```gdscript
func _on_body_entered(body: PhysicsBody2D) -> void:
    var player := body as PlayerController
    if not player:
        return

    player.damage()
```

As we're dealing with a custom type, if the `body` doesn't extend `PlayerController`, the `player` variable will be set to `null`. We can use this to check if the body is the player or not. We will also get full autocompletion on the player variable thanks to that cast.

> **Note:** The `as` keyword silently casts the variable to `null` in case of a type mismatch at runtime, without an error/warning. While this may be convenient in some cases, it can also lead to bugs. Use the `as` keyword only if this behavior is intended. A safer alternative is to use the `is` keyword: ```gdscript
> if not (body is PlayerController):

    push_error("Bug: body is not PlayerController.")

var player: PlayerController = body
if not player:
return

player.damage()
``You can also simplify the code by using the `is not` operator:``gdscript
if body is not PlayerController:
push_error("Bug: body is not PlayerController")
``Alternatively, you can use the `assert()` statement:``gdscript
assert(body is PlayerController, "Bug: body is not PlayerController.")

var player: PlayerController = body
if not player:
return

player.damage()

````



> **Note:** If you try to cast with a built-in type and it fails, Godot will throw an error.



##### Safe lines



You can also use casting to ensure safe lines. Safe lines are a tool to tell you when ambiguous lines of code are type-safe. As you can mix and match typed and dynamic code, at times, Godot doesn't have enough information to know if an instruction will trigger an error or not at runtime.



This happens when you get a child node. Let's take a timer for example: with dynamic code, you can get the node with `$Timer`. GDScript supports [duck-typing](https://stackoverflow.com/a/4205163/8125343), so even if your timer is of type `Timer`, it is also a `Node` and an `Object`, two classes it extends. With dynamic GDScript, you also don't care about the node's type as long as it has the methods you need to call.



You can use casting to tell Godot the type you expect when you get a node: `($Timer as Timer)`, `($Player as CharacterBody2D)`, etc. Godot will ensure the type works and if so, the line number will turn green at the left of the script editor.



> **Note:** Safe lines do not always mean better or more reliable code. See the note above about the `as` keyword. For example: ```gdscript
@onready var node_1 := $Node1 as Type1 # Safe line.
@onready var node_2: Type2 = $Node2 # Unsafe line.
``` Even though `node_2` declaration is marked as an unsafe line, it is more reliable than `node_1` declaration. Because if you change the node type in the scene and accidentally forget to change it in the script, the error will be detected immediately when the scene is loaded. Unlike `node_1`, which will be silently cast to `null` and the error will be detected later.



> **Note:** You can turn off safe lines or change their color in the editor settings.



### Typed or dynamic: stick to one style



Typed GDScript and dynamic GDScript can coexist in the same project. But it's recommended to stick to either style for consistency in your codebase, and for your peers. It's easier for everyone to work together if you follow the same guidelines, and faster to read and understand other people's code.



Typed code takes a little more writing, but you get the benefits we discussed above. Here's an example of the same, empty script, in a dynamic style:


```gdscript
extends Node

func _ready():
    pass

func _process(delta):
    pass
````

And with static typing:

```gdscript
extends Node

func _ready() -> void:
    pass

func _process(delta: float) -> void:
    pass
```

As you can see, you can also use types with the engine's virtual methods. Signal callbacks, like any methods, can also use types. Here's a `body_entered` signal in a dynamic style:

```gdscript
func _on_area_2d_body_entered(body):
    pass
```

And the same callback, with type hints:

```gdscript
func _on_area_2d_body_entered(body: PhysicsBody2D) -> void:
    pass
```

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

```gdscript
if "some_property" in node_2d:
    node_2d.some_property = 20  # Produces UNSAFE_PROPERTY_ACCESS warning.

if node_2d.has_method("some_function"):
    node_2d.some_function()  # Produces UNSAFE_METHOD_ACCESS warning.
```

However, this code will produce `UNSAFE_PROPERTY_ACCESS` and `UNSAFE_METHOD_ACCESS` warnings as the property and method are not present in the referenced type - in this case a `Node2D`. To make these operations safe, you can first check if the object is of type `MyScript` using the `is` keyword and then declare a variable with the type `MyScript` on which you can set its properties and call its methods:

```gdscript
if node_2d is MyScript:
    var my_script: MyScript = node_2d
    my_script.some_property = 20
    my_script.some_function()
```

Alternatively, you can declare a variable and use the `as` operator to try to cast the object. You'll then want to check whether the cast was successful by confirming that the variable was assigned:

```gdscript
var my_script := node_2d as MyScript
if my_script != null:
    my_script.some_property = 20
    my_script.some_function()
```

#### UNSAFE_CAST warning

In this example, we would like the label connected to an object entering our collision area to show the area's name. Once the object enters the collision area, the physics system sends a signal with a `Node2D` object, and the most straightforward (but not statically typed) solution to do what we want could be achieved like this:

```gdscript
func _on_body_entered(body: Node2D) -> void:
    body.label.text = name  # Produces UNSAFE_PROPERTY_ACCESS warning.
```

This piece of code produces an `UNSAFE_PROPERTY_ACCESS` warning because `label` is not defined in `Node2D`. To solve this, we could first check if the `label` property exist and cast it to type `Label` before settings its text property like so:

```gdscript
func _on_body_entered(body: Node2D) -> void:
    if "label" in body:
        (body.label as Label).text = name  # Produces UNSAFE_CAST warning.
```

However, this produces an `UNSAFE_CAST` warning because `body.label` is of a `Variant` type. To safely get the property in the type you want, you can use the `Object.get()` method which returns the object as a `Variant` value or returns `null` if the property doesn't exist. You can then determine whether the property contains an object of the right type using the `is` keyword, and finally declare a statically typed variable with the object:

```gdscript
func _on_body_entered(body: Node2D) -> void:
    var label_variant: Variant = body.get("label")
    if label_variant is Label:
        var label: Label = label_variant
        label.text = name
```

### Cases where you can't specify types

To wrap up this introduction, let's mention cases where you can't use type hints. This will trigger a **syntax error**.

1. You can't specify the type of individual elements in an array or a dictionary:

```gdscript
var enemies: Array = [$Goblin: Enemy, $Zombie: Enemy]
var character: Dictionary = {
    name: String = "Richard",
    money: int = 1000,
    inventory: Inventory = $Inventory,
}
```

1. Nested types are not currently supported:

```gdscript
var teams: Array[Array[Character]] = []
```

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
- During execution, by calling [Node.add_to_group()](../godot_gdscript_misc.md) or [Node.remove_from_group()](../godot_gdscript_misc.md).

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

```gdscript
func _ready():
    add_to_group("guards")
```

Imagine you're creating an infiltration game. When an enemy spots the player, you want all guards and robots to be on alert.

In the fictional example below, we use `SceneTree.call_group()` to alert all enemies that the player was spotted.

```gdscript
func _on_player_spotted():
    get_tree().call_group("guards", "enter_alert_mode")
```

The above code calls the function `enter_alert_mode` on every member of the group `guards`.

To get the full list of nodes in the `guards` group as an array, you can call [SceneTree.get_nodes_in_group()](../godot_gdscript_core.md):

```gdscript
var guards = get_tree().get_nodes_in_group("guards")
```

The [SceneTree](../godot_gdscript_core.md) class provides many more useful methods to interact with scenes, their node hierarchy, and groups. It allows you to switch scenes easily or reload them, quit the game or pause and unpause it. It also provides useful signals.

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

> **Note:** Knowing the setter and getter names is useful when one must bind a method name or [Callable](../godot_gdscript_misc.md) to something.

### Method Descriptions

The Method Descriptions list details everything about each method.

It restates the method's return data type, parameter names/types/defaults, and qualifiers.

Below that is a detailed summary of what the method does and its use case(s). It may include code samples and/or links to relevant parts of the Godot API.

---

## Idle and Physics Processing

Games run in a loop. Each frame, you need to update the state of your game world before drawing it on screen. Godot provides two virtual methods in the Node class to do so: [Node.\_process()](../godot_gdscript_misc.md) and [Node.\_physics_process()](../godot_gdscript_misc.md). If you define either or both in a script, the engine will call them automatically.

There are two types of processing available to you:

1. **Idle processing** allows you to run code that updates a node every frame, as often as possible.
2. **Physics processing** happens at a fixed rate, 60 times per second by default. This is independent of your game's actual framerate, and keeps physics running smoothly. You should use it for anything that involves the physics engine, like moving a body that collides with the environment.

You can activate idle processing by defining the `_process()` method in a script. You can turn it off and back on by calling [Node.set_process()](../godot_gdscript_misc.md).

The engine calls this method every time it draws a frame:

```gdscript
func _process(delta):
    # Do something...
    pass
```

Keep in mind that the frequency at which the engine calls `_process()` depends on your application's framerate, which varies over time and across devices.

The function's `delta` parameter is the time elapsed in seconds since the previous call to `_process()`. Use this parameter to make calculations independent of the framerate. For example, you should always multiply a speed value by `delta` to animate a moving object.

Physics processing works with a similar virtual function: `_physics_process()`. Use it for calculations that must happen before each physics step, like moving a character that collides with the game world. As mentioned above, `_physics_process()` runs at fixed time intervals as much as possible to keep the physics interactions stable. You can change the interval between physics steps in the Project Settings, under Physics -> Common -> Physics Fps. By default, it's set to run 60 times per second.

The engine calls this method before every physics step:

```gdscript
func _physics_process(delta):
    # Do something...
    pass
```

The function `_process()` is not synchronized with physics. Its rate depends on hardware and game optimization. It also runs after the physics step in single-threaded games.

You can see the `_process()` function at work by creating a scene with a single Label node, with the following script attached to it:

```gdscript
extends Label

var time = 0

func _process(delta):
    time += delta
    text = str(time) # 'text' is a built-in Label property.
```

When you run the scene, you should see a counter increasing each frame.

---
