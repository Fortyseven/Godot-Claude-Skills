# Godot 4 C# API Reference — Resources

> C#-only reference. 85 classes.

### AnimatedTexture
*Inherits: **Texture2D < Texture < Resource < RefCounted < Object***

AnimatedTexture is a resource format for frame-based animations, where multiple textures can be chained automatically with a predefined delay for each frame. Unlike AnimationPlayer or AnimatedSprite2D, it isn't a Node, but has the advantage of being usable anywhere a Texture2D resource can be used, e.g. in a TileSet.

**Properties**
- `int CurrentFrame`
- `int Frames` = `1`
- `bool OneShot` = `false`
- `bool Pause` = `false`
- `bool ResourceLocalToScene` = `false (overrides Resource)`
- `float SpeedScale` = `1.0`

**Methods**
- `float GetFrameDuration(int frame)`
- `Texture2D GetFrameTexture(int frame)`
- `void SetFrameDuration(int frame, float duration)`
- `void SetFrameTexture(int frame, Texture2D texture)`

### AnimationLibrary
*Inherits: **Resource < RefCounted < Object***

An animation library stores a set of animations accessible through StringName keys, for use with AnimationPlayer nodes.

**Methods**
- `Error AddAnimation(StringName name, Animation animation)`
- `Animation GetAnimation(StringName name)`
- `Array[StringName] GetAnimationList()`
- `int GetAnimationListSize()`
- `bool HasAnimation(StringName name)`
- `void RemoveAnimation(StringName name)`
- `void RenameAnimation(StringName name, StringName newname)`

### AnimationMixer
*Inherits: **Node < Object** | Inherited by: AnimationPlayer, AnimationTree*

Base class for AnimationPlayer and AnimationTree to manage animation lists. It also has general properties and methods for playback and blending.

**Properties**
- `bool Active` = `true`
- `int AudioMaxPolyphony` = `32`
- `AnimationCallbackModeDiscrete CallbackModeDiscrete` = `1`
- `AnimationCallbackModeMethod CallbackModeMethod` = `0`
- `AnimationCallbackModeProcess CallbackModeProcess` = `1`
- `bool Deterministic` = `false`
- `bool ResetOnSave` = `true`
- `bool RootMotionLocal` = `false`
- `NodePath RootMotionTrack` = `NodePath("")`
- `NodePath RootNode` = `NodePath("..")`

**Methods**
- `Variant _PostProcessKeyValue(Animation animation, int track, Variant value, int objectId, int objectSubIdx) [virtual]`
- `Error AddAnimationLibrary(StringName name, AnimationLibrary library)`
- `void Advance(float delta)`
- `void Capture(StringName name, float duration, TransitionType transType = 0, EaseType easeType = 0)`
- `void ClearCaches()`
- `StringName FindAnimation(Animation animation)`
- `StringName FindAnimationLibrary(Animation animation)`
- `Animation GetAnimation(StringName name)`
- `AnimationLibrary GetAnimationLibrary(StringName name)`
- `Array[StringName] GetAnimationLibraryList()`
- `PackedStringArray GetAnimationList()`
- `Vector3 GetRootMotionPosition()`
- `Vector3 GetRootMotionPositionAccumulator()`
- `Quaternion GetRootMotionRotation()`
- `Quaternion GetRootMotionRotationAccumulator()`
- `Vector3 GetRootMotionScale()`
- `Vector3 GetRootMotionScaleAccumulator()`
- `bool HasAnimation(StringName name)`
- `bool HasAnimationLibrary(StringName name)`
- `void RemoveAnimationLibrary(StringName name)`
- `void RenameAnimationLibrary(StringName name, StringName newname)`

### AnimationNodeAdd2
*Inherits: **AnimationNodeSync < AnimationNode < Resource < RefCounted < Object***

A resource to add to an AnimationNodeBlendTree. Blends two animations additively based on the amount value.

### AnimationNodeAdd3
*Inherits: **AnimationNodeSync < AnimationNode < Resource < RefCounted < Object***

A resource to add to an AnimationNodeBlendTree. Blends two animations out of three additively out of three based on the amount value.

### AnimationNodeAnimation
*Inherits: **AnimationRootNode < AnimationNode < Resource < RefCounted < Object***

A resource to add to an AnimationNodeBlendTree. Only has one output port using the animation property. Used as an input for AnimationNodes that blend animations together.

**Properties**
- `bool AdvanceOnStart` = `false`
- `StringName Animation` = `&""`
- `LoopMode LoopMode`
- `PlayMode PlayMode` = `0`
- `float StartOffset`
- `bool StretchTimeScale`
- `float TimelineLength`
- `bool UseCustomTimeline` = `false`

### AnimationNodeBlend2
*Inherits: **AnimationNodeSync < AnimationNode < Resource < RefCounted < Object***

A resource to add to an AnimationNodeBlendTree. Blends two animations linearly based on the amount value.

### AnimationNodeBlend3
*Inherits: **AnimationNodeSync < AnimationNode < Resource < RefCounted < Object***

A resource to add to an AnimationNodeBlendTree. Blends two animations out of three linearly out of three based on the amount value.

### AnimationNodeBlendSpace1D
*Inherits: **AnimationRootNode < AnimationNode < Resource < RefCounted < Object***

A resource used by AnimationNodeBlendTree.

**Properties**
- `BlendMode BlendMode` = `0`
- `float MaxSpace` = `1.0`
- `float MinSpace` = `-1.0`
- `float Snap` = `0.1`
- `bool Sync` = `false`
- `string ValueLabel` = `"value"`

**Methods**
- `void AddBlendPoint(AnimationRootNode node, float pos, int atIndex = -1)`
- `int GetBlendPointCount()`
- `AnimationRootNode GetBlendPointNode(int point)`
- `float GetBlendPointPosition(int point)`
- `void RemoveBlendPoint(int point)`
- `void SetBlendPointNode(int point, AnimationRootNode node)`
- `void SetBlendPointPosition(int point, float pos)`

### AnimationNodeBlendSpace2D
*Inherits: **AnimationRootNode < AnimationNode < Resource < RefCounted < Object***

A resource used by AnimationNodeBlendTree.

**Properties**
- `bool AutoTriangles` = `true`
- `BlendMode BlendMode` = `0`
- `Vector2 MaxSpace` = `Vector2(1, 1)`
- `Vector2 MinSpace` = `Vector2(-1, -1)`
- `Vector2 Snap` = `Vector2(0.1, 0.1)`
- `bool Sync` = `false`
- `string XLabel` = `"x"`
- `string YLabel` = `"y"`

**Methods**
- `void AddBlendPoint(AnimationRootNode node, Vector2 pos, int atIndex = -1)`
- `void AddTriangle(int x, int y, int z, int atIndex = -1)`
- `int GetBlendPointCount()`
- `AnimationRootNode GetBlendPointNode(int point)`
- `Vector2 GetBlendPointPosition(int point)`
- `int GetTriangleCount()`
- `int GetTrianglePoint(int triangle, int point)`
- `void RemoveBlendPoint(int point)`
- `void RemoveTriangle(int triangle)`
- `void SetBlendPointNode(int point, AnimationRootNode node)`
- `void SetBlendPointPosition(int point, Vector2 pos)`

### AnimationNodeBlendTree
*Inherits: **AnimationRootNode < AnimationNode < Resource < RefCounted < Object***

This animation node may contain a sub-tree of any other type animation nodes, such as AnimationNodeTransition, AnimationNodeBlend2, AnimationNodeBlend3, AnimationNodeOneShot, etc. This is one of the most commonly used animation node roots.

**Properties**
- `Vector2 GraphOffset` = `Vector2(0, 0)`

**Methods**
- `void AddNode(StringName name, AnimationNode node, Vector2 position = Vector2(0, 0))`
- `void ConnectNode(StringName inputNode, int inputIndex, StringName outputNode)`
- `void DisconnectNode(StringName inputNode, int inputIndex)`
- `AnimationNode GetNode(StringName name)`
- `Array[StringName] GetNodeList()`
- `Vector2 GetNodePosition(StringName name)`
- `bool HasNode(StringName name)`
- `void RemoveNode(StringName name)`
- `void RenameNode(StringName name, StringName newName)`
- `void SetNodePosition(StringName name, Vector2 position)`

### AnimationNodeExtension
*Inherits: **AnimationNode < Resource < RefCounted < Object***

AnimationNodeExtension exposes the APIs of AnimationRootNode to allow users to extend it from GDScript, C#, or C++. This class is not meant to be used directly, but to be extended by other classes. It is used to create custom nodes for the AnimationTree system.

**Methods**
- `PackedFloat32Array _ProcessAnimationNode(PackedFloat64Array playbackInfo, bool testOnly) [virtual]`
- `float GetRemainingTime(PackedFloat32Array nodeInfo, bool breakLoop) [static]`
- `bool IsLooping(PackedFloat32Array nodeInfo) [static]`

### AnimationNodeOneShot
*Inherits: **AnimationNodeSync < AnimationNode < Resource < RefCounted < Object***

A resource to add to an AnimationNodeBlendTree. This animation node will execute a sub-animation and return once it finishes. Blend times for fading in and out can be customized, as well as filters.

**Properties**
- `bool AbortOnReset` = `false`
- `bool Autorestart` = `false`
- `float AutorestartDelay` = `1.0`
- `float AutorestartRandomDelay` = `0.0`
- `bool BreakLoopAtEnd` = `false`
- `Curve FadeinCurve`
- `float FadeinTime` = `0.0`
- `Curve FadeoutCurve`
- `float FadeoutTime` = `0.0`
- `MixMode MixMode` = `0`

**C# Examples**
```csharp
// Play child animation connected to "shot" port.
animationTree.Set("parameters/OneShot/request", (int)AnimationNodeOneShot.OneShotRequest.Fire);

// Abort child animation connected to "shot" port.
animationTree.Set("parameters/OneShot/request", (int)AnimationNodeOneShot.OneShotRequest.Abort);

// Abort child animation with fading out connected to "shot" port.
animationTree.Set("parameters/OneShot/request", (int)AnimationNodeOneShot.OneShotRequest.FadeOut);

// Get current state (read-only).
animationTree.Get("parameters/OneShot/active");

// Get current internal state (read-only).
animationTr
// ...
```

### AnimationNodeOutput
*Inherits: **AnimationNode < Resource < RefCounted < Object***

A node created automatically in an AnimationNodeBlendTree that outputs the final animation.

### AnimationNodeStateMachinePlayback
*Inherits: **Resource < RefCounted < Object***

Allows control of AnimationTree state machines created with AnimationNodeStateMachine. Retrieve with $AnimationTree.get("parameters/playback").

**Properties**
- `bool ResourceLocalToScene` = `true (overrides Resource)`

**Methods**
- `float GetCurrentLength()`
- `StringName GetCurrentNode()`
- `float GetCurrentPlayPosition()`
- `float GetFadingFromLength()`
- `StringName GetFadingFromNode()`
- `float GetFadingFromPlayPosition()`
- `float GetFadingLength()`
- `float GetFadingPosition()`
- `Array[StringName] GetTravelPath()`
- `bool IsPlaying()`
- `void Next()`
- `void Start(StringName node, bool reset = true)`
- `void Stop()`
- `void Travel(StringName toNode, bool resetOnTeleport = true)`

**C# Examples**
```csharp
var stateMachine = GetNode<AnimationTree>("AnimationTree").Get("parameters/playback").As<AnimationNodeStateMachinePlayback>();
stateMachine.Travel("some_state");
```

### AnimationNodeStateMachineTransition
*Inherits: **Resource < RefCounted < Object***

The path generated when using AnimationNodeStateMachinePlayback.travel() is limited to the nodes connected by AnimationNodeStateMachineTransition.

**Properties**
- `StringName AdvanceCondition` = `&""`
- `string AdvanceExpression` = `""`
- `AdvanceMode AdvanceMode` = `1`
- `bool BreakLoopAtEnd` = `false`
- `int Priority` = `1`
- `bool Reset` = `true`
- `SwitchMode SwitchMode` = `0`
- `Curve XfadeCurve`
- `float XfadeTime` = `0.0`

**C# Examples**
```csharp
GetNode<AnimationTree>("animation_tree").Set("parameters/conditions/idle", IsOnFloor && (LinearVelocity.X == 0));
```

### AnimationNodeStateMachine
*Inherits: **AnimationRootNode < AnimationNode < Resource < RefCounted < Object***

Contains multiple AnimationRootNodes representing animation states, connected in a graph. State transitions can be configured to happen automatically or via code, using a shortest-path algorithm. Retrieve the AnimationNodeStateMachinePlayback object from the AnimationTree node to control it programmatically.

**Properties**
- `bool AllowTransitionToSelf` = `false`
- `bool ResetEnds` = `false`
- `StateMachineType StateMachineType` = `0`

**Methods**
- `void AddNode(StringName name, AnimationNode node, Vector2 position = Vector2(0, 0))`
- `void AddTransition(StringName from, StringName to, AnimationNodeStateMachineTransition transition)`
- `Vector2 GetGraphOffset()`
- `AnimationNode GetNode(StringName name)`
- `Array[StringName] GetNodeList()`
- `StringName GetNodeName(AnimationNode node)`
- `Vector2 GetNodePosition(StringName name)`
- `AnimationNodeStateMachineTransition GetTransition(int idx)`
- `int GetTransitionCount()`
- `StringName GetTransitionFrom(int idx)`
- `StringName GetTransitionTo(int idx)`
- `bool HasNode(StringName name)`
- `bool HasTransition(StringName from, StringName to)`
- `void RemoveNode(StringName name)`
- `void RemoveTransition(StringName from, StringName to)`
- `void RemoveTransitionByIndex(int idx)`
- `void RenameNode(StringName name, StringName newName)`
- `void ReplaceNode(StringName name, AnimationNode node)`
- `void SetGraphOffset(Vector2 offset)`
- `void SetNodePosition(StringName name, Vector2 position)`

**C# Examples**
```csharp
var stateMachine = GetNode<AnimationTree>("AnimationTree").Get("parameters/playback") as AnimationNodeStateMachinePlayback;
stateMachine.Travel("some_state");
```

### AnimationNodeSub2
*Inherits: **AnimationNodeSync < AnimationNode < Resource < RefCounted < Object***

A resource to add to an AnimationNodeBlendTree. Blends two animations subtractively based on the amount value.

### AnimationNodeSync
*Inherits: **AnimationNode < Resource < RefCounted < Object** | Inherited by: AnimationNodeAdd2, AnimationNodeAdd3, AnimationNodeBlend2, AnimationNodeBlend3, AnimationNodeOneShot, AnimationNodeSub2, ...*

An animation node used to combine, mix, or blend two or more animations together while keeping them synchronized within an AnimationTree.

**Properties**
- `bool Sync` = `false`

### AnimationNodeTimeScale
*Inherits: **AnimationNode < Resource < RefCounted < Object***

Allows to scale the speed of the animation (or reverse it) in any child AnimationNodes. Setting it to 0.0 will pause the animation.

### AnimationNodeTimeSeek
*Inherits: **AnimationNode < Resource < RefCounted < Object***

This animation node can be used to cause a seek command to happen to any sub-children of the animation graph. Use to play an Animation from the start or a certain playback position inside the AnimationNodeBlendTree.

**Properties**
- `bool ExplicitElapse` = `true`

**C# Examples**
```csharp
// Play child animation from the start.
animationTree.Set("parameters/TimeSeek/seek_request", 0.0);

// Play child animation from 12 second timestamp.
animationTree.Set("parameters/TimeSeek/seek_request", 12.0);
```

### AnimationNodeTransition
*Inherits: **AnimationNodeSync < AnimationNode < Resource < RefCounted < Object***

Simple state machine for cases which don't require a more advanced AnimationNodeStateMachine. Animations can be connected to the inputs and transition times can be specified.

**Properties**
- `bool AllowTransitionToSelf` = `false`
- `int InputCount` = `0`
- `Curve XfadeCurve`
- `float XfadeTime` = `0.0`

**Methods**
- `bool IsInputLoopBrokenAtEnd(int input)`
- `bool IsInputReset(int input)`
- `bool IsInputSetAsAutoAdvance(int input)`
- `void SetInputAsAutoAdvance(int input, bool enable)`
- `void SetInputBreakLoopAtEnd(int input, bool enable)`
- `void SetInputReset(int input, bool enable)`

**C# Examples**
```csharp
// Play child animation connected to "state_2" port.
animationTree.Set("parameters/Transition/transition_request", "state_2");

// Get current state name (read-only).
animationTree.Get("parameters/Transition/current_state");

// Get current state index (read-only).
animationTree.Get("parameters/Transition/current_index");
```

### AnimationNode
*Inherits: **Resource < RefCounted < Object** | Inherited by: AnimationNodeExtension, AnimationNodeOutput, AnimationNodeSync, AnimationNodeTimeScale, AnimationNodeTimeSeek, AnimationRootNode*

Base resource for AnimationTree nodes. In general, it's not used directly, but you can create custom ones with custom blending formulas.

**Properties**
- `bool FilterEnabled`

**Methods**
- `string _GetCaption() [virtual]`
- `AnimationNode _GetChildByName(StringName name) [virtual]`
- `Godot.Collections.Dictionary _GetChildNodes() [virtual]`
- `Variant _GetParameterDefaultValue(StringName parameter) [virtual]`
- `Godot.Collections.Array _GetParameterList() [virtual]`
- `bool _HasFilter() [virtual]`
- `bool _IsParameterReadOnly(StringName parameter) [virtual]`
- `float _Process(float time, bool seek, bool isExternalSeeking, bool testOnly) [virtual]`
- `bool AddInput(string name)`
- `void BlendAnimation(StringName animation, float time, float delta, bool seeked, bool isExternalSeeking, float blend, LoopedFlag loopedFlag = 0)`
- `float BlendInput(int inputIndex, float time, bool seek, bool isExternalSeeking, float blend, FilterAction filter = 0, bool sync = true, bool testOnly = false)`
- `float BlendNode(StringName name, AnimationNode node, float time, bool seek, bool isExternalSeeking, float blend, FilterAction filter = 0, bool sync = true, bool testOnly = false)`
- `int FindInput(string name)`
- `int GetInputCount()`
- `string GetInputName(int input)`
- `Variant GetParameter(StringName name)`
- `int GetProcessingAnimationTreeInstanceId()`
- `bool IsPathFiltered(NodePath path)`
- `bool IsProcessTesting()`
- `void RemoveInput(int index)`
- `void SetFilterPath(NodePath path, bool enable)`
- `bool SetInputName(int input, string name)`
- `void SetParameter(StringName name, Variant value)`

### AnimationPlayer
*Inherits: **AnimationMixer < Node < Object***

An animation player is used for general-purpose playback of animations. It contains a dictionary of AnimationLibrary resources and custom blend times between animation transitions.

**Properties**
- `StringName AssignedAnimation`
- `StringName Autoplay` = `&""`
- `StringName CurrentAnimation` = `&""`
- `float CurrentAnimationLength`
- `float CurrentAnimationPosition`
- `bool MovieQuitOnFinish` = `false`
- `bool PlaybackAutoCapture` = `true`
- `float PlaybackAutoCaptureDuration` = `-1.0`
- `EaseType PlaybackAutoCaptureEaseType` = `0`
- `TransitionType PlaybackAutoCaptureTransitionType` = `0`
- `float PlaybackDefaultBlendTime` = `0.0`
- `float SpeedScale` = `1.0`

**Methods**
- `StringName AnimationGetNext(StringName animationFrom)`
- `void AnimationSetNext(StringName animationFrom, StringName animationTo)`
- `void ClearQueue()`
- `float GetBlendTime(StringName animationFrom, StringName animationTo)`
- `AnimationMethodCallMode GetMethodCallMode()`
- `float GetPlayingSpeed()`
- `AnimationProcessCallback GetProcessCallback()`
- `Array[StringName] GetQueue()`
- `NodePath GetRoot()`
- `float GetSectionEndTime()`
- `float GetSectionStartTime()`
- `bool HasSection()`
- `bool IsAnimationActive()`
- `bool IsPlaying()`
- `void Pause()`
- `void Play(StringName name = &"", float customBlend = -1, float customSpeed = 1.0, bool fromEnd = false)`
- `void PlayBackwards(StringName name = &"", float customBlend = -1)`
- `void PlaySection(StringName name = &"", float startTime = -1, float endTime = -1, float customBlend = -1, float customSpeed = 1.0, bool fromEnd = false)`
- `void PlaySectionBackwards(StringName name = &"", float startTime = -1, float endTime = -1, float customBlend = -1)`
- `void PlaySectionWithMarkers(StringName name = &"", StringName startMarker = &"", StringName endMarker = &"", float customBlend = -1, float customSpeed = 1.0, bool fromEnd = false)`
- `void PlaySectionWithMarkersBackwards(StringName name = &"", StringName startMarker = &"", StringName endMarker = &"", float customBlend = -1)`
- `void PlayWithCapture(StringName name = &"", float duration = -1.0, float customBlend = -1, float customSpeed = 1.0, bool fromEnd = false, TransitionType transType = 0, EaseType easeType = 0)`
- `void Queue(StringName name)`
- `void ResetSection()`
- `void Seek(float seconds, bool update = false, bool updateOnly = false)`
- `void SetBlendTime(StringName animationFrom, StringName animationTo, float sec)`
- `void SetMethodCallMode(AnimationMethodCallMode mode)`
- `void SetProcessCallback(AnimationProcessCallback mode)`
- `void SetRoot(NodePath path)`
- `void SetSection(float startTime = -1, float endTime = -1)`
- `void SetSectionWithMarkers(StringName startMarker = &"", StringName endMarker = &"")`
- `void Stop(bool keepState = false)`

### AnimationRootNode
*Inherits: **AnimationNode < Resource < RefCounted < Object** | Inherited by: AnimationNodeAnimation, AnimationNodeBlendSpace1D, AnimationNodeBlendSpace2D, AnimationNodeBlendTree, AnimationNodeStateMachine*

AnimationRootNode is a base class for AnimationNodes that hold a complete animation. A complete animation refers to the output of an AnimationNodeOutput in an AnimationNodeBlendTree or the output of another AnimationRootNode. Used for AnimationTree.tree_root or in other AnimationRootNodes.

### AnimationTree
*Inherits: **AnimationMixer < Node < Object***

A node used for advanced animation transitions in an AnimationPlayer.

**Properties**
- `NodePath AdvanceExpressionBaseNode` = `NodePath(".")`
- `NodePath AnimPlayer` = `NodePath("")`
- `AnimationCallbackModeDiscrete CallbackModeDiscrete` = `2 (overrides AnimationMixer)`
- `bool Deterministic` = `true (overrides AnimationMixer)`
- `AnimationRootNode TreeRoot`

**Methods**
- `AnimationProcessCallback GetProcessCallback()`
- `void SetProcessCallback(AnimationProcessCallback mode)`

### Animation
*Inherits: **Resource < RefCounted < Object***

This resource holds data that can be used to animate anything in the engine. Animations are divided into tracks and each track must be linked to a node. The state of that node can be changed through time, by adding timed keys (events) to the track.

**Properties**
- `bool CaptureIncluded` = `false`
- `float Length` = `1.0`
- `LoopMode LoopMode` = `0`
- `float Step` = `0.033333335`

**Methods**
- `void AddMarker(StringName name, float time)`
- `int AddTrack(TrackType type, int atPosition = -1)`
- `StringName AnimationTrackGetKeyAnimation(int trackIdx, int keyIdx)`
- `int AnimationTrackInsertKey(int trackIdx, float time, StringName animation)`
- `void AnimationTrackSetKeyAnimation(int trackIdx, int keyIdx, StringName animation)`
- `float AudioTrackGetKeyEndOffset(int trackIdx, int keyIdx)`
- `float AudioTrackGetKeyStartOffset(int trackIdx, int keyIdx)`
- `Resource AudioTrackGetKeyStream(int trackIdx, int keyIdx)`
- `int AudioTrackInsertKey(int trackIdx, float time, Resource stream, float startOffset = 0, float endOffset = 0)`
- `bool AudioTrackIsUseBlend(int trackIdx)`
- `void AudioTrackSetKeyEndOffset(int trackIdx, int keyIdx, float offset)`
- `void AudioTrackSetKeyStartOffset(int trackIdx, int keyIdx, float offset)`
- `void AudioTrackSetKeyStream(int trackIdx, int keyIdx, Resource stream)`
- `void AudioTrackSetUseBlend(int trackIdx, bool enable)`
- `Vector2 BezierTrackGetKeyInHandle(int trackIdx, int keyIdx)`
- `Vector2 BezierTrackGetKeyOutHandle(int trackIdx, int keyIdx)`
- `float BezierTrackGetKeyValue(int trackIdx, int keyIdx)`
- `int BezierTrackInsertKey(int trackIdx, float time, float value, Vector2 inHandle = Vector2(0, 0), Vector2 outHandle = Vector2(0, 0))`
- `float BezierTrackInterpolate(int trackIdx, float time)`
- `void BezierTrackSetKeyInHandle(int trackIdx, int keyIdx, Vector2 inHandle, float balancedValueTimeRatio = 1.0)`
- `void BezierTrackSetKeyOutHandle(int trackIdx, int keyIdx, Vector2 outHandle, float balancedValueTimeRatio = 1.0)`
- `void BezierTrackSetKeyValue(int trackIdx, int keyIdx, float value)`
- `int BlendShapeTrackInsertKey(int trackIdx, float time, float amount)`
- `float BlendShapeTrackInterpolate(int trackIdx, float timeSec, bool backward = false)`
- `void Clear()`
- `void Compress(int pageSize = 8192, int fps = 120, float splitTolerance = 4.0)`
- `void CopyTrack(int trackIdx, Animation toAnimation)`
- `int FindTrack(NodePath path, TrackType type)`
- `StringName GetMarkerAtTime(float time)`
- `Color GetMarkerColor(StringName name)`
- `PackedStringArray GetMarkerNames()`
- `float GetMarkerTime(StringName name)`
- `StringName GetNextMarker(float time)`
- `StringName GetPrevMarker(float time)`
- `int GetTrackCount()`
- `bool HasMarker(StringName name)`
- `StringName MethodTrackGetName(int trackIdx, int keyIdx)`
- `Godot.Collections.Array MethodTrackGetParams(int trackIdx, int keyIdx)`
- `void Optimize(float allowedVelocityErr = 0.01, float allowedAngularErr = 0.01, int precision = 3)`
- `int PositionTrackInsertKey(int trackIdx, float time, Vector3 position)`

**C# Examples**
```csharp
// This creates an animation that makes the node "Enemy" move to the right by
// 100 pixels in 2.0 seconds.
var animation = new Animation();
int trackIndex = animation.AddTrack(Animation.TrackType.Value);
animation.TrackSetPath(trackIndex, "Enemy:position:x");
animation.TrackInsertKey(trackIndex, 0.0f, 0);
animation.TrackInsertKey(trackIndex, 2.0f, 100);
animation.Length = 2.0f;
```

### AtlasTexture
*Inherits: **Texture2D < Texture < Resource < RefCounted < Object***

Texture2D resource that draws only part of its atlas texture, as defined by the region. An additional margin can also be set, which is useful for small adjustments.

**Properties**
- `Texture2D Atlas`
- `bool FilterClip` = `false`
- `Rect2 Margin` = `Rect2(0, 0, 0, 0)`
- `Rect2 Region` = `Rect2(0, 0, 0, 0)`
- `bool ResourceLocalToScene` = `false (overrides Resource)`

### BitMap
*Inherits: **Resource < RefCounted < Object***

A two-dimensional array of boolean values, can be used to efficiently store a binary matrix (every matrix element takes only one bit) and query the values using natural cartesian coordinates.

**Methods**
- `Image ConvertToImage()`
- `void Create(Vector2i size)`
- `void CreateFromImageAlpha(Image image, float threshold = 0.1)`
- `bool GetBit(int x, int y)`
- `bool GetBitv(Vector2i position)`
- `Vector2i GetSize()`
- `int GetTrueBitCount()`
- `void GrowMask(int pixels, Rect2i rect)`
- `Array[PackedVector2Array] OpaqueToPolygons(Rect2i rect, float epsilon = 2.0)`
- `void Resize(Vector2i newSize)`
- `void SetBit(int x, int y, bool bit)`
- `void SetBitRect(Rect2i rect, bool bit)`
- `void SetBitv(Vector2i position, bool bit)`

### CSharpScript
*Inherits: **Script < Resource < RefCounted < Object***

This class represents a C# script. It is the C# equivalent of the GDScript class and is only available in Mono-enabled Godot builds.

**Methods**
- `Variant New()`

### CameraTexture
*Inherits: **Texture2D < Texture < Resource < RefCounted < Object***

This texture gives access to the camera texture provided by a CameraFeed.

**Properties**
- `int CameraFeedId` = `0`
- `bool CameraIsActive` = `false`
- `bool ResourceLocalToScene` = `false (overrides Resource)`
- `FeedImage WhichFeed` = `0`

### CompressedTexture2DArray
*Inherits: **CompressedTextureLayered < TextureLayered < Texture < Resource < RefCounted < Object***

A texture array that is loaded from a .ctexarray file. This file format is internal to Godot; it is created by importing other image formats with the import system. CompressedTexture2DArray can use one of 4 compression methods:

### CompressedTexture2D
*Inherits: **Texture2D < Texture < Resource < RefCounted < Object***

A texture that is loaded from a .ctex file. This file format is internal to Godot; it is created by importing other image formats with the import system. CompressedTexture2D can use one of 4 compression methods (including a lack of any compression):

**Properties**
- `string LoadPath` = `""`
- `bool ResourceLocalToScene` = `false (overrides Resource)`

**Methods**
- `Error Load(string path)`

### Curve2D
*Inherits: **Resource < RefCounted < Object***

This class describes a Bézier curve in 2D space. It is mainly used to give a shape to a Path2D, but can be manually sampled for other purposes.

**Properties**
- `float BakeInterval` = `5.0`
- `int PointCount` = `0`

**Methods**
- `void AddPoint(Vector2 position, Vector2 in = Vector2(0, 0), Vector2 out = Vector2(0, 0), int index = -1)`
- `void ClearPoints()`
- `float GetBakedLength()`
- `PackedVector2Array GetBakedPoints()`
- `float GetClosestOffset(Vector2 toPoint)`
- `Vector2 GetClosestPoint(Vector2 toPoint)`
- `Vector2 GetPointIn(int idx)`
- `Vector2 GetPointOut(int idx)`
- `Vector2 GetPointPosition(int idx)`
- `void RemovePoint(int idx)`
- `Vector2 Sample(int idx, float t)`
- `Vector2 SampleBaked(float offset = 0.0, bool cubic = false)`
- `Transform2D SampleBakedWithRotation(float offset = 0.0, bool cubic = false)`
- `Vector2 Samplef(float fofs)`
- `void SetPointIn(int idx, Vector2 position)`
- `void SetPointOut(int idx, Vector2 position)`
- `void SetPointPosition(int idx, Vector2 position)`
- `PackedVector2Array Tessellate(int maxStages = 5, float toleranceDegrees = 4)`
- `PackedVector2Array TessellateEvenLength(int maxStages = 5, float toleranceLength = 20.0)`

### Curve3D
*Inherits: **Resource < RefCounted < Object***

This class describes a Bézier curve in 3D space. It is mainly used to give a shape to a Path3D, but can be manually sampled for other purposes.

**Properties**
- `float BakeInterval` = `0.2`
- `bool Closed` = `false`
- `int PointCount` = `0`
- `bool UpVectorEnabled` = `true`

**Methods**
- `void AddPoint(Vector3 position, Vector3 in = Vector3(0, 0, 0), Vector3 out = Vector3(0, 0, 0), int index = -1)`
- `void ClearPoints()`
- `float GetBakedLength()`
- `PackedVector3Array GetBakedPoints()`
- `PackedFloat32Array GetBakedTilts()`
- `PackedVector3Array GetBakedUpVectors()`
- `float GetClosestOffset(Vector3 toPoint)`
- `Vector3 GetClosestPoint(Vector3 toPoint)`
- `Vector3 GetPointIn(int idx)`
- `Vector3 GetPointOut(int idx)`
- `Vector3 GetPointPosition(int idx)`
- `float GetPointTilt(int idx)`
- `void RemovePoint(int idx)`
- `Vector3 Sample(int idx, float t)`
- `Vector3 SampleBaked(float offset = 0.0, bool cubic = false)`
- `Vector3 SampleBakedUpVector(float offset, bool applyTilt = false)`
- `Transform3D SampleBakedWithRotation(float offset = 0.0, bool cubic = false, bool applyTilt = false)`
- `Vector3 Samplef(float fofs)`
- `void SetPointIn(int idx, Vector3 position)`
- `void SetPointOut(int idx, Vector3 position)`
- `void SetPointPosition(int idx, Vector3 position)`
- `void SetPointTilt(int idx, float tilt)`
- `PackedVector3Array Tessellate(int maxStages = 5, float toleranceDegrees = 4)`
- `PackedVector3Array TessellateEvenLength(int maxStages = 5, float toleranceLength = 0.2)`

### FastNoiseLite
*Inherits: **Noise < Resource < RefCounted < Object***

This class generates noise using the FastNoiseLite library, which is a collection of several noise algorithms including Cellular, Perlin, Value, and more.

**Properties**
- `CellularDistanceFunction CellularDistanceFunction` = `0`
- `float CellularJitter` = `1.0`
- `CellularReturnType CellularReturnType` = `1`
- `float DomainWarpAmplitude` = `30.0`
- `bool DomainWarpEnabled` = `false`
- `float DomainWarpFractalGain` = `0.5`
- `float DomainWarpFractalLacunarity` = `6.0`
- `int DomainWarpFractalOctaves` = `5`
- `DomainWarpFractalType DomainWarpFractalType` = `1`
- `float DomainWarpFrequency` = `0.05`
- `DomainWarpType DomainWarpType` = `0`
- `float FractalGain` = `0.5`
- `float FractalLacunarity` = `2.0`
- `int FractalOctaves` = `5`
- `float FractalPingPongStrength` = `2.0`
- `FractalType FractalType` = `1`
- `float FractalWeightedStrength` = `0.0`
- `float Frequency` = `0.01`
- `NoiseType NoiseType` = `1`
- `Vector3 Offset` = `Vector3(0, 0, 0)`
- `int Seed` = `0`

### FontFile
*Inherits: **Font < Resource < RefCounted < Object***

FontFile contains a set of glyphs to represent Unicode characters imported from a font file, as well as a cache of rasterized glyphs, and a set of fallback Fonts to use.

**Properties**
- `bool AllowSystemFallback` = `true`
- `FontAntialiasing Antialiasing` = `1`
- `PackedByteArray Data` = `PackedByteArray()`
- `bool DisableEmbeddedBitmaps` = `true`
- `int FixedSize` = `0`
- `FixedSizeScaleMode FixedSizeScaleMode` = `0`
- `string FontName` = `""`
- `int FontStretch` = `100`
- `BitField[FontStyle] FontStyle` = `0`
- `int FontWeight` = `400`
- `bool ForceAutohinter` = `false`
- `bool GenerateMipmaps` = `false`
- `Hinting Hinting` = `1`
- `bool KeepRoundingRemainders` = `true`
- `bool ModulateColorGlyphs` = `false`
- `int MsdfPixelRange` = `16`
- `int MsdfSize` = `48`
- `bool MultichannelSignedDistanceField` = `false`
- `Godot.Collections.Dictionary OpentypeFeatureOverrides` = `{}`
- `float Oversampling` = `0.0`
- `string StyleName` = `""`
- `SubpixelPositioning SubpixelPositioning` = `1`

**Methods**
- `void ClearCache()`
- `void ClearGlyphs(int cacheIndex, Vector2i size)`
- `void ClearKerningMap(int cacheIndex, int size)`
- `void ClearSizeCache(int cacheIndex)`
- `void ClearTextures(int cacheIndex, Vector2i size)`
- `float GetCacheAscent(int cacheIndex, int size)`
- `int GetCacheCount()`
- `float GetCacheDescent(int cacheIndex, int size)`
- `float GetCacheScale(int cacheIndex, int size)`
- `float GetCacheUnderlinePosition(int cacheIndex, int size)`
- `float GetCacheUnderlineThickness(int cacheIndex, int size)`
- `int GetCharFromGlyphIndex(int size, int glyphIndex)`
- `float GetEmbolden(int cacheIndex)`
- `float GetExtraBaselineOffset(int cacheIndex)`
- `int GetExtraSpacing(int cacheIndex, SpacingType spacing)`
- `int GetFaceIndex(int cacheIndex)`
- `Vector2 GetGlyphAdvance(int cacheIndex, int size, int glyph)`
- `int GetGlyphIndex(int size, int char, int variationSelector)`
- `PackedInt32Array GetGlyphList(int cacheIndex, Vector2i size)`
- `Vector2 GetGlyphOffset(int cacheIndex, Vector2i size, int glyph)`
- `Vector2 GetGlyphSize(int cacheIndex, Vector2i size, int glyph)`
- `int GetGlyphTextureIdx(int cacheIndex, Vector2i size, int glyph)`
- `Rect2 GetGlyphUvRect(int cacheIndex, Vector2i size, int glyph)`
- `Vector2 GetKerning(int cacheIndex, int size, Vector2i glyphPair)`
- `Array[Vector2i] GetKerningList(int cacheIndex, int size)`
- `bool GetLanguageSupportOverride(string language)`
- `PackedStringArray GetLanguageSupportOverrides()`
- `bool GetScriptSupportOverride(string script)`
- `PackedStringArray GetScriptSupportOverrides()`
- `Array[Vector2i] GetSizeCacheList(int cacheIndex)`
- `int GetTextureCount(int cacheIndex, Vector2i size)`
- `Image GetTextureImage(int cacheIndex, Vector2i size, int textureIndex)`
- `PackedInt32Array GetTextureOffsets(int cacheIndex, Vector2i size, int textureIndex)`
- `Transform2D GetTransform(int cacheIndex)`
- `Godot.Collections.Dictionary GetVariationCoordinates(int cacheIndex)`
- `Error LoadBitmapFont(string path)`
- `Error LoadDynamicFont(string path)`
- `void RemoveCache(int cacheIndex)`
- `void RemoveGlyph(int cacheIndex, Vector2i size, int glyph)`
- `void RemoveKerning(int cacheIndex, int size, Vector2i glyphPair)`

**C# Examples**
```csharp
var f = ResourceLoader.Load<FontFile>("res://BarlowCondensed-Bold.ttf");
GetNode("Label").AddThemeFontOverride("font", f);
GetNode("Label").AddThemeFontSizeOverride("font_size", 64);
```

### FontVariation
*Inherits: **Font < Resource < RefCounted < Object***

Provides OpenType variations, simulated bold / slant, and additional font settings like OpenType features and extra spacing.

**Properties**
- `Font BaseFont`
- `float BaselineOffset` = `0.0`
- `Godot.Collections.Dictionary OpentypeFeatures` = `{}`
- `int SpacingBottom` = `0`
- `int SpacingGlyph` = `0`
- `int SpacingSpace` = `0`
- `int SpacingTop` = `0`
- `float VariationEmbolden` = `0.0`
- `int VariationFaceIndex` = `0`
- `Godot.Collections.Dictionary VariationOpentype` = `{}`
- `Transform2D VariationTransform` = `Transform2D(1, 0, 0, 1, 0, 0)`

**Methods**
- `void SetSpacing(SpacingType spacing, int value)`

**C# Examples**
```csharp
var fv = new FontVariation();
fv.SetBaseFont(ResourceLoader.Load<FontFile>("res://BarlowCondensed-Regular.ttf"));
fv.SetVariationEmbolden(1.2);
GetNode("Label").AddThemeFontOverride("font", fv);
GetNode("Label").AddThemeFontSizeOverride("font_size", 64);
```

### GDScriptSyntaxHighlighter
*Inherits: **EditorSyntaxHighlighter < SyntaxHighlighter < Resource < RefCounted < Object***

Note: This class can only be used for editor plugins because it relies on editor settings.

**C# Examples**
```csharp
var codePreview = new TextEdit();
var highlighter = new GDScriptSyntaxHighlighter();
codePreview.SyntaxHighlighter = highlighter;
```

### GDScript
*Inherits: **Script < Resource < RefCounted < Object***

A script implemented in the GDScript programming language, saved with the .gd extension. The script extends the functionality of all objects that instantiate it.

**Methods**
- `Variant New()`

### GradientTexture1D
*Inherits: **Texture2D < Texture < Resource < RefCounted < Object***

A 1D texture that obtains colors from a Gradient to fill the texture data. The texture is filled by sampling the gradient for each pixel. Therefore, the texture does not necessarily represent an exact copy of the gradient, as it may miss some colors if there are not enough pixels. See also GradientTexture2D, CurveTexture and CurveXYZTexture.

**Properties**
- `Gradient Gradient`
- `bool ResourceLocalToScene` = `false (overrides Resource)`
- `bool UseHdr` = `false`
- `int Width` = `256`

### GradientTexture2D
*Inherits: **Texture2D < Texture < Resource < RefCounted < Object***

A 2D texture that obtains colors from a Gradient to fill the texture data. This texture is able to transform a color transition into different patterns such as a linear or a radial gradient. The texture is filled by interpolating colors starting from fill_from to fill_to offsets by default, but the gradient fill can be repeated to cover the entire texture.

**Properties**
- `Fill Fill` = `0`
- `Vector2 FillFrom` = `Vector2(0, 0)`
- `Vector2 FillTo` = `Vector2(1, 0)`
- `Gradient Gradient`
- `int Height` = `64`
- `Repeat Repeat` = `0`
- `bool ResourceLocalToScene` = `false (overrides Resource)`
- `bool UseHdr` = `false`
- `int Width` = `64`

### Gradient
*Inherits: **Resource < RefCounted < Object***

This resource describes a color transition by defining a set of colored points and how to interpolate between them.

**Properties**
- `PackedColorArray Colors` = `PackedColorArray(0, 0, 0, 1, 1, 1, 1, 1)`
- `ColorSpace InterpolationColorSpace` = `0`
- `InterpolationMode InterpolationMode` = `0`
- `PackedFloat32Array Offsets` = `PackedFloat32Array(0, 1)`

**Methods**
- `void AddPoint(float offset, Color color)`
- `Color GetColor(int point)`
- `float GetOffset(int point)`
- `int GetPointCount()`
- `void RemovePoint(int point)`
- `void Reverse()`
- `Color Sample(float offset)`
- `void SetColor(int point, Color color)`
- `void SetOffset(int point, float offset)`

### ImageTexture3D
*Inherits: **Texture3D < Texture < Resource < RefCounted < Object***

ImageTexture3D is a 3-dimensional ImageTexture that has a width, height, and depth. See also ImageTextureLayered.

**Methods**
- `Error Create(Format format, int width, int height, int depth, bool useMipmaps, Array[Image] data)`
- `void Update(Array[Image] data)`

### ImageTextureLayered
*Inherits: **TextureLayered < Texture < Resource < RefCounted < Object** | Inherited by: Cubemap, CubemapArray, Texture2DArray*

Base class for Texture2DArray, Cubemap and CubemapArray. Cannot be used directly, but contains all the functions necessary for accessing the derived resource types. See also Texture3D.

**Methods**
- `Error CreateFromImages(Array[Image] images)`
- `void UpdateLayer(Image image, int layer)`

### ImageTexture
*Inherits: **Texture2D < Texture < Resource < RefCounted < Object***

A Texture2D based on an Image. For an image to be displayed, an ImageTexture has to be created from it using the create_from_image() method:

**Properties**
- `bool ResourceLocalToScene` = `false (overrides Resource)`

**Methods**
- `ImageTexture CreateFromImage(Image image) [static]`
- `Format GetFormat()`
- `void SetImage(Image image)`
- `void SetSizeOverride(Vector2i size)`
- `void Update(Image image)`

### NoiseTexture2D
*Inherits: **Texture2D < Texture < Resource < RefCounted < Object***

Uses the FastNoiseLite library or other noise generators to fill the texture data of your desired size. NoiseTexture2D can also generate normal map textures.

**Properties**
- `bool AsNormalMap` = `false`
- `float BumpStrength` = `8.0`
- `Gradient ColorRamp`
- `bool GenerateMipmaps` = `true`
- `int Height` = `512`
- `bool In3dSpace` = `false`
- `bool Invert` = `false`
- `Noise Noise`
- `bool Normalize` = `true`
- `bool ResourceLocalToScene` = `false (overrides Resource)`
- `bool Seamless` = `false`
- `float SeamlessBlendSkirt` = `0.1`
- `int Width` = `512`

### Occluder3D
*Inherits: **Resource < RefCounted < Object** | Inherited by: ArrayOccluder3D, BoxOccluder3D, PolygonOccluder3D, QuadOccluder3D, SphereOccluder3D*

Occluder3D stores an occluder shape that can be used by the engine's occlusion culling system.

**Methods**
- `PackedInt32Array GetIndices()`
- `PackedVector3Array GetVertices()`

### OccluderInstance3D
*Inherits: **VisualInstance3D < Node3D < Node < Object***

Occlusion culling can improve rendering performance in closed/semi-open areas by hiding geometry that is occluded by other objects.

**Properties**
- `int BakeMask` = `4294967295`
- `float BakeSimplificationDistance` = `0.1`
- `Occluder3D Occluder`

**Methods**
- `bool GetBakeMaskValue(int layerNumber)`
- `void SetBakeMaskValue(int layerNumber, bool value)`

### PackedScene
*Inherits: **Resource < RefCounted < Object***

A simplified interface to a scene file. Provides access to operations and checks that can be performed on the scene resource itself.

**Methods**
- `bool CanInstantiate()`
- `SceneState GetState()`
- `Node Instantiate(GenEditState editState = 0)`
- `Error Pack(Node path)`

**C# Examples**
```csharp
// C# has no preload, so you have to always use ResourceLoader.Load<PackedScene>().
var scene = ResourceLoader.Load<PackedScene>("res://scene.tscn").Instantiate();
// Add the node as a child of the node the script is attached to.
AddChild(scene);
```
```csharp
// Create the objects.
var node = new Node2D();
var body = new RigidBody2D();
var collision = new CollisionShape2D();

// Create the object hierarchy.
body.AddChild(collision);
node.AddChild(body);

// Change owner of `body`, but not of `collision`.
body.Owner = node;
var scene = new PackedScene();

// Only `node` and `body` are now packed.
Error result = scene.Pack(node);
if (result == Error.Ok)
{
    Error error = ResourceSaver.Save(scene, "res://path/name.tscn"); // Or "user://..."
    if (error != Error.Ok)
    {
        GD.PushError("An error occurred while saving the scene to disk.");

// ...
```

### PlaceholderTexture2DArray
*Inherits: **PlaceholderTextureLayered < TextureLayered < Texture < Resource < RefCounted < Object***

This class is used when loading a project that uses a Texture2D subclass in 2 conditions:

### PlaceholderTexture2D
*Inherits: **Texture2D < Texture < Resource < RefCounted < Object***

This class is used when loading a project that uses a Texture2D subclass in 2 conditions:

**Properties**
- `bool ResourceLocalToScene` = `false (overrides Resource)`
- `Vector2 Size` = `Vector2(1, 1)`

### PortableCompressedTexture2D
*Inherits: **Texture2D < Texture < Resource < RefCounted < Object***

This class allows storing compressed textures as self contained (not imported) resources.

**Properties**
- `bool KeepCompressedBuffer` = `false`
- `bool ResourceLocalToScene` = `false (overrides Resource)`
- `Vector2 SizeOverride` = `Vector2(0, 0)`

**Methods**
- `void CreateFromImage(Image image, CompressionMode compressionMode, bool normalMap = false, float lossyQuality = 0.8)`
- `CompressionMode GetCompressionMode()`
- `Format GetFormat()`
- `bool IsKeepingAllCompressedBuffers() [static]`
- `void SetBasisuCompressorParams(int uastcLevel, float rdoQualityLoss)`
- `void SetKeepAllCompressedBuffers(bool keep) [static]`

### SceneState
*Inherits: **RefCounted < Object***

Maintains a list of resources, nodes, exported and overridden properties, and built-in scripts associated with a scene. They cannot be modified from a SceneState, only accessed. Useful for peeking into what a PackedScene contains without instantiating it.

**Methods**
- `SceneState GetBaseSceneState()`
- `Godot.Collections.Array GetConnectionBinds(int idx)`
- `int GetConnectionCount()`
- `int GetConnectionFlags(int idx)`
- `StringName GetConnectionMethod(int idx)`
- `StringName GetConnectionSignal(int idx)`
- `NodePath GetConnectionSource(int idx)`
- `NodePath GetConnectionTarget(int idx)`
- `int GetConnectionUnbinds(int idx)`
- `int GetNodeCount()`
- `PackedStringArray GetNodeGroups(int idx)`
- `int GetNodeIndex(int idx)`
- `PackedScene GetNodeInstance(int idx)`
- `string GetNodeInstancePlaceholder(int idx)`
- `StringName GetNodeName(int idx)`
- `NodePath GetNodeOwnerPath(int idx)`
- `NodePath GetNodePath(int idx, bool forParent = false)`
- `int GetNodePropertyCount(int idx)`
- `StringName GetNodePropertyName(int idx, int propIdx)`
- `Variant GetNodePropertyValue(int idx, int propIdx)`
- `StringName GetNodeType(int idx)`
- `string GetPath()`
- `bool IsNodeInstancePlaceholder(int idx)`

### ScriptBacktrace
*Inherits: **RefCounted < Object***

ScriptBacktrace holds an already captured backtrace of a specific script language, such as GDScript or C#, which are captured using Engine.capture_script_backtraces().

**Methods**
- `string Format(int indentAll = 0, int indentFrames = 4)`
- `int GetFrameCount()`
- `string GetFrameFile(int index)`
- `string GetFrameFunction(int index)`
- `int GetFrameLine(int index)`
- `int GetGlobalVariableCount()`
- `string GetGlobalVariableName(int variableIndex)`
- `Variant GetGlobalVariableValue(int variableIndex)`
- `string GetLanguageName()`
- `int GetLocalVariableCount(int frameIndex)`
- `string GetLocalVariableName(int frameIndex, int variableIndex)`
- `Variant GetLocalVariableValue(int frameIndex, int variableIndex)`
- `int GetMemberVariableCount(int frameIndex)`
- `string GetMemberVariableName(int frameIndex, int variableIndex)`
- `Variant GetMemberVariableValue(int frameIndex, int variableIndex)`
- `bool IsEmpty()`

### ScriptCreateDialog
*Inherits: **ConfirmationDialog < AcceptDialog < Window < Viewport < Node < Object***

The ScriptCreateDialog creates script files according to a given template for a given scripting language. The standard use is to configure its fields prior to calling one of the Window.popup() methods.

**Properties**
- `bool DialogHideOnOk` = `false (overrides AcceptDialog)`
- `string OkButtonText` = `"Create" (overrides AcceptDialog)`
- `string Title` = `"Attach Node Script" (overrides Window)`

**Methods**
- `void Config(string inherits, string path, bool builtInEnabled = true, bool loadEnabled = true)`

**C# Examples**
```csharp
public override void _Ready()
{
    var dialog = new ScriptCreateDialog();
    dialog.Config("Node", "res://NewNode.cs"); // For in-engine types.
    dialog.Config("\"res://BaseNode.cs\"", "res://DerivedNode.cs"); // For script types.
    dialog.PopupCentered();
}
```

### ScriptEditorBase
*Inherits: **VBoxContainer < BoxContainer < Container < Control < CanvasItem < Node < Object***

Base editor for editing scripts in the ScriptEditor. This does not include documentation items.

**Methods**
- `void AddSyntaxHighlighter(EditorSyntaxHighlighter highlighter)`
- `Control GetBaseEditor()`

### ScriptEditor
*Inherits: **PanelContainer < Container < Control < CanvasItem < Node < Object***

Godot editor's script editor.

**Methods**
- `void ClearDocsFromScript(Script script)`
- `PackedStringArray GetBreakpoints()`
- `ScriptEditorBase GetCurrentEditor()`
- `Script GetCurrentScript()`
- `Array[ScriptEditorBase] GetOpenScriptEditors()`
- `Array[Script] GetOpenScripts()`
- `void GotoHelp(string topic)`
- `void GotoLine(int lineNumber)`
- `void OpenScriptCreateDialog(string baseName, string basePath)`
- `void RegisterSyntaxHighlighter(EditorSyntaxHighlighter syntaxHighlighter)`
- `void UnregisterSyntaxHighlighter(EditorSyntaxHighlighter syntaxHighlighter)`
- `void UpdateDocsFromScript(Script script)`

### ScriptExtension
*Inherits: **Script < Resource < RefCounted < Object***

There is currently no description for this class. Please help us by contributing one!

**Methods**
- `bool _CanInstantiate() [virtual]`
- `bool _EditorCanReloadFromFile() [virtual]`
- `Script _GetBaseScript() [virtual]`
- `string _GetClassIconPath() [virtual]`
- `Godot.Collections.Dictionary _GetConstants() [virtual]`
- `StringName _GetDocClassName() [virtual]`
- `Array[Dictionary] _GetDocumentation() [virtual]`
- `StringName _GetGlobalName() [virtual]`
- `StringName _GetInstanceBaseType() [virtual]`
- `ScriptLanguage _GetLanguage() [virtual]`
- `int _GetMemberLine(StringName member) [virtual]`
- `Array[StringName] _GetMembers() [virtual]`
- `Godot.Collections.Dictionary _GetMethodInfo(StringName method) [virtual]`
- `Variant _GetPropertyDefaultValue(StringName property) [virtual]`
- `Variant _GetRpcConfig() [virtual]`
- `Variant _GetScriptMethodArgumentCount(StringName method) [virtual]`
- `Array[Dictionary] _GetScriptMethodList() [virtual]`
- `Array[Dictionary] _GetScriptPropertyList() [virtual]`
- `Array[Dictionary] _GetScriptSignalList() [virtual]`
- `string _GetSourceCode() [virtual]`
- `bool _HasMethod(StringName method) [virtual]`
- `bool _HasPropertyDefaultValue(StringName property) [virtual]`
- `bool _HasScriptSignal(StringName signal) [virtual]`
- `bool _HasSourceCode() [virtual]`
- `bool _HasStaticMethod(StringName method) [virtual]`
- `bool _InheritsScript(Script script) [virtual]`
- `void* _InstanceCreate(Object forObject) [virtual]`
- `bool _InstanceHas(Object object) [virtual]`
- `bool _IsAbstract() [virtual]`
- `bool _IsPlaceholderFallbackEnabled() [virtual]`
- `bool _IsTool() [virtual]`
- `bool _IsValid() [virtual]`
- `void _PlaceholderErased(void* placeholder) [virtual]`
- `void* _PlaceholderInstanceCreate(Object forObject) [virtual]`
- `Error _Reload(bool keepState) [virtual]`
- `void _SetSourceCode(string code) [virtual]`
- `void _UpdateExports() [virtual]`

### ScriptLanguageExtension
*Inherits: **ScriptLanguage < Object***

There is currently no description for this class. Please help us by contributing one!

**Methods**
- `void _AddGlobalConstant(StringName name, Variant value) [virtual]`
- `void _AddNamedGlobalConstant(StringName name, Variant value) [virtual]`
- `string _AutoIndentCode(string code, int fromLine, int toLine) [virtual]`
- `bool _CanInheritFromFile() [virtual]`
- `bool _CanMakeFunction() [virtual]`
- `Godot.Collections.Dictionary _CompleteCode(string code, string path, Object owner) [virtual]`
- `Object _CreateScript() [virtual]`
- `Array[Dictionary] _DebugGetCurrentStackInfo() [virtual]`
- `string _DebugGetError() [virtual]`
- `Godot.Collections.Dictionary _DebugGetGlobals(int maxSubitems, int maxDepth) [virtual]`
- `int _DebugGetStackLevelCount() [virtual]`
- `string _DebugGetStackLevelFunction(int level) [virtual]`
- `void* _DebugGetStackLevelInstance(int level) [virtual]`
- `int _DebugGetStackLevelLine(int level) [virtual]`
- `Godot.Collections.Dictionary _DebugGetStackLevelLocals(int level, int maxSubitems, int maxDepth) [virtual]`
- `Godot.Collections.Dictionary _DebugGetStackLevelMembers(int level, int maxSubitems, int maxDepth) [virtual]`
- `string _DebugGetStackLevelSource(int level) [virtual]`
- `string _DebugParseStackLevelExpression(int level, string expression, int maxSubitems, int maxDepth) [virtual]`
- `int _FindFunction(string function, string code) [virtual]`
- `void _Finish() [virtual]`
- `void _Frame() [virtual]`
- `Array[Dictionary] _GetBuiltInTemplates(StringName object) [virtual]`
- `PackedStringArray _GetCommentDelimiters() [virtual]`
- `PackedStringArray _GetDocCommentDelimiters() [virtual]`
- `string _GetExtension() [virtual]`
- `Godot.Collections.Dictionary _GetGlobalClassName(string path) [virtual]`
- `string _GetName() [virtual]`
- `Array[Dictionary] _GetPublicAnnotations() [virtual]`
- `Godot.Collections.Dictionary _GetPublicConstants() [virtual]`
- `Array[Dictionary] _GetPublicFunctions() [virtual]`
- `PackedStringArray _GetRecognizedExtensions() [virtual]`
- `PackedStringArray _GetReservedWords() [virtual]`
- `PackedStringArray _GetStringDelimiters() [virtual]`
- `string _GetType() [virtual]`
- `bool _HandlesGlobalClassType(string type) [virtual]`
- `bool _HasNamedClasses() [virtual]`
- `void _Init() [virtual]`
- `bool _IsControlFlowKeyword(string keyword) [virtual]`
- `bool _IsUsingTemplates() [virtual]`
- `Godot.Collections.Dictionary _LookupCode(string code, string symbol, string path, Object owner) [virtual]`

### ScriptLanguage
*Inherits: **Object** | Inherited by: ScriptLanguageExtension*

There is currently no description for this class. Please help us by contributing one!

### Script
*Inherits: **Resource < RefCounted < Object** | Inherited by: CSharpScript, GDScript, ScriptExtension*

A class stored as a resource. A script extends the functionality of all objects that instantiate it.

**Properties**
- `string SourceCode`

**Methods**
- `bool CanInstantiate()`
- `Script GetBaseScript()`
- `StringName GetGlobalName()`
- `StringName GetInstanceBaseType()`
- `Variant GetPropertyDefaultValue(StringName property)`
- `Variant GetRpcConfig()`
- `Godot.Collections.Dictionary GetScriptConstantMap()`
- `Array[Dictionary] GetScriptMethodList()`
- `Array[Dictionary] GetScriptPropertyList()`
- `Array[Dictionary] GetScriptSignalList()`
- `bool HasScriptSignal(StringName signalName)`
- `bool HasSourceCode()`
- `bool InstanceHas(Object baseObject)`
- `bool IsAbstract()`
- `bool IsTool()`
- `Error Reload(bool keepState = false)`

**C# Examples**
```csharp
using Godot;

[GlobalClass]
public partial class MyNode : Node
{
}
```

### StyleBoxEmpty
*Inherits: **StyleBox < Resource < RefCounted < Object***

An empty StyleBox that can be used to display nothing instead of the default style (e.g. it can "disable" focus styles).

### StyleBoxFlat
*Inherits: **StyleBox < Resource < RefCounted < Object***

By configuring various properties of this style box, you can achieve many common looks without the need of a texture. This includes optionally rounded borders, antialiasing, shadows, and skew.

**Properties**
- `bool AntiAliasing` = `true`
- `float AntiAliasingSize` = `1.0`
- `Color BgColor` = `Color(0.6, 0.6, 0.6, 1)`
- `bool BorderBlend` = `false`
- `Color BorderColor` = `Color(0.8, 0.8, 0.8, 1)`
- `int BorderWidthBottom` = `0`
- `int BorderWidthLeft` = `0`
- `int BorderWidthRight` = `0`
- `int BorderWidthTop` = `0`
- `int CornerDetail` = `8`
- `int CornerRadiusBottomLeft` = `0`
- `int CornerRadiusBottomRight` = `0`
- `int CornerRadiusTopLeft` = `0`
- `int CornerRadiusTopRight` = `0`
- `bool DrawCenter` = `true`
- `float ExpandMarginBottom` = `0.0`
- `float ExpandMarginLeft` = `0.0`
- `float ExpandMarginRight` = `0.0`
- `float ExpandMarginTop` = `0.0`
- `Color ShadowColor` = `Color(0, 0, 0, 0.6)`
- `Vector2 ShadowOffset` = `Vector2(0, 0)`
- `int ShadowSize` = `0`
- `Vector2 Skew` = `Vector2(0, 0)`

**Methods**
- `int GetBorderWidth(Side margin)`
- `int GetBorderWidthMin()`
- `int GetCornerRadius(Corner corner)`
- `float GetExpandMargin(Side margin)`
- `void SetBorderWidth(Side margin, int width)`
- `void SetBorderWidthAll(int width)`
- `void SetCornerRadius(Corner corner, int radius)`
- `void SetCornerRadiusAll(int radius)`
- `void SetExpandMargin(Side margin, float size)`
- `void SetExpandMarginAll(float size)`

### StyleBoxLine
*Inherits: **StyleBox < Resource < RefCounted < Object***

A StyleBox that displays a single line of a given color and thickness. The line can be either horizontal or vertical. Useful for separators.

**Properties**
- `Color Color` = `Color(0, 0, 0, 1)`
- `float GrowBegin` = `1.0`
- `float GrowEnd` = `1.0`
- `int Thickness` = `1`
- `bool Vertical` = `false`

### StyleBoxTexture
*Inherits: **StyleBox < Resource < RefCounted < Object***

A texture-based nine-patch StyleBox, in a way similar to NinePatchRect. This stylebox performs a 3×3 scaling of a texture, where only the center cell is fully stretched. This makes it possible to design bordered styles regardless of the stylebox's size.

**Properties**
- `AxisStretchMode AxisStretchHorizontal` = `0`
- `AxisStretchMode AxisStretchVertical` = `0`
- `bool DrawCenter` = `true`
- `float ExpandMarginBottom` = `0.0`
- `float ExpandMarginLeft` = `0.0`
- `float ExpandMarginRight` = `0.0`
- `float ExpandMarginTop` = `0.0`
- `Color ModulateColor` = `Color(1, 1, 1, 1)`
- `Rect2 RegionRect` = `Rect2(0, 0, 0, 0)`
- `Texture2D Texture`
- `float TextureMarginBottom` = `0.0`
- `float TextureMarginLeft` = `0.0`
- `float TextureMarginRight` = `0.0`
- `float TextureMarginTop` = `0.0`

**Methods**
- `float GetExpandMargin(Side margin)`
- `float GetTextureMargin(Side margin)`
- `void SetExpandMargin(Side margin, float size)`
- `void SetExpandMarginAll(float size)`
- `void SetTextureMargin(Side margin, float size)`
- `void SetTextureMarginAll(float size)`

### StyleBox
*Inherits: **Resource < RefCounted < Object** | Inherited by: StyleBoxEmpty, StyleBoxFlat, StyleBoxLine, StyleBoxTexture*

StyleBox is an abstract base class for drawing stylized boxes for UI elements. It is used for panels, buttons, LineEdit backgrounds, Tree backgrounds, etc. and also for testing a transparency mask for pointer signals. If mask test fails on a StyleBox assigned as mask to a control, clicks and motion signals will go through it to the one below.

**Properties**
- `float ContentMarginBottom` = `-1.0`
- `float ContentMarginLeft` = `-1.0`
- `float ContentMarginRight` = `-1.0`
- `float ContentMarginTop` = `-1.0`

**Methods**
- `void _Draw(RID toCanvasItem, Rect2 rect) [virtual]`
- `Rect2 _GetDrawRect(Rect2 rect) [virtual]`
- `Vector2 _GetMinimumSize() [virtual]`
- `bool _TestMask(Vector2 point, Rect2 rect) [virtual]`
- `void Draw(RID canvasItem, Rect2 rect)`
- `float GetContentMargin(Side margin)`
- `CanvasItem GetCurrentItemDrawn()`
- `float GetMargin(Side margin)`
- `Vector2 GetMinimumSize()`
- `Vector2 GetOffset()`
- `void SetContentMargin(Side margin, float offset)`
- `void SetContentMarginAll(float offset)`
- `bool TestMask(Vector2 point, Rect2 rect)`

### SystemFont
*Inherits: **Font < Resource < RefCounted < Object***

SystemFont loads a font from a system font with the first matching name from font_names.

**Properties**
- `bool AllowSystemFallback` = `true`
- `FontAntialiasing Antialiasing` = `1`
- `bool DisableEmbeddedBitmaps` = `true`
- `bool FontItalic` = `false`
- `PackedStringArray FontNames` = `PackedStringArray()`
- `int FontStretch` = `100`
- `int FontWeight` = `400`
- `bool ForceAutohinter` = `false`
- `bool GenerateMipmaps` = `false`
- `Hinting Hinting` = `1`
- `bool KeepRoundingRemainders` = `true`
- `bool ModulateColorGlyphs` = `false`
- `int MsdfPixelRange` = `16`
- `int MsdfSize` = `48`
- `bool MultichannelSignedDistanceField` = `false`
- `float Oversampling` = `0.0`
- `SubpixelPositioning SubpixelPositioning` = `1`

### Texture2DArrayRD
*Inherits: **TextureLayeredRD < TextureLayered < Texture < Resource < RefCounted < Object***

This texture array class allows you to use a 2D array texture created directly on the RenderingDevice as a texture for materials, meshes, etc.

### Texture2DArray
*Inherits: **ImageTextureLayered < TextureLayered < Texture < Resource < RefCounted < Object***

A Texture2DArray is different from a Texture3D: The Texture2DArray does not support trilinear interpolation between the Images, i.e. no blending. See also Cubemap and CubemapArray, which are texture arrays with specialized cubemap functions.

**Methods**
- `Resource CreatePlaceholder()`

### Texture2DRD
*Inherits: **Texture2D < Texture < Resource < RefCounted < Object***

This texture class allows you to use a 2D texture created directly on the RenderingDevice as a texture for materials, meshes, etc.

**Properties**
- `bool ResourceLocalToScene` = `false (overrides Resource)`
- `RID TextureRdRid`

### Texture2D
*Inherits: **Texture < Resource < RefCounted < Object** | Inherited by: AnimatedTexture, AtlasTexture, CameraTexture, CanvasTexture, CompressedTexture2D, CurveTexture, ...*

A texture works by registering an image in the video hardware, which then can be used in 3D models or 2D Sprite2D or GUI Control.

**Methods**
- `void _Draw(RID toCanvasItem, Vector2 pos, Color modulate, bool transpose) [virtual]`
- `void _DrawRect(RID toCanvasItem, Rect2 rect, bool tile, Color modulate, bool transpose) [virtual]`
- `void _DrawRectRegion(RID toCanvasItem, Rect2 rect, Rect2 srcRect, Color modulate, bool transpose, bool clipUv) [virtual]`
- `int _GetHeight() [virtual]`
- `int _GetWidth() [virtual]`
- `bool _HasAlpha() [virtual]`
- `bool _IsPixelOpaque(int x, int y) [virtual]`
- `Resource CreatePlaceholder()`
- `void Draw(RID canvasItem, Vector2 position, Color modulate = Color(1, 1, 1, 1), bool transpose = false)`
- `void DrawRect(RID canvasItem, Rect2 rect, bool tile, Color modulate = Color(1, 1, 1, 1), bool transpose = false)`
- `void DrawRectRegion(RID canvasItem, Rect2 rect, Rect2 srcRect, Color modulate = Color(1, 1, 1, 1), bool transpose = false, bool clipUv = true)`
- `int GetHeight()`
- `Image GetImage()`
- `Vector2 GetSize()`
- `int GetWidth()`
- `bool HasAlpha()`

### Texture3DRD
*Inherits: **Texture3D < Texture < Resource < RefCounted < Object***

This texture class allows you to use a 3D texture created directly on the RenderingDevice as a texture for materials, meshes, etc.

**Properties**
- `RID TextureRdRid`

### Texture3D
*Inherits: **Texture < Resource < RefCounted < Object** | Inherited by: CompressedTexture3D, ImageTexture3D, NoiseTexture3D, PlaceholderTexture3D, Texture3DRD*

Base class for ImageTexture3D and CompressedTexture3D. Cannot be used directly, but contains all the functions necessary for accessing the derived resource types. Texture3D is the base class for all 3-dimensional texture types. See also TextureLayered.

**Methods**
- `Array[Image] _GetData() [virtual]`
- `int _GetDepth() [virtual]`
- `Format _GetFormat() [virtual]`
- `int _GetHeight() [virtual]`
- `int _GetWidth() [virtual]`
- `bool _HasMipmaps() [virtual]`
- `Resource CreatePlaceholder()`
- `Array[Image] GetData()`
- `int GetDepth()`
- `Format GetFormat()`
- `int GetHeight()`
- `int GetWidth()`
- `bool HasMipmaps()`

### TextureCubemapArrayRD
*Inherits: **TextureLayeredRD < TextureLayered < Texture < Resource < RefCounted < Object***

This texture class allows you to use a cubemap array texture created directly on the RenderingDevice as a texture for materials, meshes, etc.

### TextureCubemapRD
*Inherits: **TextureLayeredRD < TextureLayered < Texture < Resource < RefCounted < Object***

This texture class allows you to use a cubemap texture created directly on the RenderingDevice as a texture for materials, meshes, etc.

### TextureLayeredRD
*Inherits: **TextureLayered < Texture < Resource < RefCounted < Object** | Inherited by: Texture2DArrayRD, TextureCubemapArrayRD, TextureCubemapRD*

Base class for Texture2DArrayRD, TextureCubemapRD and TextureCubemapArrayRD. Cannot be used directly, but contains all the functions necessary for accessing the derived resource types.

**Properties**
- `RID TextureRdRid`

### TextureLayered
*Inherits: **Texture < Resource < RefCounted < Object** | Inherited by: CompressedTextureLayered, ImageTextureLayered, PlaceholderTextureLayered, TextureLayeredRD*

Base class for ImageTextureLayered and CompressedTextureLayered. Cannot be used directly, but contains all the functions necessary for accessing the derived resource types. See also Texture3D.

**Methods**
- `Format _GetFormat() [virtual]`
- `int _GetHeight() [virtual]`
- `Image _GetLayerData(int layerIndex) [virtual]`
- `int _GetLayeredType() [virtual]`
- `int _GetLayers() [virtual]`
- `int _GetWidth() [virtual]`
- `bool _HasMipmaps() [virtual]`
- `Format GetFormat()`
- `int GetHeight()`
- `Image GetLayerData(int layer)`
- `LayeredType GetLayeredType()`
- `int GetLayers()`
- `int GetWidth()`
- `bool HasMipmaps()`

### TextureProgressBar
*Inherits: **Range < Control < CanvasItem < Node < Object***

TextureProgressBar works like ProgressBar, but uses up to 3 textures instead of Godot's Theme resource. It can be used to create horizontal, vertical and radial progress bars.

**Properties**
- `int FillMode` = `0`
- `MouseFilter MouseFilter` = `1 (overrides Control)`
- `bool NinePatchStretch` = `false`
- `Vector2 RadialCenterOffset` = `Vector2(0, 0)`
- `float RadialFillDegrees` = `360.0`
- `float RadialInitialAngle` = `0.0`
- `BitField[SizeFlags] SizeFlagsVertical` = `1 (overrides Control)`
- `float Step` = `1.0 (overrides Range)`
- `int StretchMarginBottom` = `0`
- `int StretchMarginLeft` = `0`
- `int StretchMarginRight` = `0`
- `int StretchMarginTop` = `0`
- `Texture2D TextureOver`
- `Texture2D TextureProgress`
- `Vector2 TextureProgressOffset` = `Vector2(0, 0)`
- `Texture2D TextureUnder`
- `Color TintOver` = `Color(1, 1, 1, 1)`
- `Color TintProgress` = `Color(1, 1, 1, 1)`
- `Color TintUnder` = `Color(1, 1, 1, 1)`

**Methods**
- `int GetStretchMargin(Side margin)`
- `void SetStretchMargin(Side margin, int value)`

### Texture
*Inherits: **Resource < RefCounted < Object** | Inherited by: Texture2D, Texture3D, TextureLayered*

Texture is the base class for all texture types. Common texture types are Texture2D and ImageTexture. See also Image.

### TileData
*Inherits: **Object***

TileData object represents a single tile in a TileSet. It is usually edited using the tileset editor, but it can be modified at runtime using TileMapLayer._tile_data_runtime_update().

**Properties**
- `bool FlipH` = `false`
- `bool FlipV` = `false`
- `Material Material`
- `Color Modulate` = `Color(1, 1, 1, 1)`
- `float Probability` = `1.0`
- `int Terrain` = `-1`
- `int TerrainSet` = `-1`
- `Vector2i TextureOrigin` = `Vector2i(0, 0)`
- `bool Transpose` = `false`
- `int YSortOrigin` = `0`
- `int ZIndex` = `0`

**Methods**
- `void AddCollisionPolygon(int layerId)`
- `void AddOccluderPolygon(int layerId)`
- `float GetCollisionPolygonOneWayMargin(int layerId, int polygonIndex)`
- `PackedVector2Array GetCollisionPolygonPoints(int layerId, int polygonIndex)`
- `int GetCollisionPolygonsCount(int layerId)`
- `float GetConstantAngularVelocity(int layerId)`
- `Vector2 GetConstantLinearVelocity(int layerId)`
- `Variant GetCustomData(string layerName)`
- `Variant GetCustomDataByLayerId(int layerId)`
- `NavigationPolygon GetNavigationPolygon(int layerId, bool flipH = false, bool flipV = false, bool transpose = false)`
- `OccluderPolygon2D GetOccluder(int layerId, bool flipH = false, bool flipV = false, bool transpose = false)`
- `OccluderPolygon2D GetOccluderPolygon(int layerId, int polygonIndex, bool flipH = false, bool flipV = false, bool transpose = false)`
- `int GetOccluderPolygonsCount(int layerId)`
- `int GetTerrainPeeringBit(CellNeighbor peeringBit)`
- `bool HasCustomData(string layerName)`
- `bool IsCollisionPolygonOneWay(int layerId, int polygonIndex)`
- `bool IsValidTerrainPeeringBit(CellNeighbor peeringBit)`
- `void RemoveCollisionPolygon(int layerId, int polygonIndex)`
- `void RemoveOccluderPolygon(int layerId, int polygonIndex)`
- `void SetCollisionPolygonOneWay(int layerId, int polygonIndex, bool oneWay)`
- `void SetCollisionPolygonOneWayMargin(int layerId, int polygonIndex, float oneWayMargin)`
- `void SetCollisionPolygonPoints(int layerId, int polygonIndex, PackedVector2Array polygon)`
- `void SetCollisionPolygonsCount(int layerId, int polygonsCount)`
- `void SetConstantAngularVelocity(int layerId, float velocity)`
- `void SetConstantLinearVelocity(int layerId, Vector2 velocity)`
- `void SetCustomData(string layerName, Variant value)`
- `void SetCustomDataByLayerId(int layerId, Variant value)`
- `void SetNavigationPolygon(int layerId, NavigationPolygon navigationPolygon)`
- `void SetOccluder(int layerId, OccluderPolygon2D occluderPolygon)`
- `void SetOccluderPolygon(int layerId, int polygonIndex, OccluderPolygon2D polygon)`
- `void SetOccluderPolygonsCount(int layerId, int polygonsCount)`
- `void SetTerrainPeeringBit(CellNeighbor peeringBit, int terrain)`

### TileSetAtlasSource
*Inherits: **TileSetSource < Resource < RefCounted < Object***

An atlas is a grid of tiles laid out on a texture. Each tile in the grid must be exposed using create_tile(). Those tiles are then indexed using their coordinates in the grid.

**Properties**
- `Vector2i Margins` = `Vector2i(0, 0)`
- `Vector2i Separation` = `Vector2i(0, 0)`
- `Texture2D Texture`
- `Vector2i TextureRegionSize` = `Vector2i(16, 16)`
- `bool UseTexturePadding` = `true`

**Methods**
- `void ClearTilesOutsideTexture()`
- `int CreateAlternativeTile(Vector2i atlasCoords, int alternativeIdOverride = -1)`
- `void CreateTile(Vector2i atlasCoords, Vector2i size = Vector2i(1, 1))`
- `Vector2i GetAtlasGridSize()`
- `int GetNextAlternativeTileId(Vector2i atlasCoords)`
- `Texture2D GetRuntimeTexture()`
- `Rect2i GetRuntimeTileTextureRegion(Vector2i atlasCoords, int frame)`
- `int GetTileAnimationColumns(Vector2i atlasCoords)`
- `float GetTileAnimationFrameDuration(Vector2i atlasCoords, int frameIndex)`
- `int GetTileAnimationFramesCount(Vector2i atlasCoords)`
- `TileAnimationMode GetTileAnimationMode(Vector2i atlasCoords)`
- `Vector2i GetTileAnimationSeparation(Vector2i atlasCoords)`
- `float GetTileAnimationSpeed(Vector2i atlasCoords)`
- `float GetTileAnimationTotalDuration(Vector2i atlasCoords)`
- `Vector2i GetTileAtCoords(Vector2i atlasCoords)`
- `TileData GetTileData(Vector2i atlasCoords, int alternativeTile)`
- `Vector2i GetTileSizeInAtlas(Vector2i atlasCoords)`
- `Rect2i GetTileTextureRegion(Vector2i atlasCoords, int frame = 0)`
- `PackedVector2Array GetTilesToBeRemovedOnChange(Texture2D texture, Vector2i margins, Vector2i separation, Vector2i textureRegionSize)`
- `bool HasRoomForTile(Vector2i atlasCoords, Vector2i size, int animationColumns, Vector2i animationSeparation, int framesCount, Vector2i ignoredTile = Vector2i(-1, -1))`
- `bool HasTilesOutsideTexture()`
- `void MoveTileInAtlas(Vector2i atlasCoords, Vector2i newAtlasCoords = Vector2i(-1, -1), Vector2i newSize = Vector2i(-1, -1))`
- `void RemoveAlternativeTile(Vector2i atlasCoords, int alternativeTile)`
- `void RemoveTile(Vector2i atlasCoords)`
- `void SetAlternativeTileId(Vector2i atlasCoords, int alternativeTile, int newId)`
- `void SetTileAnimationColumns(Vector2i atlasCoords, int frameColumns)`
- `void SetTileAnimationFrameDuration(Vector2i atlasCoords, int frameIndex, float duration)`
- `void SetTileAnimationFramesCount(Vector2i atlasCoords, int framesCount)`
- `void SetTileAnimationMode(Vector2i atlasCoords, TileAnimationMode mode)`
- `void SetTileAnimationSeparation(Vector2i atlasCoords, Vector2i separation)`
- `void SetTileAnimationSpeed(Vector2i atlasCoords, float speed)`

### TileSetScenesCollectionSource
*Inherits: **TileSetSource < Resource < RefCounted < Object***

When placed on a TileMapLayer, tiles from TileSetScenesCollectionSource will automatically instantiate an associated scene at the cell's position in the TileMapLayer.

**Methods**
- `int CreateSceneTile(PackedScene packedScene, int idOverride = -1)`
- `int GetNextSceneTileId()`
- `bool GetSceneTileDisplayPlaceholder(int id)`
- `int GetSceneTileId(int index)`
- `PackedScene GetSceneTileScene(int id)`
- `int GetSceneTilesCount()`
- `bool HasSceneTileId(int id)`
- `void RemoveSceneTile(int id)`
- `void SetSceneTileDisplayPlaceholder(int id, bool displayPlaceholder)`
- `void SetSceneTileId(int id, int newId)`
- `void SetSceneTileScene(int id, PackedScene packedScene)`

**C# Examples**
```csharp
int sourceId = tileMapLayer.GetCellSourceId(new Vector2I(x, y));
if (sourceId > -1)
{
    TileSetSource source = tileMapLayer.TileSet.GetSource(sourceId);
    if (source is TileSetScenesCollectionSource sceneSource)
    {
        int altId = tileMapLayer.GetCellAlternativeTile(new Vector2I(x, y));
        // The assigned PackedScene.
        PackedScene scene = sceneSource.GetSceneTileScene(altId);
    }
}
```

### TileSetSource
*Inherits: **Resource < RefCounted < Object** | Inherited by: TileSetAtlasSource, TileSetScenesCollectionSource*

Exposes a set of tiles for a TileSet resource.

**Methods**
- `int GetAlternativeTileId(Vector2i atlasCoords, int index)`
- `int GetAlternativeTilesCount(Vector2i atlasCoords)`
- `Vector2i GetTileId(int index)`
- `int GetTilesCount()`
- `bool HasAlternativeTile(Vector2i atlasCoords, int alternativeTile)`
- `bool HasTile(Vector2i atlasCoords)`

### TileSet
*Inherits: **Resource < RefCounted < Object***

A TileSet is a library of tiles for a TileMapLayer. A TileSet handles a list of TileSetSource, each of them storing a set of tiles.

**Properties**
- `TileLayout TileLayout` = `0`
- `TileOffsetAxis TileOffsetAxis` = `0`
- `TileShape TileShape` = `0`
- `Vector2i TileSize` = `Vector2i(16, 16)`
- `bool UvClipping` = `false`

**Methods**
- `void AddCustomDataLayer(int toPosition = -1)`
- `void AddNavigationLayer(int toPosition = -1)`
- `void AddOcclusionLayer(int toPosition = -1)`
- `int AddPattern(TileMapPattern pattern, int index = -1)`
- `void AddPhysicsLayer(int toPosition = -1)`
- `int AddSource(TileSetSource source, int atlasSourceIdOverride = -1)`
- `void AddTerrain(int terrainSet, int toPosition = -1)`
- `void AddTerrainSet(int toPosition = -1)`
- `void CleanupInvalidTileProxies()`
- `void ClearTileProxies()`
- `Godot.Collections.Array GetAlternativeLevelTileProxy(int sourceFrom, Vector2i coordsFrom, int alternativeFrom)`
- `Godot.Collections.Array GetCoordsLevelTileProxy(int sourceFrom, Vector2i coordsFrom)`
- `int GetCustomDataLayerByName(string layerName)`
- `string GetCustomDataLayerName(int layerIndex)`
- `Variant.Type GetCustomDataLayerType(int layerIndex)`
- `int GetCustomDataLayersCount()`
- `bool GetNavigationLayerLayerValue(int layerIndex, int layerNumber)`
- `int GetNavigationLayerLayers(int layerIndex)`
- `int GetNavigationLayersCount()`
- `int GetNextSourceId()`
- `int GetOcclusionLayerLightMask(int layerIndex)`
- `bool GetOcclusionLayerSdfCollision(int layerIndex)`
- `int GetOcclusionLayersCount()`
- `TileMapPattern GetPattern(int index = -1)`
- `int GetPatternsCount()`
- `int GetPhysicsLayerCollisionLayer(int layerIndex)`
- `int GetPhysicsLayerCollisionMask(int layerIndex)`
- `float GetPhysicsLayerCollisionPriority(int layerIndex)`
- `PhysicsMaterial GetPhysicsLayerPhysicsMaterial(int layerIndex)`
- `int GetPhysicsLayersCount()`
- `TileSetSource GetSource(int sourceId)`
- `int GetSourceCount()`
- `int GetSourceId(int index)`
- `int GetSourceLevelTileProxy(int sourceFrom)`
- `Color GetTerrainColor(int terrainSet, int terrainIndex)`
- `string GetTerrainName(int terrainSet, int terrainIndex)`
- `TerrainMode GetTerrainSetMode(int terrainSet)`
- `int GetTerrainSetsCount()`
- `int GetTerrainsCount(int terrainSet)`
- `bool HasAlternativeLevelTileProxy(int sourceFrom, Vector2i coordsFrom, int alternativeFrom)`
