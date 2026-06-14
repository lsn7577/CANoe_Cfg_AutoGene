# linSetSchedulerJitter

> Category: `LIN` | Type: `function`

## Syntax

```c
long linSetSchedulerJitter (long mode)
```

## Description

Sets/resets the jitter mode and the jitter of the LIN hardware scheduler. (the channel is determined by the CAPL program context).

If the Master node is not simulated or no schedule tables are defined, then this function will have no effect.

## Return Values

On success, a value unequal to zero, otherwise zero.

## Example

```c
on key 'j'
{
if (0!=linSetSchedulerJitter(1))
{
// for the next LIN hardware scheduler will use jitter specified in the LDF
}
}
```

## Availability

| Since Version |
|---|
