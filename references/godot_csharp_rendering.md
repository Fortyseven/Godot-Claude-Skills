# Godot 4 C# API Reference — Rendering

> C#-only reference. 148 classes.

### ArrayMesh
*Inherits: **Mesh < Resource < RefCounted < Object***

The ArrayMesh is used to construct a Mesh by specifying the attributes as arrays.

**Properties**
- `BlendShapeMode BlendShapeMode` = `1`
- `AABB CustomAabb` = `AABB(0, 0, 0, 0, 0, 0)`
- `ArrayMesh ShadowMesh`

**Methods**
- `void AddBlendShape(StringName name)`
- `void AddSurfaceFromArrays(PrimitiveType primitive, Godot.Collections.Array arrays, Array[Array] blendShapes = [], Godot.Collections.Dictionary lods = {}, BitField[ArrayFormat] flags = 0)`
- `void ClearBlendShapes()`
- `void ClearSurfaces()`
- `int GetBlendShapeCount()`
- `StringName GetBlendShapeName(int index)`
- `Error LightmapUnwrap(Transform3D transform, float texelSize)`
- `void RegenNormalMaps()`
- `void SetBlendShapeName(int index, StringName name)`
- `int SurfaceFindByName(string name)`
- `int SurfaceGetArrayIndexLen(int surfIdx)`
- `int SurfaceGetArrayLen(int surfIdx)`
- `BitField[ArrayFormat] SurfaceGetFormat(int surfIdx)`
- `string SurfaceGetName(int surfIdx)`
- `PrimitiveType SurfaceGetPrimitiveType(int surfIdx)`
- `void SurfaceRemove(int surfIdx)`
- `void SurfaceSetName(int surfIdx, string name)`
- `void SurfaceUpdateAttributeRegion(int surfIdx, int offset, PackedByteArray data)`
- `void SurfaceUpdateSkinRegion(int surfIdx, int offset, PackedByteArray data)`
- `void SurfaceUpdateVertexRegion(int surfIdx, int offset, PackedByteArray data)`

**C# Examples**
```csharp
Vector3[] vertices =
[
    new Vector3(0, 1, 0),
    new Vector3(1, 0, 0),
    new Vector3(0, 0, 1),
];

// Initialize the ArrayMesh.
var arrMesh = new ArrayMesh();
Godot.Collections.Array arrays = [];
arrays.Resize((int)Mesh.ArrayType.Max);
arrays[(int)Mesh.ArrayType.Vertex] = vertices;

// Create the Mesh.
arrMesh.AddSurfaceFromArrays(Mesh.PrimitiveType.Triangles, arrays);
var m = new MeshInstance3D();
m.Mesh = arrMesh;
```

### BaseMaterial3D
*Inherits: **Material < Resource < RefCounted < Object** | Inherited by: ORMMaterial3D, StandardMaterial3D*

This class serves as a default material with a wide variety of rendering features and properties without the need to write shader code. See the tutorial below for details.

**Properties**
- `Color AlbedoColor` = `Color(1, 1, 1, 1)`
- `Texture2D AlbedoTexture`
- `bool AlbedoTextureForceSrgb` = `false`
- `bool AlbedoTextureMsdf` = `false`
- `float AlphaAntialiasingEdge`
- `AlphaAntiAliasing AlphaAntialiasingMode`
- `float AlphaHashScale`
- `float AlphaScissorThreshold`
- `float Anisotropy` = `0.0`
- `bool AnisotropyEnabled` = `false`
- `Texture2D AnisotropyFlowmap`
- `bool AoEnabled` = `false`
- `float AoLightAffect` = `0.0`
- `bool AoOnUv2` = `false`
- `Texture2D AoTexture`
- `TextureChannel AoTextureChannel` = `0`
- `Color Backlight` = `Color(0, 0, 0, 1)`
- `bool BacklightEnabled` = `false`
- `Texture2D BacklightTexture`
- `bool BentNormalEnabled` = `false`
- `Texture2D BentNormalTexture`
- `bool BillboardKeepScale` = `false`
- `BillboardMode BillboardMode` = `0`
- `BlendMode BlendMode` = `0`
- `float Clearcoat` = `1.0`
- `bool ClearcoatEnabled` = `false`
- `float ClearcoatRoughness` = `0.5`
- `Texture2D ClearcoatTexture`
- `CullMode CullMode` = `0`
- `DepthDrawMode DepthDrawMode` = `0`

**Methods**
- `bool GetFeature(Feature feature)`
- `bool GetFlag(Flags flag)`
- `Texture2D GetTexture(TextureParam param)`
- `void SetFeature(Feature feature, bool enable)`
- `void SetFlag(Flags flag, bool enable)`
- `void SetTexture(TextureParam param, Texture2D texture)`

### BoxMesh
*Inherits: **PrimitiveMesh < Mesh < Resource < RefCounted < Object***

Generate an axis-aligned box PrimitiveMesh.

**Properties**
- `Vector3 Size` = `Vector3(1, 1, 1)`
- `int SubdivideDepth` = `0`
- `int SubdivideHeight` = `0`
- `int SubdivideWidth` = `0`

### CameraAttributesPhysical
*Inherits: **CameraAttributes < Resource < RefCounted < Object***

CameraAttributesPhysical is used to set rendering settings based on a physically-based camera's settings. It is responsible for exposure, auto-exposure, and depth of field.

**Properties**
- `float AutoExposureMaxExposureValue` = `10.0`
- `float AutoExposureMinExposureValue` = `-8.0`
- `float ExposureAperture` = `16.0`
- `float ExposureShutterSpeed` = `100.0`
- `float FrustumFar` = `4000.0`
- `float FrustumFocalLength` = `35.0`
- `float FrustumFocusDistance` = `10.0`
- `float FrustumNear` = `0.05`

**Methods**
- `float GetFov()`

### CameraAttributesPractical
*Inherits: **CameraAttributes < Resource < RefCounted < Object***

Controls camera-specific attributes such as auto-exposure, depth of field, and exposure override.

**Properties**
- `float AutoExposureMaxSensitivity` = `800.0`
- `float AutoExposureMinSensitivity` = `0.0`
- `float DofBlurAmount` = `0.1`
- `float DofBlurFarDistance` = `10.0`
- `bool DofBlurFarEnabled` = `false`
- `float DofBlurFarTransition` = `5.0`
- `float DofBlurNearDistance` = `2.0`
- `bool DofBlurNearEnabled` = `false`
- `float DofBlurNearTransition` = `1.0`

### CameraAttributes
*Inherits: **Resource < RefCounted < Object** | Inherited by: CameraAttributesPhysical, CameraAttributesPractical*

Controls camera-specific attributes such as depth of field and exposure override.

**Properties**
- `bool AutoExposureEnabled` = `false`
- `float AutoExposureScale` = `0.4`
- `float AutoExposureSpeed` = `0.5`
- `float ExposureMultiplier` = `1.0`
- `float ExposureSensitivity` = `100.0`

### CapsuleMesh
*Inherits: **PrimitiveMesh < Mesh < Resource < RefCounted < Object***

Class representing a capsule-shaped PrimitiveMesh.

**Properties**
- `float Height` = `2.0`
- `int RadialSegments` = `64`
- `float Radius` = `0.5`
- `int Rings` = `8`

### CompositorEffect
*Inherits: **Resource < RefCounted < Object***

This resource defines a custom rendering effect that can be applied to Viewports through the viewports' Environment. You can implement a callback that is called during rendering at a given stage of the rendering pipeline and allows you to insert additional passes. Note that this callback happens on the rendering thread. CompositorEffect is an abstract base class and must be extended to implement specific rendering logic.

**Properties**
- `bool AccessResolvedColor`
- `bool AccessResolvedDepth`
- `EffectCallbackType EffectCallbackType`
- `bool Enabled`
- `bool NeedsMotionVectors`
- `bool NeedsNormalRoughness`
- `bool NeedsSeparateSpecular`

**Methods**
- `void _RenderCallback(int effectCallbackType, RenderData renderData) [virtual]`

### Compositor
*Inherits: **Resource < RefCounted < Object***

The compositor resource stores attributes used to customize how a Viewport is rendered.

**Properties**
- `Array[CompositorEffect] CompositorEffects` = `[]`

### CylinderMesh
*Inherits: **PrimitiveMesh < Mesh < Resource < RefCounted < Object***

Class representing a cylindrical PrimitiveMesh. This class can be used to create cones by setting either the top_radius or bottom_radius properties to 0.0.

**Properties**
- `float BottomRadius` = `0.5`
- `bool CapBottom` = `true`
- `bool CapTop` = `true`
- `float Height` = `2.0`
- `int RadialSegments` = `64`
- `int Rings` = `4`
- `float TopRadius` = `0.5`

### Environment
*Inherits: **Resource < RefCounted < Object***

Resource for environment nodes (like WorldEnvironment) that define multiple environment operations (such as background Sky or Color, ambient light, fog, depth-of-field...). These parameters affect the final render of the scene. The order of these operations is:

**Properties**
- `float AdjustmentBrightness` = `1.0`
- `Texture AdjustmentColorCorrection`
- `float AdjustmentContrast` = `1.0`
- `bool AdjustmentEnabled` = `false`
- `float AdjustmentSaturation` = `1.0`
- `Color AmbientLightColor` = `Color(0, 0, 0, 1)`
- `float AmbientLightEnergy` = `1.0`
- `float AmbientLightSkyContribution` = `1.0`
- `AmbientSource AmbientLightSource` = `0`
- `int BackgroundCameraFeedId` = `1`
- `int BackgroundCanvasMaxLayer` = `0`
- `Color BackgroundColor` = `Color(0, 0, 0, 1)`
- `float BackgroundEnergyMultiplier` = `1.0`
- `float BackgroundIntensity` = `30000.0`
- `BGMode BackgroundMode` = `0`
- `float FogAerialPerspective` = `0.0`
- `float FogDensity` = `0.01`
- `float FogDepthBegin` = `10.0`
- `float FogDepthCurve` = `1.0`
- `float FogDepthEnd` = `100.0`
- `bool FogEnabled` = `false`
- `float FogHeight` = `0.0`
- `float FogHeightDensity` = `0.0`
- `Color FogLightColor` = `Color(0.518, 0.553, 0.608, 1)`
- `float FogLightEnergy` = `1.0`
- `FogMode FogMode` = `0`
- `float FogSkyAffect` = `1.0`
- `float FogSunScatter` = `0.0`
- `GlowBlendMode GlowBlendMode` = `1`
- `float GlowBloom` = `0.0`

**Methods**
- `float GetGlowLevel(int idx)`
- `void SetGlowLevel(int idx, float intensity)`

### ImmediateMesh
*Inherits: **Mesh < Resource < RefCounted < Object***

A mesh type optimized for creating geometry manually, similar to OpenGL 1.x immediate mode.

**Methods**
- `void ClearSurfaces()`
- `void SurfaceAddVertex(Vector3 vertex)`
- `void SurfaceAddVertex2d(Vector2 vertex)`
- `void SurfaceBegin(PrimitiveType primitive, Material material = null)`
- `void SurfaceEnd()`
- `void SurfaceSetColor(Color color)`
- `void SurfaceSetNormal(Vector3 normal)`
- `void SurfaceSetTangent(Plane tangent)`
- `void SurfaceSetUv(Vector2 uv)`
- `void SurfaceSetUv2(Vector2 uv2)`

**C# Examples**
```csharp
var mesh = new ImmediateMesh();
mesh.SurfaceBegin(Mesh.PrimitiveType.Triangles);
mesh.SurfaceAddVertex(Vector3.Left);
mesh.SurfaceAddVertex(Vector3.Forward);
mesh.SurfaceAddVertex(Vector3.Zero);
mesh.SurfaceEnd();
```

### Material
*Inherits: **Resource < RefCounted < Object** | Inherited by: BaseMaterial3D, CanvasItemMaterial, FogMaterial, PanoramaSkyMaterial, ParticleProcessMaterial, PhysicalSkyMaterial, ...*

Material is a base resource used for coloring and shading geometry. All materials inherit from it and almost all VisualInstance3D derived nodes carry a Material. A few flags and parameters are shared between all material types and are configured here.

**Properties**
- `Material NextPass`
- `int RenderPriority`

**Methods**
- `bool _CanDoNextPass() [virtual]`
- `bool _CanUseRenderPriority() [virtual]`
- `Mode _GetShaderMode() [virtual]`
- `RID _GetShaderRid() [virtual]`
- `Resource CreatePlaceholder()`
- `void InspectNativeShaderCode()`

### MeshDataTool
*Inherits: **RefCounted < Object***

MeshDataTool provides access to individual vertices in a Mesh. It allows users to read and edit vertex data of meshes. It also creates an array of faces and edges.

**Methods**
- `void Clear()`
- `Error CommitToSurface(ArrayMesh mesh, int compressionFlags = 0)`
- `Error CreateFromSurface(ArrayMesh mesh, int surface)`
- `int GetEdgeCount()`
- `PackedInt32Array GetEdgeFaces(int idx)`
- `Variant GetEdgeMeta(int idx)`
- `int GetEdgeVertex(int idx, int vertex)`
- `int GetFaceCount()`
- `int GetFaceEdge(int idx, int edge)`
- `Variant GetFaceMeta(int idx)`
- `Vector3 GetFaceNormal(int idx)`
- `int GetFaceVertex(int idx, int vertex)`
- `int GetFormat()`
- `Material GetMaterial()`
- `Vector3 GetVertex(int idx)`
- `PackedInt32Array GetVertexBones(int idx)`
- `Color GetVertexColor(int idx)`
- `int GetVertexCount()`
- `PackedInt32Array GetVertexEdges(int idx)`
- `PackedInt32Array GetVertexFaces(int idx)`
- `Variant GetVertexMeta(int idx)`
- `Vector3 GetVertexNormal(int idx)`
- `Plane GetVertexTangent(int idx)`
- `Vector2 GetVertexUv(int idx)`
- `Vector2 GetVertexUv2(int idx)`
- `PackedFloat32Array GetVertexWeights(int idx)`
- `void SetEdgeMeta(int idx, Variant meta)`
- `void SetFaceMeta(int idx, Variant meta)`
- `void SetMaterial(Material material)`
- `void SetVertex(int idx, Vector3 vertex)`
- `void SetVertexBones(int idx, PackedInt32Array bones)`
- `void SetVertexColor(int idx, Color color)`
- `void SetVertexMeta(int idx, Variant meta)`
- `void SetVertexNormal(int idx, Vector3 normal)`
- `void SetVertexTangent(int idx, Plane tangent)`
- `void SetVertexUv(int idx, Vector2 uv)`
- `void SetVertexUv2(int idx, Vector2 uv2)`
- `void SetVertexWeights(int idx, PackedFloat32Array weights)`

**C# Examples**
```csharp
var mesh = new ArrayMesh();
mesh.AddSurfaceFromArrays(Mesh.PrimitiveType.Triangles, new BoxMesh().GetMeshArrays());
var mdt = new MeshDataTool();
mdt.CreateFromSurface(mesh, 0);
for (var i = 0; i < mdt.GetVertexCount(); i++)
{
    Vector3 vertex = mdt.GetVertex(i);
    // In this example we extend the mesh by one unit, which results in separated faces as it is flat shaded.
    vertex += mdt.GetVertexNormal(i);
    // Save your change.
    mdt.SetVertex(i, vertex);
}
mesh.ClearSurfaces();
mdt.CommitToSurface(mesh);
var mi = new MeshInstance();
mi.Mesh = mesh;
AddChild(mi);
```
```csharp
int index = meshDataTool.GetFaceVertex(0, 1); // Gets the index of the second vertex of the first face.
Vector3 position = meshDataTool.GetVertex(index);
Vector3 normal = meshDataTool.GetVertexNormal(index);
```

### MultiMesh
*Inherits: **Resource < RefCounted < Object***

MultiMesh provides low-level mesh instancing. Drawing thousands of MeshInstance3D nodes can be slow, since each object is submitted to the GPU then drawn individually.

**Properties**
- `PackedFloat32Array Buffer` = `PackedFloat32Array()`
- `PackedColorArray ColorArray`
- `AABB CustomAabb` = `AABB(0, 0, 0, 0, 0, 0)`
- `PackedColorArray CustomDataArray`
- `int InstanceCount` = `0`
- `Mesh Mesh`
- `PhysicsInterpolationQuality PhysicsInterpolationQuality` = `0`
- `PackedVector2Array Transform2dArray`
- `PackedVector3Array TransformArray`
- `TransformFormat TransformFormat` = `0`
- `bool UseColors` = `false`
- `bool UseCustomData` = `false`
- `int VisibleInstanceCount` = `-1`

**Methods**
- `AABB GetAabb()`
- `Color GetInstanceColor(int instance)`
- `Color GetInstanceCustomData(int instance)`
- `Transform3D GetInstanceTransform(int instance)`
- `Transform2D GetInstanceTransform2d(int instance)`
- `void ResetInstancePhysicsInterpolation(int instance)`
- `void ResetInstancesPhysicsInterpolation()`
- `void SetBufferInterpolated(PackedFloat32Array bufferCurr, PackedFloat32Array bufferPrev)`
- `void SetInstanceColor(int instance, Color color)`
- `void SetInstanceCustomData(int instance, Color customData)`
- `void SetInstanceTransform(int instance, Transform3D transform)`
- `void SetInstanceTransform2d(int instance, Transform2D transform)`

### ORMMaterial3D
*Inherits: **BaseMaterial3D < Material < Resource < RefCounted < Object***

ORMMaterial3D's properties are inherited from BaseMaterial3D. Unlike StandardMaterial3D, ORMMaterial3D uses a single texture for ambient occlusion, roughness and metallic maps, known as an ORM texture.

### ParticleProcessMaterial
*Inherits: **Material < Resource < RefCounted < Object***

ParticleProcessMaterial defines particle properties and behavior. It is used in the process_material of the GPUParticles2D and GPUParticles3D nodes. Some of this material's properties are applied to each particle when emitted, while others can have a CurveTexture or a GradientTexture1D applied to vary numerical or color values over the lifetime of the particle.

**Properties**
- `Texture2D AlphaCurve`
- `Texture2D AngleCurve`
- `float AngleMax` = `0.0`
- `float AngleMin` = `0.0`
- `Texture2D AngularVelocityCurve`
- `float AngularVelocityMax` = `0.0`
- `float AngularVelocityMin` = `0.0`
- `Texture2D AnimOffsetCurve`
- `float AnimOffsetMax` = `0.0`
- `float AnimOffsetMin` = `0.0`
- `Texture2D AnimSpeedCurve`
- `float AnimSpeedMax` = `0.0`
- `float AnimSpeedMin` = `0.0`
- `bool AttractorInteractionEnabled` = `true`
- `float CollisionBounce`
- `float CollisionFriction`
- `CollisionMode CollisionMode` = `0`
- `bool CollisionUseScale` = `false`
- `Color Color` = `Color(1, 1, 1, 1)`
- `Texture2D ColorInitialRamp`
- `Texture2D ColorRamp`
- `Texture2D DampingCurve`
- `float DampingMax` = `0.0`
- `float DampingMin` = `0.0`
- `Vector3 Direction` = `Vector3(1, 0, 0)`
- `Texture2D DirectionalVelocityCurve`
- `float DirectionalVelocityMax`
- `float DirectionalVelocityMin`
- `Vector3 EmissionBoxExtents`
- `Texture2D EmissionColorTexture`

**Methods**
- `Vector2 GetParam(Parameter param)`
- `float GetParamMax(Parameter param)`
- `float GetParamMin(Parameter param)`
- `Texture2D GetParamTexture(Parameter param)`
- `bool GetParticleFlag(ParticleFlags particleFlag)`
- `void SetParam(Parameter param, Vector2 value)`
- `void SetParamMax(Parameter param, float value)`
- `void SetParamMin(Parameter param, float value)`
- `void SetParamTexture(Parameter param, Texture2D texture)`
- `void SetParticleFlag(ParticleFlags particleFlag, bool enable)`

### PlaneMesh
*Inherits: **PrimitiveMesh < Mesh < Resource < RefCounted < Object** | Inherited by: QuadMesh*

Class representing a planar PrimitiveMesh. This flat mesh does not have a thickness. By default, this mesh is aligned on the X and Z axes; this default rotation isn't suited for use with billboarded materials. For billboarded materials, change orientation to FACE_Z.

**Properties**
- `Vector3 CenterOffset` = `Vector3(0, 0, 0)`
- `Orientation Orientation` = `1`
- `Vector2 Size` = `Vector2(2, 2)`
- `int SubdivideDepth` = `0`
- `int SubdivideWidth` = `0`

### PrimitiveMesh
*Inherits: **Mesh < Resource < RefCounted < Object** | Inherited by: BoxMesh, CapsuleMesh, CylinderMesh, PlaneMesh, PointMesh, PrismMesh, ...*

Base class for all primitive meshes. Handles applying a Material to a primitive mesh. Examples include BoxMesh, CapsuleMesh, CylinderMesh, PlaneMesh, PrismMesh, and SphereMesh.

**Properties**
- `bool AddUv2` = `false`
- `AABB CustomAabb` = `AABB(0, 0, 0, 0, 0, 0)`
- `bool FlipFaces` = `false`
- `Material Material`
- `float Uv2Padding` = `2.0`

**Methods**
- `Godot.Collections.Array _CreateMeshArray() [virtual]`
- `Godot.Collections.Array GetMeshArrays()`
- `void RequestUpdate()`

**C# Examples**
```csharp
var c = new CylinderMesh();
var arrMesh = new ArrayMesh();
arrMesh.AddSurfaceFromArrays(Mesh.PrimitiveType.Triangles, c.GetMeshArrays());
```

### QuadMesh
*Inherits: **PlaneMesh < PrimitiveMesh < Mesh < Resource < RefCounted < Object***

Class representing a square PrimitiveMesh. This flat mesh does not have a thickness. By default, this mesh is aligned on the X and Y axes; this rotation is more suited for use with billboarded materials. A QuadMesh is equivalent to a PlaneMesh except its default PlaneMesh.orientation is PlaneMesh.FACE_Z.

**Properties**
- `Orientation Orientation` = `2 (overrides PlaneMesh)`
- `Vector2 Size` = `Vector2(1, 1) (overrides PlaneMesh)`

### RDShaderFile
*Inherits: **Resource < RefCounted < Object***

Compiled shader file in SPIR-V form.

**Properties**
- `string BaseError` = `""`

**Methods**
- `RDShaderSPIRV GetSpirv(StringName version = &"")`
- `Array[StringName] GetVersionList()`
- `void SetBytecode(RDShaderSPIRV bytecode, StringName version = &"")`

### RenderingDevice
*Inherits: **Object***

RenderingDevice is an abstraction for working with modern low-level graphics APIs such as Vulkan. Compared to RenderingServer (which works with Godot's own rendering subsystems), RenderingDevice is much lower-level and allows working more directly with the underlying graphics APIs. RenderingDevice is used in Godot to provide support for several modern low-level graphics APIs while reducing the amount of code duplication required. RenderingDevice can also be used in your own projects to perform things that are not exposed by RenderingServer or high-level nodes, such as using compute shaders.

**Methods**
- `void Barrier(BitField[BarrierMask] from = 32767, BitField[BarrierMask] to = 32767)`
- `Error BufferClear(RID buffer, int offset, int sizeBytes)`
- `Error BufferCopy(RID srcBuffer, RID dstBuffer, int srcOffset, int dstOffset, int size)`
- `PackedByteArray BufferGetData(RID buffer, int offsetBytes = 0, int sizeBytes = 0)`
- `Error BufferGetDataAsync(RID buffer, Callable callback, int offsetBytes = 0, int sizeBytes = 0)`
- `int BufferGetDeviceAddress(RID buffer)`
- `Error BufferUpdate(RID buffer, int offset, int sizeBytes, PackedByteArray data)`
- `void CaptureTimestamp(string name)`
- `void ComputeListAddBarrier(int computeList)`
- `int ComputeListBegin()`
- `void ComputeListBindComputePipeline(int computeList, RID computePipeline)`
- `void ComputeListBindUniformSet(int computeList, RID uniformSet, int setIndex)`
- `void ComputeListDispatch(int computeList, int xGroups, int yGroups, int zGroups)`
- `void ComputeListDispatchIndirect(int computeList, RID buffer, int offset)`
- `void ComputeListEnd()`
- `void ComputeListSetPushConstant(int computeList, PackedByteArray buffer, int sizeBytes)`
- `RID ComputePipelineCreate(RID shader, Array[RDPipelineSpecializationConstant] specializationConstants = [])`
- `bool ComputePipelineIsValid(RID computePipeline)`
- `RenderingDevice CreateLocalDevice()`
- `void DrawCommandBeginLabel(string name, Color color)`
- `void DrawCommandEndLabel()`
- `void DrawCommandInsertLabel(string name, Color color)`
- `int DrawListBegin(RID framebuffer, BitField[DrawFlags] drawFlags = 0, PackedColorArray clearColorValues = PackedColorArray(), float clearDepthValue = 1.0, int clearStencilValue = 0, Rect2 region = Rect2(0, 0, 0, 0), int breadcrumb = 0)`
- `int DrawListBeginForScreen(int screen = 0, Color clearColor = Color(0, 0, 0, 1))`
- `PackedInt64Array DrawListBeginSplit(RID framebuffer, int splits, InitialAction initialColorAction, FinalAction finalColorAction, InitialAction initialDepthAction, FinalAction finalDepthAction, PackedColorArray clearColorValues = PackedColorArray(), float clearDepth = 1.0, int clearStencil = 0, Rect2 region = Rect2(0, 0, 0, 0), Array[RID] storageTextures = [])`
- `void DrawListBindIndexArray(int drawList, RID indexArray)`
- `void DrawListBindRenderPipeline(int drawList, RID renderPipeline)`
- `void DrawListBindUniformSet(int drawList, RID uniformSet, int setIndex)`
- `void DrawListBindVertexArray(int drawList, RID vertexArray)`
- `void DrawListBindVertexBuffersFormat(int drawList, int vertexFormat, int vertexCount, Array[RID] vertexBuffers, PackedInt64Array offsets = PackedInt64Array())`
- `void DrawListDisableScissor(int drawList)`
- `void DrawListDraw(int drawList, bool useIndices, int instances, int proceduralVertexCount = 0)`
- `void DrawListDrawIndirect(int drawList, bool useIndices, RID buffer, int offset = 0, int drawCount = 1, int stride = 0)`
- `void DrawListEnableScissor(int drawList, Rect2 rect = Rect2(0, 0, 0, 0))`
- `void DrawListEnd()`
- `void DrawListSetBlendConstants(int drawList, Color color)`
- `void DrawListSetPushConstant(int drawList, PackedByteArray buffer, int sizeBytes)`
- `int DrawListSwitchToNextPass()`
- `PackedInt64Array DrawListSwitchToNextPassSplit(int splits)`
- `RID FramebufferCreate(Array[RID] textures, int validateWithFormat = -1, int viewCount = 1)`

### RenderingServer
*Inherits: **Object***

The rendering server is the API backend for everything visible. The whole scene system mounts on it to display. The rendering server is completely opaque: the internals are entirely implementation-specific and cannot be accessed.

**Properties**
- `bool RenderLoopEnabled`

**Methods**
- `Array[Image] BakeRenderUv2(RID base, Array[RID] materialOverrides, Vector2i imageSize)`
- `void CallOnRenderThread(Callable callable)`
- `RID CameraAttributesCreate()`
- `void CameraAttributesSetAutoExposure(RID cameraAttributes, bool enable, float minSensitivity, float maxSensitivity, float speed, float scale)`
- `void CameraAttributesSetDofBlur(RID cameraAttributes, bool farEnable, float farDistance, float farTransition, bool nearEnable, float nearDistance, float nearTransition, float amount)`
- `void CameraAttributesSetDofBlurBokehShape(DOFBokehShape shape)`
- `void CameraAttributesSetDofBlurQuality(DOFBlurQuality quality, bool useJitter)`
- `void CameraAttributesSetExposure(RID cameraAttributes, float multiplier, float normalization)`
- `RID CameraCreate()`
- `void CameraSetCameraAttributes(RID camera, RID effects)`
- `void CameraSetCompositor(RID camera, RID compositor)`
- `void CameraSetCullMask(RID camera, int layers)`
- `void CameraSetEnvironment(RID camera, RID env)`
- `void CameraSetFrustum(RID camera, float size, Vector2 offset, float zNear, float zFar)`
- `void CameraSetOrthogonal(RID camera, float size, float zNear, float zFar)`
- `void CameraSetPerspective(RID camera, float fovyDegrees, float zNear, float zFar)`
- `void CameraSetTransform(RID camera, Transform3D transform)`
- `void CameraSetUseVerticalAspect(RID camera, bool enable)`
- `RID CanvasCreate()`
- `void CanvasItemAddAnimationSlice(RID item, float animationLength, float sliceBegin, float sliceEnd, float offset = 0.0)`
- `void CanvasItemAddCircle(RID item, Vector2 pos, float radius, Color color, bool antialiased = false)`
- `void CanvasItemAddClipIgnore(RID item, bool ignore)`
- `void CanvasItemAddEllipse(RID item, Vector2 pos, float major, float minor, Color color, bool antialiased = false)`
- `void CanvasItemAddLcdTextureRectRegion(RID item, Rect2 rect, RID texture, Rect2 srcRect, Color modulate)`
- `void CanvasItemAddLine(RID item, Vector2 from, Vector2 to, Color color, float width = -1.0, bool antialiased = false)`
- `void CanvasItemAddMesh(RID item, RID mesh, Transform2D transform = Transform2D(1, 0, 0, 1, 0, 0), Color modulate = Color(1, 1, 1, 1), RID texture = RID())`
- `void CanvasItemAddMsdfTextureRectRegion(RID item, Rect2 rect, RID texture, Rect2 srcRect, Color modulate = Color(1, 1, 1, 1), int outlineSize = 0, float pxRange = 1.0, float scale = 1.0)`
- `void CanvasItemAddMultiline(RID item, PackedVector2Array points, PackedColorArray colors, float width = -1.0, bool antialiased = false)`
- `void CanvasItemAddMultimesh(RID item, RID mesh, RID texture = RID())`
- `void CanvasItemAddNinePatch(RID item, Rect2 rect, Rect2 source, RID texture, Vector2 topleft, Vector2 bottomright, NinePatchAxisMode xAxisMode = 0, NinePatchAxisMode yAxisMode = 0, bool drawCenter = true, Color modulate = Color(1, 1, 1, 1))`
- `void CanvasItemAddParticles(RID item, RID particles, RID texture)`
- `void CanvasItemAddPolygon(RID item, PackedVector2Array points, PackedColorArray colors, PackedVector2Array uvs = PackedVector2Array(), RID texture = RID())`
- `void CanvasItemAddPolyline(RID item, PackedVector2Array points, PackedColorArray colors, float width = -1.0, bool antialiased = false)`
- `void CanvasItemAddPrimitive(RID item, PackedVector2Array points, PackedColorArray colors, PackedVector2Array uvs, RID texture)`
- `void CanvasItemAddRect(RID item, Rect2 rect, Color color, bool antialiased = false)`
- `void CanvasItemAddSetTransform(RID item, Transform2D transform)`
- `void CanvasItemAddTextureRect(RID item, Rect2 rect, RID texture, bool tile = false, Color modulate = Color(1, 1, 1, 1), bool transpose = false)`
- `void CanvasItemAddTextureRectRegion(RID item, Rect2 rect, RID texture, Rect2 srcRect, Color modulate = Color(1, 1, 1, 1), bool transpose = false, bool clipUv = true)`
- `void CanvasItemAddTriangleArray(RID item, PackedInt32Array indices, PackedVector2Array points, PackedColorArray colors, PackedVector2Array uvs = PackedVector2Array(), PackedInt32Array bones = PackedInt32Array(), PackedFloat32Array weights = PackedFloat32Array(), RID texture = RID(), int count = -1)`
- `void CanvasItemAttachSkeleton(RID item, RID skeleton)`

### RibbonTrailMesh
*Inherits: **PrimitiveMesh < Mesh < Resource < RefCounted < Object***

RibbonTrailMesh represents a straight ribbon-shaped mesh with variable width. The ribbon is composed of a number of flat or cross-shaped sections, each with the same section_length and number of section_segments. A curve is sampled along the total length of the ribbon, meaning that the curve determines the size of the ribbon along its length.

**Properties**
- `Curve Curve`
- `float SectionLength` = `0.2`
- `int SectionSegments` = `3`
- `int Sections` = `5`
- `Shape Shape` = `1`
- `float Size` = `1.0`

### ShaderGlobalsOverride
*Inherits: **Node < Object***

Similar to how a WorldEnvironment node can be used to override the environment while a specific scene is loaded, ShaderGlobalsOverride can be used to override global shader parameters temporarily. Once the node is removed, the project-wide values for the global shader parameters are restored. See the RenderingServer global_shader_parameter_* methods for more information.

### ShaderIncludeDB
*Inherits: **Object***

This object contains shader fragments from Godot's internal shaders. These can be used when access to internal uniform buffers and/or internal functions is required for instance when composing compositor effects or compute shaders. Only fragments for the current rendering device are loaded.

**Methods**
- `string GetBuiltInIncludeFile(string filename) [static]`
- `bool HasBuiltInIncludeFile(string filename) [static]`
- `PackedStringArray ListBuiltInIncludeFiles() [static]`

### ShaderInclude
*Inherits: **Resource < RefCounted < Object***

A shader include file, saved with the .gdshaderinc extension. This class allows you to define a custom shader snippet that can be included in a Shader by using the preprocessor directive #include, followed by the file path (e.g. #include "res://shader_lib.gdshaderinc"). The snippet doesn't have to be a valid shader on its own.

**Properties**
- `string Code` = `""`

### ShaderMaterial
*Inherits: **Material < Resource < RefCounted < Object***

A material that uses a custom Shader program to render visual items (canvas items, meshes, skies, fog), or to process particles. Compared to other materials, ShaderMaterial gives deeper control over the generated shader code. For more information, see the shaders documentation index below.

**Properties**
- `Shader Shader`

**Methods**
- `Variant GetShaderParameter(StringName param)`
- `void SetShaderParameter(StringName param, Variant value)`

### Shader
*Inherits: **Resource < RefCounted < Object** | Inherited by: VisualShader*

A custom shader program implemented in the Godot shading language, saved with the .gdshader extension.

**Properties**
- `string Code` = `""`

**Methods**
- `Texture GetDefaultTextureParameter(StringName name, int index = 0)`
- `Mode GetMode()`
- `Godot.Collections.Array GetShaderUniformList(bool getGroups = false)`
- `void InspectNativeShaderCode()`
- `void SetDefaultTextureParameter(StringName name, Texture texture, int index = 0)`

### SphereMesh
*Inherits: **PrimitiveMesh < Mesh < Resource < RefCounted < Object***

Class representing a spherical PrimitiveMesh.

**Properties**
- `float Height` = `1.0`
- `bool IsHemisphere` = `false`
- `int RadialSegments` = `64`
- `float Radius` = `0.5`
- `int Rings` = `32`

### StandardMaterial3D
*Inherits: **BaseMaterial3D < Material < Resource < RefCounted < Object***

StandardMaterial3D's properties are inherited from BaseMaterial3D. StandardMaterial3D uses separate textures for ambient occlusion, roughness and metallic maps. To use a single ORM map for all 3 textures, use an ORMMaterial3D instead.

### SubViewport
*Inherits: **Viewport < Node < Object***

SubViewport Isolates a rectangular region of a scene to be displayed independently. This can be used, for example, to display UI in 3D space.

**Properties**
- `ClearMode RenderTargetClearMode` = `0`
- `UpdateMode RenderTargetUpdateMode` = `2`
- `Vector2i Size` = `Vector2i(512, 512)`
- `Vector2i Size2dOverride` = `Vector2i(0, 0)`
- `bool Size2dOverrideStretch` = `false`

### SurfaceTool
*Inherits: **RefCounted < Object***

The SurfaceTool is used to construct a Mesh by specifying vertex attributes individually. It can be used to construct a Mesh from a script. All properties except indices need to be added before calling add_vertex(). For example, to add vertex colors and UVs:

**Methods**
- `void AddIndex(int index)`
- `void AddTriangleFan(PackedVector3Array vertices, PackedVector2Array uvs = PackedVector2Array(), PackedColorArray colors = PackedColorArray(), PackedVector2Array uv2s = PackedVector2Array(), PackedVector3Array normals = PackedVector3Array(), Array[Plane] tangents = [])`
- `void AddVertex(Vector3 vertex)`
- `void AppendFrom(Mesh existing, int surface, Transform3D transform)`
- `void Begin(PrimitiveType primitive)`
- `void Clear()`
- `ArrayMesh Commit(ArrayMesh existing = null, int flags = 0)`
- `Godot.Collections.Array CommitToArrays()`
- `void CreateFrom(Mesh existing, int surface)`
- `void CreateFromArrays(Godot.Collections.Array arrays, PrimitiveType primitiveType = 3)`
- `void CreateFromBlendShape(Mesh existing, int surface, string blendShape)`
- `void Deindex()`
- `PackedInt32Array GenerateLod(float ndThreshold, int targetIndexCount = 3)`
- `void GenerateNormals(bool flip = false)`
- `void GenerateTangents()`
- `AABB GetAabb()`
- `CustomFormat GetCustomFormat(int channelIndex)`
- `PrimitiveType GetPrimitiveType()`
- `SkinWeightCount GetSkinWeightCount()`
- `void Index()`
- `void OptimizeIndicesForCache()`
- `void SetBones(PackedInt32Array bones)`
- `void SetColor(Color color)`
- `void SetCustom(int channelIndex, Color customColor)`
- `void SetCustomFormat(int channelIndex, CustomFormat format)`
- `void SetMaterial(Material material)`
- `void SetNormal(Vector3 normal)`
- `void SetSkinWeightCount(SkinWeightCount count)`
- `void SetSmoothGroup(int index)`
- `void SetTangent(Plane tangent)`
- `void SetUv(Vector2 uv)`
- `void SetUv2(Vector2 uv2)`
- `void SetWeights(PackedFloat32Array weights)`

**C# Examples**
```csharp
var st = new SurfaceTool();
st.Begin(Mesh.PrimitiveType.Triangles);
st.SetColor(new Color(1, 0, 0));
st.SetUV(new Vector2(0, 0));
st.AddVertex(new Vector3(0, 0, 0));
```

### TubeTrailMesh
*Inherits: **PrimitiveMesh < Mesh < Resource < RefCounted < Object***

TubeTrailMesh represents a straight tube-shaped mesh with variable width. The tube is composed of a number of cylindrical sections, each with the same section_length and number of section_rings. A curve is sampled along the total length of the tube, meaning that the curve determines the radius of the tube along its length.

**Properties**
- `bool CapBottom` = `true`
- `bool CapTop` = `true`
- `Curve Curve`
- `int RadialSteps` = `8`
- `float Radius` = `0.5`
- `float SectionLength` = `0.2`
- `int SectionRings` = `3`
- `int Sections` = `5`

### ViewportTexture
*Inherits: **Texture2D < Texture < Resource < RefCounted < Object***

A ViewportTexture provides the content of a Viewport as a dynamic Texture2D. This can be used to combine the rendering of Control, Node2D and Node3D nodes. For example, you can use this texture to display a 3D scene inside a TextureRect, or a 2D overlay in a Sprite3D.

**Properties**
- `NodePath ViewportPath` = `NodePath("")`

### Viewport
*Inherits: **Node < Object** | Inherited by: SubViewport, Window*

A Viewport creates a different view into the screen, or a sub-view inside another viewport. Child 2D nodes will display on it, and child Camera3D 3D nodes will render on it too.

**Properties**
- `AnisotropicFiltering AnisotropicFilteringLevel` = `2`
- `bool AudioListenerEnable2d` = `false`
- `bool AudioListenerEnable3d` = `false`
- `int CanvasCullMask` = `4294967295`
- `DefaultCanvasItemTextureFilter CanvasItemDefaultTextureFilter` = `1`
- `DefaultCanvasItemTextureRepeat CanvasItemDefaultTextureRepeat` = `0`
- `Transform2D CanvasTransform`
- `DebugDraw DebugDraw` = `0`
- `bool Disable3d` = `false`
- `float FsrSharpness` = `0.2`
- `Transform2D GlobalCanvasTransform`
- `bool GuiDisableInput` = `false`
- `int GuiDragThreshold` = `10`
- `bool GuiEmbedSubwindows` = `false`
- `bool GuiSnapControlsToPixels` = `true`
- `bool HandleInputLocally` = `true`
- `float MeshLodThreshold` = `1.0`
- `MSAA Msaa2d` = `0`
- `MSAA Msaa3d` = `0`
- `bool Oversampling` = `true`
- `float OversamplingOverride` = `0.0`
- `bool OwnWorld3d` = `false`
- `PhysicsInterpolationMode PhysicsInterpolationMode` = `1 (overrides Node)`
- `bool PhysicsObjectPicking` = `false`
- `bool PhysicsObjectPickingFirstOnly` = `false`
- `bool PhysicsObjectPickingSort` = `false`
- `bool PositionalShadowAtlas16Bits` = `true`
- `PositionalShadowAtlasQuadrantSubdiv PositionalShadowAtlasQuad0` = `2`
- `PositionalShadowAtlasQuadrantSubdiv PositionalShadowAtlasQuad1` = `2`
- `PositionalShadowAtlasQuadrantSubdiv PositionalShadowAtlasQuad2` = `3`

**Methods**
- `World2D FindWorld2d()`
- `World3D FindWorld3d()`
- `AudioListener2D GetAudioListener2d()`
- `AudioListener3D GetAudioListener3d()`
- `Camera2D GetCamera2d()`
- `Camera3D GetCamera3d()`
- `bool GetCanvasCullMaskBit(int layer)`
- `Array[Window] GetEmbeddedSubwindows()`
- `Transform2D GetFinalTransform()`
- `Vector2 GetMousePosition()`
- `float GetOversampling()`
- `PositionalShadowAtlasQuadrantSubdiv GetPositionalShadowAtlasQuadrantSubdiv(int quadrant)`
- `int GetRenderInfo(RenderInfoType type, RenderInfo info)`
- `Transform2D GetScreenTransform()`
- `Transform2D GetStretchTransform()`
- `ViewportTexture GetTexture()`
- `RID GetViewportRid()`
- `Rect2 GetVisibleRect()`
- `void GuiCancelDrag()`
- `Variant GuiGetDragData()`
- `string GuiGetDragDescription()`
- `Control GuiGetFocusOwner()`
- `Control GuiGetHoveredControl()`
- `bool GuiIsDragSuccessful()`
- `bool GuiIsDragging()`
- `void GuiReleaseFocus()`
- `void GuiSetDragDescription(string description)`
- `bool IsInputHandled()`
- `void NotifyMouseEntered()`
- `void NotifyMouseExited()`
- `void PushInput(InputEvent event, bool inLocalCoords = false)`
- `void PushTextInput(string text)`
- `void PushUnhandledInput(InputEvent event, bool inLocalCoords = false)`
- `void SetCanvasCullMaskBit(int layer, bool enable)`
- `void SetInputAsHandled()`
- `void SetPositionalShadowAtlasQuadrantSubdiv(int quadrant, PositionalShadowAtlasQuadrantSubdiv subdiv)`
- `void UpdateMouseCursorState()`
- `void WarpMouse(Vector2 position)`

**C# Examples**
```csharp
public async override void _Ready()
{
    await ToSignal(RenderingServer.Singleton, RenderingServer.SignalName.FramePostDraw);
    var viewport = GetNode<Viewport>("Viewport");
    viewport.GetTexture().GetImage().SavePng("user://Screenshot.png");
}
```

### VisualShaderNodeBillboard
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

The output port of this node needs to be connected to Model View Matrix port of VisualShaderNodeOutput.

**Properties**
- `BillboardType BillboardType` = `1`
- `bool KeepScale` = `false`

### VisualShaderNodeBooleanConstant
*Inherits: **VisualShaderNodeConstant < VisualShaderNode < Resource < RefCounted < Object***

Has only one output port and no inputs.

**Properties**
- `bool Constant` = `false`

### VisualShaderNodeBooleanParameter
*Inherits: **VisualShaderNodeParameter < VisualShaderNode < Resource < RefCounted < Object***

Translated to uniform bool in the shader language.

**Properties**
- `bool DefaultValue` = `false`
- `bool DefaultValueEnabled` = `false`

### VisualShaderNodeClamp
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

Constrains a value to lie between min and max values.

**Properties**
- `OpType OpType` = `0`

### VisualShaderNodeColorConstant
*Inherits: **VisualShaderNodeConstant < VisualShaderNode < Resource < RefCounted < Object***

Has two output ports representing RGB and alpha channels of Color.

**Properties**
- `Color Constant` = `Color(1, 1, 1, 1)`

### VisualShaderNodeColorFunc
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

Accept a Color to the input port and transform it according to function.

**Properties**
- `Function Function` = `0`

### VisualShaderNodeColorOp
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

Applies operator to two color inputs.

**Properties**
- `Operator Operator` = `0`

### VisualShaderNodeColorParameter
*Inherits: **VisualShaderNodeParameter < VisualShaderNode < Resource < RefCounted < Object***

Translated to uniform vec4 in the shader language.

**Properties**
- `Color DefaultValue` = `Color(1, 1, 1, 1)`
- `bool DefaultValueEnabled` = `false`

### VisualShaderNodeComment
*Inherits: **VisualShaderNodeFrame < VisualShaderNodeResizableBase < VisualShaderNode < Resource < RefCounted < Object***

This node was replaced by VisualShaderNodeFrame and only exists to preserve compatibility. In the VisualShader editor it behaves exactly like VisualShaderNodeFrame.

**Properties**
- `string Description` = `""`

### VisualShaderNodeCompare
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

Compares a and b of type by function. Returns a boolean scalar. Translates to if instruction in shader code.

**Properties**
- `Condition Condition` = `0`
- `Function Function` = `0`
- `ComparisonType Type` = `0`

### VisualShaderNodeConstant
*Inherits: **VisualShaderNode < Resource < RefCounted < Object** | Inherited by: VisualShaderNodeBooleanConstant, VisualShaderNodeColorConstant, VisualShaderNodeFloatConstant, VisualShaderNodeIntConstant, VisualShaderNodeTransformConstant, VisualShaderNodeUIntConstant, ...*

This is an abstract class. See the derived types for descriptions of the possible values.

### VisualShaderNodeCubemapParameter
*Inherits: **VisualShaderNodeTextureParameter < VisualShaderNodeParameter < VisualShaderNode < Resource < RefCounted < Object***

Translated to uniform samplerCube in the shader language. The output value can be used as port for VisualShaderNodeCubemap.

### VisualShaderNodeCubemap
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

Translated to texture(cubemap, vec3) in the shader language. Returns a color vector and alpha channel as scalar.

**Properties**
- `TextureLayered CubeMap`
- `Source Source` = `0`
- `TextureType TextureType` = `0`

### VisualShaderNodeCurveTexture
*Inherits: **VisualShaderNodeResizableBase < VisualShaderNode < Resource < RefCounted < Object***

Comes with a built-in editor for texture's curves.

**Properties**
- `CurveTexture Texture`

### VisualShaderNodeCurveXYZTexture
*Inherits: **VisualShaderNodeResizableBase < VisualShaderNode < Resource < RefCounted < Object***

Comes with a built-in editor for texture's curves.

**Properties**
- `CurveXYZTexture Texture`

### VisualShaderNodeCustom
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

By inheriting this class you can create a custom VisualShader script addon which will be automatically added to the Visual Shader Editor. The VisualShaderNode's behavior is defined by overriding the provided virtual methods.

**Methods**
- `string _GetCategory() [virtual]`
- `string _GetCode(Array[String] inputVars, Array[String] outputVars, Mode mode, Type type) [virtual]`
- `int _GetDefaultInputPort(PortType type) [virtual]`
- `string _GetDescription() [virtual]`
- `string _GetFuncCode(Mode mode, Type type) [virtual]`
- `string _GetGlobalCode(Mode mode) [virtual]`
- `int _GetInputPortCount() [virtual]`
- `Variant _GetInputPortDefaultValue(int port) [virtual]`
- `string _GetInputPortName(int port) [virtual]`
- `PortType _GetInputPortType(int port) [virtual]`
- `string _GetName() [virtual]`
- `int _GetOutputPortCount() [virtual]`
- `string _GetOutputPortName(int port) [virtual]`
- `PortType _GetOutputPortType(int port) [virtual]`
- `int _GetPropertyCount() [virtual]`
- `int _GetPropertyDefaultIndex(int index) [virtual]`
- `string _GetPropertyName(int index) [virtual]`
- `PackedStringArray _GetPropertyOptions(int index) [virtual]`
- `PortType _GetReturnIconType() [virtual]`
- `bool _IsAvailable(Mode mode, Type type) [virtual]`
- `bool _IsHighend() [virtual]`
- `int GetOptionIndex(int option)`

### VisualShaderNodeDerivativeFunc
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

This node is only available in Fragment and Light visual shaders.

**Properties**
- `Function Function` = `0`
- `OpType OpType` = `0`
- `Precision Precision` = `0`

### VisualShaderNodeDeterminant
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

Translates to determinant(x) in the shader language.

### VisualShaderNodeDistanceFade
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

The distance fade effect fades out each pixel based on its distance to another object.

### VisualShaderNodeDotProduct
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

Translates to dot(a, b) in the shader language.

### VisualShaderNodeExpression
*Inherits: **VisualShaderNodeGroupBase < VisualShaderNodeResizableBase < VisualShaderNode < Resource < RefCounted < Object** | Inherited by: VisualShaderNodeGlobalExpression*

Custom Godot Shading Language expression, with a custom number of input and output ports.

**Properties**
- `string Expression` = `""`

### VisualShaderNodeFaceForward
*Inherits: **VisualShaderNodeVectorBase < VisualShaderNode < Resource < RefCounted < Object***

Translates to faceforward(N, I, Nref) in the shader language. The function has three vector parameters: N, the vector to orient, I, the incident vector, and Nref, the reference vector. If the dot product of I and Nref is smaller than zero the return value is N. Otherwise, -N is returned.

### VisualShaderNodeFloatConstant
*Inherits: **VisualShaderNodeConstant < VisualShaderNode < Resource < RefCounted < Object***

Translated to float in the shader language.

**Properties**
- `float Constant` = `0.0`

### VisualShaderNodeFloatFunc
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

Accept a floating-point scalar (x) to the input port and transform it according to function.

**Properties**
- `Function Function` = `13`

### VisualShaderNodeFloatOp
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

Applies operator to two floating-point inputs: a and b.

**Properties**
- `Operator Operator` = `0`

### VisualShaderNodeFloatParameter
*Inherits: **VisualShaderNodeParameter < VisualShaderNode < Resource < RefCounted < Object***

Translated to uniform float in the shader language.

**Properties**
- `float DefaultValue` = `0.0`
- `bool DefaultValueEnabled` = `false`
- `Hint Hint` = `0`
- `float Max` = `1.0`
- `float Min` = `0.0`
- `float Step` = `0.1`

### VisualShaderNodeFrame
*Inherits: **VisualShaderNodeResizableBase < VisualShaderNode < Resource < RefCounted < Object** | Inherited by: VisualShaderNodeComment*

A rectangular frame that can be used to group visual shader nodes together to improve organization.

**Properties**
- `PackedInt32Array AttachedNodes` = `PackedInt32Array()`
- `bool Autoshrink` = `true`
- `Color TintColor` = `Color(0.3, 0.3, 0.3, 0.75)`
- `bool TintColorEnabled` = `false`
- `string Title` = `"Title"`

**Methods**
- `void AddAttachedNode(int node)`
- `void RemoveAttachedNode(int node)`

### VisualShaderNodeFresnel
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

Returns falloff based on the dot product of surface normal and view direction of camera (pass associated inputs to it).

### VisualShaderNodeGlobalExpression
*Inherits: **VisualShaderNodeExpression < VisualShaderNodeGroupBase < VisualShaderNodeResizableBase < VisualShaderNode < Resource < RefCounted < Object***

Custom Godot Shader Language expression, which is placed on top of the generated shader. You can place various function definitions inside to call later in VisualShaderNodeExpressions (which are injected in the main shader functions). You can also declare varyings, uniforms and global constants.

### VisualShaderNodeGroupBase
*Inherits: **VisualShaderNodeResizableBase < VisualShaderNode < Resource < RefCounted < Object** | Inherited by: VisualShaderNodeExpression*

Currently, has no direct usage, use the derived classes instead.

**Methods**
- `void AddInputPort(int id, int type, string name)`
- `void AddOutputPort(int id, int type, string name)`
- `void ClearInputPorts()`
- `void ClearOutputPorts()`
- `int GetFreeInputPortId()`
- `int GetFreeOutputPortId()`
- `int GetInputPortCount()`
- `string GetInputs()`
- `int GetOutputPortCount()`
- `string GetOutputs()`
- `bool HasInputPort(int id)`
- `bool HasOutputPort(int id)`
- `bool IsValidPortName(string name)`
- `void RemoveInputPort(int id)`
- `void RemoveOutputPort(int id)`
- `void SetInputPortName(int id, string name)`
- `void SetInputPortType(int id, int type)`
- `void SetInputs(string inputs)`
- `void SetOutputPortName(int id, string name)`
- `void SetOutputPortType(int id, int type)`
- `void SetOutputs(string outputs)`

### VisualShaderNodeIf
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

This visual shader node has six input ports:

### VisualShaderNodeInput
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

Gives access to input variables (built-ins) available for the shader. See the shading reference for the list of available built-ins for each shader type (check Tutorials section for link).

**Properties**
- `string InputName` = `"[None]"`

**Methods**
- `string GetInputRealName()`

### VisualShaderNodeIntConstant
*Inherits: **VisualShaderNodeConstant < VisualShaderNode < Resource < RefCounted < Object***

Translated to int in the shader language.

**Properties**
- `int Constant` = `0`

### VisualShaderNodeIntFunc
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

Accept an integer scalar (x) to the input port and transform it according to function.

**Properties**
- `Function Function` = `2`

### VisualShaderNodeIntOp
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

Applies operator to two integer inputs: a and b.

**Properties**
- `Operator Operator` = `0`

### VisualShaderNodeIntParameter
*Inherits: **VisualShaderNodeParameter < VisualShaderNode < Resource < RefCounted < Object***

A VisualShaderNodeParameter of type int. Offers additional customization for range of accepted values.

**Properties**
- `int DefaultValue` = `0`
- `bool DefaultValueEnabled` = `false`
- `PackedStringArray EnumNames` = `PackedStringArray()`
- `Hint Hint` = `0`
- `int Max` = `100`
- `int Min` = `0`
- `int Step` = `1`

### VisualShaderNodeIs
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

Returns the boolean result of the comparison between INF or NaN and a scalar parameter.

**Properties**
- `Function Function` = `0`

### VisualShaderNodeLinearSceneDepth
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

This node can be used in fragment shaders.

### VisualShaderNodeMix
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

Translates to mix(a, b, weight) in the shader language.

**Properties**
- `OpType OpType` = `0`

### VisualShaderNodeMultiplyAdd
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

Uses three operands to compute (a * b + c) expression.

**Properties**
- `OpType OpType` = `0`

### VisualShaderNodeOuterProduct
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

OuterProduct treats the first parameter c as a column vector (matrix with one column) and the second parameter r as a row vector (matrix with one row) and does a linear algebraic matrix multiply c * r, yielding a matrix whose number of rows is the number of components in c and whose number of columns is the number of components in r.

### VisualShaderNodeOutput
*Inherits: **VisualShaderNode < Resource < RefCounted < Object** | Inherited by: VisualShaderNodeParticleOutput*

This visual shader node is present in all shader graphs in form of "Output" block with multiple output value ports.

### VisualShaderNodeParameterRef
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

Creating a reference to a VisualShaderNodeParameter allows you to reuse this parameter in different shaders or shader stages easily.

**Properties**
- `string ParameterName` = `"[None]"`

### VisualShaderNodeParameter
*Inherits: **VisualShaderNode < Resource < RefCounted < Object** | Inherited by: VisualShaderNodeBooleanParameter, VisualShaderNodeColorParameter, VisualShaderNodeFloatParameter, VisualShaderNodeIntParameter, VisualShaderNodeTextureParameter, VisualShaderNodeTransformParameter, ...*

A parameter represents a variable in the shader which is set externally, i.e. from the ShaderMaterial. Parameters are exposed as properties in the ShaderMaterial and can be assigned from the Inspector or from a script.

**Properties**
- `int InstanceIndex` = `0`
- `string ParameterName` = `""`
- `Qualifier Qualifier` = `0`

### VisualShaderNodeParticleAccelerator
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

Particle accelerator can be used in "process" step of particle shader. It will accelerate the particles. Connect it to the Velocity output port.

**Properties**
- `Mode Mode` = `0`

### VisualShaderNodeParticleBoxEmitter
*Inherits: **VisualShaderNodeParticleEmitter < VisualShaderNode < Resource < RefCounted < Object***

VisualShaderNodeParticleEmitter that makes the particles emitted in box shape with the specified extents.

### VisualShaderNodeParticleConeVelocity
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

This node can be used in "start" step of particle shader. It defines the initial velocity of the particles, making them move in cone shape starting from the center, with a given spread.

### VisualShaderNodeParticleEmitter
*Inherits: **VisualShaderNode < Resource < RefCounted < Object** | Inherited by: VisualShaderNodeParticleBoxEmitter, VisualShaderNodeParticleMeshEmitter, VisualShaderNodeParticleRingEmitter, VisualShaderNodeParticleSphereEmitter*

Particle emitter nodes can be used in "start" step of particle shaders and they define the starting position of the particles. Connect them to the Position output port.

**Properties**
- `bool Mode2d` = `false`

### VisualShaderNodeParticleEmit
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

This node internally calls emit_subparticle shader method. It will emit a particle from the configured sub-emitter and also allows to customize how its emitted. Requires a sub-emitter assigned to the particles node with this shader.

**Properties**
- `EmitFlags Flags` = `31`

### VisualShaderNodeParticleMeshEmitter
*Inherits: **VisualShaderNodeParticleEmitter < VisualShaderNode < Resource < RefCounted < Object***

VisualShaderNodeParticleEmitter that makes the particles emitted in a shape of the assigned mesh. It will emit from the mesh's surfaces, either all or only the specified one.

**Properties**
- `Mesh Mesh`
- `int SurfaceIndex` = `0`
- `bool UseAllSurfaces` = `true`

### VisualShaderNodeParticleMultiplyByAxisAngle
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

This node helps to multiply a position input vector by rotation using specific axis. Intended to work with emitters.

**Properties**
- `bool DegreesMode` = `true`

### VisualShaderNodeParticleOutput
*Inherits: **VisualShaderNodeOutput < VisualShaderNode < Resource < RefCounted < Object***

This node defines how particles are emitted. It allows to customize e.g. position and velocity. Available ports are different depending on which function this node is inside (start, process, collision) and whether custom data is enabled.

### VisualShaderNodeParticleRandomness
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

Randomness node will output pseudo-random values of the given type based on the specified minimum and maximum values.

**Properties**
- `OpType OpType` = `0`

### VisualShaderNodeParticleRingEmitter
*Inherits: **VisualShaderNodeParticleEmitter < VisualShaderNode < Resource < RefCounted < Object***

VisualShaderNodeParticleEmitter that makes the particles emitted in ring shape with the specified inner and outer radii and height.

### VisualShaderNodeParticleSphereEmitter
*Inherits: **VisualShaderNodeParticleEmitter < VisualShaderNode < Resource < RefCounted < Object***

VisualShaderNodeParticleEmitter that makes the particles emitted in sphere shape with the specified inner and outer radii.

### VisualShaderNodeProximityFade
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

The proximity fade effect fades out each pixel based on its distance to another object.

### VisualShaderNodeRandomRange
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

Random range node will output a pseudo-random scalar value in the specified range, based on the seed. The value is always the same for the given seed and range, so you should provide a changing input, e.g. by using time.

### VisualShaderNodeRemap
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

Remap will transform the input range into output range, e.g. you can change a 0..1 value to -2..2 etc. See @GlobalScope.remap() for more details.

**Properties**
- `OpType OpType` = `0`

### VisualShaderNodeReroute
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

Automatically adapts its port type to the type of the incoming connection and ensures valid connections.

**Methods**
- `PortType GetPortType()`

### VisualShaderNodeResizableBase
*Inherits: **VisualShaderNode < Resource < RefCounted < Object** | Inherited by: VisualShaderNodeCurveTexture, VisualShaderNodeCurveXYZTexture, VisualShaderNodeFrame, VisualShaderNodeGroupBase*

Resizable nodes have a handle that allows the user to adjust their size as needed.

**Properties**
- `Vector2 Size` = `Vector2(0, 0)`

### VisualShaderNodeRotationByAxis
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

RotationByAxis node will transform the vertices of a mesh with specified axis and angle in radians. It can be used to rotate an object in an arbitrary axis.

### VisualShaderNodeSDFRaymarch
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

Casts a ray against the screen SDF (signed-distance field) and returns the distance travelled.

### VisualShaderNodeSDFToScreenUV
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

Translates to sdf_to_screen_uv(sdf_pos) in the shader language.

### VisualShaderNodeSample3D
*Inherits: **VisualShaderNode < Resource < RefCounted < Object** | Inherited by: VisualShaderNodeTexture2DArray, VisualShaderNodeTexture3D*

A virtual class, use the descendants instead.

**Properties**
- `Source Source` = `0`

### VisualShaderNodeScreenNormalWorldSpace
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

The ScreenNormalWorldSpace node allows to create outline effects.

### VisualShaderNodeScreenUVToSDF
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

Translates to screen_uv_to_sdf(uv) in the shader language. If the UV port isn't connected, SCREEN_UV is used instead.

### VisualShaderNodeSmoothStep
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

Translates to smoothstep(edge0, edge1, x) in the shader language.

**Properties**
- `OpType OpType` = `0`

### VisualShaderNodeStep
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

Translates to step(edge, x) in the shader language.

**Properties**
- `OpType OpType` = `0`

### VisualShaderNodeSwitch
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

Returns an associated value of the op_type type if the provided boolean value is true or false.

**Properties**
- `OpType OpType` = `0`

### VisualShaderNodeTexture2DArrayParameter
*Inherits: **VisualShaderNodeTextureParameter < VisualShaderNodeParameter < VisualShaderNode < Resource < RefCounted < Object***

This parameter allows to provide a collection of textures for the shader. You can use VisualShaderNodeTexture2DArray to extract the textures from array.

### VisualShaderNodeTexture2DArray
*Inherits: **VisualShaderNodeSample3D < VisualShaderNode < Resource < RefCounted < Object***

Translated to uniform sampler2DArray in the shader language.

**Properties**
- `TextureLayered TextureArray`

### VisualShaderNodeTexture2DParameter
*Inherits: **VisualShaderNodeTextureParameter < VisualShaderNodeParameter < VisualShaderNode < Resource < RefCounted < Object***

Translated to uniform sampler2D in the shader language.

### VisualShaderNodeTexture3DParameter
*Inherits: **VisualShaderNodeTextureParameter < VisualShaderNodeParameter < VisualShaderNode < Resource < RefCounted < Object***

Translated to uniform sampler3D in the shader language.

### VisualShaderNodeTexture3D
*Inherits: **VisualShaderNodeSample3D < VisualShaderNode < Resource < RefCounted < Object***

Performs a lookup operation on the provided texture, with support for multiple texture sources to choose from.

**Properties**
- `Texture3D Texture`

### VisualShaderNodeTextureParameterTriplanar
*Inherits: **VisualShaderNodeTextureParameter < VisualShaderNodeParameter < VisualShaderNode < Resource < RefCounted < Object***

Performs a lookup operation on the texture provided as a uniform for the shader, with support for triplanar mapping.

### VisualShaderNodeTextureParameter
*Inherits: **VisualShaderNodeParameter < VisualShaderNode < Resource < RefCounted < Object** | Inherited by: VisualShaderNodeCubemapParameter, VisualShaderNodeTexture2DArrayParameter, VisualShaderNodeTexture2DParameter, VisualShaderNodeTexture3DParameter, VisualShaderNodeTextureParameterTriplanar*

Performs a lookup operation on the texture provided as a uniform for the shader.

**Properties**
- `ColorDefault ColorDefault` = `0`
- `TextureFilter TextureFilter` = `0`
- `TextureRepeat TextureRepeat` = `0`
- `TextureSource TextureSource` = `0`
- `TextureType TextureType` = `0`

### VisualShaderNodeTextureSDFNormal
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

Translates to texture_sdf_normal(sdf_pos) in the shader language.

### VisualShaderNodeTextureSDF
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

Translates to texture_sdf(sdf_pos) in the shader language.

### VisualShaderNodeTexture
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

Performs a lookup operation on the provided texture, with support for multiple texture sources to choose from.

**Properties**
- `Source Source` = `0`
- `Texture2D Texture`
- `TextureType TextureType` = `0`

### VisualShaderNodeTransformCompose
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

Creates a 4×4 transform matrix using four vectors of type vec3. Each vector is one row in the matrix and the last column is a vec4(0, 0, 0, 1).

### VisualShaderNodeTransformConstant
*Inherits: **VisualShaderNodeConstant < VisualShaderNode < Resource < RefCounted < Object***

A constant Transform3D, which can be used as an input node.

**Properties**
- `Transform3D Constant` = `Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0)`

### VisualShaderNodeTransformDecompose
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

Takes a 4×4 transform matrix and decomposes it into four vec3 values, one from each row of the matrix.

### VisualShaderNodeTransformFunc
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

Computes an inverse or transpose function on the provided Transform3D.

**Properties**
- `Function Function` = `0`

### VisualShaderNodeTransformOp
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

Applies operator to two transform (4×4 matrices) inputs.

**Properties**
- `Operator Operator` = `0`

### VisualShaderNodeTransformParameter
*Inherits: **VisualShaderNodeParameter < VisualShaderNode < Resource < RefCounted < Object***

Translated to uniform mat4 in the shader language.

**Properties**
- `Transform3D DefaultValue` = `Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0)`
- `bool DefaultValueEnabled` = `false`

### VisualShaderNodeTransformVecMult
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

A multiplication operation on a transform (4×4 matrix) and a vector, with support for different multiplication operators.

**Properties**
- `Operator Operator` = `0`

### VisualShaderNodeUIntConstant
*Inherits: **VisualShaderNodeConstant < VisualShaderNode < Resource < RefCounted < Object***

Translated to uint in the shader language.

**Properties**
- `int Constant` = `0`

### VisualShaderNodeUIntFunc
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

Accept an unsigned integer scalar (x) to the input port and transform it according to function.

**Properties**
- `Function Function` = `0`

### VisualShaderNodeUIntOp
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

Applies operator to two unsigned integer inputs: a and b.

**Properties**
- `Operator Operator` = `0`

### VisualShaderNodeUIntParameter
*Inherits: **VisualShaderNodeParameter < VisualShaderNode < Resource < RefCounted < Object***

A VisualShaderNodeParameter of type unsigned int. Offers additional customization for range of accepted values.

**Properties**
- `int DefaultValue` = `0`
- `bool DefaultValueEnabled` = `false`

### VisualShaderNodeUVFunc
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

UV functions are similar to Vector2 functions, but the input port of this node uses the shader's UV value by default.

**Properties**
- `Function Function` = `0`

### VisualShaderNodeUVPolarCoord
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

UV polar coord node will transform UV values into polar coordinates, with specified scale, zoom strength and repeat parameters. It can be used to create various swirl distortions.

### VisualShaderNodeVaryingGetter
*Inherits: **VisualShaderNodeVarying < VisualShaderNode < Resource < RefCounted < Object***

Outputs a value of a varying defined in the shader. You need to first create a varying that can be used in the given function, e.g. varying getter in Fragment shader requires a varying with mode set to VisualShader.VARYING_MODE_VERTEX_TO_FRAG_LIGHT.

### VisualShaderNodeVaryingSetter
*Inherits: **VisualShaderNodeVarying < VisualShaderNode < Resource < RefCounted < Object***

Inputs a value to a varying defined in the shader. You need to first create a varying that can be used in the given function, e.g. varying setter in Fragment shader requires a varying with mode set to VisualShader.VARYING_MODE_FRAG_TO_LIGHT.

### VisualShaderNodeVarying
*Inherits: **VisualShaderNode < Resource < RefCounted < Object** | Inherited by: VisualShaderNodeVaryingGetter, VisualShaderNodeVaryingSetter*

Varying values are shader variables that can be passed between shader functions, e.g. from Vertex shader to Fragment shader.

**Properties**
- `string VaryingName` = `"[None]"`
- `VaryingType VaryingType` = `0`

### VisualShaderNodeVec2Constant
*Inherits: **VisualShaderNodeConstant < VisualShaderNode < Resource < RefCounted < Object***

A constant Vector2, which can be used as an input node.

**Properties**
- `Vector2 Constant` = `Vector2(0, 0)`

### VisualShaderNodeVec2Parameter
*Inherits: **VisualShaderNodeParameter < VisualShaderNode < Resource < RefCounted < Object***

Translated to uniform vec2 in the shader language.

**Properties**
- `Vector2 DefaultValue` = `Vector2(0, 0)`
- `bool DefaultValueEnabled` = `false`

### VisualShaderNodeVec3Constant
*Inherits: **VisualShaderNodeConstant < VisualShaderNode < Resource < RefCounted < Object***

A constant Vector3, which can be used as an input node.

**Properties**
- `Vector3 Constant` = `Vector3(0, 0, 0)`

### VisualShaderNodeVec3Parameter
*Inherits: **VisualShaderNodeParameter < VisualShaderNode < Resource < RefCounted < Object***

Translated to uniform vec3 in the shader language.

**Properties**
- `Vector3 DefaultValue` = `Vector3(0, 0, 0)`
- `bool DefaultValueEnabled` = `false`

### VisualShaderNodeVec4Constant
*Inherits: **VisualShaderNodeConstant < VisualShaderNode < Resource < RefCounted < Object***

A constant 4D vector, which can be used as an input node.

**Properties**
- `Quaternion Constant` = `Quaternion(0, 0, 0, 1)`

### VisualShaderNodeVec4Parameter
*Inherits: **VisualShaderNodeParameter < VisualShaderNode < Resource < RefCounted < Object***

Translated to uniform vec4 in the shader language.

**Properties**
- `Vector4 DefaultValue` = `Vector4(0, 0, 0, 0)`
- `bool DefaultValueEnabled` = `false`

### VisualShaderNodeVectorBase
*Inherits: **VisualShaderNode < Resource < RefCounted < Object** | Inherited by: VisualShaderNodeFaceForward, VisualShaderNodeVectorCompose, VisualShaderNodeVectorDecompose, VisualShaderNodeVectorDistance, VisualShaderNodeVectorFunc, VisualShaderNodeVectorLen, ...*

This is an abstract class. See the derived types for descriptions of the possible operations.

**Properties**
- `OpType OpType` = `1`

### VisualShaderNodeVectorCompose
*Inherits: **VisualShaderNodeVectorBase < VisualShaderNode < Resource < RefCounted < Object***

Creates a vec2, vec3 or vec4 using scalar values that can be provided from separate inputs.

### VisualShaderNodeVectorDecompose
*Inherits: **VisualShaderNodeVectorBase < VisualShaderNode < Resource < RefCounted < Object***

Takes a vec2, vec3 or vec4 and decomposes it into scalar values that can be used as separate outputs.

### VisualShaderNodeVectorDistance
*Inherits: **VisualShaderNodeVectorBase < VisualShaderNode < Resource < RefCounted < Object***

Calculates distance from point represented by vector p0 to vector p1.

### VisualShaderNodeVectorFunc
*Inherits: **VisualShaderNodeVectorBase < VisualShaderNode < Resource < RefCounted < Object***

A visual shader node able to perform different functions using vectors.

**Properties**
- `Function Function` = `0`

### VisualShaderNodeVectorLen
*Inherits: **VisualShaderNodeVectorBase < VisualShaderNode < Resource < RefCounted < Object***

Translated to length(p0) in the shader language.

### VisualShaderNodeVectorOp
*Inherits: **VisualShaderNodeVectorBase < VisualShaderNode < Resource < RefCounted < Object***

A visual shader node for use of vector operators. Operates on vector a and vector b.

**Properties**
- `Operator Operator` = `0`

### VisualShaderNodeVectorRefract
*Inherits: **VisualShaderNodeVectorBase < VisualShaderNode < Resource < RefCounted < Object***

Translated to refract(I, N, eta) in the shader language, where I is the incident vector, N is the normal vector and eta is the ratio of the indices of the refraction.

### VisualShaderNodeWorldPositionFromDepth
*Inherits: **VisualShaderNode < Resource < RefCounted < Object***

The WorldPositionFromDepth node reconstructs the depth position of the pixel in world space. This can be used to obtain world space UVs for projection mapping like Caustics.

### VisualShaderNode
*Inherits: **Resource < RefCounted < Object** | Inherited by: VisualShaderNodeBillboard, VisualShaderNodeClamp, VisualShaderNodeColorFunc, VisualShaderNodeColorOp, VisualShaderNodeCompare, VisualShaderNodeConstant, ...*

Visual shader graphs consist of various nodes. Each node in the graph is a separate object and they are represented as a rectangular boxes with title and a set of properties. Each node also has connection ports that allow to connect it to another nodes and control the flow of the shader.

**Properties**
- `int LinkedParentGraphFrame` = `-1`
- `int OutputPortForPreview` = `-1`

**Methods**
- `void ClearDefaultInputValues()`
- `int GetDefaultInputPort(PortType type)`
- `Godot.Collections.Array GetDefaultInputValues()`
- `Variant GetInputPortDefaultValue(int port)`
- `void RemoveInputPortDefaultValue(int port)`
- `void SetDefaultInputValues(Godot.Collections.Array values)`
- `void SetInputPortDefaultValue(int port, Variant value, Variant prevValue = null)`

### VisualShader
*Inherits: **Shader < Resource < RefCounted < Object***

This class provides a graph-like visual editor for creating a Shader. Although VisualShaders do not require coding, they share the same logic with script shaders. They use VisualShaderNodes that can be connected to each other to control the flow of the shader. The visual shader graph is converted to a script shader behind the scenes.

**Properties**
- `Vector2 GraphOffset`

**Methods**
- `void AddNode(Type type, VisualShaderNode node, Vector2 position, int id)`
- `void AddVarying(string name, VaryingMode mode, VaryingType type)`
- `void AttachNodeToFrame(Type type, int id, int frame)`
- `bool CanConnectNodes(Type type, int fromNode, int fromPort, int toNode, int toPort)`
- `Error ConnectNodes(Type type, int fromNode, int fromPort, int toNode, int toPort)`
- `void ConnectNodesForced(Type type, int fromNode, int fromPort, int toNode, int toPort)`
- `void DetachNodeFromFrame(Type type, int id)`
- `void DisconnectNodes(Type type, int fromNode, int fromPort, int toNode, int toPort)`
- `VisualShaderNode GetNode(Type type, int id)`
- `Array[Dictionary] GetNodeConnections(Type type)`
- `PackedInt32Array GetNodeList(Type type)`
- `Vector2 GetNodePosition(Type type, int id)`
- `int GetValidNodeId(Type type)`
- `bool HasVarying(string name)`
- `bool IsNodeConnection(Type type, int fromNode, int fromPort, int toNode, int toPort)`
- `void RemoveNode(Type type, int id)`
- `void RemoveVarying(string name)`
- `void ReplaceNode(Type type, int id, StringName newClass)`
- `void SetMode(Mode mode)`
- `void SetNodePosition(Type type, int id, Vector2 position)`
