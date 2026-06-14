# GNSSMakeName

> Category: `J1939` | Type: `function`

## Syntax

```c
void GNSSMakeName( word deviceName[8], dword selfConfigurable, dword industryGroup, dword deviceClassInstance, dword deviceClass, dword function, dword functionInstance, dword ECUInstance, dword manufacturerCode, dword identityNumber);
```

## Description

The function generates a J1939 device name. It must be transferred with a byte array of size 8. This array is filled with the device name.

## Parameters

| Name | Description |
|---|---|
| deviceName | Name of the device (determines the function) |
| selfConfigurable | Self-configurability of the device |
| industryGroup | Industry group |
| deviceClassInstance | Instance of a device class on the network |
| deviceClass | Device class |
| function | Function |
| functionInstance | Instance of a function on the network |
| ECUInstance | An ECU instance |
| manufacturerCode | Manufacturer of the device |
| identityNumber | Manufacturer-specific number |

## Return Values

—

## Example

```c
char name[8];
GNSSMakeName( 
 name, 1, 0, 0, 0, 28, 0, 0, 0, 0);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.2 | 13.0 | — | — | — |
| Restricted To | — | J1939 ISO11783 | J1939 ISO11783 | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
