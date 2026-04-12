# Godot 4 C# Tutorials — 2D (Part 3)

> 3 tutorials. C#-specific code examples.

## 2D particle systems

> **Work in progress:** The content of this page was not yet updated for Godot `4.6` and may be **outdated**. If you know how to improve this page or you can confirm that it's up to date, feel free to [open a pull request](https://github.com/godotengine/godot-docs).

### Intro

Particle systems are used to simulate complex physical effects, such as sparks, fire, magic particles, smoke, mist, etc.

The idea is that a "particle" is emitted at a fixed interval and with a fixed lifetime. During its lifetime, every particle will have the same base behavior. What makes each particle different from the rest and provides a more organic look is the "randomness" associated with each parameter. In essence, creating a particle system means setting base physics parameters and then adding randomness to them.

#### Particle nodes

Godot provides two different nodes for 2D particles, [GPUParticles2D](../godot_csharp_nodes_2d.md) and [CPUParticles2D](../godot_csharp_nodes_2d.md). GPUParticles2D is more advanced and uses the GPU to process particle effects. CPUParticles2D is a CPU-driven option with near-feature parity with GPUParticles2D, but lower performance when using large amounts of particles. On the other hand, CPUParticles2D may perform better on low-end systems or in GPU-bottlenecked situations.

While GPUParticles2D is configured via a [ParticleProcessMaterial](../godot_csharp_rendering.md) (and optionally with a custom shader), the matching options are provided via node properties in CPUParticles2D (with the exception of the trail settings).

Going forward there are no plans to add new features to CPUParticles2D, though pull requests to add features already in GPUParticles2D will be accepted. For that reason we recommend using GPUParticles2D unless you have an explicit reason not to.

You can convert a CPUParticles2D node into a GPUParticles2D node by clicking on the node in the scene tree, selecting the 2D workspace, and selecting **CPUParticles2D > Convert to GPUParticles2D** in the toolbar.

It is also possible to convert a GPUParticles2D node to a CPUParticles2D node, however there may be issues if you use GPU-only features.

The rest of this tutorial is going to use the GPUParticles2D node. First, add a GPUParticles2D node to your scene. After creating that node you will notice that only a white dot was created, and that there is a warning icon next to your GPUParticles2D node in the scene dock. This is because the node needs a ParticleProcessMaterial to function.

#### ParticleProcessMaterial

To add a process material to your particles node, go to `Process Material` in your inspector panel. Click on the box next to `Material`, and from the dropdown menu select `New ParticleProcessMaterial`.

Your GPUParticles2D node should now be emitting white points downward.

#### Texture

A particle system can use a single texture or an animation _flipbook_. A flipbook is a texture that contains several frames of animation that can be played back, or chosen at random during emission. This is equivalent to a spritesheet for particles.

The texture is set via the **Texture** property:

##### Using an animation flipbook

Particle flipbooks are suited to reproduce complex effects such as smoke, fire, explosions. They can also be used to introduce random texture variation, by making every particle use a different texture. You can find existing particle flipbook images online, or pre-render them using external tools such as [Blender](https://www.blender.org/) or [EmberGen](https://jangafx.com/software/embergen/).

Using an animation flipbook requires additional configuration compared to a single texture. For demonstration purposes, we'll use this texture with 5 columns and 7 rows (right-click and choose **Save as…**):

To use an animation flipbook, you must create a new CanvasItemMaterial in the Material section of the GPUParticles2D (or CPUParticles2D) node:

In this CanvasItemMaterial, enable **Particle Animation** and set **H Frames** and **V Frames** to the number of columns and rows present in your flipbook texture:

Once this is done, the Animation section in ParticleProcessMaterial (for GPUParticles2D) or in the CPUParticles2D inspector will be effective.

> **Tip:** If your flipbook texture has a black background instead of a transparent background, you will also need to set the blend mode to **Add** instead of **Mix** for correct display. Alternatively, you can modify the texture to have a transparent background in an image editor. In [GIMP](https://gimp.org), this can be done using the **Color > Color to Alpha** menu.

### Time parameters

#### Lifetime

The time in seconds that every particle will stay alive. When lifetime ends, a new particle is created to replace it.

Lifetime: 0.5

Lifetime: 4.0

#### One Shot

When enabled, a GPUParticles2D node will emit all of its particles once and then never again.

#### Preprocess

Particle systems begin with zero particles emitted, then start emitting. This can be an inconvenience when loading a scene and systems like a torch, mist, etc. begin emitting the moment you enter. Preprocess is used to let the system process a given number of seconds before it is actually drawn the first time.

#### Speed Scale

The speed scale has a default value of `1` and is used to adjust the speed of a particle system. Lowering the value will make the particles slower while increasing the value will make the particles much faster.

#### Explosiveness

If lifetime is `1` and there are 10 particles, it means a particle will be emitted every 0.1 seconds. The explosiveness parameter changes this, and forces particles to be emitted all together. Ranges are:

- 0: Emit particles at regular intervals (default value).
- 1: Emit all particles simultaneously.

Values in the middle are also allowed. This feature is useful for creating explosions or sudden bursts of particles:

#### Randomness

All physics parameters can be randomized. Random values range from `0` to `1`. The formula to randomize a parameter is:

#### Fixed FPS

This setting can be used to set the particle system to render at a fixed FPS. For instance, changing the value to `2` will make the particles render at 2 frames per second. Note this does not slow down the particle system itself.

> **Note:** Godot 4.3 does not currently support physics interpolation for 2D particles. As a workaround, disable physics interpolation for the particles node by setting **Node > Physics Interpolation > Mode** at the bottom of the inspector.

#### Fract Delta

Setting Fract Delta to `true` results in fractional delta calculation, which has a smoother particles display effect. This increased smoothness stems from higher accuracy. The difference is more noticeable in systems with high randomness or fast-moving particles. It helps maintain the visual consistency of the particle system, making sure that each particle's motion aligns with its actual lifespan. Without it, particles might appear to jump or move more than they should in a single frame if they are emitted at a point within the frame. The greater accuracy has a performance tradeoff, particularly in systems with a higher amount of particles.

### Drawing parameters

#### Visibility Rect

The visibility rectangle controls the visibility of the particles on screen. If this rectangle is outside of the viewport, the engine will not render the particles on screen.

The rectangle's `W` and `H` properties respectively control its Width and its Height. The `X` and `Y` properties control the position of the upper-left corner of the rectangle, relative to the particle emitter.

You can have Godot generate a Visibility Rect automatically using the toolbar above the 2d view. To do so, select the GPUParticles2D node and Click `Particles > Generate Visibility Rect`. Godot will simulate the Particles2D node emitting particles for a few seconds and set the rectangle to fit the surface the particles take.

You can control the emit duration with the `Generation Time (sec)` option. The maximum value is 25 seconds. If you need more time for your particles to move around, you can temporarily change the `preprocess` duration on the Particles2D node.

#### Local Coords

By default, this option is off. It means that the space that particles are emitted to is global, and **not** relative to the node. If the node is moved, existing particles are not moved with it:

If enabled, particles will emit to local space, meaning that if the node is moved, already emitted particles are also affected:

#### Draw Order

This controls the order in which individual particles are drawn. `Index` means particles are drawn according to their emission order (default). `Lifetime` means they are drawn in order of remaining lifetime.

### Particle Process Material Settings

For information on the settings in the ParticleProcessMaterial see this page.

---

## Using TileMaps

> **See also:** This page assumes you have created or downloaded a TileSet already. If not, please read Using TileSets first as you will need a TileSet to create a TileMap.

### Introduction

A tilemap is a grid of tiles used to create a game's layout. There are several benefits to using [TileMapLayer](../godot_csharp_nodes_2d.md) nodes to design your levels. First, they make it possible to draw the layout by "painting" the tiles onto a grid, which is much faster than placing individual [Sprite2D](../godot_csharp_nodes_2d.md) nodes one by one. Second, they allow for much larger levels because they are optimized for drawing large numbers of tiles. Finally, you can add collision, occlusion, and navigation shapes to tiles, adding greater functionality to the TileMap.

### Specifying the TileSet in the TileMapLayer

If you've followed the previous page on Using TileSets, you should have a TileSet resource that is built into the TileMapLayer node. This is good for prototyping, but in a real world project, you will generally have multiple levels reusing the same tileset.

The recommended way to reuse the same TileSet in several TileMapLayer nodes is to save the TileSet to an external resource. To do so, click the dropdown next to the TileSet resource and choose **Save**:

### Multiple TileMapLayers and settings

When working with tilemaps it's generally advised that you use multiple TileMapLayer nodes when appropriate. Using multiple layers can be advantageous, for example, this allows you to distinguish foreground tiles from background tiles for better organization. You can place one tile per layer at a given location, which allows you to overlap several tiles together if you have more than one layer.

Each TileMapLayer node has several properties you can adjust:

- **Enabled:** If `true`, the layer is visible in the editor and when running the project.
- **TileSet** The tileset used by the TileMapLayer node.

#### Rendering

- **Y Sort Origin:** The vertical offset to use for Y-sorting on each tile (in pixels). Only effective if **Y Sort Enabled** under CanvasItem settings is `true`.
- **X Draw Order Reversed** Reverses the order tiles are drawn on the X axis. Requires that **Y Sort Enabled** under CanvasItem settings is `true`.
- **Rendering Quadrant Size** A quadrant is a group of tiles drawn together on a single CanvasItem for optimization purposes. This setting defines the length of a square's side in the map's coordinate system. The quadrant size does not apply to a Y sorted TileMapLayer since tiles are grouped by Y position in that case.

#### Physics

- **Collision Enabled** Enables or disables collision.
- **Use Kinematic Bodies** When true TileMapLayer collision shapes will be instantiated as kinematic bodies.
- **Collision Visibility Mode** Whether or not the TileMapLayer's collision shapes are visible. If set to default, then it depends on the show collision debug settings.

#### Navigation

- **Navigation Enabled** Whether or not navigation regions are enabled.
- **Navigation Visible** Whether or not the TileMapLayer's navigation meshes are visible. If set to default then it depends on the show navigation debug settings.

> **Tip:** TileMap built-in navigation has many practical limitations that result in inferior pathfinding performance and pathfollowing quality. After designing the TileMap consider baking it to a more optimized navigation mesh (and disabling the TileMap NavigationLayer) using a [NavigationRegion2D](../godot_csharp_nodes_2d.md) or the [NavigationServer2D](../godot_csharp_misc.md). See [Using navigation meshes](tutorials_navigation.md) for additional information.

> **Warning:** 2D navigation meshes can not be "layered" or stacked on top of each other like visuals or physic shapes. Attempting to stack navigation meshes on the same navigation map will result in merge and logical errors that break the pathfinding.

#### Reordering layers

You can reorder layers by drag-and-dropping their node in the Scene tab. You can also switch between which TileMapLayer node you're working on by using the buttons in the top right corner of the TileMap editor.

> **Note:** You can create, rename or reorder layers in the future without affecting existing tiles. Be careful though, as _removing_ a layer will also remove all tiles that were placed on the layer.

### Opening the TileMap editor

Select the TileMapLayer node, then open the TileMap panel at the bottom of the editor:

### Selecting tiles to use for painting

First, if you've created additional layers above, make sure you've selected the layer you wish to paint on:

> **Tip:** In the 2D editor, the layers you aren't currently editing from the same TileMapLayer node will appear grayed out while in the TileMap editor. You can disable this behavior by clicking the icon next to the layer selection menu (**Highlight Selected TileMap Layer** tooltip).

You can skip the above step if you haven't created additional layers, as the first layer is automatically selected when entering the TileMap editor.

Before you can place tiles in the 2D editor, you must select one or more tiles in the TileMap panel located at the bottom of the editor. To do so, click a tile in the TileMap panel, or hold down the mouse button to select multiple tiles:

> **Tip:** Like in the 2D and TileSet editors, you can pan across the TileMap panel using the middle or right mouse buttons, and zoom using the mouse wheel or buttons in the top-left corner.

You can also hold down Shift to append to the current selection. When selecting more than one tile, multiple tiles will be placed every time you perform a painting operation. This can be used to paint structures composed of multiple tiles in a single click (such as large platforms or trees).

The final selection does not have to be contiguous: if there is empty space between selected tiles, it will be left empty in the pattern that will be painted in the 2D editor.

If you've created alternative tiles in your TileSet, you can select them for painting on the right of the base tiles:

Lastly, if you've created a _scenes collection_ in the TileSet, you can place scene tiles in the TileMap:

### Painting modes and tools

Using the toolbar at the top of the TileMap editor, you can choose between several painting modes and tools. These modes affect operation when clicking in the 2D editor, **not** the TileMap panel itself.

From left to right, the painting modes and tools you can choose are:

#### Selection

Select tiles by clicking a single tile, or by holding down the left mouse button to select multiple with a rectangle in the 2D editor. Note that empty space cannot be selected: if you create a rectangle selection, only non-empty tiles will be selected.

To append to the current selection, hold Shift then select a tile. To remove from the current selection, hold Ctrl then select a tile.

The selection can then be used in any other painting mode to quickly create copies of an already-placed pattern.

You can remove the selected tiles from the TileMap by pressing Del.

You can toggle this mode temporarily while in Paint mode by holding Ctrl then performing a selection.

> **Tip:** You can copy and paste tiles that were already placed by performing a selection, pressing Ctrl + C then pressing Ctrl + V. The selection will be pasted after left-clicking. You can press Ctrl + V another time to perform more copies this way. Right-click or press Escape to cancel pasting.

#### Paint

The standard Paint mode allows you to place tiles by clicking or holding down the left mouse button.

If you right-click, the currently selected tile will be erased from the tilemap. In other words, it will be replaced by empty space.

If you have selected multiple tiles in the TileMap or using the Selection tool, they will be placed every time you click or drag the mouse while holding down the left mouse button.

> **Tip:** While in Paint mode, you can draw a line by holding Shift _before_ holding down the left mouse button, then dragging the mouse to the line's end point. This is identical to using the Line tool described below. You can also draw a rectangle by holding Ctrl and Shift _before_ holding down the left mouse button, then dragging the mouse to the rectangle's end point. This is identical to using the Rectangle tool described below. Lastly, you can pick existing tiles in the 2D editor by holding Ctrl then clicking on a tile (or holding and dragging the mouse). This will switch the currently painted tile(s) to the tile(s) you've just clicked. This is identical to using the Picker tool described below.

#### Line

After selecting Line Paint mode, you can draw in a line that is always 1 tile thick (no matter its orientation).

If you right-click while in Line Paint mode, you will erase in a line.

If you have selected multiple tiles in the TileMap or using the Selection tool, you can place them in a repeating pattern across the line.

You can toggle this mode temporarily while in Paint or Eraser mode by holding Shift then drawing.

#### Rectangle

After selecting Rectangle Paint mode, you can draw in an axis-aligned rectangle.

If you right-click while in Rectangle Paint mode, you will erase in an axis-aligned rectangle.

If you have selected multiple tiles in the TileMap or using the Selection tool, you can place them in a repeating pattern within the rectangle.

You can toggle this mode temporarily while in Paint or Eraser mode by holding Ctrl and Shift then drawing.

#### Bucket Fill

After selecting Bucket Fill mode, you can choose whether painting should be limited to contiguous areas only by toggling the **Contiguous** checkbox that appears on the right of the toolbar.

If you enable **Contiguous** (the default), only matching tiles that touch the current selection will be replaced. This contiguous check is performed horizontally and vertically, but _not_ diagonally.

If you disable **Contiguous**, all tiles with the same ID in the entire TileMap will be replaced by the currently selected tile. If selecting an empty tile with **Contiguous** unchecked, all tiles in the rectangle that encompasses the TileMap's effective area will be replaced instead.

If you right-click while in Bucket Fill mode, you will replace matching tiles with empty tiles.

If you have selected multiple tiles in the TileMap or using the Selection tool, you can place them in a repeating pattern within the filled area.

#### Picker

After selecting Picker mode, you can pick existing tiles in the 2D editor by holding Ctrl then clicking on a tile. This will switch the currently painted tile to the tile you've just clicked. You can also pick multiple tiles at once by holding down the left mouse button and forming a rectangle selection. Only non-empty tiles can be picked.

You can toggle this mode temporarily while in Paint mode by holding Ctrl then clicking or dragging the mouse.

#### Eraser

This mode is combined with any other painting mode (Paint, Line, Rectangle, Bucket Fill). When eraser mode is enabled, tiles will be replaced by empty tiles instead of drawing new lines when left-clicking.

You can toggle this mode temporarily while in any other mode by right-clicking instead of left-clicking.

### Painting randomly using scattering

While painting, you can optionally enable _randomization_. When enabled, a random tile will be chosen between all the currently selected tiles when painting. This is supported with the Paint, Line, Rectangle and Bucket Fill tools. For effective paint randomization, you must select multiple tiles in the TileMap editor or use scattering (both approaches can be combined).

If **Scattering** is set to a value greater than 0, there is a chance that no tile will be placed when painting. This can be used to add occasional, non-repeating detail to large areas (such as adding grass or crumbs on a large top-down TileMap).

Example when using Paint mode:

Example when using Bucket Fill mode:

> **Note:** Eraser mode does not take randomization and scattering into account. All tiles within the selection are always removed.

### Saving and loading premade tile placements using patterns

While you can copy and paste tiles while in Select mode, you may wish to save premade _patterns_ of tiles to place together in a go. This can be done on a per-TileMap basis by choosing the **Patterns** tab of the TileMap editor.

To create a new pattern, switch to Select mode, perform a selection and press Ctrl + C. Click on empty space within the Patterns tab (a blue focus rectangle should appear around the empty space), then press Ctrl + V:

To use an existing pattern, click its image in the **Patterns** tab, switch to any painting mode, then left-click somewhere in the 2D editor:

Like multi-tile selections, patterns will be repeated if used with the Line, Rectangle or Bucket Fill painting modes.

> **Note:** Despite being edited in the TileMap editor, patterns are stored in the TileSet resource. This allows reusing patterns in different TileMapLayer nodes after loading a TileSet resource saved to an external file.

### Handling tile connections automatically using terrains

To use terrains, the TileMapLayer node must feature at least one terrain set and a terrain within this terrain set. See Creating terrain sets (autotiling) if you haven't created a terrain set for the TileSet yet.

There are 3 kinds of painting modes available for terrain connections:

- **Connect**, where tiles are connected to surrounding tiles on the same TileMapLayer.
- **Path**, where tiles are connected to tiles painted in the same stroke (until the mouse button is released).
- Tile-specific overrides to resolve conflicts or handle situations not covered by the terrain system.

The Connect mode is easier to use, but Path is more flexible as it allows for more artist control during painting. For instance, Path can allow roads to be directly adjacent to each other without being connected to each other, while Connect will force both roads to be connected.

Lastly, you can select specific tiles from the terrain to resolve conflicts in certain situations:

Any tile that has at least one of its bits set to a value set to the corresponding terrain ID will appear in the list of tiles to choose from.

### Handling missing tiles

If you remove tiles in the TileSet that are referenced in a TileMap, the TileMap will display a placeholder to indicate that an invalid tile ID is placed:

These placeholders are **not** visible in the running project, but the tile data is still persisted to disk. This allows you to safely close and reopen such scenes. Once you re-add a tile with the matching ID, the tiles will appear with the new tile's appearance.

> **Note:** Missing tile placeholders may not be visible until you select the TileMapLayer node and open the TileMap editor.

---

## Using TileSets

### Introduction

A tilemap is a grid of tiles used to create a game's layout. There are several benefits to using [TileMapLayer](../godot_csharp_nodes_2d.md) nodes to design your levels. First, they let you draw a layout by "painting" tiles onto a grid, which is much faster than placing individual [Sprite2D](../godot_csharp_nodes_2d.md) nodes one by one. Second, they allow for larger levels because they are optimized for drawing large numbers of tiles. Finally, they allow you to add greater functionality to your tiles with collision, occlusion, and navigation shapes.

To use TileMapLayer nodes, you will need to create a TileSet first. A TileSet is a collection of tiles that can be placed in a TileMapLayer node. After creating a TileSet, you will be able to place them using the TileMap editor.

To follow this guide, you will need an image containing your tiles where every tile has the same size (large objects can be split into several tiles). This image is called a _tilesheet_. Tiles do not have to be square: they can be rectangular, hexagonal, or isometric (pseudo-3D perspective).

### Creating a new TileSet

#### Using a tilesheet

This demonstration will use the following tiles taken from [Kenney's "Abstract Platformer" pack](https://kenney.nl/assets/abstract-platformer). We'll use this particular _tilesheet_ from the set:

Create a new **TileMapLayer** node, then select it and create a new TileSet resource in the inspector:

After creating the TileSet resource, click the value to unfold it in the inspector. The default tile shape is Square, but you can also choose Isometric, Half-Offset Square or Hexagon (depending on the shape of your tile images). If using a tile shape other than Square, you may also need to adjust the **Tile Layout** and **Tile Offset Axis** properties. Lastly, enabling the **Rendering > UV Clipping** property may be useful if you wish tiles to be clipped by their tile coordinates. This ensures tiles cannot draw outside their allocated area on the tilesheet.

Set the tile size to 64×64 in the inspector to match the example tilesheet:

If relying on automatic tiles creation (like we're about to do here), you must set the tile size **before** creating the _atlas_. The atlas will determine which tiles from the tilesheet can be added to a TileMapLayer node (as not every part of the image may be a valid tile).

Open the **TileSet** panel at the bottom of the editor, then click and drag the tilesheet image onto the panel. You will be asked whether to create tiles automatically. Answer **Yes**:

This will automatically create tiles according to the tile size you specified earlier in the TileSet resource. This greatly speeds up initial tile setup.

> **Note:** When using automatic tile generation based on image contents, parts of the tilesheet that are _fully_ transparent will not have tiles generated.

If there are tiles from the tilesheet you do not wish to be present in atlas, choose the Eraser tool at the top of the tileset preview, then click the tiles you wish to remove:

You can also right-click a tile and choose **Delete**, as an alternative to the Eraser tool.

> **Tip:** Like in the 2D and TileMap editors, you can pan across the TileSet panel using the middle or right mouse buttons, and zoom using the mouse wheel or buttons in the top-left corner.

If you wish to source tiles from several tilesheet images for a single TileSet, create additional atlases and assign textures to each of them before continuing. It is also possible to use one image per tile this way (although using tilesheets is recommended for better usability).

You can adjust properties for the atlas in the middle column:

The following properties can be adjusted on the atlas:

- **ID:** The identifier (unique within this TileSet), used for sorting.
- **Name:** The human-readable name for the atlas. Use a descriptive name here for organizational purposes (such as "terrain", "decoration", etc).
- **Margins:** The margins on the image's edges that should not be selectable as tiles (in pixels). Increasing this can be useful if you download a tilesheet image that has margins on the edges (e.g. for attribution).
- **Separation:** The separation between each tile on the atlas in pixels. Increasing this can be useful if the tilesheet image you're using contains guides (such as outlines between every tile).
- **Texture Region Size:** The size of each tile on the atlas in pixels. In most cases, this should match the tile size defined in the TileMapLayer property (although this is not strictly necessary).
- **Use Texture Padding:** If checked, adds a 1-pixel transparent edge around each tile to prevent texture bleeding when filtering is enabled. It's recommended to leave this enabled unless you're running into rendering issues due to texture padding.

Note that changing texture margin, separation and region size may cause tiles to be lost (as some of them would be located outside the atlas image's coordinates). To regenerate tiles automatically from the tilesheet, use the three vertical dots menu button at the top of the TileSet editor and choose **Create Tiles in Non-Transparent Texture Regions**:

#### Using a collection of scenes

You can also place actual _scenes_ as tiles. This allows you to use any collection of nodes as a tile. For example, you could use scene tiles to place gameplay elements, such as shops the player may be able to interact with. You could also use scene tiles to place AudioStreamPlayer2Ds (for ambient sounds), particle effects, and more.

> **Warning:** Scene tiles come with a greater performance overhead compared to atlases, as every scene is instanced individually for every placed tile. It's recommended to only use scene tiles when necessary. To draw sprites in a tile without any kind of advanced manipulation, **use atlases instead**.

For this example, we'll create a scene containing a CPUParticles2D root node. Save this scene to a scene file (separate from the scene containing the TileMapLayer), then switch to the scene containing the TileMapLayer node. Open the TileSet editor, and create a new **Scenes Collection** in the left column:

After creating a scenes collection, you can enter a descriptive name for the scenes collection in the middle column if you wish. Select this scenes collection then create a new scene slot:

Select this scene slot in the right column, then use **Quick Load** (or **Load**) to load the scene file containing the particles:

You now have a scene tile in your TileSet. Once you switch to the TileMap editor, you'll be able to select it from the scenes collection and paint it like any other tile.

### Merging several atlases into a single atlas

Using multiple atlases within a single TileSet resource can sometimes be useful, but it can also be cumbersome in certain situations (especially if you're using one image per tile). Godot allows you to merge several atlases into a single atlas for easier organization.

To do so, you must have more than one atlas created in the TileSet resource. Use the "three vertical dots" menu button located at the bottom of the list of atlases, then choose **Open Atlas Merging Tool**:

This will open a dialog, in which you can select several atlases by holding Shift or Ctrl then clicking on multiple elements:

Choose **Merge** to merge the selected atlases into a single atlas image (which translates to a single atlas within the TileSet). The unmerged atlases will be removed within the TileSet, but _the original tilesheet images will be kept on the filesystem_. If you don't want the unmerged atlases to be removed from the TileSet resource, choose **Merge (Keep Original Atlases)** instead.

> **Tip:** TileSet features a system of _tile proxies_. Tile proxies are a mapping table that allows notifying the TileMap using a given TileSet that a given set of tile identifiers should be replaced by another one. Tile proxies are automatically set up when merging different atlases, but they can also be set manually thanks to the **Manage Tile Proxies** dialog you can access using the "three vertical dots" menu mentioned above. Manually creating tile proxies may be useful when you changed an atlas ID or want to replace all tiles from an atlas by the ones from another atlas. Note that when editing a TileMap, you can replace all cells by their corresponding mapped value.

### Adding collision, navigation and occlusion to the TileSet

We've now successfully created a basic TileSet. We could start using it in the TileMapLayer node now, but it currently lacks any form of collision detection. This means the player and other objects could walk straight through the floor or walls.

If you use [2D navigation](tutorials_navigation.md), you'll also need to define navigation polygons for tiles to generate a navigation mesh that agents can use for pathfinding.

Lastly, if you use 2D lights and shadows or GPUParticles2D, you may also want your TileSet to be able to cast shadows and collide with particles. This requires defining occluder polygons for "solid" tiles on the TileSet.

To be able to define collision, navigation and occlusion shapes for each tile, you will need to create a physics, navigation or occlusion layer for the TileSet resource first. To do so, select the TileMapLayer node, click the TileSet property value in the inspector to edit it then unfold **Physics Layers** and choose **Add Element**:

If you also need navigation support, now is a good time to create a navigation layer:

If you need support for light polygon occluders, now is a good time to create an occlusion layer:

> **Note:** Future steps in this tutorial are tailored to creating collision polygons, but the procedure for navigation and occlusion is very similar. Their respective polygon editors behave in the same way, so these steps are not repeated for brevity. The only caveat is that the tile's occlusion polygon property is part of a **Rendering** subsection in the atlas inspector. Make sure to unfold this section so you can edit the polygon.

After creating a physics layer, you have access to the **Physics Layer** section in the TileSet atlas inspector:

You can quickly create a rectangle collision shape by pressing F while the TileSet editor is focused. If the keyboard shortcut doesn't work, try clicking in the empty area around the polygon editor to focus it:

In this tile collision editor, you have access to all the 2D polygon editing tools:

- Use the toolbar above the polygon to toggle between creating a new polygon, editing an existing polygon and removing points on the polygon. The "three vertical dots" menu button offers additional options, such as rotating and flipping the polygon.
- Create new points by clicking and dragging a line between two points.
- Remove a point by right-clicking it (or using the Remove tool described above and left-clicking).
- Pan in the editor by middle-clicking or right-clicking. (Right-click panning can only be used in areas where there is no point nearby.)

You can use the default rectangle shape to quickly create a triangle-shaped collision shape by removing one of the points:

You can also use the rectangle as a base for more complex shapes by adding more points:

> **Tip:** If you have a large tileset, specifying the collision for each tile individually could take a lot of time. This is especially true as TileMaps tend to have many tiles with common collision patterns (such as solid blocks or 45-degree slopes). To apply a similar collision shape to several tiles quickly, use functionality to **assign properties to multiple tiles at once**.

### Assigning custom metadata to the TileSet's tiles

You can assign custom data on a per-tile basis using _custom data layers_. This can be useful to store information specific to your game, such as the damage that a tile should deal when the player touches it, or whether a tile can be destroyed using a weapon.

The data is associated with the tile in the TileSet: all instances of the placed tile will use the same custom data. If you need to create a variant of a tile that has different custom data, this can be done by **creating an alternative tile** and changing the custom data for the alternative tile only.

You can reorder custom data without breaking existing metadata: the TileSet editor will update automatically after reordering custom data properties.

With the custom data layers example shown above, we're assigning a tile to have the `damage_per_second` metadata set to `25` and the `destructible` metadata to `false`:

**Tile property painting** can also be used for custom data:

### Creating terrain sets (autotiling)

> **Note:** This functionality was implemented in a different form as _autotiling_ in Godot 3.x. Terrains are essentially a more powerful replacement of autotiles. Unlike autotiles, terrains can support transitions from one terrain to another, as a tile may define several terrains at once. Unlike before, where autotiles were a specific kind of tiles, terrains are only a set of properties assigned to atlas tiles. These properties are then used by a dedicated TileMap painting mode that selects tiles featuring terrain data in a smart way. This means any terrain tile can be either painted as terrain or as a single tile, like any other.

A "polished" tileset generally features variations that you should use on corners or edges of platforms, floors, etc. While these can be placed manually, this quickly becomes tedious. Handling this situation with procedurally generated levels can also be difficult and require a lot of code.

Godot offers _terrains_ to perform this kind of tile connection automatically. This allows you to have the "correct" tile variants automatically used.

Terrains are grouped into terrain sets. Each terrain set is assigned a mode from **Match Corners and Sides**, **Match Corners** and **Match sides**. They define how terrains are matched to each other in a terrain set.

> **Note:** The above modes correspond to the previous bitmask modes autotiles used in Godot 3.x: 2×2, 3×3 or 3×3 minimal. This is also similar to what the [Tiled](https://www.mapeditor.org/) editor features.

Select the TileMapLayer node, go to the inspector and create a new terrain set within the TileSet _resource_:

After creating a terrain set, you **must** create one or more terrains _within_ the terrain set:

In the TileSet editor, switch to Select mode and click a tile. In the middle column, unfold the **Terrains** section then assign a terrain set ID and a terrain ID for the tile. `-1` means "no terrain set" or "no terrain", which means you must set **Terrain Set** to `0` or greater before you can set **Terrain** to `0` or greater.

> **Note:** Terrain set IDs and terrain IDs are independent from each other. They also start from `0`, not `1`.

After doing so, you can now configure the **Terrain Peering Bits** section which becomes visible in the middle column. The peering bits determine which tile will be placed depending on neighboring tiles. `-1` is a special value which refers to empty space.

For example, if a tile has all its bits set to `0` or greater, it will only appear if _all_ 8 neighboring tiles are using a tile with the same terrain ID. If a tile has its bits set to `0` or greater, but the top-left, top and top-right bits are set to `-1`, it will only appear if there is empty space on top of it (including diagonally).

An example configuration for a full tilesheet may look as follows:

### Assigning properties to multiple tiles at once

There are two ways to assign properties to multiple tiles at once. Depending on your use cases, one method may be faster than the other:

#### Using multiple tile selection

If you wish to configure various properties on several tiles at once, choose the **Select** mode at the top of the TileSet editor:

After doing this, you can select multiple tiles on the right column by holding Shift then clicking on tiles. You can also perform rectangle selection by holding down the left mouse button then dragging the mouse. Lastly, you can deselect tiles that were already selected (without affecting the rest of the selection) by holding Shift then clicking on a selected tile.

You can then assign properties using the inspector in the middle column of the TileSet editor. Only properties that you change here will be applied to all selected tiles. Like in the editor's inspector, properties that differ on selected tiles will remain different until you edit them.

With numerical and color properties, you will also see a preview of the property's value on all tiles in the atlas after editing a property:

#### Using tile property painting

If you wish to apply a single property to several tiles at once, you can use the _property painting_ mode for this purpose.

Configure a property to be painted in the middle column, then click on tiles (or hold down the left mouse button) in the right column to "paint" properties onto tiles.

Tile property painting is especially useful with properties that are time-consuming to set manually, such as collision shapes:

### Creating alternative tiles

Sometimes, you want to use a single tile image (found only once within the atlas), but configured in different ways. For example, you may want to use the same tile image, but rotated, flipped, or modulated with a different color. This can be done using _alternative tiles_.

> **Tip:** Since Godot 4.2, you don't have to create alternative tiles to rotate or flip tiles anymore. You can rotate any tile while placing it in the TileMap editor by using the rotation/flip buttons in the TileMap editor toolbar.

To create an alternative tile, right-click a base tile in the atlas displayed by the TileSet editor, then choose **Create an Alternative Tile**:

If currently in Select mode, the alternative tile will already be selected for editing. If not currently in Select mode, you can still create alternative tiles, but you will need to switch to Select mode and select the alternative tile to edit it.

If you don't see the alternative tile, pan over to the right of the atlas image, as alternative tiles always appear on the right of base tiles of a given atlas in the TileSet editor:

After selecting an alternative tile, you can change any properties using the middle column like you would on a base tile. However, the list of exposed properties is different compared to base tiles:

- **Alternative ID:** The unique numerical identifier for this alternative tile. Changing it will break existing TileMaps, so be careful! This ID also controls the sorting in the list of alternative tiles displayed in the editor.
- **Rendering > Flip H:** If `true`, the tile is horizontally flipped.
- **Rendering > Flip V:** If `true`, the tile is vertically flipped.
- **Rendering > Transpose:** If `true`, the tile is rotated 90 degrees _counter-clockwise_ and then flipped vertically. In practice, this means that to rotate a tile by 90 degrees clockwise without flipping it, you should enable **Flip H** and **Transpose**. To rotate a tile by 180 degrees clockwise, enable **Flip H** and **Flip V**. To rotate a tile by 270 degrees clockwise, enable **Flip V** and **Transpose**.
- **Rendering > Texture Origin:** The origin to use for drawing the tile. This can be used to visually offset the tile compared to the base tile.
- **Rendering > Modulate:** The color multiplier to use when rendering the tile.
- **Rendering > Material:** The material to use for this tile. This can be used to apply a different blend mode or custom shaders to a single tile.
- **Z Index:** The sorting order for this tile. Higher values will make the tile render in front of others on the same layer.
- **Y Sort Origin:** The vertical offset to use for tile sorting based on its Y coordinate (in pixels). This allows using layers as if they were on different height for top-down games. Adjusting this can help alleviate issues with sorting certain tiles. Only effective if **Y Sort Enabled** is `true` on the TileMapLayer node under **CanvasItem > Ordering**

You can create an additional alternative tile variant by clicking the large "+" icon next to the alternative tile. This is equivalent to selecting the base tile and right-clicking it to choose **Create an Alternative Tile** again.

> **Note:** When creating an alternative tile, none of the properties from the base tile are inherited. You must set properties again on the alternative tile if you wish those to be identical on the base tile and the alternative tile.

---
