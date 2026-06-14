# ExtendedRemoteFrameRate

> Category: `CAN` | Type: `function`

## Syntax

```c
long ExtendedRemoteFrameRate ()
CANx.ExtendedRemoteFrameRate
```

## Description

Returns the current rate of extended remote CAN messages on channel x.

Valid x values: 1…32

## Return Values

Current rate of extended remote CAN messages on channel x in frames per second.

## Example

```c
write ("Rate of extended remote messages on CAN1 = %d", CAN1.ExtendedRemoteFrameRate);
```

## Availability

| Since Version |
|---|
