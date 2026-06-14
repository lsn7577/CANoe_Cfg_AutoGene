# TestWaitForMostApInstID

> Category: `Test` | Type: `function`

## Syntax

```c
long TestWaitForMostApInstID(unsigned long aTimeout);
```

## Description

The function waits for the specified period of time for a special change event of the application socket which is triggered when the InstanceId of an FBlock on its channel changes.

## Parameters

| Name | Description |
|---|---|
| aTimeout | Maximum time that should be waited [ms] (Transmission of 0: no timeout monitoring) |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.2 | — | — | 14 | — |
| Restricted To | — | MOST | — | — | MOST | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | ✔ | N/A |
| 32-Bit | — | ✔ | — | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | — | — | ✔ | N/A |
