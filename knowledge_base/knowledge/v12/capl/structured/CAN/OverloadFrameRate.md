# OverloadFrameRate

> Category: `CAN` | Type: `function`

## Syntax

```c
long OverloadFrameRate ()
CANx.OverloadFrameRate
```

## Description

Returns the current rate of CAN overload frames on channel x.

Valid x values: 1 ... 32

## Return Values

Current rate of CAN overload frames on channel x in messages per second.

## Example

```c
write ("Rate of overload frames on CAN1 = %d", CAN1.OverloadFrameRate);
```

## Availability

| Since Version |
|---|
