# RegisterSignalDriverByTxNode

> Category: `Obsolete` | Type: `notes`

| Deprecated Function No replacement. |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | long RegisterSignalDriver (dbSignal aSignal , dbNode aTxNode, char aCallbackFunction[]) |  |  |  |
| Function | Registers the given callback as a 'signal driver' for the signal. |  |  |  |
| Parameters | aSignal DB signal to be queried. |  |  |  |
| aTxNode DB node that should send the signal. It is only necessary if several send nodes are approved for a message. |  |  |  |  |
| aCallbackFunction Name of a callback function that should be defined as follows: void function(double value). |  |  |  |  |
| Return Values | 1: Correct functionality |  |  |  |
| 0: CAPL 'signal driver' could not be registered |  |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 7.0 | — | — | • |  |
| Example — |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
