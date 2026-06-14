# linSetWakeupBehavior

> Category: `LIN` | Type: `function`

## Syntax

```c
linSetWakeupBehavior(dword restartScheduler, dword wakeupIdentifier);
```

## Description

Defines the behavior after wake-up signal or an internal wake-up.

When LIN hardware is not in sleep mode calling this function will have no effect.

## Return Values

On success, a value unequal to zero, otherwise zero.

## Example

Change wake-up behavior on receiving a sleep mode event

```c
on linSleepModeEvent
{
  linSetWakeupBehavior (0, 0x1, 0, 100); // don't restart scheduler, use 0x1 as wake-up identifier, start scheduling or send the wake-up identifier after 100 ms.
}
```

## Availability

| Since Version |
|---|
