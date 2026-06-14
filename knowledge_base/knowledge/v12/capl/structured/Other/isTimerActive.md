# isTimerActive

> Category: `Other` | Type: `function`

## Syntax

```c
int isTimerActive(timer t)
```

## Description

Return value indicates whether a specific timer is active.

This is the case between the call to the setTimer function and the call to the on timer event procedure.

## Return Values

1, if the timer is active; otherwise 0.

## Example

```c
timer t;
write("Active? %d", isTimerActive(t)); // writes 0
setTimer(t, 5);
write("Active? %d", isTimerActive(t)); // writes 1
```

## Availability

| Since Version |
|---|
