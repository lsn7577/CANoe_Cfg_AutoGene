# J1939ILAddDTC

> Category: `J1939` | Type: `function`

## Syntax

```c
long J1939ILAddDTC(dword pgn, dword spn, byte fmi, byte occurrenceCount); // form 1
long J1939ILAddDTC(dbNode node, dword pgn, dword spn, byte fmi, byte occurrenceCount); // form 2
```

## Description

This function adds a diagnostics trouble code (DTC) to a diagnostics message.

If the diagnostics message with the specified PGN is requested, the response contains the added DTC.

The added DTC uses conversion method 4 (SPN represented as Intel format for all 19 bits with the SPN Conversion Method set to 0).

You can remove an added DTC with function J1939IL_RemoveDTC.

Note: You can use this function only if support of J1939 Diagnostics is enabled by function J1939ILActivateDiagnosticsSupport.

## Parameters

| Name | Type | Description |
|---|---|---|
| spn |  | Suspect Parameter Number of the deactivated DTC, 0..524287. |
| fmi |  | Failure Mode Indicator of the deactivated DTC, 0.. 31. |
| State |  | Returns the current state of the DTC. 0: DTC is not active and hasn’t been previously active. 1: DTC is active. 2: DTC has been previously active. |
| occurrenceCount |  | Occurrence Count of the activated DTC, 0..127. |
| PGN | Acronym | Message |
| FECAh | DM1 | Active Diagnostic Trouble Codes |
| FECBh | DM2 | Previously Active Diagnostic Trouble Codes |
| FECFh | DM6 | Emission-Related Pending Diagnostic Trouble Codes |
| FED4h | DM12 | Emission-Related MIL-On Diagnostic Trouble Codes |
| FDB5h | DM23 | Emission-Related Previously MIL-On Diagnostic Trouble Codes |
| FD82h | DM27 | All Pending DTCs |
| FD80h | DM28 | Emission-Related Permanent Diagnostic Trouble Codes |
| 9F00h | DM35 | Immediate Fault Status |
| FD5Fh | DM41 | DTCs - A, Pending |
| FD5Eh | DM42 | DTCs - A, Confirmed and Active |
| FD5Dh | DM43 | DTCs - A, Previously Active |
| FD5Ch | DM44 | DTCs - B1, Pending |
| FD5Bh | DM45 | DTCs - B1, Confirmed and Active |
| FD5Ah | DM46 | DTCs - B1, Previously Active |
| FD59h | DM47 | DTCs - B2, Pending |
| FD58h | DM48 | DTCs - B2, Confirmed and Active |
| FD57h | DM49 | DTCs - B2, Previously Active |
| FD56h | DM50 | DTCs - C, Pending |
| FD55h | DM51 | DTCs - C, Confirmed and Active |
| FD54h | DM52 | DTCs - C, Previously Active |
| node |  | Simulation node to apply the function. |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 13.0 | 13.0 | — | — | 5.0 |
| Restricted To | — | J1939 | J1939 | — | — | form 2 J1939 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1) | ✔ (form 1) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 2) | ✔ (form 2) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 2) | ✔ (form 2) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
