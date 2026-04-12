# Godot 4 GDScript Tutorials — Platform (Part 2)

> 6 tutorials. GDScript-specific code examples.

## Creating iOS plugins

> **Work in progress:** The content of this page was not yet updated for Godot `4.6` and may be **outdated**. If you know how to improve this page or you can confirm that it's up to date, feel free to [open a pull request](https://github.com/godotengine/godot-docs).

This page explains what iOS plugins can do for you, how to use an existing plugin, and the steps to code a new one.

iOS plugins allow you to use third-party libraries and support iOS-specific features like In-App Purchases, GameCenter integration, ARKit support, and more.

### Loading and using an existing plugin

An iOS plugin requires a `.gdip` configuration file, a binary file which can be either `.a` static library or `.xcframework` containing `.a` static libraries, and possibly other dependencies. To use it, you need to:

1. Copy the plugin's files to your Godot project's `res://ios/plugins` directory. You can also group files in a sub-directory, like `res://ios/plugins/my_plugin`.
2. The Godot editor automatically detects and imports `.gdip` files inside `res://ios/plugins` and its subdirectories.
3. You can find and activate detected plugins by going to Project -> Export... -> iOS and in the Options tab, scrolling to the Plugins section.

When a plugin is active, you can access it in your code using `Engine.get_singleton()`:

```gdscript
if Engine.has_singleton("MyPlugin"):
    var singleton = Engine.get_singleton("MyPlugin")
    print(singleton.foo())
```

> **Note:** The plugin's files have to be in the `res://ios/plugins/` directory or a subdirectory, otherwise the Godot editor will not automatically detect them.

### Creating an iOS plugin

At its core, a Godot iOS plugin is an iOS library (_.a_ archive file or _.xcframework_ containing static libraries) with the following requirements:

- The library must have a dependency on the Godot engine headers.
- The library must come with a `.gdip` configuration file.

An iOS plugin can have the same functionality as a Godot module but provides more flexibility and doesn't require to rebuild the engine.

Here are the steps to get a plugin's development started. We recommend using [Xcode](https://developer.apple.com/develop/) as your development environment.

> **See also:** The [Godot iOS Plugins](https://github.com/godotengine/godot-ios-plugins). The [Godot iOS plugin template](https://github.com/naithar/godot_ios_plugin) gives you all the boilerplate you need to get your iOS plugin started.

To build an iOS plugin:

1. Create an Objective-C static library for your plugin inside Xcode.
2. Add the Godot engine header files as a dependency for your plugin library in `HEADER_SEARCH_PATHS`. You can find the setting inside the `Build Settings` tab:

- Download the Godot engine source from the [Godot GitHub page](https://github.com/godotengine/godot).
- Run SCons to generate headers. You can learn the process by reading Compiling for iOS. You don't have to wait for compilation to complete to move forward as headers are generated before the engine starts to compile.
- You should use the same header files for iOS plugins and for the iOS export template.

3. In the `Build Settings` tab, specify the compilation flags for your static library in `OTHER_CFLAGS`. The most important ones are `-fcxx-modules`, `-fmodules`, and `-DDEBUG` if you need debug support. Other flags should be the same you use to compile Godot. For instance:

```gdscript
-DPTRCALL_ENABLED -DDEBUG_ENABLED -DDEBUG_MEMORY_ALLOC -DDISABLE_FORCED_INLINE -DTYPED_METHOD_BIND
```

1. Add the required logic for your plugin and build your library to generate a `.a` file. You will probably need to build both `debug` and `release` target `.a` files. Depending on your needs, pick either or both. If you need both debug and release `.a` files, their name should match following pattern: `[PluginName].[TargetType].a`. You can also build the static library with your SCons configuration.
2. The iOS plugin system also supports `.xcframework` files. To generate one, you can use a command such as:

```gdscript
xcodebuild -create-xcframework -library [DeviceLibrary].a -library [SimulatorLibrary].a -output [PluginName].xcframework
```

1. Create a Godot iOS Plugin configuration file to help the system detect and load your plugin:

- The configuration file extension must be `gdip` (e.g.: `MyPlugin.gdip`).
- The configuration file format is as follow:

```gdscript
[config]
    name="MyPlugin"
    binary="MyPlugin.a"

    initialization="init_my_plugin"
    deinitialization="deinit_my_plugin"

    [dependencies]
    linked=[]
    embedded=[]
    system=["Foundation.framework"]

    capabilities=["arkit", "metal"]

    files=["data.json"]

    linker_flags=["-ObjC"]

    [plist]
    PlistKeyWithDefaultType="Some Info.plist key you might need"
    StringPlistKey:string="String value"
    IntegerPlistKey:integer=42
    BooleanPlistKey:boolean=true
    RawPlistKey:raw="
    <array>
        <string>UIInterfaceOrientationPortrait</string>
    </array>
    "
    StringPlistKeyToInput:string_input="Type something"

The ``config`` section and fields are required and defined as follow:

    -   **name**: name of the plugin

    -   **binary**: this should be t
# ...
```

---

## Plugins for iOS

> **Work in progress:** The content of this page was not yet updated for Godot `4.6` and may be **outdated**. If you know how to improve this page or you can confirm that it's up to date, feel free to [open a pull request](https://github.com/godotengine/godot-docs).

Godot provides StoreKit, GameCenter, iCloud services and other plugins. They are using same model of asynchronous calls explained below.

ARKit and Camera access are also provided as plugins.

Latest updates, documentation and source code can be found at [Godot iOS plugins repository](https://github.com/godotengine/godot-ios-plugins)

### Accessing plugin singletons

To access plugin functionality, you first need to check that the plugin is exported and available by calling the Engine.has_singleton() function, which returns a registered singleton.

Here's an example of how to do this in GDScript:

```gdscript
var in_app_store
var game_center

func _ready():
    if Engine.has_singleton("InAppStore"):
        in_app_store = Engine.get_singleton("InAppStore")
    else:
        print("iOS IAP plugin is not available on this platform.")

    if Engine.has_singleton("GameCenter"):
        game_center = Engine.get_singleton("GameCenter")
    else:
        print("iOS Game Center plugin is not available on this platform.")
```

### Asynchronous methods

When requesting an asynchronous operation, the method will look like this:

```gdscript
Error purchase(Variant params);
```

The parameter will usually be a Dictionary, with the information necessary to make the request, and the call will have two phases. First, the method will immediately return an Error value. If the Error is not 'OK', the call operation is completed, with an error probably caused locally (no internet connection, API incorrectly configured, etc). If the error value is 'OK', a response event will be produced and added to the 'pending events' queue. Example:

```gdscript
func on_purchase_pressed():
    var result = in_app_store.purchase({ "product_id": "my_product" })
    if result == OK:
        animation.play("busy") # show the "waiting for response" animation
    else:
        show_error()

# put this on a 1 second timer or something
func check_events():
    while in_app_store.get_pending_event_count() > 0:
        var event = in_app_store.pop_pending_event()
        if event.type == "purchase":
            if event.result == "ok":
                show_success(event.product_id)
            else:
                show_error()
```

Remember that when a call returns OK, the API will _always_ produce an event through the pending_event interface, even if it's an error, or a network timeout, etc. You should be able to, for example, safely block the interface waiting for a reply from the server. If any of the APIs don't behave this way it should be treated as a bug.

The pending event interface consists of two methods:

- `get_pending_event_count()` Returns the number of pending events on the queue.
- `Variant pop_pending_event()` Pops the first event from the queue and returns it.

### Store Kit

Implemented in [Godot iOS InAppStore plugin](https://github.com/godotengine/godot-ios-plugins/blob/master/plugins/inappstore/in_app_store.mm).

The Store Kit API is accessible through the `InAppStore` singleton. It is initialized automatically.

The following methods are available and documented below:

```gdscript
Error purchase(Variant params)
   Error request_product_info(Variant params)
   Error restore_purchases()
   void set_auto_finish_transaction(bool enable)
   void finish_transaction(String product_id)

and the pending events interface:

::

   int get_pending_event_count()
   Variant pop_pending_event()
```

#### purchase

Purchases a product ID through the Store Kit API. You have to call `finish_transaction(product_id)` once you receive a successful response or call `set_auto_finish_transaction(true)` prior to calling `purchase()`. These two methods ensure the transaction is completed.

##### Parameters

Takes a dictionary as a parameter, with one field, `product_id`, a string with your product ID. Example:

```gdscript
var result = in_app_store.purchase({ "product_id": "my_product" })
```

##### Response event

The response event will be a dictionary with the following fields:

On error:

```gdscript
{
  "type": "purchase",
  "result": "error",
  "product_id": "the product ID requested",
}
```

On success:

```gdscript
{
  "type": "purchase",
  "result": "ok",
  "product_id": "the product ID requested",
}
```

#### request_product_info

Requests the product info on a list of product IDs.

##### Parameters

Takes a dictionary as a parameter, with a single `product_ids` key to which a string array of product IDs is assigned. Example:

```gdscript
var result = in_app_store.request_product_info({ "product_ids": ["my_product1", "my_product2"] })
```

##### Response event

The response event will be a dictionary with the following fields:

```gdscript
{
  "type": "product_info",
  "result": "ok",
  "invalid_ids": [ list of requested IDs that were invalid ],
  "ids": [ list of IDs that were valid ],
  "titles": [ list of valid product titles (corresponds with list of valid IDs) ],
  "descriptions": [ list of valid product descriptions ],
  "prices": [ list of valid product prices ],
  "localized_prices": [ list of valid product localized prices ],
}
```

#### restore_purchases

Restores previously made purchases on user's account. This will create response events for each previously purchased product ID.

##### Response event

The response events will be dictionaries with the following fields:

```gdscript
{
  "type": "restore",
  "result": "ok",
  "product_id": "product ID of restored purchase",
}
```

#### set_auto_finish_transaction

If set to `true`, once a purchase is successful, your purchase will be finalized automatically. Call this method prior to calling `purchase()`.

##### Parameters

Takes a boolean as a parameter which specifies if purchases should be automatically finalized. Example:

```gdscript
in_app_store.set_auto_finish_transaction(true)
```

#### finish_transaction

If you don't want transactions to be automatically finalized, call this method after you receive a successful purchase response.

##### Parameters

Takes a string `product_id` as an argument. `product_id` specifies what product to finalize the purchase on. Example:

```gdscript
in_app_store.finish_transaction("my_product1")
```

### Game Center

Implemented in [Godot iOS GameCenter plugin](https://github.com/godotengine/godot-ios-plugins/blob/master/plugins/gamecenter/game_center.mm).

The Game Center API is available through the `GameCenter` singleton. It has the following methods:

```gdscript
Error authenticate()
bool is_authenticated()
Error post_score(Variant score)
Error award_achievement(Variant params)
void reset_achievements()
void request_achievements()
void request_achievement_descriptions()
Error show_game_center(Variant params)
Error request_identity_verification_signature()
```

and the pending events interface:

```gdscript
int get_pending_event_count()
Variant pop_pending_event()
```

#### authenticate

Authenticates a user in Game Center.

##### Response event

The response event will be a dictionary with the following fields:

On error:

```gdscript
{
  "type": "authentication",
  "result": "error",
  "error_code": the value from NSError::code,
  "error_description": the value from NSError::localizedDescription,
}
```

On success:

```gdscript
{
  "type": "authentication",
  "result": "ok",
  "player_id": the value from GKLocalPlayer::playerID,
}
```

#### post_score

Posts a score to a Game Center leaderboard.

##### Parameters

Takes a dictionary as a parameter, with two fields:

- `score` a float number
- `category` a string with the category name

Example:

```gdscript
var result = game_center.post_score({ "score": 100, "category": "my_leaderboard", })
```

##### Response event

The response event will be a dictionary with the following fields:

On error:

```gdscript
{
  "type": "post_score",
  "result": "error",
  "error_code": the value from NSError::code,
  "error_description": the value from NSError::localizedDescription,
}
```

On success:

```gdscript
{
  "type": "post_score",
  "result": "ok",
}
```

#### award_achievement

Modifies the progress of a Game Center achievement.

##### Parameters

Takes a Dictionary as a parameter, with 3 fields:

- `name` (string) the achievement name
- `progress` (float) the achievement progress from 0.0 to 100.0 (passed to `GKAchievement::percentComplete`)
- `show_completion_banner` (bool) whether Game Center should display an achievement banner at the top of the screen

Example:

```gdscript
var result = award_achievement({ "name": "hard_mode_completed", "progress": 6.1 })
```

##### Response event

The response event will be a dictionary with the following fields:

On error:

```gdscript
{
  "type": "award_achievement",
  "result": "error",
  "error_code": the error code taken from NSError::code,
}
```

On success:

```gdscript
{
  "type": "award_achievement",
  "result": "ok",
}
```

#### reset_achievements

Clears all Game Center achievements. The function takes no parameters.

##### Response event

The response event will be a dictionary with the following fields:

On error:

```gdscript
{
  "type": "reset_achievements",
  "result": "error",
  "error_code": the value from NSError::code,
}
```

On success:

```gdscript
{
  "type": "reset_achievements",
  "result": "ok",
}
```

#### request_achievements

Request all the Game Center achievements the player has made progress on. The function takes no parameters.

##### Response event

The response event will be a dictionary with the following fields:

On error:

```gdscript
{
  "type": "achievements",
  "result": "error",
  "error_code": the value from NSError::code,
}
```

On success:

```gdscript
{
  "type": "achievements",
  "result": "ok",
  "names": [ list of the name of each achievement ],
  "progress": [ list of the progress made on each achievement ],
}
```

#### request_achievement_descriptions

Request the descriptions of all existing Game Center achievements regardless of progress. The function takes no parameters.

##### Response event

The response event will be a dictionary with the following fields:

On error:

```gdscript
{
  "type": "achievement_descriptions",
  "result": "error",
  "error_code": the value from NSError::code,
}
```

On success:

```gdscript
{
  "type": "achievement_descriptions",
  "result": "ok",
  "names": [ list of the name of each achievement ],
  "titles": [ list of the title of each achievement ],
  "unachieved_descriptions": [ list of the description of each achievement when it is unachieved ],
  "achieved_descriptions": [ list of the description of each achievement when it is achieved ],
  "maximum_points": [ list of the points earned by completing each achievement ],
  "hidden": [ list of booleans indicating whether each achievement is initially visible ],
  "replayable": [ list of booleans indicating whether each achievement can be earned more than once ],
}
```

#### show_game_center

Displays the built-in Game Center overlay showing leaderboards, achievements, and challenges.

##### Parameters

Takes a Dictionary as a parameter, with two fields:

- `view` (string) (optional) the name of the view to present. Accepts "default", "leaderboards", "achievements", or "challenges". Defaults to "default".
- `leaderboard_name` (string) (optional) the name of the leaderboard to present. Only used when "view" is "leaderboards" (or "default" is configured to show leaderboards). If not specified, Game Center will display the aggregate leaderboard.

Examples:

```gdscript
var result = show_game_center({ "view": "leaderboards", "leaderboard_name": "best_time_leaderboard" })
var result = show_game_center({ "view": "achievements" })
```

##### Response event

The response event will be a dictionary with the following fields:

On close:

```gdscript
{
  "type": "show_game_center",
  "result": "ok",
}
```

---

## Wayland/X11

### Overview

One of the important components of any operating system is its display server. Windows and MacOS only provide one option, Linux however has two, X11 and Wayland.

X11 is an older standard and is currently being gradually phased out by the majority of linux distributions in favor of supporting Wayland, which has been developed as a replacement. Applications running on X11 can still work when a distribution is using Wayland thanks to a compatibility layer known as Xwayland.

Godot's support is still a work in progress, so for now X11 remains the default setting for game projects, that will likely change in a future version.

### When to use Wayland

If you're an engine developer who wants to help improve support, or if you think Xwayland might be causing visual glitches in your exported project for whatever reason, then we would recommend using Wayland. But outside of that it's recommended to stick with X11 for now. It's important to note that while X11 applications can run on Wayland, the reverse is not true.

As of January 2026 most popular distributions are using Wayland by default, including, but not limited to, the following:

- SteamOS
- Bazzite
- CachyOS
- Fedora
- Fedora Silverblue
- Ubuntu
- OpenSuse

Keep in mind that for some distributions, like Ubuntu, users may have changed the display server to X11 manually themselves.

### Changing the setting

To change your display server to Wayland click on Project > project settings, from here, go to Display Server and change the driver.linuxbsd option to `wayland`.

### Disabling Libdecor loading

Libdecor loading on Wayland has some quirks and it may be useful to disable it depending on your situation. To do that you need to set the `GODOT_WAYLAND_DISABLE_LIBDECOR` environment variable to `1` like this:

```gdscript
OS.set_environment("GODOT_WAYLAND_DISABLE_LIBDECOR", "1")
```

---

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

- `$GODOT_PROJECT_NAME`: The project name as defined in the [Name](../godot_gdscript_misc.md) setting in **Project Settings > Application > Config**. It is a good idea to use it as a `<title>` in your template.
- `$GODOT_HEAD_INCLUDE`: A custom string to include in the HTML document just before the end of the `<head>` tag. It is customized in the export options under the _Html / Head Include_ section. While you fully control the HTML page you create, this variable can be useful for configuring parts of the HTML `head` element from the Godot Editor, e.g. for different Web export presets.
- `$GODOT_SPLASH`: The path to the image used as the boot splash as defined in the [Image](../godot_gdscript_resources.md) setting in **Project Settings > Application > Boot Splash**.
- `$GODOT_SPLASH_COLOR` The splash screen background color as defined in the [BG Color](../godot_gdscript_misc.md) setting in **Project Settings > Application > Boot Splash**, converted to a hex color code.
- `$GODOT_SPLASH_CLASSES`: This placeholder provides a string of setting names and their values, which affect the splash screen. This string is meant to be used as a set of CSS class names, which allows styling the splash image based on the splash project settings. The following settings from **Project Settings > Application > Boot Splash** are provided, represented by the class names shown below depending on the setting's boolean value:

- [Show Image](../godot_gdscript_misc.md): `show-image--true`, `show-image--false`
- [Stretch Mode](../godot_gdscript_misc.md): `fullsize--true` (if **not** Disabled), `fullsize--false`
- [Use Filter](../godot_gdscript_misc.md): `use-filter--true`, `use-filter--false`

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

As the real executable file does not exist in the Web environment, the engine only stores a virtual filename formed from the base name of loaded engine files. This value affects the output of the [OS.get_executable_path()](../godot_gdscript_misc.md) method and defines the name of the automatically started main pack. The executable override option can be used to override this value.

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

In web builds, the [JavaScriptBridge](../godot_gdscript_misc.md) singleton allows interaction with JavaScript and web browsers, and can be used to implement some functionalities unique to the web platform.

### Interacting with JavaScript

Sometimes, when exporting Godot for the Web, it might be necessary to interface with external JavaScript code like third-party SDKs, libraries, or simply to access browser features that are not directly exposed by Godot.

The `JavaScriptBridge` singleton provides methods to wrap a native JavaScript object into a Godot [JavaScriptObject](../godot_gdscript_misc.md) that tries to feel natural in the context of Godot scripting (e.g. GDScript and C#).

The [JavaScriptBridge.get_interface()](../godot_gdscript_misc.md) method retrieves an object in the global scope.

```gdscript
extends Node

func _ready():
    # Retrieve the `window.console` object.
    var console = JavaScriptBridge.get_interface("console")
    # Call the `window.console.log()` method.
    console.log("test")
```

The [JavaScriptBridge.create_object()](../godot_gdscript_misc.md) creates a new object via the JavaScript `new` constructor.

```gdscript
extends Node

func _ready():
    # Call the JavaScript `new` operator on the `window.Array` object.
    # Passing 10 as argument to the constructor:
    # JS: `new Array(10);`
    var arr = JavaScriptBridge.create_object("Array", 10)
    # Set the first element of the JavaScript array to the number 42.
    arr[0] = 42
    # Call the `pop` function on the JavaScript array.
    arr.pop()
    # Print the value of the `length` property of the array (9 after the pop).
    print(arr.length)
```

As you can see, by wrapping JavaScript objects into `JavaScriptObject` you can interact with them like they were native Godot objects, calling their methods, and retrieving (or even setting) their properties.

Base types (int, floats, strings, booleans) are automatically converted (floats might lose precision when converted from Godot to JavaScript). Anything else (i.e. objects, arrays, functions) are seen as `JavaScriptObjects` themselves.

### Callbacks

Calling JavaScript code from Godot is nice, but sometimes you need to call a Godot function from JavaScript instead.

This case is a bit more complicated. JavaScript relies on garbage collection, while Godot uses reference counting for memory management. This means you have to explicitly create callbacks (which are returned as `JavaScriptObjects` themselves) and you have to keep their reference.

Arguments passed by JavaScript to the callback will be passed as a single Godot `Array`.

```gdscript
extends Node

# Here we create a reference to the `_my_callback` function (below).
# This reference will be kept until the node is freed.
var _callback_ref = JavaScriptBridge.create_callback(_my_callback)

func _ready():
    # Get the JavaScript `window` object.
    var window = JavaScriptBridge.get_interface("window")
    # Set the `window.onbeforeunload` DOM event listener.
    window.onbeforeunload = _callback_ref

func _my_callback(args):
    # Get the first argument (the DOM event in our case).
    var js_event = args[0]
    # Call preventDefault and set the `returnValue` property of the DOM event.
    js_event.preventDefault()
    js_event.returnValue = ''
```

> **Warning:** Callback methods created via [JavaScriptBridge.get_interface()](../godot_gdscript_misc.md) (`_my_callback` in the above example) **must** take exactly one [Array](../godot_gdscript_misc.md) argument, which is going to be the JavaScript [arguments object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments) converted to an array. Otherwise, the callback method will not be called.

Here is another example that asks the user for the [Notification permission](https://developer.mozilla.org/en-US/docs/Web/API/Notifications_API) and waits asynchronously to deliver a notification if the permission is granted:

```gdscript
extends Node

# Here we create a reference to the `_on_permissions` function (below).
# This reference will be kept until the node is freed.
var _permission_callback = JavaScriptBridge.create_callback(_on_permissions)

func _ready():
    # NOTE: This is done in `_ready` for simplicity, but SHOULD BE done in response
    # to user input instead (e.g. during `_input`, or `button_pressed` event, etc.),
    # otherwise it might not work.

    # Get the `window.Notification` JavaScript object.
    var notification = JavaScriptBridge.get_interface("Notification")
    # Call the `window.Notification.requestPermission` method which returns a JavaScript
    # Promise, and bind our callback to it.
    notification.requestPermission().then(_permission_callback)

func _on_permissions(args):
    # The
# ...
```

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

```gdscript
extends Node

# Here create a reference to the `_on_get` function (below).
# This reference will be kept until the node is freed.
var _callback = JavaScriptBridge.create_callback(_on_get)

func _ready():
    # Get the `window` object, where globally defined functions are.
    var window = JavaScriptBridge.get_interface("window")
    # Call the JavaScript `myFunc` function defined in the custom HTML head.
    window.myFunc()
    # Get the `axios` library (loaded from a CDN in the custom HTML head).
    var axios = JavaScriptBridge.get_interface("axios")
    # Make a GET request to the current location, and receive the callback when done.
    axios.get(window.location.toString()).then(_callback)

func _on_get(args):
    OS.alert("On Get")
```

### The eval interface

The `eval` method works similarly to the JavaScript function of the same name. It takes a string as an argument and executes it as JavaScript code. This allows interacting with the browser in ways not possible with script languages integrated into Godot.

```gdscript
func my_func():
    JavaScriptBridge.eval("alert('Calling JavaScript per GDScript!');")
```

The value of the last JavaScript statement is converted to a GDScript value and returned by `eval()` under certain circumstances:

- JavaScript `number` is returned as [float](../godot_gdscript_misc.md)
- JavaScript `boolean` is returned as [bool](../godot_gdscript_misc.md)
- JavaScript `string` is returned as [String](../godot_gdscript_misc.md)
- JavaScript `ArrayBuffer`, `TypedArray`, and `DataView` are returned as [PackedByteArray](../godot_gdscript_misc.md)

```gdscript
func my_func2():
    var js_return = JavaScriptBridge.eval("var myNumber = 1; myNumber + 2;")
    print(js_return) # prints '3.0'
```

Any other JavaScript value is returned as `null`.

HTML5 export templates may be built without support for the singleton to improve security. With such templates, and on platforms other than HTML5, calling `JavaScriptBridge.eval` will also return `null`. The availability of the singleton can be checked with the `web` [feature tag](tutorials_export.md):

```gdscript
func my_func3():
    if OS.has_feature('web'):
        JavaScriptBridge.eval("""
            console.log('The JavaScriptBridge singleton is available')
        """)
    else:
        print("The JavaScriptBridge singleton is NOT available")
```

> **Tip:** GDScript's multi-line strings, surrounded by 3 quotes `"""` as in `my_func3()` above, are useful to keep JavaScript code readable.

The `eval` method also accepts a second, optional Boolean argument, which specifies whether to execute the code in the global execution context, defaulting to `false` to prevent polluting the global namespace:

```gdscript
func my_func4():
    # execute in global execution context,
    # thus adding a new JavaScript global variable `SomeGlobal`
    JavaScriptBridge.eval("var SomeGlobal = {};", true)
```

### Downloading files

Downloading files (e.g. a save game) from the Godot Web export to the user's computer can be done by directly interacting with JavaScript, but given it is a very common use case, Godot exposes this functionality to scripting via a dedicated [JavaScriptBridge.download_buffer()](../godot_gdscript_misc.md) function which lets you download any generated buffer.

Here is a minimal example on how to use it:

extends Node

```gdscript
func _ready():
    # Asks the user download a file called "hello.txt" whose content will be the string "Hello".
    JavaScriptBridge.download_buffer("Hello".to_utf8_buffer(), "hello.txt")
```

And here is a more complete example on how to download a previously saved file:

```gdscript
extends Node

# Open a file for reading and download it via the JavaScript singleton.
func _download_file(path):
    var file = FileAccess.open(path, FileAccess.READ)
    if file == null:
        push_error("Failed to load file")
        return
    # Get the file name.
    var fname = path.get_file()
    # Read the whole file to memory.
    var buffer = file.get_buffer(file.get_len())
    # Prompt the user to download the file (will have the same name as the input file).
    JavaScriptBridge.download_buffer(buffer, fname)

func _ready():
    # Create a temporary file.
    var config = ConfigFile.new()
    config.set_value("option", "one", false)
    config.save("/tmp/test.cfg")

    # Download it
    _download_file("/tmp/test.cfg")
```

---
