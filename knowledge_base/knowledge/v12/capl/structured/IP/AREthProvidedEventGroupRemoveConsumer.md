# AREthProvidedEventGroupRemoveConsumer

> Category: `IP` | Type: `function`

## Syntax

```c
long AREthProvidedEventGroupRemoveConsumer(dword pevgHandle, dword remoteIPv4Address, dword remoteUDPPort, dword remoteTCPPort);
```

## Description

Removes a consumer from a provided event group. Afterwards event/field notifications will not be sent to this consumer anymore.

## Return Values

0: The function was successfully executed

## Availability

| Since Version |
|---|
