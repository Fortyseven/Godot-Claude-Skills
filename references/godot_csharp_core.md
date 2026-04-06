# Godot 4 C# API Reference — Core

> C#-only reference. 39 classes.

### ClassDB
*Inherits: **Object***

Provides access to metadata stored for every available engine class.

**Methods**
- `bool CanInstantiate(StringName class)`
- `Variant ClassCallStatic(StringName class, StringName method)`
- `bool ClassExists(StringName class)`
- `APIType ClassGetApiType(StringName class)`
- `PackedStringArray ClassGetEnumConstants(StringName class, StringName enum, bool noInheritance = false)`
- `PackedStringArray ClassGetEnumList(StringName class, bool noInheritance = false)`
- `int ClassGetIntegerConstant(StringName class, StringName name)`
- `StringName ClassGetIntegerConstantEnum(StringName class, StringName name, bool noInheritance = false)`
- `PackedStringArray ClassGetIntegerConstantList(StringName class, bool noInheritance = false)`
- `int ClassGetMethodArgumentCount(StringName class, StringName method, bool noInheritance = false)`
- `Array[Dictionary] ClassGetMethodList(StringName class, bool noInheritance = false)`
- `Variant ClassGetProperty(Object object, StringName property)`
- `Variant ClassGetPropertyDefaultValue(StringName class, StringName property)`
- `StringName ClassGetPropertyGetter(StringName class, StringName property)`
- `Array[Dictionary] ClassGetPropertyList(StringName class, bool noInheritance = false)`
- `StringName ClassGetPropertySetter(StringName class, StringName property)`
- `Godot.Collections.Dictionary ClassGetSignal(StringName class, StringName signal)`
- `Array[Dictionary] ClassGetSignalList(StringName class, bool noInheritance = false)`
- `bool ClassHasEnum(StringName class, StringName name, bool noInheritance = false)`
- `bool ClassHasIntegerConstant(StringName class, StringName name)`
- `bool ClassHasMethod(StringName class, StringName method, bool noInheritance = false)`
- `bool ClassHasSignal(StringName class, StringName signal)`
- `Error ClassSetProperty(Object object, StringName property, Variant value)`
- `PackedStringArray GetClassList()`
- `PackedStringArray GetInheritersFromClass(StringName class)`
- `StringName GetParentClass(StringName class)`
- `Variant Instantiate(StringName class)`
- `bool IsClassEnabled(StringName class)`
- `bool IsClassEnumBitfield(StringName class, StringName enum, bool noInheritance = false)`
- `bool IsParentClass(StringName class, StringName inherits)`

### EngineDebugger
*Inherits: **Object***

EngineDebugger handles the communication between the editor and the running game. It is active in the running game. Messages can be sent/received through it. It also manages the profilers.

**Methods**
- `void ClearBreakpoints()`
- `void Debug(bool canContinue = true, bool isErrorBreakpoint = false)`
- `int GetDepth()`
- `int GetLinesLeft()`
- `bool HasCapture(StringName name)`
- `bool HasProfiler(StringName name)`
- `void InsertBreakpoint(int line, StringName source)`
- `bool IsActive()`
- `bool IsBreakpoint(int line, StringName source)`
- `bool IsProfiling(StringName name)`
- `bool IsSkippingBreakpoints()`
- `void LinePoll()`
- `void ProfilerAddFrameData(StringName name, Godot.Collections.Array data)`
- `void ProfilerEnable(StringName name, bool enable, Godot.Collections.Array arguments = [])`
- `void RegisterMessageCapture(StringName name, Callable callable)`
- `void RegisterProfiler(StringName name, EngineProfiler profiler)`
- `void RemoveBreakpoint(int line, StringName source)`
- `void ScriptDebug(ScriptLanguage language, bool canContinue = true, bool isErrorBreakpoint = false)`
- `void SendMessage(string message, Godot.Collections.Array data)`
- `void SetDepth(int depth)`
- `void SetLinesLeft(int lines)`
- `void UnregisterMessageCapture(StringName name)`
- `void UnregisterProfiler(StringName name)`

### EngineProfiler
*Inherits: **RefCounted < Object***

This class can be used to implement custom profilers that are able to interact with the engine and editor debugger.

**Methods**
- `void _AddFrame(Godot.Collections.Array data) [virtual]`
- `void _Tick(float frameTime, float processTime, float physicsTime, float physicsFrameTime) [virtual]`
- `void _Toggle(bool enable, Godot.Collections.Array options) [virtual]`

### Engine
*Inherits: **Object***

The Engine singleton allows you to query and modify the project's run-time parameters, such as frames per second, time scale, and others. It also stores information about the current build of Godot, such as the current version.

**Properties**
- `int MaxFps` = `0`
- `int MaxPhysicsStepsPerFrame` = `8`
- `float PhysicsJitterFix` = `0.5`
- `int PhysicsTicksPerSecond` = `60`
- `bool PrintErrorMessages` = `true`
- `bool PrintToStdout` = `true`
- `float TimeScale` = `1.0`

**Methods**
- `Array[ScriptBacktrace] CaptureScriptBacktraces(bool includeVariables = false)`
- `string GetArchitectureName()`
- `Godot.Collections.Dictionary GetAuthorInfo()`
- `Array[Dictionary] GetCopyrightInfo()`
- `Godot.Collections.Dictionary GetDonorInfo()`
- `int GetFramesDrawn()`
- `float GetFramesPerSecond()`
- `Godot.Collections.Dictionary GetLicenseInfo()`
- `string GetLicenseText()`
- `MainLoop GetMainLoop()`
- `int GetPhysicsFrames()`
- `float GetPhysicsInterpolationFraction()`
- `int GetProcessFrames()`
- `ScriptLanguage GetScriptLanguage(int index)`
- `int GetScriptLanguageCount()`
- `Object GetSingleton(StringName name)`
- `PackedStringArray GetSingletonList()`
- `Godot.Collections.Dictionary GetVersionInfo()`
- `string GetWriteMoviePath()`
- `bool HasSingleton(StringName name)`
- `bool IsEditorHint()`
- `bool IsEmbeddedInEditor()`
- `bool IsInPhysicsFrame()`
- `Error RegisterScriptLanguage(ScriptLanguage language)`
- `void RegisterSingleton(StringName name, Object instance)`
- `Error UnregisterScriptLanguage(ScriptLanguage language)`
- `void UnregisterSingleton(StringName name)`

**C# Examples**
```csharp
public override void _PhysicsProcess(double delta)
{
    base._PhysicsProcess(delta);

    if (Engine.GetPhysicsFrames() % 2 == 0)
    {
        // Run expensive logic only once every 2 physics frames here.
    }
}
```
```csharp
public override void _Process(double delta)
{
    base._Process(delta);

    if (Engine.GetProcessFrames() % 5 == 0)
    {
        // Run expensive logic only once every 5 process (render) frames here.
    }
}
```

### MainLoop
*Inherits: **Object** | Inherited by: SceneTree*

MainLoop is the abstract base class for a Godot project's game loop. It is inherited by SceneTree, which is the default game loop implementation used in Godot projects, though it is also possible to write and use one's own MainLoop subclass instead of the scene tree.

**Methods**
- `void _Finalize() [virtual]`
- `void _Initialize() [virtual]`
- `bool _PhysicsProcess(float delta) [virtual]`
- `bool _Process(float delta) [virtual]`

**C# Examples**
```csharp
using Godot;

[GlobalClass]
public partial class CustomMainLoop : MainLoop
{
    private double _timeElapsed = 0;

    public override void _Initialize()
    {
        GD.Print("Initialized:");
        GD.Print($"  Starting Time: {_timeElapsed}");
    }

    public override bool _Process(double delta)
    {
        _timeElapsed += delta;
        // Return true to end the main loop.
        return Input.GetMouseButtonMask() != 0 || Input.IsKeyPressed(Key.Escape);
    }

    private void _Finalize()
    {
        GD.Print("Finalized:");
        GD.Print($"  End Time: {_timeElapsed}");
    }
}
```

### Marshalls
*Inherits: **Object***

Provides data transformation and encoding utility functions.

**Methods**
- `PackedByteArray Base64ToRaw(string base64Str)`
- `string Base64ToUtf8(string base64Str)`
- `Variant Base64ToVariant(string base64Str, bool allowObjects = false)`
- `string RawToBase64(PackedByteArray array)`
- `string Utf8ToBase64(string utf8Str)`
- `string VariantToBase64(Variant variant, bool fullObjects = false)`

### Object
*Inherited by: AudioServer, CameraServer, ClassDB, DisplayServer, EditorFileSystemDirectory, EditorInterface, ...*

An advanced Variant type. All classes in the engine inherit from Object. Each class may define new properties, methods or signals, which are available to all inheriting classes. For example, a Sprite2D instance is able to call Node.add_child() because it inherits from Node.

**Methods**
- `Variant _Get(StringName property) [virtual]`
- `Array[Dictionary] _GetPropertyList() [virtual]`
- `void _Init() [virtual]`
- `Variant _IterGet(Variant iter) [virtual]`
- `bool _IterInit(Godot.Collections.Array iter) [virtual]`
- `bool _IterNext(Godot.Collections.Array iter) [virtual]`
- `void _Notification(int what) [virtual]`
- `bool _PropertyCanRevert(StringName property) [virtual]`
- `Variant _PropertyGetRevert(StringName property) [virtual]`
- `bool _Set(StringName property, Variant value) [virtual]`
- `string _ToString() [virtual]`
- `void _ValidateProperty(Godot.Collections.Dictionary property) [virtual]`
- `void AddUserSignal(string signal, Godot.Collections.Array arguments = [])`
- `Variant Call(StringName method)`
- `Variant CallDeferred(StringName method)`
- `Variant Callv(StringName method, Godot.Collections.Array argArray)`
- `bool CanTranslateMessages()`
- `void CancelFree()`
- `Error Connect(StringName signal, Callable callable, int flags = 0)`
- `void Disconnect(StringName signal, Callable callable)`
- `Error EmitSignal(StringName signal)`
- `void Free()`
- `Variant Get(StringName property)`
- `string GetClass()`
- `Array[Dictionary] GetIncomingConnections()`
- `Variant GetIndexed(NodePath propertyPath)`
- `int GetInstanceId()`
- `Variant GetMeta(StringName name, Variant default = null)`
- `Array[StringName] GetMetaList()`
- `int GetMethodArgumentCount(StringName method)`
- `Array[Dictionary] GetMethodList()`
- `Array[Dictionary] GetPropertyList()`
- `Variant GetScript()`
- `Array[Dictionary] GetSignalConnectionList(StringName signal)`
- `Array[Dictionary] GetSignalList()`
- `StringName GetTranslationDomain()`
- `bool HasConnections(StringName signal)`
- `bool HasMeta(StringName name)`
- `bool HasMethod(StringName method)`
- `bool HasSignal(StringName signal)`

**C# Examples**
```csharp
public override Variant _Get(StringName property)
{
    if (property == "FakeProperty")
    {
        GD.Print("Getting my property!");
        return 4;
    }
    return default;
}

public override Godot.Collections.Array<Godot.Collections.Dictionary> _GetPropertyList()
{
    return
    [
        new Godot.Collections.Dictionary()
        {
            { "name", "FakeProperty" },
            { "type", (int)Variant.Type.Int },
        },
    ];
}
```
```csharp
[Tool]
public partial class MyNode : Node
{
    private int _numberCount;

    [Export]
    public int NumberCount
    {
        get => _numberCount;
        set
        {
            _numberCount = value;
            _numbers.Resize(_numberCount);
            NotifyPropertyListChanged();
        }
    }

    private Godot.Collections.Array<int> _numbers = [];

    public override Godot.Collections.Array<Godot.Collections.Dictionary> _GetPropertyList()
    {
        Godot.Collections.Array<Godot.Collections.Dictionary> properties = [];

        for (int i = 0; i < _numberCount; i++)
        {

// ...
```

### Performance
*Inherits: **Object***

This class provides access to a number of different monitors related to performance, such as memory usage, draw calls, and FPS. These are the same as the values displayed in the Monitor tab in the editor's Debugger panel. By using the get_monitor() method of this class, you can access this data from your code.

**Methods**
- `void AddCustomMonitor(StringName id, Callable callable, Godot.Collections.Array arguments = [], MonitorType type = 0)`
- `Variant GetCustomMonitor(StringName id)`
- `Array[StringName] GetCustomMonitorNames()`
- `PackedInt32Array GetCustomMonitorTypes()`
- `float GetMonitor(Monitor monitor)`
- `int GetMonitorModificationTime()`
- `bool HasCustomMonitor(StringName id)`
- `void RemoveCustomMonitor(StringName id)`

**C# Examples**
```csharp
public override void _Ready()
{
    var monitorValue = new Callable(this, MethodName.GetMonitorValue);

    // Adds monitor with name "MyName" to category "MyCategory".
    Performance.AddCustomMonitor("MyCategory/MyMonitor", monitorValue);
    // Adds monitor with name "MyName" to category "Custom".
    // Note: "MyCategory/MyMonitor" and "MyMonitor" have same name but different ids so the code is valid.
    Performance.AddCustomMonitor("MyMonitor", monitorValue);

    // Adds monitor with name "MyName" to category "Custom".
    // Note: "MyMonitor" and "Custom/MyMonitor" have same name and s
// ...
```
```csharp
GD.Print(Performance.GetMonitor(Performance.Monitor.TimeFps)); // Prints the FPS to the console.
```

### RefCounted
*Inherits: **Object** | Inherited by: AESContext, AStar2D, AStar3D, AStarGrid2D, AudioEffectInstance, AudioSample, ...*

Base class for any object that keeps a reference count. Resource and many other helper objects inherit this class.

**Methods**
- `int GetReferenceCount()`
- `bool InitRef()`
- `bool Reference()`
- `bool Unreference()`

### ResourceFormatLoader
*Inherits: **RefCounted < Object***

Godot loads resources in the editor or in exported games using ResourceFormatLoaders. They are queried automatically via the ResourceLoader singleton, or when a resource with internal dependencies is loaded. Each file type may load as a different resource type, so multiple ResourceFormatLoaders are registered in the engine.

**Methods**
- `bool _Exists(string path) [virtual]`
- `PackedStringArray _GetClassesUsed(string path) [virtual]`
- `PackedStringArray _GetDependencies(string path, bool addTypes) [virtual]`
- `PackedStringArray _GetRecognizedExtensions() [virtual]`
- `string _GetResourceScriptClass(string path) [virtual]`
- `string _GetResourceType(string path) [virtual]`
- `int _GetResourceUid(string path) [virtual]`
- `bool _HandlesType(StringName type) [virtual]`
- `Variant _Load(string path, string originalPath, bool useSubThreads, int cacheMode) [virtual]`
- `bool _RecognizePath(string path, StringName type) [virtual]`
- `Error _RenameDependencies(string path, Godot.Collections.Dictionary renames) [virtual]`

### ResourceFormatSaver
*Inherits: **RefCounted < Object***

The engine can save resources when you do it from the editor, or when you use the ResourceSaver singleton. This is accomplished thanks to multiple ResourceFormatSavers, each handling its own format and called automatically by the engine.

**Methods**
- `PackedStringArray _GetRecognizedExtensions(Resource resource) [virtual]`
- `bool _Recognize(Resource resource) [virtual]`
- `bool _RecognizePath(Resource resource, string path) [virtual]`
- `Error _Save(Resource resource, string path, int flags) [virtual]`
- `Error _SetUid(string path, int uid) [virtual]`

### ResourceImporterBMFont
*Inherits: **ResourceImporter < RefCounted < Object***

The BMFont format is a format created by the BMFont program. Many BMFont-compatible programs also exist, like BMGlyph.

**Properties**
- `bool Compress` = `true`
- `Godot.Collections.Array Fallbacks` = `[]`
- `int ScalingMode` = `2`

### ResourceImporterBitMap
*Inherits: **ResourceImporter < RefCounted < Object***

BitMap resources are typically used as click masks in TextureButton and TouchScreenButton.

**Properties**
- `int CreateFrom` = `0`
- `float Threshold` = `0.5`

### ResourceImporterCSVTranslation
*Inherits: **ResourceImporter < RefCounted < Object***

Comma-separated values are a plain text table storage format. The format's simplicity makes it easy to edit in any text editor or spreadsheet software. This makes it a common choice for game localization.

**Properties**
- `int Compress` = `1`
- `int Delimiter` = `0`
- `bool UnescapeKeys` = `false`
- `bool UnescapeTranslations` = `true`

### ResourceImporterDynamicFont
*Inherits: **ResourceImporter < RefCounted < Object***

Unlike bitmap fonts, dynamic fonts can be resized to any size and still look crisp. Dynamic fonts also optionally support MSDF font rendering, which allows for run-time scale changes with no re-rasterization cost.

**Properties**
- `bool AllowSystemFallback` = `true`
- `int Antialiasing` = `1`
- `bool Compress` = `true`
- `bool DisableEmbeddedBitmaps` = `true`
- `Godot.Collections.Array Fallbacks` = `[]`
- `bool ForceAutohinter` = `false`
- `bool GenerateMipmaps` = `false`
- `int Hinting` = `1`
- `bool KeepRoundingRemainders` = `true`
- `Godot.Collections.Dictionary LanguageSupport` = `{}`
- `bool ModulateColorGlyphs` = `false`
- `int MsdfPixelRange` = `8`
- `int MsdfSize` = `48`
- `bool MultichannelSignedDistanceField` = `false`
- `Godot.Collections.Dictionary OpentypeFeatures` = `{}`
- `float Oversampling` = `0.0`
- `Godot.Collections.Array Preload` = `[]`
- `Godot.Collections.Dictionary ScriptSupport` = `{}`
- `int SubpixelPositioning` = `4`

### ResourceImporterImageFont
*Inherits: **ResourceImporter < RefCounted < Object***

This image-based workflow can be easier to use than ResourceImporterBMFont, but it requires all glyphs to have the same width and height, glyph advances and drawing offsets can be customized. This makes ResourceImporterImageFont most suited to fixed-width fonts.

**Properties**
- `int Ascent` = `0`
- `Rect2i CharacterMargin` = `Rect2i(0, 0, 0, 0)`
- `PackedStringArray CharacterRanges` = `PackedStringArray()`
- `int Columns` = `1`
- `bool Compress` = `true`
- `int Descent` = `0`
- `Godot.Collections.Array Fallbacks` = `[]`
- `Rect2i ImageMargin` = `Rect2i(0, 0, 0, 0)`
- `PackedStringArray KerningPairs` = `PackedStringArray()`
- `int Rows` = `1`
- `int ScalingMode` = `2`

### ResourceImporterImage
*Inherits: **ResourceImporter < RefCounted < Object***

This importer imports Image resources, as opposed to CompressedTexture2D. If you need to render the image in 2D or 3D, use ResourceImporterTexture instead.

### ResourceImporterLayeredTexture
*Inherits: **ResourceImporter < RefCounted < Object***

This imports a 3-dimensional texture, which can then be used in custom shaders, as a FogMaterial density map or as a GPUParticlesAttractorVectorField3D. See also ResourceImporterTexture and ResourceImporterTextureAtlas.

**Properties**
- `int Compress/channelPack` = `0`
- `int Compress/hdrCompression` = `1`
- `bool Compress/highQuality` = `false`
- `float Compress/lossyQuality` = `0.7`
- `int Compress/mode` = `1`
- `float Compress/rdoQualityLoss` = `0.0`
- `int Compress/uastcLevel` = `0`
- `bool Mipmaps/generate` = `true`
- `int Mipmaps/limit` = `-1`
- `int Slices/arrangement` = `1`

### ResourceImporterMP3
*Inherits: **ResourceImporter < RefCounted < Object***

MP3 is a lossy audio format, with worse audio quality compared to ResourceImporterOggVorbis at a given bitrate.

**Properties**
- `int BarBeats` = `4`
- `int BeatCount` = `0`
- `float Bpm` = `0`
- `bool Loop` = `false`
- `float LoopOffset` = `0`

### ResourceImporterOBJ
*Inherits: **ResourceImporter < RefCounted < Object***

Unlike ResourceImporterScene, ResourceImporterOBJ will import a single Mesh resource by default instead of importing a PackedScene. This makes it easier to use the Mesh resource in nodes that expect direct Mesh resources, such as GridMap, GPUParticles3D or CPUParticles3D. Note that it is still possible to save mesh resources from 3D scenes using the Advanced Import Settings dialog, regardless of the source format.

**Properties**
- `bool ForceDisableMeshCompression` = `false`
- `bool GenerateLightmapUv2` = `false`
- `float GenerateLightmapUv2TexelSize` = `0.2`
- `bool GenerateLods` = `true`
- `bool GenerateShadowMesh` = `true`
- `bool GenerateTangents` = `true`
- `Vector3 OffsetMesh` = `Vector3(0, 0, 0)`
- `Vector3 ScaleMesh` = `Vector3(1, 1, 1)`

### ResourceImporterOggVorbis
*Inherits: **ResourceImporter < RefCounted < Object***

Ogg Vorbis is a lossy audio format, with better audio quality compared to ResourceImporterMP3 at a given bitrate.

**Properties**
- `int BarBeats` = `4`
- `int BeatCount` = `0`
- `float Bpm` = `0`
- `bool Loop` = `false`
- `float LoopOffset` = `0`

**Methods**
- `AudioStreamOggVorbis LoadFromBuffer(PackedByteArray streamData) [static]`
- `AudioStreamOggVorbis LoadFromFile(string path) [static]`

### ResourceImporterSVG
*Inherits: **ResourceImporter < RefCounted < Object***

This importer imports DPITexture resources. See also ResourceImporterTexture and ResourceImporterImage.

**Properties**
- `float BaseScale` = `1.0`
- `Godot.Collections.Dictionary ColorMap` = `{}`
- `bool Compress` = `true`
- `float Saturation` = `1.0`

### ResourceImporterScene
*Inherits: **ResourceImporter < RefCounted < Object***

See also ResourceImporterOBJ, which is used for OBJ models that can be imported as an independent Mesh or a scene.

**Properties**
- `Godot.Collections.Dictionary _Subresources` = `{}`
- `float Animation/fps` = `30`
- `bool Animation/import` = `true`
- `bool Animation/importRestAsReset` = `false`
- `bool Animation/removeImmutableTracks` = `true`
- `bool Animation/trimming` = `false`
- `string ImportScript/path` = `""`
- `int Materials/extract` = `0`
- `int Materials/extractFormat` = `0`
- `string Materials/extractPath` = `""`
- `bool Meshes/createShadowMeshes` = `true`
- `bool Meshes/ensureTangents` = `true`
- `bool Meshes/forceDisableCompression` = `false`
- `bool Meshes/generateLods` = `true`
- `int Meshes/lightBaking` = `1`
- `float Meshes/lightmapTexelSize` = `0.2`
- `bool Nodes/applyRootScale` = `true`
- `bool Nodes/importAsSkeletonBones` = `false`
- `string Nodes/rootName` = `""`
- `float Nodes/rootScale` = `1.0`
- `Script Nodes/rootScript` = `null`
- `string Nodes/rootType` = `""`
- `bool Nodes/useNameSuffixes` = `true`
- `bool Nodes/useNodeTypeSuffixes` = `true`
- `bool Skins/useNamedSkins` = `true`

### ResourceImporterShaderFile
*Inherits: **ResourceImporter < RefCounted < Object***

This imports native GLSL shaders as RDShaderFile resources, for use with low-level RenderingDevice operations. This importer does not handle .gdshader files.

### ResourceImporterTextureAtlas
*Inherits: **ResourceImporter < RefCounted < Object***

This imports a collection of textures from a PNG image into an AtlasTexture or 2D ArrayMesh. This can be used to save memory when importing 2D animations from spritesheets. Texture atlases are only supported in 2D rendering, not 3D. See also ResourceImporterTexture and ResourceImporterLayeredTexture.

**Properties**
- `string AtlasFile` = `""`
- `bool CropToRegion` = `false`
- `int ImportMode` = `0`
- `bool TrimAlphaBorderFromRegion` = `true`

### ResourceImporterTexture
*Inherits: **ResourceImporter < RefCounted < Object***

This importer imports CompressedTexture2D resources. If you need to process the image in scripts in a more convenient way, use ResourceImporterImage instead. See also ResourceImporterLayeredTexture.

**Properties**
- `int Compress/channelPack` = `0`
- `int Compress/hdrCompression` = `1`
- `bool Compress/highQuality` = `false`
- `float Compress/lossyQuality` = `0.7`
- `int Compress/mode` = `0`
- `int Compress/normalMap` = `0`
- `float Compress/rdoQualityLoss` = `0.0`
- `int Compress/uastcLevel` = `0`
- `int Detect3d/compressTo` = `1`
- `bool Editor/convertColorsWithEditorTheme` = `false`
- `bool Editor/scaleWithEditorScale` = `false`
- `bool Mipmaps/generate` = `false`
- `int Mipmaps/limit` = `-1`
- `int Process/channelRemap/alpha` = `3`
- `int Process/channelRemap/blue` = `2`
- `int Process/channelRemap/green` = `1`
- `int Process/channelRemap/red` = `0`
- `bool Process/fixAlphaBorder` = `true`
- `bool Process/hdrAsSrgb` = `false`
- `bool Process/hdrClampExposure` = `false`
- `bool Process/normalMapInvertY` = `false`
- `bool Process/premultAlpha` = `false`
- `int Process/sizeLimit` = `0`
- `int Roughness/mode` = `0`
- `string Roughness/srcNormal` = `""`
- `float Svg/scale` = `1.0`

### ResourceImporterWAV
*Inherits: **ResourceImporter < RefCounted < Object***

WAV is an uncompressed format, which can provide higher quality compared to Ogg Vorbis and MP3. It also has the lowest CPU cost to decode. This means high numbers of WAV sounds can be played at the same time, even on low-end devices.

**Properties**
- `int Compress/mode` = `2`
- `int Edit/loopBegin` = `0`
- `int Edit/loopEnd` = `-1`
- `int Edit/loopMode` = `0`
- `bool Edit/normalize` = `false`
- `bool Edit/trim` = `false`
- `bool Force/8Bit` = `false`
- `bool Force/maxRate` = `false`
- `float Force/maxRateHz` = `44100`
- `bool Force/mono` = `false`

### ResourceImporter
*Inherits: **RefCounted < Object** | Inherited by: EditorImportPlugin, ResourceImporterBitMap, ResourceImporterBMFont, ResourceImporterCSVTranslation, ResourceImporterDynamicFont, ResourceImporterImage, ...*

This is the base class for Godot's resource importers. To implement your own resource importers using editor plugins, see EditorImportPlugin.

**Methods**
- `PackedStringArray _GetBuildDependencies(string path) [virtual]`

### ResourceLoader
*Inherits: **Object***

A singleton used to load resource files from the filesystem.

**Methods**
- `void AddResourceFormatLoader(ResourceFormatLoader formatLoader, bool atFront = false)`
- `bool Exists(string path, string typeHint = "")`
- `Resource GetCachedRef(string path)`
- `PackedStringArray GetDependencies(string path)`
- `PackedStringArray GetRecognizedExtensionsForType(string type)`
- `int GetResourceUid(string path)`
- `bool HasCached(string path)`
- `PackedStringArray ListDirectory(string directoryPath)`
- `Resource Load(string path, string typeHint = "", CacheMode cacheMode = 1)`
- `Resource LoadThreadedGet(string path)`
- `ThreadLoadStatus LoadThreadedGetStatus(string path, Godot.Collections.Array progress = [])`
- `Error LoadThreadedRequest(string path, string typeHint = "", bool useSubThreads = false, CacheMode cacheMode = 1)`
- `void RemoveResourceFormatLoader(ResourceFormatLoader formatLoader)`
- `void SetAbortOnMissingResources(bool abort)`

### ResourcePreloader
*Inherits: **Node < Object***

This node is used to preload sub-resources inside a scene, so when the scene is loaded, all the resources are ready to use and can be retrieved from the preloader. You can add the resources using the ResourcePreloader tab when the node is selected.

**Methods**
- `void AddResource(StringName name, Resource resource)`
- `Resource GetResource(StringName name)`
- `PackedStringArray GetResourceList()`
- `bool HasResource(StringName name)`
- `void RemoveResource(StringName name)`
- `void RenameResource(StringName name, StringName newname)`

### ResourceSaver
*Inherits: **Object***

A singleton for saving resource types to the filesystem.

**Methods**
- `void AddResourceFormatSaver(ResourceFormatSaver formatSaver, bool atFront = false)`
- `PackedStringArray GetRecognizedExtensions(Resource type)`
- `int GetResourceIdForPath(string path, bool generate = false)`
- `void RemoveResourceFormatSaver(ResourceFormatSaver formatSaver)`
- `Error Save(Resource resource, string path = "", BitField[SaverFlags] flags = 0)`
- `Error SetUid(string resource, int uid)`

### ResourceUID
*Inherits: **Object***

Resource UIDs (Unique IDentifiers) allow the engine to keep references between resources intact, even if files are renamed or moved. They can be accessed with uid://.

**Methods**
- `void AddId(int id, string path)`
- `int CreateId()`
- `int CreateIdForPath(string path)`
- `string EnsurePath(string pathOrUid) [static]`
- `string GetIdPath(int id)`
- `bool HasId(int id)`
- `string IdToText(int id)`
- `string PathToUid(string path) [static]`
- `void RemoveId(int id)`
- `void SetId(int id, string path)`
- `int TextToId(string textId)`
- `string UidToPath(string uid) [static]`

### Resource
*Inherits: **RefCounted < Object** | Inherited by: Animation, AnimationLibrary, AnimationNode, AnimationNodeStateMachinePlayback, AnimationNodeStateMachineTransition, AudioBusLayout, ...*

Resource is the base class for all Godot-specific resource types, serving primarily as data containers. Since they inherit from RefCounted, resources are reference-counted and freed when no longer in use. They can also be nested within other resources, and saved on disk. PackedScene, one of the most common Objects in a Godot project, is also a resource, uniquely capable of storing and instantiating the Nodes it contains as many times as desired.

**Properties**
- `bool ResourceLocalToScene` = `false`
- `string ResourceName` = `""`
- `string ResourcePath` = `""`
- `string ResourceSceneUniqueId`

**Methods**
- `RID _GetRid() [virtual]`
- `void _ResetState() [virtual]`
- `void _SetPathCache(string path) [virtual]`
- `void _SetupLocalToScene() [virtual]`
- `Resource Duplicate(bool deep = false)`
- `Resource DuplicateDeep(DeepDuplicateMode deepSubresourcesMode = 1)`
- `void EmitChanged()`
- `string GenerateSceneUniqueId() [static]`
- `string GetIdForPath(string path)`
- `Node GetLocalScene()`
- `RID GetRid()`
- `bool IsBuiltIn()`
- `void ResetState()`
- `void SetIdForPath(string path, string id)`
- `void SetPathCache(string path)`
- `void SetupLocalToScene()`
- `void TakeOverPath(string path)`

### SceneTreeTimer
*Inherits: **RefCounted < Object***

A one-shot timer managed by the scene tree, which emits timeout on completion. See also SceneTree.create_timer().

**Properties**
- `float TimeLeft`

**C# Examples**
```csharp
public async Task SomeFunction()
{
    GD.Print("Timer started.");
    await ToSignal(GetTree().CreateTimer(1.0f), SceneTreeTimer.SignalName.Timeout);
    GD.Print("Timer ended.");
}
```

### SceneTree
*Inherits: **MainLoop < Object***

As one of the most important classes, the SceneTree manages the hierarchy of nodes in a scene, as well as scenes themselves. Nodes can be added, fetched and removed. The whole scene tree (and thus the current scene) can be paused. Scenes can be loaded, switched and reloaded.

**Properties**
- `bool AutoAcceptQuit` = `true`
- `Node CurrentScene`
- `bool DebugCollisionsHint` = `false`
- `bool DebugNavigationHint` = `false`
- `bool DebugPathsHint` = `false`
- `Node EditedSceneRoot`
- `bool MultiplayerPoll` = `true`
- `bool Paused` = `false`
- `bool PhysicsInterpolation` = `false`
- `bool QuitOnGoBack` = `true`
- `Window Root`

**Methods**
- `void CallGroup(StringName group, StringName method)`
- `void CallGroupFlags(int flags, StringName group, StringName method)`
- `Error ChangeSceneToFile(string path)`
- `Error ChangeSceneToNode(Node node)`
- `Error ChangeSceneToPacked(PackedScene packedScene)`
- `SceneTreeTimer CreateTimer(float timeSec, bool processAlways = true, bool processInPhysics = false, bool ignoreTimeScale = false)`
- `Tween CreateTween()`
- `Node GetFirstNodeInGroup(StringName group)`
- `int GetFrame()`
- `MultiplayerAPI GetMultiplayer(NodePath forPath = NodePath(""))`
- `int GetNodeCount()`
- `int GetNodeCountInGroup(StringName group)`
- `Array[Node] GetNodesInGroup(StringName group)`
- `Array[Tween] GetProcessedTweens()`
- `bool HasGroup(StringName name)`
- `bool IsAccessibilityEnabled()`
- `bool IsAccessibilitySupported()`
- `void NotifyGroup(StringName group, int notification)`
- `void NotifyGroupFlags(int callFlags, StringName group, int notification)`
- `void QueueDelete(Object obj)`
- `void Quit(int exitCode = 0)`
- `Error ReloadCurrentScene()`
- `void SetGroup(StringName group, string property, Variant value)`
- `void SetGroupFlags(int callFlags, StringName group, string property, Variant value)`
- `void SetMultiplayer(MultiplayerAPI multiplayer, NodePath rootPath = NodePath(""))`
- `void UnloadCurrentScene()`

**C# Examples**
```csharp
public async Task SomeFunction()
{
    GD.Print("start");
    await ToSignal(GetTree().CreateTimer(1.0f), SceneTreeTimer.SignalName.Timeout);
    GD.Print("end");
}
```

### Semaphore
*Inherits: **RefCounted < Object***

A synchronization semaphore that can be used to synchronize multiple Threads. Initialized to zero on creation. For a binary version, see Mutex.

**Methods**
- `void Post(int count = 1)`
- `bool TryWait()`
- `void Wait()`

### Thread
*Inherits: **RefCounted < Object***

A unit of execution in a process. Can run methods on Objects simultaneously. The use of synchronization via Mutex or Semaphore is advised if working with shared objects.

**Methods**
- `string GetId()`
- `bool IsAlive()`
- `bool IsMainThread() [static]`
- `bool IsStarted()`
- `void SetThreadSafetyChecksEnabled(bool enabled) [static]`
- `Error Start(Callable callable, Priority priority = 1)`
- `Variant WaitToFinish()`

### WeakRef
*Inherits: **RefCounted < Object***

A weakref can hold a RefCounted without contributing to the reference counter. A weakref can be created from an Object using @GlobalScope.weakref(). If this object is not a reference, weakref still works, however, it does not have any effect on the object. Weakrefs are useful in cases where multiple classes have variables that refer to each other. Without weakrefs, using these classes could lead to memory leaks, since both references keep each other from being released. Making part of the variables a weakref can prevent this cyclic dependency, and allows the references to be released.

**Methods**
- `Variant GetRef()`

### WorkerThreadPool
*Inherits: **Object***

The WorkerThreadPool singleton allocates a set of Threads (called worker threads) on project startup and provides methods for offloading tasks to them. This can be used for simple multithreading without having to create Threads.

**Methods**
- `int AddGroupTask(Callable action, int elements, int tasksNeeded = -1, bool highPriority = false, string description = "")`
- `int AddTask(Callable action, bool highPriority = false, string description = "")`
- `int GetCallerGroupId()`
- `int GetCallerTaskId()`
- `int GetGroupProcessedElementCount(int groupId)`
- `bool IsGroupTaskCompleted(int groupId)`
- `bool IsTaskCompleted(int taskId)`
- `void WaitForGroupTaskCompletion(int groupId)`
- `Error WaitForTaskCompletion(int taskId)`

**C# Examples**
```csharp
private List<Node> _enemies = new List<Node>(); // A list to be filled with enemies.

private void ProcessEnemyAI(int enemyIndex)
{
    Node processedEnemy = _enemies[enemyIndex];
    // Expensive logic here.
}

public override void _Process(double delta)
{
    long taskId = WorkerThreadPool.AddGroupTask(Callable.From<int>(ProcessEnemyAI), _enemies.Count);
    // Other code...
    WorkerThreadPool.WaitForGroupTaskCompletion(taskId);
    // Other code that depends on the enemy AI already being processed.
}
```
