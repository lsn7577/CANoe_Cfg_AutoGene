# stopStatisticAcquisition

> Category: `Other` | Type: `function`

## Syntax

```c
void stopStatisticAcquisition();
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

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 3.0 | 3.0 | 13.0 | — | 14 | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | — | — | — | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | ✔ | N/A |
