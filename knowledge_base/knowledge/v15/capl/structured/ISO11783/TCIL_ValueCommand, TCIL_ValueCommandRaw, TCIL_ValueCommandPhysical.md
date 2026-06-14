# TCIL_ValueCommand, TCIL_ValueCommandRaw, TCIL_ValueCommandPhysical

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long TCIL_ValueCommand(dbNode client, dword ddi, dword elementNumber); // form 1
long TCIL_ValueCommand(dword addressClient, dword ddi, dword elementNumber); // form 2
long TCIL_ValueCommand(dbNode tc, dbNode client, dword ddi, dword elementNumber); // form 3
long TCIL_ValueCommand(dbNode tc, dword addressClient, dword ddi, dword elementNumber); // form 4
long TCIL_ValueCommandRaw(dbNode client, dword ddi, dword elementNumber, long value); // form 5
long TCIL_ValueCommandRaw(dword addressClient, dword ddi, dword elementNumber, long value); // form 6
long TCIL_ValueCommandRaw(dbNode tc, dbNode client, dword ddi, dword elementNumber, long value); // form 7
long TCIL_ValueCommandRaw(dbNode tc, dword addressClient, dword ddi, dword elementNumber, long value); // form 8
long TCIL_ValueCommandPhysical(dbNode client, dword ddi, dword elementNumber, double value); // form 9
long TCIL_ValueCommandPhysical(dword addressClient, dword ddi, dword elementNumber, double value); // form 10
long TCIL_ValueCommandPhysical(dbNode tc, dbNode client, dword ddi, dword elementNumber, double value); // form 11
long TCIL_ValueCommandPhysical(dbNode tc, dword addressClient, dword ddi, dword elementNumber, double value); // form 12
```

## Description

Form (1) and (3) send the current value of the specified data entity to the client with Value command. It can be used to send to the client the previously set Compressed State DDIs (using TCIL_SetValueRaw or TCIL_SetValuePhysical).

Form (5)-(12) set the value to the specified data entity (if exists) and sends the value to the client with Value command.

## Parameters

| Name | Description |
|---|---|
| tc | Task Controller simulation node to apply the function. |
| client | Task Controller client node the TC sends the Value command to. |
| addressClient | Address of the Task Controller client node the TC sends the Value command to. |
| elementNumber | Element number, 0x000..0xFFF. |
| ddi | Data dictionary identifier, 0x0000..0xFFFF. |
| value | New value of the data entity. |

## Example

Example form 11

```c
void SendSetpointMassPerAreaApplicationRate(long double value)
{
  long result;
  result = TCIL_ValueCommandPhysical(TC, Sprayer, 6, 1, value);
  switch (result)
  {
    case     0: TestStepPass(); break;
    case -2202: TestStepFail("Function is not available in passive mode of the TC IL!"); break;
    case -2204: TestStepFail("Node 'Sprayer' is no client device!"); break;
    case -2210: TestStepFail("Failed to send Value command!"); break;
    default:    TestStepFail("Unexpected error"); break;
  }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 9.0: form 1, 3, 5, 7, 9, 11 13.0: form 2, 4, 6, 8, 10, 12 | 13.0 | — | — | 2.1: form 3, 7, 11 5.0: form 4, 8, 12 |
| Restricted To | — | ISO11783 | ISO11783 | — | — | form 3, 4, 7, 8, 11, 12 ISO11783 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1, 2, 5, 6, 9, 10) | ✔ (form 1, 2, 5, 6, 9, 10) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 3, 4, 7, 8, 11, 12) | ✔ (form 3, 4, 7, 8, 11, 12) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 3, 4, 7, 8, 11, 12) | ✔ (form 3, 4, 7, 8, 11, 12) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
