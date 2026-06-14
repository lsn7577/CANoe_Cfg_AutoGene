# linSendAsSporadic

> Category: `LIN` | Type: `function`

## Syntax

```c
long linSendAsSporadic (long frameID)
```

## Description

This function can be used to configure an associated frame as being ready for transmission. At the next time slot, corresponding to its sporadic frame, the associated frame will be sent once.

If LIN hardware is not in Master mode or there is no schedule table with corresponding sporadic frame defined then calling this function will have no effect.

## Return Values

On success, a value unequal to zero, otherwise zero.

## Availability

| Since Version |
|---|
