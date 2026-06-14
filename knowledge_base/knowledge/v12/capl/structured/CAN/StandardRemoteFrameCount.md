# StandardRemoteFrameCount

> Category: `CAN` | Type: `function`

## Syntax

```c
long StandardRemoteFrameCount ()
CANx.StandardRemoteFrameCount
```

## Description

Returns the number of standard remote CAN frames on channel x since start of measurement.

Valid x values: 1…32

## Return Values

Number of standard remote CAN frames on channel x since start of measurement.

## Example

```c
write ("Number of standard remote frames on CAN1 = %d", CAN1.StandardRemoteFrameCount);
```

## Availability

| Since Version |
|---|
