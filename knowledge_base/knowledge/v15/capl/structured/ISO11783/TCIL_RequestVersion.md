# TCIL_RequestVersion

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long TCIL_RequestVersion(dbNode client); // form 1
long TCIL_RequestVersion(dword addressClient); // form 2
long TCIL_RequestVersion(dbNode tc, dbNode client); // form 3
long TCIL_RequestVersion(dbNode tc, dword addressClient); // form 4
```

## Description

This function requests the Version message from the client.

## Parameters

| Name | Description |
|---|---|
| tc | Task Controller simulation node to apply the function. |
| client | Task Controller client node the TC sends the Request Version to. |
| addressClient | Address of the Task Controller client node the TC sends the Request Version to. |

## Example

Example form 3

```c
long result;
result = TCIL_RequestVersion(TC, Sprayer);
switch (result)
{
  case     0: TestStepPass(); break;
  case -2202: TestStepFail("Function is not available in passive mode of the TC IL!"); break;
  case -2204: TestStepFail("Node 'Sprayer' is no client device!"); break;
  case -2210: TestStepFail("Failed to send Request Version message!"); break;
  default:    TestStepFail("Unexpected error"); break;
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
| CANoe Test Setup for Test Modules | N/A | ✔ (form form 3, 4) | ✔ (form form 3, 4) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form form 3, 4) | ✔ (form form 3, 4) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
