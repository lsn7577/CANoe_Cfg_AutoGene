# TestWaitForMostStableLock

> Category: `Test` | Type: `function`

## Syntax

```c
long TestWaitForMostStableLock(dword aTimeout);
```

## Description

The function waits until the expiration of the time aTimout for the occurrence of a LightLock event indicating "stable lock" state.

A LightLock event with a "stable lock" state is generated, when a "light & Lock" state lasts uninterrupted at the hardware for a period of time equal or longer than tLock (see MOST specification).

Consider to set always the appropriate bus context in a multibus environment before the function is called.

Further information on site MultiBus Environment.

## Return Values

-2: Resume due to constraint violation

## Availability

| Since Version |
|---|
