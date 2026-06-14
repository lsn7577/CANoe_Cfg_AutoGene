# _diag_ConfigureChannel

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void _Diag_ConfigureChannel(char target[]);
```

## Description

This callback function will be called when a diagnostic request has to be sent to a new target. The CAPL node can configure the transport protocol, e.g. set CAN IDs for sending and receiving.

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

| Since Version |
|---|
