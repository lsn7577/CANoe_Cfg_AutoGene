# ExtendedFrameRate

> Category: `CAN` | Type: `function`

## Syntax

```c
long ExtendedFrameRate ()
CANx.ExtendedFrameRate
```

## Description

Returns the current rate of extended CAN messages on channel x.

Valid x values: 1…32

## Return Values

Current rate of extended CAN messages on channel x in messages per second.

## Example

```c
write ("Rate of extended frames on CAN1 = %d", 
 CAN1.ExtendedFrameRate);
```

## Availability

| Since Version |
|---|
