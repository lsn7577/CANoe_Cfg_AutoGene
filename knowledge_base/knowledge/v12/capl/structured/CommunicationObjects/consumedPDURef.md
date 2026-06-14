# consumedPDURef

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
consumedPDURef * <var>
```

## Description

References a consumed PDU endpoint, which means a specific combination of consumer and provider for a service PDU on consumer side.

## Example

```c
consumedPDURef MirrorAdjustment.StatusPDU pdu1;
pdu1 = MirrorAdjustment.consumerSide[CANoe,LeftMirror].StatusPDU;
pdu1.AbstractRequestPDU();
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
| SubscriptionState State of the PDU subscription: Unavailable: there’s no connection between consumer and provider, the PDU cannot be subscribed. Available: the PDU can be subscribed, but currently is not subscribed. Subscribed: the PDU is subscribed. | enum | Read only |
| <SignalName> Accesses the specified signal on the PDU. | <Data type of the signal> |  |
