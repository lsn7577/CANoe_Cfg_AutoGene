# consumedEventRef::AbstractReleaseEvent

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
int consumedEventRef::AbstractReleaseEvent()
```

## Description

Releases the subscription of a specific service event if abstract binding is used: for the specified consumer from the specified provider. If the event is released, it will be unsubscribed and not automatically re-subscribed.

## Return Values

0: Success

## Example

```c
MirrorAdjustment.consumerSide[CANoe,LeftMirror].CurrentPosition.AbstractReleaseEvent();
```

## Availability

| Since Version |
|---|
