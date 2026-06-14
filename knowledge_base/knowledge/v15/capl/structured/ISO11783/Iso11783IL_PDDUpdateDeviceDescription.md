# Iso11783IL_PDDUpdateDeviceDescription

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_PDDUpdateDeviceDescription( char deviceCfgPath [] ); // form 1
long Iso11783IL_PDDUpdateDeviceDescription( dbNode implement, char deviceCfgPath [] ); // form 2
```

## Description

The function updates the current device description object pool at runtime.

Only the device object and objects of type DeviceValuePresentation of the specified file are transmitted.

## Parameters

| Name | Description |
|---|---|
| deviceCfgPath | filename of the device configuration file The file must be located in the directory of the CANoe configuration. |
| implement | Simulation node to apply the function. |

## Return Values

error code

## Example

```c
if (Iso11783IL_PDDUpdateDeviceDescription( "Sprayer01.XML" ) == 0) {
  // after  the device value presentation has changed to English
  // the designators are changed too
  Iso11783IL_PDDChangeDesignator ( 1, "Tank volume" );
  Iso11783IL_PDDChangeDesignator ( 2, "App rate per area" );
}
else {
  write( "Error while update file" );
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.1: form 1 9.0: form 2 | 13.0 | — | — | 2.1 |
| Restricted To | — | ISO11783 | ISO11783 | — | — | form 2 ISO11783 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1) | ✔ (form 1) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 2) | ✔ (form 2) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 2) | ✔ (form 2) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
