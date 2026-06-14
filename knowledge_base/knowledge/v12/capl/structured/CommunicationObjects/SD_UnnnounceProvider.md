# SD_UnnnounceProvider

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
long SD_UnannounceProvider(serviceProviderRef * provider)
```

## Description

Announces over the network that a service provider is no longer running. This may be necessary for some bindings where a central service registry is used.

Note that the service provider will be unannounced automatically if you call ReleaseService on the endpoint.

## Return Values

0: Success

## Example

```c
SD_UnnnounceProvider(myProvider);
```

## Availability

| Since Version |
|---|
