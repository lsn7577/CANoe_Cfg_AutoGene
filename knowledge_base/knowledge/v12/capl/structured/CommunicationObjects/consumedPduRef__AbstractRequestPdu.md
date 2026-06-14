# consumedPduRef::AbstractRequestPdu

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
int consumedPDURef::AbstractRequestPDU()
```

## Description

Requests the subscription of a specific service PDU if abstract binding is used: for the specified consumer from the specified provider. If the PDU is requested, it will be subscribed as soon as the provider is connected with the consumer.

## Return Values

0: Success

## Example

```c
MirrorAdjustment.consumerSide[CANoe,LeftMirror].StatusPDU.AbstractRequestPDU();
```

## Availability

| Since Version |
|---|
