# Godot 4 GDScript Tutorials — Assets Pipeline (Part 2)

> 5 tutorials. GDScript-specific code examples.

## Node type customization using name suffixes

Many times, when editing a scene, there are common tasks that need to be done after exporting:

- Adding collision detection to objects.
- Setting objects as navigation meshes.
- Deleting nodes that are not used in the game engine (like specific lights used for modeling).

To simplify this workflow, Godot offers several suffixes that can be added to the names of the objects in your 3D modeling software. When imported, Godot will detect suffixes in object names and will perform actions automatically.

> **Warning:** All the suffixes described below can be used with `-`, `$`, and `_` and are **case-insensitive**.

### Opting out

If you do not want Godot to perform any of the actions described below, you can set the `nodes/use_node_type_suffixes` import option to `false`. This will disable all node type suffixes, which keeps nodes the same type as the original file indicated. However, the `-noimp` suffix will still be respected, as well as non-node suffixes like `-vcol` or `-loop`.

Alternatively, you can completely opt out of all name suffixes by setting the `nodes/use_name_suffixes` import option to `false`. This will completely stop the general scene import code from looking at name suffixes. However, the format-specific import code may still look at name suffixes, such as the glTF importer checking for the `-loop` suffix.

Disabling these options makes editor-imported files more similar to the original files, and more similar to importing files at runtime. For an import workflow that works at runtime, gives more predictable results, and only has explicitly defined behavior, consider setting these options to `false` and using [GLTFDocumentExtension](../godot_gdscript_misc.md) instead.

### Remove nodes and animations (-noimp)

Nodes and animations that have the `-noimp` suffix will be removed at import time no matter what their type is. They will not appear in the imported scene.

This is equivalent to enabling **Skip Import** for a node in the Advanced Import Settings dialog.

### Create collisions (-col, -convcol, -colonly, -convcolonly)

The option `-col` will work only for Mesh objects. If it is detected, a child static collision node will be added, using the same geometry as the mesh. This will create a triangle mesh collision shape, which is a slow, but accurate option for collision detection. This option is usually what you want for level geometry (but see also `-colonly` below).

The option `-convcol` will create a [ConvexPolygonShape3D](../godot_gdscript_misc.md) instead of a [ConcavePolygonShape3D](../godot_gdscript_misc.md). Unlike triangle meshes which can be concave, a convex shape can only accurately represent a shape that doesn't have any concave angles (a pyramid is convex, but a hollow box is concave). Due to this, convex collision shapes are generally not suited for level geometry. When representing simple enough meshes, convex collision shapes can result in better performance compared to a triangle collision shape. This option is ideal for simple or dynamic objects that require mostly-accurate collision detection.

However, in both cases, the visual geometry may be too complex or not smooth enough for collisions. This can create physics glitches and slow down the engine unnecessarily.

To solve this, the `-colonly` modifier exists. It will remove the mesh upon importing and will create a [StaticBody3D](../godot_gdscript_nodes_3d.md) collision instead. This helps the visual mesh and actual collision to be separated.

The option `-convcolonly` works in a similar way, but will create a [ConvexPolygonShape3D](../godot_gdscript_misc.md) instead using convex decomposition.

With Collada files, the option `-colonly` can also be used with Blender's empty objects. On import, it will create a [StaticBody3D](../godot_gdscript_nodes_3d.md) with a collision node as a child. The collision node will have one of a number of predefined shapes, depending on Blender's empty draw type:

- Single arrow will create a [SeparationRayShape3D](../godot_gdscript_misc.md).
- Cube will create a [BoxShape3D](../godot_gdscript_misc.md).
- Image will create a [WorldBoundaryShape3D](../godot_gdscript_misc.md).
- Sphere (and the others not listed) will create a [SphereShape3D](../godot_gdscript_misc.md).

When possible, **try to use a few primitive collision shapes** instead of triangle mesh or convex shapes. Primitive shapes often have the best performance and reliability.

> **Note:** For better visibility on Blender's editor, you can set the "X-Ray" option on collision empties and set some distinct color for them by changing **Edit > Preferences > Themes > 3D Viewport > Empty**. If using Blender 2.79 or older, follow these steps instead: **User Preferences > Themes > 3D View > Empty**.

> **See also:** See [Collision shapes (3D)](tutorials_physics.md) for a comprehensive overview of collision shapes.

### Create Occluder (-occ, -occonly)

If a mesh is imported with the `-occ` suffix an [Occluder3D](../godot_gdscript_resources.md) node will be created based on the geometry of the mesh, it does not replace the mesh. A mesh node with the `-occonly` suffix will be converted to an [Occluder3D](../godot_gdscript_resources.md) on import.

### Create navigation (-navmesh)

A mesh node with the `-navmesh` suffix will be converted to a navigation mesh. The original Mesh object will be removed at import-time.

### Create a VehicleBody (-vehicle)

A mesh node with the `-vehicle` suffix will be imported as a child to a [VehicleBody3D](../godot_gdscript_nodes_3d.md) node.

### Create a VehicleWheel (-wheel)

A mesh node with the `-wheel` suffix will be imported as a child to a [VehicleWheel3D](../godot_gdscript_nodes_3d.md) node.

### Rigid Body (-rigid)

A mesh node with the `-rigid` suffix will be imported as a [RigidBody3D](../godot_gdscript_nodes_3d.md).

### Animation loop (-loop, -cycle)

Animation clips in the source 3D file that start or end with the token `loop` or `cycle` will be imported as a Godot [Animation](../godot_gdscript_resources.md) with the loop flag set. **Unlike the other suffixes described above, this does not require a hyphen.**

In Blender, this requires using the NLA Editor and naming the Action with the `loop` or `cycle` prefix or suffix.

### Material alpha (-alpha)

A material with the `-alpha` suffix will be imported with the [TRANSPARENCY_ALPHA](../godot_gdscript_misc.md) transparency mode.

### Material vertex color (-vcol)

A material with the `-vcol` suffix will be imported with the [FLAG_ALBEDO_FROM_VERTEX_COLOR](../godot_gdscript_misc.md) and [FLAG_SRGB_VERTEX_COLOR](../godot_gdscript_misc.md) flags set.

---

## Importing audio samples

### Supported audio formats

Godot provides 3 options to import your audio data: WAV, Ogg Vorbis and MP3.

Each format has different advantages:

- WAV files use raw data or light compression (IMA ADPCM or Quite OK Audio). Currently they can only be imported in raw format, but Godot allows compression after import. They are lightweight to play back on the CPU (hundreds of simultaneous voices in this format are fine). The downside is that they take up a lot of disk space.
- Ogg Vorbis files use a stronger compression that results in much smaller file size, but require significantly more processing power to play back.
- MP3 files use better compression than WAV with IMA ADPCM or Quite OK Audio, but worse than Ogg Vorbis. This means that an MP3 file with roughly equal quality to Ogg Vorbis will be significantly larger. On the bright side, MP3 requires less CPU usage to play back compared to Ogg Vorbis.

> **Note:** If you've compiled the Godot editor from source with specific modules disabled, some formats may not be available.

Here is a comparative chart representing the file size of 1 second of audio with each format:

| Format                       | 1 second of audio |
| ---------------------------- | ----------------- |
| WAV 24-bit, 96 kHz, stereo   | 576 KB            |
| WAV 16-bit, 44 kHz, mono     | 88 KB             |
| WAV IMA ADPCM, 44 kHz, mono  | 22 KB             |
| Quite OK Audio, 44 kHz, mono | 17 KB             |
| MP3 192 Kb/s, stereo         | 24 KB             |
| Ogg Vorbis 128 Kb/s, stereo  | 16 KB             |
| Ogg Vorbis 96 Kb/s, stereo   | 12 KB             |

Note that the MP3 and Ogg Vorbis figures can vary depending on the encoding type. The above figures use CBR encoding for simplicity, but most Ogg Vorbis and MP3 files you can find online are encoded with VBR encoding which is more efficient. VBR encoding makes the effective audio file size depend on how "complex" the source audio is.

> **Tip:** Consider using WAV for short and repetitive sound effects, and Ogg Vorbis for music, speech, and long sound effects. MP3 is useful for mobile and web projects where CPU resources are limited, especially when playing multiple compressed sounds at the same time (such as long ambient sounds).

### Importing audio samples

Several options are available in the Import dock after selecting a WAV file in the FileSystem dock:

The set of options available after selecting an Ogg Vorbis or MP3 file is different:

After importing a sound, you can play it back using the AudioStreamPlayer, AudioStreamPlayer2D or AudioStreamPlayer3D nodes. See [Audio streams](tutorials_audio.md) for more information.

### Import options (WAV)

### Force > 8 Bit

If enabled, forces the imported audio to use 8-bit quantization if the source file is 16-bit or higher.

Enabling this is generally not recommended, as 8-bit quantization decreases audio quality significantly. If you need smaller file sizes, consider using Ogg Vorbis or MP3 audio instead.

### Force > Mono

If enabled, forces the imported audio to be mono if the source file is stereo. This decreases the file size by 50% by merging the two channels into one.

### Force > Max Rate

If set to a value greater than `0`, forces the audio's sample rate to be reduced to a value lower than or equal to the value specified here.

This can decrease file size noticeably on certain sounds, without impacting quality depending on the actual sound's contents. See **Best practices** for more information.

### Edit > Trim

The source audio file may contain long silences at the beginning and/or the end. These silences are inserted by DAWs when saving to a waveform, which increases their size unnecessarily and add latency to the moment they are played back.

Enabling **Trim** will automatically trim the beginning and end of the audio if it's lower than -50 dB _after_ normalization (see **Edit > Normalize** below). A fade-in/fade-out period of 500 samples is also used during trimming to avoid audible pops.

### Edit > Normalize

If enabled, audio volume will be _normalized_ so that its peak volume is equal to 0 dB. When enabled, normalization will make audio sound louder depending on its original peak volume.

### Edit > Loop Mode

Unlike Ogg Vorbis and MP3, WAV files can contain metadata to indicate whether they're looping (in addition to loop points). By default, Godot will follow this metadata, but you can choose to apply a specific loop mode:

- **Detect from WAV:** Uses loop information from the WAV metadata.
- **Disabled:** Don't loop audio, even if metadata indicates the file should be played back looping.
- **Forward:** Standard audio looping. Plays the audio forward from the beginning to the loop end, then returns to the loop beginning and repeats.
- **Ping-Pong:** Plays the audio forward until the loop end, then backwards to the loop beginning, repeating this cycle.
- **Backward:** Plays the audio backwards from the loop end to the loop beginning, then repeats.

When choosing one of the **Forward**, **Ping-Pong** or **Backward** loop modes, loop points can also be defined to make only a specific part of the sound loop. **Loop Begin** is set in samples after the beginning of the audio file. **Loop End** is also set in samples after the beginning of the audio file, but will use the end of the audio file if set to `-1`.

> **Warning:** In AudioStreamPlayer, the `finished` signal won't be emitted for looping audio when it reaches the end of the audio file, as the audio will keep playing indefinitely.

### Compress > Mode

Three compression modes can be chosen from for WAV files: **PCM (Uncompressed)**, **IMA ADPCM**, or **Quite OK Audio** (default). **IMA ADPCM** reduces file size and memory usage a little, at the cost of decreasing quality in an audible manner. **Quite OK Audio** reduces file size a bit more than **IMA ADPCM** and the quality decrease is much less noticeable, at the cost of slightly higher CPU usage (still much lower than MP3).

Ogg Vorbis and MP3 don't decrease quality as much and can provide greater file size reductions, at the cost of higher CPU usage during playback. This higher CPU usage is usually not a problem (especially with MP3), unless playing dozens of compressed sounds at the same time on mobile/web platforms.

### Import options (Ogg Vorbis and MP3)

#### Loop

If enabled, the audio will begin playing at the beginning after playback ends by reaching the end of the audio.

> **Warning:** In AudioStreamPlayer, the `finished` signal won't be emitted for looping audio when it reaches the end of the audio file, as the audio will keep playing indefinitely.

#### Loop Offset

The loop offset determines where audio will start to loop after playback reaches the end of the audio. This can be used to only loop a part of the audio file, which is useful for some ambient sounds or music. The value is determined in seconds relative to the beginning of the audio, so `0` will loop the entire audio file.

Only has an effect if **Loop** is enabled.

A more convenient editor for **Loop Offset** is provided in the **Advanced import settings** dialog, as it lets you preview your changes without having to reimport the audio.

#### BPM

The Beats Per Minute of the audio track. This should match the BPM measure that was used to compose the track. This is only relevant for music that wishes to make use of interactive music functionality, not sound effects.

A more convenient editor for **BPM** is provided in the **Advanced import settings** dialog, as it lets you preview your changes without having to reimport the audio.

#### Beat Count

The beat count of the audio track. This is only relevant for music that wishes to make use of interactive music functionality, not sound effects.

A more convenient editor for **Beat Count** is provided in the **Advanced import settings** dialog, as it lets you preview your changes without having to reimport the audio.

#### Bar Beats

The number of bars within a single beat in the audio track. This is only relevant for music that wishes to make use of interactive music functionality , not sound effects.

A more convenient editor for **Bar Beats** is provided in the **Advanced import settings** dialog, as it lets you preview your changes without having to reimport the audio.

### Advanced import settings (Ogg Vorbis and MP3)

If you double-click an Ogg Vorbis or MP3 file in the FileSystem dock (or choose **Advanced…** in the Import dock), you will see a dialog appear:

This dialog allows you to edit the audio's loop point with a real-time preview, in addition to the BPM, beat count and bar beats. These 3 settings are currently unused, but they will be used in the future for interactive music support (which allows smoothly transitioning between different music tracks).

> **Note:** Unlike WAV files, Ogg Vorbis and MP3 only support a "loop begin" loop point, not a "loop end" point. Looping can also be only be standard forward looping, not ping-pong or backward.

### Best practices

#### Use appropriate quality settings

While keeping pristine-quality audio sources is important if you're performing editing, using the same quality in the exported project is not necessary. For WAV files, Godot offers several import options to reduce the final file size without modifying the source file on disk.

To reduce memory usage and file size, choose an appropriate quantization, sample rate and number of channels for your audio:

- There's no _audible_ benefit to using 24-bit audio, especially in a game where several sounds are often playing at the same time (which makes it harder to appreciate individual sounds).
- Unless you are slowing down the audio at runtime, there's no _audible_ benefit to using a sample rate greater than 48 kHz. If you wish to keep a source with a higher sample rate for editing, use the **Force > Max Rate** import option to limit the sample rate of the imported sound (only available for WAV files).
- Many sound effects can generally be converted to mono as opposed to stereo. If you wish to keep a source with stereo for editing, use the **Force > Mono** import option to convert the imported sound to mono (only available for WAV files).
- Voices can generally be converted to mono, but can also have their sample rate reduced to 22 kHz without a noticeable loss in quality (unless the voice is very high-pitched). This is because most human voices never go past 11 kHz.

#### Use real-time audio effects to reduce file size

Godot has an [extensive bus system](tutorials_audio.md) with built-in effects. This saves SFX artists the need to add reverb to the sound effects, reducing their size greatly and ensuring correct trimming.

As you can see above, sound effects become much larger in file size with reverb added.

> **See also:** Audio samples can be loaded and saved at runtime using [runtime file loading and saving](tutorials_io.md), including from an exported project.

---

## Importing images

### Supported image formats

Godot can import the following image formats:

- BMP (`.bmp`) - No support for 16-bit per pixel images. Only 1-bit, 4-bit, 8-bit, 24-bit, and 32-bit per pixel images are supported.
- DirectDraw Surface (`.dds`) - If mipmaps are present in the texture, they will be loaded directly. This can be used to achieve effects using custom mipmaps.
- Khronos Texture (`.ktx`) - Decoding is done using [libktx](https://github.com/KhronosGroup/KTX-Software). Only supports 2D images. Cubemaps, texture arrays and de-padding are not supported.
- OpenEXR (`.exr`) - Supports HDR (highly recommended for panorama skies).
- Radiance HDR (`.hdr`) - Supports HDR (highly recommended for panorama skies).
- JPEG (`.jpg`, `.jpeg`) - Doesn't support transparency per the format's limitations.
- PNG (`.png`) - Precision is limited to 8 bits per channel upon importing (no HDR images).
- Truevision Targa (`.tga`)
- SVG (`.svg`) - SVGs are rasterized using [ThorVG](https://www.thorvg.org/) when importing them. [Support is limited](https://www.thorvg.org/about#:~:text=certain%20features%20remain%20unsupported%20within%20the%20current%20framework); complex vectors may not render correctly. **Text must be converted to paths**; otherwise, it won't appear in the rasterized image. You can check whether ThorVG can render a certain vector correctly using its [web-based viewer](https://www.thorvg.org/viewer). For complex vectors, rendering them to PNGs using [Inkscape](https://inkscape.org/) is often a better solution. This can be automated thanks to its [command-line interface](https://wiki.inkscape.org/wiki/index.php/Using_the_Command_Line#Export_files).
- WebP (`.webp`) - WebP files support transparency and can be compressed lossily or losslessly. The precision is limited to 8 bits per channel.

> **Note:** If you've compiled the Godot editor from source with specific modules disabled, some formats may not be available.

### Importing textures

The default action in Godot is to import images as textures. Textures are stored in video memory. Their pixel data can't be accessed directly from the CPU without converting them back to an [Image](../godot_gdscript_resources.md) in a script. This is what makes drawing them efficient.

There are over a dozen import options that can be adjusted after selecting an image in the FileSystem dock:

#### Changing import type

It is possible to choose other types of imported resources in the Import dock:

- **BitMap:** 1-bit monochrome texture (intended to be used as a click mask in [TextureButton](../godot_gdscript_ui_controls.md) and [TouchScreenButton](../godot_gdscript_nodes_2d.md)). This resource type cannot be displayed directly onto 2D or 3D nodes, but the pixel values can be queried from a script using [get_bit](../godot_gdscript_misc.md).
- **Cubemap:** Import the texture as a 6-sided cubemap, with interpolation between the cubemap's sides (seamless cubemaps), which can be sampled in custom shaders.
- **CubemapArray:** Import the texture as a collection of 6-sided cubemaps, which can be sampled in custom shaders. This resource type can only be displayed when using the Forward+ or Mobile renderers, not the Compatibility renderer.
- **Font Data (Monospace Image Font):** Import the image as a bitmap font where all characters have the same width. See [Using Fonts](tutorials_ui.md).
- **Image:** Import the image as-is. This resource type cannot be displayed directly onto 2D or 3D nodes, but the pixel values can be queried from a script using [get_pixel](../godot_gdscript_misc.md).
- **Texture2D:** Import the image as a 2-dimensional texture, suited for display on 2D and 3D surfaces. This is the default import mode.
- **Texture2DArray:** Import the image as a collection of 2-dimensional textures. Texture2DArray is similar to a 3-dimensional texture, but without interpolation between layers. Built-in 2D and 3D shaders cannot display texture arrays, so you must create a custom shader in [2D](tutorials_shaders.md) or [3D](tutorials_shaders.md) to display a texture from a texture array.
- **Texture3D:** Import the image as a 3-dimensional texture. This is _not_ a 2D texture applied onto a 3D surface. Texture3D is similar to a texture array, but with interpolation between layers. Texture3D is typically used for [FogMaterial](../godot_gdscript_misc.md) density maps in [volumetric fog](tutorials_3d.md), [particle attractor](tutorials_3d.md) vector fields, [Environment](../godot_gdscript_rendering.md) 3D LUT color correction, and custom shaders.
- **TextureAtlas:** Import the image as an _atlas_ of different textures. Can be used to reduce memory usage for animated 2D sprites. Only supported in 2D due to missing support in built-in 3D shaders.

For **Cubemap**, the expected image order is X+, X-, Y+, Y-, Z+, Z- (in Godot's coordinate system, so Y+ is "up" and Z- is "forward"). Here are templates you can use for cubemap images (right-click > **Save Link As…**):

- 2×3 cubemap template (default layout option)
- 3×2 cubemap template
- 1×6 cubemap template
- 6×1 cubemap template

#### Detect 3D

The default import options (no mipmaps and **Lossless** compression) are suited for 2D, but are not ideal for most 3D projects. **Detect 3D** makes Godot aware of when a texture is used in a 3D scene (such as a texture in a [BaseMaterial3D](../godot_gdscript_rendering.md)). If this happens, several import options are changed so the texture flags are friendlier to 3D. Mipmaps are enabled and the compression mode is changed to **VRAM Compressed** unless **Detect 3D > Compress To** is changed. The texture is also reimported automatically.

A message is printed to the Output panel when a texture is detected to be used in 3D.

If you run into quality issues when a texture is detected to be used in 3D (e.g. for pixel art textures), change the **Detect 3D > Compress To** option before using the texture in 3D, or change **Compress > Mode** to **Lossless** after using the texture in 3D. This is preferable to disabling **Detect 3D**, as mipmap generation remains enabled to prevent textures from looking grainy at a distance.

### Import options

> **See also:** Since Godot 4.0, texture filter and repeat modes are set in the CanvasItem properties in 2D (with a project setting acting as a default), and in a [per-material configuration in 3D](tutorials_3d.md). In custom shaders, filter and repeat mode is changed on the `sampler2D` uniform using hints described in the [Shading language](tutorials_shaders.md) documentation.

#### Compress > Mode

Images are one of the largest assets in a game. To handle them efficiently, they need to be compressed. Godot offers several compression methods, depending on the use case.

- **Lossless:** This is the default and most common compression mode for 2D assets. It shows assets without any kind of artifacting, and disk compression is decent. It will use considerably more amount of video memory than VRAM Compression, though. This is also the recommended setting for pixel art.
- **Lossy:** This is a good choice for large 2D assets. It has some artifacts, but less than VRAM compression and the file size is several times lower compared to Lossless or VRAM Uncompressed. Video memory usage isn't decreased by this mode; it's the same as with Lossless or VRAM Uncompressed.
- **VRAM Compressed:** This is the default and most common compression mode for 3D assets. Size on disk is reduced and video memory usage is also decreased considerably (usually by a factor between 4 and 6). This mode should be avoided for 2D as it exhibits noticeable artifacts, especially for lower-resolution textures.
- **VRAM Uncompressed:** Only useful for formats that can't be compressed, such as raw floating-point images.
- **Basis Universal:** This alternative VRAM compression mode encodes the texture to a format that can be transcoded to most GPU-compressed formats at load-time. This provides very small files that make use of VRAM compression, at the cost of lower quality compared to VRAM Compressed and slow compression times. VRAM usage is usually the same as VRAM Compressed. Basis Universal does not support floating-point image formats (the engine will internally fall back to VRAM Compressed instead).

> **Note:** Even in 3D, "pixel art" textures should have VRAM compression disabled as it will negatively affect their appearance, without improving performance significantly due to their low resolution.

In this table, each of the 5 options are described together with their advantages and disadvantages ( = best, = worst):

| Compress mode | Lossless                      | Lossy                | VRAM Compressed                                    | VRAM Uncompressed    | Basis Universal                      |
| ------------- | ----------------------------- | -------------------- | -------------------------------------------------- | -------------------- | ------------------------------------ |
| Description   | Stored as Lossless WebP / PNG | Stored as Lossy WebP | Stored as S3TC, BPTC or ETC2 depending on platform | Stored as raw pixels | Transcoded to VRAM Compressed format |
| Size on disk  | Small                         | Very small           | Small                                              | Large                | Very small                           |
| Memory usage  | Large                         | Large                | Small                                              | Large                | Small                                |
| Performance   | Normal                        | Normal               | Fast                                               | Normal               | Fast                                 |
| Quality loss  | None                          | Slight               | Moderate                                           | None                 | Moderate                             |
| Load time     | Slow                          | Slow                 | Fast                                               | Normal               | Normal                               |

Estimated memory usage for a single RGBA8 texture with mipmaps enabled:

| Texture size | Lossless  | Lossy     | VRAM Compressed | VRAM Uncompressed | Basis Universal |
| ------------ | --------- | --------- | --------------- | ----------------- | --------------- |
| 128×128      | 85 KiB    | 85 KiB    | 21 KiB          | 85 KiB            | 21 KiB          |
| 256×256      | 341 KiB   | 341 KiB   | 85 KiB          | 341 KiB           | 85 KiB          |
| 512×512      | 1.33 MiB  | 1.33 MiB  | 341 KiB         | 1.33 MiB          | 341 KiB         |
| 1024×1024    | 5.33 MiB  | 5.33 MiB  | 1.33 MiB        | 5.33 MiB          | 1.33 MiB        |
| 2048×2048    | 21.33 MiB | 21.33 MiB | 5.33 MiB        | 21.33 MiB         | 5.33 MiB        |
| 4096×4096    | 85.33 MiB | 85.33 MiB | 21.33 MiB       | 85.33 MiB         | 21.33 MiB       |

> **Note:** In the above table, memory usage will be reduced by 25% for images that do not have an alpha channel (RGB8). Memory usage will be further decreased by 25% for images that have mipmaps disabled.

Notice how at larger resolutions, the impact of VRAM compression is much greater. With a 4:1 compression ratio (6:1 for opaque textures with S3TC), VRAM compression effectively allows a texture to be twice as large on each axis, while using the same amount of memory on the GPU.

VRAM compression also reduces the memory bandwidth required to sample the texture, which can speed up rendering in memory bandwidth-constrained scenarios (which are frequent on integrated graphics and mobile). These factors combined make VRAM compression a must-have for 3D games with high-resolution textures.

You can preview how much memory a texture takes by double-clicking it in the FileSystem dock, then looking at the Inspector:

#### Compress > High Quality

> **Note:** High-quality VRAM texture compression is only supported in the Forward+ and Mobile renderers. When using the Compatibility renderer, this option is always considered disabled.

If enabled, uses BPTC compression on desktop platforms and ASTC compression on mobile platforms. When using BPTC, BC7 is used for SDR textures and BC6H is used for HDR textures.

If disabled (default), uses the faster but lower-quality S3TC compression on desktop platforms and ETC2 on mobile/web platforms. When using S3TC, DXT1 (BC1) is used for opaque textures and DXT5 (BC3) is used for transparent or normal map (RGTC) textures.

BPTC and ASTC support VRAM compression for HDR textures, but S3TC and ETC2 do not (see **HDR Compression** below).

#### Compress > HDR Compression

> **Note:** This option only has an effect on textures that are imported as HDR formats in Godot (`.hdr` and `.exr` files).

If set to **Disabled**, never uses VRAM compression for HDR textures, regardless of whether they're opaque or transparent. Instead, the texture is converted to RGBE9995 (9-bits per channel + 5-bit exponent = 32 bits per pixel) to reduce memory usage compared to a half-float or single-precision float image format.

If set to **Opaque Only** (default), only uses VRAM compression for opaque HDR textures. This is due to a limitation of HDR formats, as there is no VRAM-compressed HDR format that supports transparency at the same time.

If set to **Always**, will force VRAM compression even for HDR textures with an alpha channel. To perform this, the alpha channel is discarded on import.

#### Compress > Normal Map

When using a texture as normal map, only the red and green channels are required. Given regular texture compression algorithms produce artifacts that don't look that nice in normal maps, the RGTC compression format is the best fit for this data. Forcing this option to **Enable** will make Godot import the image as RGTC compressed. By default, it's set to **Detect**. This means that if the texture is ever detected to be used as a normal map, it will be changed to **Enable** and reimported automatically.

Note that RGTC compression affects the resulting normal map image. You will have to adjust custom shaders that use the normal map's blue channel to take this into account. Built-in material shaders already ignore the blue channel in a normal map (regardless of the actual normal map's contents).

In the example below, the normal map with RGTC compression is able to preserve its detail much better, while using the same amount of memory as a standard RGBA VRAM-compressed texture:

> **Note:** Godot requires the normal map to use the X+, Y+ and Z+ coordinates, which is known as an OpenGL-style normal map. If you've imported a material made to be used with another engine, it may be DirectX-style. In this case, the normal map needs to be converted by enabling the **Normal Map Invert Y** import option. More information about normal maps (including a coordinate order table for popular engines) can be found [here](http://wiki.polycount.com/wiki/Normal_Map_Technical_Details).

#### Compress > Channel Pack

If set to **sRGB Friendly** (default), prevents the RG color format from being used as it does not support sRGB color.

If set to **Optimized**, allows the RG color format to be used if the texture does not use the blue channel.

A third option **Normal Map (RG Channels)** is _only_ available in layered textures ([Cubemap](../godot_gdscript_misc.md), [CubemapArray](../godot_gdscript_misc.md), [Texture2DArray](../godot_gdscript_resources.md) and [Texture3D](../godot_gdscript_resources.md)). This forces all layers from the texture to be imported with the RG color format, with only the red and green channels preserved. RGTC compression is able to preserve its detail much better, while using the same amount of memory as a standard RGBA VRAM-compressed texture. This only has an effect on textures with the **VRAM Compressed** or **Basis Universal** compression modes.

#### Mipmaps > Generate

If enabled, smaller versions of the texture are generated on import. For example, a 64×64 texture will generate 6 mipmaps (32×32, 16×16, 8×8, 4×4, 2×2, 1×1). This has several benefits:

- Textures will not become grainy in the distance (in 3D), or if scaled down due to camera zoom or CanvasItem scale (in 2D).
- Performance will improve if the texture is displayed in the distance, since sampling smaller versions of the original texture is faster and requires less memory bandwidth.

The downside of mipmaps is that they increase memory usage by roughly 33%.

It's recommended to enable mipmaps in 3D. However, in 2D, this should only be enabled if your project visibly benefits from having mipmaps enabled. If the camera never zooms out significantly, there won't be a benefit to enabling mipmaps but memory usage will increase.

#### Mipmaps > Limit

> **Warning:** **Mipmaps > Limit** is currently not implemented and has no effect when changed.

If set to a value greater than `-1`, limits the maximum number of mipmaps that can be generated. This can be decreased if you don't want textures to become too low-resolution at extreme distances, at the cost of some graininess.

#### Roughness > Mode

The color channel to consider as a roughness map in this texture. Only effective if **Roughness > Src Normal** is not empty.

#### Roughness > Src Normal

The path to the texture to consider as a normal map for roughness filtering on import. Specifying this can help decrease specular aliasing slightly in 3D.

Roughness filtering on import is only used in 3D rendering, not 2D.

#### Process > Fix Alpha Border

This puts pixels of the same surrounding color in transition from transparent to opaque areas. For textures displayed with bilinear filtering, this helps mitigate the outline effect when exporting images from an image editor.

It's recommended to leave this enabled (as it is by default), unless this causes issues for a particular image.

#### Process > Premult Alpha

An alternative to fixing darkened borders with **Fix Alpha Border** is to use premultiplied alpha. By enabling this option, the texture will be converted to this format. A premultiplied alpha texture requires specific materials to be displayed correctly:

- In 2D, a [CanvasItemMaterial](../godot_gdscript_nodes_2d.md) will need to be created and configured to use the **Premul Alpha** blend mode on CanvasItems that use this texture. In [custom canvas item shaders](tutorials_shaders.md), `render_mode blend_premul_alpha;` should be used.
- In 3D, a [BaseMaterial3D](../godot_gdscript_rendering.md) will need to be created and configured to use the **Premul Alpha** blend mode on materials that use this texture. In [custom spatial shaders](tutorials_shaders.md), `render_mode blend_premul_alpha;` should be used.

#### Process > Normal Map Invert Y

Godot requires the normal map to use the X+, Y+ and Z+ coordinates, which is known as an OpenGL-style normal map. If you've imported a material made to be used with another engine, it may be DirectX-style. In this case, the normal map needs to be converted by enabling the **Normal Map Invert Y** import option.

More information about normal maps (including a coordinate order table for popular engines) can be found [here](http://wiki.polycount.com/wiki/Normal_Map_Technical_Details).

#### Process > HDR as sRGB

Some HDR images you can find online may be broken and contain sRGB color data (instead of linear color data). It is advised not to use those files. If you absolutely have to, enabling this option on will make them look correct.

> **Warning:** Enabling **HDR as sRGB** on well-formatted HDR images will cause the resulting image to look too dark, so leave this disabled if unsure.

#### Process > HDR Clamp Exposure

Some HDR panorama images you can find online may contain extremely bright pixels, due to being taken from real life sources without any clipping.

While these HDR panorama images are accurate to real life, this can cause the radiance map generated by Godot to contain sparkles when used as a background sky. This can be seen in material reflections (even on rough materials in extreme cases). Enabling **HDR Clamp Exposure** can resolve this using a smart clamping formula that does not introduce _visible_ clipping – glow will keep working when looking at the background sky.

#### Process > Size Limit

If set to a value greater than `0`, the size of the texture is limited on import to a value smaller than or equal to the value specified here. For non-square textures, the size limit affects the longer dimension, with the shorter dimension scaled to preserve aspect ratio. Resizing is performed using cubic interpolation.

This can be used to reduce memory usage without affecting the source images, or avoid issues with textures not displaying on mobile/web platforms (as these usually can't display textures larger than 4096×4096).

#### Detect 3D > Compress To

This changes the **Compress > Mode** option that is used when a texture is detected as being used in 3D.

Changing this import option only has an effect if a texture is detected as being used in 3D. Changing this to **Disabled** then reimporting will not change the existing compress mode on a texture (if it's detected to be used in 3D), but choosing **VRAM Compressed** or **Basis Universal** will.

#### SVG > Scale

_This is only available for SVG images._

The scale the SVG should be rendered at, with `1.0` being the original design size. Higher values result in a larger image. Note that unlike font oversampling, this affects the physical size the SVG is rendered at in 2D. See also **Editor > Scale With Editor Scale** below.

#### Editor > Scale With Editor Scale

_This is only available for SVG images._

If true, scales the imported image to match the editor's display scale factor. This should be enabled for editor plugin icons and custom class icons, but should be left disabled otherwise.

#### Editor > Convert Colors With Editor Theme

_This is only available for SVG images._

If checked, converts the imported image's colors to match the editor's icon and font color palette. This assumes the image uses the exact same colors as [Godot's own color palette for editor icons](tutorials_editor.md), with the source file designed for a dark editor theme. This should be enabled for editor plugin icons and custom class icons, but should be left disabled otherwise.

### Importing SVG images with text

As the SVG library used in Godot doesn't support rasterizing text found in SVG images, text must be converted to a path first. Otherwise, text won't appear in the rasterized image.

There are two ways to achieve this in a non-destructive manner, so you can keep editing the original text afterwards:

- Select your text object in Inkscape, then duplicate it in place by pressing Ctrl + D and use **Path > Object to Path**. Hide the original text object afterwards using the **Layers and Objects** dock.
- Use the Inkscape command line to export an SVG from another SVG file with text converted to paths:

```gdscript
inkscape --export-text-to-path --export-filename svg_with_text_converted_to_path.svg svg_with_text.svg
```

### Best practices

#### Supporting high-resolution texture sizes in 2D without artifacts

To support [multiple resolutions](tutorials_rendering.md) with crisp visuals at high resolutions, you will need to use high-resolution source images (suited for the highest resolution you wish to support without blurriness, which is typically 4K in modern desktop games).

There are 2 ways to proceed:

- Use a high base resolution in the project settings (such as 4K), then use the textures at original scale. This is an easier approach.
- Use a low base resolution in the project settings (such as 1080p), then downscale textures when using them. This is often more difficult and can make various calculations in script tedious, so the approach described above is recommended instead.

After doing this, you may notice that textures become grainy at lower viewport resolutions. To resolve this, enable **Mipmaps** on textures used in 2D in the Import dock. This will increase memory usage.

Enabling mipmaps can also make textures appear blurrier, but you can choose to make textures sharper (at the cost of some graininess) by setting **Rendering > Textures > Default Filters > Texture Mipmap Bias** to a negative value.

#### Use appropriate texture sizes in 3D

While there's no "one size fits all" recommendation, here are some general recommendations for choosing texture sizes in 3D:

- The size of a texture should be adjusted to have a consistent texel density compared to surrounding objects. While this cannot be ensured perfectly when sticking to power-of-two texture sizes, it's usually possible to keep texture detail fairly consistent throughout a 3D scene.
- The smaller the object appears on screen, the smaller its texture should be. For example, a tree that only appears in the background doesn't need a texture resolution as high as other objects the player may be able to walk close to.
- Using power-of-two texture sizes is recommended, but is not required. Textures don't have to be square – sizes such as 1024×512 are acceptable.
- There are diminishing returns to using large texture sizes, despite the increased memory usage and loading times. Most modern 3D games not using a pixel art style stick to 2048×2048 textures on average, with 1024×1024 and 512×512 for textures spanning smaller surfaces.
- When working with physically-based materials in 3D, you can reduce memory usage and file size without affecting quality too much by using a lower resolution for certain texture maps. This works especially well for textures that only feature low-frequency detail (such as a normal map for a snow texture).

If you have control over how the 3D models are created, these tips are also worth exploring:

- When working with 3D models that are mostly symmetrical, you may be able to use mirrored UVs to double the effective texel density. This may look unnatural when used on human faces though.
- When working with 3D models using a low-poly style and plain colors, you can rely on vertex colors instead of textures to represent colors on the model's surfaces.

> **See also:** Images can be loaded and saved at runtime using [runtime file loading and saving](tutorials_io.md), including from an exported project.

---

## Importing translations

### Games and internationalization

The gaming community isn't monolingual or monocultural. It's made up of many different languages and cultures - just like the Godot community! If you want to allow players to experience your game in their language, one of things you'll need to provide is text translations, which Godot supports via internationalized text.

In regular desktop or mobile applications, internationalized text is usually located in resource files (or .po files for GNU stuff). Games, however, can use several orders of magnitude more text than applications, so they must support efficient methods for dealing with loads of multilingual text.

There are two approaches to generate multilingual language games and applications. Both are based on a key:value system. The first is to use one of the languages as the key (usually English), the second is to use a specific identifier. The first approach is probably easier for development if a game is released first in English, later in other languages, but a complete nightmare if working with many languages at the same time.

In general, games use the second approach and a unique ID is used for each string. This allows you to revise the text while it is being translated to other languages. The unique ID can be a number, a string, or a string with a number (it's just a unique string anyway).

### Supported formats

To complete the picture and allow efficient support for translations, Godot has a special importer that can read CSV files. Most spreadsheet editors can export to this format, so the only requirement is that the files have a special arrangement. See [Localization using spreadsheets](tutorials_i18n.md) for detailed info on formatting and importing CSVs.

If you need a more powerful file format, Godot also supports loading translations written in the gettext `.po` format. See [Localization using gettext (PO files)](tutorials_i18n.md) for details.

---

## Retargeting 3D Skeletons

### To share animations among multiple Skeletons

Godot has Position/Rotation/Scale 3D tracks (which this document calls "Transform" tracks) with Nodepaths to bones for Skeleton bone animation. This means you can't share animations between multiple Skeletons just by using the same bone names.

Godot allows each bone to have a parent-child relationship and can have rotation and scale as well as position, which means that bones that share a name can still have different Transform values.

The Skeleton stores the Transform values necessary for the default pose as Bone Rest. If Bone Pose is equal to Bone Rest, it means that the Skeleton is in the default pose.

> **Note:** Godot 3 and Godot 4 have different Bone Pose behaviors. In Godot 3, Bone Pose is relative to Bone Rest, but in Godot 4, it includes Bone Rest. See this [article](https://godotengine.org/article/animation-data-redesign-40) for more information.

Skeletal models have different Bone Rests depending on the environment from which they were exported. For example, the bones of a glTF model output from Blender have "Edit Bone Orientation" as the Bone Rest rotation. However, there are skeletal models without any Bone Rest rotations, such as the glTF model output from Maya.

To share animations in Godot, it is necessary to match Bone Rests as well as Bone Names to remove unwanted tracks in some cases. You can do that using the scene importer.

### Options for Retargeting

#### Bone Map

When you select the Skeleton3D node in the advanced scene import menu, a menu will appear on the right-hand side containing the "Retarget" section. The Retarget section has a single property `bone_map`.

With the Skeleton node selected, first set up a new [BoneMap](../godot_gdscript_misc.md) and [SkeletonProfile](../godot_gdscript_misc.md). Godot has a preset called [SkeletonProfileHumanoid](../godot_gdscript_misc.md) for humanoid models. This tutorial proceeds with the assumption that you are using [SkeletonProfileHumanoid](../godot_gdscript_misc.md).

> **Note:** If you need a profile that is different from [SkeletonProfileHumanoid](../godot_gdscript_misc.md), you can export a [SkeletonProfile](../godot_gdscript_misc.md) from the editor by selecting a Skeleton3D and using the **Skeleton3D** menu in the 3D viewport's toolbar.

When you use [SkeletonProfileHumanoid](../godot_gdscript_misc.md), auto-mapping will be performed when the [SkeletonProfile](../godot_gdscript_misc.md) is set. If the auto-mapping does not work well, you can map bones manually.

Any missing, duplicate or incorrect parent-child relationship mappings will be indicated by a magenta / red button (depending on the editor setting). It does not block the import process, but it warns that animations may not be shared correctly.

> **Note:** The auto-mapping uses pattern matching for the bone names. So we recommend to use common English names for bones.

After you set up the `bone_map`, several options are available in the sections below.

#### Remove Tracks

If you import resources as an [AnimationLibrary](../godot_gdscript_resources.md) that will be shared, we recommend to enable these options. However, if you import resources as scenes, these should be disabled in some cases. For example, if you import a character with animated accessories, these options may cause the accessories to not animate.

##### Except Bone Transform

Removes any tracks except the bone Transform track from the animations.

##### Unimportant Positions

Removes Position tracks other than `root_bone` and `scale_base_bone` defined in [SkeletonProfile](../godot_gdscript_misc.md) from the animations. In [SkeletonProfileHumanoid](../godot_gdscript_misc.md), this means that to remove Position tracks other than "Root" and "Hips". Since Godot 4, animations include Bone Rest in the Transform value. If you disable this option, the animation may change the body shape unpredictably.

##### Unmapped Bones

Removes unmapped bone Transform tracks from the animations.

#### Bone Renamer

##### Rename Bones

Rename the mapped bones.

##### Unique Node

Makes Skeleton a unique node with the name specified in the `skeleton_name`. This allows the animation track paths to be unified independent of the scene hierarchy.

#### Rest Fixer

Reference poses defined in [SkeletonProfileHumanoid](../godot_gdscript_misc.md) have the following rules:

- The humanoid is T-pose
- The humanoid is facing +Z in the Right-Handed Y-UP Coordinate System
- The humanoid should not have a Transform as Node
- Directs the +Y axis from the parent joint to the child joint
- +X rotation bends the joint like a muscle contracting

These rules are convenient definitions for blend animation and Inverse Kinematics (IK). If your model does not match this definition, you need to fix it with these options.

##### Apply Node Transform

If the asset is not exported correctly for sharing, the imported Skeleton may have a Transform as a Node. For example, a glTF exported from Blender with no "Apply Transform" executed is one such case. It looks like the model matches the definition, but the internal Transforms are different from the definition. This option fixes such models by applying Transforms on import.

> **Note:** If the imported scene contains objects other than Skeletons, this option may have a negative effect.

##### Normalize Position Tracks

Position track is used mostly for model movement, but sharing the moving animation between models with different heights may cause the appearance of slipping due to the difference in stride length. This option normalizes the Position track values based on the `scale_base_bone` height. The `scale_base_bone` height is stored in the Skeleton as the `motion_scale`, and the normalized Position track values is multiplied by that value on playback. If this option is disabled, the Position tracks is not normalized and the Skeleton's `motion_scale` is always imported as `1.0`.

With [SkeletonProfileHumanoid](../godot_gdscript_misc.md), `scale_base_bone` is "Hips", therefore the Hips' height is used as the `motion_scale`.

##### Overwrite Axis

Unifies the models' Bone Rests by overwriting it to match the reference poses defined in the [SkeletonProfile](../godot_gdscript_misc.md).

> **Note:** This is the most important option for sharing animations in Godot 4, but be aware that this option can produce horrible results **if the original Bone Rest set externally is important**. If you want to share animations with keeping the original Bone Rest, consider to use the [Realtime Retarget Module](https://github.com/TokageItLab/realtime_retarget).

##### Fix Silhouette

Attempts to make the model's silhouette match that of the reference poses defined in the [SkeletonProfile](../godot_gdscript_misc.md), such as T-Pose. This cannot fix silhouettes which are too different, and it may not work for fixing bone roll.

With [SkeletonProfileHumanoid](../godot_gdscript_misc.md), this option does not need to be enabled for T-pose models, but should be enabled for A-pose models. However in that case, the fixed foot results may be bad depending on the heel height of the model, so it may be necessary to add the [SkeletonProfile](../godot_gdscript_misc.md) bone names you do not want fixed in the `filter` array, as in the below example.

Also, for models with bent knees or feet, it may be necessary to adjust the `scale_base_bone` height. For that, you can use `base_height_adjustment` option.

---
