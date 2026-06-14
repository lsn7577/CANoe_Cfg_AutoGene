# sensorQueueSerialFrame

> Category: `Sensor` | Type: `function`

## Syntax

```c
SensorErrorCode sensorQueueSerialFrame(char[] sysVarNamespace, dword data); // from 1
SensorErrorCode sensorQueueSerialFrame(char[] sysVarNamespace, dword data, dword frameSpacingNs); // from 2
```

## Description

Queues one frame for the given datum.

## Parameters

| Name | Description |
|---|---|
| sysVarNamespace | The namespace of the UART/RS-485/LVDS channel the data shall be queued in. |
| data | The datum that shall be sent. |
| frameSpacingNs | The wait time after each sent frame in ns (default is 0). Spacing is performed with a resolution of 10µs. Intermediate values are rounded up to the next greater supported value. |

## Return Values

This function returns a SensorErrorCode.

## Example

```c
// Send a single frame with payload "42"
sensorQueueSerialFrame(“SENSOR::UART::ExampleChannel”, 42);
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
