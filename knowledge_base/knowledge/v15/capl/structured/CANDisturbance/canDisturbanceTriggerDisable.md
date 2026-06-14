# canDisturbanceTriggerDisable

> Category: `CANDisturbance` | Type: `method`

## Syntax

```c
long canDisturbanceTriggerDisable(long deviceID);
```

## Description

Disables the currently configured trigger on the CAN Disturbance Interface.

If no trigger is configured for the device, the function also returns success.

## Parameters

| Name | Description |
|---|---|
| deviceID | The unique device ID of the configured trigger. |

## Example

```c
on key '1'
{
long deviceID = @CANDisturbanceInterface1::DeviceNo;
CanDisturbanceTriggerDisable (deviceID);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 10.0 10.0 SP3 recommended | — | — | — | 2.2 |
| Restricted To | — | CAN CAN Disturbance Interface | — | — | — | CAN CAN Disturbance Interface |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
