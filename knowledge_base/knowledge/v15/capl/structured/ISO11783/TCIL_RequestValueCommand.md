# TCIL_RequestValueCommand

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long TCIL_RequestValueCommand(dbNode client, dword ddi, dword elementNumber); // form 1
long TCIL_RequestValueCommand(dword addressClient, dword ddi, dword elementNumber); // form 2
long TCIL_RequestValueCommand(dbNode tc, dbNode client, dword ddi, dword elementNumber); // form 3
long TCIL_RequestValueCommand(dbNode tc, dword addressClient, dword ddi, dword elementNumber); // form 4
```

## Description

This function sends the Request Value command to the client.

## Parameters

| Name | Description |
|---|---|
| tc | Task Controller simulation node to apply the function. |
| client | Task Controller client node the TC sends the Request Value command to. |
| addressClient | Address of the Task Controller client node the TC sends the Request Value command to. |
| ddi | Data dictionary identifier, 0x0000..0xFFFF. |
| elementNumber | Element number, 0x000..0xFFF. |

## Example

Example form 3

```c
long result;
result = TCIL_RequestValueCommand(TC, Sprayer, 6, 3);
if (result != 0)
{
  TestStepFail("RequestValue", "Failed to request value of data entity (DDI 6 , element number 1). Error %i", result);
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
