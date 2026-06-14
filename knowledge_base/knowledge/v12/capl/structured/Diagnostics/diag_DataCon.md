# diag_DataCon

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void diag_DataCon (long count); // form 1
```

## Description

Tells the diagnostic layer, via the count parameter, how many bytes of data were transmitted successfully.

This function is typically called within a transport layer callback. Once the diagnostic layer has initiated the transmission of a message via _diag_DataRequest and the transport layer has sent this message in its entirety, using several message segments if needed, the diagnostic layer transport layer uses this function to indicate that the message was sent successfully.

## Return Values

Error code

## Example

See DoIP_DataCon

```c
// This callback shall be called by an example TP layer
TPLayer_SendConfirmation( long connectionHandle, long count)
{
  char ecuQualifier[20];
  TPLayerGetECUQualifierForHandle(connectionHandle, ecuQualifier);
  diag_DataCon(ecuQualifier, count);
}
```

## Availability

| Since Version |
|---|
