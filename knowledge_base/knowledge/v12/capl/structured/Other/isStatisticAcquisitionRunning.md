# isStatisticAcquisitionRunning

> Category: `Other` | Type: `function`

## Syntax

```c
int isStatisticAcquisitionRunning()
```

## Description

This function is used to test whether an acquisition range has already been started.

## Return Values

The function returns 1 if an evaluation is already running. Otherwise it returns 0.

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
}...
```

## Availability

| Since Version |
|---|
