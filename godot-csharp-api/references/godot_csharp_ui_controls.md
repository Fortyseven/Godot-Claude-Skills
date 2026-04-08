# Godot 4 C# API Reference — Ui Controls

> C#-only reference. 54 classes.

### AcceptDialog
*Inherits: **Window < Viewport < Node < Object** | Inherited by: ConfirmationDialog*

The default use of AcceptDialog is to allow it to only be accepted or closed, with the same result. However, the confirmed and canceled signals allow to make the two actions different, and the add_button() method allows to add custom buttons and actions.

**Properties**
- `bool DialogAutowrap` = `false`
- `bool DialogCloseOnEscape` = `true`
- `bool DialogHideOnOk` = `true`
- `string DialogText` = `""`
- `bool Exclusive` = `true (overrides Window)`
- `bool KeepTitleVisible` = `true (overrides Window)`
- `bool MaximizeDisabled` = `true (overrides Window)`
- `bool MinimizeDisabled` = `true (overrides Window)`
- `string OkButtonText` = `""`
- `string Title` = `"Alert!" (overrides Window)`
- `bool Transient` = `true (overrides Window)`
- `bool Visible` = `false (overrides Window)`
- `bool WrapControls` = `true (overrides Window)`

**Methods**
- `Button AddButton(string text, bool right = false, string action = "")`
- `Button AddCancelButton(string name)`
- `Label GetLabel()`
- `Button GetOkButton()`
- `void RegisterTextEnter(LineEdit lineEdit)`
- `void RemoveButton(Button button)`

### AspectRatioContainer
*Inherits: **Container < Control < CanvasItem < Node < Object***

A container type that arranges its child controls in a way that preserves their proportions automatically when the container is resized. Useful when a container has a dynamic size and the child nodes must adjust their sizes accordingly without losing their aspect ratios.

**Properties**
- `AlignmentMode AlignmentHorizontal` = `1`
- `AlignmentMode AlignmentVertical` = `1`
- `float Ratio` = `1.0`
- `StretchMode StretchMode` = `2`

### BaseButton
*Inherits: **Control < CanvasItem < Node < Object** | Inherited by: Button, LinkButton, TextureButton*

BaseButton is an abstract base class for GUI buttons. It doesn't display anything by itself.

**Properties**
- `ActionMode ActionMode` = `1`
- `ButtonGroup ButtonGroup`
- `BitField[MouseButtonMask] ButtonMask` = `1`
- `bool ButtonPressed` = `false`
- `bool Disabled` = `false`
- `FocusMode FocusMode` = `2 (overrides Control)`
- `bool KeepPressedOutside` = `false`
- `Shortcut Shortcut`
- `bool ShortcutFeedback` = `true`
- `bool ShortcutInTooltip` = `true`
- `bool ToggleMode` = `false`

**Methods**
- `void _Pressed() [virtual]`
- `void _Toggled(bool toggledOn) [virtual]`
- `DrawMode GetDrawMode()`
- `bool IsHovered()`
- `void SetPressedNoSignal(bool pressed)`

### BoxContainer
*Inherits: **Container < Control < CanvasItem < Node < Object** | Inherited by: HBoxContainer, VBoxContainer*

A container that arranges its child controls horizontally or vertically, rearranging them automatically when their minimum size changes.

**Properties**
- `AlignmentMode Alignment` = `0`
- `bool Vertical` = `false`

**Methods**
- `Control AddSpacer(bool begin)`

### ButtonGroup
*Inherits: **Resource < RefCounted < Object***

A group of BaseButton-derived buttons. The buttons in a ButtonGroup are treated like radio buttons: No more than one button can be pressed at a time. Some types of buttons (such as CheckBox) may have a special appearance in this state.

**Properties**
- `bool AllowUnpress` = `false`
- `bool ResourceLocalToScene` = `true (overrides Resource)`

**Methods**
- `Array[BaseButton] GetButtons()`
- `BaseButton GetPressedButton()`

### Button
*Inherits: **BaseButton < Control < CanvasItem < Node < Object** | Inherited by: CheckBox, CheckButton, ColorPickerButton, MenuButton, OptionButton*

Button is the standard themed button. It can contain text and an icon, and it will display them according to the current Theme.

**Properties**
- `HorizontalAlignment Alignment` = `1`
- `AutowrapMode AutowrapMode` = `0`
- `BitField[LineBreakFlag] AutowrapTrimFlags` = `128`
- `bool ClipText` = `false`
- `bool ExpandIcon` = `false`
- `bool Flat` = `false`
- `Texture2D Icon`
- `HorizontalAlignment IconAlignment` = `0`
- `string Language` = `""`
- `string Text` = `""`
- `TextDirection TextDirection` = `0`
- `OverrunBehavior TextOverrunBehavior` = `0`
- `VerticalAlignment VerticalIconAlignment` = `1`

**C# Examples**
```csharp
public override void _Ready()
{
    var button = new Button();
    button.Text = "Click me";
    button.Pressed += ButtonPressed;
    AddChild(button);
}

private void ButtonPressed()
{
    GD.Print("Hello world!");
}
```

### CenterContainer
*Inherits: **Container < Control < CanvasItem < Node < Object***

CenterContainer is a container that keeps all of its child controls in its center at their minimum size.

**Properties**
- `bool UseTopLeft` = `false`

### CheckBox
*Inherits: **Button < BaseButton < Control < CanvasItem < Node < Object***

CheckBox allows the user to choose one of only two possible options. It's similar to CheckButton in functionality, but it has a different appearance. To follow established UX patterns, it's recommended to use CheckBox when toggling it has no immediate effect on something. For example, it could be used when toggling it will only do something once a confirmation button is pressed.

**Properties**
- `HorizontalAlignment Alignment` = `0 (overrides Button)`
- `bool ToggleMode` = `true (overrides BaseButton)`

### CheckButton
*Inherits: **Button < BaseButton < Control < CanvasItem < Node < Object***

CheckButton is a toggle button displayed as a check field. It's similar to CheckBox in functionality, but it has a different appearance. To follow established UX patterns, it's recommended to use CheckButton when toggling it has an immediate effect on something. For example, it can be used when pressing it shows or hides advanced settings, without asking the user to confirm this action.

**Properties**
- `HorizontalAlignment Alignment` = `0 (overrides Button)`
- `bool ToggleMode` = `true (overrides BaseButton)`

### CodeEdit
*Inherits: **TextEdit < Control < CanvasItem < Node < Object***

CodeEdit is a specialized TextEdit designed for editing plain text code files. It has many features commonly found in code editors such as line numbers, line folding, code completion, indent management, and string/comment management.

**Properties**
- `bool AutoBraceCompletionEnabled` = `false`
- `bool AutoBraceCompletionHighlightMatching` = `false`
- `Godot.Collections.Dictionary AutoBraceCompletionPairs` = `{ "\"": "\"", "'": "'", "(": ")", "[": "]", "{": "}" }`
- `bool CodeCompletionEnabled` = `false`
- `Array[String] CodeCompletionPrefixes` = `[]`
- `Array[String] DelimiterComments` = `[]`
- `Array[String] DelimiterStrings` = `["' '", "\" \""]`
- `bool GuttersDrawBookmarks` = `false`
- `bool GuttersDrawBreakpointsGutter` = `false`
- `bool GuttersDrawExecutingLines` = `false`
- `bool GuttersDrawFoldGutter` = `false`
- `bool GuttersDrawLineNumbers` = `false`
- `int GuttersLineNumbersMinDigits` = `3`
- `bool GuttersZeroPadLineNumbers` = `false`
- `bool IndentAutomatic` = `false`
- `Array[String] IndentAutomaticPrefixes` = `[":", "{", "[", "("]`
- `int IndentSize` = `4`
- `bool IndentUseSpaces` = `false`
- `LayoutDirection LayoutDirection` = `2 (overrides Control)`
- `bool LineFolding` = `false`
- `Array[int] LineLengthGuidelines` = `[]`
- `bool SymbolLookupOnClick` = `false`
- `bool SymbolTooltipOnHover` = `false`
- `TextDirection TextDirection` = `1 (overrides TextEdit)`

**Methods**
- `void _ConfirmCodeCompletion(bool replace) [virtual]`
- `Array[Dictionary] _FilterCodeCompletionCandidates(Array[Dictionary] candidates) [virtual]`
- `void _RequestCodeCompletion(bool force) [virtual]`
- `void AddAutoBraceCompletionPair(string startKey, string endKey)`
- `void AddCodeCompletionOption(CodeCompletionKind type, string displayText, string insertText, Color textColor = Color(1, 1, 1, 1), Resource icon = null, Variant value = null, int location = 1024)`
- `void AddCommentDelimiter(string startKey, string endKey, bool lineOnly = false)`
- `void AddStringDelimiter(string startKey, string endKey, bool lineOnly = false)`
- `bool CanFoldLine(int line)`
- `void CancelCodeCompletion()`
- `void ClearBookmarkedLines()`
- `void ClearBreakpointedLines()`
- `void ClearCommentDelimiters()`
- `void ClearExecutingLines()`
- `void ClearStringDelimiters()`
- `void ConfirmCodeCompletion(bool replace = false)`
- `void ConvertIndent(int fromLine = -1, int toLine = -1)`
- `void CreateCodeRegion()`
- `void DeleteLines()`
- `void DoIndent()`
- `void DuplicateLines()`
- `void DuplicateSelection()`
- `void FoldAllLines()`
- `void FoldLine(int line)`
- `string GetAutoBraceCompletionCloseKey(string openKey)`
- `PackedInt32Array GetBookmarkedLines()`
- `PackedInt32Array GetBreakpointedLines()`
- `Godot.Collections.Dictionary GetCodeCompletionOption(int index)`
- `Array[Dictionary] GetCodeCompletionOptions()`
- `int GetCodeCompletionSelectedIndex()`
- `string GetCodeRegionEndTag()`
- `string GetCodeRegionStartTag()`
- `string GetDelimiterEndKey(int delimiterIndex)`
- `Vector2 GetDelimiterEndPosition(int line, int column)`
- `string GetDelimiterStartKey(int delimiterIndex)`
- `Vector2 GetDelimiterStartPosition(int line, int column)`
- `PackedInt32Array GetExecutingLines()`
- `Array[int] GetFoldedLines()`
- `string GetTextForCodeCompletion()`
- `string GetTextForSymbolLookup()`
- `string GetTextWithCursorChar(int line, int column)`

### ColorPickerButton
*Inherits: **Button < BaseButton < Control < CanvasItem < Node < Object***

Encapsulates a ColorPicker, making it accessible by pressing a button. Pressing the button will toggle the ColorPicker's visibility.

**Properties**
- `Color Color` = `Color(0, 0, 0, 1)`
- `bool EditAlpha` = `true`
- `bool EditIntensity` = `true`
- `bool ToggleMode` = `true (overrides BaseButton)`

**Methods**
- `ColorPicker GetPicker()`
- `PopupPanel GetPopup()`

### ColorPicker
*Inherits: **VBoxContainer < BoxContainer < Container < Control < CanvasItem < Node < Object***

A widget that provides an interface for selecting or modifying a color. It can optionally provide functionalities like a color sampler (eyedropper), color modes, and presets.

**Properties**
- `bool CanAddSwatches` = `true`
- `Color Color` = `Color(1, 1, 1, 1)`
- `ColorModeType ColorMode` = `0`
- `bool ColorModesVisible` = `true`
- `bool DeferredMode` = `false`
- `bool EditAlpha` = `true`
- `bool EditIntensity` = `true`
- `bool HexVisible` = `true`
- `PickerShapeType PickerShape` = `0`
- `bool PresetsVisible` = `true`
- `bool SamplerVisible` = `true`
- `bool SlidersVisible` = `true`

**Methods**
- `void AddPreset(Color color)`
- `void AddRecentPreset(Color color)`
- `void ErasePreset(Color color)`
- `void EraseRecentPreset(Color color)`
- `PackedColorArray GetPresets()`
- `PackedColorArray GetRecentPresets()`

### ColorRect
*Inherits: **Control < CanvasItem < Node < Object***

Displays a rectangle filled with a solid color. If you need to display the border alone, consider using a Panel instead.

**Properties**
- `Color Color` = `Color(1, 1, 1, 1)`

### ConfirmationDialog
*Inherits: **AcceptDialog < Window < Viewport < Node < Object** | Inherited by: EditorCommandPalette, FileDialog, ScriptCreateDialog*

A dialog used for confirmation of actions. This window is similar to AcceptDialog, but pressing its Cancel button can have a different outcome from pressing the OK button. The order of the two buttons varies depending on the host OS.

**Properties**
- `string CancelButtonText` = `"Cancel"`
- `Vector2i MinSize` = `Vector2i(200, 70) (overrides Window)`
- `Vector2i Size` = `Vector2i(200, 100) (overrides Window)`
- `string Title` = `"Please Confirm..." (overrides Window)`

**Methods**
- `Button GetCancelButton()`

**C# Examples**
```csharp
GetCancelButton().Pressed += OnCanceled;
```

### Container
*Inherits: **Control < CanvasItem < Node < Object** | Inherited by: AspectRatioContainer, BoxContainer, CenterContainer, EditorProperty, FlowContainer, FoldableContainer, ...*

Base class for all GUI containers. A Container automatically arranges its child controls in a certain way. This class can be inherited to make custom container types.

**Properties**
- `MouseFilter MouseFilter` = `1 (overrides Control)`

**Methods**
- `PackedInt32Array _GetAllowedSizeFlagsHorizontal() [virtual]`
- `PackedInt32Array _GetAllowedSizeFlagsVertical() [virtual]`
- `void FitChildInRect(Control child, Rect2 rect)`
- `void QueueSort()`

### Control
*Inherits: **CanvasItem < Node < Object** | Inherited by: BaseButton, ColorRect, Container, GraphEdit, ItemList, Label, ...*

Base class for all UI-related nodes. Control features a bounding rectangle that defines its extents, an anchor position relative to its parent control or the current viewport, and offsets relative to the anchor. The offsets update automatically when the node, any of its parents, or the screen size change.

**Properties**
- `Array[NodePath] AccessibilityControlsNodes` = `[]`
- `Array[NodePath] AccessibilityDescribedByNodes` = `[]`
- `string AccessibilityDescription` = `""`
- `Array[NodePath] AccessibilityFlowToNodes` = `[]`
- `Array[NodePath] AccessibilityLabeledByNodes` = `[]`
- `AccessibilityLiveMode AccessibilityLive` = `0`
- `string AccessibilityName` = `""`
- `float AnchorBottom` = `0.0`
- `float AnchorLeft` = `0.0`
- `float AnchorRight` = `0.0`
- `float AnchorTop` = `0.0`
- `bool AutoTranslate`
- `bool ClipContents` = `false`
- `Vector2 CustomMinimumSize` = `Vector2(0, 0)`
- `FocusBehaviorRecursive FocusBehaviorRecursive` = `0`
- `FocusMode FocusMode` = `0`
- `NodePath FocusNeighborBottom` = `NodePath("")`
- `NodePath FocusNeighborLeft` = `NodePath("")`
- `NodePath FocusNeighborRight` = `NodePath("")`
- `NodePath FocusNeighborTop` = `NodePath("")`
- `NodePath FocusNext` = `NodePath("")`
- `NodePath FocusPrevious` = `NodePath("")`
- `Vector2 GlobalPosition`
- `GrowDirection GrowHorizontal` = `1`
- `GrowDirection GrowVertical` = `1`
- `LayoutDirection LayoutDirection` = `0`
- `bool LocalizeNumeralSystem` = `true`
- `MouseBehaviorRecursive MouseBehaviorRecursive` = `0`
- `CursorShape MouseDefaultCursorShape` = `0`
- `MouseFilter MouseFilter` = `0`

**Methods**
- `string _AccessibilityGetContextualInfo() [virtual]`
- `bool _CanDropData(Vector2 atPosition, Variant data) [virtual]`
- `void _DropData(Vector2 atPosition, Variant data) [virtual]`
- `string _GetAccessibilityContainerName(Node node) [virtual]`
- `Variant _GetDragData(Vector2 atPosition) [virtual]`
- `Vector2 _GetMinimumSize() [virtual]`
- `string _GetTooltip(Vector2 atPosition) [virtual]`
- `void _GuiInput(InputEvent event) [virtual]`
- `bool _HasPoint(Vector2 point) [virtual]`
- `Object _MakeCustomTooltip(string forText) [virtual]`
- `Array[Vector3i] _StructuredTextParser(Godot.Collections.Array args, string text) [virtual]`
- `void AcceptEvent()`
- `void AccessibilityDrag()`
- `void AccessibilityDrop()`
- `void AddThemeColorOverride(StringName name, Color color)`
- `void AddThemeConstantOverride(StringName name, int constant)`
- `void AddThemeFontOverride(StringName name, Font font)`
- `void AddThemeFontSizeOverride(StringName name, int fontSize)`
- `void AddThemeIconOverride(StringName name, Texture2D texture)`
- `void AddThemeStyleboxOverride(StringName name, StyleBox stylebox)`
- `void BeginBulkThemeOverride()`
- `void EndBulkThemeOverride()`
- `Control FindNextValidFocus()`
- `Control FindPrevValidFocus()`
- `Control FindValidFocusNeighbor(Side side)`
- `void ForceDrag(Variant data, Control preview)`
- `float GetAnchor(Side side)`
- `Vector2 GetBegin()`
- `Vector2 GetCombinedMinimumSize()`
- `Vector2 GetCombinedPivotOffset()`
- `CursorShape GetCursorShape(Vector2 position = Vector2(0, 0))`
- `Vector2 GetEnd()`
- `FocusMode GetFocusModeWithOverride()`
- `NodePath GetFocusNeighbor(Side side)`
- `Rect2 GetGlobalRect()`
- `Vector2 GetMinimumSize()`
- `MouseFilter GetMouseFilterWithOverride()`
- `float GetOffset(Side offset)`
- `Vector2 GetParentAreaSize()`
- `Control GetParentControl()`

**C# Examples**
```csharp
var styleBox = new StyleBoxFlat();
styleBox.SetBgColor(new Color(1, 1, 0));
styleBox.SetBorderWidthAll(2);
// We assume here that the `Theme` property has been assigned a custom Theme beforehand.
Theme.SetStyleBox("panel", "TooltipPanel", styleBox);
Theme.SetColor("font_color", "TooltipLabel", new Color(0, 1, 1));
```
```csharp
public override bool _CanDropData(Vector2 atPosition, Variant data)
{
    // Check position if it is relevant to you
    // Otherwise, just check data
    return data.VariantType == Variant.Type.Dictionary && data.AsGodotDictionary().ContainsKey("expected");
}
```

### FileDialog
*Inherits: **ConfirmationDialog < AcceptDialog < Window < Viewport < Node < Object** | Inherited by: EditorFileDialog*

FileDialog is a preset dialog used to choose files and directories in the filesystem. It supports filter masks. FileDialog automatically sets its window title according to the file_mode. If you want to use a custom title, disable this by setting mode_overrides_title to false.

**Properties**
- `Access Access` = `0`
- `string CurrentDir`
- `string CurrentFile`
- `string CurrentPath`
- `bool DeletingEnabled` = `true`
- `bool DialogHideOnOk` = `false (overrides AcceptDialog)`
- `DisplayMode DisplayMode` = `0`
- `bool FavoritesEnabled` = `true`
- `bool FileFilterToggleEnabled` = `true`
- `FileMode FileMode` = `4`
- `bool FileSortOptionsEnabled` = `true`
- `string FilenameFilter` = `""`
- `PackedStringArray Filters` = `PackedStringArray()`
- `bool FolderCreationEnabled` = `true`
- `bool HiddenFilesToggleEnabled` = `true`
- `bool LayoutToggleEnabled` = `true`
- `bool ModeOverridesTitle` = `true`
- `int OptionCount` = `0`
- `bool OverwriteWarningEnabled` = `true`
- `bool RecentListEnabled` = `true`
- `string RootSubfolder` = `""`
- `bool ShowHiddenFiles` = `false`
- `Vector2i Size` = `Vector2i(640, 360) (overrides Window)`
- `string Title` = `"Save a File" (overrides Window)`
- `bool UseNativeDialog` = `false`

**Methods**
- `void AddFilter(string filter, string description = "", string mimeType = "")`
- `void AddOption(string name, PackedStringArray values, int defaultValueIndex)`
- `void ClearFilenameFilter()`
- `void ClearFilters()`
- `void DeselectAll()`
- `PackedStringArray GetFavoriteList() [static]`
- `LineEdit GetLineEdit()`
- `int GetOptionDefault(int option)`
- `string GetOptionName(int option)`
- `PackedStringArray GetOptionValues(int option)`
- `PackedStringArray GetRecentList() [static]`
- `Godot.Collections.Dictionary GetSelectedOptions()`
- `VBoxContainer GetVbox()`
- `void Invalidate()`
- `bool IsCustomizationFlagEnabled(Customization flag)`
- `void PopupFileDialog()`
- `void SetCustomizationFlagEnabled(Customization flag, bool enabled)`
- `void SetFavoriteList(PackedStringArray favorites) [static]`
- `void SetGetIconCallback(Callable callback) [static]`
- `void SetGetThumbnailCallback(Callable callback) [static]`
- `void SetOptionDefault(int option, int defaultValueIndex)`
- `void SetOptionName(int option, string name)`
- `void SetOptionValues(int option, PackedStringArray values)`
- `void SetRecentList(PackedStringArray recents) [static]`

### FlowContainer
*Inherits: **Container < Control < CanvasItem < Node < Object** | Inherited by: HFlowContainer, VFlowContainer*

A container that arranges its child controls horizontally or vertically and wraps them around at the borders. This is similar to how text in a book wraps around when no more words can fit on a line.

**Properties**
- `AlignmentMode Alignment` = `0`
- `LastWrapAlignmentMode LastWrapAlignment` = `0`
- `bool ReverseFill` = `false`
- `bool Vertical` = `false`

**Methods**
- `int GetLineCount()`

### GraphEdit
*Inherits: **Control < CanvasItem < Node < Object***

GraphEdit provides tools for creation, manipulation, and display of various graphs. Its main purpose in the engine is to power the visual programming systems, such as visual shaders, but it is also available for use in user projects.

**Properties**
- `bool ClipContents` = `true (overrides Control)`
- `bool ConnectionLinesAntialiased` = `true`
- `float ConnectionLinesCurvature` = `0.5`
- `float ConnectionLinesThickness` = `4.0`
- `Array[Dictionary] Connections` = `[]`
- `FocusMode FocusMode` = `2 (overrides Control)`
- `GridPattern GridPattern` = `0`
- `bool MinimapEnabled` = `true`
- `float MinimapOpacity` = `0.65`
- `Vector2 MinimapSize` = `Vector2(240, 160)`
- `PanningScheme PanningScheme` = `0`
- `bool RightDisconnects` = `false`
- `Vector2 ScrollOffset` = `Vector2(0, 0)`
- `bool ShowArrangeButton` = `true`
- `bool ShowGrid` = `true`
- `bool ShowGridButtons` = `true`
- `bool ShowMenu` = `true`
- `bool ShowMinimapButton` = `true`
- `bool ShowZoomButtons` = `true`
- `bool ShowZoomLabel` = `false`
- `int SnappingDistance` = `20`
- `bool SnappingEnabled` = `true`
- `Godot.Collections.Dictionary TypeNames` = `{}`
- `float Zoom` = `1.0`
- `float ZoomMax` = `2.0736003`
- `float ZoomMin` = `0.23256795`
- `float ZoomStep` = `1.2`

**Methods**
- `PackedVector2Array _GetConnectionLine(Vector2 fromPosition, Vector2 toPosition) [virtual]`
- `bool _IsInInputHotzone(Object inNode, int inPort, Vector2 mousePosition) [virtual]`
- `bool _IsInOutputHotzone(Object inNode, int inPort, Vector2 mousePosition) [virtual]`
- `bool _IsNodeHoverValid(StringName fromNode, int fromPort, StringName toNode, int toPort) [virtual]`
- `void AddValidConnectionType(int fromType, int toType)`
- `void AddValidLeftDisconnectType(int type)`
- `void AddValidRightDisconnectType(int type)`
- `void ArrangeNodes()`
- `void AttachGraphElementToFrame(StringName element, StringName frame)`
- `void ClearConnections()`
- `Error ConnectNode(StringName fromNode, int fromPort, StringName toNode, int toPort, bool keepAlive = false)`
- `void DetachGraphElementFromFrame(StringName element)`
- `void DisconnectNode(StringName fromNode, int fromPort, StringName toNode, int toPort)`
- `void ForceConnectionDragEnd()`
- `Array[StringName] GetAttachedNodesOfFrame(StringName frame)`
- `Godot.Collections.Dictionary GetClosestConnectionAtPoint(Vector2 point, float maxDistance = 4.0)`
- `int GetConnectionCount(StringName fromNode, int fromPort)`
- `PackedVector2Array GetConnectionLine(Vector2 fromNode, Vector2 toNode)`
- `Array[Dictionary] GetConnectionListFromNode(StringName node)`
- `Array[Dictionary] GetConnectionsIntersectingWithRect(Rect2 rect)`
- `GraphFrame GetElementFrame(StringName element)`
- `HBoxContainer GetMenuHbox()`
- `bool IsNodeConnected(StringName fromNode, int fromPort, StringName toNode, int toPort)`
- `bool IsValidConnectionType(int fromType, int toType)`
- `void RemoveValidConnectionType(int fromType, int toType)`
- `void RemoveValidLeftDisconnectType(int type)`
- `void RemoveValidRightDisconnectType(int type)`
- `void SetConnectionActivity(StringName fromNode, int fromPort, StringName toNode, int toPort, float amount)`
- `void SetSelected(Node node)`

**C# Examples**
```csharp
public override bool _IsNodeHoverValid(StringName fromNode, int fromPort, StringName toNode, int toPort)
{
    return fromNode != toNode;
}
```

### GraphFrame
*Inherits: **GraphElement < Container < Control < CanvasItem < Node < Object***

GraphFrame is a special GraphElement to which other GraphElements can be attached. It can be configured to automatically resize to enclose all attached GraphElements. If the frame is moved, all the attached GraphElements inside it will be moved as well.

**Properties**
- `bool AutoshrinkEnabled` = `true`
- `int AutoshrinkMargin` = `40`
- `int DragMargin` = `16`
- `MouseFilter MouseFilter` = `0 (overrides Control)`
- `Color TintColor` = `Color(0.3, 0.3, 0.3, 0.75)`
- `bool TintColorEnabled` = `false`
- `string Title` = `""`

**Methods**
- `HBoxContainer GetTitlebarHbox()`

### GraphNode
*Inherits: **GraphElement < Container < Control < CanvasItem < Node < Object***

GraphNode allows to create nodes for a GraphEdit graph with customizable content based on its child controls. GraphNode is derived from Container and it is responsible for placing its children on screen. This works similar to VBoxContainer. Children, in turn, provide GraphNode with so-called slots, each of which can have a connection port on either side.

**Properties**
- `FocusMode FocusMode` = `3 (overrides Control)`
- `bool IgnoreInvalidConnectionType` = `false`
- `MouseFilter MouseFilter` = `0 (overrides Control)`
- `FocusMode SlotsFocusMode` = `3`
- `string Title` = `""`

**Methods**
- `void _DrawPort(int slotIndex, Vector2i position, bool left, Color color) [virtual]`
- `void ClearAllSlots()`
- `void ClearSlot(int slotIndex)`
- `Color GetInputPortColor(int portIdx)`
- `int GetInputPortCount()`
- `Vector2 GetInputPortPosition(int portIdx)`
- `int GetInputPortSlot(int portIdx)`
- `int GetInputPortType(int portIdx)`
- `Color GetOutputPortColor(int portIdx)`
- `int GetOutputPortCount()`
- `Vector2 GetOutputPortPosition(int portIdx)`
- `int GetOutputPortSlot(int portIdx)`
- `int GetOutputPortType(int portIdx)`
- `Color GetSlotColorLeft(int slotIndex)`
- `Color GetSlotColorRight(int slotIndex)`
- `Texture2D GetSlotCustomIconLeft(int slotIndex)`
- `Texture2D GetSlotCustomIconRight(int slotIndex)`
- `Variant GetSlotMetadataLeft(int slotIndex)`
- `Variant GetSlotMetadataRight(int slotIndex)`
- `int GetSlotTypeLeft(int slotIndex)`
- `int GetSlotTypeRight(int slotIndex)`
- `HBoxContainer GetTitlebarHbox()`
- `bool IsSlotDrawStylebox(int slotIndex)`
- `bool IsSlotEnabledLeft(int slotIndex)`
- `bool IsSlotEnabledRight(int slotIndex)`
- `void SetSlot(int slotIndex, bool enableLeftPort, int typeLeft, Color colorLeft, bool enableRightPort, int typeRight, Color colorRight, Texture2D customIconLeft = null, Texture2D customIconRight = null, bool drawStylebox = true)`
- `void SetSlotColorLeft(int slotIndex, Color color)`
- `void SetSlotColorRight(int slotIndex, Color color)`
- `void SetSlotCustomIconLeft(int slotIndex, Texture2D customIcon)`
- `void SetSlotCustomIconRight(int slotIndex, Texture2D customIcon)`
- `void SetSlotDrawStylebox(int slotIndex, bool enable)`
- `void SetSlotEnabledLeft(int slotIndex, bool enable)`
- `void SetSlotEnabledRight(int slotIndex, bool enable)`
- `void SetSlotMetadataLeft(int slotIndex, Variant value)`
- `void SetSlotMetadataRight(int slotIndex, Variant value)`
- `void SetSlotTypeLeft(int slotIndex, int type)`
- `void SetSlotTypeRight(int slotIndex, int type)`

### GridContainer
*Inherits: **Container < Control < CanvasItem < Node < Object***

GridContainer arranges its child controls in a grid layout. The number of columns is specified by the columns property, whereas the number of rows depends on how many are needed for the child controls. The number of rows and columns is preserved for every size of the container.

**Properties**
- `int Columns` = `1`

### HBoxContainer
*Inherits: **BoxContainer < Container < Control < CanvasItem < Node < Object** | Inherited by: EditorResourcePicker, EditorToaster, OpenXRInteractionProfileEditorBase*

A variant of BoxContainer that can only arrange its child controls horizontally. Child controls are rearranged automatically when their minimum size changes.

### HScrollBar
*Inherits: **ScrollBar < Range < Control < CanvasItem < Node < Object***

A horizontal scrollbar, typically used to navigate through content that extends beyond the visible width of a control. It is a Range-based control and goes from left (min) to right (max).

### HSlider
*Inherits: **Slider < Range < Control < CanvasItem < Node < Object***

A horizontal slider, used to adjust a value by moving a grabber along a horizontal axis. It is a Range-based control and goes from left (min) to right (max).

### HSplitContainer
*Inherits: **SplitContainer < Container < Control < CanvasItem < Node < Object***

A container that accepts only two child controls, then arranges them horizontally and creates a divisor between them. The divisor can be dragged around to change the size relation between the child controls.

### ItemList
*Inherits: **Control < CanvasItem < Node < Object***

This control provides a vertical list of selectable items that may be in a single or in multiple columns, with each item having options for text and an icon. Tooltips are supported and may be different for every item in the list.

**Properties**
- `bool AllowReselect` = `false`
- `bool AllowRmbSelect` = `false`
- `bool AllowSearch` = `true`
- `bool AutoHeight` = `false`
- `bool AutoWidth` = `false`
- `bool ClipContents` = `true (overrides Control)`
- `int FixedColumnWidth` = `0`
- `Vector2i FixedIconSize` = `Vector2i(0, 0)`
- `FocusMode FocusMode` = `2 (overrides Control)`
- `IconMode IconMode` = `1`
- `float IconScale` = `1.0`
- `int ItemCount` = `0`
- `int MaxColumns` = `1`
- `int MaxTextLines` = `1`
- `bool SameColumnWidth` = `false`
- `ScrollHintMode ScrollHintMode` = `0`
- `SelectMode SelectMode` = `0`
- `OverrunBehavior TextOverrunBehavior` = `3`
- `bool TileScrollHint` = `false`
- `bool WraparoundItems` = `true`

**Methods**
- `int AddIconItem(Texture2D icon, bool selectable = true)`
- `int AddItem(string text, Texture2D icon = null, bool selectable = true)`
- `void Clear()`
- `void Deselect(int idx)`
- `void DeselectAll()`
- `void EnsureCurrentIsVisible()`
- `void ForceUpdateListSize()`
- `HScrollBar GetHScrollBar()`
- `int GetItemAtPosition(Vector2 position, bool exact = false)`
- `AutoTranslateMode GetItemAutoTranslateMode(int idx)`
- `Color GetItemCustomBgColor(int idx)`
- `Color GetItemCustomFgColor(int idx)`
- `Texture2D GetItemIcon(int idx)`
- `Color GetItemIconModulate(int idx)`
- `Rect2 GetItemIconRegion(int idx)`
- `string GetItemLanguage(int idx)`
- `Variant GetItemMetadata(int idx)`
- `Rect2 GetItemRect(int idx, bool expand = true)`
- `string GetItemText(int idx)`
- `TextDirection GetItemTextDirection(int idx)`
- `string GetItemTooltip(int idx)`
- `PackedInt32Array GetSelectedItems()`
- `VScrollBar GetVScrollBar()`
- `bool IsAnythingSelected()`
- `bool IsItemDisabled(int idx)`
- `bool IsItemIconTransposed(int idx)`
- `bool IsItemSelectable(int idx)`
- `bool IsItemTooltipEnabled(int idx)`
- `bool IsSelected(int idx)`
- `void MoveItem(int fromIdx, int toIdx)`
- `void RemoveItem(int idx)`
- `void Select(int idx, bool single = true)`
- `void SetItemAutoTranslateMode(int idx, AutoTranslateMode mode)`
- `void SetItemCustomBgColor(int idx, Color customBgColor)`
- `void SetItemCustomFgColor(int idx, Color customFgColor)`
- `void SetItemDisabled(int idx, bool disabled)`
- `void SetItemIcon(int idx, Texture2D icon)`
- `void SetItemIconModulate(int idx, Color modulate)`
- `void SetItemIconRegion(int idx, Rect2 rect)`
- `void SetItemIconTransposed(int idx, bool transposed)`

### LineEdit
*Inherits: **Control < CanvasItem < Node < Object***

LineEdit provides an input field for editing a single line of text.

**Properties**
- `HorizontalAlignment Alignment` = `0`
- `bool BackspaceDeletesCompositeCharacterEnabled` = `false`
- `bool CaretBlink` = `false`
- `float CaretBlinkInterval` = `0.65`
- `int CaretColumn` = `0`
- `bool CaretForceDisplayed` = `false`
- `bool CaretMidGrapheme` = `false`
- `bool ClearButtonEnabled` = `false`
- `bool ContextMenuEnabled` = `true`
- `bool DeselectOnFocusLossEnabled` = `true`
- `bool DragAndDropSelectionEnabled` = `true`
- `bool DrawControlChars` = `false`
- `bool Editable` = `true`
- `bool EmojiMenuEnabled` = `true`
- `bool ExpandToTextLength` = `false`
- `bool Flat` = `false`
- `FocusMode FocusMode` = `2 (overrides Control)`
- `ExpandMode IconExpandMode` = `0`
- `bool KeepEditingOnTextSubmit` = `false`
- `string Language` = `""`
- `int MaxLength` = `0`
- `bool MiddleMousePasteEnabled` = `true`
- `CursorShape MouseDefaultCursorShape` = `1 (overrides Control)`
- `string PlaceholderText` = `""`
- `Texture2D RightIcon`
- `float RightIconScale` = `1.0`
- `bool Secret` = `false`
- `string SecretCharacter` = `"•"`
- `bool SelectAllOnFocus` = `false`
- `bool SelectingEnabled` = `true`

**Methods**
- `void ApplyIme()`
- `void CancelIme()`
- `void Clear()`
- `void DeleteCharAtCaret()`
- `void DeleteText(int fromColumn, int toColumn)`
- `void Deselect()`
- `void Edit(bool hideFocus = false)`
- `PopupMenu GetMenu()`
- `int GetNextCompositeCharacterColumn(int column)`
- `int GetPreviousCompositeCharacterColumn(int column)`
- `float GetScrollOffset()`
- `string GetSelectedText()`
- `int GetSelectionFromColumn()`
- `int GetSelectionToColumn()`
- `bool HasImeText()`
- `bool HasRedo()`
- `bool HasSelection()`
- `bool HasUndo()`
- `void InsertTextAtCaret(string text)`
- `bool IsEditing()`
- `bool IsMenuVisible()`
- `void MenuOption(int option)`
- `void Select(int from = 0, int to = -1)`
- `void SelectAll()`
- `void Unedit()`

**C# Examples**
```csharp
Text = "Hello world";
MaxLength = 5;
// `Text` becomes "Hello".
MaxLength = 10;
Text += " goodbye";
// `Text` becomes "Hello good".
// `text_change_rejected` is emitted with "bye" as a parameter.
```
```csharp
public override void _Ready()
{
    var menu = GetMenu();
    // Remove all items after "Redo".
    menu.ItemCount = menu.GetItemIndex(LineEdit.MenuItems.Redo) + 1;
    // Add custom items.
    menu.AddSeparator();
    menu.AddItem("Insert Date", LineEdit.MenuItems.Max + 1);
    // Add event handler.
    menu.IdPressed += OnItemPressed;
}

public void OnItemPressed(int id)
{
    if (id == LineEdit.MenuItems.Max + 1)
    {
        InsertTextAtCaret(Time.GetDateStringFromSystem());
    }
}
```

### LinkButton
*Inherits: **BaseButton < Control < CanvasItem < Node < Object***

A button that represents a link. This type of button is primarily used for interactions that cause a context change (like linking to a web page).

**Properties**
- `string EllipsisChar` = `"…"`
- `FocusMode FocusMode` = `3 (overrides Control)`
- `string Language` = `""`
- `CursorShape MouseDefaultCursorShape` = `2 (overrides Control)`
- `StructuredTextParser StructuredTextBidiOverride` = `0`
- `Godot.Collections.Array StructuredTextBidiOverrideOptions` = `[]`
- `string Text` = `""`
- `TextDirection TextDirection` = `0`
- `OverrunBehavior TextOverrunBehavior` = `0`
- `UnderlineMode Underline` = `0`
- `string Uri` = `""`

**C# Examples**
```csharp
Uri = "https://godotengine.org"; // Opens the URL in the default web browser.
Uri = "C:\SomeFolder"; // Opens the file explorer at the given path.
Uri = "C:\SomeImage.png"; // Opens the given image in the default viewing app.
```

### MarginContainer
*Inherits: **Container < Control < CanvasItem < Node < Object** | Inherited by: EditorDock*

MarginContainer adds an adjustable margin on each side of its child controls. The margins are added around all children, not around each individual one. To control the MarginContainer's margins, use the margin_* theme properties listed below.

**C# Examples**
```csharp
// This code sample assumes the current script is extending MarginContainer.
int marginValue = 100;
AddThemeConstantOverride("margin_top", marginValue);
AddThemeConstantOverride("margin_left", marginValue);
AddThemeConstantOverride("margin_bottom", marginValue);
AddThemeConstantOverride("margin_right", marginValue);
```

### MenuButton
*Inherits: **Button < BaseButton < Control < CanvasItem < Node < Object***

A button that brings up a PopupMenu when clicked. To create new items inside this PopupMenu, use get_popup().add_item("My Item Name"). You can also create them directly from Godot editor's inspector.

**Properties**
- `ActionMode ActionMode` = `0 (overrides BaseButton)`
- `bool Flat` = `true (overrides Button)`
- `FocusMode FocusMode` = `3 (overrides Control)`
- `int ItemCount` = `0`
- `bool SwitchOnHover` = `false`
- `bool ToggleMode` = `true (overrides BaseButton)`

**Methods**
- `PopupMenu GetPopup()`
- `void SetDisableShortcuts(bool disabled)`
- `void ShowPopup()`

### OptionButton
*Inherits: **Button < BaseButton < Control < CanvasItem < Node < Object***

OptionButton is a type of button that brings up a dropdown with selectable items when pressed. The item selected becomes the "current" item and is displayed as the button text.

**Properties**
- `ActionMode ActionMode` = `0 (overrides BaseButton)`
- `HorizontalAlignment Alignment` = `0 (overrides Button)`
- `bool AllowReselect` = `false`
- `bool FitToLongestItem` = `true`
- `int ItemCount` = `0`
- `int Selected` = `-1`
- `bool ToggleMode` = `true (overrides BaseButton)`

**Methods**
- `void AddIconItem(Texture2D texture, string label, int id = -1)`
- `void AddItem(string label, int id = -1)`
- `void AddSeparator(string text = "")`
- `void Clear()`
- `AutoTranslateMode GetItemAutoTranslateMode(int idx)`
- `Texture2D GetItemIcon(int idx)`
- `int GetItemId(int idx)`
- `int GetItemIndex(int id)`
- `Variant GetItemMetadata(int idx)`
- `string GetItemText(int idx)`
- `string GetItemTooltip(int idx)`
- `PopupMenu GetPopup()`
- `int GetSelectableItem(bool fromLast = false)`
- `int GetSelectedId()`
- `Variant GetSelectedMetadata()`
- `bool HasSelectableItems()`
- `bool IsItemDisabled(int idx)`
- `bool IsItemSeparator(int idx)`
- `void RemoveItem(int idx)`
- `void Select(int idx)`
- `void SetDisableShortcuts(bool disabled)`
- `void SetItemAutoTranslateMode(int idx, AutoTranslateMode mode)`
- `void SetItemDisabled(int idx, bool disabled)`
- `void SetItemIcon(int idx, Texture2D texture)`
- `void SetItemId(int idx, int id)`
- `void SetItemMetadata(int idx, Variant metadata)`
- `void SetItemText(int idx, string text)`
- `void SetItemTooltip(int idx, string tooltip)`
- `void ShowPopup()`

### PanelContainer
*Inherits: **Container < Control < CanvasItem < Node < Object** | Inherited by: OpenXRBindingModifierEditor, ScriptEditor*

A container that keeps its child controls within the area of a StyleBox. Useful for giving controls an outline.

**Properties**
- `MouseFilter MouseFilter` = `0 (overrides Control)`

### PopupMenu
*Inherits: **Popup < Window < Viewport < Node < Object***

PopupMenu is a modal window used to display a list of options. Useful for toolbars and context menus.

**Properties**
- `bool AllowSearch` = `true`
- `bool HideOnCheckableItemSelection` = `true`
- `bool HideOnItemSelection` = `true`
- `bool HideOnStateItemSelection` = `false`
- `int ItemCount` = `0`
- `bool PreferNativeMenu` = `false`
- `bool ShrinkHeight` = `true`
- `bool ShrinkWidth` = `true`
- `float SubmenuPopupDelay` = `0.2`
- `SystemMenus SystemMenuId` = `0`
- `bool Transparent` = `true (overrides Window)`
- `bool TransparentBg` = `true (overrides Viewport)`

**Methods**
- `bool ActivateItemByEvent(InputEvent event, bool forGlobalOnly = false)`
- `void AddCheckItem(string label, int id = -1, Key accel = 0)`
- `void AddCheckShortcut(Shortcut shortcut, int id = -1, bool global = false)`
- `void AddIconCheckItem(Texture2D texture, string label, int id = -1, Key accel = 0)`
- `void AddIconCheckShortcut(Texture2D texture, Shortcut shortcut, int id = -1, bool global = false)`
- `void AddIconItem(Texture2D texture, string label, int id = -1, Key accel = 0)`
- `void AddIconRadioCheckItem(Texture2D texture, string label, int id = -1, Key accel = 0)`
- `void AddIconRadioCheckShortcut(Texture2D texture, Shortcut shortcut, int id = -1, bool global = false)`
- `void AddIconShortcut(Texture2D texture, Shortcut shortcut, int id = -1, bool global = false, bool allowEcho = false)`
- `void AddItem(string label, int id = -1, Key accel = 0)`
- `void AddMultistateItem(string label, int maxStates, int defaultState = 0, int id = -1, Key accel = 0)`
- `void AddRadioCheckItem(string label, int id = -1, Key accel = 0)`
- `void AddRadioCheckShortcut(Shortcut shortcut, int id = -1, bool global = false)`
- `void AddSeparator(string label = "", int id = -1)`
- `void AddShortcut(Shortcut shortcut, int id = -1, bool global = false, bool allowEcho = false)`
- `void AddSubmenuItem(string label, string submenu, int id = -1)`
- `void AddSubmenuNodeItem(string label, PopupMenu submenu, int id = -1)`
- `void Clear(bool freeSubmenus = false)`
- `int GetFocusedItem()`
- `Key GetItemAccelerator(int index)`
- `AutoTranslateMode GetItemAutoTranslateMode(int index)`
- `Texture2D GetItemIcon(int index)`
- `int GetItemIconMaxWidth(int index)`
- `Color GetItemIconModulate(int index)`
- `int GetItemId(int index)`
- `int GetItemIndent(int index)`
- `int GetItemIndex(int id)`
- `string GetItemLanguage(int index)`
- `Variant GetItemMetadata(int index)`
- `int GetItemMultistate(int index)`
- `int GetItemMultistateMax(int index)`
- `Shortcut GetItemShortcut(int index)`
- `string GetItemSubmenu(int index)`
- `PopupMenu GetItemSubmenuNode(int index)`
- `string GetItemText(int index)`
- `TextDirection GetItemTextDirection(int index)`
- `string GetItemTooltip(int index)`
- `bool IsItemCheckable(int index)`
- `bool IsItemChecked(int index)`
- `bool IsItemDisabled(int index)`

### PopupPanel
*Inherits: **Popup < Window < Viewport < Node < Object***

A popup with a configurable panel background. Any child controls added to this node will be stretched to fit the panel's size (similar to how PanelContainer works). If you are making windows, see Window.

**Properties**
- `bool Transparent` = `true (overrides Window)`
- `bool TransparentBg` = `true (overrides Viewport)`

### ProgressBar
*Inherits: **Range < Control < CanvasItem < Node < Object***

A control used for visual representation of a percentage. Shows the fill percentage in the center. Can also be used to show indeterminate progress. For more fill modes, use TextureProgressBar instead.

**Properties**
- `bool EditorPreviewIndeterminate`
- `int FillMode` = `0`
- `bool Indeterminate` = `false`
- `bool ShowPercentage` = `true`

### RichTextLabel
*Inherits: **Control < CanvasItem < Node < Object***

A control for displaying text that can contain custom fonts, images, and basic formatting. RichTextLabel manages these as an internal tag stack. It also adapts itself to given width/heights.

**Properties**
- `AutowrapMode AutowrapMode` = `3`
- `BitField[LineBreakFlag] AutowrapTrimFlags` = `192`
- `bool BbcodeEnabled` = `false`
- `bool ClipContents` = `true (overrides Control)`
- `bool ContextMenuEnabled` = `false`
- `Godot.Collections.Array CustomEffects` = `[]`
- `bool DeselectOnFocusLossEnabled` = `true`
- `bool DragAndDropSelectionEnabled` = `true`
- `bool FitContent` = `false`
- `FocusMode FocusMode` = `3 (overrides Control)`
- `bool HintUnderlined` = `true`
- `HorizontalAlignment HorizontalAlignment` = `0`
- `BitField[JustificationFlag] JustificationFlags` = `163`
- `string Language` = `""`
- `bool MetaUnderlined` = `true`
- `int ProgressBarDelay` = `1000`
- `bool ScrollActive` = `true`
- `bool ScrollFollowing` = `false`
- `bool ScrollFollowingVisibleCharacters` = `false`
- `bool SelectionEnabled` = `false`
- `bool ShortcutKeysEnabled` = `true`
- `StructuredTextParser StructuredTextBidiOverride` = `0`
- `Godot.Collections.Array StructuredTextBidiOverrideOptions` = `[]`
- `int TabSize` = `4`
- `PackedFloat32Array TabStops` = `PackedFloat32Array()`
- `string Text` = `""`
- `TextDirection TextDirection` = `0`
- `bool Threaded` = `false`
- `VerticalAlignment VerticalAlignment` = `0`
- `int VisibleCharacters` = `-1`

**Methods**
- `void AddHr(int width = 90, int height = 2, Color color = Color(1, 1, 1, 1), HorizontalAlignment alignment = 1, bool widthInPercent = true, bool heightInPercent = false)`
- `void AddImage(Texture2D image, int width = 0, int height = 0, Color color = Color(1, 1, 1, 1), InlineAlignment inlineAlign = 5, Rect2 region = Rect2(0, 0, 0, 0), Variant key = null, bool pad = false, string tooltip = "", bool widthInPercent = false, bool heightInPercent = false, string altText = "")`
- `void AddText(string text)`
- `void AppendText(string bbcode)`
- `void Clear()`
- `void Deselect()`
- `int GetCharacterLine(int character)`
- `int GetCharacterParagraph(int character)`
- `int GetContentHeight()`
- `int GetContentWidth()`
- `int GetLineCount()`
- `int GetLineHeight(int line)`
- `float GetLineOffset(int line)`
- `Vector2i GetLineRange(int line)`
- `int GetLineWidth(int line)`
- `PopupMenu GetMenu()`
- `int GetParagraphCount()`
- `float GetParagraphOffset(int paragraph)`
- `string GetParsedText()`
- `string GetSelectedText()`
- `int GetSelectionFrom()`
- `float GetSelectionLineOffset()`
- `int GetSelectionTo()`
- `int GetTotalCharacterCount()`
- `VScrollBar GetVScrollBar()`
- `Rect2i GetVisibleContentRect()`
- `int GetVisibleLineCount()`
- `int GetVisibleParagraphCount()`
- `void InstallEffect(Variant effect)`
- `bool InvalidateParagraph(int paragraph)`
- `bool IsFinished()`
- `bool IsMenuVisible()`
- `bool IsReady()`
- `void MenuOption(int option)`
- `void Newline()`
- `void ParseBbcode(string bbcode)`
- `Godot.Collections.Dictionary ParseExpressionsForValues(PackedStringArray expressions)`
- `void Pop()`
- `void PopAll()`
- `void PopContext()`

**C# Examples**
```csharp
public override void _Ready()
{
    var menu = GetMenu();
    // Remove "Select All" item.
    menu.RemoveItem(RichTextLabel.MenuItems.SelectAll);
    // Add custom items.
    menu.AddSeparator();
    menu.AddItem("Duplicate Text", RichTextLabel.MenuItems.Max + 1);
    // Add event handler.
    menu.IdPressed += OnItemPressed;
}

public void OnItemPressed(int id)
{
    if (id == TextEdit.MenuItems.Max + 1)
    {
        AddText("\n" + GetParsedText());
    }
}
```
```csharp
public partial class TestLabel : RichTextLabel
{
    [Export]
    public Panel BackgroundPanel { get; set; }

    public override async void _Ready()
    {
        await ToSignal(this, Control.SignalName.Draw);
        BackgroundGPanel.Position = GetVisibleContentRect().Position;
        BackgroundPanel.Size = GetVisibleContentRect().Size;
    }
}
```

### ScrollBar
*Inherits: **Range < Control < CanvasItem < Node < Object** | Inherited by: HScrollBar, VScrollBar*

Abstract base class for scrollbars, typically used to navigate through content that extends beyond the visible area of a control. Scrollbars are Range-based controls.

**Properties**
- `float CustomStep` = `-1.0`
- `FocusMode FocusMode` = `3 (overrides Control)`
- `float Step` = `0.0 (overrides Range)`

### ScrollContainer
*Inherits: **Container < Control < CanvasItem < Node < Object** | Inherited by: EditorInspector*

A container used to provide a child control with scrollbars when needed. Scrollbars will automatically be drawn at the right (for vertical) or bottom (for horizontal) and will enable dragging to move the viewable Control (and its children) within the ScrollContainer. Scrollbars will also automatically resize the grabber based on the Control.custom_minimum_size of the Control relative to the ScrollContainer.

**Properties**
- `bool ClipContents` = `true (overrides Control)`
- `bool DrawFocusBorder` = `false`
- `bool FollowFocus` = `false`
- `ScrollMode HorizontalScrollMode` = `1`
- `int ScrollDeadzone` = `0`
- `ScrollHintMode ScrollHintMode` = `0`
- `int ScrollHorizontal` = `0`
- `float ScrollHorizontalCustomStep` = `-1.0`
- `int ScrollVertical` = `0`
- `float ScrollVerticalCustomStep` = `-1.0`
- `bool TileScrollHint` = `false`
- `ScrollMode VerticalScrollMode` = `1`

**Methods**
- `void EnsureControlVisible(Control control)`
- `HScrollBar GetHScrollBar()`
- `VScrollBar GetVScrollBar()`

### Slider
*Inherits: **Range < Control < CanvasItem < Node < Object** | Inherited by: HSlider, VSlider*

Abstract base class for sliders, used to adjust a value by moving a grabber along a horizontal or vertical axis. Sliders are Range-based controls.

**Properties**
- `bool Editable` = `true`
- `FocusMode FocusMode` = `2 (overrides Control)`
- `bool Scrollable` = `true`
- `float Step` = `1.0 (overrides Range)`
- `int TickCount` = `0`
- `bool TicksOnBorders` = `false`
- `TickPosition TicksPosition` = `0`

### SpinBox
*Inherits: **Range < Control < CanvasItem < Node < Object***

SpinBox is a numerical input text field. It allows entering integers and floating-point numbers. The SpinBox also has up and down buttons that can be clicked increase or decrease the value. The value can also be changed by dragging the mouse up or down over the SpinBox's arrows.

**Properties**
- `HorizontalAlignment Alignment` = `0`
- `bool CustomArrowRound` = `false`
- `float CustomArrowStep` = `0.0`
- `bool Editable` = `true`
- `string Prefix` = `""`
- `bool SelectAllOnFocus` = `false`
- `BitField[SizeFlags] SizeFlagsVertical` = `1 (overrides Control)`
- `float Step` = `1.0 (overrides Range)`
- `string Suffix` = `""`
- `bool UpdateOnTextChanged` = `false`

**Methods**
- `void Apply()`
- `LineEdit GetLineEdit()`

**C# Examples**
```csharp
var spinBox = new SpinBox();
AddChild(spinBox);
var lineEdit = spinBox.GetLineEdit();
lineEdit.ContextMenuEnabled = false;
spinBox.AlignHorizontal = LineEdit.HorizontalAlignEnum.Right;
```

### SplitContainer
*Inherits: **Container < Control < CanvasItem < Node < Object** | Inherited by: HSplitContainer, VSplitContainer*

A container that arranges child controls horizontally or vertically and creates grabbers between them. The grabbers can be dragged around to change the size relations between the child controls.

**Properties**
- `bool Collapsed` = `false`
- `bool DragAreaHighlightInEditor` = `false`
- `int DragAreaMarginBegin` = `0`
- `int DragAreaMarginEnd` = `0`
- `int DragAreaOffset` = `0`
- `DraggerVisibility DraggerVisibility` = `0`
- `bool DraggingEnabled` = `true`
- `int SplitOffset` = `0`
- `PackedInt32Array SplitOffsets` = `PackedInt32Array(0)`
- `bool TouchDraggerEnabled` = `false`
- `bool Vertical` = `false`

**Methods**
- `void ClampSplitOffset(int priorityIndex = 0)`
- `Control GetDragAreaControl()`
- `Array[Control] GetDragAreaControls()`

### SubViewportContainer
*Inherits: **Container < Control < CanvasItem < Node < Object***

A container that displays the contents of underlying SubViewport child nodes. It uses the combined size of the SubViewports as minimum size, unless stretch is enabled.

**Properties**
- `FocusMode FocusMode` = `1 (overrides Control)`
- `bool MouseTarget` = `false`
- `bool Stretch` = `false`
- `int StretchShrink` = `1`

**Methods**
- `bool _PropagateInputEvent(InputEvent event) [virtual]`

### TabBar
*Inherits: **Control < CanvasItem < Node < Object***

A control that provides a horizontal bar with tabs. Similar to TabContainer but is only in charge of drawing tabs, not interacting with children.

**Properties**
- `bool ClipTabs` = `true`
- `bool CloseWithMiddleMouse` = `true`
- `int CurrentTab` = `-1`
- `bool DeselectEnabled` = `false`
- `bool DragToRearrangeEnabled` = `false`
- `FocusMode FocusMode` = `2 (overrides Control)`
- `int MaxTabWidth` = `0`
- `bool ScrollToSelected` = `true`
- `bool ScrollingEnabled` = `true`
- `bool SelectWithRmb` = `false`
- `bool SwitchOnDragHover` = `true`
- `AlignmentMode TabAlignment` = `0`
- `CloseButtonDisplayPolicy TabCloseDisplayPolicy` = `0`
- `int TabCount` = `0`
- `int TabsRearrangeGroup` = `-1`

**Methods**
- `void AddTab(string title = "", Texture2D icon = null)`
- `void ClearTabs()`
- `void EnsureTabVisible(int idx)`
- `bool GetOffsetButtonsVisible()`
- `int GetPreviousTab()`
- `Texture2D GetTabButtonIcon(int tabIdx)`
- `Texture2D GetTabIcon(int tabIdx)`
- `int GetTabIconMaxWidth(int tabIdx)`
- `int GetTabIdxAtPoint(Vector2 point)`
- `string GetTabLanguage(int tabIdx)`
- `Variant GetTabMetadata(int tabIdx)`
- `int GetTabOffset()`
- `Rect2 GetTabRect(int tabIdx)`
- `TextDirection GetTabTextDirection(int tabIdx)`
- `string GetTabTitle(int tabIdx)`
- `string GetTabTooltip(int tabIdx)`
- `bool IsTabDisabled(int tabIdx)`
- `bool IsTabHidden(int tabIdx)`
- `void MoveTab(int from, int to)`
- `void RemoveTab(int tabIdx)`
- `bool SelectNextAvailable()`
- `bool SelectPreviousAvailable()`
- `void SetTabButtonIcon(int tabIdx, Texture2D icon)`
- `void SetTabDisabled(int tabIdx, bool disabled)`
- `void SetTabHidden(int tabIdx, bool hidden)`
- `void SetTabIcon(int tabIdx, Texture2D icon)`
- `void SetTabIconMaxWidth(int tabIdx, int width)`
- `void SetTabLanguage(int tabIdx, string language)`
- `void SetTabMetadata(int tabIdx, Variant metadata)`
- `void SetTabTextDirection(int tabIdx, TextDirection direction)`
- `void SetTabTitle(int tabIdx, string title)`
- `void SetTabTooltip(int tabIdx, string tooltip)`

**C# Examples**
```csharp
GetNode<TabBar>("TabBar").TabClosePressed += GetNode<TabBar>("TabBar").RemoveTab;
```

### TabContainer
*Inherits: **Container < Control < CanvasItem < Node < Object***

Arranges child controls into a tabbed view, creating a tab for each one. The active tab's corresponding control is made visible, while all other child controls are hidden. Ignores non-control children.

**Properties**
- `bool AllTabsInFront` = `false`
- `bool ClipTabs` = `true`
- `int CurrentTab` = `-1`
- `bool DeselectEnabled` = `false`
- `bool DragToRearrangeEnabled` = `false`
- `bool SwitchOnDragHover` = `true`
- `AlignmentMode TabAlignment` = `0`
- `FocusMode TabFocusMode` = `2`
- `TabPosition TabsPosition` = `0`
- `int TabsRearrangeGroup` = `-1`
- `bool TabsVisible` = `true`
- `bool UseHiddenTabsForMinSize` = `false`

**Methods**
- `Control GetCurrentTabControl()`
- `Popup GetPopup()`
- `int GetPreviousTab()`
- `TabBar GetTabBar()`
- `Texture2D GetTabButtonIcon(int tabIdx)`
- `Control GetTabControl(int tabIdx)`
- `int GetTabCount()`
- `Texture2D GetTabIcon(int tabIdx)`
- `int GetTabIconMaxWidth(int tabIdx)`
- `int GetTabIdxAtPoint(Vector2 point)`
- `int GetTabIdxFromControl(Control control)`
- `Variant GetTabMetadata(int tabIdx)`
- `string GetTabTitle(int tabIdx)`
- `string GetTabTooltip(int tabIdx)`
- `bool IsTabDisabled(int tabIdx)`
- `bool IsTabHidden(int tabIdx)`
- `bool SelectNextAvailable()`
- `bool SelectPreviousAvailable()`
- `void SetPopup(Node popup)`
- `void SetTabButtonIcon(int tabIdx, Texture2D icon)`
- `void SetTabDisabled(int tabIdx, bool disabled)`
- `void SetTabHidden(int tabIdx, bool hidden)`
- `void SetTabIcon(int tabIdx, Texture2D icon)`
- `void SetTabIconMaxWidth(int tabIdx, int width)`
- `void SetTabMetadata(int tabIdx, Variant metadata)`
- `void SetTabTitle(int tabIdx, string title)`
- `void SetTabTooltip(int tabIdx, string tooltip)`

### TextEdit
*Inherits: **Control < CanvasItem < Node < Object** | Inherited by: CodeEdit*

A multiline text editor. It also has limited facilities for editing code, such as syntax highlighting support. For more advanced facilities for editing code, see CodeEdit.

**Properties**
- `AutowrapMode AutowrapMode` = `3`
- `bool BackspaceDeletesCompositeCharacterEnabled` = `false`
- `bool CaretBlink` = `false`
- `float CaretBlinkInterval` = `0.65`
- `bool CaretDrawWhenEditableDisabled` = `false`
- `bool CaretMidGrapheme` = `false`
- `bool CaretMoveOnRightClick` = `true`
- `bool CaretMultiple` = `true`
- `CaretType CaretType` = `0`
- `bool ContextMenuEnabled` = `true`
- `string CustomWordSeparators` = `""`
- `bool DeselectOnFocusLossEnabled` = `true`
- `bool DragAndDropSelectionEnabled` = `true`
- `bool DrawControlChars` = `false`
- `bool DrawSpaces` = `false`
- `bool DrawTabs` = `false`
- `bool Editable` = `true`
- `bool EmojiMenuEnabled` = `true`
- `bool EmptySelectionClipboardEnabled` = `true`
- `FocusMode FocusMode` = `2 (overrides Control)`
- `bool HighlightAllOccurrences` = `false`
- `bool HighlightCurrentLine` = `false`
- `bool IndentWrappedLines` = `false`
- `string Language` = `""`
- `bool MiddleMousePasteEnabled` = `true`
- `bool MinimapDraw` = `false`
- `int MinimapWidth` = `80`
- `CursorShape MouseDefaultCursorShape` = `1 (overrides Control)`
- `string PlaceholderText` = `""`
- `bool ScrollFitContentHeight` = `false`

**Methods**
- `void _Backspace(int caretIndex) [virtual]`
- `void _Copy(int caretIndex) [virtual]`
- `void _Cut(int caretIndex) [virtual]`
- `void _HandleUnicodeInput(int unicodeChar, int caretIndex) [virtual]`
- `void _Paste(int caretIndex) [virtual]`
- `void _PastePrimaryClipboard(int caretIndex) [virtual]`
- `int AddCaret(int line, int column)`
- `void AddCaretAtCarets(bool below)`
- `void AddGutter(int at = -1)`
- `void AddSelectionForNextOccurrence()`
- `void AdjustCaretsAfterEdit(int caret, int fromLine, int fromCol, int toLine, int toCol)`
- `void AdjustViewportToCaret(int caretIndex = 0)`
- `void ApplyIme()`
- `void Backspace(int caretIndex = -1)`
- `void BeginComplexOperation()`
- `void BeginMulticaretEdit()`
- `void CancelIme()`
- `void CenterViewportToCaret(int caretIndex = 0)`
- `void Clear()`
- `void ClearUndoHistory()`
- `void CollapseCarets(int fromLine, int fromColumn, int toLine, int toColumn, bool inclusive = false)`
- `void Copy(int caretIndex = -1)`
- `void Cut(int caretIndex = -1)`
- `void DeleteSelection(int caretIndex = -1)`
- `void Deselect(int caretIndex = -1)`
- `void EndAction()`
- `void EndComplexOperation()`
- `void EndMulticaretEdit()`
- `int GetCaretColumn(int caretIndex = 0)`
- `int GetCaretCount()`
- `Vector2 GetCaretDrawPos(int caretIndex = 0)`
- `PackedInt32Array GetCaretIndexEditOrder()`
- `int GetCaretLine(int caretIndex = 0)`
- `int GetCaretWrapIndex(int caretIndex = 0)`
- `int GetFirstNonWhitespaceColumn(int line)`
- `int GetFirstVisibleLine()`
- `int GetGutterCount()`
- `string GetGutterName(int gutter)`
- `GutterType GetGutterType(int gutter)`
- `int GetGutterWidth(int gutter)`

**C# Examples**
```csharp
public override void _Ready()
{
    var menu = GetMenu();
    // Remove all items after "Redo".
    menu.ItemCount = menu.GetItemIndex(TextEdit.MenuItems.Redo) + 1;
    // Add custom items.
    menu.AddSeparator();
    menu.AddItem("Insert Date", TextEdit.MenuItems.Max + 1);
    // Add event handler.
    menu.IdPressed += OnItemPressed;
}

public void OnItemPressed(int id)
{
    if (id == TextEdit.MenuItems.Max + 1)
    {
        InsertTextAtCaret(Time.GetDateStringFromSystem());
    }
}
```
```csharp
Vector2I result = Search("print", (uint)TextEdit.SearchFlags.WholeWords, 0, 0);
if (result.X != -1)
{
    // Result found.
    int lineNumber = result.Y;
    int columnNumber = result.X;
}
```

### TextureButton
*Inherits: **BaseButton < Control < CanvasItem < Node < Object***

TextureButton has the same functionality as Button, except it uses sprites instead of Godot's Theme resource. It is faster to create, but it doesn't support localization like more complex Controls.

**Properties**
- `bool FlipH` = `false`
- `bool FlipV` = `false`
- `bool IgnoreTextureSize` = `false`
- `StretchMode StretchMode` = `2`
- `BitMap TextureClickMask`
- `Texture2D TextureDisabled`
- `Texture2D TextureFocused`
- `Texture2D TextureHover`
- `Texture2D TextureNormal`
- `Texture2D TexturePressed`

### TextureRect
*Inherits: **Control < CanvasItem < Node < Object***

A control that displays a texture, for example an icon inside a GUI. The texture's placement can be controlled with the stretch_mode property. It can scale, tile, or stay centered inside its bounding rectangle.

**Properties**
- `ExpandMode ExpandMode` = `0`
- `bool FlipH` = `false`
- `bool FlipV` = `false`
- `MouseFilter MouseFilter` = `1 (overrides Control)`
- `StretchMode StretchMode` = `0`
- `Texture2D Texture`

### VBoxContainer
*Inherits: **BoxContainer < Container < Control < CanvasItem < Node < Object** | Inherited by: ColorPicker, ScriptEditorBase*

A variant of BoxContainer that can only arrange its child controls vertically. Child controls are rearranged automatically when their minimum size changes.

### VScrollBar
*Inherits: **ScrollBar < Range < Control < CanvasItem < Node < Object***

A vertical scrollbar, typically used to navigate through content that extends beyond the visible height of a control. It is a Range-based control and goes from top (min) to bottom (max). Note that this direction is the opposite of VSlider's.

**Properties**
- `BitField[SizeFlags] SizeFlagsHorizontal` = `0 (overrides Control)`
- `BitField[SizeFlags] SizeFlagsVertical` = `1 (overrides Control)`

### VSlider
*Inherits: **Slider < Range < Control < CanvasItem < Node < Object***

A vertical slider, used to adjust a value by moving a grabber along a vertical axis. It is a Range-based control and goes from bottom (min) to top (max). Note that this direction is the opposite of VScrollBar's.

**Properties**
- `BitField[SizeFlags] SizeFlagsHorizontal` = `0 (overrides Control)`
- `BitField[SizeFlags] SizeFlagsVertical` = `1 (overrides Control)`

### VSplitContainer
*Inherits: **SplitContainer < Container < Control < CanvasItem < Node < Object***

A container that accepts only two child controls, then arranges them vertically and creates a divisor between them. The divisor can be dragged around to change the size relation between the child controls.

### VideoStreamPlayer
*Inherits: **Control < CanvasItem < Node < Object***

A control used for playback of VideoStream resources.

**Properties**
- `int AudioTrack` = `0`
- `bool Autoplay` = `false`
- `int BufferingMsec` = `500`
- `StringName Bus` = `&"Master"`
- `bool Expand` = `false`
- `bool Loop` = `false`
- `bool Paused` = `false`
- `float SpeedScale` = `1.0`
- `VideoStream Stream`
- `float StreamPosition`
- `float Volume`
- `float VolumeDb` = `0.0`

**Methods**
- `float GetStreamLength()`
- `string GetStreamName()`
- `Texture2D GetVideoTexture()`
- `bool IsPlaying()`
- `void Play()`
- `void Stop()`

### Window
*Inherits: **Viewport < Node < Object** | Inherited by: AcceptDialog, Popup*

A node that creates a window. The window can either be a native system window or embedded inside another Window (see Viewport.gui_embed_subwindows).

**Properties**
- `string AccessibilityDescription` = `""`
- `string AccessibilityName` = `""`
- `bool AlwaysOnTop` = `false`
- `bool AutoTranslate`
- `bool Borderless` = `false`
- `ContentScaleAspect ContentScaleAspect` = `0`
- `float ContentScaleFactor` = `1.0`
- `ContentScaleMode ContentScaleMode` = `0`
- `Vector2i ContentScaleSize` = `Vector2i(0, 0)`
- `ContentScaleStretch ContentScaleStretch` = `0`
- `int CurrentScreen`
- `bool ExcludeFromCapture` = `false`
- `bool Exclusive` = `false`
- `bool ExtendToTitle` = `false`
- `bool ForceNative` = `false`
- `WindowInitialPosition InitialPosition` = `0`
- `bool KeepTitleVisible` = `false`
- `Vector2i MaxSize` = `Vector2i(0, 0)`
- `bool MaximizeDisabled` = `false`
- `Vector2i MinSize` = `Vector2i(0, 0)`
- `bool MinimizeDisabled` = `false`
- `Mode Mode` = `0`
- `bool MousePassthrough` = `false`
- `PackedVector2Array MousePassthroughPolygon` = `PackedVector2Array()`
- `Rect2i NonclientArea` = `Rect2i(0, 0, 0, 0)`
- `bool PopupWindow` = `false`
- `bool PopupWmHint` = `false`
- `Vector2i Position` = `Vector2i(0, 0)`
- `bool SharpCorners` = `false`
- `Vector2i Size` = `Vector2i(100, 100)`

**Methods**
- `Vector2 _GetContentsMinimumSize() [virtual]`
- `void AddThemeColorOverride(StringName name, Color color)`
- `void AddThemeConstantOverride(StringName name, int constant)`
- `void AddThemeFontOverride(StringName name, Font font)`
- `void AddThemeFontSizeOverride(StringName name, int fontSize)`
- `void AddThemeIconOverride(StringName name, Texture2D texture)`
- `void AddThemeStyleboxOverride(StringName name, StyleBox stylebox)`
- `void BeginBulkThemeOverride()`
- `bool CanDraw()`
- `void ChildControlsChanged()`
- `void EndBulkThemeOverride()`
- `Vector2 GetContentsMinimumSize()`
- `bool GetFlag(Flags flag)`
- `Window GetFocusedWindow() [static]`
- `LayoutDirection GetLayoutDirection()`
- `Vector2i GetPositionWithDecorations()`
- `Vector2i GetSizeWithDecorations()`
- `Color GetThemeColor(StringName name, StringName themeType = &"")`
- `int GetThemeConstant(StringName name, StringName themeType = &"")`
- `float GetThemeDefaultBaseScale()`
- `Font GetThemeDefaultFont()`
- `int GetThemeDefaultFontSize()`
- `Font GetThemeFont(StringName name, StringName themeType = &"")`
- `int GetThemeFontSize(StringName name, StringName themeType = &"")`
- `Texture2D GetThemeIcon(StringName name, StringName themeType = &"")`
- `StyleBox GetThemeStylebox(StringName name, StringName themeType = &"")`
- `int GetWindowId()`
- `void GrabFocus()`
- `bool HasFocus()`
- `bool HasThemeColor(StringName name, StringName themeType = &"")`
- `bool HasThemeColorOverride(StringName name)`
- `bool HasThemeConstant(StringName name, StringName themeType = &"")`
- `bool HasThemeConstantOverride(StringName name)`
- `bool HasThemeFont(StringName name, StringName themeType = &"")`
- `bool HasThemeFontOverride(StringName name)`
- `bool HasThemeFontSize(StringName name, StringName themeType = &"")`
- `bool HasThemeFontSizeOverride(StringName name)`
- `bool HasThemeIcon(StringName name, StringName themeType = &"")`
- `bool HasThemeIconOverride(StringName name)`
- `bool HasThemeStylebox(StringName name, StringName themeType = &"")`

**C# Examples**
```csharp
// Set region, using Path2D node.
GetNode<Window>("Window").MousePassthroughPolygon = GetNode<Path2D>("Path2D").Curve.GetBakedPoints();

// Set region, using Polygon2D node.
GetNode<Window>("Window").MousePassthroughPolygon = GetNode<Polygon2D>("Polygon2D").Polygon;

// Reset region to default.
GetNode<Window>("Window").MousePassthroughPolygon = [];
```
