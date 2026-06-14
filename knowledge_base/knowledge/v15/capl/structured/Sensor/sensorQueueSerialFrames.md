# sensorQueueSerialFrames

> Category: `Sensor` | Type: `function`

## Syntax

```c
SensorErrorCode sensorQueueSerialFrames(char[] sysVarNamespace, char[] data, dword dataCount); // form 1
SensorErrorCode sensorQueueSerialFrames(char[] sysVarNamespace, dword[] data, dword dataCount); // from 2
SensorErrorCode sensorQueueSerialFrames(char[] sysVarNamespace, dword[] data, dword dataCount, dword frameSpacingNs); // from 3
```

## Description

Queues one frame for each given datum.

## Parameters

| Name | Description |
|---|---|
| sysVarNamespace | The namespace of the UART/RS-485/LVDS channel the data shall be queued in. |
| data | The array of values/characters that shall be sent (one datum per frame). |
| dataCount | The number of data/frames to send. |
| frameSpacingNs | The wait time after each sent frame in ns (default is 0). Spacing is performed with a resolution of 10µs. Intermediate values are rounded up to the next greater supported value. |

## Return Values

This function returns a SensorErrorCode.

## Example

```c
// Send three frames with different payloads
dword data[3] = {0x01, 0x02, 0x03};
sensorQueueSerialFrames(“SENSOR::UART::ExampleChannel”, data, 3);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 10.0 SP3 | — | — | — | 2.2 SP2 |
| Restricted To | — | Sensor | — | — | — | Sensor |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
