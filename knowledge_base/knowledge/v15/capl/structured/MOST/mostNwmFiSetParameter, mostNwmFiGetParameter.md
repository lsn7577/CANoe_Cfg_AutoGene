# mostNwmFiSetParameter, mostNwmFiGetParameter

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostNwmFiSetParameter(long paramID, long value);
long mostNwmFiGetParameter(long paramID);
```

## Description

In order to modify timing parameters the functions mostNwmFiSetParameter and mostNwmFiGetParameter provide access to the timing parameters of CANoe’s NetworkMaster implementation.

Use the function with care since the state machine of the NetworkMaster is not guaranteed to work properly afterwards.

Refer to the MOST specification for a detailed description of the timing parameters and the NetworkMaster state machine.

The function is available for CAPL programs assigned to the NetworkMaster block in the Simulation Setup.

## Parameters

| Name | Description |
|---|---|
| paramID | -1: set default for all parameter values1: timer value tWaitBeforeScan (value range: 1…20000 ms)2: timer value tWaitAfterNCE (value range: 1…20000 ms)3: timer value tWaitForAnswer (value range: 1…20000 ms)4: timer value tDelayCfgRequest1 (value range: 1…200000 ms)5: timer value tDelayCfgRequest2 (value range: 1…200000 ms) |
| value | New value to be set. |

## Example

```c
// set the timer value for tDelayCfgRequest2 to 15 s
mostNwmFiSetParameter(5, 15000);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.2 | — | — | — | —✔ |
| Restricted To | — | MOST25 MOST50 MOST150 | — | — | — | —✔ |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | — |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | —✔ |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | —✔ |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | —✔ |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | —✔ |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | —✔ |
| 32-Bit | — | ✔ | — | N/A | — | —✔ |
| 64-Bit | — | ✔ | — | — | — | —✔ |
