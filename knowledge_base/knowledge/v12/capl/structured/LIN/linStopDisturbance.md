# linStopDisturbance

> Category: `LIN` | Type: `function`

## Syntax

```c
long linStopDisturbance()
```

## Description

Stops the disturbance on the bus which is started with linStartDisturbance().

Note that disturbances shorter than 64 bit times cannot be stopped.

## Return Values

On success a value unequal to zero, otherwise zero.

## Availability

| Since Version |
|---|
