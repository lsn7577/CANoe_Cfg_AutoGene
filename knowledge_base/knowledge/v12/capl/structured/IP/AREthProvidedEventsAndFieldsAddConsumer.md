# AREthProvidedEventsAndFieldsAddConsumer

> Category: `IP` | Type: `function`

## Syntax

```c
long AREthProvidedEventsAndFieldsAddConsumer(dword psiHandle, dword remoteIPv4Address, dword remoteUDPPort, dword remoteTCPPort);
```

## Description

Adds a consumer to a provided service instance. Afterwards all event/field notifications belonging to this service instance will be sent to this consumer.

## Return Values

0: The function was successfully executed

## Availability

| Since Version |
|---|
