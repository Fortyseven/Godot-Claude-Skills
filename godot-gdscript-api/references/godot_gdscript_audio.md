# Godot 4 GDScript API Reference — Audio

> GDScript-only reference. 54 classes.

### AudioBusLayout
*Inherits: **Resource < RefCounted < Object***

Stores position, muting, solo, bypass, effects, effect position, volume, and the connections between buses. See AudioServer for usage.

### AudioEffectAmplify
*Inherits: **AudioEffect < Resource < RefCounted < Object***

Increases or decreases the volume being routed through the audio bus.

**Properties**
- `float volume_db` = `0.0`
- `float volume_linear`

### AudioEffectBandLimitFilter
*Inherits: **AudioEffectFilter < AudioEffect < Resource < RefCounted < Object***

Limits the frequencies in a range around the AudioEffectFilter.cutoff_hz and allows frequencies outside of this range to pass.

### AudioEffectBandPassFilter
*Inherits: **AudioEffectFilter < AudioEffect < Resource < RefCounted < Object***

Attenuates the frequencies inside of a range around the AudioEffectFilter.cutoff_hz and cuts frequencies outside of this band.

### AudioEffectCapture
*Inherits: **AudioEffect < Resource < RefCounted < Object***

AudioEffectCapture is an AudioEffect which copies all audio frames from the attached audio effect bus into its internal ring buffer.

**Properties**
- `float buffer_length` = `0.1`

**Methods**
- `bool can_get_buffer(frames: int) const`
- `void clear_buffer()`
- `PackedVector2Array get_buffer(frames: int)`
- `int get_buffer_length_frames() const`
- `int get_discarded_frames() const`
- `int get_frames_available() const`
- `int get_pushed_frames() const`

### AudioEffectChorus
*Inherits: **AudioEffect < Resource < RefCounted < Object***

Adds a chorus audio effect. The effect applies a filter with voices to duplicate the audio source and manipulate it through the filter.

**Properties**
- `float dry` = `1.0`
- `float voice/1/cutoff_hz` = `8000.0`
- `float voice/1/delay_ms` = `15.0`
- `float voice/1/depth_ms` = `2.0`
- `float voice/1/level_db` = `0.0`
- `float voice/1/pan` = `-0.5`
- `float voice/1/rate_hz` = `0.8`
- `float voice/2/cutoff_hz` = `8000.0`
- `float voice/2/delay_ms` = `20.0`
- `float voice/2/depth_ms` = `3.0`
- `float voice/2/level_db` = `0.0`
- `float voice/2/pan` = `0.5`
- `float voice/2/rate_hz` = `1.2`
- `float voice/3/cutoff_hz`
- `float voice/3/delay_ms`
- `float voice/3/depth_ms`
- `float voice/3/level_db`
- `float voice/3/pan`
- `float voice/3/rate_hz`
- `float voice/4/cutoff_hz`
- `float voice/4/delay_ms`
- `float voice/4/depth_ms`
- `float voice/4/level_db`
- `float voice/4/pan`
- `float voice/4/rate_hz`
- `int voice_count` = `2`
- `float wet` = `0.5`

**Methods**
- `float get_voice_cutoff_hz(voice_idx: int) const`
- `float get_voice_delay_ms(voice_idx: int) const`
- `float get_voice_depth_ms(voice_idx: int) const`
- `float get_voice_level_db(voice_idx: int) const`
- `float get_voice_pan(voice_idx: int) const`
- `float get_voice_rate_hz(voice_idx: int) const`
- `void set_voice_cutoff_hz(voice_idx: int, cutoff_hz: float)`
- `void set_voice_delay_ms(voice_idx: int, delay_ms: float)`
- `void set_voice_depth_ms(voice_idx: int, depth_ms: float)`
- `void set_voice_level_db(voice_idx: int, level_db: float)`
- `void set_voice_pan(voice_idx: int, pan: float)`
- `void set_voice_rate_hz(voice_idx: int, rate_hz: float)`

### AudioEffectCompressor
*Inherits: **AudioEffect < Resource < RefCounted < Object***

Dynamic range compressor reduces the level of the sound when the amplitude goes over a certain threshold in Decibels. One of the main uses of a compressor is to increase the dynamic range by clipping as little as possible (when sound goes over 0dB).

**Properties**
- `float attack_us` = `20.0`
- `float gain` = `0.0`
- `float mix` = `1.0`
- `float ratio` = `4.0`
- `float release_ms` = `250.0`
- `StringName sidechain` = `&""`
- `float threshold` = `0.0`

### AudioEffectDelay
*Inherits: **AudioEffect < Resource < RefCounted < Object***

Plays input signal back after a period of time. The delayed signal may be played back multiple times to create the sound of a repeating, decaying echo. Delay effects range from a subtle echo effect to a pronounced blending of previous sounds with new sounds.

**Properties**
- `float dry` = `1.0`
- `bool feedback_active` = `false`
- `float feedback_delay_ms` = `340.0`
- `float feedback_level_db` = `-6.0`
- `float feedback_lowpass` = `16000.0`
- `bool tap1_active` = `true`
- `float tap1_delay_ms` = `250.0`
- `float tap1_level_db` = `-6.0`
- `float tap1_pan` = `0.2`
- `bool tap2_active` = `true`
- `float tap2_delay_ms` = `500.0`
- `float tap2_level_db` = `-12.0`
- `float tap2_pan` = `-0.4`

### AudioEffectDistortion
*Inherits: **AudioEffect < Resource < RefCounted < Object***

Different types are available: clip, tan, lo-fi (bit crushing), overdrive, or waveshape.

**Properties**
- `float drive` = `0.0`
- `float keep_hf_hz` = `16000.0`
- `Mode mode` = `0`
- `float post_gain` = `0.0`
- `float pre_gain` = `0.0`

### AudioEffectEQ10
*Inherits: **AudioEffectEQ < AudioEffect < Resource < RefCounted < Object***

Frequency bands:

### AudioEffectEQ21
*Inherits: **AudioEffectEQ < AudioEffect < Resource < RefCounted < Object***

Frequency bands:

### AudioEffectEQ6
*Inherits: **AudioEffectEQ < AudioEffect < Resource < RefCounted < Object***

Frequency bands:

### AudioEffectEQ
*Inherits: **AudioEffect < Resource < RefCounted < Object** | Inherited by: AudioEffectEQ10, AudioEffectEQ21, AudioEffectEQ6*

AudioEffectEQ gives you control over frequencies. Use it to compensate for existing deficiencies in audio. AudioEffectEQs are useful on the Master bus to completely master a mix and give it more character. They are also useful when a game is run on a mobile device, to adjust the mix to that kind of speakers (it can be added but disabled when headphones are plugged).

**Methods**
- `int get_band_count() const`
- `float get_band_gain_db(band_idx: int) const`
- `void set_band_gain_db(band_idx: int, volume_db: float)`

### AudioEffectFilter
*Inherits: **AudioEffect < Resource < RefCounted < Object** | Inherited by: AudioEffectBandLimitFilter, AudioEffectBandPassFilter, AudioEffectHighPassFilter, AudioEffectHighShelfFilter, AudioEffectLowPassFilter, AudioEffectLowShelfFilter, ...*

Allows frequencies other than the cutoff_hz to pass.

**Properties**
- `float cutoff_hz` = `2000.0`
- `FilterDB db` = `0`
- `float gain` = `1.0`
- `float resonance` = `0.5`

### AudioEffectHardLimiter
*Inherits: **AudioEffect < Resource < RefCounted < Object***

A limiter is an effect designed to disallow sound from going over a given dB threshold. Hard limiters predict volume peaks, and will smoothly apply gain reduction when a peak crosses the ceiling threshold to prevent clipping and distortion. It preserves the waveform and prevents it from crossing the ceiling threshold. Adding one in the Master bus is recommended as a safety measure to prevent sudden volume peaks from occurring, and to prevent distortion caused by clipping.

**Properties**
- `float ceiling_db` = `-0.3`
- `float pre_gain_db` = `0.0`
- `float release` = `0.1`

### AudioEffectHighPassFilter
*Inherits: **AudioEffectFilter < AudioEffect < Resource < RefCounted < Object***

Cuts frequencies lower than the AudioEffectFilter.cutoff_hz and allows higher frequencies to pass.

### AudioEffectHighShelfFilter
*Inherits: **AudioEffectFilter < AudioEffect < Resource < RefCounted < Object***

Reduces all frequencies above the AudioEffectFilter.cutoff_hz.

### AudioEffectInstance
*Inherits: **RefCounted < Object** | Inherited by: AudioEffectSpectrumAnalyzerInstance*

An audio effect instance manipulates the audio it receives for a given effect. This instance is automatically created by an AudioEffect when it is added to a bus, and should usually not be created directly. If necessary, it can be fetched at run-time with AudioServer.get_bus_effect_instance().

**Methods**
- `void _process(src_buffer: const void*, dst_buffer: AudioFrame*, frame_count: int) virtual required`
- `bool _process_silence() virtual const`

### AudioEffectLimiter
*Inherits: **AudioEffect < Resource < RefCounted < Object***

A limiter is similar to a compressor, but it's less flexible and designed to disallow sound going over a given dB threshold. Adding one in the Master bus is always recommended to reduce the effects of clipping.

**Properties**
- `float ceiling_db` = `-0.1`
- `float soft_clip_db` = `2.0`
- `float soft_clip_ratio` = `10.0`
- `float threshold_db` = `0.0`

### AudioEffectLowPassFilter
*Inherits: **AudioEffectFilter < AudioEffect < Resource < RefCounted < Object***

Cuts frequencies higher than the AudioEffectFilter.cutoff_hz and allows lower frequencies to pass.

### AudioEffectLowShelfFilter
*Inherits: **AudioEffectFilter < AudioEffect < Resource < RefCounted < Object***

Reduces all frequencies below the AudioEffectFilter.cutoff_hz.

### AudioEffectNotchFilter
*Inherits: **AudioEffectFilter < AudioEffect < Resource < RefCounted < Object***

Attenuates frequencies in a narrow band around the AudioEffectFilter.cutoff_hz and cuts frequencies outside of this range.

### AudioEffectPanner
*Inherits: **AudioEffect < Resource < RefCounted < Object***

Determines how much of an audio signal is sent to the left and right buses.

**Properties**
- `float pan` = `0.0`

### AudioEffectPhaser
*Inherits: **AudioEffect < Resource < RefCounted < Object***

Combines phase-shifted signals with the original signal. The movement of the phase-shifted signals is controlled using a low-frequency oscillator.

**Properties**
- `float depth` = `1.0`
- `float feedback` = `0.7`
- `float range_max_hz` = `1600.0`
- `float range_min_hz` = `440.0`
- `float rate_hz` = `0.5`

### AudioEffectPitchShift
*Inherits: **AudioEffect < Resource < RefCounted < Object***

Allows modulation of pitch independently of tempo. All frequencies can be increased/decreased with minimal effect on transients.

**Properties**
- `FFTSize fft_size` = `3`
- `int oversampling` = `4`
- `float pitch_scale` = `1.0`

### AudioEffectRecord
*Inherits: **AudioEffect < Resource < RefCounted < Object***

Allows the user to record the sound from an audio bus into an AudioStreamWAV. When used on the "Master" audio bus, this includes all audio output by Godot.

**Properties**
- `Format format` = `1`

**Methods**
- `AudioStreamWAV get_recording() const`
- `bool is_recording_active() const`
- `void set_recording_active(record: bool)`

### AudioEffectReverb
*Inherits: **AudioEffect < Resource < RefCounted < Object***

Simulates the sound of acoustic environments such as rooms, concert halls, caverns, or an open spaces.

**Properties**
- `float damping` = `0.5`
- `float dry` = `1.0`
- `float hipass` = `0.0`
- `float predelay_feedback` = `0.4`
- `float predelay_msec` = `150.0`
- `float room_size` = `0.8`
- `float spread` = `1.0`
- `float wet` = `0.5`

### AudioEffectSpectrumAnalyzerInstance
*Inherits: **AudioEffectInstance < RefCounted < Object***

The runtime part of an AudioEffectSpectrumAnalyzer, which can be used to query the magnitude of a frequency range on its host bus.

**Methods**
- `Vector2 get_magnitude_for_frequency_range(from_hz: float, to_hz: float, mode: MagnitudeMode = 1) const`

### AudioEffectSpectrumAnalyzer
*Inherits: **AudioEffect < Resource < RefCounted < Object***

This audio effect does not affect sound output, but can be used for real-time audio visualizations.

**Properties**
- `float buffer_length` = `2.0`
- `FFTSize fft_size` = `2`
- `float tap_back_pos` = `0.01`

### AudioEffectStereoEnhance
*Inherits: **AudioEffect < Resource < RefCounted < Object***

An audio effect that can be used to adjust the intensity of stereo panning.

**Properties**
- `float pan_pullout` = `1.0`
- `float surround` = `0.0`
- `float time_pullout_ms` = `0.0`

### AudioEffect
*Inherits: **Resource < RefCounted < Object** | Inherited by: AudioEffectAmplify, AudioEffectCapture, AudioEffectChorus, AudioEffectCompressor, AudioEffectDelay, AudioEffectDistortion, ...*

The base Resource for every audio effect. In the editor, an audio effect can be added to the current bus layout through the Audio panel. At run-time, it is also possible to manipulate audio effects through AudioServer.add_bus_effect(), AudioServer.remove_bus_effect(), and AudioServer.get_bus_effect().

**Methods**
- `AudioEffectInstance _instantiate() virtual required`

**GDScript Examples**
```gdscript
extends AudioEffect

@export var strength = 4.0

func _instantiate():
    var effect = CustomAudioEffectInstance.new()
    effect.base = self

    return effect
```

### AudioServer
*Inherits: **Object***

AudioServer is a low-level server interface for audio access. It is in charge of creating sample data (playable audio) as well as its playback via a voice interface.

**Properties**
- `int bus_count` = `1`
- `String input_device` = `"Default"`
- `String output_device` = `"Default"`
- `float playback_speed_scale` = `1.0`

**Methods**
- `void add_bus(at_position: int = -1)`
- `void add_bus_effect(bus_idx: int, effect: AudioEffect, at_position: int = -1)`
- `AudioBusLayout generate_bus_layout() const`
- `int get_bus_channels(bus_idx: int) const`
- `AudioEffect get_bus_effect(bus_idx: int, effect_idx: int)`
- `int get_bus_effect_count(bus_idx: int)`
- `AudioEffectInstance get_bus_effect_instance(bus_idx: int, effect_idx: int, channel: int = 0)`
- `int get_bus_index(bus_name: StringName) const`
- `String get_bus_name(bus_idx: int) const`
- `float get_bus_peak_volume_left_db(bus_idx: int, channel: int) const`
- `float get_bus_peak_volume_right_db(bus_idx: int, channel: int) const`
- `StringName get_bus_send(bus_idx: int) const`
- `float get_bus_volume_db(bus_idx: int) const`
- `float get_bus_volume_linear(bus_idx: int) const`
- `String get_driver_name() const`
- `int get_input_buffer_length_frames()`
- `PackedStringArray get_input_device_list()`
- `PackedVector2Array get_input_frames(frames: int)`
- `int get_input_frames_available()`
- `float get_input_mix_rate() const`
- `float get_mix_rate() const`
- `PackedStringArray get_output_device_list()`
- `float get_output_latency() const`
- `SpeakerMode get_speaker_mode() const`
- `float get_time_since_last_mix() const`
- `float get_time_to_next_mix() const`
- `bool is_bus_bypassing_effects(bus_idx: int) const`
- `bool is_bus_effect_enabled(bus_idx: int, effect_idx: int) const`
- `bool is_bus_mute(bus_idx: int) const`
- `bool is_bus_solo(bus_idx: int) const`
- `bool is_stream_registered_as_sample(stream: AudioStream)`
- `void lock()`
- `void move_bus(index: int, to_index: int)`
- `void register_stream_as_sample(stream: AudioStream)`
- `void remove_bus(index: int)`
- `void remove_bus_effect(bus_idx: int, effect_idx: int)`
- `void set_bus_bypass_effects(bus_idx: int, enable: bool)`
- `void set_bus_effect_enabled(bus_idx: int, effect_idx: int, enabled: bool)`
- `void set_bus_layout(bus_layout: AudioBusLayout)`
- `void set_bus_mute(bus_idx: int, enable: bool)`

### AudioStreamGeneratorPlayback
*Inherits: **AudioStreamPlaybackResampled < AudioStreamPlayback < RefCounted < Object***

This class is meant to be used with AudioStreamGenerator to play back the generated audio in real-time.

**Methods**
- `bool can_push_buffer(amount: int) const`
- `void clear_buffer()`
- `int get_frames_available() const`
- `int get_skips() const`
- `bool push_buffer(frames: PackedVector2Array)`
- `bool push_frame(frame: Vector2)`

### AudioStreamGenerator
*Inherits: **AudioStream < Resource < RefCounted < Object***

AudioStreamGenerator is a type of audio stream that does not play back sounds on its own; instead, it expects a script to generate audio data for it. See also AudioStreamGeneratorPlayback.

**Properties**
- `float buffer_length` = `0.5`
- `float mix_rate` = `44100.0`
- `AudioStreamGeneratorMixRate mix_rate_mode` = `2`

**GDScript Examples**
```gdscript
var playback # Will hold the AudioStreamGeneratorPlayback.
@onready var sample_hz = $AudioStreamPlayer.stream.mix_rate
var pulse_hz = 440.0 # The frequency of the sound wave.
var phase = 0.0

func _ready():
    $AudioStreamPlayer.play()
    playback = $AudioStreamPlayer.get_stream_playback()
    fill_buffer()

func fill_buffer():
    var increment = pulse_hz / sample_hz
    var frames_available = playback.get_frames_available()

    for i in range(frames_available):
        playback.push_frame(Vector2.ONE * sin(phase * TAU))
        phase = fmod(phase + increment, 1.0)
```

### AudioStreamInteractive
*Inherits: **AudioStream < Resource < RefCounted < Object***

This is an audio stream that can playback music interactively, combining clips and a transition table. Clips must be added first, and then the transition rules via the add_transition(). Additionally, this stream exports a property parameter to control the playback via AudioStreamPlayer, AudioStreamPlayer2D, or AudioStreamPlayer3D.

**Properties**
- `int clip_count` = `0`
- `int initial_clip` = `0`

**Methods**
- `void add_transition(from_clip: int, to_clip: int, from_time: TransitionFromTime, to_time: TransitionToTime, fade_mode: FadeMode, fade_beats: float, use_filler_clip: bool = false, filler_clip: int = -1, hold_previous: bool = false)`
- `void erase_transition(from_clip: int, to_clip: int)`
- `AutoAdvanceMode get_clip_auto_advance(clip_index: int) const`
- `int get_clip_auto_advance_next_clip(clip_index: int) const`
- `StringName get_clip_name(clip_index: int) const`
- `AudioStream get_clip_stream(clip_index: int) const`
- `float get_transition_fade_beats(from_clip: int, to_clip: int) const`
- `FadeMode get_transition_fade_mode(from_clip: int, to_clip: int) const`
- `int get_transition_filler_clip(from_clip: int, to_clip: int) const`
- `TransitionFromTime get_transition_from_time(from_clip: int, to_clip: int) const`
- `PackedInt32Array get_transition_list() const`
- `TransitionToTime get_transition_to_time(from_clip: int, to_clip: int) const`
- `bool has_transition(from_clip: int, to_clip: int) const`
- `bool is_transition_holding_previous(from_clip: int, to_clip: int) const`
- `bool is_transition_using_filler_clip(from_clip: int, to_clip: int) const`
- `void set_clip_auto_advance(clip_index: int, mode: AutoAdvanceMode)`
- `void set_clip_auto_advance_next_clip(clip_index: int, auto_advance_next_clip: int)`
- `void set_clip_name(clip_index: int, name: StringName)`
- `void set_clip_stream(clip_index: int, stream: AudioStream)`

### AudioStreamMP3
*Inherits: **AudioStream < Resource < RefCounted < Object***

MP3 audio stream driver. See data if you want to load an MP3 file at run-time.

**Properties**
- `int bar_beats` = `4`
- `int beat_count` = `0`
- `float bpm` = `0.0`
- `PackedByteArray data` = `PackedByteArray()`
- `bool loop` = `false`
- `float loop_offset` = `0.0`

**Methods**
- `AudioStreamMP3 load_from_buffer(stream_data: PackedByteArray) static`
- `AudioStreamMP3 load_from_file(path: String) static`

**GDScript Examples**
```gdscript
func load_mp3(path):
    var file = FileAccess.open(path, FileAccess.READ)
    var sound = AudioStreamMP3.new()
    sound.data = file.get_buffer(file.get_length())
    return sound
```

### AudioStreamMicrophone
*Inherits: **AudioStream < Resource < RefCounted < Object***

When used directly in an AudioStreamPlayer node, AudioStreamMicrophone plays back microphone input in real-time. This can be used in conjunction with AudioEffectCapture to process the data or save it.

### AudioStreamOggVorbis
*Inherits: **AudioStream < Resource < RefCounted < Object***

The AudioStreamOggVorbis class is a specialized AudioStream for handling Ogg Vorbis file formats. It offers functionality for loading and playing back Ogg Vorbis files, as well as managing looping and other playback properties. This class is part of the audio stream system, which also supports WAV files through the AudioStreamWAV class.

**Properties**
- `int bar_beats` = `4`
- `int beat_count` = `0`
- `float bpm` = `0.0`
- `bool loop` = `false`
- `float loop_offset` = `0.0`
- `OggPacketSequence packet_sequence`
- `Dictionary tags` = `{}`

**Methods**
- `AudioStreamOggVorbis load_from_buffer(stream_data: PackedByteArray) static`
- `AudioStreamOggVorbis load_from_file(path: String) static`

### AudioStreamPlaybackInteractive
*Inherits: **AudioStreamPlayback < RefCounted < Object***

Playback component of AudioStreamInteractive. Contains functions to change the currently played clip.

**Methods**
- `int get_current_clip_index() const`
- `void switch_to_clip(clip_index: int)`
- `void switch_to_clip_by_name(clip_name: StringName)`

**GDScript Examples**
```gdscript
var playing_clip_name = stream.get_clip_name(get_stream_playback().get_current_clip_index())
```

### AudioStreamPlaybackOggVorbis
*Inherits: **AudioStreamPlaybackResampled < AudioStreamPlayback < RefCounted < Object***

There is currently no description for this class. Please help us by contributing one!

### AudioStreamPlaybackPlaylist
*Inherits: **AudioStreamPlayback < RefCounted < Object***

Playback class used for AudioStreamPlaylist.

### AudioStreamPlaybackPolyphonic
*Inherits: **AudioStreamPlayback < RefCounted < Object***

Playback instance for AudioStreamPolyphonic. After setting the stream property of AudioStreamPlayer, AudioStreamPlayer2D, or AudioStreamPlayer3D, the playback instance can be obtained by calling AudioStreamPlayer.get_stream_playback(), AudioStreamPlayer2D.get_stream_playback() or AudioStreamPlayer3D.get_stream_playback() methods.

**Methods**
- `bool is_stream_playing(stream: int) const`
- `int play_stream(stream: AudioStream, from_offset: float = 0, volume_db: float = 0, pitch_scale: float = 1.0, playback_type: PlaybackType = 0, bus: StringName = &"Master")`
- `void set_stream_pitch_scale(stream: int, pitch_scale: float)`
- `void set_stream_volume(stream: int, volume_db: float)`
- `void stop_stream(stream: int)`

### AudioStreamPlaybackResampled
*Inherits: **AudioStreamPlayback < RefCounted < Object** | Inherited by: AudioStreamGeneratorPlayback, AudioStreamPlaybackOggVorbis*

There is currently no description for this class. Please help us by contributing one!

**Methods**
- `float _get_stream_sampling_rate() virtual required const`
- `int _mix_resampled(dst_buffer: AudioFrame*, frame_count: int) virtual required`
- `void begin_resample()`

### AudioStreamPlaybackSynchronized
*Inherits: **AudioStreamPlayback < RefCounted < Object***

There is currently no description for this class. Please help us by contributing one!

### AudioStreamPlayback
*Inherits: **RefCounted < Object** | Inherited by: AudioStreamPlaybackInteractive, AudioStreamPlaybackPlaylist, AudioStreamPlaybackPolyphonic, AudioStreamPlaybackResampled, AudioStreamPlaybackSynchronized*

Can play, loop, pause a scroll through audio. See AudioStream and AudioStreamOggVorbis for usage.

**Methods**
- `int _get_loop_count() virtual const`
- `Variant _get_parameter(name: StringName) virtual const`
- `float _get_playback_position() virtual required const`
- `bool _is_playing() virtual required const`
- `int _mix(buffer: AudioFrame*, rate_scale: float, frames: int) virtual required`
- `void _seek(position: float) virtual`
- `void _set_parameter(name: StringName, value: Variant) virtual`
- `void _start(from_pos: float) virtual required`
- `void _stop() virtual required`
- `void _tag_used_streams() virtual`
- `int get_loop_count() const`
- `float get_playback_position() const`
- `AudioSamplePlayback get_sample_playback() const`
- `bool is_playing() const`
- `PackedVector2Array mix_audio(rate_scale: float, frames: int)`
- `void seek(time: float = 0.0)`
- `void set_sample_playback(playback_sample: AudioSamplePlayback)`
- `void start(from_pos: float = 0.0)`
- `void stop()`

### AudioStreamPlayer2D
*Inherits: **Node2D < CanvasItem < Node < Object***

Plays audio that is attenuated with distance to the listener.

**Properties**
- `int area_mask` = `1`
- `float attenuation` = `1.0`
- `bool autoplay` = `false`
- `StringName bus` = `&"Master"`
- `float max_distance` = `2000.0`
- `int max_polyphony` = `1`
- `float panning_strength` = `1.0`
- `float pitch_scale` = `1.0`
- `PlaybackType playback_type` = `0`
- `bool playing` = `false`
- `AudioStream stream`
- `bool stream_paused` = `false`
- `float volume_db` = `0.0`
- `float volume_linear`

**Methods**
- `float get_playback_position()`
- `AudioStreamPlayback get_stream_playback()`
- `bool has_stream_playback()`
- `void play(from_position: float = 0.0)`
- `void seek(to_position: float)`
- `void stop()`

### AudioStreamPlayer3D
*Inherits: **Node3D < Node < Object***

Plays audio with positional sound effects, based on the relative position of the audio listener. Positional effects include distance attenuation, directionality, and the Doppler effect. For greater realism, a low-pass filter is applied to distant sounds. This can be disabled by setting attenuation_filter_cutoff_hz to 20500.

**Properties**
- `int area_mask` = `1`
- `float attenuation_filter_cutoff_hz` = `5000.0`
- `float attenuation_filter_db` = `-24.0`
- `AttenuationModel attenuation_model` = `0`
- `bool autoplay` = `false`
- `StringName bus` = `&"Master"`
- `DopplerTracking doppler_tracking` = `0`
- `float emission_angle_degrees` = `45.0`
- `bool emission_angle_enabled` = `false`
- `float emission_angle_filter_attenuation_db` = `-12.0`
- `float max_db` = `3.0`
- `float max_distance` = `0.0`
- `int max_polyphony` = `1`
- `float panning_strength` = `1.0`
- `float pitch_scale` = `1.0`
- `PlaybackType playback_type` = `0`
- `bool playing` = `false`
- `AudioStream stream`
- `bool stream_paused` = `false`
- `float unit_size` = `10.0`
- `float volume_db` = `0.0`
- `float volume_linear`

**Methods**
- `float get_playback_position()`
- `AudioStreamPlayback get_stream_playback()`
- `bool has_stream_playback()`
- `void play(from_position: float = 0.0)`
- `void seek(to_position: float)`
- `void stop()`

### AudioStreamPlayer
*Inherits: **Node < Object***

The AudioStreamPlayer node plays an audio stream non-positionally. It is ideal for user interfaces, menus, or background music.

**Properties**
- `bool autoplay` = `false`
- `StringName bus` = `&"Master"`
- `int max_polyphony` = `1`
- `MixTarget mix_target` = `0`
- `float pitch_scale` = `1.0`
- `PlaybackType playback_type` = `0`
- `bool playing` = `false`
- `AudioStream stream`
- `bool stream_paused` = `false`
- `float volume_db` = `0.0`
- `float volume_linear`

**Methods**
- `float get_playback_position()`
- `AudioStreamPlayback get_stream_playback()`
- `bool has_stream_playback()`
- `void play(from_position: float = 0.0)`
- `void seek(to_position: float)`
- `void stop()`

### AudioStreamPlaylist
*Inherits: **AudioStream < Resource < RefCounted < Object***

AudioStream that includes sub-streams and plays them back like a playlist.

**Properties**
- `float fade_time` = `0.3`
- `bool loop` = `true`
- `bool shuffle` = `false`
- `int stream_count` = `0`

**Methods**
- `float get_bpm() const`
- `AudioStream get_list_stream(stream_index: int) const`
- `void set_list_stream(stream_index: int, audio_stream: AudioStream)`

### AudioStreamPolyphonic
*Inherits: **AudioStream < Resource < RefCounted < Object***

AudioStream that lets the user play custom streams at any time from code, simultaneously using a single player.

**Properties**
- `int polyphony` = `32`

### AudioStreamRandomizer
*Inherits: **AudioStream < Resource < RefCounted < Object***

Picks a random AudioStream from the pool, depending on the playback mode, and applies random pitch shifting and volume shifting during playback.

**Properties**
- `PlaybackMode playback_mode` = `0`
- `float random_pitch` = `1.0`
- `float random_pitch_semitones` = `0.0`
- `float random_volume_offset_db` = `0.0`
- `int streams_count` = `0`

**Methods**
- `void add_stream(index: int, stream: AudioStream, weight: float = 1.0)`
- `AudioStream get_stream(index: int) const`
- `float get_stream_probability_weight(index: int) const`
- `void move_stream(index_from: int, index_to: int)`
- `void remove_stream(index: int)`
- `void set_stream(index: int, stream: AudioStream)`
- `void set_stream_probability_weight(index: int, weight: float)`

### AudioStreamSynchronized
*Inherits: **AudioStream < Resource < RefCounted < Object***

This is a stream that can be fitted with sub-streams, which will be played in-sync. The streams begin at exactly the same time when play is pressed, and will end when the last of them ends. If one of the sub-streams loops, then playback will continue.

**Properties**
- `int stream_count` = `0`

**Methods**
- `AudioStream get_sync_stream(stream_index: int) const`
- `float get_sync_stream_volume(stream_index: int) const`
- `void set_sync_stream(stream_index: int, audio_stream: AudioStream)`
- `void set_sync_stream_volume(stream_index: int, volume_db: float)`

### AudioStreamWAV
*Inherits: **AudioStream < Resource < RefCounted < Object***

AudioStreamWAV stores sound samples loaded from WAV files. To play the stored sound, use an AudioStreamPlayer (for non-positional audio) or AudioStreamPlayer2D/AudioStreamPlayer3D (for positional audio). The sound can be looped.

**Properties**
- `PackedByteArray data` = `PackedByteArray()`
- `Format format` = `0`
- `int loop_begin` = `0`
- `int loop_end` = `0`
- `LoopMode loop_mode` = `0`
- `int mix_rate` = `44100`
- `bool stereo` = `false`
- `Dictionary tags` = `{}`

**Methods**
- `AudioStreamWAV load_from_buffer(stream_data: PackedByteArray, options: Dictionary = {}) static`
- `AudioStreamWAV load_from_file(path: String, options: Dictionary = {}) static`
- `Error save_to_wav(path: String)`

**GDScript Examples**
```gdscript
@onready var audio_player = $AudioStreamPlayer

func _ready():
    get_window().files_dropped.connect(_on_files_dropped)

func _on_files_dropped(files):
    if files[0].get_extension() == "wav":
        audio_player.stream = AudioStreamWAV.load_from_file(files[0], {
                "force/max_rate": true,
                "force/max_rate_hz": 11025
            })
        audio_player.play()
```

### AudioStream
*Inherits: **Resource < RefCounted < Object** | Inherited by: AudioStreamGenerator, AudioStreamInteractive, AudioStreamMicrophone, AudioStreamMP3, AudioStreamOggVorbis, AudioStreamPlaylist, ...*

Base class for audio streams. Audio streams are used for sound effects and music playback, and support WAV (via AudioStreamWAV) and Ogg (via AudioStreamOggVorbis) file formats.

**Methods**
- `int _get_bar_beats() virtual const`
- `int _get_beat_count() virtual const`
- `float _get_bpm() virtual const`
- `float _get_length() virtual const`
- `Array[Dictionary] _get_parameter_list() virtual const`
- `String _get_stream_name() virtual const`
- `Dictionary _get_tags() virtual const`
- `bool _has_loop() virtual const`
- `AudioStreamPlayback _instantiate_playback() virtual required const`
- `bool _is_monophonic() virtual const`
- `bool can_be_sampled() const`
- `AudioSample generate_sample() const`
- `float get_length() const`
- `AudioStreamPlayback instantiate_playback()`
- `bool is_meta_stream() const`
- `bool is_monophonic() const`
