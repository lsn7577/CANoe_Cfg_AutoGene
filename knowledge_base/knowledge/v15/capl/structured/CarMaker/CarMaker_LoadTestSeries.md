# CarMaker_LoadTestSeries

> Category: `CarMaker` | Type: `function`

## Syntax

```c
long CarMaker_LoadTestSeries(char testSeries[]);
```

## Description

Loads a test series with the given name within CarMaker. Although CarMaker_LoadTestRun can also be used to load test series, this function should be preferred. This is because CarMaker may display a warning about unsaved test series that will otherwise interfere with the test.

## Parameters

| Name | Description |
|---|---|
| testSeries | Hierarchical name of the test series. |

## Return Values

APO return code

## Example

```c
// load the test series into CarMaker
gErrorState = CarMaker_LoadTestSeries("Examples/Powertrain/DrivingCycles/DrivingCycles.ts");
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 13.0 | — | — | — | 5.0 |
| Restricted To | — | CarMaker | — | — | — | CarMaker |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
