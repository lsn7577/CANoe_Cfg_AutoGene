# AvbGetAafFormat

> Category: `Obsolete` | Type: `notes`

| Deprecated Function Use AvbGetMediaType and query property AudioBitsPerSample using MediaGetProperty. |  |  |  |  |  |  |
|---|---|---|---|---|---|---|
| Function Syntax | dword AvbGetAafFormat(dword listenerOrTalkerHandle, dword& retFormat); |  |  |  |  |  |
| Function | The function retrieves the format of the AAF samples in the stream received by the Listener or originated by the Talker. |  |  |  |  |  |
| Parameters | listenerOrTalkerHandle The handle of the Listener or Talker. |  |  |  |  |  |
| retFormat The sample format of the AAF stream upon successful return of the function. The following formats are supported: Value Description 2 32 bit integer 4 16 bit integer | Value | Description | 2 | 32 bit integer | 4 | 16 bit integer |
| Value | Description |  |  |  |  |  |
| 2 | 32 bit integer |  |  |  |  |  |
| 4 | 16 bit integer |  |  |  |  |  |
| Return Values | 0: The function completed successfully. |  |  |  |  |  |
| >0: Error code |  |  |  |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |  |  |
| 8.2 SP2-9.0 SP5 | Ethernet | — | • |  |  |  |
| Example — |  |  |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
