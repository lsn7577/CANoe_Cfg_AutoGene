# sensorQueuePsi5Frame

> Category: `Sensor` | Type: `function`

## Syntax

```c
SensorErrorCode sensorQueuePsi5Frame(char[] sysVarNamespace, Psi5SensorFrameStruct frame);
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
Psi5SensorFrameStruct frame;

// Set bit 1 -> this frame will be the only frame sent in this cycle
frame.Frametype = (1 << 1);

// The frame will be sent 30µs after the sync pulse
frame.StartDelayUs = 30;

// Use automatic CRC calculation
frame.CrcMode = ePsi5AutoCrc;

// Fill the frame with data
frame.StartBits = 0; // Binary 00
frame.StartBitsCount = 2;
frame.DataRegionABits = 250;
frame.DataRegionABitsCount = 10;
frame.CrcBits = 0; // Will be set automatically
frame.CrcBitsCount = 3;

// Queue the frame for sending
sensorQueuePsi5Frame("SENSOR::PSI5::ExampleChannel", frame);
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
