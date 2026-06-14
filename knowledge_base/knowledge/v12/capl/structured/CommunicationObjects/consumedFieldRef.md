# consumedFieldRef

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
consumedFieldRef * <var>
```

## Description

References a consumed field endpoint, which means a specific combination of consumer and provider for a service field on consumer side.

## Example

```c
consumedFieldRef long field1;
field1 = MirrorAdjustment.consumerSide[CANoe,LeftMirror].CurrentPosition;
field1.AbstractRequestField();
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
| SubscriptionState State of the field subscription: Unavailable: there’s no connection between consumer and provider, the field cannot be subscribed. Available: the field can be subscribed, but currently is not subscribed. Subscribed: the field is subscribed. | enum | Read only |
