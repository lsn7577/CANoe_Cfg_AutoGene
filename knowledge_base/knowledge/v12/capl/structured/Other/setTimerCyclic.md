# setTimerCyclic

> Category: `Other` | Type: `function`

## Syntax

```c
void setTimerCyclic(msTimer t, long firstDuration, long period); // form 1
```

## Description

Sets a cyclical timer.

With form 2, firstDuration is implicitly the same as period, i.e. the timer runs precisely according to period the first time.

## Return Values

—

## Example

Starting of a timer that expires the first time 10 ms after the start of measurement and thereafter every 20 ms (10 ms, 30 ms, 50 ms, 70 ms etc.)

```c
variables {
   msTimer t;
}
on start {
   setTimerCyclic(t, 10, 20)
}
```

## Availability

| Since Version |
|---|
