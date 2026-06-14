# J1939ILActivateDTC

> Category: `J1939` | Type: `function`

## Syntax

```c
long J1939ILActivateDTC(dword spn, byte fmi, dword options); // form 1
long J1939ILActivateDTC(dword spn, byte fmi, byte occurrenceCount, dword options); // form 2
long J1939ILActivateDTC(dbNode node, dword spn, byte fmi, dword options); // form 3
long J1939ILActivateDTC(dbNode node, dword spn, byte fmi, byte occurrenceCount, dword options); // form 4
```

## Description

This function activates a diagnostics trouble code (DTC) and add it to the list of active DTCs.

This list with active DTCs is reported in the message DM1.

The occurrence count of the DTC is either determined automatically (form 1, 3) or set to a specific value (form 2, 4). Calling form 1 or 3 of the function increments the occurrence count of the DTC with every call.

The DTC is uniquely identified by the combination of SPN and FMI.

The activated DTC uses conversion method 4 (SPN represented as Intel format for all 19 bits with the SPN Conversion Method set to 0).

If a previously active DTC (reported with DM2) is activated again then it is removed from the list of previous active DTCs (and therefore no more reported in message DM2).

You can deactivate an activated DTC with J1939ILDeactivateDTC.

Note: You can use this function only if support of <J1939|ISO11783> Diagnostics is enabled by function J1939ILActivateDiagnosticsSupport.

## Parameters

| Name | Description |
|---|---|
| spn | Suspect Parameter Number of the activated DTC, 0..524287. |
| fmi | Failure Mode Indicator of the activated DTC, 0.. 31. |
| options | Bit 0 = 0: Send message DM1 as soon as possible. Bit 0 = 1: Send message DM1 with next cycle. |
| occurrenceCount | Occurrence Count of the activated DTC, 0..127. If a form without this parameter is used, then the occurrence count is determined automatically. |
| node | Simulation node to apply the function. |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 13.0 | 13.0 | — | — | 5.0 |
| Restricted To | — | J1939 | J1939 | — | — | form 3, 4 J1939 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1, 2) | ✔ (form 1, 2) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 3, 4) | ✔ (form 3, 4) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 3, 4) | ✔ (form 3, 4) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
