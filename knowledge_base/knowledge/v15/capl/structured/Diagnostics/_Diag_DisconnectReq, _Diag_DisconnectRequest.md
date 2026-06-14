# _Diag_DisconnectReq, _Diag_DisconnectRequest

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void _Diag_DisconnectReq(); // form 1
void _Diag_DisconnectRequest(char target[]); // form 2
```

## Description

The diagnostic communication channel to the target with the given qualifier shall be closed. For connectionless transport protocols, diag_ClosedChannelInd can be called immediately. Otherwise the completion of the channel closing must be indicated when the TP layer indicates it.

For connection oriented protocols the CAPL program can call a close connection routine of the TP layer.

## Parameters

| Name | Description |
|---|---|
| target | Qualifier of the ECU whose communication channel shall be closed. |

## Return Values

—

## Example

```c
// disconnect request callback for DoIP
_Diag_DisconnectReq()
{
  DoIP_CloseConnection();
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 12.0 SP3: form1 11.0: form 2 | — | — | — | 4.0 SP3: form 1 3.0: form 2 |
| Restricted To | — | Online mode | — | — | — | Online mode |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
