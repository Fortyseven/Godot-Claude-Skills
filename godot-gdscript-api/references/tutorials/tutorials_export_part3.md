# Godot 4 GDScript Tutorials — Export (Part 3)

> 2 tutorials. GDScript-specific code examples.

## One-click deploy

### What is one-click deploy?

One-click deploy is a feature that is available once a platform is properly configured and a supported device is connected to the computer. Since things can go wrong at many levels (platform may not be configured correctly, SDK may be incorrectly installed, device may be improperly configured, etc.), it's good to let the user know that it exists.

After adding an Android export preset marked as Runnable, Godot can detect when a USB device is connected to the computer and offer the user to automatically export, install and run the project (in debug mode) on the device. This feature is called _one-click deploy_.

> **Note:** One-click deploy is only available once you've added an export template marked as **Runnable** in the Export dialog. You can mark several export presets as runnable, but only one preset per platform may be marked as runnable. If you mark a second preset in a given platform as runnable, the other preset will no longer be marked as runnable.

### Supported platforms

- **Android:** Exports the project with debugging enabled and runs it on the connected device.

- Make sure to follow the steps described in Exporting for Android. Otherwise, the one-click deploy button won't appear.
- If you have more than one device connected, Godot will ask you which device the project should be exported to.
- **iOS:** Exports the project with debugging enabled and runs it on the connected device.

- Make sure to follow the steps described in Exporting for iOS. Otherwise, the one-click deploy button won't appear.
- For each new bundle identifier, export the project, open it in the Xcode, and build at least once to create new provisioning profile or create a provisioning profile in the Apple Developer account dashboard.
- If you have more than one device connected, Godot will ask you which device the project should be exported to.
- **Desktop platforms:** Exports the project with debugging enabled and runs it on the remote computer via SSH.
- **Web:** Starts a local web server and runs the exported project by opening the default web browser. This is only accessible on `localhost` by default. See **Troubleshooting** for making the exported project accessible on remote devices.

### Using one-click deploy

- **Android:**
  : - Enable developer mode on your mobile device then enable USB debugging in the device's settings.
- After enabling USB debugging, connect the device to your PC using a USB cable.
- **It's also possible to one-click deploy via wireless ADB instead of with a USB cable. In order to do this, it is necessary to:**
  : - Enable wireless debugging on the device: Settings > Developer options > Debugging
- Connect to the same Wi-Fi network on your mobile device and PC.
- Click Pair device with pairing code: (can be accessed via long press on wireless debugging) to display IP, port, and pairing code.
- On your PC, enter the command `adb pair <ip address>:<port>` and provide the pairing code when prompted. If `adb` is not recognized, you may need to add the android-sdk's platform-tools folder to your `PATH` or execute this command from there.
- You can verify the ADB device is successfully connected by entering `adb devices` in the terminal.
- **iOS:**
  : - Install Xcode, accept Xcode license and login with your Apple Developer account.
- If you are using Xcode 14 or earlier, install [ios-deploy](https://github.com/ios-control/ios-deploy) and set path to ios-deploy in the Editor Settings (see Export ⇾ iOS ⇾ iOS Deploy).
- **For running on device:**
  : - Pair your mobile device with a Mac.
- Enable developer mode on your device.
- Device can be connected via USB or local network.
- Make sure the device is on the same local network and a correct network interface is selected in the editor settings (see Network ⇾ Debug ⇾ Remote Host). By default, the editor is listening for localhost connections only.
- Device screen should be unlocked.
- **Desktop platforms:**
  : - Enable SSH Remote Deploy and configure connection settings in the project export setting.
- Make sure there is an export preset marked as **Runnable** for the target platform (Android, iOS or Web).
- If everything is configured correctly and with no errors, platform-specific icons will appear in the top-right corner of the editor.
- Click the button to export to the desired platform in one click.

### Troubleshooting

#### Android

If you can't see the device in the list of devices when running the `adb devices` command in a terminal, it will not be visible by Godot either. To resolve this:

- Check if USB debugging is enabled _and authorized on the device_. Try unlocking your device and accepting the authorization prompt if you see any. If you can't see this prompt, running `adb devices` on your PC should make the authorization prompt appear on the device.
- Try [revoking the debugging authorization](https://stackoverflow.com/questions/23081263/adb-android-device-unauthorized) in the device's developer settings, then follow the steps again.
- Try using USB debugging instead of wireless debugging or vice versa. Sometimes, one of those can work better than the other.
- On Linux, you may be missing the required [udev rules](https://github.com/M0Rf30/android-udev-rules) for your device to be recognized.

#### Web

By default, the web server started by the editor is only accessible from `localhost`. This means the web server can't be reached by other devices on the local network or the Internet (if port forwarding is set up on the router). This is done for security reasons, as you may not want other devices to be able to access the exported project while you're testing it. Binding to `localhost` also prevents a firewall popup from appearing when you use one-click deploy for the web platform.

To make the local web server accessible over the local network, you'll need to change the **Export > Web > HTTP Host** editor setting to `0.0.0.0`. You will also need to enable **Export > Web > Use TLS** as SharedArrayBuffer requires the use of a secure connection to work, _unless_ connecting to `localhost`. However, since other clients will be connecting to a remote device, the use of TLS is absolutely required here.

To make the local web server accessible over the Internet, you'll also need to forward the **Export > Web > HTTP Port** port specified in the Editor Settings (`8060` by default) in TCP on your router. This is usually done by accessing your router's web interface then adding a NAT rule for the port in question. For IPv6 connections, you should allow the port in the router's IPv6 firewall instead. Like for local network devices, you will also need to enable **Export > Web > Use TLS**.

> **Note:** When **Use TLS** is enabled, you will get a warning from your web browser as Godot will use a temporary self-signed certificate. You can safely ignore it and bypass the warning by clicking **Advanced** and then **Proceed to (address)**. If you have an SSL/TLS certificate that is trusted by browsers, you can specify the paths to the key and certificate files in the **Export > Web > TLS Key** and **Export > Web > TLS Certificate**. This will only work if the project is accessed through a domain name that is part of the TLS certificate.

> **Warning:** When using one-click deploy on different projects, it's possible that a previously edited project is being shown instead. This is due to service worker caching not being cleared automatically. See Troubleshooting for instructions on unregistering the service worker, which will effectively clear the cache and resolve the issue.

---

## Running Godot apps on macOS

> **See also:** This page covers running Godot projects on macOS. If you haven't exported your project yet, read Exporting for macOS first.

By default, macOS will run only applications that are signed and notarized.

> **Note:** When running an app from the Downloads folder or when still in quarantine, Gatekeeper will perform _path randomization_ as a security measure. This breaks access to relative paths from the app, which the app relies upon to work. To resolve this issue, move the app to the `/Applications` folder. In general, macOS apps should avoid relying on relative paths from the application folder.

Depending on the way a macOS app is signed and distributed, the following scenarios are possible:

### App is signed, notarized and distributed via App Store

> **Note:** App developers need to join the Apple Developer Program, and configure signing and notarization options during export, then upload the app to the App Store.

The app should run out of the box, without extra user interaction required.

### App is signed, notarized and distributed outside App Store

> **Note:** App developers need to join the Apple Developer Program, and configure signing and notarization options during export, then distribute the app as ".DMG" or ".ZIP" archive.

When you run the app for the first time, the following dialog is displayed:

Click `Open` to start the app.

If you see the following warning dialog, your Mac is set up to allow apps only from the App Store.

To allow third-party apps, open `System Preferences`, click `Security & Privacy`, then click `General`, unlock settings, and select `App Store and identified developers`.

### App is signed (including ad-hoc signatures) but not notarized

> **Note:** App developer used self-signed certificate or ad-hoc signing (default Godot behavior for exported project).

When you run the app for the first time, the following dialog is displayed:

To run this app, you can temporarily override Gatekeeper:

- Either open `System Preferences`, click `Security & Privacy`, then click `General`, and click `Open Anyway`.
- Or, right-click (Control-click) on the app icon in the Finder window and select `Open` from the menu.
- Then click `Open` in the confirmation dialog.
- Enter your password if you're prompted.

Another option is to disable Gatekeeper entirely. Note that this does decrease the security of your computer by allowing you to run any software you want. To do this, run `sudo spctl --master-disable` in the Terminal, enter your password, and then the **Anywhere** option will be available:

Note that Gatekeeper will re-enable itself when macOS updates.

### App is not signed, executable is linker-signed

> **Note:** App is built using official export templates, but it is not signed.

When you run the app for the first time, the following dialog is displayed:

To run this app, you should remove the quarantine extended file attribute manually:

- Open `Terminal.app` (press Cmd + Space and enter `Terminal`).
- Navigate to the folder containing the target application.

Use the `cd path_to_the_app_folder` command, e.g. `cd ~/Downloads/` if it's in the `Downloads` folder.

- Run the command `xattr -dr com.apple.quarantine "Unsigned Game.app"` (including quotation marks and `.app` extension).

### Neither app nor executable is signed (relevant for Apple Silicon Macs only)

> **Note:** App is built using custom export templates, compiled using OSXCross, and it is not signed at all.

When you run the app for the first time, the following dialog is displayed:

To run this app, you can ad-hoc sign it yourself:

- Install `Xcode` for the App Store, start it and confirm command line tools installation.
- Open `Terminal.app` (press Cmd + Space and enter `Terminal`).
- Navigate to the folder containing the target application.

Use the `cd path_to_the_app_folder` command, e.g. `cd ~/Downloads/` if it's in the `Downloads` folder.

- Run the following commands:

`xattr -dr com.apple.quarantine "Unsigned Game.app"` (including quotation marks and ".app" extension).

`codesign -s - --force --deep "Unsigned Game.app"` (including quotation marks and ".app" extension).

---
