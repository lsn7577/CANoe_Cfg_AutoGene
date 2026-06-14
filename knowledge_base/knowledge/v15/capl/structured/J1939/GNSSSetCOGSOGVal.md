# GNSSSetCOGSOGVal

> Category: `J1939` | Type: `function`

## Syntax

```c
dword GNSSSetCOGSOGVal ( dword fixSID, dword cogReference}
```

## Description

This function can be used to change values of the parameter group "COG & SOG, Rapid Update" (PGN 129026) which are not modified by the simulation automatically.

## Parameters

| Name | Description |
|---|---|
| fixSID | 1 if fix sequence ID (255) has to be used, else 0 |
| cogReference | Course Over Ground (COG) reference possible values: 0: true 1: magnetic 2: error 3: null |

## Return Values

error code

## Example

```c
GNSSSetCOGSOGVal ( 0, 1 );
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.5 | 13.0 | — | — | — |
| Restricted To | — | J1939 ISO11783 | J1939 ISO11783 | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
