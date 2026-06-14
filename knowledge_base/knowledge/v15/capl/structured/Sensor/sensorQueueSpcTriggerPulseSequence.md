# sensorQueueSpcTriggerPulseSequence

> Category: `Sensor` | Type: `method`

## Syntax

```c
SensorErrorCode sensorQueueSpcTriggerPulseSequence(char[] sysVarNamespace, dword[] triggerLengthsNs, dword[] responseSpaceLengthsNs, dword sequenceLength, dword periodic);
```

## Description

Queues a sequence of SPC trigger pulses on the specified ECU channel.

## Parameters

| Name | Description |
|---|---|
| sysVarNamespace | The namespace of the channel or ECU. |
| triggerLengthNs | Array of trigger pulse lengths in nanoseconds. |
| responseSpaceLengthNs | Array of sensor response space lengths in nanoseconds. |
| sequenceLength | The length of the trigger pulse sequence. |
| periodic | 1 = periodic transmission, otherwise single transmission. |

## Return Values

This function returns a SensorErrorCode.

## Example

```c
// Sensor configurations
const dword cNumSpcSensors = 2;
double cSensorTickLengthUs[cNumSpcSensors] = { 3.0, 3.0 };
double cSensorMinTriggerLenTicks[cNumSpcSensors] = { 1.5, 5.0 };
double cSensorTotalTriggerLenTicks[cNumSpcSensors] = { 13.0, 13.0 };
dword cSensorNumLowTicks[cNumSpcSensors] = { 5, 5 };
dword cSensorNumDataNibbles[cNumSpcSensors] = { 6, 4 };

dword i;
dword triggerLensNs[cNumSpcSensors];
dword responseSpaceLensNs[cNumSpcSensors];

enum sensorErrorCode result;

for (i = 0; i < cNumSpcSensors; i++)
{
  double maxSensorResponseTicks;

  // Calculate length of SPC trigger pulse in nanoseconds
  triggerLensNs[i] = cSensorTickLengthUs[i] * cSensorMinTriggerLenTicks[i] * 1000;

  // Calculate length of the sensor's response space in ticks
  maxSensorResponseTicks = cSensorTotalTriggerLenTicks[i] - cSensorMinTriggerLenTicks[i]; // Total trigger time high ticks
  maxSensorResponseTicks += 56; // Sync pulse
  maxSensorResponseTicks += (cSensorNumDataNibbles[i] + 2) * 27; // Status + data + crc nibbles
  maxSensorResponseTicks += cSensorNumLowTicks[i]; // SPC end pulse

  // Calculate length of the sensor's response space in nanoseconds
  responseSpaceLensNs[i] = maxSensorResponseTicks * cSensorTickLengthUs[i] * 1000;
}

// Queue a periodic SPC trigger pulse sequence with the calculated lengths
result = sensorQueueSpcTriggerPulseSequence("SENSOR::SENT::ECUSIM", triggerLensNs, responseSpaceLensNs, cNumSpcSensors, 1);
if (result == eSensorNoError)
{
  write("Queuing of periodic SPC trigger pulse sequence succeeded.");
}
else
{
  write("Queuing of periodic SPC trigger pulse sequence failed with code: %d.", result);
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
