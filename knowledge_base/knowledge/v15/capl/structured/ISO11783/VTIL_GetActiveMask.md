# VTIL_GetActiveMask

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long VTIL_GetActiveMask(dword & maskId); // form 1
long VTIL_GetActiveMask(dbNode vt, dword & maskId); // form 2
```

## Description

Returns object ID of the active Data or Alarm Mask.

## Parameters

| Name | Description |
|---|---|
| vt | VT simulation node to apply the function |
| maskId | Returns object ID of the active data- or alarm mask |

## Example

Example for test node

```c
long result;
dword maskId;
result = VTIL_GetActiveMask(VT, maskId);
switch (result)
{
  case 0:
    write("ID of current mask is %u", maskId);
    TestStepPass();
    break;
  case -2104: TestStepFail("Currently there is no active Working Set!"); break;
  case -2106: TestStepFail("Currently there is no active Data or Alarm mask!"); break;
  default:    TestStepFail("Unexpected error!"); break;
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 9.0 | 13.0 | — | — | 2.1 |
| Restricted To | — | ISO11783 | ISO11783 | — | — | form 2 ISO11783 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1) | ✔ (form 1) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 2) | ✔ (form 2) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 2) | ✔ (form 2) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
