# sensorQueueFrame

> Category: `Sensor` | Type: `function`

## Syntax

```c
SensorErrorCode sensorQueueFrame(char[] sysVarNamespace, byte buffer[], dword byteCount);
```

## Description

This function is intended to be used for I2C slave simulation. It inserts the given data bytes into the response queue of the given slave.

## Return Values

This method returns a SensorErrorCode.

## Example

```c
// Byte array used to prepare the slave's 12 bit response
byte responseData[2] = {0x42, 0x21};

// Queue the resonse in the slave
sensorQueueFrame("SENSOR::I2C::ExampleChannel::ExampleSlave", responseData, 2);
```

## Availability

| Since Version |
|---|
