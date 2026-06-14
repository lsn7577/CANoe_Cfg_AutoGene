# consumedMethodRef

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
consumedMethodRef * <var>
```

## Description

References a consumed method endpoint, which means a specific combination of consumer and provider for a service function on consumer side.

## Example

```c
consumedMethodRef MirrorAdjustment.Adjust method;
method = MirrorAdjustment.consumerSide[CANoe,LeftMirror].Adjust;
method.CallAsync(-50, 0);
```

## Availability

| Since Version |
|---|

## Selectors

| Selector | Type | Access Limitation |
|---|---|---|
| Name Name of the consumed endpoint | char[] | Read only |
| Path Full path of the consumed endpoint (including namespaces) | char[] | Read only |
| ConsumerIndex Index of the consumer. Note that the index may change if consumers are added or removed. | dword | Read only |
| ProviderIndex Index of the provider. Note that the index may change if providers are added or removed. | dword | Read only |
| LatestCall Information about the latest call started at this endpoint. | struct | Read only |
| LatestReturn Information about the latest return received at this endpoint. | struct | Read only |
