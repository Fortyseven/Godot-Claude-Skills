# Godot 4 C# API Reference — Physics

> C#-only reference. 40 classes.

### Area2D
*Inherits: **CollisionObject2D < Node2D < CanvasItem < Node < Object***

Area2D is a region of 2D space defined by one or multiple CollisionShape2D or CollisionPolygon2D child nodes. It detects when other CollisionObject2Ds enter or exit it, and it also keeps track of which collision objects haven't exited it yet (i.e. which one are overlapping it).

**Properties**
- `float AngularDamp` = `1.0`
- `SpaceOverride AngularDampSpaceOverride` = `0`
- `StringName AudioBusName` = `&"Master"`
- `bool AudioBusOverride` = `false`
- `float Gravity` = `980.0`
- `Vector2 GravityDirection` = `Vector2(0, 1)`
- `bool GravityPoint` = `false`
- `Vector2 GravityPointCenter` = `Vector2(0, 1)`
- `float GravityPointUnitDistance` = `0.0`
- `SpaceOverride GravitySpaceOverride` = `0`
- `float LinearDamp` = `0.1`
- `SpaceOverride LinearDampSpaceOverride` = `0`
- `bool Monitorable` = `true`
- `bool Monitoring` = `true`
- `int Priority` = `0`

**Methods**
- `Array[Area2D] GetOverlappingAreas()`
- `Array[Node2D] GetOverlappingBodies()`
- `bool HasOverlappingAreas()`
- `bool HasOverlappingBodies()`
- `bool OverlapsArea(Node area)`
- `bool OverlapsBody(Node body)`

### Area3D
*Inherits: **CollisionObject3D < Node3D < Node < Object***

Area3D is a region of 3D space defined by one or multiple CollisionShape3D or CollisionPolygon3D child nodes. It detects when other CollisionObject3Ds enter or exit it, and it also keeps track of which collision objects haven't exited it yet (i.e. which one are overlapping it).

**Properties**
- `float AngularDamp` = `0.1`
- `SpaceOverride AngularDampSpaceOverride` = `0`
- `StringName AudioBusName` = `&"Master"`
- `bool AudioBusOverride` = `false`
- `float Gravity` = `9.8`
- `Vector3 GravityDirection` = `Vector3(0, -1, 0)`
- `bool GravityPoint` = `false`
- `Vector3 GravityPointCenter` = `Vector3(0, -1, 0)`
- `float GravityPointUnitDistance` = `0.0`
- `SpaceOverride GravitySpaceOverride` = `0`
- `float LinearDamp` = `0.1`
- `SpaceOverride LinearDampSpaceOverride` = `0`
- `bool Monitorable` = `true`
- `bool Monitoring` = `true`
- `int Priority` = `0`
- `float ReverbBusAmount` = `0.0`
- `bool ReverbBusEnabled` = `false`
- `StringName ReverbBusName` = `&"Master"`
- `float ReverbBusUniformity` = `0.0`
- `float WindAttenuationFactor` = `0.0`
- `float WindForceMagnitude` = `0.0`
- `NodePath WindSourcePath` = `NodePath("")`

**Methods**
- `Array[Area3D] GetOverlappingAreas()`
- `Array[Node3D] GetOverlappingBodies()`
- `bool HasOverlappingAreas()`
- `bool HasOverlappingBodies()`
- `bool OverlapsArea(Node area)`
- `bool OverlapsBody(Node body)`

### CollisionPolygon3D
*Inherits: **Node3D < Node < Object***

A node that provides a thickened polygon shape (a prism) to a CollisionObject3D parent and allows it to be edited. The polygon can be concave or convex. This can give a detection shape to an Area3D or turn a PhysicsBody3D into a solid object.

**Properties**
- `Color DebugColor` = `Color(0, 0, 0, 0)`
- `bool DebugFill` = `true`
- `float Depth` = `1.0`
- `bool Disabled` = `false`
- `float Margin` = `0.04`
- `PackedVector2Array Polygon` = `PackedVector2Array()`

### CollisionShape3D
*Inherits: **Node3D < Node < Object***

A node that provides a Shape3D to a CollisionObject3D parent and allows it to be edited. This can give a detection shape to an Area3D or turn a PhysicsBody3D into a solid object.

**Properties**
- `Color DebugColor` = `Color(0, 0, 0, 0)`
- `bool DebugFill` = `true`
- `bool Disabled` = `false`
- `Shape3D Shape`

**Methods**
- `void MakeConvexFromSiblings()`
- `void ResourceChanged(Resource resource)`

### ConeTwistJoint3D
*Inherits: **Joint3D < Node3D < Node < Object***

A physics joint that connects two 3D physics bodies in a way that simulates a ball-and-socket joint. The twist axis is initiated as the X axis of the ConeTwistJoint3D. Once the physics bodies swing, the twist axis is calculated as the middle of the X axes of the joint in the local space of the two physics bodies. Useful for limbs like shoulders and hips, lamps hanging off a ceiling, etc.

**Properties**
- `float Bias` = `0.3`
- `float Relaxation` = `1.0`
- `float Softness` = `0.8`
- `float SwingSpan` = `0.7853982`
- `float TwistSpan` = `3.1415927`

**Methods**
- `float GetParam(Param param)`
- `void SetParam(Param param, float value)`

### Generic6DOFJoint3D
*Inherits: **Joint3D < Node3D < Node < Object***

The Generic6DOFJoint3D (6 Degrees Of Freedom) joint allows for implementing custom types of joints by locking the rotation and translation of certain axes.

**Properties**
- `float AngularLimitX/damping` = `1.0`
- `bool AngularLimitX/enabled` = `true`
- `float AngularLimitX/erp` = `0.5`
- `float AngularLimitX/forceLimit` = `0.0`
- `float AngularLimitX/lowerAngle` = `0.0`
- `float AngularLimitX/restitution` = `0.0`
- `float AngularLimitX/softness` = `0.5`
- `float AngularLimitX/upperAngle` = `0.0`
- `float AngularLimitY/damping` = `1.0`
- `bool AngularLimitY/enabled` = `true`
- `float AngularLimitY/erp` = `0.5`
- `float AngularLimitY/forceLimit` = `0.0`
- `float AngularLimitY/lowerAngle` = `0.0`
- `float AngularLimitY/restitution` = `0.0`
- `float AngularLimitY/softness` = `0.5`
- `float AngularLimitY/upperAngle` = `0.0`
- `float AngularLimitZ/damping` = `1.0`
- `bool AngularLimitZ/enabled` = `true`
- `float AngularLimitZ/erp` = `0.5`
- `float AngularLimitZ/forceLimit` = `0.0`
- `float AngularLimitZ/lowerAngle` = `0.0`
- `float AngularLimitZ/restitution` = `0.0`
- `float AngularLimitZ/softness` = `0.5`
- `float AngularLimitZ/upperAngle` = `0.0`
- `bool AngularMotorX/enabled` = `false`
- `float AngularMotorX/forceLimit` = `300.0`
- `float AngularMotorX/targetVelocity` = `0.0`
- `bool AngularMotorY/enabled` = `false`
- `float AngularMotorY/forceLimit` = `300.0`
- `float AngularMotorY/targetVelocity` = `0.0`

**Methods**
- `bool GetFlagX(Flag flag)`
- `bool GetFlagY(Flag flag)`
- `bool GetFlagZ(Flag flag)`
- `float GetParamX(Param param)`
- `float GetParamY(Param param)`
- `float GetParamZ(Param param)`
- `void SetFlagX(Flag flag, bool value)`
- `void SetFlagY(Flag flag, bool value)`
- `void SetFlagZ(Flag flag, bool value)`
- `void SetParamX(Param param, float value)`
- `void SetParamY(Param param, float value)`
- `void SetParamZ(Param param, float value)`

### HingeJoint3D
*Inherits: **Joint3D < Node3D < Node < Object***

A physics joint that restricts the rotation of a 3D physics body around an axis relative to another physics body. For example, Body A can be a StaticBody3D representing a door hinge that a RigidBody3D rotates around.

**Properties**
- `float AngularLimit/bias` = `0.3`
- `bool AngularLimit/enable` = `false`
- `float AngularLimit/lower` = `-1.5707964`
- `float AngularLimit/relaxation` = `1.0`
- `float AngularLimit/softness` = `0.9`
- `float AngularLimit/upper` = `1.5707964`
- `bool Motor/enable` = `false`
- `float Motor/maxImpulse` = `1.0`
- `float Motor/targetVelocity` = `1.0`
- `float Params/bias` = `0.3`

**Methods**
- `bool GetFlag(Flag flag)`
- `float GetParam(Param param)`
- `void SetFlag(Flag flag, bool enabled)`
- `void SetParam(Param param, float value)`

### Joint3D
*Inherits: **Node3D < Node < Object** | Inherited by: ConeTwistJoint3D, Generic6DOFJoint3D, HingeJoint3D, PinJoint3D, SliderJoint3D*

Abstract base class for all joints in 3D physics. 3D joints bind together two physics bodies (node_a and node_b) and apply a constraint. If only one body is defined, it is attached to a fixed StaticBody3D without collision shapes.

**Properties**
- `bool ExcludeNodesFromCollision` = `true`
- `NodePath NodeA` = `NodePath("")`
- `NodePath NodeB` = `NodePath("")`
- `int SolverPriority` = `1`

**Methods**
- `RID GetRid()`

### PhysicsBody2D
*Inherits: **CollisionObject2D < Node2D < CanvasItem < Node < Object** | Inherited by: CharacterBody2D, RigidBody2D, StaticBody2D*

PhysicsBody2D is an abstract base class for 2D game objects affected by physics. All 2D physics bodies inherit from it.

**Properties**
- `bool InputPickable` = `false (overrides CollisionObject2D)`

**Methods**
- `void AddCollisionExceptionWith(Node body)`
- `Array[PhysicsBody2D] GetCollisionExceptions()`
- `Vector2 GetGravity()`
- `KinematicCollision2D MoveAndCollide(Vector2 motion, bool testOnly = false, float safeMargin = 0.08, bool recoveryAsCollision = false)`
- `void RemoveCollisionExceptionWith(Node body)`
- `bool TestMove(Transform2D from, Vector2 motion, KinematicCollision2D collision = null, float safeMargin = 0.08, bool recoveryAsCollision = false)`

### PhysicsBody3D
*Inherits: **CollisionObject3D < Node3D < Node < Object** | Inherited by: CharacterBody3D, PhysicalBone3D, RigidBody3D, StaticBody3D*

PhysicsBody3D is an abstract base class for 3D game objects affected by physics. All 3D physics bodies inherit from it.

**Properties**
- `bool AxisLockAngularX` = `false`
- `bool AxisLockAngularY` = `false`
- `bool AxisLockAngularZ` = `false`
- `bool AxisLockLinearX` = `false`
- `bool AxisLockLinearY` = `false`
- `bool AxisLockLinearZ` = `false`

**Methods**
- `void AddCollisionExceptionWith(Node body)`
- `bool GetAxisLock(BodyAxis axis)`
- `Array[PhysicsBody3D] GetCollisionExceptions()`
- `Vector3 GetGravity()`
- `KinematicCollision3D MoveAndCollide(Vector3 motion, bool testOnly = false, float safeMargin = 0.001, bool recoveryAsCollision = false, int maxCollisions = 1)`
- `void RemoveCollisionExceptionWith(Node body)`
- `void SetAxisLock(BodyAxis axis, bool lock)`
- `bool TestMove(Transform3D from, Vector3 motion, KinematicCollision3D collision = null, float safeMargin = 0.001, bool recoveryAsCollision = false, int maxCollisions = 1)`

### PhysicsDirectBodyState2DExtension
*Inherits: **PhysicsDirectBodyState2D < Object***

This class extends PhysicsDirectBodyState2D by providing additional virtual methods that can be overridden. When these methods are overridden, they will be called instead of the internal methods of the physics server.

**Methods**
- `void _AddConstantCentralForce(Vector2 force) [virtual]`
- `void _AddConstantForce(Vector2 force, Vector2 position) [virtual]`
- `void _AddConstantTorque(float torque) [virtual]`
- `void _ApplyCentralForce(Vector2 force) [virtual]`
- `void _ApplyCentralImpulse(Vector2 impulse) [virtual]`
- `void _ApplyForce(Vector2 force, Vector2 position) [virtual]`
- `void _ApplyImpulse(Vector2 impulse, Vector2 position) [virtual]`
- `void _ApplyTorque(float torque) [virtual]`
- `void _ApplyTorqueImpulse(float impulse) [virtual]`
- `float _GetAngularVelocity() [virtual]`
- `Vector2 _GetCenterOfMass() [virtual]`
- `Vector2 _GetCenterOfMassLocal() [virtual]`
- `int _GetCollisionLayer() [virtual]`
- `int _GetCollisionMask() [virtual]`
- `Vector2 _GetConstantForce() [virtual]`
- `float _GetConstantTorque() [virtual]`
- `RID _GetContactCollider(int contactIdx) [virtual]`
- `int _GetContactColliderId(int contactIdx) [virtual]`
- `Object _GetContactColliderObject(int contactIdx) [virtual]`
- `Vector2 _GetContactColliderPosition(int contactIdx) [virtual]`
- `int _GetContactColliderShape(int contactIdx) [virtual]`
- `Vector2 _GetContactColliderVelocityAtPosition(int contactIdx) [virtual]`
- `int _GetContactCount() [virtual]`
- `Vector2 _GetContactImpulse(int contactIdx) [virtual]`
- `Vector2 _GetContactLocalNormal(int contactIdx) [virtual]`
- `Vector2 _GetContactLocalPosition(int contactIdx) [virtual]`
- `int _GetContactLocalShape(int contactIdx) [virtual]`
- `Vector2 _GetContactLocalVelocityAtPosition(int contactIdx) [virtual]`
- `float _GetInverseInertia() [virtual]`
- `float _GetInverseMass() [virtual]`
- `Vector2 _GetLinearVelocity() [virtual]`
- `PhysicsDirectSpaceState2D _GetSpaceState() [virtual]`
- `float _GetStep() [virtual]`
- `float _GetTotalAngularDamp() [virtual]`
- `Vector2 _GetTotalGravity() [virtual]`
- `float _GetTotalLinearDamp() [virtual]`
- `Transform2D _GetTransform() [virtual]`
- `Vector2 _GetVelocityAtLocalPosition(Vector2 localPosition) [virtual]`
- `void _IntegrateForces() [virtual]`
- `bool _IsSleeping() [virtual]`

### PhysicsDirectBodyState2D
*Inherits: **Object** | Inherited by: PhysicsDirectBodyState2DExtension*

Provides direct access to a physics body in the PhysicsServer2D, allowing safe changes to physics properties. This object is passed via the direct state callback of RigidBody2D, and is intended for changing the direct state of that body. See RigidBody2D._integrate_forces().

**Properties**
- `float AngularVelocity`
- `Vector2 CenterOfMass`
- `Vector2 CenterOfMassLocal`
- `int CollisionLayer`
- `int CollisionMask`
- `float InverseInertia`
- `float InverseMass`
- `Vector2 LinearVelocity`
- `bool Sleeping`
- `float Step`
- `float TotalAngularDamp`
- `Vector2 TotalGravity`
- `float TotalLinearDamp`
- `Transform2D Transform`

**Methods**
- `void AddConstantCentralForce(Vector2 force = Vector2(0, 0))`
- `void AddConstantForce(Vector2 force, Vector2 position = Vector2(0, 0))`
- `void AddConstantTorque(float torque)`
- `void ApplyCentralForce(Vector2 force = Vector2(0, 0))`
- `void ApplyCentralImpulse(Vector2 impulse)`
- `void ApplyForce(Vector2 force, Vector2 position = Vector2(0, 0))`
- `void ApplyImpulse(Vector2 impulse, Vector2 position = Vector2(0, 0))`
- `void ApplyTorque(float torque)`
- `void ApplyTorqueImpulse(float impulse)`
- `Vector2 GetConstantForce()`
- `float GetConstantTorque()`
- `RID GetContactCollider(int contactIdx)`
- `int GetContactColliderId(int contactIdx)`
- `Object GetContactColliderObject(int contactIdx)`
- `Vector2 GetContactColliderPosition(int contactIdx)`
- `int GetContactColliderShape(int contactIdx)`
- `Vector2 GetContactColliderVelocityAtPosition(int contactIdx)`
- `int GetContactCount()`
- `Vector2 GetContactImpulse(int contactIdx)`
- `Vector2 GetContactLocalNormal(int contactIdx)`
- `Vector2 GetContactLocalPosition(int contactIdx)`
- `int GetContactLocalShape(int contactIdx)`
- `Vector2 GetContactLocalVelocityAtPosition(int contactIdx)`
- `PhysicsDirectSpaceState2D GetSpaceState()`
- `Vector2 GetVelocityAtLocalPosition(Vector2 localPosition)`
- `void IntegrateForces()`
- `void SetConstantForce(Vector2 force)`
- `void SetConstantTorque(float torque)`

### PhysicsDirectBodyState3DExtension
*Inherits: **PhysicsDirectBodyState3D < Object***

This class extends PhysicsDirectBodyState3D by providing additional virtual methods that can be overridden. When these methods are overridden, they will be called instead of the internal methods of the physics server.

**Methods**
- `void _AddConstantCentralForce(Vector3 force) [virtual]`
- `void _AddConstantForce(Vector3 force, Vector3 position) [virtual]`
- `void _AddConstantTorque(Vector3 torque) [virtual]`
- `void _ApplyCentralForce(Vector3 force) [virtual]`
- `void _ApplyCentralImpulse(Vector3 impulse) [virtual]`
- `void _ApplyForce(Vector3 force, Vector3 position) [virtual]`
- `void _ApplyImpulse(Vector3 impulse, Vector3 position) [virtual]`
- `void _ApplyTorque(Vector3 torque) [virtual]`
- `void _ApplyTorqueImpulse(Vector3 impulse) [virtual]`
- `Vector3 _GetAngularVelocity() [virtual]`
- `Vector3 _GetCenterOfMass() [virtual]`
- `Vector3 _GetCenterOfMassLocal() [virtual]`
- `int _GetCollisionLayer() [virtual]`
- `int _GetCollisionMask() [virtual]`
- `Vector3 _GetConstantForce() [virtual]`
- `Vector3 _GetConstantTorque() [virtual]`
- `RID _GetContactCollider(int contactIdx) [virtual]`
- `int _GetContactColliderId(int contactIdx) [virtual]`
- `Object _GetContactColliderObject(int contactIdx) [virtual]`
- `Vector3 _GetContactColliderPosition(int contactIdx) [virtual]`
- `int _GetContactColliderShape(int contactIdx) [virtual]`
- `Vector3 _GetContactColliderVelocityAtPosition(int contactIdx) [virtual]`
- `int _GetContactCount() [virtual]`
- `Vector3 _GetContactImpulse(int contactIdx) [virtual]`
- `Vector3 _GetContactLocalNormal(int contactIdx) [virtual]`
- `Vector3 _GetContactLocalPosition(int contactIdx) [virtual]`
- `int _GetContactLocalShape(int contactIdx) [virtual]`
- `Vector3 _GetContactLocalVelocityAtPosition(int contactIdx) [virtual]`
- `Vector3 _GetInverseInertia() [virtual]`
- `Basis _GetInverseInertiaTensor() [virtual]`
- `float _GetInverseMass() [virtual]`
- `Vector3 _GetLinearVelocity() [virtual]`
- `Basis _GetPrincipalInertiaAxes() [virtual]`
- `PhysicsDirectSpaceState3D _GetSpaceState() [virtual]`
- `float _GetStep() [virtual]`
- `float _GetTotalAngularDamp() [virtual]`
- `Vector3 _GetTotalGravity() [virtual]`
- `float _GetTotalLinearDamp() [virtual]`
- `Transform3D _GetTransform() [virtual]`
- `Vector3 _GetVelocityAtLocalPosition(Vector3 localPosition) [virtual]`

### PhysicsDirectBodyState3D
*Inherits: **Object** | Inherited by: PhysicsDirectBodyState3DExtension*

Provides direct access to a physics body in the PhysicsServer3D, allowing safe changes to physics properties. This object is passed via the direct state callback of RigidBody3D, and is intended for changing the direct state of that body. See RigidBody3D._integrate_forces().

**Properties**
- `Vector3 AngularVelocity`
- `Vector3 CenterOfMass`
- `Vector3 CenterOfMassLocal`
- `int CollisionLayer`
- `int CollisionMask`
- `Vector3 InverseInertia`
- `Basis InverseInertiaTensor`
- `float InverseMass`
- `Vector3 LinearVelocity`
- `Basis PrincipalInertiaAxes`
- `bool Sleeping`
- `float Step`
- `float TotalAngularDamp`
- `Vector3 TotalGravity`
- `float TotalLinearDamp`
- `Transform3D Transform`

**Methods**
- `void AddConstantCentralForce(Vector3 force = Vector3(0, 0, 0))`
- `void AddConstantForce(Vector3 force, Vector3 position = Vector3(0, 0, 0))`
- `void AddConstantTorque(Vector3 torque)`
- `void ApplyCentralForce(Vector3 force = Vector3(0, 0, 0))`
- `void ApplyCentralImpulse(Vector3 impulse = Vector3(0, 0, 0))`
- `void ApplyForce(Vector3 force, Vector3 position = Vector3(0, 0, 0))`
- `void ApplyImpulse(Vector3 impulse, Vector3 position = Vector3(0, 0, 0))`
- `void ApplyTorque(Vector3 torque)`
- `void ApplyTorqueImpulse(Vector3 impulse)`
- `Vector3 GetConstantForce()`
- `Vector3 GetConstantTorque()`
- `RID GetContactCollider(int contactIdx)`
- `int GetContactColliderId(int contactIdx)`
- `Object GetContactColliderObject(int contactIdx)`
- `Vector3 GetContactColliderPosition(int contactIdx)`
- `int GetContactColliderShape(int contactIdx)`
- `Vector3 GetContactColliderVelocityAtPosition(int contactIdx)`
- `int GetContactCount()`
- `Vector3 GetContactImpulse(int contactIdx)`
- `Vector3 GetContactLocalNormal(int contactIdx)`
- `Vector3 GetContactLocalPosition(int contactIdx)`
- `int GetContactLocalShape(int contactIdx)`
- `Vector3 GetContactLocalVelocityAtPosition(int contactIdx)`
- `PhysicsDirectSpaceState3D GetSpaceState()`
- `Vector3 GetVelocityAtLocalPosition(Vector3 localPosition)`
- `void IntegrateForces()`
- `void SetConstantForce(Vector3 force)`
- `void SetConstantTorque(Vector3 torque)`

### PhysicsDirectSpaceState2DExtension
*Inherits: **PhysicsDirectSpaceState2D < Object***

This class extends PhysicsDirectSpaceState2D by providing additional virtual methods that can be overridden. When these methods are overridden, they will be called instead of the internal methods of the physics server.

**Methods**
- `bool _CastMotion(RID shapeRid, Transform2D transform, Vector2 motion, float margin, int collisionMask, bool collideWithBodies, bool collideWithAreas, float* closestSafe, float* closestUnsafe) [virtual]`
- `bool _CollideShape(RID shapeRid, Transform2D transform, Vector2 motion, float margin, int collisionMask, bool collideWithBodies, bool collideWithAreas, void* results, int maxResults, int32_t* resultCount) [virtual]`
- `int _IntersectPoint(Vector2 position, int canvasInstanceId, int collisionMask, bool collideWithBodies, bool collideWithAreas, PhysicsServer2DExtensionShapeResult* results, int maxResults) [virtual]`
- `bool _IntersectRay(Vector2 from, Vector2 to, int collisionMask, bool collideWithBodies, bool collideWithAreas, bool hitFromInside, PhysicsServer2DExtensionRayResult* result) [virtual]`
- `int _IntersectShape(RID shapeRid, Transform2D transform, Vector2 motion, float margin, int collisionMask, bool collideWithBodies, bool collideWithAreas, PhysicsServer2DExtensionShapeResult* result, int maxResults) [virtual]`
- `bool _RestInfo(RID shapeRid, Transform2D transform, Vector2 motion, float margin, int collisionMask, bool collideWithBodies, bool collideWithAreas, PhysicsServer2DExtensionShapeRestInfo* restInfo) [virtual]`
- `bool IsBodyExcludedFromQuery(RID body)`

### PhysicsDirectSpaceState2D
*Inherits: **Object** | Inherited by: PhysicsDirectSpaceState2DExtension*

Provides direct access to a physics space in the PhysicsServer2D. It's used mainly to do queries against objects and areas residing in a given space.

**Methods**
- `PackedFloat32Array CastMotion(PhysicsShapeQueryParameters2D parameters)`
- `Array[Vector2] CollideShape(PhysicsShapeQueryParameters2D parameters, int maxResults = 32)`
- `Godot.Collections.Dictionary GetRestInfo(PhysicsShapeQueryParameters2D parameters)`
- `Array[Dictionary] IntersectPoint(PhysicsPointQueryParameters2D parameters, int maxResults = 32)`
- `Godot.Collections.Dictionary IntersectRay(PhysicsRayQueryParameters2D parameters)`
- `Array[Dictionary] IntersectShape(PhysicsShapeQueryParameters2D parameters, int maxResults = 32)`

### PhysicsDirectSpaceState3DExtension
*Inherits: **PhysicsDirectSpaceState3D < Object***

This class extends PhysicsDirectSpaceState3D by providing additional virtual methods that can be overridden. When these methods are overridden, they will be called instead of the internal methods of the physics server.

**Methods**
- `bool _CastMotion(RID shapeRid, Transform3D transform, Vector3 motion, float margin, int collisionMask, bool collideWithBodies, bool collideWithAreas, float* closestSafe, float* closestUnsafe, PhysicsServer3DExtensionShapeRestInfo* info) [virtual]`
- `bool _CollideShape(RID shapeRid, Transform3D transform, Vector3 motion, float margin, int collisionMask, bool collideWithBodies, bool collideWithAreas, void* results, int maxResults, int32_t* resultCount) [virtual]`
- `Vector3 _GetClosestPointToObjectVolume(RID object, Vector3 point) [virtual]`
- `int _IntersectPoint(Vector3 position, int collisionMask, bool collideWithBodies, bool collideWithAreas, PhysicsServer3DExtensionShapeResult* results, int maxResults) [virtual]`
- `bool _IntersectRay(Vector3 from, Vector3 to, int collisionMask, bool collideWithBodies, bool collideWithAreas, bool hitFromInside, bool hitBackFaces, bool pickRay, PhysicsServer3DExtensionRayResult* result) [virtual]`
- `int _IntersectShape(RID shapeRid, Transform3D transform, Vector3 motion, float margin, int collisionMask, bool collideWithBodies, bool collideWithAreas, PhysicsServer3DExtensionShapeResult* resultCount, int maxResults) [virtual]`
- `bool _RestInfo(RID shapeRid, Transform3D transform, Vector3 motion, float margin, int collisionMask, bool collideWithBodies, bool collideWithAreas, PhysicsServer3DExtensionShapeRestInfo* restInfo) [virtual]`
- `bool IsBodyExcludedFromQuery(RID body)`

### PhysicsDirectSpaceState3D
*Inherits: **Object** | Inherited by: PhysicsDirectSpaceState3DExtension*

Provides direct access to a physics space in the PhysicsServer3D. It's used mainly to do queries against objects and areas residing in a given space.

**Methods**
- `PackedFloat32Array CastMotion(PhysicsShapeQueryParameters3D parameters)`
- `Array[Vector3] CollideShape(PhysicsShapeQueryParameters3D parameters, int maxResults = 32)`
- `Godot.Collections.Dictionary GetRestInfo(PhysicsShapeQueryParameters3D parameters)`
- `Array[Dictionary] IntersectPoint(PhysicsPointQueryParameters3D parameters, int maxResults = 32)`
- `Godot.Collections.Dictionary IntersectRay(PhysicsRayQueryParameters3D parameters)`
- `Array[Dictionary] IntersectShape(PhysicsShapeQueryParameters3D parameters, int maxResults = 32)`

### PhysicsMaterial
*Inherits: **Resource < RefCounted < Object***

Holds physics-related properties of a surface, namely its roughness and bounciness. This class is used to apply these properties to a physics body.

**Properties**
- `bool Absorbent` = `false`
- `float Bounce` = `0.0`
- `float Friction` = `1.0`
- `bool Rough` = `false`

### PhysicsPointQueryParameters2D
*Inherits: **RefCounted < Object***

By changing various properties of this object, such as the point position, you can configure the parameters for PhysicsDirectSpaceState2D.intersect_point().

**Properties**
- `int CanvasInstanceId` = `0`
- `bool CollideWithAreas` = `false`
- `bool CollideWithBodies` = `true`
- `int CollisionMask` = `4294967295`
- `Array[RID] Exclude` = `[]`
- `Vector2 Position` = `Vector2(0, 0)`

### PhysicsPointQueryParameters3D
*Inherits: **RefCounted < Object***

By changing various properties of this object, such as the point position, you can configure the parameters for PhysicsDirectSpaceState3D.intersect_point().

**Properties**
- `bool CollideWithAreas` = `false`
- `bool CollideWithBodies` = `true`
- `int CollisionMask` = `4294967295`
- `Array[RID] Exclude` = `[]`
- `Vector3 Position` = `Vector3(0, 0, 0)`

### PhysicsRayQueryParameters2D
*Inherits: **RefCounted < Object***

By changing various properties of this object, such as the ray position, you can configure the parameters for PhysicsDirectSpaceState2D.intersect_ray().

**Properties**
- `bool CollideWithAreas` = `false`
- `bool CollideWithBodies` = `true`
- `int CollisionMask` = `4294967295`
- `Array[RID] Exclude` = `[]`
- `Vector2 From` = `Vector2(0, 0)`
- `bool HitFromInside` = `false`
- `Vector2 To` = `Vector2(0, 0)`

**Methods**
- `PhysicsRayQueryParameters2D Create(Vector2 from, Vector2 to, int collisionMask = 4294967295, Array[RID] exclude = []) [static]`

### PhysicsRayQueryParameters3D
*Inherits: **RefCounted < Object***

By changing various properties of this object, such as the ray position, you can configure the parameters for PhysicsDirectSpaceState3D.intersect_ray().

**Properties**
- `bool CollideWithAreas` = `false`
- `bool CollideWithBodies` = `true`
- `int CollisionMask` = `4294967295`
- `Array[RID] Exclude` = `[]`
- `Vector3 From` = `Vector3(0, 0, 0)`
- `bool HitBackFaces` = `true`
- `bool HitFromInside` = `false`
- `Vector3 To` = `Vector3(0, 0, 0)`

**Methods**
- `PhysicsRayQueryParameters3D Create(Vector3 from, Vector3 to, int collisionMask = 4294967295, Array[RID] exclude = []) [static]`

### PhysicsServer2DExtension
*Inherits: **PhysicsServer2D < Object***

This class extends PhysicsServer2D by providing additional virtual methods that can be overridden. When these methods are overridden, they will be called instead of the internal methods of the physics server.

**Methods**
- `void _AreaAddShape(RID area, RID shape, Transform2D transform, bool disabled) [virtual]`
- `void _AreaAttachCanvasInstanceId(RID area, int id) [virtual]`
- `void _AreaAttachObjectInstanceId(RID area, int id) [virtual]`
- `void _AreaClearShapes(RID area) [virtual]`
- `RID _AreaCreate() [virtual]`
- `int _AreaGetCanvasInstanceId(RID area) [virtual]`
- `int _AreaGetCollisionLayer(RID area) [virtual]`
- `int _AreaGetCollisionMask(RID area) [virtual]`
- `int _AreaGetObjectInstanceId(RID area) [virtual]`
- `Variant _AreaGetParam(RID area, AreaParameter param) [virtual]`
- `RID _AreaGetShape(RID area, int shapeIdx) [virtual]`
- `int _AreaGetShapeCount(RID area) [virtual]`
- `Transform2D _AreaGetShapeTransform(RID area, int shapeIdx) [virtual]`
- `RID _AreaGetSpace(RID area) [virtual]`
- `Transform2D _AreaGetTransform(RID area) [virtual]`
- `void _AreaRemoveShape(RID area, int shapeIdx) [virtual]`
- `void _AreaSetAreaMonitorCallback(RID area, Callable callback) [virtual]`
- `void _AreaSetCollisionLayer(RID area, int layer) [virtual]`
- `void _AreaSetCollisionMask(RID area, int mask) [virtual]`
- `void _AreaSetMonitorCallback(RID area, Callable callback) [virtual]`
- `void _AreaSetMonitorable(RID area, bool monitorable) [virtual]`
- `void _AreaSetParam(RID area, AreaParameter param, Variant value) [virtual]`
- `void _AreaSetPickable(RID area, bool pickable) [virtual]`
- `void _AreaSetShape(RID area, int shapeIdx, RID shape) [virtual]`
- `void _AreaSetShapeDisabled(RID area, int shapeIdx, bool disabled) [virtual]`
- `void _AreaSetShapeTransform(RID area, int shapeIdx, Transform2D transform) [virtual]`
- `void _AreaSetSpace(RID area, RID space) [virtual]`
- `void _AreaSetTransform(RID area, Transform2D transform) [virtual]`
- `void _BodyAddCollisionException(RID body, RID exceptedBody) [virtual]`
- `void _BodyAddConstantCentralForce(RID body, Vector2 force) [virtual]`
- `void _BodyAddConstantForce(RID body, Vector2 force, Vector2 position) [virtual]`
- `void _BodyAddConstantTorque(RID body, float torque) [virtual]`
- `void _BodyAddShape(RID body, RID shape, Transform2D transform, bool disabled) [virtual]`
- `void _BodyApplyCentralForce(RID body, Vector2 force) [virtual]`
- `void _BodyApplyCentralImpulse(RID body, Vector2 impulse) [virtual]`
- `void _BodyApplyForce(RID body, Vector2 force, Vector2 position) [virtual]`
- `void _BodyApplyImpulse(RID body, Vector2 impulse, Vector2 position) [virtual]`
- `void _BodyApplyTorque(RID body, float torque) [virtual]`
- `void _BodyApplyTorqueImpulse(RID body, float impulse) [virtual]`
- `void _BodyAttachCanvasInstanceId(RID body, int id) [virtual]`

### PhysicsServer2DManager
*Inherits: **Object***

PhysicsServer2DManager is the API for registering PhysicsServer2D implementations and for setting the default implementation.

**Methods**
- `void RegisterServer(string name, Callable createCallback)`
- `void SetDefaultServer(string name, int priority)`

### PhysicsServer2D
*Inherits: **Object** | Inherited by: PhysicsServer2DExtension*

PhysicsServer2D is the server responsible for all 2D physics. It can directly create and manipulate all physics objects:

**Methods**
- `void AreaAddShape(RID area, RID shape, Transform2D transform = Transform2D(1, 0, 0, 1, 0, 0), bool disabled = false)`
- `void AreaAttachCanvasInstanceId(RID area, int id)`
- `void AreaAttachObjectInstanceId(RID area, int id)`
- `void AreaClearShapes(RID area)`
- `RID AreaCreate()`
- `int AreaGetCanvasInstanceId(RID area)`
- `int AreaGetCollisionLayer(RID area)`
- `int AreaGetCollisionMask(RID area)`
- `int AreaGetObjectInstanceId(RID area)`
- `Variant AreaGetParam(RID area, AreaParameter param)`
- `RID AreaGetShape(RID area, int shapeIdx)`
- `int AreaGetShapeCount(RID area)`
- `Transform2D AreaGetShapeTransform(RID area, int shapeIdx)`
- `RID AreaGetSpace(RID area)`
- `Transform2D AreaGetTransform(RID area)`
- `void AreaRemoveShape(RID area, int shapeIdx)`
- `void AreaSetAreaMonitorCallback(RID area, Callable callback)`
- `void AreaSetCollisionLayer(RID area, int layer)`
- `void AreaSetCollisionMask(RID area, int mask)`
- `void AreaSetMonitorCallback(RID area, Callable callback)`
- `void AreaSetMonitorable(RID area, bool monitorable)`
- `void AreaSetParam(RID area, AreaParameter param, Variant value)`
- `void AreaSetShape(RID area, int shapeIdx, RID shape)`
- `void AreaSetShapeDisabled(RID area, int shapeIdx, bool disabled)`
- `void AreaSetShapeTransform(RID area, int shapeIdx, Transform2D transform)`
- `void AreaSetSpace(RID area, RID space)`
- `void AreaSetTransform(RID area, Transform2D transform)`
- `void BodyAddCollisionException(RID body, RID exceptedBody)`
- `void BodyAddConstantCentralForce(RID body, Vector2 force)`
- `void BodyAddConstantForce(RID body, Vector2 force, Vector2 position = Vector2(0, 0))`
- `void BodyAddConstantTorque(RID body, float torque)`
- `void BodyAddShape(RID body, RID shape, Transform2D transform = Transform2D(1, 0, 0, 1, 0, 0), bool disabled = false)`
- `void BodyApplyCentralForce(RID body, Vector2 force)`
- `void BodyApplyCentralImpulse(RID body, Vector2 impulse)`
- `void BodyApplyForce(RID body, Vector2 force, Vector2 position = Vector2(0, 0))`
- `void BodyApplyImpulse(RID body, Vector2 impulse, Vector2 position = Vector2(0, 0))`
- `void BodyApplyTorque(RID body, float torque)`
- `void BodyApplyTorqueImpulse(RID body, float impulse)`
- `void BodyAttachCanvasInstanceId(RID body, int id)`
- `void BodyAttachObjectInstanceId(RID body, int id)`

### PhysicsServer3DExtension
*Inherits: **PhysicsServer3D < Object***

This class extends PhysicsServer3D by providing additional virtual methods that can be overridden. When these methods are overridden, they will be called instead of the internal methods of the physics server.

**Methods**
- `void _AreaAddShape(RID area, RID shape, Transform3D transform, bool disabled) [virtual]`
- `void _AreaAttachObjectInstanceId(RID area, int id) [virtual]`
- `void _AreaClearShapes(RID area) [virtual]`
- `RID _AreaCreate() [virtual]`
- `int _AreaGetCollisionLayer(RID area) [virtual]`
- `int _AreaGetCollisionMask(RID area) [virtual]`
- `int _AreaGetObjectInstanceId(RID area) [virtual]`
- `Variant _AreaGetParam(RID area, AreaParameter param) [virtual]`
- `RID _AreaGetShape(RID area, int shapeIdx) [virtual]`
- `int _AreaGetShapeCount(RID area) [virtual]`
- `Transform3D _AreaGetShapeTransform(RID area, int shapeIdx) [virtual]`
- `RID _AreaGetSpace(RID area) [virtual]`
- `Transform3D _AreaGetTransform(RID area) [virtual]`
- `void _AreaRemoveShape(RID area, int shapeIdx) [virtual]`
- `void _AreaSetAreaMonitorCallback(RID area, Callable callback) [virtual]`
- `void _AreaSetCollisionLayer(RID area, int layer) [virtual]`
- `void _AreaSetCollisionMask(RID area, int mask) [virtual]`
- `void _AreaSetMonitorCallback(RID area, Callable callback) [virtual]`
- `void _AreaSetMonitorable(RID area, bool monitorable) [virtual]`
- `void _AreaSetParam(RID area, AreaParameter param, Variant value) [virtual]`
- `void _AreaSetRayPickable(RID area, bool enable) [virtual]`
- `void _AreaSetShape(RID area, int shapeIdx, RID shape) [virtual]`
- `void _AreaSetShapeDisabled(RID area, int shapeIdx, bool disabled) [virtual]`
- `void _AreaSetShapeTransform(RID area, int shapeIdx, Transform3D transform) [virtual]`
- `void _AreaSetSpace(RID area, RID space) [virtual]`
- `void _AreaSetTransform(RID area, Transform3D transform) [virtual]`
- `void _BodyAddCollisionException(RID body, RID exceptedBody) [virtual]`
- `void _BodyAddConstantCentralForce(RID body, Vector3 force) [virtual]`
- `void _BodyAddConstantForce(RID body, Vector3 force, Vector3 position) [virtual]`
- `void _BodyAddConstantTorque(RID body, Vector3 torque) [virtual]`
- `void _BodyAddShape(RID body, RID shape, Transform3D transform, bool disabled) [virtual]`
- `void _BodyApplyCentralForce(RID body, Vector3 force) [virtual]`
- `void _BodyApplyCentralImpulse(RID body, Vector3 impulse) [virtual]`
- `void _BodyApplyForce(RID body, Vector3 force, Vector3 position) [virtual]`
- `void _BodyApplyImpulse(RID body, Vector3 impulse, Vector3 position) [virtual]`
- `void _BodyApplyTorque(RID body, Vector3 torque) [virtual]`
- `void _BodyApplyTorqueImpulse(RID body, Vector3 impulse) [virtual]`
- `void _BodyAttachObjectInstanceId(RID body, int id) [virtual]`
- `void _BodyClearShapes(RID body) [virtual]`
- `RID _BodyCreate() [virtual]`

### PhysicsServer3DManager
*Inherits: **Object***

PhysicsServer3DManager is the API for registering PhysicsServer3D implementations and for setting the default implementation.

**Methods**
- `void RegisterServer(string name, Callable createCallback)`
- `void SetDefaultServer(string name, int priority)`

### PhysicsServer3DRenderingServerHandler
*Inherits: **Object***

A class used to provide PhysicsServer3DExtension._soft_body_update_rendering_server() with a rendering handler for soft bodies.

**Methods**
- `void _SetAabb(AABB aabb) [virtual]`
- `void _SetNormal(int vertexId, Vector3 normal) [virtual]`
- `void _SetVertex(int vertexId, Vector3 vertex) [virtual]`
- `void SetAabb(AABB aabb)`
- `void SetNormal(int vertexId, Vector3 normal)`
- `void SetVertex(int vertexId, Vector3 vertex)`

### PhysicsServer3D
*Inherits: **Object** | Inherited by: PhysicsServer3DExtension*

PhysicsServer3D is the server responsible for all 3D physics. It can directly create and manipulate all physics objects:

**Methods**
- `void AreaAddShape(RID area, RID shape, Transform3D transform = Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0), bool disabled = false)`
- `void AreaAttachObjectInstanceId(RID area, int id)`
- `void AreaClearShapes(RID area)`
- `RID AreaCreate()`
- `int AreaGetCollisionLayer(RID area)`
- `int AreaGetCollisionMask(RID area)`
- `int AreaGetObjectInstanceId(RID area)`
- `Variant AreaGetParam(RID area, AreaParameter param)`
- `RID AreaGetShape(RID area, int shapeIdx)`
- `int AreaGetShapeCount(RID area)`
- `Transform3D AreaGetShapeTransform(RID area, int shapeIdx)`
- `RID AreaGetSpace(RID area)`
- `Transform3D AreaGetTransform(RID area)`
- `void AreaRemoveShape(RID area, int shapeIdx)`
- `void AreaSetAreaMonitorCallback(RID area, Callable callback)`
- `void AreaSetCollisionLayer(RID area, int layer)`
- `void AreaSetCollisionMask(RID area, int mask)`
- `void AreaSetMonitorCallback(RID area, Callable callback)`
- `void AreaSetMonitorable(RID area, bool monitorable)`
- `void AreaSetParam(RID area, AreaParameter param, Variant value)`
- `void AreaSetRayPickable(RID area, bool enable)`
- `void AreaSetShape(RID area, int shapeIdx, RID shape)`
- `void AreaSetShapeDisabled(RID area, int shapeIdx, bool disabled)`
- `void AreaSetShapeTransform(RID area, int shapeIdx, Transform3D transform)`
- `void AreaSetSpace(RID area, RID space)`
- `void AreaSetTransform(RID area, Transform3D transform)`
- `void BodyAddCollisionException(RID body, RID exceptedBody)`
- `void BodyAddConstantCentralForce(RID body, Vector3 force)`
- `void BodyAddConstantForce(RID body, Vector3 force, Vector3 position = Vector3(0, 0, 0))`
- `void BodyAddConstantTorque(RID body, Vector3 torque)`
- `void BodyAddShape(RID body, RID shape, Transform3D transform = Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0), bool disabled = false)`
- `void BodyApplyCentralForce(RID body, Vector3 force)`
- `void BodyApplyCentralImpulse(RID body, Vector3 impulse)`
- `void BodyApplyForce(RID body, Vector3 force, Vector3 position = Vector3(0, 0, 0))`
- `void BodyApplyImpulse(RID body, Vector3 impulse, Vector3 position = Vector3(0, 0, 0))`
- `void BodyApplyTorque(RID body, Vector3 torque)`
- `void BodyApplyTorqueImpulse(RID body, Vector3 impulse)`
- `void BodyAttachObjectInstanceId(RID body, int id)`
- `void BodyClearShapes(RID body)`
- `RID BodyCreate()`

### PhysicsShapeQueryParameters2D
*Inherits: **RefCounted < Object***

By changing various properties of this object, such as the shape, you can configure the parameters for PhysicsDirectSpaceState2D's methods.

**Properties**
- `bool CollideWithAreas` = `false`
- `bool CollideWithBodies` = `true`
- `int CollisionMask` = `4294967295`
- `Array[RID] Exclude` = `[]`
- `float Margin` = `0.0`
- `Vector2 Motion` = `Vector2(0, 0)`
- `Resource Shape`
- `RID ShapeRid` = `RID()`
- `Transform2D Transform` = `Transform2D(1, 0, 0, 1, 0, 0)`

**C# Examples**
```csharp
RID shapeRid = PhysicsServer2D.CircleShapeCreate();
int radius = 64;
PhysicsServer2D.ShapeSetData(shapeRid, radius);

var params = new PhysicsShapeQueryParameters2D();
params.ShapeRid = shapeRid;

// Execute physics queries here...

// Release the shape when done with physics queries.
PhysicsServer2D.FreeRid(shapeRid);
```

### PhysicsShapeQueryParameters3D
*Inherits: **RefCounted < Object***

By changing various properties of this object, such as the shape, you can configure the parameters for PhysicsDirectSpaceState3D's methods.

**Properties**
- `bool CollideWithAreas` = `false`
- `bool CollideWithBodies` = `true`
- `int CollisionMask` = `4294967295`
- `Array[RID] Exclude` = `[]`
- `float Margin` = `0.0`
- `Vector3 Motion` = `Vector3(0, 0, 0)`
- `Resource Shape`
- `RID ShapeRid` = `RID()`
- `Transform3D Transform` = `Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0)`

**C# Examples**
```csharp
RID shapeRid = PhysicsServer3D.SphereShapeCreate();
float radius = 2.0f;
PhysicsServer3D.ShapeSetData(shapeRid, radius);

var params = new PhysicsShapeQueryParameters3D();
params.ShapeRid = shapeRid;

// Execute physics queries here...

// Release the shape when done with physics queries.
PhysicsServer3D.FreeRid(shapeRid);
```

### PhysicsTestMotionParameters2D
*Inherits: **RefCounted < Object***

By changing various properties of this object, such as the motion, you can configure the parameters for PhysicsServer2D.body_test_motion().

**Properties**
- `bool CollideSeparationRay` = `false`
- `Array[RID] ExcludeBodies` = `[]`
- `Array[int] ExcludeObjects` = `[]`
- `Transform2D From` = `Transform2D(1, 0, 0, 1, 0, 0)`
- `float Margin` = `0.08`
- `Vector2 Motion` = `Vector2(0, 0)`
- `bool RecoveryAsCollision` = `false`

### PhysicsTestMotionParameters3D
*Inherits: **RefCounted < Object***

By changing various properties of this object, such as the motion, you can configure the parameters for PhysicsServer3D.body_test_motion().

**Properties**
- `bool CollideSeparationRay` = `false`
- `Array[RID] ExcludeBodies` = `[]`
- `Array[int] ExcludeObjects` = `[]`
- `Transform3D From` = `Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0)`
- `float Margin` = `0.001`
- `int MaxCollisions` = `1`
- `Vector3 Motion` = `Vector3(0, 0, 0)`
- `bool RecoveryAsCollision` = `false`

### PhysicsTestMotionResult2D
*Inherits: **RefCounted < Object***

Describes the motion and collision result from PhysicsServer2D.body_test_motion().

**Methods**
- `Object GetCollider()`
- `int GetColliderId()`
- `RID GetColliderRid()`
- `int GetColliderShape()`
- `Vector2 GetColliderVelocity()`
- `float GetCollisionDepth()`
- `int GetCollisionLocalShape()`
- `Vector2 GetCollisionNormal()`
- `Vector2 GetCollisionPoint()`
- `float GetCollisionSafeFraction()`
- `float GetCollisionUnsafeFraction()`
- `Vector2 GetRemainder()`
- `Vector2 GetTravel()`

### PhysicsTestMotionResult3D
*Inherits: **RefCounted < Object***

Describes the motion and collision result from PhysicsServer3D.body_test_motion().

**Methods**
- `Object GetCollider(int collisionIndex = 0)`
- `int GetColliderId(int collisionIndex = 0)`
- `RID GetColliderRid(int collisionIndex = 0)`
- `int GetColliderShape(int collisionIndex = 0)`
- `Vector3 GetColliderVelocity(int collisionIndex = 0)`
- `int GetCollisionCount()`
- `float GetCollisionDepth(int collisionIndex = 0)`
- `int GetCollisionLocalShape(int collisionIndex = 0)`
- `Vector3 GetCollisionNormal(int collisionIndex = 0)`
- `Vector3 GetCollisionPoint(int collisionIndex = 0)`
- `float GetCollisionSafeFraction()`
- `float GetCollisionUnsafeFraction()`
- `Vector3 GetRemainder()`
- `Vector3 GetTravel()`

### PinJoint3D
*Inherits: **Joint3D < Node3D < Node < Object***

A physics joint that attaches two 3D physics bodies at a single point, allowing them to freely rotate. For example, a RigidBody3D can be attached to a StaticBody3D to create a pendulum or a seesaw.

**Properties**
- `float Params/bias` = `0.3`
- `float Params/damping` = `1.0`
- `float Params/impulseClamp` = `0.0`

**Methods**
- `float GetParam(Param param)`
- `void SetParam(Param param, float value)`

### Shape2D
*Inherits: **Resource < RefCounted < Object** | Inherited by: CapsuleShape2D, CircleShape2D, ConcavePolygonShape2D, ConvexPolygonShape2D, RectangleShape2D, SegmentShape2D, ...*

Abstract base class for all 2D shapes, intended for use in physics.

**Properties**
- `float CustomSolverBias` = `0.0`

**Methods**
- `bool Collide(Transform2D localXform, Shape2D withShape, Transform2D shapeXform)`
- `PackedVector2Array CollideAndGetContacts(Transform2D localXform, Shape2D withShape, Transform2D shapeXform)`
- `bool CollideWithMotion(Transform2D localXform, Vector2 localMotion, Shape2D withShape, Transform2D shapeXform, Vector2 shapeMotion)`
- `PackedVector2Array CollideWithMotionAndGetContacts(Transform2D localXform, Vector2 localMotion, Shape2D withShape, Transform2D shapeXform, Vector2 shapeMotion)`
- `void Draw(RID canvasItem, Color color)`
- `Rect2 GetRect()`

### Shape3D
*Inherits: **Resource < RefCounted < Object** | Inherited by: BoxShape3D, CapsuleShape3D, ConcavePolygonShape3D, ConvexPolygonShape3D, CylinderShape3D, HeightMapShape3D, ...*

Abstract base class for all 3D shapes, intended for use in physics.

**Properties**
- `float CustomSolverBias` = `0.0`
- `float Margin` = `0.04`

**Methods**
- `ArrayMesh GetDebugMesh()`

### SliderJoint3D
*Inherits: **Joint3D < Node3D < Node < Object***

A physics joint that restricts the movement of a 3D physics body along an axis relative to another physics body. For example, Body A could be a StaticBody3D representing a piston base, while Body B could be a RigidBody3D representing the piston head, moving up and down.

**Properties**
- `float AngularLimit/damping` = `0.0`
- `float AngularLimit/lowerAngle` = `0.0`
- `float AngularLimit/restitution` = `0.7`
- `float AngularLimit/softness` = `1.0`
- `float AngularLimit/upperAngle` = `0.0`
- `float AngularMotion/damping` = `1.0`
- `float AngularMotion/restitution` = `0.7`
- `float AngularMotion/softness` = `1.0`
- `float AngularOrtho/damping` = `1.0`
- `float AngularOrtho/restitution` = `0.7`
- `float AngularOrtho/softness` = `1.0`
- `float LinearLimit/damping` = `1.0`
- `float LinearLimit/lowerDistance` = `-1.0`
- `float LinearLimit/restitution` = `0.7`
- `float LinearLimit/softness` = `1.0`
- `float LinearLimit/upperDistance` = `1.0`
- `float LinearMotion/damping` = `0.0`
- `float LinearMotion/restitution` = `0.7`
- `float LinearMotion/softness` = `1.0`
- `float LinearOrtho/damping` = `1.0`
- `float LinearOrtho/restitution` = `0.7`
- `float LinearOrtho/softness` = `1.0`

**Methods**
- `float GetParam(Param param)`
- `void SetParam(Param param, float value)`
