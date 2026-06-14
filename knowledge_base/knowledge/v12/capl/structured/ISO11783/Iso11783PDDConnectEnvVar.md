# Iso11783PDDConnectEnvVar

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783PDDConnectEnvVar( dword ecuHandle, dbSignal signal, dword elementNumber, char envVarName[] );
```

## Description

The function connects a process variable with an environment variable.

## Return Values

Error code

## Example

```c
if (Iso11783PDDLoadDeviceDescription( ecuHandle, "Sprayer.XML" ) == 0) {
  Iso11783PDDConnectEnvVar( ecuHandle, 0x0060, 1, "EvSprayer_TankVolume" );
  Iso11783PDDConnectEnvVar( ecuHandle, 0x0048, 2, "EvSprayer_AppRatePerArea" );
}
else {
  write( "Error while load task file" );
}
```

## Availability

| Since Version |
|---|
