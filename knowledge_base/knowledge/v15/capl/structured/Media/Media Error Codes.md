# Media Error Codes

> Category: `Media` | Type: `notes`

## Description

For your convenience, the Media Foundation Error Codes are re-printed from the Windows SDK/MSDN online library.

| Return Code | Value | Description |
|---|---|---|
| S_OK | 0 | Success/no error. |

| Return Code | Value | Description |
|---|---|---|
| MF_E_PLATFORM_NOT_INITIALIZED | 0xC00D36B0 | Platform not initialized. Please call MFStartup. |
| MF_E_BUFFERTOOSMALL | 0xC00D36B1 | The buffer was too small to execute the requested action. |
| MF_E_INVALIDREQUEST | 0xC00D36B2 | The request is invalid in the current state. |
| MF_E_INVALIDSTREAMNUMBER | 0xC00D36B3 | The stream number provided was invalid. |
| MF_E_INVALIDMEDIATYPE | 0xC00D36B4 | The data specified for the media type is invalid, inconsistent, or not supported by this object. |
| MF_E_NOTACCEPTING | 0xC00D36B5 | The call is currently not accepting further input. |
| MF_E_NOT_INITIALIZED | 0xC00D36B6 | This object needs to be initialized before the requested operation can be carried out. |
| MF_E_UNSUPPORTED_REPRESENTATION | 0xC00D36B7 | The requested representation is not supported by this object. |
| MF_E_NO_MORE_TYPES | 0xC00D36B9 | An object ran out of media types to suggest therefore the requested chain of streaming objects cannot be completed. |
| MF_E_UNSUPPORTED_SERVICE | 0xC00D36BA | The object does not support the specified service. |
| MF_E_UNEXPECTED | 0xC00D36BB | An unexpected error has occurred in the operation requested. |
| MF_E_INVALIDNAME | 0xC00D36BC | Invalid name. |
| MF_E_INVALIDTYPE | 0xC00D36BD | Invalid type. |
| MF_E_INVALID_FILE_FORMAT | 0xC00D36BE | The file does not conform to the relevant file format specification. |
| MF_E_INVALIDINDEX | 0xC00D36BF | Invalid index. |
| MF_E_INVALID_TIMESTAMP | 0xC00D36C0 | An invalid time stamp was given. |
| MF_E_UNSUPPORTED_SCHEME | 0xC00D36C3 | The scheme of the given URL is unsupported. |
| MF_E_UNSUPPORTED_BYTESTREAM | 0xC00D36C4 | The byte stream type of the given URL is unsupported. |
| MF_E_UNSUPPORTED_TIME_FORMAT | 0xC00D36C5 | The given time format is unsupported. |
| MF_E_NO_SAMPLE_TIMESTAMP | 0xC00D36C8 | The Media Sample does not have a time stamp. |
| MF_E_NO_SAMPLE_DURATION | 0xC00D36C9 | The Media Sample does not have a duration. |
| MF_E_INVALID_STREAM_DATA | 0xC00D36CB | The request failed because the data in the stream is corrupt. |
| MF_E_RT_UNAVAILABLE | 0xC00D36CF | Real time services are not available. |
| MF_E_UNSUPPORTED_RATE | 0xC00D36D0 | The specified rate is not supported. |
| MF_E_THINNING_UNSUPPORTED | 0xC00D36D1 | This component does not support stream-thinning. |
| MF_E_REVERSE_UNSUPPORTED | 0xC00D36D2 | The call failed because no reverse playback rates are available. |
| MF_E_UNSUPPORTED_RATE_TRANSITION | 0xC00D36D3 | The requested rate transition cannot occur in the current state. |
| MF_E_RATE_CHANGE_PREEMPTED | 0xC00D36D4 | The requested rate change has been pre-empted and will not occur. |
| MF_E_NOT_FOUND | 0xC00D36D5 | The specified object or value does not exist. |
| MF_E_NOT_AVAILABLE | 0xC00D36D6 | The requested value is not available. |
| MF_E_NO_CLOCK | 0xC00D36D7 | The specified operation requires a clock and no clock is available. |
| MF_S_MULTIPLE_BEGIN | 0x000D36D8 | This callback and state had already been passed in to this event generator earlier. |
| MF_E_MULTIPLE_BEGIN | 0xC00D36D9 | This callback has already been passed in to this event generator. |
| MF_E_MULTIPLE_SUBSCRIBERS | 0xC00D36DA | Some component is already listening to events on this event generator. |
| MF_E_TIMER_ORPHANED | 0xC00D36DB | This timer was orphaned before its callback time arrived. |
| MF_E_STATE_TRANSITION_PENDING | 0xC00D36DC | A state transition is already pending. |
| MF_E_UNSUPPORTED_STATE_TRANSITION | 0xC00D36DD | The requested state transition is unsupported. |
| MF_E_UNRECOVERABLE_ERROR_OCCURRED | 0xC00D36DE | An unrecoverable error has occurred. |
| MF_E_SAMPLE_HAS_TOO_MANY_BUFFERS | 0xC00D36DF | The provided sample has too many buffers. |
| MF_E_SAMPLE_NOT_WRITABLE | 0xC00D36E0 | The provided sample is not writable. |
| MF_E_INVALID_KEY | 0xC00D36E2 | The specified key is not valid. |
| MF_E_BAD_STARTUP_VERSION | 0xC00D36E3 | You are calling MFStartup with the wrong MF_VERSION. Mismatched bits? |
| MF_E_UNSUPPORTED_CAPTION | 0xC00D36E4 | The caption of the given URL is unsupported. |
| MF_E_INVALID_POSITION | 0xC00D36E5 | The operation on the current offset is not permit-ted. |
| MF_E_ATTRIBUTENOTFOUND | 0xC00D36E6 | The requested attribute was not found. |
| MF_E_PROPERTY_TYPE_NOT_ALLOWED | 0xC00D36E7 | The specified property type is not allowed in this context. |
| MF_E_PROPERTY_TYPE_NOT_SUPPORTED | 0xC00D36E8 | The specified property type is not supported. |
| MF_E_PROPERTY_EMPTY | 0xC00D36E9 | The specified property is empty. |
| MF_E_PROPERTY_NOT_EMPTY | 0xC00D36EA | The specified property is not empty. |
| MF_E_PROPERTY_VECTOR_NOT_ALLOWED | 0xC00D36EB | The vector property specified is not allowed in this context. |
| MF_E_PROPERTY_VECTOR_REQUIRED | 0xC00D36EC | A vector property is required in this context. |
| MF_E_OPERATION_CANCELLED | 0xC00D36ED | The operation is canceled. |
| MF_E_BYTESTREAM_NOT_SEEKABLE | 0xC00D36EE | The provided byte stream was expected to be seekable and it is not. |
| MF_E_DISABLED_IN_SAFEMODE | 0xC00D36EF | The Media Foundation platform is disabled when the system is running in Safe Mode. |
| MF_E_CANNOT_PARSE_BYTESTREAM | 0xC00D36F0 | The Media Source could not parse the byte stream. |
| MF_E_SOURCERESOLVER_MUTUALLY_EXCLUSIVE_FLAGS | 0xC00D36F1 | Mutually exclusive flags have been specified to source resolver. This flag combination is invalid. |
| MF_E_MEDIAPROC_WRONGSTATE | 0xC00D36F2 | MediaProc is in the wrong state. |
| MF_E_RT_THROUGHPUT_NOT_AVAILABLE | 0xC00D36F3 | Real time I/O service can not provide requested throughput. |
| MF_E_RT_TOO_MANY_CLASSES | 0xC00D36F4 | The work queue cannot be registered with more classes. |
| MF_E_RT_WOULDBLOCK | 0xC00D36F5 | This operation cannot succeed because another thread owns this object. |
| MF_E_NO_BITPUMP | 0xC00D36F6 | Internal. Bitpump not found. |
| MF_E_RT_OUTOFMEMORY | 0xC00D36F7 | No more RT memory available. |
| MF_E_RT_WORKQUEUE_CLASS_NOT_SPECIFIED | 0xC00D36F8 | An MMCSS class has not been set for this work queue. |
| MF_E_INSUFFICIENT_BUFFER | 0xC00D7170 | Insufficient memory for response. |
| MF_E_CANNOT_CREATE_SINK | 0xC00D36FA | Activate failed to create media sink.Call Output-Node::GetUINT32(MF_TOPONODE_MAJORTYPE) for more information. |
| MF_E_BYTESTREAM_UNKNOWN_LENGTH | 0xC00D36FB | The length of the provided byte stream is unknown. |
| MF_E_SESSION_PAUSEWHILESTOPPED | 0xC00D36FC | The media session cannot pause from a stopped state. |
| MF_S_ACTIVATE_REPLACED | 0x000D36FD | The activate could not be created in the remote process for some reason it was replaced with empty one. |
| MF_E_FORMAT_CHANGE_NOT_SUPPORTED | 0xC00D36FE | The data specified for the media type is support-ed, but would require a format change, which is not supported by this object. |
| MF_E_INVALID_WORKQUEUE | 0xC00D36FF | The operation failed because an invalid combination of work queue ID and flags was specified. |
| MF_E_DRM_UNSUPPORTED | 0xC00D3700 | No DRM support is available. |
| MF_E_UNAUTHORIZED | 0xC00D3701 | This operation is not authorized. |
| MF_E_OUT_OF_RANGE | 0xC00D3702 | The value is not in the specified or valid range. |
| MF_E_INVALID_CODEC_MERIT | 0xC00D3703 | The registered codec merit is not valid. |
| MF_E_HW_MFT_FAILED_START_STREAMING | 0xC00D3704 | Hardware MFT failed to start streaming due to lack of hardware resources. |

| Return Code | Value | Description |
|---|---|---|
| MF_S_ASF_PARSEINPROGRESS | 0x400D3A98 | Parsing is still in progress and is not yet complete. |
| MF_E_ASF_PARSINGINCOMPLETE | 0xC00D3A98 | Not enough data have been parsed to execute the requested action. |
| MF_E_ASF_MISSINGDATA | 0xC00D3A99 | There is a gap in the ASF data provided. |
| MF_E_ASF_INVALIDDATA | 0xC00D3A9A | The data provided are not valid ASF. |
| MF_E_ASF_OPAQUEPACKET | 0xC00D3A9B | The packet is opaque, so the requested information cannot be returned. |
| MF_E_ASF_NOINDEX | 0xC00D3A9C | The requested operation failed since there is no appropriate ASF index. |
| MF_E_ASF_OUTOFRANGE | 0xC00D3A9D | The value supplied is out of range for this operation. |
| MF_E_ASF_INDEXNOTLOADED | 0xC00D3A9E | The index entry requested needs to be loaded before it can be available. |
| MF_E_ASF_TOO_MANY_PAYLOADS | 0xC00D3A9F | The packet has reached the maximum number of payloads. |
| MF_E_ASF_UNSUPPORTED_STREAM_TYPE | 0xC00D3AA0 | Stream type is not supported. |
| MF_E_ASF_DROPPED_PACKET | 0xC00D3AA1 | One or more ASF packets were dropped. |

| Return Code | Value | Description |
|---|---|---|
| MF_E_NO_EVENTS_AVAILABLE | 0xC00D3E80 | There are no events available in the queue. |
| MF_E_INVALID_STATE_TRANSITION | 0xC00D3E82 | A media source cannot go from the stopped state to the paused state. |
| MF_E_END_OF_STREAM | 0xC00D3E84 | The media stream cannot process any more samples because there are no more samples in the stream. |
| MF_E_SHUTDOWN | 0xC00D3E85 | The request is invalid because Shutdown() has been called. |
| MF_E_MP3_NOTFOUND | 0xC00D3E86 | The MP3 object was not found. |
| MF_E_MP3_OUTOFDATA | 0xC00D3E87 | The MP3 parser ran out of data before finding the MP3 object. |
| MF_E_MP3_NOTMP3 | 0xC00D3E88 | The file is not really a MP3 file. |
| MF_E_MP3_NOTSUPPORTED | 0xC00D3E89 | The MP3 file is not supported. |
| MF_E_NO_DURATION | 0xC00D3E8A | The Media stream has no duration. |
| MF_E_INVALID_FORMAT | 0xC00D3E8C | The Media format is recognized but is invalid. |
| MF_E_PROPERTY_NOT_FOUND | 0xC00D3E8D | The property requested was not found. |
| MF_E_PROPERTY_READ_ONLY | 0xC00D3E8E | The property is read only. |
| MF_E_PROPERTY_NOT_ALLOWED | 0xC00D3E8F | The specified property is not allowed in this context. |
| MF_E_MEDIA_SOURCE_NOT_STARTED | 0xC00D3E91 | The media source is not started. |
| MF_E_UNSUPPORTED_FORMAT | 0xC00D3E98 | The Media format is recognized but not supported. |
| MF_E_MP3_BAD_CRC | 0xC00D3E99 | The MPEG frame has bad CRC. |
| MF_E_NOT_PROTECTED | 0xC00D3E9A | The file is not protected. |
| MF_E_MEDIA_SOURCE_WRONGSTATE | 0xC00D3E9B | The media source is in the wrong state. |
| MF_E_MEDIA_SOURCE_NO_STREAMS_SELECTED | 0xC00D3E9C | No streams are selected in source presentation descriptor. |
| MF_E_CANNOT_FIND_KEYFRAME_SAMPLE | 0xC00D3E9D | No key frame sample was found. |

| Return Code | Value | Description |
|---|---|---|
| MF_E_NETWORK_RESOURCE_FAILURE | 0xC00D4268 | An attempt to acquire a network resource failed. |
| MF_E_NET_WRITE | 0xC00D4269 | Error writing to the network. |
| MF_E_NET_READ | 0xC00D426A | Error reading from the network. |
| MF_E_NET_REQUIRE_NETWORK | 0xC00D426B | Internal. Entry cannot complete operation without network. |
| MF_E_NET_REQUIRE_ASYNC | 0xC00D426C | Internal. Async op is required. |
| MF_E_NET_BWLEVEL_NOT_SUPPORTED | 0xC00D426D | Internal. Bandwidth levels are not supported. |
| MF_E_NET_STREAMGROUPS_NOT_SUPPORTED | 0xC00D426E | Internal. Stream groups are not supported. |
| MF_E_NET_MANUALSS_NOT_SUPPORTED | 0xC00D426F | Manual stream selection is not supported. |
| MF_E_NET_INVALID_PRESENTATION_DESCRIPTOR | 0xC00D4270 | Invalid presentation descriptor. |
| MF_E_NET_CACHESTREAM_NOT_FOUND | 0xC00D4271 | Cannot find cache stream. |
| MF_I_MANUAL_PROXY | 0x400D4272 | The proxy setting is manual. |
| MF_E_NET_REQUIRE_INPUT | 0xC00D4274 | Internal. Entry cannot complete operation without input. |
| MF_E_NET_REDIRECT | 0xC00D4275 | The client redirected to another server. |
| MF_E_NET_REDIRECT_TO_PROXY | 0xC00D4276 | The client is redirected to a proxy server. |
| MF_E_NET_TOO_MANY_REDIRECTS | 0xC00D4277 | The client reached maximum redirection limit. |
| MF_E_NET_TIMEOUT | 0xC00D4278 | The server, a computer set up to offer multimedia content to other computers, could not handle your request for multimedia content in a timely manner. Please try again later. |
| MF_E_NET_CLIENT_CLOSE | 0xC00D4279 | The control socket is closed by the client. |
| MF_E_NET_BAD_CONTROL_DATA | 0xC00D427A | The server received invalid data from the client on the control connection. |
| MF_E_NET_INCOMPATIBLE_SERVER | 0xC00D427B | The server is not a compatible streaming media server. |
| MF_E_NET_UNSAFE_URL | 0xC00D427C | Url. |
| MF_E_NET_CACHE_NO_DATA | 0xC00D427D | Data is not available. |
| MF_E_NET_EOL | 0xC00D427E | End of line. |
| MF_E_NET_BAD_REQUEST | 0xC00D427F | The request could not be understood by the server. |
| MF_E_NET_INTERNAL_SERVER_ERROR | 0xC00D4280 | The server encountered an unexpected condition which prevented it from fulfilling the request. |
| MF_E_NET_SESSION_NOT_FOUND | 0xC00D4281 | Session not found. |
| MF_E_NET_NOCONNECTION | 0xC00D4282 | There is no connection established with the Windows Media server. The operation failed. |
| MF_E_NET_CONNECTION_FAILURE | 0xC00D4283 | The network connection has failed. |
| MF_E_NET_INCOMPATIBLE_PUSHSERVER | 0xC00D4284 | The Server service that received the HTTP push request is not a compatible version of Windows Media Services (WMS). This error may indicate the push request was received by IIS instead of WMS. Ensure WMS is started and has the HTTP Server control protocol properly enabled and try again. |
| MF_E_NET_SERVER_ACCESSDENIED | 0xC00D4285 | The Windows Media server is denying access. The username and/or password might be incorrect. |
| MF_E_NET_PROXY_ACCESSDENIED | 0xC00D4286 | The proxy server is denying access. The username and/or password might be incorrect. |
| MF_E_NET_CANNOTCONNECT | 0xC00D4287 | Unable to establish a connection to the server. |
| MF_E_NET_INVALID_PUSH_TEMPLATE | 0xC00D4288 | The specified push template is invalid. |
| MF_E_NET_INVALID_PUSH_PUBLISHING_POINT | 0xC00D4289 | The specified push publishing point is invalid. |
| MF_E_NET_BUSY | 0xC00D428A | The requested resource is in use. |
| MF_E_NET_RESOURCE_GONE | 0xC00D428B | The Publishing Point or file on the Windows Media Server is no longer available. |
| MF_E_NET_ERROR_FROM_PROXY | 0xC00D428C | The proxy experienced an error while attempting to contact the media server. |
| MF_E_NET_PROXY_TIMEOUT | 0xC00D428D | The proxy did not receive a timely response while attempting to contact the media server. |
| MF_E_NET_SERVER_UNAVAILABLE | 0xC00D428E | The server is currently unable to handle the request due to a temporary overloading or maintenance of the server. |
| MF_E_NET_TOO_MUCH_DATA | 0xC00D428F | The encoding process was unable to keep up with the amount of supplied data. |
| MF_E_NET_SESSION_INVALID | 0xC00D4290 | Session not found. |
| MF_E_OFFLINE_MODE | 0xC00D4291 | The requested URL is not available in offline mode. |
| MF_E_NET_UDP_BLOCKED | 0xC00D4292 | A device in the network is blocking UDP traffic. |
| MF_E_NET_UNSUPPORTED_CONFIGURATION | 0xC00D4293 | The specified configuration value is not supported. |
| MF_E_NET_PROTOCOL_DISABLED | 0xC00D4294 | The networking protocol is disabled. |

| Return Code | Value | Description |
|---|---|---|
| MF_E_ALREADY_INITIALIZED | 0xC00D4650 | This object has already been initialized and cannot be re-initialized at this time. |
| MF_E_BANDWIDTH_OVERRUN | 0xC00D4651 | The amount of data passed in exceeds the given bitrate and buffer window. |
| MF_E_LATE_SAMPLE | 0xC00D4652 | The sample was passed in too late to be correctly processed. |
| MF_E_FLUSH_NEEDED | 0xC00D4653 | The requested action cannot be carried out until the object is flushed and the queue is emptied. |
| MF_E_INVALID_PROFILE | 0xC00D4654 | The profile is invalid. |
| MF_E_INDEX_NOT_COMMITTED | 0xC00D4655 | The index that is being generated needs to be committed before the requested action can be carried out. |
| MF_E_NO_INDEX | 0xC00D4656 | The index that is necessary for the requested action is not found. |
| MF_E_CANNOT_INDEX_IN_PLACE | 0xC00D4657 | The requested index cannot be added in-place to the specified ASF content. |
| MF_E_MISSING_ASF_LEAKYBUCKET | 0xC00D4658 | The ASF leaky bucket parameters must be specified in order to execute this request. |
| MF_E_INVALID_ASF_STREAMID | 0xC00D4659 | The stream id is invalid. The valid range for ASF stream id is from 1 to 127. |

| Return Code | Value | Description |
|---|---|---|
| MF_E_STREAMSINK_REMOVED | 0xC00D4A38 | The requested Stream Sink has been removed and cannot be used. |
| MF_E_STREAMSINKS_OUT_OF_SYNC | 0xC00D4A3A | The various Stream Sinks in this Media Sink are too far out of sync for the requested action to take place. |
| MF_E_STREAMSINKS_FIXED | 0xC00D4A3B | Stream Sinks cannot be added to or removed from this Media Sink because its set of streams is fixed. |
| MF_E_STREAMSINK_EXISTS | 0xC00D4A3C | The given Stream Sink already exists. |
| MF_E_SAMPLEALLOCATOR_CANCELED | 0xC00D4A3D | Sample allocations have been canceled. |
| MF_E_SAMPLEALLOCATOR_EMPTY | 0xC00D4A3E | The sample allocator is currently empty, due to outstanding requests. |
| MF_E_SINK_ALREADYSTOPPED | 0xC00D4A3F | When we try to sopt a stream sink, it is already stopped. |
| MF_E_ASF_FILESINK_BITRATE_UNKNOWN | 0xC00D4A40 | The ASF file sink could not reserve AVIO because the bitrate is unknown. |
| MF_E_SINK_NO_STREAMS | 0xC00D4A41 | No streams are selected in sink presentation descriptor. |
| MF_S_SINK_NOT_FINALIZED | 0x000D4A42 | The sink has not been finalized before shut down. This may cause sink generate a corrupted content. |
| MF_E_METADATA_TOO_LONG | 0xC00D4A43 | A metadata item was too long to write to the output container. |
| MF_E_SINK_NO_SAMPLES_PROCESSED | 0xC00D4A44 | The operation failed because no samples were processed by the sink. |

| Return Code | Value | Description |
|---|---|---|
| MF_E_VIDEO_REN_NO_PROCAMP_HW | 0xC00D4E20 | There is no available procamp hardware with which to perform color correction. |
| MF_E_VIDEO_REN_NO_DEINTERLACE_HW | 0xC00D4E21 | There is no available deinterlacing hardware with which to deinterlace the video stream. |
| MF_E_VIDEO_REN_COPYPROT_FAILED | 0xC00D4E22 | A video stream requires copy protection to be enabled, but there was a failure in attempting to enable copy protection. |
| MF_E_VIDEO_REN_SURFACE_NOT_SHARED | 0xC00D4E23 | A component is attempting to access a surface for sharing that is not shared. |
| MF_E_VIDEO_DEVICE_LOCKED | 0xC00D4E24 | A component is attempting to access a shared device that is already locked by another component. |
| MF_E_NEW_VIDEO_DEVICE | 0xC00D4E25 | The device is no longer available. The handle should be closed and a new one opened. |
| MF_E_NO_VIDEO_SAMPLE_AVAILABLE | 0xC00D4E26 | A video sample is not currently queued on a stream that is required for mixing. |
| MF_E_NO_AUDIO_PLAYBACK_DEVICE | 0xC00D4E84 | No audio playback device was found. |
| MF_E_AUDIO_PLAYBACK_DEVICE_IN_USE | 0xC00D4E85 | The requested audio playback device is currently in use. |
| MF_E_AUDIO_PLAYBACK_DEVICE_INVALIDATED | 0xC00D4E86 | The audio playback device is no longer present. |
| MF_E_AUDIO_SERVICE_NOT_RUNNING | 0xC00D4E87 | The audio service is not running. |

| Return Code | Value | Description |
|---|---|---|
| MF_E_TOPO_INVALID_OPTIONAL_NODE | 0xC00D520E | The topology contains an invalid optional node. Possible reasons are incorrect number of outputs and inputs or optional node is at the beginning or end of a segment. |
| MF_E_TOPO_CANNOT_FIND_DECRYPTOR | 0xC00D5211 | No suitable transform was found to decrypt the content. |
| MF_E_TOPO_CODEC_NOT_FOUND | 0xC00D5212 | No suitable transform was found to encode or decode the content. |
| MF_E_TOPO_CANNOT_CONNECT | 0xC00D5213 | Unable to find a way to connect nodes. |
| MF_E_TOPO_UNSUPPORTED | 0xC00D5214 | Unsupported operations in topoloader. |
| MF_E_TOPO_INVALID_TIME_ATTRIBUTES | 0xC00D5215 | The topology or its nodes contain incorrectly set time attributes. |
| MF_E_TOPO_LOOPS_IN_TOPOLOGY | 0xC00D5216 | The topology contains loops, which are unsupported in media foundation topologies. |
| MF_E_TOPO_MISSING_PRESENTATION_DESCRIPTOR | 0xC00D5217 | A source stream node in the topology does not have a presentation descriptor. |
| MF_E_TOPO_MISSING_STREAM_DESCRIPTOR | 0xC00D5218 | A source stream node in the topology does not have a stream descriptor. |
| MF_E_TOPO_STREAM_DESCRIPTOR_NOT_SELECTED | 0xC00D5219 | A stream descriptor was set on a source stream node but it was not selected on the presentation descriptor. |
| MF_E_TOPO_MISSING_SOURCE | 0xC00D521A | A source stream node in the topology does not have a source. |
| MF_E_TOPO_SINK_ACTIVATES_UNSUPPORTED | 0xC00D521B | The topology loader does not support sink activates on output nodes. |

| Return Code | Value | Description |
|---|---|---|
| MF_E_SEQUENCER_UNKNOWN_SEGMENT_ID | 0xC00D61AC | The sequencer cannot find a segment with the given ID. |
| MF_S_SEQUENCER_CONTEXT_CANCELED | 0x000D61AD | The context was canceled. |
| MF_E_NO_SOURCE_IN_CACHE | 0xC00D61AE | Cannot find source in source cache. |
| MF_S_SEQUENCER_SEGMENT_AT_END_OF_STREAM | 0x000D61AF | Cannot update topology flags. |

| Return Code | Value | Description |
|---|---|---|
| MF_E_TRANSFORM_TYPE_NOT_SET | 0xC00D6D60 | A valid type has not been set for this stream or a stream that it depends on. |
| MF_E_TRANSFORM_STREAM_CHANGE | 0xC00D6D61 | A stream change has occurred. Output cannot be produced until the streams have been renegotiated. |
| MF_E_TRANSFORM_INPUT_REMAINING | 0xC00D6D62 | The transform cannot take the requested action until all of the input data it currently holds is processed or flushed. |
| MF_E_TRANSFORM_PROFILE_MISSING | 0xC00D6D63 | The transform requires a profile but no profile was supplied or found. |
| MF_E_TRANSFORM_PROFILE_INVALID_OR_CORRUPT | 0xC00D6D64 | The transform requires a profile but the supplied profile was invalid or corrupt. |
| MF_E_TRANSFORM_PROFILE_TRUNCATED | 0xC00D6D65 | The transform requires a profile but the supplied profile ended unexpectedly while parsing. |
| MF_E_TRANSFORM_PROPERTY_PID_NOT_RECOGNIZED | 0xC00D6D66 | The property ID does not match any property supported by the transform. |
| MF_E_TRANSFORM_PROPERTY_VARIANT_TYPE_WRONG | 0xC00D6D67 | The variant does not have the type expected for this property ID. |
| MF_E_TRANSFORM_PROPERTY_NOT_WRITEABLE | 0xC00D6D68 | An attempt was made to set the value on a read-only property. |
| MF_E_TRANSFORM_PROPERTY_ARRAY_VALUE_WRONG_NUM_DIM | 0xC00D6D69 | The array property value has an unexpected number of dimensions. |
| MF_E_TRANSFORM_PROPERTY_VALUE_SIZE_WRONG | 0xC00D6D6A | The array or blob property value has an unexpected size. |
| MF_E_TRANSFORM_PROPERTY_VALUE_OUT_OF_RANGE | 0xC00D6D6B | The property value is out of range for this transform. |
| MF_E_TRANSFORM_PROPERTY_VALUE_INCOMPATIBLE | 0xC00D6D6C | The property value is incompatible with some other property or mediatype set on the transform. |
| MF_E_TRANSFORM_NOT_POSSIBLE_FOR_CURRENT_OUTPUT_MEDIATYPE | 0xC00D6D6D | The requested operation is not supported for the currently set output mediatype. |
| MF_E_TRANSFORM_NOT_POSSIBLE_FOR_CURRENT_INPUT_MEDIATYPE | 0xC00D6D6E | The requested operation is not supported for the currently set input mediatype. |
| MF_E_TRANSFORM_NOT_POSSIBLE_FOR_CURRENT_MEDIATYPE_COMBINATION | 0xC00D6D6F | The requested operation is not supported for the currently set combination of mediatypes. |
| MF_E_TRANSFORM_CONFLICTS_WITH_OTHER_CURRENTLY_ENABLED_FEATURES | 0xC00D6D70 | The requested feature is not supported in combination with some other currently enabled feature. |
| MF_E_TRANSFORM_NEED_MORE_INPUT | 0xC00D6D72 | The transform cannot produce output until it gets more input samples. |
| MF_E_TRANSFORM_NOT_POSSIBLE_FOR_CURRENT_SPKR_CONFIG | 0xC00D6D73 | The requested operation is not supported for the current speaker configuration. |
| MF_E_TRANSFORM_CANNOT_CHANGE_MEDIATYPE_WHILE_PROCESSING | 0xC00D6D74 | The transform cannot accept mediatype changes in the middle of processing. |
| MF_S_TRANSFORM_DO_NOT_PROPAGATE_EVENT | 0x000D6D75L | The caller should not propagate this event to downstream components. |
| MF_E_UNSUPPORTED_D3D_TYPE | 0xC00D6D76 | The input type is not supported for D3D device. |
| MF_E_TRANSFORM_ASYNC_LOCKED | 0xC00D6D77 | The caller does not appear to support this transform's asynchronous capabilities. |
| MF_E_TRANSFORM_CANNOT_INITIALIZE_ACM_DRIVER | 0xC00D6D78 | An audio compression manager driver could not be initialized by the transform. |

| Return Code | Value | Description |
|---|---|---|
| MF_E_LICENSE_INCORRECT_RIGHTS | 0xC00D7148 | You are not allowed to open this file. Contact the content provider for further assistance. |
| MF_E_LICENSE_OUTOFDATE | 0xC00D7149 | The license for this media file has expired. Get a new license or contact the content provider for further assistance. |
| MF_E_LICENSE_REQUIRED | 0xC00D714A | You need a license to perform the requested operation on this media file. |
| MF_E_DRM_HARDWARE_INCONSISTENT | 0xC00D714B | The licenses for your media files are corrupted. Contact Microsoft product support. |
| MF_E_NO_CONTENT_PROTECTION_MANAGER | 0xC00D714C | The APP needs to provide IMFContentProtectionManager callback to access the protected media file. |
| MF_E_LICENSE_RESTORE_NO_RIGHTS | 0xC00D714D | Client does not have rights to restore licenses. |
| MF_E_BACKUP_RESTRICTED_LICENSE | 0xC00D714E | Licenses are restricted and hence can not be backed up. |
| MF_E_LICENSE_RESTORE_NEEDS_INDIVIDUALIZATION | 0xC00D714F | License restore requires machine to be individualized. |
| MF_S_PROTECTION_NOT_REQUIRED | 0x000D7150 | Protection for stream is not required. |
| MF_E_COMPONENT_REVOKED | 0xC00D7151 | Component is revoked. |
| MF_E_TRUST_DISABLED | 0xC00D7152 | Trusted functionality is currently disabled on this component. |
| MF_E_WMDRMOTA_NO_ACTION | 0xC00D7153 | No Action is set on WMDRM Output Trust Authority. |
| MF_E_WMDRMOTA_ACTION_ALREADY_SET | 0xC00D7154 | Action is already set on WMDRM Output Trust Authority. |
| MF_E_WMDRMOTA_DRM_HEADER_NOT_AVAILABLE | 0xC00D7155 | DRM Heaader is not available. |
| MF_E_WMDRMOTA_DRM_ENCRYPTION_SCHEME_NOT_SUPPORTED | 0xC00D7156 | Current encryption scheme is not supported. |
| MF_E_WMDRMOTA_ACTION_MISMATCH | 0xC00D7157 | Action does not match with current configuration. |
| MF_E_WMDRMOTA_INVALID_POLICY | 0xC00D7158 | Invalid policy for WMDRM Output Trust Authority. |
| MF_E_POLICY_UNSUPPORTED | 0xC00D7159 | The policies that the Input Trust Authority requires to be enforced are unsupported by the outputs. |
| MF_E_OPL_NOT_SUPPORTED | 0xC00D715A | The OPL that the license requires to be enforced are not supported by the Input Trust Authority. |
| MF_E_TOPOLOGY_VERIFICATION_FAILED | 0xC00D715B | The topology could not be successfully verified. |
| MF_E_SIGNATURE_VERIFICATION_FAILED | 0xC00D715C | Signature verification could not be completed successfully for this component. |
| MF_E_DEBUGGING_NOT_ALLOWED | 0xC00D715D | Running this process under a debugger while using protected content is not allowed. |
| MF_E_CODE_EXPIRED | 0xC00D715E | MF component has expired. |
| MF_E_GRL_VERSION_TOO_LOW | 0xC00D715F | The current GRL on the machine does not meet the minimum version requirements. |
| MF_E_GRL_RENEWAL_NOT_FOUND | 0xC00D7160 | The current GRL on the machine does not contain any renewal entries for the specified revocation. |
| MF_E_GRL_EXTENSIBLE_ENTRY_NOT_FOUND | 0xC00D7161 | The current GRL on the machine does not contain any extensible entries for the specified extension GUID. |
| MF_E_KERNEL_UNTRUSTED | 0xC00D7162 | The kernel isn't secure for high security level content. |
| MF_E_PEAUTH_UNTRUSTED | 0xC00D7163 | The response from protected environment driver isn't valid. |
| MF_E_NON_PE_PROCESS | 0xC00D7165 | A non-PE process tried to talk to PEAuth. |
| MF_E_REBOOT_REQUIRED | 0xC00D7167 | We need to reboot the machine. |
| MF_S_WAIT_FOR_POLICY_SET | 0x000D7168 | Protection for this stream is not guaranteed to be enforced until the MEPolicySet event is fired. |
| MF_S_VIDEO_DISABLED_WITH_UNKNOWN_SOFTWARE_OUTPUT | 0x000D7169 | This video stream is disabled because it is being sent to an unknown software output. |
| MF_E_GRL_INVALID_FORMAT | 0xC00D716A | The GRL file is not correctly formed, it may have been corrupted or overwritten. |
| MF_E_GRL_UNRECOGNIZED_FORMAT | 0xC00D716B | The GRL file is in a format newer than those recognized by this GRL Reader. |
| MF_E_ALL_PROCESS_RESTART_REQUIRED | 0xC00D716C | The GRL was reloaded and required all processes that can run protected media to restart. |
| MF_E_PROCESS_RESTART_REQUIRED | 0xC00D716D | The GRL was reloaded and the current process needs to restart. |
| MF_E_USERMODE_UNTRUSTED | 0xC00D716E | The user space is untrusted for protected content play. |
| MF_E_PEAUTH_SESSION_NOT_STARTED | 0xC00D716F | PEAuth communication session hasn't been started. |
| MF_E_PEAUTH_PUBLICKEY_REVOKED | 0xC00D7171 | PEAuth's public key is revoked. |
| MF_E_GRL_ABSENT | 0xC00D7172 | The GRL is absent. |
| MF_S_PE_TRUSTED | 0x000D7173 | The Protected Environment is trusted. |
| MF_E_PE_UNTRUSTED | 0xC00D7174 | The Protected Environment is untrusted. |
| MF_E_PEAUTH_NOT_STARTED | 0xC00D7175 | The Protected Environment Authorization service (PEAUTH) has not been started. |
| MF_E_INCOMPATIBLE_SAMPLE_PROTECTION | 0xC00D7176 | The sample protection algorithms supported by components are not compatible. |
| MF_E_PE_SESSIONS_MAXED | 0xC00D7177 | No more protected environment sessions can be supported. |
| MF_E_HIGH_SECURITY_LEVEL_CONTENT_NOT_ALLOWED | 0xC00D7178 | WMDRM ITA does not allow protected content with high security level for this release. |
| MF_E_TEST_SIGNED_COMPONENTS_NOT_ALLOWED | 0xC00D7179 | WMDRM ITA cannot allow the requested action for the content as one or more components is not properly signed. |
| MF_E_ITA_UNSUPPORTED_ACTION | 0xC00D717A | WMDRM ITA does not support the requested action. |
| MF_E_ITA_ERROR_PARSING_SAP_PARAMETERS | 0xC00D717B | WMDRM ITA encountered an error in parsing the Secure Audio Path parameters. |
| MF_E_POLICY_MGR_ACTION_OUTOFBOUNDS | 0xC00D717C | The Policy Manager action passed in is invalid. |
| MF_E_BAD_OPL_STRUCTURE_FORMAT | 0xC00D717D | The structure specifying Output Protection Level is not the correct format. |
| MF_E_ITA_UNRECOGNIZED_ANALOG_VIDEO_PROTECTION_GUID | 0xC00D717E | WMDRM ITA does not recognize the Explicite Analog Video Output Protection guid specified in the license. |
| MF_E_NO_PMP_HOST | 0xC00D717F | IMFPMPHost object not available. |
| MF_E_ITA_OPL_DATA_NOT_INITIALIZED | 0xC00D7180 | WMDRM ITA could not initialize the Output Protection Level data. |
| MF_E_ITA_UNRECOGNIZED_ANALOG_VIDEO_OUTPUT | 0xC00D7181 | WMDRM ITA does not recognize the Analog Video Output specified by the OTA. |
| MF_E_ITA_UNRECOGNIZED_DIGITAL_VIDEO_OUTPUT | 0xC00D7182 | WMDRM ITA does not recognize the Digital Video Output specified by the OTA. |

| Return Code | Value | Description |
|---|---|---|
| MF_E_CLOCK_INVALID_CONTINUITY_KEY | 0xC00D9C40 | The continuity key supplied is not currently valid. |
| MF_E_CLOCK_NO_TIME_SOURCE | 0xC00D9C41 | No Presentation Time Source has been specified. |
| MF_E_CLOCK_STATE_ALREADY_SET | 0xC00D9C42 | The clock is already in the requested state. |
| MF_E_CLOCK_NOT_SIMPLE | 0xC00D9C43 | The clock has too many advanced features to execute the request. |
| MF_S_CLOCK_STOPPED | 0x000D9C44 | Timer::SetTimer returns this success code if called happened while timer is stopped. Timer is not going to be dispatched until clock is running |

| Return Code | Value | Description |
|---|---|---|
| MF_E_NO_MORE_DROP_MODES | 0xC00DA028 | The component does not support any more drop modes. |
| MF_E_NO_MORE_QUALITY_LEVELS | 0xC00DA029 | The component does not support any more quality levels. |
| MF_E_DROPTIME_NOT_SUPPORTED | 0xC00DA02A | The component does not support drop time functionality. |
| MF_E_QUALITYKNOB_WAIT_LONGER | 0xC00DA02B | Quality Manager needs to wait longer before bumping the Quality Level up. |
| MF_E_QM_INVALIDSTATE | 0xC00DA02C | Quality Manager is in an invalid state. Quality Management is off at this moment. |

| Return Code | Value | Description |
|---|---|---|
| MF_E_TRANSCODE_NO_CONTAINERTYPE | 0xC00DA410 | No transcode output container type is specified. |
| MF_E_TRANSCODE_PROFILE_NO_MATCHING_STREAMS | 0xC00DA411 | The profile does not have a media type configuration for any selected source streams. |
| MF_E_TRANSCODE_NO_MATCHING_ENCODER | 0xC00DA412 | Cannot find an encoder MFT that accepts the user preferred output type. |

| Return Code | Value | Description |
|---|---|---|
| MF_E_ALLOCATOR_NOT_INITIALIZED | 0xC00DA7F8 | Memory allocator is not initialized. |
| MF_E_ALLOCATOR_NOT_COMMITED | 0xC00DA7F9 | Memory allocator is not committed yet. |
| MF_E_ALLOCATOR_ALREADY_COMMITED | 0xC00DA7FA | Memory allocator has already been committed. |
| MF_E_STREAM_ERROR | 0xC00DA7FB | An error occurred in media stream. |
| MF_E_INVALID_STREAM_STATE | 0xC00DA7FC | Stream is not in a state to handle the request. |
| MF_E_HW_STREAM_NOT_CONNECTED | 0xC00DA7FD | Hardware stream is not connected yet. |

| Version 15© Vector Informatik GmbH |
|---|
