# QueueCombinedFrame

> Category: `Sensor` | Type: `method`

## Syntax

```c
SensorErrorCode SysVarNamespace.QueueCombinedFrame(byte[] writeBuffer, dword writeBufferCount, dword readByteCount); // from 1
SensorErrorCode SysVarNamespace.QueueCombinedFrame(byte[] writeBuffer, dword writeBufferCount, dword readByteCount, dword startDelayNs); // from 2
```

## Description

This method is intended to be used for I2C master simulation. It queues a frame to write and then read the given number of bytes from the given slave.

## Parameters

| Name | Description |
|---|---|
| writeBuffer | Buffer containing the bytes to be sent to the slave. |
| writeByteCount | Length of the write buffer in bytes. |
| readByteCount | The number of bytes to read from the slave. |
| startDelayNs | Delay in ns before the frame is actually sent to the slave. |

## Return Values

This method returns a SensorErrorCode.

## Example

```c
// Byte array to be sent to the slave
byte sendData[2] = {0x42, 0x21};

// Send the prepared byte array to the slave, then read 4 bytes from the slave
sysvar::SENSOR::I2C::ExampleChannel::ExampleSlave.QueueCombinedFrame (sendData, 2, 4);
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
