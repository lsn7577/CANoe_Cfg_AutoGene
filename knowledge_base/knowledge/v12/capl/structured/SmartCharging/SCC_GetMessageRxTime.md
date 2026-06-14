# SCC_GetMessageRxTime

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
qword SCC_GetMessageRxTime ( ) // form 1
```

## Description

Queries the CANoe internal timestamp of the message receipt event, i.e. the CANoe simulation time, via references. The function is available for all kinds of message callbacks.

## Return Values

Timestamp in nanoseconds

## Availability

| Since Version |
|---|
