# GNSSMakeName

> Category: `J1939` | Type: `function`

## Syntax

```c
void GNSSMakeName( word deviceName[8], dword selfConfigurable, dword industryGroup, dword deviceClassInstance, dword deviceClass, dword function, dword functionInstance, dword ECUInstance, dword manufacturerCode, dword identityNumber);
```

## Description

The function generates a J1939 device name. It must be transferred with a byte array of size 8. This array is filled with the device name.

## Return Values

—

## Example

```c
char name[8];
GNSSMakeName( 
 name, 1, 0, 0, 0, 28, 0, 0, 0, 0);
```

## Availability

| Since Version |
|---|
