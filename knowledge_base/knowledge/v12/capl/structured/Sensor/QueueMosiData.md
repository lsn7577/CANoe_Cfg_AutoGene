# QueueMosiData

> Category: `Sensor` | Type: `function`

## Syntax

```c
SensorErrorCode SysVarNamespace.QueueMosiData(byte buffer[], dword bitCount);
```

## Description

This method is intended to be used for SPI master simulation. It inserts the given MOSI data into the send queue from the master to the given slave.

## Return Values

This method returns a SensorErrorCode.

## Example

```c
  // Some example values
  dword value1 = 7;
  dword value2 = 13;

  // Byte array used to prepare the master request
  byte requestData[2] = {0x00, 0x00};

  // Insert two 6 bit values
  SensorInsertInteger(requestData, 2, value1, 0, 6, 1);
  SensorInsertInteger(requestData, 2, value2, 6, 6, 1);

  // Send the prepared 12 bits to the ExampleSlave

sysvar::SENSOR::SPI::ExampleChannel::ExampleSlave.QueueMosiData(requestData, 12);
```

## Availability

| Since Version |
|---|
