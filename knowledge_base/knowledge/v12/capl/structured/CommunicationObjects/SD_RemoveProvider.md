# SD_RemoveProvider

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
void SD_RemoveProvider(serviceProviderRef * provider)
```

## Description

Removes a provider endpoint from a service. You may call this to react to timeouts, or unannouncements from a real provider, or to remove a simulated provider endpoint.

## Return Values

0: Success

## Example

```c
SD_RemoveProvider(newProvider);
```

## Availability

| Since Version |
|---|
