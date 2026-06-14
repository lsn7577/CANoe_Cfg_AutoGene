# Abstract_UnsubscribeEvent

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
long Abstract_UnsubscribeEvent(consumedEventRef * event)
```

## Description

Unsubscribes for a service event if abstract binding is used. Note that this is more low-level; usually its more convenient to call consumedEventRef::AbstractReleaseEvent on the event.

## Return Values

0: Success

## Example

```c
Abstract_UnsubscribeEvent(MirrorAdjustment.consumerSide[0,0].Position);
```

## Availability

| Since Version |
|---|
