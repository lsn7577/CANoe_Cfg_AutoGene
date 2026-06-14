# ExtendedFrameCount

> Category: `CAN` | Type: `function`

## Syntax

```c
long ExtendedFrameCount ()
CANx.ExtendedFrameCount
```

## Description

Returns the number of extended CAN messages on channel x since start of measurement.

Valid x values: 1…32

## Return Values

Number of extended CAN messages on channel x since start of measurement

## Example

```c
write ("Number of extended frames on CAN1 = 
 %d", CAN1.ExtendedFrameCount);
```

## Availability

| Since Version |
|---|
