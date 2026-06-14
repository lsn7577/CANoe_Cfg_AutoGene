# ErrorFrameCount

> Category: `CAN` | Type: `function`

## Syntax

```c
long ErrorFrameCount ()
CANx.ErrorFrameCount
```

## Description

Returns the number of Error Frames on channel x since start of measurement.

Valid x values: 1…32

## Return Values

Number of Error Frames on channel x since start of measurement.

## Example

```c
write ("Number of error frames on CAN1 = %d", 
 CAN1.ErrorFrameCount);
```

## Availability

| Since Version |
|---|
