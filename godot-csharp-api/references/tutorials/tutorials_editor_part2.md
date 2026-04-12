# Godot 4 C# Tutorials — Editor (Part 2)

> 8 tutorials. C#-specific code examples.

## Inspector Dock

The Inspector dock lists all properties of an object, resource, or node. It will update the list of the properties as you select a different node from the Scene Tree dock, or if you use **Open** command from the FileSystem's context menu.

This page explains how the Inspector dock works in-depth. You will learn how to edit properties, fold and unfold areas, use the search bar, and more.

### Usage

If the inspector dock is visible, clicking on a node in the scene tree will automatically display its properties. If it is not visible, you can show it by navigating to **Editor > Editor Docks > Inspector**.

At the top of the dock are the file and navigation buttons.

From left to right:

- Opens a new window to select and create a resource in the memory and edit it.
- Opens a resource from the FileSystem to edit.
- Saves the currently edited resource to disk.
- Provides options to:

- **Edit Resource from Clipboard** by pasting the copied resource.
- **Copy Resource** to clipboard.
- **Show in FileSystem** if the resource is already saved.
- **Make Resource Built-In** to work in a built-in resource, not the one from the disk.
- The "<" and ">" arrows let you navigate through your edited object history.
- The button next to them opens the history list for a quicker navigation. If you created multiple resources in the memory, you will also see them here.

Below, you can find the selected node's icon, its name, and the quick button to open its documentation on the right side. Clicking on the node's name itself will list the sub-resources of this node if there are any.

Then comes the search bar. Type anything in it to filter displayed properties. Delete the text to clear the search. This search is case insensitive and also searches letter by letter as you type. For instance, if you type `vsb`, one of the results you see will be Visibility property as this property contains all of these letters.

Before discussing the tool button next to the filter bar, it is worth mentioning what you actually see below it and how it is structured.

Properties are grouped inside their respective _classes_ as _sections_. You can expand each section to view the related properties.

You can also open the documentation of each class by right-clicking on a class and selecting **Open Documentation**. Similarly, you can right click on a property and copy or paste its value, copy the property path, favorite it to be shown on the top of the inspector, or open its documentation page.

If you hover your mouse over a property, you will see the description of what it does as well as how it can be called inside the script.

You can directly change the values by clicking, typing, or selecting from the menu. If the property is a number or a slider, you can keep your left mouse button pressed and drag to change the values.

If a node's property is a sub-resource, you can click on the down arrow to pick a resource type, or load one using the **Quick Load** or **Load** options. Alternatively, a supported resource can be dragged from the FileSystem. Once you start dragging, the compatible property will be highlighted. Simply drop it on the appropriate property's value.

After loading a sub-resource, you can click on it to see its properties or adjust them.

The values with different values than their original values will have a revert icon (). Clicking on this icon reverts the value to its original state. If the values are linked with each other, they will have a chain icon and changing one will change others as well. You can unchain them by clicking on this icon.

If you are changing a property a lot, you may consider favoriting it by right-clicking and choosing **Favorite Property**. This will show it at the top of the inspector for all objects of this class.

Now that we have a better understanding of the terms, we can proceed with the tool menu. If you click the tool menu icon next to the filter bar, a drop-down menu will offer various view and edit options.

- **Expand All**: Expands all sections showing all available properties.
- **Collapse All**: Collapses all properties showing only classes and the sections.
- **Expand Non-Default**: Only expands the sections where the original value is different than the current value (the properties with a revert icon ()).
- **Property Name Style**: This section determines how the properties' text is displayed in the inspector. `Raw` uses the property's own naming, `Capitalized` uses title case by changing the initial letters of each word to uppercase and removing underscores, `Localized` displays the translation of the properties if you are using the Editor in a language other than English.
- **Copy Properties**: Copies all properties of the current node with their current values.
- **Paste Properties**: Pastes the copied properties from the clipboard. Useful to apply the common properties of one node to another.
- **Make Sub-Resources Unique**: By default, a duplicated node shares the sub-resources of the original node. Changing one parameter of the sub-resource in one node, affects the other one. Clicking this option makes each sub-resource used in this node unique, separated from other nodes.

> **Tip:** If a node has exported variables in its attached script, you will also see these in the inspector. The first image in this section has one for the Player node: Action Suffix. See [GDScript exported properties](tutorials_scripting.md) for more on this topic.

> **See also:** Refer to Customizing the interface for dock customization options.

---

## Managing editor features

> **Work in progress:** The content of this page was not yet updated for Godot `4.6` and may be **outdated**. If you know how to improve this page or you can confirm that it's up to date, feel free to [open a pull request](https://github.com/godotengine/godot-docs).

### Introduction

In certain situations, it may be desirable to limit what features can be used in the Godot editor. For example, a UI designer on a team who doesn't need to see 3D features, or an educator slowly introducing features to students. Godot has a built-in system called "feature profiles" to do this.

With feature profiles, major features and nodes can be hidden from the editor. This only hides parts of the interface and does not actually remove support for these features, so scenes and scripts relying on those features will still work fine. This also means feature profiles are not an optimization technique. For information on how to optimize Godot see [Performance](tutorials_performance.md).

### Creating a profile

To manage editor features go to **Editor > Manage Editor Features**. This will open the **Manage Editor Feature Profiles** window. By default there will be no profile. Click on **Create Profile** and give it a name. You will then see a list of all the features in the Godot editor.

The first section allows major editor features to be removed, such as the 3D editor or scripting editor. Below the main features is every class and node in Godot, which can be disabled as well. Click on a node and all of its properties and options will be listed in the **Extra Items** box, these can all be individually disabled.

### Sharing a profile

To share profiles between editors click on the **Export** button. Save the custom profile somewhere as a `.profile` file. To use this in another editor open that editor's **Manage Editor Feature Profiles** window and click import, then select the `.profile` file.

This process is potentially cumbersome however if a large amount of computers need custom profiles. As an alternative, you can enable self-contained mode for Godot, which allows putting all editor configuration in the same folder as the editor binary. See [Self-contained mode](tutorials_io.md) for details.

---

## Using the Project Manager

When you launch Godot, the first window you see is the Project Manager. It lets you create, remove, import, or play game projects:

To change the editors language click on the **Settings** Button in the top right corner:

In Project Manager Settings, you can change the interface **language** from the language dropdown menu, which is the system default language by default.

You can also change the **theme** and **color preset** of the editor, the **display scale** for different interface element sizes, and the availability of online functionality using **network mode**. If network mode is online, Godot will also check and inform you about new versions of Godot.

The **directory naming convention** can also be changed to replace spaces according to the chosen format when creating folders automatically.

### Creating and importing projects

To create a new project:

1. Click the **Create** button on the top-left of the window.
2. Give the project a name, then open the file browser using the **Browse** button, and choose an empty folder on your computer to save the files. Alternatively, you can enable **Create Folder** option to automatically create a new sub-folder with the project name, following the directory naming convention set in the settings. An empty folder will show a green tick on the right.
3. Select one of the renderers (this can also be changed later).
4. Click the Create button to create the project folder and open it in the editor.

> **Note:** You can optionally choose a version control system. Currently, only [git](https://git-scm.com) is supported and it needs the Godot Git Plugin to be installed, either manually or using the Asset Library. To learn more about the Godot Git Plugin, see its [wiki](https://github.com/godotengine/godot-git-plugin/wiki).

#### Using the file browser

From the **Create New Project** window, click the **Browse** button to open Godot's file browser. You can pick a location or type the folder's path in the **Path** field, after choosing a drive.

Left of the path field on the top row contains arrows to navigate backward and forward through the last visited locations. The up arrow navigates to parent folder. On the right side of the path field, there are buttons to refresh the current folder's contents, favorite/unfavorite the current folder, and show/hide hidden folders.

Next, the buttons to switch the display type of the folders and files between grid view and list view are seen.

The last button on the right will create a new folder.

Favorited folders will be displayed on the left side under the **Favorites** section. You can sort the favorites using the up and down buttons in this section. Last chosen folders will be listed under the **Recent** list.

### Opening and importing projects

The next time you open the Project Manager, you'll see your new project in the list. Double click on it to open it in the editor.

You can similarly import existing projects using the **Import** button. Locate the folder that contains the project or the **project.godot** file to import and edit it.

Alternatively, it is possible to choose a zip file to be automatically extracted by Godot.

When the folder path is correct, you'll see a green checkmark.

### Downloading demos and templates

From the **Asset Library** tab you can download open source project templates and demos from the Asset Library to help you get started faster.

The first time you open this tab you'll notice that it's asking you to go online. For privacy reasons the project manager, and Godot editor, can't access the internet by default. To enable accessing the internet click the **Go Online** button. This will also allow project manager to notify you about updates. If you wish to turn this off in the future go into project manager settings and change **Network Mode** to "Offline"

Now that Godot is connected to the internet you can download a demo or template, to do this:

1. Click on its title.
2. On the page that opens, click the download button.
3. Once it finished downloading, click install and choose where you want to save the project.

### Managing projects with tags

For users with a lot of projects on one PC it can be a lot to keep track of. To aid in this Godot allows you to create project tags. To add a tag to a project click on the project in the project manager, then click on the **Manage Tags** button

This will open up the manage project tags window. To add a tag click the plus button.

Type out the tag name, and click **OK**. Your project will now have a tag added to it. These tags can be used for any other project in your project manager.

To show projects with a specific tag only, you can click on the tags or write `tag:` and type the tag you would like to search for in the filter bar. To limit the results using multiple tags, you can click on another tag or add `tag:` after a space and type another tag in the filter bar.

In addition, tags will stay with projects. So if you tag your project, send it to another machine, and import it into the project manager you will see the tags you created.

To remove a tag from your project manager it must be removed from all the projects it's used by. Once that's done close the project manager, open it up again, and the tag should be gone.

### Recovery Mode

If a project is immediately crashing on startup, or crashing frequently during editing it can be opened in recovery mode, to attempt to make it more stable while looking for the source of the crashing to fix it.

Usually a project should open in recovery mode automatically when you re-open it after a crash. If it doesn't you can manually open recovery mode by selecting the project in the project manager, to do that select the project from your list of projects, click the dropdown button next to the edit node, and select `Edit in recovery mode`.

While in recovery mode the following are disabled:

- Tool scripts
- Editor plugins
- GDExtension addons
- Automatic scene restoring
- Running the project

It is recommended that you backup your project before editing it in recovery mode.

---

## Project Settings

There are dozens of settings you can change to control a project's execution, including physics, rendering, and windowing settings. These settings can be changed from the **Project Settings** window, from code, or by manually editing the `project.godot` file. You can see a full list of settings in the [ProjectSettings](../godot_csharp_filesystem.md) class.

Internally, Godot stores the settings for a project in a `project.godot` file, a plain text file in INI format. While this is human-readable and version control friendly, it's not the most convenient to edit. For that reason, the **Project Settings** window is available to edit these settings. To open the Project Settings, select **Project > Project Settings** from the main menu.

The **Project Settings** window is mainly used to change settings in the **General** tab. Additionally, there are tabs for the [Input Map](tutorials_inputs.md), [Localization](tutorials_i18n.md), [Globals](tutorials_scripting.md), [Plugins](tutorials_editor.md), and **Import Defaults**. Usage of these other tabs is documented elsewhere.

### Changing project settings

The **General** tab of the project settings window works much like the inspector. It displays a list of project settings which you can change, just like inspector properties. There is a list of categories on the left, which you can use to select related groups of settings. You can also search for a specific setting with the **Filter Settings** field.

Each setting has a default value. Settings can be reset to their default values by clicking the circular arrow **Reset** button next to each property.

#### Changing project settings from code

You can use [set_setting()](../godot_csharp_misc.md) to change a setting's value from code:

```csharp
ProjectSettings.SetSetting("application/run/max_fps", 60);
ProjectSettings.SetSetting("display/window/size/mode", (int)DisplayServer.WindowMode.Windowed);
```

However, many project settings are only read once when the game starts. After that, changing the setting with `set_setting()` will have no effect. Instead, most settings have a corresponding property or method on a runtime class like [Engine](../godot_csharp_core.md) or [DisplayServer](../godot_csharp_misc.md):

```csharp
Engine.MaxFps = 60;
DisplayServer.WindowSetMode(DisplayServer.WindowMode.Windowed);
```

In general, project settings are duplicated at runtime in the [Engine](../godot_csharp_core.md), [PhysicsServer2D](../godot_csharp_physics.md), [PhysicsServer3D](../godot_csharp_physics.md), [RenderingServer](../godot_csharp_rendering.md), [Viewport](../godot_csharp_rendering.md), or [Window](../godot_csharp_ui_controls.md) classes. In the [ProjectSettings](../godot_csharp_filesystem.md) class reference, settings links to their equivalent runtime property or method.

### Reading project settings

You can read project settings with [get_setting()](../godot_csharp_misc.md) or [get_setting_with_override()](../godot_csharp_misc.md):

```csharp
int maxFps = (int)ProjectSettings.GetSetting("application/run/max_fps");
var windowMode = (DisplayServer.WindowMode)(int)ProjectSettings.GetSetting("display/window/size/mode");
```

Since many project settings are only read once at startup, the value in the project settings may no longer be accurate. In these cases, it's better to read the value from the runtime equivalent property or method:

```csharp
int maxFps = Engine.MaxFps;
DisplayServer.WindowMode windowMode = DisplayServer.WindowGetMode();
```

### Manually editing project.godot

You can open the `project.godot` file using a text editor and manually change project settings. Note that if the `project.godot` file does not have a stored value for a particular setting, it is implicitly the default value of that setting. This means that if you are manually editing the file, you may have to write in both the setting name _and_ the value.

In general, it is recommended to use the Project Settings window rather than manually edit `project.godot`.

### Advanced project settings

By default, only some project settings are shown. To see all the project settings, enable the **Advanced Settings** toggle.

---

## Script Editor

### Introduction

Godot Engine's script editor is a powerful and fully-integrated text editor that not only streamlines the process of writing and debugging code written in GDScript but also allows for working with plain text files, providing developers with a seamless environment for scripting game logic and behaviors. It can highlight your code, automatically indent it, perform syntax checks, and much more. You can also create breakpoints to debug your project without switching to another window. The text editor also serves as an offline class reference viewer, which can be accessed in several ways as described in the Integrated class reference (see Getting Started docs).

### Features

Some of the key features of the text editor are listed below:

- Fully-integrated code editor for GDScript.
- Syntax highlighting support for GDScript and JSON files.
- Syntax checking for GDScript and JSON files.
- Bookmark and breakpoint support.
- Automatic indentation.
- Code folding.
- Customizable theme.
- Multiple carets, which can be enabled using Alt + Left Click.
- Auto-completion of variables, functions, constants, etc.
- Inline refactoring of symbols by selecting them and using Ctrl + D.
- Mass find and replace across project files.

### Usage

If you are using GDScript in your project, the built-in text editor in Godot provides everything you need, serving as a one-stop location to fully utilize the Godot Engine. Nearly all parameters that can be adjusted via the user interface can also be modified directly through code.

> **Note:** If you would like to use an external text editor or prefer to use C# in your project, see Using an external text editor and [Configuring an external editor](tutorials_scripting.md).

> **Tip:** Similar to many parts of the Godot's interface, the text editor can also be customized by changing its settings to your liking. You can access these settings by opening **Editor > Editor Settings** and going to the **Text Editor** group.

You can open the Script Editor using the **Script** button in the workspace selector, located at the top center of Godot's interface. Alternatively, you can use the **Open Script** button next to a node in the Scene Tree dock, or double-click on a `.gd` file or a recognized text file in the FileSystem dock to open it directly in the Script Editor.

Once it is open, you will see the text editor menus at the top, below the scene switcher. Next to the menus, you'll find buttons to open the online documentation or search within the built-in class reference. To the right of these buttons are two navigation arrows that allow you to navigate through your viewing history. Finally, you can use the float button to separate the text editor from Godot's window, which is useful if you are working with multiple monitors.

Underneath the menus on the left, you will see the script panel. In the center, adjacent to the script panel, is the coding area. Beneath the coding area is the status bar, which displays the error and warning count in the code. Clicking on the error or warning icons will show the list of errors with the line numbers. Clicking on one will jump to that line. You can also choose to ignore warnings by opening the list and clicking `Ignore`. The status bar also lets you change the zoom level of the code by clicking the percentage value. You can also use Ctrl + Mouse Wheel (Cmd + Mouse Wheel on Mac) to achieve the same effect. The status bar also shows the current position of the caret in terms of line and column, and whether the indentation is done using tabs, or spaces.

Many of the actions performed in the text editor can also be executed using shortcuts. The actions show their corresponding shortcuts next to them. For a complete shortcut list, see the text editor shortcuts.

In the next sections, we will go through different aspects of the text editor. You can also select a section below to jump to a specific topic:

#### Script Panel

Below the menus, on the left panel, you will see a list of opened files and documentation pages. Depending on the file type, this list will have an icon next to the file name. For example, the icon means that it is a GDScript. the means it is a C# script. The means that this is a built-in class reference. Finally, the means it is a currently running script (See [tool annotation](tutorials_plugins.md) for more on this). Hovering a file will show a tooltip with its relative location in the project folder.

On the status bar, clicking the left arrow hides the script panel, clicking on the right arrow shows it.

If you did not change any settings, the file names may also have a different coloring. This helps you identify the recently edited files by highlighting them. This behavior can be changed in the **Editor > Editor Settings** by adjusting the **Script Temperature** properties in the **Text Editor** section.

The filter bar above the file names introduces a handy case-insensitive search to find a specific file. Even if you just type the letters of a file name into the bar, files containing these letters in order will also appear. Assume that there is a file named `button.gd` in the list. If you type `btn` into the filter bar, this file will appear in the results. To reset the filter, clear the filter bar.

An asterisk (\*) next to a file name indicates that the file has unsaved changes.

> **Tip:** If you just enter "\*" in the filter bar, you can display all unsaved files.

You can drag a file to change the ordering. Middle-clicking on a file closes it. Right-clicking on a file provides several options to save or close files, or to copy the relative path of the file. On this menu:

You can also use **Move Up** and **Move Down** to change the order of the file, or use **Sort** to sort all files alphabetically. **Toggle Scripts Panel** hides the panel, which can be displayed again using the right arrow on the status bar. **Close Docs** closes all opened in-class reference documents leaving only script files open. **Show in FileSystem** finds and highlights the file in the FileSystem dock.

Below the file list, you'll see the name of the currently open file. The button next to this switches the ordering of the methods defined in this file between alphabetical and as they appear. Under this is the outline of the file. If this is a script file, it will contain the list of defined methods. If, however, a class reference page is open, this area will show the table of contents of this document. Clicking on an item in this list will jump to the respective function or section in the file. Similarly, the **Filter Methods** bar lets you search for a specific function or section within the selected document with the same behavior as filtering scripts.

#### Menus

The text editor's menus lie below the scene switcher and allow you to access a variety of tools and options, such as file management, search and replace, debugging controls, and code formatting features.

> **Tip:** An asterisk (\*) next to an action means that this operation is also available in the context menu, which can be opened by right-clicking in the code editor.

The **File** menu provides the following options:

- **New Script...**: Opens the new script dialog to create and add the script to the project. If creation is successful, it will directly open it in the text editor. Depending on the version of Godot (with C# support or not), you can choose `.gd` or `.cs` as the extension.
- **New Text File...**: Opens the file dialog to create a plain text file with one of the recognized formats. Godot can also highlight `json` files.
- **Open...**: Opens the file dialog to let you browse inside your computer and choose any recognized text file to open it.
- **Reopen Closed Script**: Reopens the last closed scripts. You can use this option multiple times to reopen other closed scripts if you closed more than one.
- **Open Recent**: Provides a list of last opened scripts. You can also clear the list using the provided option at the bottom of the list.
- **Save**: Saves the currently selected script.
- **Save As...**: Opens the file dialog to save the currently open script with a different name.
- **Save All**: Saves all unsaved open scripts in the text editor. Scripts with unsaved changes will have an asterisk (\*) next to their names in the script list.
- **Soft Reload Tool Script**: If the selected script is a [tool](tutorials_plugins.md), reloads the script to execute it again.
- **Copy Script Path**: Copies the currently selected script's relative path in the project using the `res://` prefix.
- **Show in FileSystem**: Finds and highlights the selected file in the FileSystem dock.
- **History Previous**: Changes the active script to the one that was previously opened. This is useful when you have multiple scripts open and want to quickly navigate back to the last script you were editing. If you also changed the caret position more than 10 lines, you will first move it to its previous location in the same file.
- **History Next**: After using History Previous to go back to an earlier script, this feature allows you to move forward through the script history, switching to scripts that were previously accessed. Similar to above, if you also changed the caret position more than 10 lines, you will first move it to its next location in the same file.
- **Theme**: Provides options to import an existing theme, save, or reload it. Changing theme settings is performed via Editor Settings.
- **Close**: Closes the active script.
- **Close All**: Closes all open scripts and prompts to save if there are unsaved changes.
- **Close Other Tabs**: Closes all open scripts except the selected one.
- **Close Docs**: Closes the class reference documentation pages, leaving only the scripts.
- **Run**: If the script extends [EditorScript](../godot_csharp_editor.md) and intended to be executed without running the project, this option runs the script. See [Running one-off scripts using EditorScript](tutorials_plugins.md) for more.
- **Toggle Scripts Panel**: Shows or hides the script panel located on the left side of the text editor, allowing you to expand the available coding area. More on the Scripts Panel is explained **above**.

The **Edit** menu provides several options for line operations:

- **Undo\***: Allows you to reverse the most recent action or series of actions, restoring document or code to its previous state before the changes were made.
- **Redo\***: Allows you to reapply an action that was previously undone, effectively redoing the last action that was reversed by the Undo function.
- **Cut\***: Cuts the selection to the clipboard.
- **Copy\***: Copies the selection to the clipboard.
- **Paste\***: Pastes the content of the clipboard if it contains text.
- **Select All\***: Selects the all code in the text editor.
- **Duplicate Selection**: Copies the selection and appends it next to the selection.
- **Duplicate Lines**: Duplicates the current line and adds it as a new line below the current line.
- **Evaluate Selection\***: Computes the values of the selected text if it contains only a mathematical expression, such as `83 * 3` or `pow(2,3)`.
- **Toggle Word Wrap**: Disables the horizontal scrollbar by wrapping the long lines to the next line. Note that this is just a visual change and no new linebreaks are added.
- **Line**: Provides a set of line operations. Depending on the opened file, the options might also be directly in the Edit menu, instead of a submenu.

- **Move Up**: Moves the current line or the selected line(s) one line up.
- **Move Down**: Moves the current line or the selected line(s) one line down.
- **Indent\***: Indents the text from the caret or the selected line(s), following the indentation setting.
- **Unindent\***: Unindents the text from the caret or the selected line(s), following the indentation setting.
- **Delete Line**: Deletes the current line or the selected line(s).
- **Toggle Comment\***: Comments and uncomments the current line or the selected line(s). You can perform the same action by selecting line(s) and choosing the same action after right-clicking on the selected text.
- **Folding**: Provides a set of folding options for the selected text. Depending on the opened file, the options might also be directly in the Edit menu, instead of a submenu.

- **Fold/Unfold Line\***: If the code in the current line has a code block or code region beneath it, it hides this block by collapsing the lines. You can then unfold it using this option again, using the ">" arrow next to the line number in the coding area, or clicking on the ellipsis "..." icon at the end of the folded line.
- **Fold All Lines**: Folds all code blocks or code regions in the open document.
- **Unfold All Lines**: Unfolds all code blocks and code regions in the open document.
- **Create Code Region\***: Wraps the selected text in a foldable code region to improve the readability of larger scripts. See [Built-in types](tutorials_scripting.md) for more.
- **Completion Query**: Suggests from built-in or user created symbols to auto-complete the partially written code. Up and Down arrows navigate up and down, pressing Enter or Tab accepts and adds the highlighted symbol to the code. Tab will also replace existing text to the right of the caret.
- **Trim Trailing Whitespaces**: Removes extra spacing at the end of each line in the file.
- **Trim Final Newlines**: Removes the extra new lines at the end of the file.
- **Indentation**: Provides options for the indentation of the open file. Depending on the opened file, the options might also be directly in the Edit menu, instead of a submenu.

- **Convert Indent to Spaces**: Converts all indentation in the file to spaces.
- **Convert Indent to Tabs**: Converts all indentation in the file to tabs.
- **Auto Indent**: Converts the indentation of the selected lines (or the entire file) following the indentation setting.
- **Convert Case**: Changes the case of the selected text to Upper Case*, Lower Case*, or capitalizes each initial letter of the words.
- **Syntax Highlighter**: Allows you to choose the syntax highlighter.

- **Plain Text**: Disables highlighting.
- **Standard**: Default highlighting for C# scripts.
- **JSON**: Syntax highlighting for JSON files.
- **GDScript**: Syntax highlighting for GDScript files.

The **Search** menu provides the following options:

- **Find...**: Opens the quick-find bar under the status bar to search for text in the open file. You can navigate to the next match and previous match using the up and down arrows, respectively. Checking **Match Case** makes the search case-sensitive. Checking **Whole Words** means that the text must not have any letters or numbers next to it, only symbols and whitespace.
- **Find Next**: Similar to the down arrow, shows the next occurrence.
- **Find Previous**: Similar to the up arrow, shows the previous occurrence.
- **Replace...**: Opens the find and replace bar under the status bar to find text and replace it in the open file. You can choose to replace them one at a time or all at once. Additionally, you can limit the replacement to the selected text by checking the **Selection Only** checkbox in the find and replace bar. You can also use Ctrl + D to additionally select the next instance of the currently selected text, allowing you to perform an in-line replacement on multiple occurrences.
- **Find in Files...**: Opens a window to search for text within the files in the project folder. Selecting "Find..." starts with the chosen folder, and includes the file extensions checked in the filters. The results are shown in the bottom panel with the number of matches and total number of files found, in the **Search Results** tab. Clicking on a result opens the file and jumps to the respective line.
- **Replace in Files...**: Opens a window to search and replace text with different text within the found files in the project folder. After clicking **Replace...**, you can select in which files to replace using the **Search Results** tab in the bottom panel by (un)checking them and using **Replace All** button.

> **Warning:** Note that "Replace in Files" operation cannot be undone!

> **Tip:** Both the **Find in Files** and **Replace in Files** windows share the **Search...** and **Replace...** buttons. The only difference in the latter window is an additional text field that automatically fills in the search results panel when the **Replace...** button is clicked. The replacement operation is only executed if you click the **Replace All** button in this bottom panel, allowing you to also edit the word to replace later within this panel.

- **Contextual Help\***: Opens the list of built-in class reference similar to pressing F1 on a symbol, or choosing **Lookup Symbol** from the context menu.

The **Go To** menu lets you navigate within the code at ease with these options:

- **Go to Function...**: Opens the function list to jump to. You can achieve the same result by typing in the filter methods bar in the script panel.
- **Go to Line...**: Jumps to the entered line number in the code editor.
- **Bookmarks**: Contains actions for the bookmark functionality, which you can use to find your way through your code easier, such as an incomplete section. Bookmarked lines will have a blue bookmark symbol left of the line number.

- **Toggle Bookmark\***: Adds or removes the bookmark on the line where the caret is. You can also right click on a line to achieve this.
- **Remove All Bookmarks**: Removes all bookmarks in the open document.
- **Go to Next Bookmark**: Jumps to the next bookmark in the open document.
- **Go to Previous Bookmark**: Jumps to the previous bookmark in the open document.
- **Bookmarks** menu will also contain the list of bookmarked lines, including their line number and displaying the partial content in that line.
- **Breakpoints**: Breakpoints are helpful while debugging your code. Similar to **Bookmarks** menu, this menu lets you add or remove breakpoints, navigate between them and directly jump to a specific breakpoint. An easy way to add a breakpoint is hovering over the blank area left of a line number. It will show a faded red circle. Clicking it will add a breakpoint and the circle will stay there. Clicking on a circle removes the breakpoint.

**Debug** menu offers actions which can be used while debugging. See [Script editor debug tools and options](tutorials_scripting.md) for more.

#### Coding area

> **Note:** This section will only cover the basics of the coding area in terms of the user interface. To learn more about scripting in Godot, refer to the [GDScript](tutorials_scripting.md) or [Scripting](tutorials_scripting.md) documentation.

The coding area is where you will type your scripts if you are using the built-in text editor. It offers highlighting and auto-completion features to help you while you code.

The coding area shows line numbers on the left side. Below the navigation arrows on the right side, there is a clickable minimap that provides an overview of the entire script, allowing you to scroll through it.

If a line of code is long enough (more than 80 characters, by default), the text editor will display a vertical line that can be used as a soft guideline. For a hard guideline, this value is set to 100 characters, by default. Both values can be changed, or the display of the line can be toggled in the "Appearance" settings of the text editor.

In the script, to the left of function definitions, you might see additional icons. The icon indicates that this function is an [override](tutorials_scripting.md) of an existing function. Clicking it opens the documentation of the original function. The icon means that it is a receiving method of a signal. Clicking it shows where the signal is coming from. A icon to the left of the line denotes a foldable block. You can click to collapse or expand it. Alternatively, the ellipsis (...) icon can also be clicked to expand a folded block.

The example below summarizes the paragraph above. Lines 52, 56, and 58 are foldable blocks, line 57 is a code region with the name "New Code Region," which you can also fold, and line 62 is a folded block. Line 53 is a bookmark, which can quickly be jumped to using the **Go To > Bookmarks** menu. Line 55 is a breakpoint that can be used in [debugging](tutorials_scripting.md).

Many of the colors of the text editor such as highlighting colors, or even breakpoint or bookmark icon colors can be customized. You can experiment them by opening the text editor settings navigating to **Editor > Editor Settings > Text Editor** section.

---

## Using the engine compilation configuration editor

Godot comes with a large set of built-in features. While this is convenient, this also means its binary size is larger than it could be, especially for projects that only use a small portion of its feature set.

To help reduce binary size, it is possible to compile custom export templates with certain features disabled. This is described in detail in Optimizing a build for size. However, determining which features need to be disabled can be a tedious task. The engine compilation configuration editor aims to address this by providing an interface to view and manage these features easily, while also being able to detect the features currently being used in the project.

The Project > Tools > Engine Compilation Configuration Editor allows you to create and manage build profiles for your Godot project.

From now on, you have two possibilities:

- View the list and manually uncheck features that you don't need.
- Use the Detect from Project button to automatically detect features currently used in the project and disable unused features. Note that this will override the existing list of features, so if you have manually unchecked some items, their state will be reset based on whether the project actually uses the feature.

Once you click Detect from Project, the project detection step will run. This can take from a few seconds up to several minutes depending on the project size. Once detection is complete, you'll see an updated list of features with some features disabled:

> **Warning:** Unchecking features in this dialog will not reduce binary size directly on export. Since it is only possible to actually remove features from the binary at compile-time, you still need to compile custom export templates with the build profile specified to actually benefit from the engine compilation configuration editor.

You can now save the build profile by clicking **Save As** at the top. The build profile can be saved in any location, but it's a good idea to save it somewhere in your project folder and add it to version control to be able to go back to it later when needed. This also allows using version control to track changes to the build profile.

The build profile is a JSON file (and `.gdbuild` extension) that looks like this after detection in the above example:

This file can be passed as a SCons option when compiling export templates:

The buildsystem will use this to disable unused classes and reduce binary size as a result.

### Limitations

The Detect from Project functionality relies on reading the project's scenes and scripts. It will not be able to detect used features in the following scenarios:

- Features that are used in GDScripts that are procedurally created then run at runtime.
- Features that are used in [expressions](tutorials_scripting.md).
- Features that are used in [GDExtensions](tutorials_scripting.md), unless the language binding allows for defining used classes and the extension makes use of the functionality. See [GH-104129](https://github.com/godotengine/godot/pull/104129) for details.
- Features that are used in [external PCKs loaded at runtime](tutorials_export.md).
- Certain edge cases may exist. If unsure, please [open an issue on GitHub](https://github.com/godotengine/godot/issues) with a minimal reproduction project attached.

> **See also:** You can achieve further size reductions by passing other options that reduce binary size. See Optimizing a build for size for more information.

---

## Using the Android editor

In 2023, we added an [Android port of the editor](https://godotengine.org/article/android_godot_editor_play_store_beta_release/) that can be used to create, develop, and export 2D and 3D projects on Android devices.

The app can be downloaded from the [Godot download page](https://godotengine.org/download/android/) or from the [Google Play Store](https://play.google.com/store/apps/details?id=org.godotengine.editor.v4).

> **Note:** The Android editor is in early access, while we continue to refine the experience. See **Limitations & known issues** below.

### Android devices support

The Android editor requires devices running Android 5 Lollipop or higher, with at least OpenGL 3 support. This includes (not exhaustive):

- Android tablets, foldables and large phones
- Android-powered netbooks
- Chromebooks supporting Android apps

### Runtime Permissions

- [All files access permission](https://developer.android.com/training/data-storage/manage-all-files#all-files-access): Enables the editor to create, import, and read project files from any file locations on the device. Without this permission, the editor is still functional, but has limited access to the device's files and directories.
- [REQUEST_INSTALL_PACKAGES](https://developer.android.com/reference/android/Manifest.permission#REQUEST_INSTALL_PACKAGES): Enables the editor to install exported project APKs.
- [RECORD_AUDIO](https://developer.android.com/reference/android/Manifest.permission#RECORD_AUDIO): Requested when the [audio/driver/enable_input](https://docs.godotengine.org/en/stable/classes/class_projectsettings.html#class-projectsettings-property-audio-driver-enable-input) project setting is enabled.

### Tips & Tricks

**Input**

- For the best experience and high level of productivity, connecting a bluetooth keyboard & mouse is recommended to interact with the Android editor. The Android editor supports all of the [usual shortcuts and key mappings](https://docs.godotengine.org/en/stable/tutorials/editor/default_key_mapping.html).
- When interacting with keyboard & mouse, you can decrease the size of the scrollbar using the [interface/touchscreen/increase_scrollbar_touch_area](https://docs.godotengine.org/en/stable/classes/class_editorsettings.html#class-editorsettings-property-interface-touchscreen-increase-scrollbar-touch-area) editor setting.
- For 2D projects, the [block coding plugin](https://godotengine.org/asset-library/asset/3095) can provide a block-based visual alternative to composing scripts when lacking a connected hardware keyboard.

**Multi-tasking**

- On smaller devices, enabling and using picture-in-picture (PiP) mode provides the ability to easily transition between the _Editor_ and the _Play window_.

- PiP can be enabled via the [run/window_placement/play_window_pip_mode](https://docs.godotengine.org/en/latest/classes/class_editorsettings.html#class-editorsettings-property-run-window-placement-play-window-pip-mode) editor setting.
- The [run/window_placement/android_window](https://docs.godotengine.org/en/latest/classes/class_editorsettings.html#class-editorsettings-property-run-window-placement-android-window) editor setting can be used to specify whether the _Play_ window should always launch in PiP mode.
- **Note:** In PiP mode, the _Play_ window does not have input access.

**Projects sync**

- Syncing projects via Git can be done by downloading an Android Git client. We recommend the [Termux terminal](https://termux.dev/en/), an Android terminal emulator which provides access to common terminal utilities such Git and SSH.

- **Note:** To use Git with the Termux terminal, you'll need to grant _WRITE_ permission to the terminal. This can be done by [running the following command](https://wiki.termux.com/wiki/Termux-setup-storage) from within the terminal: `termux-setup-storage`

**Plugins**

- GDExtension plugins work as expected, but require the plugin developer to provide native Android binaries.

### Limitations & known issues

Here are the known limitations and issues of the Android editor:

- No C#/Mono support.
- No support for external script editors.
- While available, the Forward+ renderer is not recommended due to severe performance issues.
- UX not optimized for Android phones form-factor.
- [Android Go devices](https://developer.android.com/guide/topics/androidgo) lacks the _All files access_ permission required for device read/write access. As a workaround, when using an Android Go device, it's recommended to create new projects only in the Android _Documents_ or _Downloads_ directories.
- The editor doesn't properly resume when _Don't keep activities_ is enabled in the _Developer Options_.
- There is a [bug](https://github.com/godotengine/godot/issues/70751) with the Samsung keyboard that causes random input to be inserted when writing scripts. It's recommended to use the [Google keyboard (Gboard)](https://play.google.com/store/apps/details?id=com.google.android.inputmethod.latin) instead.

> **See also:** See the [list of open issues on GitHub related to the Android editor](https://github.com/godotengine/godot/issues?q=is%3Aopen+is%3Aissue+label%3Aplatform%3Aandroid+label%3Atopic%3Aeditor) for a list of known bugs.

---

## Using the Web editor

> **Work in progress:** The content of this page was not yet updated for Godot `4.6` and may be **outdated**. If you know how to improve this page or you can confirm that it's up to date, feel free to [open a pull request](https://github.com/godotengine/godot-docs).

There is a [Web editor](https://editor.godotengine.org/) you can use to work on new or existing projects.

> **Note:** The web editor is in a preliminary stage. While its feature set may be sufficient for educational purposes, it is currently **not recommended for production work**. See **Limitations** below.

### Browser support

The Web editor requires support for WebAssembly's SharedArrayBuffer. This is in turn required to support threading in the browser.

See System requirements (see About docs) for a list of supported web browsers. Mobile browsers are supported, but won't provide an ideal experience due to performance and input limitations.

The web editor only supports the Compatibility renderer, as there is no stable way to run Vulkan applications on the web yet.

> **Note:** If you run into performance issues on Firefox, try using a Chromium-based browser as these may perform better in WebGL applications.

### Limitations

Due to limitations on the Godot or Web platform side, the following features are currently missing:

- No C#/Mono support.
- No GDExtension support.
- No debugging support. This means GDScript debugging/profiling, live scene editing, the Remote Scene tree dock and other features that rely on the debugger protocol will not work.
- No project exporting. As a workaround, you can download the project source using **Project > Tools > Download Project Source** and export it using a [native version of the Godot editor](https://godotengine.org/download).
- The editor won't warn you when closing the tab with unsaved changes.
- No lightmap baking support. You can still use existing lightmaps if they were baked with a native version of the Godot editor (e.g. by importing an existing project).

The following features are unlikely to be supported due to inherent limitations of the Web platform:

- No support for external script editors.
- No support for Android one-click deploy.

> **See also:** See the [list of open issues on GitHub related to the web editor](https://github.com/godotengine/godot/issues?q=is%3Aopen+is%3Aissue+label%3Aplatform%3Aweb+label%3Atopic%3Aeditor) for a list of known bugs.

### Importing a project

To import an existing project, the current process is as follows:

- Specify a ZIP file to preload on the HTML5 filesystem using the **Preload project ZIP** input.
- Run the editor by clicking **Start Godot editor**. The Godot Project Manager should appear after 10-20 seconds. On slower machines or connections, loading may take up to a minute.
- In the dialog that appears at the middle of the window, specify a name for the folder to create then click the **Create Folder** button (it doesn't have to match the ZIP archive's name).
- Click **Install & Edit** and the project will open in the editor.

> **Attention:** It's important to place the project folder somewhere in `/home/web_user/`. If your project folder is placed outside `/home/web_user/`, you will lose your project when closing the editor! When you follow the steps described above, the project folder will always be located in `/home/web_user/projects`, keeping it safe.

### Editing and running a project

Unlike the native version of Godot, the web editor is constrained to a single window. Therefore, it cannot open a new window when running the project. Instead, when you run the project by clicking the Run button or pressing F5, it will appear to "replace" the editor window.

The web editor offers an alternative way to deal with the editor and game windows (which are now "tabs"). You can switch between the **Editor** and **Game** tabs using the buttons on the top. You can also close the running game or editor by clicking the **×** button next to those tabs.

### Where are my project files?

Due to browser security limitations, the editor will save the project files to the browser's IndexedDB storage. This storage isn't accessible as a regular folder on your machine, but is abstracted away in a database.

You can download the project files as a ZIP archive by using **Project > Tools > Download Project Source**. This can be used to export the project using a [native Godot editor](https://godotengine.org/download), since exporting from the web editor isn't supported yet.

In the future, it may be possible to use the [HTML5 FileSystem API](https://developer.mozilla.org/en-US/docs/Web/API/FileSystem) to store the project files on the user's filesystem as the native editor would do. However, this isn't implemented yet.

---
