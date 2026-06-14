# diag_SetupChannelCon

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diag_SetupChannelCon ();
```

## Description

This function communicates to CANoe, that a communication channel is available to the communication partner and data can be sent.

For connectionless transport protocols this function can be called out of the callback _diag_SetupChannelReq.

## Return Values

Error code

## Availability

| Since Version |
|---|
