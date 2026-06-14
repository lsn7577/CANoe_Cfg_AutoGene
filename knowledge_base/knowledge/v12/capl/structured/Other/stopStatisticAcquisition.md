# stopStatisticAcquisition

> Category: `Other` | Type: `function`

## Syntax

```c
void stopStatisticAcquisition()
```

## Description

A started acquisition range is stopped with this function. If no acquisition range has been started yet, this function has no effect.

## Return Values

—

## Example

Statistical Evaluation (StatisticAcquisition)

```c
...
// Tests for running acquisition range and stops it.
// If no statistical data acquisition is active a new one is started.
if(isStatisticAcquisitionRunning())
{
// Stops the running acquisition range
stopStatisticAcquisition();
}
else
{
// Starts a new acquisition range
startStatisticAcquisition();
}
...
```

## Availability

| Since Version |
|---|
