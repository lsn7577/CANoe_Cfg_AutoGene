# CANdelaLibCloseChannel

> Category: `Obsolete` | Type: `function`

## Syntax

```c
void CANdelaLibCloseChannel(char ECUqualifier[])
```

## Description

Closes the communication channel to the control unit, thereby terminating the sending of 'Tester Present' on the selected diagnostic channel for the selected diagnostic descriptions.

If necessary in the context of sending requests from the Diagnostic Console, the Fault Memory Window and diagnostic test modules which do not implement a dedicated callback interface for the transport protocol layer, the channel can be restored automatically.

This function can be used, for example, to ensure that a 'Tester Present' sent cyclically does not prevent the bus switching to sleep mode in the context of network management when the Diagnostic Console is in use.

## Return Values

void

## Availability

| Up to Version |
|---|
