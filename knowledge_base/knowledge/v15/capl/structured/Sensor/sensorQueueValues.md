# sensorQueueValues

> Category: `Sensor` | Type: `function`

## Syntax

```c
SensorErrorCode sensorQueueValues (char[] sysVarName, float[] values, dword valueCount);
```

## Description

Inserts the given values into the send queue of the given sensor signal system variable.

## Parameters

| Name | Description |
|---|---|
| sysVarName | The name of the sensor signal system variable the values shall be queued in. |
| values | Specifies the values that shall be queued. |
| valueCount | Specifies the number of values in the given array. |

## Return Values

This function returns a SensorErrorCode.

## Example

```c
float values[10];
// Todo: fill array with signal values

sensorQueueValues("SENSOR::PSI5::ExampleChannel::ExampleSensor::ExampleTimeslot::Signals::ExampleSignal_Stim", values, 10);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 9.0 SP3 | — | — | — | 2.2 |
| Restricted To | — | Sensor | — | — | — | Sensor |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
