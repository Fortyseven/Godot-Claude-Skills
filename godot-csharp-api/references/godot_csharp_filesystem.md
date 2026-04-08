# Godot 4 C# API Reference — Filesystem

> C#-only reference. 9 classes.

### ConfigFile
*Inherits: **RefCounted < Object***

This helper class can be used to store Variant values on the filesystem using INI-style formatting. The stored values are identified by a section and a key:

**Methods**
- `void Clear()`
- `string EncodeToText()`
- `void EraseSection(string section)`
- `void EraseSectionKey(string section, string key)`
- `PackedStringArray GetSectionKeys(string section)`
- `PackedStringArray GetSections()`
- `Variant GetValue(string section, string key, Variant default = null)`
- `bool HasSection(string section)`
- `bool HasSectionKey(string section, string key)`
- `Error Load(string path)`
- `Error LoadEncrypted(string path, PackedByteArray key)`
- `Error LoadEncryptedPass(string path, string password)`
- `Error Parse(string data)`
- `Error Save(string path)`
- `Error SaveEncrypted(string path, PackedByteArray key)`
- `Error SaveEncryptedPass(string path, string password)`
- `void SetValue(string section, string key, Variant value)`

**C# Examples**
```csharp
// Create new ConfigFile object.
var config = new ConfigFile();

// Store some values.
config.SetValue("Player1", "player_name", "Steve");
config.SetValue("Player1", "best_score", 10);
config.SetValue("Player2", "player_name", "V3geta");
config.SetValue("Player2", "best_score", 9001);

// Save it to a file (overwrite if already exists).
config.Save("user://scores.cfg");
```
```csharp
var score_data = new Godot.Collections.Dictionary();
var config = new ConfigFile();

// Load data from a file.
Error err = config.Load("user://scores.cfg");

// If the file didn't load, ignore it.
if (err != Error.Ok)
{
    return;
}

// Iterate over all sections.
foreach (String player in config.GetSections())
{
    // Fetch the data for each section.
    var player_name = (String)config.GetValue(player, "player_name");
    var player_score = (int)config.GetValue(player, "best_score");
    score_data[player_name] = player_score;
}
```

### DirAccess
*Inherits: **RefCounted < Object***

This class is used to manage directories and their content, even outside of the project folder.

**Properties**
- `bool IncludeHidden`
- `bool IncludeNavigational`

**Methods**
- `Error ChangeDir(string toDir)`
- `Error Copy(string from, string to, int chmodFlags = -1)`
- `Error CopyAbsolute(string from, string to, int chmodFlags = -1) [static]`
- `Error CreateLink(string source, string target)`
- `DirAccess CreateTemp(string prefix = "", bool keep = false) [static]`
- `bool CurrentIsDir()`
- `bool DirExists(string path)`
- `bool DirExistsAbsolute(string path) [static]`
- `bool FileExists(string path)`
- `string GetCurrentDir(bool includeDrive = true)`
- `int GetCurrentDrive()`
- `PackedStringArray GetDirectories()`
- `PackedStringArray GetDirectoriesAt(string path) [static]`
- `int GetDriveCount() [static]`
- `string GetDriveName(int idx) [static]`
- `PackedStringArray GetFiles()`
- `PackedStringArray GetFilesAt(string path) [static]`
- `string GetFilesystemType()`
- `string GetNext()`
- `Error GetOpenError() [static]`
- `int GetSpaceLeft()`
- `bool IsBundle(string path)`
- `bool IsCaseSensitive(string path)`
- `bool IsEquivalent(string pathA, string pathB)`
- `bool IsLink(string path)`
- `Error ListDirBegin()`
- `void ListDirEnd()`
- `Error MakeDir(string path)`
- `Error MakeDirAbsolute(string path) [static]`
- `Error MakeDirRecursive(string path)`
- `Error MakeDirRecursiveAbsolute(string path) [static]`
- `DirAccess Open(string path) [static]`
- `string ReadLink(string path)`
- `Error Remove(string path)`
- `Error RemoveAbsolute(string path) [static]`
- `Error Rename(string from, string to)`
- `Error RenameAbsolute(string from, string to) [static]`

**C# Examples**
```csharp
public void DirContents(string path)
{
    using var dir = DirAccess.Open(path);
    if (dir != null)
    {
        dir.ListDirBegin();
        string fileName = dir.GetNext();
        while (fileName != "")
        {
            if (dir.CurrentIsDir())
            {
                GD.Print($"Found directory: {fileName}");
            }
            else
            {
                GD.Print($"Found file: {fileName}");
            }
            fileName = dir.GetNext();
        }
    }
    else
    {
        GD.Print("An error occurred when trying to access the path.");
    }
}
```

### EditorSettings
*Inherits: **Resource < RefCounted < Object***

Object that holds the project-independent editor settings. These settings are generally visible in the Editor > Editor Settings menu.

**Properties**
- `bool AssetLibrary/useThreads`
- `bool Debugger/autoSwitchToRemoteSceneTree`
- `bool Debugger/autoSwitchToStackTrace`
- `int Debugger/maxNodeSelection`
- `bool Debugger/profileNativeCalls`
- `int Debugger/profilerFrameHistorySize`
- `int Debugger/profilerFrameMaxFunctions`
- `int Debugger/profilerTargetFps`
- `float Debugger/remoteInspectRefreshInterval`
- `float Debugger/remoteSceneTreeRefreshInterval`
- `bool Docks/filesystem/alwaysShowFolders`
- `string Docks/filesystem/otherFileExtensions`
- `string Docks/filesystem/textfileExtensions`
- `int Docks/filesystem/thumbnailSize`
- `float Docks/propertyEditor/autoRefreshInterval`
- `float Docks/propertyEditor/subresourceHueTint`
- `bool Docks/sceneTree/accessibilityWarnings`
- `bool Docks/sceneTree/askBeforeDeletingRelatedAnimationTracks`
- `bool Docks/sceneTree/askBeforeRevokingUniqueName`
- `bool Docks/sceneTree/autoExpandToSelected`
- `bool Docks/sceneTree/centerNodeOnReparent`
- `bool Docks/sceneTree/hideFilteredOutParents`
- `bool Docks/sceneTree/startCreateDialogFullyExpanded`
- `float Editors/2d/autoResampleDelay`
- `Color Editors/2d/boneColor1`
- `Color Editors/2d/boneColor2`
- `Color Editors/2d/boneIkColor`
- `Color Editors/2d/boneOutlineColor`
- `float Editors/2d/boneOutlineSize`
- `Color Editors/2d/boneSelectedColor`

**Methods**
- `void AddPropertyInfo(Godot.Collections.Dictionary info)`
- `void AddShortcut(string path, Shortcut shortcut)`
- `bool CheckChangedSettingsInGroup(string settingPrefix)`
- `void Erase(string property)`
- `PackedStringArray GetChangedSettings()`
- `PackedStringArray GetFavorites()`
- `Variant GetProjectMetadata(string section, string key, Variant default = null)`
- `PackedStringArray GetRecentDirs()`
- `Variant GetSetting(string name)`
- `Shortcut GetShortcut(string path)`
- `PackedStringArray GetShortcutList()`
- `bool HasSetting(string name)`
- `bool HasShortcut(string path)`
- `bool IsShortcut(string path, InputEvent event)`
- `void MarkSettingChanged(string setting)`
- `void RemoveShortcut(string path)`
- `void SetBuiltinActionOverride(string name, Array[InputEvent] actionsList)`
- `void SetFavorites(PackedStringArray dirs)`
- `void SetInitialValue(StringName name, Variant value, bool updateCurrent)`
- `void SetProjectMetadata(string section, string key, Variant data)`
- `void SetRecentDirs(PackedStringArray dirs)`
- `void SetSetting(string name, Variant value)`

**C# Examples**
```csharp
EditorSettings settings = EditorInterface.Singleton.GetEditorSettings();
// `settings.set("some/property", value)` also works as this class overrides `_set()` internally.
settings.SetSetting("some/property", Value);
// `settings.get("some/property", value)` also works as this class overrides `_get()` internally.
settings.GetSetting("some/property");
Godot.Collections.Array<Godot.Collections.Dictionary> listOfSettings = settings.GetPropertyList();
```
```csharp
var settings = GetEditorInterface().GetEditorSettings();
settings.Set("category/property_name", 0);

var propertyInfo = new Godot.Collections.Dictionary
{
    { "name", "category/propertyName" },
    { "type", Variant.Type.Int },
    { "hint", PropertyHint.Enum },
    { "hint_string", "one,two,three" },
};

settings.AddPropertyInfo(propertyInfo);
```

### FileAccess
*Inherits: **RefCounted < Object***

This class can be used to permanently store data in the user device's file system and to read from it. This is useful for storing game save data or player configuration files.

**Properties**
- `bool BigEndian`

**Methods**
- `void Close()`
- `FileAccess CreateTemp(ModeFlags modeFlags, string prefix = "", string extension = "", bool keep = false) [static]`
- `bool EofReached()`
- `bool FileExists(string path) [static]`
- `void Flush()`
- `int Get8()`
- `int Get16()`
- `int Get32()`
- `int Get64()`
- `int GetAccessTime(string file) [static]`
- `string GetAsText()`
- `PackedByteArray GetBuffer(int length)`
- `PackedStringArray GetCsvLine(string delim = ", Variant ")`
- `float GetDouble()`
- `Error GetError()`
- `PackedByteArray GetExtendedAttribute(string file, string attributeName) [static]`
- `string GetExtendedAttributeString(string file, string attributeName) [static]`
- `PackedStringArray GetExtendedAttributesList(string file) [static]`
- `PackedByteArray GetFileAsBytes(string path) [static]`
- `string GetFileAsString(string path) [static]`
- `float GetFloat()`
- `float GetHalf()`
- `bool GetHiddenAttribute(string file) [static]`
- `int GetLength()`
- `string GetLine()`
- `string GetMd5(string path) [static]`
- `int GetModifiedTime(string file) [static]`
- `Error GetOpenError() [static]`
- `string GetPascalString()`
- `string GetPath()`
- `string GetPathAbsolute()`
- `int GetPosition()`
- `bool GetReadOnlyAttribute(string file) [static]`
- `float GetReal()`
- `string GetSha256(string path) [static]`
- `int GetSize(string file) [static]`
- `BitField[UnixPermissionFlags] GetUnixPermissions(string file) [static]`
- `Variant GetVar(bool allowObjects = false)`
- `bool IsOpen()`
- `FileAccess Open(string path, ModeFlags flags) [static]`

**C# Examples**
```csharp
public void SaveToFile(string content)
{
    using var file = FileAccess.Open("user://save_game.dat", FileAccess.ModeFlags.Write);
    file.StoreString(content);
}

public string LoadFromFile()
{
    using var file = FileAccess.Open("user://save_game.dat", FileAccess.ModeFlags.Read);
    string content = file.GetAsText();
    return content;
}
```
```csharp
while (file.GetPosition() < file.GetLength())
{
    // Read data
}
```

### PCKPacker
*Inherits: **RefCounted < Object***

The PCKPacker is used to create packages that can be loaded into a running project using ProjectSettings.load_resource_pack().

**Methods**
- `Error AddFile(string targetPath, string sourcePath, bool encrypt = false)`
- `Error AddFileRemoval(string targetPath)`
- `Error Flush(bool verbose = false)`
- `Error PckStart(string pckPath, int alignment = 32, string key = "0000000000000000000000000000000000000000000000000000000000000000", bool encryptDirectory = false)`

**C# Examples**
```csharp
var packer = new PckPacker();
packer.PckStart("test.pck");
packer.AddFile("res://text.txt", "text.txt");
packer.Flush();
```

### ProjectSettings
*Inherits: **Object***

Stores variables that can be accessed from everywhere. Use get_setting(), set_setting() or has_setting() to access them. Variables stored in project.godot are also loaded into ProjectSettings, making this object very useful for reading custom game configuration options.

**Properties**
- `int Accessibility/general/accessibilitySupport` = `0`
- `int Accessibility/general/updatesPerSecond` = `60`
- `bool Animation/compatibility/defaultParentSkeletonInMeshInstance3d` = `false`
- `bool Animation/warnings/checkAngleInterpolationTypeConflicting` = `true`
- `bool Animation/warnings/checkInvalidTrackPaths` = `true`
- `Color Application/bootSplash/bgColor` = `Color(0.14, 0.14, 0.14, 1)`
- `string Application/bootSplash/image` = `""`
- `int Application/bootSplash/minimumDisplayTime` = `0`
- `bool Application/bootSplash/showImage` = `true`
- `int Application/bootSplash/stretchMode` = `1`
- `bool Application/bootSplash/useFilter` = `true`
- `bool Application/config/autoAcceptQuit` = `true`
- `string Application/config/customUserDirName` = `""`
- `string Application/config/description` = `""`
- `bool Application/config/disableProjectSettingsOverride` = `false`
- `string Application/config/icon` = `""`
- `string Application/config/macosNativeIcon` = `""`
- `string Application/config/name` = `""`
- `Godot.Collections.Dictionary Application/config/nameLocalized` = `{}`
- `string Application/config/projectSettingsOverride` = `""`
- `bool Application/config/quitOnGoBack` = `true`
- `bool Application/config/useCustomUserDir` = `false`
- `bool Application/config/useHiddenProjectDataDirectory` = `true`
- `string Application/config/version` = `""`
- `string Application/config/windowsNativeIcon` = `""`
- `bool Application/run/deltaSmoothing` = `true`
- `bool Application/run/disableStderr` = `false`
- `bool Application/run/disableStdout` = `false`
- `bool Application/run/enableAltSpaceMenu` = `false`
- `bool Application/run/flushStdoutOnPrint` = `false`

**Methods**
- `void AddPropertyInfo(Godot.Collections.Dictionary hint)`
- `bool CheckChangedSettingsInGroup(string settingPrefix)`
- `void Clear(string name)`
- `PackedStringArray GetChangedSettings()`
- `Array[Dictionary] GetGlobalClassList()`
- `int GetOrder(string name)`
- `Variant GetSetting(string name, Variant defaultValue = null)`
- `Variant GetSettingWithOverride(StringName name)`
- `Variant GetSettingWithOverrideAndCustomFeatures(StringName name, PackedStringArray features)`
- `string GlobalizePath(string path)`
- `bool HasSetting(string name)`
- `bool LoadResourcePack(string pack, bool replaceFiles = true, int offset = 0)`
- `string LocalizePath(string path)`
- `Error Save()`
- `Error SaveCustom(string file)`
- `void SetAsBasic(string name, bool basic)`
- `void SetAsInternal(string name, bool internal)`
- `void SetInitialValue(string name, Variant value)`
- `void SetOrder(string name, int position)`
- `void SetRestartIfChanged(string name, bool restart)`
- `void SetSetting(string name, Variant value)`

**C# Examples**
```csharp
// Set the default gravity strength to 980.
PhysicsServer2D.AreaSetParam(GetViewport().FindWorld2D().Space, PhysicsServer2D.AreaParameter.Gravity, 980);
```
```csharp
// Set the default gravity direction to `Vector2(0, 1)`.
PhysicsServer2D.AreaSetParam(GetViewport().FindWorld2D().Space, PhysicsServer2D.AreaParameter.GravityVector, Vector2.Down)
```

### XMLParser
*Inherits: **RefCounted < Object***

Provides a low-level interface for creating parsers for XML files. This class can serve as base to make custom XML parsers.

**Methods**
- `int GetAttributeCount()`
- `string GetAttributeName(int idx)`
- `string GetAttributeValue(int idx)`
- `int GetCurrentLine()`
- `string GetNamedAttributeValue(string name)`
- `string GetNamedAttributeValueSafe(string name)`
- `string GetNodeData()`
- `string GetNodeName()`
- `int GetNodeOffset()`
- `NodeType GetNodeType()`
- `bool HasAttribute(string name)`
- `bool IsEmpty()`
- `Error Open(string file)`
- `Error OpenBuffer(PackedByteArray buffer)`
- `Error Read()`
- `Error Seek(int position)`
- `void SkipSection()`

**C# Examples**
```csharp
var parser = new XmlParser();
parser.Open("path/to/file.svg");
while (parser.Read() != Error.FileEof)
{
    if (parser.GetNodeType() == XmlParser.NodeType.Element)
    {
        var nodeName = parser.GetNodeName();
        var attributesDict = new Godot.Collections.Dictionary();
        for (int idx = 0; idx < parser.GetAttributeCount(); idx++)
        {
            attributesDict[parser.GetAttributeName(idx)] = parser.GetAttributeValue(idx);
        }
        GD.Print($"The {nodeName} element has the following attributes: {attributesDict}");
    }
}
```

### ZIPPacker
*Inherits: **RefCounted < Object***

This class implements a writer that allows storing the multiple blobs in a ZIP archive. See also ZIPReader and PCKPacker.

**Properties**
- `int CompressionLevel` = `-1`

**Methods**
- `Error Close()`
- `Error CloseFile()`
- `Error Open(string path, ZipAppend append = 0)`
- `Error StartFile(string path)`
- `Error WriteFile(PackedByteArray data)`

### ZIPReader
*Inherits: **RefCounted < Object***

This class implements a reader that can extract the content of individual files inside a ZIP archive. See also ZIPPacker.

**Methods**
- `Error Close()`
- `bool FileExists(string path, bool caseSensitive = true)`
- `int GetCompressionLevel(string path, bool caseSensitive = true)`
- `PackedStringArray GetFiles()`
- `Error Open(string path)`
- `PackedByteArray ReadFile(string path, bool caseSensitive = true)`
