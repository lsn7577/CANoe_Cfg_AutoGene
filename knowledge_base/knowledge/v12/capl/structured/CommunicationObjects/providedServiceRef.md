# providedServiceRef

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
providedServiceRef * <var>
```

## Description

References a provided service endpoint, which means a specific combination of consumer and provider for a service on provider side.

## Example

```c
providedServiceRef MirrorAdjustment service1;
service1 = MirrorAdjustment.providerSide[CANoe,LeftMirror];
write("State: %d", $service1.ConnectionState);
```

## Availability

| Since Version |
|---|

## Selectors

| Selector | Type | Access Limitation |
|---|---|---|
| Name Name of the provided endpoint | char[] | Read only |
| Path Full path of the provided endpoint (including namespaces) | char[] | Read only |
| ConsumerIndex Index of the consumer. Note that the index may change if consumers are added or removed. | dword | Read only |
| ProviderIndex Index of the provider. Note that the index may change if providers are added or removed. | dword | Read only |
| ConnectionState State of the connection between consumer and provider. Unavailable: consumer and provider cannot currently connect. Connectable: consumer and provider can connect, but are not connected. Connected: consumer and provider are connected. | enum | Read only |
