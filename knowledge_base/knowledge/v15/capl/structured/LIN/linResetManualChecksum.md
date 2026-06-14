# linResetManualChecksum

> Category: `LIN` | Type: `function`

## Syntax

```c
void linResetManualChecksum(linFrame linFrame);
```

## Description

Sets the correct checksum of a LIN frame, whose checksum has been changed by using linSetManualChecksum() function. The checksum is calculated using the frame data.

## Parameters

| Name | Description |
|---|---|
| linFrame | LIN frame for which the correct checksum will be used again. |

## Return Values

—

## Example

Reset checksum error caused by previously called linSetManualChecksum()

```c
...
linFrame MotorControl frmMotorControl;
linResetManualChecksum(frmMotorControl);
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
