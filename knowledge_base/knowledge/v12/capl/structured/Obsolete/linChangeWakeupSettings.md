# linChangeWakeupSettings

> Category: `Obsolete` | Type: `function`

## Syntax

```c
dword linChangeWakeupSettings(byte restartScheduler, long wakeupIdentifier)
```

## Description

This function changes the wake-up setting.

When LIN hardware is not in Sleep mode calling this function will have no effect.

## Return Values

On success, a value unequal to zero, otherwise zero.

## Example

Change wake-up settings on getting Sleep mode event

```c
on linSleepModeEvent
{
linChangeWakeupSettings(0, 0x1); // do not restart scheduler, use 0x1 as wake-up identifier
}
```

## Availability

| Up to Version |
|---|
