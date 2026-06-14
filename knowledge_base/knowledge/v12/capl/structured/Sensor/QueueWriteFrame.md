# QueueWriteFrame

> Category: `Sensor` | Type: `function`

## Syntax

```c
SensorErrorCode SysVarNamespace.QueueWriteFrame(byte[] writeBuffer, dword writeByteCount);
```

## Description

This method is intended to be used for I2C master simulation. It queues a frame to wite the given bytes to the given slave.

## Return Values

This method returns a SensorErrorCode.

## Example

```c
// Byte array to be sent to the slave
byte sendData[2] = {0x42, 0x21};

// Queue the request to the slave
sysvar::SENSOR::I2C::ExampleChannel::ExampleSlave.QueueWriteFrame (sendData, 2);
```

## Availability

| Since Version |
|---|
