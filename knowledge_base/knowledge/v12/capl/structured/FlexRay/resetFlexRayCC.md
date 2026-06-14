# resetFlexRayCC

> Category: `FlexRay` | Type: `function`

## Syntax

```c
void resetFlexRayCC (int channel);
```

## Description

This function initializes the FlexRay Communication Controller (CC) and begins a new start-up phase for the cluster or a new integrations phase in the cluster - depending on whether a start-up frame is to be sent or not.

## Return Values

—

## Example

The following program resets the FlexRay interface of the attached channel, when <R>key is pressed.

```c
on key 'r'
{
   resetFlexRayCC(%CHANNEL%);
   Write("Reset FlexRay CC on channel %d.", %CHANNEL%);
}
```

## Availability

| Since Version |
|---|
