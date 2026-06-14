# sensorQueueCombinedFrame

> Category: `Sensor` | Type: `function`

## Syntax

```c
SensorErrorCode sensorQueueCombinedFrame(char[] sysVarNamespace, byte[] writeBuffer, dword writeBufferCount, dword readByteCount);
```

## Description

This function is intended to be used for I2C master simulation. It queues a frame to write and then read the given number of bytes from the given slave.

## Return Values

This method returns a SensorErrorCode.

## Example

```c
// Byte array to be sent to the slave
byte sendData[2] = {0x42, 0x21};

// Send the prepared byte array to the slave, then read 4 bytes from the slave
sensorQueueCombinedFrame ("SENSOR::I2C::ExampleChannel::ExampleSlave", sendData, 2, 4);
```

## Availability

| Since Version |
|---|
