# Abstract_SubscribePdu

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
long Abstract_SubscribePDU(consumedPDURef * pdu)
```

## Description

Subscribes for a service PDU if abstract binding is used. Note that this is more low-level; usually its more convenient to call consumedPduRef::AbstractRequestPdu on the PDU.

## Return Values

0: Success

## Example

```c
Abstract_SubscribePDU(MirrorAdjustment.consumerSide[0,0].PositionPDU);
```

## Availability

| Since Version |
|---|
