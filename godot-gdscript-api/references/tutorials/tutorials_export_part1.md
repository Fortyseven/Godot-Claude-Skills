# Godot 4 GDScript Tutorials — Export (Part 1)

> 8 tutorials. GDScript-specific code examples.

## Gradle builds for Android

Godot provides the option to build using the gradle buildsystem. Instead of using the already pre-built template that ships with Godot, an Android Java project gets installed into your project folder. Godot will then build it and use it as an export template every time you export the project.

There are some reasons why you may want to do this:

- Modify the project before it's built.
- Add external SDKs that build with your project.

Configuring the gradle build is a fairly straightforward process. But first you need to follow the steps in exporting for android up to **Setting it up in Godot**. After doing that, follow the steps below.

### Set up the gradle build environment

Go to the Project menu, and install the _Gradle Build_ template:

Make sure export templates are downloaded. If not, this menu will help you download them.

A Gradle-based Android project will be created under `res://android/build`. Editing these files is not needed unless you really need to modify the project.

### Enabling the gradle build and exporting

When setting up the Android project in the **Project > Export** dialog, **Gradle Build** needs to be enabled:

From now on, attempting to export the project or one-click deploy will call the [Gradle](https://gradle.org/) build system to generate fresh templates (this window will appear every time):

The templates built will be used automatically afterwards, so no further configuration is needed.

> **Note:** When using the gradle Android build system, assets that are placed within a folder whose name begins with an underscore will not be included in the generated APK. This does not apply to assets whose _file_ name begins with an underscore. For example, `_example/image.png` will **not** be included as an asset, but `_image.png` will.

---

## Manually changing application icon for Windows

Windows applications use a Windows only format called ICO for their file icon and taskbar icon. Since Godot 4.1, Godot can create an ICO file for you based on the icon file defined in the Windows export preset. Supported formats are PNG, WebP, and SVG. If no icon is defined in the Windows export preset, the [application/config/icon](../godot_gdscript_misc.md) project setting is used automatically instead.

This means you no longer need to follow the steps in this section to manually create an ICO file, unless you wish to have control over the icon design depending on its displayed size.

### Creating a custom ICO file

You can create your application icon in any program but you will have to convert it to an ICO file using a program such as GIMP.

[This video tutorial](https://www.youtube.com/watch?v=uqV3UfM-n5Y) goes over how to export an ICO file with GIMP.

It is also possible to convert a PNG image to an hiDPI-friendly ICO file using this [ImageMagick](https://www.imagemagick.org/) command:

```none
magick convert icon.png -define icon:auto-resize=256,128,64,48,32,16 icon.ico
```

Depending on which version of ImageMagick you installed, you might need to leave out the `magick` and run this command instead:

```none
convert icon.png -define icon:auto-resize=256,128,64,48,32,16 icon.ico
```

> **Warning:** For the ICO file to effectively replace the default Godot icon, it must contain _all_ the sizes included in the default Godot icon: 16×16, 32×32, 48×48, 64×64, 128×128, 256×256. If the ICO file does not contain all the sizes, the default Godot icon will be kept for the sizes that weren't overridden. The above ImageMagick command takes this into account.

### Changing the taskbar icon

The taskbar icon is the icon that shows up on the taskbar when your project is running.

To change the taskbar icon, go to **Project > Project Settings > Application > Config**, make sure **Advanced Settings** are enabled to see the setting, then go to `Windows Native Icon`. Click on the folder icon and select your ICO file.

This setting only changes the icon for your exported game on Windows. To set the icon for macOS, use `Macos Native Icon`. And for any other platform, use the `Icon` setting.

### Changing the file icon

The file icon is the icon of the executable that you click on to start the project.

To do that, you will need to specify the icon when exporting. Go to **Project > Export**. Assuming you have already created a Windows Desktop preset, select your icon in ICO format in the **Application > Icon** field.

### Testing the result

You can now export the project. If it worked correctly, you should see this:

> **Note:** If your icon isn't showing up properly try clearing the icon cache. To do so, open the **Run** dialog and enter `ie4uinit.exe -ClearIconCache` or `ie4uinit.exe -show`.

---

## Exporting for Android

> **See also:** This page describes how to export a Godot project to Android. If you're looking to compile export template binaries from source instead, read Compiling for Android.

Exporting for Android has fewer requirements than compiling Godot for Android. The following steps detail what is needed to set up the Android SDK and the engine.

> **Attention:** Projects written in C# can be exported to Android as of Godot 4.2, but support is experimental and [some limitations apply](tutorials_scripting.md).

### Install OpenJDK 17

Download and install [OpenJDK 17](https://adoptium.net/temurin/releases/?variant=openjdk17&version=17&os=any&arch=any).

> **Note:** Higher versions of the JDK are also supported, but we recommend using JDK 17 for optimal compatibility and stability.

### Download the Android SDK

Download and install the Android SDK.

- You can install the Android SDK using [Android Studio Iguana (version 2023.2.1) or later](https://developer.android.com/studio/).

- Run it once to complete the SDK setup using these [instructions](https://developer.android.com/studio/intro/update#sdk-manager).
- Ensure that the [required packages](https://developer.android.com/studio/intro/update#required) are installed as well.

- Android SDK Platform-Tools version 35.0.0 or later
- Android SDK Build-Tools version 35.0.1
- Android SDK Platform 35
- Android SDK Command-line Tools (latest)
- Ensure that the [NDK and CMake are installed and configured](https://developer.android.com/studio/projects/install-ndk).

- CMake version 3.10.2.4988404
- NDK version r28b (28.1.13356709)
- Alternatively, you can install the Android SDK with the sdkmanager command line tool.

- Install the command line tools package using these [instructions](https://developer.android.com/tools/sdkmanager).
- Once the command line tools are installed, run the following sdkmanager command to complete the setup process:

```gdscript
sdkmanager --sdk_root=<android_sdk_path> "platform-tools" "build-tools;35.0.1" "platforms;android-35" "cmdline-tools;latest" "cmake;3.10.2.4988404" "ndk;28.1.13356709"
```

> **Note:** If you are using Linux, **do not use an Android SDK provided by your distribution's repositories as it will often be outdated**.

### Setting it up in Godot

Enter the Editor Settings screen (under the Godot tab for macOS, or the Editor tab for other platforms). This screen contains the editor settings for the user account in the computer (it's independent of the project).

Scroll down to the section where the Android settings are located:

In that screen, 2 paths need to be set:

- `Java SDK Path` should be the location where OpenJDK 17 was installed.
- `Android SDK Path` should be the location where the Android SDK was installed. This directory should contain `platform-tools/adb`. - For example `%LOCALAPPDATA%\Android\Sdk\` on Windows or `/Users/$USER/Library/Android/sdk/` on macOS.

Once that is configured, everything is ready to export to Android!

> **Note:** If you get an error saying _"Could not install to device."_, make sure you do not have an application with the same Android package name already installed on the device (but signed with a different key). If you have an application with the same Android package name but a different signing key already installed on the device, you **must** remove the application in question from the Android device before exporting to Android again.

### Providing launcher icons

Launcher icons are used by Android launcher apps to represent your application to users. Godot only requires high-resolution icons (for `xxxhdpi` density screens) and will automatically generate lower-resolution variants.

There are three types of icons:

- **Main Icon:** The "classic" icon. This will be used on all Android versions up to Android 8 (Oreo), exclusive. Must be at least 192×192 px.
- **Adaptive Icons:** Starting from Android 8 (inclusive), [Adaptive Icons](https://developer.android.com/guide/practices/ui_guidelines/icon_design_adaptive) were introduced. Applications will need to include separate background and foreground icons to have a native look. The user's launcher application will control the icon's animation and masking. Must be at least 432×432 px.
- **Themed Icons (optional):** Starting from Android 13 (inclusive), Themed Icons were introduced. Applications will need to include a monochrome icon to enable this feature. The user's launcher application will control the icon's theme. Must be at least 432×432 px.

> **See also:** It's important to adhere to some rules when designing adaptive icons. [Google Design has provided a nice article](https://medium.com/google-design/designing-adaptive-icons-515af294c783) that helps to understand those rules and some of the capabilities of adaptive icons.

Caution

The most important adaptive icon design rule is to have your icon critical elements inside the safe zone: a centered circle with a diameter of 66dp (264 pixels on `xxxhdpi`) to avoid being clipped by the launcher.

If you don't provide the requested icons (except for Monochrome), Godot will replace them using a fallback chain, trying the next in line when the current one fails:

- **Main Icon:** Provided main icon -> Project icon -> Default Godot main icon.
- **Adaptive Icon Foreground:** Provided foreground icon -> Provided main icon -> Project icon -> Default Godot foreground icon.
- **Adaptive Icon Background:** Provided background icon -> Default Godot background icon.

It's highly recommended to provide all the requested icons with their specified resolutions. This way, your application will look great on all Android devices and versions.

### Exporting for Google Play Store

All new apps uploaded to Google Play after August 2021 must be an AAB (Android App Bundle) file.

Uploading an AAB or APK to Google's Play Store requires you to sign using a non-debug keystore file; such a file can be generated like this:

```shell
keytool -v -genkey -keystore mygame.keystore -alias mygame -keyalg RSA -validity 10000
```

This keystore and key are used to verify your developer identity, remember the password and keep it in a safe place! It is suggested to use only upper and lowercase letters and numbers. Special characters may cause errors. Use Google's Android Developer guides to learn more about [app signing](https://developer.android.com/studio/publish/app-signing).

Now fill in the following forms in your Android Export Presets:

- **Release:** Enter the path to the keystore file you just generated.
- **Release User:** Replace with the key alias.
- **Release Password:** Key password. Note that the keystore password and the key password currently have to be the same.

Don't forget to uncheck the **Export With Debug** checkbox while exporting.

### Optimizing the file size

If you're working with APKs and not AABs, by default, the APK will contain native libraries for both ARMv7 and ARMv8 architectures. This increases its size significantly. To create a smaller file, uncheck either **Armeabi-v 7a** or **Arm 64 -v 8a** in your project's Android export preset. This will create an APK that only contains a library for a single architecture. Note that applications targeting ARMv7 can also run on ARMv8 devices, but the opposite is not true. The reason you don't do this to save space with AABs is that Google automatically splits up the AAB on their backend, so the user only downloads what they need.

You can optimize the size further by compiling an Android export template with only the features you need. See Optimizing a build for size for more information.

### Environment variables

You can use the following environment variables to set export options outside of the editor. During the export process, these override the values that you set in the export menu.

| Export option                         | Environment variable                    |
| ------------------------------------- | --------------------------------------- |
| Encryption / Encryption Key           | GODOT_SCRIPT_ENCRYPTION_KEY             |
| Options / Keystore / Debug            | GODOT_ANDROID_KEYSTORE_DEBUG_PATH       |
| Options / Keystore / Debug User       | GODOT_ANDROID_KEYSTORE_DEBUG_USER       |
| Options / Keystore / Debug Password   | GODOT_ANDROID_KEYSTORE_DEBUG_PASSWORD   |
| Options / Keystore / Release          | GODOT_ANDROID_KEYSTORE_RELEASE_PATH     |
| Options / Keystore / Release User     | GODOT_ANDROID_KEYSTORE_RELEASE_USER     |
| Options / Keystore / Release Password | GODOT_ANDROID_KEYSTORE_RELEASE_PASSWORD |

### Export options

You can find a full list of export options available in the [EditorExportPlatformAndroid](../godot_gdscript_editor.md) class reference.

---

## Exporting for dedicated servers

If you want to run a dedicated server for your project on a machine that doesn't have a GPU or display server available, you'll need to run Godot with the `headless` display server and `Dummy` [audio driver](../godot_gdscript_misc.md).

Since Godot 4.0, this can be done by running a Godot binary on any platform with the `--headless` command line argument, or running a project exported as dedicated server. You do not need to use a specialized server binary anymore, unlike Godot 3.x.

### Editor versus export template

It is possible to use either an editor or export template (debug or release) binary in headless mode. Which one you should use depends on your use case:

- **Export template:** Use this one for running dedicated servers. It does not contain editor functionality, and is therefore smaller and more optimized.
- **Editor:** This binary contains editor functionality and is intended to be used for exporting projects. This binary _can_ be used to run dedicated servers, but it's not recommended as it's larger and less optimized.

### Export approaches

There are two ways to export a project for a server:

- Create a separate export preset for the platform that will host the server, then export your project as usual.
- Export a PCK file only, preferably for the platform that matches the platform that will host the server. Place this PCK file in the same folder as an export template binary, rename the binary to have the same name as the PCK (minus the file extension), then run the binary.

Both methods should result in identical output. The rest of the page will focus on the first approach.

See Exporting projects for more information.

### Exporting a project for a dedicated server

If you export a project as usual when targeting a server, you will notice that the PCK file is just as large as for the client. This is because it includes all resources, including those the server doesn't need (such as texture data). Additionally, headless mode won't be automatically used; the user will have to specify `--headless` to make sure no window spawns.

Many resources such as textures can be stripped from the PCK file to greatly reduce its size. Godot offers a way to do this for textures and materials in a way that preserves references in scene or resource files (built-in or external).

To begin doing so, make sure you have a dedicated export preset for your server, then select it, go to its **Resources** tab and change its export mode:

When this export mode is chosen, the `dedicated_server` feature tag is automatically added to the exported project.

> **Note:** If you do not wish to use this export mode but still want the feature tag, you can write the name `dedicated_server` in the **Features** tab of the export preset. This will also force `--headless` when running the exported project.

After selecting this export mode, you will be presented with a list of resources in the project:

Ticking a box allows you to override options for the specified file or folder. Checking boxes does **not** affect which files are exported; this is done by the options selected for each checkbox instead.

Files within a checked folder will automatically use the parent's option by default, which is indicated by the **(Inherited)** suffix for the option name (and the option name being grayed out). To change the option for a file whose option is currently inherited, you must tick the box next to it first.

- **Strip Visuals:** Export this resource, with visual files (textures and materials) replaced by placeholder classes. Placeholder classes store the image size (as it's sometimes used to position elements in a 2D scene), but nothing else.
- **Keep:** Export this resource as usual, with visual files intact.
- **Remove:** The file is not included in the PCK. This is useful to ignore scenes and resources that only the client needs. If you do so, make sure the server doesn't reference these client-only scenes and resources in any way.

The general recommendation is to use **Strip Visuals** whenever possible, unless the server needs to access image data such as pixels' colors. For example, if your server generates collision data based on an image's contents, you need to use **Keep** for that particular image.

> **Tip:** To check the file structure of your exported PCK, use the **Export PCK/ZIP...** button with a `.zip` file extension, then open the resulting ZIP file in a file manager.

> **Warning:** Be careful when using the **Remove** mode, as scenes/resources that reference a removed file will no longer be able to load successfully. If you wish to remove specific resources but make the scenes still be able to load without them, you'll have to remove the reference in the scene file and load the files to the nodes' properties using `load()` in a script. This approach can be used to strip resources that Godot doesn't support replacing with placeholders yet, such as audio. Removing textures is often what makes the greatest impact on the PCK size, so it is recommended to stick with **Strip Visuals** at first.

With the above options used, a PCK for the client (which exports all resources normally) will look as follows:

```none
.
├── .godot
│   ├── exported
│   │   └── 133200997
│   │       └── export-78c237d4bfdb4e1d02e0b5f38ddfd8bd-scene.scn
│   ├── global_script_class_cache.cfg
│   ├── imported
│   │   ├── map_data.png-ce840618f399a990343bfc7298195a13.ctex
│   │   ├── music.ogg-fa883da45ae49695a3d022f64e60aee2.oggvorbisstr
│   │   └── sprite.png-7958af25f91bb9dbae43f35388f8e840.ctex
│   └── uid_cache.bin
├── client
│   ├── music.ogg.import
│   └── sprite.png.import
├── server
│   └── map_data.png.import
├── test
│   └── scene.gd
└── unused
│   └── development_test.gd
├── project.binary
├── scene.gd
├── scene.tscn.remap
```

The PCK's file structure for the server will look as follows:

```none
.
├── .godot
│   ├── exported
│   │   └── 3400186661
│   │       ├── export-78c237d4bfdb4e1d02e0b5f38ddfd8bd-scene.scn
│   │       ├── export-7958af25f91bb9dbae43f35388f8e840-sprite.res  # Placeholder texture
│   │       └── export-fa883da45ae49695a3d022f64e60aee2-music.res
│   ├── global_script_class_cache.cfg
│   ├── imported
│   │   └── map_data.png-ce840618f399a990343bfc7298195a13.ctex
│   └── uid_cache.bin
├── client
│   ├── music.ogg.import
│   └── sprite.png.import  # Points to placeholder texture
└── server
│   └── map_data.png.import
├── project.binary
├── scene.gd
├── scene.tscn.remap
```

### Starting the dedicated server

If both your client and server are part of the same Godot project, you will have to add a way to start the server directly using a command-line argument.

If you **exported the project** using the **Export as dedicated server** export mode (or have added `dedicated_server` as a custom feature tag), you can use the `dedicated_server` feature tag to detect whether a dedicated server PCK is being used:

```gdscript
# Note: Feature tags are case-sensitive.
if OS.has_feature("dedicated_server"):
    # Run your server startup code here...
    pass
```

If you also wish to host a server when using the built-in `--headless` command line argument, this can be done by adding the following code snippet in your main scene (or an autoload)'s `_ready()` method:

```gdscript
if DisplayServer.get_name() == "headless":
    # Run your server startup code here...
    #
    # Using this check, you can start a dedicated server by running
    # a Godot binary (editor or export template) with the `--headless`
    # command-line argument.
    pass
```

If you wish to use a custom command line argument, this can be done by adding the following code snippet in your main scene (or an autoload)'s `_ready()` method:

```gdscript
if "--server" in OS.get_cmdline_user_args():
    # Run your server startup code here...
    #
    # Using this check, you can start a dedicated server by running
    # a Godot binary (editor or export template) with the `--server`
    # command-line argument.
    pass
```

It's a good idea to add at least one of the above command-line arguments to start a server, as it can be used to test server functionality from the command line without having to export the project.

If your client and server are separate Godot projects, your server should most likely be configured in a way where running the main scene starts a server automatically.

### Next steps

On Linux, to make your dedicated server restart after a crash or system reboot, you can [create a systemd service](https://medium.com/@benmorel/creating-a-linux-service-with-systemd-611b5c8b91d6). This also lets you view server logs in a more convenient fashion, with automatic log rotation provided by systemd. When making your project hostable as a systemd service, you should also enable the `application/run/flush_stdout_on_print` project setting. This way, journald (the systemd logging service) can collect logs while the process is running.

If you have experience with containers, you could also look into wrapping your dedicated server in a [Docker](https://www.docker.com/) container. This way, it can be used more easily in an automatic scaling setup (which is outside the scope of this tutorial).

---

## Exporting for iOS

> **See also:** This page describes how to export a Godot project to iOS. If you're looking to compile export template binaries from source instead, read Compiling for iOS.

These are the steps to load a Godot project in Xcode. This allows you to build and deploy to an iOS device, build a release for the App Store, and do everything else you can normally do with Xcode.

> **Attention:** Projects written in C# can be exported to iOS as of Godot 4.2, but support is experimental and [some limitations apply](tutorials_scripting.md).

### Requirements

- You must export for iOS from a computer running macOS with Xcode installed.
- Download the Godot export templates. Use the Godot menu: Editor > Manage Export Templates

### Export a Godot project to Xcode

In the Godot editor, open the **Export** window from the **Project** menu. When the Export window opens, click **Add..** and select **iOS**.

The **App Store Team ID** and (Bundle) **Identifier** options in the **Application** category are required. Leaving them blank will cause the exporter to throw an error.

> **Note:** If you encounter an error during export similar to `JSON text did not start with array or object and option to allow fragments not set` then it might be due to a malformated **App Store Team ID**! The exporter expects a (10 characters long) code like `ABCDE12XYZ` and not, e.g., your name as Xcode likes to display in the _Signing & Capabilities_ tab. You can find the code over at [developer.apple.com](https://developer.apple.com/account/resources/certificates/list) next to your name in the top right corner.

After you click **Export Project**, there are still two important options left:

- **Path** is an empty folder that will contain the exported Xcode project files.
- **File** will be the name of the Xcode project and several project specific files and directories.

> **Note:** This tutorial uses **exported_xcode_project_name**, but you will use your project's name. When you see **exported_xcode_project_name** in the following steps, replace it with the name you used instead.

> **Note:** Avoid using spaces when you choose your **exported_xcode_project_name** as this can lead to corruption in your XCode project file.

When the export completes, the output folder should look like this:

> **Warning:** Exporting for the iOS simulator is currently not supported as per [GH-102149](https://github.com/godotengine/godot/issues/102149). Apple Silicon Macs can run iOS apps natively, so you can run exported iOS projects directly on an Apple Silicon Mac without needing the iOS simulator.

Opening **exported_xcode_project_name.xcodeproj** lets you build and deploy like any other iOS app.

### Active development considerations

The above method creates an exported project that you can build for release, but you have to re-export every time you make a change in Godot.

While developing, you can speed this process up by linking your Godot project files directly into your app.

In the following example:

- **exported_xcode_project_name** is the name of the exported iOS application (as above).
- **godot_project_to_export** is the name of the Godot project.

> **Note:** **godot_project_to_export** must not be the same as **exported_xcode_project_name** to prevent signing issues in Xcode.

#### Steps to link a Godot project folder to Xcode

1. Start from an exported iOS project (follow the steps above).
2. In Finder, drag the Godot project folder into the Xcode file browser.

3. In the dialog, make sure to select Action: **Reference files in place** and Groups: **Create folders**. Uncheck Targets: **exported_xcode_project_name**.

4. See the **godot_project_to_export** folder in the Xcode file browser.
5. Select the godot project in the Project navigator. Then on the other side of the XCode window, in the File Inspector, make these selections:

- **Location**: Relative to Project
- **Build Rules**: Apply Once to Folder
- add your project to **Target Membership**

1. Delete **exported_xcode_project_name.pck** from the Xcode project in the project navigator.

2. Open **exported_xcode_project_name-Info.plist** and add a string property named **godot_path** (this is the real key name) with a value **godot_project_to_export** (this is the name of your project)

That's it! You can now edit your project in the Godot editor and build it in Xcode when you want to run it on a device.

### Plugins for iOS

Special iOS plugins can be used in Godot. Check out the [Plugins for iOS](tutorials_platform.md) page.

### Environment variables

You can use the following environment variables to set export options outside of the editor. During the export process, these override the values that you set in the export menu.

| Export option                                             | Environment variable                        |
| --------------------------------------------------------- | ------------------------------------------- |
| Encryption / Encryption Key                               | GODOT_SCRIPT_ENCRYPTION_KEY                 |
| Options / Application / Provisioning Profile UUID Debug   | GODOT_IOS_PROVISIONING_PROFILE_UUID_DEBUG   |
| Options / Application / Provisioning Profile UUID Release | GODOT_IOS_PROVISIONING_PROFILE_UUID_RELEASE |

### Troubleshooting

#### xcode-select points at wrong SDK location

xcode-select is a tool that comes with Xcode and among other things points at iOS SDKs on your Mac. If you have Xcode installed, opened it, agreed to the license agreement, and installed the command line tools, xcode-select should point at the right location for the iPhone SDK. If it somehow doesn't, Godot will fail exporting to iOS with an error that may look like this:

```gdscript
MSB3073: The command ""clang" <LOTS OF PATHS AND COMMAND LINE ARGUMENTS HERE>
"/Library/Developer/CommandLineTools/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS.sdk"" exited with code 1.
```

In this case, Godot is trying to find the `Platforms` folder containing the iPhone SDK inside the `/Library/Developer/CommandLineTools/` folder, but the `Platforms` folder with the iPhone SDK is actually located under `/Applications/Xcode.app/Contents/Developer`. To verify this, you can open up Terminal and run the following command to see what xcode-select points at:

```gdscript
xcode-select -p
```

To fix xcode-select pointing at a wrong location, enter this command in Terminal:

```gdscript
sudo xcode-select -switch /Applications/Xcode.app
```

After running this command, Godot should be able to successfully export to iOS.

### Export options

You can find a full list of export options available in the [EditorExportPlatformIOS](../godot_gdscript_editor.md) class reference.

---

## Exporting for Linux

> **See also:** This page describes how to export a Godot project to Linux. If you're looking to compile editor or export template binaries from source instead, read Compiling for Linux, \*BSD.

The simplest way to distribute a game for PC is to copy the executable (`godot`), compress the folder and send it to someone else. However, this is often not desired.

Godot offers a more elegant approach for PC distribution when using the export system. When exporting for Linux, the exporter takes all the project files and creates a `data.pck` file. This file is bundled with a specially optimized binary that is smaller, faster and does not contain the editor and debugger.

### Architecture

There are 7 different processor architectures that exported Godot projects can run on in Linux:

- x86_64
- x86_32
- arm64
- arm32
- rv64
- ppc64
- loongarch64

The default is x86_64, this is the most common architecture of PC processors today. All modern Intel and AMD processors as of writing this are x86_64.

x86_32 will give you a 32bit executable that can run on 32bit only distributions of Linux as well as some modern distributions that are 64bit. It is NOT recommended to use this option unless you are trying to get your project to run on an old 32bit distribution and processor. It should also be noted that several prominent distributions, such as Fedora, have been discussing removing their 32bit libraries which would prevent executables made this way from running on future versions of that distribution.

arm64 executables can run on 64bit ARM processors. If you're familiar with the Raspberry Pi, those have utilized 64bit ARM processors since the Pi 3 (older versions used 32bit ARM processors). If you're uploading to a platform that supports multiple executables, such as itch.io, and you're confident your game could run on a common ARM computer, such as the Pi 5, then we'd recommend exporting this version and providing it as an option.

arm32 executables are for older 32bit arm processors, such as what the Raspberry Pi 1 and 2 used. Given that they're not common at all these days we do not recommend exporting for this unless you have a computer with one of these processors you know you can, and want to have your game running on.

rv64 is for RISC-V processors, ppc64 is for 64bit PowerPC processors, and loongarch64 is for 64bit LoongArch processors. All of these architectures are substantially more niche when it comes to running videogames on them. And we only recommend exporting for them if you have a reason to, such as if you're an enthusiast who owns hardware. Official export templates are not provided by Godot, you will have to create them on your own. Instructions for compiling the engine for RISC-V and creating export templates can be found on the Compiling for Linux, \*BSD page.

### Environment variables

You can use the following environment variables to set export options outside of the editor. During the export process, these override the values that you set in the export menu.

| Export option               | Environment variable        |
| --------------------------- | --------------------------- |
| Encryption / Encryption Key | GODOT_SCRIPT_ENCRYPTION_KEY |

### Export options

You can find a full list of export options available in the [EditorExportPlatformLinuxBSD](../godot_gdscript_editor.md) class reference.

---

## Exporting for macOS

> **See also:** This page describes how to export a Godot project to macOS. If you're looking to compile editor or export template binaries from source instead, read Compiling for macOS.

macOS apps exported with the official export templates are exported as a single "Universal 2" binary `.app` bundle, a folder with a specific structure which stores the executable, libraries and all the project files. This bundle can be exported as is, packed in a ZIP archive, or packed in a DMG disk image (only supported when exporting from macOS). [Universal binaries for macOS support both Intel x86_64 and ARM64 (Apple Silicon) architectures](https://developer.apple.com/documentation/apple-silicon/building-a-universal-macos-binary).

> **Warning:** Due to file system limitations, `.app` bundles exported from Windows lack the `executable` flag and won't run on macOS. Projects exported as `.zip` are not affected by this issue. To run `.app` bundles exported from Windows on macOS, transfer the `.app` to a device running macOS or Linux and use the `chmod +x {executable_name}` terminal command to add the `executable` permission. The main executable located in the `Contents/MacOS/` subfolder, as well as optional helper executables in the `Contents/Helpers/` subfolder, should have the `executable` permission for the `.app` bundle to be valid.

### Requirements

- Download the Godot export templates. Use the Godot menu: `Editor > Manage Export Templates`.
- A valid and unique `Bundle identifier` should be set in the `Application` section of the export options.

> **Warning:** Projects exported without code signing and notarization will be blocked by Gatekeeper if they are downloaded from unknown sources, see the Running Godot apps on macOS page for more information.

### Code signing and notarization

By default, macOS will run only applications that are signed and notarized. If you use any other signing configuration, see Running Godot apps on macOS for workarounds.

To notarize an app, you **must** have a valid [Apple Developer ID Certificate](https://developer.apple.com/).

#### If you have an Apple Developer ID Certificate and exporting from macOS

Install [Xcode](https://developer.apple.com/xcode/) command line tools and open Xcode at least once or run the `sudo xcodebuild -license accept` command to accept license agreement.

##### To sign exported app

- Select `Xcode codesign` in the `Code Signing > Codesign` option.
- Set valid Apple ID certificate identity (certificate "Common Name") in the `Code Signing > Identity` section.

##### To notarize exported app

- Select `Xcode altool` in the `Notarization > Notarization` option.
- Disable the `Debugging` entitlement.
- Set valid Apple ID login / app. specific password or [App Store Connect](https://developer.apple.com/documentation/appstoreconnectapi) API UUID / Key in the `Notarization` section.

You can use the `xcrun notarytool history` command to check notarization status and use the `xcrun notarytool log {ID}` command to download the notarization log.

If you encounter notarization issues, see [Resolving common notarization issues](https://developer.apple.com/documentation/security/notarizing_macos_software_before_distribution/resolving_common_notarization_issues) for more info.

After notarization is completed, [staple the ticket](https://developer.apple.com/documentation/security/notarizing_macos_software_before_distribution/customizing_the_notarization_workflow) to the exported project.

#### If you have an Apple Developer ID Certificate and exporting from Linux or Windows

Install [PyOxidizer rcodesign](https://github.com/indygreg/apple-platform-rs/tree/main/apple-codesign), and configure the path to `rcodesign` in the `Editor Settings > Export > macOS > rcodesign`.

##### To sign exported app

- Select `PyOxidizer rcodesign` in the `Code Signing > Codesign` option.
- Set valid Apple ID PKCS #12 certificate file and password in the `Code Signing` section.

##### To notarize exported app

- Select `PyOxidizer rcodesign` in the `Notarization > Notarization` option.
- Disable the `Debugging` entitlement.
- Set valid [App Store Connect](https://developer.apple.com/documentation/appstoreconnectapi) API UUID / Key in the `Notarization` section.

You can use the `rcodesign notary-log` command to check notarization status.

After notarization is completed, use the `rcodesign staple` command to staple the ticket to the exported project.

#### If you do not have an Apple Developer ID Certificate

- Select `Built-in (ad-hoc only)` in the `Code Signing > Codesign` option.
- Select `Disabled` in the `Notarization > Notarization` option.

In this case Godot will use an ad-hoc signature, which will make running an exported app easier for the end users, see the Running Godot apps on macOS page for more information.

#### Signing Options

| Option               | Description                                                                                |
| -------------------- | ------------------------------------------------------------------------------------------ |
| Codesign             | Tool to use for code signing.                                                              |
| Identity             | The "Full Name" or "Common Name" of the signing identity, store in the macOS keychain. [1] |
| Certificate File     | The PKCS #12 certificate file. [2]                                                         |
| Certificate Password | Password for the certificate file. [2]                                                     |
| Custom Options       | Array of command line arguments passed to the code signing tool.                           |

[**1**]

This option is visible only when signing with Xcode codesign.

[2] (**1**,**2**)

These options are visible only when signing with PyOxidizer rcodesign.

#### Notarization Options

| Option            | Description                                                                                                                       |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| Notarization      | Tool to use for notarization.                                                                                                     |
| Apple ID Name     | Apple ID account name (email address). [3]                                                                                        |
| Apple ID Password | Apple ID app-specific password. See Using app-specific passwords to enable two-factor authentication and create app password. [3] |
| Apple Team ID     | Team ID ("Organization Unit"), if your Apple ID belongs to multiple teams (optional). [3]                                         |
| API UUID          | Apple App Store Connect API issuer UUID.                                                                                          |
| API Key           | Apple App Store Connect API key.                                                                                                  |

> **Note:** You should set either Apple ID Name/Password or App Store Connect API UUID/Key.

[3] (**1**,**2**,**3**)

These options are visible only when notarizing with Xcode altool.

See [Notarizing macOS Software Before Distribution](https://developer.apple.com/documentation/security/notarizing_macos_software_before_distribution?language=objc) for more info.

### Entitlements

#### Hardened Runtime Entitlements

Hardened Runtime entitlements manage security options and resource access policy. See [Hardened Runtime](https://developer.apple.com/documentation/security/hardened_runtime?language=objc) for more info.

| Entitlement                          | Description                                                                                                                                                                                      |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Allow JIT Code Execution [4]         | Allows creating writable and executable memory for JIT code. If you are using add-ons with dynamic or self-modifying native code, enable them according to the add-on documentation.             |
| Allow Unsigned Executable Memory [4] | Allows creating writable and executable memory without JIT restrictions. If you are using add-ons with dynamic or self-modifying native code, enable them according to the add-on documentation. |
| Allow DYLD Environment Variables [4] | Allows app to uss dynamic linker environment variables to inject code. If you are using add-ons with dynamic or self-modifying native code, enable them according to the add-on documentation.   |
| Disable Library Validation           | Allows app to load arbitrary libraries and frameworks. Enable it if you are using GDExtension add-ons or ad-hoc signing, or want to support user-provided external add-ons.                      |
| Audio Input                          | Enable if you need to use the microphone or other audio input sources, if it's enabled you should also provide usage message in the privacy/microphone_usage_description option.                 |
| Camera                               | Enable if you need to use the camera, if it's enabled you should also provide usage message in the privacy/camera_usage_description option.                                                      |
| Location                             | Enable if you need to use location information from Location Services, if it's enabled you should also provide usage message in the privacy/location_usage_description option.                   |
| Address Book                         | [5] Enable to allow access contacts in the user's address book, if it's enabled you should also provide usage message in the privacy/address_book_usage_description option.                      |
| Calendars                            | [5] Enable to allow access to the user's calendar, if it's enabled you should also provide usage message in the privacy/calendar_usage_description option.                                       |
| Photo Library                        | [5] Enable to allow access to the user's Photos library, if it's enabled you should also provide usage message in the privacy/photos_library_usage_description option.                           |
| Apple Events                         | [5] Enable to allow app to send Apple events to other apps.                                                                                                                                      |
| Debugging                            | [6] You can temporarily enable this entitlement to use native debugger (GDB, LLDB) with the exported app. This entitlement should be disabled for production export.                             |

[4] (**1**,**2**,**3**)

The `Allow JIT Code Execution`, `Allow Unsigned Executable Memory` and `Allow DYLD Environment Variables` entitlements are always enabled for the Godot Mono exports, and are not visible in the export options.

[5] (**1**,**2**,**3**,**4**)

These features aren't supported by Godot out of the box, enable them only if you are using add-ons which require them.

[**6**]

To notarize an app, you must disable the `Debugging` entitlement.

#### App Sandbox Entitlement

The App Sandbox restricts access to user data, networking and devices. Sandboxed apps can't access most of the file system, can't use custom file dialogs and execute binaries (using `OS.execute` and `OS.create_process`) outside the `.app` bundle. See [App Sandbox](https://developer.apple.com/documentation/security/app_sandbox?language=objc) for more info.

> **Note:** To distribute an app through the App Store, you must enable the App Sandbox.

| Entitlement             | Description                                                                                                                         |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| Enabled                 | Enables App Sandbox.                                                                                                                |
| Network Server          | Enable to allow app to listen for incoming network connections.                                                                     |
| Network Client          | Enable to allow app to establish outgoing network connections.                                                                      |
| Device USB              | Enable to allow app to interact with USB devices. This entitlement is required to use wired controllers.                            |
| Device Bluetooth        | Enable to allow app to interact with Bluetooth devices. This entitlement is required to use wireless controllers.                   |
| Files Downloads [7]     | Allows read or write access to the user's "Downloads" folder.                                                                       |
| Files Pictures [7]      | Allows read or write access to the user's "Pictures" folder.                                                                        |
| Files Music [7]         | Allows read or write access to the user's "Music" folder.                                                                           |
| Files Movies [7]        | Allows read or write access to the user's "Movies" folder.                                                                          |
| Files User Selected [7] | Allows read or write access to arbitrary folder. To gain access, a folder must be selected from the native file dialog by the user. |
| Helper Executable       | List of helper executables to embedded to the app bundle. Sandboxed app are limited to execute only these executable.               |

[7] (**1**,**2**,**3**,**4**,**5**)

You can optionally provide usage messages for various folders in the privacy/\*\_folder_usage_description options.

> **Note:** You can override default entitlements by selecting custom entitlements file, in this case all other entitlement are ignored.

### Environment variables

You can use the following environment variables to set export options outside of the editor. During the export process, these override the values that you set in the export menu.

| Export option                              | Environment variable                       |
| ------------------------------------------ | ------------------------------------------ |
| Encryption / Encryption Key                | GODOT_SCRIPT_ENCRYPTION_KEY                |
| Options / Codesign / Certificate File      | GODOT_MACOS_CODESIGN_CERTIFICATE_FILE      |
| Options / Codesign / Certificate Password  | GODOT_MACOS_CODESIGN_CERTIFICATE_PASSWORD  |
| Options / Codesign / Provisioning Profile  | GODOT_MACOS_CODESIGN_PROVISIONING_PROFILE  |
| Options / Notarization / API UUID          | GODOT_MACOS_NOTARIZATION_API_UUID          |
| Options / Notarization / API Key           | GODOT_MACOS_NOTARIZATION_API_KEY           |
| Options / Notarization / API Key ID        | GODOT_MACOS_NOTARIZATION_API_KEY_ID        |
| Options / Notarization / Apple ID Name     | GODOT_MACOS_NOTARIZATION_APPLE_ID_NAME     |
| Options / Notarization / Apple ID Password | GODOT_MACOS_NOTARIZATION_APPLE_ID_PASSWORD |

### Export options

You can find a full list of export options available in the [EditorExportPlatformMacOS](../godot_gdscript_editor.md) class reference.

---

## Exporting for visionOS

> **See also:** This page describes how to export a Godot project to visionOS. If you're looking to compile export template binaries from source instead, see Compiling for visionOS.

Exporting instructions for visionOS are currently identical to Compiling for iOS, except you should add a **visionOS** export preset instead of **iOS**. See the linked page for details.

> **Note:** Note that currently, only exporting an application for use on a flat plane within the headset is supported. Immersive experiences are not supported.

---
