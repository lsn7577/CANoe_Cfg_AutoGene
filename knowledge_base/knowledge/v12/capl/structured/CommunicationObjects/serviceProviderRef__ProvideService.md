# serviceProviderRef::ProvideService

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
int serviceProviderRef::ProvideService()
```

## Description

Provides the service at the endpoint. This means that the binding will announce the service either by broadcast or at a central registry (depending on the binding) and that connection requests from consumers will be accepted.

## Return Values

0: Success

## Example

```c
MirrorAdjustment.providerSide[LeftMirror].ProvideService();
```

## Availability

| Since Version |
|---|
