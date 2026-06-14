# diag_ClosedChannelInd

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diag_ClosedChannelInd (); // form 1
```

## Description

This function communicates to CANoe that the communication channel is not longer available, e.g. the tester closed the channel or a non reparable error occurred.

The CAPL program first has to call diag_SetupChannelCon before further data can be sent.

## Return Values

Error code

## Example

```c
// This callback shall be called by an example TP layer
	TPLayer_ClosedChannel( long connectionHandle)
{
   char ecuQualifier[20];
  TPLayerGetECUQualifierForHandle(connectionHandle, ecuQualifier);
  diag_ClosedChannelInd(ecuQualifier);
}
```

## Availability

| Since Version |
|---|
