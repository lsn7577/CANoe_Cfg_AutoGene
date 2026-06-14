# sensorQueueSerialMessage

> Category: `Sensor` | Type: `function`

## Syntax

```c
SensorErrorCode sensorQueueSerialMessage(char[] sysVarNamespace, dword messageId, dword useLongMessageId);
```

## Description

Inserts the given serial message into the send queue of the given time slot (PSI5)/channel (SENT).

Please note that the actual data of the message is not specified in this function call. Instead it will be taken from any signal system variables defined in the Sensor configuration dialog for this serial message ID.

## Return Values

This function returns a SensorErrorCode.

## Example

```c
// Send serial message with ID 15 (4 bit ID, 16 bit data)
sensorQueueSerialMessage("SENSOR::PSI5::ExampleChannel", 0x15, 0);
```

## Availability

| Since Version |
|---|
