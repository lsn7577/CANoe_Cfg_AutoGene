# TestWaitForMostLightOff

> Category: `Test` | Type: `function`

## Syntax

```c
long TestWaitForMostLightOff(dword aTimeout);
```

## Description

The function waits until the expiration of the time aTimout for the occurrence of a LightLock event indicating "no Light & no Lock" state.

A LightLock event with a "no Light & no Lock" state is generated, when the hardware connected to the channel no longer receives light at the Fiber Optical Receiver (FOR).

Consider to set always the appropriate bus context in a multibus environment before the function is called.

Further information on site MultiBus Environment.

## Return Values

-2: Resume due to constraint violation

## Availability

| Since Version |
|---|
