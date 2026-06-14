# measuredServiceRef

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
measuredServiceRef * <var>
```

## Description

References a service measurement point, which means measuring a specific connection between consumer and provider for a service.

## Example

```c
measuredServiceRef MirrorAdjustment svc1;
svc1 = MirrorAdjustment.measure[CANoe,LeftMirror];
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
