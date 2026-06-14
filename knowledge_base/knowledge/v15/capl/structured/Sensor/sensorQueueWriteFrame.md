# sensorQueueWriteFrame

> Category: `Sensor` | Type: `function`

## Syntax

```c
SensorErrorCode sensorQueueWriteFrame(char[] sysVarNamespace, byte[] writeBuffer, dword writeByteCount); // from 1
SensorErrorCode sensorQueueWriteFrame(char[] sysVarNamespace, byte[] writeBuffer, dword writeByteCount, dword startDelayNs); // from 2
```

## Description

This function is intended to be used for I2C master simulation. It queues a frame to write the given bytes to the given slave.

## Parameters

| Name | Description |
|---|---|
| sysVarNamespace | The namespace of the slave the data shall be queued in. |
| writeBuffer | Buffer containing the bytes to be sent to the slave. |
| writeByteCount | Length of the write buffer in bytes. |
| startDelayNs | Delay in ns before the frame is actually sent to the slave. |

## Return Values

This method returns a SensorErrorCode.

## Example

```c
// Byte array to be sent to the slave
byte sendData[2] = {0x42, 0x21};

// Queue the request to the slave
sensorQueueWriteFrame ("SENSOR::I2C::ExampleChannel::ExampleSlave", sendData, 2);
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
