# QueueSerialFrame

> Category: `Sensor` | Type: `method`

## Syntax

```c
SensorErrorCode SysVarNamespace.QueueSerialFrame(dword data); // form 1
SensorErrorCode SysVarNamespace.QueueSerialFrame(dword data, dword frameSpacingNs); // form 2
```

## Description

Queues one frame for the given datum.

## Parameters

| Name | Description |
|---|---|
| data | The datum that shall be sent. |
| frameSpacingNs | The wait time after each sent frame in ns (default is 0). Spacing is performed with a resolution of 10µs. Intermediate values are rounded up to the next greater supported value. |

## Return Values

This method returns a SensorErrorCode.

## Example

```c
// Send a single frame with payload "42"
sysvar::SENSOR::UART::ExampleChannel.QueueSerialFrame(42);
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
