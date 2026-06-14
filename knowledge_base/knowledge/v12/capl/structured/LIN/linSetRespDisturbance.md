# linSetRespDisturbance

> Category: `LIN` | Type: `function`

## Syntax

```c
long linSetRespDisturbance (long frameId, long lengthInBits, long level, long offsetInSixteenthBits)
```

## Description

Activates a disturbance in the response space of the specified LIN frame. A normal response by a simulated slave will be deactivated as long as the disturbance is active.

The disturbance starts with the next occurrence of the specified frame. To stop the disturbance the functions linResetRespDisturbance() shall be used.

## Return Values

On success, a value unequal to zero, otherwise zero.

## Example

On pressing 'c' key start corrupting the response space and the first databyte of the response for LIN frame Motor1State_Cycl.

```c
on key 'c'
{
linFrame Motor1State_Cycl mMotor1State_Cycl;
if (0!=linSetRespDisturbance (mMotor1State_Cycl.id, 
 1, 0, 20))
{
// for the next the first bit of the response space 
 or of the first databyte
// (if the response space is zero) is inverted from recessive to 
dominant
}
}
```

## Availability

| Since Version |
|---|
