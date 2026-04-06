# Godot 4 C# API Reference — Editor

> C#-only reference. 53 classes.

### EditorCommandPalette
*Inherits: **ConfirmationDialog < AcceptDialog < Window < Viewport < Node < Object***

Object that holds all the available Commands and their shortcuts text. These Commands can be accessed through Editor > Command Palette menu.

**Properties**
- `bool DialogHideOnOk` = `false (overrides AcceptDialog)`

**Methods**
- `void AddCommand(string commandName, string keyName, Callable bindedCallable, string shortcutText = "None")`
- `void RemoveCommand(string keyName)`

**C# Examples**
```csharp
EditorCommandPalette commandPalette = EditorInterface.Singleton.GetCommandPalette();
// ExternalCommand is a function that will be called with the command is executed.
Callable commandCallable = new Callable(this, MethodName.ExternalCommand);
commandPalette.AddCommand("command", "test/command", commandCallable)
```

### EditorContextMenuPlugin
*Inherits: **RefCounted < Object***

EditorContextMenuPlugin allows for the addition of custom options in the editor's context menu.

**Methods**
- `void _PopupMenu(PackedStringArray paths) [virtual]`
- `void AddContextMenuItem(string name, Callable callback, Texture2D icon = null)`
- `void AddContextMenuItemFromShortcut(string name, Shortcut shortcut, Texture2D icon = null)`
- `void AddContextSubmenuItem(string name, PopupMenu menu, Texture2D icon = null)`
- `void AddMenuShortcut(Shortcut shortcut, Callable callback)`

### EditorDebuggerPlugin
*Inherits: **RefCounted < Object***

EditorDebuggerPlugin provides functions related to the editor side of the debugger.

**Methods**
- `void _BreakpointSetInTree(Script script, int line, bool enabled) [virtual]`
- `void _BreakpointsClearedInTree() [virtual]`
- `bool _Capture(string message, Godot.Collections.Array data, int sessionId) [virtual]`
- `void _GotoScriptLine(Script script, int line) [virtual]`
- `bool _HasCapture(string capture) [virtual]`
- `void _SetupSession(int sessionId) [virtual]`
- `EditorDebuggerSession GetSession(int id)`
- `Godot.Collections.Array GetSessions()`

### EditorDebuggerSession
*Inherits: **RefCounted < Object***

This class cannot be directly instantiated and must be retrieved via an EditorDebuggerPlugin.

**Methods**
- `void AddSessionTab(Control control)`
- `bool IsActive()`
- `bool IsBreaked()`
- `bool IsDebuggable()`
- `void RemoveSessionTab(Control control)`
- `void SendMessage(string message, Godot.Collections.Array data = [])`
- `void SetBreakpoint(string path, int line, bool enabled)`
- `void ToggleProfiler(string profiler, bool enable, Godot.Collections.Array data = [])`

### EditorDock
*Inherits: **MarginContainer < Container < Control < CanvasItem < Node < Object** | Inherited by: FileSystemDock*

EditorDock is a Container node that can be docked in one of the editor's dock slots. Docks are added by plugins to provide space for controls related to an EditorPlugin. The editor comes with a few built-in docks, such as the Scene dock, FileSystem dock, etc.

**Properties**
- `BitField[DockLayout] AvailableLayouts` = `5`
- `bool Closable` = `false`
- `DockSlot DefaultSlot` = `-1`
- `Texture2D DockIcon`
- `Shortcut DockShortcut`
- `bool ForceShowIcon` = `false`
- `bool Global` = `true`
- `StringName IconName` = `&""`
- `string LayoutKey` = `""`
- `string Title` = `""`
- `Color TitleColor` = `Color(0, 0, 0, 0)`
- `bool Transient` = `false`

**Methods**
- `void _LoadLayoutFromConfig(ConfigFile config, string section) [virtual]`
- `void _SaveLayoutToConfig(ConfigFile config, string section) [virtual]`
- `void _UpdateLayout(int layout) [virtual]`
- `void Close()`
- `void MakeVisible()`
- `void Open()`

### EditorExportPlatformAndroid
*Inherits: **EditorExportPlatform < RefCounted < Object***

Exporter for Android.

**Properties**
- `string ApkExpansion/salt`
- `bool ApkExpansion/enable`
- `string ApkExpansion/publicKey`
- `bool Architectures/arm64-v8a`
- `bool Architectures/armeabi-v7a`
- `bool Architectures/x86`
- `bool Architectures/x8664`
- `string CommandLine/extraArgs`
- `string CustomTemplate/debug`
- `string CustomTemplate/release`
- `bool Gesture/swipeToDismiss`
- `string GradleBuild/androidSourceTemplate`
- `bool GradleBuild/compressNativeLibraries`
- `Godot.Collections.Dictionary GradleBuild/customThemeAttributes`
- `int GradleBuild/exportFormat`
- `string GradleBuild/gradleBuildDirectory`
- `string GradleBuild/minSdk`
- `string GradleBuild/targetSdk`
- `bool GradleBuild/useGradleBuild`
- `bool Graphics/openglDebug`
- `string Keystore/debug`
- `string Keystore/debugPassword`
- `string Keystore/debugUser`
- `string Keystore/release`
- `string Keystore/releasePassword`
- `string Keystore/releaseUser`
- `string LauncherIcons/adaptiveBackground432x432`
- `string LauncherIcons/adaptiveForeground432x432`
- `string LauncherIcons/adaptiveMonochrome432x432`
- `string LauncherIcons/main192x192`

### EditorExportPlatformAppleEmbedded
*Inherits: **EditorExportPlatform < RefCounted < Object** | Inherited by: EditorExportPlatformIOS, EditorExportPlatformVisionOS*

The base class for Apple embedded platform exporters. These include iOS and visionOS, but not macOS. See the classes inheriting from this one for more details.

### EditorExportPlatformExtension
*Inherits: **EditorExportPlatform < RefCounted < Object***

External EditorExportPlatform implementations should inherit from this class.

**Methods**
- `bool _CanExport(EditorExportPreset preset, bool debug) [virtual]`
- `void _Cleanup() [virtual]`
- `Error _ExportPack(EditorExportPreset preset, bool debug, string path, BitField[DebugFlags] flags) [virtual]`
- `Error _ExportPackPatch(EditorExportPreset preset, bool debug, string path, PackedStringArray patches, BitField[DebugFlags] flags) [virtual]`
- `Error _ExportProject(EditorExportPreset preset, bool debug, string path, BitField[DebugFlags] flags) [virtual]`
- `Error _ExportZip(EditorExportPreset preset, bool debug, string path, BitField[DebugFlags] flags) [virtual]`
- `Error _ExportZipPatch(EditorExportPreset preset, bool debug, string path, PackedStringArray patches, BitField[DebugFlags] flags) [virtual]`
- `PackedStringArray _GetBinaryExtensions(EditorExportPreset preset) [virtual]`
- `string _GetDebugProtocol() [virtual]`
- `string _GetDeviceArchitecture(int device) [virtual]`
- `bool _GetExportOptionVisibility(EditorExportPreset preset, string option) [virtual]`
- `string _GetExportOptionWarning(EditorExportPreset preset, StringName option) [virtual]`
- `Array[Dictionary] _GetExportOptions() [virtual]`
- `Texture2D _GetLogo() [virtual]`
- `string _GetName() [virtual]`
- `Texture2D _GetOptionIcon(int device) [virtual]`
- `string _GetOptionLabel(int device) [virtual]`
- `string _GetOptionTooltip(int device) [virtual]`
- `int _GetOptionsCount() [virtual]`
- `string _GetOptionsTooltip() [virtual]`
- `string _GetOsName() [virtual]`
- `PackedStringArray _GetPlatformFeatures() [virtual]`
- `PackedStringArray _GetPresetFeatures(EditorExportPreset preset) [virtual]`
- `Texture2D _GetRunIcon() [virtual]`
- `bool _HasValidExportConfiguration(EditorExportPreset preset, bool debug) [virtual]`
- `bool _HasValidProjectConfiguration(EditorExportPreset preset) [virtual]`
- `void _Initialize() [virtual]`
- `bool _IsExecutable(string path) [virtual]`
- `bool _PollExport() [virtual]`
- `Error _Run(EditorExportPreset preset, int device, BitField[DebugFlags] debugFlags) [virtual]`
- `bool _ShouldUpdateExportOptions() [virtual]`
- `string GetConfigError()`
- `bool GetConfigMissingTemplates()`
- `void SetConfigError(string errorText)`
- `void SetConfigMissingTemplates(bool missingTemplates)`

### EditorExportPlatformIOS
*Inherits: **EditorExportPlatformAppleEmbedded < EditorExportPlatform < RefCounted < Object***

Exporter for iOS.

**Properties**
- `string Application/additionalPlistContent`
- `string Application/appStoreTeamId`
- `string Application/bundleIdentifier`
- `string Application/codeSignIdentityDebug`
- `string Application/codeSignIdentityRelease`
- `bool Application/deleteOldExportFilesUnconditionally`
- `int Application/exportMethodDebug`
- `int Application/exportMethodRelease`
- `bool Application/exportProjectOnly`
- `int Application/iconInterpolation`
- `string Application/minIosVersion`
- `string Application/provisioningProfileSpecifierDebug`
- `string Application/provisioningProfileSpecifierRelease`
- `string Application/provisioningProfileUuidDebug`
- `string Application/provisioningProfileUuidRelease`
- `string Application/shortVersion`
- `string Application/signature`
- `int Application/targetedDeviceFamily`
- `string Application/version`
- `bool Architectures/arm64`
- `bool Capabilities/accessWifi`
- `PackedStringArray Capabilities/additional`
- `bool Capabilities/performanceA12`
- `bool Capabilities/performanceGamingTier`
- `string CustomTemplate/debug`
- `string CustomTemplate/release`
- `string Entitlements/additional`
- `bool Entitlements/gameCenter`
- `bool Entitlements/increasedMemoryLimit`
- `string Entitlements/pushNotifications`

### EditorExportPlatformLinuxBSD
*Inherits: **EditorExportPlatformPC < EditorExportPlatform < RefCounted < Object***

Exporter for Linux/BSD.

**Properties**
- `string BinaryFormat/architecture`
- `bool BinaryFormat/embedPck`
- `string CustomTemplate/debug`
- `string CustomTemplate/release`
- `int Debug/exportConsoleWrapper`
- `bool ShaderBaker/enabled`
- `string SshRemoteDeploy/cleanupScript`
- `bool SshRemoteDeploy/enabled`
- `string SshRemoteDeploy/extraArgsScp`
- `string SshRemoteDeploy/extraArgsSsh`
- `string SshRemoteDeploy/host`
- `string SshRemoteDeploy/port`
- `string SshRemoteDeploy/runScript`
- `bool TextureFormat/etc2Astc`
- `bool TextureFormat/s3tcBptc`

### EditorExportPlatformMacOS
*Inherits: **EditorExportPlatform < RefCounted < Object***

Exporter for macOS.

**Properties**
- `string Application/additionalPlistContent`
- `string Application/appCategory`
- `string Application/bundleIdentifier`
- `string Application/copyright`
- `Godot.Collections.Dictionary Application/copyrightLocalized`
- `int Application/exportAngle`
- `string Application/icon`
- `int Application/iconInterpolation`
- `string Application/liquidGlassIcon`
- `string Application/minMacosVersionArm64`
- `string Application/minMacosVersionX8664`
- `string Application/shortVersion`
- `string Application/signature`
- `string Application/version`
- `string BinaryFormat/architecture`
- `string Codesign/appleTeamId`
- `string Codesign/certificateFile`
- `string Codesign/certificatePassword`
- `int Codesign/codesign`
- `PackedStringArray Codesign/customOptions`
- `string Codesign/entitlements/additional`
- `bool Codesign/entitlements/addressBook`
- `bool Codesign/entitlements/allowDyldEnvironmentVariables`
- `bool Codesign/entitlements/allowJitCodeExecution`
- `bool Codesign/entitlements/allowUnsignedExecutableMemory`
- `bool Codesign/entitlements/appSandbox/deviceBluetooth`
- `bool Codesign/entitlements/appSandbox/deviceUsb`
- `bool Codesign/entitlements/appSandbox/enabled`
- `int Codesign/entitlements/appSandbox/filesDownloads`
- `int Codesign/entitlements/appSandbox/filesMovies`

### EditorExportPlatformPC
*Inherits: **EditorExportPlatform < RefCounted < Object** | Inherited by: EditorExportPlatformLinuxBSD, EditorExportPlatformWindows*

The base class for the desktop platform exporters. These include Windows and Linux/BSD, but not macOS. See the classes inheriting from this one for more details.

### EditorExportPlatformVisionOS
*Inherits: **EditorExportPlatformAppleEmbedded < EditorExportPlatform < RefCounted < Object***

Exporter for visionOS.

**Properties**
- `string Application/additionalPlistContent`
- `string Application/appStoreTeamId`
- `string Application/bundleIdentifier`
- `string Application/codeSignIdentityDebug`
- `string Application/codeSignIdentityRelease`
- `bool Application/deleteOldExportFilesUnconditionally`
- `int Application/exportMethodDebug`
- `int Application/exportMethodRelease`
- `bool Application/exportProjectOnly`
- `int Application/iconInterpolation`
- `string Application/minVisionosVersion`
- `string Application/provisioningProfileSpecifierDebug`
- `string Application/provisioningProfileSpecifierRelease`
- `string Application/provisioningProfileUuidDebug`
- `string Application/provisioningProfileUuidRelease`
- `string Application/shortVersion`
- `string Application/signature`
- `string Application/version`
- `bool Architectures/arm64`
- `bool Capabilities/accessWifi`
- `PackedStringArray Capabilities/additional`
- `bool Capabilities/performanceA12`
- `bool Capabilities/performanceGamingTier`
- `string CustomTemplate/debug`
- `string CustomTemplate/release`
- `string Entitlements/additional`
- `bool Entitlements/gameCenter`
- `bool Entitlements/increasedMemoryLimit`
- `string Entitlements/pushNotifications`
- `string Icons/icon1024x1024`

### EditorExportPlatformWeb
*Inherits: **EditorExportPlatform < RefCounted < Object***

The Web exporter customizes how a web build is handled. In the editor's "Export" window, it is created when adding a new "Web" preset.

**Properties**
- `string CustomTemplate/debug`
- `string CustomTemplate/release`
- `int Html/canvasResizePolicy`
- `string Html/customHtmlShell`
- `bool Html/experimentalVirtualKeyboard`
- `bool Html/exportIcon`
- `bool Html/focusCanvasOnStart`
- `string Html/headInclude`
- `Color ProgressiveWebApp/backgroundColor`
- `int ProgressiveWebApp/display`
- `bool ProgressiveWebApp/enabled`
- `bool ProgressiveWebApp/ensureCrossOriginIsolationHeaders`
- `string ProgressiveWebApp/icon144x144`
- `string ProgressiveWebApp/icon180x180`
- `string ProgressiveWebApp/icon512x512`
- `string ProgressiveWebApp/offlinePage`
- `int ProgressiveWebApp/orientation`
- `int Threads/emscriptenPoolSize`
- `int Threads/godotPoolSize`
- `bool Variant/extensionsSupport`
- `bool Variant/threadSupport`
- `bool VramTextureCompression/forDesktop`
- `bool VramTextureCompression/forMobile`

### EditorExportPlatformWindows
*Inherits: **EditorExportPlatformPC < EditorExportPlatform < RefCounted < Object***

The Windows exporter customizes how a Windows build is handled. In the editor's "Export" window, it is created when adding a new "Windows" preset.

**Properties**
- `string Application/companyName`
- `string Application/consoleWrapperIcon`
- `string Application/copyright`
- `bool Application/d3d12AgilitySdkMultiarch`
- `int Application/exportAngle`
- `int Application/exportD3d12`
- `string Application/fileDescription`
- `string Application/fileVersion`
- `string Application/icon`
- `int Application/iconInterpolation`
- `bool Application/modifyResources`
- `string Application/productName`
- `string Application/productVersion`
- `string Application/trademarks`
- `string BinaryFormat/architecture`
- `bool BinaryFormat/embedPck`
- `PackedStringArray Codesign/customOptions`
- `string Codesign/description`
- `int Codesign/digestAlgorithm`
- `bool Codesign/enable`
- `string Codesign/identity`
- `int Codesign/identityType`
- `string Codesign/password`
- `bool Codesign/timestamp`
- `string Codesign/timestampServerUrl`
- `string CustomTemplate/debug`
- `string CustomTemplate/release`
- `int Debug/exportConsoleWrapper`
- `bool ShaderBaker/enabled`
- `string SshRemoteDeploy/cleanupScript`

### EditorExportPlatform
*Inherits: **RefCounted < Object** | Inherited by: EditorExportPlatformAndroid, EditorExportPlatformAppleEmbedded, EditorExportPlatformExtension, EditorExportPlatformMacOS, EditorExportPlatformPC, EditorExportPlatformWeb*

Base resource that provides the functionality of exporting a release build of a project to a platform, from the editor. Stores platform-specific metadata such as the name and supported features of the platform, and performs the exporting of projects, PCK files, and ZIP files. Uses an export template for the platform provided at the time of project exporting.

**Methods**
- `void AddMessage(ExportMessageType type, string category, string message)`
- `void ClearMessages()`
- `EditorExportPreset CreatePreset()`
- `Error ExportPack(EditorExportPreset preset, bool debug, string path, BitField[DebugFlags] flags = 0)`
- `Error ExportPackPatch(EditorExportPreset preset, bool debug, string path, PackedStringArray patches = PackedStringArray(), BitField[DebugFlags] flags = 0)`
- `Error ExportProject(EditorExportPreset preset, bool debug, string path, BitField[DebugFlags] flags = 0)`
- `Error ExportProjectFiles(EditorExportPreset preset, bool debug, Callable saveCb, Callable sharedCb = Callable())`
- `Error ExportZip(EditorExportPreset preset, bool debug, string path, BitField[DebugFlags] flags = 0)`
- `Error ExportZipPatch(EditorExportPreset preset, bool debug, string path, PackedStringArray patches = PackedStringArray(), BitField[DebugFlags] flags = 0)`
- `Godot.Collections.Dictionary FindExportTemplate(string templateFileName)`
- `PackedStringArray GenExportFlags(BitField[DebugFlags] flags)`
- `Godot.Collections.Array GetCurrentPresets()`
- `PackedStringArray GetForcedExportFiles(EditorExportPreset preset = null) [static]`
- `Godot.Collections.Dictionary GetInternalExportFiles(EditorExportPreset preset, bool debug)`
- `string GetMessageCategory(int index)`
- `int GetMessageCount()`
- `string GetMessageText(int index)`
- `ExportMessageType GetMessageType(int index)`
- `string GetOsName()`
- `ExportMessageType GetWorstMessageType()`
- `Godot.Collections.Dictionary SavePack(EditorExportPreset preset, bool debug, string path, bool embed = false)`
- `Godot.Collections.Dictionary SavePackPatch(EditorExportPreset preset, bool debug, string path)`
- `Godot.Collections.Dictionary SaveZip(EditorExportPreset preset, bool debug, string path)`
- `Godot.Collections.Dictionary SaveZipPatch(EditorExportPreset preset, bool debug, string path)`
- `Error SshPushToRemote(string host, string port, PackedStringArray scpArgs, string srcFile, string dstFile)`
- `Error SshRunOnRemote(string host, string port, PackedStringArray sshArg, string cmdArgs, Godot.Collections.Array output = [], int portFwd = -1)`
- `int SshRunOnRemoteNoWait(string host, string port, PackedStringArray sshArgs, string cmdArgs, int portFwd = -1)`

### EditorExportPlugin
*Inherits: **RefCounted < Object***

EditorExportPlugins are automatically invoked whenever the user exports the project. Their most common use is to determine what files are being included in the exported project. For each plugin, _export_begin() is called at the beginning of the export process and then _export_file() is called for each exported file.

**Methods**
- `bool _BeginCustomizeResources(EditorExportPlatform platform, PackedStringArray features) [virtual]`
- `bool _BeginCustomizeScenes(EditorExportPlatform platform, PackedStringArray features) [virtual]`
- `Resource _CustomizeResource(Resource resource, string path) [virtual]`
- `Node _CustomizeScene(Node scene, string path) [virtual]`
- `void _EndCustomizeResources() [virtual]`
- `void _EndCustomizeScenes() [virtual]`
- `void _ExportBegin(PackedStringArray features, bool isDebug, string path, int flags) [virtual]`
- `void _ExportEnd() [virtual]`
- `void _ExportFile(string path, string type, PackedStringArray features) [virtual]`
- `PackedStringArray _GetAndroidDependencies(EditorExportPlatform platform, bool debug) [virtual]`
- `PackedStringArray _GetAndroidDependenciesMavenRepos(EditorExportPlatform platform, bool debug) [virtual]`
- `PackedStringArray _GetAndroidLibraries(EditorExportPlatform platform, bool debug) [virtual]`
- `string _GetAndroidManifestActivityElementContents(EditorExportPlatform platform, bool debug) [virtual]`
- `string _GetAndroidManifestApplicationElementContents(EditorExportPlatform platform, bool debug) [virtual]`
- `string _GetAndroidManifestElementContents(EditorExportPlatform platform, bool debug) [virtual]`
- `int _GetCustomizationConfigurationHash() [virtual]`
- `PackedStringArray _GetExportFeatures(EditorExportPlatform platform, bool debug) [virtual]`
- `bool _GetExportOptionVisibility(EditorExportPlatform platform, string option) [virtual]`
- `string _GetExportOptionWarning(EditorExportPlatform platform, string option) [virtual]`
- `Array[Dictionary] _GetExportOptions(EditorExportPlatform platform) [virtual]`
- `Godot.Collections.Dictionary _GetExportOptionsOverrides(EditorExportPlatform platform) [virtual]`
- `string _GetName() [virtual]`
- `bool _ShouldUpdateExportOptions(EditorExportPlatform platform) [virtual]`
- `bool _SupportsPlatform(EditorExportPlatform platform) [virtual]`
- `PackedByteArray _UpdateAndroidPrebuiltManifest(EditorExportPlatform platform, PackedByteArray manifestData) [virtual]`
- `void AddAppleEmbeddedPlatformBundleFile(string path)`
- `void AddAppleEmbeddedPlatformCppCode(string code)`
- `void AddAppleEmbeddedPlatformEmbeddedFramework(string path)`
- `void AddAppleEmbeddedPlatformFramework(string path)`
- `void AddAppleEmbeddedPlatformLinkerFlags(string flags)`
- `void AddAppleEmbeddedPlatformPlistContent(string plistContent)`
- `void AddAppleEmbeddedPlatformProjectStaticLib(string path)`
- `void AddFile(string path, PackedByteArray file, bool remap)`
- `void AddIosBundleFile(string path)`
- `void AddIosCppCode(string code)`
- `void AddIosEmbeddedFramework(string path)`
- `void AddIosFramework(string path)`
- `void AddIosLinkerFlags(string flags)`
- `void AddIosPlistContent(string plistContent)`
- `void AddIosProjectStaticLib(string path)`

### EditorExportPreset
*Inherits: **RefCounted < Object***

Represents the configuration of an export preset, as created by the editor's export dialog. An EditorExportPreset instance is intended to be used a read-only configuration passed to the EditorExportPlatform methods when exporting the project.

**Methods**
- `bool AreAdvancedOptionsEnabled()`
- `string GetCustomFeatures()`
- `Godot.Collections.Dictionary GetCustomizedFiles()`
- `int GetCustomizedFilesCount()`
- `bool GetEncryptDirectory()`
- `bool GetEncryptPck()`
- `string GetEncryptionExFilter()`
- `string GetEncryptionInFilter()`
- `string GetEncryptionKey()`
- `string GetExcludeFilter()`
- `ExportFilter GetExportFilter()`
- `string GetExportPath()`
- `FileExportMode GetFileExportMode(string path, FileExportMode default = 0)`
- `PackedStringArray GetFilesToExport()`
- `string GetIncludeFilter()`
- `Variant GetOrEnv(StringName name, string envVar)`
- `PackedStringArray GetPatches()`
- `string GetPresetName()`
- `Variant GetProjectSetting(StringName name)`
- `ScriptExportMode GetScriptExportMode()`
- `string GetVersion(StringName name, bool windowsVersion)`
- `bool Has(StringName property)`
- `bool HasExportFile(string path)`
- `bool IsDedicatedServer()`
- `bool IsRunnable()`

### EditorFeatureProfile
*Inherits: **RefCounted < Object***

An editor feature profile can be used to disable specific features of the Godot editor. When disabled, the features won't appear in the editor, which makes the editor less cluttered. This is useful in education settings to reduce confusion or when working in a team. For example, artists and level designers could use a feature profile that disables the script editor to avoid accidentally making changes to files they aren't supposed to edit.

**Methods**
- `string GetFeatureName(Feature feature)`
- `bool IsClassDisabled(StringName className)`
- `bool IsClassEditorDisabled(StringName className)`
- `bool IsClassPropertyDisabled(StringName className, StringName property)`
- `bool IsFeatureDisabled(Feature feature)`
- `Error LoadFromFile(string path)`
- `Error SaveToFile(string path)`
- `void SetDisableClass(StringName className, bool disable)`
- `void SetDisableClassEditor(StringName className, bool disable)`
- `void SetDisableClassProperty(StringName className, StringName property, bool disable)`
- `void SetDisableFeature(Feature feature, bool disable)`

### EditorFileDialog
*Inherits: **FileDialog < ConfirmationDialog < AcceptDialog < Window < Viewport < Node < Object***

EditorFileDialog is a FileDialog tweaked to work in the editor. It automatically handles favorite and recent directory lists, and synchronizes some properties with their corresponding editor settings.

**Properties**
- `bool DisableOverwriteWarning` = `false`

**Methods**
- `void AddSideMenu(Control menu, string title = "")`

### EditorFileSystemDirectory
*Inherits: **Object***

A more generalized, low-level variation of the directory concept.

**Methods**
- `int FindDirIndex(string name)`
- `int FindFileIndex(string name)`
- `string GetFile(int idx)`
- `int GetFileCount()`
- `bool GetFileImportIsValid(int idx)`
- `string GetFilePath(int idx)`
- `string GetFileScriptClassExtends(int idx)`
- `string GetFileScriptClassName(int idx)`
- `StringName GetFileType(int idx)`
- `string GetName()`
- `EditorFileSystemDirectory GetParent()`
- `string GetPath()`
- `EditorFileSystemDirectory GetSubdir(int idx)`
- `int GetSubdirCount()`

### EditorFileSystemImportFormatSupportQuery
*Inherits: **RefCounted < Object***

This class is used to query and configure a certain import format. It is used in conjunction with asset format import plugins.

**Methods**
- `PackedStringArray _GetFileExtensions() [virtual]`
- `bool _IsActive() [virtual]`
- `bool _Query() [virtual]`

### EditorFileSystem
*Inherits: **Node < Object***

This object holds information of all resources in the filesystem, their types, etc.

**Methods**
- `string GetFileType(string path)`
- `EditorFileSystemDirectory GetFilesystem()`
- `EditorFileSystemDirectory GetFilesystemPath(string path)`
- `float GetScanningProgress()`
- `bool IsScanning()`
- `void ReimportFiles(PackedStringArray files)`
- `void Scan()`
- `void ScanSources()`
- `void UpdateFile(string path)`

### EditorImportPlugin
*Inherits: **ResourceImporter < RefCounted < Object***

EditorImportPlugins provide a way to extend the editor's resource import functionality. Use them to import resources from custom files or to provide alternatives to the editor's existing importers.

**Methods**
- `bool _CanImportThreaded() [virtual]`
- `int _GetFormatVersion() [virtual]`
- `Array[Dictionary] _GetImportOptions(string path, int presetIndex) [virtual]`
- `int _GetImportOrder() [virtual]`
- `string _GetImporterName() [virtual]`
- `bool _GetOptionVisibility(string path, StringName optionName, Godot.Collections.Dictionary options) [virtual]`
- `int _GetPresetCount() [virtual]`
- `string _GetPresetName(int presetIndex) [virtual]`
- `float _GetPriority() [virtual]`
- `PackedStringArray _GetRecognizedExtensions() [virtual]`
- `string _GetResourceType() [virtual]`
- `string _GetSaveExtension() [virtual]`
- `string _GetVisibleName() [virtual]`
- `Error _Import(string sourceFile, string savePath, Godot.Collections.Dictionary options, Array[String] platformVariants, Array[String] genFiles) [virtual]`
- `Error AppendImportExternalResource(string path, Godot.Collections.Dictionary customOptions = {}, string customImporter = "", Variant generatorParameters = null)`

**C# Examples**
```csharp
using Godot;

public partial class MySpecialPlugin : EditorImportPlugin
{
    public override string _GetImporterName()
    {
        return "my.special.plugin";
    }

    public override string _GetVisibleName()
    {
        return "Special Mesh";
    }

    public override string[] _GetRecognizedExtensions()
    {
        return ["special", "spec"];
    }

    public override string _GetSaveExtension()
    {
        return "mesh";
    }

    public override string _GetResourceType()
    {
        return "Mesh";
    }

    public override int _GetPresetCount()
    {
        return 1;
    }

// ...
```
```csharp
public override bool _GetOptionVisibility(string path, StringName optionName, Godot.Collections.Dictionary options)
{
    // Only show the lossy quality setting if the compression mode is set to "Lossy".
    if (optionName == "compress/lossy_quality" && options.ContainsKey("compress/mode"))
    {
        return (int)options["compress/mode"] == CompressLossy; // This is a constant you set
    }

    return true;
}
```

### EditorInspectorPlugin
*Inherits: **RefCounted < Object***

EditorInspectorPlugin allows adding custom property editors to EditorInspector.

**Methods**
- `bool _CanHandle(Object object) [virtual]`
- `void _ParseBegin(Object object) [virtual]`
- `void _ParseCategory(Object object, string category) [virtual]`
- `void _ParseEnd(Object object) [virtual]`
- `void _ParseGroup(Object object, string group) [virtual]`
- `bool _ParseProperty(Object object, Variant.Type type, string name, PropertyHint hintType, string hintString, BitField[PropertyUsageFlags] usageFlags, bool wide) [virtual]`
- `void AddCustomControl(Control control)`
- `void AddPropertyEditor(string property, Control editor, bool addToEnd = false, string label = "")`
- `void AddPropertyEditorForMultipleProperties(string label, PackedStringArray properties, Control editor)`

### EditorInspector
*Inherits: **ScrollContainer < Container < Control < CanvasItem < Node < Object***

This is the control that implements property editing in the editor's Settings dialogs, the Inspector dock, etc. To get the EditorInspector used in the editor's Inspector dock, use EditorInterface.get_inspector().

**Properties**
- `bool DrawFocusBorder` = `true (overrides ScrollContainer)`
- `FocusMode FocusMode` = `2 (overrides Control)`
- `bool FollowFocus` = `true (overrides ScrollContainer)`
- `ScrollMode HorizontalScrollMode` = `0 (overrides ScrollContainer)`

**Methods**
- `void Edit(Object object)`
- `Object GetEditedObject()`
- `string GetSelectedPath()`
- `EditorProperty InstantiatePropertyEditor(Object object, Variant.Type type, string path, PropertyHint hint, string hintText, int usage, bool wide = false) [static]`

### EditorInterface
*Inherits: **Object***

EditorInterface gives you control over Godot editor's window. It allows customizing the window, saving and (re-)loading scenes, rendering mesh previews, inspecting and editing resources and objects, and provides access to EditorSettings, EditorFileSystem, EditorResourcePreview, ScriptEditor, the editor viewport, and information about scenes.

**Properties**
- `bool DistractionFreeMode`
- `bool MovieMakerEnabled`

**Methods**
- `void AddRootNode(Node node)`
- `Error CloseScene()`
- `void EditNode(Node node)`
- `void EditResource(Resource resource)`
- `void EditScript(Script script, int line = -1, int column = 0, bool grabFocus = true)`
- `Control GetBaseControl()`
- `EditorCommandPalette GetCommandPalette()`
- `string GetCurrentDirectory()`
- `string GetCurrentFeatureProfile()`
- `string GetCurrentPath()`
- `Node GetEditedSceneRoot()`
- `string GetEditorLanguage()`
- `VBoxContainer GetEditorMainScreen()`
- `EditorPaths GetEditorPaths()`
- `float GetEditorScale()`
- `EditorSettings GetEditorSettings()`
- `Theme GetEditorTheme()`
- `EditorToaster GetEditorToaster()`
- `EditorUndoRedoManager GetEditorUndoRedo()`
- `SubViewport GetEditorViewport2d()`
- `SubViewport GetEditorViewport3d(int idx = 0)`
- `FileSystemDock GetFileSystemDock()`
- `EditorInspector GetInspector()`
- `float GetNode3dRotateSnap()`
- `float GetNode3dScaleSnap()`
- `float GetNode3dTranslateSnap()`
- `Array[Node] GetOpenSceneRoots()`
- `PackedStringArray GetOpenScenes()`
- `string GetPlayingScene()`
- `EditorFileSystem GetResourceFilesystem()`
- `EditorResourcePreview GetResourcePreviewer()`
- `ScriptEditor GetScriptEditor()`
- `PackedStringArray GetSelectedPaths()`
- `EditorSelection GetSelection()`
- `void InspectObject(Object object, string forProperty = "", bool inspectorOnly = false)`
- `bool IsMultiWindowEnabled()`
- `bool IsNode3dSnapEnabled()`
- `bool IsObjectEdited(Object object)`
- `bool IsPlayingScene()`
- `bool IsPluginEnabled(string plugin)`

**C# Examples**
```csharp
// In C# you can access it via the static Singleton property.
EditorSettings settings = EditorInterface.Singleton.GetEditorSettings();
```

### EditorNode3DGizmoPlugin
*Inherits: **Resource < RefCounted < Object***

EditorNode3DGizmoPlugin allows you to define a new type of Gizmo. There are two main ways to do so: extending EditorNode3DGizmoPlugin for the simpler gizmos, or creating a new EditorNode3DGizmo type. See the tutorial in the documentation for more info.

**Methods**
- `void _BeginHandleAction(EditorNode3DGizmo gizmo, int handleId, bool secondary) [virtual]`
- `bool _CanBeHidden() [virtual]`
- `void _CommitHandle(EditorNode3DGizmo gizmo, int handleId, bool secondary, Variant restore, bool cancel) [virtual]`
- `void _CommitSubgizmos(EditorNode3DGizmo gizmo, PackedInt32Array ids, Array[Transform3D] restores, bool cancel) [virtual]`
- `EditorNode3DGizmo _CreateGizmo(Node3D forNode3d) [virtual]`
- `string _GetGizmoName() [virtual]`
- `string _GetHandleName(EditorNode3DGizmo gizmo, int handleId, bool secondary) [virtual]`
- `Variant _GetHandleValue(EditorNode3DGizmo gizmo, int handleId, bool secondary) [virtual]`
- `int _GetPriority() [virtual]`
- `Transform3D _GetSubgizmoTransform(EditorNode3DGizmo gizmo, int subgizmoId) [virtual]`
- `bool _HasGizmo(Node3D forNode3d) [virtual]`
- `bool _IsHandleHighlighted(EditorNode3DGizmo gizmo, int handleId, bool secondary) [virtual]`
- `bool _IsSelectableWhenHidden() [virtual]`
- `void _Redraw(EditorNode3DGizmo gizmo) [virtual]`
- `void _SetHandle(EditorNode3DGizmo gizmo, int handleId, bool secondary, Camera3D camera, Vector2 screenPos) [virtual]`
- `void _SetSubgizmoTransform(EditorNode3DGizmo gizmo, int subgizmoId, Transform3D transform) [virtual]`
- `PackedInt32Array _SubgizmosIntersectFrustum(EditorNode3DGizmo gizmo, Camera3D camera, Array[Plane] frustumPlanes) [virtual]`
- `int _SubgizmosIntersectRay(EditorNode3DGizmo gizmo, Camera3D camera, Vector2 screenPos) [virtual]`
- `void AddMaterial(string name, StandardMaterial3D material)`
- `void CreateHandleMaterial(string name, bool billboard = false, Texture2D texture = null)`
- `void CreateIconMaterial(string name, Texture2D texture, bool onTop = false, Color color = Color(1, 1, 1, 1))`
- `void CreateMaterial(string name, Color color, bool billboard = false, bool onTop = false, bool useVertexColor = false)`
- `StandardMaterial3D GetMaterial(string name, EditorNode3DGizmo gizmo = null)`

### EditorNode3DGizmo
*Inherits: **Node3DGizmo < RefCounted < Object***

Gizmo that is used for providing custom visualization and editing (handles and subgizmos) for Node3D objects. Can be overridden to create custom gizmos, but for simple gizmos creating an EditorNode3DGizmoPlugin is usually recommended.

**Methods**
- `void _BeginHandleAction(int id, bool secondary) [virtual]`
- `void _CommitHandle(int id, bool secondary, Variant restore, bool cancel) [virtual]`
- `void _CommitSubgizmos(PackedInt32Array ids, Array[Transform3D] restores, bool cancel) [virtual]`
- `string _GetHandleName(int id, bool secondary) [virtual]`
- `Variant _GetHandleValue(int id, bool secondary) [virtual]`
- `Transform3D _GetSubgizmoTransform(int id) [virtual]`
- `bool _IsHandleHighlighted(int id, bool secondary) [virtual]`
- `void _Redraw() [virtual]`
- `void _SetHandle(int id, bool secondary, Camera3D camera, Vector2 point) [virtual]`
- `void _SetSubgizmoTransform(int id, Transform3D transform) [virtual]`
- `PackedInt32Array _SubgizmosIntersectFrustum(Camera3D camera, Array[Plane] frustum) [virtual]`
- `int _SubgizmosIntersectRay(Camera3D camera, Vector2 point) [virtual]`
- `void AddCollisionSegments(PackedVector3Array segments)`
- `void AddCollisionTriangles(TriangleMesh triangles)`
- `void AddHandles(PackedVector3Array handles, Material material, PackedInt32Array ids, bool billboard = false, bool secondary = false)`
- `void AddLines(PackedVector3Array lines, Material material, bool billboard = false, Color modulate = Color(1, 1, 1, 1))`
- `void AddMesh(Mesh mesh, Material material = null, Transform3D transform = Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0), SkinReference skeleton = null)`
- `void AddUnscaledBillboard(Material material, float defaultScale = 1, Color modulate = Color(1, 1, 1, 1))`
- `void Clear()`
- `Node3D GetNode3d()`
- `EditorNode3DGizmoPlugin GetPlugin()`
- `PackedInt32Array GetSubgizmoSelection()`
- `bool IsSubgizmoSelected(int id)`
- `void SetHidden(bool hidden)`
- `void SetNode3d(Node node)`

### EditorPaths
*Inherits: **Object***

This editor-only singleton returns OS-specific paths to various data folders and files. It can be used in editor plugins to ensure files are saved in the correct location on each operating system.

**Methods**
- `string GetCacheDir()`
- `string GetConfigDir()`
- `string GetDataDir()`
- `string GetProjectSettingsDir()`
- `string GetSelfContainedFile()`
- `bool IsSelfContained()`

### EditorPlugin
*Inherits: **Node < Object** | Inherited by: GridMapEditorPlugin*

Plugins are used by the editor to extend functionality. The most common types of plugins are those which edit a given node or resource type, import plugins and export plugins. See also EditorScript to add functions to the editor.

**Methods**
- `void _ApplyChanges() [virtual]`
- `bool _Build() [virtual]`
- `void _Clear() [virtual]`
- `void _DisablePlugin() [virtual]`
- `void _Edit(Object object) [virtual]`
- `void _EnablePlugin() [virtual]`
- `void _Forward3dDrawOverViewport(Control viewportControl) [virtual]`
- `void _Forward3dForceDrawOverViewport(Control viewportControl) [virtual]`
- `int _Forward3dGuiInput(Camera3D viewportCamera, InputEvent event) [virtual]`
- `void _ForwardCanvasDrawOverViewport(Control viewportControl) [virtual]`
- `void _ForwardCanvasForceDrawOverViewport(Control viewportControl) [virtual]`
- `bool _ForwardCanvasGuiInput(InputEvent event) [virtual]`
- `PackedStringArray _GetBreakpoints() [virtual]`
- `Texture2D _GetPluginIcon() [virtual]`
- `string _GetPluginName() [virtual]`
- `Godot.Collections.Dictionary _GetState() [virtual]`
- `string _GetUnsavedStatus(string forScene) [virtual]`
- `void _GetWindowLayout(ConfigFile configuration) [virtual]`
- `bool _Handles(Object object) [virtual]`
- `bool _HasMainScreen() [virtual]`
- `void _MakeVisible(bool visible) [virtual]`
- `PackedStringArray _RunScene(string scene, PackedStringArray args) [virtual]`
- `void _SaveExternalData() [virtual]`
- `void _SetState(Godot.Collections.Dictionary state) [virtual]`
- `void _SetWindowLayout(ConfigFile configuration) [virtual]`
- `void AddAutoloadSingleton(string name, string path)`
- `void AddContextMenuPlugin(ContextMenuSlot slot, EditorContextMenuPlugin plugin)`
- `Button AddControlToBottomPanel(Control control, string title, Shortcut shortcut = null)`
- `void AddControlToContainer(CustomControlContainer container, Control control)`
- `void AddControlToDock(DockSlot slot, Control control, Shortcut shortcut = null)`
- `void AddCustomType(string type, string base, Script script, Texture2D icon)`
- `void AddDebuggerPlugin(EditorDebuggerPlugin script)`
- `void AddDock(EditorDock dock)`
- `void AddExportPlatform(EditorExportPlatform platform)`
- `void AddExportPlugin(EditorExportPlugin plugin)`
- `void AddImportPlugin(EditorImportPlugin importer, bool firstPriority = false)`
- `void AddInspectorPlugin(EditorInspectorPlugin plugin)`
- `void AddNode3dGizmoPlugin(EditorNode3DGizmoPlugin plugin)`
- `void AddResourceConversionPlugin(EditorResourceConversionPlugin plugin)`
- `void AddSceneFormatImporterPlugin(EditorSceneFormatImporter sceneFormatImporter, bool firstPriority = false)`

**C# Examples**
```csharp
public override void _Forward3DDrawOverViewport(Control viewportControl)
{
    // Draw a circle at the cursor's position.
    viewportControl.DrawCircle(viewportControl.GetLocalMousePosition(), 64, Colors.White);
}

public override EditorPlugin.AfterGuiInput _Forward3DGuiInput(Camera3D viewportCamera, InputEvent @event)
{
    if (@event is InputEventMouseMotion)
    {
        // Redraw the viewport when the cursor is moved.
        UpdateOverlays();
        return EditorPlugin.AfterGuiInput.Stop;
    }
    return EditorPlugin.AfterGuiInput.Pass;
}
```
```csharp
// Prevents the InputEvent from reaching other Editor classes.
public override EditorPlugin.AfterGuiInput _Forward3DGuiInput(Camera3D camera, InputEvent @event)
{
    return EditorPlugin.AfterGuiInput.Stop;
}
```

### EditorProperty
*Inherits: **Container < Control < CanvasItem < Node < Object***

A custom control for editing properties that can be added to the EditorInspector. It is added via EditorInspectorPlugin.

**Properties**
- `bool Checkable` = `false`
- `bool Checked` = `false`
- `bool Deletable` = `false`
- `bool DrawBackground` = `true`
- `bool DrawLabel` = `true`
- `bool DrawWarning` = `false`
- `FocusMode FocusMode` = `3 (overrides Control)`
- `bool Keying` = `false`
- `string Label` = `""`
- `float NameSplitRatio` = `0.5`
- `bool ReadOnly` = `false`
- `bool Selectable` = `true`
- `bool UseFolding` = `false`

**Methods**
- `void _SetReadOnly(bool readOnly) [virtual]`
- `void _UpdateProperty() [virtual]`
- `void AddFocusable(Control control)`
- `void Deselect()`
- `void EmitChanged(StringName property, Variant value, StringName field = &"", bool changing = false)`
- `Object GetEditedObject()`
- `StringName GetEditedProperty()`
- `bool IsSelected()`
- `void Select(int focusable = -1)`
- `void SetBottomEditor(Control editor)`
- `void SetLabelReference(Control control)`
- `void SetObjectAndProperty(Object object, StringName property)`
- `void UpdateProperty()`

### EditorResourceConversionPlugin
*Inherits: **RefCounted < Object***

EditorResourceConversionPlugin is invoked when the context menu is brought up for a resource in the editor inspector. Relevant conversion plugins will appear as menu options to convert the given resource to a target type.

**Methods**
- `Resource _Convert(Resource resource) [virtual]`
- `string _ConvertsTo() [virtual]`
- `bool _Handles(Resource resource) [virtual]`

### EditorResourcePicker
*Inherits: **HBoxContainer < BoxContainer < Container < Control < CanvasItem < Node < Object** | Inherited by: EditorScriptPicker*

This Control node is used in the editor's Inspector dock to allow editing of Resource type properties. It provides options for creating, loading, saving and converting resources. Can be used with EditorInspectorPlugin to recreate the same behavior.

**Properties**
- `string BaseType` = `""`
- `bool Editable` = `true`
- `Resource EditedResource`
- `bool ToggleMode` = `false`

**Methods**
- `bool _HandleMenuSelected(int id) [virtual]`
- `void _SetCreateOptions(Object menuNode) [virtual]`
- `PackedStringArray GetAllowedTypes()`
- `void SetTogglePressed(bool pressed)`

### EditorResourcePreviewGenerator
*Inherits: **RefCounted < Object***

Custom code to generate previews. Check EditorSettings.filesystem/file_dialog/thumbnail_size to find a proper size to generate previews at.

**Methods**
- `bool _CanGenerateSmallPreview() [virtual]`
- `Texture2D _Generate(Resource resource, Vector2i size, Godot.Collections.Dictionary metadata) [virtual]`
- `Texture2D _GenerateFromPath(string path, Vector2i size, Godot.Collections.Dictionary metadata) [virtual]`
- `bool _GenerateSmallPreviewAutomatically() [virtual]`
- `bool _Handles(string type) [virtual]`
- `void RequestDrawAndWait(RID viewport)`

### EditorResourcePreview
*Inherits: **Node < Object***

This node is used to generate previews for resources or files.

**Methods**
- `void AddPreviewGenerator(EditorResourcePreviewGenerator generator)`
- `void CheckForInvalidation(string path)`
- `void QueueEditedResourcePreview(Resource resource, Object receiver, StringName receiverFunc, Variant userdata)`
- `void QueueResourcePreview(string path, Object receiver, StringName receiverFunc, Variant userdata)`
- `void RemovePreviewGenerator(EditorResourcePreviewGenerator generator)`

### EditorResourceTooltipPlugin
*Inherits: **RefCounted < Object***

Resource tooltip plugins are used by FileSystemDock to generate customized tooltips for specific resources. E.g. tooltip for a Texture2D displays a bigger preview and the texture's dimensions.

**Methods**
- `bool _Handles(string type) [virtual]`
- `Control _MakeTooltipForPath(string path, Godot.Collections.Dictionary metadata, Control base) [virtual]`
- `void RequestThumbnail(string path, TextureRect control)`

### EditorSceneFormatImporterBlend
*Inherits: **EditorSceneFormatImporter < RefCounted < Object***

Imports Blender scenes in the .blend file format through the glTF 2.0 3D import pipeline. This importer requires Blender to be installed by the user, so that it can be used to export the scene as glTF 2.0.

### EditorSceneFormatImporterFBX2GLTF
*Inherits: **EditorSceneFormatImporter < RefCounted < Object***

Imports Autodesk FBX 3D scenes by way of converting them to glTF 2.0 using the FBX2glTF command line tool.

### EditorSceneFormatImporterGLTF
*Inherits: **EditorSceneFormatImporter < RefCounted < Object***

There is currently no description for this class. Please help us by contributing one!

### EditorSceneFormatImporterUFBX
*Inherits: **EditorSceneFormatImporter < RefCounted < Object***

EditorSceneFormatImporterUFBX is designed to load FBX files and supports both binary and ASCII FBX files from version 3000 onward. This class supports various 3D object types like meshes, skins, blend shapes, materials, and rigging information. The class aims for feature parity with the official FBX SDK and supports FBX 7.4 specifications.

### EditorSceneFormatImporter
*Inherits: **RefCounted < Object** | Inherited by: EditorSceneFormatImporterBlend, EditorSceneFormatImporterFBX2GLTF, EditorSceneFormatImporterGLTF, EditorSceneFormatImporterUFBX*

EditorSceneFormatImporter allows to define an importer script for a third-party 3D format.

**Methods**
- `PackedStringArray _GetExtensions() [virtual]`
- `void _GetImportOptions(string path) [virtual]`
- `Variant _GetOptionVisibility(string path, bool forAnimation, string option) [virtual]`
- `Object _ImportScene(string path, int flags, Godot.Collections.Dictionary options) [virtual]`
- `void AddImportOption(string name, Variant value)`
- `void AddImportOptionAdvanced(Variant.Type type, string name, Variant defaultValue, PropertyHint hint = 0, string hintString = "", int usageFlags = 6)`

### EditorScenePostImportPlugin
*Inherits: **RefCounted < Object***

This plugin type exists to modify the process of importing scenes, allowing to change the content as well as add importer options at every stage of the process.

**Methods**
- `void _GetImportOptions(string path) [virtual]`
- `void _GetInternalImportOptions(int category) [virtual]`
- `Variant _GetInternalOptionUpdateViewRequired(int category, string option) [virtual]`
- `Variant _GetInternalOptionVisibility(int category, bool forAnimation, string option) [virtual]`
- `Variant _GetOptionVisibility(string path, bool forAnimation, string option) [virtual]`
- `void _InternalProcess(int category, Node baseNode, Node node, Resource resource) [virtual]`
- `void _PostProcess(Node scene) [virtual]`
- `void _PreProcess(Node scene) [virtual]`
- `void AddImportOption(string name, Variant value)`
- `void AddImportOptionAdvanced(Variant.Type type, string name, Variant defaultValue, PropertyHint hint = 0, string hintString = "", int usageFlags = 6)`
- `Variant GetOptionValue(StringName name)`

### EditorScenePostImport
*Inherits: **RefCounted < Object***

Imported scenes can be automatically modified right after import by setting their Custom Script Import property to a tool script that inherits from this class.

**Methods**
- `Object _PostImport(Node scene) [virtual]`
- `string GetSourceFile()`

**C# Examples**
```csharp
using Godot;

// This sample changes all node names.
// Called right after the scene is imported and gets the root node.
[Tool]
public partial class NodeRenamer : EditorScenePostImport
{
    public override GodotObject _PostImport(Node scene)
    {
        // Change all node names to "modified_[oldnodename]"
        Iterate(scene);
        return scene; // Remember to return the imported scene
    }

    public void Iterate(Node node)
    {
        if (node != null)
        {
            node.Name = $"modified_{node.Name}";
            foreach (Node child in node.GetChildren())
            {

// ...
```

### EditorScriptPicker
*Inherits: **EditorResourcePicker < HBoxContainer < BoxContainer < Container < Control < CanvasItem < Node < Object***

Similar to EditorResourcePicker this Control node is used in the editor's Inspector dock, but only to edit the script property of a Node. Default options for creating new resources of all possible subtypes are replaced with dedicated buttons that open the "Attach Node Script" dialog. Can be used with EditorInspectorPlugin to recreate the same behavior.

**Properties**
- `Node ScriptOwner`

### EditorScript
*Inherits: **RefCounted < Object***

Scripts extending this class and implementing its _run() method can be executed from the Script Editor's File > Run menu option (or by pressing Ctrl + Shift + X) while the editor is running. This is useful for adding custom in-editor functionality to Godot. For more complex additions, consider using EditorPlugins instead.

**Methods**
- `void _Run() [virtual]`
- `void AddRootNode(Node node)`
- `EditorInterface GetEditorInterface()`
- `Node GetScene()`

**C# Examples**
```csharp
using Godot;

[Tool]
public partial class HelloEditor : EditorScript
{
    public override void _Run()
    {
        GD.Print("Hello from the Godot Editor!");
    }
}
```

### EditorSelection
*Inherits: **Object***

This object manages the SceneTree selection in the editor.

**Methods**
- `void AddNode(Node node)`
- `void Clear()`
- `Array[Node] GetSelectedNodes()`
- `Array[Node] GetTopSelectedNodes()`
- `Array[Node] GetTransformableSelectedNodes()`
- `void RemoveNode(Node node)`

### EditorSpinSlider
*Inherits: **Range < Control < CanvasItem < Node < Object***

This Control node is used in the editor's Inspector dock to allow editing of numeric values. Can be used with EditorInspectorPlugin to recreate the same behavior.

**Properties**
- `ControlState ControlState` = `0`
- `bool EditingInteger` = `false`
- `bool Flat` = `false`
- `FocusMode FocusMode` = `2 (overrides Control)`
- `bool HideSlider` = `false`
- `string Label` = `""`
- `bool ReadOnly` = `false`
- `BitField[SizeFlags] SizeFlagsVertical` = `1 (overrides Control)`
- `float Step` = `1.0 (overrides Range)`
- `string Suffix` = `""`

### EditorSyntaxHighlighter
*Inherits: **SyntaxHighlighter < Resource < RefCounted < Object** | Inherited by: GDScriptSyntaxHighlighter*

Base class that all SyntaxHighlighters used by the ScriptEditor extend from.

**Methods**
- `EditorSyntaxHighlighter _Create() [virtual]`
- `string _GetName() [virtual]`
- `PackedStringArray _GetSupportedLanguages() [virtual]`

### EditorToaster
*Inherits: **HBoxContainer < BoxContainer < Container < Control < CanvasItem < Node < Object***

This object manages the functionality and display of toast notifications within the editor, ensuring immediate and informative alerts are presented to the user.

**Methods**
- `void PushToast(string message, Severity severity = 0, string tooltip = "")`

### EditorTranslationParserPlugin
*Inherits: **RefCounted < Object***

EditorTranslationParserPlugin is invoked when a file is being parsed to extract strings that require translation. To define the parsing and string extraction logic, override the _parse_file() method in script.

**Methods**
- `PackedStringArray _GetRecognizedExtensions() [virtual]`
- `Array[PackedStringArray] _ParseFile(string path) [virtual]`

**C# Examples**
```csharp
using Godot;

[Tool]
public partial class CustomParser : EditorTranslationParserPlugin
{
    public override Godot.Collections.Array<string[]> _ParseFile(string path)
    {
        Godot.Collections.Array<string[]> ret;
        using var file = FileAccess.Open(path, FileAccess.ModeFlags.Read);
        string text = file.GetAsText();
        string[] splitStrs = text.Split(",", allowEmpty: false);
        foreach (string s in splitStrs)
        {
            ret.Add([s]);
            //GD.Print($"Extracted string: {s}");
        }
        return ret;
    }

    public override string[] _GetReco
// ...
```
```csharp
// This will add a message with msgid "Test 1", msgctxt "context", msgid_plural "test 1 plurals", comment "test 1 comment", and source line "7".
ret.Add(["Test 1", "context", "test 1 plurals", "test 1 comment", "7"]);
// This will add a message with msgid "A test without context" and msgid_plural "plurals".
ret.Add(["A test without context", "", "plurals"]);
// This will add a message with msgid "Only with context" and msgctxt "a friendly context".
ret.Add(["Only with context", "a friendly context"]);
```

### EditorUndoRedoManager
*Inherits: **Object***

EditorUndoRedoManager is a manager for UndoRedo objects associated with edited scenes. Each scene has its own undo history and EditorUndoRedoManager ensures that each action performed in the editor gets associated with a proper scene. For actions not related to scenes (ProjectSettings edits, external resources, etc.), a separate global history is used.

**Methods**
- `void AddDoMethod(Object object, StringName method)`
- `void AddDoProperty(Object object, StringName property, Variant value)`
- `void AddDoReference(Object object)`
- `void AddUndoMethod(Object object, StringName method)`
- `void AddUndoProperty(Object object, StringName property, Variant value)`
- `void AddUndoReference(Object object)`
- `void ClearHistory(int id = -99, bool increaseVersion = true)`
- `void CommitAction(bool execute = true)`
- `void CreateAction(string name, MergeMode mergeMode = 0, Object customContext = null, bool backwardUndoOps = false, bool markUnsaved = true)`
- `void ForceFixedHistory()`
- `UndoRedo GetHistoryUndoRedo(int id)`
- `int GetObjectHistoryId(Object object)`
- `bool IsCommittingAction()`

### EditorVCSInterface
*Inherits: **Object***

Defines the API that the editor uses to extract information from the underlying VCS. The implementation of this API is included in VCS plugins, which are GDExtension plugins that inherit EditorVCSInterface and are attached (on demand) to the singleton instance of EditorVCSInterface. Instead of performing the task themselves, all the virtual functions listed below are calling the internally overridden functions in the VCS plugins to provide a plug-n-play experience. A custom VCS plugin is supposed to inherit from EditorVCSInterface and override each of these virtual functions.

**Methods**
- `bool _CheckoutBranch(string branchName) [virtual]`
- `void _Commit(string msg) [virtual]`
- `void _CreateBranch(string branchName) [virtual]`
- `void _CreateRemote(string remoteName, string remoteUrl) [virtual]`
- `void _DiscardFile(string filePath) [virtual]`
- `void _Fetch(string remote) [virtual]`
- `Array[String] _GetBranchList() [virtual]`
- `string _GetCurrentBranchName() [virtual]`
- `Array[Dictionary] _GetDiff(string identifier, int area) [virtual]`
- `Array[Dictionary] _GetLineDiff(string filePath, string text) [virtual]`
- `Array[Dictionary] _GetModifiedFilesData() [virtual]`
- `Array[Dictionary] _GetPreviousCommits(int maxCommits) [virtual]`
- `Array[String] _GetRemotes() [virtual]`
- `string _GetVcsName() [virtual]`
- `bool _Initialize(string projectPath) [virtual]`
- `void _Pull(string remote) [virtual]`
- `void _Push(string remote, bool force) [virtual]`
- `void _RemoveBranch(string branchName) [virtual]`
- `void _RemoveRemote(string remoteName) [virtual]`
- `void _SetCredentials(string username, string password, string sshPublicKeyPath, string sshPrivateKeyPath, string sshPassphrase) [virtual]`
- `bool _ShutDown() [virtual]`
- `void _StageFile(string filePath) [virtual]`
- `void _UnstageFile(string filePath) [virtual]`
- `Godot.Collections.Dictionary AddDiffHunksIntoDiffFile(Godot.Collections.Dictionary diffFile, Array[Dictionary] diffHunks)`
- `Godot.Collections.Dictionary AddLineDiffsIntoDiffHunk(Godot.Collections.Dictionary diffHunk, Array[Dictionary] lineDiffs)`
- `Godot.Collections.Dictionary CreateCommit(string msg, string author, string id, int unixTimestamp, int offsetMinutes)`
- `Godot.Collections.Dictionary CreateDiffFile(string newFile, string oldFile)`
- `Godot.Collections.Dictionary CreateDiffHunk(int oldStart, int newStart, int oldLines, int newLines)`
- `Godot.Collections.Dictionary CreateDiffLine(int newLineNo, int oldLineNo, string content, string status)`
- `Godot.Collections.Dictionary CreateStatusFile(string filePath, ChangeType changeType, TreeArea area)`
- `void PopupError(string msg)`
