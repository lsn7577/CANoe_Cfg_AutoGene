# TestGetWaitPDUData

> Category: `Test` | Type: `function`

## Syntax

```c
long TestGetWaitPDUData (PDU * aPDU); // form 1
long TestGetWaitPDUData (dword explicitJoinIndex, PDU * aPDU); // form 2
```

## Description

If a valid PDU is the last event that triggers a wait instruction, the PDU’s content can be called up with form 1.

Form 2 can only be used for joined events. The number of the joined event (return value of TestJoin...) is here being used as an index.

## Parameters

| Name | Description |
|---|---|
| aPDU | PDU variable of type PDU that should be filled in with this function. It has to be either a type free PDU variable, or a PDU variable that was created for the PDU type that triggered the wait instruction. |
| explicitJoinIndex | Number of the joined event corresponds with the return value of TestJoin.... |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 9.0 SP1 | 13.0 | — | — | 2.1 SP2 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
