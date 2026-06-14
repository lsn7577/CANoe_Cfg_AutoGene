# StandardFrameRate

> Category: `CAN` | Type: `function`

## Syntax

```c
long StandardFrameRate ()
CANx.StandardFrameRate
```

## Description

Returns the current rate of standard CAN messages on channel x.

Valid x values: 1…32

## Return Values

Current rate of standard CAN frames on channel x in messages per second.

## Example

```c
write ("Rate of standard frames on CAN1 = %d", CAN1.StandardFrameRate);
```

## Availability

| Since Version |
|---|
