# _KLine_DataInd

> Category: `KLine` | Type: `function`

## Syntax

```c
_KLine_DataInd(byte data[])
```

## Description

Called for a received K-Line request.

## Parameters

| Name | Description |
|---|---|
| data | Data buffer. |

## Return Values

—

## Example

```c
variables
{
   BYTE cKLine_HandleStartCommunication = 0;
   BYTE cKLine_HandleStopCommunication = 1;
}

_KLine_DataInd( byte data[]) // Receive a request
{
   if (cKLine_HandleStartCommunication && data[0] == 0x81)
   {
   BYTE StartCommunicationResp_raw[3] = { 0xC1, 0xEF, 0x8F };
   _Diag_DataRequest( StartCommunicationResp_raw, elcount( StartCommunicationResp_raw), 0);
   }
   else if (cKLine_HandleStopCommunication && data[0] == 0x82)
   {
   BYTE StopCommunicationResp_raw[1] = { 0xC2 };
   _Diag_DataRequest( StopCommunicationResp_raw, elcount( StopCommunicationResp_raw), 0);
   }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.0 SP4 | — | — | — | 1.1 SP2 |
| Restricted To | — | K-Line Real bus mode Online mode ECU simulation | — | — | — | K-Line Real bus mode Online mode ECU simulation |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
