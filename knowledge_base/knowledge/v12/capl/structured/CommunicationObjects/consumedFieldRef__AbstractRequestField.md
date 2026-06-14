# consumedFieldRef::AbstractRequestField

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
int consumedFieldRef::AbstractRequestField()
```

## Description

Requests the subscription of a specific service field if abstract binding is used: for the specified consumer from the specified provider. If the field is requested, it will be subscribed as soon as the provider is connected with the consumer.

## Return Values

0: Success

## Example

```c
MirrorAdjustment.consumerSide[CANoe,LeftMirror].CurrentPosition.AbstractRequestField();
```

## Availability

| Since Version |
|---|
