# sensorQueueSentFrame

> Category: `Sensor` | Type: `function`

## Syntax

```c
SensorErrorCode sensorQueueSentFrame(char[] sysVarNamespace, SentSensorFrameStruct frame);
```

## Description

Inserts the given frame into the send queue of the given channel.

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

| Since Version |
|---|
