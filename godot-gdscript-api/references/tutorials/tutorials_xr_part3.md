# Godot 4 GDScript Tutorials — Xr (Part 3)

> 2 tutorials. GDScript-specific code examples.

## OpenXR spatial entities

For any sort of augmented reality application you need to access real world information, and be able to track real world locations. OpenXR's spatial entities API was introduced for this exact purpose.

It has a very modular design. The core of the API defines how real world entities are structured, how they are found, and how information about them is stored and accessed.

Various extensions are added on top, which implement specific systems such as marker tracking, plane tracking, and anchors. These are referred to as spatial capabilities.

Each entity that can be handled by the system is broken up into smaller components, which makes it easy to extend the system and add new capabilities.

Vendors have the ability to implement and expose additional capabilities and component types that can be used with the core API. For Godot these can be implemented in extensions. These implementations however fall outside of the scope of this manual.

Finally it is important to note that the spatial entity system makes use of asynchronous functions. This means that you can start a process, and then get informed of it finishing later on.

### Setup

In order to use spatial entities you need to enable the related project settings. You can find these in the OpenXR section:

| Setting                          | Description                                                                                                                                                      |
| -------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Enabled                          | Enables the core of the spatial entities system. This must be enabled for any of the spatial entities systems to work.                                           |
| Enable spatial anchors           | Enables the spatial anchors capability that allow creating and tracking spatial anchors.                                                                         |
| Enable persistent anchors        | Enables the ability to make spatial anchors persistent. This means that their location is stored and can be retrieved in subsequent sessions.                    |
| Enable built-in anchor detection | Enables our built-in anchor detection logic, this will automatically retrieve persistent anchors and adjust the positioning of anchors when tracking is updated. |
| Enable plane tracking            | Enables the plane tracking capability that allows detection of surfaces such as floors, walls, ceilings, and tables.                                             |
| Enable built-in plane detection  | Enables our built-in plane detection logic, this will automatically react to new plane data becoming available.                                                  |
| Enable marker tracking           | Enables our marker tracking capability that allows detection of markers such as QR codes, Aruco markers, and April tags.                                         |
| Enable built-in marker tracking  | Enables our built-in marker detection logic, this will automatically react to new markers being found or markers being moved around the player's space.          |

> **Note:** Note that various XR devices also require permission flags to be set. These will need to be enabled in the export preset settings.

Enabling the different capabilities activates the related OpenXR APIs, but additional logic is needed to interact with this data. For each core system we have built-in logic that can be enabled that will do this for you.

We'll discuss the spatial entities system under the assumption that the built-in logic is enabled first. We will then take a look at the underlying APIs and how you can implement this yourself, however it should be noted that this is often overkill and that the underlying APIs are mostly exposed to allow GDExtension plugins to implement additional capabilities.

### Creating our spatial manager

When spatial entities are detected or created an [OpenXRSpatialEntityTracker](../godot_gdscript_misc.md) object is instantiated and registered with the [XRServer](../godot_gdscript_misc.md).

Each type of spatial entity will implement its own subclass and we can thus react differently to each type of entity.

Generally speaking we will instance different subscenes for each type of entity. As the tracker objects can be used with [XRAnchor3D](../godot_gdscript_misc.md) nodes, these subscenes should have such a node as their root node.

All entity trackers will expose their location through the `default` pose.

We can automate creating these subscenes and adding them to our scene tree by creating a manager object. As all locations are local to the [XROrigin3D](../godot_gdscript_misc.md) node, we should create our manager as a child node of our origin node.

Below is the basis of the script that implements our manager logic:

```gdscript
class_name SpatialEntitiesManager
extends Node3D

## Signals a new spatial entity node was added.
signal added_spatial_entity(node: XRNode3D)

## Signals a spatial entity node is about to be removed.
signal removed_spatial_entity(node: XRNode3D)

## Scene to instantiate for spatial anchor entities.
@export var spatial_anchor_scene: PackedScene

## Scene to instantiate for plane tracking spatial entities.
@export var plane_tracker_scene: PackedScene

## Scene to instantiate for marker tracking spatial entities.
@export var marker_tracker_scene: PackedScene

# Trackers we manage nodes for.
var _managed_nodes: Dictionary[OpenXRSpatialEntityTracker, XRAnchor3D]

# Enter tree is called whenever our node is added to our scene.
func _enter_tree():
    # Connect to signals that inform us about tra
# ...
```

### Spatial anchors

Spatial anchors allow us to map real world locations in our virtual world in such a way that the XR runtime will keep track of these locations and adjust them as needed. If supported, anchors can be made persistent which means the anchors will be recreated in the correct location when your application starts again.

You can think of use cases such as: - placing virtual windows around your space that are recreated when your application restarts - placing virtual objects on your table or on your walls and have them recreated

Spatial anchors are tracked using [OpenXRAnchorTracker](../godot_gdscript_misc.md) objects registered with the XRServer.

When needed, the location of the spatial anchor will be updated automatically; the pose on the related tracker will be updated and thus the [XRAnchor3D](../godot_gdscript_misc.md) node will reposition.

When a spatial anchor has been made persistent, a Universally Unique Identifier (or UUID) is assigned to the anchor. You will need to store this with whatever information you need to reconstruct the scene. In our example code below we'll simply call `set_scene_path` and `get_scene_path`, but you will need to supply your own implementations for these functions.

In order to create a persistent anchor you need to follow a specific flow: - Create the spatial anchor - Wait until the tracking status changes to `ENTITY_TRACKING_STATE_TRACKING` - Make the anchor persistent - Obtain the UUID and save it

When an existing persistent anchor is found a new tracker is added that has the UUID already set. It is this difference in workflow that allows us to correctly react to new and existing persistent anchors.

> **Note:** If you unpersist an anchor, the UUID is destroyed but the anchor is not removed automatically. You will need to react to the completion of unpersisting an anchor and then clean it up. Also you will get an error if you try to destroy an anchor that is still persistent.

To complete our anchor system we start by creating a scene that we'll set as the scene to instantiate for anchors on our spatial manager node.

This scene should have an [XRAnchor3D](../godot_gdscript_misc.md) node as the root but nothing else. We will add a script to it that will load a subscene that contains the actual visual aspect of our anchor so we can create different anchors in our scene. We'll assume the intention is to make these anchors persistent and save the path to this subscene as metadata for our UUID.

```gdscript
class_name OpenXRSpatialAnchor3D
extends XRAnchor3D

var anchor_tracker: OpenXRAnchorTracker
var child_scene: Node
var made_persistent: bool = false

## Return the scene path for our UUID.
func get_scene_path(p_uuid: String) -> String:
    # Placeholder, implement this.
    return ""

## Store our scene path for our UUID.
func set_scene_path(p_uuid: String, p_scene_path: String):
    # Placeholder, implement this.
    pass

## Remove info related to our UUID.
func remove_uuid(p_uuid: String):
    # Placeholder, implement this.
    pass

## Set our child scene for this anchor, call this when creating a new anchor.
func set_child_scene(p_child_scene_path: String):
    var packed_scene: PackedScene = load(p_child_scene_path)
    if not packed_scene:
        return

    child_scene = packed
# ...
```

With our anchor scene in place we can add a couple of functions to our spatial manager script to create or remove anchors:

```gdscript
...

## Create a new spatial anchor with the associated child scene.
## If persistent anchors are supported, this will be created as a persistent node
## and we will store the child scene path with the anchor's UUID for future recreation.
func create_spatial_anchor(p_transform: Transform3D, p_child_scene_path: String):
    # Do we have anchor support?
    if not OpenXRSpatialAnchorCapability.is_spatial_anchor_supported():
        push_error("Spatial anchors are not supported on this device!")
        return

    # Adjust our transform to local space.
    var t: Transform3D = global_transform.inverse() * p_transform

    # Create anchor on our current manager.
    var new_anchor = OpenXRSpatialAnchorCapability.create_new_anchor(t, RID())
    if not new_anchor:
        push_error("Couldn't c
# ...
```

> **Note:** There seems to be a bit of magic going on in the code above. Whenever a spatial anchor is created or removed on our anchor capability, the related tracker object is created or destroyed. This results in the spatial manager adding or removing the child scene for this anchor. Hence we can rely on this here.

### Plane tracking

Plane tracking allows us to detect surfaces such as walls, floors, ceilings, and tables in the player's vicinity. This data could come from a room capture performed by the user at any time in the past, or detected live by optical sensors. The plane tracking extension doesn't make a distinction here.

> **Note:** Some XR runtimes do require vendor extensions to enable and/or configure this process but the data will be exposed through this extension.

The code we wrote up above for the spatial manager will already detect our new planes. We do need to set up a new scene and assign that scene to the spatial manager.

The root node for this scene must be an [XRAnchor3D](../godot_gdscript_misc.md) node. We'll add a [StaticBody3D](../godot_gdscript_nodes_3d.md) node as a child and add a [CollisionShape3D](../godot_gdscript_physics.md) and [MeshInstance3D](../godot_gdscript_nodes_3d.md) node as children of the static body.

The static body and collision shape will allow us to make the plane interactable.

The mesh instance node allows us to apply a "hole punch" material to the plane, when combined with passthrough this turns our plane into a visual occluder. Alternatively we can assign a material that will visualize the plane for debugging.

We configure this material as the `material_override` material on our MeshInstance3D. For our "hole punch" material, create a [ShaderMaterial](../godot_gdscript_rendering.md) and use the following code as the shader code:

```glsl
shader_type spatial;
render_mode unshaded, shadow_to_opacity;

void fragment() {
    ALBEDO = vec3(0.0, 0.0, 0.0);
}
```

We also need to add a script to our scene to ensure our collision and mesh are applied.

```gdscript
extends XRAnchor3D

var plane_tracker: OpenXRPlaneTracker

func _update_mesh_and_collision():
    if plane_tracker:
        # Place our static body using our offset so both collision
        # and mesh are positioned correctly.
        $StaticBody3D.transform = plane_tracker.get_mesh_offset()

        # Set our mesh so we can occlude the surface.
        $StaticBody3D/MeshInstance3D.mesh = plane_tracker.get_mesh()

        # And set our shape so we can have things collide things with our surface.
        $StaticBody3D/CollisionShape3D.shape = plane_tracker.get_shape()

func _ready():
    plane_tracker = XRServer.get_tracker(tracker)
    if plane_tracker:
        _update_mesh_and_collision()

        plane_tracker.mesh_changed.connect(_update_mesh_and_collision)
```

If supported by the XR runtime there is additional metadata you can query on the plane tracker object. Of specific note is the `plane_label` property that, if available, identifies the type of surface. Please consult the [OpenXRPlaneTracker](../godot_gdscript_misc.md) class documentation for further information.

### Marker tracking

Marker tracking detects specific markers in the real world. These are usually printed images such as QR codes.

The API exposes support for 4 different codes, QR codes, Micro QR codes, Aruco codes, and April tags, however XR runtimes are not required to support them all.

When markers are detected, [OpenXRMarkerTracker](../godot_gdscript_misc.md) objects are instantiated and registered with the XRServer.

Our existing spatial manager code already detects these, all we need to do is create a scene with an [XRAnchor3D](../godot_gdscript_misc.md) node at the root, save this, and assign it to the spatial manager as the scene to instantiate for markers.

The marker tracker should be fully configured when assigned, so all that is needed is a `_ready` function that reacts to the marker data. Below is a template for the required code:

```gdscript
extends XRAnchor3D

var marker_tracker: OpenXRMarkerTracker

func _ready():
    marker_tracker = XRServer.get_tracker(tracker)
    if marker_tracker:
        match marker_tracker.marker_type:
            OpenXRSpatialComponentMarkerList.MARKER_TYPE_QRCODE:
                var data = marker_tracker.get_marker_data()
                if data.type_of() == TYPE_STRING:
                    # Data is a QR code as a string, usually a URL.
                    pass
                elif data.type_of() == TYPE_PACKED_BYTE_ARRAY:
                    # Data is binary, can be anything.
                    pass
            OpenXRSpatialComponentMarkerList.MARKER_TYPE_MICRO_QRCODE:
                var data = marker_tracker.get_marker_data()
                if data.type_of() == TYPE_STRING:

# ...
```

As we can see, QR Codes provide a data block that is either a string or a byte array. Aruco and April tags provide an ID that is read from the code.

It's up to your use case how best to link the marker data to the scene that needs to be loaded. An example would be to encode the name of the asset you wish to display in a QR code.

### Backend access

For most purposes the core system, along with any vendor extensions, should be what most users would use as provided.

For those who are implementing vendor extensions, or those for whom the built-in logic doesn't suffice, backend access is provided through a set of singleton objects.

These objects can also be used to query what capabilities are supported by the headset in use. We've already added code that checks for these in our spatial manager and spatial anchor code in the sections above.

> **Note:** The spatial entities system will encapsulate many OpenXR entities in resources that are returned as RIDs.

#### Spatial entity core

The core spatial entity functionality is exposed through the [OpenXRSpatialEntityExtension](../godot_gdscript_misc.md) singleton.

Specific logic is exposed through capabilities that introduce specialised component types, and give access to specific types of entities, however they all use the same mechanisms for accessing the entity data managed by the spatial entity system.

We'll start by having a look at the individual components that make up the core system.

##### Spatial contexts

A spatial context is the main object through which we query the spatial entities system. Spatial contexts allow us to configure how we interact with one or more capabilities.

It's recommended to create a spatial context for each capability that you wish to interact with, in fact, this is what Godot does for its built-in logic.

We start by setting the capability configuration objects for the capabilities we wish to access. Each capability will enable the components we support for that capability. Settings can determine which components will be enabled. We'll look at these configuration objects in more detail as we look at each supported capability.

Creating a spatial context is an asynchronous action. This means we ask the XR runtime to create a spatial context, and at a point in the future the XR runtime will provide us with the result.

The following script is the start of our example and can be added as a node to your scene. It shows the creation of a spatial context for plane tracking, and sets up our entity discovery.

```gdscript
extends Node

var spatial_context: RID

func _set_up_spatial_context():
    # Already set up?
    if spatial_context:
        return

    # Not supported or we're not yet ready?
    if not OpenXRSpatialPlaneTrackingCapability.is_supported():
        return

    # We'll use plane tracking as an example here, our configuration object
    # here does not have any additional configuration. It just needs to exist.
    var plane_capability : OpenXRSpatialCapabilityConfigurationPlaneTracking = OpenXRSpatialCapabilityConfigurationPlaneTracking.new()

    var future_result : OpenXRFutureResult = OpenXRSpatialEntityExtension.create_spatial_context([ plane_capability ])

    # Wait for async completion.
    await future_result.completed

    # Obtain our result.
    spatial_context = future_result.ge
# ...
```

##### Discovery snapshots

Once our spatial context has been created the XR runtime will start managing spatial entities according to the configuration of the specified capabilities.

In order to find new entities, or to get information about our current entities, we can create a discovery snapshot. This will tell the XR runtime to gather specific data related to all the spatial entities currently managed by the spatial context.

This function is asynchronous as it may take some time to gather this data and offer its results. Generally speaking you will want to perform a discovery snapshot when new entities are found. OpenXR emits an event when there are new entities to be processed, this results in the `spatial_discovery_recommended` signal being emitted by our [OpenXRSpatialEntityExtension](../godot_gdscript_misc.md) singleton.

Note in the example code shown above, we're already connecting to this signal and calling the `_on_perform_discovery` method on our node. Let's implement this:

```gdscript
...

var discovery_result : OpenXRFutureResult

func _on_perform_discovery(p_spatial_context):
    # We get this signal for all spatial contexts, so exit if this is not for us.
    if p_spatial_context != spatial_context:
        return

    # If we currently have an ongoing discovery result, cancel it.
    if discovery_result:
        discovery_result.cancel_discovery()

    # Perform our discovery.
    discovery_result = OpenXRSpatialEntityExtension.discover_spatial_entities(spatial_context, [ \
            OpenXRSpatialEntityExtension.COMPONENT_TYPE_BOUNDED_2D, \
            OpenXRSpatialEntityExtension.COMPONENT_TYPE_PLANE_ALIGNMENT \
        ])

    # Wait for async completion.
    await discovery_result.completed

    var snapshot : RID = discovery_result.get_spatial_snapshot()
    i
# ...
```

Note that when calling `discover_spatial_entities` we specify a list of components. The discovery query will find any entity that is managed by the spatial context and has at least one of the specified components.

##### Update snapshots

Performing an update snapshot allows us to get updated information about entities we already found previously with our discovery snapshot. This function is synchronous, and is mainly meant to obtain status and positioning data and can be run every frame.

Generally speaking you would only perform update snapshots when it's likely entities change or have a lifetime process. A good example of this are persistent anchors and markers. Consult the documentation about a capability to determine if this is needed.

It is not needed for plane tracking however to complete our example, here is an example of what an update snapshot would look like for plane tracking if we needed one:

```gdscript
...

func _process(_delta):
    if not spatial_context:
        return

    if entities.is_empty():
        return

    var entity_rids: Array[RID]
    for entity_id in entities:
        entity_rids.push_back(entities[entity_id].entity)

    var snapshot : RID = OpenXRSpatialEntityExtension.update_spatial_entities(spatial_context, entity_rids, [ \
            OpenXRSpatialEntityExtension.COMPONENT_TYPE_BOUNDED_2D, \
            OpenXRSpatialEntityExtension.COMPONENT_TYPE_PLANE_ALIGNMENT \
        ])
    if snapshot:
        # Process our snapshot.
        _process_snapshot(snapshot)

        # And clean up our snapshot.
        OpenXRSpatialEntityExtension.free_spatial_snapshot(snapshot)
```

Note that in our example here we're using the same `_process_snapshot` function to process the snapshot. This makes sense in most situations. However if the components you've specified when creating the snapshot are different between your discovery snapshot and your update snapshot, you have to take the different components into account.

##### Querying snapshots

Once we have a snapshot we can run queries over that snapshot to obtain the data held within. The snapshot is guaranteed to remain unchanged until you free it.

For each component we've added to our snapshot we have an accompanying data object. This data object has a double function, adding it to your query ensures we query that component type, and it is the object into which the queried data is loaded.

There is one special data object that must always be added to our request list as the very first entry and that is [OpenXRSpatialQueryResultData](../godot_gdscript_misc.md). This object will hold an entry for every returned entity with its unique ID and the current state of the entity.

Completing our discovery logic we add the following:

```gdscript
...

var entities : Dictionary[int, OpenXRSpatialEntityTracker]

func _process_snapshot(p_snapshot):
    # Always include our query result data.
    var query_result_data : OpenXRSpatialQueryResultData = OpenXRSpatialQueryResultData.new()

    # Add our bounded 2D component data.
    var bounded2d_list : OpenXRSpatialComponentBounded2DList = OpenXRSpatialComponentBounded2DList.new()

    # And our plane alignment component data.
    var alignment_list : OpenXRSpatialComponentPlaneAlignmentList = OpenXRSpatialComponentPlaneAlignmentList.new()

    if OpenXRSpatialEntityExtension.query_snapshot(p_snapshot, [ query_result_data, bounded2d_list, alignment_list]):
        for i in query_result_data.get_entity_id_size():
            var entity_id = query_result_data.get_entity_id(i)
            v
# ...
```

> **Note:** In the above example we're relying on `ENTITY_TRACKING_STATE_STOPPED` to clean up spatial entities that are no longer being tracked. This is only available with update snapshots. For capabilities that only rely on discovery snapshots you may wish to do a cleanup based on entities that are no longer part of the snapshot instead of relying on the state change.

##### Spatial entities

With the above information we now know how to query our spatial entities and get information about them, but there is a little more we need to look at when it comes to the entities themselves.

In theory we're getting all our data from our snapshots, however OpenXR has an extra API where we create a spatial entity object from our entity ID. While this object exists the XR runtime knows that we are using this entity and that the entity is not cleaned up early. This is a prerequisite for performing an update query on this entity.

In our example code we do so by calling `OpenXRSpatialEntityExtension.make_spatial_entity`.

Some spatial entity APIs will automatically create the object for us. In this case we need to call `OpenXRSpatialEntityExtension.add_spatial_entity` to register the created object with our implementation.

Both functions return an RID that we can use in further functions that require our entity object.

When we're done we can call `OpenXRSpatialEntityExtension.free_spatial_entity`.

Note that we didn't do so in our example code. This is automatically handled when our [OpenXRSpatialEntityTracker](../godot_gdscript_misc.md) instance is destroyed.

#### Spatial anchor capability

Spatial anchors are managed by our [OpenXRSpatialAnchorCapability](../godot_gdscript_misc.md) singleton object. After the OpenXR session has been created you can call `OpenXRSpatialAnchorCapability.is_spatial_anchor_supported` to check if the spatial anchor feature is supported on your hardware.

The spatial anchor capability breaks the mold a little from what we've shown above.

The spatial anchor system allows us to identify, track, persist, and share a physical location. What makes this different is that we're creating and destroying the anchor and are thus managing its lifecycle.

We thus only use the discovery system to discover anchors created and persisted in previous sessions, or anchors shared with us.

> **Note:** Sharing of anchors is currently not supported in the spatial entities specification.

As we showed in our example before we always start with creating a spatial context but now using the [OpenXRSpatialCapabilityConfigurationAnchor](../godot_gdscript_misc.md) configuration object. We'll show an example of this code after we discuss persistence scopes. First we'll look at managing local anchors.

There is no difference in creating spatial anchors from what we've discussed around the built-in logic. The only important thing is to pass your own spatial context as a parameter to `OpenXRSpatialAnchorCapability.create_new_anchor`.

Making an anchor persistent requires you to wait until the anchor is tracking, this means that you must perform update queries for any anchor you create so you can process state changes.

In order to enable making anchors persistent you also have to set up a persistence scope. In the core of OpenXR two types of persistence scopes are supported:

| Enum                             | Description                                                                                                                                                                                                                                                                                         |
| -------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| PERSISTENCE_SCOPE_SYSTEM_MANAGED | Provides the application with read-only access (i.e. applications cannot modify this store) to spatial entities persisted and managed by the system. The application can use the UUID in the persistence component for this store to correlate entities across spatial contexts and device reboots. |
| PERSISTENCE_SCOPE_LOCAL_ANCHORS  | Persistence operations and data access is limited to spatial anchors, on the same device, for the same user and app (using persist_anchor and unpersist_anchor functions)                                                                                                                           |

We'll start with a new script that handles our spatial anchors. It will be similar to the script presented earlier but with a few differences.

The first being the creation of our persistence scope.

```gdscript
extends Node

var persistence_context : RID

func _set_up_persistence_context():
    # Already set up?
    if persistence_context:
        # Check our spatial context.
        _set_up_spatial_context()
        return

    # Not supported or we're not yet ready? Just exit.
    if not OpenXRSpatialAnchorCapability.is_spatial_anchor_supported():
        return

    # If we can't use a persistence scope, just create our spatial context without one.
    if not OpenXRSpatialAnchorCapability.is_spatial_persistence_supported():
        _set_up_spatial_context()
        return

    var scope : int = 0
    if OpenXRSpatialAnchorCapability.is_persistence_scope_supported(OpenXRSpatialAnchorCapability.PERSISTENCE_SCOPE_LOCAL_ANCHORS):
        scope = OpenXRSpatialAnchorCapability.PERSISTENCE_SCOPE_LOCA
# ...
```

With our persistence scope created, we can now create our spatial context.

```gdscript
...

var spatial_context: RID

func _set_up_spatial_context():
    # Already set up?
    if spatial_context:
        return

    # Not supported or we're not yet set up.
    if not OpenXRSpatialAnchorCapability.is_spatial_anchor_supported():
        return

    # Create our anchor capability.
    var anchor_capability : OpenXRSpatialCapabilityConfigurationAnchor = OpenXRSpatialCapabilityConfigurationAnchor.new()

    # And set up our persistence configuration object (if needed).
    var persistence_config : OpenXRSpatialContextPersistenceConfig
    if persistence_context:
        persistence_config = OpenXRSpatialContextPersistenceConfig.new()
        persistence_config.add_persistence_context(persistence_context)

    var future_result : OpenXRFutureResultg = OpenXRSpatialEntityExtension.
# ...
```

Creating our discovery snapshot for our anchors is nearly the same as we did before, however it only makes sense to create our snapshot for persistent anchors. We already know the anchors we created during our session, we just want access to those coming from the XR runtime.

We also want to perform regular update queries, here we are only interested in the state so we do want to process our snapshot slightly differently.

The anchor system gives us access to two components:

| Component                  | Data class                            | Description                                                       |
| -------------------------- | ------------------------------------- | ----------------------------------------------------------------- |
| COMPONENT_TYPE_ANCHOR      | OpenXRSpatialComponentAnchorList      | Provides us with the pose (location + orientation) of each anchor |
| COMPONENT_TYPE_PERSISTENCE | OpenXRSpatialComponentPersistenceList | Provides us with the persistence state and UUID of each anchor    |

```gdscript
...

var discovery_result : OpenXRFutureResult
var entities : Dictionary[int, OpenXRAnchorTracker]

func _on_perform_discovery(p_spatial_context):
    # We get this signal for all spatial contexts, so exit if this is not for us.
    if p_spatial_context != spatial_context:
        return

    # Skip this if we don't have a persistence context.
    if not persistence_context:
        return

    # If we currently have an ongoing discovery result, cancel it.
    if discovery_result:
        discovery_result.cancel_discovery()

    # Perform our discovery.
    discovery_result = OpenXRSpatialEntityExtension.discover_spatial_entities(spatial_context, [ \
            OpenXRSpatialEntityExtension.COMPONENT_TYPE_ANCHOR, \
            OpenXRSpatialEntityExtension.COMPONENT_TYPE_PERSISTENCE \

# ...
```

Finally we can process our snapshot. Note that we are using [OpenXRAnchorTracker](../godot_gdscript_misc.md) as our tracker class as this already has all the support for anchors built in.

```gdscript
...

func _process_snapshot(p_snapshot, p_get_uuids):
    var result_data : Array

    # Always include our query result data.
    var query_result_data : OpenXRSpatialQueryResultData = OpenXRSpatialQueryResultData.new()
    result_data.push_back(query_result_data)

    # Add our anchor component data.
    var anchor_list : OpenXRSpatialComponentAnchorList = OpenXRSpatialComponentAnchorList.new()
    result_data.push_back(anchor_list)

    # And our persistent component data.
    var persistent_list : OpenXRSpatialComponentPersistenceList
    if p_get_uuids:
        # Only add this when we need it.
        persistent_list = OpenXRSpatialComponentPersistenceList.new()
        result_data.push_back(persistent_list)

    if OpenXRSpatialEntityExtension.query_snapshot(p_snapshot, result_data):
# ...
```

#### Plane tracking capability

Plane tracking is handled by the [OpenXRSpatialPlaneTrackingCapability](../godot_gdscript_misc.md) singleton class.

After the OpenXR session has been created you can call `OpenXRSpatialPlaneTrackingCapability.is_supported` to check if the plane tracking feature is supported on your hardware.

While we've provided most of the code for plane tracking up above, we'll present the full implementation below as it has a few small tweaks. There is no need to update snapshots here, we just do our discovery snapshot and implement our process function.

Plane tracking gives access to two components that are guaranteed to be supported, and three optional components.

| Component                           | Data class                                   | Description                                                             |
| ----------------------------------- | -------------------------------------------- | ----------------------------------------------------------------------- |
| COMPONENT_TYPE_BOUNDED_2D           | OpenXRSpatialComponentBounded2DList          | Provides us with the center pose and bounding rectangle for each plane. |
| COMPONENT_TYPE_PLANE_ALIGNMENT      | OpenXRSpatialComponentPlaneAlignmentList     | Provides us with the alignment of each plane                            |
| COMPONENT_TYPE_MESH_2D              | OpenXRSpatialComponentMesh2DList             | Provides us with a 2D mesh that shapes each plane                       |
| COMPONENT_TYPE_POLYGON_2D           | OpenXRSpatialComponentPolygon2DList          | Provides us with a 2D polygon that shapes each plane                    |
| COMPONENT_TYPE_PLANE_SEMANTIC_LABEL | OpenXRSpatialComponentPlaneSemanticLabelList | Provides us with a type identification of each plane                    |

Our plane tracking configuration object already enables all supported components, but we'll need to interrogate it so we'll store our instance in a member variable. We can use our [OpenXRPlaneTracker](../godot_gdscript_misc.md) tracker object to store our component data.

```gdscript
extends Node

var plane_capability : OpenXRSpatialCapabilityConfigurationPlaneTracking
var spatial_context: RID
var discovery_result : OpenXRFutureResult
var entities : Dictionary[int, OpenXRPlaneTracker]

func _set_up_spatial_context():
    # Already set up?
    if spatial_context:
        return

    # Not supported or we're not yet ready?
    if not OpenXRSpatialPlaneTrackingCapability.is_supported():
        return

    # We'll use plane tracking as an example here, our configuration object
    # here does not have any additional configuration. It just needs to exist.
    plane_capability = OpenXRSpatialCapabilityConfigurationPlaneTracking.new()

    var future_result : OpenXRFutureResult = OpenXRSpatialEntityExtension.create_spatial_context([ plane_capability ])

    # Wait for async
# ...
```

#### Marker tracking capability

Marker tracking is handled by the [OpenXRSpatialMarkerTrackingCapability](../godot_gdscript_misc.md) singleton class.

Marker tracking works similarly to plane tracking, however we're now tracking specific entities in the real world based on some code printed on an object like a piece of paper.

There are various different marker tracking options. OpenXR supports 4 out of the box, the following table provides more information and the function name with which to check if your headset supports a given option:

| Option        | Check for support         | Configuration object                            |
| ------------- | ------------------------- | ----------------------------------------------- |
| April tag     | april_tag_is_supported    | OpenXRSpatialCapabilityConfigurationAprilTag    |
| Aruco         | aruco_is_supported        | OpenXRSpatialCapabilityConfigurationAruco       |
| QR code       | qrcode_is_supported       | OpenXRSpatialCapabilityConfigurationQrCode      |
| Micro QR code | micro_qrcode_is_supported | OpenXRSpatialCapabilityConfigurationMicroQrCode |

Each option has its own configuration object that you can use when creating a spatial entity.

QR codes allow you to encode a string which is decoded by the XR runtime and accessible when a marker is found. With April tags and Aruco markers, binary data is encoded which you again can access when a marker is found, however you need to configure the detection with the correct decoding format.

As an example we'll create a spatial context that will find QR codes and Aruco markers.

```gdscript
extends Node

var qrcode_config : OpenXRSpatialCapabilityConfigurationQrCode
var aruco_config : OpenXRSpatialCapabilityConfigurationAruco
var spatial_context: RID

func _set_up_spatial_context():
    # Already set up?
    if spatial_context:
        return

    var configurations : Array

    # Add our QR code configuration.
    if not OpenXRSpatialMarkerTrackingCapability.qrcode_is_supported():
        qrcode_config = OpenXRSpatialCapabilityConfigurationQrCode.new()
        configurations.push_back(qrcode_config)

    # Add our Aruco marker configuration.
    if not OpenXRSpatialMarkerTrackingCapability.aruco_is_supported():
        aruco_config = OpenXRSpatialCapabilityConfigurationAruco.new()
        aruco_config.aruco_dict = OpenXRSpatialCapabilityConfigurationAruco.ARUCO_DICT_7X7_1000
# ...
```

Every marker regardless of typer will consist of two components:

| Component                 | Data class                          | Description                                                                                 |
| ------------------------- | ----------------------------------- | ------------------------------------------------------------------------------------------- |
| COMPONENT_TYPE_MARKER     | OpenXRSpatialComponentMarkerList    | Provides us with the type, ID (Aruco and April Tag), and/or data (QR Code) for each marker. |
| COMPONENT_TYPE_BOUNDED_2D | OpenXRSpatialComponentBounded2DList | Provides us with the center pose and bounding rectangle for each plane.                     |

We add our discovery implementation:

```gdscript
...

var discovery_result : OpenXRFutureResult
var entities : Dictionary[int, OpenXRMarkerTracker]

func _on_perform_discovery(p_spatial_context):
    # We get this signal for all spatial contexts, so exit if this is not for us.
    if p_spatial_context != spatial_context:
        return

    # If we currently have an ongoing discovery result, cancel it.
    if discovery_result:
        discovery_result.cancel_discovery()

    # Perform our discovery.
    discovery_result = OpenXRSpatialEntityExtension.discover_spatial_entities(spatial_context, [\
            OpenXRSpatialEntityExtension.COMPONENT_TYPE_MARKER, \
            OpenXRSpatialEntityExtension.COMPONENT_TYPE_BOUNDED_2D \
        ])

    # Wait for async completion.
    await discovery_result.completed

    var snapshot : RID = dis
# ...
```

And we add our update functionality:

```gdscript
...

func _process(_delta):
    if not spatial_context:
        return

    if entities.is_empty():
        return

    var entity_rids: Array[RID]
    for entity_id in entities:
        entity_rids.push_back(entities[entity_id].entity)

    # We just want our anchor component here.
    var snapshot : RID = OpenXRSpatialEntityExtension.update_spatial_entities(spatial_context, entity_rids, [ \
            OpenXRSpatialEntityExtension.COMPONENT_TYPE_BOUNDED_2D, \
        ])
    if snapshot:
        # Process our snapshot.
        _process_snapshot(snapshot, false)

        # And clean up our snapshot.
        OpenXRSpatialEntityExtension.free_spatial_snapshot(snapshot)
```

---

## Setting up XR

### Introduction to the XR system in Godot

Godot provides a modular XR system that abstracts many of the different XR platform specifics away from the user. At the core sits the [XRServer](../godot_gdscript_misc.md) which acts as a central interface to the XR system that allows users to discover interfaces and interact with the components of the XR system.

Each supported XR platform is implemented as an [XRInterface](../godot_gdscript_misc.md). A list of supported platforms can be found on the list of features page here (see About docs). Supported interfaces register themselves with the [XRServer](../godot_gdscript_misc.md) and can be queried with the `find_interface` method on the [XRServer](../godot_gdscript_misc.md). When the desired interface is found it can be initialized by calling `initialize` on the interface.

> **Warning:** A registered interface means nothing more than that the interface is available, if the interface is not supported by the host system, initialization may fail and return `false`. This can have many reasons and sadly the reasons differ from platform to platform. It can be because the user hasn't installed the required software, or that the user simply hasn't plugged in their headset. You as a developer must thus react properly on an interface failing to initialize.

Due to the special requirements for output in XR, especially for head mounted devices that supply different images to each eye, the [XRServer](../godot_gdscript_misc.md) in Godot will override various features in the rendering system. For stand-alone devices this means the final output is handled by the [XRInterface](../godot_gdscript_misc.md) and Godot's usual output system is disabled. For desktop XR devices that work as a second screen it is possible to dedicate a separate [Viewport](../godot_gdscript_rendering.md) to handle the XR output, leaving the main Godot window available for displaying alternative content.

> **Note:** Note that only one interface can be responsible for handling the output to an XR device, this is known as the primary interface and by default will be the first interface that is initialized. Godot currently thus only supports implementations with a single headset. It is possible, but increasingly uncommon, to have a secondary interface, for example to add tracking to an otherwise 3DOF only device.

There are three XR specific node types that you will find in nearly all XR applications:

- [XROrigin3D](../godot_gdscript_misc.md) represents, for all intents and purposes, the center point of your play space. That is an oversimplified statement but we'll go into more detail later. All objects tracked in physical space by the XR platform are positioned in relation to this point.
- [XRCamera3D](../godot_gdscript_misc.md) represents the (stereo) camera that is used when rendering output for the XR device. The positioning of this node is controlled by the XR system and updated automatically using the tracking information provided by the XR platform.
- [XRController3D](../godot_gdscript_misc.md) represents a controller used by the player, commonly there are two, one held in each hand. These nodes give access to various states on these controllers and send out signals when the player presses buttons on them. The positioning of this node is controlled by the XR system and updated automatically using the tracking information provided by the XR platform.

There are other XR related nodes and there is much more to say about these three nodes, but we'll get into that later on.

### Which Renderer to use

Godot has 3 renderer options for projects: Compatibility, Mobile, and Forward+. The current recommendation is to use the Mobile renderer for any desktop VR project, and use the Compatibility renderer for any project running on a standalone headset like the Meta Quest 3. XR projects will run with the Forward+ renderer, but it isn't well optimized for XR right now compared to the other two.

### OpenXR

OpenXR is a new industry standard that allows different XR platforms to present themselves through a standardized API to XR applications. This standard is an open standard maintained by the Khronos Group and thus aligns very well with Godot's interests.

The Vulkan implementation of OpenXR is closely integrated with Vulkan, taking over part of the Vulkan system. This requires tight integration of certain core graphics features in the Vulkan renderer which are needed before the XR system is setup. This was one of the main deciding factors to include OpenXR as a core interface.

This also means OpenXR needs to be enabled when Godot starts in order to set things up correctly. Check the [Enabled](../godot_gdscript_misc.md) setting in your project settings under **XR > OpenXR**.

You can find several other settings related to OpenXR here as well. These can't be changed while your application is running. The default settings will get us started, but for more information on what's here see OpenXR Settings.

You'll also need to go to **XR > Shaders** in the project settings and check the [Enabled](../godot_gdscript_misc.md) box to enable them. Once you've done that click the **Save & Restart** button.

> **Warning:** Many post process effects have not yet been updated to support stereoscopic rendering. Using these will have adverse effects.

### Setting up the XR scene

Every XR application needs at least an [XROrigin3D](../godot_gdscript_misc.md) and an [XRCamera3D](../godot_gdscript_misc.md) node. Most will have two [XRController3D](../godot_gdscript_misc.md), one for the left hand and one for the right. Keep in mind that the camera and controller nodes should be children of the origin node. Add these nodes to a new scene and rename the controller nodes to `LeftHand` and `RightHand`, your scene should look something like this:

The warning icons are expected and should go away after you configure the controllers. Select the left hand and set it up as follows:

And the right hand:

Right now all these nodes are on the floor, they will be positioned correctly in runtime. To help during development, it can be helpful to move the camera upwards so its `y` is set to `1.7`, and move the controller nodes to `-0.5, 1.0, -0.5` and `0.5, 1.0, -0.5` for respectively the left and right hand.

Next we need to add a script to our root node. Add the following code into this script:

```gdscript
extends Node3D

var xr_interface: XRInterface

func _ready():
    xr_interface = XRServer.find_interface("OpenXR")
    if xr_interface and xr_interface.is_initialized():
        print("OpenXR initialized successfully")

        # Turn off v-sync!
        DisplayServer.window_set_vsync_mode(DisplayServer.VSYNC_DISABLED)

        # Change our main viewport to output to the HMD
        get_viewport().use_xr = true
    else:
        print("OpenXR not initialized, please check if your headset is connected")
```

This code fragment assumes we are using OpenXR, if you wish to use any of the other interfaces you can change the `find_interface` call.

> **Warning:** As you can see in the code snippet above, we turn off v-sync. When using OpenXR you are outputting the rendering results to an HMD that often requires us to run at 90Hz or higher. If your monitor is a 60hz monitor and v-sync is turned on, you will limit the output to 60 frames per second. XR interfaces like OpenXR perform their own sync. Also note that by default the physics engine runs at 60Hz as well and this can result in choppy physics. You should set `Engine.physics_ticks_per_second` to a higher value.

If you run your project at this point in time, everything will work but you will be in a dark world. So to finish off our starting point add a [DirectionalLight3D](../godot_gdscript_nodes_3d.md) and a [WorldEnvironment](../godot_gdscript_nodes_3d.md) node to your scene. You may wish to also add a mesh instance as a child to each controller node just to temporarily visualise them. Make sure you configure a sky in your world environment.

Now run your project, you should be floating somewhere in space and be able to look around.

> **Note:** While traditional level switching can definitely be used with XR applications, where this scene setup is repeated in each level, most find it easier to set this up once and loading levels as a subscene. If you do switch scenes and replicate the XR setup in each one, do make sure you do not run `initialize` multiple times. The effect can be unpredictable depending on the XR interface used. For the rest of this basic tutorial series we will create a game that uses a single scene.

---
