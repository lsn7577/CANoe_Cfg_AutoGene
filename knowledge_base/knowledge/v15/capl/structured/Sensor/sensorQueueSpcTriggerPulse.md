# sensorQueueSpcTriggerPulse

> Category: `Sensor` | Type: `method`

## Syntax

```c
SensorErrorCode sensorQueueSpcTriggerPulse(char[] sysVarNamespace, dword triggerLengthNs, dword responseSpaceLengthNs, dword periodic);
```

## Description

Queues a single SPC trigger pulse on the specified ECU channel.

## Parameters

| Name | Description |
|---|---|
| sysVarNamespace | The namespace of the channel or ECU. |
| triggerLengthNs | The length of the trigger pulse in nanoseconds. |
| responseSpaceLengthNs | The length of the sensor's response space in nanoseconds. |
| periodic | 1 = periodic transmission, otherwise single transmission. |

## Return Values

This function returns a SensorErrorCode.

## Example

```c
// Sensor configuration
const double cSensorTickLengthUs = 3.0;
const double cSensorMinTriggerLenTicks = 1.5;
const double cSensorTotalTriggerLenTicks = 13.0;
const dword cSensorNumLowTicks = 5;
const dword cSensorNumDataNibbles = 6;

dword triggerLenNs;
dword responseSpaceLenNs;
double maxSensorResponseTicks;

enum sensorErrorCode result;

// Calculate length of SPC trigger pulse in nanoseconds
triggerLenNs = cSensorTickLengthUs * cSensorMinTriggerLenTicks * 1000;

// Calculate length of the sensor's response space in ticks
maxSensorResponseTicks = cSensorTotalTriggerLenTicks - cSensorMinTriggerLenTicks; // Total trigger time high ticks
maxSensorResponseTicks += 56; // Sync pulse
maxSensorResponseTicks += (cSensorNumDataNibbles + 2) * 27; // Status + data + crc nibbles
maxSensorResponseTicks += cSensorNumLowTicks; // SPC end pulse

// Calculate length of the sensor's response space in nanoseconds
responseSpaceLenNs = maxSensorResponseTicks * cSensorTickLengthUs * 1000;

// Queue a periodic SPC trigger pulse with the calculated lengths
result = sensorQueueSpcTriggerPulse("SENSOR::SENT::ECUSIM", triggerLenNs, responseSpaceLenNs, 1);
if (result == eSensorNoError)
{
  write("Queuing of periodic SPC trigger pulse succeeded.");
}
else
{
  write("Queuing of periodic SPC trigger pulse failed with code: %d.", result);
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
