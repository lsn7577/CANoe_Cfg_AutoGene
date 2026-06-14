# _diag_DisconnectRequest

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void _Diag_DisconnectRequest(char target[]);
```

## Description

The diagnostic communication channel to the target with the given qualifier shall be closed. For connectionless transport protocols, diag_ClosedChannelInd can be called immediately. Otherwise the completion of the channel closing must be indicated when the TP layer indicates it.

## Return Values

—

## Availability

| Since Version |
|---|
