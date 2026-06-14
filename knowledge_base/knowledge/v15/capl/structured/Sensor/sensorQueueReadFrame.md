# sensorQueueReadFrame

> Category: `Sensor` | Type: `function`

## Syntax

```c
SensorErrorCode sensorQueueReadFrame(char[] sysVarNamespace, dword readByteCount); // from 1
SensorErrorCode sensorQueueReadFrame(char[] sysVarNamespace, dword readByteCount, dword startDelayNs); // from 2
```

## Description

This function is intended to be used for I2C master simulation. It queues a frame to read the given number of bytes from the given slave.

## Parameters

| Name | Description |
|---|---|
| sysVarNamespace | The namespace of the slave the data shall be queued in. |
| readByteCount | The number of bytes to read from the slave. |
| startDelayNs | Delay in ns before the frame is actually sent to the slave. |

## Return Values

This method returns a SensorErrorCode.

## Example

```c
// Queue a request to read 4 bytes from the slave
sensorQueueFrame("SENSOR::I2C::ExampleChannel::ExampleSlave", 4);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 11.0 SP3 | — | — | — | 3.0 SP3 |
| Restricted To | — | Sensor | — | — | — | Sensor |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
