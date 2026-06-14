# TestWaitForSignal

> Category: `Obsolete` | Type: `function`

## Syntax

```c
long TestWaitForSignal (Signal aSignal, dword aTimeout)
```

## Description

Tests the availability of a specific signal and waits if necessary until its availability.A signal that is received at least once from the bus after the measurement starts is classified as "available".

This function is useful when you want to assure that single signals are available before starting a signal-oriented test, i.e. to synchronize the tester with the bus.

## Return Values

-2: Wait state is exited due to a constraint/condition violation

## Availability

| Since Version |
|---|
