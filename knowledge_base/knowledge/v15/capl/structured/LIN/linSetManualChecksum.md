# linSetManualChecksum

> Category: `LIN` | Type: `function`

## Syntax

```c
void linSetManualChecksum(linFrame linFrame, byte csValue);
```

## Description

Sets a checksum (that is usually not a correct one) for a LIN frame.

## Parameters

| Name | Description |
|---|---|
| linFrame | LIN frame for which a checksum will be set. |
| csValue | The checksum value to be set. |

## Return Values

—

## Example

```c
...
linFrame MotorControl frmMotorControl;
linSetManualChecksum(frmMotorControl, 0x1A);
output(frmMotorControl); // it is important to call output() to make the changes active
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 6.0 | 6.0 | 13.0 | 13.0 | — | 1.0 |
| Restricted To | LIN | LIN | LIN | LIN | — | LIN |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | ✔ | — | N/A |
