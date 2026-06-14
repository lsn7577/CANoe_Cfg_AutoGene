# linSendWakeup

> Category: `Obsolete` | Type: `function`

## Syntax

```c
long linSendWakeup()
```

## Description

This command is used to send Wakeup frames. Wakeup frames can only be sent while the LIN hardware is in Sleep mode. If no parameters are given, the default values of the parameters are used.

When LIN hardware is not in Sleep mode calling this function will have no effect.

## Return Values

On success, a value unequal to zero, otherwise zero.

## Example

Send wake-up frame on keyboard event

```c
on key 'w'
{
linSendWakeup(); 
}
or
// simulate LIN 2.0 “slow” Master
...
// configure LIN hardware to wake-up after 3 wake-up frames and to send first header
// 100 ms after wake-up 
linSetWakeupParams(100, 3);
// send wake-up frame 3 times with 150 ms delay between 2 consecutive frames
linSendWakeup(150, 3);
...
```

## Availability

| Up to Version |
|---|
