# Godot 4 GDScript Tutorials — Export (Part 2)

> 5 tutorials. GDScript-specific code examples.

## Exporting for the Web

> **See also:** This page describes how to export a Godot project to HTML5. If you're looking to compile editor or export template binaries from source instead, read Compiling for the Web.

HTML5 export allows publishing games made in Godot Engine to the browser. This requires support for [WebAssembly](https://webassembly.org/) and [WebGL 2.0](https://www.khronos.org/webgl/) in the user's browser.

> **Attention:** Projects written in C# using Godot 4 currently cannot be exported to the web. See [this blog post](https://godotengine.org/article/platform-state-in-csharp-for-godot-4-2/#web) for more information. To use C# on web platforms, use Godot 3 instead.

> **Tip:** Use the browser-integrated developer console, usually opened with F12 or Ctrl + Shift + I (Cmd + Option + I on macOS), to view **debug information** like JavaScript, engine, and WebGL errors. If the shortcut doesn't work, it's because Godot actually captures the input. You can still open the developer console by accessing the browser's menu.

> **Note:** Due to security concerns with `SharedArrayBuffer` due to various exploits, the use of multiple threads for the Web platform has multiple drawbacks, including requiring specific server-side headers and complete cross-origin isolation (meaning no ads, nor third-party integrations on the website hosting your game). Since Godot 4.3, Godot supports exporting your game on a single thread, which solves this issue. While it has some drawbacks on its own (it cannot use threads, and is not as performant as the multi-threaded export), it doesn't require as much overhead to install. It is also more compatible overall with stores like [itch.io](https://itch.io/) or Web publishers like [Poki](https://poki.com/) or [CrazyGames](https://crazygames.com/). The single-threaded export works very well on macOS and iOS too, where it always had compatibility issues with multiple threads exports. For these reasons, it is the preferred and now default way to export your games on the Web. For more information, see [this blog post about single-threaded Web export](https://godotengine.org/article/progress-report-web-export-in-4-3/#single-threaded-web-export).

> **See also:** See the [list of open issues on GitHub related to the web export](https://github.com/godotengine/godot/issues?q=is%3Aopen+is%3Aissue+label%3Aplatform%3Aweb) for a list of known bugs.

### Export file name

We suggest users to export their Web projects with `index.html` as the file name. `index.html` is usually the default file loaded by web servers when accessing the parent directory, usually hiding the name of that file.

> **Attention:** The Godot 4 Web export expects some files to be named the same name as the one set in the initial export. Some issues could occur if some exported files are renamed, including the main HTML file.

### WebGL version

Godot 4 can only target WebGL 2.0 (using the Compatibility rendering method). Forward+/Mobile are not supported on the web platform, as these rendering methods are designed around modern low-level graphics APIs. Godot currently does not support WebGPU, which is a prerequisite for allowing Forward+/Mobile to run on the web platform.

See [Can I use WebGL 2.0](https://caniuse.com/webgl2) for a list of browser versions supporting WebGL 2.0. Note that Safari has several issues with WebGL 2.0 support that other browsers don't have, so we recommend using a Chromium-based browser or Firefox if possible.

### Mobile considerations

The Web export can run on mobile platforms with some caveats. While native Android and iOS exports will always perform better by a significant margin, the Web export allows people to run your project without going through app stores.

Remember that CPU and GPU performance is at a premium when running on mobile devices. This is even more the case when running a project exported to Web (as it's WebAssembly instead of native code). See [Performance](tutorials_performance.md) section of the documentation for advice on optimizing your project. If your project runs on platforms other than Web, you can use Feature tags to apply low-end-oriented settings when running the project exported to Web.

To speed up loading times on mobile devices, you should also compile an optimized export template with unused features disabled. Depending on the features used by your project, this can reduce the size of the WebAssembly payload significantly, making it faster to download and initialize (even when cached).

### Audio playback

Since Godot 4.3, audio playback is done using the Web Audio API on the web platform. This **Sample** playback mode allows for low latency even when the project is exported without thread support, but it has several limitations:

- AudioEffects are not supported.
- [Reverberation and doppler](tutorials_audio.md) effects are not supported.
- Procedural audio generation is not supported.
- Positional audio may not always work correctly depending on the node's properties.

To use Godot's own audio playback system on the web platform, you can change the default playback mode using the **Audio > General > Default Playback Type.web** project setting, or change the **Playback Type** property to **Stream** on an [AudioStreamPlayer](../godot_gdscript_audio.md), [AudioStreamPlayer2D](../godot_gdscript_audio.md) or [AudioStreamPlayer3D](../godot_gdscript_audio.md) node. This leads to increased latency (especially when thread support is disabled), but it allows the full suite of Godot's audio features to work.

### Export options

If a runnable web export template is available, a button appears between the _Stop scene_ and _Play edited Scene_ buttons in the editor to quickly open the game in the default browser for testing.

If your project uses GDExtension, **Extension Support** needs to be enabled.

If you plan to use [VRAM compression](tutorials_assets_pipeline.md) make sure that **VRAM Texture Compression** is enabled for the targeted platforms (enabling both **For Desktop** and **For Mobile** will result in a bigger, but more compatible export).

If a path to a **Custom HTML shell** file is given, it will be used instead of the default HTML page. See [Custom HTML page for Web export](tutorials_platform.md).

**Head Include** is appended into the `<head>` element of the generated HTML page. This allows to, for example, load webfonts and third-party JavaScript APIs, include CSS, or run JavaScript code.

The window size will automatically match the browser window size by default. If you want to use a fixed size instead regardless of the browser window size, change **Canvas Resize Policy** to **None**. This allows controlling the window size with custom JavaScript code in the HTML shell. You can also set it to **Project** to make it behave closer to a native export, according to the [project settings](tutorials_rendering.md).

> **Important:** Each project must generate their own HTML file. On export, several text placeholders are replaced in the generated HTML file specifically for the given export options. Any direct modifications to that HTML file will be lost in future exports. To customize the generated file, use the **Custom HTML shell** option.

#### Thread and extension support

If **Thread Support** is enabled, the exported project will be able to [make use of multithreading](tutorials_performance.md) to improve performance. This also allows for low-latency audio playback when the playback type is set to **Stream** (instead of the default **Sample** that is used in web exports). Enabling this feature requires the use of cross-origin isolation headers, which are described in the **Serving the files** section below.

If **Extensions Support** is enabled, [GDExtensions](tutorials_scripting.md) will be able to be loaded. Note that GDExtensions still need to be specifically compiled for the web platform to work. Like thread support, enabling this feature requires the use of cross-origin isolation headers.

#### Exporting as a Progressive Web App (PWA)

If **Progressive Web App > Enable** is enabled, it will have several effects:

- Configure high-resolution icons, a display mode and screen orientation. These are configured at the end of the Progressive Web App section in the export options. These options are used if the user adds the project to their device's homescreen, which is common on mobile platforms. This is also supported on desktop platforms, albeit in a more limited capacity.
- Allow the project to be loaded without an Internet connection if it has been loaded at least once beforehand. This works thanks to the _service worker_ that is installed when the project is first loaded in the user's browser. This service worker provides a local fallback when no Internet connection is available.

- Note that web browsers can choose to evict the cached data if the user runs low on disk space, or if the user hasn't opened the project for a while. To ensure data is cached for a longer duration, the user can bookmark the page, or ideally add it to their device's home screen.
- If the offline data is not available because it was evicted from the cache, you can configure an **Offline Page** that will be displayed in this case. The page must be in HTML format and will be saved on the client's machine the first time the project is loaded.
- Ensure cross-origin isolation headers are always present, even if the web server hasn't been configured to send them. This allows exports with threads enabled to work when hosted on any website, even if there is no way for you to control the headers it sends.

- This behavior can be disabled by unchecking **Enable Cross Origin Isolation Headers** in the Progressive Web App section.

### Limitations

For security and privacy reasons, many features that work effortlessly on native platforms are more complicated on the web platform. Following is a list of limitations you should be aware of when porting a Godot game to the web.

> **Important:** Browser vendors are making more and more functionalities only available in [secure contexts](https://developer.mozilla.org/en-US/docs/Web/Security/Secure_Contexts), this means that such features are only be available if the web page is served via a secure HTTPS connection (localhost is usually exempt from such requirement).

#### Using cookies for data persistence

Users must **allow cookies** (specifically IndexedDB) if persistence of the `user://` file system is desired. When playing a game presented in an `iframe`, **third-party** cookies must also be enabled. Incognito/private browsing mode also prevents persistence.

The method `OS.is_userfs_persistent()` can be used to check if the `user://` file system is persistent, but can give false positives in some cases.

#### Background processing

The project will be paused by the browser when the tab is no longer the active tab in the user's browser. This means functions such as `_process()` and `_physics_process()` will no longer run until the tab is made active again by the user (by switching back to the tab). This can cause networked games to disconnect if the user switches tabs for a long duration.

This limitation does not apply to unfocused browser _windows_. Therefore, on the user's side, this can be worked around by running the project in a separate _window_ instead of a separate tab.

#### Full screen and mouse capture

Browsers do not allow arbitrarily **entering full screen**. The same goes for **capturing the cursor**. Instead, these actions have to occur as a response to a JavaScript input event. In Godot, this means entering full screen from within a pressed input event callback such as `_input` or `_unhandled_input`. Querying the [Input](../godot_gdscript_input.md) singleton is not sufficient, the relevant input event must currently be active.

For the same reason, the full screen project setting doesn't work unless the engine is started from within a valid input event handler. This requires [customization of the HTML page](tutorials_platform.md).

#### Audio

Some browsers restrict autoplay for audio on websites. The easiest way around this limitation is to request the player to click, tap or press a key/button to enable audio, for instance when displaying a splash screen at the start of your game.

> **See also:** Google offers additional information about their [Web Audio autoplay policies](https://www.chromium.org/audio-video/autoplay/). Apple's Safari team also posted additional information about their [Auto-Play Policy Changes for macOS](https://webkit.org/blog/7734/auto-play-policy-changes-for-macos/).

> **Warning:** Access to microphone requires a **secure context**.

> **Warning:** Since Godot 4.3, by default Web exports will use samples instead of streams to play audio. This is due to the way browsers prefer to play audio and the lack of processing power available when exporting Web games with the **Use Threads** export option off. Please note that audio effects aren't yet implemented for samples.

#### Networking

Low-level networking is not implemented due to lacking support in browsers.

Currently, only [HTTP client](tutorials_networking.md), [HTTP requests](tutorials_networking.md), [WebSocket (client)](tutorials_networking.md) and [WebRTC](tutorials_networking.md) are supported.

The HTTP classes also have several restrictions on the HTML5 platform:

- Accessing or changing the `StreamPeer` is not possible
- Threaded/Blocking mode is not available
- Cannot progress more than once per frame, so polling in a loop will freeze
- No chunked responses
- Host verification cannot be disabled
- Subject to [same-origin policy](https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy)

#### Clipboard

Clipboard synchronization between engine and the operating system requires a browser supporting the [Clipboard API](https://developer.mozilla.org/en-US/docs/Web/API/Clipboard_API), additionally, due to the API asynchronous nature might not be reliable when accessed from GDScript.

> **Warning:** Requires a **secure context**.

#### Gamepads

Gamepads will not be detected until one of their button is pressed. Gamepads might have the wrong mapping depending on the browser/OS/gamepad combination, sadly the [Gamepad API](https://developer.mozilla.org/en-US/docs/Web/API/Gamepad_API/Using_the_Gamepad_API) does not provide a reliable way to detect the gamepad information necessary to remap them based on model/vendor/OS due to privacy considerations.

> **Warning:** Requires a **secure context**.

### Serving the files

Exporting for the web generates several files to be served from a web server, including a default HTML page for presentation. A custom HTML file can be used, see [Custom HTML page for Web export](tutorials_platform.md).

> **Warning:** Only when exporting with **Use Threads**, to ensure low audio latency and the ability to use [Thread](../godot_gdscript_core.md) in web exports, Godot 4 web exports use [SharedArrayBuffer](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SharedArrayBuffer). This requires a **secure context**, while also requiring the following CORS headers to be set when serving the files: ```gdscript
> Cross-Origin-Opener-Policy: same-origin
> Cross-Origin-Embedder-Policy: require-corp

````If you don't control the web server or are unable to add response headers, check **Progressive Web App > Enable** in the export options. This applies a service worker-based workaround that allows the project to run by simulating the presence of these response headers. A secure context is still required in this case. If the client doesn't receive the required response headers or the service worker-based workaround is not applied, **the project will not run**.



The generated `.html` file can be used as `DirectoryIndex` in Apache servers and can be renamed to e.g. `index.html` at any time. Its name is never depended on by default.



The HTML page draws the game at maximum size within the browser window. This way, it can be inserted into an `<iframe>` with the game's size, as is common on most web game hosting sites.



The other exported files are served as they are, next to the `.html` file, names unchanged. The `.wasm` file is a binary WebAssembly module implementing the engine. The `.pck` file is the Godot main pack containing your game. The `.js` file contains start-up code and is used by the `.html` file to access the engine. The `.png` file contains the boot splash image.



The `.pck` file is binary, usually delivered with the MIME-type *application/octet-stream*. The `.wasm` file is delivered as *application/wasm*.



> **Warning:** Delivering the WebAssembly module (`.wasm`) with a MIME-type other than *application/wasm* can prevent some start-up optimizations.



Delivering the files with server-side compression is recommended especially for the `.pck` and `.wasm` files, which are usually large in size. The WebAssembly module compresses particularly well, down to around a quarter of its original size with gzip compression. Consider using Brotli precompression if supported on your web server for further file size savings.



**Hosts that provide on-the-fly compression:** GitHub Pages (gzip)



**Hosts that don't provide on-the-fly compression:** itch.io, GitLab Pages ([supports manual gzip precompression](https://docs.gitlab.com/user/project/pages/introduction/#serving-compressed-assets))



> **Tip:** The Godot repository includes a [Python script to host a local web server](https://raw.githubusercontent.com/godotengine/godot/master/platform/web/serve.py). This script is intended for testing the web editor, but it can also be used to test exported projects. Save the linked script to a file called `serve.py`, move this file to the folder containing the exported project's `index.html`, then run the following command in a command prompt within the same folder: ```gdscript
# You may need to replace `python` with `python3` on some platforms.
python serve.py --root .
``` On Windows, you can open a command prompt in the current folder by holding Shift and right-clicking on empty space in Windows Explorer, then choosing **Open PowerShell window here**. This will serve the contents of the current folder and open the default web browser automatically. Note that for production use cases, this Python-based web server should not be used. Instead, you should use an established web server such as Apache or nginx.



### Interacting with the browser and JavaScript



See the [dedicated page](tutorials_platform.md) on how to interact with JavaScript and access some unique Web browser features.



### Environment variables



You can use the following environment variables to set export options outside of the editor. During the export process, these override the values that you set in the export menu.



| Export option | Environment variable |
| --- | --- |
| Encryption / Encryption Key | GODOT_SCRIPT_ENCRYPTION_KEY |



### Troubleshooting



#### Running the export locally shows another project instead



If you use one-click deploy in multiple projects, you may notice that one of the projects you've previously deployed is shown instead of the project you're currently working on. This is due to service worker caching which currently lacks an automated cache busting mechanism.



As a workaround, you can manually unregister the current service worker so that the cache is reset. This also allows a new service worker to be registered. In Chromium-based browsers, open the Developer Tools by pressing F12 or Ctrl + Shift + I (Cmd + Option + I on macOS), then click on the Application tab in DevTools (it may be hidden behind a chevron icon if the devtools pane is narrow). You can either check Update on reload and reload the page, or click Unregister next to the service worker that is currently registered, then reload the page.



The procedure is similar in Firefox. Open developer tools by pressing F12 or Ctrl + Shift + I (Cmd + Option + I on macOS), click on the Application tab in DevTools (it may be hidden behind a chevron icon if the devtools pane is narrow). Click Unregister next to the service worker that is currently registered, then reload the page.



### Export options



You can find a full list of export options available in the [EditorExportPlatformWeb](../godot_gdscript_editor.md) class reference.

---

## Exporting for Windows

> **See also:** This page describes how to export a Godot project to Windows. If you're looking to compile editor or export template binaries from source instead, read Compiling for Windows.



The simplest way to distribute a game for PC is to copy the executable (`godot.exe`), compress the folder and send it to someone else. However, this is often not desired.



Godot offers a more elegant approach for PC distribution when using the export system. When exporting for Windows, the exporter takes all the project files and creates a `data.pck` file. This file is bundled with a specially optimized binary that is smaller, faster and does not contain the editor and debugger.



### Architecture



There are 3 different processor architectures that exported Godot projects can run on in Windows:



- x86_64
- x86_32
- arm64



The default is x86_64, this is the most common architecture of PC processors today. All modern Intel and AMD processors as of writing this are x86_64.



x86_32 will give you a 32bit executable that can run on 32bit-only versions of Windows as well as modern versions which are 64bit. It is NOT recommended to use this option unless you are trying to get your project to run on an old 32bit version of Windows. And it should be noted that no 32bit versions of Windows receive Microsoft support anymore.



arm64 processors are modern but less common than x86_64, and run Windows on ARM. Snapdragon X Elite is an example of a modern Windows ARM processor. Using this export option will allow your project to run natively on arm processors without Microsoft's Prism emulator. Executables made using this option will NOT run on regular Windows with an x86_64 processor. If you're uploading your project to a platform that allows multiple executables, such as itch.io, and are confident a Snapdragon X Elite processor is powerful enough to run it, we would recommend providing an ARM version. Prism emulation is far from perfect, and Godot does not require you to build or design your game in any special way to run on ARM.



### Changing the executable icon



Godot will automatically use whatever image is set as your project's icon in the project settings, and convert it to an ICO file for the exported project. If you want to manually create an ICO file for greater control over how the icon looks at different resolutions then see the Manually changing application icon for Windows page.



### Code signing



Godot is capable of automatic code signing on export. To do this you must have the `Windows SDK` (on Windows) or [osslsigncode](https://github.com/mtrojnar/osslsigncode) (on any other OS) installed. You will also need a package signing certificate, information on creating one can be found [here](https://learn.microsoft.com/en-us/windows/msix/package/create-certificate-package-signing).



> **Warning:** If you export for Windows with embedded PCK files, you will not be able to sign the program as it will break. On Windows, PCK embedding is also known to cause false positives in antivirus programs. Therefore, it's recommended to avoid using it unless you're distributing your project via Steam as it bypasses code signing and antivirus checks.



#### Setup



Settings need to be changed in two places. First, in the editor settings, under **Export > Windows**. Click on the folder next to the `Sign Tool` setting, if you're using Windows navigate to and select `SignTool.exe`, if you're on a different OS select `osslsigncode`.



The second location is the Windows export preset, which can be found in **Project > Export...**. Add a windows desktop preset if you haven't already. Under options there is a code signing category.



`Enabled` must be set to true, and `Identity` must be set to the signing certificate. The other settings can be adjusted as needed. Once this is Done Godot will sign your project on export.



### Environment variables



You can use the following environment variables to set export options outside of the editor. During the export process, these override the values that you set in the export menu.



| Export option | Environment variable |
| --- | --- |
| Encryption / Encryption Key | GODOT_SCRIPT_ENCRYPTION_KEY |
| Options / Codesign / Identity Type | GODOT_WINDOWS_CODESIGN_IDENTITY_TYPE |
| Options / Codesign / Identity | GODOT_WINDOWS_CODESIGN_IDENTITY |
| Options / Codesign / Password | GODOT_WINDOWS_CODESIGN_PASSWORD |



### Export options



You can find a full list of export options available in the [EditorExportPlatformWindows](../godot_gdscript_editor.md) class reference.

---

## Exporting packs, patches, and mods

### Use cases



Oftentimes, one would like to add functionality to one's game after it has been deployed.



Examples of this include...



- Downloadable Content: the ability to add features and content to one's game.
- Patches: the ability to fix a bug that is present in a shipped product.
- Mods: grant other people the ability to create content for one's game.



These tools help developers to extend their development beyond the initial release.



### Overview of PCK/ZIP files



Godot enables this via a feature called **resource packs** (PCK files, with the `.pck` extension, or ZIP files).



**Advantages:**



- incremental updates/patches
- offer DLCs
- offer mod support
- no source code disclosure needed for mods
- more modular project structure
- users don't have to replace the entire game



The first part of using them involves exporting and delivering the project to players. Then, when one wants to add functionality or content later on, they just deliver the updates via PCK/ZIP files to the users.



PCK/ZIP files usually contain, but are not limited to:



- scripts
- scenes
- shaders
- models
- textures
- sound effects
- music
- any other asset suitable for import into the game



The PCK/ZIP files can even be an entirely different Godot project, which the original game loads in at runtime.



It is possible to load both PCK and ZIP files as additional packs at the same time. See PCK versus ZIP pack file formats for a comparison of the two formats.



> **See also:** If you want to load loose files at runtime (not packed in a PCK or ZIP by Godot), consider using [Runtime file loading and saving](tutorials_io.md) instead. This is useful for loading user-generated content that is not made with Godot, without requiring users to pack their mods into a specific file format. The downside of this approach is that it's less transparent to the game logic, as it will not benefit from the same resource management as PCK/ZIP files.



### Generating PCK files



In order to pack all resources of a project into a PCK file, open the project and go to **Project > Export** and click on **Export PCK/ZIP**. Also, make sure to have an export preset selected while doing so.



Another method would be to [export from the command line](tutorials_editor.md) with `--export-pack`. The output file must with a `.pck` or `.zip` file extension. The export process will build that type of file for the chosen platform.



> **Note:** If one wishes to support mods for their game, they will need their users to create similarly exported files. Assuming the original game expects a certain structure for the PCK's resources and/or a certain interface for its scripts, then either... 1. The developer must publicize documentation of these expected structures/ interfaces, expect modders to install Godot Engine, and then also expect those modders to conform to the documentation's defined API when building mod content for the game (so that it will work). Users would then use Godot's built in exporting tools to create a PCK file, as detailed above.
2. The developer uses Godot to build a GUI tool for adding their exact API content to a project. This Godot tool must either run on a tools-enabled build of the engine or have access to one (distributed alongside or perhaps in the original game's files). The tool can then use the Godot executable to export a PCK file from the command line with [OS.execute()](../godot_gdscript_misc.md). The game itself shouldn't use a tool-build of the engine (for security), so it's best to keep the modding tool and game separate.



### Opening PCK or ZIP files at runtime



To load a PCK or ZIP file, one uses the ProjectSettings singleton. The following example expects a `mod.pck` file in the directory of the game's executable. The PCK or ZIP file contains a `mod_scene.tscn` test scene in its root.


```gdscript
func _your_function():
    # This could fail if, for example, mod.pck cannot be found.
    var success = ProjectSettings.load_resource_pack(OS.get_executable_path().get_base_dir().path_join("mod.pck"))

    if success:
        # Now one can use the assets as if they had them in the project from the start.
        var imported_scene = load("res://mod_scene.tscn")
````

> **Warning:** By default, if you import a file with the same file path/name as one you already have in your project, the imported one will replace it. This is something to watch out for when creating DLC or mods. You can solve this problem by using a tool that isolates mods to a specific mods subfolder. However, it is also a way of creating patches for one's own game. A PCK/ZIP file of this kind can fix the content of a previously loaded PCK/ZIP (therefore, the order in which packs are loaded matters). To opt out of this behavior, pass `false` as the second argument to [ProjectSettings.load_resource_pack()](../godot_gdscript_filesystem.md).

> **Note:** For a C# project, you need to build the DLL and place it in the project directory first. Then, before loading the resource pack, you need to load its DLL as follows: `Assembly.LoadFile("mod.dll")`

#### Troubleshooting

If you are loading a resource pack and are not noticing any changes, it may be due to the pack being loaded too late. This is particularly the case with menu scenes that may preload other scenes using `preload()`. This means that loading a pack in the menu will not affect the other scene that was already preloaded.

To avoid this, you need to load the pack as early as possible. To do so, create a new [autoload](tutorials_scripting.md) script and call [ProjectSettings.load_resource_pack()](../godot_gdscript_filesystem.md) in the autoload script's `_init()` function, rather than `_enter_tree()` or `_ready()`.

### Summary

This tutorial explains how to add mods, patches, or DLC to a game. The most important thing is to identify how one plans to distribute future content for their game and develop a workflow that is customized for that purpose. Godot should make that process smooth regardless of which route a developer pursues.

---

## Exporting projects

### Why export?

Originally, Godot did not have any means to export projects. The developers would compile the proper binaries and build the packages for each platform manually.

When more developers (and even non-programmers) started using it, and when our company started taking more projects at the same time, it became evident that this was a bottleneck.

#### On PC

Distributing a game project on PC with Godot is rather easy. Drop the Godot binary in the same directory as the `project.godot` file, then compress the project directory and you are done.

It sounds simple, but there are probably a few reasons why the developer may not want to do this. The first one is that it may not be desirable to distribute loads of files. Some developers may not like curious users peeking at how the game was made, others may find it inelegant, and so on. Another reason is that the developer might prefer a specially-compiled binary, which is smaller in size, more optimized and does not include tools like the editor and debugger.

Finally, Godot has a simple but efficient system for creating DLCs as extra package files.

#### On mobile

The same scenario on mobile platforms is a little worse. To distribute a project on those devices, a binary for each of those platforms is built, then added to a native project together with the game data.

This can be troublesome because it means that the developer must be familiarized with the SDK of each platform before even being able to export. While learning each SDK is always encouraged, it can be frustrating to be forced to do it at an undesired time.

There is also another problem with this approach: different devices prefer some data in different formats to run. The main example of this is texture compression. All PC hardware uses S3TC (BC) compression and that has been standardized for more than a decade, but mobile devices use different formats for texture compression, such as ETC1 and ETC2.

### Export menu

After many attempts at different export workflows, the current one has proven to work the best. At the time of this writing, not all platforms are supported yet, but the supported platforms continue to grow.

To open the export menu, click the **Export** button:

The export menu will open. However, it will be completely empty. This is because we need to add an export preset.

To create an export preset, click the **Add…** button at the top of the export menu. This will open a drop-down list of platforms to choose from for an export preset.

The default options are often enough to export, so tweaking them is usually not necessary. However, many platforms require additional tools (SDKs) to be installed to be able to export. Additionally, Godot needs export templates installed to create packages. The export menu will complain when something is missing and will not allow the user to export for that platform until they resolve it:

At that time, the user is expected to come back to the documentation and follow instructions on how to properly set up that platform.

The buttons at the bottom of the menu allow you to export the project in a few different ways:

- Export All: Export the project as a playable build (Godot executable and project data) for all the presets defined. All presets must have an **Export Path** defined for this to work.
- Export Project: Export the project as a playable build (Godot executable and project data) for the selected preset.
- Export PCK/ZIP: Export the project resources as a PCK or ZIP package. This is not a playable build, it only exports the project data without a Godot executable.

#### Export templates

Apart from setting up the platform, the export templates must be installed to be able to export projects. They can be obtained as a TPZ file (which is a renamed ZIP archive) from the [download page of the website](https://www.godotengine.org/download).

Once downloaded, they can be installed using the **Install Export Templates** option in the editor:

#### Resource options

When exporting, Godot makes a list of all the files to export and then creates the package. There are 5 different modes for exporting:

- Export all resources in the project
- Export selected scenes (and dependencies)
- Export selected resources (and dependencies)
- Export all resources in the project except resources checked below
- Export as dedicated server

**Export all resources in the project** will export every resource in the project. **Export selected scenes** and **Export selected resources** gives you a list of the scenes or resources in the project, and you have to select every scene or resource you want to export.

**Export all resources in the project except resources checked below** does exactly what it says, everything will be exported except for what you select in the list.

**Export as dedicated server** will remove all visuals from a project and replace them with a placeholder. This includes Cubemap, CubemapArray, Material, Mesh, Texture2D, Texture2DArray, Texture3D. You can also go into the list of files and specify specific visual resources that you do wish to keep.

> **Note:** Files and folders whose name begin with a period will never be included in the exported project. This is done to prevent version control folders like `.git` from being included in the exported PCK file.

Below the list of resources are two filters that can be setup. The first allows non-resource files such as `.txt`, `.json` and `.csv` to be exported with the project. The second filter can be used to exclude every file of a certain type without manually deselecting every one. For example, `.png` files.

### Configuration files

The export configuration is stored in two files that can both be found in the project directory:

- `export_presets.cfg`: This file contains the vast majority of the export configuration and can be safely committed to version control. There is nothing in here that you would normally have to keep secret.
- `.godot/export_credentials.cfg`: This file contains export options that are considered confidential, like passwords and encryption keys. It should generally **not** be committed to version control or shared with others unless you know exactly what you are doing.

Since the credentials file is usually kept out of version control systems, some export options will be missing if you clone the project to a new machine. The easiest way to deal with this is to copy the file manually from the old location to the new one.

### Exporting from the command line

In production, it is useful to automate builds, and Godot supports this with the `--export-release` and `--export-debug` command line parameters. Exporting from the command line still requires an export preset to define the export parameters. A basic invocation of the command would be:

```shell
godot --export-release "Windows Desktop" some_name.exe
```

This will export to `some_name.exe`, assuming there is a preset called "Windows Desktop" and the template can be found. (The export preset name must be written within quotes if it contains spaces or special characters.) The output path is _relative to the project path_ or _absolute_; **it does not respect the directory the command was invoked from**.

The output file extension should match the one used by the Godot export process:

- Windows: `.exe`
- macOS: `.app` or `.zip` (or `.dmg` when exporting _from_ macOS)
- Linux: Any extension (including none). `.x86_64` is typically used for 64-bit x86 binaries.
- HTML5: `.zip`
- Android: `.apk`
- iOS: `.zip`

You can also configure it to export _only_ the PCK or ZIP file, allowing a single exported main pack file to be used with multiple Godot executables. When doing so, the export preset name must still be specified on the command line:

```shell
godot --export-pack "Windows Desktop" some_name.pck
```

It is often useful to combine the `--export-release` flag with the `--path` flag, so that you do not need to `cd` to the project folder before running the command:

```shell
godot --path /path/to/project --export-release "Windows Desktop" some_name.exe
```

> **See also:** See [Command line tutorial](tutorials_editor.md) for more information about using Godot from the command line.

### PCK versus ZIP pack file formats

Each format has its upsides and downsides. PCK is the default and recommended format for most use cases, but you may want to use a ZIP archive instead depending on your needs.

**PCK format:**

- Uncompressed format. Larger file size, but faster to read/write.
- Not readable and writable using tools normally present on the user's operating system, even though there are [third-party tools](https://github.com/hhyyrylainen/GodotPckTool) to extract and create PCK files.

**ZIP format:**

- Compressed format. Smaller file size, but slower to read/write.
- Readable and writable using tools normally present on the user's operating system. This can be useful to make modding easier (see also Exporting packs, patches, and mods).

> **Warning:** Due to a [known bug](https://github.com/godotengine/godot/pull/42123), when using a ZIP file as a pack file, the exported binary will not try to use it automatically. Therefore, you have to create a _launcher script_ that the player can double-click or run from a terminal to launch the project: ```none
> :: launch.bat (Windows)
> @echo off
> my_project.exe --main-pack my_project.zip

# launch.sh (Linux)

./my_project.x86_64 --main-pack my_project.zip
```Save the launcher script and place it in the same folder as the exported binary. On Linux, make sure to give executable permissions to the launcher script using the command`chmod +x launch.sh`.

---

## Feature tags

### Introduction

Godot has a special system to tag availability of features. Each _feature_ is represented as a string, which can refer to many of the following:

- Platform name.
- Platform architecture (64-bit or 32-bit, x86 or ARM).
- Platform type (desktop, mobile, Web).
- Supported texture compression algorithms on the platform.
- Whether a build is `debug` or `release` (`debug` includes the editor).
- Whether the project is running from the editor or a "standalone" binary.
- Many more things.

Features can be queried at runtime from the singleton API by calling:

```gdscript
OS.has_feature(name)
```

OS feature tags are used by GDExtension to determine which libraries to load. For example, a library for `linux.debug.editor.x86_64` will be loaded only on a debug editor build for Linux x86_64.

### Default features

Here is a list of most feature tags in Godot. Keep in mind they are **case-sensitive**:

| Feature tag      | Description                                                                                                            |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------- |
| android          | Running on Android (but not within a Web browser)                                                                      |
| bsd              | Running on \*BSD (but not within a Web browser)                                                                        |
| linux            | Running on Linux (but not within a Web browser)                                                                        |
| macos            | Running on macOS (but not within a Web browser)                                                                        |
| ios              | Running on iOS (but not within a Web browser)                                                                          |
| visionos         | Running on visionOS (but not within a Web browser)                                                                     |
| windows          | Running on Windows                                                                                                     |
| linuxbsd         | Running on Linux or \*BSD                                                                                              |
| debug            | Running on a debug build (including the editor)                                                                        |
| release          | Running on a release build                                                                                             |
| editor           | Running on an editor build                                                                                             |
| editor_hint      | Running on an editor build, and inside the editor                                                                      |
| editor_runtime   | Running on an editor build, and running the project                                                                    |
| template         | Running on a non-editor (export template) build                                                                        |
| double           | Running on a double-precision build                                                                                    |
| single           | Running on a single-precision build                                                                                    |
| 64               | Running on a 64-bit build (any architecture)                                                                           |
| 32               | Running on a 32-bit build (any architecture)                                                                           |
| x86_64           | Running on a 64-bit x86 build                                                                                          |
| x86_32           | Running on a 32-bit x86 build                                                                                          |
| x86              | Running on an x86 build (any bitness)                                                                                  |
| arm64            | Running on a 64-bit ARM build                                                                                          |
| arm32            | Running on a 32-bit ARM build                                                                                          |
| arm              | Running on an ARM build (any bitness)                                                                                  |
| rv64             | Running on a 64-bit RISC-V build                                                                                       |
| riscv            | Running on a RISC-V build (any bitness)                                                                                |
| ppc64            | Running on a 64-bit PowerPC build                                                                                      |
| ppc32            | Running on a 32-bit PowerPC build                                                                                      |
| ppc              | Running on a PowerPC build (any bitness)                                                                               |
| wasm64           | Running on a 64-bit WebAssembly build (not yet possible)                                                               |
| wasm32           | Running on a 32-bit WebAssembly build                                                                                  |
| wasm             | Running on a WebAssembly build (any bitness)                                                                           |
| mobile           | Host OS is a mobile platform                                                                                           |
| pc               | Host OS is a PC platform (desktop/laptop)                                                                              |
| web              | Host OS is a Web browser                                                                                               |
| nothreads        | Running without threading support                                                                                      |
| threads          | Running with threading support                                                                                         |
| web_android      | Host OS is a Web browser running on Android                                                                            |
| web_ios          | Host OS is a Web browser running on iOS                                                                                |
| web_linuxbsd     | Host OS is a Web browser running on Linux or \*BSD                                                                     |
| web_macos        | Host OS is a Web browser running on macOS                                                                              |
| web_windows      | Host OS is a Web browser running on Windows                                                                            |
| etc              | Textures using ETC1 compression are supported                                                                          |
| etc2             | Textures using ETC2 compression are supported                                                                          |
| s3tc             | Textures using S3TC (DXT/BC) compression are supported                                                                 |
| movie            | Movie Maker mode is active                                                                                             |
| shader_baker     | Project was exported with shader baking enabled (only applies to the exported project, not when running in the editor) |
| dedicated_server | Project was exported as a dedicated server (only applies to the exported project, not when running in the editor)      |

> **Warning:** With the exception of texture compression, `web_<platform>` and `movie` feature tags, default feature tags are **immutable**. This means that they will _not_ change depending on runtime conditions. For example, `OS.has_feature("mobile")` will return `false` when running a project exported to Web on a mobile device. To check whether a project exported to Web is running on a mobile device, use `OS.has_feature("web_android") or OS.has_feature("web_ios")`.

### Custom features

It is possible to add custom features to a build; use the relevant field in the _export preset_ used to generate it:

> **Note:** Custom feature tags are only used when running the exported project (including with One-click deploy). They are **not used** when running the project from the editor, even if the export preset marked as **Runnable** for your current platform has custom feature tags defined. Custom feature tags are also not used in [EditorExportPlugin](../godot_gdscript_editor.md) scripts. Instead, feature tags in [EditorExportPlugin](../godot_gdscript_editor.md) will reflect the device the editor is currently running on.

### Overriding project settings

Features can be used to override specific configuration values in the _Project Settings_. This allows you to better customize any configuration when doing a build.

In the following example, a different icon is added for the demo build of the game (which was customized in a special export preset, which, in turn, includes only demo levels).

After overriding, a new field is added for this specific configuration.

> **Note:** When using the [project settings "override.cfg" functionality](../godot_gdscript_misc.md) (which is unrelated to feature tags), remember that feature tags still apply. Therefore, make sure to _also_ override the setting with the desired feature tag(s) if you want them to override base project settings on all platforms and configurations.

### Default overrides

There are already a lot of settings that come with overrides by default; they can be found in many sections of the project settings.

### Taking feature tags into account when reading project settings

By default, feature tags are **not** taken into account when reading project settings using the typical approaches ([ProjectSettings.get_setting](../godot_gdscript_filesystem.md) or [ProjectSettings.get](../godot_gdscript_filesystem.md)). Instead, you must use [ProjectSettings.get_setting_with_override](../godot_gdscript_filesystem.md).

For example, with the following project settings:

```gdscript
[section]

subsection/example = "Release"
subsection/example.debug = "Debug"
```

Using `ProjectSettings.get_setting("section/subsection/example")` will return `"Release"` regardless of whether a debug build is currently running. On the other hand, `ProjectSettings.get_setting_with_override("section/subsection/example")` will obey feature tags and will return `"Debug"` if using a debug build.

### Customizing the build

Feature tags can be used to customize a build process too, by writing a custom **ExportPlugin**. They are also used to specify which shared library is loaded and exported in **GDExtension**.

---
