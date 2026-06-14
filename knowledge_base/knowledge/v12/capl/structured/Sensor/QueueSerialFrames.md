# QueueSerialFrames

> Category: `Sensor` | Type: `function`

## Syntax

```c
SensorErrorCode SysVarNamespace.QueueSerialFrames(char[] data, dword dataCount);
```

## Description

Queues one frame for each given datum.

## Return Values

This method returns a SensorErrorCode.

## Example

```c
// Send three frames with different payloads
dword data[3] = {0x01, 0x02, 0x03};
sysvar::SENSOR::UART::ExampleChannel.QueueSerialFrames(data, 3);
```

## Availability

| Since Version |
|---|
