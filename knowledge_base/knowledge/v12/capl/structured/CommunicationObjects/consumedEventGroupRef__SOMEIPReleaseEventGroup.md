# consumedEventGroupRef::SOMEIPReleaseEventGroup

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
int consumedEventGroupRef::SOMEIPReleaseEventGroup()
```

## Description

Releases the subscription of a specific event group: for the specified consumer from the specified provider. If the event group is released, it will be unsubscribed and not automatically re-subscribed.

## Return Values

0: Success

## Example

```c
MirrorAdjustment.consumerSide[CANoe,LeftMirror].AllEvents.SOMEIPReleaseEventGroup();
```

## Availability

| Since Version |
|---|
