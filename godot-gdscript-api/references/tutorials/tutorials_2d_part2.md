# Godot 4 GDScript Tutorials — 2D (Part 2)

> 3 tutorials. GDScript-specific code examples.

## Custom drawing in 2D

### Introduction

Godot has nodes to draw sprites, polygons, particles, text, and many other common game development needs. However, if you need something specific not covered with the standard nodes you can make any 2D node (for example, [Control](../godot_gdscript_ui_controls.md) or [Node2D](../godot_gdscript_nodes_2d.md)-based) draw on screen using custom commands.

Custom drawing in a 2D node is _really_ useful. Here are some use cases:

- Drawing shapes or logic that existing nodes can't do, such as an image with trails or a special animated polygon.
- Drawing a large number of simple objects, such as a grid or a board for a 2d game. Custom drawing avoids the overhead of using a large number of nodes, possibly lowering memory usage and improving performance.
- Making a custom UI control. There are plenty of controls available, but when you have unusual needs, you will likely need a custom control.

### Drawing

Add a script to any [CanvasItem](../godot_gdscript_nodes_2d.md) derived node, like [Control](../godot_gdscript_ui_controls.md) or [Node2D](../godot_gdscript_nodes_2d.md). Then override the [\_draw()](../godot_gdscript_misc.md) function.

```gdscript
extends Node2D

func _draw():
    pass  # Your draw commands here.
```

Draw commands are described in the [CanvasItem](../godot_gdscript_nodes_2d.md) class reference. There are plenty of them and we will see some of them in the examples below.

### Updating

The [\_draw](../godot_gdscript_misc.md) function is only called once, and then the draw commands are cached and remembered, so further calls are unnecessary.

If re-drawing is required because a variable or something else changed, call [CanvasItem.queue_redraw](../godot_gdscript_nodes_2d.md) in that same node and a new `_draw()` call will happen.

Here is a little more complex example, where we have a texture variable that can be modified at any time, and using a [setter](tutorials_scripting.md), it forces a redraw of the texture when modified:

```gdscript
extends Node2D

@export var texture : Texture2D:
    set(value):
        texture = value
        queue_redraw()

func _draw():
    draw_texture(texture, Vector2())
```

To see it in action, you can set the texture to be the Godot icon on the editor by dragging and dropping the default `icon.svg` from the `FileSystem` tab to the Texture property on the `Inspector` tab. When changing the `Texture` property value while the previous script is running, the texture will also change automatically.

In some cases, we may need to redraw every frame. For this, call [queue_redraw](../godot_gdscript_misc.md) from the [\_process](../godot_gdscript_misc.md) method, like this:

```gdscript
extends Node2D

func _draw():
    pass  # Your draw commands here.

func _process(_delta):
    queue_redraw()
```

### Coordinates and line width alignment

The drawing API uses the CanvasItem's coordinate system, not necessarily pixel coordinates. This means `_draw()` uses the coordinate space created after applying the CanvasItem's transform. Additionally, you can apply a custom transform on top of it by using [draw_set_transform](../godot_gdscript_misc.md) or [draw_set_transform_matrix](../godot_gdscript_misc.md).

When using [draw_line](../godot_gdscript_misc.md), you should consider the width of the line. When using a width that is an odd size, the position of the start and end points should be shifted by `0.5` to keep the line centered, as shown below.

```gdscript
func _draw():
    draw_line(Vector2(1.5, 1.0), Vector2(1.5, 4.0), Color.GREEN, 1.0)
    draw_line(Vector2(4.0, 1.0), Vector2(4.0, 4.0), Color.GREEN, 2.0)
    draw_line(Vector2(7.5, 1.0), Vector2(7.5, 4.0), Color.GREEN, 3.0)
```

The same applies to the [draw_rect](../godot_gdscript_misc.md) method with `filled = false`.

```gdscript
func _draw():
    draw_rect(Rect2(1.0, 1.0, 3.0, 3.0), Color.GREEN)
    draw_rect(Rect2(5.5, 1.5, 2.0, 2.0), Color.GREEN, false, 1.0)
    draw_rect(Rect2(9.0, 1.0, 5.0, 5.0), Color.GREEN)
    draw_rect(Rect2(16.0, 2.0, 3.0, 3.0), Color.GREEN, false, 2.0)
```

### Antialiased drawing

Godot offers method parameters in [draw_line](../godot_gdscript_misc.md) to enable antialiasing, but not all custom drawing methods offer this `antialiased` parameter.

For custom drawing methods that don't provide an `antialiased` parameter, you can enable 2D MSAA instead, which affects rendering in the entire viewport. This provides high-quality antialiasing, but a higher performance cost and only on specific elements. See 2D antialiasing for more information.

Here is a comparison of a line of minimal width (`width=-1`) drawn with `antialiased=false`, `antialiased=true`, and `antialiased=false` with 2D MSAA 2x, 4x, and 8x enabled.

### Tools

Drawing your own nodes might also be desired while running them in the editor. This can be used as a preview or visualization of some feature or behavior.

To do this, you can use the [tool annotation](tutorials_scripting.md) on both GDScript and C#. See **the example below** and [Running code in the editor](tutorials_plugins.md) for more information.

### Example 1: drawing a custom shape

We will now use the custom drawing functionality of the Godot Engine to draw something that Godot doesn't provide functions for. We will recreate the Godot logo but with code- only using drawing functions.

You will have to code a function to perform this and draw it yourself.

> **Note:** The following instructions use a fixed set of coordinates that could be too small for high resolution screens (larger than 1080p). If that is your case, and the drawing is too small consider increasing your window scale in the project setting [Display > Window > Stretch > Scale](../godot_gdscript_misc.md) to adjust the project to a higher resolution (a 2 or 4 scale tends to work well).

#### Drawing a custom polygon shape

While there is a dedicated node to draw custom polygons ( [Polygon2D](../godot_gdscript_nodes_2d.md)), we will use in this case exclusively lower level drawing functions to combine them on the same node and be able to create more complex shapes later on.

First, we will define a set of points -or X and Y coordinates- that will form the base of our shape:

```gdscript
extends Node2D

var coords_head : Array = [
    [ 22.952, 83.271 ],  [ 28.385, 98.623 ],
    [ 53.168, 107.647 ], [ 72.998, 107.647 ],
    [ 99.546, 98.623 ],  [ 105.048, 83.271 ],
    [ 105.029, 55.237 ], [ 110.740, 47.082 ],
    [ 102.364, 36.104 ], [ 94.050, 40.940 ],
    [ 85.189, 34.445 ],  [ 85.963, 24.194 ],
    [ 73.507, 19.930 ],  [ 68.883, 28.936 ],
    [ 59.118, 28.936 ],  [ 54.494, 19.930 ],
    [ 42.039, 24.194 ],  [ 42.814, 34.445 ],
    [ 33.951, 40.940 ],  [ 25.637, 36.104 ],
    [ 17.262, 47.082 ],  [ 22.973, 55.237 ]
]
```

This format, while compact, is not the one that Godot understands to draw a polygon. In a different scenario we could have to load these coordinates from a file or calculate the positions while the application is running, so some transformation may be needed.

To transform these coordinates into the right format, we will create a new method `float_array_to_Vector2Array()`. Then we will override the `_ready()` function, which Godot will call only once -at the start of the execution- to load those coordinates into a variable:

```gdscript
var head : PackedVector2Array

func float_array_to_Vector2Array(coords : Array) -> PackedVector2Array:
    # Convert the array of floats into a PackedVector2Array.
    var array : PackedVector2Array = []
    for coord in coords:
        array.append(Vector2(coord[0], coord[1]))
    return array

func _ready():
    head = float_array_to_Vector2Array(coords_head);
```

To finally draw our first shape, we will use the method [draw_polygon](../godot_gdscript_misc.md) and pass the points (as an array of Vector2 coordinates) and its color, like this:

```gdscript
func _draw():
    # We are going to paint with this color.
    var godot_blue : Color = Color("478cbf")
    # We pass the PackedVector2Array to draw the shape.
    draw_polygon(head, [ godot_blue ])
```

When running it you should see something like this:

Note the lower part of the logo looks segmented- this is because a low amount of points were used to define that part. To simulate a smooth curve, we could add more points to our array, or maybe use a mathematical function to interpolate a curve and create a smooth shape from code (see **example 2**).

Polygons will always **connect its last defined point to its first one** in order to have a closed shape.

#### Drawing connected lines

Drawing a sequence of connected lines that don't close down to form a polygon is very similar to the previous method. We will use a connected set of lines to draw Godot's logo mouth.

First, we will define the list of coordinates that form the mouth shape, like this:

```gdscript
var coords_mouth = [
    [ 22.817, 81.100 ], [ 38.522, 82.740 ],
    [ 39.001, 90.887 ], [ 54.465, 92.204 ],
    [ 55.641, 84.260 ], [ 72.418, 84.177 ],
    [ 73.629, 92.158 ], [ 88.895, 90.923 ],
    [ 89.556, 82.673 ], [ 105.005, 81.100 ]
]
```

We will load these coordinates into a variable and define an additional variable with the configurable line thickness:

```gdscript
var mouth : PackedVector2Array
var _mouth_width : float = 4.4

func _ready():
    head = float_array_to_Vector2Array(coords_head);
    mouth = float_array_to_Vector2Array(coords_mouth);
```

And finally we will use the method [draw_polyline](../godot_gdscript_misc.md) to actually draw the line, like this:

```gdscript
func _draw():
    # We will use white to draw the line.
    var white : Color = Color.WHITE
    var godot_blue : Color = Color("478cbf")

    draw_polygon(head, [ godot_blue ])

    # We draw the while line on top of the previous shape.
    draw_polyline(mouth, white, _mouth_width)
```

You should get the following output:

Unlike `draw_polygon()`, polylines can only have a single unique color for all its points (the second argument). This method has 2 additional arguments: the width of the line (which is as small as possible by default) and enabling or disabling the antialiasing (it is disabled by default).

The order of the `_draw` calls is important- like with the Node positions on the tree hierarchy, the different shapes will be drawn from top to bottom, resulting in the latest shapes hiding earlier ones if they overlap. In this case we want the mouth drawn over the head, so we put it afterwards.

Notice how we can define colors in different ways, either with a hexadecimal code or a predefined color name. Check the class [Color](../godot_gdscript_math_types.md) for other constants and ways to define Colors.

#### Drawing circles

To create the eyes, we are going to add 4 additional calls to draw the eye shapes, in different sizes, colors and positions.

To draw a circle, you position it based on its center using the [draw_circle](../godot_gdscript_misc.md) method. The first parameter is a [Vector2](../godot_gdscript_math_types.md) with the coordinates of its center, the second is its radius, and the third is its color:

```gdscript
func _draw():
    var white : Color = Color.WHITE
    var godot_blue : Color = Color("478cbf")
    var grey : Color = Color("414042")

    draw_polygon(head, [ godot_blue ])
    draw_polyline(mouth, white, _mouth_width)

    # Four circles for the 2 eyes: 2 white, 2 grey.
    draw_circle(Vector2(42.479, 65.4825), 9.3905, white)
    draw_circle(Vector2(85.524, 65.4825), 9.3905, white)
    draw_circle(Vector2(43.423, 65.92), 6.246, grey)
    draw_circle(Vector2(84.626, 66.008), 6.246, grey)
```

When executing it, you should have something like this:

For partial, unfilled arcs (portions of a circle shape between certain arbitrary angles), you can use the method [draw_arc](../godot_gdscript_misc.md).

#### Drawing lines

To draw the final shape (the nose) we will use a line to approximate it.

[draw_line](../godot_gdscript_misc.md) can be used to draw a single segment by providing its start and end coordinates as arguments, like this:

```gdscript
func _draw():
    var white : Color = Color.WHITE
    var godot_blue : Color = Color("478cbf")
    var grey : Color = Color("414042")

    draw_polygon(head, [ godot_blue ])
    draw_polyline(mouth, white, _mouth_width)
    draw_circle(Vector2(42.479, 65.4825), 9.3905, white)
    draw_circle(Vector2(85.524, 65.4825), 9.3905, white)
    draw_circle(Vector2(43.423, 65.92), 6.246, grey)
    draw_circle(Vector2(84.626, 66.008), 6.246, grey)

    # Draw a short but thick white vertical line for the nose.
    draw_line(Vector2(64.273, 60.564), Vector2(64.273, 74.349), white, 5.8)
```

You should now be able to see the following shape on screen:

Note that if multiple unconnected lines are going to be drawn at the same time, you may get additional performance by drawing all of them in a single call, using the [draw_multiline](../godot_gdscript_misc.md) method.

#### Drawing text

While using the [Label](../godot_gdscript_ui_controls.md) Node is the most common way to add text to your application, the low-level \_draw function includes functionality to add text to your custom Node drawing. We will use it to add the name "GODOT" under the robot head.

We will use the [draw_string](../godot_gdscript_misc.md) method to do it, like this:

```gdscript
var default_font : Font = ThemeDB.fallback_font;

func _draw():
    var white : Color = Color.WHITE
    var godot_blue : Color = Color("478cbf")
    var grey : Color = Color("414042")

    draw_polygon(head, [ godot_blue ])
    draw_polyline(mouth, white, _mouth_width)
    draw_circle(Vector2(42.479, 65.4825), 9.3905, white)
    draw_circle(Vector2(85.524, 65.4825), 9.3905, white)
    draw_circle(Vector2(43.423, 65.92), 6.246, grey)
    draw_circle(Vector2(84.626, 66.008), 6.246, grey)
    draw_line(Vector2(64.273, 60.564), Vector2(64.273, 74.349), white, 5.8)

    # Draw GODOT text below the logo with the default font, size 22.
    draw_string(default_font, Vector2(20, 130), "GODOT",
                HORIZONTAL_ALIGNMENT_CENTER, 90, 22)
```

Here we first load into the defaultFont variable the configured default theme font (a custom one can be set instead) and then we pass the following parameters: font, position, text, horizontal alignment, width, and font size.

You should see the following on your screen:

Additional parameters as well as other methods related to text and characters can be found on the [CanvasItem](../godot_gdscript_nodes_2d.md) class reference.

#### Show the drawing while editing

While the code so far is able to draw the logo on a running window, it will not show up on the `2D view` on the editor. In certain cases you would also like to show your custom Node2D or control on the editor, to position and scale it appropriately, like most other nodes do.

To show the logo directly on the editor (without running it), you can use the [@tool](tutorials_scripting.md) annotation to request the custom drawing of the node to also appear while editing, like this:

```gdscript
@tool
extends Node2D
```

You will need to save your scene, rebuild your project (for C# only) and reload the current scene manually at the menu option `Scene > Reload Saved Scene` to refresh the current node in the `2D` view the first time you add or remove the `@tool` annotation.

#### Animation

If we wanted to make the custom shape change at runtime, we could modify the methods called or its arguments at execution time, or apply a transform.

For example, if we want the custom shape we just designed to rotate, we could add the following variable and code to the `_ready` and `_process` methods:

```gdscript
extends Node2D

@export var rotation_speed : float = 1  # In radians per second.

func _ready():
    rotation = 0
    ...

func _process(delta: float):
    rotation -= rotation_speed * delta
```

The problem with the above code is that because we have created the points approximately on a rectangle starting from the upper left corner, the `(0, 0)` coordinate and extending to the right and down, we see that the rotation is done using the top left corner as pivot. A position transform change on the node won't help us here, as the rotation transform is applied first.

While we could rewrite all of the points' coordinates to be centered around `(0, 0)`, including negative coordinates, that would be a lot of work.

One possible way to work around this is to use the lower level [draw_set_transform](../godot_gdscript_misc.md) method to fix this issue, translating all points in the CanvasItem's own space, and then moving it back to its original place with a regular node transform, either in the editor or in code, like this:

```gdscript
func _ready():
    rotation = 0
    position = Vector2(60, 60)
    ...

func _draw():
    draw_set_transform(Vector2(-60, -60))
    ...
```

This is the result, rotating around a pivot now on `(60, 60)`:

If what we wanted to animate was a property inside the `_draw()` call, we must remember to call `queue_redraw()` to force a refresh, as otherwise it would not be updated on screen.

For example, this is how we can make the robot appear to open and close its mouth, by changing the width of its mouth line follow a sinusoidal (`sin`) curve:

```gdscript
var _mouth_width : float = 4.4
var _max_width : float = 7
var _time : float = 0

func _process(delta : float):
    _time += delta
    _mouth_width = abs(sin(_time) * _max_width)
    queue_redraw()

func _draw():
    ...
    draw_polyline(mouth, white, _mouth_width)
    ...
```

It will look somewhat like this when run:

Please note that `_mouth_width` is a user defined property like any other and it or any other used as a drawing argument can be animated using more standard and high-level methods such as a [Tween](../godot_gdscript_animation.md) or an [AnimationPlayer](../godot_gdscript_resources.md) Node. The only difference is that a `queue_redraw()` call is needed to apply those changes so they get shown on screen.

### Example 2: drawing a dynamic line

The previous example was useful to learn how to draw and modify nodes with custom shapes and animations. This could have some advantages, such as using exact coordinates and vectors for drawing, rather than bitmaps -which means they will scale well when transformed on screen. In some cases, similar results could be achieved composing higher level functionality with nodes such as [sprites](../godot_gdscript_misc.md) or [AnimatedSprites](../godot_gdscript_misc.md) loading SVG resources (which are also images defined with vectors) and the [AnimationPlayer](../godot_gdscript_resources.md) node.

In other cases that will not be possible because we will not know what the resulting graphical representation will be before running the code. Here we will see how to draw a dynamic line whose coordinates are not known beforehand, and are affected by the user's input.

#### Drawing a straight line between 2 points

Let's assume we want to draw a straight line between 2 points, the first one will be fixed on the upper left corner `(0, 0)` and the second will be defined by the cursor position on screen.

We could draw a dynamic line between those 2 points like this:

```gdscript
extends Node2D

var point1 : Vector2 = Vector2(0, 0)
var width : int = 10
var color : Color = Color.GREEN

var _point2 : Vector2

func _process(_delta):
    var mouse_position = get_viewport().get_mouse_position()
    if mouse_position != _point2:
        _point2 = mouse_position
        queue_redraw()

func _draw():
    draw_line(point1, _point2, color, width)
```

In this example we obtain the position of the mouse in the default viewport every frame with the method [get_mouse_position](../godot_gdscript_misc.md). If the position has changed since the last draw request (a small optimization to avoid redrawing on every frame)- we will schedule a redraw. Our `_draw()` method only has one line: requesting the drawing of a green line of width 10 pixels between the top left corner and that obtained position.

The width, color, and position of the starting point can be configured with with the corresponding properties.

It should look like this when run:

#### Drawing an arc between 2 points

The above example works, but we may want to join those 2 points with a different shape or function, other than a straight line.

Let's try now creating an arc (a portion of a circumference) between both points.

Exporting the line starting point, segments, width, color, and antialiasing will allow us to modify those properties very easily directly from the editor inspector panel:

```gdscript
extends Node2D

@export var point1 : Vector2 = Vector2(0, 0)
@export_range(1, 1000) var segments : int = 100
@export var width : int = 10
@export var color : Color = Color.GREEN
@export var antialiasing : bool = false

var _point2 : Vector2
```

To draw the arc, we can use the method [draw_arc](../godot_gdscript_misc.md). There are many arcs that pass through 2 points, so we will chose for this example the semicircle that has its center in the middle point between the 2 initial points.

Calculating this arc will be more complex than in the case of the line:

```gdscript
func _draw():
    # Average points to get center.
    var center : Vector2 = Vector2((_point2.x + point1.x) / 2,
                                   (_point2.y + point1.y) / 2)
    # Calculate the rest of the arc parameters.
    var radius : float = point1.distance_to(_point2) / 2
    var start_angle : float = (_point2 - point1).angle()
    var end_angle : float = (point1 - _point2).angle()
    if end_angle < 0:  # end_angle is likely negative, normalize it.
        end_angle += TAU

    # Finally, draw the arc.
    draw_arc(center, radius, start_angle, end_angle, segments, color,
             width, antialiasing)
```

The center of the semicircle will be the middle point between both points. The radius will be half the distance between both points. The start and end angles will be the angles of the vector from point1 to point2 and vice-versa. Note we had to normalize the `end_angle` in positive values because if `end_angle` is less than `start_angle`, the arc will be drawn counter-clockwise, which we don't want in this case (the arc would be upside-down).

The result should be something like this, with the arc going down and between the points:

Feel free to play with the parameters in the inspector to obtain different results: change the color, the width, the antialiasing, and increase the number of segments to increase the curve smoothness, at the cost of extra performance.

---

## Introduction to 2D

Godot's 2D game development tools include a dedicated 2D rendering engine, physics system, and features tailored specifically for creating 2D experiences. You can efficiently design levels with the TileMap system, animate characters with 2D sprite or Cutout animation, and leverage 2D lighting for dynamic scene illumination. The built-in 2D particle system allows you to create complex visual effects, and Godot also supports custom shaders to enhance your graphics. These features, combined with Godot's accessibility and flexibility, provide a solid foundation for creating engaging 2D games.

This page will show you the 2D workspace and how you can get to know it.

> **Tip:** If you would like to get an introduction to 3D, see [Introduction to 3D](tutorials_3d.md).

### 2D workspace

You will use the 2D workspace to work with 2D scenes, design levels, or create user interfaces. To switch to the 2D workspace, you can either select a 2D node from the scene tree, or use the workspace selector located at the top edge of the editor:

Similar to 3D, you can use the tabs below the workspace selector to change between currently opened scenes or create a new one using the plus (+) button. The left and right docks should be familiar from [editor introduction](tutorials_editor.md).

Below the scene selector is the main toolbar, and beneath the main toolbar is the 2D viewport.

You can drag and drop compatible nodes from the FileSystem dock to add them to the viewport as nodes. Dragging and dropping adds the dragged node as a sibling of the selected node (if the root node is selected, adds as a child). Keeping Shift pressed when dropping adds the node as a child of the selected node. Holding Alt when dropping adds the node as a child of the root node. If Alt + Shift is held when dropping, the node type can be selected if applicable.

#### Main toolbar

Some buttons in the main toolbar are the same as those in the 3D workspace. A brief explanation is given with the shortcut if the mouse cursor is hovered over a button for one second. Some buttons may have additional functionality if another keypress is performed. A recap of main functionality of each button with its default shortcut is provided below from left to right:

- **Select Mode** (Q): Allows selection of nodes in the viewport. Left clicking on a node in the viewport selects it. Left clicking and dragging a rectangle selects all nodes within the rectangle's boundaries, once released. Holding Shift while selecting adds more nodes to the selection. Clicking on a selected node while holding Shift deselects the node. In this mode, you can drag the selected node(s) to move, press Ctrl to switch to the rotation mode temporarily, or use the red circles to scale it. If multiple nodes are selected, only movement and rotation are possible. In this mode, rotation and scaling will not use the snapping options if snapping is enabled.
- **Move Mode** (W): Enables move (or translate) mode for the selected nodes. See **2D Viewport** for more details.
- **Rotate Mode** (E): Enables rotation mode for the selected nodes. See **2D Viewport** for more details.
- **Scale Mode** (S): Enables scaling and displays scaling gizmos in both axes for the selected node(s). See **2D Viewport** for more details.
- **Show list of selectable nodes at position clicked**: As the description suggests, this provides a list of selectable nodes at the clicked position as a context menu, if there is more than one node in the clicked area.
- **Rotation pivot**: Sets the rotation pivot to rotate node(s) around. An added node has its rotation pivot at `x: 0`, `y: 0`, by default, with exceptions. For example, the default pivot for a [Sprite2D](../godot_gdscript_nodes_2d.md) is its center if the `centered` property is set to `true`. If you would like to change the rotation pivot of a node, click this button and choose a new location by left clicking. The node rotates considering this point. If you have multiple nodes selected, this icon will add a temporary pivot to be used commonly by all selected nodes. Pressing Shift and clicking this button will create the pivot at the center of selected nodes. If any of the snap options are enabled, the pivot will also snap to them when dragged.
- **Pan Mode** (G): Allows you to navigate in the viewport without accidentally selecting any nodes. In other modes, you can also hold Space and drag with the left mouse button to do the same.
- **Ruler Mode**: After enabling, click on the viewport to display the current global x and y coordinates. Dragging from a position to another one measures the distance in pixels. If you drag diagonally, it will draw a triangle and show the separate distances in terms of x, y, and total distance to the target, including the angles to the axes in degrees. The R key activates the ruler. If snapping is enabled, it also displays the measurements in terms of grid count:

- **Use Smart Snap**: Toggles smart snapping for move, rotate, and scale modes; and the rotation pivot. Customize it using the three-dot menu next to the snap tools.
- **Use Grid Snap**: Toggles snapping to grid for move and scale mode, rotation pivot, and the ruler. Customize it using the three-dot menu next to the snap tools.

You can customize the grid settings so that move mode, rotate mode, scale mode, ruler, and rotation pivot uses snapping. Use the three-dot menu for this:

- **Use Rotation Snap**: Toggles snapping using the configured rotation setting.
- **Use Scale Snap**: Toggles snapping using the configured scaling step setting.
- **Snap Relative**: Toggles the usage of snapping based on the selected node's current transform values. For example, if the grids are set to 32x32 pixels and if the selected node is located at `x: 1, y: 1`, then, enabling this option will temporarily shift the grids by `x: 1, y: 1`.
- **Use Pixel Snap**: Toggles the use of subpixels for snapping. If enabled, the position values will be integers, disabling will enable subpixel movement as decimal values. For the runtime property, consider checking Project Settings > Rendering > 2D > Snapping property for Node2D nodes, and Project Settings > GUI > General > Snap Controls to Pixels for Control nodes.
- **Smart Snapping**: Provides a set of options to snap to specific positions if they are enabled:

- Snap to Parent: Snaps to parent's edges. For example, scaling a child control node while this is enabled will snap to the boundaries of the parent.
- Snap to Node Anchor: Snaps to the node's anchor. For example, if anchors of a control node is positioned at different positions, enabling this will snap to the sides and corners of the anchor.
- Snap to Node Sides: Snaps to the node's sides, such as for the rotation pivot or anchor positioning.
- Snap to Node Center: Snaps to the node's center, such as for the rotation pivot or anchor positioning.
- Snap to Other Nodes: Snaps to other nodes while moving or scaling. Useful to align nodes in the editor.
- Snap to Guides: Snaps to custom guides drawn using the horizontal or vertical ruler. More on the ruler and guides below.

- **Configure Snap**: Opens the window shown above, offering a set of snapping parameters.

- Grid Offset: Allows you to shift grids with respect to the origin. `x` and `y` can be adjusted separately.
- Grid Step: The distance between each grid in pixels. `x` and `y` can be adjusted separately.
- Primary Line Every: The number of grids in-between to draw infinite lines as indication of main lines.
- Rotation Offset: Sets the offset to shift rotational snapping.
- Rotation Step: Defines the snapping degree. E.g., 15 means the node will rotate and snap at multiples of 15 degrees if rotation snap is enabled and the rotate mode is used.
- Scale Step: Determines the scaling increment factor. For example, if it is 0.1, it will change the scaling at 0.1 steps if scaling snap is enabled and the scaling mode is used.
- **Lock selected nodes** (Ctrl + L). Locks the selected nodes, preventing selection and movement in the viewport. Clicking the button again (or using Ctrl + Shift + L) unlocks the selected nodes. Locked nodes can only be selected in the scene tree. They can easily be identified by a padlock next to their node names in the scene tree. Clicking on this padlock also unlocks the nodes.
- **Group selected nodes** (Ctrl + G). This allows selection of the root node if any of the children are selected. Using Ctrl + G ungroups them. Additionally, clicking the ungroup button in the scene tree performs the same action.
- **Skeleton Options**: Provides options to work with Skeleton2D and Bone2D.

- Show Bones: Toggles the visibility of bones for the selected node.
- Make Bone2D Node(s) from Node(s): Converts selected node(s) into Bone2D.

> **See also:** To learn more about Skeletons, see [Cutout animation](tutorials_animation.md).

- **View** menu: Provides options to control the viewport view. Since its options depend heavily on the viewport, it is covered in the **2D Viewport** section.

Next to the View menu, additional buttons may be visible. In the toolbar image at the beginning of this chapter, an additional _Sprite2D_ button appears because a Sprite2D is selected. This menu provides some quick actions and tools to work on a specific node or selection. For example, while drawing a polygon, it provides buttons to add, modify, or remove points.

#### Coordinate system

In the 2D editor, unlike 3D, there are only two axes: `x` and `y`. Also, the viewing angle is fixed.

In the viewport, you will see two lines in two colors going across the screen infinitely: red for the x-axis, and green for the y-axis. In Godot, going right and down are positive directions. Where these two lines intersect is the origin: `x: 0, y: 0`.

A root node will have its origin at this position once added. Switching to the move or scale modes after selecting a node will display the gizmos at the node's offset position. The gizmos will point to the positive directions of the x and y axes. In the move mode, you can drag the green line to move only in the `y` axis. Similarly, you can hold the red line to move only in the `x` axis.

In the scale mode, the gizmos will have a square shape. You can hold and drag the green and red squares to scale the nodes in the `y` or `x` axes. Dragging in a negative direction flips the node horizontally or vertically.

#### 2D Viewport

The viewport will be the area you spend the most time if you plan to design levels or user interfaces visually:

Middle-clicking and dragging the mouse will pan the view. The scrollbars on the right or bottom of the viewport also move the view. Alternatively, the G or Space keys can be used. If you enable Editor Settings > Editors > Panning > Simple Panning, you can activate panning directly with Space only, without requiring dragging.

The viewport has buttons on the top-left. **Center View** centers the selected node(s) in the screen. Useful if you have a large scene with many nodes, and want to see the node selected in the scene tree. Next to it are the zoom controls. **-** zooms out, **+** zooms in, and clicking on the number with percentage defaults to 100%. Alternatively, you can use middle-mouse scrolling to zoom in (scroll up) and out (scroll down).

The black bars at the viewport's left and top edges are the **rulers**. You can use them to orient yourself in the viewport. By default, the rulers will display the pixel coordinates of the viewport, numbered at 100 pixel steps. Changing the zoom factor will change the shown values. Enabling Grid Snap or changing the snapping options will update the ruler's scaling and the shown values.

You can also create multiple custom guides to help you make measurements or align nodes with them:

If you have at least one node in the scene, you can create guides by dragging from the horizontal or vertical ruler towards the viewport. A purple guide will appear, showing its position, and will remain there when you release the mouse. You can create both horizontal and vertical guides simultaneously by dragging from the gray square at the rulers' intersection. Guides can be repositioned by dragging them back to their respective rulers, and they can be removed by dragging them all the way back to the ruler.

You can also enable snapping to the created guides using the Smart Snap menu.

> **Note:** If you cannot create a line, or do not see previously created guides, make sure that they are visible by checking the View menu of the viewport. Y toggles their visibility, by default. Also, make sure you have at least one node in the scene.

Depending on the tool chosen in the toolbar, left-clicking will have a primary action in the viewport. For example, the Select Mode will select the left-clicked node in the viewport. Sometimes, left-clicking can be combined with a modifier (e.g., Ctrl, or Shift) to perform secondary actions. For example, keeping Shift pressed while dragging a node in the Select or Move modes will try to snap the node in a single axis while moving.

Right clicking in the viewport provides two options to create a node or instantiate a scene at the chosen position. If at least one node is selected, right clicking also provides the option to move the selected node(s) to this position.

Viewport has a **View** menu which provides several options to change the look of the viewport:

- **Grid**: Allows you to show grids all the time, only when using snapping, or not at all. You can also toggle them with the provided option.
- **Show Helpers**: Toggles the temporary display of an outline of the node, with the previous transform properties (position, scaling, or rotation) if a transform operation has been initiated. For Control nodes, it also shows the sizing parameters. Useful to see the deltas.
- **Show Rulers**: Toggles the visibility of horizontal and vertical rulers. See **2D Viewport** more on rulers.
- **Show Guides**: Toggles the visibility of created guides. See **2D Viewport** for on how to create them.
- **Show Origin**: Toggles the display of the green and red origin lines drawn at `x: 0, y: 0`.
- **Show Viewport**: Toggles the visibility of the game's default viewport, indicated by an indigo-colored rectangle. It is also the default window size on desktop platforms, which can be changed by going to Project Settings > Display > Window > Size and setting Viewport Width and Viewport Height.
- **Gizmos**: Toggles the visibility of Position (shown with cross icon), Lock (shown with padlock), Groups (shown with two squares), and Transformation (shown with green and red lines) indicators.
- **Center Selection**: The same as the **Center View** button inside the viewport. Centers the selected node(s) in the view. F is the default shortcut.
- **Frame to Selection**: Similar to Center Selection, but also changes the zoom factor to fit the contents in the screen. Shift + F is the default shortcut.
- **Clear Guides**: Deletes all guides from the screen. You will need to recreate them if you plan to use them later.
- **Preview Canvas Scale**: Toggles the preview for scaling of canvas in the editor when the zoom factor or view of the viewport changes. Useful to see how the controls will look like after scaling and moving, without running the game.
- **Preview Theme**: Allows to choose from the available themes to change the look of control items in the editor, without requiring to run the game.

### Node2D and Control node

[CanvasItem](../godot_gdscript_nodes_2d.md) is the base node for 2D. [Node2D](../godot_gdscript_nodes_2d.md) is the base node for 2D game objects, and [Control](../godot_gdscript_ui_controls.md) is the base node for everything GUI. For 3D, Godot uses the [Node3D](../godot_gdscript_nodes_3d.md) node.

### Displaying 3D nodes in 2D

It is possible to display 3D nodes in a 2D scene by using a [SubViewport](../godot_gdscript_rendering.md). You can see this in the demo [3D in 2D Viewport](https://godotengine.org/asset-library/asset/2804).

---

## ParticleProcessMaterial 2D Usage

### Process material properties

The properties in this material control how particles behave and change over their lifetime. A lot of them have `Min`, `Max`, and `Curve` values that allow you to fine-tune their behavior. The relationship between these values is this: When a particle is spawned, the property is set with a random value between `Min` and `Max`. If `Min` and `Max` are the same, the value will always be the same for every particle. If the `Curve` is also set, the value of the property will be multiplied by the value of the curve at the current point in a particle's lifetime. Use the curve to change a property over the particle lifetime. Very complex behavior can be expressed this way.

> **Note:** This page covers how to use ParticleProcessMaterial for 2D scenes specifically. For information on how to use it in a 3D scene see [Process material properties](tutorials_3d.md).

#### Lifetime Randomness

The `Lifetime Randomness` property controls how much randomness to apply to each particle's lifetime. A value of `0` means there is no randomness at all and all particles live for the same amount of time, set by the [Lifetime](tutorials_3d.md) property. A value of `1` means that a particle's lifetime is completely random within the range of [0.0, `Lifetime`].

### Particle Flags

### Spawn

#### Angle

Determines the initial angle of the particle (in degrees). This parameter is mostly useful randomized.

#### Velocity

##### Direction

This is the base direction at which particles emit. The default is `Vector3(1, 0, 0)` which makes particles emit to the right. However, with the default gravity settings, particles will go straight down.

For this property to be noticeable, you need an _initial velocity_ greater than 0. Here, we set the initial velocity to 40. You'll notice that particles emit toward the right, then go down because of gravity.

##### Spread

This parameter is the angle in degrees which will be randomly added in either direction to the base `Direction`. A spread of `180` will emit in all directions (+/- 180). For spread to do anything the "Initial Velocity" parameter must be greater than 0.

##### Flatness

This property is only useful for 3D particles.

##### Initial Velocity

Initial velocity is the speed at which particles will be emitted (in pixels/sec). Speed might later be modified by gravity or other accelerations (as described further below).

### Animated Velocity

#### Angular Velocity

Angular velocity is the speed at which particles rotate around their center (in degrees/sec).

#### Orbit Velocity

Orbit velocity is used to make particles turn around their center.

### Accelerations

#### Gravity

The gravity applied to every particle.

#### Linear Acceleration

The linear acceleration applied to each particle.

#### Radial Acceleration

If this acceleration is positive, particles are accelerated away from the center. If negative, they are absorbed towards it.

#### Tangential Acceleration

This acceleration will use the tangent vector to the center. Combining with radial acceleration can do nice effects.

#### Damping

Damping applies friction to the particles, forcing them to stop. It is especially useful for sparks or explosions, which usually begin with a high linear velocity and then stop as they fade.

### Display

#### Scale

Determines the initial scale of the particles.

#### Color Curves

##### Color

Used to change the color of the particles being emitted.

#### Hue Variation

The `Variation` value sets the initial hue variation applied to each particle. The `Variation Random` value controls the hue variation randomness ratio.

#### Animation

> **Note:** Particle flipbook animation is only effective if the CanvasItemMaterial used on the GPUParticles2D or CPUParticles2D node has been configured accordingly.

To set up the particle flipbook for linear playback, set the **Speed Min** and **Speed Max** values to 1:

By default, looping is disabled. If the particle is done playing before its lifetime ends, the particle will keep using the flipbook's last frame (which may be fully transparent depending on how the flipbook texture is designed). If looping is enabled, the animation will loop back to the first frame and resume playing.

Depending on how many images your sprite sheet contains and for how long your particle is alive, the animation might not look smooth. The relationship between particle lifetime, animation speed, and number of images in the sprite sheet is this:

> **Note:** At an animation speed of `1.0`, the animation will reach the last image in the sequence just as the particle's lifetime ends. \[Animation\ FPS = \frac{Number\ of\ images}{Lifetime}\]

If you wish the particle flipbook to be used as a source of random particle textures for every particle, keep the speed values at 0 and set **Offset Max** to 1 instead:

Note that the GPUParticles2D node's **Fixed FPS** also affects animation playback. For smooth animation playback, it's recommended to set it to 0 so that the particle is simulated on every rendered frame. If this is not an option for your use case, set **Fixed FPS** to be equal to the effective framerate used by the flipbook animation (see above for the formula).

### Emission Shapes

ParticleProcessMaterials allow you to set an Emission Mask, which dictates the area and direction in which particles are emitted. These can be generated from textures in your project.

Ensure that a ParticleProcessMaterial is set, and the GPUParticles2D node is selected. A "Particles" menu should appear in the Toolbar:

Open it and select "Load Emission Mask":

Then select which texture you want to use as your mask:

A dialog box with several settings will appear.

#### Emission Mask

Three types of emission masks can be generated from a texture:

- Solid Pixels: Particles will spawn from any area of the texture, excluding transparent areas.

- Border Pixels: Particles will spawn from the outer edges of the texture.

- Directed Border Pixels: Similar to Border Pixels, but adds extra information to the mask to give particles the ability to emit away from the borders. Note that an `Initial Velocity` will need to be set in order to utilize this.

#### Emission Colors

`Capture from Pixel` will cause the particles to inherit the color of the mask at their spawn points.

Once you click "OK", the mask will be generated and set to the ParticleProcessMaterial, under `Spawn` and then `Position`

All of the values within this section have been automatically generated by the "Load Emission Mask" menu, so they should generally be left alone.

> **Note:** An image should not be added to `Point Texture` or `Color Texture` directly. The "Load Emission Mask" menu should always be used instead.

### Customizing the process material

If you need to change or implement new behaviors in shader code, you can do so by converting the current ParticleProcessMaterial to a [ShaderMaterial](../godot_gdscript_rendering.md). Existing properties are preserved by the conversion process. Features that are enabled will also affect what's present in the converted shader code.

To do so, right-click on the material in the FileSystem dock and choose **Convert to ShaderMaterial**. You can also do so by right-clicking on any property holding a reference to the material in the inspector.

---
