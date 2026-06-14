# ILDisturbSignalUpdateBit

> Category: `Obsolete` | Type: `notes`

## Description

CAN: long ILDisturbSignalUpdateBit(dbSignal aSignal, long disturbanceMode, long disturbanceCount, long disturbanceValue);

Identifies the disturbance mode:

This value is used in combination with the disturbanceMode.

-1: General error

| Deprecated Function This function is deprecated and has been replaced by ILNodeDisturbSignalUpdateBit |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|
| Note This function is not available for all OEM packages — depends on the CANoeIL. This function can be used in a global node outside the node context of the IL. |  |  |  |  |  |  |  |  |  |
| Function Syntax | FlexRay: long ILDisturbSignalUpdateBit(char aPduName[], char aSignalName[], long disturbanceMode, long disturbanceCount, long disturbanceValue); |  |  |  |  |  |  |  |  |
| CAN: long ILDisturbSignalUpdateBit(dbSignal aSignal, long disturbanceMode, long disturbanceCount, long disturbanceValue); |  |  |  |  |  |  |  |  |  |
| Function | This function modifies the update bit of a signal. Different fault injections are possible.This function influences a simulation node with an assigned CANoe interaction layer. |  |  |  |  |  |  |  |  |
| Parameters | aPDUName Name of the PDU that should be modified. |  |  |  |  |  |  |  |  |
| aSignalName Name of the signal using an update bit. |  |  |  |  |  |  |  |  |  |
| aSignal Update bit signal. |  |  |  |  |  |  |  |  |  |
| disturbanceMode Identifies the disturbance mode: 0 Value The disturbance uses the value in disturbanceValue as update bit. 1 Freeze The current update bit value is transmitted. 2 Random A random value is transmitted as update bit. | 0 | Value | The disturbance uses the value in disturbanceValue as update bit. | 1 | Freeze | The current update bit value is transmitted. | 2 | Random | A random value is transmitted as update bit. |
| 0 | Value | The disturbance uses the value in disturbanceValue as update bit. |  |  |  |  |  |  |  |
| 1 | Freeze | The current update bit value is transmitted. |  |  |  |  |  |  |  |
| 2 | Random | A random value is transmitted as update bit. |  |  |  |  |  |  |  |
| disturbanceCount -1 Infinite. 0 Stops the disturbance, e.g.a infinite disturbance. n Number of disturbances. | -1 | Infinite. | 0 | Stops the disturbance, e.g.a infinite disturbance. | n | Number of disturbances. |  |  |  |
| -1 | Infinite. |  |  |  |  |  |  |  |  |
| 0 | Stops the disturbance, e.g.a infinite disturbance. |  |  |  |  |  |  |  |  |
| n | Number of disturbances. |  |  |  |  |  |  |  |  |
| disturbanceValue This value is used in combination with the disturbanceMode. |  |  |  |  |  |  |  |  |  |
| Return Values | 0: No error |  |  |  |  |  |  |  |  |
| -1: General error |  |  |  |  |  |  |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |  |  |  |  |  |
| 8.0 - 8.2 SP3 | FlexRay Simulation nodes | — | • |  |  |  |  |  |  |
| 8.1 SP2 - 8.2 SP3 | CAN FlexRay Simulation nodes | — | • |  |  |  |  |  |  |
| Example // Sets the Signal Update Bit to 0variables { long disturbanceMode = 0; // The disturbance uses the value in disturbanceValue as Update Bit. int disturbanceCount = 100; long disturbanceValue = 0;}on key 'a'{ ILDisturbSignalUpdateBit("PDU_A", "Signal_A", disturbanceMode, disturbanceCount, disturbanceValue);} |  |  |  |  |  |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
