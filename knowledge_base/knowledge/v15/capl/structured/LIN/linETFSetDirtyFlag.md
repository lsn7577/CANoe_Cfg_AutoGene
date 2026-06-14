# linETFSetDirtyFlag

> Category: `LIN` | Type: `function`

## Syntax

```c
long linETFSetDirtyFlag(long assocId, long dirty);
```

## Description

With this function it is possible to set/clear the dirty flag of an associated frame. If the dirty flag of an associated frame is set when the corresponding event-triggered frame is being requested, then the LIN hardware will try to transmit the associated frame's data. The dirty flag gets reset automatically when the associated frame has been sent successfully – either via the event-triggered frame or unconditionally.

## Parameters

| Name | Description |
|---|---|
| assocId | Identifier of unconditional frame LIN frame identifier of associated (unconditional) frame whose dirty flag should be set or cleared. Value range: 0 .. 63 |
| dirty | 1: Set the dirty flag. 0: Clear the dirty flag. |

## Return Values

On success, a value unequal to zero, otherwise zero.

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 5.2 | 5.2 | 13.0 | 13.0 | — | 1.0 |
| Restricted To | LIN | LIN | LIN | LIN | — | LIN |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | ✔ | — | N/A |
