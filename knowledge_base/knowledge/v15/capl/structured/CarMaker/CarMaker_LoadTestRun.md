# CarMaker_LoadTestRun

> Category: `CarMaker` | Type: `function`

## Syntax

```c
long CarMaker_LoadTestRun(char testRun[]);
```

## Description

Loads a test run with the given name within CarMaker.

## Parameters

| Name | Description |
|---|---|
| testRun | Hierarchical name of the test run. |

## Return Values

APO return code

## Example

```c
// load the test run configuration into CarMaker
gErrorState = CarMaker_LoadTestRun("Examples/Powertrain/DrivingCycles/EU/NEDC");
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
