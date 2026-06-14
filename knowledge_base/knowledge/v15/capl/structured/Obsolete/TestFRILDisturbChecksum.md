# TestFRILDisturbChecksum

> Category: `Obsolete` | Type: `notes`

## Description

-1: General error.

OEM Package based Fault Injection Functions

| Deprecated Function This function is deprecated and has been replaced by ILNodeDisturbChecksum |  |  |  |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Note This function is not available for all OEM packages - depends on the CANoeIL. |  |  |  |  |  |  |  |  |  |  |  |  |
| Function Syntax | long TestFRILDisturbChecksum(char pduName[], long checksumType, long disturbanceMode, long disturbanceCount, long disturbanceValue); |  |  |  |  |  |  |  |  |  |  |  |
| long TestFRILDisturbChecksum(char pduName[], char sigGroupName[], long checksumType, long disturbanceMode, long disturbanceCount, long disturbanceValue); |  |  |  |  |  |  |  |  |  |  |  |  |
| Function | This function modifies the checksum. Different fault injections are possible. This function influences a simulation node with an assigned CANoe Interaction Layer. |  |  |  |  |  |  |  |  |  |  |  |
| Parameters | aPDUName Name of the node that should be modified. |  |  |  |  |  |  |  |  |  |  |  |
| aSigGroupName Some systems assign a counter to signal group. With this variant you can apply the disturbance to a dedicated signal group within a PDU. |  |  |  |  |  |  |  |  |  |  |  |  |
| checksumType The possible values are described in the corresponding OEM Package manual. |  |  |  |  |  |  |  |  |  |  |  |  |
| disturbanceMode Identifies the disturbance mode: 0 Value The disturbance uses the value in disturbanceValue as Counter. 1 Freeze The current counter value is transmitted. 2 Random A random value is transmitted as counter. 3 Offset The counter is incremented with the value in disturbanceValue. | 0 | Value | The disturbance uses the value in disturbanceValue as Counter. | 1 | Freeze | The current counter value is transmitted. | 2 | Random | A random value is transmitted as counter. | 3 | Offset | The counter is incremented with the value in disturbanceValue. |
| 0 | Value | The disturbance uses the value in disturbanceValue as Counter. |  |  |  |  |  |  |  |  |  |  |
| 1 | Freeze | The current counter value is transmitted. |  |  |  |  |  |  |  |  |  |  |
| 2 | Random | A random value is transmitted as counter. |  |  |  |  |  |  |  |  |  |  |
| 3 | Offset | The counter is incremented with the value in disturbanceValue. |  |  |  |  |  |  |  |  |  |  |
| disturbanceCount -1 Infinite 0 Stops the disturbance, e.g.a infinite disturbance n Number of disturbances | -1 | Infinite | 0 | Stops the disturbance, e.g.a infinite disturbance | n | Number of disturbances |  |  |  |  |  |  |
| -1 | Infinite |  |  |  |  |  |  |  |  |  |  |  |
| 0 | Stops the disturbance, e.g.a infinite disturbance |  |  |  |  |  |  |  |  |  |  |  |
| n | Number of disturbances |  |  |  |  |  |  |  |  |  |  |  |
| disturbanceValue This value is used in combination with the disturbanceMode. |  |  |  |  |  |  |  |  |  |  |  |  |
| Return Values | 0: No error. |  |  |  |  |  |  |  |  |  |  |  |
| -1: General error. |  |  |  |  |  |  |  |  |  |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |  |  |  |  |  |  |  |  |
| 7.6 SP3 - 8.2 SP3 | FlexRay Test nodes | — | • |  |  |  |  |  |  |  |  |  |
| Example — |  |  |  |  |  |  |  |  |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
