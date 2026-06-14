# ChkConfig_SetPDUIDFormat

> Category: `Test` | Type: `function`

## Syntax

```c
long ChkConfig_SetPDUIDFormat(dword format);
```

## Description

Sets the format of the header ID for the current bus context. It affects the next checks that are created after calling this function.

It may be used if not the default header ID format shall be used. Default:

## Parameters

| Name | Description |
|---|---|
| format | Format of the header ID. 0: Default 1: Use always short header ID 2: Use always long header ID |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 9.0 SP3 | 13.0 | — | 14 | 9.0 SP3 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | — | ✔ | N/A |
