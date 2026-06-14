# Iso11783IL_PDDConnectEnvVar

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_PDDConnectEnvVar( dbSignal signal, dword elementNumber, char envVarName[] );
long Iso11783IL_PDDConnectEnvVar( dword ddi, dword elementNumber, char envVarName[] );
```

## Description

The function connects a process variable with an environment variable.

## Parameters

| Name | Description |
|---|---|
| signal | signal from the database The attribute DDI must have been defined for the signal. The signal must be defined in the same database as the node ! |
| ddi | data dictionary identifier, 0x0000..0xFFFF |
| elementNumber | element number, 0x000..0xFFF |
| envVarName | name of the environment variable |

## Example

```c
if (Iso11783IL_PDDLoadDeviceDescription( "Sprayer.XML" ) == 0) {
Iso11783IL_PDDConnectEnvVar( 0x0060, 1, "EvSprayer_TankVolume" );
Iso11783IL_PDDConnectEnvVar( 0x0048, 2, "EvSprayer_AppRatePerArea" );
}
else {
  write( "Error while load task file" );
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.0 | 13.0 | — | — | — |
| Restricted To | — | ISO11783 | ISO11783 | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
