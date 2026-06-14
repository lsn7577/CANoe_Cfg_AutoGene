# mostNwmFiSetParameter, mostNwmFiGetParameter

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostNwmFiSetParameter(long paramID, long value)
```

## Description

In order to modify timing parameters the functions mostNwmFiSetParameter and mostNwmFiGetParameter provide access to the timing parameters of CANoe’s NetworkMaster implementation.

Use the function with care since the state machine of the NetworkMaster is not guaranteed to work properly afterwards.

Refer to the MOST specification for a detailed description of the timing parameters and the NetworkMaster state machine.

The function is available for CAPL programs assigned to the NetworkMaster block in the Simulation Setup.

## Return Values

mostNwmFiSetParameter
See error codes

## Example

```c
// set the timer value for tDelayCfgRequest2 to 15 s
mostNwmFiSetParameter(5, 15000);
```

## Availability

| Since Version |
|---|
