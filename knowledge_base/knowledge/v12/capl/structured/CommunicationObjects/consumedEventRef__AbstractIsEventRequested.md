# consumedEventRef::AbstractIsEventRequested

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
dword consumedEventRef::AbstractIsEventRequested()
```

## Description

Returns whether the specified event is currently requested (if abstract binding is used).

## Return Values

0: Event is not currently requested

## Example

```c
val = MirrorAdjustment.consumerSide[CANoe,LeftMirror].CurrentPosition.AbstractIsEventRequested();
```

## Availability

| Since Version |
|---|
