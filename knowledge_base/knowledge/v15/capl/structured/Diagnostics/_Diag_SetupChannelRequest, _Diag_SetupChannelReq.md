# _Diag_SetupChannelRequest, _Diag_SetupChannelReq

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void _Diag_SetupChannelReq (); // form 1
void _Diag_SetupChannelRequest(char target[]); // form 2
```

## Description

With this function the CAPL program of a tester implementation will be requested to open a channel to the ECU. After opening the channel the CAPL program can call the function diag_SetupChannelCon.

## Parameters

| Name | Description |
|---|---|
| target | Qualifier of the ECU to open a channel to. |

## Return Values

—

## Example

```c
_Diag_SetupChannelRequest(char target[])
{
  Diag_SetupChannelCon(); // On CAN there is no need to wait for the communication channel to be established
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.1: form 1 11.0: form 2 | — | — | — | 1.0: form 1 3.0: form 2 |
| Restricted To | — | Online mode | — | — | — | Online mode |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
