# sensorExtractInteger

> Category: `Sensor` | Type: `function`

## Syntax

```c
dword sensorExtractInteger(byte sourceBuffer[], dword bufferByteCount, dword& signalValue, dword bitOffset, dword bitCount, dword msbFirst);
```

## Description

Extracts an integer value from the given byte array.

## Return Values

This function returns a SensorErrorCode.

## Example

```c
  dword value;

  // This data could have been received via SPI
  byte receivedData[2] = {0xE9, 0x40};

  // Extract a 10 bit value from the data (offset 0, MSB first)
  sensorExtractInteger(receivedData, 2, value, 0, 10, 1);

  // value is now 933
```

## Availability

| Since Version |
|---|
