# SD_Disconnect

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
void SD_Disconnect(providedServiceRef * providedService)
```

## Description

Disconnects a service provider and consumer. You can call the function from both the provider and the consumer side.

Note that you need this function only when you implement service discovery yourself. In most cases, there’s an internal CANoe model for simulated endpoints which handles the protocol.

## Return Values

—

## Example

```c
SD_Disconnect(consumedService);
```

## Availability

| Since Version |
|---|
