# QueuePsi5Frame

> Category: `Sensor` | Type: `function`

## Syntax

```c
SensorErrorCode SysVarNamespace.QueuePsi5Frame(Psi5SensorFrameStruct frame);
```

## Description

Inserts the given frame into the send queue of the given channel.

## Return Values

This method returns a SensorErrorCode.

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
frame.StartBits = 3; // Binary 11
frame.StartBitsCount = 2;
frame.DataRegionABits = 250;
frame.DataRegionABitsCount = 10;
frame.CrcBits = 0; // Will be set automatically
frame.CrcBitsCount = 3;

// Queue the frame for sending
sysvar::SENSOR::PSI5::ExampleChannel.QueuePsi5Frame(frame);
```

## Availability

| Since Version |
|---|
