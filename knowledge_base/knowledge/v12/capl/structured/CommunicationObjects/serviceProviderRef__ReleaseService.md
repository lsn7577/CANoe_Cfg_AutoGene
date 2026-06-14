# serviceProviderRef::ReleaseService

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
int serviceProviderRef::ReleaseService()
```

## Description

Releases the service at the endpoint. This means that the binding will stop announcing the service or unregister it from a central registry (depending on the binding) and that connection requests from consumers will be denied.

## Return Values

0: Success

## Example

```c
MirrorAdjustment.providerSide[LeftMirror].ReleaseService();
```

## Availability

| Since Version |
|---|
