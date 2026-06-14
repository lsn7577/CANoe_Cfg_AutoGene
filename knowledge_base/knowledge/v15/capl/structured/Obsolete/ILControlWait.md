# ILControlWait

> Category: `Obsolete` | Type: `notes`

## Description

-1: General error.

| OEM Package based Fault Injection Functions |

| Deprecated Function This function is deprecated and has been replaced by ILNodeControlWait |  |  |  |  |
|---|---|---|---|---|
| Note This function is not available for all OEM packages — depends on the CANoeIL. This function can be used in a global node outside the node context of the IL. |  |  |  |  |
| Function Syntax | long ILControlWait(char aNodeName[]) |  |  |  |
| Function | Stops the interaction layer of the selected simulation node.This function influences a simulation node with an assigned CANoe interaction layer. |  |  |  |
| Parameters | aNodeName Name of the node that should stop the interaction layer. |  |  |  |
| Return Values | 0: No error. |  |  |  |
| -1: General error. |  |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 8.0 - 8.2 SP2 | FlexRay Simulation nodes | — | • |  |
| Example // stops the interaction layer of ECU A for 2000ms.variables { msTimer WaitTimer;}On Key 'x' { ILControlWait ("ECU_A"); SetTimer(WaitTimer,2000);}On Timer WaitTimer { ILControlResume ("ECU_A");} |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
