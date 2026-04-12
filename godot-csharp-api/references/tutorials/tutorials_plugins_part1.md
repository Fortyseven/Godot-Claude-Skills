# Godot 4 C# Tutorials — Plugins (Part 1)

> 7 tutorials. C#-specific code examples.

## 3D gizmo plugins

> **Work in progress:** The content of this page was not yet updated for Godot `4.6` and may be **outdated**. If you know how to improve this page or you can confirm that it's up to date, feel free to [open a pull request](https://github.com/godotengine/godot-docs).

### Introduction

3D gizmo plugins are used by the editor and custom plugins to define the gizmos attached to any kind of Node3D node.

This tutorial shows the two main approaches to defining your own custom gizmos. The first option works well for simple gizmos and creates less clutter in your plugin structure, and the second one will let you store some per-gizmo data.

> **Note:** This tutorial assumes you already know how to make generic plugins. If in doubt, refer to the Making plugins page.

### The EditorNode3DGizmoPlugin

Regardless of the approach we choose, we will need to create a new [EditorNode3DGizmoPlugin](../godot_csharp_editor.md). This will allow us to set a name for the new gizmo type and define other behaviors such as whether the gizmo can be hidden or not.

This would be a basic setup:

For simple gizmos, inheriting [EditorNode3DGizmoPlugin](../godot_csharp_editor.md) is enough. If you want to store some per-gizmo data, you should go with the second approach.

### Simple approach

The first step is to, in our custom gizmo plugin, override the [\_has_gizmo()](../godot_csharp_misc.md) method so that it returns `true` when the node parameter is of our target type.

Then we can override methods like [\_redraw()](../godot_csharp_misc.md) or all the handle related ones.

Note that we created a material in the \_init method, and retrieved it in the \_redraw method using [get_material()](../godot_csharp_misc.md). This method retrieves one of the material's variants depending on the state of the gizmo (selected and/or editable).

So the final plugin would look somewhat like this:

Note that we just added some handles in the \_redraw method, but we still need to implement the rest of handle-related callbacks in [EditorNode3DGizmoPlugin](../godot_csharp_editor.md) to get properly working handles.

### Alternative approach

In some cases we want to provide our own implementation of [EditorNode3DGizmo](../godot_csharp_editor.md), maybe because we want to have some state stored in each gizmo or because we are porting an old gizmo plugin and we don't want to go through the rewriting process.

In these cases all we need to do is, in our new gizmo plugin, override [\_create_gizmo()](../godot_csharp_misc.md), so it returns our custom gizmo implementation for the Node3D nodes we want to target.

This way all the gizmo logic and drawing methods can be implemented in a new class extending [EditorNode3DGizmo](../godot_csharp_editor.md), like so:

Note that we just added some handles in the \_redraw method, but we still need to implement the rest of handle-related callbacks in [EditorNode3DGizmo](../godot_csharp_editor.md) to get properly working handles.

---

## Import plugins

> **Work in progress:** The content of this page was not yet updated for Godot `4.6` and may be **outdated**. If you know how to improve this page or you can confirm that it's up to date, feel free to [open a pull request](https://github.com/godotengine/godot-docs).

> **Note:** This tutorial assumes you already know how to make generic plugins. If in doubt, refer to the Making plugins page. This also assumes you are acquainted with Godot's import system.

### Introduction

An import plugin is a special type of editor tool that allows custom resources to be imported by Godot and be treated as first-class resources. The editor itself comes bundled with a lot of import plugins to handle the common resources like PNG images, Collada and glTF models, Ogg Vorbis sounds, and many more.

This tutorial shows how to create an import plugin to load a custom text file as a material resource. This text file will contain three numeric values separated by comma, which represents the three channels of a color, and the resulting color will be used as the albedo (main color) of the imported material. In this example it contains the pure blue color (zero red, zero green, and full blue):

```none
0,0,255
```

### Configuration

First we need a generic plugin that will handle the initialization and destruction of our import plugin. Let's add the `plugin.cfg` file first:

```ini
[plugin]

name="Silly Material Importer"
description="Imports a 3D Material from an external text file."
author="Yours Truly"
version="1.0"
script="material_import.gd"
```

Then we need the `material_import.gd` file to add and remove the import plugin when needed:

When this plugin is activated, it will create a new instance of the import plugin (which we'll soon make) and add it to the editor using the [add_import_plugin()](../godot_csharp_misc.md) method. We store a reference to it in a class member `import_plugin` so we can refer to it later when removing it. The [remove_import_plugin()](../godot_csharp_misc.md) method is called when the plugin is deactivated to clean up the memory and let the editor know the import plugin isn't available anymore.

Note that the import plugin is a reference type, so it doesn't need to be explicitly released from memory with the `free()` function. It will be released automatically by the engine when it goes out of scope.

### The EditorImportPlugin class

The main character of the show is the [EditorImportPlugin class](../godot_csharp_editor.md). It is responsible for implementing the methods that are called by Godot when it needs to know how to deal with files.

Let's begin to code our plugin, one method at time:

The first method is the [\_get_importer_name()](../godot_csharp_misc.md). This is a unique name for your plugin that is used by Godot to know which import was used in a certain file. When the files needs to be reimported, the editor will know which plugin to call.

The [\_get_visible_name()](../godot_csharp_misc.md) method is responsible for returning the name of the type it imports and it will be shown to the user in the Import dock.

You should choose this name as a continuation to "Import as", e.g. _"Import as Silly Material"_. You can name it whatever you want but we recommend a descriptive name for your plugin.

Godot's import system detects file types by their extension. In the [\_get_recognized_extensions()](../godot_csharp_misc.md) method you return an array of strings to represent each extension that this plugin can understand. If an extension is recognized by more than one plugin, the user can select which one to use when importing the files.

> **Tip:** Common extensions like `.json` and `.txt` might be used by many plugins. Also, there could be files in the project that are just data for the game and should not be imported. You have to be careful when importing to validate the data. Never expect the file to be well-formed.

The imported files are saved in the `.import` folder at the project's root. Their extension should match the type of resource you are importing, but since Godot can't tell what you'll use (because there might be multiple valid extensions for the same resource), you need to declare what will be used in the import.

Since we're importing a Material, we'll use the special extension for such resource types. If you are importing a scene, you can use `scn`. Generic resources can use the `res` extension. However, this is not enforced in any way by the engine.

The imported resource has a specific type, so the editor can know which property slot it belongs to. This allows drag and drop from the FileSystem dock to a property in the Inspector.

In our case it's a [StandardMaterial3D](../godot_csharp_rendering.md), which can be applied to 3D objects.

> **Note:** If you need to import different types from the same extension, you have to create multiple import plugins. You can abstract the import code on another file to avoid duplication in this regard.

### Options and presets

Your plugin can provide different options to allow the user to control how the resource will be imported. If a set of selected options is common, you can also create different presets to make it easier for the user. The following image shows how the options will appear in the editor:

Since there might be many presets and they are identified with a number, it's a good practice to use an enum so you can refer to them using names.

Now that the enum is defined, let's keep looking at the methods of an import plugin:

The [\_get_preset_count()](../godot_csharp_misc.md) method returns the amount of presets that this plugins defines. We only have one preset now, but we can make this method future-proof by returning the size of our `Presets` enumeration.

Here we have the [\_get_preset_name()](../godot_csharp_misc.md) method, which gives names to the presets as they will be presented to the user, so be sure to use short and clear names.

We can use the `match` statement here to make the code more structured. This way it's easy to add new presets in the future. We use the catch all pattern to return something too. Although Godot won't ask for presets beyond the preset count you defined, it's always better to be on the safe side.

If you have only one preset you could simply return its name directly, but if you do this you have to be careful when you add more presets.

This is the method which defines the available options. [\_get_import_options()](../godot_csharp_misc.md) returns an array of dictionaries, and each dictionary contains a few keys that are checked to customize the option as it's shown to the user. The following table shows the possible keys:

| Key           | Type       | Description                                                                                       |
| ------------- | ---------- | ------------------------------------------------------------------------------------------------- |
| name          | String     | The name of the option. When showed, underscores become spaces and first letters are capitalized. |
| default_value | Any        | The default value of the option for this preset.                                                  |
| property_hint | Enum value | One of the PropertyHint values to use as hint.                                                    |
| hint_string   | String     | The hint text of the property. The same as you'd add in the export statement in GDScript.         |
| usage         | Enum value | One of the PropertyUsageFlags values to define the usage.                                         |

The `name` and `default_value` keys are **mandatory**, the rest are optional.

Note that the `_get_import_options` method receives the preset number, so you can configure the options for each different preset (especially the default value). In this example we use the `match` statement, but if you have lots of options and the presets only change the value you may want to create the array of options first and then change it based on the preset.

> **Warning:** The `_get_import_options` method is called even if you don't define presets (by making `_get_preset_count` return zero). You have to return an array even it's empty, otherwise you can get errors.

For the [\_get_option_visibility()](../godot_csharp_misc.md) method, we simply return `true` because all of our options (i.e. the single one we defined) are visible all the time.

If you need to make certain option visible only if another is set with a certain value, you can add the logic in this method.

### The import method

The heavy part of the process, responsible for converting the files into resources, is covered by the [\_import()](../godot_csharp_misc.md) method. Our sample code is a bit long, so let's split in a few parts:

The first part of our import method opens and reads the source file. We use the [FileAccess](../godot_csharp_filesystem.md) class to do that, passing the `source_file` parameter which is provided by the editor.

If there's an error when opening the file, we return it to let the editor know that the import wasn't successful.

This code takes the line of the file it read before and splits it in pieces that are separated by a comma. If there are more or less than the three values, it considers the file invalid and reports an error.

Then it creates a new [Color](../godot_csharp_math_types.md) variable and sets its values according to the input file. If the `use_red_anyway` option is enabled, then it sets the color as a pure red instead.

This part makes a new [StandardMaterial3D](../godot_csharp_rendering.md) that is the imported resource. We create a new instance of it and then set its albedo color as the value we got before.

This is the last part and quite an important one, because here we save the made resource to the disk. The path of the saved file is generated and informed by the editor via the `save_path` parameter. Note that this comes **without** the extension, so we add it using [string formatting](tutorials_scripting.md). For this we call the `_get_save_extension` method that we defined earlier, so we can be sure that they won't get out of sync.

We also return the result from the [ResourceSaver.save()](../godot_csharp_core.md) method, so if there's an error in this step, the editor will know about it.

### Platform variants and generated files

You may have noticed that our plugin ignored two arguments of the `import` method. Those are _return arguments_ (hence the `r` at the beginning of their name), which means that the editor will read from them after calling your import method. Both of them are arrays that you can fill with information.

The `r_platform_variants` argument is used if you need to import the resource differently depending on the target platform. While it's called _platform_ variants, it is based on the presence of [feature tags](tutorials_export.md), so even the same platform can have multiple variants depending on the setup.

To import a platform variant, you need to save it with the feature tag before the extension, and then push the tag to the `r_platform_variants` array so the editor can know that you did.

For example, let's say we save a different material for a mobile platform. We would need to do something like the following:

The `r_gen_files` argument is meant for extra files that are generated during your import process and need to be kept. The editor will look at it to understand the dependencies and make sure the extra file is not inadvertently deleted.

This is also an array and should be filled with full paths of the files you save. As an example, let's create another material for the next pass and save it in a different file:

### Trying the plugin

This has been theoretical, but now that the import plugin is done, let's test it. Make sure you created the sample file (with the contents described in the introduction section) and save it as `test.mtxt`. Then activate the plugin in the Project Settings.

If everything goes well, the import plugin is added to the editor and the file system is scanned, making the custom resource appear on the FileSystem dock. If you select it and focus the Import dock, you can see the only option to select there.

Create a MeshInstance3D node in the scene, and for its Mesh property set up a new SphereMesh. Unfold the Material section in the Inspector and then drag the file from the FileSystem dock to the material property. The object will update in the viewport with the blue color of the imported material.

Go to Import dock, enable the "Use Red Anyway" option, and click on "Reimport". This will update the imported material and should automatically update the view showing the red color instead.

And that's it! Your first import plugin is done! Now get creative and make plugins for your own beloved formats. This can be quite useful to write your data in a custom format and then use it in Godot as if they were native resources. This shows how the import system is powerful and extendable.

---

## Inspector plugins

The inspector dock allows you to create custom widgets to edit properties through plugins. This can be beneficial when working with custom datatypes and resources, although you can use the feature to change the inspector widgets for built-in types. You can design custom controls for specific properties, entire objects, and even separate controls associated with particular datatypes.

This guide explains how to use the [EditorInspectorPlugin](../godot_csharp_editor.md) and [EditorProperty](../godot_csharp_editor.md) classes to create a custom interface for integers, replacing the default behavior with a button that generates random values between 0 and 99.

### Setting up your plugin

Create a new empty plugin to get started.

> **See also:** See Making plugins guide to set up your new plugin.

Let's assume you've called your plugin folder `my_inspector_plugin`. If so, you should end up with a new `addons/my_inspector_plugin` folder that contains two files: `plugin.cfg` and `plugin.gd`.

As before, `plugin.gd` is a script extending [EditorPlugin](../godot_csharp_editor.md) and you need to introduce new code for its `_enter_tree` and `_exit_tree` methods. To set up your inspector plugin, you must load its script, then create and add the instance by calling `add_inspector_plugin()`. If the plugin is disabled, you should remove the instance you have added by calling `remove_inspector_plugin()`.

> **Note:** Here, you are loading a script and not a packed scene. Therefore you should use `new()` instead of `instantiate()`.

```csharp
// Plugin.cs
#if TOOLS
using Godot;

[Tool]
public partial class Plugin : EditorPlugin
{
    private MyInspectorPlugin _plugin;

    public override void _EnterTree()
    {
        _plugin = new MyInspectorPlugin();
        AddInspectorPlugin(_plugin);
    }

    public override void _ExitTree()
    {
        RemoveInspectorPlugin(_plugin);
    }
}
#endif
```

### Interacting with the inspector

To interact with the inspector dock, your `my_inspector_plugin.gd` script must extend the [EditorInspectorPlugin](../godot_csharp_editor.md) class. This class provides several virtual methods that affect how the inspector handles properties.

To have any effect at all, the script must implement the `_can_handle()` method. This function is called for each edited [Object](../godot_csharp_core.md) and must return `true` if this plugin should handle the object or its properties.

> **Note:** This includes any [Resource](../godot_csharp_core.md) attached to the object.

You can implement four other methods to add controls to the inspector at specific positions. The `_parse_begin()` and `_parse_end()` methods are called only once at the beginning and the end of parsing for each object, respectively. They can add controls at the top or bottom of the inspector layout by calling `add_custom_control()`.

As the editor parses the object, it calls the `_parse_category()` and `_parse_property()` methods. There, in addition to `add_custom_control()`, you can call both `add_property_editor()` and `add_property_editor_for_multiple_properties()`. Use these last two methods to specifically add [EditorProperty](../godot_csharp_editor.md)-based controls.

```csharp
// MyInspectorPlugin.cs
#if TOOLS
using Godot;

public partial class MyInspectorPlugin : EditorInspectorPlugin
{
    public override bool _CanHandle(GodotObject @object)
    {
        // We support all objects in this example.
        return true;
    }

    public override bool _ParseProperty(GodotObject @object, Variant.Type type,
        string name, PropertyHint hintType, string hintString,
        PropertyUsageFlags usageFlags, bool wide)
    {
        // We handle properties of type integer.
        if (type == Variant.Type.Int)
        {
            // Create an instance of the custom property editor and register
            // it to a specific property path.
            AddPropertyEditor(name, new RandomIntEditor());
            // Inform the editor to remove the default property e
// ...
```

### Adding an interface to edit properties

The [EditorProperty](../godot_csharp_editor.md) class is a special type of [Control](../godot_csharp_ui_controls.md) that can interact with the inspector dock's edited objects. It doesn't display anything but can house any other control nodes, including complex scenes.

There are three essential parts to the script extending [EditorProperty](../godot_csharp_editor.md):

1. You must define the `_init()` method to set up the control nodes' structure.
2. You should implement the `_update_property()` to handle changes to the data from the outside.
3. A signal must be emitted at some point to inform the inspector that the control has changed the property using `emit_changed`.

You can display your custom widget in two ways. Use just the default `add_child()` method to display it to the right of the property name, and use `add_child()` followed by `set_bottom_editor()` to position it below the name.

```csharp
// RandomIntEditor.cs
#if TOOLS
using Godot;

public partial class RandomIntEditor : EditorProperty
{
    // The main control for editing the property.
    private Button _propertyControl = new Button();
    // An internal value of the property.
    private int _currentValue = 0;
    // A guard against internal changes when the property is updated.
    private bool _updating = false;

    public RandomIntEditor()
    {
        // Add the control as a direct child of EditorProperty node.
        AddChild(_propertyControl);
        // Make sure the control is able to retain the focus.
        AddFocusable(_propertyControl);
        // Setup the initial state and connect to the signal to track changes.
        RefreshControlText();
        _propertyControl.Pressed += OnButtonPressed;
    }


// ...
```

Using the example code above you should be able to make a custom widget that replaces the default [SpinBox](../godot_csharp_ui_controls.md) control for integers with a [Button](../godot_csharp_ui_controls.md) that generates random values.

---

## Installing plugins

Godot features an editor plugin system with numerous plugins developed by the community. Plugins can extend the editor's functionality with new nodes, additional docks, convenience features, and more.

### Finding plugins

The preferred way to find Godot plugins is to use the [Asset Library](https://godotengine.org/asset-library/). While it can be browsed online, it's more convenient to use it directly from the editor. To do so, click the **AssetLib** tab at the top of the editor:

You can also find assets on code hosting websites such as GitHub.

> **Note:** Some repositories describe themselves as "plugins" but may not actually be _editor_ plugins. This is especially the case for scripts that are intended to be used in a running project. You don't need to enable such plugins to use them. Download them and extract the files in your project folder. One way to distinguish editor plugins from non-editor plugins is to look for a `plugin.cfg` file in the repository that hosts the plugin. If the repository contains a `plugin.cfg` file in a folder placed in the `addons/` folder, then it is an editor plugin.

### Installing a plugin

To install a plugin, download it as a ZIP archive. On the Asset Library, this can be done using the **Download** button, either from the editor or using the Web interface.

On GitHub, if a plugin has _tags_ (versions) declared, go to the **Releases** tab to download a stable release. This ensures you download a version that was declared to be stable by its author.

On GitHub, if the plugin doesn't have any _tags_ declared, use the **Download ZIP** button to download a ZIP of the latest revision:

Extract the ZIP archive and move the `addons/` folder it contains into your project folder. If your project already contains an `addons/` folder, move the plugin's `addons/` folder into your project folder to merge the new folder contents with the existing one. Your file manager may ask you whether to write into the folder; answer **Yes**. No files will be overwritten in the process.

### Enabling a plugin

To enable the freshly installed plugin, open **Project > Project Settings** at the top of the editor then go the **Plugins** tab. If the plugin was packaged correctly, you should see it in the list of plugins. Click on the **Enable** checkbox to enable the plugin.

You can use the plugin immediately after enabling it; there's no need to restart the editor. Likewise, disabling a plugin can be done without having to restart the editor.

---

## Making main screen plugins

### What this tutorial covers

Main screen plugins allow you to create new UIs in the central part of the editor, which appear next to the "2D", "3D", "Script", "Game", and "AssetLib" buttons. Such editor plugins are referred as "Main screen plugins".

This tutorial leads you through the creation of a basic main screen plugin. For the sake of simplicity, our main screen plugin will contain a single button that prints text to the console.

### Initializing the plugin

First create a new plugin from the Plugins menu. For this tutorial, we'll put it in a folder called `main_screen`, but you can use any name you'd like.

The plugin script will come with `_enter_tree()` and `_exit_tree()` methods, but for a main screen plugin we need to add a few extra methods. Add five extra methods such that the script looks like this:

```csharp
#if TOOLS
using Godot;

[Tool]
public partial class MainScreenPlugin : EditorPlugin
{
    public override void _EnterTree()
    {

    }

    public override void _ExitTree()
    {

    }

    public override bool _HasMainScreen()
    {
        return true;
    }

    public override void _MakeVisible(bool visible)
    {

    }

    public override string _GetPluginName()
    {
        return "Main Screen Plugin";
    }

    public override Texture2D _GetPluginIcon()
    {
        return EditorInterface.Singleton.GetEditorTheme().GetIcon("Node", "EditorIcons");
    }
}
#endif
```

The important part in this script is the `_has_main_screen()` function, which is overloaded so it returns `true`. This function is automatically called by the editor on plugin activation, to tell it that this plugin adds a new center view to the editor. For now, we'll leave this script as-is and we'll come back to it later.

### Main screen scene

Create a new scene with a root node derived from `Control` (for this example plugin, we'll make the root node a `CenterContainer`). Select this root node, and in the viewport, click the `Layout` menu and select `Full Rect`. You also need to enable the `Expand` vertical size flag in the inspector. The panel now uses all the space available in the main viewport.

Next, let's add a button to our example main screen plugin. Add a `Button` node, and set the text to "Print Hello" or similar. Add a script to the button like this:

```csharp
using Godot;

[Tool]
public partial class PrintHello : Button
{
    private void OnPrintHelloPressed()
    {
        GD.Print("Hello from the main screen plugin!");
    }
}
```

Then connect the "pressed" signal to itself. If you need help with signals, see the Using signals (see Getting Started docs) article.

We are done with the main screen panel. Save the scene as `main_panel.tscn`.

### Update the plugin script

We need to update the `main_screen_plugin.gd` script so the plugin instances our main panel scene and places it where it needs to be. Here is the full plugin script:

```csharp
#if TOOLS
using Godot;

[Tool]
public partial class MainScreenPlugin : EditorPlugin
{
    PackedScene MainPanel = ResourceLoader.Load<PackedScene>("res://addons/main_screen/main_panel.tscn");
    Control MainPanelInstance;

    public override void _EnterTree()
    {
        MainPanelInstance = (Control)MainPanel.Instantiate();
        // Add the main panel to the editor's main viewport.
        EditorInterface.Singleton.GetEditorMainScreen().AddChild(MainPanelInstance);
        // Hide the main panel. Very much required.
        _MakeVisible(false);
    }

    public override void _ExitTree()
    {
        if (MainPanelInstance != null)
        {
            MainPanelInstance.QueueFree();
        }
    }

    public override bool _HasMainScreen()
    {
        return true;
    }

    publ
// ...
```

A couple of specific lines were added. `MainPanel` is a constant that holds a reference to the scene, and we instance it into main_panel_instance.

The `_enter_tree()` function is called before `_ready()`. This is where we instance the main panel scene, and add them as children of specific parts of the editor. We use `EditorInterface.get_editor_main_screen()` to obtain the main editor screen and add our main panel instance as a child to it. We call the `_make_visible(false)` function to hide the main panel so it doesn't compete for space when first activating the plugin.

The `_exit_tree()` function is called when the plugin is deactivated. If the main screen still exists, we call `queue_free()` to free the instance and remove it from memory.

The `_make_visible()` function is overridden to hide or show the main panel as needed. This function is automatically called by the editor when the user clicks on the main viewport buttons at the top of the editor.

The `_get_plugin_name()` and `_get_plugin_icon()` functions control the displayed name and icon for the plugin's main viewport button.

Another function you can add is the `handles()` function, which allows you to handle a node type, automatically focusing the main screen when the type is selected. This is similar to how clicking on a 3D node will automatically switch to the 3D viewport.

### Try the plugin

Activate the plugin in the Project Settings. You'll observe a new button next to 2D, 3D, Script above the main viewport. Clicking it will take you to your new main screen plugin, and the button in the middle will print text.

If you would like to try a finished version of this plugin, check out the plugin demos here: [https://github.com/godotengine/godot-demo-projects/tree/master/plugins](https://github.com/godotengine/godot-demo-projects/tree/master/plugins)

If you would like to see a more complete example of what main screen plugins are capable of, check out the 2.5D demo projects here: [https://github.com/godotengine/godot-demo-projects/tree/master/misc/2.5d](https://github.com/godotengine/godot-demo-projects/tree/master/misc/2.5d)

---

## Making plugins

### About plugins

A plugin is a great way to extend the editor with useful tools. It can be made entirely with GDScript and standard scenes, without even reloading the editor. Unlike modules, you don't need to create C++ code nor recompile the engine. While this makes plugins less powerful, there are still many things you can do with them. Note that a plugin is similar to any scene you can already make, except it is created using a script to add editor functionality.

This tutorial will guide you through the creation of two plugins so you can understand how they work and be able to develop your own. The first is a custom node that you can add to any scene in the project, and the other is a custom dock added to the editor.

### Creating a plugin

Before starting, create a new empty project wherever you want. This will serve as a base to develop and test the plugins.

The first thing you need for the editor to identify a new plugin is to create two files: a `plugin.cfg` for configuration and a tool script with the functionality. Plugins have a standard path like `addons/plugin_name` inside the project folder. Godot provides a dialog for generating those files and placing them where they need to be.

In the main toolbar, click the `Project` dropdown. Then click `Project Settings...`. Go to the `Plugins` tab and then click on the Create New Plugin button in the top-right.

You will see the dialog appear, like so:

The placeholder text in each field describes how it affects the plugin's creation of the files and the config file's values.

To continue with the example, use the following values:

```csharp
Plugin Name: My Custom Node
Subfolder: MyCustomNode
Description: A custom node made to extend the Godot Engine.
Author: Your Name Here
Version: 1.0.0
Language: C#
Script Name: CustomNode.cs
```

> **Warning:** In C#, the EditorPlugin script needs to be compiled, which requires building the project. After building the project the plugin can be enabled in the `Plugins` tab of `Project Settings`.

You should end up with a directory structure like this:

`plugin.cfg` is an INI file with metadata about your plugin. The name and description help people understand what it does. Your name helps you get properly credited for your work. The version number helps others know if they have an outdated version; if you are unsure on how to come up with the version number, check out [Semantic Versioning](https://semver.org/). The main script file will instruct Godot what your plugin does in the editor once it is active.

#### The script file

Upon creation of the plugin, the dialog will automatically open the EditorPlugin script for you. The script has two requirements that you cannot change: it must be a `@tool` script, or else it will not load properly in the editor, and it must inherit from [EditorPlugin](../godot_csharp_editor.md).

> **Warning:** In addition to the EditorPlugin script, any other GDScript that your plugin uses must _also_ be a tool. Any GDScript without `@tool` used by the editor will act like an empty file!

It's important to deal with initialization and clean-up of resources. A good practice is to use the virtual function [\_enter_tree()](../godot_csharp_misc.md) to initialize your plugin and [\_exit_tree()](../godot_csharp_misc.md) to clean it up. Thankfully, the dialog generates these callbacks for you. Your script should look something like this:

```csharp
#if TOOLS
using Godot;

[Tool]
public partial class CustomNode : EditorPlugin
{
    public override void _EnterTree()
    {
        // Initialization of the plugin goes here.
    }

    public override void _ExitTree()
    {
        // Clean-up of the plugin goes here.
    }
}
#endif
```

This is a good template to use when creating new plugins.

### A custom node

Sometimes you want a certain behavior in many nodes, such as a custom scene or control that can be reused. Instancing is helpful in a lot of cases, but sometimes it can be cumbersome, especially if you're using it in many projects. A good solution to this is to make a plugin that adds a node with a custom behavior.

For this tutorial, we'll create a button that prints a message when clicked. For that, we'll need a script that extends from [Button](../godot_csharp_ui_controls.md). It could also extend [BaseButton](../godot_csharp_ui_controls.md) if you prefer:

```csharp
using Godot;

// Optional, add to execute in the editor.
[Tool]

// Icons are optional.
// Alternatively, you may use the UID of the icon or the absolute path.
[Icon("icon.png")]

// Automatically register the node in the Create New Node dialog
// and make it available for use with other scripts.
[GlobalClass]
public partial class MyButton : Button
{
    public override void _EnterTree()
    {
        Pressed += Clicked;
    }

    public void Clicked()
    {
        GD.Print("You clicked me!");
    }
}
```

That's it for our basic button. You can save this as `my_button.gd` inside the plugin folder. You may have a 16×16 icon to show in the scene tree. If you don't have one, you can grab the default one from the engine and save it in your addons/my_custom_node folder as icon.png, or use the default Godot logo (preload("res://icon.svg")).

> **Tip:** SVG images that are used as custom node icons should have the **Editor > Scale With Editor Scale** and **Editor > Convert Colors With Editor Theme** [import options](tutorials_assets_pipeline.md) enabled. This allows icons to follow the editor's scale and theming settings if the icons are designed with the same color palette as Godot's own icons.

With that done, the plugin should already be available in the plugin list in the **Project Settings**, so activate it as explained in **Checking the results**.

Then try it out by adding your new node:

When you add the node, you can see that it already has the script you created attached to it. Set a text to the button, save and run the scene. When you click the button, you can see some text in the console:

### A custom dock

Sometimes, you need to extend the editor and add tools that are always available. An easy way to do it is to add a new dock with a plugin. Docks are just scenes based on Control, so they are created in a way similar to usual GUI scenes.

Creating a custom dock is done just like a custom node. Create a new `plugin.cfg` file in the `addons/my_custom_dock` folder, then add the following content to it:

```csharp
[plugin]

name="My Custom Dock"
description="A custom dock made so I can learn how to make plugins."
author="Your Name Here"
version="1.0"
script="CustomDock.cs"
```

Then create the script `custom_dock.gd` in the same folder. Fill it with the **template we've seen before** to get a good start.

Since we're trying to add a new custom dock, we need to create the contents of the dock. This is nothing more than a standard Godot scene: just create a new scene in the editor then edit it.

For an editor dock, the root node **must** be a [Control](../godot_csharp_ui_controls.md) or one of its child classes. For this tutorial, you can create a single button. Don't forget to add some text to your button.

Save this scene as `my_dock.tscn`. Now, we need to grab the scene we created then add it as a dock in the editor. For this, you can rely on the function [add_dock()](../godot_csharp_misc.md) from the [EditorPlugin](../godot_csharp_editor.md) class.

You need to select a dock position and define the control to add (which is the scene you just created). Don't forget to **remove the dock** when the plugin is deactivated. The script could look like this:

```csharp
#if TOOLS
using Godot;

[Tool]
public partial class CustomDock : EditorPlugin
{
    private EditorDock _dock;

    public override void _EnterTree()
    {
        var _dock_scene = GD.Load<PackedScene>("res://addons/MyCustomDock/MyDock.tscn").Instantiate<Control>();

        // Create the dock and add the loaded scene to it.
        _dock = new EditorDock();
        _dock.AddChild(dock_scene);

        _dock.Title = "My Dock";

        // Note that LeftUl means the left of the editor, upper-left dock.
        _dock.DefaultSlot = DockSlot.LeftUl;

        // Allow the dock to be on the left or right of the editor, and to be made floating.
        _dock.AvailableLayouts = DockLayout.Horizontal | DockLayout.Floating;

        AddDock(_dock);
    }

    public override void _ExitTree()
    {

// ...
```

Note that, while the dock will initially appear at its specified position, the user can freely change its position and save the resulting layout.

#### Checking the results

It's now time to check the results of your work. Open the **Project Settings** and click on the **Plugins** tab. Your plugin should be the only one on the list.

You can see the plugin is not enabled. Click the **Enable** checkbox to activate the plugin. The dock should become visible before you even close the settings window. You should now have a custom dock:

### Registering autoloads/singletons in plugins

It is possible for editor plugins to automatically register [autoloads](tutorials_scripting.md) when the plugin is enabled. This also includes unregistering the autoload when the plugin is disabled.

This makes setting up plugins faster for users, as they no longer have to manually add autoloads to their project settings if your editor plugin requires the use of an autoload.

Use the following code to register a singleton from an editor plugin:

```csharp
#if TOOLS
using Godot;

[Tool]
public partial class MyEditorPlugin : EditorPlugin
{
    // Replace this value with a PascalCase autoload name.
    private const string AutoloadName = "SomeAutoload";

    public override void _EnablePlugin()
    {
        // The autoload can be a scene or script file.
        AddAutoloadSingleton(AutoloadName, "res://addons/MyAddon/SomeAutoload.tscn");
    }

    public override void _DisablePlugin()
    {
        RemoveAutoloadSingleton(AutoloadName);
    }
}
#endif
```

### Using sub-plugins

Often a plugin adds multiple things, for example a custom node and a panel. In those cases it might be easier to have a separate plugin script for each of those features. Sub-plugins can be used for this.

First create all plugins and sub plugins as normal plugins:

Then move the sub plugins into the main plugin folder:

Godot will hide sub-plugins from the plugin list, so that a user can't enable or disable them. Instead the main plugin script should enable and disable sub-plugins like this:

### Going beyond

Now that you've learned how to make basic plugins, you can extend the editor in several ways. Lots of functionality can be added to the editor with GDScript; it is a powerful way to create specialized editors without having to delve into C++ modules.

You can make your own plugins to help yourself and share them in the [Asset Library](https://godotengine.org/asset-library/) so that people can benefit from your work.

---

## Visual Shader plugins

Visual Shader plugins are used to create custom [VisualShader](../godot_csharp_rendering.md) nodes in GDScript.

The creation process is different from usual editor plugins. You do not need to create a `plugin.cfg` file to register it; instead, create and save a script file and it will be ready to use, provided the custom node is registered with `class_name`.

This short tutorial will explain how to make a Perlin-3D noise node (original code from this [GPU noise shaders plugin](https://github.com/curly-brace/Godot-3.0-Noise-Shaders/blob/master/assets/gpu_noise_shaders/classic_perlin3d.tres).

Create a Sprite2D and assign a [ShaderMaterial](../godot_csharp_rendering.md) to its material slot:

Assign [VisualShader](../godot_csharp_rendering.md) to the shader slot of the material:

Don't forget to change its mode to "CanvasItem" (if you are using a Sprite2D):

Create a script which derives from [VisualShaderNodeCustom](../godot_csharp_rendering.md). This is all you need to initialize your plugin.

Save it and open the Visual Shader. You should see your new node type within the member's dialog under the Addons category (if you can't see your new node, try restarting the editor):

Place it on a graph and connect the required ports:

That is everything you need to do, as you can see it is easy to create your own custom VisualShader nodes!

---
