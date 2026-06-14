# AvbGetCrfAudioSampleTimestampInterval

> Category: `Obsolete` | Type: `notes`

| Deprecated Function Use AvbGetMediaType and query property TimestampInterval using MediaGetProperty. |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | dword AvbGetCrfAudioSampleTimestampInterval(dword listenerOrTalkerHandle, dword& retTimestampInterval); |  |  |  |
| Function | The function retrieves the interval between each Audio Sample Timestamp in the CRF stream received by the Listener or originated by the Talker. |  |  |  |
| Parameters | listenerOrTalkerHandle The handle of the Listener or Talker. |  |  |  |
| retTimestampInterval The number of audio samples between each Audio Sample Timestamp of the CRF stream upon successful return of the function. |  |  |  |  |
| Return Values | 0: The function completed successfully. |  |  |  |
| >0: Error code |  |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 8.2 SP2-9.0 SP5 | Ethernet | — | • |  |
| Example — |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
