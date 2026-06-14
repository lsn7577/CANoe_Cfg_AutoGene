# Iso11783PDDUpdateDeviceDescription

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783PDDUpdateDeviceDescription( dword ecuHandle, char deviceCfgPath [] );
```

## Description

The function updates the current device description object pool at runtime.

Only the device object and objects of type DeviceValuePresentation of the specified file are transmitted.

## Parameters

| Name | Description |
|---|---|
| ecuHandle | Handle of the ECU. The handle must be created with Iso11783CreateECU beforehand or ZERO for general parameters. |
| deviceCfgPath | File name of the device configuration file. The file must be located in the directory of the CANoe configuration. |

## Return Values

error code

## Example

```c
if (Iso11783PDDUpdateDeviceDescription( ecuHandle, "Sprayer01.XML" ) == 0) {
  // after  the device value presentation has changed to English
  // the designators are changed too
  Iso11783PDDChangeDesignator ( ecuHandle, 1, "Tank volume" );
  Iso11783PDDChangeDesignator ( ecuHandle, 2, "App rate per area" );
}
else {
  write( "Error while update file" );
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.1 | 13.0 | — | — | — |
| Restricted To | — | ISO11783 | ISO11783 | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
