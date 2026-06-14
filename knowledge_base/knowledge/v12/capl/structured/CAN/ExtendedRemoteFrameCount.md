# ExtendedRemoteFrameCount

> Category: `CAN` | Type: `function`

## Syntax

```c
long ExtendedRemoteFrameCount ()
CANx.ExtendedRemoteFrameCount
```

## Description

Returns the number of extended remote CAN messages on channel x since start of measurement.

Valid x values: 1…32

## Return Values

Number of extended remote CAN messages on channel x since start of measurement.

## Example

```c
write ("Number of extended remote messages on CAN1 = %d", CAN1.ExtendedRemoteFrameCount);
```

## Availability

| Since Version |
|---|
