# _KLine_DataInd

> Category: `KLine` | Type: `function`

## Syntax

```c
_KLine_DataInd(byte data[])
```

## Description

Called for a received K-Line request.

This function models a K-Line TP layer which is required for a ECU simulation.

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

| Since Version |
|---|
