# consumedFieldRef::AbstractIsFieldRequested

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
dword consumedFieldRef::AbstractIsFieldRequested()
```

## Description

Returns whether the specified field is currently requested (if abstract binding is used).

## Return Values

0: Field is not currently requested

## Example

```c
val = MirrorAdjustment.consumerSide[CANoe,LeftMirror].CurrentPosition.AbstractIsFieldRequested();
```

## Availability

| Since Version |
|---|
