# Media Properties

> Category: `Media` | Type: `notes`

## Description

The following properties apply to media types.

These properties can be applied to all media types.

These properties can be applied to media types whose major type equals MediaType_Audio.

These properties can be applied to media types whose major type equals MediaType_Video.

The following properties apply to interleaved DV video.

The following attributes apply to Advanced Streaming Format (ASF) files.

The following attributes apply to MPEG-4 files.

These properties can be applied to media types whose major type equals MediaType_Timestamp.

Media CAPL Functions | Major Media Types / Audio Subtypes

| Functions | Type | Short Description |
|---|---|---|
| AllSamplesIndependent | dword | Specifies whether each sample is independent of the other samples in the stream. |
| Compressed | dword | Specifies whether the media data is compressed. |
| FixedSizeSamples | dword | Specifies whether the samples have a fixed size. |
| MajorType | string | Major type |
| SampleSize | dword | Size of each sample, in bytes. |
| Subtype | string | Subtype |

| Functions | Type | Short Description |
|---|---|---|
| AacAudioProfileLevelIndication | dword | Specifies the audio profile and level of an Advanced Audio Coding (AAC) stream. |
| AacPayloadType | dword | Specifies the payload type for an Advanced Audio Coding (AAC) stream. |
| AudioAvgBytesPerSecond | dword | Average number of bytes per second. |
| AudioBitsPerSample | dword | Number of bits per audio sample. |
| AudioBlockAlignment | dword | Block alignment, in bytes. |
| AudioChannelMask | dword | Specifies the assignment of audio channels to speaker positions. |
| AudioFloatSamplesPerSecond | double | Number of audio samples per second (floating-point value). |
| AudioFolddownMatrix | byte[] | Specifies how an audio decoder should transform multichannel audio to stereo output. |
| AudioNumChannels | dword | Number of audio channels. |
| AudioSamplesPerBlock | dword | Number of audio samples contained in one compressed block of audio data. |
| AudioSamplesPerSecond | dword | Number of audio samples per second (integer value). |
| AudioValidBitsPerSample | dword | Number of valid bits of audio data in each audio sample. |
| AudioWmadrcAvgref | dword | Reference average volume level of a Windows Media Audio file. |
| AudioWmadrcAvgtarget | dword | Target average volume level of a Windows Media Audio file. |
| AudioWmadrcPeakref | dword | Reference peak volume level of a Windows Media Audio file. |
| AudioWmadrcPeaktarget | dword | Target peak volume level of a Windows Media Audio file. |
| OriginalWaveFormatTag | dword | Contains the original WAVE format tag for an audio stream. |

| Functions | Type | Short Description |
|---|---|---|
| AvgBitErrorRate | dword | Data error rate. |
| AvgBitrate | dword | Approximate data rate of the video stream. |
| DefaultStride | dword | Default surface stride. |
| DrmFlags | dword | Specifies whether the video requires enforcing copy protection. |
| FrameRate | qword | Frame rate. |
| FrameRateRangeMax | qword | The maximum frame rate supported by a video capture device. |
| FrameRateRangeMin | qword | The minimum frame rate supported by a video capture device. |
| FrameSize | qword | Width and height of the video frame. |
| GeometricAperture | dword | Geometric aperture. |
| InterlaceMode | dword | Describes how the frames are interlaced. |
| MaxKeyframeSpacing | dword | Maximum number of frames from one key frame to the next. |
| MinimumDisplayAperture | byte[] | Minimum display aperture. |
| MpegSequenceHeader | byte[] | MPEG-1 or MPEG-2 sequence header. |
| MpegStartTimeCode | dword | Group-of-pictures (GOP) start time code. |
| Mpeg2Flags | dword | Miscellaneous flags for MPEG-2 video. |
| Mpeg2Level | dword | MPEG-2 or H.264 level. |
| Mpeg2Profile | dword | MPEG-2 or H.264 profile. |
| Original4cc | dword | Contains the original codec FOURCC for a video stream. |
| PadControlFlags | dword | Aspect ratio of the output rectangle. |
| Palette | dword | Palette entries. |
| PanScanAperture | dword | Defines the 4×3 region of video that should be displayed in pan/scan mode. |
| PanScanEnabled | dword | Specifies whether pan/scan mode is enabled. |
| PixelAspectRatio | qword | Pixel aspect ratio. |
| SourceContentHint | dword | Intended aspect ratio. |
| TransferFunction | dword | Conversion function from RGB to R'G'B'. |
| Video3d | dword | Specifies whether a video stream contains 3D content. |
| VideoChromaSiting | dword | Describes how chroma was sampled for Y'Cb'Cr' video. |
| VideoLighting | dword | Optimal lighting conditions for viewing. |
| VideoNominalRange | dword | Nominal range of the color information. |
| VideoPrimaries | dword | Color primaries. |
| VideoRotation | dword | Specifies the rotation of a video frame in the counter-clockwise direction. |
| YuvMatrix | dword | Conversion matrix from the Y'Cb'Cr' color space to the R'G'B' color space. |

| Functions | Type | Short Description |
|---|---|---|
| DvAauxSrcPack0 | dword | Audio auxiliary (AAUX) source control pack for the first audio block. |
| DvAauxCtrlPack0 | dword | AAUX source control pack for the second audio block. |
| DvAauxSrcPack1 | dword | AAUX source pack for the first audio block. |
| DvAauxCtrlPack1 | dword | AAUX source pack for the second audio block. |
| DvVauxSrcPack | dword | Video auxiliary (VAUX) source control pack. |
| DvVauxCtrlPack | dword | VAUX source pack. |

| Functions | Type | Short Description |
|---|---|---|
| ArbitraryFormat | byte[] | Additional format data for a binary stream in an ASF file. |
| ArbitraryHeader | byte[] | Type-specific data for a binary stream in an ASF file. |
| ImageLossTolerant | dword | Specifies whether an ASF image stream is a degradable JPEG type. |

| Functions | Type | Short Description |
|---|---|---|
| Mpeg4CurrentSampleEntry | dword | The index of the current entry in the sample description box. |
| Mpeg4SampleDescription | byte[] | The sample description box. |

| Functions | Type | Short Description |
|---|---|---|
| TimestampInterval | dword | Number of events between each timestamp. |
| TimestampRate | qword | Event rate for the timestamp stream. |
| TimestampType | dword | Event type for the timestamp stream. |

| Version 15© Vector Informatik GmbH |
|---|
