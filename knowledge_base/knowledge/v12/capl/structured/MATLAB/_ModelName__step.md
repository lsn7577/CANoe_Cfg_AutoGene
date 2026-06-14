# <ModelName>_step

> Category: `MATLAB` | Type: `function`

## Syntax

```c
long <ModelName>_step();
```

## Description

Executes a simulation step.

## Return Values

On success 0, otherwise a value unequal to zero.

## Example

```c
on timer modelTimer
{
myControllerMdl_step();
}
```

## Availability

| Since Version |
|---|
