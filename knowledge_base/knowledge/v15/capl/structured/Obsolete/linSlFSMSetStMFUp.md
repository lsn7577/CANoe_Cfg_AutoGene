# linSlFSMSetStMFUp

> Category: `Obsolete` | Type: `notes`

| Deprecated Function No replacement. |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | unsigned long linSlFSMSetStMFUp (unsigned int slaveId, unsigned int stateId, unsigned int uniqueKey, unsigned int patternRequestId, unsigned long dlc, unsigned char maskBytes[], unsigned char patternBytes[], unsigned int followUpState); |  |  |  |
| Function | Sets up a comparison operation for the state stateId of the Slave slaveId. If no DLC has been set by the data base, the DLC will be set by the dlc parameter of the function. If the DLC already has been set by the data base, this value must be handover correctly on every call of this function. DLC value range: 0 ... 8 (bytes) The functionality to set the DLC is only available with LIN specification 1.2 (or above)! LIN specification 1.1 presets the DLC of an identifier. |  |  |  |
| Parameters | slaveId Identifier of the relevant Slave. Corresponds to the slaveId, that was defined with linSlSimulate. |  |  |  |
| stateId Identifier of the relevant state of the Finite State Machine (FSM). Lies in the range defined by linSlFSMSetGlobal. |  |  |  |  |
| uniqueKey Dummy differentiation code for multiple comparison operations with the same slaveId/stateId pair (see below) |  |  |  |  |
| patternRequestId If this transmit identifier was placed on the bus by the Master, the condition described here is evaluated. |  |  |  |  |
| dlc DLC of the message |  |  |  |  |
| maskBytes Mask with which the bytes/bits of interest can be filtered out. |  |  |  |  |
| patternBytes Pattern with which the comparison is made after masking. |  |  |  |  |
| followUpState State to be switched to after successful comparison |  |  |  |  |
| Return Values | Nonzero if the comparison operator was configured; else 0. The contents of messages with the identifier pattern RequestId that are sent on the LIN bus are linked bitwise with maskBytes by an AND operation. If the result of this comparison is identical to patternBytes, the Slave transitions to the state followUpState. Since multiple comparisons may be configured for the same message identifier for a given Slave state, a code uniqueKey is also necessary to permit identification of the various comparison operations. This code must be unique within the Slave state. If there are multiple comparison operations for a message identifier within a state of a Slave, they are processed in the order of their specification until all comparisons have been performed or a comparison was successful. During a measurement this function can be used to change the following data of a comparison operation already configured in the on preStart event procedure: Comparison mask Results pattern Resulting state |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 3.1 - 5.1 | LIN | — | • |  |
| Example — |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
