# AvbSetAafFormat

> Category: `Obsolete` | Type: `notes`

| Deprecated Function Set property AudioBitsPerSample on the media type (retrievable via AvbGetMediaType) and call AvbSetMediaType. |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | dword AvbSetAafFormat(dword talkerHandle, dword format); |  |  |  |
| Function | The function sets the format of the AAF samples in the stream originated by the Talker. |  |  |  |
| Parameters | talkerHandle The handle of the Talker. |  |  |  |
| format The sample format of the AAF stream. For supported formats see AvbGetAafFormat. |  |  |  |  |
| Return Values | 0: The function completed successfully. |  |  |  |
| >0: Error code |  |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 8.2 SP2-9.0 SP5 | Ethernet | — | • |  |
| Example — |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
