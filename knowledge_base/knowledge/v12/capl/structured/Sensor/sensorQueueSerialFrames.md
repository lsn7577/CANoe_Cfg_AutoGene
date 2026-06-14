# sensorQueueSerialFrames

> Category: `Sensor` | Type: `function`

## Syntax

```c
SensorErrorCode sensorQueueSerialFrames(char[] sysVarNamespace, char[] data, dword dataCount);
```

## Return Values

This function returns a SensorErrorCode.

## Example

```c
// Send three frames with different payloads
dword data[3] = {0x01, 0x02, 0x03};
sensorQueueSerialFrames(“SENSOR::UART::ExampleChannel”, data, 3);
```

## Availability

| Since Version |
|---|
