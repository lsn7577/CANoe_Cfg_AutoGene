# CANstressGetInfo

> Category: `CANstress` | Type: `function`

## Syntax

```c
long CANstressGetInfo( char softwareVersion[], long swVersionBufLen, char firmwareVersion[], long fwVersionBufLen, char serialNumber[], long snBufLen, char canInterface1[], long if1BufLen, char canInterface2[], long if2BufLen );
```

## Description

Delivers information on CANstress software and the connected CAN hardware.

## Parameters

| Name | Description |
|---|---|
| softwareVersion | Buffer in which the version of the software is written (recommended buffer size: 20 Byte). |
| swVersionBufLen | Size of the buffer in which the software version is written (in bytes). |
| firmwareVersion | Buffer in which the version of the firmware is written (recommended buffer size: 10 Byte). |
| fwVersionBufLen | Size of the buffer in which the firmware version is written (in bytes). |
| serialNumber | Buffer in which the serial number of the CANstress hardware is written (recommended buffer size: 20 Byte). |
| snBufLen | Size of the buffer in which the hardware serial number is written (in bytes). |
| canInterface1 | Buffer in which the type of the CAN interface 1 of the CANstress hardware is written (recommended buffer size: 40 Byte). |
| if1BufLen | Size of the buffer in which the type of the CAN interface1 is written (in bytes). |
| canInterface2 | Buffer in which the type of the CAN interface 2 of the CANstress hardware is written (recommended buffer size: 40 Byte). |
| if2BufLen | Size of the buffer in which the type of the CAN interface 2 is written (in bytes). |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 6.0 | — | — | — | 1.1 |
| Restricted To | — | CAN CANstress | — | — | — | CAN CANstress |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
