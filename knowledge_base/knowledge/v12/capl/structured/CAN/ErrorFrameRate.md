# ErrorFrameRate

> Category: `CAN` | Type: `function`

## Syntax

```c
long ErrorFrameRate ()
CANx.ErrorFrameRate
```

## Description

Returns the current rate of CAN error messages of channel x.

Valid x values: 1…32

## Return Values

Current rate of CAN error messages on channel x in messages per second.

## Example

```c
write ("Rate of error messages on CAN1 = %d", CAN1.ErrorFrameRate);
```

## Availability

| Since Version |
|---|
