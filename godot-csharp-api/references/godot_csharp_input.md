# Godot 4 C# API Reference — Input

> C#-only reference. 18 classes.

### InputEventAction
*Inherits: **InputEvent < Resource < RefCounted < Object***

Contains a generic action which can be targeted from several types of inputs. Actions and their events can be set in the Input Map tab in Project > Project Settings, or with the InputMap class.

**Properties**
- `StringName Action` = `&""`
- `int EventIndex` = `-1`
- `bool Pressed` = `false`
- `float Strength` = `1.0`

### InputEventFromWindow
*Inherits: **InputEvent < Resource < RefCounted < Object** | Inherited by: InputEventScreenDrag, InputEventScreenTouch, InputEventWithModifiers*

InputEventFromWindow represents events specifically received by windows. This includes mouse events, keyboard events in focused windows or touch screen actions.

**Properties**
- `int WindowId` = `0`

### InputEventGesture
*Inherits: **InputEventWithModifiers < InputEventFromWindow < InputEvent < Resource < RefCounted < Object** | Inherited by: InputEventMagnifyGesture, InputEventPanGesture*

InputEventGestures are sent when a user performs a supported gesture on a touch screen. Gestures can't be emulated using mouse, because they typically require multi-touch.

**Properties**
- `Vector2 Position` = `Vector2(0, 0)`

### InputEventJoypadButton
*Inherits: **InputEvent < Resource < RefCounted < Object***

Input event type for gamepad buttons. For gamepad analog sticks and joysticks, see InputEventJoypadMotion.

**Properties**
- `JoyButton ButtonIndex` = `0`
- `bool Pressed` = `false`
- `float Pressure` = `0.0`

### InputEventJoypadMotion
*Inherits: **InputEvent < Resource < RefCounted < Object***

Stores information about joystick motions. One InputEventJoypadMotion represents one axis at a time. For gamepad buttons, see InputEventJoypadButton.

**Properties**
- `JoyAxis Axis` = `0`
- `float AxisValue` = `0.0`

### InputEventKey
*Inherits: **InputEventWithModifiers < InputEventFromWindow < InputEvent < Resource < RefCounted < Object***

An input event for keys on a keyboard. Supports key presses, key releases and echo events. It can also be received in Node._unhandled_key_input().

**Properties**
- `bool Echo` = `false`
- `Key KeyLabel` = `0`
- `Key Keycode` = `0`
- `KeyLocation Location` = `0`
- `Key PhysicalKeycode` = `0`
- `bool Pressed` = `false`
- `int Unicode` = `0`

**Methods**
- `string AsTextKeyLabel()`
- `string AsTextKeycode()`
- `string AsTextLocation()`
- `string AsTextPhysicalKeycode()`
- `Key GetKeyLabelWithModifiers()`
- `Key GetKeycodeWithModifiers()`
- `Key GetPhysicalKeycodeWithModifiers()`

**C# Examples**
```csharp
public override void _Input(InputEvent @event)
{
    if (@event is InputEventKey inputEventKey)
    {
        var keycode = DisplayServer.KeyboardGetKeycodeFromPhysical(inputEventKey.PhysicalKeycode);
        var label = DisplayServer.KeyboardGetLabelFromPhysical(inputEventKey.PhysicalKeycode);
        GD.Print(OS.GetKeycodeString(keycode));
        GD.Print(OS.GetKeycodeString(label));
    }
}
```

### InputEventMIDI
*Inherits: **InputEvent < Resource < RefCounted < Object***

InputEventMIDI stores information about messages from MIDI (Musical Instrument Digital Interface) devices. These may include musical keyboards, synthesizers, and drum machines.

**Properties**
- `int Channel` = `0`
- `int ControllerNumber` = `0`
- `int ControllerValue` = `0`
- `int Instrument` = `0`
- `MIDIMessage Message` = `0`
- `int Pitch` = `0`
- `int Pressure` = `0`
- `int Velocity` = `0`

**C# Examples**
```csharp
public override void _Ready()
{
    OS.OpenMidiInputs();
    GD.Print(OS.GetConnectedMidiInputs());
}

public override void _Input(InputEvent inputEvent)
{
    if (inputEvent is InputEventMidi midiEvent)
    {
        PrintMIDIInfo(midiEvent);
    }
}

private void PrintMIDIInfo(InputEventMidi midiEvent)
{
    GD.Print(midiEvent);
    GD.Print($"Channel {midiEvent.Channel}");
    GD.Print($"Message {midiEvent.Message}");
    GD.Print($"Pitch {midiEvent.Pitch}");
    GD.Print($"Velocity {midiEvent.Velocity}");
    GD.Print($"Instrument {midiEvent.Instrument}");
    GD.Print($"Pressure {midiEven
// ...
```

### InputEventMagnifyGesture
*Inherits: **InputEventGesture < InputEventWithModifiers < InputEventFromWindow < InputEvent < Resource < RefCounted < Object***

Stores the factor of a magnifying touch gesture. This is usually performed when the user pinches the touch screen and used for zooming in/out.

**Properties**
- `float Factor` = `1.0`

### InputEventMouseButton
*Inherits: **InputEventMouse < InputEventWithModifiers < InputEventFromWindow < InputEvent < Resource < RefCounted < Object***

Stores information about mouse click events. See Node._input().

**Properties**
- `MouseButton ButtonIndex` = `0`
- `bool Canceled` = `false`
- `bool DoubleClick` = `false`
- `float Factor` = `1.0`
- `bool Pressed` = `false`

### InputEventMouseMotion
*Inherits: **InputEventMouse < InputEventWithModifiers < InputEventFromWindow < InputEvent < Resource < RefCounted < Object***

Stores information about a mouse or a pen motion. This includes relative position, absolute position, and velocity. See Node._input().

**Properties**
- `bool PenInverted` = `false`
- `float Pressure` = `0.0`
- `Vector2 Relative` = `Vector2(0, 0)`
- `Vector2 ScreenRelative` = `Vector2(0, 0)`
- `Vector2 ScreenVelocity` = `Vector2(0, 0)`
- `Vector2 Tilt` = `Vector2(0, 0)`
- `Vector2 Velocity` = `Vector2(0, 0)`

### InputEventMouse
*Inherits: **InputEventWithModifiers < InputEventFromWindow < InputEvent < Resource < RefCounted < Object** | Inherited by: InputEventMouseButton, InputEventMouseMotion*

Stores general information about mouse events.

**Properties**
- `BitField[MouseButtonMask] ButtonMask` = `0`
- `Vector2 GlobalPosition` = `Vector2(0, 0)`
- `Vector2 Position` = `Vector2(0, 0)`

### InputEventPanGesture
*Inherits: **InputEventGesture < InputEventWithModifiers < InputEventFromWindow < InputEvent < Resource < RefCounted < Object***

Stores information about pan gestures. A pan gesture is performed when the user swipes the touch screen with two fingers. It's typically used for panning/scrolling.

**Properties**
- `Vector2 Delta` = `Vector2(0, 0)`

### InputEventScreenDrag
*Inherits: **InputEventFromWindow < InputEvent < Resource < RefCounted < Object***

Stores information about screen drag events. See Node._input().

**Properties**
- `int Index` = `0`
- `bool PenInverted` = `false`
- `Vector2 Position` = `Vector2(0, 0)`
- `float Pressure` = `0.0`
- `Vector2 Relative` = `Vector2(0, 0)`
- `Vector2 ScreenRelative` = `Vector2(0, 0)`
- `Vector2 ScreenVelocity` = `Vector2(0, 0)`
- `Vector2 Tilt` = `Vector2(0, 0)`
- `Vector2 Velocity` = `Vector2(0, 0)`

### InputEventScreenTouch
*Inherits: **InputEventFromWindow < InputEvent < Resource < RefCounted < Object***

Stores information about multi-touch press/release input events. Supports touch press, touch release and index for multi-touch count and order.

**Properties**
- `bool Canceled` = `false`
- `bool DoubleTap` = `false`
- `int Index` = `0`
- `Vector2 Position` = `Vector2(0, 0)`
- `bool Pressed` = `false`

### InputEventShortcut
*Inherits: **InputEvent < Resource < RefCounted < Object***

InputEventShortcut is a special event that can be received in Node._input(), Node._shortcut_input(), and Node._unhandled_input(). It is typically sent by the editor's Command Palette to trigger actions, but can also be sent manually using Viewport.push_input().

**Properties**
- `Shortcut Shortcut`

### InputEventWithModifiers
*Inherits: **InputEventFromWindow < InputEvent < Resource < RefCounted < Object** | Inherited by: InputEventGesture, InputEventKey, InputEventMouse*

Stores information about mouse, keyboard, and touch gesture input events. This includes information about which modifier keys are pressed, such as Shift or Alt. See Node._input().

**Properties**
- `bool AltPressed` = `false`
- `bool CommandOrControlAutoremap` = `false`
- `bool CtrlPressed` = `false`
- `bool MetaPressed` = `false`
- `bool ShiftPressed` = `false`

**Methods**
- `BitField[KeyModifierMask] GetModifiersMask()`
- `bool IsCommandOrControlPressed()`

### InputEvent
*Inherits: **Resource < RefCounted < Object** | Inherited by: InputEventAction, InputEventFromWindow, InputEventJoypadButton, InputEventJoypadMotion, InputEventMIDI, InputEventShortcut*

Abstract base class of all types of input events. See Node._input().

**Properties**
- `int Device` = `0`

**Methods**
- `bool Accumulate(InputEvent withEvent)`
- `string AsText()`
- `float GetActionStrength(StringName action, bool exactMatch = false)`
- `bool IsAction(StringName action, bool exactMatch = false)`
- `bool IsActionPressed(StringName action, bool allowEcho = false, bool exactMatch = false)`
- `bool IsActionReleased(StringName action, bool exactMatch = false)`
- `bool IsActionType()`
- `bool IsCanceled()`
- `bool IsEcho()`
- `bool IsMatch(InputEvent event, bool exactMatch = true)`
- `bool IsPressed()`
- `bool IsReleased()`
- `InputEvent XformedBy(Transform2D xform, Vector2 localOfs = Vector2(0, 0))`

### InputMap
*Inherits: **Object***

Manages all InputEventAction which can be created/modified from the project settings menu Project > Project Settings > Input Map or in code with add_action() and action_add_event(). See Node._input().

**Methods**
- `void ActionAddEvent(StringName action, InputEvent event)`
- `void ActionEraseEvent(StringName action, InputEvent event)`
- `void ActionEraseEvents(StringName action)`
- `float ActionGetDeadzone(StringName action)`
- `Array[InputEvent] ActionGetEvents(StringName action)`
- `bool ActionHasEvent(StringName action, InputEvent event)`
- `void ActionSetDeadzone(StringName action, float deadzone)`
- `void AddAction(StringName action, float deadzone = 0.2)`
- `void EraseAction(StringName action)`
- `bool EventIsAction(InputEvent event, StringName action, bool exactMatch = false)`
- `string GetActionDescription(StringName action)`
- `Array[StringName] GetActions()`
- `bool HasAction(StringName action)`
- `void LoadFromProjectSettings()`
