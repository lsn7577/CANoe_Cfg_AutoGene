# Abstract_SubscribeEvent

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
long Abstract_SubscribeEvent(consumedEventRef * event)
```

## Description

Subscribes for a service event if abstract binding is used. Note that this is more low-level; usually its more convenient to call consumedEventRef::AbstractRequestEvent on the event.

## Return Values

0: Success

## Example

```c
Abstract_SubscribeEvent(MirrorAdjustment.consumerSide[0,0].Position);
```

## Availability

| Since Version |
|---|
