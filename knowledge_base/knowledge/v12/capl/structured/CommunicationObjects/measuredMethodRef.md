# measuredMethodRef

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
measuredMethodRef * <var>
```

## Description

References a method measurement point, which means measuring a specific connection between consumer and provider for a service function.

## Example

```c
measuredMethodRef MirrorAdjustment.Adjust method;
method = MirrorAdjustment.measure[CANoe,LeftMirror].Adjust;
write("Latest x: %d", method.LatestCall.x);
```

## Availability

| Since Version |
|---|

## Selectors

| Selector | Type | Access Limitation |
|---|---|---|
| Name Name of the measurement endpoint | char[] | Read only |
| Path Full path of the measurement endpoint (including namespaces) | char[] | Read only |
| ConsumerIndex Index of the consumer. Note that the index may change if consumers are added or removed. | dword | Read only |
| ProviderIndex Index of the provider. Note that the index may change if providers are added or removed. | dword | Read only |
| measuredService The measurement point at the service. | measuredServiceRef * | Read only |
| LatestCall Information about the latest call measured at this point. | struct | Read only |
| LatestReturn Information about the latest return measured at this point. | struct | Read only |
