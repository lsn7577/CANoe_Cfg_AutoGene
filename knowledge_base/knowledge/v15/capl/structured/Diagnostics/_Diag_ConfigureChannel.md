# _Diag_ConfigureChannel

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void _Diag_ConfigureChannel(char target[]);
```

## Description

This callback function will be called when a diagnostic request has to be sent to a new target. The CAPL node can configure the transport protocol, e.g. set CAN IDs for sending and receiving.

## Parameters

| Name | Description |
|---|---|
| target | Qualifier of the ECU to communicate with. |

## Return Values

—

## Example

```c
_Diag_ConfigureChannel(char target[])
{
  long connectionHandle;
  connectionHandle = CreateConnection(target);
  TPLayer_SetTxId(connectionHandle, GetTxId(target));
  TPLayer_SetRxId(connectionHandle, GetRxId(target));
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 11.0 | — | — | — | 3.0 |
| Restricted To | — | Online mode | — | — | — | Online mode |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
