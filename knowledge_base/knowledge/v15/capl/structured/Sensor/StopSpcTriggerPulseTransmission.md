# StopSpcTriggerPulseTransmission

> Category: `Sensor` | Type: `method`

## Syntax

```c
SensorErrorCode sysvarSensorNamespace.StopSpcTriggerPulseTransmission();
```

## Description

Stops any periodic trigger pulse transmission on the specified ECU channel.

## Return Values

This method returns a SensorErrorCode.

## Example

```c
enum sensorErrorCode result;

// Stop periodic SPC trigger pulse transmission
result = sysvar::SENSOR::SENT::ECUSIM.StopSpcTriggerPulseTransmission();

if (result == eSensorNoError)
{
  write("Stopping of SPC trigger pulse transmission succeeded.");
}
else
{
  write("Stopping of SPC trigger pulse transmission failed with code: %d.", result);
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
