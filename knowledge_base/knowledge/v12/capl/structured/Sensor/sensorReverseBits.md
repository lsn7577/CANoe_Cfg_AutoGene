# sensorReverseBits

> Category: `Sensor` | Type: `function`

## Syntax

```c
SensorErrorCode sensorReverseBits(byte buffer[], dword bufferByteCount, dword bitCount);
```

## Description

Reverses the given number of bits in the given array.

## Return Values

This function returns a SensorErrorCode.

## Example

```c
  // Byte array containing 10 bits of data in MSB first format
  byte sendData[2] = {0xE9, 0x40};

  // Convert to LSB first by reversing these 10 bits
  sensorReverseBits(sendData, 2, 10);

  // sendData is now {0xA5, 0xC0 }

  // Send the data via SPI
```

## Availability

| Since Version |
|---|
