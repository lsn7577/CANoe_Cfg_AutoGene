# Iso11783PDDOnPDM

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783PDDOnPDM( long command, long parameter, long senderAddress, long pddStatus );
```

## Description

The callback method is called from the ISO11783 Node Layer if the ISO11783 Node Layer receives the Process Data Message parameter group (PDM pg).

## Parameters

| Name | Description |
|---|---|
| command | First nibble of the first byte of the received PDM pg; usually represents the received command |
| parameter | Second nibble of the first byte of the received PDM pg |
| senderAddress | Address of the sender of the received PDM pg |
| pddStatus | Current state of the Process Data Dictionary 0: not initialized 1: initialized 2: start up delay (6 seconds) 3: wait for task controller status 4: query information 5: transfer object pool 6: object pool activation 7: online 8: task active |

## Example

The following example is to be used in the environment, where more than one Task Controller is available and determines, that the current node has to communicate with the Task Controller with the address 246:

```c
LONG Iso11783PDDOnPDM (long command, long parameter, long senderAddress, long pddStatus)
{
  if (command != 0x0e)
    return 1; //isn't a TC status
  if (pddStatus != 3)
    return 1; //node isn't in a state 'WaitForStatus'
  if (senderAddress == 247)
    return 1;
  else
    return 0;
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 6.1 | 13.0 | — | — | — |
| Restricted To | — | ISO11783 | ISO11783 | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
