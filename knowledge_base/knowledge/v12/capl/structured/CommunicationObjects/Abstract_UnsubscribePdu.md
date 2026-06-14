# Abstract_UnsubscribePdu

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
long Abstract_UnsubscribePDU(consumedPDURef * pdu)
```

## Description

Unsubscribes for a service PDU if abstract binding is used. Note that this is more low-level; usually its more convenient to call consumedPduRef::AbstractReleasePdu on the PDU.

## Return Values

0: Success

## Example

```c
Abstract_UnsubscribePDU(MirrorAdjustment.consumerSide[0,0].PositionPDU);
```

## Availability

| Since Version |
|---|
