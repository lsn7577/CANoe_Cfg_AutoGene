# TestILDisturbSignalUpdateBit, TestILDisturbSignalGroupUpdateBit

> Category: `Obsolete` | Type: `notes`

| Deprecated Function This function is deprecated and has been replaced by ILNodeDisturbSignalUpdateBit |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Note This function is not available for all OEM packages - depends on the CANoeIL. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Function Syntax | long TestILDisturbSignalUpdateBit (dbSignal aSig, long disturbanceMode, long disturbanceCount, long disturbanceValue); |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| long TestILDisturbSignalGroupUpdateBit (dbMsg dbMessage, char signalGroupName[],long disturbanceMode, long disturbanceCount, long disturbanceValue); |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Function | Modifies the update bit of a signal/signal group. Different fault injections are possible. The function influences a simulation node with an assigned CANoe Interaction Layer. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Parameters | aSig The symbolic name of an update bit signal in the database. The update bit’s signal names have the same name as the signal or the signal group they control followed by the suffix “_UB”. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| dbMessage The symbolic name of a message in the database. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| signalGroupName The symbolic full name of the signal group. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| disturbanceMode Defines the function for the disturbance. 0 Value Sets the update bit fix to the value of parameter disturbanceValue. 1 Freeze Current signal value is used (disturbanceValue is not used). 2 Random Random value is used for setting and resetting the update bit (disturbanceValue is not used). 3 Opposite Signal value is set when update bit should be cleared and is cleared when update bit should be set. 4 Random Set The update bit will randomly be not set but will always after transmission be cleared (disturbanceValue is not used). 5 Random Reset The update bit will always correctly be set but randomly not reset (disturbanceValue is not used). | 0 | Value | Sets the update bit fix to the value of parameter disturbanceValue. | 1 | Freeze | Current signal value is used (disturbanceValue is not used). | 2 | Random | Random value is used for setting and resetting the update bit (disturbanceValue is not used). | 3 | Opposite | Signal value is set when update bit should be cleared and is cleared when update bit should be set. | 4 | Random Set | The update bit will randomly be not set but will always after transmission be cleared (disturbanceValue is not used). | 5 | Random Reset | The update bit will always correctly be set but randomly not reset (disturbanceValue is not used). |
| 0 | Value | Sets the update bit fix to the value of parameter disturbanceValue. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 1 | Freeze | Current signal value is used (disturbanceValue is not used). |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 2 | Random | Random value is used for setting and resetting the update bit (disturbanceValue is not used). |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 3 | Opposite | Signal value is set when update bit should be cleared and is cleared when update bit should be set. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 4 | Random Set | The update bit will randomly be not set but will always after transmission be cleared (disturbanceValue is not used). |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 5 | Random Reset | The update bit will always correctly be set but randomly not reset (disturbanceValue is not used). |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| disturbanceCount The number of disturbances. -1 Infinite 0 Stops the disturbance, e.g.a infinite disturbance. n Number of disturbances. | -1 | Infinite | 0 | Stops the disturbance, e.g.a infinite disturbance. | n | Number of disturbances. |  |  |  |  |  |  |  |  |  |  |  |  |
| -1 | Infinite |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 0 | Stops the disturbance, e.g.a infinite disturbance. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| n | Number of disturbances. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| disturbanceValue This value is used in combination with the disturbanceMode. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Return Values | 0: No error |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| -1: General error |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 7.6 SP4 - 8.2 SP3 | CAN Test nodes | — | • |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Example — |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
