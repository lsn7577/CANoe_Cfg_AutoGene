# linSlFSMSetGlobal

> Category: `Obsolete` | Type: `notes`

| Deprecated Function No replacement. |  |  |  |  |
|---|---|---|---|---|
| Note This function may only be called in the event procedure on preStart. |  |  |  |  |
| Function Syntax | void linSlFSMSetGlobal(unsigned int slaveId, unsigned int numberOfStates); |  |  |  |
| Function | Sets the number of states given in numberOfStates for the Slave with identifier slaveId. This function must be called before the Slave's states are configured. |  |  |  |
| Parameters | slaveId Identifier of the relevant Slave. Corresponds to the slaveId, that was defined with linSlSimulate. |  |  |  |
| numberOfStates Number of states that the Finite State Machine (FSM) which implements the Slave should have. |  |  |  |  |
| Return Values | — |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 3.1 - 5.1 | LIN | — | • |  |
| Example — |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
