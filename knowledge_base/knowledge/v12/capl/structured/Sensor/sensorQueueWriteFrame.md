# sensorQueueWriteFrame

> Category: `Sensor` | Type: `function`

## Syntax

```c
SensorErrorCode sensorQueueWriteFrame(char[] sysVarNamespace, byte[] writeBuffer, dword writeByteCount);
```

## Description

This function is intended to be used for I2C master simulation. It queues a frame to wite the given bytes to the given slave.

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

| Since Version |
|---|
