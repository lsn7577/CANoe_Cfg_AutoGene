# on Abstract_EventSubscribed

> Category: `CommunicationObjects` | Type: `event`

## Syntax

```c
on Abstract_EventSubscribed <Event>
```

## Description

The event procedure is called at the provider when an event is subscribed by a consumer and abstract binding is used.

## Example

```c
on Abstract_EventSubscribed MirrorAdjustment[LeftMirror].CurrentPosition
{
  // send the event to the consumer on subscription
  providedEventRef long ev1;
  ev1 = MirrorAdjustment.providerSide[this.consumer.ConsumerIndex,LeftMirror].CurrentPosition;
  ev1.Trigger();
}
```

## Availability

| Since Version |
|---|

## Selectors

| eventConsumerRef * | ../Objects/CAPLfunctionEventConsumerRef.htm |
|---|---|
