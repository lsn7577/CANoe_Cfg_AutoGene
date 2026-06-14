# TestWaitForMostAllBypass

> Category: `Test` | Type: `function`

## Syntax

```c
long TestWaitForMostAllBypass(long aValue, unsigned long aTimeout);
```

## Description

Use this function to determine whether the bypass on the MOST hardware connected to the channel has been set to the specified condition within the waiting time. The wait point is only triggered if a change to this condition takes place.

The following can be entered as possible condition values: 1 for closed bypass and 0 for open bypass. In the case of a closed bypass, the MOST device can not be seen by the other devices in the loop.

## Parameters

| Name | Description |
|---|---|
| 1 | Bypass is closed |
| 0 | Bypass is opened |
| aTimeout | Maximum wait time [ms] (Transmission of 0: no timeout controlling); test module waits infinitely long) |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.2 | — | — | — | — |
| Restricted To | — | MOST25, MOST50, MOST150 | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
