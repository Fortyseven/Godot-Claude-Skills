# Godot 4 C# Tutorials — Ui (Part 3)

> 3 tutorials. C#-specific code examples.

## Introduction to GUI skinning

It is essential for a game to provide clear, informative, and yet visually pleasing user interface to its players. While [Control](../godot_csharp_ui_controls.md) nodes come with a decently functional look out of the box, there is always room for uniqueness and case-specific tuning. For this purpose Godot engine includes a system for GUI skinning (or theming), which allows you to customize the look of every control in your user interface, including your custom controls.

Here is an example of this system in action — a game with the GUI that is radically different from the default UI theme of the engine:

Beyond achieving a unique look for your game, this system also enables developers to provide customization options to the end users, including accessibility settings. UI themes are applied in a cascading manner (i.e. they propagate from parent controls to their children), which means that font settings or adjustments for colorblind users can be applied in a single place and affect the entire UI tree. Of course this system can also be used for gameplay purposes: your hero-based game can change its style for the selected player character, or you can give different flavors to the sides in your team-based project.

### Basics of themes

The skinning system is driven by the [Theme](../godot_csharp_resources.md) resource. Every Godot project has an inherent default theme that contains the settings used by the built-in control nodes. This is what gives the controls their distinct look out of the box. A theme only describes the configuration, however, and it is still the job of each individual control to use that configuration in the way it requires to display itself. This is important to remember when implementing your own custom controls.

> **Note:** Even the Godot editor itself relies on the default theme. But it doesn't look the same as a Godot project, because it applies its own heavily customized theme on top of the default one. In principle, this works exactly like it would in your game as explained **below**.

#### Theme items

The configuration that is stored in a theme consists of theme items. Each item has a unique name and must be one of the following data types:

- **Color**

A [color](../godot_csharp_misc.md) value, which is often used for fonts and backgrounds. Colors can also be used for modulation of controls and icons.

- **Constant**

An integer value, which can be used either for numeric properties of controls (such as the item separation in a [BoxContainer](../godot_csharp_ui_controls.md)), or for boolean flags (such as the drawing of relationship lines in a [Tree](../godot_csharp_ui_controls.md)).

- **Font**

A [font](../godot_csharp_misc.md) resource, which is used by controls that display text. Fonts contain most text rendering settings, except for its size and color. On top of that, alignment and text direction are controlled by individual controls.

- **Font size**

An integer value, which is used alongside a font to determine the size at which the text should be displayed.

- **Icon**

A [texture](../godot_csharp_misc.md) resource, which is normally used to display an icon (on a [Button](../godot_csharp_ui_controls.md), for example).

- **StyleBox**

A [StyleBox](../godot_csharp_resources.md) resource, a collection of configuration options which define the way a UI panel should be displayed. This is not limited to the [Panel](../godot_csharp_ui_controls.md) control, as styleboxes are used by many controls for their backgrounds and overlays.

Different controls will apply StyleBoxes in a different manner. Most notably, `focus` styleboxes are drawn as an _overlay_ to other styleboxes (such as `normal` or `pressed`) to allow the base stylebox to remain visible. This means the focus stylebox should be designed as an outline or translucent box, so that its background can remain visible.

#### Theme types

To help with the organization of its items each theme is separated into types, and each item must belong to a single type. In other words, each theme item is defined by its name, its data type and its theme type. This combination must be unique within the theme. For example, there cannot be two color items named `font_color` in a type called `Label`, but there can be another `font_color` item in a type `LineEdit`.

The default Godot theme comes with multiple theme types already defined, one for every built-in control node that uses UI skinning. The example above contains actual theme items present in the default theme. You can refer to the **Theme Properties** section in the class reference for each control to see which items are available to it and its child classes.

> **Note:** Child classes can use theme items defined for their parent class (`Button` and its derivatives being a good example of that). In fact, every control can use every theme item of any theme type, if it needs to (but for the clarity and predictability we try to avoid that in the engine). It is important to remember that for child classes that process is automated. Whenever a built-in control requests a theme item from the theme it can omit the theme type, and its class name will be used instead. On top of that, the class names of its parent classes will also be used in turn. This allows changes to the parent class, such as `Button`, to affect all derived classes without the need to customize every one of them.

You can also define your own theme types, and additionally customize both built-in controls and your own controls. Because built-in controls have no knowledge of your custom theme types, you must utilize scripts to access those items. All control nodes have several methods that allow you to fetch theme items from the theme that is applied to them. Those methods accept the theme type as one of the arguments.

```csharp
Color accentColor = GetThemeColor("accent_color", "MyType");
label.AddThemeColorOverride("font_color", accentColor);
```

To give more customization opportunities types can also be linked together as type variations. This is another use-case for custom theme types. For example, a theme can contain a type `Header` which can be marked as a variation of the base `Label` type. An individual `Label` control can then be set to use the `Header` variation for its type, and every time a theme item is requested from a theme this variation will be used before any other type. This allows to store various presets of theme items for the same class of the control node in the single `Theme` resource.

> **Warning:** Only variations available from the default theme or defined in the custom project theme are shown in the Inspector dock as options. You can still input manually the name of a variation that is defined outside of those two places, but it is recommended to keep all variations to the project theme.

You can learn more about creating and using theme type variations in a dedicated article.

### Customizing a control

Each control node can be customized directly without the use of themes. This is called local overrides. Every theme property from the control's class reference can be overridden directly on the control itself, using either the Inspector dock, or scripts. This allows to make granular changes to a particular part of the UI, while not affecting anything else in the project, including this control's children.

Local overrides are less useful for the visual flair of your user interface, especially if you aim for consistency. However, for layout nodes these are essential. Nodes such as [BoxContainer](../godot_csharp_ui_controls.md) and [GridContainer](../godot_csharp_ui_controls.md) use theme constants for defining separation between their children, and [MarginContainer](../godot_csharp_ui_controls.md) stores its customizable margins in its theme items.

Whenever a control has a local theme item override, this is the value that it uses. Values provided by the theme are ignored.

### Customizing a project

Out of the box each project adopts the default project theme provided by Godot. The default theme itself is constant and cannot be changed, but its items can be overridden with a custom theme. Custom themes can be applied in two ways: as a project setting, and as a node property throughout the tree of control nodes.

There are two project settings that can be adjusted to affect your entire project: [GUI > Theme > Custom](../godot_csharp_misc.md) allows you to set a custom project-wide theme, and [GUI > Theme > Custom Font](../godot_csharp_misc.md) does the same to the default fallback font. When a theme item is requested by a control node the custom project theme, if present, is checked first. Only if it doesn't have the item the default theme is checked.

This allows you to configure the default look of every Godot control with a single theme resource, but you can go more granular than that. Every control node also has a [theme](../godot_csharp_misc.md) property, which allows you to set a custom theme for the branch of nodes starting with that control. This means that the control and all of its children, and their children in turn, would first check that custom theme resource before falling back on the project and the default themes.

> **Note:** Instead of changing the project setting you can set the custom theme resource to the root-most control node of your entire UI branch to almost the same effect. While in the running project it will behave as expected, individual scenes will still display using the default theme when previewing or running them directly. To fix that you can set the same theme resource to the root control of each individual scene.

For example, you can have a certain style for buttons in your project theme, but want a different look for buttons inside of a popup dialog. You can set a custom theme resource to the root control of your popup and define a different style for buttons within that resource. As long as the chain of control nodes between the root of the popup and the buttons is uninterrupted, those buttons will use the styles defined in the theme resource that is closest to them. All other controls will still be styled using the project-wide theme and the default theme styles.

To sum it up, for an arbitrary control its theme item lookup would look something like this:

1. Check for local overrides of the same data type and name.
2. Using control's type variation, class name and parent class names:

3. Check every control starting from itself and see if it has a theme property set;
4. If it does, check that theme for the matching item of the same name, data and theme type;
5. If there is no custom theme or it doesn't have the item, move to the parent control;
6. Repeat steps a-c. until the root of the tree is reached, or a non-control node is reached.
7. Using control's type variation, class name and parent class names check the project-wide theme, if it's present.
8. Using control's type variation, class name and parent class names check the default theme.

Even if the item doesn't exist in any theme, a corresponding default value for that data type will be returned.

### Beyond controls

Naturally, themes are an ideal type of resource for storing configuration for something visual. While the support for theming is built into control nodes, other nodes can use them as well, just like any other resource.

An example of using themes for something beyond controls can be a modulation of sprites for the same units on different teams in a strategy game. A theme resource can define a collection of colors, and sprites (with a help from scripts) can use those colors to draw the texture. The main benefit being that you could make different themes using the same theme items for red, blue, and green teams, and swap them with a single resource change.

---

## Theme type variations

When designing a user interface there may be times when a [Control](../godot_csharp_ui_controls.md) node needs to have a different look than what is normally defined by a [Theme](../godot_csharp_resources.md). Every control node has theme property overrides, which allow you to redefine the styling for each individual UI element.

This approach quickly becomes hard to manage, if you need to share the same custom look between several controls. Imagine that you use gray, blue, and red variants of [Button](../godot_csharp_ui_controls.md) throughout your project. Setting it up every time you add a new button element to your interface is a tedious task.

To help with the organization and to better utilize the power of themes you can use theme type variations. These work like normal theme types, but instead of being self-sufficient and standalone they extend another, base type.

Following the previous example, your theme can have some styles, colors, and fonts defined for the `Button` type, customizing the looks of every button element in your UI. To then have a gray, red, or blue button you would create a new type, e.g. `GrayButton`, and mark it as a variation of the base `Button` type.

Type variations can replace some aspects of the base type, but keep others. They can also define properties that the base style hasn't defined. For example, your `GrayButton` can override the `normal` style from the base `Button` and add `font_color` that `Button` has never defined. The control will use a combination of both types giving priority to the type variation.

> **Note:** The way controls resolve what theme items they use from each type and each theme is better described in the Customizing a project section of the "Introduction to GUI skinning" article.

### Creating a type variation

To create a type variation open the theme editor, then click the plus icon next to the **Type** dropdown on the right side of the editor. Type in what you want to name your theme type variation in the text box, then click **Add Type**.

Below the **Type** dropdown are the property tabs. Switch to the tab with a wrench and screwdriver icon.

Click on the plus icon next to the **Base Type** field. You can select the base type there, which would typically be the name of a control node class (e.g., `Button`, `Label`, etc). Type variations can also chain and extend other type variations. This works in the same way control nodes inherit styling of their base class. For example, `CheckButton` inherits styles from `Button` because corresponding node types extend each other.

After you select the base type, you should now be able to see its properties on the other tabs in the theme editor. You can edit them as usual.

### Using a type variation

Now that a type variation has been created you can apply it to your nodes. In the inspector dock, under the **Theme** property of a control node, you can find the **Theme Type Variation** property. It is empty by default, which means that only the base type has an effect on this node.

You can either select a type variation from a dropdown list, or input its name manually. Variations appear on the list only if the type variation belongs to the project-wide theme, which you can configure in the project settings. For any other case you have to input the name of the variation manually. Click on the pencil icon to the right. Then type in the name of the type variation and click the check mark icon or press enter. If a type variation with that name exists it will now be used by the node.

---

## Using Fonts

Godot allows you to set specific fonts for different UI nodes.

There are three different places where you can setup font usage. The first is the theme editor. Choose the node you want to set the font for and select the font tab. The second is in the inspector for control nodes under **Theme Overrides > Fonts**. Lastly, in the inspector settings for themes under **Default Font**.

If no font override is specified anywhere, [Open Sans](https://fonts.google.com/specimen/Open+Sans) SemiBold is used as the default project font.

> **Note:** Since Godot 4.0, font sizes are no longer defined in the font itself but are instead defined in the node that uses the font. This is done in the **Theme Overrides > Font Sizes** section of the inspector. This allows changing the font size without having to duplicate the font resource for every different font size.

There are 2 kinds of font files: _dynamic_ (TTF/OTF/WOFF/WOFF2 formats) and _bitmap_ (BMFont `.fnt` format or monospaced image). Dynamic fonts are the most commonly used option, as they can be resized and still look crisp at higher sizes. Thanks to their vector-based nature, they can also contain a lot more glyphs while keeping a reasonable file size compared to bitmap fonts. Dynamic fonts also support some advanced features that bitmap fonts cannot support, such as _ligatures_ (several characters transforming into a single different design).

> **Tip:** You can find freely licensed font files on websites such as [Google Fonts](https://fonts.google.com/) and [Font Library](https://fontlibrary.org/). Fonts are covered by copyright. Double-check the license of a font before using it, as not all fonts allow commercial use without purchasing a license.

> **See also:** You can see how fonts work in action using the [BiDI and Font Features demo project](https://github.com/godotengine/godot-demo-projects/tree/master/gui/bidi_and_font_features).

### Dynamic fonts

Godot supports the following dynamic font formats:

- TrueType Font or Collection (`.ttf`, `.ttc`)
- OpenType Font or Collection (`.otf`, `.otc`)
- Web Open Font Format 1 (`.woff`)
- Web Open Font Format 2 (`.woff2`)

While `.woff` and especially `.woff2` tend to result in smaller file sizes, there is no universally "better" font format. In most situations, it's recommended to use the font format that was shipped on the font developer's website.

### Bitmap fonts

Godot supports the BMFont (`.fnt`) bitmap font format. This is a format created by the [BMFont](https://www.angelcode.com/products/bmfont/) program. Many BMFont-compatible programs also exist, like [BMGlyph](https://www.bmglyph.com/) or web-based [fontcutter](https://github.com/fabienbk/fontcutter).

Alternatively, you can import any image to be used as a bitmap font. To do so, select the image in the FileSystem dock, go to the Import dock, change its import type to **Font Data (Image Font)** then click **Reimport**:

The font's character set layout can be in any order, but orders that match standard Unicode are recommended as they'll require far less configuration to import. For example, the bitmap font below contains [ASCII](https://en.wikipedia.org/wiki/ASCII) characters and follows standard ASCII ordering:

The following import options can be used to import the above font image successfully:

The **Character Ranges** option is an array that maps each position on the image (in tile coordinates, not pixels). The font atlas is traversed from left to right and top to bottom. Characters can be specified with decimal numbers (`127`), hexadecimal numbers (`0x007f`) or between _single_ quotes (`'~'`). Ranges can be specified with a hyphen between characters.

For instance, `0-127` (or `0x0000-0x007f`) denotes the full ASCII range. As another example, `' '-'~'` is equivalent to `32-127` and denotes the range of _printable_ (visible) ASCII characters.

Make sure the **Character Ranges** option doesn't exceed the number of **Columns** × **Rows** defined. Otherwise, the font will fail to import.

If your font image contains margins not used for font glyphs (such as attribution information), try adjusting **Image Margin**. This is a margin applied only once around the whole image.

If your font image contains guides (in the form of lines between glyphs) or if spacing between characters appears incorrect, try adjusting **Character Margin**. This margin is applied for every imported glyph.

If you need finer control over character spacing than what the **Character Margin** options provide, you have more options.

For one, **Character Ranges** supports 3 additional arguments after the specified range of characters. These additional arguments control their positioning and spacing. They represent space advance, X axis offset, and Y axis offset in that order. They will change the space advance and offset of each character by the amount of pixels written. Space advance is most useful if, for example, your lowercase letters are thinner than your uppercase letters.

Secondly, you can also set up **Kerning Pairs** for individual characters. Specify your kerning pair by typing two sets of characters separated by a space, then followed by another space, a number to specify how many extra/less pixels to space those two sets of characters when placed next to each other.

If needed, your kerning pair characters can be specified by Unicode character code by entering `\uXXXX` where XXXX is the hexadecimal value of the Unicode character.

### Loading a font file

To load a font file (dynamic or bitmap), use the resource dropdown's **Quick Load** or **Load** option next to a font property, then navigate to the font file in question:

You can also drag-and-drop a font file from the FileSystem dock to the inspector property that accepts a Font resource.

> **Warning:** In Godot 4.0 and later, texture filter and repeat properties are defined in the location where the texture is used, rather than on the texture itself. This also applies to fonts (both dynamic fonts and bitmap fonts). Fonts that have a pixel art appearance should have bilinear filtering disabled by changing the **Rendering > Textures > Canvas Textures > Default Texture Filter** project setting to **Nearest**. The font size must also be an integer multiple of the design size (which varies on a per-font basis), and the Control node using the font must be scaled by an integer multiple as well. Otherwise, the font may look blurry. Font sizes in Godot are specified in pixels (px), not points (pt). Keep this in mind when comparing font sizes across different software. The texture filter mode can also be set on individual nodes that inherit from CanvasItem by setting [CanvasItem.texture_filter](../godot_csharp_nodes_2d.md).

### Font outlines and shadows

Font outlines and shadows can be used to improve readability when the background color isn't known in advance. For instance, this is the case for HUD elements that are drawn over a 2D/3D scene.

Font outlines are available in most nodes that derive from Control, in addition to [Label3D](../godot_csharp_misc.md).

To enable outline for a font on a given node, configure the theme overrides **Font Outline Color** and **Outline Size** in the inspector. The result should look like this:

> **Note:** If using a font with MSDF rendering, its **MSDF Pixel Range** import option be set to at least _twice_ the value of the outline size for outline rendering to look correct. Otherwise, the outline may appear to be cut off earlier than intended.

Support for font shadows is more limited: they are only available in [Label](../godot_csharp_ui_controls.md) and [RichTextLabel](../godot_csharp_ui_controls.md). Additionally, font shadows always have a hard edge (but you can reduce their opacity to make them look more subtle). To enable font shadows on a given node, configure the **Font Shadow Color**, **Shadow Offset X**, and **Shadow Offset Y** theme overrides in a Label or RichTextLabel node accordingly:

The result should look like this:

> **Tip:** You can create local overrides to font display in Label nodes by creating a [LabelSettings](../godot_csharp_misc.md) resource that you reuse across Label nodes. This resource takes priority over theme properties.

### Advanced font features

#### Antialiasing

You can adjust how the font should be smoothed out when rendering by adjusting _antialiasing_ and _hinting_. These are different properties, with different use cases.

Antialiasing controls how glyph edges should be smoothed out when rasterizing the font. The default antialiasing method (**Grayscale**) works well on every display technology. However, at small sizes, grayscale antialiasing may result in fonts looking blurry.

The antialiasing sharpness can be improved by using LCD subpixel optimization, which exploits the subpixel patterns of most LCD displays by offsetting the font antialiasing on a per-channel basis (red/green/blue). The downside is that this can introduce "fringing" on edges, especially on display technologies that don't use standard RGB subpixels (such as OLED displays).

In most games, it's recommended to stick to the default **Grayscale** antialiasing. For non-game applications, LCD subpixel optimization is worth exploring.

> **Note:** Antialiasing cannot be changed on **MSDF-rendered fonts** – these are always rendered with grayscale antialiasing.

#### Hinting

Hinting controls how aggressively glyph edges should be snapped to pixels when rasterizing the font. **None** results in the smoothest appearance, which can make the font look blurry at small sizes. **Light** (default) is sharper by snapping glyph edges to pixels on the Y axis only, while **Full** is even sharper by snapping glyph edges to pixels on both X and Y axes. Depending on personal preference, you may prefer using one hinting mode over the other.

> **Note:** If changing the hinting mode has no visible effect after clicking **Reimport**, it's usually because the font doesn't include hinting instructions. This can be resolved by looking for a version of the font file that includes hinting instructions, or enabling **Force Autohinter** in the Import dock. This will use [FreeType](https://freetype.org/)'s autohinter to automatically add hinting instructions to the imported font.

#### Subpixel positioning

Subpixel positioning can be adjusted. This is a [FreeType](https://freetype.org/) feature that allows glyphs to be rendered more closely to their intended form. The default setting of **Auto** automatically enables subpixel positioning at small sizes, but disables it at large font sizes to improve rasterization performance.

You can force the subpixel positioning mode to **Disabled**, **One half of a pixel** or **One quarter of a pixel**. **One quarter of a pixel** provides the best quality, at the cost of longer rasterization times.

Changing antialiasing, hinting and subpixel positioning has the most visible effect at smaller font sizes.

> **Warning:** Fonts that have a pixel art appearance should have their subpixel positioning mode set to **Disabled**. Otherwise, the font may appear to have uneven pixel sizes. This step is not required for bitmap fonts, as subpixel positioning is only relevant for dynamic fonts (which are usually made of vector elements).

#### Mipmaps

By default, fonts do not have mipmaps generated to reduce memory usage and speed up rasterization. However, this can cause downscaled fonts to become grainy. This can be especially noticeable with [3D text](tutorials_3d.md) that doesn't have **Fixed Size** enabled. This can also occur when displaying text with a traditional rasterized (non-**MSDF**) font in a Control node that has its scale lower than `(1, 1)`.

After selecting a font in the FileSystem dock, you can enable the **Mipmaps** in the Import dock to improve downscaled font rendering appearance.

Mipmaps can be enabled on MSDF fonts as well. This can improve font rendering quality a little at smaller-than-default sizes, but MSDF fonts are already resistant to graininess out of the box.

#### MSDF font rendering

Multi-channel signed distance field (MSDF) font rendering allows rendering fonts at any size, without having to re-rasterize them when their size changes.

MSDF font rendering has 2 upsides over traditional font rasterization, which Godot uses by default:

- The font will always look crisp, even at huge sizes.
- There is less stuttering when rendering characters _at large font sizes_ for the first time, as there is no rasterization performed.

The downsides of MSDF font rendering are:

- Higher baseline cost for font rendering. This is usually not noticeable on desktop platforms, but it can have an impact on low-end mobile devices.
- Fonts at small sizes will not look as clear as rasterized fonts, due to the lack of hinting.
- Rendering new glyphs for the first time _at small font sizes_ may be more expensive compared to traditional rasterized fonts. **Font prerendering** can be used to alleviate this.
- LCD subpixel optimization cannot be enabled for MSDF fonts.
- Fonts with self-intersecting outlines will not render correctly in MSDF mode. If you notice rendering issues on fonts downloaded from websites such as [Google Fonts](https://fonts.google.com), try downloading the font from the font author's official website instead.

To enable MSDF rendering for a given font, select it in the FileSystem dock, go to the Import dock, enable **Multichannel Signed Distance Field**, then click **Reimport**:

#### Using emoji

Godot has limited support for emoji fonts:

- CBDT/CBLC (embedded PNGs) and SVG emoji fonts are supported.
- COLR/CPAL emoji fonts (custom vector format) are **not** supported.
- EMJC bitmap image compression (used by iOS' system emoji font) is **not** supported. This means that to support emoji on iOS, you must use a custom font that uses SVG or PNG bitmap compression instead.

For Godot to be able to display emoji, the font used (or one of its **fallbacks**) needs to include them. Otherwise, emoji won't be displayed and placeholder "tofu" characters will appear instead:

After adding a font to display emoji such as [Noto Color Emoji](https://fonts.google.com/noto/specimen/Noto+Color+Emoji), you get the expected result:

To use a regular font alongside emoji, it's recommended to specify a **fallback font** that points to the emoji font in the regular font's advanced import options. If you wish to use the default project font while displaying emoji, leave the **Base Font** property in FontVariation empty while adding a font fallback pointing to the emoji font:

> **Tip:** Emoji fonts are quite large in size, so you may want to **load a system font** to provide emoji glyphs rather than bundling it with your project. This allows providing full emoji support in your project without increasing the size of its exported PCK. The downside is that emoji will look different depending on the platform, and loading system fonts is not supported on all platforms. It's possible to use a system font as a fallback font too.

#### Using icon fonts

Tools like [Fontello](https://fontello.com/) can be used to generate font files containing vectors imported from SVG files. This can be used to render custom vector elements as part of your text, or to create extruded 3D icons with [3D text](tutorials_3d.md) and TextMesh.

> **Note:** Fontello currently does not support creating multicolored fonts (which Godot can render). As of November 2022, support for multicolored fonts in icon font generation tools remains scarce.

Depending on your use cases, this may lead to better results compared to using the `img` tag in RichTextLabel. Unlike bitmap images (including SVGs which are rasterized on import by Godot), true vector data can be resized to any size without losing quality.

After downloading the generated font file, load it in your Godot project then specify it as a custom font for a Label, RichTextLabel or Label3D node. Switch over to the Fontello web interface, then copy the character by selecting it then pressing Ctrl + C (Cmd + C on macOS). Paste the character in the **Text** property of your Label node. The character will appear as a placeholder glyph in the inspector, but it should appear correctly in the 2D/3D viewport.

To use an icon font alongside a traditional font in the same Control, you can specify the icon font as a **fallback**. This works because icon fonts use the Unicode _private use area_, which is reserved for use by custom fonts and doesn't contain standard glyphs by design.

> **Note:** Several modern icon fonts such as [Font Awesome 6](https://fontawesome.com/download) have a desktop variant that uses _ligatures_ to specify icons. This allows you to specify icons by entering their name directly in the **Text** property of any node that can display fonts. Once the icon's name is fully entered as text (such as `house`), it will be replaced by the icon. While easier to use, this approach cannot be used with font fallbacks as the main font's characters will take priority over the fallback font's ligatures.

#### Font fallbacks

Godot supports defining one or more fallbacks when the main font lacks a glyph to be displayed. There are 2 main use cases for defining font fallbacks:

- Use a font that only supports Latin character sets, but use another font to be able to display text another character set such as Cyrillic.
- Use a font to render text, and another font to render emoji or icons.

Open the Advanced Import Settings dialog by double-clicking the font file in the FileSystem dock. You can also select the font in the FileSystem dock, go to the Import dock then choose **Advanced…** at the bottom:

In the dialog that appears, look for **Fallbacks** section on the sidebar on the right, click the **Array[Font] (size 0)** text to expand the property, then click **Add Element**:

Click the dropdown arrow on the new element, then choose a font file using the **Quick Load** or **Load** options:

It is possible to add fallback fonts while using the default project font. To do so, leave the **Base Font** property empty while adding one or more font fallbacks.

> **Note:** Font fallbacks can also be defined on a local basis similar to **OpenType font features**, but this is not covered here for brevity reasons.

#### Variable fonts

Godot has full support for [variable fonts](https://variablefonts.io/), which allow you to use a single font file to represent various font weights and styles (regular, bold, italic, …). This must be supported by the font file you're using.

To use a variable font, create a [FontVariation](../godot_csharp_resources.md) resource in the location where you intend to use the font, then load a font file within the FontVariation resource:

Scroll down to the FontVariation's **Variation** section, then click the **Variation Coordinates** text to expand the list of axes that can be adjusted:

The set of axes you can adjust depends on the font loaded. Some variable fonts only support one axis of adjustment (typically _weight_ or _slant_), while others may support multiple axes of adjustment.

For example, here's the [Inter V](https://rsms.me/inter/) font with a _weight_ of `900` and a _slant_ of `-10`:

> | **Tip:** While variable font axis names and scales aren't standardized, some common conventions are usually followed by font designers. The _weight_ axis is standardized in OpenType to work as follows: | Axis value                | Effective font weight |
> | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------- | --------------------- |
> | 100                                                                                                                                                                                                       | Thin (Hairline)           |
> | 200                                                                                                                                                                                                       | Extra Light (Ultra Light) |
> | 300                                                                                                                                                                                                       | Light                     |
> | 400                                                                                                                                                                                                       | Regular (Normal)          |
> | 500                                                                                                                                                                                                       | Medium                    |
> | 600                                                                                                                                                                                                       | Semi-Bold (Demi-Bold)     |
> | 700                                                                                                                                                                                                       | Bold                      |
> | 800                                                                                                                                                                                                       | Extra Bold (Ultra Bold)   |
> | 900                                                                                                                                                                                                       | Black (Heavy)             |
> | 950                                                                                                                                                                                                       | Extra Black (Ultra Black) |

You can save the FontVariation to a `.tres` resource file to reuse it in other places:

#### Faux bold and italic

When writing text in bold or italic, using font variants specifically designed for this looks better. Spacing between glyphs will be more consistent when using a bold font, and certain glyphs' shapes may change entirely in italic variants (compare "a" and _"a"_).

However, real bold and italic fonts require shipping more font files, which increases distribution size. A single **variable font** file can also be used, but this file will be larger than a single non-variable font. While file size is usually not an issue for desktop projects, it can be a concern for mobile/web projects that strive to keep distribution size as low as possible.

To allow bold and italic fonts to be displayed without having to ship additional fonts (or use a variable font that is larger in size), Godot supports _faux_ bold and italic.

Faux bold and italic is automatically used in [RichTextLabel](../godot_csharp_ui_controls.md)'s bold and italic tags if no custom fonts are provided for bold and/or italic.

To use faux bold, create a FontVariation resource in a property where a Font resource is expected. Set **Variation > Embolden** to a positive value to make a font bolder, or to a negative value to make it less bold. Recommended values are between `0.5` and `1.2` depending on the font.

Faux italic is created by skewing the text, which is done by modifying the per-character transform. This is also provided in FontVariation using the **Variation > Transform** property. Setting the `yx` component of the character transform to a positive value will italicize the text. Recommended values are between `0.2` and `0.4` depending on the font.

#### Adjusting font spacing

For stylistic purposes or for better readability, you may want to adjust how a font is presented in Godot.

Create a FontVariation resource in a property where a Font resource is expected. There are 4 properties available in the **Variation > Extra Spacing** section, which accept positive and negative values:

- **Glyph:** Additional spacing between every glyph.
- **Space:** Additional spacing between words.
- **Top:** Additional spacing above glyphs. This is used for multiline text, but also to calculate the minimum size of controls such as [Label](../godot_csharp_ui_controls.md) and [Button](../godot_csharp_ui_controls.md).
- **Bottom:** Additional spacing below glyphs. This is used for multiline text, but also to calculate the minimum size of controls such as [Label](../godot_csharp_ui_controls.md) and [Button](../godot_csharp_ui_controls.md).

The **Variation > Transform** property can also be adjusted to stretch characters horizontally or vertically. This is specifically done by adjusting the `xx` (horizontal scale) and `yy` (vertical scale) components. Remember to adjust glyph spacing to account for any changes, as glyph transform doesn't affect how much space each glyph takes in the text. Non-uniform scaling of this kind should be used sparingly, as fonts are generally not designed to be displayed with stretching.

#### OpenType font features

Godot supports enabling OpenType font features, which are a standardized way to define alternate characters that can be toggled without having to swap font files entirely. Despite being named OpenType font features, these are also supported in TrueType (`.ttf`) and WOFF/WOFF2 font files.

Support for OpenType features highly depends on the font used. Some fonts don't support any OpenType features, while other fonts can support dozens of toggleable features.

There are 2 ways to use OpenType font features:

**Globally on a font file**

Open the Advanced Import Settings dialog by double-clicking the font file in the FileSystem dock. You can also select the font in the FileSystem dock, go to the Import dock then choose **Advanced…** at the bottom:

In the dialog that appears, look for the **Metadata Overrides > OpenType Features** section on the sidebar on the right, click the **Features (0 of N set)** text to expand the property, then click **Add Feature**:

**In a specific font usage (FontVariation)**

To use a font feature, create a FontVariation resource like you would do for a **variable font**, then load a font file within the FontVariation resource:

Scroll down to the FontVariation's **OpenType Features** section, click the **Features (0 of N set)** text to expand the property, then click **Add Feature** and select the desired feature in the dropdown:

For example, here's the [Inter](https://rsms.me/inter/) font without the _Slashed Zero_ feature (top), then with the _Slashed Zero_ OpenType feature enabled (bottom):

You can disable ligatures and/or kerning for a specific font by adding OpenType features, then unchecking them in the inspector:

#### System fonts

> **Warning:** Loading system fonts is only supported on Windows, macOS, Linux, Android and iOS. However, loading system fonts on Android is unreliable as there is no official API for doing so. Godot has to rely on parsing system configuration files, which can be modified by third-party Android vendors. This may result in non-functional system font loading.

System fonts are a different type of resource compared to imported fonts. They are never actually imported into the project, but are loaded at runtime. This has 2 benefits:

- The fonts are not included within the exported PCK file, leading to a smaller file size for the exported project.
- Since fonts are not included with the exported project, this avoids licensing issues that would occur if proprietary system fonts were distributed alongside the project.

The engine automatically uses system fonts as fallback fonts, which makes it possible to display CJK characters and emoji without having to load a custom font. There are some restrictions that apply though, as mentioned in the **Using emoji** section.

Create a [SystemFont](../godot_csharp_resources.md) resource in the location where you desire to use the system font:

You can either specify one or more font names explicitly (such as `Arial`), or specify the name of a font _alias_ that maps to a "standard" default font for the system:

| Font alias | Windows         | macOS/iOS      | Linux                 | Android            |
| ---------- | --------------- | -------------- | --------------------- | ------------------ |
| sans-serif | Arial           | Helvetica      | Handled by fontconfig | Roboto / Noto Sans |
| serif      | Times New Roman | Times          | Handled by fontconfig | Noto Serif         |
| monospace  | Courier New     | Courier        | Handled by fontconfig | Droid Sans Mono    |
| cursive    | Comic Sans MS   | Apple Chancery | Handled by fontconfig | Dancing Script     |
| fantasy    | Gabriola        | Papyrus        | Handled by fontconfig | Droid Sans Mono    |

On Android, Roboto is used for Latin/Cyrillic text and Noto Sans is used for other languages' glyphs such as CJK. On third-party Android distributions, the exact font selection may differ.

If specifying more than one font, the first font that is found on the system will be used (from top to bottom). Font names and aliases are case-insensitive on all platforms.

Like for font variations, you can save the SystemFont arrangement to a resource file to reuse it in other places.

Remember that different system fonts have different metrics, which means that text that can fit within a rectangle on one platform may not be doing so on another platform. Always reserve some additional space during development so that labels can extend further if needed.

> **Note:** Unlike Windows and macOS/iOS, the set of default fonts shipped on Linux depends on the distribution. This means that on different Linux distributions, different fonts may be displayed for a given system font name or alias.

It is also possible to load fonts at runtime even if they aren't installed on the system. See [Runtime loading and saving](tutorials_io.md) for details.

#### Font prerendering

When using traditional rasterized fonts, Godot caches glyphs on a per-font and per-size basis. This reduces stuttering, but it can still occur the first time a glyph is displayed when running the project. This can be especially noticeable at higher font sizes or on mobile devices.

When using MSDF fonts, they only need to be rasterized once to a special signed distance field texture. This means caching can be done purely on a per-font basis, without taking the font size into consideration. However, the initial rendering of MSDF fonts is slower compared to a traditional rasterized font at a medium size.

To avoid stuttering issues related to font rendering, it is possible to _prerender_ certain glyphs. This can be done for all glyphs you intend to use (for optimal results), or only for common glyphs that are most likely to appear during gameplay (to reduce file size). Glyphs that aren't pre-rendered will be rasterized on-the-fly as usual.

> **Note:** In both cases (traditional and MSDF), font rasterization is done on the CPU. This means that the GPU performance doesn't affect how long it takes for fonts to be rasterized.

Open the Advanced Import Settings dialog by double-clicking the font file in the FileSystem dock. You can also select the font in the FileSystem dock, go to the Import dock then choose **Advanced…** at the bottom:

Move to the **Pre-render Configurations** tab of the Advanced Import Settings dialog, then add a configuration by clicking the "plus" symbol:

After adding a configuration, make sure it is selected by clicking its name once. You can also rename the configuration by double-clicking it.

There are 2 ways to add glyphs to be prerendered to a given configuration. It is possible to use both approaches in a cumulative manner:

**Using text from translations**

For most projects, this approach is the most convenient to use, as it automatically sources text from your language translations. The downside is that it can only be used if your project supports [internationalization](tutorials_i18n.md). Otherwise, stick to the "Using custom text" approach described below.

After adding translations to the Project Settings, use the **Glyphs from the Translations** tab to check translations by double-clicking them, then click **Shape All Strings in the Translations and Add Glyphs** at the bottom:

> **Note:** The list of prerendered glyphs is not automatically updated when translations are updated, so you need to repeat this process if your translations have changed significantly.

**Using custom text**

While it requires manually specifying text that will appear in the game, this is the most efficient approach for games which don't feature user text input. This approach is worth exploring for mobile games to reduce the file size of the distributed app.

To use existing text as a baseline for prerendering, go to the **Glyphs from the Text** sub-tab of the Advanced Import Settings dialog, enter text in the window on the right, then click **Shape Text and Add Glyphs** at the bottom of the dialog:

> **Tip:** If your project supports [internationalization](tutorials_i18n.md), you can paste the contents of your CSV or PO files in the above box to quickly prerender all possible characters that may be rendered during gameplay (excluding user-provided or non-translatable strings).

**By enabling character sets**

The second method requires less configuration and fewer updates if your game's text changes, and is more suited to text-heavy games or multiplayer games with chat. On the other hand, it may cause glyphs that never show up in the game to be prerendered, which is less efficient in terms of file size.

To use existing text as a baseline for prerendering, go to the **Glyphs from the Character Map** sub-tab of the Advanced Import Settings dialog, then _double-click_ character sets to be enabled on the right:

To ensure full prerendering, the character sets you need to enable depend on which languages are supported in your game. For English, only **Basic Latin** needs to be enabled. Enabling **Latin-1 Supplement** as well allows fully covering many more languages, such as French, German and Spanish. For Russian, **Cyrillic** needs to be enabled, and so on.

#### Default project font properties

In the **GUI > Theme** section of the advanced Project Settings, you can choose how the default font should be rendered:

- **Default Font Antialiasing:** Controls the **antialiasing** method used for the default project font.
- **Default Font Hinting:** Controls the **hinting** method used for the default project font.
- **Default Font Subpixel Positioning:** Controls the **subpixel positioning** method for the default project font.
- **Default Font Multichannel Signed Distance Field:** If `true`, makes the default project font use **MSDF font rendering** instead of traditional rasterization.
- **Default Font Generate Mipmaps:** If `true`, enables **mipmap** generation and usage for the default project font.

> **Note:** These project settings _only_ affect the default project font (the one that is hardcoded in the engine binary). Custom fonts' properties are governed by their respective import options instead. You can use the **Import Defaults** section of the Project Settings dialog to override default import options for custom fonts.

---
