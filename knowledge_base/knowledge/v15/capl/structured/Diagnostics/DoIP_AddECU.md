# DoIP_AddECU

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void DoIP_AddECU( dword address);
```

## Description

Adds a valid DoIP ECU address to the DoIP layer.

## Parameters

| Name | Description |
|---|---|
| address | Logical DoIP address of an ECU. You must set at least one logical ECU address (e.g. the logical DoIP address of the DoIP entity). |

## Example

```c
DoIP_AddECU( 0x200);
DoIP_AddECU( 0x201);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.1 SP4 | — | — | — | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
