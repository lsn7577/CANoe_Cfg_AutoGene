# SomeIpProvidedEventAddConsumer

> Category: `IP` | Type: `function`

## Syntax

```c
long SomeIpProvidedEventAddConsumer(dword pevHandle, dword remoteIPv4Address, dword remoteUDPPort, dword remoteTCPPort);
```

## Description

Adds a consumer to a provided event. Afterwards the event notifications will be sent to this consumer.

## Return Values

0: The function was successfully executed

## Availability

| Since Version |
|---|
