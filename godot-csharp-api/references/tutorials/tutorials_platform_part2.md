# Godot 4 C# Tutorials — Platform (Part 2)

> 3 tutorials. C#-specific code examples.

## Custom HTML page for Web export

While Web export templates provide a default HTML page fully capable of launching the project without any further customization, it may be beneficial to create a custom HTML page. While the game itself cannot easily be directly controlled from the outside yet, such page allows to customize the initialization process for the engine.

Some use-cases where customizing the default page is useful include:

- Loading files from a different directory than the page;
- Loading a `.zip` file instead of a `.pck` file as the main pack;
- Loading the engine from a different directory than the main pack file;
- Adding a click-to-play button so that games can be started in the fullscreen mode;
- Loading some extra files before the engine starts, making them available in the project file system as soon as possible;
- Passing custom command line arguments, e.g. `-s` to start a `MainLoop` script.

The default HTML page is available in the Godot Engine repository at [/misc/dist/html/full-size.html](https://github.com/godotengine/godot/blob/master/misc/dist/html/full-size.html) but the following template can be used as a much simpler example:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>My Template</title>
        <meta charset="UTF-8" />
    </head>
    <body>
        <canvas id="canvas"></canvas>
        <script src="$GODOT_URL"></script>
        <script>
            var engine = new Engine($GODOT_CONFIG);
            engine.startGame();
        </script>
    </body>
</html>
```

### Setup

As shown by the example above, it is mostly a regular HTML document, with few placeholders which needs to be replaced during export, an html `<canvas>` element, and some simple JavaScript code that calls the Engine() class.

The only required placeholders are:

- `$GODOT_URL`: The name of the main JavaScript file, which provides the Engine() class required to start the engine and that must be included in the HTML as a `<script>`. The name is generated from the _Export Path_ during the export process.
- `$GODOT_CONFIG`: A JavaScript object, containing the export options and can be later overridden. See EngineConfig for the full list of overrides.

The following optional placeholders will enable some extra features in your custom HTML template.

- `$GODOT_PROJECT_NAME`: The project name as defined in the [Name](../godot_csharp_misc.md) setting in **Project Settings > Application > Config**. It is a good idea to use it as a `<title>` in your template.
- `$GODOT_HEAD_INCLUDE`: A custom string to include in the HTML document just before the end of the `<head>` tag. It is customized in the export options under the _Html / Head Include_ section. While you fully control the HTML page you create, this variable can be useful for configuring parts of the HTML `head` element from the Godot Editor, e.g. for different Web export presets.
- `$GODOT_SPLASH`: The path to the image used as the boot splash as defined in the [Image](../godot_csharp_resources.md) setting in **Project Settings > Application > Boot Splash**.
- `$GODOT_SPLASH_COLOR` The splash screen background color as defined in the [BG Color](../godot_csharp_misc.md) setting in **Project Settings > Application > Boot Splash**, converted to a hex color code.
- `$GODOT_SPLASH_CLASSES`: This placeholder provides a string of setting names and their values, which affect the splash screen. This string is meant to be used as a set of CSS class names, which allows styling the splash image based on the splash project settings. The following settings from **Project Settings > Application > Boot Splash** are provided, represented by the class names shown below depending on the setting's boolean value:

- [Show Image](../godot_csharp_misc.md): `show-image--true`, `show-image--false`
- [Stretch Mode](../godot_csharp_misc.md): `fullsize--true` (if **not** Disabled), `fullsize--false`
- [Use Filter](../godot_csharp_misc.md): `use-filter--true`, `use-filter--false`

When the custom page is ready, it can be selected in the export options under the _Html / Custom Html Shell_ section.

### Starting the project

To be able to start the game, you need to write a script that initializes the engine — the control code. This process consists of three steps, but as shown here, most of them can be skipped depending on how much customization is needed.

See the HTML5 shell class reference, for the full list of methods and options available.

First, the engine must be loaded, then it needs to be initialized, and after this the project can finally be started. You can perform every of these steps manually and with great control. However, in the simplest case all you need to do is to create an instance of the Engine() class with the exported configuration, and then call the engine.startGame method optionally overriding any EngineConfig parameters.

```js
const engine = new Engine($GODOT_CONFIG);
engine.startGame({
    /* optional override configuration, eg. */
    // unloadAfterInit: false,
    // canvasResizePolicy: 0,
    // ...
});
```

This snippet of code automatically loads and initializes the engine before starting the game. It uses the given configuration to load the engine. The engine.startGame method is asynchronous and returns a `Promise`. This allows your control code to track if the game was loaded correctly without blocking execution or relying on polling.

In case your project needs to have special control over the start arguments and dependency files, the engine.start method can be used instead. Note, that this method do not automatically preload the `pck` file, so you will probably want to manually preload it (and any other extra file) via the engine.preloadFile method.

Optionally, you can also manually engine.init to perform specific actions after the module initialization, but before the engine starts.

This process is a bit more complex, but gives you full control over the engine startup process.

```js
const myWasm = "mygame.wasm";
const myPck = "mygame.pck";
const engine = new Engine();
Promise.all([
    // Load and init the engine
    engine.init(myWasm),
    // And the pck concurrently
    engine.preloadFile(myPck),
])
    .then(() => {
        // Now start the engine.
        return engine.start({ args: ["--main-pack", myPck] });
    })
    .then(() => {
        console.log("Engine has started!");
    });
```

To load the engine manually the Engine.load() static method must be called. As this method is static, multiple engine instances can be spawned if the share the same `wasm`.

> **Note:** Multiple instances cannot be spawned by default, as the engine is immediately unloaded after it is initialized. To prevent this from happening see the unloadAfterInit override option. It is still possible to unload the engine manually afterwards by calling the Engine.unload() static method. Unloading the engine frees browser memory by unloading files that are no longer needed once the instance is initialized.

### Customizing the behavior

In the Web environment several methods can be used to guarantee that the game will work as intended.

If you target a specific version of WebGL, or just want to check if WebGL is available at all, you can call the Engine.isWebGLAvailable() method. It optionally takes an argument that allows to test for a specific major version of WebGL.

As the real executable file does not exist in the Web environment, the engine only stores a virtual filename formed from the base name of loaded engine files. This value affects the output of the [OS.get_executable_path()](../godot_csharp_misc.md) method and defines the name of the automatically started main pack. The executable override option can be used to override this value.

### Customizing the presentation

Several configuration options can be used to further customize the look and behavior of the game on your page.

By default, the first canvas element on the page is used for rendering. To use a different canvas element the canvas override option can be used. It requires a reference to the DOM element itself.

```js
const canvasElement = document.querySelector("#my-canvas-element");
engine.startGame({ canvas: canvasElement });
```

The way the engine resize the canvas can be configured via the canvasResizePolicy override option.

If your game takes some time to load, it may be useful to display a custom loading UI which tracks the progress. This can be achieved with the onProgress callback option, which allows to set up a callback function that will be called regularly as the engine loads new bytes.

```js
function printProgress(current, total) {
    console.log("Loaded " + current + " of " + total + " bytes");
}
engine.startGame({ onProgress: printProgress });
```

Be aware that in some cases `total` can be `0`. This means that it cannot be calculated.

If your game supports multiple languages, the locale override option can be used to force a specific locale, provided you have a valid language code string. It may be good to use server-side logic to determine which languages a user may prefer. This way the language code can be taken from the `Accept-Language` HTTP header, or determined by a GeoIP service.

### Debugging

To debug exported projects, it may be useful to read the standard output and error streams generated by the engine. This is similar to the output shown in the editor console window. By default, standard `console.log` and `console.warn` are used for the output and error streams respectively. This behavior can be customized by setting your own functions to handle messages.

Use the onPrint override option to set a callback function for the output stream, and the onPrintError override option to set a callback function for the error stream.

```js
function print(text) {
    console.log(text);
}
function printError(text) {
    console.warn(text);
}
engine.startGame({ onPrint: print, onPrintError: printError });
```

When handling the engine output, keep in mind that it may not be desirable to print it out in the finished product.

---

## HTML5 shell class reference

> **Work in progress:** The content of this page was not yet updated for Godot `4.6` and may be **outdated**. If you know how to improve this page or you can confirm that it's up to date, feel free to [open a pull request](https://github.com/godotengine/godot-docs).

Projects exported for the Web expose the **Engine()** class to the JavaScript environment, that allows fine control over the engine's start-up process.

This API is built in an asynchronous manner and requires basic understanding of [Promises](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises).

### Engine

The `Engine` class provides methods for loading and starting exported projects on the Web. For default export settings, this is already part of the exported HTML page. To understand practical use of the `Engine` class, see Custom HTML page for Web export.

#### Static Methods

| Promise | load ( string basePath ) |
| void | unload ( ) |
| boolean | isWebGLAvailable ( [ number majorVersion=1 ] ) |

#### Instance Methods

| Promise | init ( [ string basePath ] ) |
| Promise | preloadFile ( string\|ArrayBuffer file [, string path ] ) |
| Promise | start ( EngineConfig override ) |
| Promise | startGame ( EngineConfig override ) |
| void | copyToFS ( string path, ArrayBuffer buffer ) |
| void | requestQuit ( ) |

**class Engine(initConfig)**
: Create a new Engine instance with the given configuration.

**Arguments:**
: - **initConfig** (**EngineConfig()**) -- The initial config for this instance.

**Static Methods**

**Engine.load(basePath)**
: Load the engine from the specified base path.

**Arguments:**
: - **basePath** (`string()`) -- Base path of the engine to load.

**Returns:**
: A Promise that resolves once the engine is loaded.

**Return type:**
: Promise

**Engine.unload()**
: Unload the engine to free memory.

This method will be called automatically depending on the configuration. See **unloadAfterInit**.

**Engine.isWebGLAvailable([majorVersion=1])**
: Check whether WebGL is available. Optionally, specify a particular version of WebGL to check for.

**Arguments:**
: - **majorVersion** (`number()`) -- The major WebGL version to check for.

**Returns:**
: If the given major version of WebGL is available.

**Return type:**
: boolean

**Instance Methods**

**Engine.prototype.init([basePath])**
: Initialize the engine instance. Optionally, pass the base path to the engine to load it, if it hasn't been loaded yet. See **Engine.load()**.

**Arguments:**
: - **basePath** (`string()`) -- Base path of the engine to load.

**Returns:**
: A `Promise` that resolves once the engine is loaded and initialized.

**Return type:**
: Promise

**Engine.prototype.preloadFile(file[, path])**
: Load a file so it is available in the instance's file system once it runs. Must be called **before** starting the instance.

If not provided, the `path` is derived from the URL of the loaded file.

**Arguments:**
: - **file** (`string|ArrayBuffer()`) --

The file to preload.

If a `string` the file will be loaded from that path.

If an `ArrayBuffer` or a view on one, the buffer will used as the content of the file.

- **path** (`string()`) -- Path by which the file will be accessible. Required, if `file` is not a string.

**Returns:**
: A Promise that resolves once the file is loaded.

**Return type:**
: Promise

**Engine.prototype.start(override)**
: Start the engine instance using the given override configuration (if any). **startGame** can be used in typical cases instead.

This will initialize the instance if it is not initialized. For manual initialization, see **init**. The engine must be loaded beforehand.

Fails if a canvas cannot be found on the page, or not specified in the configuration.

**Arguments:**
: - **override** (**EngineConfig()**) -- An optional configuration override.

**Returns:**
: Promise that resolves once the engine started.

**Return type:**
: Promise

**Engine.prototype.startGame(override)**
: Start the game instance using the given configuration override (if any).

This will initialize the instance if it is not initialized. For manual initialization, see **init**.

This will load the engine if it is not loaded, and preload the main pck.

This method expects the initial config (or the override) to have both the **executable** and **mainPack** properties set (normally done by the editor during export).

**Arguments:**
: - **override** (**EngineConfig()**) -- An optional configuration override.

**Returns:**
: Promise that resolves once the game started.

**Return type:**
: Promise

**Engine.prototype.copyToFS(path, buffer)**
: Create a file at the specified `path` with the passed as `buffer` in the instance's file system.

**Arguments:**
: - **path** (`string()`) -- The location where the file will be created.

- **buffer** (`ArrayBuffer()`) -- The content of the file.

**Engine.prototype.requestQuit()**
: Request that the current instance quit.

This is akin the user pressing the close button in the window manager, and will have no effect if the engine has crashed, or is stuck in a loop.

### Engine configuration

An object used to configure the Engine instance based on godot export options, and to override those in custom HTML templates if needed.

#### Properties

| type | name |
| boolean | unloadAfterInit |
| HTMLCanvasElement | canvas |
| string | executable |
| string | mainPack |
| string | locale |
| number | canvasResizePolicy |
| Array.<string> | args |
| function | onExecute |
| function | onExit |
| function | onProgress |
| function | onPrint |
| function | onPrintError |

**EngineConfig**
: The Engine configuration object. This is just a typedef, create it like a regular object, e.g.:

`const MyConfig = { executable: 'godot', unloadAfterInit: false }`

**Property Descriptions**

**unloadAfterInit**
: Whether the unload the engine automatically after the instance is initialized.

**Type:**
: boolean

**Value:**
: `true`

**canvas**
: The HTML DOM Canvas object to use.

By default, the first canvas element in the document will be used is none is specified.

**Type:**
: HTMLCanvasElement

**Value:**
: `null`

**executable**
: The name of the WASM file without the extension. (Set by Godot Editor export process).

**Type:**
: string

**Value:**
: `""`

**mainPack**
: An alternative name for the game pck to load. The executable name is used otherwise.

**Type:**
: string

**Value:**
: `null`

**locale**
: Specify a language code to select the proper localization for the game.

The browser locale will be used if none is specified. See complete list of [supported locales](tutorials_i18n.md).

**Type:**
: string

**Value:**
: `null`

**canvasResizePolicy**
: The canvas resize policy determines how the canvas should be resized by Godot.

`0` means Godot won't do any resizing. This is useful if you want to control the canvas size from javascript code in your template.

`1` means Godot will resize the canvas on start, and when changing window size via engine functions.

`2` means Godot will adapt the canvas size to match the whole browser window.

**Type:**
: number

**Value:**
: `2`

**args**
: The arguments to be passed as command line arguments on startup.

See [command line tutorial](tutorials_editor.md).

**Note**: **startGame** will always add the `--main-pack` argument.

**Type:**
: Array.<string>

**Value:**
: `[]`

**onExecute(path, args)**
: A callback function for handling Godot's `OS.execute` calls.

This is for example used in the Web Editor template to switch between Project Manager and editor, and for running the game.

**Arguments:**
: - **path** (`string()`) -- The path that Godot's wants executed.

- **args** (`Array.`) -- The arguments of the "command" to execute.

**onExit(status_code)**
: A callback function for being notified when the Godot instance quits.

**Note**: This function will not be called if the engine crashes or become unresponsive.

**Arguments:**
: - **status_code** (`number()`) -- The status code returned by Godot on exit.

**onProgress(current, total)**
: A callback function for displaying download progress.

The function is called once per frame while downloading files, so the usage of `requestAnimationFrame()` is not necessary.

If the callback function receives a total amount of bytes as 0, this means that it is impossible to calculate. Possible reasons include:

- Files are delivered with server-side chunked compression
- Files are delivered with server-side compression on Chromium
- Not all file downloads have started yet (usually on servers without multi-threading)

**Arguments:**
: - **current** (`number()`) -- The current amount of downloaded bytes so far.

- **total** (`number()`) -- The total amount of bytes to be downloaded.

**onPrint([...var_args])**
: A callback function for handling the standard output stream. This method should usually only be used in debug pages.

By default, `console.log()` is used.

**Arguments:**
: - **var_args** (`*()`) -- A variadic number of arguments to be printed.

**onPrintError([...var_args])**
: A callback function for handling the standard error stream. This method should usually only be used in debug pages.

By default, `console.error()` is used.

**Arguments:**
: - **var_args** (`*()`) -- A variadic number of arguments to be printed as errors.

---

## The JavaScriptBridge singleton

In web builds, the [JavaScriptBridge](../godot_csharp_misc.md) singleton allows interaction with JavaScript and web browsers, and can be used to implement some functionalities unique to the web platform.

### Interacting with JavaScript

Sometimes, when exporting Godot for the Web, it might be necessary to interface with external JavaScript code like third-party SDKs, libraries, or simply to access browser features that are not directly exposed by Godot.

The `JavaScriptBridge` singleton provides methods to wrap a native JavaScript object into a Godot [JavaScriptObject](../godot_csharp_misc.md) that tries to feel natural in the context of Godot scripting (e.g. GDScript and C#).

The [JavaScriptBridge.get_interface()](../godot_csharp_misc.md) method retrieves an object in the global scope.

The [JavaScriptBridge.create_object()](../godot_csharp_misc.md) creates a new object via the JavaScript `new` constructor.

As you can see, by wrapping JavaScript objects into `JavaScriptObject` you can interact with them like they were native Godot objects, calling their methods, and retrieving (or even setting) their properties.

Base types (int, floats, strings, booleans) are automatically converted (floats might lose precision when converted from Godot to JavaScript). Anything else (i.e. objects, arrays, functions) are seen as `JavaScriptObjects` themselves.

### Callbacks

Calling JavaScript code from Godot is nice, but sometimes you need to call a Godot function from JavaScript instead.

This case is a bit more complicated. JavaScript relies on garbage collection, while Godot uses reference counting for memory management. This means you have to explicitly create callbacks (which are returned as `JavaScriptObjects` themselves) and you have to keep their reference.

Arguments passed by JavaScript to the callback will be passed as a single Godot `Array`.

> **Warning:** Callback methods created via [JavaScriptBridge.get_interface()](../godot_csharp_misc.md) (`_my_callback` in the above example) **must** take exactly one [Array](../godot_csharp_misc.md) argument, which is going to be the JavaScript [arguments object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments) converted to an array. Otherwise, the callback method will not be called.

Here is another example that asks the user for the [Notification permission](https://developer.mozilla.org/en-US/docs/Web/API/Notifications_API) and waits asynchronously to deliver a notification if the permission is granted:

### Can I use my favorite library?

You most likely can. First, you have to include your library in the page. You can customize the [Head Include](tutorials_export.md) during export (see below), or even write your own template.

In the example below, we customize the `Head Include` to add an external library ([axios](https://axios-http.com/)) from a content delivery network, and a second `<script>` tag to define our own custom function:

```html
<!-- Axios -->
<script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
<!-- Custom function -->
<script>
    function myFunc() {
        alert("My func!");
    }
</script>
```

We can then access both the library and the function from Godot, like we did in previous examples:

### The eval interface

The `eval` method works similarly to the JavaScript function of the same name. It takes a string as an argument and executes it as JavaScript code. This allows interacting with the browser in ways not possible with script languages integrated into Godot.

```csharp
private void MyFunc()
{
    JavaScriptBridge.Eval("alert('Calling JavaScript per C#!');")
}
```

The value of the last JavaScript statement is converted to a GDScript value and returned by `eval()` under certain circumstances:

- JavaScript `number` is returned as [float](../godot_csharp_misc.md)
- JavaScript `boolean` is returned as [bool](../godot_csharp_misc.md)
- JavaScript `string` is returned as [String](../godot_csharp_misc.md)
- JavaScript `ArrayBuffer`, `TypedArray`, and `DataView` are returned as [PackedByteArray](../godot_csharp_misc.md)

```csharp
private void MyFunc2()
{
    var jsReturn = JavaScriptBridge.Eval("var myNumber = 1; myNumber + 2;");
    GD.Print(jsReturn); // prints '3.0'
}
```

Any other JavaScript value is returned as `null`.

HTML5 export templates may be built without support for the singleton to improve security. With such templates, and on platforms other than HTML5, calling `JavaScriptBridge.eval` will also return `null`. The availability of the singleton can be checked with the `web` [feature tag](tutorials_export.md):

```csharp
private void MyFunc3()
{
    if (OS.HasFeature("web"))
    {
        JavaScriptBridge.Eval("console.log('The JavaScriptBridge singleton is available')");
    }
    else
    {
        GD.Print("The JavaScriptBridge singleton is NOT available");
    }
}
```

> **Tip:** GDScript's multi-line strings, surrounded by 3 quotes `"""` as in `my_func3()` above, are useful to keep JavaScript code readable.

The `eval` method also accepts a second, optional Boolean argument, which specifies whether to execute the code in the global execution context, defaulting to `false` to prevent polluting the global namespace:

```csharp
private void MyFunc4()
{
    // execute in global execution context,
    // thus adding a new JavaScript global variable `SomeGlobal`
    JavaScriptBridge.Eval("var SomeGlobal = {};", true);
}
```

### Downloading files

Downloading files (e.g. a save game) from the Godot Web export to the user's computer can be done by directly interacting with JavaScript, but given it is a very common use case, Godot exposes this functionality to scripting via a dedicated [JavaScriptBridge.download_buffer()](../godot_csharp_misc.md) function which lets you download any generated buffer.

Here is a minimal example on how to use it:

extends Node

And here is a more complete example on how to download a previously saved file:

---
