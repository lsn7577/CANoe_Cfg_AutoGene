# sensorQueueSerialFrame

> Category: `Sensor` | Type: `function`

## Syntax

```c
SensorErrorCode sensorQueueSerialFrame(char[] sysVarNamespace, dword data);
```

## Return Values

This function returns a SensorErrorCode.

## Example

```c
// Send a single frame with payload "42"
sensorQueueSerialFrame(“SENSOR::UART::ExampleChannel”, 42);
```

## Availability

| Since Version |
|---|
