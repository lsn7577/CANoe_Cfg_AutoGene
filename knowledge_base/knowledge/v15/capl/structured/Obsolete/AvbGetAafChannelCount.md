# AvbGetAafChannelCount

> Category: `Obsolete` | Type: `notes`

| Deprecated Function Use AvbGetMediaType and query property AudioNumChannels using MediaGetProperty. |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | dword AvbGetAafChannelCount(dword listenerOrTalkerHandle, dword& retChannelCount); |  |  |  |
| Function | The function retrieves the number of channels contained in an AAF frame in the stream received by the Listener or originated by the Talker. |  |  |  |
| Parameters | listenerOrTalkerHandle The handle of the Listener or Talker. |  |  |  |
| retChannelCount The channel count of an AAF frame upon successful return of the function. Values range between 0 and 1023. |  |  |  |  |
| Return Values | 0: The function completed successfully. |  |  |  |
| >0: Error code |  |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 8.2 SP2-9.0 SP5 | Ethernet | — | • |  |
| Example — |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
