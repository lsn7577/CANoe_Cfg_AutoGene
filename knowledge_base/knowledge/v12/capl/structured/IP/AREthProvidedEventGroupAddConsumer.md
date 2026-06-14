# AREthProvidedEventGroupAddConsumer

> Category: `IP` | Type: `function`

## Syntax

```c
long AREthProvidedEventGroupAddConsumer(dword pevgHandle, dword remoteIPv4Address, dword remoteUDPPort, dword remoteTCPPort);
```

## Description

Adds a consumer to a provided event group. Afterwards event/field notifications will be sent to this consumer.

## Return Values

0: The function was successfully executed

## Availability

| Since Version |
|---|
