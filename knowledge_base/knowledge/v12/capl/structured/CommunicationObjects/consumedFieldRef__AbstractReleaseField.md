# consumedFieldRef::AbstractReleaseField

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
int consumedFieldRef::AbstractReleaseField()
```

## Description

Releases the subscription of a specific service field if abstract binding is used: for the specified consumer from the specified provider. If the field is released, it will be unsubscribed and not automatically re-subscribed.

## Return Values

0: Success

## Example

```c
MirrorAdjustment.consumerSide[CANoe,LeftMirror].CurrentPosition.AbstractReleaseField();
```

## Availability

| Since Version |
|---|
