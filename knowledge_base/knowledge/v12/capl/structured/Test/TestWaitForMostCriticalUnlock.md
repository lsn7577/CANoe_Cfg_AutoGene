# TestWaitForMostCriticalUnlock

> Category: `Test` | Type: `function`

## Syntax

```c
long TestWaitForMostCriticalUnlock(dword aTimeout);
```

## Description

The function waits until the expiration of the time aTimout for the occurrence of a LightLock event indicating "critical unlock" state.

A LightLock event with a "critical unlock" state is generated, when a single "Light & no Lock" state occurs after a "stable lock" state and lasts longer than tUnlock (see MOST specification), or several "light, no lock" states occur successively and add up to a duration longer than tUnlock.

Consider to set always the appropriate bus context in a multibus environment before the function is called.

Further information on site MultiBus Environment.

## Return Values

-2: Resume due to constraint violation

## Availability

| Since Version |
|---|
