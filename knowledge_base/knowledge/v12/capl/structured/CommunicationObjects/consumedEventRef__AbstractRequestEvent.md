# consumedEventRef::AbstractRequestEvent

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
int consumedEventRef::AbstractRequestEvent()
```

## Description

Requests the subscription of a specific service event if abstract binding is used: for the specified consumer from the specified provider. If the event is requested, it will be subscribed as soon as the provider is connected with the consumer.

## Return Values

0: Success

## Example

```c
MirrorAdjustment.consumerSide[CANoe,LeftMirror].CurrentPosition.AbstractRequestEvent();
```

## Availability

| Since Version |
|---|
