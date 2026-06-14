# startStatisticAcquisition

> Category: `Other` | Type: `function`

## Syntax

```c
void startStatisticAcquisition()
```

## Description

A new acquisition range is started with this function. If an acquisition range has already been started, the function has no effect since it cannot influence the currently active range.

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
