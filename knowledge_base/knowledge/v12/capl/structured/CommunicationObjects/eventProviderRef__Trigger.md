# eventProviderRef::Trigger

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
void eventProviderRef::Trigger()
```

## Description

Triggers the specified event. This leads to a transmission of the event to all subscribed consumers without changing the current event value. The method is particularly useful for events which do not carry a value (have data type void).

## Return Values

—

## Example

```c
MirrorAdjustment.providerSide[LeftMirror].CurrentPosition.Trigger();
```

## Availability

| Since Version |
|---|
