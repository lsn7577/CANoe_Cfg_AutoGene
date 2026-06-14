# _diag_SendFunctional

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void _diag_SendFunctional (BYTE data[]);
```

## Description

With this CAPL callback function CANoe triggers the CAPL program to send a functional diagnostic request.

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

| Since Version |
|---|
