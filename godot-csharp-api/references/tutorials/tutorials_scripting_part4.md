# Godot 4 C# Tutorials — Scripting (Part 4)

> 6 tutorials. C#-specific code examples.

## Getting started

### Workflow overview

As a GDExtension, godot-cpp is more complicated to use than GDScript and C#. If you decide to work with it, here's what to expect your workflow to look like:

- Create a new godot-cpp project (from the [template](https://github.com/godotengine/godot-cpp-template), or from scratch, as explained below).
- Develop your code with your favorite IDE locally.
- Build and test your code with the earliest compatible Godot version.
- Create builds for all platforms you want to support (e.g. using [GitHub Actions](https://github.com/godotengine/godot-cpp-template/blob/main/.github/workflows/make_build.yml)).
- Optional: Publish on the [Godot Asset Library](https://godotengine.org/asset-library/asset).

### Example project

For your first godot-cpp project, we recommend starting with this guide to understand the technology involved with godot-cpp. After you're done, you can use the [godot-cpp template](https://github.com/godotengine/godot-cpp-template), which has better coverage of features, such as a GitHub action pipeline and useful `SConstruct` boilerplate code. However, the template does not explain itself to a high level of detail, which is why we recommend going through this guide first.

### Setting up the project

There are a few prerequisites you'll need:

- A Godot 4 executable.
- A C++ compiler.
- SCons as a build tool.
- A copy of the [godot-cpp repository](https://github.com/godotengine/godot-cpp).

See also Configuring an IDE and Compiling as the build tools are identical to the ones you need to compile Godot from source.

You can download the [godot-cpp repository](https://github.com/godotengine/godot-cpp) from GitHub or let Git do the work for you. Note that this repository has different branches for different versions of Godot. GDExtensions will not work in older versions of Godot (only Godot 4 and up) and vice versa, so make sure you download the correct branch.

> **Note:** To use [GDExtension](https://godotengine.org/article/introducing-gd-extensions) you need to use the godot-cpp branch that matches the version of Godot that you are targeting. For example, if you're targeting Godot 4.1, use the `4.1` branch. Throughout this tutorial we use `4.x`, which will need to be replaced with the version of Godot you are targeting. The `master` branch is the development branch which is updated regularly to work with Godot's `master` branch.

> **Warning:** GDExtensions targeting an earlier version of Godot should work in later minor versions, but not vice-versa. For example, a GDExtension targeting Godot 4.2 should work just fine in Godot 4.3, but one targeting Godot 4.3 won't work in Godot 4.2. There is one exception to this: extensions targeting Godot 4.0 will **not** work with Godot 4.1 and later (see [Updating your GDExtension for 4.1](tutorials_migrating.md)).

If you are versioning your project using Git, it is recommended to add it as a Git submodule:

```none
mkdir gdextension_cpp_example
cd gdextension_cpp_example
git init
git submodule add -b 4.x https://github.com/godotengine/godot-cpp
cd godot-cpp
git submodule update --init
```

Alternatively, you can also clone it to the project folder:

```none
mkdir gdextension_cpp_example
cd gdextension_cpp_example
git clone -b 4.x https://github.com/godotengine/godot-cpp
```

> **Note:** If you decide to download the repository or clone it into your folder, make sure to keep the folder layout the same as we've setup here. Much of the code we'll be showcasing here assumes the project has this layout.

If you cloned the example from the link specified in the introduction, the submodules are not automatically initialized. You will need to execute the following commands:

```none
cd gdextension_cpp_example
git submodule update --init
```

This will initialize the repository in your project folder.

### Creating a simple plugin

Now it's time to build an actual plugin. We'll start by creating an empty Godot project in which we'll place a few files.

Open Godot and create a new project. For this example, we will place it in a folder called `project` inside our GDExtension's folder structure.

In our project, we'll create a scene containing a Node called "Main" and we'll save it as `main.tscn`. We'll come back to that later.

Back in the top-level GDExtension module folder, we're also going to create a subfolder called `src` in which we'll place our source files.

You should now have `project`, `godot-cpp`, and `src` directories in your GDExtension module.

Your folder structure should now look like this:

```none
gdextension_cpp_example/
|
+--project/                  # game example/demo to test the extension
|
+--godot-cpp/             # C++ bindings
|
+--src/                   # source code of the extension we are building
```

In the `src` folder, we'll start with creating our header file for the GDExtension node we'll be creating. We will name it `gdexample.h`:

gdextension_cpp_example/src/gdexample.h

```cpp
#pragma once

#include <godot_cpp/classes/sprite2d.hpp>

namespace godot {

class GDExample : public Sprite2D {
    GDCLASS(GDExample, Sprite2D)

private:
    double time_passed;

protected:
    static void _bind_methods();

public:
    GDExample();
    ~GDExample();

    void _process(double delta) override;
};

} // namespace godot
```

There are a few things of note to the above. We include `sprite2d.hpp` which contains bindings to the Sprite2D class. We'll be extending this class in our module.

We're using the namespace `godot`, since everything in GDExtension is defined within this namespace.

Then we have our class definition, which inherits from our Sprite2D through a container class. We'll see a few side effects of this later on. The `GDCLASS` macro sets up a few internal things for us.

After that, we declare a single member variable called `time_passed`.

In the next block we're defining our methods, we have our constructor and destructor defined, but there are two other functions that will likely look familiar to some, and one new method.

The first is `_bind_methods`, which is a static function that Godot will call to find out which methods can be called and which properties it exposes. The second is our `_process` function, which will work exactly the same as the `_process` function you're used to in GDScript.

Let's implement our functions by creating our `gdexample.cpp` file:

gdextension_cpp_example/src/gdexample.cpp

```cpp
#include "gdexample.h"
#include <godot_cpp/core/class_db.hpp>

using namespace godot;

void GDExample::_bind_methods() {
}

GDExample::GDExample() {
    // Initialize any variables here.
    time_passed = 0.0;
}

GDExample::~GDExample() {
    // Add your cleanup here.
}

void GDExample::_process(double delta) {
    time_passed += delta;

    Vector2 new_position = Vector2(10.0 + (10.0 * sin(time_passed * 2.0)), 10.0 + (10.0 * cos(time_passed * 1.5)));

    set_position(new_position);
}
```

This one should be straightforward. We're implementing each method of our class that we defined in our header file.

Note our `_process` function, which keeps track of how much time has passed and calculates a new position for our sprite using a sine and cosine function.

There is one more C++ file we need; we'll name it `register_types.cpp`. Our GDExtension plugin can contain multiple classes, each with their own header and source file like we've implemented `GDExample` up above. What we need now is a small bit of code that tells Godot about all the classes in our GDExtension plugin.

gdextension_cpp_example/src/register_types.cpp

```cpp
#include "register_types.h"

#include "gdexample.h"

#include <gdextension_interface.h>
#include <godot_cpp/core/defs.hpp>
#include <godot_cpp/godot.hpp>

using namespace godot;

void initialize_example_module(ModuleInitializationLevel p_level) {
    if (p_level != MODULE_INITIALIZATION_LEVEL_SCENE) {
        return;
    }

    GDREGISTER_CLASS(GDExample);
}

void uninitialize_example_module(ModuleInitializationLevel p_level) {
    if (p_level != MODULE_INITIALIZATION_LEVEL_SCENE) {
        return;
    }
}

extern "C" {
// Initialization.
GDExtensionBool GDE_EXPORT example_library_init(GDExtensionInterfaceGetProcAddress p_get_proc_address, const GDExtensionClassLibraryPtr p_library, GDExtensionInitialization *r_initialization) {
    godot::GDExtensionBinding::InitObject init_obj(p_get_proc
# ...
```

The `initialize_example_module` and `uninitialize_example_module` functions get called respectively when Godot loads our plugin and when it unloads it. All we're doing here is parse through the functions in our bindings module to initialize them, but you might have to set up more things depending on your needs. We call the `GDREGISTER_CLASS` macro for each of our classes in our library.

> **Note:** You can find information about `GDREGISTER_CLASS` (and alternatives) at Object class.

The important function is the third function called `example_library_init`. We first call a function in our bindings library that creates an initialization object. This object registers the initialization and termination functions of the GDExtension. Furthermore, it sets the level of initialization (core, servers, scene, editor, level).

At last, we need the header file for the `register_types.cpp` named `register_types.h`.

gdextension_cpp_example/src/register_types.h

```cpp
#pragma once

#include <godot_cpp/core/class_db.hpp>

using namespace godot;

void initialize_example_module(ModuleInitializationLevel p_level);
void uninitialize_example_module(ModuleInitializationLevel p_level);
```

### Compiling the plugin

To compile the project we need to define how SCons using should compile it using an `SConstruct` file which references the one in `godot-cpp`. Writing it from scratch is outside the scope of this tutorial, but you can the SConstruct file we prepared. We'll cover a more customizable, detailed example on how to use these build files in a subsequent tutorial.

> **Note:** This `SConstruct` file was written to be used with the latest `godot-cpp` master, you may need to make small changes using it with older versions or refer to the `SConstruct` file in the Godot 4.x documentation.

Once you've downloaded the `SConstruct` file, place it in your GDExtension folder structure alongside `godot-cpp`, `src`, and `project`, then run:

```bash
scons platform=<platform>
```

You should now be able to find the module in `project/bin/<platform>`.

> **Note:** Here, we've compiled both godot-cpp and our gdexample library as debug builds. For optimized builds, you should compile them using the `target=template_release` switch.

### Using the GDExtension module

Before we jump back into Godot, we need to create one more file in `project/bin/`.

This file lets Godot know what dynamic libraries should be loaded for each platform and the entry function for the module. It is called `gdexample.gdextension`.

```none
[configuration]

entry_symbol = "example_library_init"
compatibility_minimum = "4.1"
reloadable = true

[libraries]

macos.debug = "./libgdexample.macos.template_debug.dylib"
macos.release = "./libgdexample.macos.template_release.dylib"
windows.debug.x86_32 = "./gdexample.windows.template_debug.x86_32.dll"
windows.release.x86_32 = "./gdexample.windows.template_release.x86_32.dll"
windows.debug.x86_64 = "./gdexample.windows.template_debug.x86_64.dll"
windows.release.x86_64 = "./gdexample.windows.template_release.x86_64.dll"
linux.debug.x86_64 = "./libgdexample.linux.template_debug.x86_64.so"
linux.release.x86_64 = "./libgdexample.linux.template_release.x86_64.so"
linux.debug.arm64 = "./libgdexample.linux.template_debug.arm64.so"
linux.release.arm64 = "./libgdexample.linux.template_release.a
# ...
```

This file contains a `configuration` section that controls the entry function of the module. You should also set the minimum compatible Godot version with `compatibility_minimum`, which prevents older version of Godot from trying to load your extension. The `reloadable` flag enables automatic reloading of your extension by the editor every time you recompile it, without needing to restart the editor. This only works if you compile your extension in debug mode (default).

The `libraries` section is the important bit: it tells Godot the location of the dynamic library in the project's filesystem for each supported platform. It will also result in _just_ that file being exported when you export the project, which means the data pack won't contain libraries that are incompatible with the target platform.

You can learn more about `.gdextension` files at The .gdextension file.

Here is another overview to check the correct file structure:

```none
gdextension_cpp_example/
|
+--project/                  # game example/demo to test the extension
|   |
|   +--main.tscn
|   |
|   +--bin/
|       |
|       +--gdexample.gdextension
|
+--godot-cpp/             # C++ bindings
|
+--src/                   # source code of the extension we are building
|   |
|   +--register_types.cpp
|   +--register_types.h
|   +--gdexample.cpp
|   +--gdexample.h
```

Time to jump back into Godot. We load up the main scene we created way back in the beginning and now add a newly available GDExample node to the scene:

We're going to assign the Godot logo to this node as our texture, disable the `centered` property:

We're finally ready to run the project:

### Adding properties

GDScript allows you to add properties to your script using the `export` keyword. In GDExtension you have to register the properties with a getter and setter function or directly implement the `_get_property_list`, `_get` and `_set` methods of an object (but that goes far beyond the scope of this tutorial).

Lets add a property that allows us to control the amplitude of our wave.

In our `gdexample.h` file we need to add a member variable and getter and setter functions:

```cpp
...
private:
    double time_passed;
    double amplitude;

public:
    void set_amplitude(const double p_amplitude);
    double get_amplitude() const;
...
```

In our `gdexample.cpp` file we need to make a number of changes, we will only show the methods we end up changing, don't remove the lines we're omitting:

```cpp
void GDExample::_bind_methods() {
    ClassDB::bind_method(D_METHOD("get_amplitude"), &GDExample::get_amplitude);
    ClassDB::bind_method(D_METHOD("set_amplitude", "p_amplitude"), &GDExample::set_amplitude);

    ADD_PROPERTY(PropertyInfo(Variant::FLOAT, "amplitude"), "set_amplitude", "get_amplitude");
}

GDExample::GDExample() {
    // Initialize any variables here.
    time_passed = 0.0;
    amplitude = 10.0;
}

void GDExample::_process(double delta) {
    time_passed += delta;

    Vector2 new_position = Vector2(
        amplitude + (amplitude * sin(time_passed * 2.0)),
        amplitude + (amplitude * cos(time_passed * 1.5))
    );

    set_position(new_position);
}

void GDExample::set_amplitude(const double p_amplitude) {
    amplitude = p_amplitude;
}

double GDExample::get_amplitu
# ...
```

Once you compile the module with these changes in place, you will see that a property has been added to our interface. You can now change this property and when you run your project, you will see that our Godot icon travels along a larger figure.

Let's do the same but for the speed of our animation and use a setter and getter function. Our `gdexample.h` header file again only needs a few more lines of code:

```cpp
...
    double amplitude;
    double speed;
...
    void _process(double delta) override;
    void set_speed(const double p_speed);
    double get_speed() const;
...
```

This requires a few more changes to our `gdexample.cpp` file, again we're only showing the methods that have changed so don't remove anything we're omitting:

```cpp
void GDExample::_bind_methods() {
    ...
    ClassDB::bind_method(D_METHOD("get_speed"), &GDExample::get_speed);
    ClassDB::bind_method(D_METHOD("set_speed", "p_speed"), &GDExample::set_speed);

    ADD_PROPERTY(PropertyInfo(Variant::FLOAT, "speed", PROPERTY_HINT_RANGE, "0,20,0.01"), "set_speed", "get_speed");
}

GDExample::GDExample() {
    time_passed = 0.0;
    amplitude = 10.0;
    speed = 1.0;
}

void GDExample::_process(double delta) {
    time_passed += speed * delta;

    Vector2 new_position = Vector2(
        amplitude + (amplitude * sin(time_passed * 2.0)),
        amplitude + (amplitude * cos(time_passed * 1.5))
    );

    set_position(new_position);
}

...

void GDExample::set_speed(const double p_speed) {
    speed = p_speed;
}

double GDExample::get_speed() const {
    r
# ...
```

Now when the project is compiled, we'll see another property called speed. Changing its value will make the animation go faster or slower. Furthermore, we added a property range which describes in which range the value can be. The first two arguments are the minimum and maximum value and the third is the step size.

> **Note:** For simplicity, we've only used the hint_range of the property method. There are a lot more options to choose from. These can be used to further configure how properties are displayed and set on the Godot side.

### Signals

Last but not least, signals fully work in GDExtension as well. Having your extension react to a signal given out by another object requires you to call `connect` on that object. We can't think of a good example for our wobbling Godot icon, we would need to showcase a far more complete example.

This is the required syntax:

```cpp
some_other_node->connect("the_signal", Callable(this, "my_method"));
```

To connect our signal `the_signal` from some other node with our method `my_method`, we need to provide the `connect` method with the name of the signal and a `Callable`. The `Callable` holds information about an object on which a method can be called. In our case, it associates our current object instance `this` with the method `my_method` of the object. Then the `connect` method will add this to the observers of `the_signal`. Whenever `the_signal` is now emitted, Godot knows which method of which object it needs to call.

Note that you can only call `my_method` if you've previously registered it in your `_bind_methods` method. Otherwise Godot will not know about the existence of `my_method`.

To learn more about `Callable`, check out the class reference here: [Callable](../godot_csharp_misc.md).

Having your object sending out signals is more common. For our wobbling Godot icon, we'll do something silly just to show how it works. We're going to emit a signal every time a second has passed and pass the new location along.

In our `gdexample.h` header file, we need to define a new member `time_emit`:

```cpp
...
    double time_passed;
    double time_emit;
    double amplitude;
...
```

This time, the changes in `gdexample.cpp` are more elaborate. First, you'll need to set `time_emit = 0.0;` in either our `_init` method or in our constructor. We'll look at the other 2 needed changes one by one.

In our `_bind_methods` method, we need to declare our signal. This is done as follows:

```cpp
void GDExample::_bind_methods() {
    ...
    ADD_PROPERTY(PropertyInfo(Variant::FLOAT, "speed", PROPERTY_HINT_RANGE, "0,20,0.01"), "set_speed", "get_speed");

    ADD_SIGNAL(MethodInfo("position_changed", PropertyInfo(Variant::OBJECT, "node"), PropertyInfo(Variant::VECTOR2, "new_pos")));
}
```

Here, our `ADD_SIGNAL` macro can be a single call with a `MethodInfo` argument. `MethodInfo`'s first parameter will be the signal's name, and its remaining parameters are `PropertyInfo` types which describe the essentials of each of the method's parameters. `PropertyInfo` parameters are defined with the data type of the parameter, and then the name that the parameter will have by default.

So here, we add a signal, with a `MethodInfo` which names the signal "position_changed". The `PropertyInfo` parameters describe two essential arguments, one of type `Object`, the other of type `Vector2`, respectively named "node" and "new_pos".

Next, we'll need to change our `_process` method:

```cpp
void GDExample::_process(double delta) {
    time_passed += speed * delta;

    Vector2 new_position = Vector2(
        amplitude + (amplitude * sin(time_passed * 2.0)),
        amplitude + (amplitude * cos(time_passed * 1.5))
    );

    set_position(new_position);

    time_emit += delta;
    if (time_emit > 1.0) {
        emit_signal("position_changed", this, new_position);

        time_emit = 0.0;
    }
}
```

After a second has passed, we emit our signal and reset our counter. We can add our parameter values directly to `emit_signal`.

Once the GDExtension library is compiled, we can go into Godot and select our sprite node. In the **Node** dock, we can find our new signal and link it up by pressing the **Connect** button or double-clicking the signal. We've added a script on our main node and implemented our signal like this:

Every second, we output our position to the console.

### Next steps

We hope the above example showed you the basics. You can build upon this example to create full-fledged scripts to control nodes in Godot using C++!

Instead of basing your project off the above example setup, we recommend to restart now by cloning the [godot-cpp template](https://github.com/godotengine/godot-cpp-template), and base your project off of that. It has better coverage of features, such as a GitHub build action and additional useful `SConstruct` boilerplate.

---

## Adding documentation

> **Note:** Adding documentation for GDExtensions is only possible with Godot 4.3 and later.

The GDExtension documentation system works in a similar manner to the built-in engine documentation: It uses XML files (one per class) to document the exposed constructors, properties, methods, constants, signals, and more.

To get started, identify your project's test project folder, which should contain a Godot project with your extension installed and working. If you are using [godot-cpp-template](https://github.com/godotengine/godot-cpp-template), your GDExtension project already has a `project` folder. Alternatively, you can add one by following the steps described in Getting started. Inside the `project` folder, run the following terminal command:

```shell
# Replace "godot" with the full path to a Godot editor binary
# if Godot is not installed in your `PATH`.
godot --doctool ../ --gdextension-docs
```

This command instructs Godot to generate documentation via the `--doctool` and `--gdextension-docs` commands. The `../` argument specifies the base path of your GDExtension.

After running this command, you should find XML files for your registered GDExtension classes inside the `doc_classes` folder in your GDExtension project. You could edit them now, but for this tutorial, the empty files will suffice.

Now that you have XML files containing your documentation, the next step is to include them in your GDExtension binary. Assuming you are using SCons as your build system, you can add the following lines to your `SConstruct` file. If you are using [godot-cpp-template](https://github.com/godotengine/godot-cpp-template), your file already contains code for this.

```py
if env["target"] in ["editor", "template_debug"]:
    doc_data = env.GodotCPPDocData("src/gen/doc_data.gen.cpp", source=Glob("doc_classes/*.xml"))
    sources.append(doc_data)
```

The `if` statement avoids adding the documentation to release builds of your GDExtension, where it is not needed. SCons then loads all the XML files inside the `doc_classes` directory, and appends the resulting targets to the `sources` array, to be included in your GDExtension build.

After building, launch your Godot project again. You can open the documentation of one of your extension classes either using Ctrl + Click on a class name in the script editor, or inside by finding it in the Editor help dialog. If everything went well, you should see something like this:

### Writing and styling documentation

The format of the class reference XML files is the same as the one used by Godot. Is is documented in Class reference primer.

If you are looking for pointers to write high quality documentation, feel free to refer to Godot's [documentation guidelines](https://contributing.godotengine.org/en/latest/documentation/guidelines/index.html).

### Publishing documentation online

You may want to publish an online reference for your GDExtension, similar to this website. The most important step is to build reStructuredText (`.rst`) files from your XML class reference:

```shell
# You need a version.py file, so download it first.
curl -sSLO https://raw.githubusercontent.com/godotengine/godot/refs/heads/master/version.py

# Edit version.py according to your project before proceeding.
# Then, run the rst generator. You'll need to have Python installed for this command to work.
curl -sSL https://raw.githubusercontent.com/godotengine/godot/master/doc/tools/make_rst.py | python3 - -o "docs/classes" -l "en" doc_classes
```

Your `.rst` files will now be available in `docs/classes/`. From here, you can use any documentation builder that supports reStructuredText syntax to create a website from them.

[godot-docs](https://github.com/godotengine/godot-docs) uses [Sphinx](https://www.sphinx-doc.org/en/master/). You can use the repository as a basis to build your own documentation system. The following guide describes the basic steps, but they are not exhaustive: you will need a bit of personal insight to make it work.

1. Add [godot-docs](https://github.com/godotengine/godot-docs) as a submodule to your `docs/` folder.
2. Copy over its `conf.py`, `index.rst`, `.readthedocs.yaml` files into `/docs/`. You may later decide to copy over and edit more of godot-docs' files, like `_templates/layout.html`.
3. Modify these files according to your project. This mostly involves adjusting paths to point to the `godot-docs` subfolder, as well as strings to reflect it's your project rather than Godot you're building the docs for.
4. Create an account on [readthedocs.org](http://readthedocs.org). Import your project, and modify its base `.readthedocs.yaml` file path to `/docs/.readthedocs.yaml`.

Once you have completed all these steps, your documentation should be available at `<repo-name>.readthedocs.io`.

---

## Creating script templates

Godot provides a way to use script templates as seen in the `Script Create Dialog` while creating a new script:

A set of built-in script templates are provided with the editor, but it is also possible to create new ones and set them by default, both per project and at editor scope.

Templates are linked to a specific node type, so when you create a script you will only see the templates corresponding to that particular node, or one of its parent types. For example, if you are creating a script for a CharacterBody3D, you will only see templates defined for CharacterBody3Ds, Node3Ds or Nodes.

### Locating the templates

There are two places where templates can be managed.

#### Editor-defined templates

These are available globally throughout any project. The location of these templates are determined per each OS:

- Windows: `%APPDATA%\Godot\script_templates\`
- Linux: `$HOME/.config/godot/script_templates/`
- macOS: `$HOME/Library/Application Support/Godot/script_templates/`

If you're getting Godot from somewhere other than the official website, such as Steam, the folder might be in a different location. You can find it using the Godot editor. Go to `Editor > Open Editor Data/Settings Folder` and it will open a folder in your file browser, inside that folder is the `script_templates` folder.

#### Project-defined templates

The default path to search for templates is the `res://script_templates/` directory. The path can be changed by configuring the project setting [Editor > Script > Templates Search Path](../godot_csharp_editor.md), both via code and the editor.

If no `script_templates` directory is found within a project, it is simply ignored.

#### Template organization and naming

Both editor and project defined templates are organized in the following way:

where:

- `template_path` is one of the 2 locations discussed in the previous two sections.
- `node_type` is the node it will apply to (for example, [Node](../godot_csharp_core.md), or [CharacterBody3D](../godot_csharp_nodes_3d.md)), This is **case-sensitive**. If a script isn't in the proper `node_type` folder, it won't be detected.
- `file` is the custom name you can chose for the template (for example, `platformer_movement` or `smooth_camera`).
- `extension` indicates which language the template will apply to (it should be `gd` for GDScript or `cs` for C#).

For example:

- `script_templates/Node/smooth_camera.gd`
- `script_templates/CharacterBody3D/platformer_movement.gd`

### Default behavior and overriding it

By default:

- the template's name is the same as the file name (minus the extension, prettyfied)
- the description is empty
- the space indent is set to 4
- the template will not be set as the default for the given node

It is possible to customize this behavior by adding meta headers at the start of your file, like this:

```csharp
// meta-name: Platformer movement
// meta-description: Predefined movement for classical platformers
// meta-default: true
// meta-space-indent: 4
```

In this case, the name will be set to "Platformer movement", with the given custom description, and it will be set as the default template for the node in which directory it has been saved.

This is an example of utilizing custom templates at editor and project level:

> **Note:** The script templates have the same extension as the regular script files. This may lead to an issue of a script parser treating those templates as actual scripts within a project. To avoid this, make sure to ignore the directory containing them by creating an empty `.gdignore` file. The directory won't be visible throughout the project's filesystem anymore, yet the templates can be modified by an external text editor anytime.

> **Tip:** By default, every C# file inside the project directory is included in the compilation. Script templates must be manually excluded from the C# project to avoid build errors. See [Exclude files from the build](https://learn.microsoft.com/en-us/visualstudio/msbuild/how-to-exclude-files-from-the-build) in the Microsoft documentation.

It is possible to create editor-level templates that have the same level as a project-specific templates, and also that have the same name as a built-in one, all will be shown on the new script dialog.

### Default template

To override the default template, create a custom template at editor or project level inside a `Node` directory (or a more specific type, if only a subtype wants to be overridden) and start the file with the `meta-default: true` header.

Only one template can be set as default at the same time for the same node type.

The `Default` templates for basic Nodes, for both GDScript and C#, are shown here so you can use these as the base for creating other templates:

```csharp
// meta-description: Base template for Node with default Godot cycle methods

using _BINDINGS_NAMESPACE_;
using System;

public partial class _CLASS_ : _BASE_
{
    // Called when the node enters the scene tree for the first time.
    public override void _Ready()
    {
    }

    // Called every frame. 'delta' is the elapsed time since the previous frame.
    public override void _Process(double delta)
    {
    }
}
```

The Godot editor provides a set of useful built-in node-specific templates, such as `basic_movement` for both [CharacterBody2D](../godot_csharp_nodes_2d.md) and [CharacterBody3D](../godot_csharp_nodes_3d.md) and `plugin` for [EditorPlugin](../godot_csharp_editor.md).

### List of template placeholders

The following describes the complete list of built-in template placeholders which are currently implemented.

#### Base placeholders

| Placeholder          | Description                                                                                                                                                                                                                                                                               |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| _BINDINGS_NAMESPACE_ | The name of the Godot namespace (used in C# only).                                                                                                                                                                                                                                        |
| _CLASS_              | The name of the new class.                                                                                                                                                                                                                                                                |
| _CLASS_SNAKE_CASE_   | The name of the new class as snake_case (used in GDScript only).                                                                                                                                                                                                                          |
| _BASE_               | The base type a new script inherits from.                                                                                                                                                                                                                                                 |
| _TS_                 | Indentation placeholder. The exact type and number of whitespace characters used for indentation is determined by the text_editor/indent/type and text_editor/indent/size settings in the EditorSettings respectively. Can be overridden by the meta-space-indent header on the template. |

#### Type placeholders

There used to be, in Godot 3.x, placeholders for GDScript type hints that would get replaced whenever a template was used to create a new script, such as: `%INT_TYPE%`, `%STRING_TYPE%`, `%FLOAT_TYPE%` or `%VOID_RETURN%`.

The placeholders no longer work for Godot 4.x, but if the setting `text_editor/completion/add_type_hints` from [EditorSettings](../godot_csharp_filesystem.md) is disabled, type hints for parameters and return types will be automatically removed for a few base types:

- `int`
- `String`
- `Array[String]`
- `float`
- `void`
- `:=` will be transformed into `=`

---

## Cross-language scripting

Godot allows you to mix and match scripting languages to suit your needs. This means a single project can define nodes in both C# and GDScript. This page will go through the possible interactions between two nodes written in different languages.

The following two scripts will be used as references throughout this page.

```csharp
using Godot;

public partial class MyCSharpNode : Node
{
    public string MyProperty { get; set; } = "my c# value";

    [Signal] public delegate void MySignalEventHandler();
    [Signal] public delegate void MySignalWithParamsEventHandler(string msg, int n);

    public void PrintNodeName(Node node)
    {
        GD.Print(node.Name);
    }

    public void PrintArray(string[] arr)
    {
        foreach (string element in arr)
        {
            GD.Print(element);
        }
    }

    public void PrintNTimes(string msg, int n)
    {
        for (int i = 0; i < n; ++i)
        {
            GD.Print(msg);
        }
    }

    public void MySignalHandler()
    {
        GD.Print("The signal handler was called!");
    }

    public void MySignalWithParamsHandler(string msg, int n)
    {

// ...
```

### Instantiating nodes

If you're not using nodes from the scene tree, you'll probably want to instantiate nodes directly from the code.

#### Instantiating C# nodes from GDScript

Using C# from GDScript doesn't need much work. Once loaded (see Classes as resources), the script can be instantiated with [new()](../godot_csharp_misc.md).

> **Warning:** When creating `.cs` scripts, you should always keep in mind that the class Godot will use is the one named like the `.cs` file itself. If that class does not exist in the file, you'll see the following error: `Invalid call. Nonexistent function `new` in base`. For example, MyCoolNode.cs should contain a class named MyCoolNode. The C# class needs to derive a Godot class, for example `GodotObject`. Otherwise, the same error will occur. You also need to check your `.cs` file is referenced in the project's `.csproj` file. Otherwise, the same error will occur.

#### Instantiating GDScript nodes from C#

From the C# side, everything work the same way. Once loaded, the GDScript can be instantiated with [GDScript.New()](../godot_csharp_resources.md).

```csharp
var myGDScript = GD.Load<GDScript>("res://path/to/my_gd_script.gd");
var myGDScriptNode = (GodotObject)myGDScript.New(); // This is a GodotObject.
```

Here we are using an [Object](../godot_csharp_core.md), but you can use type conversion like explained in Type conversion and casting.

### Accessing fields

#### Accessing C# fields from GDScript

Accessing C# fields from GDScript is straightforward, you shouldn't have anything to worry about.

#### Accessing GDScript fields from C#

As C# is statically typed, accessing GDScript from C# is a bit more convoluted. You will have to use [GodotObject.Get()](../godot_csharp_misc.md) and [GodotObject.Set()](../godot_csharp_misc.md). The first argument is the name of the field you want to access.

```csharp
// Output: "my gdscript value".
GD.Print(myGDScriptNode.Get("my_property"));
myGDScriptNode.Set("my_property", "MY GDSCRIPT VALUE");
// Output: "MY GDSCRIPT VALUE".
GD.Print(myGDScriptNode.Get("my_property"));
```

Keep in mind that when setting a field value you should only use types the GDScript side knows about. Essentially, you want to work with built-in types as described in Built-in types or classes extending [Object](../godot_csharp_core.md).

### Calling methods

#### Calling C# methods from GDScript

Again, calling C# methods from GDScript should be straightforward. The marshalling process will do its best to cast the arguments to match function signatures. If that's impossible, you'll see the following error: `Invalid call. Nonexistent function `FunctionName``.

#### Calling GDScript methods from C#

To call GDScript methods from C# you'll need to use [GodotObject.Call()](../godot_csharp_misc.md). The first argument is the name of the method you want to call. The following arguments will be passed to said method.

```csharp
// Output: "MyCSharpNode" (or name of node where this code is placed).
myGDScriptNode.Call("print_node_name", this);
// This line will fail silently and won't error out.
// myGDScriptNode.Call("print_node_name");

// Outputs "Hello there!" twice, once per line.
myGDScriptNode.Call("print_n_times", "Hello there!", 2);

string[] arr = ["a", "b", "c"];
// Output: "a", "b", "c" (one per line).
myGDScriptNode.Call("print_array", arr);
// Output: "1", "2", "3"  (one per line).
myGDScriptNode.Call("print_array", new int[] { 1, 2, 3 });
// Note how the type of each array entry does not matter
// as long as it can be handled by the marshaller.
```

### Connecting to signals

#### Connecting to C# signals from GDScript

Connecting to a C# signal from GDScript is the same as connecting to a signal defined in GDScript:

#### Connecting to GDScript signals from C#

Connecting to a GDScript signal from C# only works with the `Connect` method because no C# static types exist for signals defined by GDScript:

```csharp
myGDScriptNode.Connect("my_signal", Callable.From(MySignalHandler));

myGDScriptNode.Connect("my_signal_with_params", Callable.From<string, int>(MySignalWithParamsHandler));
```

### Inheritance

A GDScript file may not inherit from a C# script. Likewise, a C# script may not inherit from a GDScript file. Due to how complex this would be to implement, this limitation is unlikely to be lifted in the future. See [this GitHub issue](https://github.com/godotengine/godot/issues/38352) for more information.

---

## Custom performance monitors

### Introduction

As explained in the Debugger panel documentation, Godot features a **Debugger > Monitors** bottom panel that allows tracking various values with graphs showing their evolution over time. The data for those graphs is sourced from the engine's [Performance](../godot_csharp_core.md) singleton.

Godot lets you declare custom values to be displayed in the Monitors tab. Example use cases for custom performance monitors include:

- Displaying performance metrics that are specific to your project. For instance, in a voxel game, you could create a performance monitor to track the number of chunks that are loaded every second.
- Displaying in-game metrics that are not strictly related to performance, but are still useful to graph for debugging purposes. For instance, you could track the number of enemies present in the game to make sure your spawning mechanic works as intended.

### Creating a custom performance monitor

In this example, we'll create a custom performance monitor to track how many enemies are present in the currently running project.

The main scene features a [Timer](../godot_csharp_misc.md) node with the following script attached:

The second parameter of [Performance.add_custom_monitor](../godot_csharp_core.md) is a [Callable](../godot_csharp_misc.md).

`enemy.tscn` is a scene with a Node2D root node and Timer child node. The Node2D has the following script attached:

In this example, since we spawn 20 enemies per second, and each enemy despawns 2.5 seconds after they spawn, we expect the number of enemies present in the scene to stabilize to 50. We can make sure about this by looking at the graph.

To visualize the graph created from this custom performance monitor, run the project, switch to the editor while the project is running and open **Debugger > Monitors** at the bottom of the editor window. Scroll down to the newly available **Game** section and check **Enemies**. You should see a graph appearing as follows:

> **Note:** The performance monitor handling code doesn't have to live in the same script as the nodes themselves. You may choose to move the performance monitor registration and getter function to an autoload instead.

### Querying a performance monitor in a project

If you wish to display the value of the performance monitor in the running project's window (rather than the editor), use `Performance.get_custom_monitor("category/name")` to fetch the value of the custom monitor. You can display the value using a [Label](../godot_csharp_ui_controls.md), [RichTextLabel](../godot_csharp_ui_controls.md), [Custom drawing in 2D](tutorials_2d.md), [3D text](tutorials_3d.md), etc.

This method can be used in exported projects as well (debug and release mode), which allows you to create visualizations outside the editor.

---

## Debugger panel

Many of Godot's debugging tools, including the debugger, can be found in the debugger panel at the bottom of the screen. Click on **Debugger** to open it.

The debugger panel is split into several tabs, each focusing on a specific task.

### Stack Trace

The Stack Trace tab opens automatically when the GDScript compiler reaches a breakpoint in your code.

It gives you a [stack trace](https://en.wikipedia.org/wiki/Stack_trace), information about the state of the object, and buttons to control the program's execution. When the debugger breaks on a breakpoint, a green triangle arrow is visible in the script editor's gutter. This arrow indicates the line of code the debugger broke on.

> **Tip:** You can create a breakpoint by clicking the gutter in the left of the script editor (on the left of the line numbers). When hovering this gutter, you will see a transparent red dot appearing, which turns into an opaque red dot after the breakpoint is placed by clicking. Click the red dot again to remove the breakpoint. Breakpoints created this way persist across editor restarts, even if the script wasn't saved when exiting the editor. You can also use the `breakpoint` keyword in GDScript to create a breakpoint that is stored in the script itself. Unlike breakpoints created by clicking in the gutter, this keyword-based breakpoint is persistent across different machines when using version control.

You can use the buttons in the top-right corner to:

- Skip all breakpoints. That way, you can save breakpoints for future debugging sessions.
- Copy the current error message.
- **Step Into** the code. This button takes you to the next line of code, and if it's a function, it steps line-by-line through the function.
- **Step Over** the code. This button goes to the next line of code, but it doesn't step line-by-line through functions.
- **Break**. This button pauses the game's execution.
- **Continue**. This button resumes the game after a breakpoint or pause.

> **Note:** Using the debugger and breakpoints on [tool scripts](tutorials_plugins.md) is not currently supported. Breakpoints placed in the script editor or using the `breakpoint` keyword are ignored. You can use print statements to display the contents of variables instead.

### Errors

This is where error and warning messages are printed while running the game.

You can disable specific warnings in **Project Settings > Debug > GDScript**.

### Evaluator

This tab contains an expression evaluator, also known as a REPL. This is a more powerful complement to the Stack Variables tree available in the Stack Trace tab.

When the project is interrupted in the debugger (due to a breakpoint or script error), you can enter an expression in the text field at the top. If the project is running, the expression field won't be editable, so you will need to set a breakpoint first. Expressions can be persisted across runs by unchecking **Clear on Run**, although they will be lost when the editor quits.

Expressions are evaluated using Godot's expression language, which allows you to perform arithmetic and call some functions within the expression. Expressions can refer to member variables, or local variables within the same scope as the line the breakpoint is on. You can also enter constant values, which makes it usable as a built-in calculator.

Consider the following script:

If the debugger breaks on the **first** line containing `breakpoint`, the following expressions return non-null values:

- **Constant expression:** `2 * PI + 5`
- **Member variable:** `counter`, `counter ** 2`, `sqrt(counter)`
- **Local variable or function parameter:** `delta`, `text`, `text.to_upper()`

If the debugger breaks on the **second** line containing `breakpoint`, the following expressions return non-null values:

- **Constant expression:** `2 * PI + 5`
- **Member variable:** `counter`, `counter ** 2`, `sqrt(counter)`
- **Local variable or function parameter:** `delta`, `other_text`, `other_text.to_upper()`

### Profiler

The profiler is used to see what code is running while your project is in use, and how that effects performance.

> **See also:** A detailed explanation of how to use the profiler can be found in the dedicated The Profiler page.

### Visual Profiler

The Visual Profiler can be used to monitor what is taking the most time when rendering a frame on the CPU and GPU respectively. This allows tracking sources of potential CPU and GPU bottlenecks caused by rendering.

> **Warning:** The Visual Profiler only measures CPU time taken for rendering tasks, such as performing draw calls. The Visual Profiler does **not** include CPU time taken for other tasks such as scripting and physics. Use the standard Profiler tab to track non-rendering-related CPU tasks.

To use the visual profiler, run the project, switch to the **Visual Profiler** tab within the Debugger bottom panel, then click **Start**:

> **Tip:** You can also check **Autostart**, which will make the visual profiler automatically start when the project is run the next time. Note that the **Autostart** checkbox's state is not preserved across editor sessions.

You will see categories and results appearing as the profiler is running. Graph lines also appear, with the left side being a CPU framegraph and the right side being a GPU framegraph.

Click **Stop** to finish profiling, which will keep the results visible but frozen in place. Results remain visible after stopping the running project, but not after exiting the editor.

Click on result categories on the left to highlight them in the CPU and GPU graphs on the right. You can also click on the graph to move the cursor to a specific frame number and highlight the selected data type in the result categories on the left.

You can switch the result display between a time value (in milliseconds per frame) or a percentage of the target frametime (which is currently hardcoded to 16.67 milliseconds, or 60 FPS).

If framerate spikes occur during profiling, this can cause the graph to be poorly scaled. Disable **Fit to Frame** so that the graph will zoom onto the 60 FPS+ portion.

> **Note:** Remember that Visual Profiler results can vary **heavily** based on viewport resolution, which is determined by the window size if using the `disabled` or `canvas_items` [stretch modes](tutorials_rendering.md). When comparing results across different runs, make sure to use the same viewport size for all runs.

Visual Profiler is supported when using any rendering method (Forward+, Mobile or Compatibility), but the reported categories will vary depending on the current rendering method as well as the enabled graphics features. For example, when using Forward+, a simple 2D scene with shadow-casting lights will result in the following categories appearing:

To give another example with Forward+, a 3D scene with shadow-casting lights and various effects enabled will result in the following categories enabled:

Notice how in the 3D example, several of the categories have **(Parallel)** appended to their name. This hints that multiple tasks are being performed in parallel on the GPU. This generally means that disabling only one of the features involved won't improve performance as much as anticipated, as the other task still needs to be performed sequentially.

> **Note:** The Visual Profiler is not supported when using the Compatibility renderer on macOS, due to platform limitations.

### Network Profiler

The Network Profiler contains a list of all the nodes that communicate over the multiplayer API and, for each one, some counters on the amount of incoming and outgoing network interactions. It also features a bandwidth meter that displays the total bandwidth usage at any given moment.

> **Note:** The bandwidth meter does **not** take the [High-level multiplayer](tutorials_networking.md) API's own compression system into account. This means that changing the compression algorithm used will not change the metrics reported by the bandwidth meter.

### Monitors

The monitors are graphs of several aspects of the game while it's running such as FPS, memory usage, how many nodes are in a scene and more. All monitors keep track of stats automatically, so even if one monitor isn't open while the game is running, you can open it later and see how the values changed.

> **See also:** In addition to the default performance monitors, you can also create custom performance monitors to track arbitrary values in your project.

### Video RAM

The **Video RAM** tab shows the video RAM usage of the game while it is running. It provides a list of every resource using video RAM by resource path, the type of resource it is, what format it is in, and how much Video RAM that resource is using. There is also a total video RAM usage number at the top right of the panel.

### Misc

The **Misc** tab contains tools to identify the control nodes you are clicking at runtime:

- **Clicked Control** tells you where the clicked node is in the scene tree.
- **Clicked Control Type** tells you the type of the node you clicked is.

---
