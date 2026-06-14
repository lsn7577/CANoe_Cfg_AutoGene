# mostGenerateEclSequence

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostGenerateEclSequence (long channel, long startstop);
```

## Description

Starts the generation of the signal sequence on the ECL which was prepared by mostConfigureEclSequence. Dominant levels will be set actively whereas during recessive phases the generator is passive and other devices connected to the ECL may pull the line to dominant level.

## Parameters

| Name | Description |
|---|---|
| channel | Channel of the connected interface. |
| startstop | 0: stops the generation of the sequence1: starts the generation of the sequence |

## Return Values

See error codes

## Example

See mostConfigureEclSequence

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
