# sensorQueueSentFrame

> Category: `Sensor` | Type: `function`

## Syntax

```c
SensorErrorCode sensorQueueSentFrame(char[] sysVarNamespace, SentSensorFrameStruct frame);
```

## Description

Inserts the given frame into the send queue of the given channel.

## Parameters

| Name | Description |
|---|---|
| sysVarNamespace | The namespace of the channel the frame shall be queued in. |
| frame | Specifies the details of the frame that shall be inserted into the send queue. |

## Return Values

This function returns a SensorErrorCode.

## Example

```c
SentSensorFrameStruct frame;

// Use automatic CRC calculation
frame.CrcMode = eSentAutoCrc;

// Fill the frame with data
frame.StatusBits = 0;
frame.DataBits = 7;
frame.CrcBits = 0; // Will be set automatically

// Queue the frame for sending
sensorQueueSentFrame("SENSOR::SENT::ExampleChannel", frame);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 9.0 SP3 | — | — | — | 2.2 |
| Restricted To | — | Sensor | — | — | — | Sensor |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
