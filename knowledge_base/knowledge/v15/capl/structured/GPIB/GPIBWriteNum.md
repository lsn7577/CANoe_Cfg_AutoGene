# GPIBWriteNum

> Category: `GPIB` | Type: `function`

## Syntax

```c
long GPIBWriteNum (long deviceDescriptor, char cmdStr[], double value);
```

## Description

Writes cmdStr + numeric value to the device.

The function returns immediately and does not wait for the end of the command transmission.

## Parameters

| Name | Description |
|---|---|
| deviceDescriptor | Device ID |
| cmdStr | GPIB command |
| value | Numeric value of the parameter |

## Example

```c
Setting of a voltage of 1.23 V: GPIBWriteStr(myDev, "V", 1.23)
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.0 | — | — | — | 1.1 SP2 |
| Restricted To | — | GPIB | — | — | — | GPIB |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
