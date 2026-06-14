# timeToElapse

> Category: `Other` | Type: `function`

## Syntax

```c
long timeToElapse(timer t) (Form 1)
```

## Description

Returns a value indicating how much more time will elapse before an on timer event procedure is called.

For form 1, the time value is returned in seconds; for form 2, the time value is returned in milliseconds.

If the timer is not active, -1 is returned. This is also the case in the on timer event procedure itself.

## Return Values

Time to go until the timer elapses and the event procedure is called.

## Example

```c
timer t;
setTimer(t, 5);
write("Time to elapse: %d", timeToElapse(t)); // writes 5
```

## Availability

| Since Version |
|---|
