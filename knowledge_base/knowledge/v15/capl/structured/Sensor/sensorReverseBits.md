# sensorReverseBits

> Category: `Sensor` | Type: `function`

## Syntax

```c
SensorErrorCode sensorReverseBits(byte buffer[], dword bufferByteCount, dword bitCount);
```

## Description

Reverses the given number of bits in the given array.

## Parameters

| Name | Description |
|---|---|
| buffer | The array in which the bits shall be reversed. |
| bufferByteCount | The length of the array in bytes. |
| bitCount | The number of bits in the array that shall be reversed. |

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

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 10.0 | — | — | — | 2.2 |
| Restricted To | — | Sensor | — | — | — | Sensor |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
