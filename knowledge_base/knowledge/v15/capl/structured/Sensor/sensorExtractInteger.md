# sensorExtractInteger

> Category: `Sensor` | Type: `function`

## Syntax

```c
dword sensorExtractInteger(byte sourceBuffer[], dword bufferByteCount, dword& signalValue, dword bitOffset, dword bitCount, dword msbFirst);
```

## Description

Extracts an integer value from the given byte array.

## Parameters

| Name | Description |
|---|---|
| sourceBuffer | The array from which the given value shall be extracted. |
| bufferByteCount | The length of the source array in bytes. |
| signalValue | The variable the extracted signal value will be written to. |
| bitOffset | The offset in bits at which the integer value shall be extracted from the byte array. |
| bitCount | The length of the value in bits (max. 32 is allowed). |
| msbFirst | This parameter controls in which order the bits are extracted from the array. 1: the bits will be extracted from MSB to LSB. 0: the bits will be extracted from LSB to MSB. |

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
