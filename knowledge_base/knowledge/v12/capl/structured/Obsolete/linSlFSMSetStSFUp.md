# linSlFSMSetStSFUp

> Category: `Obsolete` | Type: `function`

## Syntax

```c
long linSlFSMSetStSFUp (unsigned int slaveId, unsigned int stateId, unsigned int requestId, unsigned long dlc, unsigned char dataBytes[], unsigned char checksum, unsigned int followUpState);
```

## Description

Causes the Slave with identifier slaveId that is in the specified state stateId to respond to the transmit request for the message with identifier requestId. This involves using the data specified in dataBytes and the checksum.

DLC value range: 0 ... 8 (bytes)

The functionality to set the DLC is only available with LIN specification 1.2 (or above)!

LIN specification 1.1 presets the DLC of an identifier.

## Return Values

Nonzero if the action was configured, else 0.
During a measurement the following data can be modified for an action already configured in the on preStart event procedure:

## Availability

| Up to Version |
|---|
