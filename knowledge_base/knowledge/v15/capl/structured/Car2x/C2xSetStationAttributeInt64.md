# C2xSetStationAttributeInt64

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xSetStationAttributeInt64(char stationName[], char attributeName[], long keypointIndex, int64 value)
```

## Description

Sets an attribute value for a scenario station and a particular keypoint as Int64.

## Parameters

| Name | Description |
|---|---|
| stationName | Name of the station. |
| attributeName | Name of the attribute in the station’s timeline. |
| keypointIndex | The Keypoint index of the attribute (starts at 0). |
| value | The value to be set. |

## Example

```c
on start
{
  // Set the first lights keypoint to 1
  C2xSetStationAttributeInt64("DuT", "R_Light", 0, 1);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 14.0 SP2 | — | — | — | 5 SP3 |
| Restricted To | — | Car2x | — | — | — | Car2x |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
