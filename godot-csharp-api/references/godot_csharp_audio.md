# Godot 4 C# API Reference — Audio

> C#-only reference. 54 classes.

### AudioBusLayout
*Inherits: **Resource < RefCounted < Object***

Stores position, muting, solo, bypass, effects, effect position, volume, and the connections between buses. See AudioServer for usage.

### AudioEffectAmplify
*Inherits: **AudioEffect < Resource < RefCounted < Object***

Increases or decreases the volume being routed through the audio bus.

**Properties**
- `float VolumeDb` = `0.0`
- `float VolumeLinear`

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
- `float BufferLength` = `0.1`

**Methods**
- `bool CanGetBuffer(int frames)`
- `void ClearBuffer()`
- `PackedVector2Array GetBuffer(int frames)`
- `int GetBufferLengthFrames()`
- `int GetDiscardedFrames()`
- `int GetFramesAvailable()`
- `int GetPushedFrames()`

### AudioEffectChorus
*Inherits: **AudioEffect < Resource < RefCounted < Object***

Adds a chorus audio effect. The effect applies a filter with voices to duplicate the audio source and manipulate it through the filter.

**Properties**
- `float Dry` = `1.0`
- `float Voice/1/cutoffHz` = `8000.0`
- `float Voice/1/delayMs` = `15.0`
- `float Voice/1/depthMs` = `2.0`
- `float Voice/1/levelDb` = `0.0`
- `float Voice/1/pan` = `-0.5`
- `float Voice/1/rateHz` = `0.8`
- `float Voice/2/cutoffHz` = `8000.0`
- `float Voice/2/delayMs` = `20.0`
- `float Voice/2/depthMs` = `3.0`
- `float Voice/2/levelDb` = `0.0`
- `float Voice/2/pan` = `0.5`
- `float Voice/2/rateHz` = `1.2`
- `float Voice/3/cutoffHz`
- `float Voice/3/delayMs`
- `float Voice/3/depthMs`
- `float Voice/3/levelDb`
- `float Voice/3/pan`
- `float Voice/3/rateHz`
- `float Voice/4/cutoffHz`
- `float Voice/4/delayMs`
- `float Voice/4/depthMs`
- `float Voice/4/levelDb`
- `float Voice/4/pan`
- `float Voice/4/rateHz`
- `int VoiceCount` = `2`
- `float Wet` = `0.5`

**Methods**
- `float GetVoiceCutoffHz(int voiceIdx)`
- `float GetVoiceDelayMs(int voiceIdx)`
- `float GetVoiceDepthMs(int voiceIdx)`
- `float GetVoiceLevelDb(int voiceIdx)`
- `float GetVoicePan(int voiceIdx)`
- `float GetVoiceRateHz(int voiceIdx)`
- `void SetVoiceCutoffHz(int voiceIdx, float cutoffHz)`
- `void SetVoiceDelayMs(int voiceIdx, float delayMs)`
- `void SetVoiceDepthMs(int voiceIdx, float depthMs)`
- `void SetVoiceLevelDb(int voiceIdx, float levelDb)`
- `void SetVoicePan(int voiceIdx, float pan)`
- `void SetVoiceRateHz(int voiceIdx, float rateHz)`

### AudioEffectCompressor
*Inherits: **AudioEffect < Resource < RefCounted < Object***

Dynamic range compressor reduces the level of the sound when the amplitude goes over a certain threshold in Decibels. One of the main uses of a compressor is to increase the dynamic range by clipping as little as possible (when sound goes over 0dB).

**Properties**
- `float AttackUs` = `20.0`
- `float Gain` = `0.0`
- `float Mix` = `1.0`
- `float Ratio` = `4.0`
- `float ReleaseMs` = `250.0`
- `StringName Sidechain` = `&""`
- `float Threshold` = `0.0`

### AudioEffectDelay
*Inherits: **AudioEffect < Resource < RefCounted < Object***

Plays input signal back after a period of time. The delayed signal may be played back multiple times to create the sound of a repeating, decaying echo. Delay effects range from a subtle echo effect to a pronounced blending of previous sounds with new sounds.

**Properties**
- `float Dry` = `1.0`
- `bool FeedbackActive` = `false`
- `float FeedbackDelayMs` = `340.0`
- `float FeedbackLevelDb` = `-6.0`
- `float FeedbackLowpass` = `16000.0`
- `bool Tap1Active` = `true`
- `float Tap1DelayMs` = `250.0`
- `float Tap1LevelDb` = `-6.0`
- `float Tap1Pan` = `0.2`
- `bool Tap2Active` = `true`
- `float Tap2DelayMs` = `500.0`
- `float Tap2LevelDb` = `-12.0`
- `float Tap2Pan` = `-0.4`

### AudioEffectDistortion
*Inherits: **AudioEffect < Resource < RefCounted < Object***

Different types are available: clip, tan, lo-fi (bit crushing), overdrive, or waveshape.

**Properties**
- `float Drive` = `0.0`
- `float KeepHfHz` = `16000.0`
- `Mode Mode` = `0`
- `float PostGain` = `0.0`
- `float PreGain` = `0.0`

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
- `int GetBandCount()`
- `float GetBandGainDb(int bandIdx)`
- `void SetBandGainDb(int bandIdx, float volumeDb)`

### AudioEffectFilter
*Inherits: **AudioEffect < Resource < RefCounted < Object** | Inherited by: AudioEffectBandLimitFilter, AudioEffectBandPassFilter, AudioEffectHighPassFilter, AudioEffectHighShelfFilter, AudioEffectLowPassFilter, AudioEffectLowShelfFilter, ...*

Allows frequencies other than the cutoff_hz to pass.

**Properties**
- `float CutoffHz` = `2000.0`
- `FilterDB Db` = `0`
- `float Gain` = `1.0`
- `float Resonance` = `0.5`

### AudioEffectHardLimiter
*Inherits: **AudioEffect < Resource < RefCounted < Object***

A limiter is an effect designed to disallow sound from going over a given dB threshold. Hard limiters predict volume peaks, and will smoothly apply gain reduction when a peak crosses the ceiling threshold to prevent clipping and distortion. It preserves the waveform and prevents it from crossing the ceiling threshold. Adding one in the Master bus is recommended as a safety measure to prevent sudden volume peaks from occurring, and to prevent distortion caused by clipping.

**Properties**
- `float CeilingDb` = `-0.3`
- `float PreGainDb` = `0.0`
- `float Release` = `0.1`

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
- `void _Process(const void* srcBuffer, AudioFrame* dstBuffer, int frameCount) [virtual]`
- `bool _ProcessSilence() [virtual]`

### AudioEffectLimiter
*Inherits: **AudioEffect < Resource < RefCounted < Object***

A limiter is similar to a compressor, but it's less flexible and designed to disallow sound going over a given dB threshold. Adding one in the Master bus is always recommended to reduce the effects of clipping.

**Properties**
- `float CeilingDb` = `-0.1`
- `float SoftClipDb` = `2.0`
- `float SoftClipRatio` = `10.0`
- `float ThresholdDb` = `0.0`

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
- `float Pan` = `0.0`

### AudioEffectPhaser
*Inherits: **AudioEffect < Resource < RefCounted < Object***

Combines phase-shifted signals with the original signal. The movement of the phase-shifted signals is controlled using a low-frequency oscillator.

**Properties**
- `float Depth` = `1.0`
- `float Feedback` = `0.7`
- `float RangeMaxHz` = `1600.0`
- `float RangeMinHz` = `440.0`
- `float RateHz` = `0.5`

### AudioEffectPitchShift
*Inherits: **AudioEffect < Resource < RefCounted < Object***

Allows modulation of pitch independently of tempo. All frequencies can be increased/decreased with minimal effect on transients.

**Properties**
- `FFTSize FftSize` = `3`
- `int Oversampling` = `4`
- `float PitchScale` = `1.0`

### AudioEffectRecord
*Inherits: **AudioEffect < Resource < RefCounted < Object***

Allows the user to record the sound from an audio bus into an AudioStreamWAV. When used on the "Master" audio bus, this includes all audio output by Godot.

**Properties**
- `Format Format` = `1`

**Methods**
- `AudioStreamWAV GetRecording()`
- `bool IsRecordingActive()`
- `void SetRecordingActive(bool record)`

### AudioEffectReverb
*Inherits: **AudioEffect < Resource < RefCounted < Object***

Simulates the sound of acoustic environments such as rooms, concert halls, caverns, or an open spaces.

**Properties**
- `float Damping` = `0.5`
- `float Dry` = `1.0`
- `float Hipass` = `0.0`
- `float PredelayFeedback` = `0.4`
- `float PredelayMsec` = `150.0`
- `float RoomSize` = `0.8`
- `float Spread` = `1.0`
- `float Wet` = `0.5`

### AudioEffectSpectrumAnalyzerInstance
*Inherits: **AudioEffectInstance < RefCounted < Object***

The runtime part of an AudioEffectSpectrumAnalyzer, which can be used to query the magnitude of a frequency range on its host bus.

**Methods**
- `Vector2 GetMagnitudeForFrequencyRange(float fromHz, float toHz, MagnitudeMode mode = 1)`

### AudioEffectSpectrumAnalyzer
*Inherits: **AudioEffect < Resource < RefCounted < Object***

This audio effect does not affect sound output, but can be used for real-time audio visualizations.

**Properties**
- `float BufferLength` = `2.0`
- `FFTSize FftSize` = `2`
- `float TapBackPos` = `0.01`

### AudioEffectStereoEnhance
*Inherits: **AudioEffect < Resource < RefCounted < Object***

An audio effect that can be used to adjust the intensity of stereo panning.

**Properties**
- `float PanPullout` = `1.0`
- `float Surround` = `0.0`
- `float TimePulloutMs` = `0.0`

### AudioEffect
*Inherits: **Resource < RefCounted < Object** | Inherited by: AudioEffectAmplify, AudioEffectCapture, AudioEffectChorus, AudioEffectCompressor, AudioEffectDelay, AudioEffectDistortion, ...*

The base Resource for every audio effect. In the editor, an audio effect can be added to the current bus layout through the Audio panel. At run-time, it is also possible to manipulate audio effects through AudioServer.add_bus_effect(), AudioServer.remove_bus_effect(), and AudioServer.get_bus_effect().

**Methods**
- `AudioEffectInstance _Instantiate() [virtual]`

### AudioServer
*Inherits: **Object***

AudioServer is a low-level server interface for audio access. It is in charge of creating sample data (playable audio) as well as its playback via a voice interface.

**Properties**
- `int BusCount` = `1`
- `string InputDevice` = `"Default"`
- `string OutputDevice` = `"Default"`
- `float PlaybackSpeedScale` = `1.0`

**Methods**
- `void AddBus(int atPosition = -1)`
- `void AddBusEffect(int busIdx, AudioEffect effect, int atPosition = -1)`
- `AudioBusLayout GenerateBusLayout()`
- `int GetBusChannels(int busIdx)`
- `AudioEffect GetBusEffect(int busIdx, int effectIdx)`
- `int GetBusEffectCount(int busIdx)`
- `AudioEffectInstance GetBusEffectInstance(int busIdx, int effectIdx, int channel = 0)`
- `int GetBusIndex(StringName busName)`
- `string GetBusName(int busIdx)`
- `float GetBusPeakVolumeLeftDb(int busIdx, int channel)`
- `float GetBusPeakVolumeRightDb(int busIdx, int channel)`
- `StringName GetBusSend(int busIdx)`
- `float GetBusVolumeDb(int busIdx)`
- `float GetBusVolumeLinear(int busIdx)`
- `string GetDriverName()`
- `int GetInputBufferLengthFrames()`
- `PackedStringArray GetInputDeviceList()`
- `PackedVector2Array GetInputFrames(int frames)`
- `int GetInputFramesAvailable()`
- `float GetInputMixRate()`
- `float GetMixRate()`
- `PackedStringArray GetOutputDeviceList()`
- `float GetOutputLatency()`
- `SpeakerMode GetSpeakerMode()`
- `float GetTimeSinceLastMix()`
- `float GetTimeToNextMix()`
- `bool IsBusBypassingEffects(int busIdx)`
- `bool IsBusEffectEnabled(int busIdx, int effectIdx)`
- `bool IsBusMute(int busIdx)`
- `bool IsBusSolo(int busIdx)`
- `bool IsStreamRegisteredAsSample(AudioStream stream)`
- `void Lock()`
- `void MoveBus(int index, int toIndex)`
- `void RegisterStreamAsSample(AudioStream stream)`
- `void RemoveBus(int index)`
- `void RemoveBusEffect(int busIdx, int effectIdx)`
- `void SetBusBypassEffects(int busIdx, bool enable)`
- `void SetBusEffectEnabled(int busIdx, int effectIdx, bool enabled)`
- `void SetBusLayout(AudioBusLayout busLayout)`
- `void SetBusMute(int busIdx, bool enable)`

### AudioStreamGeneratorPlayback
*Inherits: **AudioStreamPlaybackResampled < AudioStreamPlayback < RefCounted < Object***

This class is meant to be used with AudioStreamGenerator to play back the generated audio in real-time.

**Methods**
- `bool CanPushBuffer(int amount)`
- `void ClearBuffer()`
- `int GetFramesAvailable()`
- `int GetSkips()`
- `bool PushBuffer(PackedVector2Array frames)`
- `bool PushFrame(Vector2 frame)`

### AudioStreamGenerator
*Inherits: **AudioStream < Resource < RefCounted < Object***

AudioStreamGenerator is a type of audio stream that does not play back sounds on its own; instead, it expects a script to generate audio data for it. See also AudioStreamGeneratorPlayback.

**Properties**
- `float BufferLength` = `0.5`
- `float MixRate` = `44100.0`
- `AudioStreamGeneratorMixRate MixRateMode` = `2`

**C# Examples**
```csharp
[Export] public AudioStreamPlayer Player { get; set; }

private AudioStreamGeneratorPlayback _playback; // Will hold the AudioStreamGeneratorPlayback.
private float _sampleHz;
private float _pulseHz = 440.0f; // The frequency of the sound wave.
private double phase = 0.0;

public override void _Ready()
{
    if (Player.Stream is AudioStreamGenerator generator) // Type as a generator to access MixRate.
    {
        _sampleHz = generator.MixRate;
        Player.Play();
        _playback = (AudioStreamGeneratorPlayback)Player.GetStreamPlayback();
        FillBuffer();
    }
}

public void FillBu
// ...
```

### AudioStreamInteractive
*Inherits: **AudioStream < Resource < RefCounted < Object***

This is an audio stream that can playback music interactively, combining clips and a transition table. Clips must be added first, and then the transition rules via the add_transition(). Additionally, this stream exports a property parameter to control the playback via AudioStreamPlayer, AudioStreamPlayer2D, or AudioStreamPlayer3D.

**Properties**
- `int ClipCount` = `0`
- `int InitialClip` = `0`

**Methods**
- `void AddTransition(int fromClip, int toClip, TransitionFromTime fromTime, TransitionToTime toTime, FadeMode fadeMode, float fadeBeats, bool useFillerClip = false, int fillerClip = -1, bool holdPrevious = false)`
- `void EraseTransition(int fromClip, int toClip)`
- `AutoAdvanceMode GetClipAutoAdvance(int clipIndex)`
- `int GetClipAutoAdvanceNextClip(int clipIndex)`
- `StringName GetClipName(int clipIndex)`
- `AudioStream GetClipStream(int clipIndex)`
- `float GetTransitionFadeBeats(int fromClip, int toClip)`
- `FadeMode GetTransitionFadeMode(int fromClip, int toClip)`
- `int GetTransitionFillerClip(int fromClip, int toClip)`
- `TransitionFromTime GetTransitionFromTime(int fromClip, int toClip)`
- `PackedInt32Array GetTransitionList()`
- `TransitionToTime GetTransitionToTime(int fromClip, int toClip)`
- `bool HasTransition(int fromClip, int toClip)`
- `bool IsTransitionHoldingPrevious(int fromClip, int toClip)`
- `bool IsTransitionUsingFillerClip(int fromClip, int toClip)`
- `void SetClipAutoAdvance(int clipIndex, AutoAdvanceMode mode)`
- `void SetClipAutoAdvanceNextClip(int clipIndex, int autoAdvanceNextClip)`
- `void SetClipName(int clipIndex, StringName name)`
- `void SetClipStream(int clipIndex, AudioStream stream)`

### AudioStreamMP3
*Inherits: **AudioStream < Resource < RefCounted < Object***

MP3 audio stream driver. See data if you want to load an MP3 file at run-time.

**Properties**
- `int BarBeats` = `4`
- `int BeatCount` = `0`
- `float Bpm` = `0.0`
- `PackedByteArray Data` = `PackedByteArray()`
- `bool Loop` = `false`
- `float LoopOffset` = `0.0`

**Methods**
- `AudioStreamMP3 LoadFromBuffer(PackedByteArray streamData) [static]`
- `AudioStreamMP3 LoadFromFile(string path) [static]`

**C# Examples**
```csharp
public AudioStreamMP3 LoadMP3(string path)
{
    using var file = FileAccess.Open(path, FileAccess.ModeFlags.Read);
    var sound = new AudioStreamMP3();
    sound.Data = file.GetBuffer(file.GetLength());
    return sound;
}
```

### AudioStreamMicrophone
*Inherits: **AudioStream < Resource < RefCounted < Object***

When used directly in an AudioStreamPlayer node, AudioStreamMicrophone plays back microphone input in real-time. This can be used in conjunction with AudioEffectCapture to process the data or save it.

### AudioStreamOggVorbis
*Inherits: **AudioStream < Resource < RefCounted < Object***

The AudioStreamOggVorbis class is a specialized AudioStream for handling Ogg Vorbis file formats. It offers functionality for loading and playing back Ogg Vorbis files, as well as managing looping and other playback properties. This class is part of the audio stream system, which also supports WAV files through the AudioStreamWAV class.

**Properties**
- `int BarBeats` = `4`
- `int BeatCount` = `0`
- `float Bpm` = `0.0`
- `bool Loop` = `false`
- `float LoopOffset` = `0.0`
- `OggPacketSequence PacketSequence`
- `Godot.Collections.Dictionary Tags` = `{}`

**Methods**
- `AudioStreamOggVorbis LoadFromBuffer(PackedByteArray streamData) [static]`
- `AudioStreamOggVorbis LoadFromFile(string path) [static]`

### AudioStreamPlaybackInteractive
*Inherits: **AudioStreamPlayback < RefCounted < Object***

Playback component of AudioStreamInteractive. Contains functions to change the currently played clip.

**Methods**
- `int GetCurrentClipIndex()`
- `void SwitchToClip(int clipIndex)`
- `void SwitchToClipByName(StringName clipName)`

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
- `bool IsStreamPlaying(int stream)`
- `int PlayStream(AudioStream stream, float fromOffset = 0, float volumeDb = 0, float pitchScale = 1.0, PlaybackType playbackType = 0, StringName bus = &"Master")`
- `void SetStreamPitchScale(int stream, float pitchScale)`
- `void SetStreamVolume(int stream, float volumeDb)`
- `void StopStream(int stream)`

### AudioStreamPlaybackResampled
*Inherits: **AudioStreamPlayback < RefCounted < Object** | Inherited by: AudioStreamGeneratorPlayback, AudioStreamPlaybackOggVorbis*

There is currently no description for this class. Please help us by contributing one!

**Methods**
- `float _GetStreamSamplingRate() [virtual]`
- `int _MixResampled(AudioFrame* dstBuffer, int frameCount) [virtual]`
- `void BeginResample()`

### AudioStreamPlaybackSynchronized
*Inherits: **AudioStreamPlayback < RefCounted < Object***

There is currently no description for this class. Please help us by contributing one!

### AudioStreamPlayback
*Inherits: **RefCounted < Object** | Inherited by: AudioStreamPlaybackInteractive, AudioStreamPlaybackPlaylist, AudioStreamPlaybackPolyphonic, AudioStreamPlaybackResampled, AudioStreamPlaybackSynchronized*

Can play, loop, pause a scroll through audio. See AudioStream and AudioStreamOggVorbis for usage.

**Methods**
- `int _GetLoopCount() [virtual]`
- `Variant _GetParameter(StringName name) [virtual]`
- `float _GetPlaybackPosition() [virtual]`
- `bool _IsPlaying() [virtual]`
- `int _Mix(AudioFrame* buffer, float rateScale, int frames) [virtual]`
- `void _Seek(float position) [virtual]`
- `void _SetParameter(StringName name, Variant value) [virtual]`
- `void _Start(float fromPos) [virtual]`
- `void _Stop() [virtual]`
- `void _TagUsedStreams() [virtual]`
- `int GetLoopCount()`
- `float GetPlaybackPosition()`
- `AudioSamplePlayback GetSamplePlayback()`
- `bool IsPlaying()`
- `PackedVector2Array MixAudio(float rateScale, int frames)`
- `void Seek(float time = 0.0)`
- `void SetSamplePlayback(AudioSamplePlayback playbackSample)`
- `void Start(float fromPos = 0.0)`
- `void Stop()`

### AudioStreamPlayer2D
*Inherits: **Node2D < CanvasItem < Node < Object***

Plays audio that is attenuated with distance to the listener.

**Properties**
- `int AreaMask` = `1`
- `float Attenuation` = `1.0`
- `bool Autoplay` = `false`
- `StringName Bus` = `&"Master"`
- `float MaxDistance` = `2000.0`
- `int MaxPolyphony` = `1`
- `float PanningStrength` = `1.0`
- `float PitchScale` = `1.0`
- `PlaybackType PlaybackType` = `0`
- `bool Playing` = `false`
- `AudioStream Stream`
- `bool StreamPaused` = `false`
- `float VolumeDb` = `0.0`
- `float VolumeLinear`

**Methods**
- `float GetPlaybackPosition()`
- `AudioStreamPlayback GetStreamPlayback()`
- `bool HasStreamPlayback()`
- `void Play(float fromPosition = 0.0)`
- `void Seek(float toPosition)`
- `void Stop()`

### AudioStreamPlayer3D
*Inherits: **Node3D < Node < Object***

Plays audio with positional sound effects, based on the relative position of the audio listener. Positional effects include distance attenuation, directionality, and the Doppler effect. For greater realism, a low-pass filter is applied to distant sounds. This can be disabled by setting attenuation_filter_cutoff_hz to 20500.

**Properties**
- `int AreaMask` = `1`
- `float AttenuationFilterCutoffHz` = `5000.0`
- `float AttenuationFilterDb` = `-24.0`
- `AttenuationModel AttenuationModel` = `0`
- `bool Autoplay` = `false`
- `StringName Bus` = `&"Master"`
- `DopplerTracking DopplerTracking` = `0`
- `float EmissionAngleDegrees` = `45.0`
- `bool EmissionAngleEnabled` = `false`
- `float EmissionAngleFilterAttenuationDb` = `-12.0`
- `float MaxDb` = `3.0`
- `float MaxDistance` = `0.0`
- `int MaxPolyphony` = `1`
- `float PanningStrength` = `1.0`
- `float PitchScale` = `1.0`
- `PlaybackType PlaybackType` = `0`
- `bool Playing` = `false`
- `AudioStream Stream`
- `bool StreamPaused` = `false`
- `float UnitSize` = `10.0`
- `float VolumeDb` = `0.0`
- `float VolumeLinear`

**Methods**
- `float GetPlaybackPosition()`
- `AudioStreamPlayback GetStreamPlayback()`
- `bool HasStreamPlayback()`
- `void Play(float fromPosition = 0.0)`
- `void Seek(float toPosition)`
- `void Stop()`

### AudioStreamPlayer
*Inherits: **Node < Object***

The AudioStreamPlayer node plays an audio stream non-positionally. It is ideal for user interfaces, menus, or background music.

**Properties**
- `bool Autoplay` = `false`
- `StringName Bus` = `&"Master"`
- `int MaxPolyphony` = `1`
- `MixTarget MixTarget` = `0`
- `float PitchScale` = `1.0`
- `PlaybackType PlaybackType` = `0`
- `bool Playing` = `false`
- `AudioStream Stream`
- `bool StreamPaused` = `false`
- `float VolumeDb` = `0.0`
- `float VolumeLinear`

**Methods**
- `float GetPlaybackPosition()`
- `AudioStreamPlayback GetStreamPlayback()`
- `bool HasStreamPlayback()`
- `void Play(float fromPosition = 0.0)`
- `void Seek(float toPosition)`
- `void Stop()`

### AudioStreamPlaylist
*Inherits: **AudioStream < Resource < RefCounted < Object***

AudioStream that includes sub-streams and plays them back like a playlist.

**Properties**
- `float FadeTime` = `0.3`
- `bool Loop` = `true`
- `bool Shuffle` = `false`
- `int StreamCount` = `0`

**Methods**
- `float GetBpm()`
- `AudioStream GetListStream(int streamIndex)`
- `void SetListStream(int streamIndex, AudioStream audioStream)`

### AudioStreamPolyphonic
*Inherits: **AudioStream < Resource < RefCounted < Object***

AudioStream that lets the user play custom streams at any time from code, simultaneously using a single player.

**Properties**
- `int Polyphony` = `32`

### AudioStreamRandomizer
*Inherits: **AudioStream < Resource < RefCounted < Object***

Picks a random AudioStream from the pool, depending on the playback mode, and applies random pitch shifting and volume shifting during playback.

**Properties**
- `PlaybackMode PlaybackMode` = `0`
- `float RandomPitch` = `1.0`
- `float RandomPitchSemitones` = `0.0`
- `float RandomVolumeOffsetDb` = `0.0`
- `int StreamsCount` = `0`

**Methods**
- `void AddStream(int index, AudioStream stream, float weight = 1.0)`
- `AudioStream GetStream(int index)`
- `float GetStreamProbabilityWeight(int index)`
- `void MoveStream(int indexFrom, int indexTo)`
- `void RemoveStream(int index)`
- `void SetStream(int index, AudioStream stream)`
- `void SetStreamProbabilityWeight(int index, float weight)`

### AudioStreamSynchronized
*Inherits: **AudioStream < Resource < RefCounted < Object***

This is a stream that can be fitted with sub-streams, which will be played in-sync. The streams begin at exactly the same time when play is pressed, and will end when the last of them ends. If one of the sub-streams loops, then playback will continue.

**Properties**
- `int StreamCount` = `0`

**Methods**
- `AudioStream GetSyncStream(int streamIndex)`
- `float GetSyncStreamVolume(int streamIndex)`
- `void SetSyncStream(int streamIndex, AudioStream audioStream)`
- `void SetSyncStreamVolume(int streamIndex, float volumeDb)`

### AudioStreamWAV
*Inherits: **AudioStream < Resource < RefCounted < Object***

AudioStreamWAV stores sound samples loaded from WAV files. To play the stored sound, use an AudioStreamPlayer (for non-positional audio) or AudioStreamPlayer2D/AudioStreamPlayer3D (for positional audio). The sound can be looped.

**Properties**
- `PackedByteArray Data` = `PackedByteArray()`
- `Format Format` = `0`
- `int LoopBegin` = `0`
- `int LoopEnd` = `0`
- `LoopMode LoopMode` = `0`
- `int MixRate` = `44100`
- `bool Stereo` = `false`
- `Godot.Collections.Dictionary Tags` = `{}`

**Methods**
- `AudioStreamWAV LoadFromBuffer(PackedByteArray streamData, Godot.Collections.Dictionary options = {}) [static]`
- `AudioStreamWAV LoadFromFile(string path, Godot.Collections.Dictionary options = {}) [static]`
- `Error SaveToWav(string path)`

### AudioStream
*Inherits: **Resource < RefCounted < Object** | Inherited by: AudioStreamGenerator, AudioStreamInteractive, AudioStreamMicrophone, AudioStreamMP3, AudioStreamOggVorbis, AudioStreamPlaylist, ...*

Base class for audio streams. Audio streams are used for sound effects and music playback, and support WAV (via AudioStreamWAV) and Ogg (via AudioStreamOggVorbis) file formats.

**Methods**
- `int _GetBarBeats() [virtual]`
- `int _GetBeatCount() [virtual]`
- `float _GetBpm() [virtual]`
- `float _GetLength() [virtual]`
- `Array[Dictionary] _GetParameterList() [virtual]`
- `string _GetStreamName() [virtual]`
- `Godot.Collections.Dictionary _GetTags() [virtual]`
- `bool _HasLoop() [virtual]`
- `AudioStreamPlayback _InstantiatePlayback() [virtual]`
- `bool _IsMonophonic() [virtual]`
- `bool CanBeSampled()`
- `AudioSample GenerateSample()`
- `float GetLength()`
- `AudioStreamPlayback InstantiatePlayback()`
- `bool IsMetaStream()`
- `bool IsMonophonic()`
