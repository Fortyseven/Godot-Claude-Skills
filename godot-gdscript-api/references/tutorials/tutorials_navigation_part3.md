# Godot 4 GDScript Tutorials — Navigation (Part 3)

> 1 tutorials. GDScript-specific code examples.

## Using NavigationServer

2D and 3D version of the NavigationServer are available as [NavigationServer2D](../godot_gdscript_misc.md) and [NavigationServer3D](../godot_gdscript_misc.md) respectively.

### Communicating with the NavigationServer

To work with the NavigationServer means to prepare parameters for a **query** that can be sent to the NavigationServer for updates or requesting data.

To reference the internal NavigationServer objects like maps, regions and agents RIDs are used as identification numbers. Every navigation related node in the scene tree has a function that returns the RID for this node.

### Threading and Synchronization

The NavigationServer does not update every change immediately but waits until the end of the **physics frame** to synchronize all the changes together.

Waiting for synchronization is required to apply changes to all maps, regions and agents. Synchronization is done because some updates like a recalculation of the entire navigation map are very expensive and require updated data from all other objects. Also the NavigationServer uses a **threadpool** by default for some functionality like avoidance calculation between agents.

Waiting is not required for most `get()` functions that only request data from the NavigationServer without making changes. Note that not all data will account for changes made in the same frame. E.g. if an avoidance agent changed the navigation map this frame the `agent_get_map()` function will still return the old map before the synchronization. The exception to this are nodes that store their values internally before sending the update to the NavigationServer. When a getter on a node is used for a value that was updated in the same frame it will return the already updated value stored on the node.

The NavigationServer is **thread-safe** as it places all API calls that want to make changes in a queue to be executed in the synchronization phase. Synchronization for the NavigationServer happens in the middle of the physics frame after scene input from scripts and nodes are all done.

> **Note:** The important takeaway is that most NavigationServer changes take effect after the next physics frame and not immediately. This includes all changes made by navigation related nodes in the scene tree or through scripts.

> **Note:** All setters and delete functions require synchronization.

### 2D and 3D NavigationServer differences

NavigationServer2D and NavigationServer3D are equivalent in functionality for their dimension.

Technically it is possible to use the tools for creating navigation meshes in one dimension for the other dimension, e.g. baking a 2D navigation mesh with the 3D NavigationMesh when using flat 3D source geometry or creating 3D flat navigation meshes with the polygon outline draw tools of NavigationRegion2D and NavigationPolygons.

### Waiting for synchronization

At the start of the game, a new scene or procedural navigation changes any path query to a NavigationServer will return empty or wrong.

The navigation map is still empty or not updated at this point. All nodes from the scene tree need to first upload their navigation related data to the NavigationServer. Each added or changed map, region or agent need to be registered with the NavigationServer. Afterward the NavigationServer requires a **physics frame** for synchronization to update the maps, regions and agents.

One workaround is to make a deferred call to a custom setup function (so all nodes are ready). The setup function makes all the navigation changes, e.g. adding procedural stuff. Afterwards the function waits for the next physics frame before continuing with path queries.

```gdscript
extends Node3D

func _ready():
    # Use call deferred to make sure the entire scene tree nodes are setup
    # else await on 'physics_frame' in a _ready() might get stuck.
    custom_setup.call_deferred()

func custom_setup():

    # Create a new navigation map.
    var map: RID = NavigationServer3D.map_create()
    NavigationServer3D.map_set_up(map, Vector3.UP)
    NavigationServer3D.map_set_active(map, true)

    # Create a new navigation region and add it to the map.
    var region: RID = NavigationServer3D.region_create()
    NavigationServer3D.region_set_transform(region, Transform3D())
    NavigationServer3D.region_set_map(region, map)

    # Create a procedural navigation mesh for the region.
    var new_navigation_mesh: NavigationMesh = NavigationMesh.new()
    var vertices: Packe
# ...
```

### Server Avoidance Callbacks

If RVO avoidance agents are registered for avoidance callbacks the NavigationServer dispatches their `velocity_computed` signals just before the PhysicsServer synchronization.

To learn more about NavigationAgents see Using NavigationAgents.

The simplified order of execution for NavigationAgents that use avoidance:

- physics frame starts.
- `_physics_process(delta)`.
- `velocity` property is set on NavigationAgent Node.
- Agent sends velocity and position to NavigationServer.
- NavigationServer waits for synchronization.
- NavigationServer synchronizes and computes avoidance velocities for all registered avoidance agents.
- NavigationServer sends safe velocity vector with signals for each registered avoidance agents.
- Agents receive the signal and move their parent e.g. with `move_and_slide` or `linear_velocity`.
- PhysicsServer synchronizes.
- physics frame ends.

Therefore moving a physicsbody actor in the callback function with the safe velocity is perfectly thread- and physics-safe as all happens inside the same physics frame before the PhysicsServer commits to changes and does its own calculations.

---
