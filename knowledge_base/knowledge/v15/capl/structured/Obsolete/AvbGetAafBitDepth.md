# AvbGetAafBitDepth

> Category: `Obsolete` | Type: `notes`

| Deprecated Function Use AvbGetMediaType and query property AudioValidBitsPerSample using MediaGetProperty. |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | dword AvbGetAafBitDepth(dword listenerOrTalkerHandle, dword& retBitDepth); |  |  |  |
| Function | The function retrieves the bit depth of an AAF sample in the stream received by the Listener or originated by the Talker. |  |  |  |
| Parameters | listenerOrTalkerHandle The handle of the Listener or Talker. |  |  |  |
| retBitDepth The bit depth of an AAF sample upon successful return of the function. Valid values for the bit depth are: For the 32 bit sample format: [1; 32] For the 16 bit sample format: [1; 16] |  |  |  |  |
| Return Values | 0: The function completed successfully. |  |  |  |
| >0: Error code |  |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 8.2 SP2-9.0 SP5 | Ethernet | — | • |  |
| Example — |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
