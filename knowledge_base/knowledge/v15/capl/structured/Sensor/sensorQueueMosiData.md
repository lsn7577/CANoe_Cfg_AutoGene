# sensorQueueMosiData

> Category: `Sensor` | Type: `function`

## Syntax

```c
SensorErrorCode sensorQueueMosiData(char[] sysVarNamespace, byte buffer[], dword bitCount); // from 1
SensorErrorCode sensorQueueMosiData(char[] sysVarNamespace, byte buffer[], dword bitCount, dword delayNs); // from 2
```

## Description

This function is intended to be used for SPI master simulation. It inserts the given MOSI data into the send queue from the master to the given slave.

## Parameters

| Name | Description |
|---|---|
| sysVarNamespace | The namespace of the slave the data shall be queued for. |
| buffer | The array of bytes that shall be put into the masters send queue. The bytes of the array will be output in the order they are specified. The bits of the bytes will be output MSB first. Example: The byte array { 0xD1, 0x3B } will be output as 11010001 00111011. |
| bitCount | The length of the data in bits. Must be at least 2. |
| delayNs | If this parameter is provided, the master will wait the specified amount of time before actually sending the data. |

## Return Values

This function returns a SensorErrorCode.

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

sensorQueueMosiData(“SENSOR::SPI::ExampleChannel::ExampleSlave”, requestData, 12);
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
