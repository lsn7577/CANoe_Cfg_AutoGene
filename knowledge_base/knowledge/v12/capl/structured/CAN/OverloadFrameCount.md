# OverloadFrameCount

> Category: `CAN` | Type: `function`

## Syntax

```c
long OverloadFrameCount ()
CANx.OverloadFrameCount
```

## Description

Returns the number of CAN overload frames on channel x since start of measurement.

Valid x values: 1 ... 32

## Return Values

Number of CAN overload frames on channel x since start of measurement.

## Example

```c
write ("Number of overload frames on CAN1 = %d", CAN1.OverloadFrameCount);
```

## Availability

| Since Version |
|---|
