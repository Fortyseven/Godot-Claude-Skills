# Godot 4 GDScript Tutorials — Math (Part 2)

> 2 tutorials. GDScript-specific code examples.

## Vector math

### Introduction

This tutorial is a short and practical introduction to linear algebra as it applies to game development. Linear algebra is the study of vectors and their uses. Vectors have many applications in both 2D and 3D development and Godot uses them extensively. Developing a good understanding of vector math is essential to becoming a strong game developer.

> **Note:** This tutorial is **not** a formal textbook on linear algebra. We will only be looking at how it is applied to game development. For a broader look at the mathematics, see [https://www.khanacademy.org/math/linear-algebra](https://www.khanacademy.org/math/linear-algebra)

### Coordinate systems (2D)

In 2D space, coordinates are defined using a horizontal axis (`x`) and a vertical axis (`y`). A particular position in 2D space is written as a pair of values such as `(4, 3)`.

> **Note:** If you're new to computer graphics, it might seem odd that the positive `y` axis points **downwards** instead of upwards, as you probably learned in math class. However, this is common in most computer graphics applications.

Any position in the 2D plane can be identified by a pair of numbers in this way. However, we can also think of the position `(4, 3)` as an **offset** from the `(0, 0)` point, or **origin**. Draw an arrow pointing from the origin to the point:

This is a **vector**. A vector represents a lot of useful information. As well as telling us that the point is at `(4, 3)`, we can also think of it as an angle `θ` (theta) and a length (or magnitude) `m`. In this case, the arrow is a **position vector** - it denotes a position in space, relative to the origin.

A very important point to consider about vectors is that they only represent **relative** direction and magnitude. There is no concept of a vector's position. The following two vectors are identical:

Both vectors represent a point 4 units to the right and 3 units below some starting point. It does not matter where on the plane you draw the vector, it always represents a relative direction and magnitude.

### Vector operations

You can use either method (x and y coordinates or angle and magnitude) to refer to a vector, but for convenience, programmers typically use the coordinate notation. For example, in Godot, the origin is the top-left corner of the screen, so to place a 2D node named `Node2D` 400 pixels to the right and 300 pixels down, use the following code:

```gdscript
$Node2D.position = Vector2(400, 300)
```

Godot supports both [Vector2](../godot_gdscript_math_types.md) and [Vector3](../godot_gdscript_math_types.md) for 2D and 3D usage, respectively. The same mathematical rules discussed in this article apply to both types, and wherever we link to `Vector2` methods in the class reference, you can also check out their `Vector3` counterparts.

#### Member access

The individual components of the vector can be accessed directly by name.

```gdscript
# Create a vector with coordinates (2, 5).
var a = Vector2(2, 5)
# Create a vector and assign x and y manually.
var b = Vector2()
b.x = 3
b.y = 1
```

#### Adding vectors

When adding or subtracting two vectors, the corresponding components are added:

```gdscript
var c = a + b  # (2, 5) + (3, 1) = (5, 6)
```

We can also see this visually by adding the second vector at the end of the first:

Note that adding `a + b` gives the same result as `b + a`.

#### Scalar multiplication

> **Note:** Vectors represent both direction and magnitude. A value representing only magnitude is called a **scalar**. Scalars use the [float](../godot_gdscript_misc.md) type in Godot.

A vector can be multiplied by a **scalar**:

```gdscript
var c = a * 2  # (2, 5) * 2 = (4, 10)
var d = b / 3  # (3, 6) / 3 = (1, 2)
var e = d * -2 # (1, 2) * -2 = (-2, -4)
```

> **Note:** Multiplying a vector by a positive scalar does not change its direction, only its magnitude. Multiplying with a negative scalar results in a vector in the opposite direction. This is how you **scale** a vector.

### Practical applications

Let's look at two common uses for vector addition and subtraction.

#### Movement

A vector can represent **any** quantity with a magnitude and direction. Typical examples are: position, velocity, acceleration, and force. In this image, the spaceship at step 1 has a position vector of `(1, 3)` and a velocity vector of `(2, 1)`. The velocity vector represents how far the ship moves each step. We can find the position for step 2 by adding the velocity to the current position.

> **Tip:** Velocity measures the **change** in position per unit of time. The new position is found by adding the velocity multiplied by the elapsed time (here assumed to be one unit, e.g. 1 s) to the previous position. In a typical 2D game scenario, you would have a velocity in pixels per second, and multiply it by the `delta` parameter (time elapsed since the previous frame) from the [\_process()](../godot_gdscript_misc.md) or [\_physics_process()](../godot_gdscript_misc.md) callbacks.

#### Pointing toward a target

In this scenario, you have a tank that wishes to point its turret at a robot. Subtracting the tank's position from the robot's position gives the vector pointing from the tank to the robot.

> **Tip:** To find a vector pointing from `A` to `B`, use `B - A`.

### Unit vectors

A vector with **magnitude** of `1` is called a **unit vector**. They are also sometimes referred to as **direction vectors** or **normals**. Unit vectors are helpful when you need to keep track of a direction.

#### Normalization

**Normalizing** a vector means reducing its length to `1` while preserving its direction. This is done by dividing each of its components by its magnitude. Because this is such a common operation, Godot provides a dedicated [normalized()](../godot_gdscript_misc.md) method for this:

```gdscript
a = a.normalized()
```

> **Warning:** Because normalization involves dividing by the vector's length, you cannot normalize a vector of length `0`. Attempting to do so would normally result in an error. In GDScript though, trying to call the `normalized()` method on a vector of length 0 leaves the value untouched and avoids the error for you.

#### Reflection

A common use of unit vectors is to indicate **normals**. Normal vectors are unit vectors aligned perpendicularly to a surface, defining its direction. They are commonly used for lighting, collisions, and other operations involving surfaces.

For example, imagine we have a moving ball that we want to bounce off a wall or other object:

The surface normal has a value of `(0, -1)` because this is a horizontal surface. When the ball collides, we take its remaining motion (the amount left over when it hits the surface) and reflect it using the normal. In Godot, there is a [bounce()](../godot_gdscript_misc.md) method to handle this. Here is a code example of the above diagram using a [CharacterBody2D](../godot_gdscript_nodes_2d.md):

```gdscript
var collision: KinematicCollision2D = move_and_collide(velocity * delta)
if collision:
    var reflect = collision.get_remainder().bounce(collision.get_normal())
    velocity = velocity.bounce(collision.get_normal())
    move_and_collide(reflect)
```

### Dot product

The **dot product** is one of the most important concepts in vector math, but is often misunderstood. Dot product is an operation on two vectors that returns a **scalar**. Unlike a vector, which contains both magnitude and direction, a scalar value has only magnitude.

The formula for dot product takes two common forms:

and

The mathematical notation _||A||_ represents the magnitude of vector `A`, and *A*x means the `x` component of vector `A`.

However, in most cases it is easiest to use the built-in [dot()](../godot_gdscript_misc.md) method. Note that the order of the two vectors does not matter:

```gdscript
var c = a.dot(b)
var d = b.dot(a)  # These are equivalent.
```

The dot product is most useful when used with unit vectors, making the first formula reduce to just `cos(θ)`. This means we can use the dot product to tell us something about the angle between two vectors:

When using unit vectors, the result will always be between `-1` (180°) and `1` (0°).

#### Facing

We can use this fact to detect whether an object is facing toward another object. In the diagram below, the player `P` is trying to avoid the zombies `A` and `B`. Assuming a zombie's field of view is **180°**, can they see the player?

The green arrows `fA` and `fB` are **unit vectors** representing the zombie's facing direction and the blue semicircle represents its field of view. For zombie `A`, we find the direction vector `AP` pointing to the player using `P - A` and normalize it, however, Godot has a helper method to do this called [direction_to()](../godot_gdscript_misc.md). If the angle between this vector and the facing vector is less than 90°, then the zombie can see the player.

In code it would look like this:

```gdscript
var AP = A.direction_to(P)
if AP.dot(fA) > 0:
    print("A sees P!")
```

### Cross product

Like the dot product, the **cross product** is an operation on two vectors. However, the result of the cross product is a vector with a direction that is perpendicular to both. Its magnitude depends on their relative angle. If two vectors are parallel, the result of their cross product will be a null vector.

The cross product is calculated like this:

```gdscript
var c = Vector3()
c.x = (a.y * b.z) - (a.z * b.y)
c.y = (a.z * b.x) - (a.x * b.z)
c.z = (a.x * b.y) - (a.y * b.x)
```

With Godot, you can use the built-in [Vector3.cross()](../godot_gdscript_math_types.md) method:

```gdscript
var c = a.cross(b)
```

The cross product is not mathematically defined in 2D. The [Vector2.cross()](../godot_gdscript_math_types.md) method is a commonly used analog of the 3D cross product for 2D vectors.

> **Note:** In the cross product, order matters. `a.cross(b)` does not give the same result as `b.cross(a)`. The resulting vectors point in **opposite** directions.

#### Calculating normals

One common use of cross products is to find the surface normal of a plane or surface in 3D space. If we have the triangle `ABC` we can use vector subtraction to find two edges `AB` and `AC`. Using the cross product, `AB × AC` produces a vector perpendicular to both: the surface normal.

Here is a function to calculate a triangle's normal:

```gdscript
func get_triangle_normal(a, b, c):
    # Find the surface normal given 3 vertices.
    var side1 = b - a
    var side2 = c - a
    var normal = side1.cross(side2)
    return normal
```

#### Pointing to a target

In the dot product section above, we saw how it could be used to find the angle between two vectors. However, in 3D, this is not enough information. We also need to know what axis to rotate around. We can find that by calculating the cross product of the current facing direction and the target direction. The resulting perpendicular vector is the axis of rotation.

### More information

For more information on using vector math in Godot, see the following articles:

- Advanced vector math
- Matrices and transforms

---

## Advanced vector math

### Planes

The dot product has another interesting property with unit vectors. Imagine that perpendicular to that vector (and through the origin) passes a plane. Planes divide the entire space into positive (over the plane) and negative (under the plane), and (contrary to popular belief) you can also use their math in 2D:

Unit vectors that are perpendicular to a surface (so, they describe the orientation of the surface) are called **unit normal vectors**. Though, usually they are just abbreviated as _normals_. Normals appear in planes, 3D geometry (to determine where each face or vertex is siding), etc. A **normal** _is_ a **unit vector**, but it's called _normal_ because of its usage. (Just like we call (0,0) the Origin!).

The plane passes by the origin and the surface of it is perpendicular to the unit vector (or _normal_). The side the vector points to is the positive half-space, while the other side is the negative half-space. In 3D this is exactly the same, except that the plane is an infinite surface (imagine an infinite, flat sheet of paper that you can orient and is pinned to the origin) instead of a line.

#### Distance to plane

Now that it's clear what a plane is, let's go back to the dot product. The dot product between a **unit vector** and any **point in space** (yes, this time we do dot product between vector and position), returns the **distance from the point to the plane**:

```gdscript
var distance = normal.dot(point)
```

But not just the absolute distance, if the point is in the negative half space the distance will be negative, too:

This allows us to tell which side of the plane a point is.

#### Away from the origin

I know what you are thinking! So far this is nice, but _real_ planes are everywhere in space, not only passing through the origin. You want real _plane_ action and you want it _now_.

Remember that planes not only split space in two, but they also have _polarity_. This means that it is possible to have perfectly overlapping planes, but their negative and positive half-spaces are swapped.

With this in mind, let's describe a full plane as a **normal** _N_ and a **distance from the origin** scalar _D_. Thus, our plane is represented by N and D. For example:

For 3D math, Godot provides a [Plane](../godot_gdscript_math_types.md) built-in type that handles this.

Basically, N and D can represent any plane in space, be it for 2D or 3D (depending on the amount of dimensions of N) and the math is the same for both. It's the same as before, but D is the distance from the origin to the plane, travelling in N direction. As an example, imagine you want to reach a point in the plane, you will just do:

```gdscript
var point_in_plane = N*D
```

This will stretch (resize) the normal vector and make it touch the plane. This math might seem confusing, but it's actually much simpler than it seems. If we want to tell, again, the distance from the point to the plane, we do the same but adjusting for distance:

```gdscript
var distance = N.dot(point) - D
```

The same thing, using a built-in function:

```gdscript
var distance = plane.distance_to(point)
```

This will, again, return either a positive or negative distance.

Flipping the polarity of the plane can be done by negating both N and D. This will result in a plane in the same position, but with inverted negative and positive half spaces:

```gdscript
N = -N
D = -D
```

Godot also implements this operator in [Plane](../godot_gdscript_math_types.md). So, using the format below will work as expected:

```gdscript
var inverted_plane = -plane
```

So, remember, the plane's main practical use is that we can calculate the distance to it. So, when is it useful to calculate the distance from a point to a plane? Let's see some examples.

#### Constructing a plane in 2D

Planes clearly don't come out of nowhere, so they must be built. Constructing them in 2D is easy, this can be done from either a normal (unit vector) and a point, or from two points in space.

In the case of a normal and a point, most of the work is done, as the normal is already computed, so calculate D from the dot product of the normal and the point.

```gdscript
var N = normal
var D = normal.dot(point)
```

For two points in space, there are actually two planes that pass through them, sharing the same space but with normal pointing to the opposite directions. To compute the normal from the two points, the direction vector must be obtained first, and then it needs to be rotated 90 degrees to either side:

```gdscript
# Calculate vector from `a` to `b`.
var dvec = point_a.direction_to(point_b)
# Rotate 90 degrees.
var normal = Vector2(dvec.y, -dvec.x)
# Alternatively (depending the desired side of the normal):
# var normal = Vector2(-dvec.y, dvec.x)
```

The rest is the same as the previous example. Either point_a or point_b will work, as they are in the same plane:

```gdscript
var N = normal
var D = normal.dot(point_a)
# this works the same
# var D = normal.dot(point_b)
```

Doing the same in 3D is a little more complex and is explained further down.

#### Some examples of planes

Here is an example of what planes are useful for. Imagine you have a [convex](https://www.mathsisfun.com/definitions/convex.html) polygon. For example, a rectangle, a trapezoid, a triangle, or just any polygon where no faces bend inwards.

For every segment of the polygon, we compute the plane that passes by that segment. Once we have the list of planes, we can do neat things, for example checking if a point is inside the polygon.

We go through all planes, if we can find a plane where the distance to the point is positive, then the point is outside the polygon. If we can't, then the point is inside.

Code should be something like this:

```gdscript
var inside = true
for p in planes:
    # check if distance to plane is positive
    if (p.distance_to(point) > 0):
        inside = false
        break # with one that fails, it's enough
```

Pretty cool, huh? But this gets much better! With a little more effort, similar logic will let us know when two convex polygons are overlapping too. This is called the Separating Axis Theorem (or SAT) and most physics engines use this to detect collision.

With a point, just checking if a plane returns a positive distance is enough to tell if the point is outside. With another polygon, we must find a plane where _all_ _the_ _other_ _polygon_ _points_ return a positive distance to it. This check is performed with the planes of A against the points of B, and then with the planes of B against the points of A:

Code should be something like this:

```gdscript
var overlapping = true

for p in planes_of_A:
    var all_out = true
    for v in points_of_B:
        if (p.distance_to(v) < 0):
            all_out = false
            break

    if (all_out):
        # a separating plane was found
        # do not continue testing
        overlapping = false
        break

if (overlapping):
    # only do this check if no separating plane
    # was found in planes of A
    for p in planes_of_B:
        var all_out = true
        for v in points_of_A:
            if (p.distance_to(v) < 0):
                all_out = false
                break

        if (all_out):
            overlapping = false
            break

if (overlapping):
    print("Polygons Collided!")
```

As you can see, planes are quite useful, and this is the tip of the iceberg. You might be wondering what happens with non convex polygons. This is usually just handled by splitting the concave polygon into smaller convex polygons, or using a technique such as BSP (which is not used much nowadays).

### Collision detection in 3D

This is another bonus bit, a reward for being patient and keeping up with this long tutorial. Here is another piece of wisdom. This might not be something with a direct use case (Godot already does collision detection pretty well) but it's used by almost all physics engines and collision detection libraries :)

Remember that converting a convex shape in 2D to an array of 2D planes was useful for collision detection? You could detect if a point was inside any convex shape, or if two 2D convex shapes were overlapping.

Well, this works in 3D too, if two 3D polyhedral shapes are colliding, you won't be able to find a separating plane. If a separating plane is found, then the shapes are definitely not colliding.

To refresh a bit a separating plane means that all vertices of polygon A are in one side of the plane, and all vertices of polygon B are in the other side. This plane is always one of the face-planes of either polygon A or polygon B.

In 3D though, there is a problem to this approach, because it is possible that, in some cases a separating plane can't be found. This is an example of such situation:

To avoid it, some extra planes need to be tested as separators, these planes are the cross product between the edges of polygon A and the edges of polygon B

So the final algorithm is something like:

```gdscript
var overlapping = true

for p in planes_of_A:
    var all_out = true
    for v in points_of_B:
        if (p.distance_to(v) < 0):
            all_out = false
            break

    if (all_out):
        # a separating plane was found
        # do not continue testing
        overlapping = false
        break

if (overlapping):
    # only do this check if no separating plane
    # was found in planes of A
    for p in planes_of_B:
        var all_out = true
        for v in points_of_A:
            if (p.distance_to(v) < 0):
                all_out = false
                break

        if (all_out):
            overlapping = false
            break

if (overlapping):
    for ea in edges_of_A:
        for eb in edges_of_B:
            var n = ea.cross(eb)
            if (n.length() == 0):

# ...
```

### More information

For more information on using vector math in Godot, see the following article:

- Matrices and transforms

If you would like additional explanation, you should check out 3Blue1Brown's excellent video series [Essence of Linear Algebra](https://www.youtube.com/watch?v=fNk_zzaMoSs&list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab).

---
