# Godot 4 C# API Reference — Animation

> C#-only reference. 18 classes.

### AimModifier3D
*Inherits: **BoneConstraint3D < SkeletonModifier3D < Node3D < Node < Object***

This is a simple version of LookAtModifier3D that only allows bone to the reference without advanced options such as angle limitation or time-based interpolation.

**Properties**
- `int SettingCount` = `0`

**Methods**
- `BoneAxis GetForwardAxis(int index)`
- `Axis GetPrimaryRotationAxis(int index)`
- `bool IsRelative(int index)`
- `bool IsUsingEuler(int index)`
- `bool IsUsingSecondaryRotation(int index)`
- `void SetForwardAxis(int index, BoneAxis axis)`
- `void SetPrimaryRotationAxis(int index, Axis axis)`
- `void SetRelative(int index, bool enabled)`
- `void SetUseEuler(int index, bool enabled)`
- `void SetUseSecondaryRotation(int index, bool enabled)`

### CallbackTweener
*Inherits: **Tweener < RefCounted < Object***

CallbackTweener is used to call a method in a tweening sequence. See Tween.tween_callback() for more usage information.

**Methods**
- `CallbackTweener SetDelay(float delay)`

### IntervalTweener
*Inherits: **Tweener < RefCounted < Object***

IntervalTweener is used to make delays in a tweening sequence. See Tween.tween_interval() for more usage information.

### LookAtModifier3D
*Inherits: **SkeletonModifier3D < Node3D < Node < Object***

This SkeletonModifier3D rotates a bone to look at a target. This is helpful for moving a character's head to look at the player, rotating a turret to look at a target, or any other case where you want to make a bone rotate towards something quickly and easily.

**Properties**
- `int Bone` = `-1`
- `string BoneName` = `""`
- `float Duration` = `0.0`
- `EaseType EaseType` = `0`
- `BoneAxis ForwardAxis` = `4`
- `int OriginBone`
- `string OriginBoneName`
- `NodePath OriginExternalNode`
- `OriginFrom OriginFrom` = `0`
- `Vector3 OriginOffset` = `Vector3(0, 0, 0)`
- `float OriginSafeMargin` = `0.1`
- `float PrimaryDampThreshold`
- `float PrimaryLimitAngle`
- `float PrimaryNegativeDampThreshold`
- `float PrimaryNegativeLimitAngle`
- `float PrimaryPositiveDampThreshold`
- `float PrimaryPositiveLimitAngle`
- `Axis PrimaryRotationAxis` = `1`
- `bool Relative` = `true`
- `float SecondaryDampThreshold`
- `float SecondaryLimitAngle`
- `float SecondaryNegativeDampThreshold`
- `float SecondaryNegativeLimitAngle`
- `float SecondaryPositiveDampThreshold`
- `float SecondaryPositiveLimitAngle`
- `bool SymmetryLimitation`
- `NodePath TargetNode` = `NodePath("")`
- `TransitionType TransitionType` = `0`
- `bool UseAngleLimitation` = `false`
- `bool UseSecondaryRotation` = `true`

**Methods**
- `float GetInterpolationRemaining()`
- `bool IsInterpolating()`
- `bool IsTargetWithinLimitation()`

### MethodTweener
*Inherits: **Tweener < RefCounted < Object***

MethodTweener is similar to a combination of CallbackTweener and PropertyTweener. It calls a method providing an interpolated value as a parameter. See Tween.tween_method() for more usage information.

**Methods**
- `MethodTweener SetDelay(float delay)`
- `MethodTweener SetEase(EaseType ease)`
- `MethodTweener SetTrans(TransitionType trans)`

### PropertyTweener
*Inherits: **Tweener < RefCounted < Object***

PropertyTweener is used to interpolate a property in an object. See Tween.tween_property() for more usage information.

**Methods**
- `PropertyTweener AsRelative()`
- `PropertyTweener From(Variant value)`
- `PropertyTweener FromCurrent()`
- `PropertyTweener SetCustomInterpolator(Callable interpolatorMethod)`
- `PropertyTweener SetDelay(float delay)`
- `PropertyTweener SetEase(EaseType ease)`
- `PropertyTweener SetTrans(TransitionType trans)`

**C# Examples**
```csharp
Tween tween = GetTree().CreateTween();
tween.TweenProperty(this, "position", Vector2.Right * 100.0f, 1.0f).AsRelative();
```
```csharp
Tween tween = GetTree().CreateTween();
tween.TweenProperty(this, "position", new Vector2(200.0f, 100.0f), 1.0f).From(new Vector2(100.0f, 100.0f));
```

### SkeletonIK3D
*Inherits: **SkeletonModifier3D < Node3D < Node < Object***

SkeletonIK3D is used to rotate all bones of a Skeleton3D bone chain a way that places the end bone at a desired 3D position. A typical scenario for IK in games is to place a character's feet on the ground or a character's hands on a currently held object. SkeletonIK uses FabrikInverseKinematic internally to solve the bone chain and applies the results to the Skeleton3D bones_global_pose_override property for all affected bones in the chain. If fully applied, this overwrites any bone transform from Animations or bone custom poses set by users. The applied amount can be controlled with the SkeletonModifier3D.influence property.

**Properties**
- `float Interpolation`
- `Vector3 Magnet` = `Vector3(0, 0, 0)`
- `int MaxIterations` = `10`
- `float MinDistance` = `0.01`
- `bool OverrideTipBasis` = `true`
- `StringName RootBone` = `&""`
- `Transform3D Target` = `Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0)`
- `NodePath TargetNode` = `NodePath("")`
- `StringName TipBone` = `&""`
- `bool UseMagnet` = `false`

**Methods**
- `Skeleton3D GetParentSkeleton()`
- `bool IsRunning()`
- `void Start(bool oneTime = false)`
- `void Stop()`

### SkeletonModification2DCCDIK
*Inherits: **SkeletonModification2D < Resource < RefCounted < Object***

This SkeletonModification2D uses an algorithm called Cyclic Coordinate Descent Inverse Kinematics, or CCDIK, to manipulate a chain of bones in a Skeleton2D so it reaches a defined target.

**Properties**
- `int CcdikDataChainLength` = `0`
- `NodePath TargetNodepath` = `NodePath("")`
- `NodePath TipNodepath` = `NodePath("")`

**Methods**
- `NodePath GetCcdikJointBone2dNode(int jointIdx)`
- `int GetCcdikJointBoneIndex(int jointIdx)`
- `bool GetCcdikJointConstraintAngleInvert(int jointIdx)`
- `float GetCcdikJointConstraintAngleMax(int jointIdx)`
- `float GetCcdikJointConstraintAngleMin(int jointIdx)`
- `bool GetCcdikJointEnableConstraint(int jointIdx)`
- `bool GetCcdikJointRotateFromJoint(int jointIdx)`
- `void SetCcdikJointBone2dNode(int jointIdx, NodePath bone2dNodepath)`
- `void SetCcdikJointBoneIndex(int jointIdx, int boneIdx)`
- `void SetCcdikJointConstraintAngleInvert(int jointIdx, bool invert)`
- `void SetCcdikJointConstraintAngleMax(int jointIdx, float angleMax)`
- `void SetCcdikJointConstraintAngleMin(int jointIdx, float angleMin)`
- `void SetCcdikJointEnableConstraint(int jointIdx, bool enableConstraint)`
- `void SetCcdikJointRotateFromJoint(int jointIdx, bool rotateFromJoint)`

### SkeletonModification2DFABRIK
*Inherits: **SkeletonModification2D < Resource < RefCounted < Object***

This SkeletonModification2D uses an algorithm called Forward And Backward Reaching Inverse Kinematics, or FABRIK, to rotate a bone chain so that it reaches a target.

**Properties**
- `int FabrikDataChainLength` = `0`
- `NodePath TargetNodepath` = `NodePath("")`

**Methods**
- `NodePath GetFabrikJointBone2dNode(int jointIdx)`
- `int GetFabrikJointBoneIndex(int jointIdx)`
- `Vector2 GetFabrikJointMagnetPosition(int jointIdx)`
- `bool GetFabrikJointUseTargetRotation(int jointIdx)`
- `void SetFabrikJointBone2dNode(int jointIdx, NodePath bone2dNodepath)`
- `void SetFabrikJointBoneIndex(int jointIdx, int boneIdx)`
- `void SetFabrikJointMagnetPosition(int jointIdx, Vector2 magnetPosition)`
- `void SetFabrikJointUseTargetRotation(int jointIdx, bool useTargetRotation)`

### SkeletonModification2DJiggle
*Inherits: **SkeletonModification2D < Resource < RefCounted < Object***

This modification moves a series of bones, typically called a bone chain, towards a target. What makes this modification special is that it calculates the velocity and acceleration for each bone in the bone chain, and runs a very light physics-like calculation using the inputted values. This allows the bones to overshoot the target and "jiggle" around. It can be configured to act more like a spring, or sway around like cloth might.

**Properties**
- `float Damping` = `0.75`
- `Vector2 Gravity` = `Vector2(0, 6)`
- `int JiggleDataChainLength` = `0`
- `float Mass` = `0.75`
- `float Stiffness` = `3.0`
- `NodePath TargetNodepath` = `NodePath("")`
- `bool UseGravity` = `false`

**Methods**
- `int GetCollisionMask()`
- `NodePath GetJiggleJointBone2dNode(int jointIdx)`
- `int GetJiggleJointBoneIndex(int jointIdx)`
- `float GetJiggleJointDamping(int jointIdx)`
- `Vector2 GetJiggleJointGravity(int jointIdx)`
- `float GetJiggleJointMass(int jointIdx)`
- `bool GetJiggleJointOverride(int jointIdx)`
- `float GetJiggleJointStiffness(int jointIdx)`
- `bool GetJiggleJointUseGravity(int jointIdx)`
- `bool GetUseColliders()`
- `void SetCollisionMask(int collisionMask)`
- `void SetJiggleJointBone2dNode(int jointIdx, NodePath bone2dNode)`
- `void SetJiggleJointBoneIndex(int jointIdx, int boneIdx)`
- `void SetJiggleJointDamping(int jointIdx, float damping)`
- `void SetJiggleJointGravity(int jointIdx, Vector2 gravity)`
- `void SetJiggleJointMass(int jointIdx, float mass)`
- `void SetJiggleJointOverride(int jointIdx, bool override)`
- `void SetJiggleJointStiffness(int jointIdx, float stiffness)`
- `void SetJiggleJointUseGravity(int jointIdx, bool useGravity)`
- `void SetUseColliders(bool useColliders)`

### SkeletonModification2DLookAt
*Inherits: **SkeletonModification2D < Resource < RefCounted < Object***

This SkeletonModification2D rotates a bone to look a target. This is extremely helpful for moving character's head to look at the player, rotating a turret to look at a target, or any other case where you want to make a bone rotate towards something quickly and easily.

**Properties**
- `NodePath Bone2dNode` = `NodePath("")`
- `int BoneIndex` = `-1`
- `NodePath TargetNodepath` = `NodePath("")`

**Methods**
- `float GetAdditionalRotation()`
- `bool GetConstraintAngleInvert()`
- `float GetConstraintAngleMax()`
- `float GetConstraintAngleMin()`
- `bool GetEnableConstraint()`
- `void SetAdditionalRotation(float rotation)`
- `void SetConstraintAngleInvert(bool invert)`
- `void SetConstraintAngleMax(float angleMax)`
- `void SetConstraintAngleMin(float angleMin)`
- `void SetEnableConstraint(bool enableConstraint)`

### SkeletonModification2DPhysicalBones
*Inherits: **SkeletonModification2D < Resource < RefCounted < Object***

This modification takes the transforms of PhysicalBone2D nodes and applies them to Bone2D nodes. This allows the Bone2D nodes to react to physics thanks to the linked PhysicalBone2D nodes.

**Properties**
- `int PhysicalBoneChainLength` = `0`

**Methods**
- `void FetchPhysicalBones()`
- `NodePath GetPhysicalBoneNode(int jointIdx)`
- `void SetPhysicalBoneNode(int jointIdx, NodePath physicalbone2dNode)`
- `void StartSimulation(Array[StringName] bones = [])`
- `void StopSimulation(Array[StringName] bones = [])`

### SkeletonModification2DStackHolder
*Inherits: **SkeletonModification2D < Resource < RefCounted < Object***

This SkeletonModification2D holds a reference to a SkeletonModificationStack2D, allowing you to use multiple modification stacks on a single Skeleton2D.

**Methods**
- `SkeletonModificationStack2D GetHeldModificationStack()`
- `void SetHeldModificationStack(SkeletonModificationStack2D heldModificationStack)`

### SkeletonModification2DTwoBoneIK
*Inherits: **SkeletonModification2D < Resource < RefCounted < Object***

This SkeletonModification2D uses an algorithm typically called TwoBoneIK. This algorithm works by leveraging the law of cosines and the lengths of the bones to figure out what rotation the bones currently have, and what rotation they need to make a complete triangle, where the first bone, the second bone, and the target form the three vertices of the triangle. Because the algorithm works by making a triangle, it can only operate on two bones.

**Properties**
- `bool FlipBendDirection` = `false`
- `float TargetMaximumDistance` = `0.0`
- `float TargetMinimumDistance` = `0.0`
- `NodePath TargetNodepath` = `NodePath("")`

**Methods**
- `NodePath GetJointOneBone2dNode()`
- `int GetJointOneBoneIdx()`
- `NodePath GetJointTwoBone2dNode()`
- `int GetJointTwoBoneIdx()`
- `void SetJointOneBone2dNode(NodePath bone2dNode)`
- `void SetJointOneBoneIdx(int boneIdx)`
- `void SetJointTwoBone2dNode(NodePath bone2dNode)`
- `void SetJointTwoBoneIdx(int boneIdx)`

### SkeletonModification2D
*Inherits: **Resource < RefCounted < Object** | Inherited by: SkeletonModification2DCCDIK, SkeletonModification2DFABRIK, SkeletonModification2DJiggle, SkeletonModification2DLookAt, SkeletonModification2DPhysicalBones, SkeletonModification2DStackHolder, ...*

This resource provides an interface that can be expanded so code that operates on Bone2D nodes in a Skeleton2D can be mixed and matched together to create complex interactions.

**Properties**
- `bool Enabled` = `true`
- `int ExecutionMode` = `0`

**Methods**
- `void _DrawEditorGizmo() [virtual]`
- `void _Execute(float delta) [virtual]`
- `void _SetupModification(SkeletonModificationStack2D modificationStack) [virtual]`
- `float ClampAngle(float angle, float min, float max, bool invert)`
- `bool GetEditorDrawGizmo()`
- `bool GetIsSetup()`
- `SkeletonModificationStack2D GetModificationStack()`
- `void SetEditorDrawGizmo(bool drawGizmo)`
- `void SetIsSetup(bool isSetup)`

### SkeletonModificationStack2D
*Inherits: **Resource < RefCounted < Object***

This resource is used by the Skeleton and holds a stack of SkeletonModification2Ds.

**Properties**
- `bool Enabled` = `false`
- `int ModificationCount` = `0`
- `float Strength` = `1.0`

**Methods**
- `void AddModification(SkeletonModification2D modification)`
- `void DeleteModification(int modIdx)`
- `void EnableAllModifications(bool enabled)`
- `void Execute(float delta, int executionMode)`
- `bool GetIsSetup()`
- `SkeletonModification2D GetModification(int modIdx)`
- `Skeleton2D GetSkeleton()`
- `void SetModification(int modIdx, SkeletonModification2D modification)`
- `void Setup()`

### SkeletonModifier3D
*Inherits: **Node3D < Node < Object** | Inherited by: BoneConstraint3D, BoneTwistDisperser3D, IKModifier3D, LimitAngularVelocityModifier3D, LookAtModifier3D, ModifierBoneTarget3D, ...*

SkeletonModifier3D retrieves a target Skeleton3D by having a Skeleton3D parent.

**Properties**
- `bool Active` = `true`
- `float Influence` = `1.0`

**Methods**
- `void _ProcessModification() [virtual]`
- `void _ProcessModificationWithDelta(float delta) [virtual]`
- `void _SkeletonChanged(Skeleton3D oldSkeleton, Skeleton3D newSkeleton) [virtual]`
- `void _ValidateBoneNames() [virtual]`
- `Skeleton3D GetSkeleton()`

### Tweener
*Inherits: **RefCounted < Object** | Inherited by: CallbackTweener, IntervalTweener, MethodTweener, PropertyTweener, SubtweenTweener*

Tweeners are objects that perform a specific animating task, e.g. interpolating a property or calling a method at a given time. A Tweener can't be created manually, you need to use a dedicated method from Tween.
