# QueueMisoData

> Category: `Sensor` | Type: `function`

## Syntax

```c
SensorErrorCode SysVarNamespace.QueueMisoData(byte buffer[], dword bitCount);
```

## Description

This method is intended to be used for SPI slave simulation in basic mode. It inserts the given MISO data into the response queue of the given slave.

## Return Values

This method returns a SensorErrorCode.

## Example

```c
  // Some example values
  dword value1 = 7;
  dword value2 = 13;

  // Byte array used to prepare the slave's 12 bit response
  byte responseData[2] = {0x00, 0x00};

  // Insert two 6 bit values
  SensorInsertInteger(responseData, 2, value1, 0, 6, 1);
  SensorInsertInteger(responseData, 2, value2, 6, 6, 1);

  // Queue the resonse in the slave

sysvar::SENSOR::SPI::ExampleChannel::ExampleSlave.QueueMisoData(responseData, 12);
```

## Availability

| Since Version |
|---|
