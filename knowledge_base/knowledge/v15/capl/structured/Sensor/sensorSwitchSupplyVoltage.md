# sensorSwitchSupplyVoltage

> Category: `Sensor` | Type: `function`

## Syntax

```c
SensorErrorCode sensorSwitchSupplyVoltage(char[] sysVarNamespace, dword onOff);
```

## Description

Enables or disables the sensor supply voltage of a simulated ECU.

## Parameters

| Name | Description |
|---|---|
| sysVarNamespace | The namespace of the channel or ECU. |
| onOff | 1 = Supply voltage on 0 = Supply voltage off |

## Return Values

This function returns a SensorErrorCode.

## Example

```c
// Switch off the supply voltage of a simulated PSI5 ECU
sensorSwitchSupplyVoltage("SENSOR::PSI5::ECUSIM", 0);

// Switch off the supply voltage of a simulated SENT ECU
sensorSwitchSupplyVoltage("SENSOR::SENT::ECUSIM", 0);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 14 SP2 | — | — | — | 6 |
| Restricted To | — | Sensor | — | — | — | Sensor |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
