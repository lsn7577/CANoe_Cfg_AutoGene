# consumedEventRef

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
consumedEventRef * <var>
```

## Description

References a consumed event endpoint, which means a specific combination of consumer and provider for a service event on consumer side.

## Example

```c
consumedEventRef long ev1;
ev1 = MirrorAdjustment.consumerSide[CANoe,LeftMirror].CurrentPosition;
ev1.AbstractRequestEvent();
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
| SubscriptionState State of the event subscription: Unavailable: there’s no connection between consumer and provider, the event cannot be subscribed. Available: the event can be subscribed, but currently is not subscribed. Subscribed: the event is subscribed. | enum | Read only |
