# linSetwakeupCondition

> Category: `LIN` | Type: `function`

## Syntax

```c
linSetWakeupCondition(dword numWakeupSignals);
```

## Description

Determines the conditions under which the LIN hardware can be reactivated (leaves the sleep mode).

When LIN hardware is not in master mode calling this function will have no effect.

## Return Values

On success, a value unequal to zero, otherwise zero.

## Example

```c
// configure LIN hardware to wakeup after 3 wakeup signals
linSetWakeupCondition (3);
```

## Availability

| Since Version |
|---|
