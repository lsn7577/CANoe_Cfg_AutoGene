# AvbSetAafChannelCount

> Category: `Obsolete` | Type: `notes`

| Deprecated Function Set property AudioNumChannels on the Media Type (retrievable via AvbGetMediaType) and call AvbSetMediaType. |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | dword AvbSetAafChannelCount(dword talkerHandle, dword channelCount); |  |  |  |
| Function | The function sets the number of channels to be contained in an AAF frame in the stream originated by the Talker. |  |  |  |
| Parameters | talkerHandle The handle of the Talker. |  |  |  |
| channelCount The channel count of an AAF frame. For supported values see AvbGetAafChannelCount. |  |  |  |  |
| Return Values | 0: The function completed successfully. |  |  |  |
| >0: Error code |  |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 8.2 SP2-9.0 SP5 | Ethernet | — | • |  |
| Example — |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
