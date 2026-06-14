# SD_RemoveConsumer

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
void SD_RemoveConsumer(serviceConsumerRef * consumer)
```

## Description

Removes a consumer endpoint from a service. You may call this to react to timeouts, or unannouncements from a real consumer, or to remove a simulated consumer endpoint.

## Return Values

0: Success

## Example

```c
SD_RemoveConsumer(newConsumer);
```

## Availability

| Since Version |
|---|
