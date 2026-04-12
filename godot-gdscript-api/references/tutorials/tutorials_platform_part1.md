# Godot 4 GDScript Tutorials — Platform (Part 1)

> 5 tutorials. GDScript-specific code examples.

## Android in-app purchases

Godot offers a first-party `GodotGooglePlayBilling` Android plugin compatible with Godot 4.2+ which uses the [Google Play Billing library](https://developer.android.com/google/play/billing).

### Usage

#### Getting started

Make sure you have enabled and successfully set up [Android Gradle Builds](tutorials_export.md). Follow the installation instructions on the `GodotGooglePlayBilling` [github page](https://github.com/godotengine/godot-google-play-billing).

#### Initialize the plugin

To use the `GodotGooglePlayBilling` API:

1. Access the `BillingClient`.
2. Connect to its signals to receive billing results.
3. Call `start_connection`.

Initialization example:

```gdscript
var billing_client: BillingClient
func _ready():
    billing_client = BillingClient.new()
    billing_client.connected.connect(_on_connected) # No params
    billing_client.disconnected.connect(_on_disconnected) # No params
    billing_client.connect_error.connect(_on_connect_error) # response_code: int, debug_message: String
    billing_client.query_product_details_response.connect(_on_query_product_details_response) # response: Dictionary
    billing_client.query_purchases_response.connect(_on_query_purchases_response) # response: Dictionary
    billing_client.on_purchase_updated.connect(_on_purchase_updated) # response: Dictionary
    billing_client.consume_purchase_response.connect(_on_consume_purchase_response) # response: Dictionary
    billing_client.acknowledge_purchase_response.co
# ...
```

The API must be in a connected state prior to use. The `connected` signal is sent when the connection process succeeds. You can also use `is_ready()` to determine if the plugin is ready for use. The `get_connection_state()` function returns the current connection state of the plugin.

Return values for `get_connection_state()`:

```gdscript
# Matches BillingClient.ConnectionState in the Play Billing Library.
# Access in your script as: BillingClient.ConnectionState.CONNECTED
enum ConnectionState {
    DISCONNECTED, # This client was not yet connected to billing service or was already closed.
    CONNECTING, # This client is currently in process of connecting to billing service.
    CONNECTED, # This client is currently connected to billing service.
    CLOSED, # This client was already closed and shouldn't be used again.
}
```

#### Query available items

Once the API has connected, query product IDs using query_product_details(). You must successfully complete a product details query before calling the `purchase()`, `purchase_subscription()`, or `update_subscription()` functions, or they will return an error. `query_product_details()` takes two parameters: an array of product ID strings and the type of product being queried. The product type should be `BillingClient.ProductType.INAPP` for normal in-app purchases or `BillingClient.ProductType.SUBS` for subscriptions. The ID strings in the array should match the product IDs defined in the Google Play Console entry for your app.

Example use of `query_product_details()`:

```gdscript
func _on_connected():
  billing_client.query_product_details(["my_iap_item"], BillingClient.ProductType.INAPP) # BillingClient.ProductType.SUBS for subscriptions.

func _on_query_product_details_response(query_result: Dictionary):
    if query_result.response_code == BillingClient.BillingResponseCode.OK:
        print("Product details query success")
        for available_product in query_result.product_details:
            print(available_product)
    else:
        print("Product details query failed")
        print("response_code: ", query_result.response_code, "debug_message: ", query_result.debug_message)
```

#### Query user purchases

To retrieve a user's purchases, call the `query_purchases()` function passing a product type to query. The product type should be `BillingClient.ProductType.INAPP` for normal in-app purchases or `BillingClient.ProductType.SUBS` for subscriptions. The `query_purchases_response` signal is sent with the result. The signal has a single parameter: a [Dictionary](../godot_gdscript_misc.md) with a response code and either an array of purchases or a debug message. Only active subscriptions and non-consumed one-time purchases are included in the purchase array.

Example use of `query_purchases()`:

```gdscript
func _query_purchases():
    billing_client.query_purchases(BillingClient.ProductType.INAPP) # Or BillingClient.ProductType.SUBS for subscriptions.

func _on_query_purchases_response(query_result: Dictionary):
    if query_result.response_code == BillingClient.BillingResponseCode.OK:
        print("Purchase query success")
        for purchase in query_result.purchases:
            _process_purchase(purchase)
    else:
        print("Purchase query failed")
        print("response_code: ", query_result.response_code, "debug_message: ", query_result.debug_message)
```

#### Purchase an item

To launch the billing flow for an item: Use `purchase()` for in-app products, passing the product ID string. Use `purchase_subscription()` for subscriptions, passing the product ID and base plan ID. You may also optionally provide an offer ID.

For both `purchase()` and `purchase_subscription()`, you can optionally pass a boolean to indicate whether offers are [personallised](https://developer.android.com/google/play/billing/integrate#personalized-price)

Reminder: you **must** query the product details for an item before you can pass it to `purchase()`. This method returns a dictionary indicating whether the billing flow was successfully launched. It includes a response code and either an array of purchases or a debug message.

Example use of `purchase()`:

```gdscript
var result = billing_client.purchase("my_iap_item")
if result.response_code == BillingClient.BillingResponseCode.OK:
    print("Billing flow launch success")
else:
    print("Billing flow launch failed")
    print("response_code: ", result.response_code, "debug_message: ", result.debug_message)
```

The result of the purchase will be sent through the `on_purchases_updated` signal.

```gdscript
func _on_purchases_updated(result: Dictionary):
    if result.response_code == BillingClient.BillingResponseCode.OK:
        print("Purchase update received")
        for purchase in result.purchases:
            _process_purchase(purchase)
    else:
        print("Purchase update error")
        print("response_code: ", result.response_code, "debug_message: ", result.debug_message)
```

#### Processing a purchase item

The `query_purchases_response` and `on_purchases_updated` signals provide an array of purchases in [Dictionary](../godot_gdscript_misc.md) format. The purchase Dictionary includes keys that map to values of the Google Play Billing [Purchase](https://developer.android.com/reference/com/android/billingclient/api/Purchase) class.

Purchase fields:

```gdscript
order_id: String
purchase_token: String
package_name: String
purchase_state: int
purchase_time: int (milliseconds since the epoch (Jan 1, 1970))
original_json: String
is_acknowledged: bool
is_auto_renewing: bool
quantity: int
signature: String
product_ids: PackedStringArray
```

#### Check purchase state

Check the `purchase_state` value of a purchase to determine if a purchase was completed or is still pending.

PurchaseState values:

```gdscript
# Matches Purchase.PurchaseState in the Play Billing Library
# Access in your script as: BillingClient.PurchaseState.PURCHASED
enum PurchaseState {
    UNSPECIFIED,
    PURCHASED,
    PENDING,
}
```

If a purchase is in a `PENDING` state, you should not award the contents of the purchase or do any further processing of the purchase until it reaches the `PURCHASED` state. If you have a store interface, you may wish to display information about pending purchases needing to be completed in the Google Play Store. For more details on pending purchases, see [Handling pending transactions](https://developer.android.com/google/play/billing/integrate#pending) in the Google Play Billing Library documentation.

#### Consumables

If your in-app item is not a one-time purchase but a consumable item (e.g. coins) which can be purchased multiple times, you can consume an item by calling `consume_purchase()` passing the `purchase_token` value from the purchase dictionary. Calling `consume_purchase()` automatically acknowledges a purchase. Consuming a product allows the user to purchase it again, it will no longer appear in subsequent `query_purchases()` calls unless it is repurchased.

Example use of `consume_purchase()`:

```gdscript
func _process_purchase(purchase):
    if "my_consumable_iap_item" in purchase.product_ids and purchase.purchase_state == BillingClient.PurchaseState.PURCHASED:
        # Add code to store payment so we can reconcile the purchase token
        # in the completion callback against the original purchase
        billing_client.consume_purchase(purchase.purchase_token)

func _on_consume_purchase_response(result: Dictionary):
    if result.response_code == BillingClient.BillingResponseCode.OK:
        print("Consume purchase success")
        _handle_purchase_token(result.token, true)
    else:
        print("Consume purchase failed")
        print("response_code: ", result.response_code, "debug_message: ", result.debug_message, "purchase_token: ", result.token)

# Find the product associated wi
# ...
```

#### Acknowledging purchases

If your in-app item is a one-time purchase, you must acknowledge the purchase by calling the `acknowledge_purchase()` function, passing the `purchase_token` value from the purchase dictionary. If you do not acknowledge a purchase within three days, the user automatically receives a refund, and Google Play revokes the purchase. If you are calling `comsume_purchase()` it automatically acknowledges the purchase and you do not need to call `acknowledge_purchase()`.

Example use of `acknowledge_purchase()`:

```gdscript
func _process_purchase(purchase):
    if "my_one_time_iap_item" in purchase.product_ids and \
            purchase.purchase_state == BillingClient.PurchaseState.PURCHASED and \
            not purchase.is_acknowledged:
        # Add code to store payment so we can reconcile the purchase token
        # in the completion callback against the original purchase
        billing_client.acknowledge_purchase(purchase.purchase_token)

func _on_acknowledge_purchase_response(result: Dictionary):
    if result.response_code == BillingClient.BillingResponseCode.OK:
        print("Acknowledge purchase success")
        _handle_purchase_token(result.token, true)
    else:
        print("Acknowledge purchase failed")
        print("response_code: ", result.response_code, "debug_message: ", result.debug_m
# ...
```

#### Subscriptions

Subscriptions work mostly like regular in-app items. Use `BillingClient.ProductType.SUBS` as the second argument to `query_product_details()` to get subscription details. Pass `BillingClient.ProductType.SUBS` to `query_purchases()` to get subscription purchase details.

You can check `is_auto_renewing` in the a subscription purchase returned from `query_purchases()` to see if a user has cancelled an auto-renewing subscription.

You need to acknowledge new subscription purchases, but not automatic subscription renewals.

If you support upgrading or downgrading between different subscription levels, you should use `update_subscription()` to use the subscription update flow to change an active subscription. Like `purchase()`, results are returned by the `on_purchases_updated` signal. These are the parameters of `update_subscription()`:

1. old_purchase_token: The purchase token of the currently active subscription
2. replacement_mode: The replacement mode to apply to the subscription
3. product_id: The product ID of the new subscription to switch to
4. base_plan_id: The base plan ID of the target subscription
5. offer_id: The offer ID under the base plan (optional)
6. is_offer_personalized: Whether to enable personalized pricing (optional)

The replacement modes values are defined as:

```gdscript
# Access in your script as: BillingClient.ReplacementMode.WITH_TIME_PRORATION
enum ReplacementMode {
    # Unknown...
    UNKNOWN_REPLACEMENT_MODE = 0,

    # The new plan takes effect immediately, and the remaining time will be prorated and credited to the user.
    # Note: This is the default behavior.
    WITH_TIME_PRORATION = 1,

    # The new plan takes effect immediately, and the billing cycle remains the same.
    CHARGE_PRORATED_PRICE = 2,

    # The new plan takes effect immediately, and the new price will be charged on next recurrence time.
    WITHOUT_PRORATION = 3,

    # Replacement takes effect immediately, and the user is charged full price of new plan and
    # is given a full billing cycle of subscription, plus remaining prorated time from the old plan.
    CHARGE_FULL_PRI
# ...
```

Default behavior is `WITH_TIME_PRORATION`.

Example use of `update_subscription`:

```gdscript
billing_client.update_subscription(_active_subscription_purchase.purchase_token, \
                    BillingClient.ReplacementMode.WITH_TIME_PRORATION, "new_sub_product_id", "base_plan_id")
```

---

## Godot Android library

The Godot Engine for Android platforms is designed to be used as an [Android library](https://developer.android.com/studio/projects/android-library). This architecture enables several key features on Android platforms:

- Ability to integrate the Gradle build system within the Godot Editor, which provides the ability to leverage more components from the Android ecosystem such as libraries and tools
- Ability to make the engine portable and embeddable:

- Key in enabling the port of the Godot Editor to Android and mobile XR devices
- Key in allowing the integration and reuse of Godot's capabilities within existing codebase

Below we describe some of the use-cases and scenarios this architecture enables.

### Using the Godot Android library

The Godot Android library is packaged as an AAR archive file and hosted on [MavenCentral](https://central.sonatype.com/artifact/org.godotengine/godot) along with [its documentation](https://javadoc.io/doc/org.godotengine/godot/latest/index.html).

It provides access to Godot APIs and capabilities on Android platforms for the following non-exhaustive use-cases.

### Godot Android plugins

Android plugins are powerful tools to extend the capabilities of the Godot Engine by tapping into the functionality provided by Android platforms and ecosystem.

An Android plugin is an Android library with a dependency on the Godot Android library which the plugin uses to integrate into the engine's lifecycle and to access Godot APIs, granting it powerful capabilities such as GDExtension support which allows to update / mod the engine behavior as needed.

For more information, see Godot Android plugins.

### Embedding Godot in existing Android projects

The Godot Engine can be embedded within existing Android applications or libraries, allowing developers to leverage mature and battle-tested code and libraries better suited to a specific task.

The hosting component is responsible for driving the engine lifecycle via Godot's Android APIs. These APIs can also be used to provide bidirectional communication between the host and the embedded Godot instance allowing for greater control over the desired experience.

We showcase how this is done using a sample Android app that embeds the Godot Engine as an Android view, and uses it to render 3D glTF models.

The [GLTF Viewer](https://github.com/m4gr3d/Godot-Android-Samples/tree/master/apps/gltf_viewer) sample app uses an [Android RecyclerView component](https://developer.android.com/develop/ui/views/layout/recyclerview) to create a list of glTF items, populated from [Kenney's Food Kit pack](https://kenney.nl/assets/food-kit). When an item on the list is selected, the app's logic interacts with the embedded Godot Engine to render the selected glTF item as a 3D model.

The sample app source code can be found [on GitHub](https://github.com/m4gr3d/Godot-Android-Samples/tree/master/apps/gltf_viewer). Follow the instructions on [its README](https://github.com/m4gr3d/Godot-Android-Samples/blob/master/apps/gltf_viewer/README.md) to build and install it.

Below we break-down the steps used to create the GLTF Viewer app.

> **Warning:** Currently only a single instance of the Godot Engine is supported per process. You can configure the process the Android Activity runs under using the [android:process attribute](https://developer.android.com/guide/topics/manifest/activity-element#proc).

> **Warning:** Automatic resizing / orientation configuration events are not supported and may cause a crash. You can disable those events: - By locking to a specific orientation using the [android:screenOrientation attribute](https://developer.android.com/guide/topics/manifest/activity-element#screen).

- By declaring that the Activity will handle these configuration events using the [android:configChanges attribute](https://developer.android.com/guide/topics/manifest/activity-element#config).

#### 1. Create the Android app

> **Note:** The Android sample app was created using [Android Studio](https://developer.android.com/studio) and using [Gradle](https://developer.android.com/build) as the build system. The Android ecosystem provides multiple tools, IDEs, build systems for creating Android apps so feel free to use what you're familiar with, and update the steps below accordingly (contributions to this documentation are welcomed as well!).

- Set up an Android application project. It may be a brand new empty project, or an existing project
- Add the [maven dependency for the Godot Android library](https://central.sonatype.com/artifact/org.godotengine/godot)

- If using `gradle`, add the following to the `dependency` section of the app's gradle build file. Make sure to update `<version>` to the latest version of the Godot Android library:

```kotlin
implementation("org.godotengine:godot:<version>")
```

- If using `gradle`, include the following `aaptOptions` configuration under the `android > defaultConfig` section of the app's gradle build file. Doing so allows `gradle` to include Godot's hidden directories when building the app binary.

- If your build system does not support including hidden directories, you can configure the Godot project to not use hidden directories by deselecting [Application > Config > Use Hidden Project Data Directory](../godot_gdscript_misc.md) in the Project Settings.

```groovy
android {

  defaultConfig {
      // The default ignore pattern for the 'assets' directory includes hidden files and
      // directories which are used by Godot projects, so we override it with the following.
      aaptOptions {
          ignoreAssetsPattern "!.svn:!.git:!.gitignore:!.ds_store:!*.scc:<dir>_*:!CVS:!thumbs.db:!picasa.ini:!*~"
      }
    ...
```

- Create / update the application's Activity that will be hosting the Godot Engine instance. For the sample app, this is [MainActivity](https://github.com/m4gr3d/Godot-Android-Samples/blob/master/apps/gltf_viewer/src/main/java/fhuyakou/godot/app/android/gltfviewer/MainActivity.kt)

- The host Activity should implement the [GodotHost interface](https://github.com/godotengine/godot/blob/master/platform/android/java/lib/src/org/godotengine/godot/GodotHost.java)
- The sample app uses [Fragments](https://developer.android.com/guide/fragments) to organize its UI, so it uses [GodotFragment](https://github.com/godotengine/godot/blob/master/platform/android/java/lib/src/org/godotengine/godot/GodotFragment.java), a fragment component provided by the Godot Android library to automatically host and manage the Godot Engine instance.

```kotlin
private var godotFragment: GodotFragment? = null

override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)

    setContentView(R.layout.activity_main)

    val currentGodotFragment = supportFragmentManager.findFragmentById(R.id.godot_fragment_container)
    if (currentGodotFragment is GodotFragment) {
        godotFragment = currentGodotFragment
    } else {
        godotFragment = GodotFragment()
        supportFragmentManager.beginTransaction()
            .replace(R.id.godot_fragment_container, godotFragment!!)
            .commitNowAllowingStateLoss()
    }

    ...
```

> **Note:** The Godot Android library also provide [GodotActivity](https://github.com/godotengine/godot/blob/master/platform/android/java/lib/src/org/godotengine/godot/GodotActivity.kt), an Activity component that can be extended to automatically host and manage the Godot Engine instance. Alternatively, applications can directly create a [Godot](https://github.com/godotengine/godot/blob/master/platform/android/java/lib/src/org/godotengine/godot/Godot.kt) instance, host and manage it themselves.

- Using [GodotHost#getHostPlugins(...)](https://github.com/m4gr3d/Godot-Android-Samples/blob/0e3440f357f8be5b4c63a4fe75766793199a99d0/apps/gltf_viewer/src/main/java/fhuyakou/godot/app/android/gltfviewer/MainActivity.kt#L55), the sample app creates a [runtime GodotPlugin instance](https://github.com/m4gr3d/Godot-Android-Samples/blob/master/apps/gltf_viewer/src/main/java/fhuyakou/godot/app/android/gltfviewer/AppPlugin.kt) that's used to send signals (see Getting Started docs) to the `gdscript` logic

- The runtime `GodotPlugin` can also be used by `gdscript` logic to access JVM methods. For more information, see Godot Android plugins.
- Add any additional logic that will be used by your application

- For the sample app, this includes adding the [ItemsSelectionFragment fragment](https://github.com/m4gr3d/Godot-Android-Samples/blob/master/apps/gltf_viewer/src/main/java/fhuyakou/godot/app/android/gltfviewer/ItemsSelectionFragment.kt) (and related classes), a fragment used to build and show the list of glTF items
- Open the `AndroidManifest.xml` file, and configure the orientation if needed using the [android:screenOrientation attribute](https://developer.android.com/guide/topics/manifest/activity-element#screen)

- If needed, disable automatic resizing / orientation configuration changes using the [android:configChanges attribute](https://developer.android.com/guide/topics/manifest/activity-element#config)

```xml
<activity android:name=".MainActivity"
    android:screenOrientation="fullUser"
    android:configChanges="orientation|screenSize|smallestScreenSize|screenLayout"
    android:exported="true">

    ...
</activity>
```

#### 2. Create the Godot project

> **Note:** On Android, Godot's project files are exported to the `assets` directory of the generated `apk` binary. We leverage that architecture to bind our Android app and Godot project together by creating the Godot project in the Android app's `assets` directory. Note that it's also possible to create the Godot project in a separate directory and export it as a [PCK or ZIP file](https://docs.godotengine.org/en/stable/tutorials/export/exporting_projects.html#pck-versus-zip-pack-file-formats) to the Android app's `assets` directory. Using this approach requires passing the `--main-pack <pck_or_zip_filepath_relative_to_assets_dir>` argument to the hosted Godot Engine instance using [GodotHost#getCommandLine()](https://github.com/godotengine/godot/blob/6916349697a4339216469e9bf5899b983d78db07/platform/android/java/lib/src/org/godotengine/godot/GodotHost.java#L45). Example: ```java
> @Override
> public List<String> getCommandLine(){

    List<String> results = new ArrayList<>();
    results.addAll(super.getCommandLine());
    results.add("--main-pack");
    results.add("res://foo.pck");
    return results;

}
```The instructions below and the sample app follow the first approach of creating the Godot project in the Android app's`assets` directory.

- As mentioned in the **note** above, open the Godot Editor and create a Godot project directly (no subfolder) in the `assets` directory of the Android application project

- See the sample app's [Godot project](https://github.com/m4gr3d/Godot-Android-Samples/tree/master/apps/gltf_viewer/src/main/assets) for reference
- Configure the Godot project as desired

- Make sure the [orientation](https://docs.godotengine.org/en/stable/classes/class_projectsettings.html#class-projectsettings-property-display-window-handheld-orientation) set for the Godot project matches the one set in the Android app's manifest
- For Android, make sure [textures/vram_compression/import_etc2_astc](https://docs.godotengine.org/en/stable/classes/class_projectsettings.html#class-projectsettings-property-rendering-textures-vram-compression-import-etc2-astc) is set to true
- Update the Godot project script logic as needed

- For the sample app, the [script logic](https://github.com/m4gr3d/Godot-Android-Samples/blob/master/apps/gltf_viewer/src/main/assets/main.gd) queries for the runtime `GodotPlugin` instance and uses it to register for signals fired by the app logic
- The app logic fires a signal every time an item is selected in the list. The signal contains the filepath of the glTF model, which is used by the `gdscript` logic to render the model.

```gdscript
extends Node3D

# Reference to the gltf model that's currently being shown.
var current_gltf_node: Node3D = null

func _ready():
  # Default asset to load when the app starts
  _load_gltf("res://gltfs/food_kit/turkey.glb")

  var appPlugin = Engine.get_singleton("AppPlugin")
  if appPlugin:
    print("App plugin is available")

    # Signal fired from the app logic to update the gltf model being shown
    appPlugin.connect("show_gltf", _load_gltf)
  else:
    print("App plugin is not available")

# Load the gltf model specified by the given path
func _load_gltf(gltf_path: String):
  if current_gltf_node != null:
    remove_child(current_gltf_node)

  current_gltf_node = load(gltf_path).instantiate()

  add_child(current_gltf_node)
```

#### 3. Build and run the app

Once you complete configuration of your Godot project, build and run the Android app. If set up correctly, the host Activity will initialize the embedded Godot Engine on startup. The Godot Engine will check the `assets` directory for project files to load (unless configured to look for a `main pack`), and will proceed to run the project.

While the app is running on device, you can check [Android logcat](https://developer.android.com/studio/debug/logcat) to investigate any errors or crashes.

For reference, check the [build and install instructions](https://github.com/m4gr3d/Godot-Android-Samples/blob/master/apps/gltf_viewer/README.md) for the GLTF Viewer sample app.

---

## Godot Android plugins

### Introduction

Android plugins are powerful tools to extend the capabilities of the Godot engine by tapping into the functionality provided by Android platforms and ecosystem.

For example in Godot 4, Android plugins are used to support multiple Android-based XR platforms without encumbering the core codebase with vendor specific code or binaries.

### Android plugin

**Version 1 (v1)** of the Android plugin system was introduced in Godot 3 and compatible with Godot 4.0 and 4.1. That version allowed developers to augment the Godot engine with Java, Kotlin and native functionality.

Starting in Godot 4.2, Android plugins built on the v1 architecture are now deprecated. Instead, Godot 4.2 introduces a new **Version 2 (v2)** architecture for Android plugins.

#### v2 Architecture

> **Note:** Godot Android plugin leverages the [Gradle build system](tutorials_export.md).

Building on the previous v1 architecture, Android plugins continue to be derived from the [Android archive library](https://developer.android.com/studio/projects/android-library#aar-contents).

At its core, a Godot Android plugin v2 is an Android library with a dependency on the Godot Android library, and a custom Android library manifest.

This architecture allows Android plugins to extend the functionality of the engine with:

- Android platform APIs
- Android libraries
- Kotlin and Java libraries
- Native libraries (via JNI)
- GDExtension libraries

Each plugin has an init class extending from the [GodotPlugin](https://github.com/godotengine/godot/blob/0a7f75ec7b465604b6496c8f5f1d638aed250d6d/platform/android/java/lib/src/org/godotengine/godot/plugin/GodotPlugin.java#L80) class which is provided by the Godot Android library.

The `GodotPlugin` class provides APIs to access the running Godot instance and hook into its lifecycle. It is loaded at runtime by the Godot engine.

#### v2 Packaging format

v1 Android plugins required a custom `gdap` configuration file that was used by the Godot Editor to detect and load them. However this approach had several drawbacks, primary ones being that it lacked flexibility and departed from the [existing Godot EditorExportPlugin format, delivery and installation flow](https://docs.godotengine.org/en/stable/tutorials/plugins/editor/installing_plugins.html).

This has been resolved for v2 Android plugins by deprecating the `gdap` packaging and configuration mechanism in favor of the existing Godot `EditorExportPlugin` packaging format. The `EditorExportPlugin` API in turn has been extended to properly support Android plugins.

### Building a v2 Android plugin

A github project template **is provided** at [https://github.com/m4gr3d/Godot-Android-Plugin-Template](https://github.com/m4gr3d/Godot-Android-Plugin-Template) as a **quickstart for building Godot Android plugins for Godot 4.2+**. You can follow the [template README](https://github.com/m4gr3d/Godot-Android-Plugin-Template#readme) to set up your own Godot Android plugin project.

To provide further understanding, here is a break-down of the steps used to create the project template:

1. Create an Android library module using [these instructions](https://developer.android.com/studio/projects/android-library)
2. Add the Godot Android library as a dependency by updating the module's `gradle` [build file](https://github.com/m4gr3d/Godot-Android-Plugin-Template/blob/main/plugin/build.gradle.kts#L42):

```text
dependencies {
    implementation("org.godotengine:godot:4.2.0.stable")
}
```

The Godot Android library is [hosted on MavenCentral](https://central.sonatype.com/artifact/org.godotengine/godot), and updated for each release.

1. Create [GodotAndroidPlugin](https://github.com/m4gr3d/Godot-Android-Plugin-Template/blob/a01286b4cb459133bf07b11dfabdfd3980268797/plugin/src/main/java/org/godotengine/plugin/android/template/GodotAndroidPlugin.kt#L10), an init class for the plugin extending [GodotPlugin](https://github.com/godotengine/godot/blob/0a7f75ec7b465604b6496c8f5f1d638aed250d6d/platform/android/java/lib/src/org/godotengine/godot/plugin/GodotPlugin.java#L80).

- If the plugin exposes Kotlin or Java methods to be called from GDScript, they must be annotated with [@UsedByGodot](https://github.com/godotengine/godot/blob/0a7f75ec7b465604b6496c8f5f1d638aed250d6d/platform/android/java/lib/src/org/godotengine/godot/plugin/UsedByGodot.java#L45). The name called from GDScript **must match the method name exactly**. There is **no** coercing `snake_case` to `camelCase`. For example, from GDScript:

```gdscript
if Engine.has_singleton("MyPlugin"):
    var singleton = Engine.get_singleton("MyPlugin")
    print(singleton.myPluginFunction("World"))
```

- If the plugin uses [signals](https://docs.godotengine.org/en/stable/getting_started/step_by_step/signals.html), the init class must return the set of signals used by overriding [GodotPlugin::getPluginSignals()](https://github.com/godotengine/godot/blob/fa3428ff25bc577d2a3433090478a6d615567056/platform/android/java/lib/src/org/godotengine/godot/plugin/GodotPlugin.java#L302). To emit signals, the plugin can use the [GodotPlugin::emitSignal(...) method](https://github.com/godotengine/godot/blob/0a7f75ec7b465604b6496c8f5f1d638aed250d6d/platform/android/java/lib/src/org/godotengine/godot/plugin/GodotPlugin.java#L317).

2. Update the plugin `AndroidManifest.xml` [file](https://github.com/m4gr3d/Godot-Android-Plugin-Template/blob/main/plugin/src/main/AndroidManifest.xml) with the following meta-data:

```xml
<meta-data
    android:name="org.godotengine.plugin.v2.[PluginName]"
    android:value="[plugin.init.ClassFullName]" />
```

Where:

- `PluginName` is the name of the plugin
- `plugin.init.ClassFullName` is the full component name (package + class name) of the plugin init class (e.g: `org.godotengine.plugin.android.template.GodotAndroidPlugin`).

1. Create the [EditorExportPlugin configuration](https://github.com/m4gr3d/Godot-Android-Plugin-Template/tree/main/plugin/export_scripts_template) to package the plugin. The steps used to create the configuration can be seen in the **Packaging a v2 Android plugin** section.

#### Building a v2 Android plugin with GDExtension capabilities

Similar to GDNative support in v1 Android plugins, v2 Android plugins support the ability to integrate GDExtension capabilities.

A github project template is provided at [https://github.com/m4gr3d/GDExtension-Android-Plugin-Template](https://github.com/m4gr3d/GDExtension-Android-Plugin-Template) as a quickstart for building GDExtension Android plugins for Godot 4.2+. You can follow the [template's README](https://github.com/m4gr3d/GDExtension-Android-Plugin-Template#readme) to set up your own Godot Android plugin project.

#### Migrating a v1 Android plugin to v2

Use the following steps if you have a v1 Android plugin you want to migrate to v2:

1. Update the plugin's manifest file:

- Change the `org.godotengine.plugin.v1` prefix to `org.godotengine.plugin.v2`

2. Update the Godot Android library build dependency:

- You can continue using the `godot-lib.<version>.<status>.aar` binary from [Godot's download page](https://godotengine.org/download) if that's your preference. Make sure it's updated to the latest stable version.
- Or you can switch to the MavenCentral provided dependency:

```gdscript
dependencies {
    implementation("org.godotengine:godot:4.2.0.stable")
}
```

1. After updating the Godot Android library dependency, sync or build the plugin and resolve any compile errors:

- The `Godot` instance provided by `GodotPlugin::getGodot()` no longer has access to an `android.content.Context` reference. Use `GodotPlugin::getActivity()` instead.

2. Delete the `gdap` configuration file(s) and follow the instructions in the **Packaging a v2 Android plugin** section to set up the plugin configuration.

### Packaging a v2 Android plugin

As mentioned, a v2 Android plugin is now provided to the Godot Editor as an `EditorExportPlugin` plugin, so it shares a lot of the [same packaging steps](https://docs.godotengine.org/en/stable/tutorials/plugins/editor/making_plugins.html#creating-a-plugin).

1. Add the plugin output binaries within the plugin directory (e.g: in `addons/<plugin_name>/`)
2. Add the [tool script](https://docs.godotengine.org/en/stable/tutorials/plugins/editor/making_plugins.html#the-script-file) for the export functionality within the plugin directory (e.g: in `addons/<plugin_name>/`)

- The created script must be a `@tool` script, or else it will not work properly
- The export tool script is used to configure the Android plugin and hook it within the Godot Editor's export process. It should look something like this:

```gdscript
@tool
extends EditorPlugin

# A class member to hold the editor export plugin during its lifecycle.
var export_plugin : AndroidExportPlugin

func _enter_tree():
    # Initialization of the plugin goes here.
    export_plugin = AndroidExportPlugin.new()
    add_export_plugin(export_plugin)

func _exit_tree():
    # Clean-up of the plugin goes here.
    remove_export_plugin(export_plugin)
    export_plugin = null

class AndroidExportPlugin extends EditorExportPlugin:
    # Plugin's name.
    var _plugin_name = "<plugin_name>"

    # Specifies which platform is supported by the plugin.
    func _supports_platform(platform):
        if platform is EditorExportPlatformAndroid:
            return true
        return false

    # Return the paths of the plugin's AAR binaries relative to the 'ad
# ...
```

1. Create a `plugin.cfg`. This is an INI file with metadata about your plugin:

```gdscript
[plugin]

name="<plugin_name>"
description="<plugin_description>"
author="<plugin_author>"
version="<plugin_version>"
script="<relative_path_to_the_export_tool_script>"
```

For reference, here is the [folder structure for the Godot Android plugin project template](https://github.com/m4gr3d/Godot-Android-Plugin-Template/tree/main/plugin/export_scripts_template). At build time, the contents of the `export_scripts_template` directory as well as the generated plugin binaries are copied to the `addons/<plugin_name>` directory:

```none
export_scripts_template/
|
+--export_plugin.gd         # export plugin tool script
|
+--plugin.cfg               # plugin INI file
```

#### Packaging a v2 Android plugin with GDExtension capabilities

For GDExtension, we follow the same steps as for **Packaging a v2 Android plugin** and add the [GDExtension config file](https://docs.godotengine.org/en/stable/tutorials/scripting/cpp/gdextension_cpp_example.html#using-the-gdextension-module) in the same location as `plugin.cfg`.

For reference, here is the [folder structure for the GDExtension Android plugin project template](https://github.com/m4gr3d/GDExtension-Android-Plugin-Template/tree/main/plugin/export_scripts_template). At build time, the contents of the `export_scripts_template` directory as well as the generated plugin binaries are copied to the `addons/<plugin_name>` directory:

```none
export_scripts_template/
|
+--export_plugin.gd         # export plugin tool script
|
+--plugin.cfg               # plugin INI file
|
+--plugin.gdextension       # GDExtension config file
```

Here is what the `plugin.gdextension` config file should look like:

```gdscript
[configuration]

entry_symbol = "plugin_library_init"
compatibility_minimum = "4.2"
android_aar_plugin = true

[libraries]

android.debug.arm64 = "res://addons/GDExtensionAndroidPluginTemplate/bin/debug/arm64-v8a/libGDExtensionAndroidPluginTemplate.so"
android.release.arm64 = "res://addons/GDExtensionAndroidPluginTemplate/bin/release/arm64-v8a/libGDExtensionAndroidPluginTemplate.so"
...
```

Of note is the `android_aar_plugin` field that specifies this GDExtension module is provided as part of a v2 Android plugin. During the export process, this will indicate to the Godot Editor that the GDExtension native shared libraries are exported by the Android plugin AAR binaries.

For GDExtension Android plugins, the plugin init class must override [GodotPlugin::getPluginGDExtensionLibrariesPaths()](https://github.com/godotengine/godot/blob/0a7f75ec7b465604b6496c8f5f1d638aed250d6d/platform/android/java/lib/src/org/godotengine/godot/plugin/GodotPlugin.java#L277), and return the paths to the bundled GDExtension libraries config files (`*.gdextension`).

The paths must be relative to the Android library's `assets` directory. At runtime, the plugin will provide these paths to the Godot engine which will use them to load and initialize the bundled GDExtension libraries.

### Using a v2 Android plugin

> **Note:** - Godot 4.2 or higher is required

- v2 Android plugin requires the use of the [Gradle build process](https://docs.godotengine.org/en/stable/classes/class_editorexportplatformandroid.html#class-editorexportplatformandroid-property-gradle-build-use-gradle-build).
- The provided github project templates include demo Godot projects for quick testing.

1. Copy the plugin's output directory (`addons/<plugin_name>`) to the target Godot project's directory
2. Open the project in the Godot Editor; the Editor should detect the plugin
3. Navigate to `Project` -> `Project Settings...` -> `Plugins`, and ensure the plugin is enabled
4. Install the Godot Android build template by clicking on `Project` -> `Install Android Build Template...`
5. Navigate to `Project` -> `Export...`
6. In the `Export` window, create an `Android export preset`
7. In the `Android export preset`, scroll to `Gradle Build` and set `Use Gradle Build` to `true`
8. Update the project's scripts as needed to access the plugin's functionality. For example:

```gdscript
if Engine.has_singleton("MyPlugin"):
        var singleton = Engine.get_singleton("MyPlugin")
        print(singleton.myPluginFunction("World"))
```

1. Connect an Android device to your machine and run the project on it

#### Using a v2 Android plugin as an Android library

Since they are also Android libraries, Godot v2 Android plugins can be stripped from their `EditorExportPlugin` packaging and provided as raw `AAR` binaries for use as libraries alongside the Godot Android library by Android apps.

If targeting this use-case, make sure to include additional instructions for how the `AAR` binaries should be included (e.g: custom additions to the Android app's manifest).

### Reference implementations

- [Godot Android Plugins Samples](https://github.com/m4gr3d/Godot-Android-Samples/tree/master/plugins)
- [Godot Android Plugin Template](https://github.com/m4gr3d/Godot-Android-Plugin-Template)
- [GDExtension Android Plugin Template](https://github.com/m4gr3d/GDExtension-Android-Plugin-Template)
- [Godot OpenXR Loaders](https://github.com/GodotVR/godot_openxr_loaders)

### Tips and Guidelines

#### Simplify access to the exposed Java / Kotlin APIs

To make it easier to access the exposed Java / Kotlin APIs in the Godot Editor, it's recommended to provide one (or multiple) gdscript wrapper class(es) for your plugin users to interface with.

For example:

```gdscript
class_name PluginInterface extends Object

## Interface used to access the functionality provided by this plugin.

var _plugin_name = "GDExtensionAndroidPluginTemplate"
var _plugin_singleton

func _init():
    if Engine.has_singleton(_plugin_name):
        _plugin_singleton = Engine.get_singleton(_plugin_name)
    else:
        printerr("Initialization error: unable to access the java logic")

## Print a 'Hello World' message to the logcat.
func helloWorld():
    if _plugin_singleton:
        _plugin_singleton.helloWorld()
    else:
        printerr("Initialization error")
```

#### Support using the GDExtension functionality in the Godot Editor

If planning to use the GDExtension functionality in the Godot Editor, it is recommended that the GDExtension's native binaries are compiled not just for Android, but also for the OS onto which developers / users intend to run the Godot Editor. Not doing so may prevent developers / users from writing code that accesses the plugin from within the Godot Editor.

This may involve creating dummy plugins for the host OS just so the API is published to the editor. You can use the [godot-cpp-template](https://github.com/godotengine/godot-cpp-template) github template for reference on how to do so.

#### Supported data types

All data types are supported. Common types are mapped to their Godot equivalents (for example, `String[]` is mapped to `PackedStringArray()`), but for other types, you can use [JavaClassWrapper](https://docs.godotengine.org/en/stable/tutorials/platform/android/javaclasswrapper_and_androidruntimeplugin.html#javaclasswrapper-godot-singleton) to access it.

#### Godot crashes upon load

Check [adb logcat](https://developer.android.com/tools/logcat) for possible problems.

---

## Integrating with Android APIs

The Android platform has numerous APIs as well as a rich ecosystem of third-party libraries with wide and diverse functionality, like push notifications, analytics, authentication, ads, etc...

These don't make sense in Godot core itself so Godot has long provided an Android plugin system. The Android plugin system enables developers to create Godot Android plugins using Java or Kotlin code, which provides an interface to access and use Android APIs or third-party libraries in Godot projects from GDScript, C# or GDExtension.

```kotlin
class MyAndroidSingleton(godot: Godot?) : GodotPlugin(godot) {
        @UsedByGodot
        fun doSomething(value: String) {
                // ...
        }
}
```

Writing an Android plugin however requires knowledge of Java or Kotlin code, which most Godot developers do not have. As such there are many Android APIs and third-party libraries that don't have a Godot plugin that developers can interface with. In fact, this is one of the main reasons that developers cite for not being able to switch to Godot from other game engines.

To address this, we've introduced a couple of tools in **Godot 4.4** to simplify the process for developers to access Android APIs and third-party libraries.

### JavaClassWrapper (Godot singleton)

`JavaClassWrapper` is a [Godot singleton](../godot_gdscript_misc.md) which allows creating instances of Java / Kotlin classes and calling methods on them using only GDScript, C# or GDExtension.

```gdscript
var LocalDateTime = JavaClassWrapper.wrap("java.time.LocalDateTime")
var DateTimeFormatter = JavaClassWrapper.wrap("java.time.format.DateTimeFormatter")

var datetime = LocalDateTime.now()
var formatter = DateTimeFormatter.ofPattern("dd-MM-yyyy HH:mm:ss")

print(datetime.format(formatter))
```

In the code snippet above, `JavaClassWrapper` is used from GDScript to access the Java `LocalDateTime` and `DateTimeFormatter` classes. Through `JavaClassWrapper`, we can call the Java classes methods directly from GDScript as if they were GDScript methods.

### AndroidRuntime plugin

`JavaClassWrapper` is great, but to do many things on Android, you need access to various Android lifecycle / runtime objects. `AndroidRuntime` plugin is a [built-in Godot Android plugin](https://javadoc.io/doc/org.godotengine/godot/latest/org/godotengine/godot/plugin/AndroidRuntimePlugin.html) that allows you to do this.

Combining `JavaClassWrapper` and `AndroidRuntime` plugin allows developers to access and use Android APIs without switching away from GDScript, or using any tools aside from Godot itself. This is **huge** for the adoption of Godot for Android development:

- If you need to do something simple, or only use a small part of a third-party library, you don't have to make a plugin
- It allows developers to quickly integrate Android functionality
- It allows developers to create Godot addons using only GDScript and `JavaClassWrapper` (no Java or Kotlin needed)

> **Note:** For exports using `gradle`, Godot will automatically include `.jar` or `.aar` files it find in the project `addons` directory. So to use a third-party library, you can just drop its `.jar` or `.aar` file in the `addons` directory, and call its method directly from GDScript using `JavaClassWrapper`.

#### Example: Show an Android toast

```gdscript
# Retrieve the AndroidRuntime singleton.
var android_runtime = Engine.get_singleton("AndroidRuntime")
if android_runtime:
    # Retrieve the Android Activity instance.
    var activity = android_runtime.getActivity()

    # Create a Godot Callable to wrap the toast display logic.
    var toast_callable = func():
        # Use JavaClassWrapper to retrieve the android.widget.Toast class, then make and show a toast using the class APIs.
        var ToastClass = JavaClassWrapper.wrap("android.widget.Toast")
        ToastClass.makeText(activity, "This is a test", ToastClass.LENGTH_LONG).show()

    # Wrap the Callable in a Java Runnable and run it on the Android UI thread to show the toast.
    activity.runOnUiThread(android_runtime.createRunnableFromGodotCallable(toast_callable))
```

#### Example: Vibrate the device

```gdscript
# Retrieve the AndroidRuntime singleton.
var android_runtime = Engine.get_singleton("AndroidRuntime")
if android_runtime:
    # Retrieve the Android Vibrator system service and check if the device supports it.
    var vibrator_service = android_runtime.getApplicationContext().getSystemService("vibrator")
    if vibrator_service and vibrator_service.hasVibrator():
        # Configure and run a VibrationEffect.
        var VibrationEffect = JavaClassWrapper.wrap("android.os.VibrationEffect")
        var effect = VibrationEffect.createOneShot(500, VibrationEffect.DEFAULT_AMPLITUDE)
        vibrator_service.vibrate(effect)
```

#### Example: Accessing inner classes

Java inner classes can be accessed using the `$` sign:

```gdscript
# Accessing 'VERSION' class, which is an inner class from the 'android.os.Build' class.
var version = JavaClassWrapper.wrap("android.os.Build$VERSION")
var sdk_int = version.SDK_INT
if sdk_int == 30:
    # Do something specific on android 11 devices.
else:
    # All other devices
```

#### Example: Calling a constructor

A constructor is invoked by calling a method with the same name as the class.

This example creates an intent to send a text:

```gdscript
# Retrieve the AndroidRuntime singleton.
var android_runtime = Engine.get_singleton("AndroidRuntime")
if android_runtime:
    var Intent = JavaClassWrapper.wrap("android.content.Intent")
    var activity = android_runtime.getActivity()
    var intent = Intent.Intent() # Call the constructor.
    intent.setAction(Intent.ACTION_SEND)
    intent.putExtra(Intent.EXTRA_TEXT, "This is a test message.")
    intent.setType("text/plain")
    activity.startActivity(intent)
```

#### Example: Saving an image to the Android gallery

```gdscript
# Retrieve the AndroidRuntime singleton.
var android_runtime = Engine.get_singleton("AndroidRuntime")
if android_runtime:
    var Intent = JavaClassWrapper.wrap("android.content.Intent")
    var activity = android_runtime.getActivity()
    var intent = Intent.Intent()

    # Create the File and Uri.
    var Uri = JavaClassWrapper.wrap("android.net.Uri")
    var File = JavaClassWrapper.wrap("java.io.File")
    var file = File.File(file_path_to_image_here)
    var uri = Uri.fromFile(file)

    # Set Action and Data of Intent.
    intent.setAction(Intent.ACTION_MEDIA_SCANNER_SCAN_FILE)
    intent.setData(uri)

    # Broadcast it.
    activity.sendBroadcast(intent)
```

---

## Resolving crashes on Android

When your game crashes on Android, you often see obfuscated stack traces in Play Console or other crash reporting tools like Firebase Crashlytics. To make these stack traces human-readable (symbolicated), you need native debug symbols that correspond to your game's exported build.

Godot now provides downloadable native debug symbols for each official export template.

### Getting Native Debug symbols for official templates

Native debug symbol files are provided for every stable Godot release and can be downloaded from the [GitHub release page](https://github.com/godotengine/godot/releases/).

For example, to get the native debug symbols for version `4.5.1.stable`:

- Go to the [4.5.1.stable release page](https://github.com/godotengine/godot/releases/)
- Download the release artifact `Godot_native_debug_symbols.4.5.1.stable.template_release.android.zip`

### Getting Native Debug symbols for custom builds

Your exported template and its native debug symbols must come from the **same build**, so you can use the official symbols only if you are using the **official export templates**. If you are building **custom export templates**, you need to generate matching symbol files yourself.

To do so, add `debug_symbols=yes separate_debug_symbols=yes` to your scons build command. This will generate a file named `android-template-release-native-symbols.zip` containing the native debug symbols for your custom build.

For example,

```gdscript
scons platform=android target=template_release debug_symbols=yes separate_debug_symbols=yes generate_android_binaries=yes
```

If you are building for multiple architectures, you should include the `separate_debug_symbols=yes` only in the last build command, similar to how `generate_android_binaries=yes` is used.

```gdscript
scons platform=android arch=arm32 target=template_release debug_symbols=yes
scons platform=android arch=arm64 target=template_release debug_symbols=yes
scons platform=android arch=x86_32 target=template_release debug_symbols=yes
scons platform=android arch=x86_64 target=template_release debug_symbols=yes separate_debug_symbols=yes generate_android_binaries=yes
```

### Uploading Symbols to Google Play Console

Follow these steps to upload the native debug symbols:

1. Open [Play Console](https://play.google.com/console).
2. Select any app.
3. In the left menu, navigate to `Test and release > Latest releases and bundles`.

4. Now choose the relevant bundle and open it.

5. Select the `Downloads` tab, and scroll down to the `Assets` section.

6. Next to `Native debug symbols`, click the upload arrow icon.

7. Select and upload the corresponding native debug symbols file for that build version.

Alternatively, you can upload the symbols when creating a new release:

1. On the Create release page, locate your new release bundle.

1. Click the three-dot menu beside it.
1. Choose `Upload native debug symbols (.zip)` from the menu.

1. Select and upload the corresponding native debug symbols file for that build version.

### Manually Symbolicating Crash Logs

You can also symbolicate the crash logs manually using the [ndk-stack](https://developer.android.com/ndk/guides/ndk-stack) tool included in the Android NDK.

> **Note:** If you already have the Android SDK installed, you can find the `ndk-stack` tool inside the `ndk` folder in your SDK location. Otherwise, you can download the NDK directly from the [NDK downloads page](https://developer.android.com/ndk/downloads).

1. Extract the native debug symbols zip you downloaded earlier (or generated with your custom build).
2. Save your crash log to a text file (for example, `crash.txt`).

> **Important:** `ndk-stack` looks for an initial line of asterisks when parsing the crash log. Make sure your `crash.txt` starts with the following line: ```gdscript

---

````



1. Run ndk-stack with the path to the symbol directory that matches the crash's CPU architecture (for example, `arm64-v8a`):


```gdscript
ndk-stack -sym path/to/native_debug_symbols/arm64-v8a/ -dump crash.txt
````

1. The output will display a symbolicated trace, showing file names and line numbers in Godot's source code (or your custom build).

---
