# consumedEventGroupRef::SOMEIPRequestEventGroup

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
int consumedEventGroupRef::SOMEIPRequestEventGroup()
```

## Description

Requests the subscription of a specific event group: for the specified consumer from the specified provider. If the event group is requested, it will be subscribed as soon as the provider is connected with the consumer.

## Return Values

0: Success

## Example

```c
MirrorAdjustment.consumerSide[CANoe,LeftMirror].AllEvents.SOMEIPRequestEventGroup();
```

## Availability

| Since Version |
|---|
