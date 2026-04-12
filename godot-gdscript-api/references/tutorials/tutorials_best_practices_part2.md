# Godot 4 GDScript Tutorials — Best Practices (Part 2)

> 4 tutorials. GDScript-specific code examples.

## Scene organization

This article covers topics related to the effective organization of scene content. Which nodes should you use? Where should you place them? How should they interact?

### How to build relationships effectively

When Godot users begin crafting their own scenes, they often run into the following problem:

They create their first scene and fill it with content only to eventually end up saving branches of their scene into separate scenes as the nagging feeling that they should split things up starts to accumulate. However, they then notice that the hard references they were able to rely on before are no longer possible. Re-using the scene in multiple places creates issues because the node paths do not find their targets and signal connections established in the editor break.

To fix these problems, you must instantiate the sub-scenes without them requiring details about their environment. You need to be able to trust that the sub-scene will create itself without being picky about how it's used.

One of the biggest things to consider in OOP is maintaining focused, singular-purpose classes with [loose coupling](https://en.wikipedia.org/wiki/Loose_coupling) to other parts of the codebase. This keeps the size of objects small (for maintainability) and improves their reusability.

These OOP best practices have _several_ implications for best practices in scene structure and script usage.

**If at all possible, you should design scenes to have no dependencies.** That is, you should create scenes that keep everything they need within themselves.

If a scene must interact with an external context, experienced developers recommend the use of [Dependency Injection](https://en.wikipedia.org/wiki/Dependency_injection). This technique involves having a high-level API provide the dependencies of the low-level API. Why do this? Because classes which rely on their external environment can inadvertently trigger bugs and unexpected behavior.

To do this, you must expose data and then rely on a parent context to initialize it:

1. Connect to a signal. Extremely safe, but should be used only to "respond" to behavior, not start it. By convention, signal names are usually past-tense verbs like "entered", "skill_activated", or "item_collected".

```gdscript
# Parent
$Child.signal_name.connect(method_on_the_object)

# Child
signal_name.emit() # Triggers parent-specified behavior.
```

2. Call a method. Used to start behavior.

```gdscript
# Parent
$Child.method_name = "do"

# Child, assuming it has String property 'method_name' and method 'do'.
call(method_name) # Call parent-specified method (which child must own).
```

3. Initialize a [Callable](../godot_gdscript_misc.md) property. Safer than a method as ownership of the method is unnecessary. Used to start behavior.

```gdscript
# Parent
$Child.func_property = object_with_method.method_on_the_object

# Child
func_property.call() # Call parent-specified method (can come from anywhere).
```

4. Initialize a Node or other Object reference.

```gdscript
# Parent
$Child.target = self

# Child
print(target) # Use parent-specified node.
```

5. Initialize a NodePath.

```gdscript
# Parent
$Child.target_path = ".."

# Child
get_node(target_path) # Use parent-specified NodePath.
```

These options hide the points of access from the child node. This in turn keeps the child **loosely coupled** to its environment. You can reuse it in another context without any extra changes to its API.

> **Note:** Although the examples above illustrate parent-child relationships, the same principles apply towards all object relations. Nodes which are siblings should only be aware of their own hierarchies while an ancestor mediates their communications and references. ```gdscript

# Parent

$Left.target = $Right.get_node("Receiver")

# Left

var target: Node
func execute(): # Do something with 'target'.

# Right

func \_init():
var receiver = Receiver.new()
add_child(receiver)

````The same principles also apply to non-Node objects that maintain dependencies on other objects. Whichever object owns the other objects should manage the relationships between them.



> **Warning:** You should favor keeping data in-house (internal to a scene), though, as placing a dependency on an external context, even a loosely coupled one, still means that the node will expect something in its environment to be true. The project's design philosophies should prevent this from happening. If not, the code's inherent liabilities will force developers to use documentation to keep track of object relations on a microscopic scale; this is otherwise known as development hell. Writing code that relies on external documentation to use it safely is error-prone by default. To avoid creating and maintaining such documentation, you convert the dependent node ("child" above) into a tool script that implements `_get_configuration_warnings()`. Returning a non-empty PackedStringArray from it will make the Scene dock generate a warning icon with the string(s) as a tooltip by the node. This is the same icon that appears for nodes such as the [Area2D](../godot_gdscript_physics.md) node when it has no child [CollisionShape2D](../godot_gdscript_nodes_2d.md) nodes defined. The editor then self-documents the scene through the script code. No content duplication via documentation is necessary. A GUI like this can better inform project users of critical information about a Node. Does it have external dependencies? Have those dependencies been satisfied? Other programmers, and especially designers and writers, will need clear instructions in the messages telling them what to do to configure it.



So, why does all this complex switcheroo work? Well, because scenes operate best when they operate alone. If unable to work alone, then working with others anonymously (with minimal hard dependencies, i.e. loose coupling) is the next best thing. Inevitably, changes may need to be made to a class, and if these changes cause it to interact with other scenes in unforeseen ways, then things will start to break down. The whole point of all this indirection is to avoid ending up in a situation where changing one class results in adversely affecting other classes dependent on it.



Scripts and scenes, as extensions of engine classes, should abide by *all* OOP principles. Examples include...



- [SOLID](https://en.wikipedia.org/wiki/SOLID)
- [DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself)
- [KISS](https://en.wikipedia.org/wiki/KISS_principle)
- [YAGNI](https://en.wikipedia.org/wiki/You_aren%27t_gonna_need_it)



### Choosing a node tree structure



You might start to work on a game but get overwhelmed by the vast possibilities before you. You might know what you want to do, what systems you want to have, but *where* do you put them all? How you go about making your game is always up to you. You can construct node trees in countless ways. If you are unsure, this guide can give you a sample of a decent structure to start with.



A game should always have an "entry point"; somewhere you can definitively track where things begin so that you can follow the logic as it continues elsewhere. It also serves as a bird's eye view of all other data and logic in the program. For traditional applications, this is normally a "main" function. In Godot, it's a Main node.



- Node "Main" (main.gd)



The `main.gd` script will serve as the primary controller of your game.



Then you have an in-game "World" (a 2D or 3D one). This can be a child of Main. In addition, you will need a primary GUI for your game that manages the various menus and widgets the project needs.



- **Node "Main" (main.gd)**
: - Node2D/Node3D "World" (game_world.gd)
- Control "GUI" (gui.gd)



When changing levels, you can then swap out the children of the "World" node. [Changing scenes manually](tutorials_scripting.md) gives you full control over how your game world transitions.



The next step is to consider what gameplay systems your project requires. If you have a system that...



1. tracks all of its data internally
2. should be globally accessible
3. should exist in isolation



... then you should create an [autoload 'singleton' node](tutorials_scripting.md).



> **Note:** For smaller games, a simpler alternative with less control would be to have a "Game" singleton that simply calls the [SceneTree.change_scene_to_file()](../godot_gdscript_core.md) method to swap out the main scene's content. This structure more or less keeps the "World" as the main game node. Any GUI would also need to be either a singleton, a transitory part of the "World", or manually added as a direct child of the root. Otherwise, the GUI nodes would also delete themselves during scene transitions.



If you have systems that modify other systems' data, you should define those as their own scripts or scenes, rather than autoloads. For more information, see Autoloads versus regular nodes.



Each subsystem within your game should have its own section within the SceneTree. You should use parent-child relationships only in cases where nodes are effectively elements of their parents. Does removing the parent reasonably mean that the children should also be removed? If not, then it should have its own place in the hierarchy as a sibling or some other relation.



> **Note:** In some cases, you need these separated nodes to *also* position themselves relative to each other. You can use the [RemoteTransform](../godot_gdscript_misc.md) / [RemoteTransform2D](../godot_gdscript_nodes_2d.md) nodes for this purpose. They will allow a target node to conditionally inherit selected transform elements from the Remote* node. To assign the `target` [NodePath](../godot_gdscript_misc.md), use one of the following: 1. A reliable third party, likely a parent node, to mediate the assignment.
2. A group, to pull a reference to the desired node (assuming there will only ever be one of the targets). When you should do this is subjective. The dilemma arises when you must micro-manage when a node must move around the SceneTree to preserve itself. For example... - Add a "player" node to a "room".
- Need to change rooms, so you must delete the current room.
- Before the room can be deleted, you must preserve and/or move the player.



If memory is not a concern, you can...



- Create the new room.
- Move the player to the new room.
- Delete the old room.



If memory is a concern, instead you will need to...



- Move the player somewhere else in the tree.
- Delete the room.
- Instantiate and add the new room.
- Re-add the player to the new room. The issue is that the player here is a "special case" where the developers must *know* that they need to handle the player this way for the project. The only way to reliably share this information as a team is to *document* it. Keeping implementation details in documentation is dangerous. It's a maintenance burden, strains code readability, and unnecessarily bloats the intellectual content of a project. In a more complex game with larger assets, it can be a better idea to keep the player somewhere else in the SceneTree entirely. This results in: 1. More consistency.
2. No "special cases" that must be documented and maintained somewhere.
3. No opportunity for errors to occur because these details are not accounted for. In contrast, if you ever need a child node that does *not* inherit the transform of its parent, you have the following options: 1. The **declarative** solution: place a [Node](../godot_gdscript_core.md) in between them. Since it doesn't have a transform, they won't pass this information to its children.
2. The **imperative** solution: Use the `top_level` property for the [CanvasItem](../godot_gdscript_nodes_2d.md) or [Node3D](../godot_gdscript_nodes_3d.md) node. This will make the node ignore its inherited transform.



> **Note:** If building a networked game, keep in mind which nodes and gameplay systems are relevant to all players versus those just pertinent to the authoritative server. For example, users do not all need to have a copy of every players' "PlayerController" logic - they only need their own. Keeping them in a separate branch from the "world" can help simplify the management of game connections and the like.



The key to scene organization is to consider the SceneTree in relational terms rather than spatial terms. Are the nodes dependent on their parent's existence? If not, then they can thrive all by themselves somewhere else. If they are dependent, then it stands to reason that they should be children of that parent (and likely part of that parent's scene if they aren't already).



Does this mean nodes themselves are components? Not at all. Godot's node trees form an aggregation relationship, not one of composition. But while you still have the flexibility to move nodes around, it is still best when such moves are unnecessary by default.

---

## When to use scenes versus scripts

We've already covered how scenes and scripts are different. Scripts define an engine class extension with imperative code, scenes with declarative code.



Each system's capabilities are different as a result. Scenes can define how an extended class initializes, but not what its behavior actually is. Scenes are often used in conjunction with a script, the scene declaring a composition of nodes, and the script adding behavior with imperative code.



### Anonymous types



It *is* possible to completely define a scenes' contents using a script alone. This is, in essence, what the Godot Editor does, only in the C++ constructor of its objects.



But, choosing which one to use can be a dilemma. Creating script instances is identical to creating in-engine classes whereas handling scenes requires a change in API:


```gdscript
const MyNode = preload("my_node.gd")
const MyScene = preload("my_scene.tscn")
var node = Node.new()
var my_node = MyNode.new() # Same method call.
var my_scene = MyScene.instantiate() # Different method call.
var my_inherited_scene = MyScene.instantiate(PackedScene.GEN_EDIT_STATE_MAIN) # Create scene inheriting from MyScene.
````

Also, scripts will operate a little slower than scenes due to the speed differences between engine and script code. The larger and more complex the node, the more reason there is to build it as a scene.

### Named types

Scripts can be registered as a new type within the editor itself. This displays it as a new type in the node or resource creation dialog with an optional icon. This way, the user's ability to use the script is much more streamlined. Rather than having to...

1. Know the base type of the script they would like to use.
2. Create an instance of that base type.
3. Add the script to the node.

With a registered script, the scripted type instead becomes a creation option like the other nodes and resources in the system. The creation dialog even has a search bar to look up the type by name.

There are two systems for registering types:

- [Custom Types](tutorials_editor.md)

- Editor-only. Typenames are not accessible at runtime.
- Does not support inherited custom types.
- An initializer tool. Creates the node with the script. Nothing more.
- Editor has no type-awareness of the script or its relationship to other engine types or scripts.
- Allows users to define an icon.
- Works for all scripting languages because it deals with Script resources in abstract.
- Set up using [EditorPlugin.add_custom_type](../godot_gdscript_editor.md).
- [Script Classes](tutorials_scripting.md)

- Editor and runtime accessible.
- Displays inheritance relationships in full.
- Creates the node with the script, but can also change types or extend the type from the editor.
- Editor is aware of inheritance relationships between scripts, script classes, and engine C++ classes.
- Allows users to define an icon.
- Engine developers must add support for languages manually (both name exposure and runtime accessibility).
- The Editor scans project folders and registers any exposed names for all scripting languages. Each scripting language must implement its own support for exposing this information.

Both methodologies add names to the creation dialog, but script classes, in particular, also allow for users to access the typename without loading the script resource. Creating instances and accessing constants or static methods is viable from anywhere.

With features like these, one may wish their type to be a script without a scene due to the ease of use it grants users. Those developing plugins or creating in-house tools for designers to use will find an easier time of things this way.

On the downside, it also means having to use largely imperative programming.

### Performance of Script vs PackedScene

One last aspect to consider when choosing scenes and scripts is execution speed.

As the size of objects increases, the scripts' necessary size to create and initialize them grows much larger. Creating node hierarchies demonstrates this. Each Node's logic could be several hundred lines of code in length.

The code example below creates a new `Node`, changes its name, assigns a script to it, sets its future parent as its owner so it gets saved to disk along with it, and finally adds it as a child of the `Main` node:

```gdscript
# main.gd
extends Node

func _init():
    var child = Node.new()
    child.name = "Child"
    child.script = preload("child.gd")
    add_child(child)
    child.owner = self
```

Script code like this is much slower than engine-side C++ code. Each instruction makes a call to the scripting API which leads to many "lookups" on the back-end to find the logic to execute.

Scenes help to avoid this performance issue. [PackedScene](../godot_gdscript_resources.md), the base type that scenes inherit from, defines resources that use serialized data to create objects. The engine can process scenes in batches on the back-end and provide much better performance than scripts.

### Conclusion

In the end, the best approach is to consider the following:

- If one wishes to create a basic tool that is going to be re-used in several different projects and which people of all skill levels will likely use (including those who don't label themselves as "programmers"), then chances are that it should probably be a script, likely one with a custom name/icon.
- If one wishes to create a concept that is particular to their game, then it should always be a scene. Scenes are easier to track/edit and provide more security than scripts.
- If one would like to give a name to a scene, then they can still sort of do this by declaring a script class and giving it a scene as a constant. The script becomes, in effect, a namespace:

```gdscript
# game.gd
class_name Game # extends RefCounted, so it won't show up in the node creation dialog.
extends RefCounted

const MyScene = preload("my_scene.tscn")

# main.gd
extends Node
func _ready():
    add_child(Game.MyScene.instantiate())
```

---

## Version control systems

### Introduction

Godot aims to be VCS-friendly and generate mostly readable and mergeable files.

### Version control plugins

Godot also supports the use of version control systems in the editor itself. However, version control in the editor requires a plugin for the specific VCS you're using.

As of October 2025, there is only a Git plugin available, but the community may create additional VCS plugins.

#### Official Git plugin

Using Git from inside the editor is supported with an official plugin. You can find the latest releases on [GitHub](https://github.com/godotengine/godot-git-plugin/releases).

Documentation on how to use the Git plugin can be found on its [wiki](https://github.com/godotengine/godot-git-plugin/wiki).

### Files to exclude from VCS

> **Note:** This lists files and folders that should be ignored from version control in Godot 4.1 and later. The list of files of folders that should be ignored from version control in Godot 3.x and Godot 4.0 is **entirely** different. This is important, as Godot 3.x and 4.0 may store sensitive credentials in `export_presets.cfg` (unlike Godot 4.1 and later). If you are using Godot 3, check the `3.6` version of this documentation page instead.

There are some files and folders Godot automatically creates when opening a project in the editor for the first time. To avoid bloating your version control repository with generated data, you should add them to your VCS ignore:

- `.godot/`: This folder stores various project cache data.
- `*.translation`: These files are binary imported [translations](tutorials_i18n.md) generated from CSV files.

You can make the Godot project manager generate version control metadata for you automatically when creating a project. When choosing the **Git** option, this creates `.gitignore` and `.gitattributes` files in the project root:

In existing projects, select the **Project** menu at the top of the editor, then choose **Version Control > Generate Version Control Metadata**. This creates the same files as if the operation was performed in the project manager.

### Working with Git on Windows

Most Git for Windows clients are configured with the `core.autocrlf` set to `true`. This can lead to files unnecessarily being marked as modified by Git due to their line endings being converted from LF to CRLF automatically.

It is better to set this option as:

```gdscript
git config --global core.autocrlf input
```

Creating version control metadata using the project manager or editor will automatically enforce LF line endings using the `.gitattributes` file. In this case, you don't need to change your Git configuration.

### Git LFS

Git LFS (Large File Storage) is a Git extension that allows you to manage large files in your repository. It replaces large files with text pointers inside Git, while storing the file contents on a remote server. This is useful for managing large assets, such as textures, audio files, and 3D models, without bloating your Git repository.

> **Note:** When using Git LFS you will want to ensure it is setup before you commit any files to your repository. If you have already committed files to your repository, you will need to remove them from the repository and re-add them after setting up Git LFS. It is possible to use `git lfs migrate` to convert existing files in your repository, but this is more in-depth and requires a good understanding of Git. A common approach is setting up a new repository with Git LFS (and a proper `.gitattributes`), then copying the files from the old repository to the new one. This way, you can ensure that all files are tracked by LFS from the start.

To use Git LFS with Godot, you need to install the Git LFS extension and configure it to track the file types you want to manage. You can do this by running the following command in your terminal:

```gdscript
git lfs install
```

This will create a `.gitattributes` file in your repository that tells Git to use LFS for the specified file types. You can add more file types by modifying the `.gitattributes` file. For example, to track all GLB files, you can do this by running the following command in your terminal:

```gdscript
git lfs track "*.glb"
```

When you add or modify files that are tracked by LFS, Git will automatically store them in LFS instead of the regular Git history. You can push and pull LFS files just like regular Git files, but keep in mind that LFS files are stored separately from the rest of your Git history. This means that you may need to install Git LFS on any machine that you clone the repository to in order to access the LFS files.

Below is an example `.gitattributes` file that you can use as a starting point for Git LFS. These file types were chosen because they are commonly used, but you can modify the list to include any binary types you may have in your project.

```unixconfig
# Normalize EOL for all files that Git considers text files.
* text=auto eol=lf

# Git LFS Tracking (Assets)

# 3D Models
*.fbx filter=lfs diff=lfs merge=lfs -text
*.gltf filter=lfs diff=lfs merge=lfs -text
*.glb filter=lfs diff=lfs merge=lfs -text
*.blend filter=lfs diff=lfs merge=lfs -text
*.obj filter=lfs diff=lfs merge=lfs -text

# Images
*.png filter=lfs diff=lfs merge=lfs -text
*.svg filter=lfs diff=lfs merge=lfs -text
*.jpg filter=lfs diff=lfs merge=lfs -text
*.jpeg filter=lfs diff=lfs merge=lfs -text
*.gif filter=lfs diff=lfs merge=lfs -text
*.tga filter=lfs diff=lfs merge=lfs -text
*.webp filter=lfs diff=lfs merge=lfs -text
*.exr filter=lfs diff=lfs merge=lfs -text
*.hdr filter=lfs diff=lfs merge=lfs -text
*.dds filter=lfs diff=lfs merge=lfs -text

# Audio
*.mp3 filter=lfs diff=lf
# ...
```

For more information on Git LFS, check the official documentation: [https://git-lfs.github.com/](https://git-lfs.github.com/) and [https://docs.github.com/en/repositories/working-with-files/managing-large-files](https://docs.github.com/en/repositories/working-with-files/managing-large-files).

---

## Applying object-oriented principles in Godot

The engine offers two main ways to create reusable objects: scripts and scenes. Neither of these technically define classes under the hood.

Still, many best practices using Godot involve applying object-oriented programming principles to the scripts and scenes that compose your game. That is why it's useful to understand how we can think of them as classes.

This guide briefly explains how scripts and scenes work in the engine's core to help you understand how they work under the hood.

### How scripts work in the engine

The engine provides built-in classes like [Node](../godot_gdscript_core.md). You can extend those to create derived types using a script.

These scripts are not technically classes. Instead, they are resources that tell the engine a sequence of initializations to perform on one of the engine's built-in classes.

Godot's internal classes have methods that register a class's data with a [ClassDB](../godot_gdscript_core.md). This database provides runtime access to class information. `ClassDB` contains information about classes like:

- Properties.
- Methods.
- Constants.
- Signals.

This `ClassDB` is what objects check against when performing an operation like accessing a property or calling a method. It checks the database's records and the object's base types' records to see if the object supports the operation.

Attaching a [Script](../godot_gdscript_resources.md) to your object extends the methods, properties, and signals available from the `ClassDB`.

> **Note:** Even scripts that don't use the `extends` keyword implicitly inherit from the engine's base [RefCounted](../godot_gdscript_core.md) class. As a result, you can instantiate scripts without the `extends` keyword from code. Since they extend `RefCounted` though, you cannot attach them to a [Node](../godot_gdscript_core.md).

### Scenes

The behavior of scenes has many similarities to classes, so it can make sense to think of a scene as a class. Scenes are reusable, instantiable, and inheritable groups of nodes. Creating a scene is similar to having a script that creates nodes and adds them as children using `add_child()`.

We often pair a scene with a scripted root node that makes use of the scene's nodes. As such, the script extends the scene by adding behavior through imperative code.

The content of a scene helps to define:

- What nodes are available to the script.
- How they are organized.
- How they are initialized.
- What signal connections they have with each other.

Why is any of this important to scene organization? Because instances of scenes _are_ objects. As a result, many object-oriented principles that apply to written code also apply to scenes: single responsibility, encapsulation, and others.

The scene is _always an extension of the script attached to its root node_, so you can interpret it as part of a class.

Most of the techniques explained in this best practices series build on this point.

---
