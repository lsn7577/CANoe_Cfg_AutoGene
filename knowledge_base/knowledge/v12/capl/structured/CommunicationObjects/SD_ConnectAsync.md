# SD_ConnectAsync

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
void SD_ConnectAsync(providedServiceRef * providedService)
```

## Description

Requests that a connection will be established between a service provider and a service consumer. The connection will be established asynchronously, i.e. after the call it will in the general case not be available immediately. You can react to the establishment of the connection with an on SD_connection_established (or on SD_connection_failed) handler. You can call the function from both the provider and the consumer side.

Note that you need this function only when you implement service discovery yourself. In most cases, there’s an internal CANoe model for simulated endpoints which handles the protocol.

## Return Values

—

## Example

```c
SD_ConnectAsync(consumedService);
```

## Availability

| Since Version |
|---|
