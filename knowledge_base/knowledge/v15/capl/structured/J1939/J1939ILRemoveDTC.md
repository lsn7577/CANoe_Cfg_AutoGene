# J1939ILRemoveDTC

> Category: `J1939` | Type: `function`

## Syntax

```c
long J1939ILRemoveDTC(dword pgn, dword spn, byte fmi); // form 1
long J1939ILRemoveDTC(dword pgn, dword spn); // form 2
long J1939ILRemoveDTC(dbNode node, dword pgn, dword spn, byte fmi); // form 3
long J1939ILRemoveDTC(dbNode node, dword pgn, dword spn); // form 4
```

## Description

This function removes a diagnostics trouble code (DTC) from a diagnostics message which has been added by J1939ILAddDTC.

Form 2 and 4 removes all DTCs with the specified SPN (regardless of FMI).

A removed DTC is no longer reported by the message if the message is requested.

Note: You can use this function only if support of J1939 Diagnostics is enabled by function J1939ILActivateDiagnosticsSupport.

## Parameters

| Name | Description |
|---|---|
| pgn | Parameter Group Number (PGN) of the message which shall contain the DTC. |
| spn | Suspect Parameter Number of the deactivated DTC, 0..524287. |
| fmi | Failure Mode Indicator of the deactivated DTC, 0.. 31. |
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
