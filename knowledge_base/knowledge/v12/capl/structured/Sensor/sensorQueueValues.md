# sensorQueueValues

> Category: `Sensor` | Type: `function`

## Syntax

```c
SensorErrorCode sensorQueueValues (char[] sysVarName, float[] values, dword valueCount);
```

## Description

Inserts the given values into the send queue of the given sensor signal system variable.

## Return Values

This function returns a SensorErrorCode.

## Example

```c
float values[10];
// Todo: fill array with signal values

sensorQueueValue("SENSOR::PSI5::ExampleChannel::ExampleSensor::ExampleTimeslot::Signals::ExampleSignal_Stim", values, 10);
```

## Availability

| Since Version |
|---|
