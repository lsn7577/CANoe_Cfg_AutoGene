# linSlFSMSetStTO

> Category: `Obsolete` | Type: `notes`

| Deprecated Function No replacement. |  |  |  |  |
|---|---|---|---|---|
| Note This function may only be called in the event procedure on preStart. |  |  |  |  |
| Function Syntax | void linSlFSMSetStTO (unsigned int slaveId, unsigned int stateId, unsigned int timeout, unsigned int followUpState); |  |  |  |
| Function | Sets a timeout for the state specified by stateId of the Slave with the identifier slaveId. |  |  |  |
| Parameters | slaveId Identifier of the relevant Slave. Corresponds to the slaveId, that was defined with linSlSimulate. |  |  |  |
| stateId Identifier of the relevant state of the Finite State Machine (FSM). Lies in the range that was defined by linSlFSMSetGlobal. |  |  |  |  |
| timeout Timeout in milliseconds after which the state should automatically be ended. |  |  |  |  |
| followUpState State that should be assumed if the current state is ended with a timeout.After a timeout has occurred the hardware sends a Slave Timeout message and switches the Slave to the followUpState state. |  |  |  |  |
| Return Values | — |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 3.1 - 5.1 | LIN | — | • |  |
| Example — |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
