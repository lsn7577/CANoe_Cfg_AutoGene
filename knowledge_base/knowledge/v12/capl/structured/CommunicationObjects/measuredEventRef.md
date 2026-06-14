# measuredEventRef

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
measuredEventRef * <var>
```

## Description

References an event measurement point, which means measuring a specific connection between consumer and provider for a service event.

## Example

```c
measuredEventRef MirrorAdjustment.Position event;
event = MirrorAdjustment.measure[CANoe,LeftMirror].Position;
write("Latest x: %d", $event.x);
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
| SubscriptionState State of the event subscription: Unknown: the event subscription was not observed yet Unsubscribed: the event is not subscribed Subscribed: the event is subscribed | enum | Read only |
