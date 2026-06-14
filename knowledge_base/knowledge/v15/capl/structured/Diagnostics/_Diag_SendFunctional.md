# _Diag_SendFunctional

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void _Diag_SendFunctional (BYTE data[]);
```

## Description

With this CAPL callback function CANoe triggers the CAPL program to send a functional diagnostic request.

## Parameters

| Name | Description |
|---|---|
| data | The data of the diagnostic primitive (request) that should be transmitted on the bus. |

## Return Values

—

## Example

```c
_Diag_SendFunctional( BYTE data[])
{
  // Send data on the functional TP connection created earlier
  CanTpSendData( gHandleFunctional, data, elcount( data));
  write("_Diag_SendFunctional data[0]=%d", data[0]);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.2 | — | — | — | 1.1 |
| Restricted To | — | Real bus mode Online mode ECU tester | — | — | — | Real bus mode Online mode ECU tester |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
