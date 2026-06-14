# Iso11783IL_SetWSMAddr

> Category: `ISO11783` | Type: `function`

## Syntax

```c
dword Iso11783IL_SetWSMAddr(dword wsmAddress);
```

## Description

Use this function to set the address of the Working Set Master, if this ECU is a member of a working set. All parameter groups which are addressed to the Working Set Master are also received by an ECU which calls this function.

## Parameters

| Name | Description |
|---|---|
| wsmAddress | Address of the Working Set Master for this ECU. |

## Return Values

0 on success or error code

## Example

```c
Iso11783IL_SetWSMAddr(0x06 );
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.0 | 13.0 | — | — | — |
| Restricted To | — | ISO11783 | ISO11783 | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
