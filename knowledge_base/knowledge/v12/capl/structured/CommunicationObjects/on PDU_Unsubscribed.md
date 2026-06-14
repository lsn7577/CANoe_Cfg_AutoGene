# on PDU_Unsubscribed

> Category: `CommunicationObjects` | Type: `event`

## Syntax

```c
on PDU_Unsubscribed <PDU>
```

## Description

The event procedure is called at the provider when a PDU is unsubscribed by a consumer.

## Example

```c
on PDU_Unsubscribed Mirrors::MirrorAdjustment[LeftMirror].StatusPdu
{
  write("PDU unsubscribed by %s", this.consumer.Name);
}
```

## Availability

| Since Version |
|---|

## Selectors

| pduConsumerRef * | ../Objects/CAPLfunctionPDUConsumerRef.htm |
|---|---|
