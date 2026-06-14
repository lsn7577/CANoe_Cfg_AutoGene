# AvbGetAafSampleRate

> Category: `Obsolete` | Type: `notes`

| Deprecated Function Use AvbGetMediaType and query property AudioSamplesPerSecond using MediaGetProperty. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Function Syntax | dword AvbGetAafSampleRate(dword listenerOrTalkerHandle, dword& retSampleRate); |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Function | The function retrieves the sample rate of the AAF stream received by the Listener or originated by the Talker. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Parameters | listenerOrTalkerHandle The handle of the Listener or Talker. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| retSampleRate The sample rate of the AAF stream upon successful return of the function. The following values are supported: Value Description 1 8 kHz 2 16 kHz 3 32 kHz 4 44.1 kHz 5 48 kHz 6 88.2 kHz 7 96 kHz 8 176.4 kHz 9 192 kHz | Value | Description | 1 | 8 kHz | 2 | 16 kHz | 3 | 32 kHz | 4 | 44.1 kHz | 5 | 48 kHz | 6 | 88.2 kHz | 7 | 96 kHz | 8 | 176.4 kHz | 9 | 192 kHz |
| Value | Description |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 1 | 8 kHz |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 2 | 16 kHz |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 3 | 32 kHz |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 4 | 44.1 kHz |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 5 | 48 kHz |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 6 | 88.2 kHz |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 7 | 96 kHz |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 8 | 176.4 kHz |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 9 | 192 kHz |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Return Values | 0: The function completed successfully. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| >0: Error code |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 8.2 SP2-9.0 SP5 | Ethernet | — | • |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Example — |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
