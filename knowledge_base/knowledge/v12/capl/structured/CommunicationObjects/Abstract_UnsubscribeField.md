# Abstract_UnsubscribeField

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
long Abstract_UnsubscribeField(consumedFieldRef * field)
```

## Description

Unsubscribes for a service field if abstract binding is used. Note that this is more low-level; usually its more convenient to call consumedFieldRef::AbstractReleaseField on the field.

## Return Values

0: Success

## Example

```c
Abstract_UnsubscribeField(MirrorAdjustment.consumerSide[0,0].CurrentPosition);
```

## Availability

| Since Version |
|---|
