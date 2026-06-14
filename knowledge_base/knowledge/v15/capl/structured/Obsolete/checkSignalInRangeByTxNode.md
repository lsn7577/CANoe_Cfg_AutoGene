# checkSignalInRangeByTxNode

> Category: `Obsolete` | Type: `notes`

| Deprecated Function This function replaces the function checkSignalInRangeGM. Version 7.1: Replaced by checkSignalInRange. |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | long checkSignalInRangeByTxNode (dbSignal aSignal, dbNode aTxNode, float aLowLimit, float aHighLimit); |  |  |  |
| Function | Checks the signal value against the condition: aLowLimit <= Value <= aHighLimit |  |  |  |
| Parameters | aSignal The signal to be polled |  |  |  |
| aTxNode Send node of the message whose signal should be polled |  |  |  |  |
| aLowLimit Lower limit of the signal value |  |  |  |  |
| aHighLimit Upper limit of the signal value |  |  |  |  |
| Return Values | 1: If the condition is TRUE |  |  |  |
| 0: If the condition is violated or the signal is unavailable, i.e. was not on the bus yet |  |  |  |  |
| Availability | Since Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 5.1 | — | — | • |  |
| Example — |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
