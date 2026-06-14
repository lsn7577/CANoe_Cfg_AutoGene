# Iso11783IL_PDDConnectEnvVar

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_PDDConnectEnvVar( dbSignal signal, dword elementNumber, char envVarName[] );
```

## Description

The function connects a process variable with an environment variable.

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

| Since Version |
|---|
