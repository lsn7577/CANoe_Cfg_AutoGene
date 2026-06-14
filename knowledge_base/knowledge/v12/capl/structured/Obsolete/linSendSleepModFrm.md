# linSendSleepModFrm

> Category: `Obsolete` | Type: `function`

## Syntax

```c
long linSendSleepModFrm (long silent, long restartScheduler, long wakeupIdentifier)
```

## Description

This function leads to a transmission of a go-to-sleep-command. Frame identifier and data byte values of that command depend on the used LIN specification:

Frame length is 2 bytes. The data bytes remain not changed.

Frame length is 8 bytes. The first data byte is set to 0, the other data bytes remain not changed.

Calling this function in the event procedure on preStart (parameter silent = 1) leads to measurement start in Sleep mode.

## Return Values

On success, a value unequal to zero, otherwise zero.

## Example

Start measurement in Sleep mode

```c
on preStart
{
linSendSleepModFrm(1, 0 , 0x1); // use 0x1 as wake-up 
 identifier
}
or
// send go-to-sleep-command during measurement
...
linSendSleepModFrm(0, 0 , 0xFF); // explicit sleep frame, no wake-up identifier
```

## Availability

| Up to Version |
|---|
