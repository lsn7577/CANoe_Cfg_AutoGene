# Iso11783MakeName

> Category: `ISO11783` | Type: `function`

## Syntax

```c
void Iso11783MakeName( char[] retDeviceName, long selfConfiguring, long industryGroup, long deviceClassInstance, long deviceClass, long function, long functionInstance, long ECUInstance, long manufacturerCode, long identityNumber );
```

## Description

This function creates a Iso11783 device name.

The parameter retDeviceName must be an array with size 8. It will be filled with the device name.

## Parameters

| Name | Description |
|---|---|
| retDeviceName | Device name is copied in this buffer (must be 8 bytes) |

## Return Values

—

## Example

```c
char name[8];
Iso11783MakeName( name, 1, 2, 3, 4, 5, 6, 7, 8, 9);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 6.1 | 13.0 | — | — | — |
| Restricted To | — | Iso11783 | Iso11783 | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
