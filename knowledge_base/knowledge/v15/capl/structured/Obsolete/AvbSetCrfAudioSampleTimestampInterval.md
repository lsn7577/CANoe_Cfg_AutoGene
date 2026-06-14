# AvbSetCrfAudioSampleTimestampInterval

> Category: `Obsolete` | Type: `notes`

| Deprecated Function Set property TimestampInterval on the media type (retrievable via AvbGetMediaType) and call AvbSetMediaType. |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | dword AvbSetCrfAudioSampleTimestampInterval(dword talkerHandle, dword timestampInterval); |  |  |  |
| Function | The function sets the interval between each Audio Sample Timestamp in the CRF stream originated by the Talker. |  |  |  |
| Parameters | talkerHandle The handle of the Talker. |  |  |  |
| timestampInterval The number of audio samples between each Audio Sample Timestamp of the CRF stream to set. |  |  |  |  |
| Return Values | 0: The function completed successfully. |  |  |  |
| >0: Error code |  |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 8.2 SP2-9.0 SP5 | Ethernet | — | • |  |
| Example — |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
