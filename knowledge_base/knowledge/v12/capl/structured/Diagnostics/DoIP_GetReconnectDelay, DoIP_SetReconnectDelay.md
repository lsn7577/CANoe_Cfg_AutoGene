# DoIP_GetReconnectDelay, DoIP_SetReconnectDelay

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void DoIP_SetReconnectDelay(dword reconnectDelay_ms);
```

## Description

Sets or returns the delay started by the tester when the ECU closes the TCP connection. After the configured time the tester attempts at first to re-open the TCP connection and afterwards to re-establish the routing activation.

## Return Values

Form 1: —Form 2: TCP reconnection delay

## Availability

| Since Version |
|---|
