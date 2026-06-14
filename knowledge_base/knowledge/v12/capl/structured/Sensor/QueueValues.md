# QueueValues

> Category: `Sensor` | Type: `function`

## Syntax

```c
SensorErrorCode SysVarName.QueueValues (float[] values, dword valueCount);
```

## Description

Inserts the given values into the send queue of the given sensor signal system variable.

## Return Values

This method returns a SensorErrorCode.

## Example

```c
float values[10];
// Todo: fill array with signal values

sysvar::SENSOR::PSI5::ExampleChannel::ExampleSensor::ExampleTimeslot::Signals::ExampleSignal_Stim.QueueValues( values, 10);
```

## Availability

| Since Version |
|---|
