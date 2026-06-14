# on PDU_Subscribed

> Category: `CommunicationObjects` | Type: `event`

## Syntax

```c
on PDU_Subscribed <PDU>
```

## Description

The event procedure is called at the provider when a PDU is subscribed by a consumer.

## Example

```c
on PDU_Subscribed Mirrors::MirrorAdjustment[LeftMirror].StatusPdu
{
  write("PDU subscribed by %s", this.consumer.Name);
}
```

## Availability

| Since Version |
|---|

## Selectors

| pduConsumerRef * | ../Objects/CAPLfunctionPDUConsumerRef.htm |
|---|---|
