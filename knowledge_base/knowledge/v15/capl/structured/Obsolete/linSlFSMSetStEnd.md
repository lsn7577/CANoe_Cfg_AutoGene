# linSlFSMSetStEnd

> Category: `Obsolete` | Type: `notes`

| Deprecated Function No replacement. |  |  |  |  |
|---|---|---|---|---|
| Note This function may only be called in the event procedure on preStart. |  |  |  |  |
| Function Syntax | void linSlFSMSetStEnd(unsigned int slaveId, unsigned int stateId); |  |  |  |
| Function | Ends the configuration of the state specified by stateId of the Slave with the identifier slaveId. The entire configuration of a state must appear within a linSlFSMSetStBegin / linSlFSMSetStEnd pair. |  |  |  |
| Parameters | slaveId Identifier of the relevant Slave. Corresponds to the slaveId, that was defined with linSlSimulate. |  |  |  |
| stateId Identifier of the relevant state of the Finite State Machine (FSM). Lies in the range that was defined by linSlFSMSetGlobal. |  |  |  |  |
| Return Values | — |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 3.1 - 5.1 | LIN | — | • |  |
| Example — |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
