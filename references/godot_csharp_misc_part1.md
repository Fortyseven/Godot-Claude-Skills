# Godot 4 C# API Reference — Misc (Part 1)

> C#-only reference. 285 classes.

### @GDScript

A list of utility functions and annotations accessible from any script written in GDScript.

**Methods**
- `Color Color8(int r8, int g8, int b8, int a8 = 255)`
- `void Assert(bool condition, string message = "")`
- `string Char(int code)`
- `Variant Convert(Variant what, Variant.Type type)`
- `Object DictToInst(Godot.Collections.Dictionary dictionary)`
- `Godot.Collections.Array GetStack()`
- `Godot.Collections.Dictionary InstToDict(Object instance)`
- `bool IsInstanceOf(Variant value, Variant type)`
- `int Len(Variant var)`
- `Resource Load(string path)`
- `int Ord(string char)`
- `Resource Preload(string path)`
- `void PrintDebug()`
- `void PrintStack()`
- `Godot.Collections.Array Range()`
- `bool TypeExists(StringName type)`

### @GlobalScope

A list of global scope enumerated constants and built-in functions. This is all that resides in the globals, constants regarding error codes, keycodes, property hints, etc.

**Properties**
- `AudioServer Audioserver`
- `CameraServer Cameraserver`
- `ClassDB Classdb`
- `DisplayServer Displayserver`
- `EditorInterface Editorinterface`
- `Engine Engine`
- `EngineDebugger Enginedebugger`
- `GDExtensionManager Gdextensionmanager`
- `Geometry2D Geometry2d`
- `Geometry3D Geometry3d`
- `IP Ip`
- `Input Input`
- `InputMap Inputmap`
- `JavaClassWrapper Javaclasswrapper`
- `JavaScriptBridge Javascriptbridge`
- `Marshalls Marshalls`
- `NativeMenu Nativemenu`
- `NavigationMeshGenerator Navigationmeshgenerator`
- `NavigationServer2D Navigationserver2d`
- `NavigationServer2DManager Navigationserver2dmanager`
- `NavigationServer3D Navigationserver3d`
- `NavigationServer3DManager Navigationserver3dmanager`
- `OS Os`
- `Performance Performance`
- `PhysicsServer2D Physicsserver2d`
- `PhysicsServer2DManager Physicsserver2dmanager`
- `PhysicsServer3D Physicsserver3d`
- `PhysicsServer3DManager Physicsserver3dmanager`
- `ProjectSettings Projectsettings`
- `RenderingServer Renderingserver`

**Methods**
- `Variant Abs(Variant x)`
- `float Absf(float x)`
- `int Absi(int x)`
- `float Acos(float x)`
- `float Acosh(float x)`
- `float AngleDifference(float from, float to)`
- `float Asin(float x)`
- `float Asinh(float x)`
- `float Atan(float x)`
- `float Atan2(float y, float x)`
- `float Atanh(float x)`
- `float BezierDerivative(float start, float control1, float control2, float end, float t)`
- `float BezierInterpolate(float start, float control1, float control2, float end, float t)`
- `Variant BytesToVar(PackedByteArray bytes)`
- `Variant BytesToVarWithObjects(PackedByteArray bytes)`
- `Variant Ceil(Variant x)`
- `float Ceilf(float x)`
- `int Ceili(float x)`
- `Variant Clamp(Variant value, Variant min, Variant max)`
- `float Clampf(float value, float min, float max)`
- `int Clampi(int value, int min, int max)`
- `float Cos(float angleRad)`
- `float Cosh(float x)`
- `float CubicInterpolate(float from, float to, float pre, float post, float weight)`
- `float CubicInterpolateAngle(float from, float to, float pre, float post, float weight)`
- `float CubicInterpolateAngleInTime(float from, float to, float pre, float post, float weight, float toT, float preT, float postT)`
- `float CubicInterpolateInTime(float from, float to, float pre, float post, float weight, float toT, float preT, float postT)`
- `float DbToLinear(float db)`
- `float DegToRad(float deg)`
- `float Ease(float x, float curve)`
- `string ErrorString(int error)`
- `float Exp(float x)`
- `Variant Floor(Variant x)`
- `float Floorf(float x)`
- `int Floori(float x)`
- `float Fmod(float x, float y)`
- `float Fposmod(float x, float y)`
- `int Hash(Variant variable)`
- `Object InstanceFromId(int instanceId)`
- `float InverseLerp(float from, float to, float weight)`

**C# Examples**
```csharp
// Array of elemType.
hintString = $"{elemType:D}:";
hintString = $"{elemType:}/{elemHint:D}:{elemHintString}";
// Two-dimensional array of elemType (array of arrays of elemType).
hintString = $"{Variant.Type.Array:D}:{elemType:D}:";
hintString = $"{Variant.Type.Array:D}:{elemType:D}/{elemHint:D}:{elemHintString}";
// Three-dimensional array of elemType (array of arrays of arrays of elemType).
hintString = $"{Variant.Type.Array:D}:{Variant.Type.Array:D}:{elemType:D}:";
hintString = $"{Variant.Type.Array:D}:{Variant.Type.Array:D}:{elemType:D}/{elemHint:D}:{elemHintString}";
```
```csharp
hintString = $"{Variant.Type.Int:D}/{PropertyHint.Range:D}:1,10,1"; // Array of integers (in range from 1 to 10).
hintString = $"{Variant.Type.Int:D}/{PropertyHint.Enum:D}:Zero,One,Two"; // Array of integers (an enum).
hintString = $"{Variant.Type.Int:D}/{PropertyHint.Enum:D}:Zero,One,Three:3,Six:6"; // Array of integers (an enum).
hintString = $"{Variant.Type.String:D}/{PropertyHint.File:D}:*.png"; // Array of strings (file paths).
hintString = $"{Variant.Type.Object:D}/{PropertyHint.ResourceType:D}:Texture2D"; // Array of textures.

hintString = $"{Variant.Type.Array:D}:{Variant.Type.Float:D
// ...
```

### AABB

The AABB built-in Variant type represents an axis-aligned bounding box in a 3D space. It is defined by its position and size, which are Vector3. It is frequently used for fast overlap tests (see intersects()). Although AABB itself is axis-aligned, it can be combined with Transform3D to represent a rotated or skewed bounding box.

**Properties**
- `Vector3 End` = `Vector3(0, 0, 0)`
- `Vector3 Position` = `Vector3(0, 0, 0)`
- `Vector3 Size` = `Vector3(0, 0, 0)`

**Methods**
- `AABB Abs()`
- `bool Encloses(AABB with)`
- `AABB Expand(Vector3 toPoint)`
- `Vector3 GetCenter()`
- `Vector3 GetEndpoint(int idx)`
- `Vector3 GetLongestAxis()`
- `int GetLongestAxisIndex()`
- `float GetLongestAxisSize()`
- `Vector3 GetShortestAxis()`
- `int GetShortestAxisIndex()`
- `float GetShortestAxisSize()`
- `Vector3 GetSupport(Vector3 direction)`
- `float GetVolume()`
- `AABB Grow(float by)`
- `bool HasPoint(Vector3 point)`
- `bool HasSurface()`
- `bool HasVolume()`
- `AABB Intersection(AABB with)`
- `bool Intersects(AABB with)`
- `bool IntersectsPlane(Plane plane)`
- `Variant IntersectsRay(Vector3 from, Vector3 dir)`
- `Variant IntersectsSegment(Vector3 from, Vector3 to)`
- `bool IsEqualApprox(AABB aabb)`
- `bool IsFinite()`
- `AABB Merge(AABB with)`

**C# Examples**
```csharp
var box = new Aabb(new Vector3(5, 0, 5), new Vector3(-20, -10, -5));
var absolute = box.Abs();
GD.Print(absolute.Position); // Prints (-15, -10, 0)
GD.Print(absolute.Size);     // Prints (20, 10, 5)
```
```csharp
var a = new Aabb(new Vector3(0, 0, 0), new Vector3(4, 4, 4));
var b = new Aabb(new Vector3(1, 1, 1), new Vector3(3, 3, 3));
var c = new Aabb(new Vector3(2, 2, 2), new Vector3(8, 8, 8));

GD.Print(a.Encloses(a)); // Prints True
GD.Print(a.Encloses(b)); // Prints True
GD.Print(a.Encloses(c)); // Prints False
```

### AStar2D
*Inherits: **RefCounted < Object***

An implementation of the A* algorithm, used to find the shortest path between two vertices on a connected graph in 2D space.

**Properties**
- `bool NeighborFilterEnabled` = `false`

**Methods**
- `float _ComputeCost(int fromId, int toId) [virtual]`
- `float _EstimateCost(int fromId, int endId) [virtual]`
- `bool _FilterNeighbor(int fromId, int neighborId) [virtual]`
- `void AddPoint(int id, Vector2 position, float weightScale = 1.0)`
- `bool ArePointsConnected(int id, int toId, bool bidirectional = true)`
- `void Clear()`
- `void ConnectPoints(int id, int toId, bool bidirectional = true)`
- `void DisconnectPoints(int id, int toId, bool bidirectional = true)`
- `int GetAvailablePointId()`
- `int GetClosestPoint(Vector2 toPosition, bool includeDisabled = false)`
- `Vector2 GetClosestPositionInSegment(Vector2 toPosition)`
- `PackedInt64Array GetIdPath(int fromId, int toId, bool allowPartialPath = false)`
- `int GetPointCapacity()`
- `PackedInt64Array GetPointConnections(int id)`
- `int GetPointCount()`
- `PackedInt64Array GetPointIds()`
- `PackedVector2Array GetPointPath(int fromId, int toId, bool allowPartialPath = false)`
- `Vector2 GetPointPosition(int id)`
- `float GetPointWeightScale(int id)`
- `bool HasPoint(int id)`
- `bool IsPointDisabled(int id)`
- `void RemovePoint(int id)`
- `void ReserveSpace(int numNodes)`
- `void SetPointDisabled(int id, bool disabled = true)`
- `void SetPointPosition(int id, Vector2 position)`
- `void SetPointWeightScale(int id, float weightScale)`

**C# Examples**
```csharp
var astar = new AStar2D();
astar.AddPoint(1, new Vector2(1, 0), 4); // Adds the point (1, 0) with weight_scale 4 and id 1
```
```csharp
var astar = new AStar2D();
astar.AddPoint(1, new Vector2(1, 1));
astar.AddPoint(2, new Vector2(0, 5));
astar.ConnectPoints(1, 2, false);
```

### AStar3D
*Inherits: **RefCounted < Object***

A* (A star) is a computer algorithm used in pathfinding and graph traversal, the process of plotting short paths among vertices (points), passing through a given set of edges (segments). It enjoys widespread use due to its performance and accuracy. Godot's A* implementation uses points in 3D space and Euclidean distances by default.

**Properties**
- `bool NeighborFilterEnabled` = `false`

**Methods**
- `float _ComputeCost(int fromId, int toId) [virtual]`
- `float _EstimateCost(int fromId, int endId) [virtual]`
- `bool _FilterNeighbor(int fromId, int neighborId) [virtual]`
- `void AddPoint(int id, Vector3 position, float weightScale = 1.0)`
- `bool ArePointsConnected(int id, int toId, bool bidirectional = true)`
- `void Clear()`
- `void ConnectPoints(int id, int toId, bool bidirectional = true)`
- `void DisconnectPoints(int id, int toId, bool bidirectional = true)`
- `int GetAvailablePointId()`
- `int GetClosestPoint(Vector3 toPosition, bool includeDisabled = false)`
- `Vector3 GetClosestPositionInSegment(Vector3 toPosition)`
- `PackedInt64Array GetIdPath(int fromId, int toId, bool allowPartialPath = false)`
- `int GetPointCapacity()`
- `PackedInt64Array GetPointConnections(int id)`
- `int GetPointCount()`
- `PackedInt64Array GetPointIds()`
- `PackedVector3Array GetPointPath(int fromId, int toId, bool allowPartialPath = false)`
- `Vector3 GetPointPosition(int id)`
- `float GetPointWeightScale(int id)`
- `bool HasPoint(int id)`
- `bool IsPointDisabled(int id)`
- `void RemovePoint(int id)`
- `void ReserveSpace(int numNodes)`
- `void SetPointDisabled(int id, bool disabled = true)`
- `void SetPointPosition(int id, Vector3 position)`
- `void SetPointWeightScale(int id, float weightScale)`

**C# Examples**
```csharp
using Godot;

[GlobalClass]
public partial class MyAStar3D : AStar3D
{
    public override float _ComputeCost(long fromId, long toId)
    {
        Vector3 fromPoint = GetPointPosition(fromId);
        Vector3 toPoint = GetPointPosition(toId);

        return Mathf.Abs(fromPoint.X - toPoint.X) + Mathf.Abs(fromPoint.Y - toPoint.Y) + Mathf.Abs(fromPoint.Z - toPoint.Z);
    }

    public override float _EstimateCost(long fromId, long toId)
    {
        Vector3 fromPoint = GetPointPosition(fromId);
        Vector3 toPoint = GetPointPosition(toId);
        return Mathf.Abs(fromPoint.X - toPoint.X)
// ...
```
```csharp
var astar = new AStar3D();
astar.AddPoint(1, new Vector3(1, 0, 0), 4); // Adds the point (1, 0, 0) with weight_scale 4 and id 1
```

### AStarGrid2D
*Inherits: **RefCounted < Object***

AStarGrid2D is a variant of AStar2D that is specialized for partial 2D grids. It is simpler to use because it doesn't require you to manually create points and connect them together. This class also supports multiple types of heuristics, modes for diagonal movement, and a jumping mode to speed up calculations.

**Properties**
- `CellShape CellShape` = `0`
- `Vector2 CellSize` = `Vector2(1, 1)`
- `Heuristic DefaultComputeHeuristic` = `0`
- `Heuristic DefaultEstimateHeuristic` = `0`
- `DiagonalMode DiagonalMode` = `0`
- `bool JumpingEnabled` = `false`
- `Vector2 Offset` = `Vector2(0, 0)`
- `Rect2i Region` = `Rect2i(0, 0, 0, 0)`
- `Vector2i Size` = `Vector2i(0, 0)`

**Methods**
- `float _ComputeCost(Vector2i fromId, Vector2i toId) [virtual]`
- `float _EstimateCost(Vector2i fromId, Vector2i endId) [virtual]`
- `void Clear()`
- `void FillSolidRegion(Rect2i region, bool solid = true)`
- `void FillWeightScaleRegion(Rect2i region, float weightScale)`
- `Array[Vector2i] GetIdPath(Vector2i fromId, Vector2i toId, bool allowPartialPath = false)`
- `Array[Dictionary] GetPointDataInRegion(Rect2i region)`
- `PackedVector2Array GetPointPath(Vector2i fromId, Vector2i toId, bool allowPartialPath = false)`
- `Vector2 GetPointPosition(Vector2i id)`
- `float GetPointWeightScale(Vector2i id)`
- `bool IsDirty()`
- `bool IsInBounds(int x, int y)`
- `bool IsInBoundsv(Vector2i id)`
- `bool IsPointSolid(Vector2i id)`
- `void SetPointSolid(Vector2i id, bool solid = true)`
- `void SetPointWeightScale(Vector2i id, float weightScale)`
- `void Update()`

**C# Examples**
```csharp
AStarGrid2D astarGrid = new AStarGrid2D();
astarGrid.Region = new Rect2I(0, 0, 32, 32);
astarGrid.CellSize = new Vector2I(16, 16);
astarGrid.Update();
GD.Print(astarGrid.GetIdPath(Vector2I.Zero, new Vector2I(3, 4))); // Prints [(0, 0), (1, 1), (2, 2), (3, 3), (3, 4)]
GD.Print(astarGrid.GetPointPath(Vector2I.Zero, new Vector2I(3, 4))); // Prints [(0, 0), (16, 16), (32, 32), (48, 48), (48, 64)]
```

### AnimatedSprite3D
*Inherits: **SpriteBase3D < GeometryInstance3D < VisualInstance3D < Node3D < Node < Object***

AnimatedSprite3D is similar to the Sprite3D node, except it carries multiple textures as animation sprite_frames. Animations are created using a SpriteFrames resource, which allows you to import image files (or a folder containing said files) to provide the animation frames for the sprite. The SpriteFrames resource can be configured in the editor via the SpriteFrames bottom panel.

**Properties**
- `StringName Animation` = `&"default"`
- `string Autoplay` = `""`
- `int Frame` = `0`
- `float FrameProgress` = `0.0`
- `float SpeedScale` = `1.0`
- `SpriteFrames SpriteFrames`

**Methods**
- `float GetPlayingSpeed()`
- `bool IsPlaying()`
- `void Pause()`
- `void Play(StringName name = &"", float customSpeed = 1.0, bool fromEnd = false)`
- `void PlayBackwards(StringName name = &"")`
- `void SetFrameAndProgress(int frame, float progress)`
- `void Stop()`

### ArrayOccluder3D
*Inherits: **Occluder3D < Resource < RefCounted < Object***

ArrayOccluder3D stores an arbitrary 3D polygon shape that can be used by the engine's occlusion culling system. This is analogous to ArrayMesh, but for occluders.

**Properties**
- `PackedInt32Array Indices` = `PackedInt32Array()`
- `PackedVector3Array Vertices` = `PackedVector3Array()`

**Methods**
- `void SetArrays(PackedVector3Array vertices, PackedInt32Array indices)`

### Array

An array data structure that can contain a sequence of elements of any Variant type by default. Values can optionally be constrained to a specific type by creating a typed array. Elements are accessed by a numerical index starting at 0. Negative indices are used to count from the back (-1 is the last element, -2 is the second to last, etc.).

**Methods**
- `bool All(Callable method)`
- `bool Any(Callable method)`
- `void Append(Variant value)`
- `void AppendArray(Godot.Collections.Array array)`
- `void Assign(Godot.Collections.Array array)`
- `Variant Back()`
- `int Bsearch(Variant value, bool before = true)`
- `int BsearchCustom(Variant value, Callable func, bool before = true)`
- `void Clear()`
- `int Count(Variant value)`
- `Godot.Collections.Array Duplicate(bool deep = false)`
- `Godot.Collections.Array DuplicateDeep(int deepSubresourcesMode = 1)`
- `void Erase(Variant value)`
- `void Fill(Variant value)`
- `Godot.Collections.Array Filter(Callable method)`
- `int Find(Variant what, int from = 0)`
- `int FindCustom(Callable method, int from = 0)`
- `Variant Front()`
- `Variant Get(int index)`
- `int GetTypedBuiltin()`
- `StringName GetTypedClassName()`
- `Variant GetTypedScript()`
- `bool Has(Variant value)`
- `int Hash()`
- `int Insert(int position, Variant value)`
- `bool IsEmpty()`
- `bool IsReadOnly()`
- `bool IsSameTyped(Godot.Collections.Array array)`
- `bool IsTyped()`
- `void MakeReadOnly()`
- `Godot.Collections.Array Map(Callable method)`
- `Variant Max()`
- `Variant Min()`
- `Variant PickRandom()`
- `Variant PopAt(int position)`
- `Variant PopBack()`
- `Variant PopFront()`
- `void PushBack(Variant value)`
- `void PushFront(Variant value)`
- `Variant Reduce(Callable method, Variant accum = null)`

**C# Examples**
```csharp
Godot.Collections.Array array = ["First", 2, 3, "Last"];
GD.Print(array[0]); // Prints "First"
GD.Print(array[2]); // Prints 3
GD.Print(array[^1]); // Prints "Last"

array[1] = "Second";
GD.Print(array[1]); // Prints "Second"
GD.Print(array[^3]); // Prints "Second"

// This typed array can only contain integers.
// Attempting to add any other type will result in an error.
Godot.Collections.Array<int> typedArray = [1, 2, 3];
```
```csharp
private static bool GreaterThan5(int number)
{
    return number > 5;
}

public override void _Ready()
{
    // Prints True (3/3 elements evaluate to true).
    GD.Print(new Godot.Collections.Array>int< { 6, 10, 6 }.All(GreaterThan5));
    // Prints False (1/3 elements evaluate to true).
    GD.Print(new Godot.Collections.Array>int< { 4, 10, 4 }.All(GreaterThan5));
    // Prints False (0/3 elements evaluate to true).
    GD.Print(new Godot.Collections.Array>int< { 4, 4, 4 }.All(GreaterThan5));
    // Prints True (0/0 elements evaluate to true).
    GD.Print(new Godot.Collections.Array>int< { }
// ...
```

### AudioListener2D
*Inherits: **Node2D < CanvasItem < Node < Object***

Once added to the scene tree and enabled using make_current(), this node will override the location sounds are heard from. Only one AudioListener2D can be current. Using make_current() will disable the previous AudioListener2D.

**Methods**
- `void ClearCurrent()`
- `bool IsCurrent()`
- `void MakeCurrent()`

### AudioListener3D
*Inherits: **Node3D < Node < Object***

Once added to the scene tree and enabled using make_current(), this node will override the location sounds are heard from. This can be used to listen from a location different from the Camera3D.

**Properties**
- `DopplerTracking DopplerTracking` = `0`

**Methods**
- `void ClearCurrent()`
- `Transform3D GetListenerTransform()`
- `bool IsCurrent()`
- `void MakeCurrent()`

### AudioSamplePlayback
*Inherits: **RefCounted < Object***

Meta class for playing back audio samples.

### AudioSample
*Inherits: **RefCounted < Object***

Base class for audio samples.

### BackBufferCopy
*Inherits: **Node2D < CanvasItem < Node < Object***

Node for back-buffering the currently-displayed screen. The region defined in the BackBufferCopy node is buffered with the content of the screen it covers, or the entire screen according to the copy_mode. It can be accessed in shader scripts using the screen texture (i.e. a uniform sampler with hint_screen_texture).

**Properties**
- `CopyMode CopyMode` = `1`
- `Rect2 Rect` = `Rect2(-100, -100, 200, 200)`

### Basis

The Basis built-in Variant type is a 3×3 matrix used to represent 3D rotation, scale, and shear. It is frequently used within a Transform3D.

**Properties**
- `Vector3 X` = `Vector3(1, 0, 0)`
- `Vector3 Y` = `Vector3(0, 1, 0)`
- `Vector3 Z` = `Vector3(0, 0, 1)`

**Methods**
- `float Determinant()`
- `Basis FromEuler(Vector3 euler, int order = 2) [static]`
- `Basis FromScale(Vector3 scale) [static]`
- `Vector3 GetEuler(int order = 2)`
- `Quaternion GetRotationQuaternion()`
- `Vector3 GetScale()`
- `Basis Inverse()`
- `bool IsConformal()`
- `bool IsEqualApprox(Basis b)`
- `bool IsFinite()`
- `Basis LookingAt(Vector3 target, Vector3 up = Vector3(0, 1, 0), bool useModelFront = false) [static]`
- `Basis Orthonormalized()`
- `Basis Rotated(Vector3 axis, float angle)`
- `Basis Scaled(Vector3 scale)`
- `Basis ScaledLocal(Vector3 scale)`
- `Basis Slerp(Basis to, float weight)`
- `float Tdotx(Vector3 with)`
- `float Tdoty(Vector3 with)`
- `float Tdotz(Vector3 with)`
- `Basis Transposed()`

**C# Examples**
```csharp
// Creates a Basis whose z axis points down.
var myBasis = Basis.FromEuler(new Vector3(Mathf.Tau / 4.0f, 0.0f, 0.0f));

GD.Print(myBasis.Z); // Prints (0, -1, 0)
```
```csharp
var myBasis = Basis.FromScale(new Vector3(2.0f, 4.0f, 8.0f));

GD.Print(myBasis.X); // Prints (2, 0, 0)
GD.Print(myBasis.Y); // Prints (0, 4, 0)
GD.Print(myBasis.Z); // Prints (0, 0, 8)
```

### Bone2D
*Inherits: **Node2D < CanvasItem < Node < Object***

A hierarchy of Bone2Ds can be bound to a Skeleton2D to control and animate other Node2D nodes.

**Properties**
- `Transform2D Rest` = `Transform2D(0, 0, 0, 0, 0, 0)`

**Methods**
- `void ApplyRest()`
- `bool GetAutocalculateLengthAndAngle()`
- `float GetBoneAngle()`
- `int GetIndexInSkeleton()`
- `float GetLength()`
- `Transform2D GetSkeletonRest()`
- `void SetAutocalculateLengthAndAngle(bool autoCalculate)`
- `void SetBoneAngle(float angle)`
- `void SetLength(float length)`

### BoneConstraint3D
*Inherits: **SkeletonModifier3D < Node3D < Node < Object** | Inherited by: AimModifier3D, ConvertTransformModifier3D, CopyTransformModifier3D*

Base class of SkeletonModifier3D that modifies the bone set in set_apply_bone() based on the transform of the bone retrieved by get_reference_bone().

**Methods**
- `void ClearSetting()`
- `float GetAmount(int index)`
- `int GetApplyBone(int index)`
- `string GetApplyBoneName(int index)`
- `int GetReferenceBone(int index)`
- `string GetReferenceBoneName(int index)`
- `NodePath GetReferenceNode(int index)`
- `ReferenceType GetReferenceType(int index)`
- `int GetSettingCount()`
- `void SetAmount(int index, float amount)`
- `void SetApplyBone(int index, int bone)`
- `void SetApplyBoneName(int index, string boneName)`
- `void SetReferenceBone(int index, int bone)`
- `void SetReferenceBoneName(int index, string boneName)`
- `void SetReferenceNode(int index, NodePath node)`
- `void SetReferenceType(int index, ReferenceType type)`
- `void SetSettingCount(int count)`

### BoneMap
*Inherits: **Resource < RefCounted < Object***

This class contains a dictionary that uses a list of bone names in SkeletonProfile as key names.

**Properties**
- `SkeletonProfile Profile`

**Methods**
- `StringName FindProfileBoneName(StringName skeletonBoneName)`
- `StringName GetSkeletonBoneName(StringName profileBoneName)`
- `void SetSkeletonBoneName(StringName profileBoneName, StringName skeletonBoneName)`

### BoneTwistDisperser3D
*Inherits: **SkeletonModifier3D < Node3D < Node < Object***

This BoneTwistDisperser3D allows for smooth twist interpolation between multiple bones by dispersing the end bone's twist to the parents. This only changes the twist without changing the global position of each joint.

**Properties**
- `bool MutableBoneAxes` = `true`
- `int SettingCount` = `0`

**Methods**
- `void ClearSettings()`
- `Curve GetDampingCurve(int index)`
- `DisperseMode GetDisperseMode(int index)`
- `int GetEndBone(int index)`
- `BoneDirection GetEndBoneDirection(int index)`
- `string GetEndBoneName(int index)`
- `int GetJointBone(int index, int joint)`
- `string GetJointBoneName(int index, int joint)`
- `int GetJointCount(int index)`
- `float GetJointTwistAmount(int index, int joint)`
- `int GetReferenceBone(int index)`
- `string GetReferenceBoneName(int index)`
- `int GetRootBone(int index)`
- `string GetRootBoneName(int index)`
- `Quaternion GetTwistFrom(int index)`
- `float GetWeightPosition(int index)`
- `bool IsEndBoneExtended(int index)`
- `bool IsTwistFromRest(int index)`
- `void SetDampingCurve(int index, Curve curve)`
- `void SetDisperseMode(int index, DisperseMode disperseMode)`
- `void SetEndBone(int index, int bone)`
- `void SetEndBoneDirection(int index, BoneDirection boneDirection)`
- `void SetEndBoneName(int index, string boneName)`
- `void SetExtendEndBone(int index, bool enabled)`
- `void SetJointTwistAmount(int index, int joint, float twistAmount)`
- `void SetRootBone(int index, int bone)`
- `void SetRootBoneName(int index, string boneName)`
- `void SetTwistFrom(int index, Quaternion from)`
- `void SetTwistFromRest(int index, bool enabled)`
- `void SetWeightPosition(int index, float weightPosition)`

### BoxOccluder3D
*Inherits: **Occluder3D < Resource < RefCounted < Object***

BoxOccluder3D stores a cuboid shape that can be used by the engine's occlusion culling system.

**Properties**
- `Vector3 Size` = `Vector3(1, 1, 1)`

### BoxShape3D
*Inherits: **Shape3D < Resource < RefCounted < Object***

A 3D box shape, intended for use in physics. Usually used to provide a shape for a CollisionShape3D.

**Properties**
- `Vector3 Size` = `Vector3(1, 1, 1)`

### CCDIK3D
*Inherits: **IterateIK3D < ChainIK3D < IKModifier3D < SkeletonModifier3D < Node3D < Node < Object***

CCDIK3D is rotation based IK, enabling fast and effective tracking even with large joint rotations. It's especially suitable for chains with limitations, providing smoother and more stable target tracking compared to FABRIK3D.

### CPUParticles3D
*Inherits: **GeometryInstance3D < VisualInstance3D < Node3D < Node < Object***

CPU-based 3D particle node used to create a variety of particle systems and effects.

**Properties**
- `int Amount` = `8`
- `Curve AngleCurve`
- `float AngleMax` = `0.0`
- `float AngleMin` = `0.0`
- `Curve AngularVelocityCurve`
- `float AngularVelocityMax` = `0.0`
- `float AngularVelocityMin` = `0.0`
- `Curve AnimOffsetCurve`
- `float AnimOffsetMax` = `0.0`
- `float AnimOffsetMin` = `0.0`
- `Curve AnimSpeedCurve`
- `float AnimSpeedMax` = `0.0`
- `float AnimSpeedMin` = `0.0`
- `Color Color` = `Color(1, 1, 1, 1)`
- `Gradient ColorInitialRamp`
- `Gradient ColorRamp`
- `Curve DampingCurve`
- `float DampingMax` = `0.0`
- `float DampingMin` = `0.0`
- `Vector3 Direction` = `Vector3(1, 0, 0)`
- `DrawOrder DrawOrder` = `0`
- `Vector3 EmissionBoxExtents`
- `PackedColorArray EmissionColors` = `PackedColorArray()`
- `PackedVector3Array EmissionNormals`
- `PackedVector3Array EmissionPoints`
- `Vector3 EmissionRingAxis`
- `float EmissionRingConeAngle`
- `float EmissionRingHeight`
- `float EmissionRingInnerRadius`
- `float EmissionRingRadius`

**Methods**
- `AABB CaptureAabb()`
- `void ConvertFromParticles(Node particles)`
- `Curve GetParamCurve(Parameter param)`
- `float GetParamMax(Parameter param)`
- `float GetParamMin(Parameter param)`
- `bool GetParticleFlag(ParticleFlags particleFlag)`
- `void RequestParticlesProcess(float processTime)`
- `void Restart(bool keepSeed = false)`
- `void SetParamCurve(Parameter param, Curve curve)`
- `void SetParamMax(Parameter param, float value)`
- `void SetParamMin(Parameter param, float value)`
- `void SetParticleFlag(ParticleFlags particleFlag, bool enable)`

### CSGBox3D
*Inherits: **CSGPrimitive3D < CSGShape3D < GeometryInstance3D < VisualInstance3D < Node3D < Node < Object***

This node allows you to create a box for use with the CSG system.

**Properties**
- `Material Material`
- `Vector3 Size` = `Vector3(1, 1, 1)`

### CSGCombiner3D
*Inherits: **CSGShape3D < GeometryInstance3D < VisualInstance3D < Node3D < Node < Object***

For complex arrangements of shapes, it is sometimes needed to add structure to your CSG nodes. The CSGCombiner3D node allows you to create this structure. The node encapsulates the result of the CSG operations of its children. In this way, it is possible to do operations on one set of shapes that are children of one CSGCombiner3D node, and a set of separate operations on a second set of shapes that are children of a second CSGCombiner3D node, and then do an operation that takes the two end results as its input to create the final shape.

### CSGCylinder3D
*Inherits: **CSGPrimitive3D < CSGShape3D < GeometryInstance3D < VisualInstance3D < Node3D < Node < Object***

This node allows you to create a cylinder (or cone) for use with the CSG system.

**Properties**
- `bool Cone` = `false`
- `float Height` = `2.0`
- `Material Material`
- `float Radius` = `0.5`
- `int Sides` = `8`
- `bool SmoothFaces` = `true`

### CSGMesh3D
*Inherits: **CSGPrimitive3D < CSGShape3D < GeometryInstance3D < VisualInstance3D < Node3D < Node < Object***

This CSG node allows you to use any mesh resource as a CSG shape, provided it is manifold. A manifold shape is closed, does not self-intersect, does not contain internal faces and has no edges that connect to more than two faces. See also CSGPolygon3D for drawing 2D extruded polygons to be used as CSG nodes.

**Properties**
- `Material Material`
- `Mesh Mesh`

### CSGPolygon3D
*Inherits: **CSGPrimitive3D < CSGShape3D < GeometryInstance3D < VisualInstance3D < Node3D < Node < Object***

An array of 2D points is extruded to quickly and easily create a variety of 3D meshes. See also CSGMesh3D for using 3D meshes as CSG nodes.

**Properties**
- `float Depth` = `1.0`
- `Material Material`
- `Mode Mode` = `0`
- `bool PathContinuousU`
- `float PathInterval`
- `PathIntervalType PathIntervalType`
- `bool PathJoined`
- `bool PathLocal`
- `NodePath PathNode`
- `PathRotation PathRotation`
- `bool PathRotationAccurate`
- `float PathSimplifyAngle`
- `float PathUDistance`
- `PackedVector2Array Polygon` = `PackedVector2Array(0, 0, 0, 1, 1, 1, 1, 0)`
- `bool SmoothFaces` = `false`
- `float SpinDegrees`
- `int SpinSides`

### CSGPrimitive3D
*Inherits: **CSGShape3D < GeometryInstance3D < VisualInstance3D < Node3D < Node < Object** | Inherited by: CSGBox3D, CSGCylinder3D, CSGMesh3D, CSGPolygon3D, CSGSphere3D, CSGTorus3D*

Parent class for various CSG primitives. It contains code and functionality that is common between them. It cannot be used directly. Instead use one of the various classes that inherit from it.

**Properties**
- `bool FlipFaces` = `false`

### CSGShape3D
*Inherits: **GeometryInstance3D < VisualInstance3D < Node3D < Node < Object** | Inherited by: CSGCombiner3D, CSGPrimitive3D*

This is the CSG base class that provides CSG operation support to the various CSG nodes in Godot.

**Properties**
- `bool CalculateTangents` = `true`
- `int CollisionLayer` = `1`
- `int CollisionMask` = `1`
- `float CollisionPriority` = `1.0`
- `Operation Operation` = `0`
- `float Snap`
- `bool UseCollision` = `false`

**Methods**
- `ConcavePolygonShape3D BakeCollisionShape()`
- `ArrayMesh BakeStaticMesh()`
- `bool GetCollisionLayerValue(int layerNumber)`
- `bool GetCollisionMaskValue(int layerNumber)`
- `Godot.Collections.Array GetMeshes()`
- `bool IsRootShape()`
- `void SetCollisionLayerValue(int layerNumber, bool value)`
- `void SetCollisionMaskValue(int layerNumber, bool value)`

### CSGSphere3D
*Inherits: **CSGPrimitive3D < CSGShape3D < GeometryInstance3D < VisualInstance3D < Node3D < Node < Object***

This node allows you to create a sphere for use with the CSG system.

**Properties**
- `Material Material`
- `int RadialSegments` = `12`
- `float Radius` = `0.5`
- `int Rings` = `6`
- `bool SmoothFaces` = `true`

### CSGTorus3D
*Inherits: **CSGPrimitive3D < CSGShape3D < GeometryInstance3D < VisualInstance3D < Node3D < Node < Object***

This node allows you to create a torus for use with the CSG system.

**Properties**
- `float InnerRadius` = `0.5`
- `Material Material`
- `float OuterRadius` = `1.0`
- `int RingSides` = `6`
- `int Sides` = `8`
- `bool SmoothFaces` = `true`

### Callable

Callable is a built-in Variant type that represents a function. It can either be a method within an Object instance, or a custom callable used for different purposes (see is_custom()). Like all Variant types, it can be stored in variables and passed to other functions. It is most commonly used for signal callbacks.

**Methods**
- `Callable Bind()`
- `Callable Bindv(Godot.Collections.Array arguments)`
- `Variant Call()`
- `void CallDeferred()`
- `Variant Callv(Godot.Collections.Array arguments)`
- `Callable Create(Variant variant, StringName method) [static]`
- `int GetArgumentCount()`
- `Godot.Collections.Array GetBoundArguments()`
- `int GetBoundArgumentsCount()`
- `StringName GetMethod()`
- `Object GetObject()`
- `int GetObjectId()`
- `int GetUnboundArgumentsCount()`
- `int Hash()`
- `bool IsCustom()`
- `bool IsNull()`
- `bool IsStandard()`
- `bool IsValid()`
- `void Rpc()`
- `void RpcId(int peerId)`
- `Callable Unbind(int argcount)`

**C# Examples**
```csharp
// Default parameter values are not supported.
public void PrintArgs(Variant arg1, Variant arg2, Variant arg3 = default)
{
    GD.PrintS(arg1, arg2, arg3);
}

public void Test()
{
    // Invalid calls fail silently.
    Callable callable = new Callable(this, MethodName.PrintArgs);
    callable.Call("hello", "world"); // Default parameter values are not supported, should have 3 arguments.
    callable.Call(Vector2.Up, 42, callable); // Prints "(0, -1) 42 Node(Node.cs)::PrintArgs"
    callable.Call("invalid"); // Invalid call, should have 3 arguments.
}
```
```csharp
public override void _Ready()
{
    Callable.From(GrabFocus).CallDeferred();
}
```

### CameraFeed
*Inherits: **RefCounted < Object***

A camera feed gives you access to a single physical camera attached to your device. When enabled, Godot will start capturing frames from the camera which can then be used. See also CameraServer.

**Properties**
- `bool FeedIsActive` = `false`
- `Transform2D FeedTransform` = `Transform2D(1, 0, 0, -1, 0, 1)`
- `Godot.Collections.Array Formats` = `[]`

**Methods**
- `bool _ActivateFeed() [virtual]`
- `void _DeactivateFeed() [virtual]`
- `FeedDataType GetDatatype()`
- `int GetId()`
- `string GetName()`
- `FeedPosition GetPosition()`
- `int GetTextureTexId(FeedImage feedImageType)`
- `void SetExternal(int width, int height)`
- `bool SetFormat(int index, Godot.Collections.Dictionary parameters)`
- `void SetName(string name)`
- `void SetPosition(FeedPosition position)`
- `void SetRgbImage(Image rgbImage)`
- `void SetYcbcrImage(Image ycbcrImage)`
- `void SetYcbcrImages(Image yImage, Image cbcrImage)`

### CameraServer
*Inherits: **Object***

The CameraServer keeps track of different cameras accessible in Godot. These are external cameras such as webcams or the cameras on your phone.

**Properties**
- `bool MonitoringFeeds` = `false`

**Methods**
- `void AddFeed(CameraFeed feed)`
- `Array[CameraFeed] Feeds()`
- `CameraFeed GetFeed(int index)`
- `int GetFeedCount()`
- `void RemoveFeed(CameraFeed feed)`

**C# Examples**
```csharp
public override void _Ready()
{
    CameraServer.CameraFeedsUpdated += OnCameraFeedsUpdated;
    CameraServer.MonitoringFeeds = true;
}

void OnCameraFeedsUpdated()
{
    var feeds = CameraServer.Feeds();
}
```

### CanvasGroup
*Inherits: **Node2D < CanvasItem < Node < Object***

Child CanvasItem nodes of a CanvasGroup are drawn as a single object. It allows to e.g. draw overlapping translucent 2D nodes without causing the overlapping sections to be more opaque than intended (set the CanvasItem.self_modulate property on the CanvasGroup to achieve this effect).

**Properties**
- `float ClearMargin` = `10.0`
- `float FitMargin` = `10.0`
- `bool UseMipmaps` = `false`

### CanvasTexture
*Inherits: **Texture2D < Texture < Resource < RefCounted < Object***

CanvasTexture is an alternative to ImageTexture for 2D rendering. It allows using normal maps and specular maps in any node that inherits from CanvasItem. CanvasTexture also allows overriding the texture's filter and repeat mode independently of the node's properties (or the project settings).

**Properties**
- `Texture2D DiffuseTexture`
- `Texture2D NormalTexture`
- `bool ResourceLocalToScene` = `false (overrides Resource)`
- `Color SpecularColor` = `Color(1, 1, 1, 1)`
- `float SpecularShininess` = `1.0`
- `Texture2D SpecularTexture`
- `TextureFilter TextureFilter` = `0`
- `TextureRepeat TextureRepeat` = `0`

### CapsuleShape2D
*Inherits: **Shape2D < Resource < RefCounted < Object***

A 2D capsule shape, intended for use in physics. Usually used to provide a shape for a CollisionShape2D.

**Properties**
- `float Height` = `30.0`
- `float MidHeight`
- `float Radius` = `10.0`

### CapsuleShape3D
*Inherits: **Shape3D < Resource < RefCounted < Object***

A 3D capsule shape, intended for use in physics. Usually used to provide a shape for a CollisionShape3D.

**Properties**
- `float Height` = `2.0`
- `float MidHeight`
- `float Radius` = `0.5`

### ChainIK3D
*Inherits: **IKModifier3D < SkeletonModifier3D < Node3D < Node < Object** | Inherited by: IterateIK3D, SplineIK3D*

Base class of SkeletonModifier3D that automatically generates a joint list from the bones between the root bone and the end bone.

**Methods**
- `int GetEndBone(int index)`
- `BoneDirection GetEndBoneDirection(int index)`
- `float GetEndBoneLength(int index)`
- `string GetEndBoneName(int index)`
- `int GetJointBone(int index, int joint)`
- `string GetJointBoneName(int index, int joint)`
- `int GetJointCount(int index)`
- `int GetRootBone(int index)`
- `string GetRootBoneName(int index)`
- `bool IsEndBoneExtended(int index)`
- `void SetEndBone(int index, int bone)`
- `void SetEndBoneDirection(int index, BoneDirection boneDirection)`
- `void SetEndBoneLength(int index, float length)`
- `void SetEndBoneName(int index, string boneName)`
- `void SetExtendEndBone(int index, bool enabled)`
- `void SetRootBone(int index, int bone)`
- `void SetRootBoneName(int index, string boneName)`

### CharFXTransform
*Inherits: **RefCounted < Object***

By setting various properties on this object, you can control how individual characters will be displayed in a RichTextEffect.

**Properties**
- `Color Color` = `Color(0, 0, 0, 1)`
- `float ElapsedTime` = `0.0`
- `Godot.Collections.Dictionary Env` = `{}`
- `RID Font` = `RID()`
- `int GlyphCount` = `0`
- `int GlyphFlags` = `0`
- `int GlyphIndex` = `0`
- `Vector2 Offset` = `Vector2(0, 0)`
- `bool Outline` = `false`
- `Vector2i Range` = `Vector2i(0, 0)`
- `int RelativeIndex` = `0`
- `Transform2D Transform` = `Transform2D(1, 0, 0, 1, 0, 0)`
- `bool Visible` = `true`

### CircleShape2D
*Inherits: **Shape2D < Resource < RefCounted < Object***

A 2D circle shape, intended for use in physics. Usually used to provide a shape for a CollisionShape2D.

**Properties**
- `float Radius` = `10.0`

### CodeHighlighter
*Inherits: **SyntaxHighlighter < Resource < RefCounted < Object***

By adjusting various properties of this resource, you can change the colors of strings, comments, numbers, and other text patterns inside a TextEdit control.

**Properties**
- `Godot.Collections.Dictionary ColorRegions` = `{}`
- `Color FunctionColor` = `Color(0, 0, 0, 1)`
- `Godot.Collections.Dictionary KeywordColors` = `{}`
- `Godot.Collections.Dictionary MemberKeywordColors` = `{}`
- `Color MemberVariableColor` = `Color(0, 0, 0, 1)`
- `Color NumberColor` = `Color(0, 0, 0, 1)`
- `Color SymbolColor` = `Color(0, 0, 0, 1)`

**Methods**
- `void AddColorRegion(string startKey, string endKey, Color color, bool lineOnly = false)`
- `void AddKeywordColor(string keyword, Color color)`
- `void AddMemberKeywordColor(string memberKeyword, Color color)`
- `void ClearColorRegions()`
- `void ClearKeywordColors()`
- `void ClearMemberKeywordColors()`
- `Color GetKeywordColor(string keyword)`
- `Color GetMemberKeywordColor(string memberKeyword)`
- `bool HasColorRegion(string startKey)`
- `bool HasKeywordColor(string keyword)`
- `bool HasMemberKeywordColor(string memberKeyword)`
- `void RemoveColorRegion(string startKey)`
- `void RemoveKeywordColor(string keyword)`
- `void RemoveMemberKeywordColor(string memberKeyword)`

### CollisionObject3D
*Inherits: **Node3D < Node < Object** | Inherited by: Area3D, PhysicsBody3D*

Abstract base class for 3D physics objects. CollisionObject3D can hold any number of Shape3Ds for collision. Each shape must be assigned to a shape owner. Shape owners are not nodes and do not appear in the editor, but are accessible through code using the shape_owner_* methods.

**Properties**
- `int CollisionLayer` = `1`
- `int CollisionMask` = `1`
- `float CollisionPriority` = `1.0`
- `DisableMode DisableMode` = `0`
- `bool InputCaptureOnDrag` = `false`
- `bool InputRayPickable` = `true`

**Methods**
- `void _InputEvent(Camera3D camera, InputEvent event, Vector3 eventPosition, Vector3 normal, int shapeIdx) [virtual]`
- `void _MouseEnter() [virtual]`
- `void _MouseExit() [virtual]`
- `int CreateShapeOwner(Object owner)`
- `bool GetCollisionLayerValue(int layerNumber)`
- `bool GetCollisionMaskValue(int layerNumber)`
- `RID GetRid()`
- `PackedInt32Array GetShapeOwners()`
- `bool IsShapeOwnerDisabled(int ownerId)`
- `void RemoveShapeOwner(int ownerId)`
- `void SetCollisionLayerValue(int layerNumber, bool value)`
- `void SetCollisionMaskValue(int layerNumber, bool value)`
- `int ShapeFindOwner(int shapeIndex)`
- `void ShapeOwnerAddShape(int ownerId, Shape3D shape)`
- `void ShapeOwnerClearShapes(int ownerId)`
- `Object ShapeOwnerGetOwner(int ownerId)`
- `Shape3D ShapeOwnerGetShape(int ownerId, int shapeId)`
- `int ShapeOwnerGetShapeCount(int ownerId)`
- `int ShapeOwnerGetShapeIndex(int ownerId, int shapeId)`
- `Transform3D ShapeOwnerGetTransform(int ownerId)`
- `void ShapeOwnerRemoveShape(int ownerId, int shapeId)`
- `void ShapeOwnerSetDisabled(int ownerId, bool disabled)`
- `void ShapeOwnerSetTransform(int ownerId, Transform3D transform)`

### ColorPalette
*Inherits: **Resource < RefCounted < Object***

The ColorPalette resource is designed to store and manage a collection of colors. This resource is useful in scenarios where a predefined set of colors is required, such as for creating themes, designing user interfaces, or managing game assets. The built-in ColorPicker control can also make use of ColorPalette without additional code.

**Properties**
- `PackedColorArray Colors` = `PackedColorArray()`

### Color

A color represented in RGBA format by a red (r), green (g), blue (b), and alpha (a) component. Each component is a 32-bit floating-point value, usually ranging from 0.0 to 1.0. Some properties (such as CanvasItem.modulate) may support values greater than 1.0, for overbright or HDR (High Dynamic Range) colors.

**Properties**
- `float A` = `1.0`
- `int A8` = `255`
- `float B` = `0.0`
- `int B8` = `0`
- `float G` = `0.0`
- `int G8` = `0`
- `float H` = `0.0`
- `float OkHslH` = `0.0`
- `float OkHslL` = `0.0`
- `float OkHslS` = `0.0`
- `float R` = `0.0`
- `int R8` = `0`
- `float S` = `0.0`
- `float V` = `0.0`

**Methods**
- `Color Blend(Color over)`
- `Color Clamp(Color min = Color(0, 0, 0, 0), Color max = Color(1, 1, 1, 1))`
- `Color Darkened(float amount)`
- `Color FromHsv(float h, float s, float v, float alpha = 1.0) [static]`
- `Color FromOkHsl(float h, float s, float l, float alpha = 1.0) [static]`
- `Color FromRgba8(int r8, int g8, int b8, int a8 = 255) [static]`
- `Color FromRgbe9995(int rgbe) [static]`
- `Color FromString(string str, Color default) [static]`
- `float GetLuminance()`
- `Color Hex(int hex) [static]`
- `Color Hex64(int hex) [static]`
- `Color Html(string rgba) [static]`
- `bool HtmlIsValid(string color) [static]`
- `Color Inverted()`
- `bool IsEqualApprox(Color to)`
- `Color Lerp(Color to, float weight)`
- `Color Lightened(float amount)`
- `Color LinearToSrgb()`
- `Color SrgbToLinear()`
- `int ToAbgr32()`
- `int ToAbgr64()`
- `int ToArgb32()`
- `int ToArgb64()`
- `string ToHtml(bool withAlpha = true)`
- `int ToRgba32()`
- `int ToRgba64()`

**C# Examples**
```csharp
var red = new Color(Colors.Red, 0.2f); // 20% opaque red.
```
```csharp
var color = new Color(0.2f, 1.0f, 0.7f); // Similar to `Color.Color8(51, 255, 178, 255)`
```

### CompressedCubemapArray
*Inherits: **CompressedTextureLayered < TextureLayered < Texture < Resource < RefCounted < Object***

A cubemap array that is loaded from a .ccubearray file. This file format is internal to Godot; it is created by importing other image formats with the import system. CompressedCubemapArray can use one of 4 compression methods:

### CompressedCubemap
*Inherits: **CompressedTextureLayered < TextureLayered < Texture < Resource < RefCounted < Object***

A cubemap that is loaded from a .ccube file. This file format is internal to Godot; it is created by importing other image formats with the import system. CompressedCubemap can use one of 4 compression methods:

### CompressedTexture3D
*Inherits: **Texture3D < Texture < Resource < RefCounted < Object***

CompressedTexture3D is the VRAM-compressed counterpart of ImageTexture3D. The file extension for CompressedTexture3D files is .ctex3d. This file format is internal to Godot; it is created by importing other image formats with the import system.

**Properties**
- `string LoadPath` = `""`

**Methods**
- `Error Load(string path)`

### CompressedTextureLayered
*Inherits: **TextureLayered < Texture < Resource < RefCounted < Object** | Inherited by: CompressedCubemap, CompressedCubemapArray, CompressedTexture2DArray*

Base class for CompressedTexture2DArray and CompressedTexture3D. Cannot be used directly, but contains all the functions necessary for accessing the derived resource types. See also TextureLayered.

**Properties**
- `string LoadPath` = `""`

**Methods**
- `Error Load(string path)`

### ConcavePolygonShape2D
*Inherits: **Shape2D < Resource < RefCounted < Object***

A 2D polyline shape, intended for use in physics. Used internally in CollisionPolygon2D when it's in CollisionPolygon2D.BUILD_SEGMENTS mode.

**Properties**
- `PackedVector2Array Segments` = `PackedVector2Array()`

### ConcavePolygonShape3D
*Inherits: **Shape3D < Resource < RefCounted < Object***

A 3D trimesh shape, intended for use in physics. Usually used to provide a shape for a CollisionShape3D.

**Properties**
- `bool BackfaceCollision` = `false`

**Methods**
- `PackedVector3Array GetFaces()`
- `void SetFaces(PackedVector3Array faces)`

### ConvertTransformModifier3D
*Inherits: **BoneConstraint3D < SkeletonModifier3D < Node3D < Node < Object***

Apply the copied transform of the bone set by BoneConstraint3D.set_reference_bone() to the bone set by BoneConstraint3D.set_apply_bone() about the specific axis with remapping it with some options.

**Properties**
- `int SettingCount` = `0`

**Methods**
- `Axis GetApplyAxis(int index)`
- `float GetApplyRangeMax(int index)`
- `float GetApplyRangeMin(int index)`
- `TransformMode GetApplyTransformMode(int index)`
- `Axis GetReferenceAxis(int index)`
- `float GetReferenceRangeMax(int index)`
- `float GetReferenceRangeMin(int index)`
- `TransformMode GetReferenceTransformMode(int index)`
- `bool IsAdditive(int index)`
- `bool IsRelative(int index)`
- `void SetAdditive(int index, bool enabled)`
- `void SetApplyAxis(int index, Axis axis)`
- `void SetApplyRangeMax(int index, float rangeMax)`
- `void SetApplyRangeMin(int index, float rangeMin)`
- `void SetApplyTransformMode(int index, TransformMode transformMode)`
- `void SetReferenceAxis(int index, Axis axis)`
- `void SetReferenceRangeMax(int index, float rangeMax)`
- `void SetReferenceRangeMin(int index, float rangeMin)`
- `void SetReferenceTransformMode(int index, TransformMode transformMode)`
- `void SetRelative(int index, bool enabled)`

### ConvexPolygonShape2D
*Inherits: **Shape2D < Resource < RefCounted < Object***

A 2D convex polygon shape, intended for use in physics. Used internally in CollisionPolygon2D when it's in CollisionPolygon2D.BUILD_SOLIDS mode.

**Properties**
- `PackedVector2Array Points` = `PackedVector2Array()`

**Methods**
- `void SetPointCloud(PackedVector2Array pointCloud)`

### ConvexPolygonShape3D
*Inherits: **Shape3D < Resource < RefCounted < Object***

A 3D convex polyhedron shape, intended for use in physics. Usually used to provide a shape for a CollisionShape3D.

**Properties**
- `PackedVector3Array Points` = `PackedVector3Array()`

### CopyTransformModifier3D
*Inherits: **BoneConstraint3D < SkeletonModifier3D < Node3D < Node < Object***

Apply the copied transform of the bone set by BoneConstraint3D.set_reference_bone() to the bone set by BoneConstraint3D.set_apply_bone() with processing it with some masks and options.

**Properties**
- `int SettingCount` = `0`

**Methods**
- `BitField[AxisFlag] GetAxisFlags(int index)`
- `BitField[TransformFlag] GetCopyFlags(int index)`
- `BitField[AxisFlag] GetInvertFlags(int index)`
- `bool IsAdditive(int index)`
- `bool IsAxisXEnabled(int index)`
- `bool IsAxisXInverted(int index)`
- `bool IsAxisYEnabled(int index)`
- `bool IsAxisYInverted(int index)`
- `bool IsAxisZEnabled(int index)`
- `bool IsAxisZInverted(int index)`
- `bool IsPositionCopying(int index)`
- `bool IsRelative(int index)`
- `bool IsRotationCopying(int index)`
- `bool IsScaleCopying(int index)`
- `void SetAdditive(int index, bool enabled)`
- `void SetAxisFlags(int index, BitField[AxisFlag] axisFlags)`
- `void SetAxisXEnabled(int index, bool enabled)`
- `void SetAxisXInverted(int index, bool enabled)`
- `void SetAxisYEnabled(int index, bool enabled)`
- `void SetAxisYInverted(int index, bool enabled)`
- `void SetAxisZEnabled(int index, bool enabled)`
- `void SetAxisZInverted(int index, bool enabled)`
- `void SetCopyFlags(int index, BitField[TransformFlag] copyFlags)`
- `void SetCopyPosition(int index, bool enabled)`
- `void SetCopyRotation(int index, bool enabled)`
- `void SetCopyScale(int index, bool enabled)`
- `void SetInvertFlags(int index, BitField[AxisFlag] axisFlags)`
- `void SetRelative(int index, bool enabled)`

### CubemapArray
*Inherits: **ImageTextureLayered < TextureLayered < Texture < Resource < RefCounted < Object***

CubemapArrays are made of an array of Cubemaps. Like Cubemaps, they are made of multiple textures, the amount of which must be divisible by 6 (one for each face of the cube).

**Methods**
- `Resource CreatePlaceholder()`

### Cubemap
*Inherits: **ImageTextureLayered < TextureLayered < Texture < Resource < RefCounted < Object***

A cubemap is made of 6 textures organized in layers. They are typically used for faking reflections in 3D rendering (see ReflectionProbe). It can be used to make an object look as if it's reflecting its surroundings. This usually delivers much better performance than other reflection methods.

**Methods**
- `Resource CreatePlaceholder()`

### CurveTexture
*Inherits: **Texture2D < Texture < Resource < RefCounted < Object***

A 1D texture where pixel brightness corresponds to points on a unit Curve resource, either in grayscale or in red. This visual representation simplifies the task of saving curves as image files.

**Properties**
- `Curve Curve`
- `bool ResourceLocalToScene` = `false (overrides Resource)`
- `TextureMode TextureMode` = `0`
- `int Width` = `256`

### CurveXYZTexture
*Inherits: **Texture2D < Texture < Resource < RefCounted < Object***

A 1D texture where the red, green, and blue color channels correspond to points on 3 unit Curve resources. Compared to using separate CurveTextures, this further simplifies the task of saving curves as image files.

**Properties**
- `Curve CurveX`
- `Curve CurveY`
- `Curve CurveZ`
- `bool ResourceLocalToScene` = `false (overrides Resource)`
- `int Width` = `256`

### Curve
*Inherits: **Resource < RefCounted < Object***

This resource describes a mathematical curve by defining a set of points and tangents at each point. By default, it ranges between 0 and 1 on the X and Y axes, but these ranges can be changed.

**Properties**
- `int BakeResolution` = `100`
- `float MaxDomain` = `1.0`
- `float MaxValue` = `1.0`
- `float MinDomain` = `0.0`
- `float MinValue` = `0.0`
- `int PointCount` = `0`

**Methods**
- `int AddPoint(Vector2 position, float leftTangent = 0, float rightTangent = 0, TangentMode leftMode = 0, TangentMode rightMode = 0)`
- `void Bake()`
- `void CleanDupes()`
- `void ClearPoints()`
- `float GetDomainRange()`
- `TangentMode GetPointLeftMode(int index)`
- `float GetPointLeftTangent(int index)`
- `Vector2 GetPointPosition(int index)`
- `TangentMode GetPointRightMode(int index)`
- `float GetPointRightTangent(int index)`
- `float GetValueRange()`
- `void RemovePoint(int index)`
- `float Sample(float offset)`
- `float SampleBaked(float offset)`
- `void SetPointLeftMode(int index, TangentMode mode)`
- `void SetPointLeftTangent(int index, float tangent)`
- `int SetPointOffset(int index, float offset)`
- `void SetPointRightMode(int index, TangentMode mode)`
- `void SetPointRightTangent(int index, float tangent)`
- `void SetPointValue(int index, float y)`

### CylinderShape3D
*Inherits: **Shape3D < Resource < RefCounted < Object***

A 3D cylinder shape, intended for use in physics. Usually used to provide a shape for a CollisionShape3D.

**Properties**
- `float Height` = `2.0`
- `float Radius` = `0.5`

### DPITexture
*Inherits: **Texture2D < Texture < Resource < RefCounted < Object***

An automatically scalable Texture2D based on an SVG image. DPITextures are used to automatically re-rasterize icons and other texture based UI theme elements to match viewport scale and font oversampling. See also ProjectSettings.display/window/stretch/mode ("canvas_items" mode) and Viewport.oversampling_override.

**Properties**
- `float BaseScale` = `1.0`
- `Godot.Collections.Dictionary ColorMap` = `{}`
- `bool ResourceLocalToScene` = `false (overrides Resource)`
- `float Saturation` = `1.0`

**Methods**
- `DPITexture CreateFromString(string source, float scale = 1.0, float saturation = 1.0, Godot.Collections.Dictionary colorMap = {}) [static]`
- `RID GetScaledRid()`
- `string GetSource()`
- `void SetSizeOverride(Vector2i size)`
- `void SetSource(string source)`

### Decal
*Inherits: **VisualInstance3D < Node3D < Node < Object***

Decals are used to project a texture onto a Mesh in the scene. Use Decals to add detail to a scene without affecting the underlying Mesh. They are often used to add weathering to building, add dirt or mud to the ground, or add variety to props. Decals can be moved at any time, making them suitable for things like blob shadows or laser sight dots.

**Properties**
- `float AlbedoMix` = `1.0`
- `int CullMask` = `1048575`
- `float DistanceFadeBegin` = `40.0`
- `bool DistanceFadeEnabled` = `false`
- `float DistanceFadeLength` = `10.0`
- `float EmissionEnergy` = `1.0`
- `float LowerFade` = `0.3`
- `Color Modulate` = `Color(1, 1, 1, 1)`
- `float NormalFade` = `0.0`
- `Vector3 Size` = `Vector3(2, 2, 2)`
- `Texture2D TextureAlbedo`
- `Texture2D TextureEmission`
- `Texture2D TextureNormal`
- `Texture2D TextureOrm`
- `float UpperFade` = `0.3`

**Methods**
- `Texture2D GetTexture(DecalTexture type)`
- `void SetTexture(DecalTexture type, Texture2D texture)`

**C# Examples**
```csharp
for (int i = 0; i < (int)Decal.DecalTexture.Max; i++)
{
    GetNode<Decal>("NewDecal").SetTexture(i, GetNode<Decal>("OldDecal").GetTexture(i));
}
```
```csharp
for (int i = 0; i < (int)Decal.DecalTexture.Max; i++)
{
    GetNode<Decal>("NewDecal").SetTexture(i, GetNode<Decal>("OldDecal").GetTexture(i));
}
```

### Dictionary

Dictionaries are associative containers that contain values referenced by unique keys. Dictionaries will preserve the insertion order when adding new entries. In other programming languages, this data structure is often referred to as a hash map or an associative array.

**Methods**
- `void Assign(Godot.Collections.Dictionary dictionary)`
- `void Clear()`
- `Godot.Collections.Dictionary Duplicate(bool deep = false)`
- `Godot.Collections.Dictionary DuplicateDeep(int deepSubresourcesMode = 1)`
- `bool Erase(Variant key)`
- `Variant FindKey(Variant value)`
- `Variant Get(Variant key, Variant default = null)`
- `Variant GetOrAdd(Variant key, Variant default = null)`
- `int GetTypedKeyBuiltin()`
- `StringName GetTypedKeyClassName()`
- `Variant GetTypedKeyScript()`
- `int GetTypedValueBuiltin()`
- `StringName GetTypedValueClassName()`
- `Variant GetTypedValueScript()`
- `bool Has(Variant key)`
- `bool HasAll(Godot.Collections.Array keys)`
- `int Hash()`
- `bool IsEmpty()`
- `bool IsReadOnly()`
- `bool IsSameTyped(Godot.Collections.Dictionary dictionary)`
- `bool IsSameTypedKey(Godot.Collections.Dictionary dictionary)`
- `bool IsSameTypedValue(Godot.Collections.Dictionary dictionary)`
- `bool IsTyped()`
- `bool IsTypedKey()`
- `bool IsTypedValue()`
- `Godot.Collections.Array Keys()`
- `void MakeReadOnly()`
- `void Merge(Godot.Collections.Dictionary dictionary, bool overwrite = false)`
- `Godot.Collections.Dictionary Merged(Godot.Collections.Dictionary dictionary, bool overwrite = false)`
- `bool RecursiveEqual(Godot.Collections.Dictionary dictionary, int recursionCount)`
- `bool Set(Variant key, Variant value)`
- `int Size()`
- `void Sort()`
- `Godot.Collections.Array Values()`

**C# Examples**
```csharp
var myDict = new Godot.Collections.Dictionary(); // Creates an empty dictionary.
var pointsDict = new Godot.Collections.Dictionary
{
    { "White", 50 },
    { "Yellow", 75 },
    { "Orange", 100 },
};
```
```csharp
[Export(PropertyHint.Enum, "White,Yellow,Orange")]
public string MyColor { get; set; }
private Godot.Collections.Dictionary _pointsDict = new Godot.Collections.Dictionary
{
    { "White", 50 },
    { "Yellow", 75 },
    { "Orange", 100 },
};

public override void _Ready()
{
    int points = (int)_pointsDict[MyColor];
}
```

### DirectionalLight2D
*Inherits: **Light2D < Node2D < CanvasItem < Node < Object***

A directional light is a type of Light2D node that models an infinite number of parallel rays covering the entire scene. It is used for lights with strong intensity that are located far away from the scene (for example: to model sunlight or moonlight).

**Properties**
- `float Height` = `0.0`
- `float MaxDistance` = `10000.0`

### DisplayServer
*Inherits: **Object***

DisplayServer handles everything related to window management. It is separated from OS as a single operating system may support multiple display servers.

**Methods**
- `RID AccessibilityCreateElement(int windowId, AccessibilityRole role)`
- `RID AccessibilityCreateSubElement(RID parentRid, AccessibilityRole role, int insertPos = -1)`
- `RID AccessibilityCreateSubTextEditElements(RID parentRid, RID shapedText, float minHeight, int insertPos = -1, bool isLastLine = false)`
- `Variant AccessibilityElementGetMeta(RID id)`
- `void AccessibilityElementSetMeta(RID id, Variant meta)`
- `void AccessibilityFreeElement(RID id)`
- `RID AccessibilityGetWindowRoot(int windowId)`
- `bool AccessibilityHasElement(RID id)`
- `int AccessibilityScreenReaderActive()`
- `void AccessibilitySetWindowFocused(int windowId, bool focused)`
- `void AccessibilitySetWindowRect(int windowId, Rect2 rectOut, Rect2 rectIn)`
- `int AccessibilityShouldIncreaseContrast()`
- `int AccessibilityShouldReduceAnimation()`
- `int AccessibilityShouldReduceTransparency()`
- `void AccessibilityUpdateAddAction(RID id, AccessibilityAction action, Callable callable)`
- `void AccessibilityUpdateAddChild(RID id, RID childId)`
- `void AccessibilityUpdateAddCustomAction(RID id, int actionId, string actionDescription)`
- `void AccessibilityUpdateAddRelatedControls(RID id, RID relatedId)`
- `void AccessibilityUpdateAddRelatedDescribedBy(RID id, RID relatedId)`
- `void AccessibilityUpdateAddRelatedDetails(RID id, RID relatedId)`
- `void AccessibilityUpdateAddRelatedFlowTo(RID id, RID relatedId)`
- `void AccessibilityUpdateAddRelatedLabeledBy(RID id, RID relatedId)`
- `void AccessibilityUpdateAddRelatedRadioGroup(RID id, RID relatedId)`
- `void AccessibilityUpdateSetActiveDescendant(RID id, RID otherId)`
- `void AccessibilityUpdateSetBackgroundColor(RID id, Color color)`
- `void AccessibilityUpdateSetBounds(RID id, Rect2 pRect)`
- `void AccessibilityUpdateSetChecked(RID id, bool checekd)`
- `void AccessibilityUpdateSetClassname(RID id, string classname)`
- `void AccessibilityUpdateSetColorValue(RID id, Color color)`
- `void AccessibilityUpdateSetDescription(RID id, string description)`
- `void AccessibilityUpdateSetErrorMessage(RID id, RID otherId)`
- `void AccessibilityUpdateSetExtraInfo(RID id, string name)`
- `void AccessibilityUpdateSetFlag(RID id, AccessibilityFlags flag, bool value)`
- `void AccessibilityUpdateSetFocus(RID id)`
- `void AccessibilityUpdateSetForegroundColor(RID id, Color color)`
- `void AccessibilityUpdateSetInPageLinkTarget(RID id, RID otherId)`
- `void AccessibilityUpdateSetLanguage(RID id, string language)`
- `void AccessibilityUpdateSetListItemCount(RID id, int size)`
- `void AccessibilityUpdateSetListItemExpanded(RID id, bool expanded)`
- `void AccessibilityUpdateSetListItemIndex(RID id, int index)`

**C# Examples**
```csharp
// Set region, using Path2D node.
DisplayServer.WindowSetMousePassthrough(GetNode<Path2D>("Path2D").Curve.GetBakedPoints());

// Set region, using Polygon2D node.
DisplayServer.WindowSetMousePassthrough(GetNode<Polygon2D>("Polygon2D").Polygon);

// Reset region to default.
DisplayServer.WindowSetMousePassthrough([]);
```

### EncodedObjectAsID
*Inherits: **RefCounted < Object***

Utility class which holds a reference to the internal identifier of an Object instance, as given by Object.get_instance_id(). This ID can then be used to retrieve the object instance with @GlobalScope.instance_from_id().

**Properties**
- `int ObjectId` = `0`

### Expression
*Inherits: **RefCounted < Object***

An expression can be made of any arithmetic operation, built-in math function call, method call of a passed instance, or built-in type construction call.

**Methods**
- `Variant Execute(Godot.Collections.Array inputs = [], Object baseInstance = null, bool showError = true, bool constCallsOnly = false)`
- `string GetErrorText()`
- `bool HasExecuteFailed()`
- `Error Parse(string expression, PackedStringArray inputNames = PackedStringArray())`

**C# Examples**
```csharp
private Expression _expression = new Expression();

public override void _Ready()
{
    GetNode<LineEdit>("LineEdit").TextSubmitted += OnTextEntered;
}

private void OnTextEntered(string command)
{
    Error error = _expression.Parse(command);
    if (error != Error.Ok)
    {
        GD.Print(_expression.GetErrorText());
        return;
    }
    Variant result = _expression.Execute();
    if (!_expression.HasExecuteFailed())
    {
        GetNode<LineEdit>("LineEdit").Text = result.ToString();
    }
}
```

### ExternalTexture
*Inherits: **Texture2D < Texture < Resource < RefCounted < Object***

Displays the content of an external buffer provided by the platform.

**Properties**
- `bool ResourceLocalToScene` = `false (overrides Resource)`
- `Vector2 Size` = `Vector2(256, 256)`

**Methods**
- `int GetExternalTextureId()`
- `void SetExternalBufferId(int externalBufferId)`

### FABRIK3D
*Inherits: **IterateIK3D < ChainIK3D < IKModifier3D < SkeletonModifier3D < Node3D < Node < Object***

FABRIK3D is position based IK, allowing precise and accurate tracking of targets. It's ideal for simple chains without limitations.

### FBXDocument
*Inherits: **GLTFDocument < Resource < RefCounted < Object***

The FBXDocument handles FBX documents. It provides methods to append data from buffers or files, generate scenes, and register/unregister document extensions.

### FBXState
*Inherits: **GLTFState < Resource < RefCounted < Object***

The FBXState handles the state data imported from FBX files.

**Properties**
- `bool AllowGeometryHelperNodes` = `false`

### FileSystemDock
*Inherits: **EditorDock < MarginContainer < Container < Control < CanvasItem < Node < Object***

This class is available only in EditorPlugins and can't be instantiated. You can access it using EditorInterface.get_file_system_dock().

**Methods**
- `void AddResourceTooltipPlugin(EditorResourceTooltipPlugin plugin)`
- `void NavigateToPath(string path)`
- `void RemoveResourceTooltipPlugin(EditorResourceTooltipPlugin plugin)`

### FogMaterial
*Inherits: **Material < Resource < RefCounted < Object***

A Material resource that can be used by FogVolumes to draw volumetric effects.

**Properties**
- `Color Albedo` = `Color(1, 1, 1, 1)`
- `float Density` = `1.0`
- `Texture3D DensityTexture`
- `float EdgeFade` = `0.1`
- `Color Emission` = `Color(0, 0, 0, 1)`
- `float HeightFalloff` = `0.0`

### FoldableContainer
*Inherits: **Container < Control < CanvasItem < Node < Object***

A container that can be expanded/collapsed, with a title that can be filled with controls, such as buttons. This is also called an accordion.

**Properties**
- `FocusMode FocusMode` = `2 (overrides Control)`
- `FoldableGroup FoldableGroup`
- `bool Folded` = `false`
- `string Language` = `""`
- `MouseFilter MouseFilter` = `0 (overrides Control)`
- `string Title` = `""`
- `HorizontalAlignment TitleAlignment` = `0`
- `TitlePosition TitlePosition` = `0`
- `TextDirection TitleTextDirection` = `0`
- `OverrunBehavior TitleTextOverrunBehavior` = `0`

**Methods**
- `void AddTitleBarControl(Control control)`
- `void Expand()`
- `void Fold()`
- `void RemoveTitleBarControl(Control control)`

### FoldableGroup
*Inherits: **Resource < RefCounted < Object***

A group of FoldableContainer-derived nodes. Only one container can be expanded at a time.

**Properties**
- `bool AllowFoldingAll` = `false`
- `bool ResourceLocalToScene` = `true (overrides Resource)`

**Methods**
- `Array[FoldableContainer] GetContainers()`
- `FoldableContainer GetExpandedContainer()`

### Font
*Inherits: **Resource < RefCounted < Object** | Inherited by: FontFile, FontVariation, SystemFont*

Abstract base class for different font types. It has methods for drawing text and font character introspection.

**Properties**
- `Array[Font] Fallbacks` = `[]`

**Methods**
- `float DrawChar(RID canvasItem, Vector2 pos, int char, int fontSize, Color modulate = Color(1, 1, 1, 1), float oversampling = 0.0)`
- `float DrawCharOutline(RID canvasItem, Vector2 pos, int char, int fontSize, int size = -1, Color modulate = Color(1, 1, 1, 1), float oversampling = 0.0)`
- `void DrawMultilineString(RID canvasItem, Vector2 pos, string text, HorizontalAlignment alignment = 0, float width = -1, int fontSize = 16, int maxLines = -1, Color modulate = Color(1, 1, 1, 1), BitField[LineBreakFlag] brkFlags = 3, BitField[JustificationFlag] justificationFlags = 3, Direction direction = 0, Orientation orientation = 0, float oversampling = 0.0)`
- `void DrawMultilineStringOutline(RID canvasItem, Vector2 pos, string text, HorizontalAlignment alignment = 0, float width = -1, int fontSize = 16, int maxLines = -1, int size = 1, Color modulate = Color(1, 1, 1, 1), BitField[LineBreakFlag] brkFlags = 3, BitField[JustificationFlag] justificationFlags = 3, Direction direction = 0, Orientation orientation = 0, float oversampling = 0.0)`
- `void DrawString(RID canvasItem, Vector2 pos, string text, HorizontalAlignment alignment = 0, float width = -1, int fontSize = 16, Color modulate = Color(1, 1, 1, 1), BitField[JustificationFlag] justificationFlags = 3, Direction direction = 0, Orientation orientation = 0, float oversampling = 0.0)`
- `void DrawStringOutline(RID canvasItem, Vector2 pos, string text, HorizontalAlignment alignment = 0, float width = -1, int fontSize = 16, int size = 1, Color modulate = Color(1, 1, 1, 1), BitField[JustificationFlag] justificationFlags = 3, Direction direction = 0, Orientation orientation = 0, float oversampling = 0.0)`
- `RID FindVariation(Godot.Collections.Dictionary variationCoordinates, int faceIndex = 0, float strength = 0.0, Transform2D transform = Transform2D(1, 0, 0, 1, 0, 0), int spacingTop = 0, int spacingBottom = 0, int spacingSpace = 0, int spacingGlyph = 0, float baselineOffset = 0.0)`
- `float GetAscent(int fontSize = 16)`
- `Vector2 GetCharSize(int char, int fontSize)`
- `float GetDescent(int fontSize = 16)`
- `int GetFaceCount()`
- `string GetFontName()`
- `int GetFontStretch()`
- `BitField[FontStyle] GetFontStyle()`
- `string GetFontStyleName()`
- `int GetFontWeight()`
- `float GetHeight(int fontSize = 16)`
- `Vector2 GetMultilineStringSize(string text, HorizontalAlignment alignment = 0, float width = -1, int fontSize = 16, int maxLines = -1, BitField[LineBreakFlag] brkFlags = 3, BitField[JustificationFlag] justificationFlags = 3, Direction direction = 0, Orientation orientation = 0)`
- `Godot.Collections.Dictionary GetOpentypeFeatures()`
- `Godot.Collections.Dictionary GetOtNameStrings()`
- `Array[RID] GetRids()`
- `int GetSpacing(SpacingType spacing)`
- `Vector2 GetStringSize(string text, HorizontalAlignment alignment = 0, float width = -1, int fontSize = 16, BitField[JustificationFlag] justificationFlags = 3, Direction direction = 0, Orientation orientation = 0)`
- `string GetSupportedChars()`
- `Godot.Collections.Dictionary GetSupportedFeatureList()`
- `Godot.Collections.Dictionary GetSupportedVariationList()`
- `float GetUnderlinePosition(int fontSize = 16)`
- `float GetUnderlineThickness(int fontSize = 16)`
- `bool HasChar(int char)`
- `bool IsLanguageSupported(string language)`
- `bool IsScriptSupported(string script)`
- `void SetCacheCapacity(int singleLine, int multiLine)`

**C# Examples**
```csharp
Label label = GetNode<Label>("Label");
Vector2 stringSize = label.GetThemeFont("font").GetStringSize(label.Text, HorizontalAlignment.Left, -1, label.GetThemeFontSize("font_size"));
```

### FramebufferCacheRD
*Inherits: **Object***

Framebuffer cache manager for RenderingDevice-based renderers. Provides a way to create a framebuffer and reuse it in subsequent calls for as long as the used textures exists. Framebuffers will automatically be cleaned up when dependent objects are freed.

**Methods**
- `RID GetCacheMultipass(Array[RID] textures, Array[RDFramebufferPass] passes, int views) [static]`

### GDExtensionManager
*Inherits: **Object***

The GDExtensionManager loads, initializes, and keeps track of all available GDExtension libraries in the project.

**Methods**
- `GDExtension GetExtension(string path)`
- `PackedStringArray GetLoadedExtensions()`
- `bool IsExtensionLoaded(string path)`
- `LoadStatus LoadExtension(string path)`
- `LoadStatus LoadExtensionFromFunction(string path, const GDExtensionInitializationFunction* initFunc)`
- `LoadStatus ReloadExtension(string path)`
- `LoadStatus UnloadExtension(string path)`

### GDExtension
*Inherits: **Resource < RefCounted < Object***

The GDExtension resource type represents a shared library which can expand the functionality of the engine. The GDExtensionManager singleton is responsible for loading, reloading, and unloading GDExtension resources.

**Methods**
- `InitializationLevel GetMinimumLibraryInitializationLevel()`
- `bool IsLibraryOpen()`

### GLTFAccessor
*Inherits: **Resource < RefCounted < Object***

GLTFAccessor is a data structure representing a glTF accessor that would be found in the "accessors" array. A buffer is a blob of binary data. A buffer view is a slice of a buffer. An accessor is a typed interpretation of the data in a buffer view.

**Properties**
- `GLTFAccessorType AccessorType` = `0`
- `int BufferView` = `-1`
- `int ByteOffset` = `0`
- `GLTFComponentType ComponentType` = `0`
- `int Count` = `0`
- `PackedFloat64Array Max` = `PackedFloat64Array()`
- `PackedFloat64Array Min` = `PackedFloat64Array()`
- `bool Normalized` = `false`
- `int SparseCount` = `0`
- `int SparseIndicesBufferView` = `0`
- `int SparseIndicesByteOffset` = `0`
- `GLTFComponentType SparseIndicesComponentType` = `0`
- `int SparseValuesBufferView` = `0`
- `int SparseValuesByteOffset` = `0`
- `int Type`

**Methods**
- `GLTFAccessor FromDictionary(Godot.Collections.Dictionary dictionary) [static]`
- `Godot.Collections.Dictionary ToDictionary()`

### GLTFAnimation
*Inherits: **Resource < RefCounted < Object***

There is currently no description for this class. Please help us by contributing one!

**Properties**
- `bool Loop` = `false`
- `string OriginalName` = `""`

**Methods**
- `Variant GetAdditionalData(StringName extensionName)`
- `void SetAdditionalData(StringName extensionName, Variant additionalData)`

### GLTFBufferView
*Inherits: **Resource < RefCounted < Object***

GLTFBufferView is a data structure representing a glTF bufferView that would be found in the "bufferViews" array. A buffer is a blob of binary data. A buffer view is a slice of a buffer that can be used to identify and extract data from the buffer.

**Properties**
- `int Buffer` = `-1`
- `int ByteLength` = `0`
- `int ByteOffset` = `0`
- `int ByteStride` = `-1`
- `bool Indices` = `false`
- `bool VertexAttributes` = `false`

**Methods**
- `GLTFBufferView FromDictionary(Godot.Collections.Dictionary dictionary) [static]`
- `PackedByteArray LoadBufferViewData(GLTFState state)`
- `Godot.Collections.Dictionary ToDictionary()`

### GLTFCamera
*Inherits: **Resource < RefCounted < Object***

Represents a camera as defined by the base glTF spec.

**Properties**
- `float DepthFar` = `4000.0`
- `float DepthNear` = `0.05`
- `float Fov` = `1.3089969`
- `bool Perspective` = `true`
- `float SizeMag` = `0.5`

**Methods**
- `GLTFCamera FromDictionary(Godot.Collections.Dictionary dictionary) [static]`
- `GLTFCamera FromNode(Camera3D cameraNode) [static]`
- `Godot.Collections.Dictionary ToDictionary()`
- `Camera3D ToNode()`

### GLTFDocumentExtensionConvertImporterMesh
*Inherits: **GLTFDocumentExtension < Resource < RefCounted < Object***

There is currently no description for this class. Please help us by contributing one!

### GLTFDocumentExtension
*Inherits: **Resource < RefCounted < Object** | Inherited by: GLTFDocumentExtensionConvertImporterMesh*

Extends the functionality of the GLTFDocument class by allowing you to run arbitrary code at various stages of glTF import or export.

**Methods**
- `void _ConvertSceneNode(GLTFState state, GLTFNode gltfNode, Node sceneNode) [virtual]`
- `Error _ExportNode(GLTFState state, GLTFNode gltfNode, Godot.Collections.Dictionary json, Node node) [virtual]`
- `GLTFObjectModelProperty _ExportObjectModelProperty(GLTFState state, NodePath nodePath, Node godotNode, int gltfNodeIndex, Object targetObject, int targetDepth) [virtual]`
- `Error _ExportPost(GLTFState state) [virtual]`
- `Error _ExportPostConvert(GLTFState state, Node root) [virtual]`
- `Error _ExportPreflight(GLTFState state, Node root) [virtual]`
- `Error _ExportPreserialize(GLTFState state) [virtual]`
- `Node3D _GenerateSceneNode(GLTFState state, GLTFNode gltfNode, Node sceneParent) [virtual]`
- `string _GetImageFileExtension() [virtual]`
- `PackedStringArray _GetSaveableImageFormats() [virtual]`
- `PackedStringArray _GetSupportedExtensions() [virtual]`
- `Error _ImportNode(GLTFState state, GLTFNode gltfNode, Godot.Collections.Dictionary json, Node node) [virtual]`
- `GLTFObjectModelProperty _ImportObjectModelProperty(GLTFState state, PackedStringArray splitJsonPointer, Array[NodePath] partialPaths) [virtual]`
- `Error _ImportPost(GLTFState state, Node root) [virtual]`
- `Error _ImportPostParse(GLTFState state) [virtual]`
- `Error _ImportPreGenerate(GLTFState state) [virtual]`
- `Error _ImportPreflight(GLTFState state, PackedStringArray extensions) [virtual]`
- `Error _ParseImageData(GLTFState state, PackedByteArray imageData, string mimeType, Image retImage) [virtual]`
- `Error _ParseNodeExtensions(GLTFState state, GLTFNode gltfNode, Godot.Collections.Dictionary extensions) [virtual]`
- `Error _ParseTextureJson(GLTFState state, Godot.Collections.Dictionary textureJson, GLTFTexture retGltfTexture) [virtual]`
- `Error _SaveImageAtPath(GLTFState state, Image image, string filePath, string imageFormat, float lossyQuality) [virtual]`
- `PackedByteArray _SerializeImageToBytes(GLTFState state, Image image, Godot.Collections.Dictionary imageDict, string imageFormat, float lossyQuality) [virtual]`
- `Error _SerializeTextureJson(GLTFState state, Godot.Collections.Dictionary textureJson, GLTFTexture gltfTexture, string imageFormat) [virtual]`

### GLTFDocument
*Inherits: **Resource < RefCounted < Object** | Inherited by: FBXDocument*

GLTFDocument supports reading data from a glTF file, buffer, or Godot scene. This data can then be written to the filesystem, buffer, or used to create a Godot scene.

**Properties**
- `string FallbackImageFormat` = `"None"`
- `float FallbackImageQuality` = `0.25`
- `string ImageFormat` = `"PNG"`
- `float LossyQuality` = `0.75`
- `RootNodeMode RootNodeMode` = `0`
- `VisibilityMode VisibilityMode` = `0`

**Methods**
- `Error AppendFromBuffer(PackedByteArray bytes, string basePath, GLTFState state, int flags = 0)`
- `Error AppendFromFile(string path, GLTFState state, int flags = 0, string basePath = "")`
- `Error AppendFromScene(Node node, GLTFState state, int flags = 0)`
- `GLTFObjectModelProperty ExportObjectModelProperty(GLTFState state, NodePath nodePath, Node godotNode, int gltfNodeIndex) [static]`
- `PackedByteArray GenerateBuffer(GLTFState state)`
- `Node GenerateScene(GLTFState state, float bakeFps = 30, bool trimming = false, bool removeImmutableTracks = true)`
- `PackedStringArray GetSupportedGltfExtensions() [static]`
- `GLTFObjectModelProperty ImportObjectModelProperty(GLTFState state, string jsonPointer) [static]`
- `void RegisterGltfDocumentExtension(GLTFDocumentExtension extension, bool firstPriority = false) [static]`
- `void UnregisterGltfDocumentExtension(GLTFDocumentExtension extension) [static]`
- `Error WriteToFilesystem(GLTFState state, string path)`

### GLTFLight
*Inherits: **Resource < RefCounted < Object***

Represents a light as defined by the KHR_lights_punctual glTF extension.

**Properties**
- `Color Color` = `Color(1, 1, 1, 1)`
- `float InnerConeAngle` = `0.0`
- `float Intensity` = `1.0`
- `string LightType` = `""`
- `float OuterConeAngle` = `0.7853982`
- `float Range` = `inf`

**Methods**
- `GLTFLight FromDictionary(Godot.Collections.Dictionary dictionary) [static]`
- `GLTFLight FromNode(Light3D lightNode) [static]`
- `Variant GetAdditionalData(StringName extensionName)`
- `void SetAdditionalData(StringName extensionName, Variant additionalData)`
- `Godot.Collections.Dictionary ToDictionary()`
- `Light3D ToNode()`

### GLTFMesh
*Inherits: **Resource < RefCounted < Object***

GLTFMesh handles 3D mesh data imported from glTF files. It includes properties for blend channels, blend weights, instance materials, and the mesh itself.

**Properties**
- `PackedFloat32Array BlendWeights` = `PackedFloat32Array()`
- `Array[Material] InstanceMaterials` = `[]`
- `ImporterMesh Mesh`
- `string OriginalName` = `""`

**Methods**
- `Variant GetAdditionalData(StringName extensionName)`
- `void SetAdditionalData(StringName extensionName, Variant additionalData)`

### GLTFNode
*Inherits: **Resource < RefCounted < Object***

Represents a glTF node. glTF nodes may have names, transforms, children (other glTF nodes), and more specialized properties (represented by their own classes).

**Properties**
- `int Camera` = `-1`
- `PackedInt32Array Children` = `PackedInt32Array()`
- `int Height` = `-1`
- `int Light` = `-1`
- `int Mesh` = `-1`
- `string OriginalName` = `""`
- `int Parent` = `-1`
- `Vector3 Position` = `Vector3(0, 0, 0)`
- `Quaternion Rotation` = `Quaternion(0, 0, 0, 1)`
- `Vector3 Scale` = `Vector3(1, 1, 1)`
- `int Skeleton` = `-1`
- `int Skin` = `-1`
- `bool Visible` = `true`
- `Transform3D Xform` = `Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0)`

**Methods**
- `void AppendChildIndex(int childIndex)`
- `Variant GetAdditionalData(StringName extensionName)`
- `NodePath GetSceneNodePath(GLTFState gltfState, bool handleSkeletons = true)`
- `void SetAdditionalData(StringName extensionName, Variant additionalData)`

### GLTFObjectModelProperty
*Inherits: **RefCounted < Object***

GLTFObjectModelProperty defines a mapping between a property in the glTF object model and a NodePath in the Godot scene tree. This can be used to animate properties in a glTF file using the KHR_animation_pointer extension, or to access them through an engine-agnostic script such as a behavior graph as defined by the KHR_interactivity extension.

**Properties**
- `Expression GltfToGodotExpression`
- `Expression GodotToGltfExpression`
- `Array[PackedStringArray] JsonPointers` = `[]`
- `Array[NodePath] NodePaths` = `[]`
- `GLTFObjectModelType ObjectModelType` = `0`
- `Variant.Type VariantType` = `0`

**Methods**
- `void AppendNodePath(NodePath nodePath)`
- `void AppendPathToProperty(NodePath nodePath, StringName propName)`
- `GLTFAccessorType GetAccessorType()`
- `bool HasJsonPointers()`
- `bool HasNodePaths()`
- `void SetTypes(Variant.Type variantType, GLTFObjectModelType objModelType)`

### GLTFPhysicsBody
*Inherits: **Resource < RefCounted < Object***

Represents a physics body as an intermediary between the OMI_physics_body glTF data and Godot's nodes, and it's abstracted in a way that allows adding support for different glTF physics extensions in the future.

**Properties**
- `Vector3 AngularVelocity` = `Vector3(0, 0, 0)`
- `string BodyType` = `"rigid"`
- `Vector3 CenterOfMass` = `Vector3(0, 0, 0)`
- `Vector3 InertiaDiagonal` = `Vector3(0, 0, 0)`
- `Quaternion InertiaOrientation` = `Quaternion(0, 0, 0, 1)`
- `Basis InertiaTensor` = `Basis(0, 0, 0, 0, 0, 0, 0, 0, 0)`
- `Vector3 LinearVelocity` = `Vector3(0, 0, 0)`
- `float Mass` = `1.0`

**Methods**
- `GLTFPhysicsBody FromDictionary(Godot.Collections.Dictionary dictionary) [static]`
- `GLTFPhysicsBody FromNode(CollisionObject3D bodyNode) [static]`
- `Godot.Collections.Dictionary ToDictionary()`
- `CollisionObject3D ToNode()`

### GLTFPhysicsShape
*Inherits: **Resource < RefCounted < Object***

Represents a physics shape as defined by the OMI_physics_shape or OMI_collider glTF extensions. This class is an intermediary between the glTF data and Godot's nodes, and it's abstracted in a way that allows adding support for different glTF physics extensions in the future.

**Properties**
- `float Height` = `2.0`
- `ImporterMesh ImporterMesh`
- `bool IsTrigger` = `false`
- `int MeshIndex` = `-1`
- `float Radius` = `0.5`
- `string ShapeType` = `""`
- `Vector3 Size` = `Vector3(1, 1, 1)`

**Methods**
- `GLTFPhysicsShape FromDictionary(Godot.Collections.Dictionary dictionary) [static]`
- `GLTFPhysicsShape FromNode(CollisionShape3D shapeNode) [static]`
- `GLTFPhysicsShape FromResource(Shape3D shapeResource) [static]`
- `Godot.Collections.Dictionary ToDictionary()`
- `CollisionShape3D ToNode(bool cacheShapes = false)`
- `Shape3D ToResource(bool cacheShapes = false)`

### GLTFSkeleton
*Inherits: **Resource < RefCounted < Object***

There is currently no description for this class. Please help us by contributing one!

**Properties**
- `PackedInt32Array Joints` = `PackedInt32Array()`
- `PackedInt32Array Roots` = `PackedInt32Array()`

**Methods**
- `BoneAttachment3D GetBoneAttachment(int idx)`
- `int GetBoneAttachmentCount()`
- `Godot.Collections.Dictionary GetGodotBoneNode()`
- `Skeleton3D GetGodotSkeleton()`
- `Array[String] GetUniqueNames()`
- `void SetGodotBoneNode(Godot.Collections.Dictionary godotBoneNode)`
- `void SetUniqueNames(Array[String] uniqueNames)`

### GLTFSkin
*Inherits: **Resource < RefCounted < Object***

There is currently no description for this class. Please help us by contributing one!

**Properties**
- `Skin GodotSkin`
- `PackedInt32Array Joints` = `PackedInt32Array()`
- `PackedInt32Array JointsOriginal` = `PackedInt32Array()`
- `PackedInt32Array NonJoints` = `PackedInt32Array()`
- `PackedInt32Array Roots` = `PackedInt32Array()`
- `int Skeleton` = `-1`
- `int SkinRoot` = `-1`

**Methods**
- `Array[Transform3D] GetInverseBinds()`
- `Godot.Collections.Dictionary GetJointIToBoneI()`
- `Godot.Collections.Dictionary GetJointIToName()`
- `void SetInverseBinds(Array[Transform3D] inverseBinds)`
- `void SetJointIToBoneI(Godot.Collections.Dictionary jointIToBoneI)`
- `void SetJointIToName(Godot.Collections.Dictionary jointIToName)`

### GLTFSpecGloss
*Inherits: **Resource < RefCounted < Object***

KHR_materials_pbrSpecularGlossiness is an archived glTF extension. This means that it is deprecated and not recommended for new files. However, it is still supported for loading old files.

**Properties**
- `Color DiffuseFactor` = `Color(1, 1, 1, 1)`
- `Image DiffuseImg`
- `float GlossFactor` = `1.0`
- `Image SpecGlossImg`
- `Color SpecularFactor` = `Color(1, 1, 1, 1)`

### GLTFState
*Inherits: **Resource < RefCounted < Object** | Inherited by: FBXState*

Contains all nodes and resources of a glTF file. This is used by GLTFDocument as data storage, which allows GLTFDocument and all GLTFDocumentExtension classes to remain stateless.

**Properties**
- `float BakeFps` = `30.0`
- `string BasePath` = `""`
- `Array[PackedByteArray] Buffers` = `[]`
- `string Copyright` = `""`
- `bool CreateAnimations` = `true`
- `string Filename` = `""`
- `PackedByteArray GlbData` = `PackedByteArray()`
- `HandleBinaryImageMode HandleBinaryImageMode` = `1`
- `bool ImportAsSkeletonBones` = `false`
- `Godot.Collections.Dictionary Json` = `{}`
- `int MajorVersion` = `0`
- `int MinorVersion` = `0`
- `PackedInt32Array RootNodes` = `PackedInt32Array()`
- `string SceneName` = `""`
- `bool UseNamedSkinBinds` = `false`

**Methods**
- `void AddUsedExtension(string extensionName, bool required)`
- `int AppendDataToBuffers(PackedByteArray data, bool deduplication)`
- `int AppendGltfNode(GLTFNode gltfNode, Node godotSceneNode, int parentNodeIndex)`
- `Array[GLTFAccessor] GetAccessors()`
- `Variant GetAdditionalData(StringName extensionName)`
- `AnimationPlayer GetAnimationPlayer(int animPlayerIndex)`
- `int GetAnimationPlayersCount(int animPlayerIndex)`
- `Array[GLTFAnimation] GetAnimations()`
- `Array[GLTFBufferView] GetBufferViews()`
- `Array[GLTFCamera] GetCameras()`
- `int GetHandleBinaryImage()`
- `Array[Texture2D] GetImages()`
- `Array[GLTFLight] GetLights()`
- `Array[Material] GetMaterials()`
- `Array[GLTFMesh] GetMeshes()`
- `int GetNodeIndex(Node sceneNode)`
- `Array[GLTFNode] GetNodes()`
- `Node GetSceneNode(int gltfNodeIndex)`
- `Array[GLTFSkeleton] GetSkeletons()`
- `Array[GLTFSkin] GetSkins()`
- `Array[GLTFTextureSampler] GetTextureSamplers()`
- `Array[GLTFTexture] GetTextures()`
- `Array[String] GetUniqueAnimationNames()`
- `Array[String] GetUniqueNames()`
- `void SetAccessors(Array[GLTFAccessor] accessors)`
- `void SetAdditionalData(StringName extensionName, Variant additionalData)`
- `void SetAnimations(Array[GLTFAnimation] animations)`
- `void SetBufferViews(Array[GLTFBufferView] bufferViews)`
- `void SetCameras(Array[GLTFCamera] cameras)`
- `void SetHandleBinaryImage(int method)`
- `void SetImages(Array[Texture2D] images)`
- `void SetLights(Array[GLTFLight] lights)`
- `void SetMaterials(Array[Material] materials)`
- `void SetMeshes(Array[GLTFMesh] meshes)`
- `void SetNodes(Array[GLTFNode] nodes)`
- `void SetSkeletons(Array[GLTFSkeleton] skeletons)`
- `void SetSkins(Array[GLTFSkin] skins)`
- `void SetTextureSamplers(Array[GLTFTextureSampler] textureSamplers)`
- `void SetTextures(Array[GLTFTexture] textures)`
- `void SetUniqueAnimationNames(Array[String] uniqueAnimationNames)`

### GLTFTextureSampler
*Inherits: **Resource < RefCounted < Object***

Represents a texture sampler as defined by the base glTF spec. Texture samplers in glTF specify how to sample data from the texture's base image, when rendering the texture on an object.

**Properties**
- `int MagFilter` = `9729`
- `int MinFilter` = `9987`
- `int WrapS` = `10497`
- `int WrapT` = `10497`

### GLTFTexture
*Inherits: **Resource < RefCounted < Object***

GLTFTexture represents a texture in a glTF file.

**Properties**
- `int Sampler` = `-1`
- `int SrcImage` = `-1`

### GPUParticles3D
*Inherits: **GeometryInstance3D < VisualInstance3D < Node3D < Node < Object***

3D particle node used to create a variety of particle systems and effects. GPUParticles3D features an emitter that generates some number of particles at a given rate.

**Properties**
- `int Amount` = `8`
- `float AmountRatio` = `1.0`
- `float CollisionBaseSize` = `0.01`
- `DrawOrder DrawOrder` = `0`
- `Mesh DrawPass1`
- `Mesh DrawPass2`
- `Mesh DrawPass3`
- `Mesh DrawPass4`
- `int DrawPasses` = `1`
- `Skin DrawSkin`
- `bool Emitting` = `true`
- `float Explosiveness` = `0.0`
- `int FixedFps` = `30`
- `bool FractDelta` = `true`
- `float InterpToEnd` = `0.0`
- `bool Interpolate` = `true`
- `float Lifetime` = `1.0`
- `bool LocalCoords` = `false`
- `bool OneShot` = `false`
- `float Preprocess` = `0.0`
- `Material ProcessMaterial`
- `float Randomness` = `0.0`
- `int Seed` = `0`
- `float SpeedScale` = `1.0`
- `NodePath SubEmitter` = `NodePath("")`
- `bool TrailEnabled` = `false`
- `float TrailLifetime` = `0.3`
- `TransformAlign TransformAlign` = `0`
- `bool UseFixedSeed` = `false`
- `AABB VisibilityAabb` = `AABB(-4, -4, -4, 8, 8, 8)`

**Methods**
- `AABB CaptureAabb()`
- `void ConvertFromParticles(Node particles)`
- `void EmitParticle(Transform3D xform, Vector3 velocity, Color color, Color custom, int flags)`
- `Mesh GetDrawPassMesh(int pass)`
- `void RequestParticlesProcess(float processTime)`
- `void Restart(bool keepSeed = false)`
- `void SetDrawPassMesh(int pass, Mesh mesh)`

### GPUParticlesAttractor3D
*Inherits: **VisualInstance3D < Node3D < Node < Object** | Inherited by: GPUParticlesAttractorBox3D, GPUParticlesAttractorSphere3D, GPUParticlesAttractorVectorField3D*

Particle attractors can be used to attract particles towards the attractor's origin, or to push them away from the attractor's origin.

**Properties**
- `float Attenuation` = `1.0`
- `int CullMask` = `4294967295`
- `float Directionality` = `0.0`
- `float Strength` = `1.0`

### GPUParticlesAttractorBox3D
*Inherits: **GPUParticlesAttractor3D < VisualInstance3D < Node3D < Node < Object***

A box-shaped attractor that influences particles from GPUParticles3D nodes. Can be used to attract particles towards its origin, or to push them away from its origin.

**Properties**
- `Vector3 Size` = `Vector3(2, 2, 2)`

### GPUParticlesAttractorSphere3D
*Inherits: **GPUParticlesAttractor3D < VisualInstance3D < Node3D < Node < Object***

A spheroid-shaped attractor that influences particles from GPUParticles3D nodes. Can be used to attract particles towards its origin, or to push them away from its origin.

**Properties**
- `float Radius` = `1.0`

### GPUParticlesAttractorVectorField3D
*Inherits: **GPUParticlesAttractor3D < VisualInstance3D < Node3D < Node < Object***

A box-shaped attractor with varying directions and strengths defined in it that influences particles from GPUParticles3D nodes.

**Properties**
- `Vector3 Size` = `Vector3(2, 2, 2)`
- `Texture3D Texture`

### GPUParticlesCollision3D
*Inherits: **VisualInstance3D < Node3D < Node < Object** | Inherited by: GPUParticlesCollisionBox3D, GPUParticlesCollisionHeightField3D, GPUParticlesCollisionSDF3D, GPUParticlesCollisionSphere3D*

Particle collision shapes can be used to make particles stop or bounce against them.

**Properties**
- `int CullMask` = `4294967295`

### GPUParticlesCollisionBox3D
*Inherits: **GPUParticlesCollision3D < VisualInstance3D < Node3D < Node < Object***

A box-shaped 3D particle collision shape affecting GPUParticles3D nodes.

**Properties**
- `Vector3 Size` = `Vector3(2, 2, 2)`

### GPUParticlesCollisionHeightField3D
*Inherits: **GPUParticlesCollision3D < VisualInstance3D < Node3D < Node < Object***

A real-time heightmap-shaped 3D particle collision shape affecting GPUParticles3D nodes.

**Properties**
- `bool FollowCameraEnabled` = `false`
- `int HeightfieldMask` = `1048575`
- `Resolution Resolution` = `2`
- `Vector3 Size` = `Vector3(2, 2, 2)`
- `UpdateMode UpdateMode` = `0`

**Methods**
- `bool GetHeightfieldMaskValue(int layerNumber)`
- `void SetHeightfieldMaskValue(int layerNumber, bool value)`

### GPUParticlesCollisionSDF3D
*Inherits: **GPUParticlesCollision3D < VisualInstance3D < Node3D < Node < Object***

A baked signed distance field 3D particle collision shape affecting GPUParticles3D nodes.

**Properties**
- `int BakeMask` = `4294967295`
- `Resolution Resolution` = `2`
- `Vector3 Size` = `Vector3(2, 2, 2)`
- `Texture3D Texture`
- `float Thickness` = `1.0`

**Methods**
- `bool GetBakeMaskValue(int layerNumber)`
- `void SetBakeMaskValue(int layerNumber, bool value)`

### GPUParticlesCollisionSphere3D
*Inherits: **GPUParticlesCollision3D < VisualInstance3D < Node3D < Node < Object***

A sphere-shaped 3D particle collision shape affecting GPUParticles3D nodes.

**Properties**
- `float Radius` = `1.0`

### Geometry2D
*Inherits: **Object***

Provides a set of helper functions to create geometric shapes, compute intersections between shapes, and process various other geometric operations in 2D.

**Methods**
- `Array[Vector2i] BresenhamLine(Vector2i from, Vector2i to)`
- `Array[PackedVector2Array] ClipPolygons(PackedVector2Array polygonA, PackedVector2Array polygonB)`
- `Array[PackedVector2Array] ClipPolylineWithPolygon(PackedVector2Array polyline, PackedVector2Array polygon)`
- `PackedVector2Array ConvexHull(PackedVector2Array points)`
- `Array[PackedVector2Array] DecomposePolygonInConvex(PackedVector2Array polygon)`
- `Array[PackedVector2Array] ExcludePolygons(PackedVector2Array polygonA, PackedVector2Array polygonB)`
- `Vector2 GetClosestPointToSegment(Vector2 point, Vector2 s1, Vector2 s2)`
- `Vector2 GetClosestPointToSegmentUncapped(Vector2 point, Vector2 s1, Vector2 s2)`
- `PackedVector2Array GetClosestPointsBetweenSegments(Vector2 p1, Vector2 q1, Vector2 p2, Vector2 q2)`
- `Array[PackedVector2Array] IntersectPolygons(PackedVector2Array polygonA, PackedVector2Array polygonB)`
- `Array[PackedVector2Array] IntersectPolylineWithPolygon(PackedVector2Array polyline, PackedVector2Array polygon)`
- `bool IsPointInCircle(Vector2 point, Vector2 circlePosition, float circleRadius)`
- `bool IsPointInPolygon(Vector2 point, PackedVector2Array polygon)`
- `bool IsPolygonClockwise(PackedVector2Array polygon)`
- `Variant LineIntersectsLine(Vector2 fromA, Vector2 dirA, Vector2 fromB, Vector2 dirB)`
- `Godot.Collections.Dictionary MakeAtlas(PackedVector2Array sizes)`
- `Array[PackedVector2Array] MergePolygons(PackedVector2Array polygonA, PackedVector2Array polygonB)`
- `Array[PackedVector2Array] OffsetPolygon(PackedVector2Array polygon, float delta, PolyJoinType joinType = 0)`
- `Array[PackedVector2Array] OffsetPolyline(PackedVector2Array polyline, float delta, PolyJoinType joinType = 0, PolyEndType endType = 3)`
- `bool PointIsInsideTriangle(Vector2 point, Vector2 a, Vector2 b, Vector2 c)`
- `float SegmentIntersectsCircle(Vector2 segmentFrom, Vector2 segmentTo, Vector2 circlePosition, float circleRadius)`
- `Variant SegmentIntersectsSegment(Vector2 fromA, Vector2 toA, Vector2 fromB, Vector2 toB)`
- `PackedInt32Array TriangulateDelaunay(PackedVector2Array points)`
- `PackedInt32Array TriangulatePolygon(PackedVector2Array polygon)`

**C# Examples**
```csharp
var fromA = Vector2.Zero;
var dirA = Vector2.Right;
var fromB = Vector2.Down;

// Returns new Vector2(1, 0)
Geometry2D.LineIntersectsLine(fromA, dirA, fromB, new Vector2(1, -1));
// Returns new Vector2(-1, 0)
Geometry2D.LineIntersectsLine(fromA, dirA, fromB, new Vector2(-1, -1));
// Returns null
Geometry2D.LineIntersectsLine(fromA, dirA, fromB, Vector2.Right);
```
```csharp
Vector2[] polygon = [new Vector2(0, 0), new Vector2(100, 0), new Vector2(100, 100), new Vector2(0, 100)];
var offset = new Vector2(50, 50);
polygon = new Transform2D(0, offset) * polygon;
GD.Print((Variant)polygon); // Prints [(50, 50), (150, 50), (150, 150), (50, 150)]
```

### Geometry3D
*Inherits: **Object***

Provides a set of helper functions to create geometric shapes, compute intersections between shapes, and process various other geometric operations in 3D.

**Methods**
- `Array[Plane] BuildBoxPlanes(Vector3 extents)`
- `Array[Plane] BuildCapsulePlanes(float radius, float height, int sides, int lats, Axis axis = 2)`
- `Array[Plane] BuildCylinderPlanes(float radius, float height, int sides, Axis axis = 2)`
- `PackedVector3Array ClipPolygon(PackedVector3Array points, Plane plane)`
- `PackedVector3Array ComputeConvexMeshPoints(Array[Plane] planes)`
- `Vector3 GetClosestPointToSegment(Vector3 point, Vector3 s1, Vector3 s2)`
- `Vector3 GetClosestPointToSegmentUncapped(Vector3 point, Vector3 s1, Vector3 s2)`
- `PackedVector3Array GetClosestPointsBetweenSegments(Vector3 p1, Vector3 p2, Vector3 q1, Vector3 q2)`
- `Vector3 GetTriangleBarycentricCoords(Vector3 point, Vector3 a, Vector3 b, Vector3 c)`
- `Variant RayIntersectsTriangle(Vector3 from, Vector3 dir, Vector3 a, Vector3 b, Vector3 c)`
- `PackedVector3Array SegmentIntersectsConvex(Vector3 from, Vector3 to, Array[Plane] planes)`
- `PackedVector3Array SegmentIntersectsCylinder(Vector3 from, Vector3 to, float height, float radius)`
- `PackedVector3Array SegmentIntersectsSphere(Vector3 from, Vector3 to, Vector3 spherePosition, float sphereRadius)`
- `Variant SegmentIntersectsTriangle(Vector3 from, Vector3 to, Vector3 a, Vector3 b, Vector3 c)`
- `PackedInt32Array TetrahedralizeDelaunay(PackedVector3Array points)`

### GodotInstance
*Inherits: **Object***

GodotInstance represents a running Godot instance that is controlled from an outside codebase, without a perpetual main loop. It is created by the C API libgodot_create_godot_instance. Only one may be created per process.

**Methods**
- `void FocusIn()`
- `void FocusOut()`
- `bool IsStarted()`
- `bool Iteration()`
- `void Pause()`
- `void Resume()`
- `bool Start()`

### GraphElement
*Inherits: **Container < Control < CanvasItem < Node < Object** | Inherited by: GraphFrame, GraphNode*

GraphElement allows to create custom elements for a GraphEdit graph. By default such elements can be selected, resized, and repositioned, but they cannot be connected. For a graph element that allows for connections see GraphNode.

**Properties**
- `bool Draggable` = `true`
- `Vector2 PositionOffset` = `Vector2(0, 0)`
- `bool Resizable` = `false`
- `bool ScalingMenus` = `false`
- `bool Selectable` = `true`
- `bool Selected` = `false`

### GridMapEditorPlugin
*Inherits: **EditorPlugin < Node < Object***

GridMapEditorPlugin provides access to the GridMap editor functionality.

**Methods**
- `void ClearSelection()`
- `GridMap GetCurrentGridMap()`
- `Godot.Collections.Array GetSelectedCells()`
- `int GetSelectedPaletteItem()`
- `AABB GetSelection()`
- `bool HasSelection()`
- `void SetSelectedPaletteItem(int item)`
- `void SetSelection(Vector3i begin, Vector3i end)`

### GridMap
*Inherits: **Node3D < Node < Object***

GridMap lets you place meshes on a grid interactively. It works both from the editor and from scripts, which can help you create in-game level editors.

**Properties**
- `bool BakeNavigation` = `false`
- `bool CellCenterX` = `true`
- `bool CellCenterY` = `true`
- `bool CellCenterZ` = `true`
- `int CellOctantSize` = `8`
- `float CellScale` = `1.0`
- `Vector3 CellSize` = `Vector3(2, 2, 2)`
- `int CollisionLayer` = `1`
- `int CollisionMask` = `1`
- `float CollisionPriority` = `1.0`
- `MeshLibrary MeshLibrary`
- `PhysicsMaterial PhysicsMaterial`

**Methods**
- `void Clear()`
- `void ClearBakedMeshes()`
- `RID GetBakeMeshInstance(int idx)`
- `Godot.Collections.Array GetBakeMeshes()`
- `Basis GetBasisWithOrthogonalIndex(int index)`
- `int GetCellItem(Vector3i position)`
- `Basis GetCellItemBasis(Vector3i position)`
- `int GetCellItemOrientation(Vector3i position)`
- `bool GetCollisionLayerValue(int layerNumber)`
- `bool GetCollisionMaskValue(int layerNumber)`
- `Godot.Collections.Array GetMeshes()`
- `RID GetNavigationMap()`
- `int GetOrthogonalIndexFromBasis(Basis basis)`
- `Array[Vector3i] GetUsedCells()`
- `Array[Vector3i] GetUsedCellsByItem(int item)`
- `Vector3i LocalToMap(Vector3 localPosition)`
- `void MakeBakedMeshes(bool genLightmapUv = false, float lightmapUvTexelSize = 0.1)`
- `Vector3 MapToLocal(Vector3i mapPosition)`
- `void ResourceChanged(Resource resource)`
- `void SetCellItem(Vector3i position, int item, int orientation = 0)`
- `void SetCollisionLayerValue(int layerNumber, bool value)`
- `void SetCollisionMaskValue(int layerNumber, bool value)`
- `void SetNavigationMap(RID navigationMap)`

### HFlowContainer
*Inherits: **FlowContainer < Container < Control < CanvasItem < Node < Object***

A variant of FlowContainer that can only arrange its child controls horizontally, wrapping them around at the borders. This is similar to how text in a book wraps around when no more words can fit on a line.

### HMACContext
*Inherits: **RefCounted < Object***

The HMACContext class is useful for advanced HMAC use cases, such as streaming the message as it supports creating the message over time rather than providing it all at once.

**Methods**
- `PackedByteArray Finish()`
- `Error Start(HashType hashType, PackedByteArray key)`
- `Error Update(PackedByteArray data)`

**C# Examples**
```csharp
using Godot;
using System.Diagnostics;

public partial class MyNode : Node
{
    private HmacContext _ctx = new HmacContext();

    public override void _Ready()
    {
        byte[] key = "supersecret".ToUtf8Buffer();
        Error err = _ctx.Start(HashingContext.HashType.Sha256, key);
        Debug.Assert(err == Error.Ok);
        byte[] msg1 = "this is ".ToUtf8Buffer();
        byte[] msg2 = "super duper secret".ToUtf8Buffer();
        err = _ctx.Update(msg1);
        Debug.Assert(err == Error.Ok);
        err = _ctx.Update(msg2);
        Debug.Assert(err == Error.Ok);
        byte[] hmac =
// ...
```

### HSeparator
*Inherits: **Separator < Control < CanvasItem < Node < Object***

A horizontal separator used for separating other controls that are arranged vertically. HSeparator is purely visual and normally drawn as a StyleBoxLine.

### HeightMapShape3D
*Inherits: **Shape3D < Resource < RefCounted < Object***

A 3D heightmap shape, intended for use in physics to provide a shape for a CollisionShape3D. This type is most commonly used for terrain with vertices placed in a fixed-width grid.

**Properties**
- `PackedFloat32Array MapData` = `PackedFloat32Array(0, 0, 0, 0)`
- `int MapDepth` = `2`
- `int MapWidth` = `2`

**Methods**
- `float GetMaxHeight()`
- `float GetMinHeight()`
- `void UpdateMapDataFromImage(Image image, float heightMin, float heightMax)`

### IKModifier3D
*Inherits: **SkeletonModifier3D < Node3D < Node < Object** | Inherited by: ChainIK3D, TwoBoneIK3D*

Base class of SkeletonModifier3Ds that has some joint lists and applies inverse kinematics. This class has some structs, enums, and helper methods which are useful to solve inverse kinematics.

**Properties**
- `bool MutableBoneAxes` = `true`

**Methods**
- `void ClearSettings()`
- `int GetSettingCount()`
- `void Reset()`
- `void SetSettingCount(int count)`

### IP
*Inherits: **Object***

IP contains support functions for the Internet Protocol (IP). TCP/IP support is in different classes (see StreamPeerTCP and TCPServer). IP provides DNS hostname resolution support, both blocking and threaded.

**Methods**
- `void ClearCache(string hostname = "")`
- `void EraseResolveItem(int id)`
- `PackedStringArray GetLocalAddresses()`
- `Array[Dictionary] GetLocalInterfaces()`
- `string GetResolveItemAddress(int id)`
- `Godot.Collections.Array GetResolveItemAddresses(int id)`
- `ResolverStatus GetResolveItemStatus(int id)`
- `string ResolveHostname(string host, Type ipType = 3)`
- `PackedStringArray ResolveHostnameAddresses(string host, Type ipType = 3)`
- `int ResolveHostnameQueueItem(string host, Type ipType = 3)`

### ImageFormatLoaderExtension
*Inherits: **ImageFormatLoader < RefCounted < Object***

The engine supports multiple image formats out of the box (PNG, SVG, JPEG, WebP to name a few), but you can choose to implement support for additional image formats by extending this class.

**Methods**
- `PackedStringArray _GetRecognizedExtensions() [virtual]`
- `Error _LoadImage(Image image, FileAccess fileaccess, BitField[LoaderFlags] flags, float scale) [virtual]`
- `void AddFormatLoader()`
- `void RemoveFormatLoader()`

### ImageFormatLoader
*Inherits: **RefCounted < Object** | Inherited by: ImageFormatLoaderExtension*

The engine supports multiple image formats out of the box (PNG, SVG, JPEG, WebP to name a few), but you can choose to implement support for additional image formats by extending ImageFormatLoaderExtension.

### Image
*Inherits: **Resource < RefCounted < Object***

Native image datatype. Contains image data which can be converted to an ImageTexture and provides commonly used image processing methods. The maximum width and height for an Image are MAX_WIDTH and MAX_HEIGHT.

**Properties**
- `Godot.Collections.Dictionary Data` = `{ "data": PackedByteArray(), "format": "Lum8", "height": 0, "mipmaps": false, "width": 0 }`

**Methods**
- `void AdjustBcs(float brightness, float contrast, float saturation)`
- `void BlendRect(Image src, Rect2i srcRect, Vector2i dst)`
- `void BlendRectMask(Image src, Image mask, Rect2i srcRect, Vector2i dst)`
- `void BlitRect(Image src, Rect2i srcRect, Vector2i dst)`
- `void BlitRectMask(Image src, Image mask, Rect2i srcRect, Vector2i dst)`
- `void BumpMapToNormalMap(float bumpScale = 1.0)`
- `void ClearMipmaps()`
- `Error Compress(CompressMode mode, CompressSource source = 0, ASTCFormat astcFormat = 0)`
- `Error CompressFromChannels(CompressMode mode, UsedChannels channels, ASTCFormat astcFormat = 0)`
- `Godot.Collections.Dictionary ComputeImageMetrics(Image comparedImage, bool useLuma)`
- `void Convert(Format format)`
- `void CopyFrom(Image src)`
- `Image Create(int width, int height, bool useMipmaps, Format format) [static]`
- `Image CreateEmpty(int width, int height, bool useMipmaps, Format format) [static]`
- `Image CreateFromData(int width, int height, bool useMipmaps, Format format, PackedByteArray data) [static]`
- `void Crop(int width, int height)`
- `Error Decompress()`
- `AlphaMode DetectAlpha()`
- `UsedChannels DetectUsedChannels(CompressSource source = 0)`
- `void Fill(Color color)`
- `void FillRect(Rect2i rect, Color color)`
- `void FixAlphaEdges()`
- `void FlipX()`
- `void FlipY()`
- `Error GenerateMipmaps(bool renormalize = false)`
- `PackedByteArray GetData()`
- `int GetDataSize()`
- `Format GetFormat()`
- `int GetHeight()`
- `int GetMipmapCount()`
- `int GetMipmapOffset(int mipmap)`
- `Color GetPixel(int x, int y)`
- `Color GetPixelv(Vector2i point)`
- `Image GetRegion(Rect2i region)`
- `Vector2i GetSize()`
- `Rect2i GetUsedRect()`
- `int GetWidth()`
- `bool HasMipmaps()`
- `bool IsCompressed()`
- `bool IsEmpty()`

**C# Examples**
```csharp
int imgWidth = 10;
int imgHeight = 5;
var img = Image.Create(imgWidth, imgHeight, false, Image.Format.Rgba8);

img.SetPixel(1, 2, Colors.Red); // Sets the color at (1, 2) to red.
```
```csharp
int imgWidth = 10;
int imgHeight = 5;
var img = Image.Create(imgWidth, imgHeight, false, Image.Format.Rgba8);

img.SetPixelv(new Vector2I(1, 2), Colors.Red); // Sets the color at (1, 2) to red.
```

### ImporterMeshInstance3D
*Inherits: **Node3D < Node < Object***

There is currently no description for this class. Please help us by contributing one!

**Properties**
- `ShadowCastingSetting CastShadow` = `1`
- `int LayerMask` = `1`
- `ImporterMesh Mesh`
- `NodePath SkeletonPath` = `NodePath("")`
- `Skin Skin`
- `float VisibilityRangeBegin` = `0.0`
- `float VisibilityRangeBeginMargin` = `0.0`
- `float VisibilityRangeEnd` = `0.0`
- `float VisibilityRangeEndMargin` = `0.0`
- `VisibilityRangeFadeMode VisibilityRangeFadeMode` = `0`

### ImporterMesh
*Inherits: **Resource < RefCounted < Object***

ImporterMesh is a type of Resource analogous to ArrayMesh. It contains vertex array-based geometry, divided in surfaces. Each surface contains a completely separate array and a material used to draw it. Design wise, a mesh with multiple surfaces is preferred to a single surface, because objects created in 3D editing software commonly contain multiple materials.

**Methods**
- `void AddBlendShape(string name)`
- `void AddSurface(PrimitiveType primitive, Godot.Collections.Array arrays, Array[Array] blendShapes = [], Godot.Collections.Dictionary lods = {}, Material material = null, string name = "", int flags = 0)`
- `void Clear()`
- `ImporterMesh FromMesh(Mesh mesh) [static]`
- `void GenerateLods(float normalMergeAngle, float normalSplitAngle, Godot.Collections.Array boneTransformArray)`
- `int GetBlendShapeCount()`
- `BlendShapeMode GetBlendShapeMode()`
- `string GetBlendShapeName(int blendShapeIdx)`
- `Vector2i GetLightmapSizeHint()`
- `ArrayMesh GetMesh(ArrayMesh baseMesh = null)`
- `Godot.Collections.Array GetSurfaceArrays(int surfaceIdx)`
- `Godot.Collections.Array GetSurfaceBlendShapeArrays(int surfaceIdx, int blendShapeIdx)`
- `int GetSurfaceCount()`
- `int GetSurfaceFormat(int surfaceIdx)`
- `int GetSurfaceLodCount(int surfaceIdx)`
- `PackedInt32Array GetSurfaceLodIndices(int surfaceIdx, int lodIdx)`
- `float GetSurfaceLodSize(int surfaceIdx, int lodIdx)`
- `Material GetSurfaceMaterial(int surfaceIdx)`
- `string GetSurfaceName(int surfaceIdx)`
- `PrimitiveType GetSurfacePrimitiveType(int surfaceIdx)`
- `void SetBlendShapeMode(BlendShapeMode mode)`
- `void SetLightmapSizeHint(Vector2i size)`
- `void SetSurfaceMaterial(int surfaceIdx, Material material)`
- `void SetSurfaceName(int surfaceIdx, string name)`

### Input
*Inherits: **Object***

The Input singleton handles key presses, mouse buttons and movement, gamepads, and input actions. Actions and their events can be set in the Input Map tab in Project > Project Settings, or with the InputMap class.

**Properties**
- `bool EmulateMouseFromTouch`
- `bool EmulateTouchFromMouse`
- `MouseMode MouseMode`
- `bool UseAccumulatedInput`

**Methods**
- `void ActionPress(StringName action, float strength = 1.0)`
- `void ActionRelease(StringName action)`
- `void AddJoyMapping(string mapping, bool updateExisting = false)`
- `void FlushBufferedEvents()`
- `Vector3 GetAccelerometer()`
- `float GetActionRawStrength(StringName action, bool exactMatch = false)`
- `float GetActionStrength(StringName action, bool exactMatch = false)`
- `float GetAxis(StringName negativeAction, StringName positiveAction)`
- `Array[int] GetConnectedJoypads()`
- `CursorShape GetCurrentCursorShape()`
- `Vector3 GetGravity()`
- `Vector3 GetGyroscope()`
- `float GetJoyAxis(int device, JoyAxis axis)`
- `string GetJoyGuid(int device)`
- `Godot.Collections.Dictionary GetJoyInfo(int device)`
- `string GetJoyName(int device)`
- `float GetJoyVibrationDuration(int device)`
- `Vector2 GetJoyVibrationStrength(int device)`
- `Vector2 GetLastMouseScreenVelocity()`
- `Vector2 GetLastMouseVelocity()`
- `Vector3 GetMagnetometer()`
- `BitField[MouseButtonMask] GetMouseButtonMask()`
- `Vector2 GetVector(StringName negativeX, StringName positiveX, StringName negativeY, StringName positiveY, float deadzone = -1.0)`
- `bool HasJoyLight(int device)`
- `bool IsActionJustPressed(StringName action, bool exactMatch = false)`
- `bool IsActionJustPressedByEvent(StringName action, InputEvent event, bool exactMatch = false)`
- `bool IsActionJustReleased(StringName action, bool exactMatch = false)`
- `bool IsActionJustReleasedByEvent(StringName action, InputEvent event, bool exactMatch = false)`
- `bool IsActionPressed(StringName action, bool exactMatch = false)`
- `bool IsAnythingPressed()`
- `bool IsJoyButtonPressed(int device, JoyButton button)`
- `bool IsJoyKnown(int device)`
- `bool IsKeyLabelPressed(Key keycode)`
- `bool IsKeyPressed(Key keycode)`
- `bool IsMouseButtonPressed(MouseButton button)`
- `bool IsPhysicalKeyPressed(Key keycode)`
- `void ParseInputEvent(InputEvent event)`
- `void RemoveJoyMapping(string guid)`
- `void SetAccelerometer(Vector3 value)`
- `void SetCustomMouseCursor(Resource image, CursorShape shape = 0, Vector2 hotspot = Vector2(0, 0))`

**C# Examples**
```csharp
var cancelEvent = new InputEventAction();
cancelEvent.Action = "ui_cancel";
cancelEvent.Pressed = true;
Input.ParseInputEvent(cancelEvent);
```

### InstancePlaceholder
*Inherits: **Node < Object***

Turning on the option Load As Placeholder for an instantiated scene in the editor causes it to be replaced by an InstancePlaceholder when running the game, this will not replace the node in the editor. This makes it possible to delay actually loading the scene until calling create_instance(). This is useful to avoid loading large scenes all at once by loading parts of it selectively.

**Methods**
- `Node CreateInstance(bool replace = false, PackedScene customScene = null)`
- `string GetInstancePath()`
- `Godot.Collections.Dictionary GetStoredValues(bool withOrder = false)`

### IterateIK3D
*Inherits: **ChainIK3D < IKModifier3D < SkeletonModifier3D < Node3D < Node < Object** | Inherited by: CCDIK3D, FABRIK3D, JacobianIK3D*

Base class of SkeletonModifier3D to approach the goal by repeating small rotations.

**Properties**
- `float AngularDeltaLimit` = `0.034906585`
- `bool Deterministic` = `false`
- `int MaxIterations` = `4`
- `float MinDistance` = `0.001`
- `int SettingCount` = `0`

**Methods**
- `JointLimitation3D GetJointLimitation(int index, int joint)`
- `SecondaryDirection GetJointLimitationRightAxis(int index, int joint)`
- `Vector3 GetJointLimitationRightAxisVector(int index, int joint)`
- `Quaternion GetJointLimitationRotationOffset(int index, int joint)`
- `RotationAxis GetJointRotationAxis(int index, int joint)`
- `Vector3 GetJointRotationAxisVector(int index, int joint)`
- `NodePath GetTargetNode(int index)`
- `void SetJointLimitation(int index, int joint, JointLimitation3D limitation)`
- `void SetJointLimitationRightAxis(int index, int joint, SecondaryDirection direction)`
- `void SetJointLimitationRightAxisVector(int index, int joint, Vector3 vector)`
- `void SetJointLimitationRotationOffset(int index, int joint, Quaternion offset)`
- `void SetJointRotationAxis(int index, int joint, RotationAxis axis)`
- `void SetJointRotationAxisVector(int index, int joint, Vector3 axisVector)`
- `void SetTargetNode(int index, NodePath targetNode)`

### JNISingleton
*Inherits: **Object***

The JNISingleton is implemented only in the Android export. It's used to call methods and connect signals from an Android plugin written in Java or Kotlin. Methods and signals can be called and connected to the JNISingleton as if it is a Node. See Java Native Interface - Wikipedia for more information.

**Methods**
- `bool HasJavaMethod(StringName method)`

### JSONRPC
*Inherits: **Object***

JSON-RPC is a standard which wraps a method call in a JSON object. The object has a particular structure and identifies which method is called, the parameters to that function, and carries an ID to keep track of responses. This class implements that standard on top of Dictionary; you will have to convert between a Dictionary and JSON with other functions.

**Methods**
- `Godot.Collections.Dictionary MakeNotification(string method, Variant params)`
- `Godot.Collections.Dictionary MakeRequest(string method, Variant params, Variant id)`
- `Godot.Collections.Dictionary MakeResponse(Variant result, Variant id)`
- `Godot.Collections.Dictionary MakeResponseError(int code, string message, Variant id = null)`
- `Variant ProcessAction(Variant action, bool recurse = false)`
- `string ProcessString(string action)`
- `void SetMethod(string name, Callable callback)`

### JSON
*Inherits: **Resource < RefCounted < Object***

The JSON class enables all data types to be converted to and from a JSON string. This is useful for serializing data, e.g. to save to a file or send over the network.

**Properties**
- `Variant Data` = `null`

**Methods**
- `Variant FromNative(Variant variant, bool fullObjects = false) [static]`
- `int GetErrorLine()`
- `string GetErrorMessage()`
- `string GetParsedText()`
- `Error Parse(string jsonText, bool keepText = false)`
- `Variant ParseString(string jsonString) [static]`
- `string Stringify(Variant data, string indent = "", bool sortKeys = true, bool fullPrecision = false) [static]`
- `Variant ToNative(Variant json, bool allowObjects = false) [static]`

### JacobianIK3D
*Inherits: **IterateIK3D < ChainIK3D < IKModifier3D < SkeletonModifier3D < Node3D < Node < Object***

JacobianIK3D calculates rotations for all joints simultaneously, producing natural and smooth movement. It is particularly suited for biological animations.

### JavaClassWrapper
*Inherits: **Object***

The JavaClassWrapper singleton provides a way for the Godot application to send and receive data through the Java Native Interface (JNI).

**Methods**
- `JavaObject GetException()`
- `JavaClass Wrap(string name)`

### JavaClass
*Inherits: **RefCounted < Object***

Represents a class from the Java Native Interface. It is returned from JavaClassWrapper.wrap().

**Methods**
- `string GetJavaClassName()`
- `Array[Dictionary] GetJavaMethodList()`
- `JavaClass GetJavaParentClass()`
- `bool HasJavaMethod(StringName method)`

### JavaObject
*Inherits: **RefCounted < Object***

Represents an object from the Java Native Interface. It can be returned from Java methods called on JavaClass or other JavaObjects. See JavaClassWrapper for an example.

**Methods**
- `JavaClass GetJavaClass()`
- `bool HasJavaMethod(StringName method)`

### JavaScriptBridge
*Inherits: **Object***

The JavaScriptBridge singleton is implemented only in the Web export. It's used to access the browser's JavaScript context. This allows interaction with embedding pages or calling third-party JavaScript APIs.

**Methods**
- `JavaScriptObject CreateCallback(Callable callable)`
- `Variant CreateObject(string object)`
- `void DownloadBuffer(PackedByteArray buffer, string name, string mime = "application/octet-stream")`
- `Variant Eval(string code, bool useGlobalExecutionContext = false)`
- `void ForceFsSync()`
- `JavaScriptObject GetInterface(string interface)`
- `bool IsJsBuffer(JavaScriptObject javascriptObject)`
- `PackedByteArray JsBufferToPackedByteArray(JavaScriptObject javascriptBuffer)`
- `bool PwaNeedsUpdate()`
- `Error PwaUpdate()`

### JavaScriptObject
*Inherits: **RefCounted < Object***

JavaScriptObject is used to interact with JavaScript objects retrieved or created via JavaScriptBridge.get_interface(), JavaScriptBridge.create_object(), or JavaScriptBridge.create_callback().

### JointLimitation3D
*Inherits: **Resource < RefCounted < Object** | Inherited by: JointLimitationCone3D*

The limitation is attached to each joint and limits the rotation of the bone.

### JointLimitationCone3D
*Inherits: **JointLimitation3D < Resource < RefCounted < Object***

A cone shape limitation that interacts with ChainIK3D.

**Properties**
- `float Angle` = `1.5707964`

### KinematicCollision2D
*Inherits: **RefCounted < Object***

Holds collision data from the movement of a PhysicsBody2D, usually from PhysicsBody2D.move_and_collide(). When a PhysicsBody2D is moved, it stops if it detects a collision with another body. If a collision is detected, a KinematicCollision2D object is returned.

**Methods**
- `float GetAngle(Vector2 upDirection = Vector2(0, -1))`
- `Object GetCollider()`
- `int GetColliderId()`
- `RID GetColliderRid()`
- `Object GetColliderShape()`
- `int GetColliderShapeIndex()`
- `Vector2 GetColliderVelocity()`
- `float GetDepth()`
- `Object GetLocalShape()`
- `Vector2 GetNormal()`
- `Vector2 GetPosition()`
- `Vector2 GetRemainder()`
- `Vector2 GetTravel()`

### KinematicCollision3D
*Inherits: **RefCounted < Object***

Holds collision data from the movement of a PhysicsBody3D, usually from PhysicsBody3D.move_and_collide(). When a PhysicsBody3D is moved, it stops if it detects a collision with another body. If a collision is detected, a KinematicCollision3D object is returned.

**Methods**
- `float GetAngle(int collisionIndex = 0, Vector3 upDirection = Vector3(0, 1, 0))`
- `Object GetCollider(int collisionIndex = 0)`
- `int GetColliderId(int collisionIndex = 0)`
- `RID GetColliderRid(int collisionIndex = 0)`
- `Object GetColliderShape(int collisionIndex = 0)`
- `int GetColliderShapeIndex(int collisionIndex = 0)`
- `Vector3 GetColliderVelocity(int collisionIndex = 0)`
- `int GetCollisionCount()`
- `float GetDepth()`
- `Object GetLocalShape(int collisionIndex = 0)`
- `Vector3 GetNormal(int collisionIndex = 0)`
- `Vector3 GetPosition(int collisionIndex = 0)`
- `Vector3 GetRemainder()`
- `Vector3 GetTravel()`

### Label3D
*Inherits: **GeometryInstance3D < VisualInstance3D < Node3D < Node < Object***

A node for displaying plain text in 3D space. By adjusting various properties of this node, you can configure things such as the text's appearance and whether it always faces the camera.

**Properties**
- `float AlphaAntialiasingEdge` = `0.0`
- `AlphaAntiAliasing AlphaAntialiasingMode` = `0`
- `AlphaCutMode AlphaCut` = `0`
- `float AlphaHashScale` = `1.0`
- `float AlphaScissorThreshold` = `0.5`
- `AutowrapMode AutowrapMode` = `0`
- `BitField[LineBreakFlag] AutowrapTrimFlags` = `192`
- `BillboardMode Billboard` = `0`
- `ShadowCastingSetting CastShadow` = `0 (overrides GeometryInstance3D)`
- `bool DoubleSided` = `true`
- `bool FixedSize` = `false`
- `Font Font`
- `int FontSize` = `32`
- `GIMode GiMode` = `0 (overrides GeometryInstance3D)`
- `HorizontalAlignment HorizontalAlignment` = `1`
- `BitField[JustificationFlag] JustificationFlags` = `163`
- `string Language` = `""`
- `float LineSpacing` = `0.0`
- `Color Modulate` = `Color(1, 1, 1, 1)`
- `bool NoDepthTest` = `false`
- `Vector2 Offset` = `Vector2(0, 0)`
- `Color OutlineModulate` = `Color(0, 0, 0, 1)`
- `int OutlineRenderPriority` = `-1`
- `int OutlineSize` = `12`
- `float PixelSize` = `0.005`
- `int RenderPriority` = `0`
- `bool Shaded` = `false`
- `StructuredTextParser StructuredTextBidiOverride` = `0`
- `Godot.Collections.Array StructuredTextBidiOverrideOptions` = `[]`
- `string Text` = `""`

**Methods**
- `TriangleMesh GenerateTriangleMesh()`
- `bool GetDrawFlag(DrawFlags flag)`
- `void SetDrawFlag(DrawFlags flag, bool enabled)`

### LabelSettings
*Inherits: **Resource < RefCounted < Object***

LabelSettings is a resource that provides common settings to customize the text in a Label. It will take priority over the properties defined in Control.theme. The resource can be shared between multiple labels and changed on the fly, so it's convenient and flexible way to setup text style.

**Properties**
- `Font Font`
- `Color FontColor` = `Color(1, 1, 1, 1)`
- `int FontSize` = `16`
- `float LineSpacing` = `3.0`
- `Color OutlineColor` = `Color(1, 1, 1, 1)`
- `int OutlineSize` = `0`
- `float ParagraphSpacing` = `0.0`
- `Color ShadowColor` = `Color(0, 0, 0, 0)`
- `Vector2 ShadowOffset` = `Vector2(1, 1)`
- `int ShadowSize` = `1`
- `int StackedOutlineCount` = `0`
- `int StackedShadowCount` = `0`

**Methods**
- `void AddStackedOutline(int index = -1)`
- `void AddStackedShadow(int index = -1)`
- `Color GetStackedOutlineColor(int index)`
- `int GetStackedOutlineSize(int index)`
- `Color GetStackedShadowColor(int index)`
- `Vector2 GetStackedShadowOffset(int index)`
- `int GetStackedShadowOutlineSize(int index)`
- `void MoveStackedOutline(int fromIndex, int toPosition)`
- `void MoveStackedShadow(int fromIndex, int toPosition)`
- `void RemoveStackedOutline(int index)`
- `void RemoveStackedShadow(int index)`
- `void SetStackedOutlineColor(int index, Color color)`
- `void SetStackedOutlineSize(int index, int size)`
- `void SetStackedShadowColor(int index, Color color)`
- `void SetStackedShadowOffset(int index, Vector2 offset)`
- `void SetStackedShadowOutlineSize(int index, int size)`

### Label
*Inherits: **Control < CanvasItem < Node < Object***

A control for displaying plain text. It gives you control over the horizontal and vertical alignment and can wrap the text inside the node's bounding rectangle. It doesn't support bold, italics, or other rich text formatting. For that, use RichTextLabel instead.

**Properties**
- `AutowrapMode AutowrapMode` = `0`
- `BitField[LineBreakFlag] AutowrapTrimFlags` = `192`
- `bool ClipText` = `false`
- `string EllipsisChar` = `"…"`
- `HorizontalAlignment HorizontalAlignment` = `0`
- `BitField[JustificationFlag] JustificationFlags` = `163`
- `LabelSettings LabelSettings`
- `string Language` = `""`
- `int LinesSkipped` = `0`
- `int MaxLinesVisible` = `-1`
- `MouseFilter MouseFilter` = `2 (overrides Control)`
- `string ParagraphSeparator` = `"\\n"`
- `BitField[SizeFlags] SizeFlagsVertical` = `4 (overrides Control)`
- `StructuredTextParser StructuredTextBidiOverride` = `0`
- `Godot.Collections.Array StructuredTextBidiOverrideOptions` = `[]`
- `PackedFloat32Array TabStops` = `PackedFloat32Array()`
- `string Text` = `""`
- `TextDirection TextDirection` = `0`
- `OverrunBehavior TextOverrunBehavior` = `0`
- `bool Uppercase` = `false`
- `VerticalAlignment VerticalAlignment` = `0`
- `int VisibleCharacters` = `-1`
- `VisibleCharactersBehavior VisibleCharactersBehavior` = `0`
- `float VisibleRatio` = `1.0`

**Methods**
- `Rect2 GetCharacterBounds(int pos)`
- `int GetLineCount()`
- `int GetLineHeight(int line = -1)`
- `int GetTotalCharacterCount()`
- `int GetVisibleLineCount()`

### LightmapperRD
*Inherits: **Lightmapper < RefCounted < Object***

LightmapperRD ("RD" stands for RenderingDevice) is the built-in GPU-based lightmapper for use with LightmapGI. On most dedicated GPUs, it can bake lightmaps much faster than most CPU-based lightmappers. LightmapperRD uses compute shaders to bake lightmaps, so it does not require CUDA or OpenCL libraries to be installed to be usable.

### Lightmapper
*Inherits: **RefCounted < Object** | Inherited by: LightmapperRD*

This class should be extended by custom lightmapper classes. Lightmappers can then be used with LightmapGI to provide fast baked global illumination in 3D.

### LimitAngularVelocityModifier3D
*Inherits: **SkeletonModifier3D < Node3D < Node < Object***

This modifier limits bone rotation angular velocity by comparing poses between previous and current frame.

**Properties**
- `int ChainCount` = `0`
- `bool Exclude` = `false`
- `int JointCount` = `0`
- `float MaxAngularVelocity` = `6.2831855`

**Methods**
- `void ClearChains()`
- `int GetEndBone(int index)`
- `string GetEndBoneName(int index)`
- `int GetRootBone(int index)`
- `string GetRootBoneName(int index)`
- `void Reset()`
- `void SetEndBone(int index, int bone)`
- `void SetEndBoneName(int index, string boneName)`
- `void SetRootBone(int index, int bone)`
- `void SetRootBoneName(int index, string boneName)`

### Logger
*Inherits: **RefCounted < Object***

Custom logger to receive messages from the internal error/warning stream. Loggers are registered via OS.add_logger().

**Methods**
- `void _LogError(string function, string file, int line, string code, string rationale, bool editorNotify, int errorType, Array[ScriptBacktrace] scriptBacktraces) [virtual]`
- `void _LogMessage(string message, bool error) [virtual]`

### MenuBar
*Inherits: **Control < CanvasItem < Node < Object***

A horizontal menu bar that creates a menu for each PopupMenu child. New items are created by adding PopupMenus to this node. Item title is determined by Window.title, or node name if Window.title is empty. Item title can be overridden using set_menu_title().

**Properties**
- `bool Flat` = `false`
- `FocusMode FocusMode` = `3 (overrides Control)`
- `string Language` = `""`
- `bool PreferGlobalMenu` = `true`
- `int StartIndex` = `-1`
- `bool SwitchOnHover` = `true`
- `TextDirection TextDirection` = `0`

**Methods**
- `int GetMenuCount()`
- `PopupMenu GetMenuPopup(int menu)`
- `string GetMenuTitle(int menu)`
- `string GetMenuTooltip(int menu)`
- `bool IsMenuDisabled(int menu)`
- `bool IsMenuHidden(int menu)`
- `bool IsNativeMenu()`
- `void SetDisableShortcuts(bool disabled)`
- `void SetMenuDisabled(int menu, bool disabled)`
- `void SetMenuHidden(int menu, bool hidden)`
- `void SetMenuTitle(int menu, string title)`
- `void SetMenuTooltip(int menu, string tooltip)`

### MeshConvexDecompositionSettings
*Inherits: **RefCounted < Object***

Parameters to be used with a Mesh convex decomposition operation.

**Properties**
- `bool ConvexHullApproximation` = `true`
- `int ConvexHullDownsampling` = `4`
- `float MaxConcavity` = `1.0`
- `int MaxConvexHulls` = `1`
- `int MaxNumVerticesPerConvexHull` = `32`
- `float MinVolumePerConvexHull` = `0.0001`
- `Mode Mode` = `0`
- `bool NormalizeMesh` = `false`
- `int PlaneDownsampling` = `4`
- `bool ProjectHullVertices` = `true`
- `int Resolution` = `10000`
- `float RevolutionAxesClippingBias` = `0.05`
- `float SymmetryPlanesClippingBias` = `0.05`

### MeshLibrary
*Inherits: **Resource < RefCounted < Object***

A library of meshes. Contains a list of Mesh resources, each with a name and ID. Each item can also include collision and navigation shapes. This resource is used in GridMap.

**Methods**
- `void Clear()`
- `void CreateItem(int id)`
- `int FindItemByName(string name)`
- `PackedInt32Array GetItemList()`
- `Mesh GetItemMesh(int id)`
- `ShadowCastingSetting GetItemMeshCastShadow(int id)`
- `Transform3D GetItemMeshTransform(int id)`
- `string GetItemName(int id)`
- `int GetItemNavigationLayers(int id)`
- `NavigationMesh GetItemNavigationMesh(int id)`
- `Transform3D GetItemNavigationMeshTransform(int id)`
- `Texture2D GetItemPreview(int id)`
- `Godot.Collections.Array GetItemShapes(int id)`
- `int GetLastUnusedItemId()`
- `void RemoveItem(int id)`
- `void SetItemMesh(int id, Mesh mesh)`
- `void SetItemMeshCastShadow(int id, ShadowCastingSetting shadowCastingSetting)`
- `void SetItemMeshTransform(int id, Transform3D meshTransform)`
- `void SetItemName(int id, string name)`
- `void SetItemNavigationLayers(int id, int navigationLayers)`
- `void SetItemNavigationMesh(int id, NavigationMesh navigationMesh)`
- `void SetItemNavigationMeshTransform(int id, Transform3D navigationMesh)`
- `void SetItemPreview(int id, Texture2D texture)`
- `void SetItemShapes(int id, Godot.Collections.Array shapes)`

### MeshTexture
*Inherits: **Texture2D < Texture < Resource < RefCounted < Object***

Simple texture that uses a mesh to draw itself. It's limited because flags can't be changed and region drawing is not supported.

**Properties**
- `Texture2D BaseTexture`
- `Vector2 ImageSize` = `Vector2(0, 0)`
- `Mesh Mesh`
- `bool ResourceLocalToScene` = `false (overrides Resource)`

### Mesh
*Inherits: **Resource < RefCounted < Object** | Inherited by: ArrayMesh, ImmediateMesh, PlaceholderMesh, PrimitiveMesh*

Mesh is a type of Resource that contains vertex array-based geometry, divided in surfaces. Each surface contains a completely separate array and a material used to draw it. Design wise, a mesh with multiple surfaces is preferred to a single surface, because objects created in 3D editing software commonly contain multiple materials. The maximum number of surfaces per mesh is RenderingServer.MAX_MESH_SURFACES.

**Properties**
- `Vector2i LightmapSizeHint` = `Vector2i(0, 0)`

**Methods**
- `AABB _GetAabb() [virtual]`
- `int _GetBlendShapeCount() [virtual]`
- `StringName _GetBlendShapeName(int index) [virtual]`
- `int _GetSurfaceCount() [virtual]`
- `void _SetBlendShapeName(int index, StringName name) [virtual]`
- `int _SurfaceGetArrayIndexLen(int index) [virtual]`
- `int _SurfaceGetArrayLen(int index) [virtual]`
- `Godot.Collections.Array _SurfaceGetArrays(int index) [virtual]`
- `Array[Array] _SurfaceGetBlendShapeArrays(int index) [virtual]`
- `int _SurfaceGetFormat(int index) [virtual]`
- `Godot.Collections.Dictionary _SurfaceGetLods(int index) [virtual]`
- `Material _SurfaceGetMaterial(int index) [virtual]`
- `int _SurfaceGetPrimitiveType(int index) [virtual]`
- `void _SurfaceSetMaterial(int index, Material material) [virtual]`
- `ConvexPolygonShape3D CreateConvexShape(bool clean = true, bool simplify = false)`
- `Mesh CreateOutline(float margin)`
- `Resource CreatePlaceholder()`
- `ConcavePolygonShape3D CreateTrimeshShape()`
- `TriangleMesh GenerateTriangleMesh()`
- `AABB GetAabb()`
- `PackedVector3Array GetFaces()`
- `int GetSurfaceCount()`
- `Godot.Collections.Array SurfaceGetArrays(int surfIdx)`
- `Array[Array] SurfaceGetBlendShapeArrays(int surfIdx)`
- `Material SurfaceGetMaterial(int surfIdx)`
- `void SurfaceSetMaterial(int surfIdx, Material material)`

### MissingNode
*Inherits: **Node < Object***

This is an internal editor class intended for keeping data of nodes of unknown type (most likely this type was supplied by an extension that is no longer loaded). It can't be manually instantiated or placed in a scene.

**Properties**
- `string OriginalClass`
- `string OriginalScene`
- `bool RecordingProperties`
- `bool RecordingSignals`

### MissingResource
*Inherits: **Resource < RefCounted < Object***

This is an internal editor class intended for keeping data of resources of unknown type (most likely this type was supplied by an extension that is no longer loaded). It can't be manually instantiated or placed in a scene.

**Properties**
- `string OriginalClass`
- `bool RecordingProperties`

### MobileVRInterface
*Inherits: **XRInterface < RefCounted < Object***

This is a generic mobile VR implementation where you need to provide details about the phone and HMD used. It does not rely on any existing framework. This is the most basic interface we have. For the best effect, you need a mobile phone with a gyroscope and accelerometer.

**Properties**
- `float DisplayToLens` = `4.0`
- `float DisplayWidth` = `14.5`
- `float EyeHeight` = `1.85`
- `float Iod` = `6.0`
- `float K1` = `0.215`
- `float K2` = `0.215`
- `Rect2 OffsetRect` = `Rect2(0, 0, 1, 1)`
- `float Oversample` = `1.5`
- `float VrsMinRadius` = `20.0`
- `float VrsStrength` = `1.0`
- `PlayAreaMode XrPlayAreaMode` = `1 (overrides XRInterface)`

### ModifierBoneTarget3D
*Inherits: **SkeletonModifier3D < Node3D < Node < Object***

This node selects a bone in a Skeleton3D and attaches to it. This means that the ModifierBoneTarget3D node will dynamically copy the 3D transform of the selected bone.

**Properties**
- `int Bone` = `-1`
- `string BoneName` = `""`

### MovieWriter
*Inherits: **Object***

Godot can record videos with non-real-time simulation. Like the --fixed-fps command line argument, this forces the reported delta in Node._process() functions to be identical across frames, regardless of how long it actually took to render the frame. This can be used to record high-quality videos with perfect frame pacing regardless of your hardware's capabilities.

**Methods**
- `int _GetAudioMixRate() [virtual]`
- `SpeakerMode _GetAudioSpeakerMode() [virtual]`
- `bool _HandlesFile(string path) [virtual]`
- `Error _WriteBegin(Vector2i movieSize, int fps, string basePath) [virtual]`
- `void _WriteEnd() [virtual]`
- `Error _WriteFrame(Image frameImage, const void* audioFrameBlock) [virtual]`
- `void AddWriter(MovieWriter writer) [static]`

### MultiplayerSpawner
*Inherits: **Node < Object***

Spawnable scenes can be configured in the editor or through code (see add_spawnable_scene()).

**Properties**
- `Callable SpawnFunction`
- `int SpawnLimit` = `0`
- `NodePath SpawnPath` = `NodePath("")`

**Methods**
- `void AddSpawnableScene(string path)`
- `void ClearSpawnableScenes()`
- `string GetSpawnableScene(int index)`
- `int GetSpawnableSceneCount()`
- `Node Spawn(Variant data = null)`

### MultiplayerSynchronizer
*Inherits: **Node < Object***

By default, MultiplayerSynchronizer synchronizes configured properties to all peers.

**Properties**
- `float DeltaInterval` = `0.0`
- `bool PublicVisibility` = `true`
- `SceneReplicationConfig ReplicationConfig`
- `float ReplicationInterval` = `0.0`
- `NodePath RootPath` = `NodePath("..")`
- `VisibilityUpdateMode VisibilityUpdateMode` = `0`

**Methods**
- `void AddVisibilityFilter(Callable filter)`
- `bool GetVisibilityFor(int peer)`
- `void RemoveVisibilityFilter(Callable filter)`
- `void SetVisibilityFor(int peer, bool visible)`
- `void UpdateVisibility(int forPeer = 0)`

### Mutex
*Inherits: **RefCounted < Object***

A synchronization mutex (mutual exclusion). This is used to synchronize multiple Threads, and is equivalent to a binary Semaphore. It guarantees that only one thread can access a critical section at a time.

**Methods**
- `void Lock()`
- `bool TryLock()`
- `void Unlock()`

### NativeMenu
*Inherits: **Object***

NativeMenu handles low-level access to the OS native global menu bar and popup menus.

**Methods**
- `int AddCheckItem(RID rid, string label, Callable callback = Callable(), Callable keyCallback = Callable(), Variant tag = null, Key accelerator = 0, int index = -1)`
- `int AddIconCheckItem(RID rid, Texture2D icon, string label, Callable callback = Callable(), Callable keyCallback = Callable(), Variant tag = null, Key accelerator = 0, int index = -1)`
- `int AddIconItem(RID rid, Texture2D icon, string label, Callable callback = Callable(), Callable keyCallback = Callable(), Variant tag = null, Key accelerator = 0, int index = -1)`
- `int AddIconRadioCheckItem(RID rid, Texture2D icon, string label, Callable callback = Callable(), Callable keyCallback = Callable(), Variant tag = null, Key accelerator = 0, int index = -1)`
- `int AddItem(RID rid, string label, Callable callback = Callable(), Callable keyCallback = Callable(), Variant tag = null, Key accelerator = 0, int index = -1)`
- `int AddMultistateItem(RID rid, string label, int maxStates, int defaultState, Callable callback = Callable(), Callable keyCallback = Callable(), Variant tag = null, Key accelerator = 0, int index = -1)`
- `int AddRadioCheckItem(RID rid, string label, Callable callback = Callable(), Callable keyCallback = Callable(), Variant tag = null, Key accelerator = 0, int index = -1)`
- `int AddSeparator(RID rid, int index = -1)`
- `int AddSubmenuItem(RID rid, string label, RID submenuRid, Variant tag = null, int index = -1)`
- `void Clear(RID rid)`
- `RID CreateMenu()`
- `int FindItemIndexWithSubmenu(RID rid, RID submenuRid)`
- `int FindItemIndexWithTag(RID rid, Variant tag)`
- `int FindItemIndexWithText(RID rid, string text)`
- `void FreeMenu(RID rid)`
- `Key GetItemAccelerator(RID rid, int idx)`
- `Callable GetItemCallback(RID rid, int idx)`
- `int GetItemCount(RID rid)`
- `Texture2D GetItemIcon(RID rid, int idx)`
- `int GetItemIndentationLevel(RID rid, int idx)`
- `Callable GetItemKeyCallback(RID rid, int idx)`
- `int GetItemMaxStates(RID rid, int idx)`
- `int GetItemState(RID rid, int idx)`
- `RID GetItemSubmenu(RID rid, int idx)`
- `Variant GetItemTag(RID rid, int idx)`
- `string GetItemText(RID rid, int idx)`
- `string GetItemTooltip(RID rid, int idx)`
- `float GetMinimumWidth(RID rid)`
- `Callable GetPopupCloseCallback(RID rid)`
- `Callable GetPopupOpenCallback(RID rid)`
- `Vector2 GetSize(RID rid)`
- `RID GetSystemMenu(SystemMenus menuId)`
- `string GetSystemMenuName(SystemMenus menuId)`
- `string GetSystemMenuText(SystemMenus menuId)`
- `bool HasFeature(Feature feature)`
- `bool HasMenu(RID rid)`
- `bool HasSystemMenu(SystemMenus menuId)`
- `bool IsItemCheckable(RID rid, int idx)`
- `bool IsItemChecked(RID rid, int idx)`
- `bool IsItemDisabled(RID rid, int idx)`

### NavigationMeshGenerator
*Inherits: **Object***

This class is responsible for creating and clearing 3D navigation meshes used as NavigationMesh resources inside NavigationRegion3D. The NavigationMeshGenerator has very limited to no use for 2D as the navigation mesh baking process expects 3D node types and 3D source geometry to parse.

**Methods**
- `void Bake(NavigationMesh navigationMesh, Node rootNode)`
- `void BakeFromSourceGeometryData(NavigationMesh navigationMesh, NavigationMeshSourceGeometryData3D sourceGeometryData, Callable callback = Callable())`
- `void Clear(NavigationMesh navigationMesh)`
- `void ParseSourceGeometryData(NavigationMesh navigationMesh, NavigationMeshSourceGeometryData3D sourceGeometryData, Node rootNode, Callable callback = Callable())`

### NavigationMeshSourceGeometryData2D
*Inherits: **Resource < RefCounted < Object***

Container for parsed source geometry data used in navigation mesh baking.

**Methods**
- `void AddObstructionOutline(PackedVector2Array shapeOutline)`
- `void AddProjectedObstruction(PackedVector2Array vertices, bool carve)`
- `void AddTraversableOutline(PackedVector2Array shapeOutline)`
- `void AppendObstructionOutlines(Array[PackedVector2Array] obstructionOutlines)`
- `void AppendTraversableOutlines(Array[PackedVector2Array] traversableOutlines)`
- `void Clear()`
- `void ClearProjectedObstructions()`
- `Rect2 GetBounds()`
- `Array[PackedVector2Array] GetObstructionOutlines()`
- `Godot.Collections.Array GetProjectedObstructions()`
- `Array[PackedVector2Array] GetTraversableOutlines()`
- `bool HasData()`
- `void Merge(NavigationMeshSourceGeometryData2D otherGeometry)`
- `void SetObstructionOutlines(Array[PackedVector2Array] obstructionOutlines)`
- `void SetProjectedObstructions(Godot.Collections.Array projectedObstructions)`
- `void SetTraversableOutlines(Array[PackedVector2Array] traversableOutlines)`

### NavigationMeshSourceGeometryData3D
*Inherits: **Resource < RefCounted < Object***

Container for parsed source geometry data used in navigation mesh baking.

**Methods**
- `void AddFaces(PackedVector3Array faces, Transform3D xform)`
- `void AddMesh(Mesh mesh, Transform3D xform)`
- `void AddMeshArray(Godot.Collections.Array meshArray, Transform3D xform)`
- `void AddProjectedObstruction(PackedVector3Array vertices, float elevation, float height, bool carve)`
- `void AppendArrays(PackedFloat32Array vertices, PackedInt32Array indices)`
- `void Clear()`
- `void ClearProjectedObstructions()`
- `AABB GetBounds()`
- `PackedInt32Array GetIndices()`
- `Godot.Collections.Array GetProjectedObstructions()`
- `PackedFloat32Array GetVertices()`
- `bool HasData()`
- `void Merge(NavigationMeshSourceGeometryData3D otherGeometry)`
- `void SetIndices(PackedInt32Array indices)`
- `void SetProjectedObstructions(Godot.Collections.Array projectedObstructions)`
- `void SetVertices(PackedFloat32Array vertices)`

### NavigationMesh
*Inherits: **Resource < RefCounted < Object***

A navigation mesh is a collection of polygons that define which areas of an environment are traversable to aid agents in pathfinding through complicated spaces.

**Properties**
- `float AgentHeight` = `1.5`
- `float AgentMaxClimb` = `0.25`
- `float AgentMaxSlope` = `45.0`
- `float AgentRadius` = `0.5`
- `float BorderSize` = `0.0`
- `float CellHeight` = `0.25`
- `float CellSize` = `0.25`
- `float DetailSampleDistance` = `6.0`
- `float DetailSampleMaxError` = `1.0`
- `float EdgeMaxError` = `1.3`
- `float EdgeMaxLength` = `0.0`
- `AABB FilterBakingAabb` = `AABB(0, 0, 0, 0, 0, 0)`
- `Vector3 FilterBakingAabbOffset` = `Vector3(0, 0, 0)`
- `bool FilterLedgeSpans` = `false`
- `bool FilterLowHangingObstacles` = `false`
- `bool FilterWalkableLowHeightSpans` = `false`
- `int GeometryCollisionMask` = `4294967295`
- `ParsedGeometryType GeometryParsedGeometryType` = `2`
- `SourceGeometryMode GeometrySourceGeometryMode` = `0`
- `StringName GeometrySourceGroupName` = `&"navigation_mesh_source_group"`
- `float RegionMergeSize` = `20.0`
- `float RegionMinSize` = `2.0`
- `SamplePartitionType SamplePartitionType` = `0`
- `float VerticesPerPolygon` = `6.0`

**Methods**
- `void AddPolygon(PackedInt32Array polygon)`
- `void Clear()`
- `void ClearPolygons()`
- `void CreateFromMesh(Mesh mesh)`
- `bool GetCollisionMaskValue(int layerNumber)`
- `PackedInt32Array GetPolygon(int idx)`
- `int GetPolygonCount()`
- `PackedVector3Array GetVertices()`
- `void SetCollisionMaskValue(int layerNumber, bool value)`
- `void SetVertices(PackedVector3Array vertices)`

### NavigationPathQueryParameters2D
*Inherits: **RefCounted < Object***

By changing various properties of this object, such as the start and target position, you can configure path queries to the NavigationServer2D.

**Properties**
- `Array[RID] ExcludedRegions` = `[]`
- `Array[RID] IncludedRegions` = `[]`
- `RID Map` = `RID()`
- `BitField[PathMetadataFlags] MetadataFlags` = `7`
- `int NavigationLayers` = `1`
- `PathPostProcessing PathPostprocessing` = `0`
- `float PathReturnMaxLength` = `0.0`
- `float PathReturnMaxRadius` = `0.0`
- `float PathSearchMaxDistance` = `0.0`
- `int PathSearchMaxPolygons` = `4096`
- `PathfindingAlgorithm PathfindingAlgorithm` = `0`
- `float SimplifyEpsilon` = `0.0`
- `bool SimplifyPath` = `false`
- `Vector2 StartPosition` = `Vector2(0, 0)`
- `Vector2 TargetPosition` = `Vector2(0, 0)`

### NavigationPathQueryParameters3D
*Inherits: **RefCounted < Object***

By changing various properties of this object, such as the start and target position, you can configure path queries to the NavigationServer3D.

**Properties**
- `Array[RID] ExcludedRegions` = `[]`
- `Array[RID] IncludedRegions` = `[]`
- `RID Map` = `RID()`
- `BitField[PathMetadataFlags] MetadataFlags` = `7`
- `int NavigationLayers` = `1`
- `PathPostProcessing PathPostprocessing` = `0`
- `float PathReturnMaxLength` = `0.0`
- `float PathReturnMaxRadius` = `0.0`
- `float PathSearchMaxDistance` = `0.0`
- `int PathSearchMaxPolygons` = `4096`
- `PathfindingAlgorithm PathfindingAlgorithm` = `0`
- `float SimplifyEpsilon` = `0.0`
- `bool SimplifyPath` = `false`
- `Vector3 StartPosition` = `Vector3(0, 0, 0)`
- `Vector3 TargetPosition` = `Vector3(0, 0, 0)`

### NavigationPathQueryResult2D
*Inherits: **RefCounted < Object***

This class stores the result of a 2D navigation path query from the NavigationServer2D.

**Properties**
- `PackedVector2Array Path` = `PackedVector2Array()`
- `float PathLength` = `0.0`
- `PackedInt64Array PathOwnerIds` = `PackedInt64Array()`
- `Array[RID] PathRids` = `[]`
- `PackedInt32Array PathTypes` = `PackedInt32Array()`

**Methods**
- `void Reset()`

### NavigationPathQueryResult3D
*Inherits: **RefCounted < Object***

This class stores the result of a 3D navigation path query from the NavigationServer3D.

**Properties**
- `PackedVector3Array Path` = `PackedVector3Array()`
- `float PathLength` = `0.0`
- `PackedInt64Array PathOwnerIds` = `PackedInt64Array()`
- `Array[RID] PathRids` = `[]`
- `PackedInt32Array PathTypes` = `PackedInt32Array()`

**Methods**
- `void Reset()`

### NavigationPolygon
*Inherits: **Resource < RefCounted < Object***

A navigation mesh can be created either by baking it with the help of the NavigationServer2D, or by adding vertices and convex polygon indices arrays manually.

**Properties**
- `float AgentRadius` = `10.0`
- `Rect2 BakingRect` = `Rect2(0, 0, 0, 0)`
- `Vector2 BakingRectOffset` = `Vector2(0, 0)`
- `float BorderSize` = `0.0`
- `float CellSize` = `1.0`
- `int ParsedCollisionMask` = `4294967295`
- `ParsedGeometryType ParsedGeometryType` = `2`
- `SamplePartitionType SamplePartitionType` = `0`
- `StringName SourceGeometryGroupName` = `&"navigation_polygon_source_geometry_group"`
- `SourceGeometryMode SourceGeometryMode` = `0`

**Methods**
- `void AddOutline(PackedVector2Array outline)`
- `void AddOutlineAtIndex(PackedVector2Array outline, int index)`
- `void AddPolygon(PackedInt32Array polygon)`
- `void Clear()`
- `void ClearOutlines()`
- `void ClearPolygons()`
- `NavigationMesh GetNavigationMesh()`
- `PackedVector2Array GetOutline(int idx)`
- `int GetOutlineCount()`
- `bool GetParsedCollisionMaskValue(int layerNumber)`
- `PackedInt32Array GetPolygon(int idx)`
- `int GetPolygonCount()`
- `PackedVector2Array GetVertices()`
- `void MakePolygonsFromOutlines()`
- `void RemoveOutline(int idx)`
- `void SetOutline(int idx, PackedVector2Array outline)`
- `void SetParsedCollisionMaskValue(int layerNumber, bool value)`
- `void SetVertices(PackedVector2Array vertices)`

**C# Examples**
```csharp
var newNavigationMesh = new NavigationPolygon();
Vector2[] boundingOutline = [new Vector2(0, 0), new Vector2(0, 50), new Vector2(50, 50), new Vector2(50, 0)];
newNavigationMesh.AddOutline(boundingOutline);
NavigationServer2D.BakeFromSourceGeometryData(newNavigationMesh, new NavigationMeshSourceGeometryData2D());
GetNode<NavigationRegion2D>("NavigationRegion2D").NavigationPolygon = newNavigationMesh;
```
```csharp
var newNavigationMesh = new NavigationPolygon();
Vector2[] newVertices = [new Vector2(0, 0), new Vector2(0, 50), new Vector2(50, 50), new Vector2(50, 0)];
newNavigationMesh.Vertices = newVertices;
int[] newPolygonIndices = [0, 1, 2, 3];
newNavigationMesh.AddPolygon(newPolygonIndices);
GetNode<NavigationRegion2D>("NavigationRegion2D").NavigationPolygon = newNavigationMesh;
```

### NavigationServer2DManager
*Inherits: **Object***

NavigationServer2DManager is the API for registering NavigationServer2D implementations and setting the default implementation.

**Methods**
- `void RegisterServer(string name, Callable createCallback)`
- `void SetDefaultServer(string name, int priority)`

### NavigationServer2D
*Inherits: **Object***

NavigationServer2D is the server that handles navigation maps, regions and agents. It does not handle A* navigation from AStar2D or AStarGrid2D.

**Methods**
- `RID AgentCreate()`
- `bool AgentGetAvoidanceEnabled(RID agent)`
- `int AgentGetAvoidanceLayers(RID agent)`
- `int AgentGetAvoidanceMask(RID agent)`
- `float AgentGetAvoidancePriority(RID agent)`
- `RID AgentGetMap(RID agent)`
- `int AgentGetMaxNeighbors(RID agent)`
- `float AgentGetMaxSpeed(RID agent)`
- `float AgentGetNeighborDistance(RID agent)`
- `bool AgentGetPaused(RID agent)`
- `Vector2 AgentGetPosition(RID agent)`
- `float AgentGetRadius(RID agent)`
- `float AgentGetTimeHorizonAgents(RID agent)`
- `float AgentGetTimeHorizonObstacles(RID agent)`
- `Vector2 AgentGetVelocity(RID agent)`
- `bool AgentHasAvoidanceCallback(RID agent)`
- `bool AgentIsMapChanged(RID agent)`
- `void AgentSetAvoidanceCallback(RID agent, Callable callback)`
- `void AgentSetAvoidanceEnabled(RID agent, bool enabled)`
- `void AgentSetAvoidanceLayers(RID agent, int layers)`
- `void AgentSetAvoidanceMask(RID agent, int mask)`
- `void AgentSetAvoidancePriority(RID agent, float priority)`
- `void AgentSetMap(RID agent, RID map)`
- `void AgentSetMaxNeighbors(RID agent, int count)`
- `void AgentSetMaxSpeed(RID agent, float maxSpeed)`
- `void AgentSetNeighborDistance(RID agent, float distance)`
- `void AgentSetPaused(RID agent, bool paused)`
- `void AgentSetPosition(RID agent, Vector2 position)`
- `void AgentSetRadius(RID agent, float radius)`
- `void AgentSetTimeHorizonAgents(RID agent, float timeHorizon)`
- `void AgentSetTimeHorizonObstacles(RID agent, float timeHorizon)`
- `void AgentSetVelocity(RID agent, Vector2 velocity)`
- `void AgentSetVelocityForced(RID agent, Vector2 velocity)`
- `void BakeFromSourceGeometryData(NavigationPolygon navigationPolygon, NavigationMeshSourceGeometryData2D sourceGeometryData, Callable callback = Callable())`
- `void BakeFromSourceGeometryDataAsync(NavigationPolygon navigationPolygon, NavigationMeshSourceGeometryData2D sourceGeometryData, Callable callback = Callable())`
- `void FreeRid(RID rid)`
- `bool GetDebugEnabled()`
- `Array[RID] GetMaps()`
- `int GetProcessInfo(ProcessInfo processInfo)`
- `bool IsBakingNavigationPolygon(NavigationPolygon navigationPolygon)`

### NavigationServer3DManager
*Inherits: **Object***

NavigationServer3DManager is the API for registering NavigationServer3D implementations and setting the default implementation.

**Methods**
- `void RegisterServer(string name, Callable createCallback)`
- `void SetDefaultServer(string name, int priority)`

### NavigationServer3D
*Inherits: **Object***

NavigationServer3D is the server that handles navigation maps, regions and agents. It does not handle A* navigation from AStar3D.

**Methods**
- `RID AgentCreate()`
- `bool AgentGetAvoidanceEnabled(RID agent)`
- `int AgentGetAvoidanceLayers(RID agent)`
- `int AgentGetAvoidanceMask(RID agent)`
- `float AgentGetAvoidancePriority(RID agent)`
- `float AgentGetHeight(RID agent)`
- `RID AgentGetMap(RID agent)`
- `int AgentGetMaxNeighbors(RID agent)`
- `float AgentGetMaxSpeed(RID agent)`
- `float AgentGetNeighborDistance(RID agent)`
- `bool AgentGetPaused(RID agent)`
- `Vector3 AgentGetPosition(RID agent)`
- `float AgentGetRadius(RID agent)`
- `float AgentGetTimeHorizonAgents(RID agent)`
- `float AgentGetTimeHorizonObstacles(RID agent)`
- `bool AgentGetUse3dAvoidance(RID agent)`
- `Vector3 AgentGetVelocity(RID agent)`
- `bool AgentHasAvoidanceCallback(RID agent)`
- `bool AgentIsMapChanged(RID agent)`
- `void AgentSetAvoidanceCallback(RID agent, Callable callback)`
- `void AgentSetAvoidanceEnabled(RID agent, bool enabled)`
- `void AgentSetAvoidanceLayers(RID agent, int layers)`
- `void AgentSetAvoidanceMask(RID agent, int mask)`
- `void AgentSetAvoidancePriority(RID agent, float priority)`
- `void AgentSetHeight(RID agent, float height)`
- `void AgentSetMap(RID agent, RID map)`
- `void AgentSetMaxNeighbors(RID agent, int count)`
- `void AgentSetMaxSpeed(RID agent, float maxSpeed)`
- `void AgentSetNeighborDistance(RID agent, float distance)`
- `void AgentSetPaused(RID agent, bool paused)`
- `void AgentSetPosition(RID agent, Vector3 position)`
- `void AgentSetRadius(RID agent, float radius)`
- `void AgentSetTimeHorizonAgents(RID agent, float timeHorizon)`
- `void AgentSetTimeHorizonObstacles(RID agent, float timeHorizon)`
- `void AgentSetUse3dAvoidance(RID agent, bool enabled)`
- `void AgentSetVelocity(RID agent, Vector3 velocity)`
- `void AgentSetVelocityForced(RID agent, Vector3 velocity)`
- `void BakeFromSourceGeometryData(NavigationMesh navigationMesh, NavigationMeshSourceGeometryData3D sourceGeometryData, Callable callback = Callable())`
- `void BakeFromSourceGeometryDataAsync(NavigationMesh navigationMesh, NavigationMeshSourceGeometryData3D sourceGeometryData, Callable callback = Callable())`
- `void FreeRid(RID rid)`

### NinePatchRect
*Inherits: **Control < CanvasItem < Node < Object***

Also known as 9-slice panels, NinePatchRect produces clean panels of any size based on a small texture. To do so, it splits the texture in a 3×3 grid. When you scale the node, it tiles the texture's edges horizontally or vertically, tiles the center on both axes, and leaves the corners unchanged.

**Properties**
- `AxisStretchMode AxisStretchHorizontal` = `0`
- `AxisStretchMode AxisStretchVertical` = `0`
- `bool DrawCenter` = `true`
- `MouseFilter MouseFilter` = `2 (overrides Control)`
- `int PatchMarginBottom` = `0`
- `int PatchMarginLeft` = `0`
- `int PatchMarginRight` = `0`
- `int PatchMarginTop` = `0`
- `Rect2 RegionRect` = `Rect2(0, 0, 0, 0)`
- `Texture2D Texture`

**Methods**
- `int GetPatchMargin(Side margin)`
- `void SetPatchMargin(Side margin, int value)`

### NodePath

The NodePath built-in Variant type represents a path to a node or property in a hierarchy of nodes. It is designed to be efficiently passed into many built-in methods (such as Node.get_node(), Object.set_indexed(), Tween.tween_property(), etc.) without a hard dependence on the node or property they point to.

**Methods**
- `NodePath GetAsPropertyPath()`
- `StringName GetConcatenatedNames()`
- `StringName GetConcatenatedSubnames()`
- `StringName GetName(int idx)`
- `int GetNameCount()`
- `StringName GetSubname(int idx)`
- `int GetSubnameCount()`
- `int Hash()`
- `bool IsAbsolute()`
- `bool IsEmpty()`
- `NodePath Slice(int begin, int end = 2147483647)`

**C# Examples**
```csharp
// nodePath points to the "x" property of the child node named "position".
var nodePath = new NodePath("position:x");

// propertyPath points to the "position" in the "x" axis of this node.
NodePath propertyPath = nodePath.GetAsPropertyPath();
GD.Print(propertyPath); // Prints ":position:x"
```
```csharp
var nodePath = new NodePath("Sprite2D:texture:resource_name");
GD.Print(nodePath.GetConcatenatedSubnames()); // Prints "texture:resource_name"
```

### Node
*Inherits: **Object** | Inherited by: AnimationMixer, AudioStreamPlayer, CanvasItem, CanvasLayer, EditorFileSystem, EditorPlugin, ...*

Nodes are Godot's building blocks. They can be assigned as the child of another node, resulting in a tree arrangement. A given node can contain any number of nodes as children with the requirement that all siblings (direct children of a node) should have unique names.

**Properties**
- `AutoTranslateMode AutoTranslateMode` = `0`
- `string EditorDescription` = `""`
- `MultiplayerAPI Multiplayer`
- `Node Owner`
- `PhysicsInterpolationMode PhysicsInterpolationMode` = `0`
- `ProcessMode ProcessMode` = `0`
- `int ProcessPhysicsPriority` = `0`
- `int ProcessPriority` = `0`
- `ProcessThreadGroup ProcessThreadGroup` = `0`
- `int ProcessThreadGroupOrder`
- `BitField[ProcessThreadMessages] ProcessThreadMessages`
- `string SceneFilePath`
- `bool UniqueNameInOwner` = `false`

**Methods**
- `void _EnterTree() [virtual]`
- `void _ExitTree() [virtual]`
- `PackedStringArray _GetAccessibilityConfigurationWarnings() [virtual]`
- `PackedStringArray _GetConfigurationWarnings() [virtual]`
- `RID _GetFocusedAccessibilityElement() [virtual]`
- `void _Input(InputEvent event) [virtual]`
- `void _PhysicsProcess(float delta) [virtual]`
- `void _Process(float delta) [virtual]`
- `void _Ready() [virtual]`
- `void _ShortcutInput(InputEvent event) [virtual]`
- `void _UnhandledInput(InputEvent event) [virtual]`
- `void _UnhandledKeyInput(InputEvent event) [virtual]`
- `void AddChild(Node node, bool forceReadableName = false, InternalMode internal = 0)`
- `void AddSibling(Node sibling, bool forceReadableName = false)`
- `void AddToGroup(StringName group, bool persistent = false)`
- `string Atr(string message, StringName context = "")`
- `string AtrN(string message, StringName pluralMessage, int n, StringName context = "")`
- `Variant CallDeferredThreadGroup(StringName method)`
- `Variant CallThreadSafe(StringName method)`
- `bool CanAutoTranslate()`
- `bool CanProcess()`
- `Tween CreateTween()`
- `Node Duplicate(int flags = 15)`
- `Node FindChild(string pattern, bool recursive = true, bool owned = true)`
- `Array[Node] FindChildren(string pattern, string type = "", bool recursive = true, bool owned = true)`
- `Node FindParent(string pattern)`
- `RID GetAccessibilityElement()`
- `Node GetChild(int idx, bool includeInternal = false)`
- `int GetChildCount(bool includeInternal = false)`
- `Array[Node] GetChildren(bool includeInternal = false)`
- `Array[StringName] GetGroups()`
- `int GetIndex(bool includeInternal = false)`
- `Window GetLastExclusiveWindow()`
- `int GetMultiplayerAuthority()`
- `Node GetNode(NodePath path)`
- `Godot.Collections.Array GetNodeAndResource(NodePath path)`
- `Node GetNodeOrNull(NodePath path)`
- `Variant GetNodeRpcConfig()`
- `Array[int] GetOrphanNodeIds() [static]`
- `Node GetParent()`

**C# Examples**
```csharp
Node childNode = GetChild(0);
if (childNode.GetParent() != null)
{
    childNode.GetParent().RemoveChild(childNode);
}
AddChild(childNode);
```
```csharp
GetTree().CreateTween().BindNode(this);
```

### NoiseTexture3D
*Inherits: **Texture3D < Texture < Resource < RefCounted < Object***

Uses the FastNoiseLite library or other noise generators to fill the texture data of your desired size.

**Properties**
- `Gradient ColorRamp`
- `int Depth` = `64`
- `int Height` = `64`
- `bool Invert` = `false`
- `Noise Noise`
- `bool Normalize` = `true`
- `bool Seamless` = `false`
- `float SeamlessBlendSkirt` = `0.1`
- `int Width` = `64`

### Noise
*Inherits: **Resource < RefCounted < Object** | Inherited by: FastNoiseLite*

This class defines the interface for noise generation libraries to inherit from.

**Methods**
- `Image GetImage(int width, int height, bool invert = false, bool in3dSpace = false, bool normalize = true)`
- `Array[Image] GetImage3d(int width, int height, int depth, bool invert = false, bool normalize = true)`
- `float GetNoise1d(float x)`
- `float GetNoise2d(float x, float y)`
- `float GetNoise2dv(Vector2 v)`
- `float GetNoise3d(float x, float y, float z)`
- `float GetNoise3dv(Vector3 v)`
- `Image GetSeamlessImage(int width, int height, bool invert = false, bool in3dSpace = false, float skirt = 0.1, bool normalize = true)`
- `Array[Image] GetSeamlessImage3d(int width, int height, int depth, bool invert = false, float skirt = 0.1, bool normalize = true)`

### OS
*Inherits: **Object***

The OS class wraps the most common functionalities for communicating with the host operating system, such as the video driver, delays, environment variables, execution of binaries, command line, etc.

**Properties**
- `bool DeltaSmoothing` = `true`
- `bool LowProcessorUsageMode` = `false`
- `int LowProcessorUsageModeSleepUsec` = `6900`

**Methods**
- `void AddLogger(Logger logger)`
- `void Alert(string text, string title = "Alert!")`
- `void CloseMidiInputs()`
- `void Crash(string message)`
- `int CreateInstance(PackedStringArray arguments)`
- `int CreateProcess(string path, PackedStringArray arguments, bool openConsole = false)`
- `void DelayMsec(int msec)`
- `void DelayUsec(int usec)`
- `int Execute(string path, PackedStringArray arguments, Godot.Collections.Array output = [], bool readStderr = false, bool openConsole = false)`
- `Godot.Collections.Dictionary ExecuteWithPipe(string path, PackedStringArray arguments, bool blocking = true)`
- `Key FindKeycodeFromString(string string)`
- `string GetCacheDir()`
- `PackedStringArray GetCmdlineArgs()`
- `PackedStringArray GetCmdlineUserArgs()`
- `string GetConfigDir()`
- `PackedStringArray GetConnectedMidiInputs()`
- `string GetDataDir()`
- `string GetDistributionName()`
- `PackedByteArray GetEntropy(int size)`
- `string GetEnvironment(string variable)`
- `string GetExecutablePath()`
- `PackedStringArray GetGrantedPermissions()`
- `string GetKeycodeString(Key code)`
- `string GetLocale()`
- `string GetLocaleLanguage()`
- `int GetMainThreadId()`
- `Godot.Collections.Dictionary GetMemoryInfo()`
- `string GetModelName()`
- `string GetName()`
- `int GetProcessExitCode(int pid)`
- `int GetProcessId()`
- `int GetProcessorCount()`
- `string GetProcessorName()`
- `PackedStringArray GetRestartOnExitArguments()`
- `int GetStaticMemoryPeakUsage()`
- `int GetStaticMemoryUsage()`
- `StdHandleType GetStderrType()`
- `StdHandleType GetStdinType()`
- `StdHandleType GetStdoutType()`
- `string GetSystemCaCertificates()`

**C# Examples**
```csharp
var pid = OS.CreateProcess(OS.GetExecutablePath(), []);
```
```csharp
Godot.Collections.Array output = [];
int exitCode = OS.Execute("ls", ["-l", "/tmp"], output);
```

### OccluderPolygon2D
*Inherits: **Resource < RefCounted < Object***

Editor facility that helps you draw a 2D polygon used as resource for LightOccluder2D.

**Properties**
- `bool Closed` = `true`
- `CullMode CullMode` = `0`
- `PackedVector2Array Polygon` = `PackedVector2Array()`

### OfflineMultiplayerPeer
*Inherits: **MultiplayerPeer < PacketPeer < RefCounted < Object***

This is the default MultiplayerAPI.multiplayer_peer for the Node.multiplayer. It mimics the behavior of a server with no peers connected.

### OggPacketSequencePlayback
*Inherits: **RefCounted < Object***

There is currently no description for this class. Please help us by contributing one!

### OggPacketSequence
*Inherits: **Resource < RefCounted < Object***

A sequence of Ogg packets.

**Properties**
- `PackedInt64Array GranulePositions` = `PackedInt64Array()`
- `Array[Array] PacketData` = `[]`
- `float SamplingRate` = `0.0`

**Methods**
- `float GetLength()`

### OpenXRAPIExtension
*Inherits: **RefCounted < Object***

OpenXRAPIExtension makes OpenXR available for GDExtension. It provides the OpenXR API to GDExtension through the get_instance_proc_addr() method, and the OpenXR instance through get_instance().

**Methods**
- `int ActionGetHandle(RID action)`
- `void BeginDebugLabelRegion(string labelName)`
- `bool CanRender()`
- `void EndDebugLabelRegion()`
- `RID FindAction(string name, RID actionSet)`
- `string GetErrorString(int result)`
- `int GetHandTracker(int handIndex)`
- `int GetInstance()`
- `int GetInstanceProcAddr(string name)`
- `int GetNextFrameTime()`
- `int GetOpenxrVersion()`
- `int GetPlaySpace()`
- `int GetPredictedDisplayTime()`
- `int GetProjectionLayer()`
- `float GetRenderStateZFar()`
- `float GetRenderStateZNear()`
- `int GetSession()`
- `PackedInt64Array GetSupportedSwapchainFormats()`
- `string GetSwapchainFormatName(int swapchainFormat)`
- `int GetSystemId()`
- `void InsertDebugLabel(string labelName)`
- `OpenXRAlphaBlendModeSupport IsEnvironmentBlendModeAlphaSupported()`
- `bool IsInitialized()`
- `bool IsRunning()`
- `bool OpenxrIsEnabled(bool checkRunInEditor) [static]`
- `void OpenxrSwapchainAcquire(int swapchain)`
- `int OpenxrSwapchainCreate(int createFlags, int usageFlags, int swapchainFormat, int width, int height, int sampleCount, int arraySize)`
- `void OpenxrSwapchainFree(int swapchain)`
- `RID OpenxrSwapchainGetImage(int swapchain)`
- `int OpenxrSwapchainGetSwapchain(int swapchain)`
- `void OpenxrSwapchainRelease(int swapchain)`
- `void RegisterCompositionLayerProvider(OpenXRExtensionWrapper extension)`
- `void RegisterFrameInfoExtension(OpenXRExtensionWrapper extension)`
- `void RegisterProjectionViewsExtension(OpenXRExtensionWrapper extension)`
- `void SetCustomPlaySpace(const void* space)`
- `void SetEmulateEnvironmentBlendModeAlphaBlend(bool enabled)`
- `void SetObjectName(int objectType, int objectHandle, string objectName)`
- `void SetRenderRegion(Rect2i renderRegion)`
- `void SetVelocityDepthTexture(RID renderTarget)`
- `void SetVelocityTargetSize(Vector2i targetSize)`

### OpenXRActionBindingModifier
*Inherits: **OpenXRBindingModifier < Resource < RefCounted < Object** | Inherited by: OpenXRAnalogThresholdModifier*

Binding modifier that applies on individual actions related to an interaction profile.

### OpenXRActionMap
*Inherits: **Resource < RefCounted < Object***

OpenXR uses an action system similar to Godots Input map system to bind inputs and outputs on various types of XR controllers to named actions. OpenXR specifies more detail on these inputs and outputs than Godot supports.

**Properties**
- `Godot.Collections.Array ActionSets` = `[]`
- `Godot.Collections.Array InteractionProfiles` = `[]`

**Methods**
- `void AddActionSet(OpenXRActionSet actionSet)`
- `void AddInteractionProfile(OpenXRInteractionProfile interactionProfile)`
- `void CreateDefaultActionSets()`
- `OpenXRActionSet FindActionSet(string name)`
- `OpenXRInteractionProfile FindInteractionProfile(string name)`
- `OpenXRActionSet GetActionSet(int idx)`
- `int GetActionSetCount()`
- `OpenXRInteractionProfile GetInteractionProfile(int idx)`
- `int GetInteractionProfileCount()`
- `void RemoveActionSet(OpenXRActionSet actionSet)`
- `void RemoveInteractionProfile(OpenXRInteractionProfile interactionProfile)`

### OpenXRActionSet
*Inherits: **Resource < RefCounted < Object***

Action sets in OpenXR define a collection of actions that can be activated in unison. This allows games to easily change between different states that require different inputs or need to reinterpret inputs. For instance we could have an action set that is active when a menu is open, an action set that is active when the player is freely walking around and an action set that is active when the player is controlling a vehicle.

**Properties**
- `Godot.Collections.Array Actions` = `[]`
- `string LocalizedName` = `""`
- `int Priority` = `0`

**Methods**
- `void AddAction(OpenXRAction action)`
- `int GetActionCount()`
- `void RemoveAction(OpenXRAction action)`

### OpenXRAction
*Inherits: **Resource < RefCounted < Object***

This resource defines an OpenXR action. Actions can be used both for inputs (buttons, joysticks, triggers, etc.) and outputs (haptics).

**Properties**
- `ActionType ActionType` = `1`
- `string LocalizedName` = `""`
- `PackedStringArray ToplevelPaths` = `PackedStringArray()`

### OpenXRAnalogThresholdModifier
*Inherits: **OpenXRActionBindingModifier < OpenXRBindingModifier < Resource < RefCounted < Object***

The analog threshold binding modifier can modify a float input to a boolean input with specified thresholds.

**Properties**
- `OpenXRHapticBase OffHaptic`
- `float OffThreshold` = `0.4`
- `OpenXRHapticBase OnHaptic`
- `float OnThreshold` = `0.6`

### OpenXRAnchorTracker
*Inherits: **OpenXRSpatialEntityTracker < XRPositionalTracker < XRTracker < RefCounted < Object***

Positional tracker for our OpenXR spatial entity anchor extension, it tracks a user defined location in real space and maps it to our virtual space.

**Properties**
- `string Uuid` = `""`

**Methods**
- `bool HasUuid()`

### OpenXRAndroidThreadSettingsExtension
*Inherits: **OpenXRExtensionWrapper < Object***

For XR to be comfortable, it is important for applications to deliver frames quickly and consistently. In order to make sure the important application threads get their full share of time, these threads must be identified to the system, which will adjust their scheduling priority accordingly.

**Methods**
- `bool SetApplicationThreadType(ThreadType threadType, int threadId = 0)`

### OpenXRBindingModifierEditor
*Inherits: **PanelContainer < Container < Control < CanvasItem < Node < Object***

This is the default binding modifier editor used in the OpenXR action map.

**Properties**
- `BitField[SizeFlags] SizeFlagsHorizontal` = `3 (overrides Control)`

**Methods**
- `OpenXRBindingModifier GetBindingModifier()`
- `void Setup(OpenXRActionMap actionMap, OpenXRBindingModifier bindingModifier)`

### OpenXRBindingModifier
*Inherits: **Resource < RefCounted < Object** | Inherited by: OpenXRActionBindingModifier, OpenXRIPBindingModifier*

Binding modifier base class. Subclasses implement various modifiers that alter how an OpenXR runtime processes inputs.

**Methods**
- `string _GetDescription() [virtual]`
- `PackedByteArray _GetIpModification() [virtual]`

### OpenXRCompositionLayerCylinder
*Inherits: **OpenXRCompositionLayer < Node3D < Node < Object***

An OpenXR composition layer that allows rendering a SubViewport on an internal slice of a cylinder.

**Properties**
- `float AspectRatio` = `1.0`
- `float CentralAngle` = `1.5707964`
- `int FallbackSegments` = `10`
- `float Radius` = `1.0`

### OpenXRCompositionLayerEquirect
*Inherits: **OpenXRCompositionLayer < Node3D < Node < Object***

An OpenXR composition layer that allows rendering a SubViewport on an internal slice of a sphere.

**Properties**
- `float CentralHorizontalAngle` = `1.5707964`
- `int FallbackSegments` = `10`
- `float LowerVerticalAngle` = `0.7853982`
- `float Radius` = `1.0`
- `float UpperVerticalAngle` = `0.7853982`

### OpenXRCompositionLayerQuad
*Inherits: **OpenXRCompositionLayer < Node3D < Node < Object***

An OpenXR composition layer that allows rendering a SubViewport on a quad.

**Properties**
- `Vector2 QuadSize` = `Vector2(1, 1)`

### OpenXRCompositionLayer
*Inherits: **Node3D < Node < Object** | Inherited by: OpenXRCompositionLayerCylinder, OpenXRCompositionLayerEquirect, OpenXRCompositionLayerQuad*

Composition layers allow 2D viewports to be displayed inside of the headset by the XR compositor through special projections that retain their quality. This allows for rendering clear text while keeping the layer at a native resolution.

**Properties**
- `bool AlphaBlend` = `false`
- `Vector2i AndroidSurfaceSize` = `Vector2i(1024, 1024)`
- `bool EnableHolePunch` = `false`
- `SubViewport LayerViewport`
- `bool ProtectedContent` = `false`
- `int SortOrder` = `1`
- `Swizzle SwapchainStateAlphaSwizzle` = `3`
- `Swizzle SwapchainStateBlueSwizzle` = `2`
- `Color SwapchainStateBorderColor` = `Color(0, 0, 0, 0)`
- `Swizzle SwapchainStateGreenSwizzle` = `1`
- `Wrap SwapchainStateHorizontalWrap` = `0`
- `Filter SwapchainStateMagFilter` = `1`
- `float SwapchainStateMaxAnisotropy` = `1.0`
- `Filter SwapchainStateMinFilter` = `1`
- `MipmapMode SwapchainStateMipmapMode` = `2`
- `Swizzle SwapchainStateRedSwizzle` = `0`
- `Wrap SwapchainStateVerticalWrap` = `0`
- `bool UseAndroidSurface` = `false`

**Methods**
- `JavaObject GetAndroidSurface()`
- `Vector2 IntersectsRay(Vector3 origin, Vector3 direction)`
- `bool IsNativelySupported()`

### OpenXRDpadBindingModifier
*Inherits: **OpenXRIPBindingModifier < OpenXRBindingModifier < Resource < RefCounted < Object***

The DPad binding modifier converts an axis input to a dpad output, emulating a DPad. New input paths for each dpad direction will be added to the interaction profile. When bound to actions the DPad emulation will be activated. You should not combine dpad inputs with normal inputs in the same action set for the same control, this will result in an error being returned when suggested bindings are submitted to OpenXR.

**Properties**
- `OpenXRActionSet ActionSet`
- `float CenterRegion` = `0.1`
- `string InputPath` = `""`
- `bool IsSticky` = `false`
- `OpenXRHapticBase OffHaptic`
- `OpenXRHapticBase OnHaptic`
- `float Threshold` = `0.6`
- `float ThresholdReleased` = `0.4`
- `float WedgeAngle` = `1.5707964`

### OpenXRExtensionWrapperExtension
*Inherits: **OpenXRExtensionWrapper < Object***

OpenXRExtensionWrapperExtension allows implementing OpenXR extensions with GDExtension. The extension should be registered with OpenXRExtensionWrapper.register_extension_wrapper().

### OpenXRExtensionWrapper
*Inherits: **Object** | Inherited by: OpenXRAndroidThreadSettingsExtension, OpenXRExtensionWrapperExtension, OpenXRFrameSynthesisExtension, OpenXRFutureExtension, OpenXRRenderModelExtension, OpenXRSpatialAnchorCapability, ...*

OpenXRExtensionWrapper allows implementing OpenXR extensions with GDExtension. The extension should be registered with register_extension_wrapper().

**Methods**
- `int _GetCompositionLayer(int index) [virtual]`
- `int _GetCompositionLayerCount() [virtual]`
- `int _GetCompositionLayerOrder(int index) [virtual]`
- `Godot.Collections.Dictionary _GetRequestedExtensions(int xrVersion) [virtual]`
- `PackedStringArray _GetSuggestedTrackerNames() [virtual]`
- `Array[Dictionary] _GetViewportCompositionLayerExtensionProperties() [virtual]`
- `Godot.Collections.Dictionary _GetViewportCompositionLayerExtensionPropertyDefaults() [virtual]`
- `void _OnBeforeInstanceCreated() [virtual]`
- `bool _OnEventPolled(const void* event) [virtual]`
- `void _OnInstanceCreated(int instance) [virtual]`
- `void _OnInstanceDestroyed() [virtual]`
- `void _OnMainSwapchainsCreated() [virtual]`
- `void _OnPostDrawViewport(RID viewport) [virtual]`
- `void _OnPreDrawViewport(RID viewport) [virtual]`
- `void _OnPreRender() [virtual]`
- `void _OnProcess() [virtual]`
- `void _OnRegisterMetadata() [virtual]`
- `void _OnSessionCreated(int session) [virtual]`
- `void _OnSessionDestroyed() [virtual]`
- `void _OnStateExiting() [virtual]`
- `void _OnStateFocused() [virtual]`
- `void _OnStateIdle() [virtual]`
- `void _OnStateLossPending() [virtual]`
- `void _OnStateReady() [virtual]`
- `void _OnStateStopping() [virtual]`
- `void _OnStateSynchronized() [virtual]`
- `void _OnStateVisible() [virtual]`
- `void _OnSyncActions() [virtual]`
- `void _OnViewportCompositionLayerDestroyed(const void* layer) [virtual]`
- `void _PrepareViewConfiguration(int viewCount) [virtual]`
- `void _PrintViewConfigurationInfo(int view) [virtual]`
- `int _SetAndroidSurfaceSwapchainCreateInfoAndGetNextPointer(Godot.Collections.Dictionary propertyValues, void* nextPointer) [virtual]`
- `int _SetFrameEndInfoAndGetNextPointer(void* nextPointer) [virtual]`
- `int _SetFrameWaitInfoAndGetNextPointer(void* nextPointer) [virtual]`
- `int _SetHandJointLocationsAndGetNextPointer(int handIndex, void* nextPointer) [virtual]`
- `int _SetInstanceCreateInfoAndGetNextPointer(int xrVersion, void* nextPointer) [virtual]`
- `int _SetProjectionViewsAndGetNextPointer(int viewIndex, void* nextPointer) [virtual]`
- `int _SetReferenceSpaceCreateInfoAndGetNextPointer(int referenceSpaceType, void* nextPointer) [virtual]`
- `int _SetSessionCreateAndGetNextPointer(void* nextPointer) [virtual]`
- `int _SetSwapchainCreateInfoAndGetNextPointer(void* nextPointer) [virtual]`

### OpenXRFrameSynthesisExtension
*Inherits: **OpenXRExtensionWrapper < Object***

This class implements the OpenXR Frame synthesis extension. When enabled in the project settings and supported by the XR runtime in use, frame synthesis uses advanced reprojection techniques to inject additional frames so that your XR experience hits the full frame rate of the device.

**Properties**
- `bool Enabled` = `false`
- `bool RelaxFrameInterval` = `false`

**Methods**
- `bool IsAvailable()`
- `void SkipNextFrame()`

### OpenXRFutureExtension
*Inherits: **OpenXRExtensionWrapper < Object***

This is a support extension in OpenXR that allows other OpenXR extensions to start asynchronous functions and get a callback after this function finishes. It is not intended for consumption within GDScript but can be accessed from GDExtension.

**Methods**
- `void CancelFuture(int future)`
- `bool IsActive()`
- `OpenXRFutureResult RegisterFuture(int future, Callable onSuccess = Callable())`

### OpenXRFutureResult
*Inherits: **RefCounted < Object***

Result object tracking the asynchronous result of an OpenXR Future object, you can use this object to track the result status.

**Methods**
- `void CancelFuture()`
- `int GetFuture()`
- `Variant GetResultValue()`
- `ResultStatus GetStatus()`
- `void SetResultValue(Variant resultValue)`

### OpenXRHand
*Inherits: **Node3D < Node < Object***

This node enables OpenXR's hand tracking functionality. The node should be a child node of an XROrigin3D node, tracking will update its position to the player's tracked hand Palm joint location (the center of the middle finger's metacarpal bone). This node also updates the skeleton of a properly skinned hand or avatar model.

**Properties**
- `BoneUpdate BoneUpdate` = `0`
- `Hands Hand` = `0`
- `NodePath HandSkeleton` = `NodePath("")`
- `MotionRange MotionRange` = `0`
- `SkeletonRig SkeletonRig` = `0`

### OpenXRHapticBase
*Inherits: **Resource < RefCounted < Object** | Inherited by: OpenXRHapticVibration*

This is a base class for haptic feedback resources.

### OpenXRHapticVibration
*Inherits: **OpenXRHapticBase < Resource < RefCounted < Object***

This haptic feedback resource makes it possible to define a vibration based haptic feedback pulse that can be triggered through actions in the OpenXR action map.

**Properties**
- `float Amplitude` = `1.0`
- `int Duration` = `-1`
- `float Frequency` = `0.0`

### OpenXRIPBindingModifier
*Inherits: **OpenXRBindingModifier < Resource < RefCounted < Object** | Inherited by: OpenXRDpadBindingModifier*

Binding modifier that applies directly on an interaction profile.

### OpenXRIPBinding
*Inherits: **Resource < RefCounted < Object***

This binding resource binds an OpenXRAction to an input or output. As most controllers have left hand and right versions that are handled by the same interaction profile we can specify multiple bindings. For instance an action "Fire" could be bound to both "/user/hand/left/input/trigger" and "/user/hand/right/input/trigger". This would require two binding entries.

**Properties**
- `OpenXRAction Action`
- `Godot.Collections.Array BindingModifiers` = `[]`
- `string BindingPath` = `""`
- `PackedStringArray Paths`

**Methods**
- `void AddPath(string path)`
- `OpenXRActionBindingModifier GetBindingModifier(int index)`
- `int GetBindingModifierCount()`
- `int GetPathCount()`
- `bool HasPath(string path)`
- `void RemovePath(string path)`

### OpenXRInteractionProfileEditorBase
*Inherits: **HBoxContainer < BoxContainer < Container < Control < CanvasItem < Node < Object** | Inherited by: OpenXRInteractionProfileEditor*

This is a base class for interaction profile editors used by the OpenXR action map editor. It can be used to create bespoke editors for specific interaction profiles.

**Properties**
- `BitField[SizeFlags] SizeFlagsHorizontal` = `3 (overrides Control)`
- `BitField[SizeFlags] SizeFlagsVertical` = `3 (overrides Control)`

**Methods**
- `void Setup(OpenXRActionMap actionMap, OpenXRInteractionProfile interactionProfile)`

### OpenXRInteractionProfileEditor
*Inherits: **OpenXRInteractionProfileEditorBase < HBoxContainer < BoxContainer < Container < Control < CanvasItem < Node < Object***

This is the default OpenXR interaction profile editor that provides a generic interface for editing any interaction profile for which no custom editor has been defined.

### OpenXRInteractionProfileMetadata
*Inherits: **Object***

This class allows OpenXR core and extensions to register metadata relating to supported interaction devices such as controllers, trackers, haptic devices, etc. It is primarily used by the action map editor and to sanitize any action map by removing extension-dependent entries when applicable.

**Methods**
- `void RegisterInteractionProfile(string displayName, string openxrPath, string openxrExtensionNames)`
- `void RegisterIoPath(string interactionProfile, string displayName, string toplevelPath, string openxrPath, string openxrExtensionNames, ActionType actionType)`
- `void RegisterPathRename(string oldName, string newName)`
- `void RegisterProfileRename(string oldName, string newName)`
- `void RegisterTopLevelPath(string displayName, string openxrPath, string openxrExtensionNames)`

### OpenXRInteractionProfile
*Inherits: **Resource < RefCounted < Object***

This object stores suggested bindings for an interaction profile. Interaction profiles define the metadata for a tracked XR device such as an XR controller.

**Properties**
- `Godot.Collections.Array BindingModifiers` = `[]`
- `Godot.Collections.Array Bindings` = `[]`
- `string InteractionProfilePath` = `""`

**Methods**
- `OpenXRIPBinding GetBinding(int index)`
- `int GetBindingCount()`
- `OpenXRIPBindingModifier GetBindingModifier(int index)`
- `int GetBindingModifierCount()`

### OpenXRInterface
*Inherits: **XRInterface < RefCounted < Object***

The OpenXR interface allows Godot to interact with OpenXR runtimes and make it possible to create XR experiences and games.

**Properties**
- `float DisplayRefreshRate` = `0.0`
- `bool FoveationDynamic` = `false`
- `int FoveationLevel` = `0`
- `float RenderTargetSizeMultiplier` = `1.0`
- `float VrsMinRadius` = `20.0`
- `float VrsStrength` = `1.0`

**Methods**
- `Godot.Collections.Array GetActionSets()`
- `Godot.Collections.Array GetAvailableDisplayRefreshRates()`
- `Vector3 GetHandJointAngularVelocity(Hand hand, HandJoints joint)`
- `BitField[HandJointFlags] GetHandJointFlags(Hand hand, HandJoints joint)`
- `Vector3 GetHandJointLinearVelocity(Hand hand, HandJoints joint)`
- `Vector3 GetHandJointPosition(Hand hand, HandJoints joint)`
- `float GetHandJointRadius(Hand hand, HandJoints joint)`
- `Quaternion GetHandJointRotation(Hand hand, HandJoints joint)`
- `HandTrackedSource GetHandTrackingSource(Hand hand)`
- `HandMotionRange GetMotionRange(Hand hand)`
- `SessionState GetSessionState()`
- `bool IsActionSetActive(string name)`
- `bool IsEyeGazeInteractionSupported()`
- `bool IsFoveationSupported()`
- `bool IsHandInteractionSupported()`
- `bool IsHandTrackingSupported()`
- `void SetActionSetActive(string name, bool active)`
- `void SetCpuLevel(PerfSettingsLevel level)`
- `void SetGpuLevel(PerfSettingsLevel level)`
- `void SetMotionRange(Hand hand, HandMotionRange motionRange)`

### OpenXRMarkerTracker
*Inherits: **OpenXRSpatialEntityTracker < XRPositionalTracker < XRTracker < RefCounted < Object***

Spatial entity tracker for our OpenXR spatial entity marker tracking extension. These trackers identify entities in our real space detected by a visual marker such as a QRCode or Aruco code, and map their location to our virtual space.

**Properties**
- `Vector2 BoundsSize` = `Vector2(0, 0)`
- `int MarkerId` = `0`
- `MarkerType MarkerType` = `0`

**Methods**
- `Variant GetMarkerData()`
- `void SetMarkerData(Variant markerData)`

### OpenXRPlaneTracker
*Inherits: **OpenXRSpatialEntityTracker < XRPositionalTracker < XRTracker < RefCounted < Object***

Spatial entity tracker for our OpenXR spatial entity plane tracking extension. These trackers identify entities in our real space such as walls, floors, tables, etc. and map their location to our virtual space.

**Properties**
- `Vector2 BoundsSize` = `Vector2(0, 0)`
- `PlaneAlignment PlaneAlignment` = `0`
- `string PlaneLabel` = `""`

**Methods**
- `void ClearMeshData()`
- `Mesh GetMesh()`
- `Transform3D GetMeshOffset()`
- `Shape3D GetShape(float thickness = 0.01)`
- `void SetMeshData(Transform3D origin, PackedVector2Array vertices, PackedInt32Array indices = PackedInt32Array())`

### OpenXRRenderModelExtension
*Inherits: **OpenXRExtensionWrapper < Object***

This class implements the OpenXR Render Model Extension, if enabled it will maintain a list of active render models and provides an interface to the render model data.

**Methods**
- `bool IsActive()`
- `RID RenderModelCreate(int renderModelId)`
- `void RenderModelDestroy(RID renderModel)`
- `Array[RID] RenderModelGetAll()`
- `int RenderModelGetAnimatableNodeCount(RID renderModel)`
- `string RenderModelGetAnimatableNodeName(RID renderModel, int index)`
- `Transform3D RenderModelGetAnimatableNodeTransform(RID renderModel, int index)`
- `TrackingConfidence RenderModelGetConfidence(RID renderModel)`
- `Transform3D RenderModelGetRootTransform(RID renderModel)`
- `PackedStringArray RenderModelGetSubactionPaths(RID renderModel)`
- `string RenderModelGetTopLevelPath(RID renderModel)`
- `bool RenderModelIsAnimatableNodeVisible(RID renderModel, int index)`
- `Node3D RenderModelNewSceneInstance(RID renderModel)`

### OpenXRRenderModelManager
*Inherits: **Node3D < Node < Object***

This helper node will automatically manage displaying render models. It will create new OpenXRRenderModel nodes as controllers and other hand held devices are detected, and remove those nodes when they are deactivated.

**Properties**
- `string MakeLocalToPose` = `""`
- `RenderModelTracker Tracker` = `0`

### OpenXRRenderModel
*Inherits: **Node3D < Node < Object***

This node will display an OpenXR render model by accessing the associated GLTF and processes all animation data (if supported by the XR runtime).

**Properties**
- `RID RenderModel` = `RID()`

**Methods**
- `string GetTopLevelPath()`

### OpenXRSpatialAnchorCapability
*Inherits: **OpenXRExtensionWrapper < Object***

This is an internal class that handles the OpenXR anchor spatial entity extension.

**Methods**
- `OpenXRAnchorTracker CreateNewAnchor(Transform3D transform, RID spatialContext = RID())`
- `OpenXRFutureResult CreatePersistenceContext(PersistenceScope scope, Callable userCallback = Callable())`
- `void FreePersistenceContext(RID persistenceContext)`
- `int GetPersistenceContextHandle(RID persistenceContext)`
- `bool IsPersistenceScopeSupported(PersistenceScope scope)`
- `bool IsSpatialAnchorSupported()`
- `bool IsSpatialPersistenceSupported()`
- `OpenXRFutureResult PersistAnchor(OpenXRAnchorTracker anchorTracker, RID persistenceContext = RID(), Callable userCallback = Callable())`
- `void RemoveAnchor(OpenXRAnchorTracker anchorTracker)`
- `OpenXRFutureResult UnpersistAnchor(OpenXRAnchorTracker anchorTracker, RID persistenceContext = RID(), Callable userCallback = Callable())`

### OpenXRSpatialCapabilityConfigurationAnchor
*Inherits: **OpenXRSpatialCapabilityConfigurationBaseHeader < RefCounted < Object***

Configuration header for spatial anchors. Pass this to OpenXRSpatialEntityExtension.create_spatial_context() to create a spatial context with spatial anchor capabilities.

**Methods**
- `PackedInt64Array GetEnabledComponents()`

### OpenXRSpatialCapabilityConfigurationAprilTag
*Inherits: **OpenXRSpatialCapabilityConfigurationBaseHeader < RefCounted < Object***

Configuration header for April tag markers. Pass this to OpenXRSpatialEntityExtension.create_spatial_context() to create a spatial context that can detect April tags.

**Properties**
- `AprilTagDict AprilDict` = `4`

**Methods**
- `PackedInt64Array GetEnabledComponents()`

### OpenXRSpatialCapabilityConfigurationAruco
*Inherits: **OpenXRSpatialCapabilityConfigurationBaseHeader < RefCounted < Object***

Configuration header for Aruco markers. Pass this to OpenXRSpatialEntityExtension.create_spatial_context() to create a spatial context that can detect Aruco markers.

**Properties**
- `ArucoDict ArucoDict` = `16`

**Methods**
- `PackedInt64Array GetEnabledComponents()`

### OpenXRSpatialCapabilityConfigurationBaseHeader
*Inherits: **RefCounted < Object** | Inherited by: OpenXRSpatialCapabilityConfigurationAnchor, OpenXRSpatialCapabilityConfigurationAprilTag, OpenXRSpatialCapabilityConfigurationAruco, OpenXRSpatialCapabilityConfigurationMicroQrCode, OpenXRSpatialCapabilityConfigurationPlaneTracking, OpenXRSpatialCapabilityConfigurationQrCode*

Wrapper base class for OpenXR Spatial Capability Configuration headers. This class needs to be implemented for each capability configuration structure usable within OpenXR's spatial entities system.

**Methods**
- `int _GetConfiguration() [virtual]`
- `bool _HasValidConfiguration() [virtual]`
- `bool HasValidConfiguration()`

### OpenXRSpatialCapabilityConfigurationMicroQrCode
*Inherits: **OpenXRSpatialCapabilityConfigurationBaseHeader < RefCounted < Object***

Configuration header for QR code markers. Pass this to OpenXRSpatialEntityExtension.create_spatial_context() to create a spatial context that can detect QR code markers.

**Methods**
- `PackedInt64Array GetEnabledComponents()`

### OpenXRSpatialCapabilityConfigurationPlaneTracking
*Inherits: **OpenXRSpatialCapabilityConfigurationBaseHeader < RefCounted < Object***

Configuration header for plane tracking. Pass this to OpenXRSpatialEntityExtension.create_spatial_context() to create a spatial context with plane tracking capabilities.

**Methods**
- `PackedInt64Array GetEnabledComponents()`
- `bool SupportsLabels()`
- `bool SupportsMesh2d()`
- `bool SupportsPolygons()`

### OpenXRSpatialCapabilityConfigurationQrCode
*Inherits: **OpenXRSpatialCapabilityConfigurationBaseHeader < RefCounted < Object***

Configuration header for micro QR code markers. Pass this to OpenXRSpatialEntityExtension.create_spatial_context() to create a spatial context that can detect micro QR code markers.

**Methods**
- `PackedInt64Array GetEnabledComponents()`

### OpenXRSpatialComponentAnchorList
*Inherits: **OpenXRSpatialComponentData < RefCounted < Object***

Object for storing the queries anchor result data when calling OpenXRSpatialEntityExtension.query_snapshot().

**Methods**
- `Transform3D GetEntityPose(int index)`

### OpenXRSpatialComponentBounded2DList
*Inherits: **OpenXRSpatialComponentData < RefCounted < Object***

Object for storing the queries 2D bounding rectangle result data when calling OpenXRSpatialEntityExtension.query_snapshot().

**Methods**
- `Transform3D GetCenterPose(int index)`
- `Vector2 GetSize(int index)`

### OpenXRSpatialComponentBounded3DList
*Inherits: **OpenXRSpatialComponentData < RefCounted < Object***

Object for storing the queries 3d bounding box result data when calling OpenXRSpatialEntityExtension.query_snapshot().

**Methods**
- `Transform3D GetCenterPose(int index)`
- `Vector3 GetSize(int index)`

### OpenXRSpatialComponentData
*Inherits: **RefCounted < Object** | Inherited by: OpenXRSpatialComponentAnchorList, OpenXRSpatialComponentBounded2DList, OpenXRSpatialComponentBounded3DList, OpenXRSpatialComponentMarkerList, OpenXRSpatialComponentMesh2DList, OpenXRSpatialComponentMesh3DList, ...*

Object for storing OpenXR spatial entity component data.

**Methods**
- `int _GetComponentType() [virtual]`
- `int _GetStructureData(int next) [virtual]`
- `void _SetCapacity(int capacity) [virtual]`
- `void SetCapacity(int capacity)`

### OpenXRSpatialComponentMarkerList
*Inherits: **OpenXRSpatialComponentData < RefCounted < Object***

Object for storing the queries marker result data when calling OpenXRSpatialEntityExtension.query_snapshot().

**Methods**
- `Variant GetMarkerData(RID snapshot, int index)`
- `int GetMarkerId(int index)`
- `MarkerType GetMarkerType(int index)`

### OpenXRSpatialComponentMesh2DList
*Inherits: **OpenXRSpatialComponentData < RefCounted < Object***

Object for storing the queries 2D mesh result data when calling OpenXRSpatialEntityExtension.query_snapshot().

**Methods**
- `PackedInt32Array GetIndices(RID snapshot, int index)`
- `Transform3D GetTransform(int index)`
- `PackedVector2Array GetVertices(RID snapshot, int index)`

### OpenXRSpatialComponentMesh3DList
*Inherits: **OpenXRSpatialComponentData < RefCounted < Object***

Object for storing the queries 3d mesh result data when calling OpenXRSpatialEntityExtension.query_snapshot().

**Methods**
- `Mesh GetMesh(int index)`
- `Transform3D GetTransform(int index)`

### OpenXRSpatialComponentParentList
*Inherits: **OpenXRSpatialComponentData < RefCounted < Object***

Object for storing the queries parent result data when calling OpenXRSpatialEntityExtension.query_snapshot().

**Methods**
- `RID GetParent(int index)`

### OpenXRSpatialComponentPersistenceList
*Inherits: **OpenXRSpatialComponentData < RefCounted < Object***

Object for storing the query persistence result data when calling OpenXRSpatialEntityExtension.query_snapshot().

**Methods**
- `int GetPersistentState(int index)`
- `string GetPersistentUuid(int index)`

### OpenXRSpatialComponentPlaneAlignmentList
*Inherits: **OpenXRSpatialComponentData < RefCounted < Object***

Object for storing the queries plane alignment result data when calling OpenXRSpatialEntityExtension.query_snapshot().

**Methods**
- `PlaneAlignment GetPlaneAlignment(int index)`

### OpenXRSpatialComponentPlaneSemanticLabelList
*Inherits: **OpenXRSpatialComponentData < RefCounted < Object***

Object for storing the queries plane semantic label result data when calling OpenXRSpatialEntityExtension.query_snapshot().

**Methods**
- `PlaneSemanticLabel GetPlaneSemanticLabel(int index)`

### OpenXRSpatialComponentPolygon2DList
*Inherits: **OpenXRSpatialComponentData < RefCounted < Object***

Object for storing the queries 2D polygon result data when calling OpenXRSpatialEntityExtension.query_snapshot().

**Methods**
- `Transform3D GetTransform(int index)`
- `PackedVector2Array GetVertices(RID snapshot, int index)`

### OpenXRSpatialContextPersistenceConfig
*Inherits: **OpenXRStructureBase < RefCounted < Object***

Configuration header for spatial persistence. Pass this to OpenXRSpatialEntityExtension.create_spatial_context() as the next parameter to create a spatial context with spatial persistence capabilities.

**Methods**
- `void AddPersistenceContext(RID persistenceContext)`
- `void RemovePersistenceContext(RID persistenceContext)`

### OpenXRSpatialEntityExtension
*Inherits: **OpenXRExtensionWrapper < Object***

OpenXR extension that handles spatial entities and, when enabled, allows querying those spatial entities. This extension will also automatically manage XRTracker objects for static entities.

**Methods**
- `RID AddSpatialEntity(RID spatialContext, int entityId, int entity)`
- `OpenXRFutureResult CreateSpatialContext(Array[OpenXRSpatialCapabilityConfigurationBaseHeader] capabilityConfigurations, OpenXRStructureBase next = null, Callable userCallback = Callable())`
- `OpenXRFutureResult DiscoverSpatialEntities(RID spatialContext, PackedInt64Array componentTypes, OpenXRStructureBase next = null, Callable userCallback = Callable())`
- `RID FindSpatialEntity(int entityId)`
- `void FreeSpatialContext(RID spatialContext)`
- `void FreeSpatialEntity(RID entity)`
- `void FreeSpatialSnapshot(RID spatialSnapshot)`
- `PackedFloat32Array GetFloatBuffer(RID spatialSnapshot, int bufferId)`
- `int GetSpatialContextHandle(RID spatialContext)`
- `bool GetSpatialContextReady(RID spatialContext)`
- `RID GetSpatialEntityContext(RID entity)`
- `int GetSpatialEntityId(RID entity)`
- `RID GetSpatialSnapshotContext(RID spatialSnapshot)`
- `int GetSpatialSnapshotHandle(RID spatialSnapshot)`
- `string GetString(RID spatialSnapshot, int bufferId)`
- `PackedByteArray GetUint8Buffer(RID spatialSnapshot, int bufferId)`
- `PackedInt32Array GetUint16Buffer(RID spatialSnapshot, int bufferId)`
- `PackedInt32Array GetUint32Buffer(RID spatialSnapshot, int bufferId)`
- `PackedVector2Array GetVector2Buffer(RID spatialSnapshot, int bufferId)`
- `PackedVector3Array GetVector3Buffer(RID spatialSnapshot, int bufferId)`
- `RID MakeSpatialEntity(RID spatialContext, int entityId)`
- `bool QuerySnapshot(RID spatialSnapshot, Array[OpenXRSpatialComponentData] componentData, OpenXRStructureBase next = null)`
- `bool SupportsCapability(Capability capability)`
- `bool SupportsComponentType(Capability capability, ComponentType componentType)`
- `RID UpdateSpatialEntities(RID spatialContext, Array[RID] entities, PackedInt64Array componentTypes, OpenXRStructureBase next = null)`

### OpenXRSpatialEntityTracker
*Inherits: **XRPositionalTracker < XRTracker < RefCounted < Object** | Inherited by: OpenXRAnchorTracker, OpenXRMarkerTracker, OpenXRPlaneTracker*

These are trackers created and managed by OpenXR's spatial entity extensions that give access to specific data related to OpenXR's spatial entities. They will always be of type TRACKER_ANCHOR.

**Properties**
- `RID Entity` = `RID()`
- `EntityTrackingState SpatialTrackingState` = `2`
- `TrackerType Type` = `8 (overrides XRTracker)`

### OpenXRSpatialMarkerTrackingCapability
*Inherits: **OpenXRExtensionWrapper < Object***

This class handles the OpenXR marker tracking spatial entity extension.

**Methods**
- `bool IsAprilTagSupported()`
- `bool IsArucoSupported()`
- `bool IsMicroQrcodeSupported()`
- `bool IsQrcodeSupported()`

### OpenXRSpatialPlaneTrackingCapability
*Inherits: **OpenXRExtensionWrapper < Object***

This class handles the OpenXR plane tracking spatial entity extension.

**Methods**
- `bool IsSupported()`

### OpenXRSpatialQueryResultData
*Inherits: **OpenXRSpatialComponentData < RefCounted < Object***

Object for storing the main query result data when calling OpenXRSpatialEntityExtension.query_snapshot(). This must always be the first component requested.

**Methods**
- `int GetCapacity()`
- `int GetEntityId(int index)`
- `EntityTrackingState GetEntityState(int index)`

### OpenXRStructureBase
*Inherits: **RefCounted < Object** | Inherited by: OpenXRSpatialContextPersistenceConfig*

Object for storing OpenXR structure data that is passed when calling into OpenXR APIs.

**Properties**
- `OpenXRStructureBase Next`

**Methods**
- `int _GetHeader(int next) [virtual]`
- `int GetStructureType()`

### OpenXRVisibilityMask
*Inherits: **VisualInstance3D < Node3D < Node < Object***

The visibility mask allows us to black out the part of the render result that is invisible due to lens distortion.

### OptimizedTranslation
*Inherits: **Translation < Resource < RefCounted < Object***

An optimized translation. Uses real-time compressed translations, which results in very small dictionaries.

**Methods**
- `void Generate(Translation from)`

### PackedByteArray

An array specifically designed to hold bytes. Packs data tightly, so it saves memory for large array sizes.

**Methods**
- `bool Append(int value)`
- `void AppendArray(PackedByteArray array)`
- `int Bsearch(int value, bool before = true)`
- `void Bswap16(int offset = 0, int count = -1)`
- `void Bswap32(int offset = 0, int count = -1)`
- `void Bswap64(int offset = 0, int count = -1)`
- `void Clear()`
- `PackedByteArray Compress(int compressionMode = 0)`
- `int Count(int value)`
- `float DecodeDouble(int byteOffset)`
- `float DecodeFloat(int byteOffset)`
- `float DecodeHalf(int byteOffset)`
- `int DecodeS8(int byteOffset)`
- `int DecodeS16(int byteOffset)`
- `int DecodeS32(int byteOffset)`
- `int DecodeS64(int byteOffset)`
- `int DecodeU8(int byteOffset)`
- `int DecodeU16(int byteOffset)`
- `int DecodeU32(int byteOffset)`
- `int DecodeU64(int byteOffset)`
- `Variant DecodeVar(int byteOffset, bool allowObjects = false)`
- `int DecodeVarSize(int byteOffset, bool allowObjects = false)`
- `PackedByteArray Decompress(int bufferSize, int compressionMode = 0)`
- `PackedByteArray DecompressDynamic(int maxOutputSize, int compressionMode = 0)`
- `PackedByteArray Duplicate()`
- `void EncodeDouble(int byteOffset, float value)`
- `void EncodeFloat(int byteOffset, float value)`
- `void EncodeHalf(int byteOffset, float value)`
- `void EncodeS8(int byteOffset, int value)`
- `void EncodeS16(int byteOffset, int value)`
- `void EncodeS32(int byteOffset, int value)`
- `void EncodeS64(int byteOffset, int value)`
- `void EncodeU8(int byteOffset, int value)`
- `void EncodeU16(int byteOffset, int value)`
- `void EncodeU32(int byteOffset, int value)`
- `void EncodeU64(int byteOffset, int value)`
- `int EncodeVar(int byteOffset, Variant value, bool allowObjects = false)`
- `bool Erase(int value)`
- `void Fill(int value)`
- `int Find(int value, int from = 0)`

**C# Examples**
```csharp
byte[] array = [11, 46, 255];
GD.Print(array.HexEncode()); // Prints "0b2eff"
```

### PackedColorArray

An array specifically designed to hold Color. Packs data tightly, so it saves memory for large array sizes.

**Methods**
- `bool Append(Color value)`
- `void AppendArray(PackedColorArray array)`
- `int Bsearch(Color value, bool before = true)`
- `void Clear()`
- `int Count(Color value)`
- `PackedColorArray Duplicate()`
- `bool Erase(Color value)`
- `void Fill(Color value)`
- `int Find(Color value, int from = 0)`
- `Color Get(int index)`
- `bool Has(Color value)`
- `int Insert(int atIndex, Color value)`
- `bool IsEmpty()`
- `bool PushBack(Color value)`
- `void RemoveAt(int index)`
- `int Resize(int newSize)`
- `void Reverse()`
- `int Rfind(Color value, int from = -1)`
- `void Set(int index, Color value)`
- `int Size()`
- `PackedColorArray Slice(int begin, int end = 2147483647)`
- `void Sort()`
- `PackedByteArray ToByteArray()`

### PackedDataContainerRef
*Inherits: **RefCounted < Object***

When packing nested containers using PackedDataContainer, they are recursively packed into PackedDataContainerRef (only applies to Array and Dictionary). Their data can be retrieved the same way as from PackedDataContainer.

**Methods**
- `int Size()`

### PackedDataContainer
*Inherits: **Resource < RefCounted < Object***

PackedDataContainer can be used to efficiently store data from untyped containers. The data is packed into raw bytes and can be saved to file. Only Array and Dictionary can be stored this way.

**Methods**
- `Error Pack(Variant value)`
- `int Size()`

### PackedFloat32Array

An array specifically designed to hold 32-bit floating-point values (float). Packs data tightly, so it saves memory for large array sizes.

**Methods**
- `bool Append(float value)`
- `void AppendArray(PackedFloat32Array array)`
- `int Bsearch(float value, bool before = true)`
- `void Clear()`
- `int Count(float value)`
- `PackedFloat32Array Duplicate()`
- `bool Erase(float value)`
- `void Fill(float value)`
- `int Find(float value, int from = 0)`
- `float Get(int index)`
- `bool Has(float value)`
- `int Insert(int atIndex, float value)`
- `bool IsEmpty()`
- `bool PushBack(float value)`
- `void RemoveAt(int index)`
- `int Resize(int newSize)`
- `void Reverse()`
- `int Rfind(float value, int from = -1)`
- `void Set(int index, float value)`
- `int Size()`
- `PackedFloat32Array Slice(int begin, int end = 2147483647)`
- `void Sort()`
- `PackedByteArray ToByteArray()`

### PackedFloat64Array

An array specifically designed to hold 64-bit floating-point values (double). Packs data tightly, so it saves memory for large array sizes.

**Methods**
- `bool Append(float value)`
- `void AppendArray(PackedFloat64Array array)`
- `int Bsearch(float value, bool before = true)`
- `void Clear()`
- `int Count(float value)`
- `PackedFloat64Array Duplicate()`
- `bool Erase(float value)`
- `void Fill(float value)`
- `int Find(float value, int from = 0)`
- `float Get(int index)`
- `bool Has(float value)`
- `int Insert(int atIndex, float value)`
- `bool IsEmpty()`
- `bool PushBack(float value)`
- `void RemoveAt(int index)`
- `int Resize(int newSize)`
- `void Reverse()`
- `int Rfind(float value, int from = -1)`
- `void Set(int index, float value)`
- `int Size()`
- `PackedFloat64Array Slice(int begin, int end = 2147483647)`
- `void Sort()`
- `PackedByteArray ToByteArray()`

### PackedInt32Array

An array specifically designed to hold 32-bit integer values. Packs data tightly, so it saves memory for large array sizes.

**Methods**
- `bool Append(int value)`
- `void AppendArray(PackedInt32Array array)`
- `int Bsearch(int value, bool before = true)`
- `void Clear()`
- `int Count(int value)`
- `PackedInt32Array Duplicate()`
- `bool Erase(int value)`
- `void Fill(int value)`
- `int Find(int value, int from = 0)`
- `int Get(int index)`
- `bool Has(int value)`
- `int Insert(int atIndex, int value)`
- `bool IsEmpty()`
- `bool PushBack(int value)`
- `void RemoveAt(int index)`
- `int Resize(int newSize)`
- `void Reverse()`
- `int Rfind(int value, int from = -1)`
- `void Set(int index, int value)`
- `int Size()`
- `PackedInt32Array Slice(int begin, int end = 2147483647)`
- `void Sort()`
- `PackedByteArray ToByteArray()`

### PackedInt64Array

An array specifically designed to hold 64-bit integer values. Packs data tightly, so it saves memory for large array sizes.

**Methods**
- `bool Append(int value)`
- `void AppendArray(PackedInt64Array array)`
- `int Bsearch(int value, bool before = true)`
- `void Clear()`
- `int Count(int value)`
- `PackedInt64Array Duplicate()`
- `bool Erase(int value)`
- `void Fill(int value)`
- `int Find(int value, int from = 0)`
- `int Get(int index)`
- `bool Has(int value)`
- `int Insert(int atIndex, int value)`
- `bool IsEmpty()`
- `bool PushBack(int value)`
- `void RemoveAt(int index)`
- `int Resize(int newSize)`
- `void Reverse()`
- `int Rfind(int value, int from = -1)`
- `void Set(int index, int value)`
- `int Size()`
- `PackedInt64Array Slice(int begin, int end = 2147483647)`
- `void Sort()`
- `PackedByteArray ToByteArray()`

### PackedStringArray

An array specifically designed to hold Strings. Packs data tightly, so it saves memory for large array sizes.

**Methods**
- `bool Append(string value)`
- `void AppendArray(PackedStringArray array)`
- `int Bsearch(string value, bool before = true)`
- `void Clear()`
- `int Count(string value)`
- `PackedStringArray Duplicate()`
- `bool Erase(string value)`
- `void Fill(string value)`
- `int Find(string value, int from = 0)`
- `string Get(int index)`
- `bool Has(string value)`
- `int Insert(int atIndex, string value)`
- `bool IsEmpty()`
- `bool PushBack(string value)`
- `void RemoveAt(int index)`
- `int Resize(int newSize)`
- `void Reverse()`
- `int Rfind(string value, int from = -1)`
- `void Set(int index, string value)`
- `int Size()`
- `PackedStringArray Slice(int begin, int end = 2147483647)`
- `void Sort()`
- `PackedByteArray ToByteArray()`

### PackedVector2Array

An array specifically designed to hold Vector2. Packs data tightly, so it saves memory for large array sizes.

**Methods**
- `bool Append(Vector2 value)`
- `void AppendArray(PackedVector2Array array)`
- `int Bsearch(Vector2 value, bool before = true)`
- `void Clear()`
- `int Count(Vector2 value)`
- `PackedVector2Array Duplicate()`
- `bool Erase(Vector2 value)`
- `void Fill(Vector2 value)`
- `int Find(Vector2 value, int from = 0)`
- `Vector2 Get(int index)`
- `bool Has(Vector2 value)`
- `int Insert(int atIndex, Vector2 value)`
- `bool IsEmpty()`
- `bool PushBack(Vector2 value)`
- `void RemoveAt(int index)`
- `int Resize(int newSize)`
- `void Reverse()`
- `int Rfind(Vector2 value, int from = -1)`
- `void Set(int index, Vector2 value)`
- `int Size()`
- `PackedVector2Array Slice(int begin, int end = 2147483647)`
- `void Sort()`
- `PackedByteArray ToByteArray()`

### PackedVector3Array

An array specifically designed to hold Vector3. Packs data tightly, so it saves memory for large array sizes.

**Methods**
- `bool Append(Vector3 value)`
- `void AppendArray(PackedVector3Array array)`
- `int Bsearch(Vector3 value, bool before = true)`
- `void Clear()`
- `int Count(Vector3 value)`
- `PackedVector3Array Duplicate()`
- `bool Erase(Vector3 value)`
- `void Fill(Vector3 value)`
- `int Find(Vector3 value, int from = 0)`
- `Vector3 Get(int index)`
- `bool Has(Vector3 value)`
- `int Insert(int atIndex, Vector3 value)`
- `bool IsEmpty()`
- `bool PushBack(Vector3 value)`
- `void RemoveAt(int index)`
- `int Resize(int newSize)`
- `void Reverse()`
- `int Rfind(Vector3 value, int from = -1)`
- `void Set(int index, Vector3 value)`
- `int Size()`
- `PackedVector3Array Slice(int begin, int end = 2147483647)`
- `void Sort()`
- `PackedByteArray ToByteArray()`

### PackedVector4Array

An array specifically designed to hold Vector4. Packs data tightly, so it saves memory for large array sizes.

**Methods**
- `bool Append(Vector4 value)`
- `void AppendArray(PackedVector4Array array)`
- `int Bsearch(Vector4 value, bool before = true)`
- `void Clear()`
- `int Count(Vector4 value)`
- `PackedVector4Array Duplicate()`
- `bool Erase(Vector4 value)`
- `void Fill(Vector4 value)`
- `int Find(Vector4 value, int from = 0)`
- `Vector4 Get(int index)`
- `bool Has(Vector4 value)`
- `int Insert(int atIndex, Vector4 value)`
- `bool IsEmpty()`
- `bool PushBack(Vector4 value)`
- `void RemoveAt(int index)`
- `int Resize(int newSize)`
- `void Reverse()`
- `int Rfind(Vector4 value, int from = -1)`
- `void Set(int index, Vector4 value)`
- `int Size()`
- `PackedVector4Array Slice(int begin, int end = 2147483647)`
- `void Sort()`
- `PackedByteArray ToByteArray()`

### Panel
*Inherits: **Control < CanvasItem < Node < Object***

Panel is a GUI control that displays a StyleBox. See also PanelContainer.

### PanoramaSkyMaterial
*Inherits: **Material < Resource < RefCounted < Object***

A resource referenced in a Sky that is used to draw a background. PanoramaSkyMaterial functions similar to skyboxes in other engines, except it uses an equirectangular sky map instead of a Cubemap.

**Properties**
- `float EnergyMultiplier` = `1.0`
- `bool Filter` = `true`
- `Texture2D Panorama`

### Parallax2D
*Inherits: **Node2D < CanvasItem < Node < Object***

A Parallax2D is used to create a parallax effect. It can move at a different speed relative to the camera movement using scroll_scale. This creates an illusion of depth in a 2D game. If manual scrolling is desired, the Camera2D position can be ignored with ignore_camera_scroll.

**Properties**
- `Vector2 Autoscroll` = `Vector2(0, 0)`
- `bool FollowViewport` = `true`
- `bool IgnoreCameraScroll` = `false`
- `Vector2 LimitBegin` = `Vector2(-10000000, -10000000)`
- `Vector2 LimitEnd` = `Vector2(10000000, 10000000)`
- `PhysicsInterpolationMode PhysicsInterpolationMode` = `2 (overrides Node)`
- `Vector2 RepeatSize` = `Vector2(0, 0)`
- `int RepeatTimes` = `1`
- `Vector2 ScreenOffset` = `Vector2(0, 0)`
- `Vector2 ScrollOffset` = `Vector2(0, 0)`
- `Vector2 ScrollScale` = `Vector2(1, 1)`

### ParallaxBackground
*Inherits: **CanvasLayer < Node < Object***

A ParallaxBackground uses one or more ParallaxLayer child nodes to create a parallax effect. Each ParallaxLayer can move at a different speed using ParallaxLayer.motion_offset. This creates an illusion of depth in a 2D game. If not used with a Camera2D, you must manually calculate the scroll_offset.

**Properties**
- `int Layer` = `-100 (overrides CanvasLayer)`
- `Vector2 ScrollBaseOffset` = `Vector2(0, 0)`
- `Vector2 ScrollBaseScale` = `Vector2(1, 1)`
- `bool ScrollIgnoreCameraZoom` = `false`
- `Vector2 ScrollLimitBegin` = `Vector2(0, 0)`
- `Vector2 ScrollLimitEnd` = `Vector2(0, 0)`
- `Vector2 ScrollOffset` = `Vector2(0, 0)`

### ParallaxLayer
*Inherits: **Node2D < CanvasItem < Node < Object***

A ParallaxLayer must be the child of a ParallaxBackground node. Each ParallaxLayer can be set to move at different speeds relative to the camera movement or the ParallaxBackground.scroll_offset value.

**Properties**
- `Vector2 MotionMirroring` = `Vector2(0, 0)`
- `Vector2 MotionOffset` = `Vector2(0, 0)`
- `Vector2 MotionScale` = `Vector2(1, 1)`
- `PhysicsInterpolationMode PhysicsInterpolationMode` = `2 (overrides Node)`

### PhysicalBone2D
*Inherits: **RigidBody2D < PhysicsBody2D < CollisionObject2D < Node2D < CanvasItem < Node < Object***

The PhysicalBone2D node is a RigidBody2D-based node that can be used to make Bone2Ds in a Skeleton2D react to physics.

**Properties**
- `bool AutoConfigureJoint` = `true`
- `int Bone2dIndex` = `-1`
- `NodePath Bone2dNodepath` = `NodePath("")`
- `bool FollowBoneWhenSimulating` = `false`
- `bool SimulatePhysics` = `false`

**Methods**
- `Joint2D GetJoint()`
- `bool IsSimulatingPhysics()`

### PhysicalBone3D
*Inherits: **PhysicsBody3D < CollisionObject3D < Node3D < Node < Object***

The PhysicalBone3D node is a physics body that can be used to make bones in a Skeleton3D react to physics.

**Properties**
- `float AngularDamp` = `0.0`
- `DampMode AngularDampMode` = `0`
- `Vector3 AngularVelocity` = `Vector3(0, 0, 0)`
- `Transform3D BodyOffset` = `Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0)`
- `float Bounce` = `0.0`
- `bool CanSleep` = `true`
- `bool CustomIntegrator` = `false`
- `float Friction` = `1.0`
- `float GravityScale` = `1.0`
- `Transform3D JointOffset` = `Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0)`
- `Vector3 JointRotation` = `Vector3(0, 0, 0)`
- `JointType JointType` = `0`
- `float LinearDamp` = `0.0`
- `DampMode LinearDampMode` = `0`
- `Vector3 LinearVelocity` = `Vector3(0, 0, 0)`
- `float Mass` = `1.0`

**Methods**
- `void _IntegrateForces(PhysicsDirectBodyState3D state) [virtual]`
- `void ApplyCentralImpulse(Vector3 impulse)`
- `void ApplyImpulse(Vector3 impulse, Vector3 position = Vector3(0, 0, 0))`
- `int GetBoneId()`
- `bool GetSimulatePhysics()`
- `bool IsSimulatingPhysics()`

### PhysicalBoneSimulator3D
*Inherits: **SkeletonModifier3D < Node3D < Node < Object***

Node that can be the parent of PhysicalBone3D and can apply the simulation results to Skeleton3D.

**Methods**
- `bool IsSimulatingPhysics()`
- `void PhysicalBonesAddCollisionException(RID exception)`
- `void PhysicalBonesRemoveCollisionException(RID exception)`
- `void PhysicalBonesStartSimulation(Array[StringName] bones = [])`
- `void PhysicalBonesStopSimulation()`

### PhysicalSkyMaterial
*Inherits: **Material < Resource < RefCounted < Object***

The PhysicalSkyMaterial uses the Preetham analytic daylight model to draw a sky based on physical properties. This results in a substantially more realistic sky than the ProceduralSkyMaterial, but it is slightly slower and less flexible.

**Properties**
- `float EnergyMultiplier` = `1.0`
- `Color GroundColor` = `Color(0.1, 0.07, 0.034, 1)`
- `float MieCoefficient` = `0.005`
- `Color MieColor` = `Color(0.69, 0.729, 0.812, 1)`
- `float MieEccentricity` = `0.8`
- `Texture2D NightSky`
- `float RayleighCoefficient` = `2.0`
- `Color RayleighColor` = `Color(0.3, 0.405, 0.6, 1)`
- `float SunDiskScale` = `1.0`
- `float Turbidity` = `10.0`
- `bool UseDebanding` = `true`

### PlaceholderCubemapArray
*Inherits: **PlaceholderTextureLayered < TextureLayered < Texture < Resource < RefCounted < Object***

This class replaces a CubemapArray or a CubemapArray-derived class in 2 conditions:

### PlaceholderCubemap
*Inherits: **PlaceholderTextureLayered < TextureLayered < Texture < Resource < RefCounted < Object***

This class replaces a Cubemap or a Cubemap-derived class in 2 conditions:

### PlaceholderMaterial
*Inherits: **Material < Resource < RefCounted < Object***

This class is used when loading a project that uses a Material subclass in 2 conditions:

### PlaceholderMesh
*Inherits: **Mesh < Resource < RefCounted < Object***

This class is used when loading a project that uses a Mesh subclass in 2 conditions:

**Properties**
- `AABB Aabb` = `AABB(0, 0, 0, 0, 0, 0)`

### PlaceholderTexture3D
*Inherits: **Texture3D < Texture < Resource < RefCounted < Object***

This class is used when loading a project that uses a Texture3D subclass in 2 conditions:

**Properties**
- `Vector3i Size` = `Vector3i(1, 1, 1)`

### PlaceholderTextureLayered
*Inherits: **TextureLayered < Texture < Resource < RefCounted < Object** | Inherited by: PlaceholderCubemap, PlaceholderCubemapArray, PlaceholderTexture2DArray*

This class is used when loading a project that uses a TextureLayered subclass in 2 conditions:

**Properties**
- `int Layers` = `1`
- `Vector2i Size` = `Vector2i(1, 1)`

### Plane

Represents a normalized plane equation. normal is the normal of the plane (a, b, c normalized), and d is the distance from the origin to the plane (in the direction of "normal"). "Over" or "Above" the plane is considered the side of the plane towards where the normal is pointing.

**Properties**
- `float D` = `0.0`
- `Vector3 Normal` = `Vector3(0, 0, 0)`
- `float X` = `0.0`
- `float Y` = `0.0`
- `float Z` = `0.0`

**Methods**
- `float DistanceTo(Vector3 point)`
- `Vector3 GetCenter()`
- `bool HasPoint(Vector3 point, float tolerance = 1e-05)`
- `Variant Intersect3(Plane b, Plane c)`
- `Variant IntersectsRay(Vector3 from, Vector3 dir)`
- `Variant IntersectsSegment(Vector3 from, Vector3 to)`
- `bool IsEqualApprox(Plane toPlane)`
- `bool IsFinite()`
- `bool IsPointOver(Vector3 point)`
- `Plane Normalized()`
- `Vector3 Project(Vector3 point)`

### PointLight2D
*Inherits: **Light2D < Node2D < CanvasItem < Node < Object***

Casts light in a 2D environment. This light's shape is defined by a (usually grayscale) texture.

**Properties**
- `float Height` = `0.0`
- `Vector2 Offset` = `Vector2(0, 0)`
- `Texture2D Texture`
- `float TextureScale` = `1.0`

### PointMesh
*Inherits: **PrimitiveMesh < Mesh < Resource < RefCounted < Object***

A PointMesh is a primitive mesh composed of a single point. Instead of relying on triangles, points are rendered as a single rectangle on the screen with a constant size. They are intended to be used with particle systems, but can also be used as a cheap way to render billboarded sprites (for example in a point cloud).

### PolygonOccluder3D
*Inherits: **Occluder3D < Resource < RefCounted < Object***

PolygonOccluder3D stores a polygon shape that can be used by the engine's occlusion culling system. When an OccluderInstance3D with a PolygonOccluder3D is selected in the editor, an editor will appear at the top of the 3D viewport so you can add/remove points. All points must be placed on the same 2D plane, which means it is not possible to create arbitrary 3D shapes with a single PolygonOccluder3D. To use arbitrary 3D shapes as occluders, use ArrayOccluder3D or OccluderInstance3D's baking feature instead.

**Properties**
- `PackedVector2Array Polygon` = `PackedVector2Array()`

### PolygonPathFinder
*Inherits: **Resource < RefCounted < Object***

There is currently no description for this class. Please help us by contributing one!

**Methods**
- `PackedVector2Array FindPath(Vector2 from, Vector2 to)`
- `Rect2 GetBounds()`
- `Vector2 GetClosestPoint(Vector2 point)`
- `PackedVector2Array GetIntersections(Vector2 from, Vector2 to)`
- `float GetPointPenalty(int idx)`
- `bool IsPointInside(Vector2 point)`
- `void SetPointPenalty(int idx, float penalty)`
- `void Setup(PackedVector2Array points, PackedInt32Array connections)`

**C# Examples**
```csharp
var polygonPathFinder = new PolygonPathFinder();
Vector2[] points =
[
    new Vector2(0.0f, 0.0f),
    new Vector2(1.0f, 0.0f),
    new Vector2(0.0f, 1.0f)
];
int[] connections = [0, 1, 1, 2, 2, 0];
polygonPathFinder.Setup(points, connections);
GD.Print(polygonPathFinder.IsPointInside(new Vector2(0.2f, 0.2f))); // Prints True
GD.Print(polygonPathFinder.IsPointInside(new Vector2(1.0f, 1.0f))); // Prints False
```
```csharp
var polygonPathFinder = new PolygonPathFinder();
Vector2[] points =
[
    new Vector2(0.0f, 0.0f),
    new Vector2(1.0f, 0.0f),
    new Vector2(0.0f, 1.0f)
];
int[] connections = [0, 1, 1, 2, 2, 0];
polygonPathFinder.Setup(points, connections);
```

### Popup
*Inherits: **Window < Viewport < Node < Object** | Inherited by: PopupMenu, PopupPanel*

Popup is a base class for contextual windows and panels with fixed position. It's a modal by default (see Window.popup_window) and provides methods for implementing custom popup behavior.

**Properties**
- `bool Borderless` = `true (overrides Window)`
- `bool MaximizeDisabled` = `true (overrides Window)`
- `bool MinimizeDisabled` = `true (overrides Window)`
- `bool PopupWindow` = `true (overrides Window)`
- `bool PopupWmHint` = `true (overrides Window)`
- `bool Transient` = `true (overrides Window)`
- `bool Unresizable` = `true (overrides Window)`
- `bool Visible` = `false (overrides Window)`
- `bool WrapControls` = `true (overrides Window)`

### PrismMesh
*Inherits: **PrimitiveMesh < Mesh < Resource < RefCounted < Object***

Class representing a prism-shaped PrimitiveMesh.

**Properties**
- `float LeftToRight` = `0.5`
- `Vector3 Size` = `Vector3(1, 1, 1)`
- `int SubdivideDepth` = `0`
- `int SubdivideHeight` = `0`
- `int SubdivideWidth` = `0`
