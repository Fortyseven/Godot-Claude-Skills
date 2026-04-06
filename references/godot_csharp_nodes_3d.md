# Godot 4 C# API Reference — Nodes 3D

> C#-only reference. 39 classes.

### AnimatableBody3D
*Inherits: **StaticBody3D < PhysicsBody3D < CollisionObject3D < Node3D < Node < Object***

An animatable 3D physics body. It can't be moved by external forces or contacts, but can be moved manually by other means such as code, AnimationMixers (with AnimationMixer.callback_mode_process set to AnimationMixer.ANIMATION_CALLBACK_MODE_PROCESS_PHYSICS), and RemoteTransform3D.

**Properties**
- `bool SyncToPhysics` = `true`

### BoneAttachment3D
*Inherits: **Node3D < Node < Object***

This node selects a bone in a Skeleton3D and attaches to it. This means that the BoneAttachment3D node will either dynamically copy or override the 3D transform of the selected bone.

**Properties**
- `int BoneIdx` = `-1`
- `string BoneName` = `""`
- `NodePath ExternalSkeleton`
- `bool OverridePose` = `false`
- `PhysicsInterpolationMode PhysicsInterpolationMode` = `2 (overrides Node)`
- `bool UseExternalSkeleton` = `false`

**Methods**
- `Skeleton3D GetSkeleton()`
- `void OnSkeletonUpdate()`

### Camera3D
*Inherits: **Node3D < Node < Object** | Inherited by: XRCamera3D*

Camera3D is a special node that displays what is visible from its current location. Cameras register themselves in the nearest Viewport node (when ascending the tree). Only one camera can be active per viewport. If no viewport is available ascending the tree, the camera will register in the global viewport. In other words, a camera just provides 3D display capabilities to a Viewport, and, without one, a scene registered in that Viewport (or higher viewports) can't be displayed.

**Properties**
- `CameraAttributes Attributes`
- `Compositor Compositor`
- `int CullMask` = `1048575`
- `bool Current` = `false`
- `DopplerTracking DopplerTracking` = `0`
- `Environment Environment`
- `float Far` = `4000.0`
- `float Fov` = `75.0`
- `Vector2 FrustumOffset` = `Vector2(0, 0)`
- `float HOffset` = `0.0`
- `KeepAspect KeepAspect` = `1`
- `float Near` = `0.05`
- `ProjectionType Projection` = `0`
- `float Size` = `1.0`
- `float VOffset` = `0.0`

**Methods**
- `void ClearCurrent(bool enableNext = true)`
- `Projection GetCameraProjection()`
- `RID GetCameraRid()`
- `Transform3D GetCameraTransform()`
- `bool GetCullMaskValue(int layerNumber)`
- `Array[Plane] GetFrustum()`
- `RID GetPyramidShapeRid()`
- `bool IsPositionBehind(Vector3 worldPoint)`
- `bool IsPositionInFrustum(Vector3 worldPoint)`
- `void MakeCurrent()`
- `Vector3 ProjectLocalRayNormal(Vector2 screenPoint)`
- `Vector3 ProjectPosition(Vector2 screenPoint, float zDepth)`
- `Vector3 ProjectRayNormal(Vector2 screenPoint)`
- `Vector3 ProjectRayOrigin(Vector2 screenPoint)`
- `void SetCullMaskValue(int layerNumber, bool value)`
- `void SetFrustum(float size, Vector2 offset, float zNear, float zFar)`
- `void SetOrthogonal(float size, float zNear, float zFar)`
- `void SetPerspective(float fov, float zNear, float zFar)`
- `Vector2 UnprojectPosition(Vector3 worldPoint)`

### CharacterBody3D
*Inherits: **PhysicsBody3D < CollisionObject3D < Node3D < Node < Object***

CharacterBody3D is a specialized class for physics bodies that are meant to be user-controlled. They are not affected by physics at all, but they affect other physics bodies in their path. They are mainly used to provide high-level API to move objects with wall and slope detection (move_and_slide() method) in addition to the general collision detection provided by PhysicsBody3D.move_and_collide(). This makes it useful for highly configurable physics bodies that must move in specific ways and collide with the world, as is often the case with user-controlled characters.

**Properties**
- `bool FloorBlockOnWall` = `true`
- `bool FloorConstantSpeed` = `false`
- `float FloorMaxAngle` = `0.7853982`
- `float FloorSnapLength` = `0.1`
- `bool FloorStopOnSlope` = `true`
- `int MaxSlides` = `6`
- `MotionMode MotionMode` = `0`
- `int PlatformFloorLayers` = `4294967295`
- `PlatformOnLeave PlatformOnLeave` = `0`
- `int PlatformWallLayers` = `0`
- `float SafeMargin` = `0.001`
- `bool SlideOnCeiling` = `true`
- `Vector3 UpDirection` = `Vector3(0, 1, 0)`
- `Vector3 Velocity` = `Vector3(0, 0, 0)`
- `float WallMinSlideAngle` = `0.2617994`

**Methods**
- `void ApplyFloorSnap()`
- `float GetFloorAngle(Vector3 upDirection = Vector3(0, 1, 0))`
- `Vector3 GetFloorNormal()`
- `Vector3 GetLastMotion()`
- `KinematicCollision3D GetLastSlideCollision()`
- `Vector3 GetPlatformAngularVelocity()`
- `Vector3 GetPlatformVelocity()`
- `Vector3 GetPositionDelta()`
- `Vector3 GetRealVelocity()`
- `KinematicCollision3D GetSlideCollision(int slideIdx)`
- `int GetSlideCollisionCount()`
- `Vector3 GetWallNormal()`
- `bool IsOnCeiling()`
- `bool IsOnCeilingOnly()`
- `bool IsOnFloor()`
- `bool IsOnFloorOnly()`
- `bool IsOnWall()`
- `bool IsOnWallOnly()`
- `bool MoveAndSlide()`

### DirectionalLight3D
*Inherits: **Light3D < VisualInstance3D < Node3D < Node < Object***

A directional light is a type of Light3D node that models an infinite number of parallel rays covering the entire scene. It is used for lights with strong intensity that are located far away from the scene to model sunlight or moonlight.

**Properties**
- `bool DirectionalShadowBlendSplits` = `false`
- `float DirectionalShadowFadeStart` = `0.8`
- `float DirectionalShadowMaxDistance` = `100.0`
- `ShadowMode DirectionalShadowMode` = `2`
- `float DirectionalShadowPancakeSize` = `20.0`
- `float DirectionalShadowSplit1` = `0.1`
- `float DirectionalShadowSplit2` = `0.2`
- `float DirectionalShadowSplit3` = `0.5`
- `SkyMode SkyMode` = `0`

### FogVolume
*Inherits: **VisualInstance3D < Node3D < Node < Object***

FogVolumes are used to add localized fog into the global volumetric fog effect. FogVolumes can also remove volumetric fog from specific areas if using a FogMaterial with a negative FogMaterial.density.

**Properties**
- `Material Material`
- `FogVolumeShape Shape` = `3`
- `Vector3 Size` = `Vector3(2, 2, 2)`

### GeometryInstance3D
*Inherits: **VisualInstance3D < Node3D < Node < Object** | Inherited by: CPUParticles3D, CSGShape3D, GPUParticles3D, Label3D, MeshInstance3D, MultiMeshInstance3D, ...*

Base node for geometry-based visual instances. Shares some common functionality like visibility and custom materials.

**Properties**
- `ShadowCastingSetting CastShadow` = `1`
- `AABB CustomAabb` = `AABB(0, 0, 0, 0, 0, 0)`
- `float ExtraCullMargin` = `0.0`
- `LightmapScale GiLightmapScale` = `0`
- `float GiLightmapTexelScale` = `1.0`
- `GIMode GiMode` = `1`
- `bool IgnoreOcclusionCulling` = `false`
- `float LodBias` = `1.0`
- `Material MaterialOverlay`
- `Material MaterialOverride`
- `float Transparency` = `0.0`
- `float VisibilityRangeBegin` = `0.0`
- `float VisibilityRangeBeginMargin` = `0.0`
- `float VisibilityRangeEnd` = `0.0`
- `float VisibilityRangeEndMargin` = `0.0`
- `VisibilityRangeFadeMode VisibilityRangeFadeMode` = `0`

**Methods**
- `Variant GetInstanceShaderParameter(StringName name)`
- `void SetInstanceShaderParameter(StringName name, Variant value)`

### Light3D
*Inherits: **VisualInstance3D < Node3D < Node < Object** | Inherited by: DirectionalLight3D, OmniLight3D, SpotLight3D*

Light3D is the abstract base class for light nodes. As it can't be instantiated, it shouldn't be used directly. Other types of light nodes inherit from it. Light3D contains the common variables and parameters used for lighting.

**Properties**
- `float DistanceFadeBegin` = `40.0`
- `bool DistanceFadeEnabled` = `false`
- `float DistanceFadeLength` = `10.0`
- `float DistanceFadeShadow` = `50.0`
- `bool EditorOnly` = `false`
- `float LightAngularDistance` = `0.0`
- `BakeMode LightBakeMode` = `2`
- `Color LightColor` = `Color(1, 1, 1, 1)`
- `int LightCullMask` = `4294967295`
- `float LightEnergy` = `1.0`
- `float LightIndirectEnergy` = `1.0`
- `float LightIntensityLumens`
- `float LightIntensityLux`
- `bool LightNegative` = `false`
- `Texture2D LightProjector`
- `float LightSize` = `0.0`
- `float LightSpecular` = `1.0`
- `float LightTemperature`
- `float LightVolumetricFogEnergy` = `1.0`
- `float ShadowBias` = `0.1`
- `float ShadowBlur` = `1.0`
- `int ShadowCasterMask` = `4294967295`
- `bool ShadowEnabled` = `false`
- `float ShadowNormalBias` = `2.0`
- `float ShadowOpacity` = `1.0`
- `bool ShadowReverseCullFace` = `false`
- `float ShadowTransmittanceBias` = `0.05`

**Methods**
- `Color GetCorrelatedColor()`
- `float GetParam(Param param)`
- `void SetParam(Param param, float value)`

### LightmapGIData
*Inherits: **Resource < RefCounted < Object***

LightmapGIData contains baked lightmap and dynamic object probe data for LightmapGI. It is replaced every time lightmaps are baked in LightmapGI.

**Properties**
- `TextureLayered LightTexture`
- `Array[TextureLayered] LightmapTextures` = `[]`
- `Array[TextureLayered] ShadowmaskTextures` = `[]`

**Methods**
- `void AddUser(NodePath path, Rect2 uvScale, int sliceIndex, int subInstance)`
- `void ClearUsers()`
- `int GetUserCount()`
- `NodePath GetUserPath(int userIdx)`
- `bool IsUsingSphericalHarmonics()`
- `void SetUsesSphericalHarmonics(bool usesSphericalHarmonics)`

### LightmapGI
*Inherits: **VisualInstance3D < Node3D < Node < Object***

The LightmapGI node is used to compute and store baked lightmaps. Lightmaps are used to provide high-quality indirect lighting with very little light leaking. LightmapGI can also provide rough reflections using spherical harmonics if directional is enabled. Dynamic objects can receive indirect lighting thanks to light probes, which can be automatically placed by setting generate_probes_subdiv to a value other than GENERATE_PROBES_DISABLED. Additional lightmap probes can also be added by creating LightmapProbe nodes. The downside is that lightmaps are fully static and cannot be baked in an exported project. Baking a LightmapGI node is also slower compared to VoxelGI.

**Properties**
- `float Bias` = `0.0005`
- `float BounceIndirectEnergy` = `1.0`
- `int Bounces` = `3`
- `CameraAttributes CameraAttributes`
- `int DenoiserRange` = `10`
- `float DenoiserStrength` = `0.1`
- `bool Directional` = `false`
- `Color EnvironmentCustomColor` = `Color(1, 1, 1, 1)`
- `float EnvironmentCustomEnergy` = `1.0`
- `Sky EnvironmentCustomSky`
- `EnvironmentMode EnvironmentMode` = `1`
- `GenerateProbes GenerateProbesSubdiv` = `2`
- `bool Interior` = `false`
- `LightmapGIData LightData`
- `int MaxTextureSize` = `16384`
- `BakeQuality Quality` = `1`
- `ShadowmaskMode ShadowmaskMode` = `0`
- `bool Supersampling` = `false`
- `float SupersamplingFactor` = `2.0`
- `float TexelScale` = `1.0`
- `bool UseDenoiser` = `true`
- `bool UseTextureForBounces` = `true`

### LightmapProbe
*Inherits: **Node3D < Node < Object***

LightmapProbe represents the position of a single manually placed probe for dynamic object lighting with LightmapGI. Lightmap probes affect the lighting of GeometryInstance3D-derived nodes that have their GeometryInstance3D.gi_mode set to GeometryInstance3D.GI_MODE_DYNAMIC.

### Marker3D
*Inherits: **Node3D < Node < Object***

Generic 3D position hint for editing. It's just like a plain Node3D, but it displays as a cross in the 3D editor at all times.

**Properties**
- `float GizmoExtents` = `0.25`

### MeshInstance3D
*Inherits: **GeometryInstance3D < VisualInstance3D < Node3D < Node < Object** | Inherited by: SoftBody3D*

MeshInstance3D is a node that takes a Mesh resource and adds it to the current scenario by creating an instance of it. This is the class most often used to render 3D geometry and can be used to instance a single Mesh in many places. This allows reusing geometry, which can save on resources. When a Mesh has to be instantiated more than thousands of times at close proximity, consider using a MultiMesh in a MultiMeshInstance3D instead.

**Properties**
- `Mesh Mesh`
- `NodePath Skeleton` = `NodePath("")`
- `Skin Skin`

**Methods**
- `ArrayMesh BakeMeshFromCurrentBlendShapeMix(ArrayMesh existing = null)`
- `ArrayMesh BakeMeshFromCurrentSkeletonPose(ArrayMesh existing = null)`
- `void CreateConvexCollision(bool clean = true, bool simplify = false)`
- `void CreateDebugTangents()`
- `void CreateMultipleConvexCollisions(MeshConvexDecompositionSettings settings = null)`
- `void CreateTrimeshCollision()`
- `int FindBlendShapeByName(StringName name)`
- `Material GetActiveMaterial(int surface)`
- `int GetBlendShapeCount()`
- `float GetBlendShapeValue(int blendShapeIdx)`
- `SkinReference GetSkinReference()`
- `Material GetSurfaceOverrideMaterial(int surface)`
- `int GetSurfaceOverrideMaterialCount()`
- `void SetBlendShapeValue(int blendShapeIdx, float value)`
- `void SetSurfaceOverrideMaterial(int surface, Material material)`

### MultiMeshInstance3D
*Inherits: **GeometryInstance3D < VisualInstance3D < Node3D < Node < Object***

MultiMeshInstance3D is a specialized node to instance GeometryInstance3Ds based on a MultiMesh resource.

**Properties**
- `MultiMesh Multimesh`

### NavigationAgent3D
*Inherits: **Node < Object***

A 3D agent used to pathfind to a position while avoiding static and dynamic obstacles. The calculation can be used by the parent node to dynamically move it along the path. Requires navigation data to work correctly.

**Properties**
- `bool AvoidanceEnabled` = `false`
- `int AvoidanceLayers` = `1`
- `int AvoidanceMask` = `1`
- `float AvoidancePriority` = `1.0`
- `bool DebugEnabled` = `false`
- `Color DebugPathCustomColor` = `Color(1, 1, 1, 1)`
- `float DebugPathCustomPointSize` = `4.0`
- `bool DebugUseCustom` = `false`
- `float Height` = `1.0`
- `bool KeepYVelocity` = `true`
- `int MaxNeighbors` = `10`
- `float MaxSpeed` = `10.0`
- `int NavigationLayers` = `1`
- `float NeighborDistance` = `50.0`
- `float PathDesiredDistance` = `1.0`
- `float PathHeightOffset` = `0.0`
- `float PathMaxDistance` = `5.0`
- `BitField[PathMetadataFlags] PathMetadataFlags` = `7`
- `PathPostProcessing PathPostprocessing` = `0`
- `float PathReturnMaxLength` = `0.0`
- `float PathReturnMaxRadius` = `0.0`
- `float PathSearchMaxDistance` = `0.0`
- `int PathSearchMaxPolygons` = `4096`
- `PathfindingAlgorithm PathfindingAlgorithm` = `0`
- `float Radius` = `0.5`
- `float SimplifyEpsilon` = `0.0`
- `bool SimplifyPath` = `false`
- `float TargetDesiredDistance` = `1.0`
- `Vector3 TargetPosition` = `Vector3(0, 0, 0)`
- `float TimeHorizonAgents` = `1.0`

**Methods**
- `float DistanceToTarget()`
- `bool GetAvoidanceLayerValue(int layerNumber)`
- `bool GetAvoidanceMaskValue(int maskNumber)`
- `PackedVector3Array GetCurrentNavigationPath()`
- `int GetCurrentNavigationPathIndex()`
- `NavigationPathQueryResult3D GetCurrentNavigationResult()`
- `Vector3 GetFinalPosition()`
- `bool GetNavigationLayerValue(int layerNumber)`
- `RID GetNavigationMap()`
- `Vector3 GetNextPathPosition()`
- `float GetPathLength()`
- `RID GetRid()`
- `bool IsNavigationFinished()`
- `bool IsTargetReachable()`
- `bool IsTargetReached()`
- `void SetAvoidanceLayerValue(int layerNumber, bool value)`
- `void SetAvoidanceMaskValue(int maskNumber, bool value)`
- `void SetNavigationLayerValue(int layerNumber, bool value)`
- `void SetNavigationMap(RID navigationMap)`
- `void SetVelocityForced(Vector3 velocity)`

### NavigationLink3D
*Inherits: **Node3D < Node < Object***

A link between two positions on NavigationRegion3Ds that agents can be routed through. These positions can be on the same NavigationRegion3D or on two different ones. Links are useful to express navigation methods other than traveling along the surface of the navigation mesh, such as ziplines, teleporters, or gaps that can be jumped across.

**Properties**
- `bool Bidirectional` = `true`
- `bool Enabled` = `true`
- `Vector3 EndPosition` = `Vector3(0, 0, 0)`
- `float EnterCost` = `0.0`
- `int NavigationLayers` = `1`
- `Vector3 StartPosition` = `Vector3(0, 0, 0)`
- `float TravelCost` = `1.0`

**Methods**
- `Vector3 GetGlobalEndPosition()`
- `Vector3 GetGlobalStartPosition()`
- `bool GetNavigationLayerValue(int layerNumber)`
- `RID GetNavigationMap()`
- `RID GetRid()`
- `void SetGlobalEndPosition(Vector3 position)`
- `void SetGlobalStartPosition(Vector3 position)`
- `void SetNavigationLayerValue(int layerNumber, bool value)`
- `void SetNavigationMap(RID navigationMap)`

### NavigationObstacle3D
*Inherits: **Node3D < Node < Object***

An obstacle needs a navigation map and outline vertices defined to work correctly. The outlines can not cross or overlap and are restricted to a plane projection. This means the y-axis of the vertices is ignored, instead the obstacle's global y-axis position is used for placement. The projected shape is extruded by the obstacles height along the y-axis.

**Properties**
- `bool AffectNavigationMesh` = `false`
- `bool AvoidanceEnabled` = `true`
- `int AvoidanceLayers` = `1`
- `bool CarveNavigationMesh` = `false`
- `float Height` = `1.0`
- `float Radius` = `0.0`
- `bool Use3dAvoidance` = `false`
- `Vector3 Velocity` = `Vector3(0, 0, 0)`
- `PackedVector3Array Vertices` = `PackedVector3Array()`

**Methods**
- `bool GetAvoidanceLayerValue(int layerNumber)`
- `RID GetNavigationMap()`
- `RID GetRid()`
- `void SetAvoidanceLayerValue(int layerNumber, bool value)`
- `void SetNavigationMap(RID navigationMap)`

### NavigationRegion3D
*Inherits: **Node3D < Node < Object***

A traversable 3D region based on a NavigationMesh that NavigationAgent3Ds can use for pathfinding.

**Properties**
- `bool Enabled` = `true`
- `float EnterCost` = `0.0`
- `int NavigationLayers` = `1`
- `NavigationMesh NavigationMesh`
- `float TravelCost` = `1.0`
- `bool UseEdgeConnections` = `true`

**Methods**
- `void BakeNavigationMesh(bool onThread = true)`
- `AABB GetBounds()`
- `bool GetNavigationLayerValue(int layerNumber)`
- `RID GetNavigationMap()`
- `RID GetRegionRid()`
- `RID GetRid()`
- `bool IsBaking()`
- `void SetNavigationLayerValue(int layerNumber, bool value)`
- `void SetNavigationMap(RID navigationMap)`

### Node3DGizmo
*Inherits: **RefCounted < Object** | Inherited by: EditorNode3DGizmo*

This abstract class helps connect the Node3D scene with the editor-specific EditorNode3DGizmo class.

### Node3D
*Inherits: **Node < Object** | Inherited by: AudioListener3D, AudioStreamPlayer3D, BoneAttachment3D, Camera3D, CollisionObject3D, CollisionPolygon3D, ...*

The Node3D node is the base representation of a node in 3D space. All other 3D nodes inherit from this class.

**Properties**
- `Basis Basis`
- `Basis GlobalBasis`
- `Vector3 GlobalPosition`
- `Vector3 GlobalRotation`
- `Vector3 GlobalRotationDegrees`
- `Transform3D GlobalTransform`
- `Vector3 Position` = `Vector3(0, 0, 0)`
- `Quaternion Quaternion`
- `Vector3 Rotation` = `Vector3(0, 0, 0)`
- `Vector3 RotationDegrees`
- `RotationEditMode RotationEditMode` = `0`
- `EulerOrder RotationOrder` = `2`
- `Vector3 Scale` = `Vector3(1, 1, 1)`
- `bool TopLevel` = `false`
- `Transform3D Transform` = `Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0)`
- `NodePath VisibilityParent` = `NodePath("")`
- `bool Visible` = `true`

**Methods**
- `void AddGizmo(Node3DGizmo gizmo)`
- `void ClearGizmos()`
- `void ClearSubgizmoSelection()`
- `void ForceUpdateTransform()`
- `Array[Node3DGizmo] GetGizmos()`
- `Transform3D GetGlobalTransformInterpolated()`
- `Node3D GetParentNode3d()`
- `World3D GetWorld3d()`
- `void GlobalRotate(Vector3 axis, float angle)`
- `void GlobalScale(Vector3 scale)`
- `void GlobalTranslate(Vector3 offset)`
- `void Hide()`
- `bool IsLocalTransformNotificationEnabled()`
- `bool IsScaleDisabled()`
- `bool IsTransformNotificationEnabled()`
- `bool IsVisibleInTree()`
- `void LookAt(Vector3 target, Vector3 up = Vector3(0, 1, 0), bool useModelFront = false)`
- `void LookAtFromPosition(Vector3 position, Vector3 target, Vector3 up = Vector3(0, 1, 0), bool useModelFront = false)`
- `void Orthonormalize()`
- `void Rotate(Vector3 axis, float angle)`
- `void RotateObjectLocal(Vector3 axis, float angle)`
- `void RotateX(float angle)`
- `void RotateY(float angle)`
- `void RotateZ(float angle)`
- `void ScaleObjectLocal(Vector3 scale)`
- `void SetDisableScale(bool disable)`
- `void SetIdentity()`
- `void SetIgnoreTransformNotification(bool enabled)`
- `void SetNotifyLocalTransform(bool enable)`
- `void SetNotifyTransform(bool enable)`
- `void SetSubgizmoSelection(Node3DGizmo gizmo, int id, Transform3D transform)`
- `void Show()`
- `Vector3 ToGlobal(Vector3 localPoint)`
- `Vector3 ToLocal(Vector3 globalPoint)`
- `void Translate(Vector3 offset)`
- `void TranslateObjectLocal(Vector3 offset)`
- `void UpdateGizmos()`

### OmniLight3D
*Inherits: **Light3D < VisualInstance3D < Node3D < Node < Object***

An Omnidirectional light is a type of Light3D that emits light in all directions. The light is attenuated by distance and this attenuation can be configured by changing its energy, radius, and attenuation parameters.

**Properties**
- `float LightSpecular` = `0.5 (overrides Light3D)`
- `float OmniAttenuation` = `1.0`
- `float OmniRange` = `5.0`
- `ShadowMode OmniShadowMode` = `1`
- `float ShadowNormalBias` = `1.0 (overrides Light3D)`

### Path3D
*Inherits: **Node3D < Node < Object***

Can have PathFollow3D child nodes moving along the Curve3D. See PathFollow3D for more information on the usage.

**Properties**
- `Curve3D Curve`
- `Color DebugCustomColor` = `Color(0, 0, 0, 1)`

### PathFollow3D
*Inherits: **Node3D < Node < Object***

This node takes its parent Path3D, and returns the coordinates of a point within it, given a distance from the first vertex.

**Properties**
- `bool CubicInterp` = `true`
- `float HOffset` = `0.0`
- `bool Loop` = `true`
- `float Progress` = `0.0`
- `float ProgressRatio` = `0.0`
- `RotationMode RotationMode` = `3`
- `bool TiltEnabled` = `true`
- `bool UseModelFront` = `false`
- `float VOffset` = `0.0`

**Methods**
- `Transform3D CorrectPosture(Transform3D transform, RotationMode rotationMode) [static]`

### RayCast3D
*Inherits: **Node3D < Node < Object***

A raycast represents a ray from its origin to its target_position that finds the closest object along its path, if it intersects any.

**Properties**
- `bool CollideWithAreas` = `false`
- `bool CollideWithBodies` = `true`
- `int CollisionMask` = `1`
- `Color DebugShapeCustomColor` = `Color(0, 0, 0, 1)`
- `int DebugShapeThickness` = `2`
- `bool Enabled` = `true`
- `bool ExcludeParent` = `true`
- `bool HitBackFaces` = `true`
- `bool HitFromInside` = `false`
- `Vector3 TargetPosition` = `Vector3(0, -1, 0)`

**Methods**
- `void AddException(CollisionObject3D node)`
- `void AddExceptionRid(RID rid)`
- `void ClearExceptions()`
- `void ForceRaycastUpdate()`
- `Object GetCollider()`
- `RID GetColliderRid()`
- `int GetColliderShape()`
- `int GetCollisionFaceIndex()`
- `bool GetCollisionMaskValue(int layerNumber)`
- `Vector3 GetCollisionNormal()`
- `Vector3 GetCollisionPoint()`
- `bool IsColliding()`
- `void RemoveException(CollisionObject3D node)`
- `void RemoveExceptionRid(RID rid)`
- `void SetCollisionMaskValue(int layerNumber, bool value)`

**C# Examples**
```csharp
var target = (CollisionObject3D)GetCollider(); // A CollisionObject3D.
var shapeId = GetColliderShape(); // The shape index in the collider.
var ownerId = target.ShapeFindOwner(shapeId); // The owner ID in the collider.
var shape = target.ShapeOwnerGetOwner(ownerId);
```

### ReflectionProbe
*Inherits: **VisualInstance3D < Node3D < Node < Object***

Captures its surroundings as a cubemap, and stores versions of it with increasing levels of blur to simulate different material roughnesses.

**Properties**
- `Color AmbientColor` = `Color(0, 0, 0, 1)`
- `float AmbientColorEnergy` = `1.0`
- `AmbientMode AmbientMode` = `1`
- `float BlendDistance` = `1.0`
- `bool BoxProjection` = `false`
- `int CullMask` = `1048575`
- `bool EnableShadows` = `false`
- `float Intensity` = `1.0`
- `bool Interior` = `false`
- `float MaxDistance` = `0.0`
- `float MeshLodThreshold` = `1.0`
- `Vector3 OriginOffset` = `Vector3(0, 0, 0)`
- `int ReflectionMask` = `1048575`
- `Vector3 Size` = `Vector3(20, 20, 20)`
- `UpdateMode UpdateMode` = `0`

### RemoteTransform3D
*Inherits: **Node3D < Node < Object***

RemoteTransform3D pushes its own Transform3D to another Node3D derived Node (called the remote node) in the scene.

**Properties**
- `NodePath RemotePath` = `NodePath("")`
- `bool UpdatePosition` = `true`
- `bool UpdateRotation` = `true`
- `bool UpdateScale` = `true`
- `bool UseGlobalCoordinates` = `true`

**Methods**
- `void ForceUpdateCache()`

### RigidBody3D
*Inherits: **PhysicsBody3D < CollisionObject3D < Node3D < Node < Object** | Inherited by: VehicleBody3D*

RigidBody3D implements full 3D physics. It cannot be controlled directly, instead, you must apply forces to it (gravity, impulses, etc.), and the physics simulation will calculate the resulting movement, rotation, react to collisions, and affect other physics bodies in its path.

**Properties**
- `float AngularDamp` = `0.0`
- `DampMode AngularDampMode` = `0`
- `Vector3 AngularVelocity` = `Vector3(0, 0, 0)`
- `bool CanSleep` = `true`
- `Vector3 CenterOfMass` = `Vector3(0, 0, 0)`
- `CenterOfMassMode CenterOfMassMode` = `0`
- `Vector3 ConstantForce` = `Vector3(0, 0, 0)`
- `Vector3 ConstantTorque` = `Vector3(0, 0, 0)`
- `bool ContactMonitor` = `false`
- `bool ContinuousCd` = `false`
- `bool CustomIntegrator` = `false`
- `bool Freeze` = `false`
- `FreezeMode FreezeMode` = `0`
- `float GravityScale` = `1.0`
- `Vector3 Inertia` = `Vector3(0, 0, 0)`
- `float LinearDamp` = `0.0`
- `DampMode LinearDampMode` = `0`
- `Vector3 LinearVelocity` = `Vector3(0, 0, 0)`
- `bool LockRotation` = `false`
- `float Mass` = `1.0`
- `int MaxContactsReported` = `0`
- `PhysicsMaterial PhysicsMaterialOverride`
- `bool Sleeping` = `false`

**Methods**
- `void _IntegrateForces(PhysicsDirectBodyState3D state) [virtual]`
- `void AddConstantCentralForce(Vector3 force)`
- `void AddConstantForce(Vector3 force, Vector3 position = Vector3(0, 0, 0))`
- `void AddConstantTorque(Vector3 torque)`
- `void ApplyCentralForce(Vector3 force)`
- `void ApplyCentralImpulse(Vector3 impulse)`
- `void ApplyForce(Vector3 force, Vector3 position = Vector3(0, 0, 0))`
- `void ApplyImpulse(Vector3 impulse, Vector3 position = Vector3(0, 0, 0))`
- `void ApplyTorque(Vector3 torque)`
- `void ApplyTorqueImpulse(Vector3 impulse)`
- `Array[Node3D] GetCollidingBodies()`
- `int GetContactCount()`
- `Basis GetInverseInertiaTensor()`
- `void SetAxisVelocity(Vector3 axisVelocity)`

**C# Examples**
```csharp
private RigidBody3D _ball;

public override void _Ready()
{
    _ball = GetNode<RigidBody3D>("Ball");
}

private Vector3 GetBallInertia()
{
    return PhysicsServer3D.BodyGetDirectState(_ball.GetRid()).InverseInertia.Inverse();
}
```

### ShapeCast3D
*Inherits: **Node3D < Node < Object***

Shape casting allows to detect collision objects by sweeping its shape along the cast direction determined by target_position. This is similar to RayCast3D, but it allows for sweeping a region of space, rather than just a straight line. ShapeCast3D can detect multiple collision objects. It is useful for things like wide laser beams or snapping a simple shape to a floor.

**Properties**
- `bool CollideWithAreas` = `false`
- `bool CollideWithBodies` = `true`
- `int CollisionMask` = `1`
- `Godot.Collections.Array CollisionResult` = `[]`
- `Color DebugShapeCustomColor` = `Color(0, 0, 0, 1)`
- `bool Enabled` = `true`
- `bool ExcludeParent` = `true`
- `float Margin` = `0.0`
- `int MaxResults` = `32`
- `Shape3D Shape`
- `Vector3 TargetPosition` = `Vector3(0, -1, 0)`

**Methods**
- `void AddException(CollisionObject3D node)`
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
- `Vector3 GetCollisionNormal(int index)`
- `Vector3 GetCollisionPoint(int index)`
- `bool IsColliding()`
- `void RemoveException(CollisionObject3D node)`
- `void RemoveExceptionRid(RID rid)`
- `void ResourceChanged(Resource resource)`
- `void SetCollisionMaskValue(int layerNumber, bool value)`

### Skeleton3D
*Inherits: **Node3D < Node < Object***

Skeleton3D provides an interface for managing a hierarchy of bones, including pose, rest and animation (see Animation). It can also use ragdoll physics.

**Properties**
- `bool AnimatePhysicalBones` = `true`
- `ModifierCallbackModeProcess ModifierCallbackModeProcess` = `1`
- `float MotionScale` = `1.0`
- `bool ShowRestOnly` = `false`

**Methods**
- `int AddBone(string name)`
- `void Advance(float delta)`
- `void ClearBones()`
- `void ClearBonesGlobalPoseOverride()`
- `Skin CreateSkinFromRestTransforms()`
- `int FindBone(string name)`
- `void ForceUpdateAllBoneTransforms()`
- `void ForceUpdateBoneChildTransform(int boneIdx)`
- `PackedInt32Array GetBoneChildren(int boneIdx)`
- `int GetBoneCount()`
- `Transform3D GetBoneGlobalPose(int boneIdx)`
- `Transform3D GetBoneGlobalPoseNoOverride(int boneIdx)`
- `Transform3D GetBoneGlobalPoseOverride(int boneIdx)`
- `Transform3D GetBoneGlobalRest(int boneIdx)`
- `Variant GetBoneMeta(int boneIdx, StringName key)`
- `Array[StringName] GetBoneMetaList(int boneIdx)`
- `string GetBoneName(int boneIdx)`
- `int GetBoneParent(int boneIdx)`
- `Transform3D GetBonePose(int boneIdx)`
- `Vector3 GetBonePosePosition(int boneIdx)`
- `Quaternion GetBonePoseRotation(int boneIdx)`
- `Vector3 GetBonePoseScale(int boneIdx)`
- `Transform3D GetBoneRest(int boneIdx)`
- `StringName GetConcatenatedBoneNames()`
- `PackedInt32Array GetParentlessBones()`
- `int GetVersion()`
- `bool HasBoneMeta(int boneIdx, StringName key)`
- `bool IsBoneEnabled(int boneIdx)`
- `void LocalizeRests()`
- `void PhysicalBonesAddCollisionException(RID exception)`
- `void PhysicalBonesRemoveCollisionException(RID exception)`
- `void PhysicalBonesStartSimulation(Array[StringName] bones = [])`
- `void PhysicalBonesStopSimulation()`
- `SkinReference RegisterSkin(Skin skin)`
- `void ResetBonePose(int boneIdx)`
- `void ResetBonePoses()`
- `void SetBoneEnabled(int boneIdx, bool enabled = true)`
- `void SetBoneGlobalPose(int boneIdx, Transform3D pose)`
- `void SetBoneGlobalPoseOverride(int boneIdx, Transform3D pose, float amount, bool persistent = false)`
- `void SetBoneMeta(int boneIdx, StringName key, Variant value)`

### SoftBody3D
*Inherits: **MeshInstance3D < GeometryInstance3D < VisualInstance3D < Node3D < Node < Object***

A deformable 3D physics mesh. Used to create elastic or deformable objects such as cloth, rubber, or other flexible materials.

**Properties**
- `int CollisionLayer` = `1`
- `int CollisionMask` = `1`
- `float DampingCoefficient` = `0.01`
- `DisableMode DisableMode` = `0`
- `float DragCoefficient` = `0.0`
- `float LinearStiffness` = `0.5`
- `NodePath ParentCollisionIgnore` = `NodePath("")`
- `float PressureCoefficient` = `0.0`
- `bool RayPickable` = `true`
- `float ShrinkingFactor` = `0.0`
- `int SimulationPrecision` = `5`
- `float TotalMass` = `1.0`

**Methods**
- `void AddCollisionExceptionWith(Node body)`
- `void ApplyCentralForce(Vector3 force)`
- `void ApplyCentralImpulse(Vector3 impulse)`
- `void ApplyForce(int pointIndex, Vector3 force)`
- `void ApplyImpulse(int pointIndex, Vector3 impulse)`
- `Array[PhysicsBody3D] GetCollisionExceptions()`
- `bool GetCollisionLayerValue(int layerNumber)`
- `bool GetCollisionMaskValue(int layerNumber)`
- `RID GetPhysicsRid()`
- `Vector3 GetPointTransform(int pointIndex)`
- `bool IsPointPinned(int pointIndex)`
- `void RemoveCollisionExceptionWith(Node body)`
- `void SetCollisionLayerValue(int layerNumber, bool value)`
- `void SetCollisionMaskValue(int layerNumber, bool value)`
- `void SetPointPinned(int pointIndex, bool pinned, NodePath attachmentPath = NodePath(""), int insertAt = -1)`

### SpotLight3D
*Inherits: **Light3D < VisualInstance3D < Node3D < Node < Object***

A Spotlight is a type of Light3D node that emits lights in a specific direction, in the shape of a cone. The light is attenuated through the distance. This attenuation can be configured by changing the energy, radius and attenuation parameters of Light3D.

**Properties**
- `float LightSpecular` = `0.5 (overrides Light3D)`
- `float ShadowBias` = `0.03 (overrides Light3D)`
- `float ShadowNormalBias` = `1.0 (overrides Light3D)`
- `float SpotAngle` = `45.0`
- `float SpotAngleAttenuation` = `1.0`
- `float SpotAttenuation` = `1.0`
- `float SpotRange` = `5.0`

### SpringArm3D
*Inherits: **Node3D < Node < Object***

SpringArm3D casts a ray or a shape along its Z axis and moves all its direct children to the collision point, with an optional margin. This is useful for 3rd person cameras that move closer to the player when inside a tight space (you may need to exclude the player's collider from the SpringArm3D's collision check).

**Properties**
- `int CollisionMask` = `1`
- `float Margin` = `0.01`
- `Shape3D Shape`
- `float SpringLength` = `1.0`

**Methods**
- `void AddExcludedObject(RID RID)`
- `void ClearExcludedObjects()`
- `float GetHitLength()`
- `bool RemoveExcludedObject(RID RID)`

### StaticBody3D
*Inherits: **PhysicsBody3D < CollisionObject3D < Node3D < Node < Object** | Inherited by: AnimatableBody3D*

A static 3D physics body. It can't be moved by external forces or contacts, but can be moved manually by other means such as code, AnimationMixers (with AnimationMixer.callback_mode_process set to AnimationMixer.ANIMATION_CALLBACK_MODE_PROCESS_PHYSICS), and RemoteTransform3D.

**Properties**
- `Vector3 ConstantAngularVelocity` = `Vector3(0, 0, 0)`
- `Vector3 ConstantLinearVelocity` = `Vector3(0, 0, 0)`
- `PhysicsMaterial PhysicsMaterialOverride`

### VehicleBody3D
*Inherits: **RigidBody3D < PhysicsBody3D < CollisionObject3D < Node3D < Node < Object***

This physics body implements all the physics logic needed to simulate a car. It is based on the raycast vehicle system commonly found in physics engines. Aside from a CollisionShape3D for the main body of the vehicle, you must also add a VehicleWheel3D node for each wheel. You should also add a MeshInstance3D to this node for the 3D model of the vehicle, but this model should generally not include meshes for the wheels. You can control the vehicle by using the brake, engine_force, and steering properties. The position or orientation of this node shouldn't be changed directly.

**Properties**
- `float Brake` = `0.0`
- `float EngineForce` = `0.0`
- `float Mass` = `40.0 (overrides RigidBody3D)`
- `float Steering` = `0.0`

### VehicleWheel3D
*Inherits: **Node3D < Node < Object***

A node used as a child of a VehicleBody3D parent to simulate the behavior of one of its wheels. This node also acts as a collider to detect if the wheel is touching a surface.

**Properties**
- `float Brake` = `0.0`
- `float DampingCompression` = `0.83`
- `float DampingRelaxation` = `0.88`
- `float EngineForce` = `0.0`
- `PhysicsInterpolationMode PhysicsInterpolationMode` = `2 (overrides Node)`
- `float Steering` = `0.0`
- `float SuspensionMaxForce` = `6000.0`
- `float SuspensionStiffness` = `5.88`
- `float SuspensionTravel` = `0.2`
- `bool UseAsSteering` = `false`
- `bool UseAsTraction` = `false`
- `float WheelFrictionSlip` = `10.5`
- `float WheelRadius` = `0.5`
- `float WheelRestLength` = `0.15`
- `float WheelRollInfluence` = `0.1`

**Methods**
- `Node3D GetContactBody()`
- `Vector3 GetContactNormal()`
- `Vector3 GetContactPoint()`
- `float GetRpm()`
- `float GetSkidinfo()`
- `bool IsInContact()`

### VisualInstance3D
*Inherits: **Node3D < Node < Object** | Inherited by: Decal, FogVolume, GeometryInstance3D, GPUParticlesAttractor3D, GPUParticlesCollision3D, Light3D, ...*

The VisualInstance3D is used to connect a resource to a visual representation. All visual 3D nodes inherit from the VisualInstance3D. In general, you should not access the VisualInstance3D properties directly as they are accessed and managed by the nodes that inherit from VisualInstance3D. VisualInstance3D is the node representation of the RenderingServer instance.

**Properties**
- `int Layers` = `1`
- `float SortingOffset` = `0.0`
- `bool SortingUseAabbCenter`

**Methods**
- `AABB _GetAabb() [virtual]`
- `AABB GetAabb()`
- `RID GetBase()`
- `RID GetInstance()`
- `bool GetLayerMaskValue(int layerNumber)`
- `void SetBase(RID base)`
- `void SetLayerMaskValue(int layerNumber, bool value)`

### VoxelGIData
*Inherits: **Resource < RefCounted < Object***

VoxelGIData contains baked voxel global illumination for use in a VoxelGI node. VoxelGIData also offers several properties to adjust the final appearance of the global illumination. These properties can be adjusted at run-time without having to bake the VoxelGI node again.

**Properties**
- `float Bias` = `1.5`
- `float DynamicRange` = `2.0`
- `float Energy` = `1.0`
- `bool Interior` = `false`
- `float NormalBias` = `0.0`
- `float Propagation` = `0.5`
- `bool UseTwoBounces` = `true`

**Methods**
- `void Allocate(Transform3D toCellXform, AABB aabb, Vector3 octreeSize, PackedByteArray octreeCells, PackedByteArray dataCells, PackedByteArray distanceField, PackedInt32Array levelCounts)`
- `AABB GetBounds()`
- `PackedByteArray GetDataCells()`
- `PackedInt32Array GetLevelCounts()`
- `PackedByteArray GetOctreeCells()`
- `Vector3 GetOctreeSize()`
- `Transform3D GetToCellXform()`

### VoxelGI
*Inherits: **VisualInstance3D < Node3D < Node < Object***

VoxelGIs are used to provide high-quality real-time indirect light and reflections to scenes. They precompute the effect of objects that emit light and the effect of static geometry to simulate the behavior of complex light in real-time. VoxelGIs need to be baked before having a visible effect. However, once baked, dynamic objects will receive light from them. Furthermore, lights can be fully dynamic or baked.

**Properties**
- `CameraAttributes CameraAttributes`
- `VoxelGIData Data`
- `Vector3 Size` = `Vector3(20, 20, 20)`
- `Subdiv Subdiv` = `1`

**Methods**
- `void Bake(Node fromNode = null, bool createVisualDebug = false)`
- `void DebugBake()`

### WorldEnvironment
*Inherits: **Node < Object***

The WorldEnvironment node is used to configure the default Environment for the scene.

**Properties**
- `CameraAttributes CameraAttributes`
- `Compositor Compositor`
- `Environment Environment`
