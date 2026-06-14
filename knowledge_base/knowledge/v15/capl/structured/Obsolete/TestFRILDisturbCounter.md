# TestFRILDisturbCounter

> Category: `Obsolete` | Type: `notes`

## Description

aSigGroupName

Some systems assign a counter to signal group. With this variant you can apply the disturbance to a dedicated signal group within a PDU.

-1: General error.

OEM Package based Fault Injection Functions

| Deprecated Function This function is deprecated and has been replaced by ILNodeDisturbCounter |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Note This function is not available for all OEM packages - depends on the CANoeIL. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Function Syntax | long TestFRILDisturbCounter(char aPduName[], long counterType, long disturbanceMode, long disturbanceCount, long disturbanceValue, long continueMode); |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| long TestFRILDisturbCounter(char pduName[], char aSigGroupName[], long counterType, long disturbanceMode, long disturbanceCount, long disturbanceValue, long continueMode); |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Function | This function modifies the counter. Different fault injections are possible. This function influences a simulation node with an assigned CANoe Interaction Layer. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Parameters | aPDUName Name of the node that should be modified. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| aSigGroupName Some systems assign a counter to signal group. With this variant you can apply the disturbance to a dedicated signal group within a PDU. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| counterType The possible values are described in the corresponding OEM Package manual. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| disturbanceMode Identifies the disturbance mode: 0 Value The disturbance uses the value in disturbanceValue as Counter. 1 Freeze The current counter value is transmitted. 2 Random A random value is transmitted as counter. 3 Offset The counter is incremented with the value in disturbanceValue. | 0 | Value | The disturbance uses the value in disturbanceValue as Counter. | 1 | Freeze | The current counter value is transmitted. | 2 | Random | A random value is transmitted as counter. | 3 | Offset | The counter is incremented with the value in disturbanceValue. |  |  |  |  |  |  |  |  |
| 0 | Value | The disturbance uses the value in disturbanceValue as Counter. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 1 | Freeze | The current counter value is transmitted. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 2 | Random | A random value is transmitted as counter. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 3 | Offset | The counter is incremented with the value in disturbanceValue. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| disturbanceCount -1 Infinite 0 Stops the disturbance, e.g.a infinite disturbance n Number of disturbances | -1 | Infinite | 0 | Stops the disturbance, e.g.a infinite disturbance | n | Number of disturbances |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| -1 | Infinite |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 0 | Stops the disturbance, e.g.a infinite disturbance |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| n | Number of disturbances |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| disturbanceValue This value is used in combination with the disturbanceMode. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| continueMode Defines the behavior of the counter after the disturbances are finished. 0 CorrectCounter The counter will be incremented with counter value + number of disturbances. 1 LastValidCounter The counters next value bases on the last value before the disturbance has started. 2 LastValue The counter incremets the last counter value (last disturbance value). | 0 | CorrectCounter | The counter will be incremented with counter value + number of disturbances. | 1 | LastValidCounter | The counters next value bases on the last value before the disturbance has started. | 2 | LastValue | The counter incremets the last counter value (last disturbance value). |  |  |  |  |  |  |  |  |  |  |  |
| 0 | CorrectCounter | The counter will be incremented with counter value + number of disturbances. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 1 | LastValidCounter | The counters next value bases on the last value before the disturbance has started. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 2 | LastValue | The counter incremets the last counter value (last disturbance value). |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Return Values | 0: No error. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| -1: General error. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 7.6 SP3 - 8.2 SP3 | FlexRay Test nodes | — | • |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Example 1 Continue Mode: disturbanceMode=Value, disturbanceValue=8, disturbanceCount=2 Regular continueMode:CorrectCounter continueMode:LastValidCounter continueMode:LastValue Counter = 1 Counter = 1 Counter = 1 Counter = 1 Counter = 2 Counter = 8 Counter = 8 Counter = 8 Counter = 3 Counter = 8 Counter = 8 Counter = 8 Counter = 4 Counter = 4 Counter = 2 Counter = 9 | Regular | continueMode:CorrectCounter | continueMode:LastValidCounter | continueMode:LastValue | Counter = 1 | Counter = 1 | Counter = 1 | Counter = 1 | Counter = 2 | Counter = 8 | Counter = 8 | Counter = 8 | Counter = 3 | Counter = 8 | Counter = 8 | Counter = 8 | Counter = 4 | Counter = 4 | Counter = 2 | Counter = 9 |
| Regular | continueMode:CorrectCounter | continueMode:LastValidCounter | continueMode:LastValue |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Counter = 1 | Counter = 1 | Counter = 1 | Counter = 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Counter = 2 | Counter = 8 | Counter = 8 | Counter = 8 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Counter = 3 | Counter = 8 | Counter = 8 | Counter = 8 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Counter = 4 | Counter = 4 | Counter = 2 | Counter = 9 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Example 2 Disturbance Mode: disturbanceCount=2, continueMode=CorrectCounter, disturbanceMode=Value, disturbanceValue=8 Regular disturbanceMode:Value (8) disturbanceMode:Freeze disturbanceMode:Offset Counter = 1 Counter = 1 Counter = 1 Counter = 1 Counter = 2 Counter = 8 Counter = 1 Counter = 9 Counter = 3 Counter = 8 Counter = 1 Counter = 1 Counter = 4 Counter = 4 Counter = 4 Counter = 4 | Regular | disturbanceMode:Value (8) | disturbanceMode:Freeze | disturbanceMode:Offset | Counter = 1 | Counter = 1 | Counter = 1 | Counter = 1 | Counter = 2 | Counter = 8 | Counter = 1 | Counter = 9 | Counter = 3 | Counter = 8 | Counter = 1 | Counter = 1 | Counter = 4 | Counter = 4 | Counter = 4 | Counter = 4 |
| Regular | disturbanceMode:Value (8) | disturbanceMode:Freeze | disturbanceMode:Offset |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Counter = 1 | Counter = 1 | Counter = 1 | Counter = 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Counter = 2 | Counter = 8 | Counter = 1 | Counter = 9 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Counter = 3 | Counter = 8 | Counter = 1 | Counter = 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Counter = 4 | Counter = 4 | Counter = 4 | Counter = 4 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
