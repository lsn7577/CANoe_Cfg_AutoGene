# measuredServicePDURef

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
measuredServicePDURef * <var>
```

## Description

References a service PDU measurement point, which means measuring a specific connection between consumer and provider for a service PDU.

Not used for PDUs outside services, the data type of these is measuredPDURef.

## Example

```c
measuredServicePDURef MirrorAdjustment.StatusPDU pdu1;
pdu1 = MirrorAdjustment.measure[CANoe,LeftMirror].StatusPDU;
write("Latest x: %d", $pdu1.Position.x);
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
| SubscriptionState State of the PDU subscription: Unknown: the PDUsubscription was not observed yet Unsubscribed: the PDU is not subscribed Subscribed: the PDU is subscribed | enum | Read only |
