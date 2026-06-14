# FSIL_DeactivateDTC

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long FSIL_DeactivateDTC(dword spn, byte fmi, dword options); // form 1
long FSIL_DeactivateDTC(dword spn, dword options); // form 2
long FSIL_DeactivateDTC(dbNode node, dword spn, byte fmi, dword options); // form 3
long FSIL_DeactivateDTC(dbNode node, dword spn, dword options); // form 4
```

## Description

This function deactivates a diagnostics trouble code (DTC) and removes it from the list of active DTCs.

A deactivated DTC is no longer reported in message DM1 (Active Diagnostic Trouble Codes, PGN FECAh) but it is moved to the list of previously active DTCs and is reported in the requestable message DM2 (Previously Active Diagnostic Trouble Codes, PGN FECBh).

Note: You can use this function only if support of ISO11783 Diagnostics is enabled by function FSIL_ActivateDiagnosticsSupport.

## Parameters

| Name | Description |
|---|---|
| spn | Suspect Parameter Number of the deactivated DTC, 0..524287. |
| fmi | Failure Mode Indicator of the deactivated DTC, 0.. 31. |
| options | Bit 0 = 0: Send message DM1 as soon as possible. Bit 0 = 1: Send message DM1 with next cycle. |
| node | Simulation node to apply the function. |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 13.0 | 13.0 | — | — | 5.0 |
| Restricted To | — | ISO11783 | ISO11783 | — | — | form 3, 4 ISO11783 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1, 2) | ✔ (form 1, 2) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 3, 4) | ✔ (form 3, 4) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 3, 4) | ✔ (form 3, 4) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
