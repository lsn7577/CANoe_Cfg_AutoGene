# _diag_SetupChannelRequest, _diag_SetupChannelReq

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void _diag_SetupChannelReq (); // form 1
```

## Description

With this function the CAPL program of a tester implementation will be requested to open a channel to the ECU. After opening the channel the CAPL program can call the function diag_SetupChannelCon.

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

| Since Version |
|---|
