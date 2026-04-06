# Godot 4 C# API Reference — Nodes 2D

> C#-only reference. 43 classes.

### AnimatableBody2D
*Inherits: **StaticBody2D < PhysicsBody2D < CollisionObject2D < Node2D < CanvasItem < Node < Object***

An animatable 2D physics body. It can't be moved by external forces or contacts, but can be moved manually by other means such as code, AnimationMixers (with AnimationMixer.callback_mode_process set to AnimationMixer.ANIMATION_CALLBACK_MODE_PROCESS_PHYSICS), and RemoteTransform2D.

**Properties**
- `bool SyncToPhysics` = `true`

### AnimatedSprite2D
*Inherits: **Node2D < CanvasItem < Node < Object***

AnimatedSprite2D is similar to the Sprite2D node, except it carries multiple textures as animation frames. Animations are created using a SpriteFrames resource, which allows you to import image files (or a folder containing said files) to provide the animation frames for the sprite. The SpriteFrames resource can be configured in the editor via the SpriteFrames bottom panel.

**Properties**
- `StringName Animation` = `&"default"`
- `string Autoplay` = `""`
- `bool Centered` = `true`
- `bool FlipH` = `false`
- `bool FlipV` = `false`
- `int Frame` = `0`
- `float FrameProgress` = `0.0`
- `Vector2 Offset` = `Vector2(0, 0)`
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

### CPUParticles2D
*Inherits: **Node2D < CanvasItem < Node < Object***

CPU-based 2D particle node used to create a variety of particle systems and effects.

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
- `Vector2 Direction` = `Vector2(1, 0)`
- `DrawOrder DrawOrder` = `0`
- `PackedColorArray EmissionColors`
- `PackedVector2Array EmissionNormals`
- `PackedVector2Array EmissionPoints`
- `Vector2 EmissionRectExtents`
- `float EmissionRingInnerRadius`
- `float EmissionRingRadius`
- `EmissionShape EmissionShape` = `0`
- `float EmissionSphereRadius`
- `bool Emitting` = `true`

**Methods**
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

### Camera2D
*Inherits: **Node2D < CanvasItem < Node < Object***

Camera node for 2D scenes. It forces the screen (current layer) to scroll following this node. This makes it easier (and faster) to program scrollable scenes than manually changing the position of CanvasItem-based nodes.

**Properties**
- `AnchorMode AnchorMode` = `1`
- `Node CustomViewport`
- `float DragBottomMargin` = `0.2`
- `bool DragHorizontalEnabled` = `false`
- `float DragHorizontalOffset` = `0.0`
- `float DragLeftMargin` = `0.2`
- `float DragRightMargin` = `0.2`
- `float DragTopMargin` = `0.2`
- `bool DragVerticalEnabled` = `false`
- `float DragVerticalOffset` = `0.0`
- `bool EditorDrawDragMargin` = `false`
- `bool EditorDrawLimits` = `false`
- `bool EditorDrawScreen` = `true`
- `bool Enabled` = `true`
- `bool IgnoreRotation` = `true`
- `int LimitBottom` = `10000000`
- `bool LimitEnabled` = `true`
- `int LimitLeft` = `-10000000`
- `int LimitRight` = `10000000`
- `bool LimitSmoothed` = `false`
- `int LimitTop` = `-10000000`
- `Vector2 Offset` = `Vector2(0, 0)`
- `bool PositionSmoothingEnabled` = `false`
- `float PositionSmoothingSpeed` = `5.0`
- `Camera2DProcessCallback ProcessCallback` = `1`
- `bool RotationSmoothingEnabled` = `false`
- `float RotationSmoothingSpeed` = `5.0`
- `Vector2 Zoom` = `Vector2(1, 1)`

**Methods**
- `void Align()`
- `void ForceUpdateScroll()`
- `float GetDragMargin(Side margin)`
- `int GetLimit(Side margin)`
- `Vector2 GetScreenCenterPosition()`
- `float GetScreenRotation()`
- `Vector2 GetTargetPosition()`
- `bool IsCurrent()`
- `void MakeCurrent()`
- `void ResetSmoothing()`
- `void SetDragMargin(Side margin, float dragMargin)`
- `void SetLimit(Side margin, int limit)`

### CanvasItemMaterial
*Inherits: **Material < Resource < RefCounted < Object***

CanvasItemMaterials provide a means of modifying the textures associated with a CanvasItem. They specialize in describing blend and lighting behaviors for textures. Use a ShaderMaterial to more fully customize a material's interactions with a CanvasItem.

**Properties**
- `BlendMode BlendMode` = `0`
- `LightMode LightMode` = `0`
- `int ParticlesAnimHFrames`
- `bool ParticlesAnimLoop`
- `int ParticlesAnimVFrames`
- `bool ParticlesAnimation` = `false`

### CanvasItem
*Inherits: **Node < Object** | Inherited by: Control, Node2D*

Abstract base class for everything in 2D space. Canvas items are laid out in a tree; children inherit and extend their parent's transform. CanvasItem is extended by Control for GUI-related nodes, and by Node2D for 2D game objects.

**Properties**
- `ClipChildrenMode ClipChildren` = `0`
- `int LightMask` = `1`
- `Material Material`
- `Color Modulate` = `Color(1, 1, 1, 1)`
- `Color SelfModulate` = `Color(1, 1, 1, 1)`
- `bool ShowBehindParent` = `false`
- `TextureFilter TextureFilter` = `0`
- `TextureRepeat TextureRepeat` = `0`
- `bool TopLevel` = `false`
- `bool UseParentMaterial` = `false`
- `int VisibilityLayer` = `1`
- `bool Visible` = `true`
- `bool YSortEnabled` = `false`
- `bool ZAsRelative` = `true`
- `int ZIndex` = `0`

**Methods**
- `void _Draw() [virtual]`
- `void DrawAnimationSlice(float animationLength, float sliceBegin, float sliceEnd, float offset = 0.0)`
- `void DrawArc(Vector2 center, float radius, float startAngle, float endAngle, int pointCount, Color color, float width = -1.0, bool antialiased = false)`
- `void DrawChar(Font font, Vector2 pos, string char, int fontSize = 16, Color modulate = Color(1, 1, 1, 1), float oversampling = 0.0)`
- `void DrawCharOutline(Font font, Vector2 pos, string char, int fontSize = 16, int size = -1, Color modulate = Color(1, 1, 1, 1), float oversampling = 0.0)`
- `void DrawCircle(Vector2 position, float radius, Color color, bool filled = true, float width = -1.0, bool antialiased = false)`
- `void DrawColoredPolygon(PackedVector2Array points, Color color, PackedVector2Array uvs = PackedVector2Array(), Texture2D texture = null)`
- `void DrawDashedLine(Vector2 from, Vector2 to, Color color, float width = -1.0, float dash = 2.0, bool aligned = true, bool antialiased = false)`
- `void DrawEllipse(Vector2 position, float major, float minor, Color color, bool filled = true, float width = -1.0, bool antialiased = false)`
- `void DrawEllipseArc(Vector2 center, float major, float minor, float startAngle, float endAngle, int pointCount, Color color, float width = -1.0, bool antialiased = false)`
- `void DrawEndAnimation()`
- `void DrawLcdTextureRectRegion(Texture2D texture, Rect2 rect, Rect2 srcRect, Color modulate = Color(1, 1, 1, 1))`
- `void DrawLine(Vector2 from, Vector2 to, Color color, float width = -1.0, bool antialiased = false)`
- `void DrawMesh(Mesh mesh, Texture2D texture, Transform2D transform = Transform2D(1, 0, 0, 1, 0, 0), Color modulate = Color(1, 1, 1, 1))`
- `void DrawMsdfTextureRectRegion(Texture2D texture, Rect2 rect, Rect2 srcRect, Color modulate = Color(1, 1, 1, 1), float outline = 0.0, float pixelRange = 4.0, float scale = 1.0)`
- `void DrawMultiline(PackedVector2Array points, Color color, float width = -1.0, bool antialiased = false)`
- `void DrawMultilineColors(PackedVector2Array points, PackedColorArray colors, float width = -1.0, bool antialiased = false)`
- `void DrawMultilineString(Font font, Vector2 pos, string text, HorizontalAlignment alignment = 0, float width = -1, int fontSize = 16, int maxLines = -1, Color modulate = Color(1, 1, 1, 1), BitField[LineBreakFlag] brkFlags = 3, BitField[JustificationFlag] justificationFlags = 3, Direction direction = 0, Orientation orientation = 0, float oversampling = 0.0)`
- `void DrawMultilineStringOutline(Font font, Vector2 pos, string text, HorizontalAlignment alignment = 0, float width = -1, int fontSize = 16, int maxLines = -1, int size = 1, Color modulate = Color(1, 1, 1, 1), BitField[LineBreakFlag] brkFlags = 3, BitField[JustificationFlag] justificationFlags = 3, Direction direction = 0, Orientation orientation = 0, float oversampling = 0.0)`
- `void DrawMultimesh(MultiMesh multimesh, Texture2D texture)`
- `void DrawPolygon(PackedVector2Array points, PackedColorArray colors, PackedVector2Array uvs = PackedVector2Array(), Texture2D texture = null)`
- `void DrawPolyline(PackedVector2Array points, Color color, float width = -1.0, bool antialiased = false)`
- `void DrawPolylineColors(PackedVector2Array points, PackedColorArray colors, float width = -1.0, bool antialiased = false)`
- `void DrawPrimitive(PackedVector2Array points, PackedColorArray colors, PackedVector2Array uvs, Texture2D texture = null)`
- `void DrawRect(Rect2 rect, Color color, bool filled = true, float width = -1.0, bool antialiased = false)`
- `void DrawSetTransform(Vector2 position, float rotation = 0.0, Vector2 scale = Vector2(1, 1))`
- `void DrawSetTransformMatrix(Transform2D xform)`
- `void DrawString(Font font, Vector2 pos, string text, HorizontalAlignment alignment = 0, float width = -1, int fontSize = 16, Color modulate = Color(1, 1, 1, 1), BitField[JustificationFlag] justificationFlags = 3, Direction direction = 0, Orientation orientation = 0, float oversampling = 0.0)`
- `void DrawStringOutline(Font font, Vector2 pos, string text, HorizontalAlignment alignment = 0, float width = -1, int fontSize = 16, int size = 1, Color modulate = Color(1, 1, 1, 1), BitField[JustificationFlag] justificationFlags = 3, Direction direction = 0, Orientation orientation = 0, float oversampling = 0.0)`
- `void DrawStyleBox(StyleBox styleBox, Rect2 rect)`
- `void DrawTexture(Texture2D texture, Vector2 position, Color modulate = Color(1, 1, 1, 1))`
- `void DrawTextureRect(Texture2D texture, Rect2 rect, bool tile, Color modulate = Color(1, 1, 1, 1), bool transpose = false)`
- `void DrawTextureRectRegion(Texture2D texture, Rect2 rect, Rect2 srcRect, Color modulate = Color(1, 1, 1, 1), bool transpose = false, bool clipUv = true)`
- `void ForceUpdateTransform()`
- `RID GetCanvas()`
- `RID GetCanvasItem()`
- `CanvasLayer GetCanvasLayerNode()`
- `Transform2D GetCanvasTransform()`
- `Vector2 GetGlobalMousePosition()`
- `Transform2D GetGlobalTransform()`

**C# Examples**
```csharp
DrawString(ThemeDB.FallbackFont, new Vector2(64, 64), "Hello world", HorizontalAlignment.Left, -1, ThemeDB.FallbackFontSize);
```

### CanvasLayer
*Inherits: **Node < Object** | Inherited by: ParallaxBackground*

CanvasItem-derived nodes that are direct or indirect children of a CanvasLayer will be drawn in that layer. The layer is a numeric index that defines the draw order. The default 2D scene renders with index 0, so a CanvasLayer with index -1 will be drawn below, and a CanvasLayer with index 1 will be drawn above. This order will hold regardless of the CanvasItem.z_index of the nodes within each layer.

**Properties**
- `Node CustomViewport`
- `bool FollowViewportEnabled` = `false`
- `float FollowViewportScale` = `1.0`
- `int Layer` = `1`
- `Vector2 Offset` = `Vector2(0, 0)`
- `float Rotation` = `0.0`
- `Vector2 Scale` = `Vector2(1, 1)`
- `Transform2D Transform` = `Transform2D(1, 0, 0, 1, 0, 0)`
- `bool Visible` = `true`

**Methods**
- `RID GetCanvas()`
- `Transform2D GetFinalTransform()`
- `void Hide()`
- `void Show()`

### CanvasModulate
*Inherits: **Node2D < CanvasItem < Node < Object***

CanvasModulate applies a color tint to all nodes on a canvas. Only one can be used to tint a canvas, but CanvasLayers can be used to render things independently.

**Properties**
- `Color Color` = `Color(1, 1, 1, 1)`

### CharacterBody2D
*Inherits: **PhysicsBody2D < CollisionObject2D < Node2D < CanvasItem < Node < Object***

CharacterBody2D is a specialized class for physics bodies that are meant to be user-controlled. They are not affected by physics at all, but they affect other physics bodies in their path. They are mainly used to provide high-level API to move objects with wall and slope detection (move_and_slide() method) in addition to the general collision detection provided by PhysicsBody2D.move_and_collide(). This makes it useful for highly configurable physics bodies that must move in specific ways and collide with the world, as is often the case with user-controlled characters.

**Properties**
- `bool FloorBlockOnWall` = `true`
- `bool FloorConstantSpeed` = `false`
- `float FloorMaxAngle` = `0.7853982`
- `float FloorSnapLength` = `1.0`
- `bool FloorStopOnSlope` = `true`
- `int MaxSlides` = `4`
- `MotionMode MotionMode` = `0`
- `int PlatformFloorLayers` = `4294967295`
- `PlatformOnLeave PlatformOnLeave` = `0`
- `int PlatformWallLayers` = `0`
- `float SafeMargin` = `0.08`
- `bool SlideOnCeiling` = `true`
- `Vector2 UpDirection` = `Vector2(0, -1)`
- `Vector2 Velocity` = `Vector2(0, 0)`
- `float WallMinSlideAngle` = `0.2617994`

**Methods**
- `void ApplyFloorSnap()`
- `float GetFloorAngle(Vector2 upDirection = Vector2(0, -1))`
- `Vector2 GetFloorNormal()`
- `Vector2 GetLastMotion()`
- `KinematicCollision2D GetLastSlideCollision()`
- `Vector2 GetPlatformVelocity()`
- `Vector2 GetPositionDelta()`
- `Vector2 GetRealVelocity()`
- `KinematicCollision2D GetSlideCollision(int slideIdx)`
- `int GetSlideCollisionCount()`
- `Vector2 GetWallNormal()`
- `bool IsOnCeiling()`
- `bool IsOnCeilingOnly()`
- `bool IsOnFloor()`
- `bool IsOnFloorOnly()`
- `bool IsOnWall()`
- `bool IsOnWallOnly()`
- `bool MoveAndSlide()`

**C# Examples**
```csharp
for (int i = 0; i < GetSlideCollisionCount(); i++)
{
    KinematicCollision2D collision = GetSlideCollision(i);
    GD.Print("Collided with: ", (collision.GetCollider() as Node).Name);
}
```

### CollisionObject2D
*Inherits: **Node2D < CanvasItem < Node < Object** | Inherited by: Area2D, PhysicsBody2D*

Abstract base class for 2D physics objects. CollisionObject2D can hold any number of Shape2Ds for collision. Each shape must be assigned to a shape owner. Shape owners are not nodes and do not appear in the editor, but are accessible through code using the shape_owner_* methods.

**Properties**
- `int CollisionLayer` = `1`
- `int CollisionMask` = `1`
- `float CollisionPriority` = `1.0`
- `DisableMode DisableMode` = `0`
- `bool InputPickable` = `true`

**Methods**
- `void _InputEvent(Viewport viewport, InputEvent event, int shapeIdx) [virtual]`
- `void _MouseEnter() [virtual]`
- `void _MouseExit() [virtual]`
- `void _MouseShapeEnter(int shapeIdx) [virtual]`
- `void _MouseShapeExit(int shapeIdx) [virtual]`
- `int CreateShapeOwner(Object owner)`
- `bool GetCollisionLayerValue(int layerNumber)`
- `bool GetCollisionMaskValue(int layerNumber)`
- `RID GetRid()`
- `float GetShapeOwnerOneWayCollisionMargin(int ownerId)`
- `PackedInt32Array GetShapeOwners()`
- `bool IsShapeOwnerDisabled(int ownerId)`
- `bool IsShapeOwnerOneWayCollisionEnabled(int ownerId)`
- `void RemoveShapeOwner(int ownerId)`
- `void SetCollisionLayerValue(int layerNumber, bool value)`
- `void SetCollisionMaskValue(int layerNumber, bool value)`
- `int ShapeFindOwner(int shapeIndex)`
- `void ShapeOwnerAddShape(int ownerId, Shape2D shape)`
- `void ShapeOwnerClearShapes(int ownerId)`
- `Object ShapeOwnerGetOwner(int ownerId)`
- `Shape2D ShapeOwnerGetShape(int ownerId, int shapeId)`
- `int ShapeOwnerGetShapeCount(int ownerId)`
- `int ShapeOwnerGetShapeIndex(int ownerId, int shapeId)`
- `Transform2D ShapeOwnerGetTransform(int ownerId)`
- `void ShapeOwnerRemoveShape(int ownerId, int shapeId)`
- `void ShapeOwnerSetDisabled(int ownerId, bool disabled)`
- `void ShapeOwnerSetOneWayCollision(int ownerId, bool enable)`
- `void ShapeOwnerSetOneWayCollisionMargin(int ownerId, float margin)`
- `void ShapeOwnerSetTransform(int ownerId, Transform2D transform)`

### CollisionPolygon2D
*Inherits: **Node2D < CanvasItem < Node < Object***

A node that provides a polygon shape to a CollisionObject2D parent and allows it to be edited. The polygon can be concave or convex. This can give a detection shape to an Area2D, turn a PhysicsBody2D into a solid object, or give a hollow shape to a StaticBody2D.

**Properties**
- `BuildMode BuildMode` = `0`
- `bool Disabled` = `false`
- `bool OneWayCollision` = `false`
- `float OneWayCollisionMargin` = `1.0`
- `PackedVector2Array Polygon` = `PackedVector2Array()`

### CollisionShape2D
*Inherits: **Node2D < CanvasItem < Node < Object***

A node that provides a Shape2D to a CollisionObject2D parent and allows it to be edited. This can give a detection shape to an Area2D or turn a PhysicsBody2D into a solid object.

**Properties**
- `Color DebugColor` = `Color(0, 0, 0, 0)`
- `bool Disabled` = `false`
- `bool OneWayCollision` = `false`
- `float OneWayCollisionMargin` = `1.0`
- `Shape2D Shape`

### DampedSpringJoint2D
*Inherits: **Joint2D < Node2D < CanvasItem < Node < Object***

A physics joint that connects two 2D physics bodies with a spring-like force. This behaves like a spring that always wants to stretch to a given length.

**Properties**
- `float Damping` = `1.0`
- `float Length` = `50.0`
- `float RestLength` = `0.0`
- `float Stiffness` = `20.0`

### GPUParticles2D
*Inherits: **Node2D < CanvasItem < Node < Object***

2D particle node used to create a variety of particle systems and effects. GPUParticles2D features an emitter that generates some number of particles at a given rate.

**Properties**
- `int Amount` = `8`
- `float AmountRatio` = `1.0`
- `float CollisionBaseSize` = `1.0`
- `DrawOrder DrawOrder` = `1`
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
- `Texture2D Texture`
- `bool TrailEnabled` = `false`
- `float TrailLifetime` = `0.3`
- `int TrailSectionSubdivisions` = `4`
- `int TrailSections` = `8`
- `bool UseFixedSeed` = `false`
- `Rect2 VisibilityRect` = `Rect2(-100, -100, 200, 200)`

**Methods**
- `Rect2 CaptureRect()`
- `void ConvertFromParticles(Node particles)`
- `void EmitParticle(Transform2D xform, Vector2 velocity, Color color, Color custom, int flags)`
- `void RequestParticlesProcess(float processTime)`
- `void Restart(bool keepSeed = false)`

### GrooveJoint2D
*Inherits: **Joint2D < Node2D < CanvasItem < Node < Object***

A physics joint that restricts the movement of two 2D physics bodies to a fixed axis. For example, a StaticBody2D representing a piston base can be attached to a RigidBody2D representing the piston head, moving up and down.

**Properties**
- `float InitialOffset` = `25.0`
- `float Length` = `50.0`

### Joint2D
*Inherits: **Node2D < CanvasItem < Node < Object** | Inherited by: DampedSpringJoint2D, GrooveJoint2D, PinJoint2D*

Abstract base class for all joints in 2D physics. 2D joints bind together two physics bodies (node_a and node_b) and apply a constraint.

**Properties**
- `float Bias` = `0.0`
- `bool DisableCollision` = `true`
- `NodePath NodeA` = `NodePath("")`
- `NodePath NodeB` = `NodePath("")`

**Methods**
- `RID GetRid()`

### Light2D
*Inherits: **Node2D < CanvasItem < Node < Object** | Inherited by: DirectionalLight2D, PointLight2D*

Casts light in a 2D environment. A light is defined as a color, an energy value, a mode (see constants), and various other parameters (range and shadows-related).

**Properties**
- `BlendMode BlendMode` = `0`
- `Color Color` = `Color(1, 1, 1, 1)`
- `bool EditorOnly` = `false`
- `bool Enabled` = `true`
- `float Energy` = `1.0`
- `int RangeItemCullMask` = `1`
- `int RangeLayerMax` = `0`
- `int RangeLayerMin` = `0`
- `int RangeZMax` = `1024`
- `int RangeZMin` = `-1024`
- `Color ShadowColor` = `Color(0, 0, 0, 0)`
- `bool ShadowEnabled` = `false`
- `ShadowFilter ShadowFilter` = `0`
- `float ShadowFilterSmooth` = `0.0`
- `int ShadowItemCullMask` = `1`

**Methods**
- `float GetHeight()`
- `void SetHeight(float height)`

### LightOccluder2D
*Inherits: **Node2D < CanvasItem < Node < Object***

Occludes light cast by a Light2D, casting shadows. The LightOccluder2D must be provided with an OccluderPolygon2D in order for the shadow to be computed.

**Properties**
- `OccluderPolygon2D Occluder`
- `int OccluderLightMask` = `1`
- `bool SdfCollision` = `true`

### Line2D
*Inherits: **Node2D < CanvasItem < Node < Object***

This node draws a 2D polyline, i.e. a shape consisting of several points connected by segments. Line2D is not a mathematical polyline, i.e. the segments are not infinitely thin. It is intended for rendering and it can be colored and optionally textured.

**Properties**
- `bool Antialiased` = `false`
- `LineCapMode BeginCapMode` = `0`
- `bool Closed` = `false`
- `Color DefaultColor` = `Color(1, 1, 1, 1)`
- `LineCapMode EndCapMode` = `0`
- `Gradient Gradient`
- `LineJointMode JointMode` = `0`
- `PackedVector2Array Points` = `PackedVector2Array()`
- `int RoundPrecision` = `8`
- `float SharpLimit` = `2.0`
- `Texture2D Texture`
- `LineTextureMode TextureMode` = `0`
- `float Width` = `10.0`
- `Curve WidthCurve`

**Methods**
- `void AddPoint(Vector2 position, int index = -1)`
- `void ClearPoints()`
- `int GetPointCount()`
- `Vector2 GetPointPosition(int index)`
- `void RemovePoint(int index)`
- `void SetPointPosition(int index, Vector2 position)`

### Marker2D
*Inherits: **Node2D < CanvasItem < Node < Object***

Generic 2D position hint for editing. It's just like a plain Node2D, but it displays as a cross in the 2D editor at all times. You can set the cross' visual size by using the gizmo in the 2D editor while the node is selected.

**Properties**
- `float GizmoExtents` = `10.0`

### MeshInstance2D
*Inherits: **Node2D < CanvasItem < Node < Object***

Node used for displaying a Mesh in 2D. This can be faster to render compared to displaying a Sprite2D node with large transparent areas, especially if the node takes up a lot of space on screen at high viewport resolutions. This is because using a mesh designed to fit the sprite's opaque areas will reduce GPU fill rate utilization (at the cost of increased vertex processing utilization).

**Properties**
- `Mesh Mesh`
- `Texture2D Texture`

### MultiMeshInstance2D
*Inherits: **Node2D < CanvasItem < Node < Object***

MultiMeshInstance2D is a specialized node to instance a MultiMesh resource in 2D. This can be faster to render compared to displaying many Sprite2D nodes with large transparent areas, especially if the nodes take up a lot of space on screen at high viewport resolutions. This is because using a mesh designed to fit the sprites' opaque areas will reduce GPU fill rate utilization (at the cost of increased vertex processing utilization).

**Properties**
- `MultiMesh Multimesh`
- `Texture2D Texture`

### NavigationAgent2D
*Inherits: **Node < Object***

A 2D agent used to pathfind to a position while avoiding static and dynamic obstacles. The calculation can be used by the parent node to dynamically move it along the path. Requires navigation data to work correctly.

**Properties**
- `bool AvoidanceEnabled` = `false`
- `int AvoidanceLayers` = `1`
- `int AvoidanceMask` = `1`
- `float AvoidancePriority` = `1.0`
- `bool DebugEnabled` = `false`
- `Color DebugPathCustomColor` = `Color(1, 1, 1, 1)`
- `float DebugPathCustomLineWidth` = `-1.0`
- `float DebugPathCustomPointSize` = `4.0`
- `bool DebugUseCustom` = `false`
- `int MaxNeighbors` = `10`
- `float MaxSpeed` = `100.0`
- `int NavigationLayers` = `1`
- `float NeighborDistance` = `500.0`
- `float PathDesiredDistance` = `20.0`
- `float PathMaxDistance` = `100.0`
- `BitField[PathMetadataFlags] PathMetadataFlags` = `7`
- `PathPostProcessing PathPostprocessing` = `0`
- `float PathReturnMaxLength` = `0.0`
- `float PathReturnMaxRadius` = `0.0`
- `float PathSearchMaxDistance` = `0.0`
- `int PathSearchMaxPolygons` = `4096`
- `PathfindingAlgorithm PathfindingAlgorithm` = `0`
- `float Radius` = `10.0`
- `float SimplifyEpsilon` = `0.0`
- `bool SimplifyPath` = `false`
- `float TargetDesiredDistance` = `10.0`
- `Vector2 TargetPosition` = `Vector2(0, 0)`
- `float TimeHorizonAgents` = `1.0`
- `float TimeHorizonObstacles` = `0.0`
- `Vector2 Velocity` = `Vector2(0, 0)`

**Methods**
- `float DistanceToTarget()`
- `bool GetAvoidanceLayerValue(int layerNumber)`
- `bool GetAvoidanceMaskValue(int maskNumber)`
- `PackedVector2Array GetCurrentNavigationPath()`
- `int GetCurrentNavigationPathIndex()`
- `NavigationPathQueryResult2D GetCurrentNavigationResult()`
- `Vector2 GetFinalPosition()`
- `bool GetNavigationLayerValue(int layerNumber)`
- `RID GetNavigationMap()`
- `Vector2 GetNextPathPosition()`
- `float GetPathLength()`
- `RID GetRid()`
- `bool IsNavigationFinished()`
- `bool IsTargetReachable()`
- `bool IsTargetReached()`
- `void SetAvoidanceLayerValue(int layerNumber, bool value)`
- `void SetAvoidanceMaskValue(int maskNumber, bool value)`
- `void SetNavigationLayerValue(int layerNumber, bool value)`
- `void SetNavigationMap(RID navigationMap)`
- `void SetVelocityForced(Vector2 velocity)`

### NavigationLink2D
*Inherits: **Node2D < CanvasItem < Node < Object***

A link between two positions on NavigationRegion2Ds that agents can be routed through. These positions can be on the same NavigationRegion2D or on two different ones. Links are useful to express navigation methods other than traveling along the surface of the navigation polygon, such as ziplines, teleporters, or gaps that can be jumped across.

**Properties**
- `bool Bidirectional` = `true`
- `bool Enabled` = `true`
- `Vector2 EndPosition` = `Vector2(0, 0)`
- `float EnterCost` = `0.0`
- `int NavigationLayers` = `1`
- `Vector2 StartPosition` = `Vector2(0, 0)`
- `float TravelCost` = `1.0`

**Methods**
- `Vector2 GetGlobalEndPosition()`
- `Vector2 GetGlobalStartPosition()`
- `bool GetNavigationLayerValue(int layerNumber)`
- `RID GetNavigationMap()`
- `RID GetRid()`
- `void SetGlobalEndPosition(Vector2 position)`
- `void SetGlobalStartPosition(Vector2 position)`
- `void SetNavigationLayerValue(int layerNumber, bool value)`
- `void SetNavigationMap(RID navigationMap)`

### NavigationObstacle2D
*Inherits: **Node2D < CanvasItem < Node < Object***

An obstacle needs a navigation map and outline vertices defined to work correctly. The outlines can not cross or overlap.

**Properties**
- `bool AffectNavigationMesh` = `false`
- `bool AvoidanceEnabled` = `true`
- `int AvoidanceLayers` = `1`
- `bool CarveNavigationMesh` = `false`
- `float Radius` = `0.0`
- `Vector2 Velocity` = `Vector2(0, 0)`
- `PackedVector2Array Vertices` = `PackedVector2Array()`

**Methods**
- `bool GetAvoidanceLayerValue(int layerNumber)`
- `RID GetNavigationMap()`
- `RID GetRid()`
- `void SetAvoidanceLayerValue(int layerNumber, bool value)`
- `void SetNavigationMap(RID navigationMap)`

### NavigationRegion2D
*Inherits: **Node2D < CanvasItem < Node < Object***

A traversable 2D region based on a NavigationPolygon that NavigationAgent2Ds can use for pathfinding.

**Properties**
- `bool Enabled` = `true`
- `float EnterCost` = `0.0`
- `int NavigationLayers` = `1`
- `NavigationPolygon NavigationPolygon`
- `float TravelCost` = `1.0`
- `bool UseEdgeConnections` = `true`

**Methods**
- `void BakeNavigationPolygon(bool onThread = true)`
- `Rect2 GetBounds()`
- `bool GetNavigationLayerValue(int layerNumber)`
- `RID GetNavigationMap()`
- `RID GetRegionRid()`
- `RID GetRid()`
- `bool IsBaking()`
- `void SetNavigationLayerValue(int layerNumber, bool value)`
- `void SetNavigationMap(RID navigationMap)`

### Node2D
*Inherits: **CanvasItem < Node < Object** | Inherited by: AnimatedSprite2D, AudioListener2D, AudioStreamPlayer2D, BackBufferCopy, Bone2D, Camera2D, ...*

A 2D game object, with a transform (position, rotation, and scale). All 2D nodes, including physics objects and sprites, inherit from Node2D. Use Node2D as a parent node to move, scale and rotate children in a 2D project. Also gives control of the node's render order.

**Properties**
- `Vector2 GlobalPosition`
- `float GlobalRotation`
- `float GlobalRotationDegrees`
- `Vector2 GlobalScale`
- `float GlobalSkew`
- `Transform2D GlobalTransform`
- `Vector2 Position` = `Vector2(0, 0)`
- `float Rotation` = `0.0`
- `float RotationDegrees`
- `Vector2 Scale` = `Vector2(1, 1)`
- `float Skew` = `0.0`
- `Transform2D Transform`

**Methods**
- `void ApplyScale(Vector2 ratio)`
- `float GetAngleTo(Vector2 point)`
- `Transform2D GetRelativeTransformToParent(Node parent)`
- `void GlobalTranslate(Vector2 offset)`
- `void LookAt(Vector2 point)`
- `void MoveLocalX(float delta, bool scaled = false)`
- `void MoveLocalY(float delta, bool scaled = false)`
- `void Rotate(float radians)`
- `Vector2 ToGlobal(Vector2 localPoint)`
- `Vector2 ToLocal(Vector2 globalPoint)`
- `void Translate(Vector2 offset)`

### Path2D
*Inherits: **Node2D < CanvasItem < Node < Object***

Can have PathFollow2D child nodes moving along the Curve2D. See PathFollow2D for more information on usage.

**Properties**
- `Curve2D Curve`

### PathFollow2D
*Inherits: **Node2D < CanvasItem < Node < Object***

This node takes its parent Path2D, and returns the coordinates of a point within it, given a distance from the first vertex.

**Properties**
- `bool CubicInterp` = `true`
- `float HOffset` = `0.0`
- `bool Loop` = `true`
- `float Progress` = `0.0`
- `float ProgressRatio` = `0.0`
- `bool Rotates` = `true`
- `float VOffset` = `0.0`

### PinJoint2D
*Inherits: **Joint2D < Node2D < CanvasItem < Node < Object***

A physics joint that attaches two 2D physics bodies at a single point, allowing them to freely rotate. For example, a RigidBody2D can be attached to a StaticBody2D to create a pendulum or a seesaw.

**Properties**
- `bool AngularLimitEnabled` = `false`
- `float AngularLimitLower` = `0.0`
- `float AngularLimitUpper` = `0.0`
- `bool MotorEnabled` = `false`
- `float MotorTargetVelocity` = `0.0`
- `float Softness` = `0.0`

### Polygon2D
*Inherits: **Node2D < CanvasItem < Node < Object***

A Polygon2D is defined by a set of points. Each point is connected to the next, with the final point being connected to the first, resulting in a closed polygon. Polygon2Ds can be filled with color (solid or gradient) or filled with a given texture.

**Properties**
- `bool Antialiased` = `false`
- `Color Color` = `Color(1, 1, 1, 1)`
- `int InternalVertexCount` = `0`
- `float InvertBorder` = `100.0`
- `bool InvertEnabled` = `false`
- `Vector2 Offset` = `Vector2(0, 0)`
- `PackedVector2Array Polygon` = `PackedVector2Array()`
- `Godot.Collections.Array Polygons` = `[]`
- `NodePath Skeleton` = `NodePath("")`
- `Texture2D Texture`
- `Vector2 TextureOffset` = `Vector2(0, 0)`
- `float TextureRotation` = `0.0`
- `Vector2 TextureScale` = `Vector2(1, 1)`
- `PackedVector2Array Uv` = `PackedVector2Array()`
- `PackedColorArray VertexColors` = `PackedColorArray()`

**Methods**
- `void AddBone(NodePath path, PackedFloat32Array weights)`
- `void ClearBones()`
- `void EraseBone(int index)`
- `int GetBoneCount()`
- `NodePath GetBonePath(int index)`
- `PackedFloat32Array GetBoneWeights(int index)`
- `void SetBonePath(int index, NodePath path)`
- `void SetBoneWeights(int index, PackedFloat32Array weights)`

### RayCast2D
*Inherits: **Node2D < CanvasItem < Node < Object***

A raycast represents a ray from its origin to its target_position that finds the closest object along its path, if it intersects any.

**Properties**
- `bool CollideWithAreas` = `false`
- `bool CollideWithBodies` = `true`
- `int CollisionMask` = `1`
- `bool Enabled` = `true`
- `bool ExcludeParent` = `true`
- `bool HitFromInside` = `false`
- `Vector2 TargetPosition` = `Vector2(0, 50)`

**Methods**
- `void AddException(CollisionObject2D node)`
- `void AddExceptionRid(RID rid)`
- `void ClearExceptions()`
- `void ForceRaycastUpdate()`
- `Object GetCollider()`
- `RID GetColliderRid()`
- `int GetColliderShape()`
- `bool GetCollisionMaskValue(int layerNumber)`
- `Vector2 GetCollisionNormal()`
- `Vector2 GetCollisionPoint()`
- `bool IsColliding()`
- `void RemoveException(CollisionObject2D node)`
- `void RemoveExceptionRid(RID rid)`
- `void SetCollisionMaskValue(int layerNumber, bool value)`

**C# Examples**
```csharp
var target = (CollisionObject2D)GetCollider(); // A CollisionObject2D.
var shapeId = GetColliderShape(); // The shape index in the collider.
var ownerId = target.ShapeFindOwner(shapeId); // The owner ID in the collider.
var shape = target.ShapeOwnerGetOwner(ownerId);
```

### RemoteTransform2D
*Inherits: **Node2D < CanvasItem < Node < Object***

RemoteTransform2D pushes its own Transform2D to another Node2D derived node (called the remote node) in the scene.

**Properties**
- `NodePath RemotePath` = `NodePath("")`
- `bool UpdatePosition` = `true`
- `bool UpdateRotation` = `true`
- `bool UpdateScale` = `true`
- `bool UseGlobalCoordinates` = `true`

**Methods**
- `void ForceUpdateCache()`

### RigidBody2D
*Inherits: **PhysicsBody2D < CollisionObject2D < Node2D < CanvasItem < Node < Object** | Inherited by: PhysicalBone2D*

RigidBody2D implements full 2D physics. It cannot be controlled directly, instead, you must apply forces to it (gravity, impulses, etc.), and the physics simulation will calculate the resulting movement, rotation, react to collisions, and affect other physics bodies in its path.

**Properties**
- `float AngularDamp` = `0.0`
- `DampMode AngularDampMode` = `0`
- `float AngularVelocity` = `0.0`
- `bool CanSleep` = `true`
- `Vector2 CenterOfMass` = `Vector2(0, 0)`
- `CenterOfMassMode CenterOfMassMode` = `0`
- `Vector2 ConstantForce` = `Vector2(0, 0)`
- `float ConstantTorque` = `0.0`
- `bool ContactMonitor` = `false`
- `CCDMode ContinuousCd` = `0`
- `bool CustomIntegrator` = `false`
- `bool Freeze` = `false`
- `FreezeMode FreezeMode` = `0`
- `float GravityScale` = `1.0`
- `float Inertia` = `0.0`
- `float LinearDamp` = `0.0`
- `DampMode LinearDampMode` = `0`
- `Vector2 LinearVelocity` = `Vector2(0, 0)`
- `bool LockRotation` = `false`
- `float Mass` = `1.0`
- `int MaxContactsReported` = `0`
- `PhysicsMaterial PhysicsMaterialOverride`
- `bool Sleeping` = `false`

**Methods**
- `void _IntegrateForces(PhysicsDirectBodyState2D state) [virtual]`
- `void AddConstantCentralForce(Vector2 force)`
- `void AddConstantForce(Vector2 force, Vector2 position = Vector2(0, 0))`
- `void AddConstantTorque(float torque)`
- `void ApplyCentralForce(Vector2 force)`
- `void ApplyCentralImpulse(Vector2 impulse = Vector2(0, 0))`
- `void ApplyForce(Vector2 force, Vector2 position = Vector2(0, 0))`
- `void ApplyImpulse(Vector2 impulse, Vector2 position = Vector2(0, 0))`
- `void ApplyTorque(float torque)`
- `void ApplyTorqueImpulse(float torque)`
- `Array[Node2D] GetCollidingBodies()`
- `int GetContactCount()`
- `void SetAxisVelocity(Vector2 axisVelocity)`

**C# Examples**
```csharp
private RigidBody2D _ball;

public override void _Ready()
{
    _ball = GetNode<RigidBody2D>("Ball");
}

private float GetBallInertia()
{
    return 1.0f / PhysicsServer2D.BodyGetDirectState(_ball.GetRid()).InverseInertia;
}
```

### Skeleton2D
*Inherits: **Node2D < CanvasItem < Node < Object***

Skeleton2D parents a hierarchy of Bone2D nodes. It holds a reference to each Bone2D's rest pose and acts as a single point of access to its bones.

**Methods**
- `void ExecuteModifications(float delta, int executionMode)`
- `Bone2D GetBone(int idx)`
- `int GetBoneCount()`
- `Transform2D GetBoneLocalPoseOverride(int boneIdx)`
- `SkeletonModificationStack2D GetModificationStack()`
- `RID GetSkeleton()`
- `void SetBoneLocalPoseOverride(int boneIdx, Transform2D overridePose, float strength, bool persistent)`
- `void SetModificationStack(SkeletonModificationStack2D modificationStack)`

### Sprite2D
*Inherits: **Node2D < CanvasItem < Node < Object***

A node that displays a 2D texture. The texture displayed can be a region from a larger atlas texture, or a frame from a sprite sheet animation.

**Properties**
- `bool Centered` = `true`
- `bool FlipH` = `false`
- `bool FlipV` = `false`
- `int Frame` = `0`
- `Vector2i FrameCoords` = `Vector2i(0, 0)`
- `int Hframes` = `1`
- `Vector2 Offset` = `Vector2(0, 0)`
- `bool RegionEnabled` = `false`
- `bool RegionFilterClipEnabled` = `false`
- `Rect2 RegionRect` = `Rect2(0, 0, 0, 0)`
- `Texture2D Texture`
- `int Vframes` = `1`

**Methods**
- `Rect2 GetRect()`
- `bool IsPixelOpaque(Vector2 pos)`

**C# Examples**
```csharp
public override void _Input(InputEvent @event)
{
    if (@event is InputEventMouseButton inputEventMouse)
    {
        if (inputEventMouse.Pressed && inputEventMouse.ButtonIndex == MouseButton.Left)
        {
            if (GetRect().HasPoint(ToLocal(inputEventMouse.Position)))
            {
                GD.Print("A click!");
            }
        }
    }
}
```

### StaticBody2D
*Inherits: **PhysicsBody2D < CollisionObject2D < Node2D < CanvasItem < Node < Object** | Inherited by: AnimatableBody2D*

A static 2D physics body. It can't be moved by external forces or contacts, but can be moved manually by other means such as code, AnimationMixers (with AnimationMixer.callback_mode_process set to AnimationMixer.ANIMATION_CALLBACK_MODE_PROCESS_PHYSICS), and RemoteTransform2D.

**Properties**
- `float ConstantAngularVelocity` = `0.0`
- `Vector2 ConstantLinearVelocity` = `Vector2(0, 0)`
- `PhysicsMaterial PhysicsMaterialOverride`

### TileMapLayer
*Inherits: **Node2D < CanvasItem < Node < Object***

Node for 2D tile-based maps. A TileMapLayer uses a TileSet which contain a list of tiles which are used to create grid-based maps. Unlike the TileMap node, which is deprecated, TileMapLayer has only one layer of tiles. You can use several TileMapLayer to achieve the same result as a TileMap node.

**Properties**
- `bool CollisionEnabled` = `true`
- `DebugVisibilityMode CollisionVisibilityMode` = `0`
- `bool Enabled` = `true`
- `bool NavigationEnabled` = `true`
- `DebugVisibilityMode NavigationVisibilityMode` = `0`
- `bool OcclusionEnabled` = `true`
- `int PhysicsQuadrantSize` = `16`
- `int RenderingQuadrantSize` = `16`
- `PackedByteArray TileMapData` = `PackedByteArray()`
- `TileSet TileSet`
- `bool UseKinematicBodies` = `false`
- `bool XDrawOrderReversed` = `false`
- `int YSortOrigin` = `0`

**Methods**
- `void _TileDataRuntimeUpdate(Vector2i coords, TileData tileData) [virtual]`
- `void _UpdateCells(Array[Vector2i] coords, bool forcedCleanup) [virtual]`
- `bool _UseTileDataRuntimeUpdate(Vector2i coords) [virtual]`
- `void Clear()`
- `void EraseCell(Vector2i coords)`
- `void FixInvalidTiles()`
- `int GetCellAlternativeTile(Vector2i coords)`
- `Vector2i GetCellAtlasCoords(Vector2i coords)`
- `int GetCellSourceId(Vector2i coords)`
- `TileData GetCellTileData(Vector2i coords)`
- `Vector2i GetCoordsForBodyRid(RID body)`
- `RID GetNavigationMap()`
- `Vector2i GetNeighborCell(Vector2i coords, CellNeighbor neighbor)`
- `TileMapPattern GetPattern(Array[Vector2i] coordsArray)`
- `Array[Vector2i] GetSurroundingCells(Vector2i coords)`
- `Array[Vector2i] GetUsedCells()`
- `Array[Vector2i] GetUsedCellsById(int sourceId = -1, Vector2i atlasCoords = Vector2i(-1, -1), int alternativeTile = -1)`
- `Rect2i GetUsedRect()`
- `bool HasBodyRid(RID body)`
- `bool IsCellFlippedH(Vector2i coords)`
- `bool IsCellFlippedV(Vector2i coords)`
- `bool IsCellTransposed(Vector2i coords)`
- `Vector2i LocalToMap(Vector2 localPosition)`
- `Vector2i MapPattern(Vector2i positionInTilemap, Vector2i coordsInPattern, TileMapPattern pattern)`
- `Vector2 MapToLocal(Vector2i mapPosition)`
- `void NotifyRuntimeTileDataUpdate()`
- `void SetCell(Vector2i coords, int sourceId = -1, Vector2i atlasCoords = Vector2i(-1, -1), int alternativeTile = 0)`
- `void SetCellsTerrainConnect(Array[Vector2i] cells, int terrainSet, int terrain, bool ignoreEmptyTerrains = true)`
- `void SetCellsTerrainPath(Array[Vector2i] path, int terrainSet, int terrain, bool ignoreEmptyTerrains = true)`
- `void SetNavigationMap(RID map)`
- `void SetPattern(Vector2i position, TileMapPattern pattern)`
- `void UpdateInternals()`

### TileMapPattern
*Inherits: **Resource < RefCounted < Object***

This resource holds a set of cells to help bulk manipulations of TileMap.

**Methods**
- `int GetCellAlternativeTile(Vector2i coords)`
- `Vector2i GetCellAtlasCoords(Vector2i coords)`
- `int GetCellSourceId(Vector2i coords)`
- `Vector2i GetSize()`
- `Array[Vector2i] GetUsedCells()`
- `bool HasCell(Vector2i coords)`
- `bool IsEmpty()`
- `void RemoveCell(Vector2i coords, bool updateSize)`
- `void SetCell(Vector2i coords, int sourceId = -1, Vector2i atlasCoords = Vector2i(-1, -1), int alternativeTile = -1)`
- `void SetSize(Vector2i size)`

### TileMap
*Inherits: **Node2D < CanvasItem < Node < Object***

Node for 2D tile-based maps. Tilemaps use a TileSet which contain a list of tiles which are used to create grid-based maps. A TileMap may have several layers, layouting tiles on top of each other.

**Properties**
- `bool CollisionAnimatable` = `false`
- `VisibilityMode CollisionVisibilityMode` = `0`
- `VisibilityMode NavigationVisibilityMode` = `0`
- `int RenderingQuadrantSize` = `16`
- `TileSet TileSet`

**Methods**
- `void _TileDataRuntimeUpdate(int layer, Vector2i coords, TileData tileData) [virtual]`
- `bool _UseTileDataRuntimeUpdate(int layer, Vector2i coords) [virtual]`
- `void AddLayer(int toPosition)`
- `void Clear()`
- `void ClearLayer(int layer)`
- `void EraseCell(int layer, Vector2i coords)`
- `void FixInvalidTiles()`
- `void ForceUpdate(int layer = -1)`
- `int GetCellAlternativeTile(int layer, Vector2i coords, bool useProxies = false)`
- `Vector2i GetCellAtlasCoords(int layer, Vector2i coords, bool useProxies = false)`
- `int GetCellSourceId(int layer, Vector2i coords, bool useProxies = false)`
- `TileData GetCellTileData(int layer, Vector2i coords, bool useProxies = false)`
- `Vector2i GetCoordsForBodyRid(RID body)`
- `int GetLayerForBodyRid(RID body)`
- `Color GetLayerModulate(int layer)`
- `string GetLayerName(int layer)`
- `RID GetLayerNavigationMap(int layer)`
- `int GetLayerYSortOrigin(int layer)`
- `int GetLayerZIndex(int layer)`
- `int GetLayersCount()`
- `RID GetNavigationMap(int layer)`
- `Vector2i GetNeighborCell(Vector2i coords, CellNeighbor neighbor)`
- `TileMapPattern GetPattern(int layer, Array[Vector2i] coordsArray)`
- `Array[Vector2i] GetSurroundingCells(Vector2i coords)`
- `Array[Vector2i] GetUsedCells(int layer)`
- `Array[Vector2i] GetUsedCellsById(int layer, int sourceId = -1, Vector2i atlasCoords = Vector2i(-1, -1), int alternativeTile = -1)`
- `Rect2i GetUsedRect()`
- `bool IsCellFlippedH(int layer, Vector2i coords, bool useProxies = false)`
- `bool IsCellFlippedV(int layer, Vector2i coords, bool useProxies = false)`
- `bool IsCellTransposed(int layer, Vector2i coords, bool useProxies = false)`
- `bool IsLayerEnabled(int layer)`
- `bool IsLayerNavigationEnabled(int layer)`
- `bool IsLayerYSortEnabled(int layer)`
- `Vector2i LocalToMap(Vector2 localPosition)`
- `Vector2i MapPattern(Vector2i positionInTilemap, Vector2i coordsInPattern, TileMapPattern pattern)`
- `Vector2 MapToLocal(Vector2i mapPosition)`
- `void MoveLayer(int layer, int toPosition)`
- `void NotifyRuntimeTileDataUpdate(int layer = -1)`
- `void RemoveLayer(int layer)`
- `void SetCell(int layer, Vector2i coords, int sourceId = -1, Vector2i atlasCoords = Vector2i(-1, -1), int alternativeTile = 0)`

### TouchScreenButton
*Inherits: **Node2D < CanvasItem < Node < Object***

TouchScreenButton allows you to create on-screen buttons for touch devices. It's intended for gameplay use, such as a unit you have to touch to move. Unlike Button, TouchScreenButton supports multitouch out of the box. Several TouchScreenButtons can be pressed at the same time with touch input.

**Properties**
- `string Action` = `""`
- `BitMap Bitmask`
- `bool PassbyPress` = `false`
- `Shape2D Shape`
- `bool ShapeCentered` = `true`
- `bool ShapeVisible` = `true`
- `Texture2D TextureNormal`
- `Texture2D TexturePressed`
- `VisibilityMode VisibilityMode` = `0`

**Methods**
- `bool IsPressed()`

### VisibleOnScreenEnabler2D
*Inherits: **VisibleOnScreenNotifier2D < Node2D < CanvasItem < Node < Object***

VisibleOnScreenEnabler2D contains a rectangular region of 2D space and a target node. The target node will be automatically enabled (via its Node.process_mode property) when any part of this region becomes visible on the screen, and automatically disabled otherwise. This can for example be used to activate enemies only when the player approaches them.

**Properties**
- `EnableMode EnableMode` = `0`
- `NodePath EnableNodePath` = `NodePath("..")`

### VisibleOnScreenNotifier2D
*Inherits: **Node2D < CanvasItem < Node < Object** | Inherited by: VisibleOnScreenEnabler2D*

VisibleOnScreenNotifier2D represents a rectangular region of 2D space. When any part of this region becomes visible on screen or in a viewport, it will emit a screen_entered signal, and likewise it will emit a screen_exited signal when no part of it remains visible.

**Properties**
- `Rect2 Rect` = `Rect2(-10, -10, 20, 20)`
- `bool ShowRect` = `true`

**Methods**
- `bool IsOnScreen()`
