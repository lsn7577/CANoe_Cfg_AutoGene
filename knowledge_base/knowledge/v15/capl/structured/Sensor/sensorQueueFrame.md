# sensorQueueFrame

> Category: `Sensor` | Type: `function`

## Syntax

```c
SensorErrorCode sensorQueueFrame(char[] sysVarNamespace, byte buffer[], dword byteCount); // from 1
SensorErrorCode sensorQueueFrame(char[] sysVarNamespace, byte buffer[], dword byteCount, dword[] clockStretchNs); // from 2
```

## Description

This function is intended to be used for I2C slave simulation. It inserts the given data bytes into the response queue of the given slave.

## Parameters

| Name | Description |
|---|---|
| sysVarNamespace | The namespace of the slave the data shall be queued in. |
| buffer | The array of bytes that shall be put into the slave’s response queue. The bytes of the array will be output in the order they are specified. |
| byteCount | The length of the data in bytes. |
| clockStretchNs | Array of clock stretch values in ns for each of the data bytes. The length of this array must match the length of the data byte array. |

## Return Values

This method returns a SensorErrorCode.

## Example

```c
// Byte array used to prepare the slave's 12 bit response
byte responseData[2] = {0x42, 0x21};

// Queue the resonse in the slave
sensorQueueFrame("SENSOR::I2C::ExampleChannel::ExampleSlave", responseData, 2);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 11.0 SP3 | — | — | — | 3.0 SP2 |
| Restricted To | — | Sensor | — | — | — | Sensor |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
