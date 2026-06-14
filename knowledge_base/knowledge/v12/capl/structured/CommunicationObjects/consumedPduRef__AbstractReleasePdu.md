# consumedPduRef::AbstractReleasePdu

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
int consumedPDURef::AbstractReleasePDU()
```

## Description

Releases the subscription of a specific service PDU if abstract binding is used: for the specified consumer from the specified provider. If the PDU is released, it will be unsubscribed and not automatically re-subscribed.

## Return Values

0: Success

## Example

```c
MirrorAdjustment.consumerSide[CANoe,LeftMirror].StatusPDU.AbstractReleasePDU();
```

## Availability

| Since Version |
|---|
