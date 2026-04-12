# Godot 4 GDScript Tutorials — Navigation (Part 2)

> 7 tutorials. GDScript-specific code examples.

## Using NavigationLinks

NavigationLinks are used to connect navigation mesh polygons from [NavigationRegion2D](../godot_gdscript_nodes_2d.md) and [NavigationRegion3D](../godot_gdscript_nodes_3d.md) over arbitrary distances for pathfinding.

NavigationLinks are also used to consider movement shortcuts in pathfinding available through interacting with gameplay objects e.g. ladders, jump pads or teleports.

2D and 3D versions of NavigationJumplinks nodes are available as [NavigationLink2D](../godot_gdscript_nodes_2d.md) and [NavigationLink3D](../godot_gdscript_nodes_3d.md) respectively.

Different NavigationRegions can connect their navigation meshes without the need for a NavigationLink as long as they have overlapping edges or edges that are within navigation map `edge_connection_margin`. As soon as the distance becomes too large, building valid connections becomes a problem - a problem that NavigationLinks can solve.

See Using NavigationRegions to learn more about the use of navigation regions. See Connecting navigation meshes to learn more about how to connect navigation meshes.

NavigationLinks share many properties with NavigationRegions like `navigation_layers`. NavigationLinks add a single connection between two positions over an arbitrary distance compared to NavigationRegions that add a more local traversable area with a navigation mesh resource.

NavigationLinks have a `start_position` and `end_position` and can go in both directions when `bidirectional` is enabled. When placed a navigationlink connects the navigation mesh polygons closest to its `start_position` and `end_position` within search radius for pathfinding.

The polygon search radius can be configured globally in the ProjectSettings under `navigation/2d_or_3d/default_link_connection_radius` or set for each navigation **map** individually using the `NavigationServer.map_set_link_connection_radius()` function.

Both `start_position` and `end_position` have debug markers in the Editor. The arrows indicate which direction the link can be travelled across, and the visible radius of a position shows the polygon search radius. All navigation mesh polygons inside are compared and the closest is picked for the edge connection. If no valid polygon is found within the search radius the navigation link gets disabled.

The link debug visuals can be changed in the Editor [ProjectSettings](../godot_gdscript_filesystem.md) under `debug/shapes/navigation`. The visibility of the debug can also be controlled in the Editor 3D Viewport gizmo menu.

A navigation link does not provide any specialized movement through the link. Instead, when an agent reaches the position of a link, game code needs to react (e.g. through area triggers) and provide means for the agent to move through the link to end up at the links other position (e.g. through teleport or animation). Without that an agent will attempt to move itself along the path of the link. You could end up with an agent walking over a bottomless pit instead of waiting for a moving platform, or walking through a teleporter and proceeding through a wall.

### Navigation link script templates

The following script uses the NavigationServer to create a new navigation link.

```gdscript
extends Node2D

var link_rid: RID
var link_start_position: Vector2
var link_end_position: Vector2

func _ready() -> void:
    link_rid = NavigationServer2D.link_create()

    var link_owner_id: int = get_instance_id()
    var link_enter_cost: float = 1.0
    var link_travel_cost: float = 1.0
    var link_navigation_layers: int = 1
    var link_bidirectional: bool = true

    NavigationServer2D.link_set_owner_id(link_rid, link_owner_id)
    NavigationServer2D.link_set_enter_cost(link_rid, link_enter_cost)
    NavigationServer2D.link_set_travel_cost(link_rid, link_travel_cost)
    NavigationServer2D.link_set_navigation_layers(link_rid, link_navigation_layers)
    NavigationServer2D.link_set_bidirectional(link_rid, link_bidirectional)

    # Enable the link and set it to the default navigatio
# ...
```

```gdscript
extends Node3D

var link_rid: RID
var link_start_position: Vector3
var link_end_position: Vector3

func _ready() -> void:
    link_rid = NavigationServer3D.link_create()

    var link_owner_id: int = get_instance_id()
    var link_enter_cost: float = 1.0
    var link_travel_cost: float = 1.0
    var link_navigation_layers: int = 1
    var link_bidirectional: bool = true

    NavigationServer3D.link_set_owner_id(link_rid, link_owner_id)
    NavigationServer3D.link_set_enter_cost(link_rid, link_enter_cost)
    NavigationServer3D.link_set_travel_cost(link_rid, link_travel_cost)
    NavigationServer3D.link_set_navigation_layers(link_rid, link_navigation_layers)
    NavigationServer3D.link_set_bidirectional(link_rid, link_bidirectional)

    # Enable the link and set it to the default navigatio
# ...
```

---

## Using NavigationMaps

A NavigationMap is an abstract navigation world on the NavigationServer identified by a NavigationServer [RID](../godot_gdscript_math_types.md).

A map can hold and connect a near infinite number of navigation regions with navigation meshes to build the traversable areas of a game world for pathfinding.

A map can contain avoidance agents. Collision avoidance will be calculated based on the agents present in the map.

> **Note:** Different NavigationMaps are completely isolated from each other but navigation regions and avoidance agents can switch between different maps. Switches will become effective on NavigationServer synchronization.

### Default navigation maps

By default Godot creates a navigation map for each [World2D](../godot_gdscript_misc.md) and [World3D](../godot_gdscript_misc.md) of the root viewport.

The 2D default navigation map RID can be obtained with `get_world_2d().get_navigation_map()` from any [Node2D](../godot_gdscript_nodes_2d.md) inheriting Node.

The 3D default navigation map RID can be obtained with `get_world_3d().get_navigation_map()` from any [Node3D](../godot_gdscript_nodes_3d.md) inheriting Node.

```gdscript
extends Node2D

func _ready() -> void:
    var default_navigation_map_rid: RID = get_world_2d().get_navigation_map()
```

```gdscript
extends Node3D

func _ready() -> void:
    var default_navigation_map_rid: RID = get_world_3d().get_navigation_map()
```

### Creating new navigation maps

The NavigationServer can create and support as many navigation maps as required for specific gameplay. Additional navigation maps are created and handled by using the NavigationServer API directly e.g. to support different avoidance agent or actor locomotion types.

For example uses of different navigation maps see Support different actor types and Support different actor locomotion.

Each navigation map individually synchronizes queued changes to its navigation regions and avoidance agents. A navigation map that has not received changes will consume little to no processing time. Navigation regions and avoidance agents can only be part of a single navigation map but they can switch map at any time.

> **Note:** A navigation map switch will take effect only after the next NavigationServer synchronization.

```gdscript
extends Node2D

func _ready() -> void:
    var new_navigation_map: RID = NavigationServer2D.map_create()
    NavigationServer2D.map_set_active(new_navigation_map, true)
```

```gdscript
extends Node3D

func _ready() -> void:
    var new_navigation_map: RID = NavigationServer3D.map_create()
    NavigationServer3D.map_set_active(new_navigation_map, true)
```

> **Note:** There is no difference between navigation maps created with the NavigationServer2D API or the NavigationServer3D API.

---

## Using navigation meshes

2D and 3D versions of the navigation mesh are available as [NavigationPolygon](../godot_gdscript_misc.md) and [NavigationMesh](../godot_gdscript_misc.md) respectively.

> **Note:** A navigation mesh only describes a traversable area for an agent's center position. Any radius values an agent may have are ignored. If you want pathfinding to account for an agent's (collision) size you need to shrink the navigation mesh accordingly.

Navigation works independently from other engine parts like rendering or physics. Navigation meshes are the only things considered when doing pathfinding, e.g. visuals and collision shapes for example are completely ignored by the navigation system. If you need to take other data (like visuals for example) into account when doing pathfinding, you need to adapt your navigation meshes accordingly. The process of factoring in navigation restrictions in navigation meshes is commonly referred to as navigation mesh baking.

If you experience clipping or collision problems while following navigation paths, always remember that you need to tell the navigation system what your intentions are through an appropriate navigation mesh. By itself the navigation system will never know "this is a tree / rock / wall collision shape or visual mesh" because it only knows that "here I was told I can path safely because it is on a navigation mesh".

Navigation mesh baking can be done either by using a [NavigationRegion2D](../godot_gdscript_nodes_2d.md) or [NavigationRegion3D](../godot_gdscript_nodes_3d.md), or by using the [NavigationServer2D](../godot_gdscript_misc.md) and [NavigationServer3D](../godot_gdscript_misc.md) API directly.

### Baking a navigation mesh with a NavigationRegion

The navigation mesh baking is made more accessible with the NavigationRegion node. When baking with a NavigationRegion node, the individual parsing, baking, and region update steps are all combined into one function.

The nodes are available in 2D and 3D as [NavigationRegion2D](../godot_gdscript_nodes_2d.md) and [NavigationRegion3D](../godot_gdscript_nodes_3d.md) respectively.

> **Tip:** The navigation mesh `source_geometry_mode` can be switched to parse specific node group names so nodes that should be baked can be placed anywhere in the scene.

```gdscript
var on_thread: bool = true
bake_navigation_polygon(on_thread)
```

```gdscript
var on_thread: bool = true
bake_navigation_mesh(on_thread)
```

### Baking a navigation mesh with the NavigationServer

The [NavigationServer2D](../godot_gdscript_misc.md) and [NavigationServer3D](../godot_gdscript_misc.md) have API functions to call each step of the navigation mesh baking process individually.

- `parse_source_geometry_data()` can be used to parse source geometry to a reusable and serializable resource.
- `bake_from_source_geometry_data()` can be used to bake a navigation mesh from already parsed data e.g. to avoid runtime performance issues with (redundant) parsing.
- `bake_from_source_geometry_data_async()` is the same but bakes the navigation mesh deferred with threads, not blocking the main thread.

Compared to a NavigationRegion, the NavigationServer offers finer control over the navigation mesh baking process. In turn it is more complex to use but also provides more advanced options.

Some other advantages of the NavigationServer over a NavigationRegion are:

- The server can parse source geometry without baking, e.g. to cache it for later use.
- The server allows selecting the root node at which to start the source geometry parsing manually.
- The server can accept and bake from procedurally generated source geometry data.
- The server can bake multiple navigation meshes in sequence while (re)using the same source geometry data.

To bake navigation meshes with the NavigationServer, source geometry is required. Source geometry is geometry data that should be considered in a navigation mesh baking process. Both navigation meshes for 2D and 3D are created by baking them from source geometry.

2D and 3D versions of the source geometry resources are available as [NavigationMeshSourceGeometryData2D](../godot_gdscript_misc.md) and [NavigationMeshSourceGeometryData3D](../godot_gdscript_misc.md) respectively.

Source geometry can be geometry parsed from visual meshes, from physics collision, or procedural created arrays of data, like outlines (2D) and triangle faces (3D). For convenience, source geometry is commonly parsed directly from node setups in the SceneTree. For runtime navigation mesh (re)bakes, be aware that the geometry parsing always happens on the main thread.

> **Note:** The SceneTree is not thread-safe. Parsing source geometry from the SceneTree can only be done on the main thread.

> **Warning:** The data from visual meshes and polygons needs to be received from the GPU, stalling the RenderingServer in the process. For runtime (re)baking prefer using physics shapes as parsed source geometry.

Source geometry is stored inside resources so the created geometry can be reused for multiple bakes. E.g. baking multiple navigation meshes for different agent sizes from the same source geometry. This also allows to save source geometry to disk so it can be loaded later, e.g. to avoid the overhead of parsing it again at runtime.

The geometry data should be in general kept very simple. As many edges as are required but as few as possible. Especially in 2D duplicated and nested geometry should be avoided as it forces polygon hole calculation that can result in flipped polygons. An example for nested geometry would be a smaller StaticBody2D shape placed completely inside the bounds of another StaticBody2D shape.

### Baking navigation mesh chunks for large worlds

> **See also:** You can see the navigation mesh chunk baking in action in the [Navigation Mesh Chunks 2D](https://github.com/godotengine/godot-demo-projects/tree/master/2d/navigation_mesh_chunks) and [Navigation Mesh Chunks 3D](https://github.com/godotengine/godot-demo-projects/tree/master/3d/navigation_mesh_chunks) demo projects.

To avoid misaligned edges between different region chunks the navigation meshes have two important properties for the navigation mesh baking process. The baking bound and the border size. Together they can be used to ensure perfectly aligned edges between region chunks.

The baking bound, which is an axis-aligned [Rect2](../godot_gdscript_math_types.md) for 2D and [AABB](../godot_gdscript_math_types.md) for 3D, limits the used source geometry by discarding all the geometry that is outside of the bounds.

The [NavigationPolygon](../godot_gdscript_misc.md) properties `baking_rect` and `baking_rect_offset` can be used to create and place the 2D baking bound.

The [NavigationMesh](../godot_gdscript_misc.md) properties `filter_baking_aabb` and `filter_baking_aabb_offset` can be used to create and place the 3D baking bound.

With only the baking bound set another problem still exists. The resulting navigation mesh will inevitably be affected by necessary offsets like the `agent_radius` which makes the edges not align properly.

This is where the `border_size` property for navigation mesh comes in. The border size is an inward margin from the baking bound. The important characteristic of the border size is that it is unaffected by most offsets and postprocessing like the `agent_radius`.

Instead of discarding source geometry, the border size discards parts of the final surface of the baked navigation mesh. If the baking bound is large enough the border size can remove the problematic surface parts so that only the intended chunk size is left.

> **Note:** The baking bounds need to be large enough to include a reasonable amount of source geometry from all the neighboring chunks.

> **Warning:** In 3D the functionality of the border size is limited to the xz-axis.

### Navigation mesh baking common problems

There are some common user problems and important caveats to consider when creating or baking navigation meshes.

- **Navigation mesh baking creates frame rate problems at runtime**
  : The navigation mesh baking is by default done on a background thread, so as long as the platform supports threads, the actual baking is rarely the source of any performance issues (assuming a reasonably sized and complex geometry for runtime rebakes).

The common source for performance issues at runtime is the parsing step for source geometry that involves nodes and the SceneTree. The SceneTree is not thread-safe so all the nodes need to be parsed on the main thread. Some nodes with a lot of data can be very heavy and slow to parse at runtime, e.g. a TileMap has one or more polygons for every single used cell and TileMapLayer to parse. Nodes that hold meshes need to request the data from the RenderingServer stalling the rendering in the process.

To improve performance, use more optimized shapes, e.g. collision shapes over detailed visual meshes, and merge and simplify as much geometry as possible upfront. If nothing helps, don't parse the SceneTree and add the source geometry procedural with scripts. If only pure data arrays are used as source geometry, the entire baking process can be done on a background thread.

- **Navigation mesh creates unintended holes in 2D.**
  : The navigation mesh baking in 2D is done by doing polygon clipping operations based on outline paths. Polygons with "holes" are a necessary evil to create more complex 2D polygons but can become unpredictable for users with many complex shapes involved.

To avoid any unexpected problems with polygon hole calculations, avoid nesting any outlines inside other outlines of the same type (traversable / obstruction). This includes the parsed shapes from nodes. E.g. placing a smaller StaticBody2D shape inside a larger StaticBody2D shape can result in the resulting polygon being flipped.

- **Navigation mesh appears inside geometry in 3D.**
  : The navigation mesh baking in 3D has no concept of "inside". The voxel cells used to rasterize the geometry are either occupied or not. Remove the geometry that is on the ground inside the other geometry. If that is not possible, add smaller "dummy" geometry inside with as few triangles as possible so the cells are occupied with something.

A [NavigationObstacle3D](../godot_gdscript_nodes_3d.md) shape set to bake with navigation mesh can be used to discard geometry as well.

### Navigation mesh script templates

The following script uses the NavigationServer to parse source geometry from the scene tree, bakes a navigation mesh, and updates a navigation region with the updated navigation mesh.

```gdscript
extends Node2D

var navigation_mesh: NavigationPolygon
var source_geometry : NavigationMeshSourceGeometryData2D
var callback_parsing : Callable
var callback_baking : Callable
var region_rid: RID

func _ready() -> void:
    navigation_mesh = NavigationPolygon.new()
    navigation_mesh.agent_radius = 10.0
    source_geometry = NavigationMeshSourceGeometryData2D.new()
    callback_parsing = on_parsing_done
    callback_baking = on_baking_done
    region_rid = NavigationServer2D.region_create()

    # Enable the region and set it to the default navigation map.
    NavigationServer2D.region_set_enabled(region_rid, true)
    NavigationServer2D.region_set_map(region_rid, get_world_2d().get_navigation_map())

    # Some mega-nodes like TileMap are often not ready on the first frame.
    # Also the
# ...
```

```gdscript
extends Node3D

var navigation_mesh: NavigationMesh
var source_geometry : NavigationMeshSourceGeometryData3D
var callback_parsing : Callable
var callback_baking : Callable
var region_rid: RID

func _ready() -> void:
    navigation_mesh = NavigationMesh.new()
    navigation_mesh.agent_radius = 0.5
    source_geometry = NavigationMeshSourceGeometryData3D.new()
    callback_parsing = on_parsing_done
    callback_baking = on_baking_done
    region_rid = NavigationServer3D.region_create()

    # Enable the region and set it to the default navigation map.
    NavigationServer3D.region_set_enabled(region_rid, true)
    NavigationServer3D.region_set_map(region_rid, get_world_3d().get_navigation_map())

    # Some mega-nodes like GridMap are often not ready on the first frame.
    # Also the parsin
# ...
```

The following script uses the NavigationServer to update a navigation region with procedurally generated navigation mesh data.

```gdscript
extends Node2D

var navigation_mesh: NavigationPolygon
var region_rid: RID

func _ready() -> void:
    navigation_mesh = NavigationPolygon.new()
    region_rid = NavigationServer2D.region_create()

    # Enable the region and set it to the default navigation map.
    NavigationServer2D.region_set_enabled(region_rid, true)
    NavigationServer2D.region_set_map(region_rid, get_world_2d().get_navigation_map())

    # Add vertices for a convex polygon.
    navigation_mesh.vertices = PackedVector2Array([
        Vector2(0.0, 0.0),
        Vector2(100.0, 0.0),
        Vector2(100.0, 100.0),
        Vector2(0.0, 100.0),
    ])

    # Add indices for the polygon.
    navigation_mesh.add_polygon(
        PackedInt32Array([0, 1, 2, 3])
    )

    NavigationServer2D.region_set_navigation_polygon(regi
# ...
```

```gdscript
extends Node3D

var navigation_mesh: NavigationMesh
var region_rid: RID

func _ready() -> void:
    navigation_mesh = NavigationMesh.new()
    region_rid = NavigationServer3D.region_create()

    # Enable the region and set it to the default navigation map.
    NavigationServer3D.region_set_enabled(region_rid, true)
    NavigationServer3D.region_set_map(region_rid, get_world_3d().get_navigation_map())

    # Add vertices for a convex polygon.
    navigation_mesh.vertices = PackedVector3Array([
        Vector3(-1.0, 0.0, 1.0),
        Vector3(1.0, 0.0, 1.0),
        Vector3(1.0, 0.0, -1.0),
        Vector3(-1.0, 0.0, -1.0),
    ])

    # Add indices for the polygon.
    navigation_mesh.add_polygon(
        PackedInt32Array([0, 1, 2, 3])
    )

    NavigationServer3D.region_set_navigation_me
# ...
```

---

## Using NavigationObstacles

2D and 3D versions of NavigationObstacles nodes are available as [NavigationObstacle2D](../godot_gdscript_nodes_2d.md) and [NavigationObstacle3D](../godot_gdscript_nodes_3d.md) respectively.

Navigation obstacles are dual purpose in that they can affect both the navigation mesh baking, and the agent avoidance.

- With `affect_navigation_mesh` enabled the obstacle will affect navigation mesh when baked.
- With `avoidance_enabled` the obstacle will affect avoidance agents.

> **Tip:** Avoidance is enabled by default. If the obstacle is not used for avoidance disable `enabled_avoidance` to save performance.

### Obstacles and navigation mesh

For navigation mesh baking, obstacles can be used to discard parts of all other source geometry inside the obstacle shape.

This can be used to stop navigation meshes being baked in unwanted places, e.g. inside "solid" geometry like thick walls or on top of other geometry that should not be included for gameplay like roofs.

An obstacle does not add geometry in the baking process, it only removes geometry. It does so by nullifying all the (voxel) cells with rasterized source geometry that are within the obstacle shape. As such its effect and shape detail is limited to the cell resolution used by the baking process.

For more details on the navigation mesh baking see Using navigation meshes.

The property `affect_navigation_mesh` makes the obstacle contribute to the navigation mesh baking. It will be parsed or unparsed like all other node objects in a navigation mesh baking process.

The `carve_navigation_mesh` property makes the shape unaffected by offsets of the baking, e.g. the offset added by the navigation mesh `agent_radius`. It will basically act as a stencil and cut into the already offset navigation mesh surface. It will still be affected by further postprocessing of the baking process like edge simplification.

The obstacle shape and placement is defined with the `height` and `vertices` properties, and the `global_position` of the obstacle. The y-axis value of any Vector3 used for the vertices is ignored as the obstacle is projected on a flat horizontal plane.

When baking navigation meshes in scripts obstacles can be added procedurally as a projected obstruction. Obstacles are not involved in the source geometry parsing so adding them just before baking is enough.

```gdscript
var obstacle_outline = PackedVector2Array([
    Vector2(-50, -50),
    Vector2(50, -50),
    Vector2(50, 50),
    Vector2(-50, 50)
])

var navigation_mesh = NavigationPolygon.new()
var source_geometry = NavigationMeshSourceGeometryData2D.new()

NavigationServer2D.parse_source_geometry_data(navigation_mesh, source_geometry, $MyTestRootNode)

var obstacle_carve: bool = true

source_geometry.add_projected_obstruction(obstacle_outline, obstacle_carve)

NavigationServer2D.bake_from_source_geometry_data(navigation_mesh, source_geometry)
```

```gdscript
var obstacle_outline = PackedVector3Array([
    Vector3(-5, 0, -5),
    Vector3(5, 0, -5),
    Vector3(5, 0, 5),
    Vector3(-5, 0, 5)
])

var navigation_mesh = NavigationMesh.new()
var source_geometry = NavigationMeshSourceGeometryData3D.new()

NavigationServer3D.parse_source_geometry_data(navigation_mesh, source_geometry, $MyTestRootNode)

var obstacle_elevation: float = $MyTestObstacleNode.global_position.y
var obstacle_height: float = 50.0
var obstacle_carve: bool = true

source_geometry.add_projected_obstruction(obstacle_outline, obstacle_elevation, obstacle_height, obstacle_carve)

NavigationServer3D.bake_from_source_geometry_data(navigation_mesh, source_geometry)
```

### Obstacles and agent avoidance

For avoidance navigation obstacles can be used either as static or dynamic obstacles to affect avoidance controlled agents.

- When used statically NavigationObstacles constrain avoidance controlled agents outside or inside a polygon defined area.
- When used dynamically NavigationObstacles push away avoidance controlled agents in a radius around them.

#### Static avoidance obstacles

An avoidance obstacle is considered static when its `vertices` property is populated with an outline array of positions to form a polygon.

- Static obstacles act as hard do-not-cross boundaries for avoidance using agents, e.g. similar to physics collision but for avoidance.
- Static obstacles define their boundaries with an array of outline `vertices` (positions), and in case of 3D with an additional `height` property.
- Static obstacles only work for agents that use the 2D avoidance mode.
- Static obstacles define through winding order of the vertices if agents are pushed out or sucked in.
- Static obstacles can not change their position. They can only be warped to a new position and rebuilt from scratch. Static obstacles as a result are ill-suited for usages where the position is changed every frame, as the constant rebuild has a high performance cost.
- Static obstacles that are warped to another position can not be predicted by agents. This creates the risk of getting agents stuck should a static obstacle be warped on top of agents.

When the 2D avoidance is used in 3D the y-axis of Vector3 vertices is ignored. Instead, the global y-axis position of the obstacle is used as the elevation level. Agents will ignore static obstacles in 3D that are below or above them. This is automatically determined by global y-axis position of both obstacle and agent as the elevation level as well as their respective height properties.

#### Dynamic avoidance obstacles

An avoidance obstacle is considered dynamic when its `radius` property is greater than zero.

- Dynamic obstacles act as a soft please-move-away-from-me object for avoidance using agents, e.g. similar to how they avoid other agents.
- Dynamic obstacles define their boundaries with a single `radius` for a 2D circle, or in case of 3D avoidance a sphere shape.
- Dynamic obstacles can change their position every frame without additional performance cost.
- Dynamic obstacles with a set velocity can be predicted in their movement by agents.
- Dynamic obstacles are not a reliable way to constrain agents in crowded or narrow spaces.

While both static and dynamic properties can be active at the same time on the same obstacle this is not recommended for performance. Ideally when an obstacle is moving the static vertices are removed and instead the radius activated. When the obstacle reaches the new final position it should gradually enlarge its radius to push all other agents away. With enough created safe space around the obstacle it should add the static vertices again and remove the radius. This helps avoid getting agents stuck in the suddenly appearing static obstacle when the rebuilt static boundary is finished.

Similar to agents the obstacles can make use of the `avoidance_layers` bitmask. All agents with a matching bit on their own avoidance mask will avoid the obstacle.

### Procedural obstacles

New obstacles can be created in a script without a Node by using the NavigationServer directly.

Obstacles created with scripts require at least a `map` and a `position`. For dynamic use a `radius` is required. For static use an array of `vertices` is required.

```gdscript
# create a new "obstacle" and place it on the default navigation map.
var new_obstacle_rid: RID = NavigationServer2D.obstacle_create()
var default_map_rid: RID = get_world_2d().get_navigation_map()

NavigationServer2D.obstacle_set_map(new_obstacle_rid, default_map_rid)
NavigationServer2D.obstacle_set_position(new_obstacle_rid, global_position)

# Use obstacle dynamic by increasing radius above zero.
NavigationServer2D.obstacle_set_radius(new_obstacle_rid, 5.0)

# Use obstacle static by adding a square that pushes agents out.
var outline = PackedVector2Array([Vector2(-100, -100), Vector2(100, -100), Vector2(100, 100), Vector2(-100, 100)])
NavigationServer2D.obstacle_set_vertices(new_obstacle_rid, outline)

# Enable the obstacle.
NavigationServer2D.obstacle_set_avoidance_enabled(new_obstacle
# ...
```

```gdscript
# Create a new "obstacle" and place it on the default navigation map.
var new_obstacle_rid: RID = NavigationServer3D.obstacle_create()
var default_map_rid: RID = get_world_3d().get_navigation_map()

NavigationServer3D.obstacle_set_map(new_obstacle_rid, default_map_rid)
NavigationServer3D.obstacle_set_position(new_obstacle_rid, global_position)

# Use obstacle dynamic by increasing radius above zero.
NavigationServer3D.obstacle_set_radius(new_obstacle_rid, 0.5)

# Use obstacle static by adding a square that pushes agents out.
var outline = PackedVector3Array([Vector3(-5, 0, -5), Vector3(5, 0, -5), Vector3(5, 0, 5), Vector3(-5, 0, 5)])
NavigationServer3D.obstacle_set_vertices(new_obstacle_rid, outline)
# Set the obstacle height on the y-axis.
NavigationServer3D.obstacle_set_height(new_obstac
# ...
```

---

## Using NavigationPathQueryObjects

> **Tip:** Path query parameters expose various options to improve pathfinding performance or lower memory consumption. They cater to more advanced pathfinding needs that the high-level nodes can not always cover. See the respective option sections below.

`NavigationPathQueryObjects` can be used together with `NavigationServer.query_path()` to obtain a heavily **customized** navigation path including optional **metadata** about the path.

This requires more setup compared to obtaining a normal NavigationPath but lets you tailor the pathfinding and provided path data to the different needs of a project.

NavigationPathQueryObjects consist of a pair of objects, a `NavigationPathQueryParameters` object holding the customization options for the query and a `NavigationPathQueryResult` that receives (regular) updates with the resulting path and metadata from the query.

2D and 3D versions of `NavigationPathQueryParameters` are available as [NavigationPathQueryParameters2D](../godot_gdscript_misc.md) and [NavigationPathQueryParameters3D](../godot_gdscript_misc.md) respectively.

2D and 3D versions of `NavigationPathQueryResult` are available as [NavigationPathQueryResult2D](../godot_gdscript_misc.md) and [NavigationPathQueryResult3D](../godot_gdscript_misc.md) respectively.

### Creating a basic path query

Both parameters and result are used as a pair with the `NavigationServer.query_path()` function.

For the available customization options, see further below. See also the descriptions for each parameter in the class reference.

While not a strict requirement, both objects are intended to be created once in advance, stored in a persistent variable for the agent and reused for every followup path query with updated parameters.

Reusing the same objects improves performance when frequently creating objects or allocating memory.

The following script creates the objects and provides a `query_path()` function to create new navigation paths. The resulting path is identical to using `NavigationServer.map_get_path()` while reusing the objects.

```gdscript
extends Node2D

# Prepare query objects.
var query_parameters := NavigationPathQueryParameters2D.new()
var query_result := NavigationPathQueryResult2D.new()

func query_path(p_start_position: Vector2, p_target_position: Vector2, p_navigation_layers: int = 1) -> PackedVector2Array:
    if not is_inside_tree():
        return PackedVector2Array()

    var map: RID = get_world_2d().get_navigation_map()

    if NavigationServer2D.map_get_iteration_id(map) == 0:
        # This map has never synced and is empty, no point in querying it.
        return PackedVector2Array()

    query_parameters.map = map
    query_parameters.start_position = p_start_position
    query_parameters.target_position = p_target_position
    query_parameters.navigation_layers = p_navigation_layers

    NavigationServer2
# ...
```

```gdscript
extends Node3D

# Prepare query objects.
var query_parameters := NavigationPathQueryParameters3D.new()
var query_result := NavigationPathQueryResult3D.new()

func query_path(p_start_position: Vector3, p_target_position: Vector3, p_navigation_layers: int = 1) -> PackedVector3Array:
    if not is_inside_tree():
        return PackedVector3Array()

    var map: RID = get_world_3d().get_navigation_map()

    if NavigationServer3D.map_get_iteration_id(map) == 0:
        # This map has never synced and is empty, no point in querying it.
        return PackedVector3Array()

    query_parameters.map = map
    query_parameters.start_position = p_start_position
    query_parameters.target_position = p_target_position
    query_parameters.navigation_layers = p_navigation_layers

    NavigationServer3
# ...
```

### Path postprocessing options

A path query search travels from the closest navigation mesh polygon edge to the closest edge along the available polygons. If possible it builds a polygon corridor towards the target position polygon.

This raw "search" polygon corridor path is not very optimized and usually a bad fit for agents to travel along. E.g. the closest edge point on a navigation mesh polygon might cause a huge detour for agents on larger polygons. In order to improve the quality of paths returned by the query various `path_postprocessing` options exist.

- The `PATH_POSTPROCESSING_CORRIDORFUNNEL` post-processing shortens paths by funneling paths around corners **inside the available polygon corridor**.

This is the default post-processing and usually also the most useful as it gives the shortest path result **inside the available polygon corridor**. If the polygon corridor is already suboptimal, e.g. due to a suboptimal navigation mesh layout, the funnel can snap to unexpected polygon corners causing detours.

- The `PATH_POSTPROCESSING_EDGECENTERED` post-processing forces all path points to be placed in the middle of the crossed polygon edges **inside the available polygon corridor**.

This post-processing is usually only useful when used with strictly tile-like navigation mesh polygons that are all evenly sized and where the expected path following is also constrained to cell centers, e.g. typical grid game with movement constrained to grid cell centers.

- The `PATH_POSTPROCESSING_NONE` post-processing returns the path as is how the pathfinding traveled **inside the available polygon corridor**.

This post-processing is very useful for debug as it shows how the path search traveled from closest edge point to closet edge point and what polygons it picked. A lot of unexpected or suboptimal path results can be immediately explained by looking at this raw path and polygon corridor.

### Path simplification

> **Tip:** Path simplification can help steering agents or agents that jitter on thin polygon edges.

If `simplify_path` is enabled a variant of the Ramer-Douglas-Peucker path simplification algorithm is applied to the path. This algorithm straightens paths by removing less relevant path points depending on the `simplify_epsilon` used.

Path simplification helps with all kinds of agent movement problems in "open fields" that are caused by having many unnecessary polygon edges. E.g. a terrain mesh when baked to a navigation mesh can cause an excessive polygon count due to all the small (but for pathfinding almost meaningless) height variations in the terrain.

Path simplification also helps with "steering" agents because they only have more critical corner path points to aim for.

> **Warning:** Path simplification is an additional final post-processing of the path. It adds extra performance costs to the query so only enable when actually needed.

> **Note:** Path simplification is exposed on the NavigationServer as a generic function. It can be used outside of navigation queries for all kinds of position arrays as well.

### Path metadata

> **Tip:** Disabling unneeded path metadata options can improve performance and lower memory consumption.

A path query can return additional metadata for every path point.

- The `PATH_METADATA_INCLUDE_TYPES` flag collects an array with the primitive information about the point owners, e.g. if a point belongs to a region or link.
- The `PATH_METADATA_INCLUDE_RIDS` flag collects an array with the [RIDs](../godot_gdscript_misc.md) of the point owners. Depending on point owner primitive, these RIDs can be used with the various NavigationServer functions related to regions or links.
- The `PATH_METADATA_INCLUDE_OWNERS` flag collects an array with the `ObjectIDs` of the point owners. These object IDs can be used with `@GlobalScope.instance_from_id()` to retrieve the node behind that object instance, e.g. a NavigationRegion or NavigationLink node.

By default all path metadata is collected as this metadata can be essential for more advanced navigation gameplay.

- E.g. to know what path point maps to what object or node owner inside the SceneTree.
- E.g. to know if a path point is the start or end of a navigation link that requires scripted takeover.

For the most basic path uses metadata is not always needed. Path metadata collection can be selectively disabled to gain some performance and reduce memory consumption.

### Excluding or including regions

> **Tip:** Region filters can greatly help with performance on large navigation maps that are region partitioned.

Query parameters allow limiting the pathfinding to specific region navigation meshes.

If a large navigation map is well partitioned into smaller regions this can greatly help with performance as the query can skip a large number of polygons at one of the earliest checks in the path search.

- By default and if left empty all regions of the queried navigation map are included.
- If a region [RID](../godot_gdscript_math_types.md) is added to the `excluded_regions` array the region's navigation mesh will be ignored in the path search.
- If a region [RID](../godot_gdscript_math_types.md) is added to the `included_regions` array the region's navigation mesh will be considered in the path search and also all other regions not included will be ignored as well.
- If a region ends up both included and excluded it is considered excluded.

Region filters are very effective for performance when paired with navigation region chunks that are aligned on a grid. This way the filter can be set to only include the start position chunk and surrounding chunks instead of the entire navigation map.

Even if the target might be outside these surrounding chunks (can always add more "rings") the pathfinding will try to create a path to the polygon closest to the target. This usually creates half-paths heading in the general direction that are good enough, all for a fraction of the performance cost of a full map search.

The following addition to the basic path query script showcases the idea how to integrate a region chunk mapping with the region filters. This is not a full working example.

```gdscript
extends Node2D

# ...

var chunk_id_to_region_rid: Dictionary[Vector2i, RID] = {}

func query_path(p_start_position: Vector2, p_target_position: Vector2, p_navigation_layers: int = 1) -> PackedVector2Array:

    # ...

    var regions_around_start_position: Array[RID] = []

    var chunk_rings: int = 1 # Increase for very small regions or more quality.
    var start_chunk_id: Vector2i = floor(p_start_position / float(chunk_size))

    for y: int in range(start_chunk_id.y - chunk_rings, start_chunk_id.y + chunk_rings):
        for x: int in range(start_chunk_id.x - chunk_rings, start_chunk_id.x + chunk_rings):
            var chunk_id: Vector2i = Vector2i(x, y)
            if chunk_id_to_region_rid.has(chunk_id):
                var region: RID = chunk_id_to_region_rid[chunk_id]

# ...
```

```gdscript
extends Node3D

# ...

var chunk_id_to_region_rid: Dictionary[Vector3i, RID] = {}

func query_path(p_start_position: Vector3, p_target_position: Vector3, p_navigation_layers: int = 1) -> PackedVector3Array:

    # ...

    var regions_around_start_position: Array[RID] = []

    var chunk_rings: int = 1 # Increase for very small regions or more quality.
    var start_chunk_id: Vector3i = floor(p_start_position / float(chunk_size))
    var y: int = 0 # Assume a planar navigation map for simplicity.

    for z: int in range(start_chunk_id.z - chunk_rings, start_chunk_id.z + chunk_rings):
        for x: int in range(start_chunk_id.x - chunk_rings, start_chunk_id.x + chunk_rings):
            var chunk_id: Vector3i = Vector3i(x, y, z)
            if chunk_id_to_region_rid.has(chunk_id):

# ...
```

### Path clipping and limits

> **Tip:** Sensibly set limits can greatly help with performance on large navigation maps, especially when targets end up being unreachable.

Query parameters allow clipping returned paths to specific lengths. These options clip the path as a part of post-processing. The path is still searched as if at full length, so it will have the same quality. Path length clipping can be helpful in creating paths that better fit constrained gameplay, e.g. tactical games with limited movement ranges.

- The `path_return_max_length` property can be used to clip the returned path to a specific max length.
- The `path_return_max_radius` property can be used to clip the returned path inside a circle (2D) or sphere (3D) radius around the start position.

Query parameters allow limiting the path search to only search up to a specific distance or a specific number of searched polygons. These options are for performance and affect the path search directly.

- The `path_search_max_distance` property can be used to stop the path search when going over this distance from the start position.
- The `path_search_max_polygons` property can be used to stop the path search when going over this searched polygon number.

When the path search is stopped by reaching a limit the path resets and creates a path from the start position polygon to the polygon found so far that is closest to the target position.

> **Warning:** While good for performance, if path search limit values are set too low they can affect the path quality very negatively. Depending on polygon layout and search pattern the returned paths might go into completely wrong directions instead of the direction of the target.

---

## Using NavigationPaths

### Obtaining a NavigationPath

Navigation paths can be directly queried from the NavigationServer and do not require any additional nodes or objects as long as the navigation map has a navigation mesh to work with.

To obtain a 2D path, use `NavigationServer2D.map_get_path(map, from, to, optimize, navigation_layers)`.

To obtain a 3D path, use `NavigationServer3D.map_get_path(map, from, to, optimize, navigation_layers)`.

For more customizable navigation path queries that require additional setup see Using NavigationPathQueryObjects.

One of the required parameters for the query is the RID of the navigation map. Each game world has a default navigation map automatically created. The default navigation maps can be retrieved with `get_world_2d().get_navigation_map()` from any Node2D inheriting node or `get_world_3d().get_navigation_map()` from any Node3D inheriting node. The second and third parameters are the starting position and the target position as Vector2 for 2D or Vector3 for 3D.

If the `optimized` parameter is `true`, path positions will be shortened along polygon corners with an additional funnel algorithm pass. This works well for free movement on navigation meshes with unequally sized polygons as the path will hug around corners along the polygon corridor found by the A* algorithm. With small cells the A* algorithm creates a very narrow funnel corridor that can create ugly corner paths when used with grids.

If the `optimized` parameter is `false`, path positions will be placed at the center of each polygon edge. This works well for pure grid movement on navigation meshes with equally sized polygons as the path will go through the center of the grid cells. Outside of grids due to polygons often covering large open areas with a single, long edge this can create paths with unnecessary long detours.

```gdscript
extends Node2D

# Basic query for a navigation path using the default navigation map.

func get_navigation_path(p_start_position: Vector2, p_target_position: Vector2) -> PackedVector2Array:
    if not is_inside_tree():
        return PackedVector2Array()

    var default_map_rid: RID = get_world_2d().get_navigation_map()
    var path: PackedVector2Array = NavigationServer2D.map_get_path(
        default_map_rid,
        p_start_position,
        p_target_position,
        true
    )
    return path
```

```gdscript
extends Node3D

# Basic query for a navigation path using the default navigation map.

func get_navigation_path(p_start_position: Vector3, p_target_position: Vector3) -> PackedVector3Array:
    if not is_inside_tree():
        return PackedVector3Array()

    var default_map_rid: RID = get_world_3d().get_navigation_map()
    var path: PackedVector3Array = NavigationServer3D.map_get_path(
        default_map_rid,
        p_start_position,
        p_target_position,
        true
    )
    return path
```

A returned `path` by the NavigationServer will be a `PackedVector2Array` for 2D or a `PackedVector3Array` for 3D. These are just a memory-optimized `Array` of vector positions. All position vectors inside the array are guaranteed to be inside a NavigationPolygon or NavigationMesh. The path array, if not empty, has the navigation mesh position closest to the starting position at the first index `path[0]` position. The closest available navigation mesh position to the target position is the last index `path[path.size()-1]` position. All indexes between are the path points that an actor should follow to reach the target without leaving the navigation mesh.

> **Note:** If the target position is on a different navigation mesh that is not merged or connected the navigation path will lead to the closest possible position on the starting position navigation mesh.

The following script moves a Node3D inheriting node along a navigation path using the default navigation map by setting the target position with `set_movement_target()`.

```gdscript
@onready var default_3d_map_rid: RID = get_world_3d().get_navigation_map()

var movement_speed: float = 4.0
var movement_delta: float
var path_point_margin: float = 0.5

var current_path_index: int = 0
var current_path_point: Vector3
var current_path: PackedVector3Array

func set_movement_target(target_position: Vector3):

    var start_position: Vector3 = global_transform.origin

    current_path = NavigationServer3D.map_get_path(
        default_3d_map_rid,
        start_position,
        target_position,
        true
    )

    if not current_path.is_empty():
        current_path_index = 0
        current_path_point = current_path[0]

func _physics_process(delta):

    if current_path.is_empty():
        return

    movement_delta = movement_speed * delta

    if global_transform.origin
# ...
```

---

## Using NavigationRegions

NavigationRegions are the visual Node representation of a **region** of the navigation **map** on the NavigationServer. Each NavigationRegion node holds a resource for the navigation mesh data.

Both 2D and 3D version are available as [NavigationRegion2D](../godot_gdscript_nodes_2d.md) and [NavigationRegion3D](../godot_gdscript_nodes_3d.md) respectively.

Individual NavigationRegions upload their 2D NavigationPolygon or 3D NavigationMesh resource data to the NavigationServer. The NavigationServer map turns this information into a combined navigation map for pathfinding.

To create a navigation region using the scene tree add a `NavigationRegion2D` or `NavigationRegion3D` node to the scene. All regions require a navigation mesh resource to function. See Using navigation meshes to learn how to create and apply navigation meshes.

NavigationRegions will automatically push `global_transform` changes to the region on the NavigationServer which makes them suitable for moving platforms. The NavigationServer will attempt to connect the navigation meshes of individual regions when they are close enough. For more details see Connecting navigation meshes. To connect NavigationRegions over arbitrary distances see Using NavigationLinks to learn how to create and use `NavigationLinks`.

> **Warning:** While changing the transform of a NavigationRegion node does update the region position on the NavigationServer, changing the scale does not. A navigation mesh resource has no scale and needs to be fully updated when source geometry changes scale.

Regions can be enabled / disabled and if disabled will not contribute to future pathfinding queries.

> **Note:** Existing paths will not be automatically updated when a region gets enabled / disabled.

### Creating new navigation regions

New NavigationRegion nodes will automatically register to the default world navigation map for their 2D/3D dimension.

The region RID can then be obtained from NavigationRegion Nodes with `get_rid()`.

```gdscript
extends NavigationRegion2D

var navigationserver_region_rid: RID = get_rid()
```

```gdscript
extends NavigationRegion3D

var navigationserver_region_rid: RID = get_rid()
```

New regions can also be created with the NavigationServer API and added to any existing map.

If regions are created with the NavigationServer API directly they need to be assigned a navigation map manually.

```gdscript
extends Node2D

func _ready() -> void:
    var new_region_rid: RID = NavigationServer2D.region_create()
    var default_map_rid: RID = get_world_2d().get_navigation_map()
    NavigationServer2D.region_set_map(new_region_rid, default_map_rid)
```

```gdscript
extends Node3D

func _ready() -> void:
    var new_region_rid: RID = NavigationServer3D.region_create()
    var default_map_rid: RID = get_world_3d().get_navigation_map()
    NavigationServer3D.region_set_map(new_region_rid, default_map_rid)
```

> **Note:** Navigation regions can only be assigned to a single navigation map. If an existing region is assigned to a new navigation map it will leave the old map.

---
