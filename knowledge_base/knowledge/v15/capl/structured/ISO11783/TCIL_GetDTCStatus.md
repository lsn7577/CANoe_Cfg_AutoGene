# TCIL_GetDTCStatus

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long TCIL_GetDTCStatus(dword spn, byte fmi, word& state, word& occurrenceCount); // form 1
long TCIL_GetDTCStatus(dbNode node, dword spn, byte fmi, word& state, word& occurrenceCount); // form 2
```

## Description

This function returns the current occurrence count of a diagnostics trouble code (DTC).

The function checks the list of active DTCs and the list of previously active DTCs for the specified DTC.

Note: You can use this function only if support of ISO11783 Diagnostics is enabled by function TCIL_ActivateDiagnosticsSupport.

## Parameters

| Name | Description |
|---|---|
| spn | Suspect Parameter Number of wanted DTC, 0..524287. |
| fmi | Failure Mode Indicator of wanted DTC, 0.. 31. |
| state | Returns the current state of the DTC. 0: DTC is not active and hasn’t been previously active. 1: DTC is active. 2: DTC has been previously active. |
| occurrenceCount | Returns the current occurrent count of the DTC. If DTC has never been active the returned occurrence count is 0. |
| node | Simulation node to apply the function. |

## Example

```c
// Check the occurrence count and state for DTC with SPN=1208 and FMI=15
byte occurrenceCount, dtcState;
if (TCIL_GetDTCStatus(1208, 315, occurrenceCount, dtcState) == 0)
{
  If(dtcState == 1)
  {
    write("'EngPrefilterOilPress above normal (least severe)' is active, occurrence count is %d", occurrenceCount);
  }
  else If(dtcState == 2)
  {
    write("'EngPrefilterOilPress above normal (least severe)' has been previously active, occurrence count is %d", occurrenceCount);
  }
}
```

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
