# measuredFieldRef

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
measuredFieldRef * <var>
```

## Description

References a field measurement point, which means measuring a specific connection between consumer and provider for a service field.

## Example

```c
measuredFieldRef MirrorAdjustment.Position field;
field = MirrorAdjustment.measure[CANoe,LeftMirror].Position;
write("Latest x: %d", $field.x);
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
| SubscriptionState State of the field subscription: Unknown: the field subscription was not observed yet Unsubscribed: the field is not subscribed Subscribed: the field is subscribed | enum | Read only |
