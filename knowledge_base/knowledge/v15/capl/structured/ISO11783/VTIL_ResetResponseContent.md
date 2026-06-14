# VTIL_ResetResponseContent

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long VTIL_ResetResponseContent(dbNode workingSetMaster, byte vtFunction); // form 1
long VTIL_ResetResponseContent(dword addressWorkingSetMaster, byte vtFunction); // form 2
long VTIL_ResetResponseContent(dbNode vt, dbNode workingSetMaster, byte vtFunction); // form 3
long VTIL_ResetResponseContent(dbNode vt, dword addressWorkingSetMaster, byte vtFunction); // form 4
```

## Description

The function resets the response modification of VTIL_SetResponseContent. Afterwards the default response is sent by the VT IL.

## Parameters

| Name | Description |
|---|---|
| vt | VT simulation node to apply the function |
| workingSetMaster | Receiver of the VT12 response message |
| addressWorkingSetMaster | Address of the Receiver of the VT12 response message |
| vtFunction | The function refers to the response with this VT function value |

## Example

Example form 3, 4

```c
long result;
result = VTIL_ResetResponseContent(VT, Sprayer, 168);
if (result < 0)
{
  TestStepFail("Failed to reset fault injection");
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 9.0: form 1, 3 13.0: form 2, 4 | 13.0 | — | — | 2.1: form 3 5.0: form 4 |
| Restricted To | — | ISO11783 | ISO11783 | — | — | form 3, 4 ISO11783 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1, 2) | ✔ (form 1, 2) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 3, 4) | ✔ (form 3, 4) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 3, 4) | ✔ (form 3, 4) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
