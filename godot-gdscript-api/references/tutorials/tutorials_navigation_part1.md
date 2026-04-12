# Godot 4 GDScript Tutorials — Navigation (Part 1)

> 10 tutorials. GDScript-specific code examples.

## Connecting navigation meshes

Different NavigationMeshes are automatically merged by the NavigationServer when at least two vertex positions of one edge exactly overlap.

To connect over arbitrary distances see Using NavigationLinks.

The same is true for multiple NavigationPolygon resources. As long as their outline points overlap exactly the NavigationServer will merge them. NavigationPolygon outlines must be from different NavigationPolygon resources to connect.

Overlapping or intersecting outlines on the same NavigationPolygon will fail the navigation mesh creation. Overlapping or intersecting outlines from different NavigationPolygons will often fail to create the navigation region edge connections on the NavigationServer and should be avoided.

> **Warning:** Exactly means exactly for the vertex position merge. Small float errors that happen quite regularly with imported meshes will prevent a successful vertex merge.

Alternatively navigation meshes are not merged but still considered as **connected** by the NavigationServer when their edges are nearly parallel and within distance to each other. The connection distance is defined by the `edge_connection_margin` for each navigation map. In many cases navigation mesh edges cannot properly connect when they partly overlap. Better avoid any navigation mesh overlap at all time for a consistent merge behavior.

If navigation debug is enabled and the NavigationServer active the established navigation mesh connections will be visualized. See Navigation debug tools for more info about navigation debug options.

The default 2D `edge_connection_margin` can be changed in the ProjectSettings under `navigation/2d/default_edge_connection_margin`.

The default 3D `edge_connection_margin` can be changed in the ProjectSettings under `navigation/3d/default_edge_connection_margin`.

The edge connection margin value of any navigation map can also be changed at runtime with the NavigationServer API.

```gdscript
extends Node2D

func _ready() -> void:
    # 2D margins are designed to work with 2D "pixel" values.
    var default_map_rid: RID = get_world_2d().get_navigation_map()
    NavigationServer2D.map_set_edge_connection_margin(default_map_rid, 50.0)
```

```gdscript
extends Node3D

func _ready() -> void:
    # 3D margins are designed to work with 3D world unit values.
    var default_map_rid: RID = get_world_3d().get_navigation_map()
    NavigationServer3D.map_set_edge_connection_margin(default_map_rid, 0.5)
```

> **Note:** Changing the edge connection margin will trigger a full update of all navigation mesh connections on the NavigationServer.

---

## Navigation debug tools

> **Note:** The debug tools, properties and functions are only available in Godot debug builds. Do not use any of them in code that will be part of a release build.

### Enabling navigation debug

The navigation debug visualizations are enabled by default inside the editor. To visualize navigation meshes and connections at runtime too, enable the option **Visible Navigation** in the editor **Debug** menu.

In Godot debug builds the navigation debug can also be toggled through the NavigationServer singletons from scripts.

```gdscript
NavigationServer2D.set_debug_enabled(false)
NavigationServer3D.set_debug_enabled(true)
```

Debug visualizations are currently based on Nodes in the SceneTree. If the [NavigationServer2D](../godot_gdscript_misc.md) or [NavigationServer3D](../godot_gdscript_misc.md) APIs are used exclusively then changes will not be reflected by the debug navigation tools.

### Navigation debug settings

The appearance of navigation debug can be changed in the ProjectSettings under `debug/shapes/navigation`. Certain debug features can also be enabled or disabled at will but may require a scene restart to take effect.

### Debug navigation mesh polygons

If `enable_edge_lines` is enabled, the edges of navigation mesh polygons will be highlighted. If `enable_edge_lines_xray` is also enabled, the edges of navigation meshes will be visible through geometry.

If `enable_geometry_face_random_color` is enabled, the color of each navigation mesh face will be mixed with a random color that is itself mixed with the color specified in `geometry_face_color`.

### Debug edge connections

When two navigation meshes are connected within `edge_connection_margin` distance, the connection is overlaid. The color of the overlay is controlled by `edge_connection_color`. The connections can be made visible through geometry with `enable_edge_connections_xray`.

> **Note:** Edge connections are only visible when the NavigationServer is active.

### Debug performance

To measure NavigationServer performance a dedicated monitor exists that can be found within the Editor Debugger under _Debugger->Monitors->Navigation Process_.

Navigation Process shows how long the NavigationServer spends updating its internals this update frame in milliseconds. Navigation Process works similar to Process for visual frame rendering and Physics Process for collision and fixed updates.

Navigation Process accounts for all updates to **navigation maps**, **navigation regions** and **navigation agents** as well as all the **avoidance calculations** for the update frame.

> **Note:** Navigation Process does NOT include pathfinding performance cause pathfinding operates on the navigation map data independently from the server process update.

Navigation Process should be in general kept as low and as stable as possible for runtime performance to avoid frame rate issues. Note that since the NavigationServer process update happens in the middle of the physics update an increase in Navigation Process will automatically increase Physics Process by the same amount.

Navigation also provides more detailed statistics about the current navigation related objects and navigation map composition on the NavigationServer.

Navigation statistics shown here can not be judged as good or bad for performance as it depends entirely on the project what can be considered as reasonable or horribly excessive.

Navigation statistics help with identifying performance bottlenecks that are less obvious because the source might not always have a visible representation. E.g. pathfinding performance issues created by overly detailed navigation meshes with thousand of edges / polygons or problems caused by procedural navigation gone wrong.

---

## Support different actor area access

A typical example for different area access in gameplay are doors that connect rooms with different navigation meshes and are not accessible by all actors all the time.

Add a NavigationRegion at the door position. Add an appropriate navigation mesh the size of the door that can connect with the surrounding navigation meshes. In order to control access, enable / disable navigation layer bits so path queries that use the same navigation layer bits can find a path through the "door" navigation mesh.

The bitmask can act as a set of door keys or abilities and only actors with at least one matching and enabled bit layer in their pathfinding query will find a path through this region. See Using NavigationLayers for more information on how to work with navigation layers and the bitmask.

The entire "door" region can also be enabled / disable if required but if disabled will block access for all path queries.

Prefer working with navigation layers in path queries whenever possible as enabling or disabling navigation layers on a region triggers a costly recalculation of the navigation map connections.

> **Warning:** Changing navigation layers will only affect new path queries but not automatically update existing paths.

---

## Support different actor locomotion

To support different actor locomotion like crouching and crawling, a similar map setup as supporting Support different actor types is required.

Bake different navigation meshes with an appropriate height for crouched or crawling actors so they can find paths through those narrow sections in your game world.

When an actor changes locomotion state, e.g. stands up, starts crouching or crawling, query the appropriate map for a path.

If the avoidance behavior should also change with the locomotion e.g. only avoid while standing or only avoid other agents in the same locomotion state, switch the actor's avoidance agent to another avoidance map with each locomotion change.

```gdscript
func update_path():

    if actor_standing:
        path = NavigationServer3D.map_get_path(standing_navigation_map_rid, start_position, target_position, true)
    elif actor_crouching:
        path = NavigationServer3D.map_get_path(crouched_navigation_map_rid, start_position, target_position, true)
    elif actor_crawling:
        path = NavigationServer3D.map_get_path(crawling_navigation_map_rid, start_position, target_position, true)

func change_agent_avoidance_state():

    if actor_standing:
        NavigationServer3D.agent_set_map(avoidance_agent_rid, standing_navigation_map_rid)
    elif actor_crouching:
        NavigationServer3D.agent_set_map(avoidance_agent_rid, crouched_navigation_map_rid)
    elif actor_crawling:
        NavigationServer3D.agent_set_map(avoidance_agent_rid, cra
# ...
```

> **Note:** While a path query can be execute immediately for multiple maps, the avoidance agent map switch will only take effect after the next server synchronization.

---

## Support different actor types

To support different actor types due to e.g. their sizes each type requires its own navigation map and navigation mesh baked with an appropriated agent radius and height. The same approach can be used to distinguish between e.g. landwalking, swimming or flying agents.

> **Note:** Agents are exclusively defined by a radius and height value for baking navigation meshes, pathfinding and avoidance. More complex shapes are not supported.

```gdscript
# Create a navigation mesh resource for each actor size.
var navigation_mesh_standard_size: NavigationMesh = NavigationMesh.new()
var navigation_mesh_small_size: NavigationMesh = NavigationMesh.new()
var navigation_mesh_huge_size: NavigationMesh = NavigationMesh.new()

# Set appropriated agent parameters.
navigation_mesh_standard_size.agent_radius = 0.5
navigation_mesh_standard_size.agent_height = 1.8
navigation_mesh_small_size.agent_radius = 0.25
navigation_mesh_small_size.agent_height = 0.7
navigation_mesh_huge_size.agent_radius = 1.5
navigation_mesh_huge_size.agent_height = 2.5

# Get the root node to parse geometry for the baking.
var root_node: Node3D = get_node("NavigationMeshBakingRootNode")

# Create the source geometry resource that will hold the parsed geometry data.
var source_g
# ...
```

---

## 2D navigation overview

Godot provides multiple objects, classes and servers to facilitate grid-based or mesh-based navigation and pathfinding for 2D and 3D games. The following section provides a quick overview over all available navigation related objects in Godot for 2D scenes and their primary use.

Godot provides the following objects and classes for 2D navigation:

- **Astar2D**
  : `Astar2D` objects provide an option to find the shortest path in a graph of weighted **points**.

The AStar2D class is best suited for cell-based 2D gameplay that does not require actors to reach any possible position within an area but only predefined, distinct positions.

- **AstarGrid2D**
  : `AstarGrid2D` is a variant of AStar2D that is specialized for partial 2D grids.

AstarGrid2D is simpler to use when applicable because it doesn't require you to manually create points and connect them together.

- **NavigationServer2D**
  : `NavigationServer2D` provides a powerful server API to find the shortest path between two positions on an area defined by a navigation mesh.

The NavigationServer is best suited for 2D realtime gameplay that does require actors to reach any possible position within a navigation mesh defined area. Mesh-based navigation scales well with large game worlds as a large area can often be defined with a single polygon when it would require many, many grid cells.

The NavigationServer holds different navigation maps that each consist of regions that hold navigation mesh data. Agents can be placed on a map for avoidance calculation. RIDs are used to reference internal maps, regions, and agents when communicating with the server.

**The following NavigationServer RID types are available.**
: - **NavMap RID**
: Reference to a specific navigation map that holds regions and agents. The map will attempt to join the navigation meshes of the regions by proximity. The map will synchronize regions and agents each physics frame.

- **NavRegion RID**
  : Reference to a specific navigation region that can hold navigation mesh data. The region can be enabled / disabled or the use restricted with a navigation layer bitmask.
- **NavLink RID**
  : Reference to a specific navigation link that connects two navigation mesh positions over arbitrary distances.
- **NavAgent RID**
  : Reference to a specific avoidance agent. The avoidance is specified by a radius value.
- **NavObstacle RID**
  : Reference to a specific avoidance obstacle used to affect and constrain the avoidance velocity of agents.

The following scene tree nodes are available as helpers to work with the NavigationServer2D API.

- **NavigationRegion2D Node**
  : A Node that holds a NavigationPolygon resource that defines a navigation mesh for the NavigationServer2D.

- The region can be enabled / disabled.
- The use in pathfinding can be further restricted through the `navigation_layers` bitmask.
- The NavigationServer2D will join the navigation meshes of regions by proximity for a combined navigation mesh.
- **NavigationLink2D Node**
  : A Node that connects two positions on navigation meshes over arbitrary distances for pathfinding.

- The link can be enabled / disabled.
- The link can be made one-way or bidirectional.
- The use in pathfinding can be further restricted through the `navigation_layers` bitmask.

Links tell the pathfinding that a connection exists and at what cost. The actual agent handling and movement needs to happen in custom scripts.

- **NavigationAgent2D Node**
  : A helper Node used to facilitate common NavigationServer2D API calls for pathfinding and avoidance. Use this Node with a Node2D inheriting parent Node.
- **NavigationObstacle2D Node**
  : A Node that can be used to affect and constrain the avoidance velocity of avoidance enabled agents. This Node does NOT affect the pathfinding of agents. You need to change the navigation meshes for that instead.

The 2D navigation meshes are defined with the following resources:

- **NavigationPolygon Resource**
  : A resource that holds 2D navigation mesh data. It provides polygon drawing tools to allow defining navigation areas inside the Editor as well as at runtime.

- The NavigationRegion2D Node uses this resource to define its navigation area.
- The NavigationServer2D uses this resource to update the navigation mesh of individual regions.
- The TileSet Editor creates and uses this resource internally when defining tile navigation areas.

> **See also:** You can see how 2D navigation works in action using the [2D Navigation Polygon](https://github.com/godotengine/godot-demo-projects/tree/master/2d/navigation) and [Grid-based Navigation with AStarGrid2D](https://github.com/godotengine/godot-demo-projects/tree/master/2d/navigation_astar) demo projects.

### Setup for 2D scene

The following steps show the basic setup for minimal viable navigation in 2D. It uses the NavigationServer2D and a NavigationAgent2D for path movement.

1. Add a NavigationRegion2D Node to the scene.
2. Click on the region node and add a new NavigationPolygon Resource to the region node.
3. Define the movable navigation area with the NavigationPolygon draw tool. Then click the Bake NavigationPolygon button on the toolbar.

> **Note:** The navigation mesh defines the area where an actor can stand and move with its center. Leave enough margin between the navigation polygon edges and collision objects to not get path following actors repeatedly stuck on collision. 4. Add a CharacterBody2D node in the scene with a basic collision shape and a sprite or mesh for visuals. 5. Add a NavigationAgent2D node below the character node. 6. Add the following script to the CharacterBody2D node. We make sure to set a movement target after the scene has fully loaded and the NavigationServer had time to sync.

```gdscript
extends CharacterBody2D

var movement_speed: float = 200.0
var movement_target_position: Vector2 = Vector2(60.0,180.0)

@onready var navigation_agent: NavigationAgent2D = $NavigationAgent2D

func _ready():
    # These values need to be adjusted for the actor's speed
    # and the navigation layout.
    navigation_agent.path_desired_distance = 4.0
    navigation_agent.target_desired_distance = 4.0

    # Make sure to not await during _ready.
    actor_setup.call_deferred()

func actor_setup():
    # Wait for the first physics frame so the NavigationServer can sync.
    await get_tree().physics_frame

    # Now that the navigation map is no longer empty, set the movement target.
    set_movement_target(movement_target_position)

func set_movement_target(movement_target: Vector2):
    navigat
# ...
```

> **Note:** On the first frame the NavigationServer map has not synchronized region data and any path query will return empty. Wait for the NavigationServer synchronization by awaiting one frame in the script.

---

## 3D navigation overview

Godot provides multiple objects, classes and servers to facilitate grid-based or mesh-based navigation and pathfinding for 2D and 3D games. The following section provides a quick overview over all available navigation related objects in Godot for 3D scenes and their primary use.

Godot provides the following objects and classes for 3D navigation:

- **Astar3D**
  : `Astar3D` objects provide an option to find the shortest path in a graph of weighted **points**.

The AStar3D class is best suited for cell-based 3D gameplay that does not require actors to reach any possible position within an area but only predefined, distinct positions.

- **NavigationServer3D**
  : `NavigationServer3D` provides a powerful server API to find the shortest path between two positions on an area defined by a navigation mesh.

The NavigationServer is best suited for 3D realtime gameplay that does require actors to reach any possible position within a navigation mesh defined area. Mesh-based navigation scales well with large game worlds as a large area can often be defined with a single polygon when it would require many, many grid cells.

The NavigationServer holds different navigation maps that each consist of regions that hold navigation mesh data. Agents can be placed on a map for avoidance calculation. RIDs are used to reference internal maps, regions, and agents when communicating with the server.

**The following NavigationServer RID types are available.**
: - **NavMap RID**
: Reference to a specific navigation map that holds regions and agents. The map will attempt to join the navigation meshes of the regions by proximity. The map will synchronize regions and agents each physics frame.

- **NavRegion RID**
  : Reference to a specific navigation region that can hold navigation mesh data. The region can be enabled / disabled or the use restricted with a navigation layer bitmask.
- **NavLink RID**
  : Reference to a specific navigation link that connects two navigation mesh positions over arbitrary distances.
- **NavAgent RID**
  : Reference to a specific avoidance agent. The avoidance is defined by a radius value.
- **NavObstacle RID**
  : Reference to a specific avoidance obstacle used to affect and constrain the avoidance velocity of agents.

The following scene tree nodes are available as helpers to work with the NavigationServer3D API.

- **NavigationRegion3D Node**
  : A Node that holds a Navigation Mesh resource that defines a navigation mesh for the NavigationServer3D.

- The region can be enabled / disabled.
- The use in pathfinding can be further restricted through the `navigation_layers` bitmask.
- The NavigationServer3D will join the navigation meshes of regions by proximity for a combined navigation mesh.
- **NavigationLink3D Node**
  : A Node that connects two positions on navigation meshes over arbitrary distances for pathfinding.

- The link can be enabled / disabled.
- The link can be made one-way or bidirectional.
- The use in pathfinding can be further restricted through the `navigation_layers` bitmask.

Links tell the pathfinding that a connection exists and at what cost. The actual agent handling and movement needs to happen in custom scripts.

- **NavigationAgent3D Node**
  : A helper Node used to facilitate common NavigationServer3D API calls for pathfinding and avoidance. Use this Node with a Node3D inheriting parent Node.
- **NavigationObstacle3D Node**
  : A Node that can be used to affect and constrain the avoidance velocity of avoidance enabled agents. This Node does NOT affect the pathfinding of agents. You need to change the navigation meshes for that instead.

The 3D navigation meshes are defined with the following resources:

- **NavigationMesh Resource**
  : A resource that holds 3D navigation mesh data. It provides 3D geometry baking options to define navigation areas inside the Editor as well as at runtime.

- The NavigationRegion3D Node uses this resource to define its navigation area.
- The NavigationServer3D uses this resource to update the navigation mesh of individual regions.
- The GridMap Editor uses this resource when specific navigation meshes are defined for each grid cell.

> **See also:** You can see how 3D navigation works in action using the [3D Navigation demo project](https://github.com/godotengine/godot-demo-projects/tree/master/3d/navigation).

### Setup for 3D scene

The following steps show a basic setup for minimal viable navigation in 3D. It uses the NavigationServer3D and a NavigationAgent3D for path movement.

1. Add a NavigationRegion3D Node to the scene.
2. Click on the region node and add a new [NavigationMesh](../godot_gdscript_misc.md) Resource to the region node.
3. Add a new MeshInstance3D node as a child of the region node.
4. Select the MeshInstance3D node and add a new PlaneMesh and increase the xy size to 10.
5. Select the region node again and press the "Bake Navmesh" button on the top bar.
6. Now a transparent navigation mesh appears that hovers some distance on top of the PlaneMesh.
7. Add a CharacterBody3D node in the scene with a basic collision shape and some mesh for visuals.
8. Add a NavigationAgent3D node below the character node.
9. Add a script to the CharacterBody3D node with the following content. We make sure to set a movement target after the scene has fully loaded and the NavigationServer had time to sync. Also, add a Camera3D and some light and environment to see something.

```gdscript
extends CharacterBody3D

var movement_speed: float = 2.0
var movement_target_position: Vector3 = Vector3(-3.0,0.0,2.0)

@onready var navigation_agent: NavigationAgent3D = $NavigationAgent3D

func _ready():
    # These values need to be adjusted for the actor's speed
    # and the navigation layout.
    navigation_agent.path_desired_distance = 0.5
    navigation_agent.target_desired_distance = 0.5

    # Make sure to not await during _ready.
    actor_setup.call_deferred()

func actor_setup():
    # Wait for the first physics frame so the NavigationServer can sync.
    await get_tree().physics_frame

    # Now that the navigation map is no longer empty, set the movement target.
    set_movement_target(movement_target_position)

func set_movement_target(movement_target: Vector3):
    navigat
# ...
```

> **Note:** On the first frame the NavigationServer map has not synchronized region data and any path query will return empty. Wait for the NavigationServer synchronization by awaiting one frame in the script.

---

## Optimizing Navigation Performance

Common Navigation related performance problems can be categorized into the following topics:

- Performance problems with parsing scene tree nodes for navigation mesh baking.
- Performance problems with baking the actual navigation mesh.
- Performance problems with NavigationAgent path queries.
- Performance problems with the actual path search.
- Performance problems with synchronizing the navigation map.

In the following sections information can be found on how to identify and fix or at least mitigate their impact on framerates.

### Performance problems with parsing scene tree nodes

> **Tip:** Prefer using simple shapes with as few edges as possible e.g. nothing rounded like a circle, sphere or torus. Prefer using physics collision shapes over complex visual meshes as source geometry as meshes need to be copied from the GPU and are commonly much more detailed than necessary.

In general avoid using very complex geometry as source geometry for baking navigation meshes. E.g. never use a very detailed visual mesh, as parsing its shape to data arrays and voxelizing it for the navigation mesh baking will take a long time for no real quality gain on the final navigation mesh. Instead, use a very simplified level of detail version of a shape. Even better, use very primitive shapes like boxes and rectangles that only roughly cover the same geometry but still yield a baked result good enough for pathfinding.

Prefer using simple physics collision shapes over visual meshes, as the source geometry for baking navigation meshes. Physics shapes are by default very limited and optimized shapes that are easy and quick to parse. A visual mesh on the other hand can range from simple to complex. On top, to gain access to visual mesh data the parser needs to request the mesh data arrays from the RenderingServer as visual mesh data is stored directly on the GPU and is not cached on the CPU. This requires locking the RenderingServer thread and can severely impact framerate at runtime while the rendering runs multi-threaded. If the rendering runs single-threaded, the framerate impact might be even worse and the mesh parsing might freeze the entire game for a few seconds on complex meshes.

### Performance problems with navigation mesh baking

> **Tip:** At runtime, always prefer to use a background thread for baking navigation meshes. Increase NavigationMesh `cell_size` and `cell_height` to create less voxels. Change the `SamplePartitionType` from watershed to monotone or layers to gain baking performance.

> **Warning:** NEVER scale source geometry with nodes to avoid precision errors. Most scale applies only visually and shapes that are very large at their base scale require still a lot of extra processing even while downscaled.

Baking navigation meshes at runtime should always be done in a background thread if possible. Even small sized navigation meshes can take far longer to bake than what is possible to squeeze into a single frame, at least if the framerate should stay at a bearable level.

Complexity of source geometry data parsed from scene tree nodes has big impact on baking performance as everything needs to be mapped to a grid / voxels. For runtime baking performance the NavigationMesh cell size and cell height should be set as high as possible without causing navigation mesh quality problems for a game. If cell size or cell height is set too low the baking is forced to create an excessive amount of voxels to process the source geometry. If the source geometry spans over a very large game world it is even possible that the baking process runs out of memory in the middle and crashes the game. The partition type can also be lowered depending on how complex the games source geometry is to gain some performance. E.g. games with mostly flat surfaces with blocky geometry can get away with the monotone or layers mode that are a lot faster to bake (e.g. because they require no distance field pass).

Never scale source geometry with nodes. Not only can it result in a lot of precision errors with wrongly matched vertices and edges but also some scaling only exists as visuals and not in the actual parsed data. E.g. if a mesh is downscaled visually in the Editor, e.g. the scale set to 0.001 on a MeshInstance, the mesh still requires a gigantic and very complex voxel grid to be processed for the baking.

### Performance problems with NavigationAgent path queries

> **Tip:** Avoid unnecessary path resets and queries every frame in NavigationAgent scripts. Avoid updating all NavigationAgent paths in the same frame.

Logical errors and wasteful operations in the custom NavigationAgent scripts are very common causes of performance issues, e.g. watch out for resetting the path every single frame. By default NavigationAgents are optimized to only query new paths when the target position changes, the navigation map changes or they are forced too far away from the desired path distance.

E.g. when AI should move to the player, the target position should not be set to the player position every single frame as this queries a new path every frame. Instead, the distance from the current target position to the player position should be compared and only when the player has moved too far away a new target position should be set.

Do not check beforehand if a target position is reachable every frame. What looks like an innocent check is the equivalent of an expensive path query behind the scene. If the plan is to request a new path anyway should the position be reachable, a path should be queried directly. By looking at the last position of the returned path and if that position is in a "reachable" distance to the checked position it answers the "is this position reachable?" question. This avoids doing the equivalent of two full path queries every frame for the same NavigationAgent.

Divide the total number of NavigationAgents into update groups or use random timers so that they do not all request new paths in the same frame.

### Performance problems with the actual path search

> **Tip:** Optimize overdetailed navigation meshes by reducing the amount of polygons and edges.

The cost of the actual path search correlates directly with the amount of navigation mesh polygons and edges and not the real size of a game world. If a giant game world uses very optimized navigation meshes with only few polygons that cover large areas, performance should be acceptable. If the game world is splintered into very small navigation meshes that each have tiny polygons (like for TileMaps) pathfinding performance will be reduced.

A common problem is a sudden performance drop when a target position is not reachable in a path query. This performance drop is "normal" and the result of a too large, too unoptimized navigation mesh with way to much polygons and edges to search through. In normal path searches where the target position can be reached quickly the pathfinding will do an early exit as soon as the position is reached which can hide this lack of optimization for a while. If the target position can not be reached the pathfinding has to do a far longer search through the available polygons to confirm that the position is absolutely not reachable.

### Performance problems with navigation map synchronization

> **Tip:** Merge navigation meshes polygons by vertex instead of by edge connection wherever possible.

When changes are made to e.g. navigation meshes or navigation regions, the NavigationServer needs to synchronize the navigation map. Depending on the complexity of navigation meshes, this can take a significant amount of time which may impact the framerate.

The NavigationServer merges navigation meshes either by vertex or by edge connection. The merge by vertex happens when the two vertex of two different edges land in the same map grid cells. This is a rather quick and low-cost operation. The merge by edge connection happens in a second pass for all still unmerged edges. All the free edges are checked for possible edge connections by both distance and angle which is rather costly.

So apart from the general rule to have as few polygon edges as possible, as many edges as possible should be merged by vertex upfront so only a few edges are left for the more costly edge connection calculation. The debug Navigation PerformanceMonitor can be used to get statistics on how many polygons and edges are available and how many of them are unmerged or not merged by vertex. If the ratio between vertex merged and edge connections is way off (vertex should be significantly higher) the navigation meshes are properly created or placed very inefficient.

---

## Using NavigationAgents

NavigationsAgents are helper nodes that combine functionality for pathfinding, path following and agent avoidance for a Node2D/3D inheriting parent node. They facilitate common calls to the NavigationServer API on behalf of the parent actor node in a more convenient manner for beginners.

2D and 3D version of NavigationAgents are available as [NavigationAgent2D](../godot_gdscript_nodes_2d.md) and [NavigationAgent3D](../godot_gdscript_nodes_3d.md) respectively.

New NavigationAgent nodes will automatically join the default navigation map on the [World2D](../godot_gdscript_misc.md)/[World3D](../godot_gdscript_misc.md).

NavigationsAgent nodes are optional and not a hard requirement to use the navigation system. Their entire functionality can be replaced with scripts and direct calls to the NavigationServer API.

> **Tip:** For more advanced uses consider Using NavigationPathQueryObjects over NavigationAgent nodes.

### NavigationAgent Pathfinding

NavigationAgents query a new navigation path on their current navigation map when their `target_position` is set with a global position.

The result of the pathfinding can be influenced with the following properties.

- The `navigation_layers` bitmask can be used to limit the navigation meshes that the agent can use.
- The `pathfinding_algorithm` controls how the pathfinding travels through the navigation mesh polygons in the path search.
- The `path_postprocessing` sets if or how the raw path corridor found by the pathfinding is altered before it is returned.
- The `path_metadata_flags` enable the collection of additional path point meta data returned by the path.
- The `simplify_path` and `simplify_epsilon` properties can be used to remove less critical points from the path.

> **Warning:** Disabling path meta flags will disable related signal emissions on the agent.

### NavigationAgent Pathfollowing

After a `target_position` has been set for the agent, the next position to follow in the path can be retrieved with the `get_next_path_position()` function.

Once the next path position is received, move the parent actor node of the agent towards this path position with your own movement code.

> **Note:** The navigation system never moves the parent node of a NavigationAgent. The movement is entirely in the hands of users and their custom scripts.

NavigationAgents have their own internal logic to proceed with the current path and call for updates.

The `get_next_path_position()` function is responsible for updating many of the agent's internal states and properties. The function should be repeatedly called _once_ every `physics_process` until `is_navigation_finished()` tells that the path is finished. The function should not be called after the target position or path end has been reached as it can make the agent jitter in place due to the repeated path updates. Always check very early in script with `is_navigation_finished()` if the path is already finished.

The following distance properties influence the path following behavior.

- At `path_desired_distance` from the next path position, the agent advances its internal path index to the subsequent next path position.
- At `target_desired_distance` from the target path position, the agent considers the target position to be reached and the path at its end.
- At `path_max_distance` from the ideal path to the next path position, the agent requests a new path because it was pushed too far off.

The important updates are all triggered with the `get_next_path_position()` function when called in `_physics_process()`.

NavigationAgents can be used with `process` but are still limited to a single update that happens in `physics_process`.

Script examples for various nodes commonly used with NavigationAgents can be found further below.

#### Pathfollowing common problems

There are some common user problems and important caveats to consider when writing agent movement scripts.

- **The path is returned empty**
  : If an agent queries a path before the navigation map synchronisation, e.g. in a `_ready()` function, the path might return empty. In this case the `get_next_path_position()` function will return the same position as the agent parent node and the agent will consider the path end reached. This is fixed by making a deferred call or using a callback e.g. waiting for the navigation map changed signal.
- **The agent is stuck dancing between two positions**
  : This is usually caused by very frequent path updates every single frame, either deliberate or by accident (e.g. max path distance set too short). The pathfinding needs to find the closest position that are valid on navigation mesh. If a new path is requested every single frame the first path positions might end up switching constantly in front and behind the agent's current position, causing it to dance between the two positions.
- **The agent is backtracking sometimes**
  : If an agent moves very fast it might overshoot the path_desired_distance check without ever advancing the path index. This can lead to the agent backtracking to the path point now behind it until it passes the distance check to increase the path index. Increase the desired distances accordingly for your agent speed and update rate usually fixes this as well as a more balanced navigation mesh polygon layout with not too many polygon edges cramped together in small spaces.
- **The agent is sometimes looking backwards for a frame**
  : Same as with stuck dancing agents between two positions, this is usually caused by very frequent path updates every single frame. Depending on your navigation mesh layout, and especially when an agent is directly placed over a navigation mesh edge or edge connection, expect path positions to be sometimes slightly "behind" your actors current orientation. This happens due to precision issues and can not always be avoided. This is usually only a visible problem if actors are instantly rotated to face the current path position.

### NavigationAgent Avoidance

This section explains how to use the navigation avoidance specific to NavigationAgents.

In order for NavigationAgents to use the avoidance feature the `avoidance_enabled` property must be set to `true`.

The `velocity_computed` signal of the NavigationAgent node must be connected to receive the safe velocity calculation result.

Set the `velocity` of the NavigationAgent node in `_physics_process()` to update the agent with the current velocity of the agent's parent node.

While avoidance is enabled on the agent the `safe_velocity` vector will be received with the velocity_computed signal every physics frame. This velocity vector should be used to move the NavigationAgent's parent node in order to avoidance collision with other avoidance using agents or avoidance obstacles.

> **Note:** Only other agents on the same map that are registered for avoidance themself will be considered in the avoidance calculation.

The following NavigationAgent properties are relevant for avoidance:

- The property `height` is available in 3D only. The height together with the current global y-axis position of the agent determines the vertical placement of the agent in the avoidance simulation. Agents using the 2D avoidance will automatically ignore other agents or obstacles that are below or above them.
- The property `radius` controls the size of the avoidance circle, or in case of 3D sphere, around the agent. This area describes the agents body and not the avoidance maneuver distance.
- The property `neighbor_distance` controls the search radius of the agent when searching for other agents that should be avoided. A lower value reduces processing cost.
- The property `max_neighbors` controls how many other agents are considered in the avoidance calculation if they all have overlapping radius. A lower value reduces processing cost but a too low value may result in agents ignoring the avoidance.
- The properties `time_horizon_agents` and `time_horizon_obstacles` control the avoidance prediction time for other agents or obstacles in seconds. When agents calculate their safe velocities they choose velocities that can be kept for this amount of seconds without colliding with another avoidance object. The prediction time should be kept as low as possible as agents will slow down their velocities to avoid collision in that timeframe.
- The property `max_speed` controls the maximum velocity allowed for the agents avoidance calculation. If the agents parents moves faster than this value the avoidance `safe_velocity` might not be accurate enough to avoid collision.
- The property `use_3d_avoidance` switches the agent between the 2D avoidance (xz axis) and the 3D avoidance (xyz axis) on the next update. Note that 2D avoidance and 3D avoidance run in separate avoidance simulations so agents split between them do not affect each other.
- The properties `avoidance_layers` and `avoidance_mask` are bitmasks similar to e.g. physics layers. Agents will only avoid other avoidance objects that are on an avoidance layer that matches at least one of their own avoidance mask bits.
- The `avoidance_priority` makes agents with a higher priority ignore agents with a lower priority. This can be used to give certain agents more importance in the avoidance simulation, e.g. important non-playable characters, without constantly changing their entire avoidance layers or mask.

Avoidance exists in its own space and has no information from navigation meshes or physics collision. Behind the scene avoidance agents are just circles with different radius on a flat 2D plane or spheres in an otherwise empty 3D space. NavigationObstacles can be used to add some environment constrains to the avoidance simulation, see Using NavigationObstacles.

> **Note:** Avoidance does not affect the pathfinding. It should be seen as an additional option for constantly moving objects that cannot be (re)baked to a navigation mesh efficiently in order to move around them.

> **Note:** RVO avoidance makes implicit assumptions about natural agent behavior. E.g. that agents move on reasonable passing sides that can be assigned when they encounter each other. This means that very clinical avoidance test scenarios will commonly fail. E.g. agents moved directly against each other with perfect opposite velocities will fail because the agents can not get their passing sides assigned.

Using the NavigationAgent `avoidance_enabled` property is the preferred option to toggle avoidance. The following code snippets can be used to toggle avoidance on agents, create or delete avoidance callbacks or switch avoidance modes.

```gdscript
extends NavigationAgent2D

func _ready() -> void:
    var agent: RID = get_rid()
    # Enable avoidance
    NavigationServer2D.agent_set_avoidance_enabled(agent, true)
    # Create avoidance callback
    NavigationServer2D.agent_set_avoidance_callback(agent, Callable(self, "_avoidance_done"))

    # Disable avoidance
    NavigationServer2D.agent_set_avoidance_enabled(agent, false)
    # Delete avoidance callback
    NavigationServer2D.agent_set_avoidance_callback(agent, Callable())
```

```gdscript
extends NavigationAgent3D

func _ready() -> void:
    var agent: RID = get_rid()
    # Enable avoidance
    NavigationServer3D.agent_set_avoidance_enabled(agent, true)
    # Create avoidance callback
    NavigationServer3D.agent_set_avoidance_callback(agent, Callable(self, "_avoidance_done"))
    # Switch to 3D avoidance
    NavigationServer3D.agent_set_use_3d_avoidance(agent, true)

    # Disable avoidance
    NavigationServer3D.agent_set_avoidance_enabled(agent, false)
    # Delete avoidance callback
    NavigationServer3D.agent_set_avoidance_callback(agent, Callable())
    # Switch to 2D avoidance
    NavigationServer3D.agent_set_use_3d_avoidance(agent, false)
```

### NavigationAgent Script Templates

The following sections provides script templates for nodes commonly used with NavigationAgents.

```gdscript
extends Node2D

@export var movement_speed: float = 4.0
@onready var navigation_agent: NavigationAgent2D = get_node("NavigationAgent2D")
var movement_delta: float

func _ready() -> void:
    navigation_agent.velocity_computed.connect(Callable(_on_velocity_computed))

func set_movement_target(movement_target: Vector2):
    navigation_agent.set_target_position(movement_target)

func _physics_process(delta):
    # Do not query when the map has never synchronized and is empty.
    if NavigationServer2D.map_get_iteration_id(navigation_agent.get_navigation_map()) == 0:
        return
    if navigation_agent.is_navigation_finished():
        return

    movement_delta = movement_speed * delta
    var next_path_position: Vector2 = navigation_agent.get_next_path_position()
    var new_velocity: Vec
# ...
```

```gdscript
extends CharacterBody2D

@export var movement_speed: float = 4.0
@onready var navigation_agent: NavigationAgent2D = get_node("NavigationAgent2D")

func _ready() -> void:
    navigation_agent.velocity_computed.connect(Callable(_on_velocity_computed))

func set_movement_target(movement_target: Vector2):
    navigation_agent.set_target_position(movement_target)

func _physics_process(delta):
    # Do not query when the map has never synchronized and is empty.
    if NavigationServer2D.map_get_iteration_id(navigation_agent.get_navigation_map()) == 0:
        return
    if navigation_agent.is_navigation_finished():
        return

    var next_path_position: Vector2 = navigation_agent.get_next_path_position()
    var new_velocity: Vector2 = global_position.direction_to(next_path_position) * mov
# ...
```

```gdscript
extends RigidBody2D

@export var movement_speed: float = 4.0
@onready var navigation_agent: NavigationAgent2D = get_node("NavigationAgent2D")

func _ready() -> void:
    navigation_agent.velocity_computed.connect(Callable(_on_velocity_computed))

func set_movement_target(movement_target: Vector2):
    navigation_agent.set_target_position(movement_target)

func _physics_process(delta):
    # Do not query when the map has never synchronized and is empty.
    if NavigationServer2D.map_get_iteration_id(navigation_agent.get_navigation_map()) == 0:
        return
    if navigation_agent.is_navigation_finished():
        return

    var next_path_position: Vector2 = navigation_agent.get_next_path_position()
    var new_velocity: Vector2 = global_position.direction_to(next_path_position) * movemen
# ...
```

```gdscript
extends Node3D

@export var movement_speed: float = 4.0
@onready var navigation_agent: NavigationAgent3D = get_node("NavigationAgent3D")
var physics_delta: float

func _ready() -> void:
    navigation_agent.velocity_computed.connect(Callable(_on_velocity_computed))

func set_movement_target(movement_target: Vector3):
    navigation_agent.set_target_position(movement_target)

func _physics_process(delta):
    # Save the delta for use in _on_velocity_computed.
    physics_delta = delta
    # Do not query when the map has never synchronized and is empty.
    if NavigationServer3D.map_get_iteration_id(navigation_agent.get_navigation_map()) == 0:
        return
    if navigation_agent.is_navigation_finished():
        return

    var next_path_position: Vector3 = navigation_agent.get_next_path_
# ...
```

```gdscript
extends CharacterBody3D

@export var movement_speed: float = 4.0
@onready var navigation_agent: NavigationAgent3D = get_node("NavigationAgent3D")

func _ready() -> void:
    navigation_agent.velocity_computed.connect(Callable(_on_velocity_computed))

func set_movement_target(movement_target: Vector3):
    navigation_agent.set_target_position(movement_target)

func _physics_process(delta):
    # Do not query when the map has never synchronized and is empty.
    if NavigationServer3D.map_get_iteration_id(navigation_agent.get_navigation_map()) == 0:
        return
    if navigation_agent.is_navigation_finished():
        return

    var next_path_position: Vector3 = navigation_agent.get_next_path_position()
    var new_velocity: Vector3 = global_position.direction_to(next_path_position) * mov
# ...
```

```gdscript
extends RigidBody3D

@export var movement_speed: float = 4.0
@onready var navigation_agent: NavigationAgent3D = get_node("NavigationAgent3D")

func _ready() -> void:
    navigation_agent.velocity_computed.connect(Callable(_on_velocity_computed))

func set_movement_target(movement_target: Vector3):
    navigation_agent.set_target_position(movement_target)

func _physics_process(delta):
    # Do not query when the map has never synchronized and is empty.
    if NavigationServer3D.map_get_iteration_id(navigation_agent.get_navigation_map()) == 0:
        return
    if navigation_agent.is_navigation_finished():
        return

    var next_path_position: Vector3 = navigation_agent.get_next_path_position()
    var new_velocity: Vector3 = global_position.direction_to(next_path_position) * movemen
# ...
```

---

## Using NavigationLayers

NavigationLayers are an optional feature to further control which navigation meshes are considered in a path query. They work similar to how physics layers control collision between collision objects or how visual layers control what is rendered to the Viewport.

NavigationLayers can be named in the **ProjectSettings** the same as physics layers or visual layers.

If a region has not a single compatible navigation layer with the `navigation_layers` parameter of a path query this regions navigation mesh will be skipped in pathfinding. See Using NavigationPaths for more information on querying the NavigationServer for paths.

NavigationLayers are a single `int` value that is used as a **bitmask**. Many navigation related nodes have `set_navigation_layer_value()` and `get_navigation_layer_value()` functions to set and get a layer number directly without the need for more complex bitwise operations.

In scripts the following helper functions can be used to work with the `navigation_layers` bitmask.

```gdscript
func change_layers():
    var region: NavigationRegion2D = get_node("NavigationRegion2D")
    # enables 4-th layer for this region
    region.navigation_layers = enable_bitmask_inx(region.navigation_layers, 4)
    # disables 1-rst layer for this region
    region.navigation_layers = disable_bitmask_inx(region.navigation_layers, 1)

    var agent: NavigationAgent2D = get_node("NavigationAgent2D")
    # make future path queries of this agent ignore regions with 4-th layer
    agent.navigation_layers = disable_bitmask_inx(agent.navigation_layers, 4)

    var path_query_navigation_layers: int = 0
    path_query_navigation_layers = enable_bitmask_inx(path_query_navigation_layers, 2)
    # get a path that only considers 2-nd layer regions
    var path: PackedVector2Array = NavigationServer2D.map
# ...
```

```gdscript
func change_layers():
    var region: NavigationRegion3D = get_node("NavigationRegion3D")
    # enables 4-th layer for this region
    region.navigation_layers = enable_bitmask_inx(region.navigation_layers, 4)
    # disables 1-rst layer for this region
    region.navigation_layers = disable_bitmask_inx(region.navigation_layers, 1)

    var agent: NavigationAgent3D = get_node("NavigationAgent3D")
    # make future path queries of this agent ignore regions with 4-th layer
    agent.navigation_layers = disable_bitmask_inx(agent.navigation_layers, 4)

    var path_query_navigation_layers: int = 0
    path_query_navigation_layers = enable_bitmask_inx(path_query_navigation_layers, 2)
    # get a path that only considers 2-nd layer regions
    var path: PackedVector3Array = NavigationServer3D.map
# ...
```

Changing navigation layers for path queries is a performance friendly alternative to enabling / disabling entire navigation regions. Compared to region changes a navigation path query with different navigation layers does not trigger large scale updates on the NavigationServer.

Changing the navigation layers of NavigationAgent nodes will have an immediate effect on the next path query. Changing the navigation layers of regions will have an effect after the next NavigationServer sync.

---
