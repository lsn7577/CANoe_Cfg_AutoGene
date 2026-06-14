# getSignalTimeByTxNode

> Category: `Obsolete` | Type: `notes`

| Deprecated Function This function replaces the function getSignalTimeGM. Version 7.1: Replaced by getSignalTime. |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | dword getSignalTimeByTxNode (dbSignal aSignal, dbNode aTxNode); |  |  |  |
| Function | Gets the time point relative to the measurement start at which the signal was last sent on the bus. |  |  |  |
| Parameters | aSignal The signal to be polled. |  |  |  |
| aTxNode Send node of the message whose signal should be polled. |  |  |  |  |
| Return Values | Time point or 0 if the signal was not sent yet. |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 7.0 | — | — | • |  |
| Example — |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
