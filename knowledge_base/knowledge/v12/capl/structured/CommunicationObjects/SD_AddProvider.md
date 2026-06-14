# SD_AddProvider

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
long SD_AddProvider(service svc, char[] name, dword isSimulated, serviceProviderRef * newProvider)
```

## Description

Adds a provider endpoint to a service communication object. The new endpoint may be real and detected through some protocol messages, or it may be simulated to test reaction of a consumer to dynamic endpoint changes.

## Return Values

0: Success

## Example

```c
SD_AddProvider(MirrorAdjustment, "RearMirror", 1, newProvider);
```

## Availability

| Since Version |
|---|
