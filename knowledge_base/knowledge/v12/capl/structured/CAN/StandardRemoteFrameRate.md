# StandardRemoteFrameRate

> Category: `CAN` | Type: `function`

## Syntax

```c
long StandardRemoteFrameRate ()
CANx.StandardRemoteFrameRate
```

## Description

Returns the current rate of standard remote CAN frames of channel x.

Valid x values: 1…32

## Return Values

Current rate of standard remote CAN frames of channel x in messages per second.

## Example

```c
write ("Rate of standard remote frames of CAN1 
 = %d", CAN1.StandardRemoteFrameRate);
```

## Availability

| Since Version |
|---|
