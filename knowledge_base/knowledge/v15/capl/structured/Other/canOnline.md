# canOnline

> Category: `Other` | Type: `function`

## Syntax

```c
void canOnline(); // form 1: deprecated
dword canOnline(dword flags); // form 2
```

## Description

Restores the connection of the node to the bus. After a call to the function canOffline() the node can be connected to the bus with the function canOnline(). Messages send from the node are passed through to the bus.

If the node is set to offline, output instructions for sending messages in CAPL or NodeLayer DLL are ignored (refers to a node locally only).Regardless of the status, all messages are received in the CAPL program/NodeLayer.

Form 1 only has an effect on the CAPL-program.

In form 2 you can choose between the CAPL-program and/or the Nodelayer-DLL.

## Parameters

| Name | Description |
|---|---|
| 1 | Activates the CAPL-program |
| 2 | Activates the Nodelayer |
| 3 | Activates the CAPL-program and the Nodelayer and attaches the diagnostic ECU simulation to the network, if one is configured for the node |

## Return Values

Form 2 returns the part of the node being online before the function call. Equal to the flags.

## Example

```c
dword var;
var = canOffline(3); // Deactivates CAPL-Program and Nodelayer-DLL.
...
canOnline(); // Activates CAPL-Program. Form 1
...
var = canOnline(2); // Activates Nodelayer-DLL
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | All | 13.0 | — | 14 | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | — | ✔ | N/A |
