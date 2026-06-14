# QueueFrame

> Category: `Sensor` | Type: `function`

## Syntax

```c
SensorErrorCode SysVarNamespace.QueueFrame(byte buffer[], dword byteCount);
```

## Description

This method is intended to be used for I2C slave simulation. It inserts the given data bytes into the response queue of the given slave.

## Return Values

This method returns a SensorErrorCode.

## Example

```c
// Byte array used to prepare the slave's 2 byte response
byte responseData[2] = {0x42, 0x21};

// Queue the resonse in the slave
sysvar::SENSOR::I2C::ExampleChannel::ExampleSlave.QueueFrame (responseData, 2);
```

## Availability

| Since Version |
|---|
