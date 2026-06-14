# SCC_SetServiceDetailRequest

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
long SCC_SetServiceDetailRequest ( dword ServiceId )
```

## Description

Requests the vehicle to send a Service Detail Request during the ServiceDiscoveryRes or ServiceDetailRes callback. It is possible for multiple Service Detail Requests, or none at all, to be sent. If this function is not called, the vehicle skips this message.

This function must be called during a callback before a Service Detail Request may be sent, i.e. the callback for the messages Service Discovery Response or Service Detail Response.

## Return Values

0: Not successful

## Availability

| Since Version |
|---|
