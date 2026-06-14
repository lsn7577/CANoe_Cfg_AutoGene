# TestFRILDisturbPduUpdateBit

> Category: `Obsolete` | Type: `notes`

## Description

-1: General error.

OEM Package based Fault Injection Functions

| Deprecated Function This function is deprecated and has been replaced by ILNodeDisturbPduUpdateBit |  |  |  |  |  |  |
|---|---|---|---|---|---|---|
| Note This function is not available for all OEM packages - depends on the CANoeIL. |  |  |  |  |  |  |
| Function Syntax | long TestFRILDisturbPduUpdateBit(char aPduName[], int disturbanceCount, int updateBit); |  |  |  |  |  |
| Function | This function modifies the update bit of a PDU. Different fault injections are possible. This function influences a simulation node with an assigned CANoe Interaction Layer. |  |  |  |  |  |
| Parameters | aPDUName Name of the node that should be modified. |  |  |  |  |  |
| aSignalName Name of the signal using an update bit. |  |  |  |  |  |  |
| disturbanceCount -1 Infinite 0 Stops the disturbance, e.g.a infinite disturbance n Number of disturbances | -1 | Infinite | 0 | Stops the disturbance, e.g.a infinite disturbance | n | Number of disturbances |
| -1 | Infinite |  |  |  |  |  |
| 0 | Stops the disturbance, e.g.a infinite disturbance |  |  |  |  |  |
| n | Number of disturbances |  |  |  |  |  |
| updateBit Desired disturbance value (0,1). |  |  |  |  |  |  |
| Return Values | 0: No error. |  |  |  |  |  |
| -1: General error. |  |  |  |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |  |  |
| 7.6 SP3 - 8.2 SP3 | FlexRay Test nodes | — | • |  |  |  |
| Example // set the signal update bit of the signal “Signal_A” in PDU “PDU_A” for 100times to 1.TestFRILDisturbSignalUpdateBit(“PDU_A”, Signal_A , 0, 100, 1); |  |  |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
