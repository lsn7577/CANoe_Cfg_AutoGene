# QueueMisoData

> Category: `Sensor` | Type: `method`

## Syntax

```c
SensorErrorCode SysVarNamespace.QueueMisoData(byte buffer[], dword bitCount);
```

## Description

This method is intended to be used for SPI slave simulation in basic mode. It inserts the given MISO data into the response queue of the given slave.

## Parameters

| Name | Description |
|---|---|
| buffer | The array of bytes that shall be put into the slave’s response queue. The bytes of the array will be output in the order they are specified. The bits of the bytes will be output MSB first. Example: The byte array { 0xD1, 0x3B } will be output as 11010001 00111011. |
| bitCount | The length of the data in bits. Must be at least 2. |

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
