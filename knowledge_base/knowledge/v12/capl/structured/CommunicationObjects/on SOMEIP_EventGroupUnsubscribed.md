# on SOMEIP_EventGroupUnsubscribed

> Category: `CommunicationObjects` | Type: `event`

## Syntax

```c
On SOMEIP_EventGroupUnsubscribed <EventGroup>
```

## Description

The event procedure is called at the provider when an event group is unsubscribed by a consumer and SOME/IP binding is used.

## Example

```c
on SOMEIP_EventGroupUnsubscribed MirrorAdjustment[LeftMirror].AllEvents
{
  write("Event group unsubscribed by %s", this.consumer.Name);
}
```

## Availability

| Since Version |
|---|

## Selectors

| serviceConsumerRef * | ../Objects/CAPLfunctionServiceConsumerRef.htm |
|---|---|
