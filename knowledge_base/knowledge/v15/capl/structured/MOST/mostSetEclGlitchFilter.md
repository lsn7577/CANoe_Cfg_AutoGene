# mostSetEclGlitchFilter

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostSetEclGlitchFilter (long channel, long durationus);
```

## Description

Configures the timing of the glitch filter for the ECL. For pulses which are shorter than the given time durations the callback <OnMostEcl> will not be called, neither will those pulses appear in a Trace Window.

## Parameters

| Name | Description |
|---|---|
| channel | Channel of the connected interface. |
| durationus | Minimum duration of a pulse in µs required to generate an event which calls <OnMostECL>. The value ranges from 50 µs to 50 ms (Default: 1 ms) |

## Return Values

See error codes

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 7.6 SP3 | 7.6 SP3 | — | — | — | —✔ |
| Restricted To | MOST150 | MOST150 | — | — | — | —✔ |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | — |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | —✔ |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | —✔ |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | —✔ |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | —✔ |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | —✔ |
| 32-Bit | ✔ | ✔ | — | N/A | — | —✔ |
| 64-Bit | ✔ | ✔ | — | — | — | —✔ |
