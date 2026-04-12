# Godot 4 C# Tutorials — Editor (Part 1)

> 4 tutorials. C#-specific code examples.

## Command line tutorial

Some developers like using the command line extensively. Godot is designed to be friendly to them, so here are the steps for working entirely from the command line. Given the engine relies on almost no external libraries, initialization times are pretty fast, making it suitable for this workflow.

> **Note:** On Windows and Linux, you can run a Godot binary in a terminal by specifying its relative or absolute path. On macOS, the process is different due to Godot being contained within a `.app` bundle (which is a _folder_, not a file). To run a Godot binary from a terminal on macOS, you have to `cd` to the folder where the Godot application bundle is located, then run `Godot.app/Contents/MacOS/Godot` followed by any command line arguments. If you've renamed the application bundle from `Godot` to another name, make sure to edit this command line accordingly.

### Command line reference

**Legend**

- Available in editor builds, debug export templates and release export templates.
- Available in editor builds and debug export templates only.
- Only available in editor builds, and export templates compiled with `disable_path_overrides=false`.
- Only available in editor builds.

Note that unknown command line arguments have no effect whatsoever. The engine will **not** warn you when using a command line argument that doesn't exist with a given build type.

**General options**

| Command | Description |
| -h, --help | Display the list of command line options. |
| --version | Display the version string. |
| -v, --verbose | Use verbose stdout mode. |
| -q, --quiet | Quiet mode, silences stdout messages. Errors are still displayed. |
| --no-header | Do not print engine version and rendering method header on startup. |

**Run options**

| Command | Description |
| --, ++ | Separator for user-provided arguments. Following arguments are not used by the engine, but can be read from OS.get_cmdline_user_args(). |
| -e, --editor | Start the editor instead of running the scene. |
| -p, --project-manager | Start the Project Manager, even if a project is auto-detected. |
| --recovery-mode | "Start the editor in recovery mode, which disables features that can typically cause startup crashes, such as tool scripts, editor plugins, GDExtension addons, and others. |
| --debug-server <uri> | Start the editor debug server (<protocol>://<host/IP>[:<port>], e.g. tcp://127.0.0.1:6007) |
| --dap-port <port> | Use the specified port for the GDScript Debug Adapter Protocol. Recommended port range [1024, 49151]. |
| --lsp-port <port> | Use the specified port for the GDScript Language Server Protocol. Recommended port range [1024, 49151]. |
| --quit | Quit after the first iteration. |
| --quit-after | Quit after the given number of iterations. Set to 0 to disable. |
| -l, --language <locale> | Use a specific locale. <locale> follows the format language_Script_COUNTRY_VARIANT where language is a 2 or 3-letter language code in lowercase and the rest is optional. See Locale codes for more details. |
| --path <directory> | Path to a project (<directory> must contain a "project.godot" file). |
| --scene <path> | Path or UID of a scene in the project that should be started. |
| --main-pack <file> | Path to a pack (.pck) file to load. |
| --render-thread <mode> | Render thread mode ("unsafe", "safe", "separate"). See Thread Model for more details. |
| --remote-fs <address> | Remote filesystem (<host/IP>[:<port>] address). |
| --remote-fs-password <password> | Password for remote filesystem. |
| --audio-driver <driver> | Audio driver. Use --help first to display the list of available drivers. |
| --display-driver <driver> | Display driver (and rendering driver). Use --help first to display the list of available drivers. |
| --audio-output-latency <ms> | Override audio output latency in milliseconds (default is 15 ms). Lower values make sound playback more reactive but increase CPU usage, and may result in audio cracking if the CPU can't keep up. |
| --rendering-method <renderer> | Renderer name. Requires driver support. |
| --rendering-driver <driver> | Rendering driver (depends on display driver). Use --help first to display the list of available drivers. |
| --gpu-index <device_index> | Use a specific GPU (run with --verbose to get available device list). |
| --text-driver <driver> | Text driver (Fonts, BiDi, shaping). |
| --tablet-driver <driver> | Pen tablet input driver. |
| --headless | Enable headless mode (--display-driver headless --audio-driver Dummy). Useful for servers and with --script. |
| --log-file | Write output/error log to the specified path instead of the default location defined by the project. <file> path should be absolute or relative to the project directory. |
| --write-movie <file> | Run the engine in a way that a movie is written (usually with .avi or .png extension). --fixed-fps is forced when enabled, but can be used to change movie FPS. --disable-vsync can speed up movie writing but makes interaction more difficult. --quit-after can be used to specify the number of frames to write. |

**Display options**

| Command | Description |
| -f, --fullscreen | Request fullscreen mode. |
| -m, --maximized | Request a maximized window. |
| -w, --windowed | Request windowed mode. |
| -t, --always-on-top | Request an always-on-top window. |
| --resolution <W>x<H> | Request window resolution. |
| --position <X>,<Y> | Request window position. |
| --screen <N> | Request window screen. |
| --single-window | Use a single window (no separate subwindows). |
| --xr-mode <mode> | Select XR mode ("default", "off", "on"). |
| --wid <window_id> | Request parented to window. |
| --accessibility <mode> | Select accessibility mode ['auto" (when screen reader is running, default), "always", "disabled']. |

**Debug options**

| Command | Description |
| -d, --debug | Debug (local stdout debugger). |
| -b, --breakpoints | Breakpoint list as source::line comma-separated pairs, no spaces (use %20 instead). |
| --ignore-error-breaks | If debugger is connected, prevents sending error breakpoints. |
| --profiling | Enable profiling in the script debugger. |
| --gpu-profile | Show a GPU profile of the tasks that took the most time during frame rendering. |
| --gpu-validation | Enable graphics API validation layers for debugging. |
| --gpu-abort | Abort on GPU errors (usually validation layer errors), may help see the problem if your system freezes. |
| --generate-spirv-debug-info | Generate SPIR-V debug information. This allows source-level shader debugging with RenderDoc. |
| --extra-gpu-memory-tracking | Enables additional memory tracking (see class reference for RenderingDevice.get_driver_and_device_memory_report() and linked methods). Currently only implemented for Vulkan. Enabling this feature may cause crashes on some systems due to buggy drivers or bugs in the Vulkan Loader. See https://github.com/godotengine/godot/issues/95967 |
| --accurate-breadcrumbs | Force barriers between breadcrumbs. Useful for narrowing down a command causing GPU resets. Currently only implemented for Vulkan. |
| --remote-debug <uri> | Remote debug (<protocol>://<host/IP>[:<port>], e.g. tcp://127.0.0.1:6007). |
| --single-threaded-scene | Scene tree runs in single-threaded mode. Sub-thread groups are disabled and run on the main thread. |
| --debug-collisions | Show collision shapes when running the scene. |
| --debug-paths | Show path lines when running the scene. |
| --debug-navigation | Show navigation polygons when running the scene. |
| --debug-avoidance | Show navigation avoidance debug visuals when running the scene. |
| --debug-stringnames | Print all StringName allocations to stdout when the engine quits. |
| --debug-canvas-item-redraw | Display a rectangle each time a canvas item requests a redraw (useful to troubleshoot low processor mode). |
| --max-fps <fps> | Set a maximum number of frames per second rendered (can be used to limit power usage). A value of 0 results in unlimited framerate. |
| --frame-delay <ms> | Simulate high CPU load (delay each frame by <ms> milliseconds). Do not use as a FPS limiter; use --max-fps instead. |
| --time-scale <scale> | Force time scale (higher values are faster, 1.0 is normal speed). |
| --disable-vsync | Forces disabling of vertical synchronization, even if enabled in the project settings. Does not override driver-level V-Sync enforcement. |
| --disable-render-loop | Disable render loop so rendering only occurs when called explicitly from script. |
| --disable-crash-handler | Disable crash handler when supported by the platform code. |
| --fixed-fps <fps> | Force a fixed number of frames per second. This setting disables real-time synchronization. |
| --delta-smoothing <enable> | Enable or disable frame delta smoothing ("enable", "disable"). |
| --print-fps | Print the frames per second to the stdout. |
| --editor-pseudolocalization | Enable pseudolocalization for the editor and the project manager. |

**Standalone tools**

| Command | Description |
| -s, --script <script> | Run a script. <script> must be a resource path relative to the project (myscript.gd will be interpreted as res://my_script.gd) or an absolute filesystem path (for example, on Windows: C:/tmp/my_script.gd). |
| --main-loop <main_loop_name> | Run a MainLoop specified by its global class name. |
| --check-only | Only parse for errors and quit (use with --script). |
| --import | Starts the editor, waits for any resources to be imported, and then quits. Implies --editor and --quit. |
| --export-release <preset> <path> | Export the project in release mode using the given preset and output path. The preset name should match one defined in "export_presets.cfg". <path> should be absolute or relative to the project directory, and include the filename for the binary (e.g. "builds/game.exe"). The target directory must exist. |
| --export-debug <preset> <path> | Like --export-release, but use debug template. Implies --import. |
| --export-pack <preset> <path> | Like --export-release, but only export the game pack for the given preset. The <path> extension determines whether it will be in PCK or ZIP format. Implies --import. |
| --export-patch <preset> <path> | Export pack with changed files only. See --export-pack description for other considerations. |
| --patches <paths> | List of patches to use with --export-patch. The list is comma-separated. |
| --install-android-build-template | Install the Android build template. Used in conjunction with --export-release or --export-debug. |
| --convert-3to4 [<max_file_kb>] [<max_line_size>] | Convert project from Godot 3.x to Godot 4.x. |
| --validate-conversion-3to4 [<max_file_kb>] [<max_line_size>] | Show what elements will be renamed when converting project from Godot 3.x to Godot 4.x. |
| --doctool [<path>] | Dump the engine API reference to the given <path> in XML format, merging if existing files are found. |
| --no-docbase | Disallow dumping the base types (used with --doctool). |
| --gdextension-docs | Rather than dumping the engine API, generate API reference from all the GDExtensions loaded in the current project (used with --doctool). |
| --gdscript-docs <path> | Rather than dumping the engine API, generate API reference from the inline documentation in the GDScript files found in <path> (used with --doctool). |
| --build-solutions | Build the scripting solutions (e.g. for C# projects). Implies --editor and requires a valid project to edit. |
| --dump-gdextension-interface | Generate GDExtension header file "gdextension_interface.h" in the current folder. This file is the base file required to implement a GDExtension. |
| --dump-gdextension-interface-json | Generate a JSON dump of the GDExtension interface named "gdextension_interface.json" in the current folder. |
| --dump-extension-api | Generate JSON dump of the Godot API for GDExtension bindings named "extension_api.json" in the current folder. |
| --dump-extension-api-with-docs | Generate JSON dump of the Godot API like the previous option, but including documentation. |
| --validate-extension-api <path> | Validate an extension API file dumped (with the option above) from a previous version of the engine to ensure API compatibility. If incompatibilities or errors are detected, the return code will be non-zero. |
| --benchmark | Benchmark the run time and print it to console. |
| --benchmark-file <path> | Benchmark the run time and save it to a given file in JSON format. The path should be absolute. |
| --test [--help] | Run unit tests (requires compiling the engine with tests=yes). Use --test --help for more information. |

### Path

It is recommended to place your Godot editor binary in your `PATH` environment variable, so it can be executed easily from any place by typing `godot`. You can do so on Linux by placing the Godot binary in `/usr/local/bin` and making sure it is called `godot` (case-sensitive).

To achieve this on Windows or macOS easily, you can install Godot using [Scoop](https://scoop.sh) (on Windows) or [Homebrew](https://brew.sh) (on macOS). This will automatically make the copy of Godot installed available in the `PATH`:

### Setting the project path

Depending on where your Godot binary is located and what your current working directory is, you may need to set the path to your project for any of the following commands to work correctly.

When running the editor, this can be done by giving the path to the `project.godot` file of your project as either the first argument, like this:

```shell
godot path_to_your_project/project.godot [other] [commands] [and] [args]
```

For all commands, this can be done by using the `--path` argument:

```shell
godot --path path_to_your_project [other] [commands] [and] [args]
```

For example, the full command for exporting your game (as explained below) might look like this:

```shell
godot --headless --path path_to_your_project --export-release my_export_preset_name game.exe
```

When starting from a subdirectory of your project, use the `--upwards` argument for Godot to automatically find the `project.godot` file by recursively searching the parent directories.

For example, running a scene (as explained below) nested in a subdirectory might look like this when your working directory is in the same path:

```shell
godot --upwards nested_scene.tscn
```

### Creating a project

Creating a project from the command line can be done by navigating the shell to the desired place and making a `project.godot` file.

```shell
mkdir newgame
cd newgame
touch project.godot
```

The project can now be opened with Godot.

### Running the editor

Running the editor is done by executing Godot with the `-e` flag. This must be done from within the project directory or by setting the project path as explained above, otherwise the command is ignored and the Project Manager appears.

```shell
godot -e
```

When passing in the full path to the `project.godot` file, the `-e` flag may be omitted.

If a scene has been created and saved, it can be edited later by running the same code with that scene as argument.

```shell
godot -e scene.tscn
```

### Erasing a scene

Godot is friends with your filesystem and will not create extra metadata files. Use `rm` to erase a scene file. Make sure nothing references that scene. Otherwise, an error will be thrown upon opening the project.

```shell
rm scene.tscn
```

### Running the game

To run the game, execute Godot within the project directory or with the project path as explained above.

```shell
godot
```

Note that passing in the `project.godot` file will always run the editor instead of running the game.

When a specific scene needs to be tested, pass that scene to the command line.

```shell
godot scene.tscn
```

### Debugging

Catching errors in the command line can be a difficult task because they scroll quickly. For this, a command line debugger is provided by adding `-d`. It works for running either the game or a single scene.

```shell
godot -d
```

```shell
godot -d scene.tscn
```

### Exporting

Exporting the project from the command line is also supported. This is especially useful for continuous integration setups.

> **Note:** Using the `--headless` command line argument is **required** on platforms that do not have GPU access (such as continuous integration). On platforms with GPU access, `--headless` prevents a window from spawning while the project is exporting.

```shell
# `godot` must be a Godot editor binary, not an export template.
# Also, export templates must be installed for the editor
# (or a valid custom export template must be defined in the export preset).
godot --headless --export-release "Linux/X11" /var/builds/project
godot --headless --export-release Android /var/builds/project.apk
```

The preset name must match the name of an export preset defined in the project's `export_presets.cfg` file. If the preset name contains spaces or special characters (such as "Windows Desktop"), it must be surrounded with quotes.

To export a debug version of the game, use the `--export-debug` switch instead of `--export-release`. Their parameters and usage are the same.

To export only a PCK file, use the `--export-pack` option followed by the preset name and output path, with the file extension, instead of `--export-release` or `--export-debug`. The output path extension determines the package's format, either PCK or ZIP.

> **Warning:** When specifying a relative path as the path for `--export-release`, `--export-debug` or `--export-pack`, the path will be relative to the directory containing the `project.godot` file, **not** relative to the current working directory.

### Running a script

It is possible to run a `.gd` script from the command line. This feature is especially useful in large projects, e.g. for batch conversion of assets or custom import/export.

The script must inherit from `SceneTree` or `MainLoop`.

Here is an example `sayhello.gd`, showing how it works:

```python
#!/usr/bin/env -S godot -s
extends SceneTree

func _init():
    print("Hello!")
    quit()
```

And how to run it:

```shell
# Prints "Hello!" to standard output.
godot -s sayhello.gd
```

If no `project.godot` exists at the path, current path is assumed to be the current working directory (unless `--path` is specified).

The script path will be interpreted as a resource path relative to the project, here `res://sayhello.gd`. You can also use an absolute filesystem path instead, which is useful if the script is located outside of the project directory.

The first line of `sayhello.gd` above is commonly referred to as a _shebang_. If the Godot binary is in your `PATH` as `godot`, it allows you to run the script as follows in modern Linux distributions, as well as macOS:

```shell
# Mark script as executable.
chmod +x sayhello.gd
# Prints "Hello!" to standard output.
./sayhello.gd
```

If the above doesn't work in your current version of Linux or macOS, you can always have the shebang run Godot straight from where it is located as follows:

```shell
#!/usr/bin/godot -s
```

---

## Customizing the interface

Godot's interface lives in a single window by default. Since Godot 4.0, you can split several elements to separate windows to better make use of multi-monitor setups.

### Moving and resizing docks

Click and drag on the edge of any dock or panel to resize it horizontally or vertically:

Click the "3 vertical dots" icon at the top of any dock to change its location, or split it to a separate window by choosing **Make Floating** in the submenu that appears:

To move a floating dock back to the editor window, close the dock window using the **×** button in the top-right corner of the window (or in the top-left corner on macOS). Alternatively, you can press Alt + F4 while the split window is focused.

### Splitting the script or shader editor to its own window

> **Note:** This feature is only available on platforms that support spawning multiple windows: Windows, macOS and Linux. This feature is also not available if **Single Window Mode** is enabled in the Editor Settings.

Since Godot 4.1, you can split the script or shader editor to its own window.

To split the script editor to its own window, click the corresponding button in the top-right corner of the script editor:

To split the shader editor to its own window, click the corresponding button in the top-right corner of the script editor:

To go back to the previous state (with the script/shader editor embedded in the editor window), close the split window using the **×** button in the top-right corner of the window (or in the top-left corner on macOS). Alternatively, you can press Alt + F4 while the split window is focused.

### Customizing editor layouts

You may want to save and load a dock configuration depending on the kind of task you're working on. For instance, when working on animating a character, it may be more convenient to have docks laid out in a different fashion compared to when you're designing a level.

For this purpose, Godot provides a way to save and restore editor layouts. Before saving a layout, make changes to the docks you'd like to save. The following changes are persisted to the saved layout:

- Moving a dock.
- Resizing a dock.
- Making a dock floating.
- Changing a floating dock's position or size.
- FileSystem dock properties: split mode, display mode, sorting order, file list display mode, selected paths and unfolded paths.

> **Note:** Splitting the script or shader editor to its own window is _not_ persisted as part of a layout.

After making changes, open the **Editor** menu at the top of the editor then choose **Editor Layouts > Save**. Enter a name for the layout, then click **Save**. If you've already saved an editor layout, you can choose to override an existing layout using the list.

After making changes, open the **Editor** menu at the top of the editor then choose **Editor Layouts**. In the dropdown list, you will see a list of saved editor layouts, plus **Default** which is a hardcoded editor layout that can't be removed. The default layout matches a fresh Godot installation with no changes made to the docks' positions and sizes, and no floating docks.

You can remove a layout using the **Delete** option in the **Editor Layouts** dropdown.

> **Tip:** If you name the saved layout `Default` (case-sensitive), the default editor layout will be overwritten. Note that the `Default` does not appear in the list of layouts to overwrite until you overwrite it once, but you can still write its name manually. You can go back to the standard default layout by removing the `Default` layout after overriding it. (This option does not appear if you haven't overridden the default layout yet.)

Editor layouts are saved to a file named `editor_layouts.cfg` in the configuration path of the [Editor data paths](tutorials_io.md).

### Customizing editor settings

In the **Editor** menu at the top of the editor, you can find an **Editor Settings** option. This opens a window similar to the Project Settings, but with settings used by the editor. These settings are shared across all projects and are not saved in the project files.

Some commonly changed settings are:

- **Interface > Editor > Editor Language:** Controls the language the editor displays in. To make English tutorials easier to follow, you may want to change this to English so that menu names are identical to names referred to by tutorials. The language can also be changed in the top-right corner of the project manager.
- **Interface > Editor > Display Scale:** Controls how large UI elements display on screen. The default **Auto** setting finds a suitable value based on your display's DPI and resolution. Due to engine limitations, it only takes the display-provided scaling factor on macOS, not on Windows or Linux.
- **Interface > Editor > Single Window Mode:** If enabled, this forces the editor to use a single window. This disables certain features such as splitting the script/shaders editor to their own window. Single-window mode can be more stable, especially on Linux when using Wayland.
- **Interface > Theme > Preset:** The editor theme preset to use. The **Light** theme preset may be easier to read if you're outdoors or in a room with sunlight. The **Black (OLED)** preset can reduce power consumption on OLED displays, which are increasingly common in laptops and phones/tablets.
- **FileSystem > Directories > Autoscan Project Path:** This can be set to a folder path that will be automatically scanned for projects in the project manager every time it starts.
- **FileSystem > Directories > Default Project Path:** Controls the default location where new projects are created in the project manager.
- **Editors > 3D > Emulate Numpad:** This allows using the top row 0-9 keys in the 3D editor as their equivalent numpad keys. It's recommended to enable this option if you don't have a number pad on your keyboard.
- **Editors > 3D > Emulate 3 Button Mouse:** This allows using the pan, zoom and orbit modifiers in the 3D editor even when not holding down any mouse button. It's recommended to enable this option if you're using a trackpad.

See the [EditorSettings](../godot_csharp_filesystem.md) class reference for a complete description of most editor settings. You can also hover an editor setting's name with the mouse in the Editor Settings to show its description.

---

## Default editor shortcuts

> **Work in progress:** The content of this page was not yet updated for Godot `4.6` and may be **outdated**. If you know how to improve this page or you can confirm that it's up to date, feel free to [open a pull request](https://github.com/godotengine/godot-docs).

Many Godot editor functions can be executed with keyboard shortcuts. This page lists functions which have associated shortcuts by default, but many others are available for customization in editor settings as well. To change keys associated with these and other actions navigate to **Editor > Editor Settings > Shortcuts**.

While some actions are universal, a lot of shortcuts are specific to individual tools. For this reason it is possible for some key combinations to be assigned to more than one function. The correct action will be performed depending on the context.

> **Note:** While Windows and Linux builds of the editor share most of the default settings, some shortcuts may differ for macOS version. This is done for better integration of the editor into macOS ecosystem. Users fluent with standard shortcuts on that OS should find Godot Editor's default key mapping intuitive.

### General editor actions

| Action name           | Windows, Linux         | macOS                 | Editor setting               |
| --------------------- | ---------------------- | --------------------- | ---------------------------- |
| Open 2D Workspace     | Ctrl + F1              | Cmd + Ctrl + 1        | editor/editor_2d             |
| Open 3D Workspace     | Ctrl + F2              | Cmd + Ctrl + 2        | editor/editor_3d             |
| Open Script Editor    | Ctrl + F3              | Cmd + Ctrl + 3        | editor/editor_script         |
| Search Help           | F1                     | Opt + Space           | editor/editor_help           |
| Distraction Free Mode | Ctrl + Shift + F11     | Cmd + Shift + D       | editor/distraction_free_mode |
| Next Scene Tab        | Ctrl + Tab             | Ctrl + Tab            | editor/next_tab              |
| Previous Scene Tab    | Ctrl + Shift + Tab     | Ctrl + Shift + Tab    | editor/prev_tab              |
| Filter Files          | Ctrl + Alt + P         | Opt + Cmd + P         | editor/filter_files          |
| Open Scene            | Ctrl + O               | Cmd + O               | editor/open_scene            |
| Close Scene           | Ctrl + Shift + W       | Cmd + W               | editor/close_scene           |
| Reopen Closed Scene   | Ctrl + Shift + T       | Cmd + Shift + T       | editor/reopen_closed_scene   |
| Save Scene            | Ctrl + S               | Cmd + S               | editor/save_scene            |
| Save Scene As         | Ctrl + Shift + S       | Cmd + Shift + S       | editor/save_scene_as         |
| Save All Scenes       | Ctrl + Shift + Alt + S | Cmd + Shift + Opt + S | editor/save_all_scenes       |
| Quick Open            | Shift + Alt + O        | Cmd + Ctrl + O        | editor/quick_open            |
| Quick Open Scene      | Ctrl + Shift + O       | Cmd + Shift + O       | editor/quick_open_scene      |
| Quick Open Script     | Ctrl + Alt + O         | Opt + Cmd + O         | editor/quick_open_script     |
| Undo                  | Ctrl + Z               | Cmd + Z               | editor/undo                  |
| Redo                  | Ctrl + Shift + Z       | Cmd + Shift + Z       | editor/redo                  |
| Quit                  | Ctrl + Q               | Cmd + Q               | editor/file_quit             |
| Quit to Project List  | Ctrl + Shift + Q       | Shift + Opt + Q       | editor/quit_to_project_list  |
| Take Screenshot       | Ctrl + F12             | Cmd + F12             | editor/take_screenshot       |
| Toggle Fullscreen     | Shift + F11            | Cmd + Ctrl + F        | editor/fullscreen_mode       |
| Play                  | F5                     | Cmd + B               | editor/play                  |
| Pause Scene           | F7                     | Cmd + Ctrl + Y        | editor/pause_scene           |
| Stop                  | F8                     | Cmd + .               | editor/stop                  |
| Play Scene            | F6                     | Cmd + R               | editor/play_scene            |
| Play Custom Scene     | Ctrl + Shift + F5      | Cmd + Shift + R       | editor/play_custom_scene     |
| Expand Bottom Panel   | Shift + F12            | Shift + F12           | editor/bottom_panel_expand   |
| Command Palette       | Ctrl + Shift + P       | Cmd + Shift + P       | editor/command_palette       |

### Bottom panels

Only bottom panels that are always available have a default shortcut assigned. Others must be manually bound in the Editor Settings if desired.

| Action name                       | Windows, Linux | macOS    | Editor setting                                  |
| --------------------------------- | -------------- | -------- | ----------------------------------------------- |
| Toggle Last Opened Panel          | Ctrl + J       | Ctrl + J | editor/toggle_last_opened_bottom_panel          |
| Toggle Animation Bottom Panel     | Alt + N        | Alt + N  | bottom_panels/toggle_animation_bottom_panel     |
| Toggle Audio Bottom Panel         | Alt + A        | Alt + A  | bottom_panels/toggle_audio_bottom_panel         |
| Toggle Debugger Bottom Panel      | Alt + D        | Alt + D  | bottom_panels/toggle_debugger_bottom_panel      |
| Toggle FileSystem Bottom Panel    | Alt + F        | Alt + F  | bottom_panels/toggle_filesystem_bottom_panel    |
| Toggle Output Bottom Panel        | Alt + O        | Alt + O  | bottom_panels/toggle_output_bottom_panel        |
| Toggle Shader Editor Bottom Panel | Alt + S        | Alt + S  | bottom_panels/toggle_shader_editor_bottom_panel |

### 2D / CanvasItem editor

| Action name                  | Windows, Linux   | macOS           | Editor setting                                     |
| ---------------------------- | ---------------- | --------------- | -------------------------------------------------- |
| Zoom In                      | Ctrl + =         | Cmd + =         | canvas_item_editor/zoom_plus                       |
| Zoom Out                     | Ctrl + -         | Cmd + -         | canvas_item_editor/zoom_minus                      |
| Zoom Reset                   | Ctrl + 0         | Cmd + 0         | canvas_item_editor/zoom_reset                      |
| Pan View                     | Space            | Space           | canvas_item_editor/pan_view                        |
| Select Mode                  | Q                | Q               | canvas_item_editor/select_mode                     |
| Move Mode                    | W                | W               | canvas_item_editor/move_mode                       |
| Rotate Mode                  | E                | E               | canvas_item_editor/rotate_mode                     |
| Scale Mode                   | S                | S               | canvas_item_editor/scale_mode                      |
| Ruler Mode                   | R                | R               | canvas_item_editor/ruler_mode                      |
| Use Smart Snap               | Shift + S        | Shift + S       | canvas_item_editor/use_smart_snap                  |
| Use Grid Snap                | Shift + G        | Shift + G       | canvas_item_editor/use_grid_snap                   |
| Multiply grid step by 2      | Num \*           | Num \*          | canvas_item_editor/multiply_grid_step              |
| Divide grid step by 2        | Num /            | Num /           | canvas_item_editor/divide_grid_step                |
| Always Show Grid             | G                | G               | canvas_item_editor/show_grid                       |
| Show Helpers                 | H                | H               | canvas_item_editor/show_helpers                    |
| Show Guides                  | Y                | Y               | canvas_item_editor/show_guides                     |
| Center Selection             | F                | F               | canvas_item_editor/center_selection                |
| Frame Selection              | Shift + F        | Shift + F       | canvas_item_editor/frame_selection                 |
| Preview Canvas Scale         | Ctrl + Shift + P | Cmd + Shift + P | canvas_item_editor/preview_canvas_scale            |
| Insert Key                   | Ins              | Ins             | canvas_item_editor/anim_insert_key                 |
| Insert Key (Existing Tracks) | Ctrl + Ins       | Cmd + Ins       | canvas_item_editor/anim_insert_key_existing_tracks |
| Make Custom Bones from Nodes | Ctrl + Shift + B | Cmd + Shift + B | canvas_item_editor/skeleton_make_bones             |
| Clear Pose                   | Shift + K        | Shift + K       | canvas_item_editor/anim_clear_pose                 |

### 3D / Spatial editor

| Action name                        | Windows, Linux | macOS         | Editor setting                               |
| ---------------------------------- | -------------- | ------------- | -------------------------------------------- |
| Toggle Freelook                    | Shift + F      | Shift + F     | spatial_editor/freelook_toggle               |
| Freelook Left                      | A              | A             | spatial_editor/freelook_left                 |
| Freelook Right                     | D              | D             | spatial_editor/freelook_right                |
| Freelook Forward                   | W              | W             | spatial_editor/freelook_forward              |
| Freelook Backwards                 | S              | S             | spatial_editor/freelook_backwards            |
| Freelook Up                        | E              | E             | spatial_editor/freelook_up                   |
| Freelook Down                      | Q              | Q             | spatial_editor/freelook_down                 |
| Freelook Speed Modifier            | Shift          | Shift         | spatial_editor/freelook_speed_modifier       |
| Freelook Slow Modifier             | Alt            | Opt           | spatial_editor/freelook_slow_modifier        |
| Select Mode                        | Q              | Q             | spatial_editor/tool_select                   |
| Move Mode                          | W              | W             | spatial_editor/tool_move                     |
| Rotate Mode                        | E              | E             | spatial_editor/tool_rotate                   |
| Scale Mode                         | R              | R             | spatial_editor/tool_scale                    |
| Use Local Space                    | T              | T             | spatial_editor/local_coords                  |
| Use Snap                           | Y              | Y             | spatial_editor/snap                          |
| Snap Object to Floor               | PgDown         | PgDown        | spatial_editor/snap_to_floor                 |
| Top View                           | Num 7          | Num 7         | spatial_editor/top_view                      |
| Bottom View                        | Alt + Num 7    | Opt + Num 7   | spatial_editor/bottom_view                   |
| Front View                         | Num 1          | Num 1         | spatial_editor/front_view                    |
| Rear View                          | Alt + Num 1    | Opt + Num 1   | spatial_editor/rear_view                     |
| Right View                         | Num 3          | Num 3         | spatial_editor/right_view                    |
| Left View                          | Alt + Num 3    | Opt + Num 3   | spatial_editor/left_view                     |
| Switch Perspective/Orthogonal View | Num 5          | Num 5         | spatial_editor/switch_perspective_orthogonal |
| Insert Animation Key               | K              | K             | spatial_editor/insert_anim_key               |
| Focus Origin                       | O              | O             | spatial_editor/focus_origin                  |
| Focus Selection                    | F              | F             | spatial_editor/focus_selection               |
| Align Transform with View          | Ctrl + Alt + M | Opt + Cmd + M | spatial_editor/align_transform_with_view     |
| Align Rotation with View           | Ctrl + Alt + F | Opt + Cmd + F | spatial_editor/align_rotation_with_view      |
| 1 Viewport                         | Ctrl + 1       | Cmd + 1       | spatial_editor/1_viewport                    |
| 2 Viewports                        | Ctrl + 2       | Cmd + 2       | spatial_editor/2_viewports                   |
| 2 Viewports (Alt)                  | Ctrl + Alt + 2 | Opt + Cmd + 2 | spatial_editor/2_viewports_alt               |
| 3 Viewports                        | Ctrl + 3       | Cmd + 3       | spatial_editor/3_viewports                   |
| 3 Viewports (Alt)                  | Ctrl + Alt + 3 | Opt + Cmd + 3 | spatial_editor/3_viewports_alt               |
| 4 Viewports                        | Ctrl + 4       | Cmd + 4       | spatial_editor/4_viewports                   |

### Text editor

| Action name               | Windows, Linux            | macOS                    | Editor setting                                   |
| ------------------------- | ------------------------- | ------------------------ | ------------------------------------------------ |
| Cut                       | Ctrl + X                  | Cmd + X                  | script_text_editor/cut                           |
| Copy                      | Ctrl + C                  | Cmd + C                  | script_text_editor/copy                          |
| Paste                     | Ctrl + V                  | Cmd + V                  | script_text_editor/paste                         |
| Select All                | Ctrl + A                  | Cmd + A                  | script_text_editor/select_all                    |
| Find                      | Ctrl + F                  | Cmd + F                  | script_text_editor/find                          |
| Find Next                 | F3                        | Cmd + G                  | script_text_editor/find_next                     |
| Find Previous             | Shift + F3                | Cmd + Shift + G          | script_text_editor/find_previous                 |
| Find in Files             | Ctrl + Shift + F          | Cmd + Shift + F          | script_text_editor/find_in_files                 |
| Replace                   | Ctrl + R                  | Opt + Cmd + F            | script_text_editor/replace                       |
| Replace in Files          | Ctrl + Shift + R          | Cmd + Shift + R          | script_text_editor/replace_in_files              |
| Undo                      | Ctrl + Z                  | Cmd + Z                  | script_text_editor/undo                          |
| Redo                      | Ctrl + Y                  | Cmd + Y                  | script_text_editor/redo                          |
| Move Up                   | Alt + Up Arrow            | Opt + Up Arrow           | script_text_editor/move_up                       |
| Move Down                 | Alt + Down Arrow          | Opt + Down Arrow         | script_text_editor/move_down                     |
| Delete Line               | Ctrl + Shift + K          | Cmd + Shift + K          | script_text_editor/delete_line                   |
| Toggle Comment            | Ctrl + K                  | Cmd + K                  | script_text_editor/toggle_comment                |
| Fold/Unfold Line          | Alt + F                   | Ctrl + Cmd + F           | script_text_editor/toggle_fold_line              |
| Duplicate Lines           | Ctrl + Alt + Down Arrow   | Cmd + Shift + Down Arrow | script_text_editor/duplicate_lines               |
| Duplicate Selection       | Ctrl + Shift + D          | Cmd + Shift + C          | script_text_editor/duplicate_selection           |
| Select Down               | Ctrl + Shift + Down Arrow | Shift + Opt + Down Arrow | common/ui_text_caret_add_below                   |
| Select Up                 | Ctrl + Shift + Up Arrow   | Shift + Opt + Up Arrow   | common/ui_text_caret_add_above                   |
| Select Next Occurrence    | Ctrl + D                  | Cmd + D                  | common/ui_text_add_selection_for_next_occurrence |
| Complete Symbol           | Ctrl + Space              | Ctrl + Space             | script_text_editor/complete_symbol               |
| Evaluate Selection        | Ctrl + Shift + E          | Cmd + Shift + E          | script_text_editor/evaluate_selection            |
| Trim Trailing Whitespace  | Ctrl + Alt + T            | Opt + Cmd + T            | script_text_editor/trim_trailing_whitespace      |
| Uppercase                 | Shift + F4                | Shift + F4               | script_text_editor/convert_to_uppercase          |
| Lowercase                 | Shift + F5                | Shift + F5               | script_text_editor/convert_to_lowercase          |
| Capitalize                | Shift + F6                | Shift + F6               | script_text_editor/capitalize                    |
| Convert Indent to Spaces  | Ctrl + Shift + Y          | Cmd + Shift + Y          | script_text_editor/convert_indent_to_spaces      |
| Convert Indent to Tabs    | Ctrl + Shift + I          | Cmd + Shift + I          | script_text_editor/convert_indent_to_tabs        |
| Auto Indent               | Ctrl + I                  | Cmd + I                  | script_text_editor/auto_indent                   |
| Toggle Bookmark           | Ctrl + Alt + B            | Opt + Cmd + B            | script_text_editor/toggle_bookmark               |
| Go to Next Bookmark       | Ctrl + B                  | Cmd + B                  | script_text_editor/goto_next_bookmark            |
| Go to Previous Bookmark   | Ctrl + Shift + B          | Cmd + Shift + B          | script_text_editor/goto_previous_bookmark        |
| Go to Function            | Ctrl + Alt + F            | Ctrl + Cmd + J           | script_text_editor/goto_function                 |
| Go to Line                | Ctrl + G                  | Cmd + L                  | script_text_editor/goto_line                     |
| Toggle Breakpoint         | F9                        | Cmd + Shift + B          | script_text_editor/toggle_breakpoint             |
| Remove All Breakpoints    | Ctrl + Shift + F9         | Cmd + Shift + F9         | script_text_editor/remove_all_breakpoints        |
| Go to Next Breakpoint     | Ctrl + .                  | Cmd + .                  | script_text_editor/goto_next_breakpoint          |
| Go to Previous Breakpoint | Ctrl + ,                  | Cmd + ,                  | script_text_editor/goto_previous_breakpoint      |
| Contextual Help           | Alt + F1                  | Opt + Shift + Space      | script_text_editor/contextual_help               |

### Script editor

| Action name          | Windows, Linux           | macOS                    | Editor setting                     |
| -------------------- | ------------------------ | ------------------------ | ---------------------------------- |
| Find                 | Ctrl + F                 | Cmd + F                  | script_editor/find                 |
| Find Next            | F3                       | F3                       | script_editor/find_next            |
| Find Previous        | Shift + F3               | Shift + F3               | script_editor/find_previous        |
| Find in Files        | Ctrl + Shift + F         | Cmd + Shift + F          | script_editor/find_in_files        |
| Move Up              | Shift + Alt + Up Arrow   | Shift + Opt + Up Arrow   | script_editor/window_move_up       |
| Move Down            | Shift + Alt + Down Arrow | Shift + Opt + Down Arrow | script_editor/window_move_down     |
| Next Script          | Ctrl + Shift + .         | Cmd + Shift + .          | script_editor/next_script          |
| Previous Script      | Ctrl + Shift + ,         | Cmd + Shift + ,          | script_editor/prev_script          |
| Reopen Closed Script | Ctrl + Shift + T         | Cmd + Shift + T          | script_editor/reopen_closed_script |
| Save                 | Ctrl + Alt + S           | Opt + Cmd + S            | script_editor/save                 |
| Save All             | Ctrl + Shift + Alt + S   | Cmd + Shift + Opt + S    | script_editor/save_all             |
| Soft Reload Script   | Ctrl + Shift + R         | Cmd + Shift + R          | script_editor/reload_script_soft   |
| History Previous     | Alt + Left Arrow         | Opt + Left Arrow         | script_editor/history_previous     |
| History Next         | Alt + Right Arrow        | Opt + Right Arrow        | script_editor/history_next         |
| Close                | Ctrl + W                 | Cmd + W                  | script_editor/close_file           |
| Run                  | Ctrl + Shift + X         | Cmd + Shift + X          | script_editor/run_file             |
| Toggle Scripts Panel | Ctrl + \                 | Cmd + \                  | script_editor/toggle_scripts_panel |
| Zoom In              | Ctrl + =                 | Cmd + =                  | script_editor/zoom_in              |
| Zoom Out             | Ctrl + -                 | Cmd + -                  | script_editor/zoom_out             |
| Reset Zoom           | Ctrl + 0                 | Cmd + 0                  | script_editor/reset_zoom           |

### Editor output

| Action name    | Windows, Linux   | macOS           | Editor setting      |
| -------------- | ---------------- | --------------- | ------------------- |
| Copy Selection | Ctrl + C         | Cmd + C         | editor/copy_output  |
| Clear Output   | Ctrl + Shift + K | Cmd + Shift + K | editor/clear_output |

### Debugger

| Action name | Windows, Linux | macOS | Editor setting     |
| ----------- | -------------- | ----- | ------------------ |
| Step Into   | F11            | F11   | debugger/step_into |
| Step Over   | F10            | F10   | debugger/step_over |
| Continue    | F12            | F12   | debugger/continue  |

### File dialog

| Action name         | Windows, Linux    | macOS             | Editor setting                  |
| ------------------- | ----------------- | ----------------- | ------------------------------- |
| Go Back             | Alt + Left Arrow  | Opt + Left Arrow  | file_dialog/go_back             |
| Go Forward          | Alt + Right Arrow | Opt + Right Arrow | file_dialog/go_forward          |
| Go Up               | Alt + Up Arrow    | Opt + Up Arrow    | file_dialog/go_up               |
| Refresh             | F5                | F5                | file_dialog/refresh             |
| Toggle Hidden Files | Ctrl + H          | Cmd + H           | file_dialog/toggle_hidden_files |
| Toggle Favorite     | Alt + F           | Opt + F           | file_dialog/toggle_favorite     |
| Toggle Mode         | Alt + V           | Opt + V           | file_dialog/toggle_mode         |
| Create Folder       | Ctrl + N          | Cmd + N           | file_dialog/create_folder       |
| Delete              | Del               | Cmd + BkSp        | file_dialog/delete              |
| Focus Path          | Ctrl + L          | Cmd + Shift + G   | file_dialog/focus_path          |
| Move Favorite Up    | Ctrl + Up Arrow   | Cmd + Up Arrow    | file_dialog/move_favorite_up    |
| Move Favorite Down  | Ctrl + Down Arrow | Cmd + Down Arrow  | file_dialog/move_favorite_down  |

### FileSystem dock

| Action name | Windows, Linux | macOS      | Editor setting            |
| ----------- | -------------- | ---------- | ------------------------- |
| Copy Path   | Ctrl + C       | Cmd + C    | filesystem_dock/copy_path |
| Duplicate   | Ctrl + D       | Cmd + D    | filesystem_dock/duplicate |
| Delete      | Del            | Cmd + BkSp | filesystem_dock/delete    |

### Scene tree dock

| Action name    | Windows, Linux    | macOS            | Editor setting               |
| -------------- | ----------------- | ---------------- | ---------------------------- |
| Add Child Node | Ctrl + A          | Cmd + A          | scene_tree/add_child_node    |
| Batch Rename   | Ctrl + F2         | Cmd + F2         | scene_tree/batch_rename      |
| Copy Node Path | Ctrl + Shift + C  | Cmd + Shift + C  | scene_tree/copy_node_path    |
| Delete         | Del               | Cmd + BkSp       | scene_tree/delete            |
| Force Delete   | Shift + Del       | Shift + Del      | scene_tree/delete_no_confirm |
| Duplicate      | Ctrl + D          | Cmd + D          | scene_tree/duplicate         |
| Move Up        | Ctrl + Up Arrow   | Cmd + Up Arrow   | scene_tree/move_up           |
| Move Down      | Ctrl + Down Arrow | Cmd + Down Arrow | scene_tree/move_down         |

### Animation track editor

| Action name          | Windows, Linux     | macOS             | Editor setting                                  |
| -------------------- | ------------------ | ----------------- | ----------------------------------------------- |
| Duplicate Selection  | Ctrl + D           | Cmd + D           | animation_editor/duplicate_selection            |
| Duplicate Transposed | Ctrl + Shift + D   | Cmd + Shift + D   | animation_editor/duplicate_selection_transposed |
| Delete Selection     | Del                | Cmd + BkSp        | animation_editor/delete_selection               |
| Go to Next Step      | Ctrl + Right Arrow | Cmd + Right Arrow | animation_editor/goto_next_step                 |
| Go to Previous Step  | Ctrl + Left Arrow  | Cmd + Left Arrow  | animation_editor/goto_prev_step                 |

### TileMap editor

| Action name       | Windows, Linux | macOS      | Editor setting                    |
| ----------------- | -------------- | ---------- | --------------------------------- |
| Select            | S              | S          | tiles_editor/selection_tool       |
| Cut Selection     | Ctrl + X       | Cmd + X    | tiles_editor/cut                  |
| Copy Selection    | Ctrl + C       | Cmd + C    | tiles_editor/copy                 |
| Paste Selection   | Ctrl + V       | Cmd + V    | tiles_editor/paste                |
| Delete Selection  | Del            | Cmd + BkSp | tiles_editor/delete               |
| Cancel            | Esc            | Esc        | tiles_editor/cancel               |
| Paint             | D              | D          | tiles_editor/paint_tool           |
| Line              | L              | L          | tiles_editor/line_tool            |
| Rect              | R              | R          | tiles_editor/rect_tool            |
| Bucket            | B              | B          | tiles_editor/bucket_tool          |
| Picker            | P              | P          | tiles_editor/picker               |
| Eraser            | E              | E          | tiles_editor/eraser               |
| Flip Horizontally | C              | C          | tiles_editor/flip_tile_horizontal |
| Flip Vertically   | V              | V          | tiles_editor/flip_tile_vertical   |
| Rotate Left       | Z              | Z          | tiles_editor/rotate_tile_left     |
| Rotate Right      | X              | X          | tiles_editor/rotate_tile_right    |

### TileSet Editor

| Action name         | Windows, Linux | macOS  | Editor setting                     |
| ------------------- | -------------- | ------ | ---------------------------------- |
| Next Coordinate     | PgDown         | PgDown | tileset_editor/next_shape          |
| Previous Coordinate | PgUp           | PgUp   | tileset_editor/previous_shape      |
| Region Mode         | 1              | 1      | tileset_editor/editmode_region     |
| Collision Mode      | 2              | 2      | tileset_editor/editmode_collision  |
| Occlusion Mode      | 3              | 3      | tileset_editor/editmode_occlusion  |
| Navigation Mode     | 4              | 4      | tileset_editor/editmode_navigation |
| Bitmask Mode        | 5              | 5      | tileset_editor/editmode_bitmask    |
| Priority Mode       | 6              | 6      | tileset_editor/editmode_priority   |
| Icon Mode           | 7              | 7      | tileset_editor/editmode_icon       |
| Z Index Mode        | 8              | 8      | tileset_editor/editmode_z_index    |

### GridMap Editor

| Action name     | Windows, Linux | macOS     | Editor setting           |
| --------------- | -------------- | --------- | ------------------------ |
| Previous Floor  | 1              | 1         | grid_map/previous_floor  |
| Next Floor      | 3              | 3         | grid_map/next_floor      |
| Edit X Axis     | Shift + Z      | Shift + Z | grid_map/edit_x_axis     |
| Edit Y Axis     | Shift + X      | Shift + X | grid_map/edit_y_axis     |
| Edit Z Axis     | Shift + C      | Shift + C | grid_map/edit_z_axis     |
| Transform       | T              | T         | grid_map/transform_tool  |
| Selection       | Q              | Q         | grid_map/selection_tool  |
| Erase           | W              | W         | grid_map/erase_tool      |
| Paint           | E              | E         | grid_map/paint_tool      |
| Pick            | R              | R         | grid_map/pick_tool       |
| Fill            | Z              | Z         | grid_map/fill_tool       |
| Move            | X              | X         | grid_map/move_tool       |
| Duplicate       | C              | C         | grid_map/duplicate_tool  |
| Delete          | V              | V         | grid_map/delete_tool     |
| Cursor Rotate X | A              | A         | grid_map/cursor_rotate_x |
| Cursor Rotate Y | S              | S         | grid_map/cursor_rotate_y |
| Cursor Rotate Z | D              | D         | grid_map/cursor_rotate_z |

### Project manager

| Action name       | Windows, Linux | macOS      | Editor setting                 |
| ----------------- | -------------- | ---------- | ------------------------------ |
| New Project       | Ctrl + N       | Cmd + N    | project_manager/new_project    |
| Import Project    | Ctrl + I       | Cmd + I    | project_manager/import_project |
| Scan for Projects | Ctrl + S       | Cmd + S    | project_manager/scan_projects  |
| Edit Project      | Ctrl + E       | Cmd + E    | project_manager/edit_project   |
| Run Project       | Ctrl + R       | Cmd + R    | project_manager/run_project    |
| Rename Project    | F2             | Enter      | project_manager/rename_project |
| Remove Project    | Delete         | Cmd + BkSp | project_manager/remove_project |

---

## Using an external text editor

This page explains how to code using an external text editor.

> **Note:** To code C# in an external editor, see [the C# guide to configure an external editor](tutorials_scripting.md).

Godot can be used with an external text editor, such as Sublime Text or Visual Studio Code. Browse to the relevant editor settings: **Editor > Editor Settings > Text Editor > External**

There are two text fields: the executable path and command-line flags. The flags allow you to integrate the editor with Godot, passing it the file path to open and other relevant arguments. Godot will replace the following placeholders in the flags string:

| Field in Exec Flags | Is replaced with                           |
| ------------------- | ------------------------------------------ |
| {project}           | The absolute path to the project directory |
| {file}              | The absolute path to the file              |
| {col}               | The column number of the error             |
| {line}              | The line number of the error               |

Some example **Exec Flags** for various editors include:

| Editor             | Exec Flags                           |
| ------------------ | ------------------------------------ |
| Geany/Kate         | {file} --line {line} --column {col}  |
| Atom               | {file}:{line}                        |
| JetBrains Rider    | {project} --line {line} {file}       |
| Visual Studio Code | {project} --goto {file}:{line}:{col} |
| Vim (gVim)         | "+call cursor({line}, {col})" {file} |
| Emacs              | emacs +{line}:{col} {file}           |
| Sublime Text/Zed   | {project} {file}:{line}:{col}        |
| Visual Studio\*    | /edit "{file}"                       |

\*: Arguments are not automatically detected, so you must fill them in manually.

Since Godot 4.5, **Exec Flags** are automatically detected for all editors listed above (unless denoted with an asterisk). You don't need to paste them from this page for it to work, unless your editor has an executable name not recognized automatically (e.g. a fork of an editor listed here).

> **Note:** For Visual Studio Code on Windows, you will have to point to the `code.cmd` file. For Emacs, you can call `emacsclient` instead of `emacs` if you use the server mode. For Visual Studio, you will have to open the solution file `.sln` manually to get access to the IDE features. Additionally, it will not go to a specific line.

### Automatically reloading your changes

To have the Godot Editor automatically reload any script that has been changed by an external text editor, enable **Editor > Editor Settings > Text Editor > Behavior > Auto Reload Scripts on External Change**.

### Using External Editor in Debugger

Using external editor in debugger is determined by a separate option in settings. For details, see [Script editor debug tools and options](tutorials_scripting.md).

### Official editor plugins

We have official plugins for the following code editors:

- [Visual Studio Code](https://github.com/godotengine/godot-vscode-plugin)
- [Emacs](https://github.com/godotengine/emacs-gdscript-mode)

### LSP/DAP support

Godot supports the [Language Server Protocol](https://microsoft.github.io/language-server-protocol/) (**LSP**) for code completion and the [Debug Adapter Protocol](https://microsoft.github.io/debug-adapter-protocol/) (**DAP**) for debugging. You can check the [LSP client list](https://microsoft.github.io/language-server-protocol/implementors/tools/) and [DAP client list](https://microsoft.github.io/debug-adapter-protocol/implementors/tools/) to find if your editor supports them. If this is the case, you should be able to take advantage of these features without the need of a custom plugin.

To use these protocols, a Godot instance must be running on your current project. You should then configure your editor to communicate to the running adapter ports in Godot, which by default are `6005` for **LSP**, and `6006` for **DAP**. You can change these ports and other settings in the **Editor Settings**, under the **Network > Language Server** and **Network > Debug Adapter** sections respectively.

Below are some configuration steps for specific editors:

#### Visual Studio Code

You need to install the official [Visual Studio Code plugin](https://github.com/godotengine/godot-vscode-plugin).

For **LSP**, follow [these instructions](https://github.com/godotengine/godot-vscode-plugin#gdscript_lsp_server_port) to change the default LSP port. The connection status can be checked on the status bar:

For **DAP**, specify the `debugServer` property in your `launch.json` file:

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "GDScript Godot",
            "type": "godot",
            "request": "launch",
            "project": "${workspaceFolder}",
            "port": 6007,
            "debugServer": 6006
        }
    ]
}
```

#### Emacs

Check the official instructions to configure [LSP](https://github.com/godotengine/emacs-gdscript-mode#auto-completion-with-the-language-server-protocol-lsp), and [DAP](https://github.com/godotengine/emacs-gdscript-mode#using-the-debugger).

---
