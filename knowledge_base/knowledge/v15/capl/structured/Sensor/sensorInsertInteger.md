# sensorInsertInteger

> Category: `Sensor` | Type: `function`

## Syntax

```c
SensorErrorCode sensorInsertInteger(byte targetBuffer[], dword bufferByteCount, dword signalValue, dword bitOffset, dword bitCount, dword msbFirst);
```

## Description

Inserts the given integer value into the given byte array.

## Parameters

| Name | Description |
|---|---|
| targetBuffer | The array in which the given value shall be inserted. |
| bufferByteCount | The length of the target array in bytes. |
| signalValue | The value that shall be inserted into the array. |
| bitOffset | The offset in bits at which the integer value shall be inserted into the byte array. |
| bitCount | The length of the value in bits (max. 32 is allowed). |
| msbFirst | This parameter controls in which order the bits of the value are inserted into the array. 1: the bits will be inserted from MSB to LSB. 0: the bits will be inserted from LSB to MSB. |

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
