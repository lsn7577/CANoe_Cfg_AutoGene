# on Abstract_EventUnsubscribed

> Category: `CommunicationObjects` | Type: `event`

## Syntax

```c
on Abstract_EventUnsubscribed <Event>
```

## Description

The event procedure is called at the provider when an event is unsubscribed by a consumer and abstract binding is used.

## Example

```c
on Abstract_EventUnsubscribed MirrorAdjustment[LeftMirror].CurrentPosition
{
  write("Event unsubscribed by %s", this.consumer.Name);
}
```

## Availability

| Since Version |
|---|

## Selectors

| eventConsumerRef * | ../Objects/CAPLfunctionEventConsumerRef.htm |
|---|---|
