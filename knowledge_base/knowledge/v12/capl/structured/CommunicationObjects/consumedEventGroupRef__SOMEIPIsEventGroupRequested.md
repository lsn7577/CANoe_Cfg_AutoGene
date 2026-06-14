# consumedEventGroupRef::SOMEIPIsEventGroupRequested

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
dword consumedEventGroupRef::SOMEIPIsEventGroupRequested()
```

## Description

Returns whether the specified event group is currently requested.

## Return Values

0: Event group is not currently requested

## Example

```c
val = MirrorAdjustment.consumerSide[CANoe,LeftMirror].AllEvents.SOMEIPIsEventGroupRequested();
```

## Availability

| Since Version |
|---|
