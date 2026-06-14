# C2xStopScenario

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xStopScenario();
```

## Description

This function stops the scenario execution immediately. The values of scenario attributes remain constant after the scenario stop. The scenario can be started again by calling C2xStartScenario() CAPL function or manually in Scenario Manager Window.

## Example

```c
on key 's'
{
  if (C2xStopScenario() == 1)
  {
    write("Scenario stopped");
  }
}

on key 'r'
{
  if (C2xStartScenario() == 1)
  {
    write("Scenario started");
  }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 11.0 | — | — | — | 3.0 |
| Restricted To | — | Car2x | — | — | — | Car2x |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
