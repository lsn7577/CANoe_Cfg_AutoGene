# linGotoSleepInternal

> Category: `LIN` | Type: `function`

## Syntax

```c
long linGotoSleepInternal();
```

## Description

Sets the LIN hardware to Sleep mode without sending a go-to-sleep-command on the network.

Calling this function in the event procedure on prestart leads to measurement start in sleep mode.

## Return Values

On success, a value unequal to zero, otherwise zero.

## Example

```c
// start measurement in Sleep mode
on preStart
{
  linGotoSleepInternal();
}
```

## Availability

| Since Version |
|---|
