# SD_AnnounceProvider

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
long SD_AnnounceProvider(serviceProviderRef * provider)
```

## Description

Announces over the network that a service provider is running. You can pass either a provider endpoint, which will announce it generally (to a service registry or to all known consumers or by broadcast, depending on the binding protocol). Or you can pass a specific endpoint combination, which will announce it only to the given consumer endpoint.

Note that the provider will be automatically announced if you call ProvideService on the endpoint.

## Return Values

0: Success

## Example

```c
SD_AnnounceProvider(newProvider);
```

## Availability

| Since Version |
|---|
