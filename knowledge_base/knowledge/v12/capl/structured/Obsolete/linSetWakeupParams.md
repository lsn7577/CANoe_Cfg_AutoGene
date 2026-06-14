# linSetWakeupParams

> Category: `Obsolete` | Type: `function`

## Syntax

```c
long linSetWakeupParams (long wakeupDelimiter, long numberOfWakeupFrames)
```

## Description

This command determines the conditions under which the LIN hardware can be reactivated (leaves the Sleep mode).

Default wake-up delimiter depends on the hardware settings (see Hardware Configuration: LIN) while the number of expected wake-up frames is 1.

Main use case for this function is to simulate slow Master, which does not wake-up until an expected Wakeup frame burst.

When LIN hardware is not in Master mode calling this function will have no effect.

## Return Values

On success, a value unequal to zero, otherwise zero.

## Example

```c
// simulate LIN 2.0 'slow' Master
...
// configure LIN hardware to wake-up after 3 wake-up frames and to send first header
// 100 ms after wakeup
linSetWakeupParams(100, 3);
// send wake-up frame 3 times with 150 ms delay between 2 consecutive frames
linSendWakeup(150, 3);
...
```

## Availability

| Up to Version |
|---|
