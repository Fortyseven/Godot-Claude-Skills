# Godot 4 GDScript Tutorials — Audio

> 6 tutorials. GDScript-specific code examples.

## Audio buses

### Introduction

Godot's audio processing code has been written with games in mind, with the aim of achieving an optimal balance between performance and sound quality.

Godot's audio engine allows any number of audio buses to be created and any number of effect processors can be added to each bus. Only the hardware of the device running your game will limit the number of buses and effects that can be used before performance starts to suffer.

### Decibel scale

Godot's sound interface is designed to meet the expectations of sound design professionals. To this end, it primarily uses the decibel scale.

For those unfamiliar with it, it can be explained with a few facts:

- The decibel (dB) scale is a relative scale. It represents the ratio of sound power by using 20 times the base 10 logarithm of the ratio (20 × log10(P/P0)).
- For every 6 dB, sound amplitude doubles or halves. 12 dB represents a factor of 4, 18 dB a factor of 8, 20 dB a factor of 10, 40 dB a factor of 100, etc.
- Since the scale is logarithmic, true zero (no audio) can't be represented.
- 0 dB is the maximum amplitude possible in a digital audio system. This limit is not the human limit, but a limit from the sound hardware. Audio with amplitudes that are too high to be represented properly below 0 dB create a kind of distortion called _clipping_.
- To avoid clipping, your sound mix should be arranged so that the output of the _master bus_ (more on that later) never exceeds 0 dB.
- Every 6 dB below the 0 dB limit, sound energy is _halved_. It means the sound volume at -6 dB is half as loud as 0dB. -12 dB is half as loud as -6 dB and so on.
- When working with decibels, sound is considered no longer audible between -60 dB and -80 dB. This makes your working range generally between -60 dB and 0 dB.

This can take a bit getting used to, but it's friendlier in the end and will allow you to communicate better with audio professionals.

### Audio buses

Audio buses can be found in the bottom panel of the Godot editor:

An _audio bus_ (also called an _audio channel_) can be considered a place that audio is channeled through on the way to playback through a device's speakers. Audio data can be _modified_ and _re-routed_ by an audio bus. An audio bus has a VU meter (the bars that light up when sound is played) which indicates the amplitude of the signal passing through.

The leftmost bus is the _master bus_. This bus outputs the mix to your speakers so, as mentioned in the _Decibel scale_ section above, make sure that your mix level doesn't reach 0 dB in this bus. The rest of the audio buses can be flexibly routed. After modifying the sound, they send it to another bus to the left. The destination bus can be specified for each of the non-master audio buses. Routing always passes audio from buses on the right to buses further to the left. This avoids infinite routing loops.

In the above image, the output of _Bus 2_ has been routed to the _Master_ bus.

### Playback of audio through a bus

To test passing audio to a bus, create an AudioStreamPlayer node, load an AudioStream and select a target bus for playback:

Finally, toggle the **Playing** property to **On** and sound will flow.

> **See also:** You may also be interested in reading about Audio streams now.

### Adding effects

> **Warning:** This feature is not supported on the web platform if the AudioStreamPlayer's playback mode is set to **Sample**, which is the default. It will only work if the playback mode is set to **Stream**, at the cost of increased latency if threads are not enabled. See [Audio playback in the Exporting for the Web documentation](tutorials_export.md) for details.

Audio buses can contain all sorts of effects. These effects modify the sound in one way or another and are applied in order.

For information on what each effect does, see Audio effects.

### Automatic bus disabling

There is no need to disable buses manually when not in use. Godot detects that the bus has been silent for a few seconds and disables it (including all effects).

### Bus rearrangement

Stream Players use bus names to identify a bus, which allows adding, removing and moving buses around while the reference to them is kept. However, if a bus is renamed, the reference will be lost and the Stream Player will output to Master. This system was chosen because rearranging buses is a more common process than renaming them.

### Default bus layout

The default bus layout is automatically saved to the `res://default_bus_layout.tres` file. Custom bus arrangements can be saved and loaded from disk.

---

## Audio effects

Godot includes several audio effects that can be added to an audio bus to alter every sound file that goes through that bus.

Try them all out to get a sense of how they alter sound. Here follows a short description of the available effects:

### Amplify

Amplify changes the volume of the signal. Some care needs to be taken, though: setting the level too high can make the sound digitally clip, which can produce unpleasant crackles and pops.

### BandLimit and BandPass

These are resonant filters which block frequencies around the _Cutoff_ point. BandPass can be used to simulate sound passing through an old telephone line or megaphone. Modulating the BandPass frequency can simulate the sound of a wah-wah guitar pedal, think of the guitar in Jimi Hendrix's _Voodoo Child (Slight Return)_.

### Capture

The Capture effect copies the audio frames of the audio bus that it is on into an internal buffer. This can be used to capture data from the microphone or to transmit audio over the network in real-time.

### Chorus

As the name of the effect implies, the Chorus effect makes a single audio sample sound like an entire chorus. It does this by duplicating a signal and very slightly altering the timing and pitch of each duplicate, and varying that over time via an LFO (low frequency oscillator). The duplicate(s) are then mixed back together with the original signal, producing a lush, wide, and large sound. Although chorus is traditionally used for voices, it can be desirable with almost any type of sound.

### Compressor

A dynamic range compressor automatically attenuates (ducks) the level of the incoming signal when its amplitude exceeds a certain threshold. The level of attenuation applied is proportional to how far the incoming audio exceeds the threshold. The compressor's Ratio parameter controls the degree of attenuation. One of the main uses of a compressor is to reduce the dynamic range of signals with very loud and quiet parts. Reducing the dynamic range of a signal can make it fit more comfortably in a mix.

The compressor has many uses. For example:

- It can be used in the Master bus to compress the whole output prior to being hit by a limiter, making the effect of the limiter much more subtle.
- It can be used in voice channels to ensure they sound as even as possible.
- It can be _sidechained_ by another sound source. This means it can reduce the sound level of one signal using the level of another audio bus for threshold detection. This technique is very common in video game mixing to "duck" the level of music or sound effects when in-game or multiplayer voices need to be fully audible.
- It can accentuate transients by using a slower attack. This can make sound effects more punchy.

> **Note:** If your goal is to prevent a signal from exceeding a given amplitude altogether, rather than to reduce the dynamic range of the signal, a **limiter** is likely a better choice than a compressor for this purpose. However, applying compression before a limiter is still good practice.

### Delay

Digital delay essentially duplicates a signal and repeats it at a specified speed with a volume level that decays for each repeat. Delay is great for simulating the acoustic space of a canyon or large room, where sound bounces have a lot of _delay_ between their repeats. This is in contrast to reverb, which has a more natural and blurred sound to it. Using this in conjunction with reverb can create very natural sounding environments!

### Distortion

Makes the sound distorted. Godot offers several types of distortion:

- _Overdrive_ sounds like a guitar distortion pedal or megaphone. Sounds distorted with this sound like they're coming through a low-quality speaker or device.
- _Tan_ sounds like another interesting flavor of overdrive.
- _Bit crushing_ clamps the amplitude of the signal, making it sound flat and crunchy.

All three types of distortion can add higher frequency sounds to an original sound, making it stand out better in a mix.

### EQ

EQ is what all other equalizers inherit from. It can be extended with Custom scripts to create an equalizer with a custom number of bands.

### EQ6, EQ10, EQ21

Godot provides three equalizers with different numbers of bands, which are represented in the title (6, 10, and 21 bands, respectively). An equalizer on the Master bus can be useful for cutting low and high frequencies that the device's speakers can't reproduce well. For example, phone or tablet speakers usually don't reproduce low frequency sounds well, and could make a limiter or compressor attenuate sounds that aren't even audible to the user anyway.

Note: The equalizer effect can be disabled when headphones are plugged in, giving the user the best of both worlds.

### Filter

Filter is what all other filters inherit from and should not be used directly.

### HardLimiter

A limiter is similar to a compressor, but it's less flexible and designed to prevent a signal's amplitude exceeding a given dB threshold. Adding a limiter to the final point of the Master bus is good practice, as it offers an easy safeguard against clipping.

### HighPassFilter

Cuts frequencies below a specific _Cutoff_ frequency. HighPassFilter is used to reduce the bass content of a signal.

### HighShelfFilter

Reduces all frequencies above a specific _Cutoff_ frequency.

### Limiter

This is the old limiter effect, and it is recommended to use the new HardLimiter effect instead.

Here is an example of how this effect works, if the ceiling is set to -12 dB, and the threshold is 0 dB, all samples going through get reduced by 12dB. This changes the waveform of the sound and introduces distortion.

This effect is being kept to preserve compatibility, however it should be considered deprecated.

### LowPassFilter

Cuts frequencies above a specific _Cutoff_ frequency and can also resonate (boost frequencies close to the _Cutoff_ frequency). Low pass filters can be used to simulate "muffled" sound. For instance, underwater sounds, sounds blocked by walls, or distant sounds.

### LowShelfFilter

Reduces all frequencies below a specific _Cutoff_ frequency.

### NotchFilter

The opposite of the BandPassFilter, it removes a band of sound from the frequency spectrum at a given _Cutoff_ frequency.

### Panner

The Panner allows the stereo balance of a signal to be adjusted between the left and right channels. Headphones are recommended when configuring in this effect.

### Phaser

This effect is formed by de-phasing two duplicates of the same sound so they cancel each other out in an interesting way. Phaser produces a pleasant whooshing sound that moves back and forth through the audio spectrum, and can be a great way to create sci-fi effects or Darth Vader-like voices.

### PitchShift

This effect allows the adjustment of the signal's pitch independently of its speed. All frequencies can be increased/decreased with minimal effect on transients. PitchShift can be useful to create unusually high or deep voices. Do note that altering pitch can sound unnatural when pushed outside of a narrow window.

### Record

The Record effect allows the user to record sound from a microphone.

### Reverb

Reverb simulates rooms of different sizes. It has adjustable parameters that can be tweaked to obtain the sound of a specific room. Reverb is commonly outputted from [Area3Ds](../godot_gdscript_physics.md) (see Reverb buses), or to apply a "chamber" feel to all sounds.

### SpectrumAnalyzer

This effect doesn't alter audio, instead, you add this effect to buses you want a spectrum analysis of. This would typically be used for audio visualization. Visualizing voices can be a great way to draw attention to them without just increasing their volume. A demo project using this can be found [here](https://github.com/godotengine/godot-demo-projects/tree/master/audio/spectrum).

### StereoEnhance

This effect uses a few algorithms to enhance a signal's stereo width.

---

## Audio streams

> **Work in progress:** The content of this page was not yet updated for Godot `4.6` and may be **outdated**. If you know how to improve this page or you can confirm that it's up to date, feel free to [open a pull request](https://github.com/godotengine/godot-docs).

### Introduction

As you might have already read in Audio buses, sound is sent to each bus via an AudioStreamPlayer node. There are different kinds of AudioStreamPlayers. Each one loads an AudioStream and plays it back.

### AudioStream

An audio stream is an abstract object that emits sound. The sound can come from many places, but is most commonly loaded from the filesystem. Audio files can be loaded as AudioStreams and placed inside an AudioStreamPlayer. You can find information on supported formats and differences in [Importing audio samples](tutorials_assets_pipeline.md).

There are other types of AudioStreams, such as [AudioStreamRandomizer](../godot_gdscript_audio.md). This one picks a different audio stream from a list of streams each time it's played back, and applies random pitch and volume shifting. This can be helpful for adding variation to sounds that are played back often.

### AudioStreamPlayer

This is the standard, non-positional stream player. It can play to any bus. In 5.1 sound setups, it can send audio to stereo mix or front speakers.

Playback Type is an experimental setting, and could change in future versions of Godot. It exists so Web exports use Web Audio-API based samples instead of streaming all sounds to the browser, unlike most platforms. This prevents the audio from being garbled in single-threaded Web exports. By default, only the Web platform will use samples. Changing this setting is not recommended, unless you have an explicit reason to. You can change the default playback type for the web and other platforms in the project settings under **Audio > General** (advanced settings must be turned on to see the setting).

### AudioStreamPlayer2D

This is a variant of AudioStreamPlayer, but emits sound in a 2D positional environment. When close to the left of the screen, the panning will go left. When close to the right side, it will go right.

> **Note:** Area2Ds can be used to divert sound from any AudioStreamPlayer2Ds they contain to specific buses. This makes it possible to create buses with different reverb or sound qualities to handle action happening in a particular parts of your game world.

### AudioStreamPlayer3D

This is a variant of AudioStreamPlayer, but emits sound in a 3D positional environment. Depending on the location of the player relative to the screen, it can position sound in stereo, 5.1 or 7.1 depending on the chosen audio setup.

Similar to AudioStreamPlayer2D, an Area3D can divert the sound to an audio bus.

Unlike for 2D, the 3D version of AudioStreamPlayer has a few more advanced options:

#### Reverb buses

> **Warning:** This feature is not supported on the web platform if the AudioStreamPlayer's playback mode is set to **Sample**, which is the default. It will only work if the playback mode is set to **Stream**, at the cost of increased latency if threads are not enabled. See [Audio playback in the Exporting for the Web documentation](tutorials_export.md) for details.

Godot allows for 3D audio streams that enter a specific Area3D node to send dry and wet audio to separate buses. This is useful when you have several reverb configurations for different types of rooms. This is done by enabling this type of reverb in the **Reverb Bus** section of the Area3D's properties:

At the same time, a special bus layout is created where each Area3D receives the reverb info from each Area3D. A Reverb effect needs to be created and configured in each reverb bus to complete the setup for the desired effect:

The Area3D's **Reverb Bus** section also has a parameter named **Uniformity**. Some types of rooms bounce sounds more than others (like a warehouse), so reverberation can be heard almost uniformly across the room even though the source may be far away. Playing around with this parameter can simulate that effect.

#### Doppler

> **Warning:** This feature is not supported on the web platform if the AudioStreamPlayer's playback mode is set to **Sample**, which is the default. It will only work if the playback mode is set to **Stream**, at the cost of increased latency if threads are not enabled. See [Audio playback in the Exporting for the Web documentation](tutorials_export.md) for details.

When the relative velocity between an emitter and listener changes, this is perceived as an increase or decrease in the pitch of the emitted sound. Godot can track velocity changes in the AudioStreamPlayer3D and Camera nodes. Both nodes have this property, which must be enabled manually:

Enable it by setting it depending on how objects will be moved: use **Idle** for objects moved using `_process`, or **Physics** for objects moved using `_physics_process`. The tracking will happen automatically.

---

## Recording with microphone

> **Work in progress:** The content of this page was not yet updated for Godot `4.6` and may be **outdated**. If you know how to improve this page or you can confirm that it's up to date, feel free to [open a pull request](https://github.com/godotengine/godot-docs).

Godot supports in-game audio recording for Windows, macOS, Linux, Android and iOS.

A simple demo is included in the official demo projects and will be used as support for this tutorial: [https://github.com/godotengine/godot-demo-projects/tree/master/audio/mic_record](https://github.com/godotengine/godot-demo-projects/tree/master/audio/mic_record).

You will need to enable audio input in the [Audio > Driver > Enable Input](../godot_gdscript_misc.md) project setting, or you'll just get empty audio files.

On iOS and iPadOS, it is also important to set the advanced **Audio > General > iOS > Session Category** setting to include **Record** or **Play and Record**.

### The structure of the demo

The demo consists of a single scene. This scene includes two major parts: the GUI and the audio.

We will focus on the audio part. In this demo, a bus named `Record` with the effect `Record` is created to handle the audio recording. An `AudioStreamPlayer` named `AudioStreamRecord` is used for recording.

```gdscript
var effect
var recording

func _ready():
    # We get the index of the "Record" bus.
    var idx = AudioServer.get_bus_index("Record")
    # And use it to retrieve its first effect, which has been defined
    # as an "AudioEffectRecord" resource.
    effect = AudioServer.get_bus_effect(idx, 0)
```

The audio recording is handled by the [AudioEffectRecord](../godot_gdscript_audio.md) resource which has three methods: [get_recording()](../godot_gdscript_misc.md), [is_recording_active()](../godot_gdscript_misc.md), and [set_recording_active()](../godot_gdscript_misc.md).

```gdscript
func _on_record_button_pressed():
    if effect.is_recording_active():
        recording = effect.get_recording()
        $PlayButton.disabled = false
        $SaveButton.disabled = false
        effect.set_recording_active(false)
        $RecordButton.text = "Record"
        $Status.text = ""
    else:
        $PlayButton.disabled = true
        $SaveButton.disabled = true
        effect.set_recording_active(true)
        $RecordButton.text = "Stop"
        $Status.text = "Recording..."
```

At the start of the demo, the recording effect is not active. When the user presses the `RecordButton`, the effect is enabled with `set_recording_active(true)`.

On the next button press, as `effect.is_recording_active()` is `true`, the recorded stream can be stored into the `recording` variable by calling `effect.get_recording()`.

```gdscript
func _on_play_button_pressed():
    print(recording)
    print(recording.format)
    print(recording.mix_rate)
    print(recording.stereo)
    var data = recording.get_data()
    print(data.size())
    $AudioStreamPlayer.stream = recording
    $AudioStreamPlayer.play()
```

To playback the recording, you assign the recording as the stream of the `AudioStreamPlayer` and call `play()`.

```gdscript
func _on_save_button_pressed():
    var save_path = $SaveButton/Filename.text
    recording.save_to_wav(save_path)
    $Status.text = "Saved WAV file to: %s\n(%s)" % [save_path, ProjectSettings.globalize_path(save_path)]
```

To save the recording, you call `save_to_wav()` with the path to a file. In this demo, the path is defined by the user via a `LineEdit` input box.

---

## Sync the gameplay with audio and music

> **Work in progress:** The content of this page was not yet updated for Godot `4.6` and may be **outdated**. If you know how to improve this page or you can confirm that it's up to date, feel free to [open a pull request](https://github.com/godotengine/godot-docs).

### Introduction

In any application or game, sound and music playback will have a slight delay. For games, this delay is often so small that it is negligible. Sound effects will come out a few milliseconds after any play() function is called. For music this does not matter as in most games it does not interact with the gameplay.

Still, for some games (mainly, rhythm games), it may be required to synchronize player actions with something happening in a song (usually in sync with the BPM). For this, having more precise timing information for an exact playback position is useful.

Achieving very low playback timing precision is difficult. This is because many factors are at play during audio playback:

- Audio is mixed in chunks (not continuously), depending on the size of audio buffers used (check latency in project settings).
- Mixed chunks of audio are not played immediately.
- Graphics APIs display two or three frames late.
- When playing on TVs, some delay may be added due to image processing.

The most common way to reduce latency is to shrink the audio buffers (again, by editing the latency setting in the project settings). The problem is that when latency is too small, sound mixing will require considerably more CPU. This increases the risk of skipping (a crack in sound because a mix callback was lost).

This is a common tradeoff, so Godot ships with sensible defaults that should not need to be altered.

The problem, in the end, is not this slight delay but synchronizing graphics and audio for games that require it. Some helpers are available to obtain more precise playback timing.

### Using the system clock to sync

As mentioned before, If you call [AudioStreamPlayer.play()](../godot_gdscript_audio.md), sound will not begin immediately, but when the audio thread processes the next chunk.

This delay can't be avoided but it can be estimated by calling [AudioServer.get_time_to_next_mix()](../godot_gdscript_audio.md).

The output latency (what happens after the mix) can also be estimated by calling [AudioServer.get_output_latency()](../godot_gdscript_audio.md).

Add these two and it's possible to guess almost exactly when sound or music will begin playing in the speakers during _\_process()_:

```gdscript
var time_begin
var time_delay

func _ready():
    time_begin = Time.get_ticks_usec()
    time_delay = AudioServer.get_time_to_next_mix() + AudioServer.get_output_latency()
    $Player.play()

func _process(delta):
    # Obtain from ticks.
    var time = (Time.get_ticks_usec() - time_begin) / 1000000.0
    # Compensate for latency.
    time -= time_delay
    # May be below 0 (did not begin yet).
    time = max(0, time)
    print("Time is: ", time)
```

In the long run, though, as the sound hardware clock is never exactly in sync with the system clock, the timing information will slowly drift away.

For a rhythm game where a song begins and ends after a few minutes, this approach is fine (and it's the recommended approach). For a game where playback can last a much longer time, the game will eventually go out of sync and a different approach is needed.

### Using the sound hardware clock to sync

Using [AudioStreamPlayer.get_playback_position()](../godot_gdscript_audio.md) to obtain the current position for the song sounds ideal, but it's not that useful as-is. This value will increment in chunks (every time the audio callback mixed a block of sound), so many calls can return the same value. Added to this, the value will be out of sync with the speakers too because of the previously mentioned reasons.

To compensate for the "chunked" output, there is a function that can help: [AudioServer.get_time_since_last_mix()](../godot_gdscript_audio.md).

Adding the return value from this function to _get_playback_position()_ increases precision:

```gdscript
var time = $Player.get_playback_position() + AudioServer.get_time_since_last_mix()
```

To increase precision, subtract the latency information (how much it takes for the audio to be heard after it was mixed):

```gdscript
var time = $Player.get_playback_position() + AudioServer.get_time_since_last_mix() - AudioServer.get_output_latency()
```

The result may be a bit jittery due how multiple threads work. Just check that the value is not less than in the previous frame (discard it if so). This is also a less precise approach than the one before, but it will work for songs of any length, or synchronizing anything (sound effects, as an example) to music.

Here is the same code as before using this approach:

```gdscript
func _ready():
    $Player.play()

func _process(delta):
    var time = $Player.get_playback_position() + AudioServer.get_time_since_last_mix()
    # Compensate for output latency.
    time -= AudioServer.get_output_latency()
    print("Time is: ", time)
```

---

## Text to speech

### Basic Usage

Basic usage of text-to-speech involves the following one-time steps:

- Enable TTS in the Godot editor for your project
- Query the system for a list of usable voices
- Store the ID of the voice you want to use

By default, the Godot project-level setting for text-to-speech is disabled, to avoid unnecessary overhead. To enable it:

- Go to **Project > Project Settings**
- Make sure the **Advanced Settings** toggle is enabled
- Click on **Audio > General**
- Ensure the **Text to Speech** option is checked
- Restart Godot if prompted to do so.

Text-to-speech uses a specific voice. Depending on the user's system, they might have multiple voices installed. Once you have the voice ID, you can use it to speak some text:

```gdscript
# One-time steps.
# Pick a voice. Here, we arbitrarily pick the first English voice.
var voices = DisplayServer.tts_get_voices_for_language("en")
var voice_id = voices[0]

# Say "Hello, world!".
DisplayServer.tts_speak("Hello, world!", voice_id)

# Say a longer sentence, and then interrupt it.
# Note that this method is asynchronous: execution proceeds to the next line immediately,
# before the voice finishes speaking.
var long_message = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur"
DisplayServer.tts_spea
# ...
```

### Requirements for functionality

Godot includes text-to-speech functionality. You can find these under the [DisplayServer class](../godot_gdscript_misc.md).

Godot depends on system libraries for text-to-speech functionality. These libraries are installed by default on Windows, macOS, Web, Android and iOS, but not on all Linux distributions. If they are not present, text-to-speech functionality will not work. Specifically, the `tts_get_voices()` method will return an empty list, indicating that there are no usable voices.

Both Godot users on Linux and end-users on Linux running Godot games need to ensure that their system includes the system libraries for text-to-speech to work. Please consult the table below or your own distribution's documentation to determine what libraries you need to install.

#### Distro-specific one-liners

| Arch Linux | pacman -S speech-dispatcher festival espeakup |

### Troubleshooting

If you get the error Invalid get index '0' (on base: 'PackedStringArray'). for the line var voice_id = voices[0], check if there are any items in voices. If not:

- All users: make sure you enabled **Text to Speech** in project settings
- Linux users: ensure you installed the system-specific libraries for text to speech

### Best practices

The best practices for text-to-speech, in terms of the ideal player experience for blind players, is to send output to the player's screen reader. This preserves the choice of language, speed, pitch, etc. that the user set, as well as allows advanced features like allowing players to scroll backward and forward through text. As of now, Godot doesn't provide this level of integration.

With the current state of the Godot text-to-speech APIs, best practices include:

- Develop the game with text-to-speech enabled, and ensure that everything sounds correct
- Allow players to control which voice to use, and save/persist that selection across game sessions
- Allow players to control the speech rate, and save/persist that selection across game sessions

This provides your blind players with the most flexibility and comfort available when not using a screen reader, and minimizes the chance of frustrating and alienating them.

### Caveats and Other Information

- Expect delays when you call tts_speak and tts_stop. The actual delay time varies depending on both the OS and on your machine's specifications. This is especially critical on Android and Web, where some of the voices depend on web services, and the actual time to playback depends on server load, network latency, and other factors.
- Non-English text works if the correct voices are installed and used. On Windows, you can consult the instructions in [this article](https://www.ghacks.net/2018/08/11/unlock-all-windows-10-tts-voices-system-wide-to-get-more-of-them/) to enable additional language voices on Windows.
- Non-ASCII characters, such as umlaut, are pronounced correctly if you select the correct voice.
- Blind players use a number of screen readers, including JAWS, NVDA, VoiceOver, Narrator, and more.
- Windows text-to-speech APIs generally perform better than their equivalents on other systems (e.g. tts_stop followed by tts_speak immediately speaks the new message).

---
