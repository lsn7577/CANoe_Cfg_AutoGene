# Iso11783IL_PDDLoadDeviceDescription

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_PDDLoadDeviceDescription( char deviceCfgPath[] ); // form 1
long Iso11783IL_PDDLoadDeviceDescription( dbNode implement, char deviceCfgPath[] ); // form 2
```

## Description

The function creates a process data dictionary from a machine configuration file (XML).

## Parameters

| Name | Description |
|---|---|
| deviceCfgPath | filename of the machine configuration file The file must be located in the directory of the CANoe configuration. |
| implement | Simulation node to apply the function. |

## Example

```c
if (Iso11783IL_PDDLoadDeviceDescription( "Sprayer.XML" ) == 0) {
  Iso11783IL_PDDConnectEnvVar ( 0x0060, 1, "EvSprayer_TankVolume" );
  Iso11783IL_PDDConnectEnvVar ( 0x0048, 2, "EvSprayer_AppRatePerArea" );
}
else {
  write( "Error while load task file" );
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.0: form 1 9.0: form 2 | 13.0 | — | — | 2.1 |
| Restricted To | — | ISO11783 | ISO11783 | — | — | form 2 ISO11783 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1) | ✔ (form 1) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 2) | ✔ (form 2) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 2) | ✔ (form 2) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
