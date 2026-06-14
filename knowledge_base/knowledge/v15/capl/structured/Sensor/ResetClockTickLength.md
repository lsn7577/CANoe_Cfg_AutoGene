# ResetClockTickLength

> Category: `Sensor` | Type: `method`

## Syntax

```c
SensorErrorCode sysvarSensorNamespace.ResetClockTickLength();
```

## Description

Resets the clock tick length of a simulated sensor to the initially configured value.

## Return Values

This method returns a SensorErrorCode.

## Example

```c
enum sensorErrorCode result;

// Reset the sensor's tick length to the configured value.
result = sysvar::SENSOR::SENT::SENSORSIM::Sensor.ResetClockTickLength();

if (result == eSensorNoError)
{
  write("Sensor clock tick lenght reset successfully.");
}
else
{
  write("Resetting sensor clock tick length failed with code: %d", result);
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
