# Godot 4 GDScript API Reference — Input

> GDScript-only reference. 18 classes.

### InputEventAction
*Inherits: **InputEvent < Resource < RefCounted < Object***

Contains a generic action which can be targeted from several types of inputs. Actions and their events can be set in the Input Map tab in Project > Project Settings, or with the InputMap class.

**Properties**
- `StringName action` = `&""`
- `int event_index` = `-1`
- `bool pressed` = `false`
- `float strength` = `1.0`

### InputEventFromWindow
*Inherits: **InputEvent < Resource < RefCounted < Object** | Inherited by: InputEventScreenDrag, InputEventScreenTouch, InputEventWithModifiers*

InputEventFromWindow represents events specifically received by windows. This includes mouse events, keyboard events in focused windows or touch screen actions.

**Properties**
- `int window_id` = `0`

### InputEventGesture
*Inherits: **InputEventWithModifiers < InputEventFromWindow < InputEvent < Resource < RefCounted < Object** | Inherited by: InputEventMagnifyGesture, InputEventPanGesture*

InputEventGestures are sent when a user performs a supported gesture on a touch screen. Gestures can't be emulated using mouse, because they typically require multi-touch.

**Properties**
- `Vector2 position` = `Vector2(0, 0)`

### InputEventJoypadButton
*Inherits: **InputEvent < Resource < RefCounted < Object***

Input event type for gamepad buttons. For gamepad analog sticks and joysticks, see InputEventJoypadMotion.

**Properties**
- `JoyButton button_index` = `0`
- `bool pressed` = `false`
- `float pressure` = `0.0`

### InputEventJoypadMotion
*Inherits: **InputEvent < Resource < RefCounted < Object***

Stores information about joystick motions. One InputEventJoypadMotion represents one axis at a time. For gamepad buttons, see InputEventJoypadButton.

**Properties**
- `JoyAxis axis` = `0`
- `float axis_value` = `0.0`

### InputEventKey
*Inherits: **InputEventWithModifiers < InputEventFromWindow < InputEvent < Resource < RefCounted < Object***

An input event for keys on a keyboard. Supports key presses, key releases and echo events. It can also be received in Node._unhandled_key_input().

**Properties**
- `bool echo` = `false`
- `Key key_label` = `0`
- `Key keycode` = `0`
- `KeyLocation location` = `0`
- `Key physical_keycode` = `0`
- `bool pressed` = `false`
- `int unicode` = `0`

**Methods**
- `String as_text_key_label() const`
- `String as_text_keycode() const`
- `String as_text_location() const`
- `String as_text_physical_keycode() const`
- `Key get_key_label_with_modifiers() const`
- `Key get_keycode_with_modifiers() const`
- `Key get_physical_keycode_with_modifiers() const`

**GDScript Examples**
```gdscript
func _input(event):
    if event is InputEventKey:
        var keycode = DisplayServer.keyboard_get_keycode_from_physical(event.physical_keycode)
        var label = DisplayServer.keyboard_get_label_from_physical(event.physical_keycode)
        print(OS.get_keycode_string(keycode))
        print(OS.get_keycode_string(label))
```

### InputEventMIDI
*Inherits: **InputEvent < Resource < RefCounted < Object***

InputEventMIDI stores information about messages from MIDI (Musical Instrument Digital Interface) devices. These may include musical keyboards, synthesizers, and drum machines.

**Properties**
- `int channel` = `0`
- `int controller_number` = `0`
- `int controller_value` = `0`
- `int instrument` = `0`
- `MIDIMessage message` = `0`
- `int pitch` = `0`
- `int pressure` = `0`
- `int velocity` = `0`

**GDScript Examples**
```gdscript
func _ready():
    OS.open_midi_inputs()
    print(OS.get_connected_midi_inputs())

func _input(input_event):
    if input_event is InputEventMIDI:
        _print_midi_info(input_event)

func _print_midi_info(midi_event):
    print(midi_event)
    print("Channel ", midi_event.channel)
    print("Message ", midi_event.message)
    print("Pitch ", midi_event.pitch)
    print("Velocity ", midi_event.velocity)
    print("Instrument ", midi_event.instrument)
    print("Pressure ", midi_event.pressure)
    print("Controller number: ", midi_event.controller_number)
    print("Controller value: ", mid
# ...
```
```gdscript
func _input(event):
    if event is InputEventMIDI:
        if event.message == MIDI_MESSAGE_NOTE_ON and event.velocity > 0:
            print("Note pressed!")
```

### InputEventMagnifyGesture
*Inherits: **InputEventGesture < InputEventWithModifiers < InputEventFromWindow < InputEvent < Resource < RefCounted < Object***

Stores the factor of a magnifying touch gesture. This is usually performed when the user pinches the touch screen and used for zooming in/out.

**Properties**
- `float factor` = `1.0`

### InputEventMouseButton
*Inherits: **InputEventMouse < InputEventWithModifiers < InputEventFromWindow < InputEvent < Resource < RefCounted < Object***

Stores information about mouse click events. See Node._input().

**Properties**
- `MouseButton button_index` = `0`
- `bool canceled` = `false`
- `bool double_click` = `false`
- `float factor` = `1.0`
- `bool pressed` = `false`

### InputEventMouseMotion
*Inherits: **InputEventMouse < InputEventWithModifiers < InputEventFromWindow < InputEvent < Resource < RefCounted < Object***

Stores information about a mouse or a pen motion. This includes relative position, absolute position, and velocity. See Node._input().

**Properties**
- `bool pen_inverted` = `false`
- `float pressure` = `0.0`
- `Vector2 relative` = `Vector2(0, 0)`
- `Vector2 screen_relative` = `Vector2(0, 0)`
- `Vector2 screen_velocity` = `Vector2(0, 0)`
- `Vector2 tilt` = `Vector2(0, 0)`
- `Vector2 velocity` = `Vector2(0, 0)`

### InputEventMouse
*Inherits: **InputEventWithModifiers < InputEventFromWindow < InputEvent < Resource < RefCounted < Object** | Inherited by: InputEventMouseButton, InputEventMouseMotion*

Stores general information about mouse events.

**Properties**
- `BitField[MouseButtonMask] button_mask` = `0`
- `Vector2 global_position` = `Vector2(0, 0)`
- `Vector2 position` = `Vector2(0, 0)`

### InputEventPanGesture
*Inherits: **InputEventGesture < InputEventWithModifiers < InputEventFromWindow < InputEvent < Resource < RefCounted < Object***

Stores information about pan gestures. A pan gesture is performed when the user swipes the touch screen with two fingers. It's typically used for panning/scrolling.

**Properties**
- `Vector2 delta` = `Vector2(0, 0)`

### InputEventScreenDrag
*Inherits: **InputEventFromWindow < InputEvent < Resource < RefCounted < Object***

Stores information about screen drag events. See Node._input().

**Properties**
- `int index` = `0`
- `bool pen_inverted` = `false`
- `Vector2 position` = `Vector2(0, 0)`
- `float pressure` = `0.0`
- `Vector2 relative` = `Vector2(0, 0)`
- `Vector2 screen_relative` = `Vector2(0, 0)`
- `Vector2 screen_velocity` = `Vector2(0, 0)`
- `Vector2 tilt` = `Vector2(0, 0)`
- `Vector2 velocity` = `Vector2(0, 0)`

### InputEventScreenTouch
*Inherits: **InputEventFromWindow < InputEvent < Resource < RefCounted < Object***

Stores information about multi-touch press/release input events. Supports touch press, touch release and index for multi-touch count and order.

**Properties**
- `bool canceled` = `false`
- `bool double_tap` = `false`
- `int index` = `0`
- `Vector2 position` = `Vector2(0, 0)`
- `bool pressed` = `false`

### InputEventShortcut
*Inherits: **InputEvent < Resource < RefCounted < Object***

InputEventShortcut is a special event that can be received in Node._input(), Node._shortcut_input(), and Node._unhandled_input(). It is typically sent by the editor's Command Palette to trigger actions, but can also be sent manually using Viewport.push_input().

**Properties**
- `Shortcut shortcut`

### InputEventWithModifiers
*Inherits: **InputEventFromWindow < InputEvent < Resource < RefCounted < Object** | Inherited by: InputEventGesture, InputEventKey, InputEventMouse*

Stores information about mouse, keyboard, and touch gesture input events. This includes information about which modifier keys are pressed, such as Shift or Alt. See Node._input().

**Properties**
- `bool alt_pressed` = `false`
- `bool command_or_control_autoremap` = `false`
- `bool ctrl_pressed` = `false`
- `bool meta_pressed` = `false`
- `bool shift_pressed` = `false`

**Methods**
- `BitField[KeyModifierMask] get_modifiers_mask() const`
- `bool is_command_or_control_pressed() const`

### InputEvent
*Inherits: **Resource < RefCounted < Object** | Inherited by: InputEventAction, InputEventFromWindow, InputEventJoypadButton, InputEventJoypadMotion, InputEventMIDI, InputEventShortcut*

Abstract base class of all types of input events. See Node._input().

**Properties**
- `int device` = `0`

**Methods**
- `bool accumulate(with_event: InputEvent)`
- `String as_text() const`
- `float get_action_strength(action: StringName, exact_match: bool = false) const`
- `bool is_action(action: StringName, exact_match: bool = false) const`
- `bool is_action_pressed(action: StringName, allow_echo: bool = false, exact_match: bool = false) const`
- `bool is_action_released(action: StringName, exact_match: bool = false) const`
- `bool is_action_type() const`
- `bool is_canceled() const`
- `bool is_echo() const`
- `bool is_match(event: InputEvent, exact_match: bool = true) const`
- `bool is_pressed() const`
- `bool is_released() const`
- `InputEvent xformed_by(xform: Transform2D, local_ofs: Vector2 = Vector2(0, 0)) const`

### InputMap
*Inherits: **Object***

Manages all InputEventAction which can be created/modified from the project settings menu Project > Project Settings > Input Map or in code with add_action() and action_add_event(). See Node._input().

**Methods**
- `void action_add_event(action: StringName, event: InputEvent)`
- `void action_erase_event(action: StringName, event: InputEvent)`
- `void action_erase_events(action: StringName)`
- `float action_get_deadzone(action: StringName)`
- `Array[InputEvent] action_get_events(action: StringName)`
- `bool action_has_event(action: StringName, event: InputEvent)`
- `void action_set_deadzone(action: StringName, deadzone: float)`
- `void add_action(action: StringName, deadzone: float = 0.2)`
- `void erase_action(action: StringName)`
- `bool event_is_action(event: InputEvent, action: StringName, exact_match: bool = false) const`
- `String get_action_description(action: StringName) const`
- `Array[StringName] get_actions()`
- `bool has_action(action: StringName) const`
- `void load_from_project_settings()`
