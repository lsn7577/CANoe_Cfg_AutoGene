# SwitchSupplyVoltage

> Category: `Sensor` | Type: `method`

## Syntax

```c
SensorErrorCode SysVarNamespace.SwitchSupplyVoltage(dword onOff);
```

## Description

Enables or disables the sensor supply voltage of a simulated ECU.

## Parameters

| Name | Description |
|---|---|
| onOff | 1 = Supply voltage on 0 = Supply voltage off |

## Return Values

This method returns a SensorErrorCode.

## Example

```c
// Switch off the supply voltage of a simulated PSI5 ECU
sysvar::SENSOR::PSI5::ECUSIM.SwitchSupplyVoltage(0);

// Switch off the supply voltage of a simulated SENT ECU
sysvar::SENSOR::SENT::ECUSIM.SwitchSupplyVoltage(0);
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
