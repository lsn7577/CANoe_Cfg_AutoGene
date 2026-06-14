# sensorInsertInteger

> Category: `Sensor` | Type: `function`

## Syntax

```c
SensorErrorCode sensorInsertInteger(byte targetBuffer[], dword bufferByteCount, dword signalValue, dword bitOffset, dword bitCount, dword msbFirst);
```

## Description

Inserts the given integer value into the given byte array.

## Return Values

This function returns a SensorErrorCode.

## Example

```c
  // Byte array used to prepare send data
  byte sendData[2] = {0x00, 0x00};

  // Insert an 6 bit integer with value 53, 4 bits offset and LSB first
  sensorInsertInteger(sendData, 2, 53, 4, 6, 0);

  // sendData is now {0x0A, 0xC0 }

  // Send the data via SPI
```

## Availability

| Since Version |
|---|
