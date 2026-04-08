# Godot 4 C# API Reference — Math Types

> C#-only reference. 11 classes.

### Projection

A 4×4 matrix used for 3D projective transformations. It can represent transformations such as translation, rotation, scaling, shearing, and perspective division. It consists of four Vector4 columns.

**Properties**
- `Vector4 W` = `Vector4(0, 0, 0, 1)`
- `Vector4 X` = `Vector4(1, 0, 0, 0)`
- `Vector4 Y` = `Vector4(0, 1, 0, 0)`
- `Vector4 Z` = `Vector4(0, 0, 1, 0)`

**Methods**
- `Projection CreateDepthCorrection(bool flipY) [static]`
- `Projection CreateFitAabb(AABB aabb) [static]`
- `Projection CreateForHmd(int eye, float aspect, float intraocularDist, float displayWidth, float displayToLens, float oversample, float zNear, float zFar) [static]`
- `Projection CreateFrustum(float left, float right, float bottom, float top, float zNear, float zFar) [static]`
- `Projection CreateFrustumAspect(float size, float aspect, Vector2 offset, float zNear, float zFar, bool flipFov = false) [static]`
- `Projection CreateLightAtlasRect(Rect2 rect) [static]`
- `Projection CreateOrthogonal(float left, float right, float bottom, float top, float zNear, float zFar) [static]`
- `Projection CreateOrthogonalAspect(float size, float aspect, float zNear, float zFar, bool flipFov = false) [static]`
- `Projection CreatePerspective(float fovy, float aspect, float zNear, float zFar, bool flipFov = false) [static]`
- `Projection CreatePerspectiveHmd(float fovy, float aspect, float zNear, float zFar, bool flipFov, int eye, float intraocularDist, float convergenceDist) [static]`
- `float Determinant()`
- `Projection FlippedY()`
- `float GetAspect()`
- `Vector2 GetFarPlaneHalfExtents()`
- `float GetFov()`
- `float GetFovy(float fovx, float aspect) [static]`
- `float GetLodMultiplier()`
- `int GetPixelsPerMeter(int forPixelWidth)`
- `Plane GetProjectionPlane(int plane)`
- `Vector2 GetViewportHalfExtents()`
- `float GetZFar()`
- `float GetZNear()`
- `Projection Inverse()`
- `bool IsOrthogonal()`
- `Projection JitterOffseted(Vector2 offset)`
- `Projection PerspectiveZnearAdjusted(float newZnear)`

### Quaternion

The Quaternion built-in Variant type is a 4D data structure that represents rotation in the form of a Hamilton convention quaternion. Compared to the Basis type which can store both rotation and scale, quaternions can only store rotation.

**Properties**
- `float W` = `1.0`
- `float X` = `0.0`
- `float Y` = `0.0`
- `float Z` = `0.0`

**Methods**
- `float AngleTo(Quaternion to)`
- `float Dot(Quaternion with)`
- `Quaternion Exp()`
- `Quaternion FromEuler(Vector3 euler) [static]`
- `float GetAngle()`
- `Vector3 GetAxis()`
- `Vector3 GetEuler(int order = 2)`
- `Quaternion Inverse()`
- `bool IsEqualApprox(Quaternion to)`
- `bool IsFinite()`
- `bool IsNormalized()`
- `float Length()`
- `float LengthSquared()`
- `Quaternion Log()`
- `Quaternion Normalized()`
- `Quaternion Slerp(Quaternion to, float weight)`
- `Quaternion Slerpni(Quaternion to, float weight)`
- `Quaternion SphericalCubicInterpolate(Quaternion b, Quaternion preA, Quaternion postB, float weight)`
- `Quaternion SphericalCubicInterpolateInTime(Quaternion b, Quaternion preA, Quaternion postB, float weight, float bT, float preAT, float postBT)`

### Rect2i

The Rect2i built-in Variant type represents an axis-aligned rectangle in a 2D space, using integer coordinates. It is defined by its position and size, which are Vector2i. Because it does not rotate, it is frequently used for fast overlap tests (see intersects()).

**Properties**
- `Vector2i End` = `Vector2i(0, 0)`
- `Vector2i Position` = `Vector2i(0, 0)`
- `Vector2i Size` = `Vector2i(0, 0)`

**Methods**
- `Rect2i Abs()`
- `bool Encloses(Rect2i b)`
- `Rect2i Expand(Vector2i to)`
- `int GetArea()`
- `Vector2i GetCenter()`
- `Rect2i Grow(int amount)`
- `Rect2i GrowIndividual(int left, int top, int right, int bottom)`
- `Rect2i GrowSide(int side, int amount)`
- `bool HasArea()`
- `bool HasPoint(Vector2i point)`
- `Rect2i Intersection(Rect2i b)`
- `bool Intersects(Rect2i b)`
- `Rect2i Merge(Rect2i b)`

**C# Examples**
```csharp
var rect = new Rect2I(25, 25, -100, -50);
var absolute = rect.Abs(); // absolute is Rect2I(-75, -25, 100, 50)
```
```csharp
var rect = new Rect2I(0, 0, 5, 2);

rect = rect.Expand(new Vector2I(10, 0)); // rect is Rect2I(0, 0, 10, 2)
rect = rect.Expand(new Vector2I(-5, 5)); // rect is Rect2I(-5, 0, 15, 5)
```

### Transform2D

The Transform2D built-in Variant type is a 2×3 matrix representing a transformation in 2D space. It contains three Vector2 values: x, y, and origin. Together, they can represent translation, rotation, scale, and skew.

**Properties**
- `Vector2 Origin` = `Vector2(0, 0)`
- `Vector2 X` = `Vector2(1, 0)`
- `Vector2 Y` = `Vector2(0, 1)`

**Methods**
- `Transform2D AffineInverse()`
- `Vector2 BasisXform(Vector2 v)`
- `Vector2 BasisXformInv(Vector2 v)`
- `float Determinant()`
- `Vector2 GetOrigin()`
- `float GetRotation()`
- `Vector2 GetScale()`
- `float GetSkew()`
- `Transform2D InterpolateWith(Transform2D xform, float weight)`
- `Transform2D Inverse()`
- `bool IsConformal()`
- `bool IsEqualApprox(Transform2D xform)`
- `bool IsFinite()`
- `Transform2D LookingAt(Vector2 target = Vector2(0, 0))`
- `Transform2D Orthonormalized()`
- `Transform2D Rotated(float angle)`
- `Transform2D RotatedLocal(float angle)`
- `Transform2D Scaled(Vector2 scale)`
- `Transform2D ScaledLocal(Vector2 scale)`
- `Transform2D Translated(Vector2 offset)`
- `Transform2D TranslatedLocal(Vector2 offset)`

**C# Examples**
```csharp
var myTransform = new Transform2D(
    Vector3(2.0f, 0.0f),
    Vector3(0.0f, 4.0f),
    Vector3(0.0f, 0.0f)
);
// Rotating the Transform2D in any way preserves its scale.
myTransform = myTransform.Rotated(Mathf.Tau / 2.0f);

GD.Print(myTransform.GetScale()); // Prints (2, 4)
```

### Transform3D

The Transform3D built-in Variant type is a 3×4 matrix representing a transformation in 3D space. It contains a Basis, which on its own can represent rotation, scale, and shear. Additionally, combined with its own origin, the transform can also represent a translation.

**Properties**
- `Basis Basis` = `Basis(1, 0, 0, 0, 1, 0, 0, 0, 1)`
- `Vector3 Origin` = `Vector3(0, 0, 0)`

**Methods**
- `Transform3D AffineInverse()`
- `Transform3D InterpolateWith(Transform3D xform, float weight)`
- `Transform3D Inverse()`
- `bool IsEqualApprox(Transform3D xform)`
- `bool IsFinite()`
- `Transform3D LookingAt(Vector3 target, Vector3 up = Vector3(0, 1, 0), bool useModelFront = false)`
- `Transform3D Orthonormalized()`
- `Transform3D Rotated(Vector3 axis, float angle)`
- `Transform3D RotatedLocal(Vector3 axis, float angle)`
- `Transform3D Scaled(Vector3 scale)`
- `Transform3D ScaledLocal(Vector3 scale)`
- `Transform3D Translated(Vector3 offset)`
- `Transform3D TranslatedLocal(Vector3 offset)`

### Vector2i

A 2-element structure that can be used to represent 2D grid coordinates or any other pair of integers.

**Properties**
- `int X` = `0`
- `int Y` = `0`

**Methods**
- `Vector2i Abs()`
- `float Aspect()`
- `Vector2i Clamp(Vector2i min, Vector2i max)`
- `Vector2i Clampi(int min, int max)`
- `int DistanceSquaredTo(Vector2i to)`
- `float DistanceTo(Vector2i to)`
- `float Length()`
- `int LengthSquared()`
- `Vector2i Max(Vector2i with)`
- `int MaxAxisIndex()`
- `Vector2i Maxi(int with)`
- `Vector2i Min(Vector2i with)`
- `int MinAxisIndex()`
- `Vector2i Mini(int with)`
- `Vector2i Sign()`
- `Vector2i Snapped(Vector2i step)`
- `Vector2i Snappedi(int step)`

### Vector2

A 2-element structure that can be used to represent 2D coordinates or any other pair of numeric values.

**Properties**
- `float X` = `0.0`
- `float Y` = `0.0`

**Methods**
- `Vector2 Abs()`
- `float Angle()`
- `float AngleTo(Vector2 to)`
- `float AngleToPoint(Vector2 to)`
- `float Aspect()`
- `Vector2 BezierDerivative(Vector2 control1, Vector2 control2, Vector2 end, float t)`
- `Vector2 BezierInterpolate(Vector2 control1, Vector2 control2, Vector2 end, float t)`
- `Vector2 Bounce(Vector2 n)`
- `Vector2 Ceil()`
- `Vector2 Clamp(Vector2 min, Vector2 max)`
- `Vector2 Clampf(float min, float max)`
- `float Cross(Vector2 with)`
- `Vector2 CubicInterpolate(Vector2 b, Vector2 preA, Vector2 postB, float weight)`
- `Vector2 CubicInterpolateInTime(Vector2 b, Vector2 preA, Vector2 postB, float weight, float bT, float preAT, float postBT)`
- `Vector2 DirectionTo(Vector2 to)`
- `float DistanceSquaredTo(Vector2 to)`
- `float DistanceTo(Vector2 to)`
- `float Dot(Vector2 with)`
- `Vector2 Floor()`
- `Vector2 FromAngle(float angle) [static]`
- `bool IsEqualApprox(Vector2 to)`
- `bool IsFinite()`
- `bool IsNormalized()`
- `bool IsZeroApprox()`
- `float Length()`
- `float LengthSquared()`
- `Vector2 Lerp(Vector2 to, float weight)`
- `Vector2 LimitLength(float length = 1.0)`
- `Vector2 Max(Vector2 with)`
- `int MaxAxisIndex()`
- `Vector2 Maxf(float with)`
- `Vector2 Min(Vector2 with)`
- `int MinAxisIndex()`
- `Vector2 Minf(float with)`
- `Vector2 MoveToward(Vector2 to, float delta)`
- `Vector2 Normalized()`
- `Vector2 Orthogonal()`
- `Vector2 Posmod(float mod)`
- `Vector2 Posmodv(Vector2 modv)`
- `Vector2 Project(Vector2 b)`

### Vector3i

A 3-element structure that can be used to represent 3D grid coordinates or any other triplet of integers.

**Properties**
- `int X` = `0`
- `int Y` = `0`
- `int Z` = `0`

**Methods**
- `Vector3i Abs()`
- `Vector3i Clamp(Vector3i min, Vector3i max)`
- `Vector3i Clampi(int min, int max)`
- `int DistanceSquaredTo(Vector3i to)`
- `float DistanceTo(Vector3i to)`
- `float Length()`
- `int LengthSquared()`
- `Vector3i Max(Vector3i with)`
- `int MaxAxisIndex()`
- `Vector3i Maxi(int with)`
- `Vector3i Min(Vector3i with)`
- `int MinAxisIndex()`
- `Vector3i Mini(int with)`
- `Vector3i Sign()`
- `Vector3i Snapped(Vector3i step)`
- `Vector3i Snappedi(int step)`

### Vector3

A 3-element structure that can be used to represent 3D coordinates or any other triplet of numeric values.

**Properties**
- `float X` = `0.0`
- `float Y` = `0.0`
- `float Z` = `0.0`

**Methods**
- `Vector3 Abs()`
- `float AngleTo(Vector3 to)`
- `Vector3 BezierDerivative(Vector3 control1, Vector3 control2, Vector3 end, float t)`
- `Vector3 BezierInterpolate(Vector3 control1, Vector3 control2, Vector3 end, float t)`
- `Vector3 Bounce(Vector3 n)`
- `Vector3 Ceil()`
- `Vector3 Clamp(Vector3 min, Vector3 max)`
- `Vector3 Clampf(float min, float max)`
- `Vector3 Cross(Vector3 with)`
- `Vector3 CubicInterpolate(Vector3 b, Vector3 preA, Vector3 postB, float weight)`
- `Vector3 CubicInterpolateInTime(Vector3 b, Vector3 preA, Vector3 postB, float weight, float bT, float preAT, float postBT)`
- `Vector3 DirectionTo(Vector3 to)`
- `float DistanceSquaredTo(Vector3 to)`
- `float DistanceTo(Vector3 to)`
- `float Dot(Vector3 with)`
- `Vector3 Floor()`
- `Vector3 Inverse()`
- `bool IsEqualApprox(Vector3 to)`
- `bool IsFinite()`
- `bool IsNormalized()`
- `bool IsZeroApprox()`
- `float Length()`
- `float LengthSquared()`
- `Vector3 Lerp(Vector3 to, float weight)`
- `Vector3 LimitLength(float length = 1.0)`
- `Vector3 Max(Vector3 with)`
- `int MaxAxisIndex()`
- `Vector3 Maxf(float with)`
- `Vector3 Min(Vector3 with)`
- `int MinAxisIndex()`
- `Vector3 Minf(float with)`
- `Vector3 MoveToward(Vector3 to, float delta)`
- `Vector3 Normalized()`
- `Vector3 OctahedronDecode(Vector2 uv) [static]`
- `Vector2 OctahedronEncode()`
- `Basis Outer(Vector3 with)`
- `Vector3 Posmod(float mod)`
- `Vector3 Posmodv(Vector3 modv)`
- `Vector3 Project(Vector3 b)`
- `Vector3 Reflect(Vector3 n)`

### Vector4i

A 4-element structure that can be used to represent 4D grid coordinates or any other quadruplet of integers.

**Properties**
- `int W` = `0`
- `int X` = `0`
- `int Y` = `0`
- `int Z` = `0`

**Methods**
- `Vector4i Abs()`
- `Vector4i Clamp(Vector4i min, Vector4i max)`
- `Vector4i Clampi(int min, int max)`
- `int DistanceSquaredTo(Vector4i to)`
- `float DistanceTo(Vector4i to)`
- `float Length()`
- `int LengthSquared()`
- `Vector4i Max(Vector4i with)`
- `int MaxAxisIndex()`
- `Vector4i Maxi(int with)`
- `Vector4i Min(Vector4i with)`
- `int MinAxisIndex()`
- `Vector4i Mini(int with)`
- `Vector4i Sign()`
- `Vector4i Snapped(Vector4i step)`
- `Vector4i Snappedi(int step)`

### Vector4

A 4-element structure that can be used to represent 4D coordinates or any other quadruplet of numeric values.

**Properties**
- `float W` = `0.0`
- `float X` = `0.0`
- `float Y` = `0.0`
- `float Z` = `0.0`

**Methods**
- `Vector4 Abs()`
- `Vector4 Ceil()`
- `Vector4 Clamp(Vector4 min, Vector4 max)`
- `Vector4 Clampf(float min, float max)`
- `Vector4 CubicInterpolate(Vector4 b, Vector4 preA, Vector4 postB, float weight)`
- `Vector4 CubicInterpolateInTime(Vector4 b, Vector4 preA, Vector4 postB, float weight, float bT, float preAT, float postBT)`
- `Vector4 DirectionTo(Vector4 to)`
- `float DistanceSquaredTo(Vector4 to)`
- `float DistanceTo(Vector4 to)`
- `float Dot(Vector4 with)`
- `Vector4 Floor()`
- `Vector4 Inverse()`
- `bool IsEqualApprox(Vector4 to)`
- `bool IsFinite()`
- `bool IsNormalized()`
- `bool IsZeroApprox()`
- `float Length()`
- `float LengthSquared()`
- `Vector4 Lerp(Vector4 to, float weight)`
- `Vector4 Max(Vector4 with)`
- `int MaxAxisIndex()`
- `Vector4 Maxf(float with)`
- `Vector4 Min(Vector4 with)`
- `int MinAxisIndex()`
- `Vector4 Minf(float with)`
- `Vector4 Normalized()`
- `Vector4 Posmod(float mod)`
- `Vector4 Posmodv(Vector4 modv)`
- `Vector4 Round()`
- `Vector4 Sign()`
- `Vector4 Snapped(Vector4 step)`
- `Vector4 Snappedf(float step)`
