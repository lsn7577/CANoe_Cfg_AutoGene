# SOMEIP_UnsubscribeEventGroup

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
long SOMEIP_UnsubscribeEventGroup(consumedEventGroupRef * eventGroup)
```

## Description

Unsubscribes for a service event group if SOME/IP binding is used. Note that this is more low-level; usually its more convenient to call consumedEventGroupRef::SOMEIPReleaseEventGroup on the event group.

## Return Values

0: Success

## Example

```c
SOMEIP_UnsubscribeEventGroup(MirrorAdjustment.consumerSide[0,0].AllEvents);
```

## Availability

| Since Version |
|---|
