# Abstract_SubscribeField

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
long Abstract_SubscribeField(consumedFieldRef * field)
```

## Description

Subscribes for a service field if abstract binding is used. Note that this is more low-level; usually its more convenient to call consumedFieldRef::AbstractRequestField on the field.

## Return Values

0 : Success

## Example

```c
Abstract_SubscribeField(MirrorAdjustment.consumerSide[0,0].CurrentPosition);
```

## Availability

| Since Version |
|---|
