# VTIL_GetNextTAN

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long VTIL_GetNextTAN(byte workingSetMasterAddress, dword& tan); // form 1
long VTIL_GetNextTAN(dbNode vt, byte workingSetMasterAddress, dword& tan); // form 2
```

## Description

Gets the TAN that will be used in the next activation message.

## Parameters

| Name | Description |
|---|---|
| vt | VT simulation node to apply the function. |
| workingSetMasterAddress | Address of the Working Set Master |
| tan | Returns the next TAN. |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 14 | 13.0 | — | — | 5 |
| Restricted To | — | ISO11783 | ISO11783 | — | — | form 2 ISO11783 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1) | ✔ (form 1) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 2) | ✔ (form 2) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 2) | ✔ (form 2) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
