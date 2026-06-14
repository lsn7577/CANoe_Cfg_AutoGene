# SD_AddConsumer

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
long SD_AddConsumer(service svc, char[] name, dword isSimulated, serviceConsumerRef * newConsumer)
```

## Description

Adds a consumer endpoint to a service communication object. The new endpoint may be real and detected through some protocol messages, or it may be simulated to test reaction of a provider to dynamic endpoint changes.

## Return Values

0: Success

## Example

```c
SD_AddConsumer(MirrorAdjustment, "DiagConsole", 1, newConsumer);
```

## Availability

| Since Version |
|---|
