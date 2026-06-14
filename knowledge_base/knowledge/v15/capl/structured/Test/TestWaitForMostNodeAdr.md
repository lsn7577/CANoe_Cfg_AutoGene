# TestWaitForMostNodeAdr

> Category: `Test` | Type: `function`

## Syntax

```c
long TestWaitForMostNodeAdr(long aValue, unsigned long aTimeout);
```

## Description

The function waits for the expiration of the time aTimeout for the occurrence of the MOST event of a change of its own node address.

## Parameters

| Name | Description |
|---|---|
| aValue | Expected value of the node address that should be in the MOST event. The specification -1 (wildcard) stands for any values. |
| aTimeout | Maximum time that should be waited [ms] (Transmission of 0: no timeout monitoring) |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.1 | — | — | — | — |
| Restricted To | — | MOST25, MOST50, MOST150 | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
