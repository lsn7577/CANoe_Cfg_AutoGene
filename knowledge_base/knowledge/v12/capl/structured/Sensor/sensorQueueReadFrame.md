# sensorQueueReadFrame

> Category: `Sensor` | Type: `function`

## Syntax

```c
SensorErrorCode sensorQueueReadFrame(char[] sysVarNamespace, dword readByteCount);
```

## Description

This function is intended to be used for I2C master simulation. It queues a frame to read the given number of bytes from the given slave.

## Return Values

This method returns a SensorErrorCode.

## Example

```c
// Queue a request to read 4 bytes from the slave
sensorQueueFrame("SENSOR::I2C::ExampleChannel::ExampleSlave", 4);
```

## Availability

| Since Version |
|---|
