# QueueSerialFrame

> Category: `Sensor` | Type: `function`

## Syntax

```c
SensorErrorCode SysVarNamespace.QueueSerialFrame(dword data);
```

## Description

Queues one frame for the given datum.

## Return Values

This method returns a SensorErrorCode.

## Example

```c
// Send a single frame with payload "42"
sysvar::SENSOR::UART::ExampleChannel.QueueSerialFrame(42);
```

## Availability

| Since Version |
|---|
