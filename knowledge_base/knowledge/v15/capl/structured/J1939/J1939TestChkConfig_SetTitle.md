# J1939TestChkConfig_SetTitle

> Category: `J1939` | Type: `function`

## Syntax

```c
long J1939TestChkConfig_SetTitle( long aCheckId, char aTitle[] )
```

## Description

This functions sets the title of a check.

The check is displayed in the Write Window and the test report with this title.

## Parameters

| Name | Description |
|---|---|
| aCheckId | identifier of the check |
| aTitle | title of the check |

## Example

```c
// set title of the check
dword checkID;
checkID = J1939TestChkCreate_BAMViolation( 50, 200, 0x00 );

J1939TestChkConfig_SetTitle( checkID, "This is a BAM violation title");
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.0 | 13.0 | — | — | 1.1 SP2 |
| Restricted To | — | J1939 | J1939 | — | — | J1939 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
