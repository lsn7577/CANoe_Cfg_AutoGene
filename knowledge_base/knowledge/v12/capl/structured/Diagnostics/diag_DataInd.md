# diag_DataInd

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void diag_DataInd (byte rxBuffer [], long count, long sender); // form 1
```

## Description

Passes count bytes of the transmitter address sender from the rxBuffer buffer to the diagnostic layer.

Alternatively, the transmitter can be identified using its ECU qualifier target.

This function is typically called in a transport layer callback after a message, which may be segmented, has been received in its entirety. The transport layer removes all protocol information (segmentation, flow control, etc.) and forwards only the payload data (e.g. the ECU diagnostic response starting at the service ID and including all response parameters) to the diagnostic layer.

## Return Values

Error code

## Example

See DoIP_DataInd

```c
// This callback shall be called by an example TP layer
TPLayer_ReceivedData( long connectionHandle, byte data[])
{
  char ecuQualifier[20];
  TPLayerGetECUQualifierForHandle(connectionHandle, ecuQualifier);
  diag_DataInd(ecuQualifier, data, elcount(data));
}
```

## Availability

| Since Version |
|---|
