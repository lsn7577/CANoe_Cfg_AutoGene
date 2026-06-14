# TestWaitForMostShortUnlock

> Category: `Test` | Type: `function`

## Syntax

```c
long TestWaitForMostShortUnlock(dword aTimeout);
```

## Description

The function waits until the expiration of the time aTimout for the occurrence of a LightLock event indicating "Light & no Lock" state.

A LightLock event with a "Light & no Lock" state is generated, when there is no interpretable signal at the Optical Receiver (FOR) of the hardware for a brief moment (< tUnlock, see also MOST specification) and the ring has been in a "Light & Lock" state previously.

Consider to set always the appropriate bus context in a multibus environment before the function is called.

Further information on site MultiBus Environment.

## Return Values

-2: Resume due to constraint violation

## Availability

| Since Version |
|---|
