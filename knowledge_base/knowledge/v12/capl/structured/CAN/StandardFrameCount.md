# StandardFrameCount

> Category: `CAN` | Type: `function`

## Syntax

```c
long StandardFrameCount ()
CANx.StandardFrameCount
```

## Description

Returns the number of standard CAN messages on channel x since start of measurement.

Valid x values: 1…32

## Return Values

Number of standard CAN messages on channel x since start of measurement.

## Example

```c
write ("Number of standard frames on CAN1 = %d", CAN1.StandardFrameCount);
```

## Availability

| Since Version |
|---|
