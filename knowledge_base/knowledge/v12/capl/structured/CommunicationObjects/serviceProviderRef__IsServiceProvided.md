# serviceProviderRef::IsServiceProvided

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
dword serviceProviderRef::IsServiceProvided()
```

## Description

Returns whether the service is currently provided at the endpoint.

## Return Values

0: Service is not currently provided

## Example

```c
val = MirrorAdjustment.providerSide[LeftMirror].IsServiceProvided();
```

## Availability

| Since Version |
|---|
