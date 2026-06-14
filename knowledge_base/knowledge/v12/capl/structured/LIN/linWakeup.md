# linWakeup

> Category: `LIN` | Type: `function`

## Syntax

```c
long linWakeup()
```

## Description

Sends wakeup signals. Wakeup signals can only be sent while the LIN hardware is in Sleep mode. If no parameters are given, the default parameters or the parameters configured with linSetWakeupTimings are used. Wake up timings can be configured per node for nodes defined in a LIN database. If no database is used the signature using wake parameters shall be used.

When LIN hardware is not in Sleep mode calling this function will have no effect.

## Return Values

On success, a value unequal to zero, otherwise zero.

## Example

```c
// send a wakeup signal via a keyboard event
on key 'w'
{
  linWakeup();
}
// send wakeup signal 3 times with 150 ms delay between 2 consecutive signals and a length of 300 us
linWakeup(150, 3, 300);
...
```

## Availability

| Since Version |
|---|
