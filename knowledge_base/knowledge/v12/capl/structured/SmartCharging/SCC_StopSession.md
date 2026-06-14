# SCC_StopSession

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
long SCC_StopSession ( dword CloseTcpConnection ) // form 1
```

## Description

The function stops a connection immediately. If it is used within a message callback, a response to the message is not sent.

## Return Values

0: Not successful

## Availability

| Since Version |
|---|
