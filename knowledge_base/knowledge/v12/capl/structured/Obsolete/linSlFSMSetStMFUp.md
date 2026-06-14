# linSlFSMSetStMFUp

> Category: `Obsolete` | Type: `function`

## Syntax

```c
unsigned long linSlFSMSetStMFUp (unsigned int slaveId, unsigned int stateId, unsigned int uniqueKey, unsigned int patternRequestId, unsigned long dlc, unsigned char maskBytes[], unsigned char patternBytes[], unsigned int followUpState);
```

## Description

Sets up a comparison operation for the state stateId of the Slave slaveId.

DLC value range: 0 ... 8 (bytes)

The functionality to set the DLC is only available with LIN specification 1.2 (or above)!

LIN specification 1.1 presets the DLC of an identifier.

## Return Values

Nonzero if the comparison operator was configured; else 0.
The contents of messages with the identifier pattern RequestId that are sent on the LIN bus are linked bitwise with maskBytes by an AND operation. If the result of this comparison is identical to patternBytes, the Slave transitions to the state followUpState.
Since multiple comparisons may be configured for the same message identifier for a given Slave state, a code uniqueKey is also necessary to permit identification of the various comparison operations.
This code must be unique within the Slave state. If there are multiple comparison operations for a message identifier within a state of a Slave, they are processed in the order of their specification until all comparisons have been performed or a comparison was successful.
During a measurement this function can be used to change the following data of a comparison operation already configured in the on preStart event procedure:

## Availability

| Up to Version |
|---|
