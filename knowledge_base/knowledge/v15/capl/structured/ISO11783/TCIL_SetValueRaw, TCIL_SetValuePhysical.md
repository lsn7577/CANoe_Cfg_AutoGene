# TCIL_SetValueRaw, TCIL_SetValuePhysical

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long TCIL_SetValueRaw(dbNode client, dword ddi, dword elementNumber, long value); // form 1
long TCIL_SetValueRaw(dword addressClient, dword ddi, dword elementNumber, long value); // form 2
long TCIL_SetValueRaw(dbNode tc, dbNode client, dword ddi, dword elementNumber, long value); // form 3
long TCIL_SetValueRaw(dbNode tc, dword addressClient, dword ddi, dword elementNumber, long value); // form 4
long TCIL_SetValuePhysical(dbNode client, dword ddi, dword elementNumber, double value); // form 5
long TCIL_SetValuePhysical(dword addressClient, dword ddi, dword elementNumber, double value); // form 6
long TCIL_SetValuePhysical(dbNode tc, dbNode client, dword ddi, dword elementNumber, double value); // form 7
long TCIL_SetValuePhysical(dbNode tc, dword addressClient, dword ddi, dword elementNumber, double value); // form 8
```

## Description

These functions set the value of a data entity without sending any command.

## Parameters

| Name | Description |
|---|---|
| tc | Task Controller simulation node to apply the function. |
| client | Task Controller client node the data entity belongs to. |
| addressClient | Address of the Task Controller client node the data entity belongs to. |
| elementNumber | Element number, 0x000..0xFFF. |
| ddi | Data dictionary identifier, 0x0000..0xFFFF. |
| value | New value of the data entity. |

## Example

Example form 7

```c
void SetSetpointMassPerAreaApplicationRate(double value)
{
  long result;
  result = TCIL_SetValuePhysical(TC, Sprayer, 6, 1, value);
  switch (result)
  {
    case     0: TestStepPass(); break;
    case -2202: TestStepFail("Function is not available in passive mode of the TC IL!"); break;
    case -2204: TestStepFail("Node 'Sprayer' is no client device!"); break;
    default:    TestStepFail("Unexpected error"); break;
  }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 9.0: form 1, 3, 5, 7 13.0: form 2, 4, 6, 8 | 13.0 | — | — | 2.1: form 3, 7 5.0: form 4. 8 |
| Restricted To | — | ISO11783 | ISO11783 | — | — | form 3, 4, 7, 8 ISO11783 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1, 2, 5, 6) | ✔ (form 1, 2, 5, 6) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form form 3, 4, 7, 8) | ✔ (form form 3, 4, 7, 8) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form form 3, 4, 7, 8) | ✔ (form form 3, 4, 7, 8) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
