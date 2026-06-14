# TCIL_GetValueRaw, TCIL_GetValuePhysical

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long TCIL_GetValueRaw(dbNode client, dword ddi, dword elementNumber, long & value); // form 1
long TCIL_GetValueRaw(dword addressClient, dword ddi, dword elementNumber, long & value); // form 2
long TCIL_GetValuePhysical(dbNode client, dword ddi, dword elementNumber, double & value); // form 3
long TCIL_GetValuePhysical(dword addressClient, dword ddi, dword elementNumber, double & value); // form 4
long TCIL_GetValueRaw(dbNode tc, dbNode client, dword ddi, dword elementNumber, long & value); // form 5
long TCIL_GetValueRaw(dbNode tc, dword addressClient, dword ddi, dword elementNumber, long & value); // form 6
long TCIL_GetValuePhysical(dbNode tc, dbNode client, dword ddi, dword elementNumber, double & value); // form 7
long TCIL_GetValuePhysical(dbNode tc, dword addressClient, dword ddi, dword elementNumber, double & value); // form 8
```

## Description

These functions return the current value of a data entity of the Task Controller. No Request Value command is sent.

## Parameters

| Name | Description |
|---|---|
| tc | Task Controller simulation node to apply the function. |
| client | Task Controller client node the data entity belongs to. |
| addressClient | Address of the Task Controller client node the data entity belongs to. |
| ddi | Data dictionary identifier, 0x0000..0xFFFF. |
| elementNumber | Element number, 0x000..0xFFF. |
| value | Returns the value of the process data variable. |

## Example

Example form 5

```c
void CheckValue(double referenceValue)
{
  long result;
  double value;
  result = TCIL_GetValuePhysical(TC, Sprayer, 6, 1, value);
  if (result == 0)
  {
    if (value == referenceValue)
    {
      TestStepPass();
    }
    else
    {
      TestStepFail("CheckValue", "Value of data entity (DDI 6 , element number 1) is different (Expected value: %f)", referenceValue);
    }
  }
  else
  {
    TestStepFail("CheckValue", "Failed to get value of data entity (DDI 6 , element number 1). Error %i", result);
  }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 9.0: form 1, 3, 5, 7 13.0: form 2, 4, 6, 8 | 13.0 | — | — | 2.1: form 5, 7 5.0: form 6, 8 |
| Restricted To | — | ISO11783 | ISO11783 | — | — | form 5, 6, 7, 8 ISO11783 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1, 2, 3, 4) | ✔ (form 1, 2, 3, 4) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form form 5, 6, 7, 8) | ✔ (form form 5, 6, 7, 8) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form form 5, 6, 7, 8) | ✔ (form form 5, 6, 7, 8) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
