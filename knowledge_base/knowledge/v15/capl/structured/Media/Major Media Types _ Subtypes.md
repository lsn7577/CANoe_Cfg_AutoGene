# Major Media Types / Subtypes

> Category: `Media` | Type: `notes`

## Description

In a media type, the major type describes the overall category of the data, such as audio or video. The subtype, if present, further refines the major type. For example, if the major type is video, the subtype might be 32-bit RGB video. Subtypes also distinguish encoded formats, such as H.264 video, from uncompressed formats.

Major type and subtype are identified by strings and stored in the following properties:

You can use the following major types:

The following audio subtype strings are defined. To specify the subtype, set the Subtype property on the media type.

When these subtypes are used, set the MajorType property to MediaType_Audio.

The following stream subtype strings are defined. To specify the subtype, set the Subtype property on the media type.

When these subtypes are used, set the MajorType property to MediaType_Stream.

The following timestamp subtype strings are defined. To specify the subtype, set the Sub-type property on the media type.

When these subtypes are used, set the MajorType property to MediaType_Timestamp.

The following video subtype strings are defined. To specify the subtype, set the Subtype property on the media type.

When these subtypes are used, set the MajorType property to MediaType_Video.

Media CAPL Functions

| Property | Description |
|---|---|
| MajorType | Major type |
| Subtype | Subtype |

| Major Type | Description | Subtypes |
|---|---|---|
| MediaType_Audio | Audio | Audio Subtypes |
| MediaType_Stream | Multiplexed stream or elementary stream | Stream Subtypes |
| MediaType_Timestamp | Stream delivering timestamp values | Timestamp Subtypes |
| MediaType_Video | Video | Video Subtypes |

| String | Description | Format Tag (FOURCC) |
|---|---|---|
| AudioFormat_AAC | Advanced Audio Coding (AAC). The stream can contain raw AAC data or AAC data in an Audio Data Transport Stream (ADTS) stream. | 0x1610 |
| AudioFormat_ADTS | Not used. | 0x1600 |
| AudioFormat_ALAC | Apple Lossless Audio Codec Supported in Windows 10 and later. | 0x6C61 |
| AudioFormat_AMR_NB | Adaptative Multi-Rate audio Supported in Windows 8.1 and later. | 0x0057 |
| AudioFormat_AMR_WB | Adaptative Multi-Rate Wideband audio Supported in Windows 8.1 and later. | 0x0058 |
| AudioFormat_AMR_WP | Supported in Windows 8.1 and later. | 0x7363 |
| AudioFormat_Dolby_AC3 | Dolby Digital (AC-3). | None |
| AudioFormat_Dolby_AC3_SPDIF | Dolby AC-3 audio over Sony/Philips Digital Interface (S/PDIF). | 0x0092 |
| AudioFormat_Dolby_DDPlus | Dolby Digital Plus. | None |
| AudioFormat_DRM | Encrypted audio data used with secure audio path. | 0x0009 |
| AudioFormat_DTS | Digital Theater Systems (DTS) audio. | 0x0008 |
| AudioFormat_FLAC | Free Lossless Audio Codec Supported in Windows 10 and later. | 0xF1AC |
| AudioFormat_Float | Uncompressed IEEE floating-point audio. | 0x0003 |
| AudioFormat_MP3 | MPEG Audio Layer-3 (MP3). | 0x0055 |
| AudioFormat_MPEG | MPEG-1 audio payload. | 0x0050 |
| AudioFormat_MSP | Windows Media Audio 9 Voice codec. | 0x000A |
| AudioFormat_Opus | Opus Supported in Windows 10 and later. | 0x704F |
| AudioFormat_PCM | Uncompressed PCM audio. | 1 |
| AudioFormat_QCELP | QCELP (Qualcomm Code Excited Linear Prediction) audio. | None |
| AudioFormat_WMASPDIF | Windows Media Audio 9 Professional codec over S/PDIF. | 0x0164 |
| AudioFormat_WMAudio_Lossless | Windows Media Audio 9 Lossless codec or Windows Media Audio 9.1 codec. | 0x0163 |
| AudioFormat_WMAudioV8 | Windows Media Audio 8 codec, Windows Media Audio 9 codec, or Windows Media Audio 9.1 codec. | 0x0161 |
| AudioFormat_WMAudioV9 | Windows Media Audio 9 Professional codec or Windows Media Audio 9.1 Professional codec. | 0x0162 |

| String | Description |
|---|---|
| StreamFormat_MPEG2Transport | MPEG-2 transport stream. |
| StreamFormat_MPEG2Program | MPEG-2 program stream. |

| Notes Reading samples from an MPEG2-transport/program stream is not (yet) possible by use of a Media Source Reader created by MediaCreateSourceReaderFromUrl since Windows does not provide an appropriate Media Source. For obtaining samples from a file containing MPEG2-transport/program stream data you can use the File Functions in CAPL. |
|---|

| String | Description | Resolution | Epoch | Time Base |
|---|---|---|---|---|
| TimestampFormat_PTP | PTP timestamp stream. | 64 Bit / 1 ns | Unix (Midnight, 1 January 1970) | International Atomic Time (TAI) |

| String | Description |
|---|---|
| VideoFormat_RGB8 | RGB, 8 bits per pixel (bpp). |
| VideoFormat_RGB555 | RGB 555, 16 bpp. |
| VideoFormat_RGB565 | RGB 565, 16 bpp. |
| VideoFormat_RGB24 | RGB, 24 bpp. |
| VideoFormat_RGB32 | RGB, 32 bpp. |
| VideoFormat_ARGB32 | RGB, 32 bpp with alpha channel. |

| String | Format | Sampling | Packed or Planar | Bits per Channel |
|---|---|---|---|---|
| VideoFormat_AI44 | AI44 | 4:4:4 | Packed | Palettized |
| VideoFormat_AYUV | AYUV | 4:4:4 | Packed | 8 |
| VideoFormat_I420 | I420 | 4:2:0 | Planar | 8 |
| VideoFormat_IYUV | IYUV | 4:2:0 | Planar | 8 |
| VideoFormat_NV11 | NV11 | 4:1:1 | Planar | 8 |
| VideoFormat_NV12 | NV12 | 4:2:0 | Planar | 8 |
| VideoFormat_UYVY | UYVY | 4:2:2 | Packed | 8 |
| VideoFormat_Y41P | Y41P | 4:1:1 | Packed | 8 |
| VideoFormat_Y41T | Y41T | 4:1:1 | Packed | 8 |
| VideoFormat_Y42T | Y42T | 4:2:2 | Packed | 8 |
| VideoFormat_YUY2 | YUY2 | 4:2:2 | Packed | 8 |
| VideoFormat_YVU9 | YVU9 | 8:4:4 | Planar | 9 |
| VideoFormat_YV12 | YV12 | 4:2:0 | Planar | 8 |
| VideoFormat_YVYU | YVYU | 4:2:2 | Packed | 8 |

| String | Format | Sampling | Packed or Planar | Bits per Channel |
|---|---|---|---|---|
| VideoFormat_P010 | P010 | 4:2:0 | Planar | 10 |
| VideoFormat_P016 | P016 | 4:2:0 | Planar | 16 |
| VideoFormat_P210 | P210 | 4:2:2 | Planar | 10 |
| VideoFormat_P216 | P216 | 4:2:2 | Planar | 16 |
| VideoFormat_v210 | v210 | 4:2:2 | Packed | 10 |
| VideoFormat_v216 | v216 | 4:2:2 | Packed | 16 |
| VideoFormat_v40 | v40 | 4:4:4 | Packed | 10 |
| VideoFormat_Y210 | Y210 | 4:2:2 | Packed | 10 |
| VideoFormat_Y216 | Y216 | 4:2:2 | Packed | 16 |
| VideoFormat_Y40 | Y40 | 4:4:4 | Packed | 10 |
| VideoFormat_Y416 | Y416 | 4:4:4 | Packed | 16 |

| String | Description |
|---|---|
| VideoFormat_L8 | 8-bit luminance only. (bpp). |
| VideoFormat_L16 | 16-bit luminance only. |
| VideoFormat_D16 | 16-bit z-buffer depth. |

| String | Description | Format Tag (FOURCC) |
|---|---|---|
| VideoFormat_DV25 | DVCPRO 25 (525-60 or 625-50). | 'dv25' |
| VideoFormat_DV50 | DVCPRO 50 (525-60 or 625-50). | 'dv50' |
| VideoFormat_DVC | DVC/DV Video. | 'dvc ' |
| VideoFormat_DVH1 | DVCPRO 100 (1080/60i, 1080/50i, or 720/60P). | 'dvh1' |
| VideoFormat_DVHD | HD-DVCR (1125-60 or 1250-50). | 'dvhd' |
| VideoFormat_DVSD | SDL-DVCR (525-60 or 625-50). | 'dvsd' |
| VideoFormat_DVSL | SD-DVCR (525-60 or 625-50). | 'dvsl' |
| VideoFormat_H263 | H.263 video. | 'H263' |
| VideoFormat_H264 | H.264-Video.Media samples contain H.264 bitstream data with start codes and has interleaved SPS/PPS. Each sample contains one complete picture, either one field or one frame. | 'H264' |
| VideoFormat_H265 | H.265 video. | 'H265' |
| VideoFormat_H264_ES | H.264 elementary stream.This media type is the same as MFVideoFormat_H264, except media samples contain a fragmented H.264 bitstream. Each sample may contain a partial picture; multiple complete pictures; or one or more complete pictures plus a partial picture. | Not applicable |
| VideoFormat_HEVC | The HEVC Main profile and Main Still Picture profile.Each sample contains one complete picture. Supported in Windows 8.1 and later. The HEVC Main profile and Main Still Picture profile elementary stream. | 'HEVC' |
| VideoFormat_HEVC_ES | This media type is the same as MFVideoFormat_HEVC, except media samples contain a fragmented HEVC bitstream. Each sample may contain a partial picture; multiple complete pictures; or one or more complete pictures plus a partial picture. Supported in Windows 8.1 and later. | 'HEVS' |
| VideoFormat_M4S2 | MPEG-4 part 2 video. | 'M4S2' |
| VideoFormat _ MJPG | Motion JPEG. | 'MJPG' |
| VideoFormat_MP43 | Microsoft MPEG 4 codec version 3. This codec is no longer supported. | 'MP43' |
| VideoFormat_MP4S | ISO MPEG 4 codec version 1. | 'MP4S' |
| VideoFormat_MP4V | MPEG-4 part 2 video. | 'MP4V' |
| VideoFormat_MPEG2 | MPEG-2 video. | Not applicable |
| VideoFormat_VP80 | VP8 video. | 'MPG1' |
| VideoFormat_VP90 | VP9 video. | 'MPG1' |
| VideoFormat_MPG1 | MPEG-1 video. | 'MPG1' |
| VideoFormat_MSS1 | Windows Media Screen codec version 1. | 'MSS1' |
| VideoFormat_MSS2 | Windows Media Video 9 Screen codec. | 'MSS2' |
| VideoFormat_WMV1 | Windows Media Video codec version 7. | 'WMV1' |
| VideoFormat_WMV2 | Windows Media Video 8 codec. | 'WMV2' |
| VideoFormat_WMV3 | Windows Media Video 9 codec. | 'WMV3' |
| VideoFormat_WVC1 | SMPTE 421M ("VC-1"). | 'WVC1' |
| VideoFormat_420O | 8-bit per channel planar YUV 4:2:0 video. | '420O' |

| Version 15© Vector Informatik GmbH |
|---|
