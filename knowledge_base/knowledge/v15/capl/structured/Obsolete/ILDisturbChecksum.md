# ILDisturbChecksum

> Category: `Obsolete` | Type: `notes`

## Description

-1: General error

| Deprecated Function This function is deprecated and has been replaced by ILNodeDisturbChecksum |  |  |  |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Note This function is not available for all OEM packages — depends on the CANoeIL. This function can be used in a global node outside the node context of the IL. |  |  |  |  |  |  |  |  |  |  |  |  |
| Function Syntax | long ILDisturbChecksum(char aMsgName[], long checksumType, long disturbanceMode, long disturbanceCount, long disturbanceValue); // form 1 |  |  |  |  |  |  |  |  |  |  |  |
| long ILDisturbChecksum(char aMsgName[], char sigGroupName[], long checksumType, long disturbanceMode, long disturbanceCount, long disturbanceValue); // form 2 |  |  |  |  |  |  |  |  |  |  |  |  |
| Function | This function modifies the checksum. Different fault injections are possible.This function influences a simulation node with an assigned CANoe interaction layer. |  |  |  |  |  |  |  |  |  |  |  |
| Parameters | aMsgName Name of the message or PDU that should be modified. |  |  |  |  |  |  |  |  |  |  |  |
| aSigGroupName Some systems assign a checksum to a signal group. With this variant you can apply the disturbance to a dedicated signal group within a PDU. |  |  |  |  |  |  |  |  |  |  |  |  |
| checksumType The possible values are described in the corresponding OEM Package manual. |  |  |  |  |  |  |  |  |  |  |  |  |
| disturbanceMode Identifies the disturbance mode: 0 Value The disturbance uses the value in disturbanceValue as counter. 1 Freeze The current checksum value is transmitted. 2 Random A random value is transmitted as checksum . 3 Offset The checksum is incremented with the value in disturbanceValue. | 0 | Value | The disturbance uses the value in disturbanceValue as counter. | 1 | Freeze | The current checksum value is transmitted. | 2 | Random | A random value is transmitted as checksum . | 3 | Offset | The checksum is incremented with the value in disturbanceValue. |
| 0 | Value | The disturbance uses the value in disturbanceValue as counter. |  |  |  |  |  |  |  |  |  |  |
| 1 | Freeze | The current checksum value is transmitted. |  |  |  |  |  |  |  |  |  |  |
| 2 | Random | A random value is transmitted as checksum . |  |  |  |  |  |  |  |  |  |  |
| 3 | Offset | The checksum is incremented with the value in disturbanceValue. |  |  |  |  |  |  |  |  |  |  |
| disturbanceCount -1 Infinite. 0 Stops the disturbance, e.g.a infinite disturbance. n Number of disturbances. | -1 | Infinite. | 0 | Stops the disturbance, e.g.a infinite disturbance. | n | Number of disturbances. |  |  |  |  |  |  |
| -1 | Infinite. |  |  |  |  |  |  |  |  |  |  |  |
| 0 | Stops the disturbance, e.g.a infinite disturbance. |  |  |  |  |  |  |  |  |  |  |  |
| n | Number of disturbances. |  |  |  |  |  |  |  |  |  |  |  |
| disturbanceValue This value is used in combination with the disturbanceMode. |  |  |  |  |  |  |  |  |  |  |  |  |
| Return Values | 0: No error |  |  |  |  |  |  |  |  |  |  |  |
| -1: General error |  |  |  |  |  |  |  |  |  |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |  |  |  |  |  |  |  |  |
| 8.0 - 8.2 SP3 | CAN FlexRay Simulation nodes | — | • |  |  |  |  |  |  |  |  |  |
| Example // Disturbs the Checksum of a specific PDU, disturbance pattern: 20x fix valuevariables { long checksumType = 0; // The possible values are described in the corresponding // OEM Package manual. long disturbanceMode = 0; // The disturbance uses the value in disturbanceValue // as Counter. long disturbanceCount = 20; long disturbanceValue = 10;}on key 'a'{ ILDisturbChecksum("PDU_A", checksumType, disturbanceMode, disturbanceCount, disturbanceValue);} |  |  |  |  |  |  |  |  |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
