# eventProviderRef

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
eventProviderRef * <var>
```

## Description

References an event provider endpoint.

## Example

```c
eventProviderRef long event1;
event1 = MirrorAdjustment.providerSide[LeftMirror].CurrentPosition;
$event1 = newValue;
```

## Availability

| Since Version |
|---|

## Selectors

| Selector | Type | Access Limitation |
|---|---|---|
| Name Name of the provider endpoint | char[] | Read only |
| Path Full path of the provider endpoint (including namespaces) | char[] | Read only |
| ProviderIndex Index of the provider. Note that the index may change if providers are added or removed. | dword | Read only |
| ServiceProvider Reference to the provider of the service containing the event. | serviceProviderRef* | Read only |
