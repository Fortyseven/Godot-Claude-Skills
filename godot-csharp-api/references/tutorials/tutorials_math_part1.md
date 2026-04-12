# Godot 4 C# Tutorials — Math (Part 1)

> 4 tutorials. C#-specific code examples.

## Beziers, curves and paths

Bezier curves are a mathematical approximation of natural geometric shapes. We use them to represent a curve with as little information as possible and with a high level of flexibility.

Unlike more abstract mathematical concepts, Bezier curves were created for industrial design. They are a popular tool in the graphics software industry.

They rely on interpolation, which we saw in the previous article, combining multiple steps to create smooth curves. To better understand how Bezier curves work, let's start from its simplest form: Quadratic Bezier.

### Quadratic Bezier

Take three points, the minimum required for Quadratic Bezier to work:

To draw a curve between them, we first interpolate gradually over the two vertices of each of the two segments formed by the three points, using values ranging from 0 to 1. This gives us two points that move along the segments as we change the value of `t` from 0 to 1.

```csharp
private Vector2 QuadraticBezier(Vector2 p0, Vector2 p1, Vector2 p2, float t)
{
    Vector2 q0 = p0.Lerp(p1, t);
    Vector2 q1 = p1.Lerp(p2, t);
}
```

We then interpolate `q0` and `q1` to obtain a single point `r` that moves along a curve.

```csharp
Vector2 r = q0.Lerp(q1, t);
return r;
```

This type of curve is called a _Quadratic Bezier_ curve.

_(Image credit: Wikipedia)_

### Cubic Bezier

Building upon the previous example, we can get more control by interpolating between four points.

We first use a function with four parameters to take four points as an input, `p0`, `p1`, `p2` and `p3`:

```csharp
public Vector2 CubicBezier(Vector2 p0, Vector2 p1, Vector2 p2, Vector2 p3, float t)
{

}
```

We apply a linear interpolation to each couple of points to reduce them to three:

```csharp
Vector2 q0 = p0.Lerp(p1, t);
Vector2 q1 = p1.Lerp(p2, t);
Vector2 q2 = p2.Lerp(p3, t);
```

We then take our three points and reduce them to two:

```csharp
Vector2 r0 = q0.Lerp(q1, t);
Vector2 r1 = q1.Lerp(q2, t);
```

And to one:

```csharp
Vector2 s = r0.Lerp(r1, t);
return s;
```

Here is the full function:

```csharp
private Vector2 CubicBezier(Vector2 p0, Vector2 p1, Vector2 p2, Vector2 p3, float t)
{
    Vector2 q0 = p0.Lerp(p1, t);
    Vector2 q1 = p1.Lerp(p2, t);
    Vector2 q2 = p2.Lerp(p3, t);

    Vector2 r0 = q0.Lerp(q1, t);
    Vector2 r1 = q1.Lerp(q2, t);

    Vector2 s = r0.Lerp(r1, t);
    return s;
}
```

The result will be a smooth curve interpolating between all four points:

_(Image credit: Wikipedia)_

> **Note:** Cubic Bezier interpolation works the same in 3D, just use `Vector3` instead of `Vector2`.

### Adding control points

Building upon Cubic Bezier, we can change the way two of the points work to control the shape of our curve freely. Instead of having `p0`, `p1`, `p2` and `p3`, we will store them as:

- `point0 = p0`: Is the first point, the source
- `control0 = p1 - p0`: Is a vector relative to the first control point
- `control1 = p3 - p2`: Is a vector relative to the second control point
- `point1 = p3`: Is the second point, the destination

This way, we have two points and two control points which are relative vectors to the respective points. If you've used graphics or animation software before, this might look familiar:

This is how graphics software presents Bezier curves to the users, and how they work and look in Godot.

### Curve2D, Curve3D, Path and Path2D

There are two objects that contain curves: [Curve3D](../godot_csharp_resources.md) and [Curve2D](../godot_csharp_resources.md) (for 3D and 2D respectively).

They can contain several points, allowing for longer paths. It is also possible to set them to nodes: [Path3D](../godot_csharp_nodes_3d.md) and [Path2D](../godot_csharp_nodes_2d.md) (also for 3D and 2D respectively):

Using them, however, may not be completely obvious, so following is a description of the most common use cases for Bezier curves.

### Evaluating

Only evaluating them may be an option, but in most cases it's not very useful. The big drawback with Bezier curves is that if you traverse them at constant speed, from `t = 0` to `t = 1`, the actual interpolation will _not_ move at constant speed. The speed is also an interpolation between the distances between points `p0`, `p1`, `p2` and `p3` and there is not a mathematically simple way to traverse the curve at constant speed.

Let's do an example with the following pseudocode:

```csharp
private float _t = 0.0f;

public override void _Process(double delta)
{
    _t += (float)delta;
    Position = CubicBezier(p0, p1, p2, p3, _t);
}
```

As you can see, the speed (in pixels per second) of the circle varies, even though `t` is increased at constant speed. This makes beziers difficult to use for anything practical out of the box.

### Drawing

Drawing beziers (or objects based on the curve) is a very common use case, but it's also not easy. For pretty much any case, Bezier curves need to be converted to some sort of segments. This is normally difficult, however, without creating a very high amount of them.

The reason is that some sections of a curve (specifically, corners) may require considerable amounts of points, while other sections may not:

Additionally, if both control points were `0, 0` (remember they are relative vectors), the Bezier curve would just be a straight line (so drawing a high amount of points would be wasteful).

Before drawing Bezier curves, _tessellation_ is required. This is often done with a recursive or divide and conquer function that splits the curve until the curvature amount becomes less than a certain threshold.

The _Curve_ classes provide this via the [Curve2D.tessellate()](../godot_csharp_resources.md) function (which receives optional `stages` of recursion and angle `tolerance` arguments). This way, drawing something based on a curve is easier.

### Traversal

The last common use case for the curves is to traverse them. Because of what was mentioned before regarding constant speed, this is also difficult.

To make this easier, the curves need to be _baked_ into equidistant points. This way, they can be approximated with regular interpolation (which can be improved further with a cubic option). To do this, just use the [Curve3D.sample_baked()](../godot_csharp_resources.md) method together with [Curve2D.get_baked_length()](../godot_csharp_resources.md). The first call to either of them will bake the curve internally.

Traversal at constant speed, then, can be done with the following pseudo-code:

```csharp
private float _t = 0.0f;

public override void _Process(double delta)
{
    _t += (float)delta;
    Position = curve.SampleBaked(_t * curve.GetBakedLength(), true);
}
```

And the output will, then, move at constant speed:

---

## Interpolation

Interpolation is a common operation in graphics programming, which is used to blend or transition between two values. Interpolation can also be used to smooth movement, rotation, etc. It's good to become familiar with it in order to expand your horizons as a game developer.

The basic idea is that you want to transition from A to B. A value `t`, represents the states in-between.

For example, if `t` is 0, then the state is A. If `t` is 1, then the state is B. Anything in-between is an _interpolation_.

Between two real (floating-point) numbers, an interpolation can be described as:

And often simplified to:

The name of this type of interpolation, which transforms a value into another at _constant speed_ is _"linear"_. So, when you hear about _Linear Interpolation_, you know they are referring to this formula.

There are other types of interpolations, which will not be covered here. A recommended read afterwards is the Bezier page.

### Vector interpolation

Vector types ([Vector2](../godot_csharp_math_types.md) and [Vector3](../godot_csharp_math_types.md)) can also be interpolated, they come with handy functions to do it [Vector2.lerp()](../godot_csharp_math_types.md) and [Vector3.lerp()](../godot_csharp_math_types.md).

For cubic interpolation, there are also [Vector2.cubic_interpolate()](../godot_csharp_math_types.md) and [Vector3.cubic_interpolate()](../godot_csharp_math_types.md), which do a Bezier style interpolation.

Here is example pseudo-code for going from point A to B using interpolation:

```csharp
private float _t = 0.0f;

public override void _PhysicsProcess(double delta)
{
    _t += (float)delta * 0.4f;

    Marker2D a = GetNode<Marker2D>("A");
    Marker2D b = GetNode<Marker2D>("B");
    Sprite2D sprite = GetNode<Sprite2D>("Sprite2D");

    sprite.Position = a.Position.Lerp(b.Position, _t);
}
```

It will produce the following motion:

### Transform interpolation

It is also possible to interpolate whole transforms (make sure they have either uniform scale or, at least, the same non-uniform scale). For this, the function [Transform3D.interpolate_with()](../godot_csharp_math_types.md) can be used.

Here is an example of transforming a monkey from Position1 to Position2:

Using the following pseudocode:

```csharp
private float _t = 0.0f;

public override void _PhysicsProcess(double delta)
{
    _t += (float)delta;

    Marker3D p1 = GetNode<Marker3D>("Position1");
    Marker3D p2 = GetNode<Marker3D>("Position2");
    CSGMesh3D monkey = GetNode<CSGMesh3D>("Monkey");

    monkey.Transform = p1.Transform.InterpolateWith(p2.Transform, _t);
}
```

And again, it will produce the following motion:

### Smoothing motion

Interpolation can be used to smoothly follow a moving target value, such as a position or a rotation. Each frame, `lerp()` moves the current value towards the target value by a fixed percentage of the remaining difference between the values. The current value will smoothly move towards the target, slowing down as it gets closer. Here is an example of a circle following the mouse using interpolation smoothing:

```csharp
private const float FollowSpeed = 4.0f;

public override void _PhysicsProcess(double delta)
{
    Vector2 mousePos = GetLocalMousePosition();

    Sprite2D sprite = GetNode<Sprite2D>("Sprite2D");

    sprite.Position = sprite.Position.Lerp(mousePos, (float)delta * FollowSpeed);
}
```

Here is how it looks:

This is useful for smoothing camera movement, for allies following the player (ensuring they stay within a certain range), and for many other common game patterns.

> **Note:** Despite using `delta`, the formula used above is framerate-dependent, because the `weight` parameter of `lerp()` represents a _percentage_ of the remaining difference in values, not an _absolute amount to change_. In `_physics_process()`, this is usually fine because physics is expected to maintain a constant framerate, and therefore `delta` is expected to remain constant. For a framerate-independent version of interpolation smoothing that can also be used in `process()`, use the following formula instead: ```csharp
> private const float FollowSpeed = 4.0f;

public override void \_Process(double delta)
{
Vector2 mousePos = GetLocalMousePosition();

    Sprite2D sprite = GetNode<Sprite2D>("Sprite2D");
    float weight = 1f - Mathf.Exp(-FollowSpeed * (float)delta);
    sprite.Position = sprite.Position.Lerp(mousePos, weight);

}

````Deriving this formula is beyond the scope of this page. For an explanation, see [Improved Lerp Smoothing](https://www.gamedeveloper.com/programming/improved-lerp-smoothing-) or watch [Lerp smoothing is broken](https://www.youtube.com/watch?v=LSNQuFEDOyQ).

---

## Matrices and transforms

### Introduction



Before reading this tutorial, we recommend that you thoroughly read and understand the Vector math tutorial, as this tutorial requires a knowledge of vectors.



This tutorial is about *transformations* and how we represent them in Godot using matrices. It is not a full in-depth guide to matrices. Transformations are most of the time applied as translation, rotation, and scale, so we will focus on how to represent those with matrices.



Most of this guide focuses on 2D, using [Transform2D](../godot_csharp_math_types.md) and [Vector2](../godot_csharp_math_types.md), but the way things work in 3D is very similar.



> **Note:** As mentioned in the previous tutorial, it is important to remember that in Godot, the Y axis points *down* in 2D. This is the opposite of how most schools teach linear algebra, with the Y axis pointing up.



> **Note:** The convention is that the X axis is red, the Y axis is green, and the Z axis is blue. This tutorial is color-coded to match these conventions, but we will also represent the origin vector with a blue color.



#### Matrix components and the Identity matrix



The identity matrix represents a transform with no translation, no rotation, and no scale. Let's start by looking at the identity matrix and how its components relate to how it visually appears.



Matrices have rows and columns, and a transformation matrix has specific conventions on what each does.



In the image above, we can see that the red X vector is represented by the first column of the matrix, and the green Y vector is likewise represented by the second column. A change to the columns will change these vectors. We will see how they can be manipulated in the next few examples.



You should not worry about manipulating rows directly, as we usually work with columns. However, you can think of the rows of the matrix as showing which vectors contribute to moving in a given direction.



When we refer to a value such as `t.x.y`, that's the Y component of the X column vector. In other words, the bottom-left of the matrix. Similarly, `t.x.x` is top-left, `t.y.x` is top-right, and `t.y.y` is bottom-right, where `t` is the Transform2D.



#### Scaling the transformation matrix



Applying a scale is one of the easiest operations to understand. Let's start by placing the Godot logo underneath our vectors so that we can visually see the effects on an object:



Now, to scale the matrix, all we need to do is multiply each component by the scale we want. Let's scale it up by 2. 1 times 2 becomes 2, and 0 times 2 becomes 0, so we end up with this:



To do this in code, we multiply each of the vectors:


```csharp
Transform2D t = Transform2D.Identity;
// Scale
t.X *= 2;
t.Y *= 2;
Transform = t; // Change the node's transform to what we calculated.
````

If we wanted to return it to its original scale, we can multiply each component by 0.5. That's pretty much all there is to scaling a transformation matrix.

To calculate the object's scale from an existing transformation matrix, you can use `length()` on each of the column vectors.

> **Note:** In actual projects, you can use the `scaled()` method to perform scaling.

#### Rotating the transformation matrix

We'll start the same way as earlier, with the Godot logo underneath the identity matrix:

As an example, let's say we want to rotate our Godot logo clockwise by 90 degrees. Right now the X axis points right and the Y axis points down. If we rotate these in our head, we would logically see that the new X axis should point down and the new Y axis should point left.

You can imagine that you grab both the Godot logo and its vectors, and then spin it around the center. Wherever you finish spinning, the orientation of the vectors determines what the matrix is.

We need to represent "down" and "left" in normal coordinates, so means we'll set X to (0, 1) and Y to (-1, 0). These are also the values of `Vector2.DOWN` and `Vector2.LEFT`. When we do this, we get the desired result of rotating the object:

If you have trouble understanding the above, try this exercise: Cut a square of paper, draw X and Y vectors on top of it, place it on graph paper, then rotate it and note the endpoints.

To perform rotation in code, we need to be able to calculate the values programmatically. This image shows the formulas needed to calculate the transformation matrix from a rotation angle. Don't worry if this part seems complicated, I promise it's the hardest thing you need to know.

> **Note:** Godot represents all rotations with radians, not degrees. A full turn is TAU or PI\*2 radians, and a quarter turn of 90 degrees is TAU/4 or PI/2 radians. Working with TAU usually results in more readable code.

> **Note:** Fun fact: In addition to Y being _down_ in Godot, rotation is represented clockwise. This means that all the math and trig functions behave the same as a Y-is-up CCW system, since these differences "cancel out". You can think of rotations in both systems being "from X to Y".

In order to perform a rotation of 0.5 radians (about 28.65 degrees), we plug in a value of 0.5 to the formula above and evaluate to find what the actual values should be:

Here's how that would be done in code (place the script on a Node2D):

```csharp
float rot = 0.5f; // The rotation to apply.
Transform2D t = Transform2D.Identity;
t.X.X = t.Y.Y = Mathf.Cos(rot);
t.X.Y = t.Y.X = Mathf.Sin(rot);
t.Y.X *= -1;
Transform = t; // Change the node's transform to what we calculated.
```

To calculate the object's rotation from an existing transformation matrix, you can use `atan2(t.x.y, t.x.x)`, where t is the Transform2D.

> **Note:** In actual projects, you can use the `rotated()` method to perform rotations.

#### Basis of the transformation matrix

So far we have only been working with the `x` and `y`, vectors, which are in charge of representing rotation, scale, and/or shearing (advanced, covered at the end). The X and Y vectors are together called the _basis_ of the transformation matrix. The terms "basis" and "basis vectors" are important to know.

You might have noticed that [Transform2D](../godot_csharp_math_types.md) actually has three [Vector2](../godot_csharp_math_types.md) values: `x`, `y`, and `origin`. The `origin` value is not part of the basis, but it is part of the transform, and we need it to represent position. From now on we'll keep track of the origin vector in all examples. You can think of origin as another column, but it's often better to think of it as completely separate.

Note that in 3D, Godot has a separate [Basis](../godot_csharp_math_types.md) structure for holding the three [Vector3](../godot_csharp_math_types.md) values of the basis, since the code can get complex and it makes sense to separate it from [Transform3D](../godot_csharp_math_types.md) (which is composed of one [Basis](../godot_csharp_math_types.md) and one extra [Vector3](../godot_csharp_math_types.md) for the origin).

#### Translating the transformation matrix

Changing the `origin` vector is called _translating_ the transformation matrix. Translating is basically a technical term for "moving" the object, but it explicitly does not involve any rotation.

Let's work through an example to help understand this. We will start with the identity transform like last time, except we will keep track of the origin vector this time.

If we want to move the object to a position of (1, 2), we need to set its `origin` vector to (1, 2):

There is also a `translated_local()` method, which performs a different operation to adding or changing `origin` directly. The `translated_local()` method will translate the object _relative to its own rotation_. For example, an object rotated 90 degrees clockwise will move to the right when `translated_local()` with `Vector2.UP`. To translate _relative to the global/parent frame_ use `translated()` instead.

> **Note:** Godot's 2D uses coordinates based on pixels, so in actual projects you will want to translate by hundreds of units.

#### Putting it all together

We're going to apply everything we mentioned so far onto one transform. To follow along, create a project with a Sprite2D node and use the Godot logo for the texture resource.

Let's set the translation to (350, 150), rotate by -0.5 rad, and scale by 3. I've posted a screenshot, and the code to reproduce it, but I encourage you to try and reproduce the screenshot without looking at the code!

```csharp
Transform2D t = Transform2D.Identity;
// Translation
t.Origin = new Vector2(350, 150);
// Rotation
float rot = -0.5f; // The rotation to apply.
t.X.X = t.Y.Y = Mathf.Cos(rot);
t.X.Y = t.Y.X = Mathf.Sin(rot);
t.Y.X *= -1;
// Scale
t.X *= 3;
t.Y *= 3;
Transform = t; // Change the node's transform to what we calculated.
```

#### Shearing the transformation matrix (advanced)

> **Note:** If you are only looking for how to _use_ transformation matrices, feel free to skip this section of the tutorial. This section explores an uncommonly used aspect of transformation matrices for the purpose of building an understanding of them. Node2D provides a shearing property out of the box.

You may have noticed that a transform has more degrees of freedom than the combination of the above actions. The basis of a 2D transformation matrix has four total numbers in two [Vector2](../godot_csharp_math_types.md) values, while a rotation value and a Vector2 for scale only has 3 numbers. The high-level concept for the missing degree of freedom is called _shearing_.

Normally, you will always have the basis vectors perpendicular to each other. However, shearing can be useful in some situations, and understanding shearing helps you understand how transforms work.

To show you visually how it will look, let's overlay a grid onto the Godot logo:

Each point on this grid is obtained by adding the basis vectors together. The bottom-right corner is X + Y, while the top-right corner is X - Y. If we change the basis vectors, the entire grid moves with it, as the grid is composed of the basis vectors. All lines on the grid that are currently parallel will remain parallel no matter what changes we make to the basis vectors.

As an example, let's set Y to (1, 1):

```csharp
Transform2D t = Transform2D.Identity;
// Shear by setting Y to (1, 1)
t.Y = Vector2.One;
Transform = t; // Change the node's transform to what we calculated.
```

> **Note:** You can't set the raw values of a Transform2D in the editor, so you _must_ use code if you want to shear the object.

Due to the vectors no longer being perpendicular, the object has been sheared. The bottom-center of the grid, which is (0, 1) relative to itself, is now located at a world position of (1, 1).

The intra-object coordinates are called UV coordinates in textures, so let's borrow that terminology for here. To find the world position from a relative position, the formula is U _ X + V _ Y, where U and V are numbers and X and Y are the basis vectors.

The bottom-right corner of the grid, which is always at the UV position of (1, 1), is at the world position of (2, 1), which is calculated from X*1 + Y*1, which is (1, 0) + (1, 1), or (1 + 1, 0 + 1), or (2, 1). This matches up with our observation of where the bottom-right corner of the image is.

Similarly, the top-right corner of the grid, which is always at the UV position of (1, -1), is at the world position of (0, -1), which is calculated from X*1 + Y*-1, which is (1, 0) - (1, 1), or (1 - 1, 0 - 1), or (0, -1). This matches up with our observation of where the top-right corner of the image is.

Hopefully you now fully understand how a transformation matrix affects the object, and the relationship between the basis vectors and how the object's "UV" or "intra-coordinates" have their world position changed.

> **Note:** In Godot, all transform math is done relative to the parent node. When we refer to "world position", that would be relative to the node's parent instead, if the node had a parent.

If you would like additional explanation, you should check out 3Blue1Brown's excellent video about linear transformations: [https://www.youtube.com/watch?v=kYB8IZa5AuE](https://www.youtube.com/watch?v=kYB8IZa5AuE)

### Practical applications of transforms

In actual projects, you will usually be working with transforms inside transforms by having multiple [Node2D](../godot_csharp_nodes_2d.md) or [Node3D](../godot_csharp_nodes_3d.md) nodes parented to each other.

However, it's useful to understand how to manually calculate the values we need. We will go over how you could use [Transform2D](../godot_csharp_math_types.md) or [Transform3D](../godot_csharp_math_types.md) to manually calculate transforms of nodes.

#### Converting positions between transforms

There are many cases where you'd want to convert a position in and out of a transform. For example, if you have a position relative to the player and would like to find the world (parent-relative) position, or if you have a world position and want to know where it is relative to the player.

We can find what a vector relative to the player would be defined in world space as using the `*` operator:

```csharp
// World space vector 100 units below the player.
GD.Print(Transform * new Vector2(0, 100));
```

And we can use the `*` operator in the opposite order to find a what world space position would be if it was defined relative to the player:

```csharp
// Where is (0, 100) relative to the player?
GD.Print(new Vector2(0, 100) * Transform);
```

> **Note:** If you know in advance that the transform is positioned at (0, 0), you can use the "basis_xform" or "basis_xform_inv" methods instead, which skip dealing with translation.

#### Moving an object relative to itself

A common operation, especially in 3D games, is to move an object relative to itself. For example, in first-person shooter games, you would want the character to move forward (-Z axis) when you press W.

Since the basis vectors are the orientation relative to the parent, and the origin vector is the position relative to the parent, we can add multiples of the basis vectors to move an object relative to itself.

This code moves an object 100 units to its own right:

```csharp
Transform2D t = Transform;
t.Origin += t.X * 100;
Transform = t;
```

For moving in 3D, you would need to replace "x" with "basis.x".

> **Note:** In actual projects, you can use `translate_object_local` in 3D or `move_local_x` and `move_local_y` in 2D to do this.

#### Applying transforms onto transforms

One of the most important things to know about transforms is how you can use several of them together. A parent node's transform affects all of its children. Let's dissect an example.

In this image, the child node has a "2" after the component names to distinguish them from the parent node. It might look a bit overwhelming with so many numbers, but remember that each number is displayed twice (next to the arrows and also in the matrices), and that almost half of the numbers are zero.

The only transformations going on here are that the parent node has been given a scale of (2, 1), the child has been given a scale of (0.5, 0.5), and both nodes have been given positions.

All child transformations are affected by the parent transformations. The child has a scale of (0.5, 0.5), so you would expect it to be a 1:1 ratio square, and it is, but only relative to the parent. The child's X vector ends up being (1, 0) in world space, because it is scaled by the parent's basis vectors. Similarly, the child node's `origin` vector is set to (1, 1), but this actually moves it (2, 1) in world space, due to the parent node's basis vectors.

To calculate a child transform's world space transform manually, this is the code we would use:

```csharp
// Set up transforms like in the image, except make positions be 100 times bigger.
Transform2D parent = new Transform2D(2, 0, 0, 1, 100, 200);
Transform2D child = new Transform2D(0.5f, 0, 0, 0.5f, 100, 100);

// Calculate the child's world space transform
// origin = (2, 0) * 100 + (0, 1) * 100 + (100, 200)
Vector2 origin = parent.X * child.Origin.X + parent.Y * child.Origin.Y + parent.Origin;
// basisX = (2, 0) * 0.5 + (0, 1) * 0 = (0.5, 0)
Vector2 basisX = parent.X * child.X.X + parent.Y * child.X.Y;
// basisY = (2, 0) * 0 + (0, 1) * 0.5 = (0.5, 0)
Vector2 basisY = parent.X * child.Y.X + parent.Y * child.Y.Y;

// Change the node's transform to what we calculated.
Transform = new Transform2D(basisX, basisY, origin);
```

In actual projects, we can find the world transform of the child by applying one transform onto another using the `*` operator:

```csharp
// Set up transforms like in the image, except make positions be 100 times bigger.
Transform2D parent = new Transform2D(2, 0, 0, 1, 100, 200);
Transform2D child = new Transform2D(0.5f, 0, 0, 0.5f, 100, 100);

// Change the node's transform to what would be the child's world transform.
Transform = parent * child;
```

> **Note:** When multiplying matrices, order matters! Don't mix them up.

Lastly, applying the identity transform will always do nothing.

If you would like additional explanation, you should check out 3Blue1Brown's excellent video about matrix composition: [https://www.youtube.com/watch?v=XkY2DOUCWMU](https://www.youtube.com/watch?v=XkY2DOUCWMU)

#### Inverting a transformation matrix

The "affine_inverse" function returns a transform that "undoes" the previous transform. This can be useful in some situations. Let's take a look at a few examples.

Multiplying an inverse transform by the normal transform undoes all transformations:

```csharp
Transform2D ti = Transform.AffineInverse();
Transform2D t = ti * Transform;
// The transform is the identity transform.
```

Transforming a position by a transform and its inverse results in the same position:

```csharp
Transform2D ti = Transform.AffineInverse();
Position = Transform * Position;
Position = ti * Position;
// The position is the same as before.
```

### How does it all work in 3D?

One of the great things about transformation matrices is that they work very similarly between 2D and 3D transformations. All the code and formulas used above for 2D work the same in 3D, with 3 exceptions: the addition of a third axis, that each axis is of type [Vector3](../godot_csharp_math_types.md), and also that Godot stores the [Basis](../godot_csharp_math_types.md) separately from the [Transform3D](../godot_csharp_math_types.md), since the math can get complex and it makes sense to separate it.

All of the concepts for how translation, rotation, scale, and shearing work in 3D are all the same compared to 2D. To scale, we take each component and multiply it; to rotate, we change where each basis vector is pointing; to translate, we manipulate the origin; and to shear, we change the basis vectors to be non-perpendicular.

If you would like, it's a good idea to play around with transforms to get an understanding of how they work. Godot allows you to edit 3D transform matrices directly from the inspector. You can download this project which has colored lines and cubes to help visualize the [Basis](../godot_csharp_math_types.md) vectors and the origin in both 2D and 3D: [https://github.com/godotengine/godot-demo-projects/tree/master/misc/matrix_transform](https://github.com/godotengine/godot-demo-projects/tree/master/misc/matrix_transform)

> **Note:** You cannot edit Node2D's transform matrix directly in Godot 4.0's inspector. This may be changed in a future release of Godot.

If you would like additional explanation, you should check out 3Blue1Brown's excellent video about 3D linear transformations: [https://www.youtube.com/watch?v=rHLEWRxRGiM](https://www.youtube.com/watch?v=rHLEWRxRGiM)

#### Representing rotation in 3D (advanced)

The biggest difference between 2D and 3D transformation matrices is how you represent rotation by itself without the basis vectors.

With 2D, we have an easy way (atan2) to switch between a transformation matrix and an angle. In 3D, rotation is too complex to represent as one number. There is something called Euler angles, which can represent rotations as a set of 3 numbers, however, they are limited and not very useful, except for trivial cases.

In 3D we do not typically use angles, we either use a transformation basis (used pretty much everywhere in Godot), or we use quaternions. Godot can represent quaternions using the [Quaternion](../godot_csharp_math_types.md) struct. My suggestion to you is to completely ignore how they work under-the-hood, because they are very complicated and unintuitive.

However, if you really must know how it works, here are some great resources, which you can follow in order:

[https://www.youtube.com/watch?v=mvmuCPvRoWQ](https://www.youtube.com/watch?v=mvmuCPvRoWQ)

[https://www.youtube.com/watch?v=d4EgbgTm0Bg](https://www.youtube.com/watch?v=d4EgbgTm0Bg)

[https://eater.net/quaternions](https://eater.net/quaternions)

---

## Random number generation

Many games rely on randomness to implement core game mechanics. This page guides you through common types of randomness and how to implement them in Godot.

After giving you a brief overview of useful functions that generate random numbers, you will learn how to get random elements from arrays, dictionaries, and how to use a noise generator in GDScript. Lastly, we'll take a look at cryptographically secure random number generation and how it differs from typical random number generation.

> **Note:** Computers cannot generate "true" random numbers. Instead, they rely on [pseudorandom number generators](https://en.wikipedia.org/wiki/Pseudorandom_number_generator) (PRNGs). Godot internally uses the [PCG Family](https://www.pcg-random.org/) of pseudorandom number generators.

### Global scope versus RandomNumberGenerator class

Godot exposes two ways to generate random numbers: via _global scope_ methods or using the [RandomNumberGenerator](../godot_csharp_misc.md) class.

Global scope methods are easier to set up, but they don't offer as much control.

RandomNumberGenerator requires more code to use, but allows creating multiple instances, each with their own seed and state.

This tutorial uses global scope methods, except when the method only exists in the RandomNumberGenerator class.

### The randomize() method

> **Note:** Since Godot 4.0, the random seed is automatically set to a random value when the project starts. This means you don't need to call `randomize()` in `_ready()` anymore to ensure that results are random across project runs. However, you can still use `randomize()` if you want to use a specific seed number, or generate it using a different method.

In global scope, you can find a `randomize()` method. **This method should be called only once when your project starts to initialize the random seed.** Calling it multiple times is unnecessary and may impact performance negatively.

Putting it in your main scene script's `_ready()` method is a good choice:

```csharp
public override void _Ready()
{
    GD.Randomize();
}
```

You can also set a fixed random seed instead using `seed()`. Doing so will give you _deterministic_ results across runs:

```csharp
public override void _Ready()
{
    GD.Seed(12345);
    // To use a string as a seed, you can hash it to a number.
    GD.Seed("Hello world".Hash());
}
```

When using the RandomNumberGenerator class, you should call `randomize()` on the instance since it has its own seed:

```csharp
var random = new RandomNumberGenerator();
random.Randomize();
```

### Getting a random number

Let's look at some of the most commonly used functions and methods to generate random numbers in Godot.

The function `randi()` returns a random number between `0` and `2^32 - 1`. Since the maximum value is huge, you most likely want to use the modulo operator (`%`) to bound the result between 0 and the denominator:

```csharp
// Prints a random integer between 0 and 49.
GD.Print(GD.Randi() % 50);

// Prints a random integer between 10 and 60.
GD.Print(GD.Randi() % 51 + 10);
```

`randf()` returns a random floating-point number between 0 and 1. This is useful to implement a **Weighted random probability** system, among other things.

`randfn()` returns a random floating-point number following a [normal distribution](https://en.wikipedia.org/wiki/Normal_distribution). This means the returned value is more likely to be around the mean (0.0 by default), varying by the deviation (1.0 by default):

```csharp
// Prints a random floating-point number from a normal distribution with a mean 0.0 and deviation 1.0.
GD.Print(GD.Randfn(0.0, 1.0));
```

`randf_range()` takes two arguments `from` and `to`, and returns a random floating-point number between `from` and `to`:

```csharp
// Prints a random floating-point number between -4 and 6.5.
GD.Print(GD.RandRange(-4.0, 6.5));
```

`randi_range()` takes two arguments `from` and `to`, and returns a random integer between `from` and `to`:

```csharp
// Prints a random integer number between -10 and 10.
GD.Print(GD.RandRange(-10, 10));
```

### Get a random array element

We can use random integer generation to get a random element from an array, or use the [Array.pick_random](../godot_csharp_misc.md) method to do it for us:

```csharp
// Use Godot's Array type instead of a BCL type so we can use `PickRandom()` on it.
private Godot.Collections.Array<string> _fruits = ["apple", "orange", "pear", "banana"];

public override void _Ready()
{
    for (int i = 0; i < 100; i++)
    {
        // Pick 100 fruits randomly.
        GD.Print(GetFruit());
    }

    for (int i = 0; i < 100; i++)
    {
        // Pick 100 fruits randomly, this time using the `Array.PickRandom()`
        // helper method. This has the same behavior as `GetFruit()`.
        GD.Print(_fruits.PickRandom());
    }
}

public string GetFruit()
{
    string randomFruit = _fruits[GD.Randi() % _fruits.Size()];
    // Returns "apple", "orange", "pear", or "banana" every time the code runs.
    // We may get the same fruit multiple times in a row.
    return rand
// ...
```

To prevent the same fruit from being picked more than once in a row, we can add more logic to the above method. In this case, we can't use [Array.pick_random](../godot_csharp_misc.md) since it lacks a way to prevent repetition:

```csharp
private string[] _fruits = ["apple", "orange", "pear", "banana"];
private string _lastFruit = "";

public override void _Ready()
{
    for (int i = 0; i < 100; i++)
    {
        // Pick 100 fruits randomly.
        GD.Print(GetFruit());
    }
}

public string GetFruit()
{
    string randomFruit = _fruits[GD.Randi() % _fruits.Length];
    while (randomFruit == _lastFruit)
    {
        // The last fruit was picked. Try again until we get a different fruit.
        randomFruit = _fruits[GD.Randi() % _fruits.Length];
    }

    _lastFruit = randomFruit;

    // Returns "apple", "orange", "pear", or "banana" every time the code runs.
    // The function will never return the same fruit more than once in a row.
    return randomFruit;
}
```

This approach can be useful to make random number generation feel less repetitive. Still, it doesn't prevent results from "ping-ponging" between a limited set of values. To prevent this, use the **shuffle bag** pattern instead.

### Get a random dictionary value

We can apply similar logic from arrays to dictionaries as well:

```csharp
private Godot.Collections.Dictionary<string, Godot.Collections.Dictionary<string, int>> _metals = new()
{
    {"copper", new Godot.Collections.Dictionary<string, int>{{"quantity", 50}, {"price", 50}}},
    {"silver", new Godot.Collections.Dictionary<string, int>{{"quantity", 20}, {"price", 150}}},
    {"gold", new Godot.Collections.Dictionary<string, int>{{"quantity", 3}, {"price", 500}}},
};

public override void _Ready()
{
    for (int i = 0; i < 20; i++)
    {
        GD.Print(GetMetal());
    }
}

public Godot.Collections.Dictionary<string, int> GetMetal()
{
    var (_, randomMetal) = _metals.ElementAt((int)(GD.Randi() % _metals.Count));
    // Returns a random metal value dictionary every time the code runs.
    // The same metal may be selected multiple times in succession.
    retur
// ...
```

### Weighted random probability

The `randf()` method returns a floating-point number between 0.0 and 1.0. We can use this to create a "weighted" probability where different outcomes have different likelihoods:

```csharp
public override void _Ready()
{
    for (int i = 0; i < 100; i++)
    {
        GD.Print(GetItemRarity());
    }
}

public string GetItemRarity()
{
    float randomFloat = GD.Randf();

    if (randomFloat < 0.8f)
    {
        // 80% chance of being returned.
        return "Common";
    }
    else if (randomFloat < 0.95f)
    {
        // 15% chance of being returned.
        return "Uncommon";
    }
    else
    {
        // 5% chance of being returned.
        return "Rare";
    }
}
```

You can also get a weighted random _index_ using the [rand_weighted()](../godot_csharp_misc.md) method on a RandomNumberGenerator instance. This returns a random integer between 0 and the size of the array that is passed as a parameter. Each value in the array is a floating-point number that represents the _relative_ likelihood that it will be returned as an index. A higher value means the value is more likely to be returned as an index, while a value of `0` means it will never be returned as an index.

For example, if `[0.5, 1, 1, 2]` is passed as a parameter, then the method is twice as likely to return `3` (the index of the value `2`) and twice as unlikely to return `0` (the index of the value `0.5`) compared to the indices `1` and `2`.

Since the returned value matches the array's size, it can be used as an index to get a value from another array as follows:

```csharp
// Prints a random element using the weighted index that is returned by `RandWeighted()`.
// Here, "apple" will be returned twice as rarely as "orange" and "pear".
// "banana" is twice as common as "orange" and "pear", and four times as common as "apple".
string[] fruits = ["apple", "orange", "pear", "banana"];
float[] probabilities = [0.5f, 1, 1, 2];

var random = new RandomNumberGenerator();
GD.Print(fruits[random.RandWeighted(probabilities)]);
```

### "Better" randomness using shuffle bags

Taking the same example as above, we would like to pick fruits at random. However, relying on random number generation every time a fruit is selected can lead to a less _uniform_ distribution. If the player is lucky (or unlucky), they could get the same fruit three or more times in a row.

You can accomplish this using the _shuffle bag_ pattern. It works by removing an element from the array after choosing it. After multiple selections, the array ends up empty. When that happens, you reinitialize it to its default value:

```csharp
private Godot.Collections.Array<string> _fruits = ["apple", "orange", "pear", "banana"];
// A copy of the fruits array so we can restore the original value into `fruits`.
private Godot.Collections.Array<string> _fruitsFull;

public override void _Ready()
{
    _fruitsFull = _fruits.Duplicate();
    _fruits.Shuffle();

    for (int i = 0; i < 100; i++)
    {
        GD.Print(GetFruit());
    }
}

public string GetFruit()
{
    if(_fruits.Count == 0)
    {
        // Fill the fruits array again and shuffle it.
        _fruits = _fruitsFull.Duplicate();
        _fruits.Shuffle();
    }

    // Get a random fruit, since we shuffled the array,
    string randomFruit = _fruits[0];
    // and remove it from the `_fruits` array.
    _fruits.RemoveAt(0);
    // Returns "apple", "orange", "pear", or
// ...
```

When running the above code, there is a chance to get the same fruit twice in a row. Once we picked a fruit, it will no longer be a possible return value unless the array is now empty. When the array is empty, we reset it back to its default value, making it possible to have the same fruit again, but only once.

### Random noise

The random number generation shown above can show its limits when you need a value that _slowly_ changes depending on the input. The input can be a position, time, or anything else.

To achieve this, you can use random _noise_ functions. Noise functions are especially popular in procedural generation to generate realistic-looking terrain. Godot provides [FastNoiseLite](../godot_csharp_resources.md) for this, which supports 1D, 2D and 3D noise. Here's an example with 1D noise:

```csharp
private FastNoiseLite _noise = new FastNoiseLite();

public override void _Ready()
{
    // Configure the FastNoiseLite instance.
    _noise.NoiseType = FastNoiseLite.NoiseTypeEnum.SimplexSmooth;
    _noise.Seed = (int)GD.Randi();
    _noise.FractalOctaves = 4;
    _noise.Frequency = 1.0f / 20.0f;

    for (int i = 0; i < 100; i++)
    {
        GD.Print(_noise.GetNoise1D(i));
    }
}
```

### Cryptographically secure pseudorandom number generation

So far, the approaches mentioned above are **not** suitable for _cryptographically secure_ pseudorandom number generation (CSPRNG). This is fine for games, but this is not sufficient for scenarios where encryption, authentication or signing is involved.

Godot offers a [Crypto](../godot_csharp_networking.md) class for this. This class can perform asymmetric key encryption/decryption, signing/verification, while also generating cryptographically secure random bytes, RSA keys, HMAC digests, and self-signed [X509Certificate](../godot_csharp_networking.md)s.

The downside of CSPRNG is that it's much slower than standard pseudorandom number generation. Its API is also less convenient to use. As a result, CSPRNG should be avoided for gameplay elements.

Example of using the Crypto class to generate 2 random integers between `0` and `2^32 - 1` (inclusive):

> **See also:** See [PackedByteArray](../godot_csharp_misc.md)'s documentation for other methods you can use to decode the generated bytes into various types of data, such as integers or floats.

---
