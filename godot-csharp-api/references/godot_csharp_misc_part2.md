# Godot 4 C# API Reference — Misc (Part 2)

> C#-only reference. 135 classes.

### ProceduralSkyMaterial
*Inherits: **Material < Resource < RefCounted < Object***

ProceduralSkyMaterial provides a way to create an effective background quickly by defining procedural parameters for the sun, the sky and the ground. The sky and ground are defined by a main color, a color at the horizon, and an easing curve to interpolate between them. Suns are described by a position in the sky, a color, and a max angle from the sun at which the easing curve ends. The max angle therefore defines the size of the sun in the sky.

**Properties**
- `float EnergyMultiplier` = `1.0`
- `Color GroundBottomColor` = `Color(0.2, 0.169, 0.133, 1)`
- `float GroundCurve` = `0.02`
- `float GroundEnergyMultiplier` = `1.0`
- `Color GroundHorizonColor` = `Color(0.6463, 0.6558, 0.6708, 1)`
- `Texture2D SkyCover`
- `Color SkyCoverModulate` = `Color(1, 1, 1, 1)`
- `float SkyCurve` = `0.15`
- `float SkyEnergyMultiplier` = `1.0`
- `Color SkyHorizonColor` = `Color(0.6463, 0.6558, 0.6708, 1)`
- `Color SkyTopColor` = `Color(0.385, 0.454, 0.55, 1)`
- `float SunAngleMax` = `30.0`
- `float SunCurve` = `0.15`
- `bool UseDebanding` = `true`

### QuadOccluder3D
*Inherits: **Occluder3D < Resource < RefCounted < Object***

QuadOccluder3D stores a flat plane shape that can be used by the engine's occlusion culling system. See also PolygonOccluder3D if you need to customize the quad's shape.

**Properties**
- `Vector2 Size` = `Vector2(1, 1)`

### RDAttachmentFormat
*Inherits: **RefCounted < Object***

This object is used by RenderingDevice.

**Properties**
- `DataFormat Format` = `36`
- `TextureSamples Samples` = `0`
- `int UsageFlags` = `0`

### RDFramebufferPass
*Inherits: **RefCounted < Object***

This class contains the list of attachment descriptions for a framebuffer pass. Each points with an index to a previously supplied list of texture attachments.

**Properties**
- `PackedInt32Array ColorAttachments` = `PackedInt32Array()`
- `int DepthAttachment` = `-1`
- `PackedInt32Array InputAttachments` = `PackedInt32Array()`
- `PackedInt32Array PreserveAttachments` = `PackedInt32Array()`
- `PackedInt32Array ResolveAttachments` = `PackedInt32Array()`

### RDPipelineColorBlendStateAttachment
*Inherits: **RefCounted < Object***

Controls how blending between source and destination fragments is performed when using RenderingDevice.

**Properties**
- `BlendOperation AlphaBlendOp` = `0`
- `BlendOperation ColorBlendOp` = `0`
- `BlendFactor DstAlphaBlendFactor` = `0`
- `BlendFactor DstColorBlendFactor` = `0`
- `bool EnableBlend` = `false`
- `BlendFactor SrcAlphaBlendFactor` = `0`
- `BlendFactor SrcColorBlendFactor` = `0`
- `bool WriteA` = `true`
- `bool WriteB` = `true`
- `bool WriteG` = `true`
- `bool WriteR` = `true`

**Methods**
- `void SetAsMix()`

### RDPipelineColorBlendState
*Inherits: **RefCounted < Object***

This object is used by RenderingDevice.

**Properties**
- `Array[RDPipelineColorBlendStateAttachment] Attachments` = `[]`
- `Color BlendConstant` = `Color(0, 0, 0, 1)`
- `bool EnableLogicOp` = `false`
- `LogicOperation LogicOp` = `0`

### RDPipelineDepthStencilState
*Inherits: **RefCounted < Object***

RDPipelineDepthStencilState controls the way depth and stencil comparisons are performed when sampling those values using RenderingDevice.

**Properties**
- `CompareOperator BackOpCompare` = `7`
- `int BackOpCompareMask` = `0`
- `StencilOperation BackOpDepthFail` = `1`
- `StencilOperation BackOpFail` = `1`
- `StencilOperation BackOpPass` = `1`
- `int BackOpReference` = `0`
- `int BackOpWriteMask` = `0`
- `CompareOperator DepthCompareOperator` = `7`
- `float DepthRangeMax` = `0.0`
- `float DepthRangeMin` = `0.0`
- `bool EnableDepthRange` = `false`
- `bool EnableDepthTest` = `false`
- `bool EnableDepthWrite` = `false`
- `bool EnableStencil` = `false`
- `CompareOperator FrontOpCompare` = `7`
- `int FrontOpCompareMask` = `0`
- `StencilOperation FrontOpDepthFail` = `1`
- `StencilOperation FrontOpFail` = `1`
- `StencilOperation FrontOpPass` = `1`
- `int FrontOpReference` = `0`
- `int FrontOpWriteMask` = `0`

### RDPipelineMultisampleState
*Inherits: **RefCounted < Object***

RDPipelineMultisampleState is used to control how multisample or supersample antialiasing is being performed when rendering using RenderingDevice.

**Properties**
- `bool EnableAlphaToCoverage` = `false`
- `bool EnableAlphaToOne` = `false`
- `bool EnableSampleShading` = `false`
- `float MinSampleShading` = `0.0`
- `TextureSamples SampleCount` = `0`
- `Array[int] SampleMasks` = `[]`

### RDPipelineRasterizationState
*Inherits: **RefCounted < Object***

This object is used by RenderingDevice.

**Properties**
- `PolygonCullMode CullMode` = `0`
- `float DepthBiasClamp` = `0.0`
- `float DepthBiasConstantFactor` = `0.0`
- `bool DepthBiasEnabled` = `false`
- `float DepthBiasSlopeFactor` = `0.0`
- `bool DiscardPrimitives` = `false`
- `bool EnableDepthClamp` = `false`
- `PolygonFrontFace FrontFace` = `0`
- `float LineWidth` = `1.0`
- `int PatchControlPoints` = `1`
- `bool Wireframe` = `false`

### RDPipelineSpecializationConstant
*Inherits: **RefCounted < Object***

A specialization constant is a way to create additional variants of shaders without actually increasing the number of shader versions that are compiled. This allows improving performance by reducing the number of shader versions and reducing if branching, while still allowing shaders to be flexible for different use cases.

**Properties**
- `int ConstantId` = `0`
- `Variant Value`

### RDSamplerState
*Inherits: **RefCounted < Object***

This object is used by RenderingDevice.

**Properties**
- `float AnisotropyMax` = `1.0`
- `SamplerBorderColor BorderColor` = `2`
- `CompareOperator CompareOp` = `7`
- `bool EnableCompare` = `false`
- `float LodBias` = `0.0`
- `SamplerFilter MagFilter` = `0`
- `float MaxLod` = `1e+20`
- `SamplerFilter MinFilter` = `0`
- `float MinLod` = `0.0`
- `SamplerFilter MipFilter` = `0`
- `SamplerRepeatMode RepeatU` = `2`
- `SamplerRepeatMode RepeatV` = `2`
- `SamplerRepeatMode RepeatW` = `2`
- `bool UnnormalizedUvw` = `false`
- `bool UseAnisotropy` = `false`

### RDShaderSPIRV
*Inherits: **Resource < RefCounted < Object***

RDShaderSPIRV represents an RDShaderFile's SPIR-V code for various shader stages, as well as possible compilation error messages. SPIR-V is a low-level intermediate shader representation. This intermediate representation is not used directly by GPUs for rendering, but it can be compiled into binary shaders that GPUs can understand. Unlike compiled shaders, SPIR-V is portable across GPU models and driver versions.

**Properties**
- `PackedByteArray BytecodeCompute` = `PackedByteArray()`
- `PackedByteArray BytecodeFragment` = `PackedByteArray()`
- `PackedByteArray BytecodeTesselationControl` = `PackedByteArray()`
- `PackedByteArray BytecodeTesselationEvaluation` = `PackedByteArray()`
- `PackedByteArray BytecodeVertex` = `PackedByteArray()`
- `string CompileErrorCompute` = `""`
- `string CompileErrorFragment` = `""`
- `string CompileErrorTesselationControl` = `""`
- `string CompileErrorTesselationEvaluation` = `""`
- `string CompileErrorVertex` = `""`

**Methods**
- `PackedByteArray GetStageBytecode(ShaderStage stage)`
- `string GetStageCompileError(ShaderStage stage)`
- `void SetStageBytecode(ShaderStage stage, PackedByteArray bytecode)`
- `void SetStageCompileError(ShaderStage stage, string compileError)`

### RDShaderSource
*Inherits: **RefCounted < Object***

Shader source code in text form.

**Properties**
- `ShaderLanguage Language` = `0`
- `string SourceCompute` = `""`
- `string SourceFragment` = `""`
- `string SourceTesselationControl` = `""`
- `string SourceTesselationEvaluation` = `""`
- `string SourceVertex` = `""`

**Methods**
- `string GetStageSource(ShaderStage stage)`
- `void SetStageSource(ShaderStage stage, string source)`

### RDTextureFormat
*Inherits: **RefCounted < Object***

This object is used by RenderingDevice.

**Properties**
- `int ArrayLayers` = `1`
- `int Depth` = `1`
- `DataFormat Format` = `8`
- `int Height` = `1`
- `bool IsDiscardable` = `false`
- `bool IsResolveBuffer` = `false`
- `int Mipmaps` = `1`
- `TextureSamples Samples` = `0`
- `TextureType TextureType` = `1`
- `BitField[TextureUsageBits] UsageBits` = `0`
- `int Width` = `1`

**Methods**
- `void AddShareableFormat(DataFormat format)`
- `void RemoveShareableFormat(DataFormat format)`

### RDTextureView
*Inherits: **RefCounted < Object***

This object is used by RenderingDevice.

**Properties**
- `DataFormat FormatOverride` = `232`
- `TextureSwizzle SwizzleA` = `6`
- `TextureSwizzle SwizzleB` = `5`
- `TextureSwizzle SwizzleG` = `4`
- `TextureSwizzle SwizzleR` = `3`

### RDUniform
*Inherits: **RefCounted < Object***

This object is used by RenderingDevice.

**Properties**
- `int Binding` = `0`
- `UniformType UniformType` = `3`

**Methods**
- `void AddId(RID id)`
- `void ClearIds()`
- `Array[RID] GetIds()`

### RDVertexAttribute
*Inherits: **RefCounted < Object***

This object is used by RenderingDevice.

**Properties**
- `int Binding` = `4294967295`
- `DataFormat Format` = `232`
- `VertexFrequency Frequency` = `0`
- `int Location` = `0`
- `int Offset` = `0`
- `int Stride` = `0`

### RID

The RID Variant type is used to access a low-level resource by its unique ID. RIDs are opaque, which means they do not grant access to the resource by themselves. They are used by the low-level server classes, such as DisplayServer, RenderingServer, TextServer, etc.

**Methods**
- `int GetId()`
- `bool IsValid()`

### RandomNumberGenerator
*Inherits: **RefCounted < Object***

RandomNumberGenerator is a class for generating pseudo-random numbers. It currently uses PCG32.

**Properties**
- `int Seed` = `0`
- `int State` = `0`

**Methods**
- `int RandWeighted(PackedFloat32Array weights)`
- `float Randf()`
- `float RandfRange(float from, float to)`
- `float Randfn(float mean = 0.0, float deviation = 1.0)`
- `int Randi()`
- `int RandiRange(int from, int to)`
- `void Randomize()`

### Range
*Inherits: **Control < CanvasItem < Node < Object** | Inherited by: EditorSpinSlider, ProgressBar, ScrollBar, Slider, SpinBox, TextureProgressBar*

Range is an abstract base class for controls that represent a number within a range, using a configured step and page size. See e.g. ScrollBar and Slider for examples of higher-level nodes using Range.

**Properties**
- `bool AllowGreater` = `false`
- `bool AllowLesser` = `false`
- `bool ExpEdit` = `false`
- `float MaxValue` = `100.0`
- `float MinValue` = `0.0`
- `float Page` = `0.0`
- `float Ratio`
- `bool Rounded` = `false`
- `BitField[SizeFlags] SizeFlagsVertical` = `0 (overrides Control)`
- `float Step` = `0.01`
- `float Value` = `0.0`

**Methods**
- `void _ValueChanged(float newValue) [virtual]`
- `void SetValueNoSignal(float value)`
- `void Share(Node with)`
- `void Unshare()`

### Rect2

The Rect2 built-in Variant type represents an axis-aligned rectangle in a 2D space. It is defined by its position and size, which are Vector2. It is frequently used for fast overlap tests (see intersects()). Although Rect2 itself is axis-aligned, it can be combined with Transform2D to represent a rotated or skewed rectangle.

**Properties**
- `Vector2 End` = `Vector2(0, 0)`
- `Vector2 Position` = `Vector2(0, 0)`
- `Vector2 Size` = `Vector2(0, 0)`

**Methods**
- `Rect2 Abs()`
- `bool Encloses(Rect2 b)`
- `Rect2 Expand(Vector2 to)`
- `float GetArea()`
- `Vector2 GetCenter()`
- `Vector2 GetSupport(Vector2 direction)`
- `Rect2 Grow(float amount)`
- `Rect2 GrowIndividual(float left, float top, float right, float bottom)`
- `Rect2 GrowSide(int side, float amount)`
- `bool HasArea()`
- `bool HasPoint(Vector2 point)`
- `Rect2 Intersection(Rect2 b)`
- `bool Intersects(Rect2 b, bool includeBorders = false)`
- `bool IsEqualApprox(Rect2 rect)`
- `bool IsFinite()`
- `Rect2 Merge(Rect2 b)`

**C# Examples**
```csharp
var rect = new Rect2(25, 25, -100, -50);
var absolute = rect.Abs(); // absolute is Rect2(-75, -25, 100, 50)
```
```csharp
var rect = new Rect2(0, 0, 5, 2);

rect = rect.Expand(new Vector2(10, 0)); // rect is Rect2(0, 0, 10, 2)
rect = rect.Expand(new Vector2(-5, 5)); // rect is Rect2(-5, 0, 15, 5)
```

### RectangleShape2D
*Inherits: **Shape2D < Resource < RefCounted < Object***

A 2D rectangle shape, intended for use in physics. Usually used to provide a shape for a CollisionShape2D.

**Properties**
- `Vector2 Size` = `Vector2(20, 20)`

### ReferenceRect
*Inherits: **Control < CanvasItem < Node < Object***

A rectangular box that displays only a colored border around its rectangle (see Control.get_rect()). It can be used to visualize the extents of a Control node, for testing purposes.

**Properties**
- `Color BorderColor` = `Color(1, 0, 0, 1)`
- `float BorderWidth` = `1.0`
- `bool EditorOnly` = `true`

### RegExMatch
*Inherits: **RefCounted < Object***

Contains the results of a single RegEx match returned by RegEx.search() and RegEx.search_all(). It can be used to find the position and range of the match and its capturing groups, and it can extract its substring for you.

**Properties**
- `Godot.Collections.Dictionary Names` = `{}`
- `PackedStringArray Strings` = `PackedStringArray()`
- `string Subject` = `""`

**Methods**
- `int GetEnd(Variant name = 0)`
- `int GetGroupCount()`
- `int GetStart(Variant name = 0)`
- `string GetString(Variant name = 0)`

### RegEx
*Inherits: **RefCounted < Object***

A regular expression (or regex) is a compact language that can be used to recognize strings that follow a specific pattern, such as URLs, email addresses, complete sentences, etc. For example, a regex of ab[0-9] would find any string that is ab followed by any number from 0 to 9. For a more in-depth look, you can easily find various tutorials and detailed explanations on the Internet.

**Methods**
- `void Clear()`
- `Error Compile(string pattern, bool showError = true)`
- `RegEx CreateFromString(string pattern, bool showError = true) [static]`
- `int GetGroupCount()`
- `PackedStringArray GetNames()`
- `string GetPattern()`
- `bool IsValid()`
- `RegExMatch Search(string subject, int offset = 0, int end = -1)`
- `Array[RegExMatch] SearchAll(string subject, int offset = 0, int end = -1)`
- `string Sub(string subject, string replacement, bool all = false, int offset = 0, int end = -1)`

### RenderDataExtension
*Inherits: **RenderData < Object***

This class allows for a RenderData implementation to be made in GDExtension.

**Methods**
- `RID _GetCameraAttributes() [virtual]`
- `RID _GetEnvironment() [virtual]`
- `RenderSceneBuffers _GetRenderSceneBuffers() [virtual]`
- `RenderSceneData _GetRenderSceneData() [virtual]`

### RenderDataRD
*Inherits: **RenderData < Object***

This object manages all render data for the RenderingDevice-based renderers. See also RenderData, RenderSceneData, and RenderSceneDataRD.

### RenderData
*Inherits: **Object** | Inherited by: RenderDataExtension, RenderDataRD*

Abstract render data object, exists for the duration of rendering a single viewport. See also RenderDataRD, RenderSceneData, and RenderSceneDataRD.

**Methods**
- `RID GetCameraAttributes()`
- `RID GetEnvironment()`
- `RenderSceneBuffers GetRenderSceneBuffers()`
- `RenderSceneData GetRenderSceneData()`

### RenderSceneBuffersConfiguration
*Inherits: **RefCounted < Object***

This configuration object is created and populated by the render engine on a viewport change and used to (re)configure a RenderSceneBuffers object.

**Properties**
- `ViewportAnisotropicFiltering AnisotropicFilteringLevel` = `2`
- `float FsrSharpness` = `0.0`
- `Vector2i InternalSize` = `Vector2i(0, 0)`
- `ViewportMSAA Msaa3d` = `0`
- `RID RenderTarget` = `RID()`
- `ViewportScaling3DMode Scaling3dMode` = `255`
- `ViewportScreenSpaceAA ScreenSpaceAa` = `0`
- `Vector2i TargetSize` = `Vector2i(0, 0)`
- `float TextureMipmapBias` = `0.0`
- `int ViewCount` = `1`

### RenderSceneBuffersExtension
*Inherits: **RenderSceneBuffers < RefCounted < Object***

This class allows for a RenderSceneBuffer implementation to be made in GDExtension.

**Methods**
- `void _Configure(RenderSceneBuffersConfiguration config) [virtual]`
- `void _SetAnisotropicFilteringLevel(int anisotropicFilteringLevel) [virtual]`
- `void _SetFsrSharpness(float fsrSharpness) [virtual]`
- `void _SetTextureMipmapBias(float textureMipmapBias) [virtual]`
- `void _SetUseDebanding(bool useDebanding) [virtual]`

### RenderSceneBuffersRD
*Inherits: **RenderSceneBuffers < RefCounted < Object***

This object manages all 3D rendering buffers for the rendering device based renderers. An instance of this object is created for every viewport that has 3D rendering enabled. See also RenderSceneBuffers.

**Methods**
- `void ClearContext(StringName context)`
- `RID CreateTexture(StringName context, StringName name, DataFormat dataFormat, int usageBits, TextureSamples textureSamples, Vector2i size, int layers, int mipmaps, bool unique, bool discardable)`
- `RID CreateTextureFromFormat(StringName context, StringName name, RDTextureFormat format, RDTextureView view, bool unique)`
- `RID CreateTextureView(StringName context, StringName name, StringName viewName, RDTextureView view)`
- `RID GetColorLayer(int layer, bool msaa = false)`
- `RID GetColorTexture(bool msaa = false)`
- `RID GetDepthLayer(int layer, bool msaa = false)`
- `RID GetDepthTexture(bool msaa = false)`
- `float GetFsrSharpness()`
- `Vector2i GetInternalSize()`
- `ViewportMSAA GetMsaa3d()`
- `RID GetRenderTarget()`
- `ViewportScaling3DMode GetScaling3dMode()`
- `ViewportScreenSpaceAA GetScreenSpaceAa()`
- `Vector2i GetTargetSize()`
- `RID GetTexture(StringName context, StringName name)`
- `RDTextureFormat GetTextureFormat(StringName context, StringName name)`
- `TextureSamples GetTextureSamples()`
- `RID GetTextureSlice(StringName context, StringName name, int layer, int mipmap, int layers, int mipmaps)`
- `Vector2i GetTextureSliceSize(StringName context, StringName name, int mipmap)`
- `RID GetTextureSliceView(StringName context, StringName name, int layer, int mipmap, int layers, int mipmaps, RDTextureView view)`
- `bool GetUseDebanding()`
- `bool GetUseTaa()`
- `RID GetVelocityLayer(int layer, bool msaa = false)`
- `RID GetVelocityTexture(bool msaa = false)`
- `int GetViewCount()`
- `bool HasTexture(StringName context, StringName name)`

### RenderSceneBuffers
*Inherits: **RefCounted < Object** | Inherited by: RenderSceneBuffersExtension, RenderSceneBuffersRD*

Abstract scene buffers object, created for each viewport for which 3D rendering is done. It manages any additional buffers used during rendering and will discard buffers when the viewport is resized. See also RenderSceneBuffersRD.

**Methods**
- `void Configure(RenderSceneBuffersConfiguration config)`

### RenderSceneDataExtension
*Inherits: **RenderSceneData < Object***

This class allows for a RenderSceneData implementation to be made in GDExtension.

**Methods**
- `Projection _GetCamProjection() [virtual]`
- `Transform3D _GetCamTransform() [virtual]`
- `RID _GetUniformBuffer() [virtual]`
- `int _GetViewCount() [virtual]`
- `Vector3 _GetViewEyeOffset(int view) [virtual]`
- `Projection _GetViewProjection(int view) [virtual]`

### RenderSceneDataRD
*Inherits: **RenderSceneData < Object***

Object holds scene data related to rendering a single frame of a viewport. See also RenderSceneData, RenderData, and RenderDataRD.

### RenderSceneData
*Inherits: **Object** | Inherited by: RenderSceneDataExtension, RenderSceneDataRD*

Abstract scene data object, exists for the duration of rendering a single viewport. See also RenderSceneDataRD, RenderData, and RenderDataRD.

**Methods**
- `Projection GetCamProjection()`
- `Transform3D GetCamTransform()`
- `RID GetUniformBuffer()`
- `int GetViewCount()`
- `Vector3 GetViewEyeOffset(int view)`
- `Projection GetViewProjection(int view)`

### RetargetModifier3D
*Inherits: **SkeletonModifier3D < Node3D < Node < Object***

Retrieves the pose (or global pose) relative to the parent Skeleton's rest in model space and transfers it to the child Skeleton.

**Properties**
- `BitField[TransformFlag] Enable` = `7`
- `SkeletonProfile Profile`
- `bool UseGlobalPose` = `false`

**Methods**
- `bool IsPositionEnabled()`
- `bool IsRotationEnabled()`
- `bool IsScaleEnabled()`
- `void SetPositionEnabled(bool enabled)`
- `void SetRotationEnabled(bool enabled)`
- `void SetScaleEnabled(bool enabled)`

### RichTextEffect
*Inherits: **Resource < RefCounted < Object***

A custom effect for a RichTextLabel, which can be loaded in the RichTextLabel inspector or using RichTextLabel.install_effect().

**Methods**
- `bool _ProcessCustomFx(CharFXTransform charFx) [virtual]`

**C# Examples**
```csharp
// The RichTextEffect will be usable like this: `[example]Some text[/example]`
string bbcode = "example";
```

### RootMotionView
*Inherits: **VisualInstance3D < Node3D < Node < Object***

Root motion refers to an animation technique where a mesh's skeleton is used to give impulse to a character. When working with 3D animations, a popular technique is for animators to use the root skeleton bone to give motion to the rest of the skeleton. This allows animating characters in a way where steps actually match the floor below. It also allows precise interaction with objects during cinematics. See also AnimationMixer.

**Properties**
- `NodePath AnimationPath` = `NodePath("")`
- `float CellSize` = `1.0`
- `Color Color` = `Color(0.5, 0.5, 1, 1)`
- `float Radius` = `10.0`
- `bool ZeroY` = `true`

### SceneReplicationConfig
*Inherits: **Resource < RefCounted < Object***

Configuration for properties to synchronize with a MultiplayerSynchronizer.

**Methods**
- `void AddProperty(NodePath path, int index = -1)`
- `Array[NodePath] GetProperties()`
- `bool HasProperty(NodePath path)`
- `int PropertyGetIndex(NodePath path)`
- `ReplicationMode PropertyGetReplicationMode(NodePath path)`
- `bool PropertyGetSpawn(NodePath path)`
- `bool PropertyGetSync(NodePath path)`
- `bool PropertyGetWatch(NodePath path)`
- `void PropertySetReplicationMode(NodePath path, ReplicationMode mode)`
- `void PropertySetSpawn(NodePath path, bool enabled)`
- `void PropertySetSync(NodePath path, bool enabled)`
- `void PropertySetWatch(NodePath path, bool enabled)`
- `void RemoveProperty(NodePath path)`

### SegmentShape2D
*Inherits: **Shape2D < Resource < RefCounted < Object***

A 2D line segment shape, intended for use in physics. Usually used to provide a shape for a CollisionShape2D.

**Properties**
- `Vector2 A` = `Vector2(0, 0)`
- `Vector2 B` = `Vector2(0, 10)`

### SeparationRayShape2D
*Inherits: **Shape2D < Resource < RefCounted < Object***

A 2D ray shape, intended for use in physics. Usually used to provide a shape for a CollisionShape2D. When a SeparationRayShape2D collides with an object, it tries to separate itself from it by moving its endpoint to the collision point. For example, a SeparationRayShape2D next to a character can allow it to instantly move up when touching stairs.

**Properties**
- `float Length` = `20.0`
- `bool SlideOnSlope` = `false`

### SeparationRayShape3D
*Inherits: **Shape3D < Resource < RefCounted < Object***

A 3D ray shape, intended for use in physics. Usually used to provide a shape for a CollisionShape3D. When a SeparationRayShape3D collides with an object, it tries to separate itself from it by moving its endpoint to the collision point. For example, a SeparationRayShape3D next to a character can allow it to instantly move up when touching stairs.

**Properties**
- `float Length` = `1.0`
- `bool SlideOnSlope` = `false`

### Separator
*Inherits: **Control < CanvasItem < Node < Object** | Inherited by: HSeparator, VSeparator*

Abstract base class for separators, used for separating other controls. Separators are purely visual and normally drawn as a StyleBoxLine.

### ShapeCast2D
*Inherits: **Node2D < CanvasItem < Node < Object***

Shape casting allows to detect collision objects by sweeping its shape along the cast direction determined by target_position. This is similar to RayCast2D, but it allows for sweeping a region of space, rather than just a straight line. ShapeCast2D can detect multiple collision objects. It is useful for things like wide laser beams or snapping a simple shape to a floor.

**Properties**
- `bool CollideWithAreas` = `false`
- `bool CollideWithBodies` = `true`
- `int CollisionMask` = `1`
- `Godot.Collections.Array CollisionResult` = `[]`
- `bool Enabled` = `true`
- `bool ExcludeParent` = `true`
- `float Margin` = `0.0`
- `int MaxResults` = `32`
- `Shape2D Shape`
- `Vector2 TargetPosition` = `Vector2(0, 50)`

**Methods**
- `void AddException(CollisionObject2D node)`
- `void AddExceptionRid(RID rid)`
- `void ClearExceptions()`
- `void ForceShapecastUpdate()`
- `float GetClosestCollisionSafeFraction()`
- `float GetClosestCollisionUnsafeFraction()`
- `Object GetCollider(int index)`
- `RID GetColliderRid(int index)`
- `int GetColliderShape(int index)`
- `int GetCollisionCount()`
- `bool GetCollisionMaskValue(int layerNumber)`
- `Vector2 GetCollisionNormal(int index)`
- `Vector2 GetCollisionPoint(int index)`
- `bool IsColliding()`
- `void RemoveException(CollisionObject2D node)`
- `void RemoveExceptionRid(RID rid)`
- `void SetCollisionMaskValue(int layerNumber, bool value)`

### Shortcut
*Inherits: **Resource < RefCounted < Object***

Shortcuts (also known as hotkeys) are containers of InputEvent resources. They are commonly used to interact with a Control element from an InputEvent.

**Properties**
- `Godot.Collections.Array Events` = `[]`

**Methods**
- `string GetAsText()`
- `bool HasValidEvent()`
- `bool MatchesEvent(InputEvent event)`

**C# Examples**
```csharp
using Godot;

public partial class MyNode : Node
{
    private readonly Shortcut _saveShortcut = new Shortcut();

    public override void _Ready()
    {
        InputEventKey keyEvent = new InputEventKey
        {
            Keycode = Key.S,
            CtrlPressed = true,
            CommandOrControlAutoremap = true, // Swaps Ctrl for Command on Mac.
        };

        _saveShortcut.Events = [keyEvent];
    }

    public override void _Input(InputEvent @event)
    {
        if (@event is InputEventKey keyEvent &&
            _saveShortcut.MatchesEvent(@event) &&
            keyEvent.Presse
// ...
```

### Signal

Signal is a built-in Variant type that represents a signal of an Object instance. Like all Variant types, it can be stored in variables and passed to functions. Signals allow all connected Callables (and by extension their respective objects) to listen and react to events, without directly referencing one another. This keeps the code flexible and easier to manage. You can check whether an Object has a given signal name using Object.has_signal().

**Methods**
- `int Connect(Callable callable, int flags = 0)`
- `void Disconnect(Callable callable)`
- `void Emit()`
- `Godot.Collections.Array GetConnections()`
- `StringName GetName()`
- `Object GetObject()`
- `int GetObjectId()`
- `bool HasConnections()`
- `bool IsConnected(Callable callable)`
- `bool IsNull()`

**C# Examples**
```csharp
[Signal]
delegate void AttackedEventHandler();

// Additional arguments may be declared.
// These arguments must be passed when the signal is emitted.
[Signal]
delegate void ItemDroppedEventHandler(string itemName, int amount);
```
```csharp
public override void _Ready()
{
    var button = new Button();
    // C# supports passing signals as events, so we can use this idiomatic construct:
    button.ButtonDown += OnButtonDown;

    // This assumes that a `Player` class exists, which defines a `Hit` signal.
    var player = new Player();
    // We can use lambdas when we need to bind additional parameters.
    player.Hit += () => OnPlayerHit("sword", 100);
}

private void OnButtonDown()
{
    GD.Print("Button down!");
}

private void OnPlayerHit(string weaponType, int damage)
{
    GD.Print($"Hit with weapon {weaponType} for {damage
// ...
```

### SkeletonProfileHumanoid
*Inherits: **SkeletonProfile < Resource < RefCounted < Object***

A SkeletonProfile as a preset that is optimized for the human form. This exists for standardization, so all parameters are read-only.

**Properties**
- `int BoneSize` = `56 (overrides SkeletonProfile)`
- `int GroupSize` = `4 (overrides SkeletonProfile)`
- `StringName RootBone` = `&"Root" (overrides SkeletonProfile)`
- `StringName ScaleBaseBone` = `&"Hips" (overrides SkeletonProfile)`

### SkeletonProfile
*Inherits: **Resource < RefCounted < Object** | Inherited by: SkeletonProfileHumanoid*

This resource is used in EditorScenePostImport. Some parameters are referring to bones in Skeleton3D, Skin, Animation, and some other nodes are rewritten based on the parameters of SkeletonProfile.

**Properties**
- `int BoneSize` = `0`
- `int GroupSize` = `0`
- `StringName RootBone` = `&""`
- `StringName ScaleBaseBone` = `&""`

**Methods**
- `int FindBone(StringName boneName)`
- `StringName GetBoneName(int boneIdx)`
- `StringName GetBoneParent(int boneIdx)`
- `StringName GetBoneTail(int boneIdx)`
- `StringName GetGroup(int boneIdx)`
- `StringName GetGroupName(int groupIdx)`
- `Vector2 GetHandleOffset(int boneIdx)`
- `Transform3D GetReferencePose(int boneIdx)`
- `TailDirection GetTailDirection(int boneIdx)`
- `Texture2D GetTexture(int groupIdx)`
- `bool IsRequired(int boneIdx)`
- `void SetBoneName(int boneIdx, StringName boneName)`
- `void SetBoneParent(int boneIdx, StringName boneParent)`
- `void SetBoneTail(int boneIdx, StringName boneTail)`
- `void SetGroup(int boneIdx, StringName group)`
- `void SetGroupName(int groupIdx, StringName groupName)`
- `void SetHandleOffset(int boneIdx, Vector2 handleOffset)`
- `void SetReferencePose(int boneIdx, Transform3D boneName)`
- `void SetRequired(int boneIdx, bool required)`
- `void SetTailDirection(int boneIdx, TailDirection tailDirection)`
- `void SetTexture(int groupIdx, Texture2D texture)`

### SkinReference
*Inherits: **RefCounted < Object***

An internal object containing a mapping from a Skin used within the context of a particular MeshInstance3D to refer to the skeleton's RID in the RenderingServer.

**Methods**
- `RID GetSkeleton()`
- `Skin GetSkin()`

### Skin
*Inherits: **Resource < RefCounted < Object***

There is currently no description for this class. Please help us by contributing one!

**Methods**
- `void AddBind(int bone, Transform3D pose)`
- `void AddNamedBind(string name, Transform3D pose)`
- `void ClearBinds()`
- `int GetBindBone(int bindIndex)`
- `int GetBindCount()`
- `StringName GetBindName(int bindIndex)`
- `Transform3D GetBindPose(int bindIndex)`
- `void SetBindBone(int bindIndex, int bone)`
- `void SetBindCount(int bindCount)`
- `void SetBindName(int bindIndex, StringName name)`
- `void SetBindPose(int bindIndex, Transform3D pose)`

### Sky
*Inherits: **Resource < RefCounted < Object***

The Sky class uses a Material to render a 3D environment's background and the light it emits by updating the reflection/radiance cubemaps.

**Properties**
- `ProcessMode ProcessMode` = `0`
- `RadianceSize RadianceSize` = `3`
- `Material SkyMaterial`

### SocketServer
*Inherits: **RefCounted < Object** | Inherited by: TCPServer, UDSServer*

A socket server.

**Methods**
- `bool IsConnectionAvailable()`
- `bool IsListening()`
- `void Stop()`
- `StreamPeerSocket TakeSocketConnection()`

### SphereOccluder3D
*Inherits: **Occluder3D < Resource < RefCounted < Object***

SphereOccluder3D stores a sphere shape that can be used by the engine's occlusion culling system.

**Properties**
- `float Radius` = `1.0`

### SphereShape3D
*Inherits: **Shape3D < Resource < RefCounted < Object***

A 3D sphere shape, intended for use in physics. Usually used to provide a shape for a CollisionShape3D.

**Properties**
- `float Radius` = `0.5`

### SplineIK3D
*Inherits: **ChainIK3D < IKModifier3D < SkeletonModifier3D < Node3D < Node < Object***

A SkeletonModifier3D for aligning bones along a Path3D. The smoothness of the fitting depends on the Curve3D.bake_interval.

**Properties**
- `int SettingCount` = `0`

**Methods**
- `NodePath GetPath3d(int index)`
- `int GetTiltFadeIn(int index)`
- `int GetTiltFadeOut(int index)`
- `bool IsTiltEnabled(int index)`
- `void SetPath3d(int index, NodePath path3d)`
- `void SetTiltEnabled(int index, bool enabled)`
- `void SetTiltFadeIn(int index, int size)`
- `void SetTiltFadeOut(int index, int size)`

### SpringBoneCollision3D
*Inherits: **Node3D < Node < Object** | Inherited by: SpringBoneCollisionCapsule3D, SpringBoneCollisionPlane3D, SpringBoneCollisionSphere3D*

A collision can be a child of SpringBoneSimulator3D. If it is not a child of SpringBoneSimulator3D, it has no effect.

**Properties**
- `int Bone` = `-1`
- `string BoneName` = `""`
- `Vector3 PositionOffset`
- `Quaternion RotationOffset`

**Methods**
- `Skeleton3D GetSkeleton()`

### SpringBoneCollisionCapsule3D
*Inherits: **SpringBoneCollision3D < Node3D < Node < Object***

A capsule shape collision that interacts with SpringBoneSimulator3D.

**Properties**
- `float Height` = `0.5`
- `bool Inside` = `false`
- `float MidHeight`
- `float Radius` = `0.1`

### SpringBoneCollisionPlane3D
*Inherits: **SpringBoneCollision3D < Node3D < Node < Object***

An infinite plane collision that interacts with SpringBoneSimulator3D. It is an infinite size XZ plane, and the +Y direction is treated as normal.

### SpringBoneCollisionSphere3D
*Inherits: **SpringBoneCollision3D < Node3D < Node < Object***

A sphere shape collision that interacts with SpringBoneSimulator3D.

**Properties**
- `bool Inside` = `false`
- `float Radius` = `0.1`

### SpringBoneSimulator3D
*Inherits: **SkeletonModifier3D < Node3D < Node < Object***

This SkeletonModifier3D can be used to wiggle hair, cloth, and tails. This modifier behaves differently from PhysicalBoneSimulator3D as it attempts to return the original pose after modification.

**Properties**
- `Vector3 ExternalForce` = `Vector3(0, 0, 0)`
- `bool MutableBoneAxes` = `true`
- `int SettingCount` = `0`

**Methods**
- `bool AreAllChildCollisionsEnabled(int index)`
- `void ClearCollisions(int index)`
- `void ClearExcludeCollisions(int index)`
- `void ClearSettings()`
- `int GetCenterBone(int index)`
- `string GetCenterBoneName(int index)`
- `CenterFrom GetCenterFrom(int index)`
- `NodePath GetCenterNode(int index)`
- `int GetCollisionCount(int index)`
- `NodePath GetCollisionPath(int index, int collision)`
- `float GetDrag(int index)`
- `Curve GetDragDampingCurve(int index)`
- `int GetEndBone(int index)`
- `BoneDirection GetEndBoneDirection(int index)`
- `float GetEndBoneLength(int index)`
- `string GetEndBoneName(int index)`
- `int GetExcludeCollisionCount(int index)`
- `NodePath GetExcludeCollisionPath(int index, int collision)`
- `float GetGravity(int index)`
- `Curve GetGravityDampingCurve(int index)`
- `Vector3 GetGravityDirection(int index)`
- `int GetJointBone(int index, int joint)`
- `string GetJointBoneName(int index, int joint)`
- `int GetJointCount(int index)`
- `float GetJointDrag(int index, int joint)`
- `float GetJointGravity(int index, int joint)`
- `Vector3 GetJointGravityDirection(int index, int joint)`
- `float GetJointRadius(int index, int joint)`
- `RotationAxis GetJointRotationAxis(int index, int joint)`
- `Vector3 GetJointRotationAxisVector(int index, int joint)`
- `float GetJointStiffness(int index, int joint)`
- `float GetRadius(int index)`
- `Curve GetRadiusDampingCurve(int index)`
- `int GetRootBone(int index)`
- `string GetRootBoneName(int index)`
- `RotationAxis GetRotationAxis(int index)`
- `Vector3 GetRotationAxisVector(int index)`
- `float GetStiffness(int index)`
- `Curve GetStiffnessDampingCurve(int index)`
- `bool IsConfigIndividual(int index)`

### Sprite3D
*Inherits: **SpriteBase3D < GeometryInstance3D < VisualInstance3D < Node3D < Node < Object***

A node that displays a 2D texture in a 3D environment. The texture displayed can be a region from a larger atlas texture, or a frame from a sprite sheet animation. See also SpriteBase3D where properties such as the billboard mode are defined.

**Properties**
- `int Frame` = `0`
- `Vector2i FrameCoords` = `Vector2i(0, 0)`
- `int Hframes` = `1`
- `bool RegionEnabled` = `false`
- `Rect2 RegionRect` = `Rect2(0, 0, 0, 0)`
- `Texture2D Texture`
- `int Vframes` = `1`

### SpriteBase3D
*Inherits: **GeometryInstance3D < VisualInstance3D < Node3D < Node < Object** | Inherited by: AnimatedSprite3D, Sprite3D*

A node that displays 2D texture information in a 3D environment. See also Sprite3D where many other properties are defined.

**Properties**
- `float AlphaAntialiasingEdge` = `0.0`
- `AlphaAntiAliasing AlphaAntialiasingMode` = `0`
- `AlphaCutMode AlphaCut` = `0`
- `float AlphaHashScale` = `1.0`
- `float AlphaScissorThreshold` = `0.5`
- `Axis Axis` = `2`
- `BillboardMode Billboard` = `0`
- `bool Centered` = `true`
- `bool DoubleSided` = `true`
- `bool FixedSize` = `false`
- `bool FlipH` = `false`
- `bool FlipV` = `false`
- `Color Modulate` = `Color(1, 1, 1, 1)`
- `bool NoDepthTest` = `false`
- `Vector2 Offset` = `Vector2(0, 0)`
- `float PixelSize` = `0.01`
- `int RenderPriority` = `0`
- `bool Shaded` = `false`
- `TextureFilter TextureFilter` = `3`
- `bool Transparent` = `true`

**Methods**
- `TriangleMesh GenerateTriangleMesh()`
- `bool GetDrawFlag(DrawFlags flag)`
- `Rect2 GetItemRect()`
- `void SetDrawFlag(DrawFlags flag, bool enabled)`

### SpriteFrames
*Inherits: **Resource < RefCounted < Object***

Sprite frame library for an AnimatedSprite2D or AnimatedSprite3D node. Contains frames and animation data for playback.

**Methods**
- `void AddAnimation(StringName anim)`
- `void AddFrame(StringName anim, Texture2D texture, float duration = 1.0, int atPosition = -1)`
- `void Clear(StringName anim)`
- `void ClearAll()`
- `void DuplicateAnimation(StringName animFrom, StringName animTo)`
- `bool GetAnimationLoop(StringName anim)`
- `PackedStringArray GetAnimationNames()`
- `float GetAnimationSpeed(StringName anim)`
- `int GetFrameCount(StringName anim)`
- `float GetFrameDuration(StringName anim, int idx)`
- `Texture2D GetFrameTexture(StringName anim, int idx)`
- `bool HasAnimation(StringName anim)`
- `void RemoveAnimation(StringName anim)`
- `void RemoveFrame(StringName anim, int idx)`
- `void RenameAnimation(StringName anim, StringName newname)`
- `void SetAnimationLoop(StringName anim, bool loop)`
- `void SetAnimationSpeed(StringName anim, float fps)`
- `void SetFrame(StringName anim, int idx, Texture2D texture, float duration = 1.0)`

### StatusIndicator
*Inherits: **Node < Object***

Application status indicator (aka notification area icon).

**Properties**
- `Texture2D Icon`
- `NodePath Menu` = `NodePath("")`
- `string Tooltip` = `""`
- `bool Visible` = `true`

**Methods**
- `Rect2 GetRect()`

### StringName

StringNames are immutable strings designed for general-purpose representation of unique names (also called "string interning"). Two StringNames with the same value are the same object. Comparing them is extremely fast compared to regular Strings.

**Methods**
- `bool BeginsWith(string text)`
- `PackedStringArray Bigrams()`
- `int BinToInt()`
- `string CEscape()`
- `string CUnescape()`
- `string Capitalize()`
- `int CasecmpTo(string to)`
- `bool Contains(string what)`
- `bool Containsn(string what)`
- `int Count(string what, int from = 0, int to = 0)`
- `int Countn(string what, int from = 0, int to = 0)`
- `string Dedent()`
- `bool EndsWith(string text)`
- `string Erase(int position, int chars = 1)`
- `int FilecasecmpTo(string to)`
- `int FilenocasecmpTo(string to)`
- `int Find(string what, int from = 0)`
- `int Findn(string what, int from = 0)`
- `string Format(Variant values, string placeholder = "{_}")`
- `string GetBaseDir()`
- `string GetBasename()`
- `string GetExtension()`
- `string GetFile()`
- `string GetSlice(string delimiter, int slice)`
- `int GetSliceCount(string delimiter)`
- `string GetSlicec(int delimiter, int slice)`
- `int Hash()`
- `PackedByteArray HexDecode()`
- `int HexToInt()`
- `string Indent(string prefix)`
- `string Insert(int position, string what)`
- `bool IsAbsolutePath()`
- `bool IsEmpty()`
- `bool IsRelativePath()`
- `bool IsSubsequenceOf(string text)`
- `bool IsSubsequenceOfn(string text)`
- `bool IsValidAsciiIdentifier()`
- `bool IsValidFilename()`
- `bool IsValidFloat()`
- `bool IsValidHexNumber(bool withPrefix = false)`

**C# Examples**
```csharp
GD.Print("101".BinToInt());   // Prints 5
GD.Print("0b101".BinToInt()); // Prints 5
GD.Print("-0b10".BinToInt()); // Prints -2
```
```csharp
"move_local_x".Capitalize();   // Returns "Move Local X"
"sceneFile_path".Capitalize(); // Returns "Scene File Path"
"2D, FPS, PNG".Capitalize();   // Returns "2d, Fps, Png"
```

### String

This is the built-in string Variant type (and the one used by GDScript). Strings may contain any number of Unicode characters, and expose methods useful for manipulating and generating strings. Strings are reference-counted and use a copy-on-write approach (every modification to a string returns a new String), so passing them around is cheap in resources.

**Methods**
- `bool BeginsWith(string text)`
- `PackedStringArray Bigrams()`
- `int BinToInt()`
- `string CEscape()`
- `string CUnescape()`
- `string Capitalize()`
- `int CasecmpTo(string to)`
- `string Chr(int code) [static]`
- `bool Contains(string what)`
- `bool Containsn(string what)`
- `int Count(string what, int from = 0, int to = 0)`
- `int Countn(string what, int from = 0, int to = 0)`
- `string Dedent()`
- `bool EndsWith(string text)`
- `string Erase(int position, int chars = 1)`
- `int FilecasecmpTo(string to)`
- `int FilenocasecmpTo(string to)`
- `int Find(string what, int from = 0)`
- `int Findn(string what, int from = 0)`
- `string Format(Variant values, string placeholder = "{_}")`
- `string GetBaseDir()`
- `string GetBasename()`
- `string GetExtension()`
- `string GetFile()`
- `string GetSlice(string delimiter, int slice)`
- `int GetSliceCount(string delimiter)`
- `string GetSlicec(int delimiter, int slice)`
- `int Hash()`
- `PackedByteArray HexDecode()`
- `int HexToInt()`
- `string HumanizeSize(int size) [static]`
- `string Indent(string prefix)`
- `string Insert(int position, string what)`
- `bool IsAbsolutePath()`
- `bool IsEmpty()`
- `bool IsRelativePath()`
- `bool IsSubsequenceOf(string text)`
- `bool IsSubsequenceOfn(string text)`
- `bool IsValidAsciiIdentifier()`
- `bool IsValidFilename()`

**C# Examples**
```csharp
GD.Print("101".BinToInt());   // Prints 5
GD.Print("0b101".BinToInt()); // Prints 5
GD.Print("-0b10".BinToInt()); // Prints -2
```
```csharp
"move_local_x".Capitalize();   // Returns "Move Local X"
"sceneFile_path".Capitalize(); // Returns "Scene File Path"
"2D, FPS, PNG".Capitalize();   // Returns "2d, Fps, Png"
```

### SubtweenTweener
*Inherits: **Tweener < RefCounted < Object***

SubtweenTweener is used to execute a Tween as one step in a sequence defined by another Tween. See Tween.tween_subtween() for more usage information.

**Methods**
- `SubtweenTweener SetDelay(float delay)`

### SyntaxHighlighter
*Inherits: **Resource < RefCounted < Object** | Inherited by: CodeHighlighter, EditorSyntaxHighlighter*

Base class for syntax highlighters. Provides syntax highlighting data to a TextEdit. The associated TextEdit will call into the SyntaxHighlighter on an as-needed basis.

**Methods**
- `void _ClearHighlightingCache() [virtual]`
- `Godot.Collections.Dictionary _GetLineSyntaxHighlighting(int line) [virtual]`
- `void _UpdateCache() [virtual]`
- `void ClearHighlightingCache()`
- `Godot.Collections.Dictionary GetLineSyntaxHighlighting(int line)`
- `TextEdit GetTextEdit()`
- `void UpdateCache()`

### TextLine
*Inherits: **RefCounted < Object***

Abstraction over TextServer for handling a single line of text.

**Properties**
- `HorizontalAlignment Alignment` = `0`
- `Direction Direction` = `0`
- `string EllipsisChar` = `"…"`
- `BitField[JustificationFlag] Flags` = `3`
- `Orientation Orientation` = `0`
- `bool PreserveControl` = `false`
- `bool PreserveInvalid` = `true`
- `OverrunBehavior TextOverrunBehavior` = `3`
- `float Width` = `-1.0`

**Methods**
- `bool AddObject(Variant key, Vector2 size, InlineAlignment inlineAlign = 5, int length = 1, float baseline = 0.0)`
- `bool AddString(string text, Font font, int fontSize, string language = "", Variant meta = null)`
- `void Clear()`
- `void Draw(RID canvas, Vector2 pos, Color color = Color(1, 1, 1, 1), float oversampling = 0.0)`
- `void DrawOutline(RID canvas, Vector2 pos, int outlineSize = 1, Color color = Color(1, 1, 1, 1), float oversampling = 0.0)`
- `TextLine Duplicate()`
- `Direction GetInferredDirection()`
- `float GetLineAscent()`
- `float GetLineDescent()`
- `float GetLineUnderlinePosition()`
- `float GetLineUnderlineThickness()`
- `float GetLineWidth()`
- `Rect2 GetObjectRect(Variant key)`
- `Godot.Collections.Array GetObjects()`
- `RID GetRid()`
- `Vector2 GetSize()`
- `bool HasObject(Variant key)`
- `int HitTest(float coords)`
- `bool ResizeObject(Variant key, Vector2 size, InlineAlignment inlineAlign = 5, float baseline = 0.0)`
- `void SetBidiOverride(Godot.Collections.Array override)`
- `void TabAlign(PackedFloat32Array tabStops)`

### TextMesh
*Inherits: **PrimitiveMesh < Mesh < Resource < RefCounted < Object***

Generate a PrimitiveMesh from the text.

**Properties**
- `AutowrapMode AutowrapMode` = `0`
- `float CurveStep` = `0.5`
- `float Depth` = `0.05`
- `Font Font`
- `int FontSize` = `16`
- `HorizontalAlignment HorizontalAlignment` = `1`
- `BitField[JustificationFlag] JustificationFlags` = `163`
- `string Language` = `""`
- `float LineSpacing` = `0.0`
- `Vector2 Offset` = `Vector2(0, 0)`
- `float PixelSize` = `0.01`
- `StructuredTextParser StructuredTextBidiOverride` = `0`
- `Godot.Collections.Array StructuredTextBidiOverrideOptions` = `[]`
- `string Text` = `""`
- `Direction TextDirection` = `0`
- `bool Uppercase` = `false`
- `VerticalAlignment VerticalAlignment` = `1`
- `float Width` = `500.0`

### TextParagraph
*Inherits: **RefCounted < Object***

Abstraction over TextServer for handling a single paragraph of text.

**Properties**
- `HorizontalAlignment Alignment` = `0`
- `BitField[LineBreakFlag] BreakFlags` = `3`
- `string CustomPunctuation` = `""`
- `Direction Direction` = `0`
- `string EllipsisChar` = `"…"`
- `BitField[JustificationFlag] JustificationFlags` = `163`
- `float LineSpacing` = `0.0`
- `int MaxLinesVisible` = `-1`
- `Orientation Orientation` = `0`
- `bool PreserveControl` = `false`
- `bool PreserveInvalid` = `true`
- `OverrunBehavior TextOverrunBehavior` = `0`
- `float Width` = `-1.0`

**Methods**
- `bool AddObject(Variant key, Vector2 size, InlineAlignment inlineAlign = 5, int length = 1, float baseline = 0.0)`
- `bool AddString(string text, Font font, int fontSize, string language = "", Variant meta = null)`
- `void Clear()`
- `void ClearDropcap()`
- `void Draw(RID canvas, Vector2 pos, Color color = Color(1, 1, 1, 1), Color dcColor = Color(1, 1, 1, 1), float oversampling = 0.0)`
- `void DrawDropcap(RID canvas, Vector2 pos, Color color = Color(1, 1, 1, 1), float oversampling = 0.0)`
- `void DrawDropcapOutline(RID canvas, Vector2 pos, int outlineSize = 1, Color color = Color(1, 1, 1, 1), float oversampling = 0.0)`
- `void DrawLine(RID canvas, Vector2 pos, int line, Color color = Color(1, 1, 1, 1), float oversampling = 0.0)`
- `void DrawLineOutline(RID canvas, Vector2 pos, int line, int outlineSize = 1, Color color = Color(1, 1, 1, 1), float oversampling = 0.0)`
- `void DrawOutline(RID canvas, Vector2 pos, int outlineSize = 1, Color color = Color(1, 1, 1, 1), Color dcColor = Color(1, 1, 1, 1), float oversampling = 0.0)`
- `TextParagraph Duplicate()`
- `int GetDropcapLines()`
- `RID GetDropcapRid()`
- `Vector2 GetDropcapSize()`
- `Direction GetInferredDirection()`
- `float GetLineAscent(int line)`
- `int GetLineCount()`
- `float GetLineDescent(int line)`
- `Rect2 GetLineObjectRect(int line, Variant key)`
- `Godot.Collections.Array GetLineObjects(int line)`
- `Vector2i GetLineRange(int line)`
- `RID GetLineRid(int line)`
- `Vector2 GetLineSize(int line)`
- `float GetLineUnderlinePosition(int line)`
- `float GetLineUnderlineThickness(int line)`
- `float GetLineWidth(int line)`
- `Vector2 GetNonWrappedSize()`
- `Vector2i GetRange()`
- `RID GetRid()`
- `Vector2 GetSize()`
- `bool HasObject(Variant key)`
- `int HitTest(Vector2 coords)`
- `bool ResizeObject(Variant key, Vector2 size, InlineAlignment inlineAlign = 5, float baseline = 0.0)`
- `void SetBidiOverride(Godot.Collections.Array override)`
- `bool SetDropcap(string text, Font font, int fontSize, Rect2 dropcapMargins = Rect2(0, 0, 0, 0), string language = "")`
- `void TabAlign(PackedFloat32Array tabStops)`

### TextServerAdvanced
*Inherits: **TextServerExtension < TextServer < RefCounted < Object***

An implementation of TextServer that uses HarfBuzz, ICU and SIL Graphite to support BiDi, complex text layouts and contextual OpenType features. This is Godot's default primary TextServer interface.

### TextServerDummy
*Inherits: **TextServerExtension < TextServer < RefCounted < Object***

A dummy TextServer interface that doesn't do anything. Useful for freeing up memory when rendering text is not needed, as text servers are resource-intensive. It can also be used for performance comparisons in complex GUIs to check the impact of text rendering.

### TextServerExtension
*Inherits: **TextServer < RefCounted < Object** | Inherited by: TextServerAdvanced, TextServerDummy, TextServerFallback*

External TextServer implementations should inherit from this class.

**Methods**
- `void _Cleanup() [virtual]`
- `RID _CreateFont() [virtual]`
- `RID _CreateFontLinkedVariation(RID fontRid) [virtual]`
- `RID _CreateShapedText(Direction direction, Orientation orientation) [virtual]`
- `void _DrawHexCodeBox(RID canvas, int size, Vector2 pos, int index, Color color) [virtual]`
- `void _FontClearGlyphs(RID fontRid, Vector2i size) [virtual]`
- `void _FontClearKerningMap(RID fontRid, int size) [virtual]`
- `void _FontClearSizeCache(RID fontRid) [virtual]`
- `void _FontClearSystemFallbackCache() [virtual]`
- `void _FontClearTextures(RID fontRid, Vector2i size) [virtual]`
- `void _FontDrawGlyph(RID fontRid, RID canvas, int size, Vector2 pos, int index, Color color, float oversampling) [virtual]`
- `void _FontDrawGlyphOutline(RID fontRid, RID canvas, int size, int outlineSize, Vector2 pos, int index, Color color, float oversampling) [virtual]`
- `FontAntialiasing _FontGetAntialiasing(RID fontRid) [virtual]`
- `float _FontGetAscent(RID fontRid, int size) [virtual]`
- `float _FontGetBaselineOffset(RID fontRid) [virtual]`
- `int _FontGetCharFromGlyphIndex(RID fontRid, int size, int glyphIndex) [virtual]`
- `float _FontGetDescent(RID fontRid, int size) [virtual]`
- `bool _FontGetDisableEmbeddedBitmaps(RID fontRid) [virtual]`
- `float _FontGetEmbolden(RID fontRid) [virtual]`
- `int _FontGetFaceCount(RID fontRid) [virtual]`
- `int _FontGetFaceIndex(RID fontRid) [virtual]`
- `int _FontGetFixedSize(RID fontRid) [virtual]`
- `FixedSizeScaleMode _FontGetFixedSizeScaleMode(RID fontRid) [virtual]`
- `bool _FontGetGenerateMipmaps(RID fontRid) [virtual]`
- `float _FontGetGlobalOversampling() [virtual]`
- `Vector2 _FontGetGlyphAdvance(RID fontRid, int size, int glyph) [virtual]`
- `Godot.Collections.Dictionary _FontGetGlyphContours(RID fontRid, int size, int index) [virtual]`
- `int _FontGetGlyphIndex(RID fontRid, int size, int char, int variationSelector) [virtual]`
- `PackedInt32Array _FontGetGlyphList(RID fontRid, Vector2i size) [virtual]`
- `Vector2 _FontGetGlyphOffset(RID fontRid, Vector2i size, int glyph) [virtual]`
- `Vector2 _FontGetGlyphSize(RID fontRid, Vector2i size, int glyph) [virtual]`
- `int _FontGetGlyphTextureIdx(RID fontRid, Vector2i size, int glyph) [virtual]`
- `RID _FontGetGlyphTextureRid(RID fontRid, Vector2i size, int glyph) [virtual]`
- `Vector2 _FontGetGlyphTextureSize(RID fontRid, Vector2i size, int glyph) [virtual]`
- `Rect2 _FontGetGlyphUvRect(RID fontRid, Vector2i size, int glyph) [virtual]`
- `Hinting _FontGetHinting(RID fontRid) [virtual]`
- `bool _FontGetKeepRoundingRemainders(RID fontRid) [virtual]`
- `Vector2 _FontGetKerning(RID fontRid, int size, Vector2i glyphPair) [virtual]`
- `Array[Vector2i] _FontGetKerningList(RID fontRid, int size) [virtual]`
- `bool _FontGetLanguageSupportOverride(RID fontRid, string language) [virtual]`

### TextServerFallback
*Inherits: **TextServerExtension < TextServer < RefCounted < Object***

A fallback implementation of Godot's text server. This fallback is faster than TextServerAdvanced for processing a lot of text, but it does not support BiDi and complex text layout.

### TextServerManager
*Inherits: **Object***

TextServerManager is the API backend for loading, enumerating, and switching TextServers.

**Methods**
- `void AddInterface(TextServer interface)`
- `TextServer FindInterface(string name)`
- `TextServer GetInterface(int idx)`
- `int GetInterfaceCount()`
- `Array[Dictionary] GetInterfaces()`
- `TextServer GetPrimaryInterface()`
- `void RemoveInterface(TextServer interface)`
- `void SetPrimaryInterface(TextServer index)`

### TextServer
*Inherits: **RefCounted < Object** | Inherited by: TextServerExtension*

TextServer is the API backend for managing fonts and rendering text.

**Methods**
- `RID CreateFont()`
- `RID CreateFontLinkedVariation(RID fontRid)`
- `RID CreateShapedText(Direction direction = 0, Orientation orientation = 0)`
- `void DrawHexCodeBox(RID canvas, int size, Vector2 pos, int index, Color color)`
- `void FontClearGlyphs(RID fontRid, Vector2i size)`
- `void FontClearKerningMap(RID fontRid, int size)`
- `void FontClearSizeCache(RID fontRid)`
- `void FontClearSystemFallbackCache()`
- `void FontClearTextures(RID fontRid, Vector2i size)`
- `void FontDrawGlyph(RID fontRid, RID canvas, int size, Vector2 pos, int index, Color color = Color(1, 1, 1, 1), float oversampling = 0.0)`
- `void FontDrawGlyphOutline(RID fontRid, RID canvas, int size, int outlineSize, Vector2 pos, int index, Color color = Color(1, 1, 1, 1), float oversampling = 0.0)`
- `FontAntialiasing FontGetAntialiasing(RID fontRid)`
- `float FontGetAscent(RID fontRid, int size)`
- `float FontGetBaselineOffset(RID fontRid)`
- `int FontGetCharFromGlyphIndex(RID fontRid, int size, int glyphIndex)`
- `float FontGetDescent(RID fontRid, int size)`
- `bool FontGetDisableEmbeddedBitmaps(RID fontRid)`
- `float FontGetEmbolden(RID fontRid)`
- `int FontGetFaceCount(RID fontRid)`
- `int FontGetFaceIndex(RID fontRid)`
- `int FontGetFixedSize(RID fontRid)`
- `FixedSizeScaleMode FontGetFixedSizeScaleMode(RID fontRid)`
- `bool FontGetGenerateMipmaps(RID fontRid)`
- `float FontGetGlobalOversampling()`
- `Vector2 FontGetGlyphAdvance(RID fontRid, int size, int glyph)`
- `Godot.Collections.Dictionary FontGetGlyphContours(RID font, int size, int index)`
- `int FontGetGlyphIndex(RID fontRid, int size, int char, int variationSelector)`
- `PackedInt32Array FontGetGlyphList(RID fontRid, Vector2i size)`
- `Vector2 FontGetGlyphOffset(RID fontRid, Vector2i size, int glyph)`
- `Vector2 FontGetGlyphSize(RID fontRid, Vector2i size, int glyph)`
- `int FontGetGlyphTextureIdx(RID fontRid, Vector2i size, int glyph)`
- `RID FontGetGlyphTextureRid(RID fontRid, Vector2i size, int glyph)`
- `Vector2 FontGetGlyphTextureSize(RID fontRid, Vector2i size, int glyph)`
- `Rect2 FontGetGlyphUvRect(RID fontRid, Vector2i size, int glyph)`
- `Hinting FontGetHinting(RID fontRid)`
- `bool FontGetKeepRoundingRemainders(RID fontRid)`
- `Vector2 FontGetKerning(RID fontRid, int size, Vector2i glyphPair)`
- `Array[Vector2i] FontGetKerningList(RID fontRid, int size)`
- `bool FontGetLanguageSupportOverride(RID fontRid, string language)`
- `PackedStringArray FontGetLanguageSupportOverrides(RID fontRid)`

**C# Examples**
```csharp
var ts = TextServerManager.GetPrimaryInterface();
```

### ThemeDB
*Inherits: **Object***

This singleton provides access to static information about Theme resources used by the engine and by your projects. You can fetch the default engine theme, as well as your project configured theme.

**Properties**
- `float FallbackBaseScale` = `1.0`
- `Font FallbackFont`
- `int FallbackFontSize` = `16`
- `Texture2D FallbackIcon`
- `StyleBox FallbackStylebox`

**Methods**
- `Theme GetDefaultTheme()`
- `Theme GetProjectTheme()`

### Theme
*Inherits: **Resource < RefCounted < Object***

A resource used for styling/skinning Control and Window nodes. While individual controls can be styled using their local theme overrides (see Control.add_theme_color_override()), theme resources allow you to store and apply the same settings across all controls sharing the same type (e.g. style all Buttons the same). One theme resource can be used for the entire project, but you can also set a separate theme resource to a branch of control nodes. A theme resource assigned to a control applies to the control itself, as well as all of its direct and indirect children (as long as a chain of controls is uninterrupted).

**Properties**
- `float DefaultBaseScale` = `0.0`
- `Font DefaultFont`
- `int DefaultFontSize` = `-1`

**Methods**
- `void AddType(StringName themeType)`
- `void Clear()`
- `void ClearColor(StringName name, StringName themeType)`
- `void ClearConstant(StringName name, StringName themeType)`
- `void ClearFont(StringName name, StringName themeType)`
- `void ClearFontSize(StringName name, StringName themeType)`
- `void ClearIcon(StringName name, StringName themeType)`
- `void ClearStylebox(StringName name, StringName themeType)`
- `void ClearThemeItem(DataType dataType, StringName name, StringName themeType)`
- `void ClearTypeVariation(StringName themeType)`
- `Color GetColor(StringName name, StringName themeType)`
- `PackedStringArray GetColorList(string themeType)`
- `PackedStringArray GetColorTypeList()`
- `int GetConstant(StringName name, StringName themeType)`
- `PackedStringArray GetConstantList(string themeType)`
- `PackedStringArray GetConstantTypeList()`
- `Font GetFont(StringName name, StringName themeType)`
- `PackedStringArray GetFontList(string themeType)`
- `int GetFontSize(StringName name, StringName themeType)`
- `PackedStringArray GetFontSizeList(string themeType)`
- `PackedStringArray GetFontSizeTypeList()`
- `PackedStringArray GetFontTypeList()`
- `Texture2D GetIcon(StringName name, StringName themeType)`
- `PackedStringArray GetIconList(string themeType)`
- `PackedStringArray GetIconTypeList()`
- `StyleBox GetStylebox(StringName name, StringName themeType)`
- `PackedStringArray GetStyleboxList(string themeType)`
- `PackedStringArray GetStyleboxTypeList()`
- `Variant GetThemeItem(DataType dataType, StringName name, StringName themeType)`
- `PackedStringArray GetThemeItemList(DataType dataType, string themeType)`
- `PackedStringArray GetThemeItemTypeList(DataType dataType)`
- `PackedStringArray GetTypeList()`
- `StringName GetTypeVariationBase(StringName themeType)`
- `PackedStringArray GetTypeVariationList(StringName baseType)`
- `bool HasColor(StringName name, StringName themeType)`
- `bool HasConstant(StringName name, StringName themeType)`
- `bool HasDefaultBaseScale()`
- `bool HasDefaultFont()`
- `bool HasDefaultFontSize()`
- `bool HasFont(StringName name, StringName themeType)`

### Timer
*Inherits: **Node < Object***

The Timer node is a countdown timer and is the simplest way to handle time-based logic in the engine. When a timer reaches the end of its wait_time, it will emit the timeout signal.

**Properties**
- `bool Autostart` = `false`
- `bool IgnoreTimeScale` = `false`
- `bool OneShot` = `false`
- `bool Paused`
- `TimerProcessCallback ProcessCallback` = `1`
- `float TimeLeft`
- `float WaitTime` = `1.0`

**Methods**
- `bool IsStopped()`
- `void Start(float timeSec = -1)`
- `void Stop()`

### Time
*Inherits: **Object***

The Time singleton allows converting time between various formats and also getting time information from the system.

**Methods**
- `Godot.Collections.Dictionary GetDateDictFromSystem(bool utc = false)`
- `Godot.Collections.Dictionary GetDateDictFromUnixTime(int unixTimeVal)`
- `string GetDateStringFromSystem(bool utc = false)`
- `string GetDateStringFromUnixTime(int unixTimeVal)`
- `Godot.Collections.Dictionary GetDatetimeDictFromDatetimeString(string datetime, bool weekday)`
- `Godot.Collections.Dictionary GetDatetimeDictFromSystem(bool utc = false)`
- `Godot.Collections.Dictionary GetDatetimeDictFromUnixTime(int unixTimeVal)`
- `string GetDatetimeStringFromDatetimeDict(Godot.Collections.Dictionary datetime, bool useSpace)`
- `string GetDatetimeStringFromSystem(bool utc = false, bool useSpace = false)`
- `string GetDatetimeStringFromUnixTime(int unixTimeVal, bool useSpace = false)`
- `string GetOffsetStringFromOffsetMinutes(int offsetMinutes)`
- `int GetTicksMsec()`
- `int GetTicksUsec()`
- `Godot.Collections.Dictionary GetTimeDictFromSystem(bool utc = false)`
- `Godot.Collections.Dictionary GetTimeDictFromUnixTime(int unixTimeVal)`
- `string GetTimeStringFromSystem(bool utc = false)`
- `string GetTimeStringFromUnixTime(int unixTimeVal)`
- `Godot.Collections.Dictionary GetTimeZoneFromSystem()`
- `int GetUnixTimeFromDatetimeDict(Godot.Collections.Dictionary datetime)`
- `int GetUnixTimeFromDatetimeString(string datetime)`
- `float GetUnixTimeFromSystem()`

### TorusMesh
*Inherits: **PrimitiveMesh < Mesh < Resource < RefCounted < Object***

Class representing a torus PrimitiveMesh.

**Properties**
- `float InnerRadius` = `0.5`
- `float OuterRadius` = `1.0`
- `int RingSegments` = `32`
- `int Rings` = `64`

### TranslationDomain
*Inherits: **RefCounted < Object***

TranslationDomain is a self-contained collection of Translation resources. Translations can be added to or removed from it.

**Properties**
- `bool Enabled` = `true`
- `bool PseudolocalizationAccentsEnabled` = `true`
- `bool PseudolocalizationDoubleVowelsEnabled` = `false`
- `bool PseudolocalizationEnabled` = `false`
- `float PseudolocalizationExpansionRatio` = `0.0`
- `bool PseudolocalizationFakeBidiEnabled` = `false`
- `bool PseudolocalizationOverrideEnabled` = `false`
- `string PseudolocalizationPrefix` = `"["`
- `bool PseudolocalizationSkipPlaceholdersEnabled` = `true`
- `string PseudolocalizationSuffix` = `"]"`

**Methods**
- `void AddTranslation(Translation translation)`
- `void Clear()`
- `Array[Translation] FindTranslations(string locale, bool exact)`
- `string GetLocaleOverride()`
- `Translation GetTranslationObject(string locale)`
- `Array[Translation] GetTranslations()`
- `bool HasTranslation(Translation translation)`
- `bool HasTranslationForLocale(string locale, bool exact)`
- `StringName Pseudolocalize(StringName message)`
- `void RemoveTranslation(Translation translation)`
- `void SetLocaleOverride(string locale)`
- `StringName Translate(StringName message, StringName context = &"")`
- `StringName TranslatePlural(StringName message, StringName messagePlural, int n, StringName context = &"")`

### TranslationServer
*Inherits: **Object***

The translation server is the API backend that manages all language translations.

**Properties**
- `bool PseudolocalizationEnabled` = `false`

**Methods**
- `void AddTranslation(Translation translation)`
- `void Clear()`
- `int CompareLocales(string localeA, string localeB)`
- `Array[Translation] FindTranslations(string locale, bool exact)`
- `string FormatNumber(string number, string locale)`
- `PackedStringArray GetAllCountries()`
- `PackedStringArray GetAllLanguages()`
- `PackedStringArray GetAllScripts()`
- `string GetCountryName(string country)`
- `string GetLanguageName(string language)`
- `PackedStringArray GetLoadedLocales()`
- `string GetLocale()`
- `string GetLocaleName(string locale)`
- `TranslationDomain GetOrAddDomain(StringName domain)`
- `string GetPercentSign(string locale)`
- `string GetPluralRules(string locale)`
- `string GetScriptName(string script)`
- `string GetToolLocale()`
- `Translation GetTranslationObject(string locale)`
- `Array[Translation] GetTranslations()`
- `bool HasDomain(StringName domain)`
- `bool HasTranslation(Translation translation)`
- `bool HasTranslationForLocale(string locale, bool exact)`
- `string ParseNumber(string number, string locale)`
- `StringName Pseudolocalize(StringName message)`
- `void ReloadPseudolocalization()`
- `void RemoveDomain(StringName domain)`
- `void RemoveTranslation(Translation translation)`
- `void SetLocale(string locale)`
- `string StandardizeLocale(string locale, bool addDefaults = false)`
- `StringName Translate(StringName message, StringName context = &"")`
- `StringName TranslatePlural(StringName message, StringName pluralMessage, int n, StringName context = &"")`

### Translation
*Inherits: **Resource < RefCounted < Object** | Inherited by: OptimizedTranslation*

Translation maps a collection of strings to their individual translations, and also provides convenience methods for pluralization.

**Properties**
- `string Locale` = `"en"`
- `string PluralRulesOverride` = `""`

**Methods**
- `StringName _GetMessage(StringName srcMessage, StringName context) [virtual]`
- `StringName _GetPluralMessage(StringName srcMessage, StringName srcPluralMessage, int n, StringName context) [virtual]`
- `void AddMessage(StringName srcMessage, StringName xlatedMessage, StringName context = &"")`
- `void AddPluralMessage(StringName srcMessage, PackedStringArray xlatedMessages, StringName context = &"")`
- `void EraseMessage(StringName srcMessage, StringName context = &"")`
- `StringName GetMessage(StringName srcMessage, StringName context = &"")`
- `int GetMessageCount()`
- `PackedStringArray GetMessageList()`
- `StringName GetPluralMessage(StringName srcMessage, StringName srcPluralMessage, int n, StringName context = &"")`
- `PackedStringArray GetTranslatedMessageList()`

### TreeItem
*Inherits: **Object***

A single item of a Tree control. It can contain other TreeItems as children, which allows it to create a hierarchy. It can also contain text and buttons. TreeItem is not a Node, it is internal to the Tree.

**Properties**
- `bool Collapsed`
- `int CustomMinimumHeight`
- `bool DisableFolding`
- `bool Visible`

**Methods**
- `void AddButton(int column, Texture2D button, int id = -1, bool disabled = false, string tooltipText = "", string description = "")`
- `void AddChild(TreeItem child)`
- `void CallRecursive(StringName method)`
- `void ClearButtons()`
- `void ClearCustomBgColor(int column)`
- `void ClearCustomColor(int column)`
- `TreeItem CreateChild(int index = -1)`
- `void Deselect(int column)`
- `void EraseButton(int column, int buttonIndex)`
- `AutoTranslateMode GetAutoTranslateMode(int column)`
- `AutowrapMode GetAutowrapMode(int column)`
- `Texture2D GetButton(int column, int buttonIndex)`
- `int GetButtonById(int column, int id)`
- `Color GetButtonColor(int column, int id)`
- `int GetButtonCount(int column)`
- `int GetButtonId(int column, int buttonIndex)`
- `string GetButtonTooltipText(int column, int buttonIndex)`
- `TreeCellMode GetCellMode(int column)`
- `TreeItem GetChild(int index)`
- `int GetChildCount()`
- `Array[TreeItem] GetChildren()`
- `Color GetCustomBgColor(int column)`
- `Color GetCustomColor(int column)`
- `Callable GetCustomDrawCallback(int column)`
- `Font GetCustomFont(int column)`
- `int GetCustomFontSize(int column)`
- `StyleBox GetCustomStylebox(int column)`
- `string GetDescription(int column)`
- `bool GetExpandRight(int column)`
- `TreeItem GetFirstChild()`
- `Texture2D GetIcon(int column)`
- `int GetIconMaxWidth(int column)`
- `Color GetIconModulate(int column)`
- `Texture2D GetIconOverlay(int column)`
- `Rect2 GetIconRegion(int column)`
- `int GetIndex()`
- `string GetLanguage(int column)`
- `Variant GetMetadata(int column)`
- `TreeItem GetNext()`
- `TreeItem GetNextInTree(bool wrap = false)`

### Tree
*Inherits: **Control < CanvasItem < Node < Object***

A control used to show a set of internal TreeItems in a hierarchical structure. The tree items can be selected, expanded and collapsed. The tree can have multiple columns with custom controls like LineEdits, buttons and popups. It can be useful for structured displays and interactions.

**Properties**
- `bool AllowReselect` = `false`
- `bool AllowRmbSelect` = `false`
- `bool AllowSearch` = `true`
- `bool AutoTooltip` = `true`
- `bool ClipContents` = `true (overrides Control)`
- `bool ColumnTitlesVisible` = `false`
- `int Columns` = `1`
- `int DropModeFlags` = `0`
- `bool EnableDragUnfolding` = `true`
- `bool EnableRecursiveFolding` = `true`
- `FocusMode FocusMode` = `2 (overrides Control)`
- `bool HideFolding` = `false`
- `bool HideRoot` = `false`
- `ScrollHintMode ScrollHintMode` = `0`
- `bool ScrollHorizontalEnabled` = `true`
- `bool ScrollVerticalEnabled` = `true`
- `SelectMode SelectMode` = `0`
- `bool TileScrollHint` = `false`

**Methods**
- `void Clear()`
- `TreeItem CreateItem(TreeItem parent = null, int index = -1)`
- `void DeselectAll()`
- `bool EditSelected(bool forceEdit = false)`
- `void EnsureCursorIsVisible()`
- `int GetButtonIdAtPosition(Vector2 position)`
- `int GetColumnAtPosition(Vector2 position)`
- `int GetColumnExpandRatio(int column)`
- `string GetColumnTitle(int column)`
- `HorizontalAlignment GetColumnTitleAlignment(int column)`
- `TextDirection GetColumnTitleDirection(int column)`
- `string GetColumnTitleLanguage(int column)`
- `string GetColumnTitleTooltipText(int column)`
- `int GetColumnWidth(int column)`
- `Rect2 GetCustomPopupRect()`
- `int GetDropSectionAtPosition(Vector2 position)`
- `TreeItem GetEdited()`
- `int GetEditedColumn()`
- `Rect2 GetItemAreaRect(TreeItem item, int column = -1, int buttonIndex = -1)`
- `TreeItem GetItemAtPosition(Vector2 position)`
- `TreeItem GetNextSelected(TreeItem from)`
- `int GetPressedButton()`
- `TreeItem GetRoot()`
- `Vector2 GetScroll()`
- `TreeItem GetSelected()`
- `int GetSelectedColumn()`
- `bool IsColumnClippingContent(int column)`
- `bool IsColumnExpanding(int column)`
- `void ScrollToItem(TreeItem item, bool centerOnItem = false)`
- `void SetColumnClipContent(int column, bool enable)`
- `void SetColumnCustomMinimumWidth(int column, int minWidth)`
- `void SetColumnExpand(int column, bool expand)`
- `void SetColumnExpandRatio(int column, int ratio)`
- `void SetColumnTitle(int column, string title)`
- `void SetColumnTitleAlignment(int column, HorizontalAlignment titleAlignment)`
- `void SetColumnTitleDirection(int column, TextDirection direction)`
- `void SetColumnTitleLanguage(int column, string language)`
- `void SetColumnTitleTooltipText(int column, string tooltipText)`
- `void SetSelected(TreeItem item, int column)`

**C# Examples**
```csharp
public override void _Ready()
{
    var tree = new Tree();
    TreeItem root = tree.CreateItem();
    tree.HideRoot = true;
    TreeItem child1 = tree.CreateItem(root);
    TreeItem child2 = tree.CreateItem(root);
    TreeItem subchild1 = tree.CreateItem(child1);
    subchild1.SetText(0, "Subchild1");
}
```
```csharp
public override void _Ready()
{
    GetNode<Tree>("Tree").ItemEdited += OnTreeItemEdited;
}

public void OnTreeItemEdited()
{
    GD.Print(GetNode<Tree>("Tree").GetEdited()); // This item just got edited (e.g. checked).
}
```

### TriangleMesh
*Inherits: **RefCounted < Object***

Creates a bounding volume hierarchy (BVH) tree structure around triangle geometry.

**Methods**
- `bool CreateFromFaces(PackedVector3Array faces)`
- `PackedVector3Array GetFaces()`
- `Godot.Collections.Dictionary IntersectRay(Vector3 begin, Vector3 dir)`
- `Godot.Collections.Dictionary IntersectSegment(Vector3 begin, Vector3 end)`

### Tween
*Inherits: **RefCounted < Object***

Tweens are mostly useful for animations requiring a numerical property to be interpolated over a range of values. The name tween comes from in-betweening, an animation technique where you specify keyframes and the computer interpolates the frames that appear between them. Animating something with a Tween is called tweening.

**Methods**
- `Tween BindNode(Node node)`
- `Tween Chain()`
- `bool CustomStep(float delta)`
- `int GetLoopsLeft()`
- `float GetTotalElapsedTime()`
- `Variant InterpolateValue(Variant initialValue, Variant deltaValue, float elapsedTime, float duration, TransitionType transType, EaseType easeType) [static]`
- `bool IsRunning()`
- `bool IsValid()`
- `void Kill()`
- `Tween Parallel()`
- `void Pause()`
- `void Play()`
- `Tween SetEase(EaseType ease)`
- `Tween SetIgnoreTimeScale(bool ignore = true)`
- `Tween SetLoops(int loops = 0)`
- `Tween SetParallel(bool parallel = true)`
- `Tween SetPauseMode(TweenPauseMode mode)`
- `Tween SetProcessMode(TweenProcessMode mode)`
- `Tween SetSpeedScale(float speed)`
- `Tween SetTrans(TransitionType trans)`
- `void Stop()`
- `CallbackTweener TweenCallback(Callable callback)`
- `IntervalTweener TweenInterval(float time)`
- `MethodTweener TweenMethod(Callable method, Variant from, Variant to, float duration)`
- `PropertyTweener TweenProperty(Object object, NodePath property, Variant finalVal, float duration)`
- `SubtweenTweener TweenSubtween(Tween subtween)`

**C# Examples**
```csharp
Tween tween = GetTree().CreateTween();
tween.TweenProperty(GetNode("Sprite"), "modulate", Colors.Red, 1.0f);
tween.TweenProperty(GetNode("Sprite"), "scale", Vector2.Zero, 1.0f);
tween.TweenCallback(Callable.From(GetNode("Sprite").QueueFree));
```
```csharp
Tween tween = GetTree().CreateTween();
tween.TweenProperty(GetNode("Sprite"), "modulate", Colors.Red, 1.0f).SetTrans(Tween.TransitionType.Sine);
tween.TweenProperty(GetNode("Sprite"), "scale", Vector2.Zero, 1.0f).SetTrans(Tween.TransitionType.Bounce);
tween.TweenCallback(Callable.From(GetNode("Sprite").QueueFree));
```

### TwoBoneIK3D
*Inherits: **IKModifier3D < SkeletonModifier3D < Node3D < Node < Object***

This IKModifier3D requires a pole target. It provides deterministic results by constructing a plane from each joint and pole target and finding the intersection of two circles (disks in 3D).

**Properties**
- `int SettingCount` = `0`

**Methods**
- `int GetEndBone(int index)`
- `BoneDirection GetEndBoneDirection(int index)`
- `float GetEndBoneLength(int index)`
- `string GetEndBoneName(int index)`
- `int GetMiddleBone(int index)`
- `string GetMiddleBoneName(int index)`
- `SecondaryDirection GetPoleDirection(int index)`
- `Vector3 GetPoleDirectionVector(int index)`
- `NodePath GetPoleNode(int index)`
- `int GetRootBone(int index)`
- `string GetRootBoneName(int index)`
- `NodePath GetTargetNode(int index)`
- `bool IsEndBoneExtended(int index)`
- `bool IsUsingVirtualEnd(int index)`
- `void SetEndBone(int index, int bone)`
- `void SetEndBoneDirection(int index, BoneDirection boneDirection)`
- `void SetEndBoneLength(int index, float length)`
- `void SetEndBoneName(int index, string boneName)`
- `void SetExtendEndBone(int index, bool enabled)`
- `void SetMiddleBone(int index, int bone)`
- `void SetMiddleBoneName(int index, string boneName)`
- `void SetPoleDirection(int index, SecondaryDirection direction)`
- `void SetPoleDirectionVector(int index, Vector3 vector)`
- `void SetPoleNode(int index, NodePath poleNode)`
- `void SetRootBone(int index, int bone)`
- `void SetRootBoneName(int index, string boneName)`
- `void SetTargetNode(int index, NodePath targetNode)`
- `void SetUseVirtualEnd(int index, bool enabled)`

### UDSServer
*Inherits: **SocketServer < RefCounted < Object***

A Unix Domain Socket (UDS) server. Listens to connections on a socket path and returns a StreamPeerUDS when it gets an incoming connection. Unix Domain Sockets provide inter-process communication on the same machine using the filesystem namespace.

**Methods**
- `Error Listen(string path)`
- `StreamPeerUDS TakeConnection()`

### UPNPDevice
*Inherits: **RefCounted < Object***

Universal Plug and Play (UPnP) device. See UPNP for UPnP discovery and utility functions. Provides low-level access to UPNP control commands. Allows to manage port mappings (port forwarding) and to query network information of the device (like local and external IP address and status). Note that methods on this class are synchronous and block the calling thread.

**Properties**
- `string DescriptionUrl` = `""`
- `string IgdControlUrl` = `""`
- `string IgdOurAddr` = `""`
- `string IgdServiceType` = `""`
- `IGDStatus IgdStatus` = `9`
- `string ServiceType` = `""`

**Methods**
- `int AddPortMapping(int port, int portInternal = 0, string desc = "", string proto = "UDP", int duration = 0)`
- `int DeletePortMapping(int port, string proto = "UDP")`
- `bool IsValidGateway()`
- `string QueryExternalAddress()`

### UPNP
*Inherits: **RefCounted < Object***

This class can be used to discover compatible UPNPDevices on the local network and execute commands on them, like managing port mappings (for port forwarding/NAT traversal) and querying the local and remote network IP address. Note that methods on this class are synchronous and block the calling thread.

**Properties**
- `bool DiscoverIpv6` = `false`
- `int DiscoverLocalPort` = `0`
- `string DiscoverMulticastIf` = `""`

**Methods**
- `void AddDevice(UPNPDevice device)`
- `int AddPortMapping(int port, int portInternal = 0, string desc = "", string proto = "UDP", int duration = 0)`
- `void ClearDevices()`
- `int DeletePortMapping(int port, string proto = "UDP")`
- `int Discover(int timeout = 2000, int ttl = 2, string deviceFilter = "InternetGatewayDevice")`
- `UPNPDevice GetDevice(int index)`
- `int GetDeviceCount()`
- `UPNPDevice GetGateway()`
- `string QueryExternalAddress()`
- `void RemoveDevice(int index)`
- `void SetDevice(int index, UPNPDevice device)`

### UndoRedo
*Inherits: **Object***

UndoRedo works by registering methods and property changes inside "actions". You can create an action, then provide ways to do and undo this action using function calls and property changes, then commit the action.

**Properties**
- `int MaxSteps` = `0`

**Methods**
- `void AddDoMethod(Callable callable)`
- `void AddDoProperty(Object object, StringName property, Variant value)`
- `void AddDoReference(Object object)`
- `void AddUndoMethod(Callable callable)`
- `void AddUndoProperty(Object object, StringName property, Variant value)`
- `void AddUndoReference(Object object)`
- `void ClearHistory(bool increaseVersion = true)`
- `void CommitAction(bool execute = true)`
- `void CreateAction(string name, MergeMode mergeMode = 0, bool backwardUndoOps = false)`
- `void EndForceKeepInMergeEnds()`
- `string GetActionName(int id)`
- `int GetCurrentAction()`
- `string GetCurrentActionName()`
- `int GetHistoryCount()`
- `int GetVersion()`
- `bool HasRedo()`
- `bool HasUndo()`
- `bool IsCommittingAction()`
- `bool Redo()`
- `void StartForceKeepInMergeEnds()`
- `bool Undo()`

**C# Examples**
```csharp
private UndoRedo _undoRedo;

public override void _Ready()
{
    _undoRedo = new UndoRedo();
}

public void DoSomething()
{
    // Put your code here.
}

public void UndoSomething()
{
    // Put here the code that reverts what's done by "DoSomething()".
}

private void OnMyButtonPressed()
{
    var node = GetNode<Node2D>("MyNode2D");
    _undoRedo.CreateAction("Move the node");
    _undoRedo.AddDoMethod(new Callable(this, MethodName.DoSomething));
    _undoRedo.AddUndoMethod(new Callable(this, MethodName.UndoSomething));
    _undoRedo.AddDoProperty(node, "position", new Vector2(100, 100));

// ...
```
```csharp
_undo_redo.CreateAction("Add object");

// DO
_undo_redo.AddDoMethod(new Callable(this, MethodName.CreateObject));
_undo_redo.AddDoMethod(new Callable(this, MethodName.AddObjectToSingleton));

// UNDO
_undo_redo.AddUndoMethod(new Callable(this, MethodName.RemoveObjectFromSingleton));
_undo_redo.AddUndoMethod(new Callable(this, MethodName.DestroyThatObject));

_undo_redo.CommitAction();
```

### UniformSetCacheRD
*Inherits: **Object***

Uniform set cache manager for RenderingDevice-based renderers. Provides a way to create a uniform set and reuse it in subsequent calls for as long as the uniform set exists. Uniform set will automatically be cleaned up when dependent objects are freed.

**Methods**
- `RID GetCache(RID shader, int set, Array[RDUniform] uniforms) [static]`

### VFlowContainer
*Inherits: **FlowContainer < Container < Control < CanvasItem < Node < Object***

A variant of FlowContainer that can only arrange its child controls vertically, wrapping them around at the borders. This is similar to how text in a book wraps around when no more words can fit on a line, except vertically.

### VSeparator
*Inherits: **Separator < Control < CanvasItem < Node < Object***

A vertical separator used for separating other controls that are arranged horizontally. VSeparator is purely visual and normally drawn as a StyleBoxLine.

### Variant

In computer programming, a Variant class is a class that is designed to store a variety of other types. Dynamic programming languages like PHP, Lua, JavaScript and GDScript like to use them to store variables' data on the backend. With these Variants, properties are able to change value types freely.

**C# Examples**
```csharp
// C# is statically typed. Once a variable has a type it cannot be changed. You can use the `var` keyword to let the compiler infer the type automatically.
var foo = 2; // Foo is a 32-bit integer (int). Be cautious, integers in GDScript are 64-bit and the direct C# equivalent is `long`.
// foo = "foo was and will always be an integer. It cannot be turned into a string!";
var boo = "Boo is a string!";
var ref = new RefCounted(); // var is especially useful when used together with a constructor.

// Godot also provides a Variant type that works like a union of all the Variant-compatible types.
V
// ...
```
```csharp
Variant foo = 2;
switch (foo.VariantType)
{
    case Variant.Type.Nil:
        GD.Print("foo is null");
        break;
    case Variant.Type.Int:
        GD.Print("foo is an integer");
        break;
    case Variant.Type.Object:
        // Note that Objects are their own special category.
        // You can convert a Variant to a GodotObject and use reflection to get its name.
        GD.Print($"foo is a(n) {foo.AsGodotObject().GetType().Name}");
        break;
}
```

### VideoStreamPlayback
*Inherits: **Resource < RefCounted < Object***

This class is intended to be overridden by video decoder extensions with custom implementations of VideoStream.

**Methods**
- `int _GetChannels() [virtual]`
- `float _GetLength() [virtual]`
- `int _GetMixRate() [virtual]`
- `float _GetPlaybackPosition() [virtual]`
- `Texture2D _GetTexture() [virtual]`
- `bool _IsPaused() [virtual]`
- `bool _IsPlaying() [virtual]`
- `void _Play() [virtual]`
- `void _Seek(float time) [virtual]`
- `void _SetAudioTrack(int idx) [virtual]`
- `void _SetPaused(bool paused) [virtual]`
- `void _Stop() [virtual]`
- `void _Update(float delta) [virtual]`
- `int MixAudio(int numFrames, PackedFloat32Array buffer = PackedFloat32Array(), int offset = 0)`

### VideoStreamTheora
*Inherits: **VideoStream < Resource < RefCounted < Object***

VideoStream resource handling the Ogg Theora video format with .ogv extension. The Theora codec is decoded on the CPU.

### VideoStream
*Inherits: **Resource < RefCounted < Object** | Inherited by: VideoStreamTheora*

Base resource type for all video streams. Classes that derive from VideoStream can all be used as resource types to play back videos in VideoStreamPlayer.

**Properties**
- `string File` = `""`

**Methods**
- `VideoStreamPlayback _InstantiatePlayback() [virtual]`

### VisibleOnScreenEnabler3D
*Inherits: **VisibleOnScreenNotifier3D < VisualInstance3D < Node3D < Node < Object***

VisibleOnScreenEnabler3D contains a box-shaped region of 3D space and a target node. The target node will be automatically enabled (via its Node.process_mode property) when any part of this region becomes visible on the screen, and automatically disabled otherwise. This can for example be used to activate enemies only when the player approaches them.

**Properties**
- `EnableMode EnableMode` = `0`
- `NodePath EnableNodePath` = `NodePath("..")`

### VisibleOnScreenNotifier3D
*Inherits: **VisualInstance3D < Node3D < Node < Object** | Inherited by: VisibleOnScreenEnabler3D*

VisibleOnScreenNotifier3D represents a box-shaped region of 3D space. When any part of this region becomes visible on screen or in a Camera3D's view, it will emit a screen_entered signal, and likewise it will emit a screen_exited signal when no part of it remains visible.

**Properties**
- `AABB Aabb` = `AABB(-1, -1, -1, 2, 2, 2)`

**Methods**
- `bool IsOnScreen()`

### WebRTCDataChannelExtension
*Inherits: **WebRTCDataChannel < PacketPeer < RefCounted < Object***

There is currently no description for this class. Please help us by contributing one!

**Methods**
- `void _Close() [virtual]`
- `int _GetAvailablePacketCount() [virtual]`
- `int _GetBufferedAmount() [virtual]`
- `int _GetId() [virtual]`
- `string _GetLabel() [virtual]`
- `int _GetMaxPacketLifeTime() [virtual]`
- `int _GetMaxPacketSize() [virtual]`
- `int _GetMaxRetransmits() [virtual]`
- `Error _GetPacket(const uint8_t ** rBuffer, int32_t* rBufferSize) [virtual]`
- `string _GetProtocol() [virtual]`
- `ChannelState _GetReadyState() [virtual]`
- `WriteMode _GetWriteMode() [virtual]`
- `bool _IsNegotiated() [virtual]`
- `bool _IsOrdered() [virtual]`
- `Error _Poll() [virtual]`
- `Error _PutPacket(const uint8_t* pBuffer, int pBufferSize) [virtual]`
- `void _SetWriteMode(WriteMode pWriteMode) [virtual]`
- `bool _WasStringPacket() [virtual]`

### WebRTCDataChannel
*Inherits: **PacketPeer < RefCounted < Object** | Inherited by: WebRTCDataChannelExtension*

There is currently no description for this class. Please help us by contributing one!

**Properties**
- `WriteMode WriteMode` = `1`

**Methods**
- `void Close()`
- `int GetBufferedAmount()`
- `int GetId()`
- `string GetLabel()`
- `int GetMaxPacketLifeTime()`
- `int GetMaxRetransmits()`
- `string GetProtocol()`
- `ChannelState GetReadyState()`
- `bool IsNegotiated()`
- `bool IsOrdered()`
- `Error Poll()`
- `bool WasStringPacket()`

### WebRTCMultiplayerPeer
*Inherits: **MultiplayerPeer < PacketPeer < RefCounted < Object***

This class constructs a full mesh of WebRTCPeerConnection (one connection for each peer) that can be used as a MultiplayerAPI.multiplayer_peer.

**Methods**
- `Error AddPeer(WebRTCPeerConnection peer, int peerId, int unreliableLifetime = 1)`
- `Error CreateClient(int peerId, Godot.Collections.Array channelsConfig = [])`
- `Error CreateMesh(int peerId, Godot.Collections.Array channelsConfig = [])`
- `Error CreateServer(Godot.Collections.Array channelsConfig = [])`
- `Godot.Collections.Dictionary GetPeer(int peerId)`
- `Godot.Collections.Dictionary GetPeers()`
- `bool HasPeer(int peerId)`
- `void RemovePeer(int peerId)`

### WebRTCPeerConnectionExtension
*Inherits: **WebRTCPeerConnection < RefCounted < Object***

There is currently no description for this class. Please help us by contributing one!

**Methods**
- `Error _AddIceCandidate(string pSdpMidName, int pSdpMlineIndex, string pSdpName) [virtual]`
- `void _Close() [virtual]`
- `WebRTCDataChannel _CreateDataChannel(string pLabel, Godot.Collections.Dictionary pConfig) [virtual]`
- `Error _CreateOffer() [virtual]`
- `ConnectionState _GetConnectionState() [virtual]`
- `GatheringState _GetGatheringState() [virtual]`
- `SignalingState _GetSignalingState() [virtual]`
- `Error _Initialize(Godot.Collections.Dictionary pConfig) [virtual]`
- `Error _Poll() [virtual]`
- `Error _SetLocalDescription(string pType, string pSdp) [virtual]`
- `Error _SetRemoteDescription(string pType, string pSdp) [virtual]`

### WebRTCPeerConnection
*Inherits: **RefCounted < Object** | Inherited by: WebRTCPeerConnectionExtension*

A WebRTC connection between the local computer and a remote peer. Provides an interface to connect, maintain, and monitor the connection.

**Methods**
- `Error AddIceCandidate(string media, int index, string name)`
- `void Close()`
- `WebRTCDataChannel CreateDataChannel(string label, Godot.Collections.Dictionary options = {})`
- `Error CreateOffer()`
- `ConnectionState GetConnectionState()`
- `GatheringState GetGatheringState()`
- `SignalingState GetSignalingState()`
- `Error Initialize(Godot.Collections.Dictionary configuration = {})`
- `Error Poll()`
- `void SetDefaultExtension(StringName extensionClass) [static]`
- `Error SetLocalDescription(string type, string sdp)`
- `Error SetRemoteDescription(string type, string sdp)`

### WebXRInterface
*Inherits: **XRInterface < RefCounted < Object***

WebXR is an open standard that allows creating VR and AR applications that run in the web browser.

**Properties**
- `string EnabledFeatures`
- `string OptionalFeatures`
- `string ReferenceSpaceType`
- `string RequestedReferenceSpaceTypes`
- `string RequiredFeatures`
- `string SessionMode`
- `string VisibilityState`

**Methods**
- `Godot.Collections.Array GetAvailableDisplayRefreshRates()`
- `float GetDisplayRefreshRate()`
- `TargetRayMode GetInputSourceTargetRayMode(int inputSourceId)`
- `XRControllerTracker GetInputSourceTracker(int inputSourceId)`
- `bool IsInputSourceActive(int inputSourceId)`
- `void IsSessionSupported(string sessionMode)`
- `void SetDisplayRefreshRate(float refreshRate)`

### World2D
*Inherits: **Resource < RefCounted < Object***

Class that has everything pertaining to a 2D world: A physics space, a canvas, and a sound space. 2D nodes register their resources into the current 2D world.

**Properties**
- `RID Canvas`
- `PhysicsDirectSpaceState2D DirectSpaceState`
- `RID NavigationMap`
- `RID Space`

### World3D
*Inherits: **Resource < RefCounted < Object***

Class that has everything pertaining to a world: A physics space, a visual scenario, and a sound space. 3D nodes register their resources into the current 3D world.

**Properties**
- `CameraAttributes CameraAttributes`
- `PhysicsDirectSpaceState3D DirectSpaceState`
- `Environment Environment`
- `Environment FallbackEnvironment`
- `RID NavigationMap`
- `RID Scenario`
- `RID Space`

### WorldBoundaryShape2D
*Inherits: **Shape2D < Resource < RefCounted < Object***

A 2D world boundary shape, intended for use in physics. WorldBoundaryShape2D works like an infinite straight line that forces all physics bodies to stay above it. The line's normal determines which direction is considered as "above" and in the editor, the smaller line over it represents this direction. It can for example be used for endless flat floors.

**Properties**
- `float Distance` = `0.0`
- `Vector2 Normal` = `Vector2(0, -1)`

### WorldBoundaryShape3D
*Inherits: **Shape3D < Resource < RefCounted < Object***

A 3D world boundary shape, intended for use in physics. WorldBoundaryShape3D works like an infinite plane that forces all physics bodies to stay above it. The plane's normal determines which direction is considered as "above" and in the editor, the line over the plane represents this direction. It can for example be used for endless flat floors.

**Properties**
- `Plane Plane` = `Plane(0, 1, 0, 0)`

### XRAnchor3D
*Inherits: **XRNode3D < Node3D < Node < Object***

The XRAnchor3D point is an XRNode3D that maps a real world location identified by the AR platform to a position within the game world. For example, as long as plane detection in ARKit is on, ARKit will identify and update the position of planes (tables, floors, etc.) and create anchors for them.

**Methods**
- `Plane GetPlane()`
- `Vector3 GetSize()`

### XRBodyModifier3D
*Inherits: **SkeletonModifier3D < Node3D < Node < Object***

This node uses body tracking data from an XRBodyTracker to pose the skeleton of a body mesh.

**Properties**
- `StringName BodyTracker` = `&"/user/body_tracker"`
- `BitField[BodyUpdate] BodyUpdate` = `7`
- `BoneUpdate BoneUpdate` = `0`

### XRBodyTracker
*Inherits: **XRPositionalTracker < XRTracker < RefCounted < Object***

A body tracking system will create an instance of this object and add it to the XRServer. This tracking system will then obtain skeleton data, convert it to the Godot Humanoid skeleton and store this data on the XRBodyTracker object.

**Properties**
- `BitField[BodyFlags] BodyFlags` = `0`
- `bool HasTrackingData` = `false`
- `TrackerType Type` = `32 (overrides XRTracker)`

**Methods**
- `BitField[JointFlags] GetJointFlags(Joint joint)`
- `Transform3D GetJointTransform(Joint joint)`
- `void SetJointFlags(Joint joint, BitField[JointFlags] flags)`
- `void SetJointTransform(Joint joint, Transform3D transform)`

### XRCamera3D
*Inherits: **Camera3D < Node3D < Node < Object***

This is a helper 3D node for our camera. Note that, if stereoscopic rendering is applicable (VR-HMD), most of the camera properties are ignored, as the HMD information overrides them. The only properties that can be trusted are the near and far planes.

**Properties**
- `PhysicsInterpolationMode PhysicsInterpolationMode` = `2 (overrides Node)`

### XRController3D
*Inherits: **XRNode3D < Node3D < Node < Object***

This is a helper 3D node that is linked to the tracking of controllers. It also offers several handy passthroughs to the state of buttons and such on the controllers.

**Methods**
- `float GetFloat(StringName name)`
- `Variant GetInput(StringName name)`
- `TrackerHand GetTrackerHand()`
- `Vector2 GetVector2(StringName name)`
- `bool IsButtonPressed(StringName name)`

### XRControllerTracker
*Inherits: **XRPositionalTracker < XRTracker < RefCounted < Object***

An instance of this object represents a controller that is tracked.

**Properties**
- `TrackerType Type` = `2 (overrides XRTracker)`

### XRFaceModifier3D
*Inherits: **Node3D < Node < Object***

This node applies weights from an XRFaceTracker to a mesh with supporting face blend shapes.

**Properties**
- `StringName FaceTracker` = `&"/user/face_tracker"`
- `NodePath Target` = `NodePath("")`

### XRFaceTracker
*Inherits: **XRTracker < RefCounted < Object***

An instance of this object represents a tracked face and its corresponding blend shapes. The blend shapes come from the Unified Expressions standard, and contain extended details and visuals for each blend shape. Additionally the Tracking Standard Comparison page documents the relationship between Unified Expressions and other standards.

**Properties**
- `PackedFloat32Array BlendShapes` = `PackedFloat32Array()`
- `TrackerType Type` = `64 (overrides XRTracker)`

**Methods**
- `float GetBlendShape(BlendShapeEntry blendShape)`
- `void SetBlendShape(BlendShapeEntry blendShape, float weight)`

### XRHandModifier3D
*Inherits: **SkeletonModifier3D < Node3D < Node < Object***

This node uses hand tracking data from an XRHandTracker to pose the skeleton of a hand mesh.

**Properties**
- `BoneUpdate BoneUpdate` = `0`
- `StringName HandTracker` = `&"/user/hand_tracker/left"`

### XRHandTracker
*Inherits: **XRPositionalTracker < XRTracker < RefCounted < Object***

A hand tracking system will create an instance of this object and add it to the XRServer. This tracking system will then obtain skeleton data, convert it to the Godot Humanoid hand skeleton and store this data on the XRHandTracker object.

**Properties**
- `TrackerHand Hand` = `1 (overrides XRPositionalTracker)`
- `HandTrackingSource HandTrackingSource` = `0`
- `bool HasTrackingData` = `false`
- `TrackerType Type` = `16 (overrides XRTracker)`

**Methods**
- `Vector3 GetHandJointAngularVelocity(HandJoint joint)`
- `BitField[HandJointFlags] GetHandJointFlags(HandJoint joint)`
- `Vector3 GetHandJointLinearVelocity(HandJoint joint)`
- `float GetHandJointRadius(HandJoint joint)`
- `Transform3D GetHandJointTransform(HandJoint joint)`
- `void SetHandJointAngularVelocity(HandJoint joint, Vector3 angularVelocity)`
- `void SetHandJointFlags(HandJoint joint, BitField[HandJointFlags] flags)`
- `void SetHandJointLinearVelocity(HandJoint joint, Vector3 linearVelocity)`
- `void SetHandJointRadius(HandJoint joint, float radius)`
- `void SetHandJointTransform(HandJoint joint, Transform3D transform)`

### XRInterfaceExtension
*Inherits: **XRInterface < RefCounted < Object***

External XR interface plugins should inherit from this class.

**Methods**
- `void _EndFrame() [virtual]`
- `bool _GetAnchorDetectionIsEnabled() [virtual]`
- `int _GetCameraFeedId() [virtual]`
- `Transform3D _GetCameraTransform() [virtual]`
- `int _GetCapabilities() [virtual]`
- `RID _GetColorTexture() [virtual]`
- `RID _GetDepthTexture() [virtual]`
- `StringName _GetName() [virtual]`
- `PackedVector3Array _GetPlayArea() [virtual]`
- `PlayAreaMode _GetPlayAreaMode() [virtual]`
- `PackedFloat64Array _GetProjectionForView(int view, float aspect, float zNear, float zFar) [virtual]`
- `Vector2 _GetRenderTargetSize() [virtual]`
- `PackedStringArray _GetSuggestedPoseNames(StringName trackerName) [virtual]`
- `PackedStringArray _GetSuggestedTrackerNames() [virtual]`
- `Godot.Collections.Dictionary _GetSystemInfo() [virtual]`
- `TrackingStatus _GetTrackingStatus() [virtual]`
- `Transform3D _GetTransformForView(int view, Transform3D camTransform) [virtual]`
- `RID _GetVelocityTexture() [virtual]`
- `int _GetViewCount() [virtual]`
- `RID _GetVrsTexture() [virtual]`
- `VRSTextureFormat _GetVrsTextureFormat() [virtual]`
- `bool _Initialize() [virtual]`
- `bool _IsInitialized() [virtual]`
- `void _PostDrawViewport(RID renderTarget, Rect2 screenRect) [virtual]`
- `bool _PreDrawViewport(RID renderTarget) [virtual]`
- `void _PreRender() [virtual]`
- `void _Process() [virtual]`
- `void _SetAnchorDetectionIsEnabled(bool enabled) [virtual]`
- `bool _SetPlayAreaMode(PlayAreaMode mode) [virtual]`
- `bool _SupportsPlayAreaMode(PlayAreaMode mode) [virtual]`
- `void _TriggerHapticPulse(string actionName, StringName trackerName, float frequency, float amplitude, float durationSec, float delaySec) [virtual]`
- `void _Uninitialize() [virtual]`
- `void AddBlit(RID renderTarget, Rect2 srcRect, Rect2i dstRect, bool useLayer, int layer, bool applyLensDistortion, Vector2 eyeCenter, float k1, float k2, float upscale, float aspectRatio)`
- `RID GetColorTexture()`
- `RID GetDepthTexture()`
- `RID GetRenderTargetTexture(RID renderTarget)`
- `RID GetVelocityTexture()`

### XRInterface
*Inherits: **RefCounted < Object** | Inherited by: MobileVRInterface, OpenXRInterface, WebXRInterface, XRInterfaceExtension*

This class needs to be implemented to make an AR or VR platform available to Godot and these should be implemented as C++ modules or GDExtension modules. Part of the interface is exposed to GDScript so you can detect, enable and configure an AR or VR platform.

**Properties**
- `bool ArIsAnchorDetectionEnabled` = `false`
- `EnvironmentBlendMode EnvironmentBlendMode` = `0`
- `bool InterfaceIsPrimary` = `false`
- `PlayAreaMode XrPlayAreaMode` = `0`

**Methods**
- `int GetCameraFeedId()`
- `int GetCapabilities()`
- `StringName GetName()`
- `PackedVector3Array GetPlayArea()`
- `Projection GetProjectionForView(int view, float aspect, float near, float far)`
- `Vector2 GetRenderTargetSize()`
- `Godot.Collections.Array GetSupportedEnvironmentBlendModes()`
- `Godot.Collections.Dictionary GetSystemInfo()`
- `TrackingStatus GetTrackingStatus()`
- `Transform3D GetTransformForView(int view, Transform3D camTransform)`
- `int GetViewCount()`
- `bool Initialize()`
- `bool IsInitialized()`
- `bool IsPassthroughEnabled()`
- `bool IsPassthroughSupported()`
- `bool SetEnvironmentBlendMode(EnvironmentBlendMode mode)`
- `bool SetPlayAreaMode(PlayAreaMode mode)`
- `bool StartPassthrough()`
- `void StopPassthrough()`
- `bool SupportsPlayAreaMode(PlayAreaMode mode)`
- `void TriggerHapticPulse(string actionName, StringName trackerName, float frequency, float amplitude, float durationSec, float delaySec)`
- `void Uninitialize()`

### XRNode3D
*Inherits: **Node3D < Node < Object** | Inherited by: XRAnchor3D, XRController3D*

This node can be bound to a specific pose of an XRPositionalTracker and will automatically have its Node3D.transform updated by the XRServer. Nodes of this type must be added as children of the XROrigin3D node.

**Properties**
- `PhysicsInterpolationMode PhysicsInterpolationMode` = `2 (overrides Node)`
- `StringName Pose` = `&"default"`
- `bool ShowWhenTracked` = `false`
- `StringName Tracker` = `&""`

**Methods**
- `bool GetHasTrackingData()`
- `bool GetIsActive()`
- `XRPose GetPose()`
- `void TriggerHapticPulse(string actionName, float frequency, float amplitude, float durationSec, float delaySec)`

### XROrigin3D
*Inherits: **Node3D < Node < Object***

This is a special node within the AR/VR system that maps the physical location of the center of our tracking space to the virtual location within our game world.

**Properties**
- `bool Current` = `false`
- `float WorldScale` = `1.0`

### XRPose
*Inherits: **RefCounted < Object***

XR runtimes often identify multiple locations on devices such as controllers that are spatially tracked.

**Properties**
- `Vector3 AngularVelocity` = `Vector3(0, 0, 0)`
- `bool HasTrackingData` = `false`
- `Vector3 LinearVelocity` = `Vector3(0, 0, 0)`
- `TrackingConfidence TrackingConfidence` = `0`
- `Transform3D Transform` = `Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0)`

**Methods**
- `Transform3D GetAdjustedTransform()`

### XRPositionalTracker
*Inherits: **XRTracker < RefCounted < Object** | Inherited by: OpenXRSpatialEntityTracker, XRBodyTracker, XRControllerTracker, XRHandTracker*

An instance of this object represents a device that is tracked, such as a controller or anchor point. HMDs aren't represented here as they are handled internally.

**Properties**
- `TrackerHand Hand` = `0`
- `string Profile` = `""`

**Methods**
- `Variant GetInput(StringName name)`
- `XRPose GetPose(StringName name)`
- `bool HasPose(StringName name)`
- `void InvalidatePose(StringName name)`
- `void SetInput(StringName name, Variant value)`
- `void SetPose(StringName name, Transform3D transform, Vector3 linearVelocity, Vector3 angularVelocity, TrackingConfidence trackingConfidence)`

### XRServer
*Inherits: **Object***

The AR/VR server is the heart of our Advanced and Virtual Reality solution and handles all the processing.

**Properties**
- `bool CameraLockedToOrigin` = `false`
- `XRInterface PrimaryInterface`
- `Transform3D WorldOrigin` = `Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0)`
- `float WorldScale` = `1.0`

**Methods**
- `void AddInterface(XRInterface interface)`
- `void AddTracker(XRTracker tracker)`
- `void CenterOnHmd(RotationMode rotationMode, bool keepHeight)`
- `void ClearReferenceFrame()`
- `XRInterface FindInterface(string name)`
- `Transform3D GetHmdTransform()`
- `XRInterface GetInterface(int idx)`
- `int GetInterfaceCount()`
- `Array[Dictionary] GetInterfaces()`
- `Transform3D GetReferenceFrame()`
- `XRTracker GetTracker(StringName trackerName)`
- `Godot.Collections.Dictionary GetTrackers(int trackerTypes)`
- `void RemoveInterface(XRInterface interface)`
- `void RemoveTracker(XRTracker tracker)`

### XRTracker
*Inherits: **RefCounted < Object** | Inherited by: XRFaceTracker, XRPositionalTracker*

This object is the base of all XR trackers.

**Properties**
- `string Description` = `""`
- `TrackerType Type` = `128`

### XRVRS
*Inherits: **Object***

This class is used by various XR interfaces to generate VRS textures that can be used to speed up rendering.

**Properties**
- `float VrsMinRadius` = `20.0`
- `Rect2i VrsRenderRegion` = `Rect2i(0, 0, 0, 0)`
- `float VrsStrength` = `1.0`

**Methods**
- `RID MakeVrsTexture(Vector2 targetSize, PackedVector2Array eyeFoci)`

### bool

The bool is a built-in Variant type that may only store one of two values: true or false. You can imagine it as a switch that can be either turned on or off, or as a binary digit that can either be 1 or 0.

**C# Examples**
```csharp
bool canShoot = true;
if (canShoot)
{
    LaunchBullet();
}
```
```csharp
if (bullets > 0 && !IsReloading())
{
    LaunchBullet();
}

if (bullets == 0 || IsReloading())
{
    PlayClackSound();
}
```

### float

The float built-in type is a 64-bit double-precision floating-point number, equivalent to double in C++. This type has 14 reliable decimal digits of precision. The maximum value of float is approximately 1.79769e308, and the minimum is approximately -1.79769e308.

### int

Signed 64-bit integer type. This means that it can take values from -2^63 to 2^63 - 1, i.e. from -9223372036854775808 to 9223372036854775807. When it exceeds these bounds, it will wrap around.

**C# Examples**
```csharp
int x = 1; // x is 1
x = (int)4.2; // x is 4, because 4.2 gets truncated
// We use long below, because GDScript's int is 64-bit while C#'s int is 32-bit.
long maxLong = 9223372036854775807; // Biggest value a long can store
maxLong++; // maxLong is now -9223372036854775808, because it wrapped around.

// Alternatively with C#'s 32-bit int type, which has a smaller maximum value.
int maxInt = 2147483647; // Biggest value an int can store
maxInt++; // maxInt is now -2147483648, because it wrapped around
```
```csharp
int x = 0b1001; // x is 9
int y = 0xF5; // y is 245
int z = 10_000_000; // z is 10000000
```
