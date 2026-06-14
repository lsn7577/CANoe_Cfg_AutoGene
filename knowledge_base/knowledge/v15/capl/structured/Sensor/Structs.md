# Structs

> Category: `Sensor` | Type: `notes`

| Member | Type | Short Description |
|---|---|---|
| FrameType | bitfield | Bit 0 indicates, if the frame shall be empty. Bit 1 indicates, if this frame marks the end of a cycle. |
| StartDelayUs | dword | Start time of the frame (relative to sync pulse end or cycle start). Max value = 8191. |
| CrcMode | SensorPsi5CrcMode | Mode of CRC/parity calculation used for this frame |
| StartBits | dword | Content of the start bits |
| StartBitsCount | dword | Number of start bits |
| MessagingBits | dword | Content of the messaging bits |
| MessagingBitsCount | dword | Number of messaging bits |
| FrameControlBits | dword | Content of the frame control bits |
| FrameControlBitsCount | dword | Number of status bits |
| StatusBits | dword | Content of the status bits |
| StatusBitsCount | dword | Number of status bits |
| DataRegionBBits | dword | Content of the bits in data region B |
| DataRegionBBitsCount | dword | Number of bits in data region B |
| DataRegionABits | dword | Content of the bits in data region A |
| DataRegionABitsCount | dword | Number of bits in data region A |
| CrcBits | dword | Content of the CRC / parity bits |
| CrcBitsCount | dword | Number of CRC / parity bits |

| Member | Type | Short Description |
|---|---|---|
| CrcMode | SensorSentCrcMode | Mode of CRC calculation used for this frame |
| StatusBits | dword | Content of the status region |
| DataBits | dword | Content of the data region |
| CrcBits | dword | Content of the CRC |

| Version 15© Vector Informatik GmbH |
|---|
