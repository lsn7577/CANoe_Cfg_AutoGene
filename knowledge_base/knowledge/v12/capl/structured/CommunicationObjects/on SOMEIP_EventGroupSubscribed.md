# on SOMEIP_EventGroupSubscribed

> Category: `CommunicationObjects` | Type: `event`

## Syntax

```c
on SOMEIP_EventGroupSubscribed <EventGroup>
```

## Description

The event procedure is called at the provider when an event group is subscribed by a consumer and SOME/IP binding is used.

## Example

```c
on SOMEIP_EventGroupSubscribed MirrorAdjustment[LeftMirror].AllEvents
{
  write("Event group subscribed by %s", this.consumer.Name);
}
```

## Availability

| Since Version |
|---|

## Selectors

| serviceConsumerRef * | ../Objects/CAPLfunctionServiceConsumerRef.htm |
|---|---|
