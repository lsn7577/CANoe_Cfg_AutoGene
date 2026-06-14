# C2xTestGetWaitForMessage

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xTestGetWaitForMessage(long &packethandle) // form 1
long C2xTestGetWaitForMessage(long index, long &packethandle) // form 2
```

## Description

If a valid Car2x message is the last event that triggers a wait instruction, the packet's handle can be called up with form 1.

Form 2 can only be used for joined events. The number of the joined event (return value of C2xTestJoin…) is here being used as an index.

## Parameters

| Name | Description |
|---|---|
| packetHandle | A packet handle for the awaited Car2x message. |
| Index | Number of the joined event corresponds with the return value of C2xTestJoin…. |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 13.0: form 1, 2 | — | — | — | 5.0: form 1, 2 |
| Restricted To | — | Car2x, Testnodes: form 1, 2 | — | — | — | Car2x |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
