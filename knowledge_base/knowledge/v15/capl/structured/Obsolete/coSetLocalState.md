# coSetLocalState

> Category: `Obsolete` | Type: `notes`

## Description

See Also

| Deprecated Function Replaced by CANopen Basic Functions. |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | void coSetLocalState( dword newState, dword errCode[] ); |  |  |  |
| Function | The function sets the communication state of the node. The node must previously have been started with coStartUp. The node layer controls the local communication state independently. Also a (configured) automatic transfer into the state Operational (Bit 2 in 1F80 not set) is caused by the node layer. Should it nevertheless be necessary to intervene directly in the local state machine, this can occur via this function. Note After a successful call of this function, the new state is not yet assumed in each case since the processing of this command occurs asynchronously. The state change is signaled by the event function coOnNodeChangedState. | Note After a successful call of this function, the new state is not yet assumed in each case since the processing of this command occurs asynchronously. The state change is signaled by the event function coOnNodeChangedState. |  |  |
| Note After a successful call of this function, the new state is not yet assumed in each case since the processing of this command occurs asynchronously. The state change is signaled by the event function coOnNodeChangedState. |  |  |  |  |
| Parameters | newState Desired state of the node:4 - stopped5 - operational6 - reset node7 - reset communication127 - pre-operational |  |  |  |
| errCode Error code buffer (is entered in index 0 of the field) |  |  |  |  |
| Return Values | — |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 6.0-9.0 SP6 | CANopen | — | • |  |
| Example dword errCode[1];coSetLocalState( 5, errCode );if (errCode[0] == 0) { write( "Local state change successfully commanded" );} |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
