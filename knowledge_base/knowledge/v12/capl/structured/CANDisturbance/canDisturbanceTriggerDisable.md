# canDisturbanceTriggerDisable

> Category: `CANDisturbance` | Type: `function`

## Syntax

```c
long canDisturbanceTriggerDisable (long deviceID);
```

## Description

Disables the currently configured trigger on the CAN Disturbance Interface.

If no trigger is configured for the device, the function also returns success.

## Return Values

1: Success

## Example

```c
on key '1'
{
long deviceID = @CANDisturbanceInterface1::DeviceNo;
CanDisturbanceTriggerDisable (deviceID);
}
```

## Availability

| Since Version |
|---|
