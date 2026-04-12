# Godot 4 C# Tutorials — Ui (Part 2)

> 4 tutorials. C#-specific code examples.

## Creating applications

Godot features an extensive built-in UI system, and its small distribution size can make it a suitable alternative to frameworks like Electron or Qt.

This page provides guidelines for creating non-game applications with Godot, as well as instructions on performing common tasks to improve desktop integration.

> **Note:** Godot is a game engine first and foremost. This means that creating applications with Godot is a byproduct of its feature set, and not its primary focus of development.

> **See also:** Check out [Material Maker](https://github.com/RodZill4/material-maker) and [Pixelorama](https://github.com/Orama-Interactive/Pixelorama) for examples of open source applications made with Godot.

### Performing common tasks

#### Spawning multiple windows

_This is only supported on Windows, macOS, and Linux (X11/XWayland only, not in native Wayland mode)._

Additional windows can be created using the [Window](../godot_csharp_ui_controls.md) node. Windows can be moved, resized, minimized, and closed independently from the main application window.

However, if you close the main window, all other windows will also be closed since closing the main window ends the process. You can avoid this by minimizing the main window, setting its [unfocusable](../godot_csharp_misc.md) property to `true` (to hide it from the taskbar and task switcher), then creating additional Window nodes immediately on startup. Remember to provide an alternative means of exiting the application in this case, such as a **tray icon**.

#### Constraining the window size

Most applications can only render correctly starting from a certain minimum window size. For more specific use cases, it may also be desired to force a maximum window size.

Size limits can be enforced using the [min_size](../godot_csharp_misc.md) and [max_size](../godot_csharp_misc.md) properties on a Window node. Remember to multiply these size limits according to the application's scale factor (see **Scaling to hiDPI displays** for details).

> **Tip:** As a reminder, you can retrieve the root Window node to set properties on it using [get_window()](../godot_csharp_misc.md) on any Node.

#### Using native file dialogs

_This is only supported on Windows, macOS, Linux, and Android._

By default, Godot uses its own [FileDialog](../godot_csharp_ui_controls.md) implementation for file dialogs. However, you can use the operating system's native file dialogs instead. This is generally preferred by users, as native file dialogs better integrate with the desktop environment and provide a more familiar experience.

You can opt into native file dialogs by enabling the [use_native_dialog](../godot_csharp_misc.md) property on the FileDialog node. This must be done on each FileDialog node used in the project, as there is no project setting to control this behavior globally.

> **Note:** See the [property description](../godot_csharp_misc.md) for details on platform support. Additionally, on macOS, native file dialogs are not supported when game embedding is enabled in the editor. To test this functionality when running the project, make sure you disable game embedding by switching to the Game screen, clicking the 3 vertical dots and unchecking Embed Game on Next Play.

#### Creating an icon in the system tray

_This is only supported on Windows and macOS._

You can create one or more icons in the system tray (also known as the notification area) using a [StatusIndicator](../godot_csharp_misc.md) node. In addition to a tooltip, this node can have a [PopupMenu](../godot_csharp_ui_controls.md) node assigned, so that a dropdown can be shown when clicking the icon.

StatusIndicator also has a [pressed](../godot_csharp_misc.md) signal that is emitted when the icon is clicked. Use this to perform an action without making a dropdown show up, or perform different actions depending on which mouse button was pressed.

After creating a tray icon, you may also want to implement "minimize on close" behavior. This means that when the user attempts to close the application using the window manager X button, it will minimize to the tray instead. To do so, attach this script to an [Autoload](tutorials_scripting.md) _scene_ with a StatusIndicator as the root node:

See [Handling quit requests](tutorials_inputs.md) for details on overriding the behavior when the user tries to close the application. This is important to handle when the user has unsaved changes to avoid data loss.

> **Note:** When multiple StatusIndicator nodes are present, their order in the system tray is determined by the order in which they are added to the scene tree.

#### Using the global menu

_This is only supported on macOS._

On macOS, applications can use the system's global menu bar instead of displaying a menu bar inside the application window. This is also referred to as a _native menu_ in Godot.

Godot supports creating menus through the [MenuBar](../godot_csharp_misc.md) node, which displays its [PopupMenu](../godot_csharp_ui_controls.md) children as menus. You can enable the global menu support on a given MenuBar node by enabling its [prefer_global_menu](../godot_csharp_misc.md) property in the inspector. On macOS, this will cause the MenuBar node to disappear and take no space, with its menus being displayed in the system's global menu bar instead. If this property is disabled, the MenuBar node will display its menus inside the application window as usual, but native popups are still used when supported by the operating system.

> **Note:** The app menu (with the project name in bold), as well as the Window and Help menus are always present on macOS. You should not add these to the global menu manually. In Godot 4.6 and later, you can add new items within these menus by changing the [system_menu_id](../godot_csharp_misc.md) property on the PopupMenu node. You can choose between **Application Menu** (the first menu with the application name in bold), **Window Menu**, **Help Menu** and **Dock** (shown when right-clicking the icon in the Dock). Standard menu items that are already present in those menus will be preserved:

A project can have multiple MenuBar nodes. If multiple MenuBar nodes have the **Prefer Global Menu** property enabled, the menu options will be added at the index defined by the **Start Index** property when the MenuBar node is added to the scene tree. This allows putting context-specific menus at the end of the menu bar, so that the first menu options stay in place when the additional menu bar is added or removed.

For more advanced use cases, you can also use the [NativeMenu](../godot_csharp_misc.md) singleton directly without using the MenuBar node.

> **Note:** Global menu integration is not supported when game embedding is enabled in the editor. To test this functionality when running the project, make sure you disable game embedding by switching to the Game screen, clicking the 3 vertical dots and unchecking Embed Game on Next Play.

#### Using client-side decorations

_This is only supported on macOS._

Many modern applications use _client-side decorations_ (CSD) instead of relying on the operating system's window manager to draw the title bar and window borders (server-side decorations). This allows for a more customizable appearance and better integration with the application's UI.

Godot currently only supports client-side decorations on macOS. This can be used by enabling the [display/window/size/extend_to_title](../godot_csharp_misc.md) project setting.

After enabling client-side decorations, the window border will no longer display, and minimize/maximize/close buttons will show as an overlay to the application. You need to make sure the application provides enough of a margin at the top for the buttons to display comfortably, while also displaying the window title using a Label node or similar.

To conditionally adapt your UI according to whether client-side decorations are enabled, use [DisplayServer.has_feature](../godot_csharp_misc.md) and also check the current value of [Window.extend_to_title](../godot_csharp_ui_controls.md) (which is what the project setting changes):

To correctly position the window title, consider using [DisplayServer.window_get_safe_title_margins()](../godot_csharp_misc.md) which returns a Vector3 where `x` is the left margin, `y` is the right margin (will increase when the system uses right-to-left typesetting), and `z` is the height. Additionally, you can call [DisplayServer.window_set_window_buttons_offset()](../godot_csharp_misc.md) to adjust the position of the close/minimize/maximize buttons (usually to vertically center them).

> **Note:** On macOS, client-side decorations are not supported when game embedding is enabled in the editor. To test this functionality when running the project, make sure you disable game embedding by switching to the Game screen, clicking the 3 vertical dots and unchecking Embed Game on Next Play.

#### Sending desktop notifications

Godot currently does not have native support for sending desktop notifications.

However, on macOS and Linux, you can use the `osascript` and `notify-send` command line utilities respectively to send desktop notifications:

Unfortunately, there is no equivalent that's available out of the box on Windows.

#### Remembering window position and size across sessions

Godot doesn't have built-in support for remembering window position and size across sessions, but it can be manually implemented using a script. A basic example that supports multi-monitor setups would be an [Autoload](tutorials_scripting.md) with this script:

> **Note:** The above example only tracks the main window's position. In applications that spawn multiple windows, you will need to save and load each window position's and size separately.

#### Hiding the window during the splash screen

For some applications, it may be preferred to hide the splash screen to draw a custom splash screen with a progress bar instead (or even no splash screen at all, if the application boots quickly).

Godot lacks native support for hiding the window during the splash screen, but you can achieve this by using a very small transparent window in the project settings, then resizing the window and disabling transparency once the main scene is loaded.

To do so, project settings should be configured as follows:

- [application/boot_splash/bg_color](../godot_csharp_misc.md) set to a transparent black color (RGBA: 0, 0, 0, 0).
- [application/boot_splash/show_image](../godot_csharp_misc.md) disabled.
- [display/window/size/borderless](../godot_csharp_misc.md) enabled.
- [display/window/size/no_focus](../godot_csharp_misc.md) enabled.
- [display/window/size/window_width_override](../godot_csharp_misc.md) set to `1`.
- [display/window/size/window_height_override](../godot_csharp_misc.md) set to `1`.
- [display/window/per_pixel_transparency/allowed](../godot_csharp_misc.md) enabled.
- [display/window/size/transparent](../godot_csharp_misc.md) enabled.
- [rendering/viewport/transparent_background](../godot_csharp_misc.md) enabled.

This script can be used as an [Autoload](tutorials_scripting.md) to restore original settings once the splash screen is done displaying:

#### Displaying the application as an overlay

It is possible to display the application window as an overlay that stays on top of other windows. This can be useful for applications like widgets or system monitors.

To do so, enable **all** the following project settings:

- [display/window/size/borderless](../godot_csharp_misc.md)
- [display/window/per_pixel_transparency/allowed](../godot_csharp_misc.md)
- [display/window/size/transparent](../godot_csharp_misc.md)
- [rendering/viewport/transparent_background](../godot_csharp_misc.md)
- [display/window/size/always_on_top](../godot_csharp_misc.md)
- [display/window/size/no_focus](../godot_csharp_misc.md)

- This prevents the overlay from receiving keyboard input, and also hides from the taskbar and task switcher. Mouse input can still be received by the overlay (see below).

Remember to poosition and resize the window using scripts, as a borderless window can generally not be moved by the user.

To allow mouse input to pass through to the background application, set the [mouse_passthrough](../godot_csharp_misc.md) property to `true` on the Window that is being drawn as an overlay. You can also define a polygon in [mouse_passthrough_polygon](../godot_csharp_misc.md), so that certain areas can still intercept mouse input on the overlay.

Additionally, you may want to set the [exclude_from_capture](../godot_csharp_misc.md) property to `true` to prevent the overlay from appearing in screenshots or recordings. This hint is implemented on Windows and macOS only, and it is on a best-effort basis, so it should not be used as an absolute security measure or DRM.

> **Note:** Displaying as an overlay is not supported when game embedding is enabled in the editor. To test this functionality when running the project, make sure you disable game embedding by switching to the Game screen, clicking the 3 vertical dots and unchecking Embed Game on Next Play. Additionally, keep in mind overlays cannot be shown on top of another application if the application in question uses exclusive fullscreen. Borderless fullscreen must be used instead for overlays to be visible. There are also [known issues](https://github.com/godotengine/godot/issues/76167) with transparent window display on Windows with hybrid GPU setups (such as NVIDIA Optimus). Switching renderers may help resolve the issue. On Linux with X11, transparency will not work if the user has disabled compositing in the window manager settings.

#### Scaling to hiDPI displays

Modern displays vary a lot in terms of pixel density, which means a different scaling factor is often needed to ensure UI elements are readable. The scaling factor can also be provided as a manual adjustment for the user, so that the application remains comfortable to use.

Godot's multiple resolutions support is well-suited to scaling applications when configured correctly. Follow the instructions in the [non-game application section of the Multiple resolutions documentation](tutorials_rendering.md).

> **Note:** Godot currently only supports reading the screen scale factor from the OS settings on macOS, Android, and Linux (Wayland only). On Linux (X11) and Windows, you will need to provide a manual scaling option for the user to adjust the UI scale as needed.

#### Screen reader integration

Screen readers allow visually impaired people to use an application by reading out the UI elements and providing navigation controls. Braille displays are another approach that also rely on accessibility information to function properly.

Godot automatically enables screen reader support if a screen reader is detected as running. This can be configured in the Project Settings using [accessibility/general/accessibility_support](../godot_csharp_misc.md) to disable it in situations where it is not desired. It can also be forcibly enabled, which is useful when using accessibility debugging tools that are not recognized as screen readers by Godot.

Godot uses the [AccessKit](https://accesskit.dev/) library for screen reader integration.

> **Tip:** Since screen reader support uses the screen reader application itself to play audio (rather than the Godot project), it will work even if the audio driver is set to `Dummy` in the project settings as described below.

It's strongly recommended to test your application with popular screen readers on your target platforms to ensure a good user experience for visually impaired users. Examples include [NVDA](https://www.nvaccess.org/download/) on Windows, [VoiceOver](https://www.apple.com/accessibility/features/?vision) on macOS, and [Orca](https://help.gnome.org/orca/) on Linux.

To get screen reader support to a good level of usability, significant amounts of work are required. You need to define accessibility labels using the [Control.accessibility_name](../godot_csharp_ui_controls.md) and [Control.accessibility_description](../godot_csharp_ui_controls.md) properties, and ensure the UI flows in a logical order when read by a screen reader.

> **See also:** See also [Text to speech](tutorials_audio.md) for text-to-speech functionality that is separate from screen readers.

### Recommended project settings

#### Desktop integration

To allow the application to better integrate with the desktop environment, you can set these project settings as follows:

- Enable [application/config/use_custom_user_dir](../godot_csharp_misc.md) and set [application/config/custom_user_dir_name](../godot_csharp_misc.md) to a suitable name for your application. This ensures user settings and files are stored in a dedicated folder instead of the [default Godot folder](tutorials_io.md). By convention, it's a good idea to use normal case on Windows (e.g. `Application Name`) and kebab-case (e.g. `application-name`) on macOS and Linux.
- Configure native icons that match the operating system's design guidelines using [application/config/windows_native_icon](../godot_csharp_misc.md) (in ICO format) and [application/config/macos_native_icon](../godot_csharp_misc.md) (in ICNS format). By default, Godot will automatically generate native icons based on the project icon, but this is not always optimal.

- On Windows, using a manually designed ICO file allows you to use different icons for different resolutions. This can be used to create a special design at lower resolutions for better readability.
- macOS has [app icon guidelines](https://developer.apple.com/design/human-interface-guidelines/app-icons/) that differ significantly from other platforms. Using a tailored native icon design ensures the application better fits in its desktop environment.
- Disable [display/window/subwindows/embed_subwindows](../godot_csharp_misc.md), so that additional windows use the operating system theming and are seen as native operating system windows.

#### Performance

Here are some project settings you can use to reduce CPU, GPU, and memory utilization:

- Use the Compatibility renderer if you don't need features that are exclusive to Forward+ or Mobile. The Compatibility renderer has lower hardware requirements and generally launches faster, which makes it a better option for applications. Creating new windows is also faster with this renderer.
- Enable [application/run/low_processor_mode](../godot_csharp_misc.md) to decrease CPU and GPU usage. This makes the project only render a frame if something on screen has changed.

- Note that in certain cases, the project has to redraw continuously (e.g. if an animation or shader using `TIME` is visible). This will result in significant power draw if done for a long time, which leads to reduced battery life and increased fan noise. To troubleshoot situations where the project redraws continuously, you can enable Debug > Debug Canvas Item Redraws at the top of the editor, then run the project. Areas that are redrawn will be highlighted in red for a second. The highlighting color and duration can be adjusted using the [debug/canvas_items/debug_redraw_time](../godot_csharp_misc.md) and [debug/canvas_items/debug_redraw_color](../godot_csharp_misc.md) project settings.
- The maximum framerate at which the application can draw is determined by [application/run/low_processor_mode_sleep_usec](../godot_csharp_misc.md). This value is expressed in microseconds per frame, so the maximum FPS can be obtained using the formula `1000000.0 / sleep_usec`. By default, this is set to `6900`, which corresponds to a maximum of approximately 145 FPS. You can increase this value to further reduce CPU and GPU usage, at the cost of a less smooth experience.
- Disable [display/window/energy_saving/keep_screen_on](../godot_csharp_misc.md), so that the screen can turn off according to the operating system's power settings when the application is idle. This behavior is normally not desired in a game (e.g. when watching cutscenes), but in applications, we want the screen to turn off to save power when the user is not actively using the application.
- Set [audio/driver/driver](../godot_csharp_misc.md) to `Dummy` _(case-sensitive)_ if your application does not require audio output or input. This prevents the audio server from starting, which saves some CPU and memory resources. This also prevents the application from showing up in the list of applications playing audio in the operating system's audio mixer. On macOS, this also ensures the application does not prevent the device from sleeping.
- Set [physics/2d/physics_engine](../godot_csharp_misc.md) and [physics/3d/physics_engine](../godot_csharp_misc.md) to `Dummy` if your application does not require physics simulation (including object picking). This prevents the physics servers from starting, which saves CPU and memory resources. This also allows the [engine compilation configuration editor](tutorials_editor.md) to automatically detect the fact that the project doesn't use physics.
- Consider setting [display/window/vsync/vsync_mode](../godot_csharp_misc.md) to **Disabled** to reduce input lag. This is particularly helpful in latency-sensitive projects such as drawing applications. This may increase power usage and cause screen tearing, so it's recommended to provide an option for the user to toggle V-Sync as needed.

Check out [Material Maker](https://github.com/RodZill4/material-maker) and [Pixelorama](https://github.com/Orama-Interactive/Pixelorama) for examples of open source applications made with Godot.

#### Mobile

When designing an application for mobile platforms, there are several settings you can enable to improve usability:

**Android:**

- Enable [input_devices/pointing/android/enable_long_press_as_right_click](../godot_csharp_misc.md) to allow users to perform right-click actions using a long press gesture.
- Enable [input_devices/pointing/android/enable_pan_and_scale_gestures](../godot_csharp_misc.md) to allow users to pan and zoom using touch gestures. This will emulate [InputEventPanGesture](../godot_csharp_input.md) and [InputEventMagnifyGesture](../godot_csharp_input.md) events, which can be handled in your project's code and are normally emitted by laptop trackpads.
- Disable Screen > Immersive Mode in the Android export preset to show the system status and navigation bars while the application is active. Additionally, enable Screen > Edge to Edge to make status bars and navigation icons translucent and draw on top of the application. If you do so, make sure your application leaves enough space available for the status bar and navigation icons. You can use [DisplayServer.get_display_safe_area](../godot_csharp_misc.md) and [DisplayServer.get_display_cutouts](../godot_csharp_misc.md) to query the area in which your application can safely draw.

**iOS:**

- Disable [display/window/ios/hide_home_indicator](../godot_csharp_misc.md) to show the home indicator on top of the application.
- Disable [display/window/ios/hide_status_bar](../godot_csharp_misc.md) to keep the status bar visible when the application is active.
- Disable [display/window/ios/suppress_ui_gesture](../godot_csharp_misc.md) to allow UI gestures to work immediately, without requiring them to be done twice.

### Adding unit tests

In an application, there is often more value in having a [unit testing](https://en.wikipedia.org/wiki/Unit_testing) setup compared to a game. This can be used to catch regressions in an automated manner, which tends to be easier to do in an application scenario where logic can be cleanly separated.

GDScript does not feature an integrated unit testing framework, but several plugins for unit testing maintained by the community exist:

- [Gut](https://github.com/bitwes/Gut)
- [GdUnit4](https://github.com/godot-gdunit-labs/gdUnit4) (also supports C#)

With C# and GDExtension (C++, Rust, etc.), you can use standard testing frameworks such as NUnit or [doctest](https://github.com/doctest/doctest).

### Optimizing distribution size

Since non-game applications generally avoid using large parts of the engine, such as audio or 3D functionality, you can compile an optimized export template to reduce its file size. This will also improve startup times, especially on the web platform where binary size is directly linked to initialization speeds.

The size reduction is often significant (relative to the project's size), since applications contain fewer large assets compared to games. See Optimizing a build for size for more information on how to do this.

### Creating installers

While games are typically installed through launchers such as Steam or downloaded as a ZIP, applications are often distributed as installers for better desktop integration. The installer can perform actions like adding shortcuts to the Start Menu or desktop, setting up file associations, and more. Installers can also be run automatically through the command line, which makes them more desirable for corporate environments.

Godot does not have built-in support for creating installers for exported projects. However, it is still possible to create your own installers using third-party tools.

Here is a non-exhaustive list of tools that can be used to create installers:

- **Windows:** [Inno Setup](https://jrsoftware.org/isinfo.php), [NSIS](https://nsis.sourceforge.io/Main_Page)

- If you have a code signing certificate, remember to sign _both_ the installer and project executable. To do so, [sign the exported project executable](tutorials_export.md), create the installer containing the exported project, then manually sign the installer that you just created.
- **macOS:** [create-dmg](https://github.com/create-dmg/create-dmg)
- **Linux:** [Flatpak](https://docs.flatpak.org/en/latest/first-build.html)

- There is a [Godot BaseApp](https://github.com/flathub/org.godotengine.Godot.BaseApp) that can be used as a base for creating Flatpak packages for Godot projects. See [the Pixelorama Flatpak](https://github.com/flathub/com.orama_interactive.Pixelorama) for an example Flatpak that makes use of this BaseApp.

### Resources

These pages cover tasks commonly performed in non-game applications:

- [Runtime file loading and saving](tutorials_io.md)
- [Making HTTP requests](tutorials_networking.md)
- [ConfigFile](../godot_csharp_filesystem.md) (used to save user preferences)

---

## Custom GUI controls

> **Work in progress:** The content of this page was not yet updated for Godot `4.6` and may be **outdated**. If you know how to improve this page or you can confirm that it's up to date, feel free to [open a pull request](https://github.com/godotengine/godot-docs).

### So many controls...

Yet there are never enough. Creating your own custom controls that act just the way you want them to is an obsession of almost every GUI programmer. Godot provides plenty of them, but they may not work exactly the way you want. Before contacting the developers with a pull-request to support diagonal scrollbars, at least it will be good to know how to create these controls easily from script.

### Drawing

For drawing, it is recommended to check the [Custom drawing in 2D](tutorials_2d.md) tutorial. The same applies. Some functions are worth mentioning due to their usefulness when drawing, so they will be detailed next:

#### Checking control size

Unlike 2D nodes, "size" is important with controls, as it helps to organize them in proper layouts. For this, the [Control.size](../godot_csharp_ui_controls.md) property is provided. Checking it during `_draw()` is vital to ensure everything is kept in-bounds.

#### Checking focus

Some controls (such as buttons or text editors) might provide input focus for keyboard or joypad input. Examples of this are entering text or pressing a button. This is controlled with the [Control.focus_mode](../godot_csharp_ui_controls.md) property. When drawing, and if the control supports input focus, it is always desired to show some sort of indicator (highlight, box, etc.) to indicate that this is the currently focused control. To check for this status, the [Control.has_focus()](../godot_csharp_ui_controls.md) method exists. Example

```csharp
public override void _Draw()
{
    if (HasFocus())
    {
        DrawSelected()
    }
    else
    {
        DrawNormal();
    }
}
```

### Sizing

As mentioned before, size is important to controls. This allows them to lay out properly, when set into grids, containers, or anchored. Controls, most of the time, provide a _minimum size_ to help properly lay them out. For example, if controls are placed vertically on top of each other using a [VBoxContainer](../godot_csharp_ui_controls.md), the minimum size will make sure your custom control is not squished by the other controls in the container.

To provide this callback, just override [Control.\_get_minimum_size()](../godot_csharp_ui_controls.md), for example:

```csharp
public override Vector2 _GetMinimumSize()
{
    return new Vector2(20, 20);
}
```

Alternatively, set it using a function:

```csharp
public override void _Ready()
{
    CustomMinimumSize = new Vector2(20, 20);
}
```

### Input

Controls provide a few helpers to make managing input events much easier than regular nodes.

#### Input events

There are a few tutorials about input before this one, but it's worth mentioning that controls have a special input method that only works when:

- The mouse pointer is over the control.
- The button was pressed over this control (control always captures input until button is released)
- Control provides keyboard/joypad focus via [Control.focus_mode](../godot_csharp_ui_controls.md).

This function is [Control.\_gui_input()](../godot_csharp_ui_controls.md). To use it, override it in your control. No processing needs to be set.

```csharp
public override void _GuiInput(InputEvent @event)
{
    if (@event is InputEventMouseButton mbe && mbe.ButtonIndex == MouseButton.Left && mbe.Pressed)
    {
        GD.Print("Left mouse button was pressed!");
    }
}
```

For more information about events themselves, check the [Using InputEvent](tutorials_inputs.md) tutorial.

#### Notifications

Controls also have many useful notifications for which no dedicated callback exists, but which can be checked with the \_notification callback:

```csharp
public override void _Notification(int what)
{
    switch (what)
    {
        case NotificationMouseEnter:
            // Mouse entered the area of this control.
            break;

        case NotificationMouseExit:
            // Mouse exited the area of this control.
            break;

        case NotificationFocusEnter:
            // Control gained focus.
            break;

        case NotificationFocusExit:
            // Control lost focus.
            break;

        case NotificationThemeChanged:
            // Theme used to draw the control changed;
            // update and redraw is recommended if using a theme.
            break;

        case NotificationVisibilityChanged:
            // Control became visible/invisible;
            // check new status with is_visible()
// ...
```

---

## Using Containers

Anchors are an efficient way to handle different aspect ratios for basic multiple resolution handling in GUIs.

For more complex user interfaces, they can become difficult to use.

This is often the case of games, such as RPGs, online chats, tycoons or simulations. Another common case where more advanced layout features may be required is in-game tools (or simply just tools).

All these situations require a more capable OS-like user interface, with advanced layout and formatting. For that, [Containers](../godot_csharp_ui_controls.md) are more useful.

### Container layout

Containers provide a huge amount of layout power (as an example, the Godot editor user interface is entirely done using them):

When a [Container](../godot_csharp_ui_controls.md)-derived node is used, all children [Control](../godot_csharp_ui_controls.md) nodes give up their own positioning ability. This means the _Container_ will control their positioning and any attempt to manually alter these nodes will be either ignored or invalidated the next time their parent is resized.

Likewise, when a _Container_ derived node is resized, all its children will be re-positioned according to it, with a behavior based on the type of container used:

Example of _HBoxContainer_ resizing children buttons.

The real strength of containers is that they can be nested (as nodes), allowing the creation of very complex layouts that resize effortlessly.

### Sizing options

When adding a node to a container, the way the container treats each child depends mainly on their _container sizing options_. These options can be found by inspecting the layout of any _Control_ that is a child of a _Container_.

Sizing options are independent for vertical and horizontal sizing and not all containers make use of them (but most do):

- **Fill**: Ensures the control _fills_ the designated area within the container. No matter if a control _expands_ or not (see below), it will only _fill_ the designated area when this is toggled on (it is by default).
- **Expand**: Attempts to use as much space as possible in the parent container (in each axis). Controls that don't expand will be pushed away by those that do. Between expanding controls, the amount of space they take from each other is determined by the _Stretch Ratio_ (see below). This option is only available when the parent Container is of the right type, for example the _HBoxContainer_ has this option for horizontal sizing.
- **Shrink Begin** When expanding, try to remain at the left or top of the expanded area.
- **Shrink Center** When expanding, try to remain at the center of the expanded area.
- **Shrink End** When expanding, try to remain at the right or bottom of the expanded area.
- **Stretch Ratio**: The ratio of how much expanded controls take up the available space in relation to each other. A control with "2", will take up twice as much available space as one with "1".

Experimenting with these flags and different containers is recommended to get a better grasp on how they work.

### Container types

Godot provides several container types out of the box as they serve different purposes:

#### Box Containers

Arranges child controls vertically or horizontally (via [HBoxContainer](../godot_csharp_ui_controls.md) and [VBoxContainer](../godot_csharp_ui_controls.md)). In the opposite of the designated direction (as in, vertical for a horizontal container), it just expands the children.

These containers make use of the _Stretch Ratio_ property for children with the _Expand_ flag set.

#### Grid Container

Arranges child controls in a grid layout (via [GridContainer](../godot_csharp_ui_controls.md), amount of columns must be specified). Uses both the vertical and horizontal expand flags.

#### Margin Container

Child controls are expanded towards the bounds of this control (via [MarginContainer](../godot_csharp_ui_controls.md)). Padding will be added on the margins depending on the theme configuration.

Again, keep in mind that the margins are a _Theme_ value, so they need to be edited from the constants overrides section of each control:

#### Tab Container

Allows you to place several child controls stacked on top of each other (via [TabContainer](../godot_csharp_ui_controls.md)), with only the _current_ one visible.

Changing the _current_ one is done via tabs located at the top of the container, via clicking:

The titles are generated from the node names by default (although they can be overridden via _TabContainer_ API).

Settings such as tab placement and _StyleBox_ can be modified in the _TabContainer_ theme overrides.

#### Split Container

Accepts only one or two children controls, then places them side to side with a divisor (via [HSplitContainer](../godot_csharp_ui_controls.md) and [VSplitContainer](../godot_csharp_ui_controls.md)). Respects both horizontal and vertical flags, as well as _Ratio_.

The divisor can be dragged around to change the size relation between both children:

#### PanelContainer

A container that draws a _StyleBox_, then expands children to cover its whole area (via [PanelContainer](../godot_csharp_ui_controls.md), respecting the _StyleBox_ margins). It respects both the horizontal and vertical sizing options.

This container is useful as a top-level control, or just to add custom backgrounds to sections of a layout.

#### FoldableContainer

A container that can be expanded/collapsed (via [FoldableContainer](../godot_csharp_misc.md)). Child controls are hidden when it is collapsed.

#### ScrollContainer

Accepts a single child node. If the child node is bigger than the container, scrollbars will be added to allow panning the node around (via [ScrollContainer](../godot_csharp_ui_controls.md)). Both vertical and horizontal size options are respected, and the behavior can be turned on or off per axis in the properties.

Mouse wheel and touch drag (when touch is available) are also valid ways to pan the child control around.

As in the example above, one of the most common ways to use this container is together with a _VBoxContainer_ as child.

#### AspectRatioContainer

A container type that arranges its child controls in a way that preserves their proportions automatically when the container is resized. (via [AspectRatioContainer](../godot_csharp_ui_controls.md)). It has multiple stretch modes, providing options for adjusting the child controls' sizes concerning the container: "fill," "width control height," "height control width," and "cover."

It is useful when you have a container that needs to be dynamic and responsive to different screen sizes, and you want the child elements to scale proportionally without losing their intended shapes.

#### FlowContainer

FlowContainer is a container that arranges its child controls either horizontally or vertically (via [HFlowContainer](../godot_csharp_misc.md) and via [VFlowContainer](../godot_csharp_misc.md)). When the available space runs out, it wraps the children to the next line or column, similar to how text wraps in a book.

It is useful for creating flexible layouts where the child controls adjust automatically to the available space without overlapping.

#### CenterContainer

CenterContainer is a container that automatically keeps all of its child controls centered within it at their minimum size. It ensures that the child controls are always aligned to the center, making it easier to create centered layouts without manual positioning (via [CenterContainer](../godot_csharp_ui_controls.md)).

#### SubViewportContainer

This is a special control that will only accept a single _Viewport_ node as child, and it will display it as if it was an image (via [SubViewportContainer](../godot_csharp_ui_controls.md)).

### Creating custom Containers

It is possible to create a custom container using a script. Here is an example of a container that fits children to its size:

```csharp
using Godot;

public partial class CustomContainer : Container
{
    public override void _Notification(int what)
    {
        if (what == NotificationSortChildren)
        {
            // Must re-sort the children
            foreach (Control c in GetChildren())
            {
                // Fit to own size
                FitChildInRect(c, new Rect2(new Vector2(), Size));
            }
        }
    }

    public void SetSomeSetting()
    {
        // Some setting changed, ask for children re-sort.
        QueueSort();
    }
}
```

---

## Keyboard/Controller Navigation and Focus

It is a common requirement for a user interface to have full keyboard and controller support for navigation and interaction. There are two main reasons why this is beneficial for projects: improved accessibility (not everyone can use mouse or touch controls for interactions), and getting your project ready for consoles (or just for people who prefer to game with a controller on PC).

Navigating between UI elements with keyboard or controller is done by changing which node is actively selected. This is also called changing UI focus. Every [Control](../godot_csharp_ui_controls.md) node in Godot is capable of having focus. By default, some control nodes have the ability to automatically grab focus reacting to built-in UI actions such as `ui_up`, `ui_down`, `ui_focus_next`, etc. These actions can be seen in the project settings in the input map and can be modified.

> **Warning:** Because these actions are used for focus they should not be used for any gameplay code.

### Node settings

In addition to the built-in logic, you can define what is known as focus neighbors for each individual control node. This allows to finely tune the path the UI focus takes across the user interface of your project. The settings for individual nodes can be found in the Inspector dock, under the "Focus" category of the "Control" section.

Neighbor options are used to define nodes for 4-directional navigation, such as using arrow keys or a D-pad on a controller. For example, the bottom neighbor will be used when navigating down with the down arrow or by pushing down on the D-pad. The "Next" and "Previous" options are used with the focus shift button, such as Tab on desktop operating systems.

> **Note:** A node can lose focus if it becomes hidden.

The mode setting defines how a node can be focused. **All** means a node can be focused by clicking on it with the mouse, or selecting it with a keyboard or controller. **Click** means it can only be focused on by clicking on it. Finally, **None** means it can't be focused at all. Different control nodes have different default settings for this based on how they are typically used, for example, [Label](../godot_csharp_ui_controls.md) nodes are set to "None" by default, while [buttons](../godot_csharp_misc.md) are set to "All".

Make sure to properly configure your scenes for focus and navigation. If a node has no focus neighbor configured, the engine will try to guess the next control automatically. This may result in unintended behavior, especially in a complex user interface that doesn't have well-defined vertical or horizontal navigation flow.

### Necessary code

For keyboard and controller navigation to work correctly, any node must be focused by using code when the scene starts. Without doing this, pressing buttons or keys won't do anything.

You can use the [Control.grab_focus()](../godot_csharp_ui_controls.md) method to focus a control. Here is a basic example of setting initial focus with code:

```csharp
public override void _Ready()
{
    GetNode<Button>("StartButton").GrabFocus.CallDeferred();
}
```

Now when the scene starts, the "Start Button" node will be focused, and the keyboard or a controller can be used to navigate between it and other UI elements.

---
