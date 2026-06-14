# AvbSetCrfType

> Category: `Obsolete` | Type: `notes`

| Deprecated Function Set property TimestampRate on the media type (retrievable via AvbGetMediaType) and call AvbSetMediaType. |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | dword AvbSetCrfType(dword talkerHandle, dword type); |  |  |  |
| Function | The function sets the type of time stamp contained in the CRF stream originated by the Talker. |  |  |  |
| Parameters | talkerHandle The handle of the Talker. |  |  |  |
| type The type of timestamp of the CRF to set. The supported values see AvbGetCrfType. |  |  |  |  |
| Return Values | 0: The function completed successfully. |  |  |  |
| >0: Error code |  |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 8.2 SP2-9.0 SP5 | Ethernet | — | • |  |
| Example — |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
