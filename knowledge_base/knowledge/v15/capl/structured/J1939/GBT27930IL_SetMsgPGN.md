# GBT27930IL_SetMsgPGN

> Category: `J1939` | Type: `function`

## Syntax

```c
long GBT27930IL_SetMsgPGN(dbMsg dbMessage, dword priority ); // form 1
long GBT27930IL_SetMsgPGN(dbNode node, dbMsg dbMessage, dword pgn ); // form 2
```

## Description

Sets new value of PGN.

## Parameters

| Name | Description |
|---|---|
| dbMessage | Message name as defined in the database. |
| pgn | New value of PGN. |
| node | Simulation node to apply the function. |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 12.0 SP4 | 13.0 | — | — | 4.0 SP4 |
| Restricted To | — | J1939 and Smart Charging | J1939 and Smart Charging | — | — | form 2 J1939 and Smart Charging |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1) | ✔ (form 1) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 2) | ✔ (form 2) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 2) | ✔ (form 2) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
