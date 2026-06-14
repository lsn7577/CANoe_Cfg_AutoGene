# Iso11783PDDLoadDeviceDescription

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783PDDLoadDeviceDescription( dword ecuHandle, char deviceCfgPath[] );
```

## Description

The function creates a process data dictionary from a machine configuration file (XML).

## Return Values

Error code

## Example

```c
if (Iso11783PDDLoadDeviceDescription( ecuHandle, "Sprayer.XML" ) == 0) {
  Iso11783PDDConnectEnvVar ( ecuHandle, 0x0060, 1, "EvSprayer_TankVolume" );
  Iso11783PDDConnectEnvVar ( ecuHandle, 0x0048, 2, "EvSprayer_AppRatePerArea" );
}
else {
  write( "Error while load task file" );
}
```

## Availability

| Since Version |
|---|
