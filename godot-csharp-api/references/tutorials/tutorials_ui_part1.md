# Godot 4 C# Tutorials — Ui (Part 1)

> 2 tutorials. C#-specific code examples.

## BBCode in RichTextLabel

### Introduction

[Label](../godot_csharp_ui_controls.md) nodes are great for displaying basic text, but they have limitations. If you want to change the color of the text, or its alignment, you can only do that to the entire label. You can't make a part of the text have another color, or have a part of the text centered. To get around these limitations, you would use a [RichTextLabel](../godot_csharp_ui_controls.md).

[RichTextLabel](../godot_csharp_ui_controls.md) allows for complex formatting of text using a markup syntax or the built-in API. It uses BBCodes for the markup syntax, a system of tags that designate formatting rules for a part of the text. You may be familiar with them if you ever used forums (also known as bulletin boards, hence the "BB" in "BBCode").

Unlike Label, RichTextLabel also comes with its own vertical scrollbar. This scrollbar is automatically displayed if the text does not fit within the control's size. The scrollbar can be disabled by unchecking the **Scroll Active** property in the RichTextLabel inspector.

Note that the BBCode tags can also be used to some extent for other use cases:

- BBCode can be used to format comments in the XML source of the class reference.
- BBCode can be used in [GDScript documentation comments](tutorials_scripting.md).
- BBCode can be used when [printing rich text to the Output bottom panel](tutorials_scripting.md).

> **See also:** You can see how BBCode in RichTextLabel works in action using the [Rich Text Label with BBCode demo project](https://github.com/godotengine/godot-demo-projects/tree/master/gui/rich_text_bbcode).

### Using BBCode

By default, [RichTextLabel](../godot_csharp_ui_controls.md) functions like a normal [Label](../godot_csharp_ui_controls.md). It has the [property_text](../godot_csharp_misc.md) property, which you can edit to have uniformly formatted text. To be able to use BBCode for rich text formatting, you need to turn on the BBCode mode by setting [bbcode_enabled](../godot_csharp_misc.md). After that, you can edit the [text](../godot_csharp_misc.md) property using available tags. Both properties are located at the top of the inspector after selecting a RichTextLabel node.

For example, `BBCode [color=green]test[/color]` would render the word "test" with a green color.

Most BBCodes consist of 3 parts: the opening tag, the content and the closing tag. The opening tag delimits the start of the formatted part, and can also carry some configuration options. Some opening tags, like the `color` one shown above, also require a value to work. Other opening tags may accept multiple options (separated by spaces within the opening tag). The closing tag delimits the end of the formatted part. In some cases, both the closing tag and the content can be omitted.

Unlike BBCode in HTML, leading/trailing whitespace is not removed by a RichTextLabel upon display. Duplicate spaces are also displayed as-is in the final output. This means that when displaying a code block in a RichTextLabel, you don't need to use a preformatted text tag.

```none
[tag]content[/tag]
[tag=value]content[/tag]
[tag option1=value1 option2=value2]content[/tag]
[tag][/tag]
[tag]
```

> **Note:** RichTextLabel doesn't support entangled BBCode tags. For example, instead of using: Use:

### Handling user input safely

In a scenario where users may freely input text (such as chat in a multiplayer game), you should make sure users cannot use arbitrary BBCode tags that will be parsed by RichTextLabel. This is to avoid inappropriate use of formatting, which can be problematic if `[url]` tags are handled by your RichTextLabel (as players may be able to create clickable links to phishing sites or similar).

Using RichTextLabel's `[lb]` and/or `[rb]` tags, we can replace the opening and/or closing brackets of any BBCode tag in a message with those escaped tags. This prevents users from using BBCode that will be parsed as tags – instead, the BBCode will be displayed as text.

The above image was created using the following script:

### Stripping BBCode tags

For certain use cases, it can be desired to remove BBCode tags from the string. This is useful when displaying the RichTextLabel's text in another Control that does not support BBCode (such as a tooltip):

> **Note:** Removing BBCode tags entirely isn't advised for user input, as it can modify the displayed text without users understanding why part of their message was removed. **Escaping user input** should be preferred instead.

### Performance

In most cases, you can use BBCode directly as-is since text formatting is rarely a heavy task. However, with particularly large RichTextLabels (such as console logs spanning thousands of lines), you may encounter stuttering during gameplay when the RichTextLabel's text is updated.

There are several ways to alleviate this:

- Use the `append_text()` function instead of appending to the `text` property. This function will only parse BBCode for the added text, rather than parsing BBCode from the entire `text` property.
- Use `push_[tag]()` and `pop()` functions to add tags to RichTextLabel instead of using BBCode.
- Enable the **Threading > Threaded** property in RichTextLabel. This won't speed up processing, but it will prevent the main thread from blocking, which avoids stuttering during gameplay. Only enable threading if it's actually needed in your project, as threading has some overhead.

### Using push\_[tag]() and pop() functions instead of BBCode

If you don't want to use BBCode for performance reasons, you can use functions provided by RichTextLabel to create formatting tags without writing BBCode in the text.

Every BBCode tag (including effects) has a `push_[tag]()` function (where `[tag]` is the tag's name). There are also a few convenience functions available, such as `push_bold_italics()` that combines both `push_bold()` and `push_italics()` into a single tag. See the [RichTextLabel class reference](../godot_csharp_ui_controls.md) for a complete list of `push_[tag]()` functions.

The `pop()` function is used to end _any_ tag. Since BBCode is a tag _stack_, using `pop()` will close the most recently started tags first.

The following script will result in the same visual output as using `BBCode [color=green]test [i]example[/i][/color]`:

> **Warning:** Do **not** set the `text` property directly when using formatting functions. Appending to the `text` property will erase all modifications made to the RichTextLabel using the `append_text()`, `push_[tag]()` and `pop()` functions.

### Reference

> **See also:** _Some_ of these BBCode tags can be used in tooltips for `@export` script variables as well as in the XML source of the class reference. For more information, see Class reference BBCode.

| Tag | Example |
| b Makes {text} use the bold (or bold italics) font of RichTextLabel. | [b]{text}[/b] |
| i Makes {text} use the italics (or bold italics) font of RichTextLabel. | [i]{text}[/i] |
| u Makes {text} underlined. | [u]{text}[/u] [u color={color}]{text}[/u] |
| s Makes {text} strikethrough. | [s]{text}[/s] [s color={color}]{text}[/s] |
| code Makes {text} use the mono font of RichTextLabel. | [code]{text}[/code] |
| char Adds Unicode character with hexadecimal UTF-32 {codepoint}. | [char={codepoint}] |
| p Adds new paragraph with {text}. Supports configuration options, see Paragraph options. | [p]{text}[/p] [p {options}]{text}[/p] |
| br Adds line break in a text, without adding a new paragraph. If used within a list, this won't create a new list item, but will add a line break within the current item instead. | [br] |
| hr Adds new a horizontal rule to separate content. Supports configuration options, see Horizontal rule options. | [hr] [hr {options}] |
| center Makes {text} horizontally centered. Same as [p align=center]. | [center]{text}[/center] |
| left Makes {text} horizontally left-aligned. Same as [p align=left]. | [left]{text}[/left] |
| right Makes {text} horizontally right-aligned. Same as [p align=right]. | [right]{text}[/right] |
| fill Makes {text} fill the full width of RichTextLabel. Same as [p align=fill]. | [fill]{text}[/fill] |
| indent Indents {text} once. The indentation width is the same as with [ul] or [ol], but without a bullet point. | [indent]{text}[/indent] |
| url Creates a hyperlink (underlined and clickable text). Can contain optional {text} or display {link} as is. Supports configuration options, see URL options. Must be handled with the "meta_clicked" signal to have an effect, see Handling [url] tag clicks. | [url]{link}[/url] [url={link}]{text}[/url] [url {options}]{text}[/url] |
| hint Creates a tooltip hint that is displayed when hovering the text with the mouse. While not required, it's recommended to put tooltip text between double or single quotes. Note that it is not possible to escape quotes using \" or \'. To use single quotes for apostrophes in the hint string, you must use double quotes to surround the string. | [hint="{tooltip text displayed on hover}"]{text}[/hint] |
| img Inserts an image from the {path} (can be any valid Texture2D resource). If {width} is provided, the image will try to fit that width maintaining the aspect ratio. If both {width} and {height} are provided, the image will be scaled to that size. Add % to the end of {width} or {height} value to specify it as percentages of the control width instead of pixels. If {valign} configuration is provided, the image will try to align to the surrounding text, see Image and table vertical alignment. Supports configuration options, see Image options. | [img]{path}[/img] [img={width}]{path}[/img] [img={width}x{height}]{path}[/img] [img={valign}]{path}[/img] [img {options}]{path}[/img] |
| font Makes {text} use a font resource from the {path}. Supports configuration options, see Font options. | [font={path}]{text}[/font] [font {options}]{text}[/font] |
| font_size Use custom font size for {text}. | [font_size={size}]{text}[/font_size] |
| dropcap Use a different font size and color for {text}, while making the tag's contents span multiple lines if it's large enough. A drop cap is typically one uppercase character, but [dropcap] supports containing multiple characters. margins values are comma-separated and can be positive, zero or negative. Values must not be separated by spaces; otherwise, the values won't be parsed correctly. Negative top and bottom margins are particularly useful to allow the rest of the paragraph to display below the dropcap. | [dropcap font={font} font_size={size} color={color} outline_size={size} outline_color={color} margins={left},{top},{right},{bottom}]{text}[/dropcap] |
| opentype_features Enables custom OpenType font features for {text}. Features must be provided as a comma-separated {list}. Values must not be separated by spaces; otherwise, the list won't be parsed correctly. | [opentype_features={list}] {text} [/opentype_features] |
| lang Overrides the language for {text} that is set by the BiDi > Language property in RichTextLabel. {code} must be an ISO language code. This can be used to enforce the use of a specific script for a language without starting a new paragraph. Some font files may contain script-specific substitutes, in which case they will be used. | [lang={code}]{text}[/lang] |
| color Changes the color of {text}. Color must be provided by a common name (see Named colors) or using the HEX format (e.g. #ff00ff, see Hexadecimal color codes). | [color={code/name}]{text}[/color] |
| bgcolor Draws the color behind {text}. This can be used to highlight text. Accepts same values as the color tag. By default, there is a slight padding which is controlled by the text_highlight_h_padding and text_highlight_v_padding theme items in the RichTextLabel node. Set padding to 0 to avoid potential overlapping issues when there are background colors on neighboring lines/columns. | [bgcolor={code/name}]{text}[/bgcolor] |
| fgcolor Draws the color in front of {text}. This can be used to "redact" text by using an opaque foreground color. Accepts same values as the color tag. By default, there is a slight padding which is controlled by the text_highlight_h_padding and text_highlight_v_padding theme items in the RichTextLabel node. Set padding to 0 to avoid potential overlapping issues when there are foreground colors on neighboring lines/columns. | [fgcolor={code/name}]{text}[/fgcolor] |
| outline_size Use custom font outline size for {text}. | [outline_size={size}] {text} [/outline_size] |
| outline_color Use custom outline color for {text}. Accepts same values as the color tag. | [outline_color={code/name}] {text} [/outline_color] |
| table Creates a table with the {number} of columns. Use the cell tag to define table cells. If {valign} configuration is provided, the table will try to align to the surrounding text, see Image and table vertical alignment. If baseline alignment is used, the table is aligned to the baseline of the row with index {alignment_row} (zero-based). {name} is a table name for assistive apps (screen reader). | [table={number}]{cells}[/table] [table={number},{valign}]{cells}[/table] [table={number},{valign},{alignment_row}]{cells}[/table] [table={number},{valign},{alignment_row} name={name}]{cells}[/table] |
| cell Adds a cell with {text} to the table. If {ratio} is provided, the cell will try to expand to that value proportionally to other cells and their ratio values. Supports configuration options, see Cell options. | [cell]{text}[/cell] [cell={ratio}]{text}[/cell] [cell {options}]{text}[/cell] |
| ul Adds an unordered list. List {items} must be provided by putting one item per line of text. The bullet point can be customized using the {bullet} parameter, see Unordered list bullet. | [ul]{items}[/ul] [ul bullet={bullet}]{items}[/ul] |
| ol Adds an ordered (numbered) list of the given {type} (see Ordered list types). List {items} must be provided by putting one item per line of text. | [ol type={type}]{items}[/ol] |
| lb, rb Adds [ and ] respectively. Allows escaping BBCode markup. These are self-closing tags, which means you do not need to close them (and there is no [/lb] or [/rb] closing tag). | [lb]b[rb]text[lb]/b[rb] will display as [b]text[/b]. |
| Several Unicode control characters can be added using their own self-closing tags. This can result in easier maintenance compared to pasting those control characters directly in the text. | [lrm] (left-to-right mark), [rlm] (right-to-left mark), [lre] (left-to-right embedding), [rle] (right-to-left embedding), [lro] (left-to-right override), [rlo] (right-to-left override), [pdf] (pop directional formatting), [alm] (Arabic letter mark), [lri] (left-to-right isolate), [rli] (right-to-left isolate), [fsi] (first strong isolate), [pdi] (pop directional isolate), [zwj] (zero-width joiner), [zwnj] (zero-width non-joiner), [wj] (word joiner), [shy] (soft hyphen) |

> **Note:** Tags for bold (`[b]`) and italics (`[i]`) formatting work best if the appropriate custom fonts are set up in the RichTextLabelNode's theme overrides. If no custom bold or italic fonts are defined, [faux bold and italic fonts](https://fonts.google.com/knowledge/glossary/faux_fake_pseudo_synthesized) will be generated by Godot. These fonts rarely look good in comparison to hand-made bold/italic font variants. The monospaced (`[code]`) tag **only** works if a custom font is set up in the RichTextLabel node's theme overrides. Otherwise, monospaced text will use the regular font. There are no BBCode tags to control vertical centering of text yet. Options can be skipped for all tags.

#### Paragraph options

- **align**

| Values | left (or l), center (or c), right (or r), fill (or f) |
| Default | left |

Text horizontal alignment.

- **bidi_override**, **st**

| Values | default (of d), uri (or u), file (or f), email (or e), list (or l), none (or n), custom (or c) |
| Default | default |

Structured text override.

- **justification_flags**, **jst**

| Values | Comma-separated list of the following values (no space after each comma): kashida (or k), word (or w), trim (or tr), after_last_tab (or lt), skip_last (or sl), skip_last_with_chars (or sv), do_not_skip_single (or ns). |
| Default | word,kashida,skip_last,do_not_skip_single |

Justification (fill alignment) option. See [TextServer](../godot_csharp_misc.md) for more details.

- **direction**, **dir**

| Values | ltr (or l), rtl (or r), auto (or a) |
| Default | Inherit |

Base BiDi direction.

- **language**, **lang**

| Values | ISO language codes. See Locale codes |
| Default | Inherit |

Locale override. Some font files may contain script-specific substitutes, in which case they will be used.

- **tab_stops**

| Values | List of floating-point numbers, e.g. 10.0,30.0 |
| Default | Width of the space character in the font |

Overrides the horizontal offsets for each tab character. When the end of the list is reached, the tab stops will loop over. For example, if you set `tab_stops` to `10.0,30.0`, the first tab will be at `10` pixels, the second tab will be at `10 + 30 = 40` pixels, and the third tab will be at `10 + 30 + 10 = 50` pixels from the origin of the RichTextLabel.

#### Handling [url] tag clicks

By default, `[url]` tags do nothing when clicked. This is to allow flexible use of `[url]` tags rather than limiting them to opening URLs in a web browser.

To handle clicked `[url]` tags, connect the `RichTextLabel` node's [meta_clicked](../godot_csharp_misc.md) signal to a script function.

For example, the following method can be connected to `meta_clicked` to open clicked URLs using the user's default web browser:

For more advanced use cases, it's also possible to store JSON in a `[url]` tag's option and parse it in the function that handles the `meta_clicked` signal. For example:

```none
[url={"example": "value"}]JSON[/url]
```

#### Horizontal rule options

- **color**

| Values | Color name or color in HEX format |
| Default | Color(1, 1, 1, 1) |

Color tint of the rule (modulation).

- **height**

| Values | Integer number |
| Default | 2 |

Target height of the rule in pixels, add `%` to the end of value to specify it as percentages of the control width instead of pixels.

- **width**

| Values | Integer number |
| Default | 90% |

Target width of the rule in pixels, add `%` to the end of value to specify it as percentages of the control width instead of pixels.

- **align**

| Values | left (or l), center (or c), right (or r) |
| Default | left |

Horizontal alignment.

#### URL options

- **underline**

| Values | always, never, hover |
| Default | always |

URL underlining mode.

- **tooltip**

| Values | String. |
| Default | |

URL tooltip.

- **href**

| Values | String. |
| Default | |

URL target address.

#### Image options

- **color**

| Values | Color name or color in HEX format |
| Default | Inherit |

Color tint of the image (modulation).

- **height**

| Values | Integer number |
| Default | Inherit |

Target height of the image in pixels, add `%` to the end of value to specify it as percentages of the control width instead of pixels.

- **width**

| Values | Integer number |
| Default | Inherit |

Target width of the image in pixels, add `%` to the end of value to specify it as percentages of the control width instead of pixels.

- **region**

| Values | x,y,width,height in pixels |
| Default | Inherit |

Region rect of the image. This can be used to display a single image from a spritesheet.

- **pad**

| Values | false, true |
| Default | false |

If set to `true`, and the image is smaller than the size specified by `width` and `height`, the image padding is added to match the size instead of upscaling.

- **tooltip**

| Values | String |
| Default | |

Image tooltip.

- **alt**

| Values | see Image and table vertical alignment |
| Default | center,center |

Image alignment to the surrounding text.

- **alt**

| Values | String |
| Default | |

Image description for assistive apps (screen reader).

#### Image and table vertical alignment

When a vertical alignment value is provided with the `[img]` or `[table]` tag the image/table will try to align itself against the surrounding text. Alignment is performed using a vertical point of the image and a vertical point of the text. There are 3 possible points on the image (`top`, `center`, and `bottom`) and 4 possible points on the text and table (`top`, `center`, `baseline`, and `bottom`), which can be used in any combination.

To specify both points, use their full or short names as a value of the image/table tag:

```none
text [img=top,bottom]...[/img] text
text [img=center,center]...[/img] text
```

```none
text [table=3,center]...[/table] text  # Center to center.
text [table=3,top,bottom]...[/table] text # Top of the table to the bottom of text.
text [table=3,baseline,baseline,1]...[/table] text # Baseline of the second row (rows use zero-based indexing) to the baseline of text.
```

You can also specify just one value (`top`, `center`, or `bottom`) to make use of a corresponding preset (`top-top`, `center-center`, and `bottom-bottom` respectively).

Short names for the values are `t` (`top`), `c` (`center`), `l` (`baseline`), and `b` (`bottom`).

#### Font options

- **name**, **n**

| Values | A valid Font resource path. |
| Default | Inherit |

Font resource path.

- **size**, **s**

| Values | Number in pixels. |
| Default | Inherit |

Custom font size.

- **glyph_spacing**, **gl**

| Values | Number in pixels. |
| Default | Inherit |

Extra spacing for each glyph.

- **space_spacing**, **sp**

| Values | Number in pixels. |
| Default | Inherit |

Extra spacing for the space character.

- **top_spacing**, **top**

| Values | Number in pixels. |
| Default | Inherit |

Extra spacing at the top of the line.

- **bottom_spacing**, **bt**

| Values | Number in pixels. |
| Default | Inherit |

Extra spacing at the bottom of the line.

- **embolden**, **emb**

| Values | Floating-point number. |
| Default | 0.0 |

Font embolden strength, if it is not equal to zero, emboldens the font outlines. Negative values reduce the outline thickness.

- **face_index**, **fi**

| Values | Integer number. |
| Default | 0 |

An active face index in the TrueType / OpenType collection.

- **slant**, **sln**

| Values | Floating-point number. |
| Default | 0.0 |

Font slant strength, positive values slant glyphs to the right. Negative values to the left.

- **opentype_variation**, **otv**

| Values | Comma-separated list of the OpenType variation tags (no space after each comma). |
| Default | |

Font OpenType variation coordinates. See [OpenType variation tags](https://docs.microsoft.com/en-us/typography/opentype/spec/dvaraxisreg).

Note: The value should be enclosed in `"` to allow using `=` inside it:

```none
[font otv="wght=200,wdth=400"] # Sets variable font weight and width.
```

- **opentype_features**, **otf**

| Values | Comma-separated list of the OpenType feature tags (no space after each comma). |
| Default | |

Font OpenType features. See [OpenType features tags](https://docs.microsoft.com/en-us/typography/opentype/spec/featuretags).

Note: The value should be enclosed in `"` to allow using `=` inside it:

```none
[font otf="calt=0,zero=1"] # Disable contextual alternates, enable slashed zero.
```

#### Named colors

For tags that allow specifying a color by name, you can use names of the constants from the built-in [Color](../godot_csharp_math_types.md) class. Named classes can be specified in a number of styles using different casings: `DARK_RED`, `DarkRed`, and `darkred` will give the same exact result.

See this image for a list of color constants:

[View at full size](https://raw.githubusercontent.com/godotengine/godot-docs/master/img/color_constants.png)

#### Hexadecimal color codes

For opaque RGB colors, any valid 6-digit hexadecimal code is supported, e.g. `[color=#ffffff]white[/color]`. Shorthand RGB color codes such as `#6f2` (equivalent to `#66ff22`) are also supported.

For transparent RGB colors, any RGBA 8-digit hexadecimal code can be used, e.g. `[color=#ffffff88]translucent white[/color]`. Note that the alpha channel is the **last** component of the color code, not the first one. Short RGBA color codes such as `#6f28` (equivalent to `#66ff2288`) are supported as well.

#### Cell options

- **shrink**

| Values | false, true |
| Default | true |

If `true`, cell can shrink to its contents.

- **expand**

| Values | Integer number |
| Default | 1 |

Cell expansion ratio. This defines which cells will try to expand to proportionally to other cells and their expansion ratios.

- **border**

| Values | Color name or color in HEX format |
| Default | Inherit |

Cell border color.

- **bg**

| Values | Color name or color in HEX format |
| Default | Inherit |

Cell background color. For alternating odd/even row backgrounds, you can use `bg=odd_color,even_color`.

- **padding**

| Values | 4 comma-separated floating-point numbers (no space after each comma) |
| Default | 0,0,0,0 |

Left, top, right, and bottom cell padding.

#### Unordered list bullet

By default, the `[ul]` tag uses the `U+2022` "Bullet" Unicode glyph as the bullet character. This behavior is similar to web browsers. The bullet character can be customized using `[ul bullet={bullet}]`. If provided, this `{bullet}` parameter must be a string with no enclosing quotes (for example, `[bullet=*]`). You can add trailing spaces after the bullet character to increase the spacing between the bullet and the list item text.

See [Bullet (typography) on Wikipedia](<https://en.wikipedia.org/wiki/Bullet_(typography)>) for a list of common bullet characters that you can paste directly in the `bullet` parameter.

#### Ordered list types

Ordered lists can be used to automatically mark items with numbers or letters in ascending order. This tag supports the following type options:

- `1` - Numbers, using language specific numbering system if possible.
- `a`, `A` - Lower and upper case Latin letters.
- `i`, `I` - Lower and upper case Roman numerals.

### Text effects

BBCode can also be used to create different text effects that can optionally be animated. Several customizable effects are provided out of the box, and you can easily create your own. By default, animated effects will pause [when the SceneTree is paused](tutorials_scripting.md). You can change this behavior by adjusting the RichTextLabel's **Process > Mode** property.

All examples below mention the default values for options in the listed tag format.

> **Note:** Text effects that move characters' positions may result in characters being clipped by the RichTextLabel node bounds. You can resolve this by disabling **Control > Layout > Clip Contents** in the inspector after selecting the RichTextLabel node, or ensuring there is enough margin added around the text by using line breaks above and below the line using the effect.

#### Pulse

Pulse creates an animated pulsing effect that multiplies each character's opacity and color. It can be used to bring attention to specific text. Its tag format is `[pulse freq=1.0 color=#ffffff40 ease=-2.0]{text}[/pulse]`.

`freq` controls the frequency of the half-pulsing cycle (higher is faster). A full pulsing cycle takes `2 * (1.0 / freq)` seconds. `color` is the target color multiplier for blinking. The default mostly fades out text, but not entirely. `ease` is the easing function exponent to use. Negative values provide in-out easing, which is why the default is `-2.0`.

#### Wave

Wave makes the text go up and down. Its tag format is `[wave amp=50.0 freq=5.0 connected=1]{text}[/wave]`.

`amp` controls how high and low the effect goes, and `freq` controls how fast the text goes up and down. A `freq` value of `0` will result in no visible waves, and negative `freq` values won't display any waves either. If `connected` is `1` (default), glyphs with ligatures will be moved together. If `connected` is `0`, each glyph is moved individually even if they are joined by ligatures. This can work around certain rendering issues with font ligatures.

#### Tornado

Tornado makes the text move around in a circle. Its tag format is `[tornado radius=10.0 freq=1.0 connected=1]{text}[/tornado]`.

`radius` is the radius of the circle that controls the offset, `freq` is how fast the text moves in a circle. A `freq` value of `0` will pause the animation, while negative `freq` will play the animation backwards. If `connected` is `1` (default), glyphs with ligatures will be moved together. If `connected` is `0`, each glyph is moved individually even if they are joined by ligatures. This can work around certain rendering issues with font ligatures.

#### Shake

Shake makes the text shake. Its tag format is `[shake rate=20.0 level=5 connected=1]{text}[/shake]`.

`rate` controls how fast the text shakes, `level` controls how far the text is offset from the origin. If `connected` is `1` (default), glyphs with ligatures will be moved together. If `connected` is `0`, each glyph is moved individually even if they are joined by ligatures. This can work around certain rendering issues with font ligatures.

#### Fade

Fade creates a static fade effect that multiplies each character's opacity. Its tag format is `[fade start=4 length=14]{text}[/fade]`.

`start` controls the starting position of the falloff relative to where the fade command is inserted, `length` controls over how many characters should the fade out take place.

#### Rainbow

Rainbow gives the text a rainbow color that changes over time. Its tag format is `[rainbow freq=1.0 sat=0.8 val=0.8 speed=1.0]{text}[/rainbow]`.

`freq` determines how many letters the rainbow extends over before it repeats itself, `sat` is the saturation of the rainbow, `val` is the value of the rainbow. `speed` is the number of full rainbow cycles per second. A positive `speed` value will play the animation forwards, a value of `0` will pause the animation, and a negative `speed` value will play the animation backwards.

Font outlines are _not_ affected by the rainbow effect (they keep their original color). Existing font colors are overridden by the rainbow effect. However, CanvasItem's **Modulate** and **Self Modulate** properties will affect how the rainbow effect looks, as modulation multiplies its final colors.

### Custom BBCode tags and text effects

You can extend the [RichTextEffect](../godot_csharp_misc.md) resource type to create your own custom BBCode tags. Create a new script file that extends the [RichTextEffect](../godot_csharp_misc.md) resource type and give the script a `class_name` so that the effect can be selected in the inspector. Add the `@tool` annotation to your GDScript file if you wish to have these custom effects run within the editor itself. The RichTextLabel does not need to have a script attached, nor does it need to be running in `tool` mode. The new effect can be registered in the Inspector by adding it to the **Markup > Custom Effects** array, or in code with the [install_effect()](../godot_csharp_misc.md) method:

> **Warning:** If the custom effect is not registered within the RichTextLabel's **Markup > Custom Effects** property, no effect will be visible and the original tag will be left as-is.

There is only one function that you need to extend: `_process_custom_fx(char_fx)`. Optionally, you can also provide a custom BBCode identifier by adding a member name `bbcode`. The code will check the `bbcode` property automatically or will use the name of the file to determine what the BBCode tag should be.

#### \_process_custom_fx

This is where the logic of each effect takes place and is called once per glyph during the draw phase of text rendering. This passes in a [CharFXTransform](../godot_csharp_misc.md) object, which holds a few variables to control how the associated glyph is rendered:

- `outline` is `true` if effect is called for drawing text outline.
- `range` tells you how far into a given custom effect block you are in as an index.
- `elapsed_time` is the total amount of time the text effect has been running.
- `visible` will tell you whether the glyph is visible or not and will also allow you to hide a given portion of text.
- `offset` is an offset position relative to where the given glyph should render under normal circumstances.
- `color` is the color of a given glyph.
- `glyph_index` and `font` is glyph being drawn and font data resource used to draw it.
- Finally, `env` is a [Dictionary](../godot_csharp_misc.md) of parameters assigned to a given custom effect. You can use [get()](../godot_csharp_misc.md) with an optional default value to retrieve each parameter, if specified by the user. For example `[custom_fx spread=0.5 color=#FFFF00]test[/custom_fx]` would have a float `spread` and Color `color` parameters in its `env` Dictionary. See below for more usage examples.

The last thing to note about this function is that it is necessary to return a boolean `true` value to verify that the effect processed correctly. This way, if there's a problem with rendering a given glyph, it will back out of rendering custom effects entirely until the user fixes whatever error cropped up in their custom effect logic.

Here are some examples of custom effects:

#### Ghost

#### Matrix

This will add a few new BBCode commands, which can be used like so:

```none
[center][ghost]This is a custom [matrix]effect[/matrix][/ghost] made in
[pulse freq=5.0 height=2.0][pulse color=#00FFAA freq=2.0]GDScript[/pulse][/pulse].[/center]
```

---

## Control node gallery

Here is a list of common Control nodes with their name next to them:

The Control Gallery demo pictured above can be found [on GitHub](https://github.com/godotengine/godot-demo-projects/tree/master/gui/control_gallery).

---
