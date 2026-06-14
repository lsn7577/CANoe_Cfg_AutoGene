# mostRcvSpyMessagesOnly

> Category: `MOST` | Type: `function`

## Syntax

```c
mostRcvSpyMessagesOnly ();
```

## Description

The MOST message handling routines of this node are only called if the message was received by the Spy of the bus interfaces.

This mode is especially useful for nodes that act as pure observers or – with the help of the Spy – are used to perform cross-node analysis.

Queries such as "if (!this.MOST_IsSpy) return;" have been eliminated in the message handling routines, because the message handling routines are no longer called by node and Spy messages.

## Return Values

—

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.0 | — | — | — | —✔ |
| Restricted To | — | MOST25 MOST50 MOST150 | — | — | — | —✔ |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | — |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | —✔ |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | —✔ |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | —✔ |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | —✔ |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | —✔ |
| 32-Bit | — | ✔ | — | N/A | — | —✔ |
| 64-Bit | — | ✔ | — | — | — | —✔ |
