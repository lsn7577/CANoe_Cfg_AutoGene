# Iso11783PDDUpdateDeviceDescription

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783PDDUpdateDeviceDescription( dword ecuHandle, char deviceCfgPath [] );
```

## Description

The function updates the current device description object pool at runtime.

Only the device object and objects of type DeviceValuePresentation of the specified file are transmitted.

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

| Since Version |
|---|
