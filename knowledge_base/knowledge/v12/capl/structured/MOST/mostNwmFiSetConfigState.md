# mostNwmFiSetConfigState

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostNwmFiSetConfigState(long state, long sendConfigStatusMsg)
```

## Description

Forces the network configuration status to be set in CANoe’s NetworkMaster.

Use the function with care since the state machine of the NetworkMaster is not guaranteed to work properly afterwards. (A shutdown of the network will reset the NetworkMaster’s state machine.)

The function is available for CAPL programs assigned to the NetworkMaster block in the Simulation Setup.

## Return Values

See error codes

## Availability

| Since Version |
|---|
