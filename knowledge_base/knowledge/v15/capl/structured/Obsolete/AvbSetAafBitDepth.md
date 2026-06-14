# AvbSetAafBitDepth

> Category: `Obsolete` | Type: `notes`

| Deprecated Function Set property AudioValidBitsPerSample on the Media Type (retrievable via AvbGetMediaType) and call AvbSetMediaType. |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | dword AvbSetAafBitDepth(dword talkerHandle, dword bitDepth); |  |  |  |
| Function | The function sets the bit depth of an AAF sample in the stream originated by the Talker. |  |  |  |
| Parameters | talkerHandle The handle of the Talker. |  |  |  |
| bitDepth The bit depth of an AAF sample. For supported values see AvbGetAafBitDepth. |  |  |  |  |
| Return Values | 0: The function completed successfully. |  |  |  |
| >0: Error code |  |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 8.2 SP2-9.0 SP5 | Ethernet | — | • |  |
| Example — |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
