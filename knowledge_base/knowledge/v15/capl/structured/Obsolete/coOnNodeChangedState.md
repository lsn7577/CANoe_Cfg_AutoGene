# coOnNodeChangedState

> Category: `Obsolete` | Type: `notes`

## Description

After the call of the function coStartUp the node needs some time in order to start and be initialized completely. Therefore, do not use any NMT commands before this event function was called with the value Pre-Operational!

Otherwise the completeness and consistency of the data cannot be guaranteed.

See Also

| Deprecated Function Replaced by CANopen Basic Functions. |  |  |  |  |
|---|---|---|---|---|
| Note After the call of the function coStartUp the node needs some time in order to start and be initialized completely. Therefore, do not use any NMT commands before this event function was called with the value Pre-Operational! Otherwise the completeness and consistency of the data cannot be guaranteed. |  |  |  |  |
| Function Syntax | void coOnNodeChangedState( dword newState ); |  |  |  |
| Function | This function is called if the state of the node changes. This can be triggered by the functions coSetLocalState, coStartUp, coShutDown or via the network. |  |  |  |
| Parameters | newState New state of the node:4 - stopped5 - operational6 - reset node7 - reset communication127 - pre-operational |  |  |  |
| Return Values | — |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 6.0-9.0 SP6 | CANopen | — | • |  |
| Example void coOnNodeChangedState( dword newState ){ write( "New state %d", newState );} |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
