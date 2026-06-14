# Iso11783IL_GetDTCStatus

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_GetDTCStatus(dword spn, byte fmi, word& state, word& occurrenceCount); // form 1
long Iso11783IL_GetDTCStatus(dbNode node, dword spn, byte fmi, word& state, word& occurrenceCount); // form 2
```

## Description

This function returns the current occurrence count of a diagnostics trouble code (DTC).

The function checks the list of active DTCs and the list of previously active DTCs for the specified DTC.

Note: You can use this function only if support of ISO11783 Diagnostics is enabled by function Iso11783IL_ActivateDiagnosticsSupport.

## Parameters

| Name | Description |
|---|---|
| spn | Suspect Parameter Number of wanted DTC, 0..524287. |
| fmi | Failure Mode Indicator of wanted DTC, 0.. 31. |
| state | Returns the current state of the DTC. 0: DTC is not active and hasn’t been previously active. 1: DTC is active. 2: DTC has been previously active. |
| occurrenceCount | Returns the current occurrent count of the DTC. If DTC has never been active the returned occurrence count is 0. |
| node | Simulation node to apply the function. |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 13.0 | 13.0 | — | — | 5.0 |
| Restricted To | — | ISO11783 | ISO11783 | — | — | form 2 ISO11783 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1) | ✔ (form 1) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 2) | ✔ (form 2) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 2) | ✔ (form 2) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
