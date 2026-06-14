# consumedServiceRef

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
consumedServiceRef * <var>
```

## Description

References a consumed service endpoint, which means a specific combination of consumer and provider for a service on consumer side.

## Example

```c
consumedServiceRef MirrorAdjustment service;
service = MirrorAdjustment.consumerSide[CANoe,LeftMirror];
service.RequestService();
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
| ConnectionState State of the connection between consumer and provider: Unavailable: service provider is currently not available, cannot connect Connectable: consumer and provider can connect, but are not connected Available: consumer and provider are connected, the service is available. | enum | Read only |
