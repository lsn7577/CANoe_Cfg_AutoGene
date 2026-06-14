# SetClockTickLength

> Category: `Sensor` | Type: `method`

## Syntax

```c
SensorErrorCode sysvarSensorNamespace.SetClockTickLength(double clockTickLengthUs);
```

## Description

Overwrites the clock tick length of a simulated sensor with the given value.

## Parameters

| Name | Description |
|---|---|
| clockTickLengthUs | The overridden clock tick length in microseconds. Valid range: 1.4 – 120 µs |

## Return Values

This method returns a SensorErrorCode.

## Example

```c
enum sensorErrorCode result;

// Change the sensor's tick length to 2.5 us
result = sysvar::SENSOR::SENT::SENSORSIM::Sensor.SetClockTickLength(2.5);

if (result == eSensorNoError)
{
  write("Sensor clock tick lenght changed successfully.");
}
else
{
  write("Changing sensor clock tick length failed with code: %d", result);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 15 | — | — | — | 6 |
| Restricted To | — | Sensor | — | — | — | Sensor |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
