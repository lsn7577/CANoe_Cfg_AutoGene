# pduConsumerRef

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
pduConsumerRef * <var>
```

## Description

References a PDU consumer endpoint.

## Example

```c
pduConsumerRef MirrorAdjustment.StatusPDU pdu1;
pdu1 = MirrorAdjustment.consumerSide[CANoe].StatusPDU;
```

## Availability

| Since Version |
|---|

## Selectors

| Selector | Type | Access Limitation |
|---|---|---|
| Name Name of the consumer endpoint | char[] | Read only |
| Path Full path of the consumer endpoint (including namespaces) | char[] | Read only |
| ConsumerIndex Index of the consumer. Note that the index may change if consumers are added or removed. | dword | Read only |
| ServiceIndex Reference to the consumer of the service containing the PDU. | serviceConsumerRef * | Read only |
