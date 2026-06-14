# SOMEIP_SubscribeEventGroup

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
long SOMEIP_SubscribeEventGroup(consumedEventGroupRef * eventGroup)
```

## Description

Subscribes for a service event group if SOME/IP binding is used. Note that this is more low-level; usually its more convenient to call consumedEventGroupRef::SOMEIPRequestEventGroup on the event group.

## Return Values

0: Success

## Example

```c
SOMEIP_SubscribeEventGroup(MirrorAdjustment.consumerSide[0,0].AllEvents);
```

## Availability

| Since Version |
|---|
