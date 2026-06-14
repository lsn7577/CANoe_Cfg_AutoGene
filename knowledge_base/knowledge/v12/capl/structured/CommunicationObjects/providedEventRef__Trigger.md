# providedEventRef::Trigger

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
void providedEventRef::Trigger()
```

## Description

Triggers the specified event. This leads to a transmission of the event to the specified consumer (if the consumer is subscribed) without changing the current event value. The method is particularly useful for events which do not carry a value (have data type void).

## Return Values

—

## Example

```c
MirrorAdjustment.providerSide[CANoe,LeftMirror].CurrentPosition.Trigger();
```

## Availability

| Since Version |
|---|
