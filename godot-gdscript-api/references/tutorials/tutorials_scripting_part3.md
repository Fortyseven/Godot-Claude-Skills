# Godot 4 GDScript Tutorials — Scripting (Part 3)

> 10 tutorials. GDScript-specific code examples.

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

### How to fix violations

To fix a violation of this rule, change the type to remove the generic type parameters or remove the `[GlobalClass]` attribute.

### When to suppress warnings

Do not suppress a warning from this rule. Adding the `[GlobalClass]` to a generic type is an easy mistake to make and this warning helps users realize that it may result in unexpected errors.

---

## Change scenes manually

Sometimes it helps to have more control over how you swap scenes around. A [Viewport](../godot_gdscript_rendering.md)'s child nodes will render to the image it generates. This holds true even for nodes outside of the "current" scene. Autoloads fall into this category, and also scenes which you instantiate and add to the tree at runtime:

```gdscript
var simultaneous_scene = preload("res://levels/level2.tscn").instantiate()

func _add_a_scene_manually():
    # This is like autoloading the scene, only
    # it happens after already loading the main scene.
    get_tree().root.add_child(simultaneous_scene)
```

To complete the cycle and swap out the new scene with the old one, you have a choice to make. Many strategies exist for removing a scene from view of the [Viewport](../godot_gdscript_rendering.md). The tradeoffs involve balancing operation speed and memory consumption, as well as balancing data access and integrity.

1. **Delete the existing scene.** [SceneTree.change_scene_to_file()](../godot_gdscript_core.md) and [SceneTree.change_scene_to_packed()](../godot_gdscript_core.md) will delete the current scene immediately. You can also delete the main scene. Assuming the root node's name is "Main", you could do `get_node("/root/Main").free()` to delete the whole scene.

- Unloads memory.

- Pro: RAM is no longer dragging the dead weight.
- Con: Returning to that scene is now more expensive since it must be loaded back into memory again (takes time AND memory). Not a problem if returning soon is unnecessary.
- Con: No longer have access to that scene's data. Not a problem if using that data soon is unnecessary.
- Note: It can be useful to preserve the data in a soon-to-be-deleted scene by re-attaching one or more of its nodes to a different scene, or even directly to the [SceneTree](../godot_gdscript_core.md).
- Processing stops.

- Pro: No nodes means no processing, physics processing, or input handling. The CPU is available to work on the new scene's contents.
- Con: Those nodes' processing and input handling no longer operate. Not a problem if using the updated data is unnecessary.

2. **Hide the existing scene.** By changing the visibility or collision detection of the nodes, you can hide the entire node sub-tree from the player's perspective. Use [CanvasItem.hide()](../godot_gdscript_nodes_2d.md) to hide a scene and [CanvasItem.show()](../godot_gdscript_nodes_2d.md) to show it again.

- Memory still exists.

- Pro: You can still access the data if needed.
- Pro: There's no need to move any more nodes around to save data.
- Con: More data is being kept in memory, which will be become a problem on memory-sensitive platforms like web or mobile.
- Processing continues.

- Pro: Data continues to receive processing updates, so the scene will keep any data within it that relies on delta time or frame data updated.
- Pro: Nodes are still members of groups (since groups belong to the [SceneTree](../godot_gdscript_core.md)).
- Con: The CPU's attention is now divided between both scenes. Too much load could result in low frame rates. You should be sure to test performance as you go to ensure the target platform can support the load from this approach.

3. **Remove the existing scene from the tree.** Assign a variable to the existing scene's root node. Then use [Node.remove_child(Node)](../godot_gdscript_misc.md) to detach the entire scene from the tree. To attach it later, use [Node.add_child(Node)](../godot_gdscript_misc.md).

- Memory still exists (similar pros/cons as hiding it from view).
- Processing stops (similar pros/cons as deleting it completely).
- Pro: This variation of "hiding" it is much easier to show/hide. Rather than potentially keeping track of multiple changes to the scene, you only need to call the add/remove_child methods. This is similar to disabling game objects in other engines.
- Con: Unlike with hiding it from view only, the data contained within the scene will become stale if it relies on delta time, input, groups, or other data that is derived from [SceneTree](../godot_gdscript_core.md) access.

There are also cases where you may wish to have many scenes present at the same time, such as adding your own singleton at runtime, or preserving a scene's data between scene changes (adding the scene to the root node).

```gdscript
get_tree().root.add_child(scene)
```

Another case may be displaying multiple scenes at the same time using [SubViewportContainers](../godot_gdscript_ui_controls.md). This is optimal for rendering different content in different parts of the screen (e.g. minimaps, split-screen multiplayer).

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

To learn more about `Callable`, check out the class reference here: [Callable](../godot_gdscript_misc.md).

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

```gdscript
extends Node

func _on_Sprite2D_position_changed(node, new_pos):
    print("The position of " + node.get_class() + " is now " + str(new_pos))
```

Every second, we output our position to the console.

### Next steps

We hope the above example showed you the basics. You can build upon this example to create full-fledged scripts to control nodes in Godot using C++!

Instead of basing your project off the above example setup, we recommend to restart now by cloning the [godot-cpp template](https://github.com/godotengine/godot-cpp-template), and base your project off of that. It has better coverage of features, such as a GitHub build action and additional useful `SConstruct` boilerplate.

---
